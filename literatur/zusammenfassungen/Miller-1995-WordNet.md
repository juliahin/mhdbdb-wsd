# Miller 1995: WordNet. A Lexical Database for English

**Datei:** `pdf/Miller-1995-WordNet.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, PDF vollständig gelesen (3 Seiten, Textebene; Tab. 1 am Seitenbild geprüft); DOI über Crossref bestätigt. Priorität 3 (Hintergrund), daher knapp.

**Seitenzählung:** gedruckt S. 39 bis 41 = PDF-Seite 1 bis 3 (Kolumnentitel „COMMUNICATIONS OF THE ACM November 1995/Vol. 38, No. 11“ mit Seitenzahl); die Textebene trägt keine Seitenlabels. Zitiert wird die gedruckte Seite, die PDF-Seite steht in Klammern.

## Bibliografie

- **Vollständig:** Miller, George A., 1995. WordNet: A Lexical Database for English. *Communications of the ACM* 38(11), S. 39 bis 41.
- **DOI/URL:** https://doi.org/10.1145/219717.219748 (löst am 2026-10-29 auf dl.acm.org auf, Seite selbst 403). Crossref bestätigt Autor, Zeitschrift, Band 38, Heft 11, S. 39 bis 41, November 1995; Crossref führt als Titel nur „WordNet“, das PDF (S. 39) den vollen Titel. ✔
- **Art:** Zeitschriftenartikel (Kurzbeitrag in der Rubrik „AI: commonsense problems“, S. 39)
- **Sprache:** Englisch

## Worum es geht

Ein dreiseitiger Überblick über WordNet: Wörterbücher sind für menschliche Leser:innen gemacht, WordNet ist eine lexikalische Datenbank für den Gebrauch durch Programme (S. 39 (PDF 1)). Englische Nomen, Verben, Adjektive und Adverbien sind in Synonymmengen (Synsets) geordnet, die je ein „lexicalized concept“ darstellen und durch semantische Relationen verbunden sind (S. 39 bis 40 (PDF 1 bis 2)). Der letzte Abschnitt benennt Polysemie als Hindernis für Systeme mit natürlichsprachlicher Eingabe: WordNet listet die Alternativen, entscheidet aber nicht zwischen ihnen; wie man Kontexte für Senses repräsentiert, sei offen (S. 41 (PDF 3)).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Wortschatz als Menge von Paaren (Form f, Sense s); ein Wort mit mehr als einem Sense ist polysem, zwei Wörter mit mindestens einem gemeinsamen Sense sind synonym. | S. 39 (PDF 1), „Language Definitions“ | eigene Definition |
| Die semantischen Relationen, in die ein Wort eintritt, bestimmen seine Definition. | S. 39 (PDF 1) | eigene These (relationale Semantik) |
| Ein Sense wird durch die Menge der Synonyme dargestellt, die ihn haben (Synset); Synonymie ist die Grundrelation. | S. 40 (PDF 2) | eigene Darstellung |
| Relationen: Synonymie, Antonymie, Hyponymie/Hypernymie, Meronymie/Holonymie, Troponymie, Entailment; gewählt, weil sie im Englischen breit gelten und ohne linguistische Ausbildung verständlich sind. | S. 40 (PDF 2), Tab. 1 | eigene Darstellung |
| Für Definitionen allein aus Relationen sind zu wenige Relationen kodiert; deshalb haben die meisten Synsets nach lexikografischer Praxis eine Glosse. | S. 40 (PDF 2) | eigene Feststellung |
| Geschlossene Wortklassen (etwa 300 Präpositionen, Pronomen, Determinative) erhalten keine semantische Beschreibung. | S. 40 (PDF 2) | eigene Festlegung |
| WordNet listet die Alternativen, aus denen gewählt werden muss; Mittel, den passenden Sense im Kontext zu bestimmen, fehlen und sind ein Entwicklungsziel. | S. 41 (PDF 3), „Contextual Representations“ | eigene Feststellung |
| Menschen wählen den passenden Sense meist, ohne die Polysemie zu bemerken; wie sie das tun, ist nicht gut verstanden. | S. 41 (PDF 3) | eigene Darstellung, gestützt auf Charles 1988 |
| Kontext wird als Satz definiert; Sense-Identifikation heißt, Mengen von Satzkontexten zu unterscheiden. | S. 41 (PDF 3) | eigene Festlegung |
| Thematischer Kontext identifiziert Senses nur zu etwa 80 % richtig; Menschen nutzen mehr den lokalen Kontext unmittelbar um das Wort. | S. 41 (PDF 3) | referiert (Leacock, Towell & Voorhees 1993) |
| Eine semantische Konkordanz (Text plus Lexikon, jedes Inhaltswort mit seinem Sense verknüpft; Brown-Korpus mit WordNet) soll Sense-Identifikation empirisch prüfbar machen, ist aber noch zu klein. | S. 41 (PDF 3) | eigene Darstellung (Miller et al. 1993) |

## Daten, Methode, Zahlen

- Über 118.000 Wortformen, über 90.000 Senses, über 166.000 Paare (f, s) (S. 40 (PDF 2)).
- Etwa 17 % der Wörter polysem, etwa 40 % mit mindestens einem Synonym (S. 40 (PDF 2)).
- Über 116.000 Zeiger für semantische Relationen (S. 40 (PDF 2)).
- Tab. 1 (S. 40 (PDF 2), am Seitenbild geprüft): Relation, Wortart und Beispiele; Hyponymie und Meronymie nur Nomen, Troponymie und Entailment nur Verben, Antonymie vor allem Adjektive und Adverbien.
- Beispiel: *flight* hat acht Senses, im Bereich Flugreisen ist nur einer wahrscheinlich (S. 41 (PDF 3)).

## Wörtliche Stellen

> „English nouns, verbs, adjectives, and adverbs are organized into sets of synonyms, each representing a lexicalized concept.“ (S. 39 (PDF 1))

> „WordNet lists the alternatives from which choices must be made.“ (S. 41 (PDF 3))

> „How best to characterize the contexts associated with word senses remains an open question.“ (S. 41 (PDF 3))

## Bezug zur Dissertation

- **Protokoll 2 und 5 (Inventar, Begriffsgruppe als Bedeutung):** WordNet stellt einen Sense durch die Menge seiner Synonyme dar und nennt den Synset ein „lexicalized concept“ (S. 39 bis 40). Das MHDBDB-Inventar stellt einen Sense durch die Menge seiner Begriffszeiger dar (`knowledge/data.md`, Abschnitt 1). Beide definieren Bedeutung über eine Menge statt über eine Definition; der Unterschied ist die Richtung: WordNet geht von Wörtern zu einem Konzept, das MHDBDB-Begriffssystem ordnet Senses vorgegebenen Begriffen zu (onomasiologisch). Brauchbar für den Inventar-Abschnitt der Arbeit als Vergleichspunkt.
- **Protokoll 5 (keine LLM-Definitionen):** Miller sagt, dass Relationen allein für Definitionen nicht reichen und Glossen deshalb dazukommen (S. 40). Die MHDBDB-Senses haben fast keine Glossen (`knowledge/data.md` B13). Das ist ein Argument dafür, im Protokoll offen zu benennen, dass Annotator:innen und LLM nur Begriffsnamen und Pfad sehen, nicht eine Glosse wie bei WordNet-Annotation.
- **Protokoll 3 (Ausschluss von Präpositionen):** WordNet beschreibt geschlossene Wortklassen semantisch nicht (S. 40). Das ist eine weitere, wenn auch alte Stütze dafür, dass WSD-Vergleichsdatensätze, die auf WordNet beruhen, Präpositionen nicht enthalten, wie das Protokoll für seinen Ausschluss angibt.
- **Protokoll 6 (Kontextausschnitt, offener Punkt 4):** Kontext als Satz (S. 41) und der Hinweis, dass Menschen vor allem lokalen Kontext nutzen (S. 41, referiert), sind eine historische Vorlage für die Festlegung des Standardausschnitts. Für Verse ohne klare Satzgrenzen gilt die Satzdefinition nicht unmittelbar.

## Grenzen und Einwände

- Kurzer Überblick ohne Evaluation; die Zahlen beschreiben eine WordNet-Version von 1995, die nicht genannt wird.
- Die 80 % für thematischen Kontext sind referiert (Leacock et al. 1993) und betreffen ein Klassifikationsexperiment, keine menschliche Übereinstimmung.
- Englisch; über historische Sprachstufen oder begriffsorientierte Inventare nichts.
- Abweichende Seitenangabe zu Miller (Hg.) 1990 im Literaturverzeichnis: hier *International Journal of Lexicography* 3(4), S. 235 bis 312 (S. 41, Lit. 4); Navigli 2012 (Lit. 49) zitiert Miller, Beckwith, Fellbaum, Gross & Miller 1990, S. 235 bis 244. Wohl ein Heft mit mehreren Beiträgen gegenüber dem Einleitungsbeitrag; vor einem Zitat prüfen.

## Weiterführend

- Miller (Hg.) 1990, WordNet: An on-line lexical database, *International Journal of Lexicography* 3(4) (S. 39, Lit. 4).
- Miller & Charles 1991, Contextual correlates of semantic similarity (S. 41, Lit. 5): die Annahme, dass Kontext Bedeutung trägt, auf die sich auch Iacobacci et al. 2016 (S. 897) berufen.
- Miller, Leacock, Tengi & Bunker 1993, A semantic concordance (S. 41, Lit. 7): Ursprung von SemCor.
- Leacock, Towell & Voorhees 1993 (S. 41, Lit. 3): thematischer gegen lokalen Kontext.
- Fellbaum (Hg.) 1998, WordNet: An Electronic Lexical Database (im Aufsatz als angekündigtes Buch für 1996 erwähnt, S. 41); in `references.txt` als `fellbaum1998wordnet`.
