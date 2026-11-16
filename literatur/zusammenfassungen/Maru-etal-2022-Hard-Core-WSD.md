# Maru, Conia, Bevilacqua & Navigli 2022: Nibbling at the Hard Core of Word Sense Disambiguation

**Datei:** `pdf/Maru-etal-2022-Hard-Core-WSD.pdf` (nur lokal; 14 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen (Tabellen 1 bis 7 aus der Textebene, das PDF ist digital gesetzt; Zeilensummen von Tab. 4 und die 91,1 % nachgerechnet). Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-16), also die Verlagsfassung; es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 4723 + n (PDF 1 = S. 4724, PDF 14 = S. 4737). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Maru, Marco, Simone Conia, Michele Bevilacqua & Roberto Navigli (2022). Nibbling at the Hard Core of Word Sense Disambiguation. In: Smaranda Muresan, Preslav Nakov & Aline Villavicencio (Hg.), *Proceedings of the 60th Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*. Dublin: Association for Computational Linguistics, Mai 2022, S. 4724 bis 4737.
- **DOI/URL:** https://doi.org/10.18653/v1/2022.acl-long.324 (aufgelöst auf die ACL Anthology, 2026-11-16); https://aclanthology.org/2022.acl-long.324. Herausgeber:innen, Ort und Seiten im BibTeX der Anthology ✔; Kopfzeile S. 4724: „pages 4724 - 4737, May 22-27, 2022“ ✔.
- **Lizenz:** CC BY 4.0 (ACL Anthology, Material ab 2016, abgerufen 2026-11-16).
- **Art:** Konferenzbeitrag (ACL 2022, Long Paper)
- **Sprache:** Englisch
- **Daten:** Testsets und Systemvorhersagen unter https://github.com/SapienzaNLP/wsd-hard-benchmark (S. 4724, 4732; nicht aufgerufen).

## Worum es geht

