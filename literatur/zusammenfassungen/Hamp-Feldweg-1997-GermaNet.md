# Hamp & Feldweg 1997: GermaNet, ein lexikalisch-semantisches Netz für das Deutsche

**Datei:** `pdf/Hamp-Feldweg-1997-GermaNet.pdf` (nur lokal; 7 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Titelseite am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-13). Es ist ein Scan mit OCR-Textebene; die Textebene enthält OCR-Fehler (z. B. „fiir“, „Tiibingen“, „finanzzell“), Zitate unten sind am Sinn und, wo nötig, am Seitenbild geprüft. Die Abbildungen 1 bis 7 (Baumdiagramme) sind in der Textebene nur bruchstückhaft und hier nicht ausgewertet. Keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 8 + n (PDF 1 = S. 9, PDF 7 = S. 15). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Hamp, Birgit & Helmut Feldweg (1997). GermaNet – a Lexical-Semantic Net for German. In: *Automatic Information Extraction and Building of Lexical Semantic Resources for NLP Applications* (ACL-Workshop), Madrid, S. 9 bis 15.
- **DOI/URL:** keine DOI; https://aclanthology.org/W97-0802/ (Anthology: Booktitle wie oben, Jahr 1997, ohne Seiten, Ort und Herausgeber:innen; abgerufen 2026-11-13). Ort Madrid und Workshop-Bezeichnung „Proceedings of the ACL workshop …“ nach der Seite „Citing GermaNet“ der Universität Tübingen (https://uni-tuebingen.de/en/142823, abgerufen 2026-11-13, dort ohne Seiten). Seiten 9 bis 15 sind die gedruckten Seitenzahlen im PDF.
- **Titel:** Im Seitenbild steht zwischen „GermaNet“ und „a“ ein Halbgeviertstrich (S. 9); Anthology und Tübinger Seite schreiben einen Bindestrich.
- **Lizenz:** CC BY-NC-SA 3.0 (ACL Anthology, Material vor 2016, laut Fußzeile der Anthology, abgerufen 2026-11-13).
- **Art:** Workshopbeitrag
- **Sprache:** Englisch
- **Zitierpflicht:** Die Tübinger Seite verlangt für die Ressource GermaNet dieses Werk zusammen mit Henrich & Hinrichs 2010 (siehe Zusammenfassung `Henrich-Hinrichs-2010-GernEdiT.md`).

## Worum es geht

