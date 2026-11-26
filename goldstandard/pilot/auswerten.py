"""Übereinstimmung einer Pilotrunde aus zwei JSON-Exporten der Annotationsseite (Protokoll, Abschnitte 7 und 9.1).

Aufruf aus der Wurzel des Repos:

    python -X utf8 goldstandard/pilot/auswerten.py <export-julia.json> <export-alan.json> [--bericht <pfad.md>]

Auf die Konsole gehen nur Kennzahlen, nie ein Label, eine Item-ID, ein Lemma oder eine Sense-ID
(Protokoll, Abschnitt 10, A37: auch nicht in eine KI-Sitzung). Das Skript prüft die eigene Ausgabe darauf
und bricht ab, statt ein Leck zu drucken.

Was gerechnet wird:
- **Ganzes Label** (Maß der Stoppregel, A32): Status und Menge der gewählten Karten, exakt. Krippendorffs
  α nominal und Rohübereinstimmung mit 95-%-Wilson-Intervall, auf den Items, die beide gültig festgehalten haben.
  Ab Runde 1 dazu das Ergebnis der Stoppregel; es gilt nur, wenn beide alle Items der Runde festgehalten haben.
- **Statusebene:** Konfusionstabelle der sechs Status (Häufigkeiten).
- **Sense-Ebene** (Abschnitt 9.1): α mit MASI-Distanz d = 1 − J·M (A33), α nominal, Rohübereinstimmung exakt
  und „Überschneidung“. Einheiten sind die Items, bei denen beide `SENSE`, `MEHRERE`, `KEINE_PASST` oder
  `LEMMA_FALSCH` vergeben haben; `KEINE_PASST` und `LEMMA_FALSCH` zählen als eigene Kategorien, also als Menge
  {KEINE_PASST} bzw. {LEMMA_FALSCH} (A41, A42, Entscheidungen Julia Hintersteiner, 2026-11-20).
  `KONTEXT_UNZUREICHEND` und `TEXT_DEFEKT` sind fehlende Werte.
- Häufigkeiten von Sicherheit, erweitertem Kontext und Lesart je Person.

Nicht gerechnet (für die Hauptrunde, nicht für 15 oder 25 Pilotitems): Zufallsmodell pro Lemma, AC1,
Bootstrap nach Text, Aufschlüsselungen (Abschnitt 9.1, Punkte 3 bis 6).

Die Antworten werden aus dem Ereignisprotokoll neu abgeleitet, genau wie `ableiten()` in der Seite, und
gegen die im Export mitgelieferten Endstände geprüft. Ein Item zählt nur, wenn es festgehalten ist.

`--bericht` schreibt das Material für die Besprechung (beide Labels je Item, Lesarten, Kommentare) als
Markdown für die Menschen. Der Pfad muss außerhalb jedes Worktrees dieses Repos liegen (`git worktree list`),
weil der Fork öffentlich ist; die
Datei wird nicht auf der Konsole gezeigt. Erst rechnen, dann besprechen (Abschnitt 7, Schritt 5).
"""
import argparse
import hashlib
import json
import math
import re
import subprocess
import sys
from collections import Counter
from fractions import Fraction
from pathlib import Path

from runden import items_der_runde, runden_sha

HIER = Path(__file__).resolve().parent
SCHEMA = "wsd-goldstandard-pilot-export-v1"
KENNUNGEN = ("julia", "alan")
STATUS = ("SENSE", "MEHRERE", "KEINE_PASST", "LEMMA_FALSCH", "KONTEXT_UNZUREICHEND", "TEXT_DEFEKT")
SENSE_EBENE = {"SENSE", "MEHRERE", "KEINE_PASST", "LEMMA_FALSCH"}   # Abschnitt 9.1, A41, A42
EIGENE_KATEGORIE = {"KEINE_PASST", "LEMMA_FALSCH"}                    # gehen als Menge {Status} ein
AENDERUNG = {"status": "status", "karten": "senses", "karten_geleert": "senses", "begriffe": "begriffe",
             "begriffe_geleert": "begriffe", "sicherheit": "sicherheit", "kommentar": "kommentar"}
SICHER = ("sicher", "eher_sicher", "unsicher")


# --- Maße -----------------------------------------------------------------------------------------

