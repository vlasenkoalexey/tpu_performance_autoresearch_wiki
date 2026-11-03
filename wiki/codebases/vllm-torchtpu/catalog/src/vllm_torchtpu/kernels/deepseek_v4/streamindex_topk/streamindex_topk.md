---
title: 'Module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.deepseek_v4.streamindex_topk.streamindex_topk`/
symbols:
  kernel: kernel().
  kernel.blocked_prefill_step: kernel().blocked_prefill_step().
  streamindex_topk: streamindex_topk().
  indexer_kv_layout: indexer_kv_layout().
  get_kv_cache_shape: get_kv_cache_shape().
  KVLayout: KVLayout.
  streamindex_topk._common_path: streamindex_topk()._common_path().
  kernel.step_body: kernel().step_body().
  streamindex_topk.run_scores_kernel: streamindex_topk().run_scores_kernel().
  streamindex_topk_dcp: streamindex_topk_dcp().
  DCP_AXIS_NAME: DCP_AXIS_NAME.
  streamindex_topk_dcp._local: streamindex_topk_dcp()._local().
  kernel._run_all: kernel()._run_all().
  _BlockedPrefillConfig.cache_row: _BlockedPrefillConfig#cache_row().
  streamindex_topk._pass_specs: streamindex_topk()._pass_specs().
  align_to: align_to().
  KV_PACKING: KV_PACKING.
  _BlockedPrefillConfig.create: _BlockedPrefillConfig#create().
  logger: logger.
  cp_rank_as_data: cp_rank_as_data.
  kernel.blocked_prefill_step.load_chunk: kernel().blocked_prefill_step().load_chunk().
  MlaCase: MlaCase.
  kernel.reduce_heads: kernel().reduce_heads().
  prepare_q_inputs: prepare_q_inputs().
  prepare_index_weights: prepare_index_weights().
  convert_cache_to_seq_along_lane: convert_cache_to_seq_along_lane().
  streamindex_topk._pass_metadata: streamindex_topk()._pass_metadata().
  DEFAULT_BUFFER_COUNT: DEFAULT_BUFFER_COUNT.
  get_dtype_packing: get_dtype_packing().
  kernel.seq_tile: kernel().seq_tile().
  kernel.bkv_block: kernel().bkv_block().
  cp_local_length: cp_local_length.
  _effective_row_lengths: _effective_row_lengths().
  _INDEXER_KV_LAYOUT_FALLBACK_LOGGED._INDEXER_KV_LAYOUT_FALLBACK_LOGGED: _INDEXER_KV_LAYOUT_FALLBACK_LOGGED._INDEXER_KV_LAYOUT_FALLBACK_LOGGED.
  cp_local_to_global: cp_local_to_global.
  cp_owner_rank: cp_owner_rank.
  cp_global_to_local: cp_global_to_local.
  kernel.compute_scores: kernel().compute_scores().
  kernel.blocked_prefill_step.reduce_token_block: kernel().blocked_prefill_step().reduce_token_block().
  streamindex_topk._scores_for_chunk: streamindex_topk()._scores_for_chunk().
  streamindex_topk._fast_path: streamindex_topk()._fast_path().
  DEFAULT_VMEM_LIMIT_BYTES: DEFAULT_VMEM_LIMIT_BYTES.
  _BlockedPrefillConfig.tok_blk: _BlockedPrefillConfig#tok_blk.
  _BlockedPrefillConfig.num_head_groups: _BlockedPrefillConfig#num_head_groups.
  kernel.bq_block: kernel().bq_block().
  kernel.transpose_to_head_major: kernel().transpose_to_head_major().
  get_dtype_bitwidth: get_dtype_bitwidth().
  _BlockedPrefillConfig: _BlockedPrefillConfig#
  _BlockedPrefillConfig.enabled: _BlockedPrefillConfig#enabled.
  _BlockedPrefillConfig.num_tok_blks: _BlockedPrefillConfig#num_tok_blks.
  _BlockedPrefillConfig.rows_per_group_tok_blk: _BlockedPrefillConfig#rows_per_group_tok_blk.
  _BlockedPrefillConfig.rows_per_group: _BlockedPrefillConfig#rows_per_group.
  _BlockedPrefillConfig.score_pitch: _BlockedPrefillConfig#score_pitch.
  kernel.seq_along_lane_block_rows: kernel().seq_along_lane_block_rows().
  kernel.seq_along_lane_key_tile: kernel().seq_along_lane_key_tile().
  kernel.seq_along_lane_scale_tile: kernel().seq_along_lane_scale_tile().
  kernel.reduce_heads.qk: kernel().reduce_heads().qk().
  kernel.blocked_prefill_step.qk: kernel().blocked_prefill_step().qk().
  streamindex_topk._block_sizes: streamindex_topk()._block_sizes().
  cdiv: cdiv().
  _BlockedPrefillConfig.heads_per_group: _BlockedPrefillConfig#heads_per_group.
  _BlockedPrefillConfig.lane_chunk: _BlockedPrefillConfig#lane_chunk.
  _BlockedPrefillConfig.num_lane_chunks: _BlockedPrefillConfig#num_lane_chunks.
  _BlockedPrefillConfig.tiles_per_chunk: _BlockedPrefillConfig#tiles_per_chunk.
  _BlockedPrefillConfig.strided_score_store: _BlockedPrefillConfig#strided_score_store.
  _BlockedPrefillConfig.bf16_reduce: _BlockedPrefillConfig#bf16_reduce.
  _BlockedPrefillConfig.wb_dtype: _BlockedPrefillConfig#wb_dtype.
  kernel.pad_tokens: kernel().pad_tokens().
  kernel._run_all._run_pipeline: kernel()._run_all()._run_pipeline().
  DEFAULT_INDEXER_KV_CACHE_MODE: DEFAULT_INDEXER_KV_CACHE_MODE.
  prepare_outputs: prepare_outputs().
