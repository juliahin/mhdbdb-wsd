# Hovy, Marcus, Palmer, Ramshaw & Weischedel 2006: OntoNotes, The 90% Solution

**Datei:** `pdf/Hovy-etal-2006-OntoNotes.pdf` (nur lokal; 4 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Abb. 1 und 2 (S. 58) am Seitenbild geprüft. Das lokale PDF ist byte-gleich mit dem PDF der ACL Anthology (SHA-256 verglichen am 2026-11-13), also die Verlagsfassung; es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 56 + n (PDF 1 = S. 57, PDF 4 = S. 60). Unten stehen gedruckte Seiten.

## Bibliografie

- **Vollständig:** Hovy, Eduard, Mitchell Marcus, Martha Palmer, Lance Ramshaw & Ralph Weischedel (2006). OntoNotes: The 90% Solution. In: Robert C. Moore, Jeff Bilmes, Jennifer Chu-Carroll & Mark Sanderson (Hg.), *Proceedings of the Human Language Technology Conference of the NAACL, Companion Volume: Short Papers*. New York City: Association for Computational Linguistics, S. 57 bis 60.
- **DOI/URL:** keine DOI; https://aclanthology.org/N06-2015/ (Herausgeber:innen, Ort, Monat Juni und Seiten aus dem BibTeX der Anthology, abgerufen 2026-11-13; Kopfzeile S. 57: „pages 57–60, New York, June 2006“).
- **Lizenz:** CC BY-NC-SA 3.0 (ACL Anthology, Material vor 2016, laut Fußzeile der Anthology, abgerufen 2026-11-13).
- **Art:** Konferenzbeitrag (Kurzbeitrag, vier Seiten)
- **Sprache:** Englisch

## Worum es geht

Ein Projektbericht über OntoNotes, ein mehrsprachiges Korpus mit Syntax (Treebank), Prädikat-Argument-Struktur (PropBank), Wortbedeutungen mit Anbindung an eine Ontologie (Omega) und Koreferenz, das mit 90 % Übereinstimmung zwischen Annotator:innen entstehen soll (S. 57). Für die Wortbedeutungen gruppiert ein Linguist feinkörnige WordNet-Senses zu groben Gruppen; an 50 Sätzen pro Wort wird die Übereinstimmung geprüft, und liegt sie unter 90 %, wird die Gruppierung überarbeitet (S. 58). Das Werk ist eine Vorschau mit wenigen Zahlen: Es berichtet keine gemessenen Übereinstimmungswerte für die Sense-Annotation, nur das Ziel von 90 % und eine Systemgenauigkeit aus einer anderen Arbeit (S. 59).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Ziel: ein Korpus „constructed at 90% interannotator agreement“; erster Teil 300K Wörter englische und 250K Wörter chinesische Nachrichten, Freigabe 2007. | S. 57, Abstract | Projektangabe |
| Pilotstudien hätten gezeigt, dass Prädikatstruktur, Wortbedeutung, Ontologie-Anbindung und Koreferenz „rapidly and with better than 90% consistency“ annotierbar seien. Zahlen zu diesen Pilotstudien gibt das Werk nicht. | S. 57, Abschn. 1 | Behauptung ohne Beleg im Text |
| Die feinen WordNet-Unterscheidungen erlaubten weder hohe Übereinstimmung noch hohe Systemleistung; das Gruppieren in gröbere Senses habe beides verbessert. | S. 58, Abschn. 4 | referiert (Palmer et al. 2004; Palmer et al. 2006) |
| Sense-Unterscheidungen werden als Hierarchie „similar to a decision tree“ dargestellt, von groben Unterscheidungen bis zu den WordNet-Senses an den Blättern; Senses unter einem Knoten werden zu einem Eintrag zusammengefasst, mit syntaktischen und semantischen Kriterien für die Gruppe, die den Annotator:innen gezeigt werden. | S. 58, Abschn. 4 | eigenes Verfahren |
| **Prüfschleife:** „a 50-sentence sample of instances is annotated and immediately checked for inter-annotator agreement. ITA scores below 90% lead to a revision and clarification of the groupings by the linguist.“ Erst danach wird jede Gruppe an einen Ontologie-Knoten gebunden. | S. 58, Abschn. 4, Abb. 1 | eigenes Verfahren |
| Abb. 1 zeigt den Ablauf pro Wort: Sense-Aufteilung, Definitionen, Kommentar (2 oder 3 Personen), Adjudikation (1 Person), Abgleich mit der Ontologie (1 Person), Testannotation (2 Personen), Übereinstimmung und Konfusionsmatrix; bei „not OK“ zurück zur Sense-Aufteilung, bei „OK“ zur vollen Annotation. In der Abbildung steht der Ontologie-Abgleich **vor** der Testannotation, im Text **nach** bestandener Hürde. | S. 58, Abb. 1 (Seitenbild) | eigenes Verfahren; Widerspruch Text/Abbildung |
| Annotator:innen seien mit den Gruppen mindestens dreimal so produktiv. | S. 58 | eigene Angabe ohne Zahlenbasis |
| Verben: Ziel 700 häufigste Verben; bisher 300 gruppiert, 150 doppelt annotiert. Gruppierungskriterien sind vor allem Subkategorisierungsrahmen und semantische Klassen der Argumente; Beispiel *drive*: 22 WordNet-2.1-Senses, in Abb. 2 vier Gruppen G1 bis G4. | S. 58, Abschn. 4.1, Abb. 2 | eigenes Verfahren |
| Mit den gruppierten Daten erreichten Chen & Palmer (2005) 86,3 % Genauigkeit für Verben, 10 % mehr als zuvor mit ungruppierten, feinen Senses. | S. 59, Abschn. 4.1 | referiert (Chen & Palmer 2005) |
| Nomen: gleiches Verfahren, dieselbe Person erstellt die Nomen-Senses „starting with WordNet and other dictionaries“; Ziel 1100 häufigste polyseme Nomen bis Ende 2006. | S. 59, Abschn. 4.2 | Projektangabe |
| In Wörterbüchern seien Senses „simply listed“; OntoNotes bindet sie an die Ontologie Omega (110.000 Knoten), um Subsumption und Vererbung nutzbar zu machen. Beispiel: G1 und G4 von *drive* unter „controlled motion“, G2 unter „attitudes“. | S. 59, Abschn. 5 | eigenes Vorhaben |
| Koreferenz: doppelt annotiert und adjudiziert; mittlere Übereinstimmung jeder Annotator:in mit dem adjudizierten Ergebnis 91,8 % (normale Koreferenz) und 94,2 % (Appositionen). | S. 59, Abschn. 6 | eigenes Ergebnis (nur Koreferenz) |

## Daten, Methode, Zahlen

- **Korpus:** erster Teil 300K Wörter Englisch, 250K Wörter Chinesisch, Nachrichten (S. 57); Sense-Annotation in einem 300K-Ausschnitt der PropBank (S. 58).
- **Prüfstichprobe pro Wort:** 50 Sätze, Schwelle 90 % ITA (S. 58). Welches Maß „ITA“ ist (Rohübereinstimmung, paarweise oder gegen Adjudikation), sagt das Werk nicht.
- **Umfang bis zum Bericht:** 300 Verben gruppiert, 150 doppelt annotiert (S. 58).
- **Einzige Übereinstimmungswerte im Werk:** 91,8 % und 94,2 %, beide für Koreferenz, gemessen als Übereinstimmung mit dem adjudizierten Ergebnis (S. 59). Für Wortbedeutungen gibt es keinen gemessenen Wert.
- **Systemwert:** 86,3 % für Verben, aus Chen & Palmer 2005 (S. 59).

## Wörtliche Stellen

> „[…] a 50-sentence sample of instances is annotated and immediately checked for inter-annotator agreement. ITA scores below 90% lead to a revision and clarification of the groupings by the linguist.“ (S. 58)

> „The subtle fine-grained sense distinctions in WordNet have not lent themselves to high agreement between human annotators or high automatic tagging performance.“ (S. 58)

> „In standard dictionaries, the senses for each word are simply listed.“ (S. 59)

## Bezug zur Dissertation

**Prüfauftrag zu `goldstandard/LITERATUR-IAA.md`** (Hovy et al. 2006 dort zweimal mit ✔):

1. *Zeile „Typische Werte: feinkörnig (WordNet) ca. 67 bis 72 %, grobkörnig ca. 90 bis 94 %. Zusammenlegen von Senses hob κ von 0,46 auf 0,86 […]“* (Belege Navigli et al. 2007, Hovy et al. 2006, Ng et al. 1999, Artstein & Poesio 2008):
   - **Nicht bei Hovy et al. 2006:** κ 0,46 und 0,86 kommen im Werk nicht vor; es nennt überhaupt keinen κ-Wert. Ebenso keinen feinkörnigen Vergleichswert von 67 bis 72 %.
   - **Vorsicht bei „90 bis 94 %“:** Die einzigen Werte über 90 % im Werk sind 91,8 und 94,2 %, und die gelten für **Koreferenz** (S. 59), nicht für Wortbedeutungen. Für Senses nennt das Werk nur das Ziel 90 % (S. 58). Falls „bis 94 %“ aus diesem Werk stammt, ist es ein Fehlbeleg. Vorschlag: Hovy et al. 2006 in dieser Zeile nur für „Ziel und Prüfschwelle 90 % bei gruppierten Senses“ anführen; die übrigen Zahlen an den anderen Belegen prüfen.
2. *Zeile „OntoNotes: 50 Sätze pro Pilotrunde, Revision bis 90 %.“*
   - **Gedeckt** sind 50 Sätze und die Schwelle 90 % (S. 58).
   - **Präzisierung:** Die 50 Sätze sind eine Stichprobe **pro Wort** („a 50-sentence sample of instances“, Abb. 1 beginnt mit „word“), keine Pilotrunde über viele Lemmata. Überarbeitet werden **die Gruppierungen, also das Inventar**, durch den Linguisten, nicht Richtlinien im Sinne des MATTER-Zyklus. Das Maß hinter „ITA“ ist nicht angegeben.
3. **Protokoll §7, Schritt 2 („OntoNotes verlangte 90 % Rohübereinstimmung“):** „Roh“ steht nicht im Werk; dort steht nur „ITA scores below 90%“ (S. 58). Vorschlag: „OntoNotes verlangte 90 % Übereinstimmung (Maß nicht angegeben)“.

**Weitere Bezüge:**

- **A32, Fall α < 0,67 („Instrument ändern: gröbere Senses oder andere Darbietung“):** OntoNotes ist genau dieser Mechanismus als Regelbetrieb: Wer die Schwelle verfehlt, überarbeitet das Inventar des Wortes und misst neu (S. 58, Abb. 1). Zwei Unterschiede sind für die Begründung wichtig: (a) OntoNotes misst und überarbeitet **pro Wort**, A32 pro Runde über verschiedene Lemmata; ein Rundenwert sagt nicht, welche Lemmata das Problem sind. (b) OntoNotes darf das Inventar selbst bauen; die MHDBDB-Senses sind vorgegeben, eine Vergröberung kann nur auf einer abgeleiteten Ebene geschehen (Oberbegriffe über den Zahlencode, `knowledge/data.md` B11; Protokoll §12, Punkt 12). Das spricht dafür, im Pilot neben α pro Runde die Abweichungen pro Lemma festzuhalten, damit der Fall „gröbere Senses“ gezielt umgesetzt werden kann.
- **Protokoll §9.1, Punkt 7 (vorab definierte grobe Ebene):** Die OntoNotes-Gruppen sind von Hand mit syntaktischen und semantischen Kriterien gebildet (S. 58, Abb. 2), nicht aus einer Taxonomie abgeleitet. Als Präzedenz für eine taxonomische Vergröberung taugt eher Vial et al. 2019; OntoNotes belegt nur, dass grobe Gruppen mit begründenden Kriterien den Annotator:innen gezeigt werden.
- **Vergleichbarkeit mit dem MHDBDB-Inventar:** OntoNotes zeigt Annotator:innen Gruppen **mit** Kriterien, Definitionen und Kommentar (Abb. 1: „creating definitions, commentary“). Die MHDBDB-Karten zeigen nur Begriffsnamen ohne Definition (`knowledge/data.md`, Abschnitt 1; Protokoll §5). Ein OntoNotes-Wert ist daher kein Maßstab für die zu erwartende Übereinstimmung an MHDBDB-Karten.
- **Protokoll §7, Schritt 6 (Adjudikation):** Abb. 1 sieht für die Inventarentwicklung eine einzelne adjudizierende Person vor (S. 58); das ist ein Ablauf für das Inventar, nicht für das Gold, und trägt die Frage in §12, Punkt 2 nicht.
- **Kontamination, LLM-Konfiguration (A17 bis A29):** Das Werk sagt dazu nichts (Stand 2006).

## Grenzen und Einwände

- Vorschau eines laufenden Projekts; für die Sense-Annotation keine gemessenen Übereinstimmungswerte, keine Angabe des Maßes, keine Zahl der durchlaufenen Revisionsrunden.
- „Better than 90% consistency“ der Pilotstudien (S. 57) ist im Text nicht belegt.
- Die Schwelle wird erreicht, indem das Inventar angepasst wird; eine hohe Übereinstimmung ist damit teils eine Eigenschaft der Gruppierung, nicht der Annotator:innen. Für ein vorgegebenes Inventar wie die MHDBDB-Senses ist das nicht übertragbar.
- Widerspruch zwischen Text und Abb. 1 zur Reihenfolge von Ontologie-Abgleich und Testannotation (S. 58).
- Englisch und Chinesisch, Gegenwartssprache, Nachrichtentexte.

## Weiterführend

- Palmer, Babko-Malaya & Dang 2004, Different Sense Granularities for Different Applications (S. 58, 60).
- Palmer, Dang & Fellbaum 2006 (im Werk „to appear“), Making Fine-grained and Coarse-grained Sense Distinctions, *Natural Language Engineering* (S. 58, 60): vermutlich die Quelle für Übereinstimmungswerte vor und nach dem Gruppieren.
- Chen & Palmer 2005, IJCNLP, S. 933 bis 944 (S. 59, 60): Systemwert 86,3 %.
- Philpot, Hovy & Pantel 2005, The Omega Ontology (S. 58, 60).

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF und hat keine Anmerkungen; `markierungen.py` legt keine Datei an.
