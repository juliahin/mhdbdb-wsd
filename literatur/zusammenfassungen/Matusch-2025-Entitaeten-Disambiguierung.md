# Matusch 2025: Untersuchung von Methoden zur Erkennung und Disambiguierung von Entitäten in Texten

**Datei:** `pdf/Matusch-2025-Entitaeten-Disambiguierung.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->

**Stand:** 2026-10-29, ganze Arbeit an der rohen Textebene gelesen (PDF 1 bis 83); Tab. 4.2 bis 4.6 an den Seitenbildern geprüft (PDF 71 bis 73); Differenzen in Tab. 4.2 aus Tab. 4.3 bis 4.5 nachgerechnet. Repositoriumseintrag gesucht, nicht gefunden.

**Seitenzählung:** gedruckte Seite = PDF-Seite in der ganzen Arbeit (Kurzfassung S. 5, Tab. 4.6 S. 73). Zitiert wird deshalb nur eine Seitenzahl.

**Gewichtung:** Prio 3, Hintergrund. Die Grundlagenkapitel (Tokenisierung, Einbettungen, NER-Verfahren, S. 19 bis 39) sind gelesen, aber nicht nacherzählt; ausführlicher sind Entity Linking (S. 40 bis 50), die Experimente (S. 51 bis 59, 71 bis 73) und die Diskussion (S. 75 bis 76).

## Bibliografie

- **Vollständig:** Matusch, Felix, 2025. *Untersuchung von Methoden zur Erkennung und Disambiguierung von Entitäten in Texten.* Masterarbeit, FH JOANNEUM, Masterstudiengang „Data Science and Artificial Intelligence“, Jahrgang DAT 2023. Betreuer: DI Dr. Michael Hammer. Graz, 30.06.2025 (Titelblatt, PDF 1).
- **DOI/URL:** keine. Drei Websuchen am 2026-10-29 (Titel, Name mit Hochschule) fanden keinen Repositoriums- oder Katalogeintrag.
- **Art:** Abschlussarbeit (Masterarbeit), nicht separat begutachtet veröffentlicht.
- **Sprache:** Deutsch, Abstract zusätzlich Englisch (S. 6). Alle Daten sind englisch (S. 51, 56, 60).

## Worum es geht

Die Arbeit fragt, welche Methoden Entitäten in Texten erkennen (NER) und welche sie eindeutig einer Identität in einer Wissensbasis zuordnen (NED), und baut daraus eine Pipeline, die Personen, Orte und Organisationen in Zeitungsartikeln verlinkt und als Ko-Okkurrenz-Graph in Neo4j ablegt (S. 5, 17). Für NER werden ein Gazetteer, ein CRF und ein auf CoNLL-2003 feinabgestimmtes BERT verglichen (S. 52 bis 55); für NED fünf fertige Cross-Encoder, die fünf vorab per Bi-Encoder gewählte Wikidata-Kandidaten neu ordnen (S. 56 bis 59). Ergebnis: BERT ist bei NER meist am besten (Tab. 4.2, S. 71); bei NED erreichen ms-marco-electra-base und ms-marco-TinyBERT-L6 knapp 80 % Accuracy, und zwar fast gleich, ob der Cross-Encoder den Kontextabsatz sieht oder nicht (Tab. 4.6, S. 73). Eigene Annotation, Übereinstimmungsmessung und eine Evaluation der Pipeline auf den Zeitungsartikeln gibt es nicht (S. 17, 68).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Entity Linking besteht aus Erkennung von Erwähnungen, Kandidatenselektion und Disambiguierung; die Selektion des besten Kandidaten wird oft als Ranking-Problem behandelt. | S. 40 | referiert (Balog 2018) |
| Popularitätsprior P(e \| m): Anteil, mit dem eine Erwähnung m in Wikipedia auf Entität e verlinkt; ein Verfahren ohne Kontext. | S. 46 | referiert (Balog 2018; Medelyan, Witten & Milne 2008) |
| Popularitätsbasierte Metriken übergehen seltene, im Kontext richtige Entitäten („Popularitäts-Bias“), besonders große Systeme. | S. 46 | referiert (Shi et al. 2024) |
| Wikipedia ist wegen fehlender Annotationsregeln inkonsistent, manche Identitäten sind nicht eindeutig genug beschrieben. | S. 45 | referiert (Ling, Singh & Weld 2015) |
| Gold-Standard: von mehreren Menschen manuell annotiert; Silver-Standard: halb- bis ganz automatisch; Bronze: rein automatisch, ungeprüft. | S. 33 | ohne Quellenangabe |
| CoNLL-2003 wird „als Gold eingestuft, da dieser manuell annotiert worden ist“; eine Prüfung der Labels findet nicht statt. | S. 51 | eigene Festlegung |
| Der Gazetteer wird aus Tokens und Tags desselben Buckets gebaut, auf dem er evaluiert wird; sein guter Wert kommt daher, „dass dieser alle Entitäten tatsächlich kennt“. | S. 53, 71 | eigenes Design, eigene Einschränkung |
| BERT ist in drei von vier Buckets am besten, im vierten (BT0) 0,26 Punkte hinter dem Gazetteer. | Tab. 4.2, S. 71 | eigenes Ergebnis |
| Als „Benchmark“ für einen wesentlichen Unterschied gelten 5 Punkte Abstand zum besten Modell; ein statistischer Test wird nicht gerechnet. | S. 55 | eigene Festlegung |
| Für NED werden nur die Einträge verwendet, deren fünf Kandidaten die richtige Identität enthalten; der Bi-Encoder erreicht dafür eine Top-5-Accuracy von 90,46 %. | S. 58, 73 | eigenes Design und Ergebnis |
| Zwei Eingabeformate: A1 „(Does the entity <name> fit the description?, <description>)“, A2 „(<text>, <description>)“, also mit dem Absatz, in dem die Entität steht. Die besten Modelle unterscheiden sich zwischen A1 und A2 kaum; nur die MiniLM-Modelle gewinnen mit Kontext rund 5 Punkte. | S. 59, 73, Tab. 4.6 | eigenes Ergebnis |
| NIL (Entität ohne Eintrag in der Wissensbasis) ist in den NED-Experimenten nicht berücksichtigt; in der Pipeline entscheidet ein Schwellenwert von 0,5 auf dem sigmoid-transformierten Ranking-Score. | S. 64 bis 65, 75 | eigene Einschränkung bzw. Festlegung |
| Für NED war ein geeigneter Datensatz schwerer zu finden als erwartet, weil die vorhandenen Datensätze jeweils nur einen Ansatz erlauben; deshalb der Fokus auf die Disambiguierung der Kandidaten. | S. 75 | eigene Einschätzung |
| Ausblick: NED profitiert von besserem Kontext, der sich durch NER und Fact-Extraction verdichten ließe; bessere Kandidatengenerierung verbessert die Disambiguierung. | S. 76 | Ausblick |

## Daten, Methode, Zahlen

**Daten:** Englisch, Gegenwartssprache, keine historischen Texte.

- **NER:** englischer Teil von CoNLL-2003 (Reuters), Validierungs- und Test-Split, Entitätsklassen PER, ORG, LOC, MISC im IOB-Schema; jeder Split am Median der Entitätsdichte (0,125) in zwei Buckets geteilt, also BV0, BV1, BT0, BT1 (S. 51 bis 52, Tab. 4.1, S. 71). Wie viele Sätze oder Tokens ein Bucket hat, steht nicht in der Arbeit.
- **NED:** WikiData Disambig with Descriptions (WIDDD, nach Cetoli et al. 2019) über die Hugging-Face-Bibliothek `datasets` 3.5.0; je Eintrag Erwähnung, Textabsatz, richtige und falsche Wikidata-ID mit Kurzbeschreibung; die falsche wird verworfen (S. 56, Tab. 3.2, 3.3). Die Wissensbasis entsteht aus den deduplizierten richtigen Identitäten im Format `<name>:<description>`, z. B. „brazil:country in South America“ (S. 57, Tab. 3.4, S. 58). Wie viele Einträge in die Auswertung eingehen, nennt die Arbeit nicht (Volltext durchsucht).
- **Pipeline:** BBC-News-Datensatz von Kaggle, in einer ZODB abgelegt, das Datum je Artikel zufällig gesetzt (S. 60 bis 61); MISC-Entitäten werden verworfen (S. 62).

**Inventar, wie es dem Modell gezeigt wird:** Der Bi-Encoder all-MiniLM-L6-v2 (384 Dimensionen) wählt per Kosinus-Ähnlichkeit zwischen Erwähnung und `<name>:<description>` fünf Kandidaten aus einer Chroma-Datenbank (S. 57 bis 58, 64). Der Cross-Encoder bewertet dann jedes Paar aus Frage und Kandidatenbeschreibung einzeln; der Kandidat mit dem höchsten Score gewinnt (S. 64 bis 65, Algorithmus 4). Ob `<name>` in A1 die Erwähnung oder der Name des Kandidaten ist, bleibt für das Experiment offen („das Merkmal aus dem Datensatz, das den Namen der Identität beinhaltet“, S. 59); in der Pipeline ist es der von NER erkannte Entitätswert (S. 64).

**Modelle:** NER: Gazetteer, CRF (sklearn-crfsuite, c1 = c2 = 0,1, 100 Iterationen, ohne Hyperparametersuche), `dslim/bert-base-NER` (S. 53 bis 54). NED: ms-marco-MiniLM-L6-v2, ms-marco-MiniLM-L12-v2, ms-marco-TinyBERT-L6, ms-marco-electra-base, gte-reranker-modernbert-base (Tab. 3.5, S. 59). Kein generatives LLM; „LLM“ steht in der Arbeit auch für TinyBERT, Electra und MiniLM (S. 50).

**Ergebnisse NER** (gewichteter F1 in %, Tab. 4.3 bis 4.5, S. 72, am Bild geprüft): BERT 89,15 / 92,37 / 93,36 / 96,06 (BT0, BT1, BV0, BV1); CRF 73,82 / 81,83 / 84,45 / 88,95; Gazetteer 89,41 / 90,39 / 89,38 / 88,40. Die Abstände in Tab. 4.2 (S. 71) sind Prozentpunkte zum jeweils besten Modell und lassen sich daraus exakt nachrechnen.

**Ergebnisse NED** (Accuracy in %, A1 / A2, Tab. 4.6, S. 73, am Bild geprüft): MiniLM-L6 57,11 / 62,12; MiniLM-L12 57,24 / 62,70; TinyBERT-L6 79,58 / 79,32; electra-base 79,60 / 79,42; gte-reranker 77,14 / 77,42. Zufallsniveau bei fünf Kandidaten 20 % (eigene Angabe; die Arbeit nennt keines). Weil nur Einträge mit der richtigen Identität unter den fünf Kandidaten eingehen, wäre die Genauigkeit über alle Einträge höchstens 0,9046 × 0,796 ≈ 72 % (eigene Rechnung, nicht in der Arbeit).

**Gold, Annotator:innen, Übereinstimmung:** keine eigene Annotation. Gold sind die vorhandenen Labels von CoNLL-2003 und WIDDD (S. 51, 56). „Manuelle Evaluierung der Ergebnisse des EL“ ist ausdrücklich ein Nicht-Ziel (S. 17); die Benutzeroberfläche wird nicht evaluiert (S. 68). Cohen's κ kommt nur im referierten Grundlagenteil vor (Alshammari & Alanazi 2021: 95,14 %, S. 32).

**Statistik:** Punktwerte ohne Intervalle, ohne Test, ohne Baseline für NED. „Signifikant“ heißt in der Arbeit „mehr als 5 Punkte Abstand“ (S. 55, 71, 73).

## Wörtliche Stellen

> „Der Erfolg des Gazetteers ist darauf zurückzuführen, dass dieser alle Entitäten tatsächlich kennt, was in einer nicht-experimentellen Umgebung sehr selten der Fall sein wird.“ (S. 71)

> „Das Resultat wird eingefroren und abgespeichert, dabei werden nur die Einträge genutzt, die in den fünf Kandidaten die korrekte Identität enthalten.“ (S. 58)

> „Ein wichtiger Aspekt beim EL ist die Entscheidung, wann eine Entität keine Identität besitzt und somit nicht mit der Wissensbasis verknüpft werden sollte. Dies ist in den Experimenten für NED nicht einbezogen.“ (S. 75)

## Bezug zur Dissertation

- **Protokoll 9.2 (Bewertungsregeln, Ausweichlabels):** Die NED-Accuracy gilt nur für Einträge, bei denen die richtige Identität unter den Kandidaten ist (S. 58), und NIL ist ausgeklammert (S. 75). Die berichteten knapp 80 % sagen deshalb nichts über die Fälle, in denen das Inventar nicht passt. Das stützt die Regel des Protokolls, `KEINE_PASST` und die anderen Ausweichstatus aus der Genauigkeit zu nehmen, aber ihren Anteil und das Verhalten des LLM dort gesondert zu berichten. Ohne diesen Bericht wäre ein Wert wie der von Matusch nicht mit einem Wert über alle Items vergleichbar.
- **Protokoll 9.2 (MFS-Baseline, Nicht-MFS-Items):** Der referierte Popularitätsprior P(e | m) (S. 46) ist das Gegenstück der MFS beim Entity Linking, und der referierte Popularitäts-Bias (Shi et al. 2024, S. 46) ist derselbe Einwand, auf den die Auswertung auf Nicht-MFS-Items antwortet. Die Arbeit selbst rechnet keine Baseline und kann ihre 80 % deshalb nicht einordnen; das ist ein weiteres Gegenbeispiel für den gepaarten Vergleich gegen MFS. Für die Primärliteratur Balog 2018 und Shi et al. 2024 zitieren, nicht Matusch.
- **Protokoll 4.10 (Freeze 2: Prompt, „ob das LLM dieselben Karten sieht“) und 5:** Die Kandidaten erscheinen als `<name>:<description>` mit Wikidata-Kurzbeschreibung, und das Eingabeformat ist eine Variable: Für die MiniLM-Modelle bringt der Kontextabsatz rund 5 Punkte, für die besten Modelle nichts (Tab. 4.6). Dass die stärksten Modelle ohne Kontext genauso gut sind, deutet darauf, dass sie aus Name und Beschreibung allein entscheiden (eigene Deutung; die Arbeit kommentiert es nicht). Für das Protokoll heißt das: Kartenformat und Kontextumfang in Freeze 2 festschreiben. Ob zusätzlich ein Lauf ohne Kontext (nur Lemma und Karten) als Kontrollbedingung sinnvoll wäre, um zu sehen, wie viel das LLM aus den Karten allein errät, wäre eine Entscheidung für Freeze 2 und nur am Pilot-Pool zu prüfen (Vorschlag, nicht aus der Arbeit).
- **`knowledge/data.md` B1 (Leckgefahr der Typlisten):** Der Gazetteer wird aus den Labels genau der Daten gebaut, auf denen er gemessen wird, und erreicht deshalb fast BERT-Niveau; die Arbeit benennt das selbst (S. 53, 71). Das ist ein handliches Beispiel dafür, warum `sense/@ana` weder in die Annotationsdatei noch in den LLM-Prompt darf: Ein Verfahren, das die Antwort schon kennt, sieht gut aus und misst nichts.
- **Protokoll 2 (Begriffe Gold und Silber):** Matusch definiert, ohne Quelle, Silber als halb- bis ganz automatisch annotiert (S. 33). Das Protokoll nennt Silber eine menschliche, aber undokumentierte Annotation (für monoseme Lemmata ist sie laut `knowledge/data.md` B2 automatisch vergeben, die Auswertung betrifft aber nur polyseme). Der Unterschied ist sachlich begründet; ein Satz im Datasheet, dass „Silber“ hier nicht „automatisch“ meint, würde Leser:innen aus der NER- und EL-Literatur vor einer Verwechslung bewahren. Als Beleg für den üblichen Sprachgebrauch taugt Matusch nicht (keine Quelle).
- **Protokoll 7 und A1 (Gold aus Doppelannotation):** Gold ist hier, was ein vorhandener Datensatz als Gold ausgibt (S. 51); weder Übereinstimmung noch Fehlerquote werden geprüft. Kein Beleg für, aber ein typisches Beispiel gegen das Vorgehen, das A1 ablöst.
- **Julias Notiz (Zeitungstexte als Gegenfolie):** Die Arbeit liefert das Material für den Kontrast, zieht ihn aber nicht selbst: Jede Komponente ist fertig verfügbar (NER-Modell auf CoNLL-2003, Wissensbasis aus Wikidata, auf MS MARCO trainierte Reranker; S. 54, 57, 59), und eigenes Training, eigene Wissensbasis und eigene Annotation sind ausdrücklich Nicht-Ziele (S. 17). Für Mittelhochdeutsch fehlt jede dieser Ressourcen; das wäre die Aussage, die Julia daraus machen kann.

## Grenzen und Einwände

- Masterarbeit, nicht begutachtet veröffentlicht; Englisch, Gegenwartssprache, Nachrichtentexte; keine generativen LLMs, kein Prompting im engeren Sinn. Für ein onomasiologisches Inventar und historische Sprache sagt die Arbeit nichts.
- NED ist hier Auswahl unter fünf Kandidaten mit Kurzbeschreibung, also eine engere Aufgabe als WSD gegen ein ganzes Lemma-Inventar; Kandidaten mit ähnlichem Namen kommen aus einem vorgeschalteten Retrieval, nicht aus einem festen Inventar.
- Keine eigene Annotation, keine Übereinstimmung, keine Baseline für NED, keine Intervalle; die Pipeline auf BBC-News wird gar nicht evaluiert.
- Umfang der NED-Auswertung nicht angegeben; ob `<name>` in A1 die Erwähnung oder der Kandidatenname ist, bleibt unklar (S. 59 gegen S. 64).
- **Interne Widersprüche, an Textebene bzw. Seitenbild bestätigt:**
  - Das CRF überschreite den 5-Punkte-Abstand „in zwei von vier Fällen“ (S. 71); Tab. 4.2 zeigt −15,59, −10,54, −8,91 und −7,11, also alle vier. Der Gazetteer liegt in BV1 mit −7,66 ebenfalls darüber; der Text erwähnt das nicht.
  - „Insgesamt werden sechs Modelle gegenübergestellt“ (S. 73); Tab. 3.5 und 4.6 enthalten fünf.
  - NIL-Schwelle: Nach S. 64 bis 65 und Algorithmus 4 werden Entitäten mit Score ≤ 0,5 nicht verknüpft; nach S. 75 werden „die Entitäten, welche einen Schwellenwert der Sigmoid überschreiten, nicht verknüpft“.
  - Der NED-Datensatz heißt abwechselnd WIDDD, WIKDDD und WIKKD (S. 56 bis 58).
  - Die Forschungsfragen teilen EL in „Named Entity Recognition (NER) und Named Entity Recognition (NER)“ (S. 17); gemeint ist NER und NED.

## Julias Markierungen

Alle 16 Anmerkungen (15 Hervorhebungen, 1 Notiz) liegen auf der Kurzfassung (S. 5): EL, NER, NED, die verwendeten Methoden, Data Pipeline, Zeitungsartikel, Wissensgraph und Benutzeroberfläche sowie der Satz über die „sinnvolle Verwendung ungenutzter Ressourcen“ und die Kostenersparnis durch vortrainierte Modelle.

- **Aufgenommen:** Aufgabenzuschnitt (EL = NER + NED), Methoden, Datenquelle Zeitungsartikel, Pipeline mit Wissensgraph (Worum es geht, Daten); vortrainierte Modelle statt eigenem Training (Bezug, letzter Punkt).
- **Nur knapp:** Wissensgraph und Benutzeroberfläche; sie werden in der Arbeit nicht evaluiert (S. 68) und tragen nichts zur WSD-Evaluation bei.
- Eine Hervorhebung auf S. 5 hat keinen Text unter der Markierung.

## Julias Notizen im PDF

- S. 5, an der Kurzfassung: „gut um Disambiguierung in anderen Kontexten zu sehen, Zeitungstexte, da ist einfach viel Grundlage da - d.h. gut um sichtbar zu machen low-resource szenario“. Aufgegriffen im letzten Punkt unter „Bezug zur Dissertation“; die Arbeit selbst spricht nicht von einem Low-Resource-Szenario.

## Weiterführend

- Balog 2018, *Entity-Oriented Search*, Kapitel „Entity Linking“, S. 147 bis 188 (zitiert S. 40 bis 48): Primärquelle für die Gliederung des EL, Popularitätsprior und Kontextähnlichkeit; nicht geprüft.
- Shi et al. 2024, *Generative Multimodal Entity Linking* (zitiert S. 46): Popularitäts-Bias; im Literaturverzeichnis ohne Venue; nicht geprüft.
- Ling, Singh & Weld 2015, „Design Challenges for Entity Linking“, TACL 3, S. 315 bis 328 (zitiert S. 15, 45): Inkonsistenz von Wikipedia als Gold wegen fehlender Annotationsregeln; nicht geprüft.
- Cetoli et al. 2019, „A Neural Approach to Entity Linking on Wikidata“ (zitiert S. 56): Herkunft von WIDDD; nicht geprüft.
