# Ihden, Barteld, Dreessen & Schröder 2015: Grammatische Annotation historischer Texte, ein Tagset für das Mittelniederdeutsche

**Datei:** `pdf/Barteld-etal-2015-Tagset-Mittelniederdeutsch.pdf` (nur lokal; 40 PDF-Seiten, Vortragsfolien)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen; Titelfolie und alle Tabellen zur Übereinstimmung (Folien 15, 16, 19, 22 bis 25) am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit der Datei auf der Projektseite des ReN (SHA-256 verglichen am 2026-11-13). Keine Markierungen.

**Zitierweise:** Die Folien tragen eigene Nummern (oben links), Titel- und Zwischenfolien keine. Unten steht „Folie x (PDF y)“. Zuordnung: Folie 1 = PDF 2, 2 = PDF 4, 3 = PDF 6 bis 8 (Aufbaufolien), 4 = PDF 10, 5 = PDF 12, 6 bis 12 = PDF 14 bis 20, 13 bis 16 = PDF 23 bis 26, 17 bis 19 = PDF 28 bis 30, 20 = PDF 32, 21 = PDF 34, 22 bis 26 (Anhang) = PDF 36 bis 40.

## Bibliografie

- **Vollständig:** Ihden, Sarah, Fabian Barteld, Katharina Dreessen & Ingrid Schröder (2015). Grammatische Annotation historischer Texte: ein Tagset für das Mittelniederdeutsche. Vortragsfolien, 5. Kongress der Internationalen Gesellschaft für Dialektologie des Deutschen (IGDD), „Räume, Grenzen, Übergänge“, Universität Luxemburg, 10. bis 12. September 2015. Universität Hamburg, Projekt ReN.
- **DOI/URL:** keine DOI. https://www.slm.uni-hamburg.de/ren/media/pdf/barteld-dreessen-ihden-druckversion-igdd2015-20150908.pdf (abgerufen und byte-gleich 2026-11-13; keine Lizenz angegeben). Der Titel enthält im Original einen Gedankenstrich zwischen den beiden Teilen.
- **Autor:innen und Reihenfolge:** Die Titelfolie (PDF 1) nennt vier Personen in zwei Spalten: links Sarah Ihden über Fabian Barteld, rechts Katharina Dreessen über Ingrid Schröder. Ihden steht oben links; spaltenweise gelesen ergibt das Ihden, Barteld, Dreessen, Schröder (so auch die Textebene), zeilenweise Ihden, Dreessen, Barteld, Schröder. Der Dateiname der Projektseite („barteld-dreessen-ihden“) und die Zitierung „Barteld et al. (2015)“ in `goldstandard/PROTOKOLL.md` bzw. „Barteld, Dreessen, Ihden & Schröder“ in `goldstandard/LITERATUR-IAA.md` folgen nicht der Titelfolie.
- **Datum:** Fußzeile jeder Inhaltsfolie „10.09.2015“.
- **Art:** Vortragsfolien (nicht begutachtet, keine Druckfassung des Vortrags gefunden). Das Tagset ist später als begutachteter Beitrag erschienen: Barteld, Ihden, Dreessen & Schröder 2018, „HiNTS: A Tagset for Middle Low German“, LREC 2018 (ACL Anthology L18-1622, BibTeX abgerufen 2026-11-13; nicht gelesen).
- **Sprache:** Deutsch

## Worum es geht

