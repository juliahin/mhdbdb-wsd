"""Itemmengen der Pilotrunden 1 bis 3 (Protokoll, Abschnitt 7, Schritt 2; A32).

Aufruf aus der Wurzel des Repos (schreibt pilot/runden-pilot.json):

    python -X utf8 goldstandard/pilot/runden.py

Runde 0 steht im eingefrorenen Manifest (`manifest-pilot.json`, A30) und bleibt dort. Die Runden 1 bis 3
werden aus den übrigen Items des Pools gezogen, je 25, einfache Zufallsauswahl wie Runde 0, nacheinander
aus dem jeweiligen Rest mit den Seeds `<seed>-runde1` bis `<seed>-runde3`; der Rest ist Reserve
(Entscheidung Julia Hintersteiner, 2026-11-26). Das Manifest wird nicht verändert: Die Rundendatei trägt
seine Prüfsumme und gilt nur zusammen mit ihm.

`annotation_bauen.py` und `auswerten.py` holen die Items einer Runde über `items_der_runde()`.
"""
import hashlib
import json
import random
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
SCHEMA = "wsd-goldstandard-pilot-runden-v1"
RUNDEN = (1, 2, 3)
RUNDE_N = 25


def _sha(b):
    return hashlib.sha256(b).hexdigest()


def ziehen(manifest):
    """Runde 1 bis 3 aus dem Pool ohne Runde 0, deterministisch aus dem Seed des Manifests."""
    seed = manifest["seed"]
    rest = sorted(set(i["item"] for i in manifest["items"]) - set(manifest["runde0"]))
    runden = {}
    for n in RUNDEN:
        gezogen = sorted(random.Random(f"{seed}-runde{n}").sample(rest, RUNDE_N))
        runden[f"runde{n}"] = gezogen
        rest = [i for i in rest if i not in gezogen]
    return runden, rest


def items_der_runde(n, man_roh):
    """Item-IDs der Runde n; Runde 0 aus dem Manifest, ab Runde 1 aus runden-pilot.json (Prüfsumme geprüft)."""
    manifest = json.loads(man_roh)
    if n == 0:
        return manifest.get("runde0")
    pfad = HIER / "runden-pilot.json"
    if not pfad.exists():
        return None
    r = json.loads(pfad.read_text(encoding="utf-8"))
    if r.get("schema") != SCHEMA or r.get("manifest_sha256") != _sha(man_roh):
        sys.exit("runden-pilot.json passt nicht zu manifest-pilot.json: runden.py neu ausführen")
    return r.get(f"runde{n}")


def runden_sha():
    pfad = HIER / "runden-pilot.json"
    return _sha(pfad.read_bytes()) if pfad.exists() else None


if __name__ == "__main__":
    man_roh = (HIER / "manifest-pilot.json").read_bytes()
    manifest = json.loads(man_roh)
    runden, reserve = ziehen(manifest)
    alle = [i for n in RUNDEN for i in runden[f"runde{n}"]] + reserve + manifest["runde0"]
    assert sorted(alle) == sorted(i["item"] for i in manifest["items"]), "Runden decken den Pool nicht disjunkt ab"
    aus = {"schema": SCHEMA,
           "komponente": "Pilotrunden 1 bis 3 (Protokoll, Abschnitt 7, Schritt 2; A32)",
           "manifest_sha256": _sha(man_roh),
           "skript": "goldstandard/pilot/runden.py",
           "regel": f"je {RUNDE_N} Items, einfache Zufallsauswahl ohne Runde 0, nacheinander aus dem Rest, "
                    f"Seeds '{manifest['seed']}-runde1' bis '-runde3'; Rest ist Reserve",
           "entscheidung": "Julia Hintersteiner, 2026-11-26 (Auswahldialog: einfach zufällig, wie Runde 0)",
           **runden,
           "reserve": reserve}
    (HIER / "runden-pilot.json").write_text(json.dumps(aus, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print("runden-pilot.json:", ", ".join(f"Runde {n} {len(runden[f'runde{n}'])}" for n in RUNDEN),
          f"| Reserve {len(reserve)} | Prüfsumme {runden_sha()[:12]}")
