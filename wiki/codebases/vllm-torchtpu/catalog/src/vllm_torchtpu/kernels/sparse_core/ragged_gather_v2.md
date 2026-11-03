---
title: 'Module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_v2.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_v2.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.sparse_core.ragged_gather_v2`/
symbols:
  ragged_gather_v2: ragged_gather_v2().
  main_kernel_v2: main_kernel_v2().
  main_kernel_v2.inner_pipeline: main_kernel_v2().inner_pipeline().
  main_kernel_v2.outer_pipeline: main_kernel_v2().outer_pipeline().
  calculate_col_size: calculate_col_size().
  main_kernel_v2.col_loop: main_kernel_v2().col_loop().
---
# Module: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_v2.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_v2.py)

## Functions
- <a id="calculate_col_size"></a>`calculate_col_size(hidden_size: int, packing: int)` — [`L27`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_v2.py#L27) — Calculates the max column size bounded by VMEM limits and
- <a id="main_kernel_v2.col_loop"></a>`col_loop(col_base, gather_ref, out_ref, idx_rem, unpack_col_chunk)` — [`L126`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_v2.py#L126)
- <a id="main_kernel_v2.inner_pipeline"></a>`inner_pipeline(gather_ref, out_ref, idx_ref, unpack_col_chunk)` — [`L153`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_v2.py#L153)
- <a id="main_kernel_v2"></a>`main_kernel_v2(start_ref: jax.Ref, end_ref: jax.Ref, in_hbm_ref: jax.Ref, indices_hbm_ref: jax.Ref, out_hbm_ref: jax.Ref, start_vmem_ref: jax.Ref, end_vmem_ref: jax.Ref, sem_ref: jax.Ref, *, core_axis_name: str, subcore_axis_name: str, num_row_subchunks: int)` — [`L51`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_v2.py#L51) — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="main_kernel_v2.outer_pipeline"></a>`outer_pipeline(idx_ref)` — [`L171`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_v2.py#L171)
- <a id="ragged_gather_v2"></a>`ragged_gather_v2(x: jax.Array, indices: jax.Array, start: jax.Array, end: jax.Array)` — [`L213`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_v2.py#L213) — Perform gather on indices within dynamic array start and end using BlockSpec. — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)

