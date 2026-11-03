---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_utils.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_utils.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.streamindex_topk.kv_cache_utils`/
symbols:
  get_page_and_slot: get_page_and_slot().
  get_dcp_page_and_slot: get_dcp_page_and_slot().
  get_dst_rows: get_dst_rows().
  OOB_PAGE: OOB_PAGE.
  _row_positions: _row_positions().
  _lookup_page: _lookup_page().
  SKIP_ROW: SKIP_ROW.
  __all__: __all__.
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_utils.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_utils.py)

## Functions
- <a id="_lookup_page"></a>`_lookup_page(block_tables: jax.Array, num_seqs: int, seq_id: jax.Array, page_ordinal: jax.Array)` — [`L93`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_utils.py#L93) — Returns `(raw_page, ordinal_valid)` for `block_tables[seq_id, ordinal]`.
- <a id="_row_positions"></a>`_row_positions(num_tokens: int, seq_lens: jax.Array, query_start_loc: jax.Array)` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_utils.py#L56) — Per-token `(sequence, global KV position, in_batch)`.
- <a id="get_dcp_page_and_slot"></a>`get_dcp_page_and_slot(num_tokens: int, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, dcp_rank: jax.Array | int, *, page_size: int, num_pages: int, dcp_size: int, interleave_size: int)` — [`L143`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_utils.py#L143) — Target `(page, slot)` of every token in this rank's DCP cache shard.
- <a id="get_dst_rows"></a>`get_dst_rows(page: jax.Array, slot: jax.Array, page_size: int)` — [`L219`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_utils.py#L219) — Flattens `(page, slot)` to cache rows; `OOB_PAGE` becomes `SKIP_ROW`.
- <a id="get_page_and_slot"></a>`get_page_and_slot(num_tokens: int, seq_lens: jax.Array, block_tables: jax.Array, query_start_loc: jax.Array, *, page_size: int, num_pages: int)` — [`L107`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_utils.py#L107) — Target `(page, slot)` of every token in an unsharded paged cache.

## Module values
- <a id="OOB_PAGE"></a>`OOB_PAGE` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_utils.py#L43)
- <a id="SKIP_ROW"></a>`SKIP_ROW` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_utils.py#L45)
- <a id="__all__"></a>`__all__` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/kv_cache_utils.py#L47)

