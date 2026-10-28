# Strutz 2026: Mehrdimensionaler Evaluationsrahmen für LLM-gestützte TEI-Kodierung

**Datei:** `pdf/Strutz-2026-LLM-TEI-Evaluation.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, Volltext (20 Seiten) an Textebene gelesen, Formeln S. 7 an der Textebene, Abb. 3 bis 6 (S. 13 bis 15, 17) am Seitenbild geprüft; DOI über Crossref und Verlagsseite aufgelöst, Begutachtung an den Einreichungsrichtlinien der Zeitschrift geprüft, Datensatz auf Zenodo abgerufen. Keine Markierungen von Julia im PDF.

**Seitenzählung:** Die gedruckten Seitenzahlen (pp. 1 bis 20) stimmen mit den PDF-Seiten überein; zitiert wird „S. n".

## Bibliografie

- **Vollständig:** Strutz, Sabrina, 2026. A Multi-Dimensional Evaluation Framework for Assessing LLM Performance in TEI Encoding. *Journal of Open Humanities Data* 12(1), Artikel 39, S. 1 bis 20.
- **DOI/URL:** https://doi.org/10.5334/johd.484, löst auf openhumanitiesdata.metajnl.com auf. ✔ Crossref: Band 12, Artikelnummer 39, Ubiquity Press, „published-print" 2026-03-02; kein Heft, keine Relation, kein „update-to" oder „updated-by". Verlagsseite: Volume 12, Issue 1, eingereicht 18.11.2025, angenommen 19.01.2026, veröffentlicht 02.03.2026 (so auch S. 20); kein Hinweis auf Korrektur, Erratum oder Rückzug (beides am 2026-10-28 abgerufen).
- **Art:** begutachteter Zeitschriftenartikel, Artikeltyp „Discussion Paper" in der Kollektion „Benchmarking in Digital Humanities" (S. 1; Verlagsseite). Begutachtung ✔: Die Einreichungsrichtlinien von JOHD sagen „Discussion Papers are peer-reviewed and intended to be longer narratives (3,000-5,000 words)"; S. 20 nennt JOHD „a peer-reviewed open access journal". Eine Angabe zum Verfahren für diesen Artikel (Gutachter:innen, Editor) gibt es weder im PDF noch auf der Artikelseite. Lizenz CC BY 4.0 (S. 20).
- **Sprache:** Englisch
- **Abgleich:** `references.txt` (`strutz2026multidimensional`) und `literatur/README.md` stimmen mit Crossref überein; Heft 1 fehlt in beiden, ist aber auch in Crossref nicht eingetragen.

## Worum es geht

Die Arbeit fragt, wie sich LLM-erzeugte TEI-Kodierung systematisch und skalierbar bewerten lässt, weil NLP-Metriken wie F1 gegen ein einziges Gold die hierarchische Struktur von XML und die zulässige Vielfalt editorischer Kodierungen nicht erfassen (S. 1 bis 3). Sie zerlegt TEI-Kodierung in acht Aufgabendimensionen (0 bis 7) und entwickelt für die ersten fünf je eine Prüfung: Wohlgeformtheit, Texttreue, Schemakonformität, Strukturtreue und semantische Inhaltsgenauigkeit, zusammengeführt in einem gestuften Gesamtwert (S. 4 bis 7). Erprobt wird der Rahmen an 100 Briefen der Hammer-Purgstall-Korrespondenz mit vier Modellen (GPT-5-mini, Claude Sonnet 4.5, Qwen3-14B, OLMo2-32B), nach einer Prompt-Auswahl an 10 Briefen (S. 9 bis 10). Die kommerziellen Modelle erreichen Gesamtwerte über 92 %, doch auch Werte über 90 % verlangen nach Aussage der Autorin noch erhebliche Nacharbeit; LLMs seien noch keine verlässlichen autonomen Kodierer (S. 16, 18).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Traditionelle NLP-Metriken sind für einzelne Aspekte nützlich, „appear insufficient" für eine ganzheitliche Bewertung von TEI-Kodierung. | S. 1 (Abstract) | These der Arbeit |
| LLM-Kodierungen zeigen problematisches Verhalten: Textänderung (Normalisierung historischer Schreibung, Einfügen plausibler, aber erfundener Texte), Hang zu modernen Sprachkonventionen, inkonsistente Kodierentscheidungen. | S. 1, S. 2 (Abschnitt 1.1) | Befund aus früheren Experimenten, referiert (Scholger et al. 2024; Strutz 2025 u. a.) |
| Bisherige Experimente werten mit selbstgebauten Erfolgsquoten aus oder beschränken sich auf Teilaufgaben wie NER, bei denen ein einzelner F1-Wert genügt. | S. 2 (Abschnitt 1.1) | referiert (De Cristofaro & Zilio 2025; Pagel et al. 2024; Rastinger 2024) |
| Drei Gründe, warum TEI-Bewertung anders ist: (1) ein Syntaxfehler kann ein ganzes Dokument unbrauchbar machen, Wohlgeformtheit garantiert aber keine semantische Angemessenheit; (2) die Richtlinien erlauben mehrere gültige Kodierungen desselben Phänomens (`<persName>`, `<name type="person">`, `<rs type="person">`); (3) historische Texte bringen nicht standardisierte Orthografie, zeittypischen Wortschatz und Sprachwechsel. | S. 2 bis 3 (Abschnitt 1.2) | Argument, teils referiert (Cummings 2019; McGillivray et al. 2020) |
| NLP-Evaluation behandelt Gold als „singular ground truth" und setzt flache Annotationsstrukturen voraus; Editionsrezension (RIDE) setzt auf qualitatives Expertenurteil, ist aber nicht skalierbar. | S. 3 (Abschnitt 1.2) | referiert (Chang et al. 2023; Guo et al. 2023; Henny 2018; Sahle 2014; Dobson 2020) |
| Aufgabentaxonomie mit acht Dimensionen: 0 Formatumwandlung, 1 Quellentreue, 2 Schemaanwendung, 3 Strukturauszeichnung, 4 semantische Auszeichnung, 5 kontextuelle Anreicherung, 6 Metadaten, 7 Sammlungsverwaltung. | S. 4, Tab. 1 | eigener Vorschlag |
| Prüfweise passend zur Aufgabe: D0 bis D2 automatisch und referenzfrei, D3 bis D4 mit Gold, D5 bis D6 Expertenprüfung, D7 automatische Statistik; behandelt werden nur D0 bis D4. | S. 4 (Abschnitt 2.2) | eigener Vorschlag |
| D0: Wohlgeformtheit, binär bestanden/nicht bestanden, mit Fehlerkategorien (per Formatierwerkzeug korrigierbar oder Handarbeit). | S. 4 bis 5 (2.2.1) | Methode |
| D1: Quellentreue über Ähnlichkeitsquote der normalisierten Klartexte plus zeichengenauem Diff (Ersetzung, Einfügung, Löschung); auch 98 bis 99 % Ähnlichkeit können kritische Änderungen verdecken. | S. 5 (2.2.2) | Methode und Einschränkung |
| D2: Schemavalidierung (TEI P5 und/oder Projektschema), binär; nötige, aber nicht hinreichende Bedingung. | S. 5 (2.2.3) | Methode |
| D3: Strukturtreue über längste gemeinsame Teilfolge (LCS) der Elementfolgen; XMLDiff und Baum-Editierdistanz verworfen, weil sie verschobene Elementgrenzen doppelt bestrafen, auch bei vertretbaren editorischen Entscheidungen. | S. 5 (2.2.4) | Methode mit Begründung |
| D4: Inhalt pro Elementtyp, vier Treffertypen (exakt, Über-Einschluss, Unter-Einschluss, kein Treffer); Teiltreffer („practical matches") gewichtet mit 0,8, wenn D1 den Text als erhalten bestätigt (wohl Grenzfehler), sonst 0,6 (möglicherweise Halluzination). Substring-Vergleich erkennt keine inhaltlich falsche Zuordnung; dafür braucht es menschliche Prüfung. | S. 6 (2.2.5) | Methode und Einschränkung |
| Gesamtwert gestuft: Stufe 0 D0 als Tor (ungültig, kein Wert); Stufe 1 Kernwert = (D1 + D3 + D4 angepasst) / 3; Stufe 2 Faktor 1,0 bei Schemakonformität, 0,75 sonst; Gesamt = min(100, Kernwert × Faktor). Gleichgewichtung als „principled starting point" ohne empirische Begründung. | S. 6 bis 7 (2.2.6), Abb. 1 (S. 7) | eigener Vorschlag |
| Abhängigkeiten zwischen Dimensionen: D0-Fehler verdecken D2; eine Textänderung senkt D1 und D4 zugleich; fehlende Elemente zählen in D3 und D4 doppelt; Grenzvarianten werden in D3 und D4 bestraft, verschobene Verschachtelung nur in D3. Offene Frage, ob man das hinnimmt, eine Dimension streicht oder umgewichtet. | S. 12 (Abschnitt 4.1) | eigener Befund |
| Kommerzielle Modelle liefern bei etwa 30 % der Briefe exakt das Gold, bei etwa 40 % 91 bis 99 %; auch Werte über 90 % können erhebliche Nacharbeit verlangen. | S. 16 (4.2); Abb. 6 (S. 17) | eigenes Ergebnis |
| Fehlerqualität zählt, nicht nur Fehlerrate: Claudes niedrigere Texttreue beruht auf systematischen, per Suchen und Ersetzen behebbaren Fehlern (Apostrophe, unmaskierte `&`); GPT und Qwen machen seltene, aber verstreute Änderungen, die Einzelprüfung verlangen. | S. 12, S. 16 (4.1, 4.2) | eigenes Ergebnis |
| Vor allem D3 und D4 zeigen Schwierigkeiten, die quantitative Metriken allein nicht vollständig beschreiben; dort braucht es gezielte menschliche Prüfung, um legitime Entscheidungen von systematischen Fehlern zu trennen. | S. 16 (4.2) | Schlussfolgerung |
| Gold von nur einer Kodiererin pro Brief; Inter-Annotator-Agreement fehlt als Vergleichsrahmen dafür, welche Leistung menschlicher Streuung entspricht. Auch Menschen produzieren ohne Validierung schemawidriges Markup. | S. 16 bis 18 (4.3) | Einschränkung der Autorin |
| Keine wiederholten Läufe: Starke Zufallsvariation kann scheinbare Verbesserungen und Rangfolgen erklären. | S. 18 (4.3) | Einschränkung der Autorin |
| LLMs erzeugen mit Few-shot-Beispielen wohlgeformtes XML und wenden Schemaregeln sehr genau an; Quellentreue, Strukturdeutung und semantische Genauigkeit schwanken; LLMs sind „not yet reliable as autonomous encoders". | S. 18 (4.4) | Schlussfolgerung |
| Künftig: menschliche Benchmarks zur Einordnung, Auswertung nach systematischer Nachbearbeitung, Umweltkosten gegen Arbeitsersparnis abwägen, Attribute einbeziehen. | S. 18 (4.4) | Ausblick |

## Daten, Methode, Zahlen

- **Korpus:** Hammer-Purgstall-Korrespondenz (1790 bis 1850), über 8.500 Dokumente; aus 8.692 Katalogeinträgen 2.984 bearbeitbare Briefe; geschichtete Stichprobe von 100 Briefen nach Sprache, Schreiber:in und Länge; Sprachen Deutsch (vorwiegend), Englisch, Französisch, Italienisch mit Einsprengseln aus Latein, Griechisch und Arabisch (S. 9). Eingabe: von editorischen Eingriffen und Fußnoten bereinigte Klartexte (S. 9).
- **Gold:** 100 von Hand kodierte TEI-Dateien nach TEI-Briefrichtlinien und Projektschema (S. 9); Datensatzautorinnen Strutz und Alexandra Wagner (S. 8); eine Kodiererin pro Datei (S. 16, 18), keine Übereinstimmungsmessung.
- **Ablauf:** Prompt-Auswahl an 10 Briefen mit fünf Konfigurationen (einfache oder ausführliche Regeln, 0 bis 5 Beispielpaare), dann Bewertung an 100 Briefen (S. 9 bis 10). Ob die 10 Briefe in den 100 enthalten sind und woher die Few-shot-Beispiele stammen, sagt der Text nicht. Absichtlich erschwerte Aufgabe: `<salute>` innerhalb von `<p>` erlaubt (S. 10).
- **Modelle:** GPT-5-mini, Claude Sonnet 4.5, Qwen3-14B-Q6 (quantisiert), OLMo2-32B-instruct-Q4 (quantisiert), lokale Modelle auf einer GPU mit 24 GB (S. 10). Modellversionen und Konfiguration nur im Zenodo-Datensatz (S. 10, Anm. 14). Laut Abb. 6 (S. 17, am Bild geprüft): `claude-sonnet-4-5-20250929` (ausführlich + 5-shot, Temperatur 0,3, ca. 3,07 USD), `gpt-5-mini-2025-08-07` (ausführlich + 5-shot, 0,3, ca. 0,56 USD), `olmo2-32B-instruct-Q4` (ausführlich + 2-shot, 0,6), `qwen3-14B-Q6` ohne Thinking (kurz + 5-shot, 0,7). Die Temperaturen stehen nur in den Abbildungen, nicht im Text.
- **10-Brief-Auswahl (Abb. 5, S. 15, am Bild geprüft):** Claude mit ausführlichen Regeln und 5-shot erreicht 94,0 (Text S. 12), bei D3 97,6 gegenüber GPTs bestem 90,3 (Abb. 4, S. 14), also etwa 7 Punkte. Qwen: 8 bis 10 schemagültige Briefe mit Beispielen, 5 und 3 ohne (Abb. 3, S. 13; Text S. 12). Starke Prompt-Abhängigkeit: Claude D4 71,9 (ausführlich, 0-shot) gegenüber 42,4 (kurz, 0-shot) (Abb. 5).
- **100 Briefe (Abb. 6, S. 17, am Bild geprüft), Claude / GPT / OLMo / Qwen:**
  - D0 wohlgeformt (Dateien): 99 / 100 / 75 / 99
  - D2 projektgültig: 99 / 99 / 42 / 91
  - D1 Text unverändert: 48 / 82 / 0 / 73
  - D3 Struktur wie Gold: 76 / 37 / 0 / 31
  - D1 Ähnlichkeit (Mittel, %): 99,5 / 99,9 / 76,2 / 99,8
  - D3 Strukturähnlichkeit: 95,9 / 91,8 / 44,2 / 86,0
  - D4 angepasster Semantikwert: 81,0 / 89,6 / 46,0 / 81,1
  - Gesamtwert: 92,4 / 93,6 / 54,9 / 87,5 (so auch Text S. 16)
  - exakt wie Gold: 28 / 32 / 0 / 26; 91 bis 99 %: 41 / 43 / 0 / 23; nicht verarbeitet: 1 / 0 / 25 / 1
- **Software:** Python, lxml, Jing; Berichte als JSON und Excel; MIT-Lizenz, https://github.com/strubrina/tei-evaluation (S. 8).
- **Datensatz:** Zenodo 10.5281/zenodo.17643901 (S. 8). Abweichung: Der Artikel nennt CC BY 4.0 (S. 9) und als Urheberinnen Strutz und Wagner (S. 8); der Zenodo-Datensatz nennt am 2026-10-28 CC BY-NC 4.0 und nur Strutz (zuletzt geändert 2026-10-08).

## Wörtliche Stellen

> „While traditional Natural Language Processing (NLP) evaluation metrics are valuable for specific aspects, they appear insufficient for a holistic assessment of TEI encoding." (S. 1)

> „even high similarity scores (98-99%) may mask critical alterations" (S. 5)

> „these quantitative successes require qualification, as even scores exceeding 90% can demand substantial post-processing for reference quality." (S. 16)

> „Inter-annotator agreement baselines could establish expected human variation ranges to contextualise LLM performance" (S. 16)

> „Substantial stochastic variation means apparent improvements might reflect coincidental generation rather than genuine optimisation" (S. 18)

## Bezug zur Dissertation

- **Protokoll 9.2, Bewertungsregeln (Formatfehler):** Strutz setzt Wohlgeformtheit als Tor vor jede inhaltliche Bewertung (D0, S. 4 bis 6) und trennt behebbare von nicht behebbaren Formfehlern (S. 5, 16). Das Protokoll regelt Abstinenz bei Ausweichlabels, aber nicht, was mit einer unparsbaren LLM-Antwort, einer Sense-ID außerhalb des Menüs oder zwei IDs bei `SENSE` geschieht; `PROMPT-LOG.md` sieht dafür nur das Feld `label` vor. Vorschlag für Freeze 2: Formfehler als eigene Kategorie zählen und berichten, im primären Vergleich aber als falsch werten. Ein Ausschluss wie bei Strutz („INVALID", kein Wert) würde den gepaarten McNemar-Vergleich mit MFS brechen, weil MFS nie einen Formfehler hat (Folgerung, nicht aus der Quelle).
- **Protokoll 9.2, Teilkorrektheit (A14):** Die Teiltreffer mit festen Gewichten 0,8 und 0,6 (S. 6 bis 7) sind die TEI-Entsprechung zur Teilwertung bei `MEHRERE`. Strutz begründet weder diese Gewichte noch die Gleichgewichtung empirisch (S. 7) und nennt selbst Doppelzählungen (S. 12). Das stützt die Wahl des Protokolls, Teilwertung über einen etablierten Koeffizienten (Dice nach Henrich 2015 und Véronis 1998) und nur als Sensitivität zu berichten, statt ad hoc gewichtete Gesamtwerte zu bilden.
- **Protokoll 9.2, getrennte Maße statt Gesamtwert:** Die Diagnose kommt bei Strutz aus den einzelnen Dimensionen, nicht aus dem Gesamtwert (S. 12, 16). Für die WSD-Auswertung spricht das dafür, Genauigkeit, Abstinenzverhalten bei Ausweichlabels, Formfehler und Macro-Genauigkeit nach Sense nebeneinander zu berichten und nicht zu verrechnen (Folgerung). Strutz verwendet Macro-F1 in D4, damit seltene Klassen gleich zählen (S. 6, Anm. 7); das entspricht der Macro-Genauigkeit in 9.2.
- **Protokoll 9.1 und A5 (Gold mit gemessener Übereinstimmung):** Strutz' Gold stammt von einer Kodiererin pro Datei, und sie nennt fehlendes IAA als Grenze und als nötigen Vergleichsrahmen (S. 16, 18). Das ist ein weiteres Beispiel für die in `LITERATUR-IAA.md` beschriebene Lücke und stützt den Vergleich „LLM gegen Menschen" mit der menschlichen IAA als Obergrenze (Protokoll 9.2, Calderon et al. 2025).
- **Protokoll 4.10 und `PROMPT-LOG.md` (Läufe, Versionen):** Fehlende Wiederholungsläufe nennt Strutz als Grenze, die Rangfolgen und Prompt-Empfehlungen unsicher macht (S. 18). Das stützt die Festlegung der Läufe pro Item in Freeze 2. Modell-IDs mit Datum stehen bei ihr nur in einer Abbildung und im Datensatz, Temperaturen nur in Abbildungen (S. 10, 17): ein Grund, diese Angaben im eigenen Artikel im Text zu nennen.
- **Protokoll 7 (Pilot) und Freeze 2 (Prompt):** Strutz wählt Prompt und Konfiguration an 10 Briefen, ohne zu sagen, ob diese in der Bewertungsstichprobe liegen (S. 9 bis 10). Für die Dissertation folgt daraus: Prompt-Entwicklung und Few-shot-Beispiele nur aus dem Pilot-Pool, der laut Protokoll 4.2 lemmadisjunkt ist, und das im Artikel ausdrücklich sagen (Folgerung).
- **Quellentreue und Normalisierung:** D1 misst die Neigung, historische Schreibung zu modernisieren (S. 2, 5). In der WSD ändert das LLM den Text nicht, aber dieselbe Neigung kann als neuhochdeutsche Lesart mittelhochdeutscher Wörter auftreten. Das ist eine Hypothese, kein Befund der Arbeit; die Fehlerkategorien der Adjudikation (Protokoll 7, Schritt 6) könnten einen Code für LLM-Fehler dieser Art erhalten, falls das gewünscht ist.
- **Verhältnis zu Galka & Vogeler 2026 und Scholger & Bleier 2026:** Alle drei kommen aus dem Grazer Umfeld. Galka & Vogeler fordern die Prüfung auf Tag-Integrität und Texterhalt; Strutz formalisiert genau das als D0 und D1. Scholger & Bleier zitieren diese Arbeit als „Strutz forthcoming" (Abs. 20).

## Grenzen und Einwände

- Ein Korpus, eine Textsorte (Briefe), eine Teilaufgabe (Briefstruktur ohne Attribute, S. 18); 100 Briefe, ein Lauf pro Brief und Modell (S. 18).
- Gold von einer Kodiererin pro Datei; die Gewichte (0,8, 0,6, 0,75, Drittelung) sind gesetzt, nicht validiert (S. 7, 18). Ob der Gesamtwert mit menschlichen Qualitätsurteilen zusammenhängt, ist offen (S. 7, 16).
- Unterschiedliche Temperaturen der Modelle (0,3 bis 0,7, nur in Abb. 6) erschweren den Modellvergleich; der Text begründet sie nicht.
- Kleine Unstimmigkeiten: S. 3 nennt „GPT-5" unter den bewerteten Modellen, sonst ist es durchgehend GPT-5-mini (S. 1, 10, Abb. 4 und 6); S. 10 nennt GPT-5 ausdrücklich als nicht gewähltes Flaggschiff. Datensatzlizenz und -urheberschaft weichen von Zenodo ab (siehe oben).
- Übertragbarkeit: TEI-Kodierung hat einen offenen, strukturierten Ausgaberaum; WSD gegen ein Menü ist eine geschlossene Klassifikation, bei der Genauigkeit gegen Gold weit besser passt als bei TEI. Übertragbar sind vor allem die Trennung von Form- und Inhaltsfehlern, die Kritik an ungeprüften Gewichtungen und die Forderungen nach IAA und Wiederholungsläufen; die LCS- und Substring-Metriken selbst sind es nicht.

## Weiterführend

- Strutz 2025, DH 2025, Vortrag „Towards an Evaluation Framework …", Zenodo 10.5281/zenodo.16364518 (S. 20; Vorstufe dieser Arbeit, auf Zenodo nur Strutz als Urheberin).
- De Cristofaro & Zilio 2025, LLM-gestützte TEI-Kodierung unveröffentlichter Korrespondenz, Quaderni di Umanistica Digitale (S. 2, 19).
- Chang et al. 2023, Survey zur Evaluation von LLMs, arXiv:2307.03109 (S. 3, 19).
- Pagel, Pichler & Reiter 2024, Prompt-Brüchigkeit in den Computational Literary Studies (S. 2, 19): einschlägig für die Prompt-Abhängigkeit in Freeze 2.
- Gilardi, Alizadeh & Kubli 2023, PNAS, und Ding et al. 2023, ACL (S. 2, 19): LLMs als Annotatoren.
