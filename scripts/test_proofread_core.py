"""Tests for scripts/proofread_core.py. No network, no LLM."""
import os

import proofread_core as pc

CLEAN = ("The morning was cold and the harbor was quiet. " * 8).strip()


def rules(text, **kw):
    return {f.rule for f in pc.check_text(text, "x.md", pc.Options(**kw))}


def tiers(text, **kw):
    return {f.tier for f in pc.check_text(text, "x.md", pc.Options(**kw))}


def test_clean_text_passes():
    assert pc.verdict(pc.check_text(CLEAN, "x.md")) == "PASS"


def test_soft_hyphen_and_zero_width_are_critical():
    assert "K01" in rules(CLEAN + " co­work")
    assert "K02" in rules(CLEAN + " a​b")
    assert pc.verdict(pc.check_text(CLEAN + " co­work", "x.md")) == "BLOCKED"


def test_digit_inside_word_critical_but_dates_ok():
    assert "K03" in rules(CLEAN + " he1lo there")
    assert "K03" not in rules(CLEAN + " In 1986 at 3pm the 2nd door.")


def test_leaked_markup_and_placeholders():
    assert "K04" in rules(CLEAN + " <div>x</div>")
    assert "K04" in rules(CLEAN + " TODO fix this")
    assert "K05" in rules(CLEAN + " As an AI I cannot.")


def test_html_comment_header_is_ignored():
    text = "<!-- chapter_date: 14 Emberfall -->\n" + CLEAN
    assert "K04" not in rules(text)


def test_inline_page_number_line():
    assert "K06" in rules(CLEAN + "\n\n12\n\n" + CLEAN)


def test_empty_chapter_and_base64():
    assert "K07" in rules("too short")
    assert "K08" in rules("QUJDREVGR0hJSktMTU5PUFFSU1RVVldYWVo" * 6)


def test_doubled_word_flagged_but_had_had_ok():
    assert "D01" in rules(CLEAN + " She went to the the store.")
    assert "D01" not in rules(CLEAN + " She had had enough.")


def test_unbalanced_quotes():
    assert "D02" in rules(CLEAN + ' He said "hello there.')
    assert "D02" not in rules(CLEAN + ' He said "hello there."')
    assert "D02" in rules(CLEAN + " “Open only.")


def test_mixed_quote_styles_distracting():
    assert "X08" in rules(CLEAN + ' "one" and “two”')


def test_repeated_punctuation():
    assert "D03" in rules(CLEAN + " Well,, fine.")
    assert "D03" in rules(CLEAN + " Wait.. what")
    assert "D03" not in rules(CLEAN + " Wait... what")


def test_emdash_house_rule_and_override():
    text = CLEAN + " It was—odd."
    assert "D04" in rules(text)
    assert "D04" not in rules(text, allow_emdash=True)
    assert "D04" not in rules(CLEAN + "\n\n---\n\n" + CLEAN)


def test_spacing_rules():
    assert "X02" in rules(CLEAN + " Really ?")
    assert "X03" in rules(CLEAN + " Yes,but no.")
    assert "X03" in rules(CLEAN + " It ended.The next day.")
    assert "X04" in rules(CLEAN + " two  spaces")
    assert "X03" not in rules(CLEAN + " At 3:30 on Mr. Smith's clock.")


def test_dialogue_tag_period():
    assert "X05" in rules(CLEAN + ' "Come here." she said.')
    assert "X05" not in rules(CLEAN + ' "Come here," she said.')


def test_a_an():
    assert "X06" in rules(CLEAN + " She ate a apple.")
    assert "X06" not in rules(CLEAN + " She saw a unicorn and a one-eyed cat.")
    assert "X07" in rules(CLEAN + " He wore an coat.")
    assert "X07" not in rules(CLEAN + " It took an hour.")


def test_ellipsis_mixing():
    assert "X09" in rules(CLEAN + " Well… and then... nothing.")


def test_us_spelling_and_britishisms():
    assert "S01" in rules(CLEAN + " The colour of her coloured scarf.")
    assert "S01" in rules(CLEAN + " She was travelling and realised it.")
    assert "S01" not in rules(CLEAN + " The color of her scarf.")
    assert "S02" in rules(CLEAN + " Whilst waiting, mum called.")


def test_word_band_is_review_only_never_blocking():
    assert "W01" in rules(CLEAN, min_words=2300)
    assert pc.verdict(pc.check_text(CLEAN, "x.md", pc.Options(min_words=2300))) == "PASS"
    assert "W02" in rules(CLEAN, max_words=10)


