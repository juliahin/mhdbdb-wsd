# Entscheidungsliste: Vorschläge aus den Literaturzusammenfassungen

**Datum:** 2026-10-30
**Grundlage:** die Abschnitte „Bezug zur Dissertation“ der Zusammenfassungen vom 28./29.10.2026 in `literatur/zusammenfassungen/` und die Abschlussberichte der fünf Läufe der Welle 1 (nicht archiviert, nur in der Sitzung vom 2026-10-29). Abgeglichen mit `goldstandard/PROTOKOLL.md` (Stand 2026-10-28, A1 bis A14, §12), `LITERATUR-STICHPROBE.md`, `LITERATUR-IAA.md`, `PROMPT-LOG.md`, `DMP.md` und `knowledge/data.md`, alle auf Commit `973c001a7`.

**Entscheidungsstand:** Jede Zeile ist ein Vorschlag, über den Julia entscheidet. Entschieden bisher (2026-10-30): V5, V9, V10 und V25 übernommen, eingetragen als A15 bis A18 in `PROTOKOLL.md`. Alle übrigen sind offen.

**Frage F1 (Homographen)** ist inzwischen gemessen: `knowledge/data.md`, B15. Die Vermutung bei V2, die MHDBDB führe Homographen meist als Senses eines Lemmas, ist dort als Regel nicht gestützt.

**Zum Umfang:** `bezug.md` enthält 42 Abschnitte, nicht 43. Die zwölf Zusammenfassungen der Priorität 1 (Henrich 2015, Navigli 2009, Klein & Dipper 2016, Schmidt 1985, Hinkelmanns 2019, Hinkelmanns & Zeppezauer-Wachauer 2023, Zeppezauer-Wachauer 2022, Tittel et al. 2020, Bhat & Varma 2023, Galka & Vogeler 2026, Li et al. 2023, Pangakis et al. 2023) sind dort nicht enthalten und hier nicht ausgewertet; aus diesem Lauf stammen A13 und A14. Wo eine dieser Dateien eine Frage unten direkt berührt, steht ein Hinweis.

**Prüfstatus:** Seitenangaben und Zahlen stammen aus den Zusammenfassungen. Diese sind KI-Zusammenfassungen und nicht gegengelesen; keine Seitenangabe hier ist am Original geprüft. Geprüft habe ich nur, ob die Abschnittsnummern im aktuellen Protokoll zum genannten Inhalt passen (Ergebnis bei den Vorschlägen und in Abschnitt E), und eine Zählung in `lexicon.xml` (Frage F1).

**Gewicht:** hoch = berührt Stichprobe, Bewertungsregeln oder Freeze 1; mittel = Begründung, Richtlinie oder Formulierung im Protokoll; niedrig = Literaturverweis oder Text für den Artikel.

---

## Vorschläge mit Gewicht „hoch“

- **V5** (übernommen, A15) Ausschluss 4 (disjunkte Token-`@pos`) prüfen: Wortartwechsel an einem Lemma können gewollt sein; der Ausschluss trifft dann echte Ziellemmata (Grundgesamtheit, Freeze 1).
- **V9** (übernommen, A16) Vorab festlegen, was bei mehreren LLM-Läufen pro Item als Vorhersage zählt (ein bestimmter Lauf, Mehrheit, Verteilung), und die Streuung zwischen Läufen berichten.
- **V10** (übernommen, A17) Prompt, Antwortformat, Few-shot-Beispiele und jede Konfigurationsvariante nur am Pilot-Pool auswählen, nie an Haupt- oder Panelstichprobe.
- **V25** (übernommen, A18) Bewertungsregel für ungültige LLM-Antworten (unparsbar, Sense-ID außerhalb des Menüs, mehrere IDs bei `SENSE`): getrennt zählen, im primären gepaarten Vergleich als falsch werten.

---

## A. PROTOKOLL.md, nach Abschnitt

### §1 Forschungsfrage

**V1** Ausdrücklich entscheiden und im Protokoll festhalten, ob ein Encoder-Vergleich (z. B. GHisBERT-Einbettungen oder ein feinabgestimmtes Modell) über die Forschungsfrage hinaus vorgesehen ist; falls ja, dessen Konfiguration wie die LLM-Konfiguration in Freeze 2 festschreiben.
- Begründung: Mehrere Zusammenfassungen nennen ihn als mögliche Baseline; die Werke zeigen zugleich, dass Konfiguration, Seeds und Daten das Ergebnis tragen und dass für Mhd. kaum Trainingsdaten vorliegen (nur ReM mit 2,3 Mio. Wörtern, Silber unbekannter Qualität).
- Quellen: Beck & Köllner 2023, S. 36, 38, 41, Tab. 1; Devlin et al. 2019, S. 4176, 4183 bis 4184; Liu et al. 2019, S. 4, 7 bis 8; Manjavacas & Fonteyn 2022a, S. 4, 15; Manjavacas & Fonteyn 2022b, S. 124 bis 128; Iacobacci et al. 2016, S. 898.
- Status: neu (§1 nennt nur LLM gegen MFS; keine Entscheidung zu Encodern).
- Gewicht: niedrig (außerhalb der Forschungsfrage, solange nicht beschlossen).

### §2 Begriffe

**V2** In §2 (Begriffstabelle) oder §4.3 einen Satz ergänzen, dass „Polysemie“ hier die Zahl der Senses im Inventar meint, ohne Homonymie und Polysemie zu unterscheiden; dafür Kortmann 2020 selbst zitieren, nicht Köhnlein.
- Begründung: Die Literatur trennt Homonymie (verschiedene Lexeme) von Polysemie; ob die MHDBDB Homographen als eigene Lemmata oder als Senses eines Lemmas führt, entscheidet, was die Polysemiestufen 2 / 3 / 4+ messen (siehe Frage F1, die erste Zählung spricht für das Zweite).
- Quellen: Köhnlein 2025, S. 33 bis 35 (PDF 34 bis 36); Telljohann et al. 2017, S. 34 (PDF 35); Ganslmayer & Schwarz 2021 (Beitrag Dipper), S. 165, Anm. 12.
- Status: neu. **Verweis korrigiert:** Die Zusammenfassung nennt „Protokoll 2 und 4.3“; definiert ist „Polysemie“ nur in §4.3, §2 enthält keinen Eintrag dazu.
- Gewicht: mittel.

**V3** Im Datasheet (oder in der Begriffstabelle §2) klarstellen, dass „Silber“ hier eine menschliche, undokumentierte Annotation meint und nicht „automatisch annotiert“ wie in der NER- und Entity-Linking-Literatur; zugleich festhalten, dass monosemes Silber automatisch vergeben ist (B2).
- Begründung: Leser:innen aus NER/EL verbinden „Silber“ mit automatischer Annotation; das Protokoll verwendet den Begriff anders, sachlich begründet.
- Quellen: Matusch 2025, S. 33 (Definition dort ohne Quelle, daher nicht als Beleg zitieren); Vergleichsfälle Henrich et al. 2012 (WebCAGe), S. 390 bis 394; Tittel & Chiarcos 2018, S. 62.
- Status: neu.
- Gewicht: mittel.

### §3 Grundgesamtheit und Ausschlüsse

**V4** Den Satz „Präpositionen und Adverbien … fehlen auch in den Vergleichsdatensätzen“ auf Präpositionen beschränken oder die gemeinten Datensätze nennen.
- Begründung: Im englischen Standardrahmen sind Adverbien enthalten (Senseval-2; 346 Adverb-Instanzen in der Verkettung), Präpositionen nicht. Für den Ausschluss der Präpositionen gibt es zusätzliche Stützen.
- Quellen: Raganato et al. 2017, S. 101, Tab. 3 (S. 105), Tab. 4; Stützen: Manjavacas & Fonteyn 2022a, S. 9 (Inhalts- gegen Funktionswörter; zu Adverbien nichts); Miller 1995, S. 40.
- Status: neu; die Ausschlussentscheidung vom 2026-10-16 bleibt unberührt, nur die Begründung ist sachlich falsch.
- Gewicht: mittel.

