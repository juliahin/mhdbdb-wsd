# Sumanathilaka, Micallef & Hough 2024: LLMs und lexikalische Ambiguität (WSD auf FEWS)

**Datei:** `pdf/Sumanathilaka-etal-2024-LLMs-Ambiguity-WSD.pdf` (nur lokal; 12 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Tab. 1 bis 3 (S. 100), Abb. 1 (S. 102), Tab. 5 und 6 (S. 103) und Tab. 7 (S. 104) am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-13), also die Tagungsfassung. Keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 96 + n (PDF 1 = S. 97, PDF 12 = S. 108). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Sumanathilaka, T. G. D. K., Nicholas Micallef & Julian Hough (2024). Can LLMs assist with Ambiguity? A Quantitative Evaluation of various Large Language Models on Word Sense Disambiguation. In: Ruslan Mitkov, Saad Ezzini, Tharindu Ranasinghe, Ignatius Ezeani, Nouran Khallaf, Cengiz Acarturk, Matthew Bradbury, Mo El-Haj & Paul Rayson (Hg.), *Proceedings of the First International Conference on Natural Language Processing and Artificial Intelligence for Cyber Security (NLPAICS)*. Lancaster, S. 97 bis 108.
- **DOI/URL:** keine DOI; https://aclanthology.org/2024.nlpaics-1.12/ (Herausgeber:innen, Ort, Monat Juli und Seiten aus dem BibTeX der Anthology, abgerufen 2026-11-13; Kopfzeile S. 97: „Proceedings of the 1st International Conference on NLP & AI for Cyber Security, pages 97–108, July 29–30, 2024“). Vorname des Erstautors laut PDF-Metadaten Deshan Koshala.
- **Preprint:** arXiv:2411.18337 (laut `beschaffung-2026-10-30/2-vorschlaege.md` fünf Versionen bis 15.9.2025; nicht selbst geprüft). Meconi et al. 2025 zitieren diese Fassung als „Sumanathilaka et al. 2025“.
- **Lizenz:** CC BY 4.0 (ACL Anthology, Material ab 2016, laut Fußzeile der Anthology, abgerufen 2026-11-13).
- **Art:** Konferenzbeitrag
- **Sprache:** Englisch

## Worum es geht

