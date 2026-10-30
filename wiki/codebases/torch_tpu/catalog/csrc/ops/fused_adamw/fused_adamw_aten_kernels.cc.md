---
title: 'Module: csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenFusedAdamw: AtenFusedAdamw(5ac859cf6a16af3b).
  AtenFusedAdamwTensorLr: AtenFusedAdamwTensorLr(300f86fac5f931ab).
  BuildAdamwShlo: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/BuildAdamwShlo(6442ff49bb6409d6).'
  DispatchAdamw: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/DispatchAdamw(66204d535acefcf3).'
  BuildAdamwStepForOneParam: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/BuildAdamwStepForOneParam(92ab384fd5a1d7a9).'
  ValidateAdamwTensorListSizes: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/ValidateAdamwTensorListSizes(6bf841c21918f5f4).'
  ApplyFoundInfRevert: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/ApplyFoundInfRevert(35884fdb084bbdf1).'
  AssignBuffers: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AssignBuffers(2d951a6487e63a37).'
  AppendDtypes: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AppendDtypes(9449544dff2f41b4).'
  CastOneParamOutputs: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/CastOneParamOutputs(af226c4142650130).'
  OneParamResult.max_exp_avg_sq: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/OneParamResult#max_exp_avg_sq.'
  OneParamResult.grad: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/OneParamResult#grad.'
  AssignAdamwBuffers: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AssignAdamwBuffers(6e76845e84f33dc2).'
  AppendDims: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AppendDims(3fd35b192ff1f29).'
  OneParamResult.param: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/OneParamResult#param.'
  OneParamResult.exp_avg: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/OneParamResult#exp_avg.'
  OneParamResult.exp_avg_sq: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/OneParamResult#exp_avg_sq.'
  OneParamResult: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/OneParamResult#'
  ExtractAdamwDtypes: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/ExtractAdamwDtypes(e2a14aca8734c3e6).'
  ExtractAdamwInputs: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/ExtractAdamwInputs(9b2704dcbe04dafa).'
  AdamwInputSpans: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#'
  AdamwDtypeSpans: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwDtypeSpans#'
  AdamwInputSpans.grads: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#grads.'
  AdamwDtypeSpans.exp_avg_sqs: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwDtypeSpans#exp_avg_sqs.'
  AdamwInputSpans.exp_avg_sqs: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#exp_avg_sqs.'
  AdamwDtypeSpans.params: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwDtypeSpans#params.'
  AdamwInputSpans.exp_avgs: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#exp_avgs.'
  AdamwDtypeSpans.exp_avgs: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwDtypeSpans#exp_avgs.'
  AdamwInputSpans.params: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#params.'
  AdamwInputSpans.steps: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#steps.'
  AdamwDtypeSpans.grads: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwDtypeSpans#grads.'
  CombineAdamwResults: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/CombineAdamwResults(2a3a24978abc765f).'
  AdamwInputSpans.grad_scale: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#grad_scale.'
  AdamwInputSpans.lr: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#lr.'
  AdamwInputSpans.weight_decay: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#weight_decay.'
  AdamwInputSpans.beta2: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#beta2.'
  AdamwInputSpans.max_exp_avg_sqs: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#max_exp_avg_sqs.'
  AdamwInputSpans.beta1: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#beta1.'
  AdamwInputSpans.found_inf: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#found_inf.'
  AdamwDtypeSpans.max_exp_avg_sqs: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwDtypeSpans#max_exp_avg_sqs.'
  ComputeAdamwDonatedIndices: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/ComputeAdamwDonatedIndices(7ec692e3e5f4feac).'
  AdamwInputSpans.eps: '`$anonymous_namespace_csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`/AdamwInputSpans#eps.'
---
# Module: [`csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc)

