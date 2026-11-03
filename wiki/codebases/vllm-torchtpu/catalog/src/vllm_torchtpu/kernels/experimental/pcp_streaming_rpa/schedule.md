---
title: 'Module: src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.pcp_streaming_rpa.schedule`/
symbols:
  TilePlanField: TilePlanField#
  RuntimeScheduleField: RuntimeScheduleField#
  build_pcp_streaming_schedule_inputs_from_metadata_jax: build_pcp_streaming_schedule_inputs_from_metadata_jax().
  build_pcp_streaming_schedule_inputs_from_metadata_jax._broadcast_tile: build_pcp_streaming_schedule_inputs_from_metadata_jax()._broadcast_tile().
  TilePlanField.NUM_FIELDS: TilePlanField#NUM_FIELDS.
  build_pcp_streaming_schedule_inputs_from_metadata_jax._rank_token_count_before: build_pcp_streaming_schedule_inputs_from_metadata_jax()._rank_token_count_before().
  RuntimeScheduleField.PACKED_NUM_FIELDS: RuntimeScheduleField#PACKED_NUM_FIELDS.
  TilePlanField.REQ_ID: TilePlanField#REQ_ID.
  TilePlanField.Q_HBM_OFFSET: TilePlanField#Q_HBM_OFFSET.
  TilePlanField.Q_TILE_SIZE: TilePlanField#Q_TILE_SIZE.
  TilePlanField.WRITEBACK_HBM_PREFIX: TilePlanField#WRITEBACK_HBM_PREFIX.
  TilePlanField.HBM_ROW_FIELDS: TilePlanField#HBM_ROW_FIELDS.
  build_pcp_streaming_schedule_inputs_from_metadata_jax._rank_tile: build_pcp_streaming_schedule_inputs_from_metadata_jax()._rank_tile().
  RuntimeScheduleField.REQ_ID: RuntimeScheduleField#REQ_ID.
  RuntimeScheduleField.KV_PAGE_IDX: RuntimeScheduleField#KV_PAGE_IDX.
  RuntimeScheduleField.KV_VALID_LEN: RuntimeScheduleField#KV_VALID_LEN.
  RuntimeScheduleField.Q_HBM_OFFSET: RuntimeScheduleField#Q_HBM_OFFSET.
  RuntimeScheduleField.Q_TILE_SIZE: RuntimeScheduleField#Q_TILE_SIZE.
  RuntimeScheduleField.CAPTURE_SRC_OFFSET: RuntimeScheduleField#CAPTURE_SRC_OFFSET.
  RuntimeScheduleField.CAPTURE_DST_OFFSET: RuntimeScheduleField#CAPTURE_DST_OFFSET.
  RuntimeScheduleField.CAPTURE_LEN: RuntimeScheduleField#CAPTURE_LEN.
  TilePlanField.Q_GLOBAL_START: TilePlanField#Q_GLOBAL_START.
  TilePlanField.REQUEST_ABSOLUTE_QUERY_START: TilePlanField#REQUEST_ABSOLUTE_QUERY_START.
  TilePlanField.CURRENT_NUM_GROUPS: TilePlanField#CURRENT_NUM_GROUPS.
  TilePlanField.HISTORY_NUM_GROUPS: TilePlanField#HISTORY_NUM_GROUPS.
  query_row_positions: query_row_positions().
  _cdiv: _cdiv().
  _reshape_metadata_page_indices_jax: _reshape_metadata_page_indices_jax().
  build_pcp_streaming_schedule_inputs_from_metadata_jax._local_page_valid_len: build_pcp_streaming_schedule_inputs_from_metadata_jax()._local_page_valid_len().
  RuntimeScheduleField.Q_GLOBAL_START: RuntimeScheduleField#Q_GLOBAL_START.
  RuntimeScheduleField.KV_GLOBAL_START: RuntimeScheduleField#KV_GLOBAL_START.
  RuntimeScheduleField.KV_HBM_OFFSET: RuntimeScheduleField#KV_HBM_OFFSET.
  RuntimeScheduleField.NUM_FIELDS: RuntimeScheduleField#NUM_FIELDS.
  TilePlanField.TOKEN_OWNER_START: TilePlanField#TOKEN_OWNER_START.
  TilePlanField.CURRENT_EFFECTIVE_LEN: TilePlanField#CURRENT_EFFECTIVE_LEN.
  TilePlanField.CURRENT_KV_HBM_START: TilePlanField#CURRENT_KV_HBM_START.
  TilePlanField.CAPTURE_CURRENT_KV: TilePlanField#CAPTURE_CURRENT_KV.
  build_pcp_streaming_schedule_inputs_from_metadata_jax._compact_pass: build_pcp_streaming_schedule_inputs_from_metadata_jax()._compact_pass().
  _validate_page_interleave_size: _validate_page_interleave_size().
  build_pcp_streaming_schedule_inputs_from_metadata_jax._local_page_global_start: build_pcp_streaming_schedule_inputs_from_metadata_jax()._local_page_global_start().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py)

