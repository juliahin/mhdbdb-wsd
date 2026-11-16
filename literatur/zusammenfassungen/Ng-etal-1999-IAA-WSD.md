# Ng, Lim & Foo 1999: A Case Study on Inter-Annotator Agreement for WSD

**Datei:** `pdf/Ng-etal-1999-IAA-WSD.pdf` (nur lokal; 6 PDF-Seiten, die letzte leer)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, alle fünf Textseiten am Seitenbild geprüft (die Textebene ist eine fehlerhafte OCR eines Scans; Zahlen, Formel und Tabellen nur nach Seitenbild übernommen). Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology W99-0502 (SHA-256 verglichen am 2026-11-13); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 8 + n (PDF 1 = S. 9, Zahl am Seitenbild kaum lesbar; PDF 2 bis 5 = S. 10 bis 13; PDF 6 leer). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Ng, Hwee Tou, Chung Yong Lim & Shou King Foo (1999). A Case Study on Inter-Annotator Agreement for Word Sense Disambiguation. In: *SIGLEX99: Standardizing Lexical Resources*, S. 9 bis 13.
- **DOI/URL:** keine DOI (ACL Anthology ohne DOI, abgerufen 2026-11-13); https://aclanthology.org/W99-0502/
- **Angaben:** Titel, Autoren und Band nach Titelseite und ACL Anthology ✔; Seiten nur am PDF (gedruckte Seitenzahlen 10, 11, 13 am Seitenbild klar, 9 und 12 erschlossen), die Anthology nennt keine Seiten, Ort und Monat. Passonneau et al. (2010, S. 3248) zitieren den Band als „SIGLEX Workshop On Standardizing Lexical Resources“.
- **Lizenz:** CC BY-NC-SA 3.0 (FAQ der ACL Anthology: ACL-Material vor 2016, abgerufen 2026-11-13)
- **Art:** Workshopbeitrag (SIGLEX-Workshop)
- **Sprache:** Englisch

## Worum es geht

Die Autoren vergleichen zwei unabhängig entstandene Sense-Annotationen derselben Sätze: die Schnittmenge aus WordNet-SemCor und DSO-Korpus, 30.315 Sätze mit je einem getaggten Vorkommen eines von 191 häufigen englischen Nomen und Verben (S. 9 bis 10). Die Rohübereinstimmung beträgt nur 56,7 %, der mittlere κ 0,317 (S. 10 bis 11, Tab. 1). Ein gieriger Suchalgorithmus legt pro Wort so lange Senses zusammen, bis κ 0,8 erreicht (S. 11); bei 95 Wörtern gelingt das mit mindestens zwei groben Klassen, die Übereinstimmung steigt dann auf über 93 % (S. 11 bis 13, Tab. 2 und 3). Die Autoren sehen die so gewonnenen groben Klassen, nach menschlicher Prüfung, als besseres Inventar für die WSD-Evaluation (S. 9, 12).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Wörterbücher teilen den „semantic space“ verschieden auf, und WordNet unterscheidet häufige Wörter sehr fein; zwei Annotator:innen können daher „genuinely disagree“. | S. 9, Abschnitt 1 | Position der Autoren |
| Die Übereinstimmung zwischen Menschen bildet die Obergrenze („upper ceiling“), an der WSD-Systeme gemessen werden. | S. 9 | Position der Autoren, mit Verweis auf SENSEVAL (Kilgarriff 1998) |
| Daten: Schnittmenge aus SemCor (Brown-Korpus, WordNet 1.6) und DSO-Korpus (Brown und Wall Street Journal, 191 Wörter, 121 Nomen und 70 Verben, WordNet 1.5, DSO-Senses auf 1.6 umgerechnet). Sätze mit Sense 0 oder −1 (kein Sense passt) im DSO-Korpus wurden ignoriert. Ergebnis: 13.188 Satzpaare mit Nomen, 17.127 mit Verben, zusammen 30.315. | S. 9 bis 10, Abschnitte 2 und 3 | eigene Datenaufbereitung |
| Maß: Rohübereinstimmung P_a = A/N und κ mit P_e = Σ_j (C_j/2N)², wobei C_j die Zahl der Vergaben von Sense j durch beide Annotationen zusammen ist; κ ≥ 0,8 gilt „as indicating good agreement“ (Carletta 1996). Der Durchschnitts-κ ist ein einfacher Mittelwert der κ-Werte der einzelnen Wörter. | S. 10, Abschnitt 4 | Maß referiert (Cohen 1960, Carletta 1996), Mittelung eigene Wahl |
| Rohübereinstimmung auf allen 30.315 Sätzen 57 %; das deckt sich mit einem früheren Schnelltest auf 5.317 Sätzen. | S. 10; Tab. 1 S. 11 | eigenes Ergebnis |
| Gieriger Algorithmus: pro Wort in jedem Schritt das Paar von Sense-Klassen zusammenlegen, das den höchsten κ ergibt, bis κ ≥ κ_min = 0,8. | S. 11 bis 12, Abschnitt 5, Abb. 1 | eigenes Verfahren |
| Bei 95 Wörtern (53 Nomen, 42 Verben) erreicht der Algorithmus κ ≥ 0,8 mit mindestens zwei Klassen; bei den übrigen 96 Wörtern nur, indem er alle Senses zu einer einzigen trivialen Klasse zusammenlegt. | S. 11, Abschnitt 6 | eigenes Ergebnis |
| Für die 53 Nomen steigt κ durch das Zusammenlegen von 0,463 auf 0,862, die Übereinstimmung von 63,4 % auf 94,3 %; für die 42 Verben κ von 0,441 auf 0,852. | S. 11 bis 13, Tab. 2 und 3 | eigenes Ergebnis |
| Beispiel *change* (111 Sätze, sieben Senses): P_a = 0,38, κ = −0,09, also systematische Nichtübereinstimmung; nach Zusammenlegen zu zwei Klassen („modification vs coins“) P_a = κ = 1. | S. 11 bis 12, Abb. 2 | eigenes Ergebnis |
| Für durchschnittliche Sprachnutzer:innen ist hohe Übereinstimmung mit feinen WordNet-Senses bei knappen Definitionen und wenigen Beispielen schwer; bei SENSEVAL erreichten Lexikograph:innen mit dem ausführlicheren HECTOR-Wörterbuch hohe Werte. | S. 11, Abschnitt 7 | Deutung der Autoren, Vergleich mit Véronis 1998 und SENSEVAL |
| Ein Teil der Abweichungen sei allein den zu feinen WordNet-Senses zuzuschreiben; die gefundenen Gruppierungen entsprächen der intuitiven Granularität (Tab. 4: z. B. *board* „committee vs plank“, *field* „land vs subject“). | S. 11 bis 13, Tab. 4 | Deutung der Autoren |

