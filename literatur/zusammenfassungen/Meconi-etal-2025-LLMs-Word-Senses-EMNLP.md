# Meconi et al. 2025: Do Large Language Models Understand Word Senses?

**Datei:** `pdf/Meconi-etal-2025-LLMs-Word-Senses-EMNLP.pdf` (Verlagsfassung, ACL Anthology, nur lokal); daneben `pdf/Meconi-etal-2025-LLMs-Word-Senses.pdf` (arXiv v1)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, Verlagsfassung vollständig gelesen (20 Seiten, mit Anhängen), Tabellen 3 bis 7 und 21 am Seitenbild geprüft; beide Fassungen wortweise an der Textebene verglichen; Bibliografie an der ACL Anthology und arXiv geprüft. In beiden PDFs keine Markierungen von Julia.

**Seitenzählung:** Die Verlagsfassung trägt die Proceedings-Seiten 33897 bis 33916; gedruckte Seite = PDF-Seite + 33896. Zitiert wird die gedruckte Seite. Die arXiv-Fassung hat dieselben 20 Seiten im selben Umbruch, aber keine Seitenzahlen; PDF-Seite n der arXiv-Fassung entspricht S. 33896 + n.

**Unterschiede zur arXiv-Fassung** (Textebene beider PDFs wortweise verglichen): Der Text ist bis auf eine Zahl identisch. In Tab. 9 (S. 33904) steht für GPT-4o auf WikiPortal WSD in der Verlagsfassung „bad 1,00, borderline 2,00“, in arXiv v1 „bad 3,00, borderline 1,00“ (dort ergibt die Zeile 101 %; die Verlagsfassung korrigiert das). Dazu Kopfzeile, Seitenzahlen und arXiv-Kennungen in einigen Literaturangaben. Für Zitate die Verlagsfassung verwenden.

## Bibliografie

- **Vollständig:** Meconi, Domenico, Simone Stirpe, Federico Martelli, Leonardo Lavalle & Roberto Navigli, 2025. Do Large Language Models Understand Word Senses? In Christos Christodoulopoulos, Tanmoy Chakraborty, Carolyn Rose & Violet Peng (Hg.), *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025)*, 33897 bis 33916. Suzhou: Association for Computational Linguistics.
- **DOI/URL:** https://doi.org/10.18653/v1/2025.emnlp-main.1720 (löst auf https://aclanthology.org/2025.emnlp-main.1720 auf; BibTeX der Anthology am 2026-10-28 gelesen: Herausgeber:innen, Seiten, ISBN 979-8-89176-332-6). ✔ Kopfzeile S. 33897: „pages 33897–33916, November 4-9, 2025“.
- **Preprint:** arXiv:2509.13905 v1 vom 17. September 2025, Kommentar „20 pages, to be published in EMNLP2025“; einzige Version (Stand 2026-10-28).
- **Lizenz:** Verlagsfassung CC BY 4.0 (ACL Anthology: Material ab 2016 unter CC BY 4.0, Seitenfuß der Eintragsseite, am 2026-10-28 gelesen) ○, im PDF selbst kein Lizenzvermerk. arXiv-Fassung CC BY-NC-SA 4.0 laut arXiv-Seite.
- **Art:** begutachteter Konferenzbeitrag (EMNLP 2025, Main Conference)
- **Sprache:** Englisch
- **Code und Daten:** https://github.com/Babelscape/LLM-WSD (S. 33897); nicht abgerufen. Der neue Testdatensatz WikiPortal WSD wird bewusst **nicht** veröffentlicht (S. 33909).

## Worum es geht

