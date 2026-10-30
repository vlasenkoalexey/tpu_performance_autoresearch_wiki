---
title: 'Module: torchtitan/experiments/rl/examples/search_r1/rubric.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/search_r1/rubric.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.search_r1.rubric`/
symbols:
  RewardExactMatch.__call__: RewardExactMatch#__call__().
  RewardExactMatch: RewardExactMatch#
  RewardExactMatch.Config: RewardExactMatch#Config#
  _retrieval_surfaced_gold: _retrieval_surfaced_gold().
  _final_answer: _final_answer().
  _made_search_call: _made_search_call().
  RewardExactMatch.__init__: RewardExactMatch#__init__().
  RewardExactMatch._score: RewardExactMatch#_score.
  RewardExactMatch._retrieval_score: RewardExactMatch#_retrieval_score.
  _normalize_answer: _normalize_answer().
  _is_exact_match: _is_exact_match().
  RewardExactMatch._no_search_penalty: RewardExactMatch#_no_search_penalty.
  RewardExactMatch.Config.no_search_penalty: RewardExactMatch#Config#no_search_penalty.
  RewardExactMatch.Config.retrieval_score: RewardExactMatch#Config#retrieval_score.
  RewardExactMatch.Config.score: RewardExactMatch#Config#score.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/rl/examples/search_r1/rubric.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py)

## Classes
### <a id="RewardExactMatch"></a>`RewardExactMatch`  ·  implements/extends RewardFn
- def: [`torchtitan/experiments/rl/examples/search_r1/rubric.py:79`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L79)
- doc: Exact-match reward over the tool-calling rollout's final answer.
- signature: `class RewardExactMatch(RewardFn):`
- protocol/private: <a id="RewardExactMatch.__call__"></a>`__call__`[`L112`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L112), <a id="RewardExactMatch.__init__"></a>`__init__`[`L106`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L106), <a id="RewardExactMatch._no_search_penalty"></a>`_no_search_penalty`[`L109`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L109), <a id="RewardExactMatch._retrieval_score"></a>`_retrieval_score`[`L110`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L110), <a id="RewardExactMatch._score"></a>`_score`[`L108`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L108)
- uses (calls/refs, reference-scoped): [`Rollout`](../../rollout/types.md#Rollout), [`RewardFn`](../../rubrics/rubric.md#RewardFn), [`__init__`](../../rubrics/rubric.md#RewardFn.__init__)  (10 test-only)
- used by: [`RewardFn`](../../rubrics/rubric.md#RewardFn)  (7 test-only)

### <a id="RewardExactMatch.Config"></a>`RewardExactMatch.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/search_r1/rubric.py:93`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L93)
- signature: `class Config(RewardFn.Config):`
- members:
  - <a id="RewardExactMatch.Config.no_search_penalty"></a>`no_search_penalty` — [`L97`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L97) — ---
  - <a id="RewardExactMatch.Config.retrieval_score"></a>`retrieval_score` — [`L102`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L102) — ---
  - <a id="RewardExactMatch.Config.score"></a>`score` — [`L94`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L94) — ---
- uses (calls/refs, reference-scoped): [`RewardFn`](../../rubrics/rubric.md#RewardFn), [`Config`](../../rubrics/rubric.md#RewardFn.Config)
- used by: (11 test-only callers)

## Functions
- <a id="_final_answer"></a>`_final_answer(rollout: Rollout)` — [`L40`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L40) — The assistant's final answer: the last turn's content, if it isn't a tool call.
- <a id="_is_exact_match"></a>`_is_exact_match(prediction: str, golden_answers: list[str])` — [`L34`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L34) — True if the normalized prediction exactly equals any normalized golden answer.
- <a id="_made_search_call"></a>`_made_search_call(rollout: Rollout)` — [`L55`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L55) — True if the assistant called the search tool at least once.
- <a id="_normalize_answer"></a>`_normalize_answer(s: str)` — [`L26`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L26) — Lowercase, strip punctuation/articles, and collapse whitespace for EM.
- <a id="_retrieval_surfaced_gold"></a>`_retrieval_surfaced_gold(rollout: Rollout, golden_answers: list[str])` — [`L62`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L62) — True if a golden answer appears (as whole words) in any search (tool) result.

## Module values
- <a id="__all__"></a>`__all__` — [`L127`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/search_r1/rubric.py#L127)

