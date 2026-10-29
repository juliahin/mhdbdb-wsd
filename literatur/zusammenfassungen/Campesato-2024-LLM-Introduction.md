# Campesato 2024: Large Language Models. An Introduction (ausgewählte Kapitel)

**Datei:** `pdf/Campesato-2024-LLM-Introduction.pdf` (nur lokal; 502 PDF-Seiten, xxii + 480 S.)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29. Gelesen wurden nur die unten genannten Abschnitte; Seitenangaben an der Textebene geprüft, S. 168 zusätzlich am Seitenbild.

Seitenzählung: PDF-Seite = gedruckte Seite + 22 (durchgehend geprüft von S. 1 bis S. 461). Zitiert wird „S. x (PDF y)".

**Kapitelauswahl:** Julias Markierungen liegen alle in Kapitel 1 (S. 1 bis 14), deshalb ist dieser Teil knapp aufgenommen. Inhaltlich gewählt wurde, was Prompt-Varianz, Temperatur und Sampling, Evaluation, Halluzination und Grenzen von LLMs behandelt: Kap. 1, S. 1 bis 14 und S. 42 bis 44; Kap. 3, S. 86 bis 92; Kap. 4, S. 128 bis 138, 141, 145 bis 146, 150 bis 153 und 167 bis 174; Kap. 5, S. 187 bis 209 und S. 218 bis 219; Kap. 6, S. 295 bis 297, 311 bis 313 und 318 bis 319; aus Kap. 8 nur S. 408 und S. 460 bis 461. Code-Listings, Installationsanleitungen und Produktbeschreibungen sind nicht zusammengefasst.

## Bibliografie

