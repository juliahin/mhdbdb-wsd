# Devlin et al. 2019: BERT

**Datei:** `pdf/Devlin-etal-2019-BERT.pdf` (nur lokal; 16 Seiten, arXiv 1810.04805v2 vom 24.05.2019). Seit 2026-10-29 liegt daneben die Verlagsfassung `pdf/Devlin-etal-2019-BERT-NAACL.pdf` (ACL Anthology, CC BY 4.0).
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganze Textebene der arXiv-Fassung gelesen, Tab. 7 am Seitenbild geprüft, Seitenumbrüche mit der NAACL-Fassung abgeglichen. Priorität 3: bewusst knapp, nur was für WSD mit kontextualisierten Repräsentationen und einen späteren Feinabstimmungsvergleich zählt. Keine Markierungen im PDF (keine Anmerkungsebene).

Seitenzählung: Die arXiv-Fassung trägt keine Seitenzahlen. Ihr Umbruch stimmt mit der NAACL-Fassung überein (Seitenanfänge verglichen: Seiten 1 bis 15 gleich, auf Seite 16 beginnt die arXiv-Fassung mit dem Rest eines Satzes aus Anhang B.1); daher gedruckte Seite = 4170 + PDF-Seite. Unten steht die gedruckte Seite, die PDF-Seite in Klammern.

## Bibliografie

- **Vollständig:** Devlin, Jacob; Chang, Ming-Wei; Lee, Kenton; Toutanova, Kristina (2019). BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding. In: Jill Burstein, Christy Doran, Thamar Solorio (Hg.), *Proceedings of the 2019 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 1 (Long and Short Papers)*. Minneapolis, Minnesota: Association for Computational Linguistics, S. 4171 bis 4186.
- **DOI/URL:** https://doi.org/10.18653/v1/N19-1423, https://aclanthology.org/N19-1423/ (Herausgeber:innen, Ort, Monat Juni, Seiten und Lizenz CC BY 4.0 dort ✔; Kopfzeile der NAACL-PDF „Proceedings of NAACL-HLT 2019, pages 4171–4186“ ✔). arXiv 1810.04805 hat v1 (11.10.2018) und v2 (24.05.2019).
- **Art:** begutachteter Konferenzbeitrag (NAACL-HLT 2019, laut Anthology Best Long Paper)
- **Sprache:** Englisch

## Worum es geht

BERT ist ein Transformer-Encoder, der mit zwei Aufgaben auf unannotiertem Text vortrainiert wird: maskierte Wörter aus linkem und rechtem Kontext vorhersagen (Masked LM) und entscheiden, ob ein Satz auf einen anderen folgt (Next Sentence Prediction) (S. 4171, 4174 (PDF 1, 4)). Danach wird das ganze Modell mit einer kleinen Ausgabeschicht auf die Zielaufgabe feinabgestimmt (S. 4173 (PDF 3)). Das Paper berichtet neue Bestwerte auf elf englischen Aufgaben (GLUE, SQuAD, SWAG) und zeigt in Ablationen, dass Bidirektionalität und Modellgröße den Ausschlag geben (S. 4175 bis 4179 (PDF 5 bis 9)).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Zwei Wege, vortrainierte Repräsentationen zu nutzen: merkmalsbasiert (Repräsentationen als Zusatzmerkmale, z. B. ELMo) oder Feinabstimmung aller Parameter (z. B. GPT). | S. 4171 (PDF 1), Abschnitt 1 | Einordnung |
| BERT ist „jointly conditioning on both left and right context in all layers“; unidirektionale Modelle seien besonders für Token-Aufgaben nachteilig. | S. 4171 (PDF 1) | These, gestützt durch Ablation S. 4178 (PDF 8) |
| Jedes Token erhält eine kontextabhängige Endrepräsentation T_i; sie entsteht aus Token-, Segment- und Positionseinbettung. | S. 4174 (PDF 4), Abschnitt 3 | Modellbeschreibung |
| Ohne Next Sentence Prediction und nur von links nach rechts trainiert sinken die Werte deutlich (Tab. 5). | S. 4178 (PDF 8), Abschnitt 5.1 | eigenes Ergebnis |
| Größere Modelle verbessern auch sehr kleine Aufgaben, z. B. MRPC mit 3.600 Trainingsbeispielen. | S. 4178 (PDF 8), Abschnitt 5.2, Tab. 6 | eigenes Ergebnis |
| Merkmalsbasierte Nutzung funktioniert fast so gut wie Feinabstimmung: Bei NER liegt die Verkettung der vier obersten Schichten nur 0,3 F1 hinter der Feinabstimmung des ganzen Modells. | S. 4179 (PDF 9), Abschnitt 5.3, Tab. 7 | eigenes Ergebnis |
| Feinabstimmung von BERT-Large war auf kleinen Datensätzen manchmal instabil; deshalb mehrere Neustarts und Auswahl auf dem Dev-Set. | S. 4176 (PDF 6), Abschnitt 4.1 | eigenes Ergebnis |
| Große Datensätze (ab ca. 100.000 Beispielen) reagieren viel weniger empfindlich auf Hyperparameter als kleine. | S. 4184 (PDF 14), Anhang A.3 | eigene Beobachtung |

