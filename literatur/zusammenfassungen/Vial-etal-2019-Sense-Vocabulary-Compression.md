# Vial, Lecouteux & Schwab 2019: Sense-Vokabular-Kompression über WordNet

**Datei:** `pdf/Vial-etal-2019-Sense-Vocabulary-Compression.pdf` (nur lokal; 10 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Tab. 1 (PDF 5) und Tab. 3 und 4 (PDF 7) am Seitenbild geprüft, Tab. 2 und 5 an der Textebene. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-13), also die Tagungsfassung, nicht der arXiv-Preprint. Keine Markierungen.

**Seitenzählung:** Das PDF trägt weder Kopfzeile noch Seitenzahlen. Laut ACL Anthology steht der Beitrag auf S. 108 bis 117 des Tagungsbands; daraus PDF-Seite n = S. 107 + n. Unten steht die so abgeleitete Seite, die PDF-Seite in Klammern. Die Ableitung ist nicht am Tagungsband selbst geprüft.

## Bibliografie

- **Vollständig:** Vial, Loïc, Benjamin Lecouteux & Didier Schwab (2019). Sense Vocabulary Compression through the Semantic Knowledge of WordNet for Neural Word Sense Disambiguation. In: Piek Vossen & Christiane Fellbaum (Hg.), *Proceedings of the 10th Global Wordnet Conference*. Wrocław: Global Wordnet Association, S. 108 bis 117.
- **DOI/URL:** https://doi.org/10.18653/v1/2019.gwc-1.14 (aufgelöst am 2026-11-13, leitet auf https://aclanthology.org/2019.gwc-1.14 weiter); Herausgeber:innen, Ort, Monat Juli, Verlag und Seiten aus dem BibTeX der Anthology.
- **Lizenz:** CC BY 4.0 (ACL Anthology, Material ab 2016, laut Fußzeile der Anthology, abgerufen 2026-11-13).
- **Art:** Konferenzbeitrag (GWC 2019)
- **Sprache:** Englisch
- **Code:** https://github.com/getalp/disambiguate (S. 109 (PDF 2), Fn. 1; nicht aufgerufen).

## Worum es geht

Überwachte WSD-Systeme sehen im Training nur einen kleinen Teil der WordNet-Senses; in SemCor sind es etwa 16 % (S. 108 (PDF 1)). Die Autoren verkleinern deshalb das Ausgabevokabular: Jeder Sense wird auf einen gröberen Knoten abgebildet, aber nur so weit, dass die Senses **jedes** Wortes weiter unterscheidbar bleiben (S. 111 (PDF 4)). Zwei Verfahren: über Hyperonyme (Vokabular von 206.941 auf 39.147) und über alle WordNet-Relationen (auf 11.885) (S. 112 (PDF 5), Tab. 1). Mit einem BERT-basierten Klassifikator bleibt die Genauigkeit gleich, die Abdeckung steigt fast auf 100 % (S. 114 (PDF 7), Tab. 3 und 4). Es ist eine Kompression für die Modellausgabe, keine Vergröberung der Bewertung: Die Auswertung bleibt feinkörnig.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| In SemCor, dem größten handannotierten Korpus, kommen 33.760 verschiedene Sense-Schlüssel vor, etwa 16 % des WordNet-Inventars. | S. 108 (PDF 1), Abschn. 1 | eigene Angabe |
| Grundidee: Ein Sense und seine nächsten Verwandten teilen eine gemeinsame Vorstellung; zum Unterscheiden von *mouse* (Tier) und *mouse* (Gerät) genügen „animal“ und „electronic device“, speziellere Knoten sind überflüssig. | S. 108 bis 109 (PDF 1 bis 2), Abschn. 1 | eigene Hypothese |
| Mittlere Sense-Zahl polysemer Wörter in WordNet etwa 3; alle Wort-Senses zusammen 206.941. | S. 109 (PDF 2), Abschn. 2.2 | eigene Angabe |
| Abgrenzung zu Supersenses (26 Nomen- und 15 Verbklassen, Ciaramita & Altun 2006) und Basic Level Concepts (Izquierdo et al. 2007): Dort wird die grobe Klasse selbst vorhergesagt und bewertet; hier bleiben die Senses eines Lemmas immer in verschiedenen Clustern, sodass aus dem vorhergesagten Cluster der feine Sense zurückgewonnen wird. | S. 110 (PDF 3), Abschn. 2.3 | referiert, Abgrenzung eigen |
| **Synonymie:** Wort-Sense auf Synset abbilden ist schon üblich (Vokabular 117.659). | S. 110 bis 111 (PDF 3 bis 4), Abschn. 3.1; Tab. 1 | eigene Einordnung |
| **Hyperonyme:** Jeder Sense wird auf seinen höchsten Vorfahren abgebildet, der (1) alle Senses des Zielworts trennt und (2) keine für ein anderes Wort nötige Unterscheidung verwischt. Beispiel: *mouse#1* nicht auf *living_thing#1*, weil *animal#1* für die zwei Senses von *prey* nötig ist. Verfahren: Kinder des ersten gemeinsamen Vorfahren jedes Sense-Paars jedes Wortes als „necessary“ markieren, dann jeden Sense auf den ersten markierten Vorfahren abbilden. | S. 111 (PDF 4), Abschn. 3.2, Abb. 2 | eigenes Verfahren |
| Ergebnis ist „the smallest subset of all synsets that are necessary to distinguish every sense of every word of WordNet“ entlang der Hyperonymie. | S. 112 (PDF 5), Abschn. 3.2 | eigene Aussage |
| 41.607 von 44.449 polysemen Nomen (94 %) liegen in der Hyperonymhierarchie. | S. 111 (PDF 4), Fn. 2 | eigene Zählung |
| **Alle Relationen:** iteratives Zusammenlegen der jeweils kleinsten verwandten Cluster, solange alle Wörter unterscheidbar bleiben; stochastisch, Endgröße stets zwischen 11.000 und 13.000 Clustern; mittlere Clustergröße 17 Senses gegenüber 5 bei der Hyperonym-Methode. | S. 112 (PDF 5), Abschn. 3.3, Abb. 3 | eigenes Verfahren |
| Mit beiden Kompressionen sind die F1-Werte „overall equivalent“ zu den Systemen ohne Kompression, die Abdeckung steigt stark. | S. 114 (PDF 7), Abschn. 4.3; Tab. 3 und 4 | eigenes Ergebnis |
| Über Einzelmodelle gemessen beeinträchtigt die Hyperonym-Kompression das Ergebnis nie signifikant; die Kompression über alle Relationen verschlechtert es in manchen Fällen, vor allem mit ELMo und GloVe. | S. 115 (PDF 8), Abschn. 4.4; Tab. 5 | eigenes Ergebnis, „signifikant“ nur über Standardabweichungen begründet |
| BERT statt ELMo bzw. GloVe bringt etwa 3 bzw. 5 Punkte, WNGC als zusätzliches Training etwa 2, Ensembles etwa 1 Punkt. | S. 115 (PDF 8), Abschn. 4.4 | eigenes Ergebnis |

