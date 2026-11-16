# Passonneau, Habash & Rambow 2006: Inter-annotator Agreement on a Multilingual Semantic Annotation Task

**Datei:** `pdf/Passonneau-etal-2006-IAA-Multilingual-Semantic.pdf` (nur lokal; 6 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Tabellen 1 bis 5 (S. 1953 bis 1955) am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology L06-1391 (SHA-256 verglichen am 2026-11-13); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 1950 + n (PDF 1 = S. 1951, PDF 6 = S. 1956; Seitenzahlen in der Fußzeile). Unten stehen gedruckte Seiten.

**Tabellennummern:** Im Text und in den Bildunterschriften weichen sie voneinander ab. Der Text nennt die WordNet-Tabelle „Table 1“, Mikrokosmos „Table 2“, Theta-Rollen „Table 3“, die Bildunterschriften zählen 2, 3 und 4 (Tab. 1 ist dort das Beispiel *cost*). Unten gelten die Nummern der Bildunterschriften.

## Bibliografie

- **Vollständig:** Passonneau, Rebecca, Nizar Habash & Owen Rambow (2006). Inter-annotator Agreement on a Multilingual Semantic Annotation Task. In: Nicoletta Calzolari, Khalid Choukri, Aldo Gangemi, Bente Maegaard, Joseph Mariani, Jan Odijk & Daniel Tapias (Hg.), *Proceedings of the Fifth International Conference on Language Resources and Evaluation (LREC’06)*. Genua: European Language Resources Association (ELRA), S. 1951 bis 1956.
- **DOI/URL:** keine DOI; https://aclanthology.org/L06-1391/ (Herausgeber:innen, Ort, Verlag, Monat Mai nach dem BibTeX der Anthology, abgerufen 2026-11-13). Seiten nach den Fußzeilen des PDF; ebenso bei Artstein & Poesio (2008, S. 594) und Passonneau et al. (2010, S. 3249).
- **Lizenz:** nicht festgestellt (FAQ der ACL Anthology regelt nur ACL-Material, nicht LREC/ELRA; abgerufen 2026-11-13).
- **Art:** Konferenzbeitrag
- **Sprache:** Englisch

## Worum es geht

Im Projekt IAMTC annotierten bis zu zehn Personen an sechs Standorten englische Übersetzungen von Nachrichtentexten aus sechs Sprachen: Inhaltswörter wurden einem oder mehreren Begriffen der Omega-Ontologie zugeordnet (Teil aus WordNet, Teil aus Mikrokosmos), Verbargumente bekamen Theta-Rollen (S. 1951 bis 1952). Weil Mehrfachwahl erlaubt war, sind die Labels Mengen; gemessen wird mit Krippendorffs α und MASI-Abstand (S. 1953). Bester Bereich ist der WordNet-Teil mit α 0,45 bis 0,66, Mittel 0,58, nach Ausschluss der jeweils schwächsten Person (S. 1953 bis 1954). Die Autoren nutzen die Werte vor allem vergleichend: Lerneffekt im Projektverlauf, Unterschiede zwischen Personen und Wortarten, Verben schwerer (S. 1954 bis 1955).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Aufgabe: Inhaltswörter (Nomen, Verben, Adjektive, Adverbien) in Dependenzbäumen einem oder mehreren Begriffen der Omega-Ontologie (WordNet und Ontosem/Mikrokosmos) zuordnen, Theta-Rollen vergeben. `|DummyConcept|` heißt „kein passender Begriff“; „keine Auswahl“ war möglich. Alle Knoten gingen in die Reliabilität ein, auch die ohne Auswahl. | S. 1951 bis 1952, Abschnitt 2 | eigenes Projekt |
| In Pilotarbeiten seien Übereinstimmungsmaße am besten genutzt, um Tendenzen in den Daten zu erkennen, „rather than to adhere to an absolute agreement threshold“. | S. 1951 | Position der Autoren |
| Kritik am „cookbook approach“: der Annahme, es gebe ein bestes Maß und eine absolute Schwelle unabhängig von Zielen und Bedingungen des Projekts. | S. 1952, Abschnitt 3 | referiert (Di Eugenio 2000; Di Eugenio & Glass 2004) |
| Die Wahl des Maßes soll von Prävalenz und Bias in den Daten abhängen; α wird gewählt, weil es ein Abstandsmaß zulässt, denn ob zwei Codierer übereinstimmen, sei bei mehrteiligen Entscheidungen nicht binär. | S. 1952, Abschnitt 3.1 | referiert (Di Eugenio & Glass 2004), Begründung der Autoren |
| Krippendorff habe 0,67 nur genannt, um die Komplexität zu zeigen, und gegen pauschale Standards argumentiert. In den gemeinten Studien stand 0,67 für „cautious conclusions“, 0,8 für solide Ergebnisse; Signifikanz wurde für Variablen unter 0,70 selten erreicht. Die Frage, was reliabel genug ist, habe „no set answer“; für Daten ohne einzelne Verwendung wie IAMTC gebe es keine einzelne Antwort. | S. 1952 bis 1953, Abschnitt 3.2 | referiert (Krippendorff 1980, S. 146), Deutung der Autoren |
| MASI als Abstand in α: δ = 1 − J·M, zwischen 1 und 0; J ist Jaccard, M eine Vierstufenskala (1 gleich, 2/3 Teilmenge, 1/3 Schnitt mit zwei nicht leeren Differenzen, 0 disjunkt). Beispiel *cost*: neun Personen, fünf wählten {COST}, eine {COST, MONETARY_VALUE}, drei {COST, MONETARY_VALUE, TOLL<VALUE}. | S. 1953, Abschnitt 4, Tab. 1 | eigenes Maß (Verweis auf Passonneau 2006) |
| WordNet-Begriffe: α mit MASI 0,45 bis 0,66, Mittel 0,58, jeweils nach Ausschluss der Person mit der niedrigsten mittleren paarweisen Reliabilität; mit allen Personen im Mittel 0,49. Werte fast immer 0,5 oder höher, also „halfway between chance and perfect agreement or better“. | S. 1953 bis 1954, Tab. 2 | eigenes Ergebnis |
| Mikrokosmos-Begriffe (Mittel 0,36) und Theta-Rollen (Mittel 0,31) liegen deutlich darunter; als Grund vermuten die Autoren den viel höheren Anteil an Knoten ohne Auswahl. | S. 1954, Tab. 3 und 4 | eigenes Ergebnis, Deutung vermutet |
| Lerneffekt: Die Differenz zwischen zwei Übersetzungen desselben Texts ist in der ersten Projektphase groß (Arabisch, Koreanisch bis −0,15) und verschwindet danach fast; die Werte steigen über die Zeit (außer Französisch, dem größten Set). | S. 1954 | eigenes Ergebnis, Deutung als Vermutung |
| Wortarten: Nomen im Mittel 0,60, Verben 0,46 über die zwölf Sets; die Autoren nennen das signifikant (t-Test, angegeben „p=.5“). | S. 1954 | eigenes Ergebnis; die p-Angabe passt nicht zur Aussage „signifikant“ |
| Personen: Für alle Teilgruppen von 2 bis N Personen gerechnet; Tab. 5 nennt die größte Gruppe mit α ≥ 0,70 und den Mittelwert aller Gruppen dieser Größe (0,34 bis 0,57). Reliabilität hängt davon ab, welche Personen man nimmt; später im Projekt müssen weniger ausgeschlossen werden. | S. 1955, Tab. 5 | eigenes Ergebnis |
| Fazit: Absolute Werte sind ohne Kontext (z. B. Signifikanz abgeleiteter Variablen) schwer zu deuten; zum Vergleich entlang von Dimensionen sind absolute Werte und Wahl des Maßes weniger wichtig. Bei komplexen Entscheidungen pro Einheit muss man ein passendes Maß wählen oder entwerfen. | S. 1955, Abschnitt 6 | Position der Autoren |

## Daten, Methode, Zahlen

- **Korpus:** zwölf Dokumentsets, je zwei englische Übersetzungen derselben Texte aus Arabisch, Französisch, Hindi, Japanisch, Koreanisch, Spanisch (S. 1951, 1953 bis 1954); 76 bis 136 lexikalische Knoten pro Set.
- **Annotator:innen:** elf insgesamt an sechs Standorten (CMU, Columbia, ISI, Mitre, NMSU, Maryland), pro Set andere Zusammensetzung; Schulung vor Ort, gemeinsame Anleitung, eigene GUI (S. 1951, 1954). Eine Person war „relatively uncooperative“, eine hatte deutlich mehr Schwierigkeiten (S. 1954).
- **Maß:** Krippendorffs α mit MASI-Abstand, Formel S. 1953; die Tabellen geben die Zahl der Personen nach Ausschluss der schwächsten an („#annotators minus 1“: 6 bis 9).

**Tab. 2, WordNet-Begriffe (S. 1953, am Seitenbild geprüft):**

| Set | Personen − 1 | Knoten | α/MASI (Differenz zum Paar) |
|---|---|---|---|
| Arabic1 / Arabic2 | 6 / 9 | 80 / 97 | 0,66 (−0,15) / 0,51 |
| Korean1 / Korean2 | 9 / 9 | 112 / 92 | 0,50 (−0,15) / 0,45 |
| Japanese1 / Japanese2 | 9 / 9 | 111 / 117 | 0,66 (0,00) / 0,66 |
| Spanish1 / Spanish2 | 8 / 8 | 116 / 124 | 0,60 (0,01) / 0,61 |
| French1 / French2 | 9 / 9 | 130 / 136 | 0,54 (−0,05) / 0,49 |
| Hindi1 / Hindi2 | 8 / 8 | 77 / 76 | 0,61 (−0,02) / 0,63 |
| Mittel | | | 0,58 |

Mikrokosmos (Tab. 3, S. 1954): 0,20 bis 0,48, Mittel 0,36. Theta-Rollen (Tab. 4, S. 1954): 0,16 bis 0,43, Mittel 0,31. Tab. 5 (S. 1955): größte Gruppe mit α ≥ 0,70 zwischen 2 und 7 Personen, α der besten Gruppe 0,70 bis 0,75.

Rohübereinstimmung wird nicht berichtet.

## Wörtliche Stellen

> „[…] in pilot work such as this, agreement measures are best used to identify trends in the data rather than to adhere to an absolute agreement threshold.“ (S. 1951)

> „Ironically, Krippendorff offered the threshold of 0.67 only to exemplify the complexity of the issues, in the context of arguing against “ad hoc” standards, and against applying standards across the board.“ (S. 1952)

> „For set-valued scales, we use MASI for the distance metric δ. It is equal to 1-Jbc*Mbc, and ranges from 1 to 0.“ (S. 1953)

## Bezug zur Dissertation

**1. PROTOKOLL §9.1 Punkt 1 und A8 (α mit MASI).** Das Werk ist die WSD-nächste Anwendung von α mit MASI: Sense-artige Labels (WordNet-Begriffe der Omega-Ontologie) mit erlaubter Mehrfachwahl. Es liefert die Abstandsformel in der Form, die das Protokoll braucht: δ = 1 − J·M (S. 1953). Vorschlag: diese Stelle neben Passonneau 2006 als Formelquelle zitieren.

**2. A32 (Stoppregel mit absoluter Schwelle im Pilot).** Die Autoren vertreten für Pilotarbeit das Gegenteil einer festen Schwelle: Werte zum Erkennen von Tendenzen nutzen (S. 1951), keine pauschalen Standards (S. 1952). Die Herkunft der Zahlen: 0,67 für vorsichtige Schlüsse, 0,8 für solide Ergebnisse, beides aus Studien mit Signifikanztests (S. 1952 bis 1953). Das spricht nicht gegen A32, die Schwelle ist dort als Ende des Nachschärfens definiert und nicht als Gütesiegel; es ist aber ein Einwand, der in der Begründung von A32 genannt werden kann. Eine Literaturstütze für Schwellen als Abbruchkriterium eines Pilots liefert das Werk nicht.

**3. PROTOKOLL §7 (mehrere Pilotrunden).** Der beobachtete Lerneffekt (große Differenzen nur in der ersten Projektphase, S. 1954) stützt, den Pilot über mehrere Runden zu führen und Runde 0 ohne Schwelle zu werten (A32). Die Deutung ist bei den Autoren eine Vermutung.

**4. PROTOKOLL §9.1 (Behandlung von „keine Auswahl“ und Ausweichlabels).** IAMTC rechnete Knoten ohne Auswahl mit (S. 1952), und genau dort vermuten die Autoren die Ursache der niedrigen Werte bei Mikrokosmos und Theta-Rollen (S. 1954). Das stützt die getrennte Statusebene im Protokoll und zeigt, dass die Entscheidung, ob `KONTEXT_UNZUREICHEND` und `TEXT_DEFEKT` als fehlende Werte zählen, den Wert stark verschiebt; sie gehört vorab festgelegt (ist es) und im Bericht genannt.

**5. PROTOKOLL §9.1 Punkt 6 (Aufschlüsselung nach Wortart).** Gestützt: Verben deutlich niedriger als Nomen (0,46 gegen 0,60, S. 1954). Die Signifikanzangabe („p=.5“) ist im Werk widersprüchlich und nicht zitierfähig.

**6. A32 (α nahe an der Rohübereinstimmung).** Nicht behandelt; Rohübereinstimmung wird nicht berichtet, die erwartete Übereinstimmung nicht ausgewiesen. Gepoolt wird über alle Knoten eines Sets mit verschiedenen Wörtern, also ähnlich wie im Protokoll über Lemmata; ob α dabei nahe der Rohübereinstimmung lag, lässt sich aus dem Werk nicht ablesen.

**7. Abgleich mit `goldstandard/LITERATUR-IAA.md`** (dort ✔, Zeile „Für WordNet-Mehrfachannotation ergab das α ≈ 0,45 bis 0,66“): **Zahlen gedeckt** (Tab. 2, S. 1953), aber ohne drei Bedingungen, die zum Verständnis nötig sind: (a) die Werte gelten nach Ausschluss der schwächsten Person je Set, mit allen Personen liegt das Mittel bei 0,49 (S. 1954); (b) es waren sechs bis neun Personen pro Set (nach Ausschluss), nicht zwei; (c) Labels sind Begriffe des WordNet-Teils der Omega-Ontologie, Mehrfachwahl und „keine Auswahl“ eingeschlossen. Vorschlag: „nach Ausschluss der schwächsten Annotator:in; mit allen im Mittel 0,49“ ergänzen.

## Grenzen und Einwände

- Viele Annotator:innen pro Set, wechselnde Zusammensetzung; nicht direkt vergleichbar mit einer Doppelannotation durch zwei feste Personen.
- Ausschluss der schwächsten Person nach dem Ergebnis hebt die berichteten Werte; Tab. 5 wählt die beste Teilgruppe nachträglich.
- Keine Rohübereinstimmung, keine Konfidenzintervalle, keine Konfusionsmatrix; die Signifikanzangabe zu Verben ist widersprüchlich.
- Uneinheitliche Tabellennummern im Text.
- Englische Übersetzungen, nicht Originaltexte; Übersetzungsqualität als mögliche Störgröße nennen die Autoren selbst (S. 1954).
- Übertragbarkeit: Omega ist eine Ontologie, deren Begriffe über Wörter hinweg geteilt sein können; das ist dem MHDBDB-Begriffssystem näher als ein reines Wörterbuch, aber die Annotator:innen wählten Begriffe direkt, nicht Senses als Begriffsgruppen.

## Weiterführend

- Passonneau 2004, Computing reliability for coreference annotation, LREC (S. 1952, 1953): erste Fassung von MASI.
- Di Eugenio & Glass 2004, *Computational Linguistics* 30(1) (S. 1952): Prävalenz, Bias, kein Kochbuch.
- Di Eugenio 2000, LREC (S. 1952).
- Rosenberg & Binkowski 2004 (S. 1952, 1955): erweitertes κ für Haupt- und Nebenlabel.
- Artstein & Poesio 2005, Kappa³ = Alpha (or Beta), Technote (S. 1952, 1955): als Vergleichsmaß vorgeschlagen.
- Farwell et al. 2004; Dorr et al. 2004; Mitamura et al. 2004 (S. 1951): Beschreibungen des IAMTC-Projekts.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
