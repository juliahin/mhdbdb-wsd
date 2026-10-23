"""Prüft Annahmen über die Daten an den Originaleinträgen. Aufruf aus dem Repo-Root."""
from collections import Counter, defaultdict
from pathlib import Path
import json, re, sys

from lxml import etree

TEI = "{http://www.tei-c.org/ns/1.0}"
XID = "{http://www.w3.org/XML/1998/namespace}id"
XL = "{http://www.w3.org/XML/1998/namespace}lang"
R = {}

# ---------- Lexikon ----------
lx = etree.parse("authority-files/lexicon.xml")
senses = {}          # lemma -> [sense ids in Dokumentreihenfolge]
stypes = {}          # sense -> set(type ids) aus sense/@ana
sptr = {}            # sense -> frozenset(concept ids)
lpos = {}            # lemma -> [pos]
orth = {}
gram_n = Counter(); pos_n = Counter(); sense_attrs = Counter(); sense_children = Counter()
for e in lx.iter(f"{TEI}entry"):
    lid = e.get(XID)
    o = e.find(f"{TEI}form/{TEI}orth"); orth[lid] = o.text if o is not None else ""
    gg = e.findall(f"{TEI}gramGrp"); gram_n[len(gg)] += 1
    ps = [p.text for p in e.iter(f"{TEI}pos")]; lpos[lid] = ps; pos_n[len(ps)] += 1
    senses[lid] = []
    for s in e.findall(f"{TEI}sense"):
        sid = s.get(XID); senses[lid].append(sid)
        for k in s.attrib: sense_attrs[k] += 1
        for c in s: sense_children[etree.QName(c).localname] += 1
        stypes[sid] = set(x.lstrip("#") for x in (s.get("ana") or "").split())
        sptr[sid] = frozenset(p.get("target").split("#")[-1] for p in s.findall(f"{TEI}ptr"))
sense2lemma = {s: l for l, ss in senses.items() for s in ss}
R["lexikon"] = {
    "eintraege": len(senses), "senses": len(sense2lemma),
    "gramGrp_pro_eintrag": dict(gram_n), "pos_pro_eintrag": dict(pos_n),
    "sense_attribute": dict(sense_attrs), "sense_kinder": dict(sense_children),
    "senses_ohne_typliste": sum(1 for s in stypes if not stypes[s]),
}
# Reihenfolge der Senses = numerische Reihenfolge der IDs?
def num(s): return int(s.rsplit("_", 1)[1])
R["lexikon"]["sense_reihenfolge_gleich_id_reihenfolge"] = sum(
    1 for l, ss in senses.items() if len(ss) > 1 and [num(x) for x in ss] == sorted(num(x) for x in ss))
R["lexikon"]["polyseme_lemmata"] = sum(1 for ss in senses.values() if len(ss) > 1)
# Typ in mehreren Senses desselben Lemmas?
typ_in_senses = Counter()
for l, ss in senses.items():
    if len(ss) < 2: continue
    c = Counter(t for s in ss for t in stypes[s])
    for t, n in c.items(): typ_in_senses[min(n, 4)] += 1
R["lexikon"]["typen_polysemer_lemmata_nach_zahl_der_senses_mit_diesem_typ"] = dict(typ_in_senses)

# ---------- Begriffe ----------
cx = etree.parse("authority-files/concepts.xml")
cdesc = {}; broader = {}
for c in cx.iter(f"{TEI}category"):
    i = c.get(XID)
    de = [t.text for t in c.findall(f"{TEI}catDesc/{TEI}term[@{XL}='de']") if t.get("type") is None]
    cdesc[i] = de[0] if de else None
    broader[i] = [p.get("target").lstrip("#") for p in c.findall(f"{TEI}catDesc/{TEI}ptr[@type='broader']")]
used = Counter(c for s in sptr.values() for c in s)
R["begriffe"] = {
    "kategorien": len(cdesc), "ohne_deutschen_term": sum(1 for v in cdesc.values() if not v),
    "mit_mehreren_broader": sum(1 for v in broader.values() if len(v) > 1),
    "ohne_broader": sum(1 for v in broader.values() if not v),
    "zeiger_ins_leere": sum(n for c, n in used.items() if c not in cdesc),
    "ziele_ins_leere": sorted(c for c in used if c not in cdesc)[:10],
    "benutzte_kategorien": len(used),
    "namen_kategorien": sum(1 for v in cdesc.values() if v and v.endswith("/Namen")),
}
# Polyhierarchie: broader, das zugleich Vorfahr eines anderen broader ist (wie in genres.xml)?
def anc(i, seen=None):
    seen = set() if seen is None else seen
    for p in broader.get(i, []):
        if p not in seen: seen.add(p); anc(p, seen)
    return seen
red = {i: [p for p in ps if not any(p in anc(q) for q in ps if q != p)] for i, ps in broader.items()}
R["begriffe"]["mehrere_broader_nach_reduktion"] = sum(1 for v in red.values() if len(v) > 1)
# Stimmt der Zahlencode mit broader überein? (Präfix-Hierarchie)
def code_parent(i):
    d = i.split("_")[1].rstrip("0")
    return d
mism = 0; chk = 0
for i, ps in red.items():
    for p in ps:
        chk += 1
        if not code_parent(i).startswith(code_parent(p)): mism += 1
R["begriffe"]["broader_kanten_reduziert"] = chk
R["begriffe"]["broader_kanten_gegen_zahlencode"] = mism

