# An et al. 2024: Make Your LLM Fully Utilize the Context

**Datei:** `pdf/An-etal-2024-LLM-Context.pdf` (nur lokal; 19 Seiten, arXiv 2404.16811v2 vom 26.04.2024, Kopfvermerk „Preprint.“)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganze Textebene gelesen, Tabellen 1 und 2 am Seitenbild geprüft. Priorität 3: bewusst knapp. Keine Markierungen im PDF (keine Anmerkungsebene).

Seitenzählung: gedruckte Seite = PDF-Seite (Seitenzahl unten mittig).

## Bibliografie

- **Vollständig (lokale Fassung):** An, Shengnan; Ma, Zexiong; Lin, Zeqi; Zheng, Nanning; Lou, Jian-Guang (2024). Make Your LLM Fully Utilize the Context. arXiv:2404.16811v2 [cs.CL]. Preprint.
- **Begutachtete Fassung:** An, Shengnan; Ma, Zexiong; Lin, Zeqi; Zheng, Nanning; Lou, Jian-Guang; **Chen, Weizhu** (2024). Make Your LLM Fully Utilize the Context. In: *Advances in Neural Information Processing Systems 37 (NeurIPS 2024)*, S. 62160 bis 62188. DOI 10.52202/079017-1986. Quelle: Crossref und Proceedings-Seite (proceedings.neurips.cc), am 2026-10-28 abgerufen; die DOI löst auf proceedings.com (Curran) auf. Die NeurIPS-Fassung hat einen sechsten Autor; sie ist nicht gelesen, Unterschiede im Inhalt sind nicht geprüft.
- **DOI/URL:** arXiv https://doi.org/10.48550/arXiv.2404.16811 (nur v1 und v2, keine Journal-Angabe auf arXiv); Code laut Paper github.com/microsoft/FILM (S. 1, nicht aufgerufen).
- **Art:** lokal Preprint; begutachtet erschienen als Konferenzbeitrag (NeurIPS 2024, Main Conference Track)
- **Sprache:** Englisch

## Worum es geht

Lange Kontextfenster werden von LLMs nicht gleichmäßig genutzt: Information in der Mitte geht verloren („lost-in-the-middle“, S. 1 bis 2). Die Autor:innen führen das auf eine Positionsverzerrung der allgemeinen Trainingsdaten zurück und trainieren Mistral-7B-Instruct-v0.2 mit synthetischen Frage-Antwort-Daten nach, deren Antwort an beliebiger Stelle eines 4K- bis 32K-Kontexts steht (IN2-Training, Modell FILM-7B, S. 2 bis 5). Gemessen wird mit drei eigenen Abfrageaufgaben (VAL Probing) und LongBench (S. 5 bis 9). FILM-7B nutzt alle Positionen gleichmäßiger und verbessert sich auf realen Langkontextaufgaben, ohne auf Kurzkontextaufgaben einzubüßen.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| LLMs verarbeiten lange Eingaben, nutzen Information in der Mitte aber schlechter als am Anfang und Ende. | S. 2, Abschnitt 1 | referiert (Liu et al. 2024; Xu et al. 2023) |
| Hypothese: Allgemeines Training legt eine Positionsverzerrung nahe, „important information is always located at the beginning and end of the context“; u. a. weil die Systemnachricht meist am Anfang steht. | S. 2 | Hypothese der Autor:innen |
| Nahezu perfekte Werte bei Needle-in-the-Haystack überschätzen die Langkontextfähigkeit: vertrauter Dokumentstil und „forward retrieval“, bei dem die Antwort direkt auf das Suchwort folgt. | S. 6, Abschnitt 3.1 | Argument der Autor:innen |
| Kontextstil und Abfragemuster tragen beide zur Schwierigkeit bei; LongAlign und InternLM2 zeigen trotz nahezu perfekter Needle-Werte Verluste in der Mitte. | S. 8 bis 9, Abschnitt 4.2 | eigenes Ergebnis |
| Mistral-7B-Instruct-v0.2 verliert in allen drei Aufgaben stark in mittleren Positionen; FILM-7B bleibt über die Positionen stabil (Abb. 4a). | S. 8 | eigenes Ergebnis |
| Auf realen Langkontextaufgaben verbessert sich FILM-7B gegenüber dem Ausgangsmodell (Durchschnitt 30,6 → 39,9), bleibt aber unter GPT-4-Turbo (44,7). | S. 7, Tab. 2 (am Seitenbild geprüft); S. 9 | eigenes Ergebnis |
| Kurzkontextaufgaben bleiben etwa gleich (MMLU 59,3 → 59,2). | S. 1; S. 9, Abb. 5 | eigenes Ergebnis |
| Sliding-Window-Attention schadet: Liegt die Information weiter entfernt als das Fenster, fällt die Leistung stark ab. | S. 9 bis 10, Abschnitt 4.3, Abb. 6 | eigenes Ergebnis |

