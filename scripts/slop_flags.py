#!/usr/bin/env python3
"""
slop_flags.py - READ-ONLY second opinion for Voxel novels. It never edits a chapter.

WHAT IT DOES
Counts, per chapter, three things taken from sam-paech/slop-score (MIT licence,
pinned to commit 289264ab2a0df1358ef81ced3c259610ea709514):
  1. SLOP WORDS   single words that AI fiction uses far more than people do
                  (data/slop_list.json), as a rate per 1,000 content words.
  2. SLOP TRIGRAMS three-word runs on the same footing (data/slop_list_trigrams.json),
                  matched after common function words are dropped, so "took a deep
                  breath" is the run "took deep breath".
  3. CONTRAST PATTERNS the ten surface "not X, but Y" / "It wasn't X. It was Y."
                  patterns from js/regexes-stage1.js, ported to Python. These match
                  the frozen HUMANIZER STEP spec check B4.

HOW TO READ IT (frozen spec, principle C: WHEN UNCERTAIN, PRESERVE THE AUTHOR'S TEXT)
Every line here is a PROMPT TO LOOK, not an instruction to change anything. A word
on the list can be exactly right for a scene. Nothing here proves who wrote a
chapter, and the numbers are only comparable between chapters of THIS book. They
are not the numbers eqbench.com shows: that site's normalisation was not checked.

NEEDS: Python 3.8+, no packages. The three list files are downloaded once into
.slop_cache/ (raw.githubusercontent.com). With no network and no cache it says so
and stops; it does not guess.

USAGE
  python scripts/slop_flags.py --book warm-enough
  python scripts/slop_flags.py --book warm-enough --chapter 10 --detail
  python scripts/slop_flags.py --file path/to/chapter.md --detail
"""
import argparse
import json
import re
import sys
import urllib.request
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PIN = "289264ab2a0df1358ef81ced3c259610ea709514"
BASE = "https://raw.githubusercontent.com/sam-paech/slop-score/%s/data/" % PIN
LIST_FILES = {
    "words": "slop_list.json",
    "bigrams": "slop_list_bigrams.json",
    "trigrams": "slop_list_trigrams.json",
}
CACHE = ROOT / ".slop_cache"

# NLTK English stopwords, copied from slop-score js/metrics.js (MIT)
STOPWORDS = set("""
i me my myself we our ours ourselves you your yours yourself yourselves he him his himself
she her hers herself it its itself they them their theirs themselves what which who whom
this that these those am is are was were be been being have has had having do does did doing
a an the and but if or because as until while of at by for with about against between into
through during before after above below to from up down in out on off over under again
further then once here there when where why how all any both each few more most other some
such no nor not only own same so than too very s t can will just don should now
""".split())

# ------------------------------------------------------------------ contrast patterns
# Ported from slop-score js/regexes-stage1.js (MIT). Text is normalised first
# (curly quotes to straight), so the quote classes here are plain.
MAXG = 160
PRON = r"(?:it|they|this|that)"
BE = r"(?:is|are|was|were)"
BE_NEG = r"(?:is\s+not|are\s+not|was\s+not|were\s+not|isn't|aren't|wasn't|weren't|ain't)"
BOS = r"(?:(?<=^)|(?<=[.?!]\s))"
Q = r"[\"']?"
REPORT = (r"(?:knew|know|thought|think|said|says|told|heard|learned)")

