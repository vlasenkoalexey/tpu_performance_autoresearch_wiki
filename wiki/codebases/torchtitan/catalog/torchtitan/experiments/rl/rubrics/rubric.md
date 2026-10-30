---
title: 'Module: torchtitan/experiments/rl/rubrics/rubric.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/rubrics/rubric.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.rubrics.rubric`/
symbols:
  Rubric._score_single_rollout: Rubric#_score_single_rollout().
  RewardFn: RewardFn#
  Rubric: Rubric#
  Rubric.Config: Rubric#Config#
  Rubric._reward_fns: Rubric#_reward_fns.
  Rubric.Config.reward_fns: Rubric#Config#reward_fns.
  Rubric.score_group: Rubric#score_group().
  RewardFn.Config: RewardFn#Config#
  Rubric._weight_sum: Rubric#_weight_sum.
  RubricOutput: RubricOutput#
  RewardFn.__init__: RewardFn#__init__().
  RubricOutput.reward: RubricOutput#reward.
  RewardFn.Config.weight: RewardFn#Config#weight.
  RubricOutput.reward_breakdown: RubricOutput#reward_breakdown.
  Rubric.Config.error_reward: Rubric#Config#error_reward.
  Rubric.Config.truncation_reward: Rubric#Config#truncation_reward.
  RewardFn.__call__: RewardFn#__call__().
  Rubric.__init__: Rubric#__init__().
  Rubric._config: Rubric#_config.
  RewardFn.weight: RewardFn#weight.
---
# Module: [`torchtitan/experiments/rl/rubrics/rubric.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py)

## Classes
### <a id="RewardFn"></a>`RewardFn`  ·  implements/extends ABC, Configurable
- def: [`torchtitan/experiments/rl/rubrics/rubric.py:18`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L18)
- doc: A single reward function, as a Configurable callable.
- signature: `class RewardFn(Configurable, abc.ABC):`
- members:
  - <a id="RewardFn.__call__"></a>`__call__(self, rollout: Rollout, env_input: object)` — [`L44`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L44) — Return this fn's score for one rollout.
  - <a id="RewardFn.weight"></a>`weight` — [`L41`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L41)
- protocol/private: <a id="RewardFn.__init__"></a>`__init__`[`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L40)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Rollout`](../rollout/types.md#Rollout), [`Config`](rubric.md#RewardFn.Config), [`weight`](rubric.md#RewardFn.Config.weight)  (4 test-only)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`reward_fns`](rubric.md#Rubric.Config.reward_fns)  (10 test-only)

### <a id="RewardFn.Config"></a>`RewardFn.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/rubrics/rubric.py:36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L36)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="RewardFn.Config.weight"></a>`weight` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L37) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config)
- used by: [`reward_fns`](rubric.md#Rubric.Config.reward_fns), [`__init__`](rubric.md#RewardFn.__init__)  (8 test-only)

### <a id="Rubric"></a>`Rubric`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/rubrics/rubric.py:70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L70)
- doc: Scores rollouts with a set of weighted reward functions.
- signature: `class Rubric(Configurable):`
- members:
  - <a id="Rubric._score_single_rollout"></a>`_score_single_rollout(self, rollout: Rollout, env_input: object)` — [`L117`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L117) — Score one rollout. Short-circuits to `truncation_reward` /
  - <a id="Rubric.score_group"></a>`score_group(self, rollouts: list[Rollout], env_input: object)` — [`L158`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L158) — Score every rollout in one prompt group.
- protocol/private: <a id="Rubric.__init__"></a>`__init__`[`L100`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L100), <a id="Rubric._config"></a>`_config`[`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L101), <a id="Rubric._reward_fns"></a>`_reward_fns`[`L102`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L102), <a id="Rubric._weight_sum"></a>`_weight_sum`[`L110`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L110)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`build`](../../../config/configurable.md#Configurable.Config.build), [`log_trace_span`](../../../observability/structured_logger/structured_logging.md#log_trace_span), [`Rollout`](../rollout/types.md#Rollout), [`status`](../rollout/types.md#Rollout.status), [`Config`](rubric.md#Rubric.Config), [`reward_fns`](rubric.md#Rubric.Config.reward_fns), [`RubricOutput`](rubric.md#RubricOutput), [`reward`](rubric.md#RubricOutput.reward), [`error_reward`](rubric.md#Rubric.Config.error_reward), [`reward_breakdown`](rubric.md#RubricOutput.reward_breakdown), [`is_truncated`](../rollout/types.md#RolloutStatus.is_truncated), [`truncation_reward`](rubric.md#Rubric.Config.truncation_reward), [`is_error`](../rollout/types.md#RolloutStatus.is_error)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`score_group`](../rollout/rollouter.md#RolloutWorker.score_group), [`rubric`](../rollout/rollouter.md#RolloutWorker.rubric), [`rubric`](../rollout/rollouter.md#RolloutWorker.Config.rubric)  (7 test-only)

### <a id="Rubric.Config"></a>`Rubric.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/rubrics/rubric.py:88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L88)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="Rubric.Config.error_reward"></a>`error_reward` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L96) — ---
  - <a id="Rubric.Config.reward_fns"></a>`reward_fns` — [`L89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L89) — ---
  - <a id="Rubric.Config.truncation_reward"></a>`truncation_reward` — [`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L92) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config), [`RewardFn`](rubric.md#RewardFn), [`Config`](rubric.md#RewardFn.Config)
- used by: [`_score_single_rollout`](rubric.md#Rubric._score_single_rollout), [`_reward_fns`](rubric.md#Rubric._reward_fns), [`rubric`](../rollout/rollouter.md#RolloutWorker.Config.rubric), [`__init__`](rubric.md#Rubric.__init__)  (6 test-only)

### <a id="RubricOutput"></a>`RubricOutput`
- def: [`torchtitan/experiments/rl/rubrics/rubric.py:54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L54)
- doc: One rollout's reward, as returned by a `Rubric`.
- signature: `class RubricOutput:`
- members:
  - <a id="RubricOutput.reward"></a>`reward` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L61) — ---
  - <a id="RubricOutput.reward_breakdown"></a>`reward_breakdown` — [`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rubrics/rubric.py#L64) — ---
- used by: [`run_group`](../rollout/rollouter.md#RolloutWorker.run_group), [`_score_single_rollout`](rubric.md#Rubric._score_single_rollout), [`score_group`](../rollout/rollouter.md#RolloutWorker.score_group), [`score_group`](rubric.md#Rubric.score_group)  (2 test-only)

