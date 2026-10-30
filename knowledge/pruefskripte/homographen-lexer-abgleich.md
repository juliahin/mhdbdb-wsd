<!-- Kopf (2026-10-30, Protokollant): Kopie des Abgleichs von Agent `quellen` (Claude Opus 5.5, 2026-10-30) gegen Lexer im Wörterbuchnetz
für die Liste in homographen-stichprobe.md. Inhalt unverändert. Prüfstatus: Deutungen eines Agenten, von Julia NICHT gegengelesen.
Nachgezählt: Klassenzahlen (P 20, davon P* 5; H 2; V 9; N 1) und Wilson-Grenzen stimmen. Lexer-Artikel nicht stichprobenartig gegengeprüft. -->

# Lexer-Abgleich: Homographen in der MHDBDB-Stichprobe

**Datum:** 2026-10-30
**Quelle der Stichprobe:** `stichprobe-homographen.md` (32 Einträge mit >=2 Bedeutungen, 8 je Frequenzband, Seed 20261030).
**Quelle für Lexer:** Matthias Lexer, Mittelhochdeutsches Handwörterbuch, im Trierer Wörterbuchnetz, abgefragt über die offene Schnittstelle `https://api.woerterbuchnetz.de/open-api/dictionaries/Lexer/...` (Stichwortsuche `lemmata/<form>`, Artikeltext über `kwic/<textid>`); Nachträge über das Sigle `LexerN`. Verlinkt ist jeweils der Artikel unter `https://woerterbuchnetz.de/?sigle=Lexer&lemid=<ID>`.

**Vorgehen.** Für jede Lemmaform habe ich alle Lexer-Stichwörter gleicher Schreibung gesucht (die Stichwortsuche ignoriert Längenzeichen, ë/e und z/ʒ, findet also z. B. zu `wellen` auch `wëllen`) und von jedem Treffer den Artikelanfang gelesen, bei Bedarf weitere Abschnitte. Dann habe ich jede MHDBDB-Bedeutung über ihre Konzeptbezeichnungen und Wortformen einem Stichwort zugeordnet oder als nicht zuordenbar markiert. Die Zuordnung über Konzeptbündel ist eine Deutung; wo Lexer nur ein passendes Stichwort hat, ist H ausgeschlossen, und eine nicht zuordenbare Bedeutung senkt dann nur die Sicherheit.

**Grenzen der Lesung.** Die `kwic`-Schnittstelle liefert je Aufruf etwa 25 Textpositionen, lässt Teile des Markups (oft Stellenangaben) aus und springt bei manchen Positionen auf den Artikelanfang zurück. Lange Artikel (schrîben, schüten, rinc, geselle, lâʒen) habe ich deshalb nur teilweise gelesen; das steht im jeweiligen Block.

**Zusatzmarke P\*.** Einige Einträge vereinen zwei oder mehr Lexer-Stichwörter derselben Wortfamilie (Adjektiv, Adverb, Abstraktum, substantivierter Infinitiv) oder eine reine Variante (stv./swv.), deren Bedeutungen sich nicht trennen: Eine MHDBDB-Bedeutung trägt dann Formen beider Stichwörter. Das ist keine Homonymie im Sinn der Frage, aber formal „mehr als ein Lexer-Stichwort“. Ich zähle sie als P und weise sie getrennt aus, damit die Quote in beiden Lesarten nachrechenbar ist.

## Übersicht

