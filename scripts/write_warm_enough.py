#!/usr/bin/env python3
"""
write_warm_enough.py - strict, chapter-by-chapter writer and auditor for Warm Enough
(Larkmere, Book Two).

Per chapter the model receives: WRITER_COMMAND.md (system), CANON_LOCK.md,
HUMAN_WRITING.md, VOICE_GUIDE.md, that chapter's HEAT line and brief, the real text of
the previous chapter and a short voice sample from the earlier chapter of the same
point of view. Nothing else.

HARD failures are never saved (invented name, banned word or name, digit, month or
weekday, em dash, planning word, a locked line in the wrong chapter or missing from
its chapter, boyhood leak before chapter 30, a character outside their allowed
chapters, cut-off or far too short chapter). SOFT findings (style words, word range)
are retried; if only soft findings remain after the last try, the chapter is saved and
listed in the report.

Strict order: chapter N is only written if chapter N-1 exists. Existing chapters are
kept unless --force. With --checkpoint each chapter is committed and pushed as it is
written. With --auto the run starts at the first missing chapter; if all 40 exist it
runs the audit and exits.

Usage:
  python scripts/write_warm_enough.py --auto --checkpoint
  python scripts/write_warm_enough.py --start 1 --end 1 --dry-run
  python scripts/write_warm_enough.py --check novels/warm-enough/chapters/chapter_01.md --chapter 1
  python scripts/write_warm_enough.py --audit
"""
import argparse
import re
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BOOK = ROOT / "novels" / "warm-enough"
TOTAL = 40
MIN_HARD_WORDS = 1800
MIN_WORDS, MAX_WORDS = 2300, 2700
SINGLE_CALL = False

ALLOWED = set("""
Hester Tansley Ansel Brandt Winifred Gran Tilda Brook Mina Cray Dunstan Rudd Piers Ellory
Ostler Larkmere Water Spindle Lane House Kettle Room Ice Road Net Sheds High Fold Heron
Grey Blue Green Polite Knit Knits Open Door Onion Longnight Breaking Winter Knitter Tin
""".split())

BANNED_NAMES = "Wren Pell Bram Hale Oakes Corrin Voss Marius Mara Renn".split()

# first and last chapter in which a named character may appear at all
CHAR_RANGES = {
    "Piers": (17, 40), "Ellory": (17, 40),
    "Dunstan": (24, 28), "Rudd": (24, 28),
    "Ostler": (28, 30),
    "Mina": (6, 40), "Cray": (6, 40),
    "Tilda": (3, 40), "Brook": (3, 40),
}

# marker (lower case, straight apostrophes) -> chapters where it must appear and may appear
LOCKED = {
    "leave one door open": {6, 32},
    "stop being fine at me": {10},
    "i came for the winter i was warm": {31},
    "i've been cold since the ferry": {33},
    "i am staying": {33},
    "everything i make warm, i lose": {35},
    "i'm not a map": {35},
    "you have been polite for nine winters": {28},
    "that warm and owe nothing": {23},
}

STYLE_PATTERNS = [
    r"\bparticular\b", r"\bsome\b", r"\bsomething\b", r"\bsomeone\b", r"\bsomewhere\b",
    r"\bsomebody\b", r"\bsomehow\b", r"\bkind of\b", r"\bthe specific\b",
    r"\btestament to\b", r"\btapestry\b", r"\bunwavering\b", r"\bseamless",
]
PLANNING = r"\b(chapter|beat|protagonist|sub-beat|touch level|canon)\b"
MONTHS = r"\b(January|February|March|April|June|July|August|September|October|November|December)\b"
WEEKDAYS = r"\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b"
BOYHOOD = r"\bboyhood\b|\bas a boy\b|\bwhen he was a boy\b|\bthe girl on the quay\b"
EXPLICIT = r"\b(penis|cock|clit|clitoris|vagina|cum|orgasm|erection|nipples?)\b"


def words(text):
    return len(text.split())


def read(p):
    return Path(p).read_text(encoding="utf-8")


def norm(text):
    return text.replace("\u2019", "'").replace("\u2018", "'").lower()


def chapter_path(n):
    return BOOK / "chapters" / ("chapter_%02d.md" % n)


