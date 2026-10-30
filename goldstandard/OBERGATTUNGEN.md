# Obergattungsgruppen für den Gattungsausgleich

**Status:** entschieden von Julia Hintersteiner am 2026-10-30 (Entwurf vom 2026-10-16). Steuert die
Gewichte der Ziehung (Protokoll, Abschnitt 4.4); wird mit Freeze 1 eingefroren. Dateiname und
Skriptname (`obergattungen_entwurf.py`) bleiben.
**Werkzeug:** [`obergattungen_entwurf.py`](obergattungen_entwurf.py). Vorschlag pro Text zum
Durchsehen: `obergattungen/texte.csv`, Zahlen: `obergattungen/zusammenfassung.json`.

## 1. Was die Typologie hergibt

Die Gattungsangaben im Korpus folgen der **MHDBDB-Textreihentypologie** (Zeppezauer-Wachauer und
Heiles; SKOS-Vokabular, als Unterseite unter `textreihen/`). Zwei Regeln der Typologie sind für
uns entscheidend (`textreihen/how-to.html`):

1. Ein Werk kann **mehrere exakte Textreihen** haben (`genreForm`).
2. Zu jeder Textreihe gehört eine **eindeutige Herkunft** (`genreFormMainparent`), die festlegt,
   über welchen Pfad das Werk im polyhierarchischen Baum hängt.

Im TEI-Header steht beides: `<category>` für die Textreihe, `<category ana="parent">` für die
Herkunft. Alle 667 Texte tragen mindestens eine Herkunft (zusammen 889).

**Korrektur einer früheren Angabe.** Im Protokoll stand, die Taxonomie in `genres.xml` sei flach.
Das war falsch. `genres.xml` führt bei jeder Kategorie auch Vorfahren als `broader` (3.175 Zeiger);
nach transitiver Reduktion bleiben 819 direkte. Darunter liegt eine echte Hierarchie: zwei Wurzeln,
**12 Kategorien auf Ebene 1**, bis zu 6 Ebenen Tiefe, 171 Kategorien mit mehr als einem direkten
Elternteil. Ebenfalls falsch war „TRO hat keine Gattung": Der Header nennt Trojaroman mit Herkunft
Antikenroman; die frühere Zählung lief über `works.xml` und hat die Zuordnung verfehlt.

| Wurzel | Ebene 1 (Unterkategorien darunter) |
|---|---|
| Epik, Lyrik und Dramatik | Lyrik (179), Geistliche Literatur (134), Kurzdichtung (120), Großepik (21), Lehrdichtung (14), Dramatik (13), Reiseliteratur (7) |
| Wissensliteratur und Gebrauchsliteratur | Fachliteratur (254), Religiöser Gebrauchstext (62), Mediale Sonderform (60), Historiografie (19), Rechtstext (18), Lehrdichtung (14), Reiseliteratur (7) |

Lehrdichtung und Reiseliteratur hängen unter beiden Wurzeln.

## 2. Vorgeschlagenes Verfahren

**Grundsatz:** Die Gruppen sind die Ebene 1 der Typologie, zusammengelegt nur dort, wo das Korpus
zu dünn ist. So stammt die Einteilung aus einem veröffentlichten, kontrollierten Vokabular und
nicht aus einer Ad-hoc-Entscheidung für diese Stichprobe.

