#!/usr/bin/env python3
"""
manuscript_qa.py — Full QA pass for a Voxel novel manuscript.

Runs against raw chapter markdown AND (if given) the final built .docx,
so bugs introduced at build time (asterisk-italics, escaping) get caught,
not just source-stage issues.

Usage:
    python manuscript_qa.py --chapters chapters/ [--docx manuscript.docx] [--report report.md]

Checks:
  1. Em dash count (must be 0, excluding intentional "---" scene breaks)
  2. Doubled words ("the the")
  3. AI-tell / series-fingerprint phrase frequency
  4. Structural uniformity (repeated chapter-opening pattern)
  5. Spelling consistency (British/American mixing)
  6. Invisible/zero-width characters, BOM, curly-quote mismatches
  7. Double spaces
  8. Punctuation sanity (question mark vs period mismatch heuristic)
  9. Grammar/spelling via language_tool_python (en-US), with markdown-escape
     stripping and false-positive filtering
 10. [--docx only] Asterisk-instead-of-italics scan of word/document.xml
 11. [--docx only] Page count via LibreOffice->PDF->pdfinfo (if available)

Findings are split into CONFIRMED-FIX (safe to auto-apply / obviously wrong)
and YOUR-CALL (ambiguous, needs a human decision) per the pipeline spec.
"""
import argparse
import glob
import os
import re
import sys
import zipfile
import subprocess
import unicodedata
from collections import Counter, defaultdict

FINGERPRINT_PHRASES = [
    "the way", "the kind of", "found herself", "found himself",
    "close enough", "the shape of", "as though", "in a way that",
    "something like", "delve into", "tapestry", "bittersweet",
    "a testament to", "it's important to note", "in the world of",
]
BRITISH_AMERICAN_PAIRS = [
    ("grey", "gray"), ("colour", "color"), ("favourite", "favorite"),
    ("realise", "realize"), ("organise", "organize"), ("centre", "center"),
    ("theatre", "theater"), ("travelling", "traveling"), ("honour", "honor"),
    ("defence", "defense"), ("licence", "license"), ("analyse", "analyze"),
]
INVISIBLE_CHARS = {
    "\u200b": "ZERO WIDTH SPACE", "\u200c": "ZERO WIDTH NON-JOINER",
    "\u200d": "ZERO WIDTH JOINER", "\ufeff": "BOM", "\u00a0": "NBSP",
    "\u2028": "LINE SEPARATOR", "\u200e": "LRM", "\u200f": "RLM",
}


def read_chapters(chapters_dir):
    files = sorted(glob.glob(os.path.join(chapters_dir, "chapter_*.md")))
    if not files:
        files = sorted(glob.glob(os.path.join(chapters_dir, "*.md")))
    chapters = []
    for f in files:
        with open(f, encoding="utf-8", errors="replace") as fh:
            chapters.append((f, fh.read()))
    return chapters


def check_corrupted(chapters):
    findings = []
    for path, text in chapters:
        sample = text.strip()[:200]
        # base64 tell: long run of alnum+/= with no whitespace
        if len(sample) > 60 and re.fullmatch(r"[A-Za-z0-9+/=]+", sample.replace("\n", "")):
            findings.append(("CONFIRMED-FIX", path, "Chapter file looks base64-encoded, not prose — needs re-decoding."))
    return findings


def check_em_dash(chapters):
    findings = []
    for path, text in chapters:
        lines = text.split("\n")
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped == "---":
                continue
            count = line.count("—")
            if count:
                findings.append(("YOUR-CALL", f"{path}:{i}", f"Em dash found ({count}x): {stripped[:80]}"))
    return findings


def check_doubled_words(chapters):
    pattern = re.compile(r"\b(\w+)\s+\1\b", re.IGNORECASE)
    findings = []
    for path, text in chapters:
        for m in pattern.finditer(text):
            findings.append(("CONFIRMED-FIX", path, f"Doubled word: '{m.group(0)}'"))
    return findings


