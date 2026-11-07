#!/usr/bin/env python3
"""
humanness_bench.py - READ-ONLY benchmark: how far is each chapter from human-written fiction?
It never edits a chapter. Python standard library only (and `git` to fetch the reference novels).

DESIGN (follows accepted practice, so the numbers can be defended):
  1. HUMAN REFERENCE: public-domain English novels from 1906 to 1927, fetched from the Standard Ebooks
     repositories on GitHub (standardebooks/<author>_<title>). They are cut into non-overlapping windows
     the size of a chapter (default 2,400 words). The humanizer's older baseline is Austen-era prose;
     this set is closer to modern fiction.
  2. STYLOMETRY: Cosine Delta (Burrows 2002; Evert et al. 2017, Digital Scholarship in the Humanities
     32, ii4-ii16): relative frequencies of the most frequent words, z-scored across the reference,
     compared by cosine distance. A window's score is its distance to the CLOSEST human profile
     (one profile per reference novel).
  3. CALIBRATION AT A FIXED FALSE-ALARM RATE (the RAID benchmark rule, Dugan et al., ACL 2024):
     every reference window is scored the same way against the profiles of the OTHER novels
     (leave-one-novel-out). The flag threshold is the 95th percentile of those human scores, so about
     5 percent of real human windows are flagged by construction.
  4. PLAIN MEASURES, each flagged only OUTSIDE the human 2.5 to 97.5 percent range:
     MATTR-500 (lexical diversity, Covington and McFall 2010; stride 25), sentence-length mean and
     coefficient of variation (burstiness), share of sentences opening with he/she/they.
  5. HONEST NUMBERS: every flag rate has a Wilson 95 percent interval; an optional CONTROL group of
     chapters you wrote by hand (--control 1-6) shows what a human author of this book scores.

WHAT THIS CAN AND CANNOT SAY
  * It measures distance from a pool of human fiction. It has no machine-written reference class, so it
    cannot say "AI" or "not AI". A human author with an unusual register can also sit outside the range.
  * Window size matters: Delta needs long texts (Proisl et al. 2018). Chapters of 2,000+ words are fine.
  * No score here proves who wrote a chapter. Read it as: which chapters differ most from human fiction.
  * CHECKED (2026-11-07, sandbox): on 71 windows of six human novels NOT in the reference set, MATTR and
    pronoun-opening flagged none and Delta flagged none (the false-alarm side is sound). Two purely
    mechanical texts were flagged by all four plain measures but NOT by Delta: Delta alone is a guard
    against false alarms, not a sensitive detector. Trust the plain measures for that job.

USAGE (repo root)
  python scripts/humanness_bench.py --book warm-enough --control 1-6
  python scripts/humanness_bench.py --book warm-enough --chapter 10
"""
import argparse
import math
import re
import subprocess
import sys
from collections import Counter
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REFS = [
    "l-m-montgomery_anne-of-green-gables", "frances-hodgson-burnett_the-secret-garden",
    "eleanor-h-porter_pollyanna", "edith-wharton_the-age-of-innocence", "willa-cather_my-antonia",
    "f-scott-fitzgerald_the-great-gatsby", "e-m-forster_a-room-with-a-view", "e-m-forster_howards-end",
    "agatha-christie_the-mysterious-affair-at-styles", "agatha-christie_the-murder-of-roger-ackroyd",
    "virginia-woolf_to-the-lighthouse", "virginia-woolf_mrs-dalloway",
    "kenneth-grahame_the-wind-in-the-willows", "j-m-barrie_peter-and-wendy", "sinclair-lewis_babbitt",
    "d-h-lawrence_sons-and-lovers", "e-nesbit_the-railway-children",
    "hugh-lofting_the-story-of-doctor-dolittle", "dorothy-l-sayers_whose-body",
    "g-k-chesterton_the-man-who-was-thursday", "ernest-hemingway_the-sun-also-rises",
    "w-somerset-maugham_of-human-bondage",
]


# ------------------------------------------------------------------ text helpers
def norm(t):
    for a, b in (("\u2018", "'"), ("\u2019", "'"), ("\u201c", '"'), ("\u201d", '"'), ("\u2014", " "), ("\u2013", " ")):
        t = t.replace(a, b)
    return t


def words_of(t):
    return re.findall(r"[a-z]+(?:'[a-z]+)?", norm(t).lower())


def sentences_of(t):
    t = re.sub(r"\s+", " ", norm(t))
    parts = re.split(r'(?<=[.!?])["\')]*\s+(?=["\'(]?[A-Z])', t)
    return [p for p in parts if len(words_of(p)) > 0]


def mattr(toks, window=500, stride=25):
    if len(toks) < window:
        return len(set(toks)) / max(1, len(toks))
    vals = []
    for i in range(0, len(toks) - window + 1, stride):
        w = toks[i:i + window]
        vals.append(len(set(w)) / window)
    return sum(vals) / len(vals)


