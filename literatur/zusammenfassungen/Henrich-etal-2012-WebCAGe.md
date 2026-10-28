# Henrich, Hinrichs & Vodolazova 2012: WebCAGe

**Datei:** `pdf/Henrich-etal-2012-WebCAGe.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->

**Stand:** 2026-10-28, PDF vollständig gelesen (10 Seiten, rohe Textebene); Tabellen 1 bis 3 und Abb. 1 und 4 am Seitenbild geprüft, Tabelle 1 nachgerechnet; Bibliografie an der ACL Anthology (E12-1039) bestätigt; Abgleich mit `Henrich-2015-WSD-GermaNet.md` und Kap. 5.2 und 6.2 der Dissertation.

**Seitenzählung:** Gedruckte Seite = PDF-Seite + 386 (S. 387 = PDF 1, S. 396 = PDF 10). Zitiert wird die gedruckte Seite, die PDF-Seite in Klammern.

**Verhältnis zu Henrich 2015:** Kap. 5.2 der Dissertation übernimmt diesen Beitrag weitgehend wörtlich und erweitert ihn (Version 3.0, Mehrfach-Senses, MFS). Wo sich beides deckt, steht hier nur der Verweis; Abweichungen sind unter „Grenzen und Einwände“ gesammelt.

## Bibliografie

- **Vollständig:** Henrich, Verena; Hinrichs, Erhard & Vodolazova, Tatiana, 2012. WebCAGe – A Web-Harvested Corpus Annotated with GermaNet Senses. In: Walter Daelemans (Hg.), *Proceedings of the 13th Conference of the European Chapter of the Association for Computational Linguistics (EACL 2012)*, Avignon, April 2012. Association for Computational Linguistics, S. 387 bis 396.
- **DOI/URL:** kein DOI im Eintrag; https://aclanthology.org/E12-1039/ (Titel, Autor:innen, Herausgeber, Seiten am 2026-10-28 dort abgelesen; Seiten und Tagung auch im Kopf von S. 387 (PDF 1)). Korpusseite des Projekts: https://uni-tuebingen.de/en/134278 (verlangt dieses Zitat).
- **Art:** Konferenzbeitrag (begutachtet; Dank an „three anonymous EACL 2012 reviewers“, S. 395 (PDF 9))
- **Sprache:** Englisch

## Worum es geht

Der Beitrag beschreibt ein Verfahren, ein sense-annotiertes Korpus automatisch aus dem Web zu ernten, und wendet es auf Deutsch an (S. 387 (PDF 1)). Ausgangspunkt ist eine vorhandene, manuell nachkorrigierte Zuordnung von GermaNet-Senses zu Bedeutungen im deutschen Wiktionary: Die Beispielsätze eines Wiktionary-Sense und die daran verlinkten Texte (Wikipedia, Projekt Gutenberg, andere Webseiten) erben den zugeordneten GermaNet-Sense (S. 389 bis 390 (PDF 3 bis 4)). Ergebnis ist WebCAGe mit 10.750 annotierten Tokens zu 2.607 polysemen Wörtern, damals das größte sense-annotierte Korpus des Deutschen (S. 392 bis 393 (PDF 6 bis 7)). Evaluiert wird nur die automatische Erkennung der Zielwörter (Precision und Recall meist über 92 %), nicht die Richtigkeit der Sense-Zuordnung; eine Übereinstimmung zwischen Annotator:innen wird nicht berichtet (S. 392 bis 394 (PDF 6 bis 8)).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Große sense-annotierte Korpora sind Voraussetzung für überwachte und viele halbüberwachte WSD-Verfahren; manuell erstellt sind sie teuer, für viele Sprachen fehlen sie. | S. 387 (PDF 1), Abschn. 1 | eigene Begründung |
| Drei Kriterien für ein automatisches Verfahren: sprachunabhängig; Qualität so hoch, dass die Daten ohne oder mit minimaler Nachkorrektur nutzbar sind; nicht trivial groß, erweiterbar, domänenunabhängig, frei verfügbar. | S. 387 (PDF 1), Abschn. 1 | eigene Festlegung |
| Benötigt werden nur ein Inventar und eine Zuordnung dieses Inventars zu einer Webressource wie Wiktionary oder Wikipedia. | S. 387 bis 388 (PDF 1 bis 2), Abschn. 1 | eigenes Verfahren |
| Ein Wordnet als Gold-Inventar zu nehmen entspricht der Praxis für Englisch (Princeton WordNet). | S. 388 (PDF 2), Fn. 3 | eigene Begründung |
| Die Zuordnung GermaNet zu Wiktionary entstand in zwei Stufen: automatische Wortüberlappung, dann manuelle Nachkorrektur; die automatische Stufe war zu 93,8 % richtig. | S. 389 (PDF 3), Abschn. 3 | referiert aus eigener Vorarbeit (Henrich et al. 2011) |
| Beispielsätze eines Wiktionary-Sense und die verlinkten Texte werden über die Zuordnung automatisch mit dem GermaNet-Sense annotiert. | S. 389 bis 390 (PDF 3 bis 4), Abschn. 3 | eigenes Verfahren |
| „One sense per discourse“: Alle Vorkommen des Zielworts in einem Text erhalten denselben Sense. Laut „inspection“ ist das richtig für 99,96 % der Vorkommen in Wiktionary-Beispielen, 96,75 % in externen Webseiten, 95,62 % in Wikipedia. | S. 390 (PDF 4), Abschn. 3 | eigene Messung; wie geprüft wurde und von wem, sagt der Text nicht |
| Nur echt mehrdeutige Zielwörter (mindestens zwei GermaNet-Senses) gehen in WebCAGe ein. | S. 390 (PDF 4), Abschn. 3 | eigene Festlegung |
| Die Zuordnung ist nicht immer eins zu eins: Entsprechen einem GermaNet-Sense zwei Wiktionary-Senses, erhalten beide Beispielgruppen denselben Sense; ein GermaNet-Sense ohne Wiktionary-Gegenstück bekommt keine Belege (Beispiel *Archiv*). | S. 390 bis 391 (PDF 4 bis 5), Abschn. 3, Abb. 2 | eigenes Verfahren |
| Zielwörter im Deutschen zu finden verlangt Lemmatisierung, Kompositazerlegung und den Umgang mit abgetrennten Verbpartikeln; dafür OpenNLP, TreeTagger, BananaSplit und die Flexionstabellen aus Wiktionary. | S. 391 (PDF 5), Abschn. 4 | eigenes Verfahren |
| Pro Vorkommen werden ein GermaNet-Sense (Lexical-Unit-ID), das Lemma und die Wortart gespeichert; Komposita und Flexionsformen werden mit annotiert (Beispiel *Bogen* im Artikel *Violine*). | S. 391 bis 392 (PDF 5 bis 6), Abschn. 4, Abb. 4 | eigenes Ergebnis |
| WebCAGe ist deutlich größer als die zwei manuell erstellten deutschen Korpora (Broscheit et al. 2010; Raileanu et al. 2002). | S. 392 bis 393 (PDF 6 bis 7), Abschn. 5, Tab. 2 | eigener Vergleich |
| Precision und Recall der Zielworterkennung liegen für Wiktionary-Beispiele, externe Webseiten und Wikipedia über 92 %; einzige große Abweichung sind Verben in Gutenberg-Texten. | S. 393 bis 394 (PDF 7 bis 8), Abschn. 5, Tab. 3 | eigenes Ergebnis |
| Ohne Nachkorrektur bleiben etwa 2 bis 5 % Rauschen; die vollständige Nachkorrektur aller Vorkommen und das Nachtragen fehlender Zielwörter kostete eine erfahrene Hilfskraft 25 Stunden. | S. 393 (PDF 7), Abschn. 5 | eigenes Ergebnis |
| Frühere Ernteverfahren (Yarowsky 1995; Leacock et al. 1998; Agirre & Lopez de Lacalle 2004; Mihalcea & Moldovan 1999) beruhen auf manuell annotierten Saatbeispielen oder auf der Heuristik monosemer Verwandter; am nächsten verwandt ist Santamaría et al. 2003 (Zuordnung zu Webverzeichnissen). | S. 393 bis 395 (PDF 7 bis 9), Abschn. 6 | referiert |
| Auf Englisch übertragen (WordNet zu englischem Wiktionary) bestätigte sich die Anwendbarkeit. | S. 395 (PDF 9), Abschn. 6 | eigenes Ergebnis, nur verwiesen (Henrich et al. 2012, CICLing-Poster) |

## Daten, Methode, Zahlen

- **Inventar:** GermaNet 6.0 (April 2011): 93.407 lexikalische Einheiten in 69.594 Synsets; Adjektive, Nomen, Verben (S. 388 (PDF 2)).
- **Wiktionary:** Dump vom 2. Februar 2011, 46.457 deutsche Wörter mit 70.339 Senses, extrahiert mit JWKTL (S. 388 bis 389 (PDF 2 bis 3)). Die Projektseite nennt dagegen den 1. Februar 2011 (abgerufen 2026-10-28).
- **Größe (Tab. 1, S. 393 (PDF 7), am Seitenbild geprüft, Summen nachgerechnet und stimmig):**

| Quelle | annotierte Tokens | davon Adj. / Nomen / Verben | annotierte Sätze |
|---|---|---|---|
| Wiktionary-Beispiele | 7.644 | 575 / 4.103 / 2.966 | 7.475 |
| externe Webseiten | 589 | 31 / 446 / 112 | 563 |
| Wikipedia | 1.732 | 79 / 1.643 / 10 | 1.490 |
| Gutenberg | 785 | 28 / 655 / 102 | 752 |
| zusammen | 10.750 | 713 / 6.847 / 3.190 | 10.280 |

  Insgesamt umfassen die geernteten Texte 619.594 Sätze, davon 587.944 aus Gutenberg (ebd.).
- **Lemmata:** 2.607 polyseme Wörter (211 Adj., 1.499 Nomen, 897 Verben), im Mittel 2,9 GermaNet-Senses (2,4 / 2,6 / 3,6) (S. 392 (PDF 6); Tab. 2, S. 393 (PDF 7)). Im Mittel gut 4 Tokens pro Lemma (10.750 / 2.607, eigene Rechnung).
- **Vergleich (Tab. 2):** Broscheit et al. 2010: 40 Lemmata, etwa 800 Tokens, domänenunabhängig; Raileanu et al. 2002: 25 Nomen, 2.421 Tokens, medizinische Domäne (S. 393 (PDF 7)).
- **Zielworterkennung (Tab. 3, S. 394 (PDF 8), am Seitenbild geprüft):** Precision über alle Wortarten 97,32 % (Wiktionary), 96,19 % (Webseiten), 96,26 % (Wikipedia), 87,43 % (Gutenberg); Recall 97,94 / 97,32 / 93,36 / 95,42 %. Tiefster Wert: Verben in Gutenberg-Texten, Precision 69,87 %, Recall 89,20 %. Die Tabelle druckt einen Recall „92.70.%“ (Nomen, Wikipedia), ein Satzfehler der Vorlage.
- **Qualitätskontrolle:** (1) Zuordnung GermaNet zu Wiktionary manuell nachkorrigiert (S. 389 (PDF 3)); (2) Prüfung der Heuristik „one sense per discourse“ durch „inspection“ (S. 390 (PDF 4)); (3) Precision und Recall der Zielworterkennung (Tab. 3); (4) Nachkorrektur aller Vorkommen durch eine Hilfskraft, 25 Stunden (S. 393 (PDF 7)). Die Danksagung nennt drei Personen, die bei der Evaluation halfen (S. 395 (PDF 9)). **Keine Doppelannotation, keine Übereinstimmungsmaße, keine Stichprobe zur Richtigkeit der Sense-Labels.**
- **Mehrfach-Senses:** Der Beitrag nennt keine Zahl und beschreibt keinen Fall, in dem ein Vorkommen mehrere GermaNet-Senses erhält; das Datenformat nennt „the GermaNet sense, i.e., the lexical unit ID“ im Singular (S. 392 (PDF 6)), Abb. 4 zeigt je ein `lexUnit`. Der Anteil steht erst in Henrich 2015: 753 von 10.402 Annotationen in Version 3.0 (7,2 %, eigene Rechnung), entstanden, wo die Zuordnung mehrere GermaNet-Senses mit demselben Wiktionary-Eintrag verbindet (Henrich 2015, S. 151 bis 152 (PDF 165 bis 166), Tab. 6.1 und Fn. 1; siehe `Henrich-2015-WSD-GermaNet.md`).
- **„Kein Sense“:** kommt in WebCAGe nicht vor, weil nur Belege mit zugeordnetem Sense geerntet werden (so Henrich 2015, S. 150 (PDF 164); im Beitrag von 2012 nicht ausgesprochen, folgt aber aus S. 390 bis 391 (PDF 4 bis 5)).

## Wörtliche Stellen

> „The quality of the automatically generated data should be extremely high so as to be usable as is or with minimal amount of manual post-correction.“ (S. 387 (PDF 1), Kriterium 2)

> „In keeping with the widely used heuristic of ‚one sense per discourse‘, multiple occurrences of a target word in a given text are all assigned to the same GermaNet sense.“ (S. 390 (PDF 4))

> „The average precision for all three word classes is of sufficient quality to be used as-is if approximately 2-5% noise in the annotated data is acceptable.“ (S. 393 (PDF 7))

## Bezug zur Dissertation

- **Protokoll 2 (Gold gegenüber Silber):** WebCAGe ist ein Beispiel für eine automatisch erzeugte Annotation, deren Qualität nur teilweise gemessen ist: Geprüft sind Zielworterkennung und Heuristik, nicht die Senses gegen ein unabhängiges menschliches Urteil. Für die eigene Begrifflichkeit wäre WebCAGe nach Protokoll 2 Silber, nicht Gold. Das ist ein Vergleichsfall, um die Einstufung des MHDBDB-`@ana` als Silber zu begründen, ohne sie als Sonderfall erscheinen zu lassen.
- **Protokoll 2 und `knowledge/data.md` B1 (typbezogene Vorbelegung):** WebCAGe vergibt den Sense eines Textes an alle Vorkommen (S. 390 (PDF 4)); die gemessene Fehlerquote von 0,04 bis 4,4 % zeigt, dass eine solche Vorbelegung auch in Gegenwartstexten nicht fehlerfrei ist. Die MHDBDB-Typlisten sind eine verwandte, aber andere Vorbelegung (pro Wortform über das ganze Korpus, nicht pro Text); die Zahlen sind deshalb nicht direkt vergleichbar.
- **Protokoll 4.4, Punkt 4, und 9.1, Punkt 5 (Obergrenze pro Text, Bootstrap nach Text):** Die Messwerte zu „one sense per discourse“ (95,62 bis 99,96 %, S. 390 (PDF 4)) sind ein deutscher Beleg dafür, dass Tokens eines Lemmas im selben Text fast immer denselben Sense tragen; sie stützen Obergrenze und Cluster-Bootstrap. Vorbehalt: Wie geprüft wurde, ist nicht beschrieben.
- **Protokoll 6 und 9.2 (`MEHRERE`):** Mehrfach-Senses in WebCAGe sind ein Artefakt der Inventarzuordnung (Henrich 2015), kein Urteil einer Annotator:in, dass die Stelle unterbestimmt ist. Wer Henrichs Zahlen zu WebCAGe als Vergleich für `MEHRERE` heranzieht, vergleicht Verschiedenes. Das nächste Gegenstück im Protokoll ist Ausschluss 2 (Senses mit gleicher Begriffsgruppe, `knowledge/data.md` B7), nicht der Status `MEHRERE`.
- **Protokoll 9.2 (MFS-Baseline) und `knowledge/data.md` B9:** Senses ohne Wiktionary-Gegenstück erhalten keine Belege (S. 391 (PDF 5)), und die Projektseite nennt etwa 1 bis 3 Beispielsätze pro Sense; die Sense-Verteilung in WebCAGe ist also eine Folge der Ernte, nicht des Sprachgebrauchs. Henrich 2015 zieht daraus den Schluss, aus WebCAGe lasse sich keine MFS gewinnen (S. 143 (PDF 157)). Für das Protokoll ist das die Mahnung, die MFS nur aus Silber zu schätzen, dessen Belege Gebrauch abbilden, und zu berichten, wo das nicht gesichert ist (D1 gegenüber D0, Protokoll 3).
- **Protokoll 6 (`LEMMA_FALSCH`):** Selbst mit Lemmatisierer, Kompositazerlegung und Flexionstabellen bleibt die Zielworterkennung fehlerhaft, am stärksten bei Verben in älteren Texten (Gutenberg, Precision 69,87 %, S. 394 (PDF 8)). Für Mittelhochdeutsch mit Varianzschreibung ist eine eigene Kategorie für falsche Lemmazuweisung umso begründeter.
- **Protokoll 10 (Kontamination):** WebCAGe besteht aus Wiktionary- und Wikipedia-Text samt Sense-Labels über eine öffentliche Zuordnung; ein LLM-Vergleich auf solchen Daten wäre kaum gegen Trainingsdaten abzugrenzen. Das stützt die Entscheidung, die eigenen Labels nicht im Klartext zu veröffentlichen.

## Grenzen und Einwände

- **Keine Messung der Sense-Richtigkeit.** Tab. 3 misst, ob Zielwörter gefunden werden, nicht, ob der vergebene Sense stimmt. Die Richtigkeit hängt an der manuell korrigierten Zuordnung, an der Heuristik und daran, dass Wiktionary-Freiwillige Beispielsätze und Links dem richtigen Sense zugeordnet haben; letzteres prüft der Beitrag nicht.
- **„2 bis 5 % Rauschen“** gilt erkennbar nur für die drei Textsorten außer Gutenberg (Precision dort 87,43 %); der Text sagt das nicht ausdrücklich.
- **Verfügbarkeit:** Der Beitrag nennt WebCAGe „freely available“ (S. 388, 395 (PDF 2, 9)); laut Projektseite sind nur Wiktionary- und Wikipedia-Teil frei, Gutenberg-Texte noch nicht und externe Webseiten aus Lizenzgründen gar nicht.
- **Abweichungen zu anderen Angaben:** Dump-Datum 2. Februar 2011 im Beitrag (S. 388 (PDF 2)) und in Henrich 2015, 1. Februar 2011 auf der Projektseite. Im Text „Erk and Strapparava, 2012“ (S. 387, 393 (PDF 1, 7)), im Literaturverzeichnis 2010 (S. 395 (PDF 9)). Mehrfach-Senses fehlen im Beitrag ganz, sind aber in Version 3.0 laut Henrich 2015 7,2 % der Annotationen; ob die Fassung von 2012 sie schon enthielt, lässt sich aus dem Beitrag nicht sagen.
- **Übertragbarkeit:** Gegenwartsdeutsch, Wordnet-Inventar, Ernte über eine Webressource mit Beispielsätzen. Für Mittelhochdeutsch fehlt eine vergleichbare Ressource mit sense-verlinkten Beispielen; das Verfahren ist nicht übertragbar, nur seine Lehre über Qualitätskontrolle.
- **Lexical-Sample-Charakter:** im Mittel gut 4 Belege pro Lemma, durch die Ernte bestimmt; die Verteilung über Lemmata und Senses ist keine Stichprobe aus einem Korpus.

## Weiterführend

- Henrich, Hinrichs & Vodolazova 2011, *Semi-Automatic Extension of GermaNet with Sense Definitions from Wiktionary*, LTC'11, S. 126 bis 130 (zitiert S. 388 bis 389 (PDF 2 bis 3); Literatur S. 395 (PDF 9)): Primärquelle für die Zuordnung und die 93,8 %.
- Gale, Church & Yarowsky 1992, *One sense per discourse*: im Beitrag ohne Beleg genannt (S. 390 (PDF 4)), in Henrich 2015 als Gale et al. 1992b zitiert; auch in `Ide-Veronis-1998-WSD-State-of-the-Art.md` (dort 1992c).
- Raileanu, Buitelaar, Vintar & Bay 2002 und Broscheit et al. 2010 (Tab. 2, S. 393 (PDF 7); Literatur S. 395 bis 396): die manuellen deutschen Vergleichskorpora; schon in `Henrich-2015-WSD-GermaNet.md` geführt.
- Santamaría, Gonzalo & Verdejo 2003, *Automatic Association of Web Directories to Word Senses*, CL 29(3), S. 485 bis 502 (zitiert S. 394 (PDF 8)): verwandtes Ernteverfahren.
