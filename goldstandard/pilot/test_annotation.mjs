// Browsertest der gebauten Annotationsdateien (Protokoll, Abschnitte 6 und 8).
// Aufruf aus dem Repo-Wurzelverzeichnis, nach annotation_bauen.py für julia und alan:
//     node goldstandard/pilot/test_annotation.mjs
// Prüft am gebauten HTML: Blindheit, feste Kennung, Statusregeln, Festhalten und Rücksetzen,
// Protokoll nur anhängend, Kontexterweiterung protokolliert, Export, Import des eigenen Exports,
// Ablehnung eines fremden Exports, Seite ohne Netz.
import { chromium } from "playwright";
import { readFileSync } from "node:fs";
import { resolve } from "node:path";
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

const browser = await chromium.launch();
const ctx = await browser.newContext({ acceptDownloads: true });
const netz = [];
ctx.on("request", r => { if (!r.url().startsWith("file:") && !r.url().startsWith("blob:") && !r.url().startsWith("data:")) netz.push(r.url()); });
const page = await ctx.newPage();
const js = [];
page.on("pageerror", e => js.push(String(e)));
await page.goto(pathToFileURL(DATEI("julia")).href);

ok((await page.locator("#fortschritt").textContent()).startsWith("0 von 15"), "Start: nichts festgehalten");
ok(await page.locator("input[name=status]:checked").count() === 0, "kein Status vorausgewählt");
ok(await page.locator("input[name=karte]:not([disabled])").count() === 0, "Karten ohne Status nicht wählbar");

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
await tabB.close();

// eigener Export lässt sich in einem frischen Browser laden
const ctx2 = await browser.newContext();
const p2 = await ctx2.newPage();
p2.on("dialog", d => d.accept());
await p2.goto(pathToFileURL(DATEI("julia")).href);
await p2.setInputFiles("#importFile", await dl.path());
await p2.waitForTimeout(300);
const n2 = await p2.evaluate(() => JSON.parse(localStorage.getItem(Object.keys(localStorage).find(k => k.startsWith("wsd-pilot:")))).ereignisse.length);
ok(n2 > ev.length, "Import übernimmt das Protokoll und hängt an");

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