# ---------- Korpus ----------
W = re.compile(r"<w\s[^>]*>"); A = lambda t, k: (m.group(1) if (m := re.search(r"\s" + k + r'="([^"]*)"', t)) else None)
c = Counter()
lem_multi = []; ana_multi = []; ana_foreign = []; ana_dangling = []; ana_nolemma = []
obs_types = defaultdict(set)        # sense -> beobachtete Typen (Tokens mit diesem Sense)
silver = defaultdict(Counter)       # lemma -> Counter(sense)
type_sense = defaultdict(Counter)   # (lemma,type) -> Counter(sense)
mono = defaultdict(lambda: [0, 0])  # text -> [mono tokens, davon mit ana]
poly = defaultdict(lambda: [0, 0])
tok_pos_forms = Counter()
type_in_list = Counter()
for f in sorted(Path("tei").glob("*.tei.xml")):
    sig = f.name[:-8]
    for m in W.finditer(f.read_text(encoding="utf-8")):
        t = m.group(0); lem = A(t, "lemmaRef"); ana = A(t, "ana"); cor = A(t, "corresp"); pos = A(t, "pos")
        if not lem:
            if ana: ana_nolemma.append((sig, A(t, "xml:id")))
            continue
        c["tokens_lemmatisiert"] += 1
        ls = [x.split("#")[-1] for x in lem.split()]
        if len(ls) > 1: lem_multi.append((sig, A(t, "xml:id"), lem))
        lid = ls[0]
        if pos: tok_pos_forms[len(pos.split())] += 1
        n = len(senses.get(lid, []))
        if lid not in senses: c["lemmaRef_ins_leere"] += 1; continue
        (mono if n == 1 else poly)[sig][0] += 1
        if not ana: continue
        (mono if n == 1 else poly)[sig][1] += 1
        ss = [x.split("#")[-1] for x in ana.split()]
        if len(ss) > 1: ana_multi.append((sig, A(t, "xml:id"), ana))
        s = ss[0]
        if s not in sense2lemma: ana_dangling.append((sig, A(t, "xml:id"), ana)); continue
        if sense2lemma[s] != lid: ana_foreign.append((sig, A(t, "xml:id"), lem, ana)); continue
        ty = cor.split("#")[-1] if cor else None
        if ty: obs_types[s].add(ty)
        if n > 1:
            silver[lid][s] += 1
            if ty:
                type_sense[(lid, ty)][s] += 1
                type_in_list["typ_in_liste_des_sense" if ty in stypes[s] else "typ_nicht_in_liste"] += 1
                k = sum(1 for x in senses[lid] if ty in stypes[x])
                type_in_list[f"typ_in_{min(k,3)}_senselisten"] += 1

R["korpus"] = dict(c)
R["korpus"].update({
    "lemmaRef_mehrwertig": len(lem_multi), "lemmaRef_mehrwertig_beispiele": lem_multi[:5],
    "ana_mehrwertig": len(ana_multi), "ana_mehrwertig_beispiele": ana_multi[:5],
    "ana_fremdes_lemma": len(ana_foreign), "ana_fremdes_lemma_beispiele": ana_foreign[:8],
    "ana_ins_leere": len(ana_dangling), "ana_ins_leere_beispiele": ana_dangling[:5],
    "ana_ohne_lemmaRef": len(ana_nolemma),
    "token_pos_zahl_der_werte": dict(tok_pos_forms),
    "silber_polysem_typcheck": dict(type_in_list),
})

# sense/@ana-Typliste == beobachtete Typen?
cmp = Counter()
for s, tl in stypes.items():
    ob = obs_types.get(s, set())
    if not ob and not tl: cmp["beide_leer"] += 1
    elif tl == ob: cmp["gleich"] += 1
    elif ob < tl: cmp["liste_echte_obermenge"] += 1
    elif tl < ob: cmp["liste_echte_teilmenge"] += 1
    else: cmp["ueberlappend_oder_disjunkt"] += 1
R["typliste_gegen_korpus"] = dict(cmp)

# Ist der erste Sense im Lexikon der MFS im Silber?
first = Counter(); unatt = Counter()
for l, cn in silver.items():
    ss = senses[l]
    first["erster_ist_mfs" if cn.most_common(1)[0][0] == ss[0] else "erster_nicht_mfs"] += 1
    for s in ss: unatt["belegt" if cn[s] else "unbelegt"] += 1
R["sense_reihenfolge_mfs"] = dict(first)
R["inventar_senses_polysemer_lemmata_mit_silber"] = dict(unatt)
# Polyseme Lemmata ganz ohne Silber
R["polyseme_lemmata_ohne_silber"] = sum(1 for l, ss in senses.items() if len(ss) > 1 and l not in silver)

# Monoseme Tokens: @ana-Abdeckung pro Text
cov = Counter()
for sig, (n, a) in mono.items():
    if n: cov["voll" if a == n else ("null" if a == 0 else "teilweise")] += 1
R["monosem_ana_abdeckung_texte"] = dict(cov)
R["monosem_tokens_ohne_ana"] = sum(n - a for n, a in mono.values())
R["monosem_tokens"] = sum(n for n, a in mono.values())
R["monosem_luecken_texte"] = sorted(((sig, n - a, n) for sig, (n, a) in mono.items() if n - a), key=lambda x: -x[1])[:10]

# Typ -> mehrere Senses: wie viele Typen sind gemischt, und sind die gemischten Typen in mehreren Senselisten?
mix = Counter()
for (l, ty), cn in type_sense.items():
    gemischt = len(cn) > 1
    k = sum(1 for x in senses[l] if ty in stypes[x])
    mix[("gemischt" if gemischt else "einheitlich") + f"_in_{min(k,3)}_listen"] += 1
R["lemma_typ_kombinationen"] = dict(mix)

json.dump(R, sys.stdout, ensure_ascii=False, indent=1, default=list)
