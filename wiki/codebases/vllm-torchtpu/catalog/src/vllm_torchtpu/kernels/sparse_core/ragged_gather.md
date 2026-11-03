---
title: 'Module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.sparse_core.ragged_gather`/
symbols:
  ragged_gather: ragged_gather().
  main_kernel: main_kernel().
  main_kernel.inner_kernel: main_kernel().inner_kernel().
  calculate_col_size: calculate_col_size().
  main_kernel.inner_kernel.dma_write_loop: main_kernel().inner_kernel().dma_write_loop().
---
# Module: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather.py)

## Functions
- <a id="calculate_col_size"></a>`calculate_col_size(hidden_size: int)` — [`L213`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather.py#L213) — Calculate col size for ragged gather kernel.
- <a id="main_kernel.inner_kernel.dma_write_loop"></a>`dma_write_loop(col_vmem_start)` — [`L135`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather.py#L135)
- <a id="main_kernel.inner_kernel"></a>`inner_kernel()` — [`L85`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather.py#L85)
- <a id="main_kernel"></a>`main_kernel(start_ref: jax.Ref, end_ref: jax.Ref, in_hbm_ref: jax.Ref, indices_hbm_ref: jax.Ref, out_hbm_ref: jax.Ref, start_vmem_ref: jax.Ref, end_vmem_ref: jax.Ref, out_vmem_ref: jax.Ref, indices_vmem_ref: jax.Ref, sem_ref: jax.Ref, *, core_axis_name: str, subcore_axis_name: str)` — [`L26`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather.py#L26)
- <a id="ragged_gather"></a>`ragged_gather(x: jax.Array, indices: jax.Array, start: jax.Array, end: jax.Array)` — [`L238`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather.py#L238) — Perform gather on indices within dynamic array start and end. — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)

