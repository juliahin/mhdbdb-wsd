"""
Entwurf der Obergattungsgruppen für den Gattungsausgleich (Protokoll, Abschnitt 4.8).

Aufruf aus dem Repo-Wurzelverzeichnis:
    python goldstandard/obergattungen_entwurf.py

Grundlage ist die MHDBDB-Textreihentypologie, wie sie im TEI-Header jedes Textes steht:
zu jeder exakten Textreihe (genreForm) eine eindeutige Herkunft (genreFormMainparent,
im Header <category ana="parent">). Über die Herkunft wird der Text im Baum von
genres.xml bis zur Ebene 1 unter den beiden Wurzeln verfolgt. genres.xml führt bei jeder
Kategorie auch Vorfahren als broader; die direkte Hierarchie entsteht erst durch
transitive Reduktion.

Ausgabe:
  goldstandard/obergattungen/texte.csv           Vorschlag pro Text zur Prüfung
  goldstandard/obergattungen/zusammenfassung.json Anteile, Zielanteile, Prüffälle
"""

from collections import Counter, defaultdict
from pathlib import Path
import csv
import json
import math
import re

from lxml import etree

TEI = "{http://www.tei-c.org/ns/1.0}"
XID = "{http://www.w3.org/XML/1998/namespace}id"
XLANG = "{http://www.w3.org/XML/1998/namespace}lang"
OUT = Path("goldstandard/obergattungen")
OUT.mkdir(parents=True, exist_ok=True)

# Entwurf: Ebene-1-Kategorie der Typologie -> Gruppe. Zu prüfen von Julia.
GRUPPE = {
    "Großepik": "Großepik",
    "Lyrik": "Lyrik",
    "Kurzdichtung": "Kurzdichtung",
    "Geistliche Literatur": "Geistliche Literatur",
    "Religiöser Gebrauchstext": "Geistliche Literatur",
    "Lehrdichtung": "Lehrdichtung",
    "Historiografie": "Historiografie",
    "Fachliteratur": "Fach- und Rechtsliteratur",
    "Rechtstext": "Fach- und Rechtsliteratur",
    "Reiseliteratur": "Fach- und Rechtsliteratur",
    "Dramatik": "Kurzdichtung",
    "Mediale Sonderform": None,   # Medium, kein Inhaltsbereich: nur maßgeblich, wenn sonst nichts da ist
}
# Vorrang bei mehreren Gruppen: Inhaltsbereiche vor Formen (Begründung im Entwurf)
VORRANG = ["Geistliche Literatur", "Fach- und Rechtsliteratur", "Historiografie", "Lehrdichtung",
           "Großepik", "Kurzdichtung", "Lyrik"]

# --- Typologie: transitive Reduktion von genres.xml ---
g = etree.parse("authority-files/genres.xml")
lab, par = {}, {}
for c in g.iter(f"{TEI}category"):
    i = c.get(XID)
    t = c.find(f"{TEI}catDesc/{TEI}term[@{XLANG}='de']")
    lab[i] = t.text.strip() if t is not None else i
    par[i] = [p.get("target").lstrip("#") for p in c.findall(f"{TEI}catDesc/{TEI}ptr[@type='broader']")]


def vorfahren(i, seen=None):
    seen = set() if seen is None else seen
    for p in par.get(i, []):
        if p not in seen:
            seen.add(p)
            vorfahren(p, seen)
    return seen


red = {i: [p for p in ps if not any(p in vorfahren(q) for q in ps if q != p)] for i, ps in par.items()}
wurzeln = {i for i, ps in red.items() if not ps}
ebene1 = {i for i, ps in red.items() if wurzeln & set(ps)}


def oben(i, seen=None):
    seen = set() if seen is None else seen
    for p in red.get(i, []):
        if p not in seen:
            seen.add(p)
            oben(p, seen)
    return seen


def e1(i):
    return {lab[x] for x in ({i} | oben(i)) & ebene1}


# --- Grundgesamtheit pro Text (wie Protokoll, Abschnitt 3) ---
lex = Path("authority-files/lexicon.xml").read_text(encoding="utf-8")
nsense = Counter(m.group(1) for m in re.finditer(r'<sense xml:id="(lemma_\d+)_sense_', lex))
lexpos = {m.group(1): re.findall(r"<pos>([^<]+)</pos>", m.group(2))
          for m in re.finditer(r'<entry xml:id="(lemma_\d+)">(.*?)</entry>', lex, re.S)}
aus = {r["xml_id"] for r in csv.DictReader(open("goldstandard/ausschluss/ausschluss-tokens.csv", encoding="utf-8"))
       if r["ausschluss"] == "ja"}
MAP = {"VEX": "VRB", "VEM": "VRB"}


def eindeutig(ps):
    s = {MAP.get(p, p) for p in ps}
    return s.pop() if len(s) == 1 else None


W = re.compile(r"<w\s[^>]*>")


def attr(t, k):
    m = re.search(r"\s" + k + r'="([^"]*)"', t)
    return m.group(1) if m else None