Die Arbeit fragt, ob LLMs Wortbedeutungen verstehen, und prüft das zweifach (S. 33897 bis 33898). Erstens als klassische WSD: 16 instruktionsfeinjustierte LLMs von 1B Parametern bis GPT-4o wählen aus der Liste der WordNet-Definitionen eines Wortes die passende, auf vier englischen Testmengen, verglichen mit überwachten WSD-Systemen und einer MFS-Baseline (S. 33898 bis 33903). Zweitens ohne Inventar: Llama-3.3-70B und GPT-4o erzeugen Definitionen, freie Erklärungen und Beispielsätze, die eine Expertin oder ein Experte bewertet (S. 33903 bis 33905). Ergebnis: GPT-4o und DeepSeek-V3 liegen mit F1 82,3 bzw. 81,9 auf dem Niveau des besten überwachten Systems (ConSeC 83,0) und deutlich über MFS (65,2); auf schweren Fällen und fremden Domänen sind sie robuster als die überwachten Systeme (S. 33900 bis 33901). Gegenüber einer menschlichen Expertin bzw. einem Experten (F1 91,25) bleibt ein Abstand (S. 33902). Frei erklärt treffen die Modelle den Sinn in bis zu 98 % der Fälle (S. 33904 bis 33905).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| MFS-Baseline (häufigster Sense nach SemCor) auf dem Haupttestset: F1 65,2. Nur das kleinste Modell, Llama-3.2-1B (56,3), liegt darunter. | S. 33899, 33900; Tab. 3 | eigenes Ergebnis |
| Zero-shot F1 auf Maru et al. 2022: GPT-4o 82,3, DeepSeek-V3 81,9, Llama-3.3-70B 81,4, gemma-2-9b 78,9; überwacht: ConSeC 83,0, ESCHER 81,6, BEM 79,5. GPT-4o und DeepSeek-V3 unterscheiden sich nicht signifikant von ConSeC (χ²). | S. 33900, Tab. 3 und Abschnitt 3.2 | eigenes Ergebnis |
| One- und Few-shot ändern fast nichts (Mittel 75,2 → 75,9); nur bei GPT-4o ist der Gewinn von knapp einem Punkt (82,3 → 83,2) signifikant. | S. 33900, Tab. 3 | eigenes Ergebnis |
| Die Formulierung des Prompts verschiebt die Werte um im Mittel etwa 5 Punkte zwischen bestem und schlechtestem von 20 Prompts; kleine Modelle sind empfindlicher. | S. 33900, Tab. 2 (S. 33899) | eigenes Ergebnis |
| hardEN (476 Fälle, an denen alle überwachten Systeme scheitern): GPT-4o 45,6, ConSeC 7,4, BEM und ESCHER 0,0. Ohne diese Fälle (4.582 Items) liegt ConSeC mit 88,5 vor GPT-4o mit 85,0. | S. 33900 bis 33901, Tab. 4 | eigenes Ergebnis |
| 42D (370 Items aus 42 Domänen): GPT-4o 76,8, DeepSeek-V3 74,6; ConSeC 56,6, ESCHER 58,9. LLMs sind über Domänen robuster. | S. 33901, Tab. 4 | eigenes Ergebnis |
| Mehr Kontext (drei Sätze statt einem) hilft den meisten Modellen nicht (GPT-4o 82,3 → 81,7, nicht signifikant). | S. 33901 bis 33902, Tab. 5 | eigenes Ergebnis |
| Zufällig gemischte Reihenfolge der Definitionen senkt die Werte (GPT-4o 82,3 → 81,3; Llama-3.2-1B 56,3 → 40,4); die Autor:innen sehen eine Positionsverzerrung zugunsten früher Optionen. | S. 33902, Tab. 5 (S. 33901) | eigenes Ergebnis und Deutung |
| Kontaminationsprüfung: Auf dem neuen, unveröffentlichten WikiPortal WSD erreicht GPT-4o 84,3 und schlägt ConSeC (82,2) signifikant; die Autor:innen werten das als „unequivocal evidence“, dass die hohen Werte nicht aus Kontamination stammen. | S. 33902, Tab. 7 | eigenes Ergebnis und Wertung |
| Mensch gegen Modell auf 400 zufälligen Items: Expert:in F1 91,25, GPT-4o 82,5. Von 70 GPT-4o-Fehlern sind 25 „serious“, 45 „borderline“ (feine Granularität); von 35 Fehlern des Menschen sind 2 „serious“. Nur ein Drittel der 45 Grenzfälle von GPT-4o macht auch der Mensch falsch. | S. 33902 bis 33903 | eigenes Ergebnis (Einordnung blind von einer zweiten Expertin oder einem zweiten Experten geprüft) |
| Sechs Fehlertypen von GPT-4o: Übergeneralisierung, Überspezifität, Grenzfall, grobe Fehldeutung, wörtlich gegen metaphorisch, Metonymie; als „serious“ gelten grobe Fehldeutung, wörtlich/metaphorisch und Metonymie. | S. 33902, Tab. 6; S. 33909, Anhang F, Tab. 22 (S. 33914) | eigenes Ergebnis |
| Nach Wortart (Anhang E): Verben und Adverbien sind schwerer als Nomen und Adjektive; GPT-4o zero-shot NOUN 85,59, ADJ 84,78, VERB 74,51, ADV 69,90; ConSeC 85,41, 86,56, 75,13, 80,61. | S. 33913, Tab. 21 | eigenes Ergebnis |
| Ohne vorgegebenes Inventar erklären die Modelle den Sinn besser: freie Erklärung „good“ 95,75 bis 98 % (Llama-3.3-70B) bzw. 96 bis 97,3 % (GPT-4o); Definitionen 90,25 % bzw. 85 % „satisfactory“ auf Maru et al. 2022. | S. 33904, Tab. 8 und 9; S. 33905 | eigenes Ergebnis (Bewertung durch eine Expertin oder einen Experten) |
| Übereinstimmung zweier Expert:innen bei der Bewertung der Generierungen (100 Items): Cohen's κ 0,791 (Definition), 0,796 (Erklärung), 0,919 (Beispiele). | S. 33904 bis 33905 | eigenes Ergebnis |
| Frühere LLM-WSD-Studien: Yae et al. mit nur ca. 800 Testitems; Kibria et al. 2024 ohne robuste Auswertung bei Halluzinationen und Formatabweichungen; Basile et al. 2025 mit automatisch erzeugten Daten und übersetzten Glossen. | S. 33898, Abschnitt 2 | referiert (Wertung der Autor:innen) |
| LLMs haben besonders mit seltenen Senses Mühe (in Übersetzung und anderen Szenarien). | S. 33897 | referiert (Campolungo et al. 2022, Martelli et al. 2025, Basile et al. 2024, Capone et al. 2024) |

