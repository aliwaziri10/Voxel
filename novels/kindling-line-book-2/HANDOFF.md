# HANDOFF — Kindling Line Book 2 Polish Pass

Read `../EDITORIAL_CHARTER.md` first, then this file, then `brief.txt` and
`CONTINUITY_PLAN_ch10-20.md`. Update this file in the SAME commit as any
chapter edit. Quality only, no budget constraint. Never strip em-dashes on a
structurally broken chapter; fix structure first. Strict sequential order.

## Canon lock for ch.10-20 — do not deviate

- **Site:** Anchor Seven (Lower Reach ropewalk sublevel). Ch.13-15
  infiltration happens ONLY here. No other site (not Lower Ward Annex, not
  "three miles north," not Graywater Hollow, not a waystation).
- **Thorne seal, the only correct wording:** three strands, unbroken,
  knotted; a drop, a flame, a feather at each terminus; house colors violet
  and copper; wax dark, near-black. No red wax, no crown, no vine, no hawk,
  no motto.
- **Scripted line** ("I'm not asking you to tell me everything. I'm asking
  you to stop deciding what I don't need to know.") belongs ONLY to ch.16-18.
- **Ward Deed's full legal meaning** (clause 7/12/19 chain) is understood
  ONLY in ch.20. Ch.13-15: discovered, not understood.
- No chapter may reference its own or another chapter's number in prose.
- No em dashes, no "particular", no "some/something ___" hedges.

## Status (verified against live files 2026-09-28)

- **Ch.1-9:** rewritten/confirmed clean per earlier sessions.
- **Ch.10:** clean structurally. OPEN MECHANICAL DEFECT: the first line is
  HTML-escaped (`&lt;!-- chapter_date ... --&gt;`). Must be raw `<!-- ... -->`.
  Fix by full-file push (no other change needed).
- **Ch.11:** REWRITTEN AND STAMPED 2026-09-28 (commit `f129fd09`). Canon-lock
  clean. 2,130 words, 0 em dashes, 0 banned tells.
- **Ch.12:** REWRITTEN AND STAMPED 2026-09-28 (commit `9f7ea6de`). Canon-lock
  clean. 1,834 words, 0 em dashes, 0 banned tells.
- **Ch.13-15:** BROKEN, not yet rewritten. Ch.13 confirmed broken live this
  session: waystation site, red wax "thorned crown / Endure and Bind" seal,
  scripted line used, Deed read and fully explained. Ch.13 also has no
  chapter_date header. Full rewrite needed, in order.
- **Ch.16-45:** UNCHECKED. Treat as broken until verified.

## Canon added by the ch.11-12 rewrites (ch.13 onward must honor)

- Council granted the petition: both names (Ashworth and Vane), entry to
  Anchor Seven's sublevel from first bell 21 Sunspire through 23 Sunspire.
  Council-appointed observer rider: petitioners may propose. Sol and Kael
  proposed Renn (surveyor, holds Council survey commission).
- Thorne moved its reform hearing from 21 to 24 Sunspire, citing Kael's
  "forthcoming report" (he has written none). An eighth house signed
  (ch.12), so the 24th hearing now includes the VOTE.
- Two Ashworth wardens (Joren, older, scar on hand; Mara, 20 years' service)
  hold the ropewalk floor; they answer jointly to Kael and Sol; nothing
  they see goes upstairs without both names.
- Hooded Thorne watcher (from ch.9) now shows itself in daylight, copper
  cloak clasp bearing the Thorne knot; a fresh knife-scratched "Seven" on
  the anchor post of the rope bridge.
- Ch.12 site facts: sealed hatch at far end of the ropewalk gallery, re-laid
  cream mortar (not Accord grey lime), iron ring bright on the inner curve
  (lifted recently). Old splicer Ansa (lives over the tar-shop) says a
  ward-lamp at the foot of the stair glows blue every dusk for years; a thin
  ink-cuffed clerk (Varel, unnamed by her) watched the hatch 5-6 weeks ago;
  copper-collared men asked about her lodgers last week.
- Ch.12 ends at dusk 20 Sunspire: lamp already lit though nobody passed the
  hatch, so someone is inside; window opens in ~11 hours; Kael asks Sol
  "What do you say?" Ch.13 must open by answering that (they wait for the
  lawful window; do not let Kael decide alone).
- Dates: ch.14 header is 22 Sunspire, ch.15 header is 23 Sunspire (the 23rd
  is also the date on the Thorne pass Kael was handed in ch.8). Ch.13 = 21.

## Findings for the author or later sessions (not yet resolved)

1. **Pass conflict (editorial judgment call).** In ch.10 Kael says "Thorne's
   pass called it decommissioned" to Sol, so Sol knows about the Anchor Seven
   pass from ch.8. Brief rule 5 (ch.16-18) needs a DIFFERENT Thorne-sealed
   pass in Kael's coat, to a site he never mentioned, dated a day he claimed
   was paperwork. Ch.16 must use a new site/pass, not the ch.8 pass.
2. Ch.9 says "nine days" since the Contract on 17 Sunspire (should be eight
   if it went public 9 Sunspire). Minor; not touched.
3. Ch.13 old draft contains a Kael-conceals-then-admits beat about the Deed
   and a full legal reading. Both belong later (ch.20). Reusable: the harmonic
   ring-lock, tripwire lattice with hidden secondary trigger and dart trap,
   but relocate to Anchor Seven and remove the strongroom Deed reading.
4. Old ch.12 line "A house that has already paid the cost has earned the
   right to control who pays it next" was NOT carried into the rewrite. It
   still has to be SPOKEN as Thorne dialogue somewhere (brief rule 1). Verify
   whether any surviving chapter already has it before adding.

## Known landmarks to watch for once chapters reach them

- Ch.16-18: locked entry-pass-in-coat + confrontation scene (leaked into
  ch.4,5,6,7,orig-8,12,13,15; ch.12 and ch.13 now handled/pending).
- Ch.17: replace formal "Co-leadership. Starting now." with a private
  promise only (formal cession is ch.39).
- Ch.20: Deed fully understood; longest chapter, check trim.
- Ch.26-28: Kael's solo mistake backfires; first "I love you." Ch.28: strip
  settled "Equals, starting now" line and the repeated scripted line.
- Ch.33-35: rupture, must stay unresolved.
- Ch.38: first on-page intimate scene.
- Ch.40: check for chapter-number references.
- Ch.41: cost-transfer mechanic involuntary and non-redirectable.
- Ch.45: Keeper reveal institutional, never a named person; fix seal.

## Other notes

- `kindling-line-book-2_full_manuscript.md` is OUT OF SYNC with `chapters/`.
  Regenerate at the very end.
- Word floor: 1,800 words. Verify by reading, not by old logs.
- Defect categories to scan any unchecked chapter for: wrong magic system,
  invented soulbond (brief rule 15), wrong Thorne seal, front-loaded plot,
  corrupted or non-Latin characters, under word floor, chapter-number
  meta-references.
- Repo owner is `aliwaziri10/Voxel`. If a separate "ZB Voxel" repo exists,
  its handoff was not reachable in this session; this repo's live files
  showed ch.11 and ch.12 still broken before this pass.

## Progress log (one short line per session/chapter)

- 2026-09-28: ch.10 rewritten clean, commit `09a74af8`.
- 2026-09-28: ch.11 first rewrite violated canon lock (wrong seal, site,
  restaged confrontation).
- 2026-09-28 (proofread session): ch.11 REWRITTEN + STAMPED `f129fd09`;
  ch.12 REWRITTEN + STAMPED `9f7ea6de`. Both verified by byte-size match
  after push. Ch.13 confirmed broken live. Next: ch.13, in order.
