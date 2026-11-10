#!/usr/bin/env python3
"""
review_canary.py - SELF-TEST for the continuity check in scripts/chapter_review.py. It never changes a chapter file.
(2026-11-06, free only: NVIDIA NIM models, secret NVIDIA_API_KEY_VA.)

WHY: chapter_review.py says "no contradictions" or lists some. Nobody knows if a quiet report means a clean chapter or a
blind checker. The technique is published (FlawedFictions, COLM 2025; the "CanonBench" name used in the first version could
not be found and is not credited): plant KNOWN errors and see how many the checker finds, and also feed it harmless
re-wordings to see how often it raises a false alarm.

WHAT IT DOES (all in memory, the chapter on disk is never written)
  1. Loads the ledger of earlier chapters (stamps/FACTS_chNN.json, needs at least one earlier chapter).
  2. Runs the real check on the untouched chapter. Whatever it already flags is the BASELINE and is not counted.
  3. INJECTIONS: for K ledger facts (kinds time, knowledge, prop, place, body, relationship) a model rewrites one
     paragraph of the chapter so it contradicts that fact with the smallest possible change. The check is run again.
     Caught = the check flags that paragraph and did not flag it in the baseline.
  4. TWINS: for K other paragraphs a model re-words the paragraph with the same meaning (no new facts). If the check
     flags that twin paragraph, it is a FALSE ALARM.
  5. Report: recall, false alarm rate, and every before/after text so a human can verify each injection was real.

HONEST LIMITS (the report repeats them)
  * Small numbers (K is 12 by default, one chapter). The report gives Wilson 95 percent intervals and says how
    strong the evidence is. Pool several chapters before relying on a recall figure (30 or more tests).
  * The injections are written by the same kind of free models that do the checking. An injection can fail to be a real
    contradiction. That is why every before/after pair is printed. Judge a few by eye.
  * The ledger can only catch what it contains.

2026-11-09/10 fix: chapter_review.check_conflicts now returns four values and needs at least MIN_CONFLICT_REPLIES of the 3
replies for a verdict. This canary unpacked three values and would have crashed; it now unpacks four, and a check run where
fewer than that many replies came back is SKIPPED (no verdict) instead of being counted as "missed" or "quiet". Tested with a
stand-in model: a healthy run caught 3 of 3 and raised 0 false alarms; a run with only 1 of 3 replies stops safely.

USAGE (repo root; the earlier chapters' FACTS files must be present in novels/<book>/stamps)
  python scripts/review_canary.py --book warm-enough --chapter 11 --injections 12 --seed 7
"""
import argparse
import datetime
import os
import random
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
sys.path.insert(0, str(ROOT))

import chapter_review as cr

INJECT_KINDS = ["time", "knowledge", "prop", "place", "body", "relationship"]

SYS_EDIT = (
    "You edit fiction for a test. Answer with JSON only, no other text. Never add commentary. Keep the writer's voice, "
    "names and sentence style."
)

INJECT_PROMPT = (
    "ESTABLISHED FACT from an earlier chapter (kind %(kind)s): %(fact)s\n\nPARAGRAPH from a later chapter:\n%(para)s\n\n"
    "Rewrite the paragraph so that it now CONTRADICTS the established fact, with the smallest change you can make "
    "(change a few words, not the whole paragraph). Keep the length within about 15 percent. The contradiction must be "
    "clear to a careful reader, not hinted. Return JSON: {\"paragraph\": \"the full rewritten paragraph\", "
    "\"what_now_conflicts\": \"one short sentence\"}."
)

TWIN_PROMPT = (
    "PARAGRAPH:\n%(para)s\n\nRe-word this paragraph with exactly the same meaning and the same facts. Do not add, remove or "
    "change any fact, name, number, time, object or event. Change only wording. Keep the length within about 15 percent. "
    "Return JSON: {\"paragraph\": \"the full re-worded paragraph\"}."
)


def eligible(paras, locked):
    """Paragraphs of at least 25 words that contain no locked line."""
    out = []
    for i, p in enumerate(paras, 1):
        if len(p.split()) < 25:
            continue
        np_ = cr.norm(p)
        if any(l and l in np_ for l in locked):
            continue
        out.append(i)
    return out


def length_ok(old, new, lo, hi):
    a, b = len(old.split()), len(new.split())
    return a > 0 and lo <= b / a <= hi


def flagged_paras(client, stamps, n, paras):
    kept, dropped, replies, _compared = cr.check_conflicts(client, stamps, n, paras)
    return {e["para"]: e for e in kept}, replies


