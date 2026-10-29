# Steller 2024: KI × DH, Positionspapier der Digitalen Akademie Mainz

**Datei:** `pdf/Steller-2024-KI-DH-Positionspapier.pdf` (nur lokal; 20 Seiten, Version 0.9.1, August 2024)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganzes PDF an der Textebene gelesen; Versionen bei Zenodo über die API abgefragt (2026-10-28).

Seitenzählung: PDF-Seite n = Seitenangabe „Seite n von 20" im PDF.

## Bibliografie

- **Vollständig (lokale Fassung):** Steller, Jonatan Jalle (2024). *KI × DH: Zum Umgang mit ML, Transformern und LLMs in der Digitalen Akademie*. Positionspapier, Version 0.9.1, August 2024. Mainz: Digitale Akademie, Akademie der Wissenschaften und der Literatur Mainz. Zenodo, veröffentlicht 12.09.2024, CC BY 4.0.
- **DOI/URL:** 10.5281/zenodo.13753400 (v0.9.1; löst auf Zenodo auf). Das lokale PDF ist **byte-gleich** mit der PDF-Datei dieses Zenodo-Datensatzes (MD5 `76d7d9f4…5345e`, 804.684 Bytes, am 2026-10-28 verglichen) ✔. Konzept-DOI über alle Versionen: 10.5281/zenodo.13753399.
- **Art:** Working Paper/Positionspapier (Zenodo: „Working paper"), nicht begutachtet; innerhalb der Digitalen Akademie abgestimmt, nicht notwendig Position der ganzen Akademie (S. 1)
- **Sprache:** Deutsch
- **Neuere Fassungen (Zenodo, ○ über die API, Stand 2026-10-28):** v0.9.2 vom 24.09.2024 (10.5281/zenodo.13831622) und **v0.9.3 vom 06.02.2025** (10.5281/zenodo.14824040), jeweils CC BY 4.0. `references.txt` zitiert schon v0.9.3. Stichprobenartig an der Markdown-Datei von v0.9.3 verglichen: Gliederung, Indikatorformel, die elf Leitlinien und die neun Bedarfe stimmen inhaltlich überein; geändert sind u. a. der Hinweis auf S. 1 („nicht die Position aller Mitarbeitenden oder der gesamten Akademie") und die zitierte Fassung der Open-Source-AI-Definition (1.0.0 statt 0.0.9). Kein vollständiger Abgleich; Seitenangaben unten gelten nur für v0.9.1.

## Worum es geht

Ein Positionspapier der DH-Abteilung einer Akademie zum Umgang mit Machine Learning, Transformern und LLMs. Es verbindet eine knappe Technikerklärung (Abschn. 1) mit einer deutlich kritischen Diskurs- und Folgenanalyse (Abschn. 2 und 3), leitet daraus eine bedarfsgeleitete Abteilungsstrategie und neun Bedarfsfelder ab (Abschn. 4 und 5) und schlägt einen Risikoindikator (Abschn. 6) und elf Leitlinien (Abschn. 7) vor. Empirische Daten enthält es nicht.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| ML-Technologien eignen sich für manche repetitive Aufgaben, nehmen aber „keine eigene semantische Einordnung" vor und geben den Bias des Trainingsmaterials wieder. | S. 2, Kernaussage 1; S. 4 | Position |
| ML gewährleistet nicht, dass semantisch relevante oder kausale Parameter gelernt werden, sondern Oberflächenmerkmale typischer Trainingsbeispiele (Beispiel Hund/Schwein). | S. 3, Abschn. 1 | Position, mit Rebala et al. 2019 |
| Prompts werden um meist geheime Systemprompts ergänzt; deshalb seien Prompt-Optimierungen nicht über verschiedene LLM-Angebote hinweg verallgemeinerbar. | S. 4, Abschn. 1, Merkmal 1 | Position |
| Llama-Modelle seien kein Open Source: Sie erfüllten kein Merkmal der Quelloffenheit, das für reproduzierbare Ergebnisse wichtig wäre. | S. 9, Abschn. 3 | referiert (Liesenfeld & Dingemanse 2024) |
| Einsatz von ML soll bedarfsgeleitet sein, nicht technologiegeleitet. | S. 2, Kernaussage 4; S. 11, Abschn. 4 | Position |
| Bedarfsfeld 1: automatische Vorauszeichnung, fine-tunebar an vorhandenen Projektdaten, von Vorauswahlen aus kontrollierten Vokabularen bis zu Normdaten und Entity Recognition. | S. 12, Abschn. 5 | Bedarfsanalyse der Abteilung |
| Risikoindikator aus drei Faktoren: gesellschaftliches Risiko (nach EU AI Act, 1 bis 3 bzw. ∞), ökologische Folgen (1 bis 4), Grad der Peripherie im Vorhaben (1 bis 4); Formel (2 × Risiko) + (Ökologie × Peripherie) − 2, Wertebereich 1 bis 20, niedriger ist besser zu rechtfertigen. | S. 14 bis 15, Abschn. 6, Tab. 1 bis 3 | eigener Vorschlag |
| Leitlinie 4: „Rule of Least Power"; wenn ein klassischer Algorithmus oder einfacheres ML die Aufgabe erledigt, ist das meist die bessere Wahl. | S. 17, Abschn. 7 | Position |
| Leitlinie 6: Maschinell erstellte Bestandteile von Software und Daten müssen „eindeutig und in allen Serialisierungen" gekennzeichnet sein, besonders Vorhersagen ohne Postediting. | S. 17, Abschn. 7 | Position |
| Leitlinie 10: möglichst eigene oder geteilte Hardware; quelloffene Modelle „mit offengelegten Trainingsdaten und reproduzierbaren Ergebnissen" als Mittel der Wahl. | S. 18, Abschn. 7 | Position |
| Leitlinie 11: KI-Komponenten mit fachwissenschaftlicher Validierung begleiten, nach möglichst standardisierten Verfahren, damit die Ergebnisse auf festgelegtem Niveau bleiben. | S. 18, Abschn. 7 | Position |
| Leitlinie 2: Personenbezogene, urheberrechtlich geschützte und sicherheitsrelevante Daten nicht in externe Dienste einspeisen; Anbieter nutzten Prompts als Trainingsmaterial. | S. 16 bis 17, Abschn. 7 | Position |
| Deskilling: LLMs liefern Gesamtergebnisse statt Teilschritte; Fähigkeiten könnten prozedural verloren gehen; die Studienlage sei aber unübersichtlich. | S. 10, Abschn. 3 | referiert (Abbas et al. 2024; Reinmann 2023) |

## Daten, Methode, Zahlen

Keine Daten. Zahlen nur im Indikator (an der Textebene geprüft, S. 14 bis 15): Tab. 1 Risiko gering 1, begrenzt 2 (Chatbots und andere Generatoren, Nutzung daraus generierter Inhalte), hoch 3, unannehmbar ∞; Tab. 2 Ökologie 1 bis 4 (z. B. „Großes Modell punktuell genutzt" = 2, „Großes Modell dauerhaft genutzt" = 3); Tab. 3 Peripherie 1 („Zentraler Bestandteil des Projekts") bis 4. Rechenbeispiele im Text: Bildvorauszeichnung mit kontrolliertem Vokabular 2 Punkte, LLM-Paraphrase in einem juristischen Informationssystem 13 Punkte (S. 15); beide Rechnungen gehen mit der Formel auf. Fig. 2 (S. 16) ordnet die Punktzahlen ein [am PDF zu prüfen].

## Wörtliche Stellen

> „Als Konsequenz dieser Funktionsweise sind vermeintliche Optimierungen von Prompts nicht über verschiedene LLM-Angebote hinweg verallgemeinerbar." (S. 4)

> „Maschinell erstellte Bestandteile von Software und Daten müssen eindeutig und in allen Serialisierungen als solche gekennzeichnet sein." (S. 17)

> „Nach Möglichkeit sind quelloffene Modelle mit offengelegten Trainingsdaten und reproduzierbaren Ergebnissen das Mittel der Wahl." (S. 18)

## Bezug zur Dissertation

- **PROTOKOLL §4.10, Freeze 2 (LLM-Konfiguration):** S. 4 (Systemprompts, nicht übertragbare Prompt-Optimierung) und S. 18 (quelloffene Modelle für reproduzierbare Ergebnisse) stützen, Modell, Version und Prompt festzuschreiben und bei einem kommerziellen Modell die eingeschränkte Reproduzierbarkeit als Limitation zu nennen. Als Positionspapier ein normativer, kein empirischer Beleg.
- **PROTOKOLL §3, Ausschluss 1 (LLM-berührte Tokens):** Leitlinie 6 (S. 17) fordert die Kennzeichnung maschinell erzeugter Daten in allen Serialisierungen. Das Protokoll muss LLM-berührte Tokens per Git-Vergleich rekonstruieren, weil nicht jeder Ingest-Lauf eine Token-Liste führt (§3, Punkt 1). Ein Argument für die Dissertation, dass künftige LLM-Annotation der MHDBDB im TEI selbst gekennzeichnet sein sollte.
- **Leitlinie 11 (S. 18) und PROTOKOLL §9.2:** „fachwissenschaftliche Validierung nach möglichst standardisierten Verfahren" ist genau, was der doppelt annotierte Goldstandard leistet; zitierbar als DH-institutionelle Forderung.
- **Risikoindikator, angewandt auf die Pipeline (eigene Rechnung, nicht im Papier):** LLM-WSD wäre nach Tab. 1 eher „begrenzt" (2, Nutzung generierter Inhalte), nach Tab. 2 „Großes Modell punktuell genutzt" (2), nach Tab. 3 „zentraler Bestandteil" (1): (2 × 2) + (2 × 1) − 2 = 4. Nur als Illustration; die Einstufung ist eine Lesart.
- **Leitlinie 4 (Rule of Least Power, S. 17) und PROTOKOLL §1:** Die Forschungsfrage misst das LLM gegen die MFS-Baseline; erst ein deutlicher Abstand rechtfertigt den Ressourceneinsatz. Das Papier liefert dafür die Begründung aus Sicht einer DH-Einrichtung.
- **Leitlinie 2 (S. 16 bis 17):** Ob die mittelhochdeutschen Editionstexte an einen externen Dienst gehen dürfen, ist eine Rechtefrage pro Text (Lizenz der Edition). Für die Dissertation zu klären, bevor Freeze 2 ein kommerzielles Modell festlegt.

## Grenzen und Einwände

- Positionspapier ohne Begutachtung, zum Zeitpunkt v0.9.1 noch vor 1.0; mehrere Versionen im Umlauf, Seitenangaben je Version prüfen.
- Stark wertende Diskurs- und Ideologiekritik (Abschn. 2 und 3) mit Belegen überwiegend aus Presse und Firmenseiten; für die Dissertation tragen nur Abschnitte 1, 6 und 7.
- Der Indikator ist ungeeicht; Gewichte und Formel sind gesetzt, nicht begründet.
- Keine Aussage zu WSD, Annotation historischer Sprache oder Evaluation im Einzelnen.

## Weiterführend

- Liesenfeld & Dingemanse 2024, *Rethinking Open Source Generative AI: Open-Washing and the EU AI Act*, FAccT '24, S. 1774 bis 1787 (S. 9, 19): Offenheitsgrade von LLMs, relevant für die Modellwahl.
- Bender et al. 2021, *Stochastic Parrots* (S. 4, 11, 19).
- Canfora & Ottmann 2020, *Risks in Neural Machine Translation*, Translation Spaces 9(1) (S. 14, 19): risikobasierter Ansatz als Vorbild.
- Reinmann 2023, Deskilling, Hochschulforum Digitalisierung (S. 10, 20).
