#!/usr/bin/env python3
"""
voxel_cli.py - the one-command entry point for Voxel Publications.

This is what "one command, one book ready" means in practice:

  Picture book (like Luna):
    python voxel_cli.py book \
        --concept "A gentle bedtime story about a girl named Mira who..." \
        --pages 26 --trim 8.5x11 --series luna

  Novel chapter / sequel (like Where the Frost Doesn't Reach, Amity Falls):
    python voxel_cli.py novel \
        --series amity-falls --book "Amity Falls Book 2" \
        --chapters 45 \
        --brief "Book 2 picks up two years after the wedding in Book 1..."

  Batch images from one reference photo (Phase 9, NVIDIA FLUX.1-Kontext):
    python voxel_cli.py images \
        --reference luna_reference.png \
        --prompts "Luna waving at the beach" "Luna reading a book" \
        --out-dir output_images/luna_batch

  Audit already-written chapters (2026-09-15, read-only scan, no rewrite):
    python voxel_cli.py audit \
        --book "Amity Falls Book 2" \
        --min-words 2000 --max-words 2634

What it does NOT do yet (see HANDOFF.md "Known gaps"):
  - It does not auto-decide the story concept for you. You give it a
    concept/brief; it does not invent the creative direction from nothing.
  - It does not upload to KDP. That's still the manual walk-through in
    build_book.py's original HANDOFF.md steps 4-5.
  - Image generation for novels (cover art) is not wired into `novel`
    automatically; use the `images` command separately if you want cover
    art from a reference photo.
  - The `audit` command does NOT check grammar, plot logic, pacing,
    continuity, foreshadowing/payoff, or character consistency. Those have
    no reliable automated check and are done as a manual editorial read
    against the book's beat map. `audit` only catches word count, em-dash
    count, and AI-tell pattern hits — the three things that ARE reliably
    checkable by script.

Phase 9: novel generation now writes a whole-book chapter beat map (see
content_provider.generate_beat_map / story_bible.save_beat_map) BEFORE
writing any prose, and each chapter is written from its own specific beat
instead of just the top-level brief + "continue naturally". This is what
keeps a 45-chapter novel from losing the plot partway through. Also added
the `images` command for NVIDIA-based batch generation from one reference
photo (see nvidia_image_provider.py).

2026-09-15: added the `audit` command. It reads already-written chapter
files (does not regenerate or rewrite them) and reports word count,
em-dash count, and an offline humanizer.scan() AI-tell score per chapter,
writing a chapters_audit_report.md file next to the chapters/ folder. This
exists because story_bible.py does NOT have any word-count/em-dash checker
built in (checked directly against the live file — no such function
exists there despite it being assumed present in an earlier session).

2026-09-15 (fix): `audit`'s path resolution originally assumed the same
novels/<series>/<book-slug>/ layout that `novel` writes new chapters into.
The Amity Falls books were actually written directly under
novels/<book-slug>/ (no series-name subfolder) — confirmed by a real
failed run against amity-falls-book-2. `audit` now takes only --book (no
--series) and resolves straight to novels/<book-slug>/, with a fallback
to the old nested novels/<series>/<book-slug>/ layout in case a future
book actually uses it.

2026-09-19 (fix): `novel` previously generated each chapter once and
wrote whatever came back, with no word-count check at all - Book 2/3's
own PROOFREAD_REPORT.md showed chapters as short as 825 words against
the 2000-2300 target, entirely uncaught. `cmd_novel` now checks the word
count after generation+humanizing and retries (up to 2 extra attempts,
each with a stronger "expand, previous attempt was short" instruction)
before writing the file, falling back to the longest attempt with a
clear warning if it's still short after retries. Added --min-words/
--max-words flags (default 2000/2300) matching `audit`'s.

Required environment variables (same as before, nothing new):
    OPENROUTER_API_KEY
    GEMINI_API_KEY   (only needed for the 'book' command's illustrations)
    NVIDIA_API_KEY   (only needed for the 'images' command, or if you want
                      NVIDIA text generation instead of OpenRouter)

Required local packages (same as before, nothing new):
    pip install reportlab requests --break-system-packages

This script assumes it's run from inside a local clone of this repo (so
relative imports of content_provider/image_provider/build_book work, and
so the git commands below can commit+push using your machine's own git
login - no GitHub token is handled by this script).
"""

