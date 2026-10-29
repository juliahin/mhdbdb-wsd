# Raganato, Camacho-Collados & Navigli 2017: Unified Evaluation Framework für WSD

**Datei:** `pdf/Raganato-etal-2017-WSD-Evaluation-Framework.pdf` (nur lokal; 12 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, ganze Textebene gelesen, Tabellen 1 bis 4 am Seitenbild geprüft, DOI aufgelöst. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-10-28), also die Verlagsfassung; es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 98 + n (PDF 1 = S. 99, PDF 12 = S. 110). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Raganato, Alessandro, Jose Camacho-Collados & Roberto Navigli (2017). Word Sense Disambiguation: A Unified Evaluation Framework and Empirical Comparison. In: Mirella Lapata, Phil Blunsom & Alexander Koller (Hg.), *Proceedings of the 15th Conference of the European Chapter of the Association for Computational Linguistics: Volume 1, Long Papers*. Valencia: Association for Computational Linguistics, S. 99 bis 110.
- **DOI/URL:** https://doi.org/10.18653/v1/E17-1010 (aufgelöst auf die ACL Anthology, Crossref-Eintrag vorhanden); https://aclanthology.org/E17-1010. Herausgeber:innen, Ort und Monat April aus dem BibTeX der Anthology ✔; Kopfzeile S. 99: „pages 99–110, Valencia, Spain, April 3-7, 2017“ ✔.
- **Lizenz:** CC BY 4.0 (ACL Anthology: Material ab 2016, laut FAQ und Fußzeile der Anthology, abgerufen 2026-10-28).
- **Art:** Konferenzbeitrag (EACL 2017, Long Paper)
- **Sprache:** Englisch
- **Ressource:** Framework, Richtlinien und Prüfskript unter http://lcl.uniroma1.it/wsdeval (S. 107; nicht aufgerufen).

## Worum es geht

