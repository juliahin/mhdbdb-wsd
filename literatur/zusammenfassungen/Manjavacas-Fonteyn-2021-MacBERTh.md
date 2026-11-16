# Manjavacas Arevalo & Fonteyn 2021: MacBERTh, ein historisch vortrainiertes Sprachmodell für Englisch (1450 bis 1950)

**Datei:** `pdf/Manjavacas-Fonteyn-2021-MacBERTh.pdf` (nur lokal; 14 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Tab. 1 und 2 sowie Abb. 4 am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-13). Keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 22 + n (PDF 1 = S. 23, PDF 14 = S. 36). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Manjavacas Arevalo, Enrique & Lauren Fonteyn (2021). MacBERTh: Development and Evaluation of a Historically Pre-trained Language Model for English (1450-1950). In: Mika Hämäläinen, Khalid Alnajjar, Niko Partanen & Jack Rueter (Hg.), *Proceedings of the Workshop on Natural Language Processing for Digital Humanities (NLP4DH)*, co-located with ICON-2021, Silchar (Indien), 16. bis 19. Dezember 2021. NLP Association of India (NLPAI), S. 23 bis 36.
- **DOI/URL:** https://aclanthology.org/2021.nlp4dh-1.4/ (BibTeX der Anthology abgerufen 2026-11-13: Hg., Verlag NLPAI, Ort „NIT Silchar, India“, Dezember 2021, S. 23 bis 36 ✔). Die Kopfzeile S. 23 druckt die DOI 10.26615/978-952-94-5833-2_004; sie **löst nicht auf** (doi.org: 404, Handle-API: „handle not found“, Crossref: nicht gefunden; geprüft 2026-11-13). Nicht als DOI zitieren.
- **Name:** Im PDF „Enrique Manjavacas“ (S. 23), in der Anthology „Manjavacas Arevalo“; wie bei Manjavacas & Fonteyn 2022b die Form der Anthology verwenden.
- **Lizenz:** Kopfzeile S. 23: „©2021 NLP Association of India (NLPAI)“. Die ACL Anthology stellt laut Fußzeile ihrer Seiten Material ab 2016 unter CC BY 4.0; eine Lizenz des Verlags selbst steht nicht im PDF.
- **Art:** Workshop-Beitrag
- **Sprache:** Englisch
- **Code und Modell:** Evaluationscode github.com/emanjavacas/macberth-eval; Modell `emanjavacas/MacBERTh` auf Hugging Face (S. 23, Anm. 1; nicht aufgerufen).

## Worum es geht