---
# Module: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py)

## Classes
### <a id="_BlockedPrefillConfig"></a>`_BlockedPrefillConfig`
- def: [`src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py:81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L81)
- doc: Multi-token (prefill / mixed) scoring layout and tiling configuration.
- signature: `class _BlockedPrefillConfig:`
- members:
  - <a id="_BlockedPrefillConfig.cache_row"></a>`cache_row(self, h: int, tb: int)` — [`L173`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L173) — First `q_hm_ref` row of head `h` in token block `tb`.
  - <a id="_BlockedPrefillConfig.create"></a>`create(cls, *, bq_sz: int, bkv_sz: int, num_q_heads: int, q_dtype: Any, seq_batch_size: int)` — [`L110`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L110) — Computes the blocked-prefill layout parameters for a kernel pass.
  - <a id="_BlockedPrefillConfig.bf16_reduce"></a>`bf16_reduce` — [`L106`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L106)
  - <a id="_BlockedPrefillConfig.enabled"></a>`enabled` — [`L94`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L94)
  - <a id="_BlockedPrefillConfig.heads_per_group"></a>`heads_per_group` — [`L98`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L98)
  - <a id="_BlockedPrefillConfig.lane_chunk"></a>`lane_chunk` — [`L101`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L101)
  - <a id="_BlockedPrefillConfig.num_head_groups"></a>`num_head_groups` — [`L97`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L97)
  - <a id="_BlockedPrefillConfig.num_lane_chunks"></a>`num_lane_chunks` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L102)
  - <a id="_BlockedPrefillConfig.num_tok_blks"></a>`num_tok_blks` — [`L96`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L96)
  - <a id="_BlockedPrefillConfig.rows_per_group"></a>`rows_per_group` — [`L100`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L100)
  - <a id="_BlockedPrefillConfig.rows_per_group_tok_blk"></a>`rows_per_group_tok_blk` — [`L99`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L99)
  - <a id="_BlockedPrefillConfig.score_pitch"></a>`score_pitch` — [`L105`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L105)
  - <a id="_BlockedPrefillConfig.strided_score_store"></a>`strided_score_store` — [`L104`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L104)
  - <a id="_BlockedPrefillConfig.tiles_per_chunk"></a>`tiles_per_chunk` — [`L103`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L103)
  - <a id="_BlockedPrefillConfig.tok_blk"></a>`tok_blk` — [`L95`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L95)
  - <a id="_BlockedPrefillConfig.wb_dtype"></a>`wb_dtype` — [`L107`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L107)
- uses (calls/refs, reference-scoped): [`get_dtype_packing`](streamindex_topk.md#get_dtype_packing), [`get_dtype_bitwidth`](streamindex_topk.md#get_dtype_bitwidth)
- used by: [`kernel`](streamindex_topk.md#kernel), [`blocked_prefill_step`](streamindex_topk.md#kernel.blocked_prefill_step), [`_run_all`](streamindex_topk.md#kernel._run_all), [`reduce_token_block`](streamindex_topk.md#kernel.blocked_prefill_step.reduce_token_block)

## Functions
- <a id="streamindex_topk._block_sizes"></a>`_block_sizes(num_queries_per_block, bkv_p, static_q_len)` — [`L1252`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L1252) — Query and KV block sizes a pass runs with.
- <a id="streamindex_topk._common_path"></a>`_common_path(_)` — [`L1497`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L1497) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="_effective_row_lengths"></a>`_effective_row_lengths(seq_lens: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, num_tokens: int, num_positions: int, compression_ratio: int, cp_rank: jax.Array | int = 0, cp_size: int = 1, interleave_c: int = 1)` — [`L995`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L995) — Visible compressed KV positions per token row of the score matrix.
- <a id="streamindex_topk._fast_path"></a>`_fast_path(_)` — [`L1614`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L1614)
- <a id="streamindex_topk_dcp._local"></a>`_local(q, indexer_weights, cache_kv, seq_lens, page_indices, cu_q_lens, distribution)` — [`L1777`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L1777) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="streamindex_topk._pass_metadata"></a>`_pass_metadata(spec, chunk_starts, chunk_tokens)` — [`L1437`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L1437) — One schedule per pass, holding every chunk's steps back to back.
- <a id="streamindex_topk._pass_specs"></a>`_pass_specs(decode_batch_end)` — [`L1378`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L1378) — `run_scores_kernel` kwargs for the passes over the batch. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="kernel._run_all"></a>`_run_all(q_hm_ref=None, wb_ref=None)` — [`L725`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L725)
- <a id="kernel._run_all._run_pipeline"></a>`_run_pipeline(final_allocs)` — [`L734`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L734)
- <a id="streamindex_topk._scores_for_chunk"></a>`_scores_for_chunk(passes, chunk_idx, chunk_token_start, chunk_tokens, out_dtype, scheduling_group_id)` — [`L1464`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L1464) — Scores for one window of the flat token axis, in a private buffer.
- <a id="align_to"></a>`align_to(x, a)` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L67)
- <a id="kernel.bkv_block"></a>`bkv_block(p_id)` — [`L253`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L253) — KV block scheduled at pipeline step `p_id`.
- <a id="kernel.blocked_prefill_step"></a>`blocked_prefill_step(q_vmem, weights_vmem, bkv_vmem, scores_vmem, q_hm_ref, wb_ref)` — [`L555`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L555) — Scores one (q block, kv block) step of the multi-token path. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="kernel.bq_block"></a>`bq_block(p_id)` — [`L249`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L249) — Query block scheduled at pipeline step `p_id`.
- <a id="cdiv"></a>`cdiv(a, b)` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L62)
- <a id="kernel.compute_scores"></a>`compute_scores(bq_vec, bkv_vec, scale_val_vec, bq_weights_vec, q_is_head_major=False)` — [`L463`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L463)
- <a id="convert_cache_to_seq_along_lane"></a>`convert_cache_to_seq_along_lane(cache_kv: jax.Array, actual_head_dim: int)` — [`L964`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L964) — Repacks a HEAD_ALONG_SUBLANE index cache into the SEQ_ALONG_LANE layout.
- <a id="get_dtype_bitwidth"></a>`get_dtype_bitwidth(dtype)` — [`L71`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L71)
- <a id="get_dtype_packing"></a>`get_dtype_packing(dtype)` — [`L75`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L75)
- <a id="get_kv_cache_shape"></a>`get_kv_cache_shape(total_num_pages: int, page_size: int, actual_head_dim: int, kv_layout: KVLayout | str = KVLayout.HEAD_ALONG_SUBLANE)` — [`L923`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L923) — Returns the packed uint8 index KV cache shape for a given layout. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="indexer_kv_layout"></a>`indexer_kv_layout(block_size: int, mode: str | None = None)` — [`L847`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L847) — Returns the single-source `KVLayout` for an indexer K cache of `block_size`. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="kernel"></a>`kernel(seq_lens_ref, page_indices_ref, cu_q_lens_ref, start_end_seq_idx_ref, metadata_ref, q_hbm_ref, indexer_weights_hbm_ref, cache_kv_hbm_ref, *score_refs, bkv_p: int, bq_sz: int, seq_batch_size: int, buffer_count: int = 3, kv_layout: KVLayout = KVLayout.HEAD_ALONG_SUBLANE, chunk_idx: int = 0)` — [`L183`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L183) — Executes the n-buffered Pallas scoring pipeline for StreamIndex Top-K. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="kernel.blocked_prefill_step.load_chunk"></a>`load_chunk(c)` — [`L611`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L611)
- <a id="kernel.pad_tokens"></a>`pad_tokens(bq_rows, n_tok)` — [`L409`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L409) — [n_tok, H, D] -> [hm_tok, H, D], zero rows appended.
- <a id="prepare_index_weights"></a>`prepare_index_weights(index_weights: jax.Array, q_dtype)` — [`L799`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L799) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="prepare_outputs"></a>`prepare_outputs(out)` — [`L817`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L817)
- <a id="prepare_q_inputs"></a>`prepare_q_inputs(q: jax.Array)` — [`L780`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L780) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="kernel.reduce_heads.qk"></a>`qk(rows)` — [`L430`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L430)
- <a id="kernel.blocked_prefill_step.qk"></a>`qk(q_rows, keys)` — [`L629`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L629)
- <a id="kernel.reduce_heads"></a>`reduce_heads(bq_rows, bkv, bq_weights, head_major=False)` — [`L416`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L416) — relu(q @ k) weighted-summed over heads.
- <a id="kernel.blocked_prefill_step.reduce_token_block"></a>`reduce_token_block(sts, tb)` — [`L653`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L653) — sum_h relu(st_h) * w_h over the rows of token block `tb`.
- <a id="streamindex_topk.run_scores_kernel"></a>`run_scores_kernel(q, prepared_indexer_weights, cache_kv, scores_init, seq_lens, page_indices, cu_q_lens, start_seq_idx, end_seq_idx, static_q_len, num_kv_pages_per_block, num_queries_per_block, buffer_count, seq_batch_size, out_dtype, pass_meta, case=MlaCase.MIXED, chunk_token_start=None, chunk_tokens=None, scheduling_group_id=None, chunk_idx=0)` — [`L1261`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L1261) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="kernel.seq_along_lane_block_rows"></a>`seq_along_lane_block_rows(bkv_vmem)` — [`L373`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L373)
- <a id="kernel.seq_along_lane_key_tile"></a>`seq_along_lane_key_tile(rows, batch_idx, lane_tile_idx)` — [`L378`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L378) — [head_dim, 128] FP8 keys of lane tile `lane_tile_idx`.
- <a id="kernel.seq_along_lane_scale_tile"></a>`seq_along_lane_scale_tile(rows, batch_idx, lane_tile_idx)` — [`L387`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L387) — [1, 128] f32 dequantization scales of lane tile `lane_tile_idx`.
- <a id="kernel.seq_tile"></a>`seq_tile(p_id)` — [`L245`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L245) — Sequence tile scheduled at pipeline step `p_id`.
- <a id="kernel.step_body"></a>`step_body(q_vmem, weights_vmem, bkv_vmem, scores_vmem, q_hm_ref=None)` — [`L490`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L490) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="streamindex_topk"></a>`streamindex_topk(q: jax.Array, indexer_weights: jax.Array, cache_kv: jax.Array, seq_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, k: int, compression_ratio: int, num_kv_pages_per_block: tuple[int, int, int] | int | None = None, num_queries_per_block: tuple[int, int, int] | int | None = None, buffer_count: tuple[int, int, int] | int | None = DEFAULT_BUFFER_COUNT, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES, decode_req_batch_size: int = 4, enable_early_exit: bool = False, kv_layout: KVLayout | str = KVLayout.HEAD_ALONG_SUBLANE, chunk_tokens: int | None = None, cp_size: int = 1, cp_rank: jax.Array | int = 0, interleave_size: int = 1, return_scores: bool = False, uniform_q_len: int | None = None)` — [`L1053`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L1053) — StreamIndex Top-K retrieval. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="streamindex_topk_dcp"></a>`streamindex_topk_dcp(q: jax.Array, indexer_weights: jax.Array, cache_kv: jax.Array, seq_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, mesh, k: int, compression_ratio: int, dcp_size: int, interleave_size: int, num_kv_pages_per_block: tuple[int, int, int] | int | None = None, num_queries_per_block: tuple[int, int, int] | int | None = None, buffer_count: tuple[int, int, int] | int | None = DEFAULT_BUFFER_COUNT, vmem_limit_bytes: int = DEFAULT_VMEM_LIMIT_BYTES, decode_req_batch_size: int = 4, kv_layout: KVLayout | str = KVLayout.HEAD_ALONG_SUBLANE, chunk_tokens: int | None = None, dcp_axis_name: str = DCP_AXIS_NAME, a2a_merge: bool = False)` — [`L1657`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L1657) — Exact global top-k over a DCP-sharded KV cache, delivered rank-local. — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="kernel.transpose_to_head_major"></a>`transpose_to_head_major(bq_rows, n_tok)` — [`L398`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L398) — [n_tok*H, D] head-minor rows -> [H*n_tok, D] head-major rows.

## Module values
- <a id="DCP_AXIS_NAME"></a>`DCP_AXIS_NAME` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L53) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="DEFAULT_BUFFER_COUNT"></a>`DEFAULT_BUFFER_COUNT` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L51) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="DEFAULT_INDEXER_KV_CACHE_MODE"></a>`DEFAULT_INDEXER_KV_CACHE_MODE` — [`L843`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L843)
- <a id="DEFAULT_VMEM_LIMIT_BYTES"></a>`DEFAULT_VMEM_LIMIT_BYTES` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L52)
- <a id="KVLayout"></a>`KVLayout` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L50)
- <a id="KV_PACKING"></a>`KV_PACKING` — [`L841`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L841) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="MlaCase"></a>`MlaCase` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L49)
- <a id="_INDEXER_KV_LAYOUT_FALLBACK_LOGGED._INDEXER_KV_LAYOUT_FALLBACK_LOGGED"></a>`_INDEXER_KV_LAYOUT_FALLBACK_LOGGED` — [`L844`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L844)
- <a id="cp_global_to_local"></a>`cp_global_to_local` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L58)
- <a id="cp_local_length"></a>`cp_local_length` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L56)
- <a id="cp_local_to_global"></a>`cp_local_to_global` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L55)
- <a id="cp_owner_rank"></a>`cp_owner_rank` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L57)
- <a id="cp_rank_as_data"></a>`cp_rank_as_data` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L59) — documented in [deepseek-v4-streamindex-topk-kernel](../../../../../../concepts/deepseek-v4-streamindex-topk-kernel.md)
- <a id="logger"></a>`logger` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/deepseek_v4/streamindex_topk/streamindex_topk.py#L45)

