# Artstein & Poesio 2008: Inter-Coder Agreement for Computational Linguistics

**Datei:** `pdf/Artstein-Poesio-2008-Inter-Coder-Agreement.pdf` (nur lokal; 42 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen (auch das Literaturverzeichnis), Formeln, Tab. 2, 5, 8, Abb. 3 und die MASI-Formel (S. 584) an Textebene und Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology J08-4004 (SHA-256 verglichen am 2026-11-13), also die Verlagsfassung; es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 554 + n (PDF 1 = S. 555 ohne gedruckte Zahl, PDF 42 = S. 596). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Artstein, Ron & Massimo Poesio (2008). Inter-Coder Agreement for Computational Linguistics. *Computational Linguistics* 34(4), S. 555 bis 596.
- **DOI/URL:** https://doi.org/10.1162/coli.07-034-R2 (aufgelöst am 2026-11-13, leitet auf direct.mit.edu weiter; Crossref: Band 34, Heft 4, S. 555-596, Dezember 2008); https://aclanthology.org/J08-4004/
- **Titelzusatz:** Im PDF steht über dem Titel die Rubrik „Survey Article“ (S. 555); die ACL Anthology führt den Titel als „Survey Article: Inter-Coder Agreement for Computational Linguistics“, Crossref ohne den Zusatz.
- **Lizenz:** CC BY-NC-SA 3.0 (FAQ der ACL Anthology: ACL-Material vor 2016, abgerufen 2026-11-13); Crossref nennt keine Lizenz.
- **Art:** begutachteter Zeitschriftenartikel (Übersichtsartikel); eingereicht 26.08.2005, angenommen 28.01.2008 (S. 555)
- **Sprache:** Englisch
- **Erweiterte Fassung:** laut S. 556, Anm. 2, unter http://cswww.essex.ac.uk/Research/nle/arrau/ (nicht aufgerufen); mehrere Herleitungen und Beweise sind dorthin ausgelagert (S. 559 Anm. 3, S. 564, S. 572, S. 577, S. 587 Anm. 9).

## Worum es geht

Der Übersichtsartikel legt die Mathematik und die Annahmen der gängigen Übereinstimmungskoeffizienten offen (S, π, κ, Krippendorffs α, gewichtetes κ_w) und bringt sie auf eine einheitliche Notation (S. 557 bis 570). Er klärt die Debatten um Annotator-Bias und Prävalenz (S. 570 bis 574), fasst Krippendorffs methodische Anforderungen zusammen und prüft ein Jahrzehnt computerlinguistischer Praxis an Dialogakten, Segmentierung, Anaphern und Wortbedeutungen (S. 574 bis 589). Ergebnis: Für Reliabilität sind Koeffizienten mit einer gemeinsamen Verteilung (π, α) angemessen; bei nicht gleich weit voneinander entfernten Kategorien, besonders bei Mengenlabels, sind gewichtete Koeffizienten wie α „almost unavoidable“, machen aber die Deutung der Werte noch schwerer (S. 555, 591). Eine Schwelle von 0,8 halten die Autoren für vertretbar, aber nicht als Bedingung für eine Veröffentlichung (S. 591).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Reliabilität ist Voraussetzung für Validität, garantiert sie aber nicht: Zwei Beobachter können dasselbe Vorurteil teilen. | S. 557, Abschnitt 2.1 | Position der Autoren (nach Krippendorff 2004a) |
| Rohübereinstimmung ist zwischen Studien nicht vergleichbar: Sie begünstigt Schemata mit wenigen Kategorien (Scott 1955) und berücksichtigt die Verteilung der Items auf Kategorien nicht. Beispiel: Bei 95 % Statement erwartet der Zufall 90,5 % Übereinstimmung, 90 % beobachtet ist also schlechter als Zufall. | S. 558 bis 559, Abschnitt 2.3 | referiert (Scott 1955; Di Eugenio & Glass 2004) |
| S, π und κ haben dieselbe Form (A_o − A_e)/(1 − A_e) und unterscheiden sich nur im Zufallsmodell: S Gleichverteilung, π eine gemeinsame Verteilung aller Codierer, κ je eine Verteilung pro Codierer. Es gilt π ≤ S und π ≤ κ. | S. 559 bis 562, Abschnitt 2.4 | Darstellung, Ungleichungen als leicht zu zeigen angegeben |
| S lässt sich durch Kategorien, die nie benutzt werden, künstlich erhöhen und würde in der CL sehr feinkörnige Tagsets belohnen, „provided that most tags are never actually encountered in real data“. | S. 561, Abschnitt 2.4.1 | referiert (Scott 1955), auf CL übertragen von den Autoren |
| Was in der CL „kappa“ oder K heißt (Carletta 1996 nach Siegel & Castellan 1988, Fleiss 1971), ist eine Verallgemeinerung von Scotts π, nicht von Cohens κ. | S. 555 Anm. 1; S. 562 Anm. 5 | eigene Klärung der Terminologie |
| Krippendorffs α ist als 1 − D_o/D_e definiert, für mehrere Codierer, verschiedene Abstandsmaße und fehlende Werte geeignet und beruht auf ähnlichen Annahmen wie π. Mit nominalem Abstand ist α fast identisch mit multi-π; der Unterschied ist der unverzerrte Schätzer der erwarteten Übereinstimmung, beide nähern sich bei wachsender Zahl der Items oder Codierer an. | S. 564 bis 567, Abschnitt 2.6.1 | Herleitung der Autoren nach Krippendorff 1980, 2004a |
| α funktioniert mit jedem Abstandsmaß mit d_kk = 0; das schafft aber neue Fallstricke: Für Mengen gibt es mehrere begründbare Abstandsmaße, und sie liefern für dieselben Daten verschiedene α. | S. 567 | Position der Autoren |
| Für die Reliabilität eines Annotationsverfahrens sind Koeffizienten mit einer gemeinsamen Verteilung (π, α) angemessen; κ misst eher die Vertrauenswürdigkeit (Validität) übereinstimmender Urteile. Die Wahl soll von der gewünschten Deutung des Zufalls abhängen, nicht vom beobachteten Unterschied der Randverteilungen. | S. 570 bis 572, Abschnitt 3.1 | Position der Autoren, teils nach Krippendorff 2004b und Craggs & McGee Wood 2005 |
| Der Unterschied zwischen π und κ ist in der Praxis klein, sinkt mit steigender Übereinstimmung und mit der Zahl der Codierer (Beobachtungen 1 und 2, Bias B als Varianz). In einer Studie mit 18 Codierern unterschieden sich α und eine κ-artige Variante erst in der dritten Nachkommastelle. | S. 571 bis 572, S. 585 | eigenes Ergebnis (Formel; Poesio & Artstein 2005) |
| Reliabilität sollte mit mehr als zwei Codierern geprüft werden, damit nicht zwei Codierer eine abweichende Lesart der Richtlinien teilen. | S. 572 bis 573; ähnlich S. 590 | Empfehlung der Autoren |
| Prävalenz: Bei schiefen Verteilungen ist A_e hoch, chance-korrigierte Werte bleiben niedrig, obwohl Übereinstimmung und Richtigkeit hoch sein können. Das ist gerechtfertigt: Reliabilität heißt, auch die seltenen Kategorien zu unterscheiden; π und κ sind dann etwa δ/(δ + ε), die Übereinstimmung auf der seltenen Kategorie. | S. 573 bis 574, Abschnitt 3.2, Tab. 7 | Herleitung der Autoren |
| Krippendorffs Anforderungen an Reliabilitätsdaten: erschöpfendes, vorab festgelegtes Schema mit Anleitung; nachvollziehbare Auswahl der Codierer; unabhängiges Arbeiten. Verletzt werden sie u. a. durch Ergänzen der Anleitung während der Datenerhebung, durch Experten und langjährige Mitarbeitende, die den Zweck der Studie kennen, und durch Absprachen. Krippendorffs eigene Zusammenfassung: drei oder mehr Codierer. | S. 574 bis 575, Abschnitt 4.1.1 | referiert (Krippendorff 2004a, Kap. 11) |
| Zur Stichprobe referiert: Mindestzahl der Einheiten nach Bloch & Kraemer 1989; jede Kategorie soll so oft vorkommen, dass mindestens fünf Zufallsübereinstimmungen zu erwarten sind; die Stichprobe soll alle Werte der Kategorien enthalten und alle Domänen abdecken. | S. 575 | referiert (Krippendorff 2004a, S. 239) |
| Ein Test gegen Zufall ist trivial; relevant sind Konfidenzintervalle. Für α ist die Verteilung unbekannt, Intervalle werden per Bootstrap bestimmt (Software: Hayes & Krippendorff 2007). | S. 575 bis 576, Abschnitt 4.1.2 | referiert (Cohen 1960; Krippendorff 2004a, Abschnitt 11.4.2) |
| Schwellen: In der CL folgt man meist Krippendorff (1980, S. 147) über Carletta (1996): K > 0,8 gute Reliabilität, 0,67 bis 0,8 erlaubt vorläufige Schlüsse. Krippendorff habe 0,67 aber „highly tentative and cautious“ formuliert und halte später 0,8 für das Minimum („a pretty low standard“, 2004a, S. 242); Neuendorf (2002) nennt 0,90 für alle akzeptabel, 0,80 für die meisten Fälle. Landis & Koch (1977) sind in der Medizin üblich. | S. 576, Abschnitt 4.1.3, Abb. 1 | referiert |
| Übereinstimmungskoeffizienten sagen den Erfolg maschinellen Lernens schlecht voraus; Reliabilitätsstudien prüfen aber die Tauglichkeit von Schema und Richtlinien, nicht die Lernbarkeit. | S. 577, Abschnitt 4.1.4 | referiert (Reidsma & Carletta 2008) und Position der Autoren |
| Gewichtete Koeffizienten erfassen Teilübereinstimmung bei hierarchischen oder mehrdimensionalen Tagsets; eine Hierarchie muss aber nicht die echten Verwechslungen abbilden. | S. 579, Abschnitt 4.2 | Position der Autoren, nach Geertzen & Bunt 2006 |
| Segmentierung: Weniger Grenzen heißt höhere erwartete Übereinstimmung; dieselbe Abweichung um eine Position ergibt bei A_o = 0,96 nur K = 0,65, feinere Einheiten mit A_o = 0,88 dagegen K = 0,75. | S. 581 bis 582, Tab. 8 | eigenes Rechenbeispiel |
| Anaphern: Passonneau (2004) nimmt Koreferenzketten als Labels und α mit Mengenabstand d_P (0 gleich, 1/3 Teilmenge, 2/3 Schnitt ohne Teilmenge, 1 disjunkt); Alternativen Jaccard und Dice. MASI wird beschrieben als „obtained by multiplying Passonneau’s original metric d_P by the metric derived from Jaccard d_J“, d_M = d_P × d_J. | S. 583 bis 584, Abschnitt 4.4.1 | referiert (Passonneau 2004, 2006); Formel siehe „Bezug“, Punkt 4 |
| Mit Ketten als Labels steigt α, K sinkt stark (Abb. 3: ohne Kette K 0,628 / α 0,656, volle Kette 0,480 / 0,691). Die Wahl des Abstandsmaßes verschiebt α stärker als die Wahl des Zufallsmodells: 0,642 (Jaccard), 0,654 (Passonneau), 0,691 (Dice). | S. 584 bis 585, Abb. 3 | eigenes Ergebnis (Poesio & Artstein 2005) |
| Diskursdeixis: Weil Antezedenten verschiedener Ausdrücke sich kaum überschnitten, lag die erwartete Nichtübereinstimmung nahe 1, „so the value of α turned out to be very close to the complement of the observed disagreement“. Je nach Abstandsmaß ergaben sich für dasselbe Experiment α von 0,122 bis 0,998; daher seien gewichtete α nicht mehr mit Faustregeln (Krippendorff, Landis & Koch) deutbar, Deutungen müssten aufgaben- und maßspezifisch werden. | S. 585 bis 586, Abschnitt 4.4.3 | eigenes Ergebnis (Artstein & Poesio 2006) |
| Wortbedeutungen sind eine der schwersten Annotationsaufgaben: Für jedes Wort gelten andere Kategorien, ein einheitliches Handbuch mit Beispielen für alle Kategorien ist unmöglich, man ist auf ein Wörterbuch angewiesen; Wörterbücher unterscheiden verschieden, Laien können feine Unterscheidungen oft nicht treffen; besonders Verben. | S. 586, Abschnitt 4.5 | Position der Autoren, teils nach Palmer, Dang & Fellbaum 2007 |
| WSD-Werte aus der Literatur: Véronis (1998) mit naiven Codierern und erlaubten Mehrfachlabels κ_w 0,41 bis 0,46 bei 0,63 bis 0,73 Übereinstimmung, pro Wort von 0,007 bis 0,92; SENSEVAL-3 67,3 % und durchschnittlich K 0,58; Kilgarriff (1999) 95,5 % mit Lexikographen und Schiedsentscheidung, was keine Replikationsstudie im Sinne Krippendorffs sei; Palmer et al. (2007) 82 % mit gruppierten statt 71 % mit WordNet-Senses. | S. 587 | referiert |
| Nachträgliches Zusammenlegen erhöht K (Bruce & Wiebe 0,874 auf 0,898; Véronis bei Nomen von etwa 0,45 auf 0,86), „the post hoc merging of categories is not equivalent to running a study with fewer categories to begin with“. | S. 587 bis 588 | referiert, Einwand der Autoren |
| Für hierarchische Sense-Inventare schlagen die Autoren vor, Teilübereinstimmung über ein Abstandsmaß in α abzubilden: Melamed & Resnik als d_M+R oder erweiterte Senses (Sense plus Gruppe) als Mengen mit d_P. Beispiel *call*: WN1 gegen WN3 in derselben Gruppe ergibt d = 2/3, WN1 gegen die Oberkategorie d = 1/3. Passonneau, Habash & Rambow (2006) lassen dagegen Mehrfachlabels zu und vergleichen sie mit MASI. | S. 588 bis 589 | eigener Vorschlag; Letzteres referiert |
| Empfehlungen zur Methodik: rigoros testen und berichten (auch OntoNotes berichte nur Prozentübereinstimmung); chance-korrigierte Werte zeigen die Qualität besser als Rohübereinstimmung; Experten sind in der CL vertretbar, dann gilt die Replizierbarkeit nur für Codierer derselben Population; zusätzlich eine unabhängige Evaluation der Aufgabe. | S. 590, Abschnitt 5.1 | Empfehlung der Autoren |
| Empfehlungen zur Wahl: K und α, weil sie vom Bias einzelner Codierer abstrahieren; mehr Codierer als beste Strategie; α ist unverzichtbar, wenn Kategorien nicht gleich weit voneinander entfernt sind, bei hierarchischen Tagsets und bei Mengenlabels, im zweiten Fall sind gewichtete Koeffizienten „almost unavoidable“; die Wahl der Gewichte bestimmt aber den Zahlenwert. | S. 590 bis 591, Abschnitt 5.2 | Empfehlung der Autoren |
| Empfehlungen zur Deutung: Nur Werte über 0,8 sicherten in ihren Studien brauchbare Qualität, daher 0,8, falls eine Schwelle nötig ist; eine einzige Schwelle passe aber nicht für alle Zwecke (brauchbare Korpora auch bei 0,7), sie solle keine Publikationsbedingung sein. Stattdessen Methode ausführlich berichten (Zahl der Codierer, Unabhängigkeit, nur Handbuch), Signifikanz, Konfusionsmatrix oder Übereinstimmungstabelle, und eine unabhängige Evaluation. | S. 591, Abschnitt 5.3 | Empfehlung der Autoren, teils nach Craggs & McGee Wood 2005, Di Eugenio & Glass 2004 |

## Daten, Methode, Zahlen

Übersichtsartikel ohne eigene neue Annotationsstudie; die eigenen Zahlen stammen aus Rechenbeispielen und aus früheren Studien der Autoren.

**Rechenbeispiele** (an der Textebene geprüft):

| Beispiel | Werte | Seite |
|---|---|---|
| Tab. 1 und 2: zwei Kategorien, 100 Äußerungen | A_o = 0,7; S = 0,4; π ≈ 0,341; κ ≈ 0,348 | S. 558, 560 |
| Tab. 4 bis 6: drei Kategorien, integriertes Beispiel | A_o = 0,88; S = 0,82; π ≈ 0,7995; κ ≈ 0,8013; gewichtet (Check zwischen den beiden anderen, Abstand 0,5) α ≈ 0,8156, κ_w ≈ 0,8163 | S. 568 bis 570 |
| Tab. 8: Segmentierung, 50 Äußerungen | grob: A_o 0,96, A_e 0,89, K 0,65; fein: A_o 0,88, A_e 0,53, K 0,75 | S. 582 |

Die Daten für Tab. 4 wurden nach Angabe der Autoren so lange variiert, bis π und κ die Schwelle 0,80 knapp auf beiden Seiten trafen (S. 571).

**Eigene Studien:** Anaphern mit 18 Codierern (Poesio & Artstein 2005; S. 572, 584 bis 585, Abb. 3); Diskursdeixis mit zehn Codierern im Beispiel (Artstein & Poesio 2006; S. 585 bis 586): α 0,55 (Passonneau), 0,45 (Jaccard), 0,55 (Dice); absolute Positionen 0,998 und 0,999; relative Positionen 0,167 und 0,122.

**Zentrale Formeln** (Notation der Autoren, S. 557 bis 567):

- A_e^π = Σ_k P̂(k)², mit P̂(k) = n_k / (i·c) über alle Urteile aller Codierer (S. 561, 564).
- α = 1 − D_o / D_e; D_o = 1/(i·c·(c−1)) Σ_i Σ_j Σ_l n_ikj n_ikl d_kjkl; D_e = 1/(i·c·(i·c−1)) Σ_j Σ_l n_kj n_kl d_kjkl (S. 566).
- Nominal: d = 0 bei gleichen, 1 bei verschiedenen Labels (S. 567).

## Wörtliche Stellen

> „[…] weighted, alpha-like coefficients, traditionally less used than kappa-like measures in computational linguistics, may be more appropriate for many corpus annotation tasks […]“ (S. 555)

> „[…] their use makes the interpretation of the value of the coefficient even harder.“ (S. 555, im selben Satz)

> „[…] because antecedents of different expressions rarely overlapped, the expected disagreement was close to 1 (maximal), so the value of α turned out to be very close to the complement of the observed disagreement […]“ (S. 586)

> „[…] once we start using weighted measures we cannot anymore interpret the value of α using traditional rules of thumb such as those proposed by Krippendorff or by Landis and Koch.“ (S. 586)

> „[…] in the case of word sense tagging different categories must be used for each word […]“ (S. 586)

> „We should note, however, that the post hoc merging of categories is not equivalent to running a study with fewer categories to begin with.“ (S. 588)

> „At least in the second case, weighted coefficients are almost unavoidable.“ (S. 591; gemeint: Mengenlabels)

> „We therefore feel that if a threshold needs to be set, 0.8 is a good value.“ (S. 591)

## Bezug zur Dissertation

**1. PROTOKOLL §9.1 und A8 (α als Hauptmaß), gestützt.** Die Wahl von α statt κ für die Reliabilität der Doppelannotation folgt genau der Empfehlung (S. 572, 590). Der Unterschied zwischen π-artigen Werten und κ ist laut S. 571 bis 572 in der Praxis meist klein und sinkt mit der Zahl der Codierer; bei zwei Codierern ist er also eher größer als in der Studie mit 18. Die Wahl soll nach der gewünschten Deutung des Zufalls fallen, nicht nach dem Ergebnis; das spricht dafür, κ allenfalls als Nebenwert zu berichten. Für `MEHRERE` als Mengenlabel sind gewichtete Koeffizienten laut S. 591 „almost unavoidable“; das stützt α mit Mengenabstand als Hauptmaß.

**2. PROTOKOLL §7 Schritt 2 und A32 (Stoppregel mit 0,67 und 0,80), Herkunft und Zweck der Schwellen.** Die beiden Zahlen stammen aus der Inhaltsanalyse (Krippendorff 1980, S. 147, über Carletta 1996): ab 0,8 gute Reliabilität, 0,67 bis 0,8 vorläufige Schlüsse (S. 576). Sie beziehen sich auf die Reliabilität codierter Daten, aus denen Schlüsse gezogen werden, nicht auf das Ende einer Pilotphase. Die Autoren lehnen eine feste Schwelle als Bedingung ab und empfehlen 0,8 nur, „if a threshold needs to be set“ (S. 591). Zwei Punkte passen zu A32: Die Stoppregel misst mit **α nominal**, und genau für ungewichtete Werte sind die Faustregeln gedacht; für gewichtete α (MASI) warnen die Autoren ausdrücklich davor, sie an 0,67 oder 0,8 zu messen (S. 586). Der Satz in A32, die Schwelle entscheide über das Ende des Nachschärfens, nicht über die Brauchbarkeit des Golds, ist mit S. 591 vereinbar; eine Stütze für Schwellen als Stoppregel eines Pilots enthält der Artikel nicht.

**3. A32: „Weil jedes Lemma eigene Sense-IDs hat, schätzt α den Zufall aus fast nie zusammenfallenden Labels und liegt damit nahe an der Rohübereinstimmung.“**
- **Für WSD steht das nicht im Artikel.** S. 586 hält nur fest, dass beim Sense-Tagging für jedes Wort andere Kategorien gelten; welche Folge das für die erwartete Übereinstimmung hat, wenn man über Wörter hinweg poolt, wird nicht erörtert.
- **Der Mechanismus ist belegt, an einer anderen Aufgabe:** Bei der Diskursdeixis überschnitten sich die Labels verschiedener Items kaum, D_e lag nahe 1, und α war „very close to the complement of the observed disagreement“ (S. 586), also nahe der beobachteten Übereinstimmung. Das ist dieselbe Lage wie bei gepoolten lemmaspezifischen Sense-IDs. Mit den Formeln S. 561 und 566 folgt es auch rechnerisch: Ist jede Sense-ID nur bei einem oder wenigen Items möglich, ist Σ P̂(k)² sehr klein (eigene Ableitung, nicht im Artikel).
- **Verwandte Warnung:** S. 561 zeigt für S, dass viele selten oder nie benutzte Kategorien den Zufallsterm drücken und feine Tagsets belohnen. Das ist dieselbe Richtung: Die Zufallskorrektur verliert ihre Wirkung, der Wert nähert sich der Rohübereinstimmung. Vorschlag: In A32 und §9.1 Punkt 3 S. 586 als Beleg für den Mechanismus anführen, mit dem Hinweis, dass es dort um Diskursdeixis geht; die Schwelle 0,80 ist dann praktisch eine Schwelle von etwa 80 % exakter Übereinstimmung auf dem ganzen Label.
- **Krippendorffs Stichprobenregel** (jede Kategorie mit mindestens fünf erwarteten Zufallsübereinstimmungen, S. 575) ist bei einem Token pro Lemma und lemmaspezifischen IDs nicht erfüllbar. Das gehört als Einschränkung zu §9.1 Punkt 3.

**4. PROTOKOLL §9.1 Punkt 1 (α mit MASI-Distanz), Formel festlegen.** Der Artikel gibt MASI als d_M = d_P × d_J an (S. 584), also als Produkt zweier Abstände. Passonneau (2006, S. 834 bis 835) definiert MASI dagegen als Ähnlichkeit J × M und nimmt 1 − MASI als Abstand; Passonneau, Habash & Rambow (2006, S. 1953) schreiben den Abstand als 1 − J·M. Beide Formeln geben 0 für gleiche und 1 für disjunkte Mengen, dazwischen aber verschiedene Werte. Eigene Rechnung für den häufigsten Fall der Dissertation, eine Person `SENSE` {s1}, die andere `MEHRERE` {s1, s2}: nach Passonneau 1 − (1/2 · 2/3) = 2/3, nach der Formel bei Artstein & Poesio 1/3 · 1/2 = 1/6. Vorschlag: Im Protokoll die Formel ausschreiben (1 − J·M nach Passonneau 2006 und Passonneau et al. 2006) und die verwendete Implementierung nennen; Artstein & Poesio für MASI nicht als Formelquelle zitieren.

**5. PROTOKOLL §9.1 Punkt 1: „α nominal (Mengen als unteilbare Labels) als untere Schranke“.** Der Artikel zeigt, dass verschiedene Abstandsmaße für dieselben Daten verschiedene α ergeben (S. 567, 585 bis 586); eine Ordnung zwischen nominalem und gewichtetem α wird nicht behauptet. Dass α mit Mengenabstand unter α nominal fallen kann, zeigt Passonneau 2006 (Tab. 1, S. 835: Jaccard −0,44 gegen nominal 0). Vorschlag: „untere Schranke“ durch „strengere Variante“ ersetzen oder als empirische Erwartung kennzeichnen.

**6. PROTOKOLL §9.1 Punkt 4 (Prävalenz, AC1, MFS/Nicht-MFS getrennt).** Gestützt: Bei einem dominanten Sense zeigt sich Reliabilität an der Übereinstimmung auf den seltenen Kategorien (S. 573 bis 574). Die getrennte Übereinstimmung für Nicht-MFS-Tokens ist eine direkte Umsetzung davon. Gwets AC1 kommt im Artikel nicht vor.

**7. PROTOKOLL §9.1 Punkt 5 (Bootstrap).** Gestützt für α allgemein (S. 576); das Ziehen nach Clustern (Text) steht nicht im Artikel und ist eine eigene Festlegung des Protokolls.

**8. PROTOKOLL §9.1 Punkt 7 (grobe Ebene vorab, nicht nachträglich zusammenlegen).** Gestützt durch S. 588. Ergänzend bietet S. 588 bis 589 einen zweiten Weg, der ohne Zusammenlegen auskommt: Teilübereinstimmung über ein Abstandsmaß in α. Weil ein MHDBDB-Sense eine Menge von Begriffen ist (Protokoll §2, Begriffsgruppe), ließe sich der Abstand zwischen zwei gewählten Senses als Mengenabstand ihrer Begriffsgruppen oder ihrer Oberbegriffe rechnen. Das ist ein eigener Vorschlag, im Artikel nur am Beispiel WordNet-Gruppen skizziert; vorab festlegen, weil die Wahl des Abstands den Wert verschiebt (S. 585 bis 586).

**9. PROTOKOLL §7 (Pilot, Richtlinien, dritte Person).** Gestützt: Richtlinien vor der gemessenen Runde einfrieren, weil das Ergänzen der Anleitung während der Datenerhebung Krippendorffs erste Anforderung verletzt (S. 574); das Protokoll misst den berichteten Wert erst in der Hauptrunde mit eingefrorenen Richtlinien. Die Warnung vor Experten und Mitarbeitenden, die den Zweck der Studie kennen (S. 575), deckt die Doppelrolle Julias (Richtlinien entworfen, annotiert) und die dritte Person in Schritt 6. Zwei Annotator:innen unterschreiten Krippendorffs Empfehlung von drei oder mehr (S. 575) und die der Autoren (S. 572 bis 573, 590); das gehört zu den Einschränkungen.

**10. PROTOKOLL §9.1 (Konfusionstabelle) und §9.2.** Gestützt: Konfusionsmatrix und ausführliche Methodenangaben berichten (S. 591), dazu eine unabhängige Evaluation (S. 590, 591). Die Statusebene als eigene Konfusionstabelle passt dazu. Der Einleitungssatz von §9.1 („Artstein & Poesio 2008 verlangen, die Behandlung solcher Sonderfälle offenzulegen“) ist nur sinngemäß gedeckt: S. 591 verlangt die Offenlegung der Methode allgemein; von Ausweichlabels oder fehlenden Werten ist dort nicht die Rede (fehlende Werte nur als Eigenschaft von α, S. 564).

**Abgleich mit `goldstandard/LITERATUR-IAA.md`** (Zeilen mit Artstein & Poesio ✔): Zeile „Rohübereinstimmung allein reicht nicht …“: alle Teile gedeckt (S. 559, 572, 590, 591). Zeile „Zusammenlegen … nicht gleichwertig“: gedeckt (S. 588). Zeile „Konfidenzintervalle für α per Bootstrap“: gedeckt (S. 576). Zeile „Prävalenz … 67,3 %, κ = 0,58 oder 0,35“: Artstein & Poesio nennen für SENSEVAL-3 nur 67,3 % und K 0,58 (S. 587); der Wert 0,35 steht nicht hier.

## Grenzen und Einwände

- Übersichtsartikel; die meisten Aussagen zu Schwellen und Methodik sind referiert (Krippendorff, Carletta, Di Eugenio & Glass). Eigene Daten nur aus Anaphern- und Deixisstudien.
- Zu WSD gibt es nur einen kurzen Abschnitt (S. 586 bis 589) mit Literaturwerten; die Frage, wie man bei wortspezifischen Kategorien den Zufall schätzt (gepoolt oder pro Wort), wird nicht behandelt.
- Die MASI-Formel weicht von der Originaldefinition ab (siehe „Bezug“, Punkt 4).
- Mehrere Herleitungen und Beweise (Bias mit gewichteten Maßen, multi-κ, Diskussion von χ² und Korrelationen, POS und Named Entities) stehen nur in der erweiterten Fassung, die nicht vorliegt.
- Stand 2008: keine Behandlung von AC1, Bootstrapping nach Clustern oder Modellen der Annotation.
- Übertragbarkeit: Die Schwellen stammen aus der Inhaltsanalyse; für ein onomasiologisches Inventar mit Mengen von Begriffen als Senses und für Mittelhochdeutsch gibt es keine Werte. Dass Annotator:innen historischer Texte keine Muttersprachler:innen sind, berührt die Frage nach der „Population“ der Codierer (S. 590) zusätzlich.

## Weiterführend

- Krippendorff 2004a, *Content Analysis*, 2. Aufl., Kap. 11 (S. 574 bis 576): Anforderungen, Stichprobe (S. 239), Schwelle (S. 242), Bootstrap (Abschnitt 11.4.2).
- Krippendorff 2004b, Reliability in content analysis, *Human Communication Research* 30(3) (S. 571): Argument für π-artige Koeffizienten; in `LITERATUR-IAA.md` schon gelistet.
- Hayes & Krippendorff 2007 (S. 576): Bootstrap für α; in `LITERATUR-IAA.md` mit ○.
- Di Eugenio & Glass 2004, *Computational Linguistics* 30(1) (S. 556, 570): Bias und Prävalenz.
- Craggs & McGee Wood 2005, *Computational Linguistics* 31(3) (S. 575, 591): keine Schwelle als Publikationsbedingung.
- Reidsma & Carletta 2008, *Computational Linguistics* 34(3) (S. 577): Übereinstimmung und maschinelles Lernen; relevant für den Vergleich LLM gegen Gold.
- Véronis 1998 (S. 587): WSD mit Mehrfachlabels und κ_w.
- Palmer, Dang & Fellbaum 2007, *Natural Language Engineering* 13(2) (S. 587 bis 588): gruppierte Senses.
- Melamed & Resnik 2000, *Computers and the Humanities* 34 (S. 588): Übereinstimmung bei hierarchischen Tagsets.
- Bruce & Wiebe 1998 und 1999 (S. 587 Anm. 9): nach Ansicht der Autoren die am weitesten entwickelte Technik, Übereinstimmungsstudien auszuwerten.
- Kilgarriff 1999, 95 % replicability (S. 587).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
