# Literatur

Eigene Literatur zur Dissertation: Volltexte lokal, Zusammenfassungen im Repo.
Angelegt am 2026-10-23, Bestand am selben Tag gesichtet und umsortiert.

| Ordner/Datei | Inhalt | im Repo? |
|---|---|---|
| `pdf/` | Volltexte der aktiven Literatur, flach, Dateiname `Nachname-Jahr-Kurztitel.pdf` | **nein** (`.gitignore`) |
| `zusammenfassungen/` | eine `.md` pro Werk, gleicher Name wie das PDF | ja |
| `VORLAGE.md` | Gliederung jeder Zusammenfassung | ja |
| `archiv-intermedialitaet/` | Literatur zum früheren Dissertationsthema (Intermedialität), 23 Dateien samt alter Literaturliste; wird nicht zusammengefasst | **nein** |
| `material/` | eigene Listen und Folien (`Literaturliste.xlsx`, `Free-Prompting-25.pptx`) und `umbenennung-2026-10-23.csv` mit allen alten und neuen Dateinamen | **nein** |
| `md/` | maschinell erzeugt: `<Name>.md` (Volltext, `pdf_zu_md.py`) und `<Name>.markierungen.md` (Julias Anmerkungen im PDF, `markierungen.py`) | **nein** |
| `pdf_zu_md.py`, `markierungen.py`, `seiten.py` | die Skripte dazu; Aufruf und Verfahren im Kopf der Datei. `seiten.py` legt rohe Textebene und Seitenbilder zum Prüfen in einen eigenen Ordner pro Aufruf unter `temp/seiten/` (gitignored) und gibt dessen Pfad aus | ja |

`pdf/` ist der einzige Ort für die Volltexte. Kopien unter alten Namen (direkt in `literatur/`, in
`Dissertation/attachments/`) wurden am 2026-10-28 entfernt, nachdem jede per SHA-256 als byte-gleich
mit einer Datei in `pdf/`, `material/` oder `archiv-intermedialitaet/` bestätigt war; drei ältere
Fassungen in `Dissertation/attachments/` enthielten nur eine Teilmenge der Markierungen in `pdf/`.

**Dateinamen:** bei zwei Autor:innen beide Namen, ab drei `Nachname-etal`, bei Sammelbänden die
Herausgeber:innen. Umlaute als `ae`, `oe`, `ue`. Ohne bekanntes Jahr `oJ`.

**Themen statt Unterordner:** Ein Werk gehört oft zu mehreren Themen, ein Ordner erzwingt eines.
Das Thema steht deshalb in der Übersicht unten, die PDFs liegen flach.

## Ablauf

1. **Ablegen:** neue PDFs nach `pdf/`, nach dem Muster benennen. Gescannte PDFs ohne Textebene
   vorher mit OCR versehen, sonst lässt sich nichts zitieren.
2. **Umwandeln:** `python literatur/pdf_zu_md.py` (Volltext) und `python literatur/markierungen.py`
   (Anmerkungen) aus dem Repo-Wurzelverzeichnis. Docling liest keine Anmerkungen, deshalb das zweite
   Skript. Markierungen gibt es bisher in 17 PDFs (Stand 2026-10-28); was als „Zeichen“ erscheint, sind
   gezeichnete Häkchen und Randstriche, für die nur die Position angegeben ist. Auf Seiten mit
   Abbildungen oder Baumdiagrammen verwirft Docling oft auch den Fließtext; liefert es weniger als
   30 % der Zeichen der Textebene, hängt das Skript die rohe Textebene gekennzeichnet an (am
   2026-10-28 mit `--nachtragen` für 40 Seiten in 10 PDFs nachgeholt, u. a. Köhnlein S. 34 zur Homonymie).
   Tabellen und Text in Abbildungen bleiben trotzdem am PDF zu prüfen. Außerdem stellt Docling einen
   Absatz, der über einen Seitenumbruch läuft, ganz unter die Anfangsseite; Seitenangaben deshalb an
   der Textebene prüfen (`python literatur/seiten.py <Name>.pdf`).
