# WSD-Goldstandard

Goldstandard für die Bedeutungsdisambiguierung (WSD) im MHDBDB-Korpus, Teil der Dissertation von
Julia Hintersteiner. Dieses Verzeichnis gehört zum Fork `juliahin/mhdbdb-wsd`, nicht zum
Projektkern.

## Dokumentationsebenen

| Ebene | Datei | Stand |
|---|---|---|
| 1. Protokoll mit Abweichungslog gegenüber der Präregistrierung | [PROTOKOLL.md](PROTOKOLL.md) | Entwurf 2026-10-08, ergänzt 2026-10-30 (A28) |
| 1a. Literatur zu Inter-Annotator-Agreement (mit Prüfstatus) | [LITERATUR-IAA.md](LITERATUR-IAA.md) | 2026-10-28 |
| 1b. Literatur zum Stichprobendesign | [LITERATUR-STICHPROBE.md](LITERATUR-STICHPROBE.md) | 2026-10-16 |
| 1c. Datenmanagementplan (Science Europe / FWF) | [DMP.md](DMP.md) | Entwurf 2026-10-16 |
| 1d. Prompt-Log (Ebene B hier, Ebene A privat) | [PROMPT-LOG.md](PROMPT-LOG.md) | 2026-10-16 |
| 1e. Vorschläge aus der Literaturauswertung, zum Entscheiden | [VORSCHLAEGE-2026-10.md](VORSCHLAEGE-2026-10.md) | 2026-10-30 |
| 1f. Verschmelzungen: Erkennungsregel für Ausschluss 5 (Protokoll, Abschnitt 3) | [verschmelzungen.py](verschmelzungen.py) | 2026-10-30 |
| 1g. Verschmelzungen: Wirkung auf die Grundgesamtheit | [verschmelzungen/wirkung.py](verschmelzungen/wirkung.py) | 2026-10-30 |
| 1h. Verschmelzungen: Ziehung der Prüfrunde 2 (reproduziert Liste und Schlüssel) | [verschmelzungen/runde2_ziehen.py](verschmelzungen/runde2_ziehen.py) | 2026-10-30 |
| 1i. Verschmelzungen: Prüflisten, Schlüssel und Urteile beider Runden (Urteile von einem Agenten, nicht gegengelesen) | `verschmelzungen/runde1-*`, `verschmelzungen/runde2-*` (`-pruefliste.md`, `-schluessel.txt`, `-urteile.md`) | 2026-10-30 |
| 2. Annotationsrichtlinien | `RICHTLINIEN.md` | noch nicht angelegt |
| 3. Datasheet (Herkunft, Auswahl, Ausschlüsse, Lizenz, bekannte Lücken) | `DATASHEET.md` | noch nicht angelegt |
| 4. Kontextwissen (Sense-Karten aus dem Begriffssystem, Textmetadaten) | wird generiert | noch nicht angelegt |
| 5. Freeze-Manifest (Token-IDs, Seed, Korpus-Commit, Prüfsummen) | wird generiert | erst nach der Ziehung |

Nachvollziehbarkeit beim Annotieren selbst (wer, wann, was) regelt das Protokoll, Abschnitt 8.

## Was hier nicht liegt

Die menschlichen Labels, Ereignisprotokolle und die Adjudikation bleiben bis zur Publikation
privat (Protokoll, Abschnitt 10).