def clean_body(text):
    text = text.strip()
    text = re.sub(r"^```[a-z]*\n|\n```$", "", text)
    text = re.sub(r"^<!--.*?-->\s*", "", text, flags=re.S)
    text = re.sub(r"^(#+\s*)?(Chapter\s+\w+[^\n]*)\n+", "", text)
    return text.strip()


# ---------- plan files ----------

def load_brief(n):
    p = BOOK / "briefs" / ("ch%02d.md" % n)
    if not p.exists():
        raise SystemExit("STOP: brief for chapter %d is missing." % n)
    text = read(p)
    head = text.split("\n", 1)[0]
    m = re.match(r"# Brief (\d+) \| (Ansel|Hester) \| ([^|]+) \|", head)
    if not m or int(m.group(1)) != n:
        raise SystemExit("STOP: brief %d heading is not readable: %r" % (n, head))
    pov, season = m.group(2), m.group(3).strip()
    if (pov == "Ansel") != (n % 2 == 1):
        raise SystemExit("STOP: chapter %d heading says %s but odd chapters are Ansel and even are Hester." % (n, pov))
    return text, pov, season


def heat_line(n):
    p = BOOK / "canon" / "HEAT_LADDER.md"
    m = re.search(r"(?m)^%d: (.+)$" % n, read(p))
    return m.group(1).strip() if m else ""


def previous_text(n):
    if n == 1:
        return "(This is the opening chapter. Nothing has happened yet.)", "none"
    p = chapter_path(n - 1)
    if not p.exists():
        raise SystemExit("STOP: chapter %d does not exist yet. Chapters are written in strict order." % (n - 1))
    return clean_body(read(p)), "chapter %d" % (n - 1)


def voice_sample(n):
    if n >= 3 and chapter_path(n - 2).exists():
        return " ".join(clean_body(read(chapter_path(n - 2))).split()[:700])
    return "(No earlier chapter of this point of view yet. Use the voice guide.)"


def build_prompt(n, brief, pov, season, prev, prev_label, sample, next_head):
    parts = [
        "=== CANON LOCK (authority 1) ===\n" + read(BOOK / "canon" / "CANON_LOCK.md"),
        "=== HUMAN WRITING RULES ===\n" + read(ROOT / "novels" / "HUMAN_WRITING.md"),
        "=== VOICE GUIDE ===\n" + read(BOOK / "VOICE_GUIDE.md"),
        "=== HEAT TARGET FOR THIS CHAPTER (build the physical tension from this) ===\n" + heat_line(n),
        "=== BRIEF FOR CHAPTER %d (point of view: %s; season: %s) ===\n%s" % (n, pov, season, brief),
        "=== NEXT CHAPTER HEADING ONLY (do NOT cover it) ===\n" + (next_head or "(this is the last chapter)"),
        "=== REAL TEXT OF THE PREVIOUS CHAPTER (%s). It has already happened. Continue straight from it. ===\n%s" % (prev_label, prev),
        "=== VOICE SAMPLE (rhythm and tone only, never reuse events or lines) ===\n" + sample,
        "Write this chapter now, following every HARD RULE. Output only the chapter prose.",
    ]
    return "\n\n".join(parts)


# ---------- the model ----------

def call_model(system, user):
    import os
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    model = os.environ.get("OPENAI_MODEL", "").strip()
    if key and model:
        import requests
        r = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
            json={"model": model,
                  "messages": [{"role": "system", "content": system},
                               {"role": "user", "content": user}],
                  "max_completion_tokens": 9000},
            timeout=600)
        r.raise_for_status()
        choice = r.json()["choices"][0]
        if choice.get("finish_reason") == "length":
            raise RuntimeError("model reply was cut off at its length limit")
        return choice["message"]["content"]
    sys.path.insert(0, str(ROOT))
    import content_provider
    return content_provider.call_raw(system, user, timeout=300)