def masi(a, b):
    """MASI-Distanz 1 - J*M nach Passonneau 2006 (Protokoll 9.1, A33), exakt als Bruch."""
    a, b = frozenset(a), frozenset(b)
    if not a and not b:
        return Fraction(0)
    j = Fraction(len(a & b), len(a | b))
    if a == b:
        m = Fraction(1)
    elif a <= b or b <= a:
        m = Fraction(2, 3)
    elif a & b:
        m = Fraction(1, 3)
    else:
        m = Fraction(0)
    return 1 - j * m


def nominal(a, b):
    return Fraction(0) if a == b else Fraction(1)


def alpha(paare, d):
    """Krippendorffs α für zwei Kodierende ohne fehlende Werte innerhalb der Einheiten.

    D_o = (1/n) Σ_u 2·d(a_u, b_u), D_e = 1/(n(n-1)) Σ_{i≠j} d(v_i, v_j) über alle n = 2N Werte.
    Gibt None zurück, wenn es keine Einheit gibt oder D_e = 0 ist (alle Werte gleich: α nicht definiert).
    """
    if not paare:
        return None
    werte = [w for p in paare for w in p]
    n = len(werte)
    d_o = Fraction(sum(2 * d(a, b) for a, b in paare), n)
    d_e = Fraction(sum(d(werte[i], werte[j]) for i in range(n) for j in range(n) if i != j), n * (n - 1))
    if d_e == 0:
        return None
    return float(1 - d_o / d_e)


def wilson(k, n, z=1.959963984540054):
    if n == 0:
        return None
    p = k / n
    nenner = 1 + z * z / n
    mitte = (p + z * z / (2 * n)) / nenner
    halb = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / nenner
    return mitte - halb, mitte + halb


# --- Exporte lesen ---------------------------------------------------------------------------------

def ableiten(ereignisse, item_ids):
    """Spiegel von ableiten() in annotation.template.html: Ereignisse in Protokollreihenfolge anwenden."""
    a = {i: {"status": None, "senses": [], "begriffe": [], "sicherheit": None, "kommentar": "",
             "festgehalten": False, "aufgedeckt": False, "lesart": None} for i in item_ids}
    for e in ereignisse:
        x = a.get(e.get("item"))
        if x is None:
            continue
        akt = e.get("aktion")
        if akt in AENDERUNG:
            x[AENDERUNG[akt]] = e.get("wert")
            x["festgehalten"] = False
        elif akt == "festgehalten":
            x["festgehalten"] = True
        elif akt == "karten_aufgedeckt" and not x["aufgedeckt"]:
            x["aufgedeckt"] = True
            x["lesart"] = e.get("wert")
    return a


def gueltig(x, lesart_zuerst):
    """Spiegel von pruefe() in der Seite."""
    if lesart_zuerst and not x["aufgedeckt"]:
        return False
    s, k = x["status"], x["senses"] or []
    if s not in STATUS or not x["sicherheit"]:
        return False
    if s == "SENSE" and len(k) != 1:
        return False
    if s == "MEHRERE" and len(k) < 2:
        return False
    if s in ("LEMMA_FALSCH", "TEXT_DEFEKT") and not (x["kommentar"] or "").strip():
        return False
    return True


