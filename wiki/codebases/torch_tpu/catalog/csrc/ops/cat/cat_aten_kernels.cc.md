---
title: 'Module: csrc/ops/cat/cat_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/cat/cat_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenStackOut: AtenStackOut(dc412c106b639e73).
  AtenCatOut: AtenCatOut(21bdf3526693636c).
  PrepareStackDispatch: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/PrepareStackDispatch(9ea43fc5d5b54cf9).'
  AtenStack: AtenStack(981a90b1490c2b91).
  CatHelper: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/CatHelper(478c939b9d4ce7c5).'
  ValidateCatTensors: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/ValidateCatTensors(6eeb2d2b7e80c57).'
  MakeStackOpBuilder: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/MakeStackOpBuilder(f51265b03381d9d2).'
  StackDispatchParams.output_dims: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/StackDispatchParams#output_dims.'
  CatComputationResult: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/CatComputationResult#'
  CatShapeInfo.output_dims: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/CatShapeInfo#output_dims.'
  StackDispatchParams.output_dtype: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/StackDispatchParams#output_dtype.'
  StackDispatchParams.wrapped_dim: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/StackDispatchParams#wrapped_dim.'
  StackDispatchParams: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/StackDispatchParams#'
  CatComputationResult.result_buf: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/CatComputationResult#result_buf.'
  CatShapeInfo.wrapped_dim: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/CatShapeInfo#wrapped_dim.'
  CatShapeInfo: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/CatShapeInfo#'
  CatComputationResult.num_dims: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/CatComputationResult#num_dims.'
  CatShapeInfo.num_dims: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/CatShapeInfo#num_dims.'
  CatComputationResult.output_dims: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/CatComputationResult#output_dims.'
  CatComputationResult.promoted_dtype: '`$anonymous_namespace_csrc/ops/cat/cat_aten_kernels.cc`/CatComputationResult#promoted_dtype.'
---
# Module: [`csrc/ops/cat/cat_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc)

## Classes
### <a id="CatComputationResult"></a>`CatComputationResult`
- def: [`csrc/ops/cat/cat_aten_kernels.cc:59`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L59)
- signature: `struct CatComputationResult`
- members:
  - <a id="CatComputationResult.num_dims"></a>`num_dims` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L62)
  - <a id="CatComputationResult.output_dims"></a>`output_dims` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L63)
  - <a id="CatComputationResult.promoted_dtype"></a>`promoted_dtype` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L61)
  - <a id="CatComputationResult.result_buf"></a>`result_buf` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L60)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`DeviceBufferRef`](../../eager/device_buffer.h.md#DeviceBufferRef)
- used by: [`AtenCatOut`](cat_aten_kernels.cc.md#AtenCatOut), [`CatHelper`](cat_aten_kernels.cc.md#CatHelper), [`MakeStackOpBuilder`](cat_aten_kernels.cc.md#MakeStackOpBuilder)

### <a id="CatShapeInfo"></a>`CatShapeInfo`
- def: [`csrc/ops/cat/cat_aten_kernels.cc:66`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L66)
- signature: `struct CatShapeInfo`
- members:
  - <a id="CatShapeInfo.num_dims"></a>`num_dims` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L67)
  - <a id="CatShapeInfo.output_dims"></a>`output_dims` — [`L69`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L69)
  - <a id="CatShapeInfo.wrapped_dim"></a>`wrapped_dim` — [`L68`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L68)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`CatHelper`](cat_aten_kernels.cc.md#CatHelper), [`ValidateCatTensors`](cat_aten_kernels.cc.md#ValidateCatTensors)

### <a id="StackDispatchParams"></a>`StackDispatchParams`
- def: [`csrc/ops/cat/cat_aten_kernels.cc:125`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L125)
- signature: `struct StackDispatchParams`
- members:
  - <a id="StackDispatchParams.output_dims"></a>`output_dims` — [`L128`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L128)
  - <a id="StackDispatchParams.output_dtype"></a>`output_dtype` — [`L127`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L127)
  - <a id="StackDispatchParams.wrapped_dim"></a>`wrapped_dim` — [`L126`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L126)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`AtenStackOut`](cat_aten_kernels.cc.md#AtenStackOut), [`PrepareStackDispatch`](cat_aten_kernels.cc.md#PrepareStackDispatch), [`AtenStack`](cat_aten_kernels.cc.md#AtenStack)

## Functions
- <a id="AtenCatOut"></a>`AtenCatOut(const at::ITensorListRef& tensors, int64_t dim, at::Tensor& out)` — [`L256`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L256)
- <a id="AtenStack"></a>`AtenStack(at::TensorList tensors, int64_t dim)` — [`L271`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L271)
- <a id="AtenStackOut"></a>`AtenStackOut(at::TensorList tensors, int64_t dim, at::Tensor& out)` — [`L287`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L287)
- <a id="CatHelper"></a>`CatHelper(const at::ITensorListRef& tensors, const int64_t dim, OpParamCacheKeys param_keys, std::optional<at::ScalarType> output_dtype_override = std::nullopt)` — [`L178`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L178)
- <a id="MakeStackOpBuilder"></a>`MakeStackOpBuilder(const int64_t wrapped_dim)` — [`L171`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L171)
- <a id="PrepareStackDispatch"></a>`PrepareStackDispatch(at::TensorList tensors, const int64_t dim, const at::Tensor* out = nullptr)` — [`L131`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L131)
- <a id="ValidateCatTensors"></a>`ValidateCatTensors(const at::ITensorListRef& tensors, const int64_t dim)` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/cat/cat_aten_kernels.cc#L72)

