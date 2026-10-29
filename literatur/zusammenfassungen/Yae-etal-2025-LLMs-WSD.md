# Yae et al. 2025: Leveraging Large Language Models for Word Sense Disambiguation

**Datei:** `pdf/Yae-etal-2025-LLMs-WSD.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, Volltext (18 Seiten), Tabellen und die als Bild gesetzten Prompts (Abb. 1 bis 3) an Textebene und Seitenbild gelesen; Bibliografie, Lizenz und Korrekturnotiz über Crossref geprüft. Im PDF keine Markierungen von Julia.

**Seitenzählung:** Das lokale PDF trägt keine Heftseitenzahlen (Kopfzeile nur „Neural Computing and Applications“). Laut Crossref steht der Artikel in Band 37, Heft 6, S. 4093 bis 4110; das sind 18 Seiten wie im PDF. Zitiert wird „PDF-S. n (S. 4092 + n)“; die Heftseiten sind daraus abgeleitet und nicht an einer Heftfassung geprüft.

## Bibliografie

- **Vollständig:** Yae, Jung H., Nolan C. Skelly, Neil C. Ranly & Phillip M. LaCasse, 2025. Leveraging large language models for word sense disambiguation. *Neural Computing and Applications* 37(6), 4093 bis 4110.
- **DOI/URL:** https://doi.org/10.1007/s00521-024-10747-5 (löst auf link.springer.com auf; Metadaten am 2026-10-28 über die Crossref-API gelesen). ✔ Eingegangen 3. Juni 2024, angenommen 22. Oktober 2024 (PDF-S. 1); online 19. Dezember 2024, Heft Februar 2025 (Crossref). Yae und Skelly sind gleichberechtigte Erstautoren (PDF-S. 1).
- **Lizenz:** CC BY-NC-ND 4.0, ✔ am PDF bestätigt (Open-Access-Vermerk PDF-S. 16) und laut Crossref. Das PDF nennt „© The Author(s) 2024, corrected publication 2025“ (PDF-S. 1). Die Korrektur (DOI 10.1007/s00521-025-11082-z, *Neural Computing and Applications* 37, 7449 bis 7450, 22. Februar 2025, am 2026-10-28 als PDF gelesen) betrifft nur Urheberrechtsvermerk und Lizenz: Der Artikel erschien zuerst unter exklusiver Lizenz und wurde nachträglich Open Access. Die Notiz widerspricht sich selbst (Fließtext „Creative Commons Attribution 4.0“, Link und Lizenzblock CC BY-NC-ND 4.0); maßgeblich ist der Vermerk im Artikel.
- **Art:** begutachteter Zeitschriftenartikel („Original Article“)
- **Sprache:** Englisch
- **Code und Daten:** Das PDF gibt `https://github/neil-r/study_wsd` an (PDF-S. 16, Host-Name verstümmelt); unter github.com/neil-r/study_wsd ist am 2026-10-28 ein Repositorium erreichbar, nicht geöffnet.

## Worum es geht

