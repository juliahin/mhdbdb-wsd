# Klein & Dipper 2016: Handbuch zum Referenzkorpus Mittelhochdeutsch

**Datei:** `pdf/Klein-Dipper-2016-Handbuch-ReM.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->

**Stand:** 2026-10-28, PDF vollständig gelesen (Textebene und Seitenbilder, auch Abbildung S. 3 und Tabelle S. 6); Bibliografie am PDF und per Websuche geprüft.

**Seitenzählung:** Zitiert wird die gedruckte Seitenzahl. Gedruckte Seite = PDF-Seite minus 3
(Titelei ohne Zählung, Inhaltsverzeichnis = gedruckte S. 1 = PDF-Seite 4).

## Bibliografie

- **Vollständig:** Klein, Thomas & Dipper, Stefanie, 2016. Handbuch zum Referenzkorpus Mittelhochdeutsch. *Bochumer Linguistische Arbeitsberichte* 19. Bochum: Sprachwissenschaftliches Institut, Ruhr-Universität Bochum. ISSN 2190-0949. 20 gezählte Seiten (23 PDF-Seiten). Band 19, „December 2016" (PDF-Seite 2).
- **DOI/URL:** Kein DOI im PDF. Nachweis im Repositorium der UB Frankfurt, docId 44044 (`https://publikationen.ub.uni-frankfurt.de/frontdoor/index/index/year/2017/docId/44044`); laut Suchergebnis dort Arbeitspapier, 23 S., online März 2017 (○, Seite selbst wegen Bot-Schutz nicht abrufbar). Die URL in `references.txt` (`linguistics.rub.de/forschung/arbeitsberichte/19.pdf`) ließ sich am 2026-10-28 nicht abrufen (Verbindungsabbruch).
- **Art:** Arbeitsbericht / Korpushandbuch (graue Literatur, nicht begutachtet). Das Handbuch beruht „großenteils" auf dem Bonner Korpushandbuch des Projekts „Mhd. Grammatik", im Wesentlichen von Tobias Kemper (S. 2).
- **Sprache:** Deutsch
- **Zitierweise des Korpus selbst** (getrennt vom Handbuch, S. 2): Klein, Thomas; Wegera, Klaus-Peter; Dipper, Stefanie; Wich-Reif, Claudia (2016). Referenzkorpus Mittelhochdeutsch (1050–1350), Version 1.0. ISLRN 332-536-136-099-5. Lizenz CC BY-SA 4.0.

## Worum es geht

Das Handbuch beschreibt, woraus das Referenzkorpus Mittelhochdeutsch (ReM) besteht und wie es
annotiert ist: Herkunft der vier Teilkorpora, Struktur nach Zeit, Sprachraum und Textart,
Transkription, Tokenisierung, Interpunktion, Lemmatisierung, Wortart und Flexion sowie den
Korrekturstand. Es ist eine Dokumentation, keine Studie: Es gibt keine Evaluation, keine
gemessene Annotationsqualität und keine Inter-Annotator-Übereinstimmung. Eine
Bedeutungsannotation (Senses, Begriffe) kommt in der Aufzählung der Annotationsebenen nicht vor
(S. 7) und wird nirgends im Handbuch erwähnt.

## Kernaussagen

