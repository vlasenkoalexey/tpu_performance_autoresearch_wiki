---
title: 'Module: torchtitan/experiments/tpu/headtail.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/headtail.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.headtail`/
symbols:
  headtail_positions: headtail_positions().
  make_headtail_splash_mask: make_headtail_splash_mask().
  make_cp_segment_ids: make_cp_segment_ids().
  slice_cp_mask_info: slice_cp_mask_info().
  headtail_chunk_order: headtail_chunk_order().
  reorder_sequence_jax: reorder_sequence_jax().
  slice_cp_mask_info._slice: slice_cp_mask_info()._slice().
---
# Module: [`torchtitan/experiments/tpu/headtail.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/headtail.py)

## Functions
- <a id="slice_cp_mask_info._slice"></a>`_slice(x, axis: int)` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/headtail.py#L113) — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- <a id="headtail_chunk_order"></a>`headtail_chunk_order(cp_size: int)` — [`L16`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/headtail.py#L16) — Order of the ``2 * cp_size`` chunks: ``[0, 2cp-1, 1, 2cp-2, ...]``. — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- <a id="headtail_positions"></a>`headtail_positions(seq_len: int, cp_size: int)` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/headtail.py#L21) — Positions ``0..seq_len-1`` rearranged into head-tail order. — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- <a id="make_cp_segment_ids"></a>`make_cp_segment_ids(segment_ids_cls: Any, segment_ids_b: Any, cp_size: int, q_seq_len: int, cp_rank: Any = None)` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/headtail.py#L76) — Build Splash ``SegmentIds(q, kv)`` for one batch element under head-tail CP. — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- <a id="make_headtail_splash_mask"></a>`make_headtail_splash_mask(splash_attention_mask: Any, mask_shape: tuple[int, int], is_causal: bool, local_window_size: int | None, cp_size: int)` — [`L45`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/headtail.py#L45) — Single-head Splash mask; with CP, its Q rows are in head-tail order. — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- <a id="reorder_sequence_jax"></a>`reorder_sequence_jax(x: Any, cp_size: int)` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/headtail.py#L37) — Reorder a 1D JAX array of length S into head-tail load-balanced order. — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)
- <a id="slice_cp_mask_info"></a>`slice_cp_mask_info(mask_info: Any, cp_size: int, cp_rank: Any, field_axes: tuple[tuple[str, int], ...])` — [`L97`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/headtail.py#L97) — Slice a Splash/Tokamax ``MaskInfo`` for ``q_seq_shards=cp_size`` to ``cp_rank``. — documented in [tpu-context-parallel-attention](../../../../concepts/tpu-context-parallel-attention.md)