Die Arbeit prüft sieben generative LLMs (drei LLaMa-2-Größen, Vicuña-7B, PaLM-2, GPT-3.5, GPT-4) zero-shot auf englischer WSD mit drei selbst entworfenen Aufgabenformaten (PDF-S. 3, 5 bis 8): (1) Auswahl des richtigen Sense aus einer Liste aller BabelNet-Senses des Lemmas, (2) Wahr/Falsch-Urteil über einen einzelnen vorgegebenen Sense, (3) wie (1), aber das Zielwort durch ein erfundenes Kunstwort ersetzt. Daten sind die Standardkorpora SemCor, SemEval und Senseval, die Optionen werden über Lemma und Wortart aus BabelNet geholt (PDF-S. 5 bis 6). Bestes Modell ist durchweg GPT-4 mit 70,37 % (Aufgabe 1), 77,22 % (Aufgabe 2) und 56,11 % (Aufgabe 3) (PDF-S. 8 bis 9). Daneben versuchen die Autoren, die Parameterzahl geschlossener Modelle aus der Genauigkeit zu schätzen (ohne brauchbares Ergebnis) und Mehrheits-Ensembles zu bilden (kein nennenswerter Gewinn gegenüber GPT-4) (PDF-S. 10 bis 12).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Aufgabe 1 (Auswahl aus allen Senses): GPT-4 70,37 %, PaLM-2 65,98 %, GPT-3.5 und LLaMa-2-70B je 61,22 %, Vicuña 50,61 %, LLaMa-2-13B 50,49 %, LLaMa-2-7B 42,56 %. | PDF-S. 8, Tab. 7 | eigenes Ergebnis (aber siehe Grenzen: Zuordnung PaLM-2/GPT-3.5 im Artikel widersprüchlich) |
| Innerhalb der LLaMa-Familie steigt die Genauigkeit mit der Parameterzahl. | PDF-S. 8, Abschnitt 4.1 | eigenes Ergebnis |
| Aufgabe 2 (Wahr/Falsch über einen zufällig gewählten Sense) fällt allen größeren Modellen leichter als Aufgabe 1: GPT-4 77,22 %, PaLM-2 75,18 %; Vicuña antwortet immer „True“ (Recall 100 %), LLaMa-2-7B fast immer (Recall 99,28 %). | PDF-S. 9, Tab. 8 | eigenes Ergebnis |
| Aufgabe 3 (Kunstwort statt Zielwort) ist für alle Modelle am schwersten (GPT-4 56,11 %); der Zusammenhang mit der Modellgröße bricht hier ab. | PDF-S. 9, Abschnitt 4.3, Tab. 9 | eigenes Ergebnis |
| Für Aufgabe 3 musste der Prompt Wortart und eine ausdrückliche Auswahlanweisung enthalten, weil die Modelle das Kunstwort sonst als Tippfehler eines echten Wortes lasen; in Aufgabe 1 war das nicht nötig. | PDF-S. 8, Abschnitt 3.4.3 | eigene Beobachtung („trial and error“) |
| Aus der Genauigkeit lässt sich die Parameterzahl geschlossener Modelle nicht verlässlich schätzen; die Schätzungen schwanken für GPT-4 zwischen ca. 83 und 2.448 Mrd. | PDF-S. 10 bis 11, Tab. 10 und 11 | eigenes Ergebnis |
| Ensembles (Mehrheit, Gewichtung des besten Modells, Gewichtung ohne die zwei schwächsten) sind nicht nennenswert besser als GPT-4 allein; die Gewichtung des besten Modells schlägt die einfache Mehrheit. | PDF-S. 12, Tab. 15 und 16 (Tab. 16 auf PDF-S. 13) | eigenes Ergebnis |
| In Aufgabe 2 liegt mindestens ein Modell bei 92,46 % der 834 Items richtig, aber bei 43 Items nur genau eines; das ist im Einsatz nicht erkennbar. | PDF-S. 12, Tab. 13 | eigenes Ergebnis |
| GPT-4 (`gpt-4-0613`, Aufgabe 1) disambiguiert Wörter für physische Entitäten besser als Wörter für Abstrakta oder Handlungsverben (Baumkarte über die WordNet-Hierarchie). | PDF-S. 14, Abschnitt 5.2, Abb. 8 | eigenes Ergebnis (nur grafisch, ohne Zahlen) |
| Fehleranalyse nach Gold-Sense: Für den häufigen Sense von *act* (24 Items) liegen die Modelle zwischen 25 % und 58,3 %, für *use* (25 Items) zwischen 20 % und 100 %. | PDF-S. 15, Tab. 17 | eigenes Ergebnis |
| Generative LLMs erreichen den Stand der Technik der WSD noch nicht. | PDF-S. 15, Abschnitt 6.1 | Wertung, gestützt auf Bevilacqua et al. 2021 (referiert, ohne Zahlenvergleich) |
| Kocoń et al. 2023 fanden ChatGPT bei WSD „acceptable“, aber unter dem Stand der Technik; sie gaben einen ganzen Absatz als Kontext, Yae et al. nur einen Satz. | PDF-S. 5, Abschnitt 2.3 | referiert |

