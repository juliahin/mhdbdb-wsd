# Liu et al. 2019: RoBERTa

**Datei:** `pdf/Liu-etal-2019-RoBERTa.pdf` (nur lokal; 13 Seiten, arXiv 1907.11692v1 vom 26.07.2019)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganze Textebene gelesen, Tab. 4 am Seitenbild geprüft, Publikationsstatus geprüft. Priorität 3: bewusst knapp, nur was für WSD mit kontextualisierten Repräsentationen und einen späteren Feinabstimmungsvergleich zählt. Keine Markierungen im PDF (keine Anmerkungsebene).

Seitenzählung: Das PDF hat keine gedruckten Seitenzahlen; angegeben sind PDF-Seiten.

## Bibliografie

- **Vollständig:** Liu, Yinhan; Ott, Myle; Goyal, Naman; Du, Jingfei; Joshi, Mandar; Chen, Danqi; Levy, Omer; Lewis, Mike; Zettlemoyer, Luke; Stoyanov, Veselin (2019). RoBERTa: A Robustly Optimized BERT Pretraining Approach. arXiv:1907.11692 [cs.CL].
- **DOI/URL:** https://doi.org/10.48550/arXiv.1907.11692; Modelle und Code laut Paper https://github.com/pytorch/fairseq (S. 1, nicht aufgerufen).
- **Art:** Preprint. Geprüft am 2026-10-28: arXiv führt nur v1 ohne Journal-Angabe; Crossref kennt keine Verlagsfassung unter diesem Titel; im Suchindex von OpenReview steht eine Einreichung zu ICLR 2020 (Blind Submission, ID `SyxS0T4tvS`) ohne Venue-Angabe sowie ein dblp-Datensatz nur als „CoRR 2019“. Die Entscheidung zur ICLR-Einreichung war nicht abrufbar (OpenReview verlangte eine Browserprüfung). Eine begutachtete Fassung ist also nicht nachgewiesen.
- **Sprache:** Englisch

## Worum es geht

Eine Replikationsstudie des BERT-Vortrainings: Die Autor:innen variieren Maskierung, Eingabeformat mit und ohne Next Sentence Prediction, Batchgröße, Tokenisierung, Datenmenge und Trainingsdauer bei gleicher Architektur (S. 1, 4 bis 6). Ihr Befund: BERT war „significantly undertrained“ (S. 1). Die kombinierte Rezeptur RoBERTa erreicht mit derselben Architektur und demselben Masked-LM-Ziel wie BERT-Large Bestwerte auf GLUE, SQuAD und RACE (S. 6 bis 9).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Vergleiche zwischen Vortrainingsverfahren sind schwierig, weil Training teuer ist, oft auf privaten Daten unterschiedlicher Größe läuft und Hyperparameter die Ergebnisse stark beeinflussen. | S. 1, Abstract und Abschnitt 1 | Problemstellung |
| Dynamische Maskierung ist gleich gut oder etwas besser als statische. | S. 4, Abschnitt 4.1, Tab. 1 | eigenes Ergebnis |
| Next Sentence Prediction wegzulassen erhält oder verbessert die Leistung, im Gegensatz zu Devlin et al. (2019); einzelne Sätze statt längerer Segmente schaden. | S. 5, Abschnitt 4.2, Tab. 2 | eigenes Ergebnis |
| Große Batches verbessern Perplexität und Endaufgaben bei gleichem Rechenaufwand. | S. 5 bis 6, Abschnitt 4.3, Tab. 3 | eigenes Ergebnis |
| Byte-BPE mit 50.000 Einheiten statt WordPiece-artigem BPE mit 30.000: etwas schlechter auf einigen Aufgaben, aber ohne unbekannte Tokens; genommen wegen der universellen Kodierung. | S. 6, Abschnitt 4.4 | eigenes Ergebnis und Entscheidung |
| Mehr Daten (16 → 160 GB) und längeres Training (100K → 500K Schritte) verbessern alle Endaufgaben; auch das längste Training scheint nicht überangepasst. | S. 7, Abschnitt 5, Tab. 4 | eigenes Ergebnis |
| Dass RoBERTa mit gleicher Architektur und gleichem Ziel BERT-Large und XLNet-Large übertrifft, wirft Fragen nach dem Gewicht von Architektur und Ziel gegenüber „more mundane details like dataset size and training time“ auf. | S. 8, Abschnitt 5.1 | Schlussfolgerung |

