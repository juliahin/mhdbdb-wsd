# Sainz et al. 2023: NLP Evaluation in trouble

**Datei:** `pdf/Sainz-etal-2023-NLP-Evaluation-Trouble.pdf` (nur lokal; 12 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen; Abb. 1 bis 3 (S. 10786) am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology 2023.findings-emnlp.722 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 10775 + n (PDF 1 = S. 10776, PDF 12 = S. 10787). Text S. 10776 bis 10780, Literatur bis S. 10785, Anhang A S. 10786 bis 10787. Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Sainz, Oscar; Campos, Jon Ander; García-Ferrero, Iker; Etxaniz, Julen; Lopez de Lacalle, Oier & Agirre, Eneko (2023). NLP Evaluation in trouble: On the Need to Measure LLM Data Contamination for each Benchmark. In: Houda Bouamor, Juan Pino & Kalika Bali (Hg.), *Findings of the Association for Computational Linguistics: EMNLP 2023*. Singapur: Association for Computational Linguistics, S. 10776 bis 10787.
- **DOI/URL:** 10.18653/v1/2023.findings-emnlp.722 (aufgelöst, Crossref, 2026-11-16); https://aclanthology.org/2023.findings-emnlp.722/. Das PDF nennt den zweiten Autor „Jon Ander Campos“, Anthology und Crossref „Jon Campos“.
- **Lizenz:** CC BY 4.0 (ACL Anthology, Werke ab 2016, abgerufen 2026-11-16).
- **Art:** Konferenzbeitrag, ausdrücklich „position paper“ (S. 10776)
- **Sprache:** Englisch

## Worum es geht

Das Positionspapier argumentiert, dass die Evaluation mit annotierten Benchmarks „in trouble“ ist, weil LLMs die Testdaten im Vortraining gesehen haben können, und dass das Ausmaß unbekannt ist (S. 10776). Es unterscheidet drei Arten der Kontamination (Richtlinien, Rohtext, Annotation), beschreibt, an welchen Schritten des Trainings sie entstehen kann, schlägt Messverfahren für offene und geschlossene Modelle vor und ruft zu einem Register von Kontaminationsfällen und zur Prüfung im Begutachtungsverfahren auf (S. 10777 bis 10780). Der Anhang zeigt, dass drei Modelle den Anfang des CoNLL-2003-Trainingssplits wörtlich wiedergeben (S. 10786).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Schlimmster Fall: Ein LLM wird auf dem Test-Split eines Benchmarks trainiert und dann darauf evaluiert. Folge ist eine Überschätzung der Leistung gegenüber nicht kontaminierten Modellen; falsche Schlüsse werden veröffentlicht, richtige verworfen. | S. 10776, Abstract | Position |
| Zwei Folgen: (1) verzerrter Vergleich zwischen LLMs, (2) Arbeiten, die mit kontaminierten LLMs Hypothesen über NLP-Aufgaben prüfen, ziehen falsche Schlüsse; die zweite Folge ist das Hauptanliegen. | S. 10776 | Position |
| Eine mögliche Lösung wäre, nur Datensätze zu nutzen, deren Test-Labels nicht öffentlich sind; das würde die Zahl der Aufgaben mit Benchmark stark verringern. Vorbeugende Strategien bei Jacovi et al. (2023); dieses Papier will ergänzend messen und dokumentieren. | S. 10776 | Position, Verweis |
| Kontamination heißt allgemein jeder Bruch der strengen Datenkontrolle, die das Versuchsprotokoll verlangt. | S. 10777, Abschnitt 3 | Definition |
| **Richtlinienkontamination:** Das Modell hat die Annotationsrichtlinien gesehen; sie sind oft öffentlich, auch wenn der Datensatz es nicht ist. Ein Modell, das die Richtlinien kennt, ist im Vorteil, besonders bei Zero- und Few-shot-Evaluation. | S. 10777 | Definition und Argument |
| **Rohtextkontamination:** Das Modell hat den Ausgangstext vor der Annotation gesehen (Beispiel: Datensätze aus Wikipedia, MultiCoNER 2 mit Wikipedia-Links); es hat dann mehr Information, um einen Teil der Annotation zu erkennen. | S. 10777 bis 10778 | Definition und Beispiel |
| **Annotationskontamination:** Die Labels des Benchmarks waren im Training. Betrifft sie den Evaluationssplit, ist das Experiment „completely invalidated“; betrifft sie Trainings- oder Entwicklungssplit, bleiben Vergleiche mit Modellen gleicher Splits gültig, Aussagen über Zero- oder Few-shot-Leistung aber nicht. | S. 10778 | Definition |
| Kontamination entsteht beim Vortraining, beim überwachten Feintuning (u. a. durch maschinell erzeugte Daten und Crowdworker, die LLMs nutzen) und nach der Bereitstellung: Über API genutzte Modelle wurden mit Nutzereingaben weiter verbessert, „leading to evaluation data exposure“. | S. 10778, Abschnitte 4.1 bis 4.3 | Argument mit Verweisen (Veselovsky et al. 2023) |
| Offene Modelle: Kontamination über Abgleich mit den Vortrainingsdaten messen; vorgeschlagenes Maß ist der Anteil des Benchmarks, der sich in den Vortrainingsdaten findet. | S. 10779, Abschnitt 5.1 | Vorschlag |
| Geschlossene Modelle: Memorierung nutzen; ein Beispiel gilt als extrahierbar, wenn das Modell es nach den k vorangehenden Beispielen des Datensatzes erzeugt; Grad der Kontamination ist der Anteil extrahierbarer Beispiele. Ob fehlende Memorierung Training ausschließt, ist offen. | S. 10779, Abschnitt 5.2 | Vorschlag (nach Carlini et al. 2023) |
| Aufruf: (1) automatische oder halbautomatische Erkennungsmaße, (2) Register von Kontaminationsfällen mit Belegen, (3) Autor:innen sollen ihr Protokoll mit diesen Werkzeugen absichern, (4) Kontamination im Peer Review prüfen und betroffene Arbeiten kennzeichnen. | S. 10779 bis 10780, Abschnitt 6 | Vorschlag |
| WizardCoder, ChatGPT und GitHub Copilot geben die ersten Zeilen des CoNLL-2003-Trainingssplits wieder; „not surprising, as all the models were trained on GitHub, where this dataset has been uploaded several times“. | S. 10786, Anhang A, Abb. 1 bis 3 | eigene Demonstration (qualitativ) |

## Daten, Methode, Zahlen

Keine eigenen Messungen außer der qualitativen Demonstration im Anhang (drei Prompts, drei Ausgaben, S. 10786). Weitere Belege nur referiert: C4 enthielt Test-Splits mehrerer Benchmarks, die von GitHub gecrawlt wurden (Dodge et al. 2021, S. 10777); Teile von BIG-bench gerieten in das Training von GPT-4 (OpenAI 2023, S. 10777); Liste von Kontaminationsberichten (S. 10786 bis 10787). Verweis auf ein laufend gepflegtes „LM Contamination Index“ (S. 10776, Fn. 1).

## Wörtliche Stellen

> „The worst kind of data contamination happens when a Large Language Model (LLM) is trained on the test split of a benchmark, and then evaluated in the same benchmark.“ (S. 10776)

> „Contamination causes an overestimation of the performance of a contaminated model in a target benchmark and associated task with respect to their non-contaminated counterparts.“ (S. 10776)

> „When the evaluation split is involved, the experiment is completely invalidated.“ (S. 10778)

> „A model aware of the guidelines for a specific task or dataset has advantages over a model without such information.“ (S. 10777)

## Bezug zur Dissertation

**1. PROTOKOLL §10 (Labels privat bis zur Publikation) und DMP §5.** Gestützt: Annotationskontamination des Evaluationssplits macht das Experiment ungültig (S. 10778), und die Lösung, Test-Labels nicht zu veröffentlichen, wird ausdrücklich genannt (S. 10776). Der Begründungssatz in §10 („Öffentliche Labels können in die Trainingsdaten künftiger LLMs geraten …“) ist damit gedeckt.

**2. PROTOKOLL §10, Satz „Die mittelhochdeutschen Texte sind ohnehin online; zu schützen sind die Labels.“** Teilweise gedeckt. Nach S. 10777 ist auch **Rohtextkontamination** ein Vorteil für das Modell, und bei Texten mit eingebetteter Annotation (Wikipedia mit Links) verrät der Rohtext einen Teil der Labels. Das öffentliche MHDBDB-Korpus trägt im Rohtext schon Silber-`@ana` (D1) und im Lexikon Typlisten (D0, `knowledge/data.md`, B1). Das ist strukturell der Fall „original form (including the markup annotations)“ (S. 10777). Vorschlag: §10 so fassen, dass nicht nur die neuen Labels, sondern auch die öffentliche Altannotation als möglicher Lösungshinweis genannt und in der Auswertung berücksichtigt wird (vgl. Zusammenfassung Jacovi et al. 2023, Bezug Punkt 2).

**3. Öffentliche Richtlinien (PROTOKOLL §10, Zeile „Protokoll, Richtlinien, Datasheet“: öffentlich).** Sainz et al. nennen **Richtlinienkontamination** als eigenen Typ (S. 10777). Für dieses Design ist der Schaden gering, solange das LLM die Richtlinien ohnehin im Prompt erhält (gleiche Darbietung, A27); dann ist der Vorteil Teil der Bedingung, nicht Kontamination. Wird der Prompt kürzer als die Richtlinien, kann ein späteres Modell mehr wissen als der Prompt sagt. Kein Änderungsbedarf, aber ein Satz in den Einschränkungen.

**4. Pilot-Items und Manifest im öffentlichen Fork.** Annotationskontamination von Entwicklungsdaten macht nur Zero- und Few-shot-Aussagen ungültig, nicht Vergleiche (S. 10778). Die Pilot-Items tragen keine Labels; was öffentlich ist, sind Rohtext und Karten. Wird ein späteres Modell auf dem Fork trainiert, ist das Rohtextkontamination des Pilot-Pools, nicht des Golds. Der Anhang zeigt aber, dass Modelle Daten aus GitHub wörtlich memorieren (S. 10786); der öffentliche Fork liegt auf GitHub. Für die menschlichen Labels nach der Publikation spricht das gegen jede Klartextablage auf GitHub, auch in einem später öffentlich gestellten Repo.

**5. Auswertung (PROTOKOLL §9.2).** Das Papier verlangt, das Protokoll gegen Kontamination abzusichern und sie zu dokumentieren (S. 10779 bis 10780). Konkret anwendbar ist der Extrahierbarkeitstest (S. 10779) nur eingeschränkt, weil die Labels nicht als Folge im Netz stehen. Anwendbar wäre eine Memorierungsprüfung am Silber: das LLM für D1-Tokens nach dem MHDBDB-Sense fragen, ohne Karten. Vorschlag für den Pilot (analog zur Kontrollbedingung ohne Kontext, A28), nicht beschlossen.

**6. Abgleich mit `goldstandard/LITERATUR-IAA.md`** (Zeile „Kontamination: Testdaten nicht im Klartext veröffentlichen; verschlüsseln, Lizenz, Canary“, Sainz et al. 2023 ✔): **Nur der erste Teil ist durch dieses Werk gedeckt.** Sainz et al. begründen, warum öffentliche Test-Labels ein Problem sind (S. 10776, 10778), empfehlen aber weder Verschlüsselung noch Lizenz noch Canary-String (ganze Textebene durchsucht); sie verweisen für Vorbeugung auf Jacovi et al. (S. 10776). Die Literaturangabe dort nennt arXiv:2310.18018 statt Findings of EMNLP 2023, S. 10776 bis 10787.

## Grenzen und Einwände

- Positionspapier; die einzige eigene Evidenz ist eine qualitative Demonstration an einem Datensatz (CoNLL-2003, S. 10786).
- Die vorgeschlagenen Messverfahren sind Skizzen; ob fehlende Memorierung Training ausschließt, bleibt ausdrücklich Spekulation (S. 10779).
- Kein Bezug zu WSD oder historischen Sprachen; die Typen Rohtext und Annotation werden an modernen Webdaten gezeigt. Für ein Korpus, dessen Rohtext eine ältere Annotation enthält, die der neuen ähnelt, ist die Abgrenzung von Rohtext- und Annotationskontamination nicht behandelt.

## Weiterführend

- Jacovi et al. 2023 (S. 10776): vorbeugende Strategien; liegt als PDF vor.
- Dodge et al. 2021, Documenting large webtext corpora (S. 10777, 10779): Testsplits in C4, aus GitHub gecrawlt.
- Carlini et al. 2023, Quantifying memorization across neural language models, ICLR (S. 10779): Grundlage der Extrahierbarkeitsdefinition.
- Magar & Schwartz 2022 (S. 10777, 10779): Kontamination bei geschlossenen Trainingsdaten.
- Piktus et al. 2023, ROOTS search tool; Marone & Van Durme 2023, Data Portraits (S. 10779): Prüfwerkzeuge.
- Veselovsky et al. 2023 (S. 10778): Crowdworker nutzen LLMs.

## Julias Notizen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
