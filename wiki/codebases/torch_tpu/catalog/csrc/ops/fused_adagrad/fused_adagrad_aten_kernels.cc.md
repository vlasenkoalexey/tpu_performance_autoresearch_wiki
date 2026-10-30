---
title: 'Module: csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenFusedAdagradTensorLr: AtenFusedAdagradTensorLr(304d8363cd551411).
  AtenFusedAdagrad: AtenFusedAdagrad(f11bf39d99a7cab3).
  BuildAdagradShlo: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/BuildAdagradShlo(8245facdeb38f3c0).'
  DispatchAdagrad: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/DispatchAdagrad(b54158d4453e2fc7).'
  BuildAdagradStepForOneParam: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/BuildAdagradStepForOneParam(49c16efae04c9a5).'
  ValidateAdagradTensorListSizes: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/ValidateAdagradTensorListSizes(b9a29e7f75db1002).'
  SetAdagradParamCacheKeys: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/SetAdagradParamCacheKeys(e66ba0ad775acaf7).'
  ApplyFoundInfRevert: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/ApplyFoundInfRevert(2eef5c0df22e4440).'
  AssignBuffers: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AssignBuffers(2d951a6487e63a37).'
  AppendDtypes: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AppendDtypes(9449544dff2f41b4).'
  GradScaleMode: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/GradScaleMode#'
  CastOneParamOutputs: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/CastOneParamOutputs(603ed812421d9520).'
  ExtractAdagradInputs: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/ExtractAdagradInputs(b65cc48dc602b771).'
  GatherAdagradOutDtypes: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/GatherAdagradOutDtypes(9b1a646e9541c9ef).'
  AssignAdagradResultBuffers: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AssignAdagradResultBuffers(582302bff59f4721).'
  GatherAdagradOutDims: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/GatherAdagradOutDims(8fd81d8d7688b87d).'
  GatherAdagradInputs: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/GatherAdagradInputs(ff48cb62da6099e1).'
  GetGradScaleMode: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/GetGradScaleMode(9571ae46e3dcae0f).'
  ExtractAdagradDtypes: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/ExtractAdagradDtypes(828dba7f3ba0a400).'
  OneParamResult.grad: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/OneParamResult#grad.'
  OneParamResult.state_sum: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/OneParamResult#state_sum.'
  FoundInfMode: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/FoundInfMode#'
  GradScaleMode.kEnabled: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/GradScaleMode#kEnabled.'
  GetFoundInfMode: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/GetFoundInfMode(78cf493ad9e67ae9).'
  CombineAdagradResults: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/CombineAdagradResults(53396735191598d2).'
  OneParamResult.param: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/OneParamResult#param.'
  MetaFusedAdagradTensorLr: MetaFusedAdagradTensorLr(304d8363cd551411).
  OneParamResult: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/OneParamResult#'
  MetaFusedAdagrad: MetaFusedAdagrad(f11bf39d99a7cab3).
  AppendDims: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AppendDims(9449544dff2f41b4).'
  AdagradInputSpans: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradInputSpans#'
  AdagradDtypeSpans: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradDtypeSpans#'
  FoundInfMode.kEnabled: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/FoundInfMode#kEnabled.'
  AdagradDtypeSpans.grads: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradDtypeSpans#grads.'
  AdagradInputSpans.state_sums: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradInputSpans#state_sums.'
  AdagradInputSpans.found_inf: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradInputSpans#found_inf.'
  AdagradInputSpans.params: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradInputSpans#params.'
  AdagradDtypeSpans.params: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradDtypeSpans#params.'
  AdagradObjectiveMode: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradObjectiveMode#'
  AdagradInputSpans.grads: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradInputSpans#grads.'
  MetaFusedAdagradFunctional: MetaFusedAdagradFunctional(8999b88ac42e5fdd).
  MetaFusedAdagradFunctionalTensorLr: MetaFusedAdagradFunctionalTensorLr(b7593d19440048b2).
  AdagradDtypeSpans.state_sums: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradDtypeSpans#state_sums.'
  AdagradInputSpans.steps: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradInputSpans#steps.'
  AdagradInputSpans.eps: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradInputSpans#eps.'
  AdagradInputSpans.lr_decay: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradInputSpans#lr_decay.'
  AdagradInputSpans.lr: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradInputSpans#lr.'
  AdagradInputSpans.weight_decay: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradInputSpans#weight_decay.'
  AdagradInputSpans.grad_scale: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradInputSpans#grad_scale.'
  AdagradObjectiveMode.kMaximize: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradObjectiveMode#kMaximize.'
  AdagradObjectiveMode.kMinimize: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/AdagradObjectiveMode#kMinimize.'
  GradScaleMode.kDisabled: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/GradScaleMode#kDisabled.'
  FoundInfMode.kDisabled: '`$anonymous_namespace_csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`/FoundInfMode#kDisabled.'