Die Autoren bemängeln, dass WSD-Evaluationen nicht vergleichbar sind: Datensätze unterscheiden sich in Format, Annotationsrichtlinien und WordNet-Version, Trainingskorpora und Vorverarbeitung ebenso (S. 99). Sie vereinheitlichen fünf englische All-Words-Datensätze aus Senseval und SemEval und zwei Trainingskorpora auf ein XML-Format, WordNet 3.0 und eine gemeinsame Vorverarbeitung (S. 100 bis 101). Darauf vergleichen sie drei überwachte und drei wissensbasierte Systeme samt MFS- und WordNet-Erster-Sense-Baseline (S. 103 bis 104). Überwachte Systeme schlagen wissensbasierte klar; die MFS-Baseline ist stark, besonders schwach aber bei hoch ambigen Wörtern, und Verben sind für alle Systeme am schwersten (S. 104 bis 106).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Fehlender einheitlicher Rahmen verhindert faire Vergleiche: Datensätze differieren in Format, Richtlinien und Inventar (verschiedene WordNet-Versionen), automatische Mappings bringen Fehler, Trainingskorpora und Vorverarbeitung unterscheiden sich. Scheinbare Verbesserungen können daher aus Korpus, Vorverarbeitung oder Inventarversion stammen statt aus dem Modell. | S. 99, Abschnitt 1 | Problemstellung |
| Vierstufige Pipeline (Abb. 1): (1) einheitliches XML nach dem Schema von SemEval-13; (2) halbautomatisches Mapping auf WordNet 3.0, automatisch nur bei Mapping-Konfidenz 100 %, Rest von Hand geprüft und neu annotiert oder entfernt; Annotationen von Hilfsverben entfernt; (3) Vorverarbeitung mit Stanford CoreNLP (POS, Lemma); (4) Prüfskript, Abweichungen zwischen Sense-Annotation und CoreNLP-Lemma/POS automatisch behoben. | S. 101, Abschnitt 3 | eigenes Verfahren |
| Die Handkorrektur betraf weniger als 10 % der Instanzen in den Datensätzen, bei denen der Schritt nötig war. | S. 101, Anm. 2 | eigene Angabe |
| Fünf Evaluationsdatensätze, alle feinkörnig und All-Words: Senseval-2 (WordNet 1.7), Senseval-3 Task 1 (1.7.1; drei Dokumente aus Editorial, Nachricht, Fiktion), SemEval-07 Task 17 (2.1; nur Nomen und Verben), SemEval-13 Task 12 (3.0; 13 Dokumente; nur Nomen), SemEval-15 Task 13 (3.0; vier Dokumente aus Biomedizin, Mathematik/Informatik, Gesellschaft). | S. 101 bis 102, Abschnitt 4.1 | Beschreibung, Datensätze referiert |
| Ambiguität eines Datensatzes = Summe der Kandidaten-Senses geteilt durch Zahl der Annotationen; sie „may give a hint as to how difficult a given dataset may be“. SemEval-07 ist mit 8,5 am ambigsten. | S. 102 bis 103, Abschnitt 4.3 | eigene Kennzahl |
| MFS-Baseline = der im Trainingskorpus häufigste Sense des Zielworts. Daneben die Baseline „WordNet first sense“, als wissensbasiert gezählt, obwohl die Reihenfolge aus annotiertem Text stammt; sie sei schwer zu schlagen (mit Verweis auf Navigli 2009, Agirre et al. 2014). | S. 103 (MFS), S. 104 (WN first sense) | Definition eigen, Einschätzung teils referiert |
| Überwachte Systeme sind wegen unvollständiger Abdeckung durch das Trainingskorpus nach oben begrenzt („ceiling“). | S. 104, Abschnitt 5.2; Tab. 2 und 4 | eigenes Ergebnis |
| Überwachte Systeme übertreffen wissensbasierte durchgehend; IMS schlägt die MFS-Baseline stets; Context2Vec übertrifft IMS in den meisten Datensätzen. | S. 104, Abschnitt 5.2 | eigenes Ergebnis |
| Große Leistungsunterschiede zwischen den Datensätzen; in SemEval-07, dem ambigsten, sind die Werte niedrig, aber der Abstand überwachter Systeme zur MFS am größten. Das deute darauf, „the MFS heuristic does not perform accurately on highly ambiguous words“. | S. 104 bis 105 | eigenes Ergebnis und Deutung |
| **Verben:** „the F-Measure performance of all systems on verbs is in all cases below 58%“; erklärt mit der hohen Granularität der Verben in WordNet (*keep* hat 22 Bedeutungen). Mittlere Ambiguität der Verben 10,4 gegenüber 4,8 bei Nomen. Die MFS-Baseline „does not seem to be reliable for verbs“. | S. 106, Abschnitt 5.3; Tab. 3 (S. 105) und Tab. 4 (S. 106) | eigenes Ergebnis, Deutung der Autoren |
| Lokaler Kontext ist oft der entscheidende Hinweis; wissensbasierte Systeme gewichten alle Wörter des Satzes gleich (Beispiel *state*). | S. 105 bis 106 | eigene Fehleranalyse an einem Beispiel |
| Fehlerrate des POS-Taggers über alle Instanzen 3,9 %, korrigiert; Vorverarbeitung könne für morphologisch reichere Sprachen wichtiger sein. | S. 106, mit Anm. 18 | eigene Messung; Anm. referiert Eger et al. 2016 |
| **MFS-Bias:** Alle IMS-basierten Systeme beantworten über 75 % der Instanzen mit ihrem MFS, Context2Vec 71,5 % (SemCor) bzw. 74,7 % (SemCor+OMSTI); der Bias zeigt sich auch bei graphbasierten Systemen. | S. 106 bis 107 | eigenes Ergebnis |
| Babelfy weicht in 63 % aller Instanzen auf den WordNet-Erster-Sense aus; es ist das einzige wissensbasierte System, das diese Baseline insgesamt schlägt. | S. 107 | eigenes Ergebnis |
| Mehr, wenn auch automatisch annotierte Trainingsdaten (OMSTI) helfen leicht, z. B. Context2Vec +0,4 Punkte gesamt. | S. 105 | eigenes Ergebnis |
| Ausblick: Erweiterung auf andere Sprachen und Inventare (Open Multilingual WordNet, BabelNet, Wikipedia). | S. 107, Abschnitt 6 | Plan |

