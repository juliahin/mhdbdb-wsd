# Yang et al. 2024: Harnessing the Power of LLMs in Practice

**Datei:** `pdf/Yang-etal-2024-Harnessing-LLMs.pdf` (nur lokal; 32 Seiten, Verlagsfassung)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganze Textebene gelesen, DOI aufgelöst. Priorität 3: bewusst knapp. Keine Markierungen im PDF (keine Anmerkungsebene).

Seitenzählung: Artikel 160, gezählt 160:1 bis 160:32; PDF-Seite n = 160:n. Unten steht nur n.

## Bibliografie

- **Vollständig:** Yang, Jingfeng; Jin, Hongye; Tang, Ruixiang; Han, Xiaotian; Feng, Qizhang; Jiang, Haoming; Zhong, Shaochen; Yin, Bing; Hu, Xia (2024). Harnessing the Power of LLMs in Practice: A Survey on ChatGPT and Beyond. *ACM Transactions on Knowledge Discovery from Data* 18(6), Article 160, 32 S. (April 2024).
- **DOI/URL:** https://doi.org/10.1145/3649506 (aufgelöst auf dl.acm.org). Crossref: online 26.04.2024, Druck 31.07.2024, Lizenz CC BY 4.0. Eingereicht 6.6.2023, überarbeitet 30.10.2023, angenommen 16.1.2024 (S. 32).
- **Art:** begutachteter Zeitschriftenartikel (Survey)
- **Sprache:** Englisch

## Worum es geht

Ein Praxisleitfaden für die Frage, wann man ein großes Sprachmodell ohne aufgabenspezifisches Training (LLM) und wann ein kleineres, feinabgestimmtes Modell einsetzt (S. 1 bis 2). Er gibt einen Stammbaum der Modelle (S. 3 bis 6), diskutiert Vortrainings-, Feinabstimmungs- und Testdaten (S. 6 bis 8) und geht Aufgabentypen mit „use case“ und „no-use case“ durch (S. 8 bis 18); eine Entscheidungsgrafik fasst das zusammen (S. 18 bis 19, Abb. 2). Es folgen Effizienz, Vertrauenswürdigkeit und offene Probleme (S. 19 bis 25). Eigene Experimente enthält der Artikel nicht.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Arbeitsdefinition: LLMs sind große, ohne aufgabenspezifische Daten vortrainierte Modelle; feinabgestimmte Modelle sind kleiner und auf eine Aufgabe nachtrainiert. Praktisch gelten Modelle unter 20 Mrd. Parametern als feinabstimmbar. | S. 2, mit Anm. 1 | Festlegung der Autor:innen |
| Encoder-Modelle wie BERT und RoBERTa (Masked LM, bidirektional) sind stark im Sprachverstehen; nach 2021 dominieren Decoder-Modelle. | S. 3 bis 4, Abschnitt 2 und 2.1 | Einordnung |
| LLMs generalisieren besser bei Verteilungsverschiebung und sind bei wenigen annotierten Daten vorzuziehen; Modelle sollten auf Daten ähnlicher Domäne vortrainiert sein. | S. 6, Remark 1 | Synthese aus Literatur |
| Ohne annotierte Daten ist Zero-Shot mit LLMs der geeignete Weg; bei reichlich Daten ist die Wahl aufgabenabhängig. | S. 7, Abschnitt 3.2 | Synthese |
| In-Context Learning hängt vom Prompt-Template sowie von Auswahl und Reihenfolge der Beispiele ab; die Mechanik ist wenig verstanden. | S. 8, Abschnitt 4 | referiert |
| Bei klassischen NLU-Aufgaben sind feinabgestimmte Modelle meist besser (Remark 2); bei NER (CoNLL03) etwa doppelt so gut wie LLMs. | S. 9, Abschnitt 4.1.1 | referiert |
| LLMs übersetzen manche ressourcenarme Sprachen ins Englische gut; BLOOM übersetzt sogar aus dem Galicischen, das nicht in seinen Vortrainingsdaten ist, vermutlich über verwandte romanische Sprachen. | S. 10 bis 11, Abschnitt 4.2.1 | referiert |
| LLMs eignen sich als Annotator und Datengenerator; manche seien „as good as human annotators“ bei einigen Aufgaben. | S. 15, Remark 6 und Abschnitt 4.5.2 | referiert (Gilardi et al. 2023) |
| Auch LLMs lernen Abkürzungen beim In-Context Learning: majority label bias, position bias und common token bias; passende Prompts können den Positionseffekt mildern. | S. 21, Abschnitt 5.2 | referiert (Zhao et al. 2021; Lu et al. 2022) |
| Daten im Training, die den Testdaten ähneln, können Leistungswerte aufblähen. | S. 23, Abschnitt 6 | Einschätzung |

