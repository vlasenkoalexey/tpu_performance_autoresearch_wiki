---
title: 'Module: src/vllm_torchtpu/core/pp_chunk_scheduler.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/core/pp_chunk_scheduler.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.core.pp_chunk_scheduler`/
symbols:
  TpuPipelineChunkScheduler._mamba_block_aligned_split: TpuPipelineChunkScheduler#_mamba_block_aligned_split().
  TpuPipelineChunkScheduler.schedule: TpuPipelineChunkScheduler#schedule().
  TpuPipelineChunkScheduler._pending_step_limit: TpuPipelineChunkScheduler#_pending_step_limit().
  TpuPipelineChunkScheduler._cost: TpuPipelineChunkScheduler#_cost.
  TpuPipelineChunkScheduler.install_cost_model: TpuPipelineChunkScheduler#install_cost_model().
  profile_and_install_cost_model: profile_and_install_cost_model().
  TpuPipelineChunkScheduler._account: TpuPipelineChunkScheduler#_account().
  patch_engine_core_for_pp_chunks: patch_engine_core_for_pp_chunks().
  uses_dynamic_chunks: uses_dynamic_chunks().
  TpuPipelineChunkScheduler.step_estimate_ms: TpuPipelineChunkScheduler#step_estimate_ms().
  logger: logger.
  SCHEDULER_CLS: SCHEDULER_CLS.
  _prefill_end: _prefill_end().
  TpuPipelineChunkScheduler._step_tokens: TpuPipelineChunkScheduler#_step_tokens.
  TpuPipelineChunkScheduler._mamba_split: TpuPipelineChunkScheduler#_mamba_split.
  TpuPipelineChunkScheduler._waits: TpuPipelineChunkScheduler#_waits.
  patch_engine_core_for_pp_chunks.__init__: patch_engine_core_for_pp_chunks().__init__().
  TpuPipelineChunkScheduler._pp_size: TpuPipelineChunkScheduler#_pp_size.
  TpuPipelineChunkScheduler._step_pairs: TpuPipelineChunkScheduler#_step_pairs.
  TpuPipelineChunkScheduler._step_squares: TpuPipelineChunkScheduler#_step_squares.
  TpuPipelineChunkScheduler._step_prefill_tokens: TpuPipelineChunkScheduler#_step_prefill_tokens.
  TpuPipelineChunkScheduler._step_schedule: TpuPipelineChunkScheduler#_step_schedule.
  TpuPipelineChunkScheduler._seeded: TpuPipelineChunkScheduler#_seeded.
  TpuPipelineChunkScheduler._step_limit: TpuPipelineChunkScheduler#_step_limit.
  TpuPipelineChunkScheduler: TpuPipelineChunkScheduler#
  TpuPipelineChunkScheduler.need_mamba_block_aligned_split: TpuPipelineChunkScheduler#need_mamba_block_aligned_split.
  TpuPipelineChunkScheduler._clips: TpuPipelineChunkScheduler#_clips.
  TpuPipelineChunkScheduler.__init__: TpuPipelineChunkScheduler#__init__().
---
# Module: [`src/vllm_torchtpu/core/pp_chunk_scheduler.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py)

## Classes
### <a id="TpuPipelineChunkScheduler"></a>`TpuPipelineChunkScheduler`
- def: [`src/vllm_torchtpu/core/pp_chunk_scheduler.py:62`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L62)
- signature: `class TpuPipelineChunkScheduler(Scheduler):`
- members:
  - <a id="TpuPipelineChunkScheduler._pending_step_limit"></a>`_pending_step_limit(self)` — [`L126`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L126) — The bucket a step is held to: the prefill work still to schedule — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="TpuPipelineChunkScheduler.install_cost_model"></a>`install_cost_model(self, model: StepCostModel)` — [`L80`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L80) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="TpuPipelineChunkScheduler.schedule"></a>`schedule(self, throttle_prefills: bool = False)` — [`L90`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L90) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="TpuPipelineChunkScheduler.step_estimate_ms"></a>`step_estimate_ms(self, scheduler_output: Any)` — [`L109`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L109) — Modelled time on one stage of the step the last ``schedule``
  - <a id="TpuPipelineChunkScheduler.need_mamba_block_aligned_split"></a>`need_mamba_block_aligned_split` — [`L69`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L69)
