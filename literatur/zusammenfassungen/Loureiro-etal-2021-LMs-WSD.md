# Loureiro, Rezaee, Pilehvar & Camacho-Collados 2021: Analysis and Evaluation of Language Models for Word Sense Disambiguation

**Datei:** `pdf/Loureiro-etal-2021-LMs-WSD.pdf` (nur lokal; 58 Seiten, PDF-Seite 58 leer)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, Textebene des Haupttexts (S. 387 bis 421) ganz gelesen, Anhang (S. 421 bis 443: WiC, Sense-Definitionen, Detailtabellen, Literatur) überflogen. Tab. 5 (S. 406) und Tab. 7 (S. 411) am Seitenbild geprüft, Tab. 1, 2, 3, 6, 11 an der Textebene. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology 2021.cl-2.14 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 386 + n (PDF 1 = S. 387, PDF 57 = S. 443; Seitenzahlen in der Fußzeile, S. 387 ohne Zahl). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Loureiro, Daniel, Kiamehr Rezaee, Mohammad Taher Pilehvar & Jose Camacho-Collados (2021). Analysis and Evaluation of Language Models for Word Sense Disambiguation. *Computational Linguistics* 47(2), S. 387 bis 443.
- **DOI/URL:** 10.1162/coli_a_00405 (aufgelöst über doi.org auf direct.mit.edu, 2026-11-16). Crossref führt nur den Online-First-Datensatz vom 20.05.2021 mit „S. 1 bis 57“ ohne Band und Heft; Band 47, Heft 2, S. 387 bis 443 nach dem BibTeX der ACL Anthology (https://aclanthology.org/2021.cl-2.14/, abgerufen 2026-11-16) und den Kolumnentiteln und Seitenzahlen des PDF.
- **Lizenz:** CC BY-NC-ND 4.0 (S. 387; ebenso Crossref). Die Beschaffungstabelle `beschaffung-2026-10-30/4-stichprobe-wsd-daten.md` nennt CC BY 4.0; das trifft nicht zu.
- **Art:** begutachteter Zeitschriftenartikel (eingereicht 19.08.2020, angenommen 04.03.2021; S. 387)
- **Sprache:** Englisch

## Worum es geht

Die Arbeit untersucht, wie gut vortrainierte Encoder-Sprachmodelle (BERT, ALBERT) lexikalische Mehrdeutigkeit erfassen (S. 389). Sie vergleicht zwei Wege, solche Modelle für WSD zu nutzen: Merkmalsextraktion mit nächstem Nachbarn (1NN, gemittelte Kontextvektoren pro Sense) und Feinabstimmung (S. 395 bis 396). Auf dem englischen Standardrahmen (Raganato et al. 2017) liegen BERT-Modelle feinkörnig etwa im Bereich menschlicher Übereinstimmung, Verben bleiben am schwersten (S. 397 bis 400). Für eine genauere Analyse bauen die Autoren CoarseWSD-20: 20 englische Nomen mit 2 bis 5 groben, leicht unterscheidbaren Senses aus Wikipedia (S. 400 bis 403). Dort erreicht BERT unter idealen Bedingungen nahezu menschliche Werte; die Zahl der Senses sagt die Leistung kaum voraus, während schiefe Sense-Verteilungen vor allem feinabgestimmte Modelle mit wenig Trainingsdaten zum häufigsten Sense ziehen (S. 407, 411 bis 418).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| BERT erfasst grobe Sense-Unterscheidungen genau, auch mit wenigen Beispielen pro Sense; unter idealen Bedingungen nähert es sich der Lösung grobkörniger Nomen-WSD, die aber in der Praxis selten gegeben sind. | S. 387 bis 388, Abstract; S. 420 | eigenes Ergebnis |
| Menschliche Leistung auf WordNet-Inventaren wird auf 80 % (feinkörnig) und 90 % (grobkörnig) geschätzt; die Lücke liegt an feinen WordNet-Unterscheidungen, die auch Menschen schwer fallen. | S. 393, Abschnitt 3 | referiert (Gale, Church & Yarowsky 1992a; Palmer, Dang & Fellbaum 2007) |
| Standardrahmen, feinkörnig, alle Datensätze: BERT-Large 1NN 73,5, ALBERT-XXL 73,7, beste hybride Systeme bis 80,1 (EWISER), MFS 64,8; grobkörnig BERT-Large 82,8, MFS 76,2. | S. 397, Tab. 1 | eigenes Ergebnis (teils aus Originalarbeiten übernommen) |
| Alle BERT-basierten Modelle liegen feinkörnig „in the same ballpark“ wie die menschliche Übereinstimmung, die für die drei älteren Datensätze zwischen 64 und 80 % liege. | S. 398 | Vergleich der Autoren, Übereinstimmungswerte referiert (Navigli 2009) |
| Verben sind am schwersten, Adverbien am leichtesten: BERT-Large feinkörnig Nomen 75,1, Verben 63,2, Adverbien 85,3; grobkörnig bleiben Verben zurück. Ein Grund ist die feine Gliederung der Verbsenses (*run* hat 41 WordNet-Senses, zwölf davon Bewegung); Vergröberung über Domänen trennt Verbsenses künstlich. | S. 399 bis 400, Tab. 2 | eigenes Ergebnis, Deutung der Autoren |
| CoarseWSD-20: 20 Nomen, von zwei Fachleuten nach Art der Mehrdeutigkeit, Polysemie, Häufigkeit, Verteilung und Interpretierbarkeit ausgewählt; Senses, die Menschen nicht leicht unterscheiden, wurden verworfen; Trainings- und Testteil 60/40. | S. 400 bis 401, Abschnitt 4.1 | eigenes Verfahren |
| Menschliche Kontrolle: vier Annotator:innen, je fünf Wörter, 1.000 Testbelege (50 pro Wort); Genauigkeit über 96 % außer bei *club* (86) und *bass* (90), die feinere Unterscheidungen haben. Keine Übereinstimmung zwischen Annotator:innen, jedes Wort hatte eine Person. | S. 401 bis 403, Tab. 3 | eigenes Ergebnis |
| Schiefe der Sense-Verteilung wird als F2R (Anteil erster Sense zum Rest) und normierte Entropie angegeben; Entropie reicht von 0,04 (*pitcher*) bis 0,99 (*crane*). | S. 402 bis 403, Tab. 3, Anm. 18 | eigene Statistik |
| Auf CoarseWSD-20 liegen alle Transformer-Modelle meist über 90 %; Mittel Micro-F1: MFS 66,5, BERT-Large 1NN 95,8, feinabgestimmt 97,5; Macro-F1: MFS 33,2, 1NN 96,4, feinabgestimmt 95,1. | S. 405 bis 407, Tab. 5 | eigenes Ergebnis |
| Mehr Trainingsbelege führen nicht notwendig zu besserer Leistung (Pearson 0,2 oder weniger); **höhere Polysemie ist kein starker Indikator für niedrigere Leistung** („near zero average correlation across settings“). | S. 407 | eigenes Ergebnis, Korrelationswerte nicht tabelliert |
| Leistungsunterschiede der Modelle ähneln denen der Menschen: *java* und *digit* leicht, *bass* und *club* schwer, vermutlich wegen feinerer Unterscheidungen. | S. 407 | eigene Beobachtung |
| MFS-Verzerrung: Macro-F1 sinkt bei rein überwachten Klassifikatoren (FastText, feinabgestimmtes BERT), weil seltene Senses schlechter erkannt werden; BERT ist robuster, FastText leidet stark. | S. 407 | eigenes Ergebnis |
| Feinabstimmung neigt zur Überanpassung an den MFS; 1NN modelliert Senses unabhängig und ignoriert Sense-Verteilungen. | S. 407 | Deutung der Autoren |
| Ein ausgeglichenes Trainingsset ändert für 1NN fast nichts; feinabgestimmte Modelle sind „overly sensitive to the distribution of the training data“; bei den schiefsten Wörtern steigt der Recall des seltensten Sense stark (*deck* bis +52,4), die Precision sinkt (−27,1). | S. 411 bis 413, Tab. 7, 8 | eigenes Ergebnis |
| Mit 1 % der Trainingsdaten fällt feinabgestimmtes BERT bei den schiefsten Wörtern auf Zufallsniveau (Macro-F1 *pitcher* 49,9, *bank* 50,2), 1NN nicht. | S. 413 | eigenes Ergebnis |
| Drei Trainingsbeispiele pro Sense reichen für ein wettbewerbsfähiges Ergebnis; danach nur kleine Zuwächse. | S. 414 bis 415, Abb. 5 | eigenes Ergebnis |
| Sense-Bias (Maß B) halbiert sich etwa mit jeder Stufe mehr Trainingsdaten (1, 3, 10, 30 Beispiele pro Sense); im 1-Shot-Fall 0,232 (feinabgestimmt) gegen 0,137 (1NN). | S. 416 bis 417, Tab. 11 | eigenes Ergebnis, Maß eigen |
| Auch bei ausgeglichenen Trainingsdaten zeigt vortrainiertes BERT Vorlieben für meist häufigere Senses (*java* als Programmiersprache, *deck* als Schiffsdeck); Zahlen im Kontext ziehen zu numerischen Senses (*square*, *digit*). | S. 418 | eigenes Ergebnis |
| Beide Strategien scheitern, wenn der Kontext Hinweise auf mehrere Senses enthält (*digit*, S. 418); manche Belege sind auch für Menschen nicht entscheidbar (*it also likes apple*). | S. 407, 418 | eigene Beobachtung |
| Für feine Unterscheidungen korrelieren Kontextvektoren deutlich schwächer mit menschlichen Urteilen als für grobe. | S. 419 | referiert (Haber & Poesio 2020) |
| WSD ist auch grobkörnig nicht gelöst: vollständige Trainingsdaten sind aufwendig, Verbsenses bleiben offen. | S. 420 | Fazit der Autoren |
| WiC (inventarfreie Paaraufgabe, aber aus WordNet gebaut): BERT 69,6, menschliche Leistung 80,0, Zufall 50,0. | S. 420 bis 421, Tab. 13 | eigenes Ergebnis, Vergleichswerte referiert |

## Daten, Methode, Zahlen

- **Modelle:** BERT-Base und -Large, ALBERT-XXL (v2); Summe der letzten vier Schichten, gemittelt über Subwörter; 1NN mit Sense-Vektoren aus SemCor, MFS als Rückfall für ungesehene Lemmata (S. 396). Für CoarseWSD-20 zusätzlich Feinabstimmung pro Wort und zwei FastText-Baselines (S. 404). Generative Modelle (GPT-3) werden nur erwähnt, nicht getestet (S. 394).
- **Standardrahmen:** 7.253 Testinstanzen, 4.363 Sense-Typen, etwa 3.663 Worttypen, mittlere Polysemie 6,2 (S. 397); grobe Fassung durch Zusammenlegen von Senses derselben CSI-Domäne (Lacerra et al. 2020).
- **CoarseWSD-20:** 2 bis 5 Senses pro Wort (11 Wörter mit zwei, 6 mit drei, 2 mit vier, 1 mit fünf); 110 (*digit*) bis 9.240 Belege (*pitcher*) pro Wort (S. 403). Normierte Entropie: Σ f_i log f_i normiert durch log n (Anm. 18, S. 403). Dazu ein Testset außerhalb der Domäne mit sieben Wörtern aus WordNet-annotierten Korpora (S. 403, Tab. 4).
- **Tab. 5 (S. 406, am Seitenbild geprüft):** Zeilen nach normierter Entropie absteigend sortiert. Mensch: 100 bei 10 Wörtern, sonst 86,0 (*club*) bis 98,0. Feinabgestimmtes BERT-Large Micro-F1 bei schiefen Wörtern hoch (*pitcher* 100,0, *bank* 99,3), Macro-F1 FastText-B bei schiefen Wörtern niedrig (*pound* 48,9, *yard* 54,5, *deck* 56,1).
- **Begriffsgebrauch uneinheitlich:** Tab. 7 (S. 411, am Seitenbild geprüft) ist wie Tab. 5 nach normierter Entropie absteigend sortiert (*crane* oben, *pitcher* unten). Der Text nennt die Wörter oben „less entropic words (on top) that tend to have more uniform distributions“ und die schiefen unten (*deck*, *bank*, *pitcher*) „more entropic“ (S. 411, ebenso S. 413). Gemeint sind mit „more entropic“ offenbar die Wörter mit **niedriger** normierter Entropie, also schiefer Verteilung. Außerdem verweist S. 407 auf „Table 4.3“, gemeint ist Tab. 3.
- **Sense-Bias B:** für Sense j Summe der Anteile falsch als j klassifizierter Belege anderer Senses, B = Maximum über j; Median aus drei Läufen (S. 416).
- Rechenaufwand: über 1.500 GPU-Stunden (S. 405).

## Wörtliche Stellen

> „Also, higher polysemy is not a strong indicator of lower performance […], as one would expect from a classification task with a higher number of classes (near zero average correlation across settings).“ (S. 407)

> „By optimizing losses, fine-tuning is more susceptible to overfit on the MFS. In contrast, by memorizing states, 1NN models sense independently and disregard sense distributions entirely.“ (S. 407)

> „[…] in the ideal setting of having access to enough amounts of training data and computing power, BERT can approach human-level performance for coarse-grained noun WSD, even in cross-domain scenarios. However, this ideal setting rarely occurs in practice […]“ (S. 420)

## Bezug zur Dissertation

**1. PROTOKOLL §4.3 (Kovariaten) und LITERATUR-STICHPROBE.md: Abweichung von einer mit ✔ markierten Aussage.** LITERATUR-STICHPROBE.md führt: „Polysemiegrad sagt Schwierigkeit schlecht voraus; Sense-Schiefe (Verhältnis erster Sense zum Rest, normierte Entropie) ist der stärkere Faktor. | Loureiro et al. 2021 ✔“. PROTOKOLL §4.3 schreibt, Loureiro et al. 2021 „finden die Schiefe aussagekräftiger als die Sense-Zahl“. Am Volltext:
- **Gedeckt:** Die Zahl der Senses korreliert kaum mit der Leistung (S. 407). Die Korrelationswerte sind nicht berichtet, die Spanne ist schmal (2 bis 5 Senses, 20 Nomen, grobe Wikipedia-Senses), und gemessen ist **Systemleistung**, nicht menschliche Übereinstimmung.
- **Nicht gedeckt:** Einen Vergleich, nach dem Schiefe die Schwierigkeit **besser vorhersagt** als die Polysemie, rechnet die Arbeit nicht. F2R und Entropie stehen als Datensatzstatistik in Tab. 3; eine Korrelation von Entropie und Leistung wird nicht berichtet. Was gezeigt ist: Schiefe Verteilungen erzeugen eine MFS-Verzerrung bei überwachten und feinabgestimmten Modellen, sichtbar im Macro-F1 und bei wenig Trainingsdaten (S. 407, 411 bis 413). Für 1NN mit ausreichenden Daten ist Schiefe kaum ein Faktor (*pitcher*, Entropie 0,04: Micro- und Macro-F1 nahe 100, Tab. 5). Bei Menschen hingen die schweren Fälle an feineren Unterscheidungen (*club*, *bass*), nicht an Schiefe (S. 403, 407).
- **Vorschlag:** Die Aussage in LITERATUR-STICHPROBE.md und PROTOKOLL §4.3 auf das Belegte zurücknehmen, etwa: „Bei 20 englischen Nomen mit 2 bis 5 groben Senses korreliert die Sense-Zahl kaum mit der Systemleistung (S. 407); schiefe Verteilungen ziehen überwachte und feinabgestimmte Modelle zum häufigsten Sense, besonders bei wenig Trainingsdaten (S. 411 bis 413).“ Die Wahl von MFS-Anteil und Entropie als Kovariaten bleibt damit begründbar, aber als Faktor für Modellverzerrung, nicht als besserer Prädiktor der Schwierigkeit. Nebenbefund für dieselbe Zeile: In der (nicht gegengelesenen) Zusammenfassung zu Passonneau et al. 2010 erscheint Entropie nur als in der Literatur vorgeschlagener Faktor (dort S. 3244, referiert), nicht als Befund; auch dieser Beleg trägt „Schiefe aussagekräftiger“ offenbar nicht.

**2. PROTOKOLL §9.1 Punkt 4 und §9.2 (Prävalenz, MFS- und Nicht-MFS-Tokens).** Der Befund, dass Micro-F1 bei schiefen Wörtern hoch bleibt, während Macro-F1 einbricht (Tab. 5, Tab. 8), stützt die Festlegung, Übereinstimmung und Genauigkeit getrennt für MFS- und Nicht-MFS-Tokens zu berichten. Für das LLM gilt die Frage nach einer Verzerrung zum häufigen Sense ebenso; ob ein LLM ohne Training wie 1NN oder wie ein feinabgestimmtes Modell reagiert, zeigt die Arbeit nicht.

**3. PROTOKOLL §4.3 und §9.1 Punkt 6 (Wortart).** Gestützt: Verben am schwersten, auch nach Vergröberung (S. 399 bis 400, Tab. 2). Das deckt sich mit Raganato et al. 2017 und Passonneau et al. 2010 in LITERATUR-STICHPROBE.md.

**4. PROTOKOLL §9.1 Punkt 7 (zwei Ebenen des Begriffssystems).** Die Arbeit vergröbert über Domänen (CSI) und warnt, dass das bei Verben künstliche Trennungen erzeugt (S. 400). Für die Wahl der groben Ebene über den Zahlencode des Begriffssystems (offener Punkt 12) heißt das: prüfen, ob Senses eines Verbs auf der groben Ebene getrennt bleiben, obwohl sie inhaltlich zusammengehören. Ableitung, nicht Aussage der Arbeit.

**5. Forschungsfrage (§1) und späterer Encoder-Vergleich.** Die Arbeit untersucht Encoder, keine generativen LLMs. Sie ist der Bezugspunkt für den geplanten Encoder-Vergleich: 1NN mit gemittelten Sense-Vektoren funktioniert schon mit drei Beispielen pro Sense (S. 414), ist robust gegen Verteilungsänderungen (S. 411) und braucht keine Feinabstimmung. Für Mittelhochdeutsch fehlt aber ein passendes vortrainiertes Modell; die Ergebnisse gelten für englische Wikipedia-Daten.

**6. A31 und Weg C (offene Punkte 20 und 22).** Nur am Rand: WiC ist eine inventarfreie Paaraufgabe (gleicher Sense oder nicht), aber aus WordNet gebaut; menschliche Leistung 80 %, BERT 69,6 % (S. 420 bis 421). Für die Frage, ob ein Inventar das Urteil lenkt, liefert die Arbeit nichts.

**7. PROTOKOLL §9.1 (Vergleichswerte).** Die menschlichen Werte auf CoarseWSD-20 sind Genauigkeit einer Person gegen das Gold, keine Übereinstimmung zwischen Personen (S. 401). Sie sind nicht als IAA-Vergleichswert zu zitieren.

## Grenzen und Einwände

- Gegenwartsenglisch; CoarseWSD-20 enthält nur Nomen mit groben, ausgewählt leicht unterscheidbaren Wikipedia-Senses, teils Eigennamen (*java*, *seal* als Musiker); Ausgangsmenge waren Wörter mit mindestens 30 verlinkten Belegen, ausdrücklich, um nahezu ideale Bedingungen zu testen; der „long tail“ seltener Senses fehlt damit bewusst (S. 401, Anm. 16).
- Die Aussage zur Polysemie stützt sich auf 20 Wörter mit 2 bis 5 Senses und nennt keine Korrelationswerte.
- Schwierigkeit ist durchweg Systemleistung gegen ein Gold; menschliche Übereinstimmung wird nicht gemessen.
- Begriffe „entropic“ im Text gegenläufig zur Spalte „Ent.“ (oben).
- Keine generativen LLMs, kein Prompting; für die Pipeline der Dissertation nur mittelbar.
- Für ein onomasiologisches Inventar mit 2 bis 15 Senses und für Mittelhochdeutsch nicht geprüft.

## Weiterführend

- Postma, Izquierdo Bevia & Vossen 2016, More is not always better: balancing sense distributions for all-words WSD, COLING (S. 407, 412) und Postma et al. 2016, Addressing the MFS bias in WSD systems, LREC (Literaturverzeichnis): MFS-Verzerrung.
- Haber & Poesio 2020, Word sense distance in human similarity judgements and contextualised word embeddings, PaM (S. 419): menschliche Nähe-Urteile gegen Kontextvektoren, passt zu Weg C.
- McCarthy, Apidianaki & Erk 2016, Word sense clustering and clusterability, *Computational Linguistics* 42(2), S. 245 bis 275 (S. 419).
- Lacerra et al. 2020, CSI: A coarse sense inventory for 85 % WSD, AAAI (S. 397, 400): Vergröberung über Domänen.
- Pilehvar & Camacho-Collados 2019, WiC (S. 389, 420).
- Nair, Srinivasan & Meylan 2020, Contextualized word embeddings encode aspects of human-like word sense knowledge (S. 388).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
