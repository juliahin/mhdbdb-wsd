# Jacovi et al. 2023: Stop Uploading Test Data in Plain Text

**Datei:** `pdf/Jacovi-etal-2023-Stop-Uploading-Test-Data.pdf` (nur lokal; 10 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology 2023.emnlp-main.308 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 5074 + n (PDF 1 = S. 5075, PDF 10 = S. 5084). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Jacovi, Alon; Caciularu, Avi; Goldman, Omer & Goldberg, Yoav (2023). Stop Uploading Test Data in Plain Text: Practical Strategies for Mitigating Data Contamination by Evaluation Benchmarks. In: Houda Bouamor, Juan Pino & Kalika Bali (Hg.), *Proceedings of the 2023 Conference on Empirical Methods in Natural Language Processing*. Singapur: Association for Computational Linguistics, S. 5075 bis 5084.
- **DOI/URL:** 10.18653/v1/2023.emnlp-main.308 (aufgelöst, Crossref, 2026-11-16); https://aclanthology.org/2023.emnlp-main.308/ (Herausgeber:innen, Ort, Monat Dezember nach dem BibTeX der Anthology).
- **Lizenz:** CC BY 4.0 (ACL Anthology, Werke ab 2016, abgerufen 2026-11-16).
- **Art:** Konferenzbeitrag (Kurzbeitrag, Positionspapier mit Empfehlungen, keine Experimente). In `goldstandard/LITERATUR-IAA.md` noch als „arXiv:2305.10160“ zitiert; maßgeblich ist die Anthology-Fassung.
- **Sprache:** Englisch

## Worum es geht

Die Autoren gehen davon aus, dass Testdaten, die im Netz oder über die API eines geschlossenen Modells zugänglich sind, als kontaminiert gelten müssen, und schlagen drei Strategien vor, die einzelne Forschende selbst umsetzen können (S. 5075 bis 5076): (1) öffentlich gemachte Testdaten mit einem Schlüssel verschlüsseln und unter eine Lizenz ohne Bearbeitungen stellen, (2) geschlossene API-Modelle nicht evaluieren, solange es keine Zusage gibt, dass gesendete Daten nicht ins Training gehen, (3) keine Daten verwenden, deren Lösung im Netz neben ihnen steht, und bei Daten aus dem Netz deren Herkunftskontext mitveröffentlichen. Bestehende Wege (Leaderboards mit verborgenen Antworten, ganz neue Daten) seien teuer und mit der Zeit brüchig (S. 5077). Ein Anhang skizziert Testinstanzen aus Vorlagen als Teilstrategie (S. 5084).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Zwei Kontaminationsszenarien: (1) Trainingsdaten aus dem Netz gecrawlt; dazu zählt auch, wenn das Modell eine Form der Lösung gesehen hat, ohne die Daten wörtlich zu kennen; (2) geschlossene Modelle hinter einer API ohne Ausschlusszusage: jeder API-Aufruf mit Testdaten kompromittiert sie „for all models under the API holder and their affiliates“. | S. 5076, Abschnitt 2 | Position der Autoren |
| Annahme 1 (Vermutung der Kontamination): Was Crawlern zugänglich ist oder an eine API ohne Ausschlusszusage ging, gilt als kompromittiert. Annahme 2: alle Beteiligten sind aufrichtig, nicht feindselig. Annahme 3: Modelle, die aus anderen Modellen abgeleitet sind (Destillation, Gewichte, Ensembles), erben deren Kontamination. | S. 5076 | Setzung der Autoren |
| Auch bei Daten, die nach dem letzten Modellupdate entstanden sind, endet die Unbekanntheit beim ersten Evaluationsaufruf an eine geschlossene API; es gibt keine standardisierten Ausschlusskontrollen. | S. 5076, Abschnitt 3.1 | Position der Autoren |
| Erkennung (exakt oder unscharf) ist teuer, hat falsch Negative und ist reaktiv; die vorgeschlagenen Strategien, besonders Strategie 1, sind vorbeugend. | S. 5076 bis 5077, Abschnitt 3.2 | Argument, mit Verweisen (u. a. OpenAI 2023) |
| Leaderboards mit verborgenen Antworten schützen nur teilweise: Die Testdaten ohne Antworten bleiben im Netz und können wiederverwendet oder vom Modellentwickler selbst gelabelt werden; außerdem brauchen auch Entwicklungsdaten Schutz. | S. 5077, Abschnitt 3.3 | Argument |
| Strategie 1: Testdaten verschlüsselt hochladen, den Schlüssel daneben; einfachster Weg ein passwortgeschütztes Archiv (z. B. zip). Eine Lizenz mit „No Derivatives“-Klausel wie CC BY-ND 4.0 schützt vor Weitergabe ohne Verschlüsselung. | S. 5077, Abschnitt 4.1 | Empfehlung |
| Es geht um Schutz vor automatischem Crawlen, nicht vor Gegnern; der Schlüssel darf deshalb mit den Daten veröffentlicht werden. Warnung vor Verschleierung oder Kompression ohne Schlüssel, weil Crawler-Pipelines automatisch entpacken. | S. 5078 | Empfehlung |
| Datensatz-Plattformen sollen Testdaten nicht in ihrer Online-Ansicht zeigen; zur Präsentation genügt eine Auswahl bereits kompromittierter Beispiele. Fußnote: zugangsbeschränkte („gated“) Repositorien und Metadaten gegen Crawlen helfen, verhindern aber keine Weitergabe an schlechter geschützte Orte. | S. 5078, mit Fn. 9 | Empfehlung |
| Folgerung für Few-shot-Prompts: Prompts mit Daten sind wie Evaluationsdaten zu behandeln, nicht im Klartext ins Netz stellen „(including inside papers)“; vermutlich kompromittierte Prompts nicht wiederverwenden, sondern neue annotieren. | S. 5078 | Empfehlung |
| Strategie 2: Keine Testdaten an geschlossene API-Modelle ohne Ausschluss vom Training schicken. Zwischenlösung: billigere Einwegdaten (zurückgehaltene Trainingsdaten, synthetische Varianten) für eine weniger verlässliche Schätzung. | S. 5078, Abschnitt 4.2 | Empfehlung |
| Strategie 3: Daten aus dem Netz erscheinen dort mit ihrem Kontext; das Modell kann sich an diesen Kontext erinnern. Automatisch aus dem Kontext abgeleitete Labels sind trivial kontaminiert. Auch bei manueller Annotation gilt: Enthält der Ursprungskontext Hinweise auf die Lösung, kann das Modell „cheat the evaluation“. Zwei Schritte: (A) Kontextinformation mit den Daten veröffentlichen (als Dokumentation, nicht als Modelleingabe), (B) Instanzen erkennen und aus dem Benchmark nehmen, bei denen der Kontext die Lösung erheblich verrät. | S. 5078 bis 5079, Abschnitt 4.3 | Empfehlung |
| Benchmarks, die ältere Testsets bündeln, sollen Strategie 3 anwenden; eine Bestandsaufnahme der Netzpräsenz bestehender Evaluationsdaten sei nötig. Als nur teilweise wirksam genannt: eine Datenbank von Kontaminationsfällen, Wasserzeichen in Metadaten. | S. 5079, Abschnitt 5 | Vorschlag |
| Fahrlässigkeit kann jede Strategie aushebeln, z. B. wenn jemand eine Klartextfassung erneut hochlädt. Wer versehentlich Testdaten an eine geschlossene API geschickt hat, soll das öffentlich machen und die Verantwortlichen der Daten informieren; die Daten bleiben für andere Modelle unkompromittiert. | S. 5080, Limitations | Empfehlung |
| Was als Bearbeitung gilt, hängt vom lokalen Urheberrecht ab; die Lizenz soll Verschlüsselung bei aufrichtigen Akteuren fördern, nicht rechtlich erzwingen. Alternative: eine Lizenz, die Trainingsnutzung verbietet oder verschlüsselte Weitergabe verlangt, kann Bearbeitungen erlauben und doch ähnlich wirken wie „no derivatives“. | S. 5080, Limitations | Position der Autoren |
| Grenze der Annahme „aufrichtige Akteure“: Crowdworker könnten Labels gegen die Richtlinien mit frei verfügbaren API-Modellen wie ChatGPT erzeugen und damit die Daten kompromittieren. | S. 5080 | Überlegung der Autoren |
| Teilstrategie A (Anhang): Testinstanzen als Vorlagen, pro Evaluationsdurchgang eine kontrafaktische Variante per Seed ziehen; der Seed verfällt nach der Evaluation. | S. 5084 | Vorschlag |

## Daten, Methode, Zahlen

Keine eigenen Experimente. Einzige Zahl aus eigener Erhebung: Bei fünf zufällig gewählten Datensätzen mit Leaderboard des Allen Institute for AI zitierten im Mittel 4,2 Modelle die Datensätze, ohne Ergebnisse beim Leaderboard einzureichen; sie nutzten stattdessen die Entwicklungsdaten (S. 5077, Fn. 6). Stand der API-Regeln in Fn. 3 (S. 5075): OpenAI mit Ausschlusszusage für bestimmte API-Aufrufe ab 1. März 2023, nicht für ChatGPT-Weboberfläche; Bard ohne Zusage „as of this writing“. Diese Angaben sind zeitgebunden und für heutige Anbieter nicht übertragbar.

## Wörtliche Stellen

> „Test data made public should be encrypted with a public key and licensed to disallow derivative distribution“ (S. 5075, Abstract)

> „Therefore, the encryption key can be safely released with the encrypted data“ (S. 5078)

> „we should consider prompts with data as evaluation data: Avoid uploading them to the internet in plain text (including inside papers).“ (S. 5078)

> „If the original context of the test instance contains information that can be helpful to the model in solving the instance, the model can use this context to cheat the evaluation, even if the solution was manually annotated.“ (S. 5079)

> „we should be conscious of who and what can access our test data, and plan accordingly.“ (S. 5079)

## Bezug zur Dissertation

**1. PROTOKOLL §10 und DMP §5 (Labels privat, bei Veröffentlichung verschlüsselt).** Gestützt: Verschlüsselung mit veröffentlichtem Schlüssel (S. 5077 bis 5078) und eine Lizenz gegen unverschlüsselte Weitergabe. Drei Abweichungen im Wortlaut des Protokolls:
- **Canary-String:** steht in diesem Werk nicht (ganze Textebene durchsucht). §10, DMP §5 und `LITERATUR-IAA.md` (Zeile „Kontamination“) schreiben ihn Jacovi et al. zu. Eine Quelle für den Canary fehlt bisher in `literatur/`.
- **„Lizenz ohne Weiterverbreitung“:** Jacovi et al. empfehlen eine Lizenz ohne *Bearbeitungen* (CC BY-ND 4.0, S. 5077), die Weitergabe der verschlüsselten Fassung bleibt erlaubt; als Alternative eine Lizenz, die Trainingsnutzung verbietet oder verschlüsselte Weitergabe verlangt (S. 5080). „Ohne Weiterverbreitung“ geht darüber hinaus. Für die offene Frage im DMP §5 (Verträglichkeit mit CC BY-NC-SA) ist die Alternative von S. 5080 einschlägiger als ND: Ein ND-Vorbehalt verträgt sich vermutlich nicht mit einer Bearbeitung, die unter gleichen Bedingungen weitergegeben werden muss (DMP §4). Das ist eine rechtliche Frage, die das Werk nicht beantwortet; es sagt selbst, der Begriff der Bearbeitung hänge vom lokalen Recht ab (S. 5080).
- **„Passwort in der Publikation“:** Das Werk legt den Schlüssel neben die verschlüsselten Daten (S. 5077 bis 5078). Beides ist mit dem Zweck (Schutz vor Crawlern) verträglich; im Artikel-PDF steht der Schlüssel dann ebenfalls im Netz, was das Werk ausdrücklich zulässt.

**2. PROTOKOLL §10, Satz „Die mittelhochdeutschen Texte sind ohnehin online; zu schützen sind die Labels.“** Strategie 3 (S. 5078 bis 5079) verschärft das: Kompromittiert ist auch eine Instanz, deren *Lösung* im Netz neben ihr steht, selbst wenn das Gold neu und manuell erhoben ist. In der Domäne D1 (Abschnitt 3, A10) steht neben jedem Token das Silber-`@ana` im öffentlichen MHDBDB-Korpus. Für die unannotierten polysemen Tokens, also vor allem D0, verrät die öffentliche Typliste an `<sense>` in `lexicon.xml` bei 86 % einen Sense (`knowledge/data.md`, B1). Beides ist nicht Gold, kann ihm aber oft entsprechen. Nach Annahme 1 (S. 5076) ist ein Modell, dessen Trainingsdaten Korpus und Lexikon enthalten könnten, so zu behandeln, als kenne es Silber und Typlisten. Vorschläge: (a) den Satz in §10 präzisieren (zu schützen sind die neuen Labels; Kontext und Silber sind öffentlich und mögliche Lösungshinweise); (b) in der Auswertung den Vergleich LLM gegen Gold getrennt für D1 und D0 berichten und die Übereinstimmung des LLM mit Silber (D1) und mit dem Typlisten-Sense (D0), gerade dort, wo beide vom Gold abweichen, als Hinweis auf Kontamination ausweisen (Schritt B von Strategie 3 als Diagnose, nicht als Ausschluss, weil D1 Teil des Designs ist); (c) Strategie 3 (A) entspricht schon dem öffentlichen Manifest mit Korpus-Commit.

**3. Pilot-Items im öffentlichen Fork (`goldstandard/pilot/items-pilot.json`: Kontext, Karten mit Sense-IDs, `xml_id`; `manifest-pilot.json` mit Domäne D1/D0).** Was das Werk dazu sagt:
- Testdaten ohne Antworten im Netz sind nur ein Teilschutz (S. 5077); auch Entwicklungsdaten brauchen Schutz (S. 5077). Der Pilot ist Entwicklungsmaterial (A17: Prompt-Wahl am Pilot-Pool) und geht nicht ins Gold; sein Schutzbedarf ist daher kleiner als der der Hauptstichprobe.
- Über die öffentlichen `xml_id` lässt sich zu jedem Pilot-Item aus D1 das Silber-`@ana` im öffentlichen Korpus nachschlagen. Damit liegt für diese Items ein Lösungshinweis im Netz (Strategie 3). Für die Hauptstichprobe gilt dasselbe, sobald ihr Manifest mit Token-IDs veröffentlicht wird (§10, Zeile „Manifest“).
- Plattform-Ansicht: GitHub zeigt JSON im Klartext an; das Werk empfiehlt, Testdaten nicht in Online-Ansichten zu zeigen (S. 5078). Für den Pilot bedeutet das wenig; für Labels und LLM-Ausgaben nach der Veröffentlichung spricht es für das verschlüsselte Archiv statt Klartext im Repo.
- Vorschlag: Vor dem Veröffentlichen des Manifests der Hauptstichprobe entscheiden, ob die Token-IDs bis zum Abschluss der LLM-Läufe zurückgehalten werden (Prüfsumme öffentlich, Liste privat), damit Präregistrierung und Schutz zusammengehen. Für den Pilot genügt ein Hinweis im Datasheet.

**4. Strategie 2 (geschlossene APIs) und PROTOKOLL §4.10, A26, DMP §4 (LLM-Nutzung).** Der DMP hält die Nutzungsbedingungen pro Lauf fest, sagt aber nicht, ob gesendete Daten vom Training ausgeschlossen sind. Nach S. 5076 und 5078 kompromittiert schon der erste API-Aufruf die Testdaten für alle späteren Modelle desselben Anbieters. Vorschlag: In Freeze 2 die Ausschlusszusage des Anbieters (Datenverwendung der API) mit Datum festhalten; Pilot-Läufe zuerst; die Hauptstichprobe möglichst in einem Durchgang pro Anbieter. Gleiches gilt für KI-Werkzeuge, mit denen an den privaten Labels gearbeitet wird (Auswertungsskripte, Assistenz-Sitzungen): Auch sie senden Daten an eine API. Ob das für die hier genutzten Werkzeuge zutrifft, ist nicht geprüft.

**5. Hilfsmittelregel der Kurzanleitung (A30, offener Punkt 17: keine KI-Werkzeuge).** Gestützt durch S. 5080: Annotierende, die Labels mit einem frei verfügbaren API-Modell erzeugen, kompromittieren die Daten.

**6. Few-shot-Beispiele (A17).** Few-shot-Prompts mit Daten sind wie Evaluationsdaten zu behandeln und nicht im Klartext zu veröffentlichen, auch nicht im Artikel (S. 5078). Wenn der Prompt-Wortlaut in Freeze 2 öffentlich festgeschrieben wird, sollten Beispiele mit Silber-Label darin verschlüsselt oder nur als Prüfsumme stehen.

**7. Abgleich mit `goldstandard/LITERATUR-IAA.md`** (Zeile „Kontamination: Testdaten nicht im Klartext veröffentlichen; verschlüsseln, Lizenz, Canary“, Jacovi et al. 2023 ✔): Klartext, Verschlüsselung und Lizenz gedeckt (S. 5075, 5077 bis 5078); **Canary nicht gedeckt**. Die Literaturangabe dort nennt arXiv statt EMNLP 2023, S. 5075 bis 5084.

## Grenzen und Einwände

- Positionspapier ohne Messung der Wirksamkeit; dass Verschlüsselung Crawler fernhält, wird angenommen, nicht gezeigt (S. 5077 bis 5078).
- Die Annahme aufrichtiger Akteure (S. 5076) lässt absichtliches Umgehen außen vor.
- Die API-Angaben (S. 5075, Fn. 3) sind Stand 2023.
- Für bereits öffentliche Korpora mit vorhandener Annotation (wie das MHDBDB-Korpus mit Silber) bietet das Werk nur Strategie 3 an; es diskutiert nicht, wie man eine neue Annotation auf einem Text evaluiert, dessen ältere Annotation im Netz steht.
- Kein Bezug zu WSD, historischen Sprachen oder Mehrfachlabels.

## Weiterführend

- Magar & Schwartz 2022, Data contamination: From memorization to exploitation, ACL (S. 5075): Belege für Kontamination.
- Dodge et al. 2021, Documenting large webtext corpora (C4), EMNLP (S. 5075): Testdaten in C4.
- Carlini et al. 2021 und 2023b (S. 5076 bis 5077): Extraktion und Memorierung.
- Marone & Van Durme 2023, Data Portraits; Piktus et al. 2023, ROOTS search tool (S. 5076, Fn. 5): Werkzeuge zum Prüfen von Trainingsdaten.

## Julias Notizen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
