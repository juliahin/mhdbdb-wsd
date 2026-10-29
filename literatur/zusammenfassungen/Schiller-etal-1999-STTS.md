# Schiller et al. 1999: Guidelines für das Tagging deutscher Textcorpora mit STTS

**Datei:** `pdf/Schiller-etal-1999-STTS.pdf` (nur lokal; 87 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29. Kapitel 1 und 2 vollständig, aus Kapitel 3 die Abschnitte mit Zuordnungsregeln und Problemfällen gelesen (3.1, 3.2.2 bis 3.2.3, 3.5, 3.6 Einleitung und 3.6.4, 3.7, 3.8.3 bis 3.8.4, 3.10.3), Tabellen und Zahlen am Seitenbild geprüft. Priorität 3 (Hintergrund), daher knapp und ohne Nacherzählung des Tagsets.

**Seitenzählung:** gedruckte Seite = PDF-Seite − 1 (PDF 4 = S. 3, Einleitung; PDF 5 = S. 4). Titelblatt und Inhaltsverzeichnis (PDF 1 bis 3) ohne Seitenzahl. Unten stehen gedruckte Seiten. **Achtung:** Die Textebene des PDFs enthält keine Ziffern (Bitmap-Schriften aus dvips); Zahlen und Jahresangaben sind deshalb nur am Seitenbild oder in der Docling-Fassung (OCR) lesbar, hier alle am Seitenbild geprüft.

## Bibliografie

- **Vollständig:** Schiller, Anne, Simone Teufel, Christine Stöckert & Christine Thielen (1999). *Guidelines für das Tagging deutscher Textcorpora mit STTS (Kleines und großes Tagset)*. Universität Stuttgart, Institut für maschinelle Sprachverarbeitung, und Universität Tübingen, Seminar für Sprachwissenschaft. August 1999. Technischer Bericht ohne Reihe und Nummer.
- **Jahr und Fassung geklärt (2026-10-29):** Titelblatt (PDF 1, Seitenbild) und Fußzeile jeder Seite: „August 1999“; Einleitung S. 3: „Der jetzige Stand wurde nach wiederholter Diskussion im August 1999 am IMS festgelegt.“ Die IMS-Seite „German Tagsets“ (https://www.ims.uni-stuttgart.de/forschung/ressourcen/lexika/germantagsets/, abgerufen 2026-10-29) führt zwei Fassungen: „Guidelines, version 1995“ und „version 1999“. Die Fassung 1995 (https://www.ims.uni-stuttgart.de/documents/ressourcen/lexika/tagsets/stts-1995.pdf, abgerufen und angesehen) ist ein anderes Dokument: „Vorläufige Guidelines für das Tagging deutscher Textcorpora mit STTS“, dieselben vier Personen, „Draft“, 14. November 1995, 74 Seiten. Das lokale PDF ist **byte-gleich** (SHA-256) mit https://hinrichs.sfs.uni-tuebingen.de/files/tbs/stts-1999.pdf (verlinkt von der TüBa-D/Z-Releaseseite der Universität Tübingen). Die IMS-Datei `stts-1999.pdf` ist nicht byte-gleich (anderer PDF-Erzeuger), hat aber dieselben 87 Seiten und dasselbe Satzbild (Titelblatt und S. 5 verglichen).
- **Autorenreihenfolge:** Titelblatt Schiller, Teufel, Stöckert, Thielen; die Fußzeile schreibt „Schiller/Teufel/Thielen/Stöckert“ (z. B. S. 5). Zitiert wird nach dem Titelblatt.
- **Achtung beim Zitieren über Dritte:** Telljohann et al. 2004 und das TüBa-D/Z-Stylebook 2017 zitieren STTS als „Schiller, Teufel & Thielen 1995, Guidelines für das Tagging deutscher Textkorpora mit STTS“, also drei Personen, Jahr 1995 und ohne „Vorläufige“. Das passt zu keiner der beiden Fassungen genau.
- **DOI/URL:** keine DOI. https://www.ims.uni-stuttgart.de/documents/ressourcen/lexika/tagsets/stts-1999.pdf (Herausgeberseite); byte-gleiche Kopie in Tübingen siehe oben. Die bisherige URL in `references.txt` (`http://www.sfs.uni-tuebingen.de/resources/stts-1999.pdf`) nicht geprüft und durch die IMS-Adresse ersetzt.
- **Art:** Annotationsrichtlinie (technischer Bericht), nicht begutachtet
- **Sprache:** Deutsch

## Worum es geht

Die Guidelines sind eine Anleitung für die **manuelle** Wortartannotation deutscher Korpora mit dem STTS, das aus der Abstimmung zweier Tagsets des IMS Stuttgart und des SfS Tübingen hervorging, damit Korpusarbeit beider Standorte ohne Anpassung austauschbar ist (S. 3). Kapitel 2 erklärt den hierarchischen Aufbau, die Grundregel der Zuweisung und Sonderfälle; Kapitel 3 beschreibt jedes Tag mit Abgrenzungen, Beispielen, lexikalischen Kategorien und morphologischen Merkmalen. Für viele Grenzfälle geben die Guidelines Tests, Listen oder ausdrücklich semantische Kriterien an. Angaben zu Übereinstimmung, Taggergenauigkeit oder Annotationsablauf enthält das Dokument nicht.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| **Hierarchischer Aufbau:** Die Tags kodieren von links nach rechts zuerst die Hauptwortart, dann die Unterwortart, sodass Nutzer:innen nur auf die Hauptwortarten oder auf feinere Information zugreifen können. | S. 4, 2.1 | Setzung der Richtlinie |
| **11 Hauptwortarten** (Tab. 2.1): N, V, ART, ADJ, P, CARD, ADV, KO, AP, ITJ, PTK; orientiert am „TEI Starter Set Of Grammatical-Annotation Tags“, außer bei Kardinalzahlen und Konjunktionen. | S. 4, 2.1 (Seitenbild) | Setzung |
| **54 Tags**, davon 48 reine POS-Tags und 6 weitere für fremdsprachliches Material (FM), Kompositions-Erstglieder (TRUNC), Nichtwörter (XY) und drei Satzzeichen-Tags. Pronomina sind in 8 Untergruppen geteilt, je nach Funktion substituierend (S), attribuierend (AT) oder adverbial (AV). | S. 5, 2.1 (Seitenbild) | Setzung |
| **Grundregel:** „jede Wortform [erhält] genau ein Tag“; Wortform umfasst auch Ziffern, Satzzeichen, Sonderzeichen, abgetrennte Wortteile. | S. 5, 2.2 | Richtlinie |
| **Unterspezifikation nur auf Merkmalsebene:** Ist einem morphologischen Attribut im Kontext kein eindeutiger Wert zuzuweisen, steht ein Stern (Wertambiguität), z. B. `die/ART:Def.*.Nom.Pl Tiere`. Für die Wortart selbst gibt es keine solche Option. | S. 8, 2.4 | Richtlinie |
| **Großes Tagset:** Zu jedem Tag gibt es neben der Klassifikation (POS) lexikalische Kategorien (LEX) und morphologische Merkmale (MOR); das Dokument spricht vom „erweiterten Tagset“ (S. 9). Beispiel: substantiviertes Adjektiv `der Alte/NN<ADJ`, substantivierter Infinitiv `das Spielen/NN<VINF`. Dass „klein“ die POS-Tags und „groß“ POS plus LEX und MOR meint, ist meine Lesart; eine ausdrückliche Definition fand ich nicht. | S. 9, 2.5.2; S. 13, 3.1.1 | Richtlinie; Zuordnung klein/groß eigene Lesart |
| **Zuweisung nach Verwendung, nicht nach Herkunft:** Substantivierte Adjektive, Partizipien und Infinitive sind NN (S. 11 bis 13); adverbial gebrauchte Partizipien und Adjektive sind ADJD (S. 23); die lexikalische Herkunft hält höchstens die LEX-Kategorie fest. | S. 11 bis 13, 3.1.1; S. 23, 3.2.2 | Richtlinie |
| **Mehrwortlexeme** können „aus technischen Gründen“ nicht als Ganzes getaggt werden, auch kontrahierte Formen nicht mit mehreren Tags; die Teile werden getaggt, als stünden sie einzeln (`New/NE York/NE`, `zum/APPRART`). Wo ein gemeinsames Tag ideal wäre, markieren die Guidelines das mit `ml:`. | S. 9, 2.5.1 | Richtlinie, als Kompromiss benannt |
| **Fehler im Text** werden korrigiert und so getaggt, wie die richtige Form aussähe; Änderungen werden dokumentiert; ist die Satzstruktur nicht mehr erkennbar, wird der Artikel nicht verwendet. | S. 10, 2.5.3 | Richtlinie |
| **NN gegen NE:** Bei Einzelwortformen gilt ein „semantisches Kriterium. Namenssemantik“; ein möglicher indefiniter Artikel spricht für NN. | S. 12, 3.1.1 | Richtlinie |
| **ADJD gegen VVPP** ist ausdrücklich ein Problemfall: Passivpartizipien lassen je nach Kontext eine adjektivische Lesart zu. Drei Tests: Aktivierung bei gleicher Semantik (dann VVPP), *von*-PP oder ähnliche PP als Hinweis auf Verbsemantik (VVPP), Ersetzung durch ein „semantisch nahes Adjektiv“ (ADJD). Meist müsse „der weitere Kontext (satzübergreifend)“ herangezogen werden (*er hat die Haare kurz geschnitten*: Friseur oder Frisur). | S. 24 bis 25, 3.2.3 | Richtlinie |
| **Mehrdeutigkeiten bei Artikel und Pronomen** sind eigens aufgelistet: ART/PDS/PDAT/PRELS/PRELAT bei *der, das, dessen, deren* und ART/PIS/CARD/ADJA bei *ein*. | S. 33, 3.5.1 | Richtlinie mit Beispielen |
| **Indefinitpronomen:** Für zahlreiche Formen listen die Guidelines, ob sie nur PIS, nur PIAT, nur PIDAT oder je nach Kontext zwei bis drei Analysen erhalten, dazu ADV als vierte Möglichkeit (*bißchen, etwas, mehr, viel, wenig* …). Test für PIS/ADV: Ersetzung durch *nichts* (PIS) oder *nicht* (ADV). | S. 42 bis 44, 3.6.4 | Richtlinie |
| **ADV gegen ADJD** ist „in einigen Fällen problematisch“, wo adverbiale und prädikative Lesart homonym sind, „ihre Semantik aber verschiedene Lexikoneinträge rechtfertigt“. Kriterium teils „listenbasiert“, teils ausdrücklich ein „Semantisches Kriterium“ (*früher, eben, gerade, natürlich, endlich, rund, weit, ganz, sicher, voll*). ADV ist eng definiert: nur reine, nicht von Adjektiven abgeleitete, nicht flektierbare Modifizierer; adverbial gebrauchte Adjektive sind ADJD. | S. 56 bis 58, 3.7 | Richtlinie |
| **KOKOM gegen KOUS:** Eine semantische Unterteilung von *wie* und *als* wäre möglich, aber „Da diese semantischen Unterscheidungen vage sind“, trifft das Tagset nur die syntaktischen; *wie* und *als* haben je drei Analysen. | S. 62, 3.8.4 | Begründete Entscheidung der Richtlinie |
| **PTKVZ gegen ADV** bei mehreren Partikeln: Präfixverb lexikalisiert (PTKVZ) oder nicht (ADV), sonst Topikalisierungstest. | S. 71, 3.10.3 | Richtlinie |
| **Keine Evaluation:** keine Übereinstimmungswerte, keine Taggergenauigkeit, keine Angaben zu Annotator:innen oder Ablauf. | ganzes Dokument durchgesehen (Inhaltsverzeichnis, Kap. 1 bis 2, Problemabschnitte in Kap. 3) | Befund dieser Prüfung |

## Daten, Methode, Zahlen

- Inventar: 11 Hauptwortarten, 54 Tags (48 POS plus 6), Pronomina in 8 Untergruppen (S. 4 bis 5, Seitenbild).
- Morphologische Attribute (Tab. S. 8): Genus, Kasus, Numerus, Flexion, Grad, Person, Tempus, Modus, Definitheit; Sonderwerte `*` (Wertambiguität) und `_` (Attribut nicht vorhanden oder nicht werttragend).
- Format: eine Wortform pro Zeile, für manuelles Taggen vorbereitet (S. 5).
- Quellen der Terminologie: Bußmann 1990, Duden-Grammatik, Helbig & Buscha 1991, TEI 1991 (Literaturverzeichnis S. 86).
- Kein Korpus, keine Annotator:innen, keine Maße.

## Wörtliche Stellen

> „Als allgemeine Regel gilt, daß jede Wortform genau ein Tag erhält.“ (S. 5)

> „Die Entscheidung, ob ein Adverb oder ein adverbial verwendetes Adjektiv vorliegt, ist in einigen Fällen problematisch, nämlich in den Grenzfällen, bei denen adverbiale und prädikative Lesarten zwar homonym sind, ihre Semantik aber verschiedene Lexikoneinträge rechtfertigt.“ (S. 57)

> „Da diese semantischen Unterscheidungen vage sind, treffen wir im jetzigen Tagset nur die syntaktischen.“ (S. 62)

## Bezug zur Dissertation

- **Verhältnis zu HiTS:** HiTS übernimmt den hierarchischen Aufbau des STTS und begründet seine Abweichungen dagegen (Zusammenfassung `Dipper-etal-2013-HiTS.md`, Kernaussagen zu S. 85). Am STTS selbst lässt sich ergänzen, wogegen HiTS sich absetzt: STTS taggt **nur die Verwendung** im Kontext (NN für *der Alte*, ADJD für adverbiale Adjektive) und hält die lexikalische Herkunft allenfalls in der LEX-Kategorie fest (S. 11 bis 13). Die HiTS-Doppelannotation (Lemma- und Beleg-Wortart) macht aus dieser Nebeninformation eine eigene Ebene. Das ist meine Einordnung, keine Aussage eines der beiden Werke.
- **PROTOKOLL §3, Wortartregel, Schritt 2 (Token-`@pos`):** STTS-Wortarten sind Beleg-Wortarten, und einige Abgrenzungen hängen ausdrücklich an der Bedeutung (NN/NE: Namenssemantik, S. 12; ADV/ADJD: semantisches Kriterium und getrennte Lexikoneinträge, S. 57; ADJD/VVPP: semantisch nahes Adjektiv, S. 24). Das stützt den Befund `knowledge/data.md` B10 und die Folgerung aus HiTS: Wo die Token-Wortart so entschieden wurde, ist sie kein von der Bedeutung unabhängiges Schichtungsmerkmal. Ob die MHDBDB-Annotator:innen ähnlich entschieden haben, ist undokumentiert.
- **MHDBDB-Tagset (`docs/POS-TAGSET.md` §1 bis §4):** Die 19 MHDBDB-Tags liegen der Körnung nach näher an den 11 STTS-Hauptwortarten als an den 54 Tags. Drei Stellen decken sich mit Problemfällen, die STTS selbst benennt:
  - Der häufigste MHDBDB-Doppelwert `ADJ ADV` (304.069 Tokens, POS-TAGSET §4) ist genau der Grenzfall ADV/ADJD aus 3.7.2. STTS entscheidet ihn per Liste und semantischem Kriterium, die MHDBDB lässt ihn im Altbestand offen.
  - Unterschiedliche Prinzipien bei ADV: STTS zählt adverbial gebrauchte Adjektive zu ADJD, also zum Adjektiv (S. 23, 56); die MHDBDB führt *schône* als Beispiel für ADV (POS-TAGSET §1). Die Schicht „ADJ“ in PROTOKOLL §4.3 ist deshalb nicht ohne Weiteres mit STTS-annotierten deutschen Vergleichsdaten vergleichbar (eigene Folgerung).
  - Substantivierte Adjektive: STTS taggt sie immer NN und vermerkt ADJ nur als LEX (S. 13); die MHDBDB-Entscheidung von KZW (POS-TAGSET §2) taggt eindeutig nominalen Gebrauch NOM und behält `ADJ NOM` mit `@reason` für unentscheidbare Fälle. STTS kennt diese dritte Möglichkeit nicht.
- **PROTOKOLL §6, Status `MEHRERE`:** STTS erlaubt Unterspezifikation nur bei morphologischen Merkmalen (`*`, S. 8), nicht bei der Wortart. Zusammen mit HiTS (S. 109 bis 110 dort) ist das ein zweites Tagset, das für die Hauptkategorie eine Entscheidung erzwingt. Anders als HiTS begründet STTS das nicht. Die Gegenposition mit ausdrücklich unterspezifizierten Labels findet sich in der TüBa-D/Z (Zusammenfassung `Telljohann-etal-2004-TueBa-DZ.md`).
- **PROTOKOLL §5 und §9.1 Punkt 7 (grobe Ebene):** Die Begründung zu KOKOM (S. 62), vage semantische Unterscheidungen nicht zu treffen und nur operationalisierbare zu annotieren, ist ein Präzedenzfall für die Wahl einer gröberen Ebene, wenn feine Unterscheidungen unsicher sind. Das betrifft Wortarten, nicht Senses; als Analogie, nicht als Beleg verwenden.

## Grenzen und Einwände

- Richtlinie für Gegenwartsdeutsch (Beispiele aus Zeitungssprache und Alltagssprache); für das Mittelhochdeutsche ist HiTS die einschlägige Anpassung.
- Keine Evaluation, kein Korpus, keine Angaben zur Verlässlichkeit der Annotation nach diesen Richtlinien.
- Viele Zuordnungen sind listenbasiert; die Listen sind ausdrücklich unvollständig („Beispielliste einiger“, S. 25; „Liste einiger Adverbien“, S. 58).
- Zitierproblem: Folgewerke zitieren eine Fassung „1995“ mit drei Autor:innen, die es so nicht gibt (siehe Bibliografie). Für die Dissertation die Fassung 1999 nach dem Titelblatt zitieren.
- Nicht gelesen: die Abschnitte zu Verben (3.4), Zahlen (3.3), Präpositionen (3.9), Interpunktion und Sonstigem (3.11 bis 3.12) sowie der Index (S. 77 bis 85); sie enthalten Tagbeschreibungen ohne eigens benannte Problemfälle.

## Weiterführend

- Schiller, Teufel, Stöckert & Thielen 1995, „Vorläufige Guidelines“ (Draft, IMS-Seite), falls die Fassung zitiert werden muss, auf die sich TüBa-D/Z beruft.
- Die Modifikationen des STTS (Zürich 2000, TIGER 2001/2003) und die STTS-Workshops 2012 und 2013 nennt die IMS-Seite (abgerufen 2026-10-29), nicht das PDF.

## Julias Markierungen im PDF

Für dieses PDF gibt es keine Datei `md/…markierungen.md`; `markierungen.py` fand am 2026-10-29 keine Anmerkungen.