Die Folien stellen das Referenzkorpus Mittelniederdeutsch/Niederrheinisch (ReN, 1200 bis 1650) und das dafür entwickelte Tagset HiNTS (Historisches-Niederdeutsch-Tagset) für Wortart und Flexionsmorphologie vor (Folie 1 bis 2). Weil es für das Mittelniederdeutsche weder Werkzeuge noch Trainingsdaten noch Annotationsstandards gab und keine muttersprachliche Intuition verfügbar ist, passen die Autor:innen HiTS (Wortart) und STTS (Morphologie) an: Tags sollen aus dem Kontext entscheidbar sein, Ambiguität soll markiert, aber so spezifisch wie möglich angegeben werden (Folien 6, 10 bis 12). Zur Qualitätssicherung werden zwei Inter-Annotator-Agreements mit je zwei Annotator:innen durchgeführt und die Abweichungen nach Ursachen aufgeschlüsselt: fehlende Regeln, Abweichungen trotz bestehender Regeln, unterschiedliches Textverständnis (Folien 15, 16, 19). Fazit: HiNTS ist anwendbar, senkt den Grad der Interpretation, und Abweichungen haben verschiedene Ursachen, von denen sich systematische reduzieren lassen (Folie 20).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| ReN: Referenzkorpus Mittelniederdeutsch/Niederrheinisch (1200 bis 1650), Teil des „Korpus historischer Texte des Deutschen“ neben Altdeutsch, Mittelhochdeutsch, Frühneuhochdeutsch; Grundlage Handschriften, Drucke, Inschriften; Ziel: diplomatisch transkribierte, lemmatisierte, grammatisch annotierte Texte. | Folie 2 (PDF 4) | Projektbeschreibung |
| Korpusdesign nach Schreibsprachlandschaft, acht Zeitabschnitten (I: 1200 bis 1300 bis VIII: 1601 bis 1650) und acht Feldern der Schriftlichkeit (Recht, Urkunden, Verwaltung, Wissensvermittlung, Religion, Literarische Texte, private Schriftlichkeit, Inschriften). | Folie 3 (PDF 6 bis 8) | Projektbeschreibung |
| Ablauf in drei Phasen: Transkription; Annotation (Wortart, Flexionsmorphologie, Lemmatisierung); Publikation (ANNIS, TEI). | Folie 4 (PDF 10) | Projektbeschreibung |
| Ausgangslage: „low-resourced language“, keine Werkzeuge und keine Trainingsdaten, kaum elektronische Ressourcen; daher keine Standards für die Annotation, weder Tagset noch Lemmainventar. | Folie 6 (PDF 14) | Problemstellung |
| Anforderung: nah an HiTS (Wortart) und STTS (Morphologie) bleiben, aber Tags müssen „anhand des konkreten Kontextes auswählbar sein (keine muttersprachliche Intuition)“; Beispiel STTS PIAT gegen PIDAT, das „erst als Ergebnis der Korpusauswertung entscheidbar“ sei. | Folie 10 (PDF 18) | eigene Begründung |
| Anforderung: Ambiguitäten kennzeichnen (HiTS hat KO* für nicht entscheidbares KON/KOU), aber so spezifisch wie möglich: STTS kennt in der Morphologie nur eindeutig oder `*`. | Folie 11 (PDF 19) | eigene Begründung |
| Folge: weder STTS noch HiTS ohne Änderung geeignet, daher eigene Fassung HiNTS (Wortart plus Morphologie). | Folie 12 (PDF 20) | eigenes Ergebnis |
| Abweichung von HiTS: keine lexembezogenen Vorannahmen; statt Determinativ gegen Pronomen nach Lexem nun nach Distribution (D... attributiv, DP... substituierend); Nutzen: Lemmata, die nur substituierend vorkommen, als echte Pronomen ermitteln. | Folien 13 bis 14 (PDF 23 bis 24) | eigenes Ergebnis |
| STTS-Sternchen für Ambiguität nennt die möglichen Werte nicht und erzeugt eine Tendenz, sich zu entscheiden (Zitat TIGER-Schema); das sei für das Neuhochdeutsche möglich, für historische Sprachstufen „zu interpretatorisch“. HiNTS gibt die möglichen Werte an, z. B. `Masc-Neut.Nom.Sg`. | Folien 17 bis 18 (PDF 28 bis 29) | eigene Begründung; TIGER-Schema referiert |
| Qualitätssicherung: „Anwendung des MAMA-Zyklus (vgl. Pustejovsky/ Stubbs 2012)“; zwei IAA mit je zwei Annotator:innen. IAA I: Wortart und Morphologie, ohne Lemmatisierung, rein manuell. IAA II: dazu Lemmatisierung über eine Lemmaliste, halbautomatisches Tagging. | Folie 15 (PDF 25) | eigenes Verfahren |
| Abweichungen werden nach drei Ursachen aufgeschlüsselt: „Abweichungen aufgrund fehlender Regeln“, „Abweichungen trotz bestehender Regeln“ (unterteilt in Regelverstoß, Folgefehler, Annotation vergessen/Aufmerksamkeit), „unterschiedliches Textverständnis“. | Folien 16, 19, 23, 25 (PDF 26, 30, 37, 39) | eigenes Ergebnis |
| Wortart: Abweichungen gesamt 13,0 % (IAA I) und 11,3 % (IAA II); Anteil durch fehlende Regeln sinkt von 8,9 auf 3,7 %, Anteil trotz Regeln steigt von 3,1 auf 5,7 %. | Folie 16 (PDF 26) | eigenes Ergebnis |
| Morphologie: gesamt 19,8 % und 14,8 %; fehlende Regeln 8,2 auf 1,7 %, trotz Regeln 11,6 auf 12,6 %. | Folie 19 (PDF 30) | eigenes Ergebnis |
| Spalte „IAA III“ enthält keine Werte, nur Pfeile (fallend bzw. gleichbleibend); was sie bedeuten (Erwartung, noch laufende Runde), sagen die Folien nicht. | Folien 16, 19 (PDF 26, 30) | eigene Darstellung, ohne Erläuterung |
| Resümee: HiNTS „erfolgreich anwendbar“, mit HiNTS „sinkt der Grad der Interpretation“; Abweichungen haben unterschiedliche Ursachen; systematische lassen sich reduzieren; routinierte Anwendung werde aufmerksamkeitsbedingte Fehler und Regelverstöße senken. | Folie 20 (PDF 32) | eigene Schlussfolgerung |
| Vergleichswerte aus anderen Korpora (Wortart): 97,9 % Übereinstimmung für Lernersprache mit STTS (Rehbein et al. 2012), 96,5 % für das Kiezdeutsch-Korpus (Rehbein & Schalowski 2013). | Folie 26 (PDF 40) | referiert |

