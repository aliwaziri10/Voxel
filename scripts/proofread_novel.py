#!/usr/bin/env python3
"""
Proofreading checker for Voxel novel chapters.
Scans novels/*/chapters/*.md, runs 10 parameter checks, writes a report,
and updates HANDOFF.md with a "Last verified" section.

Exit code 0 always (report-only tool, does not fail CI by default).
Set FAIL_ON_ISSUES=1 env var to make it exit non-zero when issues are found.
"""
import os
import re
import sys
import glob
import datetime
from collections import Counter

REPO_ROOT = os.environ.get("GITHUB_WORKSPACE", os.getcwd())
NOVELS_GLOB = os.path.join(REPO_ROOT, "novels", "*", "chapters", "*.md")
HANDOFF_PATH = os.path.join(REPO_ROOT, "HANDOFF.md")

WORD_MIN = 2000
WORD_MAX = 2300

AI_TELL_PHRASES = [
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

STOPWORDS = set("""
the a an and or but if of to in on at for with as is was were be been
being by from that this these those it its he she they them his her
their i you we me my your our not no so do did does than then there
here what who whom which when where why how all any both each few
more most other some such only own same just
""".split())


def word_count(text: str) -> int:
    return len(re.findall(r"[A-Za-z'’]+", text))


def check_em_dashes(text: str) -> int:
    return text.count("—") + len(re.findall(r"\s-\s", text))


def check_ai_tells(text: str) -> list[str]:
    low = text.lower()
    return [p for p in AI_TELL_PHRASES if p in low]


def check_repeated_openers(paras: list[str]) -> list[str]:
    flags = []
    run = []
    for p in paras:
        p = p.strip()
        if not p or p.startswith('"'):
            run = []
            continue
        first_word = p.split(" ")[0].strip('.,!?"').lower()
        run.append(first_word)
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
    seen = {}
    dupes = []
    for s in sentences:
        s_norm = s.strip()
        if len(s_norm) < 20:
            continue
        if s_norm in seen:
            dupes.append(s_norm[:60] + "...")
        seen[s_norm] = True
    return dupes


def check_chapter(path: str) -> dict:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    paras = [p for p in text.split("\n\n") if p.strip()]
    wc = word_count(text)

    issues = {}
    if wc < WORD_MIN or wc > WORD_MAX:
        issues["word_count"] = f"{wc}w (target {WORD_MIN}-{WORD_MAX})"
    em = check_em_dashes(text)
    if em:
        issues["em_dashes"] = f"{em} found"
    tells = check_ai_tells(text)
    if tells:
        issues["ai_tells"] = tells
    openers = check_repeated_openers(paras)
    if openers:
        issues["repeated_openers"] = openers
    overused = check_overused_words(text)
    if overused:
        issues["overused_words"] = overused
    tags = check_dialogue_tags(text)
    if tags:
        issues["dialogue_tags"] = tags
    outliers = check_paragraph_outliers(paras)
    if outliers:
        issues["long_paragraphs"] = f"{outliers} paragraph(s) over 200w with no dialogue"
    dupes = check_duplicate_sentences(text)
    if dupes:
        issues["duplicate_sentences"] = dupes

    return {"path": path, "word_count": wc, "issues": issues}


def main():
    files = sorted(glob.glob(NOVELS_GLOB))
    if not files:
        print("No chapter files found.")
        return 0

    results = [check_chapter(f) for f in files]
    total_issues = sum(len(r["issues"]) for r in results)

    lines = []
    lines.append(f"# Proofreading Report — {datetime.datetime.utcnow().isoformat()}Z")
    lines.append("")
    lines.append(f"Scanned {len(files)} chapter file(s). {total_issues} chapter(s) with flagged issues.")
    lines.append("")

    for r in results:
        rel = os.path.relpath(r["path"], REPO_ROOT)
        if not r["issues"]:
            continue
        lines.append(f"## {rel} — {r['word_count']}w")
        for check, detail in r["issues"].items():
            lines.append(f"- **{check}**: {detail}")
        lines.append("")

    report = "\n".join(lines)
    report_path = os.path.join(REPO_ROOT, "PROOFREAD_REPORT.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(report)
    print(report)

    # Update HANDOFF.md with a "Last verified" stamp
    if os.path.exists(HANDOFF_PATH):
        with open(HANDOFF_PATH, encoding="utf-8") as f:
            handoff = f.read()
    else:
        handoff = ""

    stamp = (
        f"\n\n## Proofreading — Last Verified\n"
        f"- Run: {datetime.datetime.utcnow().isoformat()}Z\n"
        f"- Chapters scanned: {len(files)}\n"
        f"- Chapters with issues: {total_issues}\n"
        f"- Full report: PROOFREAD_REPORT.md\n"
        f"- Re-verify against live data before trusting this doc at face value.\n"
    )
    marker = "## Proofreading — Last Verified"
    if marker in handoff:
        handoff = re.sub(
            r"## Proofreading — Last Verified.*?(?=\n## |\Z)",
            stamp.strip() + "\n",
            handoff,
            flags=re.DOTALL,
        )
    else:
        handoff = handoff.rstrip() + stamp

    with open(HANDOFF_PATH, "w", encoding="utf-8") as f:
        f.write(handoff)

    if os.environ.get("FAIL_ON_ISSUES") == "1" and total_issues > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
