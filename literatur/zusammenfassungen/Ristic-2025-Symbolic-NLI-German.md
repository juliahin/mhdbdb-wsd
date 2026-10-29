# Ristic 2025: Symbolic Natural Language Inference for German Open Information Extraction

**Datei:** `pdf/Ristic-2025-Symbolic-NLI-German.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->

**Stand:** 2026-10-29, ganze Arbeit an der rohen Textebene gelesen (PDF 1 bis 85); Tab. 6.1, 6.2, 6.5 und 6.7 an den Seitenbildern geprüft (PDF 60, 64, 66), Tab. 6.3, 6.4, 6.6 an der Textebene. Bibliografie an reposiTUm und DataCite geprüft; das lokale PDF ist textgleich mit dem reposiTUm-PDF (alle 85 Seiten, Vergleich der Textebene am 2026-10-29) und unterscheidet sich nur durch Julias Anmerkungen.

**Seitenzählung:** Vorspann römisch, gleich der PDF-Seite (Kurzfassung S. xi = PDF 11); ab Kapitel 1 gedruckte Seite = PDF-Seite minus 16 (S. 1 = PDF 17, Tab. 6.5 S. 48 = PDF 64). Zitiert wird die gedruckte Seite, die PDF-Seite in Klammern.

**Gewichtung:** Prio 3, Hintergrund. Die Kapitel zu NLP-Geschichte, OpenIE und Related Work (S. 5 bis 18 (PDF 21 bis 34)) und die Graphrepräsentation (S. 19 bis 34 (PDF 35 bis 50)) sind gelesen und nur knapp erfasst; ausführlicher sind Daten, Baselines, Ergebnisse und Fehleranalyse (S. 35 bis 55 (PDF 51 bis 71)).

## Bibliografie

- **Vollständig:** Ristic, Kristian, 2025. *Symbolic Natural Language Inference for German Open Information Extraction.* Diplomarbeit zur Erlangung des akademischen Grades Diplom-Ingenieur im Rahmen des Studiums Data Science, Fakultät für Informatik, Technische Universität Wien. Betreuung: Gábor Recski. Wien, 4. Mai 2025 (Titelblatt, PDF 1). 69 gezählte Seiten (reposiTUm, DataCite).
- **DOI/URL:** DOI 10.34726/hss.2025.130460 (DataCite: Publisher TU Wien, Typ „Diploma Thesis“, eingereicht 2025-05, Betreuer „Recski, Gábor“ als Supervisor); Handle http://hdl.handle.net/20.500.12708/216545; reposiTUm-Eintrag: Institut E194 Information Systems Engineering, Rechte „In Copyright“, Rechteinhaber Kristian Ristic (beides abgerufen 2026-10-29).
- **Art:** Abschlussarbeit (Diplomarbeit), nicht separat begutachtet veröffentlicht.
- **Sprache:** Englisch, Kurzfassung zusätzlich Deutsch (S. xi (PDF 11)); Daten deutsch.

## Worum es geht

Die Arbeit prüft automatisch, ob Antworten von Jus-Studierenden auf einen Fall die Kernpunkte einer Musterlösung enthalten, und fasst das als offene Informationsextraktion auf, die durch Textual Entailment validiert wird (S. xi, 1 bis 2 (PDF 11, 17 bis 18)). Die Musterlösung liefert relationale Tupel wie *prüfen(gutgläubig, Erwerb)*; Prämisse und Antwortsatz werden als Dependenzgraph mit drei Zusatzebenen dargestellt (GermaNet-Relationen, Morphologie aus spaCy und DWDSmor, regelbasierte Negation) und per Graph-Matching verglichen (S. 19 bis 33 (PDF 35 bis 49)). Evaluiert wird an einem einzigen Fall mit fünf Antworten (S. 35 bis 36 (PDF 51 bis 52)). Bestes Ergebnis: Precision 0,947, Recall 0,750, F1 0,837 mit Synonymen, STTS-Tags für Argumente und Negationsprüfung, gegenüber F1 0,800 für eine Satzembedding-Baseline (Tab. 6.1, 6.5). Generative LLMs werden nicht eingesetzt, nur als intransparente Alternative genannt (S. 2, 16 (PDF 18, 32)).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Forschungsfragen: (1) Erhöhen symbolische Regeln auf Grundlage deutscher Morphologie und Semantik Recall und Precision gegenüber zwei Baselines? (2) Wie wirken Komposita, Kasus und Genus auf regelbasierte Inferenz? (3) Senken Negationserkennung und morphologische Prüfungen falsch Positive? | S. 3 (PDF 19) | Fragestellung |
| LLMs arbeiten als Black Box und statistisch statt über explizites Schließen; das begrenzt ihre Eignung, wo transparente Begründung verlangt ist (Bildung, Recht). | S. 2 (PDF 18); S. 16 (PDF 32) | referiert (Zini & Awad 2022; Nie et al. 2020; McCoy et al. 2019) |
| Werden Widerspruch und Neutralität nicht unterschieden, reduziert sich NLI auf binäres RTE; die Arbeit sucht nur positive Belege für Entailment. | S. 12 (PDF 28); S. 28 bis 29 (PDF 44 bis 45); S. 39 (PDF 55) | Festlegung, referiert begründet |
| GermaNet liefert für jeden Konzeptknoten Synonyme, Hyperonyme und Hyponyme (Tiefe 2), und zwar für alle Senses des Lemmas; die WSD wird auf den Matching-Schritt verschoben. | S. 22 bis 23 (PDF 38 bis 39) | eigenes Design |
| Matching über ein pfadbasiertes Ähnlichkeitsmaß in GermaNet (Schwelle 0,9); bei mehreren Senses wird das Sense-Paar mit der höchsten Ähnlichkeit gewählt. | S. 29 bis 30 (PDF 45 bis 46) | eigenes Design |
| Negation: zweistufig, erst Negationsträger aus einem Lexikon mit Ausnahmemustern („nicht nur“, „kein anderer“), dann Skopus nach Typ (Partikel, NP-Negation, Präposition, Verb) über den Dependenzbaum, begrenzt durch Nebensatzgrenzen. | S. 26 bis 28 (PDF 42 bis 44) | eigenes Design, angelehnt an Carrillo de Albornoz et al. 2012 |
| Die Satzembedding-Baseline erreicht bei Schwelle 0,1 nur Precision 0,667, „only a marginal improvement“ gegenüber dem Raten der positiven Klasse (Precision 0,60). | S. 43 bis 44 (PDF 59 bis 60), Tab. 6.1 | eigenes Ergebnis |
| Strengere Strukturprüfung hebt Precision (bis 1,000) und senkt Recall; der offene Modus hat den besten F1, vermutlich wegen des engen Vokabulars der Domäne und möglicher Parserfehler. | Tab. 6.2, 6.6, S. 44, 49 (PDF 60, 65) | eigenes Ergebnis, eigene Deutung |
| Synonyme bringen unter den GermaNet-Relationen am meisten (F1 0,438 → 0,632); Hyperonyme bringen nichts. | Tab. 6.4, S. 46 (PDF 62) | eigenes Ergebnis |
| Ein falsch Positives entsteht, weil *handeln* in einem Sense als Synonym von *verkaufen* gilt: „The system's inability to perform accurate word sense disambiguation led to this incorrect match“. | S. 47 (PDF 63) | eigene Fehleranalyse |
| Negationsprüfung hebt in allen geprüften Konfigurationen die Precision, Recall bleibt gleich (sie filtert nur). | Tab. 6.7, S. 50 (PDF 66) | eigenes Ergebnis |
| Koreferenzauflösung ändert nichts, weil die Tupel Agens und Objekt oft weglassen; Kompositumzerlegung (GermaNet) hebt Precision auf 1,000, senkt aber Recall, z. B. weil *Fahrrad* in *Fahr* und *Rad* zerfällt. | Tab. 6.3, S. 45 bis 46 (PDF 61 bis 62) | eigenes Ergebnis |
| Verpasste Entailments: morphologische Variante (*Entgeltlichkeit* gegen *entgeltlich*), nötiges Fachwissen (ob 100 € „angemessen“ sind; Schluss vom fehlenden Eigentum auf den ausgeschlossenen derivativen Erwerb), Pronomen ohne Antezedens im Kontext. | S. 50 bis 51 (PDF 66 bis 67) | eigene Fehleranalyse |
| Der Autor zweifelt ein Gold-Label an: Ob eine Antwort, die den Kernpunkt nur impliziert, „should be considered fully correct“, sei fraglich. | S. 51 (PDF 67) | eigene Einschätzung |
| Grenzen: Abhängigkeit vom Parser (trainiert auf heise.de-Nachrichten 1996 bis 2001, auf Rechtstexten nicht evaluiert); nur Negation als Kontext; ein Token pro Prädikat oder Argument (Problem bei *sich handeln um* gegen *handeln*); nur Entailment; einfache WSD. | S. 54 bis 55 (PDF 70 bis 71) | eigene Einschränkung |
| Ausblick: schrittweise gelockerte Matching-Regeln mit Konfidenz; unsichere Treffer an eine Fachperson oder ein LLM weitergeben; hybride Systeme. | S. 56 (PDF 72) | Ausblick |

## Daten, Methode, Zahlen

**Daten:** österreichisches Zivilrecht, Material eines österreichischen Verlags für juristische Lehrmaterialien (S. 1, 13 (PDF 17, 29)). Geliefert wurden zwei Fälle; ausgewertet wird nur „Case 1“, weil nur dafür detaillierte Annotationen vorliegen (S. 35 (PDF 51)). Case 1: 8 Abschnitte, 18 Prämissenmuster (Tupel), 5 Antworten von Studierenden mit zusammen 53 Sätzen und 707 Tokens; das Gold markiert 24 Antwortabschnitte als korrekt und 16 als nicht korrekt (S. 36 (PDF 52)). 24 + 16 = 40 = 5 Antworten × 8 Abschnitte (eigene Rechnung; die Arbeit sagt nicht ausdrücklich, dass das die Einheit ist). Positive Klasse 60 % (S. 43 (PDF 59)).

**Gold, Annotation:** Die Tupel stammen aus den Musterlösungen des Datensatzes (S. 20 bis 21 (PDF 36 bis 37)), die Gold-Labels der Antworten ebenfalls aus dem gelieferten Material („annotated student attempts“, S. 35 (PDF 51)). Wer annotiert hat, nach welchen Richtlinien und mit welcher Übereinstimmung, steht nicht in der Arbeit.

**Werkzeuge:** spaCy-Modell `de_hdt_lg` (Hamburg Dependency Treebank, 261.821 Sätze, etwa 4,8 Mio. Tokens aus heise.de 1996 bis 2001, dazu WikiNER) (S. 36 (PDF 52)); GermaNet (Hamp & Feldweg 1997); DWDSmor; spaCy-Koreferenz (S. 22 bis 23, 37 (PDF 38 bis 39, 53)).

**Baselines:** (1) Satzembeddings mit `distiluse-base-multilingual-cased-v1`, Kosinus-Schwelle 0,1 bis 0,7; (2) das eigene System nur mit exaktem Lemma-Abgleich, ohne GermaNet, Morphologie, Negation und Strukturprüfung (S. 38 (PDF 54)). HOLMES fand keine Entailments (Recall 0) und wurde nicht weiter verwendet (S. 38 bis 39 (PDF 54 bis 55)).

**Metriken:** Precision, Recall, F1 über die positive Klasse; True Negatives werden nicht gezählt (S. 39 bis 40 (PDF 55 bis 56)).

**Ergebnisse** (Precision / Recall / F1):

- Satzembeddings (Tab. 6.1, S. 44 (PDF 60), am Bild geprüft): Schwelle 0,1: 0,667 / 1,000 / 0,800; 0,3: 0,630 / 0,708 / 0,667; 0,5: 0,615 / 0,333 / 0,432; 0,7: 0,667 / 0,083 / 0,148.
- Symbolische Baseline (Tab. 6.2, ebd., am Bild geprüft): offen 0,875 / 0,292 / 0,438; Pfad 0,833 / 0,208 / 0,333; exakte Dependenz 1,000 / 0,167 / 0,286.
- Vorverarbeitung (Tab. 6.3, S. 45 (PDF 61)): Koreferenz 0,875 / 0,292 / 0,438; Kompositumzerlegung 1,000 / 0,250 / 0,400.
- GermaNet (Tab. 6.4, S. 46 (PDF 62)): Synonyme 0,857 / 0,500 / 0,632; Hyponyme 0,889 / 0,333 / 0,485; Hyperonyme 0,875 / 0,292 / 0,438.
- Lemma- und Tag-Strategien (Tab. 6.5, S. 48 (PDF 64), am Bild geprüft): `lemma_tag_syno` 0,818 / 0,750 / 0,783; `lemma_tag_syno_negation` 0,947 / 0,750 / 0,837 (bester F1); `lemma_pos_syno_negation` 0,900 / 0,750 / 0,818; mit Genusprüfung jeweils niedrigerer Recall (0,667).
- Strukturmodi mit Synonymen (Tab. 6.6, S. 49 (PDF 65)): offen 0,857 / 0,500 / 0,632; Pfad 0,909 / 0,417 / 0,571; exakt 1,000 / 0,292 / 0,452.
- Negation (Tab. 6.7, S. 50 (PDF 66), am Bild geprüft): `lemma_lemma_synonyms` 0,857 → 1,000 Precision; `lemma_tag_syno_open` 0,818 → 0,947; `lemma_tag_syno_path` 0,812 → 0,929; Recall jeweils unverändert.

**Einordnung der Zahlen (eigene Rechnung, nicht in der Arbeit):** Alle Recall-Werte sind Vielfache von 1/24; ein einzelner Abschnitt verschiebt den Recall also um gut 4 Punkte. Raten der positiven Klasse ergäbe Precision 0,60, Recall 1,00 und F1 0,75. Der Abstand zwischen der Satzembedding-Baseline (F1 0,800) und dem besten System (0,837) entspricht damit wenigen Abschnitten. Rund 20 Konfigurationen und vier Schwellen werden auf denselben 40 Einheiten verglichen, ohne getrennten Entwicklungs- und Testteil; Intervalle oder Tests gibt es nicht.

**Erklärbarkeit:** Für jeden Treffer wird ein Datensatz mit Muster, Satz, Knotenzuordnung, Match-Typ (z. B. `equals_lemma`, `equals_synonyms`), Ähnlichkeitswert, Ergebnis der Strukturprüfung und Bewertung (TP/FP) gespeichert (Listing 4.1, S. 34 (PDF 50)).

**Generative KI beim Schreiben:** ChatGPT-4o zum Korrekturlesen mit angegebenem Prompt, DeepL für Rechtsbegriffe, Google Translate für Abstract und Danksagung, Grammarly (S. 59 (PDF 75)).

## Wörtliche Stellen

> „The crucial step of Word Sense Disambiguation (WSD) is deferred to the matching stage“ (S. 23 (PDF 39))

> „The system's inability to perform accurate word sense disambiguation led to this incorrect match based on an inappropriate synonym sense.“ (S. 47 (PDF 63))

> „The achieved precision of 0.667 is considered low, offering only a marginal improvement over simply guessing the positive class for every instance (which would achieve 60% precision).“ (S. 43 bis 44 (PDF 59 bis 60))

> „It is worth considering whether such an answer, which relies on implied legal reasoning […] rather than stating it explicitly, should be considered fully correct for assessment purposes.“ (S. 51 (PDF 67))

## Bezug zur Dissertation

- **Protokoll 4.10 (Freeze 2) und 4.7:** Die Arbeit wählt ihre beste Konfiguration aus rund 20 Varianten und vier Schwellen auf denselben 40 Einheiten, auf denen sie auch das Ergebnis berichtet (Tab. 6.1 bis 6.7; eigene Zählung). Der berichtete Bestwert ist deshalb optimistisch, und der Abstand zur Baseline liegt im Bereich weniger Items. Genau das verhindert Freeze 2: LLM-Konfiguration (Modell, Prompt, Temperatur, Läufe) vor der Hauptrunde festlegen, Varianten nur am Pilot-Pool vergleichen.
- **Protokoll 9.2 und A4 (MFS als Baseline, gepaarter Vergleich):** Der Autor misst seine Embedding-Baseline selbst am Raten der Mehrheitsklasse (S. 43 bis 44 (PDF 59 bis 60)). Rechnet man den F1 dieser trivialen Strategie aus (0,75), liegt die Baseline nur knapp und das beste System nicht weit darüber (eigene Rechnung). Das stützt zwei Festlegungen des Protokolls: eine triviale, datengetriebene Baseline (MFS) unter derselben Bewertungsregel wie das LLM rechnen, und den Vergleich gepaart auf denselben Items mit Test statt als Differenz zweier Punktwerte berichten.
- **Protokoll 9.2, `MEHRERE`-Regel und A14:** GermaNet-Relationen werden für alle Senses eines Lemmas angehängt, und es gilt das beste Sense-Paar (S. 23, 29 bis 30 (PDF 39, 45 bis 46)). Diese Nachsicht erzeugt nachweislich falsch Positive (*handeln* als *verkaufen*, S. 47 (PDF 63)). Das ist kein WSD-Bewertungsfall, illustriert aber Henrichs Einwand gegen die Regel „richtig, wenn einer der Senses passt“: Je großzügiger „irgendein Sense passt“ gezählt wird, desto höher fällt die Leistung aus. Die in A14 ergänzten Sensitivitätsauswertungen sind die passende Antwort; als Beleg Henrich zitieren, Ristic höchstens als Beispiel.
- **Protokoll 7 und A1, A5 (Gold aus Doppelannotation, Adjudikation mit Ursachencode):** Das Gold kommt ohne Angaben zu Annotator:innen, Richtlinien oder Übereinstimmung (S. 35 bis 36 (PDF 51 bis 52)), und der Autor bezweifelt selbst ein Label (S. 51 (PDF 67)). Das ist ein weiteres Gegenbeispiel für unkontrolliertes Gold; der Zweifel des Autors entspricht dem Ursachencode „Richtlinienlücke“ (ob implizite Nennung zählt).
- **Protokoll 6 (Kontext) und offener Punkt 12.4:** Ein verpasster Treffer geht auf ein Pronomen zurück, dessen Bezugswort im Kontext fehlt (S. 51 (PDF 67)). Für die Kontextfrage bestätigt das nur, dass ein satzbegrenzter Ausschnitt Fälle unentscheidbar macht; ein Richtwert ergibt sich daraus nicht.
- **Protokoll 8 und `PROMPT-LOG.md`, Ebene A:** Der Trefferdatensatz in Listing 4.1 (S. 34 (PDF 50)) hält pro Entscheidung fest, worauf sie beruht (Match-Typ, Ähnlichkeit, Strukturprüfung). `PROMPT-LOG.md` sieht mit `ausgabe_roh` und `label` schon Rohantwort und geparstes Ergebnis vor. Ergänzbar wäre, beim Parsen festzuhalten, nach welcher Regel das Label gewonnen wurde oder warum es scheiterte, damit sich LLM-Fehler später nach Ursache sortieren lassen (Vorschlag, nicht aus der Arbeit).
- **Hintergrund für Kapitel zu Methoden:** Die Arbeit ist ein aktueller Beleg aus Wien, dass in Bildungs- und Rechtskontexten bewusst auf LLMs verzichtet wird, weil Entscheidungen begründbar sein müssen (S. 2 (PDF 18)). Für die Dissertation trägt das nur als Stimme in der Debatte; als Primärquellen für die Black-Box-Kritik die von Ristic zitierten Arbeiten nehmen (McCoy et al. 2019 u. a.).

## Grenzen und Einwände

- Diplomarbeit, nicht begutachtet veröffentlicht; Gegenwartsdeutsch, Rechtssprache, ein einziger Fall mit fünf Antworten. Für Mittelhochdeutsch, ein onomasiologisches Inventar oder LLM-Evaluation liefert die Arbeit keine Zahlen.
- WSD ist hier Nebenprodukt, kein Untersuchungsgegenstand: kein Sense-Gold, keine WSD-Evaluation, nur eine Fehlerbeobachtung (S. 47, 55 (PDF 63, 71)).
- Herkunft und Qualität des Golds undokumentiert; Konfigurationswahl auf den Testdaten; keine Intervalle, kein Test (siehe oben).
- Die Einheit der Auswertung ist uneinheitlich beschrieben: Nach S. 33 (PDF 49) entscheidet das System pro Abschnitt, ob irgendein Muster in irgendeinem Satz passt; nach S. 39 (PDF 55) wird jedes Paar aus Muster und Satz klassifiziert. Die Recall-Werte passen zur ersten Lesart (24 positive Abschnitte; eigene Rechnung).
- Auf S. 38 (PDF 54) ist von „the simplified premise sentences (as used in the LLM baseline)“ die Rede; eine LLM-Baseline beschreibt die Arbeit nirgends.
- Der Parser ist auf Nachrichtentexten von 1996 bis 2001 trainiert und auf der Zieldomäne nicht geprüft (S. 54 bis 55 (PDF 70 bis 71)); die Arbeit nennt das selbst als Schwäche.

## Julias Markierungen

Alle 11 Anmerkungen (10 Hervorhebungen, 1 Randzeichen) liegen auf der deutschen Kurzfassung (S. xi (PDF 11)): Aufgabe (Bewertung offener Antworten anhand von Musterlösungen, juristischer Bereich), Konzeption als durch Implikation validierte Informationsextraktion, Korrektheitsbedingung, symbolisches Framework, grafische Wissensrepräsentation auf Basis von Dependency Parsing und die drei Ebenen (lexikalisch, Eigenschaften, Kontext mit Negation). Das Randzeichen steht neben den fünf Zeilen, die die Ebenen beschreiben.

- **Aufgenommen:** Aufgabenzuschnitt und Korrektheitsbedingung (Worum es geht), die drei Ebenen samt GermaNet und Negation (Kernaussagen, Daten).
- **Nur knapp:** die Graphrepräsentation im Einzelnen (Konzept-, Eigenschafts-, Kontextebene, S. 19 bis 28 (PDF 35 bis 44)); sie ist Technik des Systems und trägt für die WSD-Evaluation nur über die Sense-Heuristik bei, die unter „Bezug“ steht.

## Julias Notizen im PDF

Keine; die Anmerkungen sind nur Hervorhebungen und ein Randzeichen.

## Weiterführend

- Kalouli & Crouch 2018, GKR (Workshop on Computational Semantics beyond Events and Roles, S. 27 bis 37), und Kalouli, Crouch & de Paiva 2020, Hy-NLI (COLING 2020, S. 5235 bis 5249) (zitiert S. 17, 20 (PDF 33, 36)): Vorbild der Graphrepräsentation; Hy-NLI kombiniert symbolische Inferenz mit LLMs; nicht geprüft.
- McCoy, Pavlick & Linzen 2019, „Right for the wrong reasons“ (zitiert S. 2 (PDF 18)): Heuristiken statt Inferenz in NLI-Modellen; Primärquelle für die Black-Box-Kritik; im Literaturverzeichnis ohne Venue; nicht geprüft.
- Carrillo de Albornoz et al. 2012, UCM-I (*SEM 2012) (zitiert S. 26 (PDF 42)): regelbasierter Negationsskopus; nicht geprüft.
- Sainz et al. 2022, Textual Entailment for Event Argument Extraction (Findings of NAACL 2022, S. 2439 bis 2455) (zitiert S. 16 (PDF 32)): Entailment als Verfahren für Informationsextraktion mit wenigen Annotationen; nicht geprüft.