PATTERNS = {
    "NOT_BUT": (
        r"\b(?:(?:%s)|not(?!\s+(?:that|only)\b))\s+"
        r"(?:(?!\bbut\b|[.?!]).){1,100}?"
        r"[,;:]\s*but\s+"
        r"(?!when\b|while\b|which\b|who\b|whom\b|whose\b|where\b|if\b|that\b|as\b|because\b|although\b|though\b|till\b|until\b|unless\b|"
        r"here\b|there\b|then\b|my\b|we\b|I\b|you\b|it\s+seems\b|it\s+appears\b|it\s+felt\b|it\s+looks?\b|anything\b)" % BE_NEG
    ),
    "NOT_DASH": (
        r"\b(?:\w+n't|not)\s+(?:just|only|merely)?\s+"
        r"(?:(?![.?!]).){1,%d}?"
        r"(?:-|\s-\s|[\u2014\u2013])\s*"
        r"%s\s+(?:(?:'re|are|'s|is|were|was)\b|(?!'re|are|'s|is|were|was)[*_~]*[a-z]\w*)" % (MAXG, PRON)
    ),
    "PRON_BE_NOT_THEN_BE": (
        BOS + r"\s*" + Q +
        r"(?:(?:%s\s+%s\s+not)|(?:%s\s+%sn't)|(?:it's|they're|that's)\s+not)\b"
        r"[^.?!]{0,%d}[.;:?!]\s*" % (PRON, BE, PRON, BE, MAXG) + Q +
        r"%s\s+(?:%s|(?:'s|'re))\b(?!\s+not\b)" % (PRON, BE)
    ),
    "NP_BE_NOT_THEN_THEY_BE": (
        BOS + r"\s*"
        r"(?![^.?!]{0,80}\b%s\b[^.?!]{0,40}?\bthat\b)"
        r"(?!\s*not\s+without\b)"
        r"(?![^.?!]{0,50}\bnot\s+put\b)"
        r"[^.?!]{0,%d}?\b(?:%s)\b[^.?!]{0,%d}[.;:?!]\s*" % (REPORT, MAXG, BE_NEG, MAXG) + Q +
        r"%s\b(?:'re|\s+(?:are|were|is|was))\b(?!\s+not\b)" % PRON
    ),
    "NO_LONGER": (
        BOS + r"\s*[^.?!]{0,%d}\bno\s+longer\b[^.;:?!]{0,%d}"
        r"[.;:?!]\s*(?:it|they|this|that)\s+(?:is|are|was|were)\b(?!\s+not\b)" % (MAXG, MAXG)
    ),
    "NOT_JUST_THEN": (
        BOS + r"\s*" + Q +
        r"%s\b(?:'s|'re|\s+(?:is|are|was|were))?\s+not\s+just\b[^.?!]{0,%d}[.?!]\s*" % (PRON, MAXG) + Q +
        r"%s\b(?:'s|'re|\s+(?:is|are|was|were))\b(?!\s+not\b)" % PRON
    ),
    "DIDNT_V_THEN_SAME_V": (
        BOS + r"[^.?!]*?\b(?:do|does|did)n't\b\s+"
        r"(?:(?:\w+\s+){0,2})([a-z]{3,})\b[^.?!]*[.?!]\s*"
        r"%s\s+\1(?:ed|es|s|ing)?\b" % PRON
    ),
    "ISNT_THEN_ITS": (
        BOS + r"\s*" + Q +
        r"(?!he\b|she\b|i\b|you\b|we\b)"
        r"(?![^.?!]{0,80}\b%s\b[^.?!]{0,40}?\bthat\b)"
        r"[^.?!]{0,%d}?\b%s\b[^.?!]{0,%d}[.;:?!]\s*" % (REPORT, MAXG, BE_NEG, MAXG) + Q +
        r"it(?:'s|\s+(?:is|are|was|were))\b"
    ),
    "EMBEDDED_NOT_JUST": (
        BOS +
        r"[^.?!]{0,80}?\b(?:(?:it|they)\s+(?:is|are)|(?:it's|they're))\s+not\s+just\b"
        r"[^.?!]{0,%d}[.?!]\s*"
        r"(?:(?:it|they)\s+(?:is|are)|(?:it's|they're))\b" % MAXG
    ),
    "DIALOGUE_NOT_JUST": (
        Q + r"%s(?:'re|'s|\s+(?:are|is|was|were))\s+not\s+just\b[^\"']{0,%d}[\"']?\s*"
        r"(?:[^.?!]{0,80}\b(?:said|asked|whispered|muttered|replied|added|shouted|cried)\b[^.?!]{0,80}[.?!]\s*)?"
        % (PRON, MAXG) + Q +
        r"%s(?:'re|'s|\s+(?:are|is|was|were))\s+[*_~]?[a-z]\w*" % PRON
    ),
}
COMPILED = {k: re.compile(v, re.I) for k, v in PATTERNS.items()}


# ------------------------------------------------------------------ helpers
def normalize(text):
    for a, b in (("\u2018", "'"), ("\u2019", "'"), ("\u201a", "'"), ("\u201b", "'"),
                 ("\u201c", '"'), ("\u201d", '"'), ("\u201e", '"')):
        text = text.replace(a, b)
    return text


def strip_markdown(text):
    return "\n".join("" if ln.lstrip().startswith("#") else ln for ln in text.split("\n"))


def tokens_of(text):
    low = normalize(text).lower()
    toks = [t.strip("'") for t in re.findall(r"[a-z']+", low)]
    return [t for t in toks if t]


def content_tokens(toks):
    return [t for t in toks if re.match(r"^[a-z]+(?:'[a-z]+)?$", t) and t not in STOPWORDS]


def load_lists():
    CACHE.mkdir(exist_ok=True)
    out = {}
    for key, fname in LIST_FILES.items():
        p = CACHE / fname
        if not p.exists():
            try:
                with urllib.request.urlopen(BASE + fname, timeout=60) as r:
                    p.write_bytes(r.read())
            except Exception as e:  # no network and no cache
                print("slop_flags: cannot get %s (%s). No lists, no check." % (fname, e), file=sys.stderr)
                sys.exit(5)
        data = json.loads(p.read_text(encoding="utf-8"))
        s = set()
        for item in data:
            if item:
                m = re.findall(r"[a-z]+(?:'[a-z]+)?(?:\s+[a-z]+(?:'[a-z]+)?)*", str(item[0]).lower())
                if m:
                    s.add(m[0])
        out[key] = s
    return out


