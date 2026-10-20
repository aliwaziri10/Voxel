#!/usr/bin/env python3
"""
languagetool_pass.py - read-only LanguageTool grammar pass for NEW Voxel
novels. Added 2026-10-20 (see PROOFREAD_UPGRADE_HANDOFF.md, PROOFREAD_RULES.md).

WHAT IT IS
Runs LanguageTool (en-US) over each chapter ONCE and reuses the answer from a
per-chapter cache while the chapter text is unchanged (sha256 of the text plus
this script's settings). It sits next to scripts/proofread_core.py, reuses its
Finding, tiers, report and frozen-book guard, and never writes to a chapter
file: it only reads chapters and writes a report (and the cache file).

TIERS: LanguageTool is a statistical helper, and fiction (dialogue, fragments,
invented names) produces false positives. So nothing here is ever CRITICAL or
DESTRUCTIVE and this pass can never block or fail a book on its own:
  L01 DISTRACTING  possible misspelling (invented character names filtered out)
  L02 DISTRACTING  grammar, confused word, casing or punctuation
  L03 REVIEW       anything else it reports (never auto-fixed)
A person decides each one (rule 6: counted, then judged in context). Style,
wordiness, redundancy and typography categories are dropped on purpose.

TUNING (2026-10-20, v2): every comma rule is switched off (comma before
"and"/"so", comma after "Instead" and the like were pure noise in fiction),
the report lists EVERY finding (no 50-item cap), and a book-level
ignore_words.txt (next to the chapters folder) is picked up automatically.

NEEDS Java 17+ and the language_tool_python package (pip install
language_tool_python). GitHub's ubuntu runners already have Java. Without
them the script stops with a clear message; it does not guess.

Usage:
    python scripts/languagetool_pass.py --chapters novels/<new-book>/chapters
    python scripts/languagetool_pass.py --chapters DIR --server http://localhost:8081
    python scripts/languagetool_pass.py --chapters DIR --no-cache
Exit codes: 0 PASS, 1 NEEDS-REVISION, 2 BLOCKED, 3 REFUSED (frozen), 4 no files,
5 LanguageTool unavailable. (This pass alone only ever returns 0, 3, 4 or 5.)
"""
import argparse
import hashlib
import json
import os
import re
import sys
from collections import Counter

import proofread_core as pc

EXIT_NO_LT = 5
CONFIG_VERSION = 2
LANGUAGE = "en-US"

# Categories we keep. Everything else (STYLE, REDUNDANCY, PLAIN_ENGLISH,
# WORDINESS, COLLOQUIALISMS, TYPOGRAPHY, ...) is noise for fiction.
KEEP_CATEGORIES = {"TYPOS", "GRAMMAR", "CONFUSED_WORDS", "CASING", "PUNCTUATION",
                   "SEMANTICS", "MISC", "NONSTANDARD_PHRASES", "COMPOUNDING"}
GRAMMAR_CATEGORIES = {"GRAMMAR", "CONFUSED_WORDS", "CASING", "PUNCTUATION"}
# Rules switched off: proofread_core already covers them better.
DISABLED_RULES = {"WHITESPACE_RULE", "EN_QUOTES", "EN_UNPAIRED_QUOTES",
                  "EN_UNPAIRED_BRACKETS", "COMMA_PARENTHESIS_WHITESPACE",
                  "DOUBLE_PUNCTUATION", "ELLIPSIS", "EN_A_VS_AN", "ENGLISH_WORD_REPEAT_RULE"}
# Any rule whose id contains one of these fragments is switched off (comma
# rules, e.g. COMMA_COMPOUND_SENTENCE, COMMA_AFTER_INTRODUCTORY_PHRASE).
DISABLED_RULE_FRAGMENTS = ("COMMA", "INSTEAD")

pc.RULE_PARAM.update({"L01": 4, "L02": 5, "L03": 5})


def settings_fingerprint():
    blob = json.dumps([CONFIG_VERSION, LANGUAGE, sorted(KEEP_CATEGORIES),
                       sorted(DISABLED_RULES), list(DISABLED_RULE_FRAGMENTS)])
    return hashlib.sha256(blob.encode()).hexdigest()[:12]


