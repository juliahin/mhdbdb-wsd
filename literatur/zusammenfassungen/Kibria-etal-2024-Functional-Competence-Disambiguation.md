# Kibria, Dipta & Adnan 2024: Funktionale Kompetenz von LLMs bei der Disambiguierung

**Datei:** `pdf/Kibria-etal-2024-Functional-Competence-Disambiguation.pdf` (nur lokal; 18 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Abb. 1 (S. 144) und Tab. 7 und 8 (S. 151) am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-13), also die Verlagsfassung. Keine Markierungen. Titel am PDF geprüft: „On Functional Competence of LLMs for Linguistic Disambiguation“ (S. 143).

Seitenzählung: PDF-Seite n = gedruckte S. 142 + n (PDF 1 = S. 143, PDF 18 = S. 160). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Kibria, Raihan, Sheikh Intiser Uddin Dipta & Muhammad Abdullah Adnan (2024). On Functional Competence of LLMs for Linguistic Disambiguation. In: Libby Barak & Malihe Alikhani (Hg.), *Proceedings of the 28th Conference on Computational Natural Language Learning*. Miami: Association for Computational Linguistics, S. 143 bis 160.
- **DOI/URL:** https://doi.org/10.18653/v1/2024.conll-1.12 (aufgelöst am 2026-11-13, leitet auf https://aclanthology.org/2024.conll-1.12 weiter); Herausgeber:innen, Ort, Monat November und Seiten aus dem BibTeX der Anthology; Kopfzeile S. 143: „pages 143–160, November 15-16, 2024“.
- **Lizenz:** CC BY 4.0 (ACL Anthology, Material ab 2016, laut Fußzeile der Anthology, abgerufen 2026-11-13).
- **Art:** Konferenzbeitrag
- **Sprache:** Englisch
- **Code:** laut Fn. 1 (S. 144) verfügbar unter einem Link „Functional Competence of LLMs“; die URL steht nicht in der Textebene, nicht aufgerufen.

## Worum es geht

