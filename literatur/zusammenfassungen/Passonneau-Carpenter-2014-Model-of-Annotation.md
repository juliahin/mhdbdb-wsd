# Passonneau & Carpenter 2014: The Benefits of a Model of Annotation

**Datei:** `pdf/Passonneau-Carpenter-2014-Model-of-Annotation.pdf` (nur lokal; 16 Seiten, S. 16 ohne Text außer der Seitenzahl)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen; Abb. 3 (S. 317) und Abb. 5 (S. 319) am Seitenbild geprüft, Abb. 3 zusätzlich aus der Textebene ausgezählt. Abb. 4, 6, 7 und 8 (Diagramme, S. 318 bis 323) nur über Bildunterschriften und Fließtext [Werte am PDF zu prüfen]. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology Q14-1025 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: gedruckte Seite = PDF-Seite + 310 (PDF 1 = S. 311, PDF 16 = S. 326). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Passonneau, Rebecca J. & Bob Carpenter (2014). The Benefits of a Model of Annotation. *Transactions of the Association for Computational Linguistics* 2, S. 311 bis 326.
- **DOI/URL:** 10.1162/tacl_a_00185 (aufgelöst, führt zu MIT Press; Crossref); https://aclanthology.org/Q14-1025/ (Herausgeber:innen des Bandes Dekang Lin, Michael Collins & Lillian Lee, Verlag MIT Press, Cambridge, MA, nach dem BibTeX der Anthology, abgerufen 2026-11-16)
- **Daten im PDF:** „Submitted 2/2014; Revised 6/2014; Published 10/2014“, Action Editor Chris Callison-Burch (S. 311); Crossref nennt Dezember 2014 als Erscheinungsdatum.
- **Lizenz:** im PDF „©2014 Association for Computational Linguistics“ (S. 311); laut FAQ der ACL Anthology steht ACL-Material vor 2016 unter CC BY-NC-SA 3.0 (abgerufen 2026-11-16); die Artikelseite bei MIT Press war nicht abrufbar (HTTP 403), eine dort genannte Lizenz ist nicht geprüft.
- **Art:** begutachteter Zeitschriftenartikel
- **Sprache:** Englisch

## Worum es geht

