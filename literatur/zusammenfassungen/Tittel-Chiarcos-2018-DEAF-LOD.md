# Tittel & Chiarcos 2018: Das DEAF als Linked Open Data mit OntoLex-Lemon

**Datei:** `pdf/Tittel-Chiarcos-2018-DEAF-LOD.pdf` (nur lokal; 10 Seiten: Deckblatt von OPUS Augsburg plus 9 Seiten Beitrag)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganzes PDF an der Textebene gelesen; Venue und Seiten am Tagungsband selbst geprüft (siehe Bibliografie).

Seitenzählung: Das lokale PDF trägt keine Seitenzahlen. Der Text steht mit identischen Seitenumbrüchen im GLOBALEX-2018-Band auf S. 57 bis 65 (am 2026-10-28 Seite für Seite verglichen). Daher gilt: PDF-Seite n = gedruckte S. 55 + n (PDF 2 = S. 57, PDF 10 = S. 65); PDF-Seite 1 ist das Repositoriums-Deckblatt.

## Bibliografie

- **Vollständig:** Tittel, Sabine & Chiarcos, Christian (2018). Historical Lexicography of Old French and Linked Open Data: Transforming the Resources of the *Dictionnaire étymologique de l'ancien français* with OntoLex-Lemon. In: Ilan Kernerman & Simon Krek (Hg.), *Proceedings of the LREC 2018 Workshop „Globalex 2018: Lexicography & WordNets"*, Miyazaki, 8. Mai 2018. Paris: European Language Resources Association, S. 57 bis 65. ISBN 979-10-95546-28-3.
- **DOI/URL:** keine DOI. Tagungsband als PDF (Kopie bei SADiLaR): https://sadilar.org/wp-content/uploads/2021/11/globalex-2018_proceedings.pdf ; LREC-Archiv W33: http://archive.lrec-conf.org/workshops/lrec2018/W33/index.html ; frei auch über OPUS Augsburg (CC BY-NC 4.0): https://opus.bibliothek.uni-augsburg.de/opus4/104091
- **Venue geklärt (2026-10-28):** ✔ Im GLOBALEX-Band (Titelei: Hg. Kernerman & Krek, ISBN 979-10-95546-28-3) steht der Beitrag im Inhaltsverzeichnis auf S. 57 und läuft mit gedruckten Seitenzahlen bis S. 65; der nächste Beitrag (Amaro) beginnt auf S. 66. Inhaltsverzeichnis, Programm, BibTeX des LREC-Archivs und Fußzeile nennen den Kurztitel „Linked Open Data for the Historical Lexicography of Old French", die Kopfzeile des Beitrags den langen Titel. In der Beitragsliste der LDL-2018-Proceedings (W23, ISBN 979-10-95546-19-1) steht der Beitrag **nicht**; von Tittel ist dort nur „Using RDFa to Link Text and Dictionary Data for Medieval French" (mit Bermúdez-Sabel und Chiarcos). Das OPUS-Deckblatt (PDF-Seite 1), das LDL-2018 nennt, ist also falsch. Tittel et al. 2020 (S. 10) zitieren S. 58 bis 66; der Band selbst zeigt S. 57 bis 65.
- **Art:** Workshop-Beitrag (LREC-Workshop)
- **Sprache:** Englisch

## Worum es geht

