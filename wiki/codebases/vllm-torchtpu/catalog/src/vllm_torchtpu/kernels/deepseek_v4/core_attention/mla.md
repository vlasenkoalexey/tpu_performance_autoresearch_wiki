---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.core_attention.mla`/
symbols:
  mla_ragged_paged_attention: mla_ragged_paged_attention().
  mla_ragged_paged_attention.run_mla_kernel: mla_ragged_paged_attention().run_mla_kernel().
  _mla_ragged_paged_attention_kernel.process.compute_with_bq: _mla_ragged_paged_attention_kernel().process().compute_with_bq().
  _mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv: _mla_ragged_paged_attention_kernel().process().compute_with_bq().compute_with_bkv().
  MlaCase.symbol: MlaCase#symbol().
  MlaCase: MlaCase#
  align_to: align_to().
  _mla_ragged_paged_attention_kernel.prologue: _mla_ragged_paged_attention_kernel().prologue().
  _mla_ragged_paged_attention_kernel._async_copy: _mla_ragged_paged_attention_kernel()._async_copy().
  get_dtype_packing: get_dtype_packing().
  _mla_ragged_paged_attention_kernel: _mla_ragged_paged_attention_kernel().
  _mla_ragged_paged_attention_kernel.process: _mla_ragged_paged_attention_kernel().process().
  prepare_q_inputs: prepare_q_inputs().
  prepare_swa_inputs: prepare_swa_inputs().
  _mla_ragged_paged_attention_kernel.process.compute_with_bq.prefetch_next_bq: _mla_ragged_paged_attention_kernel().process().compute_with_bq().prefetch_next_bq().
  _mla_ragged_paged_attention_kernel._fetch_bkv: _mla_ragged_paged_attention_kernel()._fetch_bkv().
  _mla_ragged_paged_attention_kernel.start_fetch_bkv: _mla_ragged_paged_attention_kernel().start_fetch_bkv().
  _mla_ragged_paged_attention_kernel.start_fetch_bq: _mla_ragged_paged_attention_kernel().start_fetch_bq().
  _mla_ragged_paged_attention_kernel.start_fetch_swa: _mla_ragged_paged_attention_kernel().start_fetch_swa().
  _mla_ragged_paged_attention_kernel.wait_send_bo: _mla_ragged_paged_attention_kernel().wait_send_bo().
  cdiv: cdiv().
  _mla_ragged_paged_attention_kernel.wait_fetch_bkv: _mla_ragged_paged_attention_kernel().wait_fetch_bkv().
  _mla_ragged_paged_attention_kernel.wait_fetch_bq: _mla_ragged_paged_attention_kernel().wait_fetch_bq().
  _mla_ragged_paged_attention_kernel.wait_fetch_swa: _mla_ragged_paged_attention_kernel().wait_fetch_swa().
  _mla_ragged_paged_attention_kernel.start_send_bo: _mla_ragged_paged_attention_kernel().start_send_bo().
  MlaCase.MIXED: MlaCase#MIXED.
  _mla_ragged_paged_attention_kernel._fetch_bq._copy: _mla_ragged_paged_attention_kernel()._fetch_bq()._copy().
  _mla_ragged_paged_attention_kernel._send_bo._copy: _mla_ragged_paged_attention_kernel()._send_bo()._copy().
  _mla_ragged_paged_attention_kernel._fetch_swa._copy_swa: _mla_ragged_paged_attention_kernel()._fetch_swa()._copy_swa().
  _mla_ragged_paged_attention_kernel.epilogue: _mla_ragged_paged_attention_kernel().epilogue().
  get_dtype_bitwidth: get_dtype_bitwidth().
  MlaCase.DECODE: MlaCase#DECODE.
  MlaCase.PREFILL: MlaCase#PREFILL.
  MlaCase.BATCHED_DECODE: MlaCase#BATCHED_DECODE.
  _mla_ragged_paged_attention_kernel._fetch_bq: _mla_ragged_paged_attention_kernel()._fetch_bq().
  _mla_ragged_paged_attention_kernel._send_bo: _mla_ragged_paged_attention_kernel()._send_bo().
  _mla_ragged_paged_attention_kernel._fetch_swa: _mla_ragged_paged_attention_kernel()._fetch_swa().
  mla_ragged_paged_attention.skip_if_empty: mla_ragged_paged_attention().skip_if_empty().
  DEFAULT_VMEM_LIMIT_BYTES: DEFAULT_VMEM_LIMIT_BYTES.
  _mla_ragged_paged_attention_kernel.flash_attention: _mla_ragged_paged_attention_kernel().flash_attention().
  _mla_ragged_paged_attention_kernel.load_bq: _mla_ragged_paged_attention_kernel().load_bq().
  _mla_ragged_paged_attention_kernel.load_bkv: _mla_ragged_paged_attention_kernel().load_bkv().
  _mla_ragged_paged_attention_kernel.process.get_next_bq_ids: _mla_ragged_paged_attention_kernel().process().get_next_bq_ids().
  _mla_ragged_paged_attention_kernel.process.get_next_bkv_ids: _mla_ragged_paged_attention_kernel().process().get_next_bkv_ids().
  prepare_outputs: prepare_outputs().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py)

## Classes
### <a id="MlaCase"></a>`MlaCase`  ·  implements/extends Enum
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py:46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L46)
- doc: Represents the different cases for MLA.
- signature: `class MlaCase(Enum):`
- members:
  - <a id="MlaCase.symbol"></a>`symbol(self)` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L61)
  - <a id="MlaCase.BATCHED_DECODE"></a>`BATCHED_DECODE` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L58)
  - <a id="MlaCase.DECODE"></a>`DECODE` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L55)
  - <a id="MlaCase.MIXED"></a>`MIXED` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L57)
  - <a id="MlaCase.PREFILL"></a>`PREFILL` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L56)
- used by: [`mla_ragged_paged_attention`](mla.md#mla_ragged_paged_attention), [`run_mla_kernel`](mla.md#mla_ragged_paged_attention.run_mla_kernel)

## Functions
- <a id="_mla_ragged_paged_attention_kernel._async_copy"></a>`_async_copy(src, dst, sem, wait)` — [`L180`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L180)
- <a id="_mla_ragged_paged_attention_kernel._fetch_bq._copy"></a>`_copy(q_len_start=q_len_start, sz=sz, bq_vmem_ref=bq_vmem_ref, sem=sem)` — [`L263`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L263)
- <a id="_mla_ragged_paged_attention_kernel._send_bo._copy"></a>`_copy(vmem_ref=vmem_ref, sz=sz, q_len_start=q_len_start, sem=sem)` — [`L287`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L287)
- <a id="_mla_ragged_paged_attention_kernel._fetch_swa._copy_swa"></a>`_copy_swa(q_len_start=q_len_start, sz=sz, b=b, sem_acc=sem_acc, sem_l=sem_l, sem_m=sem_m)` — [`L312`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L312)
- <a id="_mla_ragged_paged_attention_kernel._fetch_bkv"></a>`_fetch_bkv(batch_start_seq_idx, bkv_idx, bkv_sem_idx, *, wait=False, enabled=True)` — [`L187`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L187)
- <a id="_mla_ragged_paged_attention_kernel._fetch_bq"></a>`_fetch_bq(batch_start_seq_idx, bq_idx, bq_sem_idx, *, wait=False)` — [`L252`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L252)
- <a id="_mla_ragged_paged_attention_kernel._fetch_swa"></a>`_fetch_swa(batch_start_seq_idx, bq_idx, bq_sem_idx, *, wait=False)` — [`L300`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L300)
- <a id="_mla_ragged_paged_attention_kernel"></a>`_mla_ragged_paged_attention_kernel(kv_lens_ref, kv_lens_to_attend_ref, page_indices_ref, cu_q_lens_ref, start_end_seq_idx_ref, sem_ids_ref, bo_ids_ref, attention_sinks_ref, q_hbm_ref, cache_kv_hbm_ref, swa_accumution_hbm_ref, swa_l_hbm_ref, swa_m_hbm_ref, o_hbm_ref, bkv_x2_ref, bq_x2_ref, bo_x2_ref, bl_x2_ref, bm_x2_ref, swa_acc_x2_ref, sems, l_ref, m_ref, acc_ref, *, static_q_len: int | None, sm_scale: float, bkv_p, bq_sz, batch_size: int = 1)` — [`L70`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L70)
- <a id="_mla_ragged_paged_attention_kernel._send_bo"></a>`_send_bo(batch_start_seq_idx, bo_idx, bo_sem_idx, *, wait=False)` — [`L276`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L276)
- <a id="align_to"></a>`align_to(x, a)` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L33)
- <a id="cdiv"></a>`cdiv(a, b)` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L28)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq.compute_with_bkv"></a>`compute_with_bkv(bkv_idx, carry)` — [`L505`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L505)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq"></a>`compute_with_bq(bq_idx, _)` — [`L470`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L470)
- <a id="_mla_ragged_paged_attention_kernel.epilogue"></a>`epilogue()` — [`L610`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L610)
- <a id="_mla_ragged_paged_attention_kernel.flash_attention"></a>`flash_attention(q, kv, *, bq_idx, bkv_idx, kv_lens_to_attend_segment)` — [`L137`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L137)
- <a id="get_dtype_bitwidth"></a>`get_dtype_bitwidth(dtype)` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L37)
- <a id="get_dtype_packing"></a>`get_dtype_packing(dtype)` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L41)
- <a id="_mla_ragged_paged_attention_kernel.process.get_next_bkv_ids"></a>`get_next_bkv_ids(seq_idx, bq_idx, bkv_idx, bkv_sem_idx)` — [`L459`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L459)
- <a id="_mla_ragged_paged_attention_kernel.process.get_next_bq_ids"></a>`get_next_bq_ids(seq_idx, bq_idx, bq_sem_idx)` — [`L451`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L451)
- <a id="_mla_ragged_paged_attention_kernel.load_bkv"></a>`load_bkv(bkv_sem_idx, bkv_idx)` — [`L415`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L415)
- <a id="_mla_ragged_paged_attention_kernel.load_bq"></a>`load_bq(bq_sem_idx)` — [`L403`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L403)
- <a id="mla_ragged_paged_attention"></a>`mla_ragged_paged_attention(q: jax.Array, cache_kv: jax.Array, kv_lens: jax.Array, kv_lens_to_attend: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, attention_sinks: jax.Array, swa_accumution: jax.Array, swa_l: jax.Array, swa_m: jax.Array, *, sm_scale: float = 1, chunk_prefill_size: int | None = None, num_kv_pages_per_block: tuple[int, int, int] | int | None = None, num_queries_per_block: tuple[int, int, int] | int | None = None, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES, decode_batch_size: int = 8)` — [`L710`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L710) — MLA Ragged paged attention that supports mixed prefill and decode. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
- <a id="_mla_ragged_paged_attention_kernel.process.compute_with_bq.prefetch_next_bq"></a>`prefetch_next_bq()` — [`L500`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L500)
- <a id="prepare_outputs"></a>`prepare_outputs(out, actual_num_q_heads: int, actual_head_dim: int)` — [`L674`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L674)
- <a id="prepare_q_inputs"></a>`prepare_q_inputs(q: jax.Array)` — [`L617`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L617)
- <a id="prepare_swa_inputs"></a>`prepare_swa_inputs(swa_accumution: jax.Array, swa_l: jax.Array, swa_m: jax.Array)` — [`L636`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L636)
- <a id="_mla_ragged_paged_attention_kernel.process"></a>`process()` — [`L426`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L426)
- <a id="_mla_ragged_paged_attention_kernel.prologue"></a>`prologue()` — [`L596`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L596)
- <a id="mla_ragged_paged_attention.run_mla_kernel"></a>`run_mla_kernel(q: jax.Array, cache_kv: jax.Array, kv_lens: jax.Array, kv_lens_to_attend: jax.Array | None, page_indices: jax.Array, cu_q_lens: jax.Array, attention_sinks: jax.Array, swa_accumution: jax.Array, swa_l: jax.Array, swa_m: jax.Array, start_seq_idx: jax.Array, end_seq_idx: jax.Array, static_q_len: int | None, num_kv_pages_per_block: int, num_queries_per_block: int, batch_size: int = 1, case: MlaCase = MlaCase.MIXED)` — [`L797`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L797)
- <a id="mla_ragged_paged_attention.skip_if_empty"></a>`skip_if_empty(start_seq_idx, end_seq_idx, run)` — [`L949`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L949)
- <a id="_mla_ragged_paged_attention_kernel.start_fetch_bkv"></a>`start_fetch_bkv(batch_start_seq_idx, bkv_idx, bkv_sem_idx, enabled=True)` — [`L367`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L367)
- <a id="_mla_ragged_paged_attention_kernel.start_fetch_bq"></a>`start_fetch_bq(batch_start_seq_idx, bq_idx, bq_sem_idx)` — [`L373`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L373)
- <a id="_mla_ragged_paged_attention_kernel.start_fetch_swa"></a>`start_fetch_swa(batch_start_seq_idx, bq_idx, bq_sem_idx)` — [`L379`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L379)
- <a id="_mla_ragged_paged_attention_kernel.start_send_bo"></a>`start_send_bo(batch_start_seq_idx, bo_idx, bo_sem_idx)` — [`L385`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L385)
- <a id="_mla_ragged_paged_attention_kernel.wait_fetch_bkv"></a>`wait_fetch_bkv(batch_start_seq_idx, bkv_idx, bkv_sem_idx)` — [`L370`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L370)
- <a id="_mla_ragged_paged_attention_kernel.wait_fetch_bq"></a>`wait_fetch_bq(batch_start_seq_idx, bq_idx, bq_sem_idx)` — [`L376`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L376)
- <a id="_mla_ragged_paged_attention_kernel.wait_fetch_swa"></a>`wait_fetch_swa(batch_start_seq_idx, bq_idx, bq_sem_idx)` — [`L382`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L382)
- <a id="_mla_ragged_paged_attention_kernel.wait_send_bo"></a>`wait_send_bo(bo_sem_idx)` — [`L390`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L390)

## Module values
- <a id="DEFAULT_VMEM_LIMIT_BYTES"></a>`DEFAULT_VMEM_LIMIT_BYTES` — [`L25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/mla.py#L25)

