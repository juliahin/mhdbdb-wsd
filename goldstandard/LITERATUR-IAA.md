# Literatur: Inter-Annotator-Agreement für den WSD-Goldstandard

**Stand:** 2026-11-16 (Zitatkorrekturen K4 bis K16 nach `VORSCHLAEGE-2026-11.md`, A38 im Protokoll, geprüft an den nicht gegengelesenen KI-Zusammenfassungen in `literatur/zusammenfassungen/`; Zeile Henrich 2015 2026-10-28; sonst 2026-10-08). Zusammengetragen von drei Recherche-Agenten (Claude Code) zu drei Fragen:
Maße in der WSD, Ablauf und Stichprobengröße, Praxis bei historischen Sprachen.

**Prüfstatus beachten.** ✔ heißt: Der Agent hat den Volltext oder die Verlagsseite gelesen.
○ heißt: nur bibliografisch oder über das Abstract bzw. Sekundärzitate geprüft. Nichts davon
habe ich selbst gegengelesen. Vor dem Zitieren in der Dissertation jede Angabe am Original
prüfen, besonders die Einträge aus 2026 und alle mit ○.

## Kernaussagen, die das Protokoll übernimmt

| Aussage | Beleg | Protokoll |
|---|---|---|
| Rohübereinstimmung allein reicht nicht; zufallskorrigierte Maße mit einer Verteilung (π, α) sind Cohen's κ vorzuziehen. Bei mengenwertigen Labels ist α mit gewichteter Distanz „fast unvermeidlich". Schwelle 0,8, aber keine Publikationsbedingung. Konfusionsmatrix berichten. | Artstein & Poesio 2008 ✔ | 9.1 |
| MASI: Mengendistanz für Mehrfachlabels, einsetzbar in α. Für WordNet-Mehrfachannotation ergab das α ≈ 0,45 bis 0,66, aber erst nach Ausschluss der schwächsten Person je Set (6 bis 9 Personen pro Set); mit allen Personen im Mittel 0,49 (Passonneau et al. 2006, S. 1953 bis 1954). Die Zahlen stammen aus Passonneau et al. 2006, nicht aus Passonneau 2006. Formelvarianten: 1 − J·M (Passonneau 2006) gegen d_P × d_J (Artstein & Poesio 2008, S. 584); das Protokoll legt 1 − J·M fest. | Passonneau 2006 ✔; Passonneau, Habash & Rambow 2006 ✔ | 9.1 |
| Rohübereinstimmung ist direkt mit Systemgenauigkeit vergleichbar. | Kilgarriff 2001 ✔ | 9.1 |
| Prävalenz: Bei schiefen Verteilungen ist κ niedrig trotz hoher Übereinstimmung. Für WSD gilt: 56,7 % Übereinstimmung, mittleres κ 0,317 (Ng et al.; 0,317 ist der Mittelwert der κ pro Wort, Ng et al. vergleichen keine Zufallsmodelle); 67,3 %, κ = 0,58 (Mikro) oder 0,35 (Makro) bei Mihalcea et al. (S. 26), gerechnet über den ganzen OMWE-Bestand (über 350 Wörter, nicht das Testset); Mikro und Makro unterscheiden sich in Mittelung und Zufallsmodell zugleich. Artstein & Poesio nennen nur 67,3 % und 0,58 (S. 587). Nachgerechnet ergibt (0,673 − 0,20)/0,80 = 0,59, nicht 0,58 (Rechnung des Laufs). | Feinstein & Cicchetti 1990 ○; Ng, Lim & Foo 1999 ✔; Mihalcea, Chklovski & Kilgarriff 2004 ✔ | 9.1 |
| Gwets AC1 ist unter hoher Prävalenz stabil (umstritten). | Gwet 2008 ○ | 9.1 |
| Typische Werte: feinkörnig (WordNet) 67,3 % (OMWE) und 72,5 % (Senseval-3 All-Words) als Vergleichswerte bei Navigli et al. (S. 32); Ng et al. liegen mit 56,7 % darunter und stützen die Spanne nicht. Grobkörnig 93,80 % zwischen zwei Autoren auf 710 Instanzen, wobei einer das grobe Inventar für diese Wörter selbst abgebildet hat (Navigli et al. 2007, S. 31 bis 32); Hovy et al. 2006 nennen für Senses nur das Ziel 90 % (S. 58), ihre Werte über 90 % (91,8 und 94,2 %) gelten für Koreferenz (S. 59). Zusammenlegen hob bei 53 Nomen κ von 0,463 auf 0,862, aber der Algorithmus legt zusammen, bis κ ≥ 0,8 erreicht ist (Ng et al. 1999, S. 11 bis 13); es ist nicht gleichwertig zu einer Studie mit groben Kategorien (Artstein & Poesio 2008, S. 588; nicht mit Véronis 1998 verwechseln). | Navigli et al. 2007 ✔; Hovy et al. 2006 ✔ (nur Ziel 90 %); Ng et al. 1999 ✔; Artstein & Poesio 2008 ✔ | 9.1 Punkt 7 |
| Konfidenzintervalle für α per Bootstrap. | Hayes & Krippendorff 2007 ○; Artstein & Poesio 2008 ✔ | 9.1 |
| Ablauf: Richtlinien, Pilot, Messen, Revidieren, Einfrieren, Hauptrunde, Adjudikation (MATTER-Zyklus). OntoNotes: eine 50-Satz-Stichprobe pro Wort wird annotiert, bei ITA unter 90 % überarbeitet der Linguist das Inventar (nicht die Richtlinien); das Maß wird nicht genannt (Hovy et al. 2006, S. 58). | Pustejovsky & Stubbs 2012 ○; Hovy et al. 2006 ✔; Hovy 2010 ○ (das lokale PDF ist nur das einseitige Tutorial-Abstract und enthält nichts davon) | 7 |
| Reihenfolge der Items verändert Urteile (klein: 2,8 bzw. 4,5 Prozentpunkte über 50 Items, nur in 5 von 10 Bedingungen signifikant, Beck et al. 2024, S. 84); Vorannotationen verankern (Berzak et al. 2016, gilt nur für vorausgefüllte Antworten, nicht für Optionslisten ohne Vorauswahl). | Beck et al. 2024 ✔; Berzak et al. 2016 ✔ | 7, 8 |
| Labels vor der Aggregation mitveröffentlichen (Prabhakaran et al. 2021, S. 137; sie sprechen von „relatively more subjective tasks“); „Abweichung ist oft Signal“ steht so bei Plank 2022 (S. 10671, 10674). | Prabhakaran et al. 2021 ✔; Plank 2022 ✔ | 7 |
| Zufallskorrigierte Übereinstimmung ist für gute Goldlabels „neither necessary nor sufficient“ und „at best an indirect measure“; von adjudiziertem Gold spricht das Werk nicht (S. 311 bis 312). | Passonneau & Carpenter 2014 ✔ | 9.2 |
| LLM ersetzt Menschen nur, wenn es mit ihnen so gut übereinstimmt wie diese untereinander. | Calderon, Reichart & Dror 2025 ○ | 9.2 |
| Bei Items mit mehreren Gold-Senses nennt Henrich fünf Wege (Teilwertung, ignorieren, „einer getroffen“ gilt als richtig, alle bis auf einen Sense entfernen, je Sense ein Eintrag). „Einer getroffen“ verwirft er, weil es die Ergebnisse leicht überschätzt; Teilwertung mit Dice (Véronis 1998) hält er für fairer. Das Protokoll behält die Regel als Primärregel und berichtet Dice-Teilwertung und Auswertung ohne `MEHRERE`-Items zusätzlich. | Henrich 2015 ✔ (S. 151 bis 152, Abschnitt 6.2); Véronis 1998 ○ (zitiert nach Henrich 2015, S. 151 bis 152). Henrich führt Resnik & Yarowsky 1997 für Teilpunkte bei mehreren Gold-Senses an; das Original gibt Teilpunkte nur für die Wahrscheinlichkeit auf dem richtigen Sense und für den Abstand eines Fehlers, mit genau einem richtigen Sense pro Instanz (S. 81 bis 82), und ist nicht als Quelle der Dice-Teilwertung zu führen; die Fassung von 1999 (*Natural Language Engineering* 5(2)) bleibt zu beschaffen (○) | 9.2 |
| Kontamination: Testdaten nicht im Klartext veröffentlichen, verschlüsseln mit veröffentlichtem Schlüssel, Lizenz ohne Bearbeitungen oder gegen Trainingsnutzung (Jacovi et al. 2023, S. 5077 bis 5078, 5080). Sainz et al. begründen das Problem (S. 10776), empfehlen aber weder Verschlüsselung noch Lizenz, sondern verweisen auf Jacovi. Der Canary-String steht in keinem der beiden Werke (Textebene durchsucht); er ist im Protokoll eine eigene Maßnahme ohne Literaturbeleg. | Sainz et al. 2023 ✔ (nur Problembegründung); Jacovi et al. 2023 ✔ (ohne Canary) | 10 |
| Ursachentypologie für Abweichungen: fehlende Regeln; Abweichungen trotz bestehender Regeln (überwiegend Regelverstöße, daneben Folgefehler und vergessene Annotation); unterschiedliches Textverständnis (Folien 16, 19). Die Kategorie heißt nicht „Regelverstoß“. | Ihden et al. 2015 (Vortragsfolien, Erstautorin laut Titelfolie; Datei `Barteld-etal-2015-…`) ✔ | 7 |