## Daten, Methode, Zahlen

**Tab. 1, Rohübereinstimmung (S. 11, am Seitenbild geprüft):**

| Typ | Wörter | A | N | P_a | Ø κ |
|---|---|---|---|---|---|
| Nomen | 121 | 7.676 | 13.188 | 0,582 | 0,300 |
| Verben | 70 | 9.520 | 17.127 | 0,556 | 0,347 |
| Alle | 191 | 17.196 | 30.315 | 0,567 | 0,317 |

(Die Textebene liest bei den Verben 0,555; das Seitenbild zeigt 0,556, und 9.520/17.127 ergibt gerundet 0,556.)

**Tab. 2 und 3, vor und nach dem Zusammenlegen (S. 12 und 13, am Seitenbild geprüft):**

| Gruppe | Ø Senses | A | N | P_a | Ø κ |
|---|---|---|---|---|---|
| 53 Nomen vorher | 7,6 | 3.387 | 5.339 | 0,634 | 0,463 |
| 53 Nomen nachher | 4,0 | 5.033 | 5.339 | 0,943 | 0,862 |
| 42 Verben vorher | 12,8 | 5.115 | 8.602 | 0,595 | 0,441 |
| 42 Verben nachher | 5,6 | 8.042 | 8.602 | 0,935 | 0,852 |

**Annotator:innen:** keine Einzelpersonen, sondern „two separate groups of human annotators“ (S. 9), die SemCor- und die DSO-Annotation. Über Zahl, Ausbildung und Richtlinien der beiden Gruppen sagt der Beitrag nichts; S. 11 spricht von „average language users“.

## Wörtliche Stellen

> „Hence, two human annotators may genuinely disagree in their sense assignment to a word in context.“ (S. 9)

> „The agreement rate between human annotators will then form the upper ceiling against which to compare the performance of WSD algorithms.“ (S. 9)

> „The average κ reported in the table is a simple average of the individual κ value of each word.“ (S. 10)

## Bezug zur Dissertation

**1. PROTOKOLL §9.1 Punkt 3 (Zufallsmodell pro Lemma).** Das Protokoll schreibt, für eine pro Lemma berechnete erwartete Übereinstimmung sei kein etablierter Standard gefunden worden. Ng et al. rechnen κ **pro Wort** (P_e aus den Sense-Anteilen dieses Worts) und mitteln die Wortwerte ungewichtet (S. 10). Das ist eine veröffentlichte, verwandte Konstruktion, allerdings mit vielen Sätzen pro Wort (im Mittel etwa 159, eigene Rechnung 30.315/191) und nicht als gepoolter Wert über Items wie im Protokoll. Vorschlag: Ng et al. in §9.1 Punkt 3 als Vorbild für die Zufallsschätzung innerhalb des Lemmas nennen und den Unterschied (Mittel der Wortwerte gegenüber Summe über Items) begründen. Hinweis zur Formel: P_e = Σ(C_j/2N)² nutzt die gemeinsame Verteilung beider Annotationen; nach der Einteilung von Artstein & Poesio (2008, S. 561 bis 562) ist das Scotts π, obwohl die Autoren Cohen (1960) zitieren und von κ sprechen.