## Daten, Methode, Zahlen

- **Korpora:** SemCor, SemEval-2010, -2013, -2015, Senseval-2 und -3 (PDF-S. 5); Gold-Senses aus WordNet oder BabelNet (PDF-S. 6). Wie aus diesen Korpora die Items gezogen wurden, sagt der Artikel nicht.
- **Umfang:** 820 Items (Aufgabe 1), 834 (Aufgabe 2), 786 (Aufgabe 3) (PDF-S. 7, Tab. 6). Keine Aufschlüsselung nach Korpus, Wortart oder Zahl der Senses.
- **Inventar im Prompt:** Die Korpora enthalten nur den richtigen Sense; die übrigen Optionen holt ein Skript aus BabelNet über Lemma und Wortart (PDF-S. 7, Abschnitt 3.4). Gezeigt werden die **Glossen** als Text, mit Buchstaben A), B), … nummeriert; im Beispiel *document* vier Optionen (PDF-S. 7, Abb. 1). Keine Sense-IDs, keine Beispiele.
- **Prompt Aufgabe 1** (PDF-S. 7, Abb. 1, am Seitenbild gelesen): Frage „What is the meaning of the word "document" in the following sentence?“, dann der Satz, dann „Options:“ mit A) bis D). In Abb. 3 (PDF-S. 8) ist ein Rest des Chat-Formats mitgedruckt; daraus geht der Systemprompt hervor: „Answer the following multiple-choice question. Only respond back by outputting the letter of the correct answer choice.“
- **Prompt Aufgabe 2** (PDF-S. 7, Abb. 2): „True or false, does the word "document" in the following sentence mean "…"?“ mit einem zufällig gewählten Sense.
- **Kunstwörter (Aufgabe 3):** zufälliges WordNet-Wort derselben Wortart, Konsonanten zufällig ersetzt, geprüft, dass das Ergebnis nicht in WordNet steht (PDF-S. 8). Beispiel „moyplenebt“ für *document*; der Prompt beginnt dann mit „The word "moyplenebt" is a noun. Provided the following sentence, infer and select the meaning of the word "moyplenebt" from the presented options.“ (PDF-S. 8, Abb. 3, am vergrößerten Seitenbild gelesen).
- **Modelle und Einstellungen** (PDF-S. 6 bis 7, Tab. 4 und 5): LLaMa-2-7B/13B/70B-Chat und Vicuña-7B lokal als 4-Bit-GPTQ-Fassungen; PaLM-2 als `text-bison` über die Google-API; GPT-3.5-turbo und GPT-4 über die OpenAI-API. Temperatur 0,1 (Vicuña, LLaMa-2), 0,0 (PaLM-2), „Default“ bei GPT-3.5/4; top-p 0,1, top-k 40, Wiederholungsstrafe 1,176; maximale Antwortlänge 10 Tokens (Vicuña), 512 (LLaMa-2), 2 (PaLM-2). Eine Modellversion nennt der Artikel nur einmal: `gpt-4-0613` für die Analyse in Abschnitt 5.2 (PDF-S. 14). Kein Abfragedatum, ein Lauf pro Item.
- **Antwortauswertung:** „appropriate parsing logic utilizing regular expressions“ zieht den Buchstaben aus der Antwort (PDF-S. 6). Wie viele Antworten sich nicht parsen ließen und wie sie gezählt wurden, steht nicht im Artikel.
- **Maß:** Genauigkeit (Anteil richtiger Antworten) (PDF-S. 8); für Aufgabe 2 zusätzlich Precision und Recall (PDF-S. 8 bis 9). Keine Konfidenzintervalle, keine Signifikanztests.
- **Baselines:** keine. Weder MFS noch Zufallsniveau (die Zahl der Optionen pro Item wird nicht berichtet) noch ein überwachtes System auf denselben Items.
- **Ensembles:** Für die gewichteten Verfahren wurde jedes Korpus in Validierung und Test geteilt (410/410, 417/417, 393/393); Gewicht des besten Modells 3, 4 und 2 (PDF-S. 12 bis 13, Tab. 15 und 16). Testwerte „Weighted top“: 71,46 %, 77,70 %, 55,47 % (Tab. 16, PDF-S. 13).