titel = {}
w = etree.parse("authority-files/works.xml")
for b in w.iter(f"{TEI}bibl"):
    tt = b.find(f"{TEI}title")
    for s in b.findall(f"{TEI}idno[@type='sigle']"):
        titel[s.text.strip()] = (tt.text or "").strip() if tt is not None else ""

rows = []
for f in sorted(Path("tei").glob("*.tei.xml")):
    sig = f.name[:-8]
    txt = f.read_text(encoding="utf-8")
    tax = re.search(r'<taxonomy xml:id="genres">(.*?)</taxonomy>', txt, re.S)
    cats = re.findall(r'<category xml:id="(genre_[0-9a-f]+)"( ana="parent")?', tax.group(1)) if tax else []
    herkunft = [c for c, a in cats if a]
    formen = [c for c, a in cats if not a]
    e1_h = set().union(*(e1(x) for x in herkunft)) if herkunft else set()
    weg = "herkunft"
    if not e1_h:                       # Herkunft ist selbst eine Wurzel (z. B. NBU)
        e1_h = set().union(*(e1(x) for x in formen)) if formen else set()
        weg = "form"
    gruppen = {GRUPPE[x] for x in e1_h if GRUPPE.get(x)}
    medium_only = not gruppen and "Mediale Sonderform" in e1_h
    if len(gruppen) == 1:
        haupt, regel = next(iter(gruppen)), "eindeutig"
    elif len(gruppen) > 1:
        haupt, regel = min(gruppen, key=VORRANG.index), "vorrang"
    else:
        haupt, regel = "", "pruefen"
    # Zieltokens und Silber
    ziel = sil = 0
    if sig != "WZB":
        for m in W.finditer(txt):
            t = m.group(0)
            lem = attr(t, "lemmaRef")
            if not lem:
                continue
            lid = lem.split("#")[-1]
            if nsense[lid] < 2 or attr(t, "xml:id") in aus:
                continue
            p = eindeutig(lexpos.get(lid, [])) or eindeutig((attr(t, "pos") or "").split())
            if p not in ("NOM", "VRB", "ADJ"):
                continue
            ziel += 1
            sil += bool(attr(t, "ana"))
    rows.append({
        "sigle": sig, "titel": titel.get(sig, ""), "zieltokens": ziel,
        "silberanteil": round(sil / ziel, 3) if ziel else "",
        "domaene": ("D1" if ziel and sil / ziel >= 0.9 else "D0") if ziel else "",
        "textreihen": "|".join(lab.get(x, x) for x in formen),
        "herkunft": "|".join(lab.get(x, x) for x in herkunft),
        "ebene1": "|".join(sorted(e1_h)), "weg": weg,
        "gruppen": "|".join(sorted(gruppen)), "hauptgruppe": haupt, "regel": regel,
        "nur_medium": "ja" if medium_only else "",
    })

with open(OUT / "texte.csv", "w", newline="", encoding="utf-8") as fh:
    cw = csv.DictWriter(fh, fieldnames=rows[0].keys())
    cw.writeheader()
    cw.writerows(rows)

# --- Anteile: anteilig (Text zählt 1/k in jeder seiner Gruppen) und nach Hauptgruppe ---
tot = sum(r["zieltokens"] for r in rows)
anteilig, haupt_t, texte, d1 = Counter(), Counter(), Counter(), Counter()
for r in rows:
    gs = r["gruppen"].split("|") if r["gruppen"] else ["(zu prüfen)"]
    for x in gs:
        anteilig[x] += r["zieltokens"] / len(gs)
    haupt_t[r["hauptgruppe"] or "(zu prüfen)"] += r["zieltokens"]
    texte[r["hauptgruppe"] or "(zu prüfen)"] += 1
    if r["domaene"] == "D1":
        d1[r["hauptgruppe"] or "(zu prüfen)"] += r["zieltokens"]
gruppen_alle = [x for x in VORRANG] + (["(zu prüfen)"] if "(zu prüfen)" in haupt_t else [])
wurzel = {x: math.sqrt(haupt_t[x] / tot) for x in gruppen_alle if haupt_t[x]}
sw = sum(wurzel.values())
tab = []
for x in gruppen_alle:
    if not haupt_t[x]:
        continue
    tab.append({
        "gruppe": x, "texte": texte[x],
        "anteil_hauptgruppe": round(haupt_t[x] / tot, 4),
        "anteil_anteilig": round(anteilig[x] / tot, 4),
        "zielanteil_wurzel": round(wurzel[x] / sw, 4),
        "erwartet_von_360": round(360 * wurzel[x] / sw, 1),
        "d1_anteil_der_gruppe": round(d1[x] / haupt_t[x], 3),
    })
summary = {
    "zieltokens": tot,
    "texte_nach_regel": dict(Counter(r["regel"] for r in rows)),
    "gruppen": tab,
    "vorrangfaelle": Counter(r["gruppen"] for r in rows if r["regel"] == "vorrang").most_common(),
    "pruefen": [(r["sigle"], r["titel"], r["textreihen"], r["herkunft"], r["zieltokens"]) for r in rows if r["regel"] == "pruefen"],
}
(OUT / "zusammenfassung.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
