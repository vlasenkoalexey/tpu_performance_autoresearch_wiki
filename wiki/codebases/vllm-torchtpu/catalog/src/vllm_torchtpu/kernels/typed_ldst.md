---
title: 'Module: src/vllm_torchtpu/kernels/typed_ldst.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/typed_ldst.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.typed_ldst`/
symbols:
  load_typed: load_typed().
  store_typed: store_typed().
  _typed_view: _typed_view().
---
# Module: [`src/vllm_torchtpu/kernels/typed_ldst.py`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/typed_ldst.py)

## Functions
- <a id="_typed_view"></a>`_typed_view(block_ref, view_dtype, lane_split: int)` — [`L33`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/typed_ldst.py#L33) — Raw block ref as a ``(rows, lanes // lane_split)`` view_dtype ref.
- <a id="load_typed"></a>`load_typed(block_ref, *, view_dtype, lane_split: int = 1)` — [`L40`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/typed_ldst.py#L40) — Reads a raw block ref as ``(rows, lanes // lane_split)`` view_dtype.
- <a id="store_typed"></a>`store_typed(block_ref, values: jax.Array, *, lane_split: int = 1)` — [`L45`](../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/typed_ldst.py#L45) — Inverse of ``load_typed``: stores ``values`` through a typed view of

