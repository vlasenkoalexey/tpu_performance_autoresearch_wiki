---
title: 'Module: csrc/ops/logit/logit_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/logit/logit_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenLogitBackwardGradInput: AtenLogitBackwardGradInput(367f1a5cacc26e43).
  AtenLogit_: AtenLogit_(9d6da4eb6d66dcf6).
  AtenLogitOut: AtenLogitOut(b2538f284f8591c9).
  AtenLogit: AtenLogit(b4600284377b2f0a).
  DispatchLogit: '`$anonymous_namespace_csrc/ops/logit/logit_aten_kernels.cc`/DispatchLogit(4ee3cad408ecc558).'
  ValidateLogitInputs: '`$anonymous_namespace_csrc/ops/logit/logit_aten_kernels.cc`/ValidateLogitInputs(fd0458bfc68bb174).'
  BuildLogitShlo: '`$anonymous_namespace_csrc/ops/logit/logit_aten_kernels.cc`/BuildLogitShlo(4e058530975e9b5a).'
  BuildLogitBackwardShlo: '`$anonymous_namespace_csrc/ops/logit/logit_aten_kernels.cc`/BuildLogitBackwardShlo(6949d37ea308da71).'
  BuildLogitBufferOut: '`$anonymous_namespace_csrc/ops/logit/logit_aten_kernels.cc`/BuildLogitBufferOut(3d6b34d1266a48f).'
  BuildLogitBuffer: '`$anonymous_namespace_csrc/ops/logit/logit_aten_kernels.cc`/BuildLogitBuffer(2d68812d3c375e55).'
---
# Module: [`csrc/ops/logit/logit_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/logit/logit_aten_kernels.cc)

## Functions
- <a id="AtenLogit"></a>`AtenLogit(const at::Tensor& self, std::optional<double> eps)` — [`L257`](../../../../../../../raw/code/torch_tpu/csrc/ops/logit/logit_aten_kernels.cc#L257)
- <a id="AtenLogitBackwardGradInput"></a>`AtenLogitBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, std::optional<double> eps, at::Tensor& grad_input)` — [`L291`](../../../../../../../raw/code/torch_tpu/csrc/ops/logit/logit_aten_kernels.cc#L291)
- <a id="AtenLogitOut"></a>`AtenLogitOut(const at::Tensor& self, std::optional<double> eps, at::Tensor& out)` — [`L269`](../../../../../../../raw/code/torch_tpu/csrc/ops/logit/logit_aten_kernels.cc#L269)
- <a id="AtenLogit_"></a>`AtenLogit_(at::Tensor& self, std::optional<double> eps)` — [`L280`](../../../../../../../raw/code/torch_tpu/csrc/ops/logit/logit_aten_kernels.cc#L280)
- <a id="BuildLogitBackwardShlo"></a>`BuildLogitBackwardShlo(mlir::MlirOp grad_output_op, mlir::MlirOp self_op, mlir::MlirOp eps_op, mlir::ElementType output_dtype)` — [`L175`](../../../../../../../raw/code/torch_tpu/csrc/ops/logit/logit_aten_kernels.cc#L175)
- <a id="BuildLogitBuffer"></a>`BuildLogitBuffer(const at::Tensor& self, PromotedScalar& promoted_eps, c10::ScalarType out_type, OpParamCacheKeys param_keys)` — [`L150`](../../../../../../../raw/code/torch_tpu/csrc/ops/logit/logit_aten_kernels.cc#L150)
- <a id="BuildLogitBufferOut"></a>`BuildLogitBufferOut(const at::Tensor& self, PromotedScalar& promoted_eps, c10::ScalarType out_type, OpParamCacheKeys param_keys, at::Tensor& out)` — [`L162`](../../../../../../../raw/code/torch_tpu/csrc/ops/logit/logit_aten_kernels.cc#L162)
- <a id="BuildLogitShlo"></a>`BuildLogitShlo(mlir::MlirOp input_op, mlir::MlirOp eps_op, mlir::ElementType output_dtype)` — [`L52`](../../../../../../../raw/code/torch_tpu/csrc/ops/logit/logit_aten_kernels.cc#L52)
- <a id="DispatchLogit"></a>`DispatchLogit(const at::Tensor& self, PromotedScalar& promoted_eps, c10::ScalarType out_type, OpParamCacheKeys param_keys, DispatchFn&& dispatch_fn)` — [`L125`](../../../../../../../raw/code/torch_tpu/csrc/ops/logit/logit_aten_kernels.cc#L125)
- <a id="ValidateLogitInputs"></a>`ValidateLogitInputs(const at::Tensor& self)` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/ops/logit/logit_aten_kernels.cc#L116)