Das Paper stellt MacBERTh vor, ein BERT-Modell (Architektur „BERT-base uncased“), das von Grund auf auf rund 3,9 Mrd. Wörtern historischen Englischs (1450 bis 1950) vortrainiert wurde, und vergleicht es mit gegenwartssprachlichen Modellen (BERT, MultiBERT) und einem auf historisches Englisch nachtrainierten BERT (TuringBERT, 1760 bis 1900) (S. 24 bis 25). Getestet wird auf eigens gebauten Aufgaben: Wortartentagging (PPCEME), zwei WSD-Varianten auf OED-Belegen (Word-in-Context und parameterfreie Sense-Klassifikation), Lückentext und Datierung von Sätzen (S. 25 bis 30). MacBERTh ist in fast allen Bedingungen vorn, besonders für Belege vor etwa 1700; die Autoren folgern, dass Vortraining von Grund auf auf historischen Daten robuster sei als das Anpassen eines Gegenwartsmodells (S. 30 bis 31).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Gegenwartssprachlich vortrainierte Modelle helfen bei historischen Daten weniger, wegen Verschiebungen in Grammatik, Semantik und Orthografie; Normalisierung behebe nur die Orthografie und bringe eigene Fehler mit. | S. 23, Abschnitt 1 | Begründung, teils referiert (Han & Eisenstein 2019; Bollmann 2019) |
| Vortrainingskorpus ca. 3,9 Mrd. Wörter, 1450 bis 1950: EEBO, CLMET3.1, EVANS, ECCO, COHA, Hansard; fremdsprachige Passagen per Spracherkennung entfernt. | S. 24, Abschnitt 2.1, Anm. 4 | eigene Datengrundlage |
| Benchmark-Daten aus dem OED: 3.000 Wörter nach geglätteter Frequenz gezogen; Ergebnis 2.700 Lemmata, 35.110 Senses, 246.048 Belegzitate. | S. 25, Abschnitt 2.2.1 | eigene Datengewinnung |
| Wortartentagging (PPCEME, 1450 bis 1700, ca. 1,7 Mio. Wörter, 448 Dokumente): Gegenwartsmodelle sind in allen Bedingungen schlechter; der Vorteil der historischen Modelle ist bei unbekannten Tokens am größten, der von MacBERTh bei wenig Trainingsdaten. | S. 25 bis 26, Abschnitt 3.1, Abb. 2 | eigenes Ergebnis |
| Word-in-Context (zwei OED-Belege, gleicher Sense ja/nein): auf Entwicklungsdaten über 90 %, auf nicht gesehenen Lemmata erreicht kein Modell 70 %. MacBERTh ist bis auf gehaltene Adjektive am besten. | S. 27, Abschnitt 3.2.1, Tab. 1 | eigenes Ergebnis |
| Parameterfreie WSD (Sense-Vektor als Mittelwert der Belege, nächster Nachbar): MacBERTh 42,3 % Genauigkeit gegen 36,0 % (BERT), Mehrheitsbaseline 13,6 %, Zufall 9,2 %. | S. 28, Abschnitt 3.2.2, Tab. 2 | eigenes Ergebnis |
| Funktionswörter werden besser disambiguiert als Inhaltswörter, obwohl die Baseline sie als schwerer ausweist; TuringBERT liegt hier hinter BERT. | S. 28 | eigenes Ergebnis |
| Lückentext (Mean Reciprocal Rank) und Satzdatierung (mittlerer absoluter Fehler): MacBERTh in allen Perioden vorn, im Mittel etwa 50 Jahre daneben; Vorsprung vor 1650 am größten. | S. 28 bis 30, Abschnitte 3.3 bis 3.4 | eigenes Ergebnis |
| Fazit: Historisches Vortraining verbessert diachron relevante Aufgaben, aber nicht für alle Zeitabschnitte gleich; Vortraining von Grund auf sei vermutlich robuster als Anpassen, möglicherweise wegen des gegenwartssprachlichen Tokenizers. | S. 30 bis 31, Abschnitte 4 bis 5 | eigene Deutung |
| Ausblick: Einsatz in realen DH-Szenarien und „prompt engineering“ als vielversprechender Weg. | S. 31 | Ausblick, referiert (Liu et al. 2021) |

## Daten, Methode, Zahlen

- **Modell (S. 24):** Originalimplementierung von BERT, Hyperparameter „BERT-base uncased“, maximale Sequenzlänge 128 Subtokens, 1.000.000 Trainingsschritte.
- **Vergleichsmodelle (S. 25):** BERT (ca. 3,3 Mrd. Tokens, WordPiece 30.000), MultiBERT (100 Sprachen, WordPiece 110.000), TuringBERT (BERT-base nachtrainiert auf 5,1 Mrd. Tokens, 1760 bis 1900).
- **Word-in-Context (S. 27):** Belege mit mindestens 5 Wörtern; Lemmata mit mindestens 100 Belegen, nur Nomen, Adjektive, Verben: 408 Lemmata, davon 10 % (41) als nicht gesehene Testlemmata; Zielwort mit `[TGT]` markiert; Entwicklungsdaten = 25 % der Trainingsdaten.
- **Tab. 1 (S. 27), Genauigkeit in %, am Seitenbild geprüft.** Spalten: gesamt; Paare mit verschiedener Wortart; Paare mit gleicher Wortart, getrennt nach N, Adj, V.

