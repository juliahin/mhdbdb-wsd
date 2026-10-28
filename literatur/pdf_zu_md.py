"""
Volltexte aus literatur/pdf/ mit Docling nach Markdown umwandeln.

Aufruf aus dem Repo-Wurzelverzeichnis:
    python literatur/pdf_zu_md.py                 alle PDFs, die noch kein aktuelles .md haben
    python literatur/pdf_zu_md.py Datei.pdf ...   nur diese (Name relativ zu literatur/pdf/)
    python literatur/pdf_zu_md.py --neu           alle neu umwandeln
    python literatur/pdf_zu_md.py --nachtragen    vorhandene .md um ausgelassene Textebene ergänzen

Ausgabe nach literatur/md/ (nicht im Repo, die Volltexte sind urheberrechtlich geschützt):
  <Name>.md            Markdown mit Seitenmarken <!-- PDF-Seite n --> vor jeder Seite.
                       Das ist die physische Seite im PDF, nicht die gedruckte Seitenzahl.
  _protokoll.jsonl     eine Zeile pro Umwandlung: Datei, SHA-256 des PDFs, Seiten, OCR ja/nein,
                       Docling-Version, Dauer, Zeitpunkt

OCR: PDFs ohne Textebene (Scans) werden ganzseitig per EasyOCR (Englisch, Deutsch) gelesen,
alle anderen ohne OCR. Voraussetzung: `pip install easyocr` (lädt beim ersten Lauf seine Modelle).
Vor der OCR werden Scanseiten mit 300 dpi über den Rotkanal binarisiert: Farbige Textmarker
(rosa, gelb) werden weiß, schwarzer Text bleibt. Ohne diesen Schritt verstümmelt die OCR genau
die markierten Zeilen (gemessen am 2026-10-23 an Schmidt 1985).
Bilder werden nicht eingebettet, nur als Platzhalter markiert.
"""

from datetime import datetime, timezone
from pathlib import Path
import hashlib
import io
import tempfile
import importlib.metadata
import json
import re
import sys
import time

import pymupdf
from PIL import Image
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import EasyOcrOptions, PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc import ImageRefMode

BASIS = Path(__file__).resolve().parent
PDF = BASIS / "pdf"
MD = BASIS / "md"
MD.mkdir(exist_ok=True)
VERSION = importlib.metadata.version("docling")


def hat_textebene(pfad, seiten=5):
    d = pymupdf.open(pfad)
    return sum(len(d[i].get_text().strip()) for i in range(min(seiten, d.page_count))) > 200


def ohne_markierungen(pfad, ziel):
    """Scan ohne Textmarker als neues PDF schreiben (Rotkanal, Schwelle 140)."""
    quelle, neu = pymupdf.open(pfad), pymupdf.open()
    for seite in quelle:
        pix = seite.get_pixmap(dpi=300)
        rot = Image.open(io.BytesIO(pix.tobytes("png"))).convert("RGB").getchannel("R")
        sw = rot.point(lambda v: 255 if v > 140 else 0)
        puffer = io.BytesIO()
        sw.save(puffer, format="PNG")
        s = neu.new_page(width=seite.rect.width, height=seite.rect.height)
        s.insert_image(s.rect, stream=puffer.getvalue())
    neu.save(ziel)


def konverter(ocr):
    opt = PdfPipelineOptions()
    opt.do_ocr = ocr
    if ocr:
        # EasyOCR statt der Docling-Voreinstellung: Diese ließ am 2026-10-23 bei Schmidt 1985
        # ganze Zeilenteile aus, EasyOCR liefert vollständigen Text mit einzelnen Zeichenfehlern
        opt.ocr_options = EasyOcrOptions(force_full_page_ocr=True, lang=["en", "de"])
    opt.do_table_structure = True
    return DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opt)})


NACHTRAG = "<!-- Docling hat diese Seite weitgehend ausgelassen; es folgt die rohe Textebene des PDFs -->"


def zeichen(text):
    return len(re.sub(r"\s|<!-- image -->", "", text))