import argparse
import subprocess
from pathlib import Path

import content_provider
import humanizer
import story_bible


NOVELS_DIR = Path("novels")


def cmd_book(args):
    """Generate a full picture book: manuscript -> humanize -> images ->
    print-ready PDFs -> project.json. Wraps the existing build_book.py
    pipeline instead of duplicating it, and adds the two things Phase 4
    was missing: continuity with prior books, and an AI-tell pass."""
    import build_book  # existing Phase 4 pipeline, imported not rewritten

    continuity = story_bible.continuity_prompt_block(args.series) if args.series else ""

    print(f"[voxel] Generating manuscript ({args.pages} pages)...")
    pages = content_provider.generate_manuscript(args.concept, args.pages, continuity_block=continuity)

    print("[voxel] Running humanizer pass (removing AI tells)...")
    pages = humanizer.humanize_manuscript(pages, content_provider.call_raw)
    flagged = [p for p in pages if p.get("_humanizer", {}).get("integrity_gate_failed")]
    if flagged:
        print(f"[voxel] WARNING: {len(flagged)} page(s) failed the integrity gate "
              "(a rewrite would have dropped a fact) - kept original text for those. "
              "Check project.json's '_humanizer' field per page.")

    trim_width_in, trim_height_in = build_book.TRIM_SIZES[args.trim]
    safe_name = "".join(c if c.isalnum() or c in " -_" else "" for c in args.concept).strip().replace(" ", "_")[:60]
    run_dir = build_book.OUTPUT_DIR / safe_name

    print("[voxel] Generating illustrations...")
    style = build_book.COLORING_BOOK_STYLE_SUFFIX if args.coloring_book else build_book.BOOK_STYLE_SUFFIX
    image_files = build_book.generate_all_images(
        pages, run_dir / "images", filename_prefix="page",
        width=1600, height=1600, style_suffix=style,
        number_key="page_number", seed_base=100,
    )

    print("[voxel] Building print-ready interior PDF...")
    interior_path = run_dir / f"{safe_name}_interior.pdf"
    build_book.build_interior_pdf(pages, image_files, trim_width_in, trim_height_in, interior_path)

    print("[voxel] Building print-ready cover PDF...")
    cover_path = run_dir / f"{safe_name}_cover.pdf"
    front_image = image_files[0] if image_files else None
    build_book.build_cover_pdf(args.concept[:40], len(pages), trim_width_in, trim_height_in, cover_path, paper=args.paper, front_image=front_image)

    print("[voxel] Writing project.json...")
    product_type = "coloring_book" if args.coloring_book else "illustrated_book"
    record = build_book.build_project_record(
        concept=args.concept, product_type=product_type,
        trim_width_in=trim_width_in, trim_height_in=trim_height_in,
        paper=args.paper, pages=pages, image_files=image_files,
        interior_path=interior_path, cover_path=cover_path, run_dir=run_dir,
    )
    build_book.write_project_json(record, run_dir)

    if args.series:
        summary = args.summary or f"({args.pages}-page picture book: {args.concept[:120]})"
        story_bible.register_book(args.series, safe_name, summary)
        print(f"[voxel] Registered '{safe_name}' in the '{args.series}' story bible for future sequels.")

    print()
    print("[voxel] Done. Output folder:")
    print(f"  {run_dir.resolve()}")
    print("[voxel] Next manual step: run the interior + cover PDFs through KDP's Print Previewer, then the KDP listing flow (see HANDOFF.md).")


