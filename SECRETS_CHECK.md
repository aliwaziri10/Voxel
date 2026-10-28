# SECRETS CHECK: do this EVERY session, BEFORE any run, test or "the API keys failed" diagnosis

Set by Zia on 2026-10-27, after many days of failed runs. Standing rule. Do not remove this file.

## Why this exists
`aliwaziri10/Voxel` is a COPY (fork) of `Wazzaboyzz/Voxel`. Copying a repo does NOT copy its GitHub secrets, and a secret's value can never be read back. For days the live repo had no `NVIDIA_API_KEY` (it was saved only on the original), so the writer could only use OpenRouter's free models, which hit daily caps and "busy upstream" errors. Nobody checked the secret names, so the failure was blamed on code and models instead.

## The check (Claude cannot see secrets or their names, so Zia does this on the live repo)
1. Tell Zia to open the secrets page of the LIVE repo only:
   `https://github.com/aliwaziri10/Voxel/settings/secrets/actions`
2. Compare the names on that page with the names the workflow reads (`env:` block of the workflow being run). For `write-warm-enough.yml` those are: `NVIDIA_API_KEY_VA` (the NVIDIA key Zia generated on the Velorique Atelier account; the workflow maps it into the script's `NVIDIA_API_KEY` variable with `NVIDIA_API_KEY: ${{ secrets.NVIDIA_API_KEY_VA }}`), `OPENROUTER_API_KEY`, `OPENROUTER_API_KEY_2` to `OPENROUTER_API_KEY_6` (and the unused `OPENAI_API_KEY`, `OPENAI_MODEL`).
3. Any name missing: Zia creates it himself (New repository secret, paste the key into the Secret box). NEVER ask Zia to paste a key into the chat.
4. A name that exists can still be dead (expired or revoked). A 401 or 403 in the run log means replace the key, not the code.
5. Only after steps 1 to 4, read the run log. Do not rewrite code or switch models before this check.

## What was seen (names only, never values)
- 2026-10-27, `aliwaziri10/Voxel`: `OPENROUTER_API_KEY`, `_2` to `_7` all present ("last month"). The top of the list (names before the letter O) was NOT shown, and `NVIDIA_API_KEY` was not seen there.
- 2026-10-27, original `Wazzaboyzz/Voxel` (Zia looked in his browser): `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN`, `GEMINI_API_KEY`, `NVIDIA_API_KEY`. None of these reach the live repo. Claude never opens the original (see `REPO_ACCESS_RULE.md`); Zia may look at its secrets page himself.
- 2026-10-27: Zia generated a new NVIDIA key on the Velorique Atelier account and named the secret `NVIDIA_API_KEY_VA` (VA marks who created it). Whether it is saved on `aliwaziri10/Voxel` is NOT yet confirmed. Any workflow that needs it must map it: `NVIDIA_API_KEY: ${{ secrets.NVIDIA_API_KEY_VA }}`. A secret with a different name is silently ignored.

## Limits of the Claude connector (so no session wastes time)
- It cannot list, read or create secrets.
- It cannot create or edit anything under `.github/workflows/` (403 "without `workflows` permission"). Workflow changes are made by Zia in the GitHub web editor, with the full file given to him in a code block.
