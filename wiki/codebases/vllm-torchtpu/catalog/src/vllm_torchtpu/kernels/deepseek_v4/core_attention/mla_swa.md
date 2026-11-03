---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.core_attention.mla_swa`/
symbols:
  mla_sliding_window_ragged_paged_attention: mla_sliding_window_ragged_paged_attention().
  _mla_sliding_window_ragged_paged_attention_kernel.process.compute_with_bq: _mla_sliding_window_ragged_paged_attention_kernel().process().compute_with_bq().
  _mla_batched_decode_kernel: _mla_batched_decode_kernel().
  _mla_batched_decode_kernel.loop_body: _mla_batched_decode_kernel().loop_body().
  mla_sliding_window_ragged_paged_attention.run_mla_kernel: mla_sliding_window_ragged_paged_attention().run_mla_kernel().
  _mla_sliding_window_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv: _mla_sliding_window_ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().
  MlaCase.symbol: MlaCase#symbol().
  _mla_sliding_window_ragged_paged_attention_kernel: _mla_sliding_window_ragged_paged_attention_kernel().
  run_mla_batched_decode_kernel: run_mla_batched_decode_kernel().
  _mla_sliding_window_ragged_paged_attention_kernel._update_kv_cache: _mla_sliding_window_ragged_paged_attention_kernel()._update_kv_cache().
  _mla_sliding_window_ragged_paged_attention_kernel.wait_send_bo: _mla_sliding_window_ragged_paged_attention_kernel().wait_send_bo().
  _mla_batched_decode_kernel._fetch_bkv: _mla_batched_decode_kernel()._fetch_bkv().
  _mla_sliding_window_ragged_paged_attention_kernel._async_copy: _mla_sliding_window_ragged_paged_attention_kernel()._async_copy().
  _mla_sliding_window_ragged_paged_attention_kernel.start_send_bo: _mla_sliding_window_ragged_paged_attention_kernel().start_send_bo().
  cdiv: cdiv().
  MlaCase: MlaCase#
  _mla_sliding_window_ragged_paged_attention_kernel._start_offset: _mla_sliding_window_ragged_paged_attention_kernel()._start_offset().
  align_to: align_to().
  _mla_sliding_window_ragged_paged_attention_kernel.prologue: _mla_sliding_window_ragged_paged_attention_kernel().prologue().
  _mla_sliding_window_ragged_paged_attention_kernel._fetch_bkv: _mla_sliding_window_ragged_paged_attention_kernel()._fetch_bkv().
  _mla_batched_decode_kernel.async_copy: _mla_batched_decode_kernel().async_copy().
  _mla_batched_decode_kernel._update_kv_cache: _mla_batched_decode_kernel()._update_kv_cache().
  _mla_batched_decode_kernel.fetch_batch: _mla_batched_decode_kernel().fetch_batch().
  _mla_sliding_window_ragged_paged_attention_kernel.process: _mla_sliding_window_ragged_paged_attention_kernel().process().
  prepare_q_inputs: prepare_q_inputs().
  _mla_batched_decode_kernel.wait_fetch: _mla_batched_decode_kernel().wait_fetch().
  _mla_batched_decode_kernel.wait_update_kv_cache: _mla_batched_decode_kernel().wait_update_kv_cache().
  _mla_batched_decode_kernel.wait_send_bo: _mla_batched_decode_kernel().wait_send_bo().
  get_dtype_bitwidth: get_dtype_bitwidth().
  _mla_sliding_window_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.prefetch_next_bkv: _mla_sliding_window_ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().prefetch_next_bkv().
  _mla_sliding_window_ragged_paged_attention_kernel.epilogue: _mla_sliding_window_ragged_paged_attention_kernel().epilogue().
  _mla_sliding_window_ragged_paged_attention_kernel._fetch_bq: _mla_sliding_window_ragged_paged_attention_kernel()._fetch_bq().
  _mla_sliding_window_ragged_paged_attention_kernel._send_bo: _mla_sliding_window_ragged_paged_attention_kernel()._send_bo().
  _mla_sliding_window_ragged_paged_attention_kernel._send_l: _mla_sliding_window_ragged_paged_attention_kernel()._send_l().
  _mla_sliding_window_ragged_paged_attention_kernel._send_m: _mla_sliding_window_ragged_paged_attention_kernel()._send_m().
  _mla_sliding_window_ragged_paged_attention_kernel.start_fetch_bkv: _mla_sliding_window_ragged_paged_attention_kernel().start_fetch_bkv().
  _mla_sliding_window_ragged_paged_attention_kernel.start_fetch_bq: _mla_sliding_window_ragged_paged_attention_kernel().start_fetch_bq().
  _mla_sliding_window_ragged_paged_attention_kernel.wait_update_kv_cache: _mla_sliding_window_ragged_paged_attention_kernel().wait_update_kv_cache().
  _mla_batched_decode_kernel._fetch_bq: _mla_batched_decode_kernel()._fetch_bq().
  _mla_batched_decode_kernel._send_bo: _mla_batched_decode_kernel()._send_bo().
  narrow_page_indices: narrow_page_indices().
  get_dtype_packing: get_dtype_packing().
  _mla_sliding_window_ragged_paged_attention_kernel.flash_attention: _mla_sliding_window_ragged_paged_attention_kernel().flash_attention().
  _mla_sliding_window_ragged_paged_attention_kernel._update_kv_cache.loop_body: _mla_sliding_window_ragged_paged_attention_kernel()._update_kv_cache().loop_body().
  _mla_sliding_window_ragged_paged_attention_kernel.wait_fetch_bkv: _mla_sliding_window_ragged_paged_attention_kernel().wait_fetch_bkv().
  _mla_sliding_window_ragged_paged_attention_kernel.wait_fetch_bq: _mla_sliding_window_ragged_paged_attention_kernel().wait_fetch_bq().
  _mla_sliding_window_ragged_paged_attention_kernel.start_update_kv_cache: _mla_sliding_window_ragged_paged_attention_kernel().start_update_kv_cache().
  get_physical_layout: get_physical_layout().
  MlaCase.MIXED: MlaCase#MIXED.
  _mla_sliding_window_ragged_paged_attention_kernel.flash_attention.load_with_init: _mla_sliding_window_ragged_paged_attention_kernel().flash_attention().load_with_init().
  _mla_sliding_window_ragged_paged_attention_kernel.process.compute_with_bq.prefetch_next_bq: _mla_sliding_window_ragged_paged_attention_kernel().process().compute_with_bq().prefetch_next_bq().
  _mla_sliding_window_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.update_cur_bkv_to_cache: _mla_sliding_window_ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().update_cur_bkv_to_cache().
  MlaCase.DECODE: MlaCase#DECODE.
  MlaCase.PREFILL: MlaCase#PREFILL.
  _mla_batched_decode_kernel.get_bkv_sz_frm_cache: _mla_batched_decode_kernel().get_bkv_sz_frm_cache().
  DEFAULT_VMEM_LIMIT_BYTES: DEFAULT_VMEM_LIMIT_BYTES.
  _mla_sliding_window_ragged_paged_attention_kernel._get_kv_len: _mla_sliding_window_ragged_paged_attention_kernel()._get_kv_len().
  _mla_sliding_window_ragged_paged_attention_kernel._get_q_len: _mla_sliding_window_ragged_paged_attention_kernel()._get_q_len().
  _mla_sliding_window_ragged_paged_attention_kernel.load_bq: _mla_sliding_window_ragged_paged_attention_kernel().load_bq().
  _mla_sliding_window_ragged_paged_attention_kernel.load_bkv: _mla_sliding_window_ragged_paged_attention_kernel().load_bkv().
  _mla_sliding_window_ragged_paged_attention_kernel.process.get_next_bq_ids: _mla_sliding_window_ragged_paged_attention_kernel().process().get_next_bq_ids().
  _mla_sliding_window_ragged_paged_attention_kernel.process.compute_with_bq.get_next_bkv_ids: _mla_sliding_window_ragged_paged_attention_kernel().process().compute_with_bq().get_next_bkv_ids().
  prepare_kv_inputs: prepare_kv_inputs().
  prepare_outputs: prepare_outputs().
  _mla_batched_decode_kernel.compute_batch: _mla_batched_decode_kernel().compute_batch().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py)

## Classes
### <a id="MlaCase"></a>`MlaCase`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py:94`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L94)
- doc: Represents the different cases for MLA.
- signature: `class MlaCase(Enum):`
- members:
  - <a id="MlaCase.symbol"></a>`symbol(self)` — [`L107`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L107)
  - <a id="MlaCase.DECODE"></a>`DECODE` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L102)
  - <a id="MlaCase.MIXED"></a>`MIXED` — [`L104`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L104)
  - <a id="MlaCase.PREFILL"></a>`PREFILL` — [`L103`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L103)
