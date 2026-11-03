---
title: 'Module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.kernels.sparse_core.ragged_gather_reduce_v2.memory_ref`/
symbols:
  KernelRefs.scratch: KernelRefs#scratch.
  KernelRefs.create: KernelRefs#create().
  ScratchRef.create_scratch_types: ScratchRef#create_scratch_types().
  KernelRefs.data: KernelRefs#data.
  KernelRefs: KernelRefs#
  KernelRefs.index: KernelRefs#index.
  IndexRef: IndexRef#
  ScratchRef: ScratchRef#
  ScratchRef.sorted_by_validity_vmem: ScratchRef#sorted_by_validity_vmem.
  DataRef.out: DataRef#out.
  ScratchRef.prev_dst_row_smem: ScratchRef#prev_dst_row_smem.
  ScratchRef.src_indices_vmem: ScratchRef#src_indices_vmem.
  ScratchRef.sem: ScratchRef#sem.
  IndexRef.num_src_rows_per_row_partition: IndexRef#num_src_rows_per_row_partition.
  IndexRef.indices: IndexRef#indices.
  IndexRef.sorted_by_validity: IndexRef#sorted_by_validity.
  DataRef: DataRef#
  DataRef.source: DataRef#source.
  DataRef.topk_weights: DataRef#topk_weights.
  ScratchRef.num_rows_per_row_partition_vmem: ScratchRef#num_rows_per_row_partition_vmem.
  ScratchRef.next_window_first_row_vmem: ScratchRef#next_window_first_row_vmem.
  ScratchRef.prev_iter_last_row_vmem: ScratchRef#prev_iter_last_row_vmem.
  ScratchRef.dst_indices_vmem: ScratchRef#dst_indices_vmem.
  ScratchRef.tw_f32_vmem: ScratchRef#tw_f32_vmem.
  ScratchRef.dma_src_row_vmem: ScratchRef#dma_src_row_vmem.
  ScratchRef.dma_dst_row_vmem: ScratchRef#dma_dst_row_vmem.
  ScratchRef.prev_dst_val_vmem: ScratchRef#prev_dst_val_vmem.
  ScratchRef.out_vmem: ScratchRef#out_vmem.
---
# Module: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py)

## Classes
### <a id="DataRef"></a>`DataRef`
- def: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py:34`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L34)
- signature: `class DataRef:`
- members:
  - <a id="DataRef.out"></a>`out` — [`L37`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L37)
  - <a id="DataRef.source"></a>`source` — [`L35`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L35)
  - <a id="DataRef.topk_weights"></a>`topk_weights` — [`L36`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L36)
- used by: [`_row_kernel`](kernel.md#_row_kernel), [`_window_kernel`](kernel.md#_window_kernel), [`_col_kernel`](kernel.md#_col_kernel), [`create`](memory_ref.md#KernelRefs.create), [`data`](memory_ref.md#KernelRefs.data)

### <a id="IndexRef"></a>`IndexRef`
- def: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py:26`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L26)
- signature: `class IndexRef:`
- members:
  - <a id="IndexRef.indices"></a>`indices` — [`L28`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L28)
  - <a id="IndexRef.num_src_rows_per_row_partition"></a>`num_src_rows_per_row_partition` — [`L27`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L27)
  - <a id="IndexRef.sorted_by_validity"></a>`sorted_by_validity` — [`L29`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L29)
