#!/usr/bin/env python3
"""
test_humanizer.py - smoke tests for humanizer.py.

No API key needed for most tests: scan(), has_strong_hit(), and
scan_narrative() are pure regex/offline logic. rewrite_pass() and the
humanize_* wrappers are tested with a fake call_llm_fn (no network, no
cost), same pattern as test_content_provider.py's mocked requests.post.

Run:
    pip install pytest --break-system-packages
    python -m pytest test_humanizer.py -v
"""

import humanizer


# --- scan() ------------------------------------------------------------

def test_scan_clean_text_scores_zero():
    text = (
        "Maren pulled the door shut behind her and listened. Nothing moved "
        "in the hall. She counted to ten, then walked to the window and "
        "looked down at the empty street."
    )
    report = humanizer.scan(text)
    assert report["score"] == 0
    assert report["hits"] == []
    assert not humanizer.has_strong_hit(report)


def test_scan_flags_strong_word():
    text = "She wanted to delve into the old letters her mother left behind."
    report = humanizer.scan(text)
    assert humanizer.has_strong_hit(report)
    assert any(h["type"] == "strong_word" and h["pattern"] == "delve" for h in report["hits"])


def test_scan_flags_new_words_from_review_pass():
    # Confirms the 2026-09-19 review-pass additions actually fire.
    text = "The intricate, multifaceted plan was, in the realm of politics, unprecedented."
    report = humanizer.scan(text)
    assert humanizer.has_strong_hit(report)
    patterns_hit = {h.get("pattern") for h in report["hits"] if h["type"] == "strong_word"}
    assert "intricate" in patterns_hit
    assert "multifaceted" in patterns_hit
    assert "unprecedented" in patterns_hit


def test_scan_flags_not_x_but_y():
    text = "It's not just a house, it's a legacy built over three generations."
    report = humanizer.scan(text)
    assert any(h["type"] == "not_x_but_y" for h in report["hits"])
    assert humanizer.has_strong_hit(report)


def test_scan_flags_tricolon():
    text = "He was tired, hungry, and afraid."
    report = humanizer.scan(text)
    assert any(h["type"] == "tricolon_list" for h in report["hits"])


def test_scan_single_hedge_is_weak_alone():
    # One hedge alone should NOT be flagged (weak-alone rule).
    text = "There was something strange about the letter, but she read it twice anyway."
    report = humanizer.scan(text)
    assert not any(h["type"] == "vague_hedge" for h in report["hits"])


def test_scan_two_hedges_are_flagged():
    text = (
        "There was something strange about the letter. Something old moved "
        "beneath the floorboards, too."
    )
    report = humanizer.scan(text)
    assert any(h["type"] == "vague_hedge" for h in report["hits"])


def test_scan_flags_stacked_qualifiers():
    text = "The plan could potentially possibly work, but nobody was sure."
    report = humanizer.scan(text)
    assert any(h["type"] == "stacked_qualifier" for h in report["hits"])
    assert humanizer.has_strong_hit(report)


def test_scan_no_false_positive_on_single_qualifier():
    text = "The plan might work, but nobody was sure."
    report = humanizer.scan(text)
    assert not any(h["type"] == "stacked_qualifier" for h in report["hits"])


def test_scan_flags_emdash_overuse():
    # Well over 4 per 500 words - clearly overused as the default connector.
    sentence = "She walked—slowly—into the room—and stopped—waiting. "
    text = sentence * 8  # ~40 words, 4 dashes each = 32 dashes, way over threshold
    report = humanizer.scan(text)
    assert any(h["type"] == "emdash_overuse" for h in report["hits"])
    assert humanizer.has_strong_hit(report)


def test_scan_no_false_positive_on_occasional_emdash():
    text = (
        "She walked into the room and stopped—waiting for a sound that "
        "never came. The house was quiet. Outside, the wind picked up, "
        "rattling the shutters against the old frame. Nobody else was home."
    )
    report = humanizer.scan(text)
    assert not any(h["type"] == "emdash_overuse" for h in report["hits"])


def test_scan_repeated_openings():
    text = "She walked in. She sat down. She said nothing. He watched her."
    report = humanizer.scan(text)
    assert any(h["type"] == "repeated_openings" and h["count"] >= 3 for h in report["hits"])


