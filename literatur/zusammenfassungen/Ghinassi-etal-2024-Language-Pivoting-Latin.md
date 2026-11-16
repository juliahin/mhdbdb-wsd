# Ghinassi, Tedeschi, Marongiu, Navigli & McGillivray 2024: Language Pivoting aus Parallelkorpora für WSD historischer Sprachen am Beispiel Latein

**Datei:** `pdf/Ghinassi-etal-2024-Language-Pivoting-Latin.pdf` (nur lokal; 12 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Tab. 1 und 2 am Seitenbild geprüft, DOI aufgelöst. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-13). Keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 10072 + n (PDF 1 = S. 10073, PDF 12 = S. 10084). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Ghinassi, Iacopo, Simone Tedeschi, Paola Marongiu, Roberto Navigli & Barbara McGillivray (2024). Language Pivoting from Parallel Corpora for Word Sense Disambiguation of Historical Languages: A Case Study on Latin. In: Nicoletta Calzolari, Min-Yen Kan, Veronique Hoste, Alessandro Lenci, Sakriani Sakti & Nianwen Xue (Hg.), *Proceedings of the 2024 Joint International Conference on Computational Linguistics, Language Resources and Evaluation (LREC-COLING 2024)*. Torino: ELRA and ICCL, S. 10073 bis 10084.
- **DOI/URL:** https://doi.org/10.63317/5gaz3rzgjarc (aufgelöst auf https://lrec.elra.info/lrec2024-main-0880; Crossref: Autor:innen, S. 10073 bis 10084, Mai 2024 ✔; abgerufen 2026-11-13). ACL Anthology 2024.lrec-main.880 (BibTeX: Hg., Ort, Verlag ✔). Die DOI steht nicht im PDF.
- **Lizenz:** CC BY-NC 4.0 laut Kopfzeile S. 10073 („© 2024 ELRA Language Resource Association: CC BY-NC 4.0“).
- **Art:** begutachteter Konferenzbeitrag
- **Sprache:** Englisch
- **Daten und Code:** github.com/Ighina/LatinWSD (S. 10073, 10082; nicht aufgerufen).

## Worum es geht

Für Latein gibt es kaum sense-annotierte Daten. Die Autor:innen übertragen deshalb Sense-Labels aus dem Englischen: Ein englisches WSD-System (AMuSE-WSD) disambiguiert die englische Übersetzung in einem lateinisch-englischen Parallelkorpus, und der WordNet-Synset wird auf das lateinische Zielwort übertragen, wenn er zu den Kandidaten des lateinischen Lemmas passt (S. 10074 bis 10075). Inventar sind die 40 Lemmata des lateinischen SemEval-2020-Datensatzes, deren Senses von Hand auf Princeton WordNet 3.0 abgebildet wurden (S. 10074). Ein auf den übertragenen Daten feinjustiertes LatinBERT erreicht allein 36,93 F1, zusammen mit den SemEval-Trainingsdaten bis 61,83 F1 gegenüber 60,30 nur mit SemEval; die Verbesserung ist signifikant und betrifft vor allem seltene Senses (S. 10077, 10080 bis 10081).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Latein ist trotz langer Überlieferung ressourcenarm; Language Pivoting über Parallelkorpora sei bei ressourcenarmen Sprachen wirksam, für historische Sprachen aber bisher nicht versucht. | S. 10073 bis 10074, Abschnitte 1 bis 2 | Problemstellung, referiert (Pasini et al. 2021) |
| Bisherige lateinische WSD (Bamman & Burns 2020; Lendvai & Wick 2022) erreichte 70 bis 80 % Macro-F, betraf aber nur die ersten beiden Hauptsenses eines Lemmas und nur bis Spätlatein. | S. 10073 bis 10074 | referiert |
| Parallelkorpus aus dem Dynamic Lexicon (Perseus): 123.000 Satzpaare, 2,33 Mio. lateinische Wörter, alt aligniert (Moore, Giza++); bessere Alignierung scheitert am fehlenden Gold. | S. 10074, Abschnitt 3.1 | Datengrundlage, referiert (Yousef & Berti 2015) |
| Inventar: die 40 SemEval-Lemmata; jeder Sense von Hand einem Synset in WordNet 3.0 zugeordnet (über LiLa, Latin WordNet oder direkt PWN). Vier Lemmata ganz oder teilweise nicht abbildbar (*consul*, *sacramentum*, *templum* in einem Sense, *virtus* in zwei Senses), weil die Begriffe römischer oder christlicher Institutionen in WordNet fehlen. | S. 10074 bis 10075 | eigene Annotation |
| Zwei Übertragungsvarianten: Schnittmenge der englischen Synsets mit den Kandidaten (6.412 Sätze) oder zusätzlich über Wortalignierung (3.886 Sätze). | S. 10075, Abschnitt 3.3 | eigene Methode |
| Testdaten: lateinischer SemEval-2020-Datensatz aus LatinISE; 40 Lemmata (20 mit christlichem Bedeutungswandel, 20 Kontrollwörter), je 60 Sätze (30 vor, 30 nach Christus), annotiert nach einer Variante von DURel auf einer Vierstufenskala zu jeder Wörterbuchdefinition (Logeion). Jeder zehnte Satz geht in den Test. | S. 10075 bis 10076, Abschnitt 4.1 | Datengrundlage, referiert (Schlechtweg et al. 2020; McGillivray et al. 2022) |
| Modell: LatinBERT mit Klassifikationsschicht pro Lemma; Bewertung mit nach Sense-Häufigkeit gewichtetem F1, Precision und Recall pro Lemma, gemittelt über die 40 Lemmata. | S. 10076 bis 10077, Abschnitt 4.2 | eigene Methode |
| Nur übertragene Daten: 36,93 F1, gegenüber einer Zufallsbaseline von 17,64; mit SemEval-Daten kombiniert signifikant besser als SemEval allein (einseitiger t-Test auf Bootstrap-Ergebnissen, p < 0,01). | S. 10077, Tab. 2 | eigenes Ergebnis |
| Feine, nahe Senses (bei *credo* „believe a thing“ gegen „think, suppose“) bleiben für alle Modelle schwer. | S. 10078, Abschnitt 5.2 | eigenes Ergebnis (Einzelbeispiele) |
| Der Abstand zwischen SemEval- und übertragenen Daten erklärt sich vor allem durch verschiedene Abdeckung: 52 Senses kommen in SemEval, aber nicht in den übertragenen Daten vor; 11 umgekehrt. Der SemEval-Datensatz ist nach Lemmata und Zeiträumen ausbalanciert, Korpusdaten „in the wild“ nicht. | S. 10078 bis 10079, Abschnitt 6.1, Tab. 1 | eigenes Ergebnis, Deutung |
| Seltene Senses (weniger als 10 Trainingsbeispiele) sind schwer; zusätzliche übertragene Daten helfen dort am meisten, kosten aber Leistung bei häufigen Senses. | S. 10079 bis 10081, Abschnitt 6.2, Abb. 4 und 5 | eigenes Ergebnis |
| Grenzen: Annahme paralleler Sense-Verteilung zwischen Englisch und Latein; die Bewertung der Systemqualität sei schwierig „due to the low inter-annotator agreement“ und wegen feiner Sense-Unterscheidungen. | S. 10081, Abschnitt 7 | eigene Einschätzung, ohne Zahl |
| WSD-System als Hilfe, nicht als Ersatz für Fachurteil. | S. 10081, Abschnitt 8 | eigene Position |