**V5** Ausschluss 4 (Lemmata mit disjunkten Token-`@pos`-Werten) überprüfen: Begründung ergänzen, dass Wortartwechsel gewollt sein können (substantivierte Infinitive, substantivierte Adjektive), und vor Freeze 1 an einer Stichprobe der betroffenen Lemmata prüfen, wie viele echte Lemmatisierungsfehler sind.
- Begründung: ReM führt nominalisierte Infinitive als `NA` mit Lemma-Wortart `VVINF`, HiTS behandelt Abweichung zwischen Lemma- und Beleg-Wortart als Information (ADJ > AVD, VVINF > NA). Der Ausschluss ist im Protokoll schon als „Verdacht“ formuliert, wirkt aber als harter Ausschluss (763 Lemmata in den 190 Texten). Die Folgerung, dass der Ausschluss echte Ziellemmata trifft, ist meine, nicht die der Zusammenfassungen.
- Quellen: Ganslmayer & Schwarz 2021 (Beitrag Dipper), S. 164; Dipper et al. 2013, S. 92 bis 95, 105, 128.
- Status: neu; berührt offenen Punkt 13 (Ausschlüsse 2 bis 4 umrechnen), der ohnehin vor Freeze 1 ansteht.
- Gewicht: **hoch** (Grundgesamtheit, Freeze 1).

**V6** In der Begründung der Wortartregel (§3) festhalten, dass die Schichtungsvariable „Wortart“ zwei Ebenen mischt (Lemma-Wortart aus Schritt 1, Beleg-Wortart aus Schritt 2) und dass die Beleg-Wortart bei Lemmata wie *guot* von der Bedeutung abhängen kann; erwägen, die Hauptauswertung nach Herkunft der Wortart aufzuschlüsseln.
- Begründung: HiTS und STTS entscheiden einige Wortartgrenzen ausdrücklich über die Semantik; HiTS nennt *guot* mit ‘Besitz’ als Kennzeichen der substantivischen Lesart. Dann ist die Token-Wortart kein von der Bedeutung unabhängiges Merkmal, vor allem bei Paaren aus Schritt 2.
- Quellen: Dipper et al. 2013, S. 92 bis 95, 105, 107, 128; Schiller et al. 1999, S. 12, 24, 57; Ide & Véronis 1998, S. 3 bis 4, 25 (Stütze für Lemma × Wortart).
- Status: teilweise umgesetzt: Das Manifest führt die Herkunft der Wortart mit (§4.9). Neu sind der Satz in §3 und die Aufschlüsselung.
- Gewicht: mittel.

### §4.4 Ziehung

**V7** In §4.4, Punkt 4 „All-Words-Sets als Klumpenstichproben, Raganato et al. 2017“ als eigene Deutung kennzeichnen; gleiche Korrektur in `LITERATUR-STICHPROBE.md`, Zeile „All-Words-Sets …“: Raganato nur für die Dokumentzahlen und die Streuung der MFS zwischen Datensätzen anführen, „MFS hängt vom Dokument ab“ am zweiten Beleg (Navigli et al. 2007) prüfen oder streichen, Prüfstatus für diesen Teil ○ statt ✔. Optional als deutscher Beleg für den Klumpeneffekt WebCAGe ergänzen.
- Begründung: Raganato et al. nennen 3 / 3 / 3 / 13 / 4 Dokumente, sprechen aber nirgends von Klumpenstichproben oder dokumentabhängiger MFS; belegt ist nur die Streuung der MFS je Datensatz (54,5 bis 67,1). WebCAGe misst „one sense per discourse“ mit 95,62 bis 99,96 % (Prüfweg nicht beschrieben).
- Quellen: Raganato et al. 2017, Tab. 1 (S. 102), S. 101 bis 105, Tab. 2 (S. 105); Henrich et al. 2012, S. 390 (PDF 4); Welle-1-Bericht Raganato/Bevilacqua, Abschnitt 2 und 4.
- Status: neu. A13 hat in demselben Punkt nur die ReM-Begründung korrigiert; der Raganato-Teil steht noch unverändert.
- Gewicht: mittel.

### §4.10 Freeze 2 (LLM-Konfiguration)

**V8** Die Liste für Freeze 2 erweitern um: Zugang über API mit exakter Snapshot-ID (keine Weboberfläche), Abfragedatum, maximale Antwortlänge, alle Sampling-Parameter ausdrücklich gesetzt (Temperatur, top_p, top_k) statt Standardwerten, Kartenformat und Kontextumfang für das LLM, im Modellkarten-Text erklärter Sprachumfang; im Artikel diese Angaben im Text nennen, nicht nur in Abbildungen.
- Begründung: Die Werke zeigen, was fehlt, wenn diese Angaben fehlen (Standardtemperatur, kein Datum, ein Lauf, Längendeckel nicht berichtet), und dass die Weboberfläche Modelle wechselt, System-Prompts verbirgt und keine identischen Ausgaben liefert.
- Quellen: Scholger & Bleier 2026, Abs. 2, 5 bis 7, 40; Yae et al. 2025, PDF-S. 6 bis 7, 14; Basile et al. 2025, S. 5; Meconi et al. 2025, S. 33909; Campesato 2024, S. 168 bis 170, 218; Köhnlein 2025, S. 12, 49, 67, 87 (PDF 13, 50, 68, 88); Strutz 2026, S. 10, 17; Matusch 2025, Tab. 4.6; Jannidis et al. 2025, S. 4, 8, 19 Fn. 20; Steller 2024, S. 4; Gengnagel et al. 2024, S. 4.
- Status: teilweise umgesetzt: `PROMPT-LOG.md` Ebene A protokolliert `modell` (Snapshot), `parameter` (Temperatur, max. Tokens, Seed, alle weiteren) und `zeitpunkt`. Neu ist, diese Werte in §4.10 als Freeze-Gegenstand zu nennen und API-Zugang, Kartenformat und Modellkarte aufzunehmen.
- Gewicht: mittel.

**V9** Vor Freeze 2 festlegen, was bei mehreren Läufen pro Item als Vorhersage des LLM gilt (ein vorab bestimmter Lauf, Mehrheit mit Regel für Gleichstand, oder Verteilung), und die Übereinstimmung zwischen Läufen als eigenes Ergebnis berichten (Mittelwert und Streuung, nicht nur einen Wert).
- Begründung: Mehrfachabfrage mit Mehrheitsentscheid ist selbst ein Ensemble-Verfahren; ohne Festlegung vergleicht der McNemar-Test ein Ensemble mit einer Einzelbaseline. Vorlagen gehen auseinander: mindestens fünf Läufe bei Temperatur 0,7 mit Konsistenz als Konfidenz (Pangakis & Wolken) gegen greedy decoding mit einem Lauf (Basile et al.); „deterministisch bei Temperatur 0“ ist keine Zusage.
- Quellen: Chen et al. 2025, S. 5 bis 6; Campesato 2024, S. 129, 145 bis 146, 188, 218; Semmelrock et al. 2025, S. 4, 8, 10, Tab. 1 (S. 14); Pangakis & Wolken 2025, S. 1474 Fn. 12, S. 1475 bis 1477; Basile et al. 2025, S. 5; Scholger & Bleier 2026, Abs. 5, 18; Strutz 2026, S. 18; Köhnlein 2025, S. 71, 87 (PDF 72, 88); Rekabsaz 2018, S. 42 bis 45 (nur Analogie); Liu et al. 2019, S. 4, 7; Welle-1-Bericht An/Chen/Yang, Abschnitt 3.
- Status: teilweise umgesetzt: `PROMPT-LOG.md` sagt, welcher Lauf eingeht, „wird vorab im Protokoll festgelegt“; im Protokoll steht das noch nicht, §4.10 nennt nur die „Anzahl der Läufe pro Item“. Aggregationsregel und Bericht der Streuung sind neu.
- Gewicht: **hoch** (bestimmt, was bewertet wird).

**V10** Im Protokoll festschreiben, dass Prompt-Wortlaut, Antwortformat, Few-shot-Beispiele (Anzahl und Herkunft) und jeder Formatvergleich nur am Pilot-Pool gewählt werden; Few-shot-Beispiele aus Silber dürfen keine Stichproben-Tokens enthalten; Wirkungen von Prompt-Überarbeitungen nur auf Items berichten, die beim Überarbeiten nicht gesehen wurden; das im Artikel ausdrücklich sagen.
- Begründung: Mehrere Werke wählen Prompt oder Konfiguration auf den Testdaten oder sagen nicht, ob die Auswahlitems in der Bewertung liegen, und berichten dann optimistische Werte. Prompt-Formulierungen streuen im Mittel um etwa 5 Punkte, die Präsentation der Optionen um über 30.
- Quellen: Meconi et al. 2025, S. 33900; Strutz 2026, S. 9 bis 10; Pangakis & Wolken 2025, Abb. 3, S. 1474 Fn. 8; Ristic 2025, Tab. 6.1 bis 6.7; Köhnlein 2025, Tab. 8, S. 79 (PDF 80); Manjavacas & Fonteyn 2022b, S. 127, 130; Campesato 2024, S. 134, 295.
- Status: neu. §4.2 nennt als Zweck des Pilot-Pools nur Pilotrunden der Menschen und die Schätzung diskordanter Paare.
- Gewicht: **hoch** (Trennung von Entwicklungs- und Testdaten).

