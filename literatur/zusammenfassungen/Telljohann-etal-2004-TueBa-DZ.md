# Telljohann, Hinrichs & Kübler 2004: The TüBa-D/Z Treebank

**Datei:** `pdf/Telljohann-etal-2004-TueBa-DZ.pdf` (nur lokal; 4 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganzes PDF an der Textebene gelesen, Abbildungen am Seitenbild angesehen. Priorität 3 (Hintergrund), daher knapp.

**Seitenzählung:** gedruckt S. 2229 bis 2232 = PDF-Seite 1 bis 4 (Seitenzahl in der Fußzeile); PDF-Seite = gedruckte Seite − 2228. Zitiert wird die gedruckte Seite, die PDF-Seite in Klammern.

## Bibliografie

- **Vollständig:** Telljohann, Heike, Erhard Hinrichs & Sandra Kübler (2004). The TüBa-D/Z Treebank: Annotating German with a Context-Free Backbone. In: Maria Teresa Lino, Maria Francisca Xavier, Fátima Ferreira, Rute Costa & Raquel Silva (Hg.), *Proceedings of the Fourth International Conference on Language Resources and Evaluation (LREC'04)*, Lissabon, Mai 2004. European Language Resources Association (ELRA), S. 2229 bis 2232.
- **DOI/URL:** keine DOI. https://aclanthology.org/L04-1096/ (abgerufen 2026-10-29: Titel, Autor:innen, Herausgeber:innen, Mai 2004, Lissabon, ELRA; Seitenfeld dort leer). Seiten aus den gedruckten Seitenzahlen im PDF ✔. Das lokale PDF ist **byte-gleich** (SHA-256) mit http://www.lrec-conf.org/proceedings/lrec2004/pdf/135.pdf. Lizenz laut ACL Anthology für Material vor 2016: CC BY-NC-SA 3.0.
- **Schreibung im Titel:** Der Titel im PDF schreibt „Tüba-D/Z“, der Text „TüBa-D/Z“; die ACL Anthology übernimmt „Tüba-D/Z“. Im Text der Dissertation „TüBa-D/Z“, im Titel wie im Original.
- **Art:** begutachteter Konferenzbeitrag (LREC)
- **Sprache:** Englisch

## Worum es geht

Das Paper beschreibt die Baumbank TüBa-D/Z geschriebenen Deutschs (Zeitungstexte der *taz*) kurz nach ihrer ersten Veröffentlichung im Dezember 2003 und vergleicht ihr Annotationsschema mit der unabhängig entstandenen TIGER-Baumbank (S. 2229 (PDF 1)). Beide annotieren Phrasenstruktur plus eine Ebene der Prädikat-Argument-Struktur und verwenden STTS für die Wortarten. TüBa-D/Z kommt ohne kreuzende Kanten aus („context-free backbone“): Topologische Felder ordnen den Satz, grammatische Funktionen und diskontinuierliche Bezüge stehen in Kantenlabels (S. 2230 (PDF 2)). Unauflösbare Ambiguität wird durch unterspezifizierte Labels und Hochanbindung dargestellt (S. 2229 (PDF 1)). Zahlen zu Übereinstimmung oder Annotationsqualität enthält das Paper nicht.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Datengrundlage: Zeitungskorpus *die tageszeitung* (taz); TIGER nutzt die Frankfurter Rundschau. | S. 2229 (PDF 1), Abschn. 1 | Projektbeschreibung |
| Umfang: TüBa-D/Z „at present appr. 15.000 trees“; TIGER 40.000 annotierte Sätze. | S. 2229 (PDF 1), Abschn. 1 | Projektangabe (Stand 2004) |
| Veröffentlicht im Dezember 2003 zusammen mit einem ausführlichen Stylebook (Telljohann et al. 2003). | S. 2229 (PDF 1), Abschn. 2 | Projektangabe |
| Annotation **halbautomatisch** mit dem grafischen Werkzeug Annotate (Plaehn 1998). | S. 2229 (PDF 1), Abschn. 1 | Projektangabe |
| Schema abgeleitet von der Verbmobil-Baumbank gesprochenen Deutschs, erweitert für geschriebene Texte. Vier Ebenen: lexikalisch, phrasal, topologische Felder, Satz. | S. 2229 (PDF 1), Abschn. 2 | Beschreibung |
| Kantenlabels kodieren grammatische Funktionen und Kopf/Nicht-Kopf; für die Wortarten „the STTS (Schiller et al., 1995) is used“. | S. 2229 (PDF 1), Abschn. 2 | Beschreibung |
| **Ambiguität:** „Syntactic and semantic ambiguity is treated in terms of underspecification“, gestützt auf Hochanbindung und unterspezifizierte Knotenlabels. Ist Disambiguierung möglich, wird das eindeutige Label gewählt (z. B. OPP-MOD); sonst erhält der Modifikator das unterspezifizierte Label MOD und wird am höchstmöglichen Knoten angebunden. | S. 2229 (PDF 1), Abschn. 2 | Richtlinie |
| Kein kreuzendes Kantensystem: Subjekt und finites Verb stehen in den jeweiligen topologischen Feldern, ihre Funktion zeigen nur Kantenlabels; diskontinuierliche Konstituenten bekommen eigene Labels (z. B. OA-MOD). TIGER erlaubt kreuzende Kanten. | S. 2230 (PDF 2), Abschn. 3.1 | Vergleich |
| Inventar: TüBa-D/Z 25 Knotenlabels und 36 Kantenlabels; TIGER 25 Knoten- und 50 Kantenlabels. | S. 2230 (PDF 2), Abschn. 3.2 | Vergleich |
| TüBa-D/Z-Phrasen sind hierarchischer, TIGER-Phrasen flach mit funktionaler Markierung (NK, MO, OP). Gemeinsam: STTS, Prä-/Postmodifikator-Unterscheidung, Named Entities, Ellipsen. | S. 2230 bis 2231 (PDF 2 bis 3), Abschn. 3.2 | Vergleich |
| TüBa-D/Z-Bäume taugen direkt zum Training von PCFGs; TIGER-Bäume müssen erst umgewandelt werden, kreuzende Kanten kommen in „approximately 30% of all trees“ vor. | S. 2231 (PDF 3), Abschn. 3.2 | Angabe ohne Herleitung |
| **Keine Angaben zu Übereinstimmung, Konsistenzprüfung oder Zahl der Annotator:innen.** | ganzes Paper gelesen | Befund dieser Prüfung |

## Daten, Methode, Zahlen

- Korpus: taz, geschriebenes Gegenwartsdeutsch; ca. 15.000 Bäume (2004); bereits als Trainingsmaterial genutzt für morphologische Disambiguierung, partielles Parsing und Topologische-Felder-Parsing (S. 2229 (PDF 1), mit Literatur).
- Inventar: 25 Knoten-, 36 Kantenlabels; Wortarten STTS (S. 2229 bis 2230 (PDF 1 bis 2)).
- Werkzeug: Annotate (NEGRA-Format), halbautomatisch (S. 2229 (PDF 1), Anm. 2).
- Fünf Beispielbäume (Abb. 1 bis 5), drei aus TüBa-D/Z, zwei aus TIGER.
- Keine Annotator:innen, keine Maße, keine Fehleranalyse.

## Wörtliche Stellen

> „Syntactic and semantic ambiguity is treated in terms of underspecification, which relies on the principle of high attachment and utilizes underspecified node labels.“ (S. 2229 (PDF 1))

> „If the ambiguity cannot be resolved, the ambiguous modifier receives the underspecified label MOD and is attached to the highest possible node.“ (S. 2229 (PDF 1))

## Bezug zur Dissertation

- **PROTOKOLL §6, Status `MEHRERE`:** TüBa-D/Z ist ein Gegenbeispiel zu HiTS und STTS: Hier wird unauflösbare (auch semantische) Ambiguität **ausdrücklich** als eigenes, unterspezifiziertes Label annotiert, das nur gewählt wird, wenn die spezifische Entscheidung nicht möglich ist (S. 2229 (PDF 1)). Das ist strukturell dieselbe Logik wie ein Ausweichlabel neben den Senses. In der Begründung von §6 lassen sich beide Seiten nennen: HiTS gegen Ambiguitätsmarkierung (Zuverlässigkeit), TüBa-D/Z dafür (Unterspezifikation statt erzwungener Entscheidung). Die Unterspezifikation betrifft Syntax, nicht Wortbedeutung.
- **Henrich 2015 (WSD Deutsch, Goldstandard):** Die manuelle GermaNet-Sense-Annotation, die Henrich in Kap. 5.3 beschreibt, liegt auf dieser Baumbank (Zusammenfassung `Henrich-2015-WSD-GermaNet.md`, Abschnitt Daten). Dieses Paper von 2004 erwähnt Senses noch nicht; es ist nur für die Baumbank selbst zu zitieren.
- **Zitierweise STTS:** Das Paper zitiert „Schiller, Teufel & Thielen 1995, Guidelines für das Tagging deutscher Textkorpora mit STTS“ (S. 2232 (PDF 4)). Das passt weder zur Fassung 1995 („Vorläufige Guidelines“, vier Personen) noch zu 1999 genau (siehe `Schiller-etal-1999-STTS.md`, Bibliografie).

## Grenzen und Einwände

- Vierseitiges Konferenzpapier, im Kern ein Schemavergleich; Umfang und Inventar sind Stand 2004 und durch das Stylebook 2017 überholt (dort 104.787 Sätze und 42 plus 4 Kantenlabels, siehe `Telljohann-etal-2017-TueBa-DZ-Stylebook.md`).
- Keine Qualitätssicherung beschrieben: weder Übereinstimmung noch Konsistenzprüfung.
- Die Angabe „approximately 30%“ kreuzender Kanten in TIGER ist nicht hergeleitet.
- Für eine WSD-Arbeit zu Mittelhochdeutsch nur als Hintergrund: Herkunft der Baumbank, auf der Henrichs Sense-Annotation liegt, und ein Beispiel für Unterspezifikation als Annotationsprinzip.

## Weiterführend

- Telljohann, Hinrichs & Kübler 2003, Stylebook (S. 2232 (PDF 4)); die letzte Fassung liegt als `pdf/Telljohann-etal-2017-TueBa-DZ-Stylebook.pdf` vor.
- Brants et al. 2002, The TIGER treebank, TLT 2002 (S. 2231 (PDF 3)); in `references.txt` steht TIGER als Brants et al. 2004 (`tiger2004`).
- Hinrichs et al. 2000, Verbmobil-Baumbanken (S. 2232 (PDF 4)).

## Julias Markierungen im PDF

Für dieses PDF gibt es keine Datei `md/…markierungen.md`; `markierungen.py` fand am 2026-10-29 keine Anmerkungen.
