"""
Pilot-Pool des WSD-Goldstandards ziehen und einfrieren (Protokoll, Abschnitte 4.2 und 4.4; A30).

Aufruf aus dem Repo-Wurzelverzeichnis:
    python goldstandard/pilot/pilot_ziehen.py

Voraussetzung: goldstandard/ausschluss/ausschluss-tokens.csv (lokal, nicht im Repo) ist mit
goldstandard/ausschluss_nachmigration.py auf genau dem Korpusstand KORPUS_COMMIT erzeugt. Das Skript
bricht ab, wenn tei/ oder authority-files/ von KORPUS_COMMIT abweichen oder die Ausschlussliste auf
einem anderen Stand gerechnet ist.

Grundgesamtheit wie Protokoll, Abschnitt 3: <w> mit genau einem @lemmaRef auf ein Lemma mit
mindestens zwei Senses, Wortart NOM, VRB oder ADJ (Lexikon, sonst eindeutiges Token-@pos; VEX und
VEM als VRB), ohne WZB und SBF. Ausschlüsse 1 (nach der Migration geändert), 2 (zwei Senses mit
derselben Begriffsgruppe), 3 (ein Sense ohne Begriffszeiger) und 5 (Verschmelzungen). Ausschluss 4
ist eine Markierung (pos_abweichend), kein Ausschluss.

Ziehung (Vorschlag A30, im Kleinen wie die Hauptstichprobe nach 4.4):
  - 36 Zellen (Polysemie 2/3/4+ x Wortart x Frequenzband 1-3/4-20/21-200/>200), je 3 Items:
    eines aus D1, zwei aus D0; hat eine Zelle kein freies Paar in D1, kommt das Item aus D0.
  - Stufe 1: Paar aus Lemma und Wortart gleich wahrscheinlich, jedes Lemma höchstens einmal im Pool.
  - Stufe 2: ein Token des Paars in der Domäne, Gewicht T_G^(-1/2) nach Obergattungsgruppe.
  - Obergrenze pro Text im Pool: 3, Historiografie 5.
  - Runde 0: 15 Items des Pools, einfache Zufallsauswahl.
Die Lemmata des Pools werden bei der Ziehung von Haupt- und Panelstichprobe ausgeschlossen.

Ausgabe:
  goldstandard/pilot/manifest-pilot.json   Regeln, Seed, Commit, Prüfsummen, Zählungen, Items
  goldstandard/pilot/items-pilot.json      Baudaten der Oberfläche: Kontext und Karten, ohne Silber
"""

import csv
import hashlib
import json
import math
import random
import re
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path

from lxml import etree

sys.stdout.reconfigure(encoding="utf-8")

KORPUS_COMMIT = "a938559dc"          # Upstream-Stand vom 2026-10-14, entschieden von Julia am 2026-11-12
SEED = 20261112
ZELLE_N = 3                           # Items pro Zelle
RUNDE0_N = 15
KONTEXT = {"vers": (2, 8), "prosa": (20, 80)}   # Standard und erweitert, je Seite (Julia, 2026-11-12)
OUT = Path("goldstandard/pilot")
TEI = "{http://www.tei-c.org/ns/1.0}"
NS = {"t": "http://www.tei-c.org/ns/1.0"}
XID = "{http://www.w3.org/XML/1998/namespace}id"
XLANG = "{http://www.w3.org/XML/1998/namespace}lang"
MAP = {"VEX": "VRB", "VEM": "VRB"}
WORTARTEN = ("NOM", "VRB", "ADJ")
POLY = ("2", "3", "4+")
BAENDER = ("1-3", "4-20", "21-200", ">200")
WEG = {"WZB", "SBF"}


def git(*a):
    return subprocess.check_output(["git", *a], text=True).strip()


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


# --- Korpusstand prüfen ---
voll = git("rev-parse", KORPUS_COMMIT)
abw = git("diff", "--name-only", voll, "--", "tei", "authority-files")
lokal = git("status", "--porcelain", "--", "tei", "authority-files")
if abw or lokal:
    sys.exit(f"Korpus weicht von {KORPUS_COMMIT} ab:\n{abw}\n{lokal}")