## Daten, Methode, Zahlen

- **Inventar:** WordNet; im Prompt erscheinen die **Definitionen** (Glossen) aller Senses des Zielworts, nummeriert 1), 2), … (S. 33899, Tab. 1). Keine Sense-IDs, keine Synonyme oder Beispiele.
- **Prompt (Prompt 2, ausgewählt als bester von 20 auf SemEval-2007):** „Read the sentence: <sentence> Choose the correct dictionary definition of the word "<word>" from the options: <definitions>. Provide as output only the correct dictionary definition.“ (S. 33899, Tab. 1; S. 33911, Tab. 13). Die 20 Prompts in sechs Gruppen (Anweisung, Frage, Gespräch, erst Synonyme, Frage-Antwort, erst ausschließen) stehen in Anhang A (S. 33911 bis 33912). Few-shot mit drei Beispielen derselben Wortart (S. 33899).
- **Antwortformat und Parsing:** Das Modell soll die **Definition wiedergeben**, nicht die Nummer. Die Ausgabe wird tokenisiert (NLTK) und der Kandidat mit der höchsten lexikalischen Überlappung gewählt; richtig, wenn er unter den Gold-Definitionen ist (S. 33898 bis 33899). Laut manueller Prüfung „of a substantial subset“ stimmt die so gezogene Antwort in über 99,9 % mit der gemeinten Wahl überein (S. 33899). Perplexitätsbasierte Auswahl liefert für zehn offene Modelle fast dieselben Werte (S. 33908 bis 33910, Tab. 12). Nächstes-Token-Wahrscheinlichkeit wird bewusst nicht genutzt (S. 33899, mit Verweis auf Wang et al. 2024). Ein Anteil nicht zuordenbarer Antworten wird nicht berichtet; durch die Überlappungsregel bekommt jede Ausgabe einen Kandidaten.
- **Mehrere Gold-Senses:** zugelassen (|Gold| ≥ 1); richtig ist eine Antwort, wenn der gewählte Kandidat zu den Gold-Definitionen gehört (S. 33898 bis 33899).
- **Modelle** (S. 33899): offen Llama-3.2-1B/3B, gemma-2-2b, gemma-3-4b, Phi-3.5-mini, Phi-3-small-128k, Mistral-7B-v0.3, Ministral-8B-2410, Llama-3.1-8B, gemma-2-9b, gemma-3-12b, gemma-3-27b, Qwen2.5-32B, Llama-3.3-70B (alle Instruct); geschlossen bzw. über API DeepSeek-V3 und GPT-4o.
- **Einstellungen** (S. 33909, Anhang C): maximal 75 Ausgabetokens, alle anderen Hyperparameter (Temperatur, top-k) auf Standardwerten; kleine Modelle über HuggingFace `transformers`, größere über vLLM, GPT-4o und DeepSeek-V3 über die OpenAI-API. „Due to resource constraints, all experiments were run once without repeated trials.“ Keine Modell-Snapshots mit Datum, kein Abfragedatum.
- **Testmengen** (S. 33899 bis 33900): Maru et al. 2022 (manuell bereinigte Fassung des Raganato-Frameworks, 4.917 Instanzen), hardEN (476, Teilmenge davon), 42D (370 aus 42 Domänen), WikiPortal WSD (neu: 1.000 Sätze aus dem Wikipedia-Current-Events-Portal der letzten fünf Jahre, 5.549 Instanzen, Wortartverteilung wie Maru et al.; annotiert von einer Expertin oder einem Experten, 200 Items von einer zweiten Person gegengeprüft, „substantial κ agreement“ ohne Zahl; S. 33909, Anhang D).
- **Baselines:** MFS nach SemCor-Häufigkeit, „as customary in the WSD literature“ (S. 33899); überwachte Systeme ConSeC, ESCHER, BEM.
- **Maß:** F1 (S. 33899); Signifikanz mit χ², p < 0,05 (S. 33900, 33902).
- **Generierungsaufgaben** (S. 33903 bis 33905): 550 zufällige Items aus Maru et al. 2022, 42D und WikiPortal WSD; Bewertung durch eine Expertin oder einen Experten nach Richtlinien in Anhang G (S. 33909 bis 33910); κ mit einer zweiten Person auf 100 Items.