def ask_paragraph(client, prompt):
    data, model = client.ask(prompt, temperature=0.4, system=SYS_EDIT)
    if not isinstance(data, dict):
        return None, None
    new = str(data.get("paragraph", "")).strip()
    return new or None, cr.one_line(data.get("what_now_conflicts", ""))[:200]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--book", default="warm-enough")
    ap.add_argument("--chapter", type=int, required=True)
    ap.add_argument("--injections", type=int, default=12)
    ap.add_argument("--seed", type=int, default=7)
    ap.add_argument("--models", default="")
    a = ap.parse_args()

    if any(m in a.book for m in cr.PUBLISHED_MARKERS):
        cr.log("REFUSED: %s is a published book." % a.book)
        return 3
    book = ROOT / "novels" / a.book
    if (book / "PUBLISHED.md").exists() or (book / "FROZEN.md").exists():
        cr.log("REFUSED: %s is marked published or frozen." % a.book)
        return 3
    key = os.environ.get("NVIDIA_API_KEY", "")
    if not key:
        cr.log("NVIDIA_API_KEY is not set (map secret NVIDIA_API_KEY_VA in the workflow). Nothing done.")
        return 2
    path = book / "chapters" / ("chapter_%02d.md" % a.chapter)
    if not path.exists():
        cr.log("chapter file not found: %s" % path)
        return 4
    stamps = book / "stamps"
    rows = [r for r in cr.earlier_fact_rows(stamps, a.chapter) if r["kind"] in INJECT_KINDS and r["fact"]]
    if not cr.earlier_facts(stamps, a.chapter):
        cr.log("No FACTS files for earlier chapters found in %s. Run chapter_review on the earlier chapters first "
               "(or pass the review branch as facts_branch). Nothing done." % stamps)
        return 4
    if len(rows) < 1:
        cr.log("Earlier chapters have no facts of the kinds that can be tested. Nothing done.")
        return 4

    try:
        import write_warm_enough as wm
    except Exception as e:
        wm = None
        cr.log("book checker not importable:", e)
    locked = {cr.norm(x) for x in getattr(wm, "LOCKED", {})} if wm is not None else set()

    body = cr.body_of(path.read_text(encoding="utf-8"))
    paras = cr.paragraphs(body)
    elig = eligible(paras, locked)
    rng = random.Random(a.seed)
    k = max(1, min(a.injections, len(rows), len(elig) // 2))
    if k < a.injections:
        cr.log("note: using %d injections (limited by facts or eligible paragraphs)" % k)
    facts = rng.sample(rows, k)
    pool = elig[:]
    rng.shuffle(pool)
    inj_paras = pool[:k]
    twin_paras = pool[k:2 * k]
    models = [m.strip() for m in a.models.split(",") if m.strip()] or cr.MODELS
    client = cr.Client(key, models)
    cr.log("== canary on chapter %02d: %d paragraphs, %d eligible, %d injections, %d twins" % (
        a.chapter, len(paras), len(elig), len(inj_paras), len(twin_paras)))

    base, base_replies = flagged_paras(client, stamps, a.chapter, paras)
    cr.log("   baseline: %d paragraph(s) already flagged, %d reply(ies)" % (len(base), base_replies))
    if base_replies < cr.MIN_CONFLICT_REPLIES:
        cr.log("The checker gave fewer than %d usable replies on the untouched chapter, so the test cannot say anything. Stopping." % cr.MIN_CONFLICT_REPLIES)
        return 5

    inj_results, skipped = [], 0
    for fact, pno in zip(facts, inj_paras):
        old = paras[pno - 1]
        new, what = ask_paragraph(client, INJECT_PROMPT % {"kind": fact["kind"], "fact": fact["fact"], "para": old})
        if not new or cr.norm(new) == cr.norm(old) or not length_ok(old, new, 0.7, 1.4):
            skipped += 1
            cr.log("   injection at P%d skipped: model reply unusable" % pno)
            continue
        test = paras[:]
        test[pno - 1] = new
        flags, replies = flagged_paras(client, stamps, a.chapter, test)
        if replies < cr.MIN_CONFLICT_REPLIES:
            skipped += 1
            cr.log("   injection at P%d skipped: only %d of 3 checker replies came back, so no verdict" % (pno, replies))
            continue
        caught = pno in flags and pno not in base
        extra = sorted(p for p in flags if p != pno and p not in base)
        inj_results.append({"para": pno, "fact": fact, "old": old, "new": new, "what": what, "caught": caught,
                            "extra": extra, "replies": replies})
        cr.log("   injection %s at P%d (%s): %s" % (len(inj_results), pno, fact["kind"], "CAUGHT" if caught else "missed"))

    twin_results, twin_skipped = [], 0
    for pno in twin_paras:
        old = paras[pno - 1]
        new, _ = ask_paragraph(client, TWIN_PROMPT % {"para": old})
        if not new or cr.norm(new) == cr.norm(old) or not length_ok(old, new, 0.85, 1.15):
            twin_skipped += 1
            cr.log("   twin at P%d skipped: model reply unusable" % pno)
            continue
        test = paras[:]
        test[pno - 1] = new
        flags, replies = flagged_paras(client, stamps, a.chapter, test)
        if replies < cr.MIN_CONFLICT_REPLIES:
            twin_skipped += 1
            cr.log("   twin at P%d skipped: only %d of 3 checker replies came back, so no verdict" % (pno, replies))
            continue
        alarm = pno in flags and pno not in base
        extra = sorted(p for p in flags if p != pno and p not in base)
        twin_results.append({"para": pno, "old": old, "new": new, "alarm": alarm, "extra": extra, "replies": replies})
        cr.log("   twin at P%d: %s" % (pno, "FALSE ALARM" if alarm else "quiet"))

    report = render(a, paras, base, inj_results, twin_results, skipped, twin_skipped, models)
    print("\n" + report)
    summ = os.environ.get("GITHUB_STEP_SUMMARY")
    if summ:
        with open(summ, "a", encoding="utf-8") as f:
            f.write(report)
    stamps.mkdir(exist_ok=True)
    name = "CANARY_%s_run%s.md" % (datetime.date.today().isoformat(), os.environ.get("GITHUB_RUN_ID", "local"))
    (stamps / name).write_text(report, encoding="utf-8")
    return 0


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    cen = (p + z * z / (2 * n)) / d
    h = z * ((p * (1 - p) / n + z * z / (4 * n * n)) ** 0.5) / d
    return (max(0.0, cen - h), min(1.0, cen + h))


def evidence(n):
    if n < 10:
        return "too few tests to say anything (under 10)"
    if n < 30:
        return "weak evidence (10 to 29 tests); pool more chapters"
    return "usable evidence (30 or more tests)"


def render(a, paras, base, inj, twins, skipped, twin_skipped, models):
    caught = sum(1 for r in inj if r["caught"])
    alarms = sum(1 for r in twins if r["alarm"])
    L = ["# Review canary (%s)" % cr.ist_now(), "",
         "Book: %s, chapter %02d, seed %d. The chapter file was not changed; all edits were made in memory." % (a.book, a.chapter, a.seed),
         "Models: %s." % ", ".join(models), ""]
    if inj:
        lo, hi = wilson(caught, len(inj))
        L.append("**Recall: %d of %d planted contradictions caught (%.0f%%, 95%% CI %.0f-%.0f%%)** (%d injection(s) skipped because the model reply was unusable)." % (caught, len(inj), 100 * caught / len(inj), 100 * lo, 100 * hi, skipped))
    else:
        L.append("**Recall: no usable injection was produced.**")
    if twins:
        lo2, hi2 = wilson(alarms, len(twins))
        L.append("**False alarms: %d of %d harmless re-wordings flagged (%.0f%%, 95%% CI %.0f-%.0f%%)** (%d twin(s) skipped)." % (alarms, len(twins), 100 * alarms / len(twins), 100 * lo2, 100 * hi2, twin_skipped))
    else:
        L.append("**False alarms: no usable twin was produced.**")
    L.append("Baseline: the untouched chapter already had %d flagged paragraph(s)%s; those are not counted." % (
        len(base), (" (P" + ", P".join(str(p) for p in sorted(base)) + ")") if base else ""))
    L.append("Evidence strength: injections - %s; twins - %s." % (evidence(len(inj)), evidence(len(twins))))
    L += ["", "How to read this (accepted practice for detectors, RAID, ACL 2024): judge the checker by its recall at a false-alarm "
          "rate of at most 5 percent. Low recall means a quiet continuity report cannot be trusted. Each false alarm is noise "
          "in the report. Do not rely on one chapter: pool at least 30 injections and 30 twins by running several chapters.", ""]
    for i, r in enumerate(inj, 1):
        L += ["## Injection %d at P%d: %s" % (i, r["para"], "CAUGHT" if r["caught"] else "MISSED"),
              "Fact used (ch%02d, %s): %s" % (r["fact"]["ch"], r["fact"]["kind"], r["fact"]["fact"]),
              "Model says the new conflict is: %s" % r["what"],
              "Before: %s" % cr.one_line(r["old"])[:600],
              "After: %s" % cr.one_line(r["new"])[:600]]
        if r["extra"]:
            L.append("Other paragraphs newly flagged in this run: %s" % ", ".join("P%d" % p for p in r["extra"]))
        L.append("")
    for i, r in enumerate(twins, 1):
        L += ["## Twin %d at P%d: %s" % (i, r["para"], "FALSE ALARM" if r["alarm"] else "quiet"),
              "Before: %s" % cr.one_line(r["old"])[:600],
              "After: %s" % cr.one_line(r["new"])[:600]]
        if r["extra"]:
            L.append("Other paragraphs newly flagged in this run: %s" % ", ".join("P%d" % p for p in r["extra"]))
        L.append("")
    L += ["Check by eye: do the Before/After pairs of the injections really contradict the fact? If not, a MISSED line "
          "is the injection's fault, not the checker's.",
          "Limits: small K, injections written by the same kind of free models, only facts in the ledger can be tested."]
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    sys.exit(main())
