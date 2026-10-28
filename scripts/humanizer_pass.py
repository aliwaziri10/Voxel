#!/usr/bin/env python3
"""
humanizer_pass.py v2 - the standard humanizer check for Voxel novel chapters.

WHAT IT GIVES YOU
  HUMAN SCORE, 0 to 100. HIGHER = MORE HUMAN-LIKE. (humanizer.py's own score
  is the opposite way round: lower is cleaner. Both are printed.)
  Plus a FIX LIST: the exact sentences to edit, with the reason for each.

It READS only. It never edits a chapter. No API key, no cost, standard
library only. Internet is needed only the first time (downloads public-domain
novels as a human baseline, then caches them).

A high score is NOT proof of human authorship and no tool can give that.
The score is a heuristic built from published AI-tell research. Record the
numbers in the book's PROOFREAD_TRACKER.md. The KDP AI-content question must
still be answered truthfully.

USAGE (from the repo root)
  python scripts/humanizer_pass.py novels/warm-enough/chapters/chapter_02.md --n 2
  python scripts/humanizer_pass.py novels/warm-enough/chapters/chapter_02.md --n 2 --fixes 60
  python scripts/humanizer_pass.py --book warm-enough
  python scripts/humanizer_pass.py --selftest

WHAT THE SCORE IS MADE OF (weights add to 100; each is the MOST it can cost)
  Sources: Wikipedia "Signs of AI writing" (rule of three, negative
  parallelism, hedging, summary closers), StoryScope (arXiv 2604.03136:
  AI fiction over-states its theme, shows feeling only through the body,
  ends tidy, uses less dialogue), stylometry research (sentence rhythm,
  vocabulary variety, repeated phrasing), and public blocklists of AI
  character names. See WEIGHTS below. The first group is measured against
  the human baseline (a measure only costs points when it falls OUTSIDE the
  human 10th to 90th percentile band). The second group has no baseline and
  targets zero or a fixed ceiling.

HONEST LIMITS
  * The baseline is 19th-century prose (Austen, Chesterton, Melville and
    others), so sentence LENGTH is not scored. Read gaps with care.
  * Closer-zinger, tic-phrase and cliche checks are heuristics, not
    calibrated against Voxel books.
  * Fixing the score by mechanical shuffling does not make prose better.
    Edit for voice first, then re-run.
"""
import argparse, collections, glob, io, json, re, statistics as st, subprocess, sys, urllib.request, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
CACHE = ROOT / "scripts" / ".humanizer_baseline.json"
CACHE_VERSION = 2
URL = "https://raw.githubusercontent.com/nltk/nltk_data/gh-pages/packages/corpora/gutenberg.zip"
NAMES = ["austen-emma", "austen-persuasion", "austen-sense", "chesterton-ball", "chesterton-brown",
         "chesterton-thursday", "carroll-alice", "bryant-stories", "melville-moby_dick", "edgeworth-parents"]
WIN = 2300

# ---------------------------------------------------------------- weights
# name: (max points lost, short label)
WEIGHTS = {
    "scan":       (14, "repo humanizer.scan score (word and phrase tells)"),
    "pron_open":  (14, "sentences opening he/she/they/her/his"),
    "anaph_runs": (8,  "runs of 3+ sentences with the same first word"),
    "short":      (6,  "share of very short sentences (5 words or fewer)"),
    "cv":         (6,  "sentence-length variation (too flat or too jumpy)"),
    "ttr":        (3,  "vocabulary variety (type-token ratio)"),
    "rep4":       (3,  "repeated four-word phrases"),
    "simile":     (4,  "simile frames ('as if', 'as though', 'like a') per 1000 words"),
    "stated":     (8,  "'realized/understood/knew that' (feeling or theme stated outright)"),
    "tics":       (7,  "repeated tic phrases (3+ words, or 'and laughed' style tails)"),
    "closer":     (3,  "paragraphs ending on a short zinger sentence"),
    "cliche":     (10, "stock fiction gestures (breath held, heart hammered, silence stretched)"),
    "neg_par":    (6,  "negative parallelism ('not X, but Y' / 'It wasn't X. It was Y.')"),
    "names":      (3,  "character/place names on AI-overuse blocklists"),
    "dialogue":   (5,  "dialogue share too low against human fiction"),
}
assert sum(v[0] for v in WEIGHTS.values()) == 100, "weights must add to 100"

