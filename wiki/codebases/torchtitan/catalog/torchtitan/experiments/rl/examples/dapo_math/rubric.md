---
title: 'Module: torchtitan/experiments/rl/examples/dapo_math/rubric.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/dapo_math/rubric.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.dapo_math.rubric`/
symbols:
  score_math_response: score_math_response().
  RewardMathVerify.__call__: RewardMathVerify#__call__().
  RewardMathVerify: RewardMathVerify#
  RewardMathVerify.Config: RewardMathVerify#Config#
  _last_boxed_expression: _last_boxed_expression().
  _BOXED_START: _BOXED_START.
---
# Module: [`torchtitan/experiments/rl/examples/dapo_math/rubric.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rubric.py)

## Classes
### <a id="RewardMathVerify"></a>`RewardMathVerify`  ·  implements/extends RewardFn
- def: [`torchtitan/experiments/rl/examples/dapo_math/rubric.py:62`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rubric.py#L62)
- doc: Binary reward for a mathematically equivalent final answer.
- signature: `class RewardMathVerify(RewardFn):`
- members:
  - <a id="RewardMathVerify.__call__"></a>`__call__(self, rollout: Rollout, env_input: DapoMathSample)` — [`L69`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rubric.py#L69) — Return 1 when Math-Verify equates the response and ground truth.
- uses (calls/refs, reference-scoped): [`Rollout`](../../rollout/types.md#Rollout), [`turns`](../../rollout/types.md#Rollout.turns), [`RewardFn`](../../rubrics/rubric.md#RewardFn), [`completion_message`](../../rollout/types.md#RolloutTurn.completion_message)  (3 test-only)
- used by: [`RewardFn`](../../rubrics/rubric.md#RewardFn)  (2 test-only)

### <a id="RewardMathVerify.Config"></a>`RewardMathVerify.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/dapo_math/rubric.py:66`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rubric.py#L66)
- signature: `class Config(RewardFn.Config):`
- uses (calls/refs, reference-scoped): [`RewardFn`](../../rubrics/rubric.md#RewardFn), [`Config`](../../rubrics/rubric.md#RewardFn.Config)
- used by: (2 test-only callers)

## Functions
- <a id="_last_boxed_expression"></a>`_last_boxed_expression(text: str)` — [`L21`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rubric.py#L21) — Return the last complete `\boxed{...}` expression.
- <a id="score_math_response"></a>`score_math_response(response: str, ground_truth: str)` — [`L36`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rubric.py#L36) — Score the final `\boxed{}` expression with Math-Verify.

## Module values
- <a id="_BOXED_START"></a>`_BOXED_START` — [`L18`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rubric.py#L18)

