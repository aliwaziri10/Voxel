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

2026-09-19 (fix, then reverted same day): first attempt added a retry
loop that told the model to "expand" a chapter that came in short of a
word-count target. That's padding by another name and directly violates
novels/EDITORIAL_CHARTER.md's no-padding rule ("never inflate a one-beat
chapter to hit a word target") - reverted before ever running against a
real book, once the charter (already written 2026-09-16, just not read
first) was actually checked.

2026-09-19 (corrected): the charter's real fix for thin chapters is
upstream, in the beat map itself - content_provider.generate_beat_map()
now plans 2-4 genuine sub-beats per chapter instead of one flat beat (see
that file). `cmd_novel` no longer retries or "expands" anything. It
still checks the resulting word count against --min-words purely to
REPORT it - a short chapter is logged plainly, per the charter's
"surface everything found" rule, as something worth a manual look
(is this a genuine one-sub-beat chapter that should honestly stay short,
per the charter, or did the model skip sub-beats it was given?) - never
auto-inflated. Default --min-words/--max-words changed from an invented
2000/2300 to the charter's actual Book-4-onward standard, 2300/2700.

2026-09-19 (fix): `novel` wrote chapters to novels/<series>/<book-slug>/,
but the existing published books (and every scripts/ tool - proofreader,
word_repetition_fixer, audit) use novels/<book-slug>/chapters/. Books 1-3
are frozen and were never touched by this fix; `novel` now writes to the
same novels/<book-slug>/chapters/ layout so Book 4+ chapters are visible
to the existing tooling instead of landing in a path nothing else reads.
The compiled full-manuscript file now lives at novels/<book-slug>/ (one
level up from chapters/), matching where audit's report file is written.

2026-09-20 (new, --checkpoint): a live 60-chapter Book 4 run showed the
core risk of the original design: nothing was committed until the very
last step, so any crash, GitHub's 6-hour job limit, or a refused push
would throw away every finished chapter. `novel --checkpoint` fixes that
two ways. (1) It commits and pushes the beat map right after it is
planned, and then each chapter right after it is written, so finished
work is safe in the repo as the run goes. (2) If a chapter file already
exists (and is not empty) it is kept and skipped instead of regenerated,
so re-running the same command after a crash resumes where it stopped
instead of starting over. The beat map is reused on a resume because it
was committed too. This changes NO prose logic, word-count logic or
padding logic - it only saves and skips. Without --checkpoint the
behaviour is exactly what it was before. A failed push prints a warning
and the run carries on; it never stops the run.