STOP = set("a an and are as at be but by for from had has have he her him his i in is it its me my no not of on "
           "or our she so than that the their them then there they this to up us was we were what when which "
           "who will with you your into out over down back all one if said".split())

CLICHES = [
    r"breath (?:he|she|they|i) (?:didn'?t|did not|hadn'?t|had not) (?:know|realize|realise)",
    r"(?:let|lets|letting) out a (?:slow |long |shaky |deep |soft )?breath",
    r"(?:released|exhaled|released) a (?:slow |long |shaky |deep |soft )?breath",
    r"\bheart (?:hammered|pounded|raced|thudded|skipped|stuttered|lurched|clenched)\b",
    r"\b(?:shiver|chill) (?:ran|went|crept|traveled|travelled|slid|rippled) (?:down|up|through)\b",
    r"\bsomething (?:in (?:him|her|them|the air) )?(?:shifted|cracked|broke|snapped|stirred|unfurled)\b",
    r"\bair between (?:them|us)\b",
    r"\bsilence (?:stretched|hung|settled|thickened|pressed)\b",
    r"\b(?:barely|hardly) (?:above|more than) a whisper\b",
    r"\bfor a long (?:moment|beat|while)\b",
    r"\bcouldn'?t help (?:but|herself|himself)\b",
    r"\beyes (?:darkened|glittered|sparkled|flashed|softened)\b",
    r"\bjaw (?:tightened|clenched|ticked|worked)\b",
    r"\bknuckles (?:white|whitened|went white)\b",
    r"\bswallowed hard\b",
    r"\btension (?:hung|crackled|thickened|filled|rolled)\b",
    r"\btime (?:seemed to (?:slow|stop|stand)|slowed|stood still)\b",
    r"\ba (?:mix|mixture|blend|swirl) of [a-z]+ and [a-z]+\b",
    r"\bsomewhere in the distance\b",
    r"\bthe weight of (?:it|the|his|her|their|what)\b",
    r"\b(?:ghost of a|small|soft|tiny|quiet) smile (?:tugged|played|touched|ghosted|curved)\b",
    r"\bwhat (?:felt|seemed) like (?:hours|an eternity|forever)\b",
    r"\bheld (?:his|her|their) breath\b",
]
CLICHE_RE = [re.compile(p, re.I) for p in CLICHES]

# From public discussions of LLM fiction naming habits (Max Read "Who is Elara
# Voss?", NameGenHub). A partial list. A hit is a prompt to rename, not proof.
AI_NAMES = {"Elara", "Elena", "Elias", "Aris", "Kael", "Voss", "Vex", "Vance", "Thorne",
            "Erebus", "Eldora", "Whispering"}
AI_NAME_RE = re.compile(r"\b(" + "|".join(sorted(AI_NAMES)) + r")\b")

NEG_PAR_RE = re.compile(
    r"\b(?:it|this|that|he|she|they|there)\s+(was|were|is|did|had|could)(?:n'?t|\s+not)\s+[^.;!?]{2,70}"
    r"[.;,]\s*(?:it|this|that|he|she|they|there)\s+\1\b"
    r"|\bnot\s+(?:just|only|merely|simply)\s+[^.;!?]{2,50},?\s+(?:but|it|he|she|they)\b"
    r"|\bnot\s+[a-z]+,\s+but\s+[a-z]+", re.I)
STATED_RE = re.compile(r"\b(?:realized|realised|understood|knew|saw)\s+(?:then\s+|now\s+)?that\b", re.I)
AS_IF_RE = re.compile(r"\bas (?:if|though)\b", re.I)
LIKE_A_RE = re.compile(r"\blike (?:a|an|the)\b", re.I)
THE_WAY_RE = re.compile(r"\bthe way\b", re.I)
TAIL_RE = re.compile(r"\b(?:and|then)\s+(\w+ed|laughed|nodded|smiled|sighed|shrugged)\b", re.I)


# ---------------------------------------------------------------- text tools
def sents(t):
    t = re.sub(r"\s+", " ", t)
    return [s.strip() for s in re.split(r"(?<=[.!?])[\"”’']*\s+(?=[\"“‘']*[A-Z])", t) if s.strip()]


