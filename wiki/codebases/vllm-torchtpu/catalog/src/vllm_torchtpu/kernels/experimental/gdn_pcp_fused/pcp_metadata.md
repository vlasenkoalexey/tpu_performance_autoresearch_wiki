---
title: 'Module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.gdn_pcp_fused.pcp_metadata`/
symbols:
  _compute_pcp_stage_metadata_from_coordinates: _compute_pcp_stage_metadata_from_coordinates().
  _compute_pcp_stage_metadata_from_coordinates._emit_request: _compute_pcp_stage_metadata_from_coordinates()._emit_request().
  compute_pcp_stage_metadata: compute_pcp_stage_metadata().
  _schedule_capacities: _schedule_capacities().
  _compute_pcp_stage_metadata_from_coordinates._plan_projection_catchup: _compute_pcp_stage_metadata_from_coordinates()._plan_projection_catchup().
  PcpStageMetadata.rank_row_start: PcpStageMetadata#rank_row_start.
  PcpStageMetadata.rank_valid_rows: PcpStageMetadata#rank_valid_rows.
  _compute_pcp_stage_metadata_from_coordinates._requests_pending: _compute_pcp_stage_metadata_from_coordinates()._requests_pending().
  _compute_pcp_stage_metadata_from_coordinates._emit_request._emit_window._emit_rank_tiles: _compute_pcp_stage_metadata_from_coordinates()._emit_request()._emit_window()._emit_rank_tiles().
  PcpStageMetadata: PcpStageMetadata#
  _BuilderState.active_stages: _BuilderState#active_stages.
  _BuilderState: _BuilderState#
  _compute_pcp_stage_metadata_from_coordinates._emit_request._emit_window: _compute_pcp_stage_metadata_from_coordinates()._emit_request()._emit_window().
  _compute_pcp_stage_metadata_from_coordinates._emit_request._emit_window._emit_rank_tiles._emit_tile: _compute_pcp_stage_metadata_from_coordinates()._emit_request()._emit_window()._emit_rank_tiles()._emit_tile().
  _compute_pcp_stage_metadata_from_coordinates._set_body_projection_offset: _compute_pcp_stage_metadata_from_coordinates()._set_body_projection_offset().
  PcpStageMetadata.rank_active_row_end: PcpStageMetadata#rank_active_row_end.
  PcpStageMetadata.first_tile: PcpStageMetadata#first_tile.
  PcpStageMetadata.tile_stage: PcpStageMetadata#tile_stage.
  _BuilderState.request_index: _BuilderState#request_index.
  _BuilderState.rank_row_start: _BuilderState#rank_row_start.
  _BuilderState.rank_valid_rows: _BuilderState#rank_valid_rows.
  _BuilderState.first_tile: _BuilderState#first_tile.
  PcpStageMetadata.num_stages: PcpStageMetadata#num_stages.
  PcpStageMetadata.num_tokens: PcpStageMetadata#num_tokens.
  PcpStageMetadata.rank_recv_start: PcpStageMetadata#rank_recv_start.
  PcpStageMetadata.tile_row_in_stage: PcpStageMetadata#tile_row_in_stage.
  PcpStageMetadata.projection_catchup_start: PcpStageMetadata#projection_catchup_start.
  PcpStageMetadata.projection_catchup_count: PcpStageMetadata#projection_catchup_count.
  PcpStageMetadata.projection_work_offset_end: PcpStageMetadata#projection_work_offset_end.
  _BuilderState.active_tiles: _BuilderState#active_tiles.
  _BuilderState.rank_row_offsets: _BuilderState#rank_row_offsets.
  _BuilderState.rank_active_row_end: _BuilderState#rank_active_row_end.
  _BuilderState.request_id: _BuilderState#request_id.
  _BuilderState.query_row_start: _BuilderState#query_row_start.
  _BuilderState.num_tokens: _BuilderState#num_tokens.
  _BuilderState.rank_recv_start: _BuilderState#rank_recv_start.
  _BuilderState.stage_num_tiles: _BuilderState#stage_num_tiles.
  _BuilderState.tile_stage: _BuilderState#tile_stage.
  _BuilderState.tile_row_in_stage: _BuilderState#tile_row_in_stage.
  _BuilderState.tile_request_id: _BuilderState#tile_request_id.
  _BuilderState.tile_query_row_start: _BuilderState#tile_query_row_start.
  _BuilderState.tile_num_tokens: _BuilderState#tile_num_tokens.
  _BuilderState.tile_is_first: _BuilderState#tile_is_first.
  _BuilderState.tile_is_last: _BuilderState#tile_is_last.
  _rank_token_count_before: _rank_token_count_before().
  PcpStageMetadata.request_id: PcpStageMetadata#request_id.
  PcpStageMetadata.query_row_start: PcpStageMetadata#query_row_start.
  PcpStageMetadata.num_tiles: PcpStageMetadata#num_tiles.
  PcpStageMetadata.projection_work_offset: PcpStageMetadata#projection_work_offset.
  _compute_pcp_stage_metadata_from_coordinates._emit_request._windows_pending: _compute_pcp_stage_metadata_from_coordinates()._emit_request()._windows_pending().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py)