def _generate_chapter_with_length_retry(chapter_number, chapter_brief, continuity_block,
                                         min_words, max_words, max_retries=2):
    """Generate a chapter, retrying (up to max_retries extra attempts) if it
    comes in under min_words. Each retry adds an explicit "the previous
    attempt was too short, expand this time" instruction on top of the
    normal brief, since just re-asking the same prompt tends to reproduce
    the same length. Returns (text, attempts_made, still_short: bool)."""
    best_text = None
    best_words = -1

    brief_for_attempt = chapter_brief
    for attempt in range(1, max_retries + 2):  # 1 initial + max_retries retries
        text = content_provider.generate_novel_chapter(
            chapter_number, brief_for_attempt, continuity_block=continuity_block,
            min_words=min_words, max_words=max_words,
        )
        word_count = len(text.split())

        if word_count > best_words:
            best_text, best_words = text, word_count

        if word_count >= min_words:
            return text, attempt, False

        if attempt <= max_retries:
            print(f"[voxel]   chapter {chapter_number} attempt {attempt} came in at "
                  f"{word_count}w (below {min_words}w floor) - retrying with expand instruction...")
            brief_for_attempt = (
                f"{chapter_brief}\n\nIMPORTANT: a previous attempt at this chapter came in at "
                f"only {word_count} words, well under the required {min_words}-{max_words} word "
                "range. Do not compress or summarize the events - give scenes more room "
                "(setting detail, interiority, dialogue beats) so the chapter reaches full "
                "length naturally. This is a hard requirement."
            )

    print(f"[voxel]   WARNING: chapter {chapter_number} still under {min_words}w after "
          f"{max_retries} retries (best attempt: {best_words}w). Keeping the longest attempt - "
          "flag this chapter for a manual expansion pass.")
    return best_text, max_retries + 1, True


