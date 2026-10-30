---
title: 'Module: torchtitan/experiments/rl/components/training_sample_builder.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/components/training_sample_builder.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.components.training_sample_builder`/
symbols:
  TrainingSampleBuilder.build_from_group: TrainingSampleBuilder#build_from_group().
  TrainingSampleBuilder.rollout_to_training_samples: TrainingSampleBuilder#rollout_to_training_samples().
  TrainingSampleBuilder: TrainingSampleBuilder#
  TrainingSampleBuilder.Config: TrainingSampleBuilder#Config#
  _has_valid_loss_token: _has_valid_loss_token().
  TrainingSampleBuilder.Config.drop_zero_std_reward_groups: TrainingSampleBuilder#Config#drop_zero_std_reward_groups.
  TrainingSampleBuilder.__init__: TrainingSampleBuilder#__init__().
  TrainingSampleBuilder.config: TrainingSampleBuilder#config.
---
# Module: [`torchtitan/experiments/rl/components/training_sample_builder.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/training_sample_builder.py)

## Classes
### <a id="TrainingSampleBuilder"></a>`TrainingSampleBuilder`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/components/training_sample_builder.py:38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/training_sample_builder.py#L38)
- doc: Build trainable samples and metrics the trainer consumes from rollout groups.
- signature: `class TrainingSampleBuilder(Configurable):`
- members:
  - <a id="TrainingSampleBuilder.build_from_group"></a>`build_from_group(self, *, rollout_group: RolloutGroup)` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/training_sample_builder.py#L56) — Apply data-validity filters and convert surviving rollouts to training_samples. — documented in [rl-training](../../../../../concepts/rl-training.md)
  - <a id="TrainingSampleBuilder.rollout_to_training_samples"></a>`rollout_to_training_samples(self, rollout: Rollout)` — [`L168`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/training_sample_builder.py#L168) — Pack a scored `Rollout` into training training_samples — usually one, or several where its turns branch. — documented in [rl-training](../../../../../concepts/rl-training.md)
  - <a id="TrainingSampleBuilder.config"></a>`config` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/training_sample_builder.py#L54)
- protocol/private: <a id="TrainingSampleBuilder.__init__"></a>`__init__`[`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/training_sample_builder.py#L53)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Metric`](../observability/metrics/types.md#Metric), [`Rollout`](../rollout/types.md#Rollout), [`RolloutGroup`](../rollout/types.md#RolloutGroup), [`Mean`](../observability/metrics/types.md#Mean), [`turns`](../rollout/types.md#Rollout.turns), [`Max`](../observability/metrics/types.md#Max), [`RolloutTurnID`](../types.md#RolloutTurnID), [`rollouts`](../rollout/types.md#RolloutGroup.rollouts), [`from_list`](../observability/metrics/types.md#Max.from_list), [`TrainingSample`](../types.md#TrainingSample), [`from_list`](../observability/metrics/types.md#SummaryStats.from_list), [`from_list`](../observability/metrics/types.md#Mean.from_list), [`group_id`](../rollout/types.md#RolloutGroup.group_id), [`completion_token_ids`](../rollout/types.md#RolloutTurn.completion_token_ids), [`turn_id`](../types.md#RolloutTurnID.turn_id), [`TrainingSampleGroup`](../types.md#TrainingSampleGroup), [`group_id`](../types.md#RolloutTurnID.group_id), [`rollout_id`](../types.md#RolloutTurnID.rollout_id), [`Sum`](../observability/metrics/types.md#Sum), [`training_samples`](../types.md#TrainingSampleGroup.training_samples), [`group_id`](../rollout/types.md#Rollout.group_id), [`prompt_token_ids`](../rollout/types.md#RolloutTurn.prompt_token_ids), [`Config`](training_sample_builder.md#TrainingSampleBuilder.Config), [`rollout_id`](../rollout/types.md#Rollout.rollout_id), [`SummaryStats`](../observability/metrics/types.md#SummaryStats), [`metrics`](../types.md#TrainingSampleGroup.metrics), [`completion_logprobs`](../rollout/types.md#RolloutTurn.completion_logprobs), [`reward`](../rollout/types.md#Rollout.reward), [`Min`](../observability/metrics/types.md#Min), [`min_policy_version`](../rollout/types.md#RolloutTurn.min_policy_version), [`from_list`](../observability/metrics/types.md#Min.from_list), [`group_id`](../types.md#TrainingSampleGroup.group_id), [`_has_valid_loss_token`](training_sample_builder.md#_has_valid_loss_token), [`max_policy_version`](../rollout/types.md#RolloutTurn.max_policy_version), [`token_ids`](../types.md#TrainingSample.token_ids), [`advantage`](../rollout/types.md#Rollout.advantage), [`logprobs`](../types.md#TrainingSample.logprobs), [`loss_mask`](../types.md#TrainingSample.loss_mask), [`advantage`](../types.md#TrainingSample.advantage)  (+5 more)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`_batcher_loop`](../controller.md#Controller._batcher_loop), [`training_sample_builder`](../controller.md#AsyncLoopConfig.training_sample_builder)  (6 test-only)

### <a id="TrainingSampleBuilder.Config"></a>`TrainingSampleBuilder.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/components/training_sample_builder.py:47`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/training_sample_builder.py#L47)
- doc: TrainingSample builder filtering knobs.
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="TrainingSampleBuilder.Config.drop_zero_std_reward_groups"></a>`drop_zero_std_reward_groups` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/training_sample_builder.py#L50) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config)
- used by: [`build_from_group`](training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`training_sample_builder`](../controller.md#AsyncLoopConfig.training_sample_builder), [`__init__`](training_sample_builder.md#TrainingSampleBuilder.__init__)  (6 test-only)

## Functions
- <a id="_has_valid_loss_token"></a>`_has_valid_loss_token(training_sample: TrainingSample)` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/training_sample_builder.py#L26) — Return whether the shifted sample has a token usable by the RL loss.

