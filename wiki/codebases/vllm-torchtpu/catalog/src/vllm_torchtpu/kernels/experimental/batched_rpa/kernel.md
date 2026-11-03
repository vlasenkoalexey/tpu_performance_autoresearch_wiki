---
title: 'Module: src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.batched_rpa.kernel`/
symbols:
  rpa_body: rpa_body().
  fetch_compute_metadata: fetch_compute_metadata().
  create_allocs: create_allocs().
  fetch_stitch_metadata: fetch_stitch_metadata().
  get_kernel_name: get_kernel_name().
  get_scale_factors: get_scale_factors().
  rpa_kernel: rpa_kernel().
  rpa_body._kv_store_fence: rpa_body()._kv_store_fence().
  strided_load_bkv: strided_load_bkv().
  calculate_and_store_out: calculate_and_store_out().
  generate_mask: generate_mask().
  calculate_and_store_out._accum: calculate_and_store_out()._accum().
  _compute_valid_kv_mask: _compute_valid_kv_mask().
  rpa_kernel.ragged_paged_attention_pipeline._run: rpa_kernel().ragged_paged_attention_pipeline()._run().
  rpa_kernel.ragged_paged_attention_pipeline: rpa_kernel().ragged_paged_attention_pipeline().
  rpa_kernel.ragged_paged_attention_pipeline._run.execute_schedule_chunk: rpa_kernel().ragged_paged_attention_pipeline()._run().execute_schedule_chunk().
  calculate_and_store_out._stage_lse: calculate_and_store_out()._stage_lse().
  ComputeMetadata.local_k_start: ComputeMetadata#local_k_start.
  ComputeMetadata.local_k_end: ComputeMetadata#local_k_end.
  rpa_kernel.ragged_paged_attention_pipeline._run.loop_body: rpa_kernel().ragged_paged_attention_pipeline()._run().loop_body().
  ComputeMetadata: ComputeMetadata#
  get_kernel_metadata: get_kernel_metadata().
  rpa_kernel.ragged_paged_attention_pipeline._run.execute_schedule_chunk.compute_fn: rpa_kernel().ragged_paged_attention_pipeline()._run().execute_schedule_chunk().compute_fn().
  StitchMetadata: StitchMetadata#
  StitchMetadata.bkv_sz_frm_cache: StitchMetadata#bkv_sz_frm_cache.
  StitchMetadata.bkv_sz_frm_new: StitchMetadata#bkv_sz_frm_new.
  StitchMetadata.new_kv_len_start: StitchMetadata#new_kv_len_start.
  ComputeMetadata.causal_offset: ComputeMetadata#causal_offset.
---
# Module: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py)

## Classes
### <a id="ComputeMetadata"></a>`ComputeMetadata`
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py:231`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L231)
- doc: Scalars needed to build the QK mask, but not needed by the stitch.
- signature: `class ComputeMetadata:`
- members:
  - <a id="ComputeMetadata.causal_offset"></a>`causal_offset` — [`L234`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L234)
  - <a id="ComputeMetadata.local_k_end"></a>`local_k_end` — [`L236`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L236)
  - <a id="ComputeMetadata.local_k_start"></a>`local_k_start` — [`L235`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L235)
- used by: [`fetch_compute_metadata`](kernel.md#fetch_compute_metadata), [`generate_mask`](kernel.md#generate_mask), [`_compute_valid_kv_mask`](kernel.md#_compute_valid_kv_mask)

### <a id="StitchMetadata"></a>`StitchMetadata`
- def: [`src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py:221`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L221)
- doc: Scalars needed to merge newly arrived KV into the cached KV window.
- signature: `class StitchMetadata:`
- members:
  - <a id="StitchMetadata.bkv_sz_frm_cache"></a>`bkv_sz_frm_cache` — [`L224`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L224)
  - <a id="StitchMetadata.bkv_sz_frm_new"></a>`bkv_sz_frm_new` — [`L225`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L225)
  - <a id="StitchMetadata.new_kv_len_start"></a>`new_kv_len_start` — [`L226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L226)