## Daten, Methode, Zahlen

- **Sprache, Epoche:** Mittelniederdeutsch und Niederrheinisch, 1200 bis 1650 (Folie 2). Beispiele aus einem Brief von 1535 und dem Oldenburger Sachsenspiegel (Folien 17, 18).
- **Inventar:** grammatisch (Wortart, Flexionsmorphologie), nicht semantisch. Keine Bedeutungsannotation.
- **Annotator:innen:** je zwei pro IAA (Folie 15). Wer, wie geschult, auf welcher Textmenge: nicht angegeben.
- **Maß:** Anteil der Abweichungen in Prozent. Bezugsgröße (Tokens? Tags?) und Stichprobengröße stehen nicht auf den Folien; kein zufallskorrigiertes Maß (κ, α).
- **Tab. Folie 16 (Wortart), am Seitenbild geprüft:**

| Art der Abweichung | IAA I | IAA II | IAA III |
|---|---|---|---|
| fehlende Regeln | 8,9 % | 3,7 % | fallend (Pfeil) |
| trotz bestehender Regeln | 3,1 % | 5,7 % | fallend (Pfeil) |
| unterschiedliches Textverständnis | 1,0 % | 1,9 % | gleich (Pfeil) |
| gesamt | 13,0 % | 11,3 % | fallend (Pfeil) |

- **Tab. Folie 19 (Morphologie), am Seitenbild geprüft:** fehlende Regeln 8,2 / 1,7 %; trotz Regeln 11,6 / 12,6 %; Textverständnis 0 / 0,5 %; gesamt 19,8 / 14,8 %; IAA III wieder nur Pfeile.
- **Aufschlüsselung „trotz bestehender Regeln“ (Anhang), am Seitenbild geprüft:**

| Unterart | Wortart IAA I | Wortart IAA II | Morph. IAA I | Morph. IAA II |
|---|---|---|---|---|
| Regelverstoß | 78,6 % | 62,5 % | 35,6 % | 47,3 % |
| Folgefehler | 21,4 % | 23,2 % | 57,8 % | 25,5 % |
| Annotation vergessen, Aufmerksamkeit | 0 % | 14,3 % | 5,6 % | 17,3 % |
| tagger-reproduzierte Fehler | (keine Zeile) | (keine Zeile) | - | 10,0 % |
| verschiedene | (keine Zeile) | (keine Zeile) | 1,1 % | 0 % |
| gesamt | 100 % | 100 % | 100 % | 100 % |

  Die Prozente sind hier Anteile an den Abweichungen trotz Regeln, nicht an allen Tokens (Folien 23, 25).
- **Anhangsfolien 22 und 24** wiederholen die Tabellen der Folien 16 und 19 als Aufbaustufe mit leeren Zellen (z. B. IAA II ohne Textverständnis und gesamt); maßgeblich sind die vollständigen Folien 16 und 19.

