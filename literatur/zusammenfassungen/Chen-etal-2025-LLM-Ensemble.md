# Chen et al. 2025: Harnessing Multiple Large Language Models (Survey on LLM Ensemble)

**Datei:** `pdf/Chen-etal-2025-LLM-Ensemble.pdf` (nur lokal; 10 Seiten, arXiv 2502.18036v5 vom 18.09.2025)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-29, ganze Textebene gelesen, Julias Markierungen abgeglichen. Priorität 3: bewusst knapp. Laut Literaturliste früher gelesen und zusammengefasst; diese Zusammenfassung liegt nicht im Repo.

Seitenzählung: Das PDF hat keine gedruckten Seitenzahlen; angegeben sind PDF-Seiten.

## Bibliografie

- **Vollständig (lokale Fassung):** Chen, Zhijun; Li, Jingzheng; Chen, Pengpeng; Li, Zhuoran; Sun, Kai; Luo, Yuankai; Mao, Qianren; Li, Ming; Xiao, Likang; Yang, Dingqi; Ban, Yikun; Sun, Hailong; Yu, Philip S. (2025). Harnessing Multiple Large Language Models: A Survey on LLM Ensemble. arXiv:2502.18036v5 [cs.CL].
- **Begutachtete Fassung:** Chen, Zhijun; Lu, Xiaodong; Li, Jingzheng; Chen, Pengpeng; Li, Zhuoran; Sun, Kai; Luo, Yuankai; Mao, Qianren; Li, Ming; Xiao, Likang; Yang, Dingqi; Ban, Yikun; Sun, Hailong (2026). Harnessing Multiple Large Language Models: A Survey on LLM Ensemble. In: Diego Calvanese (Hg.), *Proceedings of the Thirty-Fifth International Joint Conference on Artificial Intelligence (IJCAI-26)*, Survey Track, S. 7807 bis 7816. DOI 10.24963/ijcai.2026/867. Quelle: IJCAI-Seite und Crossref, am 2026-10-28 abgerufen. **Autorenliste weicht ab:** IJCAI ohne Philip S. Yu, dafür mit Xiaodong Lu; arXiv v6 (22.04.2026) nennt 15 Personen. Die IJCAI-Fassung ist nicht gelesen.
- **DOI/URL:** https://doi.org/10.24963/ijcai.2026/867 (aufgelöst auf ijcai.org); arXiv https://doi.org/10.48550/arXiv.2502.18036; Paperliste github.com/junchenzhi/Awesome-LLM-Ensemble (S. 1, nicht aufgerufen).
- **Art:** lokal Preprint; begutachtet erschienen als Konferenzbeitrag (Survey Track)
- **Sprache:** Englisch

## Worum es geht

Der Überblick ordnet Verfahren, die mehrere LLMs für dieselbe Anfrage kombinieren, nach dem Zeitpunkt der Kombination: vor der Inferenz (ein Router wählt ein Modell), während der Inferenz (Token-, Span- oder Prozessebene) und nach der Inferenz (Auswahl oder Neugenerierung aus vollständigen Antworten, oder Kaskaden vom kleinen zum großen Modell) (S. 1 bis 2). Er beschreibt die Verfahren in drei Übersichtstabellen, nennt zwei Benchmarks und schließt mit offenen Forschungsfragen (S. 3 bis 7). Eigene Experimente enthält er nicht.

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Motivation: Leistungszweifel (Genauigkeit, Halluzination, Abweichung von der Absicht) und unterschiedliche Stärken und Kosten der Modelle; statt sich auf ein Modell nach Rangliste zu verlassen, mehrere kombinieren. | S. 1, Abschnitt 1 | Begründung der Autor:innen |
| Drei Paradigmen: ensemble-before-inference (Routing), ensemble-during-inference (Token, Span, Prozess), ensemble-after-inference (non-cascade, cascade). | S. 1 bis 2, Abschnitt 2.1, Abb. 1 bis 2 | eigene Taxonomie |
| Abgrenzung: LLM Merging verschmilzt Parameter; LLM Collaboration verteilt Rollen; Weak Supervision bzw. Learning from Crowds aggregiert Labels mehrerer schwacher Annotationsquellen, entspricht damit „non-cascade ensemble after inference“, ist aber meist auf Klassifikation beschränkt. | S. 2, Abschnitt 2.2 | Einordnung |
| Auswahlverfahren nach der Inferenz folgen oft dem Mehrheitsprinzip: gewählt wird die Antwort, die den anderen am ähnlichsten ist; Li et al. (2024a) fragen dasselbe Modell mehrfach und finden einen Skalierungseffekt mit mehr Antworten. | S. 5, Abschnitt 3.3.1 | referiert |
| Kaskaden entscheiden, ob die Antwort des aktuellen Modells reicht; ein Kriterium ist Antwortkonsistenz über mehrere Prompts (Yue et al. 2024), ein anderes die Klassenunsicherheit. | S. 6, Abschnitt 3.3.2 | referiert |
| Zusammenfassend: Auswahl entspricht hartem Voting; feinere Granularität nutzt die Verteilungen der Modelle besser; Verfahren ohne Kostenbeschränkung haben das größte Leistungspotenzial. | S. 7, Abschnitt 5.1, Tab. 4 | Synthese der Autor:innen |
| Benchmarks: MixInstruct (11 LLMs, 11K Testbeispiele) und RouterBench. | S. 7, Abschnitt 4 | referiert |
| Offene Probleme: zu einfache Ähnlichkeitsmaße zwischen Antworten oder überwachte Komponenten ohne Generalisierung bei Verfahren nach der Inferenz; Kaskaden selten für Generierung. | S. 7, Abschnitt 5.2 | Einschätzung |