## Historische Sprachen: Stand der Praxis

- **Fehlende Muttersprachler:innen** ist das Grundproblem. HiTS ersetzt Intuition durch Belegsynopse
  und markiert unauflösbare Ambiguität bewusst nicht (Dipper et al. 2013 ○). SemEval-2020 Task 1
  musste Latein auf eine Annotator:in pro Wort umstellen (Mangel an Annotierenden) und von der Paarvergleichs-Aufgabe auf „Beleg gegen Wörterbuchdefinition“ wechseln, weil die Fachleute zwei Textstellen nur über eine Übersetzung vergleichen konnten (Schlechtweg et al. 2020, S. 4 bis 5). IAA wurde für Latein dort nicht berichtet; Ghizzota et al. 2025 berichten sie für ein Wort (*virtus*, ρ 0,69), also nur an einem von 40 Wörtern.
- **Werte bei graduellen Urteilen:** DURel ρ ≈ 0,57 bis 0,68 (Schlechtweg et al. 2018 ✔; der Mittelwert ist im Text 0,66, aus der Tabelle 0,635), SemEval
  Runde 1 ρ ≈ 0,58 bis 0,69 (Schlechtweg et al. 2020 ✔), Erk et al. 2013 ρ ≈ 0,50 bis 0,62 (graduell, Rangkorrelation) ○. Der Vergleichswert 0,638 für die Einzelsense-Annotation ist eine Rohübereinstimmung, gerechnet nur für Items mit einer Antwort und vier Personen; über alle Items und acht Personen sind es 0,574 (Erk et al. 2013, S. 533 bis 534). Zwei verschiedene Maße, nicht nebeneinander lesen.
