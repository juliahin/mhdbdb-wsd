# Beck & Köllner 2023: GHisBERT

**Datei:** `pdf/Beck-Koellner-2023-GHisBERT.pdf` (nur lokal; 13 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, ganze Textebene gelesen, Tabellen 1 bis 3 und Abb. 1 am Seitenbild geprüft, Julias Markierungen abgeglichen, DOI aufgelöst.

Seitenzählung: PDF-Seite n = gedruckte S. 32 + n (PDF 1 = S. 33, PDF 13 = S. 45). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Beck, Christin & Marisa Köllner (2023). GHisBERT – Training BERT from scratch for lexical semantic investigations across historical German language stages. In: Nina Tahmasebi, Syrielle Montariol, Haim Dubossarsky, Andrey Kutuzov, Simon Hengchen, David Alfter, Francesco Periti & Pierluigi Cassotti (Hg.), *Proceedings of the 4th Workshop on Computational Approaches to Historical Language Change (LChange 2023)*. Singapore: Association for Computational Linguistics, S. 33 bis 45.
- **DOI/URL:** https://doi.org/10.18653/v1/2023.lchange-1.4 (aufgelöst auf https://aclanthology.org/2023.lchange-1.4; Herausgeber:innen, Ort, Monat Dezember und Seiten dort ✔). Kopfzeile S. 33: „pages 33–45, December 6, 2023“ ✔.
- **Art:** Workshop-Beitrag (ACL-Workshop LChange)
- **Sprache:** Englisch
- **Modell und Code** laut Paper: https://huggingface.co/christinbeck/GHisBERT (S. 36, Anm. 4), https://github.com/christinschaetzle/GHisBERT (S. 37, Anm. 10). Nicht aufgerufen.

## Worum es geht

Die Autorinnen trainieren ein BERT-Modell von Grund auf mit Daten aller Sprachstufen des Deutschen ab dem Althochdeutschen (S. 33 bis 34, 36). Weil es für Bedeutungswandel über Sprachstufen hinweg keine Golddaten gibt, prüfen sie das Modell indirekt: Für zehn stabile Swadesh-Begriffe messen sie Kosinusähnlichkeiten zwischen Begriffen je Sprachstufe und desselben Begriffs über Mhd., Frnhd. und Nhd. (S. 37 bis 38). GHisBERT bildet die Unterschiede zwischen Begriffen deutlicher ab als ein unverändertes und ein historisch nachtrainiertes modernes BERT (S. 38 bis 41). Die fehlende Goldannotation nennen sie selbst als stärkste Einschränkung (S. 41).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Es sei unklar, wie gut Sprachmodelle auf Untersuchungen skalieren, die weiter zurückreichen, wo die Sprache stark von den Trainingsdaten abweicht. | S. 33, Abstract | Problemstellung |
| GHisBERT ist von Grund auf mit Daten trainiert, die alle belegten Stufen des Deutschen abdecken: Ahd. (ca. 750 bis 1050), Mhd. (ca. 1050 bis 1350), Frnhd. (ca. 1350 bis 1650), Nhd. (ab 1650). | S. 34, Abschnitt 1; S. 36, Abschnitt 3 | eigenes Modell |
| Frühere historische Modelle (HistBERT, MacBERTh, GysBERT, hmBERT) decken nur jüngere Stufen ab; hmBERT enthält Deutsch nur von 1683 bis 1949. | S. 35 bis 36, Abschnitt 2.3; S. 37 | referiert |
| **Abdeckung:** „To our knowledge, there exists no contextualized language model which covers the historical stages of German which we investigate in the present study.“ | S. 36, Ende Abschnitt 2.3 | Einschätzung der Autorinnen, Stand 2023 |
| Mhd. Trainingsdaten: alle Sätze aus dem Referenzkorpus Mittelhochdeutsch (ReM, Klein et al. 2016), 245.880 Sätze, 2,3 Mio. Wörter. | S. 36, Abschnitt 3.1, Tab. 1 | Datenbeschreibung |
| Satztrennung über moderne Satzzeichen und historische Grenzzeichen wie den Mittelpunkt, nach den Korpusrichtlinien; die Autorinnen räumen ein, dass das für historisches Deutsch nicht immer stimmt. | S. 36, Anm. 6 | Methode |
| Eigener Tokenizer, auf den historischen Daten trainiert, für alle Modelle verwendet. | S. 37 | Methode |
| Vergleichsmodelle: BERT-german (dbmdz, über 2 Mrd. Wörter Gegenwartssprache) und BERT-fine (BERT-german mit denselben historischen Daten weitertrainiert, 4 Epochen). | S. 36 | Methode |
| Bewertung ohne Gold: „there exists yet no gold data that goes back far enough in time“; stattdessen t-Tests und manuelle Sichtung von 50 zufälligen Sätzen pro Begriff und Sprachstufe. | S. 38, Abschnitt 4.6 | Methode |
| GHisBERT: Ähnlichkeiten zwischen Begriffen von 0,18 bis 1; BERT-german 0,87 bis 1, „not being able to capture the differences between the concepts“. | S. 38 bis 39, Abb. 1 | eigenes Ergebnis |
| Über die Zeit: Bei allen drei Modellen unterscheidet sich die Ähnlichkeit eines Begriffs mit sich selbst signifikant von der mit anderen Begriffen. GHisBERT und BERT-fine unterscheiden sich in COS_avg nicht signifikant, beide signifikant von BERT-german (p < 0,001). | S. 39, Tab. 2 | eigenes Ergebnis |
| Nur GHisBERT schätzt den Abstand Mhd. zu Frnhd. größer als Frnhd. zu Nhd. (COS_ME signifikant verschieden von beiden anderen Modellen, p < 0,001), im Einklang mit der Sprachgeschichte. | S. 39 | eigenes Ergebnis, Deutung referiert (Nübling et al. 2008) |
| Qualitativ: *vuoz* und *visch* zeigen in allen Stufen Polysemie; *kopf* im Mhd. überwiegend ‘Trinkgefäß’. EI kommt im Mhd.-Teil nur in lateinischen Texten vor (*ei* ‘er’). | S. 39 bis 40 | eigene Beobachtung |
| Schluss: Vortraining von Grund auf mit den relevanten historischen Daten liefert angemessenere Ergebnisse als bloßes Nachtrainieren. | S. 41, Abschnitt 6 | eigenes Ergebnis |
| Limitations: Fehlendes Gold ist „the strongest limitation“; historische Daten zu annotieren sei „notoriously difficult and time-consuming, requiring expert knowledge“. Offen, wie neuere LLMs wie GPT-4 auf die Aufgabe skalieren. | S. 41 | Selbsteinschätzung |

## Daten, Methode, Zahlen

- **Trainingsdaten (Tab. 1, S. 36, am Seitenbild geprüft):** ReA Ahd. 750 bis 1050, 3.227 Sätze, 18.424 Wörter; **ReM Mhd. 1050 bis 1350, 245.880 Sätze, 2,3 Mio. Wörter**; ReF Frnhd. 1350 bis 1650, 106.988 Sätze, 3,7 Mio.; DTA1 1400 bis 1599, DTA2 1600 bis 1799, DTA3 1800 bis 1999 je 100.000 zufällig gezogene Sätze (2,6 / 2,1 / 1,6 Mio. Wörter); zusammen 656.095 Sätze, 12,3 Mio. Wörter. Das Paper nennt keine ReM-Version außer „Version 1.0“ in der Literatur (Klein et al. 2016, S. 42) und keine Auswahl oder Gewichtung nach Text oder Gattung.
- **Training (S. 36):** BERT-base-Konfiguration, 12 Schichten, Hidden Size 768, 12 Attention Heads, max. Länge 512, Vokabular 32.000, MLM, 10 Epochen, Batch 8 mit Gradient Accumulation. BERT-fine: gleiche Parameter, 4 Epochen.
- **Experiment (S. 37 bis 38):** zehn Begriffe aus der Swadesh-Liste (VOGEL, HUND, EI, FISCH, BERG, FUSS, KOPF, FRAU, BAUM, SONNE); historische Formen über „etymologische Ketten“ aus Kluge (2012), in lemmatisierten Korpora gesucht, Sätze in nicht lemmatisierter Form; Zielwort durch das nhd. Lemma ersetzt; Einbettung aus der vorletzten Schicht, Wortstücke gemittelt; Ahd. ausgeschlossen, weil zu selten (Anm. 11).
- **Satzzahlen im Experiment:** Text S. 37: 148.306 Sätze, davon 3.942 Mhd., 6.009 Frnhd., 138.355 Nhd. **Widerspruch im Werk:** Tab. 3 (S. 45, am Seitenbild geprüft) führt 3.942 in der Spalte NHG (mit den Formen *Baum*, *Berg* …) und 138.355 in der Spalte MHG (mit *boum*, *berc*, *vuoz* …); die Spaltensumme NHG ergibt nachgerechnet 3.942. Text und Tabelle widersprechen sich also in der Zuordnung; aus dem PDF ist nicht zu entscheiden, welche Angabe stimmt. Außerdem Druckfehler „3 7702“ für *vro(u)we* (Zeilensumme 42.687 passt zu 37.702).
- **Tab. 2 (S. 39):** COS_avg GHisBERT 0,81 (EI) bis 0,95 (BERG, FRAU); BERT-german 0,96 bis 0,99.

## Wörtliche Stellen

> „To our knowledge, there exists no contextualized language model which covers the historical stages of German which we investigate in the present study.“ (S. 36)

> „The lack of a gold standard for evaluation is the strongest limitation of our paper, leading to a lack of a true quantitative evaluation. Annotating data from historical language stages is notoriously difficult and time-consuming, requiring expert knowledge of the language stages“ (S. 41)

> „[…] it remains unclear how well more recent large language models, e.g., GPT-4 (OpenAI, 2023), and different model architectures scale to the task of investigating LSC across language stages“ (S. 41)

## Bezug zur Dissertation

- **Prüfauftrag „einziges Modell, das ausdrücklich Mittelhochdeutsch abdeckt“:** Das Paper sagt für sich nur, nach Kenntnis der Autorinnen gebe es kein kontextualisiertes Modell für die untersuchten historischen Stufen (S. 36), und es sei die erste Untersuchung dieser Art über Sprachstufen hinweg (S. 38, 41). Das ist eine Aussage von 2023 mit dem Vorbehalt „to our knowledge“. Eine Gegenwartsaussage „das einzige Modell“ stützt das Paper nicht; ob seither weitere Modelle Mhd. abdecken, ist nicht geprüft.
- **Mhd.-Abdeckung konkret:** Mhd. kommt ausschließlich aus dem ReM (S. 36), nicht aus der MHDBDB. Die mhd. Daten sind mit 2,3 Mio. von 12,3 Mio. Wörtern etwa ein Fünftel des Trainings (Tab. 1).
- **PROTOKOLL §9.2, Abschnitt „Ausweichlabels als Ergebnis“ und `LITERATUR-IAA.md` „Lücke“:** Das Paper bestätigt aus Sicht der Modellentwicklung, dass für historisches Deutsch Golddaten zur lexikalischen Semantik fehlen und die Annotation Expertise verlangt (S. 38, 41). Das stützt die Begründung, warum ein doppelt annotierter mhd. Goldstandard ein eigener Beitrag ist.
- **PROTOKOLL §1 (LLM gegen MFS):** GHisBERT ist kein LLM und kein WSD-System; das Paper benennt selbst offen, wie LLMs auf historische Sprachstufen skalieren (S. 41). Als Vergleichsmodell für die Dissertation käme es nur als Einbettungs-Baseline in Frage; das wäre eine eigene Entscheidung, das Paper prüft WSD nicht.
- **Leckgefahr (§10, `knowledge/data.md` B1):** nicht berührt. ReM und MHDBDB können dieselben Werke enthalten; für die Dissertation spielt das nur eine Rolle, falls ein auf ReM trainiertes Modell eingesetzt wird.
- **Polysemie über Stufen:** Die Beobachtungen zu *vuoz*, *visch*, *kopf* (S. 40) sind Beispiele für mhd. Polysemie, aber aus einer Sichtung, nicht aus einer Annotation mit Inventar.

## Grenzen und Einwände

- Keine Evaluation gegen menschliche Urteile; „besser“ heißt hier: plausiblere Ähnlichkeitsmuster bei zehn als stabil angenommenen Begriffen (S. 38, 41).
- Zehn Begriffe, Ahd. ausgeschlossen; Häufigkeits-, Gattungs- und Dialekteffekte ausdrücklich nicht betrachtet (S. 41).
- Widersprüchliche Satzzahlen zwischen Text (S. 37) und Tab. 3 (S. 45), siehe oben.
- Der Befund zu EI (im Mhd. nur lateinisches *ei*) zeigt, dass gemischtsprachige Texte die Ergebnisse treiben können (S. 39); Lemma-Suche ohne Sprachfilter.
- Kein Bezug zu einem Bedeutungsinventar; Übertragbarkeit auf ein onomasiologisches Inventar wie das MHDBDB-Begriffssystem ungeprüft.

## Weiterführend

- Manjavacas & Fonteyn 2022b, Non-parametric word sense disambiguation for historical languages, NLP4DH, S. 123 bis 134: historische Modelle (MacBERTh, GysBERT) bei WSD besser als moderne (S. 35, 43). Für WSD-Forschungsstand nachschlagen.
- Manjavacas & Fonteyn 2022a, Adapting vs. Pre-training Language Models for Historical Languages, JDMDH (S. 35, 43).
- Beck, Booth, El-Assady & Butt 2020, Representation problems in linguistic annotations: Ambiguity, variation, uncertainty, error and bias, LAW 14, S. 60 bis 73 (S. 41, 42): einschlägig für `MEHRERE` und Unsicherheitsangaben (Protokoll §6).
- Schlechtweg et al. 2020, SemEval-2020 Task 1 (S. 33, 44).
- Klein, Wegera, Dipper & Wich-Reif 2016, ReM Version 1.0 (S. 42).

## Julias Markierungen im PDF

44 violette Hervorhebungen, keine Randnotizen (`md/Beck-Koellner-2023-GHisBERT.markierungen.md`). Sie konzentrieren sich auf: Skalierung auf ältere Sprachstufen (S. 33), Periodisierung (S. 34), HistBERT und hmBERT (S. 35), Trainingsdaten aus den Referenzkorpora, ReM, DTA, Satztrennung, Tab. 1 und BERT-german (S. 36), etymologische Ketten und Swadesh-Auswahl (S. 37), fehlende Golddaten (S. 38), Zusammenfassung der Ergebnisse (S. 40 bis 41) und die Limitations zu Gold, Annotationsaufwand und Rechenaufwand (S. 41). Alle markierten Kernstellen sind in Kernaussagen, Zahlen oder wörtliche Stellen aufgenommen; nicht übernommen sind nur Literaturhinweise ohne eigene Aussage (S. 33: Paul, Ullmann u. a.) und die Hugging-Face-Links (S. 36). Eine Markierung auf S. 36 liegt über keinem Text.
