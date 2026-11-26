# WSD-Goldstandard: Protokoll v2

**Status:** Entwurf vom 2026-10-08 (Stand 2026-11-26: Kennzahlen von Runde 0 in Abschnitt 7 Schritt 2, Teilstand in den offenen Punkten 15 und 23; Stand 2026-11-20, dritte Änderung: A42 ergänzt, `LEMMA_FALSCH` auf der Sense-Ebene als eigene Kategorie, Abschnitt 9.1, offener Punkt 25 erledigt; Stand 2026-11-20, zweite Änderung: A41 ergänzt, Widerspruch in Abschnitt 9.1 zur Sense-Ebene aufgelöst, offener Punkt 25 neu; Stand 2026-11-20: A40 ergänzt, offener Punkt 14 und Abschnitt 7 Schritt 7 angepasst; A39 ergänzt, Korpusstand bleibt `a938559dc` trotz Upstream-Merge, Abschnitt 3 und offener Punkt 6 ergänzt; Stand 2026-11-16: A33 bis A38 ergänzt (Entscheidung über `VORSCHLAEGE-2026-11.md`, Teile A und B), Abschnitte 4.2, 4.3, 4.4, 4.10, 6, 7, 9.1, 9.2 und 10 sowie offene Punkte 12, 14, 22 bis 24 geändert; Stand 2026-11-13: A31 und A32 ergänzt, Abschnitt 7 (Stoppregel des Pilots, dritte Person), offene Punkte 2, 3 und 17 teilweise und 11 ganz erledigt (Hilfsmittelregel, Kurzanleitung v0.3); Stand 2026-11-12: Abschnitte 1, 2, 3, 4.2, 4.4, 4.8, 4.9, 4.10, 9.1, 9.2, 12 und Abweichungslog A15 bis A30 ergänzt oder geändert; Korpusstand für den ganzen Goldstandard festgelegt, Pilotdesign vorläufig), noch nicht eingefroren.
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

Nicht Teil dieses Protokolls: Ein Vergleich der LLM-Ergebnisse mit einem Encoder-Modell ist als
späterer, eigener Schritt geplant (Julia Hintersteiner, 2026-10-30). Eine Encoder-Konfiguration wird
hier deshalb nicht festgeschrieben.

## 2. Begriffe

| Begriff | Bedeutung hier |
|---|---|
| **Gold** | Bedeutungszuweisung, die für dieses Protokoll von zwei Annotator:innen unabhängig, blind und unter dokumentierten Richtlinien erhoben und danach adjudiziert wurde. |
| **Silber** | Die bestehende `@ana`-Annotation im Korpus. Sie stammt von Menschen, aber es ist nicht dokumentiert, von wem, wann und nach welchen Richtlinien. Deshalb kann sie nicht als Gold gelten. „Silber" heißt hier also menschlich und undokumentiert, nicht „automatisch annotiert" wie in der Literatur zu Named Entity Recognition und Entity Linking. Ausnahme sind die monosemen Lemmata, deren `@ana` automatisch vergeben ist (`knowledge/data.md`, B2). |
| **Inventar** | Die `<sense>`-Einträge eines Lemmas in `authority-files/lexicon.xml`. Ein Sense ist ausschließlich durch seine Begriffszeiger (`<ptr target="concepts.xml#…">`) bestimmt, die auf das geprüfte Begriffssystem der MHDBDB verweisen. |
| **Begriffsgruppe** | Die Menge der Begriffe, auf die ein Sense zeigt. Sie ist das, was Annotator:innen als „Bedeutung" sehen. |
| **Polysemie** | Zahl der Senses eines Lemmas im Inventar (Abschnitt 4.3), ohne Unterscheidung von Homonymie und Polysemie. Ob die MHDBDB Homographen als eigene Lemmata oder als Senses eines Lemmas führt, ist als Regel nicht gestützt (`knowledge/data.md`, B15). Zur Unterscheidung in der Literatur: Kortmann 2020 (noch nicht beschafft, ungeprüft). |

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
vorkommen; Einheit der Schichtung ist daher das Paar aus Lemma und Wortart. Die Schichtungsvariable
„Wortart" mischt dabei zwei Ebenen: die Lemma-Wortart aus `lexicon.xml` (Schritt 1) und die
Beleg-Wortart des Tokens (Schritt 2). Bei Lemmata wie *guot* kann die Beleg-Wortart von der
Bedeutung abhängen, denn HiTS nennt *guot* mit ‘Besitz’ als Kennzeichen der substantivischen
Lesart (Dipper et al. 2013, S. 92 bis 95, 107; Schiller et al. 1999, S. 12, 24, 57; Belege aus
nicht gegengelesenen KI-Zusammenfassungen). Die Token-Wortart ist dann kein von der Bedeutung
unabhängiges Merkmal, vor allem bei Paaren aus Schritt 2. Die Hauptauswertung wird deshalb auch
nach der Herkunft der Wortart aufgeschlüsselt (Abschnitt 9.1, Punkt 6; A25). Gemessen am
2026-10-16 (ohne WZB, Ausschlussliste vom 2026-10-08): 930.645 Tokens über Schritt 1, 503.625 über
Schritt 2, zusammen **1.434.270 Tokens** in 5.132 Paaren aus Lemma und Wortart (4.797 Lemmata);
409.893 Tokens bleiben wegen mehrdeutigem Token-`@pos` draußen. Diese Zahl enthielt Ausschluss 4
(unten) nie. Ohne den Text SBF (weggelassen, Abschnitt 4.8) sind es 1.434.213 Tokens (Stand
2026-10-30, `obergattungen/zusammenfassung.json`) in weiterhin 5.132 Paaren und 4.797 Lemmata
(nachgemessen am 2026-10-30 mit `verschmelzungen/wirkung.py`, ohne WZB und SBF); die Schritte 1 und 2 sind
seitdem nicht neu gemessen. Ausschluss 5 (unten) ist in diesen Zahlen noch nicht abgezogen. Präpositionen und Adverbien sind
bewusst nicht enthalten: Ihre Senses sind in der MHDBDB funktional-grammatisch (z. B. *in* mit
drei Senses), eine andere Aufgabe als lexikalische WSD. Präpositionen fehlen auch in den
englischen Vergleichsdatensätzen (Raganato et al. 2017, S. 101, Tab. 3); Adverbien sind dort
enthalten (etwa in Senseval-2), diese Stütze gilt also nur für die Präpositionen (Beleg aus einer
nicht gegengelesenen KI-Zusammenfassung; A24). Polyseme PRP-Lemmata mit eindeutiger Lexikon-Wortart: 6 Lemmata, 53.333
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
4. ~~Lemmata mit disjunkten Token-`@pos`-Werten~~: **gestrichen am 2026-10-30** (A19, löst A15
   ab), ersetzt durch eine **Markierung `pos_abweichend`**. Ein Token trägt sie, wenn sein
   `@pos` (VEX und VEM als VRB) keine Überschneidung mit den Wortarten des Lemmas in
   `lexicon.xml` hat. Markierte Tokens bleiben in der Grundgesamtheit und gehen ins Manifest
   (4.9). Echte Lemmatisierungsfehler fängt der Status `LEMMA_FALSCH` beim Annotieren (Abschnitt 6).
   - **Warum nicht ausschließen:** Ein Wortartwechsel zwischen Lemma und Beleg kann gewollt sein,
     etwa beim substantivierten Infinitiv oder Adjektiv. ReM führt nominalisierte Infinitive als
     `NA` mit Lemma-Wortart `VVINF` (Ganslmayer & Schwarz 2021, S. 164), und HiTS wertet die
     Abweichung als Information, nicht als Fehler (Dipper et al. 2013, S. 92 bis 95; beide aus
     nicht gegengelesenen KI-Zusammenfassungen).
   - **Der Ausschluss verzerrte nach Frequenz** (Messung der Hauptsitzung 2026-10-30 über das
     ganze Korpus ohne WZB, Lemmata mit mindestens zwei Senses, Definition aus
     `goldstandard-test.py`, Zeilen 128 bis 135; übernommen, nicht nachgemessen): 277 Lemmata
     mit zusammen 253.147 Tokens. Anteil betroffener Lemmata je Band (Belege 1–3 / 4–20 /
     21–200 / >200): 23 von 3.110 (0,7 %), 80 von 1.927 (4,2 %), 85 von 1.625 (5,2 %), 89 von
     966 (9,2 %). In den Bändern 21–200 und >200 lösten 68 bzw. alle 89 Fälle eine Wortart mit
     weniger als 5 % der Belege aus (Beispiel lemma_5710: 11.900 VRB, 1 NOM). Der Ausschluss
     hätte vor allem häufige Lemmata getroffen.
   - **Größe der Markierung** (Messung der Hauptsitzung, 2026-10-30, Abgrenzung wie in
     `obergattungen_entwurf.py`; übernommen, nicht nachgemessen): 226 von 1.434.213 Tokens
     (0,02 %) aus 118 Lemmata. Die Zahl ist klein, weil die Wortartliste im Lexikon fast jede
     vorkommende Token-Wortart enthält.
   - **Prüfstichprobe:** Statt der Stichprobe von Lemmata aus A15 werden ca. 30 markierte Tokens
     von Hand eingeordnet (Lemmatisierungsfehler, Substantivierung, Tagfehler). Das Ergebnis geht
     ins Datasheet. Auswahlregel (entschieden am 2026-10-30, A22): einfache Zufallsauswahl von 30 aus
     den markierten Tokens mit festem, vorab notiertem Seed (Vorschlag 20261030; der Seed wird bei
     der Ziehung im Skript festgehalten). Die Ziehung ist noch nicht gemacht.

5. **Verschmelzungen** (Klise und Kontraktion wie *sîhez*, *stoufes*, *enwellen*, *zedienest*;
   entschieden am 2026-10-30, A21). Sie tragen im Lexikon das volle Bedeutungsmenü des Grundworts samt
   Typlisten, oft bei einem einzigen Beleg (`knowledge/data.md`, B15). Ausgeschlossen wird auf
   **Lemmaebene**: Alle Tokens eines erfassten Lemmas fallen aus der Grundgesamtheit.
   - **Regel** ([`verschmelzungen.py`](verschmelzungen.py), Docstring maßgeblich): Erkennung über die
     verlinkten Bestandteile in `<etym type="morphological">` des Lexikons. Gründe: P (ein Bestandteil
     ist ein Pronomen), A (ein Bestandteil ist ein Artikel, nicht Numerale), N (Bestandteil
     `niht` und die Form beginnt mit en- oder n-, nicht mit ent-), Z (Bestandteil `zuo` und die Form
     beginnt mit z, nicht mit zuo oder zu, außer zun-), U (Bestandteil `und` und die Form endet auf
     -unde oder -und). Die Verlinkung gilt nur zusammen mit diesen Formbedingungen (siehe
     Einschränkung unten).
   - **Formen auf en-** (Entscheidung Julia Hintersteiner, 2026-10-30, auf die Frage „Wie sollen diese
     en-Formen im Goldstandard behandelt werden?“: „Alle ausschließen (Empf.)“): Die MHDBDB führt
     diese Lemmata selbst mit Wortart NEG. Einige echte ent-Verben gehen dadurch verloren; dafür
     gelangt kein kopiertes Grundwort-Menü in die Stichprobe. Verworfen: Drinlassen (`LEMMA_FALSCH`
     fängt es) und Markieren statt Ausschließen.
   - **Zählung** (`python goldstandard/verschmelzungen.py`, nachgemessen am 2026-10-30, HEAD
     `6d5369e55`): 43.710 Einträge, 3.673 Treffer, davon 1.728 mit mindestens zwei Bedeutungen. Nach
     Grund (mehrere möglich): P 2.009, N 789, A 635, Z 708, U 2. N mit Form auf en-: 776 Einträge, davon
     431 mit mindestens zwei Bedeutungen (Messung der Hauptsitzung, Ad-hoc-Abfrage ohne Skript,
     übernommen, nicht nachgemessen).
   - **Wirkung auf die Grundgesamtheit** (`python goldstandard/verschmelzungen/wirkung.py`,
     nachgemessen am 2026-10-30, Abgrenzung wie `obergattungen_entwurf.py`, ohne WZB und SBF):
     Von 1.434.213 Tokens in 5.132 Paaren und 4.797 Lemmata entfallen 1.788 Tokens (0,12 %) auf 98
     Lemmata (98 Paare); 1.662 Tokens aus 48 Lemmata davon sind en-Formen. Nach Band (Belege in der
     Grundgesamtheit) 1–3 / 4–20 / 21–200 / >200: 79 / 14 / 4 / 1. Das eine Lemma im Band >200 ist
     *enwizzen* mit 1.411 Tokens. Abgeleitet (Subtraktion, nicht gesondert gemessen): Nach Ausschluss 5
     bleiben 1.432.425 Tokens in 5.034 Paaren und 4.699 Lemmata.
   - **Prüfrunde 1** (Seed 20261030, Regel vor dem Nachschärfen; `verschmelzungen/runde1-*`; Urteilszahlen
     aus Schlüssel und Urteilsdatei ausgezählt am 2026-10-30): je 40 Treffer und 40 Nicht-Treffer mit
     Funktionswort unter den Bestandteilen, nur Einträge mit mindestens zwei Bedeutungen, blind
     eingeordnet durch einen Agenten (`quellen`, Lexer über Wörterbuchnetz) als V (Verschmelzung), K
     (keine) oder U (unklar). Treffer: 37 V, 1 K (*entliden*, Präfix ent-), 2 U (*envâhen*,
     *binnendes*). Nicht-Treffer: 3 V (*zungevüege*, *zunguot*, *klagendunde*), 35 K, 2 U. Danach
     wurden N (ent- ausgenommen), Z (zun- erfasst) und U (neu) nachgeschärft.
   - **Prüfrunde 2** (Seed 20261031, endgültige Regel, 80 neue Einträge ohne die aus Runde 1;
     `verschmelzungen/runde2-*`; reproduzierbar mit `python goldstandard/verschmelzungen/runde2_ziehen.py`,
     das Liste und Schlüssel byte-gleich neu erzeugt, geprüft am 2026-10-30;
     Grundmengen 1.686 Treffer und 1.313 Nicht-Treffer; Urteilszahlen aus Schlüssel und Urteilsdatei ausgezählt): Treffer 36 V, 0 K, 4 U
     (*enrüemen*, *enrâten*, *enschüten*, *enleiten*: Lexer führt je ein ent-Stichwort, nur der Beleg
     entscheidet). Nicht-Treffer 1 V (*alunguot*, al + unguot, Grenzfall Gradadverb), 38 K, 1 U
     (*inlant*). Wilson-Intervalle (95 %, nachgerechnet am 2026-10-30): Präzision 36/36 = 90,4 bis
     100 %; mit U als falsch gezählt 36/40 = 76,9 bis 96,0 %; übersehen 1/39 = 0,5 bis 13,2 %. Durch die
     Entscheidung zu en- zählen die vier en-Fälle als gewollte Treffer.
   - **Einschränkung:** Übersehene Verschmelzungen sind nur unter Einträgen mit einem Funktionswort
     unter den Bestandteilen gemessen. Verschmelzungen ohne verlinkte Bestandteile findet die Regel
     nicht, und die Stichprobe sieht sie nicht. Die Urteile beider Runden stammen von einem Agenten und
     sind nicht von Julia gegengelesen. Die Bestandteile im Lexikon sind als Merkmal unzuverlässig
     (`knowledge/data.md`, B16).

