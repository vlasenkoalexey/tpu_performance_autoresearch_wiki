---
title: 'Module: src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/pcp_layout.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/pcp_layout.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.experimental.pcp_streaming_rpa.pcp_layout`/
symbols:
  pcp_local_token_counts: pcp_local_token_counts().
  build_pcp_rank_major_token_order: build_pcp_rank_major_token_order().
  _resolve_token_owner_start_offsets: _resolve_token_owner_start_offsets().
  apply_pcp_rank_major_token_order: apply_pcp_rank_major_token_order().
  build_pcp_logits_indices: build_pcp_logits_indices().
  pcp_query_chunk_ranges: pcp_query_chunk_ranges().
  pcp_token_owner_chunk_ranges: pcp_token_owner_chunk_ranges().
  pcp_token_owner_start_offsets: pcp_token_owner_start_offsets().
---
# Module: [`src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/pcp_layout.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/pcp_layout.py)

## Functions
- <a id="_resolve_token_owner_start_offsets"></a>`_resolve_token_owner_start_offsets(num_scheduled_tokens_per_req: np.ndarray, token_owner_start_offsets_per_req: list[int] | np.ndarray | None, token_start_offsets_per_req: list[int] | np.ndarray | None)` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/pcp_layout.py#L37) — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="apply_pcp_rank_major_token_order"></a>`apply_pcp_rank_major_token_order(input_ids_cpu: np.ndarray, positions_cpu: np.ndarray, num_scheduled_tokens_per_req: list[int] | np.ndarray, pcp_size: int, interleave_size: int, padded_num_tokens: int, mrope_positions_cpu: np.ndarray | None = None, token_owner_start_offsets_per_req: list[int] | np.ndarray | None = None, *, token_start_offsets_per_req: list[int] | np.ndarray | None = None)` — [`L190`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/pcp_layout.py#L190) — Reorder per-DP token arrays into PCP rank-major chunk order. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="build_pcp_logits_indices"></a>`build_pcp_logits_indices(num_scheduled_tokens_per_req: list[int] | np.ndarray, pcp_size: int, interleave_size: int, padded_num_tokens: int, token_offset: int = 0, token_owner_start_offsets_per_req: list[int] | np.ndarray | None = None, *, token_start_offsets_per_req: list[int] | np.ndarray | None = None)` — [`L226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/pcp_layout.py#L226) — Return global packed indices for each request's last query token. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="build_pcp_rank_major_token_order"></a>`build_pcp_rank_major_token_order(num_scheduled_tokens_per_req: list[int] | np.ndarray, pcp_size: int, interleave_size: int, padded_num_tokens: int, token_owner_start_offsets_per_req: list[int] | np.ndarray | None = None, *, token_start_offsets_per_req: list[int] | np.ndarray | None = None)` — [`L120`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/pcp_layout.py#L120) — Build token reorder indices for rank-major PCP chunk packing. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="pcp_local_token_counts"></a>`pcp_local_token_counts(num_scheduled_tokens_per_req: list[int] | np.ndarray, pcp_size: int, interleave_size: int, token_owner_start_offsets_per_req: list[int] | np.ndarray | None = None, *, token_start_offsets_per_req: list[int] | np.ndarray | None = None)` — [`L88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/pcp_layout.py#L88) — Return local token counts for each PCP rank under chunk interleave. — documented in [pcp-streaming-rpa-kernel](../../../../../../concepts/pcp-streaming-rpa-kernel.md)
- <a id="pcp_query_chunk_ranges"></a>`pcp_query_chunk_ranges(q_len: int, q_global_base: int, pcp_rank: int, pcp_size: int, interleave_size: int)` — [`L79`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/pcp_layout.py#L79) — Compatibility alias for :func:`pcp_token_owner_chunk_ranges`.
- <a id="pcp_token_owner_chunk_ranges"></a>`pcp_token_owner_chunk_ranges(q_len: int, token_owner_start: int, pcp_rank: int, pcp_size: int, interleave_size: int)` — [`L56`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/pcp_layout.py#L56) — Yield absolute owner-coordinate ranges assigned to one PCP rank.
- <a id="pcp_token_owner_start_offsets"></a>`pcp_token_owner_start_offsets(num_scheduled_tokens_per_req: np.ndarray, token_owner_start_offsets_per_req: list[int] | np.ndarray | None)` — [`L19`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/experimental/pcp_streaming_rpa/pcp_layout.py#L19) — Normalize the coordinate used to assign query tokens to PCP ranks.

