---
title: 'Module: csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenCrossEntropyLoss: AtenCrossEntropyLoss(a835b28744cce674).
  CrossEntropyLossBackwardSelfKernel: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/CrossEntropyLossBackwardSelfKernel(f437b3b9b82af231).'
  CrossEntropyLossBackwardTargetKernel: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/CrossEntropyLossBackwardTargetKernel(3aab542e045a87bf).'
  ValidateCrossEntropyLoss: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/ValidateCrossEntropyLoss(cc782ed9e1a8f36b).'
  BuildCrossEntropyClassIndicesShlo: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/BuildCrossEntropyClassIndicesShlo(e67f42b304f2e4bc).'
  ValidateHardTargetShapes: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/ValidateHardTargetShapes(b2d6689cde60befb).'
  BuildCrossEntropyProbTargetShlo: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/BuildCrossEntropyProbTargetShlo(4b5f99a3980322d).'
  BuildCrossEntropyClassIndicesBackwardShlo: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/BuildCrossEntropyClassIndicesBackwardShlo(d99573c5692b265d).'
  ExpandGradOutputToSelfShape: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/ExpandGradOutputToSelfShape(9272795d3ca1af82).'
  BuildCrossEntropyProbTargetBackwardShlo: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/BuildCrossEntropyProbTargetBackwardShlo(2189b52b522d81db).'
  BuildCrossEntropyLossBackwardShlo: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/BuildCrossEntropyLossBackwardShlo(444258a57da8732b).'
  BuildCrossEntropyLossBackwardTargetShlo: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/BuildCrossEntropyLossBackwardTargetShlo(5a90e79abff9f838).'
  BuildCrossEntropyLossShlo: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/BuildCrossEntropyLossShlo(8fe15eb44c0e04ce).'
  BuildEmptyCrossEntropyLossShlo: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/BuildEmptyCrossEntropyLossShlo(67cff18c1b8a6a49).'
  RoundThroughOrigDtype: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/RoundThroughOrigDtype(d399942944e418c2).'
  AtenCrossEntropyLossAutograd: AtenCrossEntropyLossAutograd(a835b28744cce674).
  CrossEntropyTargetMode.kProbabilities: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/CrossEntropyTargetMode#kProbabilities.'
  CrossEntropyLossFunction.backward: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/CrossEntropyLossFunction#backward(305625f81d7e100).'
  CrossEntropyTargetMode: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/CrossEntropyTargetMode#'
  CrossEntropyLossFunction: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/CrossEntropyLossFunction#'
  CrossEntropyLossFunction.forward: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/CrossEntropyLossFunction#forward(d2f9a881c7a2ab9).'
  GetCrossEntropyOutputDims: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/GetCrossEntropyOutputDims(3758c68a339ded85).'
  CrossEntropyTargetMode.kClassIndices: '`$anonymous_namespace_csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`/CrossEntropyTargetMode#kClassIndices.'
---
# Module: [`csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc)

## Classes
### <a id="CrossEntropyLossFunction"></a>`CrossEntropyLossFunction`  ·  implements/extends Function
- def: [`csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc:885`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L885)
- signature: `class CrossEntropyLossFunction : public torch::autograd::Function<CrossEntropyLossFunction>`
- members:
  - <a id="CrossEntropyLossFunction.backward"></a>`backward(torch::autograd::AutogradContext* ctx, torch::autograd::variable_list grad_outputs)` — [`L905`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L905)
  - `backward(torch::autograd::AutogradContext* ctx, torch::autograd::variable_list grad_outputs)` — [`L905`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L905)
  - <a id="CrossEntropyLossFunction.forward"></a>`forward(torch::autograd::AutogradContext* ctx, const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, double label_smoothing)` — [`L888`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L888)
