---
title: 'Module: torchtitan/experiments/rl/examples/dapo_math/rollouter.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/examples/dapo_math/rollouter.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.examples.dapo_math.rollouter`/
symbols:
  DapoMathWorker.Config.rubric: DapoMathWorker#Config#rubric.
  DapoMathWorker.Config.token_env: DapoMathWorker#Config#token_env.
  DapoMathRollouter.Config: DapoMathRollouter#Config#
  DapoMathWorker.Config: DapoMathWorker#Config#
  DapoMathWorker.Config.advantage: DapoMathWorker#Config#advantage.
  DapoMathWorker: DapoMathWorker#
  DapoMathRollouter.Config.validation_dataset: DapoMathRollouter#Config#validation_dataset.
  DapoMathRollouter: DapoMathRollouter#
  DapoMathWorker.Config.message_env: DapoMathWorker#Config#message_env.
  DapoMathRollouter.Config.train_dataset: DapoMathRollouter#Config#train_dataset.
  DapoMathRollouter.Config.worker: DapoMathRollouter#Config#worker.
---
# Module: [`torchtitan/experiments/rl/examples/dapo_math/rollouter.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rollouter.py)

## Classes
### <a id="DapoMathRollouter"></a>`DapoMathRollouter`  ·  implements/extends Rollouter
- def: [`torchtitan/experiments/rl/examples/dapo_math/rollouter.py:51`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rollouter.py#L51)
- doc: Single-turn math reasoning with a binary Math-Verify reward.
- signature: `class DapoMathRollouter(Rollouter):`
- uses (calls/refs, reference-scoped): [`Rollouter`](../../rollout/rollouter.md#Rollouter)
- used by: [`Rollouter`](../../rollout/rollouter.md#Rollouter)  (1 test-only)

### <a id="DapoMathRollouter.Config"></a>`DapoMathRollouter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/dapo_math/rollouter.py:59`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rollouter.py#L59)
- signature: `class Config(Rollouter.Config):`
- members:
  - <a id="DapoMathRollouter.Config.train_dataset"></a>`train_dataset` — [`L60`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rollouter.py#L60)
  - <a id="DapoMathRollouter.Config.validation_dataset"></a>`validation_dataset` — [`L63`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rollouter.py#L63)
  - <a id="DapoMathRollouter.Config.worker"></a>`worker` — [`L66`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rollouter.py#L66)
- uses (calls/refs, reference-scoped): [`Rollouter`](../../rollout/rollouter.md#Rollouter), [`Config`](../../rollout/rollouter.md#Rollouter.Config)  (6 test-only)
- used by: (1 test-only callers)

### <a id="DapoMathWorker"></a>`DapoMathWorker`  ·  implements/extends RolloutWorker
- def: [`torchtitan/experiments/rl/examples/dapo_math/rollouter.py:23`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rollouter.py#L23)
- doc: DAPO-Math's env and Math-Verify reward.
- signature: `class DapoMathWorker(RolloutWorker):`
- uses (calls/refs, reference-scoped): [`RolloutWorker`](../../rollout/rollouter.md#RolloutWorker)
- used by: [`RolloutWorker`](../../rollout/rollouter.md#RolloutWorker)  (2 test-only)

### <a id="DapoMathWorker.Config"></a>`DapoMathWorker.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/examples/dapo_math/rollouter.py:30`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rollouter.py#L30)
- signature: `class Config(RolloutWorker.Config):`
- members:
  - <a id="DapoMathWorker.Config.advantage"></a>`advantage` — [`L44`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rollouter.py#L44)
  - <a id="DapoMathWorker.Config.message_env"></a>`message_env` — [`L37`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rollouter.py#L37)
  - <a id="DapoMathWorker.Config.rubric"></a>`rubric` — [`L31`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rollouter.py#L31)
  - <a id="DapoMathWorker.Config.token_env"></a>`token_env` — [`L38`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/examples/dapo_math/rollouter.py#L38)
- uses (calls/refs, reference-scoped): [`RolloutWorker`](../../rollout/rollouter.md#RolloutWorker), [`Rubric`](../../rubrics/rubric.md#Rubric), [`TokenEnv`](../../environment/token.md#TokenEnv), [`AdvantageEstimator`](../../rollout/advantage.md#AdvantageEstimator), [`Config`](../../rubrics/rubric.md#Rubric.Config), [`Config`](../../environment/token.md#TokenEnv.Config), [`Config`](../../rollout/advantage.md#AdvantageEstimator.Config), [`Config`](../../rollout/rollouter.md#RolloutWorker.Config), [`reward_fns`](../../rubrics/rubric.md#Rubric.Config.reward_fns), [`error_reward`](../../rubrics/rubric.md#Rubric.Config.error_reward), [`max_num_turns`](../../environment/token.md#TokenEnv.Config.max_num_turns), [`should_std_normalize`](../../rollout/advantage.md#AdvantageEstimator.Config.should_std_normalize), [`weight`](../../rubrics/rubric.md#RewardFn.Config.weight), [`max_rollout_tokens`](../../environment/token.md#TokenEnv.Config.max_rollout_tokens)  (4 test-only)
- used by: (2 test-only callers)

