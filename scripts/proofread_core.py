#!/usr/bin/env python3
"""
proofread_core.py - read-only mechanical proofreading engine for NEW Voxel
novels. Added 2026-10-20 (see PROOFREAD_UPGRADE_HANDOFF.md).

WHAT IT IS
One shared, fast, deterministic (no LLM, no network, no Java) pass that
labels every finding with a KDP-style severity tier and returns one verdict
per book. It sits NEXT TO the existing scripts (proofread_novel.py,
manuscript_qa.py, proofreader.py, humanizer.py) and replaces none of them
yet. Nothing here ever writes to a chapter file: it only reads chapters and
writes a report.

TIERS (our own mapping, modeled on the Critical / Destructive / Distracting
language on Amazon's KDP content-quality help page; Amazon says any Critical
issue removes a book from sale, and that US/UK spelling differences and
intentional dialect are not errors):
  CRITICAL     soft hyphens, zero-width/junk characters, digits inside words,
               leaked markup or placeholders, AI meta-leaks, in-line page
               numbers, corrupted or empty chapter files.      -> BLOCKED
  DESTRUCTIVE  doubled words, unbalanced quotes, repeated punctuation, the
               house no-em-dash rule.                           -> NEEDS-REVISION
  DISTRACTING  spacing and punctuation slips, mixed quote or ellipsis style,
               dialogue-tag punctuation, a/an, British spelling (US-first).
  REVIEW       human judgment: Britishisms, chapter outside the word band.
               Never auto-fixed, and a short chapter is NEVER a reason to pad
               (EDITORIAL_CHARTER.md).

VERDICT: BLOCKED if any CRITICAL; else NEEDS-REVISION if any DESTRUCTIVE;
else PASS (DISTRACTING and REVIEW items are still listed).

SCOPE LIMITS (be honest about these): this cannot judge continuity, timeline
math, voice, canon, or plot. Those stay the strict sequential human read in
EDITORIAL_CHARTER.md. It also does not run grammar (LanguageTool) yet.

FROZEN BOOKS: published books are protected. Any path containing a frozen
marker is refused (exit code 3) before a single file is read. Extra markers
can be added with --frozen. Source of truth for which books are frozen:
novels/FROZEN_DO_NOT_EDIT.md.

NOTE: the report never contains the literal token used by proofread.yml's
grep to fail a run, so running this next to that workflow cannot trip it.

Usage:
    python scripts/proofread_core.py --chapters novels/<book>/chapters
    python scripts/proofread_core.py --chapters DIR --min-words 2300 --max-words 2700
    python scripts/proofread_core.py --chapters DIR --allow-emdash

Exit codes: 0 PASS, 1 NEEDS-REVISION, 2 BLOCKED, 3 REFUSED (frozen), 4 no files.
"""
import argparse
import glob
import os
import re
import sys
from collections import Counter
from dataclasses import dataclass

CRITICAL = "CRITICAL"
DESTRUCTIVE = "DESTRUCTIVE"
DISTRACTING = "DISTRACTING"
REVIEW = "REVIEW"
TIER_ORDER = (CRITICAL, DESTRUCTIVE, DISTRACTING, REVIEW)

FROZEN_MARKERS = ("amity-falls", "where-the-frost-doesnt-reach", "kindling-line")

EXIT_PASS, EXIT_REVISE, EXIT_BLOCKED, EXIT_REFUSED, EXIT_NOFILES = 0, 1, 2, 3, 4


@dataclass
class Finding:
    tier: str
    rule: str
    path: str
    line: int
    quote: str
    note: str


@dataclass
class Options:
    allow_emdash: bool = False
    min_words: int = None
    max_words: int = None


# ---------------------------------------------------------------- frozen guard
def refuse_if_frozen(paths, extra_markers=()):
    """Returns the frozen marker found in any path, or None. Case-insensitive,
    checks the absolute path so a symlink-free relative path cannot dodge it."""
    markers = tuple(FROZEN_MARKERS) + tuple(m.lower() for m in extra_markers if m)
    for p in paths:
        if not p:
            continue
        norm = os.path.abspath(p).replace("\\", "/").lower()
        for marker in markers:
            if marker in norm:
                return marker
    return None


# ------------------------------------------------------------------ line rules
_SPEECH = (r"said|asked|replied|whispered|muttered|called|answered|shouted|"
           r"added|says|murmured|demanded|snapped|breathed")