**Neumessung auf dem festgelegten Korpusstand** (2026-11-12). Korpusstand für Pilot und ganzen
Goldstandard: Upstream `a938559dc` vom 2026-10-14; der Fork-Korpus ist byte-gleich mit diesem
Stand, ein Upstream-Merge vorher findet nicht statt (Entscheidung Julia Hintersteiner, 2026-11-12,
Antwort „Stand 14.10. (Empf.)“; Gegenoption „Erst Upstream mergen“: laut `git diff --stat` der
Hauptsitzung 136 Upstream-Commits weiter, 86 Korpus- und Normdatendateien geändert, darunter
`lexicon.xml` und `concepts.xml`; übernommen, nicht nachgemessen). Die alten Zahlen oben bleiben
als Messungen ihres Datums stehen. Die neuen stammen aus zwei Läufen der Hauptsitzung auf HEAD
`be8b91fc3`:

**Stand vom 2026-11-20 (A39):** Der Upstream wurde am 2026-11-20 doch in den Fork gemergt (Merge-Commit `ba6a3280a`, Upstream `d3bdfe738` vom 2026-11-19; letzter Commit mit Änderungen an `tei/` oder `authority-files/` ist `ce68c2783`). Die Aussage oben, der Fork-Korpus sei byte-gleich mit `a938559dc` und ein Merge finde nicht statt, galt am 2026-11-12 und gilt für den Arbeitsbaum des Forks nicht mehr. **Der Korpusstand des Goldstandards bleibt `a938559dc`.** Pilot, Ausschlussliste und `obergattungen/texte.csv` sind auf diesem Stand erzeugt. **Ziehungen (Pilot reproduzieren, Hauptstichprobe) und `ausschluss_nachmigration.py` laufen in einem Worktree auf `a938559dc`, nicht im Haupt-Checkout:** `git worktree add --detach <Pfad> a938559dc`, dann den ganzen Ordner `goldstandard/` aus dem aktuellen `main` hineinkopieren (auf `a938559dc` gibt es ihn noch nicht) und die Skripte aus der Wurzel des Worktrees starten. Erprobt am 2026-11-20 (Hauptsitzung): `pilot_ziehen.py` lief dort durch, `items-pilot.json` und `manifest-pilot.json` kamen byte-gleich mit den eingecheckten heraus (`git hash-object` 686aa7d73 bzw. 564c4a820). `pilot_ziehen.py` bricht im Haupt-Checkout ab (Prüfung des Korpusstands). Messung und Entscheidung: A39.

- **Ausschluss 1** (`ausschluss_nachmigration.py`, Ergebnis aus `ausschluss/zusammenfassung.json`
  gelesen am 2026-11-12): 7.545.802 lemmatisierte Tokens, 157.724 ausgeschlossen (WZB 142.412, Lemma
  oder Sense geändert 15.312), 34.336 nur markiert.
- **Grundgesamtheit und Ausschlüsse 1, 2, 3, 5** (`pilot/pilot_ziehen.py`, Zählungen aus
  `pilot/manifest-pilot.json`, Feld `zaehlungen`, gelesen am 2026-11-12): Basis (Lemma mit mindestens
  zwei Senses, Wortartregel, ohne WZB und SBF) 1.447.811 Tokens. Davon fallen heraus: Ausschluss 1
  13.781, Ausschluss 5 1.788, Ausschluss 2 1.215 (22 Lemmata), Ausschluss 3 0 Tokens (2 Lemmata im
  Lexikon). Tokens mit mehreren `@lemmaRef`: 0. **Grundgesamtheit 1.431.027 Tokens** in 5.025 Paaren,
  4.690 Lemmata und 665 Texten; D1 202 Texte mit 140.276 Tokens.
- **Markierungen** in der Grundgesamtheit: `pos_abweichend` 185 Tokens, nur-`@pos` markiert 6.534.
  Die 185 weichen von den 226 oben ab (Messung vom 2026-10-30): dort fehlten die Ausschlüsse 2 und 5
  und galt die alte Ausschlussliste, und das Skript zählt nur Tokens mit nicht leerem `@pos`. Die
  Abgrenzungen wurden nicht gegeneinander abgeglichen.
- Die Läufe selbst sind hier nicht wiederholt (je 3 bis 4 Minuten, sie überschreiben Dateien);
  gelesen wurden die Ergebnisdateien.

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
Hauptrunde durchschlagen. Der Pool wird nach dem Verfahren der Hauptstichprobe im Kleinen gezogen
(Entwurf, Julias Bestätigung steht aus, A30); er hat dann 108 statt „ca. 100“ Items, weil 36 Zellen × 3.
Gezogen und eingefroren wird der ganze Pool am 2026-11-12 (Entscheidung Julia Hintersteiner,
Antwort „Ganzen Pool, 15 morgen (Empf.)“), 15 Items davon gehen in Runde 0, ursprünglich am 2026-11-13, verschoben auf 2026-11-14 (A31).

**Entwicklungsdaten für das LLM:** Prompt-Wortlaut, Antwortformat, Few-shot-Beispiele (Anzahl und
Herkunft) und jeder Formatvergleich werden nur am Pilot-Pool gewählt, nie an der Haupt- oder
Panelstichprobe. Few-shot-Beispiele aus Silber enthalten keine Tokens der Stichproben. Wirkungen
von Prompt-Überarbeitungen werden nur an Items berichtet, die beim Überarbeiten nicht gesehen
wurden. Der Artikel sagt das ausdrücklich. Begründung: Die Prompt-Formulierung verschiebt die
Werte im Mittel um etwa 5 Punkte zwischen bestem und schlechtestem Prompt, und Meconi et al.
(2025, S. 33900) wählen den Prompt an einer eigenen Entwicklungsmenge, nicht an den Testdaten.

**Kontrollbedingung ohne Kontext (nur im Pilot, A28):** Am Pilot-Pool kann eine Bedingung ohne
Kontext (nur Lemma und Karten) laufen, um zu sehen, wie viel das LLM aus den Karten allein errät.
Anlass ist eine Deutung der KI-Zusammenfassung zu Matusch (2025, Tab. 4.6), nicht die Aussage der
Arbeit. In Haupt- und Panelstichprobe gibt es diese Bedingung nicht.

**Variante am Pilot-Pool für Freeze 2 (A34):** Am Pilot-Pool kann zusätzlich geprüft werden, ob der
Oberbegriffspfad auf den Karten dem LLM hilft oder schadet (Karten mit und ohne Pfad für das LLM).
Anlass: Zusatzkontext aus Hyperonymen schadete bei Ghizzota et al. (2026, Tab. 2) zwei von drei LLMs
deutlich (Beleg aus einer nicht gegengelesenen KI-Zusammenfassung; dort eine binäre Entscheidung je Sense
im Lateinischen, also eine andere Aufgabe). Die Variante läuft nur am Pilot-Pool (A17) und wird in
Freeze 2 festgeschrieben. Für Menschen bleibt der Pfad auf der Karte (Abschnitt 5); eine Karte ohne Pfad
für das LLM wäre eine Abweichung von der gleichen Darbietung (A27) und gilt nur, wenn Freeze 2 sie
ausdrücklich so festlegt.

### 4.3 Zellen der Hauptstichprobe

36 Zellen = **Polysemie** × **Wortart** × **Frequenzband**:

- **Polysemie** = Zahl der Senses im Inventar: 2 / 3 / 4+ (4+ reicht bis 15, Median 5). Inventar
  statt Belegung, weil die Menügröße für alle Lemmata beobachtbar ist, auch ohne Silber, und das
  ist, was Mensch und LLM sehen. Die Zahl der im Silber belegten Senses, der MFS-Anteil und die
  Sense-Entropie werden pro Item im Manifest mitgeführt, als Kovariaten (Begründung unten). Geschichtet wird
  nicht nach ihnen, weil sie aus Silber stammen, dessen Qualität selbst gemessen werden soll.
  Genauer belegt ist davon nur Folgendes (Korrektur vom 2026-11-16, K1 und K11, A38; Belege aus nicht
  gegengelesenen KI-Zusammenfassungen): Loureiro et al. (2021, S. 407) finden kaum Zusammenhang zwischen
  der Sense-Zahl und der Leistung von **Systemen**, gemessen an 20 Nomen mit 2 bis 5 groben Senses; die
  Schiefe des Sense-Verhältnisses vergleichen sie nicht mit der Sense-Zahl, sie zieht überwachte und
  feinabgestimmte Modelle zum häufigsten Sense (S. 411 bis 413). MFS-Anteil und Entropie bleiben deshalb
  als Kovariaten, begründet als Faktor für Modellverzerrung. Dass die Entropie die **Schwierigkeit**
  besser vorhersagt als die Sense-Zahl, zeigen Kilgarriff & Rosenzweig (2000, Abschnitt 5.1;
  Korrelation mit der Systemleistung −0,510 gegen −0,258); Passonneau et al. (2010) referieren die
  Entropie nur. Kilgarriff (1998, S. 15 bis 16) schichtet nach Wortart, Frequenz und Polysemie, misst aber
  keine Schwierigkeit.
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
4. **Obergrenze pro Text:** höchstens 3 Items aus einem Text über alle Komponenten (bestätigt am 2026-10-16);
   **Ausnahme Historiografie: höchstens 5** (entschieden am 2026-10-30, A20), weil 13 Texte × 3 = 39
   Items den Zielanteil von etwa 48 Items nicht erreichen. Ist die Grenze
   erreicht, wird in Stufe 2 neu gezogen. Die Grenze hält den Klumpeneffekt klein; sie ist über die
   Abhängigkeit innerhalb eines Textes zu begründen. Gale, Church & Yarowsky (1992, S. 236) belegen
   dagegen die Klumpung **desselben Wortes** im selben Text (51 von 54 Paaren, 94 %, mit den
   Einschränkungen: 9 Nomen, Artikel einer Enzyklopädie, fünf Urteilende, darunter die drei Autoren; die
   96,9 % aus dem ACL-Beitrag derselben Autoren lassen sich aus 54 Paaren nicht bilden). Das stützt
   „1 Token pro Paar“ und die Panelregel (5 Tokens aus 5 Texten), nicht die Obergrenze pro Text (K2, A38;
   Beleg aus nicht gegengelesenen KI-Zusammenfassungen). Dass die
   All-Words-Sets des englischen Standardrahmens aus wenigen Dokumenten bestehen (3 bis 13) und
   ihre MFS-Werte streuen (54,5 bis 67,1), belegen Raganato et al. (2017, Tab. 1 und 2; aus einer
   nicht gegengelesenen KI-Zusammenfassung); die Deutung als Klumpenstichproben ist unsere eigene,
   die Arbeit spricht nicht so (A24). Ein Vorbild im ReM gibt es dafür nicht: Das
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
vor den Formen. **Entschieden am 2026-10-30** (Julia Hintersteiner): sieben Gruppen, Einzelheiten
und Zuordnung der Sonderfälle in [OBERGATTUNGEN.md](OBERGATTUNGEN.md). Der Text SBF (Flugschrift
Donnerstein, 57 Zieltokens, nur „Mediale Sonderform") ist **weggelassen**, also nicht in der
Grundgesamtheit; HZU2, HZU und HNI gehören zu Fach- und Rechtsliteratur, BAR zur Großepik. Die
Tabelle steuert die Gewichte in 4.4 und wird mit Freeze 1 eingefroren.

### 4.9 Manifest pro Item

Item-ID, `xml:id`, Datei, Komponente, Zelle, Lemma, Wortart und ihre Herkunft (Lexikon oder Token),
Zahl der Senses (Inventar und im Silber belegt), MFS-Anteil und Entropie im Silber (Leave-out),
Frequenz und Band, Domäne, Obergattungsgruppe, Markierung „nur `@pos` geändert", Markierung
`pos_abweichend` (Abschnitt 3, Ausschluss 4),
Inklusionswahrscheinlichkeit.

### 4.10 Zwei Einfrierpunkte

- **Freeze 1, vor der Ziehung:** Grundgesamtheit und Ausschlüsse mit Zahlen, Wortartregel, Zellen,
  Bänder, Domänenquote, Panel-Regeln, Gattungstabelle, Obergrenze pro Text, Seed, Korpus-Commit.
- **Freeze 2, vor der Hauptrunde:** Richtlinien, Pilotschwelle, Agreement-Maße, Bewertungsregeln
  (Abschnitt 9.2), MFS-Definition, LLM-Konfiguration (Modell und Version, Prompt, Temperatur,
  Anzahl der Läufe pro Item, ob das LLM dieselben Karten sieht wie die Menschen), endgültiges N.
  Die Konfiguration umfasst zusätzlich (A26): Zugang über die API mit exakter Snapshot-ID (keine
  Weboberfläche), Abfragedatum, maximale Antwortlänge, alle Sampling-Parameter ausdrücklich gesetzt
  (Temperatur, top_p, top_k) statt Standardwerten, Kartenformat und Kontextumfang für das LLM und
  den im Modellkarten-Text erklärten Sprachumfang. Der Artikel nennt diese Angaben im Text, nicht
  nur in Abbildungen. Dazu kommt (A37): die Ausschlusszusage des API-Anbieters, dass Eingaben nicht ins
  Training gehen, mit Datum dokumentiert; schon der erste Aufruf mit Testdaten kompromittiert sie für
  spätere Modelle desselben Anbieters (Jacovi et al. 2023, S. 5076, 5078). Der Prompt-Wortlaut wird am Pilot-Pool gewählt (Abschnitt 4.2, A17) und in
  Freeze 2 festgeschrieben, einschließlich der Anweisung, wie `MEHRERE` zu beantworten ist
  (Abschnitt 9.2, A23). Das LLM sieht dieselbe pro Item gemischte Kartenreihenfolge wie die
  Menschen, und diese Reihenfolge wird für das LLM ebenso protokolliert (A27). Zusatzinformation
  auf Karte und im Kontext (Werktitel, Notizen an Senses, Nennung von Sprachstufe und Epoche im
  Prompt) ist für Mensch und LLM gleich; was konkret gezeigt wird, bleibt offener Punkt 4 (A27).
  Bei mehreren Läufen pro Item wird in Freeze 2 festgelegt, was als LLM-Vorhersage gilt: ein
  vorab bestimmter Lauf, die Mehrheit mit Gleichstandsregel oder die Verteilung (welche, entscheidet
  Julia in Freeze 2). Die Übereinstimmung zwischen den Läufen wird als eigenes Ergebnis berichtet
  (Mittelwert und Streuung). Begründung: Eine Mehrheit über mehrere Läufe ist selbst ein Ensemble
  (Chen et al. 2025, S. 5), und der McNemar-Test verglich dann ein Ensemble mit einer
  Einzelbaseline. Vorlagen gehen auseinander: mindestens fünf Läufe bei Temperatur 0,7 mit
  Konsistenz als Konfidenz (Pangakis & Wolken 2025, S. 1474 Fn. 12, S. 1475) gegen greedy decoding
  mit einem Lauf (Basile et al. 2025, S. 5). „Deterministisch bei Temperatur 0“ ist eine
  Behauptung, keine Zusage (Campesato 2024, S. 218).
  **Für Freeze 2 vorgemerkt (A34, A35):** die Variante mit und ohne Oberbegriffspfad für das LLM am
  Pilot-Pool (Abschnitt 4.2) und drei Sekundärauswertungen (Abschnitt 9.2).

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

**Im Pilot: eigene Lesart vor den Karten (A31).** Im Pilot (Ablauf `lesart-zuerst`, Standard) bleiben
Karten, Status, Sicherheit und Kommentar verdeckt, bis die annotierende Person eine eigene Lesart
(Paraphrase, mindestens 2 Zeichen) notiert und „Karten zeigen“ geklickt hat. Die Lesart wird mit
Zeitstempel protokolliert (`karten_aufgedeckt`) und ist danach nicht mehr änderbar; es gilt die erste
Aufdeckung, ein Entwurf vor dem Aufdecken wird nicht protokolliert. Danach folgt die Kartenwahl wie oben.
Über den Ablauf in der Hauptrunde (ganz oder als Teilstichprobe, z. B. Lemma-Panel) entscheidet Julia
Hintersteiner nach dem Pilot. Der Ablauf `direkt` (Karten sofort) bleibt baubar.
**Ablaufwechsel zur Hauptrunde (A34):** `lesart-zuerst` und `direkt` sind zwei verschiedene Instrumente,
denn schon kleine Änderungen am Instrument verschieben Labels (Beck et al. 2024: zwei Fragen auf zwei
Bildschirme statt einem verschoben die Labelraten um 5 bis 7 Prozentpunkte, S. 81, dort referiert;
starke Haupteffekte der Bedingung, S. 84; Belege aus einer nicht gegengelesenen KI-Zusammenfassung). Die
Schwelle der Stoppregel (Abschnitt 7, A32) misst `lesart-zuerst`. Wird für die Hauptrunde ein anderer
Ablauf gewählt als der des Pilots, gilt das als Abweichung (Eintrag im Abweichungslog) und verlangt
mindestens eine Pilotrunde im neuen Ablauf.

**Blindheit:** Die Annotationsdatei enthält weder Silber-`@ana` noch LLM-Vorschläge. Die
Blindheit ist damit technisch gesichert, nicht nur durch eine Anweisung.

## 7. Ablauf

Der Ablauf folgt dem in der Annotationsliteratur üblichen Zyklus (Pustejovsky & Stubbs 2012;
Hovy et al. 2006; Belege in [LITERATUR-IAA.md](LITERATUR-IAA.md)).

1. **Richtlinien v0** mit einer Entscheidungsregel für jeden Status aus Abschnitt 6.
2. **Pilot:** ca. 50 Items **außerhalb** der Hauptstichprobe, von beiden blind annotiert.
   Übereinstimmung und Konfusionsmatrix rechnen, Abweichungen besprechen, Richtlinien und
   Oberfläche nachschärfen. Mit **frischen** Items wiederholen, bis eine vorab festgelegte Schwelle
   erreicht ist (OntoNotes verlangte 90 %; im Werk steht nur „ITA scores below 90%“ ohne Angabe des Maßes, Hovy et al. 2006, S. 58; K7, A38). Pilotitems gehen weder in den
   berichteten IAA-Wert noch ins Gold.
   **Rundengröße und Stoppregel (A32, entschieden 2026-11-13):** Nach Runde 0 (15 Items, ohne
   Schwelle) Runden zu je 25 frischen Items aus dem Pilot-Pool; bei 108 Items reicht der Pool für
   drei solche Runden (90 Items), 18 bleiben Reserve. Gemessen wird pro Runde auf den 25 Items,
   bevor Abweichungen besprochen werden, mit Krippendorffs α nominal auf dem ganzen Label (Status
   und Menge der gewählten Karten, exakt). Ergebnis einer Runde:
   - α ≥ 0,80: Richtlinien einfrieren, Hauptrunde.
   - 0,67 ≤ α < 0,80: nachschärfen, nächste Runde; nach der letzten Poolrunde trotzdem einfrieren
     und als Einschränkung berichten.
   - α < 0,67 nach der letzten Poolrunde: keine Hauptrunde; das Instrument ändern (gröbere Senses
     oder andere Darbietung) und neue Pilotitems ziehen.
   **Die Schwelle ist eine Projektregel (A34):** Sie folgt nicht aus der Literatur. 0,67 und 0,80 stammen
   aus der Inhaltsanalyse (Krippendorff 1980, über Carletta 1996; Artstein & Poesio 2008, S. 576),
   Passonneau et al. (2006, S. 1951) raten im Pilot von absoluten Schwellen ab, und Passonneau (2006,
   S. 833) ordnet 0,67 als Schwelle für Schlüsse aus codierten Variablen ein. Gestützt wird 0,8 als Maß für
   die Tragfähigkeit eines WSD-Golds von Kilgarriff (1998, S. 11: κ > 0,8, entsprechend 80 bis 90 %
   Rohübereinstimmung je nach Sense-Zahl, „critical to the viability of the exercise“). Vorab festgelegt
   ist sie trotzdem, weil das besser ist als nachträglich.
   Weil jedes Lemma eigene Sense-IDs hat, schätzt α den Zufall aus fast nie zusammenfallenden
   Labels und liegt damit nahe an der Rohübereinstimmung. Für WSD steht das in keinem der gelesenen Werke;
   den Mechanismus zeigen Artstein & Poesio (2008, S. 586, auch S. 561) an der Diskursdeixis, einer
   anderen Aufgabe: Die Labels verschiedener Items überschnitten sich kaum, die erwartete Abweichung lag
   nahe 1, und α war „very close to the complement of the observed disagreement“. Das gepoolte α ist
   nicht mit WSD-Werten vergleichbar, die den Zufall pro Wort schätzen (Ng et al. 1999: κ 0,317 bei
   56,7 % Rohübereinstimmung). **In Pilot und Hauptrunde wird die Rohübereinstimmung immer neben α
   berichtet; Vergleiche mit der Literatur laufen über die Rohübereinstimmung.** Belege aus nicht
   gegengelesenen KI-Zusammenfassungen.
   Bei 25 Items ist ein einzelner Wert unsicher (bei 80 % Übereinstimmung 95 %-Wilson-Intervall
   etwa 61 bis 91 %). Die Schwelle entscheidet, wann das Nachschärfen endet, nicht ob das Gold
   brauchbar ist.
   **Auswertung des Pilots (A34):** Die Abweichungen werden pro Lemma festgehalten, nicht nur als
   Gesamtwert. OntoNotes vergröbert Senses pro Wort, bis die Übereinstimmung erreicht ist (Hovy et al.
   2006, S. 58, Abb. 1); für den Ausweg „gröbere Senses“ braucht es deshalb die Abweichungen pro Lemma.
   **Ergebnis Runde 0 (gerechnet am 2026-11-26 mit `pilot/auswerten.py`, vor jeder Besprechung, Schritt 5;
   nur Kennzahlen, keine Labels):** 15 Items, beide Personen haben alle 15 festgehalten (gültig 15).
   Beide mit Kurzanleitung v0.3 (2026-11-13), Werkzeugstand `a2a1715e99e4`, Ablauf Lesart zuerst;
   exportiert am 2026-11-23 (Julia) und 2026-11-25 (Alan). Ganzes Label (Maß der Stoppregel): Roh
   9 von 15 = 60,0 % (95 %-Wilson 35,7 bis 80,2 %), α nominal 0,587; Runde 0 ohne Schwelle (A32).
   Status gleich: 10 von 15 = 66,7 % (41,7 bis 84,8 %). Sense-Ebene (14 Einheiten, Abschnitt 9.1):
   α MASI 0,684, α nominal 0,629, Roh exakt 9 von 14 = 64,3 % (38,8 bis 83,7 %), Roh Überschneidung
   12 von 14 = 85,7 % (60,1 bis 96,0 %). Sicherheit sicher/eher sicher/unsicher: Julia 9/6/0, Alan
   4/8/3; Kontext erweitert: Julia 8, Alan 6 Items; Lesart notiert: beide 15. Aus der
   Konfusionstabelle: 5 Items mit abweichendem Status, bei allen steht auf mindestens einer Seite
   `MEHRERE`; 1 Item mit gleichem Status, aber anderer Kartenmenge; 3 Sense-Einheiten mit
   Überschneidung, aber nicht exakt. Bei 15 Items sind die Intervalle breit; die Zahlen steuern
   die Besprechung, nicht die Schwelle.
3. **Einfrieren:** Richtlinien mit Versionsnummer und Prüfsumme; Schwelle, Maße und
   Auswertungsplan werden vor der Hauptrunde festgeschrieben.
4. **Hauptrunde:** beide annotieren alle Items unabhängig und blind. Die Itemreihenfolge wird pro
   Annotator:in zufällig gemischt (Seed protokolliert), weil Reihenfolge Urteile verschiebt
   (Beck et al. 2024). Kurze Sitzungen; die Zeitstempel erlauben nachträglich eine Prüfung auf
   Ermüdung und Drift.
5. **Roh-IAA zuerst:** Die Übereinstimmung wird gerechnet und festgehalten, **bevor** irgendeine
   Abweichung besprochen wird.
6. **Adjudikation:**
   - **blind:** Die Adjudikation sieht beide Labels, aber nicht, von wem sie stammen, und ebenso wenig
     Silber-`@ana` und LLM-Ausgabe (A36): Vorgaben verankern die Korrektur messbar (Berzak et al. 2016,
     S. 2219 bis 2220; dort für vorausgefüllte Parserausgaben, hier als Analogie).
   - **Ursachencode pro Abweichung** nach Ihden et al. (2015, Folien 16, 19; Vortragsfolien, Erstautorin
     laut Titelfolie, Datei `Barteld-etal-2015-…`, BibTeX-Schlüssel `ihden2015tagset`). Die drei
     Kategorien der Vorlage werden übernommen: (1) fehlende Regeln, (2) Abweichungen trotz bestehender
     Regeln (in der Vorlage überwiegend Regelverstöße, daneben Folgefehler und vergessene Annotation),
     (3) unterschiedliches Textverständnis. **Eigene Erweiterungen, nicht aus der Vorlage:**
     Inventarlücke, Editions- oder Normalisierungseffekt, echte Textambiguität. Letztere ist in der
     Vorlage kein Ursachencode, sondern ein Annotationswert (bei uns eher `MEHRERE`).
   - **Dritte Person:** Weil Julia die Richtlinien entworfen hat und zugleich annotiert, kann ihr
     implizites Wissen die Übereinstimmung aufblähen. Eine dritte Person prüft deshalb mindestens
     eine Zufallsauswahl von 10 bis 20 % der Adjudikationen sowie **alle** Fälle, in denen Julias
     Label übernommen wurde. Die Doppelrolle wird in der Publikation als Limitation genannt.
     Vorgesehen ist KZW (Entscheidung Julia Hintersteiner, 2026-11-13, A32); sie ist noch nicht
     angefragt.
   - `MEHRERE` darf als Mehrfachlabel ins Gold eingehen, wo die Richtlinien es zulassen.
7. **Alles bleibt erhalten:** Labels vor der Adjudikation, Sicherheitsangaben, Ereignisprotokolle,
   Richtlinienversionen (Prabhakaran et al. 2021; Plank 2022: Abweichung ist oft Signal). Veröffentlicht
   werden die Labels pro Person mit Kennung (Prabhakaran et al. 2021, S. 137: Labels pro Annotator:in,
   dazu Angaben zur Rekrutierung); die Grundlage dafür (Arbeitsauftrag und Informationsblatt statt Einwilligung, A40; offener Punkt 14) muss das abdecken. Die Lesarten
   aus A31 werden als Rohdaten mitveröffentlicht (Plank 2022, S. 10673: Unsicherheitsmarkierungen und
   Freitext-Begründungen als wertvolle Metadaten) (A36).
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

Zwei Ebenen werden getrennt ausgewertet (Artstein & Poesio 2008, S. 591, verlangen allgemein, die
Methode offenzulegen; von Ausweichlabels oder fehlenden Werten ist dort nicht die Rede, K5, A38):

- **Statusebene:** Konfusionstabelle über die sechs Status aus Abschnitt 6, mit Häufigkeiten.
- **Sense-Ebene:** nur Items, bei denen beide `SENSE`, `MEHRERE`, `KEINE_PASST` oder `LEMMA_FALSCH` vergeben haben
  (A41, A42). `KEINE_PASST` geht als eigene Kategorie ein, als Menge {KEINE_PASST}; `SENSE` gegen
  `KEINE_PASST` ist damit eine volle Abweichung (Abstand 1). `LEMMA_FALSCH` geht ebenso als eigene
  Kategorie ein, als Menge {LEMMA_FALSCH} (A42). Nur `KONTEXT_UNZUREICHEND` und `TEXT_DEFEKT` gelten
  hier als fehlende Werte.

Auf der Sense-Ebene werden berichtet:

1. **Hauptmaß:** Krippendorffs α mit MASI-Distanz (Passonneau 2006), damit `MEHRERE` als
   Teilübereinstimmung zählt. Der Abstand ist **d = 1 − J·M** (Passonneau 2006, S. 834 bis 835; ebenso
   Passonneau et al. 2006, S. 1953; A33). J ist der Jaccard-Koeffizient (Schnitt durch Vereinigung der
   beiden Mengen), M die Monotonie: 1 bei gleichen Mengen, 2/3 bei Teilmenge, 1/3 bei Schnitt mit zwei
   nicht leeren Differenzen, 0 bei disjunkten Mengen. Die Einheit ist das Item, die Mengen sind die
   gewählten Sense-IDs, bei `KEINE_PASST` die Menge {KEINE_PASST}. Typische Fälle (M-Werte und Rechenweg nach der nicht gegengelesenen
   KI-Zusammenfassung zu Passonneau 2006, Rechnung nachgerechnet):

   | Person 1 | Person 2 | J | M | Abstand 1 − J·M |
   |---|---|---|---|---|
   | {s1} | {s1} | 1 | 1 | 0 |
   | {s1} | {s1, s2} | 1/2 | 2/3 | 2/3 |
   | {s1, s2} | {s1, s2, s3} | 2/3 | 2/3 | 5/9 |
   | {s1, s2} | {s2, s3} | 1/3 | 1/3 | 8/9 |
   | {s1} | {s2} | 0 | 0 | 1 |

   `SENSE` gegen `MEHRERE` mit Überschneidung zählt also nur zu einem Drittel als Übereinstimmung.
   Artstein & Poesio (2008, S. 584) geben MASI abweichend als Produkt zweier Abstände d_P × d_J an; das
   ergäbe für {s1} gegen {s1, s2} 1/6 statt 2/3. Festgelegt wird 1 − J·M. Dazu α nominal (Mengen als
   unteilbare Labels) als **strengere Variante**, nicht als allgemeine untere Schranke: Bei Passonneau
   (2006, Tab. 1, S. 835) liegt ein gewichtetes α (Jaccard, −0,44) unter dem nominalen (0) (A33).
2. **Rohübereinstimmung** (exakt und „Überschneidung"). Nur sie ist direkt mit LLM- und
   MFS-Genauigkeit vergleichbar (Kilgarriff 2001).
3. **Zufallsmodell über Lemmata hinweg:** Jedes Lemma hat sein eigenes Inventar, und pro Lemma
   gibt es meist nur ein Token. Naives Poolen über alle Sense-IDs macht die erwartete
   Übereinstimmung winzig und bläht den Wert auf. Festlegung dieses Protokolls: Die erwartete
   Übereinstimmung wird pro Lemma aus den Sense-Anteilen berechnet und über die Items summiert,
   κ = (ΣA_o − ΣA_e) / (N − ΣA_e). Die Aussage, für diese Konstruktion gebe es keinen etablierten
   Standard, gilt nicht (Korrektur vom 2026-11-16, A33): Veröffentlichte Vorbilder rechnen den Zufall
   pro Wort, Ng et al. (1999, S. 10: κ pro Wort, ungewichtet gemittelt) und Passonneau et al. (2010,
   S. 3245, Tab. 1: α pro Wort), allerdings mit vielen Sätzen pro Wort. Das Protokoll übernimmt das
   Prinzip, nicht das Verfahren, und begründet die Wahl: Das Inventar ist pro Lemma verschieden, ein
   Zufallsmodell über alle Sense-IDs beschriebe keinen Zufall zwischen Alternativen, die eine
   Annotator:in je sieht. Die gepoolte Variante wird daneben berichtet. **Einschränkung:** Krippendorffs
   Stichprobenregel (jede Kategorie so oft, dass mindestens fünf Zufallsübereinstimmungen zu erwarten
   sind; Artstein & Poesio 2008, S. 575) ist bei meist einem Token pro Lemma und lemmaspezifischen
   Sense-IDs nicht erfüllbar.
4. **Prävalenz:** Bei einem dominanten Sense kann allein das Zufallsmodell κ um mehr als 0,2
   verschieben (Senseval-3: κ 0,58 gegenüber 0,35; Mihalcea et al. 2004, S. 26). Beide Werte stammen
   aus dem ganzen OMWE-Bestand (über 350 Wörter), nicht aus dem Testset, und Mikro- und Makro-κ
   unterscheiden sich in Mittelung und Zufallsmodell zugleich (K15, A38).
   Deshalb werden die Sense-Randverteilungen, die Übereinstimmung getrennt für MFS- und
   Nicht-MFS-Tokens und Gwets AC1 als Kontrollgröße mitberichtet.
5. **Konfidenzintervalle:** 95 %, per Bootstrap. Gezogen wird nach Clustern (Text), weil Tokens
   aus demselben Text nicht unabhängig sind. Grobe Erwartung: bei N ≈ 500 etwa ±0,05 bis ±0,09,
   bei Untergruppen von ca. 120 Items etwa ±0,11 bis ±0,18 (eigene Rechnung mit der
   Großstichproben-Näherung, nachgerechnet am 2026-10-08).
6. **Aufschlüsselung** nach Polysemiegrad, Wortart, Frequenzband, Domäne, Obergattungsgruppe und
   angegebener Sicherheit, jeweils mit Intervall. Die Hauptauswertung wird zusätzlich nach der
   Herkunft der Wortart aufgeschlüsselt (Lexikon oder Token, Abschnitt 3; A25).
7. **Zwei Ebenen des Begriffssystems:** zusätzlich die Übereinstimmung, wenn jeder Sense auf die
   Oberbegriffe seiner Begriffe abgebildet wird. Die Granularität ist der stärkste bekannte
   Einflussfaktor auf WSD-Übereinstimmung (Ng et al. 1999; Hovy et al. 2006). Das grobe Maß wird
   vorab definiert, nicht nachträglich durch Zusammenlegen gewonnen (Artstein & Poesio 2008, S. 588).
   Für die Vorabberechnung, auf welcher Stufe des Zahlencodes (`knowledge/data.md`, B11) die Senses eines
   Lemmas zusammenfallen, dient die Regel von Vial et al. (2019, S. 111): jeder Sense wird auf den
   höchsten Vorfahren abgebildet, der die Senses des Lemmas noch trennt (A33). Als Vorbild für eine grobe
   Auswertungsebene sind Vial et al. nur bedingt geeignet: Sie sorgen dafür, dass die Senses eines Lemmas
   **nie** zusammenfallen, und bewerten weiter feinkörnig (S. 110). Besser passen Supersenses (Ciaramita
   & Altun 2006) und Basic Level Concepts (Izquierdo et al. 2007); beide sind nur nach Vial et al.
   bekannt und zu beschaffen.

**Einschränkungen (A33):** Zwei Annotierende sind weniger, als Krippendorff empfiehlt (drei oder mehr;
Artstein & Poesio 2008, S. 575, nach Krippendorff 2004a, Kap. 11). Die dritte Person (Abschnitt 7,
Schritt 6) prüft die Adjudikation und annotiert nicht mit. Die Stichprobenregel zu Punkt 3 ist nicht
erfüllbar. Belege dieses Abschnitts aus nicht gegengelesenen KI-Zusammenfassungen.

### 9.2 Gold, Silber, LLM

- **Jede:r gegen das Gold:** Übereinstimmung jeder Annotator:in mit dem adjudizierten Gold, dazu die
  Adjudikationsstatistik nach Ursachencode. Nach Passonneau & Carpenter
  (2014, S. 311 bis 312) ist zufallskorrigierte Übereinstimmung für gute Goldlabels „neither necessary
  nor sufficient“ und „at best an indirect measure“; von adjudiziertem Gold spricht das Werk nicht
  (Korrektur vom 2026-11-16, K8, A38; ersetzt die Aussage, hohe Roh-IAA sage nichts über die Qualität des
  adjudizierten Golds).
- **Silberqualität:** Genauigkeit von Silber-`@ana` gegen Gold, nur Domäne D1 (Abschnitt 3), mit dem Vorbehalt, dass sie nur die Annotationskampagne dieser Texte beschreibt.
- **LLM gegen Baseline:** Genauigkeit gegen Gold. Die MFS-Baseline wird aus Silber gelernt,
  **ohne** die Stichproben-Tokens, und auf denselben Gold-Items gemessen. Damit ist der Vergleich
  gepaart (McNemar-Test) statt gegen einen festen Wert.
  - **Rückfall:** Hat ein Lemma nach dem Leave-out kein Silber, gilt der erste Sense in
    `lexicon.xml`. Der Anteil der Rückfall-Items wird berichtet; die Untergruppe „MFS aus Silber"
    wird sekundär ausgewertet. Der Test läuft über alle Items.
  - **Bewertungsregeln (vor Freeze 2 festgeschrieben):** Primäre Auswertungsmenge sind Items mit
    Gold-Status `SENSE` oder `MEHRERE`. Bei `MEHRERE` zählt eine Vorhersage als richtig, wenn sie
    einer der Gold-Senses ist (für Antworten mit mehreren IDs gilt der Punkt „Antworten mit
    `MEHRERE`" unten). Items mit `KEINE_PASST`, `LEMMA_FALSCH`, `KONTEXT_UNZUREICHEND` oder
    `TEXT_DEFEKT` gehen nicht in die Genauigkeit ein; wie oft das LLM bei ihnen abstiniert oder
    trotzdem einen Sense wählt, wird gesondert berichtet.
  - **Ungültige LLM-Antworten:** unparsbar, Sense-ID außerhalb des Menüs, ID eines anderen
    Lemmas oder mehrere IDs, die nicht als `MEHRERE` ausgewiesen sind (Status `SENSE` mit
    mehreren IDs; eine als `MEHRERE` ausgewiesene Antwort ist gültig, A23) und `MEHRERE` mit nur
    einer ID (wie bei den Menschen verlangt `MEHRERE` mindestens zwei, Abschnitt 6; A29). Sie werden als eigene Kategorie gezählt und berichtet und
    im primären gepaarten Vergleich als falsch gewertet; ein Ausschluss bräche die Paarung, weil MFS
    nie ungültig antwortet. Das LLM antwortet mit Kartennummer oder Sense-ID; die Sense-ID wird
    direkt aus der Nummer abgeleitet, nicht über Textabgleich (der Textabgleich bei Meconi et al.
    2025, S. 33898 bis 33899, ist bei kurzen, ähnlichen Begriffsnamen unsicher). Strutz (2026,
    S. 4 bis 6, 16) setzt Wohlgeformtheit ebenfalls als Tor vor die inhaltliche Bewertung. Eine
    gültige Ausweichantwort (Abstinenz) ist keine ungültige Antwort und fällt nicht hierunter.
  - **Antworten mit `MEHRERE` (entschieden am 2026-10-30, A23):** Das LLM darf mit `MEHRERE`
    und mehreren Sense-IDs antworten, hat also dieselben Optionen wie die Menschen (Prinzip des
    „Alternative Annotator Test", Calderon et al. 2025). Eine solche Antwort ist nur richtig, wenn
    jede genannte ID im Gold steht; bei einem Item mit Gold-Status `SENSE` ist sie damit falsch.
    Grund: Die Regel „richtig, wenn einer der Gold-Senses getroffen" würde bei einer Mengenantwort
    das Absichern belohnen, und die MFS-Baseline nennt immer genau einen Sense, sodass der
    McNemar-Test sonst teils das Antwortformat misst. Eine einzelne vorhergesagte ID wird weiter
    nach der Primärregel bewertet (richtig, wenn sie zu den Gold-Senses gehört). Der Anteil der
    `MEHRERE`-Antworten des LLM wird berichtet. Der genaue Prompt-Wortlaut wird in Freeze 2
    festgelegt, gewählt am Pilot-Pool (Abschnitt 4.2, A17).
  - **Einwand gegen die `MEHRERE`-Regel und Sensitivität:** Die Primärregel entspricht Henrichs
    Option (iii), „to score a system already as correct if it assigns only one of the multiple
    senses“. Henrich verwirft sie, weil sie „slightly higher evaluation results than would be
    genuinely correct“ erbrächte, und hält Teilwertung (Option i) für fairer (Henrich 2015,
    S. 151 bis 152). Die präregistrierte Primärregel bleibt stabil; zusätzlich werden zwei
    Sensitivitätsauswertungen berichtet: (a) Teilwertung mit dem Dice-Koeffizienten zwischen der
    Menge der Gold-Senses G und der tatsächlich vorhergesagten Menge P (2·|G∩P|/(|G|+|P|); bei
    genau einem vorhergesagten Sense 2/(|G|+1) bei Treffer, sonst 0; Henrich nutzt Dice nach
    Véronis 1998); (b) Genauigkeit ohne
    die `MEHRERE`-Items (Henrichs Option ii). Beides gilt für LLM und MFS-Baseline gleichermaßen,
    damit der gepaarte Vergleich gepaart bleibt. Der Anteil der `MEHRERE`-Items an der
    Auswertungsmenge wird berichtet.
  - Zusätzlich Macro-Genauigkeit nach Sense und die Genauigkeit auf Nicht-MFS-Items. Bei Maru et al.
    (2022, Tab. 1 und 2) besteht der „hard core“ (541 Instanzen, die alle sieben Systeme falsch lösen)
    fast nur aus Nicht-MFS-Instanzen; nicht alle Nicht-MFS-Belege sind aber hart (bestes System 54,2
    statt 76,4 Macro-F1 auf 2.525 Instanzen; K14, A38). Dort heißt „MFS“ der erste WordNet-Sense; die
    Festlegung für dieses Protokoll steht aus.
  - **Abstand zur Baseline (A35):** Die menschliche Rohübereinstimmung und die MFS-Genauigkeit werden auf
    denselben Items nebeneinander berichtet. Liegen beide nah beieinander, lässt sich kaum ein Verfahren
    unterscheiden („dynamic range“, Gale et al. 1992, S. 254).
- **LLM gegen menschliche Annotator:innen:** Zusätzlich zum Vergleich mit dem Gold wird geprüft,
  ob das LLM mit den beiden Menschen so gut übereinstimmt wie diese untereinander (Prinzip des
  „Alternative Annotator Test", Calderon et al. 2025). Die menschliche IAA ist ein
  Referenzwert für LLM-Werte. Als Obergrenze der Aufgabe nennt Kilgarriff (2001, S. 20) die
  Replizierbarkeit zwischen zwei Teams, nicht die IAA; eine Replizierbarkeitsmessung (ein zweites Paar
  mit denselben Richtlinien) ist hier nicht vorgesehen und bleibt als Grenze zu nennen (A35).
- **Sekundärauswertungen, für Freeze 2 vorgemerkt (A35):** (a) LLM und MFS getrennt nach Items, bei
  denen die beiden Annotierenden vor der Adjudikation übereinstimmten oder abwichen (Plank 2022,
  S. 10675); (b) nur Items, die beide als „sicher“ und gleich gelabelt haben (Passonneau & Carpenter
  2014, S. 322); (c) Kontrolle nach Position in der Sitzung (Beck et al. 2024, S. 83). Festgeschrieben
  wird in Freeze 2.
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
| Manifest des Pilots (Items mit `xml_id` liegen bereits öffentlich in `pilot/items-pilot.json`) | dieses Verzeichnis | ja |
| Manifest der Hauptstichprobe: Token-IDs | privat bis zum Ende der LLM-Läufe (A37) | erst danach; vorher nur die Prüfsumme des Manifests |
| Manifest der Hauptstichprobe ohne Token-IDs: Zellzuordnung, Seed, Korpus-Commit, Prüfsummen von Korpus, `lexicon.xml`, `concepts.xml` | dieses Verzeichnis | ja |
| Ziehungsskript, Ausschlussskript, `ausschluss/zusammenfassung.json` | dieses Verzeichnis | ja |
| Token-Liste der Ausschlüsse (`ausschluss/ausschluss-tokens.csv`) | nur lokal, reproduzierbar | nein |
| Menschliche Labels, Ereignisprotokolle, Adjudikation | privat (Drive oder privates Repo) | erst mit der Publikation, dann Zenodo |

Grund für die Trennung: Öffentliche Labels können in die Trainingsdaten künftiger LLMs geraten,
die später gegen genau diesen Goldstandard evaluiert werden sollen (Sainz et al. 2023). Die
mittelhochdeutschen Texte sind ohnehin online; zu schützen sind die Labels.

**Bei der Veröffentlichung** (Jacovi et al. 2023, EMNLP 2023, S. 5075 bis 5084): Labels verschlüsselt
ablegen, Passwort in der Publikation, Lizenz ohne Weiterverbreitung und ohne Trainingsnutzung, dazu ein
Canary-String. Der Canary-String ist eine eigene Maßnahme ohne Literaturbeleg; Jacovi et al. und Sainz
et al. erwähnen ihn nicht (Korrektur vom 2026-11-16, K9, A37; die frühere Zuschreibung an beide Werke
entfällt). Sainz et al. (Findings of EMNLP 2023, S. 10776 bis 10787) empfehlen weder Verschlüsselung noch
Lizenz, sondern verweisen auf Jacovi et al. (S. 10776).
Die Labels vor der Adjudikation werden mitveröffentlicht, pro Person mit Kennung (Prabhakaran et al.
2021, S. 137; A36), dazu die Lesarten aus A31 als Rohdaten (A36). **Token-IDs der Hauptstichprobe** bleiben
bis zum Ende der LLM-Läufe privat, öffentlich ist bis dahin nur die Prüfsumme des Manifests (A37).
Für die Pilotitems ist das zu spät, denn `pilot/items-pilot.json` liegt mit `xml_id` öffentlich im Fork,
und darüber ist für die D1-Items das Silber nachschlagbar. Pilotdaten sind Entwicklungsdaten, nicht Gold;
das Datasheet bekommt dazu einen Hinweis (offener Punkt 24). **Auswertung mit KI-Werkzeugen:**
Auswertungsskripte geben Labels nie in eine KI-Sitzung aus, nur Kennzahlen; das gilt auch für Claude
Code (A37).

## 11. Abweichungslog gegenüber der Präregistrierung vom 2026-04-24

| Nr. | Präregistriert | Jetzt | Begründung | Datum |
|---|---|---|---|---|
| A1 | Gold = bestehende MHDBDB-Annotation | Gold = neue Doppelannotation, bestehende Annotation = Silber | Herkunft, Zeitpunkt und Richtlinien der Bestandsannotation sind undokumentiert | 2026-10-08 |
| A2 | Quelle: bereits annotierte Texte ohne WZB | ganzes Korpus, geschichtet nach Silber ja/nein, ohne LLM-berührte Tokens | Mit A1 entfällt der Grund, nur annotierte Texte zu nehmen; der unannotierte Teil ist die eigentliche Zielpopulation | 2026-10-08 |
| A3 | 6 Zellen mit je ≥ 50 | Hauptstichprobe 36 Zellen × 10 (Polysemie × Wortart × feste Frequenzbänder), 1 Token pro Paar aus Lemma und Wortart; dazu Lemma-Panel 30 × 5 und Pilot-Pool | Frequenz als Schwierigkeitsfaktor (Kilgarriff 1998; **Korrektur vom 2026-11-16, K1: Kilgarriff 1998 schichtet nach Frequenz und Polysemie und misst keine Schwierigkeit, siehe A38**); Panel trennt Lemma- von Kontextschwierigkeit; Inferenz über ein gemischtes Modell | 2026-10-08, geändert 2026-10-16 |
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
| A19 | Ausschluss 4 (Abschnitt 3): Lemmata mit disjunkten Token-`@pos`-Werten ausgeschlossen (A15: vorläufig) | Ausschluss gestrichen; stattdessen Markierung `pos_abweichend` im Manifest, Tokens bleiben in der Grundgesamtheit; echte Lemmatisierungsfehler fängt `LEMMA_FALSCH`; Prüfstichprobe wird zu ca. 30 von Hand eingeordneten markierten Tokens, Ergebnis ins Datasheet. Löst A15 ab (A15 bleibt als Zwischenstand stehen) | Der Ausschluss verzerrt nach Frequenz (betroffene Lemmata: 0,7 % im Band 1–3, 9,2 % im Band >200; Messung der Hauptsitzung, übernommen) und trifft Wortartwechsel, die gewollt sein können. Die Markierung betrifft 226 Tokens (0,02 %). Die Grundgesamtheit 1.434.270 enthielt Ausschluss 4 nie, ihre Zahl ändert sich dadurch nicht. Entscheidung Julia Hintersteiner, 2026-10-30 („ja das hier 1. den ausschluss streichen und durch eine markierung ersetzen“) | 2026-10-30 |
| A20 | Obergrenze pro Text (Abschnitt 4.4, Punkt 4): höchstens 3 Items, ohne Ausnahme | Ausnahme Historiografie: höchstens 5 Items pro Text | 13 Texte × 3 = 39 Items erreichen den Zielanteil von etwa 48 Items nicht; mit 5 sind höchstens 65 möglich. Ohne Grenze hätte OVG grob 45 % der Gruppe, mit 5 höchstens etwa 10 % (grobe Wasserstandsrechnung der Hauptsitzung mit proportionaler Verteilung, keine Ziehungssimulation). Gleichzeitig entschieden: Gattungstabelle (OBERGATTUNGEN.md, Abschnitt 5) mit SBF weggelassen, HZU2, HZU und HNI zu Fach- und Rechtsliteratur, BAR (Umsetzung der Hauptsitzung nach Julias Antwort) zur Großepik, APO bleibt Historiografie. Entscheidung Julia Hintersteiner, 2026-10-30 („Historiografie: dann 5 pro Text“) | 2026-10-30 |
| A21 | Grundgesamtheit (Abschnitt 3): Verschmelzungen (Klise, Kontraktionen) wie jedes andere Lemma enthalten | Neuer Ausschluss 5: Verschmelzungen werden auf Lemmaebene aus der Grundgesamtheit genommen (Regel in `verschmelzungen.py`); Formen auf en- (Bestandteil `niht`) werden mit ausgeschlossen | Verschmelzungen tragen das volle Bedeutungsmenü des Grundworts samt Typlisten, oft bei einem Beleg (B15). Betroffen: 1.788 Tokens (0,12 %) aus 98 Lemmata, davon 1.662 Tokens aus 48 en-Lemmata (nachgemessen). Prüfrunden: Präzision 36/36 in Runde 2, 1 von 39 übersehen unter Einträgen mit Funktionswort (Urteile eines Agenten, nicht gegengelesen). Die MHDBDB führt die en-Lemmata selbst als NEG; einige echte ent-Verben gehen verloren. Entscheidung Julia Hintersteiner, 2026-10-30 („ok zu verschmelzungen: ja die nehmen wir raus“; zu den Formen auf en-: „Alle ausschließen (Empf.)“) | 2026-10-30 |
| A22 | Auswahlregel für die ca. 30 von Hand einzuordnenden Tokens mit Markierung `pos_abweichend` (Abschnitt 3, Ausschluss 4; A19): offen | Einfache Zufallsauswahl von 30 aus den markierten Tokens (226 nach Messung der Hauptsitzung, übernommen) mit festem, vorab notiertem Seed (Vorschlag 20261030; der Seed wird bei der Ziehung im Skript festgehalten) | Einfachste Regel ohne eigene Schichtung; die Ziehung ist noch nicht gemacht. Entscheidung Julia Hintersteiner, 2026-10-30 („ja passt“ auf den Vorschlag der Hauptsitzung) | 2026-10-30 |
| A23 | LLM-Antworten mit mehreren Sense-IDs (Abschnitt 9.2): „mehrere IDs bei `SENSE`“ ungültig (A18); Bewertung bei `MEHRERE`: „richtig, wenn einer der Gold-Senses getroffen“ (A14) | Das LLM darf mit `MEHRERE` und mehreren IDs antworten; so ausgewiesen ist die Antwort gültig und nur richtig, wenn jede genannte ID im Gold steht (bei Gold-Status `SENSE` also falsch). Eine einzelne ID wird weiter nach der Primärregel bewertet. Die Dice-Sensitivität aus A14 nutzt die tatsächlich vorhergesagte Menge; der Anteil der `MEHRERE`-Antworten wird berichtet. A18 bleibt bestehen und wird nur präzisiert: ungültig sind mehrere IDs ohne Ausweis als `MEHRERE`. Der Prompt-Wortlaut folgt in Freeze 2 | Die Regel „einer der Gold-Senses“ belohnte bei einer Mengenantwort das Absichern. Die MFS-Baseline nennt immer genau einen Sense, sonst misst der McNemar-Test teils das Antwortformat. Das LLM hat dieselben Optionen wie die Menschen (Alternative Annotator Test, Calderon et al. 2025). Verworfen: Bewertung nach exakter Menge; primär genau eine ID mit `MEHRERE` nur sekundär. Entscheidung Julia Hintersteiner, 2026-10-30 (Wahl „Ja, alle IDs im Gold“) | 2026-10-30 |
| A24 | (keine Abweichung von der Regel) Begründungen in Abschnitt 3 („Präpositionen und Adverbien … fehlen auch in den Vergleichsdatensätzen“) und Abschnitt 4.4, Punkt 4 („All-Words-Sets als Klumpenstichproben, Raganato et al. 2017“) | Abschnitt 3: Stütze nur noch für die Präpositionen; Adverbien sind in den englischen Datensätzen enthalten. Abschnitt 4.4: Raganato et al. nur für die Dokumentzahlen und die Streuung der MFS angeführt, die Deutung als Klumpenstichprobe als eigene gekennzeichnet. Ausschluss von PRP und ADV und Obergrenze pro Text unverändert | Raganato et al. (2017, S. 101, Tab. 1 bis 3) nennen 3 / 3 / 3 / 13 / 4 Dokumente und enthalten Adverbien (346 Instanzen in der Verkettung), sprechen aber nirgends von Klumpenstichproben oder dokumentabhängiger MFS. Vorschläge V4 und V7 aus der Literaturauswertung vom 2026-10-30; Belege aus nicht gegengelesenen KI-Zusammenfassungen. Gleiche Korrektur in LITERATUR-STICHPROBE.md (Prüfstatus ○ für „MFS hängt vom Dokument ab“, Navigli et al. 2007 nicht geprüft). Entscheidung Julia Hintersteiner, 2026-10-30 | 2026-10-30 |
| A25 | Aufschlüsselung der Auswertung (Abschnitt 9.1, Punkt 6): Polysemiegrad, Wortart, Frequenzband, Domäne, Obergattungsgruppe, Sicherheit | Zusätzlich nach Herkunft der Wortart (Lexikon oder Token); in Abschnitt 3 festgehalten, dass die Schichtungsvariable „Wortart“ Lemma- und Beleg-Wortart mischt | Die Beleg-Wortart kann von der Bedeutung abhängen (HiTS zu *guot*, Dipper et al. 2013, S. 92 bis 95, 107). Das Manifest führt die Herkunft schon (Abschnitt 4.9). Vorschlag V6 vom 2026-10-30; Belege aus nicht gegengelesenen KI-Zusammenfassungen. Entscheidung Julia Hintersteiner, 2026-10-30 | 2026-10-30 |
| A26 | Freeze 2, LLM-Konfiguration (Abschnitt 4.10): Modell und Version, Prompt, Temperatur, Anzahl der Läufe | Zusätzlich: API-Zugang mit exakter Snapshot-ID, Abfragedatum, maximale Antwortlänge, alle Sampling-Parameter ausdrücklich (Temperatur, top_p, top_k), Kartenformat und Kontextumfang, Sprachumfang laut Modellkarte; Angaben im Artikeltext | Ohne diese Angaben sind Läufe nicht reproduzierbar; Weboberflächen wechseln Modelle und verbergen System-Prompts (Scholger & Bleier 2026; Yae et al. 2025; Basile et al. 2025; Belege aus nicht gegengelesenen KI-Zusammenfassungen). `PROMPT-LOG.md` protokolliert Modell, Parameter und Zeitpunkt schon. Vorschlag V8 vom 2026-10-30. Entscheidung Julia Hintersteiner, 2026-10-30 | 2026-10-30 |
| A27 | Darbietung für das LLM (Abschnitt 4.10): „ob das LLM dieselben Karten sieht wie die Menschen“ offen | Grundsatz: gleiche Darbietung für Mensch und LLM. Das LLM sieht dieselbe pro Item gemischte Kartenreihenfolge, protokolliert; Zusatzinformation (Werktitel, Notizen an Senses, Sprachstufe, Epoche) ist für beide gleich. Was konkret auf die Karte kommt, bleibt offener Punkt 4 | Gemischte Optionen senken die Werte, Positionsverzerrung ist beschrieben (Meconi et al. 2025, S. 33902; Yang et al. 2024, S. 21; Belege aus nicht gegengelesenen KI-Zusammenfassungen). Trifft die Verzerrung nur eine Seite, hängt der Vergleich an ihr. Vorschläge V11 und V12 vom 2026-10-30. Entscheidung Julia Hintersteiner, 2026-10-30 | 2026-10-30 |
| A28 | Pilot-Pool (Abschnitt 4.2): Entwicklung der LLM-Konfiguration (A17) | Am Pilot-Pool darf zusätzlich eine Kontrollbedingung ohne Kontext (nur Lemma und Karten) laufen; nur im Pilot | Zeigt, wie viel das LLM aus den Karten allein errät (Matusch 2025, Tab. 4.6; Deutung der KI-Zusammenfassung, nicht der Arbeit). Vorschlag V13 vom 2026-10-30. Entscheidung Julia Hintersteiner, 2026-10-30 | 2026-10-30 |
| A29 | `MEHRERE`-Antwort des LLM mit nur einer ID (Abschnitt 9.2): nicht geregelt (offen nach A23) | Gilt als ungültige Antwort (eigene Kategorie, im primären gepaarten Vergleich falsch, wie A18) | Wie bei den Menschen verlangt `MEHRERE` mindestens zwei Sense-IDs (Abschnitt 6); dieselben Optionen für Mensch und LLM (A23). Entscheidung Julia Hintersteiner, 2026-10-30 („ok ja wie bei den menschen passt“ auf den Vorschlag der Hauptsitzung, eine solche Antwort als ungültig zu werten) | 2026-10-30 |
| A30 | Pilot-Pool (Abschnitt 4.2): „ca. 100 Items, Lemmata disjunkt“, Ziehungsverfahren nicht festgelegt | **Vorläufig, Bestätigung durch Julia Hintersteiner ausstehend:** 36 Zellen × 3 = 108 Items, je Zelle 1 aus D1 (sonst D0) und 2 aus D0; Stufe 1 Paar aus Lemma und Wortart gleich wahrscheinlich, jedes Lemma höchstens einmal; Stufe 2 Token mit Gewicht T_G^(-1/2); Obergrenze 3 pro Text (Historiografie 5) nur innerhalb des Pools; Seed 20261112. Runde 0: 15 Items, einfache Zufallsauswahl (Seed „20261112-runde0“). Alle 108 Pool-Lemmata werden bei der späteren Ziehung von Haupt- und Panelstichprobe ausgeschlossen, in jeder Wortart. Erweiterter Kontext 8 Verse bzw. 80 Tokens je Seite. Hilfsmittelregel der Kurzanleitung v0 (Wörterbücher wie Lexer und BMZ erlaubt und im Kommentar zu vermerken; nicht erlaubt: MHDBDB-Website und Repository, KI-Werkzeuge; Belege bis zur Auswertung nicht besprechen) | Das Hauptverfahren (Abschnitt 4.4) im Kleinen, damit der Pilot dieselben Zellen berührt; 108 statt „ca. 100“ durch 36 × 3. Gezogen (Skript `pilot/pilot_ziehen.py`, Manifest `pilot/manifest-pilot.json`, nachgelesen am 2026-11-12): 108 Items aus 69 Texten, 36 aus D1 ohne D1-Ersatz, höchstens 5 Items aus einem Text, Kontext Vers 81 und Prosa 27; Gruppen Großepik 34, Lyrik 22, Geistliche Literatur 16, Kurzdichtung 12, Historiografie 12, Lehrdichtung 6, Fach- und Rechtsliteratur 6. Zweimal gezogen (vor und nach einer Darstellungskorrektur), laut Hauptsitzung identische Items (übernommen, nicht nachgemessen). Die Größe des erweiterten Kontexts hat die Hauptsitzung gewählt; Julia hat nur den Standardausschnitt bestätigt (offener Punkt 4). Die Hilfsmittelregel ist ein Vorschlag der Hauptsitzung. Entschieden von Julia sind nur die Punkte in Abschnitt 4.2 (ganzer Pool, 15 Items für Runde 0) und Abschnitt 12 (Punkte 4 und 18) | 2026-11-12 |
| A31 | Annotation im Pilot (Abschnitte 6 und 7): bisher direkt am Inventar, d. h. Karten sofort sichtbar | **Vorschlag und Entscheidung getrennt.** Entschieden (Julia Hintersteiner, 2026-11-13): im Pilot zuerst eine eigene Lesart bei verdeckten Karten, dann die Kartenwahl („B im Pilot, Runde 0 auf morgen verschieben“); Runde 0 verschoben vom 2026-11-13 auf 2026-11-14. Als Grundlage mit vorgeschlagen von der Hauptsitzung, von Julia nur mit „B im Pilot“ wörtlich bestätigt (Weg A): die Inventarbindung im Protokoll offen benennen (Gold ist relativ zum MHDBDB-Inventar; die Übereinstimmung misst die Reproduzierbarkeit des Instruments aus Richtlinien, Inventar und Darstellung, nicht Wahrheit; „unabhängig“ heißt blind gegeneinander und gegenüber Silber und LLM). Nicht entschieden: B in der Hauptrunde (nach dem Pilot, Julia); Weg C (inventarfreie Aufgabe, Bedeutungsnähe von Belegpaaren wie DURel, Erk et al. 2013) als Kandidat für später (Beitrag V). Umsetzung `pilot/annotation.template.html` mit Ablauf `lesart-zuerst` als Standard, `--ablauf direkt` baubar, Kurzanleitung v0.2; zusätzlich auf Wunsch Julias (2026-11-13) Karten oberhalb des Status, auch ohne Status wählbar, Kurzanleitung leichter formuliert (v0.1) | Julia, 2026-11-13: „wenn ich bedeutungen vorgebe zum lemma ist das nicht schon beeinflussung? es geht ja darum einen unabhängigen goldstandard aus einem inter-annotator-agreement zu erstellen nicht?“. Die Vorgabe des Inventars kann die Lesart lenken (Ankereffekt); der Lesart-Schritt macht diesen Einfluss messbar und stützt die These aus dem Exposé zur Inventarabhängigkeit. Literaturprüfung noch offen (Kilgarriff 1997, Literatur zum Ankereffekt vorgegebener Antwortoptionen; bisher nicht in `literatur/`), deshalb keine Literaturbegründung. Umsetzung in Commits `c66cbaaab`, `55619c861`, `4c6213cb5`; Browsertest 80 Prüfungen, Chromium, Edge, Chrome, WebKit 80/80, Firefox 78/80 (zwei Prüfungen mit Eingaben in einen Tab im Hintergrund), laut Hauptsitzung (übernommen, nicht nachgemessen). A30 (vorläufig) bleibt unverändert; Runde-0-Termin dort überholt durch A31 | 2026-11-13 |
| A32 | Pilot (Abschnitt 7, Schritt 2): ca. 50 Items, Schwelle nur als Vorschlag (α ≥ 0,80, Untergrenze 0,67); dritte Person offen (Abschnitt 12, Punkt 2) | Runden zu 25 frischen Items nach Runde 0; Stoppregel mit drei Bereichen (α ≥ 0,80 einfrieren; 0,67 bis unter 0,80 nachschärfen, nach der letzten Poolrunde trotzdem einfrieren und als Einschränkung berichten; unter 0,67 nach der letzten Poolrunde keine Hauptrunde, Instrument ändern, neue Pilotitems); gemessen pro Runde vor jeder Besprechung mit α nominal auf dem ganzen Label; Runde 0 ohne Schwelle; dritte Person: KZW vorgesehen, noch nicht angefragt | Schwelle vor Runde 0 festgelegt, damit sie nicht nach dem ersten Ergebnis angepasst wird. Der Pool (108) trägt Runde 0 und drei Runden zu 25. α nominal ist für die Stoppregel die strengere Wahl; das berichtete Hauptmaß der Übereinstimmung bleibt α mit MASI-Distanz (Abschnitt 9, A8), die Hauptsitzung hatte A8 beim Vorschlag übersehen und „ganzes Label exakt als Hauptmaß“ genannt, gemeint ist hier nur das Maß der Stoppregel. Wilson-Intervall für 80 % bei 25 Items von der Hauptsitzung gerechnet (etwa 61 bis 91 %). Entscheidung Julia Hintersteiner, 2026-11-13 („ok dann 25 je runde“; „die dritte person ist katharina“; „ja die schwelle passt so“ auf das Schema der Hauptsitzung). **Ergänzung vom 2026-11-16 (V52, V53): Die Schwelle ist eine Projektregel, die nicht aus der Literatur folgt; Begründung „α nahe an der Rohübereinstimmung“ belegt und eingegrenzt, siehe A34** | 2026-11-13 |
| A33 | Übereinstimmungsmaße (Abschnitt 9.1): „α mit MASI-Distanz (Passonneau 2006)“ ohne Formel; „α nominal als untere Schranke“; für das Zufallsmodell pro Lemma „keinen etablierten Standard gefunden“; Zwei-Ebenen-Auswertung ohne Weg zur groben Ebene; keine Einschränkungen genannt | Abstand als 1 − J·M nach Passonneau 2006 (S. 834 bis 835) ausgeschrieben, mit Tabelle typischer Fälle und dem Hinweis, dass Artstein & Poesio 2008 (S. 584) d_P × d_J geben; α nominal als „strengere Variante“ (Gegenbeispiel Passonneau 2006, Tab. 1); Vorbilder für das Zufallsmodell pro Wort genannt (Ng et al. 1999; Passonneau et al. 2010), Wahl begründet; Einschränkungen: Krippendorffs Stichprobenregel nicht erfüllbar, zwei Annotierende statt drei oder mehr (Artstein & Poesio 2008, S. 575); Zusammenfallstufe der Senses vorab nach der Regel von Vial et al. 2019 aus dem Zahlencode (B11), Vial nur bedingt als Vorbild, Supersenses und Basic Level Concepts zu beschaffen | Für {s1} gegen {s1, s2} ergibt die eine Formel 2/3, die andere 1/6; ohne Festlegung wäre das Hauptmaß nicht reproduzierbar. Belege aus nicht gegengelesenen KI-Zusammenfassungen; Rechenwerte der Tabelle am 2026-11-16 nachgerechnet. V50, V51, V56, V57, V63. Entscheidung Julia Hintersteiner, 2026-11-16 („A wie empfohlen, B alle übernehmen“) | 2026-11-16 |
| A34 | Pilot und Ablauf (Abschnitte 4.2, 4.10, 6, 7): Schwelle von A32 ohne Herkunft; Begründung „α nahe an der Rohübereinstimmung“ ohne Beleg; keine Regel für einen Ablaufwechsel zur Hauptrunde; Pilot-Auswertung nur als Gesamtwert; OntoNotes „90 % Rohübereinstimmung“ | Schwelle als Projektregel gekennzeichnet (Passonneau et al. 2006, S. 1951 raten im Pilot von absoluten Schwellen ab; Kilgarriff 1998, S. 11 stützt κ > 0,8); Mechanismus mit Artstein & Poesio 2008, S. 586 belegt (Diskursdeixis, andere Aufgabe), gepooltes α nicht mit WSD-Werten pro Wort vergleichbar (Ng et al. 1999); in Pilot und Hauptrunde wird die Rohübereinstimmung immer neben α berichtet, Literaturvergleiche laufen über sie; Ablaufwechsel zur Hauptrunde gilt als Abweichung und verlangt mindestens eine Pilotrunde im neuen Ablauf (Beck et al. 2024); Abweichungen im Pilot pro Lemma festhalten (Hovy et al. 2006); am Pilot-Pool für Freeze 2 Karten mit und ohne Oberbegriffspfad für das LLM (Ghizzota et al. 2026); „Roh“ bei OntoNotes gestrichen | A32 bleibt bestehen. Vorab festgelegt ist besser als nachträglich; die Schwelle ist ehrlich als Projektregel gekennzeichnet. Belege aus nicht gegengelesenen KI-Zusammenfassungen. V52, V53, V60, V62, V66, K7. Entscheidung Julia Hintersteiner, 2026-11-16 („A wie empfohlen, B alle übernehmen“); V61 (monoseme Kontroll-Lemmata) ausdrücklich nicht übernommen | 2026-11-16 |
| A35 | Auswertung gegen Gold, Silber, LLM (Abschnitt 9.2): menschliche IAA „ist die Obergrenze“; kein Bericht des Abstands zur Baseline; keine Sekundärauswertungen vorgemerkt | Abstand zwischen menschlicher Rohübereinstimmung und MFS auf denselben Items wird berichtet (Gale et al. 1992, S. 254, „dynamic range“); menschliche IAA nur als Referenzwert, Obergrenze ist die Replizierbarkeit zwischen Teams (Kilgarriff 2001, S. 20), fehlende Replizierbarkeitsmessung als Grenze; drei Sekundärauswertungen für Freeze 2 vorgemerkt (nach Übereinstimmung vor der Adjudikation, nur „sicher“ und gleich gelabelte Items, nach Position in der Sitzung; Plank 2022; Passonneau & Carpenter 2014; Beck et al. 2024) | Keine Änderung der Primärregeln. Belege aus nicht gegengelesenen KI-Zusammenfassungen. V54, V55, V70. Entscheidung Julia Hintersteiner, 2026-11-16 („A wie empfohlen, B alle übernehmen“) | 2026-11-16 |
| A36 | Adjudikation und Veröffentlichung (Abschnitt 7, Schritte 6 und 7): Ursachencodes „angelehnt an Barteld et al. (2015)“ mit fünf Codes; Adjudikation blind nur gegenüber der Herkunft der Labels; Labels vor der Adjudikation mitveröffentlicht | Ursachencodes nach Ihden et al. 2015 mit den drei Kategorien der Vorlage (fehlende Regeln; Abweichungen trotz bestehender Regeln; unterschiedliches Textverständnis); Inventarlücke, Editions- oder Normalisierungseffekt und echte Textambiguität als eigene Erweiterungen gekennzeichnet; Adjudikation auch blind gegenüber Silber und LLM-Ausgabe (Berzak et al. 2016); Labels pro Person mit Kennung veröffentlicht, die Einwilligung (offener Punkt 14) muss das abdecken (Prabhakaran et al. 2021); Lesarten aus A31 als Rohdaten mitveröffentlicht (Plank 2022) | Die bisherigen Codes „Versehen“ und „echte Textambiguität“ passten nicht zur Vorlage (Ihden et al. 2015, Folien 16, 19). Belege aus nicht gegengelesenen KI-Zusammenfassungen. V59, V67, V68, V69. Entscheidung Julia Hintersteiner, 2026-11-16 („A wie empfohlen, B alle übernehmen“) | 2026-11-16 |
| A37 | Kontamination (Abschnitte 4.10 und 10): Manifest mit Token-IDs öffentlich; Ausschlusszusage der API-Anbieter nicht verlangt; Canary-String Jacovi et al. 2023 zugeschrieben | Token-IDs der Hauptstichprobe bleiben bis zum Ende der LLM-Läufe privat, öffentlich nur die Prüfsumme des Manifests; für den Pilot ein Hinweis im künftigen Datasheet (offener Punkt 24); Freeze 2 dokumentiert die Ausschlusszusage der API-Anbieter mit Datum; Auswertungsskripte geben Labels nie in eine KI-Sitzung aus, nur Kennzahlen (auch Claude Code); Canary-String als eigene Maßnahme ohne Literaturbeleg gekennzeichnet, die Zuschreibung an Jacovi et al. und Sainz et al. (K9) entfällt | Jacovi et al. 2023 (S. 5076 bis 5078) und Sainz et al. 2023 (S. 10777); beide Werke erwähnen keinen Canary-String (Textebene durchsucht). V72, V75, K9. Entscheidung Julia Hintersteiner, 2026-11-16 („A wie empfohlen, B alle übernehmen“); V71, V73, V74, V76 und V77 bleiben offen | 2026-11-16 |
| A38 | (keine Abweichung von der Regel) Zitatkorrekturen in `PROTOKOLL.md` (Abschnitte 4.3, 4.4, 7, 9.1, 9.2, 10), `LITERATUR-IAA.md`, `LITERATUR-STICHPROBE.md` und `DMP.md` | K1: Kilgarriff 1998 schichtet nach Frequenz und Polysemie (S. 15 bis 16), Schwierigkeit belegt Kilgarriff & Rosenzweig 2000; K2: Gale et al. 1992 stützen „1 Token pro Paar“ und Panelregel, nicht die Obergrenze pro Text (51/54, 94 %); K3: Kilgarriff 1998 empfiehlt das lexikalische Modell nur für explorative Evaluation, „80 bis 400 Belege“ pro Aufgabe; K4 und K6: Zeilen zu Ng et al., Mihalcea et al., Passonneau et al. 2006, Hovy et al. 2006, Ihden et al., Ghinassi et al., Ghizzota et al. und SemEval Latein auf die Quelle begrenzt; K5: Artstein & Poesio S. 591 nur sinngemäß; K7: „Roh“ bei OntoNotes gestrichen; K8: Passonneau & Carpenter nur zu zufallskorrigierter Übereinstimmung; K9: Canary-String; K10: Hovy 2010 trägt die Aussage nicht; K11: Loureiro et al. nur Sense-Zahl und Systemleistung; K12: Erk et al. 2013 mischen zwei Maße, SemEval-2020 nach der begutachteten Fassung; K13: Navigli et al. 2007 Streuung gemessen, Erklärung Vermutung; K14: Maru et al. 2022 Bezugsmengen; K15: Mihalcea et al. 2004 ganzer OMWE-Bestand; K16: Resnik & Yarowsky 1997 nicht Quelle der Dice-Teilwertung | Regeln und Designentscheidungen bleiben unverändert; berichtigt werden nur Zitate und Prüfstatus, geprüft an den nicht gegengelesenen KI-Zusammenfassungen in `literatur/zusammenfassungen/`. Prüfstatus ○ wurde nur dort auf ✔ gehoben, wo die Liste es ausdrücklich vorsah (K4, K8, K12, K13). Entscheidung Julia Hintersteiner, 2026-11-16 („A wie empfohlen, B alle übernehmen“) | 2026-11-16 |
| A39 | Korpusstand (Abschnitt 3, Neumessung; offener Punkt 6): „Kein Upstream-Merge vorher“ (Festlegung vom 2026-11-12, A30-Umfeld) | Upstream `d3bdfe738` (2026-11-19) wird vollständig in den Fork gemergt (Code, Doku, Daten, Merge-Commit `ba6a3280a`); der Goldstandard bleibt auf Korpusstand Upstream `a938559dc` vom 2026-10-14; Ziehungen und Ausschlussberechnung laufen künftig in einem Worktree auf `a938559dc` | Messung der Hauptsitzung (Claude Opus 5.5, 2026-11-20): 155 Korpusdateien und 4 Normdateien (`concepts.xml`, `lexicon.xml`, `variants.xml`, `works.xml`) zwischen `a938559dc` und `ce68c2783` geändert (zwischen `ce68c2783` und `d3bdfe738` keine weitere Korpus- oder Normdatenänderung). Von den 69 Pilot-Texten sind 28 upstream geändert; für alle 108 Pilot-Items sind `<w>` (`@lemmaRef`, `@ana`, `@pos`, Text), die ±30 `<w>` um das Item und der `lexicon.xml`-Eintrag des Lemmas gleich. `concepts.xml`: nur ein neuer Begriff `concept_14101100`, nichts geändert. `works.xml`: u. a. FLG/FLG1 (Titel, Textumfang, neue Gattungszeiger bei einem der beiden), HOF/VDH Anonym als zweiter Autor; FLG1 hat das Pilot-Item P101, `obergattungen/texte.csv` bleibt auf `a938559dc` gültig. `pilot_ziehen.py` bricht im Haupt-Checkout ab (Korpusprüfung). Nachgemessen vom `protokollant`: 155 Dateien (`git diff --stat`), 4 Normdateien, 166 Commits bis `ce68c2783` (`git rev-list`); bis zum gemergten Kopf `d3bdfe738` sind es 167 (Hauptsitzung, `git rev-list --count a938559dc..d3bdfe738`); Drift-Skript siehe Rückmeldung. Entscheidung Julia Hintersteiner, 2026-11-20, per Auswahldialog, Antwort „Ganz mergen (Empf.)“ auf die Frage, ob trotz der Festlegung vom 2026-11-12 gemergt werden soll. Optionstext: „Merge committen und pushen, Goldstandard bleibt auf a938559dc. Ich lasse den protokollant den Eintrag schreiben: Abweichungslog A39, §3-Satz anpassen, Drift-Messung, Hinweis ‚Ziehungen aus einem Worktree auf a938559dc‘.“ | 2026-11-20 |
| A40 | Zweite annotierende Person (DMP, Abschnitt 4; offener Punkt 14): vorgesehen war eine „informierte Einwilligung“ der zweiten Person zu Protokollierung und Veröffentlichung; Verweildauern „nur aggregiert“ (DMP) | Statt einer Einwilligung gilt der Arbeitsauftrag: Die zweite Person annotiert als Mitarbeiter:in der MHDBDB im Auftrag von Katharina Zeppezauer-Wachauer. Dazu ein Informationsblatt mit Absprache, `INFOBLATT-ANNOTATION.md` (Entwurf vom 2026-11-20): Katharina bestätigt den Auftrag, die zweite Person bestätigt den Erhalt und wählt die Nennung, Julia sagt die Behandlung zu. Die Aufzeichnung der Verweildauern bleibt (Prüfung auf Ermüdung und Drift, Abschnitt 7, Schritt 4); im Blatt steht die Zusage, sie nur gesammelt auszuwerten, nie zur Leistungsbewertung, und nur aggregiert zu veröffentlichen | Begründung der Hauptsitzung (nicht juristisch geprüft): Die Einwilligung im DMP stammte aus der Annahme, die zweite Person sei extern; bei Beschäftigten ist eine Einwilligung gegenüber der Vorgesetzten kaum freiwillig, Grundlage ist dann das Dienstverhältnis bzw. die Forschungsaufgabe. Es bleiben die Informationspflicht (Art. 13 DSGVO), die Frage, ob Zeitdaten je Person arbeitsrechtlich eine Kontrollmaßnahme sind (deshalb die Zusage), und Veröffentlichung und Nennung. Rechtsgrundlage und verantwortliche Stelle sind von der Datenschutzstelle zu bestätigen (im Blatt als [offen] markiert). Bei zwei namentlich genannten Annotierenden schützt ein Pseudonym kaum; A36 („pro Person mit Kennung“) bleibt unverändert, das Blatt sagt das offen. Entscheidungen Julia Hintersteiner, 2026-11-20. (1) Im Chat: „warum brauchen wir alans einwilligung? alan ist mitarbeiter der mhdbdb. katharina hat ihm als chefin den arbeitsauftrag erteilt den goldstandard mit mir zu machen“; danach per Auswahldialog „Infoblatt + Absprache (Empf.)“, Optionstext: „Entwurf als Datei; Katharina bestätigt den Auftrag, Alan bestätigt den Erhalt und wählt die Nennung. DMP §4 und offener Punkt 14 werden per protokollant angepasst (neuer A-Eintrag).“ (2) Per Auswahldialog „Zusage: nur aggregiert (Empf.)“ auf die Frage nach den Verweildauern, Optionstext: „Aufzeichnung bleibt (für die Prüfung auf Ermüdung und Drift, Protokoll §7.4); im Infoblatt die Zusage: nur gesammelt ausgewertet, nie zur Leistungsbewertung, Veröffentlichung nur aggregiert.“ | 2026-11-20 |
| A41 | Abschnitt 9.1 bestimmte die Sense-Ebene widersprüchlich: erster Satz „nur Items, bei denen beide `SENSE` oder `MEHRERE` vergeben haben“, zugleich sollte `KEINE_PASST` als eigene Kategorie eingehen; `LEMMA_FALSCH` kam nicht vor | Sense-Ebene = Items, bei denen beide `SENSE`, `MEHRERE` oder `KEINE_PASST` vergeben haben. `KEINE_PASST` geht als eigene Kategorie, d. h. als Menge {KEINE_PASST}, in MASI und α nominal ein; `SENSE` gegen `KEINE_PASST` ist damit eine volle Abweichung (Abstand 1). `KONTEXT_UNZUREICHEND` und `TEXT_DEFEKT` bleiben fehlende Werte; `LEMMA_FALSCH` war offen und ist mit A42 entschieden | Anlass: Review des Auswertungsskripts `goldstandard/pilot/auswerten.py` (`reviewer`, 2026-11-20), der den Widerspruch zwischen dem ersten Satz und der Behandlung von `KEINE_PASST` in Abschnitt 9.1 nachgemessen hat. Entscheidung Julia Hintersteiner, 2026-11-20, im Chat, wörtlich: „KEINE_PASST zählt als eigene Kategorie mit“. Abschnitt 9.2 (LLM-Vergleich) ist nicht betroffen: dort gehen `KEINE_PASST`-Items bewusst nicht in die Genauigkeit ein und werden gesondert berichtet | 2026-11-20 |
| A42 | Offener Punkt 25: Behandlung von `LEMMA_FALSCH` auf der Sense-Ebene (Abschnitt 9.1) war nicht geregelt; das Auswertungsskript zählte es vorläufig als fehlenden Wert | Sense-Ebene = Items, bei denen beide `SENSE`, `MEHRERE`, `KEINE_PASST` oder `LEMMA_FALSCH` vergeben haben. `LEMMA_FALSCH` geht wie `KEINE_PASST` als eigene Kategorie, d. h. als Menge {LEMMA_FALSCH}, in MASI und α ein. Nur `KONTEXT_UNZUREICHEND` und `TEXT_DEFEKT` bleiben fehlende Werte | Entscheidung Julia Hintersteiner, 2026-11-20, im Chat, wörtlich: „LEMMA_FALSCH zählt auch als eigene Kategorie mit“. Ergänzt A41. Abschnitt 9.2 wurde nicht geprüft und nicht geändert | 2026-11-20 |

## 12. Offene Punkte

1. ~~Silber-Aufteilung je Zelle~~: entschieden am 2026-10-16, Domäne D1 mit 30 % (Abschnitt 4.4).
2. **Dritte Person** für die Prüfung der Adjudikation (Abschnitt 7, Schritt 6): **Teilstand 2026-11-13:** vorgesehen ist KZW (A32), Anfrage und Zusage stehen aus. **Offen:** wer adjudiziert selbst, Julia und Alan gemeinsam im Gespräch oder die dritte Person?
3. **Pilotgröße** und Alans Zeitbudget (bestimmt, ob ca. 510 Items realistisch sind). **Teilstand 2026-11-13:** Rundengröße 25 Items nach Runde 0 (A32); Alans Zeitbudget offen.
4. **Kontextausschnitt:** Standard entschieden am 2026-11-12 (Julia Hintersteiner: „ja der kontext passt“, auf den Vorschlag 2 Verse davor und danach, bei Prosa ±20 Tokens, erweiterbar, mit Werktitel). **Offen:** Größe des erweiterten Kontexts (Entwurf der Hauptsitzung: 8 Verse bzw. 80 Tokens je Seite, nicht bestätigt, A30).
5. ~~Ausschlussliste der LLM-berührten Tokens bauen~~: erledigt am 2026-10-08, Regel bestätigt am 2026-10-16 (Abschnitt 3, Punkt 1).
6. ~~Korpusstand fürs Einfrieren~~: entschieden am 2026-11-12, Upstream `a938559dc` vom 2026-10-14 für Pilot und ganzen Goldstandard, kein Upstream-Merge vorher (Julia Hintersteiner, Abschnitt 3, Neumessung). **Ergänzung 2026-11-20 (A39):** der Upstream ist inzwischen gemergt, der Goldstandard bleibt auf `a938559dc`; Ziehungen und Ausschlussberechnung nur in einem Worktree auf diesem Stand (Abschnitt 3, Stand vom 2026-11-20).
7. **Teststärke:** grob gerechnet (Abschnitt 4.7); Anteil diskordanter Paare im Pilot schätzen, dann N vor Freeze 2 bestätigen.
8. ~~Obergattungsgruppen prüfen und festlegen~~: entschieden am 2026-10-30 ([OBERGATTUNGEN.md](OBERGATTUNGEN.md), Abschnitt 5; Abschnitt 4.8).
9. **Datierung und Vers/Prosa:** Sollen sie als weitere Ausgleichsmerkmale dienen? Dann braucht es eine manuelle Zuordnung pro Text (z. B. Jahrhundert über den Handschriftencensus, bei 323 Werken verlinkt).
10. ~~Obergrenze an Tokens pro Text~~: 3, bestätigt am 2026-10-16 (Abschnitt 4.4).
11. ~~Schwelle für das Ende des Pilots~~: entschieden am 2026-11-13, vor Runde 0 (A32, Abschnitt 7, Schritt 2).
12. **Grobe Ebene des Begriffssystems** für die Zwei-Ebenen-Auswertung festlegen (welche Oberbegriffsstufe). **Teilstand 2026-11-16 (A33):** Die Stufe, auf der die Senses eines Lemmas zusammenfallen, wird vorab nach der Regel von Vial et al. (2019, S. 111) aus dem Zahlencode (B11) berechnet; Supersenses und Basic Level Concepts als Vorbild sind zu beschaffen. Welche Stufe gilt, bleibt offen.
13. **Ausschlüsse 2 und 3** (Abschnitt 3) auf die neue Wortartregel und das ganze Korpus umrechnen. Ausschluss 4 entfällt (A19); die Auswahlregel für die ca. 30 von Hand einzuordnenden Tokens mit Markierung `pos_abweichend` ist entschieden (einfache Zufallsauswahl, A22), die Ziehung selbst steht aus. **Teilstand 2026-11-12:** Ausschlüsse 2 und 3 sind auf das ganze Korpus (Stand `a938559dc`) umgerechnet (Abschnitt 3, Neumessung: 22 Lemmata mit 1.215 Tokens, 2 Lemmata mit 0 Tokens); die Ziehung der 30 Tokens steht weiter aus.
14. **Arbeitsauftrag und Informationsblatt der zweiten Person** (statt der früher vorgesehenen Einwilligung von Alan; DMP, Abschnitt 4; A40, Entscheidung Julia Hintersteiner, 2026-11-20). `INFOBLATT-ANNOTATION.md` liegt als Entwurf vom 2026-11-20 vor, von Julia noch nicht gegengelesen, mehrere Stellen [offen]. **Es stehen aus:** die Bestätigung des Arbeitsauftrags durch Katharina Zeppezauer-Wachauer, die Bestätigung des Erhalts und die Wahl der Nennung durch die zweite Person, Julias Zusage; außerdem die Bestätigung von Rechtsgrundlage und verantwortlicher Stelle durch die Datenschutzstelle (Begründung der Hauptsitzung, nicht juristisch geprüft) sowie Ablageweg, Aufbewahrungsdauer und Nennung. **Ergänzung 2026-11-16 (A36):** Die Grundlage muss die Veröffentlichung der Labels pro Person mit Kennung, der Lesarten und der Labels vor der Adjudikation abdecken; bei zwei namentlich genannten Annotierenden schützt die Kennung kaum vor Zuordnung.
15. **Privates Repository** anlegen und eine zweite Sicherungskopie festlegen (DMP, Abschnitt 3). **Teilstand 2026-11-26:** Besprechungsdatei und eine Kopie beider Runde-0-Exporte liegen lokal außerhalb des Repos als Zwischenablage (Prüfsummen der Kopien gleich den Originalen, laut Hauptsitzung; Entscheidung Julia Hintersteiner, 2026-11-26, Auswahldialog „Eigener Ordner (Empf.)“). Das ersetzt das private Repository und die zweite Sicherung nicht.
16. **Verschmelzungen (Ausschluss 5):** Urteile beider Prüfrunden von Julia gegenlesen lassen; Verschmelzungen ohne verlinkte Bestandteile sind nicht erfasst und nicht gemessen (Abschnitt 3, Einschränkung).
17. **Bestätigung des Pilotdesigns und der Hilfsmittelregel** (A30): 108 Items, Zellen, Ausschluss der Pool-Lemmata aus Haupt- und Panelstichprobe, Größe des erweiterten Kontexts, Wortlaut der Kurzanleitung v0 mit ihrer Hilfsmittelregel. **Teilstand 2026-11-13:** Julia Hintersteiner hat die Kurzanleitung (v0.2) gegengelesen und die Hilfsmittelregel bestätigt; auf ihre Entscheidung („ja alle vier rein, vorschlag raus“ auf vier Vorschläge der Hauptsitzung) gilt seit 2026-11-13 die Kurzanleitung v0.3: (1) Zusatz „(Vorschlag)“ bei den Hilfsmitteln gestrichen; (2) „Mehrere passen“ neu gefasst als „zwei oder mehr Karten treffen zu, und die Stelle lässt keine Wahl zwischen ihnen zu“, damit es sich von „Kontext reicht nicht“ abhebt; (3) Hinweis, nicht in einem privaten Fenster zu arbeiten und zwischendurch als JSON zu sichern; (4) Erklärung der Sicherheitsstufen (sicher: keine andere Lösung kommt ernsthaft in Frage; eher sicher: eine andere Lösung ist denkbar, aber weniger wahrscheinlich; unsicher: eine andere Lösung wäre ebenso gut möglich). Den Wortlaut von (4) hat die Hauptsitzung nach der Entscheidung formuliert, von Julia noch nicht gegengelesen. Browsertest nach dem Neubau 80 von 80 Prüfungen bestanden (Chromium, Hauptsitzung). Weiter offen: 108 Items, Zellen, Ausschluss der Pool-Lemmata, Größe des erweiterten Kontexts.
18. ~~Pilotinterface~~: entschieden am 2026-11-12 (Julia Hintersteiner, Antworten im Fragedialog; betrifft `INTERFACE-BESTAND.md`, Abschnitt 5, Punkte 1, 3, 4): Ein Beleg gilt erst nach Klick auf „Festhalten“ als entschieden, eine Änderung danach setzt zurück („festhalten ja“); einen Zustand „geprüft, bleibt offen“ gibt es nicht („nein“); die Belege für die Runde werden zufällig ausgewählt („zufällig“). Runde 0 wird unabhängig annotiert, jede Person für sich („jede person für sich, deswegen auch das interface für die überprüfung“). Julia versteht unter „Disambiguieren“ den menschlichen Goldstandard (Julia und Alan); die LLM-Disambiguierung kommt später bzw. parallel. Das Pilotinterface wird als HTML-Datei pro Person gebaut (Kennungen `julia` und `alan`, `pilot/annotation_bauen.py`).
19. **Darbietung für das LLM (A27, A31):** Soll das LLM im Pilot ebenfalls zuerst eine eigene Lesart formulieren und dann wählen („gleiche Darbietung für Mensch und LLM“)? Offen, gehört in Freeze 2.
20. **Auswertung der Lesarten (A31):** Wie sie ausgewertet werden (z. B. Zuordnung der Lesart zu einer Karte durch eine dritte Person blind, Anteil „Lesart passt zu keiner Karte“, Abweichung zwischen Lesart und gewählter Karte), ist vor dem Ende des Pilots festzulegen.
21. **Literaturprüfung durch `quellen`** vor einer Begründung im Protokoll: Kilgarriff 1997 („I don't believe in word senses“) und Literatur zum Ankereffekt vorgegebener Antwortoptionen; bisher nicht in `literatur/`.
22. **Lesart-Schritt in der Hauptrunde (A31):** ganz, als Teilstichprobe (z. B. Lemma-Panel) oder gar nicht; Entscheidung Julia Hintersteiner nach dem Pilot. Weg C (Bedeutungsnähe von Belegpaaren, DURel) bleibt Kandidat für später (Beitrag V), nicht entschieden. **Ergänzung 2026-11-16 (A34):** Ein Wechsel des Ablaufs gegenüber dem Pilot gilt als Abweichung und verlangt mindestens eine Pilotrunde im neuen Ablauf (Abschnitt 6).
23. **Regel für `MEHRERE` in den Richtlinien (V58):** Bei SENSEVAL waren Mehrfachantworten nur erlaubt, wenn eine Einzelantwort unwahr wäre (Kilgarriff 1998, S. 9); das ist strenger als die Kurzanleitung v0.3. Vergleichswert aus der Rechnung eines Laufs: in SENSEVAL-2 einigten sich etwa 6,8 % der Zweierfälle auf mehr als einen Tag (nicht nachgemessen). Entscheidung nach der Besprechung von Runde 0, nicht vorher (Julia Hintersteiner, 2026-11-16, „A wie empfohlen“). **Zahlenbefund Runde 0 (2026-11-26, nur Zahlen):** Alle 5 Items mit abweichendem Status haben `MEHRERE` auf mindestens einer Seite; Status gleich bei 10 von 15 Items. Entschieden ist nichts, die Besprechung steht aus.
24. **Hinweis im künftigen Datasheet zu den Pilotdaten (V72):** `pilot/items-pilot.json` liegt mit `xml_id` öffentlich im Fork, darüber ist für die D1-Items das Silber nachschlagbar; Pilotdaten sind Entwicklungsdaten, nicht Gold. `DATASHEET.md` gibt es noch nicht.
25. ~~`LEMMA_FALSCH` auf der Sense-Ebene~~: entschieden am 2026-11-20, eigene Kategorie wie `KEINE_PASST` (Julia Hintersteiner, A42, Abschnitt 9.1).
