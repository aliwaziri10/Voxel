#!/usr/bin/env python3
"""
Continuity extractor for Voxel novel chapters.
Unlike proofread_novel.py (mechanical style checks), this tool extracts
STRUCTURED FACTS per chapter so a human/AI editor can actually reason about
plot logic, timeline consistency, and character-knowledge leaks -- things
regex cannot judge on its own, but can surface for judgment.

Outputs a single CONTINUITY_EXTRACT.md per book with, for each chapter:
- Every named character mention (for spelling-variant detection)
- Every explicit time reference ("six weeks", "three days after", "eleven days")
- Every capitalized multi-word phrase that looks like a proper noun (places,
  organizations) not already in the known character list
- First and last line of the chapter (for a fast manual continuity skim)

This does NOT judge correctness. It organizes the raw material so an editor
can. Read the output, then do the actual reasoning.
"""
import os
import re
import sys
import glob
from collections import defaultdict, Counter

REPO_ROOT = os.environ.get("GITHUB_WORKSPACE", os.getcwd())

TIME_PATTERNS = [
    r"\b(one|two|three|four|five|six|seven|eight|nine|ten|eleven|twelve|\d+)\s+(day|days|week|weeks|month|months|year|years|hour|hours|minute|minutes)\b",
    r"\b(yesterday|tomorrow|tonight|this morning|last night|next week)\b",
]

PROPER_NOUN_RE = re.compile(r"\b([A-Z][a-z]+(?:\s+[A-Z][a-z]+){0,2})\b")

# Common sentence-start words that are capitalized but not proper nouns
STOPWORD_CAPS = set("""
The A An And But If Or So When While As Because Then There Here
It She He They We I You Not No Yes Maybe Perhaps Still Yet Now
Whatever Something Nothing Everything Anyone Someone No One Everyone
""".split())


def find_book_dirs():
    return sorted(glob.glob(os.path.join(REPO_ROOT, "novels", "*")))


def extract_chapter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines = [l for l in text.split("\n") if l.strip()]
    first_line = lines[1] if len(lines) > 1 else ""  # skip CHAPTER heading
    last_line = lines[-1] if lines else ""

    time_refs = []
    for pat in TIME_PATTERNS:
        for m in re.finditer(pat, text, re.IGNORECASE):
            time_refs.append(m.group(0))

    proper_nouns = Counter()
    for m in PROPER_NOUN_RE.finditer(text):
        phrase = m.group(1)
        first_word = phrase.split(" ")[0]
        if first_word in STOPWORD_CAPS:
            continue
        proper_nouns[phrase] += 1

    return {
        "path": path,
        "first_line": first_line.strip()[:150],
        "last_line": last_line.strip()[:150],
        "time_refs": time_refs,
        "proper_nouns": proper_nouns,
    }


def fuzzy_variant_groups(all_names):
    """Group names that are likely spelling variants of each other
    (same first token, or Levenshtein distance <= 2 on close-length strings).
    NOTE: known to be noisy on short common words -- filter results manually,
    only names of length >= 5 are worth reviewing."""
    def lev(a, b):
        if abs(len(a) - len(b)) > 2:
            return 99
        prev = list(range(len(b) + 1))
        for i, ca in enumerate(a, 1):
            cur = [i]
            for j, cb in enumerate(b, 1):
                cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
            prev = cur
        return prev[-1]

    names = sorted([n for n in all_names if len(n) >= 5], key=lambda n: -all_names[n])
    groups = []
    used = set()
    for i, n1 in enumerate(names):
        if n1 in used:
            continue
        group = [n1]
        for n2 in names[i + 1:]:
            if n2 in used:
                continue
            if lev(n1, n2) <= 2 and n1 != n2:
                group.append(n2)
                used.add(n2)
        if len(group) > 1:
            groups.append(group)
        used.add(n1)
    return groups


def main():
    book_dirs = find_book_dirs()
    for book_dir in book_dirs:
        chapters_dir = os.path.join(book_dir, "chapters")
        if not os.path.isdir(chapters_dir):
            continue
        files = sorted(glob.glob(os.path.join(chapters_dir, "*.md")))
        if not files:
            continue

        book_name = os.path.basename(book_dir)
        all_extracts = [extract_chapter(f) for f in files]

        all_names = Counter()
        for ex in all_extracts:
            all_names.update(ex["proper_nouns"])

        variant_groups = fuzzy_variant_groups(all_names)

        lines = []
        lines.append(f"# Continuity Extract — {book_name}")
        lines.append("")
        lines.append(f"Scanned {len(files)} chapters. This is RAW MATERIAL for editorial review, not a verdict.")
        lines.append("Known limitation: name-variant grouping is noisy on short/common words; only review groups where both names look like real character/place names.")
        lines.append("")

        if variant_groups:
            lines.append("## Possible name/spelling variants (review each group manually, length>=5 only)")
            for g in variant_groups:
                counts = ", ".join(f'"{n}" x{all_names[n]}' for n in g)
                lines.append(f"- {counts}")
            lines.append("")
        else:
            lines.append("## Possible name/spelling variants\nNone detected.\n")

        lines.append("## Per-chapter time references (check sequencing/math manually)")
        for ex in all_extracts:
            rel = os.path.relpath(ex["path"], REPO_ROOT)
            refs = ", ".join(ex["time_refs"]) if ex["time_refs"] else "(none found)"
            lines.append(f"- **{rel}**: {refs}")
        lines.append("")

        lines.append("## Per-chapter opening/closing lines (fast continuity skim)")
        for ex in all_extracts:
            rel = os.path.relpath(ex["path"], REPO_ROOT)
            lines.append(f"### {rel}")
            lines.append(f"- Opens: {ex['first_line']}")
            lines.append(f"- Closes: {ex['last_line']}")
        lines.append("")

        out_path = os.path.join(book_dir, "CONTINUITY_EXTRACT.md")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    sys.exit(main())
