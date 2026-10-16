# Datenmanagementplan: WSD-Goldstandard MHDBDB

**Status:** Entwurf vom 2026-10-16. Gliederung nach den Kernanforderungen von Science Europe
(*Practical Guide to the International Alignment of Research Data Management*), auf denen auch
die DMP-Vorlage des FWF beruht.
**Verantwortlich:** Julia Hintersteiner. Bezug: [PROTOKOLL.md](PROTOKOLL.md).

Offene Punkte sind mit **[offen]** markiert.

---

## 1. Datenbeschreibung, Erhebung und Nachnutzung

### 1.1 Nachgenutzte Daten

| Daten | Quelle | Lizenz | Rolle |
|---|---|---|---|
| TEI-Korpus (667 Texte) | MHDBDB, `tei/` in `DigitalHumanitiesCraft/mhdbdb-tei-only` | CC BY-NC-SA 4.0 | Grundgesamtheit, Kontexte |
| Lexikon, Begriffssystem, Werke, Gattungen | `authority-files/` desselben Repos | CC BY-NC-SA 4.0 | Sense-Inventar, Bedeutungskarten, Schichtung |
| Bestehende Bedeutungsannotation (`@ana`) | Korpus | CC BY-NC-SA 4.0 | Silber, MFS-Baseline |

Eingefroren wird ein fester Commit; Prüfsummen von Korpus, `lexicon.xml` und `concepts.xml` stehen
im Manifest (Protokoll, Abschnitt 10).

### 1.2 Neu erzeugte Daten

| Daten | Format | Umfang (Schätzung) | Öffentlich |
|---|---|---|---|
| Manifest: Token-IDs, Zellzuordnung, Seed, Commits, Prüfsummen | JSON/CSV | < 1 MB | ja |
| Skripte (Ausschluss, Ziehung, Kartenbau, Interface-Bau, Auswertung) | Python, HTML/JS | < 1 MB | ja |
| Bedeutungskarten (Kontextwissen) | JSON | wenige MB | ja |
| Annotationsdateien pro Annotator:in, Ereignisprotokolle | JSON | wenige MB | erst mit Publikation |
| Adjudikation mit Ursachencodes | JSON/CSV | < 1 MB | erst mit Publikation |
| LLM-Ausgaben und Prompt-Log Ebene A | JSONL | < 100 MB | erst mit Publikation |
| Protokoll, Richtlinien, Datasheet, Prompt-Log Ebene B | Markdown | < 1 MB | ja |

Alle Formate sind offen und textbasiert (UTF-8).

## 2. Dokumentation und Datenqualität

- **Protokoll** mit Abweichungslog gegenüber der Präregistrierung vom 2026-04-24.
- **Annotationsrichtlinien** mit Versionsnummer und Prüfsumme, eingefroren vor der Hauptrunde.
- **Datasheet** (Gebru et al. 2021) und Data Statement (Bender & Friedman 2018).
- **Provenienz beim Annotieren:** Ereignisprotokoll, an das nur angehängt wird (wer, wann, was,
  gezeigte Kartenreihenfolge, Kontexterweiterung, Verweildauer); Protokoll, Abschnitt 8.
- **Qualitätssicherung:** Pilot bis zu einer vorab festgelegten Agreement-Schwelle, Doppelannotation
  aller Items, blinde Adjudikation, Prüfung durch eine dritte Person, berichtetes IAA mit Intervallen.
- **Prompt-Log** in zwei Ebenen: [PROMPT-LOG.md](PROMPT-LOG.md).
- **Reproduzierbarkeit:** Jede Zahl im Protokoll trägt Datum und Commit; Skripte erzeugen aus
  Commit und Seed dieselbe Ausgabe.

## 3. Speicherung und Sicherung während der Forschung

| Ort | Inhalt | Zugriff |
|---|---|---|
| Öffentlicher Fork `juliahin/mhdbdb-wsd`, Ordner `goldstandard/` | Protokoll, Richtlinien, Skripte, Manifest, Literatur, Prompt-Log Ebene B | öffentlich |
| Privates GitHub-Repository **[offen: anlegen, Name festlegen]** | Annotationsdateien, Ereignisprotokolle, Adjudikation, LLM-Ausgaben, Prompt-Log Ebene A | Julia; Lesezugriff für die dritte Person bei Bedarf |
| Lokale Arbeitskopien | reproduzierbare Zwischenprodukte (z. B. Token-Liste der Ausschlüsse) | nicht versioniert |