| S | Lemma | ID | Band | Klasse | Lexer-Stichwörter (gleiche Schreibung) | Sicherheit |
|---|---|---|---|---|---|---|
| S01 | zwispeltic | lemma_48510 | 1-3 | P | zwi-speltic adj. (Z02559); zwi-spëltic adv. (Z02560) | mittel |
| S02 | vawir | lemma_25011 | 1-3 | V | (vâ + wir); Bestandteil vâhen stv. (V00048) | hoch |
| S03 | sîhez | lemma_49250 | 1-3 | V | (sîhe + ez); Bestandteil sîhen stv. (S04176) | mittel |
| S04 | zeschrîben | lemma_33286 | 1-3 | V | (ze + schrîben); Bestandteil schrîben stv./swv. (S02563) | hoch |
| S05 | zegewizzen | lemma_39592 | 1-3 | V | kein Stichwort; Bestandteil ge-wiʒʒen (G04217 part. adj., G04218 an. v., G04219 stn., G04220 stf.) | mittel |
| S06 | schüttets | lemma_12402 | 1-3 | V | (schüttet + ez); Bestandteile schüten/schütten swv. (S03012), evtl. schützen swv. (S03034) | mittel |
| S07 | stoufes | lemma_8742 | 1-3 | V | ((de)s + toufes); Bestandteile touf stm. (T01266), toufe stf. (T01271) | mittel |
| S08 | heilwertec | lemma_46449 | 1-3 | P | heil-wertec adj. (H01156) | mittel |
| S09 | muosen | lemma_4262 | 4-20 | **H** (innerhalb VRB) | muosen swv. „essen“ (M03272); muosen swv. „musivisch verzieren“ (M03273) | hoch |
| S10 | brâme | lemma_827 | 4-20 | P | brâme swm. (B03700) | niedrig |
| S11 | zerspannen | lemma_17550 | 4-20 | P\* | zer-spannen stv. (Z00726); zer-spannen swv. = zerspennen (Z00727) | hoch |
| S12 | ûzlâzen | lemma_45997 | 4-20 | N | kein Stichwort (nur ûʒ-lâʒ stm. U06253; Grundwort lâʒen L00519) | hoch (dass kein Stichwort) |
| S13 | stërnesëhen | lemma_17816 | 4-20 | P | stërne-sëhende part. adj. (S07494) | mittel |
| S14 | übergiuden | lemma_13959 | 4-20 | P | über-giuden swv. (U00211) | mittel |
| S15 | geregen | lemma_2155 | 4-20 | P | ge-regen swv. (G02366); daneben ge-rëgen stn. „Regenguss“ (G02365), im Menü nicht vertreten | mittel |
| S16 | schurz | lemma_18745 | 4-20 | P | schurz stm. „Schurz“ (S02992); daneben schurz adj. (S02991), schurz stm. „Sprung“ (S02993), im Menü nicht vertreten | hoch |
| S17 | nüehtern | lemma_4433 | 21-200 | P | nüehtern adj. (N01528) | hoch |
| S18 | zedienest | lemma_15825 | 21-200 | V | (ze + dienest); Bestandteil dienest stm. „Diener“ (D00387), stmn. „Dienst“ (D00388) | hoch |
| S19 | wallen | lemma_7374 | 21-200 | **H** (innerhalb VRB) | wallen stv. „wogen, sieden“ (W00324); wallen swv. „pilgern“ (W00325); wallen stn. (W00326) | hoch |
| S20 | zunrechte | lemma_16022 | 21-200 | V | (ze + unrehte); Bestandteil un-rëht adj. (U04351), stn. (U04352) | hoch |
| S21 | beheben | lemma_16425 | 21-200 | P | be-heben stv. (B00746) | mittel |
| S22 | unbetwungen | lemma_13434 | 21-200 | P | un-betwungen part. adj. (U02193) | hoch |
| S23 | decke | lemma_1100 | 21-200 | P | decke stf. (D00146) | hoch |
| S24 | güften | lemma_2554 | 21-200 | P | güften swv. (G05985); güften stn. (G05986) | mittel |
| S25 | geselle | lemma_2213 | >200 | P | ge-selle swm. (G02918); ge-selle swf. (G02919) | hoch |
| S26 | ungemuot | lemma_6538 | >200 | P\* | un-gemuot adj. (U03341), stm. (U03340), part. adj. „unbeschwert“ (U03342); un-gemüete stn. (U03336) | mittel |
| S27 | melden | lemma_4070 | >200 | P\* | mëlden swv. (M01154), stn. (M01155), stf. = mëlde (M01153) | mittel |
| S28 | enwellen | lemma_8299 | >200 | V | (en + wellen); Bestandteile wellen an. v. „wollen“ (W01585), wëllen stv. „runden, wälzen“ (W01586) u. a. | hoch |
| S29 | verre | lemma_6913 | >200 | P\* | vërre adj. (V02185), adv. (V02186), stf. „Ferne“ (V02187/V03919); verre swm. (V02188) | mittel |
| S30 | rinc | lemma_4917 | >200 | P | rinc stm. (R01267) | hoch |
| S31 | spæhe | lemma_5633 | >200 | P\* | spæhe adj. (S05968), adv. (S05969), stf. (S05970) | mittel |
| S32 | bein | lemma_471 | >200 | P | bein stn. (B00864) | hoch |