---
# Module: [`csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc)

## Classes
### <a id="AdagradDtypeSpans"></a>`AdagradDtypeSpans`
- def: [`csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc:313`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L313)
- signature: `struct AdagradDtypeSpans`
- members:
  - <a id="AdagradDtypeSpans.grads"></a>`grads` — [`L315`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L315)
  - <a id="AdagradDtypeSpans.params"></a>`params` — [`L314`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L314)
  - <a id="AdagradDtypeSpans.state_sums"></a>`state_sums` — [`L316`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L316)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildAdagradShlo`](fused_adagrad_aten_kernels.cc.md#BuildAdagradShlo), [`ExtractAdagradDtypes`](fused_adagrad_aten_kernels.cc.md#ExtractAdagradDtypes)

### <a id="AdagradInputSpans"></a>`AdagradInputSpans`
- def: [`csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc:268`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L268)
- signature: `struct AdagradInputSpans`
- members:
  - <a id="AdagradInputSpans.eps"></a>`eps` — [`L276`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L276)
  - <a id="AdagradInputSpans.found_inf"></a>`found_inf` — [`L278`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L278)
  - <a id="AdagradInputSpans.grad_scale"></a>`grad_scale` — [`L277`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L277)
  - <a id="AdagradInputSpans.grads"></a>`grads` — [`L270`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L270)
  - <a id="AdagradInputSpans.lr"></a>`lr` — [`L273`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L273)
  - <a id="AdagradInputSpans.lr_decay"></a>`lr_decay` — [`L274`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L274)
  - <a id="AdagradInputSpans.params"></a>`params` — [`L269`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L269)
  - <a id="AdagradInputSpans.state_sums"></a>`state_sums` — [`L271`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L271)
  - <a id="AdagradInputSpans.steps"></a>`steps` — [`L272`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L272)
  - <a id="AdagradInputSpans.weight_decay"></a>`weight_decay` — [`L275`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L275)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildAdagradShlo`](fused_adagrad_aten_kernels.cc.md#BuildAdagradShlo), [`ExtractAdagradInputs`](fused_adagrad_aten_kernels.cc.md#ExtractAdagradInputs)

### <a id="AdagradObjectiveMode"></a>`AdagradObjectiveMode`
- def: [`csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc:53`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L53)
- signature: `enum class AdagradObjectiveMode : bool`
- members:
  - <a id="AdagradObjectiveMode.kMaximize"></a>`kMaximize` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L53)
  - <a id="AdagradObjectiveMode.kMinimize"></a>`kMinimize` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L53)
- used by: [`AtenFusedAdagrad`](fused_adagrad_aten_kernels.cc.md#AtenFusedAdagrad), [`AtenFusedAdagradTensorLr`](fused_adagrad_aten_kernels.cc.md#AtenFusedAdagradTensorLr), [`BuildAdagradShlo`](fused_adagrad_aten_kernels.cc.md#BuildAdagradShlo), [`DispatchAdagrad`](fused_adagrad_aten_kernels.cc.md#DispatchAdagrad), [`BuildAdagradStepForOneParam`](fused_adagrad_aten_kernels.cc.md#BuildAdagradStepForOneParam)

### <a id="FoundInfMode"></a>`FoundInfMode`
- def: [`csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc:55`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L55)
- signature: `enum class FoundInfMode : bool`
- members:
  - <a id="FoundInfMode.kDisabled"></a>`kDisabled` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L55)
  - <a id="FoundInfMode.kEnabled"></a>`kEnabled` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L55)