- used by: [`_window_kernel`](kernel.md#_window_kernel), [`main_kernel`](wrapper.md#main_kernel), [`_preprocess_scalar_data`](wrapper.md#_preprocess_scalar_data), [`create`](memory_ref.md#KernelRefs.create), [`index`](memory_ref.md#KernelRefs.index)

### <a id="KernelRefs"></a>`KernelRefs`
- def: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py:83`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L83) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- signature: `class KernelRefs:`
- members:
  - <a id="KernelRefs.create"></a>`create(cls, scalar_ref: IndexRef, in_hbm_ref: Any, topk_weights_hbm_ref: Any, out_hbm_ref: Any, scratch_ref: ScratchRef)` — [`L89`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L89) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="KernelRefs.data"></a>`data` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L85) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="KernelRefs.index"></a>`index` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L84) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="KernelRefs.scratch"></a>`scratch` — [`L86`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L86) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
- uses (calls/refs, reference-scoped): [`IndexRef`](memory_ref.md#IndexRef), [`ScratchRef`](memory_ref.md#ScratchRef), [`out`](memory_ref.md#DataRef.out), [`DataRef`](memory_ref.md#DataRef), [`source`](memory_ref.md#DataRef.source), [`topk_weights`](memory_ref.md#DataRef.topk_weights)
- used by: [`_row_kernel`](kernel.md#_row_kernel), [`_window_kernel`](kernel.md#_window_kernel), [`_col_kernel`](kernel.md#_col_kernel), [`main_kernel`](wrapper.md#main_kernel), [`call_kernel_pipeline`](kernel.md#call_kernel_pipeline), [`col_loop`](kernel.md#_col_kernel.col_loop)

### <a id="ScratchRef"></a>`ScratchRef`
- def: [`src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py:42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L42)
- signature: `class ScratchRef:`
- members:
  - <a id="ScratchRef.create_scratch_types"></a>`create_scratch_types(cls, cfg: config.Config)` — [`L58`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L58) — documented in [sparsecore-ragged-gather-scatter](../../../../../../concepts/sparsecore-ragged-gather-scatter.md)
  - <a id="ScratchRef.dma_dst_row_vmem"></a>`dma_dst_row_vmem` — [`L52`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L52)
  - <a id="ScratchRef.dma_src_row_vmem"></a>`dma_src_row_vmem` — [`L51`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L51)
  - <a id="ScratchRef.dst_indices_vmem"></a>`dst_indices_vmem` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L49)
  - <a id="ScratchRef.next_window_first_row_vmem"></a>`next_window_first_row_vmem` — [`L44`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L44)
  - <a id="ScratchRef.num_rows_per_row_partition_vmem"></a>`num_rows_per_row_partition_vmem` — [`L43`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L43)
  - <a id="ScratchRef.out_vmem"></a>`out_vmem` — [`L54`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L54)
  - <a id="ScratchRef.prev_dst_row_smem"></a>`prev_dst_row_smem` — [`L46`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L46)
  - <a id="ScratchRef.prev_dst_val_vmem"></a>`prev_dst_val_vmem` — [`L53`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L53)
  - <a id="ScratchRef.prev_iter_last_row_vmem"></a>`prev_iter_last_row_vmem` — [`L45`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L45)
  - <a id="ScratchRef.sem"></a>`sem` — [`L55`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L55)
  - <a id="ScratchRef.sorted_by_validity_vmem"></a>`sorted_by_validity_vmem` — [`L47`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L47)
  - <a id="ScratchRef.src_indices_vmem"></a>`src_indices_vmem` — [`L48`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L48)
  - <a id="ScratchRef.tw_f32_vmem"></a>`tw_f32_vmem` — [`L50`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/kernels/sparse_core/ragged_gather_reduce_v2/memory_ref.py#L50)
- uses (calls/refs, reference-scoped): [`col_chunk_size`](config.md#Config.col_chunk_size), [`sc_info`](config.md#Config.sc_info), [`row_chunk_size`](config.md#Config.row_chunk_size), [`col_size`](config.md#Config.col_size), [`Config`](config.md#Config), [`window_size`](config.md#Config.window_size)
- used by: [`_row_kernel`](kernel.md#_row_kernel), [`ragged_gather_reduce_v2`](wrapper.md#ragged_gather_reduce_v2), [`_window_kernel`](kernel.md#_window_kernel), [`_col_kernel`](kernel.md#_col_kernel), [`main_kernel`](wrapper.md#main_kernel), [`scratch`](memory_ref.md#KernelRefs.scratch), [`call_kernel_pipeline`](kernel.md#call_kernel_pipeline), [`create`](memory_ref.md#KernelRefs.create), [`col_loop`](kernel.md#_col_kernel.col_loop)

