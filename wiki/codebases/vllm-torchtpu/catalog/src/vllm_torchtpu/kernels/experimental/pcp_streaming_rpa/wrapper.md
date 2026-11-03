---
title: 'Module: src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.pcp_streaming_rpa.wrapper`/
symbols:
  sharded_pcp_ragged_paged_attention._pcp_ragged_paged_attention: sharded_pcp_ragged_paged_attention()._pcp_ragged_paged_attention().
  _compute_pcp_kv_writeback_mapping: _compute_pcp_kv_writeback_mapping().
  sharded_pcp_ragged_paged_attention: sharded_pcp_ragged_paged_attention().
  KVLayout: KVLayout.
  PCP_AXIS_NAME: PCP_AXIS_NAME.
  _compute_pcp_local_query_row_mapping: _compute_pcp_local_query_row_mapping().
  _compute_pcp_rank_major_query_row_mapping_from_metadata: _compute_pcp_rank_major_query_row_mapping_from_metadata().
  _select_replicated_query_row_mapping_for_pcp_rank: _select_replicated_query_row_mapping_for_pcp_rank().
  _prepare_packed_kv_for_cache: _prepare_packed_kv_for_cache().
  TP_AXIS_NAME: TP_AXIS_NAME.
  _PCPQueryRowMapping.is_valid: _PCPQueryRowMapping#is_valid.
  _pack_kv_for_cache: _pack_kv_for_cache().
  _compact_writeback_slot_ids_for_cache_rank: _compact_writeback_slot_ids_for_cache_rank().
  _PCPQueryRowMapping: _PCPQueryRowMapping#
  _reshape_packed_kv_cache_for_attention: _reshape_packed_kv_cache_for_attention().
  _build_writeback_segment_descriptors: _build_writeback_segment_descriptors().
  _PCPQueryRowMapping.absolute_positions: _PCPQueryRowMapping#absolute_positions.
  _PCPQueryRowMapping.request_indices: _PCPQueryRowMapping#request_indices.
  _kv_cache_page_size: _kv_cache_page_size().
  _PCPQueryRowMapping.source_ranks: _PCPQueryRowMapping#source_ranks.
  _compute_pcp_local_query_row_mapping_from_metadata: _compute_pcp_local_query_row_mapping_from_metadata().
  _pcp_rank_token_count_before: _pcp_rank_token_count_before().
  _PCPKVWritebackMapping: _PCPKVWritebackMapping#
  _PCPKVWritebackMapping.capture_offsets: _PCPKVWritebackMapping#capture_offsets.
  _PCPKVWritebackMapping.cache_owner_ranks: _PCPKVWritebackMapping#cache_owner_ranks.
  _PCPKVWritebackMapping.cache_local_slot_ids: _PCPKVWritebackMapping#cache_local_slot_ids.
  _PCPKVWritebackMapping.writeback_counts: _PCPKVWritebackMapping#writeback_counts.
  _select_replicated_shard_for_pcp_rank: _select_replicated_shard_for_pcp_rank().
  compute_pcp_local_mapping: compute_pcp_local_mapping().
  _compute_cache_owner_and_slot_ids_for_rows: _compute_cache_owner_and_slot_ids_for_rows().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py)

## Classes
### <a id="_PCPKVWritebackMapping"></a>`_PCPKVWritebackMapping`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py:54`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L54)
- doc: Unique cache destination and dense capture offset for each source row.
- signature: `class _PCPKVWritebackMapping(NamedTuple):`
- members:
  - <a id="_PCPKVWritebackMapping.cache_local_slot_ids"></a>`cache_local_slot_ids` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L58)
  - <a id="_PCPKVWritebackMapping.cache_owner_ranks"></a>`cache_owner_ranks` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L57)
  - <a id="_PCPKVWritebackMapping.capture_offsets"></a>`capture_offsets` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L59)
  - <a id="_PCPKVWritebackMapping.writeback_counts"></a>`writeback_counts` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L60)