Die Autor:innen testen, wie gut LLMs einem markierten Wort in einem Satz den richtigen Sense aus dem FEWS-Inventar (Wiktionary-Glossen) zuordnen (S. 100). In drei Phasen wird erst ein Prompt iterativ verbessert (Glossen, Beispiele aus den FEWS-Trainingsdaten, Few-shot-Chain-of-Thought), dann mit diesem Prompt acht kommerzielle und offene Modelle auf 1.050 Testitems verglichen und schließlich an den Fehlern der GPT-Modelle weitere Prompttechniken erprobt (S. 101 bis 104). Bestes Modell auf Vorhersageebene ist GPT-4 Turbo mit 0,81 (S. 103, Tab. 6). Die Arbeit ist für die Dissertation vor allem als Beispiel für Prompt- und Antwortformat und als Gegenbeispiel für die Trennung von Entwicklungs- und Testdaten nützlich; ihre Tabellen enthalten Unstimmigkeiten.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| FEWS wurde gewählt, weil es mehr selten gebrauchte ambige Wörter enthält als das Unified Evaluation Framework (Raganato et al. 2017). Das Zielwort steht zwischen `<WSD>`-Tags; die Ausgabe ist eine Sense-ID wie `dictionary.noun.0`. | S. 100, Abschn. 3.1, Tab. 1 und 2 | eigene Wahl; FEWS referiert (Blevins et al. 2021) |
| Wissensbasis: die FEWS-Trainingsdaten, als Trie nach Wort und Wortart abgelegt; daraus werden Beispielsätze je Sense in den Prompt geholt. | S. 100, Abschn. 3.1; S. 101 | eigenes Verfahren |
| **Phase 1:** Der Prompt wurde „human-in-the-loop“ vom Hauptautor iterativ verfeinert, falsche Vorhersagen wurden „systematically analyzed to improve the prompt“. Erst Zero-shot mit gefilterten Glossen (GPT-3.5 Turbo), dann Few-shot-CoT mit Beispielen aus der Wissensbasis. | S. 101, Abschn. 3.2 | eigenes Verfahren |
| Der gewählte Prompt (Tab. 4) nennt die möglichen Senses mit IDs und Definitionen, Beispiele, den Satz, verlangt erst die Bedeutung zu erschließen, dann die passende Sense-ID; bei mehreren IDs „in order of confidence level“; Ausgabe als JSON mit Wort und IDs. | S. 101, Tab. 4 | eigenes Material |
| **Phase 1, Ergebnis (Tab. 5):** allgemeiner Prompt mit Wissensbasis 0,65, erweiterter 0,70, verbesserter mit Prompt-Anreicherung 0,82 (alle Wörter); die Verbesserung ist laut McNemar-Test signifikant (p < 0,05). Nomen schneiden in allen Varianten am besten ab. | S. 103, Tab. 5 | eigenes Ergebnis |
| **Phase 2:** 1.050 Testitems aus FEWS im Verhältnis 4:3:3 für Nomen, Verben, Adjektive (400/300/300) plus 50 Adverbien; richtig, wenn die vorhergesagte ID der Gold-ID entspricht. Bewertet auf zwei Ebenen: Vorhersage (P, beste Antwort) und Vorschlag (S, die zwei sichersten Antworten). | S. 102, Abschn. 3.3 und 3.5; S. 103, Tab. 6 | eigenes Verfahren |
| Einstellungen: Temperatur 0, maximal 500 Ausgabetokens, Rolle „helpful assistant for identifying word senses“; GPT über OpenAI-API, Gemini über Google AI Studio, offene Modelle über die „together“-API mit denselben Einstellungen. Modellversionen oder Snapshot-IDs werden nicht genannt. | S. 102, Abschn. 3.5 | eigene Angabe |
| Ergebnis Phase 2: GPT-4 Turbo auf Vorhersageebene am besten (0,81), Llama-2-70B auf Vorschlagsebene (0,83); Verben am schwersten. | S. 103, Tab. 6 und Text | eigenes Ergebnis |
| **Phase 3:** nur an den falsch vorhergesagten Items (234 bei GPT-3.5, 191 bei GPT-4) drei Ansätze: Self-Consistency mit Mehrheitsentscheid über drei Strategien, Synonyme im Prompt, Prompt-Kette mit aspektbasierter Vorfilterung der Senses. Je nach Modell löst der beste Ansatz 29 % bzw. 30 % dieser Fehler. | S. 104, Tab. 7; Prompts im Anhang S. 107 bis 108 (Tab. 8) | eigenes Ergebnis |
| Die Autor:innen nennen die Verbesserungen selbst „relatively modest“ und empfehlen eine Prüfung auf SemCor, Senseval und SemEval. | S. 104, Abschn. 4 und 5 | eigene Einschätzung |

## Daten, Methode, Zahlen

**Tab. 5 (S. 103, Seitenbild), Genauigkeit Phase 1:**

| Ansatz | Nomen (400) | Verben (300) | alle (1050) |
|---|---|---|---|
| allgemeiner Prompt mit Wissensbasis | 0,70 | 0,60 | 0,65 |
| erweiterter Prompt mit Wissensbasis | 0,76 | 0,65 | 0,70 |
| verbesserter Prompt mit Anreicherung | 0,85* | 0,78* | 0,82* |

**Tab. 6 (S. 103, Seitenbild), Genauigkeit Phase 2, Vorhersageebene P und Vorschlagsebene S (Top 2):**

