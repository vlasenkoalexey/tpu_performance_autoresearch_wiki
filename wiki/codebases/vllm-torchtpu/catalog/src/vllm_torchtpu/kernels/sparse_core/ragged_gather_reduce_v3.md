---
title: 'Module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.sparse_core.ragged_gather_reduce_v3`/
symbols:
  _TOKEN_SUBCHUNK: _TOKEN_SUBCHUNK.
  ragged_gather_reduce: ragged_gather_reduce().
  _TOKEN_BLOCK: _TOKEN_BLOCK.
  _main_kernel.token_block_pipeline: _main_kernel().token_block_pipeline().
  _main_kernel.token_block_pipeline.route_pipeline: _main_kernel().token_block_pipeline().route_pipeline().
  _main_kernel: _main_kernel().
  token_block_alignment: token_block_alignment().
  _main_kernel.token_block_pipeline.zero_column: _main_kernel().token_block_pipeline().zero_column().
  _main_kernel.token_block_pipeline.route_indices_slice: _main_kernel().token_block_pipeline().route_indices_slice().
  _ROUTE_INDEX_BITS: _ROUTE_INDEX_BITS.
  _main_kernel.token_block_pipeline.route_pipeline.run_fixed_two_route_path: _main_kernel().token_block_pipeline().route_pipeline().run_fixed_two_route_path().
  _main_kernel.token_block_pipeline.route_pipeline.run_generic_path: _main_kernel().token_block_pipeline().route_pipeline().run_generic_path().
  _ROUTE_INDEX_MASK: _ROUTE_INDEX_MASK.
  partition_counts: partition_counts().
  _main_kernel.token_block_pipeline.route_pipeline.fixed_two_route_column_loop: _main_kernel().token_block_pipeline().route_pipeline().fixed_two_route_column_loop().
  _main_kernel.token_block_pipeline.route_pipeline.generic_column_loop: _main_kernel().token_block_pipeline().route_pipeline().generic_column_loop().
  _main_kernel.token_block_pipeline.cast_column: _main_kernel().token_block_pipeline().cast_column().
  _main_kernel.metadata_block_index: _main_kernel().metadata_block_index().
  _NUM_TOKEN_SUBCHUNKS: _NUM_TOKEN_SUBCHUNKS.
  _fallback_implementation: _fallback_implementation().
  _align_to: _align_to().
  _calculate_num_column_partitions: _calculate_num_column_partitions().
---
# Module: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py)

## Functions
- <a id="_align_to"></a>`_align_to(value: int, alignment: int)` — [`L40`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L40)
- <a id="_calculate_num_column_partitions"></a>`_calculate_num_column_partitions(hidden_size: int, num_cores: int, num_lanes: int)` — [`L57`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L57)
- <a id="_fallback_implementation"></a>`_fallback_implementation(x: jax.Array, indices: jax.Array, topk_weights: jax.Array, valid_rows_mask: jax.Array, reduce_group_size: int)` — [`L44`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L44)
- <a id="_main_kernel"></a>`_main_kernel(x_hbm_ref: jax.Ref, route_metadata_hbm_ref: jax.Ref, route_weights_hbm_ref: jax.Ref, route_counts_hbm_ref: jax.Ref, out_hbm_ref: jax.Ref, accum_vmem_ref: jax.Ref, out_tile_vmem_ref: jax.Ref, sem_ref: jax.Ref, *, core_axis_name: str, subcore_axis_name: str, num_row_partitions: int, num_column_partitions: int, blocks_per_row_partition: int, topk: int)` — [`L96`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L96) — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_main_kernel.token_block_pipeline.cast_column"></a>`cast_column(col_offset)` — [`L289`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L289)
- <a id="_main_kernel.token_block_pipeline.route_pipeline.fixed_two_route_column_loop"></a>`fixed_two_route_column_loop(col_offset)` — [`L191`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L191)
- <a id="_main_kernel.token_block_pipeline.route_pipeline.generic_column_loop"></a>`generic_column_loop(col_offset)` — [`L228`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L228)
- <a id="_main_kernel.metadata_block_index"></a>`metadata_block_index(block_id)` — [`L127`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L127)
- <a id="partition_counts"></a>`partition_counts(hidden_size: int, tpu_info)` — [`L81`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L81) — Column and row partition counts of the SparseCore subcores for a width. — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="ragged_gather_reduce"></a>`ragged_gather_reduce(x: jax.Array, indices: jax.Array, topk_weights: jax.Array, valid_rows_mask: jax.Array, reduce_group_size: int)` — [`L332`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L332) — Destination-major prototype for MoE output combine. — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_main_kernel.token_block_pipeline.route_indices_slice"></a>`route_indices_slice(route_chunk)` — [`L160`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L160)
- <a id="_main_kernel.token_block_pipeline.route_pipeline"></a>`route_pipeline(gather_ref)` — [`L180`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L180) — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_main_kernel.token_block_pipeline.route_pipeline.run_fixed_two_route_path"></a>`run_fixed_two_route_path()` — [`L268`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L268)
- <a id="_main_kernel.token_block_pipeline.route_pipeline.run_generic_path"></a>`run_generic_path()` — [`L274`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L274)
- <a id="token_block_alignment"></a>`token_block_alignment(hidden_size: int, tpu_info)` — [`L91`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L91) — Destination-token granularity: one 64-token block per row partition. — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_main_kernel.token_block_pipeline"></a>`token_block_pipeline(route_metadata_ref, route_weights_ref, route_counts_ref, output_sem_ref)` — [`L140`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L140) — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_main_kernel.token_block_pipeline.zero_column"></a>`zero_column(col_offset)` — [`L152`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L152)

## Module values
- <a id="_NUM_TOKEN_SUBCHUNKS"></a>`_NUM_TOKEN_SUBCHUNKS` — [`L34`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L34)
- <a id="_ROUTE_INDEX_BITS"></a>`_ROUTE_INDEX_BITS` — [`L36`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L36) — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_ROUTE_INDEX_MASK"></a>`_ROUTE_INDEX_MASK` — [`L37`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L37)
- <a id="_TOKEN_BLOCK"></a>`_TOKEN_BLOCK` — [`L35`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L35) — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- <a id="_TOKEN_SUBCHUNK"></a>`_TOKEN_SUBCHUNK` — [`L33`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v3.py#L33) — documented in [sparsecore-ragged-gather-scatter](../../../../../concepts/sparsecore-ragged-gather-scatter.md)

