# Mihalcea, Chklovski & Kilgarriff 2004: The SENSEVAL-3 English Lexical Sample Task

**Datei:** `pdf/Mihalcea-etal-2004-Senseval3-Lexical-Sample.pdf` (nur lokal; 4 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen, Tab. 1 und der Absatz zur Übereinstimmung am Seitenbild (PDF-Seite 2) geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-16), also die Verlagsfassung; es enthält keine Markierungen.

Seitenzählung: Das PDF trägt keine Seitenzahlen. Die ACL Anthology nennt S. 25 bis 28, also PDF-Seite n = S. 24 + n. Unten steht die so errechnete Seite, die PDF-Seite in Klammern.

## Bibliografie

- **Vollständig:** Mihalcea, Rada, Timothy Chklovski & Adam Kilgarriff (2004). The SENSEVAL-3 English Lexical Sample Task. In: *Proceedings of SENSEVAL-3, the Third International Workshop on the Evaluation of Systems for the Semantic Analysis of Text*. Barcelona: Association for Computational Linguistics, Juli 2004, S. 25 bis 28.
- **DOI/URL:** keine DOI (Anthology-Seite ohne DOI; Crossref-Suche nach dem Titel am 2026-11-16 ohne Treffer); https://aclanthology.org/W04-0807. Titel, Autor:innen, Workshop, Ort und Monat auch am PDF (Titel und Fußzeile S. 25) ✔; Seiten nur laut Anthology.
- **Lizenz:** CC BY-NC-SA 3.0 (ACL Anthology, Material vor 2016, abgerufen 2026-11-16).
- **Art:** Konferenzbeitrag (Aufgabenbeschreibung eines Shared Task, Workshop)
- **Sprache:** Englisch
- **Daten:** laut S. 28 (PDF 4) unter http://www.senseval.org und http://teach-computers.org (nicht aufgerufen).

## Worum es geht