## Auszählung

| Band | P (davon P\*) | H | V | N | U | weder V noch N |
|---|---|---|---|---|---|---|
| 1-3 | 2 (0) | 0 | 6 | 0 | 0 | 2 |
| 4-20 | 6 (1) | 1 | 0 | 1 | 0 | 7 |
| 21-200 | 5 (0) | 1 | 2 | 0 | 0 | 6 |
| >200 | 7 (4) | 0 | 1 | 0 | 0 | 7 |
| **gesamt** | **20 (5)** | **2** | **9** | **1** | **0** | **22** |

**H-Quote** unter den 22 Einträgen, die weder V noch N sind: **2 von 22 = 9,1 %** (Wilson-95-%-Intervall rund 2,5 % bis 27,8 %). Beide H-Fälle (muosen, wallen) vereinen Verben gleicher Wortart; über Wortartgrenzen trat kein H-Fall auf.

**Lesart „mehr als ein Lexer-Stichwort“** (P\* mitgezählt): 7 von 22 = 31,8 % (Wilson rund 16,4 % bis 52,7 %). Die fünf P\*-Fälle sind keine Homonyme: Adjektiv mit Adverb, Abstraktum oder substantiviertem Infinitiv derselben Bedeutung, bzw. eine stv./swv.-Variante.

Die Stichprobe ist nach Band geschichtet mit gleichen Fallzahlen, die Bänder sind aber verschieden groß (3106, 1913, 1629, 979). Die Quote ist ungewichtet. Gewichtet man den H-Anteil je Band (bezogen auf alle 8 Einträge des Bandes) mit den Bandgrößen, ergibt sich grob 5,8 % aller Einträge mit >=2 Bedeutungen und >=1 Beleg; bei zwei Treffern ist das nur eine Größenordnung.

## Einträge

### S01 zwispeltic (lemma_48510, ADJ NUM)
- Lexer: zwi-speltic, zwi-spaltic adj. „zwiespältig“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=Z02559 ; zwi-spëltic adv. „= zwispilde“ (1 Beleg, 1296), https://woerterbuchnetz.de/?sigle=Lexer&lemid=Z02560
- 76125 (Gestalt/Formen/Mengenbegriffe/Raum) → adj. „zwiespältig“ im Sinn von zweigeteilt.
- 76126 (Widerspruch/Moral) → adj. „zwiespältig“ im Sinn von uneins, schwankend.
- Klasse P: beide Bedeutungen adjektivisch; das Adverb spielt im Menü keine Rolle. Sicherheit mittel, weil Lexer nur die Glosse „zwiespältig“ gibt.

### S02 vawir (lemma_25011, PRO VRB)
- Verschmelzung vâ (Imp./Konj. zu vâhen) + wir. Lexer: vâhen, vân stv. red., https://woerterbuchnetz.de/?sigle=Lexer&lemid=V00048 (nur Artikelanfang gelesen).
- Alle sieben Bedeutungen tragen Wortformen von vâhen (gevangen, vieng, vâhen …), sind also Bedeutungen dieses Verbs (fangen, gefangen nehmen, ergreifen, jagen).
- Klasse V.

### S03 sîhez (lemma_49250, PRO VRB)
- Verschmelzung sîhe + ez. Lexer: sîhen stv. II „tr. seihen, colare … intr. tröpfelnd durch etw. sickern, fliessen“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=S04176
- 77359, 77360 (Gewässer/Vergehen/Bewegung) → sîhen intr. „sickern, fliessen“, „Vergehen“ evtl. versiegen (Deutung).
- 77361 (Gewässer/Handarbeit) und 77362 (Nahrungszubereitung/Chem.) → sîhen tr. „seihen“.
- Klasse V. Bestandteil: ein Stichwort.