# --- rewrite_pass() (mocked LLM) ----------------------------------------

def test_rewrite_pass_returns_clean_text_and_preserves_facts():
    original = "In 1998, Maren Castellan delved into the archives at Ellery Hall."

    def fake_call_llm(system_prompt, user_content):
        # Simulate a rewrite that removes "delved into" but keeps facts.
        return user_content.replace("delved into", "searched")

    clean, ok, dropped = humanizer.rewrite_pass(original, fake_call_llm)
    assert "delve" not in clean.lower()
    assert "1998" in clean
    assert "Maren Castellan" in clean or ("Maren" in clean and "Castellan" in clean)
    assert ok is True
    assert dropped["numbers"] == []
    assert dropped["names"] == []


def test_rewrite_pass_flags_dropped_facts():
    original = "In 1998, Maren Castellan visited Ellery Hall."

    def fake_call_llm(system_prompt, user_content):
        # Simulate a bad rewrite that drops the year and the proper name.
        return "Someone visited a building once."

    clean, ok, dropped = humanizer.rewrite_pass(original, fake_call_llm)
    assert ok is False
    assert "1998" in dropped["numbers"]
    assert "Maren Castellan" in dropped["names"] or "Ellery Hall" in dropped["names"]


# --- humanize_text() / humanize_manuscript() ----------------------------

def test_humanize_text_skips_clean_text():
    text = "Maren opened the window and let the cold air in."
    calls = []

    def fake_call_llm(system_prompt, user_content):
        calls.append(user_content)
        return user_content

    result, meta = humanizer.humanize_text(text, fake_call_llm)
    assert meta["rewritten"] is False
    assert calls == []  # never called the LLM at all


def test_humanize_text_rewrites_dirty_text():
    text = "This unprecedented, intricate plan will delve into every possibility."

    def fake_call_llm(system_prompt, user_content):
        return "This plan will look at every option."

    result, meta = humanizer.humanize_text(text, fake_call_llm)
    assert meta["rewritten"] is True
    assert meta["score_after"] < meta["score_before"]


def test_humanize_manuscript_only_rewrites_dirty_pages():
    pages = [
        {"page_number": 1, "text": "Maren opened the window."},
        {"page_number": 2, "text": "She wanted to delve into the unprecedented archives."},
    ]

    def fake_call_llm(system_prompt, user_content):
        return "She looked through the old archives."

    result = humanizer.humanize_manuscript(pages, fake_call_llm)
    assert result[0]["_humanizer"]["rewritten"] is False
    assert result[1]["_humanizer"]["rewritten"] is True
    assert "delve" not in result[1]["text"].lower()


# --- scan_narrative() ----------------------------------------------------

def test_scan_narrative_flags_neat_resolution():
    text = "After everything, she finally understood what her father had meant."
    result = humanizer.scan_narrative(text)
    assert any(f["type"] == "neat_resolution" for f in result["flags"])


def test_scan_narrative_flags_bodily_only_emotion():
    text = "His chest tightened when he saw the letter on the table."
    result = humanizer.scan_narrative(text)
    assert any(f["type"] == "bodily_only_emotion" for f in result["flags"])


def test_scan_narrative_flags_growth_arc_closer():
    text = "She was no longer the woman who had left this house ten years ago."
    result = humanizer.scan_narrative(text)
    assert any(f["type"] == "growth_arc_closer" for f in result["flags"])


def test_scan_narrative_clean_chapter_has_no_flags():
    text = (
        "\"You're late,\" Maren said, not looking up from the ledger. "
        "\"Traffic,\" Dov said, which was a lie, and they both knew it."
    )
    result = humanizer.scan_narrative(text)
    assert result["flags"] == []


def test_scan_narrative_never_returns_a_score():
    # Explicit contract check: scan_narrative is unvalidated, so it must
    # never expose a score/pass-fail field that could get treated like
    # scan()'s calibrated score.
    result = humanizer.scan_narrative("His chest tightened.")
    assert "score" not in result
    assert "pass" not in result
    assert set(result.keys()) == {"flags"}


if __name__ == "__main__":
    import pytest
    raise SystemExit(pytest.main([__file__, "-v"]))
