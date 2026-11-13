// Browsertest der gebauten Annotationsdateien (Protokoll, Abschnitte 6 und 8).
// Aufruf aus dem Repo-Wurzelverzeichnis, nach annotation_bauen.py für julia und alan:
//     node goldstandard/pilot/test_annotation.mjs [chromium|msedge|chrome|firefox|webkit]
// Ohne Argument Chromium. msedge und chrome nutzen die installierten Browser, webkit steht für Safari.
// Firefox: Die zwei Prüfungen mit Eingaben in eine Seite, die nicht vorne ist, scheitern, weil Firefox dort weder
// focus noch input zustellt (2026-11-13 gemessen, Review-Runde 8 bestätigt). Ein Tab: alles grün.
// Prüft am gebauten HTML: Blindheit, feste Kennung, Statusregeln, Festhalten und Rücksetzen,
// Protokoll nur anhängend, Kontexterweiterung protokolliert, Export, Import des eigenen Exports,
// Ablehnung eines fremden Exports, Seite ohne Netz.
import { chromium, firefox, webkit } from "playwright";
import { readFileSync, writeFileSync } from "node:fs";
import { join, resolve } from "node:path";
import { tmpdir } from "node:os";
import { pathToFileURL } from "node:url";

const DATEI = n => resolve(`goldstandard/pilot/bau/annotation-${n}-runde0.html`);
let fehler = 0;
const ok = (b, text) => { console.log((b ? "ok    " : "FEHLER") + "  " + text); if (!b) fehler++; };

