#!/usr/bin/env python3
"""
chapter_review.py v2 - REVIEW-ONLY chapter check for an UNPUBLISHED Voxel novel. It never rewrites a chapter.
(2026-11-06, free only: NVIDIA NIM models, secret NVIDIA_API_KEY_VA.)

v2 adds, on top of v1 (chapter-level checks, verified quotes, 3 votes):
  * LEDGER: every chapter's facts are saved by kind (time, knowledge, prop, place, body, relationship, promise, rule)
    each with a verified quote, and every new chapter is checked against the ledger of earlier chapters.
    (Idea from fiction-forge: a cold read that carries a running ledger found 191 errors that five chapter-by-chapter
    passes missed, because errors build up across chapters.)
  * PROMISES: planted details and promises carried in from earlier chapters are listed for you (free, no model).
  * REPEATS: phrases of 6+ words that this chapter shares with 2 or more OTHER chapters are listed (free, no model).
    Locked lines are ignored.

Ideas used from public projects (re-written here, no code copied):
  sepia (chapter-structure checks), QianBi-Novel (regex must contracts, verified quotes, 3 votes),
  fiction-forge (ledger across chapters, cross-chapter repetition), CanonBench (test the checker with injected errors,
  see scripts/review_canary.py).

OUTPUT: novels/<book>/stamps/CHAPTER_REVIEW_<date>_run<id>.md and the Actions summary page, plus
novels/<book>/stamps/FACTS_chNN.json. Nothing else is changed. It refuses published books.

USAGE (repo root)
  python scripts/chapter_review.py --book warm-enough --chapters 1-10        (review in story order)
  python scripts/chapter_review.py --book warm-enough --chapters 10 --dry-run (free checks only, no model calls)
Optional file: novels/<book>/MUST_CONTRACTS.md, one rule per line:  rule text | `regex`
"""
import argparse
import datetime
import difflib
import json
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
KINDS = ["time", "knowledge", "prop", "place", "body", "relationship", "promise", "rule"]

SYSTEM = (
    "You are a strict fiction reviewer. You only REPORT problems, you never rewrite the chapter. Every finding must "
    "contain a QUOTE copied exactly, word for word, from the chapter text (one sentence or part of a sentence, never "
    "invented, never paraphrased). If you cannot quote it, do not report it. If the chapter has no such problem, "
    "return an empty list. Answer with JSON only, no other text."
)

DIMENSIONS = {
    "theme": "Places where the NARRATOR states the theme or the lesson outright, or sums up what the moment meant "
             "(for example 'that is how people are', 'she understood now that', 'what mattered was'), or explains a "
             "symbol that the scene already showed.",
    "ending": "The chapter ending is too tidy: the point-of-view character decides AND understands AND accepts, every "
              "account is settled, a closing line explains the feeling. Quote the sentence(s) that settle too much. "
              "If the ending stops early and leaves something open, return an empty list.",
    "emotion": "Emotion that is shown ONLY through body sensation or weather/room mirroring the mood (tight chest, "
               "throat closing, light dimming to match sadness) where simple behaviour or a plain statement would "
               "do. Quote the instance. Report at most the 4 worst.",
    "dialogue": "Dialogue where characters debate ideas, feelings or the nature of things in abstract, polished "
                "sentences, instead of arguing about something specific they want or need right now.",
    "payoff": "Moments that are too convenient: a problem that solves cleanly, a helpful stranger, a setup that is "
              "paid off at once, a reconciliation exactly on schedule, a causal chain with no loose end. Quote the "
              "sentence where the convenience happens.",
}

GENERALISATION_RE = re.compile(
    r"\b(that is (how|what|why)|that was (how|what|why)|it was then (that )?(she|he)|in the end|what mattered|"
    r"(she|he) (understood|realized|realised|knew) (now|then|at last|that)|(she|he) learned that|"
    r"the truth (was|is)|maybe that was)\b", re.I)
