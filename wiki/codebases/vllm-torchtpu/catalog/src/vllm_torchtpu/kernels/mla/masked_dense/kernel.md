---
title: 'Module: src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.masked_dense.kernel`/
symbols:
  masked_dense_ragged_paged_attention: masked_dense_ragged_paged_attention().
  _mla_ragged_paged_attention_kernel.process.compute_with_bq: _mla_ragged_paged_attention_kernel().process().compute_with_bq().
  _mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv: _mla_ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().
  masked_dense_ragged_paged_attention.run_mla_kernel: masked_dense_ragged_paged_attention().run_mla_kernel().
  MlaCase.symbol: MlaCase#symbol().
  MlaCase: MlaCase#
  _mla_ragged_paged_attention_kernel._async_copy: _mla_ragged_paged_attention_kernel()._async_copy().
  _mla_ragged_paged_attention_kernel.start_fetch_bkv: _mla_ragged_paged_attention_kernel().start_fetch_bkv().
  _mla_ragged_paged_attention_kernel: _mla_ragged_paged_attention_kernel().
  _mla_ragged_paged_attention_kernel.flash_attention: _mla_ragged_paged_attention_kernel().flash_attention().
  _mla_ragged_paged_attention_kernel.wait_fetch_bkv: _mla_ragged_paged_attention_kernel().wait_fetch_bkv().
  _mla_ragged_paged_attention_kernel.process: _mla_ragged_paged_attention_kernel().process().
  prepare_q_inputs: prepare_q_inputs().
  align_to: align_to().
  _mla_ragged_paged_attention_kernel.broadcast_minor: _mla_ragged_paged_attention_kernel().broadcast_minor().
  _mla_ragged_paged_attention_kernel.prologue: _mla_ragged_paged_attention_kernel().prologue().
  _mla_ragged_paged_attention_kernel._fetch_bkv: _mla_ragged_paged_attention_kernel()._fetch_bkv().
  _mla_ragged_paged_attention_kernel._fetch_bq: _mla_ragged_paged_attention_kernel()._fetch_bq().
  _mla_ragged_paged_attention_kernel._send_bo: _mla_ragged_paged_attention_kernel()._send_bo().
  _mla_ragged_paged_attention_kernel._fetch_mask: _mla_ragged_paged_attention_kernel()._fetch_mask().
  _mla_ragged_paged_attention_kernel.start_fetch_bq: _mla_ragged_paged_attention_kernel().start_fetch_bq().
  _mla_ragged_paged_attention_kernel.wait_send_bo: _mla_ragged_paged_attention_kernel().wait_send_bo().
  cdiv: cdiv().
  _mla_ragged_paged_attention_kernel.wait_fetch_bq: _mla_ragged_paged_attention_kernel().wait_fetch_bq().
  _mla_ragged_paged_attention_kernel.start_send_bo: _mla_ragged_paged_attention_kernel().start_send_bo().
  MlaCase.MIXED: MlaCase#MIXED.
  _mla_ragged_paged_attention_kernel.process.compute_with_bq.prefetch_next_bq: _mla_ragged_paged_attention_kernel().process().compute_with_bq().prefetch_next_bq().
  _mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.prefetch_next_bkv: _mla_ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().prefetch_next_bkv().
  _mla_ragged_paged_attention_kernel.epilogue: _mla_ragged_paged_attention_kernel().epilogue().
  get_dtype_packing: get_dtype_packing().
  MlaCase.DECODE: MlaCase#DECODE.
  MlaCase.PREFILL: MlaCase#PREFILL.
  DEFAULT_MASK_VALUE: DEFAULT_MASK_VALUE.
  DEFAULT_VMEM_LIMIT_BYTES: DEFAULT_VMEM_LIMIT_BYTES.
  _mla_ragged_paged_attention_kernel.causal_mask: _mla_ragged_paged_attention_kernel().causal_mask().
  _mla_ragged_paged_attention_kernel.load_bq: _mla_ragged_paged_attention_kernel().load_bq().
  _mla_ragged_paged_attention_kernel.load_bkv: _mla_ragged_paged_attention_kernel().load_bkv().
  _mla_ragged_paged_attention_kernel.process.get_next_bq_ids: _mla_ragged_paged_attention_kernel().process().get_next_bq_ids().
  _mla_ragged_paged_attention_kernel.process.get_next_bkv_ids: _mla_ragged_paged_attention_kernel().process().get_next_bkv_ids().
  prepare_outputs: prepare_outputs().
