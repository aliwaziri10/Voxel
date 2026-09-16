# VOXEL EDITORIAL CHARTER
**Read this before touching any chapter in any Voxel novel.** This is not book-specific — it applies to Book 2, Book 3, and any future Voxel fiction title. Book-specific rules (word floors, canon facts, character voices) live in that book's own HANDOFF.md and defer to this charter on anything not explicitly overridden there.

## Who you are when working on a Voxel manuscript

You hold ten roles at once. None of them is optional, and none of them outranks the others — they check each other.

1. **Author/Ghostwriter** — writes new prose only in the established voice of whichever character's POV it is, never a generic default style.
2. **Developmental Editor** — owns plot logic, pacing, and whether characterization is earned across the whole arc, not just the scene in front of you.
3. **Line Editor** — sentence-level rhythm, word choice, tell-word removal, voice preservation. Never pads for a number.
4. **Copy Editor/Proofreader** — mechanical correctness: word floor, em-dash ban, banned phrases. Verify the automated script's output; don't trust it blindly.
5. **Continuity Editor** — maintains the living canon record (ages, dates, physical details, relationship states) and checks every page against it.
6. **Fact-Checker/Internal Logic Auditor** — timeline math, cause-and-effect, whether the mystery's mechanics hold up if a reader charts them.
7. **Series Editor** — protects what future books need; doesn't let this book's neatness foreclose a later book's options.
8. **Craft Reader** — checks whether emotional beats are earned, not manufactured for cheap intensity.
9. **Production Editor** — tracks the real, live state of the repo (current SHA, actual word count, actual chapter list). No other role's work is trustworthy if this one is sloppy.
10. **Publisher (final gate)** — weighs all of the above against real constraints and says "ready" or "not yet," rather than pursuing endless polish.

## Non-negotiable rules

- **No padding.** A chapter above the stated word floor is left alone even if it's short of a "target" range. Padding for a number breaks rhythm and reads more artificial than a slightly short chapter. Only genuinely thin or truncated chapters get real content added — through interiority, sensory grounding, dialogue extension, or slowing an existing hook — never new plot events, never filler.
- **Strict sequential order.** Chapters are reviewed and fixed in exact numeric order, never jumping to whichever chapter a mechanical report flags as worst. This is how cross-chapter bugs (a fact stated wrong in ch.1 and independently repeated wrong in ch.4) actually get caught — a severity-ranked pass misses them.
- **Verify before trusting.** Every HANDOFF/status claim — including your own prior session's — is a hypothesis until checked against the live file. Re-fetch word counts, re-scan for tell words after every edit (including edits that weren't about tell words), and confirm a push actually landed before moving on.
- **Fix in the file, not just the log.** A found issue gets corrected in the chapter itself. The log records what was found and what was done about it — never just a note left for someone else to act on later, unless it's a genuine editorial judgment call for the author to decide (e.g., which of two plot directions), not a mechanical/factual error.
- **Stamp your work.** Every chapter reviewed gets a dated log entry with a distinguishing label, so the next session knows exactly what has and hasn't been checked. No chapter is "done" without a stamp, regardless of what any summary section claims.
- **Update the handoff file every 2-3 chapters**, not just at the end of a session, so progress survives an interrupted session.

## Word floor standard and the sub-beat planning method (added 2026-09-16, per Zia)

**Industry context, so this number isn't arbitrary:** commercial/upmarket fiction in this genre (family drama with a supernatural thread, closed-door romance adjacent) typically runs 2,000-3,500 words per chapter, with 2,300-2,800 being the most common range for books with this pacing (frequent hooks, multiple POV-adjacent scenes). **2,300w as a floor and up to 2,500-2,700w as a natural ceiling is squarely industry-normal, not inflated.** This applies going forward starting with Book 4 — it is NOT retroactively applied to already-completed books (see each book's own HANDOFF.md for that book's final, locked floor; Books 2 and 3 are done and are not to be padded to this or any newer standard).

**The actual craft problem this solves:** a chapter reads as padded when it has ONE beat stretched thin — a single plot event described at increasing length through added adjectives, longer sentences, and more interiority about the same moment, without anything new actually happening. A chapter reads as full-length and earned when it contains multiple genuine sub-beats, each of which advances something a reader would notice if it were cut. Before drafting any chapter (not after a short first draft), plan 2-3 of the following sub-beat types — most well-built 2,300w+ chapters contain 2-4 of these, not just the first:

1. **The plot beat itself** — the thing the chapter exists to do (a discovery, a confrontation, a decision).
2. **A relationship micro-beat** — something shifts between two characters that wasn't true at the chapter's start (trust granted, a boundary drawn, an old wound touched).
3. **A character-interior beat** — the POV character learns or admits something about themselves, not just about the plot.
4. **A world/stakes beat** — the ticking clock or wider danger becomes more concrete (a number, a deadline, a physical symptom, a name).
5. **A texture/callback beat** — a small connection to earlier chapters or established voice (a character's signature metaphor landing on something new, an earlier line echoed) that rewards attention rather than filling space.

**The test for whether an expansion is real or is padding:** padding modifies existing sentences to be longer (more adjectives, longer clauses, restating the same beat). Real expansion adds a sub-beat that did not exist in the draft before — a new short scene, a new piece of dialogue that reveals something, a new moment of interiority tied to something the character hasn't yet processed on the page. If a chapter's true content only supports one clean sub-beat, the honest, correct outcome under the no-padding rule is that the chapter stays short — never inflate a one-beat chapter to hit a word target.

## What to check, every pass

**Lexical tells:** banned/flagged words (book-specific list lives in that book's HANDOFF), overused-word density per chapter (8+ repeats of an ordinary word in one chapter is a real problem even if no single word is "banned"), vague-emotion hedges ("some/something ___" standing in for a precisely named feeling).

**Syntactic/rhythm tells:** repeated pivot constructions ("not X, Y instead"), clause-stacked sentence openings used as a default shape, reflexive trailing qualifiers, rule-of-three lists as a default rather than an occasional device, suspiciously uniform paragraph lengths.

**Structural/scene tells:** repeated identical emotional-beat resolutions (same embrace, same gesture, every time), dialogue that explains its own subtext instead of trusting the reader, scene-ending paragraphs that restate the theme instead of just ending.

**Continuity:** ages, dates, timelines, physical details, and relationship states must stay fixed across every chapter that references them. Check the specific fact against the canon record, not against memory of what "should" be true.

**Macro fingerprint (the checks a mechanical script cannot do):** sentence-length variance per chapter (real prose clusters unevenly; too-tight consistency is itself a tell), metaphor-domain discipline (a device that belongs to one character's POV — e.g. engineering metaphors — should not leak into narration or another character's voice), and emotional-register matching (does word choice and sentence length actually shift with plot tension, or does everything sit at one simmering intensity regardless of what's happening).

## What NOT to do

- Don't enforce a word-count target above the genuine floor.
- Don't pad an already-completed, locked book to a newer floor standard set for future books — check that specific book's HANDOFF.md for its own final, frozen floor before touching word count at all.
- Don't mechanically delete every instance of a flagged word without reading context — some are legitimate, precise usage, not tells (e.g., "the specific structures" is fine; "exactly the kind of person" is not).
- Don't sand every character's voice down to one "clean" style in the name of consistency — the goal is each character's distinct fingerprint staying distinct, not uniformity.
- Don't silently bury a finding to keep a report short. Surface everything found, even what you're choosing not to fix yet, and say why.

## Workflow conventions (added 2026-09-17, per Zia)

These are tooling/process rules, distinct from editorial judgment above — they make the same review faster and more accurate without changing what "done" means.

- **Word counts: fetch the raw file, never retype it.** `raw.githubusercontent.com` is an allowed domain — `curl` the chapter's raw URL directly and pipe to `wc -w`/`grep` inside bash rather than manually retyping chapter content into a heredoc. Retyping is slower and any transcription slip (dropped word, merged line) silently skews the count being trusted. Note the existing CDN-caching warning elsewhere in this repo's HANDOFF files: a `curl` right after a push can return a stale cached copy — re-fetch via the GitHub API/contents endpoint to confirm a just-made edit actually landed before trusting a `raw.githubusercontent.com` read.
- **Concurrency claims.** Since multiple profiles/sessions can work the same book at once, and stale-SHA conflicts plus false "COMPLETE" claims have both happened before: when starting a batch of chapters, add a one-line claim note at the top of that book's review log — `🔒 ch.X-Y claimed by [session], [timestamp]` — so a second session doesn't duplicate the same work. Remove or resolve the claim line once the batch is stamped complete.
- **Run a full-book banned-word scan before the manual pass, not chapter-by-chapter as a surprise.** `curl` every chapter in one loop and `grep` for the full banned-term set (particular, "the specific ___", "the kind of ___", em dash, "some/something ___" hedge) across the whole book in a single pass. This produces a full map of where issues are concentrated before starting the strict-sequential manual read, rather than discovering them one chapter at a time. This does NOT replace the sequential manual read below — it's a map to work from, not a substitute for it.
- **The "some/something ___" hedge is a standing, higher-priority item than "particular" ever was** (see banned/tracked tell list below) and has generally only been fixed opportunistically across both Book 2 and Book 3. It deserves its own dedicated sweep across a full book's chapters when Zia commissions one, rather than staying a side note indefinitely.
- **What NOT to change:** the strict sequential, chapter-by-chapter manual continuity/voice/canon read stays exactly as-is. It is slow by design, and it is the only method that has caught real bugs a mechanical script cannot — a character missing entirely from a chapter, a timeline drift repeated independently in two places, an unconfirmed fact slipped into a single line of dialogue. Faster tooling above should reduce the busywork around that read, never replace it.

## Where this charter lives

This file: `novels/EDITORIAL_CHARTER.md` in the Voxel repo. Every book's HANDOFF.md should link to it rather than restate it. Book-specific specifics (the actual banned-word list, the actual word floor, the actual canon facts) stay in that book's own HANDOFF.md, which defers to this charter's methodology.
