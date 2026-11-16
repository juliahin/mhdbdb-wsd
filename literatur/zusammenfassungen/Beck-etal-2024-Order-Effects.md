# Beck, Eckman, Ma, Chew & Kreuter 2024: Order Effects in Annotation Tasks

**Datei:** `pdf/Beck-etal-2024-Order-Effects.pdf` (nur lokal; 6 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen; Tab. 1 und 2, Abb. 3 bis 5 (S. 83 bis 84) am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology 2024.uncertainlp-1.8 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: gedruckte Seite = PDF-Seite + 80 (PDF 1 = S. 81, PDF 6 = S. 86). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Beck, Jacob, Stephanie Eckman, Bolei Ma, Rob Chew & Frauke Kreuter (2024). Order Effects in Annotation Tasks: Further Evidence of Annotation Sensitivity. In: Raúl Vázquez, Hande Celikkanat, Dennis Ulmer, Jörg Tiedemann, Swabha Swayamdipta, Wilker Aziz, Barbara Plank, Joris Baan & Marie-Catherine de Marneffe (Hg.), *Proceedings of the 1st Workshop on Uncertainty-Aware NLP (UncertaiNLP 2024)*. St Julians, Malta: Association for Computational Linguistics, S. 81 bis 86.
- **DOI/URL:** 10.18653/v1/2024.uncertainlp-1.8 (aufgelöst, Crossref); https://aclanthology.org/2024.uncertainlp-1.8/ (Herausgeber:innen und Monat März nach dem BibTeX der Anthology, abgerufen 2026-11-16; Datum im PDF: 22.03.2024)
- **Lizenz:** CC BY 4.0 (ACL Anthology, Material ab 2016; FAQ abgerufen 2026-11-16); im PDF „©2024 Association for Computational Linguistics“.
- **Art:** Workshopbeitrag (Kurzbeitrag, von den Autor:innen „preliminary research“ genannt, S. 82)
- **Sprache:** Englisch

## Worum es geht

Die Arbeit prüft, ob die Position einer Beobachtung in einer Annotationssitzung das vergebene Label verändert (S. 81). Grundlage sind 44.550 Annotationen von 3.000 Tweets auf Hassrede (HS) und beleidigende Sprache (OL) durch 908 Prolific-Teilnehmende in fünf Varianten des Annotationsinstruments, je 50 Tweets in zufälliger Reihenfolge (S. 82). Je später ein Tweet in der Sitzung kam, desto seltener wurde er als HS oder OL markiert; der Effekt ist klein, aber signifikant und in fünf von zehn Kombinationen aus Bedingung und Label nachweisbar (S. 83 bis 85). Die Autor:innen deuten ihn eher als Belastung (Ermüdung) denn als Kontexteffekt und empfehlen zufällige Reihenfolge und genaue Dokumentation (S. 85).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Annotationen hängen von Merkmalen der Annotator:innen, vom Schulungsmaterial und von Gestaltung und Wortlaut des Instruments ab. | S. 81 Abstract | Rahmen der Autor:innen (eigene Vorarbeiten) |
| Wurden zwei Annotationen eines Tweets auf zwei Bildschirme verteilt statt auf einen, änderten sich die HS- und OL-Raten um fünf bis sieben Prozentpunkte. | S. 81 | referiert (eigene Vorarbeit Beck et al. 2022) |
| Kontexteffekte (auch Anchoring oder Priming genannt): Vorher Wahrgenommenes beeinflusst die Wahrnehmung, als Kontrast oder als Angleichung. | S. 81 | referiert (Tversky & Kahneman 1974; Strack 1992; Bless & Schwarz 2010) |
| In Umfragen ändern frühere Fragen, wie spätere verstanden werden; mit wachsender Länge nimmt „satisficing“ zu, d. h. eine ausreichend gute Antwort zu wählen, statt alle Antwortoptionen zu prüfen. Alternativ könnten Annotator:innen mit der Zeit besser werden. | S. 82 | referiert (Schuman & Presser 1996; Krosnick et al. 1996; Galesic & Bosnjak 2009; Lee et al. 2022) |
| Der Anteil der HS- und OL-Labels sinkt mit der Position in der Sitzung (lineares Wahrscheinlichkeitsmodell, Steigung −0,00057 für HS, −0,00090 für OL, beide p < 0,001). | S. 83, Tab. 1, Abb. 3 | eigenes Ergebnis |
| Der Koeffizient bleibt bei Kontrolle für Annotator:in, Bedingung oder Batch praktisch gleich. | S. 84, Abb. 5 | eigenes Ergebnis |
| Die Instrumentbedingung hat starke Haupteffekte; Reihenfolgeeffekte sind signifikant für HS in C und E, für OL in A, B und C, unterscheiden sich zwischen den Bedingungen aber nicht signifikant. | S. 84, Tab. 2, Abb. 4 | eigenes Ergebnis |
| Größe: Der 50. Tweet wird etwa 2,8 Prozentpunkte seltener als HS und 4,5 Prozentpunkte seltener als OL markiert als der erste; kein positiver Reihenfolgeeffekt in irgendeiner Bedingung. | S. 84 | eigenes Ergebnis |
| Deutung: eher Belastung (Ermüdung, Langeweile) als Kontexteffekt, weil die Bedingungsunterschiede nicht zu den Kontexthypothesen passen und die Belastung über alle Bedingungen gleich war. | S. 85 | Deutung der Autor:innen, ausdrücklich vorläufig |
| Empfehlung: Solange die Ursachen unklar sind, Beobachtungen zufällig ordnen und die Datenerhebung genau dokumentieren. | S. 85 | Empfehlung der Autor:innen |
| Offene Fragen: ob Reihenfolgeeffekte bei schwierigeren Aufgaben stärker sind und ob Richtlinien oder Tutorien das Annotationsverhalten verankern. | S. 85 | Ausblick |

## Daten, Methode, Zahlen

- **Daten:** 3.000 Tweets aus dem Korpus von Davidson et al. (2017), zufällig in Batches zu 50 gruppiert; jeder Batch 15-mal annotiert, dreimal in jeder von fünf Bedingungen (S. 82). 908 Prolific-Teilnehmende in den USA, je ein Batch in einer Bedingung; 44.550 Annotationen (S. 82). Daten öffentlich auf Hugging Face (`soda-lmu/tweet-annotation-sensitivity-2`, S. 82 Fn. 1).
- **Bedingungen (S. 82, Abb. 2):** A beide Labels auf einem Bildschirm; B erst HS, dann OL je Tweet auf zwei Bildschirmen; C umgekehrt; D erst HS für alle Tweets, dann OL für alle; E umgekehrt.
- **Reihenfolge:** innerhalb des Batches zufällig, aber **für alle 15 Annotator:innen desselben Batches gleich** (S. 82, S. 85).
- **Modelle:** lineare Wahrscheinlichkeitsmodelle, abhängige Variable HS bzw. OL ja/nein, unabhängige Variable Position 1 bis 50 (S. 83). Tab. 2 (S. 84, Seitenbild) enthält die Haupteffekte der Bedingungen (HS 0,2772 bis 0,35; OL 0,547 bis 0,620) und die Wechselwirkungen mit der Position (HS: C −0,00069*, E −0,00119***; OL: A −0,00121***, B −0,00108**, C −0,00138***).
- **Ausschlüsse:** abgebrochene Batches, zwei beschädigte Datensätze zu je 50 Tweets und N/A-Antworten (S. 82 Fn. 3).
- Kein Übereinstimmungsmaß; gemessen werden Labelraten, nicht Übereinstimmung zwischen Personen.

## Wörtliche Stellen

> „The order in which observations are presented to annotators influences the annotations they assign.“ (S. 84)

> „Until we better understand the causes of order effects, we recommend random ordering of observations. We also recommend thorough documentation of annotation collection methods to foster replicability and reproducibility.“ (S. 85)

> „[…] measure whether annotation guidelines/tutorials anchor the annotation behavior.“ (S. 85)

## Bezug zur Dissertation

**1. PROTOKOLL §7 Schritt 4 (Itemreihenfolge pro Annotator:in zufällig gemischt, Seed protokolliert, „weil Reihenfolge Urteile verschiebt (Beck et al. 2024)“): gestützt.** Die Arbeit zeigt Reihenfolgeeffekte (S. 83 bis 84) und empfiehlt zufällige Reihenfolge und Dokumentation (S. 85). Die Mischung **pro Person** geht über die Arbeit hinaus und behebt die Schwäche, die die Autor:innen selbst nennen: Bei ihnen war die Reihenfolge für alle Annotator:innen gleich, wodurch sich Ursachen nicht trennen ließen (S. 85). Folge, die das Protokoll noch nicht nennt: Wird pro Person gemischt, wird ein Reihenfolgeeffekt nicht zu einer gemeinsamen Verzerrung, sondern zu zusätzlicher Abweichung zwischen den beiden; er drückt also die Übereinstimmung, statt sie zu heben (eigene Folgerung, nicht aus der Arbeit).

**2. PROTOKOLL §7 Schritt 4 („Kurze Sitzungen; die Zeitstempel erlauben nachträglich eine Prüfung auf Ermüdung und Drift“) und §8 (Ereignisprotokoll): gestützt.** Die Deutung als Belastungseffekt (S. 85) spricht für kurze Sitzungen. Weil das Ereignisprotokoll Position und Zeitstempel festhält, lässt sich die Analyse der Arbeit wiederholen. **Vorschlag für §9.1:** als Kontrollauswertung den Anteil von `SENSE` gegenüber Ausweichlabels, die Sicherheitsangabe und die Übereinstimmung gegen die Position in der Sitzung auftragen (lineares Modell wie S. 83). Die Rundengröße 25 im Pilot (A32) liegt unter den 50 Items der Arbeit, deren Effekt über 50 Positionen nur wenige Prozentpunkte betrug (S. 84).

**3. A31 und offener Punkt 22 (Lesart-Schritt in der Hauptrunde): Einwand.** Nach der Vorarbeit der Autor:innen verschob schon die Verteilung zweier Fragen auf zwei Bildschirme die Labelraten um fünf bis sieben Prozentpunkte (S. 81, referiert), und in dieser Arbeit hat die Bedingung starke Haupteffekte (S. 84). `lesart-zuerst` und `direkt` sind zwei verschiedene Instrumente. Die Pilotschwelle (A32) misst die Zuverlässigkeit des Instruments `lesart-zuerst`; wird die Hauptrunde mit `direkt` annotiert, gilt diese Messung streng genommen für ein anderes Instrument. **Vorschlag:** bei der Entscheidung nach dem Pilot (Punkt 22) festhalten, dass ein Wechsel des Ablaufs zwischen Pilot und Hauptrunde eine Abweichung ist und mindestens eine Pilotrunde mit dem Hauptrundenablauf verlangt.

**4. Offener Punkt 21 (Literatur zum Ankereffekt vorgegebener Antwortoptionen): Spur, keine Antwort.** Die Arbeit selbst untersucht keine vorgegebenen Optionen, verweist aber auf die Umfrageforschung, in der Antwortoptionen und Fragenkontext untersucht sind: „satisficing“ als Wahl einer ausreichend guten statt der besten Antwortoption (Krosnick et al. 1996, S. 82) und Kontexteffekte von Fragen (Schuman & Presser 1996; Strack 1992; S. 82). Satisficing betrifft die Kartenwahl unmittelbar: Wer die erste passende Karte nimmt, ohne alle zu prüfen, wählt abhängig von der gezeigten Reihenfolge; die zufällige Kartenreihenfolge (§5 Punkt 5) macht das zu Rauschen statt zu Verzerrung. Die Frage der Arbeit, ob Richtlinien oder Tutorien verankern (S. 85), betrifft auch die Pilotbesprechungen nach jeder Runde (§7 Schritt 2).

**5. A27 (gleiche Darbietung für Mensch und LLM, gemischte Kartenreihenfolge): ergänzt.** Die Arbeit betrifft nur Menschen; dass schon Instrumentdetails die Labels verschieben (S. 81, S. 84), stützt aber den Grundsatz, dass Mensch und LLM dieselbe Darbietung bekommen.

**6. LITERATUR-IAA.md, Zeile „Reihenfolge der Items verändert Urteile; Vorannotationen verankern“ (Beck et al. 2024 ✔): bestätigt** für den Teil „Reihenfolge der Items verändert Urteile“. Zu ergänzen wäre die Größe: klein (2,8 bzw. 4,5 Prozentpunkte über 50 Items, S. 84) und nur in der Hälfte der Bedingungen signifikant.

## Grenzen und Einwände

- Die Reihenfolge war pro Batch für alle Annotator:innen gleich; Ursachen (Kontrast, Angleichung, Lernen, Ermüdung) lassen sich nicht trennen, und ein Fehler der Randomisierung ist nicht ausgeschlossen (S. 85, von den Autor:innen selbst genannt).
- Nur 50 Items pro Person, nur englische Tweets, nur Annotator:innen in den USA, Laien über eine Crowdworking-Plattform (S. 85).
- Binäre Aufgabe mit subjektivem Gegenstand (Hassrede); die Übertragung auf WSD mit Expert:innen und vielen Optionen ist nicht geprüft.
- Kein Übereinstimmungsmaß; ob Reihenfolgeeffekte die IAA verändern, sagt die Arbeit nicht.
- Kurzbeitrag in einem Workshop, ausdrücklich vorläufig (S. 82).
- Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar: nicht berührt.

## Weiterführend

- Beck, Eckman, Chew & Kreuter 2022, Improving labeling through social science insights, HCI International 2022, S. 245 bis 261 (S. 81, 86): Effekt der Bildschirmaufteilung.
- Kern, Eckman, Beck, Chew, Ma & Kreuter 2023, Annotation sensitivity, Findings of EMNLP 2023, S. 14874 bis 14886 (S. 82, 84, 86): Datensatz und Wirkung auf Modelle.
- Krosnick, Narayan & Smith 1996, Satisficing in surveys, *New Directions for Evaluation* 1996(70), S. 29 bis 44 (S. 82, 86): Kandidat für offenen Punkt 21.
- Schuman & Presser 1996, *Questions and Answers in Attitude Surveys*, Sage (S. 82, 85, 86): Fragenform, Wortlaut, Kontext.
- Strack 1992, „Order effects“ in survey research (S. 81, 86); Bless & Schwarz 2010, *Advances in Experimental Social Psychology* 42 (S. 81, 86).
- Galesic & Bosnjak 2009, *Public Opinion Quarterly* 73(2) (S. 82, 86): Fragebogenlänge und Antwortqualität.
- Lee, Klie & Gurevych 2022, Annotation curricula, *Computational Linguistics* 48(2) (S. 82, 86).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF.
