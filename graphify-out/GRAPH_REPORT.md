# Graph Report - Voxel  (2026-10-20)

## Corpus Check
- 44 files · ~70,708 words
- Verdict: corpus is large enough that graph structure adds value.
- Unclassified: 2 file(s) not represented in the graph (top: (none) 2)

## Summary
- 472 nodes · 1043 edges · 13 communities
- Extraction: 98% EXTRACTED · 2% INFERRED · 0% AMBIGUOUS · INFERRED: 24 edges (avg confidence: 0.86)
- Token cost: 0 input · 0 output

## Graph Freshness
- Built from commit: `d5a9e2f2`
- Run `git rev-parse HEAD` and compare to check if the graph is stale.
- Run `graphify update .` after code changes (no API cost).

## Community Hubs (Navigation)
- make_lesson.py
- json
- test_proofread_core.py
- sys
- requests
- video_output.py
- test_humanizer.py
- languagetool_pass.py
- re
- write_kindling.py
- os
- content_provider.py
- glob

## God Nodes (most connected - your core abstractions)
1. `rules()` - 23 edges
2. `scan()` - 19 edges
3. `process_book()` - 18 edges
4. `main()` - 16 edges
5. `main()` - 16 edges
6. `BookConfig` - 15 edges
7. `cmd_novel()` - 15 edges
8. `run_book()` - 14 edges
9. `check_text()` - 14 edges
10. `main()` - 12 edges

## Surprising Connections (you probably didn't know these)
- `main()` --calls--> `generate_all_images()`  [EXTRACTED]
  build_book.py → image_provider.py
- `main()` --calls--> `generate_outline()`  [EXTRACTED]
  make_lesson.py → content_provider.py
- `test_missing_api_key_raises()` --calls--> `generate_outline()`  [EXTRACTED]
  test_content_provider.py → content_provider.py
- `test_generate_manuscript_schema()` --calls--> `generate_manuscript()`  [EXTRACTED]
  test_content_provider.py → content_provider.py
- `cmd_book()` --calls--> `generate_manuscript()`  [EXTRACTED]
  voxel_cli.py → content_provider.py

## Import Cycles
- None detected.

## Communities (13 total, 0 thin omitted)

### Community 0 - "make_lesson.py"
Cohesion: 0.08
Nodes (21): build_cover_pdf(), build_interior_pdf(), calculate_spine_width(), main(), generate_manuscript(), build_deck(), fetch_background_audio(), generate_narration() (+13 more)

### Community 1 - "json"
Cohesion: 0.07
Nodes (25): date_consistency_check(), extract_chapter_date(), full_proofread(), grammar_scan(), main(), run(), main(), continuity_prompt_block() (+17 more)

### Community 2 - "test_proofread_core.py"
Cohesion: 0.09
Nodes (43): _blank_comments(), build_report(), check_book(), check_text(), add(), Finding, main(), Options (+35 more)

### Community 3 - "sys"
Cohesion: 0.09
Nodes (14): BookConfig, BookConfigError, main(), add_markdown_emphasis_paragraph(), build(), main(), read_chapters(), build_report() (+6 more)

### Community 4 - "requests"
Cohesion: 0.12
Nodes (18): generate_image(), _save(), try_cloudflare(), try_flux_hosted(), try_gemini(), generate_all_images(), generate_image(), _get_api_key() (+10 more)

### Community 5 - "video_output.py"
Cohesion: 0.36
Nodes (3): build_narrated_video(), _synthesize_narration(), _wav_duration_seconds()

### Community 6 - "test_humanizer.py"
Cohesion: 0.08
Nodes (31): _extract_facts(), has_strong_hit(), humanize_manuscript(), humanize_text(), _repeated_openings(), rewrite_pass(), scan(), scan_narrative() (+23 more)

### Community 7 - "languagetool_pass.py"
Cohesion: 0.10
Nodes (29): adapt_match(), book_names(), chapter_hash(), classify(), _first(), full_report(), keep_match(), line_of() (+21 more)

### Community 9 - "re"
Cohesion: 0.10
Nodes (23): main(), strip_dashes(), main(), run_book(), apply_tell_fixes(), check_ai_tells(), check_dialogue_ratio(), check_dialogue_tags() (+15 more)

### Community 10 - "write_kindling.py"
Cohesion: 0.15
Nodes (20): build_prompt(), call_chapter(), call_model(), chapter_path(), check(), checkpoint(), clean_body(), common_lowercase() (+12 more)

### Community 14 - "os"
Cohesion: 0.08
Nodes (19): build(), ensure_font(), main(), sample_spine_color(), check_corrupted(), check_docx_asterisks(), check_doubled_words(), check_em_dash() (+11 more)

### Community 15 - "content_provider.py"
Cohesion: 0.09
Nodes (15): _build_payload(), _build_providers(), _call_nemotron(), call_raw(), generate_beat_map(), generate_novel_chapter(), generate_outline(), _load_openrouter_keys() (+7 more)

### Community 16 - "glob"
Cohesion: 0.13
Nodes (11): main(), extract_chapter(), find_book_dirs(), fuzzy_variant_groups(), main(), main(), swap(), autofix_chapter() (+3 more)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `scan()` connect `test_humanizer.py` to `re`, `json`?**
  _High betweenness centrality (0.055) - this node is a cross-community bridge._
- **Should `make_lesson.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08362369337979095 - nodes in this community are weakly interconnected._
- **Why does `cmd_novel()` connect `json` to `test_humanizer.py`, `content_provider.py`?**
  _High betweenness centrality (0.036) - this node is a cross-community bridge._
- **Should `json` be split into smaller, more focused modules?**
  _Cohesion score 0.07088989441930618 - nodes in this community are weakly interconnected._
- **Should `test_proofread_core.py` be split into smaller, more focused modules?**
  _Cohesion score 0.08571428571428572 - nodes in this community are weakly interconnected._
- **Should `sys` be split into smaller, more focused modules?**
  _Cohesion score 0.09146341463414634 - nodes in this community are weakly interconnected._
- **Should `requests` be split into smaller, more focused modules?**
  _Cohesion score 0.12477718360071301 - nodes in this community are weakly interconnected._