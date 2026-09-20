# Book 4 canon conflicts and pending fixes (updated 2026-09-20, evening)

## PENDING FIX (do in the next push of story_bibles/amity-falls.json)

- The name "Constance" for Theo's grandmother is WRONG. It collides with
  published characters: Constance Aldridge (Book 1, chapter 32) and a
  Constance Reyes (Book 2, chapter 3). It was pushed on 2026-09-20 without
  reading the grep result that showed this. Replace every "Constance" in the
  bible (Theo's entry, the THEO'S GRANDMOTHER fact, beat 4 and beat 48) with
  "Harriet". Checked: "Harriet Marsh" appears nowhere in Books 1 to 4.
- Do the same grep check before any new invented name.
- Trim the 60-chapter beat map to about 30 (the real story ends near
  chapter 26). Needs Zia's approval.
- Sync `novels/amity-falls-book-4/architecture.md` with the locked canon.
  The pipeline does not read it, so it can drift from the JSON.
- The JSON on this branch is one compact line. Reformat with indentation
  before anyone tries to merge it with `main`, or a merge conflict will be
  unreadable.
- The bible fix lives only on branch book4-progress-saving. `main` still has
  the older bible.

## Not fixed by the bible change

- Chapters 2 to 5, 7, 9, 11 and 12 still contain the old leaks and
  contradictions until they are rewritten.
- The generator saves a chapter even if it contains meta leaks. Add the
  reject-and-regenerate guard in `voxel_cli.py`.
- `story_bible.py` builds the prompt with the header "Prior books in this
  series:", which the model can echo. Change the wording in code.

## Theo's grandmother (locked canon)

Alive, lost about ten years of memory (the decade before 2007) in Drake's
first attempt in Millbrook 19 years ago, cannot say where she was. Name:
Harriet Marsh (not Constance, Eleanor, Adelaide, Denise, Odette or Ambrose).
Old chapters disagree: ch4 (vanished 1987, "Eleanor"), ch5 (clerk typist,
1988 to 1994), ch11 ("Adelaide"). They need rewrites.

## Wren's family (locked canon)

Mother alive and living in the valley (Book 1 and ch3). Father left long
ago. Grandmother, a Finder, is dead. Ch4 says her mother left the valley;
that is wrong. Wren has never paid a large memory debt (ch4 contradicts
this).

## Other

- Ch12 invents a 2019 Drake approach to Priya. Not canon.
- Ch4 says Drake was 23 in 1987 and his father a county clerk. Not canon.
- Surnames Varela (Denise) and Hart (Adelaide) appear only in ch4. Verify or
  remove.
- Beat map items where Wren's gift takes a memory (chapters 9, 11, 17, 21,
  31, 47) sit uneasily with "never paid a large debt". Review when trimming.