| Modell | Entw. gesamt | Entw. ≠ POS | Entw. N | Entw. Adj | Entw. V | geh. gesamt | geh. ≠ POS | geh. N | geh. Adj | geh. V |
|---|---|---|---|---|---|---|---|---|---|---|
| BERT | 89,9 | 92,3 | 90,1 | 92,6 | 86,7 | 59,5 | 56,8 | 60,5 | 65,8 | 58,4 |
| MultiBERT | 92,0 | 94,8 | 91,6 | 95,6 | 88,7 | 62,1 | 63,3 | 64,0 | 66,1 | 57,1 |
| TuringBERT | 91,0 | 94,1 | 90,5 | 94,3 | 87,6 | 58,6 | 58,5 | 59,8 | 60,7 | 56,4 |
| MacBERTh | 94,5 | 96,1 | 94,1 | 96,8 | 92,6 | 63,0 | 63,8 | 65,3 | 61,8 | 59,3 |

- **Parameterfreie WSD (S. 28):** Lemmata mit mindestens 50 Belegen; einsenige Lemmata und Senses mit weniger als 2 Belegen entfernt; geschichtete Teilung 50/50; Vergleich nur mit den Senses desselben Lemmas („gold lemmata“). Funktionswörter = OED-Klassen „pron“, „prep“, „conj“, „int“ (Anm. 13).
- **Tab. 2 (S. 28), Genauigkeit in %, am Seitenbild geprüft:**

| Modell | gesamt | Inhaltswörter | Funktionswörter |
|---|---|---|---|
| BERT | 36,0 | 36,1 | 34,8 |
| MacBERTh | 42,3 | 42,0 | 50,4 |
| MultiBERT | 32,3 | 32,1 | 38,6 |
| TuringBERT | 34,8 | 34,6 | 43,2 |
| Majority | 13,6 | 13,7 | 9,1 |
| Random | 9,2 | 9,3 | 6,1 |

- **Satzdatierung (S. 29 bis 30):** Hintergrundkorpus 1.000 datierte Belege (20 pro Jahrzehnt, 1450 bis 1900); 100.000 Trainings-, je 5.000 Entwicklungs- und Testpaare; Vorhersage über den Knickpunkt der kumulativen Verteilung (Kneedle).
- **Annotation:** keine eigene. Gold-Senses sind die Zuordnungen der OED-Redaktion; keine Übereinstimmungsmessung.

## Wörtliche Stellen

> „[…] pre-training on historical language from scratch outperforms models pre-trained on present-day language and later adapted to historical language.“ (S. 23, Abstract)

> „However, on held-out lemmata, no model surpasses 70% accuracy […]“ (S. 27)

> „In any case, pre-training from scratch on historical data may be a more robust strategy than adapting a pre-trained model.“ (S. 31)

## Bezug zur Dissertation

- **PROTOKOLL §1 (späterer Encoder-Vergleich, nicht Teil des Protokolls):** MacBERTh ist der Bezugspunkt für die Herkunft historischer Encoder: von Grund auf vortrainiert, besser als nachtrainierte Gegenwartsmodelle (S. 30 bis 31). Für einen späteren Vergleich LLM gegen Encoder ist das Argument, ein historisch vortrainiertes Modell zu nehmen (für das Mittelhochdeutsche GHisBERT, Beck & Köllner 2023), nicht ein Gegenwartsmodell. Das Paper deckt Englisch ab 1450, also nicht die Zeit der MHDBDB-Texte.
- **PROTOKOLL §9.2 (MFS aus Korpus-Silber, nicht aus Wörterbuch):** In der parameterfreien WSD auf OED-Belegen liegt die Mehrheitsbaseline nur bei 13,6 % (Tab. 2, S. 28). Wörterbuchbelege sind nach Senses ausgewählt, nicht nach Gebrauchshäufigkeit; eine MFS aus ihnen sagt wenig über einen Korpus. Das stützt, die MFS aus Korpus-Silber zu lernen (§9.2) und Werte aus Wörterbuch-Benchmarks nicht mit der MHDBDB-Baseline zu vergleichen (vgl. die Zusammenfassung zu Manjavacas & Fonteyn 2022b, Abschnitt Bezug).
- **PROTOKOLL §9.2 (Aufschlüsselung nach Wortart, Inhalts- gegen Funktionswörter) und §9.1 Punkt 6:** Funktionswörter schneiden mit MacBERTh besser ab als Inhaltswörter (50,4 gegen 42,0 %), Adjektive im Word-in-Context besser als Nomen und Verben (S. 27 bis 28). Das spricht dafür, die geplante Aufschlüsselung nach Wortart beizubehalten; die Richtung ist auf das Begriffssystem nicht übertragbar.
- **Generalisierung auf nicht gesehene Lemmata (S. 27):** Über 90 % auf Entwicklungsdaten, unter 70 % auf gehaltenen Lemmata. Für die Dissertation ist das ein Argument, die LLM-Konfiguration nicht an Lemmata der Stichprobe zu justieren (Pilot-Pool außerhalb der Hauptstichprobe, PROTOKOLL §4.2 und §7 Schritt 2).
- **`knowledge/data.md`, Abschnitt 1 (Sense als Begriffsgruppe):** Die OED-Senses sind hierarchische Wörterbuch-Senses mit Definition und Belegen (S. 25, Tab. 3 S. 35); das Verfahren nutzt nur die Belege. Für MHDBDB-Senses ohne Silberbeleg (B9: 42 % der Senses polysemer Lemmata mit Silber) wäre ein solches belegbasiertes Verfahren nicht anwendbar.
- **`goldstandard/LITERATUR-IAA.md`, „Historische Sprachen“:** ein weiteres Beispiel für Gold ohne eigene Annotation und ohne Übereinstimmung; die Gold-Senses stammen aus der OED-Redaktion.

