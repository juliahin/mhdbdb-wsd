"""
Verschmelzungen erkennen (Ausschluss, Entscheidung Julia 2026-10-30; Befund in knowledge/data.md, B15).

Aufruf aus dem Repo-Wurzelverzeichnis:
    python goldstandard/verschmelzungen.py                  Zählungen
    python goldstandard/verschmelzungen.py --stichprobe N   zusätzlich eine blinde Prüfliste: N Einträge mit
                                                            Treffer und N ohne Treffer, aber mit einem
                                                            Funktionswort unter den Bestandteilen

Eine Verschmelzung (Klise, Kontraktion) ist ein Lemma wie `sîhez` (sîhe + ez), `stoufes` (des + toufes),
`enwellen` (en + wellen) oder `zedienest` (ze + dienest). Das Lexikon führt sie als eigene Einträge, die
Bedeutungen des Grundworts samt Typlisten übernehmen. Erkannt wird über die verlinkten Bestandteile in
<etym type="morphological">:
  P  ein Bestandteil hat die Wortart PRO (klitisches Pronomen: ez, er, sie, dû, ich ...)
  A  ein Bestandteil hat die Wortart ART, aber nicht NUM (Artikel; `ein` bleibt außen vor)
  N  Bestandteil `niht` und die Form beginnt mit en- oder n-, aber nicht mit ent- (proklitische Negation;
     un- und ent- sind Präfixe, das Lexikon verlinkt bei ihnen trotzdem `niht`)
  Z  Bestandteil `zuo` und die Form beginnt mit z, aber nicht mit zuo oder zu (Partikelverb wie zugesellen),
     außer zun- (proklitisches ze vor un-, wie zunguot)
  U  Bestandteil `und` und die Form endet auf -unde oder -und (angehängte Konjunktion)

Geprüft am 2026-10-30 in zwei blinden Runden zu je 80 Einträgen (je 40 Treffer und Nicht-Treffer mit
Funktionswort). Runde 1 (Seed 20261030) lief mit der Regel davor; N, Z und U wurden an ihren Fehlern
nachgeschärft. Runde 2 (Seed 20261031, neue Einträge, `verschmelzungen/runde2_ziehen.py`) misst die Regel
in dieser Fassung. Listen, Schlüssel und Urteile in goldstandard/verschmelzungen/, Ergebnis im Protokoll
(Abschnitt 3) und in knowledge/data.md. Alle Formen auf en- mit Bestandteil `niht` gelten als
Verschmelzung, auch wenn ein verkürztes ent- gemeint sein könnte (Entscheidung Julia 2026-10-30).
"""

import argparse, collections, io, random, sys
from lxml import etree

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
NS = {"t": "http://www.tei-c.org/ns/1.0"}
X = "{http://www.w3.org/XML/1998/namespace}id"
SEED = 20261030
FUNKTION = {"PRO", "ART", "NEG", "PRP", "CNJ"}

ap = argparse.ArgumentParser()
ap.add_argument("--stichprobe", type=int, default=0)
args = ap.parse_args()

E = {}
for e in etree.parse("authority-files/lexicon.xml").getroot().iterfind(".//t:entry", NS):
    E[e.get(X)] = {
        "orth": e.findtext("t:form/t:orth", namespaces=NS) or "",
        "pos": {p.text for p in e.findall("t:gramGrp/t:pos", NS)},
        "teile": [s.get("corresp").split("#")[1] for s in e.findall("t:etym/t:seg", NS)],
        "senses": len(e.findall("t:sense", NS)),
    }


def gruende(e):
    o = e["orth"].lower()
    g = set()
    for k in e["teile"]:
        t = E.get(k)
        if not t:
            continue
        if "PRO" in t["pos"]:
            g.add("P")
        if "ART" in t["pos"] and "NUM" not in t["pos"]:
            g.add("A")
        if t["orth"] == "niht" and (o.startswith("en") or o.startswith("n")) and not o.startswith("ent"):
            g.add("N")
        if t["orth"] == "zuo" and o.startswith("z") and not o.startswith("zuo")                 and not (o.startswith("zu") and not o.startswith("zun")):
            g.add("Z")
        if t["orth"] == "und" and (o.endswith("unde") or o.endswith("und")) and o != t["orth"]:
            g.add("U")
    return g


treffer = {i: gruende(e) for i, e in E.items()}
treffer = {i: g for i, g in treffer.items() if g}
poly = {i for i, e in E.items() if e["senses"] >= 2}
print("Einträge", len(E), "| Treffer", len(treffer), "| davon mit >=2 Bedeutungen", len(treffer.keys() & poly))
print("nach Grund (mehrere möglich):", dict(collections.Counter(x for g in treffer.values() for x in g)))

if args.stichprobe:
    rnd = random.Random(SEED)
    pos = sorted(treffer.keys() & poly)
    neg = sorted(i for i in poly - treffer.keys()
                 if any(E.get(k) and E[k]["pos"] & FUNKTION for k in E[i]["teile"]))
    auswahl = rnd.sample(pos, args.stichprobe) + rnd.sample(neg, args.stichprobe)
    rnd.shuffle(auswahl)
    print(f"\n# Prüfliste Verschmelzungen (Seed {SEED}; Grundmengen: {len(pos)} Treffer, {len(neg)} Nicht-Treffer mit Funktionswort)\n")
    print("| Nr. | Lemma | ID | Wortarten | Bestandteile |")
    print("|---|---|---|---|---|")
    for n, i in enumerate(auswahl, 1):
        e = E[i]
        teile = ", ".join(f"{E[k]['orth']} ({' '.join(sorted(E[k]['pos']))})" for k in e["teile"] if k in E)
        print(f"| {n} | {e['orth']} | {i} | {' '.join(sorted(e['pos']))} | {teile} |")
    print("\n<!-- Schlüssel (nicht an die prüfende Person geben):")
    for n, i in enumerate(auswahl, 1):
        print(f"{n} {i} {'Treffer ' + ''.join(sorted(treffer[i])) if i in treffer else 'kein Treffer'}")
    print("-->")
