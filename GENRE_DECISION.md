# Genre Decision - Book 4 and beyond (DRAFT, updated 2026-10-16)

Status: research round 1 done, round 2 NOT done. Pen-name lanes decided
2026-10-16 (see Decision log). Next book's genre contract, series length and
pen name are still OPEN. No chapters are written until Zia approves a genre
contract. This repo is currently public.

## Decision log

### 2026-10-16 (Zia)

DECIDED:
- Two pen names, two separate reader promises. Do not mix them.
  - Ivy Cassel = romantasy (romance plus fantasy). Series: The Kindling
    Line. Book 1 Borrowed Years and Book 2 Keep Me Past the Fire are
    published. Book 3 Count Me Through the Dark is also published (all three
    books live on KDP, 2 formats each, per the KDP series page).
  - Elif Kessler = slow-burn small-town romance (slow burn is a pacing
    style: the couple takes a long time to get together). Series: Amity
    Falls, 4 books, finished. Later Amity Falls books drifted into
    paranormal mystery; that drift must not be repeated.
- The Kindling Line and Amity Falls are both finished and frozen. See
  novels/FROZEN_DO_NOT_EDIT.md. New work happens only in new books.
- Kindling Line Book 3 was published first, as planned (now live).

KDP LIMIT (changed 2026-09-21): Amazon allows 2 new title creations per
format (ebook, paperback, hardcover) per week. The weekly limit resets every
Sunday at 12:00 AM UTC, which is Sunday 5:30 AM India time. It applies to new
titles only, not to already-published titles. Plan launches one book at a
time.

STILL OPEN:
- Series length for the next book: standalone, 2-book, or 3-book. Working
  view: a shared world of connected standalones (new couple each book, each
  ending in a complete happy ending, first book readable alone), committing
  to later books only if Book 1 sells.
- Which pen name gets the next new book, and in what genre. Working view:
  Ivy if Kindling Line Books 1-2 show strong read-through and the book is
  romantasy; Elif if the book is truly small-town and cozy. Never both.
- Kindling Line Books 1-2 sales and read-through numbers (from the KDP
  dashboard) and Amity Falls per-book numbers are not recorded here. Add
  them when available; they decide the open items above.

Note on the older text below: it was written 2026-09-19 for "Book 4" of
Amity Falls. The Amity Falls series is now frozen, so the "end Amity Falls at
three books or write a Book 4" question (item 6 under Next session) is
closed. The research and the draft genre contract below remain valid as
material for a NEW book. Whether the cozy fantasy romance hybrid belongs under
Elif or a new name is part of the open pen-name decision above.

## Why this file exists

Books 1-3 (Amity Falls) sold nothing in Book 1's first week, and Books 2-3
drifted from romance into paranormal mystery. Before Book 4 or a new series,
the genre, reader promise and series structure must be chosen from data,
written down as a "genre contract", approved by Zia, and fed to the
pipeline.

## What round 1 found (sources at the bottom)

1. Least crowded with strong demand: cozy fantasy. K-lytics (summer 2026,
   via Author Media) scores it 23.1 sales-to-competition: about 60 daily
   sales per top-20 title against about 2,576 competing books. LitRPG is
   second (14.8, about 8,620 competitors) but its books run 550-850 pages.
2. Highest earning ceiling: romance. About 44% of authors earning over
   $10,000/month write romance (21% of all respondents). Cozy mystery and
   paranormal romance also over-index. But romance has over 1,000,000
   English Kindle titles, and the #1 spot needs roughly 3,000-7,000
   sales/day versus 2-10/day on quiet shelves.
3. Cozy mystery: cozy authors appear more often in every income bracket
   above $500/month (Written Word Media 2025). One guide rates it high
   demand and high competition: a middle option.
4. Catalog size beats genre: about 80% of authors with 1-3 books earn under
   $100/month; authors with 25+ books report a median near $3,000/month.
   (Caution: this is partly survivorship. Authors whose books sold kept
   writing. It supports staying in a lane that works, not a target book
   count by itself.)
5. Supply is growing: Kindle SF&F titles rose 18% in a year (about 490 new
   books/day).
6. AI risk: KDP requires disclosure when AI created text or images. A 2025
   YouGov survey found 61% of readers would feel less fulfilled learning a
   book was AI-written. Hachette cancelled and pulled the novel "Shy Girl"
   after AI accusations.
7. Extra round-1b signals (lower-trust sources, direction only): forecasts
   say cozy fantasy is diversifying into cozy romances and cozy mysteries;
   one aggregator says "cozy paranormal" romance grew 31% year on year (its
   sourcing is vague, do not rely on it); romantasy is dominant but needs
   heavy marketing to beat established giants.

