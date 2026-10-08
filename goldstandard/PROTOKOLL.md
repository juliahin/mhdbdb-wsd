# WSD-Goldstandard: Protokoll v2

**Status:** Entwurf vom 2026-10-08, noch nicht eingefroren.
**Verantwortlich:** Julia Hintersteiner. Zweiter Annotator: Alan van Beek.
**Vorgänger:** präregistriertes Evaluationsprotokoll vom 2026-04-24, wiederherstellbar mit
`git show 873322658^:docs/features/034-wenzelsbibel-annotation.md` (Abschnitt „Pre-registered evaluation protocol").

Dieses Dokument ersetzt die Präregistrierung nicht stillschweigend. Jede Änderung gegenüber
2026-04-24 steht mit Begründung im Abweichungslog (Abschnitt 11). Sobald die Stichprobe gezogen
ist, wird diese Fassung eingefroren; spätere Änderungen sind dann neue Einträge im Log, keine
Umformulierungen.

---

## 1. Forschungsfrage

Übernommen aus der Präregistrierung, in der Baseline präzisiert:

> Erreicht LLM-gestützte Bedeutungsdisambiguierung (WSD) auf mittelhochdeutschem Text eine
> höhere Genauigkeit als die Most-Frequent-Sense-Baseline, gemessen an einem neu erhobenen,
> doppelt annotierten menschlichen Goldstandard?

Nebenfragen, die das Design ohne Mehraufwand mitbeantwortet:

- Wie verlässlich ist die bestehende MHDBDB-Bedeutungsannotation (Silber), gemessen am neuen Gold?
- Wie oft passt keine Bedeutung des Inventars? Das ist ein Befund über das Begriffssystem (#63).

## 2. Begriffe

| Begriff | Bedeutung hier |
|---|---|
| **Gold** | Bedeutungszuweisung, die für dieses Protokoll von zwei Annotator:innen unabhängig, blind und unter dokumentierten Richtlinien erhoben und danach adjudiziert wurde. |
| **Silber** | Die bestehende `@ana`-Annotation im Korpus. Sie stammt von Menschen, aber es ist nicht dokumentiert, von wem, wann und nach welchen Richtlinien. Deshalb kann sie nicht als Gold gelten. |
| **Inventar** | Die `<sense>`-Einträge eines Lemmas in `authority-files/lexicon.xml`. Ein Sense ist ausschließlich durch seine Begriffszeiger (`<ptr target="concepts.xml#…">`) bestimmt, die auf das geprüfte Begriffssystem der MHDBDB verweisen. |
| **Begriffsgruppe** | Die Menge der Begriffe, auf die ein Sense zeigt. Sie ist das, was Annotator:innen als „Bedeutung" sehen. |

**Was über Silber bekannt ist:** Laut Hinkelmanns & Zeppezauer-Wachauer (2023) wurden
MHDBDB-Bedeutungen an graphematische Typen im Wortartikel gehängt (nur über eine
Literaturrecherche erschlossen, Originaltext noch selbst zu prüfen). Das Korpus zeigt aber
mehr als reine Typ-Annotation. Gemessen am 2026-10-08 über alle Silber-Tokens polysemer
Lemmata (444.428 mit `corresp`): Bei 25,0 % der 29.677 Kombinationen aus Lemma und Typ tragen
Tokens derselben Wortform verschiedene Senses. Nur bei 34,1 % der Tokens ist der Sense durch den
Typ eindeutig festgelegt (darin auch Typen mit nur einem Beleg). Der Mehrheitssense des Typs
trifft 85,7 %. Silber ist also zumindest teilweise pro Beleg entschieden; wie, bleibt undokumentiert.

Hinweis zur Benennung: Das Sense-Attribut im Korpus heißt `@ana`, nicht mehr `@meaningRef`
wie in der Präregistrierung und in `.agent/workflows/sense-disambiguator.md`.

## 3. Grundgesamtheit und Ausschlüsse

**Grundgesamtheit:** alle `<w>` im Korpus mit `@lemmaRef` auf ein Lemma, dessen Inventar mindestens
zwei Senses hat und dessen Wortart laut `lexicon.xml` NOM, VRB oder ADJ ist (VEX und VEM werden VRB
zugeschlagen).

**Schicht „Silber":** Jedes Token gehört entweder zu *Silber ja* (trägt `@ana`) oder zu *Silber
nein*. Beide Schichten werden gezogen. *Silber nein* ist der Korpusteil, für den WSD gebraucht
wird; *Silber ja* erlaubt nebenbei die Messung der Silberqualität.

**Ausschlüsse** (jeder Ausschluss wird mit Anzahl im Datasheet dokumentiert):

1. Tokens, deren `@lemmaRef` oder `@ana` von einem LLM-Lauf stammt (u. a. WZB Phase 1b bis 3,
   #198, #216, #369/#371, #387, GWTK). Grundlage: `revisionDesc` der Texte und `ingest/pos-disambig/*/`.
   Die Ausschlussliste muss vor der Ziehung gebaut werden (offener Punkt).
2. Lemmata, bei denen zwei Senses dieselbe Begriffsgruppe haben. Diese Senses sind für niemanden
   unterscheidbar. Gemessen am 2026-10-08: 22 Lemmata.
3. Lemmata mit mindestens einem Sense ohne Begriffszeiger. Er ließe sich nicht darstellen.
   Gemessen am 2026-10-08: 126 Senses ohne Zeiger (Anzahl der betroffenen Lemmata noch zu zählen).
4. Lemmata mit disjunkten Token-`@pos`-Werten (Verdacht auf Lemmatisierungsfehler), wie in
   `goldstandard-test.py`. In der Teilmenge der 190 vollständig annotierten Texte: 763 Lemmata.

## 4. Stichprobendesign

**Zellen:** 36 = Polysemiegrad laut Inventar (2 / 3 / 4+) × Wortart (NOM / VRB / ADJ) ×
Frequenzquartil.

- **Frequenz** wird über das ganze Korpus gezählt, nicht über eine Teilmenge. In der Teilmenge
  der 190 vollständig annotierten Texte lagen die Quartilgrenzen bei 1 / 4 / 13, Q1 bestand
  damit nur aus Wörtern, die dort genau einmal vorkommen.
- **Polysemie nach Inventar, nicht nach Belegung:** Die Menügröße bestimmt die Schwierigkeit für
  Mensch und LLM. Dass bei 1.444 von 1.737 Ziel-Lemmata (Teilmenge, 2026-10-08) nicht alle
  Inventar-Senses im Silber belegt sind, ist ein Befund fürs Datasheet, kein Schichtungsmerkmal.

**Umfang:** N ≈ 500, also ca. 14 Tokens pro Zelle.

**Innerhalb einer Zelle:** höchstens ein Token pro Lemma, damit hochfrequente Lemmata (*haben*,
*werden*) die Stichprobe nicht dominieren. Aufteilung auf *Silber ja / nein* siehe offene Punkte.

**Ausgleich der Korpus-Schieflage (Gattung, Text):** Die Stichprobe soll das Korpus möglichst
in seiner Breite abbilden und den überlieferungsbedingten Bias abmildern, ohne Zellen leerlaufen
zu lassen. Befund vom 2026-10-08 (alle 667 Texte, 7.545.732 lemmatisierte Tokens):

- Wenige große Texte dominieren: OVG allein 4,6 %, die zehn größten zusammen rund 26 %.
- Lyrik umfasst 485 Texte, aber nur 3,6 % der Tokens; Fachliteratur liegt bei rund 0,4 %.
  Eine tokenproportionale Ziehung würde beides fast verschwinden lassen.
- Die Gattungstaxonomie (`genres.xml`, 615 Gattungen) ist polyhierarchisch und flach: Fast alle
  Gattungen hängen direkt an den beiden Wurzeln „Epik, Lyrik und Dramatik" und „Wissensliteratur
  und Gebrauchsliteratur". Eine verwendbare Ebene von Obergattungen gibt es nicht; sie muss
  philologisch festgelegt werden (offener Punkt). 406 Texte haben eine Gattung, 260 mehrere, TRO hat keine.
- Eine Datierung pro Text liegt nicht maschinenlesbar vor (alle Header tragen pauschal `gmh`, #118).
  Vers/Prosa lässt sich aus dem Markup nicht verlässlich ablesen (WZB ist Prosa, steht aber in `<l>`).

Vorgeschlagenes Verfahren:

1. **Obergattungsgruppen** (ca. 6 bis 8, z. B. höfische und heroische Großepik, Lyrik,
   Kleinepik, geistliche Literatur, Lehrdichtung und Didaxe, Historiografie, Fach- und
   Gebrauchsliteratur) als eigene, versionierte Zuordnungstabelle Gattung → Gruppe. Bei
   Mehrfachzuordnung entscheidet eine dokumentierte Regel.
2. **Kompromissallokation:** Der Zielanteil einer Gruppe ist proportional zur Quadratwurzel ihres
   Tokenanteils (Potenzallokation zwischen proportional und gleich verteilt). Das hebt Lyrik und
   Fachliteratur an, ohne sie so stark zu gewichten wie die Großepik.
3. **Umsetzung als weiche Quote:** Die 36 Zellen bleiben die harte Schichtung. Innerhalb einer Zelle
   wird mit Gewichten gezogen, sodass die Gruppenanteile über die ganze Stichprobe den Zielanteilen
   nahekommen. Die erreichten Anteile werden im Datasheet berichtet.
4. **Obergrenze pro Text:** höchstens wenige Tokens aus einem Text (Wert offen), damit OVG, PL1 bis PL3,
   JT und TRO nicht dominieren.
5. Die Gruppen- und Textgewichte gehen in die gewichtete Auswertung (oben) ein.

**Zufall:** fester Seed, im Manifest dokumentiert. Das Ziehungsskript wird mit eingefroren.

**Was die Zellen leisten und was nicht:** Sie sorgen für eine ausgewogene Abdeckung. Mit 14 Tokens
pro Zelle sind Zellwerte zu unsicher für eigene Schlüsse. Inferenz läuft über die Randverteilungen
(je Polysemiegrad, Wortart, Quartil mindestens ca. 120 Tokens) und über das Gesamtergebnis.

**Gewichtung:** Die gleiche Besetzung der Zellen bildet die Korpusverteilung nicht ab. Ergebnisse
werden zweifach berichtet: ungewichtet (zellbalanciert) und mit Gewichten nach dem Tokenanteil
der Zelle in der Grundgesamtheit.

## 5. Darstellung des Inventars: Vergabe der Begriffsgruppen

Die Bedeutungsangaben sind die Begriffsnamen des geprüften MHDBDB-Begriffssystems
(`concepts.xml`, deutsche `<term>`). Sie sind von Menschen erstellt. Es werden **keine**
LLM-generierten Definitionen gezeigt, weil ein LLM sonst gegen eine Annotation evaluiert würde,
die es selbst mitformuliert hat.

**Vorgeschlagenes Verfahren (hybrid):**

1. **Primärer Weg: Sense wählen.** Jeder Sense des Lemmas erscheint als Karte mit seiner
   Begriffsgruppe: Begriffsname plus Pfad zum Oberbegriff (`ptr type="broader"`). Die Annotator:in
   wählt die passende Karte. Das Ergebnis ist eine Sense-ID und damit direkt vergleichbar mit
   Silber und LLM-Ausgabe.
2. **Unterscheidende Begriffe hervorheben.** Begriffe, die nur in dieser einen Karte des Lemmas
   vorkommen, werden hervorgehoben. Das hilft bei den Fällen, in denen die Begriffsgruppe eines
   Sense eine echte Teilmenge einer anderen ist: Am 2026-10-08 betraf das 1.972 von 43.049
   Sense-Paaren innerhalb eines Lemmas (4,6 %).
3. **Mehrere passen.** Ist die Stelle zwischen zwei oder mehr Senses unterbestimmt, dürfen mehrere
   Karten gewählt werden. Das ist ein eigener Status und wird in der Auswertung getrennt behandelt.
4. **Keine passt.** Dann kann die Annotator:in aus allen Begriffen, die in den Karten dieses Lemmas
   vorkommen, die passenden ankreuzen und einen Kommentar schreiben. So entsteht ein Beleg dafür,
   welche Begriffskombination das Inventar nicht anbietet. Freies Durchsuchen des ganzen
   Begriffssystems ist für die Annotationsrunde bewusst nicht vorgesehen (Überforderung); es
   kann in der Adjudikation nachgeholt werden.
5. **Reihenfolge der Karten** wird pro Item zufällig gemischt, weil die Lexikonreihenfolge mit der
   Häufigkeit zusammenhängen kann. Die gezeigte Reihenfolge wird protokolliert.

## 6. Annotationsaufgabe und Ausweichlabels

Jedes Item endet mit genau einem Status:

| Status | Bedeutung | Pflichtangaben |
|---|---|---|
| `SENSE` | genau ein Sense passt | Sense-ID |
| `MEHRERE` | mehrere Senses passen gleichermaßen | mindestens zwei Sense-IDs |
| `KEINE_PASST` | kein Sense des Inventars passt | optional Begriffe, Kommentar empfohlen |
| `LEMMA_FALSCH` | das Token gehört nicht zu diesem Lemma | Kommentar, wenn möglich mit richtigem Lemma |
| `KONTEXT_UNZUREICHEND` | auch der erweiterte Kontext entscheidet nicht | keine |
| `TEXT_DEFEKT` | Token oder Transkription ist beschädigt | Kommentar |

**Quer dazu, bei jedem Item:** Sicherheit (sicher / eher sicher / unsicher) und ein freies
Kommentarfeld. „Unsicher" ist bewusst kein eigener Status, damit eine unsichere Entscheidung
trotzdem eine Entscheidung bleibt und in die Übereinstimmung eingeht.

**Kontext:** Standardmäßig wird ein begrenzter Ausschnitt gezeigt, auf Knopfdruck ein größerer.
Ob erweitert wurde, wird protokolliert. Umfang des Ausschnitts: offener Punkt.

**Blindheit:** Die Annotationsdatei enthält weder Silber-`@ana` noch LLM-Vorschläge. Die
Blindheit ist damit technisch gesichert, nicht nur durch eine Anweisung.

## 7. Ablauf

Der Ablauf folgt dem in der Annotationsliteratur üblichen Zyklus (Pustejovsky & Stubbs 2012;
Hovy et al. 2006; Belege in [LITERATUR-IAA.md](LITERATUR-IAA.md)).

1. **Richtlinien v0** mit einer Entscheidungsregel für jeden Status aus Abschnitt 6.
2. **Pilot:** ca. 50 Items **außerhalb** der Hauptstichprobe, von beiden blind annotiert.
   Übereinstimmung und Konfusionsmatrix rechnen, Abweichungen besprechen, Richtlinien und
   Oberfläche nachschärfen. Mit **frischen** Items wiederholen, bis eine vorab festgelegte Schwelle
   erreicht ist (Vorschlag: α ≥ 0,80, Untergrenze 0,67 nach Krippendorff; OntoNotes verlangte
   90 % Rohübereinstimmung). Pilotitems gehen weder in den berichteten IAA-Wert noch ins Gold.
3. **Einfrieren:** Richtlinien mit Versionsnummer und Prüfsumme; Schwelle, Maße und
   Auswertungsplan werden vor der Hauptrunde festgeschrieben.
4. **Hauptrunde:** beide annotieren alle Items unabhängig und blind. Die Itemreihenfolge wird pro
   Annotator:in zufällig gemischt (Seed protokolliert), weil Reihenfolge Urteile verschiebt
   (Beck et al. 2024). Kurze Sitzungen; die Zeitstempel erlauben nachträglich eine Prüfung auf
   Ermüdung und Drift.
5. **Roh-IAA zuerst:** Die Übereinstimmung wird gerechnet und festgehalten, **bevor** irgendeine
   Abweichung besprochen wird.
6. **Adjudikation:**
   - **blind:** Die Adjudikation sieht beide Labels, aber nicht, von wem sie stammen.
   - **Ursachencode pro Abweichung,** angelehnt an Barteld et al. (2015) und um zwei Codes
     erweitert: Richtlinienlücke, Versehen, echte Textambiguität, Inventarlücke,
     Editions- oder Normalisierungseffekt.
   - **Dritte Person:** Weil Julia die Richtlinien entworfen hat und zugleich annotiert, kann ihr
     implizites Wissen die Übereinstimmung aufblähen. Eine dritte Person prüft deshalb mindestens
     eine Zufallsauswahl von 10 bis 20 % der Adjudikationen sowie **alle** Fälle, in denen Julias
     Label übernommen wurde. Die Doppelrolle wird in der Publikation als Limitation genannt.
   - `MEHRERE` darf als Mehrfachlabel ins Gold eingehen, wo die Richtlinien es zulassen.
7. **Alles bleibt erhalten:** Labels vor der Adjudikation, Sicherheitsangaben, Ereignisprotokolle,
   Richtlinienversionen (Prabhakaran et al. 2021; Plank 2022: Abweichung ist oft Signal).
8. **Erst danach** werden Silber und LLM-Ausgabe mit dem Gold verglichen.

## 8. Nachvollziehbarkeit beim Annotieren

Für jede Entscheidung muss feststellbar sein: wer, wann, was, auf welcher Grundlage.

- **Wer:** Pro Annotator:in wird eine eigene Datei gebaut, in der die Kennung fest eingetragen
  ist. Es gibt kein Login und keine Namenseingabe, die man vergessen oder vertippen kann.
- **Auf welcher Grundlage:** Jede Datei trägt Korpus-Commit, Prüfsumme des Manifests,
  Richtlinienversion und Werkzeugversion. Jeder Export enthält diese Angaben.
- **Was und wann:** Ein Ereignisprotokoll, an das nur angehängt wird. Jede Aktion ist ein Eintrag:
  Zeitstempel (ISO 8601 mit Zeitzone), Item-ID, Aktion, Wert, gezeigte Kartenreihenfolge,
  ob der Kontext erweitert war, Verweildauer. Korrekturen überschreiben nichts. Das Endlabel ist
  die letzte Entscheidung; frühere bleiben sichtbar.
- **Rückgabe:** Export als JSON mit vollständigem Protokoll. Beim Wiederaufnehmen (Import) wird
  die Manifest-Prüfsumme verglichen, damit kein Export in die falsche Runde gerät.
- **Adjudikation** wird genauso protokolliert: wer, wann, welches Ergebnis, Begründung.

## 9. Auswertung

### 9.1 Übereinstimmung zwischen den Annotator:innen

Zwei Ebenen werden getrennt ausgewertet (Artstein & Poesio 2008 verlangen, die Behandlung
solcher Sonderfälle offenzulegen):

- **Statusebene:** Konfusionstabelle über die sechs Status aus Abschnitt 6, mit Häufigkeiten.
- **Sense-Ebene:** nur Items, bei denen beide `SENSE` oder `MEHRERE` vergeben haben.
  `KONTEXT_UNZUREICHEND` und `TEXT_DEFEKT` gelten hier als fehlende Werte, `KEINE_PASST` als
  eigene Kategorie.

Auf der Sense-Ebene werden berichtet:

1. **Hauptmaß:** Krippendorffs α mit MASI-Distanz (Passonneau 2006), damit `MEHRERE` als
   Teilübereinstimmung zählt. Dazu α nominal (Mengen als unteilbare Labels) als untere Schranke.
2. **Rohübereinstimmung** (exakt und „Überschneidung"). Nur sie ist direkt mit LLM- und
   MFS-Genauigkeit vergleichbar (Kilgarriff 2001).
3. **Zufallsmodell über Lemmata hinweg:** Jedes Lemma hat sein eigenes Inventar, und pro Lemma
   gibt es meist nur ein Token. Naives Poolen über alle Sense-IDs macht die erwartete
   Übereinstimmung winzig und bläht den Wert auf. Festlegung dieses Protokolls: Die erwartete
   Übereinstimmung wird pro Lemma aus den Sense-Anteilen berechnet und über die Items summiert,
   κ = (ΣA_o − ΣA_e) / (N − ΣA_e). Für diese Konstruktion haben wir keinen etablierten Standard
   gefunden; sie wird daher begründet und die gepoolte Variante daneben berichtet.
4. **Prävalenz:** Bei einem dominanten Sense kann allein das Zufallsmodell κ um mehr als 0,2
   verschieben (Senseval-3: 0,58 gegenüber 0,35 auf denselben Daten; Mihalcea et al. 2004).
   Deshalb werden die Sense-Randverteilungen, die Übereinstimmung getrennt für MFS- und
   Nicht-MFS-Tokens und Gwets AC1 als Kontrollgröße mitberichtet.
5. **Konfidenzintervalle:** 95 %, per Bootstrap. Gezogen wird nach Clustern (Text), weil Tokens
   aus demselben Text nicht unabhängig sind. Grobe Erwartung: bei N ≈ 500 etwa ±0,05 bis ±0,09,
   bei Untergruppen von ca. 120 Items etwa ±0,11 bis ±0,18 (eigene Rechnung mit der
   Großstichproben-Näherung, nachgerechnet am 2026-10-08).
6. **Aufschlüsselung** nach Polysemiegrad, Wortart, Frequenzquartil, Obergattungsgruppe und
   angegebener Sicherheit, jeweils mit Intervall.
7. **Zwei Ebenen des Begriffssystems:** zusätzlich die Übereinstimmung, wenn jeder Sense auf die
   Oberbegriffe seiner Begriffe abgebildet wird. Die Granularität ist der stärkste bekannte
   Einflussfaktor auf WSD-Übereinstimmung (Ng et al. 1999; Hovy et al. 2006). Das grobe Maß wird
   vorab definiert, nicht nachträglich durch Zusammenlegen gewonnen (Artstein & Poesio 2008).

### 9.2 Gold, Silber, LLM

- **Jede:r gegen das Gold:** Übereinstimmung jeder Annotator:in mit dem adjudizierten Gold, dazu die
  Adjudikationsstatistik nach Ursachencode. Hohe Roh-IAA sagt nichts über die Qualität des
  adjudizierten Golds (Passonneau & Carpenter 2014).
- **Silberqualität:** Genauigkeit von Silber-`@ana` gegen Gold, nur Schicht *Silber ja*.
- **LLM gegen Baseline:** Genauigkeit gegen Gold. Die MFS-Baseline wird aus Silber gelernt,
  **ohne** die Stichproben-Tokens, und auf denselben Gold-Items gemessen. Damit ist der Vergleich
  gepaart (McNemar-Test) statt gegen einen festen Wert.
- **LLM gegen menschliche Annotator:innen:** Zusätzlich zum Vergleich mit dem Gold wird geprüft,
  ob das LLM mit den beiden Menschen so gut übereinstimmt wie diese untereinander (Prinzip des
  „Alternative Annotator Test", Calderon et al. 2025). Die menschliche IAA ist die Obergrenze,
  an der LLM-Werte gemessen werden.
- **Zahlenstand zur Einordnung:** Die präregistrierte Baseline lag bei 66,7 %. In-sample aus
  Silber gerechnet ergab `goldstandard-test.py` am 2026-10-08 auf den 190 vollständig annotierten
  Texten 0,744 (tokengewichtet). Beide Werte sind in-sample und daher optimistisch; keiner von
  beiden ist die Baseline dieses Protokolls.
- **Ausweichlabels als Ergebnis:** `KEINE_PASST` mit angekreuzten Begriffen ist ein Befund über
  Lücken im Inventar. Eine IAA-Studie für ein onomasiologisches Inventar (Begriffssystem statt
  Wörterbuch) haben die Recherchen nicht gefunden; das ist ein eigener Beitrag der Arbeit.

## 10. Einfrieren und Ablage

| Gegenstand | Wo | Öffentlich? |
|---|---|---|
| Protokoll, Richtlinien, Datasheet | dieses Verzeichnis | ja |
| Manifest: Token-IDs, Zellzuordnung, Seed, Korpus-Commit, Prüfsummen von Korpus, `lexicon.xml`, `concepts.xml` | dieses Verzeichnis | ja |
| Ziehungsskript | dieses Verzeichnis | ja |
| Menschliche Labels, Ereignisprotokolle, Adjudikation | privat (Drive oder privates Repo) | erst mit der Publikation, dann Zenodo |

Grund für die Trennung: Öffentliche Labels können in die Trainingsdaten künftiger LLMs geraten,
die später gegen genau diesen Goldstandard evaluiert werden sollen (Sainz et al. 2023). Die
mittelhochdeutschen Texte sind ohnehin online; zu schützen sind die Labels.

**Bei der Veröffentlichung** (Jacovi et al. 2023): Labels verschlüsselt ablegen, Passwort in der
Publikation, Lizenz ohne Weiterverbreitung und ohne Trainingsnutzung, dazu ein Canary-String.
Die Labels vor der Adjudikation werden mitveröffentlicht.

## 11. Abweichungslog gegenüber der Präregistrierung vom 2026-04-24

| Nr. | Präregistriert | Jetzt | Begründung | Datum |
|---|---|---|---|---|
| A1 | Gold = bestehende MHDBDB-Annotation | Gold = neue Doppelannotation, bestehende Annotation = Silber | Herkunft, Zeitpunkt und Richtlinien der Bestandsannotation sind undokumentiert | 2026-10-08 |
| A2 | Quelle: bereits annotierte Texte ohne WZB | ganzes Korpus, geschichtet nach Silber ja/nein, ohne LLM-berührte Tokens | Mit A1 entfällt der Grund, nur annotierte Texte zu nehmen; der unannotierte Teil ist die eigentliche Zielpopulation | 2026-10-08 |
| A3 | 6 Zellen mit je ≥ 50 | 36 Zellen mit je ca. 14, Frequenz über das ganze Korpus, höchstens 1 Token pro Lemma und Zelle | Frequenz als Schwierigkeitsfaktor; Zellen dienen der Balance, Inferenz über Randverteilungen | 2026-10-08 |
| A4 | feste Baseline 66,7 %, einseitiger Binomialtest | MFS aus Silber ohne Stichprobe, gepaart auf denselben Items (McNemar) | Feste Baseline ist in-sample und auf anderer Population gerechnet | 2026-10-08 |
| A5 | Julia blind gegen LLM und Gold | zwei menschliche Annotator:innen (Julia, Alan van Beek) und Adjudikation | Gold braucht gemessene Übereinstimmung zwischen Menschen | 2026-10-08 |
| A6 | Sense-Wahl, LLM darf `abstain` | Statusliste mit Ausweichlabels und `MEHRERE` | Das Inventar passt nicht immer; erzwungene Wahl brächte Fehlzuordnungen ins Gold | 2026-10-08 |
| A7 | keine Gattungsbalance | weiche Gattungsquote mit Quadratwurzel-Allokation, Obergrenze pro Text | Überlieferungsbedingter Bias des Korpus soll im Goldstandard abgemildert werden | 2026-10-08 |
| A8 | Cohen's κ zwischen LLM und Julia | α mit MASI als Hauptmaß, Statusebene getrennt, Bootstrap-Intervalle nach Text, AC1 als Kontrolle | WSD-spezifische Literatur (Artstein & Poesio 2008; Passonneau 2006) und starke Prävalenz | 2026-10-08 |

## 12. Offene Punkte

1. **Silber-Aufteilung je Zelle:** hälftig oder nach Anteil in der Grundgesamtheit?
2. **Dritte Person** für die Prüfung der Adjudikation (Abschnitt 7, Schritt 6), z. B. KZW?
   Und wer adjudiziert selbst: Julia und Alan gemeinsam im Gespräch, oder die dritte Person?
3. **Pilotgröße** und Alans Zeitbudget (bestimmt, ob N ≈ 500 realistisch ist).
4. **Kontextausschnitt:** Wie viele Verse bzw. Zeilen standardmäßig, wie viele erweitert? Werktitel zeigen?
5. **Ausschlussliste der LLM-berührten Tokens** bauen (Abschnitt 3, Punkt 1).
6. **Korpusstand fürs Einfrieren:** vorher mit dem Upstream-`main` abgleichen, dann Commit festlegen.
7. **Leistungsanalyse** für den gepaarten Vergleich neu rechnen, sobald die Silber-Aufteilung feststeht.
8. **Obergattungsgruppen** festlegen (philologische Entscheidung), inklusive Regel für Texte mit mehreren Gattungen und Gattung für TRO.
9. **Datierung und Vers/Prosa:** Sollen sie als weitere Ausgleichsmerkmale dienen? Dann braucht es eine manuelle Zuordnung pro Text (z. B. Jahrhundert über den Handschriftencensus, bei 323 Werken verlinkt).
10. **Obergrenze an Tokens pro Text.**
11. **Schwelle für das Ende des Pilots** (Vorschlag α ≥ 0,80, Untergrenze 0,67) vor dem Pilot festlegen.
12. **Grobe Ebene des Begriffssystems** für die Zwei-Ebenen-Auswertung festlegen (welche Oberbegriffsstufe).