Die Arbeit beschreibt die englische Lexical-Sample-Aufgabe von SENSEVAL-3: 57 mehrdeutige Wörter, Belege aus dem British National Corpus, Nomen und Adjektive mit WordNet 1.7.1, Verben mit Wordsmyth (S. 25 bis 26). Neu gegenüber den Vorgängerrunden ist die Annotation durch freiwillige Web-Nutzer:innen über Open Mind Word Expert statt durch geschulte Lexikograf:innen (S. 25). Berichtet werden Übereinstimmung der Annotierenden (rund 67,3 % roh, κ 0,58 oder 0,35 je nach Mittelung und Zufallsmodell), eine MFS-Baseline von 55,2 % fein und 64,5 % grob sowie die Ergebnisse von 47 Systemen aus 27 Teams; das beste erreicht 72,9 % fein (S. 26).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Ziel: ein Evaluationsrahmen für gezielte WSD („targeted“), Nachfolger von SENSEVAL-1 und -2. Neu: Datensammlung über Web-Freiwillige statt geschulter Lexikograf:innen, und für Verben ein anderes Inventar (Wordsmyth). | S. 25 (PDF 1), Abschnitt 1 | Beschreibung |
| Annotationsablauf in OMWE: Pro Zielwort werden Sätze aus einem großen Korpus gezogen; Beitragende wählen den passendsten Sense per Ankreuzfeld, dazu zwei Zusatzoptionen „unclear“ und „none of the above“. Mehrere Senses dürfen gewählt werden, nur einer wird empfohlen. Die Antworten anderer werden nicht gezeigt, „to avoid artificial biases“. | S. 25 (PDF 1), Abschnitt 2 | eigenes Verfahren |
| Schema „tag until two agree“, höchstens vier Annotationen pro Item, wie in SENSEVAL-2. | S. 25 (PDF 1), Abschnitt 2 | eigenes Verfahren, Vorbild referiert |
| Quelle der Belege: BNC; frühere OMWE-Fassungen enthielten auch Penn Treebank, LA Times (TREC) und Open Mind Common Sense. | S. 25 (PDF 1), Abschnitt 2.1 | Beschreibung |
| Wahl von Wordsmyth für Verben, weil die schwache Verbleistung in SENSEVAL-2 an der hohen Sense-Zahl der Verben in WordNet liegen könnte; man hoffe so Einsicht in die Abhängigkeit der Schwierigkeit vom Inventar zu gewinnen. | S. 25 bis 26 (PDF 1 bis 2), Abschnitt 2.2 | Begründung, Vermutung der Autor:innen; ein Vergleich der Inventare wird in diesem Papier nicht ausgewertet |
| Mehrwortausdrücke wurden vor dem Annotieren herausgefiltert; die Aufgabe enthält nur Einzelwörter. Das sei eine andere Aufgabendefinition als früher und könne die Systemleistung beeinflussen. | S. 26 (PDF 2), Abschnitt 2.3 | eigene Designentscheidung |
| Übereinstimmung: 62,8 % zwischen den ersten beiden Annotationen bei Einzelwörtern; mit den etwa 12 % Mehrwortausdrücken und Eigennamen (Präzision „close-to-100%“) gesamt „about 67.3%“. Vergleichswert SENSEVAL-2 (Nomen und Adjektive): 66,5 % zwischen den ersten beiden Annotationen. **Die Zahlen gelten für den ganzen bisherigen OMWE-Bestand mit über 350 Wörtern**, nicht eigens für die 57 Wörter der Aufgabe. | S. 26 (PDF 2), Abschnitt 2.4 | eigene Messung; SENSEVAL-2-Wert referiert (Kilgarriff 2002) |
| κ zweifach: **mikro** (Sense-Zahl, Zufallsübereinstimmung und κ als Mittel über alle Wörter) und **makro** (Übereinstimmung, Zufall und κ pro Wort, dann gemittelt). Bei durchschnittlich fünf Senses liegt die Zufallsübereinstimmung bei 0,20, Mikro-κ = 0,58. Für Makro-κ wird angenommen, dass die Senses der in OMWE beobachteten Verteilung folgen; Makro-κ = 0,35. | S. 26 (PDF 2), Abschnitt 2.4 | eigene Rechnung, Formeln nicht abgedruckt |
| MFS-Baseline (Präzision = Recall): 55,2 % fein, 64,5 % grob. Die meisten Systeme, auch mehrere unüberwachte, liegen „significantly higher“; bestes System 72,9 % fein (79,3 % grob). | S. 26 (PDF 2), Abschnitt 3 | eigenes Ergebnis; ein Signifikanztest wird nicht genannt |
| Mehrere der besten Systeme kombinieren Klassifikatoren; das zeige „once again“, dass Abstimmungsverfahren einzelne Klassifikatoren übertreffen. | S. 26 (PDF 2), Abschnitt 3 | Deutung der Autor:innen |
| Fazit: überwachtes Lernen kann die MFS-Baseline deutlich übertreffen, unüberwachte Verfahren können verlässlich sein, Web-Freiwillige taugen zur Erstellung von Trainings- und Testdaten („tentatively suggest“). | S. 28 (PDF 4), Abschnitt 4 | Schlussfolgerung, vorsichtig formuliert |

## Daten, Methode, Zahlen

**Tab. 1 (S. 26, PDF 2, am Seitenbild geprüft), Inventar:**

| Wortart | Wörter | Senses im Mittel (fein) | Senses im Mittel (grob) |
|---|---|---|---|
| Nomen | 20 | 5,8 | 4,35 |
| Verben | 32 | 6,31 | 4,59 |
| Adjektive | 5 | 10,2 | 9,8 |
| gesamt | 57 | 6,47 | 4,96 |