## Daten, Methode, Zahlen

**Tab. 1 (S. 112 (PDF 5), am Seitenbild geprüft):**

| Methode | Vokabular | Kompressionsrate | Abdeckung SemCor |
|---|---|---|---|
| keine | 206.941 | 0 % | 16 % |
| Synonyme | 117.659 | 43 % | 22 % |
| Hyperonyme | 39.147 | 81 % | 32 % |
| alle Relationen | 11.885 | 94 % | 39 % |

**System (S. 113 (PDF 6)):** BERT `bert-large-cased` als Eingabe, sechs Transformer-Encoder-Schichten, Softmax über alle im Training gesehenen (komprimierten) Tags; Training auf SemCor bzw. SemCor + Princeton WordNet Gloss Corpus (WNGC), 20 Epochen; Bewertung als Ensemble aus 8 Modellen (S. 114 (PDF 7)). Parameterzahl sinkt um den Faktor 1,2 bis 2 (Tab. 2: 77,15M auf 55,16M mit SemCor, 120,85M auf 60,27M mit SemCor+WNGC).

**Tab. 3 (S. 114 (PDF 7), am Seitenbild geprüft), F1 in %, Auswahl, Spalte „ALL“ = Verkettung von SE2, SE3, SE07, SE13, SE15:**

| System | ALL gesamt | Nomen | Verben | SE07 Task 7 (grob) |
|---|---|---|---|---|
| First-Sense-Baseline | 65,5 | 67,7 | 49,8 | 78,9 |
| SemCor, ohne Kompression | 76,0 | 78,7 | 65,2 | 87,7 |
| SemCor, Hyperonyme | 76,7 | 79,6 | 65,9 | 87,6 |
| SemCor, alle Relationen | 75,4 | 77,2 | 66,0 | 86,7 |
| SemCor+WNGC, ohne Kompression | 78,3 | 80,6 | 68,1 | 90,4 |
| SemCor+WNGC, Hyperonyme | 79,0 | 81,4 | 68,7 | 90,4 |
| SemCor+WNGC, alle Relationen | 78,5 | 80,7 | 68,6 | 90,6 |

Die Spalte SE07 Task 7 ist der grobkörnige Datensatz von Navigli et al. 2007 (S. 114 (PDF 7)); dort liegen alle Werte um 11,3 bis 13,4 Punkte über dem feinkörnigen ALL-Gesamtwert desselben Systems (eigene Rechnung aus Tab. 3).

**Tab. 4 (S. 114 (PDF 7)), Abdeckung auf ALL (7.253 Wörter):** SemCor ohne Kompression 93,23 % (491 Wörter nicht annotierbar), Hyperonyme 98,75 % (91), alle Relationen 99,67 % (24); mit SemCor+WNGC bis 99,99 %.

## Wörtliche Stellen

> „[…] the most specialized concepts in WordNet are often superfluous for WSD.“ (S. 111 (PDF 4))

> „First, this ancestor must discriminate all the different senses of the target word. Second, we need to preserve the hypernyms that are indispensable to discriminate the senses of the other words in the dictionary.“ (S. 111 (PDF 4))

