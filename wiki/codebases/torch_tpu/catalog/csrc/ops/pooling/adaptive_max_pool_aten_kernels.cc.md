---
title: 'Module: csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenAdaptiveMaxPool2dOut: AtenAdaptiveMaxPool2dOut(49752c64a162150d).
  AdaptiveMaxPool2dHelper: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/AdaptiveMaxPool2dHelper(a441397736116704).'
  BuildAdaptiveMaxPool2dShlo: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/BuildAdaptiveMaxPool2dShlo(c566fcd9ac4f0358).'
  CheckAdaptiveMaxPoolDtypes: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/CheckAdaptiveMaxPoolDtypes(45982de3b0bc1087).'
  BuildGatherMaxPool1D: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/BuildGatherMaxPool1D(cffcd5950db144c4).'
  CreateI64Const: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/CreateI64Const(977ed35fcd2e8f7).'
  ComputeAdaptiveIndices: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/ComputeAdaptiveIndices(8f3e0dfbfca22ff8).'
  AdaptiveIntervals.max_k: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/AdaptiveIntervals#max_k.'
  AdaptiveMaxPoolBuffers: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/AdaptiveMaxPoolBuffers#'
  AdaptiveIntervals: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/AdaptiveIntervals#'
  GatherMaxPool1DResult: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/GatherMaxPool1DResult#'
  AdaptiveIntervals.starts: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/AdaptiveIntervals#starts.'
  GatherMaxPool1DResult.values: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/GatherMaxPool1DResult#values.'
  AdaptiveMaxPoolBuffers.values: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/AdaptiveMaxPoolBuffers#values.'
  AdaptiveIntervals.lengths: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/AdaptiveIntervals#lengths.'
  AdaptiveMaxPoolBuffers.indices: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/AdaptiveMaxPoolBuffers#indices.'
  GatherMaxPool1DResult.indices: '`$anonymous_namespace_csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`/GatherMaxPool1DResult#indices.'
---
# Module: [`csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc)

## Classes
### <a id="AdaptiveIntervals"></a>`AdaptiveIntervals`
- def: [`csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc:73`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L73)
- signature: `struct AdaptiveIntervals`
- members:
  - <a id="AdaptiveIntervals.lengths"></a>`lengths` — [`L75`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L75)
  - <a id="AdaptiveIntervals.max_k"></a>`max_k` — [`L76`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L76)
  - <a id="AdaptiveIntervals.starts"></a>`starts` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L74)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`BuildGatherMaxPool1D`](adaptive_max_pool_aten_kernels.cc.md#BuildGatherMaxPool1D), [`ComputeAdaptiveIndices`](adaptive_max_pool_aten_kernels.cc.md#ComputeAdaptiveIndices)

### <a id="AdaptiveMaxPoolBuffers"></a>`AdaptiveMaxPoolBuffers`
- def: [`csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc:68`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L68)
- signature: `struct AdaptiveMaxPoolBuffers`
- members:
  - <a id="AdaptiveMaxPoolBuffers.indices"></a>`indices` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L70)
  - <a id="AdaptiveMaxPoolBuffers.values"></a>`values` — [`L69`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L69)
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](../../eager/device_buffer.h.md#DeviceBufferRef)
- used by: [`AdaptiveMaxPool2dHelper`](adaptive_max_pool_aten_kernels.cc.md#AdaptiveMaxPool2dHelper), [`CheckAdaptiveMaxPoolDtypes`](adaptive_max_pool_aten_kernels.cc.md#CheckAdaptiveMaxPoolDtypes)

### <a id="GatherMaxPool1DResult"></a>`GatherMaxPool1DResult`
- def: [`csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc:63`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L63)
- signature: `struct GatherMaxPool1DResult`
- members:
  - <a id="GatherMaxPool1DResult.indices"></a>`indices` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L65)
  - <a id="GatherMaxPool1DResult.values"></a>`values` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L64)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildGatherMaxPool1D`](adaptive_max_pool_aten_kernels.cc.md#BuildGatherMaxPool1D), [`CreateI64Const`](adaptive_max_pool_aten_kernels.cc.md#CreateI64Const)

## Functions
- <a id="AdaptiveMaxPool2dHelper"></a>`AdaptiveMaxPool2dHelper(const at::Tensor& self, at::IntArrayRef output_size, OpParamCacheKeys param_keys)` — [`L396`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L396)
- <a id="AtenAdaptiveMaxPool2dOut"></a>`AtenAdaptiveMaxPool2dOut(const at::Tensor& self, at::IntArrayRef output_size, at::Tensor& out, at::Tensor& indices)` — [`L459`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L459)
- `BuildAdaptiveMaxPool2dShlo(mlir::MlirOp input_op, const int64_t in_h, const int64_t in_w, const int64_t out_h, const int64_t out_w, const int64_t spatial_dim_count)` — [`L241`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L241)
- <a id="BuildAdaptiveMaxPool2dShlo"></a>`BuildAdaptiveMaxPool2dShlo(mlir::MlirOp input_op, const int64_t in_h, const int64_t in_w, const int64_t out_h, const int64_t out_w, const int64_t spatial_dim_count)` — [`L241`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L241)
- <a id="BuildGatherMaxPool1D"></a>`BuildGatherMaxPool1D(mlir::MlirBuilder& builder, mlir::MlirOp input_val, mlir::MlirOp input_idx, const int64_t dim, const int64_t in_size, const int64_t out_size)` — [`L115`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L115) — Builds a 1D gather pooling operation for a given dimension using the
- <a id="CheckAdaptiveMaxPoolDtypes"></a>`CheckAdaptiveMaxPoolDtypes(const at::Tensor& self)` — [`L379`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L379)
- <a id="ComputeAdaptiveIndices"></a>`ComputeAdaptiveIndices(const int64_t in_size, const int64_t out_size)` — [`L81`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L81) — Computes the start and length of each interval along a given dimension based
- <a id="CreateI64Const"></a>`CreateI64Const(mlir::MlirBuilder& builder, const Dimensions& data)` — [`L104`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/adaptive_max_pool_aten_kernels.cc#L104) — Helper: Create a 1D [N] int64 constant tensor.