SENSATION_RE = re.compile(
    r"\b(chest (tightened|clenched|ached|squeezed)|throat (tightened|closed|ached)|heart (pounded|hammered|raced|"
    r"clenched|skipped)|stomach (dropped|knotted|twisted|clenched)|breath (caught|hitched)|shiver|trembl\w+|"
    r"cold (washed|spread|crept)|knees (weak|buckled))\b", re.I)
LABEL_RE = re.compile(r"\b(was|felt|were) (afraid|scared|sad|angry|ashamed|lonely|happy|relieved|jealous|hurt|nervous)\b", re.I)
SMELL_RE = re.compile(r"\b(smell\w*|scent\w*|aroma|fragran\w+|perfume|whiff|reek\w*)\b", re.I)

# curly quotes are handled by code points so this file has no special characters in it
CURLY = {0x2019: "'", 0x2018: "'", 0x201C: '"', 0x201D: '"'}
CLOSERS = "\"')" + chr(0x201D)
SENT_SPLIT = re.compile(r"(?<=[.!?])[" + re.escape(CLOSERS) + r"]*\s+")

STOPWORDS = set("""the a an and of to in on at he she it i you we they his her him them their its was were is are be been
that this with for as but not so or if then than too very had has have do did does said say would could will can my your
our me us from by up out into over just there here what when who whom how why all one no yes""".split())


def log(*a):
    print(*a, flush=True)


def norm(s):
    return re.sub(r"\s+", " ", s.translate(CURLY)).strip().lower()


def ist_now():
    tz = datetime.timezone(datetime.timedelta(hours=5, minutes=30))
    return datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M IST")


def one_line(s):
    return " ".join(str(s).split())


def body_of(text):
    return re.sub(r"<!--.*?-->", "", text, flags=re.S).strip()


def paragraphs(body):
    """Numbered the same way for every check: blank-line blocks, headings dropped."""
    out = []
    for blk in re.split(r"\n\s*\n", body):
        clean = "\n".join(l for l in blk.splitlines() if not l.lstrip().startswith("#")).strip()
        if clean:
            out.append(clean)
    return out


def sentences(p):
    return [s.strip() for s in SENT_SPLIT.split(p) if s.strip()]


# ------------------------------------------------------------------ model client
class Client:
    def __init__(self, key, models):
        import requests
        self.requests = requests
        self.key = key
        self.models = list(models)
        self.dead = set()
        self.turn = 0

    def alive(self):
        return any(m not in self.dead for m in self.models)

    def ask(self, user, temperature=0.3, system=None):
        """Rotates the starting model on every call so votes come from different models where possible."""
        live = [m for m in self.models if m not in self.dead]
        if not live:
            return None, "no live model"
        self.turn += 1
        order = live[self.turn % len(live):] + live[:self.turn % len(live)]
        last = ""
        for model in order:
            for attempt in range(2):
                try:
                    r = self.requests.post(
                        URL, headers={"Authorization": "Bearer " + self.key, "Content-Type": "application/json"},
                        json={"model": model, "messages": [{"role": "system", "content": system or SYSTEM},
                                                            {"role": "user", "content": user}],
                              "temperature": temperature, "max_tokens": 4000}, timeout=240)
                except Exception as e:
                    last = "%s %s" % (type(e).__name__, str(e)[:100])
                    time.sleep(4)
                    continue
                if r.status_code in (404, 401, 403):
                    log("   model %s unavailable (HTTP %d), skipping it" % (model, r.status_code))
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
                data = parse_json(text)
                if data is not None:
                    return data, model
                last = "reply was not JSON"
        return None, last


def parse_json(text):
    text = re.sub(r"^```(?:json)?|```$", "", text.strip(), flags=re.M).strip()
    i, j = text.find("{"), text.rfind("}")
    if i < 0 or j < i:
        return None
    try:
        return json.loads(text[i:j + 1])
    except Exception:
        return None