Alles hier ist Selbstbeschreibung des Korpus durch die Projektbeteiligten; „eigenes Ergebnis"
heißt in dieser Tabelle: Angabe des Handbuchs über das eigene Korpus.

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| ReM im weiteren Sinne vereint vier Korpora: Kölner Korpus hessisch-thüringischer Texte, Bonner Korpus mitteldeutscher Texte, BoMiKo/MiGraKo und eReM. | S. 2 bis 4, Abschn. 2 | eigene Angabe |
| Alle Teilkorpora wurden mit einem von Thomas Klein ab 1986 entwickelten Programmpaket halbautomatisch annotiert. | S. 2; S. 8, Abschn. 4.2 | eigene Angabe |
| MiGraKo ist strukturiert: 50-Jahres-Abschnitte (Frühzeit 1050 bis 1150 zusammengefasst), 7 (9) Sprachräume, Textart Vers / Prosa / Urkunde; strenge Bedingungen für die Textauswahl. | S. 3, Abschn. 2.3 und Abbildung S. 3 | eigene Angabe |
| eReM (DFG-Projekt 2009 bis 2014, Bonn und Bochum) ergänzt MiGraKo um möglichst alle frühmittelhochdeutschen Texte und um zuordnungssichere Texte 1200 bis 1350. | S. 4, Abschn. 2.4 | eigene Angabe |
| Texte in eReM sind „in aller Regel" komplett erfasst; nur bei sechs Großtexten wurden zusätzliche Ausschnitte zu den MiGraKo-Ausschnitten bearbeitet, sodass der annotierte Teil komplettiert oder „auf wenigstens 20.000 Tokens vergrößert" wurde. | S. 4, Abschn. 2.4 (1) | eigene Angabe |
| eReM ist „für sich genommen kein strukturiertes Korpus wie MiGraKo"; es dient zur Erweiterung von MiGraKo und zu nahezu flächendeckender Recherche im Frühmittelhochdeutschen. | S. 5 | eigene Angabe |
| Die Annotation ist „rein tokenbezogen". Pro Token: Lemma, Wortart, Flexionsklasse, Flexion, normalmittelhochdeutsche Normalform, teils graphophonemische Analyse, Stellenreferenz. | S. 7, Abschn. 4.1 | eigene Angabe |
| Neu im ReM-Projekt und mit HiTS eingeführt: Trennung von allgemeinem Lemma und Wortart (`lemmaLemma`, `posLemma`) und belegspezifischem Lemma und Wortart (`lemma`, `pos`); für MiGraKo und die Köln-Bonner Texte nachgerüstet. | S. 7 bis 8, Abschn. 4.1; S. 12, Abschn. 7.1; S. 16, Abschn. 8.2 | eigene Angabe |
| Verfahren: Den Wortformen werden automatisch Vorschläge zu Lemma und Grammatik zugeordnet, „nach einer statistischen Gewichtung geordnet"; manuell wird geprüft, ob das „Präferenzangebot" zutrifft. | S. 8, Abschn. 4.2 | eigene Angabe |
| Die HiTS-Tags entstanden erst sekundär, für den ANNIS-Import, durch ein heuristisches Skript aus dem internen Tagset; einige Tags ohne HiTS-Entsprechung blieben unüberführt. | S. 8 bis 9, Abschn. 4.2 | eigene Angabe |
| Lemmaansätze richten sich „meist" nach Lexers Handwörterbuch, mit dokumentierten Abweichungen (konsequente Segmentierung, frühmittelhochdeutscher Lautstand, ‹è› für Umlaut-e, Ansatz ohne Auslautverhärtung, Zusammenfassung von Varianten durch Klammern). | S. 12 bis 14, Abschn. 7.1 bis 7.3 | eigene Angabe |
| Lateinisches ist als `FM` markiert; die Regelung zur Lemmatisierung in rein lateinischem Kontext ist in eReM „nur sehr unsystematisch" durchgeführt. | S. 15, Abschn. 7.6 | eigene Angabe |
| Fehlerquelle des Verfahrens: Bei der ersten manuellen Korrektur werden Fehler im Präferenzangebot „leicht übersehen"; daher mindestens eine Abschlusskorrektur. MiGraKo oft zweimal nachkorrigiert; manche eReM-Texte ohne Abschlusskorrektur, erkennbar an „N0"/„G0" im Dokumentnamen und leerem Feld `proofreading_by`. | S. 20, Abschn. 9 | eigene Angabe |
| Transkription in der Regel nach Handschriftenabbildungen, teils nur nach Abdrucken des 19. Jh.; vermerkt in `notes-transcription`. | S. 7, Abschn. 3 | eigene Angabe |

## Daten, Methode, Zahlen

