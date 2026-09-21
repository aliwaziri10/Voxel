#!/usr/bin/env python3
"""
Proofreading checker for Voxel novel chapters.

SAFETY: Confirmed by Zia 2026-09-18: books 1, 2, and 3 (where-the-frost-
doesnt-reach, amity-falls-book-2, amity-falls-book-3) are ALL PUBLISHED
and are ALL hard-blocked from scanning, reporting, auto-fixing, or
writing. None of them can ever be selected. If a new, genuinely
unpublished book is started, add its folder name to UNPUBLISHED_BOOKS
below (and only there) once it exists and is confirmed unpublished by
Zia directly - never assume a book is safe to scan by default.

2026-09-21: amity-falls-book-4 added to UNPUBLISHED_BOOKS below, confirmed
unpublished and confirmed complete at 45 chapters by Zia directly. This
script is only ever run against it via manual workflow_dispatch (see
proofread.yml) - the push-trigger and daily schedule intentionally do NOT
include book-4, because multiple profiles/sessions may be actively editing
its chapters concurrently and an unsupervised auto-commit could race
against in-progress manual edits. Only run this manually, one profile at a
time, after confirming no one else is mid-edit.

Mechanical checks only. This script cannot check continuity, plot logic,
voice consistency, or canon accuracy against HANDOFF.md/beat_map.md -
that remains a manual review step (see HANDOFF.md "Pre-push checklist").

AUTO-FIX: dash/hyphen mechanics (em dash, en-dash-as-dash, non-breaking
hyphen, double-hyphen-as-dash) are auto-corrected in place, since these
have one unambiguous safe fix.

HARD VIOLATIONS (block CI via FAIL_ON_ISSUES, key suffixed _VIOLATION):
word-count hard floor, ai_tells, meta_leaks, duplicate sentences (within
a chapter and across chapters). These are objectively wrong, not
editorial judgment calls - an AI-tell phrase getting through defeats the
purpose of humanizer.py, a meta-leak breaks immersion outright, and a
verbatim duplicate sentence is never intentional.

BOOK 4 WORD COUNT (2026-09-21, per Zia): chapter lengths in Book 4 are
approved as they are, short and long. Book 4 word counts are NOT flagged
at all (no floor violation, no range advisory).

ADVISORY (report-only): word-count soft target (other books), overused words, dialogue
tags, repeated openers, long paragraphs, dialogue ratio, sentence rhythm.
Fixing those requires editorial judgment (a repeated name/theme word is
often fine), so they stay flagged for manual review rather than gating.
"""
import os
import re
import sys
import glob
import datetime
from collections import Counter

REPO_ROOT = os.environ.get("GITHUB_WORKSPACE", os.getcwd())

# All three existing novel folders are published (confirmed by Zia
# 2026-09-18). Add a new title here ONLY once Zia confirms it is
# actually unpublished - never infer that from a folder simply not
# being in PUBLISHED_BLOCKLIST yet.
PUBLISHED_BLOCKLIST = {
    "where-the-frost-doesnt-reach",
    "amity-falls-book-2",
    "amity-falls-book-3",
}
UNPUBLISHED_BOOKS = ["amity-falls-book-4"]

# Book 4 locked by Zia 2026-09-20: 45 chapters, 2,500 to 4,500 words each,
# none below 2,500. The workflow passes its own word_min/word_max inputs
# (defaults 1900/2500), so Book 4 overrides them here.
BOOK4 = "amity-falls-book-4"
BOOK4_MIN = 2500
BOOK4_MAX = 4500
# Book 4 word counts are never flagged (Zia approved every chapter length).
BOOK4_FLAG_WORD_COUNT = False

# Sentences that are repeated on purpose and must not fail the duplicate
# check. Chapter 8 has the same Drake letter read twice on purpose (a
# silent read, then a recorded read). Matched by sentence prefix.
DUPLICATE_ALLOW = {
    "chapter_08.md": (
        "He has the names of everyone who renewed the bargain since 1",
        "He says if we don't give them to him by the solstice, he pub",
    ),
}