- uses (calls/refs, reference-scoped): [`GradScaleMode`](fused_adagrad_aten_kernels.cc.md#GradScaleMode)
- used by: [`BuildAdagradShlo`](fused_adagrad_aten_kernels.cc.md#BuildAdagradShlo), [`DispatchAdagrad`](fused_adagrad_aten_kernels.cc.md#DispatchAdagrad), [`SetAdagradParamCacheKeys`](fused_adagrad_aten_kernels.cc.md#SetAdagradParamCacheKeys), [`ExtractAdagradInputs`](fused_adagrad_aten_kernels.cc.md#ExtractAdagradInputs), [`GatherAdagradInputs`](fused_adagrad_aten_kernels.cc.md#GatherAdagradInputs), [`GetGradScaleMode`](fused_adagrad_aten_kernels.cc.md#GetGradScaleMode), [`GetFoundInfMode`](fused_adagrad_aten_kernels.cc.md#GetFoundInfMode)

### <a id="GradScaleMode"></a>`GradScaleMode`
- def: [`csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc:54`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L54)
- signature: `enum class GradScaleMode : bool`
- members:
  - <a id="GradScaleMode.kDisabled"></a>`kDisabled` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L54)
  - <a id="GradScaleMode.kEnabled"></a>`kEnabled` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L54)
