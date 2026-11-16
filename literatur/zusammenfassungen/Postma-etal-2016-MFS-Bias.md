# Postma, Izquierdo, Agirre, Rigau & Vossen 2016: Addressing the MFS Bias in WSD Systems

**Datei:** `pdf/Postma-etal-2016-MFS-Bias.pdf` (nur lokal; 6 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen, Abb. 1 am Seitenbild (PDF-Seite 1) abgelesen, Tab. 1 und 2 aus der Textebene (digital gesetzt) und nachgerechnet. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-16), also die Verlagsfassung; es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 1694 + n (PDF 1 = S. 1695, PDF 6 = S. 1700). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Postma, Marten, Ruben Izquierdo, Eneko Agirre, German Rigau & Piek Vossen (2016). Addressing the MFS Bias in WSD Systems. In: Nicoletta Calzolari et al. (Hg.), *Proceedings of the Tenth International Conference on Language Resources and Evaluation (LREC'16)*. Portorož: European Language Resources Association (ELRA), Mai 2016, S. 1695 bis 1700.
- **DOI/URL:** https://doi.org/10.63317/2qcfqqj3yifp (Crossref, aufgelöst auf https://lrec.elra.info/lrec2016-main-268, dort „pp. 1695-1700“, abgerufen 2026-11-16); https://aclanthology.org/L16-1268 (Herausgeber:innen, Ort, Monat und Seiten im BibTeX der Anthology ✔). Seitenzahlen auch in den Fußzeilen des PDF ✔.
- **Lizenz:** CC BY-NC 4.0 laut ELRA-Seite („All LREC proceedings … are licenced under CC-BY-NC-4.0“, abgerufen 2026-11-16). Die ACL Anthology nennt für Material ab 2016 pauschal CC BY 4.0; maßgeblich ist die Angabe des Verlags.
- **Art:** Konferenzbeitrag (LREC, Kurzbeitrag)
- **Sprache:** Englisch
- **Code:** https://github.com/cltl/MFS_classifier (S. 1699; nicht aufgerufen)
- **Titel:** im PDF „WSD Systems“, in der Anthology „WSD systems“.

## Worum es geht

WSD-Systeme haben einen starken Hang zum häufigsten Sense (MFS): Auf Items mit MFS als Gold-Sense erreichen sie hohe Werte, auf Items mit einem selteneren Sense (LFS, „less frequent senses“) sehr niedrige (S. 1695). Die Autoren bauen einen Random-Forest-Klassifikator, der aus der Systemausgabe und meist statischen Lemma-Merkmalen vorhersagt, ob der Gold-Sense der MFS ist; sagt er „nicht MFS“ und hat das System den MFS gewählt, wird der zweitbeste Sense des Systems genommen (S. 1696 bis 1697). Angewendet auf IMS (überwacht) und UKB (wissensbasiert) steigt der Recall auf LFS-Items im Mittel um 8,5 bis 8,6 Punkte; der Gesamtrecall bleibt bei UKB gleich oder steigt leicht, bei IMS sinkt er (S. 1697 bis 1698).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Über fünf englische All-Words-Aufgaben (Senseval-2 bis SemEval-2013) liegt der mittlere Recall aller Systeme auf MFS-Items weit über, auf LFS-Items weit unter dem Durchschnitt; die Gesamtleistung sei daher stark von einer „very skewed and limited capacity to recognize senses in contexts“ bestimmt. | S. 1695, Abschnitt 1, Abb. 1 | Fehleranalyse von Izquierdo 2015 (CLIN-Vortrag), hier übernommen |
| Zwei Gründe für schwachen LFS-Recall: Systeme wählen den MFS, obwohl ein LFS gilt; und wo sie MFS und LFS richtig trennen, wählen sie den falschen LFS, vermutlich mangels Trainingsdaten. | S. 1695, Abschnitt 1 | Deutung der Autor:innen |
| Obergrenze bei perfekter Trennung MFS gegen LFS (UKB auf SemEval-2013): LFS-Recall von 25 % auf 57 %, Gesamtrecall von 66 % auf 78 %. | S. 1695, Abschnitt 1; S. 1698 bis 1699, Abschnitt 6 | eigenes Gedankenexperiment (Orakel) |
| Senses sind nicht gleich verteilt; meist dominiert einer. Systeme zeigen einen starken MFS-Bias; auch wissensbasierte, nicht nur überwachte. | S. 1696, Abschnitt 2 | referiert (Preiss 2006; Calvo & Gelbukh 2015) |
| Andere Ansätze verringern die Zahl der Klassen (WordNet Domains, Supersenses, Base Level Concepts), um Trainingsdaten verwandter Senses zu bündeln. | S. 1696, Abschnitt 2 | referiert (Peh & Ng 1997; Izquierdo et al. 2007) |
| Verfahren: Random-Forest-Klassifikator „MFS oder LFS“ mit drei Merkmalen aus der Systemausgabe (Konfidenz für den MFS, Entropie der Sense-Rangfolge, Korrelation der System-Entropie mit der Sense-Entropie in SemCor) und meist statischen Merkmalen pro Lemma (TF-IDF, Wortart, Sense-Zahl, WordNet Domains, Supersense) sowie einem korpusabhängigen Domänenmerkmal (JRC EuroVoc Indexer). Training auf SemCor. | S. 1696 bis 1697, Abschnitt 3 | eigenes Verfahren |
| Regel (Algorithmus 1): Sagt der Klassifikator LFS und ist der erste Systemsense der MFS, wird der zweite Systemsense ausgegeben; sonst bleibt der erste. | S. 1697, Abschnitt 3 | eigenes Verfahren |
| Binäre Aufgabe MFS gegen LFS: Alle Varianten schlagen die MFS-Baseline; Genauigkeit im Mittel +3,1 Punkte; Präzision und TN-Rate steigen, Recall (auf MFS) sinkt. | S. 1697, Abschnitt 4, Tab. 1 | eigenes Ergebnis |
| Feinkörnige WSD: LFS-Recall steigt im Mittel um 8,6 Punkte (S. 1697) bzw. 8,5 Punkte (S. 1698, 1699); Gesamtrecall bei UKB leicht höher, bei IMS niedriger. | S. 1697, Tab. 2; S. 1698 | eigenes Ergebnis |
| Verteilung der Gold-Senses nach Sense-Rang ist stark schief: 80 % (SemEval-2015) bzw. 90 % (SemEval-2013) in den ersten drei Rängen, 55 bis 60 % auf Rang 1. | S. 1698, Abschnitt 5, Abb. 3 | eigenes Ergebnis |
| Gewinne vor allem auf den Sense-Rängen 2 bis 4; ab Rang 5 kaum Wirkung; auf MFS-Items sinkt der Recall beider Systeme. LFS bleibt weit unter MFS. | S. 1698, Abb. 4 und 5 | eigenes Ergebnis |
| Dass der Klassifikator UKB mehr hilft als IMS, erklären die Autor:innen damit, dass die statischen Lemma-Merkmale UKB eher ergänzen („It might be the case“). | S. 1698, Abschnitt 5 | Vermutung |
| Ausblick: Sense-Cluster nutzen (den besten Sense außerhalb des MFS-Clusters wählen) und Embedding-basierte Verfahren prüfen. | S. 1698, Abschnitt 5 | Vorschlag |

## Daten, Methode, Zahlen

- **Testdaten:** SemEval-2013 Task 12 (1.514 Nomen-Instanzen) und SemEval-2015 Task 13 (815 Instanzen, alle vier Wortarten), jeweils ohne Mehrwortausdrücke; das eine Set dient bei der Auswertung des anderen als Entwicklungsset (S. 1696).
- **MFS-Baseline in der binären Aufgabe:** 60,6 % (2013) und 64 % (2015) (S. 1697). In einer binären Aufgabe entspricht eine solche Baseline dem Anteil der Items mit MFS als Gold-Sense (eigene Deutung, das Papier definiert sie nicht). Abschnitt 5 nennt dagegen 55 bis 60 % der Gold-Senses auf Sense-Rang 1 (S. 1698). Ob MFS hier aus SemCor und Sense-Rang aus WordNet stammt und die Zahlen daher abweichen, sagt das Papier nicht.

**Tab. 1 (S. 1697), binäre Aufgabe MFS gegen LFS, in %:**

| Set | System | P | R | Acc | TN-Rate |
|---|---|---|---|---|---|
| 2013 | UKB | 70,1 | 92,3 | 71,5 | 39,5 |
| 2013 | UKB+C | 77,7 | 85,4 | 76,3 | 62,3 |
| 2013 | IMS | 70,2 | 86,4 | 69,6 | 43,7 |
| 2013 | IMS+C | 76,9 | 77,4 | 72,3 | 64,3 |
| 2015 | UKB | 73,9 | 92,4 | 74,2 | 41,9 |
| 2015 | UKB+C | 78,0 | 90,3 | 77,5 | 54,7 |
| 2015 | IMS | 72,9 | 89,5 | 72,0 | 40,8 |
| 2015 | IMS+C | 78,2 | 81,5 | 73,6 | 59,5 |

TP = MFS richtig vorhergesagt, TN = LFS richtig erkannt. Die TN-Rate ohne Klassifikator (39,5 bis 43,7) zeigt: Die Systeme erkennen nur rund zwei Fünftel der LFS-Items als solche.

**Tab. 2 (S. 1697), feinkörnige WSD, in %:**

| Set | System | P | R | R auf LFS |
|---|---|---|---|---|
| 2013 | UKB | 65,9 | 65,9 | 25,3 |
| 2013 | UKB+C | 66,1 | 66,1 | 36,3 |
| 2013 | IMS | 60,6 | 60,6 | 20,9 |
| 2013 | IMS+C | 59,4 | 59,4 | 31,5 |
| 2015 | UKB | 68,5 | 67,1 | 20,8 |
| 2015 | UKB+C | 69,5 | 68,1 | 27,3 |
| 2015 | IMS | 67,1 | 65,8 | 17,3 |
| 2015 | IMS+C | 64,8 | 63,6 | 23,5 |

Nachgerechnet am 2026-11-16: Gewinn auf LFS +11,0 / +10,6 / +6,5 / +6,2, Mittel 8,575 (daher 8,6 bzw. 8,5 im Text); Genauigkeit in Tab. 1 +4,8 / +2,7 / +3,3 / +1,6, Mittel 3,1 ✔. Gesamtrecall: UKB +0,2 / +1,0, IMS −1,2 / −2,2. Der LFS-Recall der Ausgangssysteme liegt bei 17 bis 25 %.

**Abb. 1 (S. 1695, am Seitenbild abgelesen, nur ungefähr):** mittlerer Recall auf MFS-Items etwa 63 bis 80 %, auf LFS-Items etwa 14 bis 23 %, über alle fünf Aufgaben [genaue Werte am PDF nicht ablesbar, nur Balken].

## Wörtliche Stellen

> „Word Sense Disambiguation (WSD) systems tend to have a strong bias towards assigning the Most Frequent Sense (MFS), which results in high performance on the MFS but in a very low performance on the less frequent senses.“ (S. 1695, Abstract)

> „The average performance of all systems is therefore largely influenced by a very skewed and limited capacity to recognize senses in contexts.“ (S. 1695)

## Bezug zur Dissertation

- **PROTOKOLL §9.2 (Genauigkeit auf Nicht-MFS-Items, Macro-Genauigkeit):** Postma et al. sind ein früher, direkter Beleg, warum die Genauigkeit getrennt nach MFS- und Nicht-MFS-Items zu berichten ist: Ein Gesamtwert über der MFS kann fast ganz auf MFS-Items beruhen, bei 17 bis 25 % Recall auf den übrigen (Tab. 2, S. 1697). Für die Dissertation heißt das: Schlägt das LLM die MFS-Baseline, ist erst die Nicht-MFS-Genauigkeit der Beleg, dass es Kontext nutzt. Postma et al. ergänzen Maru et al. (2022) für die Zeit vor vortrainierten Modellen.
- **PROTOKOLL §9.2, McNemar und diskordante Paare (§4.7):** Wie Tab. 1 zeigt, kann ein System Genauigkeit auf MFS-Items gegen Genauigkeit auf LFS-Items tauschen, ohne den Gesamtwert viel zu ändern (IMS+C). Der gepaarte Vergleich gegen die MFS-Baseline sieht dann nur die diskordanten Items; eine Aufschlüsselung der diskordanten Paare nach MFS- und Nicht-MFS-Items im Bericht würde das sichtbar machen (Vorschlag, nicht im Protokoll).
- **PROTOKOLL §9.1, Punkt 4 (Übereinstimmung getrennt für MFS- und Nicht-MFS-Tokens):** Die Schiefe der Gold-Verteilung (55 bis 60 % Rang 1, S. 1698) ist das, was bei κ die Prävalenz ausmacht. Das stützt die getrennte Berichterstattung auch für die menschliche Übereinstimmung.
- **Manifest (§4.9) und Kovariaten (§4.3):** Die Merkmale des MFS-Klassifikators (Sense-Zahl, Entropie, Wortart, Domäne) decken sich weitgehend mit den Kovariaten im Manifest (Sense-Zahl, MFS-Anteil, Entropie, Wortart, Domäne). Das ist kein Beleg für das Protokoll, zeigt aber, dass genau diese Größen vorhersagen, ob ein Item ein MFS-Item ist.
- **MFS-Definition (§9.2, B8):** Das Papier definiert MFS nicht ausdrücklich; Abschnitt 5 setzt MFS mit Sense-Rang 1 gleich (S. 1698), die Zahlen in Abschnitt 4 und 5 passen dazu nicht ganz. Für die Dissertation erinnert das daran, die MFS-Definition (aus Silber, Rückfall erster Sense in `lexicon.xml`) im Artikel ausdrücklich zu nennen.

## Grenzen und Einwände

- Kurzbeitrag; die Merkmalsauswahl „using regression“ (S. 1696) ist nicht beschrieben, Hyperparameter fehlen, keine Signifikanztests.
- Nur zwei Systeme und zwei Testsets; die Testsets dienen wechselseitig als Entwicklungsdaten (S. 1696).
- Der Anspruch „while maintaining the overall recall“ (Abstract, S. 1699) gilt nur für UKB; bei IMS sinkt der Gesamtrecall um 1,2 bzw. 2,2 Punkte (Tab. 2).
- Abb. 1 stammt aus einer nicht begutachteten Fehleranalyse (Izquierdo 2015, CLIN-Vortrag) und ist nur als Balkendiagramm ohne Zahlen abgedruckt.
- Kleine Widersprüche: 8,6 gegen 8,5 Punkte (Rundung); MFS-Anteil 60,6 und 64 % gegen 55 bis 60 % auf Rang 1.
- Englisch, WordNet; Systeme vor vortrainierten Transformern und LLMs. Übertragbarkeit auf das MHDBDB-Begriffssystem nicht berührt.

## Weiterführend

- Preiss 2006, A detailed comparison of WSD systems, *Natural Language Engineering* 12(3), S. 209 bis 228 (S. 1696, 1699): früherer Beleg für den MFS-Bias.
- Calvo & Gelbukh 2015, Is the most frequent sense of a word better connected in a semantic network? (S. 1696, 1699): MFS-Bias bei wissensbasierten Systemen.
- Izquierdo 2015, Error analysis of WSD, CLIN25 (S. 1695, 1699): Quelle von Abb. 1, nur Vortrag.
- Agirre & López de Lacalle 2003, Clustering WordNet word senses, RANLP (S. 1698, 1699): Sense-Cluster.
- Ressourcen der Autor:innen (S. 1699): `wsd_corpora` (einheitliches XML), `WordNetMapper`, `semantic_class_manager`.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