## Wörtliche Stellen

> „Tags müssen anhand des konkreten Kontextes auswählbar sein (keine muttersprachliche Intuition)“ (Folie 10, PDF 18)

> „→ für Nhd. möglich, für historische Sprachstufen problematisch, da zu interpretatorisch“ (Folie 17, PDF 28; zur Tendenz, bei Ambiguität eine Entscheidung herbeizuführen)

> „Abweichungen zwischen den Annotatoren haben unterschiedliche Ursachen“ (Folie 20, PDF 32)

## Bezug zur Dissertation

- **PROTOKOLL §7, Schritt 6 (Ursachencode pro Abweichung):** Das Protokoll nennt fünf Codes „angelehnt an Barteld et al. (2015) und um zwei Codes erweitert: Richtlinienlücke, Versehen, echte Textambiguität, Inventarlücke, Editions- oder Normalisierungseffekt“. Am Original:
  - „Richtlinienlücke“ entspricht „Abweichungen aufgrund fehlender Regeln“ (Folie 16). Deckung gut.
  - „Versehen“ ist enger als „Abweichungen trotz bestehender Regeln“. Die Folien zählen dazu Regelverstoß, Folgefehler und vergessene Annotation (Folien 16, 23, 25); der größte Teil sind Regelverstöße (bei Wortart 78,6 und 62,5 %), nicht Aufmerksamkeitsfehler (0 und 14,3 %). Ein Regelverstoß kann bewusst sein (Annotator:in hält die Regel für falsch) und ist dann kein Versehen. Vorschlag: den Code „Regelverstoß“ oder „Abweichung trotz Regel“ nennen und Versehen als Unterart führen, oder die Abweichung von der Vorlage im Protokoll benennen.
  - „echte Textambiguität“ ist nicht dasselbe wie „unterschiedliches Textverständnis“. Die Folien sagen nicht, dass der Text mehrdeutig ist, sondern dass die beiden Personen ihn verschieden verstanden haben; ob eine der Lesarten falsch war, bleibt offen. Mehrdeutigkeit behandelt HiNTS als Annotationswert, nicht als Abweichungsursache (KO*, `Masc-Neut`, Folien 11, 18). Für das Protokoll entspricht das eher dem Status `MEHRERE` (§6) als einem Ursachencode. Vorschlag: den Code als „unterschiedliches Textverständnis“ führen und „echte Textambiguität“ als Ergebnis der Adjudikation (dann `MEHRERE` oder `KONTEXT_UNZUREICHEND` im Gold) davon trennen.
  - Die Unterarten „Folgefehler“ und „tagger-reproduzierte Fehler“ (Folien 23, 25) haben im Protokoll keine Entsprechung. Folgefehler gibt es bei der WSD vermutlich selten; tagger-reproduzierte Fehler entstehen nur bei Vorannotation, die das Protokoll durch Blindheit ausschließt (§6). Das stützt die Blindheit: Schon in IAA II mit halbautomatischem Tagging gehen 10 % der Morphologie-Abweichungen trotz Regeln auf übernommene Tagger-Fehler zurück (Folie 25).