# ------------------------------------------------------------------ quote verification
def locate(quote, paras):
    """Returns paragraph number (1-based) that holds the quote, or 0 if it cannot be verified.
    Exact normalised substring first, then a close fuzzy match against single sentences (>= 0.9)."""
    q = norm(quote)
    if len(q) < 12:
        return 0
    for i, p in enumerate(paras, 1):
        if q in norm(p):
            return i
    best, where = 0.0, 0
    for i, p in enumerate(paras, 1):
        for s in sentences(p):
            ns = norm(s)
            if abs(len(ns) - len(q)) > max(20, len(q) // 2):
                continue
            r = difflib.SequenceMatcher(None, q, ns).ratio()
            if r > best:
                best, where = r, i
    return where if best >= 0.9 else 0


# ------------------------------------------------------------------ cross-chapter repeated phrases (free)
NGRAM = 6


def tokens_of(text):
    return re.findall(r"[a-z']+", norm(text))


def good_gram(gram):
    return sum(1 for w in gram if w not in STOPWORDS) >= 3


def other_chapter_grams(book, n):
    """dict: 6-word phrase -> set of other chapter numbers that contain it."""
    grams = {}
    for f in sorted((book / "chapters").glob("chapter_*.md")):
        m = re.search(r"chapter_(\d+)\.md$", f.name)
        if not m or int(m.group(1)) == n:
            continue
        ch = int(m.group(1))
        toks = tokens_of(body_of(f.read_text(encoding="utf-8")))
        for i in range(len(toks) - NGRAM + 1):
            gram = tuple(toks[i:i + NGRAM])
            if good_gram(gram):
                grams.setdefault(gram, set()).add(ch)
    return grams


def cross_repeats(book, n, paras, locked, min_chapters=2, limit=8):
    """Phrases of 6+ words this chapter shares with at least min_chapters other chapters. Returns a list of
    (paragraph number, phrase, sorted chapter list), strongest first."""
    grams = other_chapter_grams(book, n)
    locked_text = [" ".join(tokens_of(l)) for l in locked]
    found = []
    for pno, p in enumerate(paras, 1):
        toks = tokens_of(p)
        hit = [i for i in range(len(toks) - NGRAM + 1)
               if len(grams.get(tuple(toks[i:i + NGRAM]), ())) >= min_chapters
               and not any(" ".join(toks[i:i + NGRAM]) in lt for lt in locked_text)]
        runs = []
        for i in hit:
            if runs and i <= runs[-1][1] + 1:
                runs[-1][1] = i
            else:
                runs.append([i, i])
        for s, e in runs:
            phrase = " ".join(toks[s:e + NGRAM])
            chs = set()
            for i in range(s, e + 1):
                chs |= grams.get(tuple(toks[i:i + NGRAM]), set())
            found.append((pno, phrase, sorted(chs)))
    found.sort(key=lambda x: (-len(x[2]), -len(x[1].split())))
    return found[:limit]


# ------------------------------------------------------------------ deterministic checks (free)
def load_contracts(book):
    f = book / "MUST_CONTRACTS.md"
    rules = []
    if not f.exists():
        return rules
    for line in f.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\s*[-*]?\s*(.+?)\s*\|\s*`(.+)`\s*$", line)
        if not m:
            continue
        try:
            rules.append((m.group(1), re.compile(m.group(2))))
        except re.error as e:
            log("bad regex in MUST_CONTRACTS.md, skipped: %s (%s)" % (m.group(2), e))
    return rules


def deterministic(body, paras, contracts, wm, n):
    out = {"contracts": [], "book_hard": [], "book_soft": [], "ending_generalisations": [], "stats": {}}
    for rule, rx in contracts:
        hits = []
        for i, p in enumerate(paras, 1):
            for m in rx.finditer(p):
                hits.append((i, one_line(p[max(0, m.start() - 40):m.end() + 40])))
        if hits:
            out["contracts"].append((rule, hits[:6], len(hits)))
    if wm is not None:
        try:
            hard, soft = wm.check(body, n, None)
            out["book_hard"], out["book_soft"] = list(hard), list(soft)
        except Exception as e:
            out["book_soft"] = ["book checker raised %s: %s" % (type(e).__name__, str(e)[:120])]
    tail = len(paras) - 2
    for i, p in enumerate(paras, 1):
        if i >= tail:
            m = GENERALISATION_RE.search(p)
            if m:
                out["ending_generalisations"].append((i, one_line(p[max(0, m.start() - 50):m.end() + 60])))
    sens = len(SENSATION_RE.findall(body))
    lab = len(LABEL_RE.findall(body))
    smell = len(SMELL_RE.findall(body))
    words = max(1, len(body.split()))
    out["stats"] = {"words": words, "body_sensation": sens, "plain_labels": lab, "smell_words": smell,
                    "per_1000_sensation": round(sens * 1000.0 / words, 1)}
    return out


# ------------------------------------------------------------------ voted model review
def review_dimension(client, dim, brief, body, paras, votes):
    """Returns list of dicts: para, votes, quote, problem, hint, plus counts of dropped (unverifiable) quotes."""
    numbered = "\n\n".join("[P%d] %s" % (i, p) for i, p in enumerate(paras, 1))
    user = ("CHAPTER (paragraphs numbered):\n\n%s\n\nCHECK: %s\n\nReturn JSON: {\"findings\": [{\"quote\": \"exact words from the "
            "chapter\", \"problem\": \"one short sentence\", \"hint\": \"one short idea for fixing it, no rewrite\"}]}. "
            "At most 4 findings." % (numbered, brief))
    tally, dropped, replies = {}, 0, 0
    for v in range(votes):
        data, model = client.ask(user)
        if data is None:
            log("   %s vote %d failed: %s" % (dim, v + 1, model))
            continue
        replies += 1
        seen = set()
        for f in (data.get("findings") or [])[:4]:
            if not isinstance(f, dict):
                continue
            q = str(f.get("quote", ""))
            pno = locate(q, paras)
            if not pno:
                dropped += 1
                continue
            if pno in seen:
                continue
            seen.add(pno)
            e = tally.setdefault(pno, {"para": pno, "votes": 0, "quote": one_line(q)[:240],
                                       "problem": one_line(f.get("problem", ""))[:200], "hint": one_line(f.get("hint", ""))[:200]})
            e["votes"] += 1
    need = 2 if votes >= 3 else 1
    kept = sorted((e for e in tally.values() if e["votes"] >= need), key=lambda e: (-e["votes"], e["para"]))
    return kept, dropped, replies


# ------------------------------------------------------------------ facts ledger and contradictions
FACTS_PROMPT = (
    "CHAPTER (paragraphs numbered):\n\n%s\n\nBuild the story ledger entries this chapter establishes that a later chapter "
    "could contradict. Each entry has a KIND, one of: time (what day, time of day, season, how long since something), "
    "knowledge (who knows what, and when they learned it), prop (who holds or owns an object, where it is), place "
    "(where someone is, what a location is like), body (injuries, tiredness, clothing, illness), relationship (what "
    "people are to each other, what is said between them), promise (something promised, planned or set up that must "
    "be paid off later), rule (how this world works). Each entry must carry an exact QUOTE from the chapter. Also list "
    "small planted details that may be paid off later. Return JSON: {\"facts\": [{\"kind\": \"prop\", \"subject\": "
    "\"...\", \"fact\": \"one short sentence\", \"quote\": \"exact words\"}], \"planted\": [{\"detail\": \"one short "
    "sentence\", \"quote\": \"exact words\"}]}. At most 14 facts and 5 planted."
)

CONFLICT_PROMPT = (
    "ESTABLISHED LEDGER from earlier chapters (kind in brackets):\n%s\n\nNEW CHAPTER (paragraphs numbered):\n\n%s\n\nFind "
    "places where the new chapter CONTRADICTS the ledger (not merely adds to it). Typical errors: a day or time that "
    "runs backwards, a character who knows something before they learned it, an object in two places or held by the "
    "wrong person, an injury or condition that vanished, a person described differently. Each finding needs the exact "
    "QUOTE from the new chapter. Return JSON: {\"conflicts\": [{\"old_fact\": \"the established entry\", \"quote\": "
    "\"exact words from the new chapter\", \"why\": \"one short sentence\"}]}. Empty list if none."
)


def extract_facts(client, paras):
    numbered = "\n\n".join("[P%d] %s" % (i, p) for i, p in enumerate(paras, 1))
    data, model = client.ask(FACTS_PROMPT % numbered)
    if data is None:
        return None, 0
    facts, planted, dropped = [], [], 0
    for f in (data.get("facts") or [])[:14]:
        pno = locate(str(f.get("quote", "")), paras) if isinstance(f, dict) else 0
        if pno:
            kind = str(f.get("kind", "")).strip().lower()
            facts.append({"kind": kind if kind in KINDS else "other", "subject": one_line(f.get("subject", ""))[:60],
                          "fact": one_line(f.get("fact", ""))[:200], "quote": one_line(f.get("quote", ""))[:240],
                          "para": pno})
        else:
            dropped += 1
    for f in (data.get("planted") or [])[:5]:
        pno = locate(str(f.get("quote", "")), paras) if isinstance(f, dict) else 0
        if pno:
            planted.append({"detail": one_line(f.get("detail", ""))[:200], "quote": one_line(f.get("quote", ""))[:240],
                            "para": pno})
        else:
            dropped += 1
    return {"facts": facts, "planted": planted}, dropped


def earlier_fact_rows(stamps, n, last=6):
    """Ledger rows from the last `last` chapters before chapter n, oldest first, at most 150."""
    files = []
    for f in stamps.glob("FACTS_ch*.json"):
        m = re.search(r"FACTS_ch(\d+)\.json$", f.name)
        if m and int(m.group(1)) < n:
            files.append((int(m.group(1)), f))
    files.sort()
    rows = []
    for ch, f in files[-last:]:
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for x in d.get("facts", []):
            rows.append({"ch": ch, "kind": x.get("kind", "other"), "subject": x.get("subject", ""),
                         "fact": x.get("fact", "")})
    return rows[:150]


def earlier_facts(stamps, n, last=6):
    return ["- ch%02d [%s]: %s (%s)" % (r["ch"], r["kind"], r["fact"], r["subject"])
            for r in earlier_fact_rows(stamps, n, last)]


def carried_promises(stamps, n, limit=10):
    """Promise-kind facts and planted details from all earlier chapters, for the human to keep in mind. Free."""
    out = []
    for f in sorted(stamps.glob("FACTS_ch*.json")):
        m = re.search(r"FACTS_ch(\d+)\.json$", f.name)
        if not m or int(m.group(1)) >= n:
            continue
        try:
            d = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        ch = int(m.group(1))
        for x in d.get("facts", []):
            if x.get("kind") == "promise":
                out.append((ch, x.get("fact", "")))
        for x in d.get("planted", []):
            out.append((ch, x.get("detail", "")))
    return out[-limit:]


def check_conflicts(client, stamps, n, paras):
    lines = earlier_facts(stamps, n)
    if not lines:
        return [], 0, 0
    numbered = "\n\n".join("[P%d] %s" % (i, p) for i, p in enumerate(paras, 1))
    user = CONFLICT_PROMPT % ("\n".join(lines), numbered)
    tally, dropped, replies = {}, 0, 0
    for v in range(3):
        data, model = client.ask(user)
        if data is None:
            continue
        replies += 1
        seen = set()
        for c in (data.get("conflicts") or [])[:4]:
            if not isinstance(c, dict):
                continue
            pno = locate(str(c.get("quote", "")), paras)
            if not pno:
                dropped += 1
                continue
            if pno in seen:
                continue
            seen.add(pno)
            e = tally.setdefault(pno, {"para": pno, "votes": 0, "quote": one_line(c.get("quote", ""))[:240],
                                       "old": one_line(c.get("old_fact", ""))[:200], "why": one_line(c.get("why", ""))[:200]})
            e["votes"] += 1
    kept = sorted((e for e in tally.values() if e["votes"] >= 2), key=lambda e: (-e["votes"], e["para"]))
    return kept, dropped, replies


# ------------------------------------------------------------------ one chapter
def review_chapter(wm, client, book, n, contracts, votes, do_facts, dry, locked):
    path = book / "chapters" / ("chapter_%02d.md" % n)
    if not path.exists():
        log("chapter %02d: file not found" % n)
        return None
    body = body_of(path.read_text(encoding="utf-8"))
    paras = paragraphs(body)
    log("== chapter %02d: %d paragraphs, %d words" % (n, len(paras), len(body.split())))
    res = {"n": n, "paras": len(paras), "det": deterministic(body, paras, contracts, wm, n), "dims": {}, "dropped": 0,
           "replies": 0, "conflicts": [], "facts": None, "planted": 0, "kinds": {},
           "repeats": cross_repeats(book, n, paras, locked),
           "promises": carried_promises(book / "stamps", n)}
    if dry or client is None:
        return res
    for dim, brief in DIMENSIONS.items():
        kept, dropped, replies = review_dimension(client, dim, brief, body, paras, votes)
        res["dims"][dim] = kept
        res["dropped"] += dropped
        res["replies"] += replies
        log("   %s: %d agreed finding(s), %d unverifiable quote(s) dropped, %d reply(ies)" % (dim, len(kept), dropped, replies))
    if do_facts:
        stamps = book / "stamps"
        facts, dropped = extract_facts(client, paras)
        res["dropped"] += dropped
        if facts is not None:
            res["facts"] = len(facts["facts"])
            res["planted"] = len(facts["planted"])
            for x in facts["facts"]:
                res["kinds"][x["kind"]] = res["kinds"].get(x["kind"], 0) + 1
            stamps.mkdir(exist_ok=True)
            (stamps / ("FACTS_ch%02d.json" % n)).write_text(json.dumps(facts, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        conf, d2, _ = check_conflicts(client, stamps, n, paras)
        res["conflicts"] = conf
        res["dropped"] += d2
        log("   facts: %s, planted: %s, contradictions: %d" % (res["facts"], res["planted"], len(conf)))
    return res


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


def render(results, a, models):
    L = ["# Chapter review v2 (%s)" % ist_now(), "",
         "Book: %s. Chapters: %s. Votes per check: %d. Dry run: %s." % (a.book, a.chapters, a.votes, a.dry_run),
         "Review only: no chapter text was changed. Findings need an exact verified quote and at least 2 of %d votes." % a.votes,
         "Models: %s." % ", ".join(models), ""]
    for r in results:
        d = r["det"]
        L += ["## Chapter %02d (%d paragraphs, %d words)" % (r["n"], r["paras"], d["stats"]["words"]), ""]
        L.append("**Free checks.** Book checker HARD: %s. SOFT: %s." % (
            "none" if not d["book_hard"] else "; ".join(one_line(x)[:140] for x in d["book_hard"]),
            "none" if not d["book_soft"] else "; ".join(one_line(x)[:140] for x in d["book_soft"][:6])))
        s = d["stats"]
        L.append("Emotion by body sensation: %d (%.1f per 1000 words), plain feeling statements: %d, smell words: %d." % (
            s["body_sensation"], s["per_1000_sensation"], s["plain_labels"], s["smell_words"]))
        if s["body_sensation"] >= 4 and s["plain_labels"] == 0:
            L.append("FLAG: feelings appear only as body sensation and never as plain statements.")
        if s["smell_words"] >= 4:
            L.append("FLAG: smell is used a lot (%d words), a known AI habit." % s["smell_words"])
        if d["ending_generalisations"]:
            L.append("FLAG: summing-up phrases in the last two paragraphs:")
            for p, t in d["ending_generalisations"][:5]:
                L.append("- P%d: ...%s..." % (p, t))
        if d["contracts"]:
            L.append("MUST CONTRACT broken:")
            for rule, hits, total in d["contracts"]:
                L.append("- %s (%d hit%s)" % (rule, total, "" if total == 1 else "s"))
                for p, t in hits[:3]:
                    L.append("  - P%d: ...%s..." % (p, t))
        if r["repeats"]:
            L.append("REPEATED PHRASES shared with 2 or more other chapters (locked lines ignored):")
            for p, phrase, chs in r["repeats"]:
                L.append("- P%d: \"%s\" (also in chapters %s)" % (p, phrase, ", ".join("%02d" % c for c in chs)))
        if r["promises"]:
            L.append("PROMISES AND PLANTED DETAILS carried in from earlier chapters (check that this chapter does not forget them):")
            for ch, t in r["promises"]:
                L.append("- ch%02d: %s" % (ch, one_line(t)[:160]))
        L.append("")
        if r["dims"]:
            for dim, kept in r["dims"].items():
                L.append("**%s** (%d finding%s)" % (dim, len(kept), "" if len(kept) == 1 else "s"))
                for e in kept:
                    L += ["- P%d, %d votes: \"%s\"" % (e["para"], e["votes"], e["quote"]),
                          "  Problem: %s. Idea: %s" % (e["problem"], e["hint"])]
                L.append("")
            if r["conflicts"]:
                L.append("**continuity contradictions with earlier chapters**")
                for e in r["conflicts"]:
                    L += ["- P%d, %d votes: \"%s\"" % (e["para"], e["votes"], e["quote"]),
                          "  Earlier entry: %s. Why: %s" % (e["old"], e["why"])]
                L.append("")
            kinds = ", ".join("%s %d" % (k, v) for k, v in sorted(r["kinds"].items())) or "none"
            L.append("Ledger saved: %s entries (%s). Planted details noted: %s. Unverifiable quotes dropped: %d." % (
                r["facts"] if r["facts"] is not None else "not saved", kinds, r["planted"], r["dropped"]))
            L.append("")
    L += ["Pick 3 to 5 of these per chapter at most. Fixing everything flattens the chapter into a different machine pattern.",
          "This is a mechanical review. The human read of every chapter against its brief is still not done."]
    return "\n".join(L) + "\n"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", default="warm-enough")
    ap.add_argument("--chapters", required=True, help="example: 10,20,11 or 10-12")
    ap.add_argument("--votes", type=int, default=3)
    ap.add_argument("--models", default="")
    ap.add_argument("--no-facts", action="store_true")
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
        log("NVIDIA_API_KEY is not set (map secret NVIDIA_API_KEY_VA in the workflow). Nothing done.")
        return 2
    try:
        import write_warm_enough as wm
    except Exception as e:
        wm = None
        log("book checker not importable:", e)
    locked = {norm(x) for x in getattr(wm, "LOCKED", {})} if wm is not None else set()
    contracts = load_contracts(book)
    log("must contracts loaded: %d, locked lines: %d" % (len(contracts), len(locked)))
    models = [m.strip() for m in a.models.split(",") if m.strip()] or MODELS
    client = None if a.dry_run else Client(key, models)
    results = []
    for n in parse_chapters(a.chapters):
        if client is not None and not client.alive():
            log("no live model left, stopping")
            break
        r = review_chapter(wm, client, book, n, contracts, max(1, a.votes), not a.no_facts, a.dry_run, sorted(locked))
        if r:
            results.append(r)
    report = render(results, a, models)
    print("\n" + report)
    summ = os.environ.get("GITHUB_STEP_SUMMARY")
    if summ:
        with open(summ, "a", encoding="utf-8") as f:
            f.write(report)
    if not a.dry_run:
        sd = book / "stamps"
        sd.mkdir(exist_ok=True)
        (sd / ("CHAPTER_REVIEW_%s_run%s.md" % (datetime.date.today().isoformat(), os.environ.get("GITHUB_RUN_ID", "local")))).write_text(report, encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
