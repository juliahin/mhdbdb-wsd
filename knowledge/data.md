# Daten für die WSD: was geprüft ist und was nur angenommen

**Stand:** 2026-10-23, Korpus-Commit `0357cb524` (667 Texte, 7.545.802 lemmatisierte Tokens).
**Zweck:** Grundlage für Protokoll, Datasheet und Richtlinien des Goldstandards
([../goldstandard/PROTOKOLL.md](../goldstandard/PROTOKOLL.md)). Jede Zahl hier ist gemessen; die
Skripte liegen in [`pruefskripte/`](pruefskripte/) und laufen aus dem Repo-Wurzelverzeichnis
(`inventarwandel.py` erwartet als Argument den Migrationsstand des Lexikons, erzeugt mit
`git show 0422429fc:authority-files/lexicon.xml`).
Wo etwas nur angenommen ist, steht es in Abschnitt 3.

## 1. Wie die Daten zusammenhängen

```
tei/<SIGLE>.tei.xml
  <w xml:id lemmaRef="lexicon.xml#lemma_N" pos="NOM ADJ" ana="lexicon.xml#lemma_N_sense_M"
     corresp="variants.xml#type_K">Wortform</w>
        │ lemmaRef                 │ ana (Silber)                 │ corresp
        ▼                          ▼                              ▼
authority-files/lexicon.xml        <sense xml:id ana="#type_K …"> variants.xml: Wortformen (Typen)
  <entry> <pos>* (ohne Bezug        <ptr target="concepts.xml#…"/>* pro Lemma, aus dem Korpus erzeugt
  zum einzelnen Sense)             (selten <note>, 1 <def>)
                                      │ ptr
                                      ▼
                              authority-files/concepts.xml: 567 Begriffe, deutscher und
                              englischer <term>, <ptr type="broader">, polyhierarchisch
TEI-Header: Textreihe (<category>) und Herkunft (<category ana="parent">) → genres.xml
```

- Ein Sense ist eine **Menge von Begriffszeigern**, keine Definition. Was Annotator:innen als
  Bedeutung sehen, ist diese Begriffsgruppe.
- Der Sense trägt selbst ein `@ana` mit einer **Typliste** (Wortformen). Das ist eine zweite,
  typbezogene Sense-Zuordnung neben dem Token-`@ana` (Befund B1).
- Wortarten hängen am Lemma, nicht am Sense. Ein Lemma kann bis zu sechs `<pos>` haben
  (10.160 von 43.710 Einträgen haben mehr als eine).
- `@lemmaRef` und `@ana` sind im Korpus nie mehrwertig (0 Fälle). Token-`@pos` ist es oft:
  2.139.984 lemmatisierte Tokens tragen zwei bis fünf Wortarten.

## 2. Geprüfte Annahmen

