// Durchlauf für auswerten.py mit echten Exporten der Annotationsseite (Runde 0, Ablauf lesart-zuerst).
// Beide Personen werden über die Oberfläche mit einem festen, erfundenen Plan "annotiert"; das sind Testdaten,
// keine Labels. Danach prüft der Test die Kennzahlen gegen eine eigene Rechnung, die Konsole auf Lecks, die
// Pfadsperre für --bericht und die Abbrüche bei falschen Exporten.
//
// Aufruf aus der Wurzel des Repos (die gebauten Dateien unter pilot/bau/ müssen da sein):
//     node goldstandard/pilot/test_auswerten.mjs
import { chromium } from "playwright";
import { readFileSync, writeFileSync, mkdtempSync, rmSync, existsSync } from "node:fs";
import { join, resolve } from "node:path";
import { tmpdir } from "node:os";
import { pathToFileURL } from "node:url";
import { spawnSync } from "node:child_process";

let fehler = 0;
const ok = (b, text) => { console.log((b ? "ok    " : "FEHLER") + "  " + text); if (!b) fehler++; };
const DATEI = n => resolve(`goldstandard/pilot/bau/annotation-${n}-runde0.html`);
const tmp = mkdtempSync(join(tmpdir(), "wsd-auswerten-"));
const items = Object.fromEntries(JSON.parse(readFileSync("goldstandard/pilot/items-pilot.json", "utf8")).map(i => [i.item, i]));
const runde0 = JSON.parse(readFileSync("goldstandard/pilot/manifest-pilot.json", "utf8")).runde0.slice().sort();
const S = id => items[id].karten.map(k => k.sense).sort();

// Plan je Item-Index (sortierte IDs): [Status, Karten, Sicherheit, Kommentar]; null = nicht festhalten
const plan = {julia: {}, alan: {}};
runde0.forEach((id, i) => { plan.julia[id] = ["SENSE", [S(id)[0]], "sicher", ""]; plan.alan[id] = ["SENSE", [S(id)[0]], "eher_sicher", ""]; });
const id = i => runde0[i];
plan.alan[id(1)] = ["SENSE", [S(id(1))[1]], "unsicher", ""];
plan.julia[id(3)] = ["MEHRERE", S(id(3)).slice(0, 2), "eher_sicher", ""];
plan.julia[id(5)] = ["KEINE_PASST", [], "sicher", "Test"]; plan.alan[id(5)] = ["KEINE_PASST", [], "sicher", ""];
plan.julia[id(7)] = ["KONTEXT_UNZUREICHEND", [], "unsicher", ""];
plan.alan[id(10)] = ["TEXT_DEFEKT", [], "sicher", "Testkommentar"];
plan.julia[id(13)] = ["LEMMA_FALSCH", [], "sicher", "Test"]; plan.alan[id(13)] = ["LEMMA_FALSCH", [], "eher_sicher", "Test"];
plan.alan[id(14)] = null;

const browser = await chromium.launch();
const exporte = {};
for (const k of ["julia", "alan"]) {
  const ctx = await browser.newContext({ acceptDownloads: true });
  const page = await ctx.newPage();
  await page.goto(pathToFileURL(DATEI(k)).href);
  for (const iid of runde0) {
    await page.evaluate(x => oeffne(x), iid);
    await page.fill("#paraphrase", "Testlesart");
    await page.click("#btnAufdecken");
    const p = plan[k][iid];
    if (!p) continue;
    const [status, karten, sicher, kommentar] = p;
    await page.check(`input[name=status][value=${status}]`);
    for (const s of karten) await page.check(`input[name=karte][value="${s}"]`);
    await page.check(`input[name=sicherheit][value=${sicher}]`);
    if (kommentar) { await page.fill("#kommentar", kommentar); await page.locator("#kommentar").blur(); }
    if (k === "julia" && iid === id(12)) {           // festhalten, ändern (hebt auf), wieder festhalten
      await page.click("#btnFest"); await page.evaluate(x => oeffne(x), iid);
      await page.check("input[name=sicherheit][value=unsicher]");
    }
    await page.click("#btnFest");
  }
  const [dl] = await Promise.all([page.waitForEvent("download"), page.click("#btnExport")]);
  exporte[k] = join(tmp, `wsd-pilot-runde0-${k}.json`);
  writeFileSync(exporte[k], readFileSync(await dl.path()));
  await ctx.close();
}
await browser.close();

