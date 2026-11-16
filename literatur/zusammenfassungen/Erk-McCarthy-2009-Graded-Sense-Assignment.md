# Erk & McCarthy 2009: Graded Word Sense Assignment

**Datei:** `pdf/Erk-McCarthy-2009-Graded-Sense-Assignment.pdf` (nur lokal; 10 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen, Tab. 4 und 5 (S. 446) am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology D09-1046 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 439 + n (PDF 1 = S. 440, PDF 10 = S. 449; Seitenzahlen in der Fußzeile). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Erk, Katrin & Diana McCarthy (2009). Graded Word Sense Assignment. In: Philipp Koehn & Rada Mihalcea (Hg.), *Proceedings of the 2009 Conference on Empirical Methods in Natural Language Processing*. Singapur: Association for Computational Linguistics, S. 440 bis 449.
- **DOI/URL:** keine DOI im PDF und im BibTeX der Anthology; https://aclanthology.org/D09-1046/ (Herausgeber, Ort, Verlag, Monat August nach dem BibTeX der Anthology, abgerufen 2026-11-16). Im PDF: „Singapore, 6-7 August 2009. ©2009 ACL and AFNLP“ (S. 440).
- **Lizenz:** CC BY-NC-SA 3.0 nach der Copyright-FAQ der ACL Anthology (ACL-Material vor 2016, abgerufen 2026-11-16).
- **Art:** Konferenzbeitrag
- **Sprache:** Englisch

## Worum es geht

WSD wird üblicherweise als Wahl des einen besten Sense aus einem Inventar wie WordNet gestellt, obwohl diskrete Sense-Grenzen in der lexikalischen Semantik umstritten sind (S. 440). Die Arbeit untersucht die **graduelle Sense-Zuordnung** am GWS-Datensatz von Erk et al. 2009, in dem drei Annotator:innen jeden WordNet-Sense eines Belegs auf einer Skala von 1 bis 5 bewertet haben (S. 440, 442). Sie schlägt Maße für graduelle Urteile vor (Spearman ρ auf drei Ebenen, Jensen-Shannon-Divergenz, eine graduelle Verallgemeinerung von Precision und Recall; S. 442 bis 444) und wendet sie auf die Annotator:innen selbst (menschliche Obergrenze) und auf überwachte Modelle an (S. 445 bis 447). Die Modelle bleiben deutlich unter den Menschen, besonders beim Ordnen der Belege danach, wie stark sie einen Sense evozieren (S. 447 bis 448).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| In GWS nutzten die Annotator:innen die Zwischenstufen der Skala reichlich und gaben oft mehreren WordNet-Senses desselben Belegs hohe Werte; die Urteile ließen sich nicht einfach durch gröbere Senses in kategoriale umwandeln. | S. 440, 442 | referiert (Erk et al. 2009) |
| Gröbere Inventare erleichtern die Aufgabe, aber man wisse nicht, welche Unterscheidungen die richtigen sind; feine Unterscheidungen können für manche Anwendungen nützlicher sein. | S. 441, Abschnitt 2 | referiert (Hovy et al. 2006; Stokoe 2005; Hanks 2000) |
| Die Arbeit argumentiert nicht für oder gegen ein bestimmtes Inventar; WordNet wird benutzt, weil GWS es benutzt. | S. 441 | Festlegung der Autorinnen |
| Drei Korrelationsebenen: pro Lemma (Konsistenz der Urteile für ein Lemma), pro Lemma und Sense (Belege danach geordnet, wie stark sie einen Sense evozieren), pro Lemma und Satz (Senses danach geordnet, wie gut sie auf einen Beleg passen). Gemittelt wird über Lemmata, damit Lemmata mit vielen Senses nicht stärker zählen. | S. 443, Abschnitt 4 | eigene Methode |
| Graduelle Precision und Recall: Summe der Minima aus Gold- und Systemwert, geteilt durch die Summe der System- bzw. Goldwerte; bei kategorialen Daten fallen sie mit den klassischen Maßen zusammen. | S. 443 bis 444 | eigene Methode |
| Menschliche Obergrenze (je eine Person gegen das Mittel der beiden anderen): ρ pro Lemma 0,517 bis 0,587 (Mittel 0,544), pro Lemma und Sense 0,403 bis 0,41 (0,407), pro Lemma und Satz 0,482 bis 0,612 (0,535); F 64,0 bis 68,3 (65,5). | S. 446, Tab. 4 | eigenes Ergebnis |
| Die Annotator:innen nutzen die Skala verschieden: Annotatorin 1 gibt durchweg höhere Werte (Mittel 0,540 normiert gegen 0,345 und 0,285), daher Recall 87,5 bei Precision 50,6. | S. 445, 447, Tab. 4 und 6 | eigenes Ergebnis |
| Wegen dieser Unterschiede in den absoluten Werten passt eine rangbasierte Auswertung, ergänzt um J/S, am besten zu den Daten. Mehr Annotator:innen würden die Mittelwerte weniger von Eigenheiten einzelner abhängig machen; psycholinguistische Experimente mit festen Skalen holen typischerweise 10 oder mehr Urteile pro Item ein. | S. 447 | Folgerung der Autorinnen |
| Klassische Bestannotation erzeugt „spurious negative data“: Passen s1, s2 und s3 teilweise, wird nur s1 vergeben, und s2, s3 gelten fälschlich als nicht zutreffend. | S. 445, Abschnitt 5 | Argument der Autorinnen |
| Das Standard-WSD-Modell mit Konfidenzwerten (WSD/conf) liegt in allen Maßen knapp über der Baseline aus Sense-Häufigkeiten, „a very familiar picture from standard WSD“. | S. 446 bis 447, Tab. 5 | eigenes Ergebnis |
| Kein Modell kommt beim Ordnen nach Lemma und Sense in die Nähe der Menschen (Modelle höchstens 0,177, Menschen 0,407); vermutlich fehlen Trainingsdaten für seltene Senses. | S. 447, Tab. 4 und 5 | eigenes Ergebnis und Vermutung |

## Daten, Methode, Zahlen

- **Daten:** Teil des GWS-Datensatzes (Erk et al. 2009): 8 Lemmata, je 25 Sätze zufällig aus SemCor und 25 aus dem SENSEVAL-3 English Lexical Sample, also 50 Sätze pro Lemma (S. 442, Tab. 2). Lemmata: *add* (v, 6 Senses), *argument* (n, 7), *ask* (v, 7), *different* (a, 5), *important* (a, 5), *interest* (n, 7), *paper* (n, 7), *win* (v, 4).
- **Skala:** 1 völlig verschieden, 2 überwiegend verschieden, 3 ähnlich, 4 sehr ähnlich, 5 identisch; WordNet 3.0; drei Annotator:innen; Mittel über die drei, normiert auf 0 bis 1 als (Urteil − 1)/4 (S. 442).
- **Training der Modelle:** alle Sätze aus SemCor und dem Trainingsteil von SE-3, die nicht in GWS stehen (1.047 und 1.173 Sätze; Tab. 2, S. 442).
- **Standard-WSD zur Einordnung:** Genauigkeit 77,0 % gegen MFS 63,5 % (SemCor), 53,0 % gegen 44,0 % (SE-3), 58,2 % gegen 56,0 % (beide zusammen) (S. 445).
- **Tab. 4, menschliche Obergrenze (S. 446, am Seitenbild geprüft):** Anteil signifikanter Korrelationen pro Lemma 100 %, pro Lemma und Sense 73,6 % (p ≤ 0,05), pro Lemma und Satz 29,0 % (p ≤ 0,05); J/S 0,131 bis 0,165; P 50,6 / 75,5 / 82,4; R 87,5 / 62,4 / 52,3.
- **Tab. 5, Modelle (S. 446, am Seitenbild geprüft):** bestes ρ pro Lemma Prototype/2N 0,465; bestes F Prototype 66,9 (nahe am menschlichen Mittel 65,5, aber mit hohen Werten über alle Senses, Tab. 6); Baseline ρ pro Lemma 0,338, F 48,2.
- Die Arbeit berichtet die Übereinstimmung der Menschen nur als „eine Person gegen das Mittel der anderen“, nicht als paarweise Übereinstimmung; die paarweisen Werte stehen in Erk et al. 2013 (S. 524 bis 525).

## Wörtliche Stellen

> „[…] computational linguists have readily accepted the best-fitting sense methodology despite the fact that the case for discrete sense boundaries is widely disputed by lexical semantics researchers.“ (S. 440)

> „The relatively low precision and recall in Table 4 confirm that different annotators use the 5-point scale in different ways.“ (S. 447)

## Bezug zur Dissertation

**1. A31 (Vorgabe eines Inventars) und PROTOKOLL §6 (`MEHRERE`).** Das Argument der „spurious negative data“ (S. 445) beschreibt genau, was eine Pflicht zur Bestwahl verdeckt: Senses, die teilweise passen, gelten als nicht zutreffend. Das Protokoll fängt einen Teil davon mit `MEHRERE` und den Sicherheitsstufen ab; graduelle Urteile pro Karte sind dort nicht vorgesehen. Die Arbeit liefert keinen Beleg dafür, dass ein Inventar das Urteil lenkt, nur dafür, dass Menschen mehreren Senses hohe Werte geben, wenn sie dürfen (referiert aus GWS, S. 440, 442).

**2. Offener Punkt 20 (Auswertung der Lesarten).** Die drei Korrelationsebenen (S. 443) zeigen, wie man graduelle Urteile auswertet, ohne Skalenunterschiede der Personen mitzumessen. Falls Lesarten später auf Nähe zu den Karten bewertet werden, wäre die Ebene „pro Lemma und Satz“ (Karten für einen Beleg ordnen) die passende. Das ist eine Ableitung, nicht Aussage der Arbeit.

**3. PROTOKOLL §9.1 (Maße) und LITERATUR-IAA.md.** Die Arbeit zeigt zweierlei, das für §9.1 zählt: Erstens unterscheiden sich Personen stark darin, wie sie eine Skala nutzen (Tab. 4 und 6), was für rangbasierte Maße spricht, sobald graduelle Urteile ins Spiel kommen. Zweitens berichtet sie Übereinstimmung als „eine Person gegen das Mittel der anderen“; das ist nicht mit κ oder α zweier Personen vergleichbar. LITERATUR-IAA.md zitiert Erk & McCarthy 2009 nicht; dort steht nur Erk et al. 2013.

**4. PROTOKOLL §9.2 (LLM gegen MFS).** Nebenbefund: Selbst bei graduellen Urteilen liegt das Standardmodell nur knapp über der Häufigkeits-Baseline (S. 447). Das passt zur Wahl der MFS-Baseline als Vergleichsmaß.

**5. Weg C (offener Punkt 22).** Nur mittelbar: Die Arbeit arbeitet inventargebunden (WordNet-Senses), nicht inventarfrei. Inventarfrei ist erst Usim in Erk et al. 2013.

## Grenzen und Einwände

- Sehr kleine Datenbasis: 8 Lemmata, 400 Sätze, drei Annotator:innen (S. 442). Die Autorinnen sagen selbst, dass mehr Annotator:innen nötig wären (S. 447).
- Die menschliche Obergrenze ist eine Person gegen das Mittel von nur zwei anderen.
- Modelle sind 2009er Merkmals- und Vektormodelle; ihre Zahlen sind für LLMs nicht aussagekräftig, die Maße schon.
- Englisch, WordNet; für ein onomasiologisches Inventar aus Begriffsgruppen und für Mittelhochdeutsch nicht geprüft.

## Weiterführend

- Erk, McCarthy & Gaylord 2009, Investigations on word senses and word usages, ACL-IJCNLP (S. 440, 448): der GWS-Datensatz; erweitert in Erk et al. 2013.
- Kilgarriff 2006, Word senses, in Agirre & Edmonds (Hg.), *Word Sense Disambiguation*, S. 29 bis 46 (S. 440, 448).
- Hanks 2000, Do word meanings exist?, *Computers and the Humanities* 34 (S. 440, 441, 448).
- Ide & Wilks 2006, Making sense about sense, in Agirre & Edmonds (Hg.), S. 47 bis 73 (S. 441, 448).
- Tuggy 1993, Ambiguity, polysemy and vagueness, *Cognitive Linguistics* 4 (S. 440, 449).
- Ramakrishnan et al. 2004, Soft word sense disambiguation, GWC (S. 441): einzige frühere Studie zu gradueller Zuordnung, ohne Vergleich mit Menschen.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
