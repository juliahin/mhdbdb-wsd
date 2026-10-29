# Pangakis & Wolken 2025: Keeping Humans in the Loop

**Datei:** `pdf/Pangakis-Wolken-2025-Humans-in-the-Loop.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, PDF vollständig gelesen (22 Seiten, Textebene; Tab. 1 am Seitenbild geprüft); DOI über Crossref und Verlagsseite bestätigt.

**Seitenzählung:** Das PDF trägt die Bandseiten 1471 bis 1492 unten auf der Seite, aber keine Seitenlabels. Gedruckte Seite = PDF-Seite + 1470. Zitiert wird die gedruckte Seite, die PDF-Seite steht in Klammern.

**Verhältnis zum Preprint:** Dies ist die begutachtete Fassung von Pangakis, Wolken & Fasching 2023 (arXiv). Was sich zwischen beiden Fassungen ändert, steht in [Pangakis-etal-2023-Automated-Annotation-Validation.md](Pangakis-etal-2023-Automated-Annotation-Validation.md), Abschnitt „Begutachtete Fassung“, und wird hier nicht wiederholt. Die Seitenangaben dort („ICWSM S. …“) stimmen mit diesem PDF überein. Was dort fehlt oder zu präzisieren ist, steht unten im Abschnitt „Ergänzungen zur Zusammenfassung von 2023“.

## Bibliografie

- **Vollständig:** Pangakis, Nick & Sam Wolken, 2025. Keeping Humans in the Loop: Human-Centered Automated Annotation with Generative AI. *Proceedings of the International AAAI Conference on Web and Social Media* 19(1), S. 1471 bis 1492. Kopfzeile S. 1471: „Proceedings of the Nineteenth International AAAI Conference on Web and Social Media (ICWSM 2025)“.
- **DOI/URL:** https://doi.org/10.1609/icwsm.v19i1.35883 (am 2026-10-28 aufgelöst auf https://ojs.aaai.org/index.php/ICWSM/article/view/35883; Verlagsseite: 19(1), S. 1471 bis 1492, veröffentlicht 2025-06-07). Crossref bestätigt Autoren (Nick, Sam), Titel, Band 19, Seiten und Datum; ein Heft nennt Crossref nicht. ✔
- **Lizenz:** keine offene Lizenz. PDF S. 1471: „Copyright © 2025, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved.“ Die Verlagsseite nennt ebenfalls nur das AAAI-Copyright.
- **Art:** begutachteter Konferenzbeitrag (Full Paper mit Anhängen A bis F und Paper Checklist).
- **Sprache:** Englisch
- **Code:** https://github.com/npangakis/gpt_annotate (S. 1474 (PDF 4), Fn. 9); nicht abgerufen.

## Worum es geht

Die Arbeit prüft, ob GPT-4 menschliche Textannotation in der Computational Social Science annähern kann, und plädiert für einen menschzentrierten Ablauf, in dem jede LLM-Annotation an menschlichen Labels validiert wird (S. 1471 bis 1472 (PDF 1 bis 2)). Dazu werden 27 binäre Annotationsaufgaben aus 11 passwortgeschützten Datensätzen jüngerer Studien in einem Vier-Schritte-Ablauf nachgestellt: Codebuch als Prompt, Test auf 250 menschlich gelabelten Items, Prompt-Überarbeitung auf denselben 250 Items, Endbewertung auf 1.000 zurückgehaltenen Items (S. 1471, Abb. 1; S. 1473 bis 1474 (PDF 1, 3 bis 4)). Ergebnis: Median-F1 0,707 und Median-Accuracy 0,85, aber 9 von 27 Aufgaben mit Precision oder Recall unter 0,5 und große Streuung sogar innerhalb eines Datensatzes (S. 1474 bis 1475 (PDF 4 bis 5)). Prompt-Überarbeitung und Temperatur helfen kaum; ein „Konsistenzwert“ aus wiederholten Läufen markiert unsichere Items; ein mit 1.000 Labels feinjustiertes BERT schlägt GPT-4 in 10 von 14 Aufgaben (S. 1475 bis 1477 (PDF 5 bis 7)).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Frühere Studien testen wenige Aufgaben auf öffentlichen Benchmarks und sind vermutlich von Kontamination betroffen; gute Werte können Memorierung sein. | S. 1471 bis 1472 (PDF 1 bis 2), Introduction | Argument, gestützt auf Wang et al. 2021, Ziems et al. 2023 (referiert) |
| Fehler automatischer Annotation sind vermutlich über Items korreliert und können systematische Verzerrungen erzeugen; Inkonsistenz von ChatGPT macht seine Labels unzuverlässig. | S. 1472 (PDF 2) | referiert (Ashwin et al. 2023; Ollion et al. 2023; Reiss 2023) |
| Frage ist nicht, ob LLMs Menschen „übertreffen“, sondern wie gut sie menschliches Urteil annähern; die menschlichen Labels der Originalstudien gelten als Ground Truth. | S. 1472 (PDF 2) | eigene Festlegung |
| Begründung für diese Ground Truth: Die Annotationsverfahren haben das Peer Review der Originalstudien durchlaufen und nutzten mehrere Annotator:innen oder eine Expert:in. | S. 1472 (PDF 2), Fn. 2; Anhang B, S. 1486 (PDF 16) | eigene Festlegung |
| Jede Kategorie wird als eigene binäre Aufgabe behandelt, Mehrklassenaufgaben werden zerlegt. | S. 1473 (PDF 3) | eigene Methode, mit Literaturverweis |
| Mensch und LLM sollen dasselbe Codebuch nutzen; verschiedene Codebücher erzeugen eine „conceptual gap“ und gefährden die Inhaltsvalidität. | S. 1473 (PDF 3), Fn. 7 | eigene Empfehlung, gestützt auf Jacobs & Wallach 2021 |
| Ob der Originalwortlaut der Anweisungen verfügbar war oder paraphrasiert werden musste, hing nicht mit der LLM-Leistung zusammen. | S. 1473 (PDF 3), Fn. 6 | eigenes Ergebnis, ohne Zahlen |
| Prompt-Überarbeitung auf denselben 250 Items birgt Überanpassung; bei grundlegenden Änderungen sollten auch die Menschen neu annotieren. | S. 1474 (PDF 4), Fn. 8 | eigene Empfehlung |
| Über 27 Aufgaben: Median-F1 0,707, Median-Accuracy 0,85 auf je 1.000 zurückgehaltenen Items. | S. 1474 (PDF 4), Tab. 1 | eigenes Ergebnis |
| 8 von 27 Aufgaben mit Precision und Recall über 0,7; 9 von 27 mit Precision oder Recall unter 0,5, 3 mit beidem; niedrigster F1 0,06. | S. 1474 bis 1475 (PDF 4 bis 5), Abb. 2 | eigenes Ergebnis |
| Die schwachen Ergebnisse hängen nicht an einem Datensatz oder einer Art der Label-Quelle; innerhalb eines Datensatzes (Card et al. 2022) reicht F1 von 0,259 bis 0,811. | S. 1475 (PDF 5) | eigenes Ergebnis |
| Gut bei zusammenfassungsähnlichen Aufgaben, schwach bei Aufgaben, die nuanciertes kulturelles Wissen oder Schlüsse aus dem Gesprächskontext verlangen; Ursache nicht sicher. | S. 1475 (PDF 5); S. 1477 (PDF 7) | eigene Deutung |
| Recall übertrifft Precision in 20 von 27 Aufgaben (Median 0,83 gegen 0,65); LLM-Labels eignen sich daher als erste Stufe mit menschlicher Prüfung der positiven Fälle. | S. 1472 (PDF 2); S. 1475 (PDF 5) | eigenes Ergebnis und Vorschlag |
| Prompt-Überarbeitung bringt im Median Accuracy +0,024, Precision +0,043, F1 +0,018, Recall-Median 0, Recall im Mittel −0,028; gemessen auf den Trainingsitems nach einer Überarbeitungsrunde. | S. 1475 (PDF 5); Abb. 3, S. 1476 (PDF 6) | eigenes Ergebnis |
| „Intercoder agreement“ eines LLM mit sich selbst trennt nicht zwischen schlechter Leistung, echter Mehrdeutigkeit und Zufall durch die Temperatur und wird nicht als Gütemaß verwendet, nur als Konfidenz. | S. 1474 (PDF 4), Fn. 12 | eigene Festlegung |
| Konsistenzwert: Anteil der Läufe, die mit dem Modalwert übereinstimmen; jedes Item mindestens fünfmal bei Temperatur 0,7. Items mit Konsistenz 1,0 haben 19,4 Punkte höhere Accuracy, 16,4 höhere TPR, 21,4 höhere TNR; 85,1 % der Items haben Konsistenz 1,0 und dort 87,5 % Accuracy. | S. 1475 (PDF 5); Abb. 4, S. 1476 (PDF 6) | eigenes Ergebnis |
| Temperatur: kein klarer Zusammenhang mit der Leistung (7 der 27 Aufgaben). | S. 1475 bis 1476 (PDF 5 bis 6); Abb. 5, S. 1477 (PDF 7) | eigenes Ergebnis |
| Zeitliche Drift: 14 Aufgaben im April und November 2023 wiederholt, Accuracy +0,007, F1 +0,022 (Abb. A1: Recall im Median −0,041); künftige Änderungen nicht auszuschließen. | S. 1476 (PDF 6); Abb. A1, S. 1488 (PDF 18) | eigenes Ergebnis |
| BERT mit 250 Trainingslabels unterliegt GPT-4 in 18 von 27 Aufgaben; mit 1.000 Labels schlägt BERT GPT-4 in 10 von 14 Aufgaben (nur 14 Aufgaben hatten genug Labels). | S. 1476 bis 1477 (PDF 6 bis 7), Fn. 15; Abb. A4, S. 1490 (PDF 20) | eigenes Ergebnis |
| Mistral-7B liegt im Mittel 0,16 F1 unter GPT-4. | Anhang D, S. 1486 (PDF 16) | eigenes Ergebnis |
| Textlänge und Lesbarkeit (Flesch-Kincaid) hängen nicht mit der LLM-Leistung zusammen. | Anhang E, S. 1486 (PDF 16); Abb. A3, S. 1489 (PDF 19) | eigenes Ergebnis |
| Wo die menschliche Intercoder-Reliabilität niedrig ist, ist auch GPT-4 schwach; hohe Reliabilität sagt gute LLM-Leistung nur schwach voraus. | Anhang E, S. 1486 bis 1487 (PDF 16 bis 17) | eigenes Ergebnis |
| Künftige Arbeit: wie man validiert, wenn menschliche Validierung schwierig ist; zuerst menschliche Labels über Intercoder-Maße validieren. Wenn Menschen keine Validierungsdaten erzeugen können, ist fraglich, ob ein Modell die Aufgabe kann. | S. 1477 (PDF 7), Discussion | eigene Folgerung, gestützt auf Artstein & Poesio 2008 |
| Limitation: Korrelierte Fehler der menschlichen Annotator:innen würden die gemessene LLM-Leistung nach unten verzerren; deshalb auch der Vergleich mit BERT, das denselben Gold-Fehlern unterliegt. | S. 1478 (PDF 8), Limitations | eigene Einschränkung |

## Daten, Methode, Zahlen

- **Aufgaben:** 27 binäre Aufgaben aus 11 Artikeln der letzten drei Jahre in Zeitschriften wie *Science Advances*, *PNAS*, *APSR*, *AJPS*, *JPSP* (S. 1473 (PDF 3); Tab. A1, S. 1484 (PDF 14); Tab. A2, S. 1485 (PDF 15)). Nachgezählt an Tab. A2: 3 + 4 + 2 + 2 + 4 + 3 + 1 + 2 + 1 + 3 + 2 = 27.
- **Klassenverteilung:** Anteil der positiven Klasse mindestens 0,04 %, Median 24,5 %, höchstens 70,7 % (S. 1473 (PDF 3)).
- **Herkunft der menschlichen Labels:** 22,2 % der Aufgaben Crowd, 37 % Expert:innen, 40,8 % Hilfskräfte (S. 1473 (PDF 3)); pro Studie in Tab. A2 (S. 1485 (PDF 15)). Die Qualität der Originalannotation wird nicht selbst geprüft (Anhang B, S. 1486 (PDF 16)).
- **Kontamination:** nur Datensätze aus passwortgeschützten Archiven oder direkt von den Autor:innen (S. 1473 (PDF 3)). Der Rohtext könne im Training liegen, die Labels nicht, weil sie nicht öffentlich sind (Anhang B, S. 1486 (PDF 16)).
- **Ablauf:** Prompt aus den Originalanweisungen, sonst Zitat oder Paraphrase aus Artikel und Supplement (S. 1473 (PDF 3)); 250 zufällige Items für Validierung und Prompt-Überarbeitung, Fehlerbeispiele werden in den Prompt aufgenommen (S. 1474 (PDF 4)); 1.000 zurückgehaltene Items für die Endbewertung (S. 1474 (PDF 4)).
- **Umfang und Kosten:** gut 75.000 Items mit GPT-4 über die OpenAI-API, unter 500 USD, etwa 1 Stunde pro 1.000 Items (S. 1474 (PDF 4)).
- **Maße:** Accuracy, Precision, Recall, F1 gegen die menschlichen Labels (S. 1474 (PDF 4)). Tab. 1 (am Seitenbild geprüft, PDF 4): F1 Min. 0,06 / Mittel 0,66 / Median 0,71 / Max. 0,97; Accuracy 0,67 / 0,86 / 0,85 / 0,98; Precision 0,03 / 0,62 / 0,65 / 0,96; Recall 0,25 / 0,75 / 0,83 / 0,98.
- **Konsistenzwert:** Formel (1/l) Σ [A_i = A_mode], mindestens fünf Läufe bei Temperatur 0,7 (S. 1475 (PDF 5)). Log-Wahrscheinlichkeiten der Tokens wären eine Alternative (Fn. 14).
- **BERT-Baseline:** Rastersuche über 18 Kombinationen (Lernrate 1e-5, 2e-5, 5e-5; Batchgröße 8, 16; Epochen 2, 4, 6) auf je 250 Items, über 500 trainierte Klassifikatoren, Bewertung auf denselben 1.000 Items; 215 T4-Recheneinheiten, etwa 421,4 GPU-Stunden (S. 1474 (PDF 4); Anhang C, S. 1486 (PDF 16); Tab. A3 bis A4, S. 1491 bis 1492 (PDF 21 bis 22)).
- **Reliabilität der Originalstudien:** Für 21 der 27 Aufgaben berichtet, 16-mal Krippendorffs α, 5-mal Cohens κ; bei Mehrklassenaufgaben ein über alle Labels gepoolter Wert (Anhang E, S. 1486 (PDF 16)).
- **Unsicherheit:** Die Checklist beantwortet die Frage nach Fehlerbalken mit „NA“ (S. 1481 (PDF 11)); Intervalle oder Tests werden für keine Zahl berichtet.

## Ergänzungen zur Zusammenfassung von 2023

Die Zusammenfassung des Preprints beschreibt die begutachtete Fassung korrekt; am PDF nachgeprüft wurden alle dort genannten ICWSM-Seiten und Zahlen. Es fehlt oder ist zu präzisieren:

- **Prompt-Überarbeitung ist in-sample gemessen.** Abb. 3 zeigt die Veränderung „on training data“, also auf denselben 250 Items, an denen überarbeitet wurde (S. 1475 (PDF 5); Abb. 3, S. 1476 (PDF 6)); die Arbeit selbst warnt in Fn. 8 (S. 1474) vor Überanpassung an diese Teilmenge. Die kleinen Gewinne sind damit eher eine Obergrenze. Die Zusammenfassung von 2023 nennt die Werte ohne diesen Hinweis.
- **Zählweise in Anhang E uneinheitlich.** Der Text sagt „21 tasks … reported metrics“, dann „16 studies utilized Krippendorff's alpha, while five studies calculated Cohen's kappa“ (S. 1486 (PDF 16)); es gibt aber nur 11 Studien. Gemeint sind wohl Aufgaben. Bei zerlegten Mehrklassenaufgaben ist der Wert gepoolt, also nicht aufgabenspezifisch. Die Aussage „schwache menschliche Reliabilität, schwaches LLM“ steht damit auf gröberen Daten, als die Formulierung in der Zusammenfassung von 2023 vermuten lässt.
- **Fn. 15 (S. 1476):** BERT mit 1.000 Items nur für 14 Aufgaben, „because the remaining nine studies had an insufficient number“; 27 − 14 = 13 Aufgaben. Wieder Studien und Aufgaben vermischt.
- **Neu gegenüber der Zusammenfassung von 2023, für das Protokoll brauchbar:** Konsistenz 1,0 bei 85,1 % der Items mit 87,5 % Accuracy (Abb. 4); Textlänge und Lesbarkeit ohne Zusammenhang (Anhang E); Wortlaut der Originalanweisung ohne Einfluss (Fn. 6); Drift-Zahlen (S. 1476, Abb. A1); fehlende Fehlerbalken (Checklist, S. 1481).
- **Uneinheitliche Jahresangaben** zwischen Tab. A1 und Tab. A2 (z. B. Saha et al. 2022 gegen 2020, Schub 2022 gegen 2020, Hopkins et al. 2024 gegen 2023; S. 1484 bis 1485 (PDF 14 bis 15)). Für ein Zitat der Originalstudien unerheblich, aber vor einer Übernahme prüfen.

## Wörtliche Stellen

> „Grounding automated annotation in validation labels generated by humans is essential for responsible evaluation.“ (S. 1471 (PDF 1), Abstract)

> „Rather than testing whether LLMs “outperform” human annotators, we explore how well they can approximate human judgment.“ (S. 1472 (PDF 2))

> „If humans and LLMs label the data using different codebooks, there could be a conceptual gap between the two annotation instructions“ (S. 1473 (PDF 3), Fn. 7)

> „this measure cannot distinguish between inconsistency due to poor performance, substantive ambiguity, or arbitrary randomness“ (S. 1474 (PDF 4), Fn. 12)

> „underscores the necessity of first validating human labels through inter-coder agreement metrics“ (S. 1477 (PDF 7))

> „if humans cannot effectively generate validation data then there may be concerns whether a statistical model can reasonably complete the same task either.“ (S. 1477 (PDF 7))

## Bezug zur Dissertation

Die Punkte aus der Zusammenfassung von 2023 (Protokoll 4.7, 4.10, 7, 9.2, 10, Silberqualität) gelten unverändert und sind dort nachzulesen. Zusätzlich:

- **Protokoll 4.10 (Freeze 2: Temperatur, Läufe pro Item, Modellversion):** Mindestens fünf Läufe bei Temperatur 0,7 und Konsistenz als Konfidenz, nicht als Gütemaß (S. 1474 Fn. 12; S. 1475), sind eine konkrete, zitierfähige Vorlage für die offene Festlegung „Anzahl der Läufe pro Item“. Dass die Temperatur kaum wirkt (S. 1475 bis 1477), spricht dafür, sie einmal festzulegen statt zu optimieren. Der Drift-Befund (S. 1476) ist schwach (zwei Zeitpunkte, ein Modell) und stützt eher die Pflicht, Modell und Version einzufrieren, als die Annahme, Versionen seien austauschbar.
- **Protokoll 7 (Pilot, Prompt-Revision, frische Items):** Die eigene Messung der Prompt-Revision ist in-sample (Abb. 3). Das Protokoll ist hier strenger: Pilotrunden mit frischen Items, Pilotlemmata disjunkt zur Hauptstichprobe. Für die Dissertation heißt das: eine Wirkung von Prompt-Änderungen nur auf Items berichten, die beim Überarbeiten nicht gesehen wurden.
- **Protokoll 9.2 (Baseline):** Die Arbeit vergleicht das LLM nicht mit einer Häufigkeitsbaseline, sondern mit einem überwachten Modell, das auf denselben menschlichen Labels trainiert ist (S. 1474, S. 1476 bis 1477). Die MFS aus Silber ist das Gegenstück dafür, was sich aus vorhandenen Labels ohne Training gewinnen lässt. Der Befund, dass schon 1.000 Labels pro Aufgabe ein feinjustiertes BERT vor GPT-4 bringen, lässt sich auf WSD nicht übertragen: Dort ist jedes Lemma eine eigene Aufgabe mit eigenem Inventar (Navigli 2009, S. 10:4), die Trainingsmenge zählt also pro Lemma, nicht pro Aufgabe im Sinne der Arbeit.
- **Protokoll 4.6 und 9.1, Punkt 6 (Schwierigkeitsfaktoren, Aufschlüsselung):** Textmerkmale wie Länge und Lesbarkeit erklärten die LLM-Leistung nicht, Aufgabenmerkmale (kulturelles Wissen, Gesprächskontext) schon (S. 1475, Anhang E). Für Mittelhochdeutsch ist kulturelles und historisches Wissen der Normalfall; das spricht dafür, Obergattung und Domäne als Faktoren im gemischten Modell zu behalten und die LLM-Genauigkeit zusätzlich nach menschlicher Übereinstimmung pro Item aufzuschlüsseln (siehe Zusammenfassung von 2023, Bezug 9.2).
- **Protokoll 9.1, Punkt 3 (Zufallsmodell, Poolen):** Die Arbeit poolt bei Mehrklassenaufgaben die Reliabilität über alle Labels (Anhang E). Das ist ein Beispiel dafür, wie ein gepoolter Wert die Aussage pro Aufgabe verwischt, und stützt die Entscheidung des Protokolls, die erwartete Übereinstimmung pro Lemma zu rechnen und die gepoolte Variante nur daneben zu berichten.
- **Protokoll 4.9 und 9.1, Punkt 5 (Unsicherheit):** Die Arbeit berichtet keine Intervalle (Checklist, S. 1481). Ein Gegenbeispiel, auf das sich das Protokoll mit Bootstrap-Intervallen nach Text abgrenzen kann.

## Grenzen und Einwände

- Englisch, Sozialwissenschaften, nur binäre Aufgaben mit festem Kategoriensystem (S. 1473). WSD mit wechselndem Inventar pro Lemma, historische Sprache und ein onomasiologisches Inventar kommen nicht vor.
- Ein einziges Hauptmodell (GPT-4), dazu Mistral-7B im Anhang (S. 1486). Modellversion und Datum des Hauptlaufs werden nicht genau genannt, nur April und November 2023 für die Drift-Prüfung (S. 1476).
- Das Gold sind fremde Labels, deren Qualität über das Peer Review der Originalstudien angenommen wird (Fn. 2; Anhang B); 63 % der Aufgaben stammen von Crowd oder Hilfskräften (S. 1473). Die eigene Forderung, menschliche Labels zuerst zu validieren (S. 1477), setzt die Studie damit nur indirekt um.
- Keine Fehlerbalken, keine Tests (Checklist, S. 1481); Unterschiede wie „+0,024 Accuracy“ sind ohne Unsicherheitsangabe.
- Prompt-Revision und Temperatur wurden auf wenigen Aufgaben bzw. in-sample geprüft (S. 1475 bis 1477); die Aussage „hilft kaum“ ist entsprechend vorläufig.
- Kontaminationsargument: Für die MHDBDB sind Texte und teils auch Silber-Labels öffentlich; die Lösung der Arbeit (nur nicht öffentliche Labels) deckt im Protokoll nur das neue Gold (Protokoll 10), nicht das Silber, aus dem die MFS gelernt wird.

## Weiterführend

- Pangakis, Wolken & Fasching 2023 (Preprint); eigene Zusammenfassung, mit dem Abgleich beider Fassungen.
- Jacobs & Wallach 2021, Measurement and Fairness (zitiert S. 1473 Fn. 7, S. 1477): Messmodell-Sprache für Validität von Annotation.
- Davani, Díaz & Prabhakaran 2022, Dealing with disagreements (zitiert S. 1477): Unsicherheit in menschlichen Labels modellieren, passt zu Protokoll 7, Punkt 7.
- Mikhaylov, Laver & Benoit 2012, Coder reliability and misclassification (zitiert S. 1477).
- Li & Flanigan 2023, Task Contamination (zitiert S. 1473).
- Felkner, Thompson & May 2024, „GPT is Not an Annotator“ (zitiert S. 1477).
- Li et al. 2023, CoAnnotating (zitiert S. 1475); eigene Zusammenfassung vorhanden.
