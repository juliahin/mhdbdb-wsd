# Scholger & Bleier 2026: ChatGPT als Assistent für digitales Edieren (RIDE-Rezension)

**Datei:** `pdf/Scholger-Bleier-2026-ChatGPT-RIDE.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, Volltext (32 Seiten) an Textebene gelesen, Abb. 1 und 4 sowie Factsheet S. 28 am Seitenbild geprüft; DOI über DataCite aufgelöst, RIDE-Artikelseite auf Korrektur oder Rückzug geprüft. Keine Markierungen von Julia im PDF.

**Zitierweise:** Das PDF ist ein Druck der RIDE-Webseite (Fußzeile „Accessed: 26.03.2026"). Es trägt fortlaufende Seitenzahlen, die mit den PDF-Seiten übereinstimmen, und die von RIDE vergebenen Absatznummern 1 bis 41 (die RIDE-Seite empfiehlt, mit diesen Nummern zu zitieren). Zitiert wird deshalb „Abs. n (S. m)"; für Anmerkungen „Anm. n", für das Factsheet nur die Seite.

## Bibliografie

- **Vollständig:** Scholger, Martina & Roman Bleier, 2026. ChatGPT as an Assistant for Digital Scholarly Editing. *RIDE. A Review Journal for Digital Editions and Resources* 19 (Issue 19: Tools and Environments, hg. von Roman Bleier und Stefan Dumont).
- **DOI/URL:** https://doi.org/10.18716/ride.a.19.4, löst am 2026-10-28 auf https://ride.i-d-e.de/issues/issue-19/chatgpt/ auf. ✔ DataCite: Titel „ChatGPT as an assistant for digital scholarly editing", Verlag Institut für Dokumentologie und Editorik e.V., Jahr 2026, Version 1.0, Teil von 10.18716/ride.a.19. Laut RIDE-Artikelseite veröffentlicht im März 2026; kein Hinweis auf Korrektur, Aktualisierung oder Rückzug (Seite und DataCite am 2026-10-28 abgerufen).
- **Titelform:** Der Zitiervorschlag im PDF lautet „Review of ‘ChatGPT as an Assistant for Digital Scholarly Editing’" (Fußzeile jeder Seite), der Zitiervorschlag der Webseite „Chat GPT as an assistant …", DataCite „ChatGPT as an assistant …". `references.txt` (`ScholgerBleier2026`) folgt DataCite und ist damit korrekt; Band, Herausgeber und DOI stimmen.
- **Art:** Rezension (Werkzeugrezension mit Kriterienkatalog und Factsheet). Begutachtung: ○. Die Artikelseite sagt nichts zu einem Peer Review; ein Call for Reviews der RIDE-Tools-Reihe (E-Mail-Liste EADH, 23.04.2021) sagt: „All reviews will be peer reviewed". Für diesen Beitrag nicht belegt. Hinweis: Roman Bleier ist Mitautor und zugleich Herausgeber von Issue 19 (Issue-Seite und Zitiervorschlag der Artikelseite).
- **Sprache:** Englisch

## Worum es geht

Die Rezension bewertet ChatGPT als Assistenzwerkzeug für digitales Edieren aus der Sicht von Editor:innen, die die Weboberfläche nutzen, nicht die API (Abs. 3, S. 2). Sie beschreibt Architektur, Transparenz, Reproduzierbarkeit, Prompting, Konfiguration, Formate und Ethik und ordnet den Einsatz in die Editionspipeline des IDE ein (Abs. 4 bis 20, 29 bis 37). Zwei eigene, kleine Versuche mit GPT-4o kodieren je einen Brief in TEI (Hammer-Purgstall 1794, Reichstag 1576 auf Frühneuhochdeutsch) und lassen Personen und Orte mit Normdaten erkennen (Abs. 21 bis 28). Ergebnis: Die Struktur wird gut erkannt, aber Text fehlt, Abkürzungen werden falsch behandelt, Normdaten-IDs werden erfunden, und historisches Sprachmaterial funktioniert schlechter (Abs. 27, 28, 41). ChatGPT eigne sich für explorative und vorbereitende Schritte, nicht für endgültige editorische Entscheidungen; ein Mensch müsse im Loop bleiben (Abs. 18, 41).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Alle Versuche liefen in der Weboberfläche mit GPT-4o, Zugriff zwischen Juli 2024 und Juli 2025, im Free- und im Plus-Tarif; die Rezension sei eine zeitgebundene Momentaufnahme. | Abs. 3 (S. 2 bis 3); Abs. 39 (S. 19) | eigene Angabe |
| Während der Überarbeitung des Artikels änderten sich Standardmodelle und Funktionen der Tarife deutlich. | Abs. 2 (S. 2) | eigene Beobachtung |
| Trainingsdaten sind nicht offengelegt, die Modelle nicht offen verfügbar. | Abs. 5 (S. 3) | referiert (OpenAI, Anm. 4) |
| Auch bei identischen Prompts liefert ChatGPT nicht verlässlich identische Ausgaben; das erschwert Dokumentation, Prüfung und Nachvollziehbarkeit editorischer Entscheidungen. | Abs. 5 (S. 3) | Einschätzung, gestützt auf Ouyang et al. 2023 |
| Mehrere Modellversionen in einer Plattform, Nutzungsgrenzen und automatischer Rückfall auf ein kleineres Modell fügen eine weitere Ebene der Unvorhersehbarkeit hinzu. | Abs. 6 (S. 3) | Beschreibung (Stand Juni 2025) |
| Unsichtbare System-Prompts formen das Modellverhalten; sorgfältiges Prompting ist für konsistente Ergebnisse bei formalisierten Ausgaben und Fachkonventionen nötig. | Abs. 7 (S. 4) | Beschreibung, referiert (Saravia 2022; Pollin 2025) |
| Tokenisierung ist sprachabhängig; relevant für historische Texte in anderen Sprachen als modernem Englisch. | Abs. 9 (S. 4) | Einschätzung |
| Open-Weight und Open-Source sind zu unterscheiden; für Editionen zählt das für Nachhaltigkeit, Prüfbarkeit und Nachnutzung. | Abs. 15 (S. 6) | Einschätzung, referiert (Ramlochan 2023) |
| ChatGPT unterstützt vor allem explorative und vorbereitende Schritte, nicht endgültige Entscheidungen, weil Nichtdeterminismus und fehlende stabile Versionierung die Reproduzierbarkeit begrenzen. Nichtreproduzierbarkeit könne als „digitale Hermeneutik" genutzt werden: mehrere Fassungen erzeugen und vergleichen. | Abs. 18 (S. 7) | Einschätzung der Autor:innen |
| Neuere Arbeiten betonen robuste Pipelines und systematische Evaluation, u. a. zur Qualität LLM-gestützter TEI-Kodierung (Strutz und Vogeler 2025; Strutz forthcoming) und zu NER (Galka und Vogeler 2026). | Abs. 20 (S. 8) | referiert |
| TEI-Versuch 1 (Brief 1794): Briefstruktur richtig erkannt, Datum normalisiert, Anmerkungen an der richtigen Stelle eingebettet; Personennamen unzuverlässig, ungefragt ein Ort ausgezeichnet. Risiken: unvollständiger Texterhalt, Umstellen von Datum oder Unterschrift nach typischen Brieflayouts. | Abs. 23 (S. 11); Abb. 1 (S. 10), Abb. 2 (S. 11) | eigenes Ergebnis (ein Brief, Anzahl der Läufe nicht genannt) |
| TEI-Versuch 2 (Frühneuhochdeutsch, 1576): Im ersten Lauf wurde der Text ins Standarddeutsche normalisiert; erst die Anweisung „keep the original language" verhinderte das. Struktur „reasonably well" erkannt. | Abs. 26 (S. 13 bis 14); Abb. 3 (S. 13) | eigenes Ergebnis |
| Im Ergebnis fehlt Text (Präsentationsvermerk); manche Abkürzungen richtig aufgelöst, andere nicht erkannt, normale Wörter („ewern", „bevelch", „instruction") fälschlich als Abkürzungen behandelt; Daten korrekt mit `@when`, aber ohne Rücksicht auf die Kalenderreform. | Abs. 27 (S. 14) | eigenes Ergebnis |
| Normdaten: zunächst nur eine Person richtig mit GND/VIAF; die beiden GND-Nummern für Regensburg und Wien „do not actually exist"; mit GeoNames werden beide Orte richtig identifiziert. | Abs. 28 (S. 15); Abb. 4 (S. 14), Abb. 5 (S. 15) | eigenes Ergebnis |
| Verantwortung: Das Werkzeug kann Fehler und nicht beabsichtigte Interpretationen der Quelle einführen; Prinzipien vertrauenswürdiger KI (Transparenz, Rechenschaft, Verlässlichkeit, Fairness) gelten auch hier. | Abs. 34 (S. 17) | Einschätzung, referiert (AI HLEG 2019; Pope 2024; Stahl & Eke 2024) |
| Datenschutz: Es ist unklar, ob und wie Eingaben fürs Training genutzt werden; unveröffentlichtes oder sensibles Material sollte nicht geteilt werden. | Abs. 35 (S. 17); Abs. 40 (S. 19) | Einschätzung, referiert (Merton-McCann 2023) |
| Zitierbarkeit: Chats haben keine Permalinks, keine DOI; empfohlen wird, Prompt oder ganze Unterhaltung z. B. im Anhang beizulegen. | Abs. 36 (S. 18); Anm. 18 bis 20 | referiert (APA; Universität Graz) |
| Bias: Trainingsdaten überwiegend nordamerikanisch und europäisch; Vorsicht bei kulturell sensiblem oder historisch situiertem Material. | Abs. 37 (S. 18) | referiert (UNESCO 2023; OpenAI) |
| Grenzen: geschlossenes Produkt als Blackbox, nur über Prompts steuerbar; schlecht gebaute Prompts liefern irreführende oder „totally wrong" Ergebnisse; mehrstufige Workflows für ganze Korpora nur über die API sinnvoll, deren Kosten nicht jedes Projekt trägt; Forderung nach mehr Open-Source-Modellen. | Abs. 40 (S. 19) | Schlussfolgerung |
| Es gibt noch wenig Forschung und Benchmarks zu LLMs für editorische Zwecke. | Abs. 39 (S. 19) | Einschätzung |
| Ein menschlicher Editor muss im Loop bleiben; der kleine Versuch mit zwei historischen Sprachstufen zeige, dass ChatGPT mit nicht standardisiertem und historischem Sprachmaterial weniger gut arbeitet. | Abs. 41 (S. 19) | Schlussfolgerung aus eigenem Versuch |
| Factsheet: kein offener Code, keine Lizenz („all rights reserved"), keine Testsuite, keine Zitierrichtlinien, keine ausreichende Information zur Datenbehandlung, keine Angabe zur künftigen Pflege; Finanzierungsmodell trotzdem „Free/open". | S. 28 bis 32 (Factsheet; S. 28 am Seitenbild geprüft) | eigene Bewertung nach RIDE-Kriterienkatalog |

## Daten, Methode, Zahlen

- **Kriterien:** RIDE-Kriterienkatalog für Werkzeuge; das Factsheet verweist auf dessen Nummern („cf. Catalogue 0.1.1" bis „4.5", S. 28 bis 32). Abschnitte des Textes: Methoden und Implementierung (Training, Transparenz, Reproduzierbarkeit; Interaktion und Prompting; Konfiguration; Ein- und Ausgabe; Einordnung in die LLM-Landschaft), Anwendung im Edieren, Nutzererfahrung und Ethik (Zugang, Dokumentation, Mehrsprachigkeit, Barrierefreiheit, Datenhoheit, Zitierbarkeit, Bias), Fazit.
- **Material:** zwei Briefe aus Editionen, an denen die Autor:innen beteiligt sind: Hammer-Purgstall an Jenisch, 20.02.1794 (Abs. 22, S. 8 bis 9) und Bericht der Gesandten Eulenbeck und Paulus an Kurfürst August von Sachsen, 09.05.1576, Frühneuhochdeutsch (Abs. 24 bis 25, S. 12 bis 13).
- **Prompt (Abb. 1, S. 10, am Seitenbild geprüft):** fünf Teile: Rolle („As an expert in TEI encoding"), Aufgabe, Kodierregeln (u. a. `@ref` auf Normdaten „only if you are sure that it is the correct reference"), Ausgabebedingungen („preserve the original text in its entirety"), „emotional prompting" („Take a deep breath and work step by step"). Beschreibung in Abs. 23 (S. 11).
- **Modell und Zugang:** GPT-4o, Weboberfläche, Free und Plus, Juli 2024 bis Juli 2025 (Abs. 3, S. 2 bis 3; Abs. 21, S. 8). Keine Angaben zu Temperatur, Zahl der Läufe oder Datum des einzelnen Laufs.
- **Bewertung:** qualitative Durchsicht durch die Autor:innen; keine Metrik, keine Zählung, kein Vergleichsmaßstab.
- **Zahl im Text:** Whisper sei auf 98 Sprachen trainiert, nur für etwa 58 liege die Wortfehlerrate unter 50 % (Abs. 31, S. 17; referiert nach OpenAI, Anm. 15).

## Wörtliche Stellen

> „Even when identical prompts are used, ChatGPT does not reliably produce identical outputs." (Abs. 5, S. 3)

> „The presence of multiple model versions within a single platform therefore introduces an additional layer of unpredictability for scholarly workflows." (Abs. 6, S. 3)

> „ChatGPT primarily supports exploratory and preparatory stages of editorial work rather than final, authoritative decisions, as its nondeterministic nature and lack of stable versioning limit scholarly reproducibility." (Abs. 18, S. 7)

> „The GND identifiers provided by ChatGPT for the two places do not actually exist" (Abs. 28, S. 15)

> „It shows that ChatGPT works less effectively with nonstandard and historical language material." (Abs. 41, S. 19)

## Bezug zur Dissertation

- **Protokoll 4.10 (Freeze 2, LLM-Konfiguration) und `PROMPT-LOG.md` Ebene A:** Die Rezension begründet aus der Praxis, warum die Weboberfläche für reproduzierbare Läufe ungeeignet ist: wechselnde Standardmodelle (Abs. 2), Modellwahl und automatischer Rückfall je nach Tarif (Abs. 6), unsichtbare System-Prompts (Abs. 7), keine identischen Ausgaben bei identischem Prompt (Abs. 5). Das stützt die Felder `modell` (exakte Snapshot-ID), `parameter` und `ausgabe_roh` im Prompt-Log und spricht dafür, in Freeze 2 ausdrücklich einen API-Zugang festzuschreiben (Folgerung, steht so nicht in der Rezension; sie selbst sagt nur, Korpus-Workflows seien nur über die API sinnvoll, Abs. 40).
- **Protokoll 4.10 „Anzahl der Läufe pro Item":** Die Idee, Nichtreproduzierbarkeit als „digitale Hermeneutik" zu nutzen (Abs. 18), ist ein Argument, Mehrfachläufe nicht nur als Rauschen, sondern die Streuung pro Item als Information zu berichten. Für den gepaarten Vergleich mit MFS muss aber vorab feststehen, welcher Lauf zählt (so bereits `PROMPT-LOG.md`, Mehrfachläufe).
- **Protokoll 9.2 (Abstinenz und Ausweichlabels):** Die erfundenen GND-Nummern (Abs. 28) sind das Editions-Gegenstück zu einer Sense- oder Begriffs-ID, die im Menü des Lemmas nicht vorkommt. Das Protokoll regelt Abstinenz bei Ausweichlabels, aber nicht ausdrücklich Ausgaben außerhalb des Menüs oder unparsbare Antworten; das gehört in die Bewertungsregeln vor Freeze 2 (Folgerung; siehe auch die Zusammenfassung zu Strutz 2026, Dimension 0).
- **Mittelhochdeutsch:** Der Befund, dass das Modell Frühneuhochdeutsch ungefragt ins Standarddeutsche normalisiert (Abs. 26) und mit historischem Material schlechter arbeitet (Abs. 41), ist ein Hinweis, dass ein LLM mittelhochdeutsche Wörter neuhochdeutsch lesen könnte. Für WSD ist das eine Hypothese, die die Rezension nicht prüft; sie beruht auf einem Brief.
- **Protokoll 10 (Ablage, Kontamination):** Die Warnung, unveröffentlichtes Material nicht an kommerzielle Anbieter zu geben (Abs. 35, 40), betrifft hier vor allem Labels und Adjudikation, die nie in einen Prompt gehören; die Texte sind laut Protokoll 10 ohnehin öffentlich. Die Datennutzungsbedingungen des gewählten API-Zugangs sollten im DMP dokumentiert werden (Folgerung).
- **`PROMPT-LOG.md` Ebene B:** Die Empfehlung, Prompt oder Unterhaltung beizulegen, weil Chats nicht zitierbar sind (Abs. 36), entspricht dem Vorgehen dort.
- **Verhältnis zu Galka & Vogeler 2026:** Die Rezension zitiert diese Arbeit (Abs. 20) und kommt mit GPT-4o im Chat zu ähnlichen Fehlerarten (Texterhalt, Normdaten), aber ohne Gold und ohne Zahlen. Galka & Vogeler liefern die gemessene Fassung; die Rezension ist für die Dissertation eher Beleg für die Reproduzierbarkeitsprobleme als für Leistungswerte.

## Grenzen und Einwände

- **Anekdotische Evidenz:** zwei Briefe, ein Modell, Weboberfläche, unbekannte Zahl der Läufe, keine Metrik und kein Gold. Die Aussage über historische Sprache (Abs. 41) stützt sich auf genau diesen Vergleich zweier Briefe.
- **Begriff Halluzination:** Die Rezension verwendet das Wort nicht. Sie spricht von erfundenen Normdaten-IDs (Abs. 28), fehlendem Text (Abs. 23, 27), „misleading or even totally wrong" Ergebnissen (Abs. 40) und ungewollten Interpretationen (Abs. 34). Wer sie für „Halluzination" zitiert, sollte die konkrete Stelle nennen.
- **Nähe der Beteiligten:** Die Autor:innen sind an beiden getesteten Editionen beteiligt (Abs. 3), Bleier ist zugleich Herausgeber von Issue 19. Peer Review für diesen Beitrag ist nicht ausgewiesen (siehe Bibliografie).
- **Factsheet-Spannung:** Finanzierungsmodell „Free/open" (S. 28) neben „No explicit license / all rights reserved" und geschlossenem Code (S. 30). Gemeint ist wohl der kostenlose Zugang, das steht aber nicht dort.
- **Zeitgebundenheit:** von den Autor:innen selbst betont (Abs. 3, 39); GPT-4o ist für 2026er Experimente nicht mehr der Stand.
- **Übertragbarkeit:** TEI-Kodierung und NER sind Aufgaben mit offenem Ausgaberaum; WSD gegen ein festes Menü schränkt die Ausgabe stärker ein. Die Reproduzierbarkeitsargumente gelten trotzdem unverändert.

## Weiterführend

- Strutz 2026, JOHD 12, Artikel 39 (in der Rezension als „Strutz forthcoming", Abs. 20, S. 26): eigene Zusammenfassung `Strutz-2026-LLM-TEI-Evaluation.md`.
- Strutz & Vogeler 2025, DH 2025, Zenodo 10.5281/zenodo.16364518 (Abs. 20; S. 26). Achtung: Der Zenodo-Datensatz nennt nur Sabrina Strutz als Urheberin (am 2026-10-28 abgerufen), Strutz 2026 zitiert ihn ebenfalls nur unter Strutz; die Autorschaft „Strutz and Vogeler" in der Rezension ist damit ✘ gegenüber Zenodo.
- Ouyang, Zhang, Harman & Wang 2023, Nichtdeterminismus von ChatGPT bei Codegenerierung, arXiv:2308.02828 (Abs. 5; S. 24): Primärquelle für die Reproduzierbarkeitsaussage, für Protokoll 4.10 nachzuschlagen.
- Pollin, Fischer, Sahle, Scholger & Vogeler 2025, „When it was 2024", ZfdG 10, DOI 10.17175/2025_008 (Abs. 16, 20; S. 24): Pipeline-Modell des IDE.
- Strutz & Scholger 2026, DHd 2026, Metadatenextraktion aus Briefen, Zenodo 10.5281/zenodo.18862770 (Abs. 20; S. 26).
- Galka & Vogeler 2026 (Abs. 20; S. 23): bereits zusammengefasst.
