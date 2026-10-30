---
title: 'Module: torchtitan/experiments/rl/types.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/types.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.types`/
symbols:
  RolloutTurnID: RolloutTurnID#
  Completion: Completion#
  TrainingSample: TrainingSample#
  RolloutTurnID.turn_id: RolloutTurnID#turn_id.
  RolloutTurnID.group_id: RolloutTurnID#group_id.
  RolloutTurnID.rollout_id: RolloutTurnID#rollout_id.
  TrainingSampleGroup: TrainingSampleGroup#
  TrainingSampleGroup.training_samples: TrainingSampleGroup#training_samples.
  TrainingSampleGroup.metrics: TrainingSampleGroup#metrics.
  Completion.token_ids: Completion#token_ids.
  RolloutTurnID.to_string: RolloutTurnID#to_string().
  Completion.finish_reason: Completion#finish_reason.
  TrainingMicrobatch: TrainingMicrobatch#
  Completion.min_policy_version: Completion#min_policy_version.
  TrainingSampleGroup.group_id: TrainingSampleGroup#group_id.
  Completion.max_policy_version: Completion#max_policy_version.
  Completion.token_logprobs: Completion#token_logprobs.
  TrainingSample.token_ids: TrainingSample#token_ids.
  TrainingBatch: TrainingBatch#
  TrainingSample.loss_mask: TrainingSample#loss_mask.
  TrainingSample.logprobs: TrainingSample#logprobs.
  Completion.metrics: Completion#metrics.
  Completion.request_id: Completion#request_id.
  TrainingSample.advantage: TrainingSample#advantage.
  TrainingSample.max_policy_version: TrainingSample#max_policy_version.
  TrainingSample.rollout_id: TrainingSample#rollout_id.
  TrainingBatch.microbatches: TrainingBatch#microbatches.
  TrainingBatch.metrics: TrainingBatch#metrics.
  TrainingSample.min_policy_version: TrainingSample#min_policy_version.
  TrainingBatch.num_global_valid_tokens: TrainingBatch#num_global_valid_tokens.
  OptimStepOutput: OptimStepOutput#
  TrainingMicrobatch.token_ids: TrainingMicrobatch#token_ids.
  TrainingMicrobatch.labels: TrainingMicrobatch#labels.
  TrainingMicrobatch.positions: TrainingMicrobatch#positions.
  TrainingMicrobatch.generator_logprobs: TrainingMicrobatch#generator_logprobs.
  TrainingMicrobatch.loss_mask: TrainingMicrobatch#loss_mask.
  TrainingMicrobatch.advantages: TrainingMicrobatch#advantages.
  TrainingMicrobatch.padding_mask: TrainingMicrobatch#padding_mask.
  TrainingBatch.min_policy_versions: TrainingBatch#min_policy_versions.
  OptimStepOutput.policy_version: OptimStepOutput#policy_version.
  OptimStepOutput.metrics: OptimStepOutput#metrics.
---
# Module: [`torchtitan/experiments/rl/types.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py)

## Classes
### <a id="Completion"></a>`Completion`
- def: [`torchtitan/experiments/rl/types.py:40`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L40)
- doc: A single generated sequence from the generator.
- signature: `class Completion:`
- members:
  - <a id="Completion.finish_reason"></a>`finish_reason` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L62) — ---
  - <a id="Completion.max_policy_version"></a>`max_policy_version` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L52) — ---
  - <a id="Completion.metrics"></a>`metrics` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L65) — ---
  - <a id="Completion.min_policy_version"></a>`min_policy_version` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L50) — ---
  - <a id="Completion.request_id"></a>`request_id` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L57) — ---
  - <a id="Completion.token_ids"></a>`token_ids` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L60)
  - <a id="Completion.token_logprobs"></a>`token_logprobs` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L61)