## Daten, Methode, Zahlen

- **Daten (S. 3):** fünf englische Korpora, zusammen über 160 GB: BookCorpus plus Wikipedia (16 GB), CC-News (76 GB, 63 Mio. Nachrichtenartikel 2016 bis 2019), OpenWebText (38 GB), Stories (31 GB).
- **Training (S. 3, 7):** Reimplementierung in fairseq; nur volle Sequenzen bis 512 Tokens; empfindlich gegenüber dem Adam-Epsilon. RoBERTa-Large (24 Schichten, 1024, 16 Köpfe, 355 Mio. Parameter) auf 1024 V100-GPUs ca. einen Tag für 100K Schritte (S. 7).
- **Tab. 4 (S. 7), Dev-Ergebnisse:** RoBERTa mit Books + Wiki, 100K Schritte: SQuAD 93,6/87,3, MNLI-m 89,0, SST-2 95,3; mit 160 GB und 500K Schritten 94,6/89,4, 90,2, 96,4; BERT-Large zum Vergleich 90,9/81,8, 86,6, 93,7 (am Seitenbild geprüft).
- **Feinabstimmung GLUE (S. 7):** Batch 16 oder 32, Lernrate 1e-5 bis 3e-5, 10 Epochen mit Early Stopping, Median über fünf Läufe.
- **GLUE-Leaderboard:** 88,5 Punkte, Bestwert auf 4 von 9 Aufgaben (S. 1, 8, Tab. 5; Stand 25.07.2019).
- WSD wird nicht evaluiert. Ein Satz zu „pronoun disambiguation datasets“ betrifft WNLI (S. 8, Anm. 10), nicht Wortbedeutungen.

## Wörtliche Stellen

> „We find that BERT was significantly undertrained, and can match or exceed the performance of every model published after it.“ (S. 1)

> „This raises questions about the relative importance of model architecture and pretraining objective, compared to more mundane details like dataset size and training time that we explore in this work.“ (S. 8)

## Bezug zur Dissertation

- **Späterer Feinabstimmungsvergleich:** RoBERTa ist das stärkere Encoder-Rezept gleicher Architektur wie BERT; der Befund, dass Daten, Trainingsdauer und Hyperparameter das Ergebnis tragen (S. 1, 7 bis 8), heißt für einen Vergleich mit feinabgestimmten Modellen: deren Konfiguration genauso festschreiben wie die LLM-Konfiguration in Freeze 2 (PROTOKOLL §4.10), sonst ist ein Unterschied nicht deutbar.
- **Reproduzierbarkeit:** Das Paper benennt Varianz durch Seeds und meldet Mediane über fünf Läufe (S. 4, 7). Das ist das Vorbild für mehrere Läufe pro Item bzw. pro Konfiguration, falls feinabgestimmte Modelle verglichen werden.
- **Mittelhochdeutsch:** nur englische Daten (S. 3). Byte-BPE vermeidet unbekannte Tokens (S. 6), was bei historischen Schreibvarianten hilft; über Qualität der Repräsentation für Mhd. sagt das nichts.
- Keine Folgen für Goldstandard, IAA oder Stichprobe.

## Grenzen und Einwände

- Nicht begutachtet nachgewiesen (siehe Bibliografie); als Preprint zitieren.
- Daten- und Diversitätseffekte sind vermischt, wie die Autor:innen selbst sagen (S. 7, Anm. 9).
- Nur Englisch, nur Benchmarks des Sprachverstehens; keine WSD-Aufgabe.

## Weiterführend

- Devlin et al. 2019, BERT (Zusammenfassung im selben Ordner): die replizierte Arbeit.
- Yang et al. 2019, XLNet (S. 1 bis 8): der Vergleichspunkt der Arbeit.
