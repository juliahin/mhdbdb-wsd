# Schlechtweg, McGillivray, Hengchen, Dubossarsky & Tahmasebi 2020: SemEval-2020 Task 1

**Datei:** `pdf/Schlechtweg-etal-2020-SemEval-LSC.pdf` (nur lokal; 23 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, Textebene S. 1 bis 21 gelesen (Haupttext, Literatur, Anhang A, Anhang B teilweise; S. 21 bis 23 sind weitere Systembeschreibungen und Anhang C mit F1-Werten, nur überflogen). Tab. 4 (S. 5) am Seitenbild geprüft; Tab. 5 und 6 (S. 9, 11) nur an der Textebene. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology 2020.semeval-1.1 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: PDF-Seite = gedruckte Seite (S. 1 bis 23, Seitenzahl oben auf der Seite).

## Bibliografie

- **Vollständig:** Schlechtweg, Dominik, Barbara McGillivray, Simon Hengchen, Haim Dubossarsky & Nina Tahmasebi (2020). SemEval-2020 Task 1: Unsupervised Lexical Semantic Change Detection. In: Aurelie Herbelot, Xiaodan Zhu, Alexis Palmer, Nathan Schneider, Jonathan May & Ekaterina Shutova (Hg.), *Proceedings of the Fourteenth Workshop on Semantic Evaluation*. Barcelona (online): International Committee for Computational Linguistics, S. 1 bis 23.
- **DOI/URL:** 10.18653/v1/2020.semeval-1.1 (aufgelöst über doi.org und Crossref, 2026-11-16); https://aclanthology.org/2020.semeval-1.1/ (Herausgeber:innen, Verlag und Monat Dezember nach dem BibTeX der Anthology, abgerufen 2026-11-16). Im PDF: „Proceedings of the 14th International Workshop on Semantic Evaluation, pages 1–23, Barcelona, Spain (Online), December 12, 2020“ (S. 1). Vorher als arXiv 2007.11464 verbreitet (so in LITERATUR-IAA.md zitiert); diese Fassung nicht geprüft.
- **Lizenz:** CC BY 4.0 (Fußnote S. 1).
- **Art:** Konferenzbeitrag (Aufgabenbeschreibung eines Shared Task)
- **Sprache:** Englisch

## Worum es geht

Der erste SemEval-Shared-Task zur Erkennung lexikalischen Bedeutungswandels stellt für Englisch, Deutsch, Latein und Schwedisch je ein Korpuspaar aus zwei Zeiträumen und eine Liste von Zielwörtern bereit (S. 1 bis 3). Teilaufgabe 1 fragt binär, ob ein Wort eine Bedeutung gewonnen oder verloren hat, Teilaufgabe 2 verlangt eine Rangfolge nach dem Grad des Wandels (S. 2). Das Gold entsteht aus rund 100.000 menschlichen Urteilen zur Bedeutungsnähe von Belegpaaren auf der DURel-Skala, die zu einem Belegraph verbunden und in Bedeutungscluster zerlegt werden (S. 1, 4 bis 7). Für Latein ohne Muttersprachler:innen urteilten Fachleute stattdessen über Beleg und Wörterbuchdefinition, je Wort nur eine Person (S. 4 bis 5). 33 Teams reichten 186 Systeme ein; statische Wortvektoren schnitten überraschend besser ab als kontextuelle (S. 1, 10).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Evaluation ist das dringendste Problem der Forschung zum Bedeutungswandel, weil es keine Goldstandards gibt. | S. 1, Abstract und Abschnitt 1 | Einschätzung der Autor:innen |
| Zwei Teilaufgaben: binär (Bedeutung gewonnen oder verloren zwischen C1 und C2) und Rangfolge nach Grad des Wandels; die binäre Sicht ist für historische Linguistik und Lexikografie am wichtigsten. | S. 2, Abschnitt 2 | eigene Festlegung |
| Zielwörter: 100 bis 200 Wandelkandidaten aus etymologischen und historischen Wörterbüchern, von einer Person an je 50 Belegen aus C1 und C2 geprüft; dazu stabile Kontrollwörter mit gleicher Wortart und ähnlicher Häufigkeitsentwicklung. | S. 3, Abschnitt 3.2 | eigenes Verfahren |
| Annotation (Englisch, Deutsch, Schwedisch): 9 / 8 / 5 Muttersprachler:innen, (ehemalige) Studierende; je Wort 100 Belege pro Zeitraum; Paare auf der DURel-Skala 1 bis 4 bewertet, in zufälliger Reihenfolge, ohne dass die Personen das Clustering sahen. | S. 4, Abschnitt 4 | eigenes Verfahren, Skala referiert (Schlechtweg et al. 2018; Erk et al. 2013) |
| DURel „produces high inter-annotator agreement even between non-expert annotators relying on the simple notion of semantic relatedness“. | S. 4 | Einschätzung der Autor:innen |
| Kanten werden in mehreren Runden ausgewählt (Kombination mit bestehenden Clustern, Erkundung, Nachannotation bei Abweichung ≥ 2 oder Median ≈ 2,5); etwa die Hälfte der Paare von mehr als einer Person bewertet; Urteile 0 („nicht entscheidbar“) führen ab mehr als der Hälfte zum Entfernen des Belegs. | S. 4, Anhang A.1 (S. 18) | eigenes Verfahren |
| **Latein:** keine Muttersprachler:innen; 10 Annotator:innen mit hohen Lateinkenntnissen (Studierende bis Senior Researchers). Im Probedurchlauf berichteten sie Schwierigkeiten und dass sie beim Vergleich zweier Textstellen in ihre Muttersprache übersetzen mussten. Deshalb Urteil über die Nähe von **Beleg und Wörterbuchdefinition** (Logeion) auf der DURel-Skala, nach Erk et al. 2013; 30 Belege pro Zeitraum; je Wort nur eine Person. | S. 4 bis 5, Abschnitt 4.2 | eigenes Verfahren |
| Clustering: Kantengewichte um 2,5 verschoben (3 und 4 eher gleiche, 1 und 2 eher verschiedene Bedeutung, nach Blanks Kontinuum); Korrelationsclustering minimiert positive Kanten zwischen und negative Kanten innerhalb von Clustern; Zahl der Cluster ergibt sich selbst. | S. 5 bis 6, Abschnitt 4.3 | eigenes Verfahren |
| Wandelmaße: binär, wenn eine Bedeutung in einem Zeitraum höchstens k-mal und im anderen mindestens n-mal belegt ist (Latein k = 0, n = 1; sonst k = 2, n = 5); graduell als Jensen-Shannon-Distanz der Bedeutungsverteilungen. | S. 6 bis 7, Abschnitt 4.4 | eigenes Verfahren |
| Übereinstimmung (mittleres paarweises Spearman ρ, erste Runde): Englisch 0,69, Deutsch 0,59, Schwedisch 0,58, **Latein keine**; über alle Runden gewichtet 0,52 / 0,60 / – / 0,58. In späteren Runden sinkt sie, weil gezielt strittige Paare nachannotiert wurden. | S. 5, Tab. 4; S. 7, Anm. 13 | eigenes Ergebnis |
| Vergleich: Erk et al. 2013 und Schlechtweg et al. 2018 berichten 0,55 bis 0,68, „comparable to our scores“. | S. 7 | Vergleich der Autor:innen |
| Rund 100.000 Urteile, etwa 1.000 Stunden, rund 20.000 Euro, doppelt so viel wie geplant. | S. 7 | eigene Angabe |
| Die Testdaten sind nicht nach Polysemie kontrolliert; der graduelle Wandel korreliert stark mit der Mindestzahl der Bedeutungen (PLYm 0,72 / 0,73 / 0,31 / 0,75 für EN / DE / LA / SV). | S. 5, Tab. 4; S. 7, 11 | eigenes Ergebnis |
| Bestes System Teilaufgabe 1 (Genauigkeit, Mittel über vier Sprachen) 0,687, Teilaufgabe 2 (Spearman) 0,527; Latein liegt bei vielen Systemen niedriger. | S. 9, Tab. 5 | eigenes Ergebnis |
| Statische Vektoren schlagen kontextuelle: unter den besten 10 Systemen 7 bzw. 8 mit statischen, 2 mit kontextuellen Vektoren. Mögliche Gründe: keine Konventionen für kontextuelle Modelle, Vortraining auf fremden Daten, gemischte Sätze und Lemmatisierung der Korpora. | S. 10, Tab. 6 (S. 11) | eigenes Ergebnis, Deutung der Autor:innen |
| Tote Sprachen sind schwieriger: weniger Ressourcen, keine Muttersprachler:innen, hohe Variation, uneinheitliche Schreibung, OCR-Fehler; Verfahren sind für lebende Sprachen entwickelt. | S. 10 | Deutung, referiert (Piotrowski 2012) |
| Modelle sind trotz kontrollierter Häufigkeit stark häufigkeitsabhängig (Korrelationen teils > 0,8); für schwer vorherzusagende Wörter fand sich kein Muster bei Häufigkeit oder Polysemie. | S. 10 bis 11 | eigenes Ergebnis |

## Daten, Methode, Zahlen

- **Korpora (Tab. 2, S. 3):** Englisch CCOHA 1810 bis 1860 / 1960 bis 2010; Deutsch DTA 1800 bis 1899 / BZ und ND 1946 bis 1990; Latein LatinISE −200 bis 0 / 0 bis 2000 (1,7 / 9,4 Mio. Tokens); Schwedisch Kubhist 1790 bis 1830 / 1895 bis 1903. Lemmatisiert, Wortart getaggt; CCOHA und DTA schreibnormalisiert; BZ, ND und Kubhist mit häufigen OCR-Fehlern (S. 2). Sätze für die Veröffentlichung gemischt und lemmatisiert, aus urheberrechtlichen Gründen (S. 3, Anm. 3).
- **Tab. 4 (S. 5, am Seitenbild geprüft):** Zielwörter n = 37 / 48 / 40 / 31 (EN / DE / LA / SV); Nomen/Verben/Adjektive 33/4/0, 32/14/2, 27/5/8, 23/5/3; AGR 0,69 / 0,59 / – / 0,58; beurteilte Paare 30k / 38k / 9k / 20k; Anteil Wandel (binär) 0,43 / 0,35 / 0,65 / 0,26.
- **Annotator:innen mit historisch-linguistischem Hintergrund:** Deutsch zwei, Englisch und Schwedisch je eine (S. 4).
- **Simulation (Anhang A.3, S. 18 bis 19):** 40 simulierte Belegraphen; die wahre Clusterung wurde mit einem mittleren angepassten Rand-Index über 0,96 wiedergefunden; im Mittel 5 Runden und rund 8.000 Urteile pro Person.
- Für Teilaufgabe 1 wurde Genauigkeit gewählt, weil eine ausgewogene Klassenverteilung erwartet war; da sie es nicht wurde, steht F1 zusätzlich in Anhang C (S. 8).

## Wörtliche Stellen

> „In a trial annotation task our annotators reported difficulties and that they had to translate to their native language when comparing two excerpts of text.“ (S. 5)

> „Due to the challenge of finding qualified annotators, each word was assigned only to one annotator.“ (S. 5)

> „We found that change scores in our test sets strongly correlate with polysemy, despite model predictions not showing such strong influence.“ (S. 12)

## Bezug zur Dissertation

**1. A31 und offener Punkt 22 (Weg C: inventarfreie Aufgabe).** Der Task zeigt Weg C im großen Maßstab und zugleich seine Grenze für eine Sprache ohne Muttersprachler:innen: Für Latein musste das Verfahren von Belegpaaren auf „Beleg gegen Wörterbuchdefinition“ umgestellt werden, weil die Fachleute zwei Textstellen nur über eine Übersetzung in die eigene Sprache vergleichen konnten (S. 5). Damit kehrte das Latein-Gold zu einem Inventar zurück, nur mit graduellem Urteil statt Wahl. Für Mittelhochdeutsch spricht das dafür, Weg C nicht als reine Paaraufgabe zu planen, sondern zuerst im Pilot zu prüfen, ob Julia und Alan Belegpaare ohne Übersetzung vergleichen können. Das ist eine Folgerung, kein Befund der Arbeit; Mittelhochdeutsch ist nicht untersucht.

**2. A31 (Vorgabe des Inventars).** Die Arbeit vergleicht beide Verfahren nicht an denselben Daten; sie belegt keinen Einfluss des Inventars auf das Urteil. Sie ist für A31 nur als Beispiel brauchbar, dass bei fehlender Sprecherintuition ein Inventar als Stütze dient.

**3. PROTOKOLL §7 (Annotator:innen) und LITERATUR-IAA.md, Abschnitt „Historische Sprachen“.** Bestätigt am Volltext: „SemEval-2020 Task 1 musste Latein auf eine Annotator:in pro Wort umstellen, also ohne IAA“ (S. 5, Tab. 4) und „SemEval Runde 1 ρ ≈ 0,58 bis 0,69“ (Tab. 4). Präziser: Der Grund für eine Person pro Wort war der Mangel an qualifizierten Annotator:innen, der Wechsel zu Definitionen hatte einen anderen Grund (Übersetzungszwang beim Paarvergleich, S. 5). Beides ist für den Status ✔ in LITERATUR-IAA.md vorzuschlagen (derzeit ○). Dort ist das Werk als arXiv 2007.11464 zitiert; die begutachtete Fassung ist SemEval 2020, S. 1 bis 23 (oben).

**4. PROTOKOLL §4.3 und §9.1 Punkt 6 (Polysemie als Faktor).** Der Befund, dass Wandelwerte stark mit Polysemie korrelieren, obwohl nicht danach geschichtet wurde, und die Forderung, Testdaten künftig nach Polysemie zu kontrollieren (S. 12), stützt die Schichtung des Protokolls nach Polysemie. Für die Vorhersageschwierigkeit fand sich dagegen kein Muster nach Häufigkeit oder Polysemie (S. 11).

**5. Forschungsfrage, Nebenfrage „Wie oft passt keine Bedeutung des Inventars?“ (§1) und Diachronie.** Die Arbeit liefert ein Verfahren, Bedeutungen ohne Inventar aus Urteilen zu gewinnen (Clustering des Belegraphs, S. 5 bis 6). Das wäre ein möglicher späterer Schritt, um `KEINE_PASST`-Fälle zu ordnen; für den Goldstandard selbst ist es zu aufwendig (rund 1.000 Stunden für vier Sprachen, S. 7).

**6. Kontamination und Datenschutz der Labels (§10).** Nebenbefund: Die Korpora wurden aus urheberrechtlichen Gründen gemischt und lemmatisiert veröffentlicht, die Labels erst nach der Auswertungsphase (S. 3). Das ist ein Beispiel für zurückgehaltene Labels, nicht für Schutz vor Trainingsnutzung.

**7. Encoder-Vergleich (§1, „späterer, eigener Schritt“).** Der Befund, dass kontextuelle Vektoren statischen unterlagen (S. 10), betrifft Wandelerkennung über Korpora, nicht WSD; für einen späteren Encoder-Vergleich ist er höchstens ein Hinweis, dass vortrainierte Modelle auf historischen Daten nicht selbstverständlich besser sind.

## Grenzen und Einwände

- Für Latein gibt es keine Übereinstimmungswerte; das Gold hängt pro Wort an einer Person (S. 5).
- Die Übereinstimmung ist nur für die erste Runde berichtet; über alle Runden liegt sie niedriger (S. 7, Anm. 13). Keine Zufallskorrektur.
- Kleine Testmengen (31 bis 48 Wörter pro Sprache); die Autor:innen sagen das selbst (S. 12).
- Die Zielwörter sind nach Wörterbuchangaben vorgewählt und nach Häufigkeit, nicht nach Polysemie ausgeglichen (S. 3, 7).
- Das Deutsch-Gold betrifft Neuhochdeutsch des 19. und 20. Jahrhunderts; Mittelhochdeutsch kommt nicht vor.
- Systemergebnisse sind Stand 2020, ohne LLMs.

## Weiterführend

- Schlechtweg & Schulte im Walde 2020, Simulating lexical semantic change from sense-annotated data, EvoLang13 (S. 2, 3, 6): Herkunft der Wandeldefinitionen und der SemCor-LSC-Entwicklungsdaten.
- Hätty, Schlechtweg & Schulte im Walde 2019, SURel, *SEM (S. 4): Erweiterung von DURel.
- McGillivray & Kilgarriff 2013, LatinISE-Korpus (S. 2).
- Piotrowski 2012, *Natural Language Processing for Historical Texts*, Morgan & Claypool (S. 10): Schwierigkeiten historischer und toter Sprachen.
- Clackson 2011, *A Companion to the Latin Language* (S. 4): Quelle der lateinischen Wandelwörter.
- Tahmasebi, Borin & Jatowt 2018 und Kutuzov et al. 2018 (S. 1): Überblicke zum Bedeutungswandel.
- McGillivray et al. 2019, A computational approach to lexical polysemy in Ancient Greek, *DSH* 34(4) (S. 1).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