## Classes
### <a id="PcpStageMetadata"></a>`PcpStageMetadata`
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py:40`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L40)
- doc: Replicated schedule consumed by the PCP Pallas kernel.
- signature: `class PcpStageMetadata:`
- members:
  - <a id="PcpStageMetadata.first_tile"></a>`first_tile` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L62)
  - <a id="PcpStageMetadata.num_stages"></a>`num_stages` — [`L54`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L54)
  - <a id="PcpStageMetadata.num_tiles"></a>`num_tiles` — [`L63`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L63)
  - <a id="PcpStageMetadata.num_tokens"></a>`num_tokens` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L58)
  - <a id="PcpStageMetadata.projection_catchup_count"></a>`projection_catchup_count` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L67)
  - <a id="PcpStageMetadata.projection_catchup_start"></a>`projection_catchup_start` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L66)
  - <a id="PcpStageMetadata.projection_work_offset"></a>`projection_work_offset` — [`L68`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L68)
  - <a id="PcpStageMetadata.projection_work_offset_end"></a>`projection_work_offset_end` — [`L69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L69)
  - <a id="PcpStageMetadata.query_row_start"></a>`query_row_start` — [`L57`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L57)
  - <a id="PcpStageMetadata.rank_active_row_end"></a>`rank_active_row_end` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L55)
  - <a id="PcpStageMetadata.rank_recv_start"></a>`rank_recv_start` — [`L61`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L61)
  - <a id="PcpStageMetadata.rank_row_start"></a>`rank_row_start` — [`L59`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L59)
  - <a id="PcpStageMetadata.rank_valid_rows"></a>`rank_valid_rows` — [`L60`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L60)
  - <a id="PcpStageMetadata.request_id"></a>`request_id` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L56)
  - <a id="PcpStageMetadata.tile_row_in_stage"></a>`tile_row_in_stage` — [`L65`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L65)
  - <a id="PcpStageMetadata.tile_stage"></a>`tile_stage` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L64)
- used by: [`_compute_pcp_stage_metadata_from_coordinates`](pcp_metadata.md#_compute_pcp_stage_metadata_from_coordinates), [`_pcp_qkvz_projection_gdn_outer_kernel`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel), [`_compute_gdn_tile`](pcp_wrapper.md#_compute_gdn_tile), [`_run`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel._run), [`_run_projection_catchup`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel._run_projection_catchup), [`_start_output_stage`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel._start_output_stage), [`_start_packed_qkv_copy`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel._start_packed_qkv_copy), [`compute_pcp_stage_metadata`](pcp_metadata.md#compute_pcp_stage_metadata), [`_wait_qkv_send`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel._wait_qkv_send), [`_wait_qkv_recv`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel._wait_qkv_recv), [`_wait_output_stage`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel._wait_output_stage), [`_stage_prologue`](pcp_wrapper.md#_pcp_qkvz_projection_gdn_outer_kernel._stage_prologue)

### <a id="_BuilderState"></a>`_BuilderState`
- def: [`src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py:74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L74)
- signature: `class _BuilderState:`
- members:
  - <a id="_BuilderState.active_stages"></a>`active_stages` — [`L76`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L76)
  - <a id="_BuilderState.active_tiles"></a>`active_tiles` — [`L77`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L77)
  - <a id="_BuilderState.first_tile"></a>`first_tile` — [`L86`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L86)
  - <a id="_BuilderState.num_tokens"></a>`num_tokens` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L82)
  - <a id="_BuilderState.query_row_start"></a>`query_row_start` — [`L81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L81)
  - <a id="_BuilderState.rank_active_row_end"></a>`rank_active_row_end` — [`L79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L79)
  - <a id="_BuilderState.rank_recv_start"></a>`rank_recv_start` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L85)
  - <a id="_BuilderState.rank_row_offsets"></a>`rank_row_offsets` — [`L78`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L78)
  - <a id="_BuilderState.rank_row_start"></a>`rank_row_start` — [`L83`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L83)
  - <a id="_BuilderState.rank_valid_rows"></a>`rank_valid_rows` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L84)
  - <a id="_BuilderState.request_id"></a>`request_id` — [`L80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L80)
  - <a id="_BuilderState.request_index"></a>`request_index` — [`L75`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L75)
  - <a id="_BuilderState.stage_num_tiles"></a>`stage_num_tiles` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L87)
  - <a id="_BuilderState.tile_is_first"></a>`tile_is_first` — [`L93`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L93)
  - <a id="_BuilderState.tile_is_last"></a>`tile_is_last` — [`L94`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L94)
  - <a id="_BuilderState.tile_num_tokens"></a>`tile_num_tokens` — [`L92`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L92)
  - <a id="_BuilderState.tile_query_row_start"></a>`tile_query_row_start` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L91)
  - <a id="_BuilderState.tile_request_id"></a>`tile_request_id` — [`L90`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L90)
  - <a id="_BuilderState.tile_row_in_stage"></a>`tile_row_in_stage` — [`L89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L89)
  - <a id="_BuilderState.tile_stage"></a>`tile_stage` — [`L88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L88)
