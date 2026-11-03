---
title: 'Module: src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.pcp_streaming_rpa.reference`/
symbols:
  build_runtime_schedule_reference: build_runtime_schedule_reference().
  _set_common_fields: _set_common_fields().
  _new_rows: _new_rows().
  _rank_token_count_before: _rank_token_count_before().
  RuntimeScheduleReference: RuntimeScheduleReference#
  _local_page_valid_len: _local_page_valid_len().
  RuntimeScheduleReference.current_rows: RuntimeScheduleReference#current_rows.
  RuntimeScheduleReference.history_rows: RuntimeScheduleReference#history_rows.
  RuntimeScheduleReference.current_num_groups: RuntimeScheduleReference#current_num_groups.
  RuntimeScheduleReference.history_num_groups: RuntimeScheduleReference#history_num_groups.
---
# Module: [`src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py)

## Classes
### <a id="RuntimeScheduleReference"></a>`RuntimeScheduleReference`
- def: [`src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py:27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py#L27)
- doc: Current/history runtime rows expanded from one production tile plan.
- signature: `class RuntimeScheduleReference:`
- members:
  - <a id="RuntimeScheduleReference.current_num_groups"></a>`current_num_groups` — [`L38`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py#L38)
  - <a id="RuntimeScheduleReference.current_rows"></a>`current_rows` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py#L36)
  - <a id="RuntimeScheduleReference.history_num_groups"></a>`history_num_groups` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py#L39)
  - <a id="RuntimeScheduleReference.history_rows"></a>`history_rows` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py#L37)
- used by: [`build_runtime_schedule_reference`](reference.md#build_runtime_schedule_reference)

## Functions
- <a id="_local_page_valid_len"></a>`_local_page_valid_len(kv_len: int, local_page_idx: int, source_rank: int, *, page_size: int, pcp_size: int, interleave_size: int)` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py#L53)
- <a id="_new_rows"></a>`_new_rows(num_tiles: int, max_groups: int, pcp_size: int)` — [`L74`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py#L74)
- <a id="_rank_token_count_before"></a>`_rank_token_count_before(position: int, rank: int, *, pcp_size: int, interleave_size: int)` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py#L42)
- <a id="_set_common_fields"></a>`_set_common_fields(row: np.ndarray, plan: np.ndarray, consumer_rank: int, *, req_id: int, kv_page_idx: int, kv_global_start: int, kv_valid_len: int, kv_hbm_offset: int)` — [`L89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py#L89) — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="build_runtime_schedule_reference"></a>`build_runtime_schedule_reference(tile_plan: np.ndarray, block_tables: np.ndarray, *, pcp_size: int, page_size: int, interleave_size: int)` — [`L116`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/reference.py#L116) — Expand production tile metadata into the rows staged by Pallas. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)