| Modell | P Nomen | P Verben | P Adj. | P Adv. | P alle | S alle |
|---|---|---|---|---|---|---|
| GPT-4 Turbo | 0,85 | 0,77 | 0,82 | 0,78 | 0,81 | 0,82 |
| GPT-3.5 Turbo | 0,81 | 0,75 | 0,75 | 0,76 | 0,79 | 0,82 |
| Llama-3-70B | 0,83 | 0,71 | 0,78 | 0,72 | 0,77 | 0,80 |
| Llama-2-70B | 0,67 | 0,56 | 0,61 | 0,58 | 0,68 | 0,83 |
| Gemini | 0,76 | 0,63 | 0,73 | 0,74 | 0,74 | 0,74 |
| Yi-34B | 0,65 | 0,51 | 0,57 | 0,52 | 0,66 | 0,76 |
| Gemma 7B | 0,49 | 0,41 | 0,51 | 0,46 | 0,57 | 0,73 |
| Mixtral 7B | 0,43 | 0,32 | 0,46 | 0,42 | 0,52 | 0,70 |

**Unstimmigkeiten (eigene Rechnung):**

- Tab. 6: Bei Llama-2, Yi, Gemma und Mixtral liegt der P-Wert „alle“ **über jedem** Einzelwert der Wortarten (z. B. Gemma 0,57 bei Einzelwerten 0,41 bis 0,51). Ein gewichtetes Mittel kann das nicht ergeben; mit den Gewichten 400/300/300/50 käme Gemma auf etwa 0,47. Mindestens eine Spalte ist falsch.
- Tab. 3 (S. 100): Die vier Wortarten der FEWS-Trainingsdaten summieren sich zu 101.431, die Tabelle nennt 101.458.
- Tab. 7 (S. 104): 42 von 191 sind 0,22 (Tabelle 0,21), 49 von 234 sind 0,21 (Tabelle 0,20); Rundungsabweichungen.
- Tab. 5 hat dieselben Spaltengrößen (400/300/1050) wie der Testsatz der Phase 2. Der Text sagt nicht ausdrücklich, dass Phase 1 an denselben Items lief; ein getrennter Entwicklungssatz wird nirgends erwähnt.

**Ungültige Antworten:** Abb. 1 (S. 102) zeigt nach dem LLM einen Schritt „Post processing“, der nicht beschrieben wird. Wie unparsbare Antworten, IDs außerhalb der Liste oder fehlende IDs gezählt werden, steht nicht im Werk.

## Wörtliche Stellen

> „Incorrect predictions were systematically analyzed to improve the prompt and generate optimal results.“ (S. 101)

> „If you have more than one senseIDs identified after above steps, you can return the senseIDs in order of confidence level.“ (S. 101, Tab. 4)

> „During the evaluation process, the model was configured to maintain a temperature of 0 and a maximum token limit of 500 for each output.“ (S. 102)

## Bezug zur Dissertation