## Classes
### <a id="AdamwDtypeSpans"></a>`AdamwDtypeSpans`
- def: [`csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc:366`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L366)
- signature: `struct AdamwDtypeSpans`
- members:
  - <a id="AdamwDtypeSpans.exp_avg_sqs"></a>`exp_avg_sqs` — [`L370`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L370)
  - <a id="AdamwDtypeSpans.exp_avgs"></a>`exp_avgs` — [`L369`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L369)
  - <a id="AdamwDtypeSpans.grads"></a>`grads` — [`L368`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L368)
  - <a id="AdamwDtypeSpans.max_exp_avg_sqs"></a>`max_exp_avg_sqs` — [`L371`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L371)
  - <a id="AdamwDtypeSpans.params"></a>`params` — [`L367`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L367)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildAdamwShlo`](fused_adamw_aten_kernels.cc.md#BuildAdamwShlo), [`ExtractAdamwDtypes`](fused_adamw_aten_kernels.cc.md#ExtractAdamwDtypes)

### <a id="AdamwInputSpans"></a>`AdamwInputSpans`
- def: [`csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc:314`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L314)
- signature: `struct AdamwInputSpans`
- members:
  - <a id="AdamwInputSpans.beta1"></a>`beta1` — [`L322`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L322)
  - <a id="AdamwInputSpans.beta2"></a>`beta2` — [`L323`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L323)
  - <a id="AdamwInputSpans.eps"></a>`eps` — [`L325`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L325)
  - <a id="AdamwInputSpans.exp_avg_sqs"></a>`exp_avg_sqs` — [`L318`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L318)
  - <a id="AdamwInputSpans.exp_avgs"></a>`exp_avgs` — [`L317`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L317)
  - <a id="AdamwInputSpans.found_inf"></a>`found_inf` — [`L327`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L327)
  - <a id="AdamwInputSpans.grad_scale"></a>`grad_scale` — [`L326`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L326)
  - <a id="AdamwInputSpans.grads"></a>`grads` — [`L316`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L316)
  - <a id="AdamwInputSpans.lr"></a>`lr` — [`L321`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L321)
  - <a id="AdamwInputSpans.max_exp_avg_sqs"></a>`max_exp_avg_sqs` — [`L320`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L320)
  - <a id="AdamwInputSpans.params"></a>`params` — [`L315`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L315)
  - <a id="AdamwInputSpans.steps"></a>`steps` — [`L319`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L319)
  - <a id="AdamwInputSpans.weight_decay"></a>`weight_decay` — [`L324`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L324)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildAdamwShlo`](fused_adamw_aten_kernels.cc.md#BuildAdamwShlo), [`ExtractAdamwInputs`](fused_adamw_aten_kernels.cc.md#ExtractAdamwInputs)

### <a id="OneParamResult"></a>`OneParamResult`
- def: [`csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc:81`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L81)
- signature: `struct OneParamResult`
- members:
  - <a id="OneParamResult.exp_avg"></a>`exp_avg` — [`L84`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L84)
  - <a id="OneParamResult.exp_avg_sq"></a>`exp_avg_sq` — [`L85`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L85)
  - <a id="OneParamResult.grad"></a>`grad` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L83)
  - <a id="OneParamResult.max_exp_avg_sq"></a>`max_exp_avg_sq` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L86)
  - <a id="OneParamResult.param"></a>`param` — [`L82`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L82)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildAdamwShlo`](fused_adamw_aten_kernels.cc.md#BuildAdamwShlo), [`BuildAdamwStepForOneParam`](fused_adamw_aten_kernels.cc.md#BuildAdamwStepForOneParam), [`ApplyFoundInfRevert`](fused_adamw_aten_kernels.cc.md#ApplyFoundInfRevert), [`CastOneParamOutputs`](fused_adamw_aten_kernels.cc.md#CastOneParamOutputs)

## Functions
- `AppendDims(const at::TensorList tensors, std::vector<absl::Span<const int64_t>>& out_dims)` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L73) — Appends dimension spans of input tensors to the output dimension vector.
- <a id="AppendDims"></a>`AppendDims(const at::TensorList tensors, std::vector<absl::Span<const int64_t>>& out_dims)` — [`L73`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L73) — Appends dimension spans of input tensors to the output dimension vector.
- <a id="AppendDtypes"></a>`AppendDtypes(const at::TensorList tensors, std::vector<mlir::ElementType>& out_dtypes)` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L62) — Appends converted MLIR element types of input tensors to the output vector.
- `AppendDtypes(const at::TensorList tensors, std::vector<mlir::ElementType>& out_dtypes)` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L62) — Appends converted MLIR element types of input tensors to the output vector.
- <a id="ApplyFoundInfRevert"></a>`ApplyFoundInfRevert(OneParamResult current, mlir::MlirOp param_old, mlir::MlirOp grad_old, mlir::MlirOp exp_avg_old, mlir::MlirOp exp_avg_sq_old, std::optional<mlir::MlirOp> max_exp_avg_sq_old, mlir::MlirOp found_inf, mlir::ElementType comp_type, const bool amsgrad)` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L91) — Reverts parameter, gradient, and moment tensors to pre-step values if inf/nan
- `AssignAdamwBuffers(std::vector<DeviceBufferRef>& result_buffers, const size_t num_tensors, const bool amsgrad, const bool has_grad_scale, at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs)` — [`L542`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L542) — Assigns computed output device buffers back in-place to mutated eager
- <a id="AssignAdamwBuffers"></a>`AssignAdamwBuffers(std::vector<DeviceBufferRef>& result_buffers, const size_t num_tensors, const bool amsgrad, const bool has_grad_scale, at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs)` — [`L542`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L542) — Assigns computed output device buffers back in-place to mutated eager
- <a id="AssignBuffers"></a>`AssignBuffers(std::vector<DeviceBufferRef>& buffers, const size_t offset, const at::TensorList tensors)` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L53) — Assigns compiled output device buffers to input tensors starting at offset.
- `AssignBuffers(std::vector<DeviceBufferRef>& buffers, const size_t offset, const at::TensorList tensors)` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L53) — Assigns compiled output device buffers to input tensors starting at offset.
- <a id="AtenFusedAdamw"></a>`AtenFusedAdamw(at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs, at::TensorList state_steps, const double lr, const double beta1, const double beta2, const double weight_decay, const double eps, const bool amsgrad, const bool maximize, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf)` — [`L675`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L675) — Promote scalar hyperparameters to standard eager tensors and validate input — documented in [fused-optimizer-kernels](../../../../concepts/fused-optimizer-kernels.md)
- <a id="AtenFusedAdamwTensorLr"></a>`AtenFusedAdamwTensorLr(at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs, at::TensorList state_steps, const at::Tensor& lr, const double beta1, const double beta2, const double weight_decay, const double eps, const bool amsgrad, const bool maximize, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf)` — [`L725`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L725) — Promote scalar hyperparameters to standard eager tensors and validate input — documented in [fused-optimizer-kernels](../../../../concepts/fused-optimizer-kernels.md)
- `BuildAdamwShlo(absl::Span<mlir::MlirOp> inputs, const size_t num_tensors, const AmsgradMode amsgrad_mode, const ObjectiveMode maximize_mode, const bool has_grad_scale, const bool has_found_inf, absl::Span<const mlir::ElementType> out_dtypes)` — [`L426`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L426) — Iterates across all multi-tensor optimizer lists and generates the combined
- <a id="BuildAdamwShlo"></a>`BuildAdamwShlo(absl::Span<mlir::MlirOp> inputs, const size_t num_tensors, const AmsgradMode amsgrad_mode, const ObjectiveMode maximize_mode, const bool has_grad_scale, const bool has_found_inf, absl::Span<const mlir::ElementType> out_dtypes)` — [`L426`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L426) — Iterates across all multi-tensor optimizer lists and generates the combined
- <a id="BuildAdamwStepForOneParam"></a>`BuildAdamwStepForOneParam(mlir::MlirOp param, mlir::MlirOp grad, mlir::MlirOp exp_avg, mlir::MlirOp exp_avg_sq, std::optional<mlir::MlirOp> max_exp_avg_sq, mlir::MlirOp step, mlir::MlirOp lr, mlir::MlirOp beta1, mlir::MlirOp beta2, mlir::MlirOp weight_decay, mlir::MlirOp eps, const AmsgradMode amsgrad_mode, const ObjectiveMode maximize_mode, std::optional<mlir::MlirOp> grad_scale, std::optional<mlir::MlirOp> found_inf, mlir::ElementType param_dtype, mlir::ElementType grad_dtype, mlir::ElementType exp_avg_dtype, mlir::ElementType exp_avg_sq_dtype, std::optional<mlir::ElementType> max_exp_avg_sq_dtype)` — [`L169`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L169) — Builds the StableHLO graph for updating a single parameter tensor and its
- <a id="CastOneParamOutputs"></a>`CastOneParamOutputs(OneParamResult res, mlir::ElementType param_dtype, mlir::ElementType grad_dtype, mlir::ElementType exp_avg_dtype, mlir::ElementType exp_avg_sq_dtype, std::optional<mlir::ElementType> max_exp_avg_sq_dtype, const bool amsgrad)` — [`L136`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L136) — Casts computed intermediate ops back to their respective target output buffer
- `CombineAdamwResults(const std::vector<mlir::MlirOp>& params, const std::vector<mlir::MlirOp>& grads, const std::vector<mlir::MlirOp>& exp_avgs, const std::vector<mlir::MlirOp>& exp_avg_sqs, const std::vector<mlir::MlirOp>& max_exp_avg_sqs, const size_t num_tensors, const bool amsgrad, const bool has_grad_scale)` — [`L401`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L401) — Concatenates per-tensor updated output vectors into a single flattened MLIR
- <a id="CombineAdamwResults"></a>`CombineAdamwResults(const std::vector<mlir::MlirOp>& params, const std::vector<mlir::MlirOp>& grads, const std::vector<mlir::MlirOp>& exp_avgs, const std::vector<mlir::MlirOp>& exp_avg_sqs, const std::vector<mlir::MlirOp>& max_exp_avg_sqs, const size_t num_tensors, const bool amsgrad, const bool has_grad_scale)` — [`L401`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L401) — Concatenates per-tensor updated output vectors into a single flattened MLIR
- <a id="ComputeAdamwDonatedIndices"></a>`ComputeAdamwDonatedIndices(const size_t num_tensors, const bool amsgrad, const bool has_grad_scale)` — [`L521`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L521) — Selects 0-based argument indices of input tensors to donate to XLA for HBM
- <a id="DispatchAdamw"></a>`DispatchAdamw(at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs, at::TensorList state_steps, const at::Tensor& lr_tensor, const at::Tensor& beta1_tensor, const at::Tensor& beta2_tensor, const at::Tensor& weight_decay_tensor, const at::Tensor& eps_tensor, const AmsgradMode amsgrad_mode, const ObjectiveMode maximize_mode, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf, OpParamCacheKeys param_keys)` — [`L567`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L567) — Orchestrates eager execution: flattens input tensor lists, configures
- <a id="ExtractAdamwDtypes"></a>`ExtractAdamwDtypes(absl::Span<const mlir::ElementType> out_dtypes, const size_t num_tensors, const bool amsgrad, const bool has_grad_scale)` — [`L376`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L376) — Slices flat output dtype span into individual element type spans for each
- <a id="ExtractAdamwInputs"></a>`ExtractAdamwInputs(absl::Span<mlir::MlirOp> inputs, const size_t num_tensors, const bool amsgrad, const bool has_grad_scale, const bool has_found_inf)` — [`L332`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L332) — Slices flat input op span into parameter lists, states, and optional
- <a id="ValidateAdamwTensorListSizes"></a>`ValidateAdamwTensorListSizes(at::TensorList self, at::TensorList grads, at::TensorList exp_avgs, at::TensorList exp_avg_sqs, at::TensorList max_exp_avg_sqs, at::TensorList state_steps, const bool amsgrad)` — [`L485`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.cc#L485) — Validates that all input tensor state lists have matching lengths.

