# Iacobacci, Pilehvar & Navigli 2016: Embeddings for Word Sense Disambiguation

**Datei:** `pdf/Iacobacci-etal-2016-Embeddings-WSD.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, PDF vollständig gelesen (11 Seiten, Textebene; Tab. 3 und 4 am Seitenbild geprüft); DOI über Crossref und ACL Anthology bestätigt. Priorität 3 (Hintergrund), daher knapp.

**Seitenzählung:** gedruckt S. 897 bis 907 = PDF-Seite 1 bis 11; die Textebene trägt die Seitenlabels. Zitiert wird die gedruckte Seite, die PDF-Seite steht in Klammern.

## Bibliografie

- **Vollständig:** Iacobacci, Ignacio, Mohammad Taher Pilehvar & Roberto Navigli, 2016. Embeddings for Word Sense Disambiguation: An Evaluation Study. In: Katrin Erk & Noah A. Smith (Hg.), *Proceedings of the 54th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*, Berlin, August 2016. Association for Computational Linguistics, S. 897 bis 907.
- **DOI/URL:** https://doi.org/10.18653/v1/P16-1085 (am 2026-10-29 aufgelöst auf https://aclanthology.org/P16-1085/; Crossref bestätigt Autoren, Titel, Band, S. 897 bis 907; Herausgeber:innen und Monat aus dem BibTeX der ACL Anthology). ✔
- **Art:** begutachteter Konferenzbeitrag (ACL Long Paper)
- **Sprache:** Englisch
- **Code:** https://github.com/iiacobac/ims_wsd_emb (S. 905 (PDF 9)); nicht abgerufen.

## Worum es geht

Die Arbeit untersucht, wie man vortrainierte Wort-Embeddings als Merkmale in ein überwachtes WSD-System (It Makes Sense, IMS, mit linearer SVM) einbaut (S. 897, S. 900 (PDF 1, 4)). Vier Strategien, die Embeddings der Kontextwörter zu einem Merkmalsvektor zu verrechnen, werden verglichen: Verkettung, Mittelwert, gebrochene und exponentielle Abnahme mit dem Abstand zum Zielwort (S. 899 bis 900 (PDF 3 bis 4)). Getestet wird auf den englischen Lexical-Sample- und All-Words-Aufgaben von Senseval-2, Senseval-3 und SemEval-2007 (S. 900 bis 902 (PDF 4 bis 6)). Ergebnis: IMS mit Word2vec-Embeddings und exponentieller Abnahme ist auf allen Datensätzen am besten; Embeddings allein sind konkurrenzfähig (S. 901 bis 903, S. 905 (PDF 5 bis 7, 9)).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Überwachte WSD beruht auf der Annahme, dass Kontext eine gute Annäherung an Wortbedeutung ist. | S. 897 (PDF 1), Abschn. 1 | referiert (Miller & Charles 1991) |
| Manuelle Sense-Annotation ist schwierig und zeitaufwendig („knowledge acquisition bottleneck“); überwachte Verfahren skalieren deshalb nicht und müssen für jede Sprache wiederholt werden, sind aber die leistungsstärksten. | S. 898 (PDF 2), Abschn. 3.1 | referiert (Pilehvar & Navigli 2014) |
| Unüberwachte Verfahren müssen induzierte Senses auf ein Inventar abbilden und brauchen dafür manuelle Eingriffe. | S. 898 (PDF 2), Abschn. 3.2 | eigene Darstellung |
| Wissensbasierte Verfahren decken mehr ab und können überwachte erreichen. | S. 898 bis 899 (PDF 2 bis 3), Abschn. 3.4 | referiert |
| Exponentielle Abnahme (Gewicht sinkt mit dem Abstand zum Zielwort) liefert beständiger hohe Werte als Verkettung oder Mittelwert. | S. 903 (PDF 7), Abschn. 6.1, Tab. 5; S. 905 (PDF 9), Abschn. 7 | eigenes Ergebnis |
| IMS + Word2vec übertrifft IMS und zwei frühere Embedding-Erweiterungen (Taghipour & Ng 2015; AutoExtend) auf allen drei Lexical-Sample-Datensätzen. | S. 901 (PDF 5), Tab. 2 | eigenes Ergebnis |
| Im All-Words-Setting ist IMS + Word2vec (trainiert auf OMSTI) auf allen drei Datensätzen am besten; Embeddings gleichen schwächere Trainingsdaten teilweise aus. | S. 902 bis 903 (PDF 6 bis 7), Tab. 3 und 4 | eigenes Ergebnis |
| Retrofitting-Embeddings (Word2vec mit PPDB nachjustiert) allein, ohne Standardmerkmale, schlagen das IMS-Grundsystem um 2,8 Punkte; zusammen mit den Standardmerkmalen bringen sie weniger. | S. 903 (PDF 7), Abschn. 6.1 | eigenes Ergebnis |
| Unter den Standardmerkmalen ist die Wortart der Nachbarwörter das wirksamste. | S. 903 (PDF 7), Abschn. 6.1 | eigenes Ergebnis |
| Skip-gram ist CBOW und GloVe überlegen; Fenstergröße 10 ist für Standard-Embeddings am besten. | S. 903 bis 905 (PDF 7 bis 9), Tab. 5 und 6 | eigenes Ergebnis, bestätigt Levy et al. 2015 |

## Daten, Methode, Zahlen

- **System:** IMS mit linearer SVM; Standardmerkmale: Wortarten im Fenster von drei Wörtern je Seite, Kontextwörter ohne Stoppwörter, 11 lokale Kollokationen (S. 900 (PDF 4)).
- **Embeddings:** Word2vec Skip-gram, 400 Dimensionen, englische Wikipedia (September 2014, etwa drei Milliarden Tokens), Fenster 10; C&W mit 50 Dimensionen; Retrofitting mit PPDB (S. 900 (PDF 4)). In allen Hauptexperimenten exponentielle Abnahme und Fenster 10 je Seite (S. 900 (PDF 4)).
- **Lexical Sample** (Tab. 1, S. 901 (PDF 5)): Senseval-2, Senseval-3 (Nomen, Verben, Adjektive), SemEval-2007 (Nomen, Verben). F1 (Tab. 2): IMS 65,3 / 72,9 / 87,9; IMS + Word2vec 69,9 / 75,2 / 89,4 (SE2 / SE3 / SE7).
- **All-Words:** Trainingskorpora SemCor (etwa 360.000 Wörter, über 200.000 annotierte Inhaltswörter) und OMSTI (S. 901 bis 902 (PDF 5 bis 6)); Testsets mit 2.474, 2.041 und 465 Wörtern (S. 902 (PDF 6)).
- **Tab. 3 (alle Wortarten, am Seitenbild geprüft, PDF 6):** MFS-Baseline 60,1 / 62,3 / 51,4; IMS (Zhong & Ng 2010) 68,2 / 67,6 / 58,3; IMS + Word2vec (OMSTI) 68,3 / 68,2 / 59,1; IMS + Word2vec (SemCor) 63,4 / 65,3 / 57,8 (SE2 / SE3 / SE7).
- **Tab. 4 (nur Nomen, am Seitenbild geprüft, PDF 6):** MFS-Baseline 71,6 / 70,3 / 65,8; IMS + Word2vec (OMSTI) 77,7 / 74,1 / 71,5; Babelfy (wissensbasiert) – / 68,3 / 62,7, also unter MFS.
- **Analyse** (Tab. 5 und 6, S. 904 bis 905 (PDF 8 bis 9)) nur auf Senseval-2 Lexical Sample; bestes Einzelergebnis 70,2 % F1 (ohne Kontextwortmerkmal, 800 Dimensionen, Fenster 10, exponentielle Abnahme; S. 903 (PDF 7)).
- Keine Signifikanztests, keine Intervalle.

## Wörtliche Stellen

> „Since manual sense annotation is a difficult and time-consuming process, something known as the ”knowledge acquisition bottleneck” […] supervised methods are not scalable and they require repetition of a comparable effort for each new language.“ (S. 898 (PDF 2))

## Bezug zur Dissertation

- **Protokoll 9.2 (MFS als Baseline):** Tab. 3 und 4 sind ein gut zitierbarer Beleg für den Abstand zwischen MFS und einem starken überwachten System im All-Words-Setting vor den neuronalen Sprachmodellen: je nach Testset 5,9 bis 8,2 Punkte (Tab. 3: 60,1 gegen 68,3; 62,3 gegen 68,2; 51,4 gegen 59,1). Er zeigt, wie schwer MFS bei englischen WordNet-Daten zu schlagen ist, und ein wissensbasiertes System (Babelfy) lag bei Nomen sogar darunter (Tab. 4). Diese MFS stammt aus SemCor bzw. WordNet; im Protokoll kommt sie aus Silber (Leave-out), die Werte sind also nicht direkt vergleichbar.
- **Motivation für einen LLM-Ansatz:** Die Arbeit setzt große sense-annotierte Trainingskorpora voraus (SemCor, OMSTI) und benennt den Bottleneck für jede neue Sprache (S. 898). Für Mittelhochdeutsch gibt es kein vergleichbares Trainingskorpus außer dem Silber der MHDBDB, dessen Qualität erst gemessen wird (Protokoll 1). Das ist ein Grund, warum die Dissertation kein überwachtes System trainiert.
- **Protokoll 4.3 (Wortart als Schichtung):** Dass die Wortart der Nachbarwörter das wirksamste Standardmerkmal war (S. 903), ist ein schwacher Hinweis auf die Rolle syntaktischer Information; für die Schichtung nach Wortart des Zielworts ist das kein direkter Beleg.
- **Protokoll 6 (Kontextausschnitt, offener Punkt 4):** Für Standard-Embeddings war ein Fenster von 10 Wörtern je Seite am besten (S. 903). Für die Frage, wie viel Kontext Annotator:innen und LLM sehen, ist das nur eine Orientierung aus einem Merkmalsmodell, kein Maß für menschliches oder LLM-Lesen.

## Grenzen und Einwände

- Englisch, WordNet-Inventar, überwachtes Lernen mit großen Trainingskorpora; kein Bezug zu historischen Sprachen oder onomasiologischen Inventaren.
- Die Parameteranalyse beruht auf einem einzigen Datensatz (Senseval-2 Lexical Sample, S. 903).
- Die Unterschiede in Tab. 3 sind teils klein (IMS + Word2vec gegen IMS auf SE2: 68,3 gegen 68,2), ohne Signifikanztest.
- Ein Fehler im Tabellentext: „UBK w2w“ in Tab. 4 meint UKB (S. 902; im Text richtig „UKB w2w“).
- Stand 2016: statische Embeddings, vor kontextuellen Sprachmodellen.

## Weiterführend

- Zhong & Ng 2010, It Makes Sense (S. 898, S. 900): das Grundsystem.
- Taghipour & Ng 2015, Semi-Supervised Word Sense Disambiguation Using Word Embeddings in General and Specific Domains (S. 897, S. 901).
- Pilehvar & Navigli 2014, A Large-scale Pseudoword-based Evaluation Framework for State-of-the-Art WSD, *Computational Linguistics* 40(4) (S. 898, dort als Beleg für den Bottleneck).
- Miller, Chodorow, Landes, Leacock & Thomas 1994, Using a Semantic Concordance for Sense Identification (S. 901): SemCor.
- Raganato et al. 2017 (nicht in dieser Arbeit zitiert) vereinheitlicht dieselben Testsets; liegt in `pdf/` und steht in `goldstandard/LITERATUR-STICHPROBE.md`.
