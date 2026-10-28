# Galka & Vogeler 2026: LLMs für Named Entities in digitalen Editionen

**Datei:** `pdf/Galka-Vogeler-2026-LLM-NER-Editionen.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, Volltext (27 Seiten) samt Tabellen am PDF gelesen, Julias Markierungen eingearbeitet, Bibliografie über Crossref geprüft.

**Seitenzählung:** Das lokale PDF ist die Online-First-Fassung („Published online: 28 January 2026", PDF-S. 1) ohne Seitenzahlen. Laut Crossref steht der Artikel in Band 7, Heft 3, S. 483 bis 509; das sind 27 Seiten wie im PDF. Zitiert wird „PDF-S. n (S. 482 + n)". Die Heftseiten sind daraus abgeleitet und nicht an der Heftfassung geprüft.

## Bibliografie

- **Vollständig:** Galka, Selina & Georg Vogeler, 2026. Annotating, projecting, and interpreting named entities in digital scholarly editions with LLMs. *International Journal of Digital Humanities* 7(3), 483 bis 509.
- **DOI/URL:** https://doi.org/10.1007/s42803-025-00114-8 (löst auf link.springer.com auf; die Springer-Seite verlangt eine Anmeldung, die Metadaten wurden am 2026-10-28 über die Crossref-API gelesen). ✔ Eingegangen 21. Juli 2025, angenommen 7. Dezember 2025, online 28. Januar 2026; Lizenz CC BY 4.0; laut Crossref keine Korrektur und kein Rückzug. Crossref verknüpft einen Preprint (Research Square, DOI 10.21203/rs.3.rs-7175875/v1, nicht abgerufen).
- **Art:** begutachteter Zeitschriftenartikel („Original Paper"). Die lokale Fassung ist die veröffentlichte Verlagsfassung, nur noch ohne Heftseitenzahlen.
- **Sprache:** Englisch
- **Abweichung zu `literatur/README.md`:** dort fehlen Band, Heft und Seiten (7(3), 483 bis 509).

## Worum es geht

Am Beispiel der TEI-kodierten französischen Memoiren der Gräfin Luise Charlotte von Schwerin (1684 bis 1732) und ihrer deutschen Übersetzung prüft die Arbeit LLMs für drei Aufgaben digitaler Editionen: Named Entity Recognition für Personen und Orte, Projektion dieser Annotationen auf die Übersetzung und Extraktion von Personenbeziehungen (PDF-S. 1, 3). Bei NER übertrifft Claude Sonnet 4 (Few-shot) das flair-Modell deutlich, vor allem bei Personen, die über Verwandtschaftsausdrücke wie „mon père" bezeichnet werden (PDF-S. 8 bis 9). Bei der Projektion überträgt Claude zero-shot über 97 % der 865 Entitäten korrekt, ohne Wort- oder Satzalignierung (PDF-S. 13). Die Fehleranalyse führt die Autor:innen zu der Frage, was Editor:innen mit Übersetzung und Annotation eigentlich bezwecken (PDF-S. 19, 22 bis 23).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| In Ego-Dokumenten erscheinen viele Personen nur über indirekte Ausdrücke wie „mon père", „ma belle-mère" (nicht-starre Designatoren nach Kripke); dazu kommen Titelketten und verschachtelte Entitäten. | PDF-S. 2 (S. 484), Abschnitt 1 | Problembeschreibung, Begriff referiert (Kripke 1982) |
| LLMs werden für Editionen erprobt: Transkription (besser und billiger als HTR-Systeme bei englischen Handschriften des 18./19. Jh.), Post-OCR-Korrektur, Normalisierung, Annotation. | PDF-S. 3 (S. 485), Abschnitt 2.1 | referiert (Pollin et al. 2025; Humphries et al. 2024; Thomas et al. 2024; Scholger et al. 2025; Pangakis & Wolken 2025) |
| LLMs übertreffen traditionelle NLP-Methoden bei Wortsegmentierung, Wortarten-Tagging und NER in historischen chinesischen Texten. | PDF-S. 4 (S. 486), Abschnitt 2.1 | referiert (Fang et al. 2025) |
| Vorteile von LLMs: mehrere Aufgaben in einem Modell, Few- und Zero-shot ohne große Trainingsmengen, direkte Ausgabe von TEI/XML oder RDF. | PDF-S. 4 (S. 486), Abschnitt 2.1 | Einschätzung der Autor:innen |
| Frühere Evaluationen fanden schwache LLM-Leistung bei NER, vor allem wegen unzureichender Prompts, fehlender Domänenanpassung und schwacher Evaluation; andere Studien finden hohe Genauigkeit oder häufige Halluzinationen. | PDF-S. 4 bis 5 (S. 486 bis 487), Abschnitt 2.2 | referiert (Hiltmann et al. 2025; Tudor et al. 2025) |
| NER-Vergleich: Claude Sonnet 4 erreicht bei Orten F1 0,90, bei Personen 0,73; flair 0,59 und 0,23. | PDF-S. 8 (S. 490), Tab. 1 | eigenes Ergebnis |
| flair verfehlt die meisten nicht-starren Designatoren und taggt Namensbestandteile wie „Schwerin" als Ort; Claude erkennt indirekte Bezüge, Titel und verschachtelte Entitäten besser. | PDF-S. 8 bis 9 (S. 490 bis 491) | eigenes Ergebnis |
| Die strenge Evaluation unterschätzt Claude, weil Artikel („le comte" gegen „comte") als Fehler zählen; diese Variation ist auch im Gold selbst nicht vereinheitlicht. | PDF-S. 9 (S. 491), Abschnitt 3.1.3 | eigenes Ergebnis (manuelle Durchsicht, Umfang nicht beziffert) |
| Projektion: Von 865 französischen Entitäten (761 Personen, 104 Orte) fehlen in Claudes deutscher Ausgabe 22 (16 Personen, 6 Orte); 7 kommen hinzu; über 97 % übertragen; alle `@ref`-Verweise korrekt; alle übertragenen Annotationen sitzen auf dem richtigen Textabschnitt. | PDF-S. 13 (S. 495), Abschnitt 3.2.3; Tab. 2, PDF-S. 15 | eigenes Ergebnis |
| Fehlende Projektionen gehen vor allem auf die Übersetzung zurück: Textvarianten nicht übernommen, Vereinfachung für Lesbarkeit, Paraphrase (z. B. Pronomen statt Namen). | PDF-S. 15 bis 19 (S. 497 bis 501); Tab. 3, PDF-S. 22 | eigenes Ergebnis |
| Llama 4 Maverick ist deutlich schwächer (38 und 6 fehlende, 57 und 9 zusätzliche Entitäten, ca. 36 Textänderungen), GPT-4.1 liegt dazwischen; OLMo-7B liefert unbrauchbare Ergebnisse. | PDF-S. 11, 13, 15, 17 bis 18 (S. 493, 495, 497, 499 bis 500) | eigenes Ergebnis |
| LLM-Ausgaben müssen auf Tag-Integrität und Texterhalt geprüft werden; die Rolle der Editor:innen bleibt unverzichtbar, effiziente Prüfstrategien fehlen noch. | PDF-S. 22 (S. 504), Abschnitt 4 | Schlussfolgerung |
| Für kleine Projekte (ausdrücklich: Dissertationen) kann ein LLM mit anschließender menschlicher Prüfung sinnvoller sein als ein großes Trainingsset; Opazität des Werkzeugs wiegt dann weniger, weil die Begründung aus der geprüften Einzelentscheidung kommt. | PDF-S. 23 (S. 505), Abschnitt 4 | Einschätzung der Autor:innen |

## Daten, Methode, Zahlen

- **Text:** französische Memoiren, zwei Handschriften (A und W), Varianten in `<app>`/`<rdg>`; Französisch nur orthografisch normalisiert, weil das Französisch des 18. Jh. „largely comparable to modern French" sei (PDF-S. 10, S. 492). Deutsche Übersetzung absatzweise aliniert, frei, noch nicht endkorrigiert, teils mit doppelten Satzfassungen (PDF-S. 10 bis 11, Fn. 7).
- **NER-Gold:** 50 Absätze, 444 Personen- und 81 Ortsentitäten, annotiert von drei Projektmitarbeiter:innen (Ines Peper, Michael Pölzl, Chiara Petrolini; PDF-S. 7, S. 489, Fn. 5). Eine Übereinstimmung zwischen ihnen wird nicht berichtet.
- **NER-Verfahren:** flair ner-french (BiLSTM-CRF) über Klartext mit Rückführung in TEI; Claude Sonnet 4 (claude-sonnet-4-20250514) direkt auf TEI, Few-shot-Prompt mit Beispielen für explizite und implizite Bezüge, absatzweise; Bewertung mit seqeval auf BIO-Sequenzen, entitätsbezogene Precision, Recall, F1; MISC-Spannen von flair ausgeschlossen (PDF-S. 6 bis 8).
- **Tab. 1 (PDF-S. 8, am PDF geprüft):** LOC Precision/Recall/F1 flair 0,50 / 0,72 / 0,59, Claude 0,89 / 0,91 / 0,90; PER flair 0,30 / 0,19 / 0,23, Claude 0,72 / 0,74 / 0,73.
- **Projektion:** 101 Absätze; Modelle Claude Sonnet 4, GPT-4.1, Llama-4-Maverick-17B-128E-Instruct-FP8, Qwen3-14B (Stand Juli 2025; PDF-S. 11, Fn. 8); Temperatur 0,0; Zero-shot (PDF-S. 12). Prüfung: Skript vergleicht `@ref`-Werte pro Absatz, Abweichungen manuell in einer HTML-Ansicht geprüft; die Spannen manuell, „as no ground truth reference was available" (PDF-S. 12 bis 13). Wer prüfte, wird nicht gesagt.
- **Tab. 2 (PDF-S. 15, am PDF geprüft), fehlende Personen / fehlende Orte / zusätzliche Personen / zusätzliche Orte:** Claude 16 / 6 / 6 / 1; Llama 38 / 6 / 57 / 9; GPT-4.1 20 / 7 / 26 / 10; Qwen 86 / 13 / 1 / 0. Alle vier Ausgaben gültiges TEI; Textänderungen bei Claude 6, GPT 9, Llama ca. 36.
- **Beziehungsextraktion:** ein Absatz (P.86), Claude Sonnet 4 im Chat, RDF-Ausgabe; alle neun Beziehungen erkannt, zwei Prädikate außerhalb der Relationship-Ontologie (PDF-S. 19 bis 20).

## Wörtliche Stellen

> „LLM output must be validated for tag integrity and text preservation, as subtle changes in wording, punctuation, or markup may occur or elements may be lost." (PDF-S. 22, S. 504)

> „Scholarly justification is then drawn not from the computational method but from the individual decision prepared by the LLM." (PDF-S. 23, S. 505)

> „It should also be noted that such variations are not standardized within the ground truth itself." (PDF-S. 9, S. 491)

## Bezug zur Dissertation

- **Protokoll 9.1 und 9.2 (Gold mit gemessener Übereinstimmung):** Die Arbeit evaluiert gegen ein Gold dreier Projektmitarbeiter:innen ohne berichtete IAA und stellt selbst fest, dass das Gold uneinheitlich ist (PDF-S. 9). Das ist ein konkretes Beispiel für die Lücke, die `goldstandard/LITERATUR-IAA.md` für LLM-Studien an historischen Sprachen beschreibt (F1 gegen Gold ohne IAA), und stützt Abweichung A5 (zwei Annotator:innen plus Adjudikation).
- **Protokoll 4.10 (Freeze 2, LLM-Konfiguration):** Modellversion mit Datum, Temperatur 0,0 und Prompt sind dokumentiert (PDF-S. 6, 11 bis 12, Fn. 2 und 8); als Vorlage für die Dokumentation brauchbar. Die Arbeit nennt Ausgabedrift zwischen Modellversionen als Risiko (PDF-S. 23).
- **Protokoll 6 (Ausweichlabels) und Inventarbefund:** Viele „Fehler" der Projektion liegen nicht beim Modell, sondern in der Vorlage (Übersetzung ohne Entsprechung, doppelte Fassungen; PDF-S. 15 bis 19). Analog erwartet das Protokoll `KEINE_PASST` und `TEXT_DEFEKT` als eigene Befunde statt als LLM-Fehler.
- **Protokoll 10 und Dissertationskontext:** Die Einschätzung für kleine Projekte (PDF-S. 23) passt zur Lage der Dissertation mit zwei Annotator:innen.
- **Grenze der Übertragung:** Die Arbeit nutzt normalisiertes Französisch, das nach eigener Angabe dem modernen nahe ist (PDF-S. 10). Für Mittelhochdeutsch gilt das nicht; die guten Werte sind daher kein Hinweis auf die Erwartung für WSD in der MHDBDB. NER ist zudem eine Spannenaufgabe mit wenigen Typen, keine Wahl aus einem lemmaspezifischen Bedeutungsinventar.

## Grenzen und Einwände

- Kleine Stichproben (50 Absätze für NER, 101 für Projektion, ein Absatz für Beziehungen), ein Text, ein Sprachpaar.
- NER-Gold ohne IAA und nach eigener Aussage uneinheitlich (PDF-S. 9); die Projektion hat gar kein Gold für die Spannen, nur manuelle Durchsicht unbekannter Personen (PDF-S. 12 bis 13).
- Die Aussage „over 97 % … to the correct spans" (PDF-S. 18) beruht auf dieser Durchsicht, nicht auf einem unabhängigen Vergleich.
- Spannung im Text: Einerseits sei menschliche Beteiligung hier „not necessarily" nötig, weil auch Menschen Fehler machen (PDF-S. 19), andererseits bleibe die Rolle der Editor:innen „indispensable" (PDF-S. 22).
- Kleinere Widersprüche (am PDF geprüft): Abschnitt 3.2.2 spricht von „three LLMs" und nennt vier (PDF-S. 11); für Qwen nennt der Text 101 nicht übertragene Personenannotationen (PDF-S. 18), Tab. 2 86 (PDF-S. 15).
- Few-shot-Prompt bei NER enthielt Beispiele wie „comte de Schwerin" und „ma tante" (PDF-S. 7), die im Testtext selbst vorkommen; ob die Prompt-Beispiele aus den 50 Testabsätzen stammen, wird nicht gesagt.
- Nur kommerzielle Spitzenmodelle liefern die starken Werte; die offenen Modelle (Llama, Qwen, OLMo) sind deutlich schwächer (PDF-S. 15, 17 bis 18).

## Weiterführend

- Hiltmann et al. 2025, „NER4all", LLM-NER auf historischen Reiseführern, Preprint arXiv:2502.04351 (PDF-S. 4).
- Tudor, Megyesi & Östling 2025, Zero-shot-NER in historischen Texten, LaTeCH-CLfL 2025 (PDF-S. 5).
- Fang et al. 2025, LLMs für Segmentierung, Wortarten und NER in historischen chinesischen Quellen (PDF-S. 4).
- Ehrmann et al. 2023, Survey NER in historischen Dokumenten, ACM Computing Surveys 56(2) (PDF-S. 4).
- Pollin et al. 2025, generative KI in digitalen Editionen, ZfdG 10 (PDF-S. 3).
- Pangakis & Wolken 2025, ICWSM (PDF-S. 3); siehe Zusammenfassung zu Pangakis et al. 2023.
- Törnberg 2024, Best practices für Textannotation mit LLMs, Sociologica 18(2) (PDF-S. 3).

## Julias Markierungen und Notizen im PDF

Markiert sind vor allem das Abstract (Aufgaben, Überlegenheit gegenüber Baselines, Projektion ohne Alignierung, über 97 % zero-shot, Fehleranalyse und Frage nach editorischen Absichten), auf PDF-S. 3 der Überblick über LLM-Anwendungen in Editionen (Pollin; Humphries zu HTR; Post-OCR; Normalisierung; Annotation mit Verweis auf Pangakis & Wolken) und auf PDF-S. 4 die Literatur zu historischer NER, Fang et al. zu Wortarten und NER sowie der Absatz zu Mehrfachaufgaben und Few-/Zero-shot. Alle markierten Stellen sind in die Kernaussagen oder das Weiterführende aufgenommen. Neben dem Absatz mit der Zielsetzung des Artikels (PDF-S. 3) steht ein Randstrich und die Notiz „Zusa" (offenbar unvollständig; Bedeutung nicht aus dem PDF ableitbar).
