---
title: 'Module: src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.distributed.kv_transfer.raiden.byte_spans`/
symbols:
  lower_gdn_state_shard_spans: lower_gdn_state_shard_spans().
  lower_glm_dcp_row_spans: lower_glm_dcp_row_spans().
  lower_fa_spans: lower_fa_spans().
  lower_glm_dcp_identity_spans: lower_glm_dcp_identity_spans().
  lower_glm_row_spans: lower_glm_row_spans().
  lower_dsv4_row_spans: lower_dsv4_row_spans().
  PoolSpanRegistration: PoolSpanRegistration#
  PoolSpanRegistration.spans: PoolSpanRegistration#spans.
  lower_kda_state_shard_spans: lower_kda_state_shard_spans().
  PoolByteSpan.size_bytes: PoolByteSpan#size_bytes.
  PoolByteSpan: PoolByteSpan#
  _region_value: _region_value().
  PoolByteSpan.src_offset_bytes: PoolByteSpan#src_offset_bytes.
  PoolByteSpan.src_block_ordinal: PoolByteSpan#src_block_ordinal.
  PoolByteSpan.dst_block_index: PoolByteSpan#dst_block_index.
  PoolByteSpan.dst_offset_bytes: PoolByteSpan#dst_offset_bytes.
  PoolSpanRegistration.tag: PoolSpanRegistration#tag.
  PoolSpanRegistration.declared_bytes: PoolSpanRegistration#declared_bytes.
  PoolSpanRegistration.block_ids: PoolSpanRegistration#block_ids.
  PoolByteSpan.count: PoolByteSpan#count.
  owned_token_ranges: owned_token_ranges().
  PoolByteSpan.src_stride_bytes: PoolByteSpan#src_stride_bytes.
  PoolSpanRegistration.dst_space_version: PoolSpanRegistration#dst_space_version.
  PoolByteSpan.dst_unit_ordinal: PoolByteSpan#dst_unit_ordinal.
  PoolByteSpan.dst_stride_bytes: PoolByteSpan#dst_stride_bytes.
  _TPU_PHYSICAL_TOKEN_BYTES: _TPU_PHYSICAL_TOKEN_BYTES.
  glm_dcp_chunk_bytes: glm_dcp_chunk_bytes().
---
# Module: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py)

## Classes
### <a id="PoolByteSpan"></a>`PoolByteSpan`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py:39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L39)
- doc: One byte copy between a registered source and destination block.
- signature: `class PoolByteSpan:`
- members:
  - <a id="PoolByteSpan.count"></a>`count` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L49)
  - <a id="PoolByteSpan.dst_block_index"></a>`dst_block_index` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L44)
  - <a id="PoolByteSpan.dst_offset_bytes"></a>`dst_offset_bytes` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L45)
  - <a id="PoolByteSpan.dst_stride_bytes"></a>`dst_stride_bytes` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L48)
  - <a id="PoolByteSpan.dst_unit_ordinal"></a>`dst_unit_ordinal` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L52)
  - <a id="PoolByteSpan.size_bytes"></a>`size_bytes` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L46)
  - <a id="PoolByteSpan.src_block_ordinal"></a>`src_block_ordinal` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L42)
  - <a id="PoolByteSpan.src_offset_bytes"></a>`src_offset_bytes` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L43)
  - <a id="PoolByteSpan.src_stride_bytes"></a>`src_stride_bytes` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L47)