def call_chapter(system, user):
    """Two calls per chapter (first half, then second half from the real first half)."""
    if SINGLE_CALL:
        return call_model(system, user)
    first = clean_body(call_model(system, user + (
        "\n\nWRITE ONLY THE FIRST HALF OF THE CHAPTER NOW: about 1,300 words, from the opening "
        "to roughly the middle of the brief. Stop at a natural beat in the middle. Do NOT wrap up, "
        "do NOT write the chapter's ending, no title or heading line.")))
    second = clean_body(call_model(system, user + (
        "\n\nTHE FIRST HALF OF THIS CHAPTER IS ALREADY WRITTEN (below). Write ONLY THE SECOND HALF now: "
        "about 1,300 words, continuing exactly from its last line, through the rest of the brief to the "
        "closing image named in ENDS ON. Do not repeat, summarize or rewrite the first half. "
        "No title or heading line.\n\n=== FIRST HALF (already written) ===\n" + first)))
    return first + "\n\n" + second


# ---------- checks ----------

_COMMON = None


def common_lowercase():
    global _COMMON
    if _COMMON is None:
        cnt = Counter()
        files = sorted((ROOT / "novels").glob("*/chapters/*.md"))[:80]
        for p in files:
            try:
                cnt.update(re.findall(r"\b[a-z]{3,}\b", read(p)))
            except Exception:
                pass
        _COMMON = set(cnt)
    return _COMMON


def is_ordinary(tok, common):
    low = tok.lower()
    if low in common:
        return True
    for suf in ("s", "es", "ed", "d", "ing", "er", "ers", "ly"):
        if low.endswith(suf) and low[:-len(suf)] in common:
            return True
    if low.endswith("ies") and low[:-3] + "y" in common:
        return True
    return low.endswith(("body", "where", "selves", "self", "wire"))


def length_gap(text):
    n = words(text)
    if MIN_WORDS <= n <= MAX_WORDS:
        return 0
    return min(abs(n - MIN_WORDS), abs(n - MAX_WORDS))


def check(body, n, brief=None):
    """-> (hard_list, soft_list)"""
    hard, soft = [], []
    nw = words(body)
    if nw < MIN_HARD_WORDS:
        hard.append("only %d words (a chapter must reach about 2,300)" % nw)
    elif nw < MIN_WORDS or nw > MAX_WORDS:
        soft.append("%d words (target %d to %d)" % (nw, MIN_WORDS, MAX_WORDS))
    if body and body[-1] not in ".!?\"'\u201d\u2019*_)":
        hard.append("the chapter looks cut off (it ends with %r)" % body[-20:])
    if re.search(r"\d", body):
        hard.append("a digit appears in the prose (write every number as a word; no years, ages or dates)")
    m = re.search(MONTHS, body) or re.search(WEEKDAYS, body)
    if m:
        hard.append("a month or weekday name: %r" % m.group(0))
    if re.search(r"\bdays? later\b", body, re.I):
        hard.append("the phrase 'days later'")
    m = re.search(PLANNING, body, re.I)
    if m:
        hard.append("a planning word in the prose: %r" % m.group(0))
    if body.count("\u2014") + body.count("\u2013"):
        hard.append("em or en dashes are banned in this book (%d found)" % (body.count("\u2014") + body.count("\u2013")))
    if re.search(r"\bgray\b", body, re.I):
        hard.append("'gray' (this book uses 'grey')")
    if re.search(r"\[[^\]]{2,40}\]", body):
        hard.append("a bracket tag leaked into the prose")
    if re.search(EXPLICIT, body, re.I):
        hard.append("explicit anatomical or sexual word (closed door, sensual only)")
    for nm in BANNED_NAMES:
        if re.search(r"\b%s\b" % re.escape(nm), body):
            hard.append("banned name: %s" % nm)

    low = norm(body)
    for marker, chs in LOCKED.items():
        present = marker in low
        if present and n not in chs:
            hard.append("locked line used in the wrong chapter: %r (belongs to %s)" % (marker, sorted(chs)))
        if (not present) and n in chs:
            hard.append("locked line missing from this chapter: %r" % marker)
    if n < 30 and re.search(BOYHOOD, body, re.I):
        hard.append("a boyhood or quay-girl reference before the reveal")
    if n < 30 and re.search(r"\b(opened|open|lid of) the tin\b", body, re.I):
        hard.append("the tin is opened before it is revealed")
    for nm, (lo, hi) in CHAR_RANGES.items():
        if re.search(r"\b%s\b" % nm, body) and not (lo <= n <= hi):
            hard.append("%s appears in chapter %d (allowed only in chapters %d to %d)" % (nm, n, lo, hi))

    common = common_lowercase()
    seen = {}
    for mt in re.finditer(r"\b[A-Z][a-z]{2,}\b", body):
        tok = mt.group(0)
        if tok in ALLOWED or is_ordinary(tok, common):
            continue
        before = body[:mt.start()].rstrip(" \t\u201c\"'\u2018*_(")
        at_start = before == "" or before[-1] in ".!?:\n"
        if at_start and tok.lower().endswith(("ly", "ing", "ed", "ness", "ion", "ous", "ive", "ful", "less", "ment", "ity", "ward", "wards")):
            continue
        rec = seen.setdefault(tok, [0, 0, ""])
        rec[0] += 1
        if not at_start:
            rec[1] += 1
        if not rec[2]:
            rec[2] = body[max(0, mt.start() - 25):mt.end() + 25].replace("\n", " ")
    unknown = {t: r for t, r in seen.items() if r[1] >= 1 or r[0] >= 2}
    if unknown:
        items = sorted(unknown.items(), key=lambda kv: -kv[1][0])[:12]
        hard.append("names or capitalised words not on the cast: "
                    + "; ".join("%s (x%d, e.g. \"...%s...\")" % (t, r[0], r[2]) for t, r in items))

    if brief:
        pm = re.search(r"(?m)^PRESENT:(.*)$", brief)
        present = pm.group(1) if pm else ""
        for nm in ("Gran", "Tilda", "Mina", "Dunstan", "Piers", "Ostler"):
            if re.search(r"\b%s\b" % nm, body) and nm not in present:
                soft.append("%s is named but is not in this chapter's PRESENT line" % nm)

    style = Counter()
    for pat in STYLE_PATTERNS:
        for mm in re.finditer(pat, body, re.I):
            style[mm.group(0).lower()] += 1
    if style:
        soft.append("style words: " + ", ".join("%s x%d" % kv for kv in style.most_common()))
    return hard, soft


