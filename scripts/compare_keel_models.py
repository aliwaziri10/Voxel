#!/usr/bin/env python3
"""
compare_keel_models.py - side-by-side model test for Keel and Comb.

Runs ONE chapter's real prompt (same canon, voice guide, brief, limits as the live writer) through each
model in --models, one draft per model, then saves every draft and a metrics table to
novels/larkmere-book-3/model_tests/. It never writes to chapters/, never edits the live writer and
never runs the repair loop or the brief check, so the comparison is one raw draft per model.

Usage:
  python scripts/compare_keel_models.py --models "google/gemma-4-31b-it:free,thinkingmachines/inkling:free"
  python scripts/compare_keel_models.py --chapter 1 --models "..." --no-commit
"""
import argparse
import re
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import write_keel_and_comb as k  # noqa: E402

w = k.w

FILLER = (r"\b(nice|good|great|bad|thing|things|stuff|big|small|lovely|beautiful|wonderful|amazing|"
          r"very|really|just|quite|suddenly|seemed|felt|looked|moved|went|got)\b")


def slug(m):
    return re.sub(r"[^a-z0-9]+", "-", m.lower()).strip("-")


def metrics(body):
    nw = w.words(body)
    toks = re.findall(r"[a-z']+", body.lower())
    filler = len(re.findall(FILLER, body, re.I))
    sents = [s for s in re.split(r"(?<=[.!?])[\s\"\u201d\u2019']+", body) if s.strip()]
    lens = [len(s.split()) for s in sents]
    mean = sum(lens) / len(lens) if lens else 0
    sd = (sum((x - mean) ** 2 for x in lens) / len(lens)) ** 0.5 if lens else 0
    return {
        "words": nw,
        "filler_per_1k": round(1000.0 * filler / max(nw, 1), 1),
        "distinct": round(len(set(toks)) / max(len(toks), 1), 3),
        "sent_mean": round(mean, 1),
        "sent_sd": round(sd, 1),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--models", required=True, help="comma-separated OpenRouter model ids")
    ap.add_argument("--chapter", type=int, default=1)
    ap.add_argument("--no-commit", action="store_true")
    args = ap.parse_args()
    n = args.chapter
    models = [m.strip() for m in args.models.split(",") if m.strip()]
    if not models:
        raise SystemExit("STOP: no models given.")

    system = w.read(k.BOOK / "WRITER_COMMAND.md")
    brief, pov, season = w.load_brief(n)
    try:
        next_head = w.read(k.BOOK / "briefs" / ("ch%02d.md" % (n + 1))).split("\n", 1)[0]
    except Exception:
        next_head = None
    prev, prev_label = w.previous_text(n)
    user = w.build_prompt(n, brief, pov, season, prev, prev_label, w.voice_sample(n), next_head)
    print("[compare] chapter %d | %s | %s | prompt %d words | %d model(s)"
          % (n, pov, season, w.words(system) + w.words(user), len(models)))

    out_dir = k.BOOK / "model_tests"
    out_dir.mkdir(parents=True, exist_ok=True)
    rows = []
    for m in models:
        print("[compare] model: %s" % m)
        w.WRITER_MODEL = m  # the pinned payload wrapper reads this global on every call
        t0 = time.time()
        try:
            raw = w.call_chapter(system, user)
        except SystemExit as e:
            print("[compare]   stopped: %s" % e)
            rows.append((m, None, "STOPPED: %s" % str(e)[:120], [], []))
            break
        except Exception as e:
            kind, detail = w.classify_error(e)
            print("[compare]   FAILED (%s): %s" % (kind, detail))
            rows.append((m, None, "FAILED (%s): %s" % (kind, detail[:120]), [], []))
            continue
        body, fixes = w.fix_mechanical(w.clean_body(raw))
        hard, soft = w.check(body, n, brief)
        mt = metrics(body)
        secs = int(time.time() - t0)
        head = "<!-- model: %s | chapter %d | %d words | %ds | hard=%d soft=%d | auto-fix: %s -->\n\n" % (
            m, n, mt["words"], secs, len(hard), len(soft), "; ".join(fixes) or "none")
        (out_dir / ("ch%02d_%s.md" % (n, slug(m)))).write_text(head + body + "\n", encoding="utf-8")
        print("[compare]   %d words, hard=%d soft=%d, %ds" % (mt["words"], len(hard), len(soft), secs))
        rows.append((m, mt, "ok", hard, soft))

    lines = ["# Model comparison: chapter %d (%s)" % (n, pov), "",
             "One raw draft per model, same prompt as the live writer. No repair loop, no brief check. "
             "Lower filler per 1,000 words is better. Higher sentence-length spread is more human. Read the drafts before choosing.", "",
             "| model | status | words | hard | soft | filler/1k | distinct | sentence mean | sentence spread |",
             "|---|---|---|---|---|---|---|---|---|"]
    for m, mt, status, hard, soft in rows:
        if mt:
            lines.append("| `%s` | ok | %d | %d | %d | %s | %s | %s | %s |" % (
                m, mt["words"], len(hard), len(soft), mt["filler_per_1k"], mt["distinct"], mt["sent_mean"], mt["sent_sd"]))
        else:
            lines.append("| `%s` | %s | | | | | | | |" % (m, status))
    lines.append("")
    for m, mt, status, hard, soft in rows:
        if mt:
            lines.append("## %s" % m)
            lines.append("- HARD: %s" % ("; ".join(hard) if hard else "none"))
            lines.append("- soft: %s" % ("; ".join(soft) if soft else "none"))
            lines.append("")
    (out_dir / ("COMPARE_ch%02d.md" % n)).write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))
    if not args.no_commit:
        w.checkpoint(out_dir, "Keel and Comb: model comparison for chapter %d (test drafts, not part of the book)" % n)
    return 0 if any(r[1] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
