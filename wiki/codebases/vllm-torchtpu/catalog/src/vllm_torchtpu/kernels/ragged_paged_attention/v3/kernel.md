---
title: 'Module: src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.ragged_paged_attention.v3.kernel`/
symbols:
  _ragged_paged_attention_kernel_loop.debug_print: _ragged_paged_attention_kernel_loop().debug_print().
  ragged_paged_attention: ragged_paged_attention().
  RpaCase: RpaCase#
  get_default_block_sizes: get_default_block_sizes().
  ragged_paged_attention.run_rpa_kernel: ragged_paged_attention().run_rpa_kernel().
  _ragged_paged_attention_kernel_loop: _ragged_paged_attention_kernel_loop().
  _ragged_paged_attention_kernel_loop.process.compute_with_bq: _ragged_paged_attention_kernel_loop().process().compute_with_bq().
  ref_ragged_paged_attention: ref_ragged_paged_attention().
  _ragged_paged_attention_kernel_loop._update_kv_cache: _ragged_paged_attention_kernel_loop()._update_kv_cache().
  static_validate_inputs: static_validate_inputs().
  RpaCase.symbol: RpaCase#symbol().
  RpaCase.get_range: RpaCase#get_range().
  _ragged_paged_attention_kernel_loop.flash_attention_step1_qk_softmax: _ragged_paged_attention_kernel_loop().flash_attention_step1_qk_softmax().
  prepare_inputs: prepare_inputs().
  get_vmem_estimate_bytes: get_vmem_estimate_bytes().
  _ragged_paged_attention_kernel_loop.process.compute_with_bq.compute_with_bkv: _ragged_paged_attention_kernel_loop().process().compute_with_bq().compute_with_bkv().
  _ragged_paged_attention_kernel_loop.process.compute_with_bq.compute_with_bkv.attention_loop: _ragged_paged_attention_kernel_loop().process().compute_with_bq().compute_with_bkv().attention_loop().
  _ragged_paged_attention_kernel_loop._fetch_bkv: _ragged_paged_attention_kernel_loop()._fetch_bkv().
  merge_kv: merge_kv().
  RpaCase.DECODE: RpaCase#DECODE.
  RpaCase.MIXED: RpaCase#MIXED.
  get_kv_cache_shape: get_kv_cache_shape().
  _ragged_paged_attention_kernel_loop._async_copy: _ragged_paged_attention_kernel_loop()._async_copy().
  _ragged_paged_attention_kernel_loop._fetch_bq: _ragged_paged_attention_kernel_loop()._fetch_bq().
  _ragged_paged_attention_kernel_loop._send_bo: _ragged_paged_attention_kernel_loop()._send_bo().
  _ragged_paged_attention_kernel_loop.strided_load: _ragged_paged_attention_kernel_loop().strided_load().
  _ragged_paged_attention_kernel_loop._update_kv_cache.loop_body: _ragged_paged_attention_kernel_loop()._update_kv_cache().loop_body().
  dynamic_validate_inputs: dynamic_validate_inputs().
  _ragged_paged_attention_kernel_loop.broadcast_minor: _ragged_paged_attention_kernel_loop().broadcast_minor().
  ragged_paged_attention._prepare_block_sizes: ragged_paged_attention()._prepare_block_sizes().
  RpaCase.PREFILL: RpaCase#PREFILL.
  get_smem_estimate_bytes: get_smem_estimate_bytes().
  _ragged_paged_attention_kernel_loop.prologue: _ragged_paged_attention_kernel_loop().prologue().
  _ragged_paged_attention_kernel_loop.epilogue: _ragged_paged_attention_kernel_loop().epilogue().
  _ragged_paged_attention_kernel_loop.flash_attention_step2_pv: _ragged_paged_attention_kernel_loop().flash_attention_step2_pv().
  _ragged_paged_attention_kernel_loop.start_fetch_bkv: _ragged_paged_attention_kernel_loop().start_fetch_bkv().
  _ragged_paged_attention_kernel_loop.start_fetch_bq: _ragged_paged_attention_kernel_loop().start_fetch_bq().
  _ragged_paged_attention_kernel_loop.wait_send_bo: _ragged_paged_attention_kernel_loop().wait_send_bo().
  _ragged_paged_attention_kernel_loop.wait_update_kv_cache: _ragged_paged_attention_kernel_loop().wait_update_kv_cache().
  ragged_paged_attention_bundled: ragged_paged_attention_bundled().
  _ragged_paged_attention_kernel: _ragged_paged_attention_kernel().
  _ragged_paged_attention_kernel_loop.wait_fetch_bkv: _ragged_paged_attention_kernel_loop().wait_fetch_bkv().
  _ragged_paged_attention_kernel_loop.wait_fetch_bq: _ragged_paged_attention_kernel_loop().wait_fetch_bq().
  _ragged_paged_attention_kernel_loop.start_send_bo: _ragged_paged_attention_kernel_loop().start_send_bo().
  _ragged_paged_attention_kernel_loop.start_update_kv_cache: _ragged_paged_attention_kernel_loop().start_update_kv_cache().
  _ragged_paged_attention_kernel_loop.strided_store: _ragged_paged_attention_kernel_loop().strided_store().
  _ragged_paged_attention_kernel_loop.load_bq: _ragged_paged_attention_kernel_loop().load_bq().
  _ragged_paged_attention_kernel_loop.load_bkv: _ragged_paged_attention_kernel_loop().load_bkv().
  _ragged_paged_attention_kernel_loop.process: _ragged_paged_attention_kernel_loop().process().
  prepare_outputs: prepare_outputs().
  _ragged_paged_attention_kernel_loop.mask_and: _ragged_paged_attention_kernel_loop().mask_and().
  static_validate_inputs._validate_block_sizes: static_validate_inputs()._validate_block_sizes().
  _ragged_paged_attention_kernel_loop.process.compute_with_bq.prefetch_next_bq: _ragged_paged_attention_kernel_loop().process().compute_with_bq().prefetch_next_bq().
  _ragged_paged_attention_kernel_loop.process.compute_with_bq.compute_with_bkv.prefetch_next_bkv: _ragged_paged_attention_kernel_loop().process().compute_with_bq().compute_with_bkv().prefetch_next_bkv().
  _ragged_paged_attention_kernel_loop.process.compute_with_bq.compute_with_bkv.wait_cur_bq: _ragged_paged_attention_kernel_loop().process().compute_with_bq().compute_with_bkv().wait_cur_bq().
  _ragged_paged_attention_kernel_loop.process.compute_with_bq.compute_with_bkv.update_cur_bkv_to_cache: _ragged_paged_attention_kernel_loop().process().compute_with_bq().compute_with_bkv().update_cur_bkv_to_cache().
  _ragged_paged_attention_kernel_loop.pipeline: _ragged_paged_attention_kernel_loop().pipeline().
  has_bank_conflicts: has_bank_conflicts().
  ragged_paged_attention.run_rpa_kernel.run: ragged_paged_attention().run_rpa_kernel().run().
  _ragged_paged_attention_kernel_loop.process.get_next_bq_ids: _ragged_paged_attention_kernel_loop().process().get_next_bq_ids().
  _ragged_paged_attention_kernel_loop.process.get_next_bkv_ids: _ragged_paged_attention_kernel_loop().process().get_next_bkv_ids().
