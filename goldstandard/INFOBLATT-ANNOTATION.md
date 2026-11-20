# Informationsblatt und Absprache zur Doppelannotation (WSD-Goldstandard)

**Entwurf vom 2026-11-20**, noch nicht von Julia Hintersteiner gegengelesen. Stellen mit **[offen: …]** sind
vor der Weitergabe zu füllen. Das Blatt ersetzt die im DMP (Abschnitt 4) vorgesehene Einwilligung: Die
annotierende Person arbeitet im Arbeitsauftrag ihrer Dienststelle, die Grundlage ist deshalb der Auftrag,
nicht eine Einwilligung (Entscheidung Julia Hintersteiner, 2026-11-20). Es informiert, hält die Absprachen
fest und wird von allen drei Beteiligten bestätigt.

## 1. Worum es geht

Für die Dissertation von Julia Hintersteiner zur Bedeutungsdisambiguierung im Mittelhochdeutschen entsteht
ein Goldstandard: Zwei Personen ordnen unabhängig voneinander Belegstellen aus dem MHDBDB-Korpus einer
Bedeutung des MHDBDB-Inventars zu. Aus der Übereinstimmung der beiden wird gemessen, wie gut sich die
Aufgabe reproduzieren lässt. Die Abweichungen werden anschließend gemeinsam geklärt (Adjudikation).

- **Annotierende:** Julia Hintersteiner und [offen: Name der zweiten Person].
- **Arbeitsauftrag:** Die zweite Person annotiert als Mitarbeiter:in der MHDBDB im Auftrag von Katharina
  Zeppezauer-Wachauer (Universität Salzburg). Die Arbeit gehört zu den Dienstaufgaben; Umfang und
  Zeitbudget: [offen].
- **Ablauf:** zuerst ein Pilot in Runden (Runde 0 mit 15 Belegen, danach Runden zu je 25), dann die
  Hauptrunde. Einzelheiten: `goldstandard/PROTOKOLL.md`, Abschnitt 7.

## 2. Was die Annotationsdatei aufzeichnet

Jede Person bekommt eine eigene HTML-Datei, die ohne Internetverbindung im Browser läuft. Die Datei schickt
nichts ins Netz; gespeichert wird im Browser, bis die Person ihren Stand als JSON-Datei exportiert und
zurückgibt.

Aufgezeichnet werden:

- **die Antworten** je Beleg: Status, gewählte Bedeutungskarten, Sicherheit, Kommentar und die eigene
  Lesart, die vor dem Aufdecken der Karten notiert wird;
- **ein Ereignisprotokoll** jeder Aktion mit Zeitstempel (Datum, Uhrzeit, Zeitzone), Beleg, Art der Aktion,
  gezeigter Kartenreihenfolge und der Angabe, ob der Kontext erweitert war;
- **die Verweildauer** je Beleg, also wie lange ein Beleg geöffnet war;
- **eine Kennung** (`julia` bzw. [offen: Kennung der zweiten Person]), die in der Datei fest eingetragen ist.

Nicht aufgezeichnet werden Name, Login, IP-Adresse, Gerätedaten oder irgendetwas außerhalb der
Annotationsdatei.

## 3. Wozu die Daten dienen

- Die **Antworten** ergeben die Übereinstimmung zwischen den beiden Personen und nach der Adjudikation den
  Goldstandard.
- Das **Ereignisprotokoll** macht nachvollziehbar, wer wann was entschieden hat (Protokoll, Abschnitt 8).
- **Zeitstempel und Verweildauern** dienen nur der Prüfung, ob Ermüdung oder Gewöhnung im Lauf einer
  Sitzung die Urteile verschiebt (Protokoll, Abschnitt 7, Schritt 4).

**Zusage zu Zeitdaten:** Zeitstempel und Verweildauern werden nur zusammengefasst ausgewertet (etwa: Anteil
der Übereinstimmung in der ersten und zweiten Hälfte einer Sitzung). Sie werden nicht zur Bewertung von
Arbeitsleistung, Arbeitszeit oder Arbeitstempo einer Person verwendet und nicht an die Dienststelle
weitergegeben. Veröffentlicht werden sie nur zusammengefasst, nie je Person und Beleg.