2026-09-20 (fix, broken-chapter guard): checking the 12 chapters that
run saved showed 3 of them were BROKEN and had been saved and
checkpointed anyway: chapter 6 (467 words, cut off mid-sentence),
chapter 8 (cut off mid-sentence, with the model's own summary notes
"I've written Chapter 8 at approximately 2,450 words, covering all
three sub-beats..." glued on the end of the story text), and chapter 10
(ends "Wren turned[End of Chapter 10]"). Nothing in the pipeline looked at
whether a chapter was actually finished. `novel` now runs
_chapter_problem() on every chapter: it rejects text that is far too
short to be a chapter, contains the model's own notes/markers instead of
story text, or does not end on a finished sentence. A rejected chapter is
regenerated (up to 3 tries in total) BEFORE the humanizer pass, and if
the humanizer's rewrite comes back broken the original draft is kept
instead. A chapter that is still broken after 3 tries is NOT saved, is
listed at the end, and the run exits with an error so it is visible; a
re-run with --checkpoint fills in exactly those gaps. This regenerates a
BROKEN chapter from scratch - it never lengthens or "expands" a real one,
so it does not conflict with the charter's no-padding rule. The book is
also not registered in the story bible until every chapter exists.
Same fix adds a hard style rule to every chapter brief (no em-dash
characters, end on a complete sentence of story text, no notes to the
editor), because the system prompt only said "no em-dash overuse" while
the charter bans them outright, and every one of the 12 chapters
contained 17-55 em-dashes. Em-dash count is now printed per chapter. The
prompt rule reduces them but cannot guarantee zero; the charter's
copy-editor pass still has to verify.

2026-09-20 (fix, meta-leak guard): checking chapters 2, 3, 5, 9, 11 and
12 (see novels/amity-falls-book-4/CANON_CONFLICTS.md and
CHAPTER_REVIEW_2026-09-20.md) found the model copying story-bible author
notes or book/series framing straight into the prose - e.g. a character
"writing" a note that reads "Wound: grandmother's missing decade.
Competence: high.", or dialogue like "Since Book 3." / "Before Book 3" /
"No persuasion arc needed... Book 2 he hesitated". `_META_PATTERNS` now
also catches "Book N", "the series", "protagonist", "no ... arc needed",
"persuasion arc", and the "Wound:"/"Competence:" note-style labels, so a
leaking chapter is rejected and regenerated by the same guard and retry
loop as a broken/cut-off chapter, instead of being saved. content_
provider.py's prompts were also given an explicit rule against this
(see that file), so this guard is the second layer of defense, not the
only one.

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
import re
import subprocess
from pathlib import Path

import content_provider
import humanizer
import story_bible


NOVELS_DIR = Path("novels")

# --- broken-chapter guard (2026-09-20) --------------------------------
# Below this many words a chapter is treated as cut off, not "honestly
# thin". Deliberately far under the charter's 2300 floor: a real one-beat
# chapter may stay short, but nothing under this is a finished chapter.
_BROKEN_WORD_FLOOR = 800
_CHAPTER_MAX_GENERATION_TRIES = 3

# Text the model sometimes glues onto a chapter instead of (or after)
# story text: summaries of its own work, end-of-chapter markers.
_META_PATTERNS = [
    r"\[End of Chapter",
    r"I(?:['\u2019]ve| have) written (?:Chapter|the chapter)",
    r"covering all (?:\w+ )?sub-?beats?",
    r"\bsub-?beats?\b",
    # Meta/bible leaks (2026-09-20): found live in Book 4 chapters 2, 3, 5,
    # 9, 11, 12 - the model copying story-bible author notes or book/series
    # framing straight into the prose instead of writing in-world content.
    # See novels/amity-falls-book-4/CANON_CONFLICTS.md and
    # CHAPTER_REVIEW_2026-09-20.md for the specific leaks this caught.
    r"\bBook\s*[1-9]\b",
    r"\bbook\s+(?:one|two|three|four|five)\b",
    r"\bthe series\b",
    r"\bprotagonist\b",
    r"\b[Nn]o\s+\w+\s+arc\s+needed\b",
    r"\bpersuasion arc\b",
    r"\bWound:\s",
    r"\bCompetence:\s",
]

# A finished chapter ends on a sentence: a full stop, ! or ?, a closing
# quote mark, a closing bracket, italic/bold markers, or an ellipsis.
_ENDING_OK = tuple(".!?\"\u201d\u2019')*_\u2026")

# Added to every chapter brief. The charter bans em-dashes outright and
# wants a clean chapter ending; the system prompt in content_provider only
# said "no em-dash overuse".
CHAPTER_STYLE_RULE = (
    "\n\nHARD STYLE RULES for this chapter: never use the em-dash character "
    "(the long dash); use a comma, a period, or start a new sentence "
    "instead. End the chapter on a complete final sentence of story text "
    "and write nothing after it: no title, no summary, no notes to the "
    "editor, no word count, no end-of-chapter marker."
)


def _chapter_problem(text):
    """Return a short plain-English reason if this chapter text is broken
    (cut off, empty, carrying the model's own notes, or leaking a story-
    bible/book/series reference into the prose - see _META_PATTERNS),
    else None."""
    t = (text or "").strip()
    if not t:
        return "empty reply"
    words = len(t.split())
    if words < _BROKEN_WORD_FLOOR:
        return f"only {words} words, far too short to be a finished chapter (likely cut off)"
    for pattern in _META_PATTERNS:
        if re.search(pattern, t, re.IGNORECASE | re.MULTILINE):
            return f"contains a meta/bible leak or the model's own notes instead of story text (matched: {pattern})"
    if t[-1] not in _ENDING_OK:
        return f"does not end on a finished sentence (last characters: {t[-40:]!r})"
    return None


def _checkpoint(paths, message):
    """Commit and push the given paths right now, so finished work is safe
    in the repo even if the run dies later. Never raises and never stops
    the run: a nothing-to-commit result or a failed push only prints a
    line. Used by `novel --checkpoint` only."""
    subprocess.run(["git", "add", *[str(p) for p in paths]], check=False)
    commit = subprocess.run(["git", "commit", "-m", message], check=False,
                            capture_output=True, text=True)
    if commit.returncode != 0:
        # Normal when nothing changed since the last checkpoint.
        print(f"[voxel]   checkpoint: nothing new to commit ({message})")
        return
    push = subprocess.run(["git", "push"], check=False, capture_output=True, text=True)
    if push.returncode == 0:
        print(f"[voxel]   checkpoint saved: {message}")
    else:
        print(f"[voxel]   WARNING: checkpoint push FAILED for '{message}'. "
              "The run continues, but this work is not yet safe in the repo. "
              f"Git said: {push.stderr.strip()[:300]}")


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


def cmd_novel(args):
    """Generate N chapters of a novel/sequel, one file per chapter under
    novels/<book-slug>/chapters/, plus a compiled single manuscript file
    at novels/<book-slug>/. This matches the layout the existing books
    (and every scripts/ tool - proofreader, word_repetition_fixer, audit)
    already use; see the 2026-09-19 module docstring note above for why
    this changed from the old novels/<series>/<book-slug>/ layout.

    Phase 9: before writing any prose, generates (or reuses, if this book
    already has one - e.g. a resumed run) a whole-book chapter beat map,
    so every chapter is written from ITS OWN specific outline instead of
    just the top-level brief + "continue naturally from last chapter".
    This is what keeps a long novel from losing the plot partway through
    - the outline is planned with the whole book in view before any
    chapter is drafted. As of 2026-09-19, each chapter's outline is 2-4
    genuine sub-beats (plot/relationship-micro/interior/stakes/callback -
    see content_provider.generate_beat_map and
    novels/EDITORIAL_CHARTER.md), which is what gives a chapter enough
    real content to reach a natural length without padding.

    Runs the humanizer pass per chapter. Word count is checked against
    --min-words/--max-words for REPORTING only - a short chapter is
    logged as worth a manual look, never auto-regenerated or "expanded".
    An automatic retry-and-expand loop was tried and reverted the same
    day it was written, once EDITORIAL_CHARTER.md's explicit no-padding
    rule was actually read; see the module docstring above.

    --checkpoint (2026-09-20): commit+push the beat map and every chapter
    the moment it is written, and skip any chapter file that already
    exists so a re-run resumes instead of starting over. See the module
    docstring for why.

    Broken-chapter guard (2026-09-20): a chapter that is cut off, far too
    short, carries the model's own notes, or leaks a story-bible/book/
    series reference is regenerated from scratch (up to 3 tries) and
    never saved if it stays broken. This is NOT the reverted "expand a
    short chapter" loop: it replaces a broken chapter, it never lengthens
    a real one.

    Commits+pushes at the end if --commit is passed (uses your machine's
    own git credentials)."""
    continuity = story_bible.continuity_prompt_block(args.series)
    book_slug = "".join(c if c.isalnum() or c in " -_" else "" for c in args.book).strip().replace(" ", "-").lower()
    book_dir = NOVELS_DIR / book_slug
    out_dir = book_dir / "chapters"
    out_dir.mkdir(parents=True, exist_ok=True)

    beats = story_bible.load_beat_map(args.series, args.book)
    if beats and len(beats) == args.chapters:
        print(f"[voxel] Reusing existing beat map for '{args.book}' ({len(beats)} chapters) - "
              "this looks like a resumed run.")
    else:
        if beats:
            print(f"[voxel] Existing beat map for '{args.book}' has {len(beats)} chapters, "
                  f"but {args.chapters} were requested - generating a fresh one.")
        print(f"[voxel] Planning whole-book beat map ({args.chapters} chapters, "
              "2-4 sub-beats each)...")
        beats = content_provider.generate_beat_map(args.book, args.chapters, args.brief, continuity_block=continuity)
        story_bible.save_beat_map(args.series, args.book, beats)
        print(f"[voxel] Beat map saved to story_bibles/{args.series}.json - "
              "chapters will follow this outline instead of writing blind.")
        if args.checkpoint:
            _checkpoint(["story_bibles"], f"{args.book}: beat map saved ({args.chapters} chapters planned)")

    compiled = []
    short_chapters = []   # (chapter_num, word_count, sub_beat_count) - reported, not auto-fixed
    failed_chapters = []  # chapter numbers still broken after every try - NOT saved
    for n in range(1, args.chapters + 1):
        chapter_path = out_dir / f"chapter_{n:02d}.md"

        if args.checkpoint and chapter_path.exists() and chapter_path.read_text().strip():
            print(f"[voxel] Chapter {n}/{args.chapters} already exists - keeping it, skipping (resume).")
            compiled.append(chapter_path.read_text())
            continue

        print(f"[voxel] Writing chapter {n}/{args.chapters}...")
        chapter_beat = story_bible.get_chapter_beat(args.series, args.book, n)
        sub_beat_count = None
        raw_entry = next((e for e in (beats or []) if e.get("chapter") == n), None)
        if raw_entry and raw_entry.get("sub_beats"):
            sub_beat_count = len(raw_entry["sub_beats"])

        if chapter_beat:
            chapter_brief = f"Book-level brief: {args.brief}\n\nThis chapter's sub-beats:\n{chapter_beat}"
        else:
            # Fallback, should only happen if the beat map came back short.
            chapter_brief = args.brief if n == 1 else f"{args.brief}\n(Continue naturally from chapter {n-1}.)"
        chapter_brief += CHAPTER_STYLE_RULE

        chapter_text = None
        for gen_try in range(1, _CHAPTER_MAX_GENERATION_TRIES + 1):
            candidate = content_provider.generate_novel_chapter(
                n, chapter_brief, continuity_block=continuity,
                min_words=args.min_words, max_words=args.max_words,
            )
            problem = _chapter_problem(candidate)
            if not problem:
                chapter_text = candidate
                break
            print(f"[voxel]   chapter {n} draft {gen_try}/{_CHAPTER_MAX_GENERATION_TRIES} is broken: {problem}. "
                  + ("Writing it again from scratch..." if gen_try < _CHAPTER_MAX_GENERATION_TRIES
                     else "Giving up on this chapter for now."))
        if chapter_text is None:
            failed_chapters.append(n)
            print(f"[voxel]   chapter {n} NOT saved. Re-run with the same inputs to fill this gap.")
            continue

        print(f"[voxel]   humanizer pass for chapter {n}...")
        clean_text, meta = humanizer.humanize_text(chapter_text, content_provider.call_raw)
        if meta.get("integrity_gate_failed"):
            print(f"[voxel]   WARNING: chapter {n} rewrite dropped a fact - kept original text.")
        rewrite_problem = _chapter_problem(clean_text)
        if rewrite_problem:
            print(f"[voxel]   WARNING: chapter {n} humanizer rewrite came back broken ({rewrite_problem}) - "
                  "using the un-humanized draft instead.")
            clean_text = chapter_text

        word_count = len(clean_text.split())
        em_dash_count = clean_text.count("\u2014")
        if word_count < args.min_words:
            note = f" ({sub_beat_count} sub-beat(s) given)" if sub_beat_count else ""
            print(f"[voxel]   NOTE: chapter {n} is {word_count}w, under the {args.min_words}w floor{note}. "
                  "Not auto-regenerated (see EDITORIAL_CHARTER.md's no-padding rule) - worth a manual "
                  "look at whether this is a genuinely thin chapter or a sub-beat got skipped.")
            short_chapters.append((n, word_count, sub_beat_count))

        chapter_path.write_text(clean_text)
        compiled.append(clean_text)
        print(f"[voxel]   -> {chapter_path} ({word_count}w, {em_dash_count} em-dashes)")

        if args.checkpoint:
            _checkpoint([chapter_path], f"{args.book}: chapter {n}/{args.chapters} ({word_count}w)")

    manuscript_path = book_dir / f"{book_slug}_full_manuscript.md"
    manuscript_path.write_text("\n\n---\n\n".join(compiled))

    if failed_chapters:
        print(f"[voxel] NOT registering '{args.book}' in the story bible: "
              f"{len(failed_chapters)} chapter(s) are missing.")
    else:
        summary = args.summary or f"({args.chapters}-chapter novel: {args.brief[:150]})"
        story_bible.register_book(args.series, args.book, summary)
        print(f"[voxel] Registered '{args.book}' in the '{args.series}' story bible for future sequels.")

    print()
    print("[voxel] Done. Output folder:")
    print(f"  {book_dir.resolve()}")
    if short_chapters:
        print(f"[voxel] {len(short_chapters)} chapter(s) under the {args.min_words}w floor "
              "(reported only, not auto-changed - see EDITORIAL_CHARTER.md):")
        for n, wc, sbc in short_chapters:
            sb_str = f"{sbc} sub-beat(s)" if sbc else "no sub-beat count available"
            print(f"    - chapter {n}: {wc}w, {sb_str}")
    if failed_chapters:
        print(f"[voxel] MISSING chapters (still broken after {_CHAPTER_MAX_GENERATION_TRIES} tries, not saved): "
              + ", ".join(str(c) for c in failed_chapters))
        print("[voxel] Re-run with the same inputs and --checkpoint to fill exactly these gaps.")

    if args.commit:
        print("[voxel] Committing and pushing (using your local git login)...")
        subprocess.run(["git", "add", str(book_dir), "story_bibles"], check=False)
        subprocess.run(["git", "commit", "-m", f"Add {args.book} ({args.chapters} chapters, auto-generated)"], check=False)
        subprocess.run(["git", "push"], check=False)
    else:
        print("[voxel] Not committed. Re-run with --commit to push, or paste the files via GitHub's web editor.")

    if failed_chapters:
        raise SystemExit(1)


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
    novel_p.add_argument("--min-words", type=int, default=2300,
                          help="Word-count floor per chapter, per EDITORIAL_CHARTER.md's Book-4-onward standard. "
                               "A short chapter is reported, never auto-padded.")
    novel_p.add_argument("--max-words", type=int, default=2700,
                          help="Natural ceiling per chapter (stated in the prompt, not hard-enforced).")
    novel_p.add_argument("--commit", action="store_true", help="git add/commit/push when done.")
    novel_p.add_argument("--checkpoint", action="store_true",
                          help="Commit+push the beat map and each chapter as soon as it is written, and skip "
                               "chapter files that already exist, so a crashed run can be re-run and resume.")
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