**Pfad:** Von jeder Herkunft eines Textes aufwärts bis zur Ebene 1. Ist die Herkunft selbst eine
Wurzel (ein Fall: NBU, Herkunft „Wissensliteratur und Gebrauchsliteratur"), zählt der Pfad über die
Textreihe (NBU: Historiografie).

**Zuordnung Ebene 1 → Gruppe:**

| Ebene 1 | Gruppe | Anmerkung |
|---|---|---|
| Großepik | Großepik | |
| Lyrik | Lyrik | |
| Kurzdichtung | Kurzdichtung | |
| Dramatik | Kurzdichtung | im Korpus über die Herkunft kein Text; nur zur Vollständigkeit |
| Geistliche Literatur | Geistliche Literatur | |
| Religiöser Gebrauchstext | Geistliche Literatur | allein zu dünn |
| Lehrdichtung | Lehrdichtung | |
| Historiografie | Historiografie | |
| Fachliteratur | Fach- und Rechtsliteratur | allein zu dünn |
| Rechtstext | Fach- und Rechtsliteratur | allein zu dünn |
| Reiseliteratur | Fach- und Rechtsliteratur | im Korpus über die Herkunft kein Text |
| Mediale Sonderform | (keine Gruppe) | beschreibt das Medium, nicht den Inhalt; wird ignoriert, wenn der Text eine andere Gruppe hat |

**Mehrere Gruppen (148 Texte nach Vorrang):** Eine Hauptgruppe nach festem Vorrang, **Inhaltsbereiche vor
Formen**: Geistliche Literatur > Fach- und Rechtsliteratur > Historiografie > Lehrdichtung >
Großepik > Kurzdichtung > Lyrik. Begründung: Für die Verteilung von Wortbedeutungen ist der
Sachbereich (geistlich, fachlich, rechtlich, historisch) vermutlich prägender als die Form, und
genau diese Bereiche sind im Korpus selten. Was die Regel tatsächlich tut:

| Kombination | Texte | Ergebnis | Beispiele |
|---|---|---|---|
| Kurzdichtung + Lyrik | 83 | Kurzdichtung | Schwänke und Mären (Pfad zur Lyrik über „Scherzdichtung"), Minnereden (MR1, MR2), Geistliche Reden |
| Geistliche Literatur + Kurzdichtung + Lyrik | 30 | Geistliche Literatur | Marienleben, Marienmirakel (MFR, JUK, SUM), Minneburg (MNB) |
| Geistliche Literatur + Lyrik | 6 | Geistliche Literatur | |
| Kurzdichtung + Lehrdichtung + Lyrik | 6 | Lehrdichtung | |
| Großepik + Kurzdichtung + Lyrik | 5 | Großepik | Frauendienst (FD, FDS, FLD, FH, FP) |
| Geistliche Literatur + Kurzdichtung | 5 | Geistliche Literatur | |
| übrige Kombinationen | 13 | nach Vorrang | |

Jede Zuordnung steht in `obergattungen/texte.csv` mit Spalte `regel` (eindeutig, vorrang, entschieden, weggelassen). Gemessen am 2026-10-30 aus `zusammenfassung.json`: 514 eindeutig, 148 nach Vorrang, 4 von Julia entschieden (HZU2, HZU, HNI, BAR), 1 weggelassen (SBF); zusammen 667 Texte.

## 3. Ergebnis

Zieltokens der Grundgesamtheit (Protokoll, Abschnitt 3) ohne den weggelassenen Text SBF:
1.434.213 (vorher 1.434.270, Differenz 57 = SBF). Die Zahl gilt auch ohne Ausschluss 4 des
Protokolls (ersetzt am 2026-10-30, A19); er war in ihr nie enthalten. Zielanteil nach
Quadratwurzel-Allokation, erwartete Items bei 360 in der Hauptstichprobe (Stand 2026-10-30,
`obergattungen/zusammenfassung.json`):

| Gruppe | Texte | Anteil im Korpus | Zielanteil | erwartet von 360 | davon Tokens in D1 |
|---|---|---|---|---|---|
| Großepik | 92 | 59,5 % | 33,5 % | 120,7 | 9,4 % |
| Historiografie | 13 | 9,4 % | 13,3 % | 48,0 | 15,2 % |
| Lyrik | 147 | 8,9 % | 12,9 % | 46,6 | 18,6 % |
| Geistliche Literatur | 74 | 7,6 % | 12,0 % | 43,2 | 4,0 % |
| Kurzdichtung | 272 | 6,5 % | 11,1 % | 39,9 | 11,8 % |
| Lehrdichtung | 36 | 5,5 % | 10,2 % | 36,6 | 0,3 % |
| Fach- und Rechtsliteratur | 32 | 2,5 % | 6,9 % | 24,9 | 0,4 % |

Der Anteil im Korpus ist der Tokenanteil der Hauptgruppe, die Zeile „zu prüfen" des Entwurfs
entfällt.

## 4. Was dabei auffällt

1. **Großepik sinkt von 59,5 % auf 33,5 %**, Fach- und Rechtsliteratur steigt von 2,5 % auf 6,9 %.
   Das ist der gewollte Ausgleich.
2. **Historiografie stößt an die Obergrenze pro Text.** 13 Texte zu je höchstens 3 Items ergeben
   höchstens 39, der Zielanteil verlangt 48 (OVG allein trägt den größten Teil der Gruppe). Deshalb
   gilt für Historiografie ausnahmsweise eine Obergrenze von 5 Items pro Text (Entscheidung Julia,
   2026-10-30; Protokoll 4.4, A20): 13 × 5 = höchstens 65, das deckt 48 ab. Ohne Ausnahme hätte OVG
   grob 45 % der Gruppe, mit 5 höchstens etwa 10 %. (Grobe Wasserstandsrechnung mit proportionaler
   Verteilung, keine Ziehungssimulation.)
3. **Die Silberdomäne D1 deckt die seltenen Bereiche fast nicht ab.** In Lehrdichtung (0,3 %),
   Fach- und Rechtsliteratur (0,6 %) und Geistlicher Literatur (4,0 %) liegen kaum Tokens in den
   durchannotierten Texten. Die 30 % D1-Items kommen also fast nur aus Großepik, Historiografie,
   Lyrik und Kurzdichtung, und die **Silberqualität ist für die Sachbereiche nicht messbar**. Das
   gehört als Befund über die Altannotation ins Datasheet und in den Artikel.
4. **Gruppengröße steuert den Ausgleich.** Bei Quadratwurzel-Allokation bekommt eine Gruppe, die man
   in zwei teilt, zusammen mehr als vorher (√a + √b > √(a + b)). Würde man Großepik in ihre
   Unterkategorien aufteilen (Bretonischer Roman, Höfischer Roman, Antikenroman, Heldenepik ...),
   stiege ihr Gesamtanteil wieder. Deshalb bleibt Großepik eine Gruppe; die Unterkategorie steht im
   Manifest und kann ausgewertet werden.

## 5. Entscheidungen (Julia Hintersteiner, 2026-10-30)

Im Entwurf standen vier offene Fragen. Antworten, jeweils mit dem Wortlaut, soweit er etwas festlegt:

1. **Gruppen:** Die sieben Gruppen und die Zusammenlegungen (Religiöser Gebrauchstext zu Geistlicher
   Literatur; Fachliteratur, Rechtstext und Reiseliteratur zusammen) passen. („die anderen punkte passen alle so")
2. **Vorrang:** Inhaltsbereiche vor Formen, in der Reihenfolge von Abschnitt 2, bestätigt.
3. **Die vier Texte ohne Gruppe** (Herkunft nur „Mediale Sonderform"):

   | Sigle | Titel | Zieltokens | Entscheidung |
   |---|---|---|---|
   | HZU2 | Herzogenburger Urkunden | 11.952 | Fach- und Rechtsliteratur |
   | HZU | Herzogenburger Urkunden | 1.422 | Fach- und Rechtsliteratur |
   | HNI | Helmasperger Notariatsinstrument | 187 | Fach- und Rechtsliteratur |
   | SBF | Flugschrift Donnerstein | 57 | weggelassen, aus der Grundgesamtheit genommen |

   („HZU und HZU2 passt, HNI auch und SBF weglassen")
4. **Obergrenze und Historiografie:** Ausnahme ja. Historiografie darf bis zu 5 Items pro Text
   bekommen, sonst bleibt es bei 3 („ja ausnahme für historiographie", „dann 5 pro Text").
5. **Barlaam und Josaphat (BAR) und Apollonius von Tyrus (APO):** Beide landen nur über die
   Vorrangregel bei Historiografie (BAR: Herkunft Historiografie | Höfischer Roman; APO:
   Historiografie | Großepik). Julia: „Barlaam und Josaphat soll nicht dort bleiben. das andere
   schon." APO bleibt Historiografie. **Umsetzung der Hauptsitzung, nicht Wortlaut Julias:** BAR
   wurde der Großepik zugeordnet, der einzigen anderen Gruppe seiner Herkunft. Im Skript steht BAR
   unter `ENTSCHIEDEN`, in `texte.csv` mit `regel = entschieden`.

Folge: Historiografie hat 13 statt 14 Texte, Großepik 92 statt 91, Fach- und Rechtsliteratur 32
statt 29.
