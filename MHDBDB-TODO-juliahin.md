# MHDBDB — To-do für Julia (`juliahin`)

**Stand:** 29.07.2026
**Quelle:** alle 44 offenen Issues in `DigitalHumanitiesCraft/mhdbdb-tei-only`, plus jede Nennung von `@juliahin` in Bodies und Kommentaren (9 Issues nennen dich, 36 involvieren dich historisch).

**Zugewiesen:** #235 (allein), #224 (mit chsteiner), #63 (mit wachauer)
**Namentlich gepingt ohne Assignment:** #198, #138, #114, #68, #28, #27
**Offene PRs mit Review-Anfrage an dich:** keine (#253, #254 haben keine Reviewer gesetzt)

---

## Tier 1 — Jetzt (beides am 28.07. an dich übergeben, beides WZB)

### 1. #224 — Bug report Sonderzeichen WZB · *Entscheidung + Close*

<https://github.com/DigitalHumanitiesCraft/mhdbdb-tei-only/issues/224> · dir zugewiesen · Label `bug` · externer User (Klaus Schmidt) wartet seit 27.07.

Der technische Fix ist geshippt (PR #227: NFC-Komposition, `ŏ→oe` / `ŭ→ue`, Präfix-Regel in Stufe 3).

Wachauers Auftrag im Wortlaut: *„bitte hier übernehmen, da WZB dein Baby ist … Bitte alles mal durchdenken und wenn du keine weiteren Bedenken mehr hast, bitte close."*

**Die inhaltliche Frage liegt bei dir:** Markiert das Breve über `w` (91×) und `n` (22×) in der WZB-Transkription etwas Bedeutungstragendes? Wenn ja, wird es ein Thema für die Leseansicht, nicht für die Suche.

→ Billigster Punkt der Liste: eine Einschätzung plus Close.

### 2. #235 — WZB/Header-Datenfunde, Punkte 1 & 3 · *echte Datenarbeit*

<https://github.com/DigitalHumanitiesCraft/mhdbdb-tei-only/issues/235> · dir allein zugewiesen · Label `ingestpipeline`

Punkt 2 (Harsch-URLs) ist von chsteiner erledigt (PR #238 — mit Korrektur der Zahl: 17 Vorkommen in 15 Dateien, nicht 20). Deins:

- **Punkt 1:** 17 `<w>` in `tei/WZB.tei.xml` enthalten ein literales ` `-Escape.
  **Deine Entscheidung:** Split in zwei `<w>` mit eigener `xml:id`, oder ein Token mit echtem Leerzeichen?
  Keines der 17 trägt `@lemmaRef` → ein Split ist für die Positionszählung gefahrlos (CONTRACTS §B).
- **Punkt 3:** 289 WZB-`<w>` mit o/u-Breve tragen weiterhin kein `@lemmaRef`. Matcher-Re-Run, jetzt wo die Normalizer das Breve auflösen — 405 Breve-Tokens sind bereits lemmatisiert, der Mechanismus funktioniert also. Dazu 8 Makron-Tokens.

**Reihenfolge:** Punkt 1 vor Punkt 3, damit der Matcher auf sauberen Tokens läuft. Danach voller Data-Change-Lifecycle (`variants.xml` → beide Indexe → API).

**Überschneidung mit #224:** die Breve-auf-w/n-Frage ist hier der offene ADR-016-Punkt.

### 3. #198 — „haben (NOM)": 17 Prüffälle · *prio-1, blockiert zwei Leute*

<https://github.com/DigitalHumanitiesCraft/mhdbdb-tei-only/issues/198> · Labels `prio-1`, `bug`

Wachauer, 27.07.: *„Bitte @juliahin mach du die vom Menschen zu prüfenden Fälle, danke!"*

Der Batch ist gelaufen (PR #205): 714 Tokens kontext-disambiguiert, 204 geändert. Für dich bleibt `ingest/pos-disambig/198-habe-nom/review-faelle.csv` — 17 Fälle, darunter:

- 3 echte NOM-Tokens unter lemma_2598 mit echter Ambiguität: `AC3_23010_1` („hawe vnd schaufel"), `JT_6192000_1`, `DA_8222_3` („daz er dehein habe gesehen")
- 12 Tokens der *houwen*-Familie (*hou* „Hieb" lemma_61268 / *houwe* „Haue" lemma_9644) in Fecht-, Koch- und Lehrtexten (AC2, AC3, CEFB, DES2, FWWB, KFB, MR2), fälschlich unter lemma_2598 *haben*

Die Triage-Matrix #44 führt genau diesen Punkt unter deinem Namen.

---

## Tier 2 — Billige Verifikation, jede schließt ein Issue ab

### 4. #138 — HUG-Nachprüfung (zwei deiner vier Punkte sind live)

<https://github.com/DigitalHumanitiesCraft/mhdbdb-tei-only/issues/138> · chsteiner hat dich und KZW am 29.07. gepingt

Deine Durchsicht vom 17.07. hat vier Punkte ergeben:

| Dein Punkt | Ergebnis |
|---|---|
| Verszählung beginnt erst bei 5 | ✅ gefixt (#231) — betrifft aber 49 weitere Texte, +1.352 Randnummern, **+826 allein in Parzival** |
| Nach-oben-Button fehlt | ✅ gebaut, springt zum Panelkopf statt zum Seitenanfang |
| Kleinziffern („ii") stören | ✅ KZW hat Entfernung angeordnet; HUG steht jetzt bei 0 (waren 814, davon nur 706 mit `@pos="DIG"`) |
| Winkelklammern als `<pc>` | ℹ️ kein Fehler, editionsgetreu — von KZW bestätigt |

**Dein Auftrag:** einmal auf Parzival schauen, dort ist der Effekt am größten und eine falsche Entscheidung stört am meisten. Revert wäre eine Minute Frontend-Arbeit, keine Datenänderung.

Nebenbefund: chsteiner hat HUG gegen die Hofmeister-Edition kollationiert — Verszählung deckungsgleich, 690/702 Strophengrenzen deckungsgleich, 5 Texte mit Ein-Vers-Verschiebung (Nr. 3, 6, 18, 26, 28).

### 5. #114 — Tabellenansicht: dein Review wurde im Mai erbeten

<https://github.com/DigitalHumanitiesCraft/mhdbdb-tei-only/issues/114> · Linda hat am 13.07. abgenommen (*„aus meiner Perspektive passt das sehr gut!"*)

chsteiner am 28.05.: *„@wachauer / @juliahin — schaut bitte mal über die Tabelle und den Export."* Lindas Freigabe reicht vermutlich; eine Zeile von dir lässt das Issue schließen.

---

## Tier 3 — Parken, entscheiden oder für erledigt erklären

### 6. #28 — Fremdsprachen: KZW hat gerade entschieden, dein Teil kommt später

<https://github.com/DigitalHumanitiesCraft/mhdbdb-tei-only/issues/28>

KZW hat am 29.07. die Lehnwort-/Fremdwort-Grenze festgelegt: zwei Schichten statt einem Feld.

- **Schicht A** = `@xml:lang` / `<foreign>` nur für echtes Code-Switching — explizit inkl. *„lateinische und tschechische Passagen in WZB"* → dein Material
- **Schicht B** = Herkunft in `lexicon.xml`, lemmagetrieben, trägt die Masse

Deine Antwort vom Juni (kein `xml:lang` in WZB vorhanden) steht weiterhin. Nichts zu tun, bis der Phasenplan auf zwei Schichten umgeschrieben ist; dann gehören die WZB-Latein-/Tschechisch-Passagen dir.

### 7. #63 — Begriffssystem Update? · *dein eigenes Ticket, still seit März*

<https://github.com/DigitalHumanitiesCraft/mhdbdb-tei-only/issues/63>

Null Kommentare seit deiner Anlage am 10.03. Die #44-Triage vermerkt: *„Dein eigenes Ticket, seit Anlage ohne Kommentar. Blockiert nichts, aber es steht auf dir."*

Da der SKOS-Lückencheck als diss-nah und als mögliche Co-Op mit Michaela Wiesinger (Arithmetik) angelegt ist: entweder ein Scoping-Kommentar oder ein explizites Parken.

### 8. #68 — WZB-Abschlussbesprechung-Template: veralteter Action Item

<https://github.com/DigitalHumanitiesCraft/mhdbdb-tei-only/issues/68>

Wachauers Punkt 3 vom 15.04. nennt dich für einen *„Termin Anfang Mai für Abschlussbesprechung (Projektfinanzierung für Ingest endet am 30.4.)"* plus ein nachnutzbares Workflow-Template. Die Frist liegt drei Monate zurück. Eine Statuszeile würde reichen, damit der Guide die WZB-Lehren aufnehmen kann.

### 9. #27 — „@juliahin für die TEI-Doku" vom 20.11.2025: vermutlich obsolet

<https://github.com/DigitalHumanitiesCraft/mhdbdb-tei-only/issues/27>

Die POS-Dokumentation, die wachauer dir im November übergeben hat, lebt inzwischen in `docs/POS-TAGSET.md` (am 17.06.2026 als kanonische 19-Tag-Referenz herausgezogen). Verifizieren, dann im Thread festhalten, damit der Ping nicht weiterläuft.

---

## Vorschlag für einen Arbeitsblock

**#224 → #235** als Paar (gleiche Datei, gleiche Breve-Frage, ein Data-Change-Lifecycle-Lauf), danach **#198** separat — anderer Korpusbereich, anderer wartender Reviewer.

---

## Kontext, der nicht in den Issues steht

- **WZB Phase 3** (Bedeutungsdisambiguierung) läuft weiter: 73,7 % `@meaningRef`, 32.048 Zeilen warten auf Per-Instance-LLM-Arbeit. Kein Issue, aber der größte offene Block deiner WZB-Arbeit — und laut dem gelöschten 1000-Worte-Post das empirische Testbett der Dissertation (Baseline Mehrheitssinn 66,7 %).
- **#44** ist das Evergreen-Triage-Issue — **niemals schließen**, kein `Closes #44` in Commits.
- Rollenverteilung laut #44: rein technische Issues → `chsteiner`, editorisch/philologische → `wachauer` (KZW), Julia seit Juli 2026 wieder regulär mit-assignen.
