---
title: 'Module: torchtitan/experiments/rl/components/batcher.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/components/batcher.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.components.batcher`/
symbols:
  Batcher.add_training_samples: Batcher#add_training_samples().
  Batcher._pack_one_training_batch: Batcher#_pack_one_training_batch().
  Batcher._pack_training_sample_row: Batcher#_pack_training_sample_row().
  Batcher.collate: Batcher#collate().
  Batcher._build_microbatch_grid: Batcher#_build_microbatch_grid().
  Batcher._take_groups: Batcher#_take_groups().
  Batcher._build_document_limited_microbatch_grid: Batcher#_build_document_limited_microbatch_grid().
  Batcher._packing_metrics: Batcher#_packing_metrics().
  Batcher: Batcher#
  Batcher.Config: Batcher#Config#
  Batcher._record_untrainable_groups: Batcher#_record_untrainable_groups().
  Batcher._assign_training_samples_to_rows: Batcher#_assign_training_samples_to_rows().
  Batcher.num_tokens_to_pack: Batcher#num_tokens_to_pack().
  Batcher._dp_degree: Batcher#_dp_degree.
  Batcher._max_num_documents: Batcher#_max_num_documents.
  Batcher._groups_for_next_batch: Batcher#_groups_for_next_batch.
  Batcher.Config.max_num_documents: Batcher#Config#max_num_documents.
  Batcher._per_sample_pad_multiple: Batcher#_per_sample_pad_multiple.
  Batcher.seq_len: Batcher#seq_len.
  Batcher._num_consecutive_zero_output_groups: Batcher#_num_consecutive_zero_output_groups.
  Batcher._num_rows_per_microbatch: Batcher#_num_rows_per_microbatch.
  Batcher._num_prompts_per_train_step: Batcher#_num_prompts_per_train_step.
  Batcher.Config.__post_init__: Batcher#Config#__post_init__().
  Batcher.__init__: Batcher#__init__().
  logger: logger.
  _MAX_CONSECUTIVE_UNTRAINABLE_BATCHES: _MAX_CONSECUTIVE_UNTRAINABLE_BATCHES.
  Batcher.pad_id: Batcher#pad_id.
  Batcher.Config.per_sample_pad_multiple: Batcher#Config#per_sample_pad_multiple.
  _PAD_VALUES._PAD_VALUES: _PAD_VALUES._PAD_VALUES.
  _DTYPES._DTYPES: _DTYPES._DTYPES.
---
# Module: [`torchtitan/experiments/rl/components/batcher.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py)

