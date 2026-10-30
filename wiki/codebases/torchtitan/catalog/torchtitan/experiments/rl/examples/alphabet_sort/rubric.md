---
title: 'Module: torchtitan/experiments/rl/examples/alphabet_sort/rubric.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/alphabet_sort/rubric.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.alphabet_sort.rubric`/
symbols:
  RewardAlphabetSort.__call__: RewardAlphabetSort#__call__().
  RewardAlphabetSort: RewardAlphabetSort#
  RewardAlphabetSort.Config: RewardAlphabetSort#Config#
  score_sorted_list: score_sorted_list().
  RewardAlphabetSort.Config.similarity_power: RewardAlphabetSort#Config#similarity_power.
  RewardAlphabetSort.__init__: RewardAlphabetSort#__init__().
  RewardAlphabetSort.similarity_power: RewardAlphabetSort#similarity_power.
  RewardAlphabetSort.Config.__post_init__: RewardAlphabetSort#Config#__post_init__().
  _answer_lines: _answer_lines().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/rl/examples/alphabet_sort/rubric.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rubric.py)

## Classes
### <a id="RewardAlphabetSort"></a>`RewardAlphabetSort`  ·  implements/extends RewardFn
- def: [`torchtitan/experiments/rl/examples/alphabet_sort/rubric.py:19`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rubric.py#L19)
- doc: Average over the rollout's turns of how well each turn's list was sorted, each scored by
- signature: `class RewardAlphabetSort(RewardFn):`
- members:
  - <a id="RewardAlphabetSort.similarity_power"></a>`similarity_power` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rubric.py#L38)
- protocol/private: <a id="RewardAlphabetSort.__call__"></a>`__call__`[`L40`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rubric.py#L40), <a id="RewardAlphabetSort.__init__"></a>`__init__`[`L36`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rubric.py#L36)
- uses (calls/refs, reference-scoped): [`Rollout`](../../rollout/types.md#Rollout), [`turns`](../../rollout/types.md#Rollout.turns), [`RewardFn`](../../rubrics/rubric.md#RewardFn), [`completion_message`](../../rollout/types.md#RolloutTurn.completion_message), [`__init__`](../../rubrics/rubric.md#RewardFn.__init__)  (5 test-only)
- used by: [`RewardFn`](../../rubrics/rubric.md#RewardFn)  (4 test-only)

### <a id="RewardAlphabetSort.Config"></a>`RewardAlphabetSort.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/alphabet_sort/rubric.py:26`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rubric.py#L26)
- signature: `class Config(RewardFn.Config):`
- members:
  - <a id="RewardAlphabetSort.Config.similarity_power"></a>`similarity_power` — [`L27`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rubric.py#L27) — ---
- protocol/private: <a id="RewardAlphabetSort.Config.__post_init__"></a>`__post_init__`[`L30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rubric.py#L30)
- uses (calls/refs, reference-scoped): [`RewardFn`](../../rubrics/rubric.md#RewardFn), [`Config`](../../rubrics/rubric.md#RewardFn.Config)
- used by: (6 test-only callers)

## Functions
- <a id="_answer_lines"></a>`_answer_lines(text: str, *, xml_tag: str)` — [`L100`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rubric.py#L100) — The non-empty lines inside the model's last `<xml_tag>` block, or [] if absent.
- <a id="score_sorted_list"></a>`score_sorted_list(response_text: str, *, expected_names: Sequence[str], xml_tag: str, similarity_power: int)` — [`L67`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rubric.py#L67) — Reward in [0, 1] for how closely the model's `<xml_tag>` block matches `expected_names`.

## Module values
- <a id="__all__"></a>`__all__` — [`L116`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/alphabet_sort/rubric.py#L116)