---
# Module: [`src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py)

## Classes
### <a id="RpaCase"></a>`RpaCase`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py:42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L42) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- doc: Represents the different cases for Ragged Paged Attention.
- signature: `class RpaCase(Enum):`
- members:
  - <a id="RpaCase.get_range"></a>`get_range(self, distribution)` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L62) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
  - <a id="RpaCase.symbol"></a>`symbol(self)` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L55) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
  - <a id="RpaCase.DECODE"></a>`DECODE` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L50) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
  - <a id="RpaCase.MIXED"></a>`MIXED` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L52) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
  - <a id="RpaCase.PREFILL"></a>`PREFILL` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L51) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- used by: [`ragged_paged_attention`](kernel.md#ragged_paged_attention), [`sharded_ragged_paged_attention`](../../../layers/core/attention_interface.md#sharded_ragged_paged_attention), [`get_default_block_sizes`](kernel.md#get_default_block_sizes), [`run_rpa_kernel`](kernel.md#ragged_paged_attention.run_rpa_kernel), [`_ragged_paged_attention_kernel_loop`](kernel.md#_ragged_paged_attention_kernel_loop)

## Functions
- <a id="_ragged_paged_attention_kernel_loop._async_copy"></a>`_async_copy(src, dst, sem, wait)` — [`L559`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L559)
- <a id="_ragged_paged_attention_kernel_loop._fetch_bkv"></a>`_fetch_bkv(seq_idx, bkv_idx, bkv_sem_idx, *, wait=False)` — [`L569`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L569)
- <a id="_ragged_paged_attention_kernel_loop._fetch_bq"></a>`_fetch_bq(seq_idx, bq_idx, bq_sem_idx, *, wait=False)` — [`L717`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L717)
- <a id="ragged_paged_attention._prepare_block_sizes"></a>`_prepare_block_sizes(block_sizes, case)` — [`L1929`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1929) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel"></a>`_ragged_paged_attention_kernel(*args, **kwargs)` — [`L295`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L295)
- <a id="_ragged_paged_attention_kernel_loop"></a>`_ragged_paged_attention_kernel_loop(seq_idx, kv_lens_ref, page_indices_ref, cu_q_lens_ref, distribution_ref, sem_ids_ref, bo_ids_ref, bkv_update_ids_ref, q_hbm_ref, kv_hbm_ref, kv_cache_hbm_ref, o_hbm_ref, updated_kv_cache_hbm_ref, bkv_x2_ref, bq_x2_ref, bo_x2_ref, sems, l_ref, m_ref, acc_ref, *, use_causal_mask: bool = True, skip_kv_mask: bool = False, skip_kv_update: bool = False, sm_scale: float, sliding_window: int | None = None, soft_cap: float | None = None, mask_value: float | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, static_q_len: int | None = None, bq_sz, bkv_sz, bq_csz, bkv_csz, case: RpaCase = RpaCase.MIXED, debug_mode: bool = False)` — [`L308`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L308) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel_loop._send_bo"></a>`_send_bo(seq_idx, bo_idx, bo_sem_idx, *, wait=False)` — [`L741`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L741)
- <a id="_ragged_paged_attention_kernel_loop._update_kv_cache"></a>`_update_kv_cache(seq_idx, bkv_sem_idx, offset, update_sz, *, wait=False)` — [`L652`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L652) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="static_validate_inputs._validate_block_sizes"></a>`_validate_block_sizes(block_sizes, prefix)` — [`L1506`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1506)
- <a id="_ragged_paged_attention_kernel_loop.process.compute_with_bq.compute_with_bkv.attention_loop"></a>`attention_loop(idx)` — [`L1014`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1014) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel_loop.broadcast_minor"></a>`broadcast_minor(src, shape)` — [`L880`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L880)
- <a id="_ragged_paged_attention_kernel_loop.process.compute_with_bq.compute_with_bkv"></a>`compute_with_bkv(bkv_idx)` — [`L967`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L967) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel_loop.process.compute_with_bq"></a>`compute_with_bq(bq_idx)` — [`L936`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L936) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel_loop.debug_print"></a>`debug_print(msg, *args)` — [`L432`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L432)
- <a id="dynamic_validate_inputs"></a>`dynamic_validate_inputs(queries: jax.Array, keys: jax.Array, values: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, use_causal_mask: bool = True, skip_kv_mask: bool = False, sm_scale: float = 1, sliding_window: int | None = None, soft_cap: float | None = None, out_dtype: Any = None, mask_value: float | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, chunk_prefill_size: int | None = None, d_block_sizes: tuple[int, int, int, int] | None = None, p_block_sizes: tuple[int, int, int, int] | None = None, m_block_sizes: tuple[int, int, int, int] | None = None, vmem_limit_bytes: int | None = None)` — [`L1273`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1273)
- <a id="_ragged_paged_attention_kernel_loop.epilogue"></a>`epilogue()` — [`L1122`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1122)
- <a id="_ragged_paged_attention_kernel_loop.flash_attention_step1_qk_softmax"></a>`flash_attention_step1_qk_softmax(q, k, v, l_ref, m_ref, *, processed_q_len, processed_kv_len, effective_kv_len)` — [`L455`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L455) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel_loop.flash_attention_step2_pv"></a>`flash_attention_step2_pv(p, v, exp_m_diff, o_ref)` — [`L540`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L540)
- <a id="get_default_block_sizes"></a>`get_default_block_sizes(q_dtype, kv_dtype, actual_num_q_heads, actual_num_kv_heads, head_dim, page_size, max_num_tokens, max_num_seqs, pages_per_seq, *, case: RpaCase = RpaCase.MIXED)` — [`L1541`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1541) — Get (bq, bkv_sz, bq_csz, bkv_csz) by some heuristic formulas. — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="get_kv_cache_shape"></a>`get_kv_cache_shape(total_num_pages, page_size, actual_num_kv_heads, actual_head_dim, kv_dtype)` — [`L278`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L278) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel_loop.process.get_next_bkv_ids"></a>`get_next_bkv_ids(seq_idx, bq_idx, bkv_idx, bkv_sem_idx, *, num_bkv)` — [`L914`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L914)
- <a id="_ragged_paged_attention_kernel_loop.process.get_next_bq_ids"></a>`get_next_bq_ids(seq_idx, bq_idx, bq_sem_idx)` — [`L906`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L906)
- <a id="get_smem_estimate_bytes"></a>`get_smem_estimate_bytes(max_num_seqs, pages_per_seq)` — [`L217`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L217)
- <a id="get_vmem_estimate_bytes"></a>`get_vmem_estimate_bytes(actual_num_kv_heads, actual_num_q_heads_per_kv_head, actual_head_dim, bq_sz, bkv_sz, q_dtype, kv_dtype)` — [`L243`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L243) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="has_bank_conflicts"></a>`has_bank_conflicts(stride, distance=24, num_banks=32)` — [`L1130`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1130)
- <a id="_ragged_paged_attention_kernel_loop.load_bkv"></a>`load_bkv(bkv_sem_idx, kv_head_idx, start, sz)` — [`L850`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L850)
- <a id="_ragged_paged_attention_kernel_loop.load_bq"></a>`load_bq(bq_sem_idx, kv_head_idx, start, sz)` — [`L840`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L840)
- <a id="_ragged_paged_attention_kernel_loop._update_kv_cache.loop_body"></a>`loop_body(i, states)` — [`L682`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L682)
- <a id="_ragged_paged_attention_kernel_loop.mask_and"></a>`mask_and(mask, new_mask)` — [`L891`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L891)
- <a id="merge_kv"></a>`merge_kv(k: jax.Array, v: jax.Array)` — [`L1140`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1140) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel_loop.pipeline"></a>`pipeline()` — [`L1118`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1118)
- <a id="_ragged_paged_attention_kernel_loop.process.compute_with_bq.compute_with_bkv.prefetch_next_bkv"></a>`prefetch_next_bkv()` — [`L979`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L979)
- <a id="_ragged_paged_attention_kernel_loop.process.compute_with_bq.prefetch_next_bq"></a>`prefetch_next_bq()` — [`L962`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L962)
- <a id="prepare_inputs"></a>`prepare_inputs(q: jax.Array, k: jax.Array, v: jax.Array, *, fuse_non_tiling_axis_swap: bool | None = None)` — [`L1171`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1171) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="prepare_outputs"></a>`prepare_outputs(out, actual_num_q_heads_per_kv_head: int, actual_head_dim: int, *, fuse_non_tiling_axis_swap: bool | None = None)` — [`L1222`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1222) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel_loop.process"></a>`process(static_q_len=None)` — [`L896`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L896)
- <a id="_ragged_paged_attention_kernel_loop.prologue"></a>`prologue()` — [`L1111`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1111)
- <a id="ragged_paged_attention"></a>`ragged_paged_attention(queries: jax.Array, keys: jax.Array, values: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, use_causal_mask: bool = True, skip_kv_mask: bool = False, skip_kv_update: bool = False, sm_scale: float = 1, sliding_window: int | None = None, soft_cap: float | None = None, out_dtype: Any = None, mask_value: float | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, chunk_prefill_size: int | None = None, d_block_sizes: tuple[int, int, int, int] | None = None, p_block_sizes: tuple[int, int, int, int] | None = None, m_block_sizes: tuple[int, int, int, int] | None = None, vmem_limit_bytes: int | None = None, debug_mode: bool = False, disable_bounds_checks: bool = True, disable_semaphore_checks: bool = True)` — [`L1633`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1633) — Ragged paged attention that supports mixed prefill and decode. — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="ragged_paged_attention_bundled"></a>`ragged_paged_attention_bundled(queries: jax.Array, keys: jax.Array, values: jax.Array, kv_cache_bundle: jax.Array, layer_idx: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, **kwargs)` — [`L2011`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L2011) — Executes ragged paged attention directly against a bundled block-major — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="ref_ragged_paged_attention"></a>`ref_ragged_paged_attention(queries: jax.Array, keys: jax.Array, values: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, use_causal_mask: bool = True, skip_kv_mask: bool = False, skip_kv_update: bool = False, sm_scale: float = 1, sliding_window: int | None = None, soft_cap: float | None = None, out_dtype: Any = None, mask_value: float | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None)` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L74) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="ragged_paged_attention.run_rpa_kernel.run"></a>`run(scalar_prefetches, q, kv, kv_cache)` — [`L1915`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1915)
- <a id="ragged_paged_attention.run_rpa_kernel"></a>`run_rpa_kernel(q, kv_cache, *, bq_sz, bkv_sz, bq_csz, bkv_csz, static_q_len=None, case: RpaCase = RpaCase.MIXED)` — [`L1782`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1782) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel_loop.start_fetch_bkv"></a>`start_fetch_bkv(seq_idx, bkv_idx, bkv_sem_idx)` — [`L765`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L765)
- <a id="_ragged_paged_attention_kernel_loop.start_fetch_bq"></a>`start_fetch_bq(seq_idx, bq_idx, bq_sem_idx)` — [`L771`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L771)
- <a id="_ragged_paged_attention_kernel_loop.start_send_bo"></a>`start_send_bo(seq_idx, bo_idx, bo_sem_idx)` — [`L777`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L777)
- <a id="_ragged_paged_attention_kernel_loop.start_update_kv_cache"></a>`start_update_kv_cache(seq_idx, bkv_sem_idx, offset, update_sz)` — [`L790`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L790)
- <a id="static_validate_inputs"></a>`static_validate_inputs(queries: jax.Array, keys: jax.Array, values: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, use_causal_mask: bool = True, skip_kv_mask: bool = False, sm_scale: float = 1, sliding_window: int | None = None, soft_cap: float | None = None, out_dtype: Any = None, mask_value: float | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, chunk_prefill_size: int | None = None, d_block_sizes: tuple[int, int, int, int] | None = None, p_block_sizes: tuple[int, int, int, int] | None = None, m_block_sizes: tuple[int, int, int, int] | None = None, vmem_limit_bytes: int | None = None)` — [`L1366`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L1366) — Validate inputs to the RPA kernel statically. — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel_loop.strided_load"></a>`strided_load(ref, start, sz, step, *, dtype=None)` — [`L806`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L806) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel_loop.strided_store"></a>`strided_store(ref, start, sz, step, val)` — [`L824`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L824) — documented in [ragged-paged-attention-kernel](../../../../../../concepts/ragged-paged-attention-kernel.md)
- <a id="_ragged_paged_attention_kernel_loop.process.compute_with_bq.compute_with_bkv.update_cur_bkv_to_cache"></a>`update_cur_bkv_to_cache()` — [`L994`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L994)
- <a id="_ragged_paged_attention_kernel_loop.process.compute_with_bq.compute_with_bkv.wait_cur_bq"></a>`wait_cur_bq()` — [`L985`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L985)
- <a id="_ragged_paged_attention_kernel_loop.wait_fetch_bkv"></a>`wait_fetch_bkv(seq_idx, bkv_idx, bkv_sem_idx)` — [`L768`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L768)
- <a id="_ragged_paged_attention_kernel_loop.wait_fetch_bq"></a>`wait_fetch_bq(seq_idx, bq_idx, bq_sem_idx)` — [`L774`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L774)
- <a id="_ragged_paged_attention_kernel_loop.wait_send_bo"></a>`wait_send_bo(bo_sem_idx)` — [`L782`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L782)
- <a id="_ragged_paged_attention_kernel_loop.wait_update_kv_cache"></a>`wait_update_kv_cache(bkv_sem_idx)` — [`L796`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/ragged_paged_attention/v3/kernel.py#L796)

