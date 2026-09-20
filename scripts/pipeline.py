#!/usr/bin/env python3
"""
pipeline.py — Orchestrator for the Voxel novel production pipeline.

Reads one book's book_config.json, reports its current stage, and runs
the correct existing script for that stage -- in order, never skipping
a stage, never touching a locked book.

HARD LOCK: Book 1 (Where the Frost Doesn't Reach), Book 2, and Book 3
of the Amity Falls Series are published and permanently locked. This
script refuses to run against them, full stop -- see LOCKED_BOOK_IDS
below. This is not a config flag someone can flip; it's checked before
anything else in main().

Stages and gates are defined in book_config.py. This file only knows
how to DRIVE a book through them -- it does not re-implement the
editorial charter's judgment calls, and it does not auto-set any
manual_gates value. Those are set by hand (or by an AI session doing
the real work) in the book's own book_config.json.

Usage:
    python pipeline.py <path/to/book_config.json> --status
    python pipeline.py <path/to/book_config.json> --advance

--status   prints current stage, unmet gates, and what --advance would
           do next. Always safe to run, changes nothing.
--advance  attempts to run the current stage's script (or check its
           gates) and, on success, moves the book to the next stage.
           Refuses and explains itself if a gate is unmet or a
           mechanical check fails.

2026-09-20 fix: the mechanical_qa and manuscript_build stages called
manuscript_qa.py and build_manuscript.py with flags those scripts do
not define (--chapters-dir/--out for manuscript_qa.py, which actually
takes --chapters/--report; --chapters-dir for build_manuscript.py,
which actually takes --chapters). Both would have failed argparse on
first real use -- caught by reading all three files together, before
any book_config.json existed to trigger it live. Now calls each script
with its real flag names; nothing else about either stage changed.
"""
import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from book_config import BookConfig, BookConfigError, STAGES  # noqa: E402

# Permanently locked. Do not add a config flag to bypass this -- if a
# book needs to come off this list, that's a decision Zia makes by
# editing this source file directly, not something this tool exposes.
LOCKED_BOOK_IDS = {
    "where-the-frost-doesnt-reach",
    "amity-falls-book-2",
    "amity-falls-book-3",
}

SCRIPTS_DIR = os.path.dirname(os.path.abspath(__file__))


def die(msg):
    print(f"REFUSED: {msg}", file=sys.stderr)
    sys.exit(1)


def check_not_locked(cfg):
    book_id = cfg.data.get("book_id", "")
    for locked in LOCKED_BOOK_IDS:
        if locked in book_id or book_id in locked:
            die(
                f"'{book_id}' matches a permanently locked, published book "
                f"({locked}). This pipeline will never run against Books "
                f"1-3 of the Amity Falls Series. Nothing was touched."
            )


def append_handoff(book_dir, message):
    """Best-effort append to the book's own HANDOFF.md, matching the
    repo's existing convention of a timestamped log line per action."""
    handoff_path = os.path.join(book_dir, "HANDOFF.md")
    if not os.path.exists(handoff_path):
        return  # don't invent a HANDOFF.md structure for a book that
                 # doesn't have one yet -- that's a human/editorial file
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    with open(handoff_path, "a", encoding="utf-8") as f:
        f.write(f"\n- [{ts}] pipeline.py: {message}")


