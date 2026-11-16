# Gale, Church & Yarowsky 1992: One Sense Per Discourse

**Datei:** `pdf/Gale-etal-1992-One-Sense-Per-Discourse.pdf` (nur lokal; 5 Seiten)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-11-13, ganze Textebene gelesen, Tabellen 1 und 5 am Seitenbild geprüft, DOI aufgelöst. Das lokale PDF ist byte-gleich mit https://aclanthology.org/H92-1045.pdf (SHA-256 verglichen am 2026-11-13); es enthält keine Markierungen.

Seitenzählung: PDF-Seite n = gedruckte S. 232 + n (PDF 1 = S. 233, PDF 5 = S. 237). Unten stehen gedruckte Seiten.

Nicht zu verwechseln mit dem ACL-Beitrag derselben Autoren aus demselben Jahr (`Gale-etal-1992-Upper-Lower-Bounds.md`); Buchstaben „1992a/b/c“ schwanken je Sekundärquelle.

## Bibliografie

- **Vollständig:** Gale, William A., Kenneth W. Church & David Yarowsky (1992). One Sense Per Discourse. In: *Speech and Natural Language: Proceedings of a Workshop Held at Harriman, New York, February 23-26, 1992*. Association for Computational Linguistics, S. 233 bis 237.
- **DOI/URL:** https://doi.org/10.3115/1075527.1075579 (aufgelöst am 2026-11-13, leitet auf das ACM-Portal; Crossref nennt nur Anfangsseite 233, Tagung 23. bis 26.02.1992 in Harriman, NY, und als Bandtitel „Proceedings of the workshop on Speech and Natural Language - HLT '91“); https://aclanthology.org/H92-1045 (BibTeX der Anthology ohne Seiten und ohne DOI). Seiten 233 bis 237 an den gedruckten Seitenzahlen des PDFs abgelesen.
- **Lizenz:** CC BY-NC-SA 3.0 (ACL Anthology, Material vor 2016, laut FAQ der Anthology, abgerufen 2026-11-13).
- **Art:** Workshopbeitrag (DARPA Speech and Natural Language Workshop)
- **Sprache:** Englisch

## Worum es geht

Bei der Arbeit an zwei WSD-Systemen (zweisprachig an den Hansards, einsprachig an Roget und Grolier) fiel den Autoren auf, dass ein polysemes Wort, das in einem gut geschriebenen Diskurs mehrfach vorkommt, fast immer in demselben Sense gebraucht wird (S. 233, S. 235). Ein blinder Versuch mit fünf Urteilenden an Belegpaaren aus Grolier's Encyclopedia bestätigt das: 51 von 54 Paaren aus demselben Artikel haben denselben Sense, also etwa 94 %; unter der Annahme, dass 60 % der Wörter eindeutig sind, ergeben sich 98 % (S. 236). Eine Nachprüfung im Brown Corpus durch den Erstautor ergibt 102 von 106 Paaren (S. 236). Die Autoren schlagen vor, die Diskursbindung als zusätzliche Beschränkung für WSD und als Hilfe beim Erstellen von Testmaterial zu nutzen (S. 236 bis 237).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Frühere WSD-Arbeit war durch knappe handannotierte Test- und Trainingsdaten behindert; statt dessen dienen Übersetzungen in Paralleltexten als Annotation (z. B. *sentence*: *peine* vs. *phrase*). | S. 233, Abschnitt 2.1 | eigenes Verfahren |
| Bayes-Diskriminator über ein Kontextfenster von 100 Wörtern; die Autoren messen Information bis 10.000 Wörter entfernt, das meiste nahe am Zielwort. | S. 233 bis 234, Abschnitt 2.2 | eigenes Verfahren |
| Sechs polyseme Nomen mit Übersetzungspaaren erreichen 82 bis 100 % (Tab. 1). Wörter, die sich über die Übersetzung trennen lassen und in zwei Senses je mindestens 150-mal vorkommen, sind erstaunlich selten. | S. 234, Abschnitt 2.4 | eigenes Ergebnis |
| Yarowsky (1991) trainiert ohne Paralleltext auf Roget-Kategorien (1042 Kategorien) und Grolier; 93 % auf zwölf Wörtern aus der Literatur. | S. 235, Abschnitt 2.5 | referiert (Yarowsky 1991, eingereicht) |
| **Hypothese:** Senses treten in Klumpen auf; zwei Senses eines polysemen Wortes im selben Diskurs sind sehr ungewöhnlich. | S. 235, Abschnitt 3 | eigene Hypothese |
| Vorversuch (nicht blind): 108 zufällig gezogene Nomen, drei Urteilende (die Autoren), 100 Sätze von Belegzeilen je Artikel; nur 6 von 300 Urteilen sahen mehrere Senses. | S. 235 bis 236 | eigenes Ergebnis |
| Blinder Versuch: fünf Urteilende (drei Autoren, zwei Kolleg:innen), OALD-Definitionen, 82 Belegpaare für 9 Nomen; 54 Paare aus demselben Diskurs, 28 Kontrollpaare aus verschiedenen Diskursen, von Hand auf verschiedenen Sense geprüft. | S. 236 | eigenes Versuchsdesign |
| Übereinstimmung mit der Mehrheitsmeinung 96,8 %, ohne Urteilende:n 2 99,1 % (Tab. 4). Die Urteilenden fanden die Entscheidung „quite easy“. | S. 236 | eigenes Ergebnis |
| **Ergebnis:** Von 54 Paaren aus demselben Artikel teilen 51 den Sense (Mehrheitsurteil), 3 nicht; „with probability about 94% (51/54)“ haben zwei polyseme Nomen aus demselben Artikel denselben Sense. Von den 28 Kontrollpaaren beurteilte die Mehrheit nur 1 als gleich (Anm. 3). | S. 236 | eigenes Ergebnis |
| Mit angenommener Mischung von 60 % eindeutigen und 40 % polysemen Wörtern steigt der Wert auf etwa 98 %. | S. 236 | eigene Hochrechnung unter Annahme |
| Brown Corpus (500 Fragmente zu je 2000 Wörtern): 259 Paare; vier der neun Wörter dort nur in einem Sense; für die übrigen fünf 102 von 106 Paaren im selben Sense (etwa 96 %), geprüft allein vom Erstautor. | S. 236 | eigenes Ergebnis |
| Zwei Anwendungen: zusätzliche Beschränkung für WSD-Algorithmen und Hilfe beim Erstellen von Testmaterial, indem alle Belege eines Wortes in einem Diskurs „in one fell swoop“ annotiert werden; das bringt eine kleine, in Kauf genommene Fehlerrate. | S. 236 bis 237, Abschnitte 4 und 5 | eigene Folgerung und Praxis |
| Mit allen Belegen von 97 Wörtern in Grolier's annotiert, zeigen die Autoren: Die meisten Wörter haben nach Typ und Token nur einen Sense, und auch bei polysemen Wörtern ist die Sense-Verteilung meist so schief, dass weit weniger als log2(Senses) Bits nötig sind (Tab. 5). | S. 237 | eigenes Ergebnis |