- **Grob gegen fein:** Wie die groben Senses gebildet wurden, sagt das Papier nicht; es berichtet nur Mittelwerte (Tab. 1) und eine grobe Wertung (Tab. 2 und 3).
- **Umfang der Test- und Trainingsdaten:** im Papier nicht angegeben [am PDF zu prüfen: nur in der Datenverteilung oder in Begleitpublikationen].
- **Übereinstimmung:** 62,8 % (Einzelwörter, erste zwei Annotationen), gesamt etwa 67,3 %; Mikro-κ 0,58 bei Zufallsübereinstimmung 0,20; Makro-κ 0,35 (alles S. 26, PDF 2). Nachgerechnet am 2026-11-16: (0,673 − 0,20) / (1 − 0,20) = 0,59, nicht 0,58; mit 66,5 % ergäbe sich 0,58. Welche Rohübereinstimmung in Mikro-κ eingeht, sagt das Papier nicht.
- **Systeme:** 47 Einreichungen von 27 Teams (S. 25 Abstract, S. 26). Tab. 2 (überwacht, S. 27, PDF 3) und Tab. 3 (unüberwacht, S. 28, PDF 4) mit Präzision und Recall, fein und grob. Bester fein: htsa3 (Naive Bayes mit korrigierten A-priori-Häufigkeiten) 72,9 / 72,9, grob 79,3; IRST-Kernels hat grob mit 79,5 den höchsten Wert der Tabelle. Bestes unüberwachtes System: wsdiit, P 66,1, R 65,7 fein (Tab. 3).
- **Präzision ohne Abdeckung:** DLSI-UA-LS-SU P 78,2, R 31,0 (fein); IRST-Ties P 70,6, R 50,5 (Tab. 2). Hohe Präzision bei geringem Recall ist nicht mit den vollständigen Systemen vergleichbar.
- **Zwei Systeme auf grobe Senses trainiert** (NRC-Coarse, NRC-Coarse2): fein nur 48,5 bzw. 48,4, grob 75,8 bzw. 75,7 (Tab. 2).

## Wörtliche Stellen

> „Although users are encouraged to select only one meaning per word, the selection of two or more senses is also possible. The results of the classification submitted by other users are not presented to avoid artificial biases.“ (S. 25, PDF 1)

> „By choosing a different set of senses, we hope to gain insight into the dependence of difficulty of the sense disambiguation task on sense inventories.“ (S. 26, PDF 2)

> „With an average of five senses per word, the average value for the agreement by chance is measured at 0.20, resulting in a micro-κ statistic of 0.58. For macro-κ estimations, we assume that word senses follow the distribution observed in the OMWE annotated data, and under this assumption, the macro-κ is 0.35.“ (S. 26, PDF 2)

## Bezug zur Dissertation

**Prüfauftrag zu `goldstandard/LITERATUR-IAA.md`** (dort Mihalcea, Chklovski & Kilgarriff 2004 mit ✔):

- *„67,3 %, κ = 0,58 oder 0,35 je nach Zufallsmodell“*: **gedeckt, mit zwei Präzisierungen.** (1) Die Werte beschreiben den ganzen OMWE-Bestand (über 350 Wörter), nicht das SENSEVAL-3-Testset mit 57 Wörtern (S. 26). (2) Mikro- und Makro-κ unterscheiden sich nicht nur im Zufallsmodell (fünf gleich wahrscheinliche Senses gegen beobachtete Verteilung), sondern auch in der Mittelung (über alle Wörter gegen pro Wort, dann gemittelt). Die Aussage „allein das Zufallsmodell verschiebt κ“ ist damit leicht überspitzt; beides ändert sich zugleich.
- **PROTOKOLL §9.1, Punkt 4** („Senseval-3: 0,58 gegenüber 0,35 auf denselben Daten“): Die Formulierung „Senseval-3“ trifft nur den Rahmen; die Daten sind der OMWE-Bestand. Vorschlag: „OMWE-Daten, über die SENSEVAL-3 berichtet“ und „Mittelung und Zufallsmodell“. Die Folge im Protokoll (Randverteilungen, MFS- und Nicht-MFS-Übereinstimmung, AC1 mitberichten) bleibt gut gestützt: Bei schiefer Sense-Verteilung fällt κ von 0,58 auf 0,35.
- **PROTOKOLL §9.1, Punkt 3** (erwartete Übereinstimmung pro Lemma, über Items summiert): Makro-κ rechnet ebenfalls pro Wort und mittelt dann. Das ist kein Beleg für die genaue Konstruktion des Protokolls (dort Summe der A_e über Items statt Mittel der κ), aber ein Präzedenzfall dafür, den Zufall pro Wort aus dessen Sense-Verteilung zu schätzen. Das Papier gibt die Formel nicht an; zitierbar nur als Idee.