- uses (calls/refs, reference-scoped): [`AtenCrossEntropyLoss`](cross_entropy_loss_aten_kernels.cc.md#AtenCrossEntropyLoss), [`CrossEntropyLossBackwardSelfKernel`](cross_entropy_loss_aten_kernels.cc.md#CrossEntropyLossBackwardSelfKernel), [`CrossEntropyLossBackwardTargetKernel`](cross_entropy_loss_aten_kernels.cc.md#CrossEntropyLossBackwardTargetKernel)
- used by: [`AtenCrossEntropyLossAutograd`](cross_entropy_loss_aten_kernels.cc.md#AtenCrossEntropyLossAutograd)

### <a id="CrossEntropyTargetMode"></a>`CrossEntropyTargetMode`
- def: [`csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc:62`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L62)
- signature: `enum class CrossEntropyTargetMode`
- members:
  - <a id="CrossEntropyTargetMode.kClassIndices"></a>`kClassIndices` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L63)
  - <a id="CrossEntropyTargetMode.kProbabilities"></a>`kProbabilities` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L64)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`AtenCrossEntropyLoss`](cross_entropy_loss_aten_kernels.cc.md#AtenCrossEntropyLoss), [`CrossEntropyLossBackwardSelfKernel`](cross_entropy_loss_aten_kernels.cc.md#CrossEntropyLossBackwardSelfKernel), [`BuildCrossEntropyLossBackwardShlo`](cross_entropy_loss_aten_kernels.cc.md#BuildCrossEntropyLossBackwardShlo), [`BuildCrossEntropyLossShlo`](cross_entropy_loss_aten_kernels.cc.md#BuildCrossEntropyLossShlo)

## Functions
- <a id="AtenCrossEntropyLoss"></a>`AtenCrossEntropyLoss(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, double label_smoothing)` — [`L940`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L940)
- <a id="AtenCrossEntropyLossAutograd"></a>`AtenCrossEntropyLossAutograd(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, double label_smoothing)` — [`L998`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L998)
- <a id="BuildCrossEntropyClassIndicesBackwardShlo"></a>`BuildCrossEntropyClassIndicesBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp probs, mlir::MlirOp target, std::optional<mlir::MlirOp> weight, int64_t reduction, int64_t ignore_index, double label_smoothing, mlir::ElementType compute_dtype)` — [`L394`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L394)
- <a id="BuildCrossEntropyClassIndicesShlo"></a>`BuildCrossEntropyClassIndicesShlo(mlir::MlirOp log_probs, mlir::MlirOp target, std::optional<mlir::MlirOp> weight, int64_t reduction, int64_t ignore_index, double label_smoothing, mlir::ElementType orig_self_dtype, mlir::ElementType compute_dtype, mlir::MlirBuilder& builder)` — [`L218`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L218)
- <a id="BuildCrossEntropyLossBackwardShlo"></a>`BuildCrossEntropyLossBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp self, mlir::MlirOp target, std::optional<mlir::MlirOp> weight, int64_t reduction, int64_t ignore_index, double label_smoothing, CrossEntropyTargetMode target_mode, mlir::MlirBuilder& builder)` — [`L558`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L558)
- <a id="BuildCrossEntropyLossBackwardTargetShlo"></a>`BuildCrossEntropyLossBackwardTargetShlo(mlir::MlirOp grad_output, mlir::MlirOp self, std::optional<mlir::MlirOp> weight, int64_t reduction, double label_smoothing, mlir::MlirBuilder& builder)` — [`L621`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L621)
- <a id="BuildCrossEntropyLossShlo"></a>`BuildCrossEntropyLossShlo(mlir::MlirOp self, mlir::MlirOp target, std::optional<mlir::MlirOp> weight, int64_t reduction, int64_t ignore_index, double label_smoothing, CrossEntropyTargetMode target_mode, mlir::MlirBuilder& builder)` — [`L495`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L495)
- <a id="BuildCrossEntropyProbTargetBackwardShlo"></a>`BuildCrossEntropyProbTargetBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp self, mlir::MlirOp target, std::optional<mlir::MlirOp> weight, int64_t reduction, double label_smoothing, mlir::ElementType orig_self_dtype, mlir::ElementType compute_dtype, mlir::MlirBuilder& builder)` — [`L324`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L324)
- <a id="BuildCrossEntropyProbTargetShlo"></a>`BuildCrossEntropyProbTargetShlo(mlir::MlirOp log_probs, mlir::MlirOp target, std::optional<mlir::MlirOp> weight, int64_t reduction, double label_smoothing, mlir::ElementType orig_self_dtype, mlir::ElementType compute_dtype, mlir::MlirBuilder& builder)` — [`L149`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L149)
- <a id="BuildEmptyCrossEntropyLossShlo"></a>`BuildEmptyCrossEntropyLossShlo(mlir::RankedTensorType orig_self_type, mlir::ElementType orig_self_dtype, int64_t reduction, mlir::MlirBuilder& builder)` — [`L115`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L115)
- <a id="CrossEntropyLossBackwardSelfKernel"></a>`CrossEntropyLossBackwardSelfKernel(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, double label_smoothing)` — [`L783`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L783)
- <a id="CrossEntropyLossBackwardTargetKernel"></a>`CrossEntropyLossBackwardTargetKernel(const at::Tensor& grad_output, const at::Tensor& self, const c10::optional<at::Tensor>& weight, int64_t reduction, double label_smoothing)` — [`L839`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L839)
- <a id="ExpandGradOutputToSelfShape"></a>`ExpandGradOutputToSelfShape(mlir::MlirOp grad_output, mlir::RankedTensorType self_type, int64_t reduction, std::optional<mlir::MlirOp> denom_scalar)` — [`L69`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L69) — Expands `grad_output` to match `self_type`'s shape `[N, C, d1, ..., dk]`
- <a id="GetCrossEntropyOutputDims"></a>`GetCrossEntropyOutputDims(const at::Tensor& self, int64_t reduction)` — [`L770`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L770)
- <a id="RoundThroughOrigDtype"></a>`RoundThroughOrigDtype(mlir::MlirOp op, mlir::ElementType orig_dtype, mlir::ElementType compute_dtype)` — [`L105`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L105)
- <a id="ValidateCrossEntropyLoss"></a>`ValidateCrossEntropyLoss(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, double label_smoothing)` — [`L721`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L721)
- <a id="ValidateHardTargetShapes"></a>`ValidateHardTargetShapes(const at::Tensor& self, const at::Tensor& target)` — [`L689`](../../../../../../../raw/code/torch_tpu/csrc/ops/cross_entropy_loss/cross_entropy_loss_aten_kernels.cc#L689)