Die Autor:innen stellen GermaNet vor, ein Wortnetz für das Deutsche, das im Format mit dem Princeton WordNet kompatibel ist, aber „from scratch“ gebaut wird, nicht übersetzt (S. 9). Sie beschreiben Umfang, Relationen und die Bauprinzipien, in denen GermaNet von WordNet abweicht: systematisch markierte künstliche Konzepte, Kreuzklassifikation, ein eigener Zeiger für reguläre Polysemie, taxonomische Adjektive, Partikelverben mit kompositioneller Deutung (S. 11 bis 14). Eine Evaluation oder Annotation enthält das Werk nicht. Für die Dissertation wichtig ist die Haltung zur Granularität: Polysemie wird bewusst knapp gehalten (S. 10).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| GermaNet enthält derzeit „some 16.000 words“ und soll mindestens den Grundwortschatz modellieren; Bedeutungen (Synsets) werden nach semantischer Verwandtschaft gruppiert. | S. 9, Abschn. 1 | Projektangabe |
| Grundgerüst wie WordNet, aber „built from scratch“: weder Übersetzung des englischen WordNet noch auf ein einzelnes Wörterbuch gestützt. | S. 9, Abschn. 1 | Projektangabe |
| Für das Deutsche fehlen große Ressourcen; der Bau stützt sich daher weitgehend auf Handarbeit mit ein- und fachsprachlichen Wörterbüchern und Vergleich mit WordNet, der Grundwortschatz aber korpusbasiert über lemmatisierte Frequenzlisten (Korpus von 60 Mio. Wörtern, Fn. 1), abgeglichen mit CELEX. Clustering habe sich für den Kern des Netzes nicht bewährt. | S. 9 bis 10, Abschn. 2, Fn. 1 | eigenes Verfahren |
| Vier Wortarten wie WordNet; Adverbien in der aktuellen Phase nicht umgesetzt. Pro Wortart etwa 15 semantische Felder, vor allem zur Arbeitsteilung; sie müssen nicht mit der Top-Ontologie übereinstimmen. | S. 10, Abschn. 3.1 | eigenes Verfahren |
| Nur Lemmata; Flexionsformen soll eine externe Morphologie auf Grundformen abbilden. Eigennamen und Abkürzungen in der Regel nicht aufgenommen. | S. 10, Abschn. 3.1 | eigene Festlegung |
| **Granularität:** „The amount of polysemy is kept to a minimum“; ein weiterer Sense wird nur eingeführt, wenn er mit den Koordinaten der anderen Senses im Netz in Konflikt steht; im Zweifel gilt der Polysemiegrad der gängigen einsprachigen Druckwörterbücher. | S. 10, Abschn. 3.1 | eigene Festlegung |
| Lexikalische Relationen (Synonymie, Antonymie) gelten zwischen Wörtern, konzeptuelle (Hyponymie, Meronymie u. a.) zwischen Konzepten. Nur eine Meronymie-Relation statt drei in WordNet. | S. 10, Abschn. 3.2 | eigenes Modell |
| „Pertains to“ ist semantisch, nicht morphologisch: *konventionell* gehört zu *Konvention* (Umgangsregel), *konventional* zu *Konvention* (Vertrag). | S. 10, Abschn. 3.2 | eigenes Modell |
| Verben: WordNets Entailment wird geteilt in eine Teilereignis-Relation (*schnarchen*/*schlafen*) und Entailment im Sinne der Rückwärts-Präsupposition (*gelingen*/*versuchen*); Kausation auch zu Adjektiven (*öffnen*/*offen*). | S. 11, Abschn. 3.2 | eigenes Modell, teils nach EuroWordNet (Alonge 1996) |
| Selektionsrestriktionen sollen automatisch erzeugt werden, sobald ein mit GermaNet-Klassen sense-annotiertes Korpus vorliegt; Beispiele pro Konzept sollen automatisch aus dem Korpus kommen. | S. 11, Abschn. 3.2 | Vorhaben |
| **Künstliche Konzepte** (nicht lexikalisiert) werden systematisch eingesetzt und markiert, damit man sie in der Oberfläche ausblenden kann; zwei Sorten: lexikalische Lücken und eigentliche künstliche Konzepte. Zweck: unmotivierte Ko-Hyponyme vermeiden, Daten systematisch strukturieren. | S. 11 bis 12, Abschn. 4.1, Abb. 1 bis 3 | eigenes Prinzip |
| **Kreuzklassifikation** ist Pflicht, wo zwei Hierarchien konkurrieren (Volks- und Fachtaxonomie: Katze als Wirbeltier und Haustier); bei Verben haben die meisten Konzepte mehrere Bedeutungskomponenten. | S. 12, Abschn. 4.2, Abb. 4 | eigenes Prinzip |
| **Reguläre Polysemie** (Organisation/Gebäude, Tier/Fleisch): reines Aufzählen von Senses reiche nicht; ein Zusammenlegen zu einem Konzept scheitert, weil Synonyme und Unterbegriffe die Polysemie selten teilen. Lösung: ein bidirektionaler Zeiger an den obersten betroffenen Konzepten. Häufige Fälle werden trotzdem als getrennte Konzepte kodiert; der Zeiger erlaubt, seltene Lesarten (*crocodile* als Fleisch) zu erschließen, ohne sie einzutragen. | S. 12 bis 13, Abschn. 5.1, Abb. 5 und 6 | eigenes Modell; Pustejovsky 1996 referiert |
| Adjektive taxonomisch über Hyponymie statt WordNets Satellitenmodell; Klassen nach Hundsnurscher & Splett 1982. | S. 13 bis 14, Abschn. 5.2 | eigenes Modell |
| Verben: syntaktische Rahmen pro Sense (nicht pro Lemma), nach CELEX; Partikelverben gemischt: unregelmäßige aufgezählt, regelmäßige kompositionell über ein hierarchisches Partikellexikon (*herauslaufen* als Hyponym von *laufen* und *heraus-*). | S. 14, Abschn. 5.3, Abb. 7 | eigenes Modell |

## Daten, Methode, Zahlen

- Umfang: „some 16.000 words“ (S. 9).
- Korpus für die Frequenzlisten: 60.000.000 Wörter, getaggt und lemmatisiert (ECI-Korpus 1994 mit *Frankfurter Rundschau*, *Donau-Kurier*, *VDI Nachrichten*; Tübinger NewsKorpus aus Newsgroups) (S. 10, Fn. 1; Zeitungsnamen am Seitenbild gelesen, in der OCR verstümmelt).
- Etwa 15 semantische Felder pro Wortart (S. 10).
- Keine Annotation, keine Übereinstimmungswerte, keine Evaluation.

## Wörtliche Stellen

> „The amount of polysemy is kept to a minimum in Germanet, an additional sense of a word is only introduced if it conflicts with the coordinates of other senses of the word in the network.“ (S. 10)

> „When in doubt, GermaNet refers to the degree of polysemy given in standard monolingual print dictionaries.“ (S. 10)

> „GermaNet is built from scratch, which means that it is neither a translation of the English WordNet nor is it based on a single dictionary or thesaurus.“ (S. 9)

## Bezug zur Dissertation

- **Vergleich der Inventare (Protokoll §2, §5; `knowledge/data.md`, Abschnitt 1):** GermaNet ist semasiologisch und onomasiologisch zugleich: Wörter hängen an Synsets, die in einer Hierarchie stehen. Ein GermaNet-Sense ist ein Platz im Netz; ein MHDBDB-Sense ist eine Menge von Begriffszeigern auf ein Begriffssystem ohne Definition. Gemeinsam ist beiden, dass die Bedeutung über die Stellung in einer Begriffshierarchie bestimmt wird, nicht über eine Glosse. Damit ist GermaNet der nächste moderne Vergleichspunkt für das MHDBDB-Inventar, näher als ein Wörterbuch.
- **Granularität:** GermaNet legt eine explizite Regel fest, wann ein neuer Sense entsteht: nur bei Konflikt mit der Stellung der anderen Senses im Netz (S. 10). Für die MHDBDB ist eine solche Regel nicht dokumentiert; dort können zwei Senses eines Lemmas sogar dieselbe Begriffsgruppe haben (22 Lemmata, Ausschluss 2; `knowledge/data.md` B7) oder Teilmengen voneinander sein (Protokoll §5, Punkt 2: 4,6 % der Sense-Paare). Das Werk liefert damit einen Maßstab, an dem sich die Granularität des MHDBDB-Inventars beschreiben lässt, belegt aber nichts über die MHDBDB.
- **Homonymie und Polysemie (B15):** GermaNet trennt sie nicht durch eigene Einträge, behandelt aber **reguläre** Polysemie eigens (S. 12 bis 13). Für die Frage in `knowledge/data.md` §4, Punkt 6 (Menü pro Lemma mischt Homonymie und Polysemie) bietet das Werk keine Lösung, nur die Unterscheidung „reguläre Polysemie“ als weitere Kategorie, die eine Fehleranalyse von `MEHRERE` mitführen könnte (Tier/Fleisch-artige Fälle sind typische Kandidaten für „mehrere passen“).
- **Polyhierarchie (`knowledge/data.md` B11):** GermaNet erzwingt Kreuzklassifikation bewusst (S. 12). Auch das MHDBDB-Begriffssystem ist polyhierarchisch (43 Begriffe mit mehreren Oberbegriffen). Für die grobe Auswertungsebene (Protokoll §9.1, Punkt 7; §12, Punkt 12) heißt das: Eine Abbildung auf „den“ Oberbegriff ist in beiden Systemen nur über eine zusätzliche Festlegung eindeutig (in der MHDBDB über den Zahlencode, B11).
- **Zitierpflicht:** Wird in der Dissertation GermaNet als Ressource genannt (etwa über Henrich 2015 als Vergleich eines deutschen WSD-Goldstandards), ist dieses Werk zusammen mit Henrich & Hinrichs 2010 zu zitieren.
- **LLM-Prüfung, Kontamination (A17 bis A29):** nicht berührt.

## Grenzen und Einwände

- Projektbeschreibung ohne Evaluation; keine Angaben zur Zuverlässigkeit der Sense-Unterscheidungen.
- Stand 1997 mit etwa 16.000 Wörtern; spätere GermaNet-Versionen weichen in Umfang und Teilen des Modells ab (nicht aus diesem Werk belegbar, daher hier nicht ausgeführt).
- Gegenwartsdeutsch, Zeitungs- und Newsgroup-Korpus; zum Mittelhochdeutschen nichts.
- OCR-Textebene mit Fehlern; Abbildungen nur am Seitenbild lesbar.

## Weiterführend

- Henrich & Hinrichs 2010 (GernEdiT): liegt vor, zweites Pflichtzitat für GermaNet.
- Henrich 2015 (WSD mit GermaNet): liegt vor.
- Pustejovsky 1996, *The Generative Lexicon* (S. 12, 15): zur regulären Polysemie.
- Hundsnurscher & Splett 1982, *Semantik der Adjektive des Deutschen* (S. 14, 15).
- Miller et al. 1993, *Five Papers on WordNet* (S. 9, 15).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF und hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
