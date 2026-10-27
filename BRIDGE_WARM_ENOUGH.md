# BRIDGE: Warm Enough writer runs on the Wazzaboyzz repo, chapters land here (set up by Zia, 2026-10-27)

This is the ONE allowed exception to `REPO_ACCESS_RULE.md`, and it only exists because `aliwaziri10/Voxel` has no working `NVIDIA_API_KEY` (a copied repo does not copy secrets, and Zia cannot get a new NVIDIA key: build.nvidia.com sign-up is failing, see `SECRETS_CHECK.md`).

## How it works
- Workflow file: `.github/workflows/bridge-warm-enough.yml` in `Wazzaboyzz/Voxel`. Zia pasted it there himself (the Claude connector cannot create workflow files).
- It checks out THIS repo (`aliwaziri10/Voxel`) into a folder called `live`, then runs `scripts/write_warm_enough_nim.py --auto --end 40 --checkpoint` with the `NVIDIA_API_KEY` secret that is saved on the Wazzaboyzz repo.
- Each chapter is committed and pushed straight into `aliwaziri10/Voxel` using the secret `ALI_VOXEL_PUSH_TOKEN` (a fine-grained token made by Zia on the `aliwaziri10` account: only `aliwaziri10/Voxel`, Contents read and write, no expiry). Nothing is written to the Wazzaboyzz repo.
- All writer logic (canon, checks, repair loop) is the code in this repo, so fixes made here apply to the next bridge run automatically.

## Who can start it
Only a person signed in to GitHub as `Wazzaboyzz` (Actions tab, "Bridge Warm Enough", Run workflow, `end` left at 40) in the browser. No Claude profile can start it. Any Claude profile can read the results here.
Link for Zia: `https://github.com/Wazzaboyzz/Voxel/actions/workflows/bridge-warm-enough.yml`

## Rules for Claude profiles
1. Do NOT open, read or edit anything in `Wazzaboyzz/Voxel`. If the bridge needs a change, change it in THIS repo (the script), or give Zia the full new workflow file to paste himself.
2. Do not start the scheduled `Write Warm Enough` run in this repo while the bridge runs. Both would write the next chapter at once.
3. After a bridge run, read `novels/warm-enough/chapters/` and `novels/warm-enough/rejected/` here and judge the chapters against the briefs, as in `novels/warm-enough/HANDOFF.md`.
4. If the run log shows 401 or 403 from NVIDIA, the key on the Wazzaboyzz repo is dead: Zia replaces it there. If the log shows a failure to push, the `ALI_VOXEL_PUSH_TOKEN` secret is wrong or its repo access is missing.

## Verified / not verified (2026-10-27)
- Verified: the NVIDIA-first writer script exists here (`scripts/write_warm_enough_nim.py`, free NVIDIA models, then OpenRouter Gemma as last resort).
- Not verified: that the bridge has completed a run, that the key on the Wazzaboyzz repo still works, and that the token can push. Check the first run's log and the repo history before relying on this.
