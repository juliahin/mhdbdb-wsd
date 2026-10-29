# Gengnagel et al. 2024: LLM Glossary (Entwurf)

**Datei:** `pdf/Gengnagel-etal-2024-LLM-Glossary.pdf` (nur lokal; 11 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganzes PDF an der Textebene gelesen; Suche nach einer neueren Fassung am 2026-10-28 (Ergebnis unter Bibliografie).

Seitenzählung: PDF-Seite n = gedruckte S. n.

## Bibliografie

- **Vollständig:** Gengnagel, Tessa; Jannidis, Fotis; Kleymann, Rabea; Schröter, Julian & Zinsmeister, Heike (2024). *LLM Glossary* (draft version), 28. Februar 2024. Unveröffentlichtes Manuskript, 11 S.
- **DOI/URL:** keine im PDF. Wo es herkommt, sagt das PDF nicht.
- **Art:** Entwurf (Glossar), nicht begutachtet
- **Sprache:** Englisch
- **Neuere Fassung?** Nicht gefunden (Websuche am 2026-10-28, zwei Anfragen). Gefunden wurde nur ein Panel-Abstract derselben fünf Personen in derselben Reihenfolge: „Bedeutung in Zeiten großer Sprachmodelle", DHd 2024, Zenodo 10.5281/zenodo.10698309, v1 vom 21.02.2024, CC BY 4.0, Konferenzbeitrag; der Datensatz enthält nur das Abstract (PDF und XML), kein Glossar (○, Zenodo-Seite abgerufen). Ob das Glossar zu diesem Panel gehört, steht weder im PDF noch im Zenodo-Datensatz.

## Worum es geht

Ein Glossar mit 19 Einträgen zu Begriffen rund um große Sprachmodelle, geschrieben für Geisteswissenschaftler:innen. Neben technischen Einträgen (Embedding, Neural Network, Transformer, Training) stehen sprach- und literaturtheoretische (Distributional Hypothesis, Meaning, Interpretation, Inference, Theory of Mind). Die Einträge definieren und ordnen ein; eigene Ergebnisse gibt es nicht. Für die Dissertation tragen vor allem die Einträge zu den Grenzen von LLMs (Stabilität, Opazität, Halluzination) und zu Wissensgraphen.

## Kernaussagen

| Aussage | Seite/Eintrag | eigenes Ergebnis oder referiert? |
|---|---|---|
| Distributionelle Hypothese: Wörter in gleichen Kontexten haben ähnliche Bedeutungen; theoretische Grundlage dafür, Bedeutung geometrisch in Vektorräumen darzustellen. | S. 1, Distributional Hypothesis | referiert (Harris 1954; Sahlgren 2008; Lenci 2008) |
| Grounding: LLMs neben dem Prompt anwendungsspezifische Information mitgeben, um Genauigkeit zu verbessern; häufigste Technik ist RAG. Nötig, weil LLMs „wie Maschinen statt wie Wissensspeicher" arbeiten. | S. 2, Grounding | Definition |
| Halluzination: LLMs sind Sprach-, keine Weltmodelle, ohne Bewusstsein für Faktizität; Nutzer:innen erkennen Fiktion oft nur mit eigenem Fachwissen. Vorgeschlagene Abhilfe u. a.: Antworten gegen Wissensgraphen prüfen. | S. 2, Hallucination | Definition/Einschätzung |
| Wissensgraphen stützen implizit ein Weltmodell, wie es Menschen konzipiert haben, und unterliegen deshalb Verzerrungen, Ungenauigkeiten und Lücken. | S. 3, Knowledge Graph | Einschätzung |
| Vier Grenzen von LLMs: (1) faktische Inkonsistenz/Halluzination, (2) Bias aus den Trainingsdaten, (3) **Stabilität**: kleine Änderungen am Prompt können sehr verschiedene Ausgaben ergeben, (4) Opazität. | S. 4, Large Language Model | Einschätzung, Bias mit Bender et al. 2021 |
| In-Context Learning: Prompts mit Beispielen können Fine-Tuning verringern oder ersetzen; Chat-Modelle sind meist mit RLHF nachtrainiert. | S. 3 bis 4, Large Language Model | Definition |
| „Meaning" wird oft in Wortbedeutung, Bedeutung von Wortfolgen, Äußerungsbedeutung und Sprecherbedeutung unterschieden; dahinter stehen Streitfragen zu Intentionalität, Wahrheit, Referenz und situativem Grounding, die für die Debatte über LLMs zentral sind. | S. 5, Meaning | referiert (Tolhurst 1979) |
| Vortraining auf generischer Aufgabe, dann Fine-Tuning; neuere Chat-Modelle ermöglichen oft Zero-Shot-Lösungen, die Formulierung der Aufgabe (Prompt Engineering) wird wichtiger für verlässliche Ergebnisse. | S. 6 bis 7, Neural Network | referiert (Wei et al. 2023) |
| Prompt Engineering wirft die Frage auf, wie weit regel- und modellbasierte Textanalyse in den DH durch Prompting ersetzt wird; modell- und promptbasierte Analyse würden wohl einige Jahre konkurrieren. | S. 7 bis 8, Prompt engineering | Einschätzung |
| Probing analysiert interne Repräsentationen indirekt über gezielte Aufgaben; die Ausgabe dient als Stellvertreter. | S. 7, Probing | Definition |
| Training: Beim Fine-Tuning enthalten die Trainingsdaten oft Annotationen der Zielausgabe; Modelle übernehmen die Verzerrungen ihrer Trainingsdaten, Debiasing ist ungelöst. | S. 9, Training | Definition/Einschätzung |

## Daten, Methode, Zahlen

Keine Daten. Einträge in weitgehend alphabetischer Ordnung (S. 1 bis 9): Embedding, Distributional Hypothesis, Generative AI, Grounding, Hallucination, Inference, Interpretation, Knowledge Graph, Large Language Model, Mathematical foundations, Meaning, Neural Network, Probing, Prompt engineering, Sentence Embedding, Theory of Mind, Transformer, Training, Word Embedding (19 Überschriften; „Embedding" steht vor „Distributional Hypothesis", die Ordnung ist also nicht ganz alphabetisch). Literatur S. 9 bis 11.

## Wörtliche Stellen

> „Stability: Small perturbations of the input, e.g. small changes to the prompt, may result in very different output." (S. 4)

> „Since knowledge graphs always implicitly endorse a certain model of the world inherent to their expressions (as conceptualized by humans), they are subject to biases, inaccuracies and lacunae." (S. 3)

## Bezug zur Dissertation

- **PROTOKOLL §4.10, Freeze 2 (LLM-Konfiguration):** Die Stabilitätsgrenze (S. 4) begründet, warum Modell, Version, Prompt, Temperatur und die Zahl der Läufe pro Item vor der Hauptrunde festgeschrieben werden. Als Glossar-Definition zitierbar, nicht als Messung; für Zahlen braucht es empirische Arbeiten.
- **PROTOKOLL §5 (Karten statt Definitionen) und Grounding (S. 2):** Dass das LLM das Inventar als Karten mit Begriffsnamen erhält, ist Grounding im Sinn des Glossars: anwendungsspezifische Information neben dem Prompt. Die Wahl, keine LLM-generierten Definitionen zu zeigen, wird dadurch nicht berührt.
- **Begriffssystem als Weltmodell (S. 3):** Die Aussage, Wissensgraphen trügen ein von Menschen konzipiertes Weltmodell mit Lücken in sich, passt zu `concepts.xml` (567 Begriffe, polyhierarchisch; `knowledge/data.md` B11) und zur „Historical Semantic Gap" (Tittel & Chiarcos 2018, S. 62; Tittel et al. 2020, S. 8). Sie stützt, `KEINE_PASST` als Befund über das Inventar zu behandeln (PROTOKOLL §1, §9.2).
- **„Meaning" (S. 5):** Die Unterscheidung Wort- gegen Äußerungsbedeutung kann in der Einleitung helfen zu sagen, was WSD hier annotiert: die im Kontext gültige Bedeutung eines Tokens aus einem festen Inventar, also eine Wortbedeutung im Kontext, nicht die Äußerungs- oder Sprecherbedeutung.
- **Kontamination (PROTOKOLL §10):** Der Eintrag Training (S. 9) sagt, dass Modelle aus Trainingsdaten lernen; er sagt nichts über Testdaten. Für §10 bleiben Sainz et al. 2023 und Jacovi et al. 2023 die Belege.

## Grenzen und Einwände

- Entwurf ohne Begutachtung und ohne Ort; zitierbar höchstens als „unveröffentlichter Entwurf".
- Definitionen ohne eigene Belege, manche Einträge ohne Literatur (Grounding, Knowledge Graph, Prompt engineering).
- Sachliche Unschärfen im Text: „(CoP)" für Chain-of-Thought (S. 7); Underwood (S. 7), Shazeer et al. 2017 (S. 7) und Russell & Norvig 2016 (S. 5) werden zitiert, stehen aber nicht in der Literaturliste; Sahlgren 2008 erscheint im Literaturverzeichnis unter „Italian Journal of Disability Studies", 20 (S. 10), Lenci 2008 dagegen unter „Italian journal of linguistics", 20(1) (S. 10), vermutlich eine Verwechslung [am Original von Sahlgren zu prüfen].
- Stand Februar 2024; Modellangaben (z. B. Mixture of Experts bei „(probably) GPT 4", S. 7) sind ausdrücklich vorläufig.
- Keine Aussage zu WSD oder historischen Sprachen.

## Weiterführend

- Bender et al. 2021, *On the Dangers of Stochastic Parrots*, FAccT (S. 4, 9).
- Sahlgren 2008, *The distributional hypothesis* (S. 1, 10).
- Tolhurst 1979, *On What a Text is and How it Means* (S. 5, 11).
- Wei et al. 2023, Chain-of-Thought Prompting (S. 7, 11).
- Gengnagel, Jannidis, Kleymann, Schröter & Zinsmeister 2024, *Bedeutung in Zeiten großer Sprachmodelle*, DHd 2024, Zenodo 10.5281/zenodo.10698309 (nicht im PDF zitiert; bei der Suche gefunden).

## Julias Markierungen im PDF

73 Hervorhebungen, 12 Randzeichen, keine Notizen (`md/Gengnagel-etal-2024-LLM-Glossary.markierungen.md`). Aufgenommen: Grounding und RAG mit semantischer Suche (S. 2); „LLMs are language models rather than models of the world …" mit Randzeichen (S. 2); Prüfung gegen Wissensgraphen (S. 2); Knowledge Graph samt Bias-Satz (S. 3); Fine-Tuning und In-Context Learning (S. 3); die vier Grenzen (S. 4); Probing (S. 4, 7); „Meaning" mit den vier Bedeutungsarten und den Streitfragen (S. 5); Zwei-Schritt-Ansatz aus Vortraining und Fine-Tuning mit Randzeichen (S. 6); Zero-Shot und Prompt Engineering mit Randzeichen (S. 7); Training mit Annotationen beim Fine-Tuning, Bias, Debiasing, RLHF mit Randzeichen über 13 Zeilen (S. 9). Nur knapp oder nicht aufgenommen, weil technischer Hintergrund ohne Bezug zum Protokoll: Embedding, Generative AI (Randzeichen S. 1), Mathematical foundations (Randzeichen S. 4), Aufbau von Knoten, Gewichten und Aktivierungsfunktion (S. 5 bis 6), CNN/GRU/LSTM, Multimodalität und Mixture of Experts (S. 6 bis 7), Sentence Embedding, Transformer, Word Embedding (S. 8 bis 9).