# One-off exact-text tell fixes for Book 4 (2026-09-21). Applied only when
# AUTO_FIX is on. Each old string must appear exactly once in that chapter
# or it is skipped, so re-running is safe (idempotent).
TELL_FIXES = {
    "chapter_02.md": [("The pencil marks. The blank where the memory should be. The name that wasn't hers but looked like it could have been.", "The pencil marks. The blank where the memory should be. That name again, the one that could have been hers.")],
    "chapter_03.md": [("had been woven from silence", "had been made of silence")],
    "chapter_04.md": [("the particular dry scent of documents", "the dry scent of documents")],
    "chapter_06.md": [("The specific memories taken.", "The memories taken.")],
    "chapter_11.md": [
        ("She saw the particular care of people", "She saw the care of people"),
        ("Thorough. The kind of thorough that makes my job easier.", "Thorough. It makes my job easier."),
    ],
    "chapter_13.md": [("and the particular dust that settles on things", "and the dust that settles on things")],
    "chapter_15.md": [("The valley's particular gravity loosened its hold.", "The valley's gravity loosened its hold.")],
    "chapter_16.md": [("The kind of morning that made people forget", "A morning that made people forget")],
    "chapter_19.md": [
        ("It cited the specific memories allegedly taken", "It cited the memories allegedly taken"),
        ("Mara's eyes widened.", "Mara sat forward."),
        ("and the particular dust of a place that had learned", "and the dust of a place that had learned"),
    ],
    "chapter_23.md": [("the kind of calculated risk that made Wren's stomach tighten", "a calculated risk, and it made Wren's stomach tighten")],
    "chapter_24.md": [("The kind of thing anyone might say.", "The sort of thing anyone might say.")],
    "chapter_27.md": [("and the particular dust of the county archives", "and the dust of the county archives")],
    "chapter_30.md": [
        ("and the particular cold of metal that had spent", "and the cold of metal that had spent"),
        ("The kind of honesty that had no shelter in it.", "Honesty with no shelter in it."),
    ],
    "chapter_36.md": [
        ("pressing against this particular moment", "pressing against this moment"),
        ("without naming the specific gap", "without naming the gap"),
    ],
    "chapter_37.md": [
        ("and the specific torque specification the manufacturer", "and the torque specification the manufacturer"),
        ("and the particular quiet of a man", "and the quiet of a man"),
    ],
    "chapter_38.md": [("took on the particular calm it held", "took on the calm it held")],
    "chapter_39.md": [("The room sat in the kind of stillness that follows a bell", "The room sat in the stillness that follows a bell")],
}

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
    "theo", "marsh",
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


def load_extra_fixes() -> dict:
    """Extra exact-text fixes from scripts/book4_fixes.json:
    {"chapter_NN.md": [[old, new], [old, new, "all"]]}. Optional file."""
    import json
    path = os.path.join(REPO_ROOT, "scripts", "book4_fixes.json")
    if not os.path.exists(path):
        return {}
    with open(path, encoding="utf-8") as f:
        return json.load(f)


EXTRA_FIXES = load_extra_fixes()
UNMATCHED_FIXES = []


def apply_tell_fixes(fname: str, text: str) -> tuple:
    """Exact-text replacements from TELL_FIXES and book4_fixes.json.
    An entry applies only if its old text appears exactly once (or, with a
    third element "all", at least once). Already-applied entries (new text
    present, old absent) are skipped silently; entries matching neither
    are recorded in UNMATCHED_FIXES. Returns (text, n_applied)."""
    applied = 0
    entries = [list(e) for e in TELL_FIXES.get(fname, [])]
    entries += [list(e) for e in EXTRA_FIXES.get(fname, [])]
    for e in entries:
        old, new = e[0], e[1]
        replace_all = len(e) > 2 and e[2] == "all"
        n = text.count(old)
        if n == 1 or (replace_all and n >= 1):
            text = text.replace(old, new)
            applied += 1
        elif n == 0 and new in text:
            continue
        else:
            UNMATCHED_FIXES.append(f"{fname}: {old[:50]!r} (found {n}x)")
    return text, applied


def check_ai_tells(text: str) -> list:
    low = text.lower()
    out = []
    for p in AI_TELL_PHRASES:
        if p == "the specific":
            # noun use ("the specific, not the general") and words like
            # "the specifics" / "the specification" are not tells
            n = len(re.findall(r"\bthe specific\b(?!,)", low))
        else:
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


def check_duplicate_sentences_within(text: str, allow=()) -> list:
    """Hard check only for sentences of 60+ chars; short refrains and
    list items ("The standing arrangement notation.") are advisory.
    Sentences starting with any prefix in `allow` are repeated on purpose."""
    sentences = re.split(r"(?<=[.!?])\s+", text)
    seen, dupes = set(), []
    for s in sentences:
        s_norm = " ".join(s.split())
        if len(s_norm) < 60:
            continue
        if s_norm in seen and not any(s_norm.startswith(a) for a in allow):
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