def words(t):
    return re.findall(r"[A-Za-z']+", t.lower())


def paragraphs(t):
    out = []
    for p in re.split(r"\n\s*\n", t):
        p = "\n".join(l for l in p.splitlines() if not l.lstrip().startswith("#")).strip()
        if p:
            out.append(p)
    return out


# ---------------------------------------------------------------- metrics
def metrics(t):
    """The nine ORIGINAL measures (same definitions as the first version, so
    numbers already stamped in the trackers stay comparable) plus new rates."""
    S = sents(t)
    L = [len(s.split()) for s in S]
    W = words(t)
    mean = st.mean(L)
    g = [tuple(W[i:i + 4]) for i in range(len(W) - 3)]
    c = collections.Counter(g)
    fw = [s.split()[0].strip("\"“‘'").lower() for s in S]
    runs, cur = 0, 1
    for i in range(1, len(fw)):
        if fw[i] == fw[i - 1]:
            cur += 1
        else:
            runs += cur >= 3
            cur = 1
    runs += cur >= 3
    nw = max(1, len(W))
    quoted = re.findall(r"[\"“]([^\"”]{1,600})[\"”]", t)
    return {
        "mean_len": mean,
        "cv": st.pstdev(L) / mean,
        "ttr": len(set(W[:2000])) / len(W[:2000]),
        "rep4": sum(v for v in c.values() if v > 1) / len(g),
        "anaph_runs": runs / nw * 1000,
        "pron_open": sum(f in ("she", "he", "they", "her", "his") for f in fw) / len(fw),
        "tricolon": len(re.findall(r"\b\w+,\s+\w+,\s+(?:and|or)\s+\w+", t)) / nw * 1000,
        "short": sum(l <= 5 for l in L) / len(L),
        "long": sum(l >= 30 for l in L) / len(L),
        # new in v2 (baseline-backed)
        "as_if": len(AS_IF_RE.findall(t)) / nw * 1000,
        "like_a": len(LIKE_A_RE.findall(t)) / nw * 1000,
        "the_way": len(THE_WAY_RE.findall(t)) / nw * 1000,
        "stated": len(STATED_RE.findall(t)) / nw * 1000,
        "dialogue": sum(len(q.split()) for q in quoted) / max(1, len(t.split())),
    }


def baseline():
    if CACHE.exists():
        try:
            d = json.loads(CACHE.read_text())
            if d.get("v") == CACHE_VERSION:
                return d["m"]
        except Exception:
            pass
    print("first run: downloading human baseline novels (4 MB)...", file=sys.stderr)
    z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(URL, timeout=90).read()))
    acc = collections.defaultdict(list)
    for n in NAMES:
        w = z.read(f"gutenberg/{n}.txt").decode("latin-1").split()
        for i in range(0, len(w) - WIN + 1, WIN):
            if i // WIN >= 12:
                break
            for k, v in metrics(" ".join(w[i:i + WIN])).items():
                acc[k].append(v)
    q = lambda a, p: sorted(a)[int(p * (len(a) - 1))]
    out = {k: [q(v, .1), q(v, .5), q(v, .9)] for k, v in acc.items()}
    CACHE.write_text(json.dumps({"v": CACHE_VERSION, "m": out}))
    return out


# ---------------------------------------------------------------- extra detectors
def find_tics(t):
    """Repeated 3-word phrases (3+ times, not mostly stopwords) and repeated
    'and laughed' style tails (3+ times). Returns [(phrase, count)]."""
    W = words(t)
    raw = re.findall(r"[A-Za-z']+", t)
    caps = collections.defaultdict(int)
    for i in range(len(raw) - 2):
        if raw[i + 1][0].isupper() and raw[i + 2][0].isupper():
            caps[tuple(w.lower() for w in raw[i:i + 3])] += 1
    out = []
    c3 = collections.Counter(tuple(W[i:i + 3]) for i in range(len(W) - 2))
    for g, n in c3.items():
        if n >= 3 and sum(w in STOP for w in g) <= 1 and caps.get(g, 0) * 2 < n:
            out.append((" ".join(g), n))
    c2 = collections.Counter(m.group(0).lower() for m in TAIL_RE.finditer(t))
    for g, n in c2.items():
        if n >= 3:
            out.append((g, n))
    return sorted(out, key=lambda x: -x[1])


