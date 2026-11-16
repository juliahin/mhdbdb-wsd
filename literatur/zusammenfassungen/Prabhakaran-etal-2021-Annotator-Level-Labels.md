# Prabhakaran, Mostafazadeh Davani & Díaz 2021: On Releasing Annotator-Level Labels and Information in Datasets

**Datei:** `pdf/Prabhakaran-etal-2021-Annotator-Level-Labels.pdf` (nur lokal; 6 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen; Tab. 1 und Abb. 1 (S. 135) am Seitenbild geprüft; Abb. 2 (S. 136) nur über den Fließtext. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology 2021.law-1.14 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: gedruckte Seite = PDF-Seite + 132 (PDF 1 = S. 133, PDF 6 = S. 138; Seitenzahl oben auf der Seite). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Prabhakaran, Vinodkumar, Aida Mostafazadeh Davani & Mark Díaz (2021). On Releasing Annotator-Level Labels and Information in Datasets. In: Claire Bonial & Nianwen Xue (Hg.), *Proceedings of the Joint 15th Linguistic Annotation Workshop (LAW) and 3rd Designing Meaning Representations (DMR) Workshop*. Punta Cana, Dominikanische Republik: Association for Computational Linguistics, S. 133 bis 138.
- **DOI/URL:** 10.18653/v1/2021.law-1.14 (aufgelöst, Crossref); https://aclanthology.org/2021.law-1.14/ (Herausgeber:innen und Monat November nach dem BibTeX der Anthology, abgerufen 2026-11-16)
- **Namensform:** im PDF „Mark Díaz“, bei ACL Anthology und Crossref „Mark Diaz“. Die ersten beiden sind laut PDF gleichberechtigt („Authors contributed equally“, S. 133).
- **Lizenz:** CC BY 4.0 (ACL Anthology, Material ab 2016; FAQ abgerufen 2026-11-16); im PDF „©2021 Association for Computational Linguistics“.
- **Art:** Workshopbeitrag (Kurzbeitrag)
- **Sprache:** Englisch

## Worum es geht

Mehrfach annotierte Datensätze werden meist durch Mehrheitsentscheid, Mittelwert oder Adjudikation auf ein einziges „ground truth“-Label verdichtet (S. 133). Die Autor:innen prüfen an acht binären Aufgaben aus drei Datensätzen (Hassrede, Sentiment, Emotionen), wie gut das Mehrheitslabel die einzelnen Annotator:innen und soziodemografische Gruppen abbildet (S. 133, 134 bis 136). Ergebnis: Bei vielen Aufgaben stimmt ein erheblicher Teil der Annotator:innen kaum mit der Mehrheit überein, und im Sentiment-Datensatz unterscheidet sich diese Übereinstimmung signifikant nach selbstangegebener Herkunftsgruppe (S. 136). Sie empfehlen, Labels pro Annotator:in, soziodemografische Angaben und die Rekrutierung zu veröffentlichen (S. 137).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Aggregation (Mehrheit, Mittelwert, Adjudikation) übergeht bei eher subjektiven Aufgaben die sozial konstruierte Natur der Wahrnehmungen; systematische Abweichungen nach Hintergrund werden verdeckt. | S. 133 Abstract | Position der Autor:innen |
| Bei eher subjektiven Aufgaben gibt es oft keine einzelne richtige Antwort. | S. 133 | referiert (Alm 2011; Aroyo & Welty 2013) |
| Vier Stufen der Veröffentlichung: nur aggregiertes Label; Verteilung über die Labels; Labels pro Annotator:in, anonym; zusätzlich soziodemografische Angaben. | S. 134 | Systematik der Autor:innen |
| Adjudikation durch eine:n „Expert:in“ ist in kleineren Datensätzen üblich, oft durch eine:n der Studienautor:innen selbst; Mehrheit und Adjudikation unterstellen, dass es immer ein einziges richtiges Label gibt. | S. 134 | Beschreibung der Praxis und Kritik der Autor:innen |
| Bei vielen Aufgaben bildet das Mehrheitslabel die Annotator:innen nicht gleichmäßig ab: Für *disgust* liegt κ mit der Mehrheit bei 27 von 82 Annotator:innen unter 0,3, für Sentiment bei rund einem Drittel (über 450). | S. 136, Abb. 1 (S. 135) | eigenes Ergebnis |
| Im Sentiment-Datensatz unterscheidet sich die Übereinstimmung mit der Mehrheit signifikant zwischen Herkunftsgruppen (F(2, 2387) = 3,77, p = 0,02; weiße Annotator:innen 0,42, Schwarze 0,37); nach Geschlecht und politischer Orientierung nicht signifikant. | S. 136 | eigenes Ergebnis |
| Labels pro Annotator:in sind auch für Modellierung nützlich (Verlustfunktionen, Multi-Task, Modelle pro Annotator:in). | S. 136 bis 137 | referiert |
| Empfehlungen: (1) Labels pro Annotator:in veröffentlichen, bevorzugt anonym, und die Aggregation den Nutzer:innen überlassen; (2) soziodemografische Angaben, wo verantwortbar; (3) Rekrutierung, Auswahl und Zuteilung der Annotator:innen dokumentieren (Datasheets, Data Statements). | S. 137 | Empfehlung der Autor:innen |
| „Annotators are not interchangeable“. | S. 137 | Position der Autor:innen |

## Daten, Methode, Zahlen

- **Datensätze (Tab. 1, S. 135, Seitenbild):** Hassrede (Kennedy et al. 2020): 27.665 Instanzen, 18 Annotator:innen, 86.529 Annotationen; Sentiment (Díaz et al. 2018): 14.071 / 1.481 / 59.240; Emotionen (Demszky et al. 2020): 58.011 / 82 / 211.225.
- **Aufgaben:** acht binäre Aufgaben: Hassrede, Sentiment (5-stufig, auf positiv/negativ abgebildet, S. 135 Fn. 1) und sechs Ekman-Emotionen aus den Rohannotationen (S. 135).
- **Maß:** Mehrheitslabel = Label, auf das sich die Hälfte oder mehr der Annotator:innen einer Instanz einigen; dann Cohens κ jeder Person mit dem Mehrheitslabel auf ihren Instanzen (S. 135).
- **Gruppenvergleich:** drei einfaktorielle ANOVAs nach Herkunft, Geschlecht, politischer Orientierung; Gruppen mit weniger als 50 Personen ausgeschlossen (S. 136 Fn. 2); post-hoc Tukey p = 0,03 für weiß gegenüber Schwarz (S. 136).
- Keine Aussage über WSD oder historische Sprachen.

## Wörtliche Stellen

> „Annotators are not interchangeable– that is, they draw from their socially-embedded experiences and knowledge when making annotation judgments.“ (S. 137)

> „We urge dataset developers to release the annotator-level labels, preferably in an anonymous fashion, and leave open the choice of whether and how to utilize or aggregate these labels for the dataset users.“ (S. 137)

## Bezug zur Dissertation

**1. PROTOKOLL §7 Schritt 7 („Alles bleibt erhalten: Labels vor der Adjudikation …“) und §10 („Die Labels vor der Adjudikation werden mitveröffentlicht“): gestützt.** Das entspricht Empfehlung (1) der Arbeit (S. 137) und der dritten Veröffentlichungsstufe (S. 134). Die Arbeit verlangt Labels **pro Annotator:in**, nicht nur die Menge der Labels vor der Adjudikation; das Protokoll sollte deshalb ausdrücklich sagen, dass die Labels mit der Kennung der Person (`julia`, `alan`, §8) veröffentlicht werden. Ob „anonym“ bei zwei namentlich genannten Personen möglich ist, beantwortet die Arbeit nicht; Pseudonyme helfen hier wenig, weil Protokoll und Publikation beide nennen (eigene Folgerung).

**2. PROTOKOLL §7 Schritt 6, „Dritte Person“: gestützt.** Die Arbeit beschreibt Adjudikation durch eine:n Studienautor:in als übliche, aber problematische Form der Aggregation (S. 134). Das deckt die Begründung des Protokolls, Julias Doppelrolle zu prüfen und als Limitation zu nennen.

**3. Datasheet (§10) und DMP: ergänzt.** Empfehlung (3) (S. 137) verlangt Dokumentation von Rekrutierung, Auswahl und Zuteilung. Für den Goldstandard heißt das: wie Alan van Beek gewonnen wurde, welche Vorkenntnisse beide haben (Mittelhochdeutsch, Lexikographie, MHDBDB), und dass die Zuteilung vollständig ist (beide annotieren alle Items, §7 Schritt 4). Soziodemografische Angaben (Empfehlung 2) sind bei zwei Personen weder aussagekräftig noch datenschutzrechtlich unproblematisch; für WSD auf Mittelhochdeutsch ist die fachliche Herkunft das, was der Arbeit am ehesten entspricht. Die Einwilligung (offener Punkt 14) muss die Veröffentlichung der Labels pro Person abdecken.

**4. A31, Weg A (Gold ist relativ zum Inventar; Übereinstimmung misst die Reproduzierbarkeit des Instruments, nicht Wahrheit): Begründung ergänzt.** Die Arbeit sagt für subjektive Aufgaben, dass ein einzelnes richtiges Label weder möglich noch nötig sei (S. 134, nach Alm 2011). WSD nennt sie nicht; ob die Bedeutungszuweisung im Mittelhochdeutschen in diesem Sinn „subjektiv“ ist, bleibt offen. Für die Begründung von Weg A ist Plank (2022, S. 10671), die WSD ausdrücklich nennt, die genauere Quelle.

**5. LITERATUR-IAA.md, Zeile „Labels vor der Aggregation mitveröffentlichen; Abweichung ist oft Signal“ (Prabhakaran et al. 2021 ✔): bestätigt**, mit zwei Präzisierungen: Die Arbeit bezieht sich auf „relatively more subjective tasks“ (S. 133 bis 134), und der Teil „Abweichung ist oft Signal“ steht so bei Plank 2022; Prabhakaran et al. zeigen Abweichung als systematischen Unterschied zwischen Gruppen (S. 136).

## Grenzen und Einwände

- Kurzbeitrag; nur binäre, ausdrücklich subjektive Aufgaben (Hassrede, Sentiment, Emotion) mit Crowd-Annotator:innen in großer Zahl.
- Übereinstimmung jeder Person mit einer Mehrheit, die sie selbst mitbestimmt; bei wenigen Annotator:innen pro Instanz ist das zirkulär. Die Arbeit diskutiert das nicht.
- Gruppenunterschiede nur im Sentiment-Datensatz geprüft, nur eines von drei Merkmalen signifikant, Effekt klein (0,42 gegenüber 0,37).
- Für zwei Annotator:innen wie im Goldstandard gibt es keine Mehrheit; die Analyse der Arbeit ist nicht übertragbar, nur die Empfehlungen.
- Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar: nicht berührt.

## Weiterführend

- Davani, Díaz & Prabhakaran 2022, Dealing with disagreements: Looking beyond the majority vote in subjective annotations, *TACL* 10, S. 92 bis 110 (in der Arbeit S. 136 bis 137 als 2021 zitiert).
- Aroyo & Welty 2013, Crowd truth (S. 133); Alm 2011, Subjective natural language problems, ACL (S. 133 bis 134).
- Gebru et al. 2018, Datasheets for datasets, arXiv-Fassung (S. 137; in `goldstandard/LITERATUR-IAA.md` als Zeitschriftenfassung Gebru et al. 2021, *CACM*); Bender & Friedman 2018, Data statements, *TACL* 6 (S. 137; dort ebenfalls aufgeführt).
- Waseem 2016 (S. 133): systematische Abweichungen zwischen Aktivist:innen und Crowd bei Hassrede.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF.
