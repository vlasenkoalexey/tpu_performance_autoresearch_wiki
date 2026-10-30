---
title: 'Module: csrc/ops/linear/linear_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/linear/linear_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenLinearBackward: AtenLinearBackward(af45eeb4220d81d3).
  AtenLinearOut: AtenLinearOut(d8f9c1f5a2d55969).
  ValidateLinearInputs: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/ValidateLinearInputs(6210cbcc9e693a0e).'
  AtenLinear: AtenLinear(c55e30008c36c251).
  ValidateLinearBackwardInputs: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/ValidateLinearBackwardInputs(6ddad2e2cbb424ad).'
  LinearBackward: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/LinearBackward(742bac649611de04).'
  LinearOut: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/LinearOut(6f84c791db854508).'
  BuildLinearBackwardShlo: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/BuildLinearBackwardShlo(1c35b88cec0644c4).'
  DispatchLinearImpl: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/DispatchLinearImpl(6797626b288a0552).'
  Linear: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/Linear(4b9bce3a74b6508a).'
  BuildLinearShlo: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/BuildLinearShlo(6318e57f9f0741c5).'
  BuildGradInputShlo: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/BuildGradInputShlo(6a10f8d2c27db7fa).'
  AtenLinearAutograd: AtenLinearAutograd(c55e30008c36c251).
  AtenLinearAutograd.LinearBackwardNode: AtenLinearAutograd(c55e30008c36c251).LinearBackwardNode#
  BuildDotGeneral: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/BuildDotGeneral(bb5b679b97504dd8).'
  MaybeConjPhysicalShlo: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/MaybeConjPhysicalShlo(fe77f14d92bc5d4d).'
  IsPythonWrapperSubclass: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/IsPythonWrapperSubclass(b580d0b7e29ca914).'
  MakeAutogradNode: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/MakeAutogradNode(a52531b27a9fa42b).'
  IsFunctorchActive: '`$anonymous_namespace_csrc/ops/linear/linear_aten_kernels.cc`/IsFunctorchActive(c9857a73d68e59ba).'
---
# Module: [`csrc/ops/linear/linear_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc)

