# Navigli 2012: A Quick Tour of Word Sense Disambiguation, Induction and Related Approaches

**Datei:** `pdf/Navigli-2012-Quick-Tour-WSD.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, PDF vollständig gelesen (15 Seiten, Textebene; Abb. 1 am Seitenbild geprüft); DOI über Crossref bestätigt. Priorität 3 (Hintergrund), daher knapp.

**Seitenzählung:** gedruckt S. 115 bis 129 = PDF-Seite 1 bis 15; PDF-Seite = gedruckte Seite − 114. Zitiert wird die gedruckte Seite, die PDF-Seite steht in Klammern.

**Verhältnis zu Navigli 2009:** Der Beitrag ist eine Kurzfassung mit Ausblick; für die ausführliche Darstellung verweist er selbst auf den Survey (S. 116, S. 124). Was dort schon steht (Aufgabendefinition, MFS, ITA als Obergrenze, Senseval-Zahlen, Bottleneck), ist in [Navigli-2009-WSD-Survey.md](Navigli-2009-WSD-Survey.md) zusammengefasst und wird hier nicht wiederholt. Neu gegenüber 2009 sind vor allem die Zahlen für grobkörniges All-Words (82 bis 83 %), der Befund zu Relationsdichte und Leistung (Abb. 1), die Gegenüberstellung wissensbasiert gegen überwacht nach 2009 und die Abschnitte zu WSI, Lexical Substitution und Vektorraummodellen.

## Bibliografie

- **Vollständig:** Navigli, Roberto, 2012. A Quick Tour of Word Sense Disambiguation, Induction and Related Approaches. In: Mária Bieliková, Gerhard Friedrich, Georg Gottlob, Stefan Katzenbeisser & György Turán (Hg.), *SOFSEM 2012: Theory and Practice of Computer Science*. Berlin, Heidelberg: Springer (Lecture Notes in Computer Science 7147), S. 115 bis 129.
- **DOI/URL:** https://doi.org/10.1007/978-3-642-27660-6_10 (am 2026-10-29 aufgelöst auf link.springer.com; Crossref bestätigt Autor, Titel, Reihe, S. 115 bis 129, 2012; Herausgeber:innen über den Crossref-Eintrag des Bandes 10.1007/978-3-642-27660-6). Fußzeile S. 115: „M. Bieliková et al. (Eds.): SOFSEM 2012, LNCS 7147, pp. 115–129, 2012“. ✔
- **Art:** Konferenzbeitrag (eingeladener Überblick; ob begutachtet, sagt das PDF nicht)
- **Sprache:** Englisch

## Worum es geht

Ein kurzer Einstieg in WSD und Word Sense Induction (WSI) mit dem Anspruch, die zum Zeitpunkt „heißesten“ Themen zu nennen (S. 115). Behandelt werden Sense-Repräsentation und Granularität, die drei Hauptansätze (überwacht, wissensbasiert, unüberwacht), Leistungsstand, Wissen als Engpass, Mehrsprachigkeit, Domänen-WSD (S. 116 bis 121), dann WSI mit ihren Evaluationsproblemen (S. 121 bis 122), Lexical Substitution (S. 123) und distributionelle Vektorraummodelle (S. 123 bis 124). Die These des Schlusses: Semantische Textanalyse verbessert erste Anwendungen, ihr Nutzen in realen Anwendungen ist aber noch nicht allgemein gezeigt (S. 124).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| WSD ordnet Wörtern im Kontext eine Bedeutung aus einem vordefinierten Inventar zu; WSI entdeckt Senses aus Text. | S. 115 (PDF 1), Abstract | eigene Definition |
| Ein Sense-Inventar ist im Kern eine Liste der Senses eines Wortes, wie sie Wörterbücher bieten; Inventare müssen laufend gepflegt werden und erfassen meist nur lexikografische Bedeutungen, kaum Eigennamen. | S. 116 (PDF 2), Abschn. 1 | eigene Darstellung |
| Homonyme sind völlig verschiedene Wörter, die gleich geschrieben werden; Polysemie sind feinere Unterscheidungen desselben Wortes, die sich auf jeder Granularitätsstufe ziehen lassen. | S. 116 bis 117 (PDF 2 bis 3), Abschn. 2.1 | eigene Darstellung |
| Gegen die Feinkörnigkeit von WordNet: OntoNotes legt Senses manuell neu zusammen, bis Annotator:innen 90 % Übereinstimmung erreichen; ein automatischer Weg clustert WordNet-Senses über eine Abbildung auf das Oxford Dictionary of English. | S. 117 (PDF 3), Abschn. 2.1 | referiert (Hovy et al. 2006; Navigli 2006; Navigli et al. 2007) |
| Offene Frage: welche Sense-Repräsentation und welches Inventar am besten ist, und für welche Anwendung; vorgeschlagen sind u. a. Wikipedia, Wiktionary, DANTE. | S. 117 (PDF 3), Abschn. 2.1 | eigene Frage mit Literatur |
| Drei Hauptansätze: überwacht (Klassifikator pro Zielwort aus annotierten Beispielen), wissensbasiert (Wörterbücher, Thesauri, semantische Graphen), unüberwacht (WSI). Welcher allgemein am besten ist, ist offen. | S. 117 bis 118 (PDF 3 bis 4), Abschn. 2.2 | eigene Darstellung |
| Wissensbasierte Systeme können überwachte schlagen, wenn genug Wissen vorhanden ist oder innerhalb einer Domäne, bei breiterer Abdeckung. | S. 118 (PDF 4), Abschn. 2.2 | referiert (Ponzetto & Navigli 2010; Baldwin et al. 2010; Agirre et al. 2009) |
| 2004 lag der Stand im All-Words-Setting bei etwa 65 %; die Sense-Repräsentation galt als Haupthindernis. Inzwischen 82 bis 83 % im All-Words-Setting, wenn die Sense-Unterscheidungen gröber sind. | S. 118 (PDF 4), Abschn. 2.3 | referiert (Snyder & Palmer 2004; Chan et al. 2007; Ponzetto & Navigli 2010) |
| Alternative zur Vergröberung: graduelle Sense-Zuweisungen eines Systems mit graduellen menschlichen Urteilen korrelieren. | S. 118 (PDF 4), Abschn. 2.3 | referiert (Erk & McCarthy 2009) |
| „Accuracy“ steht im Beitrag je nach Aufgabe für Recall oder F1. | S. 118 (PDF 4), Fn. 1 | eigene Festlegung |
| Mehr Wissen, bessere Leistung: Überwachte WSD gewinnt deutlich mit Hunderten Trainingsbeispielen pro Zielwort; ein einfaches Grad-basiertes wissensbasiertes Verfahren erreicht bis zu 90 %, wenn pro Sense mehr als 100 semantische Relationen verfügbar sind. | S. 118 bis 119 (PDF 4 bis 5), Abschn. 2.4, Abb. 1 | referiert (Martinez 2004; Navigli & Lapata 2010) |
| Knowledge Acquisition Bottleneck: bei einem Beleg pro Minute Dutzende, wenn nicht Hunderte Personenjahre für genug Trainingsdaten, und das für jede Sprache neu. Auswege: zweisprachige Korpora, automatische Sense-Annotation, Wikipedia. | S. 119 (PDF 5), Abschn. 2.4 | referiert (Edmonds 2000; Zhong & Ng 2009; Diab 2004; Brody & Lapata 2008; Ponzetto & Navigli 2009, 2010) |
| WSD-Forschung ist überwiegend englisch, weil dort die Ressourcen liegen; Cross-lingual WSD gewinnt das Inventar aus Übersetzungen eines Parallelkorpus. | S. 119 bis 120 (PDF 5 bis 6), Abschn. 2.5 | eigene Darstellung mit Literatur |
| Domänen-WSD arbeitet oft typbasiert (ein Sense pro Wort) statt tokenbasiert (jeder Kontext einzeln); domänengetriebene Verfahren sind unter den unüberwachten die besten, liegen aber unter überwachten. | S. 120 (PDF 6), Abschn. 2.6 | referiert (McCarthy et al. 2007; Koeling et al. 2005; Strapparava et al. 2004) |
| WSI-Evaluation ist schwer, weil es keine einzelne Gold-Clusterung gibt, auf die sich Menschen einigen; drei Wege: unüberwacht gegen Gold-Annotation, überwacht über eine Abbildung auf Gold-Senses, in einer Anwendung. | S. 122 (PDF 8), Abschn. 3.2 | eigene Darstellung mit Literatur |
| Lexical Substitution braucht kein vordefiniertes Inventar, ist aber gerade deshalb schwer zu evaluieren und zu vergleichen. | S. 123 (PDF 9), Abschn. 4 | eigene Darstellung (McCarthy & Navigli 2009) |
| Für Vektorraummodelle bleiben Skalierbarkeit, Anwendbarkeit und die Evaluation außerhalb einer Anwendung offen. | S. 123 bis 124 (PDF 9 bis 10), Abschn. 5 | eigene Wertung |

## Daten, Methode, Zahlen

Überblick ohne eigene Datenerhebung. Alle Zahlen sind referiert:

- All-Words 2004 etwa 65 %, grobkörnig 82 bis 83 % (S. 118 (PDF 4)).
- OntoNotes: Revision der Sense-Partition bis 90 % Übereinstimmung (S. 117 (PDF 3)).
- Abb. 1 (S. 119 (PDF 5), aus Navigli & Lapata 2010, am Seitenbild geprüft): F1 in Prozent gegen die Zahl der Kanten am richtigen Sense (0 bis 240), Kurven für WordNet und EnWordNet; EnWordNet ist WordNet mit etwa 60.000 zusätzlichen Relatedness-Kanten; über 100 Relationen pro Sense bis zu 90 % (Text S. 119). Am Bild abgelesen: Die WordNet-Kurve erreicht ihr Maximum knapp über 70 % bei etwa 60 Kanten und endet bei etwa 130 Kanten tiefer; nur die EnWordNet-Kurve steigt gegen 90 %.
- Bottleneck: Dutzende bis Hunderte Personenjahre bei einem Beleg pro Minute (S. 119 (PDF 5)). Navigli 2009 nennt dafür konkreter 27 Personenjahre (S. 10:56, siehe dortige Zusammenfassung); beide berufen sich auf Edmonds 2000.

## Wörtliche Stellen

> „A sense inventory is an artifact we are all very familiar with. In fact, it is merely a list of senses of a given word“ (S. 116 (PDF 2))

> „polysemous senses can be created at any level of granularity, thus leading to possibly very fine-grained sense distinctions.“ (S. 117 (PDF 3))

> „what sense representation, and inventory, is best (and for which application [63])?“ (S. 117 (PDF 3))

> „The question of which approach is best in general, and in which application, is still very much open.“ (S. 118 (PDF 4))

> „there is no single gold-standard clustering on which human annotators can agree.“ (S. 122 (PDF 8), zu WSI)

## Bezug zur Dissertation

Die Bezüge aus Navigli 2009 (MFS, ITA als Obergrenze, Granularität, typ- gegen tokenbasiert) gelten; hier nur, was der Beitrag hinzufügt.

- **Protokoll 2 und 5 (Inventar = Begriffsgruppen, keine Definitionen):** Navigli setzt Inventar und Wörterbuchliste gleich (S. 116) und stellt die Inventarwahl als offene Frage (S. 117). Das MHDBDB-Inventar ist keine solche Liste, sondern eine Menge von Begriffszeigern pro Sense (`knowledge/data.md`, Abschnitt 1). Der Beitrag liefert damit keine Vorlage, aber einen Beleg, dass die Inventarfrage auch in der englischsprachigen WSD als ungelöst gilt; das Protokoll beantwortet sie für Mittelhochdeutsch durch Vorgabe (MHDBDB-Begriffssystem).
- **Protokoll 9.1, Punkt 7 (zwei Ebenen des Begriffssystems):** Der Sprung von etwa 65 % auf 82 bis 83 % bei gröberen Senses (S. 118) und die beiden Vergröberungswege (manuell bis 90 % Übereinstimmung, automatisch über ein hierarchisches Wörterbuch, S. 117) stützen die Zwei-Ebenen-Auswertung. Der automatische Weg ähnelt dem, was das Protokoll vorhat (Abbildung auf Oberbegriffe, `knowledge/data.md` B11), mit dem Unterschied, dass das Protokoll die grobe Ebene vorab festlegt.
- **Protokoll 9.1 (graduelle Urteile):** Die Korrelation graduierter Urteile (Erk & McCarthy 2009, S. 118) ist der Weg, den das Protokoll mit `MEHRERE` und Sicherheitsangabe nicht geht; er wäre die Alternative, falls `MEHRERE` häufig wird.
- **Begriffe im Text (Protokoll 9.2):** Fn. 1 (S. 118) verwendet „accuracy“ für Recall oder F1 je nach Aufgabe. Das bestätigt den Hinweis in der Zusammenfassung von Navigli 2009, im Text einmal festzulegen, was „Genauigkeit“ meint.
- **Motivation (Knowledge Acquisition Bottleneck):** Die Auswege von 2012 (Parallelkorpora, automatische Annotation, Wikipedia, S. 119) setzen Ressourcen voraus, die es für Mittelhochdeutsch kaum gibt. An genau dieser Stelle steht Julias Notiz (unten). Für die Einleitung: Der Beitrag beschreibt den Stand unmittelbar vor neuronalen Sprachmodellen und eignet sich als Beleg dafür, welche Engpässe ein LLM-Ansatz umgehen soll; ob er es tut, misst die Dissertation.
- **`knowledge/data.md` B1 (Typlisten) und Abschnitt 4, Punkt 1:** Die Unterscheidung typ- gegen tokenbasiert (S. 120) steht hier knapper als in Navigli 2009 (S. 10:15); zitierfähig ist beides.

## Grenzen und Einwände

- Kurzüberblick ohne eigene Daten; alle Zahlen referiert, ohne Angabe, welches Maß (Recall oder F1, Fn. 1) hinter welcher steht. Vor einem Zitat der 82 bis 83 % die Primärquellen (Chan et al. 2007; Ponzetto & Navigli 2010) prüfen.
- Englisch und WordNet als Bezugspunkt; zu historischen Sprachen und onomasiologischen Inventaren nichts.
- Stand 2011/2012, vor neuronalen Sprachmodellen; Aussagen über „hot topics“ sind historisch.
- Abb. 1 gilt für ein einfaches Grad-Verfahren auf einer englischen Ressource; übertragbar ist höchstens die qualitative Aussage, dass dichtere Relationen helfen.

## Julias Markierungen im PDF

70 Hervorhebungen, 1 Notiz, 2 Randzeichen (`md/Navigli-2012-Quick-Tour-WSD.markierungen.md`), über S. 115 bis 124 verteilt. Aufgenommen: Definition WSD und WSI (S. 115); Inventar als Wörterbuchliste, nur lexikografische Bedeutungen, ohne Eigennamen (S. 116); Homonymie und Polysemie, Granularität auf jeder Stufe (S. 116 bis 117); Frage nach dem besten Inventar (S. 117); drei Ansätze und offene Frage nach dem besten (S. 117 bis 118, beide Randzeichen stehen neben dieser Aufzählung); wissensbasiert schlägt überwacht bei genug Wissen (S. 118); 65 % im All-Words-Setting, Sense-Repräsentation als Hindernis, graduierte Urteile (S. 118); Wissen als Schlüsselfaktor, Hunderte Trainingsbeispiele, Relatedness-Kanten, 90 % bei über 100 Relationen (S. 118 bis 119); Bottleneck und Auswege (S. 119); Englisch-Lastigkeit und Cross-lingual WSD (S. 119 bis 120); typ- gegen tokenbasiert, Domänen-Labels, domänengetriebene Verfahren (S. 120); WSI ohne vordefinierte Senses, WSI-Evaluation ohne einigungsfähiges Gold (S. 121 bis 122); Verweis auf den Survey (S. 124).

Nur knapp oder nicht aufgenommen: Domänentext und Anwendungen wie Question Answering (S. 120), die vier WSI-Verfahrensnamen (S. 121 bis 122), Coverage von WSI (S. 122), Vektorraummodelle und Exemplar-Modelle (S. 123 bis 124), Lexikografie als Anwendung (S. 124, Flati & Navigli 2012). Sie betreffen WSI und distributionelle Semantik, nicht die WSD-Evaluation mit festem Inventar; die Exemplar-Modelle (Erk & Padó 2010, S. 123) stehen unter „Weiterführend“.

## Julias Notizen im PDF

- S. 119 (PDF 5), neben den Auswegen aus dem Knowledge Acquisition Bottleneck (zweisprachige Korpora, automatische Sense-Annotation, Wikipedia): „punkt wo sprachmodelle alles ändern“.

Die Notiz ist in die `md`-Fassung nicht eingemischt.

## Weiterführend

- Navigli 2009, Survey (S. 116, S. 124); eigene Zusammenfassung vorhanden.
- Hovy et al. 2006, OntoNotes: The 90% Solution (S. 117, Lit. 27); in `goldstandard/LITERATUR-IAA.md` schon geführt.
- Navigli, Litkowski & Hargraves 2007, SemEval-2007 Task 07, Coarse-grained English All-Words (S. 117, Lit. 57): Vorbild für eine vorab definierte grobe Ebene.
- Erk & McCarthy 2009, Graded word sense assignment (S. 118, Lit. 16): Alternative zu Einzellabels.
- Palmer, Babko-Malaya & Dang 2004, Different sense granularities for different applications (S. 117, Lit. 63).
- Navigli & Lapata 2010, Graph connectivity for unsupervised WSD (S. 118 bis 119, Lit. 56): Quelle von Abb. 1.
- McCarthy et al. 2007, Unsupervised acquisition of predominant word senses (S. 120, Lit. 43): vorherrschender Sense ohne annotierte Daten, als mögliche Baseline ohne Silber.
- Erk & Padó 2010, Exemplar-based models (S. 123, Lit. 18).
