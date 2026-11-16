# Ghizzota, Marongiu, Basile, Ferilli & McGillivray 2026: Linguistische Wissensgraphen für die Sense-Vorhersage, Fallstudie Latein

**Datei:** `pdf/Ghizzota-etal-2026-Knowledge-Graphs-Latin.pdf` (nur lokal; 16 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Tab. 2 am Seitenbild geprüft, DOI aufgelöst. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-13). Keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 10936 + n (PDF 1 = S. 10937, PDF 16 = S. 10952). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Ghizzota, Eleonora, Paola Marongiu, Pierpaolo Basile, Stefano Ferilli & Barbara McGillivray (2026). Linguistic Knowledge Graphs for Sense Prediction: A Case-study on Latin. In: Stelios Piperidis, Núria Bel, Henk van den Heuvel, Nancy Ide, Simon Krek & Antonio Toral (Hg.), *Proceedings of the Fifteenth Language Resources and Evaluation Conference (LREC 2026)*, Palma de Mallorca, 11. bis 16. Mai 2026. ELRA, S. 10937 bis 10952.
- **DOI/URL:** https://doi.org/10.63317/2b2274srsgkf (aufgelöst auf https://lrec.elra.info/lrec2026-main-856; Crossref: Autor:innen, S. 10937 bis 10952, Mai 2026 ✔; abgerufen 2026-11-13). ACL Anthology 2026.lrec-1.856 (BibTeX: Hg., Ort, DOI ✔). Die DOI steht nicht im PDF.
- **Titel:** im PDF „a case-study on Latin“ (klein), in Anthology und Crossref „A Case-study on Latin“.
- **Lizenz:** Kopfzeile S. 10937 nur „©ELRA Language Resources Association (ELRA), 2026“; Crossref ohne Lizenzangabe. Die ACL Anthology stellt laut Fußzeile ihrer Seiten Material ab 2016 unter CC BY 4.0. Eine paperbezogene CC-Lizenz steht nicht im PDF.
- **Art:** begutachteter Konferenzbeitrag
- **Sprache:** Englisch
- **Code und Daten:** github.com/Midorilly/latin-sense-prediction (S. 10949; nicht aufgerufen).
- **Nicht verwechseln** mit Ghizzota, Basile, Siciliani & Semeraro 2025 (CLiC-it, *The Meaning of Beatus*), dessen Zero-shot-Ergebnisse hier die Baseline sind.

## Worum es geht