def sentence_of(text, start, end):
    a = max(text.rfind(". ", 0, start), text.rfind("\n", 0, start))
    a = 0 if a < 0 else a + 1
    b_candidates = [i for i in (text.find(". ", end), text.find("\n", end)) if i != -1]
    b = min(b_candidates) + 1 if b_candidates else len(text)
    return " ".join(text[a:b].split())


def analyse(text, lists):
    body = normalize(strip_markdown(text))
    toks = content_tokens(tokens_of(body))
    n = len(toks) or 1
    wc = Counter(t for t in toks if t in lists["words"])
    tri = Counter()
    for i in range(len(toks) - 2):
        g = toks[i] + " " + toks[i + 1] + " " + toks[i + 2]
        if g in lists["trigrams"]:
            tri[g] += 1
    contrast = []
    for name, rx in COMPILED.items():
        for m in rx.finditer(body):
            contrast.append((name, m.start(), sentence_of(body, m.start(), m.end())))
    # one sentence can match several patterns: keep the first pattern per sentence
    seen, unique = set(), []
    for name, pos, sent in sorted(contrast, key=lambda x: x[1]):
        if sent in seen:
            continue
        seen.add(sent)
        unique.append((name, sent))
    return {
        "words": len(body.split()),
        "content": len(toks),
        "slop_rate": sum(wc.values()) / n * 1000,
        "tri_rate": sum(tri.values()) / n * 1000,
        "word_hits": wc.most_common(),
        "tri_hits": tri.most_common(),
        "contrast": unique,
    }


def chapter_files(book):
    d = ROOT / "novels" / book / "chapters"
    files = sorted(d.glob("chapter_*.md"), key=lambda p: int(re.search(r"(\d+)", p.name).group(1)))
    return files


def main():
    ap = argparse.ArgumentParser(description="Read-only slop-score style flags for Voxel chapters.")
    ap.add_argument("--book", default=None, help="folder name under novels/ (example: warm-enough)")
    ap.add_argument("--chapter", type=int, default=None, help="one chapter number")
    ap.add_argument("--file", default=None, help="one markdown file instead of a book")
    ap.add_argument("--detail", action="store_true", help="list every flagged sentence and word")
    args = ap.parse_args()
    if not args.book and not args.file:
        ap.error("give --book or --file")
    lists = load_lists()

    if args.file:
        items = [("file", Path(args.file))]
    else:
        items = []
        for p in chapter_files(args.book):
            k = int(re.search(r"(\d+)", p.name).group(1))
            if args.chapter is None or k == args.chapter:
                items.append((k, p))
    if not items:
        print("no chapter files found", file=sys.stderr)
        return 4

    results = []
    for k, p in items:
        results.append((k, analyse(p.read_text(encoding="utf-8"), lists)))

    print("slop_flags (read only; flags are prompts to look, not instructions to change)")
    print("lists: sam-paech/slop-score @ %s" % PIN[:8])
    print("%-4s %6s %9s %8s %9s  %s" % ("ch", "words", "slop/1kw", "tri/1kw", "contrast", "top slop words"))
    for k, r in results:
        top = ", ".join("%s x%d" % kv for kv in r["word_hits"][:5])
        print("%-4s %6d %9.1f %8.1f %9d  %s" % (k, r["words"], r["slop_rate"], r["tri_rate"], len(r["contrast"]), top))
    if len(results) > 1:
        m_s = sum(r["slop_rate"] for _, r in results) / len(results)
        m_t = sum(r["tri_rate"] for _, r in results) / len(results)
        m_c = sum(len(r["contrast"]) for _, r in results) / len(results)
        print("mean %6s %9.1f %8.1f %9.1f" % ("", m_s, m_t, m_c))
        hi = sorted(results, key=lambda kr: -(kr[1]["slop_rate"] + 3 * len(kr[1]["contrast"])))[:5]
        print("look at first (highest slop rate plus contrast count): " +
              ", ".join("ch%s" % k for k, _ in hi))

    if args.detail:
        for k, r in results:
            print("\n== chapter %s ==" % k)
            if r["contrast"]:
                print("contrast patterns (%d):" % len(r["contrast"]))
                for name, sent in r["contrast"]:
                    print("  [%s] %s" % (name, sent[:260]))
            if r["tri_hits"]:
                print("slop trigrams: " + ", ".join("%s x%d" % kv for kv in r["tri_hits"]))
            if r["word_hits"]:
                print("slop words: " + ", ".join("%s x%d" % kv for kv in r["word_hits"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
