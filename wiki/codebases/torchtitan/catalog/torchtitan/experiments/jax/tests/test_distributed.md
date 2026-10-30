---
title: 'Module: torchtitan/experiments/jax/tests/test_distributed.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/jax/tests/test_distributed.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.jax.tests.test_distributed`/
symbols:
  RealShardingMapTest.test_jax_llama3_non_scan: RealShardingMapTest#test_jax_llama3_non_scan().
  RealShardingMapTest.test_jax_llama3_scan: RealShardingMapTest#test_jax_llama3_scan().
  ProcessShardingNameTest.test_process: ProcessShardingNameTest#test_process().
  MatchPathExactTest.test_hit: MatchPathExactTest#test_hit().
  MatchPathExactTest.test_miss: MatchPathExactTest#test_miss().
  MatchPathIntPreprocessingTest.test_slash_path: MatchPathIntPreprocessingTest#test_slash_path().
  MatchPathIntPreprocessingTest.test_dot_path: MatchPathIntPreprocessingTest#test_dot_path().
  MatchPathIntPreprocessingTest.test_multiple_indices: MatchPathIntPreprocessingTest#test_multiple_indices().
  MatchPathRegexTest.test_dot_star_prefix: MatchPathRegexTest#test_dot_star_prefix().
  MatchPathRegexTest.test_anchored_pattern: MatchPathRegexTest#test_anchored_pattern().
  MatchPathRegexTest.test_alternation: MatchPathRegexTest#test_alternation().
  MatchPathPrecedenceTest.test_exact_wins_over_preprocessed: MatchPathPrecedenceTest#test_exact_wins_over_preprocessed().
  MatchPathPrecedenceTest.test_preprocessed_wins_over_regex: MatchPathPrecedenceTest#test_preprocessed_wins_over_regex().
  MatchPathInvalidRegexTest.test_invalid_regex_ignored: MatchPathInvalidRegexTest#test_invalid_regex_ignored().
  RealShardingMapTest.test_torchax_llama3: RealShardingMapTest#test_torchax_llama3().
  ProcessShardingNameTest: ProcessShardingNameTest#
  MatchPathExactTest: MatchPathExactTest#
  MatchPathIntPreprocessingTest: MatchPathIntPreprocessingTest#
  MatchPathRegexTest: MatchPathRegexTest#
  MatchPathPrecedenceTest: MatchPathPrecedenceTest#
  MatchPathInvalidRegexTest: MatchPathInvalidRegexTest#
  RealShardingMapTest: RealShardingMapTest#
---
# Module: [`torchtitan/experiments/jax/tests/test_distributed.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py)

> **Collapsed catalog** (22 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="MatchPathExactTest"></a>`MatchPathExactTest` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L33)
- <a id="MatchPathExactTest.test_hit"></a>`MatchPathExactTest.test_hit` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L36)
- <a id="MatchPathExactTest.test_miss"></a>`MatchPathExactTest.test_miss` — [`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L41)
- <a id="MatchPathIntPreprocessingTest"></a>`MatchPathIntPreprocessingTest` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L46)
- <a id="MatchPathIntPreprocessingTest.test_dot_path"></a>`MatchPathIntPreprocessingTest.test_dot_path` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L58)
- <a id="MatchPathIntPreprocessingTest.test_multiple_indices"></a>`MatchPathIntPreprocessingTest.test_multiple_indices` — [`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L64)
- <a id="MatchPathIntPreprocessingTest.test_slash_path"></a>`MatchPathIntPreprocessingTest.test_slash_path` — [`L49`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L49)
- <a id="MatchPathInvalidRegexTest"></a>`MatchPathInvalidRegexTest` — [`L114`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L114)
- <a id="MatchPathInvalidRegexTest.test_invalid_regex_ignored"></a>`MatchPathInvalidRegexTest.test_invalid_regex_ignored` — [`L117`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L117)
- <a id="MatchPathPrecedenceTest"></a>`MatchPathPrecedenceTest` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L96)
- <a id="MatchPathPrecedenceTest.test_exact_wins_over_preprocessed"></a>`MatchPathPrecedenceTest.test_exact_wins_over_preprocessed` — [`L99`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L99)
- <a id="MatchPathPrecedenceTest.test_preprocessed_wins_over_regex"></a>`MatchPathPrecedenceTest.test_preprocessed_wins_over_regex` — [`L106`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L106)
- <a id="MatchPathRegexTest"></a>`MatchPathRegexTest` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L69)
- <a id="MatchPathRegexTest.test_alternation"></a>`MatchPathRegexTest.test_alternation` — [`L89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L89)
- <a id="MatchPathRegexTest.test_anchored_pattern"></a>`MatchPathRegexTest.test_anchored_pattern` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L79)
- <a id="MatchPathRegexTest.test_dot_star_prefix"></a>`MatchPathRegexTest.test_dot_star_prefix` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L72)
- <a id="ProcessShardingNameTest"></a>`ProcessShardingNameTest` — [`L18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L18)
- <a id="ProcessShardingNameTest.test_process"></a>`ProcessShardingNameTest.test_process` — [`L29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L29)
- <a id="RealShardingMapTest"></a>`RealShardingMapTest` — [`L125`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L125)
- <a id="RealShardingMapTest.test_jax_llama3_non_scan"></a>`RealShardingMapTest.test_jax_llama3_non_scan` — [`L128`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L128)
- <a id="RealShardingMapTest.test_jax_llama3_scan"></a>`RealShardingMapTest.test_jax_llama3_scan` — [`L144`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L144)
- <a id="RealShardingMapTest.test_torchax_llama3"></a>`RealShardingMapTest.test_torchax_llama3` — [`L152`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/jax/tests/test_distributed.py#L152)
