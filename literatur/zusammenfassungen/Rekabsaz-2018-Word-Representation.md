# Rekabsaz 2018: Word Representation for Text Analysis and Search

**Datei:** `pdf/Rekabsaz-2018-Word-Representation.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29. Priorität 3 (Hintergrund), daher knapp und **kapitelweise**: gelesen wurden Kap. 1, 2.1 und 2.2 (Problemaufriss, Grundlagen), Kap. 4 (Ähnlichkeitsschwelle und Unsicherheit), Kap. 7 (CL-WSD), Anhang A (Testkollektion und Annotation) und Kap. 9; Kap. 5 und die Mehrdeutigkeitsstelle in Kap. 8 nur angelesen. Auswahl nach dem Inhaltsverzeichnis: Aufgenommen ist, was zu Wortbedeutung und Mehrdeutigkeit, Ähnlichkeitsschwellen, Evaluation, Annotation und Unsicherheit etwas sagt; die übrigen Kapitel sind reine Information-Retrieval- oder Finanzanwendungen. Tabellen 4.1, 5.2, 7.1 und A.1 an der Textebene geprüft, Abb. 4.3 und 7.1 am Seitenbild. Keine Markierungen von Julia im PDF (0 Anmerkungen, mit `markierungen.py` und PyMuPDF bestätigt).

**Seitenzählung:** Vorspann römisch (PDF 1 bis 12 = S. i bis xii), danach gedruckte Seite = PDF-Seite − 12 (PDF 13 = S. 1, PDF 140 = S. 128); die Textebene trägt die Seitenlabels. Zitiert wird die gedruckte Seite, die PDF-Seite steht in Klammern.

## Bibliografie

- **Vollständig:** Rekabsaz, Navid, 2018. *Word Representation for Text Analysis and Search: Document Retrieval, Sentiment Analysis, and Cross Lingual Word Sense Disambiguation*. Dissertation (Doktor der Technischen Wissenschaften), Fakultät für Informatik, TU Wien. Betreuer: Allan Hanbury; Zweitbetreuer: Mihai Lupu; Gutachter:innen: Carsten Eickhoff, Christina Lioma. 128 S. (Titelblatt S. i (PDF 1), datiert „Vienna, 4th April, 2018“).
- **DOI/URL:** https://doi.org/10.34726/hss.2018.62352 (am 2026-10-29 aufgelöst auf reposiTUm, Handle http://hdl.handle.net/20.500.12708/1909; DataCite: Autor, Titel, Jahr 2018, Verlag TU Wien, Betreuer Hanbury). reposiTUm nennt außerdem „Date of submission“ 2019-01, Organisationseinheit E194 (Institut für Information Systems Engineering), 128 Seiten, Rechte „In Copyright“, Open Access. Das lokale PDF ist **byte-gleich** mit dem reposiTUm-PDF (SHA-256 am 2026-10-29 verglichen). ✔
- **Art:** Abschlussarbeit (Dissertation); Abschn. 1.3 verweist zu jedem Beitrag auf eigene Veröffentlichungen (S. 8 bis 10 (PDF 20 bis 22))
- **Sprache:** Englisch (Kurzfassung auch deutsch)
- **Daten und Code:** Persische CL-WSD-Kollektion, Inventar und Gold unter https://github.com/navid-rekabsaz/wsd_persian (S. 76, S. 101 bis 102 (PDF 88, 113 bis 114)); nicht abgerufen.

## Worum es geht

Die Arbeit untersucht statische Wort-Embeddings (vor allem word2vec SkipGram) als Quelle für Ähnlichkeit zwischen Wörtern und setzt sie in Information Retrieval, Interpretierbarkeit, sprachübergreifender Disambiguierung (CL-WSD) und Sentimentanalyse ein (S. ix (PDF 9), S. 6 bis 8 (PDF 18 bis 20)). Für die Bedeutungsfrage einschlägig sind zwei Teile. Kap. 4 zeigt, dass Kosinus-Ähnlichkeiten zwischen gleich trainierten Modellen schwanken, und leitet daraus eine globale Schwelle ab, ab der ein Nachbar als „verwandt“ gilt (S. 41 bis 51 (PDF 53 bis 63)). Kap. 7 und Anhang A disambiguieren 20 mehrdeutige englische Nomen, indem sie die persische Übersetzung wählen, die dem übersetzten Kontext im Embedding-Raum am ähnlichsten ist, und bauen dafür eine eigene, von drei Muttersprachler:innen annotierte Testkollektion (S. 73 bis 79, S. 99 bis 102 (PDF 85 bis 91, 111 bis 114)). Das Verfahren schlägt die Baseline der häufigsten Übersetzung knapp, für zwei Wörter gar nicht (S. 77 bis 78 (PDF 89 bis 90)).

**Übrige Kapitel, nur genannt:** Kap. 3, „Extended and Generalized Translation Models“ (S. 23 bis 40): Embedding-Ähnlichkeiten in klassischen Retrieval-Modellen. Kap. 5, „Fusion of Semantic Models with Window and Document Contexts“ (S. 53 bis 61): verwandte Wörter zusätzlich nach gemeinsamem Dokumentkontext filtern, gegen Themenverschiebung. Kap. 6, „Interpretability in Word Embedding“ (S. 63 bis 71): explizite SkipGram-Vektoren, Gender-Bias in Wikipedia. Kap. 8, „Sentiment Analysis with Generalized Translation Models“ (S. 81 bis 94): Volatilitätsprognose aus 10-K-Berichten. Anhang B (S. 103 ff.): Wortlisten zu Gender und Berufen.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Wortrepräsentationen fassen alle Relationen (Synonymie, Antonymie, Hyper- und Hyponymie, Kohyponymie) in einen einzigen Begriff von „Verwandtschaft“ zusammen. | S. 5 (PDF 17), Abschn. 1.1.2 | eigene Darstellung, gestützt auf Kruszewski & Baroni 2015 |
| Die Modelle liefern für jedes Wortpaar eine Ähnlichkeit, auch wenn die Frage sinnlos ist („too ready to provide answers to meaningless questions“). | S. 6 (PDF 18), Abschn. 1.1.2 | referiert (Karlgren, Holst & Sahlgren 2008) |
| Häufige Wörter werden mit viel mehr anderen Wörtern ähnlich als seltene, weil sie mehr Kontext haben, nicht wegen ihrer Bedeutung. | S. 6 (PDF 18), Abschn. 1.1.2 | eigene Darstellung nach Wilks 2008 |
| (CL-)WSD braucht meist reiche Wissensressourcen oder annotierte bzw. parallele Daten; der Engpass beim Wissenserwerb trifft ressourcenarme Sprachen besonders. | S. 8 (PDF 20), Abschn. 1.2; S. 73 (PDF 85) | eigene Darstellung |
| Ähnlichkeitswerte sind keine festen Größen: Zwei Modelle, die sich nur im zufälligen Startpunkt unterscheiden, liefern verschiedene Werte; die Abweichung ist bei niedriger Ähnlichkeit und bei seltenen Wörtern größer. | S. 42 bis 43 (PDF 54 bis 55), Abschn. 4.1.1, Abb. 4.1 | eigenes Ergebnis |
| Die Standardabweichung über fünf gleich trainierte Modelle sinkt mit steigender Ähnlichkeit und mit steigender Dimension; ab 300 Dimensionen ändert sie sich kaum noch. | S. 44 bis 45 (PDF 56 bis 57), Abb. 4.2a | eigenes Ergebnis |
| Eine globale Schwelle lässt sich aus der erwarteten Zahl von Nachbarn ableiten, kalibriert an der mittleren Synonymzahl in WordNet (1,6); sie hängt von der Dimension ab (Tab. 4.1). | S. 45 bis 47 (PDF 57 bis 59), Abschn. 4.1.2 bis 4.1.3 | eigenes Ergebnis |
| Die so bestimmte Schwelle ist im Retrieval nie signifikant schlechter als die durch Parametersuche gefundene beste Schwelle; bei 100, 200 und 300 Dimensionen ist sie die beste. | S. 50 (PDF 62), Abschn. 4.3 | eigenes Ergebnis |
| Mit der Schwelle hat ein Wort im Mittel 1,5 Nachbarn (SD 3,0), fast die Hälfte gar keinen; das liegt nahe an WordNet (1,6 und 3,1). | S. 51 (PDF 63), Abschn. 4.3, Tab. 4.2 | eigenes Ergebnis |
| Ein Nächste-Nachbarn-Ansatz mit festem k ist theoretisch nicht begründbar. | S. 21 (PDF 33), Abschn. 2.2 | referiert (Gyllensten & Sahlgren 2015) |
| CL-WSD ohne Trainingsdaten: Für jede Übersetzungskandidatin wird die Embedding-Ähnlichkeit zum übersetzten Kontext berechnet (nach der Grundidee von Lesk: Wörter im selben Kontext teilen ein Thema) und mit der Übersetzungswahrscheinlichkeit des Wörterbuchs gewichtet. | S. 74 bis 76 (PDF 86 bis 88), Abschn. 7.1 | eigenes Verfahren |
| Beide Varianten schlagen die Baseline der häufigsten Übersetzung und das stärkste unüberwachte Vergleichssystem (CO-Graph), aber mit kleinem Abstand und ohne Signifikanztest. | S. 77 bis 78 (PDF 89 bis 90), Tab. 7.1 | eigenes Ergebnis |
| Für *mood* und *side* schlägt kein System die Baseline; dort teilt kein Nomen oder Verb des Kontexts ein Thema mit den Bedeutungen. Kontext als Wortmenge stößt hier an eine grundsätzliche Grenze. | S. 78 bis 79 (PDF 90 bis 91), Abschn. 7.3 und 7.4 | eigenes Ergebnis |
| Fehlende Vokalzeichen im Persischen erzeugen eine eigene Art graphischer Mehrdeutigkeit (gleiche Schreibung, verschiedene Aussprache). | S. 99 (PDF 111), Abschn. A.1 | referiert (Seraji et al. 2012) |
| Innerhalb einer Domäne sind die Bedeutungen eines Wortes eingeschränkter; Beispiel *fire* (Brand im Energiesektor, Entlassung sonst). | S. 93 (PDF 105), Abschn. 8.5.3 | eigene Beobachtung an Regressionsgewichten, nicht gemessen |

## Daten, Methode, Zahlen

- **Kap. 4, Modelle:** word2vec SkipGram auf dem Wikipedia-Dump von August 2015, Porter-Stemmer, Fenster 5, 25 Epochen, Mindesthäufigkeit 20, etwa 580.000 Wörter; pro Dimension (100, 200, 300, 400) fünf Modelle, die sich nur im Startpunkt unterscheiden (S. 43 bis 44 (PDF 55 bis 56)). „Beliebiges Wort“ heißt Mittel über 100 Wörter aus Schnabel et al. 2015, nach Frequenz und Wortart gestreut (S. 43 (PDF 55)). Für die Verteilung der Ähnlichkeitswerte wird eine Normalverteilung angenommen, „in the absence of additional information“ (S. 45 (PDF 57)).
- **Tab. 4.1, Schwellen (an der Textebene geprüft, S. 46 (PDF 58)):** untere, Haupt- und obere Grenze: 100 Dim. 0,802 / 0,818 / 0,829; 200 Dim. 0,737 / 0,756 / 0,767; 300 Dim. 0,692 / 0,708 / 0,726; 400 Dim. 0,655 / 0,675 / 0,693. Kalibrierung: 147.306 WordNet-Wörter, im Mittel 1,6 Synonyme, SD 3,1 (S. 46 (PDF 58)).
- **Evaluation Kap. 4:** TREC 6, 7, 8 Ad-hoc und TREC 2005 HARD, MAP und NDCG@20, zweiseitiger gepaarter t-Test, p < 0,05 (S. 47 (PDF 59)).
- **Kap. 5, Tab. 5.2 (an der Textebene geprüft, S. 55 (PDF 67)):** Über alle Kollektionen sind 81 % (Schwelle 0,60) bzw. 58 % (Schwelle 0,80) der hinzugefügten Wörter ohne nennenswerte Wirkung auf die Suche, 11 % bzw. 15 % schaden.
- **Kap. 7, Ressourcen:** persisches SkipGram-Modell auf 323.616 Artikeln der Zeitung Hamshahri; Wörterbuch über eine Google-Translate-Schnittstelle (abgerufen Juni 2015), deren Übersetzungswahrscheinlichkeit als P(t) dient; als Kontext nur Nomen und Verben, lemmatisiert (S. 76 bis 77 (PDF 88 bis 89)).
- **Kap. 7, Maß:** F-Maß der SemEval-2013-Aufgabe in zwei Einstellungen: *Best* (beliebig viele Vorschläge, Wert durch deren Zahl geteilt) und *Out-of-Five* (bis zu fünf Vorschläge, der beste zählt) (S. 76 (PDF 88)).
- **Tab. 7.1 (an der Textebene geprüft, S. 77 (PDF 89)):** OOF: RelAgg 0,502; RelGreedy 0,493; CO-Graph 0,441; STD-Baseline 0,418. Best: 0,188; 0,183; 0,174; 0,158. STD ist die häufigste Übersetzung (Best) bzw. die fünf häufigsten (OOF).
- **Anhang A, Testkollektion:** 20 Nomen der SemEval-2013-CL-WSD-Aufgabe, je 50 Belege (S. 101 (PDF 113)). Inventar: Übersetzungen aus drei persischen Wörterbüchern, ergänzt von einer Linguistin oder einem Linguisten, auch idiomatische (*melting pot*); 13 bis 42 Übersetzungen pro Wort, von derselben Person zu 2 bis 6 Bedeutungsclustern gruppiert (S. 101 (PDF 113)). Annotation: drei persische Muttersprachler:innen, in einer Web-Anwendung erst Cluster, dann bis zu drei Übersetzungen; passt keine, wird nichts gewählt (S. 102 (PDF 114)).
- **Tab. A.1 (an der Textebene geprüft, S. 102 (PDF 114)):** „% clusters consensus“ pro Wort 92 bis 100; eigene Rechnung aus der Tabelle: Mittel 97,4, fünf Wörter mit 100, 73 Cluster und 530 Übersetzungen insgesamt. Wie der Wert berechnet ist (paarweise, alle drei, zufallskorrigiert?), steht nicht da.

## Wörtliche Stellen

> „word representation methods are too ready to provide answers to meaningless questions“ (S. 6 (PDF 18), nach Karlgren et al. 2008)

> „These observations show that the similarity between terms is not an exact value but can be considered as an approximation whose variation is dependent on the dimensionality and similarity range.“ (S. 45 (PDF 57))

> „We however observe fundamental limitations of the methods based exclusively on context as bag of words when none of the context terms share any semantic topic with the ambiguous terms.“ (S. 79 (PDF 91))

## Bezug zur Dissertation

Für WSD-Grundlagen und den Abstand zwischen MFS und überwachten Systemen sind [Navigli-2012-Quick-Tour-WSD.md](Navigli-2012-Quick-Tour-WSD.md) und [Iacobacci-etal-2016-Embeddings-WSD.md](Iacobacci-etal-2016-Embeddings-WSD.md) die Bezugswerke; Rekabsaz ergänzt sie nur in drei Punkten.

- **Protokoll 9.2 (LLM gegen MFS, gepaarter Test):** Tab. 7.1 ist ein weiteres Beispiel dafür, dass ein wissensarmes Verfahren die Häufigkeitsbaseline nur knapp schlägt (Best 0,188 gegen 0,158) und bei einzelnen Wörtern gar nicht (S. 77 bis 78). Bei 20 Wörtern mit je 50 Belegen und ohne Signifikanztest bleibt offen, ob der Abstand trägt. Das stützt die Entscheidung des Protokolls für einen gepaarten Test auf denselben Gold-Items statt eines Vergleichs gegen einen festen Wert und die getrennte Auswertung auf Nicht-MFS-Items. Die Zahlen sind mit dem Protokoll nicht vergleichbar (Übersetzungen statt Senses, F-Maß mit Mehrfachvorschlägen).
- **Protokoll 9.1 (Übereinstimmung) und 6 (Ausweichlabels):** Anhang A ist ein Gegenbeispiel für die Berichterstattung. „% clusters consensus“ von 92 bis 100 bei 2 bis 6 Clustern pro Wort ist eine undefinierte Rohübereinstimmung ohne Zufallskorrektur (S. 102); bei so wenigen Kategorien ist die zufällige Übereinstimmung hoch. Das Inventar hat eine einzige Person gebaut und gruppiert, und wie aus drei Urteilen das Gold wird, steht nicht da (S. 101 bis 102). Für Protokoll 9.1, Punkte 3 und 4 (Zufallsmodell pro Lemma, Prävalenz) ist die Arbeit damit ein zitierbarer Fall dafür, warum α und die Randverteilungen berichtet werden. Das Annotationsschema (Cluster wählen, bis zu drei Übersetzungen, „nichts wählen“, wenn keine passt) ähnelt `SENSE`, `MEHRERE` und `KEINE_PASST`; ob „nichts“ ausgewertet wird, sagt die Arbeit nicht.
- **Protokoll 6 und offener Punkt 4 (Kontextausschnitt), Status `KONTEXT_UNZUREICHEND`:** Die Fälle *mood* und *side* (S. 78 bis 79) zeigen, dass ein Kontext ohne thematische Verbindung zu den Bedeutungen für ein ähnlichkeitsbasiertes Verfahren nichts entscheidet. Für ein LLM, das Syntax und Wortstellung mitliest, ist das kein direkter Beleg, wohl aber ein Grund, Items mit erweitertem Kontext und `KONTEXT_UNZUREICHEND` getrennt auszuwerten.
- **Protokoll 4.10 (LLM-Konfiguration, „Anzahl der Läufe pro Item“):** Kap. 4 misst, dass schon gleich trainierte Embedding-Modelle verschiedene Ähnlichkeiten liefern, am stärksten im unteren Bereich und bei seltenen Wörtern (S. 42 bis 45). Das ist eine Analogie, kein Befund über LLMs: Es spricht dafür, Lauf-zu-Lauf-Streuung zu messen statt einen Einzellauf zu berichten, gerade bei seltenen Lemmata.
- **Frequenz:** Die Beobachtung, dass häufige Wörter mehr Nachbarn bekommen (S. 6), passt zur Aufschlüsselung nach Frequenzband in Protokoll 9.1, Punkt 6; sie betrifft aber Embeddings, nicht das Inventar.

## Grenzen und Einwände

- **Kapitelauswahl:** Kap. 3, 5, 6 und 8 sind IR- und Finanzanwendungen und wurden nur so weit gelesen, wie sie zur Bedeutungsfrage beitragen (Tab. 5.2, die *fire*-Stelle S. 93). Abb. 4.4, 4.5 und 5.1 wurden nicht geprüft.
- **Statische Vektoren pro Wortform:** Die ganze Arbeit rechnet mit einem Vektor pro (gestemmtem) Wort; Mehrdeutigkeit wird nicht im Modell dargestellt, sondern nur in Kap. 7 über die Kontextähnlichkeit aufgelöst. Sense-Embeddings werden nur mit einem Satz zu Chen et al. 2014 erwähnt (S. 74 (PDF 86)). Stand 2018, vor kontextuellen Sprachmodellen.
- **„Verwandt“ heißt im Kap. 4 „nützlich fürs Retrieval“.** Die Schwelle wird an Suchergebnissen geprüft, nicht an Bedeutungsurteilen; die Kalibrierung an WordNet-Synonymzahlen ist eine Hypothese, deren Bestätigung (1,5 gegen 1,6) nur die Anzahl, nicht die Art der Nachbarn betrifft (S. 51). Normalverteilung der Ähnlichkeiten ist angenommen (S. 45).
- **CL-WSD ist nicht WSD gegen ein Inventar:** Ziel sind Übersetzungen, die Cluster dienen nur der Annotation. Die Kollektion ist klein (20 Nomen mit je 50 Belegen, also 1.000), nur Nomen, nur Englisch nach Persisch. Bei der Belegzahl ist von „cases (paragraphs)“ (S. 76) und „50 sentences“ (S. 102) die Rede. Keine Signifikanztests in Kap. 7.
- **Übertragbarkeit auf Mittelhochdeutsch:** Das Verfahren braucht ein Embedding-Modell der Zielsprache und ein Wörterbuch mit Übersetzungswahrscheinlichkeiten; für ein onomasiologisches Inventar wie das Begriffssystem der MHDBDB gibt es keine Entsprechung. Die graphische Mehrdeutigkeit des Persischen (S. 99) erinnert an Normalisierungseffekte im Mittelhochdeutschen, wird in der Arbeit aber nicht untersucht.
- In Abschn. 1.3 steht für den Gender-Bias-Beitrag die Sigle [RMLH17], deren Eintrag im Literaturverzeichnis „Toward incorporation of relevant documents in word2vec“ lautet (S. 10 (PDF 22); Verzeichnis S. 124 (PDF 136)); vermutlich eine vertauschte Sigle [am PDF zu prüfen].

## Weiterführend

- Rekabsaz, Sabetghadam, Lupu, Andersson & Hanbury 2016, Standard Test Collection for English-Persian Cross-Lingual Word Sense Disambiguation, LREC 2016 (S. 10 (PDF 22); Verzeichnis S. 124 (PDF 136)): die Kollektion aus Anhang A als Artikel.
- Rekabsaz, Lupu, Hanbury & Duque 2017, Addressing Cross-Lingual Word Sense Disambiguation on Low-Density Languages: Application to Persian, arXiv 1711.06196 (S. 10 (PDF 22)): Kap. 7 als Artikel.
- Rekabsaz, Lupu & Hanbury 2017, Exploration of a Threshold for Similarity Based on Uncertainty in Word Embedding, ECIR 2017, S. 396 bis 409 (S. 9 (PDF 21)): Kap. 4 als Artikel.
- Lefever & Hoste 2013, SemEval-2013 Task 10: Cross-Lingual Word Sense Disambiguation (S. 73, S. 76, S. 99, S. 101 (PDF 85, 88, 111, 113)): Vorbild für Inventarbau und Annotation über Übersetzungscluster.
- Karlgren, Holst & Sahlgren 2008, Filaments of Meaning in Word Space, ECIR (S. 6, S. 21 (PDF 18, 33)) und Kruszewski & Baroni 2015, So Similar and Yet Incompatible, NAACL (S. 5 (PDF 17)): zu den Grenzen von „Ähnlichkeit“ als Bedeutungsersatz. Die Arbeit schreibt im Fließtext „Kruzewski“, im Verzeichnis „Kruszewski“.
- Lesk 1986 (S. 74 (PDF 86), S. 100 (PDF 112)): Grundidee des Verfahrens; fehlt laut README weiterhin als PDF.
