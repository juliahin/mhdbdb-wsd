"""
Polysemie-Analyse für das Stichprobendesign des WSD-Goldstandards (MHDBDB).

Aufruf aus dem Repo-Wurzelverzeichnis (dort, wo tei/ und authority-files/ liegen):
    python polysemie_analyse.py

Was das Skript tut, und warum:
1. Ermittelt die vollständig disambiguierten Texte rechnerisch:
   jedes Token mit @lemmaRef trägt auch @ana. Das ist reproduzierbar und
   hängt nicht von einer gepflegten Siglenliste ab.
2. Zählt pro Lemma die Senses im Lexikon (Inventar) und die in diesen Texten
   tatsächlich belegten Senses (Korpus). Beide Zahlen werden verglichen, weil
   Inventar und Korpus auseinanderlaufen können.
3. Holt die Wortart pro Lemma aus lexicon.xml, nicht aus den Tokens
   (Token-@pos ist zu 28 % mehrdeutig und zu 8 % lemmaintern inkonsistent).
4. Schließt Lemmata mit disjunkten Token-@pos-Werten aus (vermutliche
   Lemmatisierungsfehler).
5. Gibt die Verteilungen aus, die für die 36 Zellen
   (Polysemiegrad x Wortart x Frequenzquartil) gebraucht werden, sowie
   den Anteil der dominanten Bedeutung pro Lemma (Schiefe der Verteilung,
   Stärke der Most-Frequent-Sense-Baseline).

Ergebnisse landen als CSV in polysemie_out/ und als Zusammenfassung auf stdout.
"""

from collections import Counter, defaultdict
from pathlib import Path
import csv
import re
import statistics

from lxml import etree

TEI_NS = "http://www.tei-c.org/ns/1.0"
NS = {"tei": TEI_NS}
W = f"{{{TEI_NS}}}w"

TEI_DIR = Path("tei")
LEXICON = Path("authority-files/lexicon.xml")
OUT = Path("polysemie_out")
OUT.mkdir(exist_ok=True)

TARGET_POS = {"NOM", "VRB", "ADJ"}
# Verb-Subklassen werden VRB zugeschlagen
POS_MAP = {"VEX": "VRB", "VEM": "VRB"}


def lemma_id(ref):
    """'lexicon.xml#lemma_879' -> 'lemma_879'"""
    return ref.split("#", 1)[-1] if ref else None


def sense_id(ref):
    return ref.split("#", 1)[-1] if ref else None


# ---------------------------------------------------------------------------
# 1. Lexikon einlesen: Senses und Wortart pro Lemma
# ---------------------------------------------------------------------------
print("Lese Lexikon ...")
lex_tree = etree.parse(str(LEXICON))
lex_senses = {}   # lemma_id -> Anzahl <sense>
lex_pos = {}      # lemma_id -> normalisierte Wortart oder None

# Die Struktur von lexicon.xml ist hier nicht exakt bekannt, daher tolerant:
# jeder Eintrag mit @xml:id 'lemma_*' zählt, Senses werden über die
# @xml:id-Konvention 'lemma_X_sense_Y' gezählt, die Wortart über ein
# beliebiges pos-artiges Element oder Attribut im Eintrag.
for entry in lex_tree.xpath("//*[starts-with(@xml:id, 'lemma_')]"):
    lid = entry.get("{http://www.w3.org/XML/1998/namespace}id")
    if "_sense_" in lid:
        continue
    senses = entry.xpath(".//*[contains(@xml:id, '_sense_')]")
    lex_senses[lid] = len(senses)

    pos_val = None
    # Kandidaten: <pos>, <gram type="pos">, @pos, <gramGrp><pos>
    cand = entry.xpath(
        ".//tei:pos/text() | .//tei:gram[@type='pos']/text() | @pos",
        namespaces=NS,
    )
    if cand:
        pos_val = str(cand[0]).strip()
    lex_pos[lid] = pos_val

print(f"  Lexikoneinträge: {len(lex_senses)}")
n_with_pos = sum(1 for p in lex_pos.values() if p)
print(f"  davon mit Wortart im Lexikon gefunden: {n_with_pos}")
if n_with_pos == 0:
    print("  ACHTUNG: Kein Wortart-Element erkannt. Bitte XPath in Abschnitt 1 "
          "an die tatsächliche Struktur von lexicon.xml anpassen. "
          "Fallback: häufigster Token-@pos.")


def norm_pos(raw):
    """'ADJ ADV' -> None (mehrdeutig), 'VEX' -> 'VRB', 'NOM' -> 'NOM'"""
    if not raw:
        return None
    parts = {POS_MAP.get(p, p) for p in raw.split()}
    return parts.pop() if len(parts) == 1 else None


# ---------------------------------------------------------------------------
# 2. Korpus durchlaufen
# ---------------------------------------------------------------------------
print("Lese Korpus ...")
per_text = {}                       # sigle -> (lemmatisiert, davon mit ana)
tok_pos_per_lemma = defaultdict(set)
tokens = []                         # (sigle, lemma, sense) nur aus vollst. Texten

# Erster Durchlauf: Vollständigkeit und Token-@pos-Muster
for f in sorted(TEI_DIR.glob("*.tei.xml")):
    n_lem = n_ana = 0
    for _, el in etree.iterparse(str(f), tag=W):
        lem = el.get("lemmaRef")
        if lem:
            n_lem += 1
            if el.get("ana"):
                n_ana += 1
            if el.get("pos"):
                tok_pos_per_lemma[lemma_id(lem)].add(el.get("pos"))
        el.clear()
    per_text[f.stem.replace(".tei", "")] = (n_lem, n_ana)

complete = {s for s, (l, a) in per_text.items() if l > 0 and l == a}
print(f"  Texte gesamt: {len(per_text)}, vollständig disambiguiert: {len(complete)}")