**V11** In Freeze 2 festhalten, dass das LLM dieselbe pro Item gemischte Kartenreihenfolge sieht wie die Menschen und dass sie für das LLM ebenso protokolliert wird.
- Begründung: Gemischte Optionen senken die Werte (bei einem kleinen Modell F1 von 56,3 auf 40,4), position bias und majority label bias sind beschrieben; trifft die Verzerrung nur eine Seite, hängt der Vergleich an ihr.
- Quellen: Meconi et al. 2025, S. 33902, Tab. 5; Yang et al. 2024, S. 21; An et al. 2024, S. 2, 8 (nur lange Kontexte); Köhnlein 2025, Tab. 8, S. 79.
- Status: neu; §5, Punkt 5 regelt das Mischen nur für die Annotationsoberfläche, §4.10 führt „ob das LLM dieselben Karten sieht“ als offen.
- Gewicht: mittel.

**V12** Zusatzinformation auf Karte und im Kontext (Werktitel, KZW-Notizen an Senses, Nennung von Sprachstufe und Epoche im Prompt) für Mensch und LLM gleich und bewusst festlegen.
- Begründung: Modelle behandeln jede Information im Prompt als relevant; was auf der Karte steht, wirkt auf die Entscheidung.
- Quellen: Jannidis et al. 2025, S. 12, 15, 19; Gengnagel et al. 2024, S. 2 (Grounding).
- Status: offen in §12, Punkt 4 (Werktitel) und `knowledge/data.md` B13 (Notizen, „gleiche Karten für beide“); neu ist nur die Nennung von Sprachstufe und Epoche.
- Gewicht: mittel.

**V13** Am Pilot-Pool eine Kontrollbedingung ohne Kontext (nur Lemma und Karten) erwägen, um zu sehen, wie viel das LLM aus den Karten allein errät.
- Begründung: Bei den stärksten Modellen bringt der Kontextabsatz nichts, was auf Entscheidung aus Name und Beschreibung allein deutet (Deutung der Zusammenfassung, nicht der Arbeit).
- Quellen: Matusch 2025, Tab. 4.6.
- Status: neu (Vorschlag der Zusammenfassung, nicht aus der Quelle).
- Gewicht: niedrig.

**V14** Bei Wahl eines geschlossenen, kommerziellen Modells die eingeschränkte Reproduzierbarkeit als Limitation nennen und die Wahl im Artikel begründen (auch gegen ein quelloffenes Modell).
- Begründung: Ein über eine Anbieter-API genutztes Modell kann weder geteilt noch eingefroren werden; Trainingsdaten sind unbekannt (Kontamination, §10). Das Prompt-Log ersetzt die fehlende Reproduzierbarkeit nur teilweise.
- Quellen: Steller 2024, S. 4, 18; Klein et al. 2025, S. 9 bis 12; Semmelrock et al. 2025, S. 10; Scholger & Bleier 2026, Abs. 40.
- Status: neu (das Protokoll trifft noch keine Modellwahl).
- Gewicht: mittel.

**V15** Vor Freeze 2 klären, ob die mittelhochdeutschen Editionstexte an einen externen LLM-Dienst gegeben werden dürfen (pro Text bzw. Edition).
- Begründung: Leitlinie 2 des Positionspapiers betrifft urheberrechtlich geschützte Daten; die Kontexte stammen aus Editionen.
- Quellen: Steller 2024, S. 16 bis 17; Scholger & Bleier 2026, Abs. 35, 40.
- Status: teilweise: `DMP.md` §4 verweist für die Rechtegrundlage des Korpus auf `docs/RESEARCH.md` im Upstream und hält fest, dass nur Kontexte und Karten an Anbieter gehen; ob die Rechtegrundlage die Weitergabe an einen kommerziellen Dienst deckt, ist nicht geklärt. Siehe K4.
- Gewicht: mittel.

### §5 Darstellung des Inventars

**V16** Im Protokoll (oder Datasheet) offen benennen, dass Annotator:innen und LLM nur Begriffsnamen und Pfad sehen, keine Glossen wie bei WordNet-Annotation, und das als Einschränkung beim Vergleich mit englischen Werten angeben.
- Begründung: Die stärksten englischen Systeme nutzen Glossen; WordNet hat sie in den meisten Synsets, GermaNet nur optional. Die MHDBDB-Karten bieten weniger Information.
- Quellen: Miller 1995, S. 40; Bevilacqua et al. 2021, S. 4333, 4335; Henrich & Hinrichs 2010, S. 2228, Abb. 2; Tittel & Chiarcos 2018, S. 59, 64; Welle-1-Bericht Pangakis/Navigli/Iacobacci/Miller/Henrich, Abschnitt 3.
- Status: neu, aber **in Spannung mit `knowledge/data.md` B13**: Inzwischen gibt es 94 menschliche Notizen von KZW an Senses, ob sie gezeigt werden, ist für Freeze 2 offen. Der Satz müsste also lauten „keine Glossen außer …“ oder von dieser Entscheidung abhängen. Mehrere Zusammenfassungen stützen sich noch auf den alten Stand „fast keine Glossen“.
- Gewicht: mittel.

### §6 Annotationsaufgabe und Ausweichlabels

**V17** In der Begründung von `MEHRERE` (§6 oder Richtlinien v0) den Einwand von HiTS gegen das Markieren von Ambiguität nennen und beantworten (z. B.: `MEHRERE` wird mit α-MASI gemessen statt vorausgesetzt) und die Gegenposition der TüBa-D/Z (ausdrücklich unterspezifizierte Labels) daneben stellen; STTS als zweites Tagset, das eine Entscheidung erzwingt.
- Begründung: HiTS hält Ambiguitätsmarkierung für unzuverlässiger und aufwändiger; TüBa-D/Z annotiert unauflösbare Ambiguität als eigenes Label. Beide betreffen Wortarten bzw. Syntax, nicht Wortbedeutung, also als Analogie.
- Quellen: Dipper et al. 2013, S. 109 bis 110; Telljohann et al. 2004, S. 2229 (PDF 1); Telljohann et al. 2017, S. 18, 40 (PDF 19, 41); Schiller et al. 1999, S. 8; Stütze für Mehrfachlabels in WSD: Bevilacqua et al. 2021, S. 4330, 4333.
- Status: neu.
- Gewicht: mittel.

**V18** In den Richtlinien v0 unterscheiden, ob der Text zwischen zwei Lesarten schwankt (Ambiguität) oder ob die Stelle eine Unterscheidung gar nicht verlangt (Vagheit).
- Begründung: Genau diese Fälle fallen unter „mehrere Senses passen gleichermaßen“; auch nicht ambige Wörter sind kontextabhängig schattiert.
- Quellen: Köhnlein 2025, S. 35 (PDF 36).
- Status: teilweise angelegt: Der Ursachencode „echte Textambiguität“ in §7, Schritt 6 deckt die Adjudikation ab, nicht die Entscheidungsregel beim Annotieren.
- Gewicht: mittel.

**V19** In den Richtlinien v0 drei mittelhochdeutsche Fallgruppen behandeln: (a) regelhafte Polysemie abgeleiteter Nomina (-unge, -e, -heit) zwischen abstrakter Handlung und konkretem Ergebnis, Objekt, Ort, Träger, mit erwartbaren `MEHRERE`-Fällen; (b) Partikelverben in Distanzstellung (welches Lemma, welches Menü); (c) Segmentierungsfälle wie Genitivfügung oder Kompositum als Kandidaten für `LEMMA_FALSCH` oder `KONTEXT_UNZUREICHEND`.
- Begründung: Bei (a) entscheidet der Kontext zwischen den Lesarten, Grenzfälle sind zu erwarten (Beispiel *wîsheit*, B3); bei (b) und (c) hängen Lemma und damit Menü an einer Vorentscheidung.
- Quellen: Ganslmayer & Schwarz 2021 (Beitrag Pimenova), S. 229, 245; (Beitrag Dipper), S. 175, 177 bis 178.
- Status: neu; (b) setzt Frage F2 voraus.
- Gewicht: mittel.

