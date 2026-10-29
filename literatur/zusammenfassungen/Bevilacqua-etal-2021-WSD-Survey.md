# Bevilacqua, Pasini, Raganato & Navigli 2021: Recent Trends in Word Sense Disambiguation

**Datei:** `pdf/Bevilacqua-etal-2021-WSD-Survey.pdf` (nur lokal; 9 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganze Textebene gelesen, Tabellen 1 und 2 am Seitenbild geprüft, DOI aufgelöst. Das lokale PDF ist byte-gleich mit dem PDF auf ijcai.org (SHA-256 verglichen am 2026-10-28), also die Verlagsfassung; es enthält keine Markierungen.

Seitenzählung: Das PDF trägt keine Seitenlabels, aber gedruckte Seitenzahlen in der Fußzeile. PDF-Seite n = gedruckte S. 4329 + n (PDF 1 = S. 4330, PDF 9 = S. 4338). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Bevilacqua, Michele, Tommaso Pasini, Alessandro Raganato & Roberto Navigli (2021). Recent Trends in Word Sense Disambiguation: A Survey. In: Zhi-Hua Zhou (Hg.), *Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI-21)*, Survey Track. International Joint Conferences on Artificial Intelligence Organization, S. 4330 bis 4338.
- **DOI/URL:** https://doi.org/10.24963/ijcai.2021/593 (aufgelöst auf https://www.ijcai.org/proceedings/2021/593). Seiten, Survey Track und Herausgeber aus dem BibTeX von ijcai.org ✔; Crossref: S. 4330 bis 4338, August 2021, Konferenzort laut Crossref Montreal, 19. bis 27.8.2021 ✔. Kopfzeile jeder Seite: „Proceedings of the Thirtieth International Joint Conference on Artificial Intelligence (IJCAI-21), Survey Track“ ✔.
- **Lizenz:** keine offene Lizenz angegeben. Die Seite auf ijcai.org nennt nur „© 2026 International Joint Conferences on Artificial Intelligence“, Crossref führt keine Lizenz (beides abgerufen 2026-10-28). Frei lesbar, aber nicht unter CC.
- **Art:** Konferenzbeitrag (Survey Track, begutachtet)
- **Sprache:** Englisch

## Worum es geht