- **PROTOKOLL §7, Schritt 2 (Pilot, Richtlinien nachschärfen):** Die Folien zeigen genau den Effekt, den der Pilot nutzen will: Zwischen IAA I und IAA II sinkt der Anteil durch fehlende Regeln deutlich (Wortart 8,9 auf 3,7 %, Morphologie 8,2 auf 1,7 %), während Abweichungen trotz Regeln gleich bleiben oder steigen (Folien 16, 19). Nachschärfen der Richtlinien senkt also nur den einen Teil; das spricht dafür, die Pilot-Abweichungen ebenfalls nach Ursache zu zählen, damit erkennbar ist, ob eine weitere Runde noch etwas bringt. Achtung: IAA II unterscheidet sich von IAA I auch durch Lemmaliste und halbautomatisches Tagging (Folie 15); die Verbesserung ist nicht allein den Richtlinien zuzuschreiben.
- **PROTOKOLL §9.1 (Maße):** Die Folien berichten nur Abweichungsanteile ohne Zufallskorrektur und ohne Stichprobengröße. Als Vorbild für das Maß taugen sie nicht; sie stützen nur die Aufschlüsselung nach Ursachen. Die Vergleichswerte 97,9 und 96,5 % (Folie 26) sind Wortartenwerte für Gegenwartsdeutsch und nicht auf WSD übertragbar.
- **PROTOKOLL §6 (`MEHRERE`, keine Entscheidung erzwingen):** Die Begründung gegen das STTS-Sternchen (Folie 17) ist eine Parallele aus der historischen Annotation: Ein Schema, das zur Entscheidung drängt, ist für historische Sprachstufen „zu interpretatorisch“. Das stützt, Unterbestimmtheit als eigenen Status zuzulassen und die möglichen Werte (hier: die Sense-IDs) zu nennen statt nur „unklar“.
- **`knowledge/data.md`, B15 und Abschnitt 1 (Lemma, Sense, Wortart):** Die Folien vermeiden „lexembezogene Vorannahmen“ und entscheiden die Kategorie am Beleg (Folien 13 bis 14). Das ist eine Parallele zur Frage, ob Senses an Wortarten oder Typen gebunden sind (B1, B10): Auch dort hängt im Silber etwas am Lemma oder Typ, was eigentlich am Beleg zu entscheiden wäre.
- **`goldstandard/LITERATUR-IAA.md`, Zeile zur Ursachentypologie:** Dort steht „Richtlinienlücke, Regelverstoß, unterschiedliches Textverständnis“ mit Status ○. Am Original ist „Regelverstoß“ eine Unterart der mittleren Kategorie, nicht die Kategorie selbst; die Kategorie heißt „Abweichungen trotz bestehender Regeln“ (Folie 16). Der Prüfstatus kann nach diesem Lauf ✔ werden (Volltext gelesen); das entscheidet Julia.

## Grenzen und Einwände

- Vortragsfolien, nicht begutachtet. Keine Angaben zu Textmenge, Tokenzahl, Auswahl der IAA-Texte, Annotator:innen und Bezugsgröße der Prozente. Für Aussagen über HiNTS selbst ist die LREC-Fassung von 2018 zu zitieren (nicht gelesen).
- Nur Wortart und Morphologie; keine Bedeutungen. Die Übertragung der Ursachentypologie auf WSD mit onomasiologischem Inventar ist eine Entscheidung des Protokolls, keine Aussage der Folien.
- IAA I und IAA II unterscheiden sich in mehr als einer Bedingung (Richtlinienstand, Lemmaliste, halbautomatisches Tagging); die Veränderung zwischen den Runden ist keiner einzelnen Ursache zuzuordnen.
- Wie die Ursache einer Abweichung festgestellt wurde (von wem, mit welchen Kriterien, ob mit Übereinstimmungsprüfung), sagen die Folien nicht. Die Unterscheidung zwischen „trotz Regeln“ und „unterschiedliches Textverständnis“ ist damit nicht nachvollziehbar.
- „MAMA-Zyklus“ steht so auf Folie 15 (am Seitenbild geprüft), ohne Erläuterung. `goldstandard/LITERATUR-IAA.md` nennt für Pustejovsky & Stubbs (2012) den „MATTER-Zyklus“ (Status ○). Wie sich beide Bezeichnungen zueinander verhalten, sagen die Folien nicht; an Pustejovsky & Stubbs zu prüfen.

## Weiterführend

- Barteld, Ihden, Dreessen & Schröder 2018, „HiNTS: A Tagset for Middle Low German“, LREC 2018 (nicht auf den Folien zitiert; ACL Anthology L18-1622): begutachtete Fassung des Tagsets, für Zitate zu HiNTS selbst.
- Barteld, Ihden, Schröder & Zinsmeister 2014, „Annotating descriptively incomplete language phenomena“, LAW VIII, S. 99 bis 104 (Folie 21; zitiert auf Folie 18 zur Genusambiguität).
- Pustejovsky & Stubbs 2012 (Folie 21; zum MAMA-Zyklus, Folie 15).
- Dipper et al. 2013, HiTS (Folie 21; liegt vor, `zusammenfassungen/Dipper-etal-2013-HiTS.md`).
- Rehbein et al. 2012 und Rehbein & Schalowski 2013 (Folie 21; Vergleichswerte Folie 26).
- TIGER-Morphologie-Annotationsschema 2015 (Folie 21; Zitat auf Folie 17).

## Julias Notizen im PDF

Keine. Das PDF enthält keine Anmerkungen; `markierungen.py` legt keine Datei an.