Die Arbeit prüft, ob Zusatzwissen aus einem linguistischen Wissensgraphen (LKG) LLMs bei der lateinischen Sense-Vorhersage hilft (S. 10937 bis 10938). Der Graph verbindet die sense-annotierten SemEval-2020-Belege mit Latin WordNet, Wikidata und Autorenmetadaten (S. 10939 bis 10940). Per Graph-RAG werden zwei Arten von Kontext in den Prompt gelegt: Autor, Werk, Zeit und Beruf der Autor:innen der fünf ähnlichsten Belege, oder Synset, Hyperonym und je ein positives und negatives Beispiel des Zielsense; die Aufgabe ist binär (passt dieser Sense, ja/nein) (S. 10940 bis 10942). Nur LLaMA-3.3-70B gewinnt durch den Graphen leicht (F1 0,64 auf 0,65/0,66), GPT-4o-mini und LLaMA-3.1-8B verlieren deutlich; GPT-4o-mini bleibt insgesamt am besten (S. 10942 bis 10943). Konkrete und im Christentum gewandelte Wörter sind leichter als abstrakte und stabile (S. 10944 bis 10945).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| WSD mit LLMs wird in der Einleitung mit Yae et al. und Basile et al. 2025 belegt; es fehle systematische Evidenz, ob graphbasierte Metadaten der Sense-Vorhersage im historischen, ressourcenarmen Fall helfen. | S. 10937, Abschnitt 1 | Problemstellung, referiert |
| Historische Sprachen haben besondere Probleme: wenige sense-annotierte Korpora, reiche Morphologie, orthografische Variation, diachroner Bedeutungswandel. | S. 10938, Abschnitt 2.1 | Problemstellung |
| Daten: SemEval-Datensatz Latein (McGillivray et al. 2022) aus LatinISE; 39 Lemmata (17 gewandelt, 22 Kontrolle), je 60 Sätze, je zur Hälfte vor und nach Christus; Annotation nach einer Variante von DURel mit Vierstufenskala zu Logeion-Definitionen. | S. 10941, Abschnitt 4.1 | referiert |
| LKG: Labelled Property Graph in Neo4j (GraphBRAIN), Schema nach lemon und WordNet; Senses manuell mit WordNet-Synsets verknüpft, Autor:innen mit Wikidata; nach Bereinigung (Autorennamen, gleichnamige Werke) 4.276 Knoten und 31.108 Kanten. | S. 10939 bis 10940, Abschnitt 4.2 | eigene Aufbereitung, teils referiert (McGillivray et al. 2023) |
| Aufgabe: binäre Vorhersage der Eigenschaft `binary` an der Kante zwischen Beleg und Sense; DURel-Stufe ab 3 = ja, bis 2 = nein, Stufe 0 ausgeschlossen; 8.930 Paare. | S. 10940 bis 10941, Abschnitt 5.1 | eigene Aufbereitung (wie Ghizzota et al. 2025) |
| Testmenge 30 %: 2.675 Paare, 956 ja, 1.719 nein (35,73 % ja). Für die Testpaare wird `binary` im Graphen auf None gesetzt. | S. 10942, Abschnitt 6 | eigene Aufbereitung |
| Autorenmetadaten: fünf ähnlichste Sätze per Kosinus auf Einbettungen (OpenAI text-embedding-3-small, 1.536 Dimensionen) mit Werk, Zeit, Autor:in und Beruf. | S. 10941, Abschnitt 5.2 | eigene Methode |
| Linguistische Metadaten: Logeion-Sense über `same_as` zu Latin WordNet, dazu Hyperonym und je ein positives und ein negatives Beispiel; Hyponyme bewusst weggelassen. Senses ohne WordNet-Entsprechung (römische und christliche Bedeutungen, z. B. bei *virtus*, *consul*, *sacramentum*, *templum*) und 126 zugehörige Belege ausgeschlossen. | S. 10941 bis 10942, Abschnitt 5.3; S. 10950, Anhang A.2.2 | eigene Methode |
| Ohne Graph: GPT-4o-mini F1 0,77/0,76, LLaMA-3.3-70B 0,64, LLaMA-3.1-8B 0,53/0,52 (zwei Werte, weil die linguistische Bedingung auf 2.549 statt 2.675 Paaren läuft). | S. 10942, Tab. 2 | eigenes Ergebnis (Baseline aus Ghizzota et al. 2025) |
| Mit Graph: GPT-4o-mini fällt auf 0,68 (Autor), 0,68 (linguistisch), 0,61 (beides); LLaMA-3.1-8B auf 0,42, 0,31, 0,21; LLaMA-3.3-70B steigt auf 0,65, 0,66, 0,64. Signifikant (Wilcoxon, p < 0,05) ist nur der Zuwachs von LLaMA-3.3-70B mit linguistischen Metadaten (p = 0,0214). | S. 10942 bis 10943, Tab. 2; S. 10951, Tab. 4 | eigenes Ergebnis |
| Als Grund für die Verschlechterung vermuten die Autor:innen die Länge der Prompts (mittlere Promptlänge 4.104,95 bis 6.731,48, Einheit nicht angegeben). | S. 10943; S. 10949, Tab. 3 | eigene Deutung |
| Kein Zusammenhang zwischen Polysemiegrad und Leistung, aber zu wenige Wörter mit 5 bis 7 Senses für eine Aussage. | S. 10943 bis 10944, Abschnitt 6.1 | eigenes Ergebnis, mit Vorbehalt |
| Alle Modelle sind bei gewandelten Wörtern besser als bei stabilen und bei konkreten Nomen besser als bei abstrakten. | S. 10944 bis 10945; Abb. 6 | eigenes Ergebnis |
| Fazit: Unter offenen Modellen eher große; Graph-RAG muss so gebaut sein, dass Zusatzinformation nicht irreführt; semantische Merkmale (konkret/abstrakt, gewandelt/stabil) erklären die Schwierigkeit besser als Polysemie oder Wortart. | S. 10945, Abschnitt 7 | eigene Schlussfolgerung |

## Daten, Methode, Zahlen

- **Tab. 2 (S. 10943), am Seitenbild geprüft.** „LLM“ = ohne Graph; die erste LLM-Zeile gilt für 2.675 Testpaare (Autorenbedingung), die zweite für 2.549 (linguistische und kombinierte Bedingung).