## Daten, Methode, Zahlen

- **Trainingsdaten (S. 3 bis 4):** Rohtexte aus C4 (realnewslike), Fragen und Antworten von GPT-4-Turbo erzeugt; Segmente von 128 Tokens, Kontexte gleich verteilt zwischen 4K und 32K Tokens. Zusammensetzung: 1,1 Mio. Langkontextdaten für einzelne Segmente (ca. 63 %), 300.000 für die Verbindung mehrerer Segmente (ca. 17 %), 150.000 Kurzkontext-QA (ca. 9 %), 200.000 allgemeine Instruktionsdaten (ca. 11 %) (S. 4).
- **Kontamination (S. 16, Anhang A):** Rohtexte mit 10-Gramm-Überlappung zu irgendeinem Evaluationsbeispiel werden ausgeschlossen.
- **Training (S. 4 bis 5):** eine Epoche, ca. 14.000 Schritte, 16 Knoten mit je 8 A100 (80 GB), ca. 300 GPU-Tage.
- **VAL Probing (S. 6 bis 7):** drei Aufgaben (Dokument, Code, Datenbank) mit je ca. 3.000 Beispielen und Kontexten von ca. 32K Tokens; Abfragemuster bidirektional, rückwärts, vorwärts. Maße: Durchschnitt über alle Positionen und Differenz zwischen bestem und schlechtestem Wert („Gap“, S. 8).
- **Tab. 1 (S. 6, am Seitenbild geprüft), Spalte „All“ Avg/Gap:** Mistral-7B-Instruct-v0.2 47,3/56,2; GPT-4-Turbo 79,0/32,1; FILM-7B 85,9/13,9.
- **Dekodierung:** „All models and tasks employ greedy decoding“ (S. 7).
- **Analysen mit 20 % der Trainingsdaten (S. 9):** größere RoPE-Basis hilft; Empfehlung: zehnfache Standardbasis (S. 10, Tab. 3).

## Wörtliche Stellen

> „they still struggle to fully utilize information within the long context, known as the lost-in-the-middle challenge“ (S. 1)

> „the general training process may inadvertently introduce a position bias, suggesting that important information is always located at the beginning and end of the context“ (S. 2)

## Bezug zur Dissertation

- **PROTOKOLL §6 (Kontext, offener Punkt 4 in §12) und §4.10 (LLM-Konfiguration für Freeze 2):** Das Paper begründet, warum die Position einer Information im Prompt die Antwort eines LLM beeinflussen kann (S. 2, 8). Für die WSD-Prompts heißt das: Den Zielbeleg und die Sense-Karten nicht in einem langen Kontext vergraben; ihre Position im Prompt gehört zur festgeschriebenen Konfiguration. Das ist eine Übertragung, das Paper prüft weder WSD noch Klassifikation mit kurzen Kontexten.
- **Kartenreihenfolge (§5, Punkt 5):** Die Zufallsmischung der Karten pro Item fängt auch Positionseffekte beim LLM ab, sofern das LLM dieselben Karten sieht. Das Paper misst Positionseffekte nur über Kontexte von Tausenden Tokens, nicht innerhalb einer kurzen Auswahlliste.
- **Kontamination (§10):** Das 10-Gramm-Filter (S. 16) ist ein Beispiel dafür, wie Evaluationsdaten aus Trainingsdaten herausgehalten werden; es betrifft eigenes Training, nicht den Schutz eines veröffentlichten Goldstandards.
- **Modellwahl:** Proprietäre und offene Modelle unterscheiden sich in der Langkontextnutzung deutlich (Tab. 1, 2). Ob das für kurze WSD-Prompts eine Rolle spielt, zeigt das Paper nicht.

## Grenzen und Einwände

- Nur Englisch und synthetische bzw. moderne Texte; kein Bezug zu historischen Sprachen oder lexikalischer Semantik.
- Die Messung betrifft Kontexte von 4K bis 32K Tokens; WSD-Prompts der Dissertation werden voraussichtlich viel kürzer sein. Die Übertragbarkeit der Positionseffekte auf kurze Prompts ist offen.
- Gelesen ist der Preprint; die NeurIPS-Fassung (sechs Autor:innen, 29 Seiten laut Seitenangabe) kann Zahlen oder Abschnitte ändern [am PDF der Verlagsfassung zu prüfen].
- Ergebnisse für GPT-4-Turbo sind Momentaufnahmen eines API-Modells (Stand 2024).

## Weiterführend

- Liu, Lin, Hewitt, Paranjape, Bevilacqua, Petroni & Liang 2024, Lost in the middle: How language models use long contexts, TACL 12, S. 157 bis 173 (S. 2, 13): die Grundlagenstudie zum Positionseffekt.
- Bai et al. 2023, LongBench (S. 7, 11).
- Hsieh et al. 2024, RULER (S. 10, 12).
