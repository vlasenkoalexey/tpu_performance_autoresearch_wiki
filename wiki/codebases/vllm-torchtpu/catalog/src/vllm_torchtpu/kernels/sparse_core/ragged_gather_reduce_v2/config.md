---
title: 'Module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.sparse_core.ragged_gather_reduce_v2.config`/
symbols:
  Config.num_column_partitions: Config#num_column_partitions().
  Config.col_chunk_size: Config#col_chunk_size().
  Config.sc_info: Config#sc_info().
  Config.row_chunk_size: Config#row_chunk_size().
  Config.max_window: Config#max_window().
  Config.num_row_partitions: Config#num_row_partitions().
  Config.num_row_subchunks: Config#num_row_subchunks().
  Config.padded_input_size: Config#padded_input_size().
  Config.aligned_hidden_size: Config#aligned_hidden_size().
  Config.should_fallback: Config#should_fallback().
  Config.col_size: Config#col_size().
  Config: Config#
  Config.row_partition_size_padded: Config#row_partition_size_padded().
  Config.row_partition_size: Config#row_partition_size().
  Config.window_size: Config#window_size().
  Config.tpu_info: Config#tpu_info.
  Config.get_num_row_subchunks: Config#get_num_row_subchunks().
  Config.get_row_chunk_size: Config#get_row_chunk_size().
  Config.output_size: Config#output_size().
  Config.num_tot_cores: Config#num_tot_cores().
  Config.input_size: Config#input_size.
  Config.hidden_size: Config#hidden_size.
  Config.reduce_group_size: Config#reduce_group_size.
  Config.max_blocks_per_partition: Config#max_blocks_per_partition().
  Config.num_col_chunks: Config#num_col_chunks().
  Config.in_dtype: Config#in_dtype.
  Config.in_dtype_bytes: Config#in_dtype_bytes().
  Config.row_shift: Config#row_shift().
  _align_to: _align_to().
  Config.core_axis_name: Config#core_axis_name.
  Config.subcore_axis_name: Config#subcore_axis_name.
  Config.__post_init__: Config#__post_init__().
  _CostModelConstants: _CostModelConstants#
  Config.source_rows: Config#source_rows.
  _CostModelConstants.MAX_ITERATIONS: _CostModelConstants#MAX_ITERATIONS.
  _CostModelConstants.MAX_COL_CHUNK_SIZE: _CostModelConstants#MAX_COL_CHUNK_SIZE.
---
# Module: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py)

## Classes
### <a id="Config"></a>`Config`
- def: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py:43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L43) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- signature: `class Config:`
- members:
  - <a id="Config.aligned_hidden_size"></a>`aligned_hidden_size(self)` — [`L214`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L214) — Calculates the aligned hidden size. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.col_chunk_size"></a>`col_chunk_size(self)` — [`L225`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L225) — Picks the column chunk size the inner pipeline gathers at a time. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.col_size"></a>`col_size(self)` — [`L220`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L220) — Calculates the column size. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.get_num_row_subchunks"></a>`get_num_row_subchunks(self, num_row_partitions: int)` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L67) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.get_row_chunk_size"></a>`get_row_chunk_size(self, num_row_partitions: int)` — [`L72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L72) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.in_dtype_bytes"></a>`in_dtype_bytes(self)` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L84)
  - <a id="Config.max_blocks_per_partition"></a>`max_blocks_per_partition(self)` — [`L113`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L113) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.max_window"></a>`max_window(self)` — [`L117`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L117) — Largest window of row-blocks whose resident sort permutation fits SPMEM. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.num_col_chunks"></a>`num_col_chunks(self)` — [`L151`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L151) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.num_column_partitions"></a>`num_column_partitions(self)` — [`L175`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L175) — Calculates the number of row partitions. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.num_row_partitions"></a>`num_row_partitions(self)` — [`L165`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L165) — Calculates the number of row partitions. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.num_row_subchunks"></a>`num_row_subchunks(self)` — [`L76`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L76) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.num_tot_cores"></a>`num_tot_cores(self)` — [`L64`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L64)
  - <a id="Config.output_size"></a>`output_size(self)` — [`L80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L80) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.padded_input_size"></a>`padded_input_size(self)` — [`L88`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L88) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.row_chunk_size"></a>`row_chunk_size(self)` — [`L146`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L146) — Number of rows handled per row-pipeline block. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.row_partition_size"></a>`row_partition_size(self)` — [`L104`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L104) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.row_partition_size_padded"></a>`row_partition_size_padded(self)` — [`L108`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L108) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.row_shift"></a>`row_shift(self)` — [`L155`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L155) — log2 of how many source rows pack into one uint32 gather element.
  - <a id="Config.sc_info"></a>`sc_info(self)` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L58) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.should_fallback"></a>`should_fallback(self)` — [`L93`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L93) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.window_size"></a>`window_size(self)` — [`L141`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L141) — Number of rows whose sort permutation is resident per window. — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.core_axis_name"></a>`core_axis_name` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L49)
  - <a id="Config.hidden_size"></a>`hidden_size` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L45) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.in_dtype"></a>`in_dtype` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L48) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.input_size"></a>`input_size` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L44) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.reduce_group_size"></a>`reduce_group_size` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L47) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="Config.source_rows"></a>`source_rows` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L46)
  - <a id="Config.subcore_axis_name"></a>`subcore_axis_name` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L50)
  - <a id="Config.tpu_info"></a>`tpu_info` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L51) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- protocol/private: <a id="Config.__post_init__"></a>`__post_init__`[`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L53)
- uses (calls/refs, reference-scoped): [`_align_to`](config.md#_align_to), [`_CostModelConstants`](config.md#_CostModelConstants), [`MAX_COL_CHUNK_SIZE`](config.md#_CostModelConstants.MAX_COL_CHUNK_SIZE), [`MAX_ITERATIONS`](config.md#_CostModelConstants.MAX_ITERATIONS)
- used by: [`_row_kernel`](kernel.md#_row_kernel), [`ragged_gather_reduce_v2`](wrapper.md#ragged_gather_reduce_v2), [`_window_kernel`](kernel.md#_window_kernel), [`_col_kernel`](kernel.md#_col_kernel), [`main_kernel`](wrapper.md#main_kernel), [`_preprocess_scalar_data`](wrapper.md#_preprocess_scalar_data), [`call_kernel_pipeline`](kernel.md#call_kernel_pipeline), [`create_scratch_types`](memory_ref.md#ScratchRef.create_scratch_types), [`col_loop`](kernel.md#_col_kernel.col_loop), [`_col_gather_spec`](kernel.md#_col_gather_spec), [`_row_gather_specs`](kernel.md#_row_gather_specs), [`col_index_map`](kernel.md#_col_gather_spec.col_index_map), [`row_index_map`](kernel.md#_row_gather_specs.row_index_map)

### <a id="_CostModelConstants"></a>`_CostModelConstants`
- def: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py:28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L28)
- signature: `class _CostModelConstants:`
- members:
  - <a id="_CostModelConstants.MAX_COL_CHUNK_SIZE"></a>`MAX_COL_CHUNK_SIZE` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L39)
  - <a id="_CostModelConstants.MAX_ITERATIONS"></a>`MAX_ITERATIONS` — [`L33`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L33)
- used by: [`num_column_partitions`](config.md#Config.num_column_partitions), [`col_chunk_size`](config.md#Config.col_chunk_size)

## Functions
- <a id="_align_to"></a>`_align_to(a, b)` — [`L24`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/config.py#L24)

