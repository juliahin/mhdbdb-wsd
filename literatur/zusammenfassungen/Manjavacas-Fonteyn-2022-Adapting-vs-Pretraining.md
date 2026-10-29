# Manjavacas & Fonteyn 2022a: Adapting vs. Pre-Training Language Models for Historical Languages

**Datei:** `pdf/Manjavacas-Fonteyn-2022-Adapting-vs-Pretraining.pdf` (nur lokal; 19 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganze Textebene gelesen, Tab. 1 und Abb. 5, 6 am Seitenbild geprüft, DOI aufgelöst. Das lokale PDF ist byte-gleich mit dem PDF auf episciences (`https://jdmdh.episciences.org/9152/pdf`, SHA-256 verglichen am 2026-10-28), also die veröffentlichte Fassung; es enthält keine Markierungen.

Seitenzählung: Der Artikel hat eine eigene Zählung 1 bis 19 in der Fußzeile; PDF-Seite = gedruckte Seite. Die Zeitschrift vergibt Artikelnummern statt Bandseiten (Artikel 9152).

## Bibliografie

- **Vollständig:** Manjavacas, Enrique & Lauren Fonteyn (2022). Adapting vs. Pre-training Language Models for Historical Languages. *Journal of Data Mining and Digital Humanities*, Sonderband NLP4DH, Artikel 9152, 19 S.
- **DOI/URL:** https://doi.org/10.46298/jdmdh.9152 (aufgelöst auf https://jdmdh.episciences.org/9152). Crossref: Band „NLP4DH“, Artikelnummer 9152, online 13.06.2022, ISSN 2416-5999 ✔. Episciences: eingereicht 01.03.2022, angenommen 05.04.2022, veröffentlicht 13.06.2022, Rubrik „Humanités numériques en langues“ ✔. Das PDF selbst nennt weder Band noch DOI, nur „Journal of Data Mining and Digital Humanities, ISSN 2416-5999, an open-access journal“ (Fußzeile jeder Seite).
- **Lizenz:** keine CC-Lizenz. Episciences und der HAL-Datensatz hal-03592137 (Version 3, über die HAL-API abgerufen am 2026-10-28) nennen „HAL authorisation v1“ (https://about.hal.science/hal-authorisation-v1/). Frei zugänglich (Diamond Open Access laut Fußzeile „open-access journal“), Nachnutzungsrechte darüber hinaus nicht geprüft.
- **Art:** begutachteter Zeitschriftenartikel (Sonderband zum Workshop NLP4DH; die Danksagung S. 15 nennt Organisator:innen und Publikum von NLP4DH)
- **Sprache:** Englisch
- **Modell:** MacBERTh auf Hugging Face (S. 5, Anm. 4; nicht aufgerufen).

## Worum es geht

Lohnt es sich, ein BERT-Modell für historisches Englisch von Grund auf zu trainieren, oder genügt es, ein gegenwartssprachliches Modell mit historischen Texten weiterzutrainieren (S. 1, 3)? Die Autoren vergleichen das gegenwartssprachliche BERT, zwei angepasste Varianten (TuringBERT, BERT-Adapted) und das von Grund auf trainierte MacBERTh an fünf Aufgaben: Wortartentagging, Eigennamenerkennung, WSD (zweifach), Lückentext und Datierung von Sätzen (S. 4 bis 13). MacBERTh ist überall außer bei der Eigennamenerkennung vorn, besonders bei wenig Trainingsdaten und in frühen Perioden (S. 14). Als Erklärung vermuten sie die auf Gegenwartssprache optimierte Tokenisierung und übernommene Verzerrungen (S. 3, 14 bis 15); Anpassen bleibe dennoch nützlich, wo Daten für ein eigenes Modell fehlen (S. 15).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Sprachmodelle könnten die Analyse historischer Texte „more objective“ machen, weil heutige Intuitionen zu anachronistischen Deutungen führen; ein Modell, das die manuelle Beteiligung „substitutes“, minimiere solche Urteile. | S. 2 | Position der Autoren |
| Historische Texte bringen Schreibvarianz und OCR/HTR-Fehler; tokenbasierte Modelle sollten darüber abstrahieren können. | S. 2 | Erwartung |
| Zwei Einwände gegen das Anpassen gegenwartssprachlicher Modelle: (1) die Tokenisierung ist auf Gegenwartssprache optimiert und zerlegt historische Wörter uninformativ; (2) das Modell könnte anachronistische Verzerrungen in Grammatik und Semantik mitbringen. Fehleranalysen historischer Sense-Disambiguierung zeigten, dass gegenwartssprachliche Modelle heutige Lesarten aufzwingen. | S. 3 | Begründung; Fehleranalyse referiert (Fonteyn 2020) |
| Verglichene Modelle (Tab. 1): BERT (3,3 Mrd. Tokens, Gegenwart), TuringBERT (BERT angepasst auf 5,1 Mrd. Tokens, 1760 bis 1900), BERT-Adapted (BERT angepasst auf das MacBERTh-Korpus, 3,9 Mrd., 1450 bis 1950), MacBERTh (von Grund auf auf demselben Korpus); alle Vokabular 30.000. | S. 4 bis 5, Tab. 1 | eigene Versuchsanlage |
| MacBERTh-Korpus: EEBO, EVANS, ECCO, CLMET3.1, Hansard, COHA, 1473 bis 1950, ca. 3,9 Mrd. Wörter; Fremdsprachiges per Spracherkennung entfernt. | S. 4 bis 5 | Datenbeschreibung |
| POS-Tagging (PPCEME): MacBERTh überall am besten, der Vorsprung ist bei wenig Trainingsdaten am größten und nicht auf frühe Perioden beschränkt. | S. 5 bis 6, Abb. 1 und 2 | eigenes Ergebnis |
| NER (HIPE-2022, britische Zeitungen des 18. und 19. Jh.): kleine Unterschiede; TuringBERT knapp vorn, möglicherweise weil die Testdaten aus derselben Sammlung stammen wie seine Trainingsdaten. | S. 8, Abb. 3 und 4 | eigenes Ergebnis, Deutung |
| WSD ohne Feinjustieren (Sense-Zentroide aus OED-Belegen): bei Inhaltswörtern alle Modelle über den Baselines, MacBERTh vorn; ab dem 18. Jh. nähern sich die Modelle an. Bei Funktionswörtern kein klares Muster. | S. 8 bis 9, Abb. 5 | eigenes Ergebnis |
| Inhalts- und Funktionswörter werden getrennt, weil „lexical or ‘contentful’ semantics can be considered distinct from grammatical or ‘function’ semantics“; Funktionswörter sind hier Präpositionen, Pronomen, Konjunktionen, Interjektionen. | S. 9 | Begründung, Hinweis auf Hamilton et al. 2016 |
| Mit begrenzten Beispielen je Sense: MacBERTh schlägt die Mehrheits-Baseline schon mit 2 Sätzen je Sense; nach etwa 10 Sätzen (etwa ein Fünftel des Durchschnitts je Sense) nähern sich die Modelle ihrem Optimum; kaum Streuung über 20 Ziehungen. | S. 9 bis 10, Abb. 6 | eigenes Ergebnis |
| Word-in-Context (gleicher Sense ja/nein): Genauigkeit 85 bis 98 %; am schwersten Paare aus dem 15. bis 17. Jh.; MacBERTh vorn, mit größerem Abstand in frühen Perioden; BERT-Adapted besser als BERT. | S. 10 bis 11, Abb. 7 bis 9 | eigenes Ergebnis |
| Lückentext (Mean Reciprocal Rank) und Satzdatierung (mittlerer absoluter Fehler): MacBERTh vorn, bei der Datierung knapp unter 10 Jahren Vorsprung. | S. 11 bis 13, Abb. 10 bis 13 | eigenes Ergebnis |
| Fazit: Von Grund auf historisch vortrainieren ist der verlässlichste Weg; Ausnahme NER. Die Vorteile sind bei knappen Feinjustier-Daten am größten. | S. 14, Abschnitt IV | eigenes Ergebnis |
| Hypothese, nicht getestet: Die feste Tokenisierung behindert das Anpassen. | S. 14 bis 15 | Vermutung, gestützt auf referierte Arbeiten |
| Anpassen ist trotzdem nützlich; manchmal ist es „the only possibility, due to the sparsity of text in the target domain“. | S. 15 | Einschätzung |

## Daten, Methode, Zahlen

- **POS (S. 5):** PPCEME, 1450 bis 1700, 448 Dokumente, ca. 1,7 Mio. Wörter; Splits nach Han & Eisenstein 2019: 115 Test-, 316 Trainings-, 17 Entwicklungsdateien; Lernkurve ab 50 Dateien.
- **NER (S. 8):** HIPE-2022, Teilmenge topres19th, ca. 3.300 Entitäten (nur Orte), 5.874 Trainings- und 646 Entwicklungssätze, 10 Läufe je Modell.
- **WSD mit Zentroiden (S. 8):** 191 OED-Lemmata mit je mindestens 50 Belegsätzen und mindestens zwei Senses, 17.878 Sätze, Aufteilung in Training und Test proportional zu den Sätzen je Sense.
- **Abb. 6 (S. 9), am Seitenbild abgelesen [am PDF zu prüfen]:** Mehrheits-Baseline etwa 0,51, Zufall etwa 0,39; bei vollem Training MacBERTh etwa 0,69, BERT-Adapted etwa 0,64, BERT etwa 0,62, TuringBERT etwa 0,61. Mit 1 Satz je Sense liegen alle Modelle unter der Mehrheits-Baseline.
- **Abb. 5 (S. 9), am Seitenbild abgelesen [am PDF zu prüfen]:** Inhaltswörter: Mehrheits-Baseline etwa 0,44 bis 0,52, MacBERTh von etwa 0,54 (1400) bis 0,75 (1900). Funktionswörter: Mehrheits-Baseline etwa 0,57 bis 0,73, Modelle meist darüber.
- **Word-in-Context (S. 10):** 416 Lemmata, 84.712 Sätze; zu jedem Satz ein positives Paar (gleicher Sense) und ein negatives (anderer Sense desselben Lemmas); Feinjustieren 5 Epochen, Batchgröße 16. Der Text nennt 85 bis 98 % (S. 10); die Zellen in Abb. 7 (S. 11, Textebene) reichen von 0,83 (TuringBERT) bis 0,98.
- **Lückentext (S. 12):** 42.961 Sätze, 731 Wörter, im Mittel 58,8 Sätze je Wort; nur Zielwörter, die kein Modell in Teilwörter zerlegt.
- **Satzdatierung (S. 12 bis 13):** 100.000 Trainingspaare, 5.000 Testpaare, Hintergrundkorpus 5.000 Sätze, 100 je 50-Jahres-Abschnitt.
- **Kleine Unstimmigkeit:** Text S. 4 nennt für das MacBERTh-Korpus 1473 bis 1950, Tab. 1 (S. 5) 1450 bis 1950.

## Wörtliche Stellen

> „[…] some classification error analyses of historical sense disambiguation tasks indicate that present-day language models indeed erroneously impose a present-day interpretation onto the historical material“ (S. 3)

> „[…] lexical or ‘contentful’ semantics can be considered distinct from grammatical or ‘function’ semantics, both in terms of how senses can be derived from contextual information […] and in terms of the diachronic dynamics“ (S. 9)

> „[…] in some cases, adaptation is the only possibility, due to the sparsity of text in the target domain“ (S. 15)

## Bezug zur Dissertation

- **PROTOKOLL §3 (nur NOM, VRB, ADJ; Präpositionen und Adverbien ausgeschlossen):** Das Paper trennt Inhaltswörter (Nomen, Adjektive, Verben) von Funktionswörtern (Präpositionen, Pronomen, Konjunktionen, Interjektionen) mit der Begründung, deren Semantik sei grammatisch und anders aus dem Kontext ableitbar (S. 9). Das stützt die Begründung im Protokoll für Präpositionen („funktional-grammatisch“). Für Adverbien sagt es nichts, sie fehlen in beiden Listen.
- **Anachronismus als Fehlerquelle:** Die Sorge, gegenwartssprachlich vortrainierte Modelle zwängen historischen Belegen heutige Lesarten auf (S. 3), betrifft auch generative LLMs, die überwiegend auf Gegenwartssprache trainiert sind. Gezeigt ist das hier nur für BERT-artige Modelle und Englisch der Neuzeit; für die Dissertation ist es eine zu prüfende Hypothese, kein Befund. Eine Fehleranalyse der LLM-Ausgaben (etwa anhand der Adjudikations-Ursachencodes, PROTOKOLL §7) könnte sie für Mittelhochdeutsch prüfen.
- **Frühe Perioden sind schwerer** (WiC: 15. bis 17. Jh., S. 10; Zentroid-WSD: niedrigere Werte vor 1700, Abb. 5). Mittelhochdeutsch liegt noch weiter zurück; das Paper erlaubt keinen Schluss darauf, macht aber plausibel, dass Schwierigkeit mit Zeitabstand wächst.
- **Datenlage Mittelhochdeutsch:** Das MacBERTh-Korpus hat ca. 3,9 Mrd. Wörter (S. 4). Für Mittelhochdeutsch liegt nach Beck & Köllner 2023 (S. 36) das ReM mit 2,3 Mio. Wörtern vor. Das Paper selbst nennt Anpassen als einzige Möglichkeit bei dünner Datenlage (S. 15); ein von Grund auf trainiertes mhd. Modell nach diesem Rezept ist damit unrealistisch. Das ist eine Folgerung aus zwei Quellen, nicht Aussage des Papers.
- **PROTOKOLL §9.2 (Baseline):** Auch hier ist die Mehrheits-Baseline ein ernsthafter Gegner: Mit 1 Beispiel je Sense liegen alle Modelle darunter (Abb. 6, S. 9). Die Baseline wird aber aus denselben Wörterbuchbelegen gelernt, nicht aus einem Korpus.
- **PROTOKOLL §1:** Das Paper liefert kein Ergebnis zu LLM-gestützter WSD im Sinn der Dissertation (keine generativen Modelle, kein Prompting, keine menschliche Annotation, Gold = OED-Zuordnung).

## Grenzen und Einwände

- Nur Englisch (1450 bis 1950), nur BERT-base; die Autoren begründen die Beschränkung mit dem Budget (S. 4).
- WSD-Gold sind die Sense-Zuordnungen der OED-Belege, also lexikografische Auswahlbelege, kein laufender Text; keine Übereinstimmungsmessung.
- Die meisten Ergebnisse stehen nur als Grafiken; genaue Zahlen fehlen im Text (abgelesene Werte oben markiert).
- Keine Signifikanztests; bei NER sind die Unterschiede nach eigener Aussage „negligible“ (S. 8).
- Die Erklärung über die Tokenisierung ist ausdrücklich eine ungeprüfte Hypothese (S. 14 bis 15).
- Die These, Modelle machten die Analyse „more objective“ (S. 2), ist eine Position; dass die Modelle ihrerseits Verzerrungen mitbringen, räumt das Paper an anderer Stelle selbst ein (S. 3).

## Weiterführend

- Manjavacas & Fonteyn 2021, MacBERTh, NLP4DH @ ICON 2021 (S. 17): Herkunft der OED-Datensätze.
- Fonteyn 2020, „What about grammar?“, CHR 2020, CEUR 2723, S. 257 bis 268 (S. 3, 16): Fehleranalyse mit anachronistischen Lesarten.
- Beelen et al. 2021, historically-aware targeted sense disambiguation, Findings of ACL, S. 2751 bis 2761 (S. 10, 15).
- Hosseini et al. 2021, Neural Language Models for Nineteenth-Century English, JOHD 7 (S. 4, 17).
- Tahmasebi & Risse 2017, Word Sense Change in den DH (S. 2, 18).
- Pilehvar & Camacho-Collados 2019, WiC (S. 10, 17).
- Manjavacas Arevalo & Fonteyn 2022b, Non-Parametric WSD (Folgearbeit; liegt vor, `zusammenfassungen/Manjavacas-Fonteyn-2022-Nonparametric-WSD.md`).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem PDF auf episciences und hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