> „[…] we guarantee that two different senses of a lemma reside in two different clusters […]“ (S. 110 (PDF 3))

## Bezug zur Dissertation

- **Protokoll §9.1, Punkt 7, und §12, Punkt 12 (grobe Ebene über Oberbegriffe):** In `goldstandard/VORSCHLAEGE-2026-10.md` (V23) und in der Zusammenfassung von Bevilacqua et al. 2021 (S. 4334) wird Vial et al. als Präzedenz für eine grobe Auswertungsebene geführt. Am Volltext ist das nur eingeschränkt richtig:
  - **Gedeckt:** die Abbildung von Senses auf Vorfahren in einer Taxonomie (S. 111 (PDF 4)).
  - **Nicht gedeckt:** eine grobe **Auswertung**. Die Kompression ist so gebaut, dass zwei Senses eines Lemmas nie zusammenfallen (S. 110 (PDF 3)); bewertet wird weiter feinkörnig. Für die Zwei-Ebenen-Auswertung, bei der Senses eines Lemmas **zusammenfallen sollen**, sind Supersenses und Basic Level Concepts (beide nur referiert, S. 110 (PDF 3)) oder OntoNotes die passenderen Präzedenzen.
  - **Nutzbar ist ein Gedanke daraus:** Die Regel „höchster Vorfahr, der noch trennt“ (S. 111 (PDF 4)) liefert pro Lemma die gröbste Ebene, auf der seine Senses unterscheidbar bleiben. Umgekehrt gelesen zeigt sie, auf welcher Stufe des MHDBDB-Zahlencodes (B11) die Senses eines Lemmas zusammenfallen. Das wäre eine lemmaabhängige, vorab berechenbare Definition der groben Ebene, die nicht nachträglich durch Zusammenlegen gewonnen wird (Forderung in §9.1, Punkt 7).
- **A32 (Fall α < 0,67, „gröbere Senses“):** Vial et al. geben ein Verfahren an, Inventare zu verkleinern, ohne dass Senses eines Lemmas verschmelzen. Für den Goldstandard hilft das nicht, weil dort gerade das Verschmelzen ähnlicher Senses die Übereinstimmung heben soll. Als Begründung für „gröbere Senses“ taugt das Werk daher nicht; es zeigt nur, dass eine taxonomische Vergröberung **reproduzierbar** aus der Hierarchie berechnet werden kann.
- **Vergleichbarkeit mit dem MHDBDB-Inventar (`knowledge/data.md`, Abschnitt 1):** Das Verfahren setzt voraus, dass jeder Sense genau einen Platz in einer Hyperonymhierarchie hat (94 % der polysemen Nomen, Fn. 2). Ein MHDBDB-Sense zeigt dagegen auf eine **Menge** von Begriffen in einem polyhierarchischen System (B11). Eine Übertragung braucht deshalb zwei zusätzliche Festlegungen: welcher Begriff der Gruppe zählt (oder die Menge aller Oberbegriffe) und welcher Oberbegriffspfad (Zahlencode). Beide sind im Protokoll noch offen (§12, Punkt 12).
- **Granularität und Systemwerte:** Die Spanne zwischen feinkörnigem ALL (75,4 bis 79,0) und grobkörnigem SE07 Task 7 (86,7 bis 90,6) bei denselben Systemen (Tab. 3) ist ein weiterer Beleg dafür, dass die Granularität des Inventars die Messwerte stark verschiebt. Das passt zu §9.1, Punkt 7; es sind aber Systemwerte auf verschiedenen Datensätzen, keine Übereinstimmung zwischen Menschen.
- **LLM-Prüfung und Kontamination (A17 bis A29):** nicht berührt (überwachtes BERT-System, 2019).

## Grenzen und Einwände

- Nur Englisch und WordNet; die Methode braucht eine Hierarchie mit eindeutigem Platz pro Sense.
- Die Kompression dient der Abdeckung eines überwachten Klassifikators; sie sagt nichts darüber, ob Menschen die komprimierten Klassen leichter unterscheiden.
- „Signifikant“ wird nur über Standardabweichungen von acht Modellen begründet, ohne Test (S. 115 (PDF 8)).
- Die Kompression über alle Relationen ist stochastisch; berichtet wird ein einzelnes Mapping (S. 112 (PDF 5)).
- Seitenangaben aus der Anthology-Paginierung abgeleitet, nicht am gedruckten Band geprüft.

## Weiterführend

- Ciaramita & Altun 2006, Supersense-Tagger, EMNLP (S. 110 (PDF 3), 116 (PDF 9)): grobe Klassen als Bewertungsebene.
- Izquierdo, Suárez & Rigau 2007, Basic Level Concepts, RANLP (S. 110 (PDF 3), 116 (PDF 9)): Clustergröße über Schwelle steuerbar.
- Navigli, Litkowski & Hargraves 2007, SemEval-2007 Task 07, grobkörnig (S. 114 (PDF 7), 116 (PDF 9)): schon in `goldstandard/LITERATUR-IAA.md`.
- Vial, Lecouteux & Schwab 2018, UFSAC, LREC (S. 113 (PDF 6), 117 (PDF 10)).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF und hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
