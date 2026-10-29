# Mambrini & Passarotti 2023: The LiLa Lemma Bank

**Datei:** `pdf/Mambrini-Passarotti-2023-LiLa.pdf` (nur lokal; Verlags-PDF, 5 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganzes PDF an der Textebene gelesen; bibliografische Angaben am Zitiervorschlag (S. 1 und 5).

Seitenzählung: PDF-Seite n = gedruckte S. n (Zitiervorschlag „pp. 1–5", S. 1).

## Bibliografie

- **Vollständig:** Mambrini, Francesco & Passarotti, Marco Carlo (2023). The LiLa Lemma Bank: A Knowledge Base of Latin Canonical Forms. *Journal of Open Humanities Data* 9: 28, S. 1 bis 5. Collection „Representing the Ancient World through Data".
- **DOI/URL:** https://doi.org/10.5334/johd.145 (Zitiervorschlag S. 1 und 5 ✔; Auflösung laut `BESCHAFFUNG.md` am 2026-10-23 geprüft). Eingereicht 31.08.2023, angenommen 26.10.2023, veröffentlicht 24.11.2023 (S. 5). Artikel CC BY 4.0, Ubiquity Press (S. 5). Crossref (abgerufen 2026-10-29): Band 9, Artikelnummer 28, keine Heftnummer; die Angabe „9(1)“ in älteren Einträgen ist durch nichts gedeckt.
- **Art:** begutachteter Data Paper („peer-reviewed open access journal", S. 5)
- **Sprache:** Englisch

## Worum es geht

Ein Data Paper zur LiLa Lemma Bank: 215.102 lateinische Wörterbuchformen (Lemmata) mit stabilen URIs, beschrieben in 1.699.687 RDF-Tripeln mit OWL-Ontologien für Linguistic Linked Data (Abstract, S. 1). Die Lemma Bank ist der Knoten, über den das Projekt LiLa Korpora und Wörterbücher verknüpft: Ressourcen werden angebunden, indem ihre Lemma-Zeichenketten auf Einträge der Lemma Bank abgebildet werden (S. 2). Bedeutungen modelliert die Lemma Bank nicht; sie ist ein Lemma- und Morphologie-Inventar.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Ziel: alle Wörterbuchformen, die Lemmatisierungsprojekte des Lateinischen brauchen, unabhängig von deren Strategie, jede mit stabiler URI und mit OWL/OntoLex modelliert. | S. 2, Method | eigenes Vorgehen |
| Ausgangspunkt ist die Lemmaliste des Analysators LEMLAT 3.0, zusammengestellt aus klassischen Wörterbüchern (Georges, Oxford Latin Dictionary, Gradenwitz), Forcellinis Onomasticon und dem mittellateinischen Glossar von Du Cange. | S. 2 | referiert/Projektgeschichte |
| Revision in zwei Schritten: Dubletten zwischen klassischem und mittelalterlichem Latein manuell zusammengeführt; als Lemma wählbare Flexionsformen (Partizipien, deadjektivische Adverbien) ergänzt. | S. 2 | eigenes Vorgehen |
| Qualitätskontrolle über die Verknüpfung selbst: Beim Anbinden von 10 lexikalischen Ressourcen und 9 Korpora fielen fehlende Lemmata (v. a. Eigennamen) und Dubletten auf, die manuell ergänzt bzw. zusammengeführt wurden. | S. 2, Quality control | eigenes Ergebnis |
| Daten liegen in einer relationalen Datenbank (MariaDB); die RDF-Tripel werden daraus erzeugt; beide Fassungen (RDF und SQL) werden mit Anleitung veröffentlicht. | S. 2 | eigenes Vorgehen |
| Nachnutzung: andere Projekte können die URIs verwenden; OntoLex wird als „W3C de-facto standard" für lexikalische Information bezeichnet; Wikidata-Lexeme verlinken mit eigener Property auf LiLa. | S. 3, Reuse potential | Einschätzung/Beispiel |
| Für NLP soll die Lemma Bank Lemmatisierung, PoS-Tagging und Morphologieanalyse unterstützen, etwa über ein lemmatisiertes Metakorpus aus den verknüpften Korpora. | S. 4 | Ausblick, nicht gezeigt |

## Daten, Methode, Zahlen

An der Textebene geprüft:

- 215.102 Lemmata (Version 1.2), 1.699.687 RDF-Tripel (S. 1); erste Version 2020 mit 196.853 Lemmata (S. 2).
- Verknüpft: 10 lexikalische Ressourcen, 9 Korpora (S. 2); Beispiel LASLA Opera Latina mit ca. 1,7 Millionen lemmatisierten Wörtern (S. 2).
- Erstellt 2020-11-25 bis 2023-08-30; Version 1.2 veröffentlicht 2023-08-30; Formate Turtle-RDF und SQL; Repositorien Zenodo (https://doi.org/10.5281/zenodo.8300851) und GitHub (S. 2 und 3).
- **Lizenzen unterscheiden sich:** Datensatz V1.2 CC BY-SA 4.0; die erste Turtle-Fassung lag im ILC-CNR-CLARIN-Repositorium unter CC BY-NC-SA 4.0 (S. 3); der Artikel selbst CC BY 4.0 (S. 5).
- Zwölf beteiligte Personen mit Rollen (Supervisor, Developer, Annotator) sind namentlich aufgeführt (S. 3).

## Wörtliche Stellen

> „Linking those resources means to match the lemma string used to lemmatize the entries in the original resource to the entries in our Lemma Bank." (S. 2)

## Bezug zur Dissertation

- **Vergleich der Modelle, nicht Methode:** Die Lemma Bank zeigt das Gegenstück zum MHDBDB-Aufbau: ein lemmazentriertes Hub, an das Korpora und Wörterbücher per Lemma-URI andocken, ohne eigene Bedeutungsebene. Die MHDBDB legt dagegen Bedeutungen als Mengen von Begriffszeigern an das Lemma (`knowledge/data.md` Abschnitt 1; PROTOKOLL §2 „Inventar"). Für die Einordnung des Inventars in der Arbeit: LiLa beantwortet „welches Lemma?", die MHDBDB zusätzlich „welcher Begriff?".
- **Zum geplanten LOD-Modell der MHDBDB:** Hinkelmanns (2019, S. 135 bis 137; `zusammenfassungen/Hinkelmanns-2019-MHD-Lexikographie-Semantic-Web.md`) plant OntoLex mit Lemon-tree und eindeutige Token-IDs; die Lemma Bank ist ein publiziertes Beispiel dafür, wie ein solcher Lemma-Knoten mit stabilen URIs, Versionsnummer und Lizenz aussehen kann.
- **Reproduzierbarkeit (PROTOKOLL §4.10, §10):** Die Lemma Bank ist versioniert (V1.2, Datum, DOI). Das ist dieselbe Anforderung, die das Protokoll an `lexicon.xml` und `concepts.xml` stellt (Korpus-Commit und Prüfsummen im Manifest). Kein neuer Befund, nur ein Vergleichsfall.
- **Lemma-Fehler:** Dubletten und fehlende Lemmata zeigten sich erst beim Verknüpfen (S. 2). Das passt zum Status `LEMMA_FALSCH` (PROTOKOLL §6) und zu `knowledge/data.md` B5 (66 Tokens mit `@lemmaRef` ins Leere): Lemmaebene ist auch in kuratierten Ressourcen nicht fehlerfrei.

## Grenzen und Einwände

- Data Paper von fünf Seiten: keine Evaluation, keine Fehlerquote der Lemmaabbildung, keine Zahl zu den manuellen Korrekturen.
- Keine Bedeutungsebene; für WSD nur mittelbar relevant.
- Klassisches und mittelalterliches Latein werden zusammengeführt; wie Bedeutungs- oder Formwandel behandelt wird, sagt der Beitrag nicht (die „Historical Semantic Gap" bei Tittel & Chiarcos 2018 stellt sich hier nicht, weil keine Begriffe verknüpft werden).

## Weiterführend

- Passarotti et al. 2020, *Interlinking through Lemmas*, Studi e Saggi Linguistici 58, S. 177 bis 212 (S. 2, 5): ausführlichere Beschreibung des Modells.
- Fantoli et al. 2022, Anbindung des LASLA-Korpus, LDL-2022 (S. 2, 4).
- Khan et al. 2022, Überblick Linguistic Linked Data, Semantic Web 13(6) (S. 2, 5).
- McCrae et al. 2017, OntoLex-Lemon, eLex 2017 (S. 2, 5).
- Mambrini & Passarotti 2020, Etymologie in LiLa, GLOBALEX 2020 (S. 3, 5).
