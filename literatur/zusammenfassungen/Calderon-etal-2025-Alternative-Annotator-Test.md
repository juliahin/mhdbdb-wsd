# Calderon, Reichart & Dror 2025: The Alternative Annotator Test for LLM-as-a-Judge

**Datei:** `pdf/Calderon-etal-2025-Alternative-Annotator-Test.pdf` (nur lokal; 31 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16. Gelesen: Hauptteil (S. 16051 bis 16060), Anhang A bis E (S. 16065 bis 16073); Literatur, Ergebnistabellen des Anhangs F und Prompts (Anhang G) nur überflogen. Tab. 1 (S. 16056) und Tab. 2 (S. 16057) am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology 2025.acl-long.782 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 16050 + n (PDF 1 = S. 16051, PDF 31 = S. 16081). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Calderon, Nitay; Reichart, Roi & Dror, Rotem (2025). The Alternative Annotator Test for LLM-as-a-Judge: How to Statistically Justify Replacing Human Annotators with LLMs. In: Wanxiang Che, Joyce Nabende, Ekaterina Shutova & Mohammad Taher Pilehvar (Hg.), *Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)*. Wien: Association for Computational Linguistics, S. 16051 bis 16081. ISBN 979-8-89176-251-0.
- **DOI/URL:** 10.18653/v1/2025.acl-long.782 (aufgelöst, Crossref, 2026-11-16); https://aclanthology.org/2025.acl-long.782/ (Herausgeber:innen, Ort, Monat Juli, ISBN nach dem BibTeX der Anthology). Code und Daten: https://github.com/nitaytech/AltTest (S. 16051, Fn. 1).
- **Lizenz:** CC BY 4.0 (ACL Anthology, Werke ab 2016, abgerufen 2026-11-16).
- **Art:** Konferenzbeitrag (Long Paper, begutachtet)
- **Sprache:** Englisch

## Worum es geht

