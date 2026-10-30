---
title: 'Module: torchtitan/distributed/minimal_async_ep/kernels.py'
type: catalog
provenance: extracted
module: torchtitan/distributed/minimal_async_ep/kernels.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.distributed.minimal_async_ep.kernels`/
symbols:
  copy_rows_to_peers_kernel: copy_rows_to_peers_kernel().
  reduce_topk_slots_kernel: reduce_topk_slots_kernel().
  copy_full_counts_to_peers_kernel: copy_full_counts_to_peers_kernel().
  fill_dispatch_metadata_kernel: fill_dispatch_metadata_kernel().
  fill_combine_metadata_kernel: fill_combine_metadata_kernel().
  invert_flat_indices_kernel: invert_flat_indices_kernel().
  expand_topk_grad_kernel: expand_topk_grad_kernel().
  topk_scores_grad_kernel: topk_scores_grad_kernel().
  _MAX_BLOCK_N: _MAX_BLOCK_N.
  _COUNT_COPY_BLOCK_SIZE: _COUNT_COPY_BLOCK_SIZE.
  _METADATA_BLOCK_SIZE: _METADATA_BLOCK_SIZE.
  _HIDDEN_ROW_DTYPES: _HIDDEN_ROW_DTYPES.
  _copy_full_counts_to_peer_ptrs_kernel: _copy_full_counts_to_peer_ptrs_kernel().
  _fill_dispatch_metadata_kernel: _fill_dispatch_metadata_kernel().
  _fill_combine_metadata_kernel: _fill_combine_metadata_kernel().
  _invert_flat_indices_kernel: _invert_flat_indices_kernel().
  _reduce_topk_slots_kernel: _reduce_topk_slots_kernel().
  _expand_topk_grad_kernel: _expand_topk_grad_kernel().
  _topk_scores_grad_kernel: _topk_scores_grad_kernel().
  _copy_rows_to_peer_ptrs_kernel: _copy_rows_to_peer_ptrs_kernel().
---
# Module: [`torchtitan/distributed/minimal_async_ep/kernels.py`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py)

## Functions
- <a id="_copy_full_counts_to_peer_ptrs_kernel"></a>`_copy_full_counts_to_peer_ptrs_kernel(counts: tl.pointer_type(tl.int64), dst_ptrs: tl.pointer_type(tl.int64), rank: tl.int64, EP_SIZE: tl.constexpr, NUM_EXPERTS: tl.constexpr, DST_ROW_STRIDE: tl.constexpr, BLOCK_SIZE: tl.constexpr)` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L27) — Copy this rank's global expert counts into every peer count buffer.
- <a id="_copy_rows_to_peer_ptrs_kernel"></a>`_copy_rows_to_peer_ptrs_kernel(src, dst_ptrs: tl.pointer_type(tl.int64), dst_ranks: tl.pointer_type(tl.int64), dst_rows: tl.pointer_type(tl.int64), num_valid_rows: tl.pointer_type(tl.int64), src_rows: tl.pointer_type(tl.int64), NUM_ROWS: tl.constexpr, NUM_COLS: tl.constexpr, SRC_ROW_STRIDE: tl.constexpr, SRC_COL_STRIDE: tl.constexpr, DST_ROW_STRIDE: tl.constexpr, DST_DTYPE: tl.constexpr, HAS_NUM_VALID_ROWS: tl.constexpr, HAS_SRC_ROWS: tl.constexpr, BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr)` — [`L292`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L292) — Copy rows into peer symmetric hidden buffers through pointer tables.
- <a id="_expand_topk_grad_kernel"></a>`_expand_topk_grad_kernel(grad_out, flat_indices: tl.pointer_type(tl.int64), scores, grad_routed, NUM_ROWS: tl.constexpr, NUM_COLS: tl.constexpr, TOP_K: tl.constexpr, HAS_SCORES: tl.constexpr, SCORES_ARE_SLOT_ORDERED: tl.constexpr, GRAD_OUT_ROW_STRIDE: tl.constexpr, GRAD_OUT_COL_STRIDE: tl.constexpr, GRAD_ROUTED_ROW_STRIDE: tl.constexpr, GRAD_ROUTED_COL_STRIDE: tl.constexpr, BLOCK_N: tl.constexpr)` — [`L199`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L199) — Expand token gradients into expert-sorted routed-row gradients.
- <a id="_fill_combine_metadata_kernel"></a>`_fill_combine_metadata_kernel(segment_lens: tl.pointer_type(tl.int64), output_starts: tl.pointer_type(tl.int64), source_input_starts: tl.pointer_type(tl.int64), dst_ranks: tl.pointer_type(tl.int64), dst_rows: tl.pointer_type(tl.int64), ep_rank: tl.int64, EP_SIZE: tl.constexpr, NUM_LOCAL_EXPERTS: tl.constexpr, NUM_EXPERTS: tl.constexpr, BLOCK_SIZE: tl.constexpr)` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L87) — Build per-active-row peer destinations for the combine copy.
- <a id="_fill_dispatch_metadata_kernel"></a>`_fill_dispatch_metadata_kernel(counts: tl.pointer_type(tl.int64), local_dest_offsets: tl.pointer_type(tl.int64), local_count_starts: tl.pointer_type(tl.int64), dst_ranks: tl.pointer_type(tl.int64), dst_rows: tl.pointer_type(tl.int64), NUM_EXPERTS: tl.constexpr, NUM_LOCAL_EXPERTS: tl.constexpr, BLOCK_SIZE: tl.constexpr)` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L55) — Build per-routed-row peer destinations for the dispatch copy.
- <a id="_invert_flat_indices_kernel"></a>`_invert_flat_indices_kernel(flat_indices: tl.pointer_type(tl.int64), slot_to_row: tl.pointer_type(tl.int64), NUM_ROWS: tl.constexpr, BLOCK_SIZE: tl.constexpr)` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L129) — Invert routed-row to top-k-slot indices into top-k-slot to routed-row.
- <a id="_reduce_topk_slots_kernel"></a>`_reduce_topk_slots_kernel(routed_output, slot_to_row: tl.pointer_type(tl.int64), scores, out, NUM_COLS: tl.constexpr, TOP_K: tl.constexpr, HAS_SCORES: tl.constexpr, SCORES_ARE_SLOT_ORDERED: tl.constexpr, ROUTED_ROW_STRIDE: tl.constexpr, ROUTED_COL_STRIDE: tl.constexpr, OUT_ROW_STRIDE: tl.constexpr, OUT_COL_STRIDE: tl.constexpr, BLOCK_N: tl.constexpr)` — [`L148`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L148) — Reduce expert-sorted routed rows back to origin token rows.
- <a id="_topk_scores_grad_kernel"></a>`_topk_scores_grad_kernel(routed_output, grad_out, flat_indices: tl.pointer_type(tl.int64), grad_scores, NUM_COLS: tl.constexpr, TOP_K: tl.constexpr, ROUTED_ROW_STRIDE: tl.constexpr, ROUTED_COL_STRIDE: tl.constexpr, GRAD_OUT_ROW_STRIDE: tl.constexpr, GRAD_OUT_COL_STRIDE: tl.constexpr, SCORES_ARE_SLOT_ORDERED: tl.constexpr, BLOCK_N: tl.constexpr)` — [`L247`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L247) — Compute routing-score gradients for each local routed row.
- <a id="copy_full_counts_to_peers_kernel"></a>`copy_full_counts_to_peers_kernel(counts: torch.Tensor, dsts: list[torch.Tensor], *, rank: int, ep_size: int, num_experts: int, dst_ptrs: torch.Tensor)` — [`L351`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L351)
- <a id="copy_rows_to_peers_kernel"></a>`copy_rows_to_peers_kernel(src: torch.Tensor, dsts: list[torch.Tensor], dst_ranks: torch.Tensor, dst_rows: torch.Tensor, *, ep_size: int, num_rows: int, num_cols: int, dst_ptrs: torch.Tensor, block_m: int = 1, num_warps: int = 4, src_rows: torch.Tensor | None = None, num_valid_rows: torch.Tensor | None = None)` — [`L382`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L382)
- <a id="expand_topk_grad_kernel"></a>`expand_topk_grad_kernel(grad_out: torch.Tensor, flat_indices: torch.Tensor, scores: torch.Tensor | None, *, top_k: int, dtype: torch.dtype, scores_are_slot_ordered: bool = False)` — [`L562`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L562)
- <a id="fill_combine_metadata_kernel"></a>`fill_combine_metadata_kernel(segment_lens: torch.Tensor, output_starts: torch.Tensor, source_input_starts: torch.Tensor, *, ep_rank: int, ep_size: int, num_local_experts: int, receive_capacity: int, max_tokens_per_segment: int)` — [`L463`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L463)
- <a id="fill_dispatch_metadata_kernel"></a>`fill_dispatch_metadata_kernel(counts: torch.Tensor, local_dest_offsets: torch.Tensor, local_count_starts: torch.Tensor, *, num_routed_tokens: int, num_local_experts: int, max_tokens_per_segment: int)` — [`L426`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L426)
- <a id="invert_flat_indices_kernel"></a>`invert_flat_indices_kernel(flat_indices: torch.Tensor, *, num_rows: int)` — [`L508`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L508)
- <a id="reduce_topk_slots_kernel"></a>`reduce_topk_slots_kernel(routed_output: torch.Tensor, slot_to_row: torch.Tensor, scores: torch.Tensor | None, *, num_tokens: int, top_k: int, scores_are_slot_ordered: bool = False)` — [`L525`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L525)
- <a id="topk_scores_grad_kernel"></a>`topk_scores_grad_kernel(routed_output: torch.Tensor, grad_out: torch.Tensor, flat_indices: torch.Tensor, *, top_k: int, dtype: torch.dtype, scores_are_slot_ordered: bool = False)` — [`L602`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L602)

## Module values
- <a id="_COUNT_COPY_BLOCK_SIZE"></a>`_COUNT_COPY_BLOCK_SIZE` — [`L14`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L14)
- <a id="_HIDDEN_ROW_DTYPES"></a>`_HIDDEN_ROW_DTYPES` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L20)
- <a id="_MAX_BLOCK_N"></a>`_MAX_BLOCK_N` — [`L16`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L16)
- <a id="_METADATA_BLOCK_SIZE"></a>`_METADATA_BLOCK_SIZE` — [`L15`](../../../../../../../raw/code/torchtitan/torchtitan/distributed/minimal_async_ep/kernels.py#L15)