### S04 zeschrîben (lemma_33286, PRP VRB)
- ze + schrîben. Lexer: schrîben stv. II, swv. „schreiben, aufschreiben, verzeichnen, voll schreiben, beschreiben …“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=S02563 (nur Anfang gelesen).
- Schriftliche Kommunikation, Zahlen (verzeichnen), Autorität/Anordnung (vorschreiben) passen zu schrîben; Bildende Kunst (malen), Kriegswesen und Stimmlicher Ausdruck im gelesenen Teil nicht belegt.
- Klasse V. Bestandteil: ein Stichwort.

### S05 zegewizzen (lemma_39592, ADV)
- Kein Lexer-Stichwort (`lemmata/zegewizzen`: 0 Treffer). ze + gewizzen. Lexer: ge-wiʒʒen part. adj. „bekannt“ (G04217), an. v. (G04218), stn. „wissen, kenntnis, erkenntnis“ (G04219), stf. „das wissen, die kenntnis, kunde …“ (G04220), z. B. https://woerterbuchnetz.de/?sigle=Lexer&lemid=G04220
- 61772 (Wissen/Erinnerung) → gewiʒʒen stn./stf. „Wissen“.
- 61773 (Moralisches Empfinden/Etikette) → nicht zuordenbar im gelesenen Teil (ob die stf. auch „Gewissen“ führt, habe ich nicht erreicht).
- Klasse V (Präpositionalfügung, als ADV getaggt).

### S06 schüttets (lemma_12402, PRO VRB)
- schüttet + ez. Lexer: schüten, schütten swv. „in schwingende bewegung setzen, schwingen, schütteln, erschüttern“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=S03012 ; schützen swv. „auf-, ein-, umdämmen“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=S03034
- 19544 (Bewegung) → schüten „schütteln“.
- 19545 (Anlagen am Wasser) → „dämmen“; steht bei Lexer unter schützen, ob auch unter schüten („aufschütten“), habe ich im gelesenen Teil nicht gefunden.
- 19543 (Hilfeleistung/Rüstung) → nicht sicher zuordenbar (evtl. schützen „beschützen“).
- Klasse V. Bestandteile möglicherweise zwei Stichwörter (schüten, schützen), aber nicht gleicher Schreibung.

### S07 stoufes (lemma_8742, ART NOM)
- (de)s + toufes. Lexer: touf stm. „untertauchung, tiefe … meerestiefe, in welcher Pharao versank … ; taufe, baptisma“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=T01266 ; toufe, touf stf. „taufe“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=T01271
- 86858 (Taufe) → touf stm. bzw. toufe stf.; 86859 (Meer/Ausdehnung) → touf stm. „Tiefe“; 86860 (Kultgegenstände, Taufstein?) → touf/toufe (Deutung).
- Klasse V. Bemerkenswert: Lexer selbst führt „Tiefe“ und „Taufe“ unter einem Stichwort touf stm.

### S08 heilwertec (lemma_46449, ADJ)
- Lexer: heil-wertec adj. „heilbringend, salubris“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=H01156
- 72905 (Gesundheit/Vorteil), 72906 (Glückseligkeit/Judäo-christlich) → „heilbringend“ (leiblich bzw. geistlich).
- 72907 (Ästhetisches Empfinden/Vorteil) → nicht sicher zuordenbar.
- Klasse P.

### S09 muosen (lemma_4262, VRB)
- Lexer: muosen swv. „intr. essen, eine malzeit halten“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=M03272 ; muosen swv. „md. mûsen: als mosaik einlegen, musivisch verzieren“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=M03273
- 6667 (Schmuck/Handarbeit, Form gemuoset), 6668 (Bildende Kunst), 6670 (Gebäude) → M03273 „musivisch verzieren“.
- 77390 (Nahrungszubereitung/Speisen), 77391 (Mahlzeiten/Ernährung) → M03272 „essen, Mahlzeit halten“.
- Klasse **H**, innerhalb einer Wortart (zwei swv.).

