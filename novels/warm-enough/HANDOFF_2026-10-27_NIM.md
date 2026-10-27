# Warm Enough: SESSION HANDOFF (2026-10-27, Claude chat). Read AFTER HANDOFF.md and HANDOFF_2026-10-25_FIFTH.md.

CONFIRMED BY ZIA (2026-10-27): chapters 1 to 7 in `chapters/` were written BY HAND by Zia. The automatic writer (`write-warm-enough.yml`) has NEVER saved a chapter. A session wrongly assumed the schedule wrote chapter 7 because of its commit time. Do not repeat that: check who committed and how before trusting any claim.

CONFIRMED LIVE THIS SESSION: repo intact; connector is aliwaziri10; first missing chapter for `--auto` is 8 (brief 08 reads fine); the checker passes chapters 1, 4, 5, 6; it flags 2 and 3 as under 2,300 words (2036, 2181), and chapter 7 for the word "Splendid". Those are Zia's hand chapters and are not touched.

FINDING: `write_warm_enough.py` pinned the writer to ONE free OpenRouter model and dropped NVIDIA direct, so the only route was about 50 requests a day per account plus frequent "rate-limited upstream" answers. NVIDIA NIM direct (the NVIDIA_API_KEY secret) is free, about 40 requests a minute and about 10,000 a day (directory listings, 2026-10-27). NOT live-tested by Claude: the sandbox cannot reach NVIDIA.

FIX PUSHED (commit fd1d50fbdb4b46601e438adfe6619983bd146c64): new file `scripts/write_warm_enough_nim.py` (blob fcde3766bfe6ebeee341921cc92a55e99bb7dc03). It runs the unchanged `write_warm_enough.py` with this writer chain: NVIDIA `z-ai/glm-5.3`, then `z-ai/glm-5.3-flash`, `nvidia/nemotron-3-ultra-550b-a55b`, `nvidia/nemotron-3-super-120b-a12b`, then the OpenRouter keys with Gemma last. A 404, 429 or bad key moves to the next entry. Tested offline with a mock (404 then 429 then success, sticky choice, all-busy case classed transient, dry run starts at chapter 8).

NOT DONE: the workflow still calls the old script. The connector has no `workflows` permission (403), so Zia must change ONE line in `.github/workflows/write-warm-enough.yml` in the web editor: `scripts/write_warm_enough.py --auto` to `scripts/write_warm_enough_nim.py --auto` (the line starting `timeout 335m python -u`).

NEXT STEPS: (1) confirm the workflow line changed; (2) Zia runs the workflow by hand and pastes the last 40 lines of the log; (3) read the log for "writer chain" and which NVIDIA model answered; if every NVIDIA entry 404s or 403s, the model ids need updating from https://build.nvidia.com/models (free only); (4) when chapter 8 is saved, read it against `briefs/ch08.md`; (5) chapters 1 to 7 still need the human read for voice and brief.
