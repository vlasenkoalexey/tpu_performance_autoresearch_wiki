---
title: 'Module: torchtitan/experiments/rl/rollout_recorder.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/rollout_recorder.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.rollout_recorder`/
symbols:
  RolloutSampleRecorder._encode_turn: RolloutSampleRecorder#_encode_turn().
  RolloutSampleRecorder._encode_rollout: RolloutSampleRecorder#_encode_rollout().
  RolloutSampleRecorder.record: RolloutSampleRecorder#record().
  RolloutSampleRecorder.Config: RolloutSampleRecorder#Config#
  KeepExtremeRewardsFilter.__call__: KeepExtremeRewardsFilter#__call__().
  KeepExtremeRewardsFilter.Config: KeepExtremeRewardsFilter#Config#
  RolloutSampleRecorder: RolloutSampleRecorder#
  RolloutSampleRecorder._path: RolloutSampleRecorder#_path.
  KeepExtremeRewardsFilter: KeepExtremeRewardsFilter#
  KeepExtremeRewardsFilter.__init__: KeepExtremeRewardsFilter#__init__().
  KeepExtremeRewardsFilter.Config.k: KeepExtremeRewardsFilter#Config#k.
  KeepExtremeRewardsFilter._k: KeepExtremeRewardsFilter#_k.
  RolloutSampleRecorder._filter: RolloutSampleRecorder#_filter.
  RolloutSampleRecorder._log_tensors: RolloutSampleRecorder#_log_tensors.
  RolloutSampleRecorder._log_logprobs: RolloutSampleRecorder#_log_logprobs.
  RolloutSampleRecorder.__init__: RolloutSampleRecorder#__init__().
  _json_default: _json_default().
  RolloutSampleRecorder.Config.filename: RolloutSampleRecorder#Config#filename.
  RolloutSampleRecorder.Config.log_tensors: RolloutSampleRecorder#Config#log_tensors.
  RolloutSampleRecorder.Config.log_logprobs: RolloutSampleRecorder#Config#log_logprobs.
---
# Module: [`torchtitan/experiments/rl/rollout_recorder.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py)