Ein Überblick über WSD um 2021, ausdrücklich als Nachfolger der älteren Surveys (Ide & Véronis 1998, Agirre & Edmonds 2007, Navigli 2009) gedacht, die über zehn Jahre alt seien (S. 4330). Die Autoren beschreiben Inventare und annotierte Daten (§2), wissensbasierte und überwachte Verfahren (§3), stellen Ergebnisse aus der Literatur auf dem englischen Rahmen von Raganato et al. 2017 und dem mehrsprachigen XL-WSD zusammen (§4) und skizzieren Aufgaben jenseits fester Inventare (§5). Kernbefund: Vortrainierte Sprachmodelle und Glossen haben die Werte über die „80 % glass ceiling“ der Annotator:innen-Übereinstimmung gehoben; damit werde fraglich, was solche Werte bedeuten, und die Benchmarks zeigten ihre Grenzen (S. 4330, 4336).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Neue Verfahren hätten die Leistung über die „80% glass ceiling set by the inter-annotator agreement“ gehoben. | S. 4330, Abstract | Einschätzung der Autoren, gestützt auf Literaturwerte |
| WSD bildet einen Ausdruck auf „one (or potentially more)“ seiner möglichen Senses ab. | S. 4330, §1 | Definition |
| Inventare betreffen vor allem offene Wortklassen (Nomen, Verben, Adjektive, Adverbien). Ein Lexem ist ein Paar ⟨Lemma, Wortart⟩. Das Inventar ist groß, aber dünn: Jedes Lexem hat nur wenige Senses. | S. 4330, §1 mit Anm. 1 | Definition |
| Hybride Verfahren (überwacht plus Wissensbasis) liefern die höchsten Werte; rein wissensbasierte sind schlechter als überwachte. | S. 4330, §1; S. 4334, §4.2 | referiert und eigene Zusammenstellung |
| WSD ist wissensintensiv und braucht zweierlei: Inventare und annotierte Korpora. | S. 4331, §2 | Einordnung |
| WordNet 3.0 hat 117.659 Synsets; English WordNet 2020 ergänzt ca. 3.000; BabelNet 5.0 deckt 500 Sprachen mit über 20 Mio. Synsets ab. | S. 4331, §2.1 | referiert |
| **Feinkörnigkeit:** Alle gängigen Inventare leiden darunter, dass Bedeutungen „sometimes, hard to discriminate between even for humans“ sind (WordNet: 29 Senses für *line*). Grobere Inventare (Hovy et al. 2006; Lacerra et al. 2020) sind nicht Standard geworden, auch wegen geringer Abdeckung. | S. 4331, §2.1 | Einschätzung, Beispiele referiert |
| **Aufzählbarkeit:** Inventare unterstellen, Bedeutung lasse sich als endliche Liste fassen und Sprache sei statisch. | S. 4331, §2.1 | Einschätzung |
| SemCor: größter von Hand annotierter Datensatz, 200.000 Annotationen, deckt nur 22 % der knapp 118.000 Synsets; als Teil des Brown Corpus der 1960er hat er eine andere Sense-Verteilung als Gegenwartstexte. | S. 4331, §2.2 | referiert (Zahl weicht von Raganato et al. 2017 ab, dort 226.036) |
| Handannotierte Trainingsdaten fehlen für die meisten Sprachen außer Englisch; übersetzte SemCor-Fassungen sind teils nicht mehr verfügbar. | S. 4331, §2.2 | Einschätzung |
| Evaluation läuft meist auf dem Rahmen von Raganato et al. 2017a; für seltene Senses gibt es FEWS (Wiktionary). XL-WSD erweitert den Rahmen auf 18 Sprachen, darunter Deutsch, mit über 99.000 Goldannotationen, Inventar BabelNet 4.0. | S. 4331 bis 4332, §2.2 | referiert |
| Bei der Vorhersage wird nur unter den möglichen Senses des Worts V(w) gewählt (Gl. 3). | S. 4332, §3.2 | Beschreibung |
| Binäre Kreuzentropie erlaubt, mehrere Annotationen einer Instanz zu berücksichtigen statt nur einer Gold-Sense (Conia & Navigli 2021). | S. 4333, §3.2 | referiert |
| Viele Senses kommen wegen extremer Klassenungleichheit in Trainingskorpora gar nicht vor. | S. 4333, §3.2 | Einschätzung |
| Glossen (Definitionen) steigern WSD deutlich; die besten Systeme kodieren Glossen als Sequenz (ESCHER, BEM, Yap et al.). | S. 4333; S. 4335, §4.2 | referiert |
| Relationen im Inventar: Vial et al. 2019 verringern die Zahl der Ausgabeklassen, indem sie jeden Sense auf einen Vorfahren in der WordNet-Taxonomie abbilden. | S. 4334, §3.2 | referiert |
| **Obergrenze:** Als typische Obergrenze gilt die Annotator:innen-Übereinstimmung, „the percentage of words tagged with the same sense by two or more human annotators“; für feinkörnige Inventare auf 67 bis 80 % geschätzt (nach Navigli 2009). Diese Werte verlangten neue Studien für „more centered estimates of human performance, e.g., on up-to-date benchmarks“. | S. 4334, §4.1 | referiert, mit eigener Einschränkung |
| Vortrainierte Sprachmodelle sind entscheidend; rein wissensbasierte Verfahren liegen 7,2 Punkte hinter dem besten überwachten (SREF_KB gegenüber ESCHER). | S. 4334, §4.2 | eigene Zusammenstellung |
| Zusätzliche, auch verrauschte Trainingsdaten (WNG) bringen 1,8 bis 2,6 F1-Punkte. | S. 4334, §4.2 | referiert |
| Mehrsprachig: Ein nur auf englischem SemCor trainiertes XLM-R schlägt sprachspezifisch auf Silberdaten trainierte Modelle und das wissensbasierte SyntagRank; die Werte bleiben aber „mostly underwhelming“ gegenüber Englisch. | S. 4335, §4.2; Tab. 2 (S. 4336) | eigene Zusammenstellung |
| Grenzen der Aufgabe: Ein diskretes Inventar skaliert nicht auf neue und kreative Verwendungen und legt eine Granularität fest, die für die Anwendung ungünstig sein kann. Alternativen: Word-in-Context, lexikalische Substitution, Definitionsgenerierung. | S. 4335 bis 4336, §5 | Einschätzung |
| Die besten englischen Modelle liegen „close to or superior to the human upper bound, posing the question of how to interpret such performance“; die Aufgabe sei trotzdem nicht gelöst, Benchmarks würden unzureichend, nötig seien neue schwierige Testsets und Studien zu anderen Sense-Verteilungen und Sprachen. | S. 4336, §6 | Einschätzung |