- used by: [`mla_sliding_window_ragged_paged_attention`](mla_swa.md#mla_sliding_window_ragged_paged_attention), [`run_mla_kernel`](mla_swa.md#mla_sliding_window_ragged_paged_attention.run_mla_kernel)

## Functions
- <a id="_mla_sliding_window_ragged_paged_attention_kernel._async_copy"></a>`_async_copy(src, dst, sem, wait)` — [`L302`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L302)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel._fetch_bkv"></a>`_fetch_bkv(seq_idx, bkv_idx, bkv_sem_idx, start_offset, *, wait=False)` — [`L334`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L334)
- <a id="_mla_batched_decode_kernel._fetch_bkv"></a>`_fetch_bkv(batch_idx, sem_idx, wait=False)` — [`L1009`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L1009)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel._fetch_bq"></a>`_fetch_bq(seq_idx, bq_idx, bq_sem_idx, *, wait=False)` — [`L507`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L507)
- <a id="_mla_batched_decode_kernel._fetch_bq"></a>`_fetch_bq(batch_idx, sem_idx, wait=False)` — [`L993`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L993)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel._get_kv_len"></a>`_get_kv_len(seq_idx)` — [`L309`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L309)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel._get_q_len"></a>`_get_q_len(seq_idx)` — [`L312`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L312)
- <a id="_mla_batched_decode_kernel"></a>`_mla_batched_decode_kernel(kv_lens_ref, page_indices_ref, cu_q_lens_ref, start_end_seq_idx_ref, attention_sinks_ref, q_hbm_ref, new_kv_hbm_ref, cache_kv_hbm_ref, in_output_hbm_ref, in_l_hbm_ref, in_m_hbm_ref, o_hbm_ref, updated_cache_kv_hbm_ref, l_hbm_ref, m_hbm_ref, bkv_batch_x2_vmem, q_batch_x2_vmem, o_batch_x2_vmem, l_batch_x2_vmem, m_batch_x2_vmem, sems, *, sm_scale: float, sliding_window: int, logical_page_size: int, unnormalized_output: bool, bkv_p: int, seq_batch_sz: int)` — [`L905`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L905)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel"></a>`_mla_sliding_window_ragged_paged_attention_kernel(kv_lens_ref, page_indices_ref, cu_q_lens_ref, start_end_seq_idx_ref, sem_ids_ref, bo_ids_ref, bkv_update_ids_ref, attention_sinks_ref, q_hbm_ref, new_kv_hbm_ref, cache_kv_hbm_ref, in_output_hbm_ref, in_l_hbm_ref, in_m_hbm_ref, o_hbm_ref, updated_cache_kv_hbm_ref, l_hbm_ref, m_hbm_ref, bkv_x2_ref, bq_x2_ref, bo_x2_ref, bl_x2_ref, bm_x2_ref, sems, l_ref, m_ref, acc_ref, *, static_q_len: int | None, sm_scale: float, sliding_window: int, logical_page_size: int, unnormalized_output: bool, non_causal_block: bool, q_compute_block_size: int | None, bkv_p, bq_sz)` — [`L115`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L115)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel._send_bo"></a>`_send_bo(seq_idx, bo_idx, bo_sem_idx, *, wait=False)` — [`L522`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L522)
- <a id="_mla_batched_decode_kernel._send_bo"></a>`_send_bo(batch_idx, sem_idx, wait=False)` — [`L1155`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L1155)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel._send_l"></a>`_send_l(seq_idx, bo_idx, bo_sem_idx, *, wait=False)` — [`L536`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L536)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel._send_m"></a>`_send_m(seq_idx, bo_idx, bo_sem_idx, *, wait=False)` — [`L550`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L550)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel._start_offset"></a>`_start_offset(seq_idx, bq_idx)` — [`L319`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L319)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel._update_kv_cache"></a>`_update_kv_cache(seq_idx, bkv_sem_idx, offset, update_sz, *, in_vmem_start=0, wait=False)` — [`L437`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L437)
- <a id="_mla_batched_decode_kernel._update_kv_cache"></a>`_update_kv_cache(batch_idx, sem_idx, wait=False)` — [`L1183`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L1183)
- <a id="align_to"></a>`align_to(x, a)` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L35)
- <a id="_mla_batched_decode_kernel.async_copy"></a>`async_copy(src, dst, sem, wait=False)` — [`L944`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L944)
- <a id="cdiv"></a>`cdiv(a, b)` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L30)
- <a id="_mla_batched_decode_kernel.compute_batch"></a>`compute_batch(batch_idx, sem_idx)` — [`L1076`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L1076)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv"></a>`compute_with_bkv(bkv_idx, _)` — [`L688`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L688)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.process.compute_with_bq"></a>`compute_with_bq(bq_idx, _)` — [`L639`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L639)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.epilogue"></a>`epilogue()` — [`L825`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L825)
- <a id="_mla_batched_decode_kernel.fetch_batch"></a>`fetch_batch(batch_idx, sem_idx)` — [`L1224`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L1224)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.flash_attention"></a>`flash_attention(q, kv, *, bq_idx, bkv_idx, start_offset)` — [`L204`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L204)
- <a id="_mla_batched_decode_kernel.get_bkv_sz_frm_cache"></a>`get_bkv_sz_frm_cache(kv_len)` — [`L987`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L987)
- <a id="get_dtype_bitwidth"></a>`get_dtype_bitwidth(dtype)` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L85)
- <a id="get_dtype_packing"></a>`get_dtype_packing(dtype)` — [`L89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L89)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.process.compute_with_bq.get_next_bkv_ids"></a>`get_next_bkv_ids(seq_idx, bq_idx, bkv_idx, bkv_sem_idx)` — [`L665`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L665)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.process.get_next_bq_ids"></a>`get_next_bq_ids(seq_idx, bq_idx, bq_sem_idx)` — [`L631`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L631)
- <a id="get_physical_layout"></a>`get_physical_layout(cache_kv_shape, q_dtype, head_dim, max_num_seqs, num_page_indices)` — [`L883`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L883)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.load_bkv"></a>`load_bkv(bkv_sem_idx, bkv_idx, start_offset)` — [`L614`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L614)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.load_bq"></a>`load_bq(bq_sem_idx)` — [`L611`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L611)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.flash_attention.load_with_init"></a>`load_with_init(ref, init_val)` — [`L226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L226)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel._update_kv_cache.loop_body"></a>`loop_body(i, states)` — [`L467`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L467)
- <a id="_mla_batched_decode_kernel.loop_body"></a>`loop_body(i, _)` — [`L1248`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L1248)
- <a id="mla_sliding_window_ragged_paged_attention"></a>`mla_sliding_window_ragged_paged_attention(q: jax.Array, new_kv: jax.Array, cache_kv: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, attention_sinks: jax.Array, *, sm_scale: float = 1, sliding_window: int, logical_page_size: int, chunk_prefill_size: int | None = None, num_kv_pages_per_block: tuple[int, int, int] | int | None = None, num_queries_per_block: tuple[int, int, int] | int | None = None, q_compute_block_size: int | None = None, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES, unnormalized_output: bool = False, non_causal_block: bool = False, decode_seq_batch_size: int = 32)` — [`L1462`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L1462) — MLA Ragged paged attention that supports mixed prefill and decode. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
- <a id="narrow_page_indices"></a>`narrow_page_indices(kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, *, sliding_window: int, logical_page_size: int, max_q_len: int, max_kv_pages_per_block: int)` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L39) — Keep only the pages each sequence's sliding window can touch.
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.prefetch_next_bkv"></a>`prefetch_next_bkv()` — [`L697`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L697)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.process.compute_with_bq.prefetch_next_bq"></a>`prefetch_next_bq()` — [`L684`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L684)
- <a id="prepare_kv_inputs"></a>`prepare_kv_inputs(kv: jax.Array)` — [`L852`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L852) — Reinterprets bf16 new KV as one raw uint8 byte row per token.
- <a id="prepare_outputs"></a>`prepare_outputs(out, actual_num_q_heads: int, actual_head_dim: int)` — [`L875`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L875)
- <a id="prepare_q_inputs"></a>`prepare_q_inputs(q: jax.Array)` — [`L833`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L833)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.process"></a>`process()` — [`L625`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L625)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.prologue"></a>`prologue()` — [`L811`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L811)
- <a id="run_mla_batched_decode_kernel"></a>`run_mla_batched_decode_kernel(q: jax.Array, new_kv: jax.Array, cache_kv: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, num_kv_pages_per_block: int, num_queries_per_block: int, start_seq_idx: jax.Array, end_seq_idx: jax.Array, in_output: jax.Array, in_l: jax.Array, in_m: jax.Array, attention_sinks: jax.Array, *, sm_scale: float, sliding_window: int, logical_page_size: int, vmem_limit_bytes: int, unnormalized_output: bool, seq_batch_sz: int = 32)` — [`L1287`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L1287)
- <a id="mla_sliding_window_ragged_paged_attention.run_mla_kernel"></a>`run_mla_kernel(q: jax.Array, new_kv: jax.Array, cache_kv: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, start_seq_idx: jax.Array, end_seq_idx: jax.Array, in_output: jax.Array, in_l: jax.Array, in_m: jax.Array, attention_sinks: jax.Array, static_q_len: int | None, unnormalized_output: bool, num_kv_pages_per_block: int, num_queries_per_block: int, case: MlaCase = MlaCase.MIXED)` — [`L1594`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L1594)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.start_fetch_bkv"></a>`start_fetch_bkv(seq_idx, bkv_idx, bkv_sem_idx, start_offset)` — [`L564`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L564)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.start_fetch_bq"></a>`start_fetch_bq(seq_idx, bq_idx, bq_sem_idx)` — [`L570`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L570)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.start_send_bo"></a>`start_send_bo(seq_idx, bo_idx, bo_sem_idx)` — [`L576`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L576)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.start_update_kv_cache"></a>`start_update_kv_cache(seq_idx, bkv_sem_idx, offset, update_sz, vmem_start)` — [`L593`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L593)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.update_cur_bkv_to_cache"></a>`update_cur_bkv_to_cache()` — [`L725`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L725)
- <a id="_mla_batched_decode_kernel.wait_fetch"></a>`wait_fetch(batch_idx, sem_idx)` — [`L1228`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L1228)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.wait_fetch_bkv"></a>`wait_fetch_bkv(seq_idx, bkv_idx, bkv_sem_idx, start_offset)` — [`L567`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L567)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.wait_fetch_bq"></a>`wait_fetch_bq(seq_idx, bq_idx, bq_sem_idx)` — [`L573`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L573)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.wait_send_bo"></a>`wait_send_bo(bo_sem_idx)` — [`L583`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L583)
- <a id="_mla_batched_decode_kernel.wait_send_bo"></a>`wait_send_bo(batch_idx, sem_idx)` — [`L1237`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L1237)
- <a id="_mla_sliding_window_ragged_paged_attention_kernel.wait_update_kv_cache"></a>`wait_update_kv_cache(bkv_sem_idx)` — [`L601`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L601)
- <a id="_mla_batched_decode_kernel.wait_update_kv_cache"></a>`wait_update_kv_cache(batch_idx, sem_idx)` — [`L1232`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L1232)

## Module values
- <a id="DEFAULT_VMEM_LIMIT_BYTES"></a>`DEFAULT_VMEM_LIMIT_BYTES` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla_swa.py#L27)

