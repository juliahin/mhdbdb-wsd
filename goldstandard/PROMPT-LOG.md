# Prompt-Log

Zwei Ebenen, festgelegt am 2026-10-16 (DMP, Abschnitt 2).

## Ebene A: LLM-Läufe, die Forschungsdaten erzeugen

Jeder Lauf, dessen Ausgabe in eine Auswertung eingeht (LLM-Disambiguierung der Gold-Items, ggf.
später Glossen), wird vollständig protokolliert. **Ablage: privates Repository** (die Ausgaben sind
so schutzbedürftig wie die Labels). Format: eine JSONL-Datei pro Lauf, ein Objekt pro Anfrage.

| Feld | Inhalt |
|---|---|
| `lauf_id` | eindeutige Kennung des Laufs |
| `zeitpunkt` | ISO 8601 mit Zeitzone |
| `anbieter`, `modell` | exakte Modell-ID samt Snapshot bzw. Version |
| `parameter` | Temperatur, max. Tokens, Seed, alle weiteren API-Parameter |
| `system_prompt_sha256`, `prompt_vorlage_sha256` | Prüfsummen; die Texte selbst liegen versioniert daneben |
| `item_id` | Token-ID aus dem Manifest |
| `eingabe_sha256` | Prüfsumme der vollständigen Anfrage |
| `ausgabe_roh` | vollständige Antwort |
| `label` | daraus geparster Status und Sense |
| `tokens_ein`, `tokens_aus`, `kosten` | Verbrauch |
| `code_commit`, `manifest_sha256` | Stand von Skript und Stichprobe |

Mehrfachläufe (z. B. k Wiederholungen pro Item) bekommen eigene Einträge; welcher Lauf in die
Auswertung eingeht, wird vorab im Protokoll festgelegt.

## Ebene B: KI-Unterstützung bei Design, Dokumentation und Code

Eine Zeile pro Sitzung. Festgehalten wird, was die KI erzeugt hat und welche Entscheidungen die
Forscherin getroffen hat. Wortlaut der Sitzungen wird nicht archiviert.

| Datum | Werkzeug und Modell | Zweck | Erzeugte Artefakte | Entscheidungen der Forscherin | Geprüft |
|---|---|---|---|---|---|
| 2026-10-08 | Claude Code, Claude Opus 5.5; drei Recherche-Agenten (gleiches Modell) | Goldstandard-Design: Protokoll v2, IAA-Literatur, Ausschlussliste | `PROTOKOLL.md`, `README.md`, `LITERATUR-IAA.md`, `ausschluss_nachmigration.py`; Messungen zu Polysemie, Gattung, Silber | Gold = Neuannotation, Bestand = Silber; zweiter Annotator Alan van Beek; Manifest öffentlich, Labels privat; 36 Zellen; Interface als HTML-Datei auf Deutsch; Gattungsausgleich | Zahlen von der KI mit Skripten gemessen; Literatur nur vom Agenten geprüft (Prüfstatus in der Datei) |
| 2026-10-16 | Claude Code, Claude Opus 5.5; ein Recherche-Agent (gleiches Modell); ein Berater-Agent (Claude Fable 5.1) | Ausschlussregel ins Protokoll; Stichprobendesign kritisch prüfen; DMP und Prompt-Log anlegen | `LITERATUR-STICHPROBE.md`, `DMP.md`, `PROMPT-LOG.md`, `.gitignore`, `OBERGATTUNGEN.md` (Entwurf), `obergattungen_entwurf.py`; Messungen zu Wortart, Frequenzbändern, Silberdomäne, Textreihentypologie | Nur-`@pos`-Änderungen markieren statt ausschließen; Token-Liste nicht ins Repo; DMP nach Science Europe/FWF; Prompt-Log in zwei Ebenen; private Daten im privaten GitHub-Repo; Zielvenue Computerlinguistik; Wortart mit Token-Rückfall, Lemma-Panel, D1-Quote 30 %, feste Frequenzbänder, Obergrenze 3 pro Text | Connor-Formel nachgerechnet; Korpusmessungen von der KI; KI hat eigene Fehlangabe korrigiert (Taxonomie „flach“, TRO ohne Gattung) |
| 2026-10-23 | Claude Code, Claude Sonnet 5.5; Agent `protokollant` | Quellenangabe zu Hinkelmanns & Zeppezauer-Wachauer (2023) in Protokoll (Abschnitt 2), `knowledge/data.md` und `LITERATUR-IAA.md` korrigieren; Literatur-README und Beschaffungsliste nachführen | Änderungen in `PROTOKOLL.md` (Zeile A12 im Abweichungslog), `knowledge/data.md`, `LITERATUR-IAA.md`, `literatur/README.md`, `literatur/BESCHAFFUNG.md` | Julia: Korrektur beider Stellen freigegeben („ja, beides machen“); `references.txt` bleibt unverändert | Zitat am PDF gelesen (S. 180, Hauptsitzung und `protokollant`); Seitenzahlen der acht PDFs mit pymupdf gezählt |
| 2026-10-23 | Claude Code, Claude Opus 5.5 | Diss-Ordner sichten und ordnen; Datenschutz im öffentlichen Fork prüfen | `knowledge/README.md` (Übersicht aller Diss-Bereiche), `doktorat/README.md` und `doktorat/.gitignore` (Curriculum 2024 der Uni Graz zusammengefasst), Ordnertabelle in `literatur/README.md` ergänzt | keine; offen an Julia: geltende Curriculumfassung, monographisch oder kumulativ, Name des Zweitannotators im öffentlichen Repo | Curriculum am PDF gelesen, Seitenangaben nach gedruckten Seiten; getrackte Diss-Dateien per grep auf Kontaktdaten und Kennungen durchsucht (kein Treffer); `doktorat/.gitignore` mit `git check-ignore` getestet |