## 4. Wer die Daten sieht

- **Julia Hintersteiner** als Verantwortliche für die Auswertung.
- **Die dritte Person** (vorgesehen: Katharina Zeppezauer-Wachauer, Protokoll, Abschnitt 7, Schritt 6) prüft
  einen Teil der Adjudikationen. Sie sieht dabei die Labels, aber nicht, von wem sie stammen.
- **Keine KI-Werkzeuge:** Die Labels werden nicht in eine KI-Sitzung gegeben, auch nicht zur Auswertung.
  Auswertungsskripte zeigen dort nur Kennzahlen (Protokoll, Abschnitt 10, A37).
- Solange die Studie läuft, sind die Labels nicht öffentlich. Grund ist, dass öffentliche Labels in die
  Trainingsdaten künftiger Sprachmodelle geraten könnten, die später an genau diesem Goldstandard gemessen
  werden.

## 5. Ablage

- Rückgabe der Exporte an Julia Hintersteiner per [offen: Weg, z. B. Mail oder Uni-Cloud]. Eingang, Datum
  und Prüfsumme jeder Rückgabe werden festgehalten.
- Ablage in einem privaten Repository [offen: Name] mit einer zweiten Sicherung auf [offen: Speicherort]
  (DMP, Abschnitt 3). Nicht im öffentlichen Fork `juliahin/mhdbdb-wsd`.
- Aufbewahrung: [offen: Dauer; Vorschlag 10 Jahre nach der Publikation, wie für Forschungsdaten nach guter
  wissenschaftlicher Praxis üblich].

## 6. Veröffentlichung

Mit der Publikation wird der Goldstandard auf Zenodo archiviert, die Labels verschlüsselt (Passwort in der
Publikation) und mit einer Lizenz, die Weiterverbreitung im Klartext und Trainingsnutzung ausschließt
(Protokoll, Abschnitt 10). Veröffentlicht werden:

- das Gold nach der Adjudikation;
- **die Labels jeder Person vor der Adjudikation**, je Person unter ihrer Kennung (Protokoll, A36);
- die Lesarten und Kommentare als Rohdaten (A36);
- Zeitdaten nur zusammengefasst (Abschnitt 3 oben).

**Zur Kennung, offen gesagt:** Bei nur zwei Annotierenden, die beide in der Publikation genannt werden,
schützt ein Pseudonym kaum: Wer die Publikation liest, kann die Labels einer Person zuordnen. Die Wahl
unten betrifft deshalb vor allem, wie die Daten beschriftet sind, nicht ob sie zuordenbar sind.

## 7. Nennung

Wie die zweite Person in Publikation und Datensatz genannt wird, legen die Beteiligten gemeinsam fest:

- [ ] Mitautorschaft am Datensatz bzw. am Ressourcenartikel zum Goldstandard
- [ ] Nennung als Annotator:in im Datensatz (Zenodo, Datasheet) und in der Danksagung
- [ ] anders: [offen]

## 8. Rechte

Auskunft, Berichtigung und die übrigen Rechte nach der DSGVO bleiben unberührt. Ansprechperson:
Julia Hintersteiner, [offen: Mailadresse]. Datenschutzstelle: [offen: Datenschutzbeauftragte:r der
zuständigen Universität]. **[offen: Rechtsgrundlage und verantwortliche Stelle von der Datenschutzstelle
bestätigen lassen: Dienstverhältnis bzw. Forschungsaufgabe der Universität Salzburg, und wer
verantwortlich ist, wenn die Daten in die Dissertation an der Universität [offen] eingehen.]**

## 9. Bestätigung

| Wer | Was | Datum | Unterschrift oder Bestätigung per Mail |
|---|---|---|---|
| Katharina Zeppezauer-Wachauer | erteilt den Arbeitsauftrag nach Abschnitt 1 und ist mit Ablage, Veröffentlichung und Nennung nach Abschnitt 5 bis 7 einverstanden | | |
| [offen: zweite Person] | hat das Blatt erhalten und gelesen; Kennung: [offen]; Nennung: Wahl in Abschnitt 7 | | |
| Julia Hintersteiner | sagt die Behandlung nach Abschnitt 3 bis 6 zu | | |
