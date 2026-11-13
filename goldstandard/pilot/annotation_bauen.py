"""
Annotationsdatei für eine Person und eine Pilotrunde bauen (Protokoll, Abschnitte 5, 6 und 8).

Aufruf aus dem Repo-Wurzelverzeichnis:
    python goldstandard/pilot/annotation_bauen.py --kennung julia --runde 0
    python goldstandard/pilot/annotation_bauen.py --kennung alan --runde 0
    python goldstandard/pilot/annotation_bauen.py --kennung alan --runde 0 --ablauf direkt   (ohne eigene Lesart)

Ablauf "lesart-zuerst" (Standard im Pilot, Protokoll A31): pro Beleg zuerst eine eigene Lesart, erst dann die Karten.
"direkt": Karten sofort; nur für die Hauptrunde, falls Julia nach dem Pilot so entscheidet, und für den Browsertest.

Liest manifest-pilot.json und items-pilot.json (aus pilot_ziehen.py) und prüft, dass items-pilot.json
die Prüfsumme aus dem Manifest hat. Pro Person eine eigene Datei mit fest eingetragener Kennung
(kein Login, keine Namenseingabe). Itemreihenfolge pro Person und Runde gemischt, Kartenreihenfolge
pro Person und Item gemischt, beides aus dem Seed des Manifests abgeleitet und in der Datei
festgehalten. Die Datei enthält kein Silber, keine Typlisten und keine Token-Attribute; das prüft
das Skript vor dem Schreiben.

Ausgabe: goldstandard/pilot/bau/annotation-<kennung>-runde<n>.html (nicht im Repo, reproduzierbar)
"""

import argparse
import hashlib
import json
import random
import re
import sys
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

HIER = Path(__file__).resolve().parent
KENNUNGEN = ("julia", "alan")
RICHTLINIEN = "Kurzanleitung v0.3 vom 2026-11-13"

ap = argparse.ArgumentParser()
ap.add_argument("--kennung", required=True, choices=KENNUNGEN)
ap.add_argument("--runde", type=int, required=True)
ap.add_argument("--ablauf", choices=("lesart-zuerst", "direkt"), default="lesart-zuerst")
args = ap.parse_args()


def sha(b):
    return hashlib.sha256(b).hexdigest()


man_roh = (HIER / "manifest-pilot.json").read_bytes()
man = json.loads(man_roh)
items_roh = (HIER / "items-pilot.json").read_bytes()
if sha(items_roh) != man["pruefsummen"]["items-pilot.json"]:
    sys.exit("items-pilot.json passt nicht zum Manifest: pilot_ziehen.py neu ausführen")
bau = {b["item"]: b for b in json.loads(items_roh)}

runde = man.get(f"runde{args.runde}")
if not runde:
    sys.exit(f"Runde {args.runde} ist im Manifest nicht festgelegt")

seed = man["seed"]
reihe = sorted(runde)
random.Random(f"{seed}-{args.kennung}-runde{args.runde}").shuffle(reihe)
items = []
for iid in reihe:
    b = dict(bau[iid])
    del b["wortart"]   # kann aus dem Token-@pos stammen und verrät dann die Lesart (Review 2026-11-12)
    karten = list(b["karten"])
    random.Random(f"{seed}-{args.kennung}-{iid}").shuffle(karten)
    b["karten"] = karten
    items.append(b)

vorlage = (HIER / "annotation.template.html").read_text(encoding="utf-8")
werkzeug = sha(Path(__file__).read_bytes() + vorlage.encode("utf-8"))[:12]
daten = {"meta": {"kennung": args.kennung, "runde": args.runde, "korpus_commit": man["korpus_commit"],
                  "manifest_sha256": sha(man_roh), "richtlinien": RICHTLINIEN, "werkzeug": werkzeug,
                  "gebaut": date.today().isoformat(), "seed": seed,
                  "ablauf": args.ablauf, "lesart_zuerst": args.ablauf == "lesart-zuerst",
                  "itemreihenfolge": f"{seed}-{args.kennung}-runde{args.runde}",
                  "kartenreihenfolge": f"{seed}-{args.kennung}-<item>"},
         "items": items}
# Fingerprint nur über Inhalt und Herkunft, nicht über Baudatum und Werkzeug: Ein Neubau mit denselben
# Daten findet den Browserstand wieder und nimmt Sicherungen aus der ausgelieferten Datei an.
basis = {k: daten["meta"][k] for k in ("kennung", "runde", "korpus_commit", "manifest_sha256", "seed", "ablauf")}
daten["fingerprint"] = sha(json.dumps({"meta": basis, "items": items}, ensure_ascii=False, sort_keys=True).encode("utf-8"))

eingebettet = json.dumps(daten, ensure_ascii=False).replace("<", "\\u003c")
html = vorlage.replace("__DATEN__", eingebettet)

# Blindheit und Vertrag der Seite
for verboten in ('"ana"', "#type_", "lemmaRef", '"pos"', '"wortart"', "meaningRef", "http://", "https://"):
    assert verboten not in eingebettet, f"Leck in der Annotationsdatei: {verboten}"
assert not re.search(r"<(script|link)[^>]+(src|href)=", html), "externe Ressource in der Seite"
assert chr(0x2014) not in html, "Gedankenstrich in sichtbarem HTML"
assert html.count("__DATEN__") == 0

ziel = HIER / "bau" / f"annotation-{args.kennung}-runde{args.runde}{'' if args.ablauf == 'lesart-zuerst' else '-direkt'}.html"
ziel.parent.mkdir(exist_ok=True)
ziel.write_text(html, encoding="utf-8")
print(f"{ziel.relative_to(HIER.parents[1])}: {len(items)} Items, Fingerprint {daten['fingerprint'][:12]}, Werkzeug {werkzeug}")
