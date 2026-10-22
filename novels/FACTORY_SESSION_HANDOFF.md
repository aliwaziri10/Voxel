# Novel Factory: SESSION HANDOFF (2026-10-22, written at 92 percent of session limit)

Read in this order: `novels/EDITORIAL_CHARTER.md`, `novels/FACTORY_HANDOFF.md` (verified repo facts and build plan), `novels/FACTORY_DECISIONS.md` (decisions), then this file. Repo is `aliwaziri10/Voxel`. Zia is browser-only and dictates by voice (names come through garbled, e.g. "Ivy Castle" = Ivy Cassel, "Alif" = Elif).

## Everything Zia has asked for, in order
1. GitHub must do, for at least 50 novels (3 or 4 per series), everything done by hand for Warm Enough, without missing a point: canon lock, name audit, plan, tempo and heat audit, briefs of 15 to 20 lines, writer, proofread, daily cron.
2. Chapters 2,300 to 2,700 words, up to 3,000 at most. Intensity very high.
3. Talk to him before acting. Say plainly if he is right or wrong; do not just agree.
4. Build up to 15 to 25 books per pen name (he read that 15 to 20 books help sales). Delegated the exact target to Claude. Chosen: 20 each, extendable to 25.
5. Two genres: Elif Kessler = slow burn; Ivy Cassel = fast-paced Gen Z style romantasy, high heat. He says Kindling Line is that line. Claude read it: adult romantasy, open door, non-graphic, two to three scenes, no Gen Z voice. Decision: match the repo, keep the new Ivy Cassel series open-door and fast.
6. Every plot and every setting different (registry check in FACTORY_DECISIONS.md).
7. Published: Amity Falls 1 to 4, Proof of Home, Kindling Line 1 to 3. EXACT RELEASE DATES AND THE 20-DAY RULE ARE IN `novels/RELEASE_DATES.md` (last release: Proof of Home, 2026-10-21; earliest next release 2026-11-10).
8. NEW, NOT STARTED: study the most successful, best-selling authors in these genres and make the factory follow what works, so Zia can be among them. Needs real research (web search): what top romantasy and cozy romance authors do on series length, release pace, chapter hooks, tropes, blurbs, pricing and covers. Report findings to Zia before building on them.
9. Humanizer must be top-notch. Zia says the humanizer scripts were already written after research (internet and Wikipedia). Existing pieces to verify and reuse, not rebuild: `novels/HUMAN_WRITING.md`, `scripts/novel_guard.py`, `scripts/proofread_novel.py`, `scripts/proofread_core.py`, `scripts/languagetool_pass.py`, `humanizer.py` (root, referenced by content_provider). Next session: read them, run them on the first generated chapters, and confirm they catch the AI tells listed in HUMAN_WRITING.md. Wire them into the factory writer.

## State of the work
- Pushed: FACTORY_HANDOFF.md, FACTORY_DECISIONS.md, this file.
- NOT built: factory/ROADMAP.json, scripts/novel_factory.py, general writer (scripts/write_warm_enough.py is hard-coded to Warm Enough), workflow file. No workflow exists to run Warm Enough yet; copy `.github/workflows/write-kindling.yml`.
- Warm Enough has 40 briefs, canon lock, heat ladder; no chapters written. The writer has never been run.
- Open facts: repo public or private is unknown (affects scheduled run minutes). Workflow files may need Zia to paste them in the web editor if the connector refuses them.

## Next steps, in order
1. Tell Zia the plan and get a go (he wants to be told before actions).
2. Research best-selling authors (item 8) and report.
3. Verify the humanizer chain (item 9).
4. Build the general writer, factory planner, registry and workflow; test with a mock model before pushing.
5. Run Warm Enough first. Zia reads one sample chapter and the audit report before the rest is queued.
6. Then Ivy Cassel series, then Elif Kessler.