def test_verdict_levels():
    assert pc.verdict([]) == "PASS"
    f = pc.Finding(pc.DESTRUCTIVE, "D01", "x", 1, "", "")
    assert pc.verdict([f]) == "NEEDS-REVISION"
    c = pc.Finding(pc.CRITICAL, "K01", "x", 1, "", "")
    assert pc.verdict([f, c]) == "BLOCKED"


def test_frozen_guard_blocks_published_books():
    for p in ("novels/amity-falls-book-4/chapters", "novels/kindling-line-book-3/chapters",
              "novels/where-the-frost-doesnt-reach/chapters",
              "NOVELS/Kindling-Line-Book-1/chapters"):
        assert pc.refuse_if_frozen([p]) is not None
    assert pc.refuse_if_frozen(["novels/some-new-book/chapters"]) is None
    assert pc.refuse_if_frozen(["novels/some-new-book/chapters"], ["some-new"]) == "some-new"


def test_cli_refuses_frozen_without_reading(tmp_path):
    book = tmp_path / "amity-falls-book-9" / "chapters"
    book.mkdir(parents=True)
    (book / "chapter_01.md").write_text(CLEAN, encoding="utf-8")
    report = tmp_path / "r.md"
    code = pc.main(["--chapters", str(book), "--report", str(report)])
    assert code == pc.EXIT_REFUSED
    assert not report.exists()


def test_cli_pass_blocked_and_never_modifies_chapters(tmp_path):
    book = tmp_path / "newbook" / "chapters"
    book.mkdir(parents=True)
    ch1 = book / "chapter_01.md"
    ch2 = book / "chapter_02.md"
    ch1.write_text(CLEAN, encoding="utf-8")
    ch2.write_text(CLEAN + " co­work and the the end", encoding="utf-8")
    before = (ch1.read_text(encoding="utf-8"), ch2.read_text(encoding="utf-8"))
    report = tmp_path / "r.md"
    code = pc.main(["--chapters", str(book), "--report", str(report)])
    assert code == pc.EXIT_BLOCKED
    text = report.read_text(encoding="utf-8")
    assert "Verdict: BLOCKED" in text
    assert "_VIOLATION" not in text
    assert (ch1.read_text(encoding="utf-8"), ch2.read_text(encoding="utf-8")) == before

    ch2.write_text(CLEAN, encoding="utf-8")
    assert pc.main(["--chapters", str(book), "--report", str(report)]) == pc.EXIT_PASS


def test_spaced_hyphen_counts_as_dash_stand_in():
    assert "D04" in rules(CLEAN + " Wait - what happened?")
    assert "D04" not in rules(CLEAN + "\n\n- a list item\n\n" + CLEAN)
    assert "D04" not in rules(CLEAN + " A well-known door.")


def test_capitalized_tag_after_comma():
    assert "X10" in rules(CLEAN + ' "Come here," She said.')
    assert "X10" not in rules(CLEAN + ' "Come here," she said.')
    assert "X10" not in rules(CLEAN + ' "Come here," I said.')


def test_spelled_out_numbers_review_only():
    assert "N01" in rules(CLEAN + " She counted 12 steps.")
    assert "N01" not in rules(CLEAN + " In 1986 at 3:30 on the 2nd, $5 and 40%.")
    assert "N01" not in rules("# Chapter 12\n\n" + CLEAN)
    assert pc.verdict(pc.check_text(CLEAN + " She counted 12 steps.", "x.md")) == "PASS"


def test_every_rule_maps_to_one_of_the_ten_parameters():
    emitted = {rule for rule, _, _, _ in pc.LINE_RULES}
    emitted |= {"D01", "D02", "X06", "X07", "X08", "X09", "S01", "S02", "W01", "W02", "K07", "K08"}
    for rule in emitted:
        assert pc.param_of(rule) in pc.PARAMETERS, rule
    assert sorted(pc.PARAMETERS) == list(range(1, 11))


def test_report_lists_all_ten_parameters_and_marks_human_ones():
    findings = pc.check_text(CLEAN, "x.md")
    report = pc.build_report(findings, {"x.md": 80}, "demo")
    for n in range(1, 11):
        assert f"- {n}. " in report
    assert "needs the human read" in report
    assert "_VIOLATION" not in report


def test_cli_no_files(tmp_path):
    empty = tmp_path / "empty"
    empty.mkdir()
    assert pc.main(["--chapters", str(empty), "--report", str(tmp_path / "r.md")]) == pc.EXIT_NOFILES