## Daten, Methode, Zahlen

- **Tab. 1 (S. 10077), am Seitenbild geprüft:**

| | SemEval | Pers |
|---|---|---|
| Daten insgesamt | 2.400 | 6.020 |
| Lemmata | 40 | 33 |
| Senses | 125 | 84 |
| Senses nur in dieser Spalte (A \ B) | 52 | 11 |

- **Tab. 2 (S. 10077), am Seitenbild geprüft:**

| Trainingsdaten | F1 | Precision | Recall |
|---|---|---|---|
| SemEval | 60,30 | 55,63 | 67,15 |
| Pers_inter | 36,93 | 36,16 | 45,38 |
| Pers_align | 36,93 | 36,21 | 45,78 |
| SemEval + Pers_inter | 61,45* | 57,83 | 68,01 |
| SemEval + Pers_align | 61,48* | 57,46 | 68,00 |
| SemEval + Pers_rare | 61,83* | 58,17 | 67,93 |

  \* signifikant besser als SemEval allein (p < 0,01). Pers_rare: nur Senses, die in SemEval höchstens σ = 18-mal vorkommen (Durchschnitt der Sense-Häufigkeit) (S. 10076).
- **Training (S. 10077):** Lernrate 5e-5, Adam, 20 Epochen, eine Nvidia T4, im Mittel 37 Minuten. Englisches WSD-System AMuSE-WSD.
- **Vorverarbeitung (S. 10075):** Lemmatisierung und Wortartentagging mit Cracovia (Sieger EvaLatin 2022).
- **Annotation der Testdaten:** referiert, nicht selbst erhoben. Wie aus den DURel-Skalenwerten zu jeder Definition ein einzelnes Sense-Label für die Klassifikation wurde, sagt das Paper nicht. Keine Übereinstimmungswerte.
- **Unstimmigkeit:** Propagation_inter liefert laut Text 6.412 Sätze (S. 10075), Tab. 1 nennt für Pers (= Pers_inter, S. 10076) 6.020.

## Wörtliche Stellen

> „Also, valuating system quality presents challenges due to the low inter-annotator agreement, as well as the system’s granular sense distinctions, which may lead to divergent sense selections by different annotators for the same word occurrences.“ (S. 10081; „valuating“ so im Original)

> „[…] word sense disambiguation is a nuanced task for which a system like ours can be of help, but not a substitute for the opinion of an expert in the field.“ (S. 10081)

## Bezug zur Dissertation

