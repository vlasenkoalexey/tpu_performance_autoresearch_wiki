---
title: 'Module: torchtitan/experiments/rl/tests/test_alphabet_sort.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/tests/test_alphabet_sort.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.tests.test_alphabet_sort`/
symbols:
  test_rollouter_config_wires_alphabet_sort: test_rollouter_config_wires_alphabet_sort().
  test_rollouter_builds_one_env_per_group_member: test_rollouter_builds_one_env_per_group_member().
  _assistant_turn: _assistant_turn().
  test_env_walks_through_follow_up_turns: test_env_walks_through_follow_up_turns().
  test_env_single_turn_finishes_after_first_answer: test_env_single_turn_finishes_after_first_answer().
  test_single_turn_sorted_by_first_or_last: test_single_turn_sorted_by_first_or_last().
  test_reward_averages_every_turn: test_reward_averages_every_turn().
  test_reward_penalizes_incomplete_rollout: test_reward_penalizes_incomplete_rollout().
  _rollout: _rollout().
  test_state_dict_resumes_the_stream: test_state_dict_resumes_the_stream().
  test_multiturn_targets_are_cumulative_and_tagged: test_multiturn_targets_are_cumulative_and_tagged().
  test_ties_broken_by_other_name_part: test_ties_broken_by_other_name_part().
  test_turns_and_names_are_sampled_within_bounds: test_turns_and_names_are_sampled_within_bounds().
  test_names_never_repeat_across_turns: test_names_never_repeat_across_turns().
  _Author: _Author.
  test_single_turn_sorted_by_first_or_last.key: test_single_turn_sorted_by_first_or_last().key().
  test_dataset_rejects_invalid_max_turns: test_dataset_rejects_invalid_max_turns().
  test_dataset_is_deterministic: test_dataset_is_deterministic().
  _patch_names: _patch_names().
  test_score_exact_swapped_missing_and_garbage.score: test_score_exact_swapped_missing_and_garbage().score().
  _AUTHOR_BY_DISPLAY: _AUTHOR_BY_DISPLAY.
  _AUTHORS: _AUTHORS.
  test_score_exact_swapped_missing_and_garbage: test_score_exact_swapped_missing_and_garbage().
  test_score_uses_the_last_block: test_score_uses_the_last_block().
  test_followup_turns_use_the_combined_tag: test_followup_turns_use_the_combined_tag().
---
# Module: [`torchtitan/experiments/rl/tests/test_alphabet_sort.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py)

> **Collapsed catalog** (25 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="_AUTHORS"></a>`_AUTHORS` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L34)
- <a id="_AUTHOR_BY_DISPLAY"></a>`_AUTHOR_BY_DISPLAY` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L44)
- <a id="_Author"></a>`_Author` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L33)
- <a id="_assistant_turn"></a>`_assistant_turn` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L51)
- <a id="_patch_names"></a>`_patch_names` — [`L47`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L47)
- <a id="_rollout"></a>`_rollout` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L62)
- <a id="test_dataset_is_deterministic"></a>`test_dataset_is_deterministic` — [`L81`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L81)
- <a id="test_dataset_rejects_invalid_max_turns"></a>`test_dataset_rejects_invalid_max_turns` — [`L74`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L74)
- <a id="test_env_single_turn_finishes_after_first_answer"></a>`test_env_single_turn_finishes_after_first_answer` — [`L326`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L326)
- <a id="test_env_walks_through_follow_up_turns"></a>`test_env_walks_through_follow_up_turns` — [`L344`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L344)
- <a id="test_followup_turns_use_the_combined_tag"></a>`test_followup_turns_use_the_combined_tag` — [`L248`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L248)
- <a id="test_multiturn_targets_are_cumulative_and_tagged"></a>`test_multiturn_targets_are_cumulative_and_tagged` — [`L160`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L160)
- <a id="test_names_never_repeat_across_turns"></a>`test_names_never_repeat_across_turns` — [`L145`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L145)
- <a id="test_reward_averages_every_turn"></a>`test_reward_averages_every_turn` — [`L276`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L276)
- <a id="test_reward_penalizes_incomplete_rollout"></a>`test_reward_penalizes_incomplete_rollout` — [`L301`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L301)
- <a id="test_rollouter_builds_one_env_per_group_member"></a>`test_rollouter_builds_one_env_per_group_member` — [`L373`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L373)
- <a id="test_rollouter_config_wires_alphabet_sort"></a>`test_rollouter_config_wires_alphabet_sort` — [`L396`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L396)
- <a id="test_score_exact_swapped_missing_and_garbage"></a>`test_score_exact_swapped_missing_and_garbage` — [`L207`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L207)
- <a id="test_score_exact_swapped_missing_and_garbage.score"></a>`test_score_exact_swapped_missing_and_garbage.score` — [`L217`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L217)
- <a id="test_score_uses_the_last_block"></a>`test_score_uses_the_last_block` — [`L231`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L231)
- <a id="test_single_turn_sorted_by_first_or_last"></a>`test_single_turn_sorted_by_first_or_last` — [`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L103)
- <a id="test_single_turn_sorted_by_first_or_last.key"></a>`test_single_turn_sorted_by_first_or_last.key` — [`L113`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L113)
- <a id="test_state_dict_resumes_the_stream"></a>`test_state_dict_resumes_the_stream` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L88)
- <a id="test_ties_broken_by_other_name_part"></a>`test_ties_broken_by_other_name_part` — [`L183`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L183)
- <a id="test_turns_and_names_are_sampled_within_bounds"></a>`test_turns_and_names_are_sampled_within_bounds` — [`L128`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/tests/test_alphabet_sort.py#L128)