**Weitere Bezüge:**

- **PROTOKOLL §6 (Status `MEHRERE`, `KEINE_PASST`, `KONTEXT_UNZUREICHEND`):** OMWE bot schon „unclear“ und „none of the above“ und erlaubte mehrere Senses bei Empfehlung für einen (S. 25). Das ist ein frühes Vorbild für die Ausweichlabels; im Protokoll ist `MEHRERE` strenger gefasst.
- **PROTOKOLL §6 und §7 (Blindheit):** Antworten anderer wurden nicht gezeigt, „to avoid artificial biases“ (S. 25). Stützt die technische Blindheit.
- **PROTOKOLL §9.1, Punkt 7 und A32 (gröbere Senses als Ausweg):** Fein 55,2 % gegen grob 64,5 % MFS und 72,9 gegen 79,3 beim besten System (S. 26) zeigen den Granularitätseffekt auf Systemseite. Wie grob gruppiert wurde, bleibt hier offen.
- **PROTOKOLL §4 (Lexical-Sample-Design):** Das Design ist das klassische Lexical Sample mit vielen Belegen pro Wort und nur 57 Wörtern (Tab. 1); die Dissertation zieht dagegen 1 Token pro Paar aus Lemma und Wortart über 36 Zellen. Die Inventarwahl je Wortart (WordNet gegen Wordsmyth) ist ein Beispiel dafür, dass Wortart und Inventar im Design verschränkt sein können; ähnlich mischt die MHDBDB Lemma- und Beleg-Wortart (A25).
- **Rohübereinstimmung als Obergrenze:** Das Papier stellt die Übereinstimmung direkt neben die Systemwerte; das stützt §9.1, Punkt 2 (Rohübereinstimmung mitberichten), ohne es eigens zu begründen.

## Grenzen und Einwände

- Kurzes Aufgabenpapier (4 Seiten): Umfang der Test- und Trainingsdaten, Bildung der groben Senses und die κ-Formeln fehlen.
- Übereinstimmungswerte gelten für den ganzen OMWE-Bestand, nicht für das Testset; die Rohübereinstimmung von 67,3 % enthält zu etwa 12 % fast sicher übereinstimmende Mehrwortausdrücke und Eigennamen, die im Testset gar nicht vorkommen (S. 26). Der Wert für Einzelwörter ist 62,8 %.
- „Significantly higher“ (S. 26) ohne Test oder Intervall.
- Annotierende sind Web-Freiwillige; ihre Zahl, Vorbildung und Verteilung auf Items werden nicht genannt.
- Kein Vergleich der Inventare WordNet und Wordsmyth, obwohl die Inventarwahl damit begründet wird.
- Englisch, Gegenwartssprache, Wörterbuch-Inventare; Übertragung auf Mittelhochdeutsch und ein onomasiologisches Inventar nicht berührt.

## Weiterführend

- Kilgarriff 2002 (SENSEVAL-2, 66,5 % Übereinstimmung, S. 26); im Literaturverzeichnis des Papiers nicht aufgeführt, Zuordnung offen. Zum Abgleich der Zahl: Kilgarriff 2001 (`Kilgarriff-2001-English-Lexical-Sample.md`, liegt vor).
- Chklovski & Mihalcea 2002, Building a sense tagged corpus with Open Mind Word Expert, ACL-Workshop WSD (S. 25, 28).
- Carletta 1996, Assessing agreement on classification tasks: the kappa statistic, *Computational Linguistics* 22(2) (S. 26, 28).
- Kilgarriff & Palmer (Hg.) 2000, Sonderheft SENSEVAL, *Computers and the Humanities* 34 (S. 25, 28).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
