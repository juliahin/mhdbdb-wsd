# Passonneau 2006: Measuring Agreement on Set-valued Items (MASI)

**Datei:** `pdf/Passonneau-2006-MASI.pdf` (nur lokal; 6 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Formel für α (S. 833) sowie Tab. 1 und 2 (S. 835) am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology L06-1392 (SHA-256 verglichen am 2026-11-13); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 830 + n (PDF 1 = S. 831, PDF 6 = S. 836; Seitenzahlen in der Fußzeile). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Passonneau, Rebecca (2006). Measuring Agreement on Set-valued Items (MASI) for Semantic and Pragmatic Annotation. In: Nicoletta Calzolari, Khalid Choukri, Aldo Gangemi, Bente Maegaard, Joseph Mariani, Jan Odijk & Daniel Tapias (Hg.), *Proceedings of the Fifth International Conference on Language Resources and Evaluation (LREC’06)*. Genua: European Language Resources Association (ELRA), S. 831 bis 836.
- **DOI/URL:** keine DOI; https://aclanthology.org/L06-1392/ (Herausgeber:innen, Ort, Verlag, Monat Mai nach dem BibTeX der Anthology, abgerufen 2026-11-13). Die Anthology nennt keine Seiten; S. 831 bis 836 stehen in den Fußzeilen des PDF und ebenso bei Artstein & Poesio (2008, S. 594).
- **Lizenz:** nicht festgestellt. Die FAQ der ACL Anthology regelt nur ACL-Material; LREC-Beiträge (ELRA) sind dort nicht erfasst (abgerufen 2026-11-13).
- **Art:** Konferenzbeitrag
- **Sprache:** Englisch

## Worum es geht

Der Beitrag stellt MASI vor, ein Abstandsmaß für den Vergleich zweier Mengen, und zeigt es an einer Annotation aus der Evaluation automatischer Zusammenfassungen: Zwei Annotator:innen bauen unabhängig „Pyramiden“ aus Summary Content Units (SCUs) für fünf Dokumentsammlungen der DUC 2003 (S. 831 bis 832). Mit Krippendorffs α und drei Abstandsmaßen (nominal, Jaccard, MASI) ergeben sich sehr verschiedene Werte für dieselben Daten: nominal 0,01 bis 0,24, MASI 0,68 bis 0,80 (S. 835, Tab. 2). Die Autorin argumentiert, dass „ausreichend“ von der Verwendung der Daten abhängt und eine Reliabilitätsstudie die Werte mit einer unabhängigen Prüfung verbinden sollte („paradigmatic reliability study“, S. 833, 836).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Semantische und pragmatische Annotation steht vor der Wahl, die Phänomene zu vereinfachen oder Unterscheidungen zu erfassen, die übliche Maße nicht messen können; die Lösung seien Maße, die die verlangten Entscheidungen abbilden. | S. 831, Abstract | Position der Autorin |
| Andere Wege für Mehrfachlabels: Im IAMTC-Projekt sollten Annotator:innen mehrere Labels wählen, wenn eines nicht reicht; Rosenberg & Binkowski (2004) ließen ein Hauptlabel bestimmen und erweiterten κ mit einem Gewicht dafür. | S. 831 | referiert |
| Die meisten Koeffizienten teilen die Form (p(A_O) − p(A_E))/(1 − p(A_E)); der Unterschied liegt in der Schätzung von p(A_E): Scotts π und Siegel & Castellans K mit einer Verteilung für alle, Cohens κ mit einer pro Codierer. | S. 832 bis 833, Abschnitt 3.1 | referiert |
| Krippendorffs α mit nominalem Abstand entspricht bei sehr großen Stichproben Scotts π, korrigiert für kleine Stichproben, gilt für mehrere Codierer und viele Skalen. | S. 833 | referiert (Krippendorff 1980) |
| Zur Schwelle: Krippendorff (1980) werde oft mit 0,67 als Grenze für vorsichtige Schlüsse zitiert, sage aber zur Frage, was reliabel genug ist, „there is no set answer“ (S. 146). Die Schwelle stamme aus Studien, in denen dieselben Variablen auch in Signifikanztests eingingen; Variablen unter 0,67 waren dort nie signifikant. Manche Inhaltsanalysen seien aber so robust, dass Unreliabilität im Ergebnis kaum auffalle (S. 147). | S. 833 | referiert (Krippendorff 1980), Deutung der Autorin |
| „Paradigmatic reliability study“: Reliabilitätswerte zusammen mit Signifikanztests der annotierten Variablen gegenüber unabhängigen Größen untersuchen. Beispiel aus Passonneau et al. 2005: mittleres Kappa 0,57, α mit Dice 0,62, Korrelationen hoch signifikant. | S. 833 | eigener Begriff; Beispiel aus eigener früherer Arbeit |
| MASI ist ein Abstandsmaß für Mengen wie Jaccard oder Dice und enthält Jaccard. Als Gewicht ist es unabhängig davon, wie die erwartete Übereinstimmung geschätzt wird, und in jedem gewichteten Koeffizienten verwendbar, etwa α oder Artstein & Poesios Beta. | S. 833, Abschnitt 3.3 | eigenes Maß |
| Ungewichtete Maße ergeben bei Mengenlabels, die sich ähneln, aber selten identisch sind, „misleadingly low values“ (Koreferenz). | S. 833 | eigene frühere Arbeit (Passonneau 2004) |
| MASI = J × M, zwischen 1 (gleiche Mengen) und 0 (disjunkt). J ist Jaccard (Schnitt durch Vereinigung) und gewichtet Größenunterschiede; M (Monotonie) ist 1 bei gleichen Mengen, 2/3 bei Teilmenge, 1/3 bei Schnitt mit zwei nicht leeren Differenzen, 0 bei disjunkten Mengen. M bestraft nicht monotone Abweichungen stärker. | S. 834 | eigene Definition |
| In α geht als Abstand 1 − MASI ein (ebenso 1 − Jaccard). | S. 835 | eigene Festlegung |
| Für dieselben Daten hängt α stark vom Abstandsmaß ab. Beispiel aus Abb. 1 (Tab. 1): mit Spans als Einheiten nominal 0, Jaccard −0,44, MASI 0,14; mit Wörtern als Einheiten 0, 0,64, 0,81. | S. 835, Tab. 1 | eigenes Ergebnis |
| Fünf Pyramidenpaare (Tab. 2): nominal 0,01 bis 0,24, Jaccard 0,39 bis 0,58, MASI 0,68 bis 0,80. Mit MASI steigen die Werte um etwa die Hälfte des Abstands zwischen Jaccard und 1; das zeige, dass die meisten Abweichungen monoton sind (Teilmengen). | S. 835 bis 836 | eigenes Ergebnis und Deutung |
| Ob die Werte reichen, hängt von der Verwendung ab. In einer getrennten Untersuchung korrelierten Bewertungen mit Pyramiden zweier Annotator:innen mit r = 0,84 bis 0,91; das zeige, dass die Annotationen „more than reliable enough“ seien. | S. 836 | eigenes Ergebnis (Passonneau 2005) |
| Mehrere Maße mit bekanntem Verhältnis zueinander charakterisieren einen Datensatz besser als eine Zahl; was für eine Aufgabe reliabel ist, muss es für eine andere nicht sein. | S. 836, Abschnitt 5 | Position der Autorin, mit Di Eugenio & Glass 2004 |

## Daten, Methode, Zahlen

- **Daten:** fünf Dokumentsammlungen der DUC 2003, je sieben Musterzusammenfassungen; zwei Annotator:innen bauen unabhängig je eine Pyramide (S. 832). Im Mittel 725 Wörter und 92 verschiedene SCUs pro Pyramide (S. 835).
- **Einheiten und Labels:** Codiereinheit ist das Wort (zur Veranschaulichung auch der Span); Label ist die Äquivalenzklasse, also die Menge der Spans bzw. Wörter, in die eine Annotator:in die Einheit gestellt hat (S. 833 bis 835). Vor dem Vergleich wird die Einheit selbst aus beiden Mengen entfernt, sonst überschneiden sie sich immer (S. 834).
- **Maß:** Krippendorffs α mit drei Abständen (nominal, 1 − Jaccard, 1 − MASI); Formel für m Codierer und r Einheiten S. 833.
- **Rechenbeispiel (S. 834):** mittlerer Jaccard 5/9 (Abb. 2, Teilmengen) gegen 4/9 (Abb. 3, Überschneidung); mittlerer MASI 10/27 (0,37) gegen 6/27 (0,22).

**Tab. 2 (S. 835, am Seitenbild geprüft), α je Dokumentsammlung:**

| Docset | nominal | Jaccard | MASI |
|---|---|---|---|
| 30016 | 0,19 | 0,55 | 0,79 |
| 30040 | 0,24 | 0,58 | 0,80 |
| 31001 | 0,01 | 0,40 | 0,68 |
| 31010 | 0,03 | 0,39 | 0,69 |
| 31038 | 0,09 | 0,40 | 0,71 |

Kleine Unstimmigkeit im Werk: S. 836 nennt für die Korrelationsstudie die Sammlungen 30016 und „30014“; 30014 steht nicht in Tab. 2.

## Wörtliche Stellen

> „In effect, what counts as sufficiently reliable intera-annotator agreement depends on the use the annotated data will be put to.“ (S. 831; Schreibfehler „intera-“ im Original)

> „Krippendorff (1980) is often cited as recommending a threshold of 0.67 to support cautious conclusions. The comment he made that introduced his discussion should be quoted more often.“ (S. 833)

> „MASI ranges from 1, when two sets are identical, to 0, when they are disjoint. It has two terms which weight different aspects of set comparison: MASI = J*M.“ (S. 834)

> „Because Krippendorff’s Alpha measures disagreements, one minus Jaccard, and one minus MASI, are used in computing Alpha.“ (S. 835)

## Bezug zur Dissertation

**1. PROTOKOLL §9.1 Punkt 1 und A8 (α mit MASI als Hauptmaß), Formelquelle.** Das ist die Originaldefinition: MASI = J × M als Ähnlichkeit (S. 834), in α als Abstand 1 − MASI (S. 835). Eigene Rechnung für die typischen Fälle des Goldstandards (die Einheit ist das Item, nicht ein Element der Menge, das Entfernen der Einheit aus S. 834 entfällt also):

| Person 1 | Person 2 | J | M | Abstand 1 − J·M |
|---|---|---|---|---|
| {s1} | {s1} | 1 | 1 | 0 |
| {s1} | {s1, s2} | 1/2 | 2/3 | 2/3 |
| {s1, s2} | {s1, s2, s3} | 2/3 | 2/3 | 5/9 |
| {s1, s2} | {s2, s3} | 1/3 | 1/3 | 8/9 |
| {s1} | {s2} | 0 | 0 | 1 |

`SENSE` gegen `MEHRERE` mit Überschneidung zählt also nur zu einem Drittel als Übereinstimmung. Artstein & Poesio (2008, S. 584) geben MASI abweichend als Produkt d_P × d_J an, das ergäbe für {s1} gegen {s1, s2} den Abstand 1/6. Vorschlag: Im Protokoll den Abstand als 1 − J·M ausschreiben, mit Passonneau 2006 (S. 834 bis 835) als Quelle, und die Tabelle oben in den Auswertungsplan übernehmen, damit vor dem Rechnen feststeht, wie stark `MEHRERE` als Teilübereinstimmung zählt.

**2. PROTOKOLL §9.1 Punkt 1: „α nominal … als untere Schranke“.** Durch dieses Werk nicht gestützt. In Tab. 2 liegt α nominal zwar immer unter MASI, Tab. 1 zeigt aber, dass ein gewichtetes α unter das nominale fallen kann (Spans: Jaccard −0,44 gegen nominal 0, S. 835). Für MASI ist in den Daten dieses Werks keine Umkehr belegt, eine allgemeine Ordnung behauptet die Autorin nicht. Vorschlag: „untere Schranke“ ersetzen durch „strengere Variante“ oder „in der Regel niedriger“.

**3. A32 (Schwellen 0,67 und 0,80).** Die Autorin ordnet 0,67 ein: Krippendorff habe die Zahl aus Studien abgeleitet, in denen Variablen unter 0,67 nie signifikant wurden, und zugleich gesagt, es gebe „no set answer“ (S. 833). Die Schwelle ist also für Schlüsse aus codierten Variablen gedacht, nicht als Abbruchkriterium eines Pilots. Das stützt den Satz in A32, die Schwelle entscheide über das Nachschärfen, nicht über die Brauchbarkeit des Golds. 0,80 kommt in diesem Werk nicht vor.

**4. A32 (α nahe an der Rohübereinstimmung bei lemmaspezifischen IDs).** Nicht behandelt. Ein verwandter Befund: Bei Mengenlabels, die über die Einheiten hinweg kaum identisch sind, liegt α nominal nahe 0 (Tab. 2: 0,01 bis 0,24), weil fast keine exakte Übereinstimmung vorkommt; über die erwartete Übereinstimmung sagt die Autorin dabei nichts.

**5. PROTOKOLL §9.2 und §9.1 (unabhängige Prüfung, mehrere Maße).** Die „paradigmatic reliability study“ (S. 833, 836) passt zum Aufbau des Protokolls, die IAA mit dem Vergleich gegen Gold, Silber und LLM zu verbinden, und zur Liste mehrerer Maße in §9.1. Dass auch die Rohübereinstimmung exakt und mit Überschneidung berichtet wird (§9.1 Punkt 2), entspricht der Empfehlung, mehrere Maße mit bekanntem Verhältnis nebeneinander zu stellen (S. 836).

**6. Abgleich mit `goldstandard/LITERATUR-IAA.md`** (Passonneau 2006 dort ✔, Zeile „MASI: Mengendistanz für Mehrfachlabels, einsetzbar in α“): gedeckt (S. 833 bis 835). Die Zahlen „α ≈ 0,45 bis 0,66“ derselben Zeile stammen nicht aus diesem Werk, sondern aus Passonneau, Habash & Rambow 2006 (siehe dort). Dieses Werk ist keine WSD-Studie.

## Grenzen und Einwände

- Keine WSD-Daten: Die Labels sind Äquivalenzklassen von Textstellen (Pyramiden), deren Zahl nicht vorgegeben ist; bei einem festen Sense-Menü pro Lemma sind die Mengen viel kleiner (meist ein oder zwei Elemente), und M und J springen dann in groben Stufen.
- Nur zwei Annotator:innen und fünf Dokumentsammlungen; keine Konfidenzintervalle.
- Die Werte von M (1, 2/3, 1/3, 0) sind gesetzt, nicht empirisch begründet; die Motivation verweist auf Passonneau 2004 (S. 833).
- Die Brauchbarkeit wird über Korrelationen in einer getrennten Arbeit (Passonneau 2005) begründet, die nicht vorliegt.
- Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar: nicht berührt.

## Weiterführend

- Passonneau 2004, Computing reliability for coreference annotation, LREC (S. 831, 833): erste Fassung des Maßes und die Begründung der M-Stufen.
- Passonneau, Habash & Rambow 2006 (S. 831): MASI an Wortbedeutungen (WordNet, Omega); liegt als PDF vor.
- Rosenberg & Binkowski 2004, Augmenting the kappa statistic … multiply labeled data points, HLT/NAACL (S. 831): Alternative mit Hauptlabel.
- Di Eugenio & Glass 2004 (S. 832 bis 833, 836): Bias, mehrere Maße berichten.
- Krippendorff 1980, *Content Analysis*, S. 146 bis 147 (S. 833): Herkunft der 0,67.
- Artstein & Poesio 2005, Kappa³ = Alpha (or Beta), Technote (S. 833): Beta mit Gewichten; liegt nicht vor.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