- used by: [`fetch_stitch_metadata`](kernel.md#fetch_stitch_metadata), [`_kv_store_fence`](kernel.md#rpa_body._kv_store_fence), [`_compute_valid_kv_mask`](kernel.md#_compute_valid_kv_mask)

## Functions
- <a id="calculate_and_store_out._accum"></a>`_accum(b_idx: int | jax.Array, batch_acc: jax.Array, batch_l: jax.Array)` — [`L96`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L96)
- <a id="_compute_valid_kv_mask"></a>`_compute_valid_kv_mask(token: jax.Array, b_idx: int, stitch_meta: StitchMetadata, step_meta: ComputeMetadata)` — [`L239`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L239) — Builds a boolean mask for valid token slices before PV.
- <a id="rpa_body._kv_store_fence"></a>`_kv_store_fence()` — [`L467`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L467) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="rpa_kernel.ragged_paged_attention_pipeline._run"></a>`_run(final_allocs, schedule_ref, dma_sem, scratches)` — [`L913`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L913)
- <a id="calculate_and_store_out._stage_lse"></a>`_stage_lse(b_idx: int, batch_m: jax.Array, batch_l: jax.Array)` — [`L116`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L116)
- <a id="calculate_and_store_out"></a>`calculate_and_store_out(step_idx: jax.Array, schedule_ref: schedule.RpaSchedule, acc_list: jax.Array, l_list: jax.Array, m_list: jax.Array, o_vref: jax.Ref, lse_o_vref: jax.Ref | None, *, cfgs: configs.RpaConfigs)` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L85)
- <a id="rpa_kernel.ragged_paged_attention_pipeline._run.execute_schedule_chunk.compute_fn"></a>`compute_fn(step, slot, total_steps, out_slot, start_next_fetch, start_kv_writeback)` — [`L987`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L987)
- <a id="create_allocs"></a>`create_allocs(kv_cache_hbm_ref: jax.Ref, o_hbm_ref: jax.Ref, lse_hbm_ref: jax.Ref | None, cfgs: configs.RpaConfigs)` — [`L718`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L718) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="rpa_kernel.ragged_paged_attention_pipeline._run.execute_schedule_chunk"></a>`execute_schedule_chunk(start_step, num_steps)` — [`L946`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L946)
- <a id="fetch_compute_metadata"></a>`fetch_compute_metadata(step: jax.Array, schedule_ref: schedule.RpaSchedule, q_offsets_ref: jax.Ref, kv_cache_lens_ref: jax.Ref, *, cfgs: configs.RpaConfigs)` — [`L314`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L314) — Fetches the scalars consumed by the QK mask. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="fetch_stitch_metadata"></a>`fetch_stitch_metadata(step: jax.Array, schedule_ref: schedule.RpaSchedule, cu_q_lens_ref: jax.Ref, kv_cache_lens_ref: jax.Ref, kv_new_lens_ref: jax.Ref, *, cfgs: configs.RpaConfigs)` — [`L258`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L258) — Fetches the scalars consumed by the KV stitch.
- <a id="generate_mask"></a>`generate_mask(shape: tuple[int, int, int, int], *, bq_start: int, step_meta: ComputeMetadata, cfgs: configs.RpaConfigs)` — [`L371`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L371) — Generates causal, sliding window, and attention scope mask for QK computation.
- <a id="get_kernel_metadata"></a>`get_kernel_metadata(cfgs: configs.RpaConfigs)` — [`L808`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L808)
- <a id="get_kernel_name"></a>`get_kernel_name(cfgs: configs.RpaConfigs)` — [`L799`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L799)
- <a id="get_scale_factors"></a>`get_scale_factors(k: jax.Array, v: jax.Array, *, cfgs: configs.RpaConfigs)` — [`L152`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L152)
- <a id="rpa_kernel.ragged_paged_attention_pipeline._run.loop_body"></a>`loop_body(step_idx)` — [`L1026`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L1026)
- <a id="rpa_kernel.ragged_paged_attention_pipeline"></a>`ragged_paged_attention_pipeline(cu_q_lens_ref: jax.Ref, q_offsets_ref: jax.Ref, kv_cache_lens_ref: jax.Ref, kv_new_lens_ref: jax.Ref, schedule_hbm_ref: schedule.RpaSchedule, q_hbm_ref: jax.Ref, new_kv_hbm_ref: jax.Ref, kv_cache_hbm_ref: jax.Ref, lse_hbm_ref: jax.Ref | None, o_hbm_ref: jax.Ref, o_kv_cache_hbm_ref: jax.Ref, o_lse_hbm_ref: jax.Ref | None = None)` — [`L866`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L866)
- <a id="rpa_body"></a>`rpa_body(step: jax.Array, slot: int | jax.Array, q_vref: jax.Ref, kv_in_vref: jax.Ref, o_vref: jax.Ref, lse_o_vref: jax.Ref | None, schedule_ref: schedule.RpaSchedule, m_scratch_ref: jax.Ref, l_scratch_ref: jax.Ref, acc_scratch_ref: jax.Ref, *, cu_q_lens_ref: jax.Ref, q_offsets_ref: jax.Ref, kv_cache_lens_ref: jax.Ref, kv_new_lens_ref: jax.Ref, cfgs: configs.RpaConfigs, start_next_fetch: Callable[[], None], start_kv_writeback: Callable[[], None])` — [`L413`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L413) — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="rpa_kernel"></a>`rpa_kernel(cu_q_lens: jax.Array, q_offsets: jax.Array, kv_cache_lens: jax.Array, kv_new_lens: jax.Array, schedule_hbm: schedule.RpaSchedule, q_hbm: jax.Array, new_kv_hbm: jax.Array, kv_cache_hbm: jax.Array, lse_hbm: jax.Array | None, *, cfgs: configs.RpaConfigs, computer_cls: type[schedule.BaseMetadataComputer] = schedule.BaseMetadataComputer)` — [`L821`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L821) — Perform batched ragged paged attention with scheduler data. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)
- <a id="strided_load_bkv"></a>`strided_load_bkv(kv_in_vref: jax.Ref, b_idx: int, start: int, valid_mask: jax.Array | None = None, *, cfgs: configs.RpaConfigs)` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/batched_rpa/kernel.py#L36)