## Daten, Methode, Zahlen

**Tab. 1 (S. 234, am Seitenbild geprüft):** *duty* (tax 1114 Belege, 97 %; obligation 691, 84 %), *drug* (medical 2992, 84 %; illicit 855, 97 %), *land* (property 1022, 86 %; country 386, 89 %), *language* (medium 3710, 90 %; style 170, 91 %), *position* (place 5177, 82 %; job 577, 86 %), *sentence* (judicial 296, 97 %; grammatical 148, 100 %).

**Tab. 4 (S. 236), Übereinstimmung mit der Mehrheitsmeinung:** wie Tab. 3 des ACL-Beitrags: 100,0 / 87,8 / 98,7 / 100,0 / 97,6 %; Mittel 96,8 %, ohne Urteilende:n 2 99,1 %.

**Tab. 5 (S. 237, am Seitenbild geprüft), Verteilung der Polysemie in 97 Wörtern aus Grolier's:**

| Senses | Typen | Tokens | mittlere Entropie |
|---|---|---|---|
| 1 | 67 | 7569 | 0 |
| 2 | 16 | 2552 | 0,58 |
| 3 | 7 | 1313 | 0,56 |
| 4 | 5 | 1252 | 1,2 |
| 5 | 1 | 1014 | 0,43 |
| 6 | 1 | 594 | 1,3 |

Die Entropie bei 5 Senses (0,43) liegt unter der bei 2 Senses (0,58): Sense-Zahl und Schiefe gehen nicht parallel.

## Wörtliche Stellen

> „We conclude that with probability about 94% (51/54), two polysemous nouns drawn from the same article will have the same sense.“ (S. 236)

> „[…] there is a very strong tendency (98%) for multiple uses of a word to share the same sense in well-written coherent discourse.“ (S. 236)

> „Even for those words that do have more than one possible sense, it rarely takes anywhere near log2senses bits to select the appropriate sense since the distribution of senses is generally quite skewed.“ (S. 237)

## Bezug zur Dissertation

**Prüfauftrag zu `goldstandard/LITERATUR-STICHPROBE.md`** (Zeile „One sense per discourse“, dort mit ✔ und H92-1045 zitiert):

- *„zwei Belege eines polysemen Nomens im selben Text haben zu 94 % denselben Sense“* ist **gedeckt** (S. 236, 51/54). Einschränkungen, die beim Zitieren mitgenannt werden sollten: 9 Nomen, 54 Paare, „Text“ = Artikel einer Enzyklopädie, Urteil der Mehrheit von fünf Personen, darunter die drei Autoren. Die 98 % beruhen auf einer angenommenen Mischung mit eindeutigen Wörtern, nicht auf Messung.
- Im ACL-Beitrag derselben Autoren steht für dieselben 54 Paare 96,9 % (Upper-Lower-Bounds, S. 255). Für das Protokoll trägt die hier nachvollziehbare Zahl (51/54).