- used by: [`lower_fa_spans_sol`](seq_on_lane.md#lower_fa_spans_sol), [`lower_gdn_state_fanout_spans_sol`](seq_on_lane.md#lower_gdn_state_fanout_spans_sol), [`lower_gdn_state_shard_spans`](byte_spans.md#lower_gdn_state_shard_spans), [`lower_glm_dcp_row_spans`](byte_spans.md#lower_glm_dcp_row_spans), [`_lower_gdn_state_split_spans`](seq_on_lane.md#_lower_gdn_state_split_spans), [`lower_fa_spans`](byte_spans.md#lower_fa_spans), [`lower_glm_dcp_identity_spans`](byte_spans.md#lower_glm_dcp_identity_spans), [`lower_dsv4_row_spans`](byte_spans.md#lower_dsv4_row_spans), [`lower_glm_row_spans`](byte_spans.md#lower_glm_row_spans), [`spans`](byte_spans.md#PoolSpanRegistration.spans), [`lower_kda_state_shard_spans`](byte_spans.md#lower_kda_state_shard_spans), [`registration_source_bytes`](seq_on_lane.md#registration_source_bytes)

### <a id="PoolSpanRegistration"></a>`PoolSpanRegistration`
- def: [`src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py:56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L56)
- doc: One rank's byte declarations for one exact pool tag.
- signature: `class PoolSpanRegistration:`
- members:
  - <a id="PoolSpanRegistration.block_ids"></a>`block_ids` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L60)
  - <a id="PoolSpanRegistration.declared_bytes"></a>`declared_bytes` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L62)
  - <a id="PoolSpanRegistration.dst_space_version"></a>`dst_space_version` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L66)
  - <a id="PoolSpanRegistration.spans"></a>`spans` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L61)
  - <a id="PoolSpanRegistration.tag"></a>`tag` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L59)
- uses (calls/refs, reference-scoped): [`PoolByteSpan`](byte_spans.md#PoolByteSpan)
- used by: [`_register_stage3_request_blocks`](../tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_blocks), [`_register_stage3_request_row_spans`](../tpu_connector.md#TPURaidenConnectorWorker._register_stage3_request_row_spans), [`lower_fa_spans_sol`](seq_on_lane.md#lower_fa_spans_sol), [`lower_gdn_state_fanout_spans_sol`](seq_on_lane.md#lower_gdn_state_fanout_spans_sol), [`lower_gdn_state_shard_spans`](byte_spans.md#lower_gdn_state_shard_spans), [`lower_glm_dcp_row_spans`](byte_spans.md#lower_glm_dcp_row_spans), [`_lower_gdn_state_split_spans`](seq_on_lane.md#_lower_gdn_state_split_spans), [`lower_fa_spans`](byte_spans.md#lower_fa_spans), [`lower_glm_dcp_identity_spans`](byte_spans.md#lower_glm_dcp_identity_spans), [`lower_dsv4_row_spans`](byte_spans.md#lower_dsv4_row_spans), [`lower_glm_row_spans`](byte_spans.md#lower_glm_row_spans), [`lower_kda_state_shard_spans`](byte_spans.md#lower_kda_state_shard_spans), [`registration_source_bytes`](seq_on_lane.md#registration_source_bytes), [`lower_gdn_state_shard_spans_sol`](seq_on_lane.md#lower_gdn_state_shard_spans_sol)

## Functions
- <a id="_region_value"></a>`_region_value(region: object, name: str)` — [`L162`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L162)
- <a id="glm_dcp_chunk_bytes"></a>`glm_dcp_chunk_bytes(*, page_tokens: int, live_bytes_per_block: int, row_bytes: int, interleave_tokens: int)` — [`L502`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L502) — Bytes of one ``interleave_tokens`` chunk of a packed-row GLM page.
- <a id="lower_dsv4_row_spans"></a>`lower_dsv4_row_spans(*, tag: str, num_tokens: int, transfer_rank: int, parallelism: int, page_tokens: int, live_bytes_per_block: int, row_bytes: int, block_ids: Sequence[int])` — [`L660`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L660) — Lower one DeepSeek-V4 cache class to round-robin per-page byte spans.
- <a id="lower_fa_spans"></a>`lower_fa_spans(*, num_tokens: int, transfer_rank: int, parallelism: int, interleave_tokens: int, page_tokens: int, token_bytes: int, block_ids: Sequence[int])` — [`L98`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L98) — Lower PCP ownership to source-page / global-destination byte ranges.
- <a id="lower_gdn_state_shard_spans"></a>`lower_gdn_state_shard_spans(*, tag: str, block_id: int, transfer_rank: int, parallelism: int, regions: Sequence[object], physical_granule_bytes: int = _TPU_PHYSICAL_TOKEN_BYTES)` — [`L167`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L167) — Lower one rank's GDN head shard into a full destination state.
- <a id="lower_glm_dcp_identity_spans"></a>`lower_glm_dcp_identity_spans(*, tag: str, num_tokens: int, page_tokens: int, dcp_size: int, dcp_rank: int, live_bytes_per_block: int, block_ids: Sequence[int])` — [`L600`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L600) — Lower one DCP rank's GLM cache to the same DCP rank of the destination.
- <a id="lower_glm_dcp_row_spans"></a>`lower_glm_dcp_row_spans(*, tag: str, num_tokens: int, page_tokens: int, live_bytes_per_block: int, row_bytes: int, block_ids: Sequence[int], dst_dcp_size: int, interleave_tokens: int)` — [`L544`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L544) — Lower a GLM cache holding every token to a DCP-sharded destination.
- <a id="lower_glm_row_spans"></a>`lower_glm_row_spans(*, tag: str, num_tokens: int, transfer_rank: int, parallelism: int, page_tokens: int, live_bytes_per_block: int, row_bytes: int, block_ids: Sequence[int])` — [`L428`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L428) — Lower a TP-replicated GLM cache to round-robin per-page byte spans.
- <a id="lower_kda_state_shard_spans"></a>`lower_kda_state_shard_spans(*, tag: str, block_id: int, transfer_rank: int, parallelism: int, dst_shards: int, regions: Sequence[object])` — [`L357`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L357) — Concatenate aligned KDA head shards in the rank-blocked pool layout.
- <a id="owned_token_ranges"></a>`owned_token_ranges(*, num_tokens: int, transfer_rank: int, parallelism: int, interleave_tokens: int)` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L69) — Return this producer rank's PCP-owned destination token ranges.

## Module values
- <a id="_TPU_PHYSICAL_TOKEN_BYTES"></a>`_TPU_PHYSICAL_TOKEN_BYTES` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/distributed/kv_transfer/raiden/byte_spans.py#L35)

