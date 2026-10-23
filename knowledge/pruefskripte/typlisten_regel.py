# Ist bei gemischten Typen der Listen-Sense der mit der höchsten / niedrigsten ID unter den belegten Senses?
import re
from collections import Counter, defaultdict
from pathlib import Path
lex=Path("authority-files/lexicon.xml").read_text(encoding="utf-8")
senses=defaultdict(list); t2s={}
for m in re.finditer(r'<entry xml:id="(lemma_\d+)">(.*?)</entry>',lex,re.S):
    for s in re.finditer(r'<sense xml:id="([^"]+)"(?: ana="([^"]*)")?',m.group(2)):
        senses[m.group(1)].append(s.group(1))
        for t in (s.group(2) or "").split(): t2s[(m.group(1),t.lstrip('#'))]=s.group(1)
ts=defaultdict(Counter)
A=lambda t,k:(m.group(1) if (m:=re.search(r"\s"+k+r'="([^"]*)"',t)) else None)
for f in Path("tei").glob("*.tei.xml"):
    for m in re.finditer(r"<w\s[^>]*>",f.read_text(encoding="utf-8")):
        t=m.group(0); a=A(t,"ana"); l=A(t,"lemmaRef"); c=A(t,"corresp")
        if not(a and l and c): continue
        l=l.split('#')[-1]
        if len(senses[l])<2: continue
        ts[(l,c.split('#')[-1])][a.split('#')[-1]]+=1
n=lambda s:int(s.rsplit('_',1)[1]); r=Counter()
for k,cn in ts.items():
    cn=Counter({s:v for s,v in cn.items() if s in senses[k[0]]})
    if len(cn)<2 or k not in t2s: continue
    ls=t2s[k]; ids=sorted(cn,key=n)
    r["hoechste_id"]+= ls==ids[-1]; r["niedrigste_id"]+= ls==ids[0]; r["mehrheit"]+= ls==cn.most_common(1)[0][0]
    r["erster_im_lexikon"]+= ls==min(cn,key=senses[k[0]].index); r["gemischt"]+=1
print(dict(r))
