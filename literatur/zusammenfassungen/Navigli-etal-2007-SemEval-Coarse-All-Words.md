# Navigli, Litkowski & Hargraves 2007: SemEval-2007 Task 07, Coarse-Grained English All-Words

**Datei:** `pdf/Navigli-etal-2007-SemEval-Coarse-All-Words.pdf` (nur lokal; 6 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen (Tabellen 1 bis 7 aus der Textebene, das PDF ist digital gesetzt; Tab. 5 zusätzlich am Seitenbild, PDF-Seite 5). Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-16), also die Verlagsfassung; es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 29 + n (PDF 1 = S. 30, PDF 6 = S. 35). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Navigli, Roberto, Kenneth C. Litkowski & Orin Hargraves (2007). SemEval-2007 Task 07: Coarse-Grained English All-Words Task. In: Eneko Agirre, Lluís Màrquez & Richard Wicentowski (Hg.), *Proceedings of the Fourth International Workshop on Semantic Evaluations (SemEval-2007)*. Prag: Association for Computational Linguistics, Juni 2007, S. 30 bis 35.
- **DOI/URL:** https://doi.org/10.3115/1621474.1621480 (Crossref, Titel dort verkürzt „SemEval-2007 task 07“, S. 30 bis 35; die DOI leitet auf die ACM Digital Library weiter, abgerufen 2026-11-16); https://aclanthology.org/S07-1006 (Herausgeber:innen, Ort, Monat und Seiten im BibTeX der Anthology ✔; Kopfzeile S. 30: „pages 30–35, Prague, June 2007“ ✔).
- **Lizenz:** CC BY-NC-SA 3.0 (ACL Anthology, Material vor 2016, abgerufen 2026-11-16).
- **Art:** Konferenzbeitrag (Aufgabenbeschreibung eines Shared Task, Workshop)
- **Sprache:** Englisch

## Worum es geht