- used by: [`_pcp_ragged_paged_attention`](wrapper.md#sharded_pcp_ragged_paged_attention._pcp_ragged_paged_attention), [`_compute_pcp_kv_writeback_mapping`](wrapper.md#_compute_pcp_kv_writeback_mapping), [`_compact_writeback_slot_ids_for_cache_rank`](wrapper.md#_compact_writeback_slot_ids_for_cache_rank)

### <a id="_PCPQueryRowMapping"></a>`_PCPQueryRowMapping`  ·  implements/extends NamedTuple
- def: [`src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py:45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L45)
- doc: Query-row coordinates in the batch-flat PCP token stream.
- signature: `class _PCPQueryRowMapping(NamedTuple):`
- members:
  - <a id="_PCPQueryRowMapping.absolute_positions"></a>`absolute_positions` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L48)
  - <a id="_PCPQueryRowMapping.is_valid"></a>`is_valid` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L51) — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
  - <a id="_PCPQueryRowMapping.request_indices"></a>`request_indices` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L49)
  - <a id="_PCPQueryRowMapping.source_ranks"></a>`source_ranks` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L50)
- used by: [`_pcp_ragged_paged_attention`](wrapper.md#sharded_pcp_ragged_paged_attention._pcp_ragged_paged_attention), [`_compute_pcp_kv_writeback_mapping`](wrapper.md#_compute_pcp_kv_writeback_mapping), [`_compute_pcp_local_query_row_mapping`](wrapper.md#_compute_pcp_local_query_row_mapping), [`_compute_pcp_rank_major_query_row_mapping_from_metadata`](wrapper.md#_compute_pcp_rank_major_query_row_mapping_from_metadata), [`_select_replicated_query_row_mapping_for_pcp_rank`](wrapper.md#_select_replicated_query_row_mapping_for_pcp_rank), [`_compute_pcp_local_query_row_mapping_from_metadata`](wrapper.md#_compute_pcp_local_query_row_mapping_from_metadata)

## Functions
- <a id="_build_writeback_segment_descriptors"></a>`_build_writeback_segment_descriptors(compact_slot_ids: jax.Array, writeback_count: jax.Array, max_segments: int = 4096, *, kv_layout: KVLayout = KVLayout.HEAD_ALONG_SUBLANE, page_size: int | None = None)` — [`L539`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L539) — Coalesce dense captured rows into contiguous cache-copy segments.
- <a id="_compact_writeback_slot_ids_for_cache_rank"></a>`_compact_writeback_slot_ids_for_cache_rank(writeback_mapping: _PCPKVWritebackMapping, cache_rank: int | jax.Array)` — [`L525`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L525) — Compact cache slots into the same dense order as captured KV rows. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="_compute_cache_owner_and_slot_ids_for_rows"></a>`_compute_cache_owner_and_slot_ids_for_rows(absolute_positions: jax.Array, request_indices: jax.Array, row_valid: jax.Array, block_tables: jax.Array, *, local_kv_cache_num_blocks: int, page_size: int, pcp_size: int, interleave_size: int)` — [`L226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L226) — Map arbitrary source rows to their unique PCP cache owner and slot.
- <a id="_compute_pcp_kv_writeback_mapping"></a>`_compute_pcp_kv_writeback_mapping(rank_major_query_rows: _PCPQueryRowMapping, block_tables: jax.Array, *, local_kv_cache_num_blocks: int, page_size: int, pcp_size: int, interleave_size: int)` — [`L430`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L430) — Build the one-path dense ring-capture destination mapping. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="_compute_pcp_local_query_row_mapping"></a>`_compute_pcp_local_query_row_mapping(q_lens: jax.Array, token_owner_starts: jax.Array, request_absolute_starts: jax.Array, *, local_padded_tokens: int, pcp_size: int, pcp_rank: int | jax.Array, interleave_size: int)` — [`L277`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L277) — Build one source rank's batch-flat query-row coordinates. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="_compute_pcp_local_query_row_mapping_from_metadata"></a>`_compute_pcp_local_query_row_mapping_from_metadata(kv_lens: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, local_padded_tokens: int, pcp_size: int, pcp_rank: int | jax.Array, interleave_size: int)` — [`L353`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L353) — Rebuild local query-row coordinates from PCP attention metadata.
- <a id="_compute_pcp_rank_major_query_row_mapping_from_metadata"></a>`_compute_pcp_rank_major_query_row_mapping_from_metadata(kv_lens: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, *, local_padded_tokens: int, pcp_size: int, interleave_size: int)` — [`L397`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L397) — Return query-row mappings shaped like the global sharded Q axis. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="_kv_cache_page_size"></a>`_kv_cache_page_size(kv_cache: jax.Array, kv_layout: KVLayout)` — [`L93`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L93)
- <a id="_pack_kv_for_cache"></a>`_pack_kv_for_cache(k: jax.Array, v: jax.Array, cache_dtype: jnp.dtype, *, kv_layout: KVLayout = KVLayout.HEAD_ALONG_SUBLANE, page_size: int | None = None)` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L63) — Pack K and V together before converting to the cache dtype.
- <a id="sharded_pcp_ragged_paged_attention._pcp_ragged_paged_attention"></a>`_pcp_ragged_paged_attention(q_local, k_local, v_local, kv_cache, kv_lens, page_indices, cu_q_lens, distribution)` — [`L731`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L731) — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="_pcp_rank_token_count_before"></a>`_pcp_rank_token_count_before(position: jax.Array, pcp_rank: jax.Array, pcp_size: int, interleave_size: int)` — [`L215`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L215)
- <a id="_prepare_packed_kv_for_cache"></a>`_prepare_packed_kv_for_cache(k: jax.Array, v: jax.Array, kv_cache: jax.Array, *, kv_layout: KVLayout = KVLayout.HEAD_ALONG_SUBLANE)` — [`L101`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L101) — Pack K/V once and adapt the packed tail to the cache layout. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="_reshape_packed_kv_cache_for_attention"></a>`_reshape_packed_kv_cache_for_attention(kv_cache: jax.Array, kv_layout: KVLayout = KVLayout.HEAD_ALONG_SUBLANE)` — [`L142`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L142)
- <a id="_select_replicated_query_row_mapping_for_pcp_rank"></a>`_select_replicated_query_row_mapping_for_pcp_rank(mapping: _PCPQueryRowMapping, pcp_axis: str, pcp_size: int)` — [`L597`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L597) — Select a PCP rank's query rows with one collective selection. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="_select_replicated_shard_for_pcp_rank"></a>`_select_replicated_shard_for_pcp_rank(tensor: jax.Array, pcp_axis: str, pcp_size: int, *, axis: int)` — [`L157`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L157) — Select this PCP rank shard from replicated data without axis_index.
- <a id="compute_pcp_local_mapping"></a>`compute_pcp_local_mapping(positions: jax.Array, token_req_indices: jax.Array, block_tables: jax.Array, block_size: int, cp_size: int, cp_rank: int, interleave_size: int = 1)` — [`L180`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L180) — Compute vLLM-compatible local CP slot mapping for one PCP rank.
- <a id="sharded_pcp_ragged_paged_attention"></a>`sharded_pcp_ragged_paged_attention(mesh: Mesh, q: jax.Array, k: jax.Array, v: jax.Array, kv_cache: jax.Array, kv_lens: jax.Array, page_indices: jax.Array, cu_q_lens: jax.Array, distribution: jax.Array, attention_sink: jax.Array | None, sm_scale: float, attention_chunk_size: int | None = None, q_scale: float | None = None, k_scale: float | None = None, v_scale: float | None = None, update_kv_cache: bool = True, cp_kv_cache_interleave_size: int = 0, q_block_size: int = PCP_STREAMING_RPA_LOCAL_COMPILE_TOKEN_MULTIPLE, q_compute_size: int | None = None, kv_layout: KVLayout = KVLayout.HEAD_ALONG_SUBLANE)` — [`L626`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L626) — Runs streaming PCP RPA over local Q/K/V shards. — documented in [batched-ragged-paged-attention-kernel](../../../../../../concepts/batched-ragged-paged-attention-kernel.md)

## Module values
- <a id="KVLayout"></a>`KVLayout` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L42)
- <a id="PCP_AXIS_NAME"></a>`PCP_AXIS_NAME` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L39) — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="TP_AXIS_NAME"></a>`TP_AXIS_NAME` — [`L40`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/wrapper.py#L40) — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)

