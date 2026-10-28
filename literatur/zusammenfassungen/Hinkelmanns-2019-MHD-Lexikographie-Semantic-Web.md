# Hinkelmanns 2019: Mittelhochdeutsche Lexikographie und Semantic Web

**Datei:** `pdf/Hinkelmanns-2019-MHD-Lexikographie-Semantic-Web.pdf` (nur lokal; Verlags-PDF, 13 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, ganzes PDF gelesen (Text und Abbildung 1 am Seitenbild), DOI über doi.org und Crossref aufgelöst.

Seitenzählung: PDF-Seite n = gedruckte S. 128 + n (PDF 1 = S. 129, PDF 13 = S. 141).

## Bibliografie

- **Vollständig:** Hinkelmanns, Peter (2019). Mittelhochdeutsche Lexikographie und Semantic Web. Die Anbindung der ‚Mittelhochdeutschen Begriffsdatenbank' an Linked Open Data. *Das Mittelalter* 24(1), 129 bis 141.
- **DOI/URL:** https://doi.org/10.1515/mial-2019-0009 (aufgelöst; leitet auf De Gruyter Brill weiter, Verlagsseite selbst nicht abrufbar, HTTP 405). Crossref: Druck 11.07.2019, online 09.08.2019, Walter de Gruyter. Kopf S. 129: „Das Mittelalter 2019; 24(1): 129–141". ✔ (PDF und Crossref).
- **Art:** begutachteter Artikel (Zeitschrift); Themenheft „Digitale Mediävistik" laut Literaturangabe in Hinkelmanns & Zeppezauer-Wachauer 2023, S. 180 (○, Sekundärangabe)
- **Sprache:** Deutsch (Abstract Englisch)

## Worum es geht

Der Beitrag ist eine Bestandsaufnahme zu Formaten und Ontologien für Online-Wörterbücher mit Blick auf die mittelhochdeutsche Lexikographie (Abstract, S. 129). Er stellt TEI (Dictionaries), LMF, OntoLex-Lemon und Wikidata vor (S. 133 bis 135) und skizziert, wie die MHDBDB im Relaunch nach TEI und OntoLex mit Lemon-tree überführt werden soll (S. 135 bis 138). Dazu kommen Normdaten (S. 138 bis 140) und die REST-API von ZHistLex (S. 140 bis 141). Eigene empirische Ergebnisse gibt es keine.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Die MHDBDB wurde von Klaus M. Schmidt begründet, Anfänge auf Lochkarten in den frühen 1970ern, online seit 1995; die Software-Architektur mit proprietärem relationalem Datenmodell habe sich seither nicht wesentlich verändert. | S. 130 (PDF 2) | Projektbeschreibung |
| Abstract: die letzte technologische Überarbeitung datiere von 1992. (Widerspricht dem Fließtext, der 1995 nennt, und Zeppezauer-Wachauer 2022, S. 165, die 1998 ORACLE nennt.) | S. 129 (PDF 1) | Projektbeschreibung, uneinheitlich |
| MWB arbeitet semasiologisch, MHDBDB onomasiologisch; in der MHDBDB sucht man nach Begriffen (Beispiel ‚Imkerei'). Beide sind korpusbasiert und verknüpfen Wortartikel mit Editionstexten. | S. 131 (PDF 3) | Projektbeschreibung |
| Im Relaunch werden die Texte nach TEI-P5 konvertiert; jeder durch Spatien oder Satzzeichen getrennte String ist ein Token mit eindeutiger ID; Tokens und Mehrtoken-Einheiten (etwa getrennte Verbformen) werden „einem Wörterbuchartikel und der entsprechenden Bedeutung im Kontext zugeordnet". | S. 135 (PDF 7) | Plan für den Relaunch |
| Die normalisierte Grundform jedes Wortartikels richtet sich nach der Lemmaliste des MWB. | S. 135 bis 136 (PDF 7 bis 8) | Projektbeschreibung |
| Kernelemente eines MHDBDB-Artikels sind die Bedeutungsangaben, die sich aus Verweisen auf die Begriffsontologie zusammensetzen. | S. 136 (PDF 8) | Projektbeschreibung |
| Das Begriffssystem basiert auf dem Entwurf von Hallig und von Wartburg und vereint „zum gegenwärtigen Zeitpunkt" unterschiedliche Informationsebenen; Schmidt wandte es auf den Wortschatz des ‚Frauendienst' an; der Zusammenschluss mit Pütz' Namensprojekt schuf ein komplexes Werkzeug. | S. 136 bis 137 (PDF 8 bis 9) | Projektbeschreibung |
| Die Daten lassen sich mit OntoLex und der onomasiologischen Erweiterung Lemon-tree darstellen; Verweise zwischen Wortartikeln und Wörterbuch werden mit dem Web Annotation Vocabulary realisiert. | S. 137 (PDF 9) | Plan |
| Beispiel (Abb. 1): Zwei Tokens (*hunde*, *katzen* als Tiere) verweisen über ihre Senses auf dasselbe Konzept ‚Haustier(e)'; ein drittes Token *katzen* (Kriegsgerät) verweist auf denselben Wortartikel *katze*, aber auf Sense 2 ‚Kriegsmaschine'. Die Bedeutungszuordnung ist also im Modell pro Token. | S. 136 bis 137 (PDF 8 bis 9) | Modellbeispiel |
| Bei der Konversion sei mit „semantischen Unschärfen" umzugehen; generalisierte Modelle setzen konkrete Anwendungsfälle voraus; die MHDBDB-Daten ließen sich dennoch „sehr gut" in OntoLex abbilden. | S. 138 (PDF 10) | Einschätzung des Autors |
| Ziel ist, „bereits erarbeitete hermeneutische – also implizite/interpretative – Informationen" so zu systematisieren, dass sie in eine strukturelle Modellierung aufgenommen werden können. | S. 138 (PDF 10) | Programmatik |
| Normdaten (GND, LoC, Wikidata, VIAF) ergänzen und widersprechen einander, am Beispiel der Lebensdaten Walthers von der Vogelweide; Metadaten zu Personen, Orten, Werken verbessern Filtermöglichkeiten. | S. 138 bis 139 (PDF 10 bis 11) | Bestandsaufnahme |
| Fazit: Die mhd. Lexikographie ist weitgehend frei online, aber nur für direkte Abfrage; maschineller Zugriff über LOD oder Schnittstellen fehlt noch. | S. 141 (PDF 13) | Fazit |

## Daten, Methode, Zahlen

- Keine Korpus- oder Annotationszahlen. Zeitangaben: MHDBDB online seit 1995 (S. 130); MWB seit 1986, Print 2006, online 2007 (S. 130); MWV-Digitalisierung 1997 bis 2000 (S. 130); Relaunch geplant bis 2020 (S. 135, 137).
- Abb. 1 (S. 136): drei Belegstellen (Neidhart, ‚Renner', ‚Trojanerkrieg'), `ontolex:word` Hunt und Katze, `ontolex:LexicalSense` Hunt 1, Katze 1, Katze 2, `skos:Concept` Haustier und Kriegsmaschine. Pfeile von den Belegstellen zu den Senses zeigen die Bedeutung im Kontext.
- Codebeispiel OntoLex/Lemon-tree für *katze* mit `tree:isSenseInConcept` (S. 137 bis 138).

## Wörtliche Stellen

> „Die Tokens eines Textes und Einheiten, die aus mehreren Tokens bestehen – etwa getrennte Verbformen –, werden einem Wörterbuchartikel und der entsprechenden Bedeutung im Kontext zugeordnet." (S. 135)

> „Kernelemente eines Artikels der MHDBDB sind die Bedeutungsangaben, die sich aus Verweisen auf die Begriffsontologie der MHDBDB zusammensetzen." (S. 136)

> „Insbesondere wird darauf abgezielt, bereits erarbeitete hermeneutische – also implizite/interpretative – Informationen so zu systematisieren, dass sie in eine strukturelle Modellierung aufgenommen werden können." (S. 138)

(Die Striche in den Zitaten sind im Original Halbgeviertstriche.)

## Bezug zur Dissertation

- **PROTOKOLL §2, Begriff „Inventar":** S. 136 stützt die Definition, dass ein Sense durch seine Begriffszeiger bestimmt ist („Bedeutungsangaben, die sich aus Verweisen auf die Begriffsontologie … zusammensetzen").
- **PROTOKOLL §2, Silber:** Der Beitrag beschreibt das **Zielmodell** des Relaunchs (Bedeutung pro Token, S. 135, 137), nicht, wie die vorhandenen Bedeutungsannotationen entstanden sind. Wer, wann und nach welchen Richtlinien annotiert hat, steht nirgends. Er stützt also weder Gold noch die Typ-Lesart; die Lücke in §2 bleibt.
- **Typ-Lesart (§2, A12; `knowledge/data.md` B1 und Abschnitt 3):** Graphematische Types kommen in diesem Beitrag nicht vor. Kein Widerspruch zur Lesart, keine Stütze.
- **PROTOKOLL §5 und `knowledge/data.md` B11:** Begriffssystem auf Hallig-Wartburg-Basis, mit „unterschiedlichen Informationsebenen" (S. 136). Welche Ebenen, sagt der Beitrag nicht; Zeppezauer-Wachauer 2022, S. 172, nennt Funktionswörter, Fremdsprachen und Namen.
- **PROTOKOLL §1 Nebenfrage (Inventarlücken):** Die „semantischen Unschärfen" bei der Konversion (S. 138) sind ein Hinweis, dass das Modell nicht alles fasst; konkret wird das nicht.

## Grenzen und Einwände

- Programmatischer Überblick; das MHDBDB-Beispiel ist ausdrücklich vereinfacht (S. 137).
- Zeitangaben zur Technik sind inkonsistent (Abstract 1992, Text 1995; vgl. Zeppezauer-Wachauer 2022: ORACLE ab 1998).
- Hallig & Wartburg wird mit „Berlin 1952" zitiert (S. 136, Anm. 45); Zeppezauer-Wachauer 2022 und Tittel et al. 2020 zitieren die 2. Auflage 1963.

## Weiterführend

- Tittel & Chiarcos 2018 (DEAF nach OntoLex), hier zitiert als Globalex-Workshop 2018, S. 57 bis 65 (S. 135, Anm. 38). Die Seitenangabe weicht von `references.txt` (58 bis 66) und von Tittel et al. 2020 (58 bis 66) ab.
- McCrae et al. 2012, Interchanging lexical resources on the Semantic Web, *LRE* 46, 701 bis 719 (S. 133, Anm. 24).
- Cimiano, McCrae & Buitelaar 2016, OntoLex-Lemon Community Report (S. 134, Anm. 36).
- Stolk, Lemon-tree (S. 137, Anm. 47).
- Hallig & von Wartburg, Begriffssystem als Grundlage für die Lexikographie (S. 136, Anm. 45).
- Fournier 2001, New Directions in Middle High German Lexicography, *LLC* 16 (S. 131, Anm. 9).

## Julias Markierungen im PDF

55 Hervorhebungen, ein Randzeichen, keine Notizen (`md/Hinkelmanns-2019-MHD-Lexikographie-Semantic-Web.markierungen.md`). Aufgenommen: Gründung und Online-Datum, proprietäres relationales Datenmodell (S. 130); semasiologisch gegen onomasiologisch, korpusbasiert, Verknüpfung mit Editionstexten (S. 131); Relaunch bis 2020, Tokens mit Bedeutung im Kontext (S. 135, mit Randzeichen); MWB-Lemmaliste, Hallig-Wartburg und Schmidt/Pütz (S. 136 bis 137); *katze*-Beispiel (S. 137); Fazit (S. 141). Nur knapp oder gar nicht aufgenommen, weil für die Dissertation Hintergrund: Wandel zur lexikographischen Datenbank und Spohr, Fuertes Olivera & Tarp (S. 129); Verbund der Wörterbücher, Normdaten, Standards (S. 130); MWB-Daten (S. 130); ZHistLex, ENeL, Europäisches Wörterbuchportal, elexis (S. 132); Formatvielfalt nach McCrae, TEI und Semantic Web, Ciotti & Tomasi, Eide (S. 133); lemon als W3C-Report (S. 134); Metadaten und Normdaten (S. 139).