Die Arbeit bestreitet, dass hohe Übereinstimmung zwischen Annotator:innen die Qualität eines Goldstandards sichert, und setzt dem ein probabilistisches Annotationsmodell entgegen (Dawid & Skene 1979), das für jede Person Genauigkeit und Verzerrung pro Kategorie schätzt und für jedes Item eine Wahrscheinlichkeit des wahren Labels liefert (S. 311 bis 316). Fallstudie ist WSD mit WordNet-Senses: 45 Wörter aus dem MASC-Korpus, für die geschulte Studierende Übereinstimmungen von α = 0,02 bis 0,85 erreicht hatten, werden über Amazon Mechanical Turk mit bis zu 25 Labels pro Satz neu annotiert (S. 317 bis 319). Für 42 der 45 Wörter haben 80 % der geschätzten Labels eine Wahrscheinlichkeit über 0,99, auch bei Wörtern mit niedriger Übereinstimmung der Geschulten (S. 320); die Kosten pro Label lagen unter der Hälfte (S. 322).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Hohe zufallskorrigierte Übereinstimmung ist für Goldlabels hoher Qualität „neither necessary nor sufficient“. | S. 311 Abstract und Einleitung | These der Autor:innen, begründet S. 312 bis 313 |
| Übereinstimmungsmaße sind höchstens ein indirektes Maß für die Sicherheit der Labels; sie sagen nichts über einzelne Items und unterscheiden nicht zwischen Annotator:innen. | S. 312; S. 323 | Argument der Autor:innen |
| Übliche Praxis: Aufgabe entwerfen, Richtlinien schreiben, Stichprobe unabhängig doppelt annotieren, Übereinstimmung messen, iterieren; danach wird das Gold von je einer Person annotiert. Ob die Übereinstimmungsstichprobe für das Korpus repräsentativ ist, wird kaum gefragt. | S. 312 | Beschreibung und Kritik der Autor:innen |
| Sechs Schwächen von Übereinstimmungskoeffizienten: (1) paarweise; (2) zwei gleiche Fehler zählen als Übereinstimmung; (3) bei hoher Zufallsübereinstimmung (schiefe Verteilung) kann κ auch bei genauen Annotator:innen niedrig sein; (4) gleichgerichtete Verzerrung, etwa zur häufigsten Kategorie, überschätzt die Genauigkeit; (5) Itemschwierigkeit kann Übereinstimmung im Irrtum erhöhen; (6) selten mit Konfidenzintervallen, die breit sind. | S. 313 bis 314 | Argument der Autor:innen, (3) mit Verweis auf Feinstein & Cicchetti 1990 |
| Rechenbeispiel zu (3): binär, 95 % Prävalenz, zwei zu 90 % genaue Annotator:innen ergeben einen zufallskorrigierten Wert von −0,053. | S. 313 | Rechnung der Autor:innen |
| Rechenbeispiel zu (6): 80 von 100 richtig ergibt ein 95-%-Intervall für die Genauigkeit von etwa 74 % bis 86 %; Übereinstimmungsmaße haben noch breitere Grenzen; Bootstrap ist eine verlässliche Methode für Intervalle; bei nicht unabhängigen Items wird das Intervall breiter. | S. 314, Fn. 3 | Rechnung und Empfehlung der Autor:innen |
| Das Dawid-Skene-Modell schätzt Prävalenz der Kategorien, Antwortmatrix jeder Person und wahres Label pro Item; eine Mehrheitsentscheidung kann dem geschätzten Label widersprechen (Beispiel: Mehrheit für Kategorie 1, Modell 0,89 für Kategorie 2). | S. 314 bis 315 | Modell referiert (Dawid & Skene 1979), Beispiel eigen |
| Auch verzerrte, ungenaue Annotator:innen können viel Information über das wahre Label liefern; gewichtete Abstimmung ist deshalb nicht der richtige Weg. | S. 315 bis 316 | Argument der Autor:innen |
| Im MASC-Korpus wurde jedes Wort in einer einzigen Runde annotiert, ohne Iteration bis zu einer Schwelle; nur 100 von 1.000 Sätzen pro Wort hatten zwei bis vier Annotator:innen. | S. 317 bis 318 | Beschreibung der eigenen Vorarbeit |
| Übereinstimmung der Geschulten korreliert nicht mit der Zahl verfügbarer oder benutzter Senses. | S. 317 bis 318 | referiert (Passonneau et al. 2012a) |
| Für 42 von 45 Wörtern haben 80 % der geschätzten Labels eine Wahrscheinlichkeit über 0,99; bei *help* (α = 0,26) 81 % der Items, bei *date* 97 %. | S. 319 bis 320, Abb. 5 | eigenes Ergebnis |
| Verzerrung zu häufigen Senses war meist gering; die mittlere Genauigkeit pro Wort lag zwischen 0,05 und 0,86 und war für häufigere Senses höher. | S. 315; S. 321 | eigenes Ergebnis |
| Der Anteil gleicher Labels von Geschulten und Modell korreliert nicht mit α oder paarweiser Übereinstimmung der Wörter. | S. 321 | eigenes Ergebnis |
| Abweichungen zwischen Geschulten und Crowd hängen teils an Senses, die WordNet später entfernte (*meet*, *date*); Wörter mit wenigen sicheren Labels ließen sich oft durch Überarbeitung des Inventars verbessern. | S. 321 bis 322 | eigenes Ergebnis und Deutung |
| Bei Wortbedeutung beruht die Ground Truth auf dem Konsens der Sprachgemeinschaft; keine einzelne Person kann die Labels verlässlich vergeben. | S. 323 | Position der Autor:innen |
| Labels mit Sicherheitswert erlauben es Nutzer:innen, unsichere Labels in der WSD-Evaluation geringer zu gewichten oder Systeme für „incorrect but close“ Antworten milder zu bestrafen. | S. 322; S. 324 | Vorschlag der Autor:innen |

## Daten, Methode, Zahlen

- **MASC-Wortsinnkorpus:** 116 Wörter, je etwa 1.000 Sätze, Nomen, Adjektive und Verben fast gleich verteilt, WordNet-Senses; Annotation durch Studierende (Vassar, Barnard, Columbia) nach allgemeiner Schulung und 50 Übungssätzen pro Wort mit Christiane Fellbaum; Werkzeug zeigte die WordNet-Senses mit Beispielen und vier Varianten von „none of the above“ (S. 317). 17 Studierende, etwa 80.000 US-Dollar, 0,70 US-Dollar pro Label (S. 322).
- **Abb. 3 (S. 317, Seitenbild):** 45 zufällig gewählte MASC-Wörter mit verfügbaren und benutzten Senses, α und paarweiser Übereinstimmung der Geschulten. α reicht von 0,02 (*normal*) bis 0,85 (*late*), Median 0,49; paarweise Übereinstimmung 0,32 bis 0,95, Median 0,66 (aus der Textebene ausgezählt). Nur 5 Wörter erreichen α ≥ 0,67, nur 2 α ≥ 0,80.
- **Crowd-Annotation:** 45 Wörter, Sätze aus demselben Pool, WordNet 3.0, 20 bis 25 Labels pro Item, keine Schulung, zehn Sätze pro HIT mit den Senses unter jedem Satz (S. 318 bis 319); 228 Turker, Mindestanforderungen 98 % Annahmequote und 20.000 erledigte HITs, fünf gesperrt und einer wieder entsperrt, ihre Daten bleiben in der Auswertung (S. 319); 15.000 US-Dollar, 0,33 US-Dollar pro Label (S. 322).
- **Abb. 5 (S. 319, Seitenbild):** Anteil der Items mit Posterior ≥ 0,99: *add* 94 %, *date* 97 %, *help* 81 %, *ask* 83 %. Bei *help* haben von den übrigen 19 % noch 13 % einen Posterior über 0,75 (S. 320).
- **Schätzung:** EM, sehr schwache Dirichlet-Priors, Code in R; Itemschwierigkeit nicht modelliert, was die Intervalle verbreitern würde (S. 316).
- **Unstimmigkeiten im Werk:** S. 320 nennt 20 der 45 Wörter mit α unter 0,50; in Abb. 3 sind es 23 (ausgezählt). S. 320 schreibt Abb. 6a die Überverwendung von Sense 1 bei *help* zu, die Bildunterschrift ordnet 6a *add* zu. S. 321 sagt, der frühere Sense 4 von *date* sei in WordNet 3.0 nicht mehr vorhanden; gemeint ist im Zusammenhang wohl 3.1.