Englische WSD-Systeme erreichen auf dem Standardrahmen (ALL, Raganato et al. 2017) über 80 % F1, was oft als menschliche Leistung gilt (S. 4724). Die Autoren untersuchen die 541 Instanzen, die alle sieben untersuchten Systeme falsch lösen, den „hard core“ (S. 4726 bis 4727): Dort sagen die Systeme zu mindestens 62,7 % den ersten WordNet-Sense voraus, der nur bei 2,0 % der Instanzen richtig wäre (Tab. 1, S. 4727). Ein erfahrener Linguist hat ALL neu annotiert; nur 72,6 % der Instanzen blieben unverändert, Fehler im Gold und Lücken im Inventar häufen sich im hard core (Tab. 4, S. 4729). Daraus entstehen bereinigte Testsets, ein neues Challenge-Set „42D“ mit 370 Instanzen ohne ersten Sense und ohne SemCor-Sense und die Aufteilung hardEN/softEN; zusätzlich empfehlen sie Macro-F1 nach Sense (S. 4730 bis 4731).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| 80 % F1 gilt oft als menschliche Leistung, weil es der höchsten berichteten Übereinstimmung entspricht; aktuelle Systeme erreichen oder übertreffen das. | S. 4724, Abschnitt 1 | referiert (Edmonds & Kilgarriff 2002; Navigli et al. 2007; Palmer et al. 2007) |
| Trotzdem machen Systeme Fehler, die kein Mensch machen würde (Beispiele *wind*, *couple*). F1 sei daher nicht „at face value“ zu nehmen. | S. 4724 bis 4725, Abschnitt 1 | eigene Beispiele und These |
| Auswertung auf ALL beschränkt sich meist auf Gesamtwert und Wortart; das berge die Gefahr von „collective hill-climbing“ und Überanpassung an alternde Testsets. | S. 4725, Abschnitt 2 | Einschätzung der Autoren |
| Untersucht werden sieben Systeme: ARES, BEM, ESCHER, EWISER, Generationary, GlossBERT (alle überwacht, mit vortrainierten Sprachmodellen) und SyntagRank (wissensbasiert). | S. 4726, Abschnitt 3 | Beschreibung |
| Macro-F1 nach Sense statt nur Micro-F1, weil Micro-F1 häufigen Senses mehr Gewicht gibt und „mediocre performances on least frequent senses“ verdeckt. Macro-F1 liegt stets unter Micro-F1. | S. 4727, Abschnitt 4.1; S. 4728; S. 4731 | eigene Methodenwahl und Ergebnis |
| **MFS-Bias:** Auf ALL sagen die Systeme den ersten WordNet-Sense (WN1st) zu mindestens 69 % voraus, im Gold sind es 65,2 %. Im hard core mindestens 62,7 %, im Gold 2,0 %. Das wissensbasierte SyntagRank ist am stärksten verzerrt, Generationary am wenigsten. | S. 4727 bis 4728, Tab. 1 oben | eigenes Ergebnis |
| **Trainingsdaten-Bias:** Im hard core sagen die Systeme zu mindestens 95 % einen in SemCor belegten Sense voraus, im Gold sind es 67,1 %. | S. 4728, Tab. 1 unten | eigenes Ergebnis |
| Auf ALL ohne WN1st-Instanzen (ALLno1st, 2.525) liegen die Systeme bei 26,9 bis 54,2 Macro-F1; auf ALL ohne SemCor-Senses (ALLnoSC) bei 55,1 bis 71,0. Die Rangfolge der Systeme ändert sich gegenüber ALL. | S. 4727 bis 4728, Tab. 2 | eigenes Ergebnis |
| **Neuannotation:** Ein Linguist mit viel Erfahrung im Annotieren mit WordNet prüft jede Instanz von ALL (ohne SemEval-2007) und SemEval-2010 und vergibt eines von sechs Labels: unverändert, fine-grained (Senses ergänzen), Fehler Token/Lemma, Fehler Wortart, Fehler Sense, Fehler Inventar (kein passender Sense in WordNet 3.0). | S. 4728, Abschnitt 4.2 | eigenes Verfahren, **ein** Annotator |
| Auf ALL- (5.523 polyseme Instanzen) blieben 72,6 % unverändert; im hard core (ALLHC-, 500) nur 44,6 %, mit 17,8 % Sense-Fehlern und 14,2 % Inventarlücken. Der hard core sei daher auch für Menschen schwer. | S. 4729, Tab. 4 | eigenes Ergebnis, Deutung der Autoren |
| Zählt man unverändert und fine-grained zusammen und lässt Wortart-, Token- und Inventarfehler weg, stimmt der Linguist zu 91,1 % mit dem Gold überein, mehr als 10 Punkte über den üblichen Schätzungen. | S. 4729 bis 4730, Abschnitt 4.2 | eigene Rechnung |
| Bereinigte Testsets: ALLNEW (4.917 polyseme Instanzen) und S10NEW (955), korrigiert vom selben Linguisten. Die Rangfolge der Systeme ändert sich durch die Korrektur nicht. | S. 4730 bis 4731, Abschnitt 5.2 und 5.4 | eigenes Ergebnis |
| **42D:** 370 Instanzen aus 42 BNC-Absätzen, je einer pro BabelNet-Domäne; Gold-Sense nie in SemCor und nie WN1st. Bestes System (ESCHER) 54,1 Micro-F1, weit unter 80 %. | S. 4730 bis 4731, Abschnitt 5.1 und 5.4; Anhang A, S. 4737 | eigenes Ergebnis |
| **Übereinstimmung auf 42D:** Ein zweiter Linguist annotierte 42D blind; Rohübereinstimmung 79,6 %, niedriger als für ALL, aber 42D sei viel schwerer. | S. 4737, Anhang A | eigene Messung |
| **hardEN** (476 Instanzen, die kein System löst, aus ALLNEW, S10NEW und 42D) und **softEN** (5.766 übrige). | S. 4730, Abschnitt 5.3 | eigenes Ergebnis |
| Ensembles (Mehrheit der sieben Systeme, gleich oder nach Rang gewichtet) helfen auf ALLNEW leicht, auf 42D schaden sie; auf hardEN können sie per Konstruktion nichts lösen. | S. 4731 bis 4732, Abschnitt 6, Tab. 6 | eigenes Ergebnis |
| Training mit einem automatisch erzeugten Beispiel pro Sense (K1) hebt ESCHER auf hardEN auf 35,3 Macro-F1, senkt softEN aber um mehr als 18 Punkte. Eine flachere Sense-Verteilung im Training allein reicht nicht. | S. 4732, Abschnitt 6, Tab. 7 | eigenes Ergebnis; Bezug auf Postma et al. 2016 und Loureiro et al. 2021 |

## Daten, Methode, Zahlen

**Tab. 1 (S. 4727), Anteil der Vorhersagen in %:**