## Daten, Methode, Zahlen

**Tab. 1 (S. 102, am Seitenbild geprüft), nach Standardisierung:**

| Datensatz | Dok. | Sätze | Tokens | Annotationen | Sense-Typen | Wort-Typen | Ambiguität |
|---|---|---|---|---|---|---|---|
| Senseval-2 | 3 | 242 | 5.766 | 2.282 | 1.335 | 1.093 | 5,4 |
| Senseval-3 | 3 | 352 | 5.541 | 1.850 | 1.167 | 977 | 6,8 |
| SemEval-07 | 3 | 135 | 3.201 | 455 | 375 | 330 | 8,5 |
| SemEval-13 | 13 | 306 | 8.391 | 1.644 | 827 | 751 | 4,9 |
| SemEval-15 | 4 | 138 | 2.604 | 1.022 | 659 | 512 | 5,5 |
| SemCor | 352 | 37.176 | 802.443 | 226.036 | 33.362 | 22.436 | 6,8 |
| OMSTI | (keine Dokumentangabe, Anm. 6) | 813.798 | 30.441.386 | 911.134 | 3.730 | 1.149 | 8,9 |

Kleiner Widerspruch im Werk: Der Text nennt für SemCor 226.040 Annotationen (S. 102), Tab. 1 226.036.

**Tab. 2 (S. 105, am Seitenbild geprüft), F-Maß in %, Auswahl:**

| Training | System | SE2 | SE3 | SE07 | SE13 | SE15 |
|---|---|---|---|---|---|---|
| SemCor | IMS-s+emb (bester überwachter) | 72,2 | 70,4 | 62,6 | 65,9 | 71,5 |
| SemCor | MFS | 65,6 | 66,0 | 54,5 | 63,8 | 67,1 |
| SemCor | Ceiling | 91,0 | 94,5 | 93,8 | 88,6 | 90,4 |
| SemCor+OMSTI | MFS | 66,5 | 60,4 | 52,3 | 62,6 | 64,2 |
| wissensbasiert | Babelfy | 67,0 | 63,5 | 51,6 | 66,4 | 70,3 |
| wissensbasiert | WN 1st sense | 66,8 | 66,2 | 55,2 | 63,0 | 67,8 |

Die MFS-Baseline aus SemCor streut also je nach Datensatz zwischen 54,5 und 67,1.

**Tab. 3 (S. 105):** Verkettung aller fünf Datensätze: 7.253 Instanzen, davon 4.300 Nomen, 1.652 Verben, 955 Adjektive, 346 Adverbien; Ambiguität 4,8 / 10,4 / 3,8 / 3,1, gesamt 5,8.

**Tab. 4 (S. 106, am Seitenbild geprüft), F-Maß nach Wortart auf der Verkettung, Auswahl:**

| Training | System | Nomen | Verben | Adj. | Adv. | Alle |
|---|---|---|---|---|---|---|
| SemCor | MFS | 67,6 | 49,6 | 73,1 | 80,5 | 64,8 |
| SemCor | Context2Vec | 71,0 | 57,6 | 75,2 | 82,7 | 69,0 |
| SemCor | Ceiling | 89,6 | 95,1 | 91,5 | 96,4 | 91,5 |
| SemCor+OMSTI | IMS-s+emb (bester gesamt) | 72,0 | 56,5 | 76,6 | 84,7 | 69,7 |
| wissensbasiert | WN 1st sense | 67,6 | 50,3 | 74,3 | 80,9 | 65,2 |

Höchster Verbwert aller Systeme: 57,6 (Context2Vec, SemCor). Adverbien sind die leichteste Wortart, Verben die schwerste.