- **`goldstandard/LITERATUR-IAA.md`, „LLMs bei historischen Sprachen“:** Dort steht, LLMs würden bei historischen Sprachen meist mit F1 gegen ein Gold ohne berichtete IAA gemessen, mit Ghinassi et al. 2024 als Beleg (○). Am Original: Das Paper nutzt **kein LLM**, sondern LatinBERT (Encoder, feinjustiert) und ein englisches WSD-System (S. 10076 bis 10077). Richtig ist der zweite Teil: gemessen wird gewichteter F1 gegen den SemEval-Datensatz, eine IAA wird nicht berichtet, nur als „low“ erwähnt (S. 10081). Als Beleg für LLM-Studien passt das Paper nicht; als Beleg für „Gold ohne berichtete IAA, bei eingeräumt niedriger Übereinstimmung“ passt es.
- **PROTOKOLL §9.1 Punkt 7 und §5 (Granularität):** Die Autor:innen nennen feine Sense-Unterscheidungen als Grund, warum Annotator:innen bei denselben Belegen verschieden wählen (S. 10081), und zeigen das an *credo* (S. 10078). Das stützt die zusätzliche Auswertung auf grober Ebene des Begriffssystems.
- **PROTOKOLL §9.2 (Macro-Genauigkeit, Nicht-MFS-Items):** Seltene Senses sind die eigentliche Schwäche, und Verbesserungen bei ihnen kosten bei häufigen (S. 10080 bis 10081). Das gewichtete F1 des Papers verdeckt das, weil es nach Sense-Häufigkeit gewichtet (S. 10077). Das stützt, Macro-Genauigkeit und Nicht-MFS-Items getrennt zu berichten.
- **`knowledge/data.md`, B9 und PROTOKOLL §6 (`KEINE_PASST`):** Senses, die in einer Datenquelle fehlen, kann ein darauf trainiertes System nie vergeben (S. 10079). Umgekehrt fanden die übertragenen Daten 11 Senses, die im Testset nicht vorkommen (S. 10079). Beides ist eine Parallele zu B9 (Senses ohne Silberbeleg) und zu der Frage, wie oft das Inventar nicht passt.
- **Inventarlücke bei kulturspezifischen Begriffen:** Römische Ämter und Eide (*consul*, *sacramentum*) und christliche Bedeutungen von *virtus* ließen sich nicht auf WordNet abbilden (S. 10074 bis 10075). Das ist ein Beleg aus einer anderen historischen Sprache dafür, dass ein gegenwartssprachliches Inventar historische Begriffe nicht abdeckt, und ein Argument für ein eigenes Inventar wie das MHDBDB-Begriffssystem.
- **PROTOKOLL §4.3 und §4.8 (Schichtung):** Der SemEval-Datensatz ist nach Lemma und Zeitraum ausbalanciert, Korpusdaten sind es nicht; die Autor:innen betonen, dass das die Werte verschiebt (S. 10079). Das ist ein Argument, die Schichtung des Goldstandards bei der Interpretation stets mitzuberichten.

## Grenzen und Einwände

- Kein LLM; Encoder mit Klassifikationsschicht pro Lemma. Für die Forschungsfrage der Dissertation nur Kontext.
- Keine MFS-Baseline, nur eine Zufallsbaseline (17,64, S. 10077). Ob das System die häufigste Bedeutung schlägt, lässt sich nicht ablesen.
- Testset sehr klein: jeder zehnte von 2.400 Sätzen, also etwa 240 Sätze für 40 Lemmata (S. 10075 bis 10076; die genaue Zahl steht nicht im Text).
- Wie die vierstufigen DURel-Urteile pro Definition zu einem Gold-Sense wurden, bleibt offen.
- Die Lemmaauswahl folgt dem Bedeutungswandel durch das Christentum, nicht der Polysemie; die Ergebnisse sind nicht auf eine Zufallsstichprobe von Lemmata übertragbar.
- Inneres Zahlenproblem 6.412 gegen 6.020 (siehe oben).

## Weiterführend

- McGillivray et al. 2022, „A new corpus annotation framework for Latin diachronic lexical semantics“, *Journal of Latin Linguistics* 21(1), S. 47 bis 105 (S. 10075, 10083): Annotationsverfahren und vermutlich die Übereinstimmungswerte des Testdatensatzes; für die IAA-Lücke nachschlagen.
- Schlechtweg et al. 2020, SemEval-2020 Task 1 (S. 10075, 10083); Schlechtweg, Schulte im Walde & Eckmann 2018, DURel (S. 10075, 10083): beide in `LITERATUR-IAA.md` mit ○.
- Pasini, Raganato & Navigli 2021, XL-WSD (S. 10073 bis 10074, 10083): war schon zur Beschaffung vorgeschlagen (`goldstandard/VORSCHLAEGE-2026-10.md`).
- Bamman & Burns 2020, Latin BERT; Lendvai & Wick 2022, TLL (S. 10073 bis 10074, 10082).
- Orlando et al. 2021, AMuSE-WSD (S. 10077, 10083).

## Julias Notizen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF und hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
