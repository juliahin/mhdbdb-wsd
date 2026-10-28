# Dipper et al. 2013: HiTS, ein Tagset für historische Sprachstufen des Deutschen

**Datei:** `pdf/Dipper-etal-2013-HiTS.pdf` (nur lokal; 53 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, ganze Textebene gelesen (PDF-Seiten 1 bis 53), Tabelle S. 104 am Seitenbild geprüft, DOI aufgelöst.

Seitenzählung: PDF-Seite n = gedruckte S. 84 + n (PDF 1 = S. 85 ohne gedruckte Zahl, PDF 2 = S. 86, PDF 53 = S. 137). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Dipper, Stefanie, Karin Donhauser, Thomas Klein, Sonja Linde, Stefan Müller & Klaus-Peter Wegera (2013). HiTS: ein Tagset für historische Sprachstufen des Deutschen. *Journal for Language Technology and Computational Linguistics (JLCL)* 28(1), S. 85 bis 137. Themenheft „Das Stuttgart-Tübingen Wortarten-Tagset – Stand und Perspektiven“.
- **DOI/URL:** https://doi.org/10.21248/jlcl.28.2013.170 (aufgelöst auf https://jlcl.org/article/view/170; dort veröffentlicht 2013-07-01, CC BY 4.0, ISSN 2190-6858). Band, Heft und Seiten auch in der Fußzeile jeder Seite ✔ (z. B. S. 85).
- **Art:** begutachteter Zeitschriftenartikel (Dank an „anonymen Reviewer[n]“, S. 85, Anm. 1)
- **Sprache:** Deutsch

## Worum es geht

Der Artikel stellt HiTS vor, das Wortart-Tagset der Referenzkorpora Altdeutsch und Mittelhochdeutsch, und beschreibt vor allem die Unterschiede zum STTS (S. 85, 87). Drei Neuerungen stehen im Mittelpunkt: eigene Token-Tags für historische Wortgrenzen (Abschnitt 2), die durchgehende Doppelannotation nach Lemma-Wortart und Beleg-Wortart (Abschnitt 3) und feinere Klassen bei Determinativen, Pronomen und Adjektiven (Abschnitte 4 und 5). Ambiguitäten, die sich mangels muttersprachlicher Intuition nicht auflösen lassen, werden bewusst nicht als ambig markiert, sondern nach der historisch älteren Lesart entschieden (S. 86, 109 bis 110). Ein Anhang listet alle Tags (S. 114 bis 137). Evaluationszahlen (Übereinstimmung, Taggergenauigkeit) enthält der Artikel nicht.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| HiTS entstand in den Projekten Referenzkorpus Altdeutsch und Mittelhochdeutsch; im Referenzkorpus Frühneuhochdeutsch wird eine vereinfachte Version verwendet. | S. 85, Abschnitt 1 | Projektbeschreibung |
| HiTS orientiert sich am STTS und übernimmt dessen hierarchisches Tagdesign; die Tagnamen des STTS seien aber nicht immer geeignet, z. B. ist der Artikel in HiTS eine Unterklasse der Determinativa. Nicht jedes HiTS-Tag lässt sich eindeutig auf ein STTS-Tag abbilden. | S. 85 | Setzung der Autor:innen |
| Muttersprachliche Intuition fehlt; Annotator:innen können keine linguistischen Tests durchführen. An ihre Stelle treten „Synopse und statistische Analyse möglichst vieler Belege“. Bei verbleibender Ambiguität wird festgelegt, welche Analyse annotiert wird, „prinzipiell“ die historisch ältere. | S. 86, Abschnitt 1 | Richtlinie |
| Zwei Ebenen der Textrepräsentation: diplomatische „Text-Ebene“ und „Token-Ebene“ mit moderner Tokenisierung; Token-Tags (MS, US, UH, UB, MLH, ULH, ULS) benennen die Art der Abweichung. | S. 87 bis 90, Abschnitt 2 | Richtlinie |
| Getrenntschreibung, die zwischen Genitivfügung und Kompositum ambig ist, bleibt getrennt und wird als Genitivfügung analysiert (*der sunnen schîn*). | S. 89, Bsp. (3b); S. 109 | Richtlinie |
| **Lemma- vs. belegspezifische Annotation:** Die Wortart jeder Wortform wird zweifach annotiert, mit Blick auf das Lemma und mit Blick auf den Beleg im Kontext. Beide sind oft identisch, können aber divergieren (Beispiel Appellativum als Eigenname, NA > NE). | S. 92, Abschnitt 3 | Kernentscheidung des Tagsets |
| Notation „Wortform / Lemma-POS > Beleg-POS“; steht nur eine Kategorie, ist es die Beleg-Wortart. Das Zeichen „>“ zeigt oft auch eine diachrone Entwicklung an. | S. 93, Bsp. (12), Anm. 7 | Konvention |
| Begründung: Nur lemmabezogene Annotation müsste abweichende Verwendungen ignorieren; nur kontextbezogene Annotation führe dazu, dass „u.U. keine klaren kategorialen Zuweisungen mehr möglich sind“ und quantitative Recherchen verfälscht würden. Die Trennung werde kontextabhängigen Schwankungen gerecht. | S. 95, Abschnitt 3.3 | Argument der Autor:innen |
| Bei ahd. Adverb und Verbpartikel: Lemma-Ebene durchgehend AVD, Beleg-Ebene nach dem Referenzwörterbuch (Splett 1993), damit die Entscheidung „für Nutzer jederzeit nachvollziehbar“ ist; die „interpretatorische Endentscheidung“ bleibe den Nutzer:innen überlassen. | S. 94 bis 95, Abschnitt 3.2 | Richtlinie |
| Adverbial verwendete Adjektive erhalten ADJ > AVD; entschieden wird „nicht nach der Wortbildungs-, sondern nach der Verwendungsweise“. | S. 104 bis 105, Abschnitt 5.1 | Richtlinie |
| Substantivierte Adjektive (ADJS) werden von attributiven Adjektiven und von Substantiven unterschieden; ob ein Bezugswort ergänzbar ist, wäre „oft Spekulation, daher zeitaufwändig und für die Auswertung unergiebig“. | S. 106 bis 107, Abschnitt 5.3 | Richtlinie |
| Stämme wie *reht*, *guot*, *vil* kommen als Adjektiv und Substantiv vor; wo die Endung nicht unterscheidet, bleiben nur „unsicherere Anhaltspunkte“: Syntax und Semantik (‘gut, Gutes’ oder ‘Gutes; Besitz, Güte, gute Absicht’). | S. 107 | Befund und Richtlinie |
| Mhd. *dehein*: Weil die Unterscheidung nicht-affirmativ vs. negierend „teilweise nur schwer zu treffen ist“, werden beide Fälle mit demselben Tag annotiert (DI > DNEGA/DNEGS). | S. 124, Anmerkung zur Tabelle | Richtlinie |
| **Ambiguität wird nicht markiert.** Historische Daten enthalten weit häufiger kontextuell unauflösbare Ambiguitäten. Gegen eine Ambiguitätsmarkierung sprechen zwei Punkte: Die Aufgabe würde „deutlich komplexer“ und die Annotationen „(häufig) unzuverlässiger“, sodass Nutzer:innen sich nicht darauf verlassen könnten, dass alle ambigen Fälle markiert sind; und die Repräsentation wäre über mehrere Ebenen hinweg aufwändig. | S. 109 bis 110, Abschnitt 7 | Argument der Autor:innen |
| Ambige Kompositakandidaten bleiben über POS plus Morphologie gezielt suchbar; Nutzerbeiträge zu solchen Prüfungen unterstützen die Korpusarchitekturen noch nicht. | S. 110 | Einschätzung |
| Lateinische Vorlagen ahd. Paralleltexte werden mit demselben Tagset voll annotiert, ergänzt um VVINFG und VVPG. | S. 108, Abschnitt 6 | Richtlinie |
| **Keine Angaben zu Inter-Annotator-Agreement oder Taggergenauigkeit.** Der Artikel enthält keine Evaluation. | ganzer Text gelesen; Suche nach „%“, „Übereinstimm“, „Tagger“, „Annotator“ | Befund dieser Prüfung |

## Daten, Methode, Zahlen

- **Korpusgrößen** (Anm. 2, S. 85): Referenzkorpus Altdeutsch 750 bis 1050, gesamte ahd. und as. Überlieferung, 650.000 Belege; Referenzkorpus Mittelhochdeutsch 1050 bis 1350, etwa 2,1 Mio. annotierte Wortformen; Referenzkorpus Frühneuhochdeutsch 1350 bis 1650, etwa 4,4 Mio. Alle mit Metadaten, Lemma, Morphologie und Wortart annotiert (Stand 2013, teils geplant: „sind bzw. werden“).
- **MiGraKo** (Korpus der neuen Mhd. Grammatik, in Bonn tokenisiert, lemmatisiert, morphologisch annotiert; künftig separater Teil des ReM, S. 86, Anm. 3): Pronominaladverbien mit *dâ(r)* in Distanzstellung 10,6 % (= 783 Belege) (S. 102).
- **Tagset:** 12 Hauptgruppen im Anhang II (ADJ, AP, AV, CARD, D/P, KO, N, PAV, PTK, V, ITJ/FM, $) (S. 114). Anhang III listet die Beleg-Tags alphabetisch (S. 136 bis 137); eigene Zählung: 84 Einträge. Der Artikel nennt selbst keine Gesamtzahl. Eine eigene Liste der Lemma-Tags gibt es nicht; sie erscheinen nur links von „>“ in den Tabellen.
- **Aufbau der Tabellen:** zuerst „Normalfälle“ mit gleicher Haupt-Wortart von Lemma und Beleg (ADJ > ADJA), dann abweichende Lemma-Wortart (VVPP > ADJA), dann abweichende Beleg-Wortart (ADJ > AVD) (S. 114).
- **Beispielformen:** mhd. Beispiele handschriftennah, meist aus MiGraKo (S. 86).
- **Annotator:innen, Ablauf, Übereinstimmung:** nicht beschrieben.
- **Unstimmigkeit im Werk:** Die Tabelle in 5.1 (S. 104, am Seitenbild geprüft) nennt als STTS-Entsprechung für prädikative Adjektive „ADJA, präd. oder adv. Adjektiv“; Anhang II (S. 116) nennt für denselben Fall ADJD. Die Kurzbeschreibung passt zu ADJD.

## Wörtliche Stellen

> „Da die muttersprachliche Intuition für die älteren Sprachstufen grundsätzlich fehlt, können die Annotatoren z.B. keine linguistischen Tests durchführen. An die Stelle von Tests tritt daher in der historischen Sprachwissenschaft die Synopse und statistische Analyse möglichst vieler Belege entsprechender oder alternativer Konstruktionen.“ (S. 86)

> „In HiTS wird die Wortart einer jeden Wortform zweifach annotiert, und zwar zum einen mit Blick auf das Lemma und zum anderen mit Blick auf den konkreten Beleg, also der Verwendung einer Wortform in einem spezifischen Kontext.“ (S. 92)

> „Zum einen würde dadurch die Annotationsaufgabe deutlich komplexer und die resultierenden Annotationen (häufig) unzuverlässiger, so dass die Korpusnutzer sich letztlich nicht darauf verlassen könnten, dass tatsächlich alle ambigen Fälle als solche annotiert sind.“ (S. 109)

> „Dann bleiben unsicherere Anhaltspunkte: die Syntax (kongruierendes Attribut oder Bezugswort mit Genitivattribut) und die Semantik (‘gut, Gutes’ oder ‘Gutes; Besitz, Güte, gute Absicht’).“ (S. 107)

## Bezug zur Dissertation

- **PROTOKOLL §3, Wortartregel (Lexikon, sonst Token):** HiTS trennt genau die beiden Ebenen, die die Regel nacheinander abfragt. Schritt 1 (eine Wortart in `lexicon.xml`) entspricht der Lemma-Wortart, Schritt 2 (eindeutiges Token-`@pos`) der Beleg-Wortart. HiTS behandelt die Abweichung zwischen beiden als Information, nicht als Fehler (S. 92 bis 95). Folge für das Protokoll: Die Schichtungsvariable „Wortart“ mischt zwei Ebenen. Dass das Manifest die Herkunft der Wortart mitführt (§4.9), ist dafür die richtige Vorkehrung; in der Begründung von §3 lässt sich HiTS als Beleg zitieren, dass Lemma- und Beleg-Wortart legitimerweise auseinanderfallen (z. B. ADJ > AVD, VVINF > NA, S. 105, 128). Ob das MHDBDB-Token-`@pos` als Beleg-Wortart im Sinne von HiTS gemeint ist, sagt HiTS nicht und sagt die MHDBDB-Dokumentation nach `knowledge/data.md` auch nicht.
- **Mehrwertiges Token-`@pos` (`knowledge/data.md`, Abschnitt 1 und 3; Beispiel *guot* `NOM ADJ ADV`):** HiTS vergibt pro Ebene genau ein Tag und lehnt das Offenlassen von Ambiguität ausdrücklich ab (S. 109 bis 110). Die mehrwertigen MHDBDB-Werte haben in HiTS keine Entsprechung. Das stützt den Ausschluss mehrdeutiger Tokens in §3, Schritt 3.
- **`knowledge/data.md` B10 (*guot*, Sense „Besitz“ mit ADJ-Tokens):** HiTS S. 107 nennt *guot* ausdrücklich als Stamm, bei dem Adjektiv und Substantiv oft nur über die Semantik zu trennen sind, mit ‘Besitz’ als Kennzeichen der substantivischen Lesart. Wo die Wortart eines Tokens so entschieden wurde, hängt sie von der Bedeutung ab. Für die Schichtung heißt das: Bei solchen Lemmata ist die Token-Wortart kein von der Bedeutung unabhängiges Merkmal. Das betrifft vor allem Paare, deren Wortart aus Schritt 2 stammt.
- **PROTOKOLL §6, Status `MEHRERE`:** HiTS ist ein gewichtiges Gegenargument gegen das Markieren von Ambiguität, allerdings für Wortarten: unzuverlässiger, aufwändiger, und Nutzer:innen könnten sich nicht auf Vollständigkeit verlassen (S. 109). Das Protokoll entscheidet für Senses anders; die Richtlinien sollten diesen Einwand nennen und beantworten (etwa: `MEHRERE` wird mit α-MASI gemessen statt vorausgesetzt, §9.1). HiTS bietet zugleich ein Muster für eine Entscheidungsregel bei Unentscheidbarkeit (ältere Lesart; bei *dehein* Zusammenlegen, S. 124). Ob sich daraus eine Regel für Senses ableiten lässt, ist eine Entscheidung für die Richtlinien, keine Aussage des Werks.
- **`goldstandard/LITERATUR-IAA.md`, Abschnitt „Historische Sprachen“:** Die dort mit ○ geführte Aussage „HiTS ersetzt Intuition durch Belegsynopse und markiert unauflösbare Ambiguität bewusst nicht“ ist am Volltext belegt (S. 86, 109 bis 110). Eine IAA-Zahl liefert HiTS nicht.
- **PROTOKOLL §3, Ausschluss von PRP und ADV:** HiTS zeigt, wie stark gerade Adverbien, Partikeln und Pronominaladverbien im Mhd. zwischen Kategorien wechseln (S. 90 bis 95, 102 bis 104). Das stützt indirekt die Entscheidung, sie aus der WSD-Zielmenge zu nehmen; HiTS selbst sagt dazu nichts.

## Grenzen und Einwände

- Ein Tagset-Dokument, keine Evaluationsstudie: keine IAA, keine Taggergenauigkeit, keine Fehleranalyse. Für Zahlen zur Verlässlichkeit von HiTS-Annotation müssen andere Quellen herangezogen werden.
- Die Ablehnung der Ambiguitätsmarkierung ist für Wortarten begründet und mit Repräsentationsproblemen über mehrere Ebenen verknüpft (Token, POS, Morphologie, S. 109 bis 110). Für eine Sense-Wahl auf einer einzigen Ebene trägt das zweite Argument weniger; das erste (Zuverlässigkeit) gilt auch dort.
- Schwerpunkt auf Determinativen, Pronomen, Adjektiven und Tokenisierung; Nomen und Verben werden nur in den Tabellen behandelt (S. 128, 132 bis 133).
- Korpuszahlen von 2013 sind Planungsstände („sind bzw. werden“, S. 85); spätere Quellen nennen andere Größen (z. B. Beck & Köllner 2023: ReM 2,3 Mio. Wörter).
- Bezug auf MHDBDB: HiTS wird in der MHDBDB nicht verwendet; die MHDBDB-Tags (NOM, VRB, ADJ usw.) sind ein anderes Inventar. Übertragbar ist das Prinzip der zwei Ebenen, nicht das Tagset.

## Weiterführend

- Schiller, Teufel, Stöckert & Thielen 1999, STTS-Richtlinien (zitiert passim, Literatur S. 113; liegt als `pdf/Schiller-etal-1999-STTS.pdf` vor).
- Splett 1993, Althochdeutsches Wörterbuch, als Referenz für die Beleg-Wortart bei Partikelverben (S. 94, 113).
- Lexer 1872 bis 1878 als Referenz für die Klassifikation mhd. Adverbien (S. 103, 113).
- Für eine IAA zu HiTS-Annotationen im ReM wäre das ReM-Handbuch (Klein & Dipper 2016, bereits zusammengefasst) bzw. spätere Tagger-Arbeiten zu prüfen; HiTS selbst verweist auf keine.

## Julias Markierungen im PDF

Für dieses PDF gibt es keine Datei `md/…markierungen.md`.