**V20** Prüfen, ob sich eine Entscheidungsregel für unentscheidbare Fälle nach dem HiTS-Muster (ältere Lesart; Zusammenlegen wie bei *dehein*) auf Senses übertragen lässt.
- Begründung: HiTS bietet ein Muster; ob es für Senses taugt, ist eine Entscheidung für die Richtlinien, keine Aussage des Werks.
- Quellen: Dipper et al. 2013, S. 124.
- Status: neu.
- Gewicht: niedrig.

**V21** Als Rückfallplan festhalten: Wird `MEHRERE` im Pilot häufig, wären graduelle Urteile (Korrelation statt Kategorien) die Alternative.
- Begründung: Graduierte Urteile sind der Weg, den das Protokoll mit `MEHRERE` und Sicherheitsangabe bewusst nicht geht.
- Quellen: Navigli 2012, S. 118 (referiert Erk & McCarthy 2009).
- Status: neu.
- Gewicht: niedrig.

**V22** Für offenen Punkt 4 (Kontextausschnitt) die Anhaltspunkte aus der Literatur zusammenstellen, getrennt nach Mensch und System, und für Verse ohne Satzgrenzen eine eigene Regel festlegen.
- Begründung: Nur eine Zahl betrifft Menschen (Kaplan: zwei Wörter beiderseits so gut wie der Satz); die übrigen gelten für Systeme. Einzelne Werke halten einen Satz für zu wenig.
- Quellen: Ide & Véronis 1998, S. 4, 23, 25 bis 26; Iacobacci et al. 2016, S. 903; Miller 1995, S. 41; Köhnlein 2025, S. 59, 87 (PDF 60, 88); Ristic 2025, S. 51 (PDF 67).
- Status: offen in §12, Punkt 4; Vorschlag liefert nur Material, keinen Richtwert.
- Gewicht: mittel.

### §9.1 Übereinstimmung

**V23** Für offenen Punkt 12 (grobe Ebene) festhalten: die grobe Ebene nicht zu hoch ansetzen und die Wahl begründen; als Präzedenzfälle die Abbildung auf Taxonomie-Vorfahren und die Vergröberung über ein hierarchisches Wörterbuch zitieren; optional Fehler nach Abstand in der Hierarchie gewichten.
- Begründung: Obere Ebenen jeder Begriffshierarchie sind strittig und zu breit; bei gröberen Senses steigt All-Words von etwa 65 auf 82 bis 83 %.
- Quellen: Ide & Véronis 1998, S. 14, 31 bis 32; Bevilacqua et al. 2021, S. 4331, 4334 (Vial et al. 2019); Navigli 2012, S. 117 bis 118; Schiller et al. 1999, S. 62 (nur Analogie). Ergänzend aus Priorität 1, hier nicht ausgewertet: Schmidt 1985, S. 347 (Zahlencode als Abbild der Untergliederung).
- Status: offen in §12, Punkt 12; `knowledge/data.md` §4, Punkt 4 schlägt den Zahlencode vor.
- Gewicht: mittel.

### §9 Auswertung, Kontext

**V24** In §9 eine Aufschlüsselung „Kontext erweitert ja/nein“, getrennt nach Wortart, und eine getrennte Auswertung der Items mit `KONTEXT_UNZUREICHEND` vorsehen.
- Begründung: Erweiterter Kontext hilft nach älteren Befunden eher bei Nomen als bei Verben und Adjektiven (Hypothese); ob erweitert wurde, wird nach §8 schon protokolliert, aber nirgends ausgewertet.
- Quellen: Ide & Véronis 1998, S. 26; Rekabsaz 2018, S. 78 bis 79.
- Status: neu (die Protokollierung in §8 und §6 besteht schon).
- Gewicht: mittel.

### §9.2 Gold, Silber, LLM

**V25** In die Bewertungsregeln (§9.2) aufnehmen, was mit einer ungültigen LLM-Antwort geschieht (unparsbar, Sense-ID außerhalb des Menüs, ID eines anderen Lemmas, mehrere IDs bei `SENSE`): als eigene Kategorie zählen und berichten, im primären gepaarten Vergleich als falsch werten; die Antwort als Kartennummer oder Sense-ID verlangen und die Sense-ID direkt aus der Nummer ableiten, nicht über Textabgleich.
- Begründung: Ob eine ungültige Antwort als falsch, als Abstention oder als fehlend zählt, verändert die gepaarte Differenz zu MFS. Ein Ausschluss wie bei Strutz („INVALID“) bräche die Paarung, weil MFS nie ungültig antwortet (Folgerung der Zusammenfassung). Rückübersetzung über Textüberlappung ist bei kurzen, ähnlichen Begriffsnamen unsicher.
- Quellen: Strutz 2026, S. 4 bis 6, 16; Yae et al. 2025, PDF-S. 6 bis 7, 14; Basile et al. 2025, S. 7 bis 8; Meconi et al. 2025, S. 33899; Köhnlein 2025, S. 72 bis 75 (PDF 73 bis 76); Scholger & Bleier 2026, Abs. 28; Campesato 2024, S. 2; Welle-1-Bericht Yae/Basile/Meconi, Abschnitt 3.
- Status: neu; §9.2 regelt nur Abstinenz bei Ausweichlabels, `PROMPT-LOG.md` hat nur das Feld `label`.
- Gewicht: **hoch** (Bewertungsregel).

**V26** „Die menschliche IAA ist die Obergrenze“ umformulieren zu „Referenz- oder Vergleichswert“; ein LLM-Wert darüber wäre dann auslegungsbedürftig, kein Widerspruch.
- Begründung: Englische Systeme haben die menschliche Übereinstimmung erreicht oder überschritten, die Schätzung 67 bis 80 % gilt selbst als unsicher; Mensch und Modell irren bei verschiedenen Grenzfällen.
- Quellen: Bevilacqua et al. 2021, S. 4330, 4334, 4336; Meconi et al. 2025, S. 33903.
- Status: neu; ändert eine Formulierung des Entwurfs vom 2026-10-08, keinen datierten Beschluss.
- Gewicht: mittel.

**V27** Die LLM-Genauigkeit zusätzlich nach menschlicher Übereinstimmung pro Item aufschlüsseln (beide einig, uneinig, adjudiziert).
- Begründung: Aufgabenmerkmale wie kulturelles Wissen erklärten LLM-Leistung, Textmerkmale nicht; für Mhd. ist historisches Wissen der Normalfall.
- Quellen: Pangakis & Wolken 2025, S. 1475, Anhang E (Verweis auf die Zusammenfassung von Pangakis et al. 2023, Bezug 9.2, Priorität 1).
- Status: neu (§9.1, Punkt 6 schlüsselt nur die IAA nach Sicherheit auf, nicht die LLM-Genauigkeit nach IAA).
- Gewicht: mittel.

**V28** Für die LLM-Ausgaben eine Fehleranalyse mit vorab definierten Kategorien vorsehen, darunter „neuhochdeutsche Lesart eines mhd. Wortes“ (Anachronismus) und „Fehlschluss von der Wortbildungsbasis bei lexikalisierten Ableitungen“.
- Begründung: Mehrere Werke beschreiben die Neigung von Gegenwartsmodellen, historisches Material zu modernisieren oder unbekannte Wörter als Variante eines bekannten zu lesen; für WSD ist das eine Hypothese, die eine Fehleranalyse prüfen kann.
- Quellen: Strutz 2026, S. 2, 5; Manjavacas & Fonteyn 2022a, S. 3, 10, Abb. 5; Scholger & Bleier 2026, Abs. 26, 41; Yae et al. 2025, PDF-S. 8 bis 9; Ganslmayer & Schwarz 2021, Einleitung S. 2, Beitrag Dipper S. 183 bis 184.
- Status: neu. **Verweis korrigiert:** Strutz- und Manjavacas-Zusammenfassung verorten das bei den Ursachencodes der Adjudikation (§7, Schritt 6); diese gelten Abweichungen zwischen den Annotator:innen, nicht LLM-Fehlern. Gehört daher als eigene Auswertung in §9.2.
- Gewicht: mittel.

