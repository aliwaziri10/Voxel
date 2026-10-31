#!/usr/bin/env python3
"""
humanizer_revise.py v2 - paragraph-level revision of an UNPUBLISHED Voxel novel, driven by the humanizer FIX LIST.
(2026-10-31, free only: NVIDIA NIM models, secret NVIDIA_API_KEY_VA.)

v2 = the first version (written by the other profile, git hash 9591c813, never pushed) plus ideas taken from two
public humanizer projects:
  blader/humanizer (v3.1, based on Wikipedia "Signs of AI writing") and sheldum03/Humanity (40 patterns, self-audit).
  Taken from them:
    * extra tells that humanizer_pass.py does not list: "-ing" tails that explain an image (reflecting, symbolizing),
      sounds-deep sayings (at its core, the real question), staged run-ups (the thing is, honestly), arguing with
      no one (I'm not saying), stock AI words (quietly, palpable, tapestry, testament), copula avoidance (serves as),
      sentences that explain what an image meant, rows of short fragments, two or more forced triads in one paragraph
    * self-audit: every rewrite is checked again with the same detectors and is kept only if it has FEWER problems
      than the original paragraph (Humanity re-audits and does a second pass)
    * second pass: when a rewrite is rejected the model is asked once more, told exactly why
    * voice sample: unflagged paragraphs from the same chapter are shown to the model so it matches the book's own
      rhythm (blader: a writing sample overrides the generic rules)
    * [KEEP] idea: locked lines (this script's list plus every locked line of write_warm_enough.py) are never touched
    * residual count in the report: how many paragraphs are still flagged after the pass
  Added by this version for safety:
    * month, weekday, planning-word and "days later" checks on every rewritten paragraph (the book checker would
      otherwise revert the whole chapter for one bad paragraph)
    * the book checker runs on the chapter body with the HTML comment removed (same as write_warm_enough --check)
    * if the book checker cannot run, nothing is written (override with --no-book-check)
    * report lists every accepted edit with before and after text

WHAT IT DOES, per chapter, in the order given:
  1. Scores the chapter with scripts/humanizer_pass.py (HUMAN SCORE, higher = more human-like).
  2. Takes the FIX LIST paragraphs (same detectors as humanizer_pass.py plus the extra tells above).
  3. For each flagged paragraph (never the LAST paragraph of the chapter, never one holding a locked line) asks a
     free model to rewrite ONLY that paragraph, with the paragraphs before and after shown as read-only context.
  4. Keeps a rewrite only if ALL of these hold:
       - every quoted line of dialogue is still there word for word
       - no new capitalised name appears
       - no dash, no digit, none of the banned words, "grey" spelling kept
       - no new month, weekday, planning word or "days later"
       - word count within 90 to 115 percent of the original paragraph
       - the paragraph has fewer detector hits than before
       - the whole-chapter HUMAN SCORE does not go down
  5. At the end of the chapter: runs the book checker (scripts/write_warm_enough.py check). If the edited chapter has
     any HARD problem the original did not have, or lost more than 3 percent of its words, or gained under one point
     of score while removing fewer than three extra tells, the WHOLE chapter is reverted. Nothing is ever cut for length.
  6. Writes novels/<book>/stamps/HUMANIZER_REVISE_<date>_run<id>.md with scores and every accepted edit.

It never touches main. The workflow pushes a review branch. It refuses published books.
NOT live-tested against the NVIDIA models when written (the chat sandbox has no network): read the first branch
with care before merging.

USAGE (repo root)
  python scripts/humanizer_revise.py --book warm-enough --chapters 10,20,11 --max-paragraphs 25
  python scripts/humanizer_revise.py --book warm-enough --chapters 10-12 --dry-run     (no model calls, no writes)
  python scripts/humanizer_revise.py --book warm-enough --chapters 10 --models "z-ai/glm-5.3,nvidia/nemotron-3-super-120b-a12b"
"""
import argparse
import datetime
import os
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))