## Daten, Methode, Zahlen

Keine eigenen Experimente; alle Werte aus der Literatur gesammelt (S. 4334).

**Tab. 1 (S. 4335, am Seitenbild geprüft):** F1 auf dem Rahmen von Raganato et al. 2017, alle überwachten Systeme nur auf SemCor trainiert. Auswahl (ALL / SE2 / SE3 / SE07 / SE13 / SE15):

| System | Art | ALL | SE2 | SE3 | SE07 | SE13 | SE15 |
|---|---|---|---|---|---|---|---|
| SyntagRank | wissensbasiert | 71,7 | 71,6 | 72,0 | 59,3 | 72,2 | 75,8 |
| SREF_KB | wissensbasiert | 73,5 | 72,7 | 71,5 | 61,5 | 76,4 | 79,5 |
| LMMS | 1-nn | 75,4 | 76,3 | 75,6 | 68,1 | 75,1 | 77,0 |
| EWISE | Token-Klassifikator | 71,8 | 73,8 | 71,1 | 67,3 | 69,4 | 74,5 |
| BEM | Token-Klassifikator | 79,0 | 79,4 | 77,4 | 74,5 | 79,7 | 81,7 |
| GlossBERT | Sequenz | 77,0 | 77,7 | 75,2 | 72,5 | 76,1 | 80,4 |
| ESCHER | Sequenz | **80,7** | 81,7 | 77,8 | 76,3 | 82,2 | 83,2 |

SemEval-07 bleibt für alle Systeme der schwerste Datensatz.

**Tab. 2 (S. 4336, am Seitenbild geprüft):** F1 auf XL-WSD. Deutsch: XLM-R-L zero-shot 83,18; XLM-R-L auf übersetztem SemCor+WNG 73,78; SyntagRank 75,99. Micro-F1 über alle Sprachen: 65,66 (zero-shot) gegenüber 57,68 (SyntagRank). Niedrigste Werte: Baskisch 47,15, Katalanisch 49,97.

## Wörtliche Stellen

> „[…] breaching the 80% glass ceiling set by the inter-annotator agreement.“ (S. 4330)

> „Each of these inventories suffers from the so-called fine-granularity problem, that is, different meanings of the same lexeme are, sometimes, hard to discriminate between even for humans.“ (S. 4331)

> „The IAA over a fine-grained sense inventory is estimated to be around 67-80% accuracy [Navigli, 2009]; these figures, however, call for further studies so as to obtain more centered estimates of human performance, e.g., on up-to-date benchmarks.“ (S. 4334)

> „The best models for English WSD attain results that are close to or superior to the human upper bound, posing the question of how to interpret such performance.“ (S. 4336)

## Bezug zur Dissertation

