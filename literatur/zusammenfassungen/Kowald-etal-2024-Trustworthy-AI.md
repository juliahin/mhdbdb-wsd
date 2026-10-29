# Kowald et al. 2024: Establishing and Evaluating Trustworthy AI

**Datei:** `pdf/Kowald-etal-2024-Trustworthy-AI.pdf` (nur lokal; Verlags-PDF, 21 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, Abschnitte 1 bis 2, 3.1, 3.3, 3.4, 3.6 und 4 an der Textebene gelesen, 3.2 (Fairness) und 3.5 (Privacy) nur überflogen; DOI über doi.org und Crossref geprüft.

Seitenzählung: PDF-Seite n = gedruckte S. n (Fußzeile „01" bis „21").

## Bibliografie

- **Vollständig:** Kowald, Dominik; Scher, Sebastian; Pammer-Schindler, Viktoria; Müllner, Peter; Waxnegger, Kerstin; Demelius, Lea; Fessl, Angela; Toller, Maximilian; Mendoza Estrada, Inti Gabriel; Šimić, Ilija; Sabol, Vedran; Trügler, Andreas; Veas, Eduardo; Kern, Roman; Nad, Tomislav & Kopeinik, Simone (2024). Establishing and evaluating trustworthy AI: overview and research challenges. *Frontiers in Big Data* 7, Artikel 1467222.
- **DOI/URL:** https://doi.org/10.3389/fdata.2024.1467222 (löst auf frontiersin.org auf; Crossref: Frontiers Media SA, Band 7, Artikelnummer 1467222, 29.11.2024, 16 Autor:innen, CC BY 4.0) ✔ (PDF S. 1 und Crossref). Eingereicht 19.07.2024, angenommen 11.11.2024 (S. 1).
- **Art:** begutachteter Übersichtsartikel (Typ „Review", drei Gutachter:innen auf S. 1 genannt)
- **Sprache:** Englisch

## Worum es geht

Der Artikel ordnet die Literatur zu vertrauenswürdiger KI nach sechs Anforderungen: menschliche Handlungsfähigkeit und Aufsicht, Fairness, Transparenz und Erklärbarkeit, Robustheit und Genauigkeit, Privatsphäre und Sicherheit, Rechenschaft (Abstract, S. 1). Zu jeder gibt er Definition, Methoden zum Herstellen und zum Evaluieren sowie offene Fragen. Fünf übergreifende Herausforderungen schließen ihn ab: Interdisziplinarität, begriffliche Klarheit, Kontextabhängigkeit, Dynamik lernender Systeme und Untersuchung im Realeinsatz (S. 15 bis 16). Grundlage ist eine halbstrukturierte Literaturübersicht von 183 Publikationen (S. 4).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Vier gemeinsame Grundprinzipien der Rahmenwerke: Respekt vor menschlicher Autonomie, Fairness, Erklärbarkeit, Schadensvermeidung; daraus die sechs Anforderungen. Reproduzierbarkeit, Nachhaltigkeit und Data Governance gelten als übergreifend und werden nicht eigens behandelt. | S. 3 bis 4, Abschn. 2.2 | Synthese (Smuha 2019; Kaur et al. 2021, 2022) |
| Formen menschlicher Beteiligung: human-in-command, -in-the-loop, -on-the-loop, -out-of-the-loop; Muster „AI Suggests, Human Intelligence Decides". | S. 5 bis 6, Abschn. 3.1.2 | referiert (Anders et al. 2022; Wang B. Y. et al. 2023) |
| Evaluation von Aufsicht als Stufenfolge: KI-Kompetenz, Verständlichkeit des Systems, tatsächliche Aufsicht in der Evaluation, Handlungsfähigkeit; die letzte sei am schwersten nachzuweisen. | S. 6, Abschn. 3.1.3 | eigener Vorschlag |
| Erklärungsmethoden werden anwendungs-, menschen- oder funktionsbezogen evaluiert; Eigenschaften u. a. Faithfulness und Robustheit. Für LLMs sei unklar, wie Erklärungen aussehen sollen. | S. 10, Abschn. 3.3.3 bis 3.3.4 | referiert (Doshi-Velez & Kim 2017; Schneider 2024) |
| Robustheit nach Huber: nahezu optimal im vorgesehenen Setting, nur leichte Verschlechterung bei kleinen Abweichungen, keine unsinnigen Ausgaben bei großen; meist Zielkonflikt zwischen Robustheit und Genauigkeit. | S. 10 bis 11, Abschn. 3.4.1 | referiert (Huber 2004) |
| Wahl der Zielmetrik, der Datenaufteilung und der Modellauswahl werde in der Praxis oft richtig gemacht, aber unzureichend dokumentiert; Vertrauen erfordere, jede Wahl samt Begründung zu dokumentieren (Beispiel: nicht nur „F1", sondern „unbalancierte Klassen"). | S. 11, Abschn. 3.4.2 | Position, mit Huber 2004; Hamon et al. 2020 |
| Es gibt keine allgemeine Genauigkeitsmetrik; Accuracy taugt bei balancierten Klassen, bei stark unbalancierten führt sie in die Irre. Metrik und Schwellen zu wählen sei schwierig, formale Richtlinien fehlten. | S. 11, Abschn. 3.4.3 bis 3.4.4 | Synthese |
| Rechenschaft nach Bovens: Akteur, Forum, Beziehung, Rechenschaftslegung, Konsequenzen; bewertbar etwa über den „accountability cube" aus Information, Diskussion und Sanktion. | S. 14 bis 15, Abschn. 3.6 | referiert (Bovens 2007; Brandsma & Schillemans 2012) |
| Vertrauenswürdigkeit ist kontextabhängig; Erkenntnisse lassen sich schwer übertragen, und zusammengesetzte Systeme können Anforderungen verletzen, auch wenn jede Komponente sie erfüllt. | S. 16, Abschn. 4 | eigene Synthese |
| Generative KI und LLMs stellen neue Herausforderungen; bestehende Methoden (z. B. Fairnessmetriken für binäre Klassifikation) müssten auf allgemeinere Settings übertragen werden. | S. 16, Abschn. 4 | Ausblick |

## Daten, Methode, Zahlen

- Methode (S. 4): explorative Recherche, dann pro Anforderung Scopus-Suche, Screening der 100 relevantesten Abstracts, Volltextscreening, Schneeballsuche und Google Scholar; Ausschluss überspezialisierter Arbeiten.
- 183 Publikationen: 20 Aufsicht, 35 Fairness, 47 Transparenz, 21 Robustheit, 37 Privatsphäre, 23 Rechenschaft (Abb. 3, S. 4; an der Textebene geprüft, Summe stimmt).
- Keine eigenen Experimente.

## Wörtliche Stellen

> „To generate trust in AI models, it is essential to both deliver quality and document all relevant choices made in the process." (S. 11)

> „Therefore, there is no single generally applicable accuracy metric." (S. 11)

## Bezug zur Dissertation

- **PROTOKOLL §4.10 und §8 (Dokumentation jeder Wahl):** S. 11 stützt die Praxis, Metrik, Datenaufteilung und Modellauswahl samt Begründung vorab festzuschreiben (Freeze 1 und 2, Abweichungslog §11). Allgemeine KI-Literatur, kein WSD-Beleg.
- **PROTOKOLL §9.2 (Metriken):** Die Warnung vor Accuracy bei unbalancierten Klassen (S. 11) passt zur Prävalenz dominanter Senses; das Protokoll antwortet darauf mit Macro-Genauigkeit nach Sense und der Auswertung auf Nicht-MFS-Items. Für die konkrete Begründung bleiben die WSD-Quellen maßgeblich, die PROTOKOLL §9.1 Punkt 4 und §9.2 schon nennen (Mihalcea et al. 2004; Maru et al. 2022).
- **Human-in-the-loop (S. 5 bis 6):** Die Typologie benennt die Rolle, die menschliche Prüfung bei einer späteren LLM-gestützten Annotation des D0-Teils hätte („AI suggests, human decides"). Für den Goldstandard selbst gilt das Gegenteil: Menschen annotieren blind, ohne LLM-Vorschlag (PROTOKOLL §6 Blindheit).
- **Robustheit (S. 10 bis 11):** Die Verschiebung von D1 nach D0 (PROTOKOLL §3, MFS aus D1 gelernt, auf D0 angewandt) ist eine Abweichung vom Trainingssetting im Sinn Hubers; Kowald et al. geben dafür einen allgemeinen Begriff, keine Messvorschrift.

## Grenzen und Einwände

- Breiter Überblick über alle KI-Systeme; für LLMs nur Ausblicke, für WSD oder Annotation nichts Spezifisches.
- Reproduzierbarkeit wird ausdrücklich ausgeklammert (S. 4); dafür ist Semmelrock et al. 2025 (`zusammenfassungen/Semmelrock-etal-2025-Reproducibility-ML.md`, mit Kopeinik und Kowald als Mitautor:innen laut `references.txt`) die einschlägigere Quelle.
- Literaturauswahl über Scopus-Relevanzranking und Schneeball; Auswahlkriterien („limited contributions") nicht operationalisiert.
- Abschnitte 3.2 und 3.5 hier nicht im Detail gelesen.

## Weiterführend

- Huber 2004, *Robust Statistics* (S. 10 bis 11): Robustheitsbegriff.
- Hamon et al. 2020, Robustheit und Erklärbarkeit (S. 11).
- Doshi-Velez & Kim 2017, Evaluation von Interpretierbarkeit (S. 10).
- Ala-Pietilä et al. 2020 / Radclyffe et al. 2023, ALTAI-Checkliste (S. 2).
- Long & Magerko 2020, KI-Kompetenz (S. 5 bis 6).
