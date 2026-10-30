# WSD-Goldstandard: Protokoll v2

**Status:** Entwurf vom 2026-10-08 (Stand 2026-10-30: Abschnitte 3, 4.2, 4.10, 9.2 und Abweichungslog A15 bis A18 ergänzt), noch nicht eingefroren.
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

**Was über Silber bekannt ist:** Hinkelmanns & Zeppezauer-Wachauer (2023, S. 180) schreiben,
linguistische Annotationen (Beispiele dort: POS, Phrasen- und Satzstrukturen) sollten künftig
„im Stand-Off-Verfahren mit Linked Open Data (LOD) auf die Tokens der Texte bezogen [werden] und
nicht wie bisher auf die graphematischen Types im Wortartikel“. Von Bedeutungen ist an dieser
Stelle nicht die Rede; dass auch die Senses an graphematischen Typen hingen, ist eine **Lesart**,
gestützt durch die Typlisten an `<sense>` (`knowledge/data.md`, B1). Prüfstatus ✔: Original am
2026-10-23 gelesen (`literatur/pdf/Hinkelmanns-Zeppezauer-Wachauer-2023-MHDBDB-Projektbericht.pdf`,
PDF-Seite 4 = gedruckte S. 180). Das Korpus zeigt aber
mehr als reine Typ-Annotation. Gemessen am 2026-10-08 über alle Silber-Tokens polysemer
Lemmata (444.428 mit `corresp`): Bei 25,0 % der 29.677 Kombinationen aus Lemma und Typ tragen
Tokens derselben Wortform verschiedene Senses. Nur bei 34,1 % der Tokens ist der Sense durch den
Typ eindeutig festgelegt (darin auch Typen mit nur einem Beleg). Der Mehrheitssense des Typs
trifft 85,7 %. Silber ist also zumindest teilweise pro Beleg entschieden; wie, bleibt undokumentiert.

Hinweis zur Benennung: Das Sense-Attribut im Korpus heißt `@ana`, nicht mehr `@meaningRef`
wie in der Präregistrierung und in `.agent/workflows/sense-disambiguator.md`.

## 3. Grundgesamtheit und Ausschlüsse

**Grundgesamtheit:** alle `<w>` mit `@lemmaRef` auf ein Lemma mit mindestens zwei Senses im
Inventar, deren **Wortart** NOM, VRB oder ADJ ist (VEX und VEM zählen als VRB). Die Wortart wird
so bestimmt (entschieden am 2026-10-16):

1. aus `lexicon.xml`, wenn das Lemma dort genau eine Wortart hat;
2. sonst aus dem `@pos` des Tokens, wenn es genau eine Wortart nennt;
3. sonst ist das Token nicht in der Grundgesamtheit.

Ohne Schritt 2 fielen 3.654 polyseme Lemmata mit 920.011 Tokens heraus, darunter zentrale
Wörter wie *guot*: mehr als die ganze übrige Zielmenge. Ein Lemma kann so in mehreren Wortarten
vorkommen; Einheit der Schichtung ist daher das Paar aus Lemma und Wortart. Gemessen am
2026-10-16 (ohne WZB, Ausschlussliste vom 2026-10-08): 930.645 Tokens über Schritt 1, 503.625 über
Schritt 2, zusammen **1.434.270 Tokens** in 5.132 Paaren aus Lemma und Wortart (4.797 Lemmata);
409.893 Tokens bleiben wegen mehrdeutigem Token-`@pos` draußen. Präpositionen und Adverbien sind
bewusst nicht enthalten: Ihre Senses sind in der MHDBDB funktional-grammatisch (z. B. *in* mit
drei Senses), eine andere Aufgabe als lexikalische WSD, und sie fehlen auch in den
Vergleichsdatensätzen. Polyseme PRP-Lemmata mit eindeutiger Lexikon-Wortart: 6 Lemmata, 53.333
Tokens; ADV: 94 Lemmata, 29.475 Tokens.

**Silber ist eine Eigenschaft des Textes, nicht des Tokens.** In teilweise annotierten Texten
tragen die monosemen Tokens `@ana`, die polysemen nicht (Beispiel ABG: alle 2.251 monosemen
lemmatisierten Tokens mit `@ana`, keines der 745 polysemen). Über die Zieltokens gerechnet ist
die Verteilung zweigipflig: 345 Texte haben weniger als 10 % Silber, 203 Texte mindestens 90 %,
dazwischen fast keine (gemessen am 2026-10-16). Deshalb gibt es statt einer Token-Schicht zwei
**Domänen**:

- **D1, durchannotiert:** Texte, in denen mindestens 90 % der Zieltokens `@ana` tragen
  (203 Texte, 140.480 Zieltokens, ca. 10 %).
- **D0, übrige Texte** (463 Texte, 1.293.790 Zieltokens). Das ist der Korpusteil, für den WSD
  gebraucht wird.