# ---------- audit ----------

def audit():
    lines = ["# Warm Enough: AUDIT REPORT", "", "Mechanical checks only. The human continuity, voice and canon read is still required.", ""]
    total_hard, total_words, missing = 0, 0, []
    for n in range(1, TOTAL + 1):
        p = chapter_path(n)
        if not p.exists():
            missing.append(n)
            continue
        body = clean_body(read(p))
        try:
            brief = load_brief(n)[0]
        except SystemExit:
            brief = None
        hard, soft = check(body, n, brief)
        total_hard += len(hard)
        total_words += words(body)
        status = "OK" if not hard else "HARD"
        lines.append("- chapter %d: %d words, %s%s" % (n, words(body), status,
                     (" | " + "; ".join(hard + soft)) if (hard or soft) else ""))
    lines += ["", "Chapters written: %d of %d. Total words: %d. Missing: %s." % (TOTAL - len(missing), TOTAL, total_words, missing or "none"),
              "Hard failures: %d." % total_hard]
    out = BOOK / "AUDIT_REPORT.md"
    out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    return out, total_hard, missing


# ---------- git ----------

def checkpoint(path, message):
    try:
        subprocess.run(["git", "add", str(path)], check=True)
        subprocess.run(["git", "commit", "-m", message], check=True)
        subprocess.run(["git", "pull", "--rebase", "-q"], check=False)
        subprocess.run(["git", "push", "-q"], check=True)
        print("[warm-enough]   committed and pushed: %s" % message)
    except subprocess.CalledProcessError as e:
        print("[warm-enough]   WARNING: commit or push failed (%s). The file is saved on the runner." % e)