Die Aufgabe prüft WSD aller Inhaltswörter eines Textes gegen eine **grobe** Fassung von WordNet 2.1, weil die feine Granularität als Haupthindernis gilt (S. 30). Die groben Senses entstehen durch Abbildung von WordNet-Senses auf die obersten Einträge des Oxford Dictionary of English; für die Testwörter hat ein Lexikograf die Abbildung von Hand gemacht (S. 31). Testkorpus: fünf Texte mit 2.269 annotierten Wörtern (S. 31). Die Übereinstimmung zweier Annotierender lag bei 93,80 %, die MFS-Baseline (erster WordNet-Sense) bei 78,89 %, das beste System bei 82,50 % (S. 32). Die MFS-Baseline schwankt zwischen den Texten; die Autoren vermuten textspezifische vorherrschende Senses (S. 33).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Feine Granularität gilt als eines der Haupthindernisse; WordNet kodiert Unterschiede, die auch für Menschen schwer erkennbar sind. Stand der Technik im Senseval-3-All-Words-Task etwa 65 %. | S. 30, Abschnitt 1 | referiert (Snyder & Palmer 2004; Edmonds & Kilgarriff 2002) |
| Hauptproblem beim Vergröbern ist die Subjektivität der Sense-Cluster. OntoNotes gruppiert, bis 90 % Übereinstimmung erreicht ist; diese Aufgabe bildet stattdessen auf ein vorhandenes Inventar mit Granularitätsstufen ab. | S. 30, Abschnitt 1 | Abgrenzung; OntoNotes referiert (Hovy et al. 2006) |
| Testkorpus: 5.377 laufende Wörter aus fünf Texten (drei WSJ-Texte wie in Task 17, ein Wikipedia-Artikel „Computer programming“, ein Auszug aus Steedmans *Knights of the Art*); die beiden letzten kamen hinzu, damit der Umfang früheren All-Words-Sets entspricht. d003 und d004 machen 51,87 % aus. | S. 30 bis 31, Abschnitt 2.1, Tab. 1 | eigene Daten |
| Grobes Inventar: automatische Abbildung von WordNet-2.1-Senses auf nummerierte Haupteinträge des ODE (Verfahren Navigli 2006, Disambiguierung der Definitionen mit SSI); Senses auf demselben ODE-Eintrag bilden ein Cluster, Senses ohne Treffer bleiben einzeln. Für die Testwörter von Hand durch den dritten Autor, einen Lexikografen; wo das nicht ging, blieb das WordNet-Inventar. | S. 31, Abschnitt 2.2 | eigenes Verfahren |
| Annotation aller Inhaltswörter (Nomen, Verben, Adjektive, Adverbien) durch den Lexikografen; Mehrwortausdrücke als solche markiert; ausgeschlossen u. a. Hilfsverben. Mehrere grobe Senses waren erlaubt, aber nur, wenn eine einzelne Zuweisung nicht möglich war. | S. 31, Abschnitt 2.3 | eigenes Verfahren |
| Von 2.316 annotierten Inhaltswörtern wurden 47 (2 %) ausgeschlossen, weil **kein** WordNet-Sense passte; 2.269 bilden das Testset. Nur 8 erhielten mehr als einen Sense (einmal zwei grobe, siebenmal zwei feine Senses). Die Autoren werten das als Hinweis, dass die Cluster für die große Mehrheit nicht mehrdeutig waren. | S. 31, Abschnitt 2.3 | eigenes Ergebnis, Deutung der Autoren |
| 29,88 % (678 von 2.269) der Instanzen sind im groben Inventar monosem. Mittlere Polysemie 3,06 grob gegenüber 6,18 in WordNet. | S. 31 bis 32, Tab. 2 | eigenes Ergebnis |
| Übereinstimmung: Abbildung von 590 Word Senses unabhängig durch einen zweiten Autor, paarweise 86,44 %. Annotation von 710 Testinstanzen durch einen zweiten Autor, paarweise **93,80 %**. Vergleichswerte mit WordNet: 72,5 % (Senseval-3 All-Words) und 67,3 % (OMWE). Folgerung: Die Übereinstimmung „strictly depends on the granularity“. | S. 32, Abschnitt 2.4 | eigene Messung; Vergleichswerte referiert (Snyder & Palmer 2004; Chklovski & Mihalcea 2002); die Folgerung beruht auf einem Vergleich mit der Literatur, nicht auf einem kontrollierten Versuch |
| Übereinstimmung gilt als Obergrenze für Systeme; deshalb sei eine viel höhere Zahl für die grobe Aufgabe erwünscht gewesen. | S. 32, Abschnitt 2.4 | Annahme der Autoren |
| Zwei Baselines: zufällig (Mittel über 1 / Zahl der groben Senses) und MFS = **erster WordNet-Sense**, also SemCor-Häufigkeiten; als richtig zählt der erste Sense, wenn er im vom Lexikografen gewählten Cluster liegt. | S. 32, Abschnitt 3 | eigene Definition |
| Ergebnisse: 14 Systeme aus 12 Teams; MFS 78,89 %, Zufall 52,43 %. Das System eines Organisators (UOR-SSI, 83,21) wird getrennt geführt. Abstand MFS zu den besten Systemen etwa 5 Punkte, vergleichbar mit Senseval-3. | S. 32 bis 33, Abschnitt 4, Tab. 3 | eigenes Ergebnis |
| **Dokumente:** „documents from some domains seem to have predominant senses different from those in SemCor“; MFS ist bei d004 (Informatik) und d005 (Biografie) schwächer. „We believe this is due to the fact that these documents have specific predominant senses“. | S. 33, Abschnitt 4; Tab. 5 (S. 34) | eigenes Ergebnis (Streuung), Erklärung als **Vermutung** der Autoren |
| Verschiedene Systeme schneiden je Dokument und je Wortart verschieden ab. MFS liegt bei Adjektiven und Adverbien nahe an den besten Systemen, bei Verben mehr als 3, bei Nomen etwa 5 Punkte darunter. | S. 33, Tab. 5 und 6 | eigenes Ergebnis |
| Alle Systeme über der MFS-Baseline nutzten MFS als Rückfall, wenn sie keinen Sense ausgaben. | S. 34, Abschnitt 5; Tab. 7 (S. 35) | eigenes Ergebnis (Fragebogen an die Teilnehmenden) |
| Offene Fragen: ob die Systeme die groben Senses schon ausschöpfen; ob grobe Senses in Anwendungen nützen; ein vollständiges grobes Inventar fehlt. Auf Informatik schnitten überwachte Systeme wegen ihrer Trainingsdaten schlechter ab. | S. 35, Abschnitt 6 | Schlussfolgerung, teils Deutung |

## Daten, Methode, Zahlen

**Tab. 1 (S. 31), Testtexte:**

| Text | Domäne | Wörter | annotiert |
|---|---|---|---|
| d001 | JOURNALISM | 951 | 368 |
| d002 | BOOK REVIEW | 987 | 379 |
| d003 | TRAVEL | 1.311 | 500 |
| d004 | COMPUTER SCIENCE | 1.326 | 677 |
| d005 | BIOGRAPHY | 802 | 345 |
| gesamt | | 5.377 | 2.269 |

**Tab. 2 (S. 32), Polysemie im groben Inventar:** monosem 358 N / 86 V / 141 A / 93 R = 678; polysem 750 / 505 / 221 / 115 = 1.591; gesamt 1.108 / 591 / 362 / 208 = 2.269.

