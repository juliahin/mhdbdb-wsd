# Gale, Church & Yarowsky 1992: Ober- und Untergrenzen der WSD-Evaluation

**Datei:** `pdf/Gale-etal-1992-Upper-Lower-Bounds.pdf` (nur lokal; 8 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Tabellen 1 bis 3 am Seitenbild geprüft, DOI aufgelöst. Das lokale PDF ist byte-gleich mit https://aclanthology.org/P92-1032.pdf (SHA-256 verglichen am 2026-11-13); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 248 + n (PDF 1 = S. 249, PDF 8 = S. 256). Unten stehen gedruckte Seiten.

In der Sekundärliteratur heißt das Werk je nach Quelle „Gale et al. 1992a“ oder „1992b“ (`literatur/beschaffung-2026-10-30/2-vorschlaege.md`, Nr. 12); gemeint ist immer dieser ACL-Beitrag, nicht „One Sense Per Discourse“ (eigene Zusammenfassung `Gale-etal-1992-One-Sense-Per-Discourse.md`).

## Bibliografie

- **Vollständig:** Gale, William, Kenneth Ward Church & David Yarowsky (1992). Estimating Upper and Lower Bounds on the Performance of Word-Sense Disambiguation Programs. In: *30th Annual Meeting of the Association for Computational Linguistics*. Newark, Delaware: Association for Computational Linguistics, S. 249 bis 256.
- **DOI/URL:** https://doi.org/10.3115/981967.981999 (aufgelöst am 2026-11-13, leitet auf das ACM-Portal; Crossref: S. 249 bis 256, Tagung 28.06. bis 02.07.1992, Newark, Delaware); https://aclanthology.org/P92-1032 (BibTeX der Anthology: Juni 1992, S. 249 bis 256, dieselbe DOI).
- **Lizenz:** CC BY-NC-SA 3.0 (ACL Anthology, Material vor 2016, laut FAQ der Anthology, abgerufen 2026-11-13).
- **Art:** Konferenzbeitrag (ACL 1992)
- **Sprache:** Englisch

## Worum es geht

Die Autoren haben zwei WSD-Systeme gebaut (zweisprachig an den kanadischen Hansards, einsprachig an Roget's Thesaurus und Grolier's Encyclopedia) und suchen einen objektiven Maßstab, um deren Leistung zu beurteilen (S. 249). Weil die Literatur keinen Evaluationsstandard bietet, schlagen sie vor, die erreichbare Leistung einzugrenzen: Die **Untergrenze** ist ein System, das den Kontext ignoriert und immer den häufigsten Sense vergibt; die **Obergrenze** ist die Fähigkeit menschlicher Urteilender, untereinander übereinzustimmen (S. 252 bis 254). Die Untergrenze liegt bei 75 % über ambige Wortarten gemittelt (S. 254); die Obergrenze hängt stark von der Aufgabe ab: 68 % bei Jorgensens Klassifikationsexperiment, 96,8 % in einem eigenen Unterscheidungsexperiment („gleicher Sense oder nicht?“) (S. 254 bis 255). Daraus folgt ihr Kernargument: Zwischen Untergrenze und Obergrenze muss genug „dynamic range“ liegen, sonst lassen sich bessere von schlechteren Systemen nicht unterscheiden (S. 254).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Die Literatur bietet kein Vorbild für die Evaluation; viele Arbeiten vermeiden quantitative Evaluation, weil glaubwürdige Leistungsschätzungen schwer zu gewinnen sind. | S. 249 (Abstract), S. 251, Abschnitt 3 | Befund der Autoren zur Literatur |
| Die übliche Praxis, wenige von Hand gewählte Wörter mit einem menschlichen Urteil zu vergleichen, hat als größtes Problem, dass die Stichprobe für das Vokabular nicht repräsentativ ist. Wer auf neue Wörter schließen will, braucht eine **Zufallsstichprobe** von Wörtern, nicht Wörter aus der Literatur. | S. 251, Abschnitt 3 | eigene methodische Aussage |
| Vergleiche über Experimente hinweg sind unsicher wegen verschiedener Korpora, Wörter, Urteilender, Behandlung von Precision und Recall und Hilfswerkzeuge. | S. 252 | eigene Aussage |
| **Untergrenze:** ein „straw man system“, das den Kontext ignoriert und überall den wahrscheinlichsten Sense vergibt. Vernünftige Systeme sollten es schlagen, „though not all such systems actually do“. | S. 252 bis 253, Abschnitt 5.1 | eigener Vorschlag |
| Die Baseline ist **nicht operational**: Eigentlich müsste sie den häufigsten Sense vorab schätzen; die Autoren lassen sie stattdessen den häufigsten Sense **aus dem Testset** ablesen („cheat“). Sie kann daher nicht unter den Zufall (100/k % bei k Senses) fallen. | S. 253 | eigene Einschränkung |
| Die Baseline behandelt Fehler 1. und 2. Art gleich; bei ungleichen Kosten (z. B. Lexikograf:innen, die seltene Fälle suchen) kann sie irreführen. | S. 253 | eigene Einschränkung |
| Die Baseline geht schlecht mit schiefen Verteilungen um; ein Maß wie die Entropie könnte das besser abbilden (Fußnote 9). | S. 253, Anm. 9 | Vorschlag, nicht umgesetzt |
| Für die zwölf Wörter aus der Literatur streut die Baseline zwischen 48 % (*bow*) und 96 % (*issue*), Mittel 70 %; Yarowsky (1992) liegt bei *issue* unter ihr. | S. 253, Tab. 2 | eigenes Ergebnis |
| Zufallsstichprobe von 97 Wörtern (Nomen): 67 eindeutig, Baseline 93 % über Tokens, 92 % über Typen; ohne die eindeutigen 81 % über Tokens, 75 % über Typen. Die Wortauswahl aus der Literatur überbetont also schwierige Fälle. | S. 253 bis 254 | eigenes Ergebnis |
| **Obergrenze:** geschätzt als Fähigkeit menschlicher Urteilender, mit anderen (oder sich selbst) übereinzustimmen; sie hängt stark von der Aufgabendefinition ab. | S. 254, Abschnitt 5.2 | eigener Vorschlag |
| Jorgensen (1990): zwölf hochfrequente Nomen aus dem Brown Corpus, neun Personen sortieren Belegkarten nach Sense, eine bis zwei Wochen später mit Wörterbuchdefinitionen; mittlere Übereinstimmung 68 %, also unter der Baseline. | S. 254 | referiert (Jorgensen 1990), Umrechnung des A-D-Verhältnisses in Prozent durch die Autoren |
| **Dynamic range:** Ist die Aufgabe für Urteilende zu schwer, bleibt zwischen Messgrenze und Baseline kaum Raum, und bessere und schlechtere Systeme lassen sich nicht unterscheiden. Deshalb definieren die Autoren die Aufgabe von Klassifikation in **Diskrimination** um („gleicher Sense oder nicht?“). | S. 254 | eigenes Argument |
| Eigenes Experiment: fünf Urteilende (die drei Autoren und zwei Kolleg:innen), OALD-Definitionen, 82 Belegpaare für 9 polyseme Nomen; Übereinstimmung mit der Mehrheitsmeinung 96,8 % im Mittel, 99,1 % ohne Urteilende:n 2. | S. 254 bis 255, Tab. 3 | eigenes Ergebnis |
| Von den 82 Paaren stammen 54 aus demselben Diskurs; sie wurden von der Mehrheit in 96,9 % der Fälle als gleicher Sense beurteilt. Die übrigen 28 sind Kontrollpaare. | S. 255 | eigenes Ergebnis (zu dieser Zahl siehe „Grenzen“) |
| Die Diskursbindung („one sense per discourse“) eignet sich als schnelles Prüfmaß, braucht aber ein Gegenmaß, weil sie ein System belohnt, das alle Belege einem Sense zuweist. | S. 255 | eigene Folgerung |
| Fazit: Untergrenze = Baseline des häufigsten Senses; Obergrenze = Grenze der **Messbarkeit**, dominiert von der Übereinstimmung der Urteilenden; der Wert hängt am Versuchsdesign. | S. 255 bis 256, Abschnitt 7 | Zusammenfassung |
| POS-Tagging zum Vergleich: Baseline etwa 90 %, Obergrenze durch Übereinstimmung etwa 95 %; die meisten Tagger seien an der Messgrenze. | S. 256 | als „generally accepted“ referiert, ohne Beleg |

## Daten, Methode, Zahlen

**Tab. 1 (S. 252, am Seitenbild geprüft):** Yarowsky (1992) auf zwölf Wörtern aus der Literatur, Mittel 92 %; Spannweite 72 % (*interest*) bis 99 % (*bass*, *galley*, *mole*). Vergleichswerte anderer Systeme in Spalte 3 (z. B. *interest* 72 % bei Black 1988, 70 % bei Zernik 1990).

**Tab. 2 (S. 253, am Seitenbild geprüft), Baseline gegen Yarowsky (1992):**

| Wort | Baseline | Yarowsky |
|---|---|---|
| issue | 96 % | 94 % |
| duty | 87 % | 96 % |
| galley | 83 % | 99 % |
| star | 83 % | 96 % |
| taste | 74 % | 93 % |
| bass | 70 % | 99 % |
| slug | 62 % | 97 % |
| sentence | 62 % | 98 % |
| interest | 60 % | 72 % |
| mole | 59 % | 99 % |
| cone | 51 % | 77 % |
| bow | 48 % | 91 % |
| Mittel | 70 % | 92 % |

**Zufallsstichprobe (S. 253 bis 254):** 97 Wörter, 67 eindeutig (Liste in Anm. 10), 30 ambig mit Sense-Zahl und Baseline (z. B. *virus* 2 Senses, 98 %; *drive* 3, 49 %). Baseline 93 % (Tokens) bzw. 92 % (Typen); ohne eindeutige Wörter 81 % bzw. 75 %.

**Tab. 3 (S. 255, am Seitenbild geprüft), Übereinstimmung mit der Mehrheitsmeinung, 82 Paare:** Urteilende 1 bis 5: 82 (100,0 %), 72 (87,8 %), 81 (98,7 %), 82 (100,0 %), 80 (97,6 %); Mittel 96,8 %, ohne Urteilende:n 2 99,1 %. Nachgerechnet: (100 + 87,8 + 98,7 + 100 + 97,6) / 5 = 96,82.

**Vorversuch (S. 254):** 108 zufällig gezogene Nomen (darin die 97 Wörter), drei Urteilende (die Autoren), 100 Belegsätze aus je einem Grolier-Artikel; nur 6 von 300 Urteilen sahen mehrere Senses in einem Artikel. Nicht blind.

## Wörtliche Stellen

> „We will estimate the lower bound by evaluating the performance of a straw man system, which ignores context and simply assigns the most likely sense in all cases.“ (S. 252)

> „[…] we decided to "cheat" and let the baseline system peek at the test set and "estimate" the most likely sense for each word as the more frequent sense in the test set.“ (S. 253)

> „We will attempt to estimate an upper bound on performance by estimating the ability for human judges to agree with one another (or themselves).“ (S. 254)

> „If the task is too hard […], then there will be almost no room between the limits of the measurement and the baseline.“ (S. 254)

> „If the study had been intended to support predictions on new words, then the study should have used a random sample of such words, rather than a sample of words from the literature.“ (S. 251)

## Bezug zur Dissertation

- **PROTOKOLL §1 und §9.2 (MFS-Baseline als Boden):** Das Werk ist die Primärquelle für die Idee, die MFS-Baseline als Untergrenze zu setzen (bisher nur nach Ide & Véronis 1998 zitiert, `goldstandard/VORSCHLAEGE-2026-10.md`, „Primärquellen statt Sekundärzitat“). Wichtiger noch: GCY nennen die eigene Baseline selbst nicht operational, weil sie den häufigsten Sense aus dem Testset abliest (S. 253). Das stützt A4 und §9.2 direkt: Die MFS wird dort aus Silber **ohne** die Stichproben-Tokens gelernt, also genau in der Form, die GCY „ideally“ nennen. Zugleich erklärt es, warum die präregistrierten 66,7 % und die 0,744 aus `goldstandard-test.py` optimistisch sind: Beide sind in-sample wie die GCY-Baseline.
- **PROTOKOLL §9.2 („Die menschliche IAA ist die Obergrenze“) und Vorschlag V26:** GCY fassen die Obergrenze als Grenze der **Messbarkeit**, nicht als Grenze dessen, was ein System können kann (S. 254, S. 255 bis 256: „the limit of our ability to measure performance“). Das passt zu V26 (`VORSCHLAEGE-2026-10.md`), „Obergrenze“ als Referenzwert zu lesen: Ein LLM-Wert über der IAA wäre nach GCY kein Widerspruch, sondern nicht mehr messbar.
- **PROTOKOLL §7, A32 (Stoppregel des Pilots) und §4.7 (Teststärke):** Das Argument des „dynamic range“ (S. 254) betrifft die Dissertation unmittelbar. Liegt die menschliche Übereinstimmung nach dem Pilot bei α um 0,67 bis 0,80 (laut §7 nahe an der Rohübereinstimmung) und die MFS-Baseline in der Größenordnung von 0,67 bis 0,74, bleibt zwischen Boden und Decke wenig Raum, in dem sich ein LLM-Vorsprung messen lässt. Vorschlag: im Auswertungsplan (§9.2) den Abstand zwischen menschlicher Rohübereinstimmung und MFS-Genauigkeit auf denselben Items ausdrücklich berichten; die Stoppregel aus A32 bleibt davon unberührt, gewinnt aber eine zweite Lesart.
- **PROTOKOLL §4.3 (Schiefe als Kovariate):** GCY zeigen, dass die Baseline je Wort zwischen 48 und 96 % liegt (Tab. 2, S. 253) und schlagen in Anm. 9 ein Entropiemaß für schiefe Verteilungen vor. Das ist ein früher Beleg dafür, MFS-Anteil und Entropie pro Item mitzuführen; gemessen wird der Zusammenhang erst bei Kilgarriff & Rosenzweig 2000.
- **PROTOKOLL §4.4 (zufällige Ziehung statt Auswahl):** S. 251 ist ein klarer Beleg gegen handverlesene Testwörter; die Zufallsstichprobe der 97 Wörter senkt die Baseline-Erwartung gegenüber der Literaturauswahl deutlich (S. 253 bis 254). Das stützt die zufällige Ziehung aus Zellen.
- **PROTOKOLL §4.4, Punkt 4 (Klumpeneffekt):** Dieses Werk berichtet die Diskursbindung nur als Nebenergebnis (S. 255); die Primärquelle dafür ist „One Sense Per Discourse“ (eigene Zusammenfassung). Die Zahlen beider Werke für dieselben 54 Paare weichen voneinander ab (96,9 % hier, 94 % dort, siehe „Grenzen“); für das Protokoll sollte die Fassung mit nachvollziehbarer Rechnung (51/54, H92-1045, S. 236) zitiert werden.
- **`goldstandard/LITERATUR-IAA.md`:** Das Werk ist dort nicht zitiert. Die Spanne „Jorgensen 68 % gegenüber 96,8 %“ belegt dieselbe Aussage wie die Zeile zu Ng et al. 1999 und Hovy et al. 2006: Die Aufgabendefinition (dort die Granularität) ist der stärkste Einflussfaktor auf Übereinstimmung (§9.1, Punkt 7).

## Grenzen und Einwände

- **Die 96,8 % sind kein IAA-Wert im heutigen Sinn.** Gemessen wird die Übereinstimmung jeder Person mit der **Mehrheitsmeinung**, an der sie selbst beteiligt ist (S. 255); drei der fünf Urteilenden sind die Autoren, und die Aufgabe ist binär (gleich oder verschieden), nicht die Wahl aus einem Inventar. Kilgarriff (1998, ITRI-Fassung S. 10) nennt die Umdefinition „highly problematic“, weil damit der Bezug zur eigentlichen Klassifikationsaufgabe verloren geht.
- **Widerspruch zum Schwesterbeitrag:** Hier sind die 54 Paare aus demselben Diskurs „in 96.9% of the cases“ als gleicher Sense beurteilt (S. 255); in „One Sense Per Discourse“ (S. 236) sind es 51 von 54, also 94 %. 96,9 % lässt sich aus 54 Paaren nicht als ganzzahliger Anteil bilden (52/54 = 96,3 %, 53/54 = 98,1 %). Welche Zahl stimmt, klärt keines der beiden Werke.
- Jorgensens 68 % ist eine Umrechnung des A-D-Verhältnisses durch die Autoren (S. 254) und stammt aus einer Sortieraufgabe ohne vorgegebenes Inventar im ersten Durchgang; die Vergleichbarkeit mit Sense-Wahl ist begrenzt.
- Die Untergrenze von 75 % gilt für ambige Wörter einer Zufallsstichprobe von Nomen aus einer Enzyklopädie; Verben und Adjektive kommen nicht vor.
- Keine Konfidenzintervalle, keine Zufallskorrektur; die POS-Zahlen auf S. 256 sind ohne Beleg.
- Übertragbarkeit: Englisch, zwei bis sechs Senses aus Wörterbüchern bzw. Übersetzungen; ein onomasiologisches Inventar und Mittelhochdeutsch sind nicht berührt. Der Gedanke von Boden und Decke ist dagegen sprachunabhängig.

## Weiterführend

- Jorgensen, Julia C. (1990). The psychological reality of word senses. *Journal of Psycholinguistic Research* 19, 167 bis 190 (S. 254, S. 256): Primärquelle für die 68 %.
- Gale, Church & Yarowsky (1992). One Sense Per Discourse. DARPA Speech and Natural Language Workshop (S. 254, S. 256): liegt als PDF vor.
- Yarowsky (1992), Roget-Kategorien, COLING-92 (S. 251): Thesaurus-Kategorien als Sense-Inventar, dem Begriffssystem der MHDBDB strukturell näher als WordNet.
- Lesk (1986), SIGDOC (S. 251): Evaluation dort nur kurz; fehlt weiterhin als PDF (`literatur/README.md`).
- Black (1988) und Zernik (1990): frühe Einzelwort-Evaluationen (S. 251 bis 252).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