def cmd_novel(args):
    """Generate N chapters of a novel/sequel, one file per chapter under
    novels/<series>/<book-slug>/, plus a compiled single manuscript file.

    Phase 9: before writing any prose, generates (or reuses, if this book
    already has one - e.g. a resumed run) a whole-book chapter beat map,
    so every chapter is written from ITS OWN specific beat instead of just
    the top-level brief + "continue naturally from last chapter". This is
    what keeps a long novel from losing the plot partway through - the
    outline is planned with the whole book in view before any chapter is
    drafted.

    Runs the humanizer pass per chapter, then checks the resulting word
    count against --min-words/--max-words and retries a short chapter
    (see _generate_chapter_with_length_retry) before writing the file.

    Commits+pushes at the end if --commit is passed (uses your machine's
    own git credentials)."""
    continuity = story_bible.continuity_prompt_block(args.series)
    book_slug = "".join(c if c.isalnum() or c in " -_" else "" for c in args.book).strip().replace(" ", "-").lower()
    out_dir = NOVELS_DIR / args.series / book_slug
    out_dir.mkdir(parents=True, exist_ok=True)

    beats = story_bible.load_beat_map(args.series, args.book)
    if beats and len(beats) == args.chapters:
        print(f"[voxel] Reusing existing beat map for '{args.book}' ({len(beats)} chapters) - "
              "this looks like a resumed run.")
    else:
        if beats:
            print(f"[voxel] Existing beat map for '{args.book}' has {len(beats)} chapters, "
                  f"but {args.chapters} were requested - generating a fresh one.")
        print(f"[voxel] Planning whole-book beat map ({args.chapters} chapters)...")
        beats = content_provider.generate_beat_map(args.book, args.chapters, args.brief, continuity_block=continuity)
        story_bible.save_beat_map(args.series, args.book, beats)
        print(f"[voxel] Beat map saved to story_bibles/{args.series}.json - "
              "chapters will follow this outline instead of writing blind.")

    compiled = []
    still_short_chapters = []
    for n in range(1, args.chapters + 1):
        print(f"[voxel] Writing chapter {n}/{args.chapters}...")
        chapter_beat = story_bible.get_chapter_beat(args.series, args.book, n)
        if chapter_beat:
            chapter_brief = f"Book-level brief: {args.brief}\n\nThis chapter's required beat: {chapter_beat}"
        else:
            # Fallback, should only happen if the beat map came back short.
            chapter_brief = args.brief if n == 1 else f"{args.brief}\n(Continue naturally from chapter {n-1}.)"

        chapter_text, attempts, still_short = _generate_chapter_with_length_retry(
            n, chapter_brief, continuity, args.min_words, args.max_words,
        )
        if attempts > 1:
            print(f"[voxel]   chapter {n} took {attempts} attempt(s) to reach length.")
        if still_short:
            still_short_chapters.append(n)

        print(f"[voxel]   humanizer pass for chapter {n}...")
        clean_text, meta = humanizer.humanize_text(chapter_text, content_provider.call_raw)
        if meta.get("integrity_gate_failed"):
            print(f"[voxel]   WARNING: chapter {n} rewrite dropped a fact - kept original text.")

        # Humanizer rewrites can shorten text slightly; if it dropped the
        # chapter below the floor, that's worth surfacing too even though
        # we don't re-run generation at this stage (a rewrite pass is meant
        # to be a light edit, not a rewrite that changes length by much).
        final_words = len(clean_text.split())
        if final_words < args.min_words and n not in still_short_chapters:
            print(f"[voxel]   NOTE: chapter {n} is {final_words}w after the humanizer pass, "
                  f"under the {args.min_words}w floor - the humanizer rewrite likely trimmed it.")
            still_short_chapters.append(n)

        chapter_path = out_dir / f"chapter_{n:02d}.md"
        chapter_path.write_text(clean_text)
        compiled.append(clean_text)
        print(f"[voxel]   -> {chapter_path}")

    manuscript_path = out_dir / f"{book_slug}_full_manuscript.md"
    manuscript_path.write_text("\n\n---\n\n".join(compiled))

    summary = args.summary or f"({args.chapters}-chapter novel: {args.brief[:150]})"
    story_bible.register_book(args.series, args.book, summary)
    print(f"[voxel] Registered '{args.book}' in the '{args.series}' story bible for future sequels.")

    print()
    print("[voxel] Done. Output folder:")
    print(f"  {out_dir.resolve()}")
    if still_short_chapters:
        print(f"[voxel] {len(still_short_chapters)} chapter(s) still under the {args.min_words}w "
              f"floor after retries: {still_short_chapters} - worth a manual expansion pass "
              "before publishing.")

    if args.commit:
        print("[voxel] Committing and pushing (using your local git login)...")
        subprocess.run(["git", "add", str(out_dir), "story_bibles"], check=False)
        subprocess.run(["git", "commit", "-m", f"Add {args.book} ({args.chapters} chapters, auto-generated)"], check=False)
        subprocess.run(["git", "push"], check=False)
    else:
        print("[voxel] Not committed. Re-run with --commit to push, or paste the files via GitHub's web editor.")