Folgen, die in jede Auswertung gehören: Die gemessene Silberqualität ist die Qualität der
Annotationskampagne dieser 203 Texte, nichts darüber hinaus. Unterschiede zwischen D1 und D0 sind
mit Text und Gattung vermischt und werden nicht als Silber-Effekt gedeutet. Die MFS-Baseline wird
aus Silber gelernt, also im Wesentlichen aus D1, und auf D0 angewandt; diese Verschiebung ist
realistisch, wird aber benannt.

**Ausschlüsse** (jeder Ausschluss wird mit Anzahl im Datasheet dokumentiert):

1. **Tokens, deren Annotation nach der Migration verändert wurde** (bestätigt von Julia am
   2026-10-16). Jedes Token wird mit seinem Zustand im Commit `0422429fc` (2025-07-23, Stand nach
   der Migration, 666 Texte) verglichen. Das Sense-Attribut hieß dort `@meaningRef` und wurde am
   2026-04-09 in `@ana` umbenannt (#32); verglichen wird der Inhalt, nicht der Attributname.
   Werkzeug: [`ausschluss_nachmigration.py`](ausschluss_nachmigration.py).
   - **Ausgeschlossen** wird ein Token mit `@lemmaRef`, wenn es in einem nach der Baseline
     ingestierten Text liegt (WZB, ganz), wenn seine `xml:id` in der Baseline fehlt, oder wenn sich
     `@lemmaRef` oder der Sense geändert hat.
   - **Nur markiert, nicht ausgeschlossen** wird ein Token, bei dem sich ausschließlich `@pos`
     geändert hat. Lemma und Sense sind dann unverändert, die Annotator:innen sehen `@pos` nicht,
     und die Wortart für die Schichtung kommt aus `lexicon.xml`. Ein Ausschluss würde zudem
     gezielt die Fachliteratur treffen, die Abschnitt 4 anheben will. Einschränkung: Bei Lemmata
     mit mehrdeutiger Lexikon-Wortart kommt die Wortart aus dem Token (oben, Schritt 2), bei
     markierten Tokens also aus dem POS-Abgleich von #32. Die Markierung bleibt deshalb im Manifest,
     und eine Sensitivitätsanalyse wiederholt die Hauptauswertung ohne markierte Tokens.
   - `@corresp` wird nicht verglichen: Es verknüpft nur den Variantentyp.
   - **Warum ein Git-Vergleich und keine Ingest-Logs:** Die Läufe (#189, #198, #216, #369, #387 u. a.)
     mischen regelbasierte Schritte, LLM-Entscheidungen und Einzelentscheidungen von KZW, und nicht
     jeder führt eine Token-Liste. Der Vergleich erfasst jede Änderung, auch ungeloggte; die Listen
     in `ingest/pos-disambig/*/` dienen nur der Herkunftsangabe.
   - **Stand 2026-10-08** (Commit `f6fbebf`, 7.545.732 lemmatisierte Tokens): 157.459 ausgeschlossen,
     davon 142.330 aus WZB und 15.129 mit geändertem Lemma oder Sense (15.110 davon durch eine
     Ingest-Liste gedeckt, 19 aus Läufen ohne Token-Liste). 34.336 nur markiert, überwiegend aus dem
     POS-Abgleich von #32 (Commit `82c90dd85`: ADP, AC1 bis AC3, FLG, ABG, ABS, AGS). Beim Einfrieren
     wird das Skript auf dem dann gültigen Korpusstand erneut ausgeführt.
   - Die Token-Liste wird nicht ins Repo gelegt; sie ist aus Skript und Commits reproduzierbar.
     Ins Manifest geht nur `zusammenfassung.json` mit Zählungen und Commits.
2. Lemmata, bei denen zwei Senses dieselbe Begriffsgruppe haben. Diese Senses sind für niemanden
   unterscheidbar. Gemessen am 2026-10-08: 22 Lemmata.
3. Lemmata mit mindestens einem Sense ohne Begriffszeiger. Er ließe sich nicht darstellen.
   Gemessen am 2026-10-08: 126 Senses ohne Zeiger (Anzahl der betroffenen Lemmata noch zu zählen).
4. Lemmata mit disjunkten Token-`@pos`-Werten (Verdacht auf Lemmatisierungsfehler), wie in
   `goldstandard-test.py`. In der Teilmenge der 190 vollständig annotierten Texte: 763 Lemmata.
   **Vorläufig:** Ein Wortartwechsel zwischen Lemma und Beleg kann gewollt sein, etwa beim
   substantivierten Infinitiv oder substantivierten Adjektiv. ReM führt nominalisierte Infinitive
   als `NA` mit Lemma-Wortart `VVINF` (Ganslmayer & Schwarz 2021, S. 164), und HiTS wertet die
   Abweichung zwischen Lemma- und Beleg-Wortart als Information, nicht als Fehler (Dipper et al.
   2013, S. 92 bis 95). Vor Freeze 1 wird an einer Stichprobe der betroffenen Lemmata geprüft, wie
   viele davon echte Lemmatisierungsfehler sind; bis dahin gilt der Ausschluss als vorläufig.
   Größe und Auswahlregel der Stichprobe sind offen (Abschnitt 12, Punkt 13).

## 4. Stichprobendesign

Festgelegt am 2026-10-16 nach einer Literaturrecherche ([LITERATUR-STICHPROBE.md](LITERATUR-STICHPROBE.md))
und einer skeptischen Zweitmeinung. Zahlen sind vorläufig: gemessen auf dem Korpusstand vom
2026-10-16 mit der Ausschlussliste vom 2026-10-08; beim Einfrieren wird neu gemessen.

### 4.1 Schätzziele

- **Primär:** die gepaarte Differenz der Genauigkeit LLM minus MFS-Baseline, **ungewichtet** über
  die Hauptstichprobe (Abschnitt 9.2). Das Schätzziel lautet damit: Genauigkeit über die Vielfalt
  polysemer Lemmata, nicht über die Tokenmasse des Korpus.
- **Sekundär:** Inter-Annotator-Agreement (alle Komponenten), Silberqualität (nur D1),
  Schwierigkeitsfaktoren (gemischtes Modell, 4.6), korpusgewichtete Genauigkeit.
- Begründung: Mehrere Ziele werden offen benannt, eines wird primär gesetzt (Kish 1988). Eine
  korpusgewichtete Zahl hinge fast ganz am obersten Frequenzband, das 92,6 % der Zieltokens trägt;
  sie wird nur mit effektiver Stichprobengröße n_eff = n / (1 + CV² der Gewichte) berichtet.

### 4.2 Komponenten

| Komponente | Umfang | Zweck |
|---|---|---|
| Hauptstichprobe | 36 Zellen × 10 = 360 Items, 1 Token pro Paar aus Lemma und Wortart | primäres Schätzziel, Agreement, Schwierigkeitsfaktoren |
| Lemma-Panel | 30 Paare aus Lemma und Wortart × 5 Tokens = 150 Items | Lemma- gegen Kontextschwierigkeit, Sense-Abdeckung und Silberqualität pro Lemma |
| Pilot-Pool | ca. 100 Items, Lemmata disjunkt zu Haupt- und Panelstichprobe | Pilotrunden (Abschnitt 7), Schätzung des Anteils diskordanter Paare, Entwicklung der LLM-Konfiguration (siehe unten) |

Zusammen ca. 510 Items für die Hauptrunde. Die Panel-Lemmata kommen in der Hauptstichprobe nicht
vor. Pilot-Lemmata sind disjunkt, damit Besprechungen im Pilot nicht auf dieselben Lemmata in der
Hauptrunde durchschlagen.

**Entwicklungsdaten für das LLM:** Prompt-Wortlaut, Antwortformat, Few-shot-Beispiele (Anzahl und
Herkunft) und jeder Formatvergleich werden nur am Pilot-Pool gewählt, nie an der Haupt- oder
Panelstichprobe. Few-shot-Beispiele aus Silber enthalten keine Tokens der Stichproben. Wirkungen
von Prompt-Überarbeitungen werden nur an Items berichtet, die beim Überarbeiten nicht gesehen
wurden. Der Artikel sagt das ausdrücklich. Begründung: Die Prompt-Formulierung verschiebt die
Werte im Mittel um etwa 5 Punkte zwischen bestem und schlechtestem Prompt, und Meconi et al.
(2025, S. 33900) wählen den Prompt an einer eigenen Entwicklungsmenge, nicht an den Testdaten.

### 4.3 Zellen der Hauptstichprobe

36 Zellen = **Polysemie** × **Wortart** × **Frequenzband**:

- **Polysemie** = Zahl der Senses im Inventar: 2 / 3 / 4+ (4+ reicht bis 15, Median 5). Inventar
  statt Belegung, weil die Menügröße für alle Lemmata beobachtbar ist, auch ohne Silber, und das
  ist, was Mensch und LLM sehen. Die Zahl der im Silber belegten Senses, der MFS-Anteil und die
  Sense-Entropie werden pro Item im Manifest mitgeführt, als Kovariaten (Loureiro et al. 2021 und
  Passonneau et al. 2010 finden die Schiefe aussagekräftiger als die Sense-Zahl). Geschichtet wird
  nicht nach ihnen, weil sie aus Silber stammen, dessen Qualität selbst gemessen werden soll.
- **Wortart:** NOM / VRB / ADJ nach der Regel in Abschnitt 3.
- **Frequenzband** = Belege des Paars aus Lemma und Wortart in der Grundgesamtheit, feste Grenzen
  **1–3 / 4–20 / 21–200 / >200** (entschieden am 2026-10-16). Feste Bänder verschieben sich beim
  Neuzählen nicht, und anders als Quartile über Lemma-Typen trennen sie Wörter mit 62 von solchen mit
  100.000 Belegen.

Besetzung am 2026-10-16: Jede Zelle hat mindestens 16 Paare (kleinste: 3 ADJ >200 mit 16,
3 ADJ 1–3 mit 95), also reicht 1 Token pro Paar überall für 10 Items.

### 4.4 Ziehung

1. **Domänenquote:** 30 % der Hauptstichprobe aus D1 (entschieden am 2026-10-16), also 3 von 10 Items
   pro Zelle. Hat eine Zelle zu wenige Paare mit Belegen in D1 (vor allem in den Bändern 1–3 und
   4–20), wird der Fehlbetrag auf Zellen derselben Wortart mit Überschuss verteilt. Erreichte
   Anteile pro Zelle stehen im Manifest. Mit ca. 150 D1-Items (Haupt und Panel) ist die
   Silberqualität auf etwa ±7 Prozentpunkte bestimmbar.
2. **Stufe 1, Paar:** pro Zelle und Domäne werden Paare aus Lemma und Wortart ohne Zurücklegen
   gleich wahrscheinlich gezogen.
3. **Stufe 2, Token:** vom gezogenen Paar wird ein Token der jeweiligen Domäne gezogen, gewichtet
   für den **Gattungsausgleich**: Jedes Token erhält das Gewicht T_G^(−1/2), wobei T_G der
   Tokenanteil seiner Obergattungsgruppe in der Grundgesamtheit ist. Damit nähert sich der Anteil
   der Gruppen der Quadratwurzel-Allokation (Potenzallokation mit q = 0,5; Bankier 1988): Lyrik und
   Fachliteratur werden angehoben, ohne die Großepik zu verdrängen.
4. **Obergrenze pro Text:** höchstens 3 Items aus einem Text über alle Komponenten (bestätigt am 2026-10-16). Ist die Grenze
   erreicht, wird in Stufe 2 neu gezogen. Die Grenze hält den Klumpeneffekt klein (Gale, Church & Yarowsky 1992; All-Words-Sets als
   Klumpenstichproben, Raganato et al. 2017). Ein Vorbild im ReM gibt es dafür nicht: Das
   Handbuch (Klein & Dipper 2016, S. 4) kennt für eReM nur eine Untergrenze von 20.000 Tokens
   bei einigen Großtexten; nach 50-Jahres-Abschnitten, Sprachräumen und Textart strukturiert
   ist MiGraKo (S. 3), nicht eReM (S. 5).
5. **Inklusionswahrscheinlichkeiten** jeder Ziehung werden mitgeschrieben; daraus entstehen die
   Gewichte für die sekundäre, korpusgewichtete Auswertung und für die Rückgewichtung der Domänen.
6. **Fester Seed**, im Manifest. Ziehungsskript, Gattungstabelle und Parameter werden mit eingefroren.

### 4.5 Lemma-Panel

- 30 Paare aus Lemma und Wortart aus den Bändern 21–200 und >200, 10 pro Wortart, innerhalb der
  Wortart 3 / 3 / 4 auf die Polysemiestufen 2 / 3 / 4+.
- Voraussetzung: Belege in mindestens 5 verschiedenen Texten. Pro Paar 5 Tokens aus 5 verschiedenen
  Texten, davon mindestens 2 aus D1, wo vorhanden (für die Silberqualität pro Lemma).
- Ausgewertet mit Bootstrap nach Lemma. Das Panel ist eine eigene Komponente und geht nicht in das
  primäre Schätzziel ein.

### 4.6 Was die Zellen leisten und was nicht

Mit 10 Items pro Zelle ist ein Zellwert auf etwa ±25 Prozentpunkte unsicher: Zellen sind
Berichts-, keine Testeinheiten. Schwierigkeitsfaktoren werden mit **einem** gemischten logistischen
Modell über alle Items geschätzt (Polysemie, Wortart, Frequenzband, Domäne als feste Effekte;
Text und, im Panel, Lemma als Zufallseffekte). Die ausgewogene Besetzung hält die Prädiktoren
nahezu unabhängig voneinander; das ist ihr eigentlicher Zweck.

### 4.7 Teststärke

Für den gepaarten Vergleich (McNemar; Connor 1987) mit α = 0,05 und Power 0,80 ist die kleinste
nachweisbare Differenz bei 360 Items etwa 5,8 / 7,5 / 8,8 Prozentpunkte, wenn 15 / 25 / 35 % der
Items diskordant sind (eine Methode richtig, die andere falsch). Bei 500 Items wären es 4,8 / 6,2 /
7,4. Je Wortart (ca. 120 Items) sind nur Unterschiede um 10 Punkte und mehr nachweisbar. Der Pilot
schätzt den Anteil diskordanter Paare (Card et al. 2020); liegt er hoch, wird N vor Freeze 2 erhöht.

### 4.8 Gattungsausgleich: Befund und Gattungstabelle

Befund vom 2026-10-08 (alle 667 Texte, 7.545.732 lemmatisierte Tokens):

- Wenige große Texte dominieren: OVG allein 4,6 %, die zehn größten zusammen rund 26 %.
- Lyrik umfasst 485 Texte, aber nur 3,6 % der Tokens; Fachliteratur liegt bei rund 0,4 %.
- Die Gattungsangaben folgen der MHDBDB-Textreihentypologie (`genres.xml`, 615 Kategorien,
  polyhierarchisch): zwei Wurzeln, 12 Kategorien auf Ebene 1, bis zu 6 Ebenen. Jeder Text trägt im
  Header zu jeder Textreihe eine eindeutige Herkunft (`ana="parent"`). Korrektur vom 2026-10-16:
  Die frühere Angabe, die Taxonomie sei flach und TRO habe keine Gattung, war falsch
  (Einzelheiten in [OBERGATTUNGEN.md](OBERGATTUNGEN.md)).
- Datierung und Vers/Prosa liegen nicht maschinenlesbar vor (#118; WZB ist Prosa, steht aber in `<l>`).

Die **Obergattungsgruppen** sind die Ebene 1 der Textreihentypologie, zusammengelegt, wo das Korpus
zu dünn ist; Zuordnung über die Herkunft im Header, bei mehreren Gruppen Vorrang der Inhaltsbereiche
vor den Formen. Entwurf zur Prüfung: [OBERGATTUNGEN.md](OBERGATTUNGEN.md). Die Tabelle steuert die
Gewichte in 4.4 und muss deshalb vor Freeze 1 stehen.

### 4.9 Manifest pro Item

Item-ID, `xml:id`, Datei, Komponente, Zelle, Lemma, Wortart und ihre Herkunft (Lexikon oder Token),
Zahl der Senses (Inventar und im Silber belegt), MFS-Anteil und Entropie im Silber (Leave-out),
Frequenz und Band, Domäne, Obergattungsgruppe, Markierung „nur `@pos` geändert",
Inklusionswahrscheinlichkeit.

### 4.10 Zwei Einfrierpunkte

- **Freeze 1, vor der Ziehung:** Grundgesamtheit und Ausschlüsse mit Zahlen, Wortartregel, Zellen,
  Bänder, Domänenquote, Panel-Regeln, Gattungstabelle, Obergrenze pro Text, Seed, Korpus-Commit.
- **Freeze 2, vor der Hauptrunde:** Richtlinien, Pilotschwelle, Agreement-Maße, Bewertungsregeln
  (Abschnitt 9.2), MFS-Definition, LLM-Konfiguration (Modell und Version, Prompt, Temperatur,
  Anzahl der Läufe pro Item, ob das LLM dieselben Karten sieht wie die Menschen), endgültiges N.
  Bei mehreren Läufen pro Item wird in Freeze 2 festgelegt, was als LLM-Vorhersage gilt: ein
  vorab bestimmter Lauf, die Mehrheit mit Gleichstandsregel oder die Verteilung (welche, entscheidet
  Julia in Freeze 2). Die Übereinstimmung zwischen den Läufen wird als eigenes Ergebnis berichtet
  (Mittelwert und Streuung). Begründung: Eine Mehrheit über mehrere Läufe ist selbst ein Ensemble
  (Chen et al. 2025, S. 5), und der McNemar-Test verglich dann ein Ensemble mit einer
  Einzelbaseline. Vorlagen gehen auseinander: mindestens fünf Läufe bei Temperatur 0,7 mit
  Konsistenz als Konfidenz (Pangakis & Wolken 2025, S. 1474 Fn. 12, S. 1475) gegen greedy decoding
  mit einem Lauf (Basile et al. 2025, S. 5). „Deterministisch bei Temperatur 0“ ist eine
  Behauptung, keine Zusage (Campesato 2024, S. 218).

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
6. **Aufschlüsselung** nach Polysemiegrad, Wortart, Frequenzband, Domäne, Obergattungsgruppe und
   angegebener Sicherheit, jeweils mit Intervall.
7. **Zwei Ebenen des Begriffssystems:** zusätzlich die Übereinstimmung, wenn jeder Sense auf die
   Oberbegriffe seiner Begriffe abgebildet wird. Die Granularität ist der stärkste bekannte
   Einflussfaktor auf WSD-Übereinstimmung (Ng et al. 1999; Hovy et al. 2006). Das grobe Maß wird
   vorab definiert, nicht nachträglich durch Zusammenlegen gewonnen (Artstein & Poesio 2008).

### 9.2 Gold, Silber, LLM

- **Jede:r gegen das Gold:** Übereinstimmung jeder Annotator:in mit dem adjudizierten Gold, dazu die
  Adjudikationsstatistik nach Ursachencode. Hohe Roh-IAA sagt nichts über die Qualität des
  adjudizierten Golds (Passonneau & Carpenter 2014).
- **Silberqualität:** Genauigkeit von Silber-`@ana` gegen Gold, nur Domäne D1 (Abschnitt 3), mit dem Vorbehalt, dass sie nur die Annotationskampagne dieser Texte beschreibt.
- **LLM gegen Baseline:** Genauigkeit gegen Gold. Die MFS-Baseline wird aus Silber gelernt,
  **ohne** die Stichproben-Tokens, und auf denselben Gold-Items gemessen. Damit ist der Vergleich
  gepaart (McNemar-Test) statt gegen einen festen Wert.
  - **Rückfall:** Hat ein Lemma nach dem Leave-out kein Silber, gilt der erste Sense in
    `lexicon.xml`. Der Anteil der Rückfall-Items wird berichtet; die Untergruppe „MFS aus Silber"
    wird sekundär ausgewertet. Der Test läuft über alle Items.
  - **Bewertungsregeln (vor Freeze 2 festgeschrieben):** Primäre Auswertungsmenge sind Items mit
    Gold-Status `SENSE` oder `MEHRERE`. Bei `MEHRERE` zählt eine Vorhersage als richtig, wenn sie
    einer der Gold-Senses ist. Items mit `KEINE_PASST`, `LEMMA_FALSCH`, `KONTEXT_UNZUREICHEND` oder
    `TEXT_DEFEKT` gehen nicht in die Genauigkeit ein; wie oft das LLM bei ihnen abstiniert oder
    trotzdem einen Sense wählt, wird gesondert berichtet.
  - **Ungültige LLM-Antworten:** unparsbar, Sense-ID außerhalb des Menüs, ID eines anderen
    Lemmas oder mehrere IDs bei `SENSE`. Sie werden als eigene Kategorie gezählt und berichtet und
    im primären gepaarten Vergleich als falsch gewertet; ein Ausschluss bräche die Paarung, weil MFS
    nie ungültig antwortet. Das LLM antwortet mit Kartennummer oder Sense-ID; die Sense-ID wird
    direkt aus der Nummer abgeleitet, nicht über Textabgleich (der Textabgleich bei Meconi et al.
    2025, S. 33898 bis 33899, ist bei kurzen, ähnlichen Begriffsnamen unsicher). Strutz (2026,
    S. 4 bis 6, 16) setzt Wohlgeformtheit ebenfalls als Tor vor die inhaltliche Bewertung. Eine
    gültige Ausweichantwort (Abstinenz) ist keine ungültige Antwort und fällt nicht hierunter.
  - **Einwand gegen die `MEHRERE`-Regel und Sensitivität:** Die Primärregel entspricht Henrichs
    Option (iii), „to score a system already as correct if it assigns only one of the multiple
    senses“. Henrich verwirft sie, weil sie „slightly higher evaluation results than would be
    genuinely correct“ erbrächte, und hält Teilwertung (Option i) für fairer (Henrich 2015,
    S. 151 bis 152). Die präregistrierte Primärregel bleibt stabil; zusätzlich werden zwei
    Sensitivitätsauswertungen berichtet: (a) Teilwertung mit dem Dice-Koeffizienten zwischen der
    Menge der Gold-Senses G und der vorhergesagten Menge (bei genau einem vorhergesagten Sense
    2/(|G|+1) bei Treffer, sonst 0; Henrich nutzt Dice nach Véronis 1998); (b) Genauigkeit ohne
    die `MEHRERE`-Items (Henrichs Option ii). Beides gilt für LLM und MFS-Baseline gleichermaßen,
    damit der gepaarte Vergleich gepaart bleibt. Der Anteil der `MEHRERE`-Items an der
    Auswertungsmenge wird berichtet.
  - Zusätzlich Macro-Genauigkeit nach Sense und die Genauigkeit auf Nicht-MFS-Items, weil dort die
    harten Fälle liegen (Maru et al. 2022).
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
| Ziehungsskript, Ausschlussskript, `ausschluss/zusammenfassung.json` | dieses Verzeichnis | ja |
| Token-Liste der Ausschlüsse (`ausschluss/ausschluss-tokens.csv`) | nur lokal, reproduzierbar | nein |
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
| A3 | 6 Zellen mit je ≥ 50 | Hauptstichprobe 36 Zellen × 10 (Polysemie × Wortart × feste Frequenzbänder), 1 Token pro Paar aus Lemma und Wortart; dazu Lemma-Panel 30 × 5 und Pilot-Pool | Frequenz als Schwierigkeitsfaktor (Kilgarriff 1998); Panel trennt Lemma- von Kontextschwierigkeit; Inferenz über ein gemischtes Modell | 2026-10-08, geändert 2026-10-16 |
| A4 | feste Baseline 66,7 %, einseitiger Binomialtest | MFS aus Silber ohne Stichprobe, gepaart auf denselben Items (McNemar) | Feste Baseline ist in-sample und auf anderer Population gerechnet | 2026-10-08 |
| A5 | Julia blind gegen LLM und Gold | zwei menschliche Annotator:innen (Julia, Alan van Beek) und Adjudikation | Gold braucht gemessene Übereinstimmung zwischen Menschen | 2026-10-08 |
| A6 | Sense-Wahl, LLM darf `abstain` | Statusliste mit Ausweichlabels und `MEHRERE` | Das Inventar passt nicht immer; erzwungene Wahl brächte Fehlzuordnungen ins Gold | 2026-10-08 |
| A7 | keine Gattungsbalance | weiche Gattungsquote mit Quadratwurzel-Allokation, Obergrenze pro Text | Überlieferungsbedingter Bias des Korpus soll im Goldstandard abgemildert werden | 2026-10-08 |
| A8 | Cohen's κ zwischen LLM und Julia | α mit MASI als Hauptmaß, Statusebene getrennt, Bootstrap-Intervalle nach Text, AC1 als Kontrolle | WSD-spezifische Literatur (Artstein & Poesio 2008; Passonneau 2006) und starke Prävalenz | 2026-10-08 |
| A9 | Wortart laut Lexikon | Lexikon-Wortart, sonst eindeutiges Token-`@pos` | Ohne Rückfall fielen 920.011 Tokens mit mehrdeutiger Lexikon-Wortart heraus | 2026-10-16 |
| A10 | Schicht Silber ja/nein pro Token | Domänen D1 (durchannotierte Texte) und D0, D1 mit fester Quote von 30 % | Silber ist eine Texteigenschaft (zweigipflige Verteilung) | 2026-10-16 |
| A11 | Hypothese gegen festen Wert | primäres Schätzziel: ungewichtete gepaarte Differenz LLM minus MFS, Bewertungsregeln für `MEHRERE` und Ausweichlabels | Mehrere Ziele, eines primär (Kish 1988); gewichtete Zahl hätte kleine n_eff | 2026-10-16 |
| A12 | (keine Abweichung vom Design) Quellenangabe in Abschnitt 2 | Quellenangabe zu Hinkelmanns & Zeppezauer-Wachauer (2023) berichtigt: gedruckte S. 180, wörtliches Zitat, Übertragung auf Bedeutungen als Lesart gekennzeichnet; Prüfstatus ○ → ✔ | Vorher stand dort, die Quelle belege die Anbindung von Bedeutungen an Typen; im Original steht nur „linguistische Annotationen“ (POS, Phrasen- und Satzstrukturen). Entscheidung Julia Hintersteiner, 2026-10-23 | 2026-10-23 |
| A13 | (keine Abweichung von der Regel) Begründung der Obergrenze pro Text (Abschnitt 4.4, Punkt 4): „Vorbild: ReM nimmt große Texte nur in Ausschnitten auf“ | Begründung nur über den Klumpeneffekt; ReM nicht mehr als Vorbild genannt. Regel unverändert (3 Items pro Text) | Falsch gelesen: Die 20.000 Tokens sind in eReM eine Untergrenze für einige Großtexte (Klein & Dipper 2016, S. 4); das Raster aus 50-Jahres-Abschnitten, Sprachräumen und Textart gilt für MiGraKo (S. 3), eReM ist „kein strukturiertes Korpus“ (S. 5); eine Obergrenze pro Text formuliert das Handbuch nicht. Entscheidung Julia Hintersteiner, 2026-10-28. Gleiche Korrektur in LITERATUR-STICHPROBE.md | 2026-10-28 |
| A14 | Bewertungsregel bei `MEHRERE` (Abschnitt 9.2): „richtig, wenn einer der Gold-Senses getroffen“ | Regel unverändert; zwei Sensitivitätsauswertungen ergänzt: Teilwertung mit Dice-Koeffizient und Genauigkeit ohne `MEHRERE`-Items, jeweils für LLM und MFS; Anteil der `MEHRERE`-Items wird berichtet | Henrich (2015, S. 151 bis 152) verwirft diese Regel (Option iii), weil sie die Ergebnisse leicht überschätze, und hält Teilwertung für fairer. Präregistrierte Primärregel bleibt stabil, der Einwand wird beantwortet statt übergangen. Entscheidung Julia Hintersteiner, 2026-10-28 | 2026-10-28 |
| A15 | Ausschluss 4 (Abschnitt 3): Lemmata mit disjunkten Token-`@pos`-Werten werden als „Verdacht auf Lemmatisierungsfehler“ ausgeschlossen | Ausschluss gilt als vorläufig; Begründung ergänzt, dass Wortartwechsel gewollt sein können (substantivierter Infinitiv, substantiviertes Adjektiv); vor Freeze 1 Stichprobe der betroffenen Lemmata auf echte Lemmatisierungsfehler; verknüpft mit offenem Punkt 13 | ReM führt nominalisierte Infinitive als `NA` mit `VVINF` als Lemma-Wortart (Ganslmayer & Schwarz 2021, S. 164), HiTS wertet die Abweichung als Information (Dipper et al. 2013, S. 92 bis 95). Vorschlag V5 aus der Literaturauswertung vom 2026-10-30; Belege aus nicht gegengelesenen KI-Zusammenfassungen. Entscheidung Julia Hintersteiner, 2026-10-30. Größe und Regel der Stichprobe offen | 2026-10-30 |
| A16 | Mehrere Läufe pro Item (Abschnitt 4.10): im Protokoll nur „Anzahl der Läufe pro Item“ | Freeze 2 legt fest, was als LLM-Vorhersage gilt (vorab bestimmter Lauf, Mehrheit mit Gleichstandsregel oder Verteilung); Übereinstimmung zwischen den Läufen wird als eigenes Ergebnis berichtet (Mittelwert, Streuung) | Mehrheit ist ein Ensemble, McNemar verglich sonst Ensemble gegen Einzelbaseline; Temperatur 0 ist keine Zusage für Determinismus (Chen et al. 2025, S. 5; Pangakis & Wolken 2025, S. 1474 Fn. 12, S. 1475; Basile et al. 2025, S. 5; Campesato 2024, S. 218). Vorschlag V9 aus der Literaturauswertung vom 2026-10-30. Entscheidung Julia Hintersteiner, 2026-10-30; welche Aggregationsregel gilt, entscheidet sie in Freeze 2 | 2026-10-30 |
| A17 | Zweck des Pilot-Pools (Abschnitt 4.2): Pilotrunden, Schätzung diskordanter Paare | Zweck erweitert: Prompt-Wortlaut, Antwortformat, Few-shot-Beispiele und Formatvergleiche nur am Pilot-Pool gewählt; Few-shot-Beispiele aus Silber ohne Stichproben-Tokens; Wirkungen von Prompt-Überarbeitungen nur an ungesehenen Items berichtet | Trennung von Entwicklungs- und Testdaten; Prompt-Formulierung streut im Mittel um etwa 5 Punkte (Meconi et al. 2025, S. 33900). Vorschlag V10 aus der Literaturauswertung vom 2026-10-30. Entscheidung Julia Hintersteiner, 2026-10-30 | 2026-10-30 |
| A18 | Bewertungsregeln (Abschnitt 9.2): ungültige LLM-Antworten nicht geregelt | Ungültige Antworten (unparsbar, ID außerhalb des Menüs, ID eines anderen Lemmas, mehrere IDs bei `SENSE`) als eigene Kategorie berichtet, im primären gepaarten Vergleich als falsch gewertet; Antwort als Kartennummer oder Sense-ID, Sense-ID direkt aus der Nummer abgeleitet | Ein Ausschluss bräche die Paarung, weil MFS nie ungültig antwortet; Textabgleich ist bei kurzen, ähnlichen Begriffsnamen unsicher (Strutz 2026, S. 4 bis 6, 16; Meconi et al. 2025, S. 33898 bis 33899). Vorschlag V25 aus der Literaturauswertung vom 2026-10-30. Entscheidung Julia Hintersteiner, 2026-10-30 | 2026-10-30 |

## 12. Offene Punkte

1. ~~Silber-Aufteilung je Zelle~~: entschieden am 2026-10-16, Domäne D1 mit 30 % (Abschnitt 4.4).
2. **Dritte Person** für die Prüfung der Adjudikation (Abschnitt 7, Schritt 6), z. B. KZW?
   Und wer adjudiziert selbst: Julia und Alan gemeinsam im Gespräch, oder die dritte Person?
3. **Pilotgröße** und Alans Zeitbudget (bestimmt, ob ca. 510 Items realistisch sind).
4. **Kontextausschnitt:** Wie viele Verse bzw. Zeilen standardmäßig, wie viele erweitert? Werktitel zeigen?
5. ~~Ausschlussliste der LLM-berührten Tokens bauen~~: erledigt am 2026-10-08, Regel bestätigt am 2026-10-16 (Abschnitt 3, Punkt 1).
6. **Korpusstand fürs Einfrieren:** vorher mit dem Upstream-`main` abgleichen, dann Commit festlegen.
7. **Teststärke:** grob gerechnet (Abschnitt 4.7); Anteil diskordanter Paare im Pilot schätzen, dann N vor Freeze 2 bestätigen.
8. **Obergattungsgruppen** prüfen und festlegen: Entwurf vom 2026-10-16 in [OBERGATTUNGEN.md](OBERGATTUNGEN.md), Abschnitt 5.
9. **Datierung und Vers/Prosa:** Sollen sie als weitere Ausgleichsmerkmale dienen? Dann braucht es eine manuelle Zuordnung pro Text (z. B. Jahrhundert über den Handschriftencensus, bei 323 Werken verlinkt).
10. ~~Obergrenze an Tokens pro Text~~: 3, bestätigt am 2026-10-16 (Abschnitt 4.4).
11. **Schwelle für das Ende des Pilots** (Vorschlag α ≥ 0,80, Untergrenze 0,67) vor dem Pilot festlegen.
12. **Grobe Ebene des Begriffssystems** für die Zwei-Ebenen-Auswertung festlegen (welche Oberbegriffsstufe).
13. **Ausschlüsse 2 bis 4** (Abschnitt 3) auf die neue Wortartregel und das ganze Korpus umrechnen.
14. **Einwilligung von Alan** zu Protokollierung und Veröffentlichung (DMP, Abschnitt 4).
15. **Privates Repository** anlegen und eine zweite Sicherungskopie festlegen (DMP, Abschnitt 3).