- **Zeitraum:** 1050 bis 1350 (Korpustitel, S. 2 und S. 4).
- **Kölner Teilkorpus:** 11 Texte, 176.289 Tokens, 1986 bis 1993 digitalisiert (S. 2).
- **Bonner Teilkorpus:** 39 Texte, 260.470 Tokens, ab 1993 (S. 2 bis 3).
- **MiGraKo:** 102 Texte, „ca. 1 Mio. Wortformen"; 1997 bis 1999 transkribiert, in Bonn komplett tokenisiert, lemmatisiert, grammatisch annotiert (S. 3).
- **Gruppentabelle MiGraKo / eReM in ANNIS** (S. 6, am Seitenbild geprüft): Gruppen nach Zeitraum, Sprachraum, Textart. Eine Gesamtgröße von ReM oder eReM nennt das Handbuch **nicht**. Eigene Summe aus der Tabelle (nicht im Text, vom Agenten nachgerechnet): MiGraKo-Gruppen 1.117.705 Tokens in 103 Dokumenten (der Fließtext S. 3 nennt 102 Texte), eReM-Gruppen 1.020.419 Tokens in 289 Dokumenten. Die Dokumentzahl ist nicht gleich Textzahl: Große Verstexte sind in ANNIS geteilt (Kaiserchronik und Herborts „Liet von Troye" in je zwei Teiltexte, S. 5). Ob die Tabelle `tok_anno` oder `tok_dipl` zählt, sagt das Handbuch nicht.
- **Prosakorpus mittleren Umfangs** aus MiGraKo plus eReM-Erweiterungen: neun Texte zwischen 17.718 und 29.742 Tokens (Tabelle S. 4 bis 5, am Seitenbild geprüft).
- **Tokenisierung:** zwei Ebenen, `tok_dipl` (handschriftlich) und `tok_anno` (modern); Lemma und Wortart hängen an `tok_anno`, die Stellenreferenz an `tok_dipl`; Differenzen als MS/US/UL/ML kodiert, Klitika eigene Tokens (S. 9 bis 10, Abschn. 5).
- **Wortart:** Tagset HiTS auf Belegebene, Tabelle der Tags S. 16 bis 18 (u. a. `NA` Nomen appellativum, `NE` Eigenname, `ADJA`/`ADJD`/`ADJN`/`ADJS`, `VVFIN` usw.); Lemma-Ebene „im Allgemeinen gekürzte Varianten" (S. 16).
- **Unterspezifikation:** Modus, Genus und Flexionsklasse werden nur angegeben, wo die Wortform sie eindeutig zeigt (S. 18 bis 19, Abschn. 8.2 bis 8.3).
- **Annotator:innen, Übereinstimmung:** Das Handbuch nennt keine Zahl der Annotator:innen pro Text und berichtet keine Inter-Annotator-Übereinstimmung und keine Fehlerrate. Qualität wird über Korrekturdurchgänge beschrieben (S. 20).

## Wörtliche Stellen

> „Die Annotation ist rein tokenbezogen." (S. 7)

> „In aller Regel sind die Texte komplett erfasst und annotiert worden." (S. 4)

> „eReM ist also für sich genommen kein strukturiertes Korpus wie MiGraKo." (S. 5)

> „[…] dass bei der (ersten) manuellen Korrektur einzelne Fehler im Präferenzangebot leicht übersehen werden" (S. 20)

## Bezug zur Dissertation

- **Protokoll 4.4, Punkt 4 (Obergrenze pro Text) und `LITERATUR-STICHPROBE.md`:** Dort steht, ReM nehme große Texte nur in Ausschnitten auf (Stichprobe: „ca. 20.000 Tokens"). Das Handbuch sagt etwas Engeres: eReM-Texte sind „in aller Regel" komplett (S. 4); nur bei sechs Großtexten wurden MiGraKo-Ausschnitte ergänzt, bis der Text komplett ist oder **mindestens** 20.000 Tokens erreicht (S. 4). 20.000 ist also eine Untergrenze, keine Obergrenze. Dass MiGraKo selbst Ausschnitte enthält, setzt der Satz voraus („bereits in MiGraKo enthaltenen Ausschnitten", S. 4); eine Ausschnittsregel für MiGraKo steht im Handbuch nicht. Als Vorbild für die Obergrenze von 3 Items pro Text taugt ReM damit nur eingeschränkt; der eigentliche Grund (Klumpeneffekt) trägt die Regel allein.
- **Protokoll 4 (Schichtung), `LITERATUR-STICHPROBE.md`:** Das 50-Jahres-Raster mit Sprachraum und Textart gilt für MiGraKo (S. 3), nicht für eReM (S. 5). Für die offene Frage nach Datierung und Vers/Prosa als Ausgleichsmerkmal (Protokoll 12, Punkt 9) ist ReM ein Beispiel, das beides pro Text maschinenlesbar führt (Gruppennamen S. 5 bis 6), was der MHDBDB fehlt (Protokoll 4.8).
- **Protokoll 3 (Wortartregel: Lexikon, sonst Token-`@pos`) und `knowledge/data.md` Abschnitt 1:** ReM trennt allgemeine und belegspezifische Wortart ausdrücklich (`posLemma` / `pos`, S. 7 bis 8, S. 16). Das ist dieselbe Unterscheidung, die die MHDBDB implizit hat (Wortart am Lemma in `lexicon.xml`, mehrwertiges Token-`@pos`). Belegstelle für die Begründung, warum die Wortart zweistufig bestimmt wird.
- **Protokoll 6 (Blindheit) und 7 (Ablauf), `LITERATUR-IAA.md` (Vorannotationen verankern):** ReM wurde annotiert, indem Menschen ein statistisch geordnetes Präferenzangebot prüften (S. 8), und das Handbuch benennt selbst, dass Fehler im Präferenzangebot dabei leicht übersehen werden (S. 20). Das ist ein mittelhochdeutsches Beispiel für den Verankerungseffekt, den das Protokoll durch technische Blindheit ausschließt.
- **Protokoll 2 und 9.2 (Silber), `knowledge/data.md` B12 und Abschnitt 3:** ReM dokumentiert den Korrekturstand pro Text (N0/G0 gegenüber N1/G1, `proofreading_by`, S. 20). Für die MHDBDB ist genau das nicht dokumentiert (wer, wann, nach welchen Richtlinien). Der Vergleich macht die Lücke greifbar, sagt aber nichts über die Qualität des MHDBDB-Silbers.
- **Abgrenzung (Protokoll 1, 9.2 „Lücke"):** ReM hat nach diesem Handbuch keine Bedeutungsannotation (S. 7). Es ist daher kein Vergleichsgold für WSD, sondern nur Vergleich für Korpusaufbau, Lemmatisierung und Wortart.

## Grenzen und Einwände

- Handbuch zu Version 1.0 (2016). Laut Projektseite gibt es inzwischen Version 2.1 (Roussel, Klein, Dipper, Wegera, Wich-Reif 2024, ISLRN 937-948-254-174-0; nur über Suchergebnis gesehen, ○). Ob sich Umfang oder Annotation geändert haben, ist mit diesem Handbuch nicht zu beantworten.
- Keine Qualitätsmessung: keine IAA, keine Fehlerquote, nur die qualitative Aussage, dass nicht abschließend korrigierte Texte eine höhere Fehlerrate haben (S. 20).
- Keine Gesamtzahlen für ReM oder eReM im Text; die Summen oben sind aus der Tabelle S. 6 nachgerechnet.
- Die Darstellung ist auf ANNIS ausgerichtet; die vollständigen Annotationen gibt es nur im XML-Export (S. 7). Was in ANNIS fehlt (Kurzkommentare, Pointer bei Partikelverben), steht S. 8 und S. 15.
- Übertragbarkeit auf die MHDBDB: anderes Ziel (Grammatik, Graphematik), anderer Zuschnitt (1050 bis 1350, handschriftennah), normalisierte Lemmata nach Lexer mit eigenen Regeln. Für ein onomasiologisches Inventar gibt das Handbuch nichts her.

## Weiterführend

- Dipper, Donhauser, Klein, Linde, Müller & Wegera 2013, HiTS, *JLCL* 28(1), 85 bis 137 (zitiert S. 8, S. 16; liegt als `pdf/Dipper-etal-2013-HiTS.pdf` vor).
- Klein 1991 und Klein 2001 zum Annotationsverfahren (zitiert S. 2, S. 8).
- Wegera 1991 und 2000 zum Korpusdesign nach Zeit, Sprachraum und Textart (zitiert S. 3): Quelle für die Begründung des Rasters, falls es im Artikel als Vorbild dienen soll.
- ReM Version 2.1 (2024) und deren Dokumentation, falls aktuelle Zahlen gebraucht werden (○).
