"""
Ziehung der zweiten blinden Prüfrunde für goldstandard/verschmelzungen.py (2026-10-30).

Aufruf aus dem Repo-Wurzelverzeichnis:
    python goldstandard/verschmelzungen/runde2_ziehen.py

Gezogen wird mit der endgültigen Regel: 40 Treffer und 40 Nicht-Treffer mit Funktionswort unter den
Bestandteilen, beide nur aus Einträgen mit mindestens 2 Bedeutungen und ohne die 80 Einträge der
ersten Runde (runde1-schluessel.txt; die erste Runde lief mit der Regel vor dem Nachschärfen).
Seed 20261031. Schreibt runde2-pruefliste.md (ging an die prüfende Instanz) und runde2-schluessel.txt.
"""

import io, contextlib, random, re, sys
from pathlib import Path

D = Path("goldstandard/verschmelzungen")
SEED = 20261031

sys.argv = [sys.argv[0]]
src = Path("goldstandard/verschmelzungen.py").read_text(encoding="utf-8").split("if args.stichprobe:")[0]
src = src.replace('sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")', "")
ns = {}
with contextlib.redirect_stdout(io.StringIO()):
    exec(src, ns)
E, treffer, poly, F = ns["E"], ns["treffer"], ns["poly"], ns["FUNKTION"]

alt = {m.group(1) for l in open(D / "runde1-schluessel.txt", encoding="utf-8") if (m := re.search(r"(lemma_\d+)", l))}
rnd = random.Random(SEED)
pos = sorted((treffer.keys() & poly) - alt)
neg = sorted(i for i in poly - treffer.keys() - alt if any(E.get(k) and E[k]["pos"] & F for k in E[i]["teile"]))
auswahl = rnd.sample(pos, 40) + rnd.sample(neg, 40)
rnd.shuffle(auswahl)

with open(D / "runde2-pruefliste.md", "w", encoding="utf-8") as f:
    f.write("| Nr. | Lemma | ID | Wortarten | Bestandteile |\n|---|---|---|---|---|\n")
    for n, i in enumerate(auswahl, 1):
        e = E[i]
        teile = ", ".join(f"{E[k]['orth']} ({' '.join(sorted(E[k]['pos']))})" for k in e["teile"] if k in E)
        f.write(f"| {n} | {e['orth']} | {i} | {' '.join(sorted(e['pos']))} | {teile} |\n")
with open(D / "runde2-schluessel.txt", "w", encoding="utf-8") as f:
    for n, i in enumerate(auswahl, 1):
        f.write(f"{n} {i} {'Treffer' if i in treffer else 'kein Treffer'}\n")
print("Grundmengen:", len(pos), "Treffer,", len(neg), "Nicht-Treffer mit Funktionswort")
