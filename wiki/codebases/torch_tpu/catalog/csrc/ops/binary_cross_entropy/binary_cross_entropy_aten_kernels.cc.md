---
title: 'Module: csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenBinaryCrossEntropyBackwardGradInput: AtenBinaryCrossEntropyBackwardGradInput(28d93f07a9280e71).
  AtenBinaryCrossEntropyBackward: AtenBinaryCrossEntropyBackward(b69579573519f5ed).
  AtenBinaryCrossEntropy: AtenBinaryCrossEntropy(50b32a4a2a8dc3ab).
  AtenBinaryCrossEntropyOut: AtenBinaryCrossEntropyOut(b1b0eccede248130).
  DispatchBinaryCrossEntropyOut: '`$anonymous_namespace_csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc`/DispatchBinaryCrossEntropyOut(f7a2d77b281521a4).'
  DispatchBinaryCrossEntropyBackwardOut: '`$anonymous_namespace_csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc`/DispatchBinaryCrossEntropyBackwardOut(2e50dd89bd95fb71).'
  BuildBinaryCrossEntropyShlo: '`$anonymous_namespace_csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc`/BuildBinaryCrossEntropyShlo(741abce3402da453).'
  ValidateIsFloatingPoint: '`$anonymous_namespace_csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc`/ValidateIsFloatingPoint(d8359b99282c084c).'
  BuildBinaryCrossEntropyBackwardShlo: '`$anonymous_namespace_csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc`/BuildBinaryCrossEntropyBackwardShlo(54bbffe95fc0e17c).'
---
# Module: [`csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc)

## Functions
- <a id="AtenBinaryCrossEntropy"></a>`AtenBinaryCrossEntropy(const at::Tensor& self, const at::Tensor& target, const std::optional<at::Tensor>& weight, int64_t reduction)` — [`L292`](../../../../../../../raw/code/torch_tpu/csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc#L292)
- <a id="AtenBinaryCrossEntropyBackward"></a>`AtenBinaryCrossEntropyBackward(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& target, const std::optional<at::Tensor>& weight, int64_t reduction)` — [`L320`](../../../../../../../raw/code/torch_tpu/csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc#L320)
- <a id="AtenBinaryCrossEntropyBackwardGradInput"></a>`AtenBinaryCrossEntropyBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& target, const std::optional<at::Tensor>& weight, int64_t reduction, at::Tensor& grad_input)` — [`L337`](../../../../../../../raw/code/torch_tpu/csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc#L337)
- <a id="AtenBinaryCrossEntropyOut"></a>`AtenBinaryCrossEntropyOut(const at::Tensor& self, const at::Tensor& target, const std::optional<at::Tensor>& weight, int64_t reduction, at::Tensor& out)` — [`L308`](../../../../../../../raw/code/torch_tpu/csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc#L308)
- <a id="BuildBinaryCrossEntropyBackwardShlo"></a>`BuildBinaryCrossEntropyBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp self, mlir::MlirOp target, std::optional<mlir::MlirOp> weight, int64_t reduction, mlir::MlirBuilder& builder)` — [`L189`](../../../../../../../raw/code/torch_tpu/csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc#L189)
- <a id="BuildBinaryCrossEntropyShlo"></a>`BuildBinaryCrossEntropyShlo(mlir::MlirOp input, mlir::MlirOp target, std::optional<mlir::MlirOp> weight, int64_t reduction, mlir::MlirBuilder& builder)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc#L63)
- <a id="DispatchBinaryCrossEntropyBackwardOut"></a>`DispatchBinaryCrossEntropyBackwardOut(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& target, const std::optional<at::Tensor>& weight, int64_t reduction, at::Tensor& grad_input, OpParamCacheKeys param_keys)` — [`L233`](../../../../../../../raw/code/torch_tpu/csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc#L233)
- <a id="DispatchBinaryCrossEntropyOut"></a>`DispatchBinaryCrossEntropyOut(const at::Tensor& self, const at::Tensor& target, const std::optional<at::Tensor>& weight, int64_t reduction, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L137`](../../../../../../../raw/code/torch_tpu/csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc#L137)
- <a id="ValidateIsFloatingPoint"></a>`ValidateIsFloatingPoint(const at::Tensor& tensor, std::string_view arg_name)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/binary_cross_entropy/binary_cross_entropy_aten_kernels.cc#L55)

