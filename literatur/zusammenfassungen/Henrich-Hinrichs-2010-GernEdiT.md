# Henrich & Hinrichs 2010: GernEdiT. The GermaNet Editing Tool

**Datei:** `pdf/Henrich-Hinrichs-2010-GernEdiT.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, PDF vollständig gelesen (8 Seiten, Textebene; Abb. 2 am Seitenbild geprüft); bibliografische Angaben an ACL Anthology und an der Zitierseite von GermaNet bestätigt. Priorität 3 (Hintergrund), daher knapp.

**Seitenzählung:** gedruckt S. 2228 bis 2235 = PDF-Seite 1 bis 8 (Seitenzahl unten auf der Seite, keine Seitenlabels); PDF-Seite = gedruckte Seite − 2227. Zitiert wird die gedruckte Seite, die PDF-Seite steht in Klammern.

**Wofür zitieren:** Das Paper beschreibt das Editierwerkzeug, nicht GermaNet als Ressource. Die Universität Tübingen verlangt aber für GermaNet selbst ausdrücklich zwei Zitate: Hamp & Feldweg 1997 und dieses Paper (Seite „Citing GermaNet“, https://uni-tuebingen.de/en/142823, abgerufen am 2026-10-29). Wird GermaNet in der Dissertation genannt, gehören beide dazu; dieses Paper allein ist für inhaltliche Aussagen über GermaNet zu schmal. Henrich 2015 zitiert GermaNet mit Hamp & Feldweg 1997 und GernEdiT mit diesem Paper (siehe dortige Zusammenfassung bzw. `md/Henrich-2015-WSD-GermaNet.md`, Literaturverzeichnis).

## Bibliografie

- **Vollständig:** Henrich, Verena & Erhard Hinrichs, 2010. GernEdiT: The GermaNet Editing Tool. In: Nicoletta Calzolari, Khalid Choukri, Bente Maegaard, Joseph Mariani, Jan Odijk, Stelios Piperidis, Mike Rosner & Daniel Tapias (Hg.), *Proceedings of the Seventh International Conference on Language Resources and Evaluation (LREC'10)*, Valletta, Malta, Mai 2010. European Language Resources Association (ELRA), S. 2228 bis 2235. Im Originaltitel steht ein Halbgeviertstrich: `GernEdiT – The GermaNet Editing Tool`.
- **DOI/URL:** keine DOI. https://aclanthology.org/L10-1180/ (am 2026-10-29 abgerufen: Titel, Autoren, Herausgeber:innen, Mai 2010, Valletta, ELRA; PDF auf http://www.lrec-conf.org/proceedings/lrec2010/pdf/264_Paper.pdf). Seiten aus dem PDF. ✔
- **Art:** begutachteter Konferenzbeitrag (LREC)
- **Sprache:** Englisch

## Worum es geht

Das Paper stellt GernEdiT vor, eine grafische Oberfläche (Java Swing) für die Lexikograf:innen von GermaNet, dem deutschen Wordnet nach dem Vorbild des Princeton WordNet (S. 2228, S. 2230 (PDF 1, 3)). Bis dahin wurde GermaNet in Textdateien („lexicographer files“) gepflegt; das war fehleranfällig, ohne Konsistenzprüfung und ohne Versionierung (S. 2229 bis 2230 (PDF 2 bis 3)). GernEdiT speichert die Daten in einer relationalen Datenbank (PostgreSQL), prüft Konsistenz beim Editieren, führt eine Änderungshistorie und exportiert XML (S. 2230 bis 2233 (PDF 3 bis 6)). Die Bewertung beruht auf positiver Rückmeldung der Lexikograf:innen, nicht auf Messungen (S. 2233 (PDF 6)).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| GermaNet teilt den lexikalischen Raum in Konzepte, die durch semantische Relationen verbunden sind; ein Konzept ist ein Synset, also eine Menge lexikalischer Einheiten mit (fast) gleicher Bedeutung, dazu eine Paraphrase. Die Liste der lexikalischen Einheiten ist nie leer, alle anderen Eigenschaften dürfen fehlen. | S. 2228 (PDF 1), Abschn. 2 | Beschreibung der Ressource |
| Zwei Relationstypen: konzeptuelle zwischen Synsets (Hyperonymie, Teil-Ganzes, Entailment, Kausation) und lexikalische zwischen Einheiten (Antonymie). | S. 2229 (PDF 2), Abschn. 2 | Beschreibung |
| GermaNet umfasst Adjektive, Nomen und Verben, je hierarchisch nach Hyperonymie geordnet; der semantische Raum jeder Wortart ist in semantische Felder geteilt. | S. 2229 (PDF 2), Abschn. 2 | Beschreibung |
| „Künstliche Konzepte“ füllen Hierarchielücken, die sich im Deutschen nicht durch ein einfaches Wort lexikalisieren lassen (Beispiel *festes_Nahrungsmittel*). | S. 2229 (PDF 2), Abschn. 3 | Beschreibung |
| Mit wachsender Abdeckung wurde es schwerer, den richtigen Ort für neue Einträge zu finden; das Format erzwang keinen Zusammenhang der Hierarchie, die Daten litten an internen Inkonsistenzen; ohne Versionierung durfte nur eine Person eine Datei bearbeiten. | S. 2230 (PDF 3), Abschn. 4 | eigene Darstellung |
| GernEdiT verhindert Eingaben, die den Zusammenhang des Graphen verletzen, verlangt zu jeder Einheit einen Synset und löscht abhängige Daten mit. | S. 2231 bis 2232 (PDF 4 bis 5), Abschn. 5.1 | eigene Darstellung |
| Die Änderungshistorie zeigt, wer was geändert hat und wie der Eintrag vorher aussah; paralleles Arbeiten mehrerer Lexikograf:innen wird möglich. | S. 2230 (PDF 3); S. 2233 (PDF 6), Abschn. 6 | eigene Darstellung |
| Die Lexikograf:innen gaben sehr positive Rückmeldung; Bewertung „effizienter und genauer“ ohne Zahlen. | S. 2233 (PDF 6), Abschn. 6; S. 2234 (PDF 7), Abschn. 7 | eigene Bewertung, nicht gemessen |

## Daten, Methode, Zahlen

- GermaNet 5.2 (Dezember 2009): 61.575 Synsets, 84.859 lexikalische Einheiten, 76.981 Literale, 1,38 Einheiten pro Synset, 1,10 Lesarten pro Literal, 26.564 lexikalische und 73.624 konzeptuelle Relationen (S. 2229 (PDF 2)). Entwicklung seit 1997.
- Datenmodell (Anhang, S. 2234 bis 2235 (PDF 7 bis 8)): Tabellen für Synsets (mit Wortklasse als semantischem Feld, Wortart, Paraphrase, Kommentar), lexikalische Einheiten (mit Orthografie vor und nach der Reform, Eigenname, künstlich, stilistisch markiert), Beispiele, Valenzrahmen, lexikalische und konzeptuelle Relationen.
- Abb. 2 (S. 2231 (PDF 4), am Seitenbild geprüft): Suche nach *Nuss* liefert drei Synsets in drei semantischen Feldern (Artefakt, Nahrung, Pflanze); nur der Synset im Feld Nahrung trägt eine Paraphrase („der essbare Kern einer Nuss“).
- Keine Evaluation mit Zahlen.

## Bezug zur Dissertation

- **Protokoll 2 und 5 (Inventar):** GermaNet ordnet Synsets semantischen Feldern pro Wortart zu (S. 2229; Abb. 2: *Nuss* in Artefakt, Nahrung, Pflanze). Das ist die nächste Entsprechung zum MHDBDB-Begriffssystem in einem deutschen WSD-Inventar: Die Polysemie von *Nuss* ist hier auch über die Feldzugehörigkeit unterscheidbar. Der Unterschied bleibt, dass ein MHDBDB-Sense mehrere Begriffe zugleich tragen kann (`knowledge/data.md`, Abschnitt 1), ein GermaNet-Synset dagegen genau einem Feld angehört (Datenmodell S. 2235). Für den Inventarvergleich in der Arbeit ein konkretes, zitierbares Beispiel.
- **Protokoll 5 (Darstellung ohne Glossen):** In Abb. 2 hat nur einer von drei Synsets eine Paraphrase; die Paraphrase ist optional (S. 2228). Henrich 2015 hat deshalb Wiktionary-Definitionen zugeordnet (siehe dortige Zusammenfassung). Die MHDBDB-Lage ist ähnlich (`knowledge/data.md` B13); das Paper belegt, dass auch ein großes deutsches Inventar ohne durchgehende Glossen gebaut wurde.
- **`knowledge/data.md` B4 und Abschnitt 3 (Inventar vor der Migration, Herkunft unbekannt):** GernEdiT führt eine Änderungshistorie mit Person und Vorzustand (S. 2230). Das MHDBDB-Inventar hat vor 2025-07 keine solche Spur. Als Kontrast für das Datasheet: Was sich bei GermaNet rekonstruieren ließe, ist für die MHDBDB nicht rekonstruierbar.
- **Protokoll 8 (Nachvollziehbarkeit):** Die Grundsätze (wer, wann, was vorher, keine Eingabe ohne Pflichtfeld) entsprechen den Anforderungen an die Annotationsoberfläche. Nur als Parallele, nicht als Beleg: Das Paper beschreibt Lexikografie, keine Annotation.

## Grenzen und Einwände

- Werkzeugbeschreibung ohne gemessene Evaluation; „effizienter und genauer“ (S. 2233 bis 2234) ist eine Einschätzung der Entwickler:innen und Nutzer:innen.
- Über GermaNet als WSD-Inventar (Granularität, Abdeckung, Übereinstimmung) sagt das Paper nichts; dafür ist Henrich 2015 die Quelle.
- Kleine Unstimmigkeit im Anhang: `word_class_id` und `word_category_id` werden beide als „the word class of this synset“ beschrieben (S. 2235); gemeint ist bei Letzterem die Wortart (adj, nomen, verben), wie S. 2230 zeigt.

## Weiterführend

- Hamp & Feldweg 1997, GermaNet: a Lexical-Semantic Net for German (von der GermaNet-Zitierseite gefordert; in diesem Paper nicht zitiert, in Henrich 2015 schon).
- Kunze & Lemnitzer 2002, GermaNet: representation, visualization, application, LREC 2002 (S. 2228, Lit.).
- Henrich 2015, Dissertation; eigene Zusammenfassung vorhanden.