- used by: [`BuildAdagradShlo`](fused_adagrad_aten_kernels.cc.md#BuildAdagradShlo), [`DispatchAdagrad`](fused_adagrad_aten_kernels.cc.md#DispatchAdagrad), [`SetAdagradParamCacheKeys`](fused_adagrad_aten_kernels.cc.md#SetAdagradParamCacheKeys), [`ExtractAdagradInputs`](fused_adagrad_aten_kernels.cc.md#ExtractAdagradInputs), [`GatherAdagradOutDtypes`](fused_adagrad_aten_kernels.cc.md#GatherAdagradOutDtypes), [`AssignAdagradResultBuffers`](fused_adagrad_aten_kernels.cc.md#AssignAdagradResultBuffers), [`GatherAdagradOutDims`](fused_adagrad_aten_kernels.cc.md#GatherAdagradOutDims), [`GatherAdagradInputs`](fused_adagrad_aten_kernels.cc.md#GatherAdagradInputs), [`ExtractAdagradDtypes`](fused_adagrad_aten_kernels.cc.md#ExtractAdagradDtypes), [`GetGradScaleMode`](fused_adagrad_aten_kernels.cc.md#GetGradScaleMode), [`CombineAdagradResults`](fused_adagrad_aten_kernels.cc.md#CombineAdagradResults), [`kEnabled`](fused_adagrad_aten_kernels.cc.md#FoundInfMode.kEnabled)

### <a id="OneParamResult"></a>`OneParamResult`
- def: [`csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc:125`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L125)
- signature: `struct OneParamResult`
- members:
  - <a id="OneParamResult.grad"></a>`grad` — [`L127`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L127)
  - <a id="OneParamResult.param"></a>`param` — [`L126`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L126)
  - <a id="OneParamResult.state_sum"></a>`state_sum` — [`L128`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L128)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildAdagradShlo`](fused_adagrad_aten_kernels.cc.md#BuildAdagradShlo), [`BuildAdagradStepForOneParam`](fused_adagrad_aten_kernels.cc.md#BuildAdagradStepForOneParam), [`ApplyFoundInfRevert`](fused_adagrad_aten_kernels.cc.md#ApplyFoundInfRevert), [`CastOneParamOutputs`](fused_adagrad_aten_kernels.cc.md#CastOneParamOutputs)

## Functions
- `AppendDims(const at::TensorList tensors, std::vector<absl::Span<const int64_t>>& out_dims)` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L117) — Appends tensor shape dimensions to the output dimensions list.
- <a id="AppendDims"></a>`AppendDims(const at::TensorList tensors, std::vector<absl::Span<const int64_t>>& out_dims)` — [`L117`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L117) — Appends tensor shape dimensions to the output dimensions list.
- `AppendDtypes(const at::TensorList tensors, std::vector<mlir::ElementType>& out_dtypes)` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L106) — Appends converted MLIR element types of tensors to the output list.
- <a id="AppendDtypes"></a>`AppendDtypes(const at::TensorList tensors, std::vector<mlir::ElementType>& out_dtypes)` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L106) — Appends converted MLIR element types of tensors to the output list.
- <a id="ApplyFoundInfRevert"></a>`ApplyFoundInfRevert(OneParamResult current, mlir::MlirOp param_old, mlir::MlirOp grad_old, mlir::MlirOp state_sum_old, mlir::MlirOp found_inf, mlir::ElementType comp_type)` — [`L132`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L132) — Reverts param, grad, and state sum to previous values if found_inf is true.
- `AssignAdagradResultBuffers(std::vector<DeviceBufferRef>& result_buffers, at::TensorList self, at::TensorList grads, at::TensorList state_sums, const GradScaleMode grad_scale_mode)` — [`L465`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L465) — Assigns device output buffers back to ATen param, grad, and sum tensors.
- <a id="AssignAdagradResultBuffers"></a>`AssignAdagradResultBuffers(std::vector<DeviceBufferRef>& result_buffers, at::TensorList self, at::TensorList grads, at::TensorList state_sums, const GradScaleMode grad_scale_mode)` — [`L465`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L465) — Assigns device output buffers back to ATen param, grad, and sum tensors.
- <a id="AssignBuffers"></a>`AssignBuffers(std::vector<DeviceBufferRef>& buffers, const size_t offset, const at::TensorList tensors)` — [`L97`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L97) — Assigns a slice of device buffers back to a list of PyTorch tensors.
- `AssignBuffers(std::vector<DeviceBufferRef>& buffers, const size_t offset, const at::TensorList tensors)` — [`L97`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L97) — Assigns a slice of device buffers back to a list of PyTorch tensors.
- <a id="AtenFusedAdagrad"></a>`AtenFusedAdagrad(at::TensorList self, at::TensorList grads, at::TensorList state_sums, at::TensorList state_steps, double lr, double lr_decay, double weight_decay, double eps, bool maximize, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf)` — [`L543`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L543) — Executes multi-tensor Adagrad optimizer step with a scalar learning rate. — documented in [fused-optimizer-kernels](../../../../concepts/fused-optimizer-kernels.md)
- <a id="AtenFusedAdagradTensorLr"></a>`AtenFusedAdagradTensorLr(at::TensorList self, at::TensorList grads, at::TensorList state_sums, at::TensorList state_steps, const at::Tensor& lr, double lr_decay, double weight_decay, double eps, bool maximize, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf)` — [`L584`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L584) — Executes multi-tensor Adagrad optimizer step with a tensor learning rate.
- <a id="BuildAdagradShlo"></a>`BuildAdagradShlo(absl::Span<mlir::MlirOp> inputs, const size_t num_tensors, const AdagradObjectiveMode maximize_mode, const GradScaleMode grad_scale_mode, const FoundInfMode found_inf_mode, absl::Span<const mlir::ElementType> out_dtypes)` — [`L355`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L355) — Constructs the StableHLO computation graph for all parameter tensors.
- `BuildAdagradShlo(absl::Span<mlir::MlirOp> inputs, const size_t num_tensors, const AdagradObjectiveMode maximize_mode, const GradScaleMode grad_scale_mode, const FoundInfMode found_inf_mode, absl::Span<const mlir::ElementType> out_dtypes)` — [`L355`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L355) — Constructs the StableHLO computation graph for all parameter tensors.
- <a id="BuildAdagradStepForOneParam"></a>`BuildAdagradStepForOneParam(mlir::MlirOp param, mlir::MlirOp grad, mlir::MlirOp state_sum, mlir::MlirOp step, mlir::MlirOp lr, mlir::MlirOp lr_decay, mlir::MlirOp weight_decay, mlir::MlirOp eps, const AdagradObjectiveMode maximize_mode, std::optional<mlir::MlirOp> grad_scale, std::optional<mlir::MlirOp> found_inf, mlir::ElementType param_dtype, mlir::ElementType grad_dtype, mlir::ElementType state_sum_dtype)` — [`L182`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L182) — Builds StableHLO MLIR computation graph for a single param Adagrad step.
- <a id="CastOneParamOutputs"></a>`CastOneParamOutputs(OneParamResult res, mlir::ElementType param_dtype, mlir::ElementType grad_dtype, mlir::ElementType state_sum_dtype)` — [`L162`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L162) — Casts param, grad, and state sum MLIR ops back to target element types.
- <a id="CombineAdagradResults"></a>`CombineAdagradResults(const std::vector<mlir::MlirOp>& params, const std::vector<mlir::MlirOp>& grads, const std::vector<mlir::MlirOp>& state_sums, const size_t num_tensors, const GradScaleMode grad_scale_mode)` — [`L337`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L337) — Combines param, grad, and state sum results into a flat MLIR op vector.
- `CombineAdagradResults(const std::vector<mlir::MlirOp>& params, const std::vector<mlir::MlirOp>& grads, const std::vector<mlir::MlirOp>& state_sums, const size_t num_tensors, const GradScaleMode grad_scale_mode)` — [`L337`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L337) — Combines param, grad, and state sum results into a flat MLIR op vector.
- <a id="DispatchAdagrad"></a>`DispatchAdagrad(at::TensorList self, at::TensorList grads, at::TensorList state_sums, at::TensorList state_steps, const at::Tensor& lr_tensor, const at::Tensor& lr_decay_tensor, const at::Tensor& weight_decay_tensor, const at::Tensor& eps_tensor, const AdagradObjectiveMode maximize_mode, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf, OpParamCacheKeys param_keys)` — [`L482`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L482) — Dispatches fused Adagrad computation graph to TPU device for execution.
- <a id="ExtractAdagradDtypes"></a>`ExtractAdagradDtypes(absl::Span<const mlir::ElementType> out_dtypes, const size_t num_tensors, const GradScaleMode grad_scale_mode)` — [`L320`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L320) — Extracts parameter, gradient, and state sum element types from output dtypes.
- <a id="ExtractAdagradInputs"></a>`ExtractAdagradInputs(absl::Span<mlir::MlirOp> inputs, const size_t num_tensors, const GradScaleMode grad_scale_mode, const FoundInfMode found_inf_mode)` — [`L282`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L282) — Extracts and slices individual input MLIR operands from the flat input span.
- `GatherAdagradInputs(at::TensorList self, at::TensorList grads, at::TensorList state_sums, at::TensorList state_steps, const at::Tensor& lr, const at::Tensor& lr_decay, const at::Tensor& weight_decay, const at::Tensor& eps, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf, const GradScaleMode grad_scale_mode, const FoundInfMode found_inf_mode)` — [`L396`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L396) — Flattens param, grad, state tensors, and scalars into one input vector.
- <a id="GatherAdagradInputs"></a>`GatherAdagradInputs(at::TensorList self, at::TensorList grads, at::TensorList state_sums, at::TensorList state_steps, const at::Tensor& lr, const at::Tensor& lr_decay, const at::Tensor& weight_decay, const at::Tensor& eps, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf, const GradScaleMode grad_scale_mode, const FoundInfMode found_inf_mode)` — [`L396`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L396) — Flattens param, grad, state tensors, and scalars into one input vector.
- `GatherAdagradOutDims(at::TensorList self, at::TensorList grads, at::TensorList state_sums, const GradScaleMode grad_scale_mode)` — [`L448`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L448) — Gathers output shape dimensions for updated params, grads, and states.
- <a id="GatherAdagradOutDims"></a>`GatherAdagradOutDims(at::TensorList self, at::TensorList grads, at::TensorList state_sums, const GradScaleMode grad_scale_mode)` — [`L448`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L448) — Gathers output shape dimensions for updated params, grads, and states.
- <a id="GatherAdagradOutDtypes"></a>`GatherAdagradOutDtypes(at::TensorList self, at::TensorList grads, at::TensorList state_sums, const GradScaleMode grad_scale_mode)` — [`L431`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L431) — Gathers MLIR output element types for updated params, grads, and states.
- `GatherAdagradOutDtypes(at::TensorList self, at::TensorList grads, at::TensorList state_sums, const GradScaleMode grad_scale_mode)` — [`L431`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L431) — Gathers MLIR output element types for updated params, grads, and states.
- <a id="GetFoundInfMode"></a>`GetFoundInfMode(const std::optional<at::Tensor>& found_inf)` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L65) — Determines whether inf/nan check is enabled from the optional tensor.
- <a id="GetGradScaleMode"></a>`GetGradScaleMode(const std::optional<at::Tensor>& grad_scale)` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L58) — Determines whether gradient scaling is enabled from the optional tensor.
- <a id="MetaFusedAdagrad"></a>`MetaFusedAdagrad(at::TensorList /*self*/, at::TensorList /*grads*/, at::TensorList /*state_sums*/, at::TensorList /*state_steps*/, double /*lr*/, double /*lr_decay*/, double /*weight_decay*/, double /*eps*/, bool /*maximize*/, const std::optional<at::Tensor>& /*grad_scale*/, const std::optional<at::Tensor>& /*found_inf*/)` — [`L628`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L628) — Meta kernel for in-place `aten::_fused_adagrad_` (scalar `double lr`
- <a id="MetaFusedAdagradFunctional"></a>`MetaFusedAdagradFunctional(at::TensorList self, at::TensorList grads, at::TensorList state_sums, at::TensorList state_steps, double /*lr*/, double /*lr_decay*/, double /*weight_decay*/, double /*eps*/, bool /*maximize*/, const std::optional<at::Tensor>& /*grad_scale*/, const std::optional<at::Tensor>& /*found_inf*/)` — [`L656`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L656) — Meta kernel for out-of-place functional `aten::_fused_adagrad` (scalar
- <a id="MetaFusedAdagradFunctionalTensorLr"></a>`MetaFusedAdagradFunctionalTensorLr(at::TensorList self, at::TensorList grads, at::TensorList state_sums, at::TensorList /*state_steps*/, const at::Tensor& /*lr*/, double /*lr_decay*/, double /*weight_decay*/, double /*eps*/, bool /*maximize*/, const std::optional<at::Tensor>& /*grad_scale*/, const std::optional<at::Tensor>& /*found_inf*/)` — [`L683`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L683) — Meta kernel for out-of-place functional `aten::_fused_adagrad.tensor_lr`
- <a id="MetaFusedAdagradTensorLr"></a>`MetaFusedAdagradTensorLr(at::TensorList /*self*/, at::TensorList /*grads*/, at::TensorList /*state_sums*/, at::TensorList /*state_steps*/, const at::Tensor& /*lr*/, double /*lr_decay*/, double /*weight_decay*/, double /*eps*/, bool /*maximize*/, const std::optional<at::Tensor>& /*grad_scale*/, const std::optional<at::Tensor>& /*found_inf*/)` — [`L641`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L641) — Meta kernel for in-place `aten::_fused_adagrad_.tensor_lr` (`const
- <a id="SetAdagradParamCacheKeys"></a>`SetAdagradParamCacheKeys(OpParamCacheKeys& param_keys, const GradScaleMode grad_scale_mode, const FoundInfMode found_inf_mode)` — [`L87`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L87) — Records gradient scaling and inf check flags into operation cache keys.
- <a id="ValidateAdagradTensorListSizes"></a>`ValidateAdagradTensorListSizes(at::TensorList self, at::TensorList grads, at::TensorList state_sums, at::TensorList state_steps)` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adagrad/fused_adagrad_aten_kernels.cc#L72) — Validates that param, grad, state sum, and step lists have matching sizes.

