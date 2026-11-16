# Literatur: Stichprobendesign für den WSD-Goldstandard

**Stand:** 2026-11-16 (Zitatkorrekturen K1 bis K3, K11, K13, K14 nach `VORSCHLAEGE-2026-11.md`, A38 im Protokoll, geprüft an den nicht gegengelesenen KI-Zusammenfassungen; 2026-10-30: Zeile Raganato korrigiert, Prüfstatus gesenkt; Zeile ReM 2026-10-28; sonst 2026-10-16). Recherchiert von einem Recherche-Agenten (Claude Code), dazu eine skeptische
Zweitmeinung zum Entwurf. Ergänzt [LITERATUR-IAA.md](LITERATUR-IAA.md).

**Prüfstatus:** ✔ = Volltext oder Verlagsseite vom Agenten gelesen, ○ = nur bibliografisch oder
Abstract. Selbst gegengelesen habe ich nur die beiden Rechnungen unten (Connor-Formel nachgerechnet
am 2026-10-16). Vor dem Zitieren jede Angabe am Original prüfen.

## Kernaussagen

| Aussage | Beleg | Folge fürs Design |
|---|---|---|
| Zwei Modelle für WSD-Gold: „textual" (alle Inhaltswörter eines Textes) und „lexical" (erst Wortarten-Typen ziehen, dann Belege). Das lexikalische Modell empfiehlt er nur für **explorative** Evaluation (S. 13), geschichtet nach **Wortart × Korpusfrequenz × Polysemie** (S. 15 bis 16); im Beispiel 4 × 4 Bänder, mindestens 10 Typen pro Zelle. Auch monoseme Wörter mitziehen (S. 16). Kilgarriff misst keine Schwierigkeit: Frequenz und Polysemie sind dort Schichtungsmerkmale. | Kilgarriff 1998 ✔ | Direkter Vorläufer der 36-Zellen-Idee; zitieren |
| Senseval wählte Lemmata über ein Frequenz × Polysemie-Raster, „nicht nach Laune des Experimentators"; meist 80 bis 400 Belege pro Aufgabe (Wort plus Wortart; Kilgarriff & Rosenzweig 2000, Abschnitt 3, die LREC-Fassung hat keine Seitenzahlen, daher nach Abschnitt zitieren). Senseval-2: 75 + 15n + 6m Belege pro Wort (Kilgarriff 2001, S. 17). | Kilgarriff & Rosenzweig 2000 ✔; Kilgarriff 2001 ✔ | Klassische Lexical-Sample-Sets haben viele Belege pro Lemma, wir haben 1 |
| Die All-Words-Sets des englischen Standardrahmens bestehen aus wenigen Dokumenten (3 bis 13), und ihre MFS-Werte streuen je Datensatz (54,5 bis 67,1). Die Deutung als Klumpenstichproben, bei denen MFS vom Dokument abhängt, ist unsere eigene; Raganato et al. sprechen nicht so (A24 im Protokoll). | Raganato et al. 2017 ✔ (nur Dokumentzahlen und Streuung der MFS, aus einer nicht gegengelesenen KI-Zusammenfassung); Streuung der MFS über die fünf Texte (74,20 bis 85,60; Tab. 5, S. 34): Navigli et al. 2007 ✔; die Erklärung über textspezifische Senses ist eine Vermutung der Autoren („seem to“, „We believe“, S. 33), und Text und Domäne fallen dort zusammen | Textklumpen ernst nehmen; Obergrenze pro Text |
| Geschichtete Schätzung, proportionale, Neyman- und gleiche Allokation; gleiche Allokation ist am besten für Vergleiche, am schlechtesten für die Gesamtschätzung. | Cochran 1977 ○; Lohr ○ | Konflikt der Ziele benennen |
| Potenzallokation n_h ∝ X_h^q; q = 0 gleich, q = 1 proportional, q = 0,5 Quadratwurzel. | Bankier 1988 ○ (Formel nach Keto & Pahkinen 2017 ✔) | Begründung der Gattungsquote |
| Designeffekt durch ungleiche Gewichte: deff_w = 1 + CV²(w), n_eff = n / deff_w. Klumpeneffekt: deff_c ≈ 1 + (m̄ − 1)ρ. | Kish 1965, 1992 ○; Gabler, Haeder & Lahiri 1999 ○ | Gewichtete Zahl nur mit n_eff berichten |
| Mehrere Ziele offen benennen statt ein künstliches Einzelziel; Optima sind flach. Ein primäres Schätzziel festlegen, andere mit vorab angegebener Präzision. | Kish 1988 ○; Costa, Satorra & Ventura 2004 ○ | Primäres Schätzziel festlegen |
| Repräsentativität durch geschichtete statt proportionale Korpusgestaltung. | Biber 1993 ○ | Gattungsausgleich begründen |
| Historische Daten sind fragmentarisch und schief überliefert („bad data"). | Nevalainen 1999 ○ | Bias benennen |
| MiGraKo (Teilkorpus von ReM) ist nach 50-Jahres-Abschnitten, Sprachräumen und Vers/Prosa/Urkunde strukturiert (S. 3). eReM nimmt Texte „in aller Regel“ komplett auf; bei sechs Großtexten wurden Ausschnitte auf „wenigstens 20.000 Tokens“ vergrößert, also Untergrenze (S. 4); eReM ist „kein strukturiertes Korpus wie MiGraKo“ (S. 5). Eine Obergrenze pro Text formuliert das Handbuch nicht. | Klein & Dipper 2016 ✔ (am Original gegengelesen 2026-10-28) | Beispiel für Schichtung nach Zeit, Sprachraum und Textart (MiGraKo); **kein** Vorbild für die Obergrenze pro Text (Korrektur, A13) |
| Korpusdaten verletzen die Zufallsannahme auf Textebene; Resampling mit dem Text als Einheit. | Evert 2006 ○; Lijffijt et al. 2016 ○ | Bootstrap nach Text |
| One sense per discourse: zwei Belege **desselben** polysemen Nomens im selben Text haben zu 94 % (51 von 54 Paaren) denselben Sense (S. 236; 9 Nomen, Artikel einer Enzyklopädie, fünf Urteilende, darunter die drei Autoren). Die 96,9 % aus dem ACL-Beitrag derselben Autoren lassen sich aus 54 Paaren nicht bilden. | Gale, Church & Yarowsky 1992 ✔ | Stützt „1 Token pro Paar“ und die Panelregel, nicht die Obergrenze pro Text; die ist über die Abhängigkeit innerhalb eines Textes zu begründen |
| Die Sense-Zahl korreliert kaum mit der Systemleistung (20 Nomen mit 2 bis 5 groben Senses, gemessen an Systemen, nicht an Menschen; Loureiro et al. 2021, S. 407). „Schiefe sagt Schwierigkeit besser voraus“ vergleichen sie nicht; Schiefe zieht überwachte und feinabgestimmte Modelle zum häufigsten Sense, besonders bei wenig Trainingsdaten (S. 411 bis 413). Die Entropie sagt die Schwierigkeit besser voraus als die Sense-Zahl (Korrelation mit der Systemleistung −0,510 gegen −0,258; Kilgarriff & Rosenzweig 2000, Abschnitt 5.1); Passonneau et al. 2010 referieren die Entropie nur. | Loureiro et al. 2021 ✔ (nur Sense-Zahl); Kilgarriff & Rosenzweig 2000 ✔; Passonneau et al. 2010 ✔ (referiert) | Entropie und MFS-Anteil als Kovariaten, begründet als Faktor für Modellverzerrung |
| Der „hard core“ (541 Instanzen, die alle sieben Systeme falsch lösen) besteht fast nur aus Nicht-MFS-Instanzen: Systeme sagen dort zu ≥ 62,7 % den ersten Sense voraus, korrekt wäre er zu 2,0 % (Tab. 1, S. 4727). Nicht alle Nicht-MFS-Belege sind hart; für diese allgemein erreicht das beste System 54,2 statt 76,4 Macro-F1 (Tab. 2, 2.525 Instanzen). Macro-F1 nach Sense neben Micro berichten. Die Neuannotation durch einen Linguisten ließ 72,6 % von 5.523 polysemen Instanzen unverändert (ein einziger Linguist, Tab. 4, S. 4729); 91,1 % nach Ausklammern von Wortart-, Token- und Inventarfehlern (S. 4729 bis 4730). | Maru et al. 2022 ✔ | Nicht-MFS-Analyse; Altgold prüfen |
| Verben sind am schwersten. | Raganato et al. 2017 ✔; Passonneau et al. 2010 ✔ | Wortart als Schichtung behalten |
| Power für den gepaarten Vergleich (McNemar) hängt von der Genauigkeitsdifferenz und dem Anteil diskordanter Paare ab; Poweranalyse **vor** der Evaluation mit Pilotdaten. | Connor 1987 ○; Card et al. 2020 ✔ | N über den Pilot bestätigen |

## Stichprobengröße für den gepaarten Vergleich

Connor 1987: n = [z_{1−α/2} √p_d + z_{1−β} √(p_d − δ²)]² / δ², mit p_d = Anteil diskordanter Items
und δ = Genauigkeitsdifferenz. α = 0,05, Power 0,80, nachgerechnet am 2026-10-16:

| δ | p_d = 0,15 | p_d = 0,25 | p_d = 0,35 |
|---|---|---|---|
| 0,05 | 469 | 783 | 1.096 |
| 0,10 | 115 | 194 | 272 |

Bei N = 500 sind gesamt nur Unterschiede von etwa 5 bis 7 Prozentpunkten nachweisbar, je Wortart
(ca. 167 Items) etwa 10 oder mehr.

## Literatur

- Bankier, M. D. (1988). Power allocations: Determining sample sizes for subnational areas. *The American Statistician* 42(3), 174–177.
- Biber, D. (1993). Representativeness in corpus design. *Literary and Linguistic Computing* 8(4), 243–257.
- Card, D. et al. (2020). With Little Power Comes Great Responsibility. EMNLP. https://aclanthology.org/2020.emnlp-main.745
- Cochran, W. G. (1977). *Sampling Techniques*, 3. Aufl. Wiley.
- Connor, R. J. (1987). Sample size for testing differences in proportions for the paired-sample design. *Biometrics* 43, 207–211. doi:10.2307/2531961
- Costa, À., Satorra, A. & Ventura, E. (2004). Improving both domain and total area estimation by composition. *SORT* 28(1), 69–86.
- Evert, S. (2006). How random is a corpus? The library metaphor. *Zeitschrift für Anglistik und Amerikanistik* 54(2), 177–190.
- Gabler, S., Haeder, S. & Lahiri, P. (1999). A model based justification of Kish's formula for design effects for weighting and clustering. *Survey Methodology* 25(1).
- Gale, W., Church, K. & Yarowsky, D. (1992). One Sense Per Discourse. HLT Workshop. https://aclanthology.org/H92-1045
- Keto, M. & Pahkinen, E. (2017). Sample allocation for efficient model-based small area estimation. *Survey Methodology* 43(1).
- Kilgarriff, A. (1998). Gold standard datasets for evaluating word sense disambiguation programs. *Computer Speech and Language* 12(3).
- Kilgarriff, A. (2001). English Lexical Sample Task Description. SENSEVAL-2. https://aclanthology.org/S01-1004
- Kilgarriff, A. & Rosenzweig, J. (2000). English SENSEVAL: Report and Results. LREC (ohne Seitenzahlen, nach Abschnitt zitieren).
- Kish, L. (1965). *Survey Sampling*. Wiley. Kish, L. (1988). Multipurpose sample designs. *Survey Methodology* 14(1). Kish, L. (1992). Weighting for unequal Pi. *Journal of Official Statistics* 8, 183–200.
- Klein, T. & Dipper, S. (2016). *Handbuch zum Referenzkorpus Mittelhochdeutsch*. Bochumer Linguistische Arbeitsberichte 19.
- Lijffijt, J. et al. (2016). Significance testing of word frequencies in corpora. *Digital Scholarship in the Humanities* 31(2).
- Lohr, S. *Sampling: Design and Analysis*. CRC Press.
- Loureiro, D., Rezaee, K., Pilehvar, M. T. & Camacho-Collados, J. (2021). Analysis and Evaluation of Language Models for Word Sense Disambiguation. *Computational Linguistics* 47(2), 387–443. doi:10.1162/coli_a_00405
- Maru, M., Conia, S., Bevilacqua, M. & Navigli, R. (2022). Nibbling at the Hard Core of Word Sense Disambiguation. ACL. https://aclanthology.org/2022.acl-long.324
- Navigli, R., Litkowski, K. & Hargraves, O. (2007). SemEval-2007 Task 07: Coarse-Grained English All-Words Task. https://aclanthology.org/S07-1006
- Nevalainen, T. (1999). Making the best use of "bad" data. *Neuphilologische Mitteilungen* 100(4), 499–533.
- Passonneau, R., Salleb-Aoussi, A., Bhardwaj, V. & Ide, N. (2010). Word Sense Annotation of Polysemous Words by Multiple Annotators. LREC.
- Raganato, A., Camacho-Collados, J. & Navigli, R. (2017). Word Sense Disambiguation: A Unified Evaluation Framework and Empirical Comparison. EACL, 99–110. https://aclanthology.org/E17-1010