## Wörtliche Stellen

> „This is because the corpora do not enumerate all possible senses of the relevant words but only the correct sense.“ (PDF-S. 7)

> „Once all responses are obtained from the models, appropriate parsing logic utilizing regular expressions is applied to extract the letter corresponding to the answers for use in computing metrics.“ (PDF-S. 6)

> „Specifically, it is possible that the LLM might interpret the unseen word as a misspelling of a valid word.“ (PDF-S. 8)

## Bezug zur Dissertation

- **Aufgabenformat (Protokoll 5, Sense wählen aus Karten):** Aufgabe 1 ist im Kern das Format der Pipeline: Kontext, Zielwort, nummerierte Liste aller Senses des Lemmas, Antwort als Kennbuchstabe. Unterschied: Yae et al. zeigen Glossen (Definitionen), die Dissertation zeigt Begriffsgruppen aus dem Begriffssystem (Protokoll 5). Die Arbeit liefert damit eine Referenzgröße für das Format, aber keine für die Inventarart.
- **Freeze 2 (Protokoll 4.10, LLM-Konfiguration):** Als Negativbeispiel brauchbar. Für GPT-3.5/4 ist die Temperatur „Default“, eine Version steht nur beiläufig in Abschnitt 5.2, es gibt kein Abfragedatum und nur einen Lauf; die Antwortlänge ist bei PaLM-2 auf 2 Tokens gedeckelt (PDF-S. 7, 14). Die Liste in 4.10 (Modell und Version, Prompt, Temperatur, Läufe pro Item) deckt genau diese Lücken ab. Ergänzungsvorschlag: in Freeze 2 auch die **maximale Antwortlänge** und die **Parsing-Regel samt Behandlung unparsbarer Antworten** festschreiben, weil Yae et al. beides nicht berichten.
- **Unparsbare Antworten (Protokoll 9.2):** Die Arbeit sagt nicht, was mit Antworten geschieht, aus denen der Regex keinen Buchstaben zieht. Für 9.2 folgt daraus ein Regelbedarf: Ob eine unparsbare Antwort als falsch, als Abstention oder als fehlend zählt, verändert die gepaarte Differenz zu MFS und gehört vor Freeze 2 festgelegt.
- **MFS-Baseline (Protokoll 1, 9.2):** Yae et al. berichten keine Baseline. Ihre 70 % für GPT-4 lassen sich daher nicht danach beurteilen, ob sie über MFS liegen; das stützt die Entscheidung, die Forschungsfrage als gepaarten Vergleich mit MFS zu stellen (A4, A11).
- **Wortart und Abstraktheit (Protokoll 4.3, 9.1 Punkt 6):** Die Baumkarte (PDF-S. 14) deutet an, dass GPT-4 bei Abstrakta und Handlungsverben schwächer ist als bei physischen Entitäten. Das ist nur eine Grafik ohne Zahlen, passt aber zur Schichtung nach Wortart (NOM, VRB, ADJ).
- **Kunstwort-Aufgabe und Mittelhochdeutsch:** Aufgabe 3 zeigt, dass ein unbekanntes Zielwort die Leistung stark senkt und die Modelle es als Tippfehler eines bekannten Wortes deuten (PDF-S. 8 bis 9). Mittelhochdeutsche Wortformen sind für ein LLM teils ähnlich fremd; dass Fehler über eine Fehldeutung als neuhochdeutsches Wort entstehen, ist eine Vermutung, die die Fehleranalyse der Dissertation prüfen könnte.
- **Leckage (`knowledge/data.md`, B1) und Kontamination (Protokoll 10):** Die Arbeit thematisiert beides nicht, obwohl SemCor und die SemEval-Sätze samt Gold seit Jahren öffentlich sind. Für die Dissertation kein Befund, aber ein Beispiel für die Lücke, die Protokoll 10 schließt.

