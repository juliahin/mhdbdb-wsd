# Ghizzota, Basile, Siciliani & Semeraro 2025: The Meaning of Beatus, lateinische WSD mit aktuellen LLMs

**Datei:** `pdf/Ghizzota-etal-2025-Meaning-of-Beatus.pdf` (nur lokal; 11 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Tab. 5 und 6 am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF bei CEUR (Vol-4112, `45_main_long.pdf`) und mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-13). Keine Markierungen.

**Seitenzählung:** Das PDF trägt keine Seitenzahlen. Die ACL Anthology gibt S. 469 bis 479 an (11 Seiten, passt zur Seitenzahl des PDFs); daraus folgt PDF-Seite n = S. 468 + n, an einem paginierten Exemplar nicht geprüft. Unten steht deshalb „PDF-S. n“.

## Bibliografie

- **Vollständig:** Ghizzota, Eleonora, Pierpaolo Basile, Lucia Siciliani & Giovanni Semeraro (2025). The Meaning of Beatus: Disambiguating Latin with Contemporary AI Models. In: Cristina Bosco, Elisabetta Jezek, Marco Polignano & Manuela Sanguinetti (Hg.), *Proceedings of the Eleventh Italian Conference on Computational Linguistics (CLiC-it 2025)*, Cagliari, 24. bis 26. September 2025. CEUR Workshop Proceedings 4112, S. 469 bis 479.
- **DOI/URL:** keine DOI gefunden. https://ceur-ws.org/Vol-4112/45_main_long.pdf (Bandseite: Herausgeberinnen und Herausgeber, CC BY 4.0, URN urn:nbn:de:0074-4112-x, ISSN 1613-0073; abgerufen 2026-11-13). ACL Anthology 2025.clicit-1.46 (BibTeX: S. 469 bis 479, ISBN 979-12-243-0587-3, Verlag „CEUR Workshop Proceedings“; abgerufen 2026-11-13). Fußzeile PDF-S. 1: „published 2025-11-30“.
- **Lizenz:** CC BY 4.0 (Fußnote PDF-S. 1 und CEUR-Bandseite).
- **Art:** begutachteter Konferenzbeitrag (CLiC-it, „main long“)
- **Sprache:** Englisch
- **Daten und Code:** github.com/swapUniba/latin-wsd (PDF-S. 6, Anm. 16; nicht aufgerufen).
- **Nicht verwechseln** mit Ghizzota, Marongiu, Basile, Ferilli & McGillivray 2026 (LREC, Knowledge Graphs), das diese Arbeit als Baseline nutzt.

## Worum es geht