## Wörtliche Stellen

> „We argue that high chance-adjusted interannotator agreement is neither necessary nor sufficient to ensure high quality gold-standard labels.“ (S. 311)

> „In agreement-based analyses, two wrongs make a right in the sense that if two annotators both make the same mistake, they agree.“ (S. 313)

> „In such cases, no one individual can reliably assign labels because the ground truth derives from consensus among the community of language users. Word sense annotation is such a task.“ (S. 323)

## Bezug zur Dissertation

**1. PROTOKOLL §9.2 („Hohe Roh-IAA sagt nichts über die Qualität des adjudizierten Golds (Passonneau & Carpenter 2014)“): im Kern gedeckt, aber zu stark und ungenau formuliert.** Die Arbeit sagt über **zufallskorrigierte** Übereinstimmung, sie sei für gute Goldlabels weder notwendig noch hinreichend (S. 311), und nennt Übereinstimmungsmaße „at best an indirect measure“ der Sicherheit (S. 312). Für Rohübereinstimmung gilt das Argument „two wrongs make a right“ (S. 313) ebenso. Über adjudiziertes Gold spricht die Arbeit nicht; ihr Gegenbild ist ein Gold, das nach der Übereinstimmungsmessung von je einer Person annotiert wird (S. 312). **Vorschlag:** „Hohe Übereinstimmung ist für die Qualität der Goldlabels weder notwendig noch hinreichend und nur ein indirektes Maß (Passonneau & Carpenter 2014, S. 311 bis 313).“

**2. PROTOKOLL §7 (Ablauf) und §7 Schritt 4 (beide annotieren alle Items): gestützt.** Die Arbeit beschreibt den üblichen Zyklus aus Richtlinien, unabhängiger Doppelannotation einer Stichprobe, Messung und Iteration (S. 312) und kann neben Pustejovsky & Stubbs (in LITERATUR-IAA ○) als geprüfte Quelle dafür stehen. Ihr Einwand, die Übereinstimmungsstichprobe sei oft nicht repräsentativ, trifft das Protokoll nicht, weil alle Items der Hauptstichprobe doppelt annotiert werden; er trifft aber den Pilot, wenn man dessen α als Qualitätsaussage liest (A32 sagt bereits: Die Schwelle entscheidet nur, wann das Nachschärfen endet).

**3. PROTOKOLL §9.1 Punkt 4 (Prävalenz, MFS- und Nicht-MFS-Tokens, AC1) und Punkt 5 (Bootstrap-Intervalle nach Text): gestützt.** Schwäche (3) und das Rechenbeispiel (S. 313) stützen den Prävalenzpunkt, Gwet 2008 wird als Alternative erwähnt (S. 313, 322 bis 323). Das Bootstrap-Verfahren und der Hinweis, dass nicht unabhängige Items breitere Intervalle verlangen (S. 314, Fn. 3), stützen den Cluster-Bootstrap. Schwäche (4) (gleichgerichtete Verzerrung zur häufigsten Kategorie, S. 313) begründet zusätzlich, warum die Übereinstimmung getrennt für MFS- und Nicht-MFS-Tokens berichtet wird.

**4. PROTOKOLL §9.2 (Gold, `MEHRERE`, Dice-Teilwertung; A14) und §6 (Sicherheit): ergänzt.** Die Arbeit schlägt vor, unsichere Goldlabels in der WSD-Evaluation geringer zu gewichten (S. 322, 324). Im Goldstandard gibt es keinen Posterior, aber die Sicherheitsangabe beider Personen und den Adjudikationsweg. **Vorschlag für Freeze 2:** eine Sekundärauswertung der LLM- und MFS-Genauigkeit nur auf Items, die beide Personen als „sicher“ markiert und gleich gelabelt haben.

