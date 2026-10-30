"""Homographen im Lexikon: getrennte Einträge oder Bedeutungen eines Eintrags? (B15, 2026-10-30)

Aufruf aus dem Repo-Wurzelverzeichnis:
  python knowledge/pruefskripte/homographen.py                 Zählungen
  python knowledge/pruefskripte/homographen.py --stichprobe N  zusätzlich N Einträge mit >=2 Bedeutungen,
                                                                gleich verteilt auf die Frequenzbänder aus
                                                                PROTOKOLL §4 (Belegsumme laut variants.xml),
                                                                als Markdown auf stdout (Seed fest)

Die Schicht nach Wortartzahl wurde verworfen: Einträge mit mehreren Wortarten sind in der Stichprobe
fast nur Verschmelzungen (PRO VRB wie `setzens`), keine Homographen.
"""
import argparse, collections, io, random, sys
from lxml import etree

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
NS = {"t": "http://www.tei-c.org/ns/1.0"}
X = "{http://www.w3.org/XML/1998/namespace}id"
SEED = 20261030

ap = argparse.ArgumentParser()
ap.add_argument("--stichprobe", type=int, default=0)
args = ap.parse_args()

lex = etree.parse("authority-files/lexicon.xml").getroot()
eintraege = []
for e in lex.iterfind(".//t:entry", NS):
    eintraege.append({
        "id": e.get(X),
        "orth": e.findtext('t:form[@type="lemma"]/t:orth', namespaces=NS),
        "pos": [p.text for p in e.findall("t:gramGrp/t:pos", NS)],
        "senses": [(s.get(X), (s.get("ana") or "").split(), [p.get("target").split("#")[1] for p in s.findall("t:ptr", NS)])
                   for s in e.findall("t:sense", NS)],
    })

# Bedeutungen tragen keine Wortart: nur xml:id, @ana und ptr
attr_sense = collections.Counter(a for s in lex.iterfind(".//t:sense", NS) for a in s.attrib)
kind_sense = collections.Counter(etree.QName(c).localname for s in lex.iterfind(".//t:sense", NS) for c in s)

nach_orth = collections.defaultdict(list)
for e in eintraege:
    nach_orth[e["orth"]].append(e)
mehrfach = {o: v for o, v in nach_orth.items() if len(v) > 1}
gleiche_pos = {o: v for o, v in mehrfach.items() if any(sum(p in x["pos"] for x in v) > 1 for p in {p for x in v for p in x["pos"]})}
poly = [e for e in eintraege if len(e["senses"]) >= 2]
poly_mpos = [e for e in poly if len(set(e["pos"])) >= 2]
poly_nom = [e for e in poly_mpos if "NOM" in e["pos"] and ({"ADJ", "VRB"} & set(e["pos"]))]

print("Einträge", len(eintraege), "| verschiedene Lemmaformen", len(nach_orth))
print("Lemmaformen mit >1 Eintrag", len(mehrfach), "| davon mit wiederholter Wortart", len(gleiche_pos))
print("Einträge mit >=2 Bedeutungen", len(poly), "| davon mit >=2 Wortarten", len(poly_mpos), "| davon NOM mit ADJ oder VRB", len(poly_nom))
print("Attribute an <sense>", dict(attr_sense), "| Kinder", dict(kind_sense))

if args.stichprobe:
    con = etree.parse("authority-files/concepts.xml").getroot()
    label = {c.get(X): c.findtext('t:catDesc/t:term[@{http://www.w3.org/XML/1998/namespace}lang="de"]', namespaces=NS) for c in con.iterfind(".//t:category", NS)}
    var = etree.parse("authority-files/variants.xml").getroot()
    form = {f.get(X): (f.text, int(f.get("n") or 0)) for f in var.iterfind(".//t:form", NS)}
    # Näherung: Belege des Lemmas über alle Wortarten, nicht des Paars aus Lemma und Wortart wie in PROTOKOLL §4
    freq = {e.get("corresp").split("#")[1]: sum(int(f.get("n") or 0) for f in e.iterfind("t:form", NS)) for e in var.iterfind(".//t:entry", NS)}
    baender = [("1-3", 1, 3), ("4-20", 4, 20), ("21-200", 21, 200), (">200", 201, float("inf"))]
    rnd = random.Random(SEED)
    k = args.stichprobe // len(baender)
    auswahl, groessen = [], []
    for name, lo, hi in baender:
        schicht = [e for e in poly if lo <= freq.get(e["id"], 0) <= hi]
        groessen.append(f"{name}: {len(schicht)}")
        auswahl += [(name, e) for e in rnd.sample(schicht, k)]
    ohne = sum(1 for e in poly if freq.get(e["id"], 0) == 0)
    print(f"\n# Stichprobe Homographen (Seed {SEED}; Einträge mit >=2 Bedeutungen je Band: {', '.join(groessen)}; ohne Beleg: {ohne})\n")
    for i, (schicht, e) in enumerate(auswahl, 1):
        print(f"## S{i:02d} `{e['orth']}` ({e['id']}, {' '.join(e['pos'])}; Band {schicht}, {freq.get(e['id'], 0)} Belege)\n")
        for sid, typen, ptr in e["senses"]:
            fs = sorted((form.get(t.lstrip("#"), ("?", 0)) for t in typen), key=lambda x: -x[1])
            belege = sum(n for _, n in fs)
            print(f"- {sid}: {' / '.join(label.get(p, p) for p in ptr)} | Formen ({belege} Belege): {', '.join(f'{f} {n}' for f, n in fs[:8])}")
        print()