## Classes
### <a id="RuntimeScheduleField"></a>`RuntimeScheduleField`
- def: [`src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py:19`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L19) — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- doc: Minimal per-ring-step ABI consumed by the production Pallas kernels.
- signature: `class RuntimeScheduleField:`
- members:
  - <a id="RuntimeScheduleField.CAPTURE_DST_OFFSET"></a>`CAPTURE_DST_OFFSET` — [`L31`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L31)
  - <a id="RuntimeScheduleField.CAPTURE_LEN"></a>`CAPTURE_LEN` — [`L32`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L32)
  - <a id="RuntimeScheduleField.CAPTURE_SRC_OFFSET"></a>`CAPTURE_SRC_OFFSET` — [`L30`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L30)
  - <a id="RuntimeScheduleField.KV_GLOBAL_START"></a>`KV_GLOBAL_START` — [`L25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L25)
  - <a id="RuntimeScheduleField.KV_HBM_OFFSET"></a>`KV_HBM_OFFSET` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L29)
  - <a id="RuntimeScheduleField.KV_PAGE_IDX"></a>`KV_PAGE_IDX` — [`L23`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L23)
  - <a id="RuntimeScheduleField.KV_VALID_LEN"></a>`KV_VALID_LEN` — [`L26`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L26)
  - <a id="RuntimeScheduleField.NUM_FIELDS"></a>`NUM_FIELDS` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L33)
  - <a id="RuntimeScheduleField.PACKED_NUM_FIELDS"></a>`PACKED_NUM_FIELDS` — [`L34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L34)
  - <a id="RuntimeScheduleField.Q_GLOBAL_START"></a>`Q_GLOBAL_START` — [`L24`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L24)
  - <a id="RuntimeScheduleField.Q_HBM_OFFSET"></a>`Q_HBM_OFFSET` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L27)
  - <a id="RuntimeScheduleField.Q_TILE_SIZE"></a>`Q_TILE_SIZE` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L28)
  - <a id="RuntimeScheduleField.REQ_ID"></a>`REQ_ID` — [`L22`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L22)
