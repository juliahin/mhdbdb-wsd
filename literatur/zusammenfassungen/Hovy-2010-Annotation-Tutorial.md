# Hovy 2010: Annotation (Tutorial-Abstract)

**Datei:** `pdf/Hovy-2010-Annotation-Tutorial.pdf` (nur lokal; 1 Seite)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology P10-5004 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

**Wichtig: Das PDF ist nur das einseitige Abstract des Tutorials im Band „Tutorial Abstracts“, nicht die Folien und nicht die im Abstract erwähnten Tutorial-Notizen.** Zusammengefasst ist nur, was auf dieser Seite steht. Inhaltliche Aussagen des Tutorials selbst (Verfahren, Zahlen, Empfehlungen) lassen sich mit diesem PDF nicht belegen.

Seitenzählung: eine Seite, gedruckt S. 4.

## Bibliografie

- **Vollständig:** Hovy, Eduard (2010). Annotation. In: Lluís Màrquez & Haifeng Wang (Hg.), *Proceedings of the 48th Annual Meeting of the Association for Computational Linguistics: Tutorial Abstracts*. Uppsala: Association for Computational Linguistics, S. 4. Tutorial am 11. Juli 2010 (Kopfzeile des PDF).
- **DOI/URL:** keine DOI gefunden (Anthology-BibTeX ohne DOI); https://aclanthology.org/P10-5004/ (Herausgeber, Ort, Monat Juli und Seite 4 nach dem BibTeX der Anthology, abgerufen 2026-11-16).
- **Lizenz:** CC BY-NC-SA 3.0 (ACL Anthology, Werke vor 2016, abgerufen 2026-11-16).
- **Art:** Tutorial-Abstract (nicht begutachteter Volltext)
- **Sprache:** Englisch

## Worum es geht

Das Abstract kündigt ein Tutorial über Korpusannotation an. Es stellt fest, dass es kein allgemeines Paradigma, kein umfassendes Lehrbuch und keine anerkannten Standards gebe und Annotationsprojekte deshalb „something of an art“ blieben (S. 4). Das Tutorial soll Abläufe, Probleme und Fallstricke behandeln, verfügbare Ressourcen nennen und sieben offene Fragen der Annotation besprechen, für die es noch keine befriedigenden Standardantworten gebe (S. 4).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Korpusannotation wird für NLP wichtiger, es gibt aber kein allgemeines Paradigma, kein Lehrbuch, das alle Fragen abdeckt (Wilcock 2009 behandle einige Grundfragen), und keine anerkannten Standards. | S. 4, Abschnitt 1 | Einschätzung des Autors |
| Annotation wird in die Methodik „train-evaluate-apply“ eingeordnet; genannt werden Ressourcen und Dienste wie das QDAP annotation center, Amazon Mechanical Turk, GATE und UIMA. | S. 4, Abschnitt 2 | Ankündigung |
| Sieben offene Fragen: (1) welche Phänomene annotieren und wie die Theorie in einfache Anweisungen bringen; (2) wie ein ausgewogenes, repräsentatives Korpus gewinnen; (3) welche Eigenschaften Annotierende brauchen und wie sie angemessen, „but not over- or under-“, schulen; (4) wie ein einfaches, schnelles, vertrauenswürdiges Verfahren aufsetzen und wann Maßnahmen ergreifen, damit es auf Kurs bleibt, und wo aktives Lernen hilft; (5) welche Oberflächen für welches Problem und wie sicherstellen, dass die Oberfläche die Ergebnisse nicht beeinflusst; (6) wie auswerten, welche Übereinstimmungsmaße, ab welchen Grenzwerten neu entwerfen oder neu annotieren; (7) wie die Ergebnisse formulieren und speichern, wann und an wen das Korpus herausgeben, wie über Aufwand und Ergebnis berichten. | S. 4, Abschnitt 2 | Fragen, keine Antworten |
| Gliederung des Tutorials: Toward a Science of Annotation; Setting up an Annotation Project (Basic Steps, Resources); Examples; die sieben Fragen (Theorie, Korpus, Oberfläche, Annotierende, Verfahren, Evaluation und Validierung, Verbreitung und Pflege); Ausblick. In der Gliederung steht die Oberfläche vor den Annotierenden, in der Liste der Fragen danach. | S. 4, Abschnitt 3 | Ankündigung |
| Die Tutorial-Notizen enthalten mehrere Seiten Literatur und Leseempfehlungen. | S. 4 | Hinweis; die Notizen liegen nicht vor |