def lade(pfad, manifest, manifest_sha, man_roh):
    try:
        exp = json.loads(Path(pfad).read_text(encoding="utf-8"))
    except (OSError, ValueError) as f:
        sys.exit(f"{pfad}: nicht lesbar ({type(f).__name__})")
    if exp.get("schema") != SCHEMA:
        sys.exit(f"{pfad}: kein Export der Pilotseite (schema {exp.get('schema')!r})")
    meta = exp.get("meta") or {}
    if meta.get("kennung") not in KENNUNGEN:
        sys.exit(f"{pfad}: unbekannte Kennung")
    if meta.get("manifest_sha256") != manifest_sha:
        sys.exit(f"{pfad}: Manifest-Prüfsumme passt nicht zu manifest-pilot.json (falsche Runde oder alter Stand)")
    if meta.get("korpus_commit") != manifest["korpus_commit"]:
        sys.exit(f"{pfad}: Korpus-Commit passt nicht zum Manifest")
    runde = meta.get("runde")
    soll = items_der_runde(runde, man_roh) if isinstance(runde, int) else None
    if not soll:
        sys.exit(f"{pfad}: Runde {runde} ist weder im Manifest noch in runden-pilot.json festgelegt")
    if runde and meta.get("runden_sha256") != runden_sha():
        sys.exit(f"{pfad}: Prüfsumme von runden-pilot.json passt nicht zum Export")
    ids = [i.get("item") for i in exp.get("items") or []]
    if sorted(ids) != sorted(soll):
        sys.exit(f"{pfad}: Items des Exports passen nicht zur Runde {runde} in {'runden-pilot.json' if runde else 'manifest-pilot.json'}")
    abgeleitet = ableiten(exp.get("ereignisse") or [], ids)
    abweichend = 0
    for i in exp["items"]:
        x = abgeleitet[i["item"]]
        for feld in ("status", "senses", "sicherheit", "festgehalten", "aufgedeckt"):
            if (i.get(feld) or None) != (x[feld] or None):
                abweichend += 1
                break
    if abweichend:
        sys.exit(f"{pfad}: bei {abweichend} Items weicht der Endstand im Export vom Ereignisprotokoll ab; nicht ausgewertet")
    erweitert = {i: False for i in ids}
    for e in exp["ereignisse"]:
        if e.get("item") in erweitert and e.get("kontext_erweitert"):
            erweitert[e["item"]] = True
    return {"pfad": pfad, "meta": meta, "runde": runde, "ids": ids, "a": abgeleitet, "erweitert": erweitert,
            "exportiert_um": exp.get("exportiert_um"), "lesart_zuerst": bool(meta.get("lesart_zuerst"))}


# --- Bericht für die Besprechung (nur Datei, nie Konsole) -----------------------------------------------

def worktrees():
    """Alle Worktrees dieses Repos, nicht nur der, in dem das Skript liegt (Review 2026-11-20)."""
    roh = subprocess.check_output(["git", "worktree", "list", "--porcelain"], cwd=HIER, text=True)
    return [Path(z[len("worktree "):]).resolve() for z in roh.splitlines() if z.startswith("worktree ")]


def erlaubt(pfad):
    ziel = Path(pfad).resolve()
    return not any(ziel == w or w in ziel.parents for w in worktrees())


def bericht(pfad, x, y, items, ids):
    if not erlaubt(pfad):
        sys.exit("--bericht: Der Pfad liegt in einem Worktree des öffentlichen Forks. Bitte einen Ort außerhalb "
                 "wählen, z. B. das private Repository.")
    ziel = Path(pfad).resolve()
    karten = {i: {k["sense"]: k for k in items[i]["karten"]} for i in ids}

    def label(p, i):
        a = p["a"][i]
        if not a["festgehalten"]:
            return "nicht festgehalten"
        s = a["status"]
        if a["senses"]:
            terme = ["; ".join(b["term"] for b in karten[i][k]["begriffe"]) if k in karten[i] else k for k in a["senses"]]
            s += ": " + " | ".join(f"[{t}]" for t in terme)
        return s + f" ({a['sicherheit']})"

    z = [f"# Besprechung Runde {x['runde']}", "",
         f"Exporte: `{Path(x['pfad']).name}` ({x['meta']['kennung']}, {x['exportiert_um']}), "
         f"`{Path(y['pfad']).name}` ({y['meta']['kennung']}, {y['exportiert_um']}).",
         "Privat: enthält Labels. Nicht ins öffentliche Repo, nicht in eine KI-Sitzung (Protokoll, A37).", ""]
    for i in sorted(ids):
        it = items[i]
        ax, ay = x["a"][i], y["a"][i]
        gleich = ax["festgehalten"] and ay["festgehalten"] and ax["status"] == ay["status"] \
            and set(ax["senses"] or []) == set(ay["senses"] or [])
        z += [f"## {i}: {it['orth']} ({it['werk']}, {it['sigle']}) {'gleich' if gleich else 'ABWEICHEND'}", ""]
        for p, a in ((x, ax), (y, ay)):
            k = p["meta"]["kennung"]
            z.append(f"- **{k}:** {label(p, i)}")
            if a["lesart"]:
                z.append(f"  - Lesart: {a['lesart']}")
            if (a["kommentar"] or "").strip():
                z.append(f"  - Kommentar: {a['kommentar'].strip()}")
            if p["erweitert"][i]:
                z.append("  - Kontext erweitert")
        z.append("")
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text("\n".join(z), encoding="utf-8")


