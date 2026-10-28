"""
Julias Markierungen (Hervorhebungen, Notizen, Stempel, Freihandstriche) aus literatur/pdf/ auslesen.

Docling (pdf_zu_md.py) liest nur den Seitentext, keine Anmerkungen. Dieses Skript holt sie nach,
damit eine Zusammenfassung weiß, welche Stellen Julia beim Lesen für wichtig hielt.

Aufruf aus dem Repo-Wurzelverzeichnis:
    python literatur/markierungen.py                 alle PDFs mit Markierungen
    python literatur/markierungen.py Datei.pdf ...   nur diese (Name relativ zu literatur/pdf/)

Ausgabe nach literatur/md/<Name>.markierungen.md (nicht im Repo: enthält Wortlaut aus den Volltexten).
PDFs ohne Markierungen bekommen keine Datei.

Seitenangabe: „PDF-Seite n" ist die physische Seite wie in den Seitenmarken von pdf_zu_md.py;
hat das PDF Seitenlabels, steht die gedruckte Seitenzahl dahinter.
Hervorhebungen: Wörter, deren Mitte in einem der markierten Vierecke liegt.
Freihandstriche auf Scans ohne Textebene (Schmidt): die Seite wird bei 300 dpi ohne Anmerkungsebene
per EasyOCR gelesen, genommen werden die Wörter im Band jedes Strichs, also mit OCR-Fehlern.
Gezeichnete Zeichen (als Stempel gespeichert: Häkchen, Randstriche) markieren keinen Text; angegeben
werden die Zeilen auf ihrer Höhe, ausdrücklich als Position und nicht als markierter Wortlaut.
"""

from datetime import datetime, timezone
from pathlib import Path
import colorsys
import hashlib
import sys

import pymupdf

BASIS = Path(__file__).resolve().parent
PDF = BASIS / "pdf"
MD = BASIS / "md"
MD.mkdir(exist_ok=True)

# Stempel sind in diesen PDFs handgezeichnete Häkchen und Randstriche, keine Textstempel
ART = {"Highlight": "Hervorhebung", "Underline": "Unterstreichung", "StrikeOut": "Durchstreichung",
       "Squiggly": "Wellenlinie", "Text": "Notiz", "FreeText": "Textfeld", "Stamp": "Zeichen",
       "Ink": "Freihand", "Caret": "Einfügezeichen", "Square": "Rahmen", "Circle": "Kreis"}

_ocr = None


def leser():
    global _ocr
    if _ocr is None:
        import easyocr
        _ocr = easyocr.Reader(["de", "en"], verbose=False)
    return _ocr


def farbe(a):
    rgb = a.colors.get("stroke") or a.colors.get("fill")
    if not rgb:
        return ""
    h, l, s = colorsys.rgb_to_hls(*rgb)
    if s < 0.2:
        name = "grau"
    else:
        grad = h * 360
        name = next(n for g, n in [(15, "rot"), (45, "orange"), (70, "gelb"), (170, "grün"),
                                   (260, "blau"), (330, "violett"), (361, "rosa")] if grad < g)
        if name == "rot" and l > 0.6:
            name = "rosa"
    return name


def woerter_in(seite, rechtecke):
    treffer = []
    for w in seite.get_text("words"):
        mx, my = (w[0] + w[2]) / 2, (w[1] + w[3]) / 2
        if any(r.x0 <= mx <= r.x1 and r.y0 <= my <= r.y1 for r in rechtecke):
            treffer.append(w)
    treffer.sort(key=lambda w: (w[5], w[6], w[7]))
    return " ".join(w[4] for w in treffer)


_seiten_ocr = {}


def ocr_woerter(seite):
    """Ganze Seite einmal ohne Anmerkungsebene lesen; Wortkästen in PDF-Punkten wie get_text("words")."""
    schluessel = (seite.parent.name, seite.number)
    if schluessel not in _seiten_ocr:
        dpi = 300
        pix = seite.get_pixmap(dpi=dpi, annots=False)
        f = 72 / dpi
        woerter = []
        for kasten, text, _ in leser().readtext(pix.tobytes("png"), width_ths=0.1):
            xs, ys = [p[0] * f for p in kasten], [p[1] * f for p in kasten]
            woerter.append((min(xs), min(ys), max(xs), max(ys), text))
        _seiten_ocr[schluessel] = woerter
    return _seiten_ocr[schluessel]


def unter_strichen(seite, a):
    """Wörter unter Freihandstrichen eines Scans: Band um jeden Strich, so breit wie der Stift."""
    halb = (a.border.get("width") or 10) / 2
    baender = [pymupdf.Rect(min(x for x, _ in s), min(y for _, y in s) - halb,
                            max(x for x, _ in s), max(y for _, y in s) + halb) for s in a.vertices or []]
    treffer = [w for w in ocr_woerter(seite)
               if any(b.x0 - 3 <= (w[0] + w[2]) / 2 <= b.x1 + 3 and b.y0 <= (w[1] + w[3]) / 2 <= b.y1
                      for b in baender)]
    treffer.sort(key=lambda w: (round(w[1] / 6), w[0]))
    return " ".join(w[4] for w in treffer)