const quelle = readFileSync(DATEI("julia"), "utf8");
const daten = JSON.parse(quelle.match(/<script id="daten" type="application\/json">([\s\S]*?)<\/script>/)[1]);
ok(!/"ana"|#type_|lemmaRef|meaningRef|"pos"|"wortart"/.test(JSON.stringify(daten)), "keine Silber- oder Token-Attribute und keine Wortart im eingebetteten JSON");
ok(daten.meta.kennung === "julia", "Kennung fest eingetragen");
const alan = JSON.parse(readFileSync(DATEI("alan"), "utf8").match(/<script id="daten" type="application\/json">([\s\S]*?)<\/script>/)[1]);
ok(JSON.stringify(daten.items.map(i => i.item).sort()) === JSON.stringify(alan.items.map(i => i.item).sort()), "beide Personen haben dieselben Items");
ok(daten.items.map(i => i.item).join() !== alan.items.map(i => i.item).join(), "Itemreihenfolge pro Person verschieden");

const BROWSER = process.argv[2] || "chromium";
const browser = BROWSER === "firefox" ? await firefox.launch() : BROWSER === "webkit" ? await webkit.launch()
  : await chromium.launch(BROWSER === "chromium" ? {} : {channel: BROWSER});
console.log("Browser: " + BROWSER + " " + browser.version());
const ctx = await browser.newContext({ acceptDownloads: true });
const netz = [];
ctx.on("request", r => { if (!r.url().startsWith("file:") && !r.url().startsWith("blob:") && !r.url().startsWith("data:")) netz.push(r.url()); });
const page = await ctx.newPage();
const js = [];
page.on("pageerror", e => js.push(String(e)));
await page.goto(pathToFileURL(DATEI("julia")).href);

ok((await page.locator("#fortschritt").textContent()).startsWith("0 von 15"), "Start: nichts festgehalten");
ok(await page.locator("input[name=status]:checked").count() === 0, "kein Status vorausgewählt");
ok(await page.locator("input[name=karte]:not([disabled])").count() > 0 && await page.locator("input[name=karte]:checked").count() === 0, "Karten ohne Status wählbar, keine vorausgewählt");
const reihenfolge = await page.evaluate(() => { const m = document.getElementById("main").innerHTML; return [m.indexOf("Bedeutungen"), m.indexOf("<legend>Status")]; });
ok(reihenfolge[0] > -1 && reihenfolge[0] < reihenfolge[1], "Karten stehen über dem Status");

await page.click("#btnFest");
ok((await page.locator("#fehler").textContent()).includes("Status"), "Festhalten ohne Status abgelehnt");

const erstes = daten.items[0];
await page.click("#btnKontext");
ok((await page.locator("#btnKontext").textContent()) === "Weniger Kontext", "Kontext erweitert");
await page.check("input[name=status][value=SENSE]");
await page.locator("input[name=karte]").first().check();
await page.click("#btnFest");
ok((await page.locator("#fehler").textContent()).includes("Sicherheit"), "Festhalten ohne Sicherheit abgelehnt");
await page.check("input[name=sicherheit][value=eher_sicher]");
await page.fill("#kommentar", "Testkommentar");
await page.click("#btnFest");
ok((await page.locator("#fortschritt").textContent()).startsWith("1 von 15"), "Beleg 1 festgehalten");
ok((await page.locator(".eyebrow").nth(1).textContent()).startsWith("Beleg 2"), "nach Festhalten weiter zu Beleg 2");

await page.check("input[name=status][value=MEHRERE]");
await page.locator("input[name=karte]").first().check();
await page.check("input[name=sicherheit][value=sicher]");
await page.click("#btnFest");
ok((await page.locator("#fehler").textContent()).includes("mindestens zwei"), "MEHRERE mit einer Karte abgelehnt");
await page.check("input[name=status][value=LEMMA_FALSCH]");
ok(await page.locator("input[name=karte]:checked").count() === 0, "Statuswechsel leert die Karten");
await page.click("#btnFest");
ok((await page.locator("#fehler").textContent()).includes("Kommentar"), "LEMMA_FALSCH ohne Kommentar abgelehnt");

await page.locator("nav li button").first().click();
await page.check("input[name=sicherheit][value=unsicher]");
ok((await page.locator("#fortschritt").textContent()).startsWith("0 von 15"), "Änderung nach Festhalten setzt auf Entwurf zurück");

const [dl] = await Promise.all([page.waitForEvent("download"), page.click("#btnExport")]);
const exp = JSON.parse(readFileSync(await dl.path(), "utf8"));
const ev = exp.ereignisse;
ok(exp.meta.kennung === "julia" && exp.meta.manifest_sha256 === daten.meta.manifest_sha256, "Export trägt Kennung und Manifest-Prüfsumme");
ok(ev.some(e => e.aktion === "kontext_erweitert" && e.item === erstes.item), "Kontexterweiterung protokolliert");
ok(ev.some(e => e.aktion === "festgehalten") && ev.some(e => e.aktion === "festhalten_aufgehoben"), "Festhalten und Aufheben protokolliert");
ok(ev.some(e => e.aktion === "verlassen" && typeof e.wert === "number"), "Verweildauer protokolliert");
ok(ev.every(e => /T\d\d:\d\d:\d\d\.\d{3}[+-]\d\d:\d\d$/.test(e.zeit)), "Zeitstempel ISO 8601 mit Zeitzone");
ok(ev.every(e => Array.isArray(e.kartenreihenfolge) || e.item === null), "jede Aktion trägt die gezeigte Kartenreihenfolge");
const i1 = exp.items.find(i => i.item === erstes.item);
ok(i1.status === "SENSE" && i1.senses.length === 1 && i1.festgehalten === false && i1.sicherheit === "unsicher", "Endstand von Beleg 1 korrekt");
ok(JSON.stringify(i1.kartenreihenfolge) === JSON.stringify(erstes.karten.map(k => k.sense)), "Kartenreihenfolge im Export wie gezeigt");
ok(!/\((NOM|VRB|ADJ)\)/.test(await page.locator("main").textContent()), "keine Wortart auf der Seite");

// Protokoll nur anhängend: Import einer älteren Sicherung und ein zweiter Tab dürfen nichts entfernen
const protokoll = async p => p.evaluate(() => {
  const k = Object.keys(localStorage).find(x => x.startsWith("wsd-pilot:"));
  return JSON.parse(localStorage.getItem(k)).ereignisse;
});
page.on("dialog", d => d.accept());
await page.check("input[name=sicherheit][value=sicher]");
await page.click("#btnFest");                                   // Beleg 1 wieder festgehalten, danach Beleg 2 offen
const vorImport = await protokoll(page);
await page.setInputFiles("#importFile", await dl.path());      // ältere Sicherung
await page.waitForTimeout(300);
const nachImport = await protokoll(page);
ok(nachImport.length > vorImport.length && vorImport.every(e => nachImport.some(x => x.id === e.id)), "Import einer älteren Sicherung entfernt nichts aus dem Protokoll");
ok((await page.locator("#fortschritt").textContent()).startsWith("1 von 15"), "Import einer älteren Sicherung hebt Festhalten nicht auf");

const tabB = await ctx.newPage();
tabB.on("pageerror", e => js.push("Tab B: " + e));
await tabB.goto(pathToFileURL(DATEI("julia")).href);           // Tab B steht auf Beleg 1
await page.locator("nav li button").nth(1).click();            // Tab A: Beleg 2 festhalten
await page.check("input[name=status][value=KONTEXT_UNZUREICHEND]");
await page.check("input[name=sicherheit][value=sicher]");
await page.click("#btnFest");
const vorTab = await protokoll(page);
await tabB.check("input[name=sicherheit][value=unsicher]");     // Tab B ändert Beleg 1
await page.waitForTimeout(300);
const nachTab = await protokoll(page);
ok(vorTab.every(e => nachTab.some(x => x.id === e.id)) && nachTab.length > vorTab.length, "zweiter Tab entfernt nichts aus dem Protokoll");
const exp2 = await page.evaluate(() => D.items.map(i => Object.assign({item: i.item}, A[i.item])));
ok(exp2[1].festgehalten && exp2[1].status === "KONTEXT_UNZUREICHEND", "Festhalten aus Tab A bleibt nach Änderung in Tab B erhalten");
ok(!exp2[0].festgehalten && exp2[0].status === "SENSE" && exp2[0].sicherheit === "unsicher", "Änderung aus Tab B hebt Festhalten von Beleg 1 auf und bleibt erhalten");
ok((await page.locator("#fortschritt").textContent()).startsWith("1 von 15"), "Tab A zeigt die Änderung aus Tab B ohne Neuladen");
// Kommentarentwurf in Tab B übersteht Schreibvorgänge aus Tab A (Review Runde 2, Befund 2)
await tabB.fill("#kommentar", "halb getippt");                  // Tab B, Beleg 1, Feld nicht verlassen
await page.locator("nav li button").nth(3).click();             // Tab A öffnet ein anderes Item
await page.waitForTimeout(300);
ok(await tabB.inputValue("#kommentar") === "halb getippt", "Entwurf bleibt, wenn ein anderer Tab ein anderes Item öffnet");
await page.locator("nav li button").first().click();            // Tab A ändert dasselbe Item
await page.check("input[name=sicherheit][value=eher_sicher]");
await page.waitForTimeout(300);
ok(await tabB.inputValue("#kommentar") === "halb getippt", "Entwurf bleibt, wenn ein anderer Tab dasselbe Item ändert");
ok(await tabB.isChecked("input[name=sicherheit][value=eher_sicher]"), "Tab B zeigt die Änderung aus Tab A");
ok((await protokoll(page)).filter(e => e.wert === "halb getippt").length === 1, "Entwurf wird genau einmal protokolliert");
ok(await tabB.evaluate(() => document.activeElement && document.activeElement.id) === "kommentar", "Fokus bleibt beim Neuzeichnen im Kommentarfeld");
// Entwurf übersteht Verlassen des Felds und Itemwechsel (Review Runde 4, Befund 1)
await tabB.keyboard.press("Tab");
await tabB.click("#btnWeiter");
await tabB.click("#btnZurueck");
ok(await tabB.inputValue("#kommentar") === "halb getippt", "Entwurf übersteht Verlassen und Itemwechsel");
// Eigener gespeicherter Kommentar verdrängt keinen neueren fremden (Review Runde 4, Befund 2)
await tabB.fill("#kommentar", "B1");
await tabB.locator("#kommentar").blur();
await page.waitForTimeout(300);
await page.fill("#kommentar", "A1");
await page.locator("#kommentar").blur();
await page.waitForTimeout(300);
ok(await tabB.inputValue("#kommentar") === "A1", "neuerer Kommentar aus anderem Tab ersetzt den eigenen gespeicherten");
await tabB.click("#btnFest");
const nachB = await tabB.evaluate(() => A[D.items[0].item].kommentar);
ok(nachB === "A1", "Festhalten in Tab B schreibt den eigenen alten Kommentar nicht zurück");
await tabB.close();

// Kommentar aus einem anderen Tab erscheint im Feld eines Tabs ohne Entwurf (Review Runde 3, Befund 1)
const tabC = await ctx.newPage();
tabC.on("pageerror", e => js.push("Tab C: " + e));
await tabC.goto(pathToFileURL(DATEI("julia")).href);              // Tab C, Beleg 1, kein Entwurf
await page.fill("#kommentar", "neu aus A");                       // Tab A, Beleg 1
await page.locator("#kommentar").blur();
await page.waitForTimeout(300);
ok(await tabC.inputValue("#kommentar") === "neu aus A", "Kommentar aus anderem Tab erscheint im Feld");
await tabC.close();

// Rückkorrektur nach automatischer Speicherung geht beim Neuzeichnen nicht verloren (Review Runde 5, Befund 1)
const kommentarA = async () => page.evaluate(() => A[aktuell].kommentar);
for (const [name, klick] of [["Mehr Kontext", () => page.click("#btnKontext")],
                             ["Statuswechsel", () => page.check("input[name=status][value=KEINE_PASST]")]]) {
  const vorher = await kommentarA();
  await page.click("#kommentar");
  await page.keyboard.press("End");
  await page.keyboard.type("x");
  await page.waitForTimeout(1100);                                // Tipppause: "…x" wird gespeichert
  ok(await kommentarA() === vorher + "x", name + ": Tipppause speichert den Entwurf");
  await page.keyboard.press("Backspace");                          // zurück auf den Wert beim Fokussieren
  await klick();
  ok(await kommentarA() === vorher && await page.inputValue("#kommentar") === vorher, name + ": Rückkorrektur bleibt erhalten");
  const ev6 = await protokoll(page), it6 = await page.evaluate(() => aktuell);
  const letzterK = ev6.filter(e => e.item === it6 && e.aktion === "kommentar").pop();
  const ausloeser = ev6.findIndex(e => e.item === it6 && e.ms > letzterK.ms && (e.aktion === "kontext_erweitert" || e.aktion === "kontext_reduziert" || e.aktion === "status"));
  ok(letzterK.kontext_erweitert === false && ausloeser !== -1, name + ": Kommentar vor der Aktion protokolliert, mit dem Kontext beim Schreiben");
  if (name === "Mehr Kontext") await page.click("#btnKontext");     // wieder reduzieren, damit der nächste Ablauf gleich startet
}

// Sicherheit und Begriffe: Holt das Sichern fremde Ereignisse zum Beleg, bleibt die Anzeige richtig (Review Runde 7, Befund 1)
const einschleusen = async wert => page.evaluate(w => {          // fremdes Ereignis, dessen storage-Ereignis noch aussteht
  const k = Object.keys(localStorage).find(x => x.startsWith("wsd-pilot:")), g = JSON.parse(localStorage.getItem(k));
  g.ereignisse.push({id: "fremd-" + w, ms: Date.now(), zeit: "2026-11-13T00:00:00.000+01:00", item: aktuell, aktion: "kommentar",
    wert: w, kartenreihenfolge: ITEM[aktuell].karten.map(x => x.sense), kontext_erweitert: false});
  localStorage.setItem(k, JSON.stringify(g));
}, wert);
const entwurfMitPause = async () => {
  await page.click("#kommentar"); await page.keyboard.press("End"); await page.keyboard.type("y");
  await page.waitForTimeout(1100); await page.keyboard.press("Backspace");
};
await entwurfMitPause();
await einschleusen("fremd1");
await page.check("input[name=sicherheit][value=unsicher]");
ok(await page.isChecked("input[name=sicherheit][value=unsicher]") && await page.evaluate(() => A[aktuell].sicherheit) === "unsicher", "Sicherheit nach fremdem Ereignis beim Sichern richtig angezeigt");
await page.check("input[name=status][value=KEINE_PASST]").catch(() => {});
await entwurfMitPause();
await einschleusen("fremd2");
const begriff = page.locator("input[name=begriff]").first();
await begriff.check();
const bstand = await page.evaluate(() => A[aktuell].begriffe);
ok(await page.locator("input[name=begriff]").first().isChecked() && bstand.length === 1, "Begriff nach fremdem Ereignis beim Sichern richtig angezeigt, kein doppelter Eintrag");

// Uhrversatz: Sicherung von einem Rechner, dessen Uhr 10 Minuten vorgeht (Review Runde 2, Befund 1)
const versetzt = JSON.parse(readFileSync(await dl.path(), "utf8"));
versetzt.ereignisse.forEach(e => { e.ms += 600000; });
const versetztPfad = join(tmpdir(), "wsd-pilot-versetzt.json");
writeFileSync(versetztPfad, JSON.stringify(versetzt));
const p4 = await (await browser.newContext()).newPage();
p4.on("dialog", d => d.accept());
p4.on("pageerror", e => js.push("Uhrversatz: " + e));
await p4.goto(pathToFileURL(DATEI("julia")).href);
await p4.setInputFiles("#importFile", versetztPfad);
await p4.waitForTimeout(300);
await p4.check("input[name=sicherheit][value=sicher]");
await p4.click("#btnFest");                                       // Beleg 1 festgehalten (nach dem Import)
await p4.locator("nav li button").first().click();
await p4.check("input[name=sicherheit][value=eher_sicher]");     // danach wieder geändert
const live = await p4.evaluate(() => ({f: A[D.items[0].item].festgehalten, s: A[D.items[0].item].sicherheit}));
await p4.reload();
const geladen = await p4.evaluate(() => ({f: A[D.items[0].item].festgehalten, s: A[D.items[0].item].sicherheit}));
ok(!live.f && live.s === "eher_sicher", "Uhrversatz: Änderung nach Import gilt sofort");
ok(JSON.stringify(live) === JSON.stringify(geladen), "Uhrversatz: nach Neuladen derselbe Stand");
const ordnung = await protokoll(p4);
ok(ordnung.every((e, i) => i === 0 || e.ms > ordnung[i - 1].ms || (e.ms === ordnung[i - 1].ms && e.id > ordnung[i - 1].id)), "Protokoll im Speicher nach Sortierzeit geordnet");

// eigener Export lässt sich in einem frischen Browser laden
const ctx2 = await browser.newContext();
const p2 = await ctx2.newPage();
p2.on("dialog", d => d.accept());
await p2.goto(pathToFileURL(DATEI("julia")).href);
await p2.setInputFiles("#importFile", await dl.path());
await p2.waitForTimeout(300);
const n2 = await p2.evaluate(() => JSON.parse(localStorage.getItem(Object.keys(localStorage).find(k => k.startsWith("wsd-pilot:")))).ereignisse.length);
ok(n2 > ev.length, "Import übernimmt das Protokoll und hängt an");
ok(await p2.inputValue("#kommentar") === "Testkommentar", "nach Import zeigt das Feld den importierten Kommentar");
await p2.click("#btnFest");
const k2 = await p2.evaluate(() => ({k: A[D.items[0].item].kommentar, f: A[D.items[0].item].festgehalten}));
ok(k2.k === "Testkommentar" && k2.f, "Festhalten nach Import behält den Kommentar");
await p2.locator("nav li button").first().click();
await p2.fill("#kommentar", "lokal");
await p2.locator("#kommentar").blur();
const spaeter = JSON.parse(readFileSync(await dl.path(), "utf8"));
spaeter.ereignisse.push({id: "test-export-1", ms: Date.now() + 60000, zeit: "2099-01-01T00:00:00.000+00:00", item: daten.items[0].item,
  aktion: "kommentar", wert: "export", kartenreihenfolge: daten.items[0].karten.map(k => k.sense), kontext_erweitert: false});
const spaeterPfad = join(tmpdir(), "wsd-pilot-spaeter.json");
writeFileSync(spaeterPfad, JSON.stringify(spaeter));
await p2.setInputFiles("#importFile", spaeterPfad);
await p2.waitForTimeout(300);
ok(await p2.inputValue("#kommentar") === "export", "Import mit neuerem Kommentar ersetzt einen lokal gespeicherten im Feld");

// Erst Karte, dann Status: der Ablauf der Kurzanleitung v0.1
const p5 = await (await browser.newContext()).newPage();
p5.on("pageerror", e => js.push("Karte zuerst: " + e));
await p5.goto(pathToFileURL(DATEI("julia")).href);
await p5.locator("input[name=karte]").first().check();
await p5.check("input[name=status][value=SENSE]");
ok(await p5.locator("input[name=karte]:checked").count() === 1, "Karte bleibt nach Statuswahl gewählt");
await p5.locator("input[name=karte]").nth(1).check();
ok(await p5.locator("input[name=karte]:checked").count() === 1, "bei „Eine Bedeutung passt“ ersetzt eine neue Karte die alte");
await p5.check("input[name=sicherheit][value=sicher]");
await p5.click("#btnFest");
ok((await p5.locator("#fortschritt").textContent()).startsWith("1 von 15"), "Karte vor Status gewählt, Festhalten gelingt");
await p5.check("input[name=status][value=MEHRERE]");
await p5.locator("input[name=karte]").nth(0).check();
await p5.locator("input[name=karte]").nth(1).check();
await p5.check("input[name=status][value=SENSE]");
await p5.click("#btnFest");
ok((await p5.locator("#fehler").textContent()).includes("genau eine"), "zwei Karten und „Eine Bedeutung passt“: Festhalten abgelehnt");
const zweite = await p5.locator("input[name=karte]:checked").nth(1).getAttribute("value");
await p5.locator(`input[name=karte][value="${zweite}"]`).uncheck();
ok(await p5.locator("input[name=karte]:checked").count() === 1, "Abwählen einer von zwei Karten bei „Eine Bedeutung passt“ lässt die andere stehen");

// Export von julia wird in alans Datei abgelehnt
const p3 = await (await browser.newContext()).newPage();
let meldung = "";
p3.on("dialog", d => { meldung = d.message(); d.dismiss(); });
await p3.goto(pathToFileURL(DATEI("alan")).href);
await p3.setInputFiles("#importFile", await dl.path());
await p3.waitForTimeout(300);
ok(meldung.includes("gehört nicht"), "fremder Export abgelehnt");

ok(js.length === 0, "keine JavaScript-Fehler" + (js.length ? ": " + js.join(" | ") : ""));
ok(netz.length === 0, "keine Netzanfragen" + (netz.length ? ": " + netz.join(" ") : ""));
await browser.close();
console.log(fehler ? `\n${fehler} Prüfung(en) fehlgeschlagen` : "\nalle Prüfungen bestanden");
process.exit(fehler ? 1 : 0);