def cmd_audit(args):
    """Audit already-written chapters. Read-only against chapter content -
    does not rewrite, regenerate, or touch a single chapter file. Only
    writes the report file itself.

    Checks three things per chapter, the only three that are reliably
    automatable:
      - word count (vs --min-words / --max-words)
      - em-dash count (Voxel's novels use a hard zero-em-dash rule)
      - humanizer.scan() AI-tell pattern hits (banned words/phrases,
        tricolon lists, low sentence-length variance)

    Does NOT check grammar, plot logic, pacing, continuity, foreshadowing/
    payoff, or character consistency - those need a human editorial read
    against the book's beat_map.md, not a script.

    Path resolution (fixed 2026-09-15): the Amity Falls books live directly
    under novels/<book-slug>/ (e.g. novels/amity-falls-book-2/chapters/),
    NOT nested under a series-name folder the way `novel` writes new
    chapters. This command takes only --book and resolves there first,
    falling back to the older novels/<series>/<book-slug>/ layout if
    --series is also given and the direct path doesn't exist."""
    book_slug = "".join(c if c.isalnum() or c in " -_" else "" for c in args.book).strip().replace(" ", "-").lower()

    base_dir = NOVELS_DIR / book_slug
    if not base_dir.exists() and args.series:
        base_dir = NOVELS_DIR / args.series / book_slug

    chapters_dir = base_dir / "chapters"
    if not chapters_dir.exists():
        chapters_dir = base_dir  # even older layout: chapter_*.md directly under the book dir

    chapter_files = sorted(chapters_dir.glob("chapter_*.md"))
    if not chapter_files:
        print(f"[voxel] No chapter_*.md files found under {chapters_dir}")
        print(f"[voxel] Checked: novels/{book_slug}/chapters, novels/{book_slug}, "
              + (f"novels/{args.series}/{book_slug}/chapters, novels/{args.series}/{book_slug}" if args.series else "(no --series given)"))
        return

    print(f"[voxel] Auditing {len(chapter_files)} chapter(s) in {chapters_dir} (read-only scan)...")

    lines = [
        "# Chapter Audit Report", "",
        f"Book: {args.book}", f"Chapters found: {len(chapter_files)}",
        f"Word range checked: {args.min_words}-{args.max_words}", "",
        "This is a SCAN only. No chapter content was changed by this report.", "",
        "| Chapter | Words | Em-dashes | AI-tell score | Top hits |",
        "|---|---|---|---|---|",
    ]

    flagged_low, flagged_high, flagged_tells = [], [], []

    for path in chapter_files:
        text = path.read_text()
        word_count = len(text.split())
        em_dash_count = text.count("\u2014")
        report = humanizer.scan(text)
        top_hits = ", ".join(
            f"{h.get('pattern', h['type'])}x{h.get('count', 1)}"
            for h in sorted(report["hits"], key=lambda h: h.get("count", 1), reverse=True)[:3]
        ) or "-"
        lines.append(f"| {path.stem} | {word_count} | {em_dash_count} | {report['score']} | {top_hits} |")

        if word_count < args.min_words:
            flagged_low.append((path.stem, word_count))
        if args.max_words and word_count > args.max_words:
            flagged_high.append((path.stem, word_count))
        if report["score"] >= args.tell_threshold:
            flagged_tells.append((path.stem, report["score"]))

    lines += ["", f"## Under {args.min_words}-word floor ({len(flagged_low)})"]
    lines += [f"- {name}: {wc} words" for name, wc in flagged_low] or ["- none"]

    if args.max_words:
        lines += ["", f"## Over {args.max_words}-word ceiling ({len(flagged_high)})"]
        lines += [f"- {name}: {wc} words" for name, wc in flagged_high] or ["- none"]

    lines += ["", f"## AI-tell score >= {args.tell_threshold} ({len(flagged_tells)})"]
    lines += [f"- {name}: score {score}" for name, score in flagged_tells] or ["- none"]

    lines += [
        "", "---",
        "Not covered by this report (needs a manual read against beat_map.md): "
        "grammar/spelling/syntax, prose quality, dialogue, POV, character "
        "consistency/arcs, timeline, plot logic, scene purpose, chapter "
        "structure, pacing/tension, foreshadowing/payoff, subplots, ending.",
    ]

    report_path = base_dir / "chapters_audit_report.md"
    report_path.write_text("\n".join(lines))

    print(f"[voxel] Report written: {report_path.resolve()}")
    print(f"[voxel]   Under floor: {len(flagged_low)}, over ceiling: {len(flagged_high)}, "
          f"high AI-tell score: {len(flagged_tells)}")

    if args.commit:
        print("[voxel] Committing and pushing report...")
        subprocess.run(["git", "add", str(report_path)], check=False)
        subprocess.run(["git", "commit", "-m", f"Audit report for {args.book}"], check=False)
        subprocess.run(["git", "push"], check=False)
    else:
        print("[voxel] Not committed. Re-run with --commit to push, or paste the report via GitHub's web editor.")


