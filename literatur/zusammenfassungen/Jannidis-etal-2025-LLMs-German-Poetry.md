# Jannidis, Kleymann, Schröter & Zinsmeister 2025: Do Large Language Models Understand Literature?

**Datei:** `pdf/Jannidis-etal-2025-LLMs-German-Poetry.pdf` (nur lokal)
**Prüfstatus:** KI-Zusammenfassung aus dem Volltext, von Julia nicht gegengelesen
<!-- später: „von Julia gegengelesen am JJJJ-MM-TT" -->
**Stand:** 2026-10-28, Volltext vollständig gelesen (Textebene, Seiten 1 und 2 auch als Bild); DOI und Erscheinungsdaten über DataCite geprüft, Code-Archiv auf Zenodo geprüft.

**Seitenzählung:** Die Artikelseiten sind von 1 bis 25 durchgezählt (Fußzeile „JCLS 4 (1), 2025“ mit Seitenzahl). Gedruckte Seite = PDF-Seite. Die Seitenmarken in `md/` weichen an Seitenumbrüchen teils um einen Absatz ab; die Seitenangaben hier sind an der Textebene geprüft.

## Bibliografie

- **Vollständig:** Jannidis, Fotis, Rabea Kleymann, Julian Schröter & Heike Zinsmeister, 2025. Do Large Language Models Understand Literature? Case Studies and Probing Experiments on German Poetry. *Journal of Computational Literary Studies* 4(1). 25 Seiten, ohne Seitenzählung im Band.
- **DOI/URL:** https://doi.org/10.48694/jcls.4225 (DOI löst auf `jcls.io/article/id/4225/` auf; die Verlagsseite selbst war am 2026-10-28 durch einen Bot-Schutz gesperrt). DataCite-Eintrag am 2026-10-28 gelesen: Band 4, Heft 1, Jahr 2025, Verlag ULB Darmstadt, Datum „Available“ 2025-12-10. ✔
- **Abweichung in den Daten:** Das PDF nennt „Date published 2025-10-12“, „Date accepted 2025-11-30“, „Date received 2025-02-08“ (S. 1). Veröffentlichung vor Annahme ist widersprüchlich; außerdem nennt Fn. 14 (S. 8) Läufe im November 2025, und Literaturangaben sind „visited on 11/21/2025“ (S. 21 bis 24). DataCite nennt 2025-12-10. Vermutlich ein Zahlendreher im PDF; das ist nicht bestätigt. Für die Zitation genügt das Jahr 2025. ○
- **Code und Daten:** https://github.com/cophi-wue/llms_read_hoelderlin, archiviert unter https://doi.org/10.5281/zenodo.17754274 (S. 21). Zenodo-Eintrag am 2026-10-28 gelesen: „Probing experiments on German poetry“, v3, 28. November 2025, Softwaredokumentation, CC BY 4.0. ✔ Die Notebooks selbst wurden nicht gelesen.
- **Art:** begutachteter Artikel (Konferenzspur der JCLS; begutachtet und auf der 4. CCLS-Konferenz in Krakau im Juli 2025 vorgestellt, S. 1). Gutachter laut PDF: Axel Pichler und eine anonyme Person (S. 1).
- **Sprache:** Englisch

## Worum es geht

