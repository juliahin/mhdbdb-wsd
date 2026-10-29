# Telljohann et al. 2017: Stylebook for the Tübingen Treebank of Written German (TüBa-D/Z)

**Datei:** `pdf/Telljohann-etal-2017-TueBa-DZ-Stylebook.pdf` (nur lokal; 166 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29. Kapitelweise gelesen (Auswahl unten begründet), an der Textebene; Zahlen der Einleitung am Seitenbild geprüft. Priorität 3 (Hintergrund), daher knapp.

**Seitenzählung:** gedruckte Seite = PDF-Seite − 1 (PDF 2 = S. 1, Abstract; PDF 10 = S. 9, Kap. 1); Titelblatt (PDF 1) ohne Seitenzahl. Unten stehen gedruckte Seiten, die PDF-Seite in Klammern.

**Auswahl der Kapitel (nach dem Inhaltsverzeichnis S. 5 bis 7 (PDF 6 bis 8)):** Gelesen wurden Abstract und Danksagung (S. 1 bis 4: Umfang, Annotationsablauf, Konsistenzprüfungen), Kap. 1 und 2 (Umfang, Designentscheidungen), 3.3 (Annotationsprinzipien, darunter der Umgang mit Ambiguität), 3.4.1 bis 3.4.2 (Annotationsebenen, Wortarten nach STTS, Werkzeug), 3.4.4 (Druck- und Schreibfehler), **3.5 Lemmatisierung**, 4.2.6 (Named Entities mit semantischen Klassen, die einzige semantische Ebene im Stylebook), 7.2 (verbaler und adjektivischer Gebrauch von Partizipien, übernommen aus STTS) und **Kap. 9 Datenformate** (dort die einzige Erwähnung von GermaNet-Senses). Eine eigene Ebene oder ein Kapitel zu Wortbedeutungen gibt es im Inhaltsverzeichnis nicht; GermaNet kommt nur als Spalte in zwei Datenformaten vor (S. 159 bis 160 (PDF 160 bis 161)). Nur benannt, nicht zusammengefasst: die Syntaxkapitel 3.1 bis 3.2 (topologische Felder), 3.4.3, 3.4.5 bis 3.4.7, 4 (außer 4.2.6: Phrasen), 5 (Anbindung), 6 (Sätze, Koordination, Ellipse), 7 (außer 7.2) und 8 (grammatische Funktionen).

## Bibliografie

- **Vollständig:** Telljohann, Heike, Erhard W. Hinrichs, Sandra Kübler, Heike Zinsmeister & Kathrin Beck (2017). *Stylebook for the Tübingen Treebank of Written German (TüBa-D/Z)*. Universität Tübingen, Seminar für Sprachwissenschaft. Juli 2017 (Titelblatt, PDF 1).
- **DOI/URL:** keine DOI. https://hinrichs.sfs.uni-tuebingen.de/files/tbs/tuebadz-stylebook-1707.pdf; das lokale PDF ist **byte-gleich** (SHA-256) mit dieser Datei (abgerufen 2026-10-29). Die Releaseseite der Universität Tübingen (https://uni-tuebingen.de/en/134290, abgerufen 2026-10-29) führt sie als „Stylebook 2017“ neben den Fassungen 2003, 2005, 2006, 2009, 2012 und 2015.
- **Fassung:** laut Abstract eine aktualisierte Fassung von Telljohann et al. 2015 (S. 1 (PDF 2)). Release-Datum widersprüchlich: Das Stylebook nennt „Release 11 in July 2017“ als letzte Veröffentlichung (S. 1, S. 10 (PDF 2, 11)), die Releaseseite „Release 11.0 (06/2018) [Final Release]“.
- **Art:** Annotationsrichtlinie (technischer Bericht), nicht begutachtet
- **Sprache:** Englisch

## Worum es geht

Das Stylebook beschreibt Designprinzipien und Annotationsschema der TüBa-D/Z, einer Baumbank aus Artikeln der *taz* (S. 9 (PDF 10)). Es richtet sich an die Tübinger Annotator:innen und an Nutzer:innen der Daten und rät davon ab, das sprachspezifische Schema unverändert auf andere Sprachen zu übertragen (S. 9 (PDF 10)). Der Schwerpunkt liegt auf der syntaktischen Annotation (topologische Felder, Phrasen, grammatische Funktionen). Auf der lexikalischen Ebene stehen STTS-Wortarten, Morphologie und Lemmata, alle automatisch vorannotiert und manuell korrigiert (S. 19, 33 (PDF 20, 34)). Werte zur Übereinstimmung zwischen Annotator:innen enthält das Stylebook nicht.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Umfang: 3.816 Artikel, 104.787 Sätze aus taz-Ausgaben 1989 bis 1999, mittlere Satzlänge 18,7 Wörter, 1.959.474 Tokens. | S. 1 (PDF 2); S. 9 bis 10 (PDF 10 bis 11) | Projektangabe |
| Zwei Leitlinien: linguistische Adäquatheit bei Theorieneutralität („theory-neutral and minimal“) und Ausgleich der Bedürfnisse möglichst vieler Nutzer:innen. | S. 11 (PDF 12), Kap. 2 | Designentscheidung |
| Inventar: 25 syntaktische Knotenlabels, 42 Kantenlabels plus 4 sekundäre; Wortarten nach STTS mit „54 distinct part-of-speech labels“, dazu Flexionsmorphologie. | S. 12 (PDF 13), Kap. 2 | Beschreibung |
| Vier Annotationsebenen (Tab. 3.3): Satz, Felder, Phrasen, lexikalische Ebene (STTS-Tags, Morphologie, Lemmata). Anaphern und Koreferenz behandelt das Stylebook nicht (Verweis auf Naumann & Möller 2007). | S. 19 (PDF 20), 3.4.1 mit Anm. 2 | Beschreibung |
| Wortarten wurden mit dem TnT-Tagger vorannotiert und mit Annotate manuell korrigiert. STTS ist abgewandelt: PAV heißt hier PROP. | S. 19 (PDF 20), 3.4.2 mit Anm. 3 | Projektangabe |
| **Ambiguität:** Nach dem High Attachment Principle werden syntaktisch und semantisch ambige Modifikatoren am höchstmöglichen Knoten angebunden; Postmodifikatoren stehen immer höher, „to preserve ambiguity“. | S. 18 (PDF 19), 3.3.3; S. 40 (PDF 41), 4.1 | Richtlinie |
| **Lemmata:** Alle Tokens tragen ein Lemma; Morphologie und Lemmatisierung werden automatisch vorannotiert, die Ausgabe wird „manually disambiguated and corrected“. | S. 33 (PDF 34), 3.5 | Projektangabe |
| **Homonyme und Polyseme werden im Lemma nicht unterschieden:** „homonyms and polysemes keep their base form“ (*Schlösser* → *Schloß*, *Flügeln* → *Flügel*). | S. 34 (PDF 35), Tab. 3.10 | Richtlinie |
| **Mehrwertige Lemmata zulässig:** Bei Pluralformen ohne erkennbares Genus werden alle möglichen Lemmata mit `|` aufgeführt (*Jugendliche* → `Jugendlicher|Jugendliche|Jugendliches`; *die* (PDS) → `der|die|das`). | S. 38 (PDF 39), Tab. 3.11 | Richtlinie |
| Weitere Lemmaregeln: substantivierte Adjektive in der starken Form (*der Schöne* → *Schöner*), Partikelverben als `ein#stellen`, Hilfs- und Modalverbgebrauch mit Suffix `%aux`, Passiv mit `%passiv`, Schreibvarianten als getrennte Lemmata (*fantastisch* / *phantastisch*), Dialektformen auf das Standardwort abgebildet. | S. 34 bis 38 (PDF 35 bis 39), Tab. 3.10 und 3.11 | Richtlinie |
| Druck- und Schreibfehler werden nicht korrigiert annotiert: Die richtige Schreibung steht in einer Kommentarzeile, nicht zur Konstruktion gehörende Elemente bleiben unangebunden. | S. 28 bis 29 (PDF 29 bis 30), 3.4.4 | Richtlinie |
| **Named Entities** erhalten eine von fünf semantischen Klassen (PER, ORG, LOC, GPE, OTH), als Knotenlabel „syntaktische Kategorie = semantische Klasse“. Die Abgrenzung von Eigenname und Appellativum „is not always clear-cut“ (*Opel* als Firma NE, als Auto NN). | S. 56 bis 57 (PDF 57 bis 58), 4.2.6; S. 20 (PDF 21) | Richtlinie |
| Für verbalen gegen adjektivischen Gebrauch von Partizipien übernimmt das Stylebook die drei STTS-Kriterien (Aktivtest, *von*-PP, Ersetzung durch ein semantisch ähnliches Adjektiv). | S. 133 (PDF 134), 7.2 | übernommen aus STTS |
| **GermaNet-Senses nur in den Datenformaten:** CoNLL 2011/2012 hat eine Spalte „Word sense – GermaNet ID of the word sense“; CoNLL-U v2 führt in MISC „LexUnit: GermaNet ID of the word sense (only partially annotated …)“ mit Verweis auf die GermaNet-Korpusseite. Regeln für die Sense-Annotation enthält das Stylebook nicht. | S. 159 (PDF 160), 9.4.3; S. 160 (PDF 161), 9.4.4 | Formatbeschreibung |
| Das NEGRA-Exportformat ist das vollständigste, „since it preserves all the information available during the manual annotation“; Formate: NEGRA Export, Penn Treebank v1/v2, Export-XML (mit Anaphern), CoNLL 2006, 2010, 2011/12, CoNLL-U v2. | S. 146 (PDF 147), 9.1 | Formatbeschreibung |
| **Qualitätssicherung** wird nur in der Danksagung erwähnt: merkmalsbasierte Konsistenzprüfungen (Ventsislav Zhechev) und weitere Konsistenztests (Tylman Ule, Frank H. Müller) hätten die Qualität „considerably improved“; Hilfskräfte hätten durch „dedicated discussions on problematic and interesting examples“ beigetragen. **Keine Übereinstimmungswerte.** | S. 3 (PDF 4), Danksagung; gelesene Kapitel und Suche nach „agreement“, „consisten“, „kappa“ | Projektangabe; Fehlen von IAA Befund dieser Prüfung |

## Daten, Methode, Zahlen

- Korpus nach Jahrgängen (S. 9 (PDF 10), am Seitenbild geprüft): 1989 661 Artikel / 34.057 Sätze; 1992 632 / 12.245; 1995 1.107 / 21.391; 1997 238 / 7.497; 1999 1.039 / 22.195; 1998 139 / 7.402; zusammen 3.816 Artikel aus 452 Tagen in 29 Monaten aus 6 Jahren, 104.787 Sätze. Die Summen gehen auf (eigene Nachrechnung).
- Tokens 1.959.474, mittlere Satzlänge 18,7 Wörter (S. 1, 10 (PDF 2, 11)).
- Inventar: 25 Knotenlabels, 42 plus 4 sekundäre Kantenlabels, 54 STTS-Tags (S. 12 (PDF 13)); Named-Entity-Klassen 5 (S. 56 (PDF 57)).
- Ablauf: automatische Vorannotation (TnT für Wortarten; Morphologie nach Trushkina 2004 und Versley et al. 2010; Lemmata nach Versley et al. 2010), manuelle Korrektur mit Annotate (S. 19, 33 (PDF 20, 34)). Zahl der Annotator:innen je Satz und Adjudikation nicht beschrieben; die Danksagung nennt 39 Hilfskräfte namentlich (S. 3 (PDF 4), eigene Zählung).

## Wörtliche Stellen

> „homonyms and polysemes keep their base form“ (S. 34 (PDF 35), Tab. 3.10)

> „The high attachment principle prescribes that syntactically and semantically ambiguous modifiers are attached to the highest possible level in a tree structure.“ (S. 18 (PDF 19))

> „Word sense - GermaNet ID of the word sense“ (S. 159 (PDF 160))

## Bezug zur Dissertation

- **GermaNet-Senses in der TüBa-D/Z, Henrich 2015 und GernEdiT:** Das Stylebook belegt nur, dass die Daten eine (teilweise gefüllte) Spalte mit GermaNet-IDs haben (S. 159 bis 160 (PDF 160 bis 161)). Wer annotiert hat, nach welchen Regeln und mit welcher Übereinstimmung, steht bei Henrich 2015, Kap. 5.3 (Zusammenfassung `Henrich-2015-WSD-GermaNet.md`: 109 Lemmata, Dice 96,4 / 93,7 %). Für Aussagen über die Sense-Annotation also Henrich zitieren, nicht das Stylebook. GermaNet selbst wird mit Hamp & Feldweg 1997 und Henrich & Hinrichs 2010 zitiert (`Henrich-Hinrichs-2010-GernEdiT.md`, Zitierhinweis).
- **PROTOKOLL §2 (Inventar = Senses eines Lemmas) und §4.3 (Polysemie):** In der TüBa-D/Z trennt das Lemma keine Homonyme (S. 34 (PDF 35)); jede Bedeutungsunterscheidung liegt dort auf der Sense-Ebene. Werden Polysemiezahlen aus Henrichs TüBa-D/Z-Annotation mit der MHDBDB verglichen (Polysemiestufen 2 / 3 / 4+), ist zu prüfen, ob die MHDBDB Homographen schon als getrennte Lemmata führt; dann zählten dort Unterschiede, die in der TüBa-D/Z Senses sind, gar nicht als Polysemie. Das ist eine Frage an die Daten, das Stylebook beantwortet sie nicht.
- **`knowledge/data.md`, Abschnitt 1 (Token-`@pos` oft mehrwertig):** Die TüBa-D/Z erlaubt mehrwertige Annotation auf der Lemmaebene, aber eng begrenzt und regelgeleitet (nur bei unbestimmbarem Genus im Plural, S. 38 (PDF 39)). Die mehrwertigen MHDBDB-Werte (`NOM ADJ ADV`) sind dagegen ungeregelt. Als Vergleich für das Datasheet brauchbar: Mehrwertigkeit ist legitim, wenn sie eine definierte Unterspezifikation ist.
- **PROTOKOLL §6, Status `MEHRERE`:** Wie im Paper von 2004 gilt Hochanbindung als Mittel, Ambiguität zu erhalten statt aufzulösen (S. 18, 40 (PDF 19, 41)). Das stützt die Seite der Argumentation, die ein Ausweichlabel für unentscheidbare Fälle vorsieht (siehe `Telljohann-etal-2004-TueBa-DZ.md`).
- **PROTOKOLL §2 und §7 (blind und unabhängig):** Das TüBa-D/Z-Verfahren ist automatische Vorannotation plus manuelle Korrektur (S. 19, 33 (PDF 20, 34)). Das ist das Gegenmodell zum Protokoll, das Annotator:innen keine Vorbelegung zeigt (vgl. `knowledge/data.md` B1: Typlisten als Leckgefahr). Für die Diskussion, warum Silber nicht als Vorschlag gezeigt wird, ist das ein Beispiel, wie große Ressourcen es anders machen; über die Folgen für die Qualität sagt das Stylebook nichts.
- **STTS-Bezug:** TüBa-D/Z zitiert STTS als „Schiller, Teufel & Thielen 1995“ (S. 162 (PDF 163)) und weicht in einem Tag ab (PROP statt PAV, S. 19 (PDF 20)); siehe `Schiller-etal-1999-STTS.md`.

## Grenzen und Einwände

- Kein Wort zu Übereinstimmung zwischen Annotator:innen; Konsistenzprüfungen sind nur in der Danksagung genannt, ohne Verfahren oder Zahlen.
- Die Sense-Spalte ist „only partially annotated“ (S. 160 (PDF 161)); ihren Umfang nennt das Stylebook nicht.
- Gegenwartsdeutsch, eine Zeitung, sechs Jahrgänge: als Vergleich zu einem mittelhochdeutschen Korpus mit vielen Gattungen nur bedingt geeignet.
- Auswahl: Rund zwei Drittel des Umfangs (Syntaxkapitel 3.1 bis 3.2, 4 bis 8) wurden bewusst nicht gelesen; Aussagen über das Gesamtschema gelten nur, soweit Kap. 1 bis 3 sie zusammenfassen.
- Release-Datum uneinheitlich (Juli 2017 im Stylebook, 06/2018 auf der Releaseseite).

## Weiterführend

- Versley, Beck, Hinrichs & Telljohann 2010, Morphologie und Lemmadisambiguierung der TüBa-D/Z (S. 163 (PDF 164)).
- Naumann & Möller 2007, Annotation von Anaphern und Koreferenz (S. 13, 162 (PDF 14, 163)).
- Çöltekin, Campbell, Hinrichs & Telljohann 2017, Umwandlung in Universal Dependencies (S. 160, 161 (PDF 161, 162)).
- Henrich & Hinrichs 2014 (TLT13), Konsistenz manueller Sense-Annotation in der TüBa-D/Z; nicht im Stylebook zitiert, aber in `Henrich-2015-WSD-GermaNet.md` (Weiterführend) genannt.

## Julias Markierungen im PDF

Für dieses PDF gibt es keine Datei `md/…markierungen.md`; `markierungen.py` fand am 2026-10-29 keine Anmerkungen.
