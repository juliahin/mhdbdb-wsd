# Kilgarriff & Rosenzweig 2000: English SENSEVAL, Bericht und Ergebnisse

**Datei:** `pdf/Kilgarriff-Rosenzweig-2000-English-Senseval.pdf` (nur lokal; 5 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Abb. 1 und erste Seite am Seitenbild geprüft, DOI aufgelöst. Das lokale PDF ist byte-gleich mit https://aclanthology.org/L00-1005.pdf (SHA-256 verglichen am 2026-11-13); es enthält keine Markierungen.

**Seitenzählung:** Das PDF trägt keine Seitenzahlen. Das Deckblatt des ITRI-Reports ITRI-00-25 auf der Autorenseite nennt „pp. 1239-1244“ für den LREC-Band; das ist 6 Seiten lang, das lokale PDF hat 5. Eine Zuordnung zu gedruckten Seiten ist daher nicht möglich. Unten steht **PDF-S. n** mit Abschnitt.

Es gibt eine längere Fassung desselben Berichts: Kilgarriff & Rosenzweig (2000), Framework and Results for English SENSEVAL, *Computers and the Humanities* 34, S. 15 bis 48 (Fußnote 1 der lokalen Fassung; Angaben bei Crossref, DOI 10.1023/A:1002693207386, nicht aufgelöst, nicht beschafft). `goldstandard/LITERATUR-STICHPROBE.md` zitiert die LREC-Fassung.

## Bibliografie

- **Vollständig:** Kilgarriff, Adam & Joseph Rosenzweig (2000). English SENSEVAL: Report and Results. In: M. Gavrilidou, G. Carayannis, S. Markantonatou, S. Piperidis & G. Stainhauer (Hg.), *Proceedings of the Second International Conference on Language Resources and Evaluation (LREC'00)*. Athen: European Language Resources Association (ELRA). Seiten laut Autorenfassung 1239 bis 1244 (nicht am Tagungsband geprüft).
- **DOI/URL:** https://doi.org/10.63317/56t55g8zw7sm (aufgelöst am 2026-11-13, leitet auf https://lrec.elra.info/lrec2000-main-005; Crossref: ELRA, Mai 2000, Tagung 31.05. bis 02.06.2000 in Athen, ohne Seiten; die ELRA-Seite nennt „Pages: N/A“); https://aclanthology.org/L00-1005 (Herausgeber:innen, Ort und Monat aus dem BibTeX der Anthology). Autorenfassung mit Seitenangabe: https://www.kilgarriff.co.uk/Publications/2000-KilgRosenweig-LREC-Senseval.pdf (ITRI-00-25, Deckblatt „May-June, 2000“).
- **Lizenz:** Die ELRA-Seite nennt CC BY-NC 4.0; die FAQ der ACL Anthology nennt für Material vor 2016 CC BY-NC-SA 3.0 (beide abgerufen 2026-11-13). Die Angaben widersprechen sich.
- **Art:** Konferenzbeitrag (LREC 2000)
- **Sprache:** Englisch

## Worum es geht

Der Bericht beschreibt den englischen Teil des ersten SENSEVAL (1998): Aufgabendesign, Daten, teilnehmende Systeme und Ergebnisse (PDF-S. 1). Gewählt wurde eine **Lexical-Sample**-Aufgabe mit dem HECTOR-Wörterbuch und -Korpus; 35 Wörter (41 Aufgaben) wurden über einen Rahmen aus Frequenz und Polysemie gezogen (PDF-S. 1 bis 2). Das Gold stammt von professionellen Lexikograf:innen mit Schiedsverfahren; die Replizierbarkeit des ganzen Verfahrens lag bei 95 % (PDF-S. 2). Bei feinkörnigen Senses mit Trainingsdaten erreichen die besten Systeme etwa 75 bis 80 %; die Entropie der Sense-Verteilung sagt die Schwierigkeit besser voraus als die Sense-Zahl (PDF-S. 4).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Ablauf nach dem Vorbild von MUC und ARPA: Interessierte gestalten mit, Zeitplan und Auswahlplan werden vereinbart, Menschen erstellen das Gold, Daten ohne Antworten gehen an die Teilnehmenden, die Organisatoren werten aus, ein Workshop bespricht die Ergebnisse. | PDF-S. 1, Abschnitt 1 | Beschreibung |
| **Lexical sample statt all-words**, weil (a) menschliches Annotieren effizienter ist, (b) all-words ein vollständiges, kostenloses Wörterbuch bräuchte, (c) viele Systeme Training oder Handarbeit pro Wörterbucheintrag brauchten. | PDF-S. 1, Abschnitt 2.1 | Entscheidung mit Begründung |
| HECTOR (OUP/Digital) liefert Wörterbuch und Korpus; Hauptgrund: Es gab bereits handannotierte Belege, falls kein Geld für Annotation käme. SEMCOR schied aus, weil es schon weit verbreitet war (nicht „unseen“) und all-words annotiert ist. Nachteil: sehr wenig Kontext, meist zwei Sätze. | PDF-S. 1 bis 2, Abschnitt 2.2, Anm. 3 | Entscheidung mit Begründung |
| **Lexikon-Stichprobe:** Kritik an früheren Lexical-Sample-Evaluationen: Wörter „chosen according to the whim of the experimenter“. Deshalb ein Stichprobenrahmen nach Frequenz (BNC) und Polysemie (WordNet); daraus 35 Wörter (41 Aufgaben) aus dem HECTOR-Bestand. | PDF-S. 2, Abschnitt 2.3 | eigenes Verfahren |
| Wortart: Für die meisten Wörter wurde die Wortart des Belegs als Eingabe vorgegeben (WSD und POS-Tagging entkoppelt), für fünf Wörter nicht („indeterminate“). Aufgabe = Wort plus Wortart. | PDF-S. 2, Abschnitt 2.4 | Entscheidung, Mehrheit eines früheren SIGLEX-Treffens |
| Daten: Probelauf, Trainingsdaten (für fünf Wörter keine, sonst 26 bis 2008 Belege, ohne Neuannotation) und Evaluationsdaten: 8448 Belege, die meisten Aufgaben mit 80 bis 400 Belegen; 15 Nomen-, 13 Verb-, 8 Adjektiv- und 5 unbestimmte Aufgaben. Jeder Evaluationsbeleg von mindestens drei Menschen annotiert. | PDF-S. 2, Abschnitt 3 | Beschreibung |
| Systeme durften pro Beleg einen oder mehrere Sense-Tags zurückgeben, optional mit Wahrscheinlichkeiten. | PDF-S. 2 | Beschreibung |
| **Gold:** Die Annotation gilt nur als korrekt, wenn verschiedene Personen oder Teams verlässlich zum selben Tag kommen (mit Verweis auf Gale et al. 1992). Deshalb professionelle Lexikograf:innen statt Studierender und ein korpusbasiertes Wörterbuch mit vielen Beispielen. | PDF-S. 2, „Gold standard replicability“ | eigene Begründung |
| Annotierende wurden **ermutigt, mehrere Tags zu geben** (einer davon konnte „unassignable“ sein), statt sich hart zu entscheiden. | PDF-S. 2 | Verfahren |
| Verfahren: zwei oder drei Lexikograf:innen annotieren; nicht identische Belege gehen an eine dritte Person zur Schlichtung („arbitration“). | PDF-S. 2 | Verfahren |
| Einzelne Lexikograf:innen gegen das geschlichtete Ergebnis, mit dem Bewertungsalgorithmus der Systeme: 88 bis 100 %; nur 5 von 122 Paaren aus Person und Wort unter 95 %. | PDF-S. 2 | eigenes Ergebnis |
| **Replizierbarkeit:** Für vier Wörter mit 1057 Belegen, nach Schwierigkeit gestreut, annotierten zwei Lexikograf:innen ohne Vorkenntnis der Daten neu, mit Schlichtung; Übereinstimmung mit dem ersten Durchgang 95 %. | PDF-S. 2 | eigenes Ergebnis |
| 17 Systeme, grob eingeteilt in überwachte und nicht überwachte; die Einteilung sei vorläufig und teils anomal. Systeme, die WordNet-Senses ausgaben und über ein Mapping auf HECTOR abgebildet wurden, verloren deutlich. | PDF-S. 3, Tab. 1, Anm. 4 | Beschreibung, Befund |
| **Baselines:** getrennt für überwachte (mit Trainingskorpus) und nicht überwachte (nur Wörterbuch) Systeme; die besten waren Varianten von Lesk; sie schlugen RANDOM und „always choose the sense which has most training-corpus instances“. Alle Baselines profitierten von einem Filter für Mehrwortausdrücke. | PDF-S. 3, „Baselines“ | eigenes Ergebnis |
| **Wertung:** Bei mehreren Tags pro Beleg Punkte zwischen 0 und 1, Wahrscheinlichkeitsmasse geteilt (Melamed & Resnik 2000). Precision = Summe der Punkte über bearbeitete Belege / Zahl der bearbeiteten Belege; Recall = Summe der Punkte / Zahl aller Belege. Die Wahl des Wertungsschemas über die Sense-Hierarchie änderte die relativen Ergebnisse kaum; berichtet werden nur exakte Treffer. | PDF-S. 3 bis 4, Abschnitt 5, Anm. 5 | Verfahren, Befund |
| Schiefe Verteilungen bedeuten, dass Systeme vor allem an wenigen häufigen Fällen gemessen werden; seltene Fälle wirken sich kaum auf die Wertung aus. | PDF-S. 4 | eigene Überlegung |
| Stand der Technik für feinkörnige WSD mit Trainingsdaten: etwa 75 % (Abschnitt 5), im Fazit 75 bis 80 %. Nomen über 80 %, Verben um 70 %, Adjektive und unbestimmte dazwischen. Systeme mit Trainingsdaten sind deutlich besser, auch bei Wörtern ohne Trainingsdaten. | PDF-S. 4, Abschnitte 5 und 6 | eigenes Ergebnis |
| Die meisten Systeme lagen unter der Lesk-Baseline ihres Typs; bei den 2500 Verb-Belegen verbesserte kein System die Fehlerrate der besten Baseline um mehr als 2 %. | PDF-S. 4 | eigenes Ergebnis |
| Belege sind nicht nach Schwierigkeit bewertet; da viele Systeme nur Teilmengen bearbeiteten, sind ihre Ergebnisse womöglich nicht vergleichbar. | PDF-S. 4 | eigene Einschränkung |
| **Polysemie, Entropie, Schwierigkeit:** Sense-Verteilungen sind schief, die Entropie variiert aber stark (*generous* und *slight* je 6 Senses, Entropie 2,30 gegen 1,28). Nomen haben im Mittel mehr Senses, Verben höhere Entropie, und Systeme sind bei Nomen besser; Entropie sei daher das bessere Maß der Schwierigkeit. Korrelation mit der Systemleistung: Polysemie −0,258, Entropie −0,510; nur überwachte Systeme: Entropie −0,699, Polysemie −0,247. | PDF-S. 4, Abschnitt 5.1, Anm. 6 | eigenes Ergebnis |
| Fazit: hohe Replizierbarkeit des Golds als „notable success“; ein gut umgesetzter einfacher Lesk ist schwer zu schlagen; künftige SENSEVALs sollten das Design nach Stärken und Schwächen des ersten anpassen. | PDF-S. 4, Abschnitt 6 | Zusammenfassung |

## Daten, Methode, Zahlen

- **Umfang:** 35 Wörter, 41 Aufgaben (15 N, 13 V, 8 ADJ, 5 unbestimmt), 8448 Evaluationsbelege, meist 80 bis 400 pro Aufgabe (PDF-S. 2).
- **Annotierende:** professionelle Lexikograf:innen, je Beleg mindestens drei Annotationen, Schlichtung durch eine dritte Person (PDF-S. 2).
- **Übereinstimmung:** einzeln gegen geschlichtet 88 bis 100 %, 5 von 122 unter 95 %; Wiederholung mit neuem Team 95 % auf 1057 Belegen von vier Wörtern (PDF-S. 2). Kein Kappa.
- **Abb. 1 (PDF-S. 5, am Seitenbild geprüft):** Precision gegen Recall aller Systeme und Baselines über alle Belege. „hector“ (das menschliche Übereinstimmungsniveau) steht allein oben rechts, deutlich über allen Systemen; die besten Systeme (durham, hopkins, tilburg, ets-pu) liegen bei Precision und Recall um 0,7 bis 0,8, „common“ (häufigster Sense) bei Precision um 0,65 und Recall um 0,55. Werte nur grafisch, im Text nicht genannt [Zahlen am PDF abgelesen, nicht genau prüfbar].
- **Entropie (Anm. 6, PDF-S. 4):** −Σ p(x) log p(x) über die Sense-Tags eines Wortes, p(x) aus den Trainingsbelegen.

## Wörtliche Stellen

> „A criticism of earlier forays into lexical-sample WSD evaluation is that the lexical sample had been chosen according to the whim of the experimenter […].“ (PDF-S. 2, Abschnitt 2.3)

> „Taggers were encouraged to give multiple tags (one of which might be the ‘unassignable’ tag) rather than make hard choices.“ (PDF-S. 2)

> „Systems tend to do better on the nouns than the verbs, suggesting that entropy is the better measure of the difficulty of the tasks.“ (PDF-S. 4, Abschnitt 5.1)

## Bezug zur Dissertation

**Prüfauftrag zu `goldstandard/LITERATUR-STICHPROBE.md`** (Zeile „Senseval wählte Lemmata über ein Frequenz × Polysemie-Raster“, dort ✔):

- *Frequenz × Polysemie-Raster, „nicht nach Laune des Experimentators“*: **gedeckt** (PDF-S. 2, Abschnitt 2.3). Das Raster selbst (Bänder, Zellen) beschreibt die LREC-Fassung nicht; es steht bei Kilgarriff 1998 (ITRI-Fassung S. 15 bis 17).
- *„80 bis 400 Belege pro Lemma“*: **im Kern gedeckt**, genauer „most tasks having between 80 and 400 instances“ (PDF-S. 2). Eine Aufgabe ist Wort plus Wortart; „pro Aufgabe“ wäre exakt.
- Seitenangabe: Die LREC-Fassung hat keine Seitenzahlen; beim Zitieren Abschnitt 2.3 bzw. 3 angeben oder die Langfassung in *Computers and the Humanities* 34 benutzen.

**Weitere Bezüge:**

- **PROTOKOLL §4.3 (Entropie und MFS-Anteil als Kovariaten):** Der Bericht misst, was das Protokoll annimmt: Die Entropie korreliert mit der Systemleistung stärker (−0,510, überwacht −0,699) als die Sense-Zahl (−0,258 bzw. −0,247) (PDF-S. 4). Das ist ein dritter Beleg neben Loureiro et al. 2021 und Passonneau et al. 2010 (`LITERATUR-STICHPROBE.md`) und der älteste. Es stützt auch die Entscheidung, nach der Inventargröße zu schichten (beobachtbar ohne Silber) und die Entropie nur als Kovariate zu führen: SENSEVAL schichtete ebenfalls nach Sense-Zahl und fand die Entropie erst nachträglich aussagekräftiger.
- **PROTOKOLL §6 (`MEHRERE`, `KEINE_PASST`):** SENSEVAL ermutigte ausdrücklich zu mehreren Tags und bot „unassignable“ an (PDF-S. 2). Das ist großzügiger als Kilgarriffs Regel von 1998 („nur wenn eine Einzelantwort unwahr wäre“, ITRI-Fassung S. 9). Für die Richtlinien des Pilots heißt das: Die Literatur kennt beide Haltungen; welche gilt, beeinflusst den Anteil von `MEHRERE` und damit die Teilwertung.
- **PROTOKOLL §9.2 (Bewertung von Mengenantworten, A23):** SENSEVAL verteilte die Punkte bei mehreren Antworttags anteilig (PDF-S. 3). Das Protokoll wertet eine `MEHRERE`-Antwort des LLM nur als richtig, wenn jede genannte ID im Gold steht. Beide Regeln verhindern, dass Absichern belohnt wird; die anteilige Wertung wäre eine weitere mögliche Sensitivitätsauswertung neben Dice.
- **PROTOKOLL §9.2 (ungültige Antworten, Abstinenz):** SENSEVAL trennte Precision (über bearbeitete Belege) und Recall (über alle Belege) (PDF-S. 3 bis 4) und stellt fest, dass Systeme, die nur Teilmengen bearbeiten, schwer vergleichbar sind (PDF-S. 4). Die Primärregel des Protokolls (ungültig = falsch, Auswertung über alle Items) entspricht dem Recall; die Begründung „ein Ausschluss bräche die Paarung“ wird durch diese Beobachtung gestützt.
- **PROTOKOLL §7, Schritt 6 und §9.2 (Adjudikation, IAA-Bericht):** Die 88 bis 100 % sind Übereinstimmung jeder Person mit dem **geschlichteten** Ergebnis, an dem sie selbst beteiligt war (PDF-S. 2); sie sind daher höher als eine paarweise Übereinstimmung vor der Schlichtung und mit dieser nicht vergleichbar. Das stützt §7, Schritt 5 (Roh-IAA vor jeder Besprechung) und §9.2 („Jede:r gegen das Gold“ getrennt von der IAA).
- **PROTOKOLL §9.2 (menschliche Übereinstimmung als Obergrenze):** Die Replizierbarkeit zweier Teams (95 %, PDF-S. 2) ist eine andere Größe als die IAA zwischen zwei Personen; Kilgarriff 2001 (S. 20) erklärt erst die Replizierbarkeit zur eigentlichen Obergrenze. In Abb. 1 dient „hector“ als menschliches Vergleichsniveau.
- **PROTOKOLL §3 (Wortart als Eingabe):** SENSEVAL gab die Wortart in den meisten Aufgaben vor (PDF-S. 2), wie das Protokoll mit Paaren aus Lemma und Wortart. Die fünf „indeterminate“-Aufgaben zeigen, dass die Entkopplung eine Entscheidung ist, keine Selbstverständlichkeit.
- **Größenordnung und Baseline:** Bei Verben verbesserte kein System die Fehlerrate der besten Baseline um mehr als 2 % (PDF-S. 4). Für die Dissertation ist das ein Hinweis, dass in der Zelle VRB ein kleiner Abstand LLM minus MFS nicht überraschen würde; §4.7 rechnet ohnehin nur Unterschiede um 10 Punkte je Wortart als nachweisbar.

## Grenzen und Einwände

- Kurzfassung (5 Seiten); viele Details (Raster, Wortliste, Werte je Wort) stehen nur in der Langfassung, die nicht vorliegt.
- Keine Zufallskorrektur und kein Kappa; die Übereinstimmungswerte sind mit dem Systemalgorithmus berechnet (PDF-S. 2) und teils gegen das geschlichtete Ergebnis.
- Die Replizierbarkeit beruht auf vier Wörtern; welche, nennt die Kurzfassung nicht.
- Korrelationen ohne Angabe der Fallzahl (Aufgaben oder Paare aus System und Aufgabe?) und ohne Signifikanz.
- HECTOR ist ein unveröffentlichtes Wörterbuch mit Korpusbelegen als Beispielen; Lesk profitiert davon (PDF-S. 4). Die Ergebnisse hängen am Inventar, wie Kilgarriff 2001 mit WordNet zeigt.
- Übertragbarkeit: Englisch, feinkörniges Wörterbuchinventar, professionelle Lexikograf:innen; ein Begriffssystem und Mittelhochdeutsch nicht berührt.

## Weiterführend

- Kilgarriff & Rosenzweig (2000), Framework and Results for English SENSEVAL, *Computers and the Humanities* 34(1 bis 2), S. 15 bis 48 (Fußnote 1; Angaben aus Kilgarriff 2001, S. 20): Langfassung mit Raster und Werten.
- Melamed & Resnik (2000), Evaluation of sense disambiguation given hierarchical tag sets, *Computers and the Humanities* (PDF-S. 3, PDF-S. 5): Wertung bei Mehrfachtags und Hierarchie.
- Kilgarriff & Palmer (2000), Special Issue on SENSEVAL (PDF-S. 1, PDF-S. 5).
- Kilgarriff (1999), 95 % replicability for manual word sense tagging, EACL, S. 277 bis 278 (zitiert in Kilgarriff 2001, S. 20): Primärquelle für die Replizierbarkeit.
- Atkins (1993), HECTOR (PDF-S. 1, PDF-S. 4).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
