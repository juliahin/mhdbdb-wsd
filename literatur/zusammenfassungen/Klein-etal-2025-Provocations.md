# Klein et al. 2025: Provocations from the Humanities for Generative AI Research

**Datei:** `pdf/Klein-etal-2025-Provocations.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, lokales PDF (arXiv v1) vollständig gelesen; Versionen auf arXiv geprüft, v2 nur in Ausschnitten über die HTML-Fassung gesichtet; keine begutachtete Fassung gefunden.

**Seitenzählung:** Das lokale PDF ist arXiv v1 im ACM-Satz. Die Kopfzeilen tragen „111:n“ (Platzhalter der ACM-Vorlage, kein Band); n entspricht der PDF-Seite, S. 1 hat keine Kopfzeile. Zitiert wird „S. n“. Jede Seite trägt den Fußvermerk `Preprint — please check authors’ websites for updated versions.`

## Bibliografie

- **Vollständig (lokale Fassung):** Klein, Lauren, Meredith Martin, Andre Brock, Maria Antoniak, Melanie Walsh, Jessica Marie Johnson, Lauren Tilton & David Mimno, 2025. Provocations from the Humanities for Generative AI Research. arXiv:2502.19190v1 [cs.CY], 26. Februar 2025. 21 Seiten.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2502.19190 (arXiv-Seite am 2026-10-28 gelesen). ✔
- **Versionen:** v1 vom 26. Februar 2025 (lokales PDF), v2 vom 12. Januar 2026 mit dem Kommentar „revised draft; final version in preparation“; kein Journal-Ref, kein Rückzugsvermerk. ✔
- **Begutachtet?** Nicht nachgewiesen. Die v2 ist im ACM-Konferenzsatz mit der Zeile „Ninth Annual ACM Conference on Fairness, Accountability, and Transparency; Montreal, CA“ (FAccT 2026) und einem DOI-Platzhalter „XXXXXXX.XXXXXXX“ gesetzt (HTML-Fassung am 2026-10-28 gesichtet). Eine Proceedings-Fassung mit ACM-DOI wurde nicht gefunden; die Seite der angenommenen FAccT-2026-Beiträge lud ihre Liste nicht. Ein Blogeintrag vom 14. Januar 2026 spricht nur von einem überarbeiteten Preprint „in preparation for conference season“, ohne Venue. ○ Stand also: Preprint; ob die Arbeit bei FAccT 2026 erschienen ist, bleibt offen.
- **Art:** Preprint (Positionspapier, nicht empirisch).
- **Sprache:** Englisch
- **Unterschiede v1 zu v2 (nur gesichtet, nicht gelesen) ○:** In v2 hat Tab. 1 zu jeder Provokation ein Stichwort und einen Vorschlag für nächste Schritte; neu ist ein Anhang mit Erklärungen (u. a. zur Nutzung generativer KI, Positionalität, Ethik); das Beispiel *Distant Viewing* (Arnold und Tilton) steht nicht mehr in Abschnitt 4.3; Lizenz CC BY-NC-SA 4.0. Wer zitiert, sollte v2 oder eine spätere Endfassung lesen.

## Worum es geht

Acht Geisteswissenschaftler:innen und Informatiker:innen formulieren nach dem Muster von boyd & Crawfords „Critical Questions for Big Data“ (2012) acht „Provokationen“ an die Forschung zu generativer KI (S. 2, S. 5). Sie bestimmen zuerst, was geisteswissenschaftliche Forschung ist (Interpretation, Kontextualisierung, Theoriebildung aus konkreten Kulturobjekten, S. 3) und wie wenig sie bisher etwa bei FAccT vorkommt (S. 4 bis 5). Die Provokationen betreffen Bedeutung, Kultur, Repräsentativität, Modellgröße, Trainingsdaten, Offenheit, Rechenmacht und KI-Universalismus (S. 5, Tab. 1; Abschnitte 4.1 bis 4.8). Der Schluss warnt vor der „Extraktion“ geisteswissenschaftlicher Expertise durch die Informatik und fordert, Geisteswissenschaftler:innen als gleichberechtigte, finanzierte Partner:innen einzubinden (S. 13 bis 15).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Die acht Provokationen (Tab. 1): 1. Models make words, but people make meaning; 2. AI requires an understanding of culture; 3. AI can never be „representative“; 4. Bigger models are not always better models; 5. Not all training data is equivalent; 6. Openness is not an easy fix; 7. Limited access to compute enables corporate capture; 8. AI universalism creates narrow human subjects. | S. 5, Tab. 1 | eigene Thesen |
| (1) Bedeutung entsteht beim Lesen, nicht im Modell; flüssige, aber falsche Ausgaben („Halluzinationen“) wirken durch menschliche Deutungserwartung wie Wissen. Beispiel: Eine KI-Übersetzungsplattform bot kaum Begriffe in Twi und Wolof, und die vorgeschlagenen wichen vom Sinn des französischen Originals ab. | S. 6, Abschnitt 4.1 | Argument, gestützt auf Barthes, Derrida; Beispiel referiert (Translation Lab) |
| (2) „Kultur“ wird in der KI-Forschung eng als Region, Nation, Sprache oder Identität gefasst; die Geisteswissenschaften meinen auch die Werke und Praktiken einer Gruppe. Trainingsdaten und Modelle sind selbst Kulturobjekte. Genannt werden auch Modelle, die auf historische Sprachen abgestimmt sind. | S. 6 bis 7, Abschnitt 4.2 | Argument; Beispiel referiert (Yamshchikov et al. 2022) |
| (3) Lücken und Verzerrungen historischer Quellen („silences“, „absences“) lassen sich nicht „wegmodellieren“. Vorgeschlagen: fehlende Daten markieren statt übergehen, dünne Daten bewusst gewichten. | S. 8, Abschnitt 4.3 | Argument, referiert (Trouillot, Hartman, Bode, Sherman et al.) |
| (3) Jeder Akt der Datensatzbildung ist politisch; schon die Vergabe einer Annotation enthält politische, soziale und kulturelle Entscheidungen. Statt einen „repräsentativen“ Datensatz anzustreben, sollen die eingebauten Perspektiven dokumentiert und benannt werden. | S. 8, Abschnitt 4.3 | eigene These, Beispiel referiert (Arnold & Tilton, *Distant Viewing*) |
| (4) Mehr Daten, Parameter und Rechenleistung bringen nicht mehr unbedingt genauere Ausgaben. Kleinere, kuratierte, aufgabenspezifische Modelle; Fachexpert:innen nicht nur als Prompt-Ingenieur:innen, sondern als Mitentwickler:innen. Beispiel: ein LLM, das nur auf englischen Texten des 19. Jahrhunderts trainiert wird, für kontrafaktische Experimente. | S. 8 bis 9, Abschnitt 4.4 | Argument, referiert (McKenzie et al. 2024; Zhou et al. 2024); Beispiel ohne Beleg |
| (5) Trainingsdaten werden als homogener Rohstoff behandelt; ihre Inhalte sind selten offengelegt („documentation debt“). Datasheets sind nötig, aber geisteswissenschaftliche Formen wie Datenarchäologien, Datennarrative und „data essays“ gehen weiter. | S. 9 bis 10, Abschnitt 4.5 | Argument, referiert (Bandy & Vincent 2021; Gebru et al. 2021) |
| (6) „Offene“ Modelle legen Daten und Training oft nicht offen und brauchen weiter große Rechenleistung; Offenheit, Eigentum und Zugang haben keine Ja-Nein-Antworten. | S. 10 bis 11, Abschnitt 4.6 | Argument |
| (7) Die Leistungssteigerung beruht auf Ressourcenkonzentration; Universitäten und einzelne Forschende können kaum mithalten. | S. 11 bis 12, Abschnitt 4.7 | Argument, referiert (Whittaker 2021) |
| (8) KI deutet Kultur als „content“ um und beansprucht universelles Wissen. | S. 12 bis 13, Abschnitt 4.8 | Argument, referiert (Koopman, Mills, Amaro) |
| Geisteswissenschaftler:innen sollen von Projektbeginn an als gleichberechtigte, gleich finanzierte Partner:innen und Koautor:innen beteiligt werden, nicht nachträglich um Feedback gebeten. | S. 14, Abschnitt 5 | Forderung |

## Daten, Methode, Zahlen

- **Methode:** Positionspapier; die Provokationen werden mit geisteswissenschaftlicher Literatur begründet, nicht mit eigenen Daten (S. 2 bis 3).
- **Einzige Zahl:** Eine Rückschau auf FAccT ordnete 11 % der Beiträge der Philosophie zu; Philosophie war die einzige eigens ausgewiesene geisteswissenschaftliche Disziplin (S. 4, referiert: Laufer et al. 2022).
- **Unstimmigkeiten in v1:** Die erste Provokation heißt im Abstract „Models make words, but people make meaning“ (S. 1), in der Einleitung „Language makes meaning in multiple ways“ (S. 2), in Tab. 1 wieder wie im Abstract (S. 5); die zweite heißt im Abstract und auf S. 2 „Generative AI requires an expanded definition of culture“, in Tab. 1 und Abschnitt 4.2 „AI requires an understanding of culture“. Im Text werden Arnold und Tilton für *Distant Viewing* genannt (S. 8), die Literaturliste nennt nur Arnold ([14], S. 16). Ein Platzhalter „(Amaro )(cite)“ steht auf S. 13, die Einträge [22] und [23] sind doppelt, [1] und [2] leer. Das bestätigt den Entwurfsstatus von v1.

## Wörtliche Stellen

> „any act of dataset creation is a political act“ (S. 8)

> „there is always a perspective that is shaped by training data, annotations, parameters, and prompts“ (S. 8)

> „what new methods might be required in order to mark missing data, or intentionally amplify the significance of sparse data, rather than merely pass over these silences or gaps?“ (S. 8)

> „Models make words, but people make meaning“ (S. 5, Tab. 1; S. 6, Abschnitt 4.1)

## Julias Markierungen im PDF

Keine Markierungsdatei vorhanden (`md/Klein-etal-2025-Provocations.markierungen.md` fehlt).

## Bezug zur Dissertation

Die Arbeit sagt nichts über LLM-Annotation, WSD oder Evaluationsmaße. Für die Dissertation relevant sind vier Provokationen, als Rahmung und als möglicher Einwand von Gutachter:innen aus den Geisteswissenschaften.

- **Provokation 1 (S. 6) und Protokoll 5 und 9.2:** Wenn Bedeutung von Menschen gemacht wird, ist ein menschlich adjudiziertes Gold die richtige Referenz und keine LLM-Ausgabe. Das stützt die Entscheidung, keine LLM-generierten Definitionen auf die Karten zu setzen (Protokoll 5) und das LLM an der menschlichen IAA zu messen (Protokoll 9.2).
- **Provokation 3 (S. 8) und Protokoll 2, 6, 7 Schritt 6 und 7, `DMP.md` 2:** „Jede Annotation ist eine Entscheidung mit Perspektive“ ist die geisteswissenschaftliche Fassung dessen, was das Protokoll technisch umsetzt: Silber gilt nicht als Gold, weil Herkunft und Richtlinien undokumentiert sind (Protokoll 2); Labels vor der Adjudikation, Ursachencodes und Richtlinienversionen bleiben erhalten (Protokoll 7); Datasheet und Data Statement (DMP 2). Die Frage nach Methoden, fehlende Daten zu markieren statt zu übergehen (S. 8), passt zu `KEINE_PASST` mit angekreuzten Begriffen als Befund über Lücken im Begriffssystem (Protokoll 6, 9.2) und zum Gattungsausgleich gegen den Überlieferungsbias (Protokoll 4.4, A7). Das ist eine Lesart der Dissertation, nicht eine Aussage der Autor:innen.
- **Provokation 4 (S. 8 bis 9):** Möglicher Einwand gegen das Design: Warum ein großes allgemeines LLM statt eines kleinen, auf historische Sprache abgestimmten Modells, und warum Fachleute nur als Annotator:innen und nicht als Mitentwickler:innen? Die Dissertation kann antworten, dass sie Disambiguierung mit einem allgemeinen Modell gegen eine starke Baseline prüft, nicht ein Modell entwickelt; sie sollte den Einwand aber benennen.
- **Provokationen 5 bis 7 (S. 9 bis 12) und `PROMPT-LOG.md`, `DMP.md` 4:** Ein proprietäres Modell mit unbekannten Trainingsdaten lässt offen, ob mittelhochdeutsche Texte und die öffentliche MHDBDB-Annotation darin vorkommen (Protokoll 10). Das deckt sich mit Semmelrock et al. 2025 (S. 10, Offenheits-Tracker) und spricht dafür, im Prompt-Log Modell und Anbieter genau festzuhalten und die Wahl eines geschlossenen Modells im Artikel zu begründen.

## Grenzen und Einwände

- Positionspapier ohne Daten; die Provokationen sind Thesen, keine Befunde. Für die Computerlinguistik als Zielvenue taugt die Arbeit nur zur Rahmung, nicht als Beleg.
- Die Beispiele kommen überwiegend aus US-amerikanischer Kultur- und Geschichtswissenschaft (Archiv der Sklaverei, Black Studies); historische Sprachen kommen nur in einem Halbsatz vor (S. 7).
- Lokale Fassung v1 ist ein Entwurf mit Unstimmigkeiten (siehe oben); v2 ist überarbeitet, eine Endfassung ist angekündigt. Zitate vor der Verwendung an der dann gültigen Fassung prüfen.

## Weiterführend

- boyd & Crawford 2012, „Critical Questions for Big Data“ (S. 2, S. 5; Literatur [29], S. 16).
- Bode 2020, „Why You Can't Model Away Bias“, *Modern Language Quarterly* 81(1) (S. 8; Literatur [27], S. 16).
- Gebru et al. 2021, Datasheets for Datasets (S. 7, S. 9; Literatur [59], S. 18), schon im DMP genannt.
- Bandy & Vincent 2021, „Documentation Debt“ (S. 9; Literatur [16], S. 16).
- Yamshchikov et al. 2022, „BERT in Plutarch's Shadows“, EMNLP 2022 (S. 7; Literatur [136], S. 21): Sprachmodell für eine historische Sprache.
- Chang et al. 2023, „Speak, Memory“, und D'Souza & Mimno, „The Chatbot and the Canon“ (S. 7; Literatur [37], S. 17, und [50], S. 17): Was LLMs an Büchern und Gedichten gespeichert haben; einschlägig für Kontamination (Protokoll 10).
