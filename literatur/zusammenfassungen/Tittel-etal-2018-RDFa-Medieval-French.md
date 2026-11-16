# Tittel, Bermúdez-Sabel & Chiarcos 2018: Text und Wörterbuch des mittelalterlichen Französisch mit RDFa verknüpfen

**Datei:** `pdf/Tittel-etal-2018-RDFa-Medieval-French.pdf` (nur lokal; 9 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen; Inhaltsverzeichnis und Kolumnentitel des Tagungsbands geprüft (siehe Bibliografie). Das lokale PDF ist byte-gleich mit dem PDF im Repositorium der Universität Lausanne (SHA-256 verglichen am 2026-11-13). Keine Markierungen.

**Seitenzählung:** Das lokale PDF trägt keine Seitenzahlen. Im Tagungsband steht der Beitrag laut Inhaltsverzeichnis auf S. 30 (nächster Beitrag S. 39), also S. 30 bis 38; das sind 9 Seiten wie im lokalen PDF. Daraus folgt PDF-Seite n = S. 29 + n. Ob die Seitenumbrüche gleich sind, ließ sich nicht prüfen, weil der Band an dieser Stelle einen anderen Text enthält (siehe unten). Unten steht deshalb „PDF-S. n“.

## Bibliografie

- **Vollständig:** Tittel, Sabine, Helena Bermúdez-Sabel & Christian Chiarcos (2018). Using RDFa to Link Text and Dictionary Data for Medieval French. In: John P. McCrae, Christian Chiarcos, Thierry Declerck, Jorge Gracia & Bettina Klimek (Hg.), *Proceedings of the LREC 2018 Workshop „6th Workshop on Linked Data in Linguistics: Towards Linguistic Data Science“ (LDL-2018)*, Miyazaki, 12. Mai 2018. Paris: ELRA, S. 30 bis 38. ISBN 979-10-95546-19-1.
- **Quellen der Angaben (abgerufen 2026-11-13):** Tagungsband auf Zenodo, DOI 10.5281/zenodo.2599900 (CC BY 4.0; Titelblatt: Hg., ISBN, 12. Mai 2018; Inhaltsverzeichnis S. viii: Beitrag ab S. 30; Kolumnentitel „Tittel et al.: Using RDFa …“ auf S. 30 bis 38). Einzel-PDF: Repositorium der Universität Lausanne, https://iris.unil.ch/handle/iris/33793 (byte-gleich mit dem lokalen PDF; keine Lizenz angegeben).
- **Fehler im Tagungsband:** In der Zenodo-Fassung tragen S. 30 bis 38 zwar den Kolumnentitel dieses Beitrags, der Text darunter ist aber noch einmal der vorangehende Beitrag (Abgaz et al., S. 21 bis 29). Der Wortlaut dieses Beitrags ist im Band also nicht enthalten; Seitenangaben lassen sich nur über Inhaltsverzeichnis und Kolumnentitel belegen.
- **Abweichende Angabe:** Der Datensatz in Lausanne nennt als Ort „Proceedings of the Eleventh International Conference on Language Resources and Evaluation (LREC 2018)“ und S. 7 bis 12; das passt weder zum Inhaltsverzeichnis des LDL-Bands noch zum Umfang von 9 Seiten und wird nicht übernommen.
- **Nicht verwechseln** mit Tittel & Chiarcos 2018 (GLOBALEX, DEAF und OntoLex-Lemon), das dieser Beitrag als „accepted“ zitiert (PDF-S. 8 bis 9); `references.txt`: `tittel2018deaf`.
- **Art:** Workshop-Beitrag (LREC-Workshop)
- **Sprache:** Englisch

## Worum es geht

Die Autor:innen überführen eine gedruckte kritische Edition, den ersten Traktat (*Anathomie*) der mittelfranzösischen Übersetzung der *Grande Chirurgie* des Gui de Chauliac (Tittel 2004), aus ihren LaTeX-Quellen nach TEI und verknüpfen jedes annotierte Lexem per RDFa mit dem Eintrag im *Dictionnaire étymologique de l’ancien français* (DEAF) (PDF-S. 1 bis 4). Die LaTeX-Quelle enthält schon Lemmatisierung, Wortart und eine Bedeutungsangabe pro Beleg, nach dem Prinzip „ein Lexem plus genau einer seiner Bedeutungen“ (PDF-S. 2 bis 3). Aus TEI+RDFa entstehen eine HTML5-Edition, RDF-Tripel und SPARQL-Abfragen (PDF-S. 4 bis 6). Die Verknüpfung geschieht nur auf Wortebene und per exaktem Abgleich der Lemmata; die Verknüpfung auf Bedeutungsebene bleibt offen, weil die Bedeutungsdefinitionen von Edition und Wörterbuch im Wortlaut fast nie übereinstimmen (PDF-S. 8).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Editionen alt- und mittelfranzösischer Texte sind fast immer Einzelprodukte; der Wortschatz ist nicht mit einem umfassenden Wörterbuch verbunden, ein Glossar zeigt seine Stellung in der Sprachgeschichte nicht. | PDF-S. 1, Abschnitt 1 | Problemstellung |
| TEI-Zeigerstrukturen (`xr`, `ref`, `ptr`, `lbl`) sind nicht LOD-tauglich, weil sie weder URIs als Ziel noch einen typisierten Relationsbegriff verlangen. | PDF-S. 6 bis 7, Abschnitt 8.2 | eigene Analyse |
| Die LaTeX-Auszeichnung der Edition umfasst Lemmatisierung, Wortartenbestimmung und „word-sense disambiguation (semantic tagging)“, annotiert auf Ebene der lexikalischen Einheit, „the entity of one lexeme plus exactly one of its senses“. | PDF-S. 2 bis 3, Abschnitt 3 | Beschreibung der eigenen Edition; Begriff nach Blank 1997 |
| Die Annotation ist partiell: „small words“ (einige Pronomen, Präpositionen, Artikel) bleiben unannotiert, und nur die ersten zehn Belege jeder lexikalischen Einheit sind annotiert. | PDF-S. 3, Anm. 5 | Beschreibung der eigenen Edition |
| Die Bedeutungsangabe steht als Definition (Paraphrase) beim Beleg; im Druck entsteht daraus ein Glossar mit ca. 1.350 Einträgen. | PDF-S. 2 bis 3 | Beschreibung der eigenen Edition |
| Kodierung: `seg` mit `@about`, `@property="rdfs:seeAlso"`, `@resource` (DEAF-Eintrag); darin `w` mit `@lemma`, `@type` (Wortart) und `gloss` mit `skos:definition`. Dafür werden `@about`, `@property`, `@resource` zur TEI-Attributklasse `att.global.linking` hinzugefügt. | PDF-S. 3 bis 4, Abschnitte 4 bis 5, Beispiele 2 und 3 | eigenes Ergebnis |
| RDFa im TEI wird beim Erzeugen von HTML einfach mitkopiert; Tripel lassen sich mit Standardwerkzeugen (pyRdfa) extrahieren und per SPARQL abfragen, z. B. alle Belege eines Wörterbuchlemmas. | PDF-S. 4 bis 6, Abschnitte 6 bis 7 | eigenes Ergebnis |
| SPARQL ist nicht für Philolog:innen selbst gedacht, sondern als Baustein von Portalen. | PDF-S. 6 | eigene Position |
| Gegenüber dem SAWS-Ansatz mit `relation` (in TEI an Prosopografie gebunden, „tag abuse“) habe RDFa semantische Klarheit und sofortige Verarbeitbarkeit. | PDF-S. 7, Abschnitt 8.2 | eigene Analyse |
| Verknüpfung nur per exakter Übereinstimmung von Editionslemma und DEAF-Stichwort; Lemmata wie *humeur* (DEAF *umor*) oder *distribuer* (DEAF *distribüer*) bleiben unverknüpft, weil das DEAF bei der Lemmatisierung der Edition noch nicht vorlag; Abhilfe: unscharfer Abgleich. | PDF-S. 8, Abschnitt 9.1 | eigenes Ergebnis |
| Verknüpfung nur auf Wortebene, obwohl Edition und Wörterbuch Senses unterscheiden (*humeur* mit zwei medizinischen Bedeutungen in der Edition; *plaie* in der Edition nur ‚Wunde‘, im DEAF mit zwei weiteren Bedeutungen). Für eine Verknüpfung auf Bedeutungsebene müssten die Definitionen „somehow“ übereinstimmen, „in most of the cases it does not“ (Beispiele *fermer*, *fievre*). | PDF-S. 8, Abschnitt 9.3 | eigenes Ergebnis, offenes Problem |
| Nächste Schritte: DMF als weiteres Wörterbuch, OntoLex-Lemon statt `rdfs:label`/`rdfs:seeAlso`. | PDF-S. 8, Abschnitte 9.2 und 9.4 | Ausblick |

## Daten, Methode, Zahlen

- **Text:** erster Traktat (*Anathomie*) der mittelfranzösischen Übersetzung der *Chirurgia magna* (Latein 1363), älteste französische Handschrift aus dem zweiten Drittel des 15. Jh. (PDF-S. 2). Edition Tittel 2004, Sigle GuiChaulMT (PDF-S. 2).
- **Inventar:** semasiologisch, Definitionen der Editorin pro lexikalischer Einheit; Verknüpfungsziel DEAF (Wörterbuchartikel mit Baum aus Haupt- und Unterbedeutungen, PDF-S. 8).
- **Annotation:** von der Editorin für die Edition 2004 erstellt; eine Person, keine Übereinstimmungsmessung; die Bedeutungsannotation selbst ist nicht Gegenstand des Papers.
- **Zahlen:** ca. 1.350 Glossareinträge (PDF-S. 2); nur erste zehn Belege je Einheit annotiert (PDF-S. 3). Wie viele Lemmata sich mit dem DEAF verknüpfen ließen, steht nicht im Text.
- **Verfahren:** LaTeX nach XML per Perl, nach TEI P5 per XSLT; HTML5+RDFa per XSLT; Turtle-Fassung veröffentlicht (PDF-S. 3 bis 5). Personennamen mit FOAF und VIAF-URIs, Header mit Dublin Core (PDF-S. 4).
- **Abbildungen** (PDF-S. 2, 5): Ausschnitte aus Druckedition, Glossar und Online-Edition; nicht inhaltlich ausgewertet.

## Wörtliche Stellen

> „The annotation is performed on the level of the lexical unit, i.e., the entity of one lexeme plus exactly one of its senses“ (PDF-S. 2 bis 3)

> „Also, only the first ten attestations of each lexical unit are annotated.“ (PDF-S. 3, Anm. 5)

> „Thus, the goal that we need to pursue next is to raise the linking from the word level to the sense level.“ (PDF-S. 8)

## Bezug zur Dissertation

- **Bedeutungen historischer Sprachen als Linked Data (Schwerpunkt des Auftrags):** Das Paper zeigt eine Edition, in der jeder annotierte Beleg eine Bedeutungsdefinition trägt, und eine Verknüpfung mit dem Wörterbuch nur auf Lemmaebene (PDF-S. 3 bis 4, 8). Die MHDBDB ist in diesem Punkt weiter: Der Sense am Token ist ein Zeiger auf einen Sense in `lexicon.xml`, der seinerseits auf Begriffe in `concepts.xml` zeigt (`knowledge/data.md`, Abschnitt 1). Die Verknüpfung geschieht über IDs, nicht über den Wortlaut von Definitionen; das Problem aus Abschnitt 9.3 (Definitionen von Edition und Wörterbuch stimmen nicht überein) stellt sich so nicht. Das ist ein Argument für die Darstellung des Inventars über Begriffsnamen (PROTOKOLL §5) statt über frei formulierte Definitionen.
- **Silber und Vollständigkeit (`knowledge/data.md`, B2, B9; PROTOKOLL §2 und §3):** Die Bedeutungsannotation der Edition ist partiell (keine Funktionswörter, nur die ersten zehn Belege je Einheit, PDF-S. 3). Das ist ein Vergleichsfall für eine menschliche, aber nicht vollständige Bestandsannotation; für die MHDBDB ist ähnliche Unvollständigkeit nicht dokumentiert, sondern gemessen (D0/D1, PROTOKOLL §3). Die Zehn-Belege-Regel heißt außerdem: Häufige Lexeme sind in der Annotation unterrepräsentiert, eine MFS daraus wäre verzerrt.
- **Typ- gegen Tokenbezug (`knowledge/data.md`, B1, und Abschnitt 3, Herkunft der Typlisten):** Hier hängt die Bedeutung am Token (Beleg im Text), die Wörterbuchverknüpfung am Lemma. Das ist die Form, die Hinkelmanns & Zeppezauer-Wachauer (2023, S. 180) für die MHDBDB künftig vorsehen (Stand-Off, Tokens); als Beleg für die Lesart in B1 taugt das Paper nicht, es handelt nicht von der MHDBDB.
- **`goldstandard/LITERATUR-IAA.md`, „Lücke“:** Wieder eine Bedeutungsannotation einer historischen Sprache von einer Person (der Editorin), ohne Übereinstimmungsmessung; das Paper problematisiert das nicht, weil es um die Verknüpfung geht.
- **Homonymie gegen Polysemie (`knowledge/data.md`, B15):** Der DEAF-Link `plaie1` (PDF-S. 8) zeigt, dass das DEAF Homonyme als nummerierte Einträge trennt; die Edition verknüpft per Stichwort. Für B15 nur ein Hinweis, wie ein anderes historisches Wörterbuch Homonyme führt, keine Aussage über die MHDBDB.

## Grenzen und Einwände

- Machbarkeitsstudie („proof of concept“, PDF-S. 8); keine Evaluation, keine Zahlen zur Abdeckung der Verknüpfung.
- Keine WSD im Sinn eines Verfahrens: Die Bedeutungen stammen aus der Edition, das Paper beschreibt nur ihre Kodierung und Verknüpfung.
- Die eigentliche Aufgabe, Belege mit Wörterbuchbedeutungen zu verknüpfen, bleibt offen (PDF-S. 8).
- Seitenangaben im Tagungsband nicht am Text prüfbar (Produktionsfehler des Bands, siehe Bibliografie).
- Übertragbarkeit auf ein onomasiologisches Inventar: gering, das Paper arbeitet mit semasiologischen Definitionen.

## Weiterführend

- Tittel & Chiarcos 2018, GLOBALEX, DEAF und OntoLex-Lemon (PDF-S. 8 bis 9): liegt vor, `zusammenfassungen/Tittel-Chiarcos-2018-DEAF-LOD.md`.
- Tittel 2004, *Die Anathomie in der Grande Chirurgie des Gui de Chauliac*, Niemeyer (PDF-S. 9): die Edition mit der Bedeutungsannotation.
- Blank 1997, *Einführung in die lexikalische Semantik*, Niemeyer, S. 6 (PDF-S. 3, 9): Begriff der lexikalischen Einheit.
- Habert, Nazarenko & Salem 1997, *Les linguistiques de corpus*, S. 74 (PDF-S. 3, 9): partielle semantische Disambiguierung.
- Möhren 2015, „L’art du glossaire d’édition“, in Trotter (Hg.), *Manuel de la philologie de l’édition*, S. 397 bis 437 (PDF-S. 2, 9): Glossarpraxis in Editionen.
- Martin 2015, DMF (PDF-S. 1, 8, 9).

## Julias Notizen im PDF

Keine. Das PDF hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