def text_for_checking(text):
    """Blank out markdown headings but keep every newline, so offsets still
    map to the same line numbers in the real chapter file."""
    return "\n".join("" if ln.lstrip().startswith("#") else ln
                     for ln in text.split("\n"))


def chapter_hash(text):
    h = hashlib.sha256()
    h.update(settings_fingerprint().encode())
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def load_cache(path):
    try:
        with open(path, encoding="utf-8") as fh:
            data = json.load(fh)
        if data.get("version") == CONFIG_VERSION:
            return data
    except (OSError, ValueError):
        pass
    return {"version": CONFIG_VERSION, "entries": {}}


def save_cache(path, cache):
    d = os.path.dirname(path)
    if d:
        os.makedirs(d, exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(cache, fh, indent=1, sort_keys=True)


def _first(obj, *names, default=None):
    for n in names:
        v = getattr(obj, n, None)
        if v is not None:
            return v
    return default


def adapt_match(m):
    """Turn a language_tool_python Match (any version) into a plain dict."""
    if isinstance(m, dict):
        return m
    return {
        "rule_id": _first(m, "ruleId", "rule_id", default=""),
        "category": str(_first(m, "category", default="")).upper(),
        "issue_type": str(_first(m, "ruleIssueType", "rule_issue_type", default="")),
        "message": _first(m, "message", default=""),
        "offset": int(_first(m, "offset", default=0)),
        "length": int(_first(m, "errorLength", "error_length", default=0)),
        "replacements": list(_first(m, "replacements", default=[]))[:3],
    }


def keep_match(m):
    rid = str(m.get("rule_id") or "").upper()
    if any(frag in rid for frag in DISABLED_RULE_FRAGMENTS):
        return False
    return (m.get("category") in KEEP_CATEGORIES
            and m.get("rule_id") not in DISABLED_RULES)


def make_backend(server=None):
    """Returns (check_fn, close_fn). check_fn(text) -> list of match dicts."""
    try:
        import language_tool_python as ltp
    except ImportError:
        raise RuntimeError("language_tool_python is not installed "
                           "(pip install language_tool_python)")
    try:
        tool = ltp.LanguageTool(LANGUAGE, remote_server=server) if server \
            else ltp.LanguageTool(LANGUAGE)
    except Exception as e:  # Java missing, download blocked, server down
        raise RuntimeError(f"could not start LanguageTool: {e}")
    return (lambda text: [adapt_match(m) for m in tool.check(text)]), tool.close


def book_names(texts):
    """Capitalized words that never appear lowercase and occur 3+ times are
    almost certainly invented names; spelling flags on them are noise."""
    caps, lower = Counter(), set()
    for t in texts:
        for w in re.findall(r"\b[A-Za-z][a-z']+\b", t):
            if w[0].isupper():
                caps[w] += 1
            else:
                lower.add(w.lower())
    return {w for w, n in caps.items() if n >= 3 and w.lower() not in lower}


def line_of(text, offset):
    return text.count("\n", 0, max(offset, 0)) + 1


def classify(m):
    if m["category"] == "TYPOS":
        return pc.DISTRACTING, "L01"
    if m["category"] in GRAMMAR_CATEGORIES:
        return pc.DISTRACTING, "L02"
    return pc.REVIEW, "L03"


def run_book(files, check_fn, cache=None, ignore_words=(), stats=None):
    stats = stats if stats is not None else {"checked": 0, "cached": 0}
    texts, raw = {}, {}
    for path in files:
        with open(path, encoding="utf-8", errors="replace") as fh:
            texts[path] = fh.read()
    for path, text in texts.items():
        key = os.path.basename(path)
        h = chapter_hash(text)
        entry = cache["entries"].get(key) if cache is not None else None
        if entry and entry.get("hash") == h:
            raw[path] = entry["matches"]
            stats["cached"] += 1
            continue
        matches = [m for m in check_fn(text_for_checking(text)) if keep_match(m)]
        raw[path] = matches
        stats["checked"] += 1
        if cache is not None:
            cache["entries"][key] = {"hash": h, "matches": matches}
    names = book_names(texts.values()) | {w for w in ignore_words}
    findings, counts = [], {}
    for path, text in texts.items():
        counts[path] = pc.word_count(text)
        shown = text_for_checking(text)
        for m in raw[path]:
            if not keep_match(m):  # cached entries from older settings
                continue
            quote = shown[m["offset"]:m["offset"] + m["length"]]
            if m["category"] == "TYPOS" and quote.strip(".,;:!?'\u2019\"\u201c\u201d") in names:
                continue
            tier, rule = classify(m)
            sug = " / ".join(m.get("replacements") or [])
            note = m.get("message", "").strip() + (f" Suggest: {sug}." if sug else "")
            findings.append(pc.Finding(tier, rule, path, line_of(shown, m["offset"]),
                                       quote, note))
    return findings, counts, stats


def full_report(findings, counts, label):
    """pc.build_report caps DISTRACTING and REVIEW at 50 items. This keeps its
    header and counts, then lists EVERY finding in those tiers."""
    base = pc.build_report(findings, counts, label)
    cut = [base.find(f"\n## {t} (") for t in (pc.DISTRACTING, pc.REVIEW)]
    cut = [c for c in cut if c != -1]
    head = base[:min(cut)] if cut else base.rstrip("\n")
    out = [head]
    for tier in (pc.DISTRACTING, pc.REVIEW):
        items = [f for f in findings if f.tier == tier]
        if not items:
            continue
        out += ["", f"## {tier} ({len(items)})", ""]
        for f in items:
            where = f"{os.path.basename(f.path)}:{f.line}"
            q = f" | `{f.quote}`" if f.quote else ""
            out.append(f"- {where} [{f.rule}] {f.note}{q}")
    return "\n".join(out) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description="Read-only LanguageTool pass.")
    ap.add_argument("--chapters", required=True)
    ap.add_argument("--report", default="LANGUAGETOOL_REPORT.md")
    ap.add_argument("--cache", default=None,
                    help="cache file (default .lt_cache/<book>.json)")
    ap.add_argument("--no-cache", action="store_true")
    ap.add_argument("--server", default=None, help="URL of a running LanguageTool server")
    ap.add_argument("--ignore-words", default=None,
                    help="text file, one word per line, never flagged as misspelled "
                         "(default: ignore_words.txt next to the chapters folder)")
    ap.add_argument("--frozen", action="append", default=[])
    args = ap.parse_args(argv)

    hit = pc.refuse_if_frozen([args.chapters], args.frozen)
    if hit:
        print(f"REFUSED: '{args.chapters}' matches frozen marker '{hit}'. "
              "Published books are never scanned. See novels/FROZEN_DO_NOT_EDIT.md.",
              file=sys.stderr)
        return pc.EXIT_REFUSED
    files = pc.list_chapter_files(args.chapters)
    if not files:
        print(f"No chapter .md files under {args.chapters}", file=sys.stderr)
        return pc.EXIT_NOFILES
    try:
        check_fn, close_fn = make_backend(args.server)
    except RuntimeError as e:
        print(f"LanguageTool unavailable: {e}", file=sys.stderr)
        return EXIT_NO_LT

    book_dir = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(files[0]))))
    cache_path = args.cache or os.path.join(".lt_cache", f"{book_dir}.json")
    cache = None if args.no_cache else load_cache(cache_path)
    ignore_path = args.ignore_words or os.path.join(
        os.path.dirname(os.path.abspath(files[0])), "..", "ignore_words.txt")
    ignore = []
    if os.path.exists(ignore_path):
        with open(ignore_path, encoding="utf-8") as fh:
            ignore = [ln.strip() for ln in fh if ln.strip()]
    try:
        findings, counts, stats = run_book(files, check_fn, cache, ignore)
    finally:
        close_fn()
    if cache is not None:
        save_cache(cache_path, cache)

    report = full_report(findings, counts, f"{book_dir} (LanguageTool grammar pass)")
    report = report.replace(
        "Mechanical checks only.",
        f"LanguageTool {LANGUAGE} pass: {stats['checked']} chapter(s) checked, "
        f"{stats['cached']} reused from cache. Comma rules off; every finding listed. "
        "Findings are suggestions for a person to judge; this pass never blocks a "
        "book. Mechanical checks only.", 1)
    with open(args.report, "w", encoding="utf-8") as fh:
        fh.write(report)
    print(report)
    print(f"Report written to {args.report}")
    return pc.EXIT_PASS  # this pass only advises; it never blocks a book


if __name__ == "__main__":
    sys.exit(main())