Die Arbeit fragt, wann man statistisch begründet menschliche Annotierende durch ein LLM ersetzen darf, und schlägt dafür den „Alternative Annotator Test“ (alt-test) vor (S. 16051 bis 16052). Mit einem Leave-one-out-Verfahren wird für jede menschliche Person geprüft, ob das LLM mit den übrigen Annotierenden mindestens so gut übereinstimmt wie diese Person, abzüglich eines Kosten-Nutzen-Abschlags ε; die Einzeltests werden mit einer FDR-Korrektur zusammengefasst, und das LLM besteht, wenn es mindestens die Hälfte der Personen „schlägt“ (S. 16053 bis 16055). An zehn Datensätzen mit sechs LLMs besteht auf neun Datensätzen mindestens ein Modell mit irgendeiner Prompting-Variante den Test (S. 16052); zero-shot besteht auf zweien (MT-Bench, SummEval) keines, auf SummEval gelingt es erst mit Few-shot (S. 16057 bis 16058). Empfohlen werden mindestens drei Annotierende und 50 bis 100 Instanzen (S. 16052, 16059).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Es gibt kein Standardverfahren, um zu entscheiden, ob ein LLM Menschen ersetzen kann. Übliche Maße (Genauigkeit, F1, IAA-Kappas, Korrelation) haben Grenzen: IAA misst Übereinstimmung innerhalb einer Gruppe, gefragt ist der Vergleich des LLM mit der Gruppe; Mehrheitslabels übergehen Einzelne; es fehlen Entscheidungskriterien („is an F1 score of 0.6 sufficient?“). | S. 16051 bis 16052 | Position der Autor:innen |
| Rechtfertigung: Das LLM muss eine bessere Alternative zur Rekrutierung menschlicher Annotierender sein, unter Einrechnung seiner Kosten- und Zeitvorteile „as good as or better than human annotations“. | S. 16052 | Position |
| Gold-Labels werden als nicht verfügbar angenommen und durch die Gesamtheit mehrerer Annotierender angenähert. | S. 16053, Abschnitt 3 | Setzung |
| Verfahren: Für jede Person h_j wird pro Instanz ein Übereinstimmungswert S (Genauigkeit, negatives RMSE oder Ähnlichkeit) des LLM und von h_j mit den übrigen Personen berechnet; ρ^f_j ist der Anteil der Instanzen, in denen das LLM mindestens gleich gut ist, ρ^h_j umgekehrt. | S. 16054, Abschnitte 3.1 bis 3.2 | eigenes Verfahren |
| Hypothesen H0j: ρ^f_j ≤ ρ^h_j − ε, geprüft mit gepaartem t-Test; bei n < 30 ein nichtparametrischer Test (Wilcoxon). | S. 16054 bis 16055, Abschnitt 3.3 | eigenes Verfahren |
| Gewinnrate ω = Anteil der verworfenen Nullhypothesen nach Benjamini-Yekutieli-Korrektur (q = 0,05, wegen abhängiger Hypothesen); bei ω ≥ 0,5 darf das LLM ersetzen. Die 0,5 ist ein Hyperparameter, in heiklen Bereichen strenger. | S. 16055, mit Fn. 5 | eigenes Verfahren |
| Zum Vergleich mehrerer LLMs dient die mittlere Vorteilswahrscheinlichkeit ρ (Mittel der ρ^f_j): die Wahrscheinlichkeit, dass das LLM mindestens so gut ist wie eine zufällig gewählte Person. ω ist dafür zu grob (bei drei Personen nur 0, 1/3, 2/3, 1). | S. 16055, Abschnitt 3.4 | eigenes Maß |
| Theorem: Mit Genauigkeit als S ist das optimale LLM das Mehrheitsvotum, mit −RMSE der Mittelwert; beide erreichen ρ = 1. | S. 16056; Beweis S. 16071 bis 16072 | eigenes Ergebnis |
| Ergebnisse: Auf MT-Bench und SummEval besteht kein LLM; auf Framing, CEBaB-A, CEBaB-S und Lesion fast alle. Der Erfolg hängt vom Aspekt ab; schwierig sind Aspekte, die Kontextverständnis oder emotionale Intelligenz verlangen. | S. 16057 bis 16058, Tab. 2 | eigenes Ergebnis |
| Rangfolge der LLMs nach ρ und nach Genauigkeit korreliert stark (Kendall τ im Mittel 0,92 bei diskreten Aufgaben, 0,84 bei den übrigen), Ausnahme SummEval. | S. 16058 | eigenes Ergebnis |
| Few-shot (vier Beispiele mit Mehrheitslabel) verbessert fast alle LLMs; Chain-of-Thought verschlechtert in 45 % der Fälle; Ensembles bringen gegenüber Few-shot nichts. | S. 16057 bis 16058, Tab. 3 | eigenes Ergebnis |
| ω hängt stark von der Zahl der Instanzen ab (Teststärke), ρ im Erwartungswert nicht, nur seine Streuung. Mindestens 30 Instanzen für den t-Test; bei ε = 0,2 besteht das LLM meist vor 100, oft vor 50 Instanzen; bei ε = 0,1 braucht es typischerweise 100 bis 150. | S. 16058 bis 16059, Abb. 2 | eigenes Ergebnis |
| Empfehlung: mindestens drei Annotierende, 50 bis 100 Instanzen. | S. 16052, 16059 | Empfehlung |
| Mit zwei Annotierenden ist das Verfahren anwendbar, aber weniger verlässlich: Es prüft dann nur, ob das LLM mehr mit der einen als mit der anderen Person übereinstimmt, „lacking a consensus signal“. | S. 16065, Anhang A | Empfehlung |
| ε als Faustregel: 0,2 für Expert:innen, 0,15 für geschulte Annotierende (z. B. Studierende), 0,1 für Crowdworker. Wirksamer Bereich 0,05 bis 0,3: darüber bestehen fast alle LLMs, darunter fast keines. Jeder Wert ist gültig, wenn begründet. | S. 16065, 16067, Abschnitt B.1, Abb. 3 | eigenes Ergebnis und Empfehlung |
| Expert:innen bevorzugen; „If researchers themselves are experienced with the task, they can serve as annotators.“ | S. 16067, Abschnitt B.2 | Empfehlung |
| Bei schiefer Labelverteilung kann ein LLM, das immer die häufigste Klasse nennt, den Test wegen vieler Gleichstände bestehen (SummEval, Konsistenz: 89 % Note 5); Korrektur durch inverse Wahrscheinlichkeitsgewichtung. Das Vergleichs-Gold wird dabei ohne die ausgelassene Person gebildet, „ensuring the excluded annotator does not influence the gold label“. | S. 16068 bis 16069, Abschnitte B.3, C.1 | eigenes Ergebnis und Vorschlag |
| Varianten: eine einzelne Expertin als Gold gegen Nicht-Expert:innen (C.2), Qualitätsgewichte pro Person (C.3), subjektive Aufgaben (C.4), Test, ob LLMs Menschen übertreffen, mit vorhandenem Gold und ε = 0 (C.5). | S. 16069 bis 16070 | Vorschläge |
| Grenzen: mögliche Kontamination der verwendeten Datensätze (öffentliche Benchmarks wie SummEval und MT-Bench); bei hoher Uneinigkeit der Menschen besteht das LLM kaum; Missbrauch durch schwache Vergleichsannotierende ist im Einzel-Expert:innen-Fall nicht ausgeschlossen. Empfehlung, die menschlichen Annotationen zu veröffentlichen. | S. 16060, Abschnitt 7 | Selbsteinschätzung |