- uses (calls/refs, reference-scoped): [`Metric`](observability/metrics/types.md#Metric)
- used by: [`_run_single_rollout`](rollout/rollouter.md#RolloutWorker._run_single_rollout), [`step`](environment/token.md#TokenEnv.step), [`generate`](actors/generator.md#VLLMGenerator.generate), [`_rank0_resolve_futures`](actors/generator.md#RequestDispatcher._rank0_resolve_futures), [`_build_completions`](actors/generator.md#RequestDispatcher._build_completions), [`rank0_register_future`](actors/generator.md#RequestDispatcher.rank0_register_future), [`generate`](controller.md#Controller.generate), [`future`](actors/generator.md#GenerationFuture.future), [`__call__`](rollout/types.md#GenerateFn.__call__)  (6 test-only)

### <a id="OptimStepOutput"></a>`OptimStepOutput`
- def: [`torchtitan/experiments/rl/types.py:159`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L159)
- doc: Result returned by `PolicyTrainer.optim_step` to the controller.
- signature: `class OptimStepOutput:`
- members:
  - <a id="OptimStepOutput.metrics"></a>`metrics` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L163)
  - <a id="OptimStepOutput.policy_version"></a>`policy_version` — [`L162`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L162)
- used by: [`optim_step`](actors/trainer.md#PolicyTrainer.optim_step)

### <a id="RolloutTurnID"></a>`RolloutTurnID`
- def: [`torchtitan/experiments/rl/types.py:15`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L15)
- doc: A turn's id: (group, sibling rollout, turn index); renders to the generator request_id.
- signature: `class RolloutTurnID:`
- members:
  - <a id="RolloutTurnID.to_string"></a>`to_string(self, *, include_turn: bool = True)` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L34)
  - <a id="RolloutTurnID.group_id"></a>`group_id` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L26) — ---
  - <a id="RolloutTurnID.rollout_id"></a>`rollout_id` — [`L28`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L28) — ---
  - <a id="RolloutTurnID.turn_id"></a>`turn_id` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L30) — ---
- used by: [`_run_single_rollout`](rollout/rollouter.md#RolloutWorker._run_single_rollout), [`rollout_to_training_samples`](components/training_sample_builder.md#TrainingSampleBuilder.rollout_to_training_samples), [`_encode_turn`](rollout_recorder.md#RolloutSampleRecorder._encode_turn), [`rollout_id`](rollout/types.md#RolloutTurn.rollout_id), [`rollout_id`](types.md#TrainingSample.rollout_id)  (12 test-only)

### <a id="TrainingBatch"></a>`TrainingBatch`
- def: [`torchtitan/experiments/rl/types.py:138`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L138)
- doc: Packed microbatches for one optimizer step.
- signature: `class TrainingBatch:`
- members:
  - <a id="TrainingBatch.metrics"></a>`metrics` — [`L153`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L153)
  - <a id="TrainingBatch.microbatches"></a>`microbatches` — [`L151`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L151)
  - <a id="TrainingBatch.min_policy_versions"></a>`min_policy_versions` — [`L155`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L155)
  - <a id="TrainingBatch.num_global_valid_tokens"></a>`num_global_valid_tokens` — [`L152`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L152)
- uses (calls/refs, reference-scoped): [`Metric`](observability/metrics/types.md#Metric), [`TrainingMicrobatch`](types.md#TrainingMicrobatch)
- used by: [`_trainer_loop`](controller.md#Controller._trainer_loop), [`_weight_sync`](controller.md#Controller._weight_sync), [`add_training_samples`](components/batcher.md#Batcher.add_training_samples), [`_pack_one_training_batch`](components/batcher.md#Batcher._pack_one_training_batch), [`_batcher_loop`](controller.md#Controller._batcher_loop)  (1 test-only)

### <a id="TrainingMicrobatch"></a>`TrainingMicrobatch`
- def: [`torchtitan/experiments/rl/types.py:119`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L119)
- doc: Packed training batch for the RL trainer.
- signature: `class TrainingMicrobatch:`
- members:
  - <a id="TrainingMicrobatch.advantages"></a>`advantages` — [`L132`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L132)
  - <a id="TrainingMicrobatch.generator_logprobs"></a>`generator_logprobs` — [`L130`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L130)
  - <a id="TrainingMicrobatch.labels"></a>`labels` — [`L128`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L128)
  - <a id="TrainingMicrobatch.loss_mask"></a>`loss_mask` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L131)
  - <a id="TrainingMicrobatch.padding_mask"></a>`padding_mask` — [`L133`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L133) — ---
  - <a id="TrainingMicrobatch.positions"></a>`positions` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L129)
  - <a id="TrainingMicrobatch.token_ids"></a>`token_ids` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L127)