Die Autoren prüfen vier LLMs (ChatGPT-3.5, Mistral 7B, Llama 70B, Gemini Pro) auf etablierten WSD-Datensätzen, jeweils als Auswahl aus vorgegebenen Sense-Definitionen (S. 143 bis 144, Abb. 1). Die Genauigkeit liegt auf den fünf Datensätzen des Unified Evaluation Framework 9,1 bis 28,3 Punkte unter dem jeweils besten überwachten System (eigene Rechnung aus Tab. 7) (S. 151, Tab. 7). An Fehlschlägen auf FEWS entwickeln sie eine Taxonomie: Viele Fehler beruhen nicht auf fehlendem Sprachwissen, sondern auf fehlendem Welt-, Kultur- oder historischem Wissen und darauf, dieses Wissen zusammenzuführen („funktionale Kompetenz“, S. 145, 151). Die Methode ist knapp beschrieben: keine Stichprobengrößen, keine Temperatur, Antworten wurden „sanitized“ (S. 149).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Unterscheidung formaler (Regularitäten, Syntax, Morphologie) und funktionaler Sprachkompetenz (Absicht erkennen, Weltwissen nutzen); LLMs seien formal stark, funktional nicht auf menschlichem Niveau. | S. 143, 145, Abschn. 1 bis 3 | referiert (Mahowald et al. 2024) |
| Beispiel *person* im Sinn „physischer Körper“ statt „Mensch“: nur mit historischem Sprachgebrauch erschließbar. | S. 143 bis 144; Tab. 1 (S. 146) | eigenes Beispiel |
| **Fehlertaxonomie** (Tab. 1 und 9): älteres Englisch, Kultur (aktuelle Kultur, soziale Normen), Metapher, grammatisch-linguistisch (Verb-Objekt, Selektionspräferenz, Adjektiv-Nomen), Allgemeinwissen (Geografie, Handel, Fachwissen), Satire, Figuratives, religiöses Schrifttum, Weltwissen. Nach eigener Angabe bisher nicht dokumentiert. | S. 145, Abschn. 4; S. 146, Tab. 1; S. 156, Tab. 9 | eigenes Ergebnis (qualitativ, ohne Häufigkeiten) |
| Sechs Probleme der WSD-Evaluation: Domänen-Bias, MFS gegen seltene Senses, Kontext als Hinweis, „one sense per discourse“, grobe gegen feine Senses, Homonymie gegen Polysemie. | S. 148 bis 149, Abschn. 6.1 | referiert (Escudero et al. 2000; Gale et al. 1992; Ide & Wilks 2006) |
| Grobe gegen feine Senses: WordNet unterscheidet so fein, dass Annotator:innen oft uneinig sind; eine angemessene Evaluation müsse gröbere Inventare einbeziehen. | S. 149, Abschn. 6.1 Punkt 5 | Einschätzung, gestützt auf Ide & Wilks 2006 |
| Homonyme würden im Allgemeinen genauer disambiguiert als polyseme Wörter; Datensätze sollten beide enthalten. | S. 149, Abschn. 6.1 Punkt 6 | Behauptung ohne Beleg im Text |
| Auswahlkriterien für Datensätze: viel zitiert, Kontext und Zielwort, Gold-Schlüssel, Variation, von Menschen validiert, Homonyme und Polyseme gemischt. Eurosense ausgeschlossen (in Stichproben nur 67,7 % Übereinstimmung), NUS ausgeschlossen (nur Präpositionen). | S. 149, Abschn. 6.2; S. 150, Abschn. 7.1 | eigene Kriterien; Werte referiert |
| **Prompt:** Satz, Zielwort und Liste der Sense-Definitionen, Frage „Which of the following senses is correct“; für drei Modelle „Do not provide explanations“, teils „Just output the choice“; Gemini ohne diese Anweisung. Im Anhang römische Nummern I) bis III), in Abb. 1 Buchstaben A) bis E). | S. 144, Abb. 1; S. 157 bis 160, Tab. 10 bis 13 | eigenes Material |
| **Antworten:** Modelle wurden über „expert“, „non-verbose“ und „safe“ mode eingestellt; Antworten enthielten teils „spurious content“ und wurden bereinigt; „It took several iterations to arrive at a proper mechanism to capture the response.“ Wie viele Antworten betroffen waren und wie ungültige gezählt wurden, steht nicht im Werk. | S. 149, Abschn. 6.5 | eigene Angabe |
| Ergebnis: Gemini Pro auf allen Datensätzen am besten; auf FEWS liegt Gemini mit Few-shot (71,0) über dem Vergleichswert 66,4; auf WiC liegen Mistral und Gemini über dem Vergleich (58,0). | S. 151, Tab. 7 | eigenes Ergebnis |
| Die Modelle besäßen das nötige Wissen meist (mit anderen Prompts abfragbar), scheiterten aber daran, es über mehrere Dimensionen zu verbinden. | S. 151, Abschn. 8 | eigene Deutung, ohne Zahlen |
| Keine Benchmark-Absicht, weil nicht alle Modelle offen sind und sich die Technik ständig ändert. | S. 151, Abschn. 8 | eigene Einschätzung |

## Daten, Methode, Zahlen

**Modelle (S. 149 bis 150, 157 bis 160):** ChatGPT-3.5 (Tab. 10: GPT-3.5-Turbo-0125), Mistral 7B, Llama 70B (Tab. 12: Llama-2-70b-chat, laut Tab. 8 über replicate.com), Gemini Pro. Temperatur, weitere Sampling-Parameter und Abfragedatum werden nicht genannt.

**Tab. 7 (S. 151, Seitenbild), Genauigkeit in %:**