| Set | Inst. | mono | ARES | BEM | ESR | EWR | GEN | GLB | SYN | Gold |
|---|---|---|---|---|---|---|---|---|---|---|
| ALL, WN1st | 7.253 | 1.301 | 71,3 | 72,6 | 71,2 | 72,7 | 69,0 | 74,8 | 81,1 | 65,2 |
| ALLHC, WN1st | 541 | 0 | 64,7 | 71,0 | 68,6 | 67,8 | 62,7 | 70,6 | 80,2 | 2,0 |
| ALL, in SemCor | 7.253 | 1.301 | 88,2 | 87,4 | 86,3 | 88,8 | 85,9 | 88,6 | 88,8 | 84,3 |
| ALLHC, in SemCor | 541 | 0 | 96,9 | 96,7 | 96,5 | 98,0 | 95,0 | 97,2 | 98,3 | 67,1 |

Eine Instanz gilt als WN1st-Instanz, wenn mindestens einer ihrer Gold-Senses der erste WordNet-Sense ist (Anm. 8, S. 4727).

**Tab. 2 (S. 4727), Macro-F1 / Micro-F1, Auswahl:**

| Set | Inst. | ESCHER | GlossBERT | SyntagRank |
|---|---|---|---|---|
| ALL | 7.253 | 76,4 / 80,7 | 71,3 / 76,9 | 64,1 / 71,7 |
| ALLno1st | 2.525 | 54,2 / 55,2 | 42,4 / 45,0 | 26,9 / 29,5 |
| ALLnoSC | 1.138 | 71,0 / 75,0 | 57,4 / 62,2 | 55,1 / 61,0 |
| ALLHC | 541 | 0,0 / 0,0 | 0,0 / 0,0 | 0,0 / 0,0 |

**Tab. 4 (S. 4729), Labels der Neuannotation in %:**

| Set | Inst. | unverändert | fine-grained | Token/Lemma | Wortart | Sense | Inventar |
|---|---|---|---|---|---|---|---|
| ALL- | 5.523 | 72,6 | 9,4 | 2,9 | 0,3 | 8,0 | 6,8 |
| ALLNS- | 5.023 | 75,4 | 8,3 | 2,9 | 0,0 | 7,0 | 6,1 |
| ALLHC- | 500 | 44,6 | 20,4 | 3,0 | 0,0 | 17,8 | 14,2 |
| S10- | 1.251 | 62,4 | 7,6 | 4,7 | 0,0 | 8,2 | 17,1 |

ALL- = ALL ohne monoseme Instanzen und ohne SemEval-2007; ALLNS- = ALL- ohne den hard core; S10- = SemEval-2010 ohne monoseme Instanzen (S. 4729). Nachgerechnet am 2026-11-16: (72,6 + 9,4) / (100 − 2,9 − 0,3 − 6,8) = 82,0 / 90,0 = 91,1 % ✔; ALLNS- + ALLHC- = 5.023 + 500 = 5.523 ✔.

**Tab. 5 (S. 4731), Macro-F1 / Micro-F1 von ESCHER:** ALLNEW 78,7 / 81,6; S10NEW 78,0 / 82,1; 42D 58,9 / 54,1; softEN 83,7 / 86,8; hardEN 0,0 / 0,0. Auf ALL* (dieselben 4.917 Instanzen mit altem Gold) 73,1 / 78,3. Die Korrektur des Golds hebt die Werte also um 3 bis 6 Punkte.

**Tab. 7 (S. 4732), ESCHER mit K1:** hardEN 35,3 / 33,6 Macro/Micro, softEN 65,1 / 64,3 (mit SemCor allein 83,7 / 86,8).

**Annotierende:** ein Linguist für die Neuannotation und für 42D, ein zweiter nur für die blinde Zweitannotation von 42D (S. 4728, 4737). Bezahlung nach Landesniveau, hausinterne Oberfläche (Anm. 9, S. 4728).

**42D, Aufbau (Anhang A, S. 4737):** BNC in Blöcke unter 250 Tokens, Domänenzuordnung automatisch über BabelDomains, je Domäne der beste Absatz von einem Linguisten geprüft; 42 Absätze, im Mittel 208 Tokens. Annotiert wurden alle Inhaltswörter mit Hilfe von Glossen, Beispielen und Hyperonymen; mehrere Senses erlaubt; Instanzen mit WN1st oder monosem danach verworfen.

## Wörtliche Stellen

> „[…] we provide evidence showing why the F1 score metric should not simply be taken at face value […]“ (S. 4724, Abstract)

> „[…] here we choose to report macro-averaged F1 (aggregated by sense), as the former gives more weight to frequent senses simply because they occur more often […]“ (S. 4727); im Original folgt nach einem Gedankenstrich „thus hiding mediocre performances on least frequent senses.“