def mit_textebene(pdf, n, md):
    """Docling verwirft auf Seiten mit Abbildungen oder Baumdiagrammen oft auch den Fließtext
    (am 2026-10-28 gemessen: 40 Seiten in 10 PDFs). Liefert es weniger als 30 % der Zeichen der
    Textebene, wird diese gekennzeichnet angehängt."""
    roh = pdf[n - 1].get_text()
    if NACHTRAG in md or zeichen(roh) <= 300 or zeichen(md) >= 0.3 * zeichen(roh):
        return md, False
    return md.rstrip() + f"\n\n{NACHTRAG}\n\n{roh.strip()}\n", True


def umwandeln(pfad, conv, ocr):
    t0 = time.time()
    if ocr:
        with tempfile.TemporaryDirectory() as tmp:
            sauber = Path(tmp) / pfad.name
            ohne_markierungen(pfad, sauber)
            doc = conv.convert(sauber).document
    else:
        doc = conv.convert(pfad).document
    pdf = pymupdf.open(pfad)
    teile = []
    for n in sorted(doc.pages):
        md = doc.export_to_markdown(page_no=n, image_mode=ImageRefMode.PLACEHOLDER)
        if not ocr:
            md, _ = mit_textebene(pdf, n, md)
        teile.append(f"<!-- PDF-Seite {n} -->\n\n" + md)
    kopf = f"<!-- Quelle: pdf/{pfad.name} | Docling {VERSION} | nicht gegengelesen -->\n\n"
    (MD / (pfad.stem + ".md")).write_text(kopf + "\n\n".join(teile) + "\n", encoding="utf-8")
    return len(doc.pages), round(time.time() - t0, 1)


def nachtragen(pfad):
    """Vorhandenes .md um die Textebene der Seiten ergänzen, die Docling ausgelassen hat."""
    ziel = MD / (pfad.stem + ".md")
    if not ziel.exists():
        return []
    pdf = pymupdf.open(pfad)
    teile = re.split(r"(<!-- PDF-Seite (\d+) -->)", ziel.read_text(encoding="utf-8"))
    ergaenzt = []
    for i in range(1, len(teile), 3):
        n = int(teile[i + 1])
        md, neu = mit_textebene(pdf, n, teile[i + 2])
        if neu:
            teile[i + 2] = "\n\n" + md.lstrip() + "\n"
            ergaenzt.append(n)
    if ergaenzt:
        ziel.write_text("".join(t for j, t in enumerate(teile) if j % 3 != 2), encoding="utf-8")
    return ergaenzt


def main(argv):
    neu = "--neu" in argv
    namen = [a for a in argv if not a.startswith("--")]
    pdfs = [PDF / n for n in namen] if namen else sorted(PDF.glob("*.pdf"))
    if "--nachtragen" in argv:
        for p in pdfs:
            seiten = nachtragen(p)
            if seiten:
                print(f"{p.name}: Textebene nachgetragen auf PDF-Seite {', '.join(map(str, seiten))}")
                with open(MD / "_protokoll.jsonl", "a", encoding="utf-8") as fh:
                    fh.write(json.dumps({"datei": p.name, "status": "textebene nachgetragen", "seiten_nachgetragen": seiten,
                                         "zeitpunkt": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds")},
                                        ensure_ascii=False) + "\n")
        return
    convs = {}
    for p in pdfs:
        ziel = MD / (p.stem + ".md")
        if not neu and not namen and ziel.exists() and ziel.stat().st_mtime > p.stat().st_mtime:
            continue
        ocr = not hat_textebene(p)
        conv = convs.setdefault(ocr, konverter(ocr))
        print(f"{p.name} (OCR: {'ja' if ocr else 'nein'}) ...", flush=True)
        try:
            seiten, dauer = umwandeln(p, conv, ocr)
            status = "ok"
        except Exception as e:  # ein defektes PDF soll den Lauf nicht abbrechen
            seiten, dauer, status = None, None, f"fehler: {e}"
        print(f"  {status}, {seiten} Seiten, {dauer} s", flush=True)
        eintrag = {
            "datei": p.name, "sha256": hashlib.sha256(p.read_bytes()).hexdigest(),
            "seiten": seiten, "ocr": ocr, "docling": VERSION, "dauer_s": dauer, "status": status,
            "zeitpunkt": datetime.now(timezone.utc).astimezone().isoformat(timespec="seconds"),
        }
        with open(MD / "_protokoll.jsonl", "a", encoding="utf-8") as fh:
            fh.write(json.dumps(eintrag, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main(sys.argv[1:])