| Datensatz | OpenAI | Mistral | Llama | Gemini | Vergleich | IAA |
|---|---|---|---|---|---|---|
| Senseval-2 | 65,7 | 65,0 | 61,0 | 71,1 | 82,3 | – |
| Senseval-3 | 61,5 | 58,8 | 54,5 | 70,0 | 79,9 | 72,5 |
| SemEval-2007 | 58,4 | 55,7 | 49,1 | 65,4 | 77,4 | „72,86“ (Verben und Nomen) |
| SemEval-2013 | 70,1 | 65,9 | 66,5 | 74,1 | 83,2 | – |
| SemEval-2015 | 67,3 | 64,1 | 63,0 | 72,9 | 85,2 | 68 |
| WiC | 59,4 | 61,6 | 55,1 | 65,8 | 58,0 | 80 |
| CoarseWSD-20 | 84,1 | 61,6 | 33,8 | 93,9 | 95,0 | – |
| FEWS Few-shot | 63,0 | 63,7 | 60,7 | 71,0 | 66,4 | 80,2 |
| FEWS Zero-shot | 59,0 | 58,7 | 56,7 | 65,0 | – | – |

Vergleichswerte: Zeilen 1 bis 5 ConSeC (Barba et al. 2021b), WiC Pilehvar & Camacho-Collados 2018, CoarseWSD-20 Loureiro et al. 2021, FEWS Blevins et al. 2021 (Tabellenlegende). Der IAA-Wert „72,86*“ steht laut Legende für Verben und Nomen; gemeint sind vermutlich 72 und 86 [am PDF zu prüfen; die Tabelle trennt die Zahlen nicht].

**Fehlende Angaben:** Wie viele Items je Datensatz befragt wurden, wird nicht gesagt; es gibt keine Intervalle und keine Tests. „We test nine datasets“ (S. 151) passt nicht zu den acht Datensätzen in Tab. 7 (neun Zeilen nur mit FEWS doppelt).

**Weitere Unstimmigkeiten:** Tab. 3 (S. 147) nennt für SemEval-13 1.664 Annotationen, Raganato et al. 2017 (Tab. 1) 1.644. Die Diskussion nennt die Genauigkeit „comparable to the state-of-the-art models“ (S. 151), der Abstract dagegen „much less than that of well-performing existing models“ (S. 143); Tab. 7 stützt den Abstract. „Context As a Clue“ soll untersucht werden (S. 148), eine solche Auswertung kommt im Werk nicht vor.

## Wörtliche Stellen

> „The responses sometimes were found to contain some spurious content. We sanitized the output to collect the response. It took several iterations to arrive at a proper mechanism to capture the response.“ (S. 149)

> „[…] many failure cases are related to a lack of world knowledge and the reasoning to amalgamate this knowledge rather than the lack of linguistic knowledge.“ (S. 143)

> „Therefore, a proper evaluation of WSD must factor in other sense inventories that are less fine-grained […]“ (S. 149)

## Bezug zur Dissertation