**V29** Im Protokoll und im Artikel einmal festlegen, was „Genauigkeit“ meint (Accuracy über die Auswertungsmenge, nicht Recall oder F1).
- Begründung: Die Literatur verwendet „accuracy“ je nach Aufgabe für Recall oder F1.
- Quellen: Navigli 2012, S. 118, Fn. 1 (Verweis auf die Zusammenfassung von Navigli 2009, Priorität 1).
- Status: neu.
- Gewicht: niedrig.

**V30** Bei der Einordnung der eigenen Zahlen gegen veröffentlichte Werte die Unterschiede ausdrücklich nennen: Behandlung mehrerer Gold-Senses (Basile entfernt Gold-Senses aus dem Menü, Meconi wertet wie die Primärregel), monoseme Wörter in XL-WSD-F1, MFS aus SemCor ungepaart, Mehrfach-Senses in WebCAGe als Artefakt der Inventarzuordnung, Abweichung des MHDBDB-ADJ vom STTS-ADJD.
- Begründung: Ohne diese Angaben sind die Zahlen nicht vergleichbar.
- Quellen: Basile et al. 2025, S. 3 Fn. 1, S. 8, Tab. 6 und 10; Meconi et al. 2025, S. 33898 bis 33900; Iacobacci et al. 2016, Tab. 3 und 4; Henrich et al. 2012 (WebCAGe-Zusammenfassung, Bezug Protokoll 6); Schiller et al. 1999, S. 23, 56; `docs/POS-TAGSET.md` §1.
- Status: neu.
- Gewicht: niedrig.

**V31** Für den Befund `KEINE_PASST` (§1 Nebenfrage, §9.2 „Ausweichlabels als Ergebnis“) die Herkunft des Begriffs „Historical Semantic Gap“ zitieren.
- Begründung: Der Begriff stammt von 2018 (Zuordnung einzelner Bedeutungen zu modernen Konzepten) und wurde 2020 auf Hallig-Wartburg übertragen.
- Quellen: Tittel & Chiarcos 2018, S. 62; Tittel et al. 2020, S. 8; Gengnagel et al. 2024, S. 3.
- Status: neu.
- Gewicht: niedrig.

### §10 Einfrieren und Ablage

**V32** Beim Canary-String die BIG-bench-Dokumentation als verbreitetes Vorbild zitieren.
- Quellen: Köhnlein 2025, S. 49 bis 50 (PDF 50 bis 51); Primärbeleg wäre die BIG-bench-Dokumentation.
- Status: neu (der Canary-String selbst ist in §10 vorgesehen).
- Gewicht: niedrig.

**V33** Im Artikel benennen, welche Lecktypen ausgeschlossen sind (Typologie nach Kapoor & Narayanan: Leave-out bei MFS, disjunkte Pilot-Lemmata, keine Typlisten in Prompt und Annotationsdatei), und die bewusste Abwägung gegen volle Reproduzierbarkeit (Labels bis zur Publikation privat, R2 statt R4) begründen.
- Quellen: Semmelrock et al. 2025, S. 3, 5.
- Status: neu (die Maßnahmen selbst sind umgesetzt: §9.2, §4.2, §10, B1).
- Gewicht: niedrig.

---

## B. knowledge/data.md

**V34** In Abschnitt 3 („Herkunft der Typlisten“) zwei Spuren ergänzen: den Hinweis auf Schmidt 1991 zur „automatischen Disambiguierung“ als möglichen Ort einer automatischen Vorbelegung, und den Vergleich mit dem DEAF, das Varianten an den Eintrag hängt, nicht an Bedeutungen (Hinweis, dass Typlisten an `<sense>` eine MHDBDB-Eigenheit sind; kein Beweis).
- Quellen: Hinkelmanns & Zeppezauer-Wachauer 2020, S. 74, Anm. 6; Tittel & Chiarcos 2018, S. 63. Ergänzend (Priorität 1, nicht ausgewertet): Schmidt 1985, S. 346 (häufigste Bedeutung als Vorgabe, Korrektur pro Beleg).
- Status: neu; die Feststellung, dass der Beitrag von 2020 keine graphematischen Types erwähnt, ist laut Zusammenfassung bestätigt und steht schon in Abschnitt 3.
- Gewicht: niedrig.

**V35** Bei B10 und in Abschnitt 3 („Token-`@pos` als Schichtungsgrundlage“) die Literatur nachtragen, nach der Token-Wortart teils über die Bedeutung entschieden wird (HiTS zu *guot* ‘Besitz’, STTS-Abgrenzungen).
- Quellen: Dipper et al. 2013, S. 107; Schiller et al. 1999, S. 12, 24, 57.
- Status: neu; gehört zu V6.
- Gewicht: niedrig.

**V36** Bei B11 belegen, dass der Zahlencode schon 2019 die Arbeitsschnittstelle zum Begriffssystem war.
- Quellen: Hinkelmanns & Zeppezauer-Wachauer 2020, S. 78, Anm. 9 bis 10.
- Status: neu.
- Gewicht: niedrig.

**V37** Für das Datasheet zwei Vergleichsfälle festhalten: mehrwertiges Token-`@pos` in der MHDBDB ist ungeregelt, während TüBa-D/Z Mehrwertigkeit eng und regelgeleitet zulässt und HiTS sie ablehnt; GermaNet führt eine Änderungshistorie mit Person und Vorzustand, die MHDBDB vor 2025-07 keine (B4).
- Quellen: Telljohann et al. 2017, S. 38 (PDF 39); Dipper et al. 2013, S. 109 bis 110; Henrich & Hinrichs 2010, S. 2230.
- Status: neu.
- Gewicht: niedrig.

---

## C. Literaturdateien, Prompt-Log, DMP, Artikel

### LITERATUR-STICHPROBE.md und LITERATUR-IAA.md

(Die Raganato-Zeile in `LITERATUR-STICHPROBE.md` steht bei V7.)

**V38** `LITERATUR-IAA.md`, „Historische Sprachen“: Prüfstatus für Dipper et al. 2013 von ○ auf ✔ setzen; die Aussage „ersetzt Intuition durch Belegsynopse und markiert unauflösbare Ambiguität bewusst nicht“ ist laut Zusammenfassung am Volltext belegt.
- Quellen: Dipper et al. 2013, S. 86, 109 bis 110.
- Status: neu; ✔ heißt nach Konvention der Datei „vom Agenten gelesen“, nicht von Julia.
- Gewicht: niedrig.

**V39** „Véronis 1998“ (Dice-Koeffizient; `LITERATUR-IAA.md` Zeile Henrich 2015, PROTOKOLL §9.2) vollständig bibliografieren als Véronis, *A study of polysemy judgments and inter-annotator agreement*, SENSEVAL-1, und gegen Ide & Véronis 1998 abgrenzen.
- Begründung: In `references.txt` steht nur Ide & Véronis 1998; Verwechslungsgefahr.
- Quellen: Ide & Véronis 1998 (Zusammenfassung, Hinweis zu S. 30); Literaturverzeichnis von Henrich 2015.
- Status: neu.
- Gewicht: niedrig.

**V40** `LITERATUR-IAA.md`, „Lücke“ und „LLMs bei historischen Sprachen“: weitere Belege ergänzen, dass Golddaten zur lexikalischen Semantik historischer Sprachen fehlen oder ohne IAA entstehen (GHisBERT, einzelne Fachperson bei Manjavacas & Fonteyn, Strutz, Tittel & Chiarcos), Jannidis et al. als Kontrast ohne Gold, Ide & Véronis als historischen Beleg für geringe Übereinstimmung (Sekundärwerte, vor SENSEVAL).
- Quellen: Beck & Köllner 2023, S. 38, 41; Manjavacas & Fonteyn 2022b, S. 128; Strutz 2026, S. 16, 18; Tittel & Chiarcos 2018, S. 62; Jannidis et al. 2025, S. 19 bis 20; Ide & Véronis 1998, S. 30.
- Status: neu.
- Gewicht: niedrig.

**V41** `LITERATUR-IAA.md`, Zeile Henrich 2015: die Feldpraxis ergänzen: Meconi et al. werten wie die Primärregel, Basile et al. entfernen Gold-Senses aus dem Menü (Henrichs Option „alle bis auf einen entfernen“); Ristic als Beispiel, wie großzügiges „irgendein Sense passt“ Werte hebt.
- Quellen: Meconi et al. 2025, S. 33898 bis 33899; Basile et al. 2025, S. 3, Fn. 1; Ristic 2025, S. 23, 29 bis 30, 47 (PDF 39, 45 bis 46, 63).
- Status: neu; stützt A14, ändert sie nicht.
- Gewicht: niedrig.

