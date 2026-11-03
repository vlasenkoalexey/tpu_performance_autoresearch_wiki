---
title: 'Module: src/vllm_torchtpu/core/pp_chunks.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/core/pp_chunks.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.core.pp_chunks`/
symbols:
  StepCostModel.chunk: StepCostModel#chunk().
  StepCostModel.describe: StepCostModel#describe().
  StepCostModel.step_ms: StepCostModel#step_ms().
  profile_points: profile_points().
  StepCostModel.pairs: StepCostModel#pairs().
  StepCostModel: StepCostModel#
  StepCostModel.buckets: StepCostModel#buckets.
  StepCostModel.granularity: StepCostModel#granularity.
  StepCostModel.schedule: StepCostModel#schedule.
  chunk_granularity: chunk_granularity().
  chunk_buckets: chunk_buckets().
  chunk_pairs: chunk_pairs().
  StepCostModel.fit: StepCostModel#fit().
  StepCostModel.attn_ms_per_token_pair: StepCostModel#attn_ms_per_token_pair.
  logger: logger.
  schedule_pairs: schedule_pairs().
  StepCostModel.linear_ms: StepCostModel#linear_ms.
  StepCostModel.target_ms: StepCostModel#target_ms.
  _PREFIX_PROFILE_MIN_DIVISOR: _PREFIX_PROFILE_MIN_DIVISOR.
---
# Module: [`src/vllm_torchtpu/core/pp_chunks.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py)

## Classes
### <a id="StepCostModel"></a>`StepCostModel`
- def: [`src/vllm_torchtpu/core/pp_chunks.py:140`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L140)
- doc: Per-stage step time in ms as a function of the step's shape.
- signature: `class StepCostModel:`
- members:
  - <a id="StepCostModel.chunk"></a>`chunk(self, prefix: int, remaining: int, step_tokens: int, step_pairs: float, step_squares: float, step_limit: int | None = None, step_schedule: int = 0)` — [`L219`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L219) — Largest chunk of a request with ``prefix`` computed tokens and — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="StepCostModel.describe"></a>`describe(self)` — [`L272`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L272) — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
  - <a id="StepCostModel.fit"></a>`fit(cls, stage_samples: list[list[tuple[int, int, float]]], slack: float, granularity: int, schedule: tuple[int, int, int] | None = None)` — [`L152`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L152) — ``stage_samples`` holds one list of (tokens, prefix, ms) per
  - <a id="StepCostModel.pairs"></a>`pairs(self, chunk: int, prefix: int)` — [`L206`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L206) — (query block, KV block) pairs the attention kernel schedules for
  - <a id="StepCostModel.step_ms"></a>`step_ms(self, padded_tokens: int, token_pairs: float, token_squares: float)` — [`L212`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L212)
  - <a id="StepCostModel.attn_ms_per_token_pair"></a>`attn_ms_per_token_pair` — [`L145`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L145)
  - <a id="StepCostModel.buckets"></a>`buckets` — [`L143`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L143)
  - <a id="StepCostModel.granularity"></a>`granularity` — [`L147`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L147)
  - <a id="StepCostModel.linear_ms"></a>`linear_ms` — [`L144`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L144)
  - <a id="StepCostModel.schedule"></a>`schedule` — [`L149`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L149)
  - <a id="StepCostModel.target_ms"></a>`target_ms` — [`L146`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L146)
- uses (calls/refs, reference-scoped): [`chunk_pairs`](pp_chunks.md#chunk_pairs)
- used by: [`_mamba_block_aligned_split`](pp_chunk_scheduler.md#TpuPipelineChunkScheduler._mamba_block_aligned_split), [`_pending_step_limit`](pp_chunk_scheduler.md#TpuPipelineChunkScheduler._pending_step_limit), [`_cost`](pp_chunk_scheduler.md#TpuPipelineChunkScheduler._cost), [`install_cost_model`](pp_chunk_scheduler.md#TpuPipelineChunkScheduler.install_cost_model), [`profile_and_install_cost_model`](pp_chunk_scheduler.md#profile_and_install_cost_model), [`step_estimate_ms`](pp_chunk_scheduler.md#TpuPipelineChunkScheduler.step_estimate_ms)

## Functions
- <a id="chunk_buckets"></a>`chunk_buckets(max_tokens: int, granularity: int)` — [`L72`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L72) — Token buckets at every granule multiple below ``max_tokens``. — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
- <a id="chunk_granularity"></a>`chunk_granularity(block_size: int, max_tokens: int, block_aligned: bool)` — [`L61`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L61) — Token multiple that prefill chunks are cut at: an eighth of a step, — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
- <a id="chunk_pairs"></a>`chunk_pairs(schedule: tuple[int, int, int] | None, chunk: int, prefix: int)` — [`L77`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L77) — (query block, KV block) pairs the attention kernel schedules for a
- <a id="profile_points"></a>`profile_points(buckets: list[int], max_tokens: int, max_model_len: int, schedule: tuple[int, int, int] | None = None)` — [`L110`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L110) — (tokens, prefix) pairs to time as one request: every bucket without a — documented in [tpu-schedulers](../../../../concepts/tpu-schedulers.md)
- <a id="schedule_pairs"></a>`schedule_pairs(q_lens, kv_lens, bq: int, bkv: int)` — [`L91`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L91) — (query block, KV block) pairs the attention kernel schedules for

## Module values
- <a id="_PREFIX_PROFILE_MIN_DIVISOR"></a>`_PREFIX_PROFILE_MIN_DIVISOR` — [`L58`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L58)
- <a id="logger"></a>`logger` — [`L55`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/core/pp_chunks.py#L55)

