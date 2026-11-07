#!/usr/bin/env python3
"""
within_book_compare.py - READ-ONLY. Compares the chapters you wrote by hand with the other chapters
of the SAME book, on plain measures, with chance and confounds checked. Standard library only.
It never edits a chapter.

Why this and not a reference set of old novels: there is no legal modern human fiction to download
(copyright lasts about 95 years, so free books stop near 1930). The only modern human sample is the
author's own hand-written chapters. So the question asked is only: do the other chapters differ from
the hand-written ones, by more than chance? It does NOT say "AI" or "human", and it is NOT a target
to edit towards.

Method: per-chapter measures; permutation test (20,000 shuffles) of hand-written vs the rest; Bonferroni
threshold across the 7 measures; confound checks (point of view = odd/even chapter, position = early/late).
Limits: only 6 hand-written chapters (two of them, ch2 and ch3, had beats added by Claude on 2026-10-28);
the measures are simple and mine, not validated detectors; sentence splitting is rough.

USAGE (repo root):  python scripts/within_book_compare.py --book warm-enough --human 1-6
"""
import argparse, glob, math, random, re, statistics as st
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PRON = {"he", "she", "they"}
KEYS = ["meanlen", "cv", "pron", "runs", "short", "mattr", "contrast"]

def body(t):
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    return "\n".join(l for l in t.splitlines() if not l.startswith("#"))

def sents(t):
    return [s.strip() for s in re.split(r"(?<=[.!?])[\"”’']?\s+", t.replace("\n", " ")) if s.strip()]

def words(t):
    return re.findall(r"[a-z']+", t.lower())

def mattr(w, win=500, stride=25):
    v = [len(set(w[i:i + win])) / win for i in range(0, len(w) - win + 1, stride)]
    return sum(v) / len(v)

def measures(t):
    t = body(t); S = sents(t); W = words(t)
    L = [len(s.split()) for s in S]
    first = [(re.findall(r"[a-z']+", s.lower()) or [""])[0] for s in S]
    runs = 0; i = 0
    while i < len(first):
        j = i
        while j + 1 < len(first) and first[j + 1] == first[i] and first[i]:
            j += 1
        if j - i + 1 >= 3:
            runs += 1
        i = j + 1
    contrast = len(re.findall(r"\b(?:It|She|He|They|This) (?:was|is|were) not [^.!?]{1,60}[.!?]\s+(?:It|She|He|They|This) (?:was|is|were) ", t))
    m = st.mean(L)
    return dict(words=len(W), meanlen=m, cv=st.pstdev(L) / m,
                pron=sum(1 for f in first if f in PRON) / len(S), runs=runs * 1000 / len(W),
                short=sum(1 for l in L if l <= 5) / len(L), mattr=mattr(W), contrast=contrast * 1000 / len(W))

def perm_p(a, b, n=20000, rng=None):
    rng = rng or random.Random(1)
    obs = abs(st.mean(a) - st.mean(b)); pool = list(a) + list(b); c = 0
    for _ in range(n):
        rng.shuffle(pool)
        if abs(st.mean(pool[:len(a)]) - st.mean(pool[len(a):])) >= obs:
            c += 1
    return (c + 1) / (n + 1)

def cohen_d(a, b):
    sp = math.sqrt(((len(a) - 1) * st.variance(a) + (len(b) - 1) * st.variance(b)) / (len(a) + len(b) - 2))
    return (st.mean(b) - st.mean(a)) / sp

def span(s):
    a, _, b = s.partition("-")
    return list(range(int(a), int(b or a) + 1))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", default="warm-enough")
    ap.add_argument("--human", default="1-6", help="chapters written by hand, e.g. 1-6")
    a = ap.parse_args()
    d = ROOT / "novels" / a.book / "chapters"
    allc = sorted(int(re.search(r"(\d+)", p.name).group(1)) for p in d.glob("chapter_*.md"))
    hum = [n for n in span(a.human) if n in allc]
    rest = [n for n in allc if n not in hum]
    M = {n: measures((d / ("chapter_%02d.md" % n)).read_text(encoding="utf-8")) for n in allc}
    print("hand-written n=%d, other chapters n=%d" % (len(hum), len(rest)))
    print("chance: a new chapter from the same author lands outside the hand-written min-max about %.0f%% of the time (n=%d)" % (200 / (len(hum) + 1), len(hum)))
    alpha = 0.05 / len(KEYS)
    print("Bonferroni threshold across %d measures: p < %.4f\n" % (len(KEYS), alpha))
    print("%-8s %9s %9s %8s %9s  %s" % ("measure", "hand", "others", "d", "p", "verdict"))
    for k in KEYS:
        h = [M[n][k] for n in hum]; o = [M[n][k] for n in rest]
        p = perm_p(h, o)
        print("%-8s %9.3f %9.3f %8.2f %9.4f  %s" % (k, st.mean(h), st.mean(o), cohen_d(h, o), p,
              "differs beyond chance" if p < alpha else ("maybe" if p < 0.05 else "no clear difference")))
    print("\nconfound checks inside the other chapters (odd=Ansel, even=Hester; early vs late):")
    odd = [n for n in rest if n % 2]; even = [n for n in rest if n % 2 == 0]
    mid = sorted(rest)[len(rest) // 2]
    early = [n for n in rest if n < mid]; late = [n for n in rest if n >= mid]
    for k in KEYS:
        pa = perm_p([M[n][k] for n in odd], [M[n][k] for n in even], 5000)
        pb = perm_p([M[n][k] for n in early], [M[n][k] for n in late], 5000)
        print("%-8s Ansel vs Hester p=%.3f | early vs late p=%.3f" % (k, pa, pb))

if __name__ == "__main__":
    main()