**V42** `LITERATUR-STICHPROBE.md`: in der Zeile „One sense per discourse“ WebCAGe als deutschen Beleg ergänzen (mit Vorbehalt zum Prüfweg); in der Zeile „Verben sind am schwersten“ die Einschränkung auf WordNet-Granularität und Meconi et al. als LLM-Beleg ergänzen.
- Quellen: Henrich et al. 2012, S. 390 (PDF 4); Raganato et al. 2017, S. 105 bis 106, Tab. 3 und 4; Meconi et al. 2025, S. 33913; schwächer Yae et al. 2025, PDF-S. 14 (nur Grafik).
- Status: neu.
- Gewicht: niedrig.

### PROMPT-LOG.md und DMP.md

**V43** `PROMPT-LOG.md`, Ebene A: neben `label` festhalten, nach welcher Parse-Regel das Label gewonnen wurde oder warum das Parsen scheiterte (eigener Wert „unparsbar“, „außerhalb des Menüs“ usw.).
- Begründung: Damit lassen sich LLM-Fehler später nach Ursache sortieren und die Kategorie aus V25 zählen.
- Quellen: Ristic 2025, Listing 4.1, S. 34 (PDF 50) (Vorschlag der Zusammenfassung, nicht aus der Arbeit); Köhnlein 2025, S. 72 bis 75.
- Status: neu; gehört zu V25.
- Gewicht: mittel.

**V44** `DMP.md` §2: Data Cards und Model Cards neben Datasheet und Data Statement nennen.
- Quellen: Semmelrock et al. 2025, S. 9 bis 10.
- Status: neu.
- Gewicht: niedrig.

**V45** Datennutzungsbedingungen des gewählten API-Zugangs dokumentieren.
- Quellen: Scholger & Bleier 2026, Abs. 35, 40.
- Status: **schon umgesetzt** in `DMP.md` §4 („Nutzungsbedingungen des Anbieters und Modellversion werden pro Lauf im Prompt-Log festgehalten“). Kein Handlungsbedarf außer beim Festlegen des Modells.
- Gewicht: niedrig.

### Artikel und Dissertationstext (kein Protokollinhalt)

**V46** Im Diskussions- bzw. Limitationsteil drei Punkte aufnehmen: den Einwand „warum ein großes allgemeines LLM statt eines kleinen historischen Modells, und warum Fachleute nur als Annotator:innen“; die Unterscheidung in vitro / in vivo (der Goldstandard misst WSD als isolierte Aufgabe); die ausdrückliche Abgrenzung gegen Active Learning (würde die Zufallsstichprobe verzerren; erst für eine spätere D0-Annotation sinnvoll).
- Quellen: Klein et al. 2025, S. 8 bis 9; Ide & Véronis 1998, S. 30 bis 33; Weeber et al. 2021, PDF-S. 2.
- Status: neu. **Verweis korrigiert:** Die Ide-&-Véronis-Zusammenfassung nennt „Protokoll 12“ als Ort für die Grenzen der Evaluation; §12 sind die offenen Punkte, einen Limitationsabschnitt hat das Protokoll nicht (einzige Limitation dort: die Doppelrolle, §7, Schritt 6).
- Gewicht: niedrig.

**V47** Im Inventar-Kapitel die Vergleichsfälle nutzen: WordNet (Sense als Synonymmenge, semasiologisch) gegenüber MHDBDB (Sense als Menge von Begriffszeigern, onomasiologisch), GermaNet *Nuss* (drei Felder, ein Feld pro Synset), LiLa (Lemma-Hub ohne Bedeutungsebene), DEAF (Definitionen und Bedeutungsbaum), Hallig-Wartburg als in der WSD-Literatur schon früh genanntes Inventar.
- Quellen: Miller 1995, S. 39 bis 40; Henrich & Hinrichs 2010, S. 2229, 2235, Abb. 2; Mambrini & Passarotti 2023, S. 2; Tittel & Chiarcos 2018, S. 59, 64; Ide & Véronis 1998, S. 3, 14 bis 15, Fn. 9; Navigli 2012, S. 116 bis 117.
- Status: neu.
- Gewicht: niedrig.

**V48** In Einleitung und Motivation: Knowledge-Acquisition-Bottleneck (kein Trainingskorpus für Mhd. außer Silber), Ressourcenkontrast zu Gegenwartssprache (alle Komponenten fertig verfügbar), Größenordnung des Abstands MFS zu starken Systemen vor und mit LLMs, Arbeitsbegriff LLM gegenüber feinabgestimmtem Modell, „Wortbedeutung im Kontext“ statt Äußerungsbedeutung.
- Quellen: Navigli 2012, S. 119; Iacobacci et al. 2016, S. 898, Tab. 3; Meconi et al. 2025, S. 33900; Matusch 2025, S. 17, 54, 57, 59; Yang et al. 2024, S. 2, 6 bis 7; Gengnagel et al. 2024, S. 5.
- Status: neu.
- Gewicht: niedrig.

**V49** Gegenüber dem Upstream-Projekt empfehlen, künftige LLM-Annotation der MHDBDB im TEI selbst zu kennzeichnen (die Dissertation musste LLM-berührte Tokens per Git-Vergleich rekonstruieren).
- Quellen: Steller 2024, S. 17 (Leitlinie 6).
- Status: neu; Entscheidung liegt nicht bei der Dissertation (siehe K5).
- Gewicht: niedrig.

---

## D. Fragen, die die Vorschläge offenlassen

### Fragen an die Daten

- **F1 Homographen: eigene Lemmata oder Senses eines Lemmas?** Wiederkehrend in Ganslmayer & Schwarz (Dipper S. 165, Anm. 12), Telljohann et al. 2017 (S. 34) und Köhnlein (Polysemiebegriff); berührt V2, `LEMMA_FALSCH` und die Polysemiestufen. Erste Zählung von mir (Commit `973c001a7`, `lexicon.xml`, nicht gegengelesen): Von 43.710 Einträgen teilen sich nur 102 Schreibungen auf mehr als einen Eintrag (216 Einträge). Beispiele für zusammengelegte Homographen: *bar* (`lemma_377`, ADJ/ADV/NOM) mit sechs Senses, darunter „Kleidung, Rüstung, Mangel“, „Verwandtschaft“, „Gebäude“, „Literatur, Gesang“; *wer* (`lemma_7482`, NOM) mit acht Senses von „Versprechen, Rechtswesen“ über „Mensch“ bis „Waffen, Kriegswesen“ und „Anlagen am Wasser“. Lexer-Homographen stehen also offenbar oft als Senses eines Lemmas; die Polysemiestufe schließt Homonymie ein. Nicht geprüft: wie viele Ziellemmata das betrifft. (Die Prio-1-Zusammenfassung Schmidt 1985 behandelt Homographen und ist hier nicht ausgewertet.)
- **F2 Partikelverben in Distanzstellung** (*er stuont ûf*): Basisverb oder Partikelverb lemmatisiert? Bestimmt das Menü von VRB-Items (V19 b). Quelle: Ganslmayer & Schwarz (Dipper S. 177 bis 178).
- **F3 Token-Wortart und Bedeutung:** Wie viele Paare der Grundgesamtheit haben ihre Wortart aus Schritt 2, und weicht ihre Sense-Verteilung von Paaren aus Schritt 1 ab? (V6, B10.)
- **F4 Ausschluss 4:** Wie viele der Lemmata mit disjunkten Token-`@pos` sind gewollte Wortartwechsel (substantivierter Infinitiv, substantiviertes Adjektiv) statt Lemmatisierungsfehler? (V5.)
- **F5 *stein* heute und 2019:** Hat der heutige Eintrag in `lexicon.xml` noch die sieben Bedeutungen mit ‚Mineralien‘ in dreien, wie im Artikel von 2020 abgebildet? Quelle: Hinkelmanns & Zeppezauer-Wachauer 2020, S. 77 bis 78.
- **F6 Abgeleitete Nomina:** Trennt das Begriffssystem abstrakte und konkrete Lesarten von Ableitungen auf -unge, -e, -heit regelhaft? (V19 a.)
- **F7 Werkbekanntheit als Kovariate:** Bekannte Werke dürften im LLM-Training liegen; ob Bekanntheit die LLM-Leistung verändert, wäre eine mögliche Kovariate. Nur Anregung. Quelle: Jannidis et al. 2025, S. 3, 16.
- **F8 KZW-Notizen in der Stichprobe:** Wie viele Senses der gezogenen Lemmata tragen eine der 94 Notizen (B13)? Entscheidet, wie dringend V12 und V16 sind.