def percentile(sorted_vals, q):
    if not sorted_vals:
        return float("nan")
    k = (len(sorted_vals) - 1) * q
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return sorted_vals[int(k)]
    return sorted_vals[f] * (c - k) + sorted_vals[c] * (k - f)


def wilson(k, n, z=1.96):
    if n == 0:
        return (float("nan"), float("nan"))
    p = k / n
    d = 1 + z * z / n
    c = (p + z * z / (2 * n)) / d
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n)) / d
    return (max(0.0, c - h), min(1.0, c + h))


# ------------------------------------------------------------------ reference corpus
def fetch_ref(name, cache):
    d = cache / name
    if not d.exists():
        cache.mkdir(parents=True, exist_ok=True)
        r = subprocess.run(["git", "clone", "-q", "--depth", "1",
                            "https://github.com/standardebooks/%s.git" % name, str(d)],
                           capture_output=True, text=True)
        if r.returncode != 0:
            print("bench: could not fetch %s: %s" % (name, r.stderr.strip()[:120]), file=sys.stderr)
            return None
    return d


def novel_text(d):
    tdir = d / "src" / "epub" / "text"
    files = sorted(tdir.glob("*.xhtml"), key=lambda p: [int(x) if x.isdigit() else x for x in re.split(r"(\d+)", p.name)])
    out = []
    for f in files:
        h = f.read_text(encoding="utf-8", errors="ignore")
        m = re.search(r"<body[^>]*>", h)
        if not m or "bodymatter" not in m.group(0):
            continue
        h = re.sub(r"<hgroup>.*?</hgroup>", " ", h, flags=re.S)
        h = re.sub(r"<(h[1-6])[^>]*>.*?</\1>", " ", h, flags=re.S)
        for p in re.findall(r"<p[^>]*>(.*?)</p>", h, flags=re.S):
            p = unescape(re.sub(r"<[^>]+>", "", p)).strip()
            if p:
                out.append(p)
    return "\n".join(out)


def make_windows(text, size):
    toks = text.split()
    wins = []
    for i in range(0, len(toks) - int(size * 0.6), size):
        chunk = " ".join(toks[i:i + size])
        if len(chunk.split()) >= int(size * 0.6):
            wins.append(chunk)
    return wins


# ------------------------------------------------------------------ measures
def plain_measures(text):
    toks = words_of(text)
    sents = sentences_of(text)
    lens = [len(words_of(s)) for s in sents] or [0]
    mean = sum(lens) / len(lens)
    sd = math.sqrt(sum((x - mean) ** 2 for x in lens) / len(lens))
    po = sum(1 for s in sents if re.match(r'["\'(]*(he|she|they)\b', s.strip().lower())) / max(1, len(sents))
    return {"mattr": mattr(toks), "sl_mean": mean, "sl_cv": (sd / mean if mean else 0.0), "pron_open": po}


def rel_freq(text, vocab):
    toks = words_of(text)
    c = Counter(toks)
    n = max(1, len(toks))
    return [c.get(w, 0) / n for w in vocab]


def cosine_dist(a, b):
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(x * x for x in b))
    if na == 0 or nb == 0:
        return 1.0
    return 1.0 - sum(x * y for x, y in zip(a, b)) / (na * nb)


def chapter_files(book):
    d = ROOT / "novels" / book / "chapters"
    return sorted(d.glob("chapter_*.md"), key=lambda p: int(re.search(r"(\d+)", p.name).group(1)))


def parse_range(s):
    out = set()
    for part in (s or "").split(","):
        part = part.strip()
        if not part:
            continue
        if "-" in part:
            a, b = part.split("-")
            out.update(range(int(a), int(b) + 1))
        else:
            out.add(int(part))
    return out


def strip_md(t):
    return "\n".join(ln for ln in t.split("\n") if not ln.lstrip().startswith("#"))


