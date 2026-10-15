#!/usr/bin/env python3
"""
check_chapter.py - output gate. Scans a generated chapter for anything the
canon does not contain, so the chapter can be rejected and regenerated.

  python novels/next-series-canon/check_chapter.py <chapter.md> [--chapter N]

Flags (exit 1 if any):
  1. Capitalized names mid-sentence that are not in the canon (people, places).
  2. Digits and large number words not in the canon or in that chapter's beats.
  3. Leaked pipeline words (same list as build_canon.py).
Limit: it cannot catch invented ordinary nouns or events. Those need the
beat text to be specific, plus a human read of the first chapters.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canon_data as C

BANNED = re.compile(
    r"\[End of Chapter|sub-beat|\bBook [1-9]\b|\bbook (one|two|three|four|five)\b|"
    r"the series|protagonist|no \w+ arc needed|persuasion arc|Wound:|Competence:", re.I)
CALENDAR = "Monday Tuesday Wednesday Thursday Friday Saturday Sunday January February March April May June July August September October November December".split()
TITLES = ["Mr", "Mrs", "Ms", "Dr"]
BIGWORDS = "ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand dozen".split()

def allowed_names():
    names = set(CALENDAR + TITLES + [C.TOWN, "Heron"])
    srcs = list(C.CAST) + [n for n, _ in C.EXTRAS_POOL] + list(C.LOCATIONS) + [C.TOWN, C.LAKE]
    for s in srcs:
        for w in re.findall(r"[A-Za-z]+", s):
            names.add(w)
    return names

def chapter_text(n):
    for ch in getattr(C, "CHAPTERS", None) or []:
        if ch["n"] == n:
            return " ".join(t for _, t in ch["beats"])
    return ""

def canon_numbers():
    nums = {str(C.THRESHOLD), str(C.EXPECT_LEDGER_TOTAL), str(C.EXPECT_FINAL_TOTAL),
            str(C.OPENING_DAY_LOAVES), str(C.FERRY_LOAVES_UNLEDGERED),
            str(C.FERRY_CROSSING_MINUTES), str(C.LOAF_PRICE), str(C.ROLL_PRICE)}
    nums |= {str(x) for x in C.WEEKLY_LOAVES}
    return nums

def check(text, n=None):
    problems = []
    text = re.sub(r"^<!--.*?-->\s*", "", text, count=1, flags=re.S)
    names = allowed_names()
    beat = chapter_text(n) if n else ""
    for m in re.finditer(r"\b[A-Z][a-z']+\b", text):
        w = m.group(0)
        if w.startswith("I'") or w in names:
            continue
        base = w.removesuffix("'s").removesuffix("'")
        if base in names:
            continue
        before = text[:m.start()].rstrip(" \t\"\u201c\u2018'")
        if before == "" or before[-1] in ".!?\n:\u2014-":
            continue
        if base in beat:
            continue
        problems.append(f"name not in canon: {w}")
    allowed_nums = canon_numbers() | set(re.findall(r"\d[\d,]*(?:\.\d+)?", beat))
    for m in re.finditer(r"\d[\d,]*(?:\.\d+)?", text):
        v = m.group(0).rstrip(",")
        if v not in allowed_nums and v.replace(",", "") not in allowed_nums:
            problems.append(f"number not in canon: {v}")
    for w in BIGWORDS:
        if re.search(rf"\b{w}\b", text, re.I) and not re.search(rf"\b{w}\b", beat, re.I):
            problems.append(f"number word not in chapter beats: {w}")
    b = BANNED.search(text)
    if b:
        problems.append(f"leaked pipeline word: {b.group(0)}")
    return sorted(set(problems))

if __name__ == "__main__":
    path = sys.argv[1]
    n = int(sys.argv[sys.argv.index("--chapter") + 1]) if "--chapter" in sys.argv else None
    probs = check(open(path).read(), n)
    for p in probs:
        print("-", p)
    print("PASSED" if not probs else f"FAILED: {len(probs)}")
    sys.exit(1 if probs else 0)
