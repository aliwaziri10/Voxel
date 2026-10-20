"""Tests for scripts/languagetool_pass.py. No Java, no network: LanguageTool is
replaced by a fake that returns match dicts in the same shape."""
import os

import languagetool_pass as lt
import proofread_core as pc

TEXT = "# Chapter 1\n\nThe morning was cold.\n\nShe seen the Heron.\n\nOdalys waved. Odalys left. Odalys sat.\n"


def fake_factory(calls):
    def check(text):
        calls.append(text)
        out = []
        i = text.find("seen")
        if i >= 0:
            out.append({"rule_id": "HAVE_PART_AGREEMENT", "category": "GRAMMAR",
                        "issue_type": "grammar", "message": "Use 'saw'.",
                        "offset": i, "length": 4, "replacements": ["saw"]})
        j = text.find("Odalys")
        if j >= 0:
            out.append({"rule_id": "MORFOLOGIK_RULE_EN_US", "category": "TYPOS",
                        "issue_type": "misspelling", "message": "Possible spelling mistake.",
                        "offset": j, "length": 6, "replacements": []})
        k = text.find("cold")
        out.append({"rule_id": "SOME_STYLE_RULE", "category": "STYLE", "issue_type": "style",
                    "message": "Style.", "offset": k, "length": 4, "replacements": []})
        out.append({"rule_id": "WHITESPACE_RULE", "category": "TYPOGRAPHY", "issue_type": "whitespace",
                    "message": "ws", "offset": 0, "length": 1, "replacements": []})
        return out
    return check


def book(tmp_path, text=TEXT):
    d = tmp_path / "novels" / "new-book" / "chapters"
    d.mkdir(parents=True)
    p = d / "chapter_01.md"
    p.write_text(text, encoding="utf-8")
    return d, p


def test_grammar_flagged_with_line_and_suggestion_names_and_style_dropped(tmp_path):
    d, p = book(tmp_path)
    calls = []
    findings, counts, stats = lt.run_book([str(p)], fake_factory(calls), cache={"entries": {}})
    rules = {f.rule for f in findings}
    assert rules == {"L02"}  # Odalys is a name (3 uses, never lowercase); style dropped
    f = findings[0]
    assert f.line == 5 and f.quote == "seen" and "saw" in f.note
    assert stats == {"checked": 1, "cached": 0}


def test_headings_blanked_but_line_numbers_kept():
    shown = lt.text_for_checking(TEXT)
    assert shown.split("\n")[0] == "" and len(shown.split("\n")) == len(TEXT.split("\n"))


def test_never_critical_or_destructive_so_it_cannot_block(tmp_path):
    d, p = book(tmp_path)
    findings, _, _ = lt.run_book([str(p)], fake_factory([]), cache={"entries": {}})
    assert not {f.tier for f in findings} & {pc.CRITICAL, pc.DESTRUCTIVE}
    assert pc.verdict(findings) == "PASS"


def test_cache_reused_until_text_changes(tmp_path):
    d, p = book(tmp_path)
    cache, calls = {"entries": {}}, []
    lt.run_book([str(p)], fake_factory(calls), cache)
    stats = {"checked": 0, "cached": 0}
    lt.run_book([str(p)], fake_factory(calls), cache, stats=stats)
    assert len(calls) == 1 and stats == {"checked": 0, "cached": 1}
    p.write_text(TEXT + "\nOne more line.\n", encoding="utf-8")
    lt.run_book([str(p)], fake_factory(calls), cache)
    assert len(calls) == 2


def test_cache_file_roundtrip(tmp_path):
    path = str(tmp_path / "c" / "x.json")
    cache = lt.load_cache(path)
    cache["entries"]["chapter_01.md"] = {"hash": "h", "matches": []}
    lt.save_cache(path, cache)
    assert lt.load_cache(path)["entries"]["chapter_01.md"]["hash"] == "h"


def test_ignore_words_drop_spelling_flags(tmp_path):
    d, p = book(tmp_path, "One thing.\n\nZorb stood there. Zorb\n")

    def check(text):
        i = text.find("Zorb")
        return [{"rule_id": "MORFOLOGIK_RULE_EN_US", "category": "TYPOS", "issue_type": "",
                 "message": "m", "offset": i, "length": 4, "replacements": []}]
    assert lt.run_book([str(p)], check, None)[0]
    assert not lt.run_book([str(p)], check, None, ignore_words=["Zorb"])[0]


def test_adapt_match_handles_object_with_both_attribute_styles():
    class M:
        ruleId = "R"; category = "grammar"; message = "m"; offset = 3
        errorLength = 2; replacements = ["a", "b", "c", "d"]
    m = lt.adapt_match(M())
    assert m["rule_id"] == "R" and m["category"] == "GRAMMAR" and m["length"] == 2
    assert len(m["replacements"]) == 3


def test_frozen_book_refused_before_anything_runs(tmp_path):
    d = tmp_path / "novels" / "kindling-line-book-2" / "chapters"
    d.mkdir(parents=True)
    (d / "chapter_01.md").write_text("Hello.", encoding="utf-8")
    assert lt.main(["--chapters", str(d)]) == pc.EXIT_REFUSED


def test_main_reports_when_languagetool_missing_and_never_edits_chapters(tmp_path, monkeypatch):
    d, p = book(tmp_path)
    before = p.read_bytes()
    monkeypatch.setattr(lt, "make_backend", lambda server=None: (_ for _ in ()).throw(RuntimeError("no java")))
    assert lt.main(["--chapters", str(d), "--report", str(tmp_path / "r.md")]) == lt.EXIT_NO_LT
    assert p.read_bytes() == before


def test_main_with_fake_backend_writes_report_and_cache_only(tmp_path, monkeypatch):
    d, p = book(tmp_path)
    before = p.read_bytes()
    monkeypatch.setattr(lt, "make_backend", lambda server=None: (fake_factory([]), lambda: None))
    rep, cache = tmp_path / "r.md", tmp_path / "cache.json"
    assert lt.main(["--chapters", str(d), "--report", str(rep), "--cache", str(cache)]) == pc.EXIT_PASS
    assert "L02" in rep.read_text() and cache.exists()
    assert p.read_bytes() == before