def sentence_set(text: str, min_len=60) -> set:
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

    hard_floor, wmin, wmax = HARD_FLOOR, WORD_MIN, WORD_MAX
    if book == BOOK4:
        hard_floor, wmin, wmax = BOOK4_MIN, BOOK4_MIN, BOOK4_MAX

    # First pass: per-chapter checks + collect sentence sets for cross-chapter dedupe.
    per_chapter = []
    book_texts = []
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
            if book == BOOK4:
                new_text, n_tells = apply_tell_fixes(os.path.basename(path), text)
                if n_tells:
                    with open(path, "w", encoding="utf-8") as f:
                        f.write(new_text)
                    text = new_text
                    fixed_counts["tell phrases reworded"] = n_tells

        book_texts.append(text)
        paras = [p for p in text.split("\n\n") if p.strip()]
        wc = word_count(text)
        issues = {}

        if fixed_counts:
            issues["auto_fixed"] = ", ".join(f"{k}: {v}" for k, v in fixed_counts.items())

        if book == BOOK4 and not BOOK4_FLAG_WORD_COUNT:
            pass  # Book 4 chapter lengths are approved; never flagged
        elif wc < hard_floor:
            issues["word_count_VIOLATION"] = f"{wc}w (hard floor {hard_floor})"
        elif wc < wmin or wc > wmax:
            issues["word_count"] = f"{wc}w (target {wmin}-{wmax})"

        # Dashes are now auto-fixed above, so no remaining dash check here -
        # if fix_dashes still leaves something, it wasn't one of the four
        # known patterns and needs a human look (extremely unlikely).

        fname_issue = check_filename(path)
        if fname_issue:
            issues["filename"] = fname_issue

        # (check_name, check_fn, is_hard_violation) - hard violations are
        # objectively wrong and block CI; advisory ones need editorial
        # judgment and are report-only. See module docstring.
        for name, fn, hard in (
            ("ai_tells", check_ai_tells, True),
            ("meta_leaks", check_meta_leaks, True),
            ("overused_words", check_overused_words, False),
            ("dialogue_tags", check_dialogue_tags, False),
            ("duplicate_sentences_within_chapter",
             lambda t, _f=os.path.basename(path): check_duplicate_sentences_within(
                 t, DUPLICATE_ALLOW.get(_f, ())), True),
        ):
            res = fn(text)
            if res:
                key = f"{name}_VIOLATION" if hard else name
                issues[key] = res

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

    # Second pass: cross-chapter duplicate sentence detection. A verbatim
    # sentence shared between two chapters is never intentional, so this
    # is a hard violation like the within-chapter duplicate check above.
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
                    r["issues"]["cross_chapter_duplicates_VIOLATION"] = overlaps

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
        "mechanics are auto-fixed in place. Checks ending in `_VIOLATION` "
        "are hard failures that block CI (see FAIL_ON_ISSUES in the "
        "workflow); everything else is advisory and needs manual editorial "
        "judgment. It does NOT check continuity, plot logic, voice, or "
        "canon accuracy - see this book's HANDOFF.md \"Pre-push checklist\" "
        "for that.",
        "",
        f"- Chapters scanned: **{len(files)}**",
        f"- Total words: **{total_words:,}**",
        f"- Average chapter: **{total_words // max(len(files), 1):,}w**",
        f"- Chapters with issues: **{len(flagged)}**",
        f"- Chapters auto-fixed (dashes/hyphens): **{auto_fixed_count}**",
        f"- Chapters with hard violations (`_VIOLATION`, blocks CI): **{violations}**",
        ("- Word count: not flagged for this book (chapter lengths approved)"
         if book == BOOK4 and not BOOK4_FLAG_WORD_COUNT
         else f"- Target range: {wmin}-{wmax}w, hard floor {hard_floor}w"),
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

    if book == BOOK4 and AUTO_FIX and len(book_texts) == len(files):
        # Rebuild the compiled manuscript from the chapter files (it was
        # overwritten with a placeholder on 2026-09-21). Staged here so the
        # workflow's later "git diff --cached" commits it.
        ms_path = os.path.join(book_dir, "amity-falls-book-4_full_manuscript.md")
        with open(ms_path, "w", encoding="utf-8") as f:
            f.write("\n\n\n---\n\n".join(t.strip() for t in book_texts) + "\n")
        try:
            import subprocess
            subprocess.run(["git", "add", "-f", ms_path], cwd=REPO_ROOT, check=False)
        except Exception as e:
            print(f"could not stage manuscript: {e}")

    if book == BOOK4 and UNMATCHED_FIXES:
        lines.append("## Fixes not applied (text not found exactly once)")
        for u in UNMATCHED_FIXES:
            lines.append(f"- {u}")
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