## Daten, Methode, Zahlen

- **Modelle (S. 4173 (PDF 3)):** BERT-Base 12 Schichten, Hidden Size 768, 12 Köpfe, 110 Mio. Parameter; BERT-Large 24/1024/16, 340 Mio.
- **Eingabe (S. 4174 (PDF 4)):** WordPiece mit 30.000 Einheiten; ein „Satz“ ist ein beliebiges zusammenhängendes Textstück.
- **Masked LM (S. 4174 (PDF 4); S. 4182 (PDF 12)):** 15 % der WordPiece-Tokens werden ausgewählt, davon 80 % durch [MASK], 10 % zufällig, 10 % unverändert ersetzt.
- **Vortrainingsdaten (S. 4175 (PDF 5)):** BooksCorpus (800 Mio. Wörter) und englische Wikipedia (2.500 Mio. Wörter), nur Fließtext; ausschließlich Englisch.
- **Feinabstimmung:** alle Ergebnisse in höchstens einer Stunde auf einer Cloud-TPU reproduzierbar (S. 4175 (PDF 5)); empfohlene Suchbereiche Batchgröße 16/32, Lernrate 5e-5/3e-5/2e-5, 2 bis 4 Epochen (S. 4183 bis 4184 (PDF 13 bis 14)).
- **Token-Klassifikation (S. 4179 (PDF 9)):** Für NER wird die Repräsentation des ersten Subword-Tokens eines Wortes genommen; im merkmalsbasierten Fall dienen die Aktivierungen einer oder mehrerer Schichten ohne Feinabstimmung als Eingabe für ein BiLSTM.
- **Tab. 7 (S. 4179 (PDF 9)), Dev-F1 NER:** Feinabstimmung BERT-Large 96,6, BERT-Base 96,4; merkmalsbasiert (BERT-Base) Einbettungen 91,0, vorletzte Schicht 95,6, letzte 94,9, Verkettung der letzten vier 96,1 (am Seitenbild geprüft). Die 0,3 F1 sind der Abstand 96,4 zu 96,1.
- WSD wird im Paper nicht evaluiert.

## Wörtliche Stellen

> „BERT is designed to pre-train deep bidirectional representations from unlabeled text by jointly conditioning on both left and right context in all layers.“ (S. 4171 (PDF 1))

> „This demonstrates that BERT is effective for both fine-tuning and feature-based approaches.“ (S. 4179 (PDF 9))

## Bezug zur Dissertation

- **Hintergrund für WSD mit kontextualisierten Repräsentationen:** BERT liefert pro Token eine Repräsentation, die vom linken und rechten Kontext abhängt (S. 4171, 4174 (PDF 1, 4)). Darauf beruhen WSD-Verfahren mit Einbettungen (etwa Nächste-Nachbarn-Vergleich mit Sense-Beispielen); das Paper selbst zeigt das nicht, belegt aber mit Tab. 7, dass eingefrorene Repräsentationen für Token-Aufgaben fast so gut sind wie Feinabstimmung (S. 4179 (PDF 9)).
- **Späterer Feinabstimmungsvergleich (PROTOKOLL §1 und §9.2, über die Forschungsfrage hinaus):** Ein feinabgestimmtes Encoder-Modell bräuchte Trainingsdaten pro Lemma; Silber aus D1 (§3) wäre die einzige Quelle, und Instabilität bei kleinen Datensätzen (S. 4176 (PDF 6)) wäre zu erwarten. Das Paper liefert die Standard-Hyperparameter (S. 4183 bis 4184 (PDF 13 bis 14)).
- **Mittelhochdeutsch:** BERT ist rein englisch vortrainiert (S. 4175 (PDF 5)), und mhd. Wörter würden in viele WordPiece-Stücke zerlegt; das erste Subword als Wortrepräsentation (S. 4179 (PDF 9)) ist dann eine schwache Wahl. Für mhd. Einbettungen ist ein historisch vortrainiertes Modell nötig (vgl. Beck & Köllner 2023, Zusammenfassung im selben Ordner).
- Keine Folgen für Goldstandard, IAA oder Stichprobe.

## Grenzen und Einwände

- Nur Englisch, nur Gegenwartssprache, keine WSD-Evaluation.
- Bestwerte gegenüber Leaderboard-Stand vom Dezember 2018 (S. 4177 (PDF 7)); historisch zu lesen.
- Der Nutzen von Next Sentence Prediction wird von Liu et al. 2019 (RoBERTa, Zusammenfassung im selben Ordner) bestritten.

## Weiterführend

- Peters et al. 2018a, Deep contextualized word representations (ELMo), NAACL (S. 4171 (PDF 1); Literaturliste S. 4181 (PDF 11)): der merkmalsbasierte Vorgänger.
- Melamud, Goldberger & Dagan 2016, context2vec: Learning generic context embedding with bidirectional LSTM, CoNLL (S. 4172 (PDF 2); Literaturliste S. 4181 (PDF 11)): kontextuelle Repräsentationen aus linkem und rechtem Kontext mit LSTMs.