## Grenzen und Einwände

- **Widersprüchliche Zahlen** (an Textebene und Seitenbild geprüft):
  - Tab. 7 und Abschnitt 4.1 (PDF-S. 8) geben PaLM-2 65,98 % und GPT-3.5 61,22 %. Abschnitt 4.4.1 (PDF-S. 11) sagt dagegen „GPT-3.5 outperformed PaLM in Task #1“, und in Tab. 10 (PDF-S. 10) erhält PaLM in der linearen Regression für Aufgabe 1 denselben Schätzwert wie LLaMa-2-70B (56,71), was bei einem linearen Modell gleiche Genauigkeit (61,22 %) voraussetzt. Welche der beiden Zahlen zu welchem Modell gehört, ist aus dem Artikel nicht zu entscheiden.
  - Abschnitt 4.3 (PDF-S. 9) nennt Vicuña mit 28,5 % als schwächstes Modell in Aufgabe 3; nach Tab. 9 hat LLaMa-2-13B 28,50 %, Vicuña 31,93 %.
  - Abschnitt 4.3 verweist für Aufgabe 2 auf Tab. 7; gemeint ist Tab. 8. Tab. 16 heißt „for Objective #3“, enthält aber alle drei Aufgaben (PDF-S. 13).
- **Keine Baseline, keine Unsicherheit:** weder MFS noch Zufallsniveau, keine Intervalle, keine Tests; Unterschiede von wenigen Prozentpunkten bei ca. 800 Items sind nicht als gesichert gezeigt.
- **Auswahl der Items unklar:** Wie die ca. 800 Items aus sechs Korpora gezogen wurden und wie viele Optionen sie im Mittel haben, fehlt. Die Optionen stammen aus BabelNet, das Gold teils aus WordNet (PDF-S. 6 bis 7); wie Gold-Sense und BabelNet-Option zur Deckung gebracht wurden, steht nicht da.
- **Mehrere Gold-Senses:** Ob Items mit mehr als einem richtigen Sense vorkamen und wie sie gewertet wurden, sagt die Arbeit nicht.
- **Reproduzierbarkeit:** Standardparameter und unbestimmte Versionen bei den API-Modellen; quantisierte statt volle Gewichte bei den offenen Modellen, ohne Vergleich (PDF-S. 6).
- **Kontamination** nicht diskutiert.
- **Parameterschätzung** (PDF-S. 10 bis 11) stützt sich auf vier offene Modelle und eine Online-Kurvenanpassung [83]; die Autoren halten das Ergebnis selbst für nicht belastbar.
- **Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar:** gering bis mittel. Englische Standardkorpora mit Wörterbuchglossen; das Aufgabenformat ist übertragbar, die Zahlen sind es nicht.

## Weiterführend

- Kocoń et al. 2023, „ChatGPT: Jack of all trades, master of none“, *Information Fusion* 99, enthält eine WSD-Auswertung von ChatGPT (PDF-S. 2, 5; Ref. 10).
- Maru, Conia, Bevilacqua & Navigli 2022, „Nibbling at the hard core of word sense disambiguation“ (PDF-S. 12, Ref. 86); im Protokoll 9.2 schon zitiert.
- Bevilacqua, Pasini, Raganato & Navigli 2021, WSD-Survey (PDF-S. 15, Ref. 88); liegt als PDF vor.
- Hosseini, Hosseini & Javidan 2024, LLMs zur Disambiguierung klinischer Abkürzungen (PDF-S. 5, Ref. 64).
- Barba, Pasini & Navigli 2021, ESC (PDF-S. 5, Ref. 38).
