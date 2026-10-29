# Weeber et al. 2021: Assisted Text Annotation Using Active Learning

**Datei:** `pdf/Weeber-etal-2021-Active-Learning.pdf` (nur lokal; 2 Seiten, arXiv-Fassung 2112.11914v1 vom 15.12.2021 laut Randvermerk S. 1)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganzes PDF an der Textebene gelesen, S. 1 am Seitenbild; Venue nach `BESCHAFFUNG.md` Abschnitt C (Crossref, am 2026-10-23 nachgeprüft).

Seitenzählung: Das lokale PDF trägt keine Seitenzahlen; zitiert wird PDF-Seite 1 und 2. Die Druckfassung steht laut Crossref auf S. 287 bis 288 (○, Druckfassung nicht eingesehen).

## Bibliografie

- **Vollständig:** Weeber, Franziska; Hamborg, Felix; Donnay, Karsten & Gipp, Bela (2021). Assisted Text Annotation Using Active Learning to Achieve High Quality with Little Effort. In: *2021 ACM/IEEE Joint Conference on Digital Libraries (JCDL)*, Champaign, IL: IEEE, S. 287 bis 288.
- **DOI/URL:** 10.1109/JCDL52503.2021.00038 (laut `BESCHAFFUNG.md` C über doi.org und Crossref geprüft); lokal arXiv:2112.11914v1.
- **Art:** Poster bzw. Kurzbeitrag (der Text nennt sich „this poster", PDF-Seite 1 und 2); ob begutachtet, nicht geprüft
- **Sprache:** Englisch

## Worum es geht

Der Beitrag schlägt ein Annotationswerkzeug vor, das Active Learning (AL) mit einem vortrainierten Sprachmodell (Longformer) verbindet, damit Forschende mit wenigen manuellen Labels große annotierte Datensätze erzeugen können (Abstract, PDF-Seite 1). Erprobt wird es an der Klassifikation von Frames in Nachrichtenartikeln (Media Frames Corpus, Thema Todesstrafe). Vorläufiges Ergebnis: Das AL-Modell erreicht mit 320 gelabelten Dokumenten fast die Leistung des Modells, das auf dem ganzen Pool trainiert wurde (PDF-Seite 2). Eine Benutzeroberfläche gibt es noch nicht; sie ist als wichtigste künftige Arbeit genannt.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| AL trainiert einen Klassifikator in Runden und fragt jeweils nur die für das Modell informativsten Instanzen zur manuellen Annotation ab; das spart besonders bei unbalancierten Klassen Labels, weil die Minderheitsklasse in den Abfragen überrepräsentiert ist. | PDF-S. 1, Abschn. I | referiert (Settles 2009; Tomanek et al. 2007) |
| Ablauf in zwei Phasen: Auswahl einer Startmenge (Seed Set), dann wiederholt Vorhersage, Abfrage neuer Instanzen, Neutraining, bis eine Leistungsschwelle oder eine vorab festgelegte Zahl annotierter Texte erreicht ist. | PDF-S. 1, Abschn. I | referiert |
| Bisherige AL-Annotation leide an veralteten Methoden (Bag of Words, SVM) und fehlenden Oberflächen für Nicht-Programmierer:innen. | PDF-S. 1, Abschn. I | Einschätzung der Autor:innen |
| Verfahren: Longformer mit einer vollverbundenen Schicht über dem Klassifikations-Token; zufällige Startmenge; Abfrage nach kleinstem Abstand zwischen den beiden größten Logits (Margin-Unsicherheit). | PDF-S. 2, Abschn. II | eigenes Verfahren |
| Labeln von Frames ist auch für Menschen schwer, weil Frames subtil und einander ähnlich sind. | PDF-S. 2, Abschn. III | Einschätzung, ohne IAA-Zahl |
| Auf der Mehrheitsklasse sind aktiver und passiver Lerner gleich gut; das AL-Modell lernt bei den Minderheitsklassen schneller. | PDF-S. 2, Abschn. III | eigenes Ergebnis (nur als Satz und Abb. 1) |
| Konzeptuell sei die Methode auf jede Klassifikationsaufgabe anwendbar. | PDF-S. 2, Abschn. III | Behauptung, nicht gezeigt |

## Daten, Methode, Zahlen

Alle Zahlen an der Textebene geprüft (PDF-Seite 2, Abschnitt III und IV):

- Daten: Media Frames Corpus, Thema Todesstrafe; alle 2.458 Artikel mit einem der drei häufigsten primären Frames: Political (10 %), Crime and Punishment (29 %), Legality, Constitutionality and Jurisdiction (61 %). Aufteilung 80 % AL-Pool, 20 % Test.
- Ablauf: zufällige Startmenge von 160 Dokumenten, dann zehn Runden zu je 40 Abfragen. Vergleich mit einem passiven Lerner, der zufällig zieht.
- Ergebnis: Modell auf dem ganzen Pool F1m = 84,6; AL-Modell F1m = 83,5 nach 320 gelabelten Beispielen (vier Runden); passiver Lerner maximal F1m = 83,4 mit 400 Beispielen (sechs Runden).
- Daraus im Fazit: 83,7 % weniger Trainingsbeispiele als der volle Pool und 20,0 % weniger als der passive Lerner; im Abstract: AL brauche „only 16.3 %" der Annotationen (PDF-Seite 1). Die Zahlen sind untereinander stimmig (320 von 0,8 × 2.458 ≈ 1.966; 320 statt 400).
- Was F1m genau ist (vermutlich makro-gemittelt), definiert der Text nicht. Nur ein Lauf, keine Streuung, keine Signifikanz.

## Wörtliche Stellen

> „Labeling frames is difficult, even for human annotators, due to the frames' subtlety and similarity to another." (PDF-Seite 2)

> „On the majority class, the performance is equally good for both learners, but the AL model learns faster for the minority classes." (PDF-Seite 2)

## Bezug zur Dissertation

- **Kaum direkter Bezug zum Goldstandard.** Das Protokoll baut kein Trainingsset, sondern ein Evaluationsset; die Items werden geschichtet und zufällig gezogen (PROTOKOLL §4.4), nicht nach Modellunsicherheit ausgewählt. Eine AL-Auswahl würde die Stichprobe zugunsten schwieriger Items verzerren und das primäre Schätzziel (§4.1, ungewichtete Genauigkeit über die Hauptstichprobe) unbrauchbar machen. Das ist ein Argument, AL in der Arbeit ausdrücklich abzugrenzen.
- **Möglicher Bezug für eine spätere Phase:** Wenn nach dem Goldstandard der unannotierte Teil D0 (§3; 1.293.790 Zieltokens) mit LLM-Hilfe annotiert werden soll, wäre eine unsicherheitsgesteuerte Auswahl dessen, was Menschen prüfen, ein naheliegender Weg. Die Beobachtung, dass AL bei Minderheitsklassen schneller lernt (PDF-Seite 2), passt zu den Nicht-MFS-Senses, die §9.2 eigens auswertet.
- Julias Randnotiz (unten) stellt dieselbe Frage: Im Projekt gibt es schon Labels (Silber, §2).

## Grenzen und Einwände

- Zwei Seiten, vorläufige Ergebnisse, ein Datensatz, ein Thema, drei Klassen, ein Lauf ohne Streuung.
- Dokumentklassifikation, keine tokenbezogene Aufgabe; jedes Lemma der WSD hat ein eigenes Inventar (PROTOKOLL §9.1 Punkt 3), ein einzelner Klassifikator über alle Items passt darauf nicht.
- Die Qualität der Labels selbst wird nicht gemessen; „high quality" heißt hier nur, dass die Klassifikationsleistung nahe am Vollmodell liegt. Die Gold-Labels des MFC werden als gegeben genommen.
- Der Vergleich mit dem passiven Lerner stellt das AL-Ergebnis nach vier Runden dem Maximum des passiven Lerners gegenüber; die Kurven sind nur in Abb. 1 [am PDF zu prüfen].
- Kein LLM im heutigen Sinn (kein Prompting), sondern ein feinabgestimmtes Encoder-Modell.

## Weiterführend

- Settles 2009, *Active Learning Literature Survey*, Technical Report, University of Wisconsin-Madison (PDF-Seite 2, Ref. [4]); von Julia markiert.
- Skeppstedt, Paradis & Kerren 2016, PAL, Werkzeug für Vorannotation und AL, JLCL 31(1) (Ref. [5]).
- Tomanek, Wermter & Hahn 2007, JANE, LAW-Workshop (Ref. [6]).
- Prodigy (Explosion AI), Annotationswerkzeug mit AL (Ref. [3]); von Julia markiert.

## Julias Markierungen im PDF

27 Hervorhebungen, 3 Notizen (`md/Weeber-etal-2021-Active-Learning.markierungen.md`). Aufgenommen: Kosten manueller Annotation und AL-Definition (PDF-Seite 1, in „Kernaussagen"); die zwei Phasen und der Ablauf der Abfrage (PDF-Seite 1); Minderheitsklassen lernen schneller (PDF-Seite 2); Übertragbarkeit „auf jede Klassifikationsaufgabe" (PDF-Seite 2, als nicht gezeigte Behauptung); 83,7 % und 20,0 % mit F1m 83,5 gegen 84,6 (PDF-Seite 2); Schwierigkeit des Frame-Labelns (PDF-Seite 2); Settles und Prodigy (unter „Weiterführend"). Nur knapp aufgenommen: die Stichworte „deep learning", NLU durch Transformer (PDF-Seite 1 bis 2).

### Julias Notizen im PDF

- PDF-Seite 1: „gut, einige Anknüpfungspunkte für Active Learning (pro/contra) v.a. für kleine Ressourcen nützlich, bei mir gibts es aber schon Labels ?“
- PDF-Seite 1: „Ablauf“ (neben der Beschreibung der zwei Phasen)
- PDF-Seite 2: „Trainingsdaten bei mir relativ kleines Corpus?“