- **Protokoll §9.2, ungültige Antworten (A18, A29):** Das Werk ist ein Beleg für das Problem, das A18 regelt: Antworten mussten in mehreren Iterationen „bereinigt“ werden, ohne dass Zahl oder Regel berichtet werden (S. 149). Meconi et al. 2025 (S. 33898) kritisieren genau das. Für die Dissertation stützt es, ungültige Antworten als eigene Kategorie zu zählen und die Bereinigungsregel vor dem Lauf festzulegen, statt sie nach Sicht der Ausgaben anzupassen.
- **A26 (vollständige Konfiguration):** Nur für zwei Modelle wird eine Version genannt, Temperatur und Itemzahlen fehlen (S. 149 bis 160). Die „Modes“ (expert, non-verbose, safe) sind keine dokumentierten API-Parameter und nicht erklärt. Ein weiteres Beispiel für die Lücke, die A26 schließen soll.
- **Prompt- und Antwortformat (Freeze 2, A23, A27):** Die Aufgabe ist dieselbe wie im Protokoll: Satz plus nummerierte Sense-Liste, Antwort mit der Nummer (S. 157). Unterschiede: Die Liste zeigt Definitionen, die MHDBDB-Karten Begriffsgruppen ohne Definition (`knowledge/data.md`, Abschnitt 1); die Reihenfolge der Optionen wird nicht gemischt und nicht protokolliert; `MEHRERE` oder eine Ausweichantwort sind nicht vorgesehen. Dass ein Modell (Gemini) einen anderen Prompt bekam als die übrigen (S. 160), verletzt den Grundsatz gleicher Darbietung (A27) schon zwischen Modellen.
- **Historische Sprache:** Die Taxonomie ist für Mittelhochdeutsch einschlägig: Die Kategorie „Old English“ (Gebrauch des 14. Jahrhunderts, S. 146) und religiöses Schrifttum (S. 156) sind Fälle, in denen die gegenwartssprachliche Lesart naheliegt und falsch ist. Das spricht dafür, im Ursachencode der Adjudikation (Protokoll §7, Schritt 6) und in der LLM-Fehleranalyse eine Kategorie „gegenwartssprachliche Lesart“ mitzuführen. Das Werk liefert dafür aber nur Einzelbeispiele, keine Häufigkeiten.
- **Granularität:** Das Werk fordert gröbere Inventare in der Evaluation (S. 149) und zeigt die höchsten Werte auf dem groben CoarseWSD-20 (Gemini 93,9, Tab. 7). Weil die Datensätze sich in vielem unterscheiden, belegt das den Granularitätseffekt nicht sauber; als ergänzender Hinweis zu §9.1, Punkt 7 brauchbar.
- **LLM gegen menschliche Übereinstimmung (§9.2, Alternative Annotator Test):** Tab. 7 stellt LLM-Werte neben die IAA der Datensätze (S. 151): Gemini erreicht auf Senseval-3 fast die IAA (70,0 gegen 72,5) und übertrifft sie auf SemEval-2015 (72,9 gegen 68), bleibt auf WiC und FEWS deutlich darunter. Ein informeller Vorläufer des Vergleichs, den das Protokoll mit eigenen Annotator:innen sauber anlegt; die IAA-Werte stammen aus anderen Annotationen und Maßen.
- **Kontamination (Protokoll §10):** Nicht untersucht. Die Datensätze sind seit Jahren öffentlich (Senseval ab 2001, S. 147); Kim et al. 2022 zur Überexposition werden nur erwähnt (S. 148). Hohe Werte auf alten öffentlichen Datensätzen lassen sich daher nicht von Kontamination trennen; das stützt die Ablage der Labels nach Protokoll §10.

## Grenzen und Einwände

- Keine Itemzahlen, keine Streuung, keine Tests; die Genauigkeiten sind nicht nachprüfbar.
- Bereinigung der Antworten nicht dokumentiert; unklar, wie ungültige Antworten zählen.
- Die Fehlertaxonomie ist qualitativ, ohne Angabe, wie viele Fälle untersucht und wie sie kategorisiert wurden (eine Person, mehrere?).
- Widersprüche zwischen Abstract und Diskussion sowie in den Datensatzzahlen (siehe oben).
- Unterschiedliche Prompts je Modell und Datensatz (Tab. 10 bis 13).
- Englisch; historische Belege nur als Einzelfälle aus FEWS.

## Weiterführend

- Mahowald et al. 2024, Dissociating language and thought in large language models, *Trends in Cognitive Sciences* (S. 143, 145, 153): Begriffspaar formale/funktionale Kompetenz.
- Ide & Wilks 2006, Making sense about sense, in Agirre & Edmonds (Hg.) (S. 149, 152): Granularität; Band schon in `references.txt` (`agirreEdmonds2006`).
- Loureiro et al. 2021, CoarseWSD-20, *Computational Linguistics* 47(2) (S. 150, 153).
- Pilehvar & Camacho-Collados 2018, WiC (S. 150, 153): Paarvergleich statt Inventar, nahe an Weg C in A31.
- Barba, Procopio & Navigli 2021b, ConSeC, EMNLP (S. 149, 152).
- Kim, Linzen & Smolensky 2022, Uncontrolled lexical exposure (S. 148, 153): Kontamination.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF und hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
