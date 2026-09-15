#!/usr/bin/env python3
"""
Proofreading checker for Voxel novel chapters.

SAFETY: Book 1 (where-the-frost-doesnt-reach) is PUBLISHED and is hard-blocked
from scanning. It can never be selected, reported on, or modified.

Selects a book via the BOOK env var, runs parameter checks, writes a
per-book report, and stamps that book's own HANDOFF.md.
"""
import os
import re
import sys
import glob
import datetime
from collections import Counter

REPO_ROOT = os.environ.get("GITHUB_WORKSPACE", os.getcwd())

# Hard block. Published books must never be scanned or written to.
PUBLISHED_BLOCKLIST = {"where-the-frost-doesnt-reach"}

UNPUBLISHED_BOOKS = ["amity-falls-book-2", "amity-falls-book-3"]

BOOK = os.environ.get("BOOK", "amity-falls-book-3")
WORD_MIN = int(os.environ.get("WORD_MIN", "2300"))
WORD_MAX = int(os.environ.get("WORD_MAX", "2500"))

# Hard floor below which a chapter is called a violation, not a warning.
HARD_FLOOR = 2100


def resolve_books(book_arg: str) -> list[str]:
    if book_arg == "all-unpublished":
        books = list(UNPUBLISHED_BOOKS)
    else:
        books = [book_arg]
    safe = []
    for b in books:
        if b in PUBLISHED_BLOCKLIST:
            print(f"REFUSED: '{b}' is published and is never scanned.")
            continue
        safe.append(b)
    return safe


AI_TELL_PHRASES = [
    "particular", "the specific", "the kind of",
    "a testament to", "in the tapestry of", "it's important to note",
    "boasts", "unwavering", "whispered promise", "delve into",
    "in the realm of", "stands as a", "serves as a reminder",
    "a symphony of", "a rich tapestry", "underscores the",
    "plays a pivotal role", "in today's world", "navigating the",
    "it is worth noting", "a beacon of", "at the end of the day",
    "when it comes to", "in conclusion", "furthermore,", "moreover,",
    "the intricate", "the ever-evolving", "elevate", "unleash",
    "harness the power", "in the world of", "game-changer",
    "seamlessly", "meticulously", "tapestry of", "woven",
    "poignant reminder", "bittersweet", "palpable",
]

DIALOGUE_TAG_FLAGS = [
    "exclaimed", "interjected", "proclaimed", "bellowed", "retorted",
    "quipped", "snapped back", "ejaculated", "expostulated",
]

# Meta-references that must never appear in chapter prose.
META_LEAKS = ["book one", "book two", "book three", "book 1", "book 2", "book 3",
              "chapter one of", "the previous book", "the last book"]

STOPWORDS = set("""
the a an and or but if of to in on at for with as is was were be been
being by from that this these those it its he she they them his her
their i you we me my your our not no so do did does than then there
here what who whom which when where why how all any both each few
more most other some such only own same just had have has would could
said say says about into over under after before again very
""".split())


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z'\u2019]+", text))


def check_em_dashes(text: str) -> int:
    return text.count("\u2014") + text.count("--")


def check_ai_tells(text: str) -> list[str]:
    low = text.lower()
    out = []
    for p in AI_TELL_PHRASES:
        n = low.count(p)
        if n:
            out.append(f"{p} x{n}")
    return out


def check_meta_leaks(text: str) -> list[str]:
    low = text.lower()
    return [m for m in META_LEAKS if m in low]


def check_repeated_openers(paras: list[str]) -> list[str]:
    flags, run = [], []
    for p in paras:
        p = p.strip()
        if not p or p.startswith('"'):
            run = []
            continue
        first = p.split(" ")[0].strip('.,!?"').lower()
        run.append(first)
        if len(run) >= 3 and run[-1] == run[-2] == run[-3]:
            flags.append(f'"{run[-1]}" opens 3+ consecutive paragraphs')
            run = []
    return flags


def check_overused_words(text: str) -> list[str]:
    words = [w.lower() for w in re.findall(r"[A-Za-z']+", text)]
    counts = Counter(w for w in words if w not in STOPWORDS and len(w) > 3)
    return [f"{w} x{c}" for w, c in counts.items() if c >= 6]


def check_dialogue_tags(text: str) -> list[str]:
    low = text.lower()
    return [t for t in DIALOGUE_TAG_FLAGS if t in low]


def check_paragraph_outliers(paras: list[str]) -> int:
    return sum(1 for p in paras if word_count(p) > 200 and '"' not in p)


def check_duplicate_sentences(text: str) -> list[str]:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    seen, dupes = set(), []
    for s in sentences:
        s_norm = " ".join(s.split())
        if len(s_norm) < 25:
            continue
        if s_norm in seen:
            dupes.append(s_norm[:60] + "...")
        seen.add(s_norm)
    return dupes