Die Autor:innen überführen das *Dictionnaire étymologique de l'ancien français* (DEAF; Altfranzösisch 842 bis ca. 1350) aus XML in RDF mit OntoLex-Lemon (S. 57). Vorgehen: ein Musterartikel (*fiel* „Galle"), daraus ein Anwendungsprofil, manuelle Umsetzung, dann XSLT-Skripte für alle ca. 83.000 Artikel (S. 58, 61). Kernbefund: Die Struktur lässt sich automatisch umwandeln, die Verknüpfung von Bedeutungen mit Konzepten moderner Wissensbasen aber nicht, wegen der „Historical Semantic Gap" (S. 62). Offen bleiben Dialektkennzeichnung und die Modellierung der Bedeutungsbäume (S. 63 bis 64).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Das elektronische DEAF (DEAFél, seit 2010) ist ein „data silo": nur lesend oder über vorgesehene Suchfunktionen nutzbar, proprietäres Format, ungeeignet für maschinelle Verarbeitung. | S. 57, Abschn. 1.1 | Einschätzung zur eigenen Ressource |
| LOD-Arbeiten zu Wörterbüchern konzentrierten sich auf moderne Sprachstufen; Ausnahmen (Etymologie, Altgriechisch) seien technologisch statt philologisch motiviert. | S. 58, Abschn. 1.3 | Forschungsstand, referiert |
| OntoLex: Ein `LexicalSense` ist eintragsspezifisch und verbindet Eintrag und Konzept; `LexicalConcept` fasst Senses verschiedener Einträge zusammen. Best Practice: über Senses verlinken, wo das Wörterbuch eine Definition hat, damit die Originaldefinition bei späterem Konzeptwandel nachprüfbar bleibt. | S. 59, Abschn. 1.4 | referiert (OntoLex; Wang et al. 2011) |
| Musterartikel *fiel*: Lemma plus sechs graphische Varianten, drei Hauptbedeutungen („bile", „gall bladder", übertragen „bitterness"), 13 Unterbedeutungen; einzelne lexikalische Einheiten sind medizinische oder botanische Fachtermini. | S. 59, Abschn. 2 | eigene Analyse |
| Modelliert sind zunächst nur Lexeme, Schreibungen und Bedeutungen; Etymologie, Datierung und Belegzitate fehlen noch. | S. 60, Abschn. 2 | eigene Einschränkung |
| Die Skripte wurden am manuell erzeugten RDF von *fiel* und an einer Zufallsstichprobe von fünf weiteren Artikeln manuell geprüft; für die Verknüpfung mit externen Ressourcen gelte das nur eingeschränkt. | S. 62, Abschn. 3.2 | eigenes Ergebnis |
| **Historical Semantic Gap:** Das außersprachliche Konzept, das ein altfranzösisches Wort bezeichnet, weicht oft vom modernen ab (Beispiel: „function of the brain" für einen Arzt des 13. Jh.). Die Zuordnung zu einer Ontologie-Entität lasse sich für die altfranzösische Lexik nicht automatisieren. | S. 62, Abschn. 4 | eigene Analyse |
| Lösung: halbautomatisch. Die Skripte setzen einen Platzhalter („XXX"), den ein:e Fachlinguist:in für altfranzösische lexikalische Semantik ausfüllt; botanische Termini ließen sich über den lateinischen Fachnamen automatisch auf DBpedia abbilden. | S. 62, Abschn. 4 | eigenes Verfahren |
| Darstellung als Mittelweg: Originalangabe des DEAF als Zeichenkette und semantische Deutung als URI am selben Property; in OWL so nicht zulässig, per SPARQL Update bereinigbar. | S. 62, Abschn. 3.2 | eigenes Verfahren |
| Keine einheitliche Orthographie; ISO 639 hat keine Codes für altfranzösische Dialekte, deshalb vorläufig alles `fro`, wodurch Dialektinformation verloren geht. | S. 63 bis 64, Abschn. 5 | eigene Analyse |
| Bedeutungsbäume spiegeln Bedeutungswandel (Metapher, Metonymie usw.); SKOS biete nur `broader`/`narrower`; die Relationen werden über `ontolex:usage` mit DBpedia-Verweis modelliert. | S. 64, Abschn. 5 | eigenes Verfahren |
| Bevorzugte Verknüpfungspartner seien historisch oder sprachlich verwandte Wörterbücher; Verknüpfung mit modernen Ressourcen brauche theoretische Reflexion, um Fehlverknüpfungen durch die Semantic Gap zu vermeiden. | S. 64, Abschn. 5 | Programmatik |
| Offene Lizenz des konvertierten DEAF geplant, rechtliche Klärung noch ausstehend; das sei für historische Philologien typisch. | S. 62 und 64 | Projektstand |

## Daten, Methode, Zahlen

An der Textebene geprüft:

- DEAF: Altfranzösisch 842 bis ca. 1350; Print und seit 2010 DEAFél, XML/XHTML aus MySQL (S. 57).
- Ca. 83.000 Wörterbuchartikel sollen konvertiert werden (S. 61).
- *fiel*: 6 weitere Schreibungen, 3 Hauptbedeutungen, 13 Unterbedeutungen (S. 59).
- Prüfung: 1 manuell modellierter Artikel plus Stichprobe von 5 weiteren (S. 62).
- Höchste Variantenzahl: Adverb *iluec* mit mehr als 120 Schreibungen (S. 63, Anm. 12).
- Verwendete Vokabulare: OntoLex-Kern, decomp, vartrans, LexInfo, OLiA, FOAF, Dublin Core; eigene Klassen `deaf:TechReg` und `deaf:idem` (S. 60).
- Abbildungen 1 bis 4 (DEAFél-Ansicht und Modell von *fiel*, S. 60 bis 61) nur am Seitenbild lesbar [am PDF zu prüfen].

## Wörtliche Stellen

> „The mapping of a lexical unit to the correct entity in an ontology is a difficult task that cannot be automated for the Old French lexis." (S. 62)

> „His expertise assures the correct mapping." (S. 62; gemeint ist der Fachlinguist, der die Platzhalter ausfüllt)

## Bezug zur Dissertation

- **Begriff „Historical Semantic Gap" (PROTOKOLL §1 Nebenfrage, §6 `KEINE_PASST`):** Der Begriff stammt hier, zwei Jahre vor Tittel, Gillis-Webber & Nannini 2020 (S. 8; `zusammenfassungen/Tittel-etal-2020-Hallig-Wartburg-Ontologie.md`), wo er auf das Begriffssystem von Hallig-Wartburg übertragen wird. 2018 betrifft er die Zuordnung einzelner Bedeutungen zu modernen Konzepten (DBpedia), 2020 das Begriffssystem selbst. Für die Dissertation ist das die Herkunft des Arguments, dass ein Inventar moderner Begriffe historische Bedeutungen verfehlen kann; `KEINE_PASST` mit angekreuzten Begriffen kann das für das Mittelhochdeutsche zählbar machen.
- **Menschliche Zuordnung als Normalfall (PROTOKOLL §5, §9.2):** Die Autor:innen halten die Zuordnung Bedeutung zu Konzept für nicht automatisierbar und lassen sie von einem Experten machen (S. 62), ohne dessen Übereinstimmung mit anderen zu messen. Das ist genau die Lage des MHDBDB-Silbers: menschlich, aber ohne dokumentierte Richtlinien und IAA (PROTOKOLL §2). Kein Beleg für Gold, aber ein Vergleichsfall für die Lücke „keine IAA für ein onomasiologisches Inventar" (§9.2, letzter Punkt).
- **Wörterbuch- gegen Begriffssystem-Modell:** Im DEAF haben Bedeutungen Definitionen und einen Bedeutungsbaum mit Wandelrelationen (S. 64); in der MHDBDB ist ein Sense nur eine Menge von Begriffszeigern, fast ohne `<def>` (`knowledge/data.md` Abschnitt 1 und B13). Die OntoLex-Best-Practice (S. 59: über Senses verlinken, damit die Originaldefinition erhalten bleibt) setzt Definitionen voraus, die die MHDBDB nicht hat. Das stützt PROTOKOLL §5: Die Karten zeigen Begriffsnamen mit Pfad, weil es sonst nichts gibt, und keine LLM-generierten Definitionen.
- **Schreibvarianten (`knowledge/data.md` Abschnitt 1, `variants.xml`; B1):** Das DEAF modelliert Varianten als `otherForm` am Eintrag (S. 63), ohne Bindung an einzelne Bedeutungen. Die MHDBDB-Typlisten an `<sense>` (B1) sind dagegen eine typbezogene Sense-Zuordnung; das DEAF kennt so etwas nicht. Ein Hinweis, dass B1 eine Eigenheit der MHDBDB und kein Standardmuster historischer Wörterbücher ist (Vergleich mit einem Wörterbuch, kein Beweis).
- **Bezug zu Hinkelmanns 2019:** Beide setzen auf OntoLex; Hinkelmanns (S. 137) ergänzt die onomasiologische Erweiterung Lemon-tree, die das DEAF als semasiologisches Wörterbuch nicht braucht.

## Grenzen und Einwände

- Machbarkeitsstudie: ein Musterartikel, Prüfung an fünf weiteren; keine Fehlerquote, keine Zahl zur manuellen Nacharbeit.
- Die Verknüpfung mit Konzepten ist nur als Platzhalterverfahren beschrieben, nicht durchgeführt oder evaluiert.
- Die Semantic Gap wird mit einem Beispiel begründet (S. 62), nicht gemessen.
- Semasiologisches Wörterbuch; auf das onomasiologische Inventar der MHDBDB nur als Vergleich übertragbar.
- Bibliografisch: OPUS-Deckblatt nennt die falsche Venue (siehe oben).

## Weiterführend

- Tittel, Bermúdez-Sabel & Chiarcos 2018, *Using RDFa to Link Text and Dictionary Data for Medieval French*, LDL-2018 (S. 62, 65): Verknüpfung einer Edition mit dem Wörterbuch, also der Schritt von Beleg zu Bedeutung.
- Khan et al. 2017, Liddell-Scott nach OntoLex (S. 58, 65): historisches Wörterbuch, Vergleichsfall.
- Wang, Schlobach & Klein 2011, *Concept drift and how to identify it* (S. 59, 65).
- Chiarcos & Sukhareva 2014, etymologische Datenbanken, Germanisch (S. 58, 65).
- Mazziotta 2010, SRCMF, RDF-Annotation für Altfranzösisch (S. 62, 65).
