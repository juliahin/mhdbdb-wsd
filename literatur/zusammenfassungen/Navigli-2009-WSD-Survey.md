# Navigli 2009: Word Sense Disambiguation. A Survey

**Datei:** `pdf/Navigli-2009-WSD-Survey.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->

**Stand:** 2026-10-28, PDF vollständig gelesen (69 Seiten, Textebene und Seitenbilder; Tabellen VII bis IX am Seitenbild geprüft); DOI über Crossref bestätigt.

**Seitenzählung:** Der Artikel ist Artikel 10 des Hefts, gedruckt als 10:1 bis 10:69. Gedruckte Seite 10:n = PDF-Seite n; zitiert wird „S. 10:n".

**Gewichtung:** Die Zusammenfassung ist nicht gleichmäßig. Schwerpunkt sind Aufgabendefinition, Sinninventar und Granularität, MFS-Baseline, Evaluationsmaße, IAA als Obergrenze, Knowledge-Acquisition-Bottleneck und Lexical Sample gegenüber All-Words. Die Methodenkapitel 3 bis 6 (S. 10:15 bis 10:41) sind nur knapp erfasst.

## Bibliografie

- **Vollständig:** Navigli, Roberto, 2009. Word Sense Disambiguation: A Survey. *ACM Computing Surveys* 41(2), Article 10, 69 Seiten (10:1 bis 10:69).
- **DOI/URL:** 10.1145/1459352.1459355. `doi.org` leitet auf `dl.acm.org/doi/10.1145/1459352.1459355` weiter (ACM-Seite selbst gab 403); Crossref bestätigt Autor, Titel, Band 41, Heft 2, Seiten 1 bis 69, Druck Februar 2009, online 2009-02-23.
- **Art:** begutachteter Zeitschriftenartikel (Überblick). Eingereicht Dezember 2006, überarbeitet Januar 2008, angenommen März 2008 (S. 10:69); „four anonymous reviewers" (S. 10:58).
- **Sprache:** Englisch

## Worum es geht

Ein Überblick über Word Sense Disambiguation bis 2008: Aufgabe und Formalisierung, Wissensquellen
(WordNet, SemCor), überwachte, unüberwachte und wissensbasierte Verfahren, Evaluationsmaße und
Baselines, die Senseval/Semeval-Kampagnen 1998 bis 2007, Anwendungen und offene Probleme. Die
zentrale These des Schlusses: Wie schwer WSD ist, hängt an der Granularität des Sinninventars
(S. 10:56). Feinkörnige Inventare im Stil von WordNet begrenzen Systeme auf etwa 65 bis 70 %
(All-Words) bzw. etwa 73 % (Lexical Sample), grobkörnige erlauben 80 bis 90 % (S. 10:50 bis
10:51). Die Most-Frequent-Sense-Baseline ist im All-Words-Setting kaum zu schlagen (S. 10:50).
Der Text stammt aus der Zeit vor neuronalen Sprachmodellen und LLMs.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| WSD ordnet jedem Wort eine Teilmenge seiner Inventar-Senses zu, A(i) ⊆ Senses_D(w_i); mehrere Senses sind formal erlaubt, üblich ist genau einer. | S. 10:3 bis 10:4, Abschn. 2 | eigene Formalisierung |
| WSD ist Klassifikation, aber anders als POS-Tagging wechselt die Klassenmenge mit jedem Wort: „n distinct classification tasks, where n is the size of the lexicon". | S. 10:4, Abschn. 2 | eigene Darstellung |
| Lexical Sample: wenige Zielwörter, meist eines pro Satz, typisch überwacht. All-Words: alle offenen Wortklassen eines Textes, braucht breite Abdeckung, überwachte Systeme leiden an Datenknappheit. | S. 10:4, Abschn. 2 | eigene Darstellung |
| Ein Sinninventar zerlegt den Bedeutungsbereich eines Wortes; wo ein Sense endet, ist strittig, Wörterbücher entscheiden verschieden; die nötige Granularität hängt von der Anwendung ab. | S. 10:4 bis 10:5, Abschn. 2.1 | eigene Darstellung |
| Für objektive Evaluation müssen Senses aufgezählt sein (enumerativer Ansatz); dagegen steht der generative Ansatz (Pustejovsky) und Kilgarriffs Einwand, Bedeutung lasse sich nicht in eine feste Sense-Liste fassen. | S. 10:5 bis 10:6, Abschn. 2.1 | referiert (Pustejovsky 1991, 1995; Kilgarriff 1997, 2006) |
| Monosem, polysem, homonym definiert relativ zum Inventar, mit Wortart als Teil des Schlüssels (w_p). | S. 10:6, Abschn. 2.1 | eigene Definition |
| Knowledge Acquisition Bottleneck: Wissensressourcen manuell zu erstellen ist teuer und muss bei neuer Domäne, Sprache oder neuem Inventar wiederholt werden. | S. 10:2; S. 10:55, Abschn. 10.2 | Begriff referiert (Gale et al. 1992b; Ng 1997) |
| Für ein hochgenaues, breit abdeckendes überwachtes System bräuchte es etwa 3,2 Mio. sense-annotierte Wörter, rund 27 Personenjahre bei einem Wort pro Minute. | S. 10:56, Abschn. 11 | referiert (Ng 1997; Edmonds 2000) |
| Token-basierte gegenüber typ-basierter Disambiguierung: Typ-basiert heißt, einem Wort im ganzen Text denselben (vorherrschenden) Sense zu geben. | S. 10:15, Abschn. 2.4 | eigene Darstellung |
| Die Sense-Verteilung eines Wortes ist in Texten stark schief. | S. 10:38, Abschn. 6.1 | referiert (Kilgarriff & Rosenzweig 2000) |
| Maße: Coverage, Precision, Recall, F1; Recall ≤ Precision, bei voller Coverage gleich; in der WSD-Literatur heißt Recall auch „accuracy". | S. 10:41 bis 10:42, Abschn. 7.1 | eigene Darstellung |
| Fehler lassen sich nach Distanz zwischen gewähltem und richtigem Sense gewichten, wird aber selten genutzt. | S. 10:42, Abschn. 7.1 | referiert (Resnik & Yarowsky 1999) |
| Random-Baseline: 1/|Senses| pro Wort, gemittelt. First-Sense- bzw. MFS-Baseline: der häufigste Sense nach einem annotierten Referenzkorpus (bei WordNet SemCor, „or, analogously, in another reference sense-tagged data set"), unabhängig vom Kontext. | S. 10:42 bis 10:43, Abschn. 7.2 | eigene Darstellung |
| MFS als Untergrenze; „often hard to beat". | S. 10:43, Abschn. 7.3 | referiert (Gale et al. 1992a) mit eigener Wertung |
| Obergrenze ist die Inter-Annotator-Übereinstimmung (ITA): grobkörnig etwa 90 %, feinkörnig (WordNet-Stil) 67 bis 80 %. | S. 10:43, Abschn. 7.3 | referiert (Gale et al. 1992a; Navigli et al. 2007; Chklovski & Mihalcea 2003; Snyder & Palmer 2004; Palmer et al. 2007) |
| Wenn ein System die ITA übertrifft, ist unklar, was das heißt; möglicherweise sind Annotationen oder Inventarunterscheidungen strittig. | S. 10:44, Abschn. 7.3 | referiert (Gale et al. 1992a) mit eigener Folgerung |
| Im All-Words-Setting schlagen nur wenige Systeme die MFS-Baseline; im Lexical Sample ist das anders, weil dort mehr Trainingsdaten vorliegen und die Aufgabe die reale Sense-Verteilung weniger abbildet. | S. 10:50 bis 10:51, Abschn. 8.5 | eigene Auswertung der Kampagnen |
| Abstand bester System zu MFS: Lexical Sample +21 / +16,6 / +17,7 Punkte (Senseval-1/2/3); feinkörniges All-Words +12 / +3 / +7,7 (Senseval-2/3, Semeval-2007). | S. 10:50, Abschn. 8.5 | eigene Auswertung |
| Mit WordNet fiel die Genauigkeit im Lexical Sample von 78 auf 64 % (Senseval-1 zu -2). | S. 10:50, Abschn. 8.5 | eigene Auswertung |
| Wörterbuchinventare, besonders WordNet, sind für die meisten Anwendungen zu feinkörnig; die Obergrenze feinkörniger Systeme liegt bei etwa 70 %. | S. 10:54, Abschn. 10.1 | referiert (u. a. Ide & Wilks 2006; Edmonds & Kilgarriff 2002) |
| OntoNotes bildete grobe Senses, indem es WordNet-Senses so lange zusammenlegte, bis 90 % ITA erreicht waren. | S. 10:54, Abschn. 10.1 | referiert (Hovy et al. 2006) |
| Ein enumeratives Lexikon führt unvermeidlich zu fehlenden Senses (neuer Gebrauch, Fachkontext, Auslassung). | S. 10:54 bis 10:55, Abschn. 10.1 | eigene Darstellung |
| Homonyme lassen sich zu etwa 95 % disambiguieren; mit allgemeiner Polysemie wird es viel schwerer, und die Granularität bestimmt Systemleistung und Übereinstimmung der Annotator:innen. | S. 10:56, Abschn. 11 | referiert (Yarowsky 1995; Stevenson & Wilks 2001) mit eigener Folgerung |
| In All-Words-Systemen dienen First-Sense- oder wissensbasierte Rückfallstrategien, wenn Trainingsbeispiele fehlen; fast alle Systeme greifen darauf zurück. | S. 10:57, Abschn. 11 | eigene Darstellung |
| Manche Sätze tragen zu wenig Bedeutung, um selbst für Menschen feinkörnig disambiguiert zu werden, und mehr Kontext hilft nicht unbedingt; fast 8 % des Senseval-3-All-Words-Testsets sind Tokens mit Lemma *be*. Vorschlag: „disambiguate less, disambiguate better". | S. 10:57, Abschn. 11 | eigene Wertung |
| Wissensbasierte Verfahren liegen meist unter überwachten, decken aber mehr ab; Lesk erreichte 50 bis 70 %; Selektionspräferenzen schneiden schlechter ab als Lesk oder MFS. | S. 10:30 bis 10:33, Abschn. 5 | referiert |
| Nur ein kleiner Teil der Suchanfragewörter wird nicht im häufigsten Sense gebraucht; WSD muss deshalb gerade bei seltenen Senses präzise sein. | S. 10:51, Abschn. 9.1 | referiert (Krovetz & Croft 1992; Sanderson 2000) |
| Domänenorientierte Verfahren (vorherrschender Sense pro Domäne) verschieben den Blick zu einer typ-basierten Sicht; SSI war auf einem Domänentext am besten, der die meisten überwachten Systeme benachteiligte. | S. 10:38 bis 10:40; S. 10:49; S. 10:56 | referiert (McCarthy et al. 2004, 2007) und eigene Ergebnisse (SSI, Navigli & Velardi 2005) |

## Daten, Methode, Zahlen

Methode: Literaturüberblick, keine eigene Datenerhebung. Die Zahlen stammen aus den Kampagnen und
sind am Seitenbild geprüft.

| Kampagne, Aufgabe | Inventar | Umfang | MFS | bestes System | Seite |
|---|---|---|---|---|---|
| Senseval-1 (1998), Lexical Sample Englisch | HECTOR | 8.400 Instanzen, 35 Wörter | 57 % | 74 bis 78 % (JHU 78,1 % nach Neueinreichung) | S. 10:45 |
| Senseval-2 (2001), Lexical Sample | WordNet 1.7 | über 4.300 Instanzen | 47,6 % | 64,2 % (JHU) | S. 10:45 bis 10:46, Tab. VII |
| Senseval-2, All-Words | WordNet 1.7 | 2.473 Wörter | 57,0 % | 69,0 % (SMUaw) | S. 10:45 bis 10:46, Tab. VII |
| Senseval-3 (2004), Lexical Sample | WordNet 1.7.1 (Nomen, Adjektive), WordSmyth (Verben) | 3.944 Instanzen | 55,2 % | 72,9 % (htsa3); beste 14 Systeme 70,9 bis 72,9 % | S. 10:46 bis 10:47, Tab. VIII |
| Senseval-3, All-Words | WordNet 1.7.1 | 2.037 Wörter | 60,9 oder 62,4 % (je nach Mehrwort-Behandlung) | 65,1 % (GAMBL-AW) | S. 10:47, Tab. VIII |
| Semeval-2007, grobkörniges Lexical Sample | grobe Senses (OntoNotes-basiert, S. 10:54) | 4.851 Instanzen, 100 Wörter | 78,0 % | 88,7 % (NUS-ML) | S. 10:48 bis 10:49, Tab. IX |
| Semeval-2007, feinkörniges All-Words | Semeval-2007 verwendete laut S. 10:50 WordNet 2.1 und grobe Inventare; für diese Aufgabe nicht eigens genannt | 465 Wörter | 51,4 % | 59,1 % | S. 10:49 |
| Semeval-2007, grobkörniges All-Words | WordNet-Cluster über ODE (S. 10:54) | 2.269 Wörter | 78,89 % | 82,50 % im Wettbewerb; SSI außer Konkurrenz 83,21 % | S. 10:49, Tab. IX |

Weitere Zahlen:

- SemCor: 352 Texte, davon 186 mit allen offenen Wortklassen und 166 nur mit Verben sense-annotiert, rund 234.000 Annotationen, ursprünglich WordNet 1.5 (S. 10:11).
- WordNet 3.0: etwa 155.000 Wörter in über 117.000 Synsets (S. 10:8).
- ITA: grobkörnig etwa 90 %, feinkörnig 67 bis 80 % (S. 10:43).
- Ähnlichkeitsmaße auf 1.754 Nomen-Instanzen von Senseval-2: zwischen 29,5 % (Res) und 39,1 % (Lesk) (S. 10:36, Tab. VI).

## Wörtliche Stellen

> „WSD actually comprises n distinct classification tasks, where n is the size of the lexicon." (S. 10:4)

> „In WSD, a typical upper bound is the interannotator agreement or intertagger agreement (ITA)" (S. 10:43)

> „This baseline poses serious difficulties to WSD systems as it is often hard to beat" (S. 10:43, zur First-Sense-Baseline)

> „it is unclear how to interpret a performance which beats the interannotator agreement" (S. 10:44)

> „the first sense baseline is a real challenge for all-words WSD systems: only few systems are able to exceed it" (S. 10:50)

> „The hardness of WSD strictly depends on the granularity of the sense distinctions taken into account." (S. 10:56)

## Bezug zur Dissertation

- **Protokoll 1 und 9.2 (LLM gegen MFS):** Navigli liefert die Standardbegründung, warum MFS die richtige Vergleichsgröße ist: Untergrenze, die im All-Words-Setting kaum zu schlagen ist (S. 10:43, S. 10:50), weil die Sense-Verteilung schief ist (S. 10:38). Die MFS-Definition „häufigster Sense in einem annotierten Referenzkorpus" (S. 10:43) deckt die Konstruktion des Protokolls (MFS aus Silber, Leave-out) direkt ab.
- **Protokoll 4.1 bis 4.3 (Stichprobe):** Die Stichprobe zieht 1 Token pro Paar aus Lemma und Wortart über viele Lemmata, ist also der Form nach All-Words-ähnlich, nicht Lexical Sample mit vielen Belegen pro Lemma (`LITERATUR-STICHPROBE.md`, Kilgarriff & Rosenzweig). Navigli begründet, warum MFS im Lexical Sample schwächer und im All-Words-Setting stärker ist (S. 10:50). Für die Einordnung des Ergebnisses ist das wichtig: Die Gleichverteilung über Polysemiezellen weicht von der realen Tokenverteilung ab, wie Navigli es für das Lexical Sample beschreibt.
- **Protokoll 3 (D1/D0) und 9.2 (MFS aus D1 auf D0):** Navigli referiert, dass der vorherrschende Sense von der Domäne abhängt (S. 10:38 bis 10:40, S. 10:56), und dass ein Domänentext überwachte Systeme benachteiligte (S. 10:49). Das stützt den Vorbehalt des Protokolls, dass die aus D1 gelernte MFS auf D0 verschoben angewandt wird.
- **Protokoll 9.2 (LLM gegen Menschen, IAA als Obergrenze):** Die Rolle der ITA als Obergrenze (S. 10:43) und die offene Frage, was ein Wert darüber bedeutet (S. 10:44), passen zu „Die menschliche IAA ist die Obergrenze". Die Werte (fein 67 bis 80 %, grob etwa 90 %) ergänzen die Spannen in `LITERATUR-IAA.md` (dort fein 67 bis 72 %, grob 90 bis 94 %); Navigli nennt für fein eine weitere Spanne bis 80 %.
- **Protokoll 9.1, Punkt 3 (Zufallsmodell pro Lemma):** Der Satz, WSD seien n getrennte Klassifikationsaufgaben mit wechselnder Klassenmenge (S. 10:4), ist ein zitierfähiger Beleg für die Begründung, die erwartete Übereinstimmung pro Lemma statt gepoolt zu rechnen.
- **Protokoll 9.1, Punkt 7 (zwei Ebenen des Begriffssystems):** Granularität als stärkster Faktor (S. 10:56), Leistungssprung von fein zu grob (S. 10:50 bis 10:51) und die distanzgewichtete Bewertung nach Resnik & Yarowsky (S. 10:42) stützen die Zwei-Ebenen-Auswertung. Die OntoNotes-Methode, Senses bis 90 % ITA zusammenzulegen (S. 10:54), ist genau das nachträgliche Zusammenlegen, das das Protokoll mit Artstein & Poesio vermeiden will.
- **Protokoll 6 (`MEHRERE`, `KEINE_PASST`, `KONTEXT_UNZUREICHEND`):** Die Formalisierung lässt Mengen von Senses zu (S. 10:3 bis 10:4, Fußnote 11 S. 10:41); fehlende Senses sind bei enumerativen Inventaren unvermeidlich (S. 10:54 bis 10:55); manche Stellen sind auch für Menschen nicht feinkörnig entscheidbar (S. 10:57). Alle drei Ausweichlabels haben damit einen Anknüpfungspunkt in der Literatur.
- **Protokoll 9.2 (Abstinenz des LLM):** Coverage, Precision und Recall (S. 10:41 bis 10:42) sind das Begriffspaar, um zu berichten, wie oft das LLM abstiniert und wie gut es antwortet, wenn es antwortet. Das Protokoll rechnet Genauigkeit; ob „accuracy" dort Recall im Sinne Naviglis meint, sollte im Text einmal festgelegt werden.
- **`knowledge/data.md` B1 und Abschnitt 4, Punkt 1 (Typ-Sense als zweite Baseline):** Naviglis Unterscheidung token-basiert gegenüber typ-basiert (S. 10:15) ist der Begriff für das, was die Typlisten an `<sense>` leisten. Eine „Typ-Sense"-Baseline wäre eine typ-basierte Disambiguierung in seinem Sinn.
- **Knowledge Acquisition Bottleneck (S. 10:2, S. 10:55 bis 10:56):** Motivation, warum für Mittelhochdeutsch kein überwachtes WSD trainiert, sondern ein LLM gegen MFS geprüft wird.
- **Protokoll 3 (Ausschluss von Präpositionen und Adverbien):** Naviglis Bemerkung zu Tokens wie *be* im Senseval-3-Testset (S. 10:57) ist ein Beleg dafür, dass sehr häufige, bedeutungsarme Wörter WSD-Ergebnisse verzerren; die Begründung im Protokoll (funktional-grammatische Senses) ist eine andere, aber verwandt.

## Grenzen und Einwände

- Stand 2008 (angenommen März 2008, S. 10:69): keine neuronalen Sprachmodelle, keine LLMs, keine späteren Benchmarks (für diese vgl. die in `goldstandard/LITERATUR-STICHPROBE.md` geführten Arbeiten, etwa Raganato et al. 2017). Aussagen über „state of the art" sind historisch.
- Alle Zahlen beziehen sich auf Englisch und auf Wörterbuchinventare (HECTOR, WordNet, OntoNotes-Gruppen). Für ein onomasiologisches Inventar wie das MHDBDB-Begriffssystem, in dem ein Sense eine Menge von Begriffszeigern ist (`knowledge/data.md` Abschnitt 1), gibt es keine Aussage; ob die WordNet-Werte für ITA und MFS übertragbar sind, bleibt offen.
- Die ITA-Spannen sind referiert, nicht nachgerechnet; welches Maß (Rohübereinstimmung oder κ) hinter jeder Zahl steht, sagt Navigli nicht. Vor einem Zitat in der Arbeit die Primärquellen (Gale et al. 1992a, Palmer et al. 2007, Snyder & Palmer 2004) prüfen.
- MFS ist bei Navigli aus einem großen, unabhängigen Referenzkorpus (SemCor) geschätzt. Im Protokoll stammt sie aus Silber der MHDBDB mit unbekannter Herkunft; die Stärke der Baseline hängt dann an der Qualität dieses Silbers.
- Die Kampagnendifferenzen (+3 bis +21 Punkte) sind über verschiedene Inventare und Testsets hinweg kaum vergleichbar; Navigli sagt das selbst (S. 10:50).
- Kleine Inkonsistenz im Text: Senseval-2 All-Words, Platz 2 heißt im Fließtext „Ave-Antwerp", in Tabelle VII „CNTS-Antwerp" (S. 10:45 bis 10:46). Ohne Folgen für die Zahlen.

## Weiterführend

- Gale, Church & Yarowsky 1992a, Estimating upper and lower bounds (zitiert S. 10:43 bis 10:44; Literatur S. 10:61): Primärquelle für MFS als Untergrenze und ITA als Obergrenze.
- Palmer, Dang & Fellbaum 2007, Making fine-grained and coarse-grained sense distinctions (zitiert S. 10:43, S. 10:54; Literatur S. 10:66): Primärquelle für ITA fein gegen grob.
- Snyder & Palmer 2004, The English all-words task (zitiert S. 10:43, S. 10:47; Literatur S. 10:68): Senseval-3-ITA und MFS.
- Chklovski & Mihalcea 2003, Exploiting agreement and disagreement of human annotators (zitiert S. 10:43, S. 10:54; Literatur S. 10:60).
- Resnik & Yarowsky 1999, Distinguishing systems and distinguishing senses (zitiert S. 10:40, S. 10:42; Literatur S. 10:67): distanzgewichtete Bewertung, relevant für die Zwei-Ebenen-Auswertung.
- McCarthy, Koeling, Weeds & Carroll 2004 und 2007, vorherrschender Sense aus unannotiertem Text (zitiert S. 10:38; Literatur S. 10:64): Alternative MFS-Schätzung ohne Silber.
- Ide & Wilks 2006, Making sense about sense (zitiert S. 10:6, S. 10:54; Literatur S. 10:63): Granularität auf Homonymebene.
- Kilgarriff 1997, I don't believe in word senses (zitiert S. 10:5, S. 10:54; Literatur S. 10:63).
- Navigli, Litkowski & Hargraves 2007 und Hovy et al. 2006 sind bereits in `goldstandard/LITERATUR-IAA.md` verzeichnet.