- used by: [`_compute_pcp_stage_metadata_from_coordinates`](pcp_metadata.md#_compute_pcp_stage_metadata_from_coordinates), [`_emit_request`](pcp_metadata.md#_compute_pcp_stage_metadata_from_coordinates._emit_request), [`_plan_projection_catchup`](pcp_metadata.md#_compute_pcp_stage_metadata_from_coordinates._plan_projection_catchup), [`_requests_pending`](pcp_metadata.md#_compute_pcp_stage_metadata_from_coordinates._requests_pending), [`_set_body_projection_offset`](pcp_metadata.md#_compute_pcp_stage_metadata_from_coordinates._set_body_projection_offset)

## Functions
- <a id="_compute_pcp_stage_metadata_from_coordinates"></a>`_compute_pcp_stage_metadata_from_coordinates(cfg: config.GDNConfig, query_start_loc: jax.Array, state_indices: jax.Array, start_seq: jax.Array, end_seq: jax.Array, *, token_owner_starts: jax.Array, request_absolute_starts: jax.Array, pcp_size: int, comm_chunk_size: int, projection_token_block_size: int, num_qkv_out_blocks: int, num_projection_out_blocks: int)` — [`L175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L175) — Build live PCP stages and GDN tiles from independent coordinates. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="_compute_pcp_stage_metadata_from_coordinates._emit_request._emit_window._emit_rank_tiles"></a>`_emit_rank_tiles(source_rank, rank_state)` — [`L322`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L322)
- <a id="_compute_pcp_stage_metadata_from_coordinates._emit_request"></a>`_emit_request(state: _BuilderState)` — [`L265`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L265) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="_compute_pcp_stage_metadata_from_coordinates._emit_request._emit_window._emit_rank_tiles._emit_tile"></a>`_emit_tile(tile_in_rank, tile_state)` — [`L338`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L338)
- <a id="_compute_pcp_stage_metadata_from_coordinates._emit_request._emit_window"></a>`_emit_window(carry)` — [`L296`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L296)
- <a id="_compute_pcp_stage_metadata_from_coordinates._plan_projection_catchup"></a>`_plan_projection_catchup(stage, carry)` — [`L460`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L460) — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="_rank_token_count_before"></a>`_rank_token_count_before(position: jax.Array, ranks: jax.Array, *, pcp_size: int, comm_chunk_size: int)` — [`L97`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L97)
- <a id="_compute_pcp_stage_metadata_from_coordinates._requests_pending"></a>`_requests_pending(state: _BuilderState)` — [`L262`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L262)
- <a id="_schedule_capacities"></a>`_schedule_capacities(cfg: config.GDNConfig, *, max_num_seqs: int, pcp_size: int, comm_chunk_size: int)` — [`L112`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L112) — Return safe static storage capacities for stages and split tiles. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)
- <a id="_compute_pcp_stage_metadata_from_coordinates._set_body_projection_offset"></a>`_set_body_projection_offset(stage, work_offsets)` — [`L522`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L522)
- <a id="_compute_pcp_stage_metadata_from_coordinates._emit_request._windows_pending"></a>`_windows_pending(carry)` — [`L292`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L292)
- <a id="compute_pcp_stage_metadata"></a>`compute_pcp_stage_metadata(cfg: config.GDNConfig, seq_lens: jax.Array, query_start_loc: jax.Array, state_indices: jax.Array, start_seq: jax.Array, end_seq: jax.Array, *, pcp_size: int, comm_chunk_size: int, projection_token_block_size: int, num_qkv_out_blocks: int, num_projection_out_blocks: int)` — [`L132`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/gdn_pcp_fused/pcp_metadata.py#L132) — Build PCP metadata from the current public request metadata. — documented in [gdn-pcp-fused-kernel](../../../../../../concepts/gdn-pcp-fused-kernel.md)