Die Arbeit prüft, wie gut LLMs lateinische Wortbedeutungen unterscheiden, zero-shot (GPT-4o-mini, LLaMA-3.3-70B-instruct, LLaMA-3.1-8B-instruct) und nach Feinjustierung (LLaMA-3.1-8B-instruct mit LoRA) (PDF-S. 1 bis 2, 5 bis 6). Datengrundlage ist der lateinische SemEval-2020-Datensatz: Zu jedem Beleg hat eine Annotator:in für jede Wörterbuchdefinition des Lemmas eine Verwandtschaftsstufe 1 bis 4 vergeben (DURel). Daraus bauen die Autor:innen je Paar aus Satz und Sense einen Prompt, einmal als Vorhersage der Stufe (Regression), einmal als Ja/Nein (Stufe ab 3 = ja) (PDF-S. 4). Zero-shot ist GPT-4o-mini am besten; das feinjustierte 8B-Modell übertrifft die größeren Modelle bei der Stufenvorhersage deutlich und liegt bei Ja/Nein gleichauf mit GPT-4o-mini (PDF-S. 7 bis 8).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| WSD für Latein mit Sprachmodellen sei kaum erforscht; bisher Latin BERT (75,4 % auf zwei Hauptsenses, 201 Lemmata), TLL-Daten (Macro-F1 von 0,695 auf 0,794) und Language Pivoting (Ghinassi et al. 2024). | PDF-S. 2 bis 3, Abschnitt 2.1 | referiert |
| Der SemEval-2020-Datensatz sei bis heute der einzige von Latinist:innen manuell annotierte Benchmark für Latein. | PDF-S. 3 | Behauptung der Autor:innen |
| Datensatz: Ausschnitt aus LatinISE (13 Mio. Wörter); zwei Teilkorpora (2. Jh. v. Chr. bis 0, 1,7 Mio. Tokens; 0 bis 21. Jh., 9,4 Mio.); 40 Zielwörter, davon 23 stabil und 17 mit Bedeutungswandel durch das Christentum; je 60 Belege (30 je Teilkorpus), zusammen 2.398. | PDF-S. 3 bis 4, Abschnitt 3.1 | referiert (Schlechtweg et al. 2020; McGillivray et al. 2022) |
| Inventar: Hauptdefinitionen aus Logeion (Lewis & Short, Lewis, Du Cange), je nach Fall vereinfacht oder gekürzt. | PDF-S. 4 | referiert |
| Annotation: 10 Annotator:innen mit hoher Lateinkompetenz (vom Studium bis zur Forschung), **eine pro Zielwort**; Stufen 1 (unrelated) bis 4 (identical), 0 = „cannot decide“. | PDF-S. 4 | referiert |
| Übereinstimmung nur für *virtus* mit vier Annotator:innen gemessen: mittlere paarweise Spearman-Korrelation 0,69, vergleichbar mit Werten für Gegenwartssprachen (Englisch 0,69, Schwedisch 0,57, Deutsch 0,59). | PDF-S. 4 | referiert (McGillivray et al. 2022; Vergleichswerte zitiert nach Schlechtweg et al. 2018) |
| Aufgabenformat: ein Prompt je Paar aus Satz und Sense; 8.989 Paare (70/30 geschichtet: 6.299 Training, 2.690 Test). Binär ohne Stufe 0: 8.930. Oportet wegen fehlender Annotation ausgeschlossen. | PDF-S. 4 bis 5, Abschnitt 3.2, Tab. 2 | eigene Aufbereitung |
| Binäre Testmenge stark unausgewogen: 956 ja, 1.719 nein (35,73 % ja). | PDF-S. 5 | eigenes Ergebnis |
| Regression (Stufe 0 bis 4): feinjustiertes LLaMA-3.1-8B mit kleinstem Fehler und bestem F1 (0,6940), vor GPT-4o-mini (0,4170) und LLaMA-3.3-70B (0,2543). | PDF-S. 7, Tab. 5 | eigenes Ergebnis |
| Zero-shot verwechseln die Modelle oft Stufe 1 mit höheren Stufen (GPT-4o-mini 508-mal 1 als 4; LLaMA-3.1-8B 913-mal 1 als 3, 579-mal als 4); das feinjustierte Modell erkennt Stufe 1 am besten, weil es zur häufigsten Klasse hin überanpasst. | PDF-S. 7, Abschnitt 5.1, Anhang B | eigenes Ergebnis, Deutung |
| Binär: feinjustiertes 8B-Modell F1 0,7906, GPT-4o-mini 0,7682 (bei höherer Precision und Accuracy); LLaMA-3.3-70B 0,6355, LLaMA-3.1-8B zero-shot 0,5336. | PDF-S. 7 bis 8, Tab. 6 | eigenes Ergebnis |
| Fazit: LLMs haben eine „non-trivial baseline ability“ zero-shot; Feinjustieren, besonders mit Instruktionen, bringt Verbesserungen; die Unausgewogenheit der Klassen habe die Vorhersagen wohl beeinflusst. | PDF-S. 1, 7 | eigene Schlussfolgerung |

## Daten, Methode, Zahlen

- **Tab. 2 (PDF-S. 5), Verteilung der DURel-Stufen:** 0: 59; 1: 5.050; 2: 700; 3: 1.100; 4: 2.080; zusammen 8.989 (Training 6.299, Test 2.690).
- **Modelle (PDF-S. 5 bis 6, Tab. 3 und 4):** GPT-4o-mini (Azure, Parameter unbekannt), LLaMA-3.3-70B-instruct-turbo (TogetherAI), LLaMA-3.1-8B-instruct (Unsloth) zero-shot; LLaMA-3.1-8B-instruct mit LoRA feinjustiert (Rang 32, Alpha 64, Lernrate 2e-4, Batch 32, 5 Epochen, eine RTX A6000). Für zero-shot derselbe Prompt wie beim Feinjustieren, nach einer „preliminary prompt engineering step“ (PDF-S. 6).
- **Prompt (PDF-S. 4, Listings 1 und 2):** Zielwort, Satz mit `[TARGET]`-Markierung, **eine** Bedeutung als englische Glosse; Antwort nur mit Stufe bzw. „yes“/„no“. Das Modell sieht also nie das ganze Sense-Menü eines Lemmas.
- **Maße (PDF-S. 6):** MSE, RMSE, gewichtete Precision, Recall und F1, Macro-F1, Micro-F1, „Balanced Accuracy“ (Mittel der Recalls je Klasse). Die Spalte „Accuracy“ in Tab. 5 und 6 ist vermutlich diese Balanced Accuracy; ausdrücklich gesagt wird das nicht.
- **Tab. 5 (PDF-S. 7), Regression, am Seitenbild geprüft:**

