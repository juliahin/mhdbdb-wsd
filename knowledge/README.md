# Dissertation im Fork: Übersicht

**Stand:** 2026-10-23. Einstieg für jede Sitzung, die an der WSD-Dissertation arbeitet.

Dieses Repository ist der **öffentliche** Fork `juliahin/mhdbdb-wsd` von
`DigitalHumanitiesCraft/mhdbdb-tei-only`. Alles außerhalb der unten genannten Ordner gehört zum
MHDBDB-Projekt selbst (Korpus `tei/`, Normdaten `authority-files/`, Website, `docs/`, `CLAUDE.md`)
und kommt per Upstream-Merge. Die Dissertation liest diese Daten, ändert sie aber nicht.

## Die Bereiche

| Ordner | Inhalt | gepflegt von | im Repo? |
|---|---|---|---|
| [`knowledge/`](.) | Geprüfter Wissensstand zu den Daten: [`data.md`](data.md) (Datenmodell, Befunde B1 bis B14, offene Annahmen, anstehende Entscheidungen), Prüfskripte in [`pruefskripte/`](pruefskripte/) | Agent `protokollant` | ja |
| [`goldstandard/`](../goldstandard/) | Protokoll mit Abweichungslog, DMP, Prompt-Log, Literatursynthesen (IAA, Stichprobe), Entwurf der Obergattungsgruppen, Skript zur Ausschlussliste; Übersicht in [`goldstandard/README.md`](../goldstandard/README.md) | Julia, `protokollant` | ja, außer `ausschluss/ausschluss-tokens.csv` |
| [`literatur/`](../literatur/) | Forschungsliteratur: Volltexte, Docling-Markdown, Zusammenfassungen, BibTeX, Beschaffungsliste, Archiv des früheren Themas; Übersicht und Ablauf in [`literatur/README.md`](../literatur/README.md) | Agent `quellen` | nur README, Vorlage, Skript, Listen, Zusammenfassungen |
| [`doktorat/`](../doktorat/) | Studienrecht und persönliche Unterlagen zum Doktoratsstudium; README fasst das Curriculum 2024 der Uni Graz zusammen | Julia | nur README |
| [`.claude/agents/`](../.claude/agents/) | Vier Fork-Agenten `autor`, `gutachter`, `quellen`, `protokollant`; Zuschnitt in [`.claude/agents/README.md`](../.claude/agents/README.md) | Julia | ja |
| `goldstandard-test.py` (Wurzel) | Polysemie-Analyse für das Stichprobendesign (Commit `bea795b88`, Grundlage der 36 Zellen); das gültige Design steht im Protokoll, Abschnitt 4 | | ja |
| `MHDBDB-TODO-juliahin.md` (Wurzel) | To-do-Liste zur MHDBDB-Projektarbeit (Stand 29.07.2026), nicht zur Dissertation | | ja |

## Wie die Teile zusammenhängen

```
tei/ + authority-files/  (Upstream, Korpus-Commit im Protokoll festgehalten)
        │ gemessen mit knowledge/pruefskripte/, goldstandard/*.py
        ▼
knowledge/data.md  ──►  goldstandard/PROTOKOLL.md  ──►  Richtlinien, Datasheet, Freeze (noch offen)
                              ▲
literatur/pdf ─► md ─► zusammenfassungen ─► goldstandard/LITERATUR-*.md
                                                 │
                                                 ▼
                                   Artikeltext (Agent autor) ◄─ Gutachten (Agent gutachter)
doktorat/  ─ Rahmen: Studienrecht, Betreuung, Fristen (beeinflusst, was als Artikel erscheint)
```

## Was lokal bleibt und warum

Der Fork ist öffentlich. Was nicht hineingehört, ist per `.gitignore` im jeweiligen Ordner
ausgeschlossen (nicht in der Wurzel-`.gitignore`, die vom Upstream kommt):

| Was | Wo | Grund |
|---|---|---|
| Volltexte der Literatur | `literatur/pdf/`, `literatur/archiv-intermedialitaet/` | Urheberrecht |
| Docling-Markdown der Volltexte | `literatur/md/` | aus den Volltexten abgeleitet, gleiches Urheberrecht |
| Eigene Listen und Folien | `literatur/material/` | eigenes, unveröffentlichtes Material |
| Curriculum mit Markierungen, persönliche Unterlagen | `doktorat/` außer README | persönlich |
| Token-Liste der Ausschlüsse | `goldstandard/ausschluss/ausschluss-tokens.csv` | aus dem Skript reproduzierbar (Protokoll, Abschnitt 3) |
| Menschliche Labels, Adjudikation, LLM-Ausgaben, Prompt-Log Ebene A | privates Repository, noch nicht angelegt | Kontaminationsschutz bis zur Publikation (Protokoll, Abschnitt 10; DMP) |

**Regel für neue Dateien:** Alles über eine Person, das über ihre Rolle im Projekt hinausgeht
(Kontaktdaten, Zeugnisse, Gesprächsnotizen, Gutachten, Korrespondenz), gehört nach `doktorat/privat/`
oder ins private Repository, nie in einen getrackten Ordner. Was einmal gepusht ist, bleibt in der
Git-Geschichte, auch wenn die Datei später ignoriert wird.

## Lesereihenfolge für eine neue Sitzung

1. diese Datei
2. [`goldstandard/PROTOKOLL.md`](../goldstandard/PROTOKOLL.md), Abschnitt 12 (offene Punkte) und 11 (Abweichungslog)
3. [`data.md`](data.md), Abschnitte 2 bis 4
4. bei Literaturfragen [`literatur/README.md`](../literatur/README.md), bei Fragen zu Fristen und Form der Arbeit [`doktorat/README.md`](../doktorat/README.md)