### S10 brâme (lemma_827, NOM)
- Lexer: brâme swm. „dornstrauch“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=B03700 (Suche `br*m*`: kein weiteres Stichwort gleicher Schreibung).
- 1344 (Büsche) → brâme „Dornstrauch“.
- 1345 (Bäume/Holzverarbeitung/Materialien) → nicht zuordenbar.
- Klasse P mangels zweitem Stichwort; Sicherheit niedrig, weil die Hälfte des Menüs keinen Halt bei Lexer hat.

### S11 zerspannen (lemma_17550, VRB)
- Lexer: zer-spannen stv. „auseinander spannen, dehnen“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=Z00726 ; zer-spannen swv. „s. zerspennen“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=Z00727 ; zer-spennen swv. „s. v. a. zerspannen“ (Z00731).
- 29922, 29923 (beide Ausdehnung) → „auseinanderspannen“; Trennung nach stv./swv. nicht möglich.
- Klasse P\* (Variante gleicher Bedeutung).

### S12 ûzlâzen (lemma_45997, PRP VRB)
- Kein Stichwort in Lexer und LexerN (`lemmata/ûʒlâʒen`, `uzlazen`: 0 Treffer; unter `ûʒ-l*` nur ûʒ-lâʒ stm. U06253). Lexer behandelt Partikelverben wohl unter dem Grundwort lâʒen stv. (https://woerterbuchnetz.de/?sigle=Lexer&lemid=L00519), dort nicht gesucht.
- 71994 (Erlaubnis/Aufgabe), 71996 (Besitz/Lehenswesen/Recht) → plausibel ein Verb „aus-, freilassen; (rechtlich) überlassen“, aber nicht an Lexer geprüft.
- Klasse N (nicht bei Lexer als Stichwort).

### S13 stërnesëhen (lemma_17816, VRB)
- Lexer: kein Verb; stërne-sëhende part. adj. (nur Stellenangabe j.Tit. 5934), https://woerterbuchnetz.de/?sigle=Lexer&lemid=S07494
- 30231 (Wahrnehmung/Astronomie) und 92896 (Übersinnliche Wahrnehmung/Astrologie) → dasselbe Wort, Sternbeobachtung bzw. -deutung.
- Klasse P.

### S14 übergiuden (lemma_13959, NOM PRP VRB)
- Lexer: über-giuden swv. „übermässig, vollständig rühmen, preisen … ; im rühmen, grosstun übertreffen“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=U00211
- 23054, 27863 (Respekt/Ehre) → „rühmen, preisen“; 23055 (Stimmlicher Ausdruck), 36457 (Täuschung/Enthusiasmus/Geräusche) → „grosstun“.
- 36456 (Handel/Finanzen/Verhältnis) → nicht zuordenbar im gelesenen Teil.
- Klasse P.

### S15 geregen (lemma_2155, VRB)
- Lexer: ge-regen swv. „regen, bewegen“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=G02366 ; ge-rëgen stn. „s. gerigene“ = „starker regen, regenguss“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=G02365
- 3358, 3359 (Bewegung, objekt- bzw. selbstbezogen) → ge-regen swv.
- 3360 (Rechtswesen) → nicht zuordenbar (Deutung „anregen, vorbringen“ möglich, bei Lexer nicht gelesen); jedenfalls nicht ge-rëgen „Regenguss“.
- Klasse P.

### S16 schurz (lemma_18745, NOM VRB)
- Lexer: schurz adj. „abgeschnitten, kurz“ (S02991), schurz stm. „kleid, das nur einen teil des untern leibes deckt“ (https://woerterbuchnetz.de/?sigle=Lexer&lemid=S02992), schurz stm. „sprung, lauf“ (S02993).
- 31519 (Männer-Oberbekleidung/Rüstung), 72904 (Frauenbekleidung) → schurz stm. S02992.
- Klasse P. Die echten Homographen (adj., „Sprung“) fehlen im Menü.

### S17 nüehtern (lemma_4433, ADJ ADV)
- Lexer: nüehtern, nüehter adj. „nüchtern, des morgens od. seit dem morgen weder speise noch trank zu sich nehmend“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=N01528
- 6913 (Ernährung/Mangel) → „nüchtern“ im Sinn von nüchternem Magen; 93182 (Getränke/Genussmittel) und 93183 (Ruhe/Charakter) im gelesenen Anfang nicht ausdrücklich, aber kein zweites Stichwort.
- Klasse P.

### S18 zedienest (lemma_15825, NOM PRP)
- ze + dienest. Lexer: dienest, dienst stm. „diener“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=D00387 ; stmn. „dienst: verehrung …“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=D00388
- Alle vier Bedeutungen (Frauendienst, Gottesdienst, Lehensdienst, Arbeit) → dienest stmn. „Dienst“; der Begriff „Dienstklasse“ in 26080/26082 verweist eher auf Personen, ist aber im Bündel nur ein Zeiger.
- Klasse V.

### S19 wallen (lemma_7374, NOM VRB)
- Lexer: wallen stv. red. „wallen, aufwallen, -kochen, sprudeln, wogen, intr. (eigentl. u. bildl.)“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=W00324 ; wallen swv. „wallen, wandern, pilgern“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=W00325 ; wallen stn., https://woerterbuchnetz.de/?sigle=Lexer&lemid=W00326
- 11980 (Reisen/Christliche Riten) → wallen swv. „pilgern“.
- 11983 (Gewässer/Bewegung), 25171 (Temperatur/Chem.), 52708 (Gemütszustand/Erregung) → wallen stv. „wogen, aufkochen“ bzw. „bildl.“.
- Klasse **H**, innerhalb einer Wortart (stv. und swv.).

### S20 zunrechte (lemma_16022, ADJ ADV NEG PRP)
- ze + unrehte. Lexer führt die Fügung unter un-rëht stn. „unrecht, ungerechtigkeit, ungebühr … (ze unrehte, nach ungebühr Er. 4640)“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=U04352 ; daneben un-rëht adj. (U04351).
- Alle drei Bedeutungen → „zu Unrecht, ungebührlich“.
- Klasse V.

### S21 beheben (lemma_16425, VRB)
- Lexer: be-heben stv. „über etw. hinwegheben, wegnehmen … ; erhalten, erwerben ; behalten, behaupten“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=B00746
- 28234 (Kampftechnik/Bewegung) → „hinwegheben, wegnehmen“ oder „behaupten“ (Deutung); 28235 (Wille/Besitz) → „erhalten, erwerben, behalten“; 28237 (Recht/Kommunikation) und 28238 (Ehre/Fähigkeiten) → „behaupten“ (Deutung).
- Klasse P.

### S22 unbetwungen (lemma_13434, ADJ ADV NEG)
- Lexer: un-betwungen part. adj. „unbedrängt, ohne kummer u. sorge … mit gen. (in bezug auf)“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=U02193
- 21940 (Autorität/Kampf) → „unbezwungen, unbedrängt“; 78752 (Mangel/Ausdehnung/Raum) → nicht sicher zuordenbar.
- Klasse P.

### S23 decke (lemma_1100, NOM)
- Lexer: decke stf. „decke, bedeckung, allgem.“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=D00146
- 1744 (Pferd), 1745 (Stoffe), 1746 (Wäsche), 73485 (Gebäude) → jeweils Decke als Bedeckung.
- Klasse P.

### S24 güften (lemma_2554, VRB)
- Lexer: güften swv. „intr. seine freude laut äussern, übermütig sein“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=G05985 ; güften stn. (substantivierter Infinitiv), https://woerterbuchnetz.de/?sigle=Lexer&lemid=G05986
- 4094 (Freude/Enthusiasmus/Stimme) → „Freude laut äussern“; 4095 (Ehre/Charakter/Stimme) → „übermütig sein, prahlen“ (Deutung).
- 4096 (Bewegung) → nicht zuordenbar.
- Klasse P.

### S25 geselle (lemma_2213, NOM)
- Lexer: ge-selle swm. „ursprünglich hausgenosse, dann derjenige mit dem man zusammen ist … standesgenosse … gehülfe bei einer arbeit, handwerksgeselle“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=G02918 ; ge-selle swf. „gefährtin“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=G02919
- 3511 bis 3513 (Gefährte, Freund, Geliebter; Kampfgefährte) → swm.; 3514 (Formelle Bildung) → „gehülfe, handwerksgeselle“; 3515 (Jagd) → nicht sicher zuordenbar, aber kein anderes Stichwort.
- Klasse P.

### S26 ungemuot (lemma_6538, ADJ ADV NEG NOM)
- Lexer: un-gemuot adj. „übel gesinnt, böse … ; übel gestimmt, verdriesslich, zornig, betrübt“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=U03341 ; un-gemuot stm. „mismut“ (U03340) ; un-gemuot, un-gemüet part. adj. „nicht gemüejet, unbeschwert, -belästigt, -gestört“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=U03342 ; un-gemüete stn. „misstimmung des gemüts, mismut … zorn, kummer, betrübnis“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=U03336
- 10373 (Freude/Leid/Sorge) → adj. „betrübt“ und stn. „Kummer“; die Formenliste mischt beide (ungemüete 231, ungemuot 140).
- 14671 (Wut) → adj. „zornig“ bzw. stn. „zorn“.
- 14672 (Gefallen/Missfallen/Ästhetisch, Form ungemuote) und 14673 (Abscheu) → nicht sicher zuordenbar; am ehesten adj. „übel, verdriesslich“.
- Klasse P\*. Der echte Homograph (part. adj. „unbeschwert“, zu müejen) ist im Menü nicht erkennbar vertreten.

### S27 melden (lemma_4070, NOM VRB)
- Lexer: mëlden swv. „tr. u. refl. angeben, verraten …“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=M01154 ; mëlden stn. „verrat, angeberei“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=M01155 ; mëlden stf. „s. mëlde 1“ (M01153).
- 13859 (Aufmerksamkeit/Stimme), 13860 (Kommunikation/Benennung) → swv. „angeben, melden“; 6398 (Täuschung/Vertrauen) → swv. „verraten“ und stn. „Verrat“ (Formen meldes, meldens).
- Klasse P\*.

### S28 enwellen (lemma_8299, NEG VEM)
- en + wellen. Lexer: wellen an. v. „wollen“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=W01585 ; wëllen stv. „runden, rollen, wälzen“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=W01586 ; dazu sieben weitere wellen/wëllen (W01584, W01587 bis W01590, W01603, W01604), nicht gelesen.
- 20704 (Wunsch/Wille), 20706 (Werden), 20707 (Zeit/Funktionswörter) → wellen „wollen“.
- 20708 (Formen) → möglicherweise wëllen „runden, wälzen“ (Deutung); 89708 (Denken) → nicht zuordenbar.
- Klasse V. Im Bestandteil möglicherweise ein Homograph, beide Bedeutungen ohne Beleg.

### S29 verre (lemma_6913, ADJ ADV GRA NOM)
- Lexer: vërre adj. „fern, entfernt, weit (s. vër)“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=V02185 ; vërre, vërr adv. „fern, entfernt, weit, von weiten“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=V02186 ; virre, vërre stf. „ferne, weite“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=V03919 ; verre swm. „s. ver“ (V02188, nicht weiter verfolgt).
- 14327 (Ausdehnung/Raum, 3361 Belege) → adj./adv. „fern“, Formen gemischt (verre, verrer, verrest).
- 30753 (Verhältnis, Formen fer, fere) → adv. „fern“ bzw. vër (Deutung).
- 11079 („Größte Gruppierungen“, Formen verrem, verriu, verrist) → nicht zuordenbar; die Formen sind adjektivisch.
- Klasse P\*. Der Homograph verre swm. ist im Menü nicht vertreten.

### S30 rinc (lemma_4917, NOM)
- Lexer: rinc, ring stm. „ring: fingerring, annulus … ohrring …“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=R01267 (nur Anfang gelesen; Panzerring, Kreis, Ringplatz nicht erreicht).
- Alle sieben Bedeutungen (Panzerring, Kampfplatz, Fingerring/Ehe, Werkzeugring, Schmuck, Kreis von Leuten, Gerichtsring) → ein Stichwort „Ring, Kreis“.
- Klasse P.

### S31 spæhe (lemma_5633, ADJ ADV GRA NOM)
- Lexer: spæhe adj. „von pers. weise, klug, scharfsichtig, schlau“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=S05968 ; spæhe, spâhe adv. „zierlich, kunstvoll“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=S05969 ; spæhe stf. „weisheit, scharfsinnigkeit, klugheit … ; kunst“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=S05970
- 8812 (Verwunderung/Ästhetisch) → adj./adv. „kunstvoll, zierlich“ (der Sachbezug des Adjektivs liegt jenseits des gelesenen Anfangs).
- 8813 (Geist/Fähigkeiten) → adj. „klug“ bzw. stf. „Klugheit“.
- 8815 (Übersinnliche Wahrnehmung/Scherz) → nicht zuordenbar.
- Klasse P\*.

### S32 bein (lemma_471, NOM)
- Lexer: bein stn. „knochen; bein (elfenbein …), schenkel. allg.“, https://woerterbuchnetz.de/?sigle=Lexer&lemid=B00864
- 107725 (Materialien) → „Knochen, Elfenbein“; 31099 (Tierglieder), 658 (Menschenglieder) → „Bein, Schenkel“; 99593 (Möbel) → Bein eines Möbels (Deutung); 659 (Spielzeug) → nicht sicher zuordenbar (Würfel aus Knochen?).
- Klasse P.

## Nebenbefunde

1. **Verschmelzungen erben das Menü des Grundworts.** In Band 1-3 sind 6 von 8 Einträgen V. Ihre Bedeutungen sind die des Grundworts: zeschrîben hat sechs Bedeutungen von schrîben, alle ohne Beleg; vawir (1 Beleg) trägt sieben Bedeutungen von vâhen, deren Typlisten Formen wie gevangen (1679) und vieng (104) enthalten. Ein Eintrag mit 1 Beleg, dessen Bedeutungen Tausende Formen des Grundworts listen, widerspricht der Beschreibung „Typen pro Lemma“ in `knowledge/data.md`; ob diese Typen zu vawir oder zu vâhen gehören, habe ich nicht geprüft. Für die Ziehung des Goldstandards wohl relevant (Ausschluss oder eigene Schicht für V).
2. **Menüs ohne Lexer-Halt.** Nicht zuordenbar waren u. a. brâme 1345 (Bäume/Holzverarbeitung), geregen 3360 (Rechtswesen), übergiuden 36456 (Handel/Finanzen), güften 4096 (Bewegung), spæhe 8815 (Übersinnliche Wahrnehmung/Scherz), verre 11079 („Größte Gruppierungen“), heilwertec 72907. Das kann an der nur teilweisen Lesung liegen; bei brâme (kurzer Artikel, eine Glosse) und verre 11079 eher nicht.
3. **Fast gleiche Bündel.** zerspannen 29922/29923 unterscheiden sich nur in „Zielrichtung der Aktion“ vs. „Art und Weise der Handlung“; geregen 3358/3359 nur in objekt- vs. selbstbezogen; übergiuden 23054/27863 teilen „Respekt/Bewunderung“; geselle 3512/3513 unterscheiden sich nur um „Kriegswesen/Gesellschaftliche Ordnung“, zudem trägt 3513 die Form „gesell“ und 3512 „geselle“, d. h. die Typliste trennt hier Schreibvarianten, nicht Bedeutungen.
4. **Homographen bei Lexer, die im Menü fehlen:** schurz adj. „kurz“ und stm. „Sprung“, ge-rëgen stn. „Regenguss“, un-gemuot part. adj. „unbeschwert“, verre swm., wallen stn., güften stn. Die MHDBDB scheint also nicht systematisch alle Lexer-Homographen unter einem Eintrag zu sammeln, sondern nur die, die im Korpus vorkamen (Deutung).
5. **Merkwürdige Formen-Zuordnung.** übergiuden 23054 trägt die Form „griften“ (1 Beleg), die nicht zu übergiuden passt; geselle 3511 („Männlich/Mann“) trägt „gesellin“, eine feminine Bildung; schurz trägt Verbformen (schurzete, schurtzt) unter Kleidungsbedeutungen, obwohl Lexer schürzen als eigenes Verb führt (nicht nachgeschlagen).
6. **Lexer selbst vereint Homonymes:** touf stm. führt „Tiefe“ und „Taufe“ unter einem Stichwort (S07). Die Grenze zwischen H und P hängt also auch an Lexers Stichwortansatz.
