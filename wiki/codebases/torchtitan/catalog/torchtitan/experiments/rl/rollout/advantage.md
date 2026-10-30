---
title: 'Module: torchtitan/experiments/rl/rollout/advantage.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/rollout/advantage.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.rollout.advantage`/AdvantageEstimator#
symbols:
  AdvantageEstimator: ''
  AdvantageEstimator.Config: Config#
  AdvantageEstimator.__call__: __call__().
  AdvantageEstimator.Config.should_std_normalize: Config#should_std_normalize.
  AdvantageEstimator.__init__: __init__().
  AdvantageEstimator.should_std_normalize: should_std_normalize.
---
# Module: [`torchtitan/experiments/rl/rollout/advantage.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/advantage.py)

## Classes
### <a id="AdvantageEstimator"></a>`AdvantageEstimator`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/rollout/advantage.py:22`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/advantage.py#L22) — documented in [rl-training](../../../../../concepts/rl-training.md)
- doc: Group-relative advantage estimator: `A_i = (r_i - mean(r)) / denom`.
- signature: `class AdvantageEstimator(Configurable):`
- members:
  - <a id="AdvantageEstimator.__call__"></a>`__call__(self, group: RolloutGroup)` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/advantage.py#L39) — Return per-rollout advantages, in group order.
  - <a id="AdvantageEstimator.should_std_normalize"></a>`should_std_normalize` — [`L37`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/advantage.py#L37)
- protocol/private: <a id="AdvantageEstimator.__init__"></a>`__init__`[`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/advantage.py#L36)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`RolloutGroup`](types.md#RolloutGroup), [`rollouts`](types.md#RolloutGroup.rollouts), [`Config`](advantage.md#AdvantageEstimator.Config), [`reward`](types.md#Rollout.reward), [`should_std_normalize`](advantage.md#AdvantageEstimator.Config.should_std_normalize)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`advantage`](rollouter.md#RolloutWorker.Config.advantage), [`advantage_estimator`](rollouter.md#RolloutWorker.advantage_estimator)  (6 test-only)

### <a id="AdvantageEstimator.Config"></a>`AdvantageEstimator.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/rollout/advantage.py:31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/advantage.py#L31)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="AdvantageEstimator.Config.should_std_normalize"></a>`should_std_normalize` — [`L32`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/advantage.py#L32) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config)
- used by: [`advantage`](rollouter.md#RolloutWorker.Config.advantage), [`__init__`](advantage.md#AdvantageEstimator.__init__)  (5 test-only)

