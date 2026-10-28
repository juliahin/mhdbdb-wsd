# Pangakis, Wolken & Fasching 2023: Automated Annotation Requires Validation

**Datei:** `pdf/Pangakis-etal-2023-Automated-Annotation-Validation.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, Preprint vollständig gelesen; begutachtete Fassung (ICWSM 2025) gefunden, vollständig gelesen und abgeglichen.

**Seitenzählung:** Das lokale PDF ist arXiv v1. Die Titelseite (PDF-S. 1) trägt keine Nummer, ab PDF-S. 2 steht „1" unten. Zitiert wird die gedruckte Seite; PDF-Seite = gedruckte Seite + 1. Angaben „ICWSM S. …" beziehen sich auf die begutachtete Fassung (siehe unten), nicht auf das lokale PDF.

## Bibliografie

- **Vollständig (lokale Fassung):** Pangakis, Nicholas, Samuel Wolken & Neil Fasching, 2023. Automated Annotation with Generative AI Requires Validation. arXiv:2306.00176v1 [cs.CL], eingereicht 31. Mai 2023, Manuskript datiert 2. Juni 2023. 19 nummerierte Seiten plus Titelseite.
- **DOI/URL:** https://doi.org/10.48550/arXiv.2306.00176 (arXiv-Seite am 2026-10-28 abgerufen: nur v1, kein Journal-Ref, kein Rückzugsvermerk). ✔
- **Art:** Preprint (nicht begutachtet).
- **Sprache:** Englisch
- **Begutachtete Fassung (abweichender Titel, ohne Fasching):** Pangakis, Nick & Sam Wolken, 2025. Keeping Humans in the Loop: Human-Centered Automated Annotation with Generative AI. *Proceedings of the International AAAI Conference on Web and Social Media* 19(1), 1471 bis 1492. https://doi.org/10.1609/icwsm.v19i1.35883 (DOI löst auf ojs.aaai.org auf, Erscheinungsdatum 7. Juni 2025). ✔ Volltext am 2026-10-28 gelesen (abgerufene Kopie liegt nur im Sitzungsverzeichnis, nicht in `pdf/`). Die ICWSM-Seite nennt den Preprint nicht; dass es dieselbe Studie ist, folgt aus Inhalt, Aufgaben und Zahlen (27 Aufgaben, 11 Datensätze, GPT-4, Median-F1 0,707). Galka & Vogeler (2026, PDF-S. 3) zitieren diese Fassung.

## Worum es geht

Die Arbeit fragt, ob generative LLMs (hier GPT-4) menschliche Textannotation in den Sozialwissenschaften ersetzen oder ergänzen können, und argumentiert, dass jede LLM-Annotation aufgabenweise gegen menschliche Labels validiert werden muss (S. 2). Dazu schlagen die Autoren einen fünfstufigen Ablauf vor (Codebuch, Expert:innen-Labels, LLM-Test auf einer Teilmenge, Codebuch-Revision, Test auf zurückgehaltenen Items; Abb. 1, S. 4) und prüfen ihn, indem sie 27 Annotationsaufgaben aus 11 nicht öffentlichen Datensätzen aus jüngeren Artikeln in einflussreichen Zeitschriften nachstellen (S. 3, 6). Ergebnis: im Median gute Werte (Accuracy 0,850, F1 0,707), aber starke Streuung zwischen Aufgaben und sogar innerhalb eines Datensatzes; bei 9 von 27 Aufgaben lag Precision oder Recall unter 0,5 (S. 3, 7). Zusätzlich führen sie einen „Konsistenzwert" aus wiederholter Klassifikation ein, der mit der Richtigkeit korreliert (S. 9).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| LLM-Annotation muss immer gegen eine Teilmenge hochwertiger menschlicher Labels validiert werden, aufgabenweise, auch wenn die Technik besser wird. | S. 2, Abschnitt 1 | eigene These |
| „Hochwertig" heißt: Labels von Fachexpert:innen, nicht von studentischen Hilfskräften oder Crowdworkern. | S. 2, Fn. 2 | eigene Festlegung |
| Frühere Studien testen auf öffentlichen Benchmarks und sind daher vermutlich von Kontamination betroffen; gute Werte können Memorierung sein. | S. 2, Abschnitt 1 | Argument, gestützt auf Brown et al. 2020 (referiert) |
| Empfohlen: mindestens zwei Fachexpert:innen und das LLM annotieren dieselben Items mit demselben Codebuch; das Codebuch ist zugleich der Prompt. | S. 5, Abschnitt 2 | Empfehlung |
| Stichprobe für die Validierung: 250 bis 1.250 zufällige Items; bei sehr seltenen Klassen (unter 1 % positiv) deutlich mehr. | S. 5, Fn. 7 | Empfehlung „based on our analyses", die Analyse wird nicht gezeigt |
| Unterschiedliche Codebücher für Mensch und LLM erzeugen eine konzeptuelle Lücke. | S. 5, Fn. 8 | Argument |
| Nach einer Codebuch-Revision auf denselben Items zu messen ist Überanpassung; entscheidend ist die Leistung auf zurückgehaltenen Items. Bei grundlegenden Änderungen sollten auch die Menschen neu annotieren. | S. 5, Fn. 9 und Text | Empfehlung |
| Median-Accuracy 0,850, Median-F1 0,707 über 27 Aufgaben; F1 reicht von 0,059 bis 0,969. | S. 3; S. 7, Tab. 1 | eigenes Ergebnis |
| 9 von 27 Aufgaben mit Precision oder Recall unter 0,5, 3 mit beidem; Recall ist bei 20 von 27 Aufgaben höher als Precision; 8 von 27 erreichen bei beiden über 0,7. | S. 7 | eigenes Ergebnis |
| Innerhalb eines Datensatzes (Card et al. 2022) reicht F1 von 0,259 bis 0,811. | S. 9 | eigenes Ergebnis |
| Konsistenzwert: Items mit Konsistenz 1,0 haben 19,4 Prozentpunkte höhere Accuracy, 16,4 höhere TPR, 21,4 höhere TNR; 85,1 % aller Items haben Konsistenz 1,0. Empfohlen: mindestens drei Läufe mit Temperatur über 0. | S. 9, Abschnitt 3.1; Abb. 3, S. 10 | eigenes Ergebnis |
| Mehrfache Klassifikation bei Temperatur 0,6 lieferte bessere Ergebnisse als eine einzelne bei Temperatur 0; die Wahl 0,6 ist willkürlich. | S. 9, Fn. 14 | eigenes Ergebnis, ohne Zahlen |
| Eine Runde Codebuch-Revision verbesserte Accuracy und F1 meist nur leicht; Prompt-Feinheiten scheinen kein wesentlicher Hebel zu sein. | S. 11, Abschnitt 3.2; Abb. 4, S. 12 | eigenes Ergebnis |
| Vier Einsatzarten: Qualität menschlicher Labels prüfen, Fälle für menschliche Prüfung priorisieren, Trainingsdaten erzeugen, ganzes Korpus klassifizieren. Bei geringer Übereinstimmung mit vorhandenen Labels haben Menschen, LLM oder beide Fehler gemacht. | S. 12 bis 13, Tab. 2 | Vorschlag |
| Ob eine Aufgabe eine Faktenfrage ist oder ein Urteil verlangt, ist für die Klassifikationsstrategie wesentlich. | S. 14, Abschnitt 5 | referiert (Balagopalan et al. 2023) |

## Daten, Methode, Zahlen

- **Aufgaben:** 27 Aufgaben aus 11 Datensätzen (Tab. A1, S. 17; Tab. A2, S. 19), u. a. Kalter-Krieg-Texte politisch oder militärisch, Einwanderungsreden mit Tonalität, Hassrede und Angstrede auf Gab, zeitliche Ausrichtung von Parteiprogrammsätzen. Jede Dimension wird als eigene binäre Aufgabe behandelt; eine Dreiklassenaufgabe wird zu drei binären (S. 6, Fn. 11).
- **Gold:** die menschlichen Labels der Originalstudien, ohne eigene Prüfung (S. 6). Datensätze nur aus passwortgeschützten Archiven oder direkt von den Autor:innen, gegen Kontamination (S. 6). Eine Übereinstimmung zwischen den ursprünglichen Annotator:innen wird im Preprint nicht berichtet.
- **Modell:** GPT-4 über die OpenAI-API, gut 200.000 klassifizierte Items, ca. 420 USD; ein Datensatz mit 1.000 Items brauchte für sieben Durchläufe ca. 2 bis 3 Stunden (S. 6 bis 7).
- **Maße:** Accuracy, Precision, Recall, F1 gegen die menschlichen Labels, auf zurückgehaltenen Items (S. 7). Tab. 1 (S. 7, am PDF geprüft): Accuracy Min. 0,674 / Median 0,85 / Max. 0,981; Precision 0,033 / 0,650 / 0,957; Recall 0,25 / 0,829 / 0,982; F1 0,059 / 0,707 / 0,969 (Mittelwerte 0,855, 0,615, 0,749, 0,660).
- **Konsistenz:** Temperatur 0,6, mindestens sieben Läufe pro Item mit demselben Codebuch; Konsistenz = Anteil der Läufe, die mit dem Modalwert übereinstimmen (S. 9).
- **Codebuch-Revision:** höchstens eine Runde pro Aufgabe (S. 11).

## Begutachtete Fassung: was sich gegenüber dem Preprint ändert

Gelesen am 2026-10-28 (ICWSM 2025, S. 1471 bis 1492). Für Zitate in der Dissertation ist diese Fassung maßgeblich; der Preprint enthält Angaben, die dort anders stehen.

- **Ablauf:** vier statt fünf Schritte (ICWSM S. 1471, Abb. 1). Prompt-Optimierung auf 250 zufälligen, menschlich annotierten Items, Endbewertung auf 1.000 zurückgehaltenen Items pro Aufgabe (ICWSM S. 1473 bis 1474). Die Empfehlung „250 bis 1.250" und „mindestens zwei Fachexpert:innen" aus dem Preprint (S. 5) steht in dieser Form nicht mehr.
- **Umfang:** gut 75.000 Items statt gut 200.000, unter 500 USD, ca. 1 Stunde pro 1.000 Items (ICWSM S. 1474).
- **Herkunft der menschlichen Labels:** 22,2 % der Aufgaben von Crowdworkern, 37 % von Expert:innen, 40,8 % von Hilfskräften (ICWSM S. 1473). Die Originallabels gelten als Gold, weil sie das Peer Review der Originalstudien durchlaufen haben (ICWSM S. 1472, Fn. 2).
- **Konsistenz:** mindestens fünf Läufe bei Temperatur 0,7 (ICWSM S. 1475) statt sieben bei 0,6; die berichteten Unterschiede (19,4 / 16,4 / 21,4 Prozentpunkte, ca. 85 % mit Konsistenz 1,0) sind trotzdem dieselben wie im Preprint. Die „Intercoder-Übereinstimmung" des LLM mit sich selbst wird ausdrücklich nicht als Gütemaß verwendet, nur als Konfidenz (ICWSM S. 1474, Fn. 12).
- **Neu:** Schlecht schnitten Aufgaben ab, die nuanciertes kulturelles Wissen oder Schlüsse aus dem Gesprächskontext verlangen; zusammenfassungsähnliche Aufgaben gut (ICWSM S. 1475, 1477). Prompt-Revision: Median-Verbesserung Accuracy 0,024, Precision 0,043, F1 0,018, Recall-Median 0 (ICWSM S. 1476, Abb. 3). Temperatur ohne klaren Effekt (7 Aufgaben; ICWSM S. 1475 bis 1477). Kein Leistungsverlust zwischen April und November 2023 (14 Aufgaben; ICWSM S. 1476). Ein mit 250 Items feinjustiertes BERT unterliegt GPT-4 in 18 von 27 Aufgaben, mit 1.000 Items übertrifft BERT GPT-4 in 10 von 14 (ICWSM S. 1477, Abb. A4). Mistral-7B im Mittel 0,16 F1 schlechter als GPT-4 (ICWSM S. 1486).
- **Neu und für das Protokoll wichtig:** Für 21 der 27 Aufgaben berichteten die Originalstudien eine Intercoder-Reliabilität (16-mal Krippendorffs α, 5-mal Cohens κ). Bei niedriger menschlicher Reliabilität ist auch GPT-4 schwach; hohe Reliabilität sagt gute LLM-Leistung nur schwach voraus (ICWSM S. 1486 bis 1487, Anhang E, Abb. A3). In der Diskussion fordern die Autoren, menschliche Labels zuerst über Intercoder-Maße zu validieren (Artstein & Poesio 2008), und nennen als offene Frage, wie man validiert, wenn menschliche Validierung schwierig ist (ICWSM S. 1477). Als Limitation: korrelierte Fehler der menschlichen Annotator:innen drücken die gemessene LLM-Leistung (ICWSM S. 1478).

## Wörtliche Stellen

> „we argue that any automated annotation process using an LLM must validate the LLM's performance against labels generated by humans" (Abstract, PDF-S. 1)

> „both the human coders and the LLM should use the same codebook for annotation, where the codebook serves as the LLM's prompt instructions" (S. 5)

> „This exercise is overfitting to a particular subset of data and thus should not be taken as the barometer of performance." (S. 5, Fn. 9)

> „Grounding automated annotation in validation labels generated by humans is essential for responsible evaluation." (ICWSM S. 1471, Abstract)

> „underscores the necessity of first validating human labels through inter-coder agreement metrics" (ICWSM S. 1477)

## Bezug zur Dissertation

- **Protokoll 9.2 (LLM gegen menschliche Annotator:innen, menschliche IAA als Obergrenze):** gestützt durch ICWSM Anhang E (S. 1486 bis 1487): Wo Menschen untereinander schwach übereinstimmen, ist auch das LLM schwach. Das spricht dafür, LLM-Werte nach Agreement-Schichten (Protokoll 9.1, Punkt 6) aufzuschlüsseln.
- **Protokoll 4.10 (Freeze 2: Prompt, Temperatur, Läufe pro Item, gleiche Karten für Mensch und LLM):** Der Grundsatz „gleiches Codebuch für Mensch und LLM" (S. 5, Fn. 8) stützt die offene Frage in 4.10 zugunsten gleicher Karten. Der Konsistenzwert (S. 9; ICWSM S. 1475) ist ein Kandidat für die Festlegung „Anzahl der Läufe pro Item": mehrere Läufe bei Temperatur über 0, Konsistenz als Kovariate oder als Markierung unsicherer Items, nicht als Gütemaß (ICWSM S. 1474, Fn. 12).
- **Protokoll 7 (Pilot, Revision, Einfrieren, frische Items):** gestützt. Prompt-Revision nur auf Pilot-Items, Bewertung nur auf zurückgehaltenen Items (S. 5, Fn. 9; ICWSM S. 1474, Fn. 8). Das Protokoll trennt Pilot- und Hauptlemmata bereits; der Befund, dass Prompt-Revision wenig bringt (S. 11; ICWSM S. 1476), spricht gegen viele Prompt-Iterationen.
- **Protokoll 10 (Labels privat, Kontamination):** gestützt. Die Studie wählt passwortgeschützte Daten genau deshalb, und die ICWSM-Fassung argumentiert, dass öffentlicher Rohtext unkritisch ist, solange die Labels nicht öffentlich sind (ICWSM S. 1486, Anhang B). Das entspricht der Begründung in Protokoll 10 („zu schützen sind die Labels").
- **Nebenfrage Silberqualität (Protokoll 1, 9.2):** Einsatzart 1 (S. 13, Tab. 2) schlägt vor, vorhandene menschliche Labels mit dem LLM zu prüfen. Für die Dissertation nur als Ergänzung brauchbar: Das Protokoll misst Silber gegen das neue Gold, nicht gegen das LLM, und die Arbeit selbst sagt, dass bei Abweichung offen bleibt, wer irrt.
- **Stichprobengröße (Protokoll 4.7):** Die Zahlen (250 bis 1.250 im Preprint, 250 plus 1.000 pro Aufgabe in ICWSM) gelten pro binärer Aufgabe mit festem Kategoriensystem. Bei WSD ändert sich das Inventar mit jedem Lemma; ein Item ist eine eigene kleine Aufgabe. Die Zahlen sind daher kein Maßstab für die ca. 510 Items, nur ein Hinweis, dass die Validierungsmenge mehrere hundert Items umfasst.

## Grenzen und Einwände

- Nur Englisch, nur Sozialwissenschaften, nur binäre Aufgaben (S. 6, Fn. 11); keine lexikalische Semantik, keine historische Sprache.
- Das Gold sind fremde Labels ohne eigene Prüfung; der Preprint berichtet ihre Reliabilität nicht. Die eigene Empfehlung „mindestens zwei Fachexpert:innen" (S. 5) wird in der Studie selbst nicht umgesetzt; in ICWSM stammen 63 % der Aufgaben von Crowd oder Hilfskräften (ICWSM S. 1473).
- Die Stichprobenempfehlung (S. 5, Fn. 7) ist nicht hergeleitet.
- Fehlverweis im Preprint: „As shown in Table 2, the aggregate performance ranged as low as an F1 score of 0.06" (S. 7 bis 9); der Wert steht in Tab. 1 (0,059), Tab. 2 ist die Einsatzarten-Tabelle.
- Zwischen Preprint und ICWSM ändern sich Temperatur und Zahl der Läufe für den Konsistenzwert, die berichteten Prozentpunkte bleiben gleich. Welche Einstellung den Zahlen zugrunde liegt, ist aus den beiden Texten nicht zu klären.
- Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar: Das Kontaminationsargument greift nur halb, denn die MHDBDB-Texte und teils auch Silber-Annotationen sind öffentlich; Pangakis' Lösung (nur nicht öffentliche Labels) entspricht dem Protokoll nur für das neue Gold.

## Weiterführend

- Pangakis & Wolken 2025 (ICWSM), die begutachtete Fassung: für alle Zitate bevorzugen.
- Gilardi, Alizadeh & Kubli 2023, ChatGPT gegen Crowdworker (S. 1; ICWSM S. 1472, dort als PNAS 120(30) zitiert).
- Reiss 2023, Zuverlässigkeit von ChatGPT bei Textannotation (S. 1; ICWSM S. 1472).
- Balagopalan et al. 2023, Fakten- gegen Normurteile beim Labeln (S. 14).
- Ziems et al. 2023 und Zhu et al. 2023, breitere LLM-Annotationsstudien auf öffentlichen Benchmarks (S. 2).
- Li & Flanigan 2023, Task-Kontamination (ICWSM S. 1473).
- Li et al. 2023, CoAnnotating, wird in ICWSM S. 1475 als Vorbild für Mensch-Maschine-Zusammenarbeit zitiert (siehe eigene Zusammenfassung).
