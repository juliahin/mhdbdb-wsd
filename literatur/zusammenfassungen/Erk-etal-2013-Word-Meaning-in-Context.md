# Erk, McCarthy & Gaylord 2013: Measuring Word Meaning in Context

**Datei:** `pdf/Erk-etal-2013-Word-Meaning-in-Context.pdf` (nur lokal; 44 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene bis zum Literaturverzeichnis gelesen; Tab. 10 und 11 (S. 525) und die DOI auf S. 511 am Seitenbild geprüft, übrige Tabellen an der Textebene (dort sauber lesbar). Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology J13-3003 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 510 + n (PDF 1 = S. 511, PDF 44 = S. 554; Seitenzahlen in der Fußzeile, S. 511 ohne Zahl). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Erk, Katrin, Diana McCarthy & Nicholas Gaylord (2013). Measuring Word Meaning in Context. *Computational Linguistics* 39(3), S. 511 bis 554.
- **DOI/URL:** 10.1162/COLI_a_00142 (aufgelöst über doi.org auf direct.mit.edu, Crossref: Bd. 39, Heft 3, S. 511 bis 554, gedruckt September 2013; abgerufen 2026-11-16). **Die im PDF gedruckte DOI „10.1162/COLI_a_000142“ (S. 511, eine Null zu viel) löst nicht auf** (doi.org und Crossref 404, 2026-11-16). https://aclanthology.org/J13-3003/
- **Lizenz:** CC BY-NC-SA 3.0 nach der Copyright-FAQ der ACL Anthology (ACL-Material vor 2016, abgerufen 2026-11-16); im PDF nur „© 2013 Association for Computational Linguistics“ (S. 511); Crossref nennt keine Lizenz.
- **Art:** begutachteter Zeitschriftenartikel (eingereicht 3.11.2011, angenommen 25.6.2012; S. 511)
- **Sprache:** Englisch

## Worum es geht

Die Arbeit fragt, ob sich Wortbedeutung im Kontext durch **graduelle Urteile** annotieren lässt, und zwar mit ungeschulten Annotator:innen, deren Intuition erfasst werden soll (S. 512). Sie führt zwei Aufgaben ein: **WSsim**, die Bewertung jedes WordNet-Sense eines Belegs auf einer Skala von 1 bis 5, und **Usim**, die Bewertung der Bedeutungsähnlichkeit von Belegpaaren desselben Lemmas ohne Inventar (S. 519). In zwei Runden mit drei bzw. acht Personen ergeben sich mittlere paarweise Spearman-Korrelationen von 0,50 bis 0,62 (S. 524 bis 530). Beide Aufgaben korrelieren stark miteinander, mit klassischer Einzel-Sense-Annotation und mit Paraphrasen (S. 536 bis 537). Personen gaben oft mehreren Senses Höchstwerte, auch Senses, die sonst gegenläufig bewertet werden, was sich durch kein gröberes Inventar auflösen lässt (S. 525, 545 bis 546).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Die Annahme disjunkter Senses mit klaren Grenzen wird von Lexikograf:innen, Linguist:innen und Psycholog:innen bezweifelt; Kategorien haben „fuzzy boundaries“ und Mitglieder unterschiedlicher Typikalität. | S. 512, 516 bis 517 | referiert (Kilgarriff 1997; Hanks 2000; Tuggy 1993; Cruse 1995; Rosch 1975; Hampton 2007) |
| Kilgarriff (1997) bezweifelt allgemeine, aufgabenunabhängige Senses; Sense-Unterscheidungen ergäben nur in Bezug auf eine Aufgabe Sinn. | S. 516, Abschnitt 2.2.1 | referiert |
| Ungeschulte Annotator:innen werden gewählt, weil eine gründliche Schulung auf vordefinierte Senses sie dazu bringen könnte, diese binär zu vergeben. | S. 512 | Begründung der Autor:innen |
| Ziel ist nicht höhere Übereinstimmung; Skalenurteile erreichten kaum höhere exakte Übereinstimmung als binäre, und individuelle Unterschiede sollen erfasst werden. | S. 513 | Festlegung der Autor:innen |
| WordNet-ITA liegt je nach Polysemie und Verwandtschaft der Senses bei 67 bis 78 %; gröbere Inventare (SALSA 86 %, OntoNotes meist > 90 %) heben sie, aber manche Lemmata (*leave*) erreichen 90 % auch nach mehrfachem Umbau nicht. | S. 514 bis 515, Tab. 1 | referiert |
| Nach Passonneau et al. 2010 hängt die ITA an Konkretheit des Sense, Spezifik des Kontexts und Ähnlichkeit der Senses; nur der dritte Faktor lässt sich durch ein anderes Wörterbuch ändern. | S. 514 | referiert, Folgerung der Autor:innen |
| Übereinstimmung als Mittel paarweiser Spearman-Korrelationen: WSsim-1 ρ = 0,504 (0,47 bis 0,54), WSsim-2 0,60 (0,52 bis 0,72), Usim-1 0,548 (0,50 bis 0,64), Usim-2 0,62 (0,42 bis 0,73); alle Paare p ≪ 0,001. | S. 524 bis 525, 529 bis 530, Tab. 9, 10, 16, 17 | eigenes Ergebnis |
| Personen nutzen die ganze Skala; Rang 1 am häufigsten, dann 5, aber viele Zwischenwerte, nicht nur von einer Minderheit. | S. 526, 530, Tab. 12 | eigenes Ergebnis |
| Mehrere Senses mit Höchstwert 5 von derselben Person: WSsim-1 46 %, WSsim-2 30 % der Sätze, gegenüber SemCor 0,3 % und SE-3 8 %. | S. 525, Tab. 11 | eigenes Ergebnis |
| **Reihenfolgeeffekt:** Wer die klassische Bestannotation (WSbest) vor WSsim machte, vergab seltener mehrere Fünfer (23 % gegen 36 %) und häufiger die 1 (0,727 gegen 0,664). Umgekehrt wählten Personen, die WSsim zuerst machten, in WSbest öfter mehrere Senses (0,15 gegen 0,11; χ², p = 0,02). Annotator:innen in einer Bedeutungsaufgabe sind also von einer vorher gemachten Aufgabe beeinflusst. | S. 525 bis 528, 533, Tab. 11, 12, 21 | eigenes Ergebnis |
| In Usim gibt es mehr Mittelwerte als in WSsim: „The sense definitions suggest a categorization that may bias annotators towards categorical choices.“ | S. 530 | Deutung der Autor:innen |
| Klassische Einzel-Sense-Annotation (WSbest): paarweise Übereinstimmung 0,574 über alle Items, 0,626 bei Items mit je einem gewählten Sense, 0,638 bei Items mit einer Antwort und nur den vier Personen, die WSbest zuerst machten; vergleichbar mit SE-3 (0,628). | S. 533 bis 534 | eigenes Ergebnis, Vergleich referiert |
| Usim-Urteile erfüllen die Dreiecksungleichung: 99,2 % der Satztripel in Runde 1, alle in Runde 2; einzeln 93,6 bis 98,4 %. Ähnlichkeit von Belegen eines Worts im Kontext ist also metrisch, anders als Tverskys Ähnlichkeit zwischen Wörtern ohne Kontext. | S. 531 bis 533, Tab. 19, 20 | eigenes Ergebnis |
| Die Dreiecksungleichung kann künftige Usim-Annotation sparen (dritte Kante begrenzt) und grobe Verstöße als unzuverlässige Urteile kenntlich machen. | S. 533 | Vorschlag der Autor:innen |
| WSsim korreliert mit klassischen Labels (SE-3 ρ = 0,416, SemCor 0,425, WSbest 0,483), mit Usim (R1 ρ = −0,596, R2 −0,816; negativ, weil Distanz gegen Ähnlichkeit) und mit Paraphrasen (Tab. 23: Usim 0,590 und 0,764, WSsim −0,495 und −0,749). | S. 536 bis 537, Tab. 23 | eigenes Ergebnis |
| Usim „reflects word meaning but is not tied to any given sense inventory“; es eignet sich zur Prüfung von Inventaren und als inventarunabhängiges Gold für Word Sense Induction. | S. 537, 538, 550 bis 551 | Folgerung der Autor:innen |
| Die WSsim-Urteile folgen keiner festen Gruppierung: Zwei Senses aus verschiedenen groben Gruppen (OntoNotes, SemEval-2007 EAW) erhielten in 28 bis 78 % der Sätze beide ≥ 3; zwei Senses derselben Gruppe in 20 bis 60 % der Sätze stark verschiedene Werte (≤ 2 und ≥ 4). | S. 540 bis 542, Tab. 26, 27 | eigenes Ergebnis |
| Selbst über die Urteile negativ korrelierte Senses bekommen im selben Satz beide positive Werte (Runde 1: 135 Sätze mit j ≥ 3); Personen „mix and match“ Senses pro Satz, statt implizit gröbere Senses zu benutzen. | S. 545 bis 546 | eigenes Ergebnis |
| Grobe Gruppen trennen Usim im Mittel gut (gleiche Gruppe 4,0 bzw. 4,1, verschiedene 1,9 bzw. 2,0), aber nicht bei jedem Lemma (*new.a*, *shed.v*). | S. 547, Tab. 29 | eigenes Ergebnis |
| Homonymie und Polysemie werden nicht unterschieden. | S. 517 | Festlegung der Autor:innen |

## Daten, Methode, Zahlen

- **Skala (beide Aufgaben):** 1 völlig verschieden, 2 überwiegend verschieden, 3 ähnlich, 4 sehr ähnlich, 5 identisch (Tab. 4, S. 519). In WSsim jede Bewertung jedes Sense, in Usim jedes Belegpaar; „I don't know“ nur in Usim (S. 520, Anm. 9). Kommentarfeld bei jedem Item; zurückblättern erlaubt, überspringen nicht (S. 520).
- **Runde 1 (R1):** je drei Personen, getrennte Gruppen für WSsim und Usim. WSsim-1: 430 Sätze zu 11 Lemmata (8 Lemmata mit je 25 Sätzen aus SemCor und 25 aus SE-3, 3 Lemmata mit je 10 aus LEXSUB). Usim-1: 34 Lemmata aus LEXSUB mit je 10 Sätzen (*bar.n* 9), alle Paare, 45 pro Lemma, zusammen 1.521 Vergleiche pro Person. Ein Satz Kontext (S. 521).
- **Runde 2 (R2):** acht Personen machen alle vier Aufgaben (Usim-2, SYNbest, WSsim-2, WSbest) an denselben 26 Lemmata mit je 10 Sätzen aus LEXSUB: 260 Belege, 1.170 Paare; Reihenfolge von WSsim und WSbest in zwei Vierergruppen gewechselt; ein Satz Kontext mehr auf jeder Seite (S. 520 bis 521).
- Nach Entfernen der Paare mit „don't know“ (9 in R1, 28 in R2) bleiben 1.512 bzw. 1.142 Paare (S. 528).
- **Maße:** paarweises Spearman ρ für die Skalenaufgaben, gemittelt über alle Paare; für WSbest Überschneidung geteilt durch die größere Auswahl, für SYNbest Überschneidung geteilt durch die Vereinigung (Gl. 1 und 2, S. 534 bis 535). z-Werte wurden zusätzlich gerechnet, ändern aber keine Signifikanz (S. 522, Anm. 12).
- **Durchschnittliche Spannweite und Varianz pro Item** (Tab. 18, S. 530): WSsim-1 1,78 / 1,44; WSsim-2 1,55 / 0,71; Usim-1 1,41 / 0,92; Usim-2 2,50 / 1,12. Die Spannweite in Usim-2 schwankt stark je Lemma (*fire.v* 1,33 bis *function.n* 3,58), was die Autor:innen als Maß für die Schwierigkeit eines Lemmas ansehen (S. 531).
- **Alle Personen bleiben im Gold**, weil jede auf irgendeiner Aufgabe gut mit den anderen übereinstimmt und keine durchgehend abfällt (S. 535).
- **Tab. 1 (S. 515):** ITA SemCor 78,6 %, SensEval-3 72,5 %, SensEval-1 Lexical Sample 66,5 %, SensEval-3 Lexical Sample 67,3 %, SALSA 86 %, OntoNotes „most > 90%“.

## Wörtliche Stellen

> „Training annotators in depth on how to distinguish predefined hand-crafted senses could influence them to assign those senses in a binary fashion.“ (S. 512)

> „The sense definitions suggest a categorization that may bias annotators towards categorical choices.“ (S. 530)

> „This demonstrates that annotators in a word meaning task can be influenced by factors outside of the current annotation task, in this case another annotation task that they have done previously.“ (S. 526)

> „It reflects word meaning but is not tied to any given sense inventory.“ (S. 537)

## Bezug zur Dissertation

**1. A31 (Vorgabe des Inventars, Ankereffekt) und offener Punkt 21 (Literaturprüfung).** Das Werk ist bisher die stärkste Stütze im Bestand für die Frage, ob ein vorgegebenes Inventar das Urteil lenkt, aber nur in einer schwachen Form:
- Die Autor:innen meiden Schulung auf vordefinierte Senses ausdrücklich, weil sie zu binären Urteilen führen könnte (S. 512). Das ist eine Begründung, kein Befund.
- Befund ist der **Reihenfolgeeffekt** (S. 525 bis 528, 533): Eine vorher gemachte Aufgabe verschiebt das Urteil messbar. Das ist kein Ankereffekt durch Antwortoptionen im engen Sinn, aber ein Beleg, dass die Rahmung durch eine Aufgabe auf die nächste durchschlägt. Für A31 heißt das: Der Lesart-Schritt vor den Karten ist selbst eine Vorbedingung, die die Kartenwahl beeinflussen kann, und der Ablauf `lesart-zuerst` gegen `direkt` ist genau so ein Reihenfolgevergleich.
- Die Deutung, dass Definitionen zu kategorialen Urteilen verleiten (S. 530), steht als Vermutung neben dem Befund, dass Usim mehr Mittelwerte hat (Tab. 12).
- Kilgarriff 1997, das offener Punkt 21 als zu prüfen nennt, wird hier referiert (S. 512, 516): *Computers and the Humanities* 31(2), S. 91 bis 113 (Angabe nach dem Literaturverzeichnis, S. 552; nicht am Original geprüft). Der Bezug ersetzt die eigene Lektüre nicht.

**2. A31 und offener Punkt 22 (Weg C).** Usim ist der unmittelbare Vorläufer von DURel (Schlechtweg et al. 2018, S. 170 bis 172, übernehmen Richtlinien und Maß). Für Weg C bietet die Arbeit: das Verfahren, Übereinstimmungswerte (ρ 0,548 und 0,62), die Dreiecksungleichung als Sparregel und Plausibilitätsprüfung (S. 533), und die Befunde, dass Usim mit Sense-Annotation stark korreliert (bis −0,816, S. 537) und dass Usim gröbere Inventare prüfen kann (S. 547). Für die Dissertation hieße das: Ein Usim-Teil könnte die MHDBDB-Senses prüfen (trennen die Begriffsgruppen, was Personen als nah oder fern empfinden?), statt sie vorauszusetzen. Das ist ein Vorschlag, keine Aussage der Arbeit.

**3. PROTOKOLL §6 (`MEHRERE`, Sicherheit) und §9.1 Punkt 1 (MASI).** Dass Personen oft mehreren Senses Höchstwerte geben (bis 46 %, Tab. 11) und dabei auch gegenläufige Senses kombinieren (S. 545 bis 546), stützt einen eigenen Status für Mehrfachpassung und eine Teilübereinstimmung wie MASI. Es warnt zugleich: Bei einer Bestwahl ohne `MEHRERE` liegt der Anteil in klassischen Korpora bei 0,3 bis 8 %; wie oft `MEHRERE` vergeben wird, hängt also stark an der Aufgabenform.

**4. PROTOKOLL §9.1 Punkt 7 (zwei Ebenen des Begriffssystems).** Die Befunde zu OntoNotes und EAW (Tab. 26, 27, S. 541) zeigen, dass ein vorab definiertes grobes Inventar nicht alle Fälle erfasst, in denen Personen zwei Senses für passend halten, und umgekehrt Senses einer Gruppe stark verschieden bewertet werden. Das stützt die Festlegung, die grobe Ebene vorab zu definieren und die Übereinstimmung auf ihr nicht als Ersatz für die feine zu lesen.

**5. LITERATUR-IAA.md, Abschnitt „Historische Sprachen“.** Dort steht „Erk et al. 2013 ρ ≈ 0,50 bis 0,62 (graduell) gegenüber 0,638 Einzelsense ○“. Die Zahlen sind am Volltext bestätigt (S. 524, 525, 529, 530, 534), aber der Vergleich mischt zwei Maße: 0,50 bis 0,62 sind Rangkorrelationen über Skalenurteile, 0,638 ist eine Rohübereinstimmung (Anteil), und zwar nur für Items mit einer Antwort und nur für die vier Personen, die WSbest zuerst machten. Über alle Items und acht Personen beträgt sie 0,574 (S. 534). Vorschlag für die Zeile: „ρ 0,50 bis 0,62 (Skalenurteile, paarweise); klassische Bestannotation derselben Personen 0,574 paarweise Rohübereinstimmung (0,638 eingeschränkt), nicht mit ρ vergleichbar“.

**6. PROTOKOLL §4.3 und §9.1 Punkt 6 (Schwierigkeitsfaktoren).** Die Arbeit sieht die Streuung der Urteile pro Lemma als Maß für die Schwierigkeit eines Lemmas (S. 531) und referiert drei Faktoren nach Passonneau et al. 2010 (S. 514). Das stützt das Lemma-Panel (§4.5), das Lemma- von Kontextschwierigkeit trennt.

**7. Übertragbarkeit auf Mittelhochdeutsch.** Das Verfahren setzt intuitive Urteile von Sprecher:innen voraus (S. 512). Für Latein ohne Muttersprachler:innen wurde in SemEval-2020 auf Urteile „Beleg gegen Definition“ nach WSsim umgestellt (Schlechtweg et al. 2020, S. 5); das ist für Mittelhochdeutsch der näherliegende Fall als Usim.

## Grenzen und Einwände

- Englisch, WordNet 3.0, Gegenwartssprache; Sätze aus SemCor, SE-3 und LEXSUB.
- Kleine Lemmazahlen (11, 34, 26) und je Lemma 10 bis 50 Sätze; die Lemmata wurden gezielt mit breiter Bedeutungsspanne gewählt (S. 521), nicht zufällig.
- Übereinstimmung nur als Rangkorrelation, keine Zufallskorrektur für die Skalenaufgaben.
- Die Unterschiede zwischen R1 und R2 (Lemmata, Kontext, Zahl der Personen, Reihenfolge) lassen sich nicht sauber trennen; die Autor:innen sagen das selbst (S. 525, 527).
- Der Reihenfolgeeffekt ist an zwei Gruppen zu je vier Personen gemessen.
- Die Personen waren bewusst ungeschult; der Goldstandard der Dissertation arbeitet mit Richtlinien und fachkundigen Annotator:innen, der Effekt der Aufgabenform kann dort anders ausfallen.
- Für ein onomasiologisches Inventar (Senses als Begriffsgruppen ohne Definitionstext) nicht geprüft; WSsim braucht Sense-Beschreibungen, die Karten der MHDBDB sind Begriffspfade.

## Weiterführend

- Kilgarriff 1997, I don't believe in word senses, *Computers and the Humanities* 31(2), S. 91 bis 113 (S. 512, 516): offener Punkt 21.
- Brown 2008, Choosing sense distinctions for WSD: Psycholinguistic evidence, ACL-08: HLT Short Papers, S. 249 bis 252, und Brown 2010, Dissertation Colorado (S. 517): verarbeitungspsychologischer Beleg für graduelle Bedeutungsnähe.
- McCarthy & Navigli 2007 und 2009, English lexical substitution task (S. 517, 535): Paraphrasen statt Senses.
- Chen & Palmer 2009, *Language Resources and Evaluation* 43, S. 181 bis 208 (S. 514, 539): OntoNotes-Gruppen, 90 %-Kriterium.
- Palmer, Dang & Fellbaum 2007, Making fine-grained and coarse-grained sense distinctions, *Natural Language Engineering* 13, S. 137 bis 163 (S. 514, 538).
- Passonneau et al. 2010 (S. 514): schon zusammengefasst (`Passonneau-etal-2010-WS-Annotation-Multiple.md`).
- Hampton 2007, Typicality, graded membership, and vagueness, *Cognitive Science* 31, S. 355 bis 384 (S. 512).
- Tversky 1977 und Tversky & Gati 1982 (S. 513, 531): Nichtmetrik von Ähnlichkeitsurteilen.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
