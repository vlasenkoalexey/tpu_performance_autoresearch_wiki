---
title: 'Module: src/vllm_torchtpu/kernels/mla/sparse/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/mla/sparse/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.mla.sparse.kernel`/
symbols:
  sparse_ragged_paged_attention: sparse_ragged_paged_attention().
  sparse_attention_chunk: sparse_attention_chunk().
  _attention_kernel.process: _attention_kernel().process().
  _attention_kernel.fixup_capped_overflow.fix_token._fix: _attention_kernel().fixup_capped_overflow().fix_token()._fix().
  _GATHER_PAGE_CHUNK: _GATHER_PAGE_CHUNK.
  _attention_kernel: _attention_kernel().
  _attention_kernel._async_copy: _attention_kernel()._async_copy().
  gather_page_ids: gather_page_ids().
  prepare_capped_window_indices: prepare_capped_window_indices().
  align_to: align_to().
  _attention_kernel.fixup_capped_overflow.fix_token._fix.window: _attention_kernel().fixup_capped_overflow().fix_token()._fix().window().
  prepare_q_inputs: prepare_q_inputs().
  GATHER_ATOM_ROWS: GATHER_ATOM_ROWS.
  _attention_kernel._send_blse_batch: _attention_kernel()._send_blse_batch().
  TENSORCORE_CACHE_LAYOUT: TENSORCORE_CACHE_LAYOUT.
  cdiv: cdiv().
  _capped_window_indices_kernel: _capped_window_indices_kernel().
  sparse_attention_chunk.run_mla_kernel: sparse_attention_chunk().run_mla_kernel().
  get_dtype_packing: get_dtype_packing().
  _attention_kernel.wait_send_bo_batch: _attention_kernel().wait_send_bo_batch().
  SPARSECORE_CACHE_LAYOUT: SPARSECORE_CACHE_LAYOUT.
  _attention_kernel.process.prefetch_next_seq: _attention_kernel().process().prefetch_next_seq().
  _attention_kernel.process._wait_send: _attention_kernel().process()._wait_send().
  _attention_kernel.prologue: _attention_kernel().prologue().
  _attention_kernel.epilogue: _attention_kernel().epilogue().
  _attention_kernel.epilogue._wait_1: _attention_kernel().epilogue()._wait_1().
  _attention_kernel._fetch_bkv_batch: _attention_kernel()._fetch_bkv_batch().
  _attention_kernel._fetch_bq_batch: _attention_kernel()._fetch_bq_batch().
  _attention_kernel._send_bo_batch: _attention_kernel()._send_bo_batch().
  _attention_kernel.start_fetch_bkv_batch: _attention_kernel().start_fetch_bkv_batch().
  _attention_kernel.start_fetch_bq_batch: _attention_kernel().start_fetch_bq_batch().
  _attention_kernel.process.write_blse: _attention_kernel().process().write_blse().
  _chunk_kernel_batch_size: _chunk_kernel_batch_size().
  prepare_gather_indices: prepare_gather_indices().
  _gather_page_ids_kernel: _gather_page_ids_kernel().
  _attention_kernel.wait_fetch_bkv_batch: _attention_kernel().wait_fetch_bkv_batch().
  _attention_kernel.wait_fetch_bq_batch: _attention_kernel().wait_fetch_bq_batch().
  _attention_kernel.start_send_bo_batch: _attention_kernel().start_send_bo_batch().
  _attention_kernel.load_bkv: _attention_kernel().load_bkv().
  _attention_kernel.fixup_capped_overflow: _attention_kernel().fixup_capped_overflow().
  DEFAULT_GATHER_AND_ATTENTION_CHUNK_SIZE: DEFAULT_GATHER_AND_ATTENTION_CHUNK_SIZE.
  DEFAULT_ATTENTION_KERNEL_BATCH_SIZE: DEFAULT_ATTENTION_KERNEL_BATCH_SIZE.
  _floor_divmod_const: _floor_divmod_const().
  _attention_kernel.unpack_bkv: _attention_kernel().unpack_bkv().
  _attention_kernel.fixup_capped_overflow.window_copies: _attention_kernel().fixup_capped_overflow().window_copies().
  _attention_kernel.fixup_capped_overflow.fix_token._fix.window._prefetch_next: _attention_kernel().fixup_capped_overflow().fix_token()._fix().window()._prefetch_next().
  DEFAULT_VMEM_LIMIT_BYTES: DEFAULT_VMEM_LIMIT_BYTES.
  prepare_capped_window_indices.token_block: prepare_capped_window_indices().token_block().
  _attention_kernel.attention_step2_pv: _attention_kernel().attention_step2_pv().
  _attention_kernel.load_bq: _attention_kernel().load_bq().
  _attention_kernel.store_blse: _attention_kernel().store_blse().
  _attention_kernel.fixup_capped_overflow.accumulate: _attention_kernel().fixup_capped_overflow().accumulate().
  get_dtype_bitwidth: get_dtype_bitwidth().
  _largest_divisor: _largest_divisor().
  capped_live_windows: capped_live_windows().
  _attention_kernel.attention_step1_qk_softmax: _attention_kernel().attention_step1_qk_softmax().
  _attention_kernel.fixup_capped_overflow.fix_token: _attention_kernel().fixup_capped_overflow().fix_token().
  _attention_kernel.process.get_next_seq_ids: _attention_kernel().process().get_next_seq_ids().
  prepare_outputs: prepare_outputs().
