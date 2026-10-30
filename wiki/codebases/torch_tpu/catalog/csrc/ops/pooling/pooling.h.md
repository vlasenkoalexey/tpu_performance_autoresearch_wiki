---
title: 'Module: csrc/ops/pooling/pooling.h'
type: catalog
provenance: extracted
module: csrc/ops/pooling/pooling.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  PaddingParams.right: PaddingParams#right.
  ReduceWindowAttributes.padding: ReduceWindowAttributes#padding.
  BatchInput.batch_input: BatchInput#batch_input.
  ReduceWindowAttributes: ReduceWindowAttributes#
  ReduceWindowAttributes.window_dimensions: ReduceWindowAttributes#window_dimensions.
  BatchInput.original_dim_size: BatchInput#original_dim_size.
  ReduceWindowAttributes.window_strides: ReduceWindowAttributes#window_strides.
  BatchInput: BatchInput#
  ReduceWindowAttributes.window_dilations: ReduceWindowAttributes#window_dilations.
  ReduceWindowAttributes.base_dilations: ReduceWindowAttributes#base_dilations.
  PaddingParams: PaddingParams#
  PaddingParams.left: PaddingParams#left.
---
# Module: [`csrc/ops/pooling/pooling.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h)

## Classes
### <a id="BatchInput"></a>`BatchInput`
- def: [`csrc/ops/pooling/pooling.h:34`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h#L34)
- signature: `struct BatchInput`
- members:
  - <a id="BatchInput.batch_input"></a>`batch_input` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h#L35)
  - <a id="BatchInput.original_dim_size"></a>`original_dim_size` — [`L36`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h#L36)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`CreateBatchInput`](pooling.cc.md#CreateBatchInput), [`ComputeMaxPoolWithIndices`](max_pool_aten_kernels.cc.md#ComputeMaxPoolWithIndices), [`BuildAdaptiveMaxPool2dShlo`](adaptive_max_pool_aten_kernels.cc.md#BuildAdaptiveMaxPool2dShlo), [`BuildMaxPoolBackwardShlo`](max_pool_aten_kernels.cc.md#BuildMaxPoolBackwardShlo), [`BuildMaxPoolShlo`](max_pool_aten_kernels.cc.md#BuildMaxPoolShlo), [`BuildMaxPoolWithIndicesShlo`](max_pool_aten_kernels.cc.md#BuildMaxPoolWithIndicesShlo), [`BuildAvgPoolShlo`](avg_pool_aten_kernels.cc.md#BuildAvgPoolShlo), [`BuildAvgPoolBackwardShlo`](avg_pool_aten_kernels.cc.md#BuildAvgPoolBackwardShlo), [`BuildMaxPoolWithIndicesBackwardShlo`](max_pool_aten_kernels.cc.md#BuildMaxPoolWithIndicesBackwardShlo), [`BuildAdaptiveAvgPool2dBackwardShlo`](adaptive_avg_pool_aten_kernels.cc.md#BuildAdaptiveAvgPool2dBackwardShlo), [`BuildAdaptiveAvgPool2dShlo`](adaptive_avg_pool_aten_kernels.cc.md#BuildAdaptiveAvgPool2dShlo), [`BuildAdaptiveAvgPool3dBackwardShlo`](adaptive_avg_pool_aten_kernels.cc.md#BuildAdaptiveAvgPool3dBackwardShlo), [`BuildAdaptiveAvgPool3dShlo`](adaptive_avg_pool_aten_kernels.cc.md#BuildAdaptiveAvgPool3dShlo), [`ComputeMaxPool`](max_pool_aten_kernels.cc.md#ComputeMaxPool), [`padding`](pooling.h.md#ReduceWindowAttributes.padding)

### <a id="PaddingParams"></a>`PaddingParams`
- def: [`csrc/ops/pooling/pooling.h:62`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h#L62)
- doc: Defines the asymmetric padding (start and end) applied to a single spatial
- signature: `struct PaddingParams`
- members:
  - <a id="PaddingParams.left"></a>`left` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h#L65) — The amount of padding added to the start (left, top, front) of the
  - <a id="PaddingParams.right"></a>`right` — [`L68`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h#L68) — The amount of padding added to the end (right, bottom, back) of the
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`GetPoolingOutputSize`](pooling.cc.md#GetPoolingOutputSize), [`GetReduceWindowAttributes`](pooling.cc.md#GetReduceWindowAttributes), [`ReduceWindowAttributes`](pooling.h.md#ReduceWindowAttributes), [`CeilModePadding`](pooling.cc.md#CeilModePadding), [`CeilModePadding`](pooling.cc.md#CeilModePadding), [`GetReduceWindowAttributes`](pooling.cc.md#GetReduceWindowAttributes)
- used by: [`RemoveTrivialBatch`](pooling.cc.md#RemoveTrivialBatch), [`GetReduceWindowAttributes`](pooling.cc.md#GetReduceWindowAttributes), [`SliceBackwardResult`](avg_pool_aten_kernels.cc.md#SliceBackwardResult), [`CeilModePadding`](pooling.cc.md#CeilModePadding)

### <a id="ReduceWindowAttributes"></a>`ReduceWindowAttributes`
- def: [`csrc/ops/pooling/pooling.h:39`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h#L39)
- signature: `struct ReduceWindowAttributes`
- members:
  - <a id="ReduceWindowAttributes.base_dilations"></a>`base_dilations` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h#L42)
  - <a id="ReduceWindowAttributes.padding"></a>`padding` — [`L44`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h#L44)
  - <a id="ReduceWindowAttributes.window_dilations"></a>`window_dilations` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h#L43)
  - <a id="ReduceWindowAttributes.window_dimensions"></a>`window_dimensions` — [`L40`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h#L40)
  - <a id="ReduceWindowAttributes.window_strides"></a>`window_strides` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/pooling.h#L41)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`CreateBatchInput`](pooling.cc.md#CreateBatchInput), [`ExpandAttribute`](pooling.cc.md#ExpandAttribute), [`RemoveTrivialBatch`](pooling.cc.md#RemoveTrivialBatch), [`BatchInput`](pooling.h.md#BatchInput)
- used by: [`ComputeMaxPoolWithIndices`](max_pool_aten_kernels.cc.md#ComputeMaxPoolWithIndices), [`ScaleAvgPoolOutput`](avg_pool_aten_kernels.cc.md#ScaleAvgPoolOutput), [`BuildAdaptiveMaxPool2dShlo`](adaptive_max_pool_aten_kernels.cc.md#BuildAdaptiveMaxPool2dShlo), [`BuildMaxPoolBackwardShlo`](max_pool_aten_kernels.cc.md#BuildMaxPoolBackwardShlo), [`BuildMaxPoolShlo`](max_pool_aten_kernels.cc.md#BuildMaxPoolShlo), [`BuildMaxPoolWithIndicesShlo`](max_pool_aten_kernels.cc.md#BuildMaxPoolWithIndicesShlo), [`BuildAvgPoolShlo`](avg_pool_aten_kernels.cc.md#BuildAvgPoolShlo), [`BuildAvgPoolBackwardShlo`](avg_pool_aten_kernels.cc.md#BuildAvgPoolBackwardShlo), [`ComputeMaxPool`](max_pool_aten_kernels.cc.md#ComputeMaxPool), [`right`](pooling.h.md#PaddingParams.right), [`GetReduceWindowAttributes`](pooling.cc.md#GetReduceWindowAttributes), [`CeilModePadding`](pooling.cc.md#CeilModePadding)

