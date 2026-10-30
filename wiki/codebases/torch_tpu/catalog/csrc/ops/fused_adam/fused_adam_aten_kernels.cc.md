---
title: 'Module: csrc/ops/fused_adam/fused_adam_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/fused_adam/fused_adam_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenFusedAdam: AtenFusedAdam(5ac859cf6a16af3b).
  AtenFusedAdamTensorLr: AtenFusedAdamTensorLr(300f86fac5f931ab).
  BuildAdamShlo: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/BuildAdamShlo(56b4e6183c195992).'
  DispatchAdam: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/DispatchAdam(9d4ebbdf5ed1fd7f).'
  BuildAdamStepForOneParam: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/BuildAdamStepForOneParam(3c8df2de4bfc3312).'
  ValidateAdamTensorListSizes: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/ValidateAdamTensorListSizes(6bf841c21918f5f4).'
  ComputeIsInfPredicate: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/ComputeIsInfPredicate(893863f55dcdb48).'
  AssignBuffers: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AssignBuffers(68f0efce82a960d6).'
  ApplyFoundInfRevert: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/ApplyFoundInfRevert(f4051a843839b493).'
  AppendDtypes: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AppendDtypes(9449544dff2f41b4).'
  CastOneParamOutputs: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/CastOneParamOutputs(ca9427e72046663f).'
  ExtractAdamInputs: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/ExtractAdamInputs(3b3a7420e4252058).'
  PopulateAdamOutputs: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/PopulateAdamOutputs(c86aa5599d752499).'
  ExtractAdamDtypes: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/ExtractAdamDtypes(c96c32f9d5088239).'
  OneParamResult.grad: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/OneParamResult#grad.'
  MetaFusedAdamTensorLr: MetaFusedAdamTensorLr(300f86fac5f931ab).
  OneParamResult.max_exp_avg_sq: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/OneParamResult#max_exp_avg_sq.'
  MetaFusedAdamFunctionalTensorLr: MetaFusedAdamFunctionalTensorLr(a89ff47144dc65c0).
  EmptyLikeTensorList: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/EmptyLikeTensorList(a1d00ea8057e3cd3).'
  OneParamResult.exp_avg: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/OneParamResult#exp_avg.'
  ReshapeOptionalScalarTo0DIfNeeded: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/ReshapeOptionalScalarTo0DIfNeeded(3c93b0f27468deb).'
  OneParamResult.param: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/OneParamResult#param.'
  OneParamResult.exp_avg_sq: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/OneParamResult#exp_avg_sq.'
  ReshapeScalarTo0DIfNeeded: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/ReshapeScalarTo0DIfNeeded(cf97982c188f832c).'
  OneParamResult: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/OneParamResult#'
  MetaFusedAdamFunctional: MetaFusedAdamFunctional(6f5f11ef1dee124e).
  AdamDtypeSpans: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamDtypeSpans#'
  AdamInputSpans: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#'
  AdamInputSpans.steps: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#steps.'
  AppendDims: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AppendDims(3fd35b192ff1f29).'
  AdamDtypeSpans.exp_avgs: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamDtypeSpans#exp_avgs.'
  AdamInputSpans.grads: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#grads.'
  AdamDtypeSpans.params: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamDtypeSpans#params.'
  AdamDtypeSpans.exp_avg_sqs: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamDtypeSpans#exp_avg_sqs.'
  AdamDtypeSpans.grads: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamDtypeSpans#grads.'
  AdamInputSpans.exp_avg_sqs: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#exp_avg_sqs.'
  AdamInputSpans.exp_avgs: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#exp_avgs.'
  AdamInputSpans.params: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#params.'
  AdamInputSpans.grad_scale: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#grad_scale.'
  AdamInputSpans.max_exp_avg_sqs: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#max_exp_avg_sqs.'
  AdamInputSpans.weight_decay: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#weight_decay.'
  AdamInputSpans.beta1: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#beta1.'
  AdamInputSpans.eps: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#eps.'
  AdamInputSpans.beta2: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#beta2.'
  AdamInputSpans.lr: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#lr.'
  AdamInputSpans.found_inf: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamInputSpans#found_inf.'
  BuildAdamDonatedIndices: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/BuildAdamDonatedIndices(7ec692e3e5f4feac).'
  AdamDtypeSpans.max_exp_avg_sqs: '`$anonymous_namespace_csrc/ops/fused_adam/fused_adam_aten_kernels.cc`/AdamDtypeSpans#max_exp_avg_sqs.'
---
# Module: [`csrc/ops/fused_adam/fused_adam_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc)

