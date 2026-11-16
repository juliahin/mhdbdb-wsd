# Passonneau, Salleb-Aoussi, Bhardwaj & Ide 2010: Word Sense Annotation of Polysemous Words by Multiple Annotators

**Datei:** `pdf/Passonneau-etal-2010-WS-Annotation-Multiple.pdf` (nur lokal; 6 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Tab. 1 und 2 (S. 3245) am Seitenbild geprüft; die Assoziationsregeln (Tab. 3 bis 5) nur an der Textebene, dort teils verstümmelt (S. 3247, Tab. 4 „land“). Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology L10-1628 (SHA-256 verglichen am 2026-11-13); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 3243 + n (PDF 1 = S. 3244, PDF 6 = S. 3249; Seitenzahlen in der Fußzeile). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Passonneau, Rebecca J., Ansaf Salleb-Aoussi, Vikas Bhardwaj & Nancy Ide (2010). Word Sense Annotation of Polysemous Words by Multiple Annotators. In: Nicoletta Calzolari, Khalid Choukri, Bente Maegaard, Joseph Mariani, Jan Odijk, Stelios Piperidis, Mike Rosner & Daniel Tapias (Hg.), *Proceedings of the Seventh International Conference on Language Resources and Evaluation (LREC’10)*. Valletta: European Language Resources Association (ELRA), S. 3244 bis 3249.
- **DOI/URL:** keine DOI; https://aclanthology.org/L10-1628/ (Herausgeber:innen, Ort, Verlag, Monat Mai nach dem BibTeX der Anthology, abgerufen 2026-11-13). Seiten nur nach den Fußzeilen des PDF; die Anthology nennt keine.
- **Lizenz:** nicht festgestellt (FAQ der ACL Anthology regelt nur ACL-Material, nicht LREC/ELRA; abgerufen 2026-11-13).
- **Art:** Konferenzbeitrag
- **Sprache:** Englisch

## Worum es geht

Im MASC-Projekt annotierten fünf bis sechs gleich geschulte Studierende je 100 Sätze zu zehn mäßig polysemen englischen Wörtern (drei Adjektive, drei Nomen, vier Verben) mit genau einem WordNet-Sense (S. 3244 bis 3245). Krippendorffs α, für jedes Wort getrennt gerechnet, reicht von 0,37 bis 0,68 (Tab. 1, S. 3245). Die Unterschiede hängen kaum an der Zahl der Senses; die Autoren führen sie auf Wortbedeutung, Kontexte und individuelle Unterschiede der Annotator:innen zurück (S. 3245, 3248). Ein Maß für die Ähnlichkeit der Senses korreliert teilweise mit der Übereinstimmung, Assoziationsregeln zeigen Ausreißer und systematische Abweichungen einzelner Paare (S. 3245 bis 3248).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Wortbedeutung ist fließend und teils generativ; Variation zwischen Annotator:innen ist als Folge der Variation im Gebrauch zu erwarten. | S. 3244, Abschnitt 1 | Position der Autoren (nach Pustejovsky 1991, Nunberg 1979) |
| Als Einflussfaktoren auf menschliche WSD sind in der Literatur u. a. Mehrfachlabels, Zahl und Granularität der Senses (Ng et al. 1999), Zusammenlegen ähnlicher Senses, Sense-Ähnlichkeit und Entropie vorgeschlagen. | S. 3244, Abschnitt 2 | referiert |
| Daten: zehn Wörter, je 1.000 Vorkommen aus dem Open American National Corpus (OANC), davon in dieser Phase je 100 weitere Sätze von fünf oder sechs Annotator:innen; in dieser Phase musste genau ein WordNet-Sense gewählt werden, in späteren Phasen sind Mehrfachwahlen erlaubt. | S. 3244 bis 3245, Abschnitt 3 | eigene Datenerhebung |
| Maß: Krippendorffs α, 0 für zufallsgemäße, 1 für perfekte Übereinstimmung. Fünf und sechs Annotator:innen sind vergleichbar (α mit sechs gegen Mittel aller Fünfergruppen, t = 0,0024, p = 0,9982); das spreche für gleich gute Schulung, anders als im IAMTC-Projekt. | S. 3245, Abschnitt 4 | eigenes Ergebnis, Maß referiert (Krippendorff 1980) |
| α pro Wort von 0,68 (*time*) bis 0,37 (*know*, *say*); Adjektive und Nomen 0,49 bis 0,68, Verben deutlich niedriger. | S. 3245, Tab. 1 | eigenes Ergebnis |
| Die Zahl der Senses im Inventar korreliert nicht mit der Übereinstimmung (ρ = −0,38), die Zahl der tatsächlich benutzten Senses nur schwach negativ (ρ = −0,56); Übereinstimmung war teils hoch bei Wörtern mit vielen Senses. | S. 3244 Abstract, S. 3245 | eigenes Ergebnis |
| Folgerung: Die Unterschiede liegen an Bedeutung, Gebrauchskontexten und individuellen, soziolinguistischen und idiolektalen Unterschieden, „rather than deficiencies in annotation performance“. | S. 3245; S. 3248 | Deutung der Autoren |
| Inter-Sense-Ähnlichkeit (ISM, Variante des Lesk-Maßes) und Verwechslungsschwelle CT_w = Mittelwert + Standardabweichung der ISM eines Worts: Bei Nomen korreliert die Übereinstimmung mit dem Anteil über CT (ρ = 0,73; nur benutzte Senses 0,96, aber nur drei Datenpunkte), insgesamt für benutzte Senses 0,59; bei Verben und Adjektiven nicht. | S. 3245, Tab. 2 | eigenes Ergebnis, von den Autoren als vorläufig eingeschätzt |
| Assoziationsregeln über Paare „Annotator.Sense“ zeigen bei gleichem α verschiedene Muster: Bei *long* zeigen sie einen Ausreißer, Annotator 108 vergibt oft ein Kollokationslabel; ohne 108 steigt α auf 0,80. Bei *quiet*, *fair*, *work* und *land* zeigen sie systematische Gegensätze bestimmter Paare. | S. 3246 bis 3247, Tab. 3 und 4 | eigenes Ergebnis |
| Bei Verben stimmt die beobachtete Häufigkeit nicht mit der WordNet-Reihenfolge überein, und der Anteil an Regeln für Nichtübereinstimmung ist höher. | S. 3248, Abschnitt 6.3 | eigenes Ergebnis |

## Daten, Methode, Zahlen

**Tab. 1 (S. 3245, am Seitenbild geprüft):**

| Wort | Senses | benutzt | Annotator:innen | α |
|---|---|---|---|---|
| long (Adj.) | 9 | 4 | 6 | 0,67 |
| fair (Adj.) | 10 | 6 | 5 | 0,54 |
| quiet (Adj.) | 6 | 5 | 6 | 0,49 |
| time (Nomen) | 10 | 8 | 5 | 0,68 |
| work (Nomen) | 7 | 7 | 5 | 0,62 |
| land (Nomen) | 11 | 9 | 6 | 0,49 |
| show (Verb) | 12 | 10 | 5 | 0,46 |
| tell (Verb) | 8 | 8 | 6 | 0,46 |
| know (Verb) | 11 | 10 | 5 | 0,37 |
| say (Verb) | 11 | 10 | 6 | 0,37 |

- α ist **pro Wort** gerechnet, also mit einer Zufallsschätzung aus den Sense-Anteilen dieses Worts über 100 Sätze.
- Annotator:innen: sechs Studierende (Vassar College, Columbia University), vier davon schon in der Pilotphase (Passonneau et al. 2009) (S. 3245).
- Die Sätze stammen zu gleichen Teilen aus den Gattungsteilen der OANC (S. 3245, Anm. 2).
- **Unstimmigkeiten im Werk:** S. 3245 nennt für ISM einen Bereich von 0 bis 1,44, Tab. 2 zeigt aber 1,88 als Maximum (*time*); die Spalte „% > CT“ wird als Anteil der Senses beschrieben, gemeint sind offenbar Sense-Paare. Rohübereinstimmung wird nicht berichtet.

## Wörtliche Stellen

> „This variation in IA does not correlate with number of senses in the inventory, or the number of senses actually selected by annotators. In fact, IA was sometimes quite high for words with many senses.“ (S. 3244)

> „[…] variation in word sense annotation across annotators should be expected as a consequence of usage variation.“ (S. 3244)

## Bezug zur Dissertation

**1. PROTOKOLL §9.1 Punkt 3 (Zufallsmodell pro Lemma).** Wie Ng et al. (1999) rechnen die Autoren die Übereinstimmung pro Wort (S. 3245, Tab. 1); das ist die übliche Praxis bei Lexical-Sample-Daten mit vielen Sätzen pro Wort. Für die Dissertation mit meist einem Token pro Lemma ist das nicht direkt übertragbar, zeigt aber den Vergleichsmaßstab: WSD-α pro Wort mit fünf bis sechs geschulten Personen lagen hier bei 0,37 bis 0,68, also durchweg unter 0,67 außer *long* und *time*.

**2. A32 (Schwelle 0,80, α nahe an der Rohübereinstimmung).** Nicht behandelt; die Rohübereinstimmung fehlt. Für die Einordnung der Schwelle ist der Kontrast wichtig: Ein gepooltes α über viele Lemmata (A32) und ein α pro Wort wie hier messen Verschiedenes. Wer das Ergebnis der Dissertation mit diesen Werten vergleicht, muss das Zufallsmodell angeben.

**3. PROTOKOLL §4.3 und §9.1 Punkt 6 (Polysemie als Schichtungs- und Auswertungsmerkmal).** Einwand: Die Zahl der Senses sagt die Übereinstimmung hier kaum voraus (ρ = −0,38; benutzte Senses −0,56; S. 3245). Bei nur zehn Wörtern ist das schwach belegt, spricht aber dafür, Polysemie als Erklärungsfaktor nicht vorauszusetzen. Das Lemma-Panel (§4.5), das Lemma- von Kontextschwierigkeit trennt, passt zu dem Befund, dass die Übereinstimmung von Wort zu Wort stark schwankt.

**4. PROTOKOLL §9.1 Punkt 6 (Wortart).** Gestützt: Verben am niedrigsten (Tab. 1), wie bei Passonneau, Habash & Rambow 2006 (S. 1954).

**5. PROTOKOLL §7 Schritt 6 (Ursachencodes) und §9.1 (Konfusionstabelle).** Die Autoren werten Abweichungen nicht nur als Fehler, sondern als systematische Lesartunterschiede einzelner Personen (S. 3245, 3247). Das stützt die Ursachencodes „echte Textambiguität“ neben „Versehen“ und das Aufbewahren der Labels vor der Adjudikation (§7 Punkt 7). Bei zwei Annotator:innen leistet die Konfusionstabelle pro Lemma, was hier die Assoziationsregeln leisten. Der Fall *long* (ein Ausreißer mit eigenem Kollokationslabel, α ohne ihn 0,80; S. 3247) zeigt, wie stark eine einzige abweichende Regelauslegung den Wert drückt; das spricht dafür, im Pilot nach jeder Runde die Abweichungen nach Muster zu ordnen, nicht nur α zu rechnen.

**6. PROTOKOLL §6 (`MEHRERE`).** In der berichteten Phase war genau ein Sense Pflicht, Mehrfachwahl erst in späteren Phasen vorgesehen (S. 3245). Werte für Mengenlabels liefert das Werk also nicht.

**7. LITERATUR-IAA.md:** Das Werk ist dort nicht zitiert; kein Abgleich nötig.

## Grenzen und Einwände

- Nur zehn Wörter; Korrelationen über zehn (bei Nomen drei) Datenpunkte sind kaum belastbar, was die Autoren für die Nomen selbst sagen (S. 3245).
- Keine Rohübereinstimmung, keine Konfidenzintervalle.
- Die Annotator:innen waren Studierende, keine Lexikograph:innen; ihre Schulung ist nur als gleich beschrieben, nicht im Einzelnen.
- ISM hängt an der WordNet-Struktur (Relationen, Glossen) und ist nach den Autoren selbst je Wortart und Version verschieden (S. 3248); für ein Inventar aus Begriffsgruppen müsste eine Ähnlichkeit anders definiert werden, etwa als Überschneidung der Begriffe.
- Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar: nicht berührt.

## Weiterführend

- Passonneau, Salleb-Aouissi & Ide 2009 (im Literaturverzeichnis „Salleb-Ansaf Aouissi“), Making sense of word sense variation, SEW-2009, S. 2 bis 9 (S. 3244, 3249): Pilotphase mit sechs Annotator:innen.
- Passonneau 2008, Formal and functional assessment of the pyramid method, *Natural Language Engineering* (S. 3245): Begründung des Einsatzes von α.
- Palmer, Dang & Fellbaum 2005/2007, Making fine-grained and coarse-grained sense distinctions, *Natural Language Engineering* (S. 3244; im Literaturverzeichnis als 2005, 13.2:137-163).
- Ide 2006, Making senses (S. 3245): Inter-Sense-Ähnlichkeit.
- Snow, Jurafsky & Ng 2007, Learning to merge word senses, EMNLP-CoNLL (S. 3244).
- Chugur, Gonzalo & Verdejo 2002, Polysemy and sense proximity in the Senseval-2 test suite (S. 3244).
- Diab 2004, ACL (S. 3244): Sense-Perplexität und Entropie.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
