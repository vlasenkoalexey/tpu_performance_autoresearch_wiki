---
title: 'Module: csrc/ops/nll_loss/nll_loss_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/nll_loss/nll_loss_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenNllLoss2dBackward: AtenNllLoss2dBackward(8d8b68b8289e8ebc).
  AtenNllLoss2dBackwardGradInput: AtenNllLoss2dBackwardGradInput(5aaba80867bf793a).
  AtenNllLoss2dForward: AtenNllLoss2dForward(8edf79d830e85b50).
  NllLossNdForwardWithTotalWeight: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/NllLossNdForwardWithTotalWeight(8edf79d830e85b50).'
  NllLossBackwardKernel: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/NllLossBackwardKernel(8d8b68b8289e8ebc).'
  AtenNllLoss2dForwardOut: AtenNllLoss2dForwardOut(6118398328306e4).
  AtenNllLossBackwardGradInput: AtenNllLossBackwardGradInput(5aaba80867bf793a).
  AtenNllLossForwardOut: AtenNllLossForwardOut(6118398328306e4).
  ValidateNllLossCommon: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/ValidateNllLossCommon(3c2acc7524ebc5af).'
  ValidateNllLossNdShapes: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/ValidateNllLossNdShapes(b2d6689cde60befb).'
  ValidateNllLoss2dForwardShapes: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/ValidateNllLoss2dForwardShapes(b2d6689cde60befb).'
  ValidateNllLoss1dOr2dShapes: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/ValidateNllLoss1dOr2dShapes(b2d6689cde60befb).'
  DispatchNllLossForwardOut: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/DispatchNllLossForwardOut(8072f87d53c823fb).'
  DispatchNllLossBackwardOut: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/DispatchNllLossBackwardOut(99b7513493af4480).'
  DispatchNllLossBackwardBuffer: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/DispatchNllLossBackwardBuffer(945bda5aa326016f).'
  DispatchNllLossForwardBuffers: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/DispatchNllLossForwardBuffers(977cfc1d63316398).'
  IsFakeOrFunctorchLossInputs: IsFakeOrFunctorchLossInputs(7c8e4bbd25dfe6b3).
  AtenNllLossNd: AtenNllLossNd(6812504a79740e95).
  AtenNllLossNdAutograd: AtenNllLossNdAutograd(6812504a79740e95).
  IsSupportedLossFloatType: IsSupportedLossFloatType(76fead7d2a82ed4d).
  IsLongOrByteTarget: IsLongOrByteTarget(b580d0b7e29ca914).
  IsFakeOrFunctorchTensor: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/IsFakeOrFunctorchTensor(b580d0b7e29ca914).'
  NllLossNdFunction: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/NllLossNdFunction#'
  NllLossNdFunction.forward: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/NllLossNdFunction#forward(5033ce2270fdea7a).'
  NllLossNdFunction.backward: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/NllLossNdFunction#backward(305625f81d7e100).'
  IsFunctorchActive: '`$anonymous_namespace_csrc/ops/nll_loss/nll_loss_aten_kernels.cc`/IsFunctorchActive(c9857a73d68e59ba).'
---
# Module: [`csrc/ops/nll_loss/nll_loss_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc)

## Classes
### <a id="NllLossNdFunction"></a>`NllLossNdFunction`  ·  implements/extends Function
- def: [`csrc/ops/nll_loss/nll_loss_aten_kernels.cc:364`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L364)
- signature: `class NllLossNdFunction : public torch::autograd::Function<NllLossNdFunction>`
- members:
  - `backward(torch::autograd::AutogradContext* ctx, torch::autograd::variable_list grad_outputs)` — [`L381`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L381)
  - <a id="NllLossNdFunction.backward"></a>`backward(torch::autograd::AutogradContext* ctx, torch::autograd::variable_list grad_outputs)` — [`L381`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L381)
  - <a id="NllLossNdFunction.forward"></a>`forward(torch::autograd::AutogradContext* ctx, const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index)` — [`L366`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L366)