Die Arbeit fragt, ob und in welchem Sinn man großen Sprachmodellen „Verstehen“ von Lyrik zuschreiben kann (S. 1 bis 2). Drei Modelle (Claude Sonnet 3.5, Gemini 1.5, GPT4o) bearbeiten Aufgaben zu zwei deutschen Gedichten, Hölderlins *Hälfte des Lebens* (1804) und Hans Pfeifers *Unsere Toten* (1922), zu neun Textaspekten (Metrum, Reim, Assonanz, Lexik, Phrasen, Syntax, Bildsprache, Titel, Bedeutung) auf drei Stufen: Allgemeinwissen, Expertenwissen, Abstraktion und Transfer (S. 3 bis 4). Die Studie ist ausdrücklich explorativ und qualitativ, ohne Zahlen oder Benchmarks (S. 4); theoretischer Rahmen ist Dennetts intentionale Einstellung mit dem Prinzip der wohlwollenden Interpretation (S. 5 bis 7). Ergebnis: Die Modelle sind bei semantischen Aufgaben stark und bei formalen (Silben zählen, Metrum, Assonanz) schwach; die Leistung hängt mehr vom Textaspekt ab als von der Komplexitätsstufe (S. 1, S. 18). Sie bevorzugen etablierte Deutungen, behandeln jede Information im Prompt als relevant und nutzen den passenden kulturellen Kontext erst, wenn er im Prompt genannt wird (S. 19).

## Kernaussagen

| Aussage | Seite/Abschnitt | eigenes Ergebnis oder referiert? |
|---|---|---|
| Die Studie ist explorativ, liefert keine quantitativen Ergebnisse oder Benchmarks und will solche Evaluationen erst vorbereiten. | S. 4, Abschnitt 1 | eigene Festlegung |
| Gewählt wurden ein berühmtes Gedicht, das die Modelle wahrscheinlich samt Deutungen im Training gesehen haben, und ein völlig unbekanntes, nur einmal 1922 gedrucktes und bis dahin nicht digitalisiertes. Damit soll der Störfaktor „im Pretraining gesehen“ wenigstens vorläufig abschätzbar werden. | S. 3, Abschnitt 1 | eigenes Design |
| Kleinere Modelle (≤ 70B) machten in einer Vorstudie zu viele Fehler; untersucht wurden deshalb nur drei große Modelle, meist in Einzelläufen ohne systematische Wiederholung und ohne Variation der Modellparameter. | S. 4 | eigenes Vorgehen |
| Temperatur wurde nicht systematisch variiert; das schränkt die Aussage, die Modelle bevorzugten das Erwartbare, ein. | S. 19, Fn. 20 | eigene Einschränkung |
| Bei Wiederholung mit neueren Modellen (November 2025) änderte sich nichts Grundsätzliches, aber Sonnet 4.5 und ChatGPT 5 erkannten das Skansionsmuster nicht mehr, Gemini 2.5 schon. | S. 8, Fn. 14 | eigenes Ergebnis, nur erwähnt |
| Auf der Stufe Allgemeinwissen ist die erwartete richtige Antwort exakt festlegbar; die Beobachterabhängigkeit ist dort nur ein Randproblem. | S. 8, Abschnitt 3 | eigene Einschätzung |
| Je offener und abstrakter die Aufgabe, desto mehr hängt das Urteil „richtig verstanden“ vom Wohlwollen der Beobachterin ab (Unterbestimmtheit abstrakter Aussagen). | S. 6, S. 15, S. 18, S. 20 | eigene These |
| Für mehrere Experimente wurden akzeptable Antworten vorab festgelegt („pre-registered“). | S. 9 (Assonanz), S. 12 (Reim), S. 12 (Bedingungen für Expertenaufgaben) | eigenes Vorgehen |
| Assonanz: bei den deutschen Gedichten geringe Genauigkeit, bei den englischen Übersetzungen deutlich höhere Precision und Recall, unabhängig von der Definition im Prompt. Eine IPA-Umschrift gelingt, die Assonanz darauf aufzubauen nicht. | S. 9 | eigenes Ergebnis (Tabelle nur im Notebook NB 3) |
| Lexik: Das semantische Feld ausgewählter Nomen und Verben wird von allen Modellen erkannt, die Wortartbestimmung ist teilweise fehlerhaft. | S. 9 | eigenes Ergebnis |
| Mehrdeutige Phrase „im Winde klirren die Fahnen“: Nach Strauss (1965) ist nicht die Stofffahne, sondern die Wetterfahne gemeint. Im Zero-shot-Prompt lagen alle drei Modelle falsch, gemessen an Strauss als Ground Truth. | S. 13, Abschnitt 4 | eigenes Ergebnis; Deutung referiert (Strauss 1965) |
| Den „Knittelvers“ nannten Sonnet und GPT4o nur, wenn nach einem *deutschen* Versmaß gefragt wurde; den kulturellen Horizont wählen die Modelle nicht von selbst. | S. 12 | eigenes Ergebnis |
| Wird Kontext angeboten, behandeln die Modelle alles als relevant; eine Relevanzprüfung (z. B. Warnung vor Anachronismus) findet nicht statt. | S. 14 bis 15; S. 19 | eigenes Ergebnis |
| Zusammengefasst als „culturally sensitive context integration“: (1) alle Informationen im Prompt gelten als relevant, (2) komplexe Argumentation nur, wenn der Prompt sie anstößt, (3) bei einem anderen als dem englischen Kulturkontext arbeiten die Modelle besser, wenn dieser im Prompt steht. | S. 19, Abschnitt 6 | eigenes Ergebnis |
| Historisch-empirische Begründungen für Deutungshypothesen gehören nicht zu den Stärken der Modelle; Grund kann das Trainingsmaterial oder die fehlende Modellierung historischen Weltwissens sein. | S. 19 | eigene Deutung |
| Zwischen bekanntem und unbekanntem Gedicht zeigte sich bei Klangqualitäten kein nennenswerter Unterschied. | S. 16, Abschnitt 5 | eigenes Ergebnis, nicht quantifiziert |
| Weil LLMs stochastisch sind, müssen künftige Arbeiten Verteilungen von Antworten statt Einzelantworten betrachten und Beobachterabhängigkeit kontrollieren statt ignorieren. | S. 7; S. 20 | Forderung |
| Einfache Zählaufgaben sind schwer, weil es viele mögliche Antworten und damit viele Fehlermöglichkeiten gibt; scheinbar komplexe Aufgaben mit kleinem Antwortraum gelingen leichter. Die hohe Einigkeit bei einer Vier-Optionen-Wahl liegt auch am kleinen Antwortraum. | S. 10 bis 11 | eigene Deutung |