def closers(paras):
    """Paragraphs of 3+ sentences whose last sentence is 7 words or fewer.
    Returns (ratio, [(paragraph_no, sentence)])."""
    hit, tot = [], 0
    for i, p in enumerate(paras, 1):
        S = sents(p)
        if len(S) >= 3:
            tot += 1
            if len(S[-1].split()) <= 7:
                hit.append((i, S[-1]))
    return (len(hit) / tot if tot else 0.0), hit


def opening_runs(paras):
    """[(paragraph_no, run_length, opening_word)] for runs of 3+ equal openers."""
    out = []
    for i, p in enumerate(paras, 1):
        S = sents(p)
        fw = [s.split()[0].strip("\"“‘'").lower() for s in S]
        j = 0
        while j < len(fw):
            k = j
            while k + 1 < len(fw) and fw[k + 1] == fw[j]:
                k += 1
            if k - j + 1 >= 3:
                out.append((i, k - j + 1, fw[j]))
            j = k + 1
    return out


PRON = ("she", "he", "they", "her", "his")


def pronoun_clusters(paras):
    """Paragraphs where 3+ sentences open with a pronoun. [(para_no, hits, total, [openers])]"""
    out = []
    for i, p in enumerate(paras, 1):
        S = sents(p)
        op = [s for s in S if s.split()[0].strip("\"“‘'").lower() in PRON]
        if len(op) >= 3:
            out.append((i, len(op), len(S), [" ".join(s.split()[:4]) for s in op]))
    return sorted(out, key=lambda x: (-x[1], x[0]))


def sentence_issues(paras):
    """Per-sentence fix list: [(paragraph_no, label, sentence)]."""
    out = []
    for i, p in enumerate(paras, 1):
        flat = re.sub(r"\s+", " ", p)
        for m in NEG_PAR_RE.finditer(flat):
            out.append((i, "negative parallelism", m.group(0)))
        for s in sents(p):
            for rx in CLICHE_RE:
                if rx.search(s):
                    out.append((i, "stock gesture", s))
                    break
            if STATED_RE.search(s):
                out.append((i, "feeling/theme stated", s))
            if AS_IF_RE.search(s) and THE_WAY_RE.search(s):
                out.append((i, "'the way' + 'as if' in one sentence", s))
            m = AI_NAME_RE.search(s)
            if m:
                out.append((i, f"blocklist name: {m.group(1)}", s))
    return out


def frac_hi(v, lo, hi):
    return min(1.0, max(0.0, v - hi) / max(1e-9, hi - lo))


def frac_lo(v, lo, hi):
    return min(1.0, max(0.0, lo - v) / max(1e-9, hi - lo))


def human_score(t, base, repo_score):
    """Returns (score 0-100, rows [(key, lost, detail)], details dict)."""
    m = metrics(t)
    paras = paragraphs(t)
    nw = max(1, len(words(t)))
    cl_count = sum(len(rx.findall(t)) for rx in CLICHE_RE)
    neg_count = len(NEG_PAR_RE.findall(t))
    tics = find_tics(t)
    tic_excess = sum(n - 2 for _, n in tics)
    ratio, zingers = closers(paras)
    name_hits = AI_NAME_RE.findall(t)
    f = {
        "scan": min(1.0, repo_score / 30.0),
        "pron_open": frac_hi(m["pron_open"], base["pron_open"][0], base["pron_open"][2]),
        "anaph_runs": frac_hi(m["anaph_runs"], base["anaph_runs"][0], base["anaph_runs"][2]),
        "short": frac_hi(m["short"], base["short"][0], base["short"][2]),
        "cv": max(frac_hi(m["cv"], base["cv"][0], base["cv"][2]), frac_lo(m["cv"], base["cv"][0], base["cv"][2])),
        "ttr": frac_lo(m["ttr"], base["ttr"][0], base["ttr"][2]),
        "rep4": frac_hi(m["rep4"], base["rep4"][0], base["rep4"][2]),
        "simile": (frac_hi(m["as_if"], base["as_if"][0], base["as_if"][2])
                   + frac_hi(m["like_a"], base["like_a"][0], base["like_a"][2])) / 2,
        "stated": frac_hi(m["stated"], base["stated"][0], base["stated"][2]),
        "tics": min(1.0, tic_excess / 6.0),
        "closer": min(1.0, max(0.0, ratio - 0.25) / 0.35),
        "cliche": min(1.0, (cl_count / nw * 1000) / 2.0),
        "neg_par": min(1.0, (neg_count / nw * 1000) / 1.5),
        "names": 1.0 if name_hits else 0.0,
        "dialogue": frac_lo(m["dialogue"], base["dialogue"][0], base["dialogue"][2]),
    }
    rows, lost = [], 0.0
    for k, (w, _) in WEIGHTS.items():
        pts = w * f[k]
        lost += pts
        rows.append((k, pts, f[k]))
    info = {"m": m, "tics": tics, "closer_ratio": ratio, "zingers": zingers, "cliche": cl_count,
            "neg_par": neg_count, "names": sorted(set(name_hits)), "paras": paras}
    return round(100 - lost, 1), rows, info


