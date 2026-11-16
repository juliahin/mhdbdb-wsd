# Plank 2022: The „Problem“ of Human Label Variation

**Datei:** `pdf/Plank-2022-Human-Label-Variation.pdf` (nur lokal; 12 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen (Haupttext S. 10671 bis 10676, Literatur, Anhang Tab. 1 S. 10682). Abb. 1 bis 3 (S. 10671, 10672, 10674) nur über Bildunterschrift und Fließtext; Abb. 3 enthält Zahlen pro Jahr, die hier nicht übernommen sind. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology 2022.emnlp-main.731 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: gedruckte Seite = PDF-Seite + 10670 (PDF 1 = S. 10671, PDF 12 = S. 10682). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Plank, Barbara (2022). The „Problem“ of Human Label Variation: On Ground Truth in Data, Modeling and Evaluation. In: Yoav Goldberg, Zornitsa Kozareva & Yue Zhang (Hg.), *Proceedings of the 2022 Conference on Empirical Methods in Natural Language Processing*. Abu Dhabi, Vereinigte Arabische Emirate: Association for Computational Linguistics, S. 10671 bis 10682.
- **DOI/URL:** 10.18653/v1/2022.emnlp-main.731 (aufgelöst, Crossref); https://aclanthology.org/2022.emnlp-main.731/ (Herausgeber:innen und Monat Dezember nach dem BibTeX der Anthology, abgerufen 2026-11-16; Tagung laut PDF 7. bis 11.12.2022)
- **Lizenz:** CC BY 4.0 (ACL Anthology, Material ab 2016; FAQ abgerufen 2026-11-16); im PDF „©2022 Association for Computational Linguistics“.
- **Art:** Konferenzbeitrag, ausdrücklich Positionspapier (S. 10671)
- **Sprache:** Englisch

## Worum es geht

Das Positionspapier argumentiert, dass die übliche Annahme eines einzigen Goldlabels pro Instanz bei Sprache oft nicht trägt, weil Annotator:innen aus guten Gründen verschieden urteilen (S. 10671). Plank schlägt dafür den Oberbegriff „human label variation“ (HLV) vor, grenzt ihn von Fehlern ab und zeigt, dass HLV alle Stufen der Pipeline betrifft: Daten, Modellierung, Evaluation (S. 10672 bis 10675). Für jede Stufe nennt sie offene Probleme und Vorschläge, darunter die Veröffentlichung nicht aggregierter Labels und reichhaltiger Metadaten (S. 10673) sowie Evaluation jenseits der Genauigkeit gegen harte Labels (S. 10675). Der Anhang listet öffentlich verfügbare Datensätze mit mehreren Labels pro Instanz (S. 10682).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Eine Ground Truth (Mehrheit, Modus) ist sinnvoll, wenn Menschen sich bei der Frage weitgehend einig sind; bei Sprache oft nicht, als Beispiele u. a. Fragen, die einen Wortsinn bestimmen. | S. 10671 | Position der Autorin |
| Unauflösbare Variation zwischen Annotationen ist plausibel und häufig. | S. 10671 | referiert (u. a. Plank et al. 2014b; Aroyo & Welty 2015; Pavlick & Kwiatkowski 2019; Uma et al. 2021b) |
| Definition: HLV ist plausible Variation in der Annotation; „Variation“ statt „disagreement“, weil „disagreement“ unterstelle, dass nicht alle Sichten zugleich gelten können. Fehler (z. B. Aufmerksamkeitsfehler) sind davon getrennt. | S. 10672 | Begriffsvorschlag der Autorin |
| HLV setzt voraus, dass Menschen ihr bestes Urteil abgeben; Variation entsteht durch Mehrdeutigkeit der Instanz, Unsicherheit der Annotator:in, echte Meinungsverschiedenheit oder weil mehrere Optionen richtig sind. Aggregation verdeckt das. | S. 10672 | Position der Autorin |
| Die klassische Definition von Datenreliabilität setzt einen Standard voraus; bei unauflösbarer Abweichung sei zu fragen: welcher Standard? | S. 10672 | Position der Autorin (mit Verweis auf Krippendorff 2018) |
| In mindestens 20 % ihrer Daten fanden Pavlick & Kwiatkowski plausible Variation. | S. 10672 | referiert |
| Vorschläge für Daten: nicht aggregierte Labels pro Annotator:in veröffentlichen, auch nur für eine kleine Teilmenge; Erstellung dokumentieren; möglichst viele Metadaten pro Instanz (Quelle, Zeit, Annotator-IDs, Bearbeitungszeit); Unsicherheitsmarkierungen und Freitext-Begründungen haben sich bewährt. | S. 10673 | Vorschlag der Autorin; Beispiele referiert (Bassignana & Plank 2022) |
| Mehrfachannotation verlangt Forschung zur Datenqualität und neue Übereinstimmungsmaße, etwa für Mehrfachlabels. | S. 10673 | Position der Autorin |
| Modellierung: zwei Lager, Variation auflösen (Aggregation durch Mehrheit oder probabilistische Modelle, Filtern von Instanzen mit geringer Übereinstimmung) oder Variation nutzen (direkt aus nicht aggregierten Labels lernen, Gold mit HLV anreichern). Filtern kann die Leistung verschlechtern und verschwendet Daten. | S. 10673 | Überblick, referiert (u. a. Dawid & Skene 1979; Paun et al. 2022; Jamison & Gurevych 2015) |
| Fehler von Signal zu trennen ist eine offene Aufgabe; es fehle Theorie dazu, was ein Fehler und was ein schwieriger Fall ist. | S. 10674 | Position der Autorin |
| Evaluation mit Genauigkeit gegen ein einzelnes Gold ist bei vielen Aufgaben „severely flawed“; vorgeschlagen sind weiche Maße (Kreuzentropie, Entropiekorrelation, KL- oder Jensen-Shannon-Divergenz), Evaluation gegen einzelne Annotator:innen und Aufteilung der Testdaten nach Übereinstimmungsgrad oder Unsicherheitsmarkierungen. | S. 10675 | Position der Autorin; Verfahren referiert |
| Fazit: HLV ist eine Chance, kein Problem. | S. 10675 | Position der Autorin |

## Daten, Methode, Zahlen

- Keine eigene Empirie; Literaturübersicht und Position.
- **Anhang Tab. 1 (S. 10682):** Liste öffentlicher Datensätze mit mehreren Labels pro Instanz, darunter für WSD Passonneau et al. 2010 (MASC, anc.org), Supersense-Tagging (Martínez Alonso et al. 2016), Dependenzparsing auf WSJ-23 mit vier Annotator:innen (Berzak et al. 2016) und Snow et al. 2008 (u. a. WSD). Das Repositorium dazu: https://github.com/mainlp/awesome-human-label-variation (S. 10675).
- Abb. 3 (S. 10674) zählt Ressourcenartikel mit HLV pro Jahr [Zahlen am PDF zu prüfen].

## Wörtliche Stellen

> „The assumption of a ground truth […] makes sense when humans involved in labeling highly agree on the answer to the questions […]. However, this assumption often does not make sense […]. For example, on questions determining a word sense […]“ (S. 10671)

> „We define human label variation (HLV) as plausible variation in annotation […]“ (S. 10672)

> „[…] we urge the community to release annotator-level (un-aggregated) labels […] even if only for a small subset of the data […]“ (S. 10673)

Hinweis: Im Original stehen an den mit […] gekürzten Stellen Gedankenstriche (S. 10671, nach „sense“; S. 10673, nach „labels“).

## Bezug zur Dissertation

**1. PROTOKOLL §7 Schritt 7 und §10 (Labels vor der Adjudikation, Sicherheitsangaben, Ereignisprotokolle erhalten und mitveröffentlichen): gestützt, und genauer als bisher zitiert.** Plank nennt nicht nur nicht aggregierte Labels, sondern ausdrücklich Metadaten pro Instanz: Annotator-IDs, Bearbeitungszeit, Unsicherheitsmarkierungen, Freitext-Begründungen (S. 10673). Das deckt die Sicherheitsangabe (§6), das Kommentarfeld, die Verweildauer im Ereignisprotokoll (§8) und die Lesart aus A31 als Begründungstext. **Vorschlag:** Die Lesarten aus dem Pilot (A31) als Teil der Rohdaten führen und mitveröffentlichen, mit Verweis auf Plank (2022, S. 10673).

**2. PROTOKOLL §2 („Gold“) und A31, Weg A (Gold ist relativ zum Inventar; Übereinstimmung misst die Reproduzierbarkeit des Instruments, nicht Wahrheit): gestützt.** Plank nennt WSD als Fall, in dem die Annahme einer Ground Truth oft nicht trägt (S. 10671), und fragt bei unauflösbarer Abweichung „welcher Standard?“ (S. 10672). Das ist eine zitierfähige Grundlage für die Formulierung in A31.

**3. PROTOKOLL §6, Status `MEHRERE`: gestützt.** „Multiple options being plausible“ ist eine der drei Quellen von HLV (S. 10672 bis 10673), und Aggregation „by definition allows only one … label“ (S. 10673). Dass `MEHRERE` ein eigener Status ist und als Mehrfachlabel ins Gold darf (§7 Schritt 6), entspricht dem Lager „Gold mit HLV anreichern“ (S. 10673). Planks Hinweis auf neue Übereinstimmungsmaße für Mehrfachlabels (S. 10673) passt zu α mit MASI (§9.1).

**4. PROTOKOLL §7 Schritt 6, Ursachencodes (Richtlinienlücke, Versehen, echte Textambiguität, Inventarlücke, Editions- oder Normalisierungseffekt): gestützt.** Die Trennung „Versehen“ gegen „echte Textambiguität“ ist genau die Trennung von Fehler und HLV (S. 10672), für die Plank eine Theorie vermisst (S. 10674). Die Ursachencodes sind damit ein Beitrag zu einer offenen Frage, nicht nur Buchhaltung.

**5. PROTOKOLL §9.2 (LLM gegen Gold, Genauigkeit, McNemar): Einwand und Ergänzung.** Plank hält Genauigkeit gegen ein hartes Gold bei vielen Aufgaben für unzureichend (S. 10675). Das Protokoll hat drei Antworten darauf schon angelegt: den Vergleich des LLM mit jeder der beiden Personen (Alternative Annotator Test; Plank nennt Evaluation gegen einzelne Annotator:innen, S. 10675), die Aufschlüsselung nach Sicherheit (§9.1 Punkt 6; Plank nennt Aufteilung nach Unsicherheitsmarkierungen, S. 10675) und die Dice-Teilwertung bei `MEHRERE` (A14). **Vorschlag:** Die Auswertung zusätzlich getrennt für Items berichten, bei denen die beiden Personen vor der Adjudikation übereinstimmten, und für solche, bei denen sie abwichen (Aufteilung nach Übereinstimmungsgrad, S. 10675, nach Leonardelli et al. 2021). Das wäre eine vorab festzulegende Sekundärauswertung für Freeze 2.

**6. PROTOKOLL §7 Schritt 2 (Pilot, Schwelle α ≥ 0,80, A32): Spannung, kein Widerspruch.** Planks Haltung, Variation nicht zu minimieren, steht quer zum Nachschärfen der Richtlinien bis zu einer Schwelle. Das Protokoll löst das bereits über A31 (Weg A): Gemessen wird die Reproduzierbarkeit eines Instruments, und echte Mehrdeutigkeit hat mit `MEHRERE` und `KONTEXT_UNZUREICHEND` eigene Status, statt durch Richtlinien wegdefiniert zu werden. Das sollte im Artikel so begründet werden.

**7. LITERATUR-IAA.md, Zeile „Labels vor der Aggregation mitveröffentlichen; Abweichung ist oft Signal“ (Plank 2022 ✔): bestätigt.** „Signal“ ist sinngemäß belegt (HLV „provides rich information that should not be discarded“, S. 10671; „errors from signal“, S. 10674).

## Grenzen und Einwände

- Positionspapier ohne eigene Daten; die Belege für die Häufigkeit von HLV stammen aus anderen Arbeiten, überwiegend zu subjektiven Aufgaben, NLI und Bildklassifikation.
- Für WSD nennt Plank nur Beispiele und einen Datensatz (Passonneau et al. 2010), keine eigenen Zahlen.
- Wie Fehler von plausibler Variation zu trennen sind, bleibt nach eigener Aussage offen (S. 10674); für die Adjudikation im Goldstandard gibt das Papier also kein Verfahren.
- Die vorgeschlagenen weichen Evaluationsmaße setzen eine Labelverteilung aus vielen Annotator:innen voraus; mit zwei Personen pro Item ist eine solche Verteilung sehr grob.
- Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar: nicht berührt.

## Weiterführend

- Uma, Fornaciari, Hovy, Paun, Plank & Poesio 2021b, Learning from disagreement: a survey, JAIR (S. 10671 und öfter): Übersicht.
- Pavlick & Kwiatkowski 2019, Inherent disagreements in human textual inferences, *TACL* (S. 10671 bis 10672).
- Jiang & de Marneffe 2022, Taxonomie der Abweichungsquellen in NLI (S. 10675): Vorbild für Ursachencodes.
- Bassignana & Plank 2022, CrossRE (S. 10673, 10675): Unsicherheitsmarkierungen und Begründungen pro Instanz.
- Leonardelli et al. 2021 (S. 10675): Evaluation nach Übereinstimmungsgrad.
- Basile et al. 2021b, We need to consider disagreement in evaluation (S. 10673, 10675).
- Marchal et al. 2022 (S. 10673): Übereinstimmungsmaße für Mehrfachlabels.
- Paun et al. 2022 (S. 10673): Übersicht zu probabilistischer Aggregation.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF.