## Wörtliche Stellen

> „Provide as output only the correct dictionary definition.“ (S. 33899, Tab. 1, Prompt 2)

> „Manual inspection of a substantial subset of model outputs confirms that the extracted answer consistently matches the model's intended selection in over 99.9% of the cases on average.“ (S. 33899)

> „The only model that does not surpass the MFS baseline (65.2) is the smallest one, Llama-3.2-1B-Instruct.“ (S. 33900)

> „Due to resource constraints, all experiments were run once without repeated trials.“ (S. 33909)

> „For confidentiality and to prevent potential test set contamination in future research, we will not make this dataset publicly available.“ (S. 33909)

## Bezug zur Dissertation

- **Forschungsfrage und Baseline (Protokoll 1, 9.2, A4):** Die Arbeit ist der direkteste Vergleichspunkt: LLM wählt aus einem vorgegebenen Inventar, gemessen gegen MFS. Auf englischen Standarddaten liegt der Abstand des besten LLM zu MFS bei rund 17 Punkten F1 (82,3 gegen 65,2, S. 33900). MFS wird dort aber aus SemCor gelernt und auf anderen Texten gemessen, ohne gepaarten Test; das Protokoll misst MFS aus Silber mit Leave-out auf denselben Items und testet gepaart (McNemar). Die Zahl taugt zur Einordnung, nicht als Erwartungswert für Mittelhochdeutsch.
- **Freeze 2, Prompt (Protokoll 4.10):**
  - Die Prompt-Studie (20 Formulierungen, im Mittel ca. 5 Punkte Spanne, S. 33900) stützt, den Prompt vor der Hauptrunde einzufrieren, und zeigt, dass er auf einer **eigenen Entwicklungsmenge** gewählt werden sollte (hier SemEval-2007, nicht die Testdaten). Für die Dissertation wäre das der Pilot-Pool (Protokoll 4.2), nicht die Hauptstichprobe.
  - Die gemischte Reihenfolge der Optionen senkt die Werte (S. 33902). Das stützt Protokoll 5, Punkt 5 (Kartenreihenfolge pro Item zufällig mischen und protokollieren). Vorschlag: In Freeze 2 festhalten, dass das LLM **dieselbe gemischte Reihenfolge** sieht wie die Menschen, damit der Vergleich nicht an einer Positionsverzerrung hängt, die nur eine Seite trifft.
  - Temperatur und Läufe: Meconi et al. lassen die Temperatur auf dem Standardwert und laufen einmal (S. 33909). Die Liste in 4.10 verlangt ausdrücklich Temperatur und Läufe pro Item; die Arbeit ist dafür ein Beispiel, wie es nicht dokumentiert sein sollte.