| Modell | MSE | RMSE | Precision | Recall | Accuracy | F1 | Macro-F1 | Micro-F1 |
|---|---|---|---|---|---|---|---|---|
| GPT-4o-mini | 1,0743 | 2,4595 | ,6371 | ,4190 | ,3095 | ,4170 | ,2504 | ,4190 |
| LLaMA-3.3-70B-instruct-turbo | 1,4063 | 3,1550 | ,6056 | ,2743 | ,2372 | ,2543 | ,1742 | ,2743 |
| LLaMA-3.1-8B-instruct | 1,6491 | 3,7405 | ,4748 | ,1717 | ,1993 | ,1037 | ,1037 | ,1717 |
| LLaMA-3.1-8B-instruct-ft | 0,7699 | 1,8093 | ,6854 | ,7071 | ,4354 | ,6940 | ,4456 | ,7071 |

- **Tab. 6 (PDF-S. 8), binär, am Seitenbild geprüft:**

| Modell | Precision | Recall | Accuracy | F1 | Macro-F1 | Micro-F1 |
|---|---|---|---|---|---|---|
| GPT-4o-mini | ,7974 | ,7634 | ,7817 | ,7682 | ,7573 | ,7634 |
| LLaMA-3.3-70B-instruct-turbo | ,7030 | ,6301 | ,6654 | ,6355 | ,6284 | ,6301 |
| LLaMA-3.1-8B-instruct | ,5947 | ,5271 | ,5547 | ,5336 | ,5253 | ,5271 |
| LLaMA-3.1-8B-instruct-ft | ,7901 | ,7933 | ,7637 | ,7906 | ,7694 | ,7933 |

- **Innere Unstimmigkeiten:** RMSE muss die Wurzel aus MSE sein; die Tabelle nennt RMSE größer als MSE (z. B. 1,0743 und 2,4595), was für MSE > 1 nicht möglich ist. Die Zahl der Zielwörter lautet hier 23 stabil plus 17 gewandelt (PDF-S. 4), bei Ghinassi et al. 2024 (S. 10075) 20 plus 20, bei Ghizzota et al. 2026 (S. 10941) 22 plus 17 nach Ausschluss von *oportet*. Die 35,73 % „of the entire dataset“ (PDF-S. 5) beziehen sich nach den Zahlen 956 + 1.719 = 2.675 nur auf die Testmenge.

## Wörtliche Stellen

> „The lack of native Latin speakers adds a further layer of complexity to the sense annotation process.“ (PDF-S. 4)

> „Annotators – only one per target word – scored the relatedness between a usage and a sense definition […]“ (PDF-S. 4)

> „It is worth noticing that the dataset of choice was initially devised for the Unsupervised LSCD task, not for WSD; therefore, comparing the results of the shared task with the results of this work is not feasible.“ (PDF-S. 6)

## Bezug zur Dissertation

