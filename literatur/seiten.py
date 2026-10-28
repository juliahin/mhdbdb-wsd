"""
Arbeitsmaterial zum Prüfen an der Quelle: rohe Textebene und Seitenbilder eines PDFs aus literatur/pdf/.

Read mit `pages` geht auf diesem Rechner nicht (pdftoppm fehlt), und Docling (pdf_zu_md.py) verliert
Tabellenzellen und stellt Absätze, die über einen Seitenumbruch laufen, ganz unter die Anfangsseite.
Für Zahlen, Tabellen und Seitenangaben ist deshalb die Textebene bzw. das Seitenbild maßgeblich.

Aufruf aus dem Repo-Wurzelverzeichnis:
    python literatur/seiten.py Datei.pdf                 Textebene + Bilder aller Seiten mit Tabellen/Abbildungen
    python literatur/seiten.py Datei.pdf 131 140-145     Textebene + Bilder genau dieser PDF-Seiten

Ausgabe in einen neuen Ordner pro Aufruf, temp/seiten/<Name>-<Zeitstempel>-<Prozess>/ (temp/ ist
gitignored); das Skript gibt den Pfad aus:
  textebene.txt   jede Seite mit Marke „===== PDF-Seite n (gedruckt: x) =====“
  seite-NNN.png   Seitenbild, 100 dpi, ohne Anmerkungsebene
Ein Ordner pro Aufruf, damit parallele Läufe am selben Werk sich nicht überschreiben. Wer aufgerufen
hat, löscht genau den ausgegebenen Ordner, wenn die Arbeit fertig ist, und keinen anderen.
"""

from datetime import datetime
from pathlib import Path
import os
import re
import sys

import pymupdf

BASIS = Path(__file__).resolve().parent
ZIEL = BASIS.parent / "temp" / "seiten"


def seitenliste(angaben, anzahl):
    seiten = set()
    for a in angaben:
        von, _, bis = a.partition("-")
        seiten.update(range(int(von), int(bis or von) + 1))
    return sorted(s for s in seiten if 1 <= s <= anzahl)


def mit_tabelle_oder_abbildung(seite):
    text = seite.get_text()
    return bool(re.search(r"\b(Table|Tabelle|Tab\.|Figure|Fig\.|Abbildung|Abb\.)\s*\d", text)
                or len(seite.get_drawings()) > 20 or seite.get_images())


def main(argv):
    if not argv:
        sys.exit(__doc__)
    pfad = BASIS / "pdf" / argv[0]
    d = pymupdf.open(pfad)
    try:
        seiten = seitenliste(argv[1:], d.page_count) if argv[1:] else \
            [i + 1 for i, s in enumerate(d) if mit_tabelle_oder_abbildung(s)]
    except ValueError:
        sys.exit(f"Seitenangaben nicht lesbar: {' '.join(argv[1:])} (erlaubt: 12 oder 12-15)")
    # eigener Ordner pro Aufruf: parallele Läufe am selben Werk überschreiben sich nicht
    ziel = ZIEL / f"{pfad.stem}-{datetime.now():%Y%m%d-%H%M%S}-{os.getpid()}"
    ziel.mkdir(parents=True)
    with open(ziel / "textebene.txt", "w", encoding="utf-8") as fh:
        for i, seite in enumerate(d):
            fh.write(f"\n\n===== PDF-Seite {i + 1} (gedruckt: {seite.get_label() or '?'}) =====\n\n"
                     + seite.get_text())
    for n in seiten:
        d[n - 1].get_pixmap(dpi=100, annots=False).save(ziel / f"seite-{n:03d}.png")
    print(f"{ziel}: textebene.txt, {len(seiten)} Seitenbilder ({', '.join(map(str, seiten)) or 'keine'})")


if __name__ == "__main__":
    main(sys.argv[1:])