# Disjunkte @pos-Muster identifizieren (Lemmatisierungsverdacht)
disjoint = set()
for lid, vals in tok_pos_per_lemma.items():
    if len(vals) > 1:
        sets = [frozenset(v.split()) for v in vals]
        if not any(a < b for a in sets for b in sets):
            disjoint.add(lid)
print(f"  Lemmata mit disjunktem Token-@pos (ausgeschlossen): {len(disjoint)}")

# Zweiter Durchlauf: Tokens der vollständigen Texte einsammeln
for f in sorted(TEI_DIR.glob("*.tei.xml")):
    sigle = f.stem.replace(".tei", "")
    if sigle not in complete:
        continue
    for _, el in etree.iterparse(str(f), tag=W):
        lem = lemma_id(el.get("lemmaRef"))
        if lem:
            tokens.append((sigle, lem, sense_id(el.get("ana"))))
        el.clear()
print(f"  lemmatisierte Tokens in vollständigen Texten: {len(tokens)}")

with open(OUT / "vollstaendige_texte.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.writer(fh)
    w.writerow(["sigle", "tokens_lemmatisiert"])
    for s in sorted(complete):
        w.writerow([s, per_text[s][0]])

# ---------------------------------------------------------------------------
# 3. Kennzahlen pro Lemma
# ---------------------------------------------------------------------------
freq = Counter(lem for _, lem, _ in tokens)
sense_freq = defaultdict(Counter)
for _, lem, sense in tokens:
    sense_freq[lem][sense] += 1

# Fallback-Wortart aus Token-@pos, falls Lexikon nichts liefert
tok_pos_major = {}
for lid, vals in tok_pos_per_lemma.items():
    tok_pos_major[lid] = norm_pos(sorted(vals, key=len)[0])  # kürzester Wert

rows = []
for lem, n in freq.items():
    if lem in disjoint:
        continue
    pos = norm_pos(lex_pos.get(lem)) or tok_pos_major.get(lem)
    inv = lex_senses.get(lem, 0)
    attested = len(sense_freq[lem])
    dominant = sense_freq[lem].most_common(1)[0][1] / n
    rows.append({
        "lemma": lem,
        "pos": pos,
        "freq": n,
        "senses_inventar": inv,
        "senses_belegt": attested,
        "anteil_dominant": round(dominant, 3),
    })

# Frequenzquartile über die polysemen Ziel-Lemmata
target = [r for r in rows if r["pos"] in TARGET_POS and r["senses_inventar"] >= 2]
qs = statistics.quantiles([r["freq"] for r in target], n=4) if len(target) > 4 else []


def quartile(fq):
    if not qs:
        return None
    return 1 + sum(fq > q for q in qs)


def poly_class(k):
    return "1" if k < 2 else "2" if k == 2 else "3" if k == 3 else "4+"


for r in rows:
    r["freq_quartil"] = quartile(r["freq"]) if r in target else None
    r["polysemie_inventar"] = poly_class(r["senses_inventar"])
    r["polysemie_belegt"] = poly_class(r["senses_belegt"])

with open(OUT / "lemmata.csv", "w", newline="", encoding="utf-8") as fh:
    w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
    w.writeheader()
    w.writerows(rows)

# ---------------------------------------------------------------------------
# 4. Ausgabe
# ---------------------------------------------------------------------------
def dist(rows, key):
    c = Counter(r[key] for r in rows)
    return {k: c[k] for k in ["1", "2", "3", "4+"]}

print("\n=== Polysemiegrad, alle Lemmata der vollständigen Texte ===")
print("nach Inventar :", dist(rows, "polysemie_inventar"))
print("nach Belegung :", dist(rows, "polysemie_belegt"))

print("\n=== Ziel-Lemmata (NOM/VRB/ADJ, Inventar >= 2 Senses) ===")
print(f"Anzahl: {len(target)}, Frequenzquartil-Grenzen: {[round(q) for q in qs]}")

print("\n=== Zellenbesetzung: Polysemie (Inventar) x Wortart x Quartil ===")
print("Werte = Lemmata / Tokens")
cells = defaultdict(lambda: [0, 0])
for r in target:
    key = (r["polysemie_inventar"], r["pos"], r["freq_quartil"])
    cells[key][0] += 1
    cells[key][1] += r["freq"]
for p in ["2", "3", "4+"]:
    for pos in sorted(TARGET_POS):
        line = f"{p:>2} {pos}: "
        for q in [1, 2, 3, 4]:
            l, t = cells[(p, pos, q)]
            line += f"Q{q}={l:>4}/{t:>6}  "
        print(line)

print("\n=== Schiefe: Anteil der dominanten Bedeutung (Ziel-Lemmata) ===")
dom = [r["anteil_dominant"] for r in target]
for lo, hi in [(0, .5), (.5, .7), (.7, .9), (.9, 1.01)]:
    n = sum(lo <= d < hi for d in dom)
    print(f"  {lo:.1f}–{min(hi,1):.1f}: {n} Lemmata")
print(f"  Median: {statistics.median(dom):.2f}")
mfs = sum(r["freq"] * r["anteil_dominant"] for r in target) / sum(r["freq"] for r in target)
print(f"  Most-Frequent-Sense-Baseline (tokengewichtet): {mfs:.3f}")

print("\n=== Inventar vs. Belegung ===")
gap = sum(1 for r in target if r["senses_belegt"] < r["senses_inventar"])
print(f"  Ziel-Lemmata, bei denen nicht alle Inventar-Senses belegt sind: {gap} / {len(target)}")

print(f"\nDetails in {OUT}/lemmata.csv und {OUT}/vollstaendige_texte.csv")