---
title: 'Module: src/vllm_torchtpu/kernels/sparse_core/ragged_scatter.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/sparse_core/ragged_scatter.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.sparse_core.ragged_scatter`/
symbols:
  ragged_scatter: ragged_scatter().
  main_kernel: main_kernel().
  main_kernel.kernel_wrapper: main_kernel().kernel_wrapper().
  main_kernel.inner_kernel: main_kernel().inner_kernel().
  calculate_col_size: calculate_col_size().
  _preprocess_indices: _preprocess_indices().
  main_kernel.inner_kernel.dma_write_loop: main_kernel().inner_kernel().dma_write_loop().
---
# Module: [`src/vllm_torchtpu/kernels/sparse_core/ragged_scatter.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_scatter.py)

## Functions
- <a id="_preprocess_indices"></a>`_preprocess_indices(indices: jax.Array, start: jax.Array, end: jax.Array, out_pad_size: int, packing: int, row_tile_size: int)` — [`L289`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_scatter.py#L289) — Preprocesses indices for ragged scatter kernel.
- <a id="calculate_col_size"></a>`calculate_col_size(hidden_size: int)` — [`L265`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_scatter.py#L265) — Calculate col size for ragged gather kernel.
- <a id="main_kernel.inner_kernel.dma_write_loop"></a>`dma_write_loop(col_vmem_start)` — [`L127`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_scatter.py#L127)
- <a id="main_kernel.inner_kernel"></a>`inner_kernel(block_id, core_id, col_id)` — [`L69`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_scatter.py#L69)
- <a id="main_kernel.kernel_wrapper"></a>`kernel_wrapper()` — [`L250`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_scatter.py#L250)
- <a id="main_kernel"></a>`main_kernel(total_num_rows_ref: jax.Ref, in_hbm_ref: jax.Ref, src_indices_hbm_ref: jax.Ref, dst_indices_hbm_ref: jax.Ref, out_hbm_ref: jax.Ref, total_num_rows_vmem_ref: jax.Ref, out_vmem_ref: jax.Ref, src_indices_vmem_ref: jax.Ref, dst_indices_vmem_ref: jax.Ref, sem_ref: jax.Ref, *, core_axis_name: str, subcore_axis_name: str)` — [`L26`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_scatter.py#L26)
- <a id="ragged_scatter"></a>`ragged_scatter(x: jax.Array, indices: jax.Array, start: jax.Array, end: jax.Array)` — [`L354`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_scatter.py#L354) — Gathers rows from `x` according to `indices` within a specified range. — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)