**Sicherung [offen]:** Ein einzelnes privates Repository ist eine einzige Kopie bei einem einzigen
Anbieter. Empfohlen wird eine zweite Kopie auf institutionellem Speicher der Universität Salzburg
(z. B. ein verschlüsseltes Archiv pro Meilenstein: nach Pilot, nach Hauptrunde, nach Adjudikation).

Die Rückgabe von Alans Annotationsdatei erfolgt per JSON-Export; Eingang, Datum und Prüfsumme jeder
Rückgabe werden im privaten Repository festgehalten.

## 4. Rechtliche und ethische Anforderungen

- **Lizenz der Ausgangsdaten:** CC BY-NC-SA 4.0. Der Goldstandard ist eine Bearbeitung und wird unter
  denselben Bedingungen weitergegeben (Namensnennung, nicht kommerziell, Weitergabe unter gleichen
  Bedingungen). Die Kontexte stammen aus Editionen; die Rechtegrundlage des Korpus regelt
  `docs/RESEARCH.md` (Corpus Scope and Rights Basis) im Upstream-Repo.
- **Personenbezogene Daten der Annotator:innen [offen]:** Die Ereignisprotokolle enthalten Zeitstempel
  und Verweildauern, also Daten über das Arbeitsverhalten einer bestimmten Person. Vor dem Pilot
  braucht es Alans informierte Einwilligung: was protokolliert wird, wozu, wer es sieht, ob seine
  Labels vor der Adjudikation mit Namen oder pseudonymisiert veröffentlicht werden, wie lange die
  Daten aufbewahrt werden. Für die Veröffentlichung wird pseudonymisiert (A1, A2), Verweildauern
  nur aggregiert.
- **LLM-Nutzung:** An LLM-Anbieter gehen nur Korpuskontexte und Bedeutungskarten, keine
  personenbezogenen Daten. Nutzungsbedingungen des Anbieters und Modellversion werden pro Lauf im
  Prompt-Log festgehalten.
- **Gute wissenschaftliche Praxis:** Präregistrierung und Abweichungslog; Offenlegung der
  KI-Unterstützung bei Design und Code (Prompt-Log Ebene B).

## 5. Datenweitergabe und Langzeitarchivierung

- **Bis zur Publikation:** Öffentlich sind nur Manifest, Skripte und Dokumentation. Labels bleiben
  privat, damit sie nicht in Trainingsdaten künftiger LLMs geraten (Sainz et al. 2023).
- **Mit der Publikation:** Archivierung auf Zenodo mit DOI. Labels verschlüsselt (Passwort in der
  Publikation), Lizenz ohne Weiterverbreitung im Klartext und ohne Trainingsnutzung, dazu ein
  Canary-String (Jacovi et al. 2023). Mitveröffentlicht werden die Labels vor der Adjudikation
  (pseudonymisiert), die Adjudikation mit Ursachencodes und das Prompt-Log Ebene A.
  **[offen]** Verträglichkeit einer Zusatzklausel „keine Trainingsnutzung" mit CC BY-NC-SA klären.
- **Code:** Skripte im öffentlichen Fork, Release-Stand zusätzlich auf Zenodo.
- **Aufbewahrung:** mindestens 10 Jahre (Regel guter wissenschaftlicher Praxis), über Zenodo gesichert.

## 6. Verantwortlichkeiten und Ressourcen

| Rolle | Person | Aufgabe |
|---|---|---|
| Datenverantwortliche, Annotatorin 1 | Julia Hintersteiner | Protokoll, Richtlinien, Annotation, Archivierung |
| Annotator 2 | Alan van Beek | Annotation |
| Prüfung der Adjudikation | **[offen]** (z. B. Katharina Zeppezauer-Wachauer) | Stichprobenprüfung |

**Ressourcen [offen]:** Annotationszeit (grobe Schätzung, nicht gemessen: 8 bis 10 Stunden pro Person
für ca. 500 Items plus Pilot), Kosten der LLM-Läufe, Speicherplatz (vernachlässigbar).
