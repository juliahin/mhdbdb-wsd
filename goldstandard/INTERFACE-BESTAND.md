# Annotationsoberfläche: Bestandsaufnahme (2026-10-23)

**Status:** Arbeitsgrundlage für die Interface-Spezifikation, noch keine Spezifikation. Zusammengeführt aus zwei Recherche-Agenten (Repo-Bestand; Gedächtnis, Issues, Git-Historie) vom 2026-10-23. Zwei tragende Aussagen selbst nachgeprüft: das Silber-Leck der Klaus-Vorlage (`scripts/audit/review-klaus.template.html:37`, `:41`) und dass es keinen fertigen Oberbegriffspfad gibt (`scripts/build-begriffshilfe.py:118` liefert nur die Vorfahrenmenge). Alles andere ist Agentenbericht, Zeilenangaben ungeprüft.

## 1. Schon entschieden

| Entscheidung | Wer, wann | Fundstelle |
|---|---|---|
| Eine Offline-HTML-Datei, Doppelklick, ein Token pro Bildschirm, Export für die Rückgabe, auf Basis von `build-review-klaus.py`. Verworfen: Excel, INCEpTION/Label Studio | Julia, 2026-10-08 | PROMPT-LOG.md:35, Sitzungstranskript d2ea2e05 |
| Sprache nur Deutsch (Oberfläche und Bedeutungsangaben) | Julia, 2026-10-08 | ebd. |
| Zweite annotierende Person: Alan van Beek (**they/them**, KZW in #86, 2026-05-29; Personenliste in #44) | Julia, 2026-10-08 | ebd. |
| Eine Datei pro Person mit fest eingetragener Kennung, kein Login, keine Namenseingabe | Protokoll §8 | PROTOKOLL.md:338 |
| Kopf und Export: Korpus-Commit, Manifest-Prüfsumme, Richtlinien- und Werkzeugversion; Import vergleicht die Manifest-Prüfsumme | Protokoll §8 | :340-347 |
| Ereignisprotokoll, nur anhängend: Zeitstempel ISO 8601, Item, Aktion, Wert, gezeigte Kartenreihenfolge, Kontext erweitert, Verweildauer | Protokoll §8 | :342-345 |
| Blindheit: kein Silber-`@ana`, keine LLM-Vorschläge; zusätzlich keine Typlisten `sense/@ana` (verraten 86 % der Senses) | Protokoll §6, data.md B1 | :298, data.md:42 |
| Karten = deutsche `<term>` der Begriffsgruppe mit Pfad zum Oberbegriff; keine LLM-Definitionen; unterscheidende Begriffe hervorheben; Kartenreihenfolge pro Item gemischt und protokolliert | Protokoll §5 | :253-276 |
| Pfad über den Zahlencode, keine Querverweise | data.md B11 (Befund, nicht im Protokoll) | data.md:52 |
| Sechs Status (`SENSE`, `MEHRERE`, `KEINE_PASST`, `LEMMA_FALSCH`, `KONTEXT_UNZUREICHEND`, `TEXT_DEFEKT`) mit Pflichtfeldern; Sicherheit in drei Stufen; Kommentar | Protokoll §6 | :280-293 |
| `KEINE_PASST`: Begriffe nur aus den Karten dieses Lemmas | Protokoll §5.4 | :270-274 |
| Kontext zweistufig, Erweiterung wird protokolliert | Protokoll §6 | :295-296 |
| Itemreihenfolge pro Person zufällig mit Seed; Pilot außerhalb der Hauptstichprobe | Protokoll §7 | :307-317 |
| Exporte und Labels privat; die gebaute Datei ohne Labels darf öffentlich sein | Protokoll §10, DMP | :424-436, DMP.md:30-32 |
| Prüfseiten-Muster #443: nichts vorausgewählt, keine Sammelaktion, ehrliche Speicheranzeige, JSON plus HTML-Bericht, Import nur passender Exporte, `</` maskieren, keine externen Ressourcen, Generator statt Handarbeit | #443, scripts/review/README.md | INDEX.md:114 |

## 2. Vorlage

**Klaus-Prüfseite** (`scripts/audit/build-review-klaus.py`, `review-klaus.template.html`), für Lesbarkeit und fallbezogene Optionen zusätzlich die Glossar-Vorlage (`scripts/ingest/glossar-554/`).

- **Übernehmen:** Quellprüfsummen und Fingerprint als Speicher- und Importschlüssel; `--snapshot` (Bau verweigert bei geänderter Quelle, build:170-173); strenge Import-Validierung mit Dialog; ausdrückliches „Festhalten“ und Rücksetzen bei Änderung; Stepper; Kontext mit Versen, `pb`/`cb`/`lb`, `join`, zweistufig (`flat()`/`context()`, build:32-66); Rückgabekasten; Barrierefreiheit.
- **Entfernen (Lecks und Protokollverstöße):** `c.old` mit Token-`ana` (template:37, Export :41); KI-Vorprüfung `proposal()` (:35, :59); Namensfeld `#reviewer` (:14); Gruppenübertragung; Links in den Reader („TEI anzeigen“ zeigt `@ana`); Begriffssuche über alle Begriffe.
- **Neu bauen:** Sense-Karten mit Mehrfachauswahl, Pfad und Hervorhebung, gemischt; Statusleiste nach §6 mit Pflichtfeldern (Muster Glossar `needsText`); Sicherheit; Ereignisprotokoll; Kopf mit Kennung und Versionen; Item-Mischung pro Person. Oberbegriffspfad und „unterscheidende Begriffe“ gibt es noch nirgends als Code.
- **Aus `scripts/review/review_page.py` übernehmen:** Speicherprobe (:364-370), `_json_inline` (:667-676), Markup-Gates (:812-893).
- **Item-Auflösung:** nach `scripts/ingest/pos-disambig/extract-cases-by-id.py:110-150` (jede `xml:id` genau einmal, sonst Abbruch; Sigle beim ersten Unterstrich trennen), ohne `ist_ana`.
- **Tests:** Gerüst aus `testing/review-klaus.spec.js` (Datei-URL, `beforeEach`, `exported()`, Rundlauf, fremder Import, Bericht ohne Skripte, gesperrter Speicher). Neu: Blindheit (kein `ana`, `#type_`, `old`, Vorschlag im eingebetteten JSON), feste Kennung, Kartenreihenfolge aus Seed, nur anhängendes Protokoll, Ereignis bei Kontexterweiterung, Statusregeln, `KEINE_PASST` auf Lemma beschränkt, Import lehnt andere Manifest-Prüfsumme ab. Neue Spec braucht eine Zeile in DEVELOPMENT.md „Test File Inventory“.

## 3. Lehren aus früheren Prüfseiten

- **#371 stat:** JSON als Issue-Kommentar zurück, Klartextzeile „Prüfer: Alan van Beek“ mittendrin, `json.loads` brach ab. Felder sahen nach menschlicher Entscheidung aus, waren aber Maschinenurteile (`batch_verdict`, `confidence`).
- **#390/#115 Klaus:** nur HTML-Bericht zurück, kein JSON; ein Fall „inhaltlich beantwortet, formal unbestätigt“ (Bestätigungsklick fehlte); Teil B (264 Belege) unbearbeitet; Versand 22.09., Rücklauf 09.10.
- **PR #457:** Eingabe nur in „Andere Antwort“ änderte den Stand nicht (Fortschritt und Import zählten verschieden); doppelt maskiertes `&middot;`; Fall ohne Gruppe verschwand, blieb im Nenner.
- **#554 Glossar:** der saubere Fall, klare Anleitung „JSON und HTML-Bericht herunterladen, als Anhang zurück“.
- Anhänge in Issues waren für Claude-Sitzungen nicht abrufbar (403, #419).
- Verlorene Browserdaten: kein dokumentierter Fall; `localStorage` unter `file://` ist ungemessen (#443, PR #457).
- Frühere WSD-Werkzeuge nutzten ±5 Tokens Kontext (`scripts/ingest/wzb/wzb-sense-evaluate.py`, `CONTEXT_WINDOW = 5`).
- **Folge:** Rückgabe **nicht** über öffentliche Issues (Labels sind privat); eindeutige Herkunft jedes Exportfelds.

## 4. Widersprüche

- **Pronomen:** PROTOKOLL.md:4 „Zweiter Annotator“, DMP.md:75 „seine Labels“, DMP.md:102 „Annotator 2“ gegen they/them (#86, #44). Korrektur vorgeschlagen, noch nicht entschieden.
- **Präregistrierung (24.04.)** sah ein Aufdecken von LLM-Wahl und Gold nach der Eingabe vor; Protokoll §6 schließt beides ganz aus der Datei aus. Abweichungen A5/A6 decken das nur teilweise ab.
- **#443** verlangt ein Namensfeld, Protokoll §8 schließt es aus (bewusst).
- **#443** kennt den Zustand „geprüft, bleibt offen“, Protokoll §6 nicht.
- Pilot-Pool ca. 100 (§4, :152) gegenüber Pilot ca. 50 Items (§7, :312): vermutlich Pool für zwei Runden, klarstellen.

## 5. Offen (Julias Entscheidung)

Für den Bau:
1. Kontextumfang: Verse (z. B. 2 davor und danach, Prosa 20 Tokens, Muster `collect-359-evidence.py`) oder Tokens (Klaus 35/120); Werktitel zeigen? WZB-Prosa steht in `<l>` ohne `@n`.
2. Bedeutungsmenü pro Lemma oder pro Lemma und Wortart (B10), vor Freeze 1.
3. Zustand „geprüft, bleibt offen“: Zwischenzustand, der vor der Rückgabe aufgelöst sein muss?
4. „Entschieden“ erst per „Festhalten“ (Vorschlag) oder schon bei Auswahl?

Später: Glossen von KZW auf den Karten (Freeze 2; sie zitieren Korpusstellen, Leckgefahr); Pfadregel für `concept_23309030`, `concept_23309040` und „…/Namen“-Kategorien; Messung der Verweildauer und Alans Einwilligung; Adjudikationsoberfläche; `.gitignore`-Muster für Exporte.

Blockiert den echten Bau (nicht den Prototyp): Manifest und Ziehungsskript, Richtlinien v0, Korpus-Commit fürs Einfrieren.

## 6. Nächste Schritte (vorgeschlagen, nicht begonnen)

1. Interface-Spezifikation aus diesem Bestand, offene Punkte mit Vorschlag.
2. Gegenprüfung durch `fable-advisor` auf Blindheit und Lecks.
3. Prototyp mit 10 bis 15 Dummy-Items und Playwright-Tests zur Blindheit.
