# Basile et al. 2025: Exploring the Word Sense Disambiguation Capabilities of Large Language Models

**Datei:** `pdf/Basile-etal-2025-WSD-Capabilities-LLMs.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, Volltext (14 Seiten) gelesen, Tabellen 3 bis 10 an Textebene und Seitenbild geprüft; Bibliografie und Lizenz an arXiv geprüft. Im PDF keine Markierungen von Julia.

**Seitenzählung:** Preprint mit eigener Zählung 1 bis 14; gedruckte Seite = PDF-Seite.

## Bibliografie

- **Vollständig:** Basile, Pierpaolo, Lucia Siciliani, Elio Musacchio & Giovanni Semeraro, 2025. Exploring the Word Sense Disambiguation Capabilities of Large Language Models. arXiv:2503.08662 [cs.CL], v1.
- **DOI/URL:** https://arxiv.org/abs/2503.08662 (am 2026-10-28 abgerufen; einzige Version v1 vom 11. März 2025, kein „Journal reference“, kein verknüpfter DOI). Das PDF trägt das Datum 12. März 2025 und den Kopf „A Preprint“ (S. 1).
- **Lizenz:** CC BY-NC-SA 4.0 laut arXiv-Seite ✔ (im PDF selbst kein Lizenzvermerk).
- **Art:** Preprint. Eine begutachtete Fassung wurde am 2026-10-28 nicht gefunden (arXiv ohne Journal-Ref, Crossref-Suche nach Titel und Autor ohne Treffer, Websuche ohne Treffer) ○. Das schließt eine Veröffentlichung unter anderem Titel nicht aus.
- **Sprache:** Englisch
- **Ressourcen:** Daten und Modellausgaben auf Zenodo (records/15007563), Code auf GitHub (swapUniba/LLM-wsd), feinjustierte Modelle auf HuggingFace (S. 9); nicht abgerufen.

## Worum es geht

Die Arbeit prüft offene LLMs auf WSD in fünf Sprachen (Englisch, Italienisch, Spanisch, Französisch, Deutsch) und baut dafür den Benchmark XL-WSD zu zwei Aufgaben für generative Modelle um: (1) eine kurze Definition des Zielworts im Satz erzeugen, (2) aus einer nummerierten Liste von BabelNet-Glossen die richtige wählen (S. 1 bis 4). Sechs Modelle von 7B bis 405B Parametern laufen zero-shot mit greedy decoding (S. 5); zusätzlich wird Llama-3.1-8B-Instruct auf den Trainingsdaten feinjustiert (S. 5). Zero-shot erreichen die großen Modelle im Englischen etwa 75 % Genauigkeit (S. 6, Tab. 6), schlagen aber die überwachten Systeme nur im Englischen und knapp im Deutschen (S. 8, Tab. 10). Das feinjustierte 8B-Modell erreicht im XL-WSD-Maß F1 0,8472 im Mittel und 0,8652 im Englischen und liegt damit nach Darstellung der Autor:innen über dem Stand der Technik (S. 8 bis 9).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Mit dem Aufkommen der LLMs ist das Interesse an WSD in der klassischen Definition zurückgegangen; zu decoder-only LLMs als Disambiguierer gibt es wenig Arbeiten. | S. 1, Abstract; S. 3 | Einschätzung der Autor:innen |
| Multiple-Choice-Aufbau: Aus allen Senses des Worts werden alle annotierten (richtigen) entfernt, dann wird **einer** der richtigen zufällig wieder eingefügt; jede Liste enthält genau eine richtige Option. Items mit weniger als zwei Optionen und monoseme Wörter fallen weg. | S. 3 bis 4, Abschnitt 3, Fn. 1 und 2 | eigenes Verfahren |
| Zero-shot, ohne Übersetzung, Genauigkeit Multiple Choice Englisch: Llama-3.1-405B 0,7532, Llama-3.1-70B 0,7520, Qwen2-72B 0,7370, Gemma2-9B 0,6762, Mistral-7B 0,6171, Llama-3.1-8B 0,5587. | S. 6, Tab. 6 | eigenes Ergebnis |
| Größere Modelle sind besser, aber 70B und 405B liegen nah beieinander; unter den mittleren ist Gemma2-9B in Multiple Choice in allen Sprachen am besten, Llama-3.1-8B bei der Definitionserzeugung (RougeL). | S. 6, Abschnitt 5.1 | eigenes Ergebnis |
| Maschinell übersetzte Glossen ändern die Rangfolge der Modelle kaum, senken aber die Werte allgemein. | S. 6, Abschnitt 5.1; Tab. 7 (S. 7) | eigenes Ergebnis |
| Feinjustierung: Genauigkeit steigt mit der Menge der Trainingsdaten, außer im Deutschen, das am wenigsten Trainingsinstanzen hat. | S. 7, Tab. 8 | eigenes Ergebnis |
| XL-WSD-Vergleich (F1, offizielles Bewertungswerkzeug): Llama-3.1-8B-FT/ALL EN 0,8652, Mittel 0,8472; bestes Zero-shot-Modell im Mittel Llama-3.1-405B 0,7467; XLMR-Large 0,7937. | S. 8, Tab. 10 | eigenes Ergebnis (Vergleichswerte der anderen Systeme aus der Literatur übernommen) |
| Zero-shot-LLMs übertreffen die Baselines nur im Englischen und Deutschen und sind im Italienischen und Spanischen schwach. | S. 8, Aufzählung unter Tab. 10 | eigenes Ergebnis |
| Ein feinjustiertes mittelgroßes Modell übertrifft alle großen Modelle und Baselines. | S. 8, S. 9 | eigenes Ergebnis (für Spanisch durch Tab. 10 nicht gedeckt, siehe Grenzen) |
| Loureiro et al. 2021: BERT-artige Modelle unterscheiden Senses gut, auch mit wenigen Beispielen; grobkörnige Nomen-WSD sei unter idealen Bedingungen fast gelöst. | S. 2, Abschnitt 2 | referiert |
| Cabiddu et al. 2023 finden bei Sprachmodellen eine Verzerrung zum dominanten Sense. | S. 2, Abschnitt 2 | referiert |

## Daten, Methode, Zahlen

- **Korpus und Inventar:** XL-WSD (Pasini et al. 2021), Entwicklungs- und Testdaten in 18 Sprachen, davon hier fünf; Inventar BabelNet (S. 4). Glossen fehlen in BabelNet nicht für Englisch (Fn. 3, S. 4), sonst teils; daher zwei Fassungen: nur Items mit Glossen in der Sprache, oder fehlende Glossen aus dem Englischen mit NLLB-200 (1.3B) übersetzt (S. 4).
- **Umfang (S. 4, Tab. 3):** ohne Übersetzung Test 10.480 (Definition) und 9.847 (Multiple Choice), mit Übersetzung 11.473 und 11.168; Training 0,86 bis 1,45 Mio. Instanzen. Multiple-Choice-Test ohne Übersetzung pro Sprache: EN 6.605, IT 1.529, ES 1.041, FR 442, DE 230 (S. 11, Tab. 11).
- **Prompt Multiple Choice** (S. 4, Tab. 2): „Given the word "wi" in the input sentence, choose the correct meaning from the following: Ci. Generate only the number of the selected option. Input: "Sk"“. Die Optionen sind **Glossen**, mit 1), 2), … nummeriert; im Beispiel *art* vier Optionen. Kein Systemprompt bei der Feinjustierung (S. 5), für Zero-shot nicht angegeben. Prompts in allen fünf Sprachen, von Muttersprachler:innen oder Übersetzungsexpert:innen geprüft (S. 9, S. 11; deutscher Prompt S. 14, Tab. 20).
- **Mehrfachvorkommen** des Zielworts im Satz: „the x occurrence of the word“ mit Ordinalzahl; Sätze mit mehr als sechs Vorkommen fallen weg (S. 3).
- **Modelle** (S. 5): Llama-3.1-8B-Instruct, Mistral-7B-Instruct-v0.3, Gemma2-9B, Llama-3.1-70B-Instruct, Qwen2-72B-Instruct, Llama-3.1-405B-Instruct, über together.ai (Kosten aller Versuche ca. 15 $, Fn. 5). Greedy decoding „to avoid variability over different runs“; ein Lauf pro Konfiguration. Kein Abfragedatum, keine Angabe zur Quantisierung beim Dienst.
- **Feinjustierung** (S. 5, Tab. 4): Llama-3.1-8B-Instruct, volle Parameter, 4 × A100 64 GB, maximale Sequenzlänge 512, Batchgröße 512, Lernrate 4e-5, ein Epoch, AdamW. Trainingsmengen 10K und 20K pro Sprache und Aufgabe oder alles (S. 6).
- **Maße:** RougeL und BERTScore für Definitionen, Genauigkeit für Multiple Choice (S. 5); für den XL-WSD-Vergleich F1 mit dem offiziellen Werkzeug (S. 8).
- **Antwortauswertung für XL-WSD** (S. 7 bis 8): Wahl per regulärem Ausdruck aus der Antwort ziehen, daraus die Glosse, aus der Glosse die BabelNet-Sense-ID suchen; für monoseme Wörter (nicht im Multiple-Choice-Datensatz) wird der einzige Sense gesetzt. Wie viele Antworten der Regex nicht erfasst und wie sie gewertet wurden, steht nicht im Text.
- **Baselines:** überwachte Systeme aus der Literatur (XLMR-Large/-Base, BERT-L, BERT-M, LS-BERT, QInterf; S. 8, Tab. 10). **Keine MFS-Baseline** und kein Zufallsniveau.
- **Keine Aufschlüsselung** nach Wortart, Polysemiegrad oder Häufigkeit; nur nach Sprache.

## Wörtliche Stellen

> „In particular, from Li, we remove all the annotated meanings and obtain the set Ci. Then, we randomly add to Ci one of the correct meanings; in this way, Ci contains only one correct sense.“ (S. 3)

> „All models are tested using a greedy search approach as an inference strategy to avoid variability over different runs.“ (S. 5)

> „Since the multiple-choice task is also performed as a generative problem, we need to transform the answer provided by the LLM into the BabelNet sense id used by the XL-WSD scoring tool. This process is not trivial […]“ (S. 7)

## Bezug zur Dissertation

- **Aufgabenformat (Protokoll 5):** Die Multiple-Choice-Aufgabe ist strukturell das Format der Pipeline (nummerierte Liste, Antwort nur die Nummer). Unterschied wie bei Yae et al.: Glossen statt Begriffsgruppen. Bemerkenswert ist der Umgang mit fehlenden Glossen: Statt die Lücke offen zu lassen, werden englische Glossen maschinell übersetzt (S. 4), und das senkt die Werte (S. 6). Für die Dissertation stützt das die Entscheidung in Protokoll 5, nur von Menschen erstellte Begriffsnamen zu zeigen und keine maschinell erzeugten Erläuterungen.
- **`MEHRERE` (Protokoll 6, 9.2, A14):** Basile et al. lösen mehrere Gold-Senses, indem sie alle bis auf einen aus der Optionsliste **entfernen** (S. 3, Fn. 1). Das ist Henrichs Option „alle bis auf einen Sense entfernen“ (vgl. `goldstandard/LITERATUR-IAA.md`, Zeile Henrich 2015) und verändert das Menü je nach Gold, also nicht das, was ein Mensch sähe. Die Dissertation zeigt dagegen das volle Menü und wertet nachträglich (Primärregel plus zwei Sensitivitätsauswertungen). Der Unterschied sollte beim Vergleich der Zahlen genannt werden.
- **Freeze 2 (Protokoll 4.10):** Greedy decoding als Begründung für einen einzigen Lauf (S. 5) ist ein Präzedenzfall für Temperatur 0 und einen Lauf pro Item; dass ein Clouddienst auch bei greedy decoding nicht garantiert dieselbe Ausgabe liefert, diskutieren die Autor:innen nicht. Modellversionen sind genauer angegeben als bei Yae et al., ein Abfragedatum fehlt auch hier.
- **Unparsbare Antworten (9.2):** Die Abbildung Antwort → Nummer → Glosse → Sense-ID per Regex und Glossensuche (S. 7 bis 8) ist ein zweistufiges Parsing mit eigener Fehlerquelle (gleichlautende Glossen). Die Pipeline der Dissertation sollte die Sense-ID direkt aus der Optionsnummer ableiten und den Anteil nicht auswertbarer Antworten berichten; Basile et al. berichten ihn nicht.
- **Monoseme Wörter und Vergleichbarkeit der Zahlen:** Für den XL-WSD-Vergleich werden monoseme Wörter mit ihrem einzigen Sense als richtig gezählt (S. 8, Punkt 4). Die F1-Werte in Tab. 10 liegen daher über den Genauigkeiten der Multiple-Choice-Aufgabe (Llama-3.1-405B EN 0,8040 gegenüber 0,7532 in Tab. 6); das ist meine Lesart, die Autor:innen erklären den Unterschied nicht. Die Dissertation rechnet nur über polyseme Lemmata (Protokoll 3; `knowledge/data.md` B2); Zahlen aus XL-WSD-F1 sind deshalb nicht direkt vergleichbar.
- **MFS (Protokoll 1, 9.2):** Keine MFS-Baseline. Wie bei Yae et al. lässt sich nicht sagen, ob Zero-shot-LLMs MFS schlagen; das stützt den gepaarten Vergleich mit MFS (A4, A11).
- **Ressourcenarme Sprachen:** Zero-shot fällt in Sprachen mit weniger Daten (IT, ES) deutlich ab (S. 8). Das passt zur Erwartung, dass Mittelhochdeutsch schwierig ist, misst sie aber nicht.

## Grenzen und Einwände

- **Text gegen Tabelle:** Der Text sagt, das feinjustierte Modell sei „best for all languages“ und übertreffe „always“ die Baselines (S. 8); in Tab. 10 liegt für Spanisch QInterf mit 0,7900 vor Llama-3.1-8B-FT mit 0,7769, und die Tabelle hebt QInterf dort selbst fett hervor (am Seitenbild geprüft). Für Englisch ist QInterf auf einem anderen Ausschnitt des Datensatzes bewertet (Fußnote zu Tab. 10).
- **Genauigkeit und F1 vermischt:** Die Schlussfolgerung nennt 0,8472 und 0,8652 „accuracy“ (S. 9), Tab. 10 berichtet F1 (S. 8).
- **Keine MFS-Baseline**, keine Intervalle, keine Signifikanztests; die deutschen und französischen Testmengen sind klein (230 bzw. 442 Multiple-Choice-Items ohne Übersetzung, S. 11).
- **Keine Fehleranalyse**, keine Aufschlüsselung nach Wortart oder Polysemiegrad.
- **Kontamination** nicht diskutiert, obwohl XL-WSD und BabelNet-Glossen öffentlich sind; die Autor:innen nennen nur allgemein ungeprüfte Vortrainingsdaten (S. 9, Ethik).
- **Unparsbare Antworten** nicht beziffert.
- **Begrenzungen laut Autor:innen** (S. 9): nur fünf ressourcenstarke Sprachen, kein Few-shot, kein Vergleich mehrerer Prompts, nur ein feinjustiertes Modell, keine geschlossenen Modelle.
- **Preprint:** nicht begutachtet (Stand 2026-10-28).
- **Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar:** Das Format ist übertragbar, die Zahlen nicht; Glossen sind informativer als Begriffsnamen, und die Feinjustierung setzt Trainingsmengen voraus, die es für Mittelhochdeutsch nicht gibt.

## Weiterführend

- Pasini, Raganato & Navigli 2021, XL-WSD, AAAI (S. 4, 7).
- Loureiro, Rezaee, Pilehvar & Camacho-Collados 2021, „Analysis and evaluation of language models for word sense disambiguation“, *Computational Linguistics* 47(2) (S. 2).
- Kibria, Dipta & Adnan 2024, „On functional competence of LLMs for linguistic disambiguation“, CoNLL 2024, S. 143 bis 160: WSD-Genauigkeit von LLMs auf acht Datensätzen als Multiple Choice (S. 2).
- Cabiddu, Nikolaus & Fourtassi 2023, Kinder und LLMs bei WSD, Verzerrung zum dominanten Sense (S. 2).
- Zhang et al. 2024, QInterf, AAAI 38 (S. 8).
- Yae et al. 2025 (S. 2), hier ebenfalls zusammengefasst.