**Tab. 5 (S. 34), Präzision = Recall der MFS-Baseline je Text:** d001 85,60; d002 84,70; d003 77,80; d004 75,19; d005 74,20. Bestes Teilnehmersystem je Text zum Vergleich: d001 NUS-PT 88,32; d002 NUS-ML 88,39; d003 NUS-PT 83,40; d004 UPV-WSD 77,11; d005 NUS-PT 81,45. Das Organisatorensystem UOR-SSI erreicht bei d004 86,85. Kleiner Fehler im Werk: Tab. 5 markiert für d004 NUS-ML (76,66) als besten Wert, UPV-WSD liegt mit 77,11 darüber (am Seitenbild geprüft). Die Spannweite der MFS über fünf Texte beträgt also 11,4 Punkte; bei d004 liegt das beste Teilnehmersystem nur 1,9 Punkte über MFS.

**Tab. 6 (S. 33), F1 nach Wortart (Auswahl):**

| System | N | V | A | R |
|---|---|---|---|---|
| NUS-PT (bestes) | 82,31 | 78,51 | 85,64 | 89,42 |
| MFS | 77,44 | 75,30 | 84,25 | 87,50 |

**Tab. 3 und 4 (S. 33):** bestes Teilnehmersystem NUS-PT 82,50; MFS 78,89 an fünfter Stelle der Tabelle, hinter vier Systemen. Mit MFS als Rückfall für nicht beantwortete Instanzen verschieben sich sechs Systeme (Tab. 4).

**Annotierende:** ein Lexikograf (dritter Autor) für alles; ein zweiter Autor unabhängig für 590 Abbildungen und 710 Instanzen (S. 32). Welcher der beiden anderen Autoren, wird nicht gesagt.

## Wörtliche Stellen

> „The main issue is certainly the subjectivity of sense clusters.“ (S. 30)

> „This figure, compared to those in the literature for fine-grained human annotations, gives us a clear indication that the agreement of human annotators strictly depends on the granularity of the adopted sense inventory.“ (S. 32)

> „[…] documents from some domains seem to have predominant senses different from those in SemCor. […] We believe this is due to the fact that these documents have specific predominant senses, which correspond less often to the most frequent sense in SemCor than for the other three documents.“ (S. 33)

## Bezug zur Dissertation

**Prüfauftrag zu `goldstandard/LITERATUR-STICHPROBE.md`** („MFS hängt vom Dokument ab“: Navigli et al. 2007 ○):

- **Am Original klärbar, aber nur als Vermutung der Autoren.** Gemessen ist: Die MFS-Baseline (aus SemCor, erster WordNet-Sense) streut über die fünf Texte von 74,20 bis 85,60 (Tab. 5, S. 34). Erklärt wird das als textspezifische vorherrschende Senses, eingeleitet mit „seem to“ und „We believe“ (S. 33). Ein Test, eine Auswertung nach Lemmata oder eine Trennung von Text und Domäne gibt es nicht; jeder Text ist zugleich eine eigene Domäne, also sind Text- und Domäneneffekt nicht zu trennen.
- **Vorschlag:** Status ✔ für „MFS-Baseline streut zwischen den Texten (74,20 bis 85,60; Tab. 5, S. 34); die Autoren vermuten textspezifische vorherrschende Senses (S. 33)“. Die Deutung als Klumpeneffekt bleibt eigene. Für PROTOKOLL §4.4, Punkt 4 ist das ein zusätzlicher, schwacher Beleg für die Obergrenze pro Text.

**Prüfauftrag zu `goldstandard/LITERATUR-IAA.md`** („feinkörnig ca. 67 bis 72 %, grobkörnig ca. 90 bis 94 %“, Navigli et al. 2007 ✔):

- **Gedeckt** für 67,3 % und 72,5 % (fein, referiert) und 93,80 % (grob, eigene Messung) (S. 32). **Einschränkung:** Die 93,80 % sind die Übereinstimmung zweier **Autoren** des Papiers, einer davon der Lexikograf, der das grobe Inventar für genau diese Wörter selbst von Hand abgebildet hat; gemessen an 710 von 2.269 Instanzen (S. 31 bis 32). Unabhängige, nicht beteiligte Annotierende gab es nicht. Die Folgerung „strictly depends on the granularity“ stützt sich auf einen Vergleich mit Werten aus anderen Studien, nicht auf denselben Items mit beiden Inventaren. Für die Dissertation heißt das: Die Zahl taugt als Größenordnung, nicht als kontrollierter Granularitätseffekt.

**Weitere Bezüge:**