- uses (calls/refs, reference-scoped): [`NllLossNdForwardWithTotalWeight`](nll_loss_aten_kernels.cc.md#NllLossNdForwardWithTotalWeight), [`NllLossBackwardKernel`](nll_loss_aten_kernels.cc.md#NllLossBackwardKernel)
- used by: [`AtenNllLossNdAutograd`](nll_loss_aten_kernels.cc.md#AtenNllLossNdAutograd)

## Functions
- <a id="AtenNllLoss2dBackward"></a>`AtenNllLoss2dBackward(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, const at::Tensor& total_weight)` — [`L505`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L505)
- <a id="AtenNllLoss2dBackwardGradInput"></a>`AtenNllLoss2dBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, const at::Tensor& total_weight, at::Tensor& grad_input)` — [`L532`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L532)
- <a id="AtenNllLoss2dForward"></a>`AtenNllLoss2dForward(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index)` — [`L451`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L451)
- <a id="AtenNllLoss2dForwardOut"></a>`AtenNllLoss2dForwardOut(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, at::Tensor& output, at::Tensor& total_weight)` — [`L469`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L469)
- <a id="AtenNllLossBackwardGradInput"></a>`AtenNllLossBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, const at::Tensor& total_weight, at::Tensor& grad_input)` — [`L486`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L486)
- <a id="AtenNllLossForwardOut"></a>`AtenNllLossForwardOut(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, at::Tensor& output, at::Tensor& total_weight)` — [`L434`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L434)
- <a id="AtenNllLossNd"></a>`AtenNllLossNd(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index)` — [`L557`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L557)
- <a id="AtenNllLossNdAutograd"></a>`AtenNllLossNdAutograd(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index)` — [`L568`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L568)
- <a id="DispatchNllLossBackwardBuffer"></a>`DispatchNllLossBackwardBuffer(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, const at::Tensor& total_weight, OpParamCacheKeys param_keys)` — [`L240`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L240)
- <a id="DispatchNllLossBackwardOut"></a>`DispatchNllLossBackwardOut(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, const at::Tensor& total_weight, at::Tensor& grad_input, OpParamCacheKeys param_keys)` — [`L282`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L282)
- <a id="DispatchNllLossForwardBuffers"></a>`DispatchNllLossForwardBuffers(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, OpParamCacheKeys param_keys)` — [`L144`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L144)
- <a id="DispatchNllLossForwardOut"></a>`DispatchNllLossForwardOut(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, at::Tensor& output, at::Tensor& total_weight, OpParamCacheKeys param_keys)` — [`L190`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L190)
- <a id="IsFakeOrFunctorchLossInputs"></a>`IsFakeOrFunctorchLossInputs(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight)` — [`L407`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L407)
- <a id="IsFakeOrFunctorchTensor"></a>`IsFakeOrFunctorchTensor(const at::Tensor& tensor)` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L62)
- <a id="IsFunctorchActive"></a>`IsFunctorchActive()` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L56)
- <a id="IsLongOrByteTarget"></a>`IsLongOrByteTarget(const at::Tensor& tensor)` — [`L428`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L428)
- <a id="IsSupportedLossFloatType"></a>`IsSupportedLossFloatType(at::ScalarType scalar_type)` — [`L415`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L415)
- <a id="NllLossBackwardKernel"></a>`NllLossBackwardKernel(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index, const at::Tensor& total_weight)` — [`L342`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L342)
- <a id="NllLossNdForwardWithTotalWeight"></a>`NllLossNdForwardWithTotalWeight(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction, int64_t ignore_index)` — [`L324`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L324)
- <a id="ValidateNllLoss1dOr2dShapes"></a>`ValidateNllLoss1dOr2dShapes(const at::Tensor& self, const at::Tensor& target)` — [`L95`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L95)
- <a id="ValidateNllLoss2dForwardShapes"></a>`ValidateNllLoss2dForwardShapes(const at::Tensor& self, const at::Tensor& target)` — [`L115`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L115)
- <a id="ValidateNllLossCommon"></a>`ValidateNllLossCommon(const at::Tensor& self, const at::Tensor& target, const c10::optional<at::Tensor>& weight, int64_t reduction)` — [`L69`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L69)
- <a id="ValidateNllLossNdShapes"></a>`ValidateNllLossNdShapes(const at::Tensor& self, const at::Tensor& target)` — [`L127`](../../../../../../../raw/code/torch_tpu/csrc/ops/nll_loss/nll_loss_aten_kernels.cc#L127)

