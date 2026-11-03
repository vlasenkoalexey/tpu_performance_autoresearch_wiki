---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.streamindex_topk.kv_cache_append`/
symbols:
  _LANES: _LANES.
  _KV_PACKING: _KV_PACKING.
  scatter_rows: scatter_rows().
  check_scatter_rows_supported: check_scatter_rows_supported().
  _SalTiles.blend: _SalTiles#blend().
  KVLayout: KVLayout.
  scatter_rows_reference: scatter_rows_reference().
  _SalTiles.move_token: _SalTiles#move_token().
  cache_page_size: cache_page_size().
  _SalTiles._src_tile: _SalTiles#_src_tile().
  coalesced_kv_append: coalesced_kv_append().
  coalesced_kv_append_dcp: coalesced_kv_append_dcp().
  _sal_kernel: _sal_kernel().
  _sal_launch: _sal_launch().
  _SalTiles._write: _SalTiles#_write().
  _find_runs: _find_runs().
  _write_runs: _write_runs().
  _HasQuads.blend: _HasQuads#blend().
  _has_launch: _has_launch().
  _write_runs._wave: _write_runs()._wave().
  _format_rows: _format_rows().
  _SalTiles.k: _SalTiles#k.
  _SalTiles._cache_lanes: _SalTiles#_cache_lanes().
  _has_kernel: _has_kernel().
  _HasQuads.granule_copy: _HasQuads#granule_copy().
  _SalTiles.rec_dim: _SalTiles#rec_dim.
  _sal_kernel._transpose: _sal_kernel()._transpose().
  _SalTiles.granule_copy: _SalTiles#granule_copy().
  _find_runs._step: _find_runs()._step().
  _write_runs._wave._for_each: _write_runs()._wave()._for_each().
  _check_vmem: _check_vmem().
  _align_to: _align_to().
  _HasQuads.k: _HasQuads#k.
  _HasQuads.move_token: _HasQuads#move_token().
  _SalTiles.sublane_groups: _SalTiles#sublane_groups.
  _write_runs._wave._blend_and_start_write: _write_runs()._wave()._blend_and_start_write().
  _SalTiles: _SalTiles#
  _HasQuads.granule: _HasQuads#granule.
  _write_runs._wave._reads: _write_runs()._wave()._reads().
  _sal_kernel._ensure_blocks_transposed: _sal_kernel()._ensure_blocks_transposed().
  _MAX_TOKENS: _MAX_TOKENS.
  _HasQuads.rmw: _HasQuads#rmw.
  _SalTiles.padded_tokens: _SalTiles#padded_tokens.
  _SalTiles.short_run_fast_path: _SalTiles#short_run_fast_path.
  _HasQuads.cache: _HasQuads#cache.
  _find_runs._chunk: _find_runs()._chunk().
  _write_runs._wave._reads._fn: _write_runs()._wave()._reads()._fn().
  _write_runs._wave._wait_write: _write_runs()._wave()._wait_write().
  _MAX_SAFE_VMEM_BYTES: _MAX_SAFE_VMEM_BYTES.
  _HasQuads: _HasQuads#
  _SalTiles.rmw: _SalTiles#rmw.
  _SalTiles.granule: _SalTiles#granule.
  _MAX_WAVE: _MAX_WAVE.
  _SalTiles.page_size: _SalTiles#page_size.
  _SalTiles._ensure_blocks_transposed: _SalTiles#_ensure_blocks_transposed.
  _run_table_shapes: _run_table_shapes().
  _blend_token_into_quad: _blend_token_into_quad().
  _HasQuads.num_src_quads: _HasQuads#num_src_quads.
  _HasQuads.lkv_dim: _HasQuads#lkv_dim.
  _SalTiles.cache: _SalTiles#cache.
  _write_runs._wave._for_each._body: _write_runs()._wave()._for_each()._body().
  _HasQuads.__init__: _HasQuads#__init__().
  _SalTiles.__init__: _SalTiles#__init__().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py)

## Classes
### <a id="_HasQuads"></a>`_HasQuads`
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py:170`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L170)
- doc: `HEAD_ALONG_SUBLANE` granule ops: a granule is one 4-token quad.
- signature: `class _HasQuads:`
- members:
  - <a id="_HasQuads.blend"></a>`blend(self, rmw_slot, row, src_tok, n)` — [`L194`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L194) — Overwrites rows `[row, row + n)` (one quad) of RMW quad `rmw_slot`. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
  - <a id="_HasQuads.granule_copy"></a>`granule_copy(self, row, rmw_slot, sem, *, to_hbm)` — [`L188`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L188)
  - <a id="_HasQuads.move_token"></a>`move_token(self, tok, dst_tok)` — [`L213`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L213) — Copies staged token `tok` to staged position `dst_tok` (`<= tok`).
  - <a id="_HasQuads.cache"></a>`cache` — [`L182`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L182)
  - <a id="_HasQuads.granule"></a>`granule` — [`L178`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L178)
  - <a id="_HasQuads.k"></a>`k` — [`L183`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L183)
  - <a id="_HasQuads.lkv_dim"></a>`lkv_dim` — [`L186`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L186)
  - <a id="_HasQuads.num_src_quads"></a>`num_src_quads` — [`L185`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L185)
  - <a id="_HasQuads.rmw"></a>`rmw` — [`L184`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L184)