URL = "https://integrate.api.nvidia.com/v1/chat/completions"
MODELS = [
    "z-ai/glm-5.3",
    "z-ai/glm-5.3-flash",
    "nvidia/nemotron-3-ultra-550b-a55b",
    "nvidia/nemotron-3-super-120b-a12b",
]
PUBLISHED_MARKERS = ["amity-falls", "where-the-frost-doesnt-reach", "kindling-line", "proof-of-home"]
LOCKED = ["leave one door open", "stop being fine at me", "i came for the winter i was warm",
          "i've been cold since the ferry", "everything i make warm, i lose",
          "you have been polite for nine winters", '"stay."', '"eat."']
BANNED_WORDS = ["some", "something", "someone", "somewhere", "somehow", "somebody", "particular", "kind of"]
BANNED_RE = re.compile(r"\b(" + "|".join(BANNED_WORDS) + r")\b", re.I)

# same patterns as write_warm_enough.py, so a paragraph that would fail the book checker is rejected early
MONTHS_RE = re.compile(r"\b(January|February|March|April|June|July|August|September|October|November|December)\b")
WEEKDAYS_RE = re.compile(r"\b(Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)\b")
PLANNING_RE = re.compile(r"\b(chapter|beat|protagonist|sub-beat|touch level|canon)\b", re.I)
DAYS_LATER_RE = re.compile(r"\bdays? later\b", re.I)

SYSTEM = (
    "You are the line editor of a cozy fantasy slow-burn romance called Warm Enough (close third person, past tense). "
    "You rewrite ONE paragraph. You change sentence construction only. You keep every fact, event, object, "
    "name, spoken line and the final image of the paragraph exactly as they are. Spoken lines inside double "
    "quotes must stay word for word. Do not add events, objects, people, places, backstory or new metaphors "
    "from outside the character's own world. Do not add a fact that the paragraph does not already hold. "
    "Fix the listed problems: do not start several sentences in a row with he, she, they, his or her (open with a place, "
    "an object, a time, a spoken line, a clause, or join two sentences); replace stock phrases and 'not X but Y' "
    "constructions with a plain concrete statement using details already in the paragraph; do not state a feeling "
    "outright when the paragraph already shows it; do not add a closing sentence that explains what an image meant; "
    "do not hang an -ing phrase on a sentence to give it depth (reflecting, symbolizing, ensuring, highlighting); "
    "merge a row of tiny fragments into one sentence with a concrete claim; "
    "prefer plain verbs (was, had, sat) over serves as, stands as, functions as; "
    "vary sentence length unevenly, so short and long sentences alternate without a pattern. "
    "Rules: no em dashes, no en dashes, no digits, never use the words some, something, someone, somewhere, somehow, "
    "somebody, particular, or 'kind of'. Do not name any month or weekday. Never use the words quietly, palpable, "
    "unspoken, tapestry, testament. Spell grey with an e. American spelling otherwise. Keep the paragraph within "
    "10 percent of its original length and never shorter than 90 percent. "
    "A VOICE SAMPLE may be shown: match its rhythm and plainness, never copy its content. "
    "Output ONLY the rewritten paragraph as plain text: no quotes around it, no notes, no heading."
)


def log(*a):
    print(*a, flush=True)