### Fragen an Dritte (KZW, Upstream)

- **K1 (KZW): Typlisten und Herkunft von Silber.** Schon offen in `knowledge/data.md` §3. Neue Spuren dafür: Schmidt 1991 zur „automatischen Disambiguierung“ (Hinkelmanns & Zeppezauer-Wachauer 2020, S. 74, Anm. 6); Schmidt 1985, S. 346 (häufigste Bedeutung als Vorgabe, Prio 1). Frage: Wurde Silber ganz oder teilweise automatisch vorbelegt und pro Beleg korrigiert?
- **K2 (KZW): Bedeutungsumschreibungen im alten System.** Der Artikel von 2020 zeigt bei *stein* kurze menschliche Umschreibungen („Steine und Felsen“, „Edelsteine“). Gab es solche Umschreibungen pro Bedeutung, und sind sie noch irgendwo vorhanden? Sie wären menschliche Glossen, die heute fehlen (B13, V16).
- **K3 (KZW): Lemmatisierungspolitik** für Homographen (F1) und Partikelverben (F2), bevor man die Daten auszählt.
- **K4 (KZW, Upstream): Rechte** für die Weitergabe von Editionskontexten an einen kommerziellen LLM-Dienst (V15).
- **K5 (KZW, Upstream): Kennzeichnung** künftiger LLM-Annotation im TEI (V49).

### Offene bibliografische Punkte

- **Véronis 1998** (SENSEVAL-1, Dice) fehlt in `references.txt`; nicht mit Ide & Véronis 1998 verwechseln (V39).
- **Navigli, Litkowski & Hargraves 2007** (S07-1006): steht in `LITERATUR-STICHPROBE.md` mit ✔ als zweiter Beleg für „MFS hängt vom Dokument ab“, liegt aber nicht in `literatur/pdf/`; die Aussage dort prüfen (V7).
- **Kortmann 2020** beschaffen, falls V2 umgesetzt wird.
- **Hamp & Feldweg 1997** fehlt in `references.txt`, wird für jedes GermaNet-Zitat gebraucht (ACL Anthology W97-0802).
- **Miller (Hg.) 1990**, *IJL* 3(4): Seitenangabe 235 bis 312 (Miller 1995) gegen 235 bis 244 (Navigli 2012) klären.
- **Navigli 2012, 82 bis 83 %:** referierter Wert; vor einem Zitat an Chan et al. 2007 und Ponzetto & Navigli 2010 prüfen.
- **Primärquellen statt Sekundärzitat:** Gale et al. 1992b (MFS-Baseline, nach Ide & Véronis S. 6); Self-Consistency, arXiv 2203.11171 (Aggregation, nach Campesato S. 145); BIG-bench-Dokumentation (Canary); Balog 2018 und Shi et al. 2024 (Popularitätsprior, statt Matusch); Erk & McCarthy 2009; Vial et al. 2019; Kapoor & Narayanan (Lecktypologie); Schmidt 1988 und 1991 (nach Ide & Véronis Fn. 9 und Hinkelmanns 2020 Anm. 6); McCoy et al. 2019 u. a. (Black-Box-Kritik, statt Ristic).
- **STTS-Zitierweise:** TüBa-D/Z zitiert „Schiller, Teufel & Thielen 1995“; passt weder zur Fassung 1995 (vier Personen) noch genau zu 1999.
- **Fassungen:** An et al. (NeurIPS 2024) und Chen et al. (IJCAI-26, abweichende Autorenliste) mit der Verlagsfassung zitieren, die nicht gelesen ist; Liu et al. (RoBERTa) nur als Preprint; ob Devlin (NAACL-PDF) und Meconi (EMNLP-PDF) die arXiv-Dateien ersetzen, entscheidet Julia; Steller: `references.txt` zitiert v0.9.3, gelesen ist v0.9.1 (Seiten an v0.9.3 prüfen); Gengnagel et al.: Herkunft unklar, vielleicht DHd-2024-Panel; Basile et al.: begutachtete Fassung nicht gefunden (○).
- **Beck & Köllner 2023:** Eine Aussage „GHisBERT ist das einzige Modell, das Mhd. abdeckt“ stützt das Paper nicht; es sagt 2023 „to our knowledge“ (S. 36). Nicht als Gegenwartsaussage verwenden.
- **Innere Widersprüche in Quellen:** Yae et al. ordnen 61,22 % und 65,98 % PaLM-2 und GPT-3.5 widersprüchlich zu (Tab. 7 gegen PDF-S. 11 und Tab. 10); Basile et al. „best for all languages“ gegen Tab. 10 (Spanisch). Bei Manjavacas & Fonteyn sind Werte aus Abbildungen „[am PDF zu prüfen]“.
- **Code-Repositorien** von Yae, Basile und Meconi (vermutlich mit Parsing-Regeln, relevant für V25) nicht geöffnet.
- **Zur Beschaffung vorgeschlagen (Welle 1):** Ghizzota, Basile, Siciliani & Semeraro, CLiC-it 2025 (LLM-WSD für Latein; nicht dieselbe Arbeit wie Ghizzota et al. 2026 in `LITERATUR-IAA.md`); Pasini et al. 2021 (XL-WSD); Postma et al. 2016 (MFS-Bias); Manjavacas & Fonteyn 2021 (MacBERTh); Liu et al. 2024 (*Lost in the middle*); Zhao et al. 2021 (*Calibrate before use*); Kibria et al. 2024; Sumanathilaka et al. 2025; Wang et al. 2024 („My answer is C“); Maru et al. 2022 (im Protokoll zitiert, nicht im Ordner); Tittel, Bermúdez-Sabel & Chiarcos 2018 (RDFa); Liesenfeld & Dingemanse 2024.

---

## E. Abgleich mit dem Protokoll: Auffälligkeiten

- **Abschnittsverweise:** Von rund 40 stichprobenartig geprüften Verweisen passen fast alle. Falsch oder schief sind: „Protokoll 12“ für Grenzen der Evaluation (Ide & Véronis; §12 sind offene Punkte, V46); „Protokoll 4.9 … (Unsicherheit)“ (Pangakis & Wolken; §4.9 ist das Manifest, gemeint ist §9.1, Punkt 5); „PROTOKOLL §5 und §7 (doppelte Annotation)“ (Manjavacas & Fonteyn 2022b; §5 ist die Kartendarstellung, gemeint sind §7 und A5); „Protokoll 7, Schritt 6“ als Ort für LLM-Fehlercodes (Strutz, Manjavacas 2022a; die Ursachencodes gelten menschlichen Abweichungen, V28); „Protokoll 2 … Polysemie“ (Köhnlein; definiert nur in §4.3, V2).
- **Sachlich falsche Protokollaussagen:** §3 „Adverbien fehlen in den Vergleichsdatensätzen“ (V4); §4.4, Punkt 4 Raganato als Beleg für Klumpenstichproben, nach A13 noch übrig (V7).
- **Spannungen mit Entscheidungen oder Befunden:** „Karten ohne Glossen“ (V16) gegen B13 (94 KZW-Notizen); Ausschluss 4 als „Verdacht“ formuliert, aber als harter Ausschluss angewandt (V5); `PROMPT-LOG.md` verweist für den zählenden Lauf auf das Protokoll, das ihn noch nicht festlegt (V9). Unabhängig von den Zusammenfassungen: `knowledge/data.md` B8 und §4, Punkt 5 erwägen, Rückfall-Items aus dem primären Vergleich zu nehmen, während §9.2 sagt „Der Test läuft über alle Items“; diese Entscheidung ist offen.
- **Kein Vorschlag widerspricht A1 bis A14.** Mehrere stützen A14 (Basile, Meconi, Strutz, Ristic) oder A13 nur mittelbar; keiner verlangt, eine Primärregel zu ändern.

---

## Anhang: nur Stützung, kein Handlungsbedarf

Nach Protokollabschnitt; Seitenangaben aus den Zusammenfassungen, ungeprüft.