| Nr. | Bisherige Annahme | Befund am Original | Folge für den Goldstandard |
|---|---|---|---|
| B1 | Die Typliste an `<sense>` listet die Wortformen, mit denen der Sense belegt ist (so beschrieben in `docs/TEI-MODEL-AUTH-FILES.md`). | Falsch. Die Listen sind eine **Zerlegung**: Jeder Typ steht in höchstens einer Liste seines Lemmas (42.882 Typen polysemer Lemmata, alle genau einmal). Silber weicht davon ab: Bei 144.562 von 446.072 polysemen Silber-Tokens (32,4 %) steht der Typ in der Liste eines anderen Sense. Bei 7.409 Kombinationen aus Lemma und Typ mit gemischtem Silber ist der Listen-Sense nur in 3.965 (54 %) der Mehrheitssense; weder höchste (41 %) noch niedrigste Sense-ID (47 %) erklärt die Wahl. Die Listen stehen schon im Migrationsstand `0422429fc`. | Die Typliste ist eine typbezogene Vorbelegung unbekannter Herkunft (Abschnitt 3). Sie verrät für 1.340.983 der unannotierten polysemen Tokens (86 %) einen Sense und ist damit **Leckgefahr**: Weder Annotationsdatei noch LLM-Prompt dürfen `sense/@ana` enthalten. Zugleich ist sie ein Kandidat für eine zweite Baseline neben MFS. |
| B2 | Silber stammt von Menschen. | Für monoseme Lemmata nicht: 5.545.061 von 5.547.032 Tokens (99,96 %) tragen `@ana`, auch in sonst unannotierten Texten. Das entspricht der Regel „ein Sense, automatisch zuweisen" (DATA-MODEL.md, Phase 3). | Aussagen über Silber gelten nur für polyseme Lemmata. So rechnet das Protokoll bereits; im Datasheet ausdrücklich sagen. |
| B3 | Silber ist pro Beleg entschieden (Protokoll 2). | Bestätigt am Original. *wîsheit* (lemma_7542): Der Typ `wisheit` steht in der Liste von Sense 12319 (Autorität/Anordnung; Rechtswesen; Ordnungsmacht), 41 Silber-Tokens dieses Typs tragen aber Sense 12318 (Geist/Seele; Wissen …), 5 tragen 12319. Von drei dieser fünf, die ich im Kontext gelesen habe, wirken zwei fraglich, z. B. TKR_2410340180_8 „er ist ein tor der sich der wisheit fugt". | Silber ist eine echte, aber fehlerbehaftete Einzelentscheidung. Das stützt die Rolle als Silber, nicht als Gold. |
| B4 | Das heutige Inventar ist das, gegen das Silber annotiert wurde. | Seit der Migration weitgehend ja: 131 Senses neu, 173 entfernt; nur 5 polyseme Lemmata haben ihr Inventar geändert (109 Silber-Tokens betroffen). Was vor der Migration geschah, zeigen die Daten nicht. | Für die Zeit seit 2025-07 vernachlässigbar; die betroffenen 5 Lemmata vor der Ziehung ausschließen oder im Manifest markieren. |
| B5 | Jedes Silber-`@ana` zeigt auf einen Sense im Lexikon. | 596 Tokens (188 Paare, 185 Lemmata) zeigen ins Leere; 26 der Lemmata sind polysem, darunter *guot*, *tragen*, *halten*, *dinc*. Schon im Migrationsstand so (z. B. `AC1_20110_12`). `obergattungen_entwurf.py` zählt solche Tokens derzeit als Silber. | Regel nötig: als „kein Silber" behandeln oder ausschließen. Zusätzlich 66 Tokens mit `@lemmaRef` ins Leere. |
| B6 | 126 Senses ohne Begriffszeiger (Ausschluss 3). | Bestätigt: 124 leere `<sense/>` und 2 mit Inhalt ohne Zeiger, alle nach der Migration entstanden (Stubs aus #115 u. a.). Nur 2 betreffen polyseme Lemmata, beide NAM (*Hesperos*, *Stainbok*). | Ausschluss 3 trifft kein Ziel-Lemma; im Protokoll so festhalten. |
| B7 | 22 Lemmata mit zwei Senses gleicher Begriffsgruppe (Ausschluss 2). | Bestätigt: 22. | unverändert |
| B8 | Erster Sense in `lexicon.xml` als MFS-Rückfall (Protokoll 9.2). | Schwach: Nur bei 2.627 von 4.447 polysemen Lemmata mit Silber (59 %) ist der erste Sense der Mehrheitssense. Die Reihenfolge im Lexikon folgt bei 921 von 7.764 polysemen Lemmata nicht einmal der ID-Reihenfolge. | Rückfall-Items getrennt ausweisen (steht im Protokoll); erwägen, sie aus dem primären Vergleich zu nehmen. |
| B9 | Das Inventar ist das, was im Korpus vorkommt. | 6.343 von 14.980 Senses polysemer Lemmata mit Silber (42 %) sind im Silber nie belegt; 3.317 von 7.764 polysemen Lemmata haben gar kein Silber. | Viele Menüs enthalten Senses ohne einen einzigen bekannten Beleg. Erwartbar viele `KEINE_PASST` und Verwechslungen mit unbelegten Senses; Richtlinien müssen das abfangen. |
| B10 | Senses sind nicht an eine Wortart gebunden (Schichtung nach Paar aus Lemma und Wortart, Menü pro Lemma). | Im Silber faktisch doch: Von 967 Senses mehrwortartiger Lemmata mit mindestens 5 eindeutig getaggten Tokens kommen 876 nur mit einer Wortart vor, 926 zu mindestens 95 %. Ausnahme *guot*: Sense 4120 (Besitz …) trägt 23 Tokens mit `@pos="ADJ"`. | Das Menü eines Paars enthält Senses der anderen Wortart, die Polysemiestufe des Paars ist damit überzeichnet. Filtern ginge nur für belegte Senses (B9). Entscheidung nötig (Abschnitt 4). |
| B11 | Der „Pfad zum Oberbegriff" ist eindeutig (Protokoll 5) und eine grobe Ebene lässt sich ablesen (Protokoll 9.1, Punkt 7). | Polyhierarchisch: 5 Wurzeln (Universum/Welt, Tierwelt, Mensch, Mensch und Welt, Funktionswörter), Tiefe bis 6, 43 Begriffe mit mehreren direkten Oberbegriffen (z. B. Mineralien unter Planet Erde, Mineralogie/Petrologie und Geografie). Der Zahlencode bildet aber einen Primärbaum: Bis auf `concept_23309030` und `concept_23309040` hat jeder Begriff einen Oberbegriff, der zum Code passt. Alle 567 Begriffe haben einen deutschen `<term>`, kein Zeiger geht ins Leere. | Pfad und grobe Ebene über den Zahlencode definieren, Querverweise nicht anzeigen. 74 Begriffe sind „…/Namen"-Kategorien. |
| B12 | Der Header sagt, wie weit ein Text disambiguiert ist. | Der Satz in `normalization` wurde am 2026-09-30 aus dem `@ana`-Stand errechnet (#493, `revisionDesc`). | Keine unabhängige Herkunftsangabe; D1/D0 weiter aus den Tokens bestimmen. |
| B13 | Senses haben keine menschlichen Erläuterungen (1 `<def>`). | Inzwischen 94 `<note type="comment">` von KZW (Glossar Kochbuchforschung, #554, Oktober 2026), plus 1 `<def>`. | Menschliche Glossen für wenige Fachlemmata. Ob sie Annotator:innen und LLM gezeigt werden, gehört in Freeze 2 (gleiche Karten für beide). |
| B14 | Die Ausschlussliste vom 2026-10-08 gilt. | Neu gerechnet auf `0357cb524`: 157.724 ausgeschlossen (vorher 157.459), davon WZB 142.412 und 15.312 mit geändertem Lemma oder Sense (vorher 15.129); 202 davon ohne Ingest-Liste. Nur-`@pos`-Markierungen unverändert 34.336. | Die Zahlen in Protokoll 3 und 4 beruhen auf `f6fbebf`. Beim Festlegen des Korpus-Commits neu rechnen (Protokoll, offener Punkt 6). |

## 3. Weiterhin nur angenommen

- **Herkunft der Typlisten (B1).** Weder Mehrheit noch ID-Reihenfolge erklärt sie. Vermutung: die
  Anbindung von Bedeutungen an graphematische Typen im alten Wortartikel, die im RDF pro Typ nur
  einen Sense zuließ. Quelle gelesen am 2026-10-23: Hinkelmanns & Zeppezauer-Wachauer (2023,
  S. 180) schreiben, die linguistischen Annotationen (Beispiele: POS, Phrasen- und
  Satzstrukturen) würden künftig „im Stand-Off-Verfahren mit Linked Open Data (LOD) auf die
  Tokens der Texte bezogen und nicht wie bisher auf die graphematischen Types im Wortartikel“.
  Von Bedeutungen steht dort nichts; die Übertragung auf Senses ist eine **Lesart**, die zu B1
  passt, aber nicht belegt ist. Offen bleibt die Frage an KZW, ob Senses wirklich so angebunden
  waren (Herkunft, Datum). Der Beitrag von 2020 (Hinkelmanns & Zeppezauer-Wachauer, S. 73 bis 84)
  erwähnt keine graphematischen Types und ist nicht die gemeinte Quelle.
- **Wer Silber wann nach welchen Richtlinien vergeben hat.** Die Daten sagen dazu nichts; der Header
  nennt nur das MHDBDB-Team.
- **Inventar vor der Migration.** Ob Senses nach der Annotation eines Textes ergänzt wurden, ist
  aus dem Repo nicht rekonstruierbar (B4 gilt nur ab 2025-07).
- **Token-`@pos` als Schichtungsgrundlage.** Bei *guot* sind 18.047 von 27.171 unannotierten
  Tokens `NOM ADJ ADV`; nur eindeutig getaggte gehen in die Grundgesamtheit. Ob die eindeutig
  getaggten für das Lemma repräsentativ sind, ist ungeprüft.
- **Editions- und Normalisierungseffekte** (Groß-/Kleinschreibung nur teilweise wie in der
  Edition, WZB als Prosa in `<l>`) sind bekannt, ihr Einfluss auf WSD ist nicht gemessen.

## 4. Entscheidungen, die daraus folgen

1. **Typliste (B1):** Aus allen Annotations- und Prompt-Materialien entfernen (Vorschlag: ja,
   zwingend). Zusätzlich als zweite Baseline „Typ-Sense" berichten? Sie ist für D0 verfügbar und
   könnte stärker sein als MFS.
2. **Menü pro Paar aus Lemma und Wortart (B10):** volles Lemma-Menü zeigen, oder Senses mit
   Silberbelegen nur in der anderen Wortart ausblenden? Die Wahl ändert die Polysemiestufe und
   damit die Zellen; sie muss vor Freeze 1 fallen.
3. **Silber ins Leere (B5)** und **die 5 Lemmata mit geändertem Inventar (B4):** ausschließen
   oder als „kein Silber" führen.
4. **Grobe Ebene (B11):** über den Zahlencode, auf welcher Stufe.
5. **MFS-Rückfall (B8):** im primären Vergleich lassen oder nur sekundär auswerten.
