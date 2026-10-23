# Literatur: Inter-Annotator-Agreement für den WSD-Goldstandard

**Stand:** 2026-10-08. Zusammengetragen von drei Recherche-Agenten (Claude Code) zu drei Fragen:
Maße in der WSD, Ablauf und Stichprobengröße, Praxis bei historischen Sprachen.

**Prüfstatus beachten.** ✔ heißt: Der Agent hat den Volltext oder die Verlagsseite gelesen.
○ heißt: nur bibliografisch oder über das Abstract bzw. Sekundärzitate geprüft. Nichts davon
habe ich selbst gegengelesen. Vor dem Zitieren in der Dissertation jede Angabe am Original
prüfen, besonders die Einträge aus 2026 und alle mit ○.

## Kernaussagen, die das Protokoll übernimmt

| Aussage | Beleg | Protokoll |
|---|---|---|
| Rohübereinstimmung allein reicht nicht; zufallskorrigierte Maße mit einer Verteilung (π, α) sind Cohen's κ vorzuziehen. Bei mengenwertigen Labels ist α mit gewichteter Distanz „fast unvermeidlich". Schwelle 0,8, aber keine Publikationsbedingung. Konfusionsmatrix berichten. | Artstein & Poesio 2008 ✔ | 9.1 |
| MASI: Mengendistanz für Mehrfachlabels, einsetzbar in α. Für WordNet-Mehrfachannotation ergab das α ≈ 0,45 bis 0,66. | Passonneau 2006 ✔; Passonneau, Habash & Rambow 2006 ✔ | 9.1 |
| Rohübereinstimmung ist direkt mit Systemgenauigkeit vergleichbar. | Kilgarriff 2001 ✔ | 9.1 |
| Prävalenz: Bei schiefen Verteilungen ist κ niedrig trotz hoher Übereinstimmung. In WSD verschiebt allein das Zufallsmodell κ stark: 57 % Übereinstimmung, κ = 0,317 (Ng et al.); 67,3 %, κ = 0,58 oder 0,35 je nach Zufallsmodell (Mihalcea et al.). | Feinstein & Cicchetti 1990 ○; Ng, Lim & Foo 1999 ✔; Mihalcea, Chklovski & Kilgarriff 2004 ✔ | 9.1 |
| Gwets AC1 ist unter hoher Prävalenz stabil (umstritten). | Gwet 2008 ○ | 9.1 |
| Typische Werte: feinkörnig (WordNet) ca. 67 bis 72 %, grobkörnig ca. 90 bis 94 %. Zusammenlegen von Senses hob κ von 0,46 auf 0,86, ist aber nicht gleichwertig zu einer Studie mit groben Kategorien. | Navigli et al. 2007 ✔; Hovy et al. 2006 ✔; Ng et al. 1999 ✔; Artstein & Poesio 2008 ✔ | 9.1 Punkt 7 |
| Konfidenzintervalle für α per Bootstrap. | Hayes & Krippendorff 2007 ○; Artstein & Poesio 2008 ✔ | 9.1 |
| Ablauf: Richtlinien, Pilot, Messen, Revidieren, Einfrieren, Hauptrunde, Adjudikation (MATTER-Zyklus). OntoNotes: 50 Sätze pro Pilotrunde, Revision bis 90 %. | Pustejovsky & Stubbs 2012 ○; Hovy 2010 ✔; Hovy et al. 2006 ✔ | 7 |
| Reihenfolge der Items verändert Urteile; Vorannotationen verankern. | Beck et al. 2024 ✔; Berzak et al. 2016 ✔ | 7, 8 |
| Labels vor der Aggregation mitveröffentlichen; Abweichung ist oft Signal. | Prabhakaran et al. 2021 ✔; Plank 2022 ✔ | 7 |
| Hohe Roh-IAA belegt nicht die Qualität des adjudizierten Golds. | Passonneau & Carpenter 2014 ○ | 9.2 |
| LLM ersetzt Menschen nur, wenn es mit ihnen so gut übereinstimmt wie diese untereinander. | Calderon, Reichart & Dror 2025 ○ | 9.2 |
| Kontamination: Testdaten nicht im Klartext veröffentlichen; verschlüsseln, Lizenz, Canary. | Sainz et al. 2023 ✔; Jacovi et al. 2023 ✔ | 10 |
| Ursachentypologie für Abweichungen (Richtlinienlücke, Regelverstoß, unterschiedliches Textverständnis). | Barteld, Dreessen, Ihden & Schröder 2015 (Vortragsfolien) ○ | 7 |

