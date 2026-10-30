---
title: 'Module: csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenNativeBatchNorm: AtenNativeBatchNorm(12472df899712702).
  AtenNativeBatchNormLegitOut: AtenNativeBatchNormLegitOut(1b8baf62f18ef746).
  AtenNativeBatchNormLegitNoStatsOut: AtenNativeBatchNormLegitNoStatsOut(4eb712e12a1b25b2).
  AtenNativeBatchNormOut: AtenNativeBatchNormOut(7f137331c074a3e9).
  AtenNativeBatchNormBackward: AtenNativeBatchNormBackward(37e8c5eee4af20b2).
  AtenNativeBatchNormLegitNoStats: AtenNativeBatchNormLegitNoStats(de913c033c0c3673).
  AtenNativeBatchNormLegit: AtenNativeBatchNormLegit(d686d88987a4b405).
  TpuBatchNormBackward: '`$anonymous_namespace_csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`/TpuBatchNormBackward(99d88c77a291267e).'
  PrepareBatchNormDispatch: '`$anonymous_namespace_csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`/PrepareBatchNormDispatch(887f6646e17ff520).'
  ValidateIsFloating: '`$anonymous_namespace_csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`/ValidateIsFloating(d8359b99282c084c).'
  TpuBatchNormOut: '`$anonymous_namespace_csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`/TpuBatchNormOut(11e5d139d6e7cbeb).'
  TpuBatchNorm: '`$anonymous_namespace_csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`/TpuBatchNorm(cc4c209d70b78ac5).'
  GetOptionalMlirOp: '`$anonymous_namespace_csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`/GetOptionalMlirOp(d7e36d22c562da43).'
  BatchNormDispatchParams.output_dims: '`$anonymous_namespace_csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`/BatchNormDispatchParams#output_dims.'
  BatchNormDispatchParams.op_builder: '`$anonymous_namespace_csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`/BatchNormDispatchParams#op_builder.'
  BatchNormDispatchParams: '`$anonymous_namespace_csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`/BatchNormDispatchParams#'
  BatchNormDispatchParams.output_dtypes: '`$anonymous_namespace_csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`/BatchNormDispatchParams#output_dtypes.'
  BatchNormDispatchParams.inputs: '`$anonymous_namespace_csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`/BatchNormDispatchParams#inputs.'
---
# Module: [`csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc)