- **A17 (Prompt nur am Pilot-Pool wählen, Wirkungen nur an ungesehenen Items berichten):** Das Werk ist ein Gegenbeispiel. Der Prompt wurde an falschen Vorhersagen iterativ nachgebessert (S. 101), und ein getrennter Entwicklungssatz wird nicht genannt; Phase 3 arbeitet ausdrücklich nur an den Fehlern und berichtet, wie viele davon nachträglich gelöst werden (S. 104). So gewonnene Zuwächse sind auf den Testdaten optimiert. Das stützt die Trennung in A17 als Begründung („ohne sie ist ein Prompt-Zuwachs nicht von Überanpassung zu unterscheiden“).
- **A23 und A29 (`MEHRERE`-Antworten nur richtig, wenn alle IDs im Gold stehen):** Die „Vorschlagsebene“ zählt eine Antwort als richtig, wenn der Gold-Sense unter den zwei sichersten ist (S. 102 bis 103). Das belohnt genau das Absichern, das A23 ausschließen will: Bei schwachen Modellen steigt der Wert dadurch um bis zu 18 Punkte (Mixtral 0,52 auf 0,70, Tab. 6), bei Gemini gar nicht. Ein gutes Beispiel dafür, dass ein Mengenformat den Vergleich mit einer Einzelbaseline (MFS) verzerrt.
- **Protokoll §9.2, ungültige Antworten (A18):** Das Werk lässt bis zu mehreren IDs zu und gibt keine Regel für ungültige Antworten (S. 101, S. 102). Es bestätigt, dass die Regelung im Protokoll eine Lücke der Literatur schließt, liefert aber keine Vorlage.
- **A16 (mehrere Läufe, Mehrheit ist ein Ensemble):** Self-Consistency mit Mehrheitsentscheid über drei Strategien in **einem** Prompt (S. 107, Tab. 8) ist eine weitere Form von Ensemble innerhalb eines Aufrufs. Falls ein solcher Prompt in Freeze 2 erwogen wird, gehört er zur Frage, was als LLM-Vorhersage gilt.
- **A26 (Konfiguration vollständig berichten):** Temperatur und Tokenlimit werden genannt, Modellversionen, Abfragedatum und weitere Sampling-Parameter nicht (S. 102). Beleg dafür, dass selbst neuere Arbeiten die Angaben aus A26 nicht liefern.
- **Vergleichbarkeit mit dem MHDBDB-Inventar:** FEWS zeigt Glossen, Synonyme und Beispielsätze je Sense (S. 100, Tab. 1); der Zugewinn in Phase 1 kommt gerade aus Beispielen und Glossen (S. 103). Die MHDBDB-Karten haben keine Definitionen und das Protokoll zeigt bewusst keine LLM-erzeugten (Protokoll §5). Die Zahlen sind daher keine Erwartung für das MHDBDB-Setting; ob Few-shot-Beispiele aus Silber (A17) einen ähnlichen Effekt haben, wäre am Pilot-Pool zu messen.
- **Kontamination (Protokoll §10):** Nicht besprochen. FEWS beruht auf Wiktionary und ist öffentlich; ob Testsätze in den Trainingsdaten der Modelle stehen, prüft das Werk nicht.
- **Protokoll §9.2 (gepaarter Vergleich):** Das Werk nutzt den McNemar-Test für Promptvergleiche (S. 103), allerdings ohne Angabe, gegen welches Paar genau der Stern gilt. Als Beleg für McNemar in der LLM-WSD taugt es, als Vorbild für die Berichtsweise nicht.

## Grenzen und Einwände

- Rechnerisch unmögliche Gesamtwerte in Tab. 6 und kleinere Summen- und Rundungsfehler (siehe oben); die Zahlen sind nur mit Vorbehalt zitierbar.
- Keine Trennung von Entwicklungs- und Testdaten erkennbar; Promptwahl und Fehleranalyse am Testmaterial.
- Keine Angaben zu Modellversionen, ungültigen Antworten, Läufen oder Streuung.
- Nur Englisch, ein Datensatz (FEWS), Wörterbuchglossen als Inventar.
- Zweck der Arbeit laut Einleitung und Schluss ist Cyber Threat Intelligence (S. 97, 104); ein Bezug der Experimente dazu wird nicht hergestellt.

## Weiterführend

- Blevins, Joshi & Zettlemoyer 2021, FEWS, EACL, S. 455 bis 465, doi:10.18653/v1/2021.eacl-main.36 (S. 100, 105).
- Sainz et al. 2023, Zero-Shot WSD mit Domäneninventaren (S. 99 bis 100, 106): WSD als Textual Entailment.
- Wang et al. 2023, Self-Consistency, arXiv:2203.11171 (S. 102, 107); schon in `goldstandard/VORSCHLAEGE-2026-10.md` als Primärquelle vorgeschlagen.
- Pasini, Raganato & Navigli 2021, XL-WSD, AAAI (S. 98, 106); schon zur Beschaffung vorgeschlagen.
- Loureiro et al. 2021, Analysis and Evaluation of Language Models for WSD, *Computational Linguistics* (S. 100, 106).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF und hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
