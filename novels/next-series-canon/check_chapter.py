#!/usr/bin/env python3
"""
check_chapter.py - output gate. Scans a generated chapter for anything the
canon does not contain, so the chapter can be rejected and regenerated.

  python novels/next-series-canon/check_chapter.py <chapter.md> [--chapter N]

FAIL (exit 1):
  1. Capitalized names mid-sentence that are not in the canon (people, places).
  2. Digits and large number words not in the canon or in that chapter's beats.
  3. Leaked pipeline words (same list as build_canon.py).
  4. Hidden facts appearing before their reveal chapter (HIDDEN in canon_chapters.py).
  5. Required strings for that chapter missing (must lists).
WARN (printed, does not fail):
  6. Unknown capitalized word at sentence start that never appears lowercase
     (possible invented name at the start of a sentence).
Limit: it cannot catch invented ordinary nouns or events, or invented numbers
below ten. Those need specific beat text plus a human read of early chapters.
"""
import os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import canon_chapters as C

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

STARTERS = set("The A An And But Or So Then When While As If It Its He She They We You I His Her Their Our My This That These Those There Here What Why How Who Where Not No Yes Now Still Just Even Only Once After Before Because Though Although Maybe Perhaps Nothing Something Everything Someone Nobody Every Each Some Any All One Two Three Four Five Six Seven Eight Nine Behind Beside Outside Inside Across Through Under Over Down Up Out In On At By For From With Without Into Onto Like Let Do Did Does Is Was Were Are Be Been Can Could Would Should Will Shall May Might Must Of To".split())

ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()

def number_words(n):
    """Component words for n (0-9999), e.g. 97 -> {'ninety','seven'}."""
    out = set()
    if n >= 1000:
        out |= number_words(n // 1000) | {"thousand"}
        n %= 1000
    if n >= 100:
        out |= {ONES[n // 100], "hundred"}
        n %= 100
    if n >= 20:
        out.add(TENS[n // 10])
        n %= 10
    if n or not out:
        out.add(ONES[n])
    return out

def hidden_problems(text, n):
    probs = []
    for name, h in (getattr(C, "HIDDEN", {}) or {}).items():
        if n in h["forbidden_chapters"]:
            for tok in h["tokens"]:
                if tok.lower() in text.lower():
                    probs.append(f"hidden fact appears too early ({name}): {tok}")
    return probs

def must_problems(text, n):
    for ch in getattr(C, "CHAPTERS", None) or []:
        if ch["n"] == n:
            return [f"required text missing: {m}" for m in ch.get("must", []) if m not in text]
    return []

def check(text, n=None, warns=None):
    if warns is None:
        warns = []
    problems = []
    text = text.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
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
            if base not in STARTERS and not re.search(rf"\b{base.lower()}\b", text):
                warns.append(f"possible invented name at sentence start: {w}")
            continue
        if base in beat:
            continue
        problems.append(f"name not in canon: {w}")
    allowed_nums = canon_numbers() | set(re.findall(r"\d[\d,]*(?:\.\d+)?", beat))
    for m in re.finditer(r"\d[\d,]*(?:\.\d+)?", text):
        v = m.group(0).rstrip(",")
        if v not in allowed_nums and v.replace(",", "") not in allowed_nums:
            problems.append(f"number not in canon: {v}")
    ok_words = set()
    for v in allowed_nums:
        try:
            ok_words |= number_words(int(float(v.replace(",", ""))))
        except ValueError:
            pass
    for w in BIGWORDS:
        if re.search(rf"\b{w}\b", text, re.I) and w not in ok_words and not re.search(rf"\b{w}\b", beat, re.I):
            problems.append(f"number word not in canon or chapter beats: {w}")
    if n:
        problems += hidden_problems(text, n)
        problems += must_problems(text, n)
    b = BANNED.search(text)
    if b:
        problems.append(f"leaked pipeline word: {b.group(0)}")
    return sorted(set(problems))

if __name__ == "__main__":
    path = sys.argv[1]
    n = int(sys.argv[sys.argv.index("--chapter") + 1]) if "--chapter" in sys.argv else None
    warns = []
    probs = check(open(path).read(), n, warns)
    for p in probs:
        print("-", p)
    for w in sorted(set(warns)):
        print("  warn:", w)
    print("PASSED" if not probs else f"FAILED: {len(probs)}")
    sys.exit(1 if probs else 0)