- protocol/private: <a id="TpuPipelineChunkScheduler.__init__"></a>`__init__`[`L63`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L63), <a id="TpuPipelineChunkScheduler._account"></a>`_account`[`L85`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L85), <a id="TpuPipelineChunkScheduler._clips"></a>`_clips`[`L76`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L76), <a id="TpuPipelineChunkScheduler._cost"></a>`_cost`[`L65`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L65), <a id="TpuPipelineChunkScheduler._mamba_block_aligned_split"></a>`_mamba_block_aligned_split`[`L164`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L164), <a id="TpuPipelineChunkScheduler._mamba_split"></a>`_mamba_split`[`L68`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L68), <a id="TpuPipelineChunkScheduler._pp_size"></a>`_pp_size`[`L67`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L67), <a id="TpuPipelineChunkScheduler._seeded"></a>`_seeded`[`L75`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L75), <a id="TpuPipelineChunkScheduler._step_limit"></a>`_step_limit`[`L66`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L66), <a id="TpuPipelineChunkScheduler._step_pairs"></a>`_step_pairs`[`L71`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L71), <a id="TpuPipelineChunkScheduler._step_prefill_tokens"></a>`_step_prefill_tokens`[`L73`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L73), <a id="TpuPipelineChunkScheduler._step_schedule"></a>`_step_schedule`[`L74`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L74), <a id="TpuPipelineChunkScheduler._step_squares"></a>`_step_squares`[`L72`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L72), <a id="TpuPipelineChunkScheduler._step_tokens"></a>`_step_tokens`[`L70`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L70), <a id="TpuPipelineChunkScheduler._waits"></a>`_waits`[`L77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L77)
- uses (calls/refs, reference-scoped): [`chunk`](pp_chunks.md#StepCostModel.chunk), [`describe`](pp_chunks.md#StepCostModel.describe), [`step_ms`](pp_chunks.md#StepCostModel.step_ms), [`pairs`](pp_chunks.md#StepCostModel.pairs), [`logger`](pp_chunk_scheduler.md#logger), [`StepCostModel`](pp_chunks.md#StepCostModel), [`buckets`](pp_chunks.md#StepCostModel.buckets), [`granularity`](pp_chunks.md#StepCostModel.granularity), [`_prefill_end`](pp_chunk_scheduler.md#_prefill_end)
- used by: [`profile_and_install_cost_model`](pp_chunk_scheduler.md#profile_and_install_cost_model)

## Functions
- <a id="patch_engine_core_for_pp_chunks.__init__"></a>`__init__(self, *args, **kwargs)` — [`L254`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L254)
- <a id="_prefill_end"></a>`_prefill_end(request: Any)` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L58)
- <a id="patch_engine_core_for_pp_chunks"></a>`patch_engine_core_for_pp_chunks(vllm_config: Any)` — [`L242`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L242) — Have the engine core time the stages once its executor and scheduler — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
- <a id="profile_and_install_cost_model"></a>`profile_and_install_cost_model(scheduler: Any, executor: Any)` — [`L221`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L221) — Time every stage's forwards and hand the scheduler the model. — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
- <a id="uses_dynamic_chunks"></a>`uses_dynamic_chunks(vllm_config: Any)` — [`L48`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L48) — Whether this configuration sizes pipeline steps by time; the platform — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)

## Module values
- <a id="SCHEDULER_CLS"></a>`SCHEDULER_CLS` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L45)
- <a id="logger"></a>`logger` — [`L43`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunk_scheduler.py#L43)

