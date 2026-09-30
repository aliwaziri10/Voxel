# FINAL_PROOFREAD_PROTOCOL.md — Kindling Line Book 2

Use this for a final full-book proofread pass. Read `HANDOFF.md`'s standing rule
first — this protocol does not override it. Do not start this pass unless Zia
has asked for it in the current session.

## 1. Get the live text, not memory

Download all 45 chapters fresh from `main` (or a specific commit for
verification) via raw.githubusercontent.com. Never proof from a cached copy,
an earlier session's summary, or this repo's `full_manuscript.md` (it goes
stale — regenerate it only at the very end, never read it as source).

## 2. Automated scan (run before any manual read)

For every chapter, check:
- **Word count** (`wc -w` on the real file) against the chapter's target band
  stated in HANDOFF.md.
- **Em-dashes** (`—`) — should be zero.
- **Non-ASCII characters** — flag anything outside plain ASCII punctuation;
  curly quotes are fine, stray encoding artifacts are not.
- **Banned names/terms** from HANDOFF's canon lock — search with **word
  boundaries** (`\bterm\b`), case-insensitive, and print context for every
  hit before flagging it. Substring matching produces false positives (e.g.
  "Hest" matches inside "hesitate"; "nine houses" as a casual vote count is
  not the same as the banned claim that the Council itself has nine houses).
  A hit is only a real violation if the context shows it being used as the
  banned name/concept, not as an incidental substring or a different sense
  of the same words.
- **Hedge words** (particular/something/someone/somewhere/somebody/some/kind
  of/the specific) — word-boundary, case-insensitive. Distinguish the
  banned *vague* sense from a literal, precise use naming a real unspecified
  actor where no better word exists (e.g. "someone left it for us to find"
  can be legitimate; "something happened" almost never is). Read each hit's
  context before deciding.
- **Chapter-number references in prose** (e.g. "chapter 9") — should be zero.
- **Date header** present and internally consistent with the book's date
  math (see HANDOFF's Dates rule).

## 3. Manual read, chapter by chapter

For each chapter, re-read against HANDOFF's canon lock:
- Thorne seal description matches exactly (three strands, drop/flame/feather,
  violet+copper, near-black wax, Malrik's clasp plain silver).
- Site is Anchor Seven only, where the plot requires a site.
- Vote/signer counts match the running canon total for that point in the
  story (check against the previous chapter's count, not just the final
  resolved number).
- No restaged "firsts" (first "I love you," first kiss, first embrace) after
  their canon chapter.
- No living Valerius, no invented mechanisms (ward-taker trial, chosen
  cost-transfer, etc.) banned by canon lock.
- POV and voice consistent with the chapter's stated POV character.
- Continuity with the immediately preceding and following chapter (a
  reference to "yesterday," an object carried over, a wound's healing state).

## 4. Report before fixing

Produce a plain list of real findings (chapter, issue, exact snippet) before
making any edits. Let Zia see the list. Only proceed to fix chapters she
confirms should be fixed in this session — this protocol finds problems, it
does not authorize an unprompted rewrite pass on its own.

## 5. Fixing (only once confirmed)

One chapter at a time: read chapter + the one before, fix in place (edit
existing prose, don't restructure locked beats), rescan the fixed file with
step 2's checks, push, verify via the immutable commit URL, stamp HANDOFF.md
in the same commit.
