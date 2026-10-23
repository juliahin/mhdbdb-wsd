# Literatur

Eigene Literatur zur Dissertation: Volltexte lokal, Zusammenfassungen im Repo.
Angelegt am 2026-10-23, Bestand am selben Tag gesichtet und umsortiert.

| Ordner/Datei | Inhalt | im Repo? |
|---|---|---|
| `pdf/` | Volltexte der aktiven Literatur, flach, Dateiname `Nachname-Jahr-Kurztitel.pdf` | **nein** (`.gitignore`) |
| `md/` | Volltexte als Markdown, gleicher Name wie das PDF, mit Seitenmarken `<!-- PDF-Seite n -->` (physische PDF-Seite, nicht die gedruckte); `_protokoll.jsonl` hält pro Umwandlung SHA-256 des PDFs, OCR ja/nein und Docling-Version fest. Erzeugt von `pdf_zu_md.py`; Erstlauf über alle PDFs am 2026-10-23 begonnen | **nein** (aus den Volltexten abgeleitet) |
| `pdf_zu_md.py` | Umwandlung `pdf/` nach `md/` mit Docling, Scans per OCR; Aufruf im Docstring | ja |
| `zusammenfassungen/` | eine `.md` pro Werk, gleicher Name wie das PDF | ja |
| `VORLAGE.md` | Gliederung jeder Zusammenfassung | ja |
| `references.txt` | BibTeX der Literatur zur Dissertation | ja |
| `BESCHAFFUNG.md` | Werke aus `references.txt` ohne PDF: Angaben geprüft, legaler Zugangsweg | ja |
| `archiv-intermedialitaet/` | Literatur zum früheren Dissertationsthema (Intermedialität), 23 Dateien samt alter Literaturliste; wird nicht zusammengefasst | **nein** |
| `material/` | eigene Listen und Folien (`Literaturliste.xlsx`, `Free-Prompting-25.pptx`) und `umbenennung-2026-10-23.csv` mit allen alten und neuen Dateinamen | **nein** |

**Dateinamen:** bei zwei Autor:innen beide Namen, ab drei `Nachname-etal`, bei Sammelbänden die
Herausgeber:innen. Umlaute als `ae`, `oe`, `ue`. Ohne bekanntes Jahr `oJ`.

**Themen statt Unterordner:** Ein Werk gehört oft zu mehreren Themen, ein Ordner erzwingt eines.
Das Thema steht deshalb in der Übersicht unten, die PDFs liegen flach.

## Ablauf

1. **Ablegen:** neue PDFs nach `pdf/`, nach dem Muster benennen. Gescannte PDFs ohne Textebene
   vorher mit OCR versehen, sonst lässt sich nichts zitieren.
2. **Zusammenfassen:** Der Agent `quellen` liest jedes PDF vollständig und füllt die Vorlage.
   Pro Lauf etwa fünf Werke, mehrere Läufe parallel. Bücher kapitelweise; der Auftrag nennt dann
   die relevanten Kapitel.
3. **Gegenlesen:** Jede Zusammenfassung beginnt mit dem Status „KI-Zusammenfassung, nicht
   gegengelesen". Erst wenn Julia Kernaussagen und Seitenangaben am PDF geprüft hat, wird daraus
   „gegengelesen am …". Nur dann zählt sie für den Agenten `autor` als ✔.
4. **Verdichten:** Thematische Synthesen bleiben in `goldstandard/LITERATUR-*.md` und verweisen
   auf die Zusammenfassung hier, statt sie zu wiederholen.

## Regeln

- Jede Kernaussage und jede Zahl mit Seite. Was die Arbeit nur referiert, ist als solches markiert.
- Keine Ergänzungen aus dem Gedächtnis des Modells. Steht etwas nicht im PDF, gehört es nicht in
  die Zusammenfassung.
- Wörtliche Zitate nur kurz und nur, was voraussichtlich zitiert wird (Urheberrecht).
- Kein Gedankenstrich (U+2014) in `.md`; in einem zitierten Titel in Backticks.

## Übersicht

Priorität für das Zusammenfassen (Vorschlag vom 2026-10-23): **1** trägt Protokoll oder Daten
direkt, **2** Methodenkontext für den Artikel, **3** Hintergrund. Bibliografische Angaben sind
aus dem PDF abgelesen; „zu prüfen" heißt, sie stehen dort nicht vollständig.