LINE_RULES = [
    ("K01", CRITICAL, re.compile("\u00ad"),
     "Soft hyphen (U+00AD). KDP lists these as typos. Remove it."),
    ("K02", CRITICAL, re.compile("[\u200b\u200c\u200d\u2060\ufeff\u2028\u2029\ufffd]"),
     "Zero-width, BOM, line-separator or replacement character. Remove it."),
    ("K03", CRITICAL, re.compile(r"\b[A-Za-z]+\d+[A-Za-z]+\b"),
     "Digit inside a word (numbers in place of letters)."),
    ("K04", CRITICAL,
     re.compile(r"<[A-Za-z/][^>\n]*>|`|\b(?:TODO|TBD|FIXME|lorem ipsum)\b|"
                r"\[INSERT[^\]\n]*\]|\bXXX+\b", re.I),
     "Leaked markup, backtick or placeholder text."),
    ("K05", CRITICAL,
     re.compile(r"\bas an ai\b|\blanguage model\b|\bhere is the (?:revised|rewritten) chapter\b", re.I),
     "AI meta-leak in the prose."),
    ("K06", CRITICAL, re.compile(r"^\s*\d{1,4}\s*$"),
     "Line that is only a number: looks like in-line page numbering."),
    ("D03", DESTRUCTIVE, re.compile(r",,|;;|::|(?<!\.)\.\.(?!\.)"),
     "Repeated or doubled punctuation."),
    ("D04", DESTRUCTIVE, re.compile("\u2014|(?<=\\s)\u2013(?=\\s)|(?<!-)--(?!-)"),
     "House rule: no em dashes (or dash stand-ins) in the prose."),
    ("X01", DISTRACTING, re.compile(r"!!|\?\?"),
     "Doubled ! or ? (style call; usually trim to one)."),
    ("X02", DISTRACTING,
     re.compile(r"(?<=[A-Za-z0-9]) +(?:[,;:!?]|\.(?!\.))(?=\s|$)"),
     "Space before closing punctuation."),
    ("X03", DISTRACTING,
     re.compile(r"(?<=[a-z]{2})[,;:](?=[A-Za-z])|(?<=[a-z]{2})\.(?=[A-Z][a-z])"),
     "Missing space after punctuation."),
    ("X04", DISTRACTING, re.compile(r"(?<=\S)  +(?=\S)"),
     "Double or multiple spaces."),
    ("X05", DISTRACTING,
     re.compile(r"[.][\"\u201d]\s+(?:he|she|they|I|we|it)\s+(?:" + _SPEECH + r")\b"),
     "Period before a dialogue tag; Chicago wants a comma inside the quote."),
]

# --------------------------------------------------------------- US spelling
_ISE = r"(?:e|es|ed|ing|ation|ations)"
_STD = r"(?:s|ed|ing|er|ers|ful|less|ite|ites|able|ably)?"
BRITISH_SPELLING = [
    ("colour", "color", _STD), ("favour", "favor", _STD), ("honour", "honor", _STD),
    ("neighbour", "neighbor", _STD), ("behaviour", "behavior", _STD),
    ("humour", "humor", _STD), ("labour", "labor", _STD), ("rumour", "rumor", _STD),
    ("savour", "savor", _STD), ("harbour", "harbor", _STD), ("flavour", "flavor", _STD),
    ("vapour", "vapor", _STD), ("splendour", "splendor", _STD),
    ("realis", "realiz", _ISE), ("organis", "organiz", _ISE),
    ("recognis", "recogniz", _ISE), ("apologis", "apologiz", _ISE),
    ("emphasis", "emphasiz", r"(?:e|es|ed|ing)"), ("criticis", "criticiz", _ISE),
    ("analys", "analyz", r"(?:e|es|ed|ing)"), ("centre", "center", r"(?:s|d)?"),
    ("theatre", "theater", r"s?"), ("fibre", "fiber", r"s?"), ("litre", "liter", r"s?"),
    ("defence", "defense", r"s?"), ("offence", "offense", r"s?"),
    ("pretence", "pretense", r"s?"), ("travell", "travel", r"(?:ed|ing|er|ers)"),
    ("jewellery", "jewelry", ""), ("cosy", "cozy", ""), ("tyre", "tire", r"s?"),
    ("kerb", "curb", r"s?"), ("plough", "plow", r"(?:s|ed|ing)?"),
    ("mould", "mold", r"(?:s|ed|ing|y)?"), ("moustache", "mustache", r"s?"),
    ("pyjamas", "pajamas", ""), ("ageing", "aging", ""), ("sceptic", "skeptic", r"(?:s|al)?"),
    ("grey", "gray", r"(?:s|ed|ing|er|est|ish)?"),
]
_BRIT_RES = [
    (re.compile(r"\b" + b + suffix + r"\b", re.I), b, a)
    for b, a, suffix in BRITISH_SPELLING
]

