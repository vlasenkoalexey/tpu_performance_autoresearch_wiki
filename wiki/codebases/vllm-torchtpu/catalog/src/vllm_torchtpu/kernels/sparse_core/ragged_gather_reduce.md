---
title: 'Module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.sparse_core.ragged_gather_reduce`/
symbols:
  ragged_gather_reduce: ragged_gather_reduce().
  _pad_inputs_if_needed: _pad_inputs_if_needed().
  main_kernel: main_kernel().
  _align_to: _align_to().
  _fallback_implementation: _fallback_implementation().
  _calculate_num_col_column_partitions: _calculate_num_col_column_partitions().
  main_kernel.inner_kernel: main_kernel().inner_kernel().
  _preprocess: _preprocess().
  main_kernel.inner_kernel.row_loop: main_kernel().inner_kernel().row_loop().
  main_kernel.inner_kernel.row_loop.dma_write_loop: main_kernel().inner_kernel().row_loop().dma_write_loop().
---
# Module: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py)

## Functions
- <a id="_align_to"></a>`_align_to(a, b)` — [`L28`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py#L28)
- <a id="_calculate_num_col_column_partitions"></a>`_calculate_num_col_column_partitions(hidden_size: int, num_cores: int, num_lanes: int)` — [`L80`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py#L80) — Calculates the number of row partitions.
- <a id="_fallback_implementation"></a>`_fallback_implementation(x: jax.Array, indices: jax.Array, topk_weights: jax.Array, valid_rows_mask: jax.Array, reduce_group_size: int)` — [`L32`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py#L32)
- <a id="_pad_inputs_if_needed"></a>`_pad_inputs_if_needed(x: jax.Array, indices: jax.Array, topk_weights: jax.Array, valid_rows_mask: jax.Array, reduce_group_size: int, num_column_partitions: int, num_row_partitions: int, num_simd_lanes: int)` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py#L46) — Pads inputs if needed.
- <a id="_preprocess"></a>`_preprocess(indices: jax.Array, valid_rows_mask: jax.Array, reduce_group_size: int, num_row_partitions: int, num_simd_lanes: int)` — [`L398`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py#L398) — Preprocesses indices for ragged gather reduce.
- <a id="main_kernel.inner_kernel.row_loop.dma_write_loop"></a>`dma_write_loop(col_vmem_start, carry)` — [`L250`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py#L250)
- <a id="main_kernel.inner_kernel"></a>`inner_kernel()` — [`L147`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py#L147)
- <a id="main_kernel"></a>`main_kernel(num_rows_per_row_partition_ref: jax.Ref, in_hbm_ref: jax.Ref, indices_hbm_ref: jax.Ref, dst_indices_hbm_ref: jax.Ref, topk_weights_hbm_ref: jax.Ref, sorted_by_validity_hbm_ref: jax.Ref, out_hbm_ref: jax.Ref, num_rows_per_row_partition_vmem_ref: jax.Ref, out_vmem_ref: jax.Ref, prev_iter_last_row_vmem_ref: jax.Ref, src_indices_vmem_ref: jax.Ref, dst_indices_vmem_ref: jax.Ref, topk_weights_vmem_ref: jax.Ref, sorted_by_validity_vmem_ref: jax.Ref, sem_ref: jax.Ref, *, core_axis_name: str, subcore_axis_name: str, num_row_partitions: int, num_column_partitions: int)` — [`L103`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py#L103)
- <a id="ragged_gather_reduce"></a>`ragged_gather_reduce(x: jax.Array, indices: jax.Array, topk_weights: jax.Array, valid_rows_mask: jax.Array, reduce_group_size: int)` — [`L448`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py#L448) — Gathers `x` according to `indices`, applies weights and masks, and reduces. — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="main_kernel.inner_kernel.row_loop"></a>`row_loop(row_block_id)` — [`L176`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce.py#L176)

