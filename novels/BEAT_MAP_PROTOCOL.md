# Beat-Map Protocol — for the NEXT book after Kindling Line Book 2

Written 2026-09-29, after cleaning up severe chapter-to-chapter drift in
Kindling Line Book 2 (invented characters, a different magic system in
one chapter, wrong house counts, a locked line of dialogue repeated
verbatim, name collisions, wrong date math). Root cause: the beat map
that drove generation had only 2-3 one-sentence sub-beats per chapter,
which gave the generator almost nothing concrete to anchor against, so
it invented or misremembered names, objects, and mechanics between
chapters. Amity Falls and "Where the Frost Doesn't Reach" did not have
this problem, most likely because they had a richer standing canon
reference to generate against from the start.

**Any session generating a new book's beat map reads this file FIRST,**
before writing a single chapter entry, and follows it. This is not
optional polish, it is the fix for a confirmed, expensive failure mode.

## Step 0: check names against EVERY Voxel novel, not just this one

Generative models draw character names from a fairly small, statistically
common pool for a given genre (soft-sounding fantasy names like Mara,
Renn, Aldous, Ansa recur constantly across unrelated generations, purely
because they're common in the training data, not because anything is
being deliberately reused). This has already caused near-duplicate names
appearing independently across different Voxel series with no shared
plot or intent. Before locking a new book's cast:

- List every named character across Amity Falls (books 1-4), "Where the
  Frost Doesn't Reach," and Kindling Line (books 1-2), and avoid reusing
  any of them for a new series, even coincidentally.
- If a name recurs anyway once chapters are generated, that is NOT a
  sign it was meant to connect the two stories. Treat it as the same
  kind of drift as a wrong seal or wrong house count, and fix it.

## Step 1: write the canon-lock document BEFORE any beat map

Before any chapter is planned, write a canon-lock section (same shape as
the one in `novels/kindling-line-book-2/HANDOFF.md`'s "Canon lock"
block) covering, in full and unambiguous language:

- Every named character: full name, role, one physical or verbal tag
  that must stay consistent (a scar, a title, a way of addressing
  people), and whether they are alive or dead for the whole book.
- Every important object, seal, symbol, or document: its EXACT
  description, written once, to be copied verbatim into any chapter
  that mentions it, not paraphrased freshly each time.
- Every count that could drift: how many houses/factions/people sit on
  any council or body, how many signatures or votes are needed, how many
  days a threshold takes.
- The magic system (or any other world-mechanic), stated once, in plain
  unambiguous terms, with an explicit note of what it is NOT (the
  mistake that produced Book 2's "burner's brand" chapter was a
  generator inventing a plausible-sounding alternative mechanic with no
  such note to check against).
- The calendar: month names in order, days per month, and the exact
  date every chapter lands on, computed once and never re-derived
  per-chapter from "days since the last chapter."
- Style bans (banned words/phrases, punctuation rules, word floor and
  ceiling, any chapter-number meta-reference ban).
- Every locked line of dialogue or beat that may only happen ONCE across
  the whole book, and the exact chapter number it belongs to.

## Step 2: expand each chapter's beat-map entry to roughly 15-20 lines

Not 15-20 lines of atmospheric description. Quality bar per chapter
entry:

1. **3-4 lines of concrete plot** - what physically happens, with named
   places and named objects, not abstractions like "tension rises."
2. **2-3 lines naming every character who appears in this chapter**,
   each with their canon-lock tag repeated inline (do not make the
   generator cross-reference a separate document from memory).
3. **1-2 lines restating the relevant magic-system/world-mechanic facts**
   for THIS chapter, even if already established earlier - never assume
   it carries over correctly on its own.
4. **1-2 lines flagging anything locked**: "the scripted line about
   deciding for someone appears ONLY here," "the Deed's meaning is
   already known as of this chapter, do not re-explain it as news."
5. **1-2 lines anchoring the date**: the exact calendar date this
   chapter lands on, computed from the canon-lock calendar, not left for
   the generator to infer.
6. **1 interior/relationship beat** - specific, not generic ("Kael
   privately resolves to keep her off the most dangerous site, but does
   not act on it yet" rather than "Kael feels conflicted").
7. **1 stakes beat** - what is actually at risk in this chapter,
   concretely.
8. **1-2 lines of callback**, naming the SPECIFIC earlier chapter and
   fact being referenced, not a vague "echoes earlier events."

## Step 3: generate and verify in small batches, not all at once

- Generate 5 chapters at a time, not all 45 in one run.
- After each batch, before generating the next: read at least the first
  and last chapter of the batch in full, run a word-count check and a
  banned-word/banned-name grep, and check every named character/object
  against the canon-lock document.
- Feed the ACTUAL PREVIOUS CHAPTER'S TEXT into the next chapter's
  generation prompt, not just its beat-map summary. Several of Book 2's
  worst breaks (a different Thorne, a different house count) look like
  the generator was shown only the plan for the next chapter and not the
  real prose of the one before it.
- A batch that fails the checks does not get built on. Fix it before
  generating the next batch, the same way chapter-by-chapter drift in
  Book 2 compounded silently for 30+ chapters before anyone caught it.

## Step 4: keep a HANDOFF.md from chapter one, not reconstructed later

Start the book's HANDOFF.md at the same time as the canon-lock document,
before any chapter is generated, in the same format Book 2's HANDOFF now
uses (Canon lock / Status table / Running canon by topic / Plan for next
chapter / Open threads / Findings still live / Process notes / Progress
log). Do not wait until drift is discovered to start tracking it.