aus_info = json.loads(Path("goldstandard/ausschluss/zusammenfassung.json").read_text(encoding="utf-8"))
if git("diff", "--name-only", aus_info["head_commit"], voll, "--", "tei") or aus_info["tei_mit_lokalen_aenderungen"]:
    sys.exit("Ausschlussliste ist auf einem anderen Korpusstand gerechnet: ausschluss_nachmigration.py neu ausführen")

# --- Lexikon und Begriffssystem ---
lex = etree.parse("authority-files/lexicon.xml")
LEX = {}
for e in lex.getroot().iterfind(".//t:entry", NS):
    senses = [(s.get(XID), [p.get("target").split("#")[-1] for p in s.findall("t:ptr", NS)])
              for s in e.findall("t:sense", NS)]
    LEX[e.get(XID)] = {"orth": e.findtext("t:form/t:orth", namespaces=NS) or "",
                       "pos": [p.text for p in e.findall("t:gramGrp/t:pos", NS)],
                       "senses": senses}

BEGRIFF = {}
for c in etree.parse("authority-files/concepts.xml").getroot().iter(f"{TEI}category"):
    term = next((t.text for t in c.findall(f"{TEI}catDesc/{TEI}term")
                 if t.get(XLANG) == "de" and not t.get("type")), None)
    BEGRIFF[c.get(XID)] = {"term": (term or c.get(XID)).strip(),
                           "broader": [p.get("target").lstrip("#")
                                       for p in c.findall(f"{TEI}catDesc/{TEI}ptr[@type='broader']")]}


def oberbegriff(cid):
    """Primärer Oberbegriff über den Zahlencode (knowledge/data.md, B11); sonst der erste."""
    b = BEGRIFF[cid]["broader"]
    if not b:
        return None
    code = cid.split("_")[1]
    passend = [p for p in b if code.startswith(p.split("_")[1].rstrip("0")) and p != cid]
    return max(passend, key=lambda p: len(p.split("_")[1].rstrip("0"))) if passend else b[0]


def pfad(cid):
    kette, seen = [], set()
    while cid and cid not in seen:
        seen.add(cid)
        kette.append(BEGRIFF[cid]["term"])
        cid = oberbegriff(cid)
    return kette[::-1]


def eindeutig(ps):
    s = {MAP.get(p, p) for p in ps}
    return s.pop() if len(s) == 1 else None


fusion_src = Path("goldstandard/verschmelzungen.py").read_text(encoding="utf-8")
fusion_src = fusion_src.replace('sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")', "")
g = {}
_argv, sys.argv = sys.argv, [sys.argv[0]]
import contextlib, io  # noqa: E401
with contextlib.redirect_stdout(io.StringIO()):
    exec(fusion_src, g)
sys.argv = _argv
VERSCHMELZUNG = set(g["treffer"])

AUS2 = {l for l, e in LEX.items() if len(e["senses"]) >= 2
        and len({frozenset(c) for _, c in e["senses"]}) < len(e["senses"])}
AUS3 = {l for l, e in LEX.items() if len(e["senses"]) >= 2 and any(not c for _, c in e["senses"])}
assert all(c in BEGRIFF for e in LEX.values() for _, cs in e["senses"] for c in cs), "Begriffszeiger ins Leere"

aus1 = {}
nur_pos = set()
for r in csv.DictReader(open("goldstandard/ausschluss/ausschluss-tokens.csv", encoding="utf-8")):
    if r["ausschluss"] == "ja":
        aus1[r["xml_id"]] = r["grund"]
    elif r["grund"] == "nur_pos":
        nur_pos.add(r["xml_id"])

GRUPPE = {r["sigle"]: r["hauptgruppe"] for r in
          csv.DictReader(open("goldstandard/obergattungen/texte.csv", encoding="utf-8"))}

# --- Grundgesamtheit ---
W = re.compile(r"<w\s[^>]*>")


def attr(t, k):
    m = re.search(r"\s" + k + r'="([^"]*)"', t)
    return m.group(1) if m else None


zahl = Counter({k: 0 for k in ("basis", "aus_mehrere_lemmaRef", "aus_1_nach_migration", "aus_5_verschmelzung",
                               "aus_2_gleiche_begriffsgruppe", "aus_3_sense_ohne_zeiger")})