## Classes
### <a id="BatchNormDispatchParams"></a>`BatchNormDispatchParams`
- def: [`csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc:71`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L71)
- signature: `struct BatchNormDispatchParams`
- members:
  - <a id="BatchNormDispatchParams.inputs"></a>`inputs` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L72)
  - <a id="BatchNormDispatchParams.op_builder"></a>`op_builder` — [`L75`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L75)
  - <a id="BatchNormDispatchParams.output_dims"></a>`output_dims` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L74)
  - <a id="BatchNormDispatchParams.output_dtypes"></a>`output_dtypes` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L73)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`kDynamicSize`](../op_builder_utils.h.md#kDynamicSize), [`NAryMlirOpBuilder`](../op_builder_utils.h.md#NAryMlirOpBuilder)
- used by: [`PrepareBatchNormDispatch`](native_batch_norm_aten_kernels.cc.md#PrepareBatchNormDispatch), [`TpuBatchNormOut`](native_batch_norm_aten_kernels.cc.md#TpuBatchNormOut), [`TpuBatchNorm`](native_batch_norm_aten_kernels.cc.md#TpuBatchNorm)

## Functions
- <a id="AtenNativeBatchNorm"></a>`AtenNativeBatchNorm(const at::Tensor& input, const std::optional<at::Tensor>& weight, const std::optional<at::Tensor>& bias, const std::optional<at::Tensor>& running_mean, const std::optional<at::Tensor>& running_variance, bool training, double momentum, double eps)` — [`L305`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L305)
- <a id="AtenNativeBatchNormBackward"></a>`AtenNativeBatchNormBackward(const at::Tensor& grad_out, const at::Tensor& input, const std::optional<at::Tensor>& weight, const std::optional<at::Tensor>& running_mean, const std::optional<at::Tensor>& running_variance, const std::optional<at::Tensor>& save_mean, const std::optional<at::Tensor>& save_invstd, bool training, double eps, std::array<bool, 3> output_mask)` — [`L428`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L428)
- <a id="AtenNativeBatchNormLegit"></a>`AtenNativeBatchNormLegit(const at::Tensor& input, const std::optional<at::Tensor>& weight, const std::optional<at::Tensor>& bias, at::Tensor& running_mean, at::Tensor& running_variance, bool training, double momentum, double eps)` — [`L350`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L350)
- <a id="AtenNativeBatchNormLegitNoStats"></a>`AtenNativeBatchNormLegitNoStats(const at::Tensor& input, const std::optional<at::Tensor>& weight, const std::optional<at::Tensor>& bias, bool training, double momentum, double eps)` — [`L368`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L368)
- <a id="AtenNativeBatchNormLegitNoStatsOut"></a>`AtenNativeBatchNormLegitNoStatsOut(const at::Tensor& input, const std::optional<at::Tensor>& weight, const std::optional<at::Tensor>& bias, bool training, double momentum, double eps, at::Tensor& out, at::Tensor& save_mean, at::Tensor& save_invstd)` — [`L407`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L407)
- <a id="AtenNativeBatchNormLegitOut"></a>`AtenNativeBatchNormLegitOut(const at::Tensor& input, const std::optional<at::Tensor>& weight, const std::optional<at::Tensor>& bias, at::Tensor& running_mean, at::Tensor& running_variance, bool training, double momentum, double eps, at::Tensor& out, at::Tensor& save_mean, at::Tensor& save_invstd)` — [`L386`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L386)
- <a id="AtenNativeBatchNormOut"></a>`AtenNativeBatchNormOut(const at::Tensor& input, const std::optional<at::Tensor>& weight, const std::optional<at::Tensor>& bias, const std::optional<at::Tensor>& running_mean, const std::optional<at::Tensor>& running_variance, bool training, double momentum, double eps, at::Tensor& out, at::Tensor& save_mean, at::Tensor& save_invstd)` — [`L328`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L328)
- <a id="GetOptionalMlirOp"></a>`GetOptionalMlirOp(absl::Span<mlir::MlirOp> mlir_inputs, int index)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L63)
- <a id="PrepareBatchNormDispatch"></a>`PrepareBatchNormDispatch(const at::Tensor& input, std::optional<at::Tensor> weight, std::optional<at::Tensor> bias, std::optional<at::Tensor> running_mean, std::optional<at::Tensor> running_variance, bool training, double momentum, double eps)` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L78)
- <a id="TpuBatchNorm"></a>`TpuBatchNorm(const at::Tensor& input, std::optional<at::Tensor> weight, std::optional<at::Tensor> bias, std::optional<at::Tensor> running_mean, std::optional<at::Tensor> running_variance, bool training, double momentum, double eps, OpParamCacheKeys param_keys)` — [`L161`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L161)
- `TpuBatchNorm(const at::Tensor& input, std::optional<at::Tensor> weight, std::optional<at::Tensor> bias, std::optional<at::Tensor> running_mean, std::optional<at::Tensor> running_variance, bool training, double momentum, double eps, OpParamCacheKeys param_keys)` — [`L161`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L161)
- `TpuBatchNormBackward(const at::Tensor& grad_out, const at::Tensor& input, std::optional<at::Tensor> weight, std::optional<at::Tensor> running_mean, std::optional<at::Tensor> running_variance, std::optional<at::Tensor> save_mean, std::optional<at::Tensor> save_invstd, bool training, double eps, std::array<bool, 3> output_mask, OpParamCacheKeys param_keys)` — [`L201`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L201)
- <a id="TpuBatchNormBackward"></a>`TpuBatchNormBackward(const at::Tensor& grad_out, const at::Tensor& input, std::optional<at::Tensor> weight, std::optional<at::Tensor> running_mean, std::optional<at::Tensor> running_variance, std::optional<at::Tensor> save_mean, std::optional<at::Tensor> save_invstd, bool training, double eps, std::array<bool, 3> output_mask, OpParamCacheKeys param_keys)` — [`L201`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L201)
- <a id="TpuBatchNormOut"></a>`TpuBatchNormOut(const at::Tensor& input, std::optional<at::Tensor> weight, std::optional<at::Tensor> bias, std::optional<at::Tensor> running_mean, std::optional<at::Tensor> running_variance, bool training, double momentum, double eps, OpParamCacheKeys param_keys, at::Tensor& out, at::Tensor& save_mean, at::Tensor& save_invstd)` — [`L181`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L181)
- <a id="ValidateIsFloating"></a>`ValidateIsFloating(const at::Tensor& tensor, const std::string_view arg_name)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/native_batch_norm/native_batch_norm_aten_kernels.cc#L54)