**PROTOKOLL §4.4, Punkt 4 („Die Grenze hält den Klumpeneffekt klein (Gale, Church & Yarowsky 1992)“):** Das Werk belegt einen Klumpeneffekt **desselben Wortes** im selben Text. Diesen Effekt schließt das Design schon anders aus: Die Hauptstichprobe zieht 1 Token pro Paar aus Lemma und Wortart (§4.2), das Lemma-Panel nimmt 5 Tokens aus 5 verschiedenen Texten (§4.5). Die Obergrenze von 3 Items pro Text betrifft dagegen **verschiedene** Lemmata im selben Text; darüber sagt das Werk nichts. Vorschlag: in §4.4 Gale et al. als Beleg für „1 Token pro Paar“ und für die Panelregel anführen (S. 236), die Obergrenze pro Text mit der Abhängigkeit von Tokens desselben Textes begründen (Bootstrap nach Text, §9.1 Punkt 5; Evert 2006 in `LITERATUR-STICHPROBE.md`), nicht mit Gale et al. Die Folge-Spalte in `LITERATUR-STICHPROBE.md` („1 Token pro Lemma vermeidet den stärksten Klumpeneffekt“) ist schon in diesem Sinn formuliert.

**Weitere Bezüge:**

- **PROTOKOLL §4.3 (Schiefe statt Sense-Zahl):** Tab. 5 (S. 237) zeigt, dass mittlere Entropie und Sense-Zahl nicht parallel laufen, und die Autoren sagen ausdrücklich, dass schiefe Verteilungen die Aufgabe erleichtern. Das stützt, MFS-Anteil und Entropie pro Item als Kovariaten mitzuführen.
- **PROTOKOLL §3 und §4.3 (nur polyseme Lemmata):** 67 von 97 zufällig gezogenen Nomen waren eindeutig (S. 237). Das Protokoll schließt monoseme Lemmata aus; Werte aus der Dissertation sind daher mit Werten über alle Wörter (wie hier die 98 %) nicht vergleichbar.
- **PROTOKOLL §7 und §9.2 (Gold):** Die Abkürzung „alle Belege eines Diskurses auf einmal annotieren“ (S. 237) erzeugt ein „approximate ground truth“ mit bekannter Fehlerrate. Für das Gold der Dissertation ist das keine Option, weil pro Lemma und Text meist nur ein Token gezogen wird; das Werk eignet sich aber als Kontrast, warum ein Einzelbeleg-Gold teurer ist.
- **LLM-Konfiguration (§4.10):** Falls das LLM mehrere Belege desselben Lemmas aus einem Text sähe (etwa im erweiterten Kontext), könnte die Diskursbindung als Hinweis wirken. Mit 1 Token pro Paar betrifft das nur den Kontextausschnitt, nicht die Stichprobe.

## Grenzen und Einwände

- Kleine Datenbasis: 9 Nomen, 54 Paare; die Brown-Prüfung stammt von einer Person, dem Erstautor.
- Die Urteilenden sind überwiegend die Autoren, die die Hypothese aufgestellt hatten; das Kontrolldesign (28 Paare) soll Zustimmungsneigung abfangen, beseitigt aber nicht die Kenntnis der Hypothese.
- „Discourse“ ist ein Enzyklopädieartikel; die Autoren beschränken die Aussage selbst auf „well-written coherent discourse“ (S. 236). Ob sie für lange mittelhochdeutsche Erzähltexte, Sammelhandschriften oder Lyrikkorpora gilt, ist offen; in Großepik mit tausenden Versen ist „Text“ eine viel größere Einheit als ein Artikel.
- Nur Nomen, nur grobe Senses (Übersetzungs- bzw. OALD-Unterscheidungen); bei feinen Senses und bei Verben dürfte die Bindung schwächer sein, das zeigt das Werk aber nicht.
- Keine Zufallskorrektur, keine Intervalle.

## Weiterführend

- Gale, Church & Yarowsky (1992), Estimating Upper and Lower Bounds, ACL: liegt als PDF vor; dort dasselbe Experiment mit abweichender Zahl.
- Yarowsky (1991/1992), Roget-Kategorien (S. 235, S. 237): Thesaurus-Kategorien als Inventar.
- Gale, Church & Yarowsky (1992), „Discrimination Decisions for 100,000-Dimensional Spaces“, AT&T Statistical Research Report No. 103 (S. 237): Methode.
- Für die Gegenposition und Einschränkungen der Diskurshypothese wäre Literatur nach 1992 nötig; das Werk selbst nennt keine.

## Julias Markierungen im PDF

Keine. Das lokale PDF ist byte-gleich mit dem Anthology-PDF; `markierungen.py` legt keine Datei an.
