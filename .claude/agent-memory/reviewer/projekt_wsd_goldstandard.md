---
name: projekt-wsd-goldstandard
description: Fork mhdbdb-wsd, goldstandard/: Pilot-Ziehung und Offline-Annotationsseite prüfen (Blindheit, Protokoll, localStorage, Reproduktion)
metadata:
  type: project
---
Stand 2026-11-12 (Runde 1 Pilot-Pool, Korpus a938559dc). Normativ ist `goldstandard/PROTOKOLL.md`; Zahlen dort sind teils "übernommen, nicht nachgemessen".

- **Blindheit heißt mehr als `@ana`:** Protokoll §3 sagt "die Annotator:innen sehen `@pos` nicht". Eine angezeigte Wortart ist bei `wortart_herkunft: token` das Token-`@pos` (und das ist laut §3 bedeutungsabhängig, *guot* NOM = 'Besitz'). Die Leck-Asserts der Skripte prüfen nur Schlüsselnamen (`"ana"`, `"pos"`), nicht abgeleitete Felder.
- **Offline-HTML mit localStorage:** zwei Tabs derselben Datei überschreiben sich (letzter Schreiber gewinnt, ganze Antworten weg), Import ersetzt das Protokoll. Probe: Playwright-.mjs im Scratchpad mit `createRequire("<repo>/package.json")("playwright")`, zwei Pages in einem Context, Zählung `ereignisse.length` vor/nach.
- **Ziehung nachrechnen:** `pilot_ziehen.py` per Python-Replace (`OUT = Path(sys.argv[1])`) ins Scratchpad kopieren, ~3 min; items-pilot.json kam byte-gleich heraus, Manifest unterscheidet sich nur in `skript_sha256`. sed scheitert am Windows-Pfad (`\5`).
- **Runde 2 (2026-11-13), Ereignisprotokoll mit Ableitung:** Lokale Ereignisse werden angehängt, sortiert wird nur beim Vereinigen fremder (nach `ms`). Live-Stand und Stand nach Neuladen können sich deshalb unterscheiden; bei Uhrversatz zwischen zwei Rechnern (Import, dann weiterarbeiten) ist eine Änderung nach dem Neuladen weg. Probe: `ms` im Export um +10 min verschieben, frischer Context, importieren, ändern, `reload`, `A[...]` lesen. Zweite Falle: Der `storage`-Listener zeichnet neu und verwirft einen ungespeicherten Kommentarentwurf im anderen Tab. Der Test läuft etwa 3 min; `| tail` verbirgt dabei den Fortschritt, also in eine Datei umleiten.
- Korpus: 89 Grundgesamtheits-Tokens liegen in `<note>` (NEIR 49, NEIM 39, CL 1), die Kontextbauer überspringen `<note>` -> KeyError, falls je gezogen. `<w>` hat keine Kindelemente, `join` nur an `<pc>` (left/right).
