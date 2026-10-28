# Semmelrock et al. 2025: Reproducibility in machine-learning-based research

**Datei:** `pdf/Semmelrock-etal-2025-Reproducibility-ML.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, Volltext vollständig gelesen (Textebene; Abb. 1 und 2 als Bild); Jahr, Band, Heft, Artikelnummer und DOI über Crossref und arXiv geprüft.

**Seitenzählung:** Das PDF ist die Verlagsfassung, Seiten „1 of 19“ bis „19 of 19“. Gedruckte Seite = PDF-Seite. Die Seitenmarken in `md/` verrutschen bei diesem zweispaltigen Satz um bis zu eine Spalte; die Seitenangaben hier sind an der Textebene geprüft.

## Bibliografie

- **Vollständig:** Semmelrock, Harald, Tony Ross-Hellauer, Simone Kopeinik, Dieter Theiler, Armin Haberl, Stefan Thalmann & Dominik Kowald, 2025. Reproducibility in machine-learning-based research: Overview, barriers, and drivers. *AI Magazine* 46(2), e70002, 19 Seiten.
- **DOI/URL:** https://doi.org/10.1002/aaai.70002 (DOI leitet auf die Wiley-Seite weiter; diese lieferte am 2026-10-28 HTTP 403). Crossref-Eintrag am 2026-10-28 gelesen: Band 46, Heft 2, Artikelnummer e70002, online 2025-04-14, Druckausgabe 2025-06, CC BY 4.0, keine Korrektur oder Rücknahme verzeichnet. ✔ Im PDF: „Received: 2 July 2024, Revised: 19 December 2024, Accepted: 25 February 2025“ (S. 1), „AI Magazine. 2025;46:e70002“ (S. 1), Zitiervorschlag „AI Magazine 46: e70002“ (S. 19). Das Heft 2 steht im Download-Vermerk am Rand („23719621, 2025, 2“).
- **Zum Jahr 2024 in Julias Literaturliste:** Es gibt einen Preprint gleichen Inhalts, arXiv:2406.14325 („Reproducibility in Machine Learning-based Research: Overview, Barriers and Drivers“), v1 vom 20. Juni 2024, v2 vom 2. Juli 2024, v3 vom 26. Februar 2025 mit dem Kommentar „Accepted for publication in the AI Magazine“ (arXiv-Seite am 2026-10-28 gelesen). ✔ Das Jahr 2024 gehört also zum Preprint; zitiert wird die begutachtete Fassung von 2025. Ob sich v1 inhaltlich von der Zeitschriftenfassung unterscheidet, wurde nicht geprüft. Ein älterer, kürzerer Preprint des Erstautors (arXiv:2307.10320, 2023, „Reproducibility in Machine Learning-Driven Research“) wird im Artikel als „Semmelrock et al. 2023“ zitiert (S. 2); bibliografisch nur über eine Suchergebnisseite bestätigt. ○
- **Art:** begutachteter Artikel (Überblicksartikel, Kategorie „Article“).
- **Sprache:** Englisch

## Worum es geht

Der Artikel gibt einen Überblick über Hindernisse („barriers“) und Hebel („drivers“) der Reproduzierbarkeit in ML-gestützter Forschung, mit Beispielen aus Informatik und Biomedizin (S. 1 bis 2). Er übernimmt Gundersens (2021) vier Stufen der Methodenreproduzierbarkeit, R1 Beschreibung, R2 Code, R3 Daten, R4 Experiment, und Gundersens Unterscheidung von Ergebnis-, Analyse- und Interpretationsreproduzierbarkeit (S. 2 bis 3). Neun Hindernisse werden den vier Stufen zugeordnet (S. 3 bis 7), neun Hebel in drei Gruppen beschrieben (technisch, prozedural, Bewusstsein und Ausbildung; S. 7 bis 11) und in einer Matrix aufeinander abgebildet (Abb. 2, S. 12); Tab. 1 (S. 14) nennt Stärken und Grenzen jedes Hebels. Die Autor:innen sehen die Hauptursache in der Forschungskultur und setzen auf Ausbildung und Bewusstsein (S. 13 bis 14). Eigene empirische Daten enthält der Artikel nicht.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Vertrauenswürdige KI setzt Reproduzierbarkeit voraus. | S. 1, Einleitung | referiert (Kowald et al. 2024) |
| ML bringt eigene Hindernisse: Empfindlichkeit gegenüber Trainingsbedingungen, Zufallsquellen, inhärenter Nichtdeterminismus, Rechenkosten, AutoML; dazu Datenlecks, Bias, selektives Berichten und Publikationskultur. | S. 2 | Synthese aus der Literatur |
| Vier Stufen der Methodenreproduzierbarkeit (R1 bis R4); je mehr geteilt wird, desto höher die Reproduzierbarkeit, aber desto geringer der Nachweis von Generalisierbarkeit. Dasselbe auf denselben Daten zu wiederholen kann dieselben Fehler reproduzieren. | S. 3, Abb. 1 | referiert (Gundersen 2021), erläutert |
| R1, Berichtsqualität: Modell oder Training unterspezifiziert, Maße nicht definiert, selektives Berichten (nur der beste Lauf statt Mittelwert und Varianz). | S. 3 bis 4 | referiert (Pineau et al. 2021; Belz et al. 2021) |
| R1, „Spin“: In ML-gestützter biomedizinischer Forschung wird die Empfehlung eines Modells für klinischen Einsatz oder eine andere Population nur in etwa 15 % der Fälle validiert. | S. 4 | referiert (Navarro et al. 2023) |
| R2: Nur ein Drittel der Forschenden teilt Daten, noch weniger den Code. Code-Weitergabe braucht sieben Angaben (Hypothese, Vorhersagemethode, Quellcode, Hardware, Software-Abhängigkeiten, Versuchsaufbau, Experimentcode). | S. 4 bis 5 | referiert (Hutson 2018; Gundersen & Kjensmo 2018) |
| R3: In der Radiomik teilten nur 16 von 257 ML-Publikationen Daten oder nutzten öffentliche. Daten sollen mit Splits, Herkunft und Vorverarbeitung geteilt werden. | S. 5 | referiert (D'Antonoli et al. 2024; Gundersen & Kjensmo 2018) |
| Datenlecks in drei Typen: kein sauberer Train/Test-Split, nicht legitime Merkmale, Testmenge nicht aus der Zielverteilung (zeitliches Leck, abhängige Stichproben, selektiv gewählte Testmenge). | S. 5 | referiert (Kapoor & Narayanan 2023) |
| Acht Bias-Arten bei der Datenaufbereitung, u. a. Selektions-, Ausschluss- und „recall bias“ (ähnliche Fälle verschieden labeln). | S. 5 bis 6 | referiert (Rouzrokh et al. 2022) |
| R4: Inhärenter Nichtdeterminismus, Umgebungsunterschiede (Hardware, Framework, Version) und begrenzte Rechenressourcen verhindern Reproduktion auch bei geteiltem Code und Daten. Ein LLM nachzutrainieren kostet geschätzt 1 bis 3,2 Mio. USD. | S. 6 bis 7 | referiert (u. a. Beam, Manrai & Ghassemi 2020) |
| Zufallsquellen steuern: feste Seeds verwenden und veröffentlichen; zusätzlich mit mehreren Seeds evaluieren und die Varianz berichten. | S. 8 | Empfehlung, gestützt auf Raste et al. 2022 u. a. |
| Werkzeuge zur Reproduzierbarkeit stützen sich auf fünf Säulen: Code-Versionierung, Datenzugang, Daten-Versionierung, Experiment-Logging, Pipeline-Bau. | S. 9 | referiert (Quaranta, Calefato & Lanubile 2022; 19 Werkzeuge untersucht) |
| Data Cards und Model Cards standardisieren die Dokumentation; Leistung als Aggregat über mehrere Läufe mit verschiedenen Seeds berichten, möglichst auf mehreren Datensätzen. | S. 9 bis 10 | Empfehlung, referiert (Pushkarna et al. 2022; Mitchell et al. 2019; Colas et al. 2018) |
| Für Sprachmodelle gibt es Evaluationsrahmen (HELM, lm-eval), aber die meisten großen Modelle sind nicht reproduzierbar; ein Offenheits-Tracker findet, dass selbst „offene“ Projekte undokumentierte Daten erben und sorgfältige Dokumentation „exceedingly rare“ ist. | S. 10 | referiert (Liang et al. 2022; Biderman et al. 2024; Liesenfeld, Lopez & Dingemanse 2023) |
| Verpflichtende Checklisten erhöhten in einer Übersicht über 943 Artikel die Angabe der für Reproduktion nötigen Methodeninformation um 65 %. | S. 10 | referiert (Han et al. 2017) |
| Model Info Sheets gegen Datenlecks: In 12 untersuchten Arbeiten war ein Drittel von Lecks betroffen, die sich mit Info Sheets hätten vermeiden lassen. | S. 10 bis 11 | referiert (Kapoor & Narayanan 2023) |
| Präregistrierung trennt Forschungsplan und Ergebnis und verringert Spin, HARKing und p-Hacking; in der Matrix ist sie der wirksamste Hebel gegen Spin. | S. 11; S. 12 | Empfehlung, referiert (Nosek et al. 2019 u. a.) |
| Matrix: oft mehrere Hebel pro Hindernis; es braucht kontextabhängige statt Einheitslösungen. Bewusstsein und Ausbildung gelten für alle Hindernisse. | S. 12, Abb. 2 | eigene Synthese |
| Feste Seeds liefern nur Punktschätzungen der Leistung. | S. 14, Tab. 1 | eigene Einschätzung |
| Hauptursache ist die Forschungskultur (fehlende Anreize, Finanzierung, Ausbildung); Zukunftsfrage ist u. a. die Rolle von Foundation Models. | S. 13 bis 14 | eigene Schlussfolgerung |

## Daten, Methode, Zahlen

- **Art der Arbeit:** narrativer Überblick ohne beschriebene Suchstrategie oder Einschlusskriterien; keine eigenen Daten. Alle Zahlen im Artikel sind aus anderen Studien übernommen (S. 4, 5, 7, 9, 10, 11).
- **Raster:** 4 Reproduzierbarkeitsstufen (S. 3), 9 Hindernisse (S. 3), 9 Hebel in 3 Gruppen (S. 7; Abb. 2, S. 12).
- **Abb. 2 (S. 12, am Bild geprüft):** Berichtsqualität → Richtlinien/Checklisten; Spin und Publikationsbias → Bewusstsein/Publikationspolitik; begrenzter Code-Zugang → Hosting, Virtualisierung, Werkzeuge; begrenzter Datenzugang → datenschutzwahrende Verfahren, Werkzeuge, standardisierte Datensätze, Richtlinien; Datenleck → standardisierte Datensätze und Evaluation, Model Info Sheets/Model Cards; Bias → standardisierte Datensätze, Richtlinien; Nichtdeterminismus → Zufallsquellen steuern; Umgebungsunterschiede → Hosting, Virtualisierung; begrenzte Rechenressourcen → Hosting. Die Spalte Bewusstsein und Ausbildung ist für alle Zeilen hell markiert.
- **Tab. 1 (S. 14):** Stärken und Grenzen der neun Hebel, an der Textebene geprüft.

## Wörtliche Stellen

> „Trustworthy AI requires reproducibility (Kowald et al. 2024).“ (S. 1)

> „researchers may only provide results for the best test run out of many test runs, instead of properly assessing and reporting average values and variances“ (S. 4)

> „ML models should be benchmarked and evaluated with multiple random number seeds, such that the variance can be reported“ (S. 8)

> „preregistration where researchers register their research intentions for future publication. This approach ensures credibility by separating the research plan from experimental outcomes“ (S. 11)

## Julias Markierungen im PDF

2 Hervorhebungen auf S. 1 (`md/Semmelrock-etal-2025-Reproducibility-ML.markierungen.md`): der Satz zu den Hindernissen und Hebeln auf den Ebenen Methoden, Code, Daten, Experimente (Abstract) und „Trustworthy AI requires reproducibility (Kowald et al. 2024).“ Beide aufgenommen (Worum es geht; Kernaussagen, wörtliche Stelle). Die zitierte Arbeit Kowald et al. 2024 ist im Artikel als „Establishing and Evaluating Trustworthy AI: Overview and Research Challenges“, *Frontiers in Big Data* 7: 1467222, angegeben (S. 17) und liegt vermutlich als `pdf/Kowald-etal-2024-Trustworthy-AI.pdf` vor (nicht abgeglichen). Keine Notizen.

## Bezug zur Dissertation

- **`PROMPT-LOG.md` Ebene A und Protokoll 4.10:** Die Forderung, nicht nur den besten Lauf zu berichten, sondern Mittelwert und Varianz über mehrere Läufe (S. 4, S. 8, S. 10), stützt die Regel im Prompt-Log, dass jeder Lauf eigene Einträge bekommt und vorab festgelegt wird, welcher Lauf in die Auswertung eingeht. Für Freeze 2 heißt das: Anzahl der Läufe pro Item festlegen und die Streuung zwischen Läufen berichten, nicht nur einen Wert.
- **Protokoll 4.4 Punkt 6 und 7 Schritt 4 (feste Seeds):** gestützt (S. 8). Tab. 1 (S. 14) erinnert daran, dass ein fester Seed nur eine Punktschätzung liefert; das betrifft die Ziehung nicht (sie ist ein Design, kein Training), wohl aber LLM-Läufe mit Temperatur über 0.
- **Protokoll 11 (Präregistrierung und Abweichungslog):** gestützt; Präregistrierung ist im Artikel der Hebel gegen Spin und selektives Berichten (S. 11 bis 12).
- **Protokoll 9.2 (MFS ohne Stichproben-Tokens), Protokoll 4.2 (Pilot-Lemmata disjunkt), `knowledge/data.md` B1 (Typlisten):** Die Lecktypologie nach Kapoor & Narayanan (S. 5) gibt die Begriffe für das, was das Protokoll schon tut: Leave-out der Stichproben-Tokens bei der MFS-Baseline gegen Typ 1 (kein sauberer Split), disjunkte Pilot-Lemmata gegen abhängige Stichproben, Typlisten aus Prompt und Annotationsdatei entfernen gegen Informationen, die die Bewertung verfälschen. Für den Artikel lässt sich so zitierbar benennen, welche Lecks ausgeschlossen sind.
- **`DMP.md` Abschnitt 2 und 5:** Data Cards und Model Cards (S. 9 bis 10) ergänzen Datasheet und Data Statement, die der DMP schon nennt. Nach dem R1-bis-R4-Raster (S. 3) ist die Studie bis zur Publikation höchstens R2 (Beschreibung und Code öffentlich, Labels privat) und mit der verschlüsselten Ablage auf Zenodo R4. Das ist eine bewusste Abwägung gegen Kontamination (Protokoll 10), die der Artikel nicht behandelt und die im Artikel der Dissertation begründet werden sollte.
- **Grenze für die LLM-Läufe:** Der Artikel behandelt Nichtdeterminismus und Umgebungsunterschiede beim Training (S. 6) und Rechenkosten beim Nachtrainieren von LLMs (S. 7). Dass ein über eine Anbieter-API genutztes Modell weder geteilt noch eingefroren werden kann, sprechen die Autor:innen nur über den Offenheits-Tracker an (S. 10). Für die Dissertation ist das der Punkt, an dem das Prompt-Log (Modell-ID mit Snapshot, Rohausgaben) die fehlende R4-Reproduzierbarkeit nur teilweise ersetzt.

## Grenzen und Einwände

- Überblick ohne beschriebene Methode der Literaturauswahl; Beispiele überwiegend aus Biomedizin, Empfehlungssystemen und Reinforcement Learning.
- Keine Behandlung von Annotation, Goldstandards oder menschlicher Übereinstimmung; „Daten“ heißt hier Trainings- und Testdaten.
- Kein Kapitel zu prompt-basierter Nutzung geschlossener LLMs (Modellversionen, stille Updates, API-Nichtdeterminismus); LLMs erscheinen fast nur als Kostenproblem (S. 7, S. 13) und als Evaluationsgegenstand (S. 10).
- Kleine Unstimmigkeiten in der Literaturliste, z. B. Hosseini et al. „2024“ mit Angabe *Quantitative Science Studies* 6 (S. 17); für die Dissertation ohne Belang.

## Weiterführend

- Gundersen 2021, Gundersen & Kjensmo 2018, Gundersen, Shamsaliei & Isdahl 2022: Begriffe und Stufen der Reproduzierbarkeit (S. 2 bis 3).
- Belz et al. 2021, Reproduzierbarkeit in der NLP (S. 4, S. 6).
- Kapoor & Narayanan 2023, *Patterns* 4(9): 100804, Datenlecks und Model Info Sheets (S. 5, S. 10 bis 11; Literatur S. 17).
- Liesenfeld, Lopez & Dingemanse 2023, Offenheit instruktionsgetunter Textgeneratoren (S. 10; Literatur S. 17).
- Biderman et al. 2024, lm-eval (S. 10).
- Hosseini et al. 2024, Open Science und generative KI (S. 14; Literatur S. 17).
- Kowald et al. 2024, *Frontiers in Big Data* 7: 1467222 (S. 1; Literatur S. 17).
