# Schmidt 1985: Parser zur automatischen Disambiguierung von Homographen im Mittelhochdeutschen

**Datei:** `pdf/Schmidt-1985-Parser-Homographen-MHD.pdf` (nur lokal; Scan, 9 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, ganzes PDF am Seitenbild gelesen (alle Zitate und die Tabellen I bis III am Bild geprüft, nicht an der OCR), Sammelband über Titelblatt und Katalog bestimmt.

Seitenzählung: PDF-Seite n = gedruckte S. 344 + n. PDF-Seite 1 trägt keine gedruckte Zahl (erschlossen S. 345), PDF-Seite 2 bis 9 tragen S. 346 bis 353.

## Bibliografie

- **Vollständig:** Schmidt, Klaus M. (1985). An Algorithmic Approach to a Parser for Automatic Disambiguation of Homographs in Middle High German on the Basis of the Conceptual Dictionary Project. In: Jacqueline Hamesse und Antonio Zampolli (Hg.), *Computers in Literary and Linguistic Computing / L'ordinateur et les recherches littéraires et linguistiques. Proceedings of the Eleventh International Conference*, Université Catholique de Louvain (Louvain-la-Neuve), 2. bis 6. April 1984. Paris, Genève: Champion-Slatkine (Proceedings of the International Conferences of the Association for Literary and Linguistic Computing 1), S. 345 bis 353.
- **Prüfung der Angaben:**
  - Titel, Autor, Seiten 346 bis 353: ✔ am PDF (Titel S. 345, Kolumnenzahlen S. 346 bis 353).
  - Sammelband (Titel, Hg., Verlag, Ort, Jahr 1985, Tagung 2. bis 6. April 1984, Reihe ALLC 1): ✔ am Titelblatt des Bandes, abgerufen über die Digital Library of Antonio Zampolli (ILC-CNR, `Z068.pdf`); bestätigt durch CiNii (NCID BA0284241X: viii, 404 S., ISBN 2051007039).
  - Dass dieser Beitrag in genau diesem Band steht: ○. Nur über einen Sekundäreintrag (ResearchGate-Seite des MHDBDB-Labs, im Suchergebnis zitiert mit „Computers in Literary and Linguistic Computing", „Proceedings of the 11th International Conference", Université Catholique; die Seite selbst lieferte 403). Kein Inhaltsverzeichnis des Bandes eingesehen. Innere Belege passen: der Text spricht von „this conference" und dem eingereichten Abstract (S. 351), der jüngste Verweis ist von 1983 (S. 353).
- **DOI/URL:** keine
- **Art:** Konferenzbeitrag (Tagungsband)
- **Sprache:** Englisch

## Worum es geht

Schmidt beschreibt den Plan für einen Parser, der Homographen im mittelhochdeutschen Begriffswörterbuch (Conceptual Dictionary Project, Vorläufer der MHDBDB) automatisch disambiguieren soll. Grundlage sind die schon manuell disambiguierten Begriffsthesauri: Aus Kontextfenstern um Belege mit bekannter Bedeutung sollen Programme wiederkehrende Muster (Zeichenketten, Begriffskategorien der Kontextwörter, Wortart, Worttyp) finden, die nur bei einer Bedeutung auftreten. Der Beitrag ist ein Werkstattbericht: Die Masterdatei ist gebaut, die Mustererkennung in Arbeit, Ergebnisse gibt es noch keine (S. 351 bis 352).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Das Begriffswörterbuch ordnet den Wortschatz nach einem Begriffssystem ähnlich Roget und Dornseiff; Textbasis sind die großen Epen der höfischen Zeit (ca. 1175 bis 1275), jeweils nach einer Standardedition. | S. 345 (PDF 1) | Projektbeschreibung |
| Das Projekt versteht sich als „first pioneering step" zu automatisierter nicht-alphabetischer Lexikographie älterer Sprachen; Indizes und Thesauri erschließen den Wortschatz onomasiologisch und semasiologisch und sind automatisch lemmatisiert. | S. 345 (PDF 1) | Projektbeschreibung |
| Begriffsindizes dienen Forschenden, die „motifs" oder „themes" suchen; das Begriffswörterbuch soll erstmals einen systematischen Überblick über den tatsächlichen semantischen Gebrauch geben und eine Grundlage für die Revision bestehender Wörterbücher sein. | S. 346 (PDF 2) | Position des Autors |
| Jedes Lemma trägt eine oder mehrere Begriffskategorien „depending on its possible range of meaning", als Zahlencode einer verbalen Taxonomie; das System hat „appr. 350" Kategorien. | S. 345 (PDF 1) | Projektbeschreibung |
| Beispiel *arm*: Kategorie 2103 (Körperteile) und 23308 & 2431 (Besitz und soziale Stände). Eine Bedeutung kann also aus mehreren Kategorien zusammengesetzt sein. | S. 346 (PDF 2); Tab. II, File 4 und 6, S. 349 | Projektbeschreibung |
| Für Homographen werden im gedruckten Thesaurus Textzeilen unter der mit „+" markierten Kategorie gedruckt; die Nutzer:in bestimmt die Bedeutung pro Beleg selbst. Künftige Ausgaben sollen das schon erledigt haben. | S. 346 (PDF 2) | Projektbeschreibung |
| Jeder Begriffsthesaurus muss vor Aufnahme ins Wörterbuch „manuell" disambiguiert werden. Das Verfahren läuft am Terminal: Nur für Belege, die von der häufigsten Bedeutung abweichen, wird ein Befehl eingegeben; ein Programm passt dann die Frequenzen an. | S. 346 (PDF 2) | Projektbeschreibung |
| Der Ansatz der KI-Forschung (grammatischer Parser plus Weltwissen) sei für historische, „tote" Sprachen praktisch unmöglich; stattdessen soll die Maschine Kriterien aus dem schon Gespeicherten selbst finden. | S. 346 (PDF 2) | Position des Autors |
| Gespeichert sind pro Wort: Lemma/Variante, zugehöriges Lemma, Wortart (S, A, P, Z, U), Homograph ja/nein, Begriffskategorien des Lemmas, die genaue Kategorie pro Textzeile aus den manuell disambiguierten Thesauri, Belegstelle, Kookkurrenzen im Fenster von 15 Wörtern davor und danach. | S. 346 bis 347 (PDF 2 bis 3) | Projektbeschreibung |
| Verfahren: Masterdatei im Konkordanzformat mit allen Angaben je Kontextwort; daraus Teildateien je Bedeutung eines Homographen (über die manuelle Disambiguierungsdatei); Mustersuche je Wortposition, im Vor- und Nachfeld und in beiden; Kriterien sind Zeichenketten (auch Stämme und Affixe), Zahlencodes der Begriffskategorien, Wortart, Worttyp. | S. 347, 351 (PDF 3, 7); Tab. I bis III | Entwurf |
| Der Zahlencode bildet die fortschreitende Untergliederung ab: Gemeinsame Ziffernfolgen von links zeigen je nach Länge mehr oder weniger gemeinsame Bedeutung. | S. 347 bis 351 (PDF 3, 7) | Projektbeschreibung |
| Ein Muster gilt als Kandidat, wenn es in mehr als zwei Fällen wiederkehrt; Muster, die nicht nur bei einer Bedeutung vorkommen, werden verworfen; die Summe der unterscheidenden Muster je Bedeutung heißt „common denominator". | S. 351 (PDF 7) | Entwurf |
| Aus simulierten Matrizen: Der Schlüssel liegt in den Begriffskategorien der Kontextwörter (bei *arm* 'Körperteil' etwa Kategorien zu Mensch als physischem Wesen, Arbeit, Kampf; bei 'Besitz/Stände' Kategorien zu Mensch als sozialem Wesen). | S. 351 (PDF 7) | eigene Beobachtung an Simulationen, nicht gemessen |
| Erwartung: 70 % richtige automatische Disambiguierung mit dem ersten Parser wären sehr zufriedenstellend, mindestens 80 % nach Verfeinerung; Restfehler vermutlich metaphorischer Gebrauch; die Quote hänge von Stil und Inhalt des Werks ab. | S. 351 (PDF 7) | Erwartung, keine Messung |
| Stand: Masterdatei fertig, Matrizenprogramm fast fertig, Mustererkennung in Arbeit (COBOL und BASIC); Hardware an der Bowling Green State University; kein Termin für erste Ergebnisse. | S. 351 bis 352 (PDF 7 bis 8) | Projektbericht |

## Daten, Methode, Zahlen

- Inventar: Begriffssystem mit ca. 350 Kategorien, Zahlencode hierarchisch (Auszug mit Codes 1 bis 2103, S. 345).
- Wortarten im Speicher: S, A, P, Z, U (S. 346); in den Kriterien zusätzlich eine Nullkategorie für Artikel, Konjunktionen usw. (S. 351).
- Kontextfenster: 15 Wörter vor und nach dem Stichwort (S. 347). Disambiguierungsdatei: bis zu 9 Textzeilen pro Eintrag (S. 347).
- Schwelle für Muster: Wiederkehr in mehr als zwei Fällen (S. 351); Beispielregel in Tab. II, File 11A: Kommt 2103 in Vor- und Nachfeld zusammen öfter als zweimal vor, ist die Bedeutung 2103 (S. 349).
- Erwartete Quoten: 70 %, später mindestens 80 % (S. 351). Keine gemessenen Werte.
- **Tabelle I** (S. 348, PDF 4): Ablaufdiagramm mit 13 Dateien und den Programmen KWIC, Disambig. File, Conceptual Conc., Keyword Matrix, Pattern Recognition (Report A, B), Parser, Automatic Disambiguation (Ausgabe: „Final Report Thesaurus").
- **Tabelle II** (S. 349, PDF 5): Formate der Dateien 1 bis 13, u. a. File 4 (Lemma mit `2103+&23308&2431`), File 6 (Disambiguierungsdatei: Textzeilennummern, Wortform, Kategorie), File 8 („no. of meanings+frequency").
- **Tabelle III** (S. 350, PDF 6, quer gedruckt): simulierte Matrizen für *arm* in Bedeutung 2103 (File 10A) und 23308&2431 (File 10B), je Kontextwort Position, Wortform, Typ (L/V) und Begriffskategorien.
- Hinweis zum Auftrag: Die Tabellen liegen auf PDF-Seite 4 (I), 5 (II) und 6 (III), nicht nur auf 4 und 6. Docling hat Tabelle II teilweise als Text erfasst, I und III nur als Bild.

## Wörtliche Stellen

> „Each lemma, however, also comes with one or more conceptual categories depending on its possible range of meaning." (S. 345)

> „[…] for each occurrence of the homograph that deviates from its most common meaning, where the text-lines are printed, a command for disambiguation has to be typed in." (S. 346)

> „[…] the same would be virtually impossible for historical or so-called "dead" languages." (S. 346)

> „Since the number code of our conceptual system reflects the progressing subcategorization of the verbal taxonomy, each common number combination, read from left to right, shows a lesser or higher degree of common meaning" (S. 347)

> „The remaining ambiguities will most likely reflect metaphorical usage of the vocabulary, which cannot possibly be integrated with a machine-produced thesaurus or dictionary, because of the high degree of subjective usage of the individual authors." (S. 351)

## Bezug zur Dissertation

- **Frühester belegter WSD-Versuch für das Mittelhochdeutsche** auf genau diesem Inventar. Für den Forschungsstand (Einleitung, Abschnitt 1 des Protokolls) ein Vorläufer: überwacht, aus manuell disambiguierten Belegen, mit Begriffskategorien des Kontexts als Merkmalen. Ergebnisse sind in diesem Beitrag keine berichtet (S. 352); ob später welche erschienen, ist offen.
- **PROTOKOLL §2 (Sense als Menge von Begriffszeigern):** Schon 1985 ist eine Bedeutung eine Kombination von Kategorien (*arm* = 23308 & 2431, S. 346, Tab. II). Stützt die Definition „Begriffsgruppe".
- **PROTOKOLL §2 und `knowledge/data.md` B1 und Abschnitt 3 (Herkunft von Silber und Typlisten):** Das damalige Verfahren setzte die häufigste Bedeutung als Vorgabe und korrigierte nur abweichende Belege per Befehl (S. 346). Das ist eine dokumentierte Praxis für die 1980er-Thesauri, keine Aussage über das heutige `@ana`. Als **Hypothese** für B1 brauchbar (Vorbelegung pro Typ, Korrektur pro Beleg), nicht als Beleg. Die Frage an KZW bleibt nötig.
- **PROTOKOLL §9.2 (MFS-Baseline):** Die häufigste Bedeutung war im Projekt selbst die Standardannahme der Annotation (S. 346). Das ist ein Argument, warum Silber zu MFS neigen könnte und warum der Silbervergleich die MFS-Baseline begünstigen kann. Nicht gemessen.
- **PROTOKOLL §9.1 Punkt 7 und offener Punkt 12, `knowledge/data.md` B11 (grobe Ebene über den Zahlencode):** Schmidt beschreibt den Code ausdrücklich als Abbild der Untergliederung, gemeinsame Präfixe als Maß gemeinsamer Bedeutung (S. 347). Direkte Stütze dafür, die grobe Ebene über Ziffernpräfixe zu definieren.
- **PROTOKOLL §1 Nebenfrage und §6 (`KEINE_PASST`, `MEHRERE`):** Schmidt erwartet einen Rest, der vor allem metaphorischer Gebrauch ist und sich nicht maschinell einordnen lässt (S. 351). Passt zu den Ausweichlabels.
- **PROTOKOLL §4 (Gattungsausgleich):** Das ursprüngliche Inventar wurde an höfischer Epik entwickelt (S. 345). Das stützt die Annahme, dass Lyrik und Fachliteratur schlechter abgedeckt sein könnten; geprüft ist das nicht.

## Grenzen und Einwände

- Werkstattbericht ohne Evaluation; die 70 bis 80 % sind Erwartungen (S. 351).
- Das Inventar von 1985 (ca. 350 Kategorien) ist nicht das heutige (`concepts.xml`: 567 Begriffe, `knowledge/data.md` Abschnitt 1); die Übertragbarkeit einzelner Angaben auf das heutige System ist nicht belegt.
- Die Disambiguierung betrifft die gedruckten Begriffsthesauri einzelner Werke, nicht das spätere Korpus der MHDBDB.

## Weiterführend

- Schmidt, K. M. (1978): Conceptual Glossaries: A New Tool for Medievalists. *Computers and the Humanities* 12, 19 bis 26 (S. 353).
- Schmidt, K. M.: „Errungenschaften, Holzwege und Zukunftsmusik …", in Sappler & Straßner (Hg.), Maschinelle Verarbeitung altdeutscher Texte (3. Symposion Tübingen 1977), Niemeyer, Tübingen 1980, S. 101 bis 111 (S. 353). Achtung: Hinkelmanns & Zeppezauer-Wachauer 2023, S. 181, datieren denselben Beitrag auf 1978 und stellen den Titel um („Errungenschaften, Zukunftsmusik und Holzwege"); nicht geklärt.
- Schmidt, K. M. (1979): Computers and Literary Criticism. Can the Conceptual Approach Break the Deadlock? *Sprache und Datenverarbeitung* I/II, 26 bis 33 (S. 353).
- Schmidt, K. M. (1980): Begriffsglossare und Indices zu Ulrich von Lichtenstein, 2 Bde. (S. 353).
- Schmidt, K. M. (1983): Conceptual Indices and a Conceptual Dictionary as Model for an Automated Retrieval System for Medieval Scholarly Research. In Burton & Short (Hg.), Sixth International Conference on Computers and the Humanities, 602 bis 613 (S. 353).
- Für das Begriffssystem: Roget, Dornseiff (S. 353, Anm. 1).

## Julias Markierungen im PDF

52 Freihandmarkierungen, keine Notizen (`md/Schmidt-1985-Parser-Homographen-MHD.markierungen.md`). Aufgenommen: Pionierrolle, Textbasis, onomasiologischer und semasiologischer Zugang, Lemmatisierung (S. 345); *arm* als Homograph mit Kategorien (S. 346); Motive und Themen, semantischer Gebrauch, manuelle Disambiguierung jedes Thesaurus, Abgrenzung von KI-Ansätzen und „dead languages", Maschine findet eigene Kriterien (S. 346); Mustererkennung im Vor- und Nachfeld (S. 347); „common denominator", Ausschluss nicht eindeutiger Muster, Begriffskategorien als Schlüssel, metaphorischer Rest (S. 351). Bewusst nicht aufgenommen: die markierte Bemerkung zu Zeitplänen („we never get the machine to do what it is supposed to within the time-frame …", S. 351), weil sie nichts zur Sache beiträgt.