- used by: [`build_runtime_schedule_reference`](reference.md#build_runtime_schedule_reference), [`_stage_current_schedule_step_from_tile_plan`](kernel.md#_stage_current_schedule_step_from_tile_plan), [`_run_page_group`](kernel.md#_run_pcp_page_groups_multi_head._run_page_group), [`_set_common_fields`](reference.md#_set_common_fields), [`_stage_history_schedule_step_from_tile_plan`](kernel.md#_stage_history_schedule_step_from_tile_plan), [`_consume_scheduled_kv_page_multi_head`](kernel.md#_consume_scheduled_kv_page_multi_head), [`_pcp_streaming_attention_current_state_page_groups_multi_head_pallas_call`](kernel.md#_pcp_streaming_attention_current_state_page_groups_multi_head_pallas_call), [`_pcp_streaming_attention_history_output_page_groups_multi_head_pallas_call`](kernel.md#_pcp_streaming_attention_history_output_page_groups_multi_head_pallas_call), [`_round_loop`](kernel.md#_run_pcp_page_groups_multi_head._run_page_group._round_loop), [`_load_local_current_or_boundary_kv_all_heads_packed`](kernel.md#_load_local_current_or_boundary_kv_all_heads_packed), [`_load_local_kv_page_all_heads_packed`](kernel.md#_load_local_kv_page_all_heads_packed), [`_new_rows`](reference.md#_new_rows)

### <a id="TilePlanField"></a>`TilePlanField`
- def: [`src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py:37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L37) — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- doc: Fields stored once per query tile and PCP consumer rank.
- signature: `class TilePlanField:`
- members:
  - <a id="TilePlanField.CAPTURE_CURRENT_KV"></a>`CAPTURE_CURRENT_KV` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L49)
  - <a id="TilePlanField.CURRENT_EFFECTIVE_LEN"></a>`CURRENT_EFFECTIVE_LEN` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L46)
  - <a id="TilePlanField.CURRENT_KV_HBM_START"></a>`CURRENT_KV_HBM_START` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L47)
  - <a id="TilePlanField.CURRENT_NUM_GROUPS"></a>`CURRENT_NUM_GROUPS` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L50)
  - <a id="TilePlanField.HBM_ROW_FIELDS"></a>`HBM_ROW_FIELDS` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L53)
  - <a id="TilePlanField.HISTORY_NUM_GROUPS"></a>`HISTORY_NUM_GROUPS` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L51)
  - <a id="TilePlanField.NUM_FIELDS"></a>`NUM_FIELDS` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L52)
  - <a id="TilePlanField.Q_GLOBAL_START"></a>`Q_GLOBAL_START` — [`L41`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L41)
  - <a id="TilePlanField.Q_HBM_OFFSET"></a>`Q_HBM_OFFSET` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L42)
  - <a id="TilePlanField.Q_TILE_SIZE"></a>`Q_TILE_SIZE` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L43)
  - <a id="TilePlanField.REQUEST_ABSOLUTE_QUERY_START"></a>`REQUEST_ABSOLUTE_QUERY_START` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L45)
  - <a id="TilePlanField.REQ_ID"></a>`REQ_ID` — [`L40`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L40)
  - <a id="TilePlanField.TOKEN_OWNER_START"></a>`TOKEN_OWNER_START` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L44)
  - <a id="TilePlanField.WRITEBACK_HBM_PREFIX"></a>`WRITEBACK_HBM_PREFIX` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L48)
- used by: [`build_runtime_schedule_reference`](reference.md#build_runtime_schedule_reference), [`_stage_current_schedule_step_from_tile_plan`](kernel.md#_stage_current_schedule_step_from_tile_plan), [`_run_page_group`](kernel.md#_run_pcp_page_groups_multi_head._run_page_group), [`_set_common_fields`](reference.md#_set_common_fields), [`_stage_history_schedule_step_from_tile_plan`](kernel.md#_stage_history_schedule_step_from_tile_plan), [`build_pcp_streaming_schedule_inputs_from_metadata_jax`](schedule.md#build_pcp_streaming_schedule_inputs_from_metadata_jax), [`_page_group_loop`](kernel.md#_pcp_streaming_attention_zero_history_output_multi_head_kernel._page_group_loop), [`_tile_plan_value_static`](kernel.md#_tile_plan_value_static), [`_tile_plan_value`](kernel.md#_tile_plan_value), [`_load_tile_metadata`](kernel.md#_run_pcp_page_groups_multi_head._run_page_group._load_tile_metadata)

## Functions
- <a id="build_pcp_streaming_schedule_inputs_from_metadata_jax._broadcast_tile"></a>`_broadcast_tile(values)` — [`L356`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L356)
- <a id="_cdiv"></a>`_cdiv(x: int, y: int)` — [`L75`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L75)
- <a id="build_pcp_streaming_schedule_inputs_from_metadata_jax._compact_pass"></a>`_compact_pass(num_groups)` — [`L394`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L394)
- <a id="build_pcp_streaming_schedule_inputs_from_metadata_jax._local_page_global_start"></a>`_local_page_global_start(local_page_idx, src_rank)` — [`L189`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L189)
- <a id="build_pcp_streaming_schedule_inputs_from_metadata_jax._local_page_valid_len"></a>`_local_page_valid_len(kv_len, local_page_idx, src_rank)` — [`L192`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L192)
- <a id="build_pcp_streaming_schedule_inputs_from_metadata_jax._rank_tile"></a>`_rank_tile(q_len, token_owner_start, request_absolute_query_start, rank_local_prefix, consumer_rank, tile_idx)` — [`L208`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L208)
- <a id="build_pcp_streaming_schedule_inputs_from_metadata_jax._rank_token_count_before"></a>`_rank_token_count_before(position, rank)` — [`L237`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L237)
- <a id="_reshape_metadata_page_indices_jax"></a>`_reshape_metadata_page_indices_jax(page_indices, max_num_seqs: int)` — [`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L91)
- <a id="_validate_page_interleave_size"></a>`_validate_page_interleave_size(page_size: int, interleave_size: int, context: str)` — [`L79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L79)
- <a id="build_pcp_streaming_schedule_inputs_from_metadata_jax"></a>`build_pcp_streaming_schedule_inputs_from_metadata_jax(kv_lens, page_indices, cu_q_lens, distribution, *, global_bucket_tokens: int, local_kv_cache_num_blocks: int, page_size: int, pcp_size: int, interleave_size: int, q_block_size: int, num_lanes: int = 1)` — [`L112`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L112) — Build the single production current/history tile plan with JAX ops. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="query_row_positions"></a>`query_row_positions(q_global_start, q_hbm_offset, row, *, pcp_size, interleave_size)` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/schedule.py#L56) — Map compact local Q rows to request-absolute causal positions.