**2. A32 und LITERATUR-IAA (α nahe an der Rohübereinstimmung).** Ng et al. zeigen das Gegenstück: Wird der Zufall innerhalb jedes Worts geschätzt, liegt der Wert weit unter der Rohübereinstimmung (Ø κ 0,317 bei 56,7 %, Tab. 1). Das stützt die Aussage in A32 nur indirekt, nämlich dass die Wahl zwischen gepooltem und wortweisem Zufallsmodell den Wert stark bestimmt. Für die Schwelle folgt: Ein gepooltes α von 0,80 ist nicht mit wortweisen κ-Werten aus der WSD-Literatur wie diesen vergleichbar.

**3. PROTOKOLL §9.1 Punkt 7 und Hovy-Bezug (Granularität).** Gestützt: Granularität bestimmt die Übereinstimmung stark (S. 11 bis 13). Einschränkung für das Zitat: Der Anstieg von 0,463 auf 0,862 entsteht durch ein Verfahren, das auf denselben Daten so lange zusammenlegt, bis κ ≥ 0,8 erreicht ist (S. 11), und gilt nur für die 53 Nomen, bei denen das mit mindestens zwei Klassen gelang. Der Wert nach dem Zusammenlegen ist damit zum Teil durch das Abbruchkriterium festgelegt. Das ist genau der Fall, den Artstein & Poesio (2008, S. 588) meinen: nachträgliches Zusammenlegen ist keine Studie mit groben Kategorien. Das Protokoll zieht daraus die richtige Folge (grobe Ebene vorab definieren).

**4. Abgleich mit `goldstandard/LITERATUR-IAA.md`** (Ng et al. dort ✔):
- Zeile „Prävalenz … In WSD verschiebt allein das Zufallsmodell κ stark: 57 % Übereinstimmung, κ = 0,317 (Ng et al.)“: **Die Zahlen stimmen** (Tab. 1, S. 11), **die Deutung steht nicht im Werk.** Ng et al. vergleichen keine Zufallsmodelle und sprechen nicht von Prävalenz; 56,7 % ist die gepoolte Rohübereinstimmung, 0,317 der Mittelwert der Wort-κ. Der Abstand ist also teils ein Effekt der Mittelung pro Wort. Vorschlag: als Beleg für „niedriger κ bei mittlerer Rohübereinstimmung im WSD“ belassen, für „allein das Zufallsmodell“ nicht.
- Zeile „Zusammenlegen von Senses hob κ von 0,46 auf 0,86“: Zahlen gedeckt (Tab. 2, S. 12), mit der Einschränkung aus Punkt 3. Achtung Verwechslung: Artstein & Poesio (2008, S. 588) nennen fast dieselben Zahlen für Véronis 1998 (Nomen, von etwa 0,45 auf 0,86).
- Zeile „Typische Werte: feinkörnig (WordNet) ca. 67 bis 72 %“: Ng et al. liegen mit 56,7 % (Tab. 1) **darunter**; als Beleg für diese Spanne taugen sie nicht, eher als Beispiel für den unteren Rand.

**5. PROTOKOLL §9.2 (LLM gegen menschliche Annotator:innen als Obergrenze).** Gestützt durch S. 9 („upper ceiling“).

**6. PROTOKOLL §6 (`KEINE_PASST`).** Das DSO-Korpus kennt eigene Codes für „kein Sense passt“ (0 und −1); Ng et al. lassen diese Sätze für den Vergleich weg (S. 10). Das Protokoll behandelt `KEINE_PASST` dagegen als eigene Kategorie (§9.1). Beim Vergleich mit Ng-Werten beachten: dort ist dieser Fall ausgeschlossen.

## Grenzen und Einwände

- Keine kontrollierte Doppelannotation: Die beiden „Annotator:innen“ sind zwei Projekte mit verschiedenen Richtlinien, Personen und WordNet-Versionen (1.5 und 1.6, umgerechnet); ein Teil der Abweichung kann aus Umrechnung und Richtlinien kommen (S. 10, Anm. 1).
- Nur zwei Wortarten, 191 häufige englische Wörter.
- Die Werte nach dem Zusammenlegen sind auf denselben Daten optimiert und vom Abbruchkriterium mitbestimmt; keine Prüfung an neuen Daten. Die Gruppen sollen laut den Autoren erst nach menschlicher Prüfung als Inventar dienen (S. 12).
- Ungewichtete Mittelung der Wort-κ: Wörter mit wenigen Sätzen zählen gleich viel wie häufige.
- Übertragbarkeit: Das Ergebnis betrifft ein semasiologisches Inventar (WordNet). Für die MHDBDB, deren Senses Mengen von Begriffen sind, ist offen, ob gröbere Ebenen (Oberbegriffe) ähnliche Sprünge zeigen.

## Weiterführend

- Véronis 1998, A study of polysemy judgements and inter-annotator agreement (S. 11, 12): naive Annotator:innen, geringe Übereinstimmung; auch bei Artstein & Poesio 2008 referiert.
- Bruce & Wiebe 1998, Word-sense distinguishability and inter-coder agreement, EMNLP (S. 12): datengetriebene Sense-Klassen über ein Latent-Class-Modell.
- Kilgarriff 1998a bis c (S. 9): SENSEVAL-Übereinstimmung mit Lexikograph:innen.
- Carletta 1996 (S. 10): Herkunft der 0,8-Schwelle in der CL.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
