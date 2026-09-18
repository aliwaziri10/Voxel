#!/usr/bin/env python3
"""
book_config.py — Schema, loader, and validator for a Voxel novel's
per-book pipeline config.

One JSON file per book (e.g. novels/amity-falls-book-4/book_config.json)
replaces the previous pattern of trim size / word floor / series name
being hardcoded or re-typed into each script's CLI args. pipeline.py and
kdp_metadata.py both import this module rather than parsing JSON ad hoc,
so the schema only lives in one place.

This is infrastructure only — it does not read or write chapter prose,
and it does not touch Books 1-3 (Where the Frost Doesn't Reach, Amity
Falls Book 2, Amity Falls Book 3), which are already published/complete
and locked per novels/EDITORIAL_CHARTER.md's no-retroactive-padding rule.
Book 4+ is the intended scope.

Usage (as a library):
    from book_config import BookConfig
    cfg = BookConfig.load("novels/amity-falls-book-4/book_config.json")
    cfg.stage                  # current pipeline stage, e.g. "drafting"
    cfg.require_gate("editorial_review_complete")   # raises if not True
    cfg.advance_to("mechanical_qa")
    cfg.save()
"""
import json
import os
import sys
from datetime import datetime, timezone

# Fixed, ordered pipeline stages. This order is the state machine.
# pipeline.py refuses to run a stage's script unless the config's
# current stage matches it AND that stage's prerequisite gates (if any)
# are satisfied -- see STAGE_GATES below. No stage may be skipped.
STAGES = [
    "outline",             # beat_map.md exists (produced outside this
                           # pipeline, via voxel_cli.py's beat-map step)
    "drafting",            # chapters/chapter_NN.md files being written
    "editorial_review",    # MANUAL, per EDITORIAL_CHARTER.md: strict
                           # sequential continuity/voice/canon read.
                           # Never automated -- see module docstring.
    "mechanical_qa",       # manuscript_qa.py run, 0 CONFIRMED-FIX left
    "manuscript_build",    # build_manuscript.py run -> .docx
    "cover_build",         # build_cover.py run -> cover .pdf
    "kdp_metadata",        # kdp_metadata.py run -> metadata package
    "ready_for_upload",    # Publisher-role final gate (human sign-off)
    "published",
]

# Gates that must be True in a book's manual_gates dict before pipeline.py
# will let that book ADVANCE OUT of the named stage. These are exactly the
# things EDITORIAL_CHARTER.md says a mechanical script cannot verify:
# a human (or an AI session doing the actual sequential read) has to set
# these by hand, in the config, after doing the real work and logging it
# in that book's own HANDOFF.md.
STAGE_GATES = {
    "editorial_review": [
        "continuity_voice_canon_review_complete",
        "banned_word_sweep_complete",
        "hedge_sweep_complete",
    ],
    "ready_for_upload": [
        "name_collision_audit_complete",
        "real_person_name_check_complete",
        "back_cover_blurb_approved",
        "cover_image_approved",
        "kdp_metadata_approved",
        # Amazon KDP requires AI-assisted books to carry a disclosure on
        # the copyright page AND be declared as such during the backend
        # upload -- skipping this risks the KDP account, not just this
        # book. Confirmed by surveying public KDP-automation tooling
        # (see novels/PIPELINE_SPEC.md, "External research" section).
        "ai_disclosure_included",
    ],
}

REQUIRED_TOP_LEVEL_FIELDS = [
    "book_id", "title", "series", "book_number", "author", "publisher",
    "trim", "word_floor_min", "word_floor_max", "chapters_dir", "stage",
]


class BookConfigError(Exception):
    pass


class BookConfig:
    def __init__(self, data, path):
        self.data = data
        self.path = path

    # -- loading / saving --------------------------------------------
    @classmethod
    def load(cls, path):
        if not os.path.exists(path):
            raise BookConfigError(
                f"No book config at {path}. Copy "
                f"novels/BOOK_CONFIG_TEMPLATE.json to that path and fill "
                f"it in first -- pipeline.py will not invent book metadata."
            )
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
        cfg = cls(data, path)
        cfg.validate_schema()
        return cfg

    def save(self):
        with open(self.path, "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=2, ensure_ascii=False)
            f.write("\n")

    # -- schema ---------------------------------------------------------
    def validate_schema(self):
        missing = [k for k in REQUIRED_TOP_LEVEL_FIELDS if k not in self.data]
        if missing:
            raise BookConfigError(
                f"{self.path} is missing required fields: {missing}. "
                f"See novels/BOOK_CONFIG_TEMPLATE.json for the full schema."
            )
        if self.data["stage"] not in STAGES:
            raise BookConfigError(
                f"{self.path} has unknown stage '{self.data['stage']}'. "
                f"Valid stages, in order: {STAGES}"
            )
        self.data.setdefault("manual_gates", {})
        self.data.setdefault("kdp", {})
        self.data.setdefault("history", [])

    # -- stage / gate logic ----------------------------------------------
    @property
    def stage(self):
        return self.data["stage"]

    @property
    def stage_index(self):
        return STAGES.index(self.stage)

    def gates_for(self, stage):
        return STAGE_GATES.get(stage, [])

    def unmet_gates(self, stage=None):
        stage = stage or self.stage
        gates = self.data.get("manual_gates", {})
        return [g for g in self.gates_for(stage) if not gates.get(g, False)]

    def require_gate(self, gate_name):
        if not self.data.get("manual_gates", {}).get(gate_name, False):
            raise BookConfigError(
                f"Gate '{gate_name}' is not set for {self.data['book_id']}. "
                f"This is a manual editorial gate per EDITORIAL_CHARTER.md "
                f"-- it must be set to true in {self.path} by whoever "
                f"actually did and logged that work, not auto-set by a script."
            )

    def can_advance(self):
        return not self.unmet_gates()

    def advance_to(self, new_stage, note=""):
        if new_stage not in STAGES:
            raise BookConfigError(f"Unknown stage '{new_stage}'.")
        current_idx = self.stage_index
        new_idx = STAGES.index(new_stage)
        if new_idx != current_idx + 1:
            raise BookConfigError(
                f"Refusing to move '{self.data['book_id']}' from "
                f"'{self.stage}' to '{new_stage}': stages cannot be "
                f"skipped or reordered. Next allowed stage is "
                f"'{STAGES[current_idx + 1]}'."
            )
        unmet = self.unmet_gates()
        if unmet:
            raise BookConfigError(
                f"Refusing to advance out of '{self.stage}': unmet manual "
                f"gates {unmet}. Set these to true in {self.path} only "
                f"after actually doing and logging that work."
            )
        self.data["stage"] = new_stage
        self.data["history"].append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "from_stage": STAGES[current_idx],
            "to_stage": new_stage,
            "note": note,
        })

    def log(self, message):
        self.data["history"].append({
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "stage": self.stage,
            "note": message,
        })


def main():
    # Small CLI for sanity-checking a config file without importing it.
    if len(sys.argv) != 2:
        print("Usage: python book_config.py <path/to/book_config.json>", file=sys.stderr)
        sys.exit(1)
    cfg = BookConfig.load(sys.argv[1])
    print(f"book_id: {cfg.data['book_id']}")
    print(f"stage:   {cfg.stage}  (index {cfg.stage_index}/{len(STAGES) - 1})")
    unmet = cfg.unmet_gates()
    if unmet:
        print(f"unmet gates blocking advance out of this stage: {unmet}")
    else:
        print("no unmet gates for the current stage.")


if __name__ == "__main__":
    main()
