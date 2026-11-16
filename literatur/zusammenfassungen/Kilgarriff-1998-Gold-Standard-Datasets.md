# Kilgarriff 1998: Gold-Standard-Datensätze für die WSD-Evaluation

**Datei:** `pdf/Kilgarriff-1998-Gold-Standard-Datasets.pdf` (nur lokal; 22 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Tab. 1 und S. 10 am Seitenbild geprüft (das Kappa-Zeichen fehlt in der Textebene), DOI der Zeitschriftenfassung aufgelöst. Das lokale PDF ist byte-gleich mit https://www.kilgarriff.co.uk/Publications/1998-K-CompSL.pdf (SHA-256 verglichen am 2026-11-13); es enthält keine Markierungen.

**Fassung: Das lokale PDF ist der ITRI-Report ITRI-98-08 (August 1998), nicht die Zeitschriftenfassung.** Alle Seitenangaben unten beziehen sich auf den Report und lassen sich nicht auf die Seiten 453 bis 472 der Zeitschrift übertragen. Ob der Text der Zeitschriftenfassung abweicht, ist nicht geprüft; vor dem Zitieren die Zeitschriftenfassung einsehen (Elsevier, nicht frei).

Seitenzählung: PDF-Seite 1 ist das Deckblatt des Reports ohne Seitenzahl; ab PDF-Seite 2 gilt gedruckte Seite = PDF-Seite − 1 (PDF 2 = S. 1, PDF 22 = S. 21). Unten stehen gedruckte Seiten des Reports.

## Bibliografie

- **Vollständig (Zeitschrift, maßgeblich):** Kilgarriff, Adam (1998). Gold standard datasets for evaluating word sense disambiguation programs. *Computer Speech & Language* 12(4), S. 453 bis 472.
- **Lokale Fassung:** Kilgarriff, Adam (1998). *Gold Standard Datasets for Evaluating Word Sense Disambiguation Programs*. ITRI-98-08, Information Technology Research Institute Technical Report Series, University of Brighton, August 1998 (Deckblatt).
- **DOI/URL:** https://doi.org/10.1006/csla.1998.0108 (aufgelöst am 2026-11-13, leitet auf Elsevier; Crossref: Band 12, **Heft 4**, S. 453 bis 472, Oktober 1998, Elsevier BV). Das Deckblatt des Reports sagt dagegen „Also published in Computer Speech and Language 12 (3)“; Crossref ist maßgeblich. Report: https://www.kilgarriff.co.uk/Publications/1998-K-CompSL.pdf.
- **Lizenz:** für den Report keine angegeben; Zeitschriftenfassung bei Elsevier, nicht Open Access (Crossref nennt nur die TDM-Nutzerlizenz).
- **Art:** Technischer Report (Vorabfassung eines begutachteten Zeitschriftenartikels)
- **Sprache:** Englisch

## Worum es geht

Kilgarriff schreibt im Vorfeld des ersten SENSEVAL (1998) darüber, wie ein Gold-Standard-Datensatz für die WSD-Evaluation entstehen muss, damit er nicht „fool's gold“ ist (S. 1). Er sichtet die vorhandenen handannotierten englischen Korpora (S. 4 bis 7), referiert frühere Evaluationsvorschläge, vor allem Gale, Church & Yarowsky 1992 und Resnik & Yarowsky 1997 (S. 7 bis 9), und argumentiert, dass hohe Übereinstimmung zwischen Annotierenden (ITA) erreichbar ist, wenn Wörterbuch und annotierende Personen sorgfältig gewählt werden (S. 9 bis 13). Für die Auswahl der Belege plädiert er für das **lexikalische** Modell (erst Wörter ziehen, dann Belege) und gibt ein ausgearbeitetes Stichprobenschema nach Frequenz und Polysemie für Nomen (S. 13 bis 17, Tab. 1).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Die Grundsorge ist Replizierbarkeit: Zwei Personen, die denselben Text annotieren, vergeben zu oft verschiedene Tags. Hohe Replizierbarkeit ist erreichbar, aber nur, wenn das Wörterbuch und die Annotierenden „with care“ gewählt werden. | S. 1, Abschnitt 1; wiederholt S. 16 bis 18 | zentrale These |
| Was ein Word Sense ist, ist ungeklärt; Wörterbücher teilen dasselbe Wort verschieden auf, und es fehlen operationale Kriterien für Sense-Grenzen. | S. 2, Abschnitt 2.1 | Problemstellung, referiert |
| Anders als beim POS-Tagging gibt es für Senses keine allgemeinen Kategorien: Jedes Wort bringt ein neues Sense-Set, dessen Autorität an einer bestimmten Ausgabe eines Wörterbuchs hängt; WSD ist „as many tasks as there are ambiguous words in the lexicon“. | S. 4, Abschnitt 2.4 | eigene Analyse |
| SEMCOR: 250.000 Wörter, alle Inhaltswörter mit WordNet-Senses; die Erfahrung zeigte, dass Annotierende das Wörterbuch ändern können müssen, sonst wird ihre Wahl zwischen unklaren Senses willkürlich. | S. 5, Abschnitt 3.2.1 | referiert |
| DSO-Korpus (191 Nomen und Verben, 192.800 Tokens, Studierende): Übereinstimmung mit SEMCOR auf überlappenden Belegen 57 %; damit nicht als Gold verwendbar. | S. 5, Abschnitt 3.2.2 | referiert (Ng & Lee 1996), Bewertung eigen |
| HECTOR (Oxford University Press/Digital): ca. 300 Wörter mit 300 bis 1000 Belegen in einem 17-Mio.-Wörter-Korpus, alle Belege von erfahrenen Lexikograf:innen annotiert, Wörterbuch parallel zur Annotation geschrieben; wird für SENSEVAL neu annotiert, um die ITA zu bestimmen. | S. 6 bis 7, Abschnitte 3.2.5 und 3.3 | referiert, Entscheidung für SENSEVAL |
| Gale, Church & Yarowsky (1992) definieren die Obergrenze über menschliche Übereinstimmung und die Untergrenze über die Zuweisung des häufigsten Senses; für zwölf Wörter liegt die Baseline zwischen 48 und 96 %. | S. 7, Abschnitt 4 | referiert |
| Resnik & Yarowsky (1997) schlagen vor: Teilpunkte für verringerte Ambiguität, mildere Wertung naher Fehler, ein jährlich frischer Testkorpus mit ca. 200 Testwörtern, die erst nach dem Einfrieren der Systeme bekannt werden, und ein mehrsprachiges, übersetzungsbasiertes Inventar. | S. 8 bis 9, Abschnitt 5 | referiert |
| **Mehrfachlabels:** In Washington 1997 stritten „computer scientists“ (Gold soll einfach auswertbar sein) und „humanists“ (manchmal sind mehrere Antworten „simply the truth of the matter“). Abgestimmt wurde: Mehrfachantworten bleiben möglich, Annotierende sollen sie aber nur geben, wenn eine Einzelantwort unwahr wäre. Die Frage hängt eng an Granularität und Verschachtelung der Senses. | S. 9, Abschnitt 5 | referiert (Diskussion), eigene Deutung |
| Frühere ITA-Werte: Jorgensen 68 %, Fellbaum et al. „naive taggers“ gegen Expert:innen 74 %, Bruce & Wiebe nach Ausschluss einer auffälligen Person κ = 0,898. | S. 9 bis 10, Abschnitt 6 | referiert |
| Ein Gold verlangt mehr als eine annotierende Person, berechnete ITA und eine Entscheidung, ob sie hoch genug ist; „If ITA is not high enough, then we do not have a gold standard corpus.“ | S. 10, Abschnitt 6 | eigene Forderung |
| **ITA als Obergrenze:** „ITA defines the upper bound for how well a computer program can perform.“ Stimmt eine zweite Person nur zu 80 % mit der ersten überein, ist unklar, was „mehr als 80 % richtig“ für ein Programm bedeutet. | S. 10 | eigene These |
| Die Umdefinition von Klassifikation zu Diskrimination bei Gale et al. sei „highly problematic“: Der Bezug zur eigentlichen Aufgabe gehe verloren. | S. 10 | eigene Kritik |
| **Drei Ursachen für Abweichungen:** nicht auflösbare Unbestimmtheit oder Ambiguität der Daten, schlecht definierte Tags, Fehler einzelner Personen. Gegen die erste hilft ein Schema, das „ambiguous or indeterminate between two tags“, „both apply“ oder „none apply“ erlaubt; gegen die zweite klarere Sense-Definitionen; gegen die dritte motivierte Expert:innen. | S. 10 bis 11 | eigene Analyse |
| Rohübereinstimmung berücksichtigt keine Zufallsübereinstimmung; κ (Krippendorff 1980, Carletta 1996) gleicht das aus. Für den Zweck des Aufsatzes genüge: 1 ist volle Übereinstimmung. | S. 10, Anm. 3 | referiert, knapp |
| POS-Beispiel (Samuelsson & Voutilainen 1997): Zwei Expert:innen erreichten unabhängig 99,3 %, nach Besprechung über 99,7 %; nur 21 Wörter blieben echt ambig. Dass der Wert erst nach dem Vergleich über 99,7 % lag, sei „not critical“: Ziel sei ein korrektes, reproduzierbares Ergebnis; unabhängiges Arbeiten sei ein Mittel dazu, „but is not in itself critical“. | S. 11 | referiert, Deutung eigen |
| **Schwelle:** 100 % ITA sind unrealistisch, aber „Kappa of over 0.8 (equivalent to between 80 and 90% raw ITA, depending on the number of senses per word) is critical to the viability of the exercise.“ | S. 11 | eigene Festlegung für SENSEVAL |
| Annotieren ist das Spiegelbild der Lexikografie; nur ein gut geschriebenes Wörterbuch mit klaren Unterscheidungen und Beispielen erlaubt konsistentes Annotieren. Es braucht Regeln für Kollokationen und Mehrwortausdrücke, Verschachtelung, reguläre Polysemie, teilkonventionalisierte Metapher und Metonymie. | S. 11 bis 12, Abschnitt 6.1 | eigene Analyse |
| Das Wörterbuch darf nicht unveränderlich sein: Wo ein Eintrag falsch, vage oder unverständlich ist, müssen Annotierende ihn überarbeiten können. Verschachtelte Einträge erlauben, nahe Fehler milder zu werten und grob wie fein auszuwerten. | S. 12, Abschnitt 6.1 | eigene Forderung |
| Folge für Unbekanntheit der Testwörter: Sobald das überarbeitete Wörterbuch veröffentlicht ist, lassen sich die Testwörter erraten; daher zwei Termine (Bekanntgabe der Wörter, später Ausgabe der Belege). | S. 12 | eigene Folgerung |
| **Modellverfahren:** alle Zielwörter von mindestens zwei unabhängigen Annotierenden, ITA laufend verfolgt; drei Schritte: (1) Wörterbucheintrag sichten und ändern, erst getrennt, dann gemeinsam; (2) getrennt annotieren; (3) Abweichungen gemeinsam klären. | S. 12 bis 13, Abschnitt 6.2 | eigener Vorschlag |
| **Stichprobe:** Die Domäne lässt sich als Population von Texten oder von Worttypen sehen. „For evaluating user-ready systems, the former would be appropriate […] but for an exploratory evaluation, the latter will be more informative.“ | S. 13, Abschnitt 7 | eigene Position |
| Zweistufige Ziehung: erst Worttypen, dann Belege je Typ. Pilot-SENSEVAL: 40 Worttypen, eine volle Evaluation bräuchte mehrere hundert; 100 bis 400 Belege je Typ, abhängig von Frequenz und Polysemie. | S. 13, Abschnitt 7.1 | eigener Plan |
| „Lexikalisch“ (HECTOR, Wort für Wort) statt „textuell“ (SEMCOR, Token für Token): Die meiste Arbeit steckt im Verstehen der Definitionen, man kann nicht viele Unterscheidungen zugleich im Kopf halten; „Taggers will make more accurate decisions faster if they work lexically rather than textually.“ | S. 14, Abschnitt 7.2 | eigenes Argument, gestützt auf Kilgarriff 1993 |
| Gegenargumente zum Sampeln (die meisten Wörter bleiben ohne Daten; ein vollständig annotierter Text ist kompakter; Sense-Entscheidungen beschränken sich gegenseitig) seien für Evaluationszwecke nicht entscheidend. | S. 14 bis 15, Abschnitt 7.3 | eigene Abwägung |
| Ideal wäre, nach Problemtypen zu schichten; da es diese Taxonomie nicht gibt, iterativ: nach verfügbaren, auffälligen Merkmalen ziehen, untersuchen, Schema überarbeiten. Drei solche Merkmale: **Wortart, Frequenz** (großes Korpus) **und Polysemiegrad** (Zahl der Senses in einer Ressource). | S. 15, Abschnitt 7.4 | eigener Vorschlag |
| Beispiel für Nomen: Frequenz und Polysemie je in vier Bänder, 16 Zellen; Polysemie als Mittel aus Collins-Sensezahl und Zahl der WordNet-Senses; nur Nomen mit über 50 BNC-Belegen. | S. 15, Tab. 1 (S. 17) | eigenes Beispiel |
| Zahl der Typen pro Zelle steigt mit der Typenzahl der Zelle und dem Frequenzband („common words being of greater interest than rare ones“); Vielfache von fünf, Mindestgröße zehn, Ziel 200 Typen; Zellen mit weder vielen Typen noch vielen Tokens bekommen keine Teilstichprobe. | S. 15 bis 16 | eigener Vorschlag |
| **Monoseme Wörter mitziehen:** Die meisten Wörter werden zumindest gelegentlich nicht standardmäßig gebraucht; monoseme Wörter zeigen das Ausmaß ohne die Komplikation der Wörterbuchpolysemie. | S. 16 | eigene Begründung |
| Belege pro Typ steigen mit Frequenzband und Polysemie, weil „[b]oth these factors may be expected to give rise to a more complex pattern of word use, requiring more data to be understood“: 400 für die häufigsten, polysemsten Typen, je Stufe 40 weniger; zusammen 52.800 Belege für Nomen. | S. 16 | eigener Vorschlag mit Begründung als Erwartung |
| Fazit: Die besten Annotierenden sind professionelle Lexikograf:innen; das lexikalische Sampling spart Aufwand und erhöht Genauigkeit. | S. 16 bis 18, Abschnitt 8 | Zusammenfassung |

## Daten, Methode, Zahlen

**Tab. 1 (S. 17, am Seitenbild geprüft), Stichprobenrahmen für Nomen (BNC, WordNet 1.5).** Zeilen: Polysemie (Zahl der Senses); Spalten: Frequenzband. Je Zelle: Typen; Tokens in Mio. / vorgeschlagene Stichprobe (Typen × Belege = Belege).

| Senses | Top 200 | Next 1.000 | Next 5.000 | Rest | Summe |
|---|---|---|---|---|---|
| 0 bis 1 | AW 3; 0,10 / 0 | BW 76; 0,40 / 10×240 = 2.400 | CW 1.365; 0,94 / 15×200 = 3.000 | DW 10.141; 0,52 / 20×160 = 3.200 | 11.585; 1,96 / 45; 8.600 |
| 2 bis 4 | AX 30; 0,80 / 0 | BX 335; 2,27 / 25×280 = 7.000 | CX 2.436; 2,20 / 20×240 = 2.800 | DX 5.077; 0,40 / 20×200 = 4.000 | 7.878; 5,67 / 65; 3.800 |
| 5 bis 9 | AY 77; 2,20 / 10×360 = 3.600 | BY 419; 3,22 / 25×320 = 8.000 | CY 1.043; 1,22 / 15×280 = 420 | DY 471; 0,05 / 0 | 2.010; 6,67 / 50; 15.800 |
| 10+ | AZ 90; 3,08 / 15×400 = 6.000 | BZ 170; 1,26 / 15×360 = 5.400 | CZ 156; 0,24 / 10×320 = 3.200 | DZ 29; 0,00 / 0 | 445; 4,58 / 40; 14.600 |
| Summe | 200; 6,18 / 25; 9.600 | 1.000; 7,15 / 75; 22.800 | 5.000; 4,60 / 60; 13.200 | 15.718; 0,97 / 40; 7.200 | 21.918; 18,92 / 200; 52.800 |

Rechenfehler im Original (am Seitenbild bestätigt, nachgerechnet 2026-11-13): (1) CY „15x280=420“ statt 4.200; Zeilensumme 15.800 und Spaltensumme 13.200 rechnen mit 4.200. (2) CX „20x240=2,800“, das Produkt wäre 4.800; die Spaltensumme 13.200 und die Gesamtsumme 52.800 rechnen mit 2.800. (3) Zeilensumme für 2 bis 4 Senses „3,800“; aus den Zellen ergibt sich 7.000 + 2.800 + 4.000 = 13.800, und nur damit gehen die Zeilensummen in 52.800 auf. Die Gesamtzahl 52.800 (S. 16) ist also mit den gedruckten Zellprodukten konsistent, nicht mit 20 × 240 in CX.

**Anhang (S. 17 bis 19):** eine Beispielstichprobe englischer Nomen pro Zelle (z. B. AZ: *year, back, difference, light, …*).

**Pilot-SENSEVAL laut Report:** 40 Worttypen, 100 bis 400 Belege pro Typ (S. 13); Sprachen Englisch, Französisch, Italienisch (S. 2).

## Wörtliche Stellen

> „If ITA is not high enough, then we do not have a gold standard corpus. ITA defines the upper bound for how well a computer program can perform.“ (S. 10)

> „Taggings fail to agree for one of three reasons: because of an irreducible indeterminacy or ambiguity in the data, because the tags were poorly defined, or because one or more of the individuals made a mistake.“ (S. 10)

> „[…] Kappa of over 0.8 (equivalent to between 80 and 90% raw ITA, depending on the number of senses per word) is critical to the viability of the exercise.“ (S. 11)

> „[…] multiple correct answers should be retained as a possibility, though the human taggers should be discouraged from giving multiple answers unless they were clear that a single answer would be untrue.“ (S. 9)

> „For evaluating user-ready systems, the former would be appropriate, as the system would need to be able to sense-tag all words, but for an exploratory evaluation, the latter will be more informative.“ (S. 13)

## Bezug zur Dissertation

**Prüfauftrag zu `goldstandard/LITERATUR-STICHPROBE.md`** (Zeile „Zwei Modelle für WSD-Gold“, dort ✔):

1. *„Für Evaluation das lexikalische Modell“*: **nur teilweise gedeckt.** Kilgarriff empfiehlt das lexikalische Modell für eine **explorative** Evaluation und hält das textuelle für die Evaluation einsatzfertiger Systeme für angemessen (S. 13). Vorschlag: „für eine explorative Evaluation das lexikalische Modell“ schreiben. Für die Dissertation passt das, weil das primäre Schätzziel ausdrücklich die Vielfalt der Lemmata ist (§4.1), nicht die Leistung auf laufendem Text.
2. *„geschichtet nach Wortart × Korpusfrequenz × Polysemie; im Beispiel 4 × 4 Bänder, mindestens 10 Typen pro Zelle“*: **gedeckt** (S. 15 bis 16, Tab. 1), mit zwei Präzisierungen. Das Beispiel betrifft nur Nomen, die Wortart ist dort also nicht Schicht, sondern Auswahl. „Mindestens 10“ gilt für Zellen mit Teilstichprobe; vier der 16 Zellen bekommen keine (Tab. 1).
3. *„Auch monoseme Wörter mitziehen“*: **gedeckt** (S. 16). Das Protokoll weicht davon ab (§4.3: nur Polysemie 2 / 3 / 4+). Kilgarriffs Begründung, monoseme Wörter zeigten nichtstandardmäßigen Gebrauch ohne Wörterbuchpolysemie, entspricht genau der Frage nach `KEINE_PASST` (§1, Nebenfrage zum Begriffssystem). Ob das ein Grund ist, im Pilot oder als Zusatzkomponente einige monoseme Lemmata mitzuführen, wäre zu entscheiden; aufgenommen als Befund in der Rückmeldung.

**PROTOKOLL A3 („Frequenz als Schwierigkeitsfaktor (Kilgarriff 1998)“):** Das Werk misst keine Schwierigkeit nach Frequenz. Es teilt mehr Typen den häufigen Bändern zu, weil häufige Wörter „of greater interest“ sind (S. 15), und mehr Belege den häufigen und polysemen Typen, weil dort ein komplexeres Gebrauchsmuster **erwartet** wird (S. 16). Vorschlag: in A3 „Frequenz und Polysemie als Schichtungsmerkmale (Kilgarriff 1998, ITRI-Fassung S. 15 bis 16)“ statt „Frequenz als Schwierigkeitsfaktor“.

**Weitere Bezüge:**

- **PROTOKOLL §7, A32 (Schwelle α ≥ 0,80):** Kilgarriff setzt für SENSEVAL κ über 0,8 als Bedingung, ausdrücklich gleichgesetzt mit 80 bis 90 % Rohübereinstimmung je nach Sense-Zahl (S. 11). Das stützt die Schwelle von A32 als in der WSD übliche Größe. Unterschied: Bei ihm ist es eine Bedingung für die Gültigkeit des Golds, im Protokoll nur die Regel, wann das Nachschärfen endet (§7: „nicht ob das Gold brauchbar ist“).
- **PROTOKOLL §6 (Ausweichlabels, `MEHRERE`):** Die drei Antworten gegen nicht auflösbare Unbestimmtheit (ambig zwischen zwei Tags, beide zutreffend, keiner zutreffend; S. 10 bis 11) entsprechen `MEHRERE` und `KEINE_PASST`. Die Abstimmung von 1997 (S. 9) liefert eine Formulierung für die Richtlinien: Mehrfachantworten nur, wenn eine Einzelantwort unwahr wäre. Das ist strenger als „mehrere Senses passen gleichermaßen“ in §6 und könnte die Häufigkeit von `MEHRERE` begrenzen.
- **PROTOKOLL §7, Schritt 6 (Ursachencode):** Die drei Ursachen (S. 10) decken sich mit „echte Textambiguität“, „Richtlinienlücke“ bzw. „Inventarlücke“ und „Versehen“ im Code nach Barteld et al. 2015; Kilgarriff ist ein zweiter, WSD-spezifischer Beleg.
- **PROTOKOLL §7, Schritt 5 (Roh-IAA zuerst):** Kilgarriff hält es für unkritisch, wenn hohe Übereinstimmung erst nach dem Vergleich erreicht wird (S. 11). Das Protokoll ist hier bewusst strenger; es kann Kilgarriff als Gegenposition nennen und begründen, warum es den Wert vor der Besprechung festhält (Messung der Reproduzierbarkeit des Instruments, A31).
- **PROTOKOLL §5 und A31 (festes Inventar):** Kilgarriffs Forderung, das Wörterbuch während der Annotation zu ändern (S. 5, S. 12), steht dem festen MHDBDB-Inventar entgegen. Das Protokoll ersetzt das Ändern durch das Protokollieren von `KEINE_PASST` mit angekreuzten Begriffen (§5, Punkt 4). Diese Abweichung sollte im Artikel benannt werden: Gemessen wird die Übereinstimmung **relativ** zu einem nicht überarbeiteten Inventar, und niedrige Werte können am Inventar liegen.
- **PROTOKOLL §9.1, Punkt 7 (zwei Ebenen des Begriffssystems):** Verschachtelte Einträge erlauben, grob und fein mit denselben Daten auszuwerten und nahe Fehler milder zu werten (S. 12). Das stützt die vorab definierte Auswertung über Oberbegriffe.
- **PROTOKOLL §9.2 (Teilwertung):** Resnik & Yarowskys Vorschlag, verringerte Ambiguität und nahe Fehler mit Teilpunkten zu werten (S. 8), ist eine frühe Form der Sensitivitätsauswertung mit Dice.
- **PROTOKOLL §7, Schritt 4 (Itemreihenfolge zufällig) und §4.5 (Panel):** Kilgarriffs stärkstes Argument für das lexikalische Vorgehen ist, dass Annotierende Wort für Wort genauer und schneller arbeiten (S. 14). Bei 1 Token pro Paar in der Hauptstichprobe entfällt das; im Panel (5 Tokens pro Paar) wäre es möglich, die Belege eines Lemmas zusammen zu zeigen. Das Protokoll mischt die Reihenfolge zufällig (Beck et al. 2024). Beides hat Gründe; die Wahl sollte im Artikel stehen.
- **PROTOKOLL §10 (Kontamination):** Die Überlegung, Testwörter erst spät bekanntzugeben (S. 8, S. 12), ist die Vorform des Schutzes vor Lecks; bei LLMs geht es heute um die Labels, nicht um die Wortliste.
- **`goldstandard/LITERATUR-IAA.md`:** Die referierten Werte (Jorgensen 68 %, Fellbaum et al. 74 %, DSO gegen SEMCOR 57 %, S. 5 und S. 9 bis 10) passen zu den dort genannten Größenordnungen; die 57 % sind dieselbe Zahl wie bei Ng et al. 1999 (dort ✔).

## Grenzen und Einwände

- Programmatischer Text vor SENSEVAL-1, keine eigenen Messungen; die Werte zu ITA sind referiert. Wie gut die Vorschläge funktionierten, berichten erst Kilgarriff & Rosenzweig 2000 und Kilgarriff 2001.
- Kappa wird nur in einer Fußnote eingeführt; die Gleichsetzung „κ über 0,8 = 80 bis 90 % roh“ ist eine Faustregel ohne Rechnung (S. 11).
- Das Stichprobenschema ist ein Beispiel für Nomen mit Wörterbuch-Sensezahlen; Frequenz- und Polysemiebänder sind gesetzt, nicht begründet. Die Tabelle enthält mindestens einen Druckfehler (CY), möglicherweise weitere (siehe oben).
- Die Annahme, Lexikograf:innen seien die besten Annotierenden, ist plausibel, aber hier nicht geprüft; für Mittelhochdeutsch gibt es keine Muttersprachler:innen, und die Kompetenz liegt bei Philolog:innen, nicht bei Lexikograf:innen im engeren Sinn.
- Ein onomasiologisches Inventar (Begriffsgruppen) ist nicht berührt; Kilgarriffs Wörterbuchkritik (S. 11 bis 12) gilt sinngemäß aber auch für Begriffszuordnungen.
- Fassungsfrage: Zitiert werden sollte die Zeitschriftenfassung; die Seitenzahlen hier gelten nur für den Report.

## Weiterführend

- Resnik & Yarowsky (1997), A perspective on word sense disambiguation methods and their evaluation, SIGLEX-Workshop Washington, S. 79 bis 86 (S. 8, S. 21): Teilwertung und Testdesign.
- Jorgensen (1990) (S. 9): Primärquelle für 68 %.
- Fellbaum, Grabowski, Landes & Baumann (1996/1997), naive gegen Expert:innen (S. 10, S. 19).
- Bruce & Wiebe (1998), Word sense distinguishability and inter-coder agreement, EMNLP-3, S. 53 bis 60 (S. 10, S. 19).
- Samuelsson & Voutilainen (1997), ACL/EACL, S. 246 bis 253 (S. 11, S. 21): ITA nach Besprechung.
- Carletta (1996), Kappa, *Computational Linguistics* 22(2) (S. 10, S. 19).
- Kilgarriff (1993), Dictionary word sense distinctions, *Computers and the Humanities* 26 (S. 14, S. 20).
- Ng & Lee (1996), DSO-Korpus (S. 5, S. 20).
- Kilgarriff (1997), „I don't believe in word senses“: im Report nicht zitiert (zitiert ist Kilgarriff 1997, „What is word sense disambiguation good for?“, S. 2, S. 20); für offenen Punkt 21 des Protokolls also gesondert zu beschaffen.

## Julias Markierungen im PDF

Keine. `markierungen.py` legt für dieses PDF keine Datei an.