tok = []          # (xml_id, sigle, lemma, wortart, herkunft, silber, nur_pos, pos_abweichend)
for f in sorted(Path("tei").glob("*.tei.xml")):
    sig = f.name[:-8]
    if sig in WEG:
        continue
    for m in W.finditer(f.read_text(encoding="utf-8")):
        t = m.group(0)
        ref = attr(t, "lemmaRef")
        if not ref:
            continue
        refs = ref.split()
        lid = refs[0].split("#")[-1]
        if lid not in LEX or len(LEX[lid]["senses"]) < 2:
            continue
        tpos = (attr(t, "pos") or "").split()
        p, herkunft = eindeutig(LEX[lid]["pos"]), "lexikon"
        if p is None:
            p, herkunft = eindeutig(tpos), "token"
        if p not in WORTARTEN:
            continue
        zahl["basis"] += 1
        xid = attr(t, "xml:id")
        if len(refs) > 1:
            zahl["aus_mehrere_lemmaRef"] += 1
            continue
        if xid in aus1:
            zahl["aus_1_nach_migration"] += 1
            continue
        if lid in VERSCHMELZUNG:
            zahl["aus_5_verschmelzung"] += 1
            continue
        if lid in AUS2:
            zahl["aus_2_gleiche_begriffsgruppe"] += 1
            continue
        if lid in AUS3:
            zahl["aus_3_sense_ohne_zeiger"] += 1
            continue
        lexpos = {MAP.get(x, x) for x in LEX[lid]["pos"]}
        abweichend = bool(tpos) and not ({MAP.get(x, x) for x in tpos} & lexpos)
        tok.append((xid, sig, lid, p, herkunft, attr(t, "ana") is not None, xid in nur_pos, abweichend))

zahl["grundgesamtheit"] = len(tok)
silber = defaultdict(lambda: [0, 0])
for x in tok:
    silber[x[1]][0] += x[5]
    silber[x[1]][1] += 1
DOM = {s: ("D1" if a / n >= 0.9 else "D0") for s, (a, n) in silber.items()}

paar_tok = defaultdict(list)
for x in tok:
    paar_tok[(x[2], x[3])].append(x)


def band(n):
    return "1-3" if n <= 3 else "4-20" if n <= 20 else "21-200" if n <= 200 else ">200"


def poly(lid):
    n = len(LEX[lid]["senses"])
    return "2" if n == 2 else "3" if n == 3 else "4+"


zelle = {pr: (poly(pr[0]), pr[1], band(len(ts))) for pr, ts in paar_tok.items()}
gruppe_anteil = Counter(GRUPPE.get(x[1]) or "ohne Gruppe" for x in tok)
T = {k: v / len(tok) for k, v in gruppe_anteil.items()}


def gewicht(x):
    return T[GRUPPE.get(x[1]) or "ohne Gruppe"] ** -0.5


def grenze(sig):
    return 5 if GRUPPE.get(sig) == "Historiografie" else 3


zahl.update({"paare": len(paar_tok), "lemmata": len({p[0] for p in paar_tok}),
             "texte": len(silber), "texte_D1": sum(d == "D1" for d in DOM.values()),
             "tokens_D1": sum(1 for x in tok if DOM[x[1]] == "D1"),
             "pos_abweichend": sum(x[7] for x in tok), "nur_pos_markiert": sum(x[6] for x in tok)})

# --- Ziehung ---
rnd = random.Random(SEED)
benutzt, pro_text, items = set(), Counter(), []
for zp in POLY:
    for zw in WORTARTEN:
        for zb in BAENDER:
            z = (zp, zw, zb)
            for ziel in ["D1"] + ["D0"] * (ZELLE_N - 1):
                for dom in ([ziel, "D0"] if ziel == "D1" else ["D0"]):
                    kand = sorted(pr for pr, zz in zelle.items() if zz == z and pr[0] not in benutzt
                                  and any(DOM[x[1]] == dom and pro_text[x[1]] < grenze(x[1]) for x in paar_tok[pr]))
                    if kand:
                        break
                if not kand:
                    sys.exit(f"Zelle {z} hat kein freies Paar")
                pr = rnd.choice(kand)
                ts = sorted((x for x in paar_tok[pr] if DOM[x[1]] == dom and pro_text[x[1]] < grenze(x[1])),
                            key=lambda x: x[0])
                gw = [gewicht(x) for x in ts]
                x = rnd.choices(ts, weights=gw)[0]
                benutzt.add(pr[0])
                pro_text[x[1]] += 1
                items.append({"item": f"P{len(items) + 1:03d}", "xml_id": x[0], "datei": f"tei/{x[1]}.tei.xml",
                              "sigle": x[1], "lemma": pr[0], "wortart": pr[1], "wortart_herkunft": x[4],
                              "zelle": {"polysemie": zp, "wortart": zw, "band": zb},
                              "senses_im_inventar": len(LEX[pr[0]]["senses"]), "belege_des_paars": len(paar_tok[pr]),
                              "domaene": dom, "domaene_ziel": ziel, "obergattung": GRUPPE.get(x[1]) or "ohne Gruppe",
                              "nur_pos_markiert": x[6], "pos_abweichend": x[7],
                              "p_stufe1": 1 / len(kand), "p_stufe2": gewicht(x) / sum(gw)})