- **Vollständig:** Campesato, Oswald (2024). *Large Language Models: An Introduction*. Boston, MA: Mercury Learning and Information (Imprint von De Gruyter Inc.). MLI Generative AI Series. xxii + 480 S.
- **ISBN:** Paperback 978-1-5015-2329-8 (im Impressum als „978-1-501523-298" gedruckt, PDF-Seite 4); E-Book PDF 978-1-5015-2058-7; ePub 978-1-5015-2060-0. LCCN 2024943331 (Impressum).
- **DOI/URL:** 10.1515/9781501520587 (aufgelöst am 2026-10-29, leitet auf degruyterbrill.com weiter). Verlagsseite: https://reference-global.com/book/9781501520587
- **Auflage:** im Impressum keine Angabe.
- **Jahr:** Copyright 2024 (Impressum); Vorwort „August 2024" (S. xxii, PDF 22). reference-global nennt Oktober 2024, Crossref den 14.06.2024 als Erscheinungsdatum; der Juni-Termin liegt vor dem Datum des Vorworts.
- **Art:** Monografie, Lehrbuch für Entwickler:innen (Zielgruppe S. xx, PDF 20); nicht begutachtet
- **Sprache:** Englisch
- **Lizenz:** alle Rechte vorbehalten (Impressum, PDF-Seite 4)

## Worum es geht

Ein einführendes Praxisbuch zu generativer KI und LLMs für Leser:innen mit Grundkenntnissen und für Python-Entwickler:innen (S. xx, PDF 20). Es behandelt in acht Kapiteln generative KI, ChatGPT und GPT-4, die BERT-Familie, Prompt Engineering, Halluzinationen und kleine Modelle, Fine-Tuning, SVG-Erzeugung mit GPT-4 und Vermischtes. Ein großer Teil des Textes sind **wörtlich abgedruckte Antworten von Chatbots** (ChatGPT, GPT-4o, Claude 3, Gemini, Cohere, Meta AI, Grok, Perplexity) auf Fragen des Autors, meist ohne Kommentar; das Vorwort sagt es für Kapitel 5 selbst: Vorschläge gegen Halluzinationen „provided by various LLMs" (S. xix, PDF 19). Eigene Messungen gibt es nicht. Für die Dissertation trägt das Buch höchstens als Lehrbuchbeleg dafür, dass Prompt-Formulierung, wiederholte Abfrage und Temperatur die Ausgabe ändern; für Zahlen und Definitionen ist es nicht zitierfähig (siehe Grenzen).

## Kernaussagen

„Autor" heißt: Text des Autors, ohne Beleg. „Chatbot" heißt: abgedruckte Antwort eines Modells, vom Autor nicht geprüft.

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Generative KI erzeugt neue Daten, statt nur zu analysieren oder zu klassifizieren; „traditionelle" Modelle ordnen Eingaben vorgegebenen Kategorien zu. | S. 1 bis 2 (PDF 23 bis 24) | Autor, Definition |
| LLMs verstehen Sprache nicht wie Menschen; menschenähnliche Entscheidungen beweisen kein Verstehen (Schach-Anekdote). | S. 86 bis 87 (PDF 108 bis 109) | Autor, Einschätzung |
| Vorbehalte: kleinere Modelle können größere in manchen Aufgaben übertreffen; Modelle erzeugen falsche Ergebnisse („hallucinating"); Trainingsdaten enden zu einem Stichtag. | S. 87 (PDF 109) | Autor |
| Dieselbe Eingabe mehrmals an GPT-4 liefert nicht dieselben Ergebnisse („not consistent (albeit similar)"); Prompt Engineering, zusammen mit Fine-Tuning, mache sie konsistenter. Temperatur und Zahl der Wiederholungen sind nicht angegeben. | S. 129 (PDF 151) | Autor, keine Messung |
| Zwei gut gestaltete Prompts für dieselbe Aufgabe können deutlich verschiedene Ergebnisse liefern (S. 130); schon eine leicht andere Formulierung kann deutlich andere Ausgaben ergeben (S. 132); ebenso ähnliche, aber verschiedene Prompts (S. 43). | S. 43, 130, 132 (PDF 65, 152, 154) | Autor |
| Dieselbe Aussage in zwei Chatbot-Antworten: Claude 3 nennt „Sensitivity to prompts" als Ursache von Halluzinationen (S. 194), GPT-4o nennt beim Prompt Engineering als Nachteil „Inconsistency" bei leicht geänderter Formulierung (S. 312). | S. 194, 312 (PDF 216, 334) | Chatbot |
| Die Genauigkeit der Vorhersagen zu bewerten sei bei LLMs aufwendiger als bei herkömmlichen Verfahren; Inferenz großer Modelle ist langsam, mehrere hunderttausend Vorhersagen können Stunden bis Tage dauern. | S. 130 bis 131 (PDF 152 bis 153) | Autor |
| Prompt-Vorlagen mit Platzhaltern sichern Konsistenz bei mehrfacher Abfrage, erleichtern Stapelverarbeitung und verringern Unterschiede in der Fragestellung. | S. 137 (PDF 159) | Autor |
| Zero-Shot: nur Aufgabenbeschreibung; One-Shot: ein Beispiel; Few-Shot: mehrere Beispiele, „typically between ten and one hundred". | S. 134 (PDF 156) | Autor |
| Few-Shot-Beispiele verbrauchen Kontextfenster; kleinere LLMs verbessern sich durch Beispiele nicht unbedingt. | S. 295 (PDF 317) | Autor |
| Chain of Thought: „zero-shot-CoT" mit „Let's think step by step" übertreffe Zero-Shot auf mehreren Aufgaben. | S. 145 (PDF 167) | referiert (arXiv 2210.03493 und 2205.11916, nur als Link) |
| Self-Consistency wählt aus mehreren erzeugten Stichproben statt der gierigen Dekodierung und schneide besser ab als einfaches CoT; LMSI kombiniert Few-Shot-CoT mit Mehrheitsabstimmung über die Vorhersagen. | S. 145 bis 146 (PDF 167 bis 168) | referiert (arXiv 2203.11171; 2210.11610) |
| Temperatur steuert die Zufälligkeit der Tokenwahl: kleine Werte nahe 0 sind deterministischer, größere zufälliger; T steht im Exponenten der Softmax (e^(x_i/T)), T = 1 entspricht der normalen Softmax. | S. 168 bis 169 (PDF 190 bis 191) | Autor |
| Bei Temperatur 0 arbeite das LLM mit einer „so-called deterministic methodology"; bei 1 wähle es auch weniger wahrscheinliche Wörter, was bis zu scheinbarer Halluzination führen könne. | S. 218 bis 219 (PDF 240 bis 241) | Autor |
| Evaluation umfasst u. a. aufgabenbezogene Genauigkeit (Precision, Recall, F1), Generalisierung, Robustheit sowie „Consistency and Stability" mit den Metriken „Response variance, consistency scores". | S. 187 bis 190 (PDF 209 bis 212) | Chatbot (GPT-4o) |
| Halluzination: das Modell antwortet „confidently" falsch; das komme bei jedem LLM vor. | S. 191 (PDF 213) | Autor |
| Ursachen und Gegenmittel von Halluzinationen: sechs Chatbot-Antworten (S. 191 bis 200) und vier weitere (S. 200 bis 207). Genannt werden u. a. RAG und Wissensbasen, genauere Prompts, Unsicherheitsschätzung, menschliche Prüfung, Ensembles mit Mehrheitsabstimmung (Cohere, S. 203), niedrigere Temperatur (ChatGPT, S. 201). Claude 3 und Gemini sagen, keine Einzeltechnik beseitige Halluzinationen ganz (S. 195, 200). | S. 191 bis 207 (PDF 213 bis 229) | Chatbot |
| Grenzen: oberflächliches Verständnis, Inkonsistenz über lange Kontexte, flaches Wissen in Nischendomänen, die in den Trainingsdaten schwach vertreten sind. | S. 207 bis 208 (PDF 229 bis 230) | Chatbot (GPT-4o) |
| Benchmarks veralten, sobald alle aktuellen Modelle sie bestehen. | S. 43 (PDF 65) | Autor |
| Beschreibungen von MMLU, „HellSwag", TruthfulQA und MT-Bench (Schreibung wie im Buch). | S. 318 bis 319 (PDF 340 bis 341) | Chatbot (Cohere) |

## Daten, Methode, Zahlen

Keine eigenen Daten und keine Experimente. Alle Zahlen sind Behauptungen des Autors oder Chatbot-Ausgaben, nicht gemessen:

- Temperatur: laut Autor „usually between 0 and 1 inclusive", Standardwert 0,7 (S. 168, PDF 190; gleichlautend S. 218, PDF 240); laut abgedruckter GPT-4o-Antwort „Typical Range: 0.7 to 1.5" (S. 170, PDF 192) und nützliche Werte 0,7, 0,9 und 1,5 (S. 174, PDF 196).
- Few-Shot: „typically between ten and one hundred" Beispiele (S. 134, PDF 156); vier Seiten vorher heißt es, GPT-Modelle „typically require a few hundred examples" für die meisten nachgelagerten Aufgaben (S. 130, PDF 152).
- Kontextlänge: von 1.024 bis eine Million Tokens (S. 125, PDF 147), aber Prompt und Completion zusammen „at most 2,048 tokens" (S. 132, PDF 154).
- Self-Consistency: Faustregel, etwa zwei Dutzend Sätze zu erzeugen und den besten zu wählen (S. 145, PDF 167), referiert nach arXiv 2203.11171 [am Original zu prüfen].

## Wörtliche Stellen

> „For instance, if one submits the same prompt several times to GPT-4, the results are not consistent (albeit similar)." (S. 129, PDF 151)

> „It's important to note that two well-designed prompts for the same task can generate substantively different results." (S. 130, PDF 152)

> „Creation versus classification: While most traditional AI models aim to classify input data into predefined categories, generative models aim to create new data." (S. 2, PDF 24; von Julia markiert)

## Bezug zur Dissertation

- **PROTOKOLL §4.10, Freeze 2 (LLM-Konfiguration):** Das Buch stützt als Lehrbuchmeinung, dass Prompt-Wortlaut (S. 43, 130, 132), wiederholte Abfrage desselben Prompts (S. 129) und Temperatur (S. 168 bis 169) die Ausgabe ändern. Das begründet, warum Modell und Version, Prompt, Temperatur und die Zahl der Läufe pro Item vor der Hauptrunde festgeschrieben werden. Es ersetzt keine Messung: Keine dieser Aussagen ist belegt, für den Artikel braucht es empirische Arbeiten.
- **Temperatur ausdrücklich setzen, nicht den Standardwert nehmen:** Das Buch nennt einen Standardwert von 0,7 (S. 168) und widerspricht sich bei den üblichen Wertebereichen (S. 168 gegen S. 170 und S. 174). Für Freeze 2 heißt das: den tatsächlich gesetzten Wert protokollieren, dazu die übrigen Sampling-Parameter (top_p, top_k, maximale Länge), weil auch sie die Auswahl der Tokens begrenzen (S. 168).
- **„Deterministisch" bei Temperatur 0 (S. 218) ist eine Behauptung, keine Zusage.** Ob wiederholte Läufe bei 0 wirklich gleich ausfallen, sagt das Buch nicht; die Aussage zur Inkonsistenz auf S. 129 nennt keine Temperatur. Wenn das Protokoll mehrere Läufe pro Item vorsieht, ist die Übereinstimmung zwischen den Läufen selbst ein Ergebnis, das berichtet werden kann (vgl. „Consistency and Stability", S. 188, dort nur Chatbot-Text).
- **Mehrere Läufe zusammenführen:** Self-Consistency und LMSI wählen per Mehrheit über mehrere Stichproben (S. 145 bis 146), Cohere nennt Mehrheitsabstimmung über Modelle (S. 203). §4.10 legt die Zahl der Läufe fest, aber nicht, wie aus mehreren Läufen eine Vorhersage wird. Vorschlag für Freeze 2: Aggregationsregel (z. B. Mehrheit mit Regel für Gleichstand) mit festschreiben. Beleg dafür nicht dieses Buch, sondern die Self-Consistency-Arbeit selbst (im Buch nur als arXiv 2203.11171 verlinkt, S. 145).
- **Generieren statt klassifizieren (S. 2, von Julia markiert):** Die WSD-Aufgabe des Protokolls ist eine Klassifikation in ein festes Menü von Karten (PROTOKOLL §5, §6), gelöst mit einem generativen Modell. Daraus folgt eine Regel, die §9.2 bisher nur zum Teil hat: Was gilt, wenn das LLM keine gültige Sense-ID aus dem Menü des Items zurückgibt (freier Text, ID eines anderen Lemmas, mehrere IDs)? Vorschlag: vor Freeze 2 festlegen und den Anteil berichten.
- **Few-Shot (S. 134, 295):** Falls der Prompt Beispiele enthält, gehört in Freeze 2, wie viele und woher. Beispiele aus den Stichproben-Items würden die Trennung nach PROTOKOLL §10 unterlaufen; das ist eine Folgerung, keine Aussage des Buchs.
- **Nischendomänen (S. 208, Chatbot):** Die Aussage, LLMs hätten in schwach vertretenen Domänen nur flaches Wissen, passt zur Erwartung für Mittelhochdeutsch, ist aber nicht zitierfähig.

## Grenzen und Einwände

- **Großteils Chatbot-Text.** Ganze Abschnitte bestehen aus unkommentierten Modellantworten, das Halluzinationskapitel fast vollständig (S. 191 bis 207). Auch zwei der von Julia markierten Stellen stehen in Chatbot-Antworten (S. 4 und S. 14, siehe unten). Solche Stellen sind keine Aussage des Autors und nicht als Beleg zu zitieren.
- **Fehler und Widersprüche im eigenen Text des Autors** (an der Textebene, S. 168 auch am Seitenbild geprüft):
  - top_p sei „a positive integer" und im übernächsten Absatz „a floating-point number between 0.0 and 1.0" (S. 168, PDF 190).
  - Im top-p-Beispiel (Verteilung {0,1; 0,2; 0,3; 0,4}, p = 0,3) sollen gerade die beiden unwahrscheinlichsten Tokens (0,1 und 0,2) wählbar sein (S. 168). Das passt nicht zur im selben Kapitel abgedruckten GPT-4o-Beschreibung, nach der die kleinste Tokenmenge gewählt wird, deren kumulierte Wahrscheinlichkeit p übersteigt (S. 171, PDF 193); nach dieser Regel wäre es {0,4}.
  - Auswahl über die Softmax bedeute, dass immer das wahrscheinlichste Token gewählt werde (S. 169, PDF 191).
  - „stop tokens" = 1 erzeuge genau einen Satz, = 2 einen Absatz (S. 168).
  - BERT habe „only 1.5 billion parameters" (S. 38, PDF 60); BERT-large hat laut S. 94 (PDF 116) 340M.
  - Die Angaben zu Temperatur, Few-Shot-Zahl und Kontextlänge widersprechen sich (oben unter Zahlen).
  - Self-Consistency sei auf GPT-4 getestet (S. 145). Laut S. 86 erschien GPT-4 erst am 14.03.2023, die Arbeit ist nach ihrer arXiv-Nummer 2203.11171 älter [am Original zu prüfen].

  Für technische Definitionen von Sampling-Parametern ist das Buch deshalb nicht zitierfähig; dafür Originalarbeiten oder die Dokumentation des verwendeten Modells nehmen.
- Referierte Arbeiten erscheinen meist nur als arXiv-Link, ohne Literaturverzeichnis; die Ergebnisse sind nicht nachprüfbar wiedergegeben.
- Stand Mitte 2024 (GPT-4o, Claude 3, Llama 3); Modellangaben veralten schnell.
- Nichts zu WSD, zu historischen Sprachen oder zu Annotation mit festem Inventar. „Historical Bias" (S. 408, PDF 430) meint veraltete gesellschaftliche Wertungen in Trainingsdaten, nicht historische Sprachstufen.

## Weiterführend

Das Buch zitiert diese Arbeiten nur als arXiv-Link, meist ohne Autor:innen und Titel; vor einer Übernahme im Original lesen:

- Self-Consistency, arXiv 2203.11171 (S. 145, PDF 167): Auswahl aus mehreren erzeugten Stichproben, einschlägig für die Zahl der Läufe pro Item und ihre Zusammenführung.
- Zero-shot-CoT, arXiv 2205.11916; dazu arXiv 2210.03493 und 2201.11903 (alle S. 145, PDF 167).
- LMSI (Few-Shot-CoT mit Mehrheitsabstimmung), arXiv 2210.11610 (S. 146, PDF 168).
- Kaplan et al. (2020), „Scaling Laws for Neural Language Models", arXiv 2001.08361 (S. 86, PDF 108).
- „Emergent Abilities of Large Language Models", arXiv 2206.07682 (S. 45, PDF 67).

## Übrige Kapitel (nur Titel)

- Kap. 1 *The Generative AI Landscape* (S. 1): außer den genannten Abschnitten Text-to-Image, AGI, Firmenporträts (DeepMind, OpenAI, Cohere, Hugging Face, AI21, Anthropic), Geschichte der LLMs, GPT-2-Codebeispiel, Sora.
- Kap. 2 *ChatGPT and GPT-4* (S. 55): nicht gelesen.
- Kap. 3 *LLMs and the BERT Family* (S. 83): außer S. 86 bis 92 BERT, BERT-Familie, Übersetzung, mehrsprachige Modelle, T5, PaLM; Code.
- Kap. 4 *Prompt Engineering* (S. 125): außer den genannten Abschnitten Prompt Injections, Tree of Thought, GPT-4-Beispielprompts (SVG, Arithmetik, Übersetzung, Lyrik, Humor), Wiederholungen bei GPT-2; Code.
- Kap. 5 *Working with LLMs* (S. 183): außer den genannten Abschnitten Kaplan, Mixture of Experts, Open- gegen Closed-Source, Modellporträts, kleine Sprachmodelle, KI-Agenten.
- Kap. 6 *LLMs and Fine-Tuning* (S. 257): außer den genannten Abschnitten Fine-Tuning-Techniken, SFT, RLHF, PEFT, LoRA, Quantisierung, synthetische Daten, Catastrophic Forgetting, Wahrscheinlichkeitsmaße; Code.
- Kap. 7 *SVG and GPT-4* (S. 335): nicht gelesen.
- Kap. 8 *Miscellaneous Topics* (S. 407): außer S. 408 und S. 460 bis 461 (Täuschungsformen nach ChatGPT: Konfabulation, Halluzination, irreführende Antworten u. a.) Ethik, Sicherheit, Mehrsprachigkeit, Datenschutz, Nachhaltigkeit, Governance, Hardware, Quantencomputing, Robotik, AR/VR.

## Julias Markierungen im PDF

18 Hervorhebungen und 1 Notiz, alle in Kapitel 1, S. 1 bis 14 (`md/Campesato-2024-LLM-Introduction.markierungen.md`). Geprüft und so behandelt:

- **Aufgenommen:** „Generative AI stands apart in its ability to create and innovate, as opposed to merely analyzing or classifying" (S. 1) und „Creation versus classification ..." (S. 2): in die Kernaussagen und in den Bezug (Klassifikation mit einem generativen Modell, Regel für ungültige Ausgaben).
- **Geprüft, nur als Hintergrund:** Merkmale „data generation, synthesis, learning distributions" und die Techniken GANs, VAEs, RNNs (S. 2); „Unsupervised learning", „Diverse outputs", „Challenges" (dort: Mode Collapse bei GANs, Kohärenz) (S. 3); Anwendungsfelder „data augmentation" mit Definition und „text generation" (S. 3). Allgemeine Begriffsklärung ohne Bezug zum Protokoll. Datenaugmentierung „when the original dataset is limited" (S. 3) wäre nur einschlägig, wenn LLM-erzeugte Daten in die Arbeit eingingen; das Protokoll sieht das nicht vor (§5: keine LLM-generierten Definitionen).
- **Markiert, aber Chatbot-Text:** „Natural Language Processing (NLP) and Text Generation:" (S. 4) steht in einer GPT-4-Antwort (Prompt S. 4, PDF 26); „interconnected fields within artificial intelligence, each with its own focus and methodologies" (S. 14) steht in einer ChatGPT-Antwort (Prompt S. 13, PDF 35). Nicht als Aussage des Autors aufgenommen.
- **Nicht aufgenommen:** „Generative AI transcends CGI in dramatic ways ..." (S. 6), Prognose ohne Bezug; die Überschrift „GENERATIVE AI VERSUS ML, DL, NLP, AND RL" (S. 13).

## Julias Notizen im PDF

- S. 1 (PDF 23), violett: „very good glossary". Worauf sich die Notiz bezieht, steht nicht dabei; sie sitzt am Kapitelanfang.