def check_dialogue_ratio(text: str) -> str | None:
    """Flags chapters that are nearly all dialogue or nearly all narration."""
    total = word_count(text)
    if not total:
        return None
    quoted = sum(word_count(m) for m in re.findall(r'"[^"]*"', text))
    pct = round(100 * quoted / total)
    if pct < 10:
        return f"{pct}% dialogue (very narration-heavy)"
    if pct > 75:
        return f"{pct}% dialogue (very little narration)"
    return None


def check_chapter(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    paras = [p for p in text.split("\n\n") if p.strip()]
    wc = word_count(text)
    issues = {}

    if wc < HARD_FLOOR:
        issues["word_count_VIOLATION"] = f"{wc}w (hard floor {HARD_FLOOR})"
    elif wc < WORD_MIN or wc > WORD_MAX:
        issues["word_count"] = f"{wc}w (target {WORD_MIN}-{WORD_MAX})"

    em = check_em_dashes(text)
    if em:
        issues["em_dashes_VIOLATION"] = f"{em} found (must be zero)"

    for name, fn in (
        ("ai_tells", check_ai_tells),
        ("meta_leaks", check_meta_leaks),
        ("overused_words", check_overused_words),
        ("dialogue_tags", check_dialogue_tags),
        ("duplicate_sentences", check_duplicate_sentences),
    ):
        res = fn(text)
        if res:
            issues[name] = res

    openers = check_repeated_openers(paras)
    if openers:
        issues["repeated_openers"] = openers

    outliers = check_paragraph_outliers(paras)
    if outliers:
        issues["long_paragraphs"] = f"{outliers} paragraph(s) over 200w, no dialogue"

    ratio = check_dialogue_ratio(text)
    if ratio:
        issues["dialogue_ratio"] = ratio

    return {"path": path, "word_count": wc, "issues": issues}


def process_book(book: str) -> int:
    book_dir = os.path.join(REPO_ROOT, "novels", book)
    files = sorted(glob.glob(os.path.join(book_dir, "chapters", "*.md")))
    if not files:
        print(f"No chapters found for {book}.")
        return 0

    results = [check_chapter(f) for f in files]
    flagged = [r for r in results if r["issues"]]
    violations = sum(
        1 for r in results
        if any(k.endswith("_VIOLATION") for k in r["issues"])
    )
    total_words = sum(r["word_count"] for r in results)

    lines = [
        f"# Proofreading Report: {book}",
        f"_Generated {datetime.datetime.utcnow().isoformat()}Z_",
        "",
        f"- Chapters scanned: **{len(files)}**",
        f"- Total words: **{total_words:,}**",
        f"- Average chapter: **{total_words // max(len(files), 1):,}w**",
        f"- Chapters with issues: **{len(flagged)}**",
        f"- Hard violations (word floor / em dashes): **{violations}**",
        f"- Target range: {WORD_MIN}-{WORD_MAX}w, hard floor {HARD_FLOOR}w",
        "",
    ]

    if not flagged:
        lines.append("No issues found.")
    for r in flagged:
        rel = os.path.relpath(r["path"], REPO_ROOT)
        lines.append(f"## {os.path.basename(rel)} \u2014 {r['word_count']}w")
        for check, detail in r["issues"].items():
            if isinstance(detail, list):
                detail = ", ".join(detail)
            lines.append(f"- **{check}**: {detail}")
        lines.append("")

    report = "\n".join(lines)
    with open(os.path.join(book_dir, "PROOFREAD_REPORT.md"), "w", encoding="utf-8") as f:
        f.write(report)
    print(report)

    handoff_path = os.path.join(book_dir, "HANDOFF.md")
    if os.path.exists(handoff_path):
        with open(handoff_path, encoding="utf-8") as f:
            handoff = f.read()
        stamp = (
            f"## Proofreading \u2014 Last Verified\n"
            f"- Run: {datetime.datetime.utcnow().isoformat()}Z\n"
            f"- Chapters scanned: {len(files)} | Total: {total_words:,}w\n"
            f"- Chapters with issues: {len(flagged)} | Hard violations: {violations}\n"
            f"- Full report: `novels/{book}/PROOFREAD_REPORT.md`\n"
        )
        marker = "## Proofreading \u2014 Last Verified"
        if marker in handoff:
            handoff = re.sub(
                re.escape(marker) + r".*?(?=\n## |\Z)",
                stamp, handoff, flags=re.DOTALL,
            )
        else:
            handoff = handoff.rstrip() + "\n\n" + stamp
        with open(handoff_path, "w", encoding="utf-8") as f:
            f.write(handoff)

    return violations


def main():
    books = resolve_books(BOOK)
    if not books:
        print("No scannable books selected.")
        return 0
    total_violations = sum(process_book(b) for b in books)
    if os.environ.get("FAIL_ON_ISSUES") == "1" and total_violations > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