- **Mittelhochdeutsch:** UD-Treebank α = 0,85 für Syntax (Dipper et al. 2024 ○). Für die MHDBDB wurde
  **keine** veröffentlichte IAA gefunden. Hinkelmanns & Zeppezauer-Wachauer 2023 ✔ (S. 180) sagen, linguistische
  Annotationen (POS, Phrasen- und Satzstrukturen) seien „bisher“ auf graphematische Types im
  Wortartikel bezogen gewesen; dass auch Bedeutungen so angebunden waren, ist eine Lesart, nicht
  belegt. Die Korpusmessung im Protokoll (Abschnitt 2) zeigt,
  dass Silber trotzdem teilweise pro Beleg unterscheidet.
- **Lücke:** keine IAA-Studie für ein onomasiologisches Inventar (Begriffssystem) gefunden, und kein
  WSD-Goldstandard, der zugleich nach Gattung, Zeit und Raum schichtet. Beides ist ein möglicher
  Beitrag der Arbeit.
- **Sprachmodelle bei historischen Sprachen** werden meist mit F1 gegen ein Gold ohne oder mit nur punktuell berichteter IAA gemessen. Ghinassi et al. 2024 ○ enthält kein LLM (Encoder mit Klassifikationsschicht pro Lemma); Ghizzota et al. 2026 ○ ist eine binäre Entscheidung je Sense, keine Sense-Wahl. Für Mittelhochdeutsch wurde keine Studie
  gefunden.

