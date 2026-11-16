# Pasini, Raganato & Navigli 2021: XL-WSD, ein mehrsprachiger Evaluationsrahmen für WSD

**Datei:** `pdf/Pasini-etal-2021-XL-WSD.pdf` (nur lokal; 9 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen; Tab. 1 und Tab. 3 am Seitenbild (PDF-Seiten 5 und 6) geprüft, Tab. 2 und 4 aus der Textebene (digital gesetzt). Das lokale PDF trägt Kopf- und Fußzeilen der AAAI-21-Proceedings und deren Seitenzahlen; ein Abgleich mit dem Verlags-PDF war nicht möglich, weil die AAAI-Seite den automatischen Abruf am 2026-11-16 blockierte. Keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 13647 + n (PDF 1 = S. 13648, PDF 9 = S. 13656). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Pasini, Tommaso, Alessandro Raganato & Roberto Navigli (2021). XL-WSD: An Extra-Large and Cross-Lingual Evaluation Framework for Word Sense Disambiguation. *Proceedings of the AAAI Conference on Artificial Intelligence* 35(15), S. 13648 bis 13656.
- **DOI/URL:** https://doi.org/10.1609/aaai.v35i15.17609 (Crossref: Band 35, Heft 15, S. 13648 bis 13656, veröffentlicht 18.05.2021, Verlag AAAI; die DOI leitet auf https://ojs.aaai.org/index.php/AAAI/article/view/17609 weiter, abgerufen 2026-11-16). Fußzeile S. 13648: „The Thirty-Fifth AAAI Conference on Artificial Intelligence (AAAI-21)“ ✔.
- **Lizenz:** keine offene Lizenz. Im PDF: „Copyright © 2021, Association for the Advancement of Artificial Intelligence (www.aaai.org). All rights reserved.“ (S. 13648); Crossref ohne Lizenzangabe.
- **Art:** Konferenzbeitrag (AAAI-21)
- **Sprache:** Englisch
- **Daten und Code:** https://sapienzanlp.github.io/xl-wsd/ (S. 13648, 13654; nicht aufgerufen).
- Pasini und Raganato sind gleichberechtigte Erstautoren (Anm., S. 13648).

## Worum es geht

Mehrsprachige WSD hatte keinen einheitlichen Evaluationsrahmen: Die SemEval-Daten anderer Sprachen nutzen verschiedene, teils veraltete oder nicht mehr verfügbare Inventare (S. 13648 bis 13649). XL-WSD vereinheitlicht Test- und Entwicklungsdaten in 18 Sprachen auf ein gemeinsames Inventar aus BabelNet-4.0-Synsets mit Princeton-WordNet-Bezug, gewinnt für 13 Sprachen neue Testdaten automatisch aus den Beispielsätzen nationaler WordNets und erzeugt maschinell übersetzte Trainingsdaten (S. 13650 bis 13651). Mehrsprachige Sprachmodelle, nur auf Englisch trainiert (zero-shot), schlagen meist die Modelle mit sprachspezifischen Trainingsdaten und die wissensbasierten Systeme; XLM-R Large erreicht im Mittel 65,66 F1 außerhalb des Englischen, rund 10 Punkte unter Englisch (S. 13653 bis 13654). Für Deutsch liegt XLM-R Large bei 83,18, die Baseline des häufigsten Sense bei 75,99 (Tab. 3).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Mehrsprachige WSD drehte sich jahrelang um vier europäische Sprachen (Französisch, Deutsch, Italienisch, Spanisch); vorhandene Goldstandards nutzen verschiedene Formate und veraltete oder nicht mehr verfügbare Inventare. | S. 13648, Einleitung | Problemstellung |
| Gemeinsames Inventar: 117.659 BabelNet-4.0-Synsets mit mindestens einem Princeton-WordNet-3.0-Sense; Kandidaten pro Paar aus Lemma und Wortart sind alle Synsets dieser Wortart, die das Lemma als Lexikalisierung enthalten. | S. 13650, Sense Inventory | eigenes Verfahren |
| Die Autoren räumen ein, dass die Bindung anderer Sprachen an die Begriffe des englischen WordNet kein getreues Gegenstück zu einem Wörterbuch dieser Sprachen ist; sie nehmen das für einen gemeinsamen, sprachübergreifenden Vergleich in Kauf. | S. 13650 | eigene Einschränkung |
| **Neue Testdaten für 13 Sprachen** aus den Beispielsätzen nationaler WordNets: Zielwort ist das Wort des Beispiels mit derselben Wortart wie das Synset, das eine seiner Lexikalisierungen ist; bei mehr als einem Kandidaten wird der Satz verworfen. Die Zuordnung zum gemeinsamen Inventar erfolgt über vorhandene Abbildungen. | S. 13650, Gold Standards | eigenes, automatisches Verfahren |
| Übernommene SemEval-Daten: Italienisch und Chinesisch (SemEval-2010), Französisch, **Deutsch**, Italienisch, Spanisch (SemEval-2013, Texte aus den WMT-Workshops 2010 bis 2012), Italienisch und Spanisch (SemEval-2015). Das niederländische Inventar von SemEval-2010 ist nicht mehr verfügbar. | S. 13650, SemEval datasets, Anm. 4 | Datenübernahme |
| Bereinigung: Abbildung von WordNet 1.6 und 2.1 auf 3.0 über automatische Mappings (nur höchste Konfidenz) und von älteren BabelNet-Fassungen auf 4.0; nicht abbildbare Instanzen werden entfernt. | S. 13650 bis 13651, Data cleaning | eigenes Verfahren |
| Aufteilung: pro Sprache alle Instanzen zufällig 80 % Test, 20 % Entwicklung. Englisch: feiner Testsatz (English-F: Senseval-2, Senseval-3, SemEval-2010, -2013, -2015) und grober (English-C: der grobe SemEval-2007-Datensatz von Navigli et al. 2007); Entwicklung auf SemEval-2007. | S. 13651, Evaluation split | eigenes Design |
| Silberne Trainingsdaten für 15 Sprachen: SemCor und WordNet-Glossen maschinell übersetzt (Opus-MT), Sense-Annotation auf Synonyme in der Übersetzung übertragen, nur bei gleicher Wortart in Quelle und Ziel. | S. 13651, Training Data | eigenes Verfahren |
| Polysemie der Testsets streut stark: Kroatisch 1,24, Spanisch 4,95 Kandidaten-Synsets pro Wortform. | S. 13651, Statistics; Tab. 1 | eigenes Ergebnis |
| Insgesamt mehr als 99.000 goldene Instanzen in 18 Sprachen (S. 13649: 99.450), 3 Mio. silberne Annotationen. | S. 13649, S. 13651 bis 13652 | eigene Angabe |
| Zero-shot: Modelle nur mit englischen Trainingsdaten übertreffen fast immer dieselben Modelle mit sprachspezifischen Trainingsdaten und sprachspezifische BERT-Modelle; der Abstand zu wissensbasierten Systemen ist groß. | S. 13653 bis 13654, Tab. 3 | eigenes Ergebnis |
| XLM-R Large: 65,66 F1 im Mittel über alle Sprachen außer Englisch, schwach bei Baskisch, Katalanisch, Chinesisch, weil viele Test-Senses im Training kaum vorkommen. Seltene Bedeutungen bleiben auch für große vortrainierte Modelle ein offenes Problem. | S. 13654, Discussion | eigenes Ergebnis, Erklärung der Autoren |
| Verben sind in den meisten Sprachen am schwersten, im Mittel 10 F1-Punkte unter Nomen; Ausnahmen Bulgarisch, Katalanisch, Niederländisch (Katalanisch nur 31 Verbinstanzen, „not significant“). | S. 13654, Tab. 4 | eigenes Ergebnis |
| Abstand zum Englischen im Mittel etwa 10 Punkte; Wortbedeutungen seien in aktuellen Sprachmodellen noch nicht gut erfasst. | S. 13654 | eigenes Ergebnis, Deutung |
| Künftige Arbeit: die Daten **validieren**, neue Sprachen von Hand annotieren und Teilmengen nach Sense-Häufigkeit bereitstellen. | S. 13654, Conclusion | Plan |

## Daten, Methode, Zahlen

**Deutsch in XL-WSD (am Seitenbild geprüft):**

| Größe | Training (T-SC+WNG) | Test |
|---|---|---|
| Wortformen (Typen) | 16.213 | 421 |
| davon polysem | 2.332 | 166 |
| Kandidaten-Synsets pro Wortform | 1,203 | 1,639 |
| Instanzen | 184.952 | 862 |
| verschiedene Synsets | 16.437 | 417 |

Quelle Tab. 1, S. 13652. Der deutsche Test stammt aus SemEval-2013 Task 12 (S. 13650), also aus Texten der WMT-Workshops, und enthält nur Nomen (Tab. 4: nur N belegt, S. 13654). Von 421 Wortformen im Test sind nur 166 polysem; der Testsatz enthält damit viele monoseme Instanzen (Anteil der Instanzen nicht angegeben).

**F1 für Deutsch (Tab. 3, S. 13653, am Seitenbild geprüft):** XLM-R Large zero-shot 83,18; XLM-R Base 82,13; mBERT 80,63; XLM-R Large mit MuLaN-Daten 83,29 (bester Wert), deutsches BERT mit MuLaN 82,13; mit übersetzten Trainingsdaten (T-SC+WNG) 73,78 (XLM-R Large und deutsches BERT); SyntagRank 75,99; Babelfy 77,84; **MCS 75,99**. MCS heißt hier „Most Common Sense according to BabelNet“ (S. 13653), keine aus Korpusdaten gelernte Baseline. Das beste Modell liegt für Deutsch also rund 7 Punkte über MCS; mit übersetzten Trainingsdaten liegt es darunter.

**Englisch (Tab. 2 und 3):** English-F 76,28 (XLM-R Large, SC+WNG), English-C (grob) 91,30; MCS 63,37 fein, 80,23 grob. Auf ALL (Raganato et al. 2017) erreicht BERT-L mit SC+WNG 78,36; EWISER 80,10 (Tab. 2, S. 13652).

**Mittelwerte außer Englisch (Tab. 3):** XLM-R Large 65,66; SyntagRank 57,68; Babelfy 52,85; MCS 49,31 (Micro-F1 über alle Sprachen außer Englisch).

**Auswertung:** F1; Präzision, Recall und F1 sind gleich, weil die Modelle immer antworten (S. 13652).

**Kleine Unstimmigkeiten im Werk:** English-C heißt S. 13651 einmal „SemEval-07 Task 17“, sonst überall der grobe Task 7 (S. 13649, 13650, 13654). Tab. 1 hat bei Kroatisch kein Feld für die verschiedenen Synsets im Test (Seitenbild: leer).

## Wörtliche Stellen

> „We are aware that limiting the conceptualisations of other languages to the English PWN may not define a faithful equivalent of a dictionary in other languages.“ (S. 13650)

> „This also highlights that representing the least frequent meanings remains an open issue even for large pre-trained language models.“ (S. 13654)

## Bezug zur Dissertation

- **Deutsch als Vergleichsgröße:** XL-WSD liefert für **Gegenwartsdeutsch** eine Größenordnung (83 F1 bestes Modell, 76 MCS; Tab. 3), aber nur für 862 Nomen-Instanzen aus Nachrichtentexten mit niedriger Polysemie (1,64 Kandidaten pro Wortform; Tab. 1). Der Goldstandard der Dissertation schichtet dagegen nach Polysemie 2 / 3 / 4+ und schließt monoseme Lemmata aus (PROTOKOLL §4.3). Die Werte sind deshalb nicht vergleichbar; zitierbar ist XL-WSD nur als Beleg, dass es für Deutsch einen Benchmark gibt und wie klein und nomenlastig er ist.
- **PROTOKOLL §9.2 (MFS-Baseline):** MCS ist hier der häufigste Sense laut BabelNet, nicht aus Trainingsdaten gelernt (S. 13653). Die Dissertation lernt MFS aus Silber und fällt nur ersatzweise auf den ersten Sense in `lexicon.xml` zurück, dessen Reihenfolge keinen Häufigkeitsrang trägt (`knowledge/data.md`, B8). Beim Vergleich mit XL-WSD-Zahlen ist diese Definitionsdifferenz zu nennen.
- **PROTOKOLL §2 (Gold) und A1:** Die neuen Testsets für 13 Sprachen sind automatisch aus WordNet-Beispielsätzen und Abbildungen erzeugt, ohne Doppelannotation und ohne Übereinstimmungsmaß; die Autoren nennen Validierung als künftige Arbeit (S. 13654). Nach der Begriffsbestimmung des Protokolls wäre das kein Gold. Das ist ein Argument für den Aufwand der Doppelannotation und für die ausdrückliche Unterscheidung Gold gegen Silber im Artikel.
- **Lexikografische Beispielsätze als Testdaten:** Belege aus WordNet-Beispielen sind gezielt für einen Sense geschrieben und daher eher eindeutig. Die Dissertation zieht Korpusbelege, in denen der Kontext oft nicht entscheidet (`KONTEXT_UNZUREICHEND`, PROTOKOLL §6). Das ist eine eigene Deutung; das Papier untersucht den Unterschied nicht.
- **PROTOKOLL §4.3 und §9.1, Punkt 6 (Wortart):** Verben im Mittel 10 F1-Punkte unter Nomen (S. 13654) bestätigt mehrsprachig, was Raganato et al. (2017) für Englisch zeigen; stützt die Wortart als Schichtungsmerkmal.
- **Seltene Bedeutungen:** Schwäche bei Senses, die im Training selten sind (S. 13654), stützt die Nicht-MFS-Auswertung in PROTOKOLL §9.2 (wie Maru et al. 2022, Postma et al. 2016).
- **Inventar als Übersetzung des englischen WordNet:** Die Autoren benennen selbst, dass die Bindung anderer Sprachen an das englische Begriffsinventar die Bedeutungsstruktur dieser Sprachen nicht treu abbildet (S. 13650). Das ist ein Gegenbild zur Dissertation, die ein eigenständiges onomasiologisches Inventar für Mittelhochdeutsch nutzt; für die Diskussion der Inventarabhängigkeit (A31) ist das ein zitierbarer Satz.

## Grenzen und Einwände

- Keine Übereinstimmungswerte für irgendeinen der neuen Testsätze; die Daten sind laut Autoren noch zu validieren (S. 13654).
- Automatische Abbildungen zwischen Inventarfassungen können Fehler einführen; ihr Umfang wird nicht beziffert (S. 13650 bis 13651).
- Zufällige 80/20-Aufteilung auf Instanzebene: Belege desselben Dokuments oder Beispielsatzes können in Test und Entwicklung landen; das Papier prüft das nicht.
- Testsätze sehr ungleich groß (Slowenisch 2.032 Instanzen, Deutsch 862) und von verschiedener Herkunft (WordNet-Beispiele gegen laufende Texte); Sprachen sind daher nur eingeschränkt vergleichbar.
- Keine Signifikanztests oder Intervalle; Unterschiede von wenigen Punkten auf 862 deutschen Instanzen sind nicht abgesichert.
- Keine LLMs mit Prompting, nur feinjustierte Encoder und wissensbasierte Systeme.
- Gegenwartssprachen; historische Sprachstufen und ein onomasiologisches Inventar wie das MHDBDB-Begriffssystem nicht berührt.

## Weiterführend

- Navigli, Jurgens & Vannella 2013, SemEval-2013 Task 12, Multilingual WSD (S. 13650): Herkunft der deutschen Testdaten.
- Barba et al. 2020, MuLaN: Multilingual Label propagatioN for WSD, IJCAI (S. 13652, 13655): sprachspezifische Silberdaten, für Deutsch der beste Wert.
- Agirre et al. 2010, SemEval-2010 Task 17, domänenspezifische All-Words-WSD (S. 13649, 13650).
- Navigli, Litkowski & Hargraves 2007 (S. 13649, 13650): liegt als Zusammenfassung vor (`Navigli-etal-2007-SemEval-Coarse-All-Words.md`), Grundlage von English-C.
- Bond & Paik 2012, A survey of wordnets and their licenses, GWC (S. 13648, 13650).
- Pilehvar & Navigli 2014, pseudowortbasierte Evaluation (S. 13654).

## Julias Markierungen im PDF

Keine; `markierungen.py` legt keine Datei an.
