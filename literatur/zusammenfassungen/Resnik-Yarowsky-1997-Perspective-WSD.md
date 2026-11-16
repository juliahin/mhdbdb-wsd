# Resnik & Yarowsky 1997: A Perspective on Word Sense Disambiguation Methods and Their Evaluation

**Datei:** `pdf/Resnik-Yarowsky-1997-Perspective-WSD.pdf` (nur lokal; 8 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen. Das PDF ist ein Scan mit fehlerhafter OCR-Textebene; Formeln und Tab. 2 bis 5 deshalb am Seitenbild geprüft (PDF-Seiten 3, 4, 6). Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 78 + n (PDF 1 = S. 79, PDF 8 = S. 86; Seitenzahlen am Fuß jeder Seite). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Resnik, Philip & David Yarowsky (1997). A Perspective on Word Sense Disambiguation Methods and Their Evaluation. In: *Tagging Text with Lexical Semantics: Why, What, and How?* (SIGLEX-Workshop), Washington, DC, April 1997, S. 79 bis 86.
- **DOI/URL:** keine DOI (Anthology ohne DOI; Crossref-Suche nach dem Titel am 2026-11-16 ohne Treffer); https://aclanthology.org/W97-0213. Titel, Autoren und Workshoptitel laut Anthology ✔; Seiten 79 bis 86 am PDF ✔. „SIGLEX“, Washington, DC und April 1997 nur laut Literaturverzeichnis von Henrich (2015, PDF-Seite 385 von `Henrich-2015-WSD-GermaNet.pdf`); die Anthology nennt weder Ort, Monat, Herausgeber:innen noch Verlag ○.
- **Lizenz:** CC BY-NC-SA 3.0 (ACL Anthology, Material vor 2016, abgerufen 2026-11-16).
- **Art:** Positionspapier, Workshopbeitrag
- **Sprache:** Englisch

## Worum es geht

Die Autoren beschreiben den Stand der WSD 1997 in vier Beobachtungen (keine einheitliche Evaluation, Nutzen je nach Anwendung verschieden, zu wenig annotierte Daten, kaum Einigung über Verfahren) und machen vier Vorschläge (S. 79 bis 85): (1) Kreuzentropie als Maß neben der exakten Übereinstimmung, damit Wahrscheinlichkeit auf dem richtigen Sense Teilpunkte bringt; (2) Fehler nach semantischer oder kommunikativer Distanz zwischen Senses gewichten, etwa über die Hierarchie eines Wörterbuchs; (3) ein Evaluationsverfahren mit vorab geheimer, nach Kriterien und dann zufällig gezogener Wortliste, Annotation Wort für Wort, blinder Übereinstimmungsmessung, Konsens und eingefrorenem Code; (4) ein Inventar, das nur Unterscheidungen enthält, die in mehreren Sprachen lexikalisch verschieden ausgedrückt werden. Empirische Ergebnisse enthält das Papier nicht.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Evaluation in der WSD ist nicht standardisiert: verschiedene Wortmengen, Korpora und Maße; „nearly as many test suites as there are researchers“. | S. 79, Beobachtung 1 | Einschätzung |
| Der Nutzen von WSD hängt von der Anwendung ab: im Information Retrieval womöglich gering, in der maschinellen Übersetzung vielversprechender. | S. 79 bis 80, Beobachtung 2 | Einschätzung, teils referiert (Krovetz & Croft 1992; Wilks & Stevenson 1996) |
| Die sequenzielle Annotation aller Wörter eines Textes (WordNet-Semantic-Concordance) ergibt für die meisten polysemen Wörter zu wenige Belege (meist unter 10) und zwingt Annotierende, sich bei jedem Wort neu in dessen Inventar einzuarbeiten; das verlangsamt und senkt die Übereinstimmung innerhalb und zwischen Annotierenden. | S. 80, Beobachtung 3 | Behauptung der Autoren, nicht gemessen |
| Parallelkorpora können Übersetzungsunterschiede als praktischen Ersatz für Sense-Unterschiede liefern (*duty*: *devoir* / *droit*). | S. 80, Beobachtung 3 | Vorschlag |
| WSD nutzt viele Informationsquellen (lokale Kollokationen, semantische Klassen, Konsistenz im Diskurs) und ist stark lexikalisch, fast ein eigener Disambiguator pro Wort. Gegenbild ist das POS-Tagging (Tab. 1). | S. 80, Beobachtung 4 | Einschätzung mit Verweisen |
| **Vorschlag 1:** Die exakte Übereinstimmung („% correct“) bestraft alle Fehler gleich. Kreuzentropie −(1/N) Σ log₂ Pr(cs_i \| w_i, context_i) belohnt Wahrscheinlichkeit auf dem richtigen Sense cs_i und bestraft sehr niedrige stark (bei 0 unendlich). Beide Maße können nebeneinander auf denselben Testdaten stehen. | S. 81, Tab. 2 und Rechenbeispiel | eigener Vorschlag |
| Kreuzentropie sei fairer, „especially for the common case where several fine-grained senses may be correct and it is nearly impossible to select exactly the sense chosen by the human annotator“. | S. 81 | Begründung der Autoren |
| Für Systeme ohne (gute) Wahrscheinlichkeiten: Variante ohne Logarithmus, (1/N) Σ Pr(cs_i); bei 0/1-Ausgabe gleich der einfachen Genauigkeit. | S. 81 | eigener Vorschlag |
| **Vorschlag 2:** Fehler zwischen nahen Geschwistern in einer Sense-Hierarchie sollen wenig, Fehler zwischen Homographen viel kosten. Distanzmatrix aus einer Hierarchie (WordNet), aus mehreren Wörterbüchern, aus psycholinguistischen Ähnlichkeitsdaten oder aufgabenbezogen (Aussprache bei Sprachsynthese, Lexikalisierung bei Übersetzung). Beispiel *bank* mit Kosten 0 / 1 / 2 / 4 (Tab. 3 und 4). | S. 81 bis 82 | eigener Vorschlag |
| Zwei Maße mit Distanz: mittlere Distanz zwischen vergebenem und richtigem Sense, (1/N) Σ distance(cs_i, as_i); oder die nach Distanz gewichtete Wahrscheinlichkeitsmasse auf falschen Senses. Ohne Wahrscheinlichkeiten fallen beide zusammen. | S. 82 | eigener Vorschlag |
| **Vorschlag 3, Evaluationsrahmen:** großes Korpus; Inventar festlegen; Trainingsteil freigeben; aus einem Testteil eine Menge von M (z. B. 100) mehrdeutigen Wörtern ziehen, **ohne sie vorher bekannt zu geben**; alle Belege dieser Wörter annotieren, **jede:r Annotierende Wort für Wort** mit Konkordanz statt sequenziell durch den Text; Übereinstimmung Annotierende gegen Annotierende rechnen; bei Abweichungen Konsens, notfalls per Abstimmung; Code der Teilnehmenden **einfrieren**; Systeme taggen das ganze Testkorpus, ausgewertet werden nur die M Wörter; Vergleich von exakter Übereinstimmung, Kreuzentropie und Übereinstimmung zwischen Urteilenden (z. B. Cohens κ) als **Obergrenze**. | S. 82 bis 83 | eigener Vorschlag |
| Die Wortliste kann über beliebige Kriterien (Frequenz, Grad der Mehrdeutigkeit, Wortart) eingegrenzt und dann **zufällig** aus den Kandidaten gezogen werden. Weil die Wörter vorher unbekannt sind, müssen Systeme alle Wörter taggen können (Skalierbarkeit). | S. 83 | eigener Vorschlag |
| Wort-für-Wort-Annotation ergebe von Anfang an deutlich höhere Konsistenz; blinde Übereinstimmung, danach Besprechung liefert ein saubereres Testset, ohne die Obergrenze zu verfälschen. Pro Wort lassen sich Inventar und Richtlinien in mehreren Durchgängen prüfen, was für den ganzen Wortschatz zu teuer wäre. | S. 83 | Begründung der Autoren, nicht gemessen |
| **Vorschlag 4:** Das Inventar auf Unterscheidungen beschränken, die in mehreren Sprachen lexikalisch verschieden ausgedrückt werden; das liegt zwischen reinen Homographen (sehr grob) und allen Unterscheidungen eines einsprachigen Wörterbuchs. Beispiel *table* (Gegenstand gegen Tischrunde, deutsch *Tisch* / *Tischrunde*, aber auch *Tisch* für beides). | S. 84 | eigener Vorschlag |
| Tabelle von Sense-Nummern (WordNet) zu Übersetzungen in fünf Sprachen, u. a. Deutsch (*interest*: *Zinsen*, *Anteil*, *Interesse*; *bank*: *Ufer*, *Erdwall*, *Bank*, *Reihe*). | S. 84, Tab. 5 | eigenes Beispiel |
| Verschiedene Inventare begünstigen verschiedene Verfahren: WordNet Verfahren, die Taxonomien nutzen, LDOCE solche, die Sachgebietskodes nutzen. Eine Lösung, welches Inventar Standard sein soll, haben die Autoren nicht. | S. 85 | Einschätzung |

## Daten, Methode, Zahlen

Keine eigenen Daten oder Experimente. Rechenbeispiel zu Vorschlag 1 (Tab. 2 und die Illustration, S. 81, am Seitenbild geprüft): vier hypothetische Systeme für *interest* im Kontext „bought an interest in Lydak Corp.“; alle wählen den falschen Sense 1, geben dem richtigen Sense 2 aber 0,42 / 0,05 / 0,24 / 0,00. Kreuzentropie pro Instanz 1,25 / 4,32 / 2,05 / ∞. Tab. 4 (S. 82): Kosten 1 zwischen Untersenses desselben Sense, 2 zwischen Senses desselben Homographen, 4 zwischen Homographen.

## Wörtliche Stellen

> „However, a measure based on cross-entropy or perplexity would provide a fairer test, especially for the common case where several fine-grained senses may be correct and it is nearly impossible to select exactly the sense chosen by the human annotator.“ (S. 81)

> „An erroneous classification between close siblings in the sense hierarchy should be given relatively little penalty, while misclassifications across homographs should receive a much greater penalty.“ (S. 82)

> „Make sure each annotator tags all instances of a single word, e.g. using a concordance tool, as opposed to going through the corpus sequentially.“ (S. 83)

> „Step 4a can involve any form of criteria (frequency, level of ambiguity, part of speech, etc.) to narrow down to set of candidate words, and then employ random selection among those candidates.“ (S. 83)

## Bezug zur Dissertation

**Prüfauftrag zu `goldstandard/LITERATUR-IAA.md`** (Zeile Henrich 2015: „Teilwertung … Resnik & Yarowsky 1997, 1999 ○ (zitiert nach Henrich 2015, S. 151 bis 152)“):

- Henrich (2015, S. 151, PDF-Seite 165; am Volltext `literatur/md/Henrich-2015-WSD-GermaNet.md` geprüft) führt Resnik & Yarowsky 1997 und 1999 als Beleg für Option (i): Teilpunkte, wenn ein System einige, aber nicht alle annotierten Senses trifft.
- **Am Original von 1997 nur teilweise gedeckt.** Resnik & Yarowsky schlagen Teilpunkte vor, aber in anderem Sinn: für die **Wahrscheinlichkeit**, die ein System dem richtigen Sense gibt (Vorschlag 1), und für die **semantische Distanz** eines Fehlers (Vorschlag 2). Ihre Formeln setzen genau **einen** richtigen Sense cs_i pro Instanz voraus (S. 81, 82). Items mit mehreren Gold-Senses und eine Teilwertung durch Überlappung (wie Dice) behandeln sie nicht; die einzige Berührung ist die Begründung, dass oft mehrere feine Senses richtig sein können (S. 81). Die Fassung von 1999 liegt nicht vor und bleibt ○.
- **Vorschlag:** In LITERATUR-IAA und PROTOKOLL §9.2 (Einwand gegen die `MEHRERE`-Regel) Resnik & Yarowsky 1997 nicht als Quelle der Dice-Teilwertung führen, sondern höchstens als frühe Forderung nach Teilpunkten für Wahrscheinlichkeit und Distanz. Status für 1997 dann ✔ mit dieser Einschränkung.

**Weitere Bezüge:**

- **PROTOKOLL §4.3 und §4.4 (Zellen, Ziehung):** Vorschlag 3 nimmt die Logik der Hauptstichprobe vorweg: Wörter über Kriterien wie Frequenz, Mehrdeutigkeit und Wortart eingrenzen, dann zufällig ziehen (S. 83). Neben Kilgarriff 1998 ein früher, zitierbarer Beleg für die Schichtung nach Wortart × Frequenz × Polysemie. Unterschied: Resnik & Yarowsky annotieren dann **alle** Belege der gezogenen Wörter (Lexical Sample), die Dissertation zieht 1 Token pro Paar aus Lemma und Wortart.
- **PROTOKOLL §7, Schritt 4 (Reihenfolge der Items) und §8:** Resnik & Yarowsky raten, Wort für Wort zu annotieren, weil das ständige Neueinlesen in Inventare Tempo und Übereinstimmung senke (S. 80, 83; behauptet, nicht gemessen). Im Protokoll hat fast jedes Item ein eigenes Inventar, und die Itemreihenfolge wird zufällig gemischt. Das ist für die Hauptstichprobe unvermeidbar (1 Token pro Lemma), im Lemma-Panel (5 Tokens pro Paar, §4.5) aber eine Entscheidung: gemischt oder pro Lemma gebündelt. Die Bündelung senkt laut den Autoren den Aufwand, kann aber über Reihenfolgeeffekte Urteile angleichen (Beck et al. 2024, im Protokoll §7). Vorschlag: im Panel die Reihenfolge bewusst festlegen und begründen.
- **PROTOKOLL §7, Schritte 5 und 6 und §4.10 (Freeze 2):** Blinde Übereinstimmung vor der Besprechung, danach Konsens (S. 83), und eingefrorener Code der Systeme vor dem Testlauf (S. 83) entsprechen „Roh-IAA zuerst“ und dem Einfrieren der LLM-Konfiguration. Die geheime Wortliste ist ein frühes Gegenstück zum Schutz der Testdaten (PROTOKOLL §10).
- **PROTOKOLL §9.1, Punkt 7 und offener Punkt 12 (grobe Ebene):** Vorschlag 2 begründet, Fehler nach Abstand in einer Hierarchie zu gewichten (S. 81 bis 82). Mit dem Zahlencode des Begriffssystems (`knowledge/data.md`, B11) ließe sich neben der Zwei-Ebenen-Auswertung eine distanzgewichtete Auswertung definieren (z. B. Kosten nach gemeinsamer Oberbegriffsstufe). Das wäre eine neue Sekundärauswertung, nur als Vorschlag; sie müsste vor Freeze 2 festgelegt werden.
- **LLM-Konfiguration (§4.10) und Kreuzentropie:** Kreuzentropie setzt eine Wahrscheinlichkeitsverteilung über die Senses voraus. Gibt das LLM nur eine Kartennummer aus, ist das Maß nicht anwendbar; bei mehreren Läufen pro Item ergäbe die Verteilung der Antworten eine grobe Schätzung (A16, Option „Verteilung“). Eigene Überlegung, nicht im Papier.
- **Inventarabhängigkeit (A31):** „different sense inventories lead to different algorithmic biases“ (S. 85) ist ein knapper, früher Beleg für die These, dass das Ergebnis vom Inventar abhängt. Für das MHDBDB-Begriffssystem hieße das: Ein Inventar aus Begriffsnamen ohne Glossen kann Verfahren begünstigen, die mit kurzen Etiketten umgehen können (Deutung, nicht im Papier).
- **Granularität:** Vorschlag 4 zieht die Grenze über Lexikalisierung in anderen Sprachen und behandelt Unterscheidungen ohne solche als reguläre Polysemie (S. 84). Das MHDBDB-Inventar ist onomasiologisch, nicht übersetzungsbasiert; das Kriterium ist nicht übertragbar, aber als Gegenmodell für die Diskussion der Granularität brauchbar.

## Grenzen und Einwände

- Positionspapier ohne Daten; alle Aussagen über Annotationsgeschwindigkeit und Übereinstimmung sind Annahmen.
- Kreuzentropie verlangt kalibrierte Wahrscheinlichkeiten; die Autoren räumen ein, dass nicht alle Systeme solche liefern (S. 81).
- Die Distanzmatrix in Tab. 4 ist ein konstruiertes Beispiel; wie Distanzen zu bestimmen und zu prüfen sind, bleibt offen.
- Der Evaluationsrahmen (Vorschlag 3) setzt große Mittel voraus („hoped that US and international sources will see fit to fund such a data annotation effort“, S. 82).
- OCR-Textebene fehlerhaft; Zitate am Seitenbild prüfen.
- Englisch und Gegenwartssprachen; Übertragung auf Mittelhochdeutsch nicht berührt.

## Weiterführend

- Resnik & Yarowsky 1999, Distinguishing systems and distinguishing senses: new evaluation methods for WSD, *Natural Language Engineering* 5(2), S. 113 bis 133 (nicht in diesem Papier, sondern bei Henrich 2015 zusammen zitiert): die ausgearbeitete Fassung; für die Frage der Teilwertung bei mehreren Gold-Senses nachschlagen.
- Melamed & Resnik 2000, Tagger evaluation given hierarchical tag sets, *Computers and the Humanities* 34(1–2), S. 79 bis 84 (bei Henrich 2015 zitiert, nicht hier): Auswertung mit hierarchischen Tagsets.
- Gale, Church & Yarowsky 1992, One sense per discourse (S. 80, 86): liegt als Zusammenfassung vor.
- Wilks & Stevenson 1996, The grammar of sense (S. 79, 85): POS-Tagging leistet viel Disambiguierung auf Homographenebene.
- Miller & Charles 1991, Contextual correlates of semantic similarity (S. 82): psycholinguistische Ähnlichkeitsdaten für Distanzmatrizen.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