# ---------- main ----------

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--start", type=int, default=1)
    ap.add_argument("--end", type=int, default=TOTAL)
    ap.add_argument("--auto", action="store_true", help="start at the first missing chapter")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--checkpoint", action="store_true")
    ap.add_argument("--max-tries", type=int, default=3)
    ap.add_argument("--single", action="store_true")
    ap.add_argument("--audit", action="store_true")
    ap.add_argument("--check", help="run the checks on one existing file and exit")
    ap.add_argument("--chapter", type=int, default=1, help="chapter number for --check")
    args = ap.parse_args()
    global SINGLE_CALL
    SINGLE_CALL = args.single

    if args.check:
        body = clean_body(read(args.check))
        brief = load_brief(args.chapter)[0]
        hard, soft = check(body, args.chapter, brief)
        print("words:", words(body))
        print("HARD:", hard or "none")
        print("SOFT:", soft or "none")
        return 0

    if args.audit:
        out, hard, missing = audit()
        if args.checkpoint:
            checkpoint(out, "Warm Enough: audit report")
        return 0

    system = read(BOOK / "WRITER_COMMAND.md")
    (BOOK / "chapters").mkdir(parents=True, exist_ok=True)

    start = args.start
    if args.auto:
        start = next((i for i in range(1, TOTAL + 1) if not (chapter_path(i).exists() and read(chapter_path(i)).strip())), None)
        if start is None:
            print("[warm-enough] all %d chapters exist. Running the audit." % TOTAL)
            out, hard, missing = audit()
            if args.checkpoint:
                checkpoint(out, "Warm Enough: audit report")
            return 0
        print("[warm-enough] auto mode: first missing chapter is %d" % start)

    report = []
    for n in range(start, args.end + 1):
        path = chapter_path(n)
        if path.exists() and read(path).strip() and not args.force:
            print("[warm-enough] chapter %d already exists, keeping it" % n)
            continue
        brief, pov, season = load_brief(n)
        try:
            next_head = read(BOOK / "briefs" / ("ch%02d.md" % (n + 1))).split("\n", 1)[0] if n < TOTAL else None
        except Exception:
            next_head = None
        prev, prev_label = previous_text(n)
        user = build_prompt(n, brief, pov, season, prev, prev_label, voice_sample(n), next_head)
        print("[warm-enough] chapter %d | %s | %s | prompt %d words" % (n, pov, season, words(system) + words(user)))
        if args.dry_run:
            print(user[:1500])
            print("... [dry run, no model call]")
            continue

        feedback, best, best_soft, hard = "", None, None, []
        for attempt in range(1, args.max_tries + 1):
            msg = user + (("\n\nYOUR PREVIOUS DRAFT WAS REJECTED. Write the whole chapter again from the start and fix exactly these problems:\n" + feedback) if feedback else "")
            try:
                raw = call_chapter(system, msg)
            except Exception as e:
                print("[warm-enough]   model call failed on try %d: %s" % (attempt, e))
                continue
            body = clean_body(raw)
            hard, soft = check(body, n, brief)
            print("[warm-enough]   try %d: %d words, hard=%d soft=%d" % (attempt, words(body), len(hard), len(soft)))
            for h in hard:
                print("[warm-enough]     HARD: " + h)
            for s in soft:
                print("[warm-enough]     soft: " + s)
            if not hard:
                if (best is None or length_gap(body) < length_gap(best)
                        or (length_gap(body) == length_gap(best) and len(soft) <= len(best_soft))):
                    best, best_soft = body, soft
                if not soft:
                    break
            feedback = "\n".join("- " + x for x in hard + soft)
        if best is None:
            print("[warm-enough] chapter %d NOT saved: still broken after %d tries. Stopping (strict order)." % (n, args.max_tries))
            report.append((n, "NOT SAVED", hard))
            break
        text = "<!-- warm-enough chapter %d | %s | %s -->\n\n%s\n" % (n, pov, season, best)
        path.write_text(text, encoding="utf-8")
        print("[warm-enough]   saved %s (%d words)" % (path.relative_to(ROOT), words(best)))
        report.append((n, "saved", best_soft))
        if args.checkpoint:
            checkpoint(path, "Warm Enough: chapter %d (%d words)" % (n, words(best)))

    print("\n[warm-enough] REPORT")
    flagged = False
    for n, status, items in report:
        print("  chapter %d: %s%s" % (n, status, ("  | " + "; ".join(items)) if items else ""))
        flagged = flagged or status != "saved"
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main())