- used by: [`forward_backward`](actors/trainer.md#PolicyTrainer.forward_backward), [`collate`](components/batcher.md#Batcher.collate), [`_build_microbatch_grid`](components/batcher.md#Batcher._build_microbatch_grid), [`_build_document_limited_microbatch_grid`](components/batcher.md#Batcher._build_document_limited_microbatch_grid), [`microbatches`](types.md#TrainingBatch.microbatches)

### <a id="TrainingSample"></a>`TrainingSample`
- def: [`torchtitan/experiments/rl/types.py:71`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L71)
- doc: A trainable token sequence from a rollout.
- signature: `class TrainingSample:`
- members:
  - <a id="TrainingSample.advantage"></a>`advantage` — [`L100`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L100) — ---
  - <a id="TrainingSample.logprobs"></a>`logprobs` — [`L98`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L98) — ---
  - <a id="TrainingSample.loss_mask"></a>`loss_mask` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L96) — ---
  - <a id="TrainingSample.max_policy_version"></a>`max_policy_version` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L90) — ---
  - <a id="TrainingSample.min_policy_version"></a>`min_policy_version` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L88) — ---
  - <a id="TrainingSample.rollout_id"></a>`rollout_id` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L92) — ---
  - <a id="TrainingSample.token_ids"></a>`token_ids` — [`L94`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L94) — ---
- uses (calls/refs, reference-scoped): [`RolloutTurnID`](types.md#RolloutTurnID)
- used by: [`build_from_group`](components/training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`rollout_to_training_samples`](components/training_sample_builder.md#TrainingSampleBuilder.rollout_to_training_samples), [`_pack_one_training_batch`](components/batcher.md#Batcher._pack_one_training_batch), [`_pack_training_sample_row`](components/batcher.md#Batcher._pack_training_sample_row), [`training_samples`](types.md#TrainingSampleGroup.training_samples), [`_packing_metrics`](components/batcher.md#Batcher._packing_metrics), [`_take_groups`](components/batcher.md#Batcher._take_groups), [`_assign_training_samples_to_rows`](components/batcher.md#Batcher._assign_training_samples_to_rows), [`num_tokens_to_pack`](components/batcher.md#Batcher.num_tokens_to_pack), [`_has_valid_loss_token`](components/training_sample_builder.md#_has_valid_loss_token)  (2 test-only)

### <a id="TrainingSampleGroup"></a>`TrainingSampleGroup`
- def: [`torchtitan/experiments/rl/types.py:105`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L105)
- doc: The training samples + metrics built from one rollout group.
- signature: `class TrainingSampleGroup:`
- members:
  - <a id="TrainingSampleGroup.group_id"></a>`group_id` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L113)
  - <a id="TrainingSampleGroup.metrics"></a>`metrics` — [`L115`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L115)
  - <a id="TrainingSampleGroup.training_samples"></a>`training_samples` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/types.py#L114)
- uses (calls/refs, reference-scoped): [`Metric`](observability/metrics/types.md#Metric), [`TrainingSample`](types.md#TrainingSample)
- used by: [`build_from_group`](components/training_sample_builder.md#TrainingSampleBuilder.build_from_group), [`add_training_samples`](components/batcher.md#Batcher.add_training_samples), [`_take_groups`](components/batcher.md#Batcher._take_groups), [`_groups_for_next_batch`](components/batcher.md#Batcher._groups_for_next_batch)  (5 test-only)