## Daten, Methode, Zahlen

- **Texte:** zwei deutsche Gedichte, Hölderlin 1804 und Pfeifer 1922, dazu englische Übersetzungen zum Sprachvergleich (S. 3, Fn. 2). Für Transferaufgaben weitere Gedichte von Eichendorff, Novak und Lenau (S. 16 bis 17). Referenzdeutungen: Strauss (1965) und Schmidt (1982) (S. 3).
- **Modelle:** Claude Sonnet 3.5, Gemini 1.5, GPT4o, über API; Prompts in Python-Skripten und neun Jupyter-Notebooks (NB 1 bis NB 9) im Repositorium (S. 3 bis 4).
- **Umfang:** 9 Aspekte × 3 Stufen × 2 Gedichte = 54 meist mehrstufige Aufgaben (S. 4).
- **Läufe:** in der Regel ein Lauf pro Prompt und Modell, keine systematische Wiederholung (S. 4); keine Temperaturvariation (S. 19, Fn. 20).
- **Bewertung:** diskursiv, keine Tabellen im Artikel (S. 4); teils vorab festgelegte akzeptable Antworten (S. 9, S. 12). Einzige Zahl aus den Ergebnissen im Artikel: alle drei Modelle wählten bei der Vier-Optionen-Aufgabe dieselbe Ergänzung mit Konfidenz 0,9 (S. 10).
- **Menschliche Vergleichsbasis:** keine Annotator:innen, keine Übereinstimmungsmessung. Maßstab sind die Erwartungen der Autor:innen und publizierte Deutungen.

## Wörtliche Stellen

> „we take an exploratory approach in our work and will not present quantitative results or benchmarks“ (S. 4)