# ---------------------------------------------------------------- reporting
def book_gate(path, n):
    gate_script = ROOT / "scripts" / "write_warm_enough.py"
    if not gate_script.exists():
        return "(book gate script not found)"
    r = subprocess.run([sys.executable, str(gate_script), "--check", str(path), "--chapter", str(n)],
                       capture_output=True, text=True)
    return r.stdout.strip().replace("\n", " | ") or r.stderr.strip()[:200]


def check_one(path, n, base, quiet=False, fixes=30):
    t = Path(path).read_text(encoding="utf-8")
    import humanizer as h
    r, s = h.scan(t), h.scan_narrative(t)
    score, rows, info = human_score(t, base, r["score"])
    m = info["m"]
    if quiet:
        return score, m, r["score"]
    dashes, digits = len(re.findall("[—–]", t)), len(re.findall(r"\d", t))
    print(f"\n=== {path}")
    print("book gate        :", book_gate(path, n))
    print("dashes / digits  :", dashes, "/", digits, "(both must be 0)")
    print("repo scan score  :", r["score"], "(lower = cleaner)", [(x["type"], x.get("count")) for x in r["hits"]])
    print("narrative flags  :", [(x["type"], x.get("count")) for x in s["flags"]] or "none")
    print(f"\nHUMAN SCORE      : {score} / 100   (higher = more human-like; heuristic, not proof)")
    print("\npoints lost (largest first):")
    for k, pts, fr in sorted(rows, key=lambda x: -x[1]):
        if pts >= 0.5:
            print(f"  -{pts:4.1f} of {WEIGHTS[k][0]:2d}  {WEIGHTS[k][1]}")
    print(f"\n{'measure':11}{'chapter':>9}   human p10 / median / p90")
    for k in ("cv", "ttr", "rep4", "anaph_runs", "pron_open", "short", "as_if", "like_a", "stated", "dialogue"):
        v = m[k]
        lo, md, hi = base[k]
        tag = "" if lo <= v <= hi else ("  <-- above human range" if v > hi else "  <-- below human range")
        print(f"{k:11}{v:9.3f}   {lo:.3f} / {md:.3f} / {hi:.3f}{tag}")
    n_s = len(sents(t))
    n_pron = round(m["pron_open"] * n_s)
    n_goal = int(base["pron_open"][2] * n_s)
    if n_pron > n_goal:
        print(f"\npronoun openings: {n_pron} of {n_s} sentences. To reach the human ceiling "
              f"({base['pron_open'][2]:.0%}) rework about {n_pron - n_goal} of them "
              f"(start a sentence with a place, an object, a time, a line of speech, or merge two).")
    print(f"info only, NOT scored: 'the way' frames {m['the_way']:.2f} per 1000 words (human median {base['the_way'][1]:.2f})")
    print(f"\ncliches {info['cliche']}  neg-parallel {info['neg_par']}  zinger-ending paragraphs "
          f"{info['closer_ratio']:.0%}  blocklist names {info['names'] or 'none'}")
    if info["tics"]:
        print("tic phrases      :", "; ".join(f"'{p}' x{n}" for p, n in info["tics"][:8]))
    runs = opening_runs(info["paras"])
    print("\nFIX LIST (edit these sentences, keep canon and voice):")
    lines = []
    for pno, ln, w in runs:
        lines.append(f"  P{pno}: {ln} sentences in a row open with '{w}'. Vary or merge.")
    for pno, hits, tot, ops in pronoun_clusters(info["paras"])[:12]:
        lines.append(f"  P{pno}: {hits} of {tot} sentences open with a pronoun ({', '.join(ops[:4])}). Rework some.")
    for pno, label, sent in sentence_issues(info["paras"]):
        lines.append(f"  P{pno} [{label}]: {sent[:170]}")
    for pno, sent in info["zingers"]:
        lines.append(f"  P{pno} [short zinger ending]: {sent[:120]}")
    if not lines:
        lines = ["  nothing flagged"]
    for ln in lines[:fixes]:
        print(ln)
    if len(lines) > fixes:
        print(f"  ... {len(lines) - fixes} more (use --fixes {len(lines)})")
    return score, m, r["score"]


