# Kapoor & Narayanan 2022/2023: Leakage and the Reproducibility Crisis in ML-based Science (Preprint)

**Datei:** `pdf/Kapoor-Narayanan-2023-Leakage-Preprint.pdf` (nur lokal; 29 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16. Gelesen: Haupttext (PDF-Seiten 1 bis 10), Anhang A, B.1 und C (PDF-Seiten 17, 29); die Fallstudien B.2 bis B.7 (PDF-Seiten 18 bis 28) nur überflogen. Das lokale PDF ist **arXiv 2207.07048v1** vom 14.07.2022, byte-gleich mit dem arXiv-PDF (SHA-256 verglichen am 2026-11-16); arXiv führt nur diese Version. Es enthält keine Markierungen.

**Fassungen:** Zusammengefasst ist der Preprint. Die begutachtete Fassung ist Kapoor & Narayanan 2023 in *Patterns* (siehe Bibliografie) und liegt seit 2026-11-16 als `pdf/Kapoor-Narayanan-2023-Leakage.pdf` vor (CC BY 4.0, aus dem PMC-Open-Access-Bestand). Sie ist **nicht** zusammengefasst; nur die Kernzahlen wurden verglichen (unten). Zitiert werden sollte die Patterns-Fassung; Seitenangaben unten gelten nur für den Preprint.

Seitenzählung: Der Preprint hat keine gedruckten Seitenzahlen; unten steht „PDF-S. n“.

## Bibliografie

- **Vollständig (zitierfähig):** Kapoor, Sayash & Narayanan, Arvind (2023). Leakage and the reproducibility crisis in machine-learning-based science. *Patterns* 4(9), Artikel 100804. Online 4. August 2023, Heft 8. September 2023 (PMC-Seite; Eingang 3. März, Revision 18. Mai, Annahme 5. Juli 2023).
- **DOI/URL:** 10.1016/j.patter.2023.100804 (aufgelöst, Crossref, 2026-11-16; Crossref: Band 4, Heft 9, Artikelnummer 100804, Lizenz der Verlagsfassung CC BY 4.0); PMC10499856.
- **Preprint (dieses PDF):** Kapoor, Sayash & Narayanan, Arvind (2022). Leakage and the Reproducibility Crisis in ML-based Science. arXiv:2207.07048v1, 14. Juli 2022; arXiv-Lizenz „nonexclusive-distrib 1.0“. Die PDF-Metadaten nennen als Vorlage ICML 2022 („Anonymous Submission“); eine Annahme dort ist nicht belegt.
- **Art:** Preprint (Verlagsfassung: begutachteter Zeitschriftenartikel)
- **Sprache:** Englisch

## Worum es geht

Die Arbeit untersucht Reproduzierbarkeitsprobleme in „ML-based science“, also Forschung, die eine wissenschaftliche Aussage mit der Leistung eines ML-Modells belegt (PDF-S. 1). Aus 20 Übersichtsarbeiten in 17 Fächern mit zusammen 329 betroffenen Arbeiten leitet sie eine Taxonomie von acht Arten des Datenlecks (data leakage) ab (PDF-S. 1 bis 2, 5 bis 6), schlägt „model info sheets“ vor, mit denen Forschende begründen sollen, dass kein Leck vorliegt (PDF-S. 6 bis 8), und zeigt in einer Fallstudie zur Bürgerkriegsprognose, dass alle vier Arbeiten, die komplexe ML-Modelle der logistischen Regression überlegen fanden, nach Korrektur der Lecks diesen Vorsprung verlieren (PDF-S. 3, 8).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Datenleck: eine Scheinbeziehung zwischen unabhängigen Variablen und Zielvariable, die aus Datenerhebung, Stichprobe oder Vorverarbeitung entsteht und in der Verteilung, über die Aussagen gemacht werden, fehlt; Folge ist meist überhöhte Leistung. | PDF-S. 4, Abschnitt 2.1 | Definition |
| 20 Übersichtsarbeiten aus 17 Fächern, zusammen 329 betroffene Arbeiten; in jedem Fall tritt ein Datenleck auf. Das ist eine Untergrenze, keine systematische Metastudie. | PDF-S. 1 bis 2, 4, Tab. 1 | eigene Zusammenstellung aus referierten Arbeiten |
| Anders als bei Modellwettbewerben, wo eine unabhängige Stelle die Testdaten verwahrt, hat in ML-basierter Wissenschaft die forschende Person beim Modellieren Zugriff auf den ganzen Datensatz; daraus entstehen Lecks. | PDF-S. 4, Abschnitt 2.2 | Argument |
| **[L1] Keine saubere Trennung von Training und Test:** L1.1 kein Testset; L1.2 Vorverarbeitung (Imputation, Über- oder Unterabtastung) auf Training und Test zusammen; L1.3 Merkmalsauswahl auf Training und Test; L1.4 Duplikate, die in Training und Test landen. | PDF-S. 5 | eigene Taxonomie |
| **[L2] Unzulässige Merkmale:** z. B. ein Merkmal, das ein Stellvertreter für die Zielvariable ist (Medikament gegen Bluthochdruck zur Vorhersage von Bluthochdruck). Ob ein Merkmal zulässig ist, verlangt Fachwissen und ist zu begründen. | PDF-S. 5 | eigene Taxonomie, Beispiel referiert |
| **[L3] Testset nicht aus der Verteilung des wissenschaftlichen Interesses:** L3.1 zeitliches Leck; L3.2 Abhängigkeit zwischen Trainings- und Testbeispielen (dieselben Personen oder Einheiten), Abhilfe z. B. Block-Kreuzvalidierung; L3.3 Stichprobenverzerrung im Test, z. B. Ausschluss von Grenzfällen, der zu optimistischen Ergebnissen führt. | PDF-S. 5 bis 6 | eigene Taxonomie, Beispiele referiert |
| Weitere Probleme aus der Übersicht: fehlende rechnerische Reproduzierbarkeit (5 Arbeiten), Datenqualität (10), Wahl der Metrik, z. B. Genauigkeit bei starkem Klassenungleichgewicht (4), Probleme trotz Standarddatensätzen (7). | PDF-S. 6, Abschnitt 2.5 | eigene Auszählung |
| Model info sheets verlangen drei Begründungen: saubere Trennung von Training und Test in allen Schritten (L1), Zulässigkeit jedes Merkmals (L2), Testset aus der Verteilung, über die Aussagen gemacht werden (L3). Die meisten Arbeiten liefern keine davon. | PDF-S. 7, Abschnitt 3.2 | Vorschlag |
| Grenzen der model info sheets: ohne rechnerische Reproduzierbarkeit nicht überprüfbar; falsche Angaben können falsche Sicherheit geben; ML-Fachwissen nötig. | PDF-S. 7 bis 8, Abschnitt 3.4 | Selbsteinschätzung |
| Fallstudie: Von 124 gefundenen Arbeiten blieben 12 mit Train-Test-Evaluation und vollständigem Code und Daten; Fehler in genau den 4, die eine Überlegenheit komplexer Modelle behaupteten. Nach Korrektur sind sie nicht wesentlich besser als logistische Regression; bei Wang (2019) sinkt der AUC-Abstand von 0,14 auf 0,01. | PDF-S. 3, 8, Abb. 1; Auswahl PDF-S. 17 | eigenes Ergebnis |
| 9 der 12 Arbeiten berichten keine Signifikanztests oder Unsicherheiten; Beispiel Blair & Sambanis (2020): AUC 0,85, Bootstrap-Konfidenzintervall 0,66 bis 0,95, Vorsprung nicht signifikant. | PDF-S. 8 bis 9 | eigenes Ergebnis |
| Fünf Diagnosen mit Empfehlungen, u. a. Grenzen der Vorhersagbarkeit kennen, Ergebnisse vorläufig behandeln, Common Task Framework mit geheimem Holdout nutzen, rechnerische Reproduzierbarkeit sichern. | PDF-S. 9 bis 10, Abschnitt 5 | Empfehlungen |
| Anhang C ordnet jedem Lecktyp Fragen der model info sheet zu (z. B. L1.4 Duplikate: Q10; L3.2 Abhängigkeiten: Q11; L3.3 Stichprobe: Q18 bis 19). | PDF-S. 29 | Vorschlag |

## Daten, Methode, Zahlen

- Übersicht: 20 Übersichtsarbeiten, 17 Fächer, 329 betroffene Arbeiten (PDF-S. 2, Tab. 1).
- Fallstudie Bürgerkriegsprognose: Suche 1.1.2016 bis 14.5.2021, 124 Arbeiten, davon 15 mit Train-Test-Evaluation, davon 12 mit vollständigem Code und Daten (PDF-S. 17); der Haupttext spricht verkürzt von „the 12 papers“ (PDF-S. 8).
- Code der Fallstudie: CodeOcean, DOI 10.24433/CO.4899453.v1 (PDF-S. 10); Vorlage der model info sheet auf https://reproducible.cs.princeton.edu (PDF-S. 6, Fn. 2).

**Abweichungen der Patterns-Fassung (verglichen am 2026-11-16, nur diese Zahlen):** Die Verlagsfassung nennt **22** Übersichtsarbeiten und **294** betroffene Arbeiten in 17 Fächern (Patterns-PDF S. 2 und 3, Highlights auf dem Deckblatt), nicht 20 und 329. Die acht Lecktypen bleiben (Patterns S. 2, Typ L1.4 auf S. 4). Für Zitate die Zahlen der Patterns-Fassung verwenden. Weitere Unterschiede sind nicht geprüft [an der Verlagsfassung zu prüfen].

## Wörtliche Stellen

> „Data leakage is a spurious relationship between the independent variables and the target variable that arises as an artifact of the data collection, sampling, or pre-processing strategy.“ (PDF-S. 4)

> „Leakage often occurs due to the researcher having access to the entire dataset during the modeling process.“ (PDF-S. 4)

> „excluding them the evaluation set is likely to lead to overoptimistic results“ (PDF-S. 6, zum Ausschluss von Grenzfällen; Grammatik so im Original)

Wörtliche Zitate vor Verwendung an der Patterns-Fassung prüfen; der Wortlaut kann abweichen.

## Bezug zur Dissertation

Das Werk behandelt klassisches ML mit eigenem Training, nicht vortrainierte LLMs; Kontamination durch Vortraining (Sainz et al. 2023; Jacovi et al. 2023) kommt in dieser Taxonomie nicht vor. Übertragbar sind die Lecktypen auf alles, was im Design gelernt oder gewählt wird: MFS-Baseline, Prompt-Wahl, Few-shot-Beispiele.

**1. L1 (saubere Trennung) und PROTOKOLL §9.2 (MFS aus Silber ohne Stichproben-Tokens), A17 (Prompt-Wahl nur am Pilot-Pool, Few-shot aus Silber ohne Stichproben-Tokens).** Gestützt: Das sind genau die Trennungen, die L1 verlangt (PDF-S. 5, 7). Die Fallstudie zeigt, wie stark ein Vergleich „neues Modell gegen alte Baseline“ kippt, wenn die Trennung fehlt (PDF-S. 3, 8). Ein Hinweis auf Kapoor & Narayanan wäre eine Begründung für A17, die bisher nur auf Meconi et al. 2025 steht.

**2. L1.4 (Duplikate).** Neu für das Protokoll: Die Obergrenze pro Text und der Ausschluss der Pilot-Lemmata (A30) verhindern nicht, dass derselbe Wortlaut in zwei Texten des Korpus steht (Parallelfassungen, Formelverse). Liegt ein Few-shot-Beispiel aus Silber (A17) oder ein Pilot-Item in einer Parallelstelle zu einem Item der Hauptstichprobe, ist das ein Duplikat im Sinn von L1.4. Vorschlag: vor Freeze 2 prüfen, ob es im Korpus Parallelfassungen gibt, und Few-shot-Beispiele mit gleichem Kontext wie Stichproben-Items ausschließen. Ob das Korpus solche Fälle enthält, ist hier nicht geprüft.

**3. L2 (unzulässige Merkmale) und `knowledge/data.md` B1 (Typliste als Leckgefahr).** Gestützt: Die Typliste an `<sense>` ist ein Stellvertreter für die Zielvariable im Sinn von L2 (PDF-S. 5); sie aus Prompt und Karten fernzuhalten, ist die geforderte Begründung „each feature is legitimate“ (PDF-S. 7). Dasselbe gilt für Silber-`@ana` im Prompt.

**4. L3.2 (Abhängigkeit) und PROTOKOLL §9.1 Punkt 5 (Bootstrap nach Text), §4.4 (Obergrenze pro Text).** Gestützt: Abhängigkeit zwischen Beispielen derselben Einheit ist zu berücksichtigen, Block-Verfahren sind die genannte Abhilfe (PDF-S. 5 bis 6). Der Cluster-Bootstrap nach Text entspricht dem.

**5. L3.3 (Stichprobenverzerrung) und PROTOKOLL §9.2 (Items mit `KEINE_PASST`, `KONTEXT_UNZUREICHEND`, `TEXT_DEFEKT` nicht in der Genauigkeit).** Das Beispiel auf PDF-S. 6 (Grenzfälle ausgeschlossen, Ergebnis zu optimistisch) betrifft genau diese Regel: Wenn die schwierigsten Belege als Ausweichlabel aus der Genauigkeit fallen, ist die Genauigkeit für die Grundgesamtheit optimistisch. Das Protokoll berichtet das LLM-Verhalten auf diesen Items gesondert; zusätzlich sollte der Anteil der ausgeschlossenen Items neben jeder Genauigkeit stehen und die Aussage auf „Items mit passendem Sense“ begrenzt werden. Gleiches gilt für Ausschluss 5 (Verschmelzungen, A21) und die Ausschlüsse in §3: Die Aussage gilt für die Grundgesamtheit nach Ausschlüssen.

**6. Signifikanz und Unsicherheit (PDF-S. 8 bis 9) und PROTOKOLL §9.1 Punkt 5, §9.2 (McNemar).** Gestützt: Das Protokoll sieht Test und Intervalle vor.

**7. Model info sheet als Ergänzung zum Datasheet (DMP §2).** Vorschlag: Für den Artikel die drei Begründungen L1 bis L3 (PDF-S. 7) ausdrücklich ausformulieren; vieles steht schon im Protokoll (Abschnitte 3, 4.4, 9.2, A17).

**8. PROTOKOLL §10 (Kontamination).** Das Werk ist für Kontamination durch Vortraining **nicht** die richtige Quelle; es behandelt nur Lecks im eigenen Arbeitsablauf. Für §10 bleiben Sainz et al. und Jacovi et al. maßgeblich.

## Grenzen und Einwände

- Preprint; die begutachtete Fassung hat andere Zahlen (22 statt 20 Übersichtsarbeiten, 294 statt 329 Arbeiten) und ist nicht zusammengefasst.
- Die Übersicht ist ausdrücklich keine systematische Metastudie, die Zahlen sind Untergrenzen (PDF-S. 4).
- Gegenstand ist Forschung mit selbst trainierten Modellen auf tabellarischen oder Bilddaten; vortrainierte LLMs und Prompting kommen nicht vor.
- Keine Sprachdaten, keine Annotation, keine Inter-Annotator-Fragen.

## Weiterführend

- Kaufman et al. 2012, Leakage in data mining (PDF-S. 1, 4): grundlegende Arbeit zu Lecks.
- Mitchell et al. 2019, Model cards; Gebru et al. 2021, Datasheets (PDF-S. 6 bis 7): Dokumentationsformate.
- Roberts et al. 2017; Valavi et al. 2021 (PDF-S. 6): Block-Kreuzvalidierung bei abhängigen Daten.
- Salganik et al. 2020 (PDF-S. 8 bis 9): Grenzen der Vorhersagbarkeit.
- Patterns-Fassung, `pdf/Kapoor-Narayanan-2023-Leakage.pdf`: noch zusammenzufassen.

## Julias Notizen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem arXiv-PDF; `markierungen.py` legt keine Datei an.