## Daten, Methode, Zahlen

Keine. Das Abstract nennt keine Zahlen, keine Schwellen, keine Beispielprojekte mit Werten und kein Verfahren im Einzelnen.

## Wörtliche Stellen

> „setting up and performing small-, medium-, and large-scale annotation projects remains something of an art.“ (S. 4)

> „How can one ensure that the interfaces do not influence the annotation results?“ (S. 4)

> „At which cutoff points should one redesign or re-do the annotations?“ (S. 4)

## Bezug zur Dissertation

**1. Abgleich mit `goldstandard/LITERATUR-IAA.md`** (Zeile „Ablauf: Richtlinien, Pilot, Messen, Revidieren, Einfrieren, Hauptrunde, Adjudikation (MATTER-Zyklus). OntoNotes: 50 Sätze pro Pilotrunde, Revision bis 90 %.“, Beleg u. a. „Hovy 2010 ✔“): **Durch dieses PDF nicht gedeckt.** Das Abstract enthält weder den Ablauf in dieser Form noch „MATTER“, OntoNotes, 50 Sätze oder 90 %. Gedeckt ist nur, dass Verfahren, Auswertung, Grenzwerte für Neuentwurf und Herausgabe als Fragen eines Annotationsprojekts genannt werden (S. 4). Die Zahlen (50 Sätze pro Wort, Revision unter 90 %) stehen in Hovy et al. 2006, S. 58 (laut der KI-Zusammenfassung `Hovy-etal-2006-OntoNotes.md`, nicht gegengelesen); „MATTER“ steht nicht in diesem Abstract und ist auch in der Zusammenfassung von Hovy et al. 2006 nicht genannt (in derselben Zeile von `LITERATUR-IAA.md` steht dafür auch Pustejovsky & Stubbs 2012 mit ○). Vorschlag: Hovy 2010 in dieser Zeile auf ○ setzen oder streichen, bis die Folien vorliegen; die Zahlen nur mit Hovy et al. 2006 belegen. In PROTOKOLL §7 steht richtig Hovy et al. 2006, nicht Hovy 2010.

**2. PROTOKOLL §7 und A32 (Pilot mit Stoppregel).** Frage (6) „At which cutoff points should one redesign or re-do the annotations?“ (S. 4) benennt genau das, was A32 regelt. Als Beleg für eine bestimmte Schwelle taugt das Abstract nicht, nur als Beleg, dass die Frage zum Standardrepertoire gehört.

**3. A31 (Lesart vor den Karten) und offener Punkt 21 (Literatur zum Ankereffekt).** Frage (5) fragt ausdrücklich, wie man sicherstellt, dass die Oberfläche die Ergebnisse nicht beeinflusst (S. 4). Das stützt die Frage hinter A31, liefert aber keine Antwort und keinen Befund; für den Ankereffekt bleibt Literatur nötig.

**4. PROTOKOLL §10 und DMP §5 (Herausgabe).** Frage (7) „When, and to whom, should one release the corpus?“ (S. 4) gehört zum Thema der privaten Labels; das Abstract gibt keine Empfehlung und erwähnt Kontamination nicht (2010).

**5. Annotierende und Schulung (Alan, Kurzanleitung, offener Punkt 3).** Frage (3) nennt Schulung „adequately (but not over- or under-)“ (S. 4), wieder nur als Frage.

## Grenzen und Einwände

- Nur Abstract; als Beleg für Inhalte des Tutorials ungeeignet. Wer Hovy 2010 zitieren will, braucht die Folien oder die Notizen (laut Beschaffungstabelle vom 2026-10-30 nicht gefunden; die Tutorial-Seite der ACL 2010 zeige nur eine Gliederung, hier nicht selbst geprüft).
- Stand 2010: keine LLMs, keine Kontaminationsfrage, Crowdsourcing über Mechanical Turk als neue Option.
- Kein Bezug zu WSD oder historischen Sprachen.

## Weiterführend

- Wilcock (Dezember 2009) (S. 4): Lehrbuch zu Grundfragen der Annotation; Titel steht nicht im Abstract [zu ermitteln].
- Hovy et al. 2006, OntoNotes (nicht hier zitiert): Quelle der Zahlen in `LITERATUR-IAA.md` (S. 58); liegt als PDF vor und ist zusammengefasst.

## Julias Notizen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
