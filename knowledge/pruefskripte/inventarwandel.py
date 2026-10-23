import re, sys
from collections import Counter, defaultdict
from pathlib import Path
def load(p):
    d=defaultdict(list)
    for m in re.finditer(r'<sense xml:id="(lemma_\d+)_sense_(\d+)"',Path(p).read_text(encoding="utf-8")): d[m.group(1)].append(m.group(2))
    return d
now=load("authority-files/lexicon.xml"); base=load(sys.argv[1])
r=Counter()
for l,ss in now.items():
    b=base.get(l,[])
    if len(ss)>1:
        r["poly_jetzt"]+=1
        if len(b)<=1: r["poly_jetzt_mono_oder_neu_damals"]+=1
        elif set(ss)!=set(b): r["poly_beide_aber_inventar_geaendert"]+=1
r["senses_jetzt"]=sum(map(len,now.values())); r["senses_baseline"]=sum(map(len,base.values()))
r["senses_neu"]=sum(1 for l,ss in now.items() for s in ss if s not in base.get(l,[]))
r["senses_weg"]=sum(1 for l,ss in base.items() for s in ss if s not in now.get(l,[]))
print(dict(r))
chg={l for l,ss in now.items() if len(ss)>1 and set(ss)!=set(base.get(l,[]))}
mono_then={l for l in chg if len(base.get(l,[]))<=1}
# Silber-Tokens dieser Lemmata
A=lambda t,k:(m.group(1) if (m:=re.search(r"\s"+k+r'="([^"]*)"',t)) else None)
c=Counter(); per=Counter()
for f in Path("tei").glob("*.tei.xml"):
    for m in re.finditer(r"<w\s[^>]*>",f.read_text(encoding="utf-8")):
        t=m.group(0); l=A(t,"lemmaRef")
        if not l: continue
        l=l.split("#")[-1]
        if l in chg:
            k="mono_damals" if l in mono_then else "inventar_geaendert"
            c[k+"_tokens"]+=1
            if A(t,"ana"): c[k+"_mit_ana"]+=1; per[l]+=1
print(dict(c)); print([(l,n) for l,n in per.most_common(15)])