- **§1 / Forschungsfrage, LLM gegen MFS als ernsthafter Gegner:** Manjavacas & Fonteyn 2022b, S. 126 bis 128; Manjavacas & Fonteyn 2022a, Abb. 6, S. 9; Iacobacci et al. 2016, Tab. 3 und 4; Rekabsaz 2018, Tab. 7.1, S. 77 bis 78; Köhnlein 2025, S. 88; Ristic 2025, S. 43 bis 44; Yae et al. 2025 und Basile et al. 2025 (keine MFS, daher nicht einzuordnen; stützt A4, A11); Matusch 2025, S. 46; Steller 2024, S. 17 (Rule of Least Power).
- **§2 Sense als Begriffsgruppe, Silber nicht Gold:** Hinkelmanns & Zeppezauer-Wachauer 2020, S. 77 bis 78 (*stein*); Ide & Véronis 1998, S. 3, Fn. 9; Henrich et al. 2012 (WebCAGe als Silber-Vergleichsfall); Klein et al. 2025, S. 6, 8; Tittel & Chiarcos 2018, S. 62.
- **§3 Ausschluss PRP/ADV, Einheit Lemma × Wortart, mehrwertiges `@pos` ausgeschlossen:** Dipper et al. 2013, S. 90 bis 95, 102 bis 104, 109 bis 110; Bevilacqua et al. 2021, S. 4330, Anm. 1; Ide & Véronis 1998, S. 3 bis 4. **D1/D0-Verschiebung:** Bevilacqua et al. 2021, S. 4331; Ide & Véronis 1998, S. 27, 29 bis 30; Kowald et al. 2024, S. 10 bis 11.
- **§4.1 ungewichtetes Schätzziel, §4.3 Schichtung:** Ide & Véronis 1998, S. 33; Meconi et al. 2025, S. 33913 (Verben schwerer); Raganato et al. 2017, S. 103, 105; Iacobacci et al. 2016, S. 903; Yae et al. 2025, PDF-S. 14; Rekabsaz 2018, S. 6.
- **§4.4 Obergrenze pro Text, §9.1 Punkt 5 Bootstrap nach Text, zufällige Ziehung:** Henrich et al. 2012, S. 390; Ide & Véronis 1998, S. 26 bis 27; Weeber et al. 2021 (keine AL-Auswahl); Semmelrock et al. 2025, S. 8 (feste Seeds).
- **§4.6 Faktoren im gemischten Modell:** Pangakis & Wolken 2025, S. 1475, Anhang E; Ide & Véronis 1998, S. 25.
- **§4.7 Teststärke, Intervalle:** Köhnlein 2025, S. 83; Pangakis & Wolken 2025, S. 1481 (keine Intervalle, Gegenbeispiel).
- **§4.10 Freeze 2 überhaupt festschreiben:** Jannidis et al. 2025, S. 4, 8; Gengnagel et al. 2024, S. 4; Campesato 2024, S. 43, 129 bis 132, 168 bis 169; Kowald et al. 2024, S. 11; Liu et al. 2019, S. 1, 7 bis 8.
- **§5 keine LLM-Definitionen, nur menschliche Begriffsnamen:** Basile et al. 2025, S. 4, 6 (maschinell übersetzte Glossen senken Werte); Klein et al. 2025, S. 6; Tittel & Chiarcos 2018, S. 59; Gengnagel et al. 2024, S. 2. **§5 Punkt 2 unterscheidende Begriffe:** Hinkelmanns & Zeppezauer-Wachauer 2020 (‚Mineralien‘ in drei von sieben Bedeutungen). **§5 Punkt 5 Reihenfolge mischen:** An et al. 2024; Yang et al. 2024, S. 21.
- **§6 Statusliste, `LEMMA_FALSCH`, `KEINE_PASST`:** Henrich et al. 2012, S. 394 (Zielworterkennung fehlerhaft); Mambrini & Passarotti 2023, S. 2; Bevilacqua et al. 2021, S. 4331, 4335; Ide & Véronis 1998, S. 28, 33; Jannidis et al. 2025, S. 8; Manjavacas & Fonteyn 2022b, S. 134 (Unklar-Kategorie W/M); Rekabsaz 2018, S. 101 bis 102. **Blindheit:** Kowald et al. 2024, S. 5 bis 6; Telljohann et al. 2017, S. 19, 33 (Gegenmodell Vorannotation).
- **§7 Doppelannotation und Adjudikation statt Einzelgold:** Köhnlein 2025, S. 58 bis 59, 87; Strutz 2026, S. 16, 18; Matusch 2025, S. 51; Ristic 2025, S. 35 bis 36, 51; Manjavacas & Fonteyn 2022b, S. 128; Klein et al. 2025, S. 8. **Pilot mit frischen Items:** Pangakis & Wolken 2025, Abb. 3.
- **§8 Nachvollziehbarkeit:** Henrich & Hinrichs 2010, S. 2230 (Parallele aus der Lexikografie).
- **§9.1 Rohübereinstimmung neben α, Zufallsmodell pro Lemma, Prävalenz:** Bevilacqua et al. 2021, S. 4334; Pangakis & Wolken 2025, Anhang E (gepoolte Reliabilität verwischt); Rekabsaz 2018, S. 102. **Zwei Ebenen:** Navigli 2012, S. 117 bis 118; Meconi et al. 2025, S. 33903.
- **§9.2 Macro-Genauigkeit, Nicht-MFS-Items, Ausweichlabels getrennt, getrennte Maße statt Gesamtwert:** Raganato et al. 2017, S. 106 (MFS-Bias über 75 %); Meconi et al. 2025, S. 33900 bis 33901 (hardEN); Matusch 2025, S. 46, 58, 75; Strutz 2026, S. 6 bis 7, 12, 16; Kowald et al. 2024, S. 11; Yang et al. 2024, S. 21; Jannidis et al. 2025, S. 13. **MFS mit Leave-out aus Korpus-Silber, Rückfall getrennt ausweisen:** Raganato et al. 2017, S. 103 bis 104, Tab. 4 (mit B8); Manjavacas & Fonteyn 2022b (Wörterbuch-MFS nicht vergleichbar); Henrich et al. 2012, S. 391 (Sense-Verteilung aus Ernte statt Gebrauch). **Gepaarter Test:** Rekabsaz 2018, S. 77 bis 78; Ristic 2025, S. 43 bis 44. **Fachliche Validierung als DH-Forderung:** Steller 2024, S. 18 (Leitlinie 11). **Lücke onomasiologisches Inventar:** Beck & Köllner 2023, S. 38, 41; Tittel & Chiarcos 2018, S. 62; Gengnagel et al. 2024, S. 3.
- **§10 Labels privat, Kontamination:** Henrich et al. 2012 (öffentliche Labels); Meconi et al. 2025, S. 33909; Jannidis et al. 2025, S. 3; Yang et al. 2024, S. 23; Yae et al. 2025 (Gegenbeispiel); Scholger & Bleier 2026, Abs. 35; An et al. 2024, S. 16 (nur eigenes Training); Gengnagel et al. 2024, S. 9 (sagt nichts über Testdaten). **Versionierung von Inventar und Korpus:** Raganato et al. 2017, S. 99; Mambrini & Passarotti 2023.
- **§11 Präregistrierung und Abweichungslog:** Semmelrock et al. 2025, S. 11 bis 12; Kowald et al. 2024, S. 11.
- **`knowledge/data.md`:** B1 Leckgefahr (Matusch 2025, S. 53, 71; Meconi et al. 2025; Henrich et al. 2012, S. 390); B9 unbelegte Senses (Ide & Véronis 1998, S. 20 bis 21; Bevilacqua et al. 2021, S. 4333; Meconi et al. 2025, S. 33906); Abschnitt 3, Herkunft der Typlisten (Hinkelmanns & Zeppezauer-Wachauer 2020 erwähnt keine graphematischen Types: bestätigt); §12, Punkt 9 Datierung (Hinkelmanns & Zeppezauer-Wachauer 2020, S. 79).
- **`PROMPT-LOG.md`:** Ebene A Felder `modell`, `parameter`, `ausgabe_roh` (Scholger & Bleier 2026, Abs. 2, 5 bis 7; Köhnlein 2025, S. 72 bis 75); Ebene B Prompt beilegen (Scholger & Bleier 2026, Abs. 36).
- **Ohne Bezug zum Protokoll:** Devlin et al. 2019 und Liu et al. 2019 (nur für einen etwaigen Encoder-Vergleich, V1); Chen et al. 2025 außer V9; An et al. 2024 außer V11.