const lauf = (...a) => spawnSync("python", ["-X", "utf8", "goldstandard/pilot/auswerten.py", ...a], { encoding: "utf8" });
const r = lauf(exporte.alan, exporte.julia);           // Reihenfolge der Argumente egal
ok(r.status === 0, "Auswertung läuft durch" + (r.status ? ": " + r.stderr : ""));
const out = r.stdout;
console.log(out.split("\n").map(z => "        | " + z).join("\n"));

// Eigene Rechnung: α für zwei Kodierende, ohne fehlende Werte
function alpha(paare, d) {
  const v = paare.flat(), n = v.length;
  const dO = paare.reduce((s, [a, b]) => s + 2 * d(a, b), 0) / n;
  let dE = 0; for (let i = 0; i < n; i++) for (let j = 0; j < n; j++) if (i !== j) dE += d(v[i], v[j]);
  return 1 - dO / (dE / (n * (n - 1)));
}
const lab = (k, x) => { const p = plan[k][x]; return p && JSON.stringify([p[0], p[1].slice().sort()]); };
const beide = runde0.filter(x => plan.julia[x] && plan.alan[x]);
const ganz = beide.map(x => [lab("julia", x), lab("alan", x)]);
const nom = (a, b) => (a === b ? 0 : 1);
const menge = (k, x) => ["KEINE_PASST", "LEMMA_FALSCH"].includes(plan[k][x][0]) ? [plan[k][x][0]] : plan[k][x][1];
const einh = eb => beide.filter(x => eb.includes(plan.julia[x][0]) && eb.includes(plan.alan[x][0]));
const masi = (a, b) => {
  const A = new Set(a), B = new Set(b), sch = [...A].filter(x => B.has(x)).length, ver = new Set([...a, ...b]).size;
  const gleich = sch === A.size && sch === B.size, teil = sch === A.size || sch === B.size;
  return 1 - (sch / ver) * (gleich ? 1 : teil ? 2 / 3 : sch ? 1 / 3 : 0);
};
const paare = eb => einh(eb).map(x => [menge("julia", x), menge("alan", x)]);
const p2 = paare(["SENSE", "MEHRERE", "KEINE_PASST", "LEMMA_FALSCH"]);
const block = () => out.split(/\r?\n\r?\n/).find(b => b.startsWith("Sense-Ebene")) || "";
const f3 = v => v.toFixed(3);

ok(out.includes("Festgehalten: julia 15, alan 14, beide gültig 14"), "Festgehalten-Zählung (Festhalten, Aufheben, wieder Festhalten zählt)");
ok(out.includes("Rohübereinstimmung: 10 von 14 (71.4 %"), "ganzes Label: 10 von 14 gleich");
ok(out.includes("α nominal: " + f3(alpha(ganz, nom))), "ganzes Label: α nominal wie eigene Rechnung (" + f3(alpha(ganz, nom)) + ")");
// 12 Einheiten: 14 gemeinsam festgehaltene minus KONTEXT_UNZUREICHEND und TEXT_DEFEKT; das LEMMA_FALSCH-Paar zählt mit
// (ohne A42 wären es 11)
ok(block().includes("Einheiten: 12") && (out.match(/^Sense-Ebene/gm) || []).length === 1, "Sense-Ebene: 12 Einheiten mit KEINE_PASST und LEMMA_FALSCH als eigenen Kategorien (A41, A42), nur eine Lesart");
ok(block().includes("α MASI (1 - J·M, Hauptmaß): " + f3(alpha(p2, masi))), "Sense-Ebene: α MASI wie eigene Rechnung (" + f3(alpha(p2, masi)) + ")");
ok(block().includes("exakt: 10 von 12") && block().includes("Überschneidung: 11 von 12"), "Sense-Ebene: exakt 10, Überschneidung 11");
ok(/ SEN +9 +0 +0 +0 +0 +1/.test(out) && / MEH +1 /.test(out) && / KON +1 /.test(out) && / LEM +0 +0 +0 +1 +0 +0/.test(out), "Konfusionstabelle der Status");
ok(out.includes("Runde 0 hat keine Schwelle"), "Runde 0 ohne Stoppregel");
ok(out.includes("julia: Sicherheit sicher 12, eher_sicher 1, unsicher 2"), "Sicherheit je Person");
const ids = new Set(runde0.flatMap(x => [x, items[x].xml_id, items[x].lemma, ...items[x].karten.map(k => k.sense)]));
ok(![...ids].some(x => out.includes(x)) && !/(lemma|concept)_\d|_sense_/.test(out), "keine ID auf der Konsole");