**Systeme (S. 103 bis 104):** IMS (SVM über lokale Merkmale), IMS+emb und IMS-s+emb (Word2Vec, 400 Dimensionen, auf ukWaC, ca. 2 Mrd. Wörter), Context2Vec (bidirektionales LSTM); Lesk_ext, Lesk_ext+emb, UKB, UKB gloss, Babelfy. Alle überwachten Systeme mit demselben Training (SemCor bzw. SemCor+OMSTI).

## Wörtliche Stellen

> „[…] the ambiguity may give a hint as to how difficult a given dataset may be.“ (S. 103)

> „[…] the MFS heuristic does not perform accurately on highly ambiguous words.“ (S. 105)

> „[…] the F-Measure performance of all systems on verbs is in all cases below 58%. This can be explained by the high granularity of verbs in WordNet.“ (S. 106)

> „[…] all supervised systems suffer a strong bias towards the MFS, with all IMS-based systems disambiguating over 75% of instances with their MFS.“ (S. 106)

## Bezug zur Dissertation

**Prüfauftrag zu `goldstandard/LITERATUR-STICHPROBE.md`** (dort mit ✔ zitiert):

1. *„All-Words-Sets sind Klumpenstichproben aus wenigen Dokumenten (3 bis 13); MFS hängt vom Dokument ab.“*
   - **Gedeckt:** die Dokumentzahlen. Tab. 1 (S. 102) nennt 3 / 3 / 3 / 13 / 4 Dokumente; im Text S. 101 bis 102 „three documents“ (Senseval-3), „thirteen documents“ (SemEval-13), „four documents“ (SemEval-15).
   - **Nicht im Werk:** Das Wort Klumpenstichprobe und jede Überlegung zur Stichprobenziehung fehlen; das ist eine Deutung der Tabelle, kein Befund von Raganato et al. Dass die **MFS vom Dokument** abhängt, steht nirgends; es gibt keine Auswertung pro Dokument. Belegt ist nur, dass die MFS-Baseline **je Datensatz** stark streut (54,5 bis 67,1 bei SemCor-MFS, Tab. 2, S. 105) und dass die Autoren die Unterschiede zwischen Datensätzen mit dem Ambiguitätsgrad erklären (S. 104 bis 105), nicht mit Dokumenten.
   - **Vorschlag:** Raganato et al. nur für die Dokumentzahlen (Tab. 1, S. 102) und die Streuung der MFS zwischen Datensätzen (Tab. 2, S. 105) anführen; „MFS hängt vom Dokument ab“ entweder am zweiten Beleg (Navigli et al. 2007) prüfen oder streichen. Status für diesen Teil eher ○ als ✔. Dasselbe gilt für PROTOKOLL §4.4, Punkt 4 („All-Words-Sets als Klumpenstichproben, Raganato et al. 2017“): als eigene Deutung kennzeichnen.
2. *„Verben sind am schwersten.“* **Gedeckt** (S. 106; Tab. 4): alle Systeme unter 58 % bei Verben, MFS 49,6 (SemCor) bzw. 45,9 (SemCor+OMSTI); Verben haben die höchste Ambiguität (10,4, Tab. 3, S. 105). Einschränkung: Die Autoren erklären das mit der feinen Verbgranularität **in WordNet**; ob das auf das MHDBDB-Inventar übertragbar ist, zeigt das Werk nicht. Die Folge im Design (Wortart als Schichtung) bleibt davon unberührt.

**Weitere Bezüge:**

