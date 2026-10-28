# Tittel, Gillis-Webber & Nannini 2020: Ontologie auf Basis des Begriffssystems von Hallig und Wartburg

**Datei:** `pdf/Tittel-etal-2020-Hallig-Wartburg-Ontologie.pdf` (nur lokal; 10 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, ganzes PDF gelesen (Abbildungen und Listings am Seitenbild), Venue in der ACL Anthology geprüft.

Seitenzählung: PDF-Seite n = gedruckte S. n.

## Bibliografie

- **Vollständig:** Tittel, Sabine; Gillis-Webber, Frances & Nannini, Alessandro A. (2020). Towards an Ontology Based on Hallig-Wartburg's *Begriffssystem* for Historical Linguistic Linked Data. In: Maxim Ionov, John P. McCrae, Christian Chiarcos, Thierry Declerck, Julia Bosque-Gil & Jorge Gracia (Hg.), *Proceedings of the 7th Workshop on Linked Data in Linguistics (LDL-2020)*, Marseille: European Language Resources Association, S. 1 bis 10.
- **DOI/URL:** https://aclanthology.org/2020.ldl-1.1/ (abgerufen: Anthology-ID 2020.ldl-1.1, Mai 2020, S. 1 bis 10, ISBN 979-10-95546-36-8, keine DOI). Kopfzeile S. 1: LDL-2020 bei LREC 2020, Marseille, 11. bis 16. Mai 2020, ELRA, CC BY-NC. ✔
- **Art:** Workshop-Beitrag (LREC-Workshop)
- **Sprache:** Englisch

## Worum es geht

Die Arbeit überführt das Begriffssystem von Hallig und Wartburg (HW) in Linked Open Data: zuerst als RDF/SKOS-Modell mit SKOS-Thesaurus-Erweiterung und XKOS, dann als leichtgewichtige OWL-Ontologie (Abstract, S. 1). Ausgangspunkt ist eine XML-Digitalisierung der 524 Begriffe des ‚Plan' aus dem DAGél (S. 4). Anwendungsbeispiele kommen aus dem Altgaskognischen und Italienischen (S. 7). Die Diskussion benennt Grenzen von HW: zu grob, ungeeignet für Funktionswörter und modern gedacht („Historical Semantic Gap", S. 8).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Für eine onomasiologische Ordnung braucht es eine thesaurusartige Kategorisierung der Welt; HW ist das wohl bekannteste Beispiel in der Romanistik. | S. 2, Abschn. 2 | referiert/Einordnung |
| HW ist kein Thesaurus nach ISO 25964, weil es keine lexikalisierten Terme hat: ein außersprachliches Bezugssystem, die französischen Bezeichnungen sind nur Symbole. | S. 2, Abschn. 2.1 | eigene Analyse |
| Umfang: ca. 1675 Begriffe in neun Ebenen; der ‚Plan' (sechs Ebenen, 524 Begriffe, Notation A bis C mit römischen Ziffern usw.) und die ‚Application' mit ca. 1150 feineren, nicht durchnummerierten Begriffen. | S. 2, Abschn. 2.1 | eigene Analyse von HW |
| HW enthält hierarchische (generische und Teil-Ganzes) und assoziative Relationen; bei Fachdomänen wird bewusst assoziativ statt logisch eingeordnet (z. B. ‚construire' bei ‚La construction'). Begriffe können mehrfach vorkommen. | S. 2 bis 3, Abschn. 2.1 | eigene Analyse |
| Inkonsistenzen: ‚Généralités' 27-mal, ‚etc.' als Begriff, falsche Hierarchisierungen (Phonetik neben Linguistik, Alchimie unter Metallen, Fabeltiere unter Tieren, Tabak unter Nahrung). | S. 3, Abschn. 2.1 | eigene Analyse |
| Die MHDBDB baut auf HW auf; Schmidt entwickelte die Kategorisierung an ‚Frauendienst' und ‚Lanzelet' weiter (Schmidt 1980, 1988, 1993). | S. 3, Abschn. 2.2 | referiert (Hinkelmanns 2019) |
| Das SKOS-Modell der MHDBDB (vom Projekt zur Verfügung gestellt) unterscheidet sich deutlich: keine HW-Kennungen, keine französischen Bezeichnungen, stattdessen deutsche und englische Bezeichnungen als `prefLabel` (also als lexikalische Terme); Relationen nur als generisches `skos:broader`, ohne `narrower`. | S. 6, Abschn. 3.1 und Anm. 13 | eigene Prüfung des MHDBDB-Modells |
| Die Relationen sind in HW nicht explizit; eine SKOS-Darstellung erfordert eine manuelle Bewertung jeder Relation. | S. 5, Abschn. 3.1 | eigene Analyse |
| Umwandlungsregeln (11 Punkte), u. a. Bezeichnungen als `scopeNote` und `altLabel` ohne `prefLabel`, Notation erhalten, ‚etc.' gestrichen, Homonyme durch Nummer und deutsche `editorialNote` getrennt. | S. 5, Abschn. 3.1 | eigenes Verfahren |
| Leichtgewichtige OWL-Full-Ontologie: SKOS-Begriffe als Klassen, generische Relationen als `rdfs:subClassOf`; kein Schließen möglich, dafür wäre OWL DL nötig. | S. 6 bis 7, Abschn. 3.2; S. 8 | eigenes Verfahren |
| Anwendung: Sense-Definitionen aus DAGél und LEI über `ontolex:isConceptOf` an HW-Klassen gebunden; HW als sprachunabhängiger „cross-mapping hub". | S. 7, Abschn. 4 | eigene Demonstration |
| Grenzen von HW: Umfang und Granularität reichen nicht für den ganzen Wortschatz; ungeeignet für „small words" (Pronomen, Artikel); Fachgebiete wie Astronomie oder Biologie nur je ein Begriff. | S. 8, Abschn. 5 | eigene Einschätzung |
| „Historical Semantic Gap": HW bildet die moderne Welt ab; Dinge, Wörter oder Bedeutungen sind ausgestorben oder haben sich verschoben (Beispiele *jambe*, *veine*). Vorschlag: Historisierung von HW mit Klasse `HistCat` und Relation `hasModernCounterpart`. | S. 8, Abschn. 5 | eigene Analyse und Vorschlag |

## Daten, Methode, Zahlen

- HW: ca. 1675 Begriffe, 9 Ebenen; ‚Plan' 524 Begriffe in 6 Ebenen (HW S. 101 bis 112); ‚Application' ca. 1150 Begriffe (HW S. 113 bis 229) (S. 2). Digitalisiert wurden 2014 nur die 524 Plan-Begriffe der 2. Auflage 1963 (S. 4).
- ‚Généralités' 27-mal (S. 3); nur vier Begriffe mit dem Merkmal ‚ancien' (S. 8).
- Suche in DEAFél-Definitionen nach ‚pâtisserie': 46 Treffer; Suche nach HW-Begriff B I k 1 cc 2: 21 Lexeme, ungenauer (S. 7, Anm. 15).
- Veröffentlicht: das Identifikationsschema unter https://lod.academy/hw-onto/ns/hw# (S. 8).
- Figuren: Abb. 1 Plan-Auszug (HW 103), Abb. 2 Application-Auszug (HW 141), Abb. 3 Hierarchie-Schema (S. 2, 4); Listings 1 bis 7 (S. 4 bis 8).

## Wörtliche Stellen

> „The MHDBDB has created a SKOS model of the onomasiological framework (extending HW) that structures the data. However, its design differs significantly from the result of our attempt: The model excludes both the original HW identifiers and the French concept denominations. Instead, concept denominations have been translated to German and English, and they are treated as lexical terms, expressed through the SKOS property ‘prefLabel’." (S. 6)

> „HW is little appropriate for the mapping of the so-called small words (e.g., pronouns, articles)." (S. 8)

> „We refer to this circumstance as the Historical Semantic Gap." (S. 8)

## Bezug zur Dissertation

- **PROTOKOLL §5 (Begriffsnamen als Karten) und `knowledge/data.md` Abschnitt 1:** S. 6 beschreibt von außen genau die Struktur, die das Projekt nutzt: deutsche (und englische) Bezeichnungen als Terme, nur `broader`. Für die Annotationsoberfläche heißt das: Die Begriffsnamen sind von Menschen übersetzte Etiketten eines außersprachlichen Systems, keine Definitionen. Ein Argument, die Begriffsnamen mit Pfad zu zeigen, wie §5 vorsieht.
- **`knowledge/data.md` B11:** Die Autor:innen sahen 2020 im MHDBDB-Modell nur generische `broader`-Relationen (S. 6); B11 findet heute Polyhierarchie mit 43 Begriffen mit mehreren Oberbegriffen. Kein Widerspruch (mehrere `broader` sind möglich), aber die Art der Relation (generisch, Teil-Ganzes, assoziativ) ist im MHDBDB-Modell nicht unterschieden. Für die grobe Ebene (§9.1 Punkt 7) zählt deshalb der Zahlencode, nicht die Relationsart.
- **PROTOKOLL §1 Nebenfrage, §6 `KEINE_PASST`:** Die Grenzen von HW (Granularität, Funktionswörter, Historical Semantic Gap, S. 8) sind Hypothesen dafür, wo das Inventar versagen kann. Die Ausweichlabels mit angekreuzten Begriffen können diese Hypothesen für das Mittelhochdeutsche prüfen.
- **PROTOKOLL §3 (keine Präpositionen und Adverbien):** S. 8 stützt indirekt den Ausschluss der Funktionswörter: Ein HW-artiges Begriffssystem fasst „small words" schlecht. Die MHDBDB hat laut Zeppezauer-Wachauer 2022, S. 172, Funktionswörter eigens ergänzt.
- **Lücke „keine IAA für onomasiologisches Inventar" (`LITERATUR-IAA.md`):** Auch dieser Beitrag berichtet keine Annotationsübereinstimmung; die Lücke bleibt.

## Grenzen und Einwände

- Modellierungsbeitrag ohne Annotationsstudie; die Anwendung zeigt je ein Beispiel aus DAGél und LEI.
- Nur der ‚Plan' (524 Begriffe) war digitalisiert; die feinere ‚Application' fehlt im Modell (S. 4).
- Das MHDBDB-Modell wird nur in einem Absatz beschrieben (S. 6), Stand 2020.
- Kleine Inkonsistenz: HW-Erstauflage 1952 (S. 1, 2), aber „the book published in 1953" (S. 6).

## Weiterführend

- Hallig & von Wartburg 1963, *Begriffssystem als Grundlage für die Lexikographie*, Akademie-Verlag, Berlin (Erstauflage 1952) (S. 9).
- Schmidt 1980, 1988, 1993 zur Anwendung auf das Mittelhochdeutsche (S. 3, 10).
- Tittel & Chiarcos 2018, DEAF nach OntoLex, hier S. 58 bis 66 (S. 10); vgl. `BESCHAFFUNG.md` zur strittigen Venue.
- Kless et al. 2012a, 2012b, Thesaurus zu Ontologie (S. 10).
- Khan, Frontini & Boschetti 2014, lemon für semantischen Wandel (S. 10).
- Stolk 2019, Lemon-tree, `isSenseInConcept` (S. 6, Anm. 12; S. 10).
- Bizzoni et al. 2014, Ancient Greek WordNet (S. 8, 9).

## Julias Markierungen im PDF

21 Hervorhebungen, keine Notizen (`md/Tittel-etal-2020-Hallig-Wartburg-Ontologie.markierungen.md`). Aufgenommen: Ziel, HW nach LOD zu überführen, und die beiden Ansätze SKOS und OWL (S. 1); OntoLex als De-facto-Standard und wortformgebundene Suche als Problem historischer Forschung (S. 1, in „Worum es geht" und Bezug); HW-Erstveröffentlichung 1952 und 2. Auflage 1963 (S. 1); semasiologisch gegen onomasiologisch (S. 2); MHDBDB baut auf HW auf, Schmidt 1980, 1988, 1993 (S. 3). Nur knapp aufgenommen, weil romanistischer Hintergrund: FEW, DAO, DAG, LEI (S. 3).
