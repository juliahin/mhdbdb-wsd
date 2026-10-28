# Bhat & Varma 2023: LLMs as Annotators for Low-Resource Languages

**Datei:** `pdf/Bhat-Varma-2023-LLMs-as-Annotators.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, Volltext (8 Seiten) und Tabellen am PDF gelesen, Bibliografie an der ACL Anthology geprüft.

**Seitenzählung:** Das PDF ist die Verlagsfassung mit gedruckten Seiten 100 bis 107; PDF-Seite = gedruckte Seite minus 99.

## Bibliografie

- **Vollständig:** Bhat, Savita & Vasudeva Varma, 2023. Large Language Models As Annotators: A Preliminary Evaluation For Annotating Low-Resource Language Content. In *Proceedings of the 4th Workshop on Evaluation and Comparison of NLP Systems (Eval4NLP 2023)*, 100 bis 107. Association for Computational Linguistics. November 2023.
- **DOI/URL:** https://doi.org/10.18653/v1/2023.eval4nlp-1.8 (löst auf https://aclanthology.org/2023.eval4nlp-1.8 auf; Anthology-Eintrag am 2026-10-28 gelesen). ✔ Der Kopf des PDF nennt dieselben Seiten und „November 1, 2023" (S. 100).
- **Art:** Workshop-Beitrag (ACL-Workshop, im Kopf als Proceedings-Beitrag ausgewiesen; Begutachtungsverfahren des Workshops nicht im PDF beschrieben)
- **Sprache:** Englisch

## Worum es geht

Die Arbeit prüft, ob mehrsprachige LLMs menschliche Annotation in ressourcenarmen indischen Sprachen ersetzen oder unterstützen können (S. 100). Drei Modelle (ChatGPT/gpt-3.5-turbo, mT0-large, BLOOMZ-1b1) annotieren zero-shot mit englischen Prompts drei öffentliche IndicGLUE-Datensätze neu: Sentimentanalyse, Nachrichtenkategorien und Winograd-NLI, in bis zu 11 Sprachen (S. 101 bis 103). Verglichen wird mit den vorhandenen Labels als „ground truth" (S. 103). Ergebnis: Sentiment gelingt gut, Nachrichtenklassifikation und Inferenz schlecht; die Leistung schwankt stark zwischen Aufgaben und Sprachen, und feinjustierte Baselines sind meist besser (S. 101, 105).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Annotation in ressourcenarmen Sprachen ist teurer, weil Daten und menschliche Expert:innen fehlen. | S. 100, Abstract und Abschnitt 1 | Ausgangsthese |
| Die Leistung der LLMs ist nicht einheitlich, sondern schwankt über Aufgaben und Sprachen; das verlangt klarere Prompts. | S. 101, Beobachtung 2 | eigenes Ergebnis |
| Feinjustierte Baselines sind in den meisten Sprachen und Aufgaben überlegen. | S. 101, Beobachtung 3 | eigenes Ergebnis (Baselinewerte aus Doddapaneni et al. 2023 und Kakwani et al. 2020 übernommen, S. 103) |
| Sentiment: alle drei LLMs gut; BLOOMZ in 9 von 11 Sprachen gleichauf mit oder besser als die Baselines; ChatGPT meist schwächstes LLM. | S. 103, Abschnitt 4; Tab. 1, S. 103 | eigenes Ergebnis |
| Nachrichtenkategorien: „multi-class problem with a very fuzzy class separation"; alle LLMs bleiben hinter den Baselines und reproduzieren die menschlichen Labels nicht. | S. 104, Abschnitt 4; Tab. 2, S. 105 | eigenes Ergebnis |
| Die Nachrichtenlabels sind verrauscht; manche Texte passen zu mehreren Kategorien; nur ChatGPT schlägt Kategorien außerhalb der Vorgabe vor, die sich bei manueller Prüfung als relevant erweisen. | S. 104 | eigenes Ergebnis (manuelle Prüfung, Umfang nicht angegeben) |
| ChatGPT vergibt bei Sentiment zusätzlich „neutral", obwohl nur positiv/negativ vorgesehen ist; bei manueller Prüfung sind diese Texte tatsächlich neutral. | S. 103 bis 104 | eigenes Ergebnis (Umfang der Prüfung nicht angegeben) |
| Inferenz (WNLI) ist für alle Modelle und Baselines schwer; Aufgaben, die Sprachverständnis und Schlussfolgern verlangen, zeigt keines der LLMs in einer indischen Sprache außer Hindi. | S. 104 | eigenes Ergebnis |
| Die geringe Vertretung der Sprachen in CommonCrawl erklärt das begrenzte Sprachverständnis; trotz Verwandtschaft (dravidisch, indoarisch) unterscheiden sich die Werte deutlich, was für die Abhängigkeit von der Trainingsexposition spricht. | S. 104 | Deutung der Autor:innen |
| Begründungen, die nur ChatGPT liefert, helfen, Annotationsentscheidungen zu verstehen und Annotator:innen zu schulen. | S. 101, 104 bis 105 | eigene Beobachtung |
| Einfache Aufgaben wie Sentiment lassen sich mit LLMs nachbilden; für ressourcenarme Aufgaben mit Sprachverständnis und Schlussfolgern sind LLMs als Annotatoren noch nicht brauchbar. | S. 105, Abschnitt 5 | Fazit |

## Daten, Methode, Zahlen

- **Modelle:** ChatGPT (gpt-3.5-turbo, API mit Standardeinstellungen, abgefragt 5. bis 6. September 2023), mT0-large, BLOOMZ-1b1 (wegen Infrastruktur nur kleine Varianten) (S. 101, 103).
- **Sprachen:** 11 indische Sprachen; Hindi als mittlere, Punjabi, Oriya und Assamesisch als extrem ressourcenarm, die übrigen als ressourcenarm eingestuft (S. 101 bis 102).
- **Datensätze (IndicGLUE):** IndicSentiment (laut Datensatzkarte von Expert:innen annotiert, Texte in die indischen Sprachen übersetzt); News Category Classification (Kategorien laut Autor:innen vermutlich aus den URLs der Nachrichtenseiten); WNLI (von Expert:innen übersetzt und geprüft, nur mr, hi, gu) (S. 102).
- **Prompts:** englisch, aus PromptSource ausgewählt, zero-shot; Kontext in der Zielsprache (S. 102 bis 103).
- **Stichprobe:** Test-Splits; WNLI 284 Items, NewsCLS 5.986, Sentiment 2.862 zufällig gezogene Items (ca. 250 pro Sprache, aus Budgetgründen) (S. 103).
- **Maße:** gewichtete Precision, Recall, F1 (sklearn) und Makro-Mittel über Sprachen (S. 103). Keine Angabe zur Übereinstimmung der ursprünglichen Annotator:innen.
- **Tab. 4 (S. 105, am PDF geprüft), korrekt gelabelte Items, Makro-Mittel über Sprachen:** Sentiment mT0 89,8 %, BLOOMZ 93,4 %, ChatGPT 83,8 %; NewsCLS 32,1 %, 38,9 %, 51,4 %; WNLI 38,8 %, 47,7 %, 40,6 %.
- **Tab. 2 (S. 105), gewichtetes F1 NewsCLS, Beispiele:** Hindi mT0 0,076 / BLOOMZ 0,18 / ChatGPT 0,53 / IndicBERT 0,74; Telugu ChatGPT 0,10.
- **Tab. 3 (S. 105), WNLI gewichtetes F1:** ChatGPT 0,406 in allen drei Sprachen; mBERT und IndicBERT je 0,56.

## Wörtliche Stellen

> „The results show that off-the-shelf use of multilingual LLMs is not appropriate and results in poor performance in two of the three tasks." (S. 100, Abstract)

> „These tasks require a certain degree of language understanding and reasoning capability, which none of the three LLMs demonstrate in any Indic language except Hindi." (S. 104)

> „We note that the annotations for this dataset are noisy, and a few records can be assigned to multiple categories instead of just one category." (S. 104)

## Bezug zur Dissertation

- **Forschungsfrage (Protokoll 1) und Grenzen der LLM-Annotation bei ressourcenarmen Sprachen:** stützt die Erwartung, dass Leistung an der Vertretung der Sprache im Training hängt (S. 104). Mittelhochdeutsch ist in diesem Sinn ressourcenarm, aber anders als die indischen Sprachen hier eine historische Stufe einer stark vertretenen Sprache. Die Arbeit sagt dazu nichts; das bleibt eine offene Übertragungsfrage.
- **Protokoll 6 (Ausweichlabels `MEHRERE`, `KEINE_PASST`) und A6:** Die Beobachtungen zu „neutral" (S. 103 bis 104) und zu Texten mit mehreren passenden Kategorien (S. 104) zeigen, dass ein erzwungenes geschlossenes Labelset die Messung verzerrt: Das LLM wird für eine sachlich plausible Antwort als falsch gezählt. Das stützt die Statusliste mit Ausweichlabels und die getrennte Behandlung in 9.2.
- **Protokoll 2 und 9.2 (Gold gegen Silber):** Die Arbeit nimmt vorhandene Labels ungeprüft als „ground truth", obwohl sie bei NewsCLS vermutlich aus URLs stammen (S. 102) und als verrauscht beschrieben werden (S. 104). Das ist genau die Konstellation, die das Protokoll mit der Trennung von Silber und neuem Gold vermeidet (A1).
- **Protokoll 4.10 (Freeze 2, LLM-Konfiguration):** Standardeinstellungen, ein Lauf, keine Versionsangabe über den Modellnamen hinaus außer dem Abfragedatum (S. 101, 103). Als Negativbeispiel für die geplante Dokumentation von Modell, Version, Temperatur und Läufen brauchbar.

## Grenzen und Einwände

- Selbst als „preliminary" bezeichnet; die Autor:innen räumen ein, dass mehr methodische Strenge nötig ist, nur Teilmengen genutzt und teils übersetzte Daten verwendet wurden (S. 105, Limitations).
- Die offenen Modelle sind sehr klein (mT0-large, BLOOMZ-1b1; S. 103); Aussagen über „LLMs" gelten nur für diese Konfigurationen und gpt-3.5-turbo vom September 2023.
- Die Qualität des Golds ist ungeprüft; keine Annotator-Übereinstimmung berichtet. Bei NewsCLS beruhen die Labels nach Annahme der Autor:innen auf URLs (S. 102).
- Text und Tabellen widersprechen sich an mehreren Stellen (am PDF geprüft):
  - S. 104: Bei WNLI scheine nur ChatGPT über Zufall zu liegen; Tab. 4 (S. 105) zeigt BLOOMZ mit 47,7 % vor ChatGPT mit 40,6 %, und alle drei Werte liegen bei einer zweiwertigen Aufgabe unter 50 %.
  - S. 104: ChatGPT sei bei NewsCLS in 6 von 7 Sprachen das beste LLM; nach Tab. 2 (S. 105) liegt es in 5 von 7 vorn (bei Malayalam hat mT0 0,739 gegen 0,68, ist aber nicht rot markiert; bei Telugu liegt BLOOMZ vorn).
- ChatGPT wird für die Wahl von „neutral" als falsch gezählt, obwohl die manuelle Prüfung ihm recht gibt (S. 103 bis 104); die Zahlen unterschätzen ChatGPT bei Sentiment damit in unbekanntem Umfang.
- Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar: gering. Keine lexikalische Semantik, keine historische Sprache, Klassifikation auf Satz- oder Textebene, englische Prompts.

## Weiterführend

- Kuzman, Mozetič & Ljubešić 2023, ChatGPT für Genre-Erkennung, u. a. Slowenisch (S. 100).
- Lai et al. 2023, ChatGPT jenseits des Englischen, mehrsprachige Evaluation und Einstufung der Ressourcenlage (S. 100 bis 101).
- Kakwani et al. 2020, IndicNLPSuite und IndicGLUE (S. 102).
- Doddapaneni et al. 2023, IndicSentiment und Baselines (S. 102 bis 103).
- Huang, Kwak & An 2023, Begründungen von ChatGPT bei impliziter Hassrede (S. 105).