**5. Probabilistisches Modell gegenüber Adjudikation: nicht übertragbar, aber als Einwand zu nennen.** Mit zwei Annotator:innen lässt sich das Dawid-Skene-Modell nicht sinnvoll schätzen; die Arbeit nutzt 20 bis 25 Labels pro Item (S. 319) und sagt nur allgemein, das Modell brauche nicht so viele (S. 311). Für die Dissertation bleibt Adjudikation der Weg; der Artikel sollte aber sagen, dass das Gold damit **kein** Sicherheitsmaß pro Item hat, und dafür die Sicherheitsangaben und Ursachencodes anführen.

**6. A31, Weg A (Gold relativ zum Inventar) und Ausweichlabels als Ergebnis (§9.2): gestützt.** Die Arbeit führt Abweichungen teils auf das Inventar zurück (später entfernte WordNet-Senses, S. 321) und hält eine Überarbeitung des Inventars für den Weg zu sichereren Labels (S. 322). Das passt zu `KEINE_PASST` als Befund über das Begriffssystem. Ihre Begründung für Mehrfachannotation, die Ground Truth von Wortbedeutungen beruhe auf dem Konsens der Sprachgemeinschaft (S. 323), lässt sich auf Mittelhochdeutsch nicht übertragen, weil es keine Sprecher:innen gibt; das ist ein Argument dafür, das Gold ausdrücklich als relativ zu Inventar, Richtlinien und Expert:innen zu beschreiben (eigene Folgerung).

**7. A32 (Schwelle α ≥ 0,80) und §9.1: Einordnung.** Selbst geschulte Studierende im MASC-Projekt erreichten auf WordNet-Senses bei 23 von 45 Wörtern α < 0,50, nur zwei erreichten 0,80 (Abb. 3, S. 317). Das α dort ist pro Wort gerechnet, nicht über Lemmata gepoolt wie im Protokoll; vergleichbar ist es nur mit diesem Vorbehalt (wie bei Passonneau et al. 2010).

**8. LITERATUR-IAA.md, Zeile „Hohe Roh-IAA belegt nicht die Qualität des adjudizierten Golds“ (Passonneau & Carpenter 2014 ○):** Der Volltext ist jetzt gelesen; die Aussage ist mit den Präzisierungen aus Punkt 1 haltbar („zufallskorrigiert“ statt „Roh-“, „Goldlabels“ statt „adjudiziertes Gold“).

## Grenzen und Einwände

- Gegenstand ist Crowd-Annotation mit vielen Labels pro Item; der Vergleich mit den Geschulten ist ungleich (verschiedene Oberfläche, nicht identische Satzmengen, bei 90 % der MASC-Sätze nur ein Label; S. 318, 321).
- Die Überlegenheit der Modell-Labels wird über Transinformation und Übereinstimmungsanteile begründet, nicht gegen ein unabhängiges Expert:innengold (S. 321).
- Itemschwierigkeit ist nicht modelliert (S. 316); die Sicherheitswerte dürften daher zu optimistisch sein, was die Autor:innen andeuten.
- Mehrere Unstimmigkeiten zwischen Text und Abbildungen (siehe oben).
- Für historische Sprachen, bei denen es keine Crowd mit Sprachkompetenz gibt, ist der Ansatz praktisch nicht verfügbar.
- Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar: nicht berührt; die Kritik an Übereinstimmungsmaßen gilt unabhängig vom Inventar.

## Weiterführend

- Dawid & Skene 1979, *Journal of the Royal Statistical Society, Series C* 28(1), S. 20 bis 28 (S. 311, 314).
- Passonneau, Baker, Fellbaum & Ide 2012a, The MASC word sense corpus, LREC 2012, S. 3025 bis 3030 (S. 311, 317).
- Passonneau, Bhardwaj, Salleb-Aouissi & Ide 2012b, Multiplicity and word sense, *Language Resources and Evaluation* 46(2), S. 219 bis 252 (S. 317): Mehrfachlabels in MASC.
- Bruce & Wiebe 1998, Word-sense distinguishability and inter-coder agreement, EMNLP (S. 312): früheste WSD-Anwendung des Modells laut S. 323 (dort allerdings als Bruce & Wiebe 1999 zitiert, dessen Titel im Literaturverzeichnis „Recognizing subjectivity“ lautet).
- Snow, O'Connor, Jurafsky & Ng 2008, Cheap and fast, but is it good?, EMNLP (S. 321, 323).
- Hovy, Berg-Kirkpatrick, Vaswani & Hovy 2013, MACE, NAACL (S. 323).
- Feinstein & Cicchetti 1990 und Gwet 2008 (S. 313, 322 bis 323): beide schon in `goldstandard/LITERATUR-IAA.md` (○).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF.