## Historische Sprachen: Stand der Praxis

- **Fehlende Muttersprachler:innen** ist das Grundproblem. HiTS ersetzt Intuition durch Belegsynopse
  und markiert unauflösbare Ambiguität bewusst nicht (Dipper et al. 2013 ○). SemEval-2020 Task 1
  musste Latein auf eine Annotator:in pro Wort umstellen, also ohne IAA (Schlechtweg et al. 2020 ○).
- **Werte bei graduellen Urteilen:** DURel ρ ≈ 0,57 bis 0,68 (Schlechtweg et al. 2018 ○), SemEval
  Runde 1 ρ ≈ 0,58 bis 0,69, Erk et al. 2013 ρ ≈ 0,50 bis 0,62 (graduell) gegenüber 0,638 Einzelsense ○.
- **Mittelhochdeutsch:** UD-Treebank α = 0,85 für Syntax (Dipper et al. 2024 ○). Für die MHDBDB wurde
  **keine** veröffentlichte IAA gefunden. Hinkelmanns & Zeppezauer-Wachauer 2023 ✔ (S. 180) sagen, linguistische
  Annotationen (POS, Phrasen- und Satzstrukturen) seien „bisher“ auf graphematische Types im
  Wortartikel bezogen gewesen; dass auch Bedeutungen so angebunden waren, ist eine Lesart, nicht
  belegt. Die Korpusmessung im Protokoll (Abschnitt 2) zeigt,
  dass Silber trotzdem teilweise pro Beleg unterscheidet.
- **Lücke:** keine IAA-Studie für ein onomasiologisches Inventar (Begriffssystem) gefunden, und kein
  WSD-Goldstandard, der zugleich nach Gattung, Zeit und Raum schichtet. Beides ist ein möglicher
  Beitrag der Arbeit.
- **LLMs bei historischen Sprachen** werden meist mit F1 gegen ein Gold ohne berichtete IAA gemessen
  (Ghizzota et al. 2026 ○; Ghinassi et al. 2024 ○). Für Mittelhochdeutsch wurde keine Studie
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
- Barteld, F., Dreessen, K., Ihden, S. & Schröder, I. (2015). Grammatische Annotation historischer Texte: ein Tagset für das Mittelniederdeutsche. Folien, IGDD Luxemburg.
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
- Hinkelmanns, P. & Zeppezauer-Wachauer, K. (2023). Mittelhochdeutsche Begriffsdatenbank (MHDBDB). In Bleier & Klug (Hg.), *Digitale Edition in Österreich*, 179–181.
- Hovy, E. (2010). Annotation. Tutorial, ACL. https://aclanthology.org/P10-5004/
- Hovy, E., Marcus, M., Palmer, M., Ramshaw, L. & Weischedel, R. (2006). OntoNotes: The 90% solution. NAACL-HLT. https://aclanthology.org/N06-2015/
- Jacovi, A., Caciularu, A., Goldman, O. & Goldberg, Y. (2023). Stop uploading test data in plain text. EMNLP. arXiv:2305.10160
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
- Sainz, O. et al. (2023). NLP evaluation in trouble. Findings of EMNLP. arXiv:2310.18018
- Schlechtweg, D., Schulte im Walde, S. & Eckmann, S. (2018). Diachronic Usage Relatedness (DURel). NAACL-HLT. https://aclanthology.org/N18-2027/
- Schlechtweg, D. et al. (2020). SemEval-2020 Task 1: Unsupervised lexical semantic change detection. arXiv:2007.11464
- Sim, J. & Wright, C. C. (2005). The kappa statistic in reliability studies. *Physical Therapy* 85(3), 257–268.
