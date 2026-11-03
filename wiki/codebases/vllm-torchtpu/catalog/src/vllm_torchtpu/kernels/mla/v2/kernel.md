---
title: 'Module: src/vllm_torchtpu/kernels/mla/v2/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/v2/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.v2.kernel`/
symbols:
  _mla_ragged_paged_attention_kernel.debug_print: _mla_ragged_paged_attention_kernel().debug_print().
  _mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv: _mla_ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().
  mla_ragged_paged_attention: mla_ragged_paged_attention().
  _mla_ragged_paged_attention_kernel._async_copy: _mla_ragged_paged_attention_kernel()._async_copy().
  mla_ragged_paged_attention.run_mla_kernel: mla_ragged_paged_attention().run_mla_kernel().
  _mla_ragged_paged_attention_kernel._update_transposed_kv_cache: _mla_ragged_paged_attention_kernel()._update_transposed_kv_cache().
  _mla_ragged_paged_attention_kernel: _mla_ragged_paged_attention_kernel().
  _mla_ragged_paged_attention_kernel._fetch_transposed_bkv: _mla_ragged_paged_attention_kernel()._fetch_transposed_bkv().
  _mla_ragged_paged_attention_kernel._pack_new_transposed_kv._update: _mla_ragged_paged_attention_kernel()._pack_new_transposed_kv()._update().
  unsigned_align_to: unsigned_align_to().
  _mla_ragged_paged_attention_kernel._update_kv_cache: _mla_ragged_paged_attention_kernel()._update_kv_cache().
  unsigned_floor_div: unsigned_floor_div().
  get_dtype_packing: get_dtype_packing().
  MlaCase.symbol: MlaCase#symbol().
  _mla_ragged_paged_attention_kernel._fetch_bkv: _mla_ragged_paged_attention_kernel()._fetch_bkv().
  _mla_ragged_paged_attention_kernel.process.compute_with_bq: _mla_ragged_paged_attention_kernel().process().compute_with_bq().
  unsigned_cdiv: unsigned_cdiv().
  align_to: align_to().
  prepare_q_nope_inputs: prepare_q_nope_inputs().
  prepare_outputs: prepare_outputs().
  MlaCase: MlaCase#
  unsigned_mod: unsigned_mod().
  static_validate_inputs: static_validate_inputs().
  _mla_ragged_paged_attention_kernel.batch_flash_attention: _mla_ragged_paged_attention_kernel().batch_flash_attention().
  _mla_ragged_paged_attention_kernel.flash_attention_step1_qk_softmax: _mla_ragged_paged_attention_kernel().flash_attention_step1_qk_softmax().
  _mla_ragged_paged_attention_kernel._pack_new_transposed_kv._update.update_body: _mla_ragged_paged_attention_kernel()._pack_new_transposed_kv()._update().update_body().
  _mla_ragged_paged_attention_kernel.process: _mla_ragged_paged_attention_kernel().process().
  _mla_ragged_paged_attention_kernel.wait_update_kv_cache: _mla_ragged_paged_attention_kernel().wait_update_kv_cache().
  _mla_ragged_paged_attention_kernel.broadcast_minor: _mla_ragged_paged_attention_kernel().broadcast_minor().
  get_kv_cache_shape: get_kv_cache_shape().
  _mla_ragged_paged_attention_kernel.flash_attention_step2_pv: _mla_ragged_paged_attention_kernel().flash_attention_step2_pv().
  _mla_ragged_paged_attention_kernel._update_transposed_kv_cache.loop_body: _mla_ragged_paged_attention_kernel()._update_transposed_kv_cache().loop_body().
  _mla_ragged_paged_attention_kernel.start_update_kv_cache: _mla_ragged_paged_attention_kernel().start_update_kv_cache().
  prepare_q_inputs: prepare_q_inputs().
  _mla_ragged_paged_attention_kernel.prologue: _mla_ragged_paged_attention_kernel().prologue().
  _mla_ragged_paged_attention_kernel.epilogue: _mla_ragged_paged_attention_kernel().epilogue().
  logger: logger.
  _mla_ragged_paged_attention_kernel._pack_new_transposed_kv._update.copy_partial: _mla_ragged_paged_attention_kernel()._pack_new_transposed_kv()._update().copy_partial().
  _mla_ragged_paged_attention_kernel._fetch_bq: _mla_ragged_paged_attention_kernel()._fetch_bq().
  _mla_ragged_paged_attention_kernel._send_bo: _mla_ragged_paged_attention_kernel()._send_bo().
  _mla_ragged_paged_attention_kernel.start_fetch_bq: _mla_ragged_paged_attention_kernel().start_fetch_bq().
  _mla_ragged_paged_attention_kernel.wait_send_bo: _mla_ragged_paged_attention_kernel().wait_send_bo().
  prepare_kv_inputs: prepare_kv_inputs().
  _XPOSE_N_TILE_SIZE: _XPOSE_N_TILE_SIZE.
  _mla_ragged_paged_attention_kernel._pack_new_transposed_kv: _mla_ragged_paged_attention_kernel()._pack_new_transposed_kv().
  _mla_ragged_paged_attention_kernel._pack_new_kv: _mla_ragged_paged_attention_kernel()._pack_new_kv().
  _mla_ragged_paged_attention_kernel._update_kv_cache.loop_body: _mla_ragged_paged_attention_kernel()._update_kv_cache().loop_body().
  _mla_ragged_paged_attention_kernel.wait_fetch_bq: _mla_ragged_paged_attention_kernel().wait_fetch_bq().
  _mla_ragged_paged_attention_kernel.start_send_bo: _mla_ragged_paged_attention_kernel().start_send_bo().
  MlaCase.MIXED: MlaCase#MIXED.
  _mla_ragged_paged_attention_kernel.batch_flash_attention.load_with_init: _mla_ragged_paged_attention_kernel().batch_flash_attention().load_with_init().
  _mla_ragged_paged_attention_kernel.start_fetch_bkv: _mla_ragged_paged_attention_kernel().start_fetch_bkv().
  _mla_ragged_paged_attention_kernel._pack_new_kv._update: _mla_ragged_paged_attention_kernel()._pack_new_kv()._update().
  _mla_ragged_paged_attention_kernel._fetch_bq._copy: _mla_ragged_paged_attention_kernel()._fetch_bq()._copy().
  _mla_ragged_paged_attention_kernel._send_bo._copy: _mla_ragged_paged_attention_kernel()._send_bo()._copy().
  _mla_ragged_paged_attention_kernel.process.compute_with_bq.prefetch_next_bq: _mla_ragged_paged_attention_kernel().process().compute_with_bq().prefetch_next_bq().
  _mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.prefetch_next_bkv: _mla_ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().prefetch_next_bkv().
  _mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.wait_cur_bq: _mla_ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().wait_cur_bq().
  _mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.update_cur_bkv_to_cache: _mla_ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().update_cur_bkv_to_cache().
  MlaCase.DECODE: MlaCase#DECODE.
  MlaCase.PREFILL: MlaCase#PREFILL.
  MlaCase.BATCHED_DECODE: MlaCase#BATCHED_DECODE.
  _mla_ragged_paged_attention_kernel.flash_attention_step1_qk_softmax.load_with_init: _mla_ragged_paged_attention_kernel().flash_attention_step1_qk_softmax().load_with_init().
  prepare_kv_inputs_for_transposed_kv_cache: prepare_kv_inputs_for_transposed_kv_cache().
  get_dtype_bitwidth: get_dtype_bitwidth().
  _mla_ragged_paged_attention_kernel.flash_attention_step2_pv.load_with_init: _mla_ragged_paged_attention_kernel().flash_attention_step2_pv().load_with_init().
  _mla_ragged_paged_attention_kernel.wait_fetch_bkv: _mla_ragged_paged_attention_kernel().wait_fetch_bkv().
  _mla_ragged_paged_attention_kernel.load_batch_bq: _mla_ragged_paged_attention_kernel().load_batch_bq().
  _mla_ragged_paged_attention_kernel.load_bq: _mla_ragged_paged_attention_kernel().load_bq().
  _mla_ragged_paged_attention_kernel.load_bkv: _mla_ragged_paged_attention_kernel().load_bkv().
  _mla_ragged_paged_attention_kernel.load_transposed_bkv: _mla_ragged_paged_attention_kernel().load_transposed_bkv().
  _mla_ragged_paged_attention_kernel.load_batch_bkv: _mla_ragged_paged_attention_kernel().load_batch_bkv().
  _mla_ragged_paged_attention_kernel.process.get_next_bq_ids: _mla_ragged_paged_attention_kernel().process().get_next_bq_ids().
  _mla_ragged_paged_attention_kernel.process.get_next_bkv_ids: _mla_ragged_paged_attention_kernel().process().get_next_bkv_ids().