3. **Zusammenfassen:** Der Agent `aufbereiter` (seit 2026-10-28; vorher `quellen`) liest jedes
   Werk vollständig und füllt die Vorlage. Gibt es `md/<Name>.markierungen.md`, liest er sie mit:
   Die Stellen, die Julia markiert hat, gehören geprüft, ob sie in die Kernaussagen gehören. Er
   wandelt bei Bedarf selbst um, prüft an Textebene und Seitenbildern, trägt für seine Werke die
   Spalte „Zusammenfassung“, bibliografische Korrekturen, `references.txt` und geklärte Fragen in
   `BESCHAFFUNG.md` selbst nach und löscht am Ende genau die Prüfordner, die er angelegt hat. Pro Lauf zwei bis fünf Werke, mehrere Läufe
   parallel. Bücher kapitelweise; der Auftrag nennt dann die relevanten Kapitel.
4. **Gegenlesen:** Jede Zusammenfassung beginnt mit dem Status „KI-Zusammenfassung, nicht
   gegengelesen". Erst wenn Julia Kernaussagen und Seitenangaben am PDF geprüft hat, wird daraus
   „gegengelesen am …". Nur dann zählt sie für den Agenten `autor` als ✔.
5. **Verdichten:** Thematische Synthesen bleiben in `goldstandard/LITERATUR-*.md` und verweisen
   auf die Zusammenfassung hier, statt sie zu wiederholen.

## Regeln

- Jede Kernaussage und jede Zahl mit Seite. Was die Arbeit nur referiert, ist als solches markiert.
- Keine Ergänzungen aus dem Gedächtnis des Modells. Steht etwas nicht im PDF, gehört es nicht in
  die Zusammenfassung.
- Wörtliche Zitate nur kurz und nur, was voraussichtlich zitiert wird (Urheberrecht).
- Kein Gedankenstrich (U+2014) in `.md`; in einem zitierten Titel in Backticks.

## Übersicht

Priorität für das Zusammenfassen (Vorschlag vom 2026-10-23, die neun zuletzt aufgenommenen Werke
von Julia am 2026-10-28 eingestuft): **1** trägt Protokoll oder Daten
direkt, **2** Methodenkontext für den Artikel, **3** Hintergrund. Bibliografische Angaben sind
aus dem PDF abgelesen; „zu prüfen" heißt, sie stehen dort nicht vollständig.