## Daten, Methode, Zahlen

Survey ohne eigene Daten. Einzelne referierte Zahlen, nur zur Einordnung: GPT-4 86,5 % auf MMLU (S. 12); Trainingskosten T5 11B über 1,3 Mio. USD, GPT-3 175B 4,6 Mio. USD (S. 20); Inferenzzeiten GPT-J 6B 0,077 bis 0,707 s je nach Tokenlänge (S. 20). Die Preisangaben für die OpenAI-API (S. 20) beziehen sich auf den Stand 2023. Kein Abschnitt behandelt WSD, lexikalische Semantik oder historische Sprachen (Volltextsuche nach „sense“, „disambiguation“, „ambiguity“: nur „commonsense“ und ein allgemeiner Satz zu Mehrdeutigkeit in Nutzeranfragen, S. 16).

## Wörtliche Stellen

> „LLMs are huge language models pretrained on large amounts of datasets without tuning on data for specific tasks; fine-tuned models are typically smaller language models, which are also pretrained and then further tuned on a smaller, task-specific dataset“ (S. 2)

> „the examined LLMs are susceptible to majority label bias and position bias, where they tend to predict answers based on the frequency or position of the answers in the training data“ (S. 21)

## Bezug zur Dissertation

- **Einordnung im Methodenkapitel:** Die Definition von LLM gegenüber feinabgestimmtem Modell (S. 2) eignet sich als Arbeitsbegriff, wenn die Dissertation den LLM-Ansatz (Zero- oder Few-Shot mit Sense-Karten) gegen eine spätere Feinabstimmung abgrenzt. Für Mittelhochdeutsch gibt es wenig annotierte Daten; nach Remark 1 (S. 6) und Abschnitt 3.2 (S. 7) spricht das für LLMs, nach Remark 1 (3) aber gegen Modelle ohne passendes Vortraining. Beides ist allgemeine Literatursynthese, kein Befund zu historischen Sprachen.
- **PROTOKOLL §5, Punkt 5 (Kartenreihenfolge) und §4.10 (LLM-Konfiguration):** Position bias und majority label bias (S. 21) begründen, die Kartenreihenfolge auch für das LLM pro Item zu mischen und die Reihenfolge zu protokollieren. Majority label bias berührt außerdem den Vergleich mit der MFS-Baseline (§9.2): Ein LLM, das zum häufigen Sense neigt, kann MFS-ähnlich entscheiden; die vorgesehene Auswertung auf Nicht-MFS-Items fängt das auf.
- **§10 (Kontamination):** Die Warnung vor Testdaten im Training (S. 23) stützt die Ablage der Labels, ist aber nur eine allgemeine Einschätzung ohne Beleg im Artikel.
- **LLM als Annotator (Remark 6, S. 15):** Die Aussage stützt sich auf Gilardi et al. 2023 und betrifft andere Aufgaben; für das Protokoll (§9.2, Vergleich mit der menschlichen IAA) ist sie keine eigene Evidenz.

## Grenzen und Einwände

- Praxisleitfaden mit Stand 2023 (eingereicht Juni 2023); Modellstand, Preise und Bewertungen sind überholt.
- Aussagen in den „Remarks“ sind Verallgemeinerungen aus wenigen zitierten Studien, oft Preprints; keine systematische Literaturauswahl beschrieben.
- Keine Behandlung von WSD, Inventaren oder historischen Sprachen; die Übertragung auf Mittelhochdeutsch und ein onomasiologisches Inventar ist eigene Interpretation.

## Weiterführend

- Zhao, Wallace, Feng, Klein & Singh 2021, Calibrate before use: Improving few-shot performance of language models, ICML (S. 21, 32): majority label, position und common token bias.
- Lu, Bartolo, Moore, Riedel & Stenetorp 2022, Fantastically ordered prompts and where to find them, ACL, S. 8086 bis 8098 (S. 21, 29): Reihenfolge der Beispiele.
- Gilardi, Alizadeh & Kubli 2023, ChatGPT outperforms crowd-workers for text-annotation tasks (S. 15, 28).
- Ding et al. 2022, Is GPT-3 a Good Data Annotator? (S. 15, 27).