| PDF | Kurzbeleg | Thema | Prio | Seiten | Anmerkung | Zusammenfassung |
|---|---|---|---|---|---|---|
| `Schmidt-oJ-Parser-Homographen-MHD.pdf` | Schmidt o. J. | MHDBDB, Homographen, Begriffssystem | 1 | 9 | Scan ohne Textebene, braucht OCR; S. 345 bis 353 eines Sammelbands, jüngster Verweis 1983; Quelle und Jahr zu prüfen; enthält Julias Markierungen; laut Literaturliste gelesen und zusammengefasst | nein |
| `Hinkelmanns-2019-MHD-Lexikographie-Semantic-Web.pdf` | Hinkelmanns 2019 | MHDBDB, Begriffssystem, Linked Data | 1 | 13 | DOI 10.1515/mial-2019-0009 | nein |
| `Tittel-etal-2020-Hallig-Wartburg-Ontologie.pdf` | Tittel, Gillis-Webber & Nannini 2020 | Begriffssystem (Hallig-Wartburg), Ontologie | 1 | 10 | LDL-2020 @ LREC | nein |
| `Klein-Dipper-2016-Handbuch-ReM.pdf` | Klein & Dipper 2016 | Mittelhochdeutsch, Korpus | 1 | 23 | BLA 19 | nein |
| `Dipper-etal-2013-HiTS.pdf` | Dipper et al. 2013 | historische Wortarten, Tagset | 2 | 53 | JLCL 28(1), 85 bis 137 | nein |
| `Navigli-2009-WSD-Survey.pdf` | Navigli 2009 | WSD Überblick | 1 | 69 | ACM Computing Surveys | nein |
| `Ide-Veronis-1998-WSD-State-of-the-Art.pdf` | Ide & Véronis 1998 | WSD Überblick | 2 | 51 | Jahr und Venue nicht im PDF, zu prüfen | nein |
| `Navigli-2012-Quick-Tour-WSD.pdf` | Navigli 2012 | WSD Überblick | 3 | 15 | SOFSEM, LNCS 7147 | nein |
| `Henrich-2015-WSD-GermaNet.pdf` | Henrich 2015 | WSD Deutsch, Goldstandard | 1 | 393 | Dissertation Tübingen; kapitelweise | nein |
| `Henrich-etal-2012-WebCAGe.pdf` | Henrich, Hinrichs & Vodolazova 2012 | WSD Deutsch, Korpus | 2 | 10 | EACL 2012 | nein |
| `Iacobacci-etal-2016-Embeddings-WSD.pdf` | Iacobacci, Pilehvar & Navigli 2016 | WSD Methoden | 3 | 11 | ACL 2016; hieß vorher `navigli.pdf` | nein |
| `Rekabsaz-2018-Word-Representation.pdf` | Rekabsaz 2018 | WSD Methoden | 3 | 140 | Dissertation TU Wien | nein |
| `Miller-1995-WordNet.pdf` | Miller 1995 | Inventare | 3 | 3 | CACM 38(11) | nein |
| `Pangakis-etal-2023-Automated-Annotation-Validation.pdf` | Pangakis, Wolken & Fasching 2023 | LLM als Annotator, Validierung | 1 | 20 | Preprint, Status zu prüfen | nein |
| `Bhat-Varma-2023-LLMs-as-Annotators.pdf` | Bhat & Varma 2023 | LLM als Annotator, ressourcenarme Sprachen | 1 | 8 | Eval4NLP 2023 | nein |
| `Li-etal-2023-CoAnnotating.pdf` | Li et al. 2023 | LLM und Mensch annotieren gemeinsam | 1 | 12 | Venue zu prüfen | nein |
| `Galka-Vogeler-2026-LLM-NER-Editionen.pdf` | Galka & Vogeler 2026 | LLM-Annotation in Editionen | 1 | 27 | IJDH, DOI 10.1007/s42803-025-00114-8 | nein |
| `Jannidis-etal-2025-LLMs-German-Poetry.pdf` | Jannidis et al. 2025 | LLM und historische Literatur | 2 | 25 | JCLS 4(1) | nein |
| `Beck-Koellner-2023-GHisBERT.pdf` | Beck & Köllner 2023 | Sprachmodell historisches Deutsch | 2 | 13 | LChange 2023 | nein |
| `Weeber-etal-2021-Active-Learning.pdf` | Weeber et al. 2021 | Annotation | 3 | 2 | Kurzbeitrag; laut Literaturliste gelesen und zusammengefasst | nein |
| `Semmelrock-etal-2025-Reproducibility-ML.pdf` | Semmelrock et al. 2025 | Reproduzierbarkeit | 2 | 19 | AI Magazine; Literaturliste nennt 2024 | nein |
| `Kowald-etal-2024-Trustworthy-AI.pdf` | Kowald et al. 2024 | Vertrauenswürdige KI | 3 | 21 | Frontiers in Big Data | nein |
| `Klein-etal-2025-Provocations.pdf` | Klein et al. 2025 | KI und Geisteswissenschaften | 2 | 21 | arXiv 2502.19190 | nein |
| `Steller-2024-KI-DH-Positionspapier.pdf` | Steller 2024 | KI in den DH | 3 | 20 | Positionspapier v0.9.1 | nein |
| `Gengnagel-etal-2024-LLM-Glossary.pdf` | Gengnagel et al. 2024 | LLM Begriffe | 3 | 11 | Entwurf | nein |
| `Chen-etal-2025-LLM-Ensemble.pdf` | Chen et al. 2025 | LLM-Ensembles | 3 | 10 | Survey; laut Literaturliste gelesen und zusammengefasst | nein |
| `Yang-etal-2024-Harnessing-LLMs.pdf` | Yang et al. 2024 | LLM Überblick | 3 | 32 | DOI 10.1145/3649506 | nein |
| `An-etal-2024-LLM-Context.pdf` | An et al. 2024 | LLM Kontextnutzung | 3 | 19 | | nein |
| `Campesato-2024-LLM-Introduction.pdf` | Campesato 2024 | LLM Lehrbuch | 3 | 502 | nur bei Bedarf kapitelweise | nein |
| `Koehnlein-2025-Benchmark-Framework-LLM.pdf` | Köhnlein 2025 | LLM-Benchmark, Linguistik | 2 | 97 | Masterarbeit Graz; laut Literaturliste gelesen und zusammengefasst, die Zusammenfassung liegt nicht hier | nein |
| `Matusch-2025-Entitaeten-Disambiguierung.pdf` | Matusch 2025 | Entitäten-Disambiguierung | 3 | 83 | Masterarbeit FH Joanneum | nein |
| `Ristic-2025-Symbolic-NLI-German.pdf` | Ristic 2025 | NLI Deutsch | 3 | 85 | Diplomarbeit TU Wien | nein |
| `Ganslmayer-Schwarz-2021-Historische-Wortbildung.pdf` | Ganslmayer & Schwarz (Hg.) 2021 | historische Wortbildung | 3 | 453 | Sammelband; relevante Beiträge auswählen | nein |
| `Devlin-etal-2019-BERT.pdf` | Devlin et al. 2019 | Sprachmodelle | 3 | 16 | NAACL 2019 | nein |
| `Liu-etal-2019-RoBERTa.pdf` | Liu et al. 2019 | Sprachmodelle | 3 | 13 | arXiv | nein |
| `Schiller-etal-1999-STTS.pdf` | Schiller et al. 1999 | Tagset Deutsch | 3 | 87 | Jahr aus altem Dateinamen, im PDF nicht lesbar | nein |
| `Telljohann-etal-2004-TueBa-DZ.pdf` | Telljohann, Hinrichs & Kübler 2004 | Baumbank Deutsch | 3 | 4 | LREC 2004 | nein |
| `Hinkelmanns-Zeppezauer-Wachauer-2020-MHDBDB.pdf` | Hinkelmanns & Zeppezauer-Wachauer 2020 | MHDBDB, Begriffssystem, Linked Data | offen | 12 | gedruckt S. 73 bis 84 (Bamberg); erwähnt keine graphematischen Types | nein |
| `Hinkelmanns-Zeppezauer-Wachauer-2023-MHDBDB-Projektbericht.pdf` | Hinkelmanns & Zeppezauer-Wachauer 2023 | MHDBDB, Herkunft der Typlisten | offen | 5 | gedruckt S. 179 bis 181; Kernstelle S. 180 (PDF-Seite 4); KUPS, CC BY 3.0 | nein |
| `Henrich-Hinrichs-2010-GernEdiT.pdf` | Henrich & Hinrichs 2010 | WSD Deutsch, Annotationswerkzeug | offen | 8 | LREC 2010, gedruckt S. 2228 bis 2235 | nein |
| `Mambrini-Passarotti-2023-LiLa.pdf` | Mambrini & Passarotti 2023 | Linked Data, Latein | offen | 5 | JOHD 9(1), Artikel 28 | nein |
| `Scholger-Bleier-2026-ChatGPT-RIDE.pdf` | Scholger & Bleier 2026 | LLM und digitale Editionen | offen | 32 | RIDE 19, Rezension der Ressource ChatGPT | nein |
| `Telljohann-etal-2017-TueBa-DZ-Stylebook.pdf` | Telljohann et al. 2017 | Baumbank Deutsch, Richtlinien | offen | 166 | Stylebook, Juli 2017 | nein |
| `Tittel-Chiarcos-2018-DEAF-LOD.pdf` | Tittel & Chiarcos 2018 | Linked Data, historische Lexikographie | offen | 10 | Venue laut `BESCHAFFUNG.md` widersprüchlich (LDL-2018 oder GLOBALEX), PDF ohne Seitenzahlen | nein |
| `Zeppezauer-Wachauer-2022-Fuenfzig-Jahre-MHDBDB.pdf` | Zeppezauer-Wachauer 2022 | MHDBDB, Geschichte, Graphdaten | offen | 27 | BmE Themenheft 12, S. 161 bis 186 | nein |

**In der Literaturliste, aber ohne PDF:** Roe 2025 (*How to Use Generative AI in Educational
Research*), Abualhaija 2016 (*D-Bees*), Tischler 2010 (*Word sense disambiguation, Einsatz in der
Medizin*), Yedurkar et al. 2026, Akerkar 2026.

**Nachgetragen am 2026-10-23:** Hinkelmanns & Zeppezauer-Wachauer 2023 (Herkunft der
Typlisten, `knowledge/data.md` Abschnitt 3; nicht dasselbe wie Hinkelmanns 2019) liegt jetzt
als PDF vor. Lesk 1986 fehlt weiterhin (ACM lieferte nur eine HTML-Sperrseite).