- protocol/private: <a id="_HasQuads.__init__"></a>`__init__`[`L180`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L180)
- uses (calls/refs, reference-scoped): [`_KV_PACKING`](kv_cache_append.md#_KV_PACKING), [`_blend_token_into_quad`](kv_cache_append.md#_blend_token_into_quad)
- used by: [`_find_runs`](kv_cache_append.md#_find_runs), [`_write_runs`](kv_cache_append.md#_write_runs), [`_has_kernel`](kv_cache_append.md#_has_kernel), [`_step`](kv_cache_append.md#_find_runs._step), [`_blend_and_start_write`](kv_cache_append.md#_write_runs._wave._blend_and_start_write), [`_fn`](kv_cache_append.md#_write_runs._wave._reads._fn), [`_wait_write`](kv_cache_append.md#_write_runs._wave._wait_write)

### <a id="_SalTiles"></a>`_SalTiles`
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py:223`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L223)
- doc: `SEQ_ALONG_LANE` granule ops: a granule is one 128-lane tile.
- signature: `class _SalTiles:`
- members:
  - <a id="_SalTiles._cache_lanes"></a>`_cache_lanes(self, row, n)` — [`L253`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L253) — Lanes `[row, row + n)` of the cache; `row` is 128-aligned.
  - <a id="_SalTiles.blend"></a>`blend(self, rmw_slot, row, src_tok, n)` — [`L278`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L278) — Overwrites lanes `[row, row + n) & 127` of RMW tile `rmw_slot`. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
  - <a id="_SalTiles.granule_copy"></a>`granule_copy(self, row, rmw_slot, sem, *, to_hbm)` — [`L272`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L272)
  - <a id="_SalTiles.move_token"></a>`move_token(self, tok, dst_tok)` — [`L329`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L329) — Copies staged token (lane) `tok` to lane `dst_tok` (`<= tok`). — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
  - <a id="_SalTiles.cache"></a>`cache` — [`L244`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L244)
  - <a id="_SalTiles.granule"></a>`granule` — [`L231`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L231)
  - <a id="_SalTiles.k"></a>`k` — [`L245`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L245)
  - <a id="_SalTiles.padded_tokens"></a>`padded_tokens` — [`L248`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L248)
  - <a id="_SalTiles.page_size"></a>`page_size` — [`L247`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L247)
  - <a id="_SalTiles.rec_dim"></a>`rec_dim` — [`L249`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L249)
  - <a id="_SalTiles.rmw"></a>`rmw` — [`L246`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L246)
  - <a id="_SalTiles.short_run_fast_path"></a>`short_run_fast_path` — [`L251`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L251)
  - <a id="_SalTiles.sublane_groups"></a>`sublane_groups` — [`L243`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L243)
- protocol/private: <a id="_SalTiles.__init__"></a>`__init__`[`L233`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L233), <a id="_SalTiles._ensure_blocks_transposed"></a>`_ensure_blocks_transposed`[`L250`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L250), <a id="_SalTiles._src_tile"></a>`_src_tile`[`L258`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L258), <a id="_SalTiles._write"></a>`_write`[`L290`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L290)
- uses (calls/refs, reference-scoped): [`_LANES`](kv_cache_append.md#_LANES), [`_KV_PACKING`](kv_cache_append.md#_KV_PACKING)
- used by: [`kernel_fn`](../compress_and_store/kernel.md#kernel_fn), [`_sal_kernel`](kv_cache_append.md#_sal_kernel), [`_find_runs`](kv_cache_append.md#_find_runs), [`_write_runs`](kv_cache_append.md#_write_runs)

## Functions
- <a id="_align_to"></a>`_align_to(x: int, a: int)` — [`L90`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L90)
- <a id="_write_runs._wave._blend_and_start_write"></a>`_blend_and_start_write(i, src, row, n)` — [`L474`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L474)
- <a id="_blend_token_into_quad"></a>`_blend_token_into_quad(cur_quad_i32: jax.Array, src_quad_i32: jax.Array, src_l: jax.Array, dst_l: jax.Array)` — [`L150`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L150) — Returns `cur_quad_i32` with row `dst_l` set to `src_quad_i32[src_l]`.
- <a id="_write_runs._wave._for_each._body"></a>`_body(i, _)` — [`L457`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L457)
- <a id="_check_vmem"></a>`_check_vmem(vmem_bytes: int, per_token_bytes: int, fixed_bytes: int, name)` — [`L631`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L631)
- <a id="_find_runs._chunk"></a>`_chunk(c, carry)` — [`L418`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L418)
- <a id="_sal_kernel._ensure_blocks_transposed"></a>`_ensure_blocks_transposed(target_blocks)` — [`L588`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L588)
- <a id="_find_runs"></a>`_find_runs(ops: _HasQuads | _SalTiles, dst_ref: Any, run_src_ref: Any, run_dst_ref: Any, *, num_rows: int, num_tokens: jax.Array | None = None)` — [`L351`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L351) — Walks `dst_rows` once, compacting writable tokens and recording runs. — documented in [deepseek-v4-compress-and-store-kernel](../../../../../../concepts/deepseek-v4-compress-and-store-kernel.md)
- <a id="_write_runs._wave._reads._fn"></a>`_fn(i, src, row, n)` — [`L465`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L465)
- <a id="_write_runs._wave._for_each"></a>`_for_each(fn)` — [`L456`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L456)
- <a id="_format_rows"></a>`_format_rows(src: jax.Array, cache_kv: jax.Array, layout: KVLayout)` — [`L131`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L131) — Pads or truncates `src` rows to the cache's per-token record width.
- <a id="_has_kernel"></a>`_has_kernel(dst_ref, k_ref, cache_in_ref, cache_ref, run_src_ref, run_dst_ref, rmw_ref, sems, *, page_size: int, wave: int)` — [`L491`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L491)
- <a id="_has_launch"></a>`_has_launch(cache_kv: jax.Array, rows: jax.Array, *, page_size: int, wave: int)` — [`L649`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L649) — `HEAD_ALONG_SUBLANE`: `(staged source, kernel, scratch shapes)`.
- <a id="_write_runs._wave._reads"></a>`_reads(action)` — [`L464`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L464)
- <a id="_run_table_shapes"></a>`_run_table_shapes(num_tokens: int)` — [`L641`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L641) — SMEM `run_src` / `run_dst` scratch (one slot per token + a sentinel).
- <a id="_sal_kernel"></a>`_sal_kernel(dst_ref, k_ref, cache_in_ref, cache_ref, run_src_ref, run_dst_ref, transposed_ref, k_sal_ref, rmw_ref, sems, *, page_size: int, transpose_groups: int, wave: int, mask_scale_tail: bool = False, short_run_fast_path: bool = True)` — [`L524`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L524) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="_sal_launch"></a>`_sal_launch(cache_kv: jax.Array, rows: jax.Array, *, page_size: int, wave: int, short_run_fast_path: bool = True)` — [`L672`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L672) — `SEQ_ALONG_LANE`: `(staged source, kernel, scratch shapes)`. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="_find_runs._step"></a>`_step(tok, carry)` — [`L385`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L385)
- <a id="_sal_kernel._transpose"></a>`_transpose(b, _)` — [`L547`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L547)
- <a id="_write_runs._wave._wait_write"></a>`_wait_write(i, src, row, n)` — [`L478`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L478)
- <a id="_write_runs._wave"></a>`_wave(w, _)` — [`L452`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L452)
- <a id="_write_runs"></a>`_write_runs(ops: _HasQuads | _SalTiles, num_runs: jax.Array, run_src_ref: Any, run_dst_ref: Any, rd_sem: Any, wr_sem: Any, *, wave: int)` — [`L428`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L428) — Writes every run (each inside one granule), `wave` runs at a time. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="cache_page_size"></a>`cache_page_size(cache_kv: jax.Array, kv_layout: KVLayout | str | None)` — [`L94`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L94) — Validates `cache_kv` against `kv_layout` and returns its page size. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="check_scatter_rows_supported"></a>`check_scatter_rows_supported(cache_kv: jax.Array, src: jax.Array, kv_layout: KVLayout | str | None = KVLayout.HEAD_ALONG_SUBLANE)` — [`L728`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L728) — Validates `cache_kv` and `src` geometry and VMEM budget in pure Python. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="coalesced_kv_append"></a>`coalesced_kv_append(cache_kv: jax.Array, k_packed: jax.Array, seq_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, kv_layout: KVLayout | str | None = KVLayout.HEAD_ALONG_SUBLANE, *, interpret: bool = False)` — [`L870`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L870) — Appends this step's K rows into an unsharded paged indexer cache. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="coalesced_kv_append_dcp"></a>`coalesced_kv_append_dcp(cache_kv: jax.Array, k_packed: jax.Array, seq_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, dcp_rank: jax.Array | int, *, dcp_size: int, interleave_size: int, kv_layout: KVLayout | str | None = KVLayout.HEAD_ALONG_SUBLANE, interpret: bool = False)` — [`L912`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L912) — DCP twin of `coalesced_kv_append`: writes the rows this rank owns. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="scatter_rows"></a>`scatter_rows(cache_kv: jax.Array, src: jax.Array, dst_rows: jax.Array, kv_layout: KVLayout | str | None = KVLayout.HEAD_ALONG_SUBLANE, *, interpret: bool = False, short_run_fast_path: bool = True)` — [`L781`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L781) — Writes `src[i]` into flat cache row `dst_rows[i]` of `cache_kv` in place. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="scatter_rows_reference"></a>`scatter_rows_reference(cache_kv: jax.Array, src: jax.Array, dst_rows: jax.Array, kv_layout: KVLayout | str | None = KVLayout.HEAD_ALONG_SUBLANE)` — [`L968`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L968) — Pure-XLA `scatter_rows` (same arguments and contract); the test golden. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)

## Module values
- <a id="KVLayout"></a>`KVLayout` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L74)
- <a id="_KV_PACKING"></a>`_KV_PACKING` — [`L77`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L77)
- <a id="_LANES"></a>`_LANES` — [`L79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L79)
- <a id="_MAX_SAFE_VMEM_BYTES"></a>`_MAX_SAFE_VMEM_BYTES` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L84)
- <a id="_MAX_TOKENS"></a>`_MAX_TOKENS` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L87)
- <a id="_MAX_WAVE"></a>`_MAX_WAVE` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_append.py#L82)

