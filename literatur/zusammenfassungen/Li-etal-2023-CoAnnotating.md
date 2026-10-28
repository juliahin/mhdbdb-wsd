# Li et al. 2023: CoAnnotating

**Datei:** `pdf/Li-etal-2023-CoAnnotating.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, lokales arXiv-PDF vollständig gelesen, mit der EMNLP-Fassung abgeglichen, Venue, Seiten und DOI geprüft.

**Seitenzählung:** Zitiert wird nach der EMNLP-Fassung (S. 1487 bis 1505); PDF-Seite n entspricht S. 1486 + n. Gelesen wurde ursprünglich arXiv:2310.15638v1 (12 Seiten, ohne Seitenzahlen, Text gleich, Seitenumbrüche nahezu gleich), abgeglichen mit der EMNLP-Fassung. Seit 2026-10-28 liegt unter dem lokalen Dateinamen die EMNLP-Fassung (19 Seiten). Anhang A (Modelleinstellungen) und B (alle Prompts), S. 1499 bis 1505, fehlten in der arXiv-Fassung; sie sind unten mit „nur EMNLP" gekennzeichnet.

## Bibliografie

- **Vollständig:** Li, Minzhi, Taiwei Shi, Caleb Ziems, Min-Yen Kan, Nancy F. Chen, Zhengyuan Liu & Diyi Yang, 2023. CoAnnotating: Uncertainty-Guided Work Allocation between Human and Large Language Models for Data Annotation. In *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*, 1487 bis 1505. Singapur: Association for Computational Linguistics.
- **DOI/URL:** https://doi.org/10.18653/v1/2023.emnlp-main.92 (löst auf https://aclanthology.org/2023.emnlp-main.92 auf; Anthology-Eintrag und EMNLP-PDF am 2026-10-28 gelesen). ✔ Preprint: arXiv:2310.15638v1, 24. Oktober 2023, auf der arXiv-Seite mit der EMNLP-DOI verknüpft. ✔
- **Art:** Konferenzbeitrag (EMNLP 2023, Hauptkonferenz; die Danksagung nennt anonyme EMNLP-Gutachter:innen, S. 1495)
- **Sprache:** Englisch

## Worum es geht

Die Arbeit behandelt Menschen und LLMs nicht als Konkurrenten, sondern fragt, wie man Annotationsarbeit innerhalb eines Datensatzes zwischen beiden aufteilt (S. 1488). Für jedes Item wird ChatGPT (gpt-3.5-turbo) mit sieben Prompt-Varianten befragt; aus der Streuung der Antworten (Entropie) oder aus der selbst angegebenen Konfidenz wird die Unsicherheit geschätzt, und sichere Items gehen an das LLM, unsichere an Menschen (S. 1489 bis 1491). Die Qualität jeder Aufteilung wird über ein auf den gemischten Labels feinjustiertes RoBERTa gemessen und gegen die Kosten in einer Pareto-Analyse abgewogen (S. 1491 bis 1492). Ergebnis: Entropie über verschiedene Prompts trennt gute von schlechten LLM-Labels zuverlässiger als die Selbstauskunft; bei einfachen Aufgaben lässt sich ein Teil auslagern, bei nuancierten Aufgaben kostet jede Auslagerung Qualität (S. 1492 bis 1494).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Bisherige Arbeiten vergleichen Mensch und LLM auf Aufgabenebene; CoAnnotating schätzt die Eignung des LLM pro Item. | S. 1488, Abschnitt 1; Abb. 1, S. 1487 | eigener Ansatz |
| LLMs schneiden bei NER, relationalem Schließen, affektiven Aufgaben und semantischer Ähnlichkeit schlechter ab als feinjustierte Baselines. | S. 1488 bis 1489, Abschnitt 2.2 | referiert |
| Weil LLMs empfindlich auf Prompt-Änderungen reagieren, wird jedes Item mit sieben Prompt-Typen befragt (Instruktion, vertauschte Reihenfolge, Paraphrase, Wahr/Falsch, Frage, Multiple Choice, Frage mit Bestätigungsfehler). | S. 1489, Abschnitt 3.1; Tab. 1 | eigenes Verfahren, Begründung referiert (Jang & Lukasiewicz 2023) |
| Je niedriger die Entropie über die Prompt-Varianten, desto höher die Übereinstimmung von ChatGPT mit dem menschlichen Gold; der Trend gilt auf allen sechs Datensätzen. | S. 1492, Abschnitt 5.1; Abb. 4, S. 1493 | eigenes Ergebnis |
| Selbstberichtete Konfidenz ist kein verlässlicher Schätzer: bei AG News haben 94,3 % der Items Konfidenz 0,8 bis 1; bei MRPC stimmen Items mit höherer Konfidenz sogar schlechter mit dem Gold überein. | S. 1492, Abschnitt 5.1 | eigenes Ergebnis |
| Bei festem LLM-Anteil liefert unsicherheitsgeleitete Aufteilung bessere Trainingsdaten als zufällige, z. B. TempoWiC bei 40 %: F1 56,9 gegen 53,2. Entropie ist meist besser als Selbstauskunft. | S. 1493, Abschnitt 5.1; Tab. 2 | eigenes Ergebnis |
| Bei einfachen Aufgaben (Themenklassifikation) lässt sich ohne Qualitätsverlust auslagern, z. B. 33 % Kostenersparnis bei AG News; bei Haltungserkennung und „Conversation Gone Awry" mindert jede Auslagerung die Qualität. | S. 1494, Abschnitt 5.2; Abb. 5 | eigenes Ergebnis |
| Hohe Unsicherheit bei Sarkasmus, unvollständigen Sätzen, Zahlenvergleichen und irreführenden Schlüsselwörtern. | S. 1494 bis 1495, Abschnitt 5.3; Tab. 3 | eigene qualitative Analyse |
| Wiederholung desselben Prompts liefert meist Entropie 0; ChatGPT ist innerhalb eines Prompts konsistent. Entropie über verschiedene Prompts trennt deutlich besser. | S. 1495, Abschnitt 5.4; Abb. 3, S. 1492 | eigenes Ergebnis (Ablation) |
| Grenzen: mögliche Datenlecks in den Trainingsdaten; menschliche Labels gelten als Gold; nur Klassifikation und nur Englisch. | S. 1495, Abschnitt 7 | Selbstauskunft |

## Daten, Methode, Zahlen

- **Datensätze (sechs, alle englisch, alle Klassifikation):** TREC und AG News (Thema), MRPC und TempoWiC (semantische Ähnlichkeit; TempoWiC: ob ein Zielwort in zwei Tweets dieselbe Bedeutung hat), Tweet Stance Detection (Thema Abtreibung) und Conversation Gone Awry (nuanciertes Verstehen) (S. 1491, Abschnitt 4.1). Bei großen Trainingsmengen ca. 1.000 Items geschichtet gezogen (S. 1491).
- **Gold:** die vorhandenen menschlichen Labels der Datensätze (S. 1492, 1495); keine Angabe zu ihrer Übereinstimmung.
- **LLM:** gpt-3.5-turbo; mehrdeutige Antworten („I cannot determine …") werden als eigene Klasse kodiert und erhöhen so die Unsicherheit; das Endlabel ist der Mehrheitswert über die Antworten (S. 1491). Nur EMNLP, Anhang A (S. 1499): Temperatur 0,7, top_p 0,95, max_tokens 800, API-Version „2023-03-15-preview".
- **Unsicherheit:** Selbstauswertung u = 1 minus mittlere selbst angegebene Konfidenz; Entropie über die relativen Häufigkeiten der k Antworten (S. 1490).
- **Bewertung:** RoBERTa-base auf den jeweils gemischten Labels feinjustiert, Makro-F1 auf Testdaten; Signifikanz gegen Zufallsaufteilung auf 10-%-Niveau (S. 1492; Tab. 2, S. 1493). Menschenkosten aus den Datensatzartikeln, sonst angenommen: 5 Annotator:innen je Item zu 15 USD/Stunde; LLM-Kosten 0,002 USD/1.000 Tokens (S. 1492).
- **Tab. 2 (S. 1493, am PDF geprüft), TempoWiC, Makro-F1 nach LLM-Anteil 0/20/40/60/80/100 %:** Zufall 57,5 / 55,9 / 53,2 / 46,2 / 50,3 / 42,0; Entropie (verschiedene Prompts) 57,5 / 58,4 / 56,9 / 55,9 / 53,8 / 42,0. Bei 100 % LLM-Labels liegt TempoWiC 15,5 Punkte unter rein menschlichen Labels.
- **„Bis zu 21 %" Verbesserung gegenüber Zufall (Abstract, S. 1487):** im Text nicht hergeleitet. Eigene Nachrechnung: TempoWiC bei 60 % ergibt 55,9 / 46,2 = 1,21; das ist vermutlich die gemeinte Stelle.

## Wörtliche Stellen

> „Such prior works view humans and LLMs as competitors, measuring the accuracy of LLM labels as a replacement for human annotation, rather than considering how humans and LLMs might collaborate in an efficient manner." (S. 1488)

> „we observe that ChatGPT's self-reported confidence scores (orange dots) are not consistently a good estimate for its annotation quality" (S. 1492)

> „For datasets requiring nuanced comprehensions like Stance Detection and Conversation Gone Awry, any level of outsourcing to the current version of ChatGPT compromises annotation quality." (S. 1494)

## Bezug zur Dissertation

- **Protokoll 4.10 (Freeze 2: Anzahl der Läufe pro Item, Prompt):** Die Ablation (S. 1495) zeigt, dass mehrere Läufe mit demselben Prompt kaum Streuung erzeugen, Prompt-Varianten dagegen schon. Wer im Protokoll Unsicherheit des LLM messen will, sollte Prompt-Varianten festlegen, nicht nur Wiederholungen; vgl. dagegen den Konsistenzwert bei Pangakis et al. (Wiederholung bei Temperatur über 0).
- **Protokoll 5, Punkt 5 (Reihenfolge der Karten zufällig mischen):** Der Prompt-Typ „vertauschte Reihenfolge" (Tab. 1, S. 1489) behandelt dieselbe Empfindlichkeit beim LLM; die Kartenreihenfolge im LLM-Prompt sollte wie bei den Menschen gemischt und protokolliert werden.
- **Protokoll 9.2 (Auswertung LLM gegen Gold):** Entropie bzw. Konsistenz ist als Kovariate in der Auswertung nützlich (welche Items sind für das LLM unsicher, und stimmen sie mit `KONTEXT_UNZUREICHEND` oder niedriger menschlicher Sicherheit überein?). Die Selbstauskunft des Modells taugt nach S. 1492 nicht dafür.
- **Nähe zur WSD:** TempoWiC ist die einzige bedeutungsbezogene Aufgabe. Dort sinkt das Makro-F1 mit 100 % LLM-Labels von 57,5 auf 42,0 (Tab. 2, S. 1493), und in Tab. 3 (S. 1494) ist ein Bedeutungsurteil eines der hoch unsicheren Beispiele. Das ist ein Hinweis, kein Beleg, dass Bedeutungsurteile zu den für LLMs schwierigen Aufgaben gehören.
- **Forschungsfrage (Protokoll 1):** Die Arbeit bewertet über einen nachgelagerten Klassifikator und Kosten, nicht über direkte Übereinstimmung mit Gold. Für den gepaarten Vergleich LLM gegen MFS am Gold ist die Methode nicht übertragbar; übertragbar ist nur die Idee, Items nach LLM-Unsicherheit für menschliche Prüfung auszuwählen, und das ist für eine spätere Anwendung auf D0 (Protokoll 3) relevant, nicht für den Goldstandard selbst.

## Grenzen und Einwände

- Nur Englisch, nur Klassifikation, nur ein Modell (S. 1495).
- Die Qualität wird indirekt über RoBERTa gemessen; die direkte Übereinstimmung von ChatGPT mit dem Gold steht nur als Streudiagramm ohne Zahlenwerte (Abb. 4, S. 1493).
- Das Gold sind vorhandene Datensatzlabels ohne berichtete Übereinstimmung; die Autor:innen nennen das selbst als Grenze (S. 1495).
- Kosten sind nur monetär; die Menschenkosten beruhen teils auf einer Annahme (5 Annotator:innen, 15 USD/Stunde; S. 1492).
- Die Angabe „bis zu 21 %" im Abstract ist nicht im Text hergeleitet (siehe oben).
- Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar: gering. Die Kategorien sind fest und für alle Items gleich; bei WSD wechselt das Inventar mit jedem Lemma, und die Entropie über Sense-Karten wäre zwischen Lemmata mit 2 und 15 Senses nicht direkt vergleichbar (Folgerung, nicht in der Arbeit).

## Weiterführend

- Loureiro et al. 2022, TempoWiC (S. 1491): Bedeutungswandel in Tweets, der WSD-nächste Datensatz der Studie.
- Jang & Lukasiewicz 2023, Konsistenzanalyse von ChatGPT (S. 1489).
- Wang et al. 2021, „Want to reduce labeling cost? GPT-3 can help", Zuweisung über Logits (S. 1488, 1490).
- Kadavath et al. 2022 und Lin et al. 2022, Selbsteinschätzung von Sprachmodellen (S. 1490).
- Kang, Xu & Ritter 2023, Distill or annotate, Kosten-Nutzen von Annotation (S. 1491).
- Kuzman et al. 2023, ChatGPT für Genre-Erkennung in Slowenisch (S. 1488).