def norm(s):
    return (s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')).lower()


def ist_now():
    tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    return datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M IST")


# ------------------------------------------------------------------ text tools
def split_blocks(text):
    """Returns (parts, para_index) where parts alternates block, separator, block ... and para_index maps
    humanizer paragraph number (1-based, same rule as humanizer_pass.paragraphs) to the index in parts."""
    parts = re.split(r"(\n\s*\n)", text)
    para_index, n = {}, 0
    for i in range(0, len(parts), 2):
        clean = "\n".join(l for l in parts[i].splitlines() if not l.lstrip().startswith("#")).strip()
        if clean:
            n += 1
            para_index[n] = i
    return parts, para_index


def quotes(p):
    return re.findall(r"[\"\u201c][^\"\u201d]{1,600}[\"\u201d]", p)


def mid_caps(p):
    return set(re.findall(r"(?<=[a-z,;] )([A-Z][a-z]+)", p))


def all_caps(p):
    return set(re.findall(r"\b([A-Z][a-z]+)\b", p))


def validate_paragraph(orig, new, chapter_caps):
    """Returns None if acceptable, else a short reason string."""
    if not new or "\n\n" in new:
        return "empty or more than one paragraph"
    if re.search("[\u2014\u2013]", new) or re.search(r"\d", new):
        return "dash or digit"
    if BANNED_RE.search(new):
        return "banned word"
    if re.search(r"\bgray\b", new, re.I):
        return "gray spelling"
    if len(MONTHS_RE.findall(new)) > len(MONTHS_RE.findall(orig)) or len(WEEKDAYS_RE.findall(new)) > len(WEEKDAYS_RE.findall(orig)):
        return "month or weekday name"
    if len(PLANNING_RE.findall(new)) > len(PLANNING_RE.findall(orig)):
        return "planning word (chapter, beat, canon, protagonist)"
    if len(DAYS_LATER_RE.findall(new)) > len(DAYS_LATER_RE.findall(orig)):
        return "the phrase days later"
    for q in quotes(orig):
        if q not in new:
            return "dialogue changed"
    if len(quotes(new)) != len(quotes(orig)):
        return "dialogue count changed"
    wo, wn = len(orig.split()), len(new.split())
    if wn < 0.9 * wo or wn > 1.15 * wo:
        return "length %d to %d words (must stay between 90 and 115 percent)" % (wo, wn)
    new_mid = mid_caps(new) - mid_caps(orig)
    if any(w not in chapter_caps for w in new_mid):
        return "new name or capital word"
    if new.strip() == orig.strip():
        return "unchanged"
    return None


def clean_reply(s):
    s = re.sub(r"<think>.*?</think>", "", s, flags=re.S | re.I).strip()
    s = re.sub(r"^```[a-z]*\n|\n```$", "", s).strip()
    s = re.sub(r"^(Here is|Here's)[^\n]*:\s*\n", "", s, flags=re.I).strip()
    return s


# ------------------------------------------------------------------ extra tells (from blader/humanizer and sheldum/Humanity)
EXTRA_RX = [
    ("-ing tail that explains the image",
     re.compile(r",\s+(?:highlighting|underscoring|emphasizing|emphasising|ensuring|reflecting|symbolizing|symbolising|"
                r"contributing to|cultivating|fostering|encompassing|showcasing)\b", re.I)),
    ("sounds-deep saying",
     re.compile(r"\b(?:at its core|the real question|what really matters|the heart of the matter|"
                r"the deeper (?:issue|truth|meaning)|fundamentally)\b", re.I)),
    ("staged run-up",
     re.compile(r"\b(?:here'?s the thing|the thing is|let'?s be honest|to be clear|don'?t get me wrong|real talk)\b"
                r"|(?:^|[.!?]\s+)(?:Honestly|Look|Listen)[,?]", re.I)),
    ("arguing with no one",
     re.compile(r"\b(?:i'?m not saying|this isn'?t (?:about|mainly)|this is not to say|one might (?:think|say)|"
                r"you might think)\b", re.I)),
    ("stock AI word",
     re.compile(r"\b(?:quietly|delve[sd]?|tapestry|testament|pivotal|meticulous(?:ly)?|vibrant|intricate|interplay|"
                r"underscor(?:e|es|ed|ing)|palpable|unspoken)\b", re.I)),
    ("copula avoidance", re.compile(r"\b(?:serves|stands|functions|operates) as\b", re.I)),
    ("sentence that explains the image",
     re.compile(r"\b(?:the message was clear|it was a (?:lesson|reminder|testament) in|a reminder that|"
                r"this (?:showed|shows|proved) (?:that|how))\b", re.I)),
]
TRIAD_RE = re.compile(r"\b\w+,\s+\w+,\s+(?:and|or)\s+\w+")


def narration(p):
    """The paragraph without its spoken lines (spoken lines cannot be changed, so they are not scanned)."""
    return re.sub(r"[\"\u201c][^\"\u201d]*[\"\u201d]", " ", p).replace("\u2019", "'")


def fragment_run(sentence_list):
    run = best = 0
    for s in sentence_list:
        if len(s.split()) <= 4:
            run += 1
            best = max(best, run)
        else:
            run = 0
    return best


def extra_tells(hp, p):
    n = narration(p)
    out = []
    for label, rx in EXTRA_RX:
        for m in rx.finditer(n):
            out.append("%s: ...%s..." % (label, n[max(0, m.start() - 30):m.end() + 30].strip()))
    if len(TRIAD_RE.findall(n)) >= 2:
        out.append("two or more forced triads in one paragraph (A, B, and C): keep one at most")
    fr = fragment_run(hp.sents(n))
    if fr >= 3:
        out.append("row of %d very short fragments: merge them into one sentence with a concrete claim" % fr)
    return out


def extra_total(hp, t):
    return sum(len(extra_tells(hp, p)) for p in hp.paragraphs(t))


def issue_count(hp, p):
    """How many detector hits one paragraph has on its own (same detectors as the fix list)."""
    one = [p]
    return (len(hp.opening_runs(one)) + len(hp.pronoun_clusters(one)) + len(hp.sentence_issues(one))
            + len(hp.closers(one)[1]) + len(extra_tells(hp, p)))


# ------------------------------------------------------------------ model
class Writer:
    def __init__(self, key, models):
        import requests
        self.requests = requests
        self.key = key
        self.models = list(models)
        self.dead = set()

    def ask(self, user, temperature=0.7):
        last = ""
        for model in self.models:
            if model in self.dead:
                continue
            for attempt in range(2):
                try:
                    r = self.requests.post(
                        URL, headers={"Authorization": "Bearer " + self.key, "Content-Type": "application/json"},
                        json={"model": model, "messages": [{"role": "system", "content": SYSTEM},
                                                            {"role": "user", "content": user}],
                              "temperature": temperature, "max_tokens": 6000}, timeout=240)
                except Exception as e:
                    last = "%s %s" % (type(e).__name__, str(e)[:120])
                    time.sleep(4)
                    continue
                if r.status_code in (404, 401, 403):
                    log("   model %s unavailable (HTTP %d), skipping it for this run" % (model, r.status_code))
                    self.dead.add(model)
                    break
                if r.status_code == 429:
                    last = "HTTP 429"
                    time.sleep(20)
                    continue
                if not r.ok:
                    last = "HTTP %d" % r.status_code
                    time.sleep(4)
                    continue
                try:
                    text = (r.json()["choices"][0]["message"].get("content") or "").strip()
                except Exception:
                    last = "bad json"
                    continue
                text = clean_reply(text)
                if text:
                    return text, model
                last = "empty reply"
        return None, last

    def alive(self):
        return any(m not in self.dead for m in self.models)


# ------------------------------------------------------------------ one chapter
def fix_reasons(hp, t):
    paras = hp.paragraphs(t)
    why = {}
    for pno, ln, w in hp.opening_runs(paras):
        why.setdefault(pno, []).append("%d sentences in a row open with '%s'" % (ln, w))
    for pno, hits, tot, ops in hp.pronoun_clusters(paras):
        why.setdefault(pno, []).append("%d of %d sentences open with a pronoun (%s)" % (hits, tot, "; ".join(ops[:4])))
    for pno, label, sent in hp.sentence_issues(paras):
        why.setdefault(pno, []).append("%s: %s" % (label, sent[:200]))
    for pno, sent in hp.closers(paras)[1]:
        why.setdefault(pno, []).append("paragraph ends on a short punchline sentence: %s" % sent[:120])
    for i, p in enumerate(paras, 1):
        for e in extra_tells(hp, p):
            why.setdefault(i, []).append(e)
    return why


def voice_sample(hp, text, why):
    """Up to three paragraphs of this same chapter that no detector flagged (narration only, 40 to 140 words)."""
    paras = hp.paragraphs(text)
    pool = [p for i, p in enumerate(paras, 1)
            if i not in why and not p.startswith("<!--") and '"' not in p and "\u201c" not in p
            and 40 <= len(p.split()) <= 140]
    if not pool:
        return ""
    step = max(1, len(pool) // 3)
    return "\n\n".join(pool[::step][:3])


def _res(n, status, before, wc0, **kw):
    r = {"n": n, "status": status, "before": before, "after": before, "kept": 0, "tried": 0, "rejects": [],
         "wc0": wc0, "wc1": wc0, "flag0": 0, "flag1": 0, "ex0": 0, "ex1": 0, "edits": []}
    r.update(kw)
    return r


def revise_chapter(hp, h, wm, base, writer, path, n, max_paras, asks, dry, locked, use_checker):
    text = path.read_text(encoding="utf-8")
    brief_path = path.parent.parent / "briefs" / ("ch%02d.md" % n)
    brief = brief_path.read_text(encoding="utf-8") if brief_path.exists() else ""

    def score(t):
        return hp.human_score(t, base, h.scan(t)["score"])[0]

    def hard_list(t):
        return wm.check(wm.clean_body(t), n, brief)[0]

    before = score(text)
    wc0 = len(text.split())
    hard0 = []
    if use_checker:
        try:
            hard0 = hard_list(text)
        except Exception as e:
            log("== chapter %02d: SKIPPED, the book checker failed on the original: %s" % (n, e))
            return _res(n, "SKIPPED: book checker failed on the original", before, wc0)
    why = fix_reasons(hp, text)
    ex0 = extra_total(hp, text)
    parts, pidx = split_blocks(text)
    last_no = max(pidx) if pidx else 0
    cand = []
    for pno, reasons in why.items():
        if pno == last_no or pno not in pidx:
            continue
        block = parts[pidx[pno]]
        if block.lstrip().startswith("<!--"):
            continue
        nb = norm(block)
        if any(l in nb for l in locked):
            continue
        cand.append((len(reasons), pno))
    cand.sort(key=lambda x: (-x[0], x[1]))
    chosen = sorted(p for _, p in cand[:max_paras])
    log("== chapter %02d: score %.1f, %d flagged paragraphs, %d extra tells, editing %d" % (n, before, len(why), ex0, len(chosen)))
    if dry or not chosen:
        return _res(n, "dry run" if dry else "nothing to edit", before, wc0, flag0=len(why), flag1=len(why), ex0=ex0, ex1=ex0)
    chapter_caps = all_caps(text)
    pov = ("Ansel Brandt (schoolroom, chalk, slates, rivers, ferries and children are his comparisons; NO wool or knitting "
           "comparisons)" if n % 2 == 1 else
           "Hester Tansley (wool and knitting are her comparisons: tension, ply, stitch, gauge; NO schoolroom or river comparisons)")
    sample = voice_sample(hp, text, why)
    sample_block = ("VOICE SAMPLE (paragraphs from this same chapter that no detector flagged; match their rhythm and "
                    "plainness, never copy their content):\n%s\n\n" % sample) if sample else ""
    cur, kept, tried, rejects, edits = text, 0, 0, [], []
    cur_score = before
    for pno in chosen:
        if not writer.alive():
            rejects.append((pno, "no model available for the rest of the run"))
            continue
        parts, pidx = split_blocks(cur)
        if pno not in pidx:
            continue
        orig = parts[pidx[pno]]
        prev_p = parts[pidx[pno - 1]] if (pno - 1) in pidx else ""
        next_p = parts[pidx[pno + 1]] if (pno + 1) in pidx else ""
        before_cnt = issue_count(hp, orig)
        base_prompt = ("Point of view of this chapter: %s.\n\n%sPARAGRAPH BEFORE (read only):\n%s\n\nPARAGRAPH AFTER (read only):\n%s\n\n"
                       "PROBLEMS FOUND (fix all of these, add none):\n- %s\n\nPARAGRAPH TO REWRITE:\n%s\n\nRewrite it now. Output only the paragraph."
                       % (pov, sample_block, prev_p, next_p, "\n- ".join(why[pno]), orig))
        tried += 1
        feedback, accepted = "", False
        for ask_no in range(1, asks + 1):
            prompt = base_prompt
            if feedback:
                prompt += ("\n\nYOUR PREVIOUS ATTEMPT WAS REJECTED BECAUSE: %s.\nRewrite again, starting from the ORIGINAL "
                           "paragraph shown above, and avoid that mistake." % feedback)
            new, info = writer.ask(prompt, 0.7 if ask_no == 1 else 0.85)
            time.sleep(2)
            if not new:
                feedback = "no model reply (%s)" % info
                break
            bad = validate_paragraph(orig, new, chapter_caps)
            if bad:
                feedback = bad
                continue
            after_cnt = issue_count(hp, new)
            if after_cnt >= before_cnt:
                feedback = "it still has %d detector hits (the original had %d); fix every listed problem and add no new ones" % (after_cnt, before_cnt)
                continue
            trial_parts = list(parts)
            trial_parts[pidx[pno]] = new
            trial = "".join(trial_parts)
            s = score(trial)
            if s < cur_score:
                feedback = "the chapter's human score would drop from %.1f to %.1f" % (cur_score, s)
                continue
            cur, cur_score, kept, accepted = trial, s, kept + 1, True
            edits.append((pno, why[pno], orig, new))
            log("   P%d kept (%s, ask %d): hits %d to %d, score %.1f" % (pno, info, ask_no, before_cnt, after_cnt, s))
            break
        if not accepted:
            rejects.append((pno, "after %d ask(s): %s" % (asks, feedback)))
    wc1 = len(cur.split())
    status = "edited"
    ex1 = ex0
    if kept:
        hard1 = []
        if use_checker:
            try:
                hard1 = hard_list(cur)
            except Exception as e:
                log("   book checker error on edit:", e)
                hard1 = ["book checker failed on the edited chapter"]
        new_hard = [x for x in hard1 if x not in hard0]
        ex1 = extra_total(hp, cur)
        if new_hard:
            status = "REVERTED: new HARD problems %s" % new_hard[:3]
        elif wc1 < 0.97 * wc0:
            status = "REVERTED: lost %d words" % (wc0 - wc1)
        elif cur_score < before + 1.0 and ex1 > ex0 - 3:
            status = "REVERTED: score gain under one point and fewer than three extra tells removed"
        if status == "edited":
            path.write_text(cur, encoding="utf-8")
            flag1 = len(fix_reasons(hp, cur))
        else:
            cur_score, wc1, flag1 = before, wc0, len(why)
            ex1 = ex0
            kept_edits = edits
            log("   chapter %02d: %s" % (n, status))
            return _res(n, status, before, wc0, after=before, kept=0, tried=tried, rejects=rejects, wc1=wc0,
                        flag0=len(why), flag1=len(why), ex0=ex0, ex1=ex0, edits=[("(reverted) P%d" % e[0],) + e[1:] for e in kept_edits])
    else:
        status = "no paragraph accepted"
        cur_score, wc1, flag1 = before, wc0, len(why)
    log("   chapter %02d: %s, score %.1f to %.1f, words %d to %d" % (n, status, before, cur_score, wc0, wc1))
    return _res(n, status, before, wc0, after=cur_score, kept=kept, tried=tried, rejects=rejects, wc1=wc1,
                flag0=len(why), flag1=flag1, ex0=ex0, ex1=ex1, edits=edits)


def parse_chapters(s):
    out = []
    for piece in s.split(","):
        piece = piece.strip()
        if not piece:
            continue
        if "-" in piece:
            a, b = piece.split("-", 1)
            out += list(range(int(a), int(b) + 1))
        else:
            out.append(int(piece))
    return out


def one_line(s):
    return " ".join(str(s).split())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", default="warm-enough")
    ap.add_argument("--chapters", required=True, help="example: 10,20,11 or 10-12")
    ap.add_argument("--max-paragraphs", type=int, default=25)
    ap.add_argument("--asks", type=int, default=2, help="model asks per paragraph (second ask is told why the first failed)")
    ap.add_argument("--models", default="", help="comma list of NVIDIA model ids, replaces the built-in list")
    ap.add_argument("--no-book-check", action="store_true", help="write edits even if the book checker cannot run (not advised)")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()

    if any(m in a.book for m in PUBLISHED_MARKERS):
        log("REFUSED: %s is a published book." % a.book)
        return 3
    book = ROOT / "novels" / a.book
    if (book / "PUBLISHED.md").exists() or (book / "FROZEN.md").exists():
        log("REFUSED: %s is marked published or frozen." % a.book)
        return 3
    key = os.environ.get("NVIDIA_API_KEY", "")
    if not key and not a.dry_run:
        log("NVIDIA_API_KEY is not set (secret NVIDIA_API_KEY_VA must be mapped in the workflow). Nothing done.")
        return 2

    import humanizer_pass as hp
    import humanizer as h
    try:
        import write_warm_enough as wm
    except Exception as e:
        wm = None
        log("book checker not importable:", e)
    use_checker = wm is not None
    if not use_checker and not a.dry_run and not a.no_book_check:
        log("REFUSED: the book checker (scripts/write_warm_enough.py) cannot be imported, so edits could not be verified. "
            "Fix the import or pass --no-book-check.")
        return 2
    locked = {norm(x) for x in LOCKED}
    if wm is not None:
        locked |= {norm(x) for x in getattr(wm, "LOCKED", {})}
    base = hp.baseline()
    models = [m.strip() for m in a.models.split(",") if m.strip()] or MODELS
    writer = None if a.dry_run else Writer(key, models)
    results = []
    for n in parse_chapters(a.chapters):
        path = book / "chapters" / ("chapter_%02d.md" % n)
        if not path.exists():
            log("chapter %02d: file not found" % n)
            continue
        results.append(revise_chapter(hp, h, wm, base, writer, path, n, a.max_paragraphs, max(1, a.asks), a.dry_run,
                                      sorted(locked), use_checker))

    lines = ["# Humanizer revision run v2 (%s)" % ist_now(), "",
             "Book: %s. Chapters: %s. Max paragraphs per chapter: %d. Asks per paragraph: %d. Dry run: %s." % (
                 a.book, a.chapters, a.max_paragraphs, a.asks, a.dry_run),
             "Free NVIDIA models only (%s). Paragraph-level edits, last paragraph and locked lines never touched." % ", ".join(models),
             "A paragraph is kept only if dialogue, names, length, detector hits and the whole-chapter score all pass. A chapter is reverted",
             "if the book checker finds a new HARD problem, the chapter loses more than 3 percent of its words, or the gain is too small.",
             "", "| ch | status | HUMAN before | HUMAN after | paragraphs kept / tried | flagged paragraphs before to after | extra tells before to after | words before to after |",
             "|---|---|---|---|---|---|---|---|"]
    for r in results:
        lines.append("| %02d | %s | %.1f | %.1f | %d / %d | %d to %d | %d to %d | %d to %d |" % (
            r["n"], r["status"], r["before"], r["after"], r["kept"], r["tried"], r["flag0"], r["flag1"],
            r["ex0"], r["ex1"], r["wc0"], r["wc1"]))
    lines += ["", "## Rejected paragraph rewrites (reason)", ""]
    for r in results:
        for pno, why in r["rejects"]:
            lines.append("- ch%02d P%d: %s" % (r["n"], pno, why))
    lines += ["", "## Edits (before and after)", ""]
    for r in results:
        for e in r["edits"]:
            tag, why, orig, new = e[0], e[1], e[2], e[3]
            label = tag if isinstance(tag, str) else "P%d" % tag
            lines += ["### ch%02d %s" % (r["n"], label), "Fixed: " + "; ".join(one_line(x)[:160] for x in why[:4]), "",
                      "Before:", "> " + one_line(orig), "", "After:", "> " + one_line(new), ""]
    lines += ["", "The human read of every chapter against its brief is still NOT done. This is a mechanical voice pass."]
    report = "\n".join(lines) + "\n"
    print("\n" + report)
    summ = os.environ.get("GITHUB_STEP_SUMMARY")
    if summ:
        with open(summ, "a", encoding="utf-8") as f:
            f.write(report)
    if not a.dry_run:
        sd = book / "stamps"
        sd.mkdir(exist_ok=True)
        (sd / ("HUMANIZER_REVISE_%s_run%s.md" % (datetime.date.today().isoformat(), os.environ.get("GITHUB_RUN_ID", "local")))).write_text(report, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