const imRepo = resolve("goldstandard/pilot/bericht-test.md");
const r2 = lauf(exporte.julia, exporte.alan, "--bericht", imRepo);
ok(r2.status !== 0 && !existsSync(imRepo), "--bericht im Repo abgelehnt, nichts geschrieben");
// Sperre gilt für jeden Worktree des Repos, nicht nur für den eigenen (Review 2026-11-20). Das Skript wird so
// gestellt, als läge es in jedem Worktree (HIER), und muss von dort alle Worktrees sperren; sonst sähe der Test
// den Bug nicht, weil der verschachtelte Worktree im Ordner des Haupt-Worktrees liegt.
// Ein leerer temporärer Worktree (ohne Checkout) sorgt dafür, dass es immer mindestens zwei gibt (Review Runde 3)
const tmpWt = join(tmp, "worktree");
const wtAdd = spawnSync("git", ["worktree", "add", "--no-checkout", "--detach", tmpWt, "HEAD"], { encoding: "utf8" });
const wts = spawnSync("git", ["worktree", "list", "--porcelain"], { encoding: "utf8" }).stdout.split(/\r?\n/).filter(z => z.startsWith("worktree ")).map(z => z.slice(9));
const sperre = spawnSync("python", ["-X", "utf8", "-B", "-c", "import sys, json; sys.path.insert(0, 'goldstandard/pilot'); import auswerten as a, pathlib; W = json.loads(sys.argv[1]); r = []\nfor h in W:\n    a.HIER = pathlib.Path(h)\n    r += [a.erlaubt(w + '/x.md') for w in W] + [a.erlaubt(sys.argv[2])]\nprint(json.dumps(r))", JSON.stringify(wts), join(tmp, "x.md")], { encoding: "utf8" });
const erg = JSON.parse(sperre.stdout || "[]"), je = wts.length + 1;
ok(wts.length >= 2 && erg.length === wts.length * je && wts.every((_, h) => erg.slice(h * je, h * je + wts.length).every(v => v === false) && erg[h * je + wts.length] === true),
   `--bericht von jedem der ${wts.length} Worktrees aus in allen gesperrt, außerhalb erlaubt` + (wtAdd.status ? " (temporärer Worktree nicht angelegt: " + wtAdd.stderr.trim() + ")" : ""));
spawnSync("git", ["worktree", "remove", "--force", tmpWt]);
ok(!spawnSync("git", ["worktree", "list"], { encoding: "utf8" }).stdout.includes("wsd-auswerten-"), "temporärer Worktree wieder entfernt");
const draussen = join(tmp, "bericht.md");
const r3 = lauf(exporte.julia, exporte.alan, "--bericht", draussen);
const b = existsSync(draussen) ? readFileSync(draussen, "utf8") : "";
ok(r3.status === 0 && (b.match(/ ABWEICHEND$/gm) || []).length === 5, "Bericht außerhalb geschrieben, 5 Items abweichend");
ok(![...ids].some(x => r3.stdout.includes(x)), "auch mit --bericht keine ID auf der Konsole");

const r4 = lauf(exporte.julia, exporte.julia);
ok(r4.status !== 0 && r4.stderr.includes("dieselbe Kennung"), "zweimal dieselbe Person abgelehnt");
const kaputt = JSON.parse(readFileSync(exporte.alan, "utf8")); kaputt.meta.manifest_sha256 = "0".repeat(64);
writeFileSync(join(tmp, "kaputt.json"), JSON.stringify(kaputt));
const r5 = lauf(exporte.julia, join(tmp, "kaputt.json"));
ok(r5.status !== 0 && r5.stderr.includes("Manifest-Prüfsumme"), "falsche Manifest-Prüfsumme abgelehnt");
const gefaelscht = JSON.parse(readFileSync(exporte.alan, "utf8")); gefaelscht.items[0].status = "TEXT_DEFEKT";
if (gefaelscht.items[0].status === plan.alan[gefaelscht.items[0].item]?.[0]) gefaelscht.items[0].status = "SENSE";
writeFileSync(join(tmp, "gefaelscht.json"), JSON.stringify(gefaelscht));
const r6 = lauf(exporte.julia, join(tmp, "gefaelscht.json"));
ok(r6.status !== 0 && r6.stderr.includes("Ereignisprotokoll"), "Endstand, der dem Protokoll widerspricht, abgelehnt");

rmSync(tmp, { recursive: true, force: true });
console.log(fehler ? `\n${fehler} Prüfungen fehlgeschlagen` : "\nalle Prüfungen bestanden");
process.exit(fehler ? 1 : 0);