## Classes
### <a id="AtenLinearAutograd.LinearBackwardNode"></a>`AtenLinearAutograd.LinearBackwardNode`
- def: [`csrc/ops/linear/linear_aten_kernels.cc:454`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L454)
- signature: `using LinearBackwardNode = torch::autograd::generated::LinearBackward0`
- uses (calls/refs, reference-scoped): [`MakeAutogradNode`](linear_aten_kernels.cc.md#MakeAutogradNode)

## Functions
- <a id="AtenLinear"></a>`AtenLinear(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias)` — [`L474`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L474) — Implements `aten::linear` (`linear.default`): y = x @ A^T + b.
- <a id="AtenLinearAutograd"></a>`AtenLinearAutograd(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias)` — [`L435`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L435) — Implements `aten::linear` (`linear.default`) on `AutogradPrivateUse1`.
- <a id="AtenLinearBackward"></a>`AtenLinearBackward(const at::Tensor& self, const at::Tensor& grad_output, const at::Tensor& weight, std::array<bool, 3> output_mask)` — [`L493`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L493) — Implements `aten::linear_backward`, returning `(grad_input, grad_weight,
- <a id="AtenLinearOut"></a>`AtenLinearOut(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias, at::Tensor& out)` — [`L483`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L483) — Implements `aten::linear.out`: writes y = x @ A^T + b into `out`.
- <a id="BuildDotGeneral"></a>`BuildDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, absl::Span<const int64_t> lhs_contracting, absl::Span<const int64_t> rhs_contracting, mlir::stablehlo::Precision precision)` — [`L76`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L76) — Builds a StableHLO `dot_general` operation with the given contracting
- `BuildDotGeneral(mlir::MlirOp lhs, mlir::MlirOp rhs, absl::Span<const int64_t> lhs_contracting, absl::Span<const int64_t> rhs_contracting, mlir::stablehlo::Precision precision)` — [`L76`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L76) — Builds a StableHLO `dot_general` operation with the given contracting
- <a id="BuildGradInputShlo"></a>`BuildGradInputShlo(mlir::MlirOp grad_output, mlir::MlirOp weight, int64_t input_rank, int64_t weight_rank, bool is_complex, mlir::stablehlo::Precision precision)` — [`L138`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L138)
- `BuildGradInputShlo(mlir::MlirOp grad_output, mlir::MlirOp weight, int64_t input_rank, int64_t weight_rank, bool is_complex, mlir::stablehlo::Precision precision)` — [`L138`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L138)
- `BuildLinearBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp input, mlir::MlirOp weight, std::array<bool, 3> output_mask, mlir::stablehlo::Precision precision)` — [`L160`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L160) — Builds the StableHLO graph for `aten::linear_backward`.
- <a id="BuildLinearBackwardShlo"></a>`BuildLinearBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp input, mlir::MlirOp weight, std::array<bool, 3> output_mask, mlir::stablehlo::Precision precision)` — [`L160`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L160) — Builds the StableHLO graph for `aten::linear_backward`.
- <a id="BuildLinearShlo"></a>`BuildLinearShlo(mlir::MlirOp input, mlir::MlirOp weight, std::optional<mlir::MlirOp> bias, mlir::stablehlo::Precision precision)` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L112) — Builds the StableHLO graph for `aten::linear`: y = input @ weight^T + bias.
- `BuildLinearShlo(mlir::MlirOp input, mlir::MlirOp weight, std::optional<mlir::MlirOp> bias, mlir::stablehlo::Precision precision)` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L112) — Builds the StableHLO graph for `aten::linear`: y = input @ weight^T + bias.
- <a id="DispatchLinearImpl"></a>`DispatchLinearImpl(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias, Dimensions output_dims, OpParamCacheKeys param_keys, Dispatch2Fn&& dispatch2_fn, Dispatch3Fn&& dispatch3_fn)` — [`L285`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L285) — Shared dispatcher helper for `Linear` and `LinearOut`. Dispatches a 3-input
- <a id="IsFunctorchActive"></a>`IsFunctorchActive()` — [`L403`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L403)
- <a id="IsPythonWrapperSubclass"></a>`IsPythonWrapperSubclass(const at::Tensor& tensor)` — [`L414`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L414) — Returns true if `tensor` is a Python wrapper tensor subclass (such as
- <a id="Linear"></a>`Linear(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias, OpParamCacheKeys param_keys)` — [`L318`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L318)
- <a id="LinearBackward"></a>`LinearBackward(const at::Tensor& self, const at::Tensor& grad_output, const at::Tensor& weight, std::array<bool, 3> output_mask, OpParamCacheKeys param_keys)` — [`L355`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L355)
- <a id="LinearOut"></a>`LinearOut(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L336`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L336)
- <a id="MakeAutogradNode"></a>`MakeAutogradNode()` — [`L425`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L425) — Creates an autograd `Node` smart pointer (`c10::intrusive_ptr<T>` in PyTorch
- <a id="MaybeConjPhysicalShlo"></a>`MaybeConjPhysicalShlo(mlir::MlirOp op, bool is_complex)` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L130)
- <a id="ValidateLinearBackwardInputs"></a>`ValidateLinearBackwardInputs(const at::Tensor& self, const at::Tensor& grad_output, const at::Tensor& weight)` — [`L264`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L264) — Validates the self (input), grad_output, and weight tensors for
- <a id="ValidateLinearInputs"></a>`ValidateLinearInputs(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias)` — [`L216`](../../../../../../../raw/code/torch_tpu/csrc/ops/linear/linear_aten_kernels.cc#L216) — Validates the input, weight, and optional bias tensors for `aten::linear` and