BRITISHISMS = [
    "whilst", "amongst", "learnt", "dreamt", "lorry", "petrol", "fortnight",
    "mum", "mummy", "arse",
]
_BRITISHISM_RE = re.compile(r"\b(?:" + "|".join(BRITISHISMS) + r")\b", re.I)

_DOUBLE_OK = {"had", "that", "no", "so", "very", "ha", "bye"}
_DOUBLED_RE = re.compile(r"\b([A-Za-z]+)\s+\1\b", re.I)

_A_BEFORE_VOWEL = re.compile(r"\ba\s+([aeiouAEIOU][A-Za-z]*)\b")
_A_VOWEL_OK_PREFIX = ("u", "eu", "one", "once", "ewe")
_AN_BEFORE_CONS = re.compile(r"\ban\s+([bcdfgjklmnpqrstvwxyzBCDFGJKLMNPQRSTVWXYZ][a-z]*)\b")


def _blank_comments(text):
    """Blank HTML comments (e.g. chapter_date headers) but keep line numbers."""
    return re.sub(r"<!--.*?-->", lambda m: re.sub(r"[^\n]", " ", m.group(0)),
                  text, flags=re.S)


def _snippet(line, start, end):
    return line[max(0, start - 25):end + 25].strip()


def word_count(text):
    return len(_blank_comments(text).split())


# ------------------------------------------------------------------- checkers
def check_text(text, path="<text>", opts=None):
    opts = opts or Options()
    findings = []
    cleaned = _blank_comments(text)
    lines = cleaned.split("\n")

    def add(tier, rule, line_no, quote, note):
        findings.append(Finding(tier, rule, path, line_no, quote, note))

    for i, line in enumerate(lines, 1):
        stripped = line.strip()
        if stripped in ("---", "***", "* * *"):
            continue
        for rule, tier, rx, note in LINE_RULES:
            if rule == "D04" and opts.allow_emdash:
                continue
            for m in rx.finditer(line):
                add(tier, rule, i, _snippet(line, m.start(), m.end()), note)
        for m in _DOUBLED_RE.finditer(line):
            if m.group(1).lower() in _DOUBLE_OK:
                continue
            add(DESTRUCTIVE, "D01", i, _snippet(line, m.start(), m.end()),
                "Doubled word.")
        for rx, brit, amer in _BRIT_RES:
            for m in rx.finditer(line):
                add(DISTRACTING, "S01", i, _snippet(line, m.start(), m.end()),
                    f"British spelling ('{brit}...'); US-first book, use '{amer}...'. "
                    "KDP does not count this as an error, so keep one style per book.")
        for m in _BRITISHISM_RE.finditer(line):
            add(REVIEW, "S02", i, _snippet(line, m.start(), m.end()),
                "Britishism; check it suits a US-first, universal-appeal book.")
        for m in _A_BEFORE_VOWEL.finditer(line):
            word = m.group(1).lower()
            if not word.startswith(_A_VOWEL_OK_PREFIX):
                add(DISTRACTING, "X06", i, _snippet(line, m.start(), m.end()),
                    "'a' before a vowel sound; should be 'an'.")
        for m in _AN_BEFORE_CONS.finditer(line):
            add(DISTRACTING, "X07", i, _snippet(line, m.start(), m.end()),
                "'an' before a consonant sound; should be 'a'.")

    # chapter-level checks -----------------------------------------------
    body = cleaned
    words = len(body.split())
    if words < 50:
        add(CRITICAL, "K07", 1, "", f"Chapter is empty or nearly empty ({words} words).")
    sample = body.strip()[:200].replace("\n", "")
    if len(sample) > 60 and re.fullmatch(r"[A-Za-z0-9+/=]+", sample):
        add(CRITICAL, "K08", 1, sample[:40],
            "File looks base64-encoded, not prose.")

    straight = body.count('"')
    if straight % 2 == 1:
        add(DESTRUCTIVE, "D02", 1, "",
            f"Odd number of straight double quotes ({straight}): one is unclosed.")
    opens, closes = body.count("\u201c"), body.count("\u201d")
    if opens != closes:
        add(DESTRUCTIVE, "D02", 1, "",
            f"Curly quotes unbalanced ({opens} open, {closes} close).")
    if straight and (opens or closes):
        add(DISTRACTING, "X08", 1, "",
            "Mixed straight and curly double quotes in one chapter.")

    if "\u2026" in body and "..." in body:
        first = next((i for i, l in enumerate(lines, 1) if "\u2026" in l), 1)
        add(DISTRACTING, "X09", first, "",
            "Mixed ellipsis styles (character and three periods); pick one.")

    if opts.min_words is not None and words < opts.min_words:
        add(REVIEW, "W01", 1, "",
            f"{words} words, under the {opts.min_words} floor. Review only; "
            "do not pad (EDITORIAL_CHARTER.md).")
    if opts.max_words is not None and words > opts.max_words:
        add(REVIEW, "W02", 1, "",
            f"{words} words, over the {opts.max_words} ceiling.")
    return findings


