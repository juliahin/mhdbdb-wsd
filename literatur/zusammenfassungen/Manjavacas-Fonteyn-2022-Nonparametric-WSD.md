# Manjavacas Arevalo & Fonteyn 2022b: Non-Parametric Word Sense Disambiguation for Historical Languages

**Datei:** `pdf/Manjavacas-Fonteyn-2022-Nonparametric-WSD.pdf` (nur lokal; 12 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganze Textebene gelesen, Abb. 1 bis 4 und Tab. 2 am Seitenbild geprüft, DOI aufgelöst. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-10-28), also die Verlagsfassung; es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 122 + n (PDF 1 = S. 123, PDF 12 = S. 134). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Manjavacas Arevalo, Enrique & Lauren Fonteyn (2022). Non-Parametric Word Sense Disambiguation for Historical Languages. In: Mika Hämäläinen, Khalid Alnajjar, Niko Partanen & Jack Rueter (Hg.), *Proceedings of the 2nd International Workshop on Natural Language Processing for Digital Humanities (NLP4DH)*. Taipei: Association for Computational Linguistics, S. 123 bis 134.
- **DOI/URL:** https://doi.org/10.18653/v1/2022.nlp4dh-1.16 (aufgelöst auf https://aclanthology.org/2022.nlp4dh-1.16; Crossref: S. 123 bis 134 ✔). Herausgeber:innen, Ort, Monat November aus dem BibTeX der Anthology ✔. Kopfzeile S. 123: „pages 123–134, November 20, 2022“ ✔.
- **Name:** Im PDF steht „Enrique Manjavacas“ (S. 123), Anthology und Crossref führen „Manjavacas Arevalo“. Für die Bibliografie die Form der Anthology; beim Zitieren auffindbar unter beiden.
- **Lizenz:** CC BY 4.0 (ACL Anthology, Material ab 2016, laut FAQ und Fußzeile, abgerufen 2026-10-28).
- **Art:** Workshop-Beitrag (ACL-Workshop NLP4DH)
- **Sprache:** Englisch
- **Modelle:** MacBERTh und GysBERT auf Hugging Face (S. 124, Anm. 1; nicht aufgerufen).

## Worum es geht