def run_stage_script(cfg):
    """Run whatever mechanical script corresponds to the CURRENT stage.
    Returns True if the stage's work is done and it's safe to advance,
    False if it isn't (with an explanation already printed)."""
    stage = cfg.stage
    book_dir = os.path.dirname(os.path.abspath(cfg.path))
    chapters_dir = os.path.join(book_dir, os.path.basename(cfg.data["chapters_dir"]))

    if stage == "outline":
        beat_map = os.path.join(book_dir, "beat_map.md")
        if not os.path.exists(beat_map):
            print(f"Missing {beat_map}. Outline stage is manual (voxel_cli.py "
                  f"beat-map step) -- nothing for pipeline.py to run yet.")
            return False
        print(f"Found {beat_map}. Outline stage looks complete.")
        return True

    if stage == "drafting":
        if not os.path.isdir(chapters_dir):
            print(f"Missing chapters dir {chapters_dir}.")
            return False
        chapters = sorted(f for f in os.listdir(chapters_dir) if f.endswith(".md"))
        print(f"Found {len(chapters)} chapter file(s) in {chapters_dir}.")
        print("Drafting is manual. Set manual_gates when all chapters exist "
              "and you're ready to start the editorial review pass.")
        return False  # drafting has no gate defined, but we never
                       # auto-advance past creative work either -- the
                       # human runs --advance again once ready.

    if stage == "editorial_review":
        unmet = cfg.unmet_gates("editorial_review")
        if unmet:
            print(
                f"Manual editorial gates not yet set for '{cfg.data['book_id']}': "
                f"{unmet}\n"
                f"Per EDITORIAL_CHARTER.md, this stage is the strict sequential "
                f"continuity/voice/canon read plus the banned-word and hedge "
                f"sweeps. It is never automated. Do the work, log it in this "
                f"book's HANDOFF.md as usual, then set these to true in "
                f"{cfg.path}."
            )
            return False
        print("All editorial_review gates are set.")
        return True

    if stage == "mechanical_qa":
        qa_script = os.path.join(SCRIPTS_DIR, "manuscript_qa.py")
        if not os.path.exists(qa_script):
            die(f"Expected {qa_script} to exist (added to the repo already).")
        report_path = os.path.join(book_dir, "QA_REPORT.md")
        # 2026-09-20 fix: manuscript_qa.py's real flags are --chapters and
        # --report (confirmed by reading its argparse block directly) --
        # --chapters-dir/--out (used here before) do not exist on that
        # script and would have failed with "unrecognized arguments".
        cmd = [sys.executable, qa_script, "--chapters", chapters_dir,
               "--report", report_path]
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(result.stderr, file=sys.stderr)
            print("manuscript_qa.py exited non-zero -- treating as unresolved.")
            return False
        confirmed_fix_count = result.stdout.count("CONFIRMED-FIX")
        if confirmed_fix_count > 0:
            print(f"{confirmed_fix_count} CONFIRMED-FIX item(s) outstanding "
                  f"in {report_path}. Fix them and re-run --advance.")
            return False
        print("QA clean: 0 CONFIRMED-FIX items.")
        return True

    if stage == "manuscript_build":
        build_script = os.path.join(SCRIPTS_DIR, "build_manuscript.py")
        out_docx = os.path.join(book_dir, f"{cfg.data['book_id']}.docx")
        # 2026-09-20 fix: build_manuscript.py's real flag is --chapters
        # (confirmed by reading its argparse block directly), not
        # --chapters-dir (used here before, which does not exist on that
        # script and would have failed with "unrecognized arguments" /
        # "the following arguments are required: --chapters").
        cmd = [
            sys.executable, build_script,
            "--chapters", chapters_dir,
            "--title", cfg.data["title"],
            "--series", cfg.data["series"],
            "--book-number", str(cfg.data["book_number"]),
            "--author", cfg.data["author"],
            "--trim", cfg.data["trim"],
            "--out", out_docx,
        ]
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(result.stderr, file=sys.stderr)
            return False
        print(f"Manuscript built: {out_docx}")
        return True

    if stage == "cover_build":
        cover_script = os.path.join(SCRIPTS_DIR, "build_cover.py")
        front_art = cfg.data.get("cover", {}).get("front_art_path")
        back_art = cfg.data.get("cover", {}).get("back_art_path")
        if not front_art or not back_art:
            print(
                "book_config.json is missing cover.front_art_path / "
                "cover.back_art_path. This pipeline never generates cover "
                "art -- add the paths to your existing art assets and "
                "re-run --advance."
            )
            return False
        out_pdf = os.path.join(book_dir, f"{cfg.data['book_id']}_cover.pdf")
        cmd = [
            sys.executable, cover_script,
            "--front-art", front_art, "--back-art", back_art,
            "--trim", cfg.data["trim"],
            "--spine-title", cfg.data["title"],
            "--out", out_pdf,
        ]
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(result.stderr, file=sys.stderr)
            return False
        print(f"Cover built: {out_pdf}")
        return True

    if stage == "kdp_metadata":
        meta_script = os.path.join(SCRIPTS_DIR, "kdp_metadata.py")
        out_md = os.path.join(book_dir, "KDP_METADATA.md")
        cmd = [sys.executable, meta_script, "--config", cfg.path, "--out", out_md]
        print(f"Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)
        print(result.stdout)
        if result.returncode != 0:
            print(result.stderr, file=sys.stderr)
            return False
        if "OPEN ITEM" in result.stdout:
            print(f"Metadata package written to {out_md} but has open items "
                  f"-- fill them into book_config.json's \"kdp\" section and "
                  f"re-run.")
            return False
        return True

    if stage == "ready_for_upload":
        unmet = cfg.unmet_gates("ready_for_upload")
        if unmet:
            print(f"Final Publisher sign-off gates unmet: {unmet}")
            return False
        print("All final sign-off gates set. Ready for manual KDP upload.")
        return True

    if stage == "published":
        print(f"'{cfg.data['book_id']}' is already marked published. Nothing to do.")
        return False

    die(f"No handler for stage '{stage}'.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("config", help="Path to the book's book_config.json")
    group = ap.add_mutually_exclusive_group(required=True)
    group.add_argument("--status", action="store_true")
    group.add_argument("--advance", action="store_true")
    args = ap.parse_args()

    try:
        cfg = BookConfig.load(args.config)
    except BookConfigError as e:
        die(str(e))
        return

    check_not_locked(cfg)

    print(f"book_id: {cfg.data['book_id']}")
    print(f"title:   {cfg.data['title']}")
    print(f"stage:   {cfg.stage}  ({cfg.stage_index + 1}/{len(STAGES)})")

    if args.status:
        unmet = cfg.unmet_gates()
        if unmet:
            print(f"unmet gates: {unmet}")
        else:
            print("no unmet gates -- run --advance to attempt this stage.")
        return

    # --advance
    try:
        ready = run_stage_script(cfg)
    except BookConfigError as e:
        die(str(e))
        return

    if not ready:
        print("Stage not complete -- book_config.json stage unchanged.")
        return

    current_idx = cfg.stage_index
    if current_idx == len(STAGES) - 1:
        print("Already at the final stage.")
        return
    next_stage = STAGES[current_idx + 1]
    note = f"advanced by pipeline.py after completing '{cfg.stage}'"
    try:
        cfg.advance_to(next_stage, note=note)
    except BookConfigError as e:
        die(str(e))
        return
    cfg.save()
    book_dir = os.path.dirname(os.path.abspath(cfg.path))
    append_handoff(book_dir, f"stage {STAGES[current_idx]} -> {next_stage}")
    print(f"Advanced: {STAGES[current_idx]} -> {next_stage}. Config saved.")


if __name__ == "__main__":
    main()