runde0 = sorted(random.Random(f"{SEED}-runde0").sample([i["item"] for i in items], RUNDE0_N))

# --- Kontext und Karten ---
cache = {}


def textdaten(datei):
    if datei in cache:
        return cache[datei]
    tree = etree.parse(datei, etree.XMLParser(collect_ids=False, huge_tree=True))
    titel = (tree.findtext("t:teiHeader/t:fileDesc/t:titleStmt/t:title", namespaces=NS) or "").strip()
    verse = {el: i for i, el in enumerate(tree.iter(f"{TEI}l"))}
    strophe = {el: i for i, el in enumerate(tree.iter(f"{TEI}lg"))}
    toks = []
    for el in tree.find(".//t:text", NS).iter(f"{TEI}w", f"{TEI}pc"):
        anc = list(el.iterancestors())
        if any(a.tag == f"{TEI}note" for a in anc):
            continue
        l = next((a for a in anc if a.tag == f"{TEI}l"), None)
        lg = next((a for a in anc if a.tag == f"{TEI}lg"), None)
        toks.append({"lg": strophe.get(lg),"id": el.get(XID), "t": "".join(el.itertext()).strip(), "pc": el.tag == f"{TEI}pc",
                     "j": el.get("join", ""), "erg": any(a.tag == f"{TEI}supplied" for a in anc),
                     "v": verse[l] if l is not None else None, "vn": l.get("n", "") if l is not None else ""})
    cache[datei] = (titel, toks, {t["id"]: i for i, t in enumerate(toks)})
    return cache[datei]


def ausschnitt(toks, i, art, r):
    if art == "vers":
        v = toks[i]["v"]
        sel = [t for t in toks if t["v"] is not None and v - r <= t["v"] <= v + r]
    else:
        sel = toks[max(0, i - r): i + r + 1]
    zeilen, akt = [], None
    for t in sel:
        key = t["v"] if art == "vers" else 0
        if akt is None or akt["k"] != key:
            neu_strophe = bool(zeilen) and art == "vers" and t["lg"] != zeilen[-1]["lg"]
            akt = {"k": key, "lg": t["lg"], "n": t["vn"] if art == "vers" else "", "w": [], "neu": neu_strophe}
            zeilen.append(akt)
        w = {"t": t["t"]}
        if t["pc"]:
            w["pc"] = 1
        if t["j"]:
            w["j"] = t["j"]
        if t["erg"]:
            w["erg"] = 1
        if t["id"] == toks[i]["id"]:
            w["ziel"] = 1
        akt["w"].append(w)
    return [{"n": z["n"], "w": z["w"], **({"strophe": 1} if z["neu"] else {})} for z in zeilen]


bau = []
for it in items:
    titel, toks, pos = textdaten(it["datei"])
    if it["xml_id"] not in pos:
        sys.exit(f"{it['xml_id']} liegt in <note> und hat keinen Kontext; Seed oder Regel prüfen")
    i = pos[it["xml_id"]]
    art = "vers" if toks[i]["v"] is not None else "prosa"
    std, erw = KONTEXT[art]
    senses = LEX[it["lemma"]]["senses"]
    zaehl = Counter(c for _, cs in senses for c in set(cs))
    karten = [{"sense": sid, "begriffe": [{"id": c, "term": BEGRIFF[c]["term"], "pfad": pfad(c)[:-1],
                                           "eigen": zaehl[c] == 1} for c in cs]} for sid, cs in senses]
    bau.append({"item": it["item"], "xml_id": it["xml_id"], "sigle": it["sigle"], "werk": titel,
                "lemma": it["lemma"], "orth": LEX[it["lemma"]]["orth"], "wortart": it["wortart"],
                "form": toks[i]["t"], "art": art, "vers": toks[i]["vn"],
                "kontext": ausschnitt(toks, i, art, std), "erweitert": ausschnitt(toks, i, art, erw),
                "karten": karten})

