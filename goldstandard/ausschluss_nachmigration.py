"""
Ausschlussliste für die Goldstandard-Stichprobe: alle Tokens, deren Annotation
nach der Migration verändert wurde (Protokoll, Abschnitt 3, Punkt 1).

Aufruf aus dem Repo-Wurzelverzeichnis:
    python goldstandard/ausschluss_nachmigration.py

Warum ein Git-Vergleich und nicht die Ingest-Logs:
Die LLM-Läufe (#189, #198, #216, #369, #387 ...) mischen regelbasierte Schritte,
LLM-Entscheidungen und Einzelentscheidungen von KZW, und nicht jeder Lauf führt
eine Liste der geänderten Token-IDs. Der Vergleich jedes Tokens mit seinem
Zustand direkt nach der Migration erfasst dagegen jede Änderung, auch ungeloggte.
Die Ingest-Listen dienen nur der Herkunftsangabe.

Regel (betrachtet werden nur Tokens, die heute @lemmaRef tragen):
  ausschluss=ja, wenn
  - das Token in einem Text liegt, der nach der Baseline ingestiert wurde (WZB), oder
  - seine xml:id in der Baseline nicht existiert, oder
  - sich @lemmaRef oder der Sense (@ana, früher @meaningRef) unterscheidet.
  ausschluss=nein, nur markiert, wenn sich ausschließlich @pos unterscheidet:
  Lemma und Sense sind dann unverändert, die Annotator:innen sehen @pos nicht,
  und die Wortart für die Schichtung kommt aus lexicon.xml. Ein Ausschluss
  würde zudem gezielt die Fachliteratur treffen (AC1-AC3, FLG aus #32).
@corresp wird ignoriert: Es verknüpft nur den Variantentyp und berührt weder
Lemma noch Bedeutung.

Ausgabe:
  goldstandard/ausschluss/ausschluss-tokens.csv   eine Zeile pro Token
  goldstandard/ausschluss/zusammenfassung.json    Zählungen, Commits und die
      ganz ausgeschlossenen Texte (diese stehen nicht Token für Token in der CSV)
"""

from collections import Counter, defaultdict
from pathlib import Path
import csv
import json
import re
import subprocess

BASELINE = "0422429fc"   # 2025-07-23, Stand nach der Migration (666 Texte)
TEI_DIR = Path("tei")
INGEST = Path("ingest/pos-disambig")
OUT = Path("goldstandard/ausschluss")
OUT.mkdir(parents=True, exist_ok=True)

W_TAG = re.compile(r"<w\s[^>]*>", re.S)
ATTR = {k: re.compile(r'\s' + k + r'="([^"]*)"') for k in ("xml:id", "lemmaRef", "ana", "meaningRef", "pos")}


def git(*args):
    return subprocess.run(["git", *args], capture_output=True, check=True).stdout


def tokens(xml_text):
    """xml:id -> (lemmaRef, Sense, pos) für jedes <w>.

    Das Sense-Attribut hieß in der Baseline @meaningRef und wurde am 2026-04-09
    in @ana umbenannt (#32, Commit 3ec3a5f16). Gelesen wird, was vorhanden ist.
    """
    out = {}
    for m in W_TAG.finditer(xml_text):
        tag = m.group(0)
        vals = {}
        for k, rx in ATTR.items():
            hit = rx.search(tag)
            vals[k] = hit.group(1) if hit else None
        if vals["xml:id"]:
            out[vals["xml:id"]] = (vals["lemmaRef"], vals["ana"] or vals["meaningRef"], vals["pos"])
    return out