def zeilen_auf_hoehe(seite, rect):
    """Textzeilen, deren Mitte auf der Höhe eines gezeichneten Zeichens liegt (bei kleinen Zeichen ±6 pt)."""
    y0, y1 = rect.y0 - 6, rect.y1 + 6
    zeilen = []
    for block in seite.get_text("dict")["blocks"]:
        for zeile in block.get("lines", []):
            mitte = (zeile["bbox"][1] + zeile["bbox"][3]) / 2
            if y0 <= mitte <= y1:
                zeilen.append("".join(s["text"] for s in zeile["spans"]).strip())
    zeilen = [z for z in zeilen if z]
    if len(zeilen) > 2:
        return f"{zitat(zeilen[0])} bis {zitat(zeilen[-1])} ({len(zeilen)} Zeilen)"
    return " / ".join(zitat(z) for z in zeilen)


def text_zu(seite, a, hat_text):
    art = a.type[1]
    if art in ("Highlight", "Underline", "StrikeOut", "Squiggly"):
        v = a.vertices or []
        quads = [pymupdf.Quad(v[i:i + 4]).rect for i in range(0, len(v) - 3, 4)] or [a.rect]
        return woerter_in(seite, quads), ""
    if art == "Ink":
        if hat_text:
            return woerter_in(seite, [a.rect]), ""
        return unter_strichen(seite, a), "OCR"
    if art == "Stamp" and hat_text:
        return zeilen_auf_hoehe(seite, a.rect), "Höhe"
    return "", ""


def auslesen(pfad):
    d = pymupdf.open(pfad)
    eintraege = []
    for i, seite in enumerate(d):
        annots = list(seite.annots())
        if not annots:
            continue
        hat_text = len(seite.get_text().strip()) > 50
        label = seite.get_label()
        for a in annots:
            art = a.type[1]
            if art in ("Link", "Popup", "Widget"):
                continue
            text, quelle = text_zu(seite, a, hat_text)
            notiz = (a.info.get("content") or "").strip()
            if art == "Stamp" and not notiz:
                notiz = a.info.get("subject") or a.info.get("name") or ""
            eintraege.append({"seite": i + 1, "label": label, "y": a.rect.y0, "x": a.rect.x0,
                              "art": ART.get(art, art), "farbe": farbe(a), "text": text.strip(),
                              "quelle": quelle, "notiz": notiz})
    eintraege.sort(key=lambda e: (e["seite"], round(e["y"] / 4), e["x"]))
    return d, eintraege


def zitat(t):
    return "„" + t.replace("\n", " ") + "“"


def schreiben(pfad, d, eintraege):
    arten = {}
    for e in eintraege:
        arten[e["art"]] = arten.get(e["art"], 0) + 1
    kopf = [
        f"<!-- Quelle: pdf/{pfad.name} | sha256 {hashlib.sha256(pfad.read_bytes()).hexdigest()} "
        f"| ausgelesen {datetime.now(timezone.utc).astimezone().isoformat(timespec='seconds')} -->",
        "",
        f"# Markierungen in {pfad.stem}",
        "",
        "Julias Anmerkungen im PDF, in Seitenreihenfolge. Nur Wortlaut unter der Markierung, keine "
        "Deutung. " + ", ".join(f"{n} {a}" for a, n in sorted(arten.items())) + ".",
        "",
    ]
    # mehrteilige Zeichen (eine Randklammer aus mehreren Strichen) ergeben gleiche Einträge: zusammenfassen
    gruppen = []
    for e in eintraege:
        k = (e["seite"], e["art"], e["text"], e["notiz"])
        if gruppen and gruppen[-1][0] == k:
            gruppen[-1][2] += 1
        else:
            gruppen.append([k, e, 1])
    zeilen = []
    for _, e, n in gruppen:
        seite = f"PDF-Seite {e['seite']}"
        if e["label"] and e["label"] != str(e["seite"]):
            seite += f" (S. {e['label']})"
        art = e["art"] + (f", {e['farbe']}" if e["farbe"] else "") + (f", {n} Teile" if n > 1 else "")
        teile = [f"- **{seite}**, {art}"]
        if e["text"] and e["quelle"] == "Höhe":
            teile.append(" am Rand, auf Höhe von " + e["text"])
        elif e["text"]:
            teile.append(": " + zitat(e["text"]) + (" (OCR)" if e["quelle"] else ""))
        elif e["art"] in ("Hervorhebung", "Freihand"):
            teile.append(": (kein Text unter der Markierung gefunden)")
        if e["notiz"]:
            teile.append(f"\n  Notiz: {zitat(e['notiz'])}")
        zeilen.append("".join(teile))
    ziel = MD / (pfad.stem + ".markierungen.md")
    ziel.write_text("\n".join(kopf + zeilen) + "\n", encoding="utf-8")
    return ziel


def main(argv):
    pdfs = [PDF / n for n in argv] if argv else sorted(PDF.glob("*.pdf"))
    for p in pdfs:
        d, eintraege = auslesen(p)
        if not eintraege:
            continue
        leer = sum(1 for e in eintraege if e["art"] in ("Hervorhebung", "Freihand") and not e["text"])
        ziel = schreiben(p, d, eintraege)
        print(f"{p.name}: {len(eintraege)} Markierungen, {leer} ohne Text -> {ziel.name}", flush=True)


if __name__ == "__main__":
    main(sys.argv[1:])