---
# Module: [`src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py)

## Classes
### <a id="MlaCase"></a>`MlaCase`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py:69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L69)
- doc: Represents the different cases for MLA.
- signature: `class MlaCase(Enum):`
- members:
  - <a id="MlaCase.symbol"></a>`symbol(self)` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L82)
  - <a id="MlaCase.DECODE"></a>`DECODE` — [`L77`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L77)
  - <a id="MlaCase.MIXED"></a>`MIXED` — [`L79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L79)
  - <a id="MlaCase.PREFILL"></a>`PREFILL` — [`L78`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L78)
- used by: [`masked_dense_ragged_paged_attention`](kernel.md#masked_dense_ragged_paged_attention), [`run_mla_kernel`](kernel.md#masked_dense_ragged_paged_attention.run_mla_kernel)

## Functions
- <a id="_mla_ragged_paged_attention_kernel._async_copy"></a>`_async_copy(src, dst, sem, wait)` — [`L225`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L225)
- <a id="_mla_ragged_paged_attention_kernel._fetch_bkv"></a>`_fetch_bkv(seq_idx, bkv_idx, bkv_sem_idx, *, wait=False)` — [`L232`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L232)
- <a id="_mla_ragged_paged_attention_kernel._fetch_bq"></a>`_fetch_bq(seq_idx, bq_idx, bq_sem_idx, *, wait=False)` — [`L294`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L294)
- <a id="_mla_ragged_paged_attention_kernel._fetch_mask"></a>`_fetch_mask(seq_idx, bq_idx, bkv_idx, mask_sem_idx, *, wait=False)` — [`L323`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L323)
- <a id="_mla_ragged_paged_attention_kernel"></a>`_mla_ragged_paged_attention_kernel(kv_lens_ref, page_indices_ref, cu_q_lens_ref, start_end_seq_idx_ref, sem_ids_ref, bo_ids_ref, q_hbm_ref, cache_kv_nope_hbm_ref, cache_kv_rope_hbm_ref, mask_hbm_ref, o_hbm_ref, bkv_nope_x2_ref, bkv_rope_x2_ref, bq_x2_ref, bo_x2_ref, mask_hbm_x2_ref, sems, l_ref, m_ref, acc_ref, *, static_q_len: int | None, sm_scale: float, k_scale: float, mask_value: float, bkv_p: int, bq_sz: int, analytic_mask: bool)` — [`L90`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L90)
- <a id="_mla_ragged_paged_attention_kernel._send_bo"></a>`_send_bo(seq_idx, bo_idx, bo_sem_idx, *, wait=False)` — [`L309`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L309)
- <a id="align_to"></a>`align_to(x, a)` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L56)
- <a id="_mla_ragged_paged_attention_kernel.broadcast_minor"></a>`broadcast_minor(src, shape)` — [`L406`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L406)
- <a id="_mla_ragged_paged_attention_kernel.causal_mask"></a>`causal_mask(bq_idx, bkv_idx)` — [`L154`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L154) — Analytic replacement for the CSA mask. True where masked out.
- <a id="cdiv"></a>`cdiv(a, b)` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L51)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv"></a>`compute_with_bkv(bkv_idx, _)` — [`L463`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L463)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq"></a>`compute_with_bq(bq_idx, _)` — [`L447`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L447)
- <a id="_mla_ragged_paged_attention_kernel.epilogue"></a>`epilogue()` — [`L547`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L547)
- <a id="_mla_ragged_paged_attention_kernel.flash_attention"></a>`flash_attention(q, kv, *, bq_idx, bkv_idx, bq_mask_in)` — [`L172`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L172)
- <a id="get_dtype_packing"></a>`get_dtype_packing(dtype)` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L60)
- <a id="_mla_ragged_paged_attention_kernel.process.get_next_bkv_ids"></a>`get_next_bkv_ids(seq_idx, bq_idx, bkv_idx, bkv_sem_idx)` — [`L436`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L436)
- <a id="_mla_ragged_paged_attention_kernel.process.get_next_bq_ids"></a>`get_next_bq_ids(seq_idx, bq_idx, bq_sem_idx)` — [`L428`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L428)
- <a id="_mla_ragged_paged_attention_kernel.load_bkv"></a>`load_bkv(bkv_sem_idx, bkv_idx)` — [`L383`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L383)
- <a id="_mla_ragged_paged_attention_kernel.load_bq"></a>`load_bq(bq_sem_idx)` — [`L371`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L371)
- <a id="masked_dense_ragged_paged_attention"></a>`masked_dense_ragged_paged_attention(q: jax.Array, cache_kv_nope: jax.Array, cache_kv_rope: jax.Array, kv_lens: jax.Array, topk_indices: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, sm_scale: float = 1, k_scale: float = 1, mask_value: float | None = None, max_kv_len: int | None = None, chunk_prefill_size: int | None = None, num_kv_pages_per_block: tuple[int, int, int] | int | None = None, num_queries_per_block: tuple[int, int, int] | int | None = None, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES, sequence_start: jax.Array | None = None)` — [`L594`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L594) — Masked-dense DSA MLA ragged paged attention supporting mixed batches. — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.prefetch_next_bkv"></a>`prefetch_next_bkv()` — [`L472`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L472)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq.prefetch_next_bq"></a>`prefetch_next_bq()` — [`L455`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L455)
- <a id="prepare_outputs"></a>`prepare_outputs(out, actual_num_q_heads: int, actual_head_dim: int)` — [`L573`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L573)
- <a id="prepare_q_inputs"></a>`prepare_q_inputs(q: jax.Array)` — [`L554`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L554)
- <a id="_mla_ragged_paged_attention_kernel.process"></a>`process()` — [`L417`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L417)
- <a id="_mla_ragged_paged_attention_kernel.prologue"></a>`prologue()` — [`L540`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L540)
- <a id="masked_dense_ragged_paged_attention.run_mla_kernel"></a>`run_mla_kernel(q: jax.Array, cache_kv_nope: jax.Array, cache_kv_rope: jax.Array, kv_lens: jax.Array, mask_hbm: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, start_seq_idx: jax.Array, end_seq_idx: jax.Array, static_q_len: int | None, num_kv_pages_per_block: int, num_queries_per_block: int, case: MlaCase = MlaCase.MIXED)` — [`L736`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L736)
- <a id="_mla_ragged_paged_attention_kernel.start_fetch_bkv"></a>`start_fetch_bkv(seq_idx, bq_idx, bkv_idx, bkv_sem_idx)` — [`L344`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L344)
- <a id="_mla_ragged_paged_attention_kernel.start_fetch_bq"></a>`start_fetch_bq(seq_idx, bq_idx, bq_sem_idx)` — [`L352`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L352)
- <a id="_mla_ragged_paged_attention_kernel.start_send_bo"></a>`start_send_bo(seq_idx, bo_idx, bo_sem_idx)` — [`L358`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L358)
- <a id="_mla_ragged_paged_attention_kernel.wait_fetch_bkv"></a>`wait_fetch_bkv(seq_idx, bq_idx, bkv_idx, bkv_sem_idx)` — [`L348`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L348)
- <a id="_mla_ragged_paged_attention_kernel.wait_fetch_bq"></a>`wait_fetch_bq(seq_idx, bq_idx, bq_sem_idx)` — [`L355`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L355)
- <a id="_mla_ragged_paged_attention_kernel.wait_send_bo"></a>`wait_send_bo(bo_sem_idx)` — [`L363`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L363)

## Module values
- <a id="DEFAULT_MASK_VALUE"></a>`DEFAULT_MASK_VALUE` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L64)
- <a id="DEFAULT_VMEM_LIMIT_BYTES"></a>`DEFAULT_VMEM_LIMIT_BYTES` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/masked_dense/kernel.py#L66)

