---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.core_attention.sparse_mla`/
symbols:
  _attention_kernel.process: _attention_kernel().process().
  sparse_ragged_paged_attention: sparse_ragged_paged_attention().
  _attention_kernel._async_copy: _attention_kernel()._async_copy().
  align_to: align_to().
  gather_page_ids: gather_page_ids().
  sparse_ragged_paged_attention.run_mla_kernel: sparse_ragged_paged_attention().run_mla_kernel().
  _attention_kernel.process.prefetch_next_seq: _attention_kernel().process().prefetch_next_seq().
  _attention_kernel.prologue: _attention_kernel().prologue().
  _GATHER_PAGE_CHUNK: _GATHER_PAGE_CHUNK.
  get_dtype_packing: get_dtype_packing().
  _dequant_dsv4_fp8: _dequant_dsv4_fp8().
  prepare_q_inputs: prepare_q_inputs().
  prepare_swa_inputs: prepare_swa_inputs().
  _attention_kernel.wait_send_bo_batch: _attention_kernel().wait_send_bo_batch().
  cdiv: cdiv().
  get_kv_cache_shape: get_kv_cache_shape().
  _attention_kernel._fetch_bkv_batch: _attention_kernel()._fetch_bkv_batch().
  _attention_kernel._fetch_bq_batch: _attention_kernel()._fetch_bq_batch().
  _attention_kernel._send_bo_batch: _attention_kernel()._send_bo_batch().
  _attention_kernel._fetch_swa_batch: _attention_kernel()._fetch_swa_batch().
  _attention_kernel.start_fetch_bkv_batch: _attention_kernel().start_fetch_bkv_batch().
  _attention_kernel.start_fetch_bq_batch: _attention_kernel().start_fetch_bq_batch().
  _attention_kernel.start_fetch_swa_batch: _attention_kernel().start_fetch_swa_batch().
  _gather_page_ids_kernel: _gather_page_ids_kernel().
  _attention_kernel: _attention_kernel().
  _attention_kernel.wait_fetch_bkv_batch: _attention_kernel().wait_fetch_bkv_batch().
  _attention_kernel.wait_fetch_bq_batch: _attention_kernel().wait_fetch_bq_batch().
  _attention_kernel.wait_fetch_swa_batch: _attention_kernel().wait_fetch_swa_batch().
  _attention_kernel.start_send_bo_batch: _attention_kernel().start_send_bo_batch().
  _attention_kernel.load_bkv: _attention_kernel().load_bkv().
  _attention_kernel.process._wait_send: _attention_kernel().process()._wait_send().
  _attention_kernel._process_full: _attention_kernel()._process_full().
  _attention_kernel._process_masked: _attention_kernel()._process_masked().
  _attention_kernel.epilogue: _attention_kernel().epilogue().
  _attention_kernel.epilogue._wait_1: _attention_kernel().epilogue()._wait_1().
  NOPE_DIM: NOPE_DIM.
  NOPE_SCALE_PERIOD: NOPE_SCALE_PERIOD.
  _attention_kernel.flash_attention_step2_pv: _attention_kernel().flash_attention_step2_pv().
  DEFAULT_VMEM_LIMIT_BYTES: DEFAULT_VMEM_LIMIT_BYTES.
  get_dtype_bitwidth: get_dtype_bitwidth().
  _largest_divisor: _largest_divisor().
  _attention_kernel.flash_attention_step1_qk_softmax: _attention_kernel().flash_attention_step1_qk_softmax().
  _attention_kernel.load_bq: _attention_kernel().load_bq().
  _attention_kernel.load_swa_output: _attention_kernel().load_swa_output().
  _attention_kernel.process.get_next_seq_ids: _attention_kernel().process().get_next_seq_ids().
  prepare_outputs: prepare_outputs().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py)

## Functions
- <a id="_attention_kernel._async_copy"></a>`_async_copy(src, dst, sem, wait)` — [`L280`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L280)
- <a id="_attention_kernel"></a>`_attention_kernel(kv_lens_ref, start_end_seq_idx_ref, sem_ids_ref, bo_ids_ref, attention_sinks_ref, q_hbm_ref, cache_kv_nope_hbm_ref, cache_kv_rope_hbm_ref, swa_accumution_hbm_ref, swa_l_hbm_ref, swa_m_hbm_ref, o_hbm_ref, bkv_nope_x2_ref, bkv_rope_x2_ref, bq_x2_ref, bo_x2_ref, bl_x2_ref, bm_x2_ref, swa_acc_x2_ref, sems, *, sm_scale: float, batch_size: int = 1)` — [`L171`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L171)
- <a id="_dequant_dsv4_fp8"></a>`_dequant_dsv4_fp8(words: jax.Array)` — [`L144`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L144) — Dequantize gathered NoPE records to BF16 [rows, NOPE_DIM].
- <a id="_attention_kernel._fetch_bkv_batch"></a>`_fetch_bkv_batch(seq_idx_start, bkv_sem_idx, *, wait=False)` — [`L287`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L287)
- <a id="_attention_kernel._fetch_bq_batch"></a>`_fetch_bq_batch(seq_idx_start, bq_sem_idx, *, wait=False)` — [`L316`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L316)
- <a id="_attention_kernel._fetch_swa_batch"></a>`_fetch_swa_batch(seq_idx_start, bq_sem_idx, *, wait=False)` — [`L348`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L348)
- <a id="_gather_page_ids_kernel"></a>`_gather_page_ids_kernel(windows_ref, logical_ref, out_ref, *, num_chunks)` — [`L73`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L73)
- <a id="_largest_divisor"></a>`_largest_divisor(x: int, cap: int)` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L62) — Largest divisor of ``x`` that is <= ``cap``.
- <a id="_attention_kernel._process_full"></a>`_process_full()` — [`L561`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L561)
- <a id="_attention_kernel._process_masked"></a>`_process_masked()` — [`L565`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L565)
- <a id="_attention_kernel._send_bo_batch"></a>`_send_bo_batch(seq_idx_start, bo_sem_idx, *, wait=False)` — [`L330`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L330)
- <a id="_attention_kernel.epilogue._wait_1"></a>`_wait_1()` — [`L573`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L573)
- <a id="_attention_kernel.process._wait_send"></a>`_wait_send()` — [`L488`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L488)
- <a id="align_to"></a>`align_to(x, a)` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L34)
- <a id="cdiv"></a>`cdiv(a, b)` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L29)
- <a id="_attention_kernel.epilogue"></a>`epilogue()` — [`L569`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L569)
- <a id="_attention_kernel.flash_attention_step1_qk_softmax"></a>`flash_attention_step1_qk_softmax(q, kv, kv_len, swa_m, swa_l, attention_sinks, masked)` — [`L227`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L227)
- <a id="_attention_kernel.flash_attention_step2_pv"></a>`flash_attention_step2_pv(p, kv, exp_m_diff, swa_acc, l_total)` — [`L262`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L262)
- <a id="gather_page_ids"></a>`gather_page_ids(page_indices: jax.Array, seq_page_ids: jax.Array, seq_ids_segment: jax.Array, max_num_seqs: int, *, block_tokens: int = 8)` — [`L88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L88) — Gathers physical page ids for the CSA top-k tokens.
- <a id="get_dtype_bitwidth"></a>`get_dtype_bitwidth(dtype)` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L38)
- <a id="get_dtype_packing"></a>`get_dtype_packing(dtype)` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L42)
- <a id="get_kv_cache_shape"></a>`get_kv_cache_shape(total_num_pages, page_size, kv_dim, kv_dtype)` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L47)
- <a id="_attention_kernel.process.get_next_seq_ids"></a>`get_next_seq_ids(seq_idx, bi_sem_idx)` — [`L453`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L453)
- <a id="_attention_kernel.load_bkv"></a>`load_bkv(bkv_sem_idx, batch_idx, masked)` — [`L417`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L417)
- <a id="_attention_kernel.load_bq"></a>`load_bq(bq_sem_idx, batch_idx)` — [`L413`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L413)
- <a id="_attention_kernel.load_swa_output"></a>`load_swa_output(bq_sem_idx, batch_idx)` — [`L446`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L446)
- <a id="_attention_kernel.process.prefetch_next_seq"></a>`prefetch_next_seq()` — [`L465`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L465)
- <a id="prepare_outputs"></a>`prepare_outputs(out, actual_num_q_heads: int, actual_head_dim: int)` — [`L636`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L636)
- <a id="prepare_q_inputs"></a>`prepare_q_inputs(q: jax.Array)` — [`L579`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L579)
- <a id="prepare_swa_inputs"></a>`prepare_swa_inputs(swa_accumution: jax.Array, swa_l: jax.Array, swa_m: jax.Array)` — [`L598`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L598)
- <a id="_attention_kernel.process"></a>`process(masked)` — [`L452`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L452)
- <a id="_attention_kernel.prologue"></a>`prologue()` — [`L546`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L546)
- <a id="sparse_ragged_paged_attention.run_mla_kernel"></a>`run_mla_kernel(q: jax.Array, cache_kv_nope: jax.Array, cache_kv_rope: jax.Array, kv_lens: jax.Array, attention_sinks: jax.Array, swa_accumution: jax.Array, swa_l: jax.Array, swa_m: jax.Array, start_seq_idx: int, end_seq_idx: jax.Array, num_valid_tokens: jax.Array, kernel_batch_size: int)` — [`L722`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L722)
- <a id="sparse_ragged_paged_attention"></a>`sparse_ragged_paged_attention(q: jax.Array, cache_kv_nope: jax.Array, cache_kv_rope: jax.Array, topk_indices: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, attention_sinks: jax.Array, swa_accumution: jax.Array, swa_l: jax.Array, swa_m: jax.Array, *, sm_scale: float = 1, gather_and_attention_chunk_size: int = 128, attention_kernel_batch_size: int = 16, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES)` — [`L657`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L657) — MLA Ragged paged attention that supports mixed prefill and decode. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
- <a id="_attention_kernel.start_fetch_bkv_batch"></a>`start_fetch_bkv_batch(seq_idx_start, bkv_sem_idx)` — [`L383`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L383)
- <a id="_attention_kernel.start_fetch_bq_batch"></a>`start_fetch_bq_batch(seq_idx_start, bq_sem_idx)` — [`L389`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L389)
- <a id="_attention_kernel.start_fetch_swa_batch"></a>`start_fetch_swa_batch(seq_idx_start, bq_sem_idx)` — [`L395`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L395)
- <a id="_attention_kernel.start_send_bo_batch"></a>`start_send_bo_batch(seq_idx_start, bo_sem_idx)` — [`L401`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L401)
- <a id="_attention_kernel.wait_fetch_bkv_batch"></a>`wait_fetch_bkv_batch(seq_idx_start, bkv_sem_idx)` — [`L386`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L386)
- <a id="_attention_kernel.wait_fetch_bq_batch"></a>`wait_fetch_bq_batch(seq_idx_start, bq_sem_idx)` — [`L392`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L392)
- <a id="_attention_kernel.wait_fetch_swa_batch"></a>`wait_fetch_swa_batch(seq_idx_start, bq_sem_idx)` — [`L398`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L398)
- <a id="_attention_kernel.wait_send_bo_batch"></a>`wait_send_bo_batch(bo_sem_idx)` — [`L404`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L404)

## Module values
- <a id="DEFAULT_VMEM_LIMIT_BYTES"></a>`DEFAULT_VMEM_LIMIT_BYTES` — [`L26`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L26)
- <a id="NOPE_DIM"></a>`NOPE_DIM` — [`L140`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L140)
- <a id="NOPE_SCALE_PERIOD"></a>`NOPE_SCALE_PERIOD` — [`L141`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L141)
- <a id="_GATHER_PAGE_CHUNK"></a>`_GATHER_PAGE_CHUNK` — [`L70`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/core_attention/sparse_mla.py#L70)