> „The distribution divergence becomes dramatic on ALLHC, where systems predict WN1st at least 62.7% of the times, but the true WN1st rate is now just 2.0%.“ (S. 4727)

> „[…] the hard core seems to be ‚hard‘ for the human annotator too […]“ (S. 4729)

## Bezug zur Dissertation

**Prüfauftrag zu `goldstandard/LITERATUR-STICHPROBE.md`** (Maru et al. 2022 ✔: „Die harten Fälle sind Nicht-MFS-Belege: Systeme sagen dort zu ≥ 62,7 % den ersten Sense voraus, korrekt wäre er zu 2,0 %. Macro-F1 nach Sense neben Micro berichten. Neuannotation durch einen Linguisten ließ nur 72,6 % der Benchmark-Belege unverändert.“):

1. **62,7 % / 2,0 %: Zahlen gedeckt, Bezug zu präzisieren.** Die Zahlen gelten für den hard core ALLHC, also die 541 Instanzen, die **alle sieben** Systeme falsch lösen (Tab. 1, S. 4727), nicht für Nicht-MFS-Belege allgemein. Der Satz „Die harten Fälle sind Nicht-MFS-Belege“ dreht die Richtung: Belegt ist, dass der hard core fast nur aus Nicht-WN1st-Instanzen besteht (2,0 % WN1st), nicht, dass Nicht-MFS-Belege hart sind. Für Letzteres ist ALLno1st der passende Beleg: Auf allen 2.525 Instanzen ohne WN1st liegt das beste System bei 54,2 Macro-F1, gegenüber 76,4 auf ALL (Tab. 2, S. 4727). Außerdem ist „MFS“ hier der **erste WordNet-Sense**, nicht ein aus Korpusdaten gelernter MFS. Vorschlag: „Instanzen, die alle sieben Systeme verfehlen, sind fast nie WN1st-Instanzen (2,0 %), trotzdem sagen die Systeme dort zu mindestens 62,7 % WN1st voraus (Tab. 1); auf allen Nicht-WN1st-Instanzen fällt das beste System von 76,4 auf 54,2 Macro-F1 (Tab. 2)“.
2. **Macro-F1 nach Sense:** gedeckt (S. 4727, 4731).
3. **72,6 %: Zahl gedeckt, Bezugsmenge zu präzisieren.** 72,6 % unverändert gilt für ALL- = 5.523 **polyseme** Instanzen von ALL **ohne SemEval-2007**, von **einem** Linguisten geprüft (Tab. 4, S. 4729). Weitere 9,4 % sind nicht falsch, sondern bekamen zusätzliche Senses (fine-grained); falsch im engeren Sinn sind 8,0 % (Sense), 6,8 % (Inventar), 2,9 % (Token/Lemma) und 0,3 % (Wortart). Wer „nur 72,6 % unverändert“ zitiert, sollte die 91,1 % Übereinstimmung nach Ausklammern der Nicht-Sense-Fehler (S. 4729 bis 4730) daneben nennen, sonst wirkt das Altgold schlechter, als die Autoren es selbst darstellen.

**Weitere Bezüge:**

