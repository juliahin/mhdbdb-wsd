# Berzak, Huang, Barbu, Korhonen & Katz 2016: Anchoring and Agreement in Syntactic Annotations

**Datei:** `pdf/Berzak-etal-2016-Anchoring-Agreement.pdf` (nur lokal; 10 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-16, ganze Textebene gelesen; Tab. 1 bis 4 (S. 2219 bis 2221) am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology D16-1239 (SHA-256 verglichen am 2026-11-16); es enthält keine Markierungen.

Seitenzählung: gedruckte Seite = PDF-Seite + 2214 (PDF 1 = S. 2215, PDF 10 = S. 2224). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Berzak, Yevgeni, Yan Huang, Andrei Barbu, Anna Korhonen & Boris Katz (2016). Anchoring and Agreement in Syntactic Annotations. In: Jian Su, Kevin Duh & Xavier Carreras (Hg.), *Proceedings of the 2016 Conference on Empirical Methods in Natural Language Processing*. Austin, Texas: Association for Computational Linguistics, S. 2215 bis 2224.
- **DOI/URL:** 10.18653/v1/D16-1239 (aufgelöst, Crossref); https://aclanthology.org/D16-1239/ (Herausgeber:innen und Monat November nach dem BibTeX der Anthology, abgerufen 2026-11-16)
- **Lizenz:** CC BY 4.0 (ACL Anthology, Material ab 2016; FAQ abgerufen 2026-11-16); im PDF „©2016 Association for Computational Linguistics“.
- **Art:** Konferenzbeitrag (begutachtet)
- **Sprache:** Englisch

## Worum es geht

Die Arbeit prüft, ob Annotator:innen, die vorannotierte Ausgaben von Tagger und Parser korrigieren, sich an diesen Vorgaben ausrichten (Ankereffekt, hier „parser bias“), und was daraus für Evaluation und Qualität von Goldstandards folgt (S. 2215 bis 2216). Fünf geschulte Studierende annotieren Wortarten und Dependenzen englischer Lernersätze teils von Grund auf, teils als Korrektur zweier verschiedener Parser; die korrigierten Fassungen lassen jeden Parser auf „seinem“ Gold besser abschneiden, und unabhängige Gutachter:innen ziehen das rein menschliche Gold vor (S. 2218 bis 2220). In einem zweiten Experiment ohne Vorannotation messen die Autor:innen die menschliche Übereinstimmung auf WSJ-Sätzen und finden sie auf dem Niveau der besten Parser (S. 2220 bis 2221).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Anchoring ist eine Urteilsverzerrung, bei der Urteile zu vorgegebenen Werten hin gezogen werden; meist zeigt sie sich als Angleichung an die vorgegebenen Werte. | S. 2215 Abstract; S. 2216 | referiert (Tversky & Kahneman 1974) |
| Linguistische Goldstandards entstehen oft durch menschliche Korrektur automatischer Vorannotation; die Begründung dafür stammt aus den POS-Experimenten des Penn Treebank (Marcus et al. 1993): schneller, konsistenter, besser. | S. 2215 | referiert |
| Die Korrektur von Tagger- und Parserausgaben zeigt einen klaren Ankereffekt: Jedes der beiden Tagger-Parser-Paare schneidet auf dem aus seiner eigenen Ausgabe korrigierten Gold besser ab als das andere, obwohl beide auf dem menschlichen Gold gleich gut sind. | S. 2219, Tab. 1 | eigenes Ergebnis |
| Zusätzlich schneidet jedes Paar auch auf dem Gold des anderen Parsers besser ab als auf dem menschlichen Gold: eine Verzerrung zu dem hin, was Parser gemeinsam vorhersagen. | S. 2219 | eigenes Ergebnis |
| Folge für die Evaluation: Gold aus Parserkorrektur überschätzt die Leistung dieses Parsers und von Parsern überhaupt. | S. 2219; S. 2222 | eigenes Ergebnis, Deutung der Autor:innen |
| Folge für die Qualität: Unabhängige Gutachter:innen ziehen bei Abweichungen das menschliche Gold dem Parser-Gold vor (56,72 % bis 64,32 %); die schlechtere Ausgangsqualität „percolates via anchoring“ ins Gold. | S. 2220, Tab. 2 | eigenes Ergebnis |
| Der Qualitätsverlust liegt fast ganz bei parserspezifisch übernommenen Fehlern; wo beide Parser übereinstimmen, ist das Gold nicht klar schlechter. | S. 2220, Tab. 3 | eigenes Ergebnis |
| Wenn beide Annotator:innen dieselbe automatische Vorgabe bearbeiten, kann Anchoring sowohl Scheinübereinstimmung als auch Scheinabweichung erzeugen; Übereinstimmungswerte aus solchen Abläufen sind deshalb nicht verlässlich. | S. 2220 | Argument der Autor:innen |
| Marcus et al. (1993) fanden POS-Übereinstimmung 92,8 bei Annotation von Grund auf gegenüber 96,5 bei Korrektur von Taggerausgaben. | S. 2220 | referiert |
| Übereinstimmung ohne jede Vorannotation, mit einer unabhängigen Korrekturrunde je Annotation: POS 95,65, UAS 94,17, LA 94,04, LAS 90,33; vor der Korrekturrunde 94,78 / 93,07 / 92,3 / 88,32. | S. 2221, Tab. 4 | eigenes Ergebnis |
| Diese menschlichen Werte liegen unter der POS-Genauigkeit guter Tagger (über 97 %) und auf dem Niveau der besten Dependenzparser; Parsing auf englischen Zeitungstexten erreiche womöglich die menschliche Übereinstimmung. | S. 2221; S. 2223 | eigenes Ergebnis und Deutung; Vergleichswerte referiert |
| Anchoring wurde in der Psychologie auch bei Fachleuten gezeigt, dort aber schwächer als in den frühen Experimenten. | S. 2222 | referiert (Wilson et al. 1996; Mussweiler & Strack 2000) |
| Vorschlag „hybrid“: Menschen prüfen nur, worin mehrere Parser übereinstimmen, und annotieren den Rest von Grund auf. | S. 2222 | Vorschlag der Autor:innen, nicht erprobt |

## Daten, Methode, Zahlen

- **Annotator:innen:** fünf Studierende am MIT (drei Linguistik im Hauptfach, zwei Ingenieurwesen mit Linguistik im Nebenfach), zwei Monate Schulung, danach fünf Monate Arbeit an einer Lerner-Baumbank mit je etwa 800 Annotationen und ebenso vielen Korrekturen; die Autor:innen sehen darin einen Grund, warum Ankereffekte eher kleiner und Übereinstimmung eher höher ausfallen (S. 2217 bis 2218).
- **Aufgaben:** Annotation von Grund auf, Korrektur („reviewing“) einer vorgegebenen Annotation, deren Quelle nicht genannt wird, und Rangfolge mehrerer Optionen („ranking“), die in zufälliger Reihenfolge gezeigt werden (S. 2216 bis 2217). Ein Zeichen `#` in jeder Zeile der Korrekturvorlage soll verhindern, dass Vorgaben passiv durchgewunken werden (S. 2217).
- **Experiment 1 (Bias):** 360 Sätze (6.979 Tokens) aus dem FCE-Lernerkorpus; pro Satz werden vier der fünf Personen zufällig auf Annotation, Korrektur der Annotation, Korrektur Turbo und Korrektur Stanford/RBG verteilt, die fünfte beurteilt (S. 2218, Abb. 1). Übereinstimmung der Korrigierenden mit den Annotierenden: 98,24 POS, 97,16 UAS, 96,3 LA, 94,81 LAS (S. 2218).
- **Tab. 1 (S. 2219, Seitenbild):** Turbo auf Human Gold 95,32 POS / 82,29 LAS, auf Turbo Gold 97,62 / 89,16; RBG auf Human Gold 95,59 / 82,05, auf RBG Gold 97,76 / 87,87. Mittlere Fehlerreduktion auf Parser-Gold gegenüber Human Gold: 49,18 % POS, 33,71 % UAS, 34,9 % LA, 35,61 % LAS (S. 2219). Unterschiede nach McNemar mit p ≪ 0,001.
- **Tab. 2 (S. 2220):** Bevorzugung des Human Gold gegenüber Turbo Gold 64,32 / 63,96 / 61,5 % (POS / HIND / REL), gegenüber RBG Gold 56,72 / 61,38 / 57,73 %; signifikant (zweiseitiger Z-Test, p < 0,01) außer RBG-POS. Abweichende Tokens jeweils etwa 200 (POS) bzw. 435 bis 444 (HIND, REL).
- **Tab. 3 (S. 2220):** bei parserspezifisch übernommenen Werten 73,81 % bis 85,42 % für Human Gold, bei von beiden Parsern geteilten Werten nur 51,57 % bis 58,49 %.
- **Experiment 2 (IAA):** 300 Sätze (7.227 Tokens) aus Abschnitt 23 des WSJ-Penn-Treebank; pro Satz zwei Personen von Grund auf, zwei weitere korrigieren je eine dieser Annotationen unabhängig (S. 2221, Abb. 2). Maß: Prozent übereinstimmender Tokens (POS, UAS, LA, LAS), ohne Satzzeichen (S. 2217); kein zufallskorrigiertes Maß, keine Intervalle.

## Wörtliche Stellen

> „Anchoring is a well known cognitive bias in human decision making, where judgments are drawn towards pre-existing values.“ (S. 2215)

> „[…] anchoring can introduce cases of spurious disagreement as well as spurious agreement between annotators due to alignment of one or both participants towards the given input.“ (S. 2220)

> „[…] gold standard annotations that are based on editing output of automatic tools can lead to inaccurate figures in system evaluations and lower annotation quality.“ (S. 2216)

## Bezug zur Dissertation

**Antwort auf die Leitfrage: Was sagt das Werk zum Ankereffekt vorgegebener Optionen?** Untersucht ist ein **vorausgefüllter Antwortwert** (Ausgabe eines Taggers oder Parsers), den Menschen bestätigen oder korrigieren (S. 2216 bis 2217). Eine Liste von Antwortoptionen ohne vorgewählte Antwort, wie die Karten im Pilot, untersucht die Arbeit nicht. Für die Frage aus A31, ob schon das Zeigen des Inventars die Lesart lenkt, ist sie deshalb **keine direkte Stütze**, sondern nur ein Analogieschluss. Direkt belegt sie dreierlei: (a) dass Vorgaben in Annotationsabläufen messbar verankern, auch bei geschulten Personen (S. 2219, S. 2222); (b) dass das so entstandene Gold eine Systembewertung verzerrt (S. 2219); (c) dass gemeinsames Arbeiten an derselben Vorgabe die Übereinstimmung künstlich hebt oder senkt (S. 2220). Die einzige Randbemerkung zu Optionslisten ist methodisch: In der Ranking-Aufgabe werden die Optionen in zufälliger Reihenfolge gezeigt (S. 2217).

**1. PROTOKOLL §6, „Blindheit“ (keine Silber-`@ana`, keine LLM-Vorschläge in der Annotationsdatei): gestützt, und zwar direkt.** Silber oder ein LLM-Vorschlag auf der Karte wäre genau der Fall dieser Arbeit (Korrektur einer Vorannotation). Nach S. 2219 würde ein so erzeugtes Gold das System begünstigen, dessen Ausgabe gezeigt wurde; im Protokoll wären das Silber (für die Silberqualität, §9.2) bzw. das LLM (für den Vergleich mit MFS). Das ist eine stärkere Begründung als die bisherige („nicht nur durch eine Anweisung“) und lässt sich zitieren.

**2. PROTOKOLL §7 Schritt 8 („Erst danach werden Silber und LLM-Ausgabe mit dem Gold verglichen“) und §7 Schritt 6 (Adjudikation): gestützt.** Der Befund aus Tab. 2 und 3 (S. 2220) spricht dafür, dass auch die Adjudikation weder Silber noch LLM-Ausgabe sehen sollte; das Protokoll sagt bisher nur, dass sie nicht sieht, von wem die beiden Labels stammen. **Vorschlag:** in §7 Schritt 6 ergänzen, dass Silber und LLM-Ausgabe der Adjudikation verborgen bleiben, mit Verweis auf Berzak et al. (2016, S. 2219 bis 2220).

**3. A31 und offener Punkt 21 (Literatur zum Ankereffekt vorgegebener Antwortoptionen): nur teilweise gedeckt.** Die Arbeit kann im Protokoll für „Vorgaben verankern“ stehen, nicht für „ein vorgegebenes Inventar ohne vorgewählte Antwort lenkt die Lesart“. Wer A31 literarisch begründen will, braucht dafür eigene Literatur. Brauchbare Spuren aus der Arbeit selbst: Fort & Sagot 2010 (Vor-Tagging) und Skjærholt 2013 (Vor-Parsing), beide S. 2222, sowie die psychologischen Übersichten Furnham & Boo 2011 und Wilson et al. 1996 (S. 2222). Für vorgegebene Antwortoptionen im engeren Sinn verweist Beck et al. 2024 auf die Umfrageforschung (Krosnick et al. 1996, Schuman & Presser 1996; siehe dort).

**4. A31, Messidee des Lesart-Schritts: methodisch passend.** Das Design der Arbeit (dieselbe Aufgabe einmal von Grund auf, einmal mit Vorgabe, Vergleich der Ergebnisse) ist das Muster, nach dem der Lesart-Schritt den Einfluss der Karten messbar machen soll. Die Zahlen zeigen auch, in welche Richtung der Effekt erwartbar ist: Mit Vorgabe stieg die Übereinstimmung (Marcus et al., referiert S. 2220), ohne Vorgabe fiel sie niedriger aus (Tab. 4, S. 2221). Für offenen Punkt 20 (Auswertung der Lesarten) folgt daraus: Übereinstimmung der Lesarten untereinander und Übereinstimmung der Kartenwahl getrennt berichten, damit sichtbar wird, ob die Karten die Übereinstimmung heben.

**5. PROTOKOLL §5 Punkt 5 (Kartenreihenfolge zufällig gemischt): bestätigt als übliche Vorsichtsmaßnahme** (Ranking-Optionen in zufälliger Reihenfolge, S. 2217), ohne eigene Messung dazu.

**6. PROTOKOLL §9.2 (LLM gegen menschliche IAA als Obergrenze): ergänzt.** Die Arbeit vergleicht Systemleistung direkt mit menschlicher Übereinstimmung und findet Systeme auf oder über ihr (S. 2221). Das stützt die Rolle der menschlichen IAA als Vergleichsmaßstab, zeigt aber auch, dass dieser Maßstab bei Vorannotation zu hoch ausfällt.

**7. LITERATUR-IAA.md, Zeile „Reihenfolge der Items verändert Urteile; Vorannotationen verankern“ (Berzak et al. 2016 ✔): bestätigt** für den Teil „Vorannotationen verankern“. Für das Protokoll gilt die Einschränkung aus Punkt 3.

## Grenzen und Einwände

- Gegenstand ist Syntax (POS, Dependenzen) mit sehr hoher Grundübereinstimmung (über 90 %); bei WSD mit niedrigerer Übereinstimmung und Ermessensspielraum könnte der Ankereffekt größer sein, das zeigt die Arbeit aber nicht.
- Untersucht ist nur die Korrektur einer vorausgefüllten Antwort, nicht ein Menü von Optionen und nicht die Darbietung eines Inventars.
- Übereinstimmung in Prozent übereinstimmender Tokens, ohne Zufallskorrektur und ohne Konfidenzintervalle (Tab. 4); die Qualitätsurteile in Tab. 2 und 3 stammen von einer einzelnen Person pro Satz aus derselben Gruppe.
- Die fünf Personen hatten zuvor monatelang zusammengearbeitet; die Autor:innen sagen selbst, dass das Ankereffekte eher verkleinert (S. 2218).
- Die Werte von Marcus et al. (1993) sind nur referiert.
- Übertragbarkeit auf Mittelhochdeutsch und ein onomasiologisches Inventar: nicht berührt; der Mechanismus (Vorgaben werden übernommen) ist aber aufgabenunabhängig beschrieben.

## Weiterführend

- Marcus, Marcinkiewicz & Santorini 1993, *Computational Linguistics* 19(2), S. 313 bis 330 (zitiert S. 2215, 2220, 2222): Ausgangsbefund zu Annotation von Grund auf gegenüber Korrektur.
- Fort & Sagot 2010, Influence of pre-annotation on POS-tagged corpus development, LAW IV, S. 56 bis 63 (S. 2222).
- Skjærholt 2013, Influence of preprocessing on dependency syntax annotation: speed and agreement, LAW VII (S. 2222).
- Tversky & Kahneman 1974, *Science* 185 (S. 2216, 2222); Furnham & Boo 2011, *Journal of Socio-Economics* 40(1) (S. 2222); Wilson, Houston, Etling & Brekke 1996, *Journal of Experimental Psychology: General* 125(4) (S. 2222); Mussweiler & Strack 2000, *Journal of Experimental Social Psychology* 36(5) (S. 2222).
- Sampson & Babarczy 2008, *Natural Language Engineering* 14(4) (S. 2222): Übereinstimmung von Grund auf, Hauptquelle von Abweichungen seien Fehler.
- Plank, Hovy & Søgaard 2014, Linguistically debatable or just plain wrong?, ACL (S. 2223).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF.