# ---------------------------------------------------------------------------
# Herkunft: welche Token-IDs nennen die Ingest-Läufe?
# ---------------------------------------------------------------------------
herkunft = defaultdict(set)   # xml_id -> {Laufname}
for d in sorted(p for p in INGEST.iterdir() if p.is_dir()):
    for f in list(d.glob("diff-liste.csv")) + list(d.glob("faelle.csv")):
        with open(f, encoding="utf-8-sig", newline="") as fh:
            header = fh.readline()   # Trennzeichen nur aus der Kopfzeile, die Kontextspalten enthalten Kommas
            fh.seek(0)
            delim = ";" if header.count(";") > header.count(",") else ","
            for row in csv.DictReader(fh, delimiter=delim):
                xid = (row.get("xml_id") or row.get("wort_id") or row.get("id") or "").strip()
                if xid:
                    herkunft[xid].add(d.name)
    ids = d / "ids.txt"
    if ids.exists():
        for line in ids.read_text(encoding="utf-8").split():
            herkunft[line.strip()].add(d.name)

# ---------------------------------------------------------------------------
# Vergleich heute gegen Baseline
# ---------------------------------------------------------------------------
baseline_files = {Path(p).name for p in git("ls-tree", "--name-only", BASELINE, "tei/").decode().split()}
head = git("rev-parse", "HEAD").decode().strip()
dirty = bool(git("status", "--porcelain", "--", "tei/").strip())

rows = []
stat = Counter()
neue_texte = {}   # ganz ausgeschlossene Texte -> Anzahl lemmatisierter Tokens
for f in sorted(TEI_DIR.glob("*.tei.xml")):
    now = tokens(f.read_text(encoding="utf-8"))
    lemmatized = {k: v for k, v in now.items() if v[0]}
    stat["tokens_lemmatisiert"] += len(lemmatized)
    if f.name not in baseline_files:
        neue_texte[f.name] = len(lemmatized)
        stat["neuer_text"] += len(lemmatized)
        continue
    old = tokens(git("show", f"{BASELINE}:tei/{f.name}").decode("utf-8"))
    for xid, (lem, ana, pos) in lemmatized.items():
        if xid not in old:
            grund, felder, aus = "neue_id", "", "ja"
        else:
            o_lem, o_ana, o_pos = old[xid]
            diff = [n for n, a, b in (("lemmaRef", lem, o_lem), ("ana", ana, o_ana), ("pos", pos, o_pos)) if a != b]
            if not diff:
                continue
            felder = "+".join(diff)
            if diff == ["pos"]:
                grund, aus = "nur_pos", "nein"
            else:
                grund, aus = "lemma_oder_sense", "ja"
        rows.append((f.name, xid, grund, felder, "|".join(sorted(herkunft.get(xid, ()))), aus))
        stat[grund] += 1

with open(OUT / "ausschluss-tokens.csv", "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["datei", "xml_id", "grund", "geaenderte_felder", "ingest_lauf", "ausschluss"])
    w.writerows(rows)

felder = Counter(r[3] for r in rows if r[3])
nur_pos_texte = Counter(r[0] for r in rows if r[2] == "nur_pos")
laeufe = Counter()
ohne_log = 0
for r in rows:
    if r[2] == "neuer_text":
        continue
    if r[4]:
        for lauf in r[4].split("|"):
            laeufe[lauf] += 1
    else:
        ohne_log += 1

summary = {
    "baseline_commit": BASELINE,
    "head_commit": head,
    "tei_mit_lokalen_aenderungen": dirty,
    "tokens_lemmatisiert_heute": stat["tokens_lemmatisiert"],
    "ausgeschlossene_texte": neue_texte,
    "ausgeschlossen": stat["neuer_text"] + sum(1 for r in rows if r[5] == "ja"),
    "nur_markiert": sum(1 for r in rows if r[5] == "nein"),
    "nach_grund": {k: stat[k] for k in ("neuer_text", "neue_id", "lemma_oder_sense", "nur_pos")},
    "geaendert_nach_feldern": dict(felder.most_common()),
    "herkunft_ingest_lauf": dict(laeufe.most_common()),
    "geaendert_ohne_ingest_log": ohne_log,
    "texte_mit_ausschluessen": len({r[0] for r in rows if r[5] == "ja"} | set(neue_texte)),
    "groesste_texte_ausschluss": Counter(r[0] for r in rows if r[5] == "ja").most_common(15),
    "nur_pos_nach_text": nur_pos_texte.most_common(),
}
(OUT / "zusammenfassung.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
print(json.dumps(summary, ensure_ascii=False, indent=2))