- **PROTOKOLL §1 und §9.2 (Aufgabenformat, Vergleich mit MFS):** Hier entscheidet das LLM für jedes Paar aus Beleg und **einer** Bedeutung, ob sie passt; es wählt nicht aus dem Menü des Lemmas. Die F1-Werte (bis 0,79) messen deshalb etwas anderes als die Genauigkeit der Sense-Wahl im Protokoll und sind mit ihr nicht vergleichbar. Eine MFS-Baseline gibt es nicht. Für die Einordnung der eigenen Ergebnisse taugt das Paper nur als Hinweis, dass aktuelle LLMs Latein zero-shot „nicht trivial“ disambiguieren (PDF-S. 1).
- **`goldstandard/LITERATUR-IAA.md`, „Historische Sprachen“:** Dort steht, SemEval-2020 Task 1 habe Latein „auf eine Annotator:in pro Wort umstellen“ müssen, „also ohne IAA“ (Schlechtweg et al. 2020 ○). Dieses Paper bestätigt eine Annotator:in pro Zielwort, berichtet aber eine Übereinstimmung für ein einzelnes Wort (*virtus*, vier Personen, Spearman 0,69; PDF-S. 4, nach McGillivray et al. 2022). „Ohne IAA“ ist also zu schärfen: IAA nur an einem von 40 Wörtern. Die Vergleichswerte 0,69, 0,57, 0,59 schreibt das Paper Schlechtweg et al. 2018 zu; `LITERATUR-IAA.md` nennt für DURel ρ ≈ 0,57 bis 0,68 und für SemEval Runde 1 ρ ≈ 0,58 bis 0,69. Die Zuordnung ist am Original (Schlechtweg et al. 2018, 2020) zu prüfen, bevor eine der Zahlen zitiert wird.
- **PROTOKOLL §7 und A5 (doppelte Annotation):** Ein Gold mit einer Annotator:in pro Wort und IAA an einem Wort ist der Normalfall, den der doppelt annotierte Goldstandard verbessern soll. Das Paper ist ein aktueller Beleg (2025) für diese Lage bei einer historischen Sprache mit LLM-Evaluation.
- **PROTOKOLL §9.1 Punkt 4 (Prävalenz):** Die Verteilung der Urteile ist stark schief (5.050 von 8.989 sind „unrelated“, Tab. 2), und die Autor:innen führen Fehler auf diese Schiefe zurück (PDF-S. 7). Das stützt die geplante Kontrolle der Randverteilungen.
- **PROTOKOLL §5 (keine LLM-generierten Definitionen, Kartendarstellung):** Die Bedeutungen werden als gekürzte englische Glossen aus Wörterbüchern gezeigt (PDF-S. 4). Das ist eine Alternative zu den Begriffsnamen der MHDBDB; ob die Sprache der Glosse (Englisch für Latein) die Leistung beeinflusst, prüft das Paper nicht.
- **Feinjustieren gegen Prompting:** Das feinjustierte 8B-Modell schlägt das 70B-Modell zero-shot (PDF-S. 7). Für den Goldstandard folgt daraus nichts direkt, weil das Protokoll kein Feinjustieren vorsieht; es ist aber ein Gegenargument gegen „größer ist besser“ als Auswahlregel für Freeze 2 (PROTOKOLL §4.10).

## Grenzen und Einwände

- Der Datensatz war für die Erkennung von Bedeutungswandel gebaut, nicht für WSD (PDF-S. 6); die Lemmata sind nach Wandel durch das Christentum gewählt, nicht nach Polysemie oder Häufigkeit.
- Binäres Format je Sense statt Sense-Wahl: Ein Modell kann für mehrere Senses „ja“ sagen oder für keinen; wie das auf Belegebene ausgeht, wird nicht ausgewertet.
- Gold stammt von je einer Person pro Wort; Übereinstimmung nur an *virtus*.
- Keine Baseline außer den Modellen selbst (keine MFS, kein Zufall, kein „immer nein“; „immer nein“ träfe in der binären Testmenge 64 %).
- Rechenfehler oder Fehlbeschriftung bei RMSE; „Accuracy“ nicht eindeutig definiert (siehe oben).
- Einzelner Lauf, keine Streuung, keine Signifikanztests.
- Die Autor:innen nutzten nach eigener Angabe ChatGPT und Grammarly zum Umformulieren (PDF-S. 11).

## Weiterführend

- McGillivray et al. 2022, *Journal of Latin Linguistics* 21, S. 47 bis 105 (PDF-S. 4, 8): Annotationsrahmen und IAA-Messung an *virtus*; Quelle für die Übereinstimmung.
- Schlechtweg, Schulte im Walde & Eckmann 2018, DURel (PDF-S. 4, 9): Herkunft der Vergleichswerte 0,69/0,57/0,59.
- Basile, Siciliani, Musacchio & Semeraro 2025 (PDF-S. 3, 9): liegt vor, `zusammenfassungen/Basile-etal-2025-WSD-Capabilities-LLMs.md`.
- Yae et al. 2025 (PDF-S. 3, 9): liegt vor, `zusammenfassungen/Yae-etal-2025-LLMs-WSD.md`.
- Kibria, Dipta & Adnan 2024, CoNLL (PDF-S. 3, 9): LLM-WSD im Mehrfachauswahlformat.
- Basile, Musacchio & Siciliani 2024, Ita-Sense, CLiC-it 2024 (PDF-S. 3, 9).
- Loureiro et al. 2021, *Computational Linguistics* 47, S. 387 bis 443 (PDF-S. 3, 9).
- Cabiddu, Nikolaus & Fourtassi 2023 (PDF-S. 3, 9): MFS-Bias von Sprachmodellen.

## Julias Notizen im PDF

Keine. Das PDF hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
