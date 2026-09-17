#!/usr/bin/env python3
"""
Batch word-repetition scanner for Voxel novel chapters.

Scans ALL tracked banned/hedge words and phrases across ALL given chapters
in a single pass, instead of checking one word at a time per chapter.
Outputs a consolidated report grouped by chapter, with line context, so a
reviewer can apply every fix for a chapter in one edit instead of
re-scanning per word.

This is a REPORTING tool for the "some/something" hedge and "the kind of"
filler family specifically, because those require editorial judgment
(many uses are genuine and must be left alone) - it does NOT blind-replace
them. It DOES safely auto-fix the small set of patterns that have exactly
one correct fix everywhere (see SAFE_AUTOFIX below).

Usage:
    python3 word_repetition_fixer.py <chapter1.md> [chapter2.md ...]
    python3 word_repetition_fixer.py --dir <chapters_dir>
"""
import re
import sys
import os
import glob

# Words/phrases needing editorial judgment - reported with context, not auto-fixed.
TRACKED_PATTERNS = {
    "particular": r"\bparticular(?:ly)?\b",
    "the specific ___": r"\bthe specific\b",
    "the kind of ___": r"\b(?:the|that|this|its?|own|some) kind of\b",
    "some/something hedge": r"\bsome(?:thing|one|how|what)?\b",
}

# Patterns with exactly one safe, unambiguous fix everywhere - auto-applied.
SAFE_AUTOFIX = [
    (r"\u2014", " - "),          # em dash
    (r"\s\u2013\s", " - "),      # en dash used as a dash
    (r"\u2011", "-"),            # non-breaking hyphen
    (r"\s--\s", " - "),          # double-hyphen-as-dash
]


def scan_chapter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    lines = text.split("\n")
    hits = {name: [] for name in TRACKED_PATTERNS}
    for lineno, line in enumerate(lines, 1):
        for name, pattern in TRACKED_PATTERNS.items():
            for m in re.finditer(pattern, line, re.IGNORECASE):
                snippet = line.strip()
                if len(snippet) > 100:
                    start = max(0, m.start() - 40)
                    end = min(len(line), m.end() + 40)
                    snippet = "..." + line[start:end].strip() + "..."
                hits[name].append((lineno, snippet))
    return hits, text


def autofix_chapter(path):
    with open(path, encoding="utf-8") as f:
        text = f.read()
    original = text
    counts = {}
    for pattern, repl in SAFE_AUTOFIX:
        text, n = re.subn(pattern, repl, text)
        if n:
            counts[pattern] = n
    text = re.sub(r" {2,}", " ", text)
    if text != original:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
    return counts


def main():
    args = sys.argv[1:]
    if not args:
        print(__doc__)
        return
    if args[0] == "--dir":
        files = sorted(glob.glob(os.path.join(args[1], "*.md")))
    else:
        files = args

    total_by_pattern = {name: 0 for name in TRACKED_PATTERNS}

    for path in files:
        fixed = autofix_chapter(path)
        hits, _ = scan_chapter(path)
        any_hits = any(hits[name] for name in TRACKED_PATTERNS)
        if not any_hits and not fixed:
            continue
        print(f"\n=== {os.path.basename(path)} ===")
        if fixed:
            print(f"  [auto-fixed] {fixed}")
        for name, matches in hits.items():
            if not matches:
                continue
            total_by_pattern[name] += len(matches)
            print(f"  [{name}] {len(matches)} instance(s):")
            for lineno, snippet in matches:
                print(f"    L{lineno}: {snippet}")

    print("\n=== TOTALS ACROSS ALL SCANNED CHAPTERS ===")
    for name, count in total_by_pattern.items():
        print(f"  {name}: {count}")


if __name__ == "__main__":
    main()
