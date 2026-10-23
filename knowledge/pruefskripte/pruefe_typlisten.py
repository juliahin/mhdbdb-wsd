"""Typlisten an den Senses gegen die Token-Annotation; Ins-Leere-Verweise; Senses ohne Zeiger."""
from collections import Counter, defaultdict
from pathlib import Path
import json, re, sys, random

lex = Path("authority-files/lexicon.xml").read_text(encoding="utf-8")
senses, stypes, sptr, lpos, orth = defaultdict(list), {}, {}, {}, {}
for m in re.finditer(r'<entry xml:id="(lemma_\d+)">(.*?)</entry>', lex, re.S):
    lid, body = m.groups()
    lpos[lid] = re.findall(r"<pos>([^<]+)</pos>", body)
    orth[lid] = re.search(r"<orth>([^<]*)</orth>", body).group(1)
    for s in re.finditer(r'<sense xml:id="([^"]+)"(?: ana="([^"]*)")?>(.*?)</sense>', body, re.S):
        sid = s.group(1); senses[lid].append(sid)
        stypes[sid] = set(x.lstrip("#") for x in (s.group(2) or "").split())
        sptr[sid] = frozenset(re.findall(r'concepts\.xml#(concept_\d+)', s.group(3)))
s2l = {s: l for l, ss in senses.items() for s in ss}
typ2sense = {}
for l, ss in senses.items():
    for s in ss:
        for t in stypes[s]: typ2sense[(l, t)] = s

W = re.compile(r"<w\s[^>]*>")
A = lambda t, k: (m.group(1) if (m := re.search(r"\s" + k + r'="([^"]*)"', t)) else None)
ts = defaultdict(Counter)        # (lemma,type) -> Counter(sense)  nur polyseme, Silber
dangl = Counter(); dangl_pos = Counter(); dangl_texts = Counter()
nolist_tok = Counter()           # polyseme Silber-Tokens, deren Typ in keiner Liste steht
poly_unann_typ = Counter()
beispiele = defaultdict(list)
for f in sorted(Path("tei").glob("*.tei.xml")):
    sig = f.name[:-8]
    for m in W.finditer(f.read_text(encoding="utf-8")):
        t = m.group(0); lem = A(t, "lemmaRef")
        if not lem: continue
        lid = lem.split("#")[-1]; ana = A(t, "ana"); cor = A(t, "corresp"); ty = cor.split("#")[-1] if cor else None
        if ana:
            s = ana.split("#")[-1]
            if s not in s2l:
                dangl[(lid, s)] += 1; dangl_pos[A(t, "pos")] += 1; dangl_texts[sig] += 1; continue
        if len(senses.get(lid, [])) < 2: continue
        if not ana:
            poly_unann_typ["typ_in_liste" if (lid, ty) in typ2sense else "typ_in_keiner_liste"] += 1
            continue
        if ty is None: continue
        ts[(lid, ty)][s] += 1
        if (lid, ty) in typ2sense and typ2sense[(lid, ty)] != s and len(beispiele[lid]) < 3:
            beispiele[lid].append((A(t, "xml:id"), ty, s, typ2sense[(lid, ty)]))

R = {}
# Ist der Listen-Sense eines Typs der Mehrheitssense des Typs im Silber?
c = Counter(); tok = Counter()
for (l, ty), cn in ts.items():
    ls = typ2sense.get((l, ty))
    if ls is None: c["typ_in_keiner_liste"] += 1; continue
    top = cn.most_common(); best = top[0][1]
    maj = {s for s, n in top if n == best}
    key = ("listensense_ist_mehrheit" if ls in maj and len(maj) == 1 else
           "listensense_gleichauf_mehrheit" if ls in maj else
           "listensense_belegt_aber_minderheit" if cn[ls] else "listensense_im_silber_nie_belegt")
    c[key] += 1; tok[key] += sum(cn.values())
    tok["tokens_mit_listensense" if True else ""] += cn[ls]
R["typ_kombinationen_nach_listensense"] = dict(c)
R["tokens_nach_listensense_kategorie"] = dict(tok)
R["silber_poly_tokens"] = sum(sum(cn.values()) for cn in ts.values())
R["polyseme_unannotierte_tokens_typ"] = dict(poly_unann_typ)
R["ana_ins_leere"] = {"tokens": sum(dangl.values()), "paare": len(dangl),
                      "pos": dict(dangl_pos), "texte": dict(dangl_texts.most_common(12)),
                      "lemmata": sorted({(l, orth.get(l), tuple(lpos.get(l, [])), len(senses.get(l, []))) for l, s in dangl})}
# Senses ohne Begriffszeiger, identische Begriffsgruppen
R["senses_ohne_zeiger"] = sum(1 for s, p in sptr.items() if not p)
R["lemmata_mit_sense_ohne_zeiger_polysem"] = len({s2l[s] for s, p in sptr.items() if not p and len(senses[s2l[s]]) > 1})
R["lemmata_mit_identischen_begriffsgruppen"] = sum(
    1 for l, ss in senses.items() if len(ss) > 1 and len({sptr[s] for s in ss}) < len(ss))
random.seed(1)
R["beispiele_abweichung_von_typliste"] = {l: (orth[l], v) for l, v in random.sample(sorted(beispiele.items()), 12)}
json.dump(R, sys.stdout, ensure_ascii=False, indent=1, default=list)
