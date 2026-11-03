---
title: 'Module: src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.ragged_paged_attention.v3.kernel_hd64`/
symbols:
  _ragged_paged_attention_kernel.debug_print: _ragged_paged_attention_kernel().debug_print().
  _ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv: _ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().
  ragged_paged_attention_hd64: ragged_paged_attention_hd64().
  ref_ragged_paged_attention_hd64: ref_ragged_paged_attention_hd64().
  _ragged_paged_attention_kernel._fetch_bkv: _ragged_paged_attention_kernel()._fetch_bkv().
  _ragged_paged_attention_kernel.process.compute_with_bq: _ragged_paged_attention_kernel().process().compute_with_bq().
  _ragged_paged_attention_kernel._update_kv_cache: _ragged_paged_attention_kernel()._update_kv_cache().
  _ragged_paged_attention_kernel: _ragged_paged_attention_kernel().
  static_validate_inputs: static_validate_inputs().
  prepare_inputs: prepare_inputs().
  dynamic_validate_inputs: dynamic_validate_inputs().
  _ragged_paged_attention_kernel.process: _ragged_paged_attention_kernel().process().
  get_vmem_estimate_bytes: get_vmem_estimate_bytes().
  _ragged_paged_attention_kernel.flash_attention_step2_pv: _ragged_paged_attention_kernel().flash_attention_step2_pv().
  _ragged_paged_attention_kernel._async_copy: _ragged_paged_attention_kernel()._async_copy().
  _ragged_paged_attention_kernel._fetch_bq: _ragged_paged_attention_kernel()._fetch_bq().
  _ragged_paged_attention_kernel._send_bo: _ragged_paged_attention_kernel()._send_bo().
  merge_kv: merge_kv().
  DEFAULT_MASK_VALUE: DEFAULT_MASK_VALUE.
  get_kv_cache_shape: get_kv_cache_shape().
  _ragged_paged_attention_kernel.flash_attention_step1_qk_softmax: _ragged_paged_attention_kernel().flash_attention_step1_qk_softmax().
  _ragged_paged_attention_kernel._fetch_bkv.loop_body: _ragged_paged_attention_kernel()._fetch_bkv().loop_body().
  _ragged_paged_attention_kernel._update_kv_cache.loop_body: _ragged_paged_attention_kernel()._update_kv_cache().loop_body().
  _ragged_paged_attention_kernel.broadcast_minor: _ragged_paged_attention_kernel().broadcast_minor().
  get_smem_estimate_bytes: get_smem_estimate_bytes().
  _ragged_paged_attention_kernel._fetch_bkv._fetch_bkv_from_new_kv: _ragged_paged_attention_kernel()._fetch_bkv()._fetch_bkv_from_new_kv().
  _ragged_paged_attention_kernel.prologue: _ragged_paged_attention_kernel().prologue().
  _ragged_paged_attention_kernel.epilogue: _ragged_paged_attention_kernel().epilogue().
  _ragged_paged_attention_kernel.start_fetch_bkv: _ragged_paged_attention_kernel().start_fetch_bkv().
  _ragged_paged_attention_kernel.start_fetch_bq: _ragged_paged_attention_kernel().start_fetch_bq().
  _ragged_paged_attention_kernel.wait_send_bo: _ragged_paged_attention_kernel().wait_send_bo().
  _ragged_paged_attention_kernel.wait_update_kv_cache: _ragged_paged_attention_kernel().wait_update_kv_cache().
  _ragged_paged_attention_kernel.wait_fetch_bkv: _ragged_paged_attention_kernel().wait_fetch_bkv().
  _ragged_paged_attention_kernel.wait_fetch_bq: _ragged_paged_attention_kernel().wait_fetch_bq().
  _ragged_paged_attention_kernel.start_send_bo: _ragged_paged_attention_kernel().start_send_bo().
  _ragged_paged_attention_kernel.start_update_kv_cache: _ragged_paged_attention_kernel().start_update_kv_cache().
  _ragged_paged_attention_kernel.strided_load: _ragged_paged_attention_kernel().strided_load().
  _ragged_paged_attention_kernel.strided_load_bkv: _ragged_paged_attention_kernel().strided_load_bkv().
  _ragged_paged_attention_kernel.process.compute_with_bq.prefetch_next_bq: _ragged_paged_attention_kernel().process().compute_with_bq().prefetch_next_bq().
  _ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.prefetch_next_bkv: _ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().prefetch_next_bkv().
  _ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.wait_cur_bq: _ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().wait_cur_bq().
  _ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.update_cur_bkv_to_cache: _ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().update_cur_bkv_to_cache().
  _ragged_paged_attention_kernel.process_decode: _ragged_paged_attention_kernel().process_decode().
  _ragged_paged_attention_kernel.process_prefill: _ragged_paged_attention_kernel().process_prefill().
  _ragged_paged_attention_kernel.process_mixed: _ragged_paged_attention_kernel().process_mixed().
  _ragged_paged_attention_kernel.flash_attention_step1_qk_softmax.load_with_init: _ragged_paged_attention_kernel().flash_attention_step1_qk_softmax().load_with_init().
  DEFAULT_VMEM_LIMIT_BYTES: DEFAULT_VMEM_LIMIT_BYTES.
  _ragged_paged_attention_kernel.get_next_bkv_idx_start: _ragged_paged_attention_kernel().get_next_bkv_idx_start().
  _ragged_paged_attention_kernel.flash_attention_step2_pv.load_with_init: _ragged_paged_attention_kernel().flash_attention_step2_pv().load_with_init().
  _ragged_paged_attention_kernel.load_bq: _ragged_paged_attention_kernel().load_bq().
  _ragged_paged_attention_kernel.process.get_next_bq_ids: _ragged_paged_attention_kernel().process().get_next_bq_ids().
  _ragged_paged_attention_kernel.process.get_next_bkv_ids: _ragged_paged_attention_kernel().process().get_next_bkv_ids().
  prepare_outputs: prepare_outputs().