## Classes
### <a id="AdamDtypeSpans"></a>`AdamDtypeSpans`
- def: [`csrc/ops/fused_adam/fused_adam_aten_kernels.cc:403`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L403)
- signature: `struct AdamDtypeSpans`
- members:
  - <a id="AdamDtypeSpans.exp_avg_sqs"></a>`exp_avg_sqs` — [`L407`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L407)
  - <a id="AdamDtypeSpans.exp_avgs"></a>`exp_avgs` — [`L406`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L406)
  - <a id="AdamDtypeSpans.grads"></a>`grads` — [`L405`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L405)
  - <a id="AdamDtypeSpans.max_exp_avg_sqs"></a>`max_exp_avg_sqs` — [`L408`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L408)
  - <a id="AdamDtypeSpans.params"></a>`params` — [`L404`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L404)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildAdamShlo`](fused_adam_aten_kernels.cc.md#BuildAdamShlo), [`ExtractAdamDtypes`](fused_adam_aten_kernels.cc.md#ExtractAdamDtypes)

### <a id="AdamInputSpans"></a>`AdamInputSpans`
- def: [`csrc/ops/fused_adam/fused_adam_aten_kernels.cc:352`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L352)
- signature: `struct AdamInputSpans`
- members:
  - <a id="AdamInputSpans.beta1"></a>`beta1` — [`L360`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L360)
  - <a id="AdamInputSpans.beta2"></a>`beta2` — [`L361`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L361)
  - <a id="AdamInputSpans.eps"></a>`eps` — [`L363`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L363)
  - <a id="AdamInputSpans.exp_avg_sqs"></a>`exp_avg_sqs` — [`L356`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L356)
  - <a id="AdamInputSpans.exp_avgs"></a>`exp_avgs` — [`L355`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L355)
  - <a id="AdamInputSpans.found_inf"></a>`found_inf` — [`L365`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L365)
  - <a id="AdamInputSpans.grad_scale"></a>`grad_scale` — [`L364`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L364)
  - <a id="AdamInputSpans.grads"></a>`grads` — [`L354`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L354)
  - <a id="AdamInputSpans.lr"></a>`lr` — [`L359`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L359)
  - <a id="AdamInputSpans.max_exp_avg_sqs"></a>`max_exp_avg_sqs` — [`L358`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L358)
  - <a id="AdamInputSpans.params"></a>`params` — [`L353`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L353)
  - <a id="AdamInputSpans.steps"></a>`steps` — [`L357`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L357)
  - <a id="AdamInputSpans.weight_decay"></a>`weight_decay` — [`L362`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L362)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildAdamShlo`](fused_adam_aten_kernels.cc.md#BuildAdamShlo), [`ExtractAdamInputs`](fused_adam_aten_kernels.cc.md#ExtractAdamInputs)

### <a id="OneParamResult"></a>`OneParamResult`
- def: [`csrc/ops/fused_adam/fused_adam_aten_kernels.cc:82`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L82)
- signature: `struct OneParamResult`
- members:
  - <a id="OneParamResult.exp_avg"></a>`exp_avg` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L85)
  - <a id="OneParamResult.exp_avg_sq"></a>`exp_avg_sq` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L86)
  - <a id="OneParamResult.grad"></a>`grad` — [`L84`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L84)
  - <a id="OneParamResult.max_exp_avg_sq"></a>`max_exp_avg_sq` — [`L87`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L87)
  - <a id="OneParamResult.param"></a>`param` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L83)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildAdamShlo`](fused_adam_aten_kernels.cc.md#BuildAdamShlo), [`BuildAdamStepForOneParam`](fused_adam_aten_kernels.cc.md#BuildAdamStepForOneParam), [`ComputeIsInfPredicate`](fused_adam_aten_kernels.cc.md#ComputeIsInfPredicate), [`ApplyFoundInfRevert`](fused_adam_aten_kernels.cc.md#ApplyFoundInfRevert), [`CastOneParamOutputs`](fused_adam_aten_kernels.cc.md#CastOneParamOutputs)

## Functions
- <a id="AppendDims"></a>`AppendDims(const at::TensorList tensors, std::vector<absl::Span<const int64_t>>& out_dims)` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L74) — Appends dimension spans of input tensors to the output dimension vector.
- `AppendDims(const at::TensorList tensors, std::vector<absl::Span<const int64_t>>& out_dims)` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L74) — Appends dimension spans of input tensors to the output dimension vector.
- <a id="AppendDtypes"></a>`AppendDtypes(const at::TensorList tensors, std::vector<mlir::ElementType>& out_dtypes)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L63) — Appends converted MLIR element types of input tensors to the output vector.
- `AppendDtypes(const at::TensorList tensors, std::vector<mlir::ElementType>& out_dtypes)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L63) — Appends converted MLIR element types of input tensors to the output vector.
- <a id="ApplyFoundInfRevert"></a>`ApplyFoundInfRevert(OneParamResult current, mlir::MlirOp param_old, mlir::MlirOp grad_old, mlir::MlirOp exp_avg_old, mlir::MlirOp exp_avg_sq_old, std::optional<mlir::MlirOp> max_exp_avg_sq_old, mlir::MlirOp is_inf, const bool amsgrad)` — [`L133`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L133) — Conditionally reverts parameter, gradient, and moment tensors to pre-step
- `AssignBuffers(std::vector<DeviceBufferRef>& buffers, const size_t offset, const at::TensorList tensors)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L54) — Assigns compiled output device buffers to input tensors starting at offset.
- <a id="AssignBuffers"></a>`AssignBuffers(std::vector<DeviceBufferRef>& buffers, const size_t offset, const at::TensorList tensors)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L54) — Assigns compiled output device buffers to input tensors starting at offset.
- <a id="AtenFusedAdam"></a>`AtenFusedAdam(at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs, at::TensorList state_steps, const double lr, const double beta1, const double beta2, const double weight_decay, const double eps, const bool amsgrad, const bool maximize, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf)` — [`L690`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L690) — Promote scalar hyperparameters to standard eager tensors and validate input — documented in [fused-optimizer-kernels](../../../../concepts/fused-optimizer-kernels.md)
- <a id="AtenFusedAdamTensorLr"></a>`AtenFusedAdamTensorLr(at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs, at::TensorList state_steps, const at::Tensor& lr, const double beta1, const double beta2, const double weight_decay, const double eps, const bool amsgrad, const bool maximize, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf)` — [`L741`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L741) — Promote scalar hyperparameters to standard eager tensors and validate input — documented in [fused-optimizer-kernels](../../../../concepts/fused-optimizer-kernels.md)
- <a id="BuildAdamDonatedIndices"></a>`BuildAdamDonatedIndices(size_t num_tensors, bool amsgrad, bool has_grad_scale)` — [`L527`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L527)
- `BuildAdamShlo(absl::Span<mlir::MlirOp> inputs, const size_t num_tensors, const AdamStepConfig& config, absl::Span<const mlir::ElementType> out_dtypes)` — [`L439`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L439) — Iterates across all multi-tensor optimizer lists and generates the combined
- <a id="BuildAdamShlo"></a>`BuildAdamShlo(absl::Span<mlir::MlirOp> inputs, const size_t num_tensors, const AdamStepConfig& config, absl::Span<const mlir::ElementType> out_dtypes)` — [`L439`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L439) — Iterates across all multi-tensor optimizer lists and generates the combined
- <a id="BuildAdamStepForOneParam"></a>`BuildAdamStepForOneParam(mlir::MlirOp param, mlir::MlirOp grad, mlir::MlirOp exp_avg, mlir::MlirOp exp_avg_sq, std::optional<mlir::MlirOp> max_exp_avg_sq, mlir::MlirOp step, mlir::MlirOp lr, mlir::MlirOp beta1, mlir::MlirOp beta2, mlir::MlirOp weight_decay, mlir::MlirOp eps, const AdamAmsgradMode amsgrad_mode, const AdamObjectiveMode maximize_mode, std::optional<mlir::MlirOp> grad_scale, std::optional<mlir::MlirOp> is_inf, mlir::ElementType param_dtype, std::optional<mlir::ElementType> grad_dtype, mlir::ElementType exp_avg_dtype, mlir::ElementType exp_avg_sq_dtype, std::optional<mlir::ElementType> max_exp_avg_sq_dtype)` — [`L208`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L208) — Builds the StableHLO graph for updating a single parameter tensor and its
- <a id="CastOneParamOutputs"></a>`CastOneParamOutputs(OneParamResult res, mlir::ElementType param_dtype, std::optional<mlir::ElementType> grad_dtype, mlir::ElementType exp_avg_dtype, mlir::ElementType exp_avg_sq_dtype, std::optional<mlir::ElementType> max_exp_avg_sq_dtype, const bool amsgrad)` — [`L172`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L172) — Casts computed intermediate ops back to their respective target output buffer
- <a id="ComputeIsInfPredicate"></a>`ComputeIsInfPredicate(const std::optional<mlir::MlirOp>& found_inf)` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L109) — Computes a boolean Inf/NaN predicate tensor from an optional found_inf input
- <a id="DispatchAdam"></a>`DispatchAdam(at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs, at::TensorList state_steps, const at::Tensor& lr_tensor, const at::Tensor& beta1_tensor, const at::Tensor& beta2_tensor, const at::Tensor& weight_decay_tensor, const at::Tensor& eps_tensor, const AdamAmsgradMode amsgrad_mode, const AdamObjectiveMode maximize_mode, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf, OpParamCacheKeys param_keys)` — [`L583`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L583) — Orchestrates eager execution: validates multi-tensor list sizes and
- <a id="EmptyLikeTensorList"></a>`EmptyLikeTensorList(at::TensorList tensors)` — [`L789`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L789)
- `EmptyLikeTensorList(at::TensorList tensors)` — [`L789`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L789)
- <a id="ExtractAdamDtypes"></a>`ExtractAdamDtypes(absl::Span<const mlir::ElementType> out_dtypes, const size_t num_tensors, const AdamStepConfig& config)` — [`L413`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L413) — Slices flat output dtype span into individual element type spans for each
- <a id="ExtractAdamInputs"></a>`ExtractAdamInputs(absl::Span<mlir::MlirOp> inputs, const size_t num_tensors, const AdamStepConfig& config)` — [`L370`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L370) — Slices flat input op span into parameter lists, states, and optional
- <a id="MetaFusedAdamFunctional"></a>`MetaFusedAdamFunctional(at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs, at::TensorList /*state_steps*/, double /*lr*/, double /*beta1*/, double /*beta2*/, double /*weight_decay*/, double /*eps*/, bool /*amsgrad*/, bool /*maximize*/, const std::optional<at::Tensor>& /*grad_scale*/, const std::optional<at::Tensor>& /*found_inf*/)` — [`L827`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L827) — Meta kernel for out-of-place functional `aten::_fused_adamw` (scalar `double
- <a id="MetaFusedAdamFunctionalTensorLr"></a>`MetaFusedAdamFunctionalTensorLr(at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs, at::TensorList /*state_steps*/, const at::Tensor& /*lr*/, double /*beta1*/, double /*beta2*/, double /*weight_decay*/, double /*eps*/, bool /*amsgrad*/, bool /*maximize*/, const std::optional<at::Tensor>& /*grad_scale*/, const std::optional<at::Tensor>& /*found_inf*/)` — [`L849`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L849) — Meta kernel for out-of-place functional `aten::_fused_adam.tensor_lr` and
- <a id="MetaFusedAdamTensorLr"></a>`MetaFusedAdamTensorLr(at::TensorList /*self*/, at::TensorList /*grads*/, at::TensorList /*exp_avgs*/, at::TensorList /*exp_avg_sqs*/, at::TensorList /*max_exp_avg_sqs*/, at::TensorList /*state_steps*/, const at::Tensor& /*lr*/, double /*beta1*/, double /*beta2*/, double /*weight_decay*/, double /*eps*/, bool /*amsgrad*/, bool /*maximize*/, const std::optional<at::Tensor>& /*grad_scale*/, const std::optional<at::Tensor>& /*found_inf*/)` — [`L808`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L808) — Meta kernel for in-place `aten::_fused_adam_.tensor_lr` and
- <a id="PopulateAdamOutputs"></a>`PopulateAdamOutputs(at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs, bool amsgrad, bool has_grad_scale, size_t num_tensors, std::vector<mlir::ElementType>& out_dtypes, std::vector<absl::Span<const int64_t>>& out_dims_list)` — [`L553`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L553)
- `PopulateAdamOutputs(at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs, bool amsgrad, bool has_grad_scale, size_t num_tensors, std::vector<mlir::ElementType>& out_dtypes, std::vector<absl::Span<const int64_t>>& out_dims_list)` — [`L553`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L553)
- <a id="ReshapeOptionalScalarTo0DIfNeeded"></a>`ReshapeOptionalScalarTo0DIfNeeded(std::optional<mlir::MlirOp>& op)` — [`L101`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L101) — Reshapes an optional scalar MLIR operation to a 0-D tensor if defined and its
- <a id="ReshapeScalarTo0DIfNeeded"></a>`ReshapeScalarTo0DIfNeeded(mlir::MlirOp op)` — [`L92`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L92) — Reshapes a scalar MLIR operation to a 0-D tensor if its rank is greater than
- <a id="ValidateAdamTensorListSizes"></a>`ValidateAdamTensorListSizes(at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs, at::TensorList state_steps, const bool amsgrad)` — [`L499`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.cc#L499) — Validates that all input tensor state lists have matching lengths,