def selftest(base):
    """Shows the score separates human prose from stock-AI prose. Uses only the
    baseline's own windows and a deliberately AI-styled sample."""
    ai = (
        "It was not just a storm. It was a reckoning. Elara Voss stood at the window, and her heart hammered. "
        "She let out a breath she didn't know she was holding. She realized that nothing would ever be the same. "
        "Something shifted in the air between them. The silence stretched. She felt a mix of hope and fear. "
        "She smiled. She nodded. She turned. She knew that this was a testament to her resilience. "
        "The weight of it settled over her, a tapestry of grief, joy, and longing. She had grown. "
    ) * 14
    import humanizer as h
    s_ai, _, _ = human_score(ai, base, h.scan(ai)["score"])
    print(f"synthetic AI-style sample ({len(ai.split())} words): HUMAN SCORE {s_ai}")
    try:
        z = zipfile.ZipFile(io.BytesIO(urllib.request.urlopen(URL, timeout=90).read()))
        sc = []
        for n in NAMES:
            w = z.read(f"gutenberg/{n}.txt").decode("latin-1").split()
            for i in (12 * WIN, 14 * WIN):
                if i + WIN <= len(w):
                    txt = " ".join(w[i:i + WIN])
                    sc.append(human_score(txt, base, h.scan(txt)["score"])[0])
        print(f"human novel windows not used to build the baseline: n={len(sc)} "
              f"median {st.median(sc):.1f}  min {min(sc):.1f}  max {max(sc):.1f}")
    except Exception as e:
        print("could not fetch held-out human windows:", e)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("chapter", nargs="?")
    ap.add_argument("--n", type=int, default=1)
    ap.add_argument("--book")
    ap.add_argument("--fixes", type=int, default=30)
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    base = baseline()
    if a.selftest:
        selftest(base)
    elif a.book:
        rows = []
        for f in sorted(glob.glob(str(ROOT / "novels" / a.book / "chapters" / "chapter_*.md"))):
            n = int(Path(f).stem.split("_")[-1])
            sc, m, rs = check_one(f, n, base, quiet=True)
            rows.append((n, sc, rs, m["anaph_runs"], m["pron_open"], m["short"], m["ttr"]))
        print("ch  HUMAN  repo-scan  anaph/1000w  pron_open  short  ttr")
        for r in rows:
            print(f"{r[0]:2d}  {r[1]:5.1f}  {r[2]:9d}  {r[3]:11.2f}  {r[4]:9.2f}  {r[5]:5.2f}  {r[6]:.3f}")
        print("mean HUMAN", round(st.mean(r[1] for r in rows), 1), " mean repo-scan", round(st.mean(r[2] for r in rows), 1))
        worst = sorted(rows, key=lambda r: r[1])[:5]
        print("lowest 5 (do these first):", ", ".join(f"ch{r[0]} ({r[1]:.0f})" for r in worst))
    elif a.chapter:
        check_one(a.chapter, a.n, base, fixes=a.fixes)
    else:
        ap.error("give a chapter file, --book NAME, or --selftest")


if __name__ == "__main__":
    main()