- **Antwortformat und unparsbare Antworten (9.2):** Die Arbeit lässt die Definition wiedergeben und ordnet über lexikalische Überlappung zu; damit gibt es per Konstruktion keine unparsbare Antwort, aber eine stille Zwangszuordnung. Für die Pipeline der Dissertation zwei Optionen: (a) Antwort als Kartennummer oder Sense-ID mit strikter Prüfung und eigenem Status „unparsbar“, oder (b) Rückübersetzung wie hier mit stichprobenartiger Handprüfung. Für (b) spricht, dass das Modell Begriffsnamen wiedergeben müsste, die oft kurz und ähnlich sind (Begriffsgruppen, Protokoll 5); Überlappung wäre dann unsicher. Empfehlung für Freeze 2: Nummer oder ID als Antwort, unparsbare Antworten zählen und getrennt berichten; Abstention (`KEINE_PASST`) als ausdrückliche Option, die Meconi et al. nicht vorsehen.
- **Mehrere Gold-Senses (9.2, A14):** Meconi et al. werten wie die Primärregel des Protokolls: richtig, wenn der gewählte Sense zu den Gold-Senses gehört (S. 33898 bis 33899). Das ist ein Beleg, dass diese Regel im Feld üblich ist; Henrichs Einwand bleibt davon unberührt.
- **Aufschlüsselung nach Wortart (4.3, 9.1 Punkt 6):** Verben sind für alle Systeme deutlich schwerer als Nomen und Adjektive (GPT-4o 74,51 gegen 85,59 bzw. 84,78; S. 33913). Das stützt die Schichtung nach Wortart (NOM, VRB, ADJ) und lässt bei VRB niedrigere Werte erwarten.
- **Schwere Fälle und Nicht-MFS (9.2):** hardEN zeigt, dass ein Gesamtwert die Leistung auf schweren Items verdeckt (S. 33900 bis 33901). Das stützt die zusätzliche Auswertung auf Nicht-MFS-Items (Maru et al. 2022, im Protokoll schon zitiert).
- **Granularität und menschliche Obergrenze (9.1 Punkt 7, 9.2):** 45 von 70 Fehlern von GPT-4o sind Grenzfälle wegen feiner Sense-Unterscheidung, und Mensch und Modell irren bei verschiedenen Grenzfällen (S. 33903). Das stützt zwei Punkte des Protokolls: die menschliche IAA als Obergrenze (Calderon et al. 2025) und die Zwei-Ebenen-Auswertung über Oberbegriffe. Die Zahl 91,25 für eine einzelne Expertin oder einen einzelnen Experten ist eine Genauigkeit gegen Gold, keine IAA.
- **Kontamination (Protokoll 10) und Leckage (`knowledge/data.md` B1):** Die Arbeit hält ihren neuen Testdatensatz unveröffentlicht, um künftige Kontamination zu vermeiden (S. 33909); das ist dieselbe Begründung wie die Trennung in Protokoll 10. Ihre Kontaminationsprüfung (neues Testset, Vergleich der Werte) ist ein Muster, das sich auf die Dissertation nur begrenzt übertragen lässt: Die mittelhochdeutschen Texte sind öffentlich, geschützt werden die Labels. Zur Typliste (B1) sagt die Arbeit nichts; ihre Prompts enthalten keine Hinweise auf den Gold-Sense außer den Definitionen selbst, was die Forderung aus B1 (kein `sense/@ana` im Prompt) als Standard bestätigt.

## Grenzen und Einwände