# Blindheit: kein Silber, keine Typlisten, keine Token-Attribute im Baumaterial
roh = json.dumps(bau, ensure_ascii=False)
for verboten in ('"ana"', "#type_", "lemmaRef", '"pos"', "meaningRef"):
    assert verboten not in roh, f"Leck im Baumaterial: {verboten}"

tei_hash = hashlib.sha256("".join(f"{p.name}:{sha(p)}\n" for p in sorted(Path("tei").glob("*.tei.xml"))).encode()).hexdigest()
manifest = {
    "schema": "wsd-goldstandard-pilot-manifest-v1",
    "komponente": "Pilot-Pool (Protokoll 4.2)",
    "korpus_commit": voll,
    "korpus_stand": "Upstream a938559dc vom 2026-10-14 (Entscheidung Julia Hintersteiner, 2026-11-12)",
    "skript": "goldstandard/pilot/pilot_ziehen.py",
    "skript_sha256": sha(__file__),
    "seed": SEED,
    "regeln": {"zellen": "Polysemie 2/3/4+ x Wortart NOM/VRB/ADJ x Band 1-3/4-20/21-200/>200",
               "items_pro_zelle": ZELLE_N, "domaenen_pro_zelle": "1 x D1 (sonst D0), 2 x D0",
               "D1": "Text mit mindestens 90 % Silber unter den Tokens der Grundgesamtheit",
               "stufe1": "Paar aus Lemma und Wortart gleich wahrscheinlich, jedes Lemma höchstens einmal",
               "stufe2": "Token gewichtet mit T_G^(-1/2) nach Obergattungsgruppe",
               "obergrenze_pro_text": "3, Historiografie 5 (nur innerhalb des Pools)",
               "wahrscheinlichkeiten": "p_stufe1 und p_stufe2 sind bedingte Auswahlwahrscheinlichkeiten der "
                                       "sequenziellen Ziehung, keine Inklusionswahrscheinlichkeiten",
               "runde0": f"{RUNDE0_N} Items, einfache Zufallsauswahl, Seed '{SEED}-runde0'",
               "kontext_je_seite": {"vers": "2 Verse, erweitert 8", "prosa": "20 Tokens, erweitert 80"},
               "ausschluss_fuer_spaetere_ziehung": "alle Lemmata des Pools, in jeder Wortart"},
    "pruefsummen": {"tei_gesamt": tei_hash,
                    **{p: sha(p) for p in ("authority-files/lexicon.xml", "authority-files/concepts.xml",
                                           "authority-files/genres.xml", "goldstandard/obergattungen/texte.csv",
                                           "goldstandard/verschmelzungen.py",
                                           "goldstandard/ausschluss/ausschluss-tokens.csv")}},
    "ausschlussliste_head_commit": aus_info["head_commit"],
    "zaehlungen": dict(zahl),
    "ausschluss_lemmata": {"2_gleiche_begriffsgruppe": len(AUS2), "3_sense_ohne_zeiger": len(AUS3),
                           "5_verschmelzung": len(VERSCHMELZUNG)},
    "gruppenanteile_grundgesamtheit": {k: round(v, 5) for k, v in sorted(T.items())},
    "runde0": runde0,
    "items": items,
}
OUT.mkdir(parents=True, exist_ok=True)
(OUT / "items-pilot.json").write_text(json.dumps(bau, ensure_ascii=False, indent=1), encoding="utf-8")
manifest["pruefsummen"]["items-pilot.json"] = sha(OUT / "items-pilot.json")
(OUT / "manifest-pilot.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")

print(json.dumps(dict(zahl), ensure_ascii=False))
print("Items", len(items), "| aus D1", sum(i["domaene"] == "D1" for i in items),
      "| Ersatz D0 statt D1", sum(i["domaene"] != i["domaene_ziel"] for i in items))
print("Gruppen", dict(Counter(i["obergattung"] for i in items)))
print("Kontext", dict(Counter(b["art"] for b in bau)), "| Texte", len(pro_text), "| max pro Text", max(pro_text.values()))
print("Runde 0:", " ".join(runde0))
