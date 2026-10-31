# External tools handoff (2026-10-31, Claude chat session, Zia)

Notes only. No chapter, config or workflow was changed this session.

## Rule for every session
Run these tools ONLY on unpublished books. Published and frozen: Kindling Line, Amity Falls, Proof of Home (novels/proof-of-home/PUBLISHED.md, 2026-10-25). A scan of a published book counts as a proofreading pass, so do not do it. Check for PUBLISHED.md or FROZEN_DO_NOT_EDIT.md first.

## Status: nothing has been run yet
The chat sandbox could not install packages (pypi.org fails DNS, proxy bypass). So no tool below has been executed. Everything here comes from reading each repo page, license and release on GitHub on 2026-10-31.

## Verified on GitHub (2026-10-31)
- vale-cli/vale (moved from errata-ai/vale): MIT, v3.25.1 released 2026-10-22. Rule files in YAML. Fit: turn the Charter's tracked tells (particular, "the specific", "the kind of", some/something hedges) into a Vale existence rule.
- Automattic/harper: Apache-2.0, v3.0.0 released 2026-10-27. Offline grammar checker. Second opinion next to the LanguageTool pass. CLI asset name NOT verified.
- textstat/textstat: MIT, pushed 2026-10-26. Reading level numbers. proofread rules say readability is advisory only, never a pass/fail gate.
- sam-paech/slop-score: code, slop lists in data/ and js/ are MIT (GitHub shows "Other" because wordfreq files are Apache-2.0 and CC-BY-SA 4.0). Browser tool, no command line. Needs a small Node wrapper. Do not copy data/large_en.msgpack.gz into Voxel; download at run time. Overlaps heavily with scripts/humanizer_pass.py (negative parallelism, tics, cliches already covered). Real extra value: data/slop_list.json, slop_list_trigrams.json, and MATTR lexical diversity.
- sam-paech/slop-forensics: MIT, pushed 2025-11-01. Needs PyQt5, ete3, pandas and more. Later, advanced.
- w3c/epubcheck: BSD-3-Clause (the earlier answer said MIT; that was wrong), v5.4.0 released 2026-09-15. Only needed if an EPUB is built.
- explosion/spaCy: MIT, very active. Idea: load canon names from story_bibles/*.json as an EntityRuler, list PERSON names per chapter that are not in canon. This would improve scripts/continuity_extract.py, which says its own name grouping is noisy.
- booknlp/booknlp: MIT, last push 2024-07-31, so old. Heavy (torch). Python version need NOT re-verified this session; check before use.
- amperser/proselint: BSD-3-Clause, GitHub is a mirror (main repo on Codeberg). Not yet looked at in detail.

## Not found or not recommended
- Proseview (ourarash/prosview): not found on GitHub. Dropped unless Zia confirms the address.
- Syntaf/vale-llm-slop: MIT but built for software docs and agent prose, not fiction. Not a fit.
- Pandoc (GPL): only for EPUB, run as a separate command. build_manuscript.py already makes the .docx.
- Binoculars: heavy models, old. Left out.

## Unused, for the next session (in this order)
1. Vale with a Charter-tells rule file (reports only).
2. textstat numbers per chapter (advisory only).
3. Harper in Actions next to the LanguageTool pass (confirm the CLI download first).
4. slop-score word and trigram lists, ideally through a small Node wrapper, compared with the humanizer_pass.py table.
5. spaCy EntityRuler over canon names for continuity.
6. EPUBCheck, only if an EPUB is ever built.
7. slop-forensics (own tell list), BookNLP, proselint: later or optional.

## How to run (Zia's rule: browser only)
A draft workflow, read-only, was prepared in chat (ext-tools-readonly.yml). Claude cannot edit .github/workflows, so Zia pastes it. It refuses published books and writes reports only.

## Problems noticed, not changed
- STATUS.md still has the claim line for ch35 to ch40 (2026-10-28). Check whether that session is finished before reading those chapters.
- book_config.json says stage planning_done_no_chapters although chapters 1 to 38 exist.
- .github/workflows/proofread-languagetool.yml defaults to novels/proof-of-home/chapters, which is published. Change the default.