- **PROTOKOLL §9.2 (Macro-Genauigkeit und Nicht-MFS-Items):** Die Begründung im Protokoll trägt. Zu ergänzen wäre, dass Maru et al. die Nicht-MFS-Teilmenge über den **ersten Inventarsense** bilden (ALLno1st). Im Protokoll ist MFS aus Silber gelernt; die Teilmenge „Nicht-MFS-Items“ sollte deshalb ausdrücklich über die MFS-Baseline des Protokolls definiert werden (der Sense, den die Baseline vorhersagt), nicht über die Lexikonreihenfolge (B8).
- **PROTOKOLL §9.2 (Silberqualität) und §2 (Silber):** Die Neuannotation zeigt an einem etablierten Benchmark, dass ein Altgold zu rund einem Viertel nicht unverändert übernommen wird (Tab. 4). Das stützt A1 (Bestand als Silber, nicht als Gold). Die Labelliste der Neuannotation (Token/Lemma, Wortart, Sense, Inventar, ergänzende Senses) entspricht weitgehend den Status und Ursachencodes des Protokolls (`LEMMA_FALSCH`, `KEINE_PASST`, `MEHRERE`; Ursachencodes in §7, Schritt 6).
- **PROTOKOLL §6 und §9.2 (`MEHRERE`, Bewertung „einer der Gold-Senses“):** Der Standard-Scorer zählt eine Vorhersage als richtig, wenn sie im Gold-Set liegt (S. 4730); zusätzliche Senses („fine-grained“) können die Werte daher nur heben. Das entspricht der Primärregel des Protokolls und zeigt deren Kehrseite: Mehr `MEHRERE` im Gold macht die Aufgabe leichter. Stützt die Sensitivitätsauswertungen aus A14.
- **PROTOKOLL §9.1 und §9.2 (menschliche Obergrenze):** Die Obergrenze hängt von der Aufgabe ab: 91,1 % auf ALL nach Bereinigung, 79,6 % auf dem schweren 42D (S. 4729 bis 4730, 4737). Für die Dissertation heißt das: Die menschliche Übereinstimmung muss auf denselben Items gemessen werden, an denen das LLM gemessen wird, wie im Protokoll (Alternative Annotator Test) vorgesehen. Ein Literaturwert wie „80 %“ ist kein Ersatz.
- **PROTOKOLL A16 (Mehrheit über Läufe als Ensemble):** Mehrheitsentscheidungen über Systeme helfen auf leichten Daten leicht und schaden auf schweren (Tab. 6, S. 4731). Ein ähnliches Muster wäre bei einer Mehrheit über LLM-Läufe denkbar; das Papier untersucht nur verschiedene Systeme, nicht Läufe desselben Modells.
- **PROTOKOLL §4.3 (Schichtung) und §4.4 (Domäne):** 42D zieht je einen Absatz pro Domäne (S. 4730, 4737), ein Gegenstück zur Gattungsquote. Das Papier misst aber keinen Domäneneffekt.
- **`knowledge/data.md`, B9 (Senses ohne Silberbeleg):** Systeme sagen im hard core zu mindestens 95 % einen im Training gesehenen Sense voraus (Tab. 1). Für die MFS-Baseline aus Silber gilt dasselbe zwangsläufig; für ein LLM ohne Training auf MHDBDB-Silber nicht. Die Aufschlüsselung „Gold-Sense im Silber belegt oder nicht“ wäre eine Analogie zu ALLnoSC und ließe sich aus dem Manifest bilden (Zahl der im Silber belegten Senses steht dort schon; Vorschlag).

## Grenzen und Einwände

- Die Neuannotation ist das Urteil **eines** Linguisten; für ALL und SemEval-2010 gibt es keine Zweitannotation, also keine Übereinstimmung dieses Urteils selbst. Nur für 42D wurde blind zweitannotiert (79,6 %).
- Der hard core ist relativ zu sieben bestimmten Systemen definiert; mit anderen Systemen (oder LLMs) wäre er ein anderer.
- 91,1 % entsteht durch nachträgliches Ausklammern von Fehlerklassen und Zusammenzählen von „unverändert“ und „fine-grained“; das ist eine großzügige Lesart der Übereinstimmung.
- Keine Signifikanztests oder Intervalle.
- 42D hat nur 370 Instanzen aus 42 Absätzen, also Klumpen; jede Domäne ist ein einziger Absatz.
- Navigli ist laut Literaturverzeichnis Mitautor von fünf der sieben untersuchten Systeme (ARES, ESCHER, EWISER, Generationary, SyntagRank), Maru und Bevilacqua von einzelnen davon.
- Englisch, WordNet 3.0; keine LLMs. Übertragung auf Mittelhochdeutsch und ein onomasiologisches Inventar nicht berührt.

## Weiterführend

- Loureiro et al. 2021, Analysis and evaluation of language models for WSD, *Computational Linguistics* 47(2) (S. 4724, 4727, 4732): in `LITERATUR-STICHPROBE.md` schon zitiert.
- Postma et al. 2016, Addressing the MFS bias in WSD systems (S. 4725, 4727, 4732): liegt als Zusammenfassung vor (`Postma-etal-2016-MFS-Bias.md`).
- Palmer, Dang & Fellbaum 2007, Making fine-grained and coarse-grained sense distinctions, both manually and automatically, *Natural Language Engineering* 13(2), S. 137 bis 163, und Edmonds & Kilgarriff 2002 (S. 4724, 4728): Quellen der 80-%-Schätzung; Palmer et al. 2007 auch zur Granularität.
- Blevins & Zettlemoyer 2020, BEM, ACL (S. 4726, 4727): seltene Senses.
- Agirre et al. 2009, SemEval-2010 Task 17, domänenspezifische All-Words-WSD (S. 4728).
- Barba, Pasini & Navigli 2021, ESCHER, NAACL (S. 4724, 4726).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
