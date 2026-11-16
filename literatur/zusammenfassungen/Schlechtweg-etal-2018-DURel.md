# Schlechtweg, Schulte im Walde & Eckmann 2018: Diachronic Usage Relatedness (DURel)

**Datei:** `pdf/Schlechtweg-etal-2018-DURel.pdf` (nur lokal; 6 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen, Tab. 3 (S. 172) am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology N18-2027 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 168 + n (PDF 1 = S. 169, PDF 6 = S. 174; Seitenzahlen in der Fußzeile). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Schlechtweg, Dominik, Sabine Schulte im Walde & Stefanie Eckmann (2018). Diachronic Usage Relatedness (DURel): A Framework for the Annotation of Lexical Semantic Change. In: Marilyn Walker, Heng Ji & Amanda Stent (Hg.), *Proceedings of the 2018 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies, Volume 2 (Short Papers)*. New Orleans, Louisiana: Association for Computational Linguistics, S. 169 bis 174.
- **DOI/URL:** 10.18653/v1/N18-2027 (aufgelöst über doi.org und Crossref, 2026-11-16); https://aclanthology.org/N18-2027/ (Herausgeber:innen nach dem BibTeX der Anthology, abgerufen 2026-11-16).
- **Lizenz:** CC BY 4.0 nach der Copyright-FAQ der ACL Anthology (ACL-Material ab 2016, abgerufen 2026-11-16); im PDF nur „©2018 Association for Computational Linguistics“ (S. 169).
- **Art:** Konferenzbeitrag (Short Paper)
- **Sprache:** Englisch

## Worum es geht

Für die Evaluation von Modellen des lexikalischen Bedeutungswandels fehlten verlässliche Testdaten. Die Autor:innen übertragen ein synchrones Annotationsverfahren für graduelle Polysemie (Erk et al. 2013) auf diachrone Daten: Annotator:innen bewerten nicht Bedeutungen, sondern die **Bedeutungsnähe von Belegpaaren** desselben Worts auf einer Skala von 1 bis 4 (S. 170). Aus den mittleren Werten innerhalb eines frühen Zeitraums, eines späten und zwischen beiden leiten sie zwei Maße für Wandel ab (S. 171). Fünf Studierende bewerteten 1.320 Paare zu 22 deutschen Zielwörtern aus dem DTA mit einer paarweisen Übereinstimmung (Spearman ρ) von 0,57 bis 0,68 (S. 172). Das Verfahren braucht nach den Autor:innen keine Definition von Wortbedeutungen (S. 173).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Es gibt für keine Sprache einen verlässlichen Testdatensatz für Bedeutungswandel jenseits weniger handverlesener Wörter. | S. 169, Abschnitt 1 | Einschätzung der Autor:innen |
| Polysemie ist das synchrone Ergebnis von Bedeutungswandel; Blank unterscheidet innovativen Wandel (neue Bedeutung kommt hinzu, mit der alten polysem verbunden) und reduktiven (eine Bedeutung geht verloren). Beispiele: *Donnerwetter* gewinnt um 1800 die Bedeutung eines Ausrufs, *Zufall* verliert nach 1850 ‘Anfall’. | S. 169 bis 170, Abschnitt 3 | referiert (Blank 1997; Paul 2002; Osman 1971) |
| Blanks Kontinuum der Bedeutungsnähe: Identität, Kontextvarianz, Polysemie, Homonymie (Tab. 1). Es lässt sich nicht direkt in Annotationskriterien umsetzen, wird aber über eine Skala indirekt genutzt. | S. 170, Abschnitt 3.1 | referiert, Anwendung eigen |
| Skala (nach Brown 2008): 4 identisch, 3 eng verwandt, 2 entfernt verwandt, 1 unverwandt, 0 nicht entscheidbar (Tab. 2). | S. 170 | eigene Festlegung nach Brown 2008 |
| Zwei Maße: ΔLATER = Mittel(LATER) minus Mittel(EARLIER), positiv für reduktiven, negativ für innovativen Wandel; COMPARE = Mittel der Paare über beide Zeiträume, niedrig bei starkem Wandel. | S. 171, Abschnitt 3.2 | eigene Methode |
| Übereinstimmung als Mittel paarweiser Spearman-Korrelationen ohne 0-Urteile, wie bei Erk et al. 2013: Spanne 0,57 bis 0,68, „average correlation of 0.66“, alle Paare p < 0,01. | S. 172, Abschnitt 5, Tab. 3 | eigenes Ergebnis |
| Die beiden Annotator:innen mit historisch-linguistischem Hintergrund (4 und 5) stimmen am besten überein (0,68) und am besten mit dem Mittel der anderen (0,75 und 0,74); die übrigen weichen nur leicht ab. | S. 172 | eigenes Ergebnis, Deutung der Autor:innen |
| Die Werte sind vergleichbar mit Erk et al. 2013 und „moderately higher“ (dort 0,55 bis 0,62), obwohl historische Daten zu beurteilen waren; nicht direkt vergleichbar wegen der 5-stufigen Skala bei Erk et al. und vermutlich mehr ausgeschlossener 0-Urteile hier. | S. 172 | Vergleich der Autor:innen |
| ΔLATER trennt reduktiven von innovativem Wandel (Mittel 0,39 gegen −0,18), versagt aber, wenn die neue Bedeutung sehr häufig wird (*Presse*); COMPARE erfasst das, verwechselt aber Polysemie mit Wandel (*Feder*). | S. 172 bis 173 | eigenes Ergebnis |
| Empfehlung: kurze, benachbarte Zeiträume und ein ausgewogenes Korpus über alle Zeiträume; ΔLATER ist anfällig für Korpuseffekte wie Gattungswechsel. | S. 173, Discussion | Folgerung der Autor:innen |
| DURel „relies on an intuitive notion of semantic relatedness and needs no definition of word senses“. | S. 173, Abschnitt 6 | Fazit der Autor:innen |

## Daten, Methode, Zahlen

- **Korpus:** Deutsches Textarchiv (DTA), Zeiträume EARLIER 1750 bis 1800 und LATER 1850 bis 1900; Sonderzeichen auf heutige Orthografie normalisiert, um Probleme historischer Daten zu verringern (S. 171).
- **Zielwörter:** von Hand ausgewählt nach Wandelfällen bei Paul 2002 (innovativ) und Osman 1971 (reduktiv), nur wenn der Wandel im Korpus sichtbar war; 19 Fälle von Innovation, 9 von Reduktion; *Anstalt*, *Anstellung*, *Vorwort* mehrfach aufgenommen (S. 171). Zusammen 22 Zielwörter.
- **Stichprobe:** je Wort 20 zufällige Paare pro Gruppe EARLIER, LATER, COMPARE, also 60 Paare pro Wort und 1.320 insgesamt; Suche nach Lemma und Wortart (S. 171).
- **Darbietung:** Ein Beleg ist der Satz mit dem Wort, gezeigt mit vorangehendem und folgendem Satz (Abb. 2); Reihenfolge innerhalb der Paare und der Paare insgesamt zufällig, Gruppen gemischt (S. 171).
- **Annotator:innen:** fünf Muttersprachler:innen, Studierende der Linguistik, zwei mit historisch-linguistischem Hintergrund; nicht informiert, dass es um Bedeutungswandel ging (S. 171). Richtlinien nach Erk et al. 2013, Richtlinien und Daten frei verfügbar (S. 171, Anm. 1).
- **Tab. 3 (S. 172, am Seitenbild geprüft):** paarweise ρ zwischen Annotator:in 1 bis 5: 0,59 / 0,63 / 0,67 / 0,66 (1 mit 2 bis 5), 0,57 / 0,64 / 0,65 (2 mit 3 bis 5), 0,64 / 0,62 (3 mit 4, 5), 0,68 (4 mit 5); gegen das Mittel der anderen: 0,71 / 0,68 / 0,68 / 0,75 / 0,74.
- **Nachgerechnet:** Das arithmetische Mittel der zehn Paarwerte in Tab. 3 ist 0,635, das Mittel der Zeile „avg“ 0,712. Die im Text genannte „average correlation of 0.66“ (S. 172) entspricht keinem der beiden; wie sie gerechnet ist, sagt die Arbeit nicht.
- Keine zufallskorrigierte Übereinstimmung, keine Rohübereinstimmung, keine Angabe, wie viele 0-Urteile ausgeschlossen wurden.

## Wörtliche Stellen

> „It relies on an intuitive notion of semantic relatedness and needs no definition of word senses.“ (S. 173)

> „This indicates that historical knowledge makes a positive difference when annotating DURel.“ (S. 172)

## Bezug zur Dissertation

**1. A31 und offener Punkt 22 (Weg C: inventarfreie Aufgabe).** DURel ist das Verfahren, das A31 als Weg C nennt. Die Arbeit liefert die Grundform: Paare von Belegen desselben Lemmas, Skala 1 bis 4 plus „nicht entscheidbar“, Übereinstimmung als mittleres paarweises ρ (S. 170, 172). Sie zeigt auch, dass das mit historischem Deutsch (DTA, 18. und 19. Jahrhundert) und Studierenden ohne Schulung auf Bedeutungen funktioniert. Für Mittelhochdeutsch ist der Abstand größer: Die Autor:innen wählten bewusst eine späte Periode und normalisierten die Schreibung, „to reduce problems coming with historical language data as much as possible“ (S. 171). Muttersprachliche Intuition, auf der die Skala ruht, gibt es für Mittelhochdeutsch nicht; SemEval-2020 musste für Latein deshalb zu Urteilen gegen Wörterbuchdefinitionen wechseln (Schlechtweg et al. 2020, S. 5).

**2. A31, Kernfrage „Lenkt die Vorgabe eines Inventars das Urteil?“** DURel misst Bedeutungsnähe ohne Inventar und ist damit ein Gegenstück zur Kartenwahl. Die Arbeit selbst prüft aber keinen Ankereffekt eines Inventars; sie behauptet nur, dass keine Definition nötig ist (S. 173). Für eine Literaturbegründung von A31 taugt sie daher nur als Beleg, dass es die inventarfreie Alternative mit messbarer Übereinstimmung gibt, nicht als Beleg für eine Lenkung durch Inventare. Dafür ist Erk et al. 2013 (S. 512, 530) die bessere Quelle.

**3. Offener Punkt 20 (Auswertung der Lesarten).** Nicht direkt. Ein Gedanke für die Auswertung: Paare von Lesart-Paraphrasen zweier Personen ließen sich nach dem DURel-Muster auf Nähe bewerten (durch eine dritte Person), statt sie nur einer Karte zuzuordnen. Das ist eine eigene Ableitung, nicht Aussage der Arbeit.

**4. PROTOKOLL §9.1 und LITERATUR-IAA.md (Übereinstimmungswerte).** LITERATUR-IAA.md, Abschnitt „Historische Sprachen“, führt „DURel ρ ≈ 0,57 bis 0,68 (Schlechtweg et al. 2018 ○)“. Das ist am Volltext bestätigt (Spanne der Paarwerte, S. 172, Tab. 3). Hinzuzufügen wäre: Der Mittelwert ist im Text mit 0,66 angegeben, aus der Tabelle ergibt sich 0,635 (oben). Diese Werte sind Rangkorrelationen über Skalenurteile und nicht mit κ oder α der Kartenwahl (§9.1 Punkt 1) vergleichbar.

**5. PROTOKOLL §7 (Wer annotiert).** Der Befund, dass historisch geschulte Annotator:innen besser übereinstimmen (S. 172), stützt die Wahl fachkundiger Annotator:innen; bei zwei Personen pro Gruppe ist er schwach.

## Grenzen und Einwände

- Nur 22 Zielwörter, von Hand nach bekanntem Wandel ausgewählt (S. 171); kein Zufallsziehen der Wörter.
- Übereinstimmung nur als Rangkorrelation über alle Paare gemeinsam; keine Zufallskorrektur, keine Angabe zur Zahl ausgeschlossener 0-Urteile. Der Mittelwert 0,66 ist aus Tab. 3 nicht nachvollziehbar.
- Die Annotator:innen waren deutsche Muttersprachler:innen und urteilten über normalisiertes Neuhochdeutsch des 18. und 19. Jahrhunderts. Für Mittelhochdeutsch ohne Muttersprachler:innen und mit stärkerer Variation ist die Übertragbarkeit offen.
- Belegpaare messen Nähe, keine Bedeutungszuordnung; ein Gold im Sinne der Dissertation (Sense pro Beleg) entsteht daraus nicht direkt. Die Arbeit liefert Mittelwerte pro Wort und Gruppe, keine Bedeutungsgruppen; das Clustering kam erst in SemEval-2020 hinzu (Schlechtweg et al. 2020, S. 4 bis 6).
- Für ein onomasiologisches Inventar nicht einschlägig; die Arbeit kennt nur Wortbedeutungen im Sinne Blanks.

## Weiterführend

- Blank 1997, *Prinzipien des lexikalischen Bedeutungswandels am Beispiel der romanischen Sprachen*, Niemeyer (S. 169, 170): theoretische Grundlage, Kontinuum der Bedeutungsnähe.
- Brown 2008, Choosing sense distinctions for WSD: Psycholinguistic evidence, ACL Short Papers, S. 249 bis 252 (S. 169, 170): Herkunft der 4-stufigen Skala.
- Soares da Silva 1992, Homonímia e polissemia (S. 169, 170): experimentelle Prüfung der Unterscheidung von Polysemie und Homonymie.
- Erk, McCarthy & Gaylord 2009 und 2013 (S. 169, 170, 172): graduelle Bedeutungsannotation, Herkunft von Richtlinien und Maß.
- Bamman & Crane 2011, Measuring historical word sense variation, JCDL (S. 169): kleine Annotationsstudie zu lateinischen Texten verschiedener Zeiten.
- Paul 2002, *Deutsches Wörterbuch*, 10. Aufl. (S. 170, 171): Quelle der Wandelfälle.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