## Classes
### <a id="Batcher"></a>`Batcher`  ·  implements/extends Configurable
- def: [`torchtitan/experiments/rl/components/batcher.py:47`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L47)
- doc: Accumulate `num_prompts_per_train_step` groups and packs
- signature: `class Batcher(Configurable):`
- members:
  - <a id="Batcher._assign_training_samples_to_rows"></a>`_assign_training_samples_to_rows(self, training_samples: list[TrainingSample])` — [`L281`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L281) — Next-fit samples into context-length rows.
  - <a id="Batcher._build_document_limited_microbatch_grid"></a>`_build_document_limited_microbatch_grid(self, packed_rows: list[dict])` — [`L374`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L374) — Pack rows into local microbatch cells within both capacities.
  - <a id="Batcher._build_microbatch_grid"></a>`_build_microbatch_grid(self, packed_rows: list[dict])` — [`L336`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L336) — Build `[num_microbatches][dp_degree]` from however many rows packing produced (variable count).
  - <a id="Batcher._pack_one_training_batch"></a>`_pack_one_training_batch(self)` — [`L199`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L199) — Pack the oldest accumulated groups (up to `num_prompts_per_train_step` trainable groups) into one batch.
  - <a id="Batcher._pack_training_sample_row"></a>`_pack_training_sample_row(self, training_samples: list[TrainingSample])` — [`L423`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L423) — Concatenate one row's samples into a `[seq_len]` padded token chunk.
  - <a id="Batcher._packing_metrics"></a>`_packing_metrics(self, packed_rows: list[dict], training_samples: list[TrainingSample], num_rollout_groups: int, num_metric_only_groups: int, num_microbatches: int)` — [`L504`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L504) — Per-training-batch packing + count metrics. (policy age is logged at trainer consume time.)
  - <a id="Batcher._record_untrainable_groups"></a>`_record_untrainable_groups(self, *, group_is_trainable: bool)` — [`L109`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L109) — Fail when consecutive groups cannot contribute one training sample.
  - <a id="Batcher._take_groups"></a>`_take_groups(self)` — [`L252`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L252) — Pop accumulated groups oldest-first until `num_prompts_per_train_step` are taken.
  - <a id="Batcher.add_training_samples"></a>`add_training_samples(self, *, training_sample_group: TrainingSampleGroup)` — [`L147`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L147) — Add one group and report whether any samples survive batcher filtering.
  - <a id="Batcher.collate"></a>`collate(self, rows: list[dict])` — [`L492`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L492) — Concatenate packed rows into a single flat microbatch.
  - <a id="Batcher.num_tokens_to_pack"></a>`num_tokens_to_pack(self, training_sample: TrainingSample)` — [`L319`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L319) — Tokens this training_sample contributes to a packed row.
  - <a id="Batcher.pad_id"></a>`pad_id` — [`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L101)
  - <a id="Batcher.seq_len"></a>`seq_len` — [`L90`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L90)
- protocol/private: <a id="Batcher.__init__"></a>`__init__`[`L80`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L80), <a id="Batcher._dp_degree"></a>`_dp_degree`[`L105`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L105), <a id="Batcher._groups_for_next_batch"></a>`_groups_for_next_batch`[`L106`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L106), <a id="Batcher._max_num_documents"></a>`_max_num_documents`[`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L103), <a id="Batcher._num_consecutive_zero_output_groups"></a>`_num_consecutive_zero_output_groups`[`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L107), <a id="Batcher._num_prompts_per_train_step"></a>`_num_prompts_per_train_step`[`L104`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L104), <a id="Batcher._num_rows_per_microbatch"></a>`_num_rows_per_microbatch`[`L91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L91), <a id="Batcher._per_sample_pad_multiple"></a>`_per_sample_pad_multiple`[`L102`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L102)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Metric`](../observability/metrics/types.md#Metric), [`NoReduce`](../observability/metrics/types.md#NoReduce), [`TrainingSample`](../types.md#TrainingSample), [`TrainingSampleGroup`](../types.md#TrainingSampleGroup), [`Sum`](../observability/metrics/types.md#Sum), [`training_samples`](../types.md#TrainingSampleGroup.training_samples), [`Config`](batcher.md#Batcher.Config), [`metrics`](../types.md#TrainingSampleGroup.metrics), [`TrainingMicrobatch`](../types.md#TrainingMicrobatch), [`TrainingBatch`](../types.md#TrainingBatch), [`token_ids`](../types.md#TrainingSample.token_ids), [`logprobs`](../types.md#TrainingSample.logprobs), [`loss_mask`](../types.md#TrainingSample.loss_mask), [`max_num_documents`](batcher.md#Batcher.Config.max_num_documents), [`advantage`](../types.md#TrainingSample.advantage), [`metrics`](../types.md#TrainingBatch.metrics), [`microbatches`](../types.md#TrainingBatch.microbatches), [`min_policy_version`](../types.md#TrainingSample.min_policy_version), [`num_global_valid_tokens`](../types.md#TrainingBatch.num_global_valid_tokens), [`_MAX_CONSECUTIVE_UNTRAINABLE_BATCHES`](batcher.md#_MAX_CONSECUTIVE_UNTRAINABLE_BATCHES), [`advantages`](../types.md#TrainingMicrobatch.advantages), [`generator_logprobs`](../types.md#TrainingMicrobatch.generator_logprobs), [`labels`](../types.md#TrainingMicrobatch.labels), [`logger`](batcher.md#logger), [`loss_mask`](../types.md#TrainingMicrobatch.loss_mask), [`min_policy_versions`](../types.md#TrainingBatch.min_policy_versions), [`padding_mask`](../types.md#TrainingMicrobatch.padding_mask), [`positions`](../types.md#TrainingMicrobatch.positions), [`token_ids`](../types.md#TrainingMicrobatch.token_ids), [`_DTYPES`](batcher.md#_DTYPES._DTYPES), [`_PAD_VALUES`](batcher.md#_PAD_VALUES._PAD_VALUES), [`per_sample_pad_multiple`](batcher.md#Batcher.Config.per_sample_pad_multiple)
- used by: [`Configurable`](../../../config/configurable.md#Configurable), [`_batcher_loop`](../controller.md#Controller._batcher_loop), [`batcher`](../controller.md#AsyncLoopConfig.batcher)  (12 test-only)

### <a id="Batcher.Config"></a>`Batcher.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/rl/components/batcher.py:68`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L68)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="Batcher.Config.max_num_documents"></a>`max_num_documents` — [`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L73) — ---
  - <a id="Batcher.Config.per_sample_pad_multiple"></a>`per_sample_pad_multiple` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L69) — ---
- protocol/private: <a id="Batcher.Config.__post_init__"></a>`__post_init__`[`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L76)
- uses (calls/refs, reference-scoped): [`Configurable`](../../../config/configurable.md#Configurable), [`Config`](../../../config/configurable.md#Configurable.Config)
- used by: [`trainer_dp_degree`](../controller.md#Controller.trainer_dp_degree), [`batcher`](../controller.md#AsyncLoopConfig.batcher), [`_max_num_documents`](batcher.md#Batcher._max_num_documents), [`_per_sample_pad_multiple`](batcher.md#Batcher._per_sample_pad_multiple), [`__init__`](batcher.md#Batcher.__init__)  (7 test-only)

## Module values
- <a id="_DTYPES._DTYPES"></a>`_DTYPES` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L38)
- <a id="_MAX_CONSECUTIVE_UNTRAINABLE_BATCHES"></a>`_MAX_CONSECUTIVE_UNTRAINABLE_BATCHES` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L28)
- <a id="_PAD_VALUES._PAD_VALUES"></a>`_PAD_VALUES` — [`L31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L31)
- <a id="logger"></a>`logger` — [`L26`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/components/batcher.py#L26)