- **Widersprüche im Text** (am Seitenbild geprüft):
  - Metonymie-Beispiel: Der Text sagt, GPT-4o wähle „a politically organized body of people under a single government“ statt „the people who live in a nation or country“ (S. 33902); Tab. 6 (S. 33902) und Tab. 22 (S. 33914) geben es umgekehrt an (Gold: politische Körperschaft, GPT-4o: die Menschen).
  - Tab. 5 nennt als zero-shot-Mittel 76,5, Tab. 3 für dieselben Modelle 75,2 (S. 33900 bis 33901). Eigene Nachrechnung: 76,5 und 74,7 (shuffle) ergeben sich nur, wenn Llama-3.2-1B ausgelassen wird; mit allen 16 Modellen sind es ca. 75,2 und 72,6. Der im Text genannte Rückgang „from 76.5 to 74.7“ (S. 33902) unterschätzt damit den Effekt, weil das Modell mit dem größten Abfall fehlt. Erklärt wird die Auslassung nirgends.
  - Kleinere Abweichungen zwischen Tab. 3 und Tab. 5 in derselben zero-shot-Spalte (z. B. gemma-2-2b 72,4 gegen 72,5).
- **Nur ein Lauf, Standardtemperatur:** Die Signifikanztests (χ²) erfassen die Stichprobenstreuung über Items, nicht die Streuung über Läufe; bei Standardtemperatur ist diese nicht null.
- **Englisch und WordNet:** Die Autor:innen nennen selbst die Einschränkung auf Englisch und weisen darauf hin, dass in anderen Sprachen unvollständige Inventare die Ergebnisse weniger robust machten, etwa weil fehlende Senses nicht als Optionen erscheinen (S. 33906). Das trifft das MHDBDB-Inventar unmittelbar (`knowledge/data.md` B9).
- **Keine Abstention:** Das Modell muss eine Definition wählen; ob das Inventar passt, wird nicht gefragt. Die Generierungsaufgaben zeigen, dass die Modelle ohne Inventar besser abschneiden (S. 33905), aber das Format der Dissertation bleibt die Auswahl.
- **Kontaminationsbeleg:** „unequivocal evidence“ (S. 33902) ist stark formuliert: WikiPortal WSD zeigt, dass die Werte auf neuen Sätzen nicht sinken; Kontamination des Inventars (WordNet-Definitionen) und der Aufgabe selbst ist damit nicht ausgeschlossen. Der Datensatz ist nicht öffentlich, die Prüfung also nicht nachvollziehbar; der κ-Wert für dessen Annotation fehlt (S. 33909).
- **Menschlicher Vergleich mit nur einer Person** auf 400 Items.
- **Generierungsbewertung** nur durch eine Person, κ mit einer zweiten auf 100 Items (S. 33904 bis 33905); die Autor:innen nennen die rein manuelle Bewertung selbst als Grenze der Reproduzierbarkeit (S. 33906).
- **Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar:** mittel. Format und Auswertungslogik (Auswahl, MFS, Wortart, schwere Fälle) sind übertragbar; Inventar (Wörterbuchdefinitionen statt Begriffsgruppen), Sprache und Datenlage nicht.

## Weiterführend

- Maru, Conia, Bevilacqua & Navigli 2022, „Nibbling at the hard core of word sense disambiguation“, ACL 2022: Haupttestset, hardEN, 42D (S. 33899).
- Raganato, Camacho-Collados & Navigli 2017, WSD-Evaluationsframework (S. 33899); liegt als PDF vor.
- Barba, Procopio & Navigli 2021, ConSeC (S. 33899); Barba, Pasini & Navigli 2021, ESCHER; Blevins & Zettlemoyer 2020, BEM.
- Wang et al. 2024, „My answer is C“: Erste-Token-Wahrscheinlichkeiten stimmen nicht mit Textantworten überein (S. 33899). Relevant für die Wahl des Antwortformats in Freeze 2.
- Kibria, Dipta & Adnan 2024, CoNLL (S. 33898); Sumanathilaka, Micallef & Hough 2025, arXiv:2411.18337, Prompt-Anreicherung mit Wortart, Synonymen, Beispielen (S. 33898).
- Capone et al. 2024, „Lost in disambiguation: How instruction-tuned LLMs master lexical ambiguity“ (S. 33897).
- Tedeschi et al. 2023, „What's the meaning of superhuman performance in today's NLU?“, ACL 2023 (S. 33903): zum Vergleich Mensch gegen Modell.
- Basile, Musacchio & Siciliani 2024, ITA-SENSE, CLiC-it 2024 (S. 33898).
