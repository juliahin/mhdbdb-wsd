"""
Wirkung des Verschmelzungsausschlusses auf die Grundgesamtheit (Protokoll, Abschnitt 3).

Aufruf aus dem Repo-Wurzelverzeichnis (braucht die lokale goldstandard/ausschluss/ausschluss-tokens.csv):
    python goldstandard/verschmelzungen/wirkung.py

Abgrenzung der Grundgesamtheit wie in goldstandard/obergattungen_entwurf.py (ohne WZB und SBF).
Bänder nach Belegen in der Grundgesamtheit, nicht im ganzen Korpus.
"""
import sys, io, contextlib, csv, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")
from collections import Counter
from pathlib import Path
sys.argv = [sys.argv[0]]
src = open("goldstandard/verschmelzungen.py", encoding="utf-8").read().replace('sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")', '')
g = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(src, g)
V = set(g["treffer"])
lex = Path("authority-files/lexicon.xml").read_text(encoding="utf-8")
nsense = Counter(m.group(1) for m in re.finditer(r'<sense xml:id="(lemma_\d+)_sense_', lex))
lexpos = {m.group(1): re.findall(r"<pos>([^<]+)</pos>", m.group(2)) for m in re.finditer(r'<entry xml:id="(lemma_\d+)">(.*?)</entry>', lex, re.S)}
aus = {r["xml_id"] for r in csv.DictReader(open("goldstandard/ausschluss/ausschluss-tokens.csv", encoding="utf-8")) if r["ausschluss"] == "ja"}
MAP = {"VEX": "VRB", "VEM": "VRB"}
def eindeutig(ps):
    s = {MAP.get(p, p) for p in ps}; return s.pop() if len(s) == 1 else None
def attr(t, k):
    m = re.search(r"\s" + k + r'="([^"]*)"', t); return m.group(1) if m else None
W = re.compile(r"<w\s[^>]*>")
tot = vt = 0; vl = Counter(); en = 0; enl = set(); paare = set(); vpaare = set(); lem = set()
for f in sorted(Path("tei").glob("*.tei.xml")):
    sig = f.name[:-8]
    if sig in ("WZB", "SBF"): continue
    for m in W.finditer(f.read_text(encoding="utf-8")):
        t = m.group(0); l = attr(t, "lemmaRef")
        if not l: continue
        lid = l.split("#")[-1]
        if nsense[lid] < 2 or attr(t, "xml:id") in aus: continue
        p = eindeutig(lexpos.get(lid, [])) or eindeutig((attr(t, "pos") or "").split())
        if p not in ("NOM", "VRB", "ADJ"): continue
        tot += 1; paare.add((lid, p)); lem.add(lid)
        if lid in V:
            vt += 1; vl[lid] += 1; vpaare.add((lid, p))
            if g["E"][lid]["orth"].lower().startswith("en") and "N" in g["treffer"][lid]: en += 1; enl.add(lid)
print("Grundgesamtheit", tot, "Paare", len(paare), "Lemmata", len(lem))
print("Verschmelzungs-Tokens", vt, f"{vt/tot:.2%}", "Lemmata", len(vl), "Paare", len(vpaare))
print("davon en-Formen: Tokens", en, "Lemmata", len(enl))
b = Counter(("1-3" if n <= 3 else "4-20" if n <= 20 else "21-200" if n <= 200 else ">200") for n in vl.values())
print("Verschmelzungs-Lemmata nach Band (Belege in der Grundgesamtheit):", dict(b))
print("häufigste:", [(g["E"][i]["orth"], n) for i, n in vl.most_common(8)])