# --- Hauptteil --------------------------------------------------------------------------------------

def main(argv=None):
    ap = argparse.ArgumentParser(description="Übereinstimmung einer Pilotrunde, nur Kennzahlen")
    ap.add_argument("export1")
    ap.add_argument("export2")
    ap.add_argument("--bericht", help="Markdown für die Besprechung, Pfad außerhalb des Repos")
    args = ap.parse_args(argv)

    man_roh = (HIER / "manifest-pilot.json").read_bytes()
    manifest = json.loads(man_roh)
    items_roh = (HIER / "items-pilot.json").read_bytes()
    if hashlib.sha256(items_roh).hexdigest() != manifest["pruefsummen"]["items-pilot.json"]:
        sys.exit("items-pilot.json passt nicht zum Manifest")
    items = {i["item"]: i for i in json.loads(items_roh)}
    msha = hashlib.sha256(man_roh).hexdigest()

    x, y = lade(args.export1, manifest, msha, man_roh), lade(args.export2, manifest, msha, man_roh)
    if x["meta"]["kennung"] == y["meta"]["kennung"]:
        sys.exit("Beide Exporte tragen dieselbe Kennung")
    if x["runde"] != y["runde"]:
        sys.exit("Die Exporte gehören zu verschiedenen Runden")
    if x["meta"]["kennung"] != KENNUNGEN[0]:
        x, y = y, x
    ids = sorted(x["ids"])
    runde = x["runde"]

    fest = {p["meta"]["kennung"]: [i for i in ids if p["a"][i]["festgehalten"]] for p in (x, y)}
    ungueltig = {p["meta"]["kennung"]: sum(1 for i in ids if p["a"][i]["festgehalten"] and not gueltig(p["a"][i], p["lesart_zuerst"]))
                 for p in (x, y)}
    beide = [i for i in ids if x["a"][i]["festgehalten"] and y["a"][i]["festgehalten"]
             and gueltig(x["a"][i], x["lesart_zuerst"]) and gueltig(y["a"][i], y["lesart_zuerst"])]

    def ganz(a):
        return (a["status"], frozenset(a["senses"] or []))

    paare_ganz = [(ganz(x["a"][i]), ganz(y["a"][i])) for i in beide]
    k_ganz = sum(1 for a, b in paare_ganz if a == b)

    def menge(a):
        return frozenset([a["status"]]) if a["status"] in EIGENE_KATEGORIE else frozenset(a["senses"])

    def sense_paare(ebene):
        return [(menge(x["a"][i]), menge(y["a"][i])) for i in beide
                if x["a"][i]["status"] in ebene and y["a"][i]["status"] in ebene]

    def zahl(v, stellen=3):
        return "nicht definiert (alle Werte gleich oder keine Einheit)" if v is None else f"{v:.{stellen}f}"

    def anteil(k, n):
        if n == 0:
            return "0 von 0"
        lo, hi = wilson(k, n)
        return f"{k} von {n} ({100 * k / n:.1f} %, 95 % Wilson {100 * lo:.1f} bis {100 * hi:.1f} %)"

    kx, ky = KENNUNGEN
    out = [f"Runde {runde}: {len(ids)} Items",
           f"Ablauf: {kx} {'lesart-zuerst' if x['lesart_zuerst'] else 'direkt'}, {ky} {'lesart-zuerst' if y['lesart_zuerst'] else 'direkt'}"
           + ("" if x["lesart_zuerst"] == y["lesart_zuerst"] else "  ACHTUNG: verschiedene Abläufe, nicht vergleichbar"),
           f"Richtlinien: {kx} {x['meta'].get('richtlinien')}, {ky} {y['meta'].get('richtlinien')}",
           f"Werkzeug: {kx} {x['meta'].get('werkzeug')}, {ky} {y['meta'].get('werkzeug')}",
           f"Exportiert: {kx} {x['exportiert_um']}, {ky} {y['exportiert_um']}",
           f"Festgehalten: {kx} {len(fest[kx])}, {ky} {len(fest[ky])}, beide gültig {len(beide)}"
           + (f"  (ungültig festgehalten: {kx} {ungueltig[kx]}, {ky} {ungueltig[ky]})" if any(ungueltig.values()) else ""),
           "",
           "Ganzes Label (Status und Kartenmenge exakt; Maß der Stoppregel, A32)",
           f"  Rohübereinstimmung: {anteil(k_ganz, len(paare_ganz))}",
           f"  Krippendorffs α nominal: {zahl(alpha(paare_ganz, nominal))}"]
    if runde >= 1:
        a = alpha(paare_ganz, nominal)
        if len(beide) < len(ids):
            urteil = f"nicht anwendbar: nur {len(beide)} von {len(ids)} Items von beiden gültig festgehalten"
        elif a is None:
            urteil = "nicht anwendbar: α nicht definiert"
        elif a >= 0.80:
            urteil = "α ≥ 0,80: Richtlinien einfrieren, Hauptrunde"
        elif a >= 0.67:
            urteil = "0,67 ≤ α < 0,80: nachschärfen, nächste Runde (nach der letzten Poolrunde einfrieren, als Einschränkung berichten)"
        else:
            urteil = "α < 0,67: nachschärfen; nach der letzten Poolrunde keine Hauptrunde, Instrument ändern"
        out.append(f"  Stoppregel: {urteil}")
    else:
        out.append("  Stoppregel: Runde 0 hat keine Schwelle (A32)")

    konf = Counter((x["a"][i]["status"], y["a"][i]["status"]) for i in beide)
    kurz = {"SENSE": "SEN", "MEHRERE": "MEH", "KEINE_PASST": "KEI", "LEMMA_FALSCH": "LEM",
            "KONTEXT_UNZUREICHEND": "KON", "TEXT_DEFEKT": "TEX"}
    out += ["", f"Statusebene: Zeilen {kx}, Spalten {ky}",
            "       " + " ".join(f"{kurz[s]:>4}" for s in STATUS)]
    for s in STATUS:
        out.append(f"  {kurz[s]:>4} " + " ".join(f"{konf[(s, t)]:>4}" for t in STATUS))
    stimmt = sum(konf[(s, s)] for s in STATUS)
    out.append(f"  Status gleich: {anteil(stimmt, len(beide))}")

    ps = sense_paare(SENSE_EBENE)
    out += ["", "Sense-Ebene (beide SENSE, MEHRERE, KEINE_PASST oder LEMMA_FALSCH; Abschnitt 9.1)",
            f"  Einheiten: {len(ps)}",
            f"  α MASI (1 - J·M, Hauptmaß): {zahl(alpha(ps, masi))}",
            f"  α nominal: {zahl(alpha(ps, nominal))}",
            f"  Rohübereinstimmung exakt: {anteil(sum(1 for a, b in ps if a == b), len(ps))}",
            f"  Rohübereinstimmung Überschneidung: {anteil(sum(1 for a, b in ps if a & b), len(ps))}"]

    out += ["", "Je Person (festgehaltene Items)"]
    for p in (x, y):
        k = p["meta"]["kennung"]
        f_ids = fest[k]
        sich = Counter(p["a"][i]["sicherheit"] for i in f_ids)
        out.append(f"  {k}: Sicherheit " + ", ".join(f"{s} {sich[s]}" for s in SICHER)
                   + f"; Kontext erweitert {sum(p['erweitert'][i] for i in f_ids)}"
                   + f"; Lesart notiert {sum(1 for i in f_ids if p['a'][i]['aufgedeckt'])}")

    text = "\n".join(out)
    # Selbstprüfung gegen Lecks: keine Item-, Token-, Lemma-, Sense- oder Begriffs-ID auf der Konsole
    verboten = set(ids) | {items[i]["xml_id"] for i in ids} | {items[i]["lemma"] for i in ids}
    verboten |= {k["sense"] for i in ids for k in items[i]["karten"]}
    if any(v in text for v in verboten) or re.search(r"(lemma|concept)_\d|_sense_", text):
        sys.exit("Ausgabe enthielte eine ID; abgebrochen, nichts gedruckt")
    print(text)

    if args.bericht:
        bericht(args.bericht, x, y, items, ids)
        print(f"\nBericht für die Besprechung geschrieben ({len(ids)} Items). Er enthält Labels: nicht in eine KI-Sitzung geben.")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