- **PROTOKOLL §9.1, Punkt 7 und offener Punkt 12 (grobe Ebene vorab definieren):** Die Aufgabe definiert die grobe Ebene vor der Annotation über ein externes Inventar (ODE), nicht nachträglich durch Zusammenlegen. Das ist ein Vorbild für das Protokoll (grobe Ebene über den Zahlencode des Begriffssystems, `knowledge/data.md`, B11). Anders als hier wird im Protokoll fein annotiert und grob ausgewertet; hier wurde direkt grob annotiert (S. 31).
- **PROTOKOLL §7, Schritt 2 und A32 (Instrument mit gröberen Senses, wenn α unter 0,67 bleibt):** Das Papier zeigt, dass ein gröberes Inventar die Übereinstimmung auf über 90 % bringen kann, aber mit dem Vorbehalt oben. Das Protokoll sollte, falls es zu diesem Ausweg kommt, den Effekt auf denselben Items messen (fein und grob), was §9.1, Punkt 7 bereits vorsieht.
- **PROTOKOLL §9.2 (MFS-Baseline und Rückfall auf den ersten Sense):** MFS heißt hier erster WordNet-Sense, also eine Reihenfolge, die aus SemCor-Häufigkeiten stammt (S. 32). In der MHDBDB trägt die Lexikonreihenfolge diese Bedeutung nicht (nur 59 % Mehrheitssense, `knowledge/data.md`, B8). Wer Navigli et al. für die Rückfallregel zitiert, muss diesen Unterschied nennen.
- **PROTOKOLL §6 (`KEINE_PASST`, `MEHRERE`):** 2 % der Inhaltswörter hatten keinen passenden WordNet-Sense und wurden ausgeschlossen; nur 8 von 2.269 erhielten mehrere Senses (S. 31). Beides sind Vergleichsgrößen für die Häufigkeit der Ausweichlabels; das Protokoll erwartet beim MHDBDB-Inventar mehr `KEINE_PASST` (`knowledge/data.md`, B9). Die Regel „mehrere nur, wenn eine einzelne Zuweisung nicht möglich ist“ (S. 31) entspricht der Kurzanleitung v0.3 zu „Mehrere passen“ (PROTOKOLL §12, Punkt 17).
- **PROTOKOLL §4.3 und §9.1, Punkt 6 (Wortart):** MFS ist bei Adjektiven und Adverbien kaum zu schlagen, bei Nomen und Verben schon (Tab. 6, S. 33). Stützt die Aufschlüsselung nach Wortart.
- **Systeme nutzen MFS als Rückfall** (S. 34): Ein LLM-Ergebnis über der MFS kann teils aus MFS-ähnlichem Verhalten stammen; die Nicht-MFS-Auswertung (§9.2, Maru et al. 2022) trennt das.

## Grenzen und Einwände

- Nur ein Hauptannotator; Übereinstimmung nur mit einem Mitautor auf einem Teil der Daten; keine zufallskorrigierten Maße, keine Konfusionsmatrix.
- Das grobe Inventar für die Testwörter wurde vom selben Lexikografen gebaut, der annotierte. Das kann die Übereinstimmung zwischen Inventar und Annotation begünstigen.
- Fünf Texte, jeder eine eigene Domäne: Text- und Domäneneffekt sind nicht trennbar, Aussagen über Dokumentabhängigkeit bleiben Vermutung.
- Keine Signifikanztests oder Intervalle; Abstände von wenigen Punkten zwischen Systemen sind auf 2.269 Instanzen nicht abgesichert.
- Ein Organisator reichte ein eigenes System ein (getrennt geführt, S. 32).
- Englisch, WordNet und ODE; Übertragung auf ein onomasiologisches Inventar wie das MHDBDB-Begriffssystem nicht berührt.

## Weiterführend

- Navigli 2006, Meaningful clustering of senses helps boost WSD performance, COLING-ACL 2006, S. 105 bis 112 (S. 31, 35): Verfahren der groben Clusterung.
- Hovy et al. 2006, OntoNotes: The 90% solution (S. 30, 35): liegt als Zusammenfassung vor (`Hovy-etal-2006-OntoNotes.md`).
- Snyder & Palmer 2004, The English all-words task, SENSEVAL-3, S. 41 bis 43 (S. 30, 32, 35): Quelle der 72,5 %.
- Edmonds & Kilgarriff 2002, Einführung ins Sonderheft zur WSD-Evaluation, *Natural Language Engineering* 8(4) (S. 30, 33, 35).
- SemEval-2007 Task 17 (grobe Lexical Sample), im Text erwähnt (S. 30), nicht im Literaturverzeichnis.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