- **PROTOKOLL §3 (Präpositionen und Adverbien „fehlen auch in den Vergleichsdatensätzen“):** Für Adverbien stimmt das beim englischen Standardrahmen nicht. Senseval-2 enthält Adverbien (S. 101), die Verkettung hat 346 Adverb-Instanzen (Tab. 3, S. 105), Tab. 4 wertet sie eigens aus. Präpositionen kommen nicht vor; das Werk nennt die Datensätze nur als Nomen, Verben, Adjektive, Adverbien. Vorschlag: den Satz im Protokoll auf Präpositionen beschränken oder die gemeinten Vergleichsdatensätze nennen.
- **PROTOKOLL §9.2 (MFS aus Silber, Rückfall auf den ersten Sense in `lexicon.xml`):** Raganato et al. trennen genau diese beiden Baselines: MFS aus dem Trainingskorpus (S. 103) und WordNet-Erster-Sense (S. 104). Im Englischen liegen beide nahe beieinander (64,8 und 65,2 gesamt, Tab. 4), weil die WordNet-Reihenfolge aus annotiertem Text stammt (S. 104). Für die MHDBDB trägt diese Parallele nicht: Der erste Sense in `lexicon.xml` ist nur bei 59 % der polysemen Lemmata der Mehrheitssense (`knowledge/data.md`, B8). Das stützt, Rückfall-Items getrennt auszuweisen.
- **PROTOKOLL §9.2 (Nicht-MFS-Items, Macro-Genauigkeit):** Der MFS-Bias selbst starker Systeme (über 75 % MFS-Antworten, S. 106) ist ein zweiter Beleg neben Maru et al. 2022, warum die Genauigkeit auf Nicht-MFS-Items getrennt berichtet werden soll.
- **PROTOKOLL §4.3 (Polysemie als Zellmerkmal):** Ambiguität als Schwierigkeitsindikator („may give a hint“, S. 103) und die schwache MFS bei hoher Ambiguität (S. 105) passen zur Schichtung nach Sense-Zahl; die Autoren behaupten aber nur einen Hinweis, kein gemessenes Modell.
- **Datenkonsistenz und Vorverarbeitung:** Das Werk zeigt, dass Inventarversion und Vorverarbeitung Ergebnisse verschieben können (S. 99). Für die Dissertation stützt das, Korpus-Commit und Prüfsummen von `lexicon.xml` und `concepts.xml` einzufrieren (PROTOKOLL §4.10, §10).
- **Größenordnung:** Die Standard-Testsets haben 455 bis 2.282 Instanzen (Tab. 1). Die geplanten ca. 510 Items liegen im Bereich eines einzelnen Senseval/SemEval-Sets.

## Grenzen und Einwände

- Nur Englisch, nur WordNet 3.0; das Werk selbst nennt andere Sprachen als künftige Arbeit (S. 107).
- Die Testsets sind keine Stichproben im statistischen Sinn; Konfidenzintervalle oder Signifikanztests werden nicht berichtet.
- Die Datensätze wurden mit verschiedenen Richtlinien erstellt; die Pipeline gleicht Format, Inventar und Vorverarbeitung an, nicht die Annotationsrichtlinien. Übereinstimmungswerte der Annotator:innen werden nicht berichtet.
- Die Erklärung der schwachen Verbwerte (Granularität) ist eine Deutung, nicht getrennt getestet.
- Stand 2017, vor vortrainierten Transformern und LLMs; die Systemzahlen sind historisch, der Rahmen selbst bleibt Referenz (so referiert bei Bevilacqua et al. 2021, S. 4331 bis 4332).
- Übertragbarkeit auf ein onomasiologisches Inventar (Begriffsgruppen statt Synsets mit Glossen) und auf Mittelhochdeutsch nicht berührt.

## Weiterführend

- Navigli, Litkowski & Hargraves 2007, SemEval-2007 Task 07 (S. 109): zweiter Beleg in `LITERATUR-STICHPROBE.md`; dort die Aussage zur dokumentabhängigen MFS prüfen.
- Postma et al. 2016, Addressing the MFS Bias in WSD systems, LREC (S. 106, Anm. 19).
- Calvo & Gelbukh 2015, MFS und Vernetzung in WordNet (S. 107).
- Pilehvar & Navigli 2014, pseudowortbasierter Evaluationsrahmen, *Computational Linguistics* 40(4) (S. 104).
- Eger, Gleim & Mehler 2016, Lemmatisierung und morphologisches Tagging für Deutsch und Latein, LREC (S. 106, Anm. 18).
- Iacobacci, Pilehvar & Navigli 2016 (S. 100, 103): liegt als PDF vor (`Iacobacci-etal-2016-Embeddings-WSD.pdf`).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