## Daten, Methode, Zahlen

Survey ohne eigene Daten oder Messungen. Als Hintergrund: über 182.000 Modelle im Hugging-Face-Verzeichnis (S. 1, Anm. 1; Stand der Fassung, nicht datiert). Die Tabellen 1 bis 3 (S. 4 bis 6) klassifizieren je Verfahren Überwachung, Strategie, Modellzahl und Aufgabentyp; Code-Links nicht geprüft. Kein Verfahren betrifft WSD; die Aufgabentypen sind überwiegend Generierung, einige Klassifikation (Tab. 3, Kaskaden).

## Wörtliche Stellen

> „This paper presents the first systematic review of recent developments in LLM Ensemble.“ (S. 1)

> „Weak Supervision […] uses weak labels contributed from multiple weak annotation sources to perform information aggregation […] (corresponding non-cascade ensemble after inference in LLM Ensemble)“ (S. 2)

## Bezug zur Dissertation

- **PROTOKOLL §4.10 (Freeze 2: „Anzahl der Läufe pro Item“):** Mehrfaches Abfragen desselben Modells mit Mehrheitsentscheid ist ein eigenes Ensemble-Verfahren mit Skalierungseffekt (Li et al. 2024a, referiert S. 5); Antwortkonsistenz dient als Konfidenzsignal (Yue et al. 2024, S. 6). Wenn das Protokoll mehrere Läufe pro Item vorsieht, muss vorab feststehen, ob das Ergebnis ein Einzellauf, eine Mehrheit oder eine Verteilung ist; sonst vergleicht der McNemar-Test (§9.2) ein Ensemble mit einer Einzelbaseline.
- **§9.2 (LLM gegen Baseline) und Auswertung pro Modell:** Ein Ensemble mehrerer LLMs wäre eine zusätzliche Systemvariante; für die Forschungsfrage (§1) genügt ein festgelegtes System. Die Übersicht liefert die Begriffe, falls Varianten berichtet werden.
- **Annotation statt Generierung:** Die Verbindung zu Weak Supervision und Learning from Crowds (S. 2) ist der Punkt, an dem LLM-Ensembles und die Aggregation mehrerer Annotationsquellen zusammenfallen. WSD mit festem Inventar ist eine Klassifikationsaufgabe, für die nach Chen et al. die meisten Aggregationsverfahren entworfen sind.
- Kein Bezug zu IAA, Goldstandard oder historischen Sprachen.

## Grenzen und Einwände

- Reiner Überblick ohne vergleichende Messung; Wertungen (z. B. Leistungspotenzial nach Granularität, S. 7) sind nicht empirisch belegt.
- Die meisten Verfahren brauchen Zugriff auf Token-Verteilungen oder Trainingsdaten (Tab. 1 bis 2) und sind mit API-Modellen nur teils nutzbar.
- Fast alle zitierten Arbeiten sind Preprints von 2023 bis 2025; der Stand veraltet schnell.
- Gelesen ist arXiv v5; IJCAI-Fassung und v6 können Inhalt und Tabellen geändert haben [am PDF der Verlagsfassung zu prüfen].

## Weiterführend

- Li, Zhang, Yu, Fu & Ye 2024a, More agents is all you need, arXiv:2402.05120 (S. 5, 8): Mehrfachabfrage und Mehrheitsentscheid.
- Yue, Zhao, Zhang, Du & Yao 2024, Large language model cascades with mixture of thought representations, ICLR 2024 (S. 6, 10): Antwortkonsistenz als Konfidenz.
- Zheng, Li, Li, Shan & Cheng 2017, Truth inference in crowdsourcing: Is the problem solved?, PVLDB 10(5), S. 541 bis 552 (S. 2, 10): Aggregation mehrerer Annotator:innen.
- Ratner et al. 2017, Snorkel (S. 2, 9).

## Julias Markierungen im PDF

32 rosa Hervorhebungen und eine Notiz (`md/Chen-etal-2025-LLM-Ensemble.markierungen.md`). Markiert sind die Motivation (Leistungszweifel, unterschiedliche Stärken, über 182.000 Modelle) und die drei Paradigmen (PDF-Seite 1), die Abgrenzung zu Merging, Collaboration, Weak Supervision und Learning from Crowds sowie der Router (PDF-Seite 2), die Unterteilung der Router (PDF-Seite 3) und auf PDF-Seite 7 die Granularitätsbewertung, die Benchmarks MixInstruct und RouterBench und der Satz zu den sieben Ansätzen. Alles davon ist in Kernaussagen oder Bezug aufgenommen; die Router-Unterklassen nur in „Worum es geht“.

## Julias Notizen im PDF

- PDF-Seite 2, am rechten Rand auf Höhe von Abschnitt 2.2 (LLM Merging mit den Verweisen Yang et al. 2024; Yang et al. 2025; Ruan et al. 2025): „Literatur !“