def verdict(findings):
    tiers = {f.tier for f in findings}
    if CRITICAL in tiers:
        return "BLOCKED"
    if DESTRUCTIVE in tiers:
        return "NEEDS-REVISION"
    return "PASS"


def list_chapter_files(chapters_dir):
    files = sorted(glob.glob(os.path.join(chapters_dir, "chapter_*.md")))
    if not files:
        files = sorted(glob.glob(os.path.join(chapters_dir, "*.md")))
    return files


def check_book(files, opts=None):
    findings = []
    counts = {}
    for path in files:
        with open(path, encoding="utf-8", errors="replace") as fh:
            text = fh.read()
        counts[path] = word_count(text)
        findings += check_text(text, path, opts)
    return findings, counts


def build_report(findings, counts, book_label):
    v = verdict(findings)
    by_tier = Counter(f.tier for f in findings)
    by_rule = Counter((f.tier, f.rule) for f in findings)
    out = [f"# Proofread Core Report: {book_label}", "",
           f"**Verdict: {v}**  ", f"Chapters read: {len(counts)}  ",
           f"Total words: {sum(counts.values())}", "",
           "Mechanical checks only. Continuity, timeline, voice and canon still "
           "need the sequential human read (EDITORIAL_CHARTER.md).", "",
           "## Counts", ""]
    for tier in TIER_ORDER:
        out.append(f"- {tier}: {by_tier.get(tier, 0)}")
    out += ["", "## By rule", ""]
    for (tier, rule), n in sorted(by_rule.items(),
                                  key=lambda kv: (TIER_ORDER.index(kv[0][0]), kv[0][1])):
        out.append(f"- {tier} {rule}: {n}")
    for tier in TIER_ORDER:
        items = [f for f in findings if f.tier == tier]
        if not items:
            continue
        cap = None if tier in (CRITICAL, DESTRUCTIVE) else 50
        out += ["", f"## {tier} ({len(items)})", ""]
        for f in (items if cap is None else items[:cap]):
            where = f"{os.path.basename(f.path)}:{f.line}"
            q = f" | `{f.quote}`" if f.quote else ""
            out.append(f"- {where} [{f.rule}] {f.note}{q}")
        if cap is not None and len(items) > cap:
            out.append(f"- ... and {len(items) - cap} more {tier} items (rerun to list all).")
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Read-only mechanical proofreading.")
    ap.add_argument("--chapters", required=True, help="folder of chapter .md files")
    ap.add_argument("--report", default="PROOFREAD_CORE_REPORT.md")
    ap.add_argument("--min-words", type=int, default=None)
    ap.add_argument("--max-words", type=int, default=None)
    ap.add_argument("--allow-emdash", action="store_true",
                    help="skip the house no-em-dash rule")
    ap.add_argument("--frozen", action="append", default=[],
                    help="extra frozen marker (folder-name fragment); repeatable")
    args = ap.parse_args(argv)

    hit = refuse_if_frozen([args.chapters], args.frozen)
    if hit:
        print(f"REFUSED: '{args.chapters}' matches frozen marker '{hit}'. "
              "Published books are never scanned. See novels/FROZEN_DO_NOT_EDIT.md.",
              file=sys.stderr)
        return EXIT_REFUSED

    files = list_chapter_files(args.chapters)
    if not files:
        print(f"No chapter .md files under {args.chapters}", file=sys.stderr)
        return EXIT_NOFILES

    opts = Options(allow_emdash=args.allow_emdash, min_words=args.min_words,
                   max_words=args.max_words)
    findings, counts = check_book(files, opts)
    report = build_report(findings, counts, os.path.basename(
        os.path.normpath(os.path.dirname(os.path.abspath(files[0])))))
    with open(args.report, "w", encoding="utf-8") as fh:
        fh.write(report)
    print(report)
    print(f"Report written to {args.report}")
    return {"PASS": EXIT_PASS, "NEEDS-REVISION": EXIT_REVISE,
            "BLOCKED": EXIT_BLOCKED}[verdict(findings)]


if __name__ == "__main__":
    sys.exit(main())
