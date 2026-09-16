#!/usr/bin/env python3
"""
Proofreading checker for Voxel novel chapters.

SAFETY: Book 1 (where-the-frost-doesnt-reach) is PUBLISHED and is hard-blocked
from scanning, reporting, or writing. It can never be selected.

Mechanical checks only. This script cannot check continuity, plot logic,
voice consistency, or canon accuracy against HANDOFF.md/beat_map.md -
that remains a manual review step (see HANDOFF.md "Pre-push checklist").

AUTO-FIX: dash/hyphen mechanics (em dash, en-dash-as-dash, non-breaking
hyphen, double-hyphen-as-dash) are auto-corrected in place, since these
have one unambiguous safe fix. Everything else (word count, overused
words, AI-tell phrasing, repeated openers, pacing, dialogue tags) is
report-only - fixing those requires editorial judgment, not a mechanical
rule, so it stays flagged for manual review.
"""
import os
import re
import sys
import glob
import datetime
from collections import Counter

REPO_ROOT = os.environ.get("GITHUB_WORKSPACE", os.getcwd())

PUBLISHED_BLOCKLIST = {"where-the-frost-doesnt-reach"}
UNPUBLISHED_BOOKS = ["amity-falls-book-2", "amity-falls-book-3"]

BOOK = os.environ.get("BOOK", "all-unpublished")
# Confirmed by Zia 2026-09-16: floor relaxed to ~1900w, do not require 2300+.
WORD_MIN = int(os.environ.get("WORD_MIN", "1900"))
WORD_MAX = int(os.environ.get("WORD_MAX", "2500"))
HARD_FLOOR = 1900
AUTO_FIX = os.environ.get("AUTO_FIX", "1") == "1"

# Series-specific names/nouns that will legitimately repeat often and
# should never trigger the overused-word check.
SERIES_ALLOWLIST = {
    "dev", "priya", "mara", "caleb", "wren", "yusuf", "denise", "odette",
    "elias", "thorne", "halloran", "eleanor", "ambrose", "whitlock",
    "farrow", "castellan", "adelaide", "kell",
    "ring", "silo", "bargain", "eclipse", "valley", "orchard", "council",
    "blackout", "blackouts", "taking", "carrier", "candidate", "candidates",
}

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
    "poignant reminder", "bittersweet", "palpable", "steely resolve",
    "eyes widened", "let out a breath she didn't know she was holding",
    "sent a shiver down", "a mix of", "couldn't help but",
]

DIALOGUE_TAG_FLAGS = [
    "exclaimed", "interjected", "proclaimed", "bellowed", "retorted",
    "quipped", "snapped back", "ejaculated", "expostulated",
]

META_LEAKS = [
    "book one", "book two", "book three", "book 1", "book 2", "book 3",
    "chapter one of", "the previous book", "the last book",
]

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


def fix_dashes(text: str) -> tuple:
    """Auto-corrects dash/hyphen mechanics to a plain ' - '. Returns
    (fixed_text, counts_dict). This is the one category of issue with
    a single unambiguous safe fix, so it's applied in place rather than
    just reported."""
    counts = {}

    def _sub(pattern, repl, key, s):
        s2, n = re.subn(pattern, repl, s)
        if n:
            counts[key] = n
        return s2

    text = _sub(r"\u2014", " - ", "em_dash (\u2014)", text)
    text = _sub(r"\s\u2013\s", " - ", "en_dash used as dash ( \u2013 )", text)
    text = _sub(r"\u2011", "-", "non-breaking hyphen (\u2011)", text)
    text = _sub(r"\s--\s", " - ", "double hyphen as dash (--)", text)
    # Clean up any doubled spaces introduced by the substitutions.
    text = re.sub(r" {2,}", " ", text)
    text = re.sub(r" \n", "\n", text)
    return text, counts


def check_ai_tells(text: str) -> list:
    low = text.lower()
    out = []
    for p in AI_TELL_PHRASES:
        n = low.count(p)
        if n:
            out.append(f"{p} x{n}")
    return out


def check_meta_leaks(text: str) -> list:
    low = text.lower()
    return [m for m in META_LEAKS if m in low]


