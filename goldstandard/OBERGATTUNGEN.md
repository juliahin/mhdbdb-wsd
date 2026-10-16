# Obergattungsgruppen für den Gattungsausgleich: Entwurf zur Prüfung

**Status:** Entwurf vom 2026-10-16, von Julia zu prüfen. Steuert die Gewichte der Ziehung
(Protokoll, Abschnitt 4.4) und muss vor Freeze 1 feststehen.
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

**Mehrere Gruppen (149 Texte):** Eine Hauptgruppe nach festem Vorrang, **Inhaltsbereiche vor
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
| übrige Kombinationen | 14 | nach Vorrang | |

Jede Zuordnung steht in `obergattungen/texte.csv` mit Spalte `regel` (eindeutig, vorrang, pruefen).

## 3. Ergebnis

Zieltokens der Grundgesamtheit (Protokoll, Abschnitt 3): 1.434.270. Zielanteil nach
Quadratwurzel-Allokation, erwartete Items bei 360 in der Hauptstichprobe:

| Gruppe | Texte | Anteil im Korpus | Zielanteil | erwartet von 360 | davon Tokens in D1 |
|---|---|---|---|---|---|
| Großepik | 91 | 58,6 % | 32,2 % | 116 | 9,6 % |
| Historiografie | 14 | 10,4 % | 13,6 % | 49 | 13,8 % |
| Lyrik | 147 | 8,9 % | 12,5 % | 45 | 18,6 % |
| Geistliche Literatur | 74 | 7,6 % | 11,6 % | 42 | 4,0 % |
| Kurzdichtung | 272 | 6,5 % | 10,8 % | 39 | 11,8 % |
| Lehrdichtung | 36 | 5,5 % | 9,9 % | 36 | 0,3 % |
| Fach- und Rechtsliteratur | 29 | 1,6 % | 5,3 % | 19 | 0,6 % |
| zu prüfen (4 Texte, unten) | 4 | 1,0 % | 4,1 % | 15 | 0,4 % |

## 4. Was dabei auffällt

1. **Großepik sinkt von 59 % auf 32 %**, Fach- und Rechtsliteratur steigt von 1,6 % auf 5,3 %.
   Das ist der gewollte Ausgleich.
2. **Historiografie stößt an die Obergrenze pro Text.** 14 Texte zu je höchstens 3 Items ergeben
   höchstens 42, der Zielanteil verlangt 49 (OVG allein trägt den größten Teil der Gruppe). Folge:
   Historiografie bleibt etwas unter dem Ziel; der Rest verteilt sich auf die anderen Gruppen.
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

## 5. Zu entscheiden

1. **Gruppen:** Passen die sieben Gruppen und die Zusammenlegungen (Religiöser Gebrauchstext zu
   Geistlicher Literatur; Fachliteratur, Rechtstext und Reiseliteratur zusammen)?
2. **Vorrang:** Inhaltsbereiche vor Formen, in der Reihenfolge oben?
3. **Die vier Texte ohne Gruppe** (Herkunft nur „Mediale Sonderform"). Vorschlag, bitte prüfen:

   | Sigle | Titel | Textreihe | Zieltokens | Vorschlag |
   |---|---|---|---|---|
   | HZU2 | Herzogenburger Urkunden | (keine) | 11.952 | Fach- und Rechtsliteratur (Urkunden) |
   | HZU | Herzogenburger Urkunden | (keine) | 1.422 | Fach- und Rechtsliteratur (Urkunden) |
   | HNI | Helmasperger Notariatsinstrument | (keine) | 187 | Fach- und Rechtsliteratur (Rechtsdokument) |
   | SBF | Flugschrift Donnerstein | Flugblatt | 57 | unsicher; Ereignisbericht spräche für Historiografie |

4. **Obergrenze und Historiografie:** Soll Historiografie ausnahmsweise mehr als 3 Items pro Text
   bekommen dürfen, um den Zielanteil zu erreichen, oder bleibt die Obergrenze vorrangig
   (Vorschlag: Obergrenze vorrangig, weil sie den Klumpeneffekt begrenzt)?
