# Henrich 2015: Word Sense Disambiguation with GermaNet

**Datei:** `pdf/Henrich-2015-WSD-GermaNet.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext (Kap. 1, 5, 6, 9), von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->

**Stand:** 2026-10-28, Kap. 1, 5, 6 und 9 sowie Abstract gelesen (Docling-Text); Tab. 5.1 bis 5.5, 5.10, 6.1, 6.2 und 6.4 bis 6.6 an Seitenbildern geprüft, Tab. 6.3, 5.11 und 8.4 an der rohen Textebene; alle Seitenangaben an der Textebene nachgezogen, weil die Seitenmarken der Docling-Fassung um S. 134 bis 135 und 139 bis 140 um eine Seite verrutschen; MFS-Baseline gezielt in Kap. 2.2.3, 7.2.2 und 8.3 nachgeschlagen; DOI aufgelöst.

**Seitenzählung:** Gedruckte Seite = PDF-Seite minus 14 im ganzen Hauptteil (Kap. 1 beginnt S. 3 = PDF 17; Kap. 5 S. 99 = PDF 113; Kap. 6 S. 145 = PDF 159; Kap. 9 S. 291 = PDF 305). Zitiert wird die gedruckte Seite, die PDF-Seite in Klammern.

**Gewichtung:** Schwerpunkt auf Kap. 5.3 (manuelle Annotation der TüBa-D/Z) und 6.2 (Umgang mit „kein Sense“ und Mehrfach-Senses), weil sie das Vorbild für einen Goldstandard mit zwei Annotator:innen liefern. WebCAGe (5.2) ist automatisch erzeugt und nur knapp erfasst. Kap. 2, 3, 4, 7, 8 nicht gelesen; Zahlen daraus nur, wo ausdrücklich vermerkt.

## Bibliografie

- **Vollständig:** Henrich, Verena, 2015. *Word Sense Disambiguation with GermaNet. Semi-Automatic Enhancement and Empirical Results.* Dissertation, Philosophische Fakultät, Eberhard Karls Universität Tübingen. Verlag: TOBIAS-lib, Tübingen. Hauptberichterstatter Erhard Hinrichs, Mitberichterstatter Gerhard Jäger; mündliche Prüfung 29.4.2015 (PDF-Seiten 1 und 2).
- **DOI/URL:** 10.15496/publikation-4706; `doi.org` leitet auf `publikationen.uni-tuebingen.de/xmlui/handle/10900/63284` weiter. Der Repositoriumseintrag nennt Titel „Word Sense Disambiguation with GermaNet“ (ohne Untertitel), Paralleltitel „Disambiguierung von Wortbedeutungen mit GermaNet“, Jahr 2015, Sprache Englisch, Typ PhDThesis, URN urn:nbn:de:bsz:21-dspace-632846.
- **Art:** Abschlussarbeit (Dissertation), nicht separat begutachtet; Teile vorab veröffentlicht als Henrich et al. 2012b (WebCAGe) und Henrich & Hinrichs 2013, 2014 (TüBa-D/Z-Annotation) (S. 101 (PDF 115)).
- **Sprache:** Englisch

## Worum es geht

Die Arbeit will den Ressourcenengpass der deutschen WSD überwinden (S. 3 (PDF 17)). Dazu ergänzt sie GermaNet um Definitionen aus Wiktionary, baut zwei sense-annotierte Korpora (das automatisch geerntete WebCAGe und eine manuelle Annotation von 109 Lemmata in der Baumbank TüBa-D/Z), aktualisiert ein drittes (deWaC, Broscheit et al. 2010) und evaluiert darauf wissensbasierte und überwachte WSD-Verfahren (Abstract, S. i (PDF 3); S. 3 bis 5 (PDF 17 bis 19)). Die manuelle TüBa-D/Z-Annotation folgt dem Lexical-Sample-Design, ist doppelt und unabhängig annotiert, lemmaweise organisiert und von einer Lexikografin adjudiziert; die Übereinstimmung liegt bei 96,4 % (Nomen) und 93,7 % (Verben), κ 85,4 und 82,4 (S. 138 (PDF 152)). Ergebnis der Experimente: Überwachte Klassifikatoren übertreffen wissensbasierte Verfahren deutlich, decken aber nur Lemmata mit Trainingsdaten ab (S. 291 bis 292 (PDF 305 bis 306)).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| WSD-Forschung konzentriert sich auf Englisch; für andere Sprachen fehlen vor allem sense-annotierte Korpora. | S. i (PDF 3), Abstract; S. 11 (PDF 25), 1.3 | eigene Einschätzung mit Belegen (Kilgarriff & Palmer 2000) |
| Nur etwa 10 % der GermaNet-Einträge haben Definitionen; ohne Definitionen ist die Unterscheidung der Senses für Annotator:innen schwierig. Deshalb werden Wiktionary-Definitionen automatisch zugeordnet. | S. 3 (PDF 17), 1.1 | eigene Begründung |
| Ein vordefiniertes Inventar setzt voraus, dass Senses diskret und für einen Text passend sind; beides ist fraglich (Kilgarriff: Senses nur relativ zu einer Aufgabe; Hanks: Bedeutungspotenziale). | S. 7 bis 8 (PDF 21 bis 22), 1.2 | referiert |
| Die richtige Granularität hängt vom Zweck ab; WordNet gilt als zu feinkörnig, GermaNet ist gröber (Beispiele *Buch*, *Mund*); Zusammenlegen feiner Senses hob die WSD-Leistung stark. | S. 9 bis 10 (PDF 23 bis 24), 1.2 | referiert (Palmer 2000; Ide & Wilks 2006; Palmer et al. 2006, 2007) mit eigenen Beispielen |
| Zwei Arten sense-annotierter Korpora: All-Words und Lexical Sample. Beide eigenen Korpora sind Lexical Sample; bei der TüBa-D/Z wegen des maschinellen Lernens, das genug Belege pro Lemma braucht. | S. 100 (PDF 114), Kap. 5; S. 126 bis 127 (PDF 140 bis 141), 5.3.2 | eigene Entscheidung |
| Lemmaweise Annotation (erst alle Senses eines Lemmas ansehen, dann alle Belege) ergibt höhere Qualität als tokenweise, weil alle Senses präsent sind. | S. 102 (PDF 116), 5.1.1 | referiert (Kilgarriff 1997c; Palmer & Xue 2010) |
| Üblicher Ablauf: zwei oder mehr Annotator:innen annotieren dieselben Belege, eine Adjudikator:in klärt Abweichungen und kommentierte Fälle; wo dieselbe Gruppe das Inventar pflegt, wird es während der Annotation ergänzt. | S. 102 (PDF 116), 5.1.1 | referiert (Palmer et al. 2001; Palmer & Xue 2010) |
| IAA ist bei Expert:innen höher; zwischen Menge und Qualität gibt es einen Zielkonflikt. | S. 106 (PDF 120), 5.1.1 | referiert, ohne Einzelbeleg |
| Ältere deutsche GermaNet-Korpora (Saito et al. 2002; Raileanu et al. 2002; Broscheit et al. 2010) beruhen auf GermaNet-Versionen ohne persistente IDs und sind mit neuen Versionen nicht kompatibel. | S. 107 (PDF 121), 5.1.2 | eigene Bewertung |
| WebCAGe: Belege werden über die Zuordnung GermaNet zu Wiktionary automatisch geerntet und annotiert, danach manuell korrigiert („semi-automatic“). | S. 111 (PDF 125), 5.2 | eigenes Verfahren |
| „One sense per discourse“: Alle Vorkommen eines Zielworts in einem Text bekommen denselben Sense; die Heuristik stimmt in 99,96 % (Wiktionary-Beispiele), 96,75 % (externe Seiten) und 95,62 % (Wikipedia) der Fälle. | S. 114 (PDF 128), 5.2.1 | eigene Messung (Heuristik nach Gale et al. 1992b) |
| Nur echt mehrdeutige Wörter (mindestens zwei GermaNet-Senses) kommen in WebCAGe. | S. 114 (PDF 128), 5.2.1 | eigene Festlegung |
| Die automatische Zielworterkennung erreicht über 92 % Precision und Recall außer bei Verben in Gutenberg-Texten; ohne Nachkorrektur blieben etwa 2 bis 5 % Rauschen; die manuelle Nachkorrektur aller WebCAGe-Belege kostete 25 Stunden einer erfahrenen Hilfskraft. | S. 119 (PDF 133), 5.2.3, Tab. 5.2 | eigenes Ergebnis |
| Aus WebCAGe lässt sich keine MFS-Information gewinnen, weil die Ernte eine schiefe Belegzahl liefert und nicht alle Vorkommen eines Lemmas in einem Text annotiert; aus der TüBa-D/Z schon. | S. 4 (PDF 18), 1.1; S. 143 (PDF 157), 5.4 | eigene Begründung |
| Auswahl der TüBa-D/Z-Lemmata nach vier Kriterien: mindestens zwei GermaNet-Senses und mindestens 16 Belege; Ausgewogenheit von Frequenz und Sense-Zahl; Nomen und Verben; bei Verben unterschiedliche Korrelation von Sense und Valenzrahmen. | S. 127 (PDF 141), 5.3.2 | eigenes Design |
| Nomen wurden nach Frequenz und Polysemie gewählt, um den Einfluss von Belegmenge und Polysemie zu untersuchen; Verben nach vier Korrelationsklassen, aufgeteilt in eine für GermaNet repräsentative und eine „high correlation“-Stichprobe. | S. 127 bis 134 (PDF 141 bis 148), 5.3.2 | eigenes Design |
| Zwei Annotator:innen (deutsche Muttersprachler:innen, Computerlinguist:innen, beide mit GermaNet vertraut) annotieren alle Lemmata und Belege unabhängig; eine davon ist die Autorin selbst, die andere eine studentische Hilfskraft des GermaNet-Projekts. | S. 134 (PDF 148), 5.3.3 mit Fn. 1 | eigenes Verfahren |
| Pro Beleg genau ein Sense, wenn möglich; die Richtlinien erlauben mehrere Senses oder keinen, wenn unklar ist, welcher von zwei gemeint ist, oder keiner passt. Mehrere Senses sind selten, „kein Sense“ häufiger, meist bei Idiomen und übertragenem Gebrauch. | S. 134 bis 135 (PDF 148 bis 149), 5.3.3 | eigenes Ergebnis, gestützt auf Raileanu et al. 2002 und Véronis 1998 |
| Eine erfahrene Lexikografin (GermaNet-Verantwortliche) adjudiziert alle Belege mit Abweichung oder Kommentar und entscheidet, ob fehlende Senses in GermaNet ergänzt werden (Beispiel *Mann* als Zähleinheit). | S. 135 bis 136 (PDF 149 bis 150), 5.3.3 | eigenes Verfahren, „along the lines“ mit Kilgarriff & Rosenzweig 2000, Fellbaum et al. 2001, Passonneau et al. 2012 |
| Annotationswerkzeug zeigt Satz plus vorangehenden Satz, den ganzen Artikel per Link, alle Baumbank-Annotationen und alle GermaNet-Informationen; Kommentarfeld für problematische Fälle und Markierung „idiomatisch“ oder „übertragen“. | S. 137 bis 138 (PDF 151 bis 152), 5.3.3 | eigenes Verfahren |
| IAA als Dice-Koeffizient mit Teilübereinstimmung (Véronis 1998), gemittelt über Belege: Nomen 96,4 %, Verben 93,7 %; Cohen's κ 85,4 und 82,4. | S. 138 (PDF 152), 5.3.4 | eigenes Ergebnis |
| Für κ werden Belege ausgeschlossen, bei denen eine Annotator:in mehr als einen Sense wählte (60 bei Nomen, 17 bei Verben), und Lemmata, bei denen beide immer denselben Sense wählen. | S. 138 (PDF 152), Fn. 1 | eigene Festlegung nach Raileanu et al. 2002 |
| Niedrige Übereinstimmung erklärt sich durch sehr feine Sense-Unterscheidung (*Höhe*, mehrere Verben), durch Umbau des Inventars während der Annotation (*Kette*, *holen*) und durch übertragenen Gebrauch (*fressen*). | S. 138 bis 140 (PDF 152 bis 154), 5.3.4 | eigenes Ergebnis |
| κ ist bei schiefer Verteilung nicht aussagekräftig: *Bein* hat bei 97,4 % Übereinstimmung κ = −1,3, weil 77 von 78 Belegen denselben Sense tragen; bei *existieren* und *vorschreiben* κ = 0,0. | S. 139 bis 140 (PDF 153 bis 154), 5.3.4 | eigenes Ergebnis |
| Bei Nomen keine Korrelation zwischen IAA und Polysemie (Pearson r = −0,03, p = 0,88); bei Verben r = −0,39, p < 0,001. | S. 139 bis 141 (PDF 153 bis 155), 5.3.4 | eigenes Ergebnis; Nomen wie Fellbaum et al. 2001, Verben abweichend |
| Die deutsche IAA liegt viel höher als englische Werte (Véronis 1998: 73 % Nomen, 63 % Verben; Palmer et al. 2006: 71,3 %), erklärt durch die geringere Sense-Zahl (3,97 bzw. 2,84 gegenüber 7,6 bzw. 12,6). | S. 141 (PDF 155), 5.3.4 | eigene Deutung, Vergleichswerte referiert |
| Die TüBa-D/Z ist das einzige GermaNet-Korpus, bei dem das Inventar während der Annotation ergänzt wurde. | S. 108 (PDF 122), 5.1.2; S. 143 (PDF 157), 5.4 | eigene Feststellung |
| Für den Vergleich mehrerer Korpora muss das Inventar übereinstimmen; alle drei Korpora werden auf GermaNet 9.0 gehoben. | S. 145 (PDF 159), Kap. 6 | eigenes Vorgehen |
| Zum Umgang mit Annotationen ohne Sense oder mit mehreren Senses gibt es in der WSD-Literatur „very little if any information“. „Kein Sense“ wird als eigene Klasse behandelt, nicht ignoriert. | S. 150 bis 151 (PDF 164 bis 165), 6.2 | eigene Festlegung |
| Fünf Optionen für Mehrfach-Senses: (i) Teilpunkte, (ii) ignorieren, (iii) richtig, wenn einer der Senses getroffen, (iv) alle außer einem streichen, (v) pro Sense eine Annotation. (i) ist am fairsten; (iii) würde die Ergebnisse leicht überschätzen. Wissensbasiert wird (i) mit Dice umgesetzt, überwacht (iv), weil Weka keine Mehrfachlabels kann. | S. 151 bis 153 (PDF 165 bis 167), 6.2 | eigene Abwägung (Resnik & Yarowsky 1997, 1999) |
| Überwachte Evaluation nur für Lemmata mit mindestens zwei Senses mit je mindestens drei Belegen und zusammen mindestens 15 Belegen; Aufteilung 2:1 stratifiziert. | S. 146 bis 149 (PDF 160 bis 163), 6.1 | eigenes Design (2:1 nach Palmer et al. 2006) |
| MFS-Baseline: weist immer den häufigsten Sense der Annotationen zu; oft schwer zu schlagen, besonders bei schiefer Verteilung; braucht annotierte Daten und wird deshalb nur mit überwachten Systemen verglichen. Obergrenze ist die IAA. | S. 27 (PDF 41), 2.2.3; S. 185 (PDF 199), 7.2.2 | eigene Darstellung nach Gale et al. 1992a, Navigli 2009, Kilgarriff & Rosenzweig 2000 (Kap. 2/7, außerhalb des Auftrags nachgeschlagen) |
| Wissensbasierte Systeme haben höhere Abdeckung, überwachte die deutlich bessere Leistung; wissensbasierte Verfahren taugen für Nomen, kaum für Verben und Adjektive. | S. 291 bis 292 (PDF 305 bis 306), 9.1 | eigenes Ergebnis, bestätigt Kilgarriff & Rosenzweig 2000 u. a. |
| deWaC liefert die schlechtesten Ergebnisse (höhere Polysemie, heterogene Kontexte); wissensbasierte Verfahren sind auf der TüBa-D/Z am besten, überwachte auf WebCAGe (geringere Polysemie). | S. 292 bis 293 (PDF 306 bis 307), 9.2 | eigenes Ergebnis |
| Ausblick u. a.: Sense-spezifische Wortvektoren als neuer Zugang zur WSD. | S. 295 (PDF 309), 9.3 | Ausblick, referiert |

## Daten, Methode, Zahlen

**Sense-Inventar:** GermaNet (relationaler Ansatz, Wordnet); Annotation der TüBa-D/Z auf GermaNet 8.0, WebCAGe auf 6.0, deWaC (Broscheit et al.) auf 5.1; für die Experimente alle auf GermaNet 9.0 (April 2014) gehoben (S. 145 (PDF 159)).

**WebCAGe** (automatisch, nachkorrigiert):

- Ursprüngliche Fassung: 10.750 annotierte Tokens zu 2.607 polysemen Wörtern (211 Adjektive, 1.499 Nomen, 897 Verben), im Mittel 2,9 Senses (2,4 / 2,6 / 3,6) (S. 117 bis 118 (PDF 131 bis 132), Tab. 5.1). Davon 7.644 aus Wiktionary-Beispielen, 1.732 Wikipedia, 589 externe Seiten, 785 Gutenberg (S. 117 (PDF 131)).
- Precision und Recall der Zielworterkennung über 92 %, außer Verben in Gutenberg-Texten (Precision 69,87 %) (S. 118 bis 119 (PDF 132 bis 133), Tab. 5.2).
- Version 3.0 (GermaNet 9.0): 10.402 Belege zu 2.708 Lemmata (212 Adj., 1.537 Nomen, 959 Verben), im Mittel 4 Belege pro Lemma, Polysemie 3,1 (S. 154 (PDF 168), Tab. 6.2). Für überwachte WSD bleiben 1.761 Belege zu 43 Lemmata (S. 155 (PDF 169), Tab. 6.3).
- 753 Belege mit mehreren Senses, weil die Wiktionary-Zuordnung mehrere GermaNet-Senses auf einen Eintrag abbildet; keine Belege ohne Sense (S. 150 bis 152 (PDF 164 bis 166), Tab. 6.1 auf S. 151).

**TüBa-D/Z** (manuell, Zeitungstexte der *taz*):

- Annotiert auf Release 8.0 (1.365.642 Tokens, 75.408 Sätze, 3.356 Artikel) (S. 122 (PDF 136)).
- 109 Lemmata: 30 Nomen mit 7.538 Belegen (22 bis 1.427 pro Lemma, Mittel 251; Polysemie 2 bis 7, Mittel 3,97) und 79 Verben mit 7.967 Belegen (16 bis 710, Mittel 101; Polysemie 2 bis 14, Mittel 2,84) (S. 127 bis 129 (PDF 141 bis 143), Tab. 5.3).
- Verben nach Korrelationsklasse von Sense und Valenzrahmen: in GermaNet 8.0 sind 21,6 / 25,7 / 47,6 / 5,1 % der 2.739 polysemen Verben in Klasse 1 bis 4 (Tab. 5.10; der Fließtext darüber nennt für Klasse 1 „22.6%“, beides S. 133 (PDF 147)); annotiert 38 / 17 / 16 / 8 Lemmata, davon 41 in der repräsentativen und 38 in der „high correlation“-Stichprobe (S. 133 (PDF 147), Tab. 5.10).
- Mehrere Senses: laut S. 135 Fn. 1 (PDF 149) nur 2 von über 15.000 Belegen; „kein Sense“: 102 von über 15.000 (S. 135 Fn. 2 (PDF 149)). Für die κ-Berechnung aber 60 (Nomen) und 17 (Verben) Belege ausgeschlossen, bei denen eine Annotator:in mehrere Senses wählte (S. 138 Fn. 1 (PDF 152)). Die Zahlen beziehen sich offenbar auf verschiedene Stufen (einzelne Annotator:in gegenüber Endfassung); die Arbeit sagt das nicht ausdrücklich.
- Im Korpusvergleich (Tab. 5.11) führt die Arbeit für die TüBa-D/Z 15.505 annotierte Tokens, im Mittel 142 pro Lemma, Polysemie „ca. 3“, und als einziges der vier deutschen Korpora „Update of sense inventory: yes“ (S. 142 (PDF 156)).
- Release 9.1 (Gold für die Experimente): 17.910 Belege (8.803 Nomen, 9.107 Verben), Mittel 164 pro Lemma, Polysemie 3,2 (S. 158 (PDF 172), Tab. 6.4); davon 107 ohne Sense und 23 mit mehreren Senses (S. 150 bis 151 (PDF 164 bis 165), Tab. 6.1). Für überwachte WSD 16.738 Belege zu 92 Lemmata, 11.185 Training, 5.553 Test (S. 159 (PDF 173), Tab. 6.5).
- IAA: Dice-Mittel 96,4 % (Nomen), 93,7 % (Verben); κ 85,4 und 82,4 (S. 138 (PDF 152)). Einzelwerte in Tab. 5.4 und 5.5 (S. 128, 130 (PDF 142, 144)); niedrigste Nomen: *Höhe* 65,8 % (κ 11,3), *Kette* 73,9 % (κ 62,5); niedrigste Verben: *kündigen* 71,4 % (κ 42,9), *fressen* 72,7 % (κ 54,3), *verschwinden* 73,8 % (κ 47,4), *holen* 74,2 % (κ 65,4), *wiedergeben* 76,2 % (κ 40,0) (S. 138 bis 140 (PDF 152 bis 154)).

**deWaC** (Broscheit et al. 2010, aktualisiert): 1.083 Belege zu 37 Lemmata (4 Adj., 18 Nomen, 15 Verben), Polysemie 5,7; 57 ohne Sense; Kontexte gegenüber dem Original erweitert (S. 161 bis 163 (PDF 175 bis 177), Tab. 6.6).

**MFS-Baseline** (ZeroR, Kap. 8, außerhalb des Auftrags nachgeschlagen, F1 auf dem Testset, mikro-gemittelt): WebCAGe 80,49 (Adj.) / 79,96 (Nomen) / 76,92 (Verben); TüBa-D/Z 80,54 (Nomen) / 68,19 (Verben); deWaC 60,00 / 60,20 / 48,17 (S. 261 (PDF 275), Tab. 8.4; an der Textebene geprüft). Auf der TüBa-D/Z mit manuellen Baumbank-Merkmalen erreicht Vote 90,71 (Nomen) / 86,71 (Verben), SMO 90,57 / 86,53 (ebd.); der Abstand zur MFS beträgt dort also rund 10 Punkte bei Nomen und 18 bei Verben. Für die Verbstichproben liegt die MFS bei 70,91 (repräsentativ) und 69,89 (high correlation), je Korrelationsklasse zwischen 48,08 und 80,40 (S. 285 (PDF 299), Tab. 8.10; an der Textebene geprüft). Die Arbeit sagt, die MFS sei wegen schiefer Verteilung schwer zu schlagen, „usually ... only by a small margin“ (McCarthy 2009), ihre eigenen Klassifikatoren lägen aber meist deutlich darüber (S. 264 (PDF 278)). Alle Ergebnisse sind mikro-gemittelt (S. 26 (PDF 40), 2.2.2).

## Wörtliche Stellen

> „the annotation guidelines allow the assignment of multiple senses or no sense for a word occurrence“ (S. 135 (PDF 149))

> „There is very little if any information in the WSD literature on how to treat such annotations.“ (S. 150 (PDF 164), zu Annotationen ohne Sense oder mit mehreren Senses)

> „the no sense annotations are not ignored but regarded as a separate class“ (S. 151 (PDF 165))

> „For lemmas where both annotators always pick the same sense for all occurrences, Cohen's kappa is not informative.“ (S. 139 (PDF 153))

> „The reason for much higher IAA values for German than for English is the different number of distinct senses“ (S. 141 (PDF 155))

> „Due to the skewed distribution of word senses, the most frequent sense baseline (i.e., ZeroR) is difficult to beat“ (S. 264 (PDF 278), Kap. 8)

## Bezug zur Dissertation

- **Protokoll 6 (Statusliste, `MEHRERE`, `KEINE_PASST`):** Henrich erlaubt mehrere Senses und „kein Sense“ in den Richtlinien (S. 135 (PDF 149)) und hält fest, dass die Literatur dazu kaum etwas sagt (S. 150 (PDF 164)). Das stützt die eigene Statusliste und ist ein Beleg, dass sie begründet und nicht nur übernommen werden muss. Die Befunde „mehrere Senses selten, kein Sense häufiger, meist Idiome und übertragener Gebrauch“ (S. 134 bis 135 (PDF 148 bis 149)) sind eine Erwartung für den Pilot. Unterschied: Henrich hat nur „kein Sense“ mit Kommentar; das Protokoll trennt `KEINE_PASST`, `LEMMA_FALSCH`, `KONTEXT_UNZUREICHEND` und `TEXT_DEFEKT`. Die Markierung „idiomatisch“ oder „übertragen“ im Kommentarfeld (S. 137 (PDF 151)) ist ein Kandidat für einen Ursachencode.
- **Protokoll 9.2 (Bewertungsregel bei `MEHRERE`):** Henrich nennt fünf Optionen und verwirft (iii) „richtig, wenn einer der Gold-Senses getroffen“, weil sie die Ergebnisse leicht überschätzt (S. 152 (PDF 166)). Genau (iii) ist die Regel des Protokolls. Das ist kein Grund, sie zu ändern, aber ein Einwand, der im Text beantwortet werden sollte, etwa mit einer Sensitivitätsanalyse nach (i) Teilpunkte (Dice) oder (ii) Ausschluss.
- **Protokoll 9.1 (Agreement-Maße, Zufallsmodell pro Lemma, Prävalenz):** Henrich rechnet Dice mit Teilübereinstimmung (ähnlich MASI) und κ pro Lemma, mittelt dann (S. 138 (PDF 152)). Die Fälle *Bein* (κ −1,3 bei 97,4 % Übereinstimmung) und *existieren*/*vorschreiben* (κ 0,0) sind deutsche Belege für das Prävalenzproblem in 9.1, Punkt 4. Henrichs Lösung, Lemmata mit nur einem gewählten Sense aus dem κ-Mittel zu werfen (S. 138 Fn. 1 (PDF 152)), ist eine Variante, die das Protokoll ausdrücklich vermeiden sollte oder offenlegen muss, weil sie den Mittelwert nach oben verschiebt. Das Protokoll hat pro Lemma meist nur ein Token; κ pro Lemma wie bei Henrich ist dort nicht rechenbar, daher die Konstruktion in 9.1, Punkt 3.
- **Protokoll 7, Schritt 6 (Adjudikation, Doppelrolle):** Bei Henrich war die Autorin selbst eine der zwei Annotator:innen, die zweite eine Hilfskraft desselben Projekts; adjudiziert hat die Lexikografin, die das Inventar pflegt (S. 134 Fn. 1, S. 135 (PDF 148, 149)). Das ist dieselbe Doppelrolle wie Julias, ohne dass die Arbeit sie als Einschränkung nennt. Für das Protokoll ist das ein Präzedenzfall, dass die Konstellation üblich ist, und zugleich ein Argument für die dritte Person und die Offenlegung.
- **Protokoll 2 und 5 (Inventar fest, kein Nachtragen):** Henrich ergänzt GermaNet während der Annotation um fehlende Senses (*Mann* als Zähleinheit; S. 136 (PDF 150)) und nennt das übliche Praxis, wenn die Gruppe das Inventar pflegt. Das Protokoll hält das Inventar fest und sammelt Lücken als `KEINE_PASST`. Henrichs Fall *Kette* zeigt den Preis eines Umbaus mitten in der Annotation: Die zwei Annotator:innen arbeiteten auf verschiedenen Inventarständen, die IAA sank auf 73,9 % (S. 138 (PDF 152)). Das stützt das Einfrieren des Inventars mit Prüfsumme (Protokoll 4.10, 10).
- **Protokoll 4 (Stichprobe):** Henrichs Auswahl nach Mindestfrequenz, Ausgewogenheit von Frequenz und Polysemie und Wortart (S. 127 (PDF 141)) ist eine Lexical-Sample-Auswahl mit vielen Belegen pro Lemma, also das Gegenmodell zu 1 Token pro Paar aus Lemma und Wortart. Ihr Befund, dass die IAA bei Nomen nicht, bei Verben schwach mit der Polysemie korreliert (S. 139 bis 141 (PDF 153 bis 155)), ist eine Hypothese für das gemischte Modell in 4.6 (Polysemie × Wortart). Das Lemma-Panel (4.5) kommt Henrichs Design am nächsten.
- **Protokoll 6 (Kontext):** Henrich zeigt Satz plus vorangehenden Satz und den ganzen Artikel auf Klick (S. 138 (PDF 152)); das entspricht dem Vorschlag „begrenzter Ausschnitt, auf Knopfdruck größer“ und liefert einen Richtwert für offenen Punkt 4 in Protokoll 12. Anders als im Protokoll wird nicht protokolliert, ob erweitert wurde.
- **Protokoll 6 und `knowledge/data.md` B13 (Erläuterungen zu Senses):** Henrich begründet die Wiktionary-Definitionen damit, dass Annotator:innen ohne Definitionen Senses schwer unterscheiden (S. 3 (PDF 17)). Die MHDBDB-Senses haben fast keine Definitionen, nur Begriffsnamen; das ist ein Argument, im Pilot zu messen, ob Begriffsgruppen ausreichen.
- **Protokoll 9.2 (MFS):** Henrich bestimmt MFS als häufigsten Sense in den Trainingsdaten desselben Korpus (2:1-Aufteilung) und vergleicht nur überwachte Systeme mit ihr (S. 27 (PDF 41); S. 185 (PDF 199)). Das Protokoll lernt MFS aus Silber ohne die Stichprobe, vergleicht aber ein nicht überwachtes LLM damit. Ihre Aussage, aus automatisch geernteten Daten lasse sich keine MFS gewinnen (S. 143 (PDF 157)), ist ein Hinweis, dass die Herkunft der Silberdaten die MFS mitbestimmt (D1 gegenüber D0, Protokoll 3).
- **`LITERATUR-IAA.md`, Typische Werte:** Die TüBa-D/Z-Werte (96,4 / 93,7 %, κ 85,4 / 82,4) sind eine deutsche Referenz für ein grobkörniges Wordnet-Inventar mit 2,8 bis 4 Senses pro Lemma; die Arbeit führt die hohen Werte auf die geringe Sense-Zahl zurück (S. 141 (PDF 155)). Für das Protokoll mit Median 5 Senses in der Stufe 4+ (Protokoll 4.3) ist das eher eine Obergrenze.

## Grenzen und Einwände

- Gegenwartsdeutsch (Zeitung, Web), Wordnet-Inventar mit Definitionen aus Wiktionary. Für Mittelhochdeutsch ohne Muttersprachler:innen und für ein onomasiologisches Inventar (Begriffsgruppen statt Synsets) sagt die Arbeit nichts. Die hohen IAA-Werte beruhen nach der Arbeit selbst auf geringer Polysemie (S. 141 (PDF 155)).
- Die Annotator:innen kannten GermaNet, eine war die Autorin; die Adjudikatorin pflegte das Inventar und durfte es ändern. Eine Prüfung der Adjudikation durch Dritte oder ein Agreement zwischen Annotator:innen und Gold wird nicht berichtet (nur IAA zwischen den zwei Annotator:innen).
- In den gelesenen Kapiteln keine Pilotrunde, keine Angabe zur Richtlinienversion, keine Angabe, ob die Annotator:innen blind gegenüber den Entscheidungen der anderen waren, außer „independently“ (S. 134 (PDF 148)).
- IAA wird als Dice-Mittel und als κ-Mittel pro Wortart berichtet; κ schließt Mehrfach-Sense-Belege und Lemmata mit nur einem gewählten Sense aus (S. 138 Fn. 1 (PDF 152)). Konfidenzintervalle fehlen.
- Die Inventaränderungen während der Annotation (*Kette*, *holen*) senken die IAA und machen die Werte dieser Lemmata schwer deutbar.
- Interne Widersprüche in den Zahlen, alle am Seitenbild bestätigt, also Fehler der Vorlage und nicht der Umwandlung: Mehrfach-Senses in der TüBa-D/Z „2 von über 15.000“ (S. 135 Fn. 1 (PDF 149)), 60 + 17 Belege mit Mehrfachwahl einer Annotator:in (S. 138 Fn. 1 (PDF 152)) und 23 in Release 9.1 (Tab. 6.1, S. 151 (PDF 165)); Klasse 1 der Verben 22,6 % im Text, 21,6 % in Tab. 5.10 (S. 133 (PDF 147)); annotierte Verbbelege 7.967 (Tab. 5.3, S. 128 (PDF 142), und Text S. 129 (PDF 143)), 7.950 als Summe in Tab. 5.10, 7.970 als Summe der Klassenspalten derselben Zeile (S. 133 (PDF 147)) und 7.933 als Summe der Frequenzspalte in Tab. 5.5 (S. 130 (PDF 144), eigene Nachrechnung); häufigstes Verb *heißen* 709 Belege in Tab. 5.5, „710 times“ im Text (S. 129 (PDF 143)). Ohne Folgen für die IAA-Mittelwerte, aber beim Zitieren der Belegzahl die Tabelle angeben.
- MFS wird pro Korpus aus dessen Trainingsdaten bestimmt und auf einem Lexical Sample mit vielen Belegen pro Lemma gemessen; auf ein Design mit einem Token pro Lemma ist sie nicht direkt übertragbar.
- Die Experimente (Kap. 7, 8) liegen vor neuronalen Sprachmodellen; LLMs kommen nicht vor.

## Julias Markierungen außerhalb der gelesenen Kapitel

- **Abstract (S. i, PDF 3):** Forschung auf Englisch konzentriert, fehlende sense-annotierte Daten, GermaNet mit Wiktionary-Definitionen, zwei Korpora, wissensbasierte und überwachte Verfahren.
- **S. iv (PDF 6):** Hinweis auf die LaTeX-Vorlage der Universität Cambridge.
- **Kap. 2, S. 19 bis 23 (PDF 33 bis 37):** Definition von WSD („computationally assigning the most appropriate senses ... predefined sense inventory“), Inventar als Wörterbuch, Lexikon oder Wordnet, Princeton WordNet, gemeinsames Prinzip „compare linguistic clues from the target word's context with the properties of each sense“, In-vitro-Evaluation, Knowledge Acquisition Bottleneck, All-Words gegenüber Lexical Sample, Coverage, Precision, Recall, F1.
- **Literaturverzeichnis (S. 363 und 365, PDF 377 und 379):** Navigli 2009 (ACM Computing Surveys) und Palmer 2000 (*Consistent Criteria for Sense Distinctions*).

Die Markierungen in Kap. 5 (S. 106 bis 144) und Kap. 9 (S. 291 bis 292) sind oben in Kernaussagen und Bezug eingearbeitet, besonders 5.3.2 bis 5.3.4 (Auswahl, Annotationsprozess, IAA-Werte) und 5.5.

## Julias Notizen im PDF

- S. 111 (PDF 125), neben dem Absatz zur semi-automatischen Erstellung von WebCAGe und zur teuren manuellen Annotation: „das ist der punkt“.
- S. 113 (PDF 127), bei Abb. 5.1 (Sense-Zuordnung GermaNet und Wiktionary am Beispiel *Bogen*): „vgl mhdbdb zur veranschaulichung von disambiguität“.
- S. 127 (PDF 141), beim Satz zur Lexical-Sample-Entscheidung wegen des maschinellen Lernens: „bottlenecm !!“ (gemeint wohl Bottleneck).
- S. 128 (PDF 142), bei Tab. 5.4 (IAA und κ pro Nomen): „interessant anzusehen“.

Docling hat alle vier Notizen in den Text der `md`-Fassung eingemischt (S. 111, 113 und 127 in den Fließtext, S. 128 als Überschrift); sie sind nicht Teil des Werks.

## Weiterführend

- Henrich & Hinrichs 2013 und 2014 (zitiert S. 101, 108 (PDF 115, 122)): Vorveröffentlichungen der TüBa-D/Z-Annotation; laut Tübinger Repositorium erschien 2014 „Consistency of manual sense annotation and integration into TüBa-D/Z treebank“ in den TLT13-Proceedings (bibliografisch ○, nicht gelesen).
- Véronis 1998 (zitiert S. 134, 138, 141 (PDF 148, 152, 155)): Dice-Koeffizient für Teilübereinstimmung, Annotator:innen meiden Mehrfachantworten, englische IAA 73 % / 63 %.
- Raileanu et al. 2002 (zitiert S. 107, 134, 138 (PDF 121, 148, 152)): deutsches GermaNet-Korpus mit zwei Annotator:innen; Vorbild für den κ-Ausschluss von Mehrfach-Senses.
- Resnik & Yarowsky 1997, 1999 (zitiert S. 151 (PDF 165)): Teilpunkte bei Mehrfach-Senses; schon in `Navigli-2009-WSD-Survey.md` als Quelle für distanzgewichtete Bewertung genannt.
- Palmer et al. 2006 (zitiert S. 140, 141 (PDF 154, 155)): IAA-Anstieg von 71,3 auf 82 % bei gröberen Verb-Senses.
- Fellbaum et al. 2001 (zitiert S. 139 (PDF 153)): keine Korrelation zwischen IAA und Polysemie bei Nomen.
- Passonneau et al. 2012 (MASC; zitiert S. 105, 134, 135 (PDF 119, 148, 149)): lemmaweise Annotation, Adjudikation, Inventarupdate.
- Broscheit et al. 2010 (zitiert S. 107, 161 (PDF 121, 175)): deWaC-Lexical-Sample, Auswahl über Übersetzung des Senseval-2-Testsets.