| Modell | Bedingung | Precision | Recall | F1 |
|---|---|---|---|---|
| GPT-4o-mini | LLM | 0,7974 | 0,7634 | 0,7682 |
| | + Autor | 0,7373 | 0,6755 | 0,6814 |
| | LLM | 0,7906 | 0,7544 | 0,7592 |
| | + linguistisch | 0,7145 | 0,6775 | 0,6838 |
| | + beides | 0,7339 | 0,6163 | 0,6136 |
| LLaMA-3.3-70B | LLM | 0,7030 | 0,6301 | 0,6355 |
| | + Autor | 0,7427 | 0,6505 | 0,6535 |
| | LLM | 0,7009 | 0,6312 | 0,6361 |
| | + linguistisch | 0,7493 | 0,6559 | 0,6579 |
| | + beides | 0,7496 | 0,6414 | 0,6411 |
| LLaMA-3.1-8B | LLM | 0,5947 | 0,5271 | 0,5336 |
| | + Autor | 0,6061 | 0,4536 | 0,4170 |
| | LLM | 0,5877 | 0,5194 | 0,5242 |
| | + linguistisch | 0,6101 | 0,4072 | 0,3130 |
| | + beides | 0,7345 | 0,3707 | 0,2114 |

- **Tab. 4 (S. 10951), Wilcoxon-Test für LLaMA-3.3-70B:** Autor p = 0,0612; linguistisch p = 0,0214; beides p = 0,1178.
- **Lemmata (S. 10952, Tab. 5):** 7 Adjektive, 28 Nomen, 4 Verben; nach Polysemie 7 Lemmata mit 2 Senses, 10 mit 3, 12 mit 4, 4 mit 5, 4 mit 6, 2 mit 7; 16 abstrakte, 10 konkrete, 2 beides; 17 gewandelt, 22 stabil.
- **Prompt (S. 10941, 10949 bis 10951):** System-Prompt „You are a linguist proficient in Latin […]“; Aufgabe: Zielwort, Satz mit `[TARGET]`, **eine** Glosse, Antwort „yes“ oder „no“. Das Modell sieht nie das ganze Sense-Menü.
- **Annotation und Übereinstimmung:** referiert; das Paper nennt weder Zahl der Annotator:innen noch eine Übereinstimmung. Ghizzota et al. 2025 (PDF-S. 4) berichten für denselben Datensatz eine Annotator:in pro Zielwort und Spearman 0,69 an *virtus*.
- **Unstimmigkeiten:** Abstract nennt F1 „ranging from 0.53 to 0.77“ (S. 10937), Tab. 2 enthält Werte bis hinunter zu 0,2114. Der Text nennt für LLaMA-3.3-70B ohne Graph 0,63 (S. 10942 bis 10943), Tab. 2 und Abb. 5 0,6355 bzw. 0,64. „Accuracy“ steigt laut Text in allen Bedingungen (S. 10942); berichtet wird nur F1. Die Lemmazahl weicht von Ghizzota et al. 2025 (40; 23 stabil, 17 gewandelt) und Ghinassi et al. 2024 (40; je 20) ab.

## Wörtliche Stellen

> „Analysis by word type reveals that concrete and semantically shifting words are more easily disambiguated than abstract and semantically stable words.“ (S. 10937, Abstract)

> „In general, it looks like providing author and linguistic metadata combined leads to worse performances for all models, compared to providing linguistic and author information separately.“ (S. 10943)

## Bezug zur Dissertation