def check_repeated_openers(paras: list) -> list:
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


def check_overused_words(text: str) -> list:
    words = [w.lower() for w in re.findall(r"[A-Za-z']+", text)]
    counts = Counter(
        w for w in words
        if w not in STOPWORDS and w not in SERIES_ALLOWLIST and len(w) > 3
    )
    return [f"{w} x{c}" for w, c in counts.items() if c >= 6]


def check_dialogue_tags(text: str) -> list:
    low = text.lower()
    return [t for t in DIALOGUE_TAG_FLAGS if t in low]


def check_paragraph_outliers(paras: list) -> int:
    return sum(1 for p in paras if word_count(p) > 200 and '"' not in p)


def check_duplicate_sentences_within(text: str) -> list:
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


def check_dialogue_ratio(text: str):
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


def check_sentence_rhythm(text: str):
    """Advisory only. Flags a chapter as monotonous if its sentence lengths
    have unusually low variance (every sentence roughly the same length is
    a common AI-prose tell and a genuine line-editing problem; real prose
    mixes short punchy sentences with longer ones). Also flags a high ratio
    of 'telling' verbs (felt/realized/understood/knew/seemed) per 1000 words
    as a rough show-vs-tell signal. Both are hints for a human editor to
    look at, not violations -- a chapter can trip this and still be fine."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    lengths = [len(re.findall(r"[A-Za-z']+", s)) for s in sentences if s.strip()]
    lengths = [l for l in lengths if l > 0]
    if len(lengths) < 10:
        return None
    mean = sum(lengths) / len(lengths)
    variance = sum((l - mean) ** 2 for l in lengths) / len(lengths)
    stdev = variance ** 0.5
    flags = []
    if stdev < 4.5:
        flags.append(f"low sentence-length variance (stdev {stdev:.1f}, mean {mean:.0f}w) - check for monotonous rhythm")

    telling_words = ["felt", "feeling", "realized", "understood", "knew", "seemed", "noticed"]
    wc = word_count(text)
    telling_count = sum(len(re.findall(rf"\b{w}\b", text, re.IGNORECASE)) for w in telling_words)
    per_1000 = (telling_count / wc * 1000) if wc else 0
    if per_1000 > 10:
        flags.append(f"{telling_count} telling-verbs ({per_1000:.1f}/1000w) - check show-vs-tell balance")

    return flags or None


def check_filename(path: str) -> list:
    """Enforces lowercase chapter_NN.md naming per standing rule."""
    name = os.path.basename(path)
    if not re.match(r"^chapter_\d{2}\.md$", name):
        return [f"non-standard filename: '{name}' (expected chapter_NN.md)"]
    return []


def sentence_set(text: str, min_len=25) -> set:
    sentences = re.split(r"(?<=[.!?])\s+", text)
    return {" ".join(s.split()) for s in sentences if len(" ".join(s.split())) >= min_len}


def resolve_books(book_arg: str) -> list:
    books = list(UNPUBLISHED_BOOKS) if book_arg == "all-unpublished" else [book_arg]
    safe = []
    for b in books:
        if b in PUBLISHED_BLOCKLIST:
            print(f"REFUSED: '{b}' is published and is never scanned.")
            continue
        safe.append(b)
    return safe


def process_book(book: str) -> int:
    book_dir = os.path.join(REPO_ROOT, "novels", book)
    files = sorted(glob.glob(os.path.join(book_dir, "chapters", "*.md")))
    if not files:
        print(f"No chapters found for {book}.")
        return 0

    # First pass: per-chapter checks + collect sentence sets for cross-chapter dedupe.
    per_chapter = []
    chapter_sentences = {}
    for path in files:
        with open(path, encoding="utf-8") as f:
            text = f.read()

        fixed_counts = {}
        if AUTO_FIX:
            new_text, fixed_counts = fix_dashes(text)
            if fixed_counts and new_text != text:
                with open(path, "w", encoding="utf-8") as f:
                    f.write(new_text)
                text = new_text

        paras = [p for p in text.split("\n\n") if p.strip()]
        wc = word_count(text)
        issues = {}

        if fixed_counts:
            issues["auto_fixed"] = ", ".join(f"{k}: {v}" for k, v in fixed_counts.items())

        if wc < HARD_FLOOR:
            issues["word_count_VIOLATION"] = f"{wc}w (hard floor {HARD_FLOOR})"
        elif wc < WORD_MIN or wc > WORD_MAX:
            issues["word_count"] = f"{wc}w (target {WORD_MIN}-{WORD_MAX})"

        # Dashes are now auto-fixed above, so no remaining dash check here -
        # if fix_dashes still leaves something, it wasn't one of the four
        # known patterns and needs a human look (extremely unlikely).

        fname_issue = check_filename(path)
        if fname_issue:
            issues["filename"] = fname_issue

        for name, fn in (
            ("ai_tells", check_ai_tells),
            ("meta_leaks", check_meta_leaks),
            ("overused_words", check_overused_words),
            ("dialogue_tags", check_dialogue_tags),
            ("duplicate_sentences_within_chapter", check_duplicate_sentences_within),
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

        rhythm = check_sentence_rhythm(text)
        if rhythm:
            issues["rhythm_advisory"] = rhythm

        per_chapter.append({"path": path, "word_count": wc, "issues": issues})
        chapter_sentences[path] = sentence_set(text)

    # Second pass: cross-chapter duplicate sentence detection.
    paths = list(chapter_sentences.keys())
    for i, p1 in enumerate(paths):
        overlaps = []
        for p2 in paths[i + 1:]:
            shared = chapter_sentences[p1] & chapter_sentences[p2]
            if shared:
                overlaps.append(f"{os.path.basename(p2)}: {len(shared)} shared line(s)")
        if overlaps:
            for r in per_chapter:
                if r["path"] == p1:
                    r["issues"]["cross_chapter_duplicates"] = overlaps

    results = per_chapter
    flagged = [r for r in results if r["issues"]]
    violations = sum(
        1 for r in results
        if any(k.endswith("_VIOLATION") for k in r["issues"])
    )
    auto_fixed_count = sum(1 for r in results if "auto_fixed" in r["issues"])
    total_words = sum(r["word_count"] for r in results)

    lines = [
        f"# Proofreading Report: {book}",
        f"_Generated {datetime.datetime.now(datetime.timezone.utc).isoformat()}Z_",
        "",
        "**This report covers mechanical checks only** (word count, dashes, "
        "banned phrases, filename convention, repetition). Dash/hyphen "
        "mechanics are auto-fixed in place; everything else here still "
        "needs manual review. It does NOT check continuity, plot logic, "
        "voice, or canon accuracy - see this book's HANDOFF.md "
        "\"Pre-push checklist\" for that.",
        "",
        f"- Chapters scanned: **{len(files)}**",
        f"- Total words: **{total_words:,}**",
        f"- Average chapter: **{total_words // max(len(files), 1):,}w**",
        f"- Chapters with issues: **{len(flagged)}**",
        f"- Chapters auto-fixed (dashes/hyphens): **{auto_fixed_count}**",
        f"- Hard violations (word floor): **{violations}**",
        f"- Target range: {WORD_MIN}-{WORD_MAX}w, hard floor {HARD_FLOOR}w",
        "",
    ]

    if not flagged:
        lines.append("No issues found.")
    for r in flagged:
        lines.append(f"## {os.path.basename(r['path'])} \u2014 {r['word_count']}w")
        for check, detail in r["issues"].items():
            if isinstance(detail, list):
                detail = "; ".join(detail)
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
            f"- Run: {datetime.datetime.now(datetime.timezone.utc).isoformat()}Z\n"
            f"- Chapters scanned: {len(files)} | Total: {total_words:,}w\n"
            f"- Chapters with issues: {len(flagged)} | Auto-fixed: {auto_fixed_count} | "
            f"Hard violations: {violations}\n"
            f"- Full report: `novels/{book}/PROOFREAD_REPORT.md`\n"
            f"- Mechanical checks only - manual pre-push checklist still required.\n"
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