---
# Module: [`src/vllm_torchtpu/kernels/mla/sparse/kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py)

## Functions
- <a id="_attention_kernel._async_copy"></a>`_async_copy(src, dst, sem, wait)` — [`L577`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L577)
- <a id="_attention_kernel"></a>`_attention_kernel(kv_lens_ref, start_end_seq_idx_ref, sem_ids_ref, q_hbm_ref, cache_kv_nope_hbm_ref, cache_kv_rope_hbm_ref, *refs, sm_scale: float, k_scale: float = 1, batch_size: int = 1, preserve_suffix: bool = False, return_lse: bool = False, sparsecore_layout: bool = False, capped_windows: int | None = None, split_q: bool = False, lse_lane_dense: bool = False)` — [`L412`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L412)
- <a id="_capped_window_indices_kernel"></a>`_capped_window_indices_kernel(live_windows_ref, windows_ref, topk_ref, out_ref, *, block_tokens: int, chunk_size: int, topk: int, topk_cap: int, page_size: int, pages_per_seq: int, total_num_pages: int)` — [`L168`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L168) — Translates logical top-k slots to physical memory rows for one tile.
- <a id="_chunk_kernel_batch_size"></a>`_chunk_kernel_batch_size(chunk_size: int, attention_kernel_batch_size: int, small_chunk_tokens: int, small_chunk_batch_size: int | None)` — [`L999`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L999) — (is a small chunk, attention grid step) -- as `sparse_attention_chunk`.
- <a id="_attention_kernel._fetch_bkv_batch"></a>`_fetch_bkv_batch(seq_idx_start, bkv_sem_idx, *, wait=False)` — [`L584`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L584)
- <a id="_attention_kernel._fetch_bq_batch"></a>`_fetch_bq_batch(seq_idx_start, bq_sem_idx, *, wait=False)` — [`L613`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L613)
- <a id="_attention_kernel.fixup_capped_overflow.fix_token._fix"></a>`_fix()` — [`L826`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L826)
- <a id="_floor_divmod_const"></a>`_floor_divmod_const(x: jax.Array, d: int)` — [`L130`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L130) — Computes exact integer `(x // d, x % d)` without hardware integer division.
- <a id="_gather_page_ids_kernel"></a>`_gather_page_ids_kernel(windows_ref, logical_ref, out_ref, *, num_chunks)` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L67)
- <a id="_largest_divisor"></a>`_largest_divisor(x: int, cap: int)` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L56) — Largest divisor of ``x`` that is <= ``cap``.
- <a id="_attention_kernel.fixup_capped_overflow.fix_token._fix.window._prefetch_next"></a>`_prefetch_next()` — [`L849`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L849)
- <a id="_attention_kernel._send_blse_batch"></a>`_send_blse_batch(seq_idx_start, bo_sem_idx, *, wait=False)` — [`L665`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L665)
- <a id="_attention_kernel._send_bo_batch"></a>`_send_bo_batch(seq_idx_start, bo_sem_idx, *, wait=False)` — [`L639`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L639)
- <a id="_attention_kernel.epilogue._wait_1"></a>`_wait_1()` — [`L989`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L989)
- <a id="_attention_kernel.process._wait_send"></a>`_wait_send()` — [`L920`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L920)
- <a id="_attention_kernel.fixup_capped_overflow.accumulate"></a>`accumulate(q, kv, rem)` — [`L804`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L804)
- <a id="align_to"></a>`align_to(x, a)` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L43)
- <a id="_attention_kernel.attention_step1_qk_softmax"></a>`attention_step1_qk_softmax(q, kv, kv_len)` — [`L522`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L522)
- <a id="_attention_kernel.attention_step2_pv"></a>`attention_step2_pv(p, kv, l_sum)` — [`L556`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L556)
- <a id="capped_live_windows"></a>`capped_live_windows(kv_lens: jax.Array, token_end: jax.Array, *, chunk_size: int, kernel_batch_size: int, topk_cap: int, num_windows: int)` — [`L351`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L351) — Calculates how many `topk_cap` (512-slot) windows the capped path must process.
- <a id="cdiv"></a>`cdiv(a, b)` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L38)
- <a id="_attention_kernel.epilogue"></a>`epilogue()` — [`L980`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L980)
- <a id="_attention_kernel.fixup_capped_overflow.fix_token"></a>`fix_token(batch_idx, carry)` — [`L821`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L821)
- <a id="_attention_kernel.fixup_capped_overflow"></a>`fixup_capped_overflow(bi_sem_idx, bo_sem_idx)` — [`L771`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L771) — Recompute tokens with more than `bkv_sz` live rows (capped mode).
- <a id="gather_page_ids"></a>`gather_page_ids(page_indices: jax.Array, seq_page_ids: jax.Array, seq_ids_segment: jax.Array, max_num_seqs: int, *, block_tokens: int = 8)` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L82) — Gathers physical page ids for the CSA top-k tokens.
- <a id="get_dtype_bitwidth"></a>`get_dtype_bitwidth(dtype)` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L47)
- <a id="get_dtype_packing"></a>`get_dtype_packing(dtype)` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L51)
- <a id="_attention_kernel.process.get_next_seq_ids"></a>`get_next_seq_ids(seq_idx, bi_sem_idx)` — [`L881`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L881)
- <a id="_attention_kernel.load_bkv"></a>`load_bkv(bkv_sem_idx, batch_idx)` — [`L731`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L731)
- <a id="_attention_kernel.load_bq"></a>`load_bq(bq_sem_idx, batch_idx)` — [`L698`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L698)
- <a id="_attention_kernel.process.prefetch_next_seq"></a>`prefetch_next_seq()` — [`L893`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L893)
- <a id="prepare_capped_window_indices"></a>`prepare_capped_window_indices(topk_indices: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, live_windows: jax.Array, *, chunk_size: int, topk_cap: int, page_size: int, total_num_pages: int, block_tokens: int | None = None)` — [`L236`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L236) — Launches the TPU kernel to translate logical slots to physical rows. — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- <a id="prepare_gather_indices"></a>`prepare_gather_indices(topk_indices: jax.Array, page_indices: jax.Array | None, cu_q_lens: jax.Array, *, page_size: int, total_num_pages: int)` — [`L1397`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L1397) — Per-token valid top-k counts and flat cache row indices to gather.
- <a id="prepare_outputs"></a>`prepare_outputs(out, actual_num_q_heads: int, actual_head_dim: int)` — [`L1032`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L1032)
- <a id="prepare_q_inputs"></a>`prepare_q_inputs(q: jax.Array)` — [`L1013`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L1013)
- <a id="_attention_kernel.process"></a>`process()` — [`L880`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L880) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- <a id="_attention_kernel.prologue"></a>`prologue()` — [`L973`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L973)
- <a id="sparse_attention_chunk.run_mla_kernel"></a>`run_mla_kernel(q: jax.Array, cache_kv_nope: jax.Array, cache_kv_rope: jax.Array, kv_lens: jax.Array, start_seq_idx: int, end_seq_idx: jax.Array, kernel_batch_size: int, lse: jax.Array | None = None)` — [`L1529`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L1529)
- <a id="sparse_attention_chunk"></a>`sparse_attention_chunk(q: jax.Array, cache_kv_nope: jax.Array, cache_kv_rope: jax.Array, kv_lens: jax.Array, physical_indices: jax.Array | None, lse: jax.Array | None, *, start_pos: int, end_pos: int, token_end: jax.Array, sm_scale: float, k_scale: float, preserve_suffix: bool = False, attention_kernel_batch_size: int = DEFAULT_ATTENTION_KERNEL_BATCH_SIZE, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES, cache_layout: str = TENSORCORE_CACHE_LAYOUT, sparsecore_atoms_per_batch: int = 16, sparsecore_gather_wait_mode: str = "overlap_rope", sparsecore_gather_pipelined: bool = True, small_chunk_tokens: int = 0, small_chunk_batch_size: int | None = None, small_chunk_live_gather: bool = False, small_chunk_gather_atoms: int = 1, live_gather_all_chunks: bool = False, topk_cap: int | None = None, topk_override: int | None = None, window_indices: jax.Array | None = None, q_pe: jax.Array | None = None, lse_lane_dense: bool = False)` — [`L1449`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L1449) — Gathers and attends query rows `[start_pos, min(end_pos, token_end))`. — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- <a id="sparse_ragged_paged_attention"></a>`sparse_ragged_paged_attention(q: jax.Array, cache_kv_nope: jax.Array, cache_kv_rope: jax.Array, topk_indices: jax.Array, page_indices: jax.Array | None, cu_q_lens: jax.Array, distribution: jax.Array, *, sm_scale: float = 1, k_scale: float = 1, gather_and_attention_chunk_size: int = DEFAULT_GATHER_AND_ATTENTION_CHUNK_SIZE, attention_kernel_batch_size: int = DEFAULT_ATTENTION_KERNEL_BATCH_SIZE, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES, return_lse: bool = False, cache_layout: str = TENSORCORE_CACHE_LAYOUT, sparsecore_atoms_per_batch: int = 16, sparsecore_gather_wait_mode: str = "overlap_rope", sparsecore_gather_pipelined: bool = True, small_chunk_tokens: int = 16, small_chunk_batch_size: int | None = 1, small_chunk_live_gather: bool = True, small_chunk_gather_atoms: int = 1, live_gather_all_chunks: bool = True, topk_cap: int | None = None, q_pe: jax.Array | None = None, lse_lane_dense: bool = False)` — [`L1066`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L1066) — MLA Ragged paged attention that supports mixed prefill and decode. — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)
- <a id="_attention_kernel.start_fetch_bkv_batch"></a>`start_fetch_bkv_batch(seq_idx_start, bkv_sem_idx)` — [`L680`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L680)
- <a id="_attention_kernel.start_fetch_bq_batch"></a>`start_fetch_bq_batch(seq_idx_start, bq_sem_idx)` — [`L686`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L686)
- <a id="_attention_kernel.start_send_bo_batch"></a>`start_send_bo_batch(seq_idx_start, bo_sem_idx)` — [`L692`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L692)
- <a id="_attention_kernel.store_blse"></a>`store_blse(bo_sem_idx, batch_idx, lse_col)` — [`L707`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L707) — Stores one token's f32[num_q_heads, 1] log-sum-exp column.
- <a id="prepare_capped_window_indices.token_block"></a>`token_block(w, c, tb, lw)` — [`L303`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L303)
- <a id="_attention_kernel.unpack_bkv"></a>`unpack_bkv(bkv_nope_ref, bkv_rope_ref, get_kv_len)` — [`L738`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L738)
- <a id="_attention_kernel.wait_fetch_bkv_batch"></a>`wait_fetch_bkv_batch(seq_idx_start, bkv_sem_idx)` — [`L683`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L683)
- <a id="_attention_kernel.wait_fetch_bq_batch"></a>`wait_fetch_bq_batch(seq_idx_start, bq_sem_idx)` — [`L689`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L689)
- <a id="_attention_kernel.wait_send_bo_batch"></a>`wait_send_bo_batch(seq_idx_start, bo_sem_idx)` — [`L695`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L695)
- <a id="_attention_kernel.fixup_capped_overflow.fix_token._fix.window"></a>`window(j, window_carry)` — [`L845`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L845)
- <a id="_attention_kernel.fixup_capped_overflow.window_copies"></a>`window_copies(local_idx, j, slot)` — [`L789`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L789)
- <a id="_attention_kernel.process.write_blse"></a>`write_blse(batch_idx, m, l_sum)` — [`L907`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L907)

## Module values
- <a id="DEFAULT_ATTENTION_KERNEL_BATCH_SIZE"></a>`DEFAULT_ATTENTION_KERNEL_BATCH_SIZE` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L33)
- <a id="DEFAULT_GATHER_AND_ATTENTION_CHUNK_SIZE"></a>`DEFAULT_GATHER_AND_ATTENTION_CHUNK_SIZE` — [`L32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L32)
- <a id="DEFAULT_VMEM_LIMIT_BYTES"></a>`DEFAULT_VMEM_LIMIT_BYTES` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L29)
- <a id="GATHER_ATOM_ROWS"></a>`GATHER_ATOM_ROWS` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L35)
- <a id="SPARSECORE_CACHE_LAYOUT"></a>`SPARSECORE_CACHE_LAYOUT` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L31)
- <a id="TENSORCORE_CACHE_LAYOUT"></a>`TENSORCORE_CACHE_LAYOUT` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L30)
- <a id="_GATHER_PAGE_CHUNK"></a>`_GATHER_PAGE_CHUNK` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/mla/sparse/kernel.py#L64) — documented in [mla-attention-kernels](../../../../../../concepts/mla-attention-kernels.md)