> „We usually performed single-run evaluations, meaning that our prompts were run only once across all three models, without systematic repetition.“ (S. 4)

> „On the level of general knowledge, it is easy to exactly define our expectation regarding correct output and thus to evaluate the LLM's accuracy. Observer dependency is only a marginal problem at this level.“ (S. 8)

> „If there is information in the prompt, the models consider all information to be relevant, regardless of whether it is actually relevant.“ (S. 19)

> „If an answer can be found in a cultural context other than the main English one, the models work better if that context is explicitly stated in the prompt.“ (S. 19)

## Julias Markierungen im PDF

17 Hervorhebungen und 1 Notiz, alle auf S. 1 und 2 (`md/Jannidis-etal-2025-LLMs-German-Poetry.markierungen.md`). Aufgenommen: Probing-Design und neun Aspekte auf drei Stufen (Abstract, oben „Worum es geht“), „excel in analyzing semantic aspects but struggle with formal elements“ und „favor established interpretations … unless explicitly prompted“ (Kernaussagen, S. 1 und S. 19), Benchmarking für abstrakte Aufgaben „premature“ (S. 2; Kernaussage zur Beobachterabhängigkeit). Nicht eigens aufgenommen, weil nur referiert: „stochastic parrots“ (Bender et al. 2021), Mirzadeh et al. 2024, Trott et al., Kirschenbaum 2023, Gengnagel et al. 2024, Walsh et al. 2024, Bamman et al. 2024 und Yu et al. 2024 (alle S. 2; siehe „Weiterführend“).

**Julias Notizen im PDF:** S. 2: „maybe als side note: „verstehen“ LLMs Literatur ?“

## Bezug zur Dissertation

- **Prüfauftrag „wo scheitern LLMs bei älterer Sprache“:** Die Arbeit untersucht keine ältere Sprachstufe. Beide Hauptgedichte sind neuhochdeutsch (1804, 1922). Was sie zur Sprachfrage sagt, betrifft Deutsch gegenüber Englisch (Assonanz, S. 9; Standardkontext Englisch, S. 19) und historisches Weltwissen (S. 19). Für Mittelhochdeutsch ist sie daher nur indirekt ein Beleg.
- **Protokoll 4.10 (Freeze 2, LLM-Konfiguration) und `PROMPT-LOG.md` Ebene A:** Die Studie zeigt, was fehlt, wenn man nur einen Lauf ohne Temperaturvariation macht (S. 4, S. 19 Fn. 20), und dass ein Modellwechsel Einzelbefunde umkehren kann (S. 8, Fn. 14). Das stützt die Festlegung von Modell-ID samt Version, Temperatur und Anzahl der Läufe pro Item vor der Hauptrunde.
- **Protokoll 5 und 4.10 (was die Karten und der Prompt enthalten), `knowledge/data.md` B1 und B13:** Wenn Modelle jede Information im Prompt als relevant behandeln (S. 15, S. 19), wirkt alles, was auf einer Karte oder im Kontext steht (Werktitel, offener Punkt 4; KZW-Notizen, B13), auf die Entscheidung. Das ist ein Argument, Zusatzinformation für Mensch und LLM gleich und bewusst festzulegen, und ein weiteres Argument, die Typlisten (B1) aus dem Prompt fernzuhalten.
- **Prompt-Gestaltung (Freeze 2):** Der Befund zum kulturellen Kontext (S. 12, S. 19) spricht dafür, im Prompt Sprachstufe und Epoche ausdrücklich zu nennen, statt sie dem Modell zu überlassen. Ob das hilft, ist für Mittelhochdeutsch nicht gezeigt.
- **Protokoll 9.2 (Nicht-MFS-Items):** Das Fahnen-Beispiel (S. 13) ist ein Anschauungsfall für eine Wortbedeutung, bei der die zuerst naheliegende Lesart nicht die gemeinte ist und alle drei Modelle zero-shot daneben lagen. Ein Einzelfall, keine Messung; als Beispiel für die gesonderte Auswertung auf Nicht-MFS-Items brauchbar, nicht als Beleg.
- **Protokoll 6 und 9.1 (geschlossenes Inventar, Statusliste):** Nach S. 8 ist die Beobachterabhängigkeit bei Aufgaben mit festlegbarer richtiger Antwort gering. WSD mit festem Sense-Inventar ist eine solche Aufgabe; die Arbeit bestätigt damit indirekt, dass das Protokoll nicht in das „open game“-Problem fällt. Die Ausweichlabels (`KEINE_PASST`, `MEHRERE`) halten offene Fälle aus der Genauigkeit heraus.
- **Protokoll 10 (Kontamination):** Die Wahl bekannt gegen unbekannt (S. 3) ist dieselbe Sorge wie in Protokoll 10, aber für Texte, nicht für Labels. Für die MHDBDB sind die Texte öffentlich (Protokoll 10), bekannte Werke dürften im Training liegen. Ob Bekanntheit eines Werks die LLM-Leistung verändert, könnte eine Kovariate sein; die Arbeit selbst findet für Klangqualitäten keinen Unterschied (S. 16), quantifiziert aber nicht. Nur Anregung, kein Protokollinhalt.
- **Einordnung in `goldstandard/LITERATUR-IAA.md` („LLMs bei historischen Sprachen“):** Die Arbeit misst nicht gegen ein Gold, sondern qualitativ. Für den Artikel taugt sie als Kontrast: Eine quantitative Evaluation gegen doppelt annotiertes Gold ist genau das, was die Autor:innen als nächsten Schritt fordern (S. 19 bis 20).