Die Autoren fragen, ob sich vortrainierte Encoder-Modelle (im Paper „LLMs“ genannt, gemeint sind BERT-artige Modelle) mit wenig annotiertem Material für WSD in historischem Englisch und Niederländisch (1450 bis 1950) feinjustieren lassen (S. 123 bis 124). Sie nutzen ein parameterfreies, metrikbasiertes Verfahren: Aus wenigen Beispielsätzen je Sense wird ein Mittelwertvektor gebildet, ein neuer Beleg erhält den ähnlichsten (S. 124 bis 125). Getestet wird auf Belegsätzen aus OED und WNT und an einer kleinen Fachaufgabe (*mass*/*weight* in Texten der Royal Society) (S. 125, 128). Das Feinjustieren hebt die Werte um 0,2 oder mehr über eingefrorene Einbettungen, auch für Lemmata, die im Training nicht vorkamen; historisch vortrainierte Modelle (MacBERTh, das hier eingeführte GysBERT) liegen vorn, aber erst nach dem Feinjustieren (S. 126 bis 127, 130).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| In den Geisteswissenschaften wächst der Bedarf an automatischer WSD; bei historischen Sprachen gibt es keine Muttersprachler:innen und „expert annotators are rare“. | S. 123, Abschnitt 1 | Problemstellung |
| Annotierte WSD-Ressourcen sind knapp und teuer, bei historischen Sprachen verschärft durch seltenes Expertenwissen; deshalb Fokus auf Dateneffizienz. | S. 124 | Problemstellung |
| Verfahren: episodisches Feinjustieren aller Modellparameter; je Episode eine Support-Menge (höchstens 10 Sätze) und eine Query-Menge (höchstens 20); Sense-Repräsentation = Mittelwert der Einbettungen der Support-Sätze; Wahrscheinlichkeit proportional zur Ähnlichkeit, Softmax; Lemmata gleichverteilt gezogen; höchstens 3.000 Schritte. | S. 124 bis 125, Abschnitt 2.1 | eigene Methode, nach Matching und Prototypical Networks |
| Voraussetzung: Der wahre Sense jedes Query-Satzes muss in der Support-Menge vertreten sein. | S. 124 bis 125, Anm. 3 | Methode |
| Historische Texte erschweren NLP durch uneinheitliche Schreibung, fehleranfällige Digitalisierung und Sprachwandel über lange Zeiträume; deshalb von Grund auf historisch vortrainierte Modelle, die sich in früheren Arbeiten als stärker erwiesen hätten. | S. 125, Abschnitt 2.2 | Begründung, Vorbefund referiert (Manjavacas & Fonteyn 2021, 2022) |
| Daten aus OED und WNT: je 1.000 Wörter nach Frequenzbändern gezogen und im Wörterbuch gesucht; 10 % der Lemmata als „held-out“, je Lemma 50 % der Belegsätze für den Test, nach der Sense-Verteilung. | S. 125 bis 126, Abschnitt 3, Anm. 6 | eigene Datengewinnung |
| GysBERT: nach Aussage der Autoren das erste historisch vortrainierte Modell für Niederländisch; Delpher (gefiltert über Perplexität eines Zeichen-5-Gramm-Modells, Schwelle 20) und DBNL, 1500 bis 1950, ca. 7,1 Mrd. Tokens. | S. 126, Abschnitt 3.1 | eigenes Modell |
| Feinjustieren steigert gegenüber eingefrorenen Einbettungen um 0,2 Punkte oder mehr, stärker bei Macro-F1 und mehr Beispielen. | S. 126, Abschnitt 4.1; Abb. 1 und 2 | eigenes Ergebnis |
| Eingefrorene Einbettungen liegen bei Micro-F1 **unter** der MFS-Baseline, bei Macro-F1 nur knapp darüber. | S. 127 | eigenes Ergebnis |
| Für nicht gesehene Lemmata sinkt die Leistung um weniger als 0,1; mehr Beispiele je Sense helfen bis 5, danach Plateau. | S. 127 | eigenes Ergebnis |
| Niederländisch etwas besser, vermutlich wegen schieferer Sense-Verteilung, erkennbar am hohen Micro-F1 der MFS-Baseline. | S. 127 | eigenes Ergebnis, Deutung |
| Historisch vortrainierte Modelle schlagen gegenwartssprachliche „with a safe margin“, aber das zeigt sich erst nach dem Feinjustieren, nicht bei eingefrorenen Einbettungen. | S. 127; S. 130 | eigenes Ergebnis |
| Wenig Training: Schon 50 Trainingslemmata bringen Gewinne über eingefrorene Einbettungen; für OED reichen etwa 500 Lemmata mit 10 Beispielen je Sense. Beim WNT braucht es 500 Lemmata und 50 Beispiele je Sense, um die MFS-Baseline bei Micro-F1 zu schlagen. | S. 128, Abschnitt 4.2; Abb. 3 und 4 | eigenes Ergebnis |
| Zeit: Historisch vortrainierte Modelle sind über alle Jahrhunderte besser, der Vorsprung ist in den früheren Jahrhunderten größer. | S. 128, Abschnitt 4.3; Abb. 5 | eigenes Ergebnis |
| Fachaufgabe *mass*/*weight*: 1.500 Belege (621 *mass*, 879 *weight*) aus 56.813 im Royal Society Corpus, von einer Fachperson in 6 Kategorien annotiert; das parameterfreie Verfahren ist am besten und am stabilsten, der Vorsprung bei Macro-F1 hält aber angesichts der Standardabweichung nicht. | S. 128 bis 129, Abschnitt 4.4; Tab. 2 und 4 | eigenes Ergebnis |
| Normales Feinjustieren mit Klassifikationsschicht schwankt stark zwischen den Folds, vermutlich wegen weniger Beispiele und vieler Parameter. | S. 129 | eigenes Ergebnis, Deutung |

## Daten, Methode, Zahlen

- **Tab. 1 (S. 126):** OED 846 Lemmata, 22.004 Senses, 121.684 Belegsätze; WNT 755 Lemmata, 22.547 Senses, 137.131 Belegsätze.
- **Senses und Belege:** Wörterbuch-Senses mit Definition und datierten Belegzitaten (Tab. 3, S. 133, Beispiel *rat*). Das Verfahren selbst nutzt die Definitionen nicht, nur die Belegsätze.
- **Modelle (S. 126):** Englisch MacBERTh gegen BERT-base uncased; Niederländisch GysBERT gegen BERTje und RobBERT; dazu jeweils eingefrorene Varianten und eine MFS-Baseline. Maße: Micro- und Macro-F1, gemittelt über Lemmata, weil die Sense-Verteilung oft stark schief ist.
- **GysBERT (S. 126):** 5,8 Mrd. Tokens Delpher, 1,3 Mrd. DBNL; WordPiece-Vokabular 30.000; 1.000.000 Schritte; Sequenzlänge 128.
- **Ergebnisse im Text (S. 130):** nicht gesehene Lemmata, volles Training: Micro-F1 0,627 (Englisch) und 0,71 (Niederländisch), +40,3 % bzw. +34,22 % gegenüber eingefroren. Nur 50 Trainingslemmata und 2 Beispiele je Sense: 0,557 und 0,617 (+32,8 % bzw. +24,4 %).
- **MFS-Baseline, aus Abb. 1 und 2 abgelesen (S. 127):** OED Micro-F1 etwa 0,48, Macro-F1 etwa 0,17; WNT Micro-F1 etwa 0,69, Macro-F1 etwa 0,32. Die Werte stehen nur als Linie in den Abbildungen, nicht als Zahl im Text [am PDF zu prüfen]. Damit liegt GysBERT auf nicht gesehenen Lemmata (0,71) nur knapp über der MFS-Baseline bei Micro-F1.
- **Tab. 2 (S. 129, am Seitenbild geprüft),** 10-fache Kreuzvalidierung, *mass*/*weight*:

| Modell | Micro-F1 | SD | Macro-F1 | SD |
|---|---|---|---|---|
| KNN | 0,830 | 0,007 | 0,695 | 0,032 |
| SVC | 0,819 | 0,007 | 0,601 | 0,035 |
| Standard (Klassifikationsschicht) | 0,827 | 0,029 | 0,520 | 0,066 |
| parameterfrei | **0,864** | 0,006 | **0,699** | 0,025 |

- **Kategorienschema (Tab. 4, S. 134):** N (Ding/Gegenstand), M (Masse), W (Gewicht), W/M („unclear whether the example refers to MASS or WEIGHT“), COL (Ansammlung), MET (Bedeutsamkeit). Zur Annotation selbst nur: „manually annotated by a domain expert“ (S. 128); keine zweite Annotator:in, keine Übereinstimmung.

## Wörtliche Stellen

> „[…] researchers are unable to solicit native speaker interpretations and expert annotators are rare.“ (S. 123)

> „Overall, frozen baselines underperform the MFS baseline in terms of micro F1.“ (S. 127)

> „[…] the superiority of historical pre-training cannot be concluded on the basis of the frozen baselines alone, but surfaces only after applying the non-parametric fine-tuning.“ (S. 127)

## Bezug zur Dissertation

- **PROTOKOLL §1 und §9.2 (LLM gegen MFS):** Das Paper zeigt für historische Sprachen, wie stark MFS bei schiefer Sense-Verteilung ist: Eingefrorene Einbettungen verlieren bei Micro-F1 gegen MFS (S. 127), und beim WNT braucht selbst das feinjustierte Modell viel Training, um MFS zu schlagen (S. 128). Das stützt die Wahl der MFS-Baseline als ernsthaften Gegner und die getrennte Macro-Auswertung (§9.2, Macro-Genauigkeit nach Sense); das Paper berichtet beide Maße aus demselben Grund (S. 126).
- **Abgrenzung zur eigenen Methode:** Es geht um Encoder-Modelle mit Feinjustieren auf annotierten Beispielen, nicht um generative LLMs mit Prompt. Das Verfahren verlangt für jeden Sense Beispielsätze (S. 124 bis 125, Anm. 3). In der MHDBDB sind 42 % der Senses polysemer Lemmata mit Silber nie belegt (`knowledge/data.md`, B9), und D0 hat kaum Silber (PROTOKOLL §3); das Verfahren wäre dort für viele Senses nicht anwendbar.
- **Wie viele Beispiele:** Ab etwa 5 Beispielen je Sense tritt ein Plateau ein (S. 127); mit 2 Beispielen je Sense und 50 Lemmata erreicht man schon 0,557 bzw. 0,617 Micro-F1 (S. 130). Das ist eine Größenordnung für eine mögliche Few-Shot-Variante der LLM-Konfiguration (Freeze 2, PROTOKOLL §4.10), dort aber mit dem Leckrisiko abzuwägen: Beispiele aus dem Silber dürfen keine Stichproben-Tokens enthalten (§9.2, Leave-out).
- **Testdaten aus Wörterbüchern:** OED- und WNT-Belege sind gewählt, um Senses zu illustrieren, keine laufenden Texte. Ihre Sense-Verteilung und damit die MFS sind Eigenschaften der Wörterbücher, nicht eines Korpus. Für die Dissertation stützt das, MFS aus Korpus-Silber zu lernen (§9.2) und die Werte nicht direkt mit diesem Paper zu vergleichen.
- **Zeittiefe:** Frühere Jahrhunderte sind schwerer, und dort hilft historisches Vortraining am meisten (S. 128). Mittelhochdeutsch liegt vor dem untersuchten Zeitraum (ab 1450 bzw. 1500); das Paper sagt dazu nichts.
- **PROTOKOLL §6 (Ausweichlabels, `MEHRERE`):** Das *mass*/*weight*-Schema hat eine eigene Kategorie W/M für unentscheidbare Belege (S. 134). Das ist ein Beispiel aus der historischen WSD-Praxis für einen Unklar-Status neben den Senses; ob er eher `MEHRERE` oder `KONTEXT_UNZUREICHEND` entspricht, lässt das Paper offen.
- **PROTOKOLL §5 und §7 (doppelte Annotation):** Die einzige echte Anwendungsaufgabe stützt sich auf eine einzelne Fachperson ohne Übereinstimmungsmessung (S. 128). Das ist ein Beispiel für die Lücke, die der doppelt annotierte Goldstandard schließen soll.
- **Weiteres Sprachmodell für historisches Deutsch:** keines; für Mittelhochdeutsch bleibt GHisBERT (Beck & Köllner 2023, die dieses Paper auf S. 35 und 43 zitieren).

## Grenzen und Einwände

- Kein Mittelhochdeutsch, kein Deutsch; Inventare sind semasiologische Wörterbücher (OED, WNT) mit Definitionen, kein onomasiologisches Begriffssystem.
- Die Testdaten sind Wörterbuchbelege, die Gold-Senses also lexikografische Zuordnungen der Wörterbuchredaktion; eine eigene Annotation oder Übereinstimmung gibt es nur für die Fallstudie, und dort mit einer Person.
- Die meisten Ergebnisse stehen nur in Abbildungen; genaue Werte der Baselines sind nicht angegeben (siehe oben, [am PDF zu prüfen]).
- „LLM“ bezeichnet hier BERT-artige Encoder (S. 123 bis 124); Aussagen lassen sich nicht ohne Weiteres auf generative LLMs übertragen.
- Keine Signifikanztests für die Hauptvergleiche; nur die Fallstudie berichtet Standardabweichungen.
- Leichter Widerspruch im Zeitraum: Abstract nennt 1450 bis 1950 (S. 123), GysBERT ist auf 1500 bis 1950 trainiert (S. 126), Abb. 5a hat einen Datenpunkt bei 1400 (S. 130).
- Abb. 5 (S. 130) wird im Text nur für den Vergleich historisch gegen gegenwartssprachlich ausgewertet. Am Seitenbild abgelesen liegt die MFS-Linie beim WNT für Micro-F1 in allen Zeitabschnitten über allen feinjustierten Modellen, beim OED im frühesten Abschnitt ebenfalls [am PDF zu prüfen]. Das Paper kommentiert das nicht.

## Weiterführend

- Manjavacas & Fonteyn 2021, MacBERTh, NLP4DH @ ICON 2021, S. 23 bis 36 (S. 132): Herkunft des OED-Datensatzes.
- Manjavacas & Fonteyn 2022a, Adapting vs. Pre-Training, JDMDH (S. 132): liegt vor (`zusammenfassungen/Manjavacas-Fonteyn-2022-Adapting-vs-Pretraining.md`).
- Beelen et al. 2021, When time makes sense: historically-aware targeted sense disambiguation, Findings of ACL (S. 124, 131).
- Chen, Xia & Chen 2021, Non-parametric few-shot learning for WSD, NAACL (S. 124 bis 125, 130, 131).
- Holla et al. 2020, Meta-learning for few-shot WSD, Findings of EMNLP (S. 124, 131).
- Fonteyn 2020, BERT-Einbettungen für funktional-semantischen Wandel, CHR (S. 123, 131).
- Piotrowski 2012, *Natural Language Processing for Historical Texts* (S. 124, 132).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF und hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
