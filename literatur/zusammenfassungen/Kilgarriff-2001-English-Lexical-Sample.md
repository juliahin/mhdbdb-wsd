# Kilgarriff 2001: English Lexical Sample Task (SENSEVAL-2)

**Datei:** `pdf/Kilgarriff-2001-English-Lexical-Sample.pdf` (nur lokal; 4 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Tabellen 1 bis 3 am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit https://aclanthology.org/S01-1004.pdf (SHA-256 verglichen am 2026-11-13); es enthält keine Markierungen. Eine DOI wurde nicht gefunden (Crossref-Suche 2026-11-13 ohne Treffer).

Seitenzählung: PDF-Seite n = gedruckte S. 16 + n (PDF 1 = S. 17, PDF 4 = S. 20). Unten stehen gedruckte Seiten. Der Scan hat eine OCR-Textebene mit Fehlern („choic~“, „cla.':;s“); Zahlen sind am Seitenbild geprüft.

## Bibliografie

- **Vollständig:** Kilgarriff, Adam (2001). English Lexical Sample Task Description. In: Judita Preiss & David Yarowsky (Hg.), *Proceedings of SENSEVAL-2 Second International Workshop on Evaluating Word Sense Disambiguation Systems*. Toulouse: Association for Computational Linguistics, S. 17 bis 20.
- **DOI/URL:** keine DOI; https://aclanthology.org/S01-1004 (BibTeX der Anthology: Juli 2001, Toulouse, S. 17 bis 20, Herausgeber:innen Preiss und Yarowsky; abgerufen 2026-11-13). Seiten an den gedruckten Seitenzahlen des PDFs bestätigt.
- **Lizenz:** CC BY-NC-SA 3.0 (ACL Anthology, Material vor 2016, laut FAQ der Anthology, abgerufen 2026-11-13).
- **Art:** Workshopbeitrag (Aufgabenbeschreibung)
- **Sprache:** Englisch

## Worum es geht

Kilgarriff beschreibt die englische Lexical-Sample-Aufgabe für Adjektive und Nomen in SENSEVAL-2 (die Verben bereitete eine andere Gruppe vor) (S. 17). Sie folgte den Prinzipien von SENSEVAL-1, nutzte aber statt HECTOR das Inventar WordNet, dessen Einträge für die Stichprobenwörter vorher von Lexikograf:innen überarbeitet wurden (S. 17 bis 18). Das Gold entstand mit einem adaptiven Verfahren (zwei Annotierende, bei Abweichung weitere) und erreichte eine feinkörnige Übereinstimmung von 85,5 % (S. 19). Die besten Systeme lagen etwa 14 % unter SENSEVAL-1; Kilgarriff führt das auf die Sense-Unterscheidungen von WordNet zurück und folgert, die Forschung solle sich von den Algorithmen den Sense-Unterscheidungen zuwenden (S. 20).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Aufbau nach denselben Prinzipien wie SENSEVAL-1 (Kilgarriff & Rosenzweig 2000); nur Adjektive und Nomen, Verben bei Palmer et al. | S. 17 | Beschreibung |
| Lexikon-Stichprobe mit niedrig-, mittel- und hochfrequenten Wörtern, alle verschieden von SENSEVAL-1. | S. 17, Abschnitt 1 | Beschreibung |
| Korpus vor allem BNC (neue Ausgabe, weltweit verfügbar), wenig Wall Street Journal, weil amerikanisches Englisch ohne Rechtsprobleme kaum verfügbar war. | S. 17, Abschnitt 2 | Beschreibung |
| **Belege pro Wort nach „standard SENSEVAL procedure“: 75 + 15n + 6m**, n = Zahl der Senses, m = Zahl der Mehrwortausdrücke mit dem Wort, jeweils relativ zum Lexikon; tatsächlich etwas weniger, weil Belege mit falscher Wortart oder Unbrauchbarkeit entfernt wurden. | S. 17, Abschnitt 2 | Verfahren |
| **WordNet statt HECTOR:** dafür sprach die Verbreitung, dagegen die Sense-Unterscheidungen. WordNet ist wie ein Thesaurus um Synsets organisiert, nicht um die Bedeutungen eines Wortes; der Lexikograf achtet daher weniger auf die Unterscheidung zweier Senses eines Wortes. WSD brauche „clear and well-motivated sense distinctions“. | S. 17, Abschnitt 3 | eigene Analyse |
| Alle Stichprobeneinträge wurden von einer Lexikograf:in durchgesehen, vor allem um zu wenig unterschiedene Senses zusammenzulegen; die Princeton-Gruppe übernahm die Änderungen in WordNet 1.7. Die Einträge der Stichprobenwörter waren im Frühjahr 2001 fixiert. | S. 17 bis 18, Abschnitt 3 | Verfahren |
| Die Annotierenden bekamen eine HTML-Fassung jedes Eintrags mit einem **Merkwort pro Sense** statt „easily-forgotten, easily-confused sense numbers“; die Merkwörter wählte eine Lexikograf:in. | S. 18, Abschnitt 3 | Verfahren |
| Annotierende: drei professionelle Lexikograf:innen und vierzehn Studierende und andere, ausgewählt über einen Eignungstest im Netz (Belege aus SENSEVAL-1 mit bekanntem Gold); Bezahlung pro Stück. | S. 18, Abschnitt 4 | Verfahren |
| Kontext: Abschnitte von zehn Sätzen, das Zielwort im letzten Satz hervorgehoben. Rückgaben wurden automatisch auf unmögliche Antworten geprüft und zur Korrektur zurückgeschickt. | S. 18 bis 19, Abschnitt 4 | Verfahren |
| Richtlinien entwickelten sich während der Arbeit: Fragen einer Person und die Antwort gingen an alle und in die Richtlinien. | S. 19 | Verfahren |
| Wie in SENSEVAL-1 waren **„Unassignable“ und „Proper-name“** immer verfügbar; Annotierende sollten **mehrere Tags** vergeben, „where multiple tags were equally applicable“; Belege mit falscher Wortart wurden markiert und gelöscht. | S. 19 | Verfahren |
| **Adaptives Verfahren:** (1) an zwei Annotierende; (2) stimmen sie völlig überein, Ende; (3) sonst an eine weitere Person; (4) gibt es einen oder mehrere Tags, auf die sich zwei einigen? (5) wenn ja, Ende, Gold = alle Tags, auf die sich zwei einigen; (6) sonst zurück zu 3. | S. 19, Abschnitt 5 | Verfahren |
| Annotationen pro Beleg: 2 bei 5032 (66,5 %), 3 bei 2446 (32,3 %), 4 bei 86 (1,1 %), 5 bei 4 (0,05 %). Von den 5032 Zweierfällen einigten sich die beiden in 4688 auf einen Tag, in 340 auf zwei, in 4 auf drei. | S. 19 | eigenes Ergebnis |
| ITA feinkörnig, mit demselben Bewertungsalgorithmus wie für die Systeme: je Paar zwei Werte (jede Antwort einmal als Schlüssel), je Beleg auf höchstens 1 normiert. **Gesamt-ITA 85,5 %** (Adjektive 83,4 %, Nomen 86,3 %). | S. 19, Tab. 1 (S. 18) | eigenes Ergebnis |
| Alle Zahlen gelten für feine Senses; grobe Gruppen entstanden unabhängig von der Goldannotation. | S. 19, Anm. 2 | Beschreibung |
| **Kein Kappa**, weil es mehrere Berechnungswege gab, unklar war, welcher passt, und es mehr verwirrt als geklärt hätte; außerdem seien die berichteten Werte, „unlike kappa figures, […] directly comparable with system performance scores“. | S. 19 bis 20, Anm. 3 | eigene Begründung |
| **Replizierbarkeit statt ITA als Obergrenze:** Interessanter als die ITA sei, wie stark zwei völlig verschiedene Teams mit derselben Methode übereinstimmen; „It is the replicability figure, rather than ITA, which defines an upper bound for the task.“ Eine solche Studie gab es für SENSEVAL-2 noch nicht. | S. 20, Abschnitt 5 | eigene These, Verweis auf Kilgarriff & Rosenzweig 2000 und Kilgarriff 1999 |
| Daten im SENSEVAL-XML, je Wort Training zu Test 2:1; Verteilung, Baselines und Wertung an der UPenn. | S. 20, Abschnitt 6 | Beschreibung |
| Ergebnisse (Tab. 3): beste überwachte Systeme mit vollständiger Bearbeitung um 0,64 Precision; Baselines Lesk 0,51 und „Commonest“ 0,48. | S. 20, Tab. 3 | Ergebnis |
| Gegenüber SENSEVAL-1 fiel die Leistung der besten Systeme um etwa 14 %, obwohl teils verbesserte Systeme antraten. Kilgarriff vermutet die Ursache im Lexikon: Hohe Genauigkeit sei nur möglich, wo das Lexikon klare, gut begründete Unterscheidungen macht und genug Information dazu liefert. „[…] it is time to turn our attention from algorithms, to sense distinctions.“ | S. 20, Abschnitt 7 | eigene Deutung, nicht getestet |

## Daten, Methode, Zahlen

**Tab. 1 (S. 18, am Seitenbild geprüft):** 15 Adjektive (2301 Belege, ITA 83,4 %) und 29 Nomen (5266 Belege, ITA 86,3 %), zusammen 7567 Belege, ITA 85,5 %. Je Wort Sense-Zahl (2 bis 13), Mehrwortausdrücke (0 bis 82), Belege (70 bis 455) und ITA. Spannweite der ITA: 67,8 % (*simple*, 7 Senses) bis 98,7 % (*detention*, 2 Senses). Unter 80 % liegen *free*, *graceful*, *natural*, *simple* (Adjektive) und *art*, *day*, *feeling*, *lady*, *stress* (Nomen). Nachgerechnet: Die Belegzahlen der Adjektive summieren sich auf 2301, die der Nomen auf 5266.

**Annotationen pro Beleg (S. 19):** 5032 + 2446 + 86 + 4 = 7568, einer mehr als die 7567 Belege in Tab. 1; die Abweichung erklärt das Werk nicht. Anteil der Zweierfälle mit Einigung auf mehrere Tags: (340 + 4) / 5032 ≈ 6,8 % (eigene Rechnung).

**Tab. 2 (S. 19, am Seitenbild geprüft), häufigste Muster bei drei Annotierenden:** z. B. A / A / B → Gold A (651 Fälle); A / A;B / A → A (550); A / A;B / B → A;B (209); A / A;B / A;B → A;B (189); A / A;B / C → A (162). Mehrfachtags entstehen im Gold also, wenn zwei Personen sich auf verschiedene Tags je paarweise einigen.

**Tab. 3 (S. 20, am Seitenbild geprüft), Precision (PR) und Anteil bearbeiteter Belege (ATT):**

| Gruppe | System | PR | ATT |
|---|---|---|---|
| überwacht | BCU ehu-dlist-best | 0,82 | 28 |
| überwacht | IRST | 0,67 | 25 |
| überwacht | JHU (R) | 0,64 | 100 |
| überwacht | SMUls | 0,64 | 100 |
| überwacht | KUNLP | 0,63 | 100 |
| Baseline überwacht | Base Lesk | 0,51 | 100 |
| Baseline überwacht | Base Commonest | 0,48 | 100 |
| nicht überwacht | ITRI-WASPS | 0,58 | 55 |
| Baseline nicht überwacht | Base Lesk-defs | 0,16 | 100 |
| Baseline nicht überwacht | Base random | 0,14 | 100 |

(Auswahl; im Original fehlt bei UNED-LS-U der Dezimalpunkt, „40“.)

## Wörtliche Stellen

> „[…] the goal was to have 75 + 15n + 6m instances for each lexical-sample word, where n is the number of senses the word has and m is the number of multiword expressions that the word is part of […].“ (S. 17)

> „[…] taggers were told to put down more than one tag, where multiple tags were equally applicable.“ (S. 19)

> „Also the figures shown, unlike kappa figures, have the merit of being directly comparable with system performance scores.“ (S. 19 bis 20, Anm. 3)

> „It is the replicability figure, rather than ITA, which defines an upper bound for the task.“ (S. 20)

> „An implication for future WSD research is that it is time to turn our attention from algorithms, to sense distinctions.“ (S. 20)

## Bezug zur Dissertation

**Prüfauftrag zu `goldstandard/LITERATUR-IAA.md`** (Zeile „Rohübereinstimmung ist direkt mit Systemgenauigkeit vergleichbar“, Kilgarriff 2001 ✔; übernommen in PROTOKOLL §9.1, Punkt 2):

- **Gedeckt** durch Anm. 3 (S. 19 bis 20). Zwei Präzisierungen: (a) Kilgarriffs Werte sind keine reine Rohübereinstimmung, sondern mit dem Wertungsalgorithmus der Systeme berechnet (Teilpunkte bei Mehrfachtags, je Paar in beiden Richtungen, je Beleg normiert; S. 19). Vergleichbar mit Systemwerten sind sie gerade deshalb, weil derselbe Algorithmus angewandt wird. Für das Protokoll heißt das: Die „Überschneidungs“-Variante in §9.1, Punkt 2 und die Bewertungsregeln in §9.2 sollten dieselbe Regel für Mengen verwenden, sonst gilt die Vergleichbarkeit nicht. (b) Die Begründung steht in einer Fußnote und ist eine Behauptung, kein Nachweis; Kappa wurde auch deshalb nicht berechnet, weil unklar war, wie.

**Prüfauftrag zu `goldstandard/LITERATUR-STICHPROBE.md`** (Zeile Senseval, Kilgarriff 2001 ✔): *„Senseval-2: 75 + 15n + 6m Belege pro Wort“* ist **gedeckt** (S. 17), gilt für Adjektive und Nomen der englischen Lexical-Sample-Aufgabe; n und m sind relativ zum Lexikon.

**Weitere Bezüge:**

- **PROTOKOLL §9.2 („Die menschliche IAA ist die Obergrenze“) und Vorschlag V26:** Kilgarriff selbst trennt 2001 die ITA von der **Replizierbarkeit** und nennt nur diese die Obergrenze (S. 20); 1998 hatte er noch die ITA so genannt (ITRI-Fassung S. 10). Für die Dissertation stützt das V26: Die menschliche IAA ist ein Referenzwert. Eine Replizierbarkeitsmessung (ein zweites Paar mit denselben Richtlinien) ist im Protokoll nicht vorgesehen; das sollte als Grenze genannt werden.
- **PROTOKOLL §6 (Status):** Die SENSEVAL-2-Optionen decken sich weitgehend mit den Status des Protokolls: mehrere Tags „equally applicable“ entspricht `MEHRERE` („gleichermaßen“), „Unassignable“ entspricht `KEINE_PASST`, das Markieren falscher Wortart entspricht in etwa `LEMMA_FALSCH` (S. 19). Der Wortlaut von §6 hat damit ein direktes Vorbild.
- **PROTOKOLL §7 und A32 (Pilot):** Die Richtlinien wuchsen bei SENSEVAL-2 während der Hauptannotation (S. 19); das Protokoll friert sie vor der Hauptrunde ein. Das ist strenger und sollte so begründet werden.
- **PROTOKOLL §7, Schritt 6 (Mehrfachlabel im Gold):** Das adaptive Verfahren erzeugt Mehrfachlabels, wenn je zwei Personen verschiedene Tags teilen (Tab. 2, S. 19). Im Protokoll entsteht ein Mehrfachlabel dagegen durch `MEHRERE` einer Person oder durch Adjudikation. Bei SENSEVAL-2 einigten sich Paare in etwa 6,8 % der Zweierfälle auf mehr als einen Tag (eigene Rechnung, S. 19); das ist eine erste Größenordnung, mit der der `MEHRERE`-Anteil im Pilot verglichen werden kann.
- **PROTOKOLL §5 (Karten mit Begriffsnamen) und §9.2 (Antwort mit Kartennummer):** Kilgarriff ersetzte Sense-Nummern für die Menschen durch Merkwörter, weil Nummern leicht vergessen und verwechselt werden (S. 18). Das Protokoll zeigt den Menschen ebenfalls Begriffsnamen; das LLM antwortet dagegen mit Kartennummer oder Sense-ID. Die Asymmetrie ist begründet (Parsen), sollte aber in Freeze 2 bewusst festgehalten werden.
- **PROTOKOLL §6, Kontext (offener Punkt Kontextumfang):** SENSEVAL-2 zeigte zehn Sätze mit dem Zielwort im letzten Satz (S. 18), also nur vorausgehenden Kontext. Ein Anhaltspunkt für die noch offene Ausschnittsgröße.
- **PROTOKOLL §9.1, Punkt 7 und Nebenfrage zum Begriffssystem:** Der Leistungsabfall von etwa 14 % mit WordNet gegenüber HECTOR (S. 20) ist die stärkste Aussage des Werks über das Gewicht des Inventars. Für die Dissertation heißt das: Ein niedriger LLM- oder IAA-Wert kann am Begriffssystem liegen; die Auswertung über Oberbegriffe und die `KEINE_PASST`-Belege sind der Ort, das zu prüfen. Kilgarriffs Erklärung ist allerdings eine Vermutung ohne Test.
- **PROTOKOLL §1 und §9.2 (MFS-Baseline):** In SENSEVAL-2 lag die Baseline „Commonest“ bei 0,48, der beste vollständig bearbeitende überwachte Wert bei 0,64 (Tab. 3, S. 20), also etwa 16 Punkte Abstand bei einer ITA von 85,5 %. Das zeigt den Raum zwischen Boden und Decke in einem feinkörnigen englischen Setting (vgl. Gale et al. 1992, „dynamic range“).

## Grenzen und Einwände

- Kurze Aufgabenbeschreibung; eine Analyse der Ergebnisse fehlt nach eigener Aussage („There has not yet been time“, S. 20).
- Die ITA ist nicht zufallskorrigiert und mit Teilpunkten für Mehrfachtags berechnet; mit exakter Übereinstimmung oder Kappa ist sie nicht direkt vergleichbar.
- Die Annotierenden waren gemischt (Lexikograf:innen, Studierende); die ITA wird nicht nach Gruppen getrennt.
- Kleine Unstimmigkeit in den Zählungen (7568 gegen 7567 Belege).
- Die Erklärung des Leistungsabfalls durch WordNet ist nicht von anderen Unterschieden getrennt (andere Wörter, anderes Korpus, BNC statt HECTOR-Korpus).
- Übertragbarkeit: Englisch, Wörterbuch-Inventar; die Prinzipien (Status, adaptives Verfahren, Merkwörter) sind übertragbar, die Zahlen nicht.

## Weiterführend

- Kilgarriff & Rosenzweig (2000), Framework and Results for English SENSEVAL, *Computers and the Humanities* 34(1 bis 2), S. 15 bis 48 (S. 20): Langfassung zu SENSEVAL-1.
- Kilgarriff (1999), 95 % replicability for manual word sense tagging, EACL, Bergen, S. 277 bis 278 (S. 20): Primärquelle zur Replizierbarkeit als Obergrenze.
- Palmer et al. (2001), SENSEVAL-2 English all-words und Verben (S. 17): im selben Band.
- Cotton & Edmonds (2001), Organisation und Wertung (S. 20): im selben Band.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