| PDF | Kurzbeleg | Thema | Prio | Seiten | Anmerkung | Zusammenfassung |
|---|---|---|---|---|---|---|
| `Schmidt-1985-Parser-Homographen-MHD.pdf` | Schmidt 1985 | MHDBDB, Homographen, Begriffssystem | 1 | 9 | Scan ohne Textebene (OCR); S. 345 bis 353 in Hamesse & Zampolli (Hg.), *Computers in Literary and Linguistic Computing*, Champion-Slatkine 1985 (Band am Titelblatt ✔, Schmidts Beitrag darin nur über ResearchGate ○); hieß bis 2026-10-28 `Schmidt-oJ-…`; enthält Julias Markierungen; laut Literaturliste gelesen und zusammengefasst | [ja](zusammenfassungen/Schmidt-1985-Parser-Homographen-MHD.md) |
| `Hinkelmanns-2019-MHD-Lexikographie-Semantic-Web.pdf` | Hinkelmanns 2019 | MHDBDB, Begriffssystem, Linked Data | 1 | 13 | DOI 10.1515/mial-2019-0009 | [ja](zusammenfassungen/Hinkelmanns-2019-MHD-Lexikographie-Semantic-Web.md) |
| `Tittel-etal-2020-Hallig-Wartburg-Ontologie.pdf` | Tittel, Gillis-Webber & Nannini 2020 | Begriffssystem (Hallig-Wartburg), Ontologie | 1 | 10 | LDL-2020 @ LREC | [ja](zusammenfassungen/Tittel-etal-2020-Hallig-Wartburg-Ontologie.md) |
| `Klein-Dipper-2016-Handbuch-ReM.pdf` | Klein & Dipper 2016 | Mittelhochdeutsch, Korpus | 1 | 23 | BLA 19 | [ja](zusammenfassungen/Klein-Dipper-2016-Handbuch-ReM.md) |
| `Dipper-etal-2013-HiTS.pdf` | Dipper et al. 2013 | historische Wortarten, Tagset | 2 | 53 | JLCL 28(1), S. 85 bis 137, DOI 10.21248/jlcl.28.2013.170 (Crossref), CC BY 4.0 | [ja](zusammenfassungen/Dipper-etal-2013-HiTS.md) |
| `Navigli-2009-WSD-Survey.pdf` | Navigli 2009 | WSD Überblick | 1 | 69 | ACM Computing Surveys | [ja](zusammenfassungen/Navigli-2009-WSD-Survey.md) |
| `Ide-Veronis-1998-WSD-State-of-the-Art.pdf` | Ide & Véronis 1998 | WSD Überblick | 2 | 51 | *Computational Linguistics* 24(1), S. 1 bis 40, März 1998 (ACL Anthology J98-1001); **lokales PDF ist ein Manuskript mit eigener Seitenzählung**, Zitate an der Druckfassung nachschlagen | [ja](zusammenfassungen/Ide-Veronis-1998-WSD-State-of-the-Art.md) |
| `Navigli-2012-Quick-Tour-WSD.pdf` | Navigli 2012 | WSD Überblick | 3 | 15 | SOFSEM, LNCS 7147 | nein |
| `Henrich-2015-WSD-GermaNet.pdf` | Henrich 2015 | WSD Deutsch, Goldstandard | 1 | 393 | Dissertation Tübingen; kapitelweise | [ja](zusammenfassungen/Henrich-2015-WSD-GermaNet.md) |
| `Henrich-etal-2012-WebCAGe.pdf` | Henrich, Hinrichs & Vodolazova 2012 | WSD Deutsch, Korpus | 2 | 10 | EACL 2012, S. 387 bis 396 (ACL Anthology E12-1039) | [ja](zusammenfassungen/Henrich-etal-2012-WebCAGe.md) |
| `Iacobacci-etal-2016-Embeddings-WSD.pdf` | Iacobacci, Pilehvar & Navigli 2016 | WSD Methoden | 3 | 11 | ACL 2016; hieß vorher `navigli.pdf` | nein |
| `Rekabsaz-2018-Word-Representation.pdf` | Rekabsaz 2018 | WSD Methoden | 3 | 140 | Dissertation TU Wien | nein |
| `Miller-1995-WordNet.pdf` | Miller 1995 | Inventare | 3 | 3 | CACM 38(11) | nein |
| `Pangakis-etal-2023-Automated-Annotation-Validation.pdf` | Pangakis, Wolken & Fasching 2023 | LLM als Annotator, Validierung | 1 | 20 | arXiv-Preprint (nur v1); begutachtete Fassung ist Pangakis & Wolken 2025 (nächste Zeile), beim Zitieren diese verwenden | [ja](zusammenfassungen/Pangakis-etal-2023-Automated-Annotation-Validation.md) |
| `Pangakis-Wolken-2025-Humans-in-the-Loop.pdf` | Pangakis & Wolken 2025 | LLM als Annotator, Validierung | 1 | 22 | ICWSM 19(1), S. 1471 bis 1492, DOI 10.1609/icwsm.v19i1.35883; begutachtete Fassung von Pangakis et al. 2023 mit neuem Titel, ohne Fasching, teils anderen Zahlen (siehe Zusammenfassung von 2023) | nein |
| `Bhat-Varma-2023-LLMs-as-Annotators.pdf` | Bhat & Varma 2023 | LLM als Annotator, ressourcenarme Sprachen | 1 | 8 | Eval4NLP 2023 | [ja](zusammenfassungen/Bhat-Varma-2023-LLMs-as-Annotators.md) |
| `Li-etal-2023-CoAnnotating.pdf` | Li et al. 2023 | LLM und Mensch annotieren gemeinsam | 1 | 19 | EMNLP 2023, S. 1487 bis 1505, DOI 10.18653/v1/2023.emnlp-main.92; Verlagsfassung seit 2026-10-28 (vorher arXiv v1 ohne Anhänge) | [ja](zusammenfassungen/Li-etal-2023-CoAnnotating.md) |
| `Galka-Vogeler-2026-LLM-NER-Editionen.pdf` | Galka & Vogeler 2026 | LLM-Annotation in Editionen | 1 | 27 | IJDH 7(3), S. 483 bis 509 laut Crossref (lokales PDF: Online-First ohne Seitenzahlen), DOI 10.1007/s42803-025-00114-8 | [ja](zusammenfassungen/Galka-Vogeler-2026-LLM-NER-Editionen.md) |
| `Jannidis-etal-2025-LLMs-German-Poetry.pdf` | Jannidis et al. 2025 | LLM und historische Literatur | 2 | 25 | JCLS 4(1) | [ja](zusammenfassungen/Jannidis-etal-2025-LLMs-German-Poetry.md) |
| `Beck-Koellner-2023-GHisBERT.pdf` | Beck & Köllner 2023 | Sprachmodell historisches Deutsch | 2 | 13 | LChange 2023 | [ja](zusammenfassungen/Beck-Koellner-2023-GHisBERT.md) |
| `Weeber-etal-2021-Active-Learning.pdf` | Weeber et al. 2021 | Annotation | 3 | 2 | Kurzbeitrag; laut Literaturliste gelesen und zusammengefasst | nein |
| `Semmelrock-etal-2025-Reproducibility-ML.pdf` | Semmelrock et al. 2025 | Reproduzierbarkeit | 2 | 19 | AI Magazine 46(2), e70002, 2025, DOI 10.1002/aaai.70002 (Crossref); 2024 ist der arXiv-Preprint 2406.14325 | [ja](zusammenfassungen/Semmelrock-etal-2025-Reproducibility-ML.md) |
| `Kowald-etal-2024-Trustworthy-AI.pdf` | Kowald et al. 2024 | Vertrauenswürdige KI | 3 | 21 | Frontiers in Big Data | nein |
| `Klein-etal-2025-Provocations.pdf` | Klein et al. 2025 | KI und Geisteswissenschaften | 2 | 21 | arXiv 2502.19190, lokal v1; v2 vom 2026-01-12, als FAccT 2026 gesetzt, Erscheinen nicht bestätigt (Stand 2026-10-28) | [ja](zusammenfassungen/Klein-etal-2025-Provocations.md) |
| `Steller-2024-KI-DH-Positionspapier.pdf` | Steller 2024 | KI in den DH | 3 | 20 | Positionspapier v0.9.1 | nein |
| `Gengnagel-etal-2024-LLM-Glossary.pdf` | Gengnagel et al. 2024 | LLM Begriffe | 3 | 11 | Entwurf | nein |
| `Chen-etal-2025-LLM-Ensemble.pdf` | Chen et al. 2025 | LLM-Ensembles | 3 | 10 | Survey; laut Literaturliste gelesen und zusammengefasst | nein |
| `Yang-etal-2024-Harnessing-LLMs.pdf` | Yang et al. 2024 | LLM Überblick | 3 | 32 | DOI 10.1145/3649506 | nein |
| `An-etal-2024-LLM-Context.pdf` | An et al. 2024 | LLM Kontextnutzung | 3 | 19 | | nein |
| `Campesato-2024-LLM-Introduction.pdf` | Campesato 2024 | LLM Lehrbuch | 3 | 502 | nur bei Bedarf kapitelweise | nein |
| `Koehnlein-2025-Benchmark-Framework-LLM.pdf` | Köhnlein 2025 | LLM-Benchmark, Linguistik | 2 | 97 | Masterarbeit Graz; laut Literaturliste gelesen und zusammengefasst, die Zusammenfassung liegt nicht hier | [ja](zusammenfassungen/Koehnlein-2025-Benchmark-Framework-LLM.md) |
| `Matusch-2025-Entitaeten-Disambiguierung.pdf` | Matusch 2025 | Entitäten-Disambiguierung | 3 | 83 | Masterarbeit FH Joanneum | nein |
| `Ristic-2025-Symbolic-NLI-German.pdf` | Ristic 2025 | NLI Deutsch | 3 | 85 | Diplomarbeit TU Wien | nein |
| `Ganslmayer-Schwarz-2021-Historische-Wortbildung.pdf` | Ganslmayer & Schwarz (Hg.) 2021 | historische Wortbildung | 3 | 453 | Sammelband; relevante Beiträge auswählen | nein |
| `Devlin-etal-2019-BERT.pdf` | Devlin et al. 2019 | Sprachmodelle | 3 | 16 | NAACL 2019 | nein |
| `Liu-etal-2019-RoBERTa.pdf` | Liu et al. 2019 | Sprachmodelle | 3 | 13 | arXiv | nein |
| `Schiller-etal-1999-STTS.pdf` | Schiller et al. 1999 | Tagset Deutsch | 3 | 87 | Jahr aus altem Dateinamen, im PDF nicht lesbar | nein |
| `Telljohann-etal-2004-TueBa-DZ.pdf` | Telljohann, Hinrichs & Kübler 2004 | Baumbank Deutsch | 3 | 4 | LREC 2004 | nein |
| `Hinkelmanns-Zeppezauer-Wachauer-2020-MHDBDB.pdf` | Hinkelmanns & Zeppezauer-Wachauer 2020 | MHDBDB, Begriffssystem, Linked Data | 2 | 12 | gedruckt S. 73 bis 84 (Bamberg); erwähnt keine graphematischen Types | [ja](zusammenfassungen/Hinkelmanns-Zeppezauer-Wachauer-2020-MHDBDB.md) |
| `Hinkelmanns-Zeppezauer-Wachauer-2023-MHDBDB-Projektbericht.pdf` | Hinkelmanns & Zeppezauer-Wachauer 2023 | MHDBDB, Herkunft der Typlisten | 1 | 5 | gedruckt S. 179 bis 181; Kernstelle S. 180 (PDF-Seite 4); KUPS, CC BY 3.0 | [ja](zusammenfassungen/Hinkelmanns-Zeppezauer-Wachauer-2023-MHDBDB-Projektbericht.md) |
| `Henrich-Hinrichs-2010-GernEdiT.pdf` | Henrich & Hinrichs 2010 | WSD Deutsch, Annotationswerkzeug | 3 | 8 | LREC 2010, gedruckt S. 2228 bis 2235 | nein |
| `Mambrini-Passarotti-2023-LiLa.pdf` | Mambrini & Passarotti 2023 | Linked Data, Latein | 3 | 5 | JOHD 9(1), Artikel 28 | nein |
| `Scholger-Bleier-2026-ChatGPT-RIDE.pdf` | Scholger & Bleier 2026 | LLM und digitale Editionen | 2 | 32 | RIDE 19, Rezension der Ressource ChatGPT, DOI 10.18716/ride.a.19.4; Zitierweise Absatznummer | [ja](zusammenfassungen/Scholger-Bleier-2026-ChatGPT-RIDE.md) |
| `Telljohann-etal-2017-TueBa-DZ-Stylebook.pdf` | Telljohann et al. 2017 | Baumbank Deutsch, Richtlinien | 3 | 166 | Stylebook, Juli 2017 | nein |
| `Tittel-Chiarcos-2018-DEAF-LOD.pdf` | Tittel & Chiarcos 2018 | Linked Data, historische Lexikographie | 3 | 10 | Venue laut `BESCHAFFUNG.md` widersprüchlich (LDL-2018 oder GLOBALEX), PDF ohne Seitenzahlen | nein |
| `Zeppezauer-Wachauer-2022-Fuenfzig-Jahre-MHDBDB.pdf` | Zeppezauer-Wachauer 2022 | MHDBDB, Geschichte, Graphdaten | 1 | 27 | BmE Themenheft 12, S. 161 bis 186 | [ja](zusammenfassungen/Zeppezauer-Wachauer-2022-Fuenfzig-Jahre-MHDBDB.md) |
| `Strutz-2026-LLM-TEI-Evaluation.pdf` | Strutz 2026 | LLM-Evaluation, TEI-Kodierung | 2 | 20 | JOHD 12, Artikel 39, DOI 10.5334/johd.484 (Zitiervorschlag S. 1); lag bis 2026-10-28 als `69b0024ec3b99.pdf` unverzeichnet in `literatur/` | [ja](zusammenfassungen/Strutz-2026-LLM-TEI-Evaluation.md) |
| `Yae-etal-2025-LLMs-WSD.pdf` | Yae, Skelly, Ranly & LaCasse 2025 | LLM-WSD, Evaluation | offen | 18 | Neural Computing and Applications 37, DOI 10.1007/s00521-024-10747-5; CC BY-NC-ND 4.0 laut Crossref; von Springer geladen 2026-10-28; Vorschlag Prio 1 (Sense-Auswahl aus vorgegebener Liste, am nächsten an der Pipeline) | nein |
| `Basile-etal-2025-WSD-Capabilities-LLMs.pdf` | Basile, Siciliani, Musacchio & Semeraro 2025 | LLM-WSD, Evaluation | offen | 14 | arXiv 2503.08662 v1, Preprint; Lizenz und Status zu prüfen; Vorschlag Prio 1 | nein |
| `Meconi-etal-2025-LLMs-Word-Senses.pdf` | Meconi, Stirpe, Martelli, Lavalle & Navigli 2025 | LLM-WSD, Evaluation | offen | 20 | arXiv 2509.13905 v1, laut arXiv „to be published in EMNLP 2025“; Verlagsfassung und Lizenz zu prüfen; Vorschlag Prio 1 | nein |
| `Manjavacas-Fonteyn-2022-Adapting-vs-Pretraining.pdf` | Manjavacas & Fonteyn 2022a | Sprachmodelle historische Sprachen, WSD | offen | 19 | JDMDH (NLP4DH), DOI 10.46298/jdmdh.9152, von episciences geladen; Lizenz zu prüfen; Vorschlag Prio 2 | nein |
| `Manjavacas-Fonteyn-2022-Nonparametric-WSD.pdf` | Manjavacas Arevalo & Fonteyn 2022b | WSD historische Sprachen | offen | 12 | NLP4DH 2022, S. 123 bis 134, ACL Anthology 2022.nlp4dh-1.16; Vorschlag Prio 2 | nein |
| `Raganato-etal-2017-WSD-Evaluation-Framework.pdf` | Raganato, Camacho-Collados & Navigli 2017 | WSD Evaluation, Benchmark | offen | 12 | EACL 2017, S. 99 bis 110, ACL Anthology E17-1010; in `goldstandard/LITERATUR-STICHPROBE.md` schon mit ✔ zitiert; Vorschlag Prio 1 | nein |
| `Bevilacqua-etal-2021-WSD-Survey.pdf` | Bevilacqua, Pasini, Raganato & Navigli 2021 | WSD Überblick | offen | 9 | IJCAI-21, S. 4330 bis 4338, DOI 10.24963/ijcai.2021/593, von ijcai.org geladen; Vorschlag Prio 2 | nein |

**In der Literaturliste, aber ohne PDF:** Roe 2025 (*How to Use Generative AI in Educational
Research*), Abualhaija 2016 (*D-Bees*), Tischler 2010 (*Word sense disambiguation, Einsatz in der
Medizin*), Yedurkar et al. 2026, Akerkar 2026.

**Nachgetragen am 2026-10-23:** Hinkelmanns & Zeppezauer-Wachauer 2023 (Herkunft der
Typlisten, `knowledge/data.md` Abschnitt 3; nicht dasselbe wie Hinkelmanns 2019) liegt jetzt
als PDF vor. Lesk 1986 fehlt weiterhin (ACM lieferte nur eine HTML-Sperrseite).