## Options, ranked

- Best on paper: pure cozy fantasy. Strongest documented ratio. Weakness:
  new audience, likely a new pen name, and it drops the romance and
  small-town promise Book 1 sold on.
- Second best as first stated: small-town romance with a hook. Highest
  ceiling, but crowded, and its ratio is unverified (K-lytics romance
  report is paid, about $15).
- CHOSEN DIRECTION (hypothesis, needs round 2): small-town cozy fantasy
  romance. New couple each book, same town, gentle magic, happy ending.
  It keeps the romance/small-town promise Zia wanted and sits inside the
  low-competition cozy-fantasy lane. Weakness: NO ratio data exists for
  this exact hybrid. Do not lock it until round 2 measures it. If it
  fails, fall back to pure cozy fantasy.

## Draft genre contract (for the chosen direction)

- Genre: cozy fantasy romance, small town.
- Series structure: each book follows a NEW couple in the SAME town and
  ends happily. Series link = the town and recurring side characters. No
  sequel arc reusing the same couple.
- Magic: gentle, everyday, low-stakes. No rituals, hidden factions, violent
  villains, hereditary curses, or world-ending threats.
- Tone: warm, funny, comforting. Conflict is personal and community-sized.
- Heat: closed door (matches Book 1). Confirm with Zia.
- Must-haves: meet, growing closeness, low point, happy ending; a specific
  cozy hook per book (a shop, craft or food element).
- Never: paranormal mystery, ensemble ritual plots, drift into any other
  genre.
- Length, POV, pricing: NOT decided. Copy the norms of the top 20 books in
  the target Amazon categories during round 2.

## How this plugs into the pipeline that already exists

Reviewed 2026-09-19. `novels/PIPELINE_SPEC.md` and `scripts/pipeline.py`
already define a state machine for Book 4+, but it STARTS at `outline`
(stage 1). Nothing there fixes genre or canon first. Do not build a second
system beside it. Extend it:

- Add two stages before `outline`, in `scripts/book_config.py`'s `STAGES`
  list: `genre_contract` and `story_bible`.
- Add manual gates `genre_contract_approved`, `story_bible_approved` and
  `beat_map_approved`, set only by Zia, so drafting cannot start on the AI's
  say-so. This matches the pipeline's own style (named human gates, as in
  `editorial_review` and `ready_for_upload`).
- Add a `genre_contract` section to `novels/BOOK_CONFIG_TEMPLATE.json`
  (genre, series structure, banned drift list, heat, magic rules) and load
  it into every chapter prompt and into the audit check.
- Seed the story bible with Books 1-3 canon first (see HANDOFF.md problem 6)
  so a same-town sequel cannot contradict them.
- Before editing `book_config.py`, read `pipeline.py` and any tests: stage
  names are used in both. Mark the change untested until Zia runs it.

## Next session (round 2) - do these in order

1. Find sources beyond blogs: live Amazon Best Sellers and Hot New Releases
   pages for cozy fantasy, fantasy romance, small-town romance and cozy
   mystery. Record top-20 ranks, prices, page counts, series or standalone,
   KU or not, and how many titles each category holds. Free, no purchase.
2. Ask Zia before buying K-lytics reports (about $15 each per Author
   Media). Try the free reports first.
3. Test the hybrid: find real "cozy fantasy romance" books, note ranks, and
   estimate demand against competition versus pure cozy fantasy and
   small-town romance. Pick one. Say plainly if the hybrid does not hold.
4. Decide the pen name (a new genre likely needs a new one) and Zia's
   AI-disclosure stance (KDP requires it; readers are wary). Partly
   decided 2026-10-16: see Decision log.
5. Then extend the pipeline as described above, generate the first genre
   contract for Zia to approve, and stop. No chapters before he approves.
6. CLOSED 2026-10-16: Amity Falls is finished and frozen at 4 books.

## Sources

- Author Media, "Zeitgeist: Cozy Fantasy and LitRPG SURGE as Hottest Niches
  in 2026", 2026-07-13 (K-lytics figures are estimates modelled from rank).
- Written Word Media 2025 Indie Author Survey (self-reported, romance
  over-represented); figures repeated by manuscriptreport.com.
- KDP Easy niche guides - SEO-style, lower trust.
- CS Monitor (2026-08-13) for the YouGov figure; Wikipedia for "Shy Girl".
- Books Shelf, "What's Going to Be Hot in 2026" (a prediction, not data);
  commercialtoolry.com and accio.com summaries (lower trust, direction only).
- KDP weekly limit: Vappingo "How Many Books Can You Publish on Amazon KDP
  Per Week" and ALLi (selfpublishingadvice.org) news summary, both
  2026-09.