## Daten, Methode, Zahlen

- **Datensätze (Tab. 1, S. 16056, am Seitenbild geprüft):** zehn, diskret (WAX, LGBTeen, MT-Bench, Framing, CEBaB-A), kontinuierlich (SummEval, 10k Prompts, CEBaB-S, Lesion), Freitext (KiloGram); laut Text 3 bis 13 Annotierende pro Datensatz (S. 16052), Tab. 1 nennt für KiloGram aber 50; Crowdworker, Geschulte oder Expert:innen. Für diskrete Aufgaben Übereinstimmung der Paare („Agree“) und Fleiss' κ.
- **Am nächsten an WSD ist WAX** (Relationstyp zwischen zwei assoziierten Wörtern, 16 Kategorien, 8 Crowdworker, 246 Instanzen, Agree 0,33, Fleiss' κ 0,26; S. 16056, Beschreibung S. 16072). In Tab. 2 (S. 16057, ε = 0,1) erreichen Gemini-Pro und GPT-4o dort ω = 0,5 und bestehen knapp (ρ 0,74 bzw. 0,73), bei einer Genauigkeit gegen das Mehrheitsvotum von 0,39 bzw. 0,38.
- **LLMs:** Gemini-1.5-Flash und -Pro, GPT-4o und GPT-4o-mini, Llama-3.1 und Mistral-v3 (S. 16056); Prompts nach den Richtlinien der Datensätze, wo vorhanden (S. 16057).
- **Fortgeschrittene Varianten (Tab. 3, S. 16058):** Bootstrap über 100 Kombinationen aus drei Annotierenden und 100 Instanzen, fünf Datensätze; höchstens 300 annotierte Instanzen pro Datensatz (S. 16058, Fn. 11). Die Einzelwerte von Tab. 3 sind hier nicht übernommen [am PDF zu prüfen].

## Wörtliche Stellen

> „researchers should demonstrate that the LLM offers a better alternative to recruiting human annotators“ (S. 16052)

> „it involves comparing the LLM to a small group of human annotators (at least three) on a modest subset of examples (between 50 and 100).“ (S. 16052)

> „With only two, the procedure simply checks whether the LLM aligns more with one annotator than the other, lacking a consensus signal.“ (S. 16065)

> „If ω ≥ 0.5, we conclude that the LLM is more likely to hold an advantage over human annotators, which justifies using it.“ (S. 16053, Bildunterschrift Abb. 1)

## Bezug zur Dissertation

**1. PROTOKOLL §9.2, Punkt „LLM gegen menschliche Annotator:innen“ (Prinzip des Alternative Annotator Test).** Das Protokoll will prüfen, „ob das LLM mit den beiden Menschen so gut übereinstimmt wie diese untereinander“. Drei Unterschiede zum Werk:
- **Zahl der Annotierenden:** Das Werk empfiehlt mindestens drei (S. 16052, 16059); mit zwei bleibt nach dem Auslassen nur eine Person, und der Test vergleicht nur, ob das LLM der einen näher ist als der anderen (S. 16065). Mit Julia und Alan gilt also der vom Werk als „less reliable“ bezeichnete Fall, und ω kann nur 0, 0,5 oder 1 sein. Falls die vorgesehene dritte Person (KZW, A32) eine Teilmenge von mindestens 30, besser 50 bis 100 Items mitannotiert, wäre der Test in der empfohlenen Form auf dieser Teilmenge möglich. Sonst sollte das Protokoll den Test nur als „angelehnt an“ bezeichnen und die Einschränkung nennen.
- **Kriterium:** Das Werk misst nicht IAA gegen IAA, sondern pro Item, ob das LLM mit den übrigen Personen mindestens so gut übereinstimmt wie die ausgelassene Person, mit Abschlag ε, t-Test pro Person und BY-Korrektur (S. 16054 bis 16055). „Die menschliche IAA ist die Obergrenze“ ist eine andere Logik: Der alt-test lässt das LLM ausdrücklich besser sein als die Menschen und rechnet ihm über ε einen Kostenvorteil an (S. 16052, 16067). Für die Dissertation, deren Hauptfrage LLM gegen MFS ist, wäre ε = 0 (Variante C.5, S. 16070) die vorsichtigere Wahl, oder ε ausdrücklich begründet (S. 16067).
- **Gold aus denselben Personen:** Vergleicht man jede:n Annotator:in und das LLM mit dem adjudizierten Gold (§9.2, erster Punkt), sind die Menschen im Vorteil, weil ihr eigenes Label ins Gold eingegangen ist. Das Werk bildet das Vergleichslabel deshalb ohne die ausgelassene Person (S. 16068). Vorschlag: Beim Vergleich „jede:r gegen das Gold“ für die Gegenüberstellung mit dem LLM nur Items heranziehen, deren Gold ohne die jeweilige Person feststeht, oder die Verzerrung als Einschränkung nennen.

**2. A23 (LLM darf `MEHRERE` antworten, „dieselben Optionen wie die Menschen“, Prinzip des alt-test).** Ein ausdrückliches Prinzip „dieselben Optionen“ formuliert das Werk nicht. Es folgt aber aus dem Aufbau: S vergleicht die Ausgabe des LLM mit den menschlichen Annotationen im selben Labelraum (S. 16054), und die Prompts folgen, wo vorhanden, den Annotationsrichtlinien (S. 16057). Die Berufung ist vertretbar, sollte aber als Ableitung formuliert werden. Für Mengenlabels sieht das Werk kein eigenes S vor; eine MASI-Ähnlichkeit als SIM (S. 16054) wäre eine eigene Anpassung.

**3. PROTOKOLL §9.1 Punkt 4 (Prävalenz) und §9.2 (MFS-Baseline).** Das Werk zeigt, dass ein Annotator, der immer die häufigste Klasse wählt, bei schiefer Verteilung den Test bestehen kann (S. 16068). Bei WSD mit dominantem Sense gilt das für das LLM genauso, und das spricht dafür, die Übereinstimmung getrennt für MFS- und Nicht-MFS-Items zu berichten, wie es §9.1 Punkt 4 schon vorsieht.

**4. PROTOKOLL §9.1 Punkt 5 und §7 (Pilot, A32).** Die Mindestzahl von 30 Instanzen für den t-Test (S. 16059, 16065) und die Abhängigkeit von ω von n bestätigen, dass Pilotrunden zu 25 Items für einen alt-test zu klein wären; für die Stoppregel mit α ist das Werk nicht einschlägig.

**5. PROTOKOLL §10 (Kontamination).** Das Werk nennt Kontamination selbst als Grenze seiner Experimente und hofft, dass wenig bekannte oder nur auf Anfrage erhältliche Datensätze das Risiko senken (S. 16060). Zugleich empfiehlt es, die menschlichen Annotationen zu veröffentlichen (S. 16060). Beides passt zum Plan, die Labels erst mit der Publikation und verschlüsselt freizugeben.

**6. Abgleich mit `goldstandard/LITERATUR-IAA.md`** (Zeile „LLM ersetzt Menschen nur, wenn es mit ihnen so gut übereinstimmt wie diese untereinander“, Calderon, Reichart & Dror 2025 ○): Nur grob gedeckt. Genauer: Das LLM ersetzt, wenn es bei mindestens der Hälfte der Annotierenden mit den jeweils übrigen mindestens so gut übereinstimmt wie die ausgelassene Person, nach Abzug von ε, statistisch getestet (S. 16053 bis 16055); empfohlen sind mindestens drei Annotierende (S. 16052, 16065).

## Grenzen und Einwände

- Gold wird durch die Gesamtheit der Annotierenden angenähert; wo diese uneins ist, besteht das LLM kaum (S. 16060). Bei WSD mit feinen Senses ist das zu erwarten; WAX (Agree 0,33) liegt nahe an dieser Grenze.
- ε verschiebt das Ergebnis fast beliebig: über 0,3 bestehen nahezu alle LLMs (S. 16067). Die Faustregeln sind Setzungen der Autor:innen.
- Für Mehrfachlabels, Ausweichlabels (`KEINE_PASST`) und lemmaspezifische Label-Inventare gibt es kein eigenes Verfahren.
- Keine historischen Sprachen; alle Datensätze sind Englisch oder Bild-Text.
- Die Datensätze können selbst kontaminiert sein (S. 16060).

## Weiterführend

- Dror et al. 2018, The Hitchhiker's Guide to Testing Statistical Significance in NLP (S. 16054): Wahl des gepaarten Tests.
- Benjamini & Yekutieli 2001 (S. 16055, Algorithmus 1 S. 16071): FDR bei abhängigen Tests.
- Li et al. 2024a; Gu et al. 2024; Tan et al. 2024b; Pavlovic & Poesio 2024 (S. 16052): Übersichten zu LLM-as-a-judge.
- Liu et al. 2022, WAX (S. 16072): Datensatz zu Wortassoziationen, am nächsten an lexikalischer Semantik.
- Uma et al. 2021; Basile et al. 2021 (S. 16060): Uneinigkeit als Merkmal statt Fehler.
- Angelopoulos et al. 2023 (prediction-powered inference); Egami et al. 2023 (S. 16053): statistische Korrekturen für Schätzungen mit LLM-Labels.

## Julias Notizen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