def check_fingerprint_phrases(chapters):
    total_words = 0
    counts = Counter()
    for _, text in chapters:
        total_words += len(text.split())
        low = text.lower()
        for phrase in FINGERPRINT_PHRASES:
            counts[phrase] += low.count(phrase)
    findings = []
    threshold = max(30, total_words // 800)  # scales with manuscript length
    for phrase, n in counts.items():
        if n > threshold:
            findings.append(("YOUR-CALL", "manuscript-wide", f"'{phrase}' appears {n}x (threshold {threshold}) — recommend varying language."))
    return findings


def check_structural_uniformity(chapters):
    openers = []
    for path, text in chapters:
        body = text.strip()
        first_para = body.split("\n\n", 1)[0]
        first_sentence = re.split(r"(?<=[.!?])\s", first_para, maxsplit=1)[0]
        openers.append((path, first_sentence))
    # crude signal: how many openers start with a long descriptive clause before any dialogue
    long_desc_starts = sum(1 for _, s in openers if len(s.split()) > 18 and '"' not in s)
    findings = []
    if openers and long_desc_starts / len(openers) > 0.6:
        findings.append(("YOUR-CALL", "manuscript-wide",
                          f"{long_desc_starts}/{len(openers)} chapters open with a long descriptive clause before dialogue/action — pattern may read as templated."))
    return findings


def check_spelling_consistency(chapters):
    full_text = "\n".join(t for _, t in chapters).lower()
    findings = []
    for brit, amer in BRITISH_AMERICAN_PAIRS:
        b, a = full_text.count(brit), full_text.count(amer)
        if b and a:
            findings.append(("CONFIRMED-FIX", "manuscript-wide", f"Mixed spelling: '{brit}' x{b} and '{amer}' x{a} — standardize to US ('{amer}')."))
        elif b and not a:
            findings.append(("CONFIRMED-FIX", "manuscript-wide", f"British spelling '{brit}' x{b} found, no US market override set — standardize to '{amer}'."))
    return findings


def check_invisible_chars(chapters):
    findings = []
    for path, text in chapters:
        for ch, name in INVISIBLE_CHARS.items():
            n = text.count(ch)
            if n:
                findings.append(("CONFIRMED-FIX", path, f"{n}x {name} character found — strip it."))
        if re.search(r"  +", text):
            n = len(re.findall(r"  +", text))
            findings.append(("CONFIRMED-FIX", path, f"{n} instance(s) of double/multi spaces."))
    return findings


def check_punctuation_sanity(chapters):
    findings = []
    dialogue_re = re.compile(r'"([^"]{3,200})"')
    question_words = ("who", "what", "when", "where", "why", "how", "isn't", "aren't", "didn't", "don't", "won't", "can't", "wouldn't", "couldn't")
    for path, text in chapters:
        for m in dialogue_re.finditer(text):
            line = m.group(1).strip()
            low = line.lower()
            starts_q = low.split(" ")[0] in question_words if low else False
            if starts_q and line.endswith("."):
                findings.append(("YOUR-CALL", path, f"Dialogue reads as a question but ends in a period: \"{line[:80]}\""))
    return findings


def strip_markdown_escaping(text):
    return text.replace("\\'", "'").replace('\\"', '"').replace("\\_", "_").replace("\\*", "*")


def check_grammar_languagetool(chapters):
    findings = []
    try:
        import language_tool_python
    except ImportError:
        findings.append(("YOUR-CALL", "setup", "language_tool_python not installed — run `pip install language_tool_python --break-system-packages` for grammar/spelling pass."))
        return findings
    try:
        tool = language_tool_python.LanguageTool("en-US")
    except Exception as e:
        findings.append(("YOUR-CALL", "setup", f"LanguageTool failed to start ({e}) — Java runtime may be missing."))
        return findings

    ignore_rules = {
        "EN_UNPAIRED_QUOTES", "EN_UNPAIRED_BRACKETS", "TYPOGRAPHY",
        "IN_THE_MOMENT", "QUIET_QUITE", "COMMA_PARENTHESIS_WHITESPACE",
        "UPPERCASE_SENTENCE_START",  # dialogue tags often lowercase intentionally
    }
    keep_categories = {"MORFOLOGIK_RULE_EN_US", "TYPOS", "GRAMMAR", "COMPOUNDING"}

    for path, text in chapters:
        clean = strip_markdown_escaping(text)
        matches = tool.check(clean)
        for m in matches:
            if m.ruleId in ignore_rules:
                continue
            if m.ruleId not in keep_categories and m.category not in ("TYPOS", "GRAMMAR"):
                continue
            snippet = clean[max(0, m.offset - 20):m.offset + m.errorLength + 20].replace("\n", " ")
            severity = "CONFIRMED-FIX" if m.ruleId in ("MORFOLOGIK_RULE_EN_US", "TYPOS") else "YOUR-CALL"
            findings.append((severity, path, f"[{m.ruleId}] {m.message} — near: '...{snippet}...'"))
    return findings


def check_docx_asterisks(docx_path):
    findings = []
    if not docx_path or not os.path.exists(docx_path):
        return findings
    with zipfile.ZipFile(docx_path) as z:
        xml = z.read("word/document.xml").decode("utf-8", errors="replace")
    text_runs = re.findall(r"<w:t[^>]*>([^<]*)</w:t>", xml)
    for i, t in enumerate(text_runs):
        if "*" in t:
            findings.append(("YOUR-CALL", f"docx run #{i}", f"Literal asterisk found in text run — likely markdown emphasis leaked into docx: '{t.strip()[:80]}'"))
    return findings


def get_pdf_page_count(docx_path):
    if not docx_path or not os.path.exists(docx_path):
        return None
    outdir = "/tmp/mqa_pdf"
    os.makedirs(outdir, exist_ok=True)
    try:
        subprocess.run(
            ["libreoffice", "--headless", "--convert-to", "pdf", "--outdir", outdir, docx_path],
            check=True, capture_output=True, timeout=180,
        )
        pdf_path = os.path.join(outdir, os.path.splitext(os.path.basename(docx_path))[0] + ".pdf")
        result = subprocess.run(["pdfinfo", pdf_path], check=True, capture_output=True, text=True)
        for line in result.stdout.splitlines():
            if line.startswith("Pages:"):
                return int(line.split(":")[1].strip())
    except Exception as e:
        return f"error: {e}"
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--chapters", required=True)
    ap.add_argument("--docx", default=None)
    ap.add_argument("--report", default="qa_report.md")
    ap.add_argument("--skip-grammar", action="store_true", help="Skip LanguageTool pass (slow on first run — downloads ~200MB).")
    args = ap.parse_args()

    chapters = read_chapters(args.chapters)
    if not chapters:
        print(f"No chapter files found under {args.chapters}", file=sys.stderr)
        sys.exit(1)

    all_findings = []
    all_findings += check_corrupted(chapters)
    all_findings += check_em_dash(chapters)
    all_findings += check_doubled_words(chapters)
    all_findings += check_fingerprint_phrases(chapters)
    all_findings += check_structural_uniformity(chapters)
    all_findings += check_spelling_consistency(chapters)
    all_findings += check_invisible_chars(chapters)
    all_findings += check_punctuation_sanity(chapters)
    if not args.skip_grammar:
        all_findings += check_grammar_languagetool(chapters)
    if args.docx:
        all_findings += check_docx_asterisks(args.docx)
        pages = get_pdf_page_count(args.docx)
        if pages is not None:
            all_findings.append(("INFO", "page-count", f"PDF page count at final trim: {pages}"))

    by_severity = defaultdict(list)
    for sev, loc, msg in all_findings:
        by_severity[sev].append((loc, msg))

    lines = ["# Manuscript QA Report\n"]
    for sev in ("CONFIRMED-FIX", "YOUR-CALL", "INFO"):
        items = by_severity.get(sev, [])
        lines.append(f"\n## {sev} ({len(items)})\n")
        for loc, msg in items:
            lines.append(f"- **{loc}**: {msg}")
    total_words = sum(len(t.split()) for _, t in chapters)
    lines.append(f"\n---\nTotal words: {total_words} across {len(chapters)} chapter files.\n")

    report = "\n".join(lines)
    with open(args.report, "w", encoding="utf-8") as f:
        f.write(report)
    print(report)
    print(f"\nReport written to {args.report}")


if __name__ == "__main__":
    main()
