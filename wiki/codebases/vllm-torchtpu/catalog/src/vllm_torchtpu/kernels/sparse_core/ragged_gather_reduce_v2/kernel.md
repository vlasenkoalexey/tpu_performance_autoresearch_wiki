---
title: 'Module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.sparse_core.ragged_gather_reduce_v2.kernel`/
symbols:
  _row_kernel: _row_kernel().
  _window_kernel: _window_kernel().
  _col_kernel: _col_kernel().
  call_kernel_pipeline: call_kernel_pipeline().
  _col_kernel.col_loop: _col_kernel().col_loop().
  _row_gather_specs: _row_gather_specs().
  _col_gather_spec: _col_gather_spec().
  _col_gather_spec.col_index_map: _col_gather_spec().col_index_map().
  _row_gather_specs.row_index_map: _row_gather_specs().row_index_map().
  _pack_scalars_to_vector: _pack_scalars_to_vector().
---
# Module: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py)

## Functions
- <a id="_col_gather_spec"></a>`_col_gather_spec(src_indices_vmem: jax.Ref, col_start: jax.Array, cfg: config.Config)` — [`L161`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py#L161) — Indirect BlockSpec gathering columns of a 2-D input. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_col_kernel"></a>`_col_kernel(gather_ref: jax.Ref, *, refs: memory_ref.KernelRefs, col_start: jax.Array, cfg: config.Config)` — [`L337`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py#L337) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_pack_scalars_to_vector"></a>`_pack_scalars_to_vector(scalar_list: list[jax.Array])` — [`L130`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py#L130) — Pack list of scalar values into a single VMEM lane.
- <a id="_row_gather_specs"></a>`_row_gather_specs(sorted_by_validity_vmem: jax.Ref, cfg: config.Config)` — [`L140`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py#L140) — Indirect BlockSpec gathering rows of a 1-D input. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_row_kernel"></a>`_row_kernel(src_indices_refs: tuple[jax.Ref, ...], topk_weights_refs: tuple[jax.Ref, ...], *, refs: memory_ref.KernelRefs, num_rows_current_row_partition: jax.Array, col_start: jax.Array, window_block_base: jax.Array, blocks_in_window: jax.Array, cfg: config.Config)` — [`L185`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py#L185) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_window_kernel"></a>`_window_kernel(window_id: jax.Array, *, refs: memory_ref.KernelRefs, row_partition_id: jax.Array, num_row_blocks: jax.Array, num_rows_current_row_partition: jax.Array, col_start: jax.Array, cfg: config.Config)` — [`L62`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py#L62) — Stages one window of the sort permutation, then runs its row blocks. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="call_kernel_pipeline"></a>`call_kernel_pipeline(row_partition_id: jax.Array, refs: memory_ref.KernelRefs, col_start: jax.Array, cfg: config.Config)` — [`L25`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py#L25) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_col_gather_spec.col_index_map"></a>`col_index_map(s: int | jax.Array, c: int | jax.Array)` — [`L169`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py#L169) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_col_kernel.col_loop"></a>`col_loop(col_compute_offset: jax.Array)` — [`L357`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py#L357) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_row_gather_specs.row_index_map"></a>`row_index_map(r: int | jax.Array, *, offset: int)` — [`L146`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/kernel.py#L146)

