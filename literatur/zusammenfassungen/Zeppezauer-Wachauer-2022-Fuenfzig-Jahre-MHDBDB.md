# Zeppezauer-Wachauer 2022: 50 Jahre Mittelhochdeutsche Begriffsdatenbank (MHDBDB)

**Datei:** `pdf/Zeppezauer-Wachauer-2022-Fuenfzig-Jahre-MHDBDB.pdf` (nur lokal; Separatum, 27 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, ganzes PDF gelesen, alle Abbildungen am Seitenbild angesehen, DOI aufgelöst.

Seitenzählung: PDF-Seite 1 ist das Deckblatt des Separatums (ohne Zahl), PDF-Seite n = gedruckte S. 159 + n (PDF 2 = S. 161 ohne gedruckte Zahl, PDF 3 = S. 162, PDF 27 = S. 186).

## Bibliografie

- **Vollständig:** Zeppezauer-Wachauer, Katharina (2022). 50 Jahre Mittelhochdeutsche Begriffsdatenbank (MHDBDB). Eine Jubiläums-Zeitreise zwischen Lochkarten, Pixel-Drachen, relationaler Datenbank und Graphdaten. In: Elisabeth Lienert, Joachim Hamm, Albrecht Hausmann & Gabriel Viehhauser (Hg.), *Digitale Mediävistik. Perspektiven der Digital Humanities für die Altgermanistik*. Oldenburg (Beiträge zur mediävistischen Erzählforschung, Themenheft 12), S. 161 bis 186.
- **DOI/URL:** https://doi.org/10.25619/BmE20223203 (aufgelöst auf https://ojs.uni-oldenburg.de/ojs01/bme/de/article/view/203; dort veröffentlicht am 28.11.2022, CC BY-NC-ND 4.0). Seiten 161 bis 186 laut Zitiervorschlag (PDF 1) und Paginierung ✔. Titel auf der Titelseite (PDF 2) „Graphdaten", im Zitiervorschlag „Graph Daten".
- **Art:** Beitrag in einem Online-Themenheft (BIS-Verlag Oldenburg); Begutachtung nicht angegeben
- **Sprache:** Deutsch

## Worum es geht

Ein Jubiläumsrückblick auf 50 Jahre MHDBDB in vier Etappen: Lochkarten seit 1972, Online-Gang 1995 und ORACLE-Datenbank 1998, Umzug nach Salzburg, Relaunch als Graphdatenbank mit TEI, RDF, SKOS und OntoLex (S. 162 bis 179). Der Beitrag beschreibt die Herkunft und Umgestaltung des Begriffssystems und den Stand der Disambiguierung (S. 172 bis 174) und zeigt Entwürfe des neuen Frontends (S. 176 bis 179). Er ist ausdrücklich auch ein persönlicher Augenzeugenbericht (S. 166, 180).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Kernelemente sind eine Suchmaschine und ein onomasiologisches Wörterbuch; die Tokens werden „auf diese Lemmata und die im Kontext gültige Bedeutung" sowie auf weitere Annotationsebenen bezogen. | Abstract S. 161; S. 162 (PDF 3) | Projektbeschreibung |
| Umfang: über 10,6 Mio. Tokens, fast 29.000 Wortartikel, 666 Werke; rund 28.000 User jährlich. | S. 162 (PDF 3) | Projektangabe |
| Anfänge 1972 mit Schmidts Dissertation zu Ulrich von Liechtenstein (Michigan); erste elektronische Grundlagen an der Bowling Green State University; Ein- und Ausgabe der Annotationen über Fortran-Lochkarten. | S. 162 bis 163 (PDF 3 bis 4) | Projektgeschichte |
| 1992 Zusammenschluss mit Pütz' Namensprojekt; 1995 integrierte Pütz über 100 Texte mit Namensannotationen; Mai 1995 online (mhdbdb.bgsu.edu); Herbst 1998 Übertragung auf ORACLE. | S. 163 bis 165 (PDF 4 bis 6) | Projektgeschichte |
| 2002 bis 2004 Verhandlungen, 2004 Installation in Salzburg mit 1,5 Stellen. | S. 165 (PDF 6) | Projektgeschichte |
| In den 2010ern u. a. „breite Wortfeld-Annotationen" und eine „Neukonzeption des Begriffssystems". | S. 166 (PDF 7) | Projektgeschichte |
| Auf Basis der damals 10 Mio. Tokens entstand in Stuttgart eine Trainingsdatei für einen TreeTagger des Mittelhochdeutschen (Ketschik et al. 2017). | S. 167 (PDF 8) | referiert |
| Seit 1998 werden alle Daten in ORACLE verwaltet; Relaunch-Vorbereitungen seit 2017, ohne zugesagte Mittel. | S. 168 (PDF 9) | Projektangabe |
| Alle 666 E-Texte sind nach TEI konvertiert und im Stand-off-Verfahren mit LOD verknüpft; Annotationen und Metadaten liegen als RDF vor und „werden direkt auf die Tokens der E-Texte bezogen"; Verknüpfung über das Web Annotation Vocabulary. | S. 170 (PDF 11) | Projektangabe |
| Wortartikel sind nach dem OntoLex-Lemon-Lexicography-Modul kodiert. | S. 171 (PDF 12) | Projektangabe |
| Das Begriffssystem folgt Roget, entwickelt Dornseiff weiter und lehnt sich „vor allem" an Hallig und Wartburg an; korpusbedingt um viele Kategorien erweitert, auch um Funktionswörter, Fremdsprachen und eine Frühform von NER. Das Design war hierarchisch, die Arbeit mit Zahlencodes wenig intuitiv. | S. 172 (PDF 13) | Projektbeschreibung |
| Das Begriffssystem wurde in einen polyhierarchischen SKOS-Thesaurus überführt; der „weitaus größte Teil" blieb erhalten und wurde um SKOS-Relationen, Sprach-Labels (de, en, fr, lat), altLabel, editorialNote und definition angereichert. | S. 172 bis 173 (PDF 13 bis 14) | Projektbeschreibung |
| Namen wurden aus dem Begriffssystem in ein eigenes SKOS-Onomastikon herausgelöst. Bislang wurde z. B. jedes Token ‚Walther' „über den Wortindex" mit dem Begriff ‚Literatur/Namen' verknüpft. | S. 173 (PDF 14) | Projektbeschreibung |
| „Inzwischen sind alle Texte voll lemmatisiert, die Lyrik und der größte Teil der Kurzprosa zusammen mit einigen Epen sogar disambiguiert." Diese Daten sollen für ein „lernfähiges Disambiguierungsmodul" dienen. | S. 174 (PDF 15) | Projektangabe |
| Der Datenstand dürfe „wieder als gut kuratiert, dokumentiert und nachhaltig konzipiert" gelten. | S. 174 (PDF 15) | Einschätzung der Autorin |

## Daten, Methode, Zahlen

- Zahlen: 10,6 Mio. Tokens, fast 29.000 Wortartikel, 666 Werke, 28.000 User/Jahr (S. 162); 10 Mio. Tokens zur Zeit des TreeTaggers (S. 167); 666 E-Texte in TEI (S. 170); 1,5 Stellen ab 2004 (S. 165).
- **Abb. 5** (S. 166, PDF 7), „Tabellenstruktur der relationalen Datenbank", ohne Erläuterung im Text; eigene Lesung des Bildes, Auflösung gering: Eine Tokentabelle hat je Zeile u. a. die Spalten TEXT, LINE, POS, STRING, GRAMMAR, **MEANING**, WORD, LEMMA, NOTE, SOURCE. Ein Wert aus MEANING führt zu einer Tabelle mit vier CATEGORY-Einträgen, eine Kategorie zu einer Tabelle mit NAME und PARENT (Beispiel ‚Gastgewerbe'). Eine weitere Tabelle verknüpft einen STRING mit MEANINGLEMMA und TRIERID. Die Bedeutungsspalte steht also in der Zeile des Tokens.
- **Abb. 8** (S. 171, PDF 12), „Vereinfachtes Datenmodell der neuen MHDBDB": Token verweist auf Dictionary Entry (mit Lemma), auf einen Sense (Sense I oder II, je mit mehreren Concepts) und auf POS; Token gestrichelt mit der TEI-Edition verbunden; Standards TEI XML, Web Annotation Vocabulary, LEMON, Lemon-tree, SKOS.
- **Abb. 11 bis 14** (S. 177 bis 178): Frontend-Entwurf. Begriffssystem als Baum (Beispiel ‚Obstbau'); Wortartikel *wahsen* mit „Begriffsfeld 1, 2, 3" (je Sense-URI, Begriffe, Belegstellen), bei Begriffsfeld 2 der Vermerk „Wort nicht im Korpus"; „Graphische Varianz" mit Wortformen und Vorkommen.

## Wörtliche Stellen

> „Die einzelnen Vorkommensformen im Korpus (Tokens) werden auf diese Lemmata und die im Kontext gültige Bedeutung sowie auf weitere Annotationsebenen wie beispielsweise grammatikalische Daten oder Metadaten (s. u.) bezogen." (S. 162)

> „Inzwischen sind alle Texte voll lemmatisiert, die Lyrik und der größte Teil der Kurzprosa zusammen mit einigen Epen sogar disambiguiert. Diese Daten werden besonders hilfreich bei der Entwicklung eines lernfähigen Disambiguierungsmoduls sein." (S. 174)

> „Bislang wurde beispielsweise jedes Token ›Walther‹ über den Wortindex mit dem Begriffskonzept ›Literatur/Namen‹ verknüpft […]." (S. 173)

> „Aus diesem Grund wurde das Begriffssystem mittlerweile in einen polyhierarchischen SKOS-Thesaurus überführt […]." (S. 172)

## Bezug zur Dissertation

- **PROTOKOLL §2, Silber:** Der Beitrag sagt, **welche** Texte disambiguiert sind (Lyrik, größter Teil der Kurzprosa, einige Epen, S. 174), aber nicht **wer**, **wann** und **nach welchen Richtlinien**. Damit bleibt die Begründung für „Silber, nicht Gold" unberührt. Die Selbsteinschätzung „gut kuratiert, dokumentiert" (S. 174) ist keine Dokumentation der Annotationsrichtlinien.
- **PROTOKOLL §3, Domänen D1/D0:** S. 174 ist die einzige gedruckte Angabe, welche Teile des Korpus disambiguiert sind. Prüfbar wäre, ob die 203 D1-Texte überwiegend Lyrik und Kurzprosa sind; gemacht ist das nicht. Falls ja, ist die gemessene Silberqualität vor allem die dieser Gattungen.
- **Typ-Lesart (§2, A12; `knowledge/data.md` B1, Abschnitt 3):** Zwei Stellen sind zu beachten, keine entscheidet die Frage. (a) Für Namen beschreibt der Text eine Zuordnung „über den Wortindex", also über die Wortform (S. 173). (b) Abb. 5 zeigt im alten ORACLE-Schema eine MEANING-Spalte in der Tokenzeile (S. 166). Das spricht eher für eine Bedeutung pro Beleg (vgl. B3) als für eine reine Typbindung, sagt aber nicht, wie der Wert gesetzt wurde. Beide Beobachtungen gehören in die Frage an KZW.
- **PROTOKOLL §2, Inventar, und §5:** Abb. 8 (S. 171) zeigt Senses als Gruppen mehrerer Concepts. Das stützt die Definition des Sense über seine Begriffszeiger.
- **`knowledge/data.md` B11 (Polyhierarchie, Zahlencode):** S. 172 bis 173 bestätigt die Überführung in einen polyhierarchischen SKOS-Thesaurus bei Erhalt des „weitaus größten Teils" des alten, hierarchischen, zifferncodierten Systems. Das passt zum Befund „Zahlencode bildet einen Primärbaum".
- **`knowledge/data.md` B9 (Senses ohne Beleg):** Der Frontend-Entwurf zeigt Senses mit „Wort nicht im Korpus" (S. 177). Unbelegte Senses sind also im Inventar vorgesehen, nicht nur ein Datenfehler.
- **`knowledge/data.md` B13:** `skos:definition` und `skos:editorialNote` sind im SKOS-Modell vorgesehen (S. 173); im heutigen `concepts.xml` finden sich davon laut B13 nur wenige menschliche Glossen an Senses. Der Text sagt nicht, wie viele Definitionen tatsächlich angelegt wurden.
- **Forschungsstand:** S. 174 kündigt ein „lernfähiges Disambiguierungsmodul" an. Die Dissertation kann sich als eine Umsetzung oder Prüfung dieses Vorhabens einordnen.

## Grenzen und Einwände

- Rückblick mit persönlichem Charakter, keine Methoden- oder Datendokumentation.
- Abweichungen zu anderen Quellen: Salzburg 2004 (hier) gegenüber 2002 (Hinkelmanns & Zeppezauer-Wachauer 2023, S. 179); Relaunch-Vorbereitung seit 2017 (hier S. 168) gegenüber 2016 (2023, S. 179); ORACLE 1998 (hier S. 165) gegenüber „seit 1995 nicht wesentlich verändert" bzw. „1992" (Hinkelmanns 2019, S. 130 und Abstract).
- Hallig & Wartburg wird hier mit Berlin 1963 zitiert (S. 183), bei Hinkelmanns 2019 mit 1952.
- Abb. 5 ist im PDF klein; die Spaltennamen sollten an einer besseren Fassung oder bei KZW bestätigt werden, bevor sie zitiert werden.

## Weiterführend

- Schmidt 1978, Wege zu Begriffsglossaren und einem Begriffswörterbuch mhd. Epik, in Lenders & Moser (Hg.), S. 127 bis 146 (S. 184).
- Schmidt 1988, Der Beitrag der begriffsorientierten Lexikographie …, in Bachofer (Hg.), S. 35 bis 49; zur Herkunft des Begriffssystems zitiert mit „S. 40" (S. 172, 184).
- Schmidt 1993, Begriffsglossar zu Ulrichs von Zatzikhoven ‚Lanzelet', S. VII bis X (S. 172, 184).
- Springeth 2009, Der analytische Weg ist das Ziel, in Hofmeister & Hofmeister-Winter (Hg.), S. 185 bis 202; zitiert mit „S. 194" (S. 172, 185).
- Pütz & Schmidt 2001, ZfdA 130, S. 493 bis 495 (S. 184).
- Ketschik, Reiter & Schulz 2017, Ein PoS-Tagger für ‚das' Mittelhochdeutsche, DHd 2017, S. 141 bis 147 (S. 183).
- Plate 1992, Onomasiologische Umkehrlexikographie auf dem Prüfstand, ZDL 59, S. 312 bis 329 (S. 181 bis 182, Anm. 8).
- Hallig & Wartburg 1963 (S. 183).

## Julias Markierungen im PDF

Für dieses PDF gibt es keine Datei `md/…markierungen.md`.
