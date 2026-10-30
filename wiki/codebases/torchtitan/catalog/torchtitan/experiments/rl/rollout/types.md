---
title: 'Module: torchtitan/experiments/rl/rollout/types.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/rollout/types.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.rollout.types`/
symbols:
  Rollout: Rollout#
  RolloutStatus: RolloutStatus#
  RolloutGroup: RolloutGroup#
  Rollout.turns: Rollout#turns.
  RolloutTurn: RolloutTurn#
  RolloutGroup.rollouts: RolloutGroup#rollouts.
  RolloutGroup.group_id: RolloutGroup#group_id.
  RolloutTurn.completion_token_ids: RolloutTurn#completion_token_ids.
  Rollout.status: Rollout#status.
  RolloutTurn.prompt_token_ids: RolloutTurn#prompt_token_ids.
  RolloutTurn.completion_message: RolloutTurn#completion_message.
  Rollout.group_id: Rollout#group_id.
  Rollout.rollout_id: Rollout#rollout_id.
  RolloutTurn.completion_logprobs: RolloutTurn#completion_logprobs.
  Rollout.reward: Rollout#reward.
  RolloutTurn.rollout_id: RolloutTurn#rollout_id.
  GenerateFn: GenerateFn#
  RolloutTurn.min_policy_version: RolloutTurn#min_policy_version.
  RolloutStatus.COMPLETED: RolloutStatus#COMPLETED.
  RolloutTurn.max_policy_version: RolloutTurn#max_policy_version.
  Rollout.advantage: Rollout#advantage.
  RolloutTurn.metrics: RolloutTurn#metrics.
  RolloutStatus.is_terminal: RolloutStatus#is_terminal().
  GenerateFn.__call__: GenerateFn#__call__().
  RolloutStatus.ONGOING: RolloutStatus#ONGOING.
  RolloutStatus.ERROR: RolloutStatus#ERROR.
  RolloutTurn.env_messages: RolloutTurn#env_messages.
  RolloutTurn.env_rewards: RolloutTurn#env_rewards.
  RolloutStatus.is_truncated: RolloutStatus#is_truncated().
  RolloutStatus.is_error: RolloutStatus#is_error().
  RolloutStatus.TRUNCATED_PROMPT_TOO_LONG: RolloutStatus#TRUNCATED_PROMPT_TOO_LONG.
  RolloutTurn.prompt_messages: RolloutTurn#prompt_messages.
  Rollout.reward_breakdown: Rollout#reward_breakdown.
  RolloutGroup.metrics: RolloutGroup#metrics.
  RolloutStatus.TRUNCATED_LENGTH: RolloutStatus#TRUNCATED_LENGTH.
  RolloutStatus.TRUNCATED_MAX_TURNS: RolloutStatus#TRUNCATED_MAX_TURNS.
  _TRUNCATED: _TRUNCATED.
  _ERROR: _ERROR.
  RolloutStatus.ERROR_PARSE: RolloutStatus#ERROR_PARSE.
  RolloutStatus.ERROR_TIMEOUT: RolloutStatus#ERROR_TIMEOUT.
  RolloutStatus.ERROR_ABORT: RolloutStatus#ERROR_ABORT.
---
# Module: [`torchtitan/experiments/rl/rollout/types.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py)

## Classes
### <a id="GenerateFn"></a>`GenerateFn`  ·  implements/extends Protocol
- def: [`torchtitan/experiments/rl/rollout/types.py:29`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L29)
- doc: Generate one model completion for a prompt.
- signature: `class GenerateFn(Protocol):`
- members:
  - <a id="GenerateFn.__call__"></a>`__call__(self, prompt_token_ids: list[int], *, request_id: str, routing_session_id: str | None = None, sampling_config: SamplingConfig | None = None)` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L36) — Run one generation.