## Grenzen und Einwände

- Kein Deutsch, kein Mittelalter vor 1450; die frühesten OED-Belege in Abb. 4 liegen bei 1400 (S. 28), das Vortraining beginnt 1450.
- Alle WSD-Aufgaben nutzen Wörterbuchbelege, keine laufenden Texte und keine eigene Annotation. Die Werte sind daher nicht mit einer WSD auf Korpusbelegen vergleichbar.
- Keine Signifikanztests, keine Streuung über mehrere Läufe.
- Unstimmigkeiten im Text: Zeitraum „1450-1900“ in den Beiträgen (S. 24) gegen „1450-1950“ im Titel und S. 24 (Abschnitt 2.1); „surpassing 90% accuracy across conditions“ (S. 27) gilt nicht für BERT gesamt (89,9) und die Verbspalten unter 90 (Tab. 1); „Pairs with diverging part-of-speech tags resulted in higher accuracy“ (S. 27) gilt auf den gehaltenen Lemmata nicht für BERT und TuringBERT (Tab. 1). In Abb. 4 (Inhaltswörter) liegt BERT um 1900 am Seitenbild abgelesen über MacBERTh [am PDF zu prüfen]; der Text sagt dazu nur, der Zeiteffekt sei für alle Modelle gleich.
- „Large language model“ meint hier BERT-artige Encoder (S. 23); Aussagen gelten nicht ohne Weiteres für generative LLMs.

## Weiterführend

- Beelen et al. 2021, „When time makes sense“, Findings of ACL-IJCNLP 2021, S. 2751 bis 2761 (S. 23, 32): historisch bewusste Sense-Disambiguierung auf OED-Daten.
- Hosseini et al. 2021a, Neural Language Models for Nineteenth-Century English, JOHD 7:22 (S. 25, 32): Herkunft von TuringBERT.
- Bamman & Burns 2020, Latin BERT (S. 24, 32): Vergleichsfall Latein (auch in Ghinassi et al. 2024 und Ghizzota et al. 2025).
- Han & Eisenstein 2019, Domänenanpassung kontextueller Einbettungen, EMNLP-IJCNLP (S. 23 bis 26, 32).
- Pilehvar & Camacho-Collados 2019, WiC (S. 27, 33).
- Schlechtweg et al. 2020, SemEval-2020 Task 1 (S. 23, 33).
- Manjavacas & Fonteyn 2022a und 2022b (bauen auf diesem Paper auf; liegen vor, `zusammenfassungen/Manjavacas-Fonteyn-2022-*.md`).

## Julias Notizen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF und hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