## Stichprobengröße

Klassische Quellen (Flack et al. 1988 ○; Donner & Eliasziw 1992 ○; Sim & Wright 2005 ○;
Bujang & Baharum 2017 ✔) liefern keine Tabelle für ca. 500 mehrkategoriale WSD-Items. Eigene
Rechnung mit der Großstichproben-Näherung SE(κ) ≈ √(p_o(1−p_o)/N) / (1−p_e), am 2026-10-08
nachgerechnet, halbe Breite des 95-%-Intervalls:

| p_o / p_e (κ) | N = 120 | N = 250 | N = 500 |
|---|---|---|---|
| 0,80 / 0,40 (0,67) | ±0,12 | ±0,08 | ±0,06 |
| 0,80 / 0,60 (0,50) | ±0,18 | ±0,12 | ±0,09 |
| 0,90 / 0,50 (0,80) | ±0,11 | ±0,07 | ±0,05 |

## Literatur

- Artstein, R. & Poesio, M. (2008). Inter-coder agreement for computational linguistics. *Computational Linguistics* 34(4), 555–596. doi:10.1162/coli.07-034-R2
- Ihden, S., Barteld, F., Dreessen, K. & Schröder, I. (2015). Grammatische Annotation historischer Texte: ein Tagset für das Mittelniederdeutsche. Vortragsfolien, IGDD Luxemburg, 10. bis 12. September 2015 (BibTeX-Schlüssel `ihden2015tagset` in `literatur/references.txt`; Dateiname `Barteld-etal-2015-…`; Reihenfolge der Autor:innen aus der zweispaltigen Titelfolie nicht eindeutig).
- Beck, J., Eckman, S., Ma, B., Chew, R. & Kreuter, F. (2024). Order effects in annotation tasks. UncertaiNLP@EACL. https://aclanthology.org/2024.uncertainlp-1.8/
- Bender, E. & Friedman, B. (2018). Data statements for NLP. *TACL* 6, 587–604. doi:10.1162/tacl_a_00041
- Berzak, Y. et al. (2016). Anchoring and agreement in syntactic annotations. EMNLP. https://aclanthology.org/D16-1239/
- Bujang, M. A. & Baharum, N. (2017). Guidelines of the minimum sample size requirements for Kappa agreement test. *Epidemiology, Biostatistics and Public Health* 14(2).
- Calderon, N., Reichart, R. & Dror, R. (2025). The Alternative Annotator Test for LLM-as-a-Judge. ACL. https://aclanthology.org/2025.acl-long.782
- Dipper, S. et al. (2013). HiTS: ein Tagset für historische Sprachstufen des Deutschen. *JLCL* 28(1), 85–137.
- Dipper, S. et al. (2024). Universal Dependencies: Extensions for modern and historical German. LREC-COLING. https://aclanthology.org/2024.lrec-main.1485/
- Donner, A. & Eliasziw, M. (1992). A goodness-of-fit approach to inference procedures for the kappa statistic. *Statistics in Medicine* 11, 1511–1519.
- Erk, K., McCarthy, D. & Gaylord, N. (2013). Measuring word meaning in context. *Computational Linguistics* 39(3), 511–554. doi:10.1162/COLI_a_00142
- Feinstein, A. R. & Cicchetti, D. V. (1990). High agreement but low kappa: I. *Journal of Clinical Epidemiology* 43(6), 543–549.
- Flack, V. F. et al. (1988). Sample size determinations for the two rater kappa statistic. *Psychometrika* 53, 321–325.
- Gebru, T. et al. (2021). Datasheets for datasets. *Communications of the ACM* 64(12), 86–92. doi:10.1145/3458723
- Ghinassi, I. et al. (2024). Language pivoting from parallel corpora for WSD of historical languages: Latin. LREC-COLING. https://aclanthology.org/2024.lrec-main.880
- Ghizzota, E. et al. (2026). Linguistic knowledge graphs for sense prediction: Latin. LREC. https://aclanthology.org/2026.lrec-1.856/
- Gwet, K. L. (2008). Computing inter-rater reliability and its variance in the presence of high agreement. *British Journal of Mathematical and Statistical Psychology* 61, 29–48.
- Hayes, A. F. & Krippendorff, K. (2007). Answering the call for a standard reliability measure for coding data. *Communication Methods and Measures* 1(1), 77–89.
- Henrich, V. (2015). *Word Sense Disambiguation with GermaNet: Semi-Automatic Enhancement and Empirical Results*. Dissertation, Eberhard Karls Universität Tübingen. doi:10.15496/publikation-4706 (Titel vom Titelblatt, DOI aufgelöst; `literatur/references.txt`, `henrich2015word`)
- Hinkelmanns, P. & Zeppezauer-Wachauer, K. (2023). Mittelhochdeutsche Begriffsdatenbank (MHDBDB). In Bleier & Klug (Hg.), *Digitale Edition in Österreich*, 179–181.
- Hovy, E. (2010). Annotation. Tutorial, ACL. https://aclanthology.org/P10-5004/
- Hovy, E., Marcus, M., Palmer, M., Ramshaw, L. & Weischedel, R. (2006). OntoNotes: The 90% solution. NAACL-HLT. https://aclanthology.org/N06-2015/
- Jacovi, A., Caciularu, A., Goldman, O. & Goldberg, Y. (2023). Stop uploading test data in plain text. *Proceedings of EMNLP 2023*, 5075–5084. doi:10.18653/v1/2023.emnlp-main.308
- Kilgarriff, A. (2001). English lexical sample task description. SENSEVAL-2. https://aclanthology.org/S01-1004/
- Krippendorff, K. (2004). Reliability in content analysis. *Human Communication Research* 30(3), 411–433.
- Mihalcea, R., Chklovski, T. & Kilgarriff, A. (2004). The SENSEVAL-3 English lexical sample task. https://aclanthology.org/W04-0807/
- Navigli, R., Litkowski, K. & Hargraves, O. (2007). SemEval-2007 Task 07: Coarse-grained English all-words task. https://aclanthology.org/S07-1006/
- Ng, H. T., Lim, C. Y. & Foo, S. K. (1999). A case study on inter-annotator agreement for WSD. SIGLEX. https://aclanthology.org/W99-0502/
- Passonneau, R. J. (2006). Measuring agreement on set-valued items (MASI). LREC. https://aclanthology.org/L06-1392/
- Passonneau, R. J., Habash, N. & Rambow, O. (2006). Inter-annotator agreement on a multilingual semantic annotation task. LREC. https://aclanthology.org/L06-1391/
- Passonneau, R. J. & Carpenter, B. (2014). The benefits of a model of annotation. *TACL* 2, 311–326.
- Plank, B. (2022). The "problem" of human label variation. EMNLP. https://aclanthology.org/2022.emnlp-main.731
- Prabhakaran, V., Mostafazadeh Davani, A. & Díaz, M. (2021). On releasing annotator-level labels and information in datasets. LAW. https://aclanthology.org/2021.law-1.14/
- Pustejovsky, J. & Stubbs, A. (2012). *Natural Language Annotation for Machine Learning*. O'Reilly.
- Sainz, O. et al. (2023). NLP evaluation in trouble. *Findings of EMNLP 2023*, 10776–10787. doi:10.18653/v1/2023.findings-emnlp.722
- Schlechtweg, D., Schulte im Walde, S. & Eckmann, S. (2018). Diachronic Usage Relatedness (DURel). NAACL-HLT. https://aclanthology.org/N18-2027/
- Schlechtweg, D. et al. (2020). SemEval-2020 Task 1: Unsupervised lexical semantic change detection. *Proceedings of SemEval-2020*, 1–23. doi:10.18653/v1/2020.semeval-1.1
- Sim, J. & Wright, C. C. (2005). The kappa statistic in reliability studies. *Physical Therapy* 85(3), 257–268.