## Classes
### <a id="KeepExtremeRewardsFilter"></a>`KeepExtremeRewardsFilter`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/rollout_recorder.py:33`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L33)
- doc: Keep the k highest- and k lowest-reward rollouts of each group (unscored skipped).
- signature: `class KeepExtremeRewardsFilter(Configurable):`
- protocol/private: <a id="KeepExtremeRewardsFilter.__call__"></a>`__call__`[`L52`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L52), <a id="KeepExtremeRewardsFilter.__init__"></a>`__init__`[`L48`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L48), <a id="KeepExtremeRewardsFilter._k"></a>`_k`[`L49`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L49)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`log_trace_span`](../../observability/structured_logger/structured_logging.md#log_trace_span), [`Rollout`](rollout/types.md#Rollout), [`RolloutGroup`](rollout/types.md#RolloutGroup), [`rollouts`](rollout/types.md#RolloutGroup.rollouts), [`reward`](rollout/types.md#Rollout.reward), [`Config`](rollout_recorder.md#KeepExtremeRewardsFilter.Config), [`k`](rollout_recorder.md#KeepExtremeRewardsFilter.Config.k)
- used by: [`Configurable`](../../config/configurable.md#Configurable), [`Config`](rollout_recorder.md#RolloutSampleRecorder.Config)  (2 test-only)

### <a id="KeepExtremeRewardsFilter.Config"></a>`KeepExtremeRewardsFilter.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/rollout_recorder.py:44`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L44)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="KeepExtremeRewardsFilter.Config.k"></a>`k` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L45) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`Config`](../../config/configurable.md#Configurable.Config)
- used by: [`Config`](rollout_recorder.md#RolloutSampleRecorder.Config), [`__init__`](rollout_recorder.md#KeepExtremeRewardsFilter.__init__)  (2 test-only)

### <a id="RolloutSampleRecorder"></a>`RolloutSampleRecorder`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/rollout_recorder.py:65`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L65)
- doc: Append rollouts to a JSONL file for debugging and inspection.
- signature: `class RolloutSampleRecorder(Configurable):`
- members:
  - <a id="RolloutSampleRecorder._encode_rollout"></a>`_encode_rollout(self, rollout: Rollout)` — [`L118`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L118) — One JSON object per rollout: its scalar fields + each turn (see `_encode_turn`).
  - <a id="RolloutSampleRecorder._encode_turn"></a>`_encode_turn(self, turn: RolloutTurn)` — [`L130`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L130) — One JSON object per turn. The large token / logprob arrays are opt-in
  - <a id="RolloutSampleRecorder.record"></a>`record(self, *, is_validation: bool, rollout_groups: list[RolloutGroup])` — [`L99`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L99) — Append the filtered rollouts to the JSONL, one JSON object per rollout.
- protocol/private: <a id="RolloutSampleRecorder.__init__"></a>`__init__`[`L91`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L91), <a id="RolloutSampleRecorder._filter"></a>`_filter`[`L92`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L92), <a id="RolloutSampleRecorder._log_logprobs"></a>`_log_logprobs`[`L94`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L94), <a id="RolloutSampleRecorder._log_tensors"></a>`_log_tensors`[`L93`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L93), <a id="RolloutSampleRecorder._path"></a>`_path`[`L95`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L95)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`build`](../../config/configurable.md#Configurable.Config.build), [`log_trace_span`](../../observability/structured_logger/structured_logging.md#log_trace_span), [`Rollout`](rollout/types.md#Rollout), [`RolloutGroup`](rollout/types.md#RolloutGroup), [`turns`](rollout/types.md#Rollout.turns), [`RolloutTurn`](rollout/types.md#RolloutTurn), [`completion_token_ids`](rollout/types.md#RolloutTurn.completion_token_ids), [`turn_id`](types.md#RolloutTurnID.turn_id), [`status`](rollout/types.md#Rollout.status), [`Config`](rollout_recorder.md#RolloutSampleRecorder.Config), [`completion_message`](rollout/types.md#RolloutTurn.completion_message), [`group_id`](rollout/types.md#Rollout.group_id), [`prompt_token_ids`](rollout/types.md#RolloutTurn.prompt_token_ids), [`rollout_id`](rollout/types.md#Rollout.rollout_id), [`completion_logprobs`](rollout/types.md#RolloutTurn.completion_logprobs), [`reward`](rollout/types.md#Rollout.reward), [`rollout_id`](rollout/types.md#RolloutTurn.rollout_id), [`min_policy_version`](rollout/types.md#RolloutTurn.min_policy_version), [`max_policy_version`](rollout/types.md#RolloutTurn.max_policy_version), [`advantage`](rollout/types.md#Rollout.advantage), [`env_messages`](rollout/types.md#RolloutTurn.env_messages), [`env_rewards`](rollout/types.md#RolloutTurn.env_rewards), [`prompt_messages`](rollout/types.md#RolloutTurn.prompt_messages), [`reward_breakdown`](rollout/types.md#Rollout.reward_breakdown), [`_json_default`](rollout_recorder.md#_json_default), [`filename`](rollout_recorder.md#RolloutSampleRecorder.Config.filename), [`log_logprobs`](rollout_recorder.md#RolloutSampleRecorder.Config.log_logprobs), [`log_tensors`](rollout_recorder.md#RolloutSampleRecorder.Config.log_tensors)
- used by: [`Configurable`](../../config/configurable.md#Configurable), [`rollout_recorder`](controller.md#Controller.Config.rollout_recorder)  (9 test-only)

### <a id="RolloutSampleRecorder.Config"></a>`RolloutSampleRecorder.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/rollout_recorder.py:79`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L79)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="RolloutSampleRecorder.Config.filename"></a>`filename` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L84) — ---
  - <a id="RolloutSampleRecorder.Config.log_logprobs"></a>`log_logprobs` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L88) — ---
  - <a id="RolloutSampleRecorder.Config.log_tensors"></a>`log_tensors` — [`L86`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L86) — ---
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`Config`](../../config/configurable.md#Configurable.Config), [`Config`](rollout_recorder.md#KeepExtremeRewardsFilter.Config), [`KeepExtremeRewardsFilter`](rollout_recorder.md#KeepExtremeRewardsFilter)
- used by: [`_path`](rollout_recorder.md#RolloutSampleRecorder._path), [`rollout_recorder`](controller.md#Controller.Config.rollout_recorder), [`_log_logprobs`](rollout_recorder.md#RolloutSampleRecorder._log_logprobs), [`_log_tensors`](rollout_recorder.md#RolloutSampleRecorder._log_tensors), [`__init__`](rollout_recorder.md#RolloutSampleRecorder.__init__)  (2 test-only)

## Functions
- <a id="_json_default"></a>`_json_default(value: Any)` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout_recorder.py#L25)