## Grenzen und Einwände

- Zwei Gedichte, drei Modelle, Einzelläufe, keine Zahlen: Die Befunde sind Fallbeobachtungen (S. 4, S. 19). Die Autor:innen sagen das selbst.
- Keine menschlichen Annotator:innen, keine Übereinstimmung; „richtig“ heißt: entspricht den Erwartungen der Autor:innen oder einer publizierten Deutung (z. B. Strauss als Ground Truth, S. 13, von ihnen selbst „perhaps dogmatically“ genannt).
- Keine ältere Sprachstufe, kein Mittelhochdeutsch, keine lexikalische Disambiguierung gegen ein Inventar.
- Die verwendeten Modelle (Stand 2024/2025) sind überholt; Fn. 14 (S. 8) zeigt, dass Einzelbefunde mit neueren Modellen kippen.
- Detailergebnisse (z. B. Tabelle zur Assonanz) stehen nur in den Notebooks, nicht im Artikel (S. 9); sie wurden hier nicht gelesen.
- Widersprüchliche Datumsangaben im PDF (siehe Bibliografie).

## Weiterführend

- Bamman, Chang, Lucy & Zhou 2024, Klassifikation mit LLMs in Cultural Analytics, CHR 2024 (S. 2; Literatur S. 21).
- Hicke et al. 2025, Zero-shot-Annotation von Fokalisierung (S. 2; Literatur S. 22).
- Edman, Schmid & Fraser 2024, CUTE, Tokenverständnis von LLMs, EMNLP 2024 (S. 8; Literatur S. 22): Erklärung für Zählfehler über Tokengrenzen.
- Gengnagel et al. 2024, „Bedeutung in Zeiten großer Sprachmodelle“, DHd 2024 (S. 2; Literatur S. 22); liegt als `pdf/Gengnagel-etal-2024-LLM-Glossary.pdf` vor, ob es dieselbe Arbeit ist, ist nicht geprüft.
- Tong et al. 2024 und Wachowiak & Gromann 2023, Metaphernverständnis von LLMs (S. 10, Fn. 15).
- Yu, Liu & Xiong 2024, LFED, Benchmark zu literarischer Fiktion (S. 2, S. 6; Literatur S. 24).
