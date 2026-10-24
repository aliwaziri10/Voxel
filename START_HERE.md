# START HERE: every Claude session reads this first

Repo: `aliwaziri10/Voxel`. Owner: Zia, browser-only, no terminal, dictates by voice (names come out garbled: "Ivy Castle" = Ivy Cassel, "Alif" = Elif, "humanizer pie" = humanizer.py).

## Rules Zia set (2026-10-22)
1. Before acting, read the repo yourself. Reading is always allowed and expected. Do not ask Zia what a file says.
2. Then talk to Zia before doing work. Tell him plainly if he is right or wrong. Do not just agree.
3. Terse replies. One step at a time. Every path, URL or value in its own code block.
4. Times in IST. Chapters 2,300 to 2,700 words, ceiling 3,000.
5. Push work to the repo as it goes (a session can end without warning).
6. At about 80 percent of the session limit, write or update a handoff file in `novels/` and tell Zia.

## Reading order for any Voxel or novel factory work
1. `novels/EDITORIAL_CHARTER.md`
2. `novels/FACTORY_SESSION_HANDOFF.md`
3. `novels/FACTORY_ADDENDUM.md` (wins over the next two where they disagree)
4. `novels/FACTORY_DECISIONS.md`
5. `novels/FACTORY_HANDOFF.md`
6. `GENRE_DECISION.md`, `novels/FROZEN_DO_NOT_EDIT.md` (frozen books are never edited)
7. Humanizer chain: `humanizer.py`, `test_humanizer.py`, `novels/HUMAN_WRITING.md`, `PROOFREAD_RULES.md`

## One-time setup: Claude Project with the repo files loaded (browser only)
Goal: every chat opened inside the Project starts with the key files already loaded, so no session is clueless. Done by hand by Zia on 2026-10-22; result of the final click NOT yet confirmed when this was written. Check the Project's Context box first. If the files are already listed, skip to "Keep it fresh".

1. Open claude.ai, then Projects, then the project named **Github**. (Press Esc if the pin/archive/delete menu is open. Never click Delete.)
2. On the right, click **+** next to **Context**.
3. Click **GitHub**.
4. Choose repo `aliwaziri10/Voxel` (search for it if not shown).
5. In the main list, tick ONLY these files, no folders: `START_HERE.md`, `GENRE_DECISION.md`, `PLAYBOOK.md`, `PROOFREAD_RULES.md`, `PROOFREAD_UPGRADE_HANDOFF.md`, `ARCHITECTURE.md`, `humanizer.py`.
6. Click the folder name **novels** (the word, not its checkbox) and tick ONLY: `EDITORIAL_CHARTER.md`, `FACTORY_SESSION_HANDOFF.md`, `FACTORY_ADDENDUM.md`, `FACTORY_DECISIONS.md`, `FACTORY_HANDOFF.md`, `HUMAN_WRITING.md`, `FROZEN_DO_NOT_EDIT.md`, `PIPELINE_SPEC.md`. Never tick the whole `novels` folder: it is 276 percent of the size limit.
7. Click the black **Add files** button at the TOP RIGHT of the picker (not the bottom). Confirm the files appear in the Context box.

## Keep it fresh
- The Project does NOT update by itself. After any push of a handoff or decision file, Zia clicks the **Sync** icon (or "Sync now") in the Context box.
- Open every new factory chat INSIDE the Project, not from the main New button.
- A Project keeps its own memory, separate from Zia's general memory.
- Sync can hang on some accounts. If it does, tell Zia and fall back to reading files with the GitHub connector.

## Tools that do not work for Zia
claude-mem (thedotmack/claude-mem) is a Claude Code terminal plugin. It cannot be installed from the browser. Do not suggest it again.