---
# Module: [`src/vllm_torchtpu/kernels/mla/v2/kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py)

## Classes
### <a id="MlaCase"></a>`MlaCase`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/kernels/mla/v2/kernel.py:111`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L111)
- doc: Represents the different cases for MLA.
- signature: `class MlaCase(Enum):`
- members:
  - <a id="MlaCase.symbol"></a>`symbol(self)` — [`L125`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L125)
  - <a id="MlaCase.BATCHED_DECODE"></a>`BATCHED_DECODE` — [`L122`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L122)
  - <a id="MlaCase.DECODE"></a>`DECODE` — [`L119`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L119)
  - <a id="MlaCase.MIXED"></a>`MIXED` — [`L121`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L121)
  - <a id="MlaCase.PREFILL"></a>`PREFILL` — [`L120`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L120)
- used by: [`mla_ragged_paged_attention`](kernel.md#mla_ragged_paged_attention), [`run_mla_kernel`](kernel.md#mla_ragged_paged_attention.run_mla_kernel)

## Functions
- <a id="_mla_ragged_paged_attention_kernel._async_copy"></a>`_async_copy(src, dst, sem, wait)` — [`L739`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L739)
- <a id="_mla_ragged_paged_attention_kernel._fetch_bq._copy"></a>`_copy(q_len_start=q_len_start, sz=sz, bq_nope_vmem_ref=bq_nope_vmem_ref, bq_rope_vmem_ref=bq_rope_vmem_ref, sem=sem)` — [`L1610`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1610)
- <a id="_mla_ragged_paged_attention_kernel._send_bo._copy"></a>`_copy(b=b, vmem_ref=vmem_ref, sz=sz, q_len_start=q_len_start, sem=sem)` — [`L1653`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1653)
- <a id="_mla_ragged_paged_attention_kernel._fetch_bkv"></a>`_fetch_bkv(batch_start_seq_idx, bkv_idx, bkv_sem_idx, *, wait=False)` — [`L953`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L953)
- <a id="_mla_ragged_paged_attention_kernel._fetch_bq"></a>`_fetch_bq(batch_start_seq_idx, bq_idx, bq_sem_idx, *, wait=False)` — [`L1587`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1587)
- <a id="_mla_ragged_paged_attention_kernel._fetch_transposed_bkv"></a>`_fetch_transposed_bkv(batch_start_seq_idx, bkv_idx, bkv_sem_idx, *, wait=False)` — [`L749`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L749)
- <a id="_mla_ragged_paged_attention_kernel"></a>`_mla_ragged_paged_attention_kernel(kv_lens_ref, page_indices_ref, cu_q_lens_ref, start_end_seq_idx_ref, sem_ids_ref, bo_ids_ref, bkv_update_ids_ref, ql_nope_hbm_ref, q_pe_hbm_ref, new_kv_c_hbm_ref, new_k_pe_hbm_ref, cache_kv_hbm_ref, lse_in_hbm_ref, o_hbm_ref, updated_cache_kv_hbm_ref, lse_hbm_ref, bkvc_x2_ref, bkpe_x2_ref, bq_nope_x2_ref, bq_rope_x2_ref, bo_x2_ref, sems, l_ref, m_ref, acc_ref, blse_x2_ref, *, static_q_len: int | None, sm_scale: float, mask_value: float, s_dtype: jnp.dtype, transpose_kv_cache: bool, two_step_flash_attention: bool, p_same_dtype_as_v: bool, use_causal_mask: bool, sliding_window: int | None = None, soft_cap: float | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, bkv_p, bq_sz, batch_size: int = 1, q_split: int = 1, debug_mode: bool = False, return_lse: bool = False)` — [`L305`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L305)
- <a id="_mla_ragged_paged_attention_kernel._pack_new_kv"></a>`_pack_new_kv(bkv_sem_idx, offsets, update_szs)` — [`L1306`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1306) — Packs newly computed KVs into the correct sub-word alignment in VMEM.
- <a id="_mla_ragged_paged_attention_kernel._pack_new_transposed_kv"></a>`_pack_new_transposed_kv(bkv_sem_idx, bkv_idx, offsets, update_szs)` — [`L1171`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1171) — Packs newly computed KVs into the correct sub-word alignment in VMEM.
- <a id="_mla_ragged_paged_attention_kernel._send_bo"></a>`_send_bo(batch_start_seq_idx, bo_idx, bo_sem_idx, *, wait=False)` — [`L1631`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1631)
- <a id="_mla_ragged_paged_attention_kernel._pack_new_transposed_kv._update"></a>`_update(b=b, update_sz=update_sz)` — [`L1186`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1186)
- <a id="_mla_ragged_paged_attention_kernel._pack_new_kv._update"></a>`_update(b=b, offset=offset, update_sz=update_sz)` — [`L1337`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1337)
- <a id="_mla_ragged_paged_attention_kernel._update_kv_cache"></a>`_update_kv_cache(batch_start_seq_idx, b, bkv_sem_idx, offset, update_sz, *, wait=False)` — [`L1478`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1478)
- <a id="_mla_ragged_paged_attention_kernel._update_transposed_kv_cache"></a>`_update_transposed_kv_cache(batch_start_seq_idx, b, bkv_sem_idx, offset, update_sz, *, wait=False)` — [`L1357`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1357)
- <a id="align_to"></a>`align_to(a, b)` — [`L72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L72)
- <a id="_mla_ragged_paged_attention_kernel.batch_flash_attention"></a>`batch_flash_attention(ql_nope, q_pe, kv_c, k_pe, *, bq_idx, bkv_idx)` — [`L447`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L447)
- <a id="_mla_ragged_paged_attention_kernel.broadcast_minor"></a>`broadcast_minor(src, shape)` — [`L1809`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1809)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv"></a>`compute_with_bkv(bkv_idx, _)` — [`L1885`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1885) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq"></a>`compute_with_bq(bq_idx, _)` — [`L1873`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1873)
- <a id="_mla_ragged_paged_attention_kernel._pack_new_transposed_kv._update.copy_partial"></a>`copy_partial(new_kv_idx, new_kv_start, bkv_idx, bkv_start)` — [`L1239`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1239)
- <a id="_mla_ragged_paged_attention_kernel.debug_print"></a>`debug_print(msg, *args)` — [`L432`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L432) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- <a id="_mla_ragged_paged_attention_kernel.epilogue"></a>`epilogue()` — [`L2149`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L2149)
- <a id="_mla_ragged_paged_attention_kernel.flash_attention_step1_qk_softmax"></a>`flash_attention_step1_qk_softmax(ql_nope, q_pe, kv_c, k_pe, *, kv_len, q_len, bq_idx, bq_offset, bkv_idx, head_l_ref, head_m_ref)` — [`L556`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L556)
- <a id="_mla_ragged_paged_attention_kernel.flash_attention_step2_pv"></a>`flash_attention_step2_pv(p, v, exp_m_diff, bkv_idx, head_acc_ref)` — [`L712`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L712)
- <a id="get_dtype_bitwidth"></a>`get_dtype_bitwidth(dtype)` — [`L76`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L76)
- <a id="get_dtype_packing"></a>`get_dtype_packing(dtype)` — [`L80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L80)
- <a id="get_kv_cache_shape"></a>`get_kv_cache_shape(total_num_pages, page_size, kv_dim, kv_dtype, kv_packing: int | None = None, transpose_kv_cache: bool = False)` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L85)
- <a id="_mla_ragged_paged_attention_kernel.process.get_next_bkv_ids"></a>`get_next_bkv_ids(seq_idx, bq_idx, bkv_idx, bkv_sem_idx)` — [`L1862`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1862)
- <a id="_mla_ragged_paged_attention_kernel.process.get_next_bq_ids"></a>`get_next_bq_ids(seq_idx, bq_idx, bq_sem_idx)` — [`L1854`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1854)
- <a id="_mla_ragged_paged_attention_kernel.load_batch_bkv"></a>`load_batch_bkv(load_bkv_fn, bkv_sem_idx)` — [`L1800`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1800)
- <a id="_mla_ragged_paged_attention_kernel.load_batch_bq"></a>`load_batch_bq(bq_sem_idx, *, actual_bq_sz=bq_sz)` — [`L1738`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1738)
- <a id="_mla_ragged_paged_attention_kernel.load_bkv"></a>`load_bkv(batch_item_idx, bkv_sem_idx)` — [`L1780`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1780)
- <a id="_mla_ragged_paged_attention_kernel.load_bq"></a>`load_bq(batch_item_idx, bq_sem_idx, *, actual_bq_sz=bq_sz)` — [`L1759`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1759)
- <a id="_mla_ragged_paged_attention_kernel.load_transposed_bkv"></a>`load_transposed_bkv(batch_item_idx, bkv_sem_idx)` — [`L1795`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1795)
- <a id="_mla_ragged_paged_attention_kernel.batch_flash_attention.load_with_init"></a>`load_with_init(ref, init_val)` — [`L480`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L480)
- <a id="_mla_ragged_paged_attention_kernel.flash_attention_step1_qk_softmax.load_with_init"></a>`load_with_init(ref, init_val)` — [`L588`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L588)
- <a id="_mla_ragged_paged_attention_kernel.flash_attention_step2_pv.load_with_init"></a>`load_with_init(ref, init_val)` — [`L719`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L719)
- <a id="_mla_ragged_paged_attention_kernel._update_transposed_kv_cache.loop_body"></a>`loop_body(i, states)` — [`L1402`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1402)
- <a id="_mla_ragged_paged_attention_kernel._update_kv_cache.loop_body"></a>`loop_body(i, states)` — [`L1520`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1520)
- <a id="mla_ragged_paged_attention"></a>`mla_ragged_paged_attention(ql_nope: jax.Array, q_pe: jax.Array, new_kv_c: jax.Array, new_k_pe: jax.Array, cache_kv: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, sm_scale: float = 1, sliding_window: int | None = None, soft_cap: float | None = None, mask_value: float | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, chunk_prefill_size: int | None = None, num_kv_pages_per_block: tuple[int, int, int] | int | None = None, num_queries_per_block: tuple[int, int, int] | int | None = None, vmem_limit_bytes: int | None = None, decode_batch_size: int = 1, mixed_q_split: int = 1, s_dtype: jnp.dtype = jnp.bfloat16, transpose_kv_cache: bool = False, two_step_flash_attention: bool = True, p_same_dtype_as_v: bool = True, use_causal_mask: bool = True, return_lse: bool = False, debug_mode: bool = False)` — [`L2317`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L2317) — MLA Ragged paged attention that supports mixed prefill and decode. — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.prefetch_next_bkv"></a>`prefetch_next_bkv()` — [`L1894`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1894)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq.prefetch_next_bq"></a>`prefetch_next_bq()` — [`L1881`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1881)
- <a id="prepare_kv_inputs"></a>`prepare_kv_inputs(kv: jax.Array, kv_packing: int)` — [`L2226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L2226)
- <a id="prepare_kv_inputs_for_transposed_kv_cache"></a>`prepare_kv_inputs_for_transposed_kv_cache(kv: jax.Array)` — [`L2241`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L2241)
- <a id="prepare_outputs"></a>`prepare_outputs(out, actual_num_q_heads: int, actual_max_num_tokens: int, actual_head_dim: int, vmem_limit_bytes: int | None = None)` — [`L2257`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L2257)
- <a id="prepare_q_inputs"></a>`prepare_q_inputs(q: jax.Array)` — [`L2157`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L2157)
- <a id="prepare_q_nope_inputs"></a>`prepare_q_nope_inputs(q: jax.Array, vmem_limit_bytes: int | None = None)` — [`L2175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L2175) — Packs and physically transposes q_nope to the layout expected by the MLA kernel.
- <a id="_mla_ragged_paged_attention_kernel.process"></a>`process()` — [`L1838`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1838)
- <a id="_mla_ragged_paged_attention_kernel.prologue"></a>`prologue()` — [`L2118`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L2118)
- <a id="mla_ragged_paged_attention.run_mla_kernel"></a>`run_mla_kernel(ql_nope: jax.Array, q_pe: jax.Array, new_kv_c: jax.Array, new_k_pe: jax.Array, cache_kv: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, start_seq_idx: jax.Array, end_seq_idx: jax.Array, static_q_len: int | None, lse: jax.Array | None, num_kv_pages_per_block: int, num_queries_per_block: int, s_dtype: jnp.dtype, p_same_dtype_as_v: bool, batch_size: int = 1, q_split: int = 1, case: MlaCase = MlaCase.MIXED)` — [`L2499`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L2499)
- <a id="_mla_ragged_paged_attention_kernel.start_fetch_bkv"></a>`start_fetch_bkv(batch_start_seq_idx, bkv_idx, bkv_sem_idx)` — [`L1672`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1672)
- <a id="_mla_ragged_paged_attention_kernel.start_fetch_bq"></a>`start_fetch_bq(batch_start_seq_idx, bq_idx, bq_sem_idx)` — [`L1678`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1678)
- <a id="_mla_ragged_paged_attention_kernel.start_send_bo"></a>`start_send_bo(batch_start_seq_idx, bo_idx, bo_sem_idx)` — [`L1684`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1684)
- <a id="_mla_ragged_paged_attention_kernel.start_update_kv_cache"></a>`start_update_kv_cache(start_seq_idx, bkv_sem_idx, offsets, update_szs)` — [`L1703`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1703)
- <a id="static_validate_inputs"></a>`static_validate_inputs(ql_nope: jax.Array, q_pe: jax.Array, new_kv_c: jax.Array, new_k_pe: jax.Array, cache_kv: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, sm_scale: float = 1, sliding_window: int | None = None, soft_cap: float | None = None, mask_value: float | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, chunk_prefill_size: int | None = None, num_kv_pages_per_blocks: Sequence[int] | None = None, num_queries_per_blocks: Sequence[int] | None = None, vmem_limit_bytes: int | None = None, decode_batch_size: int = 1, mixed_q_split: int = 1, transpose_kv_cache: bool = False, debug_mode: bool = False)` — [`L135`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L135) — Validate inputs to the MLA RPA kernel statically.
- <a id="unsigned_align_to"></a>`unsigned_align_to(a, b)` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L62)
- <a id="unsigned_cdiv"></a>`unsigned_cdiv(a, b)` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L46)
- <a id="unsigned_floor_div"></a>`unsigned_floor_div(a, b)` — [`L54`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L54)
- <a id="unsigned_mod"></a>`unsigned_mod(a, b)` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L38)
- <a id="_mla_ragged_paged_attention_kernel._pack_new_transposed_kv._update.update_body"></a>`update_body(idx, state)` — [`L1280`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1280)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.update_cur_bkv_to_cache"></a>`update_cur_bkv_to_cache()` — [`L1920`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1920)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv.wait_cur_bq"></a>`wait_cur_bq()` — [`L1900`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1900)
- <a id="_mla_ragged_paged_attention_kernel.wait_fetch_bkv"></a>`wait_fetch_bkv(batch_start_seq_idx, bkv_idx, bkv_sem_idx)` — [`L1675`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1675)
- <a id="_mla_ragged_paged_attention_kernel.wait_fetch_bq"></a>`wait_fetch_bq(batch_start_seq_idx, bq_idx, bq_sem_idx)` — [`L1681`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1681)
- <a id="_mla_ragged_paged_attention_kernel.wait_send_bo"></a>`wait_send_bo(bo_sem_idx)` — [`L1689`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1689)
- <a id="_mla_ragged_paged_attention_kernel.wait_update_kv_cache"></a>`wait_update_kv_cache(bkv_sem_idx)` — [`L1720`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L1720)

## Module values
- <a id="_XPOSE_N_TILE_SIZE"></a>`_XPOSE_N_TILE_SIZE` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L35)
- <a id="logger"></a>`logger` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/v2/kernel.py#L33)