---
# Module: [`src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py)

## Functions
- <a id="_ragged_paged_attention_kernel._async_copy"></a>`_async_copy(src, dst, sem, wait)` — [`L495`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L495)
- <a id="_ragged_paged_attention_kernel._fetch_bkv"></a>`_fetch_bkv(seq_idx, bkv_idx, bkv_sem_idx, *, wait=False)` — [`L505`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L505) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel._fetch_bkv._fetch_bkv_from_new_kv"></a>`_fetch_bkv_from_new_kv()` — [`L579`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L579)
- <a id="_ragged_paged_attention_kernel._fetch_bq"></a>`_fetch_bq(seq_idx, bq_idx, bq_sem_idx, *, wait=False)` — [`L669`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L669)
- <a id="_ragged_paged_attention_kernel"></a>`_ragged_paged_attention_kernel(kv_lens_ref, page_indices_ref, cu_q_lens_ref, distribution_ref, sem_ids_ref, bo_ids_ref, bkv_update_ids_ref, q_hbm_ref, kv_hbm_ref, kv_cache_hbm_ref, attention_sink_ref, o_hbm_ref, updated_kv_cache_hbm_ref, bkv_x2_ref, bq_x2_ref, bo_x2_ref, sems, l_ref, m_ref, acc_ref, *, sm_scale: float, sliding_window: int | None = None, strict_sliding_window: bool = True, soft_cap: float | None = None, mask_value: float = DEFAULT_MASK_VALUE, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, skip_kv_update: bool = False, chunk_prefill_size: int | None = None, bkv_p, bq_sz, use_causal_mask: bool = True, debug_mode: bool = False)` — [`L264`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L264)
- <a id="_ragged_paged_attention_kernel._send_bo"></a>`_send_bo(seq_idx, bo_idx, bo_sem_idx, *, wait=False)` — [`L693`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L693)
- <a id="_ragged_paged_attention_kernel._update_kv_cache"></a>`_update_kv_cache(seq_idx, bkv_sem_idx, offset, update_sz, *, wait=False)` — [`L602`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L602)
- <a id="_ragged_paged_attention_kernel.broadcast_minor"></a>`broadcast_minor(src, shape)` — [`L797`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L797)
- <a id="_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv"></a>`compute_with_bkv(bkv_idx, _)` — [`L858`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L858)
- <a id="_ragged_paged_attention_kernel.process.compute_with_bq"></a>`compute_with_bq(bq_idx, _)` — [`L846`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L846)
- <a id="_ragged_paged_attention_kernel.debug_print"></a>`debug_print(msg, *args)` — [`L378`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L378)
- <a id="dynamic_validate_inputs"></a>`dynamic_validate_inputs(queries: jax.Array, keys: jax.Array, values: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, attention_sink: jax.Array | None = None, *, sm_scale: float = 1, sliding_window: int | None = None, soft_cap: float | None = None, mask_value: float | None = DEFAULT_MASK_VALUE, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, chunk_prefill_size: int | None = None, num_kv_pages_per_block: int | None = None, num_queries_per_block: int | None = None, vmem_limit_bytes: int | None = None, debug_mode: bool = False)` — [`L1121`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L1121)
- <a id="_ragged_paged_attention_kernel.epilogue"></a>`epilogue()` — [`L1010`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L1010)
- <a id="_ragged_paged_attention_kernel.flash_attention_step1_qk_softmax"></a>`flash_attention_step1_qk_softmax(q, kv, *, bq_idx, bkv_idx, kv_head_idx)` — [`L397`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L397)
- <a id="_ragged_paged_attention_kernel.flash_attention_step2_pv"></a>`flash_attention_step2_pv(q_shape_0, kv, p, exp_m_diff, *, bkv_idx, kv_head_idx)` — [`L471`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L471)
- <a id="get_kv_cache_shape"></a>`get_kv_cache_shape(total_num_pages, page_size, actual_num_kv_heads, actual_head_dim, kv_dtype)` — [`L246`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L246) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel.process.get_next_bkv_ids"></a>`get_next_bkv_ids(seq_idx, bq_idx, bkv_idx, bkv_sem_idx)` — [`L825`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L825)
- <a id="_ragged_paged_attention_kernel.get_next_bkv_idx_start"></a>`get_next_bkv_idx_start()` — [`L369`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L369)
- <a id="_ragged_paged_attention_kernel.process.get_next_bq_ids"></a>`get_next_bq_ids(seq_idx, bq_idx, bq_sem_idx)` — [`L817`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L817)
- <a id="get_smem_estimate_bytes"></a>`get_smem_estimate_bytes(max_num_seqs, pages_per_seq)` — [`L186`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L186)
- <a id="get_vmem_estimate_bytes"></a>`get_vmem_estimate_bytes(actual_num_kv_heads, actual_num_q_heads_per_kv_head, actual_head_dim, bq_sz, bkv_sz, q_dtype, kv_dtype)` — [`L212`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L212)
- <a id="_ragged_paged_attention_kernel.load_bq"></a>`load_bq(bq_sem_idx, kv_head_idx, *, actual_bq_sz=bq_sz)` — [`L758`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L758)
- <a id="_ragged_paged_attention_kernel.flash_attention_step1_qk_softmax.load_with_init"></a>`load_with_init(ref, init_val)` — [`L412`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L412)
- <a id="_ragged_paged_attention_kernel.flash_attention_step2_pv.load_with_init"></a>`load_with_init(ref, init_val)` — [`L482`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L482)
- <a id="_ragged_paged_attention_kernel._fetch_bkv.loop_body"></a>`loop_body(i, offset)` — [`L556`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L556)
- <a id="_ragged_paged_attention_kernel._update_kv_cache.loop_body"></a>`loop_body(i, states)` — [`L634`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L634)
- <a id="merge_kv"></a>`merge_kv(k: jax.Array, v: jax.Array)` — [`L1018`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L1018) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.prefetch_next_bkv"></a>`prefetch_next_bkv()` — [`L873`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L873)
- <a id="_ragged_paged_attention_kernel.process.compute_with_bq.prefetch_next_bq"></a>`prefetch_next_bq()` — [`L854`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L854)
- <a id="prepare_inputs"></a>`prepare_inputs(q: jax.Array, k: jax.Array, v: jax.Array, attention_sink: jax.Array | None = None)` — [`L1044`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L1044)
- <a id="prepare_outputs"></a>`prepare_outputs(out, actual_num_q_heads_per_kv_head: int, actual_head_dim: int)` — [`L1093`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L1093)
- <a id="_ragged_paged_attention_kernel.process"></a>`process(static_q_len=None)` — [`L808`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L808)
- <a id="_ragged_paged_attention_kernel.process_decode"></a>`process_decode()` — [`L998`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L998)
- <a id="_ragged_paged_attention_kernel.process_mixed"></a>`process_mixed()` — [`L1006`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L1006)
- <a id="_ragged_paged_attention_kernel.process_prefill"></a>`process_prefill()` — [`L1002`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L1002)
- <a id="_ragged_paged_attention_kernel.prologue"></a>`prologue()` — [`L993`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L993)
- <a id="ragged_paged_attention_hd64"></a>`ragged_paged_attention_hd64(queries: jax.Array, keys: jax.Array, values: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, attention_sink: jax.Array | None = None, *, sm_scale: float = 1, sliding_window: int | None = None, strict_sliding_window: bool = True, soft_cap: float | None = None, mask_value: float = DEFAULT_MASK_VALUE, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, chunk_prefill_size: int | None = None, num_kv_pages_per_block: int | None = None, num_queries_per_block: int | None = None, vmem_limit_bytes: int | None = None, debug_mode: bool = False, skip_kv_update: bool = False, use_causal_mask: bool = True)` — [`L1377`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L1377) — A variant of ragged paged attention for head_dim=64. — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="ref_ragged_paged_attention_hd64"></a>`ref_ragged_paged_attention_hd64(queries: jax.Array, keys: jax.Array, values: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, attention_sink: jax.Array | None = None, *, sm_scale: float = 1, sliding_window: int | None = None, soft_cap: float | None = None, mask_value: float | None = DEFAULT_MASK_VALUE, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, skip_kv_update: bool = False, use_causal_mask: bool = True)` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L43) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel.start_fetch_bkv"></a>`start_fetch_bkv(seq_idx, bkv_idx, bkv_sem_idx)` — [`L717`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L717)
- <a id="_ragged_paged_attention_kernel.start_fetch_bq"></a>`start_fetch_bq(seq_idx, bq_idx, bq_sem_idx)` — [`L723`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L723)
- <a id="_ragged_paged_attention_kernel.start_send_bo"></a>`start_send_bo(seq_idx, bo_idx, bo_sem_idx)` — [`L729`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L729)
- <a id="_ragged_paged_attention_kernel.start_update_kv_cache"></a>`start_update_kv_cache(seq_idx, bkv_sem_idx, offset, update_sz)` — [`L742`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L742)
- <a id="static_validate_inputs"></a>`static_validate_inputs(queries: jax.Array, keys: jax.Array, values: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, attention_sink: jax.Array | None = None, *, sm_scale: float = 1, sliding_window: int | None = None, soft_cap: float | None = None, mask_value: float | None = DEFAULT_MASK_VALUE, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, chunk_prefill_size: int | None = None, num_kv_pages_per_block: int | None = None, num_queries_per_block: int | None = None, vmem_limit_bytes: int | None = None, debug_mode: bool = False)` — [`L1211`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L1211) — Validate inputs to the RPA kernel statically.
- <a id="_ragged_paged_attention_kernel.strided_load"></a>`strided_load(ref, start, step)` — [`L768`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L768)
- <a id="_ragged_paged_attention_kernel.strided_load_bkv"></a>`strided_load_bkv(bkv_sem_idx, start, step, *, bkv_mask)` — [`L776`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L776)
- <a id="_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.update_cur_bkv_to_cache"></a>`update_cur_bkv_to_cache()` — [`L888`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L888)
- <a id="_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.wait_cur_bq"></a>`wait_cur_bq()` — [`L879`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L879)
- <a id="_ragged_paged_attention_kernel.wait_fetch_bkv"></a>`wait_fetch_bkv(seq_idx, bkv_idx, bkv_sem_idx)` — [`L720`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L720)
- <a id="_ragged_paged_attention_kernel.wait_fetch_bq"></a>`wait_fetch_bq(seq_idx, bq_idx, bq_sem_idx)` — [`L726`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L726)
- <a id="_ragged_paged_attention_kernel.wait_send_bo"></a>`wait_send_bo(bo_sem_idx)` — [`L734`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L734)
- <a id="_ragged_paged_attention_kernel.wait_update_kv_cache"></a>`wait_update_kv_cache(bkv_sem_idx)` — [`L748`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L748)

## Module values
- <a id="DEFAULT_MASK_VALUE"></a>`DEFAULT_MASK_VALUE` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L36) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="DEFAULT_VMEM_LIMIT_BYTES"></a>`DEFAULT_VMEM_LIMIT_BYTES` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel_hd64.py#L38)