- **`goldstandard/LITERATUR-IAA.md`, „LLMs bei historischen Sprachen“:** Dort wird dieses Paper (○) als Beleg dafür genannt, dass LLMs bei historischen Sprachen mit F1 gegen ein Gold ohne berichtete IAA gemessen werden. Am Original bestätigt: Precision, Recall, F1 gegen den SemEval-Datensatz, keine Angabe zu Annotator:innen oder Übereinstimmung (S. 10941 bis 10943). Präzisieren: Das Gold hat laut Ghizzota et al. 2025 eine Annotator:in pro Wort, IAA nur an einem Wort; die Aufgabe ist binär je Sense, keine Sense-Wahl. Prüfstatus kann ✔ werden (Volltext gelesen); das entscheidet Julia.
- **PROTOKOLL §1, §9.2 (Vergleichbarkeit):** Wie bei Ghizzota et al. 2025 misst F1 hier eine Ja/Nein-Entscheidung je Paar, nicht die Wahl eines Sense aus dem Menü; keine MFS-Baseline. Werte wie 0,77 sind mit der Genauigkeit im Protokoll nicht vergleichbar.
- **PROTOKOLL §5 (was das LLM sieht) und Freeze 2 (§4.10):** Zusatzkontext im Prompt (ähnliche Belege, Hyperonym, Beispiele) schadet hier zwei von drei Modellen, teils stark (LLaMA-3.1-8B von 0,52 auf 0,21), und hilft dem dritten nur knapp (S. 10942 bis 10943). Das stützt die Vorsicht des Protokolls, den Kartenaufbau knapp zu halten und gleiche Karten für Menschen und LLM zu zeigen (vgl. `knowledge/data.md` B13 zu Glossen). Für die Begriffsnamen samt Pfad zum Oberbegriff (§5 Punkt 1) ist der Befund ein Warnsignal: Hyperonyme halfen nur dem größten offenen Modell; ob das auch für Oberbegriffe des MHDBDB-Begriffssystems gilt, ist am Pilot-Pool zu prüfen.
- **PROTOKOLL §9.1 Punkt 6 und §4.3 (Aufschlüsselung, Polysemie):** Die Autor:innen finden keinen Zusammenhang mit dem Polysemiegrad, aber mit konkret/abstrakt (S. 10943 bis 10945). Das ist auf 39 Lemmata gestützt und daher schwach; es legt nahe, in der Auswertung neben Polysemie und Wortart auch die Domäne zu betrachten (im Protokoll schon vorgesehen).
- **Inventarlücke (`KEINE_PASST`, §6):** Senses für römische und christliche Institutionen fehlen in WordNet und mussten mitsamt 126 Belegen weg (S. 10942, 10950). Das ist derselbe Befund wie bei Ghinassi et al. 2024 und ein Argument gegen gegenwartssprachliche Inventare für historische Texte; das MHDBDB-Begriffssystem ist für das Mittelhochdeutsche gebaut.
- **Linked Data (`knowledge/data.md`, Abschnitt 1):** Der LKG koppelt Sense, Beleg, WordNet und Autorenmetadaten in einem Graphen, wie die MHDBDB Sense-Zeiger auf `concepts.xml` und Header-Kategorien nutzt. Der Nutzen der Graphdaten für LLM-WSD ist nach diesem Paper gering und modellabhängig.

## Grenzen und Einwände

- Binäre Aufgabe je Sense; ob ein Modell pro Beleg genau einen passenden Sense findet, wird nicht ausgewertet.
- Kleine, nicht zufällig gezogene Lemmamenge (39), nach Bedeutungswandel durch das Christentum gewählt.
- Gold ohne berichtete Übereinstimmung; die Baseline ist aus einem eigenen früheren Paper übernommen.
- Nur ein Lauf je Bedingung; Signifikanz nur für LLaMA-3.3-70B getestet, und dort nur einer von drei Zuwächsen signifikant.
- Ähnliche Belege für den Autorenkontext stammen per Einbettung aus dem Graphen; ob darunter Belege derselben Lemmata mit bekannter Antwort sind und ob das leckt, wird nicht diskutiert. Bei den linguistischen Metadaten sind positive und negative Beispiele ausdrücklich gelabelt (S. 10950); ob sie aus der Testmenge stammen können, sagt das Paper nicht [am PDF zu prüfen, ggf. im Code].
- Unstimmigkeiten zwischen Abstract, Text und Tabelle (siehe oben).

## Weiterführend

- McGillivray et al. 2022, *Journal of Latin Linguistics* 21(1), S. 47 bis 105 (S. 10941, 10948): Annotationsrahmen des Datensatzes.
- McGillivray et al. 2023, Graph databases for diachronic language data modelling, LDK 2023, S. 86 bis 96 (S. 10937, 10948): Herkunft des LKG.
- Basile, Cassotti, Ferilli & McGillivray 2022, zeitsensitives Modell linguistischen Wissens für Graphdatenbanken, AIxIA-Workshop (S. 10939, 10947).
- Ghizzota, Basile, d’Amato & Fanizzi 2025, GWC 2025 (S. 10939, 10948).
- Farina, Ballatore & McGillivray 2025, LLMs für lateinische Bewegungsverben, CLiC-it 2025 (S. 10945, 10948): Hinweis, dass GPT-4o-mini mehr Latein gesehen habe.
- Liu et al. 2023, *Lost in the middle* (S. 10939, 10947): war schon zur Beschaffung vorgeschlagen (`goldstandard/VORSCHLAEGE-2026-10.md`).
- Ghizzota et al. 2025 (liegt vor, `zusammenfassungen/Ghizzota-etal-2025-Meaning-of-Beatus.md`); Ghinassi et al. 2024 (liegt vor).

## Julias Notizen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF und hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