def cmd_images(args):
    """Phase 9: generate N images from ONE reference photo using NVIDIA
    FLUX.1-Kontext-dev, which keeps the subject in the reference photo
    consistent across every generated image. One call per prompt, same
    reference image reused each time."""
    import nvidia_image_provider

    print(f"[voxel] Generating {len(args.prompts)} image(s) from reference "
          f"'{args.reference}' via NVIDIA FLUX.1-Kontext-dev...")
    results = nvidia_image_provider.generate_batch_from_reference(
        args.reference, args.prompts, args.out_dir,
        filename_prefix=args.prefix,
    )
    ok = sum(1 for r in results if r is not None)
    print()
    print(f"[voxel] Done: {ok}/{len(args.prompts)} succeeded.")
    print(f"[voxel] Output folder: {Path(args.out_dir).resolve()}")
    if ok < len(args.prompts):
        print("[voxel] Some prompts failed - see [warn] lines above for details.")


def main():
    parser = argparse.ArgumentParser(description="Voxel Publications - one-command content pipeline.")
    sub = parser.add_subparsers(dest="command", required=True)

    book_p = sub.add_parser("book", help="Generate a full illustrated picture book, like Luna and the Lost Star.")
    book_p.add_argument("--concept", required=True)
    book_p.add_argument("--pages", type=int, default=26)
    book_p.add_argument("--trim", default="8.5x11", choices=["8.5x8.5", "8.5x11", "6x9", "5x8"])
    book_p.add_argument("--paper", default="white", choices=["white", "cream"])
    book_p.add_argument("--coloring-book", action="store_true")
    book_p.add_argument("--series", default=None, help="Story-bible slug, e.g. 'luna', so a sequel stays consistent.")
    book_p.add_argument("--summary", default=None, help="One-line summary to store in the series bible.")
    book_p.set_defaults(func=cmd_book)

    novel_p = sub.add_parser("novel", help="Generate a novel or novel sequel, chapter by chapter, like Amity Falls.")
    novel_p.add_argument("--series", required=True, help="Story-bible slug, e.g. 'amity-falls'.")
    novel_p.add_argument("--book", required=True, help="Book title, e.g. 'Amity Falls Book 2'.")
    novel_p.add_argument("--chapters", type=int, required=True)
    novel_p.add_argument("--brief", required=True, help="What this book/chapter arc is about.")
    novel_p.add_argument("--summary", default=None)
    novel_p.add_argument("--min-words", type=int, default=2000, help="Word-count floor per chapter; short chapters are auto-retried.")
    novel_p.add_argument("--max-words", type=int, default=2300, help="Word-count target ceiling per chapter (stated in the prompt, not hard-enforced).")
    novel_p.add_argument("--commit", action="store_true", help="git add/commit/push when done.")
    novel_p.set_defaults(func=cmd_novel)

    audit_p = sub.add_parser("audit", help="Scan already-written chapters for word count, em-dashes, and AI-tell patterns. Read-only, does not rewrite chapters.")
    audit_p.add_argument("--book", required=True, help="Book title, e.g. 'Amity Falls Book 2'. Resolves directly to novels/<book-slug>/.")
    audit_p.add_argument("--series", default=None, help="Only needed as a fallback if the book was written under novels/<series>/<book-slug>/ instead.")
    audit_p.add_argument("--min-words", type=int, default=2000)
    audit_p.add_argument("--max-words", type=int, default=2634)
    audit_p.add_argument("--tell-threshold", type=int, default=8, help="AI-tell score at/above which a chapter is flagged.")
    audit_p.add_argument("--commit", action="store_true", help="git add/commit/push the report when done.")
    audit_p.set_defaults(func=cmd_audit)

    images_p = sub.add_parser("images", help="Generate N images from one reference photo (NVIDIA FLUX.1-Kontext-dev).")
    images_p.add_argument("--reference", required=True, help="Path to the one source/reference image.")
    images_p.add_argument("--prompts", required=True, nargs="+", help="One prompt per output image, space-separated (quote each one).")
    images_p.add_argument("--out-dir", required=True)
    images_p.add_argument("--prefix", default="ref", help="Output filename prefix.")
    images_p.set_defaults(func=cmd_images)

    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