- uses (calls/refs, reference-scoped): [`SamplingConfig`](../actors/generator.md#SamplingConfig), [`Completion`](../types.md#Completion)
- used by: [`_run_single_rollout`](rollouter.md#RolloutWorker._run_single_rollout), [`_rollout_loop`](../controller.md#Controller._rollout_loop), [`run_group`](rollouter.md#RolloutWorker.run_group), [`run_group_rollouts`](rollouter.md#Rollouter.run_group_rollouts), [`_make_generate_fn`](../controller.md#Controller._make_generate_fn)  (3 test-only)

### <a id="Rollout"></a>`Rollout`
- def: [`torchtitan/experiments/rl/rollout/types.py:133`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L133) — documented in [rl-training](../../../../../concepts/rl-training.md)
- doc: A complete rollout: ordered turns + terminal state + reward + identifier.
- signature: `class Rollout:`
- members:
  - <a id="Rollout.advantage"></a>`advantage` — [`L161`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L161) — ---
  - <a id="Rollout.group_id"></a>`group_id` — [`L139`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L139) — ---
  - <a id="Rollout.reward"></a>`reward` — [`L154`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L154) — ---
  - <a id="Rollout.reward_breakdown"></a>`reward_breakdown` — [`L157`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L157) — ---
  - <a id="Rollout.rollout_id"></a>`rollout_id` — [`L142`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L142) — ---
  - <a id="Rollout.status"></a>`status` — [`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L151) — ---
  - <a id="Rollout.turns"></a>`turns` — [`L145`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L145) — ---
- uses (calls/refs, reference-scoped): [`RolloutStatus`](types.md#RolloutStatus), [`RolloutTurn`](types.md#RolloutTurn)
- used by: [`_run_single_rollout`](rollouter.md#RolloutWorker._run_single_rollout), [`build_from_group`](../components/training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`rollout_to_training_samples`](../components/training_sample_builder.md#TrainingSampleBuilder.rollout_to_training_samples), [`compute_rollout_metrics`](../controller_metrics.md#compute_rollout_metrics), [`run_group`](rollouter.md#RolloutWorker.run_group), [`_score_single_rollout`](../rubrics/rubric.md#Rubric._score_single_rollout), [`_encode_rollout`](../rollout_recorder.md#RolloutSampleRecorder._encode_rollout), [`rollouts`](types.md#RolloutGroup.rollouts), [`score_group`](rollouter.md#RolloutWorker.score_group), [`__call__`](../rollout_recorder.md#KeepExtremeRewardsFilter.__call__), [`score_group`](../rubrics/rubric.md#Rubric.score_group), [`__call__`](advantage.md#AdvantageEstimator.__call__), [`__call__`](../rubrics/rubric.md#RewardFn.__call__)  (19 test-only)

### <a id="RolloutGroup"></a>`RolloutGroup`
- def: [`torchtitan/experiments/rl/rollout/types.py:166`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L166) — documented in [rl-training](../../../../../concepts/rl-training.md)
- signature: `class RolloutGroup:`
- members:
  - <a id="RolloutGroup.group_id"></a>`group_id` — [`L167`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L167) — ---
  - <a id="RolloutGroup.metrics"></a>`metrics` — [`L173`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L173) — ---
  - <a id="RolloutGroup.rollouts"></a>`rollouts` — [`L170`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L170) — ---
- uses (calls/refs, reference-scoped): [`Metric`](../observability/metrics/types.md#Metric), [`Rollout`](types.md#Rollout)
- used by: [`build_from_group`](../components/training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`_rollout_loop`](../controller.md#Controller._rollout_loop), [`run_group`](rollouter.md#RolloutWorker.run_group), [`_collect_validation_rollouts`](../controller.md#Controller._collect_validation_rollouts), [`take_finalized`](../components/work_buffer.md#RolloutGroupWorkBuffer.take_finalized), [`finalize_work`](../components/work_buffer.md#RolloutGroupWorkBuffer.finalize_work), [`record`](../rollout_recorder.md#RolloutSampleRecorder.record), [`run_group_rollouts`](rollouter.md#Rollouter.run_group_rollouts), [`__call__`](../rollout_recorder.md#KeepExtremeRewardsFilter.__call__), [`__call__`](advantage.md#AdvantageEstimator.__call__), [`run_group`](../actors/rollout_worker.md#RolloutWorkerActor.run_group), [`rollout_group`](../components/work_buffer.md#RolloutGroupWork.rollout_group)  (10 test-only)

### <a id="RolloutStatus"></a>`RolloutStatus`  ·  implements/extends StrEnum
- def: [`torchtitan/experiments/rl/rollout/types.py:59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L59)
- doc: Per-rollout status.
- signature: `class RolloutStatus(StrEnum):`
- members:
  - <a id="RolloutStatus.is_error"></a>`is_error(self)` — [`L75`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L75)
  - <a id="RolloutStatus.is_terminal"></a>`is_terminal(self)` — [`L78`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L78)
  - <a id="RolloutStatus.is_truncated"></a>`is_truncated(self)` — [`L72`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L72)
  - <a id="RolloutStatus.COMPLETED"></a>`COMPLETED` — [`L63`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L63)
  - <a id="RolloutStatus.ERROR"></a>`ERROR` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L70)
  - <a id="RolloutStatus.ERROR_ABORT"></a>`ERROR_ABORT` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L69)
  - <a id="RolloutStatus.ERROR_PARSE"></a>`ERROR_PARSE` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L67)
  - <a id="RolloutStatus.ERROR_TIMEOUT"></a>`ERROR_TIMEOUT` — [`L68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L68)
  - <a id="RolloutStatus.ONGOING"></a>`ONGOING` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L62)
  - <a id="RolloutStatus.TRUNCATED_LENGTH"></a>`TRUNCATED_LENGTH` — [`L64`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L64)
  - <a id="RolloutStatus.TRUNCATED_MAX_TURNS"></a>`TRUNCATED_MAX_TURNS` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L66)
  - <a id="RolloutStatus.TRUNCATED_PROMPT_TOO_LONG"></a>`TRUNCATED_PROMPT_TOO_LONG` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L65)
- uses (calls/refs, reference-scoped): [`_ERROR`](types.md#_ERROR), [`_TRUNCATED`](types.md#_TRUNCATED)
- used by: [`_run_single_rollout`](rollouter.md#RolloutWorker._run_single_rollout), [`step`](../environment/token.md#TokenEnv.step), [`compute_rollout_metrics`](../controller_metrics.md#compute_rollout_metrics), [`init`](../environment/token.md#TokenEnv.init), [`_score_single_rollout`](../rubrics/rubric.md#Rubric._score_single_rollout), [`status`](types.md#Rollout.status), [`status`](../environment/token.md#TokenEnvOutput.status)  (13 test-only)

### <a id="RolloutTurn"></a>`RolloutTurn`
- def: [`torchtitan/experiments/rl/rollout/types.py:83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L83)
- doc: Full per-turn snapshot: the prompt fed to the generator + the sampled completion +
- signature: `class RolloutTurn:`
- members:
  - <a id="RolloutTurn.completion_logprobs"></a>`completion_logprobs` — [`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L101) — ---
  - <a id="RolloutTurn.completion_message"></a>`completion_message` — [`L117`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L117) — ---
  - <a id="RolloutTurn.completion_token_ids"></a>`completion_token_ids` — [`L98`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L98) — ---
  - <a id="RolloutTurn.env_messages"></a>`env_messages` — [`L121`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L121) — ---
  - <a id="RolloutTurn.env_rewards"></a>`env_rewards` — [`L125`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L125) — ---
  - <a id="RolloutTurn.max_policy_version"></a>`max_policy_version` — [`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L108) — ---
  - <a id="RolloutTurn.metrics"></a>`metrics` — [`L128`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L128) — ---
  - <a id="RolloutTurn.min_policy_version"></a>`min_policy_version` — [`L105`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L105) — ---
  - <a id="RolloutTurn.prompt_messages"></a>`prompt_messages` — [`L112`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L112) — ---
  - <a id="RolloutTurn.prompt_token_ids"></a>`prompt_token_ids` — [`L95`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L95) — ---
  - <a id="RolloutTurn.rollout_id"></a>`rollout_id` — [`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L91) — ---
- uses (calls/refs, reference-scoped): [`Metric`](../observability/metrics/types.md#Metric), [`RolloutTurnID`](../types.md#RolloutTurnID)
- used by: [`_run_single_rollout`](rollouter.md#RolloutWorker._run_single_rollout), [`build_from_group`](../components/training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`rollout_to_training_samples`](../components/training_sample_builder.md#TrainingSampleBuilder.rollout_to_training_samples), [`compute_rollout_metrics`](../controller_metrics.md#compute_rollout_metrics), [`_encode_turn`](../rollout_recorder.md#RolloutSampleRecorder._encode_turn), [`turns`](types.md#Rollout.turns)  (20 test-only)

## Module values
- <a id="_ERROR"></a>`_ERROR` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L26)
- <a id="_TRUNCATED"></a>`_TRUNCATED` — [`L23`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/rollout/types.py#L23)