- **PROTOKOLL §9.2, „Die menschliche IAA ist die Obergrenze“:** Das Survey bestätigt die Konvention (S. 4334), zeigt aber zugleich, dass Systeme diese Grenze im Englischen erreicht oder überschritten haben (S. 4330, 4336), und nennt die Schätzung 67 bis 80 % selbst unsicher. Vorschlag: im Protokoll von Referenz- oder Vergleichswert sprechen statt von harter Obergrenze; ein LLM-Wert über der menschlichen IAA wäre dann kein Widerspruch, sondern auslegungsbedürftig.
- **PROTOKOLL §9.1, Punkt 2 (Rohübereinstimmung mit Genauigkeit vergleichbar):** Die IAA ist hier als Prozentanteil übereinstimmend getaggter Wörter definiert (S. 4334), also als Rohübereinstimmung. Das stützt, sie neben α zu berichten.
- **PROTOKOLL §3 und §4.3 (Einheit „Paar aus Lemma und Wortart“):** Das Survey definiert das Lexem genauso, als ⟨Lemma, Wortart⟩ (S. 4330, Anm. 1).
- **PROTOKOLL §9.1, Punkt 7 (zwei Ebenen des Begriffssystems):** Feinkörnigkeit als Kernproblem (S. 4331) und Vial et al. 2019, die Senses auf Vorfahren in der Taxonomie abbilden (S. 4334), sind Präzedenzfälle für eine grobe Auswertungsebene über Oberbegriffe.
- **PROTOKOLL §6, Status `MEHRERE`:** WSD als Abbildung auf „one (or potentially more)“ Senses (S. 4330) und das Training mit mehreren Gold-Senses (Conia & Navigli 2021, S. 4333) zeigen, dass Mehrfachlabels in der WSD-Literatur vorgesehen sind.
- **PROTOKOLL §6, Status `KEINE_PASST`, und §9.2 „Ausweichlabels als Ergebnis“:** Die Kritik an endlichen, statischen Inventaren (S. 4331, 4335) liefert die allgemeine Begründung, warum ein Status für Inventarlücken nötig ist.
- **PROTOKOLL §3 (MFS aus D1 auf D0 angewandt):** Der Hinweis, dass SemCor als Text der 1960er eine andere Sense-Verteilung hat als Gegenwartstexte (S. 4331), ist das englische Gegenstück zur benannten Verschiebung zwischen Silber-Domäne und Zielkorpus.
- **`knowledge/data.md`, B9 (42 % der Senses polysemer Lemmata nie im Silber belegt):** Das Survey nennt fehlende Senses im Training als allgemeines Problem der Klassenungleichheit (S. 4333).
- **PROTOKOLL §5 (nur Begriffsnamen, keine Definitionen):** Die stärksten Systeme nutzen Glossen (S. 4333, 4335). Die MHDBDB-Senses haben fast keine Definitionen (`knowledge/data.md`, B13). Daraus folgt kein Befund über LLMs, aber eine Einschränkung beim Vergleich mit englischen Werten: Die Karten bieten weniger Information als WordNet-Glossen.
- **Deutsch:** XL-WSD hat deutsche Testdaten mit BabelNet-Inventar (S. 4332, Tab. 2); für Gegenwartsdeutsch, nicht für Mittelhochdeutsch.
- **LLM-Prompting kommt nicht vor.** Das Survey ist von 2021; generative Verfahren erscheinen nur als Definitionsgenerierung (Generationary, S. 4333, 4336). Für den Stand der LLM-WSD sind die neueren Arbeiten in `pdf/` (Yae et al. 2025, Basile et al. 2025, Meconi et al. 2025) zuständig.

## Grenzen und Einwände

- Kurzes Survey (9 Seiten) mit Schwerpunkt auf Arbeiten der Sapienza-Gruppe der Autoren; keine systematische Literaturauswahl beschrieben.
- Alle Zahlen sind übernommen, nicht nachgerechnet; die Systeme wurden nicht unter gleichen Bedingungen neu ausgeführt (S. 4334).
- Die IAA-Schätzung 67 bis 80 % ist eine Sekundärangabe (Navigli 2009); die Autoren räumen selbst ein, dass aktuelle Messungen fehlen (S. 4334). Ob „über der menschlichen Obergrenze“ bei verschiedenen Maßen (F1 gegen Rohübereinstimmung) überhaupt vergleichbar ist, diskutiert das Survey nicht.
- Historische Sprachstufen kommen nicht vor; die Abhängigkeit von Glossen, großen Trainingskorpora und WordNet/BabelNet trifft auf das MHDBDB-Begriffssystem nicht zu.
- Bibliografische Schwächen im Werk: Ide & Véronis 1998 erscheint als „[Nancy and Jean, 1998]“ (S. 4330, 4338); Agirre & Edmonds wird als 2007, Band 33 zitiert (S. 4336); SemCor mit 200.000 Annotationen statt 226.036 wie bei Raganato et al. 2017.

## Weiterführend

- Navigli 2009 (S. 4334, 4338): Quelle der IAA-Schätzung 67 bis 80 %; liegt zusammengefasst vor (`zusammenfassungen/Navigli-2009-WSD-Survey.md`), dort die Stelle prüfen.
- Pasini, Raganato & Navigli 2021, XL-WSD, AAAI (S. 4332, 4338): mehrsprachiger Rahmen mit deutschen Testdaten.
- Blevins, Joshi & Zettlemoyer 2021, FEWS, EACL (S. 4332, 4337): seltene Senses.
- Conia & Navigli 2021, WSD als Mehrfachlabel-Problem, EACL (S. 4333, 4337): für `MEHRERE`.
- Lacerra et al. 2020, CSI: grobes Sense-Inventar, AAAI (S. 4331, 4337); Hovy et al. 2006, OntoNotes (S. 4331): für die grobe Ebene.
- Vial, Lecouteux & Schwab 2019, Sense-Vokabular-Kompression über WordNet-Vorfahren, GWNC (S. 4334, 4338).
- Maru et al. 2019, SyntagNet (S. 4332); Navigli 2018 (S. 4336).
- Pilehvar & Camacho-Collados 2019, WiC, NAACL (S. 4335, 4338).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem PDF von ijcai.org und hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