# ------------------------------------------------------------------ main
def main():
    ap = argparse.ArgumentParser(description="Read-only human-likeness benchmark (Cosine Delta + plain measures).")
    ap.add_argument("--book", required=True)
    ap.add_argument("--chapter", type=int, default=None)
    ap.add_argument("--control", default="", help="chapters written by hand, example 1-6")
    ap.add_argument("--window", type=int, default=2400)
    ap.add_argument("--mfw", type=int, default=300)
    ap.add_argument("--cache", default=str(ROOT / ".bench_cache"))
    ap.add_argument("--refs", default="", help="comma list of Standard Ebooks repo names (default: built-in 22)")
    a = ap.parse_args()
    cache = Path(a.cache)
    refs = [r.strip() for r in a.refs.split(",") if r.strip()] or REFS

    # 1. reference windows, kept per novel
    ref_wins = {}
    for r in refs:
        d = fetch_ref(r, cache)
        if d is None:
            continue
        w = make_windows(novel_text(d), a.window)
        if w:
            ref_wins[r] = w
    n_win = sum(len(v) for v in ref_wins.values())
    if len(ref_wins) < 8 or n_win < 150:
        print("bench: only %d novels / %d windows, too few for a fair benchmark" % (len(ref_wins), n_win), file=sys.stderr)
        return 5

    # 2. vocabulary and z-scoring from the reference
    tot = Counter()
    for v in ref_wins.values():
        for w in v:
            tot.update(words_of(w))
    vocab = [w for w, _ in tot.most_common(a.mfw)]
    rf = {r: [rel_freq(w, vocab) for w in v] for r, v in ref_wins.items()}
    allrows = [x for v in rf.values() for x in v]
    mu = [sum(c) / len(allrows) for c in zip(*allrows)]
    sd = [math.sqrt(sum((x - m) ** 2 for x in c) / len(allrows)) or 1.0 for c, m in zip(zip(*allrows), mu)]

    def z(vec):
        return [(x - m) / s for x, m, s in zip(vec, mu, sd)]

    zr = {r: [z(x) for x in v] for r, v in rf.items()}
    cent = {r: [sum(c) / len(v) for c in zip(*v)] for r, v in zr.items()}

    # 3. leave-one-novel-out human scores
    human_delta = []
    for r, v in zr.items():
        others = [cent[o] for o in cent if o != r]
        for vec in v:
            human_delta.append(min(cosine_dist(vec, c) for c in others))
    human_delta.sort()
    thr = percentile(human_delta, 0.95)

    # 4. plain-measure ranges from the human windows
    pm = {k: [] for k in ("mattr", "sl_mean", "sl_cv", "pron_open")}
    for v in ref_wins.values():
        for w in v:
            m = plain_measures(w)
            for k in pm:
                pm[k].append(m[k])
    rng = {k: (percentile(sorted(v), 0.025), percentile(sorted(v), 0.5), percentile(sorted(v), 0.975)) for k, v in pm.items()}

    # 5. score the chapters
    control = parse_range(a.control)
    rows = []
    for p in chapter_files(a.book):
        n = int(re.search(r"(\d+)", p.name).group(1))
        if a.chapter is not None and n != a.chapter:
            continue
        t = strip_md(p.read_text(encoding="utf-8"))
        vec = z(rel_freq(t, vocab))
        dd = min(cosine_dist(vec, c) for c in cent.values())
        m = plain_measures(t)
        flags = {"delta": dd > thr}
        for k in pm:
            flags[k] = not (rng[k][0] <= m[k] <= rng[k][2])
        rows.append((n, len(t.split()), dd, m, flags))

    print("humanness_bench (read only; distance from human fiction, not proof of authorship)")
    print("reference: %d novels (1906-1927), %d windows of %d words, %d most frequent words" % (len(ref_wins), n_win, a.window, a.mfw))
    print("Cosine Delta flag threshold (95th percentile of human windows, leave-one-novel-out): %.4f" % thr)
    print("human ranges (2.5%-50%-97.5%):")
    for k in pm:
        print("  %-9s %.3f  %.3f  %.3f" % (k, rng[k][0], rng[k][1], rng[k][2]))
    print()
    print("%-3s %-5s %-7s %-6s | %-6s %-6s %-6s %-6s | flags" % ("ch", "words", "delta", "", "mattr", "slmean", "slcv", "pronop"))
    for n, w, dd, m, f in rows:
        mark = lambda k: "*" if f[k] else " "
        nf = sum(f.values())
        print("%-3d %-5d %-7.4f %-6s | %-5.3f%s %-5.1f%s %-5.3f%s %-5.3f%s | %d%s" % (
            n, w, dd, "OUT" if f["delta"] else "", m["mattr"], mark("mattr"), m["sl_mean"], mark("sl_mean"),
            m["sl_cv"], mark("sl_cv"), m["pron_open"], mark("pron_open"), nf, "  (control)" if n in control else ""))

    def summary(label, sel):
        if not sel:
            return
        print("%s (%d chapters):" % (label, len(sel)))
        k = sum(1 for r in sel if r[4]["delta"])
        lo, hi = wilson(k, len(sel))
        print("  Delta flagged: %d of %d  (%.0f%%, 95%% CI %.0f-%.0f%%; human windows flag at 5%% by construction)" % (k, len(sel), 100 * k / len(sel), 100 * lo, 100 * hi))
        for key in pm:
            k = sum(1 for r in sel if r[4][key])
            lo, hi = wilson(k, len(sel))
            print("  %-9s outside human range: %d of %d  (%.0f%%, 95%% CI %.0f-%.0f%%)" % (key, k, len(sel), 100 * k / len(sel), 100 * lo, 100 * hi))
        for key in pm:
            vals = sorted(r[3][key] for r in sel)
            print("  %-9s book median %.3f vs human median %.3f" % (key, percentile(vals, 0.5), rng[key][1]))

    print()
    if control:
        summary("CONTROL, written by hand", [r for r in rows if r[0] in control])
        summary("REST OF BOOK", [r for r in rows if r[0] not in control])
    else:
        summary("WHOLE BOOK", rows)
    print()
    print("Reading guide: expected false flags on real human text are about 5% per Delta and 5% per plain measure.")
    print("A flag rate far above that, with a confidence interval that stays above it, means the book differs from human fiction on that measure.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
