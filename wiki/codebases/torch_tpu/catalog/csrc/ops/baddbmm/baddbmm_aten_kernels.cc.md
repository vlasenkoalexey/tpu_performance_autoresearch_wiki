---
title: 'Module: csrc/ops/baddbmm/baddbmm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/baddbmm/baddbmm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenBaddbmmDtype: AtenBaddbmmDtype(6b83f4dd57f2f3b3).
  AtenBaddbmmDtypeOut: AtenBaddbmmDtypeOut(d26884d764022210).
  AtenBaddbmmOut: AtenBaddbmmOut(a07f23bfc1f8200e).
  ValidateBaddbmmInputs: '`$anonymous_namespace_csrc/ops/baddbmm/baddbmm_aten_kernels.cc`/ValidateBaddbmmInputs(6ddad2e2cbb424ad).'
  DispatchBaddbmm: '`$anonymous_namespace_csrc/ops/baddbmm/baddbmm_aten_kernels.cc`/DispatchBaddbmm(4c78c99b58d12717).'
  BuildBaddbmmShlo: '`$anonymous_namespace_csrc/ops/baddbmm/baddbmm_aten_kernels.cc`/BuildBaddbmmShlo(166a7834edff5b4a).'
  ValidateBaddbmmDtypes: '`$anonymous_namespace_csrc/ops/baddbmm/baddbmm_aten_kernels.cc`/ValidateBaddbmmDtypes(18e9f4ef9f9304dc).'
  ValidateBaddbmmOut: '`$anonymous_namespace_csrc/ops/baddbmm/baddbmm_aten_kernels.cc`/ValidateBaddbmmOut(acb502079e74052e).'
  ResolveAndDispatchBaddbmm: '`$anonymous_namespace_csrc/ops/baddbmm/baddbmm_aten_kernels.cc`/ResolveAndDispatchBaddbmm(3c8b5ad0d133d0ff).'
  ResolveAndRunBaddbmm: '`$anonymous_namespace_csrc/ops/baddbmm/baddbmm_aten_kernels.cc`/ResolveAndRunBaddbmm(d4f793e9eefff70e).'
  ResolveAndRunBaddbmmOut: '`$anonymous_namespace_csrc/ops/baddbmm/baddbmm_aten_kernels.cc`/ResolveAndRunBaddbmmOut(3803be0a4d7aa740).'
  GetBaddbmmOpBuilder: '`$anonymous_namespace_csrc/ops/baddbmm/baddbmm_aten_kernels.cc`/GetBaddbmmOpBuilder(f513088ce3a1cb1e).'
  BuildBaddbmmInputs: '`$anonymous_namespace_csrc/ops/baddbmm/baddbmm_aten_kernels.cc`/BuildBaddbmmInputs(3e0c6313c004fa28).'
---
# Module: [`csrc/ops/baddbmm/baddbmm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc)

## Functions
- <a id="AtenBaddbmmDtype"></a>`AtenBaddbmmDtype(const at::Tensor& self, const at::Tensor& batch1, const at::Tensor& batch2, at::ScalarType out_dtype, const at::Scalar& beta, const at::Scalar& alpha)` — [`L319`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L319)
- <a id="AtenBaddbmmDtypeOut"></a>`AtenBaddbmmDtypeOut(const at::Tensor& self, const at::Tensor& batch1, const at::Tensor& batch2, at::ScalarType out_dtype, const at::Scalar& beta, const at::Scalar& alpha, at::Tensor& out)` — [`L341`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L341)
- <a id="AtenBaddbmmOut"></a>`AtenBaddbmmOut(const at::Tensor& self, const at::Tensor& batch1, const at::Tensor& batch2, const at::Scalar& beta, const at::Scalar& alpha, at::Tensor& out)` — [`L366`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L366)
- `BuildBaddbmmInputs(const at::Tensor& self, const at::Tensor& batch1, const at::Tensor& batch2, bool beta_is_zero, std::optional<at::Tensor>& beta_tensor, std::optional<at::Tensor>& alpha_tensor)` — [`L206`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L206)
- <a id="BuildBaddbmmInputs"></a>`BuildBaddbmmInputs(const at::Tensor& self, const at::Tensor& batch1, const at::Tensor& batch2, bool beta_is_zero, std::optional<at::Tensor>& beta_tensor, std::optional<at::Tensor>& alpha_tensor)` — [`L206`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L206)
- `BuildBaddbmmShlo(std::optional<mlir::MlirOp> self_op, mlir::MlirOp batch1_op, mlir::MlirOp batch2_op, std::optional<mlir::MlirOp> beta_op, std::optional<mlir::MlirOp> alpha_op, const MaybePromotedScalar& beta, const MaybePromotedScalar& alpha, mlir::stablehlo::Precision precision, mlir::ElementType out_dtype)` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L111)
- <a id="BuildBaddbmmShlo"></a>`BuildBaddbmmShlo(std::optional<mlir::MlirOp> self_op, mlir::MlirOp batch1_op, mlir::MlirOp batch2_op, std::optional<mlir::MlirOp> beta_op, std::optional<mlir::MlirOp> alpha_op, const MaybePromotedScalar& beta, const MaybePromotedScalar& alpha, mlir::stablehlo::Precision precision, mlir::ElementType out_dtype)` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L111)
- <a id="DispatchBaddbmm"></a>`DispatchBaddbmm(const at::Tensor& self, const at::Tensor& batch1, const at::Tensor& batch2, MaybePromotedScalar beta, std::optional<at::Tensor> beta_tensor, MaybePromotedScalar alpha, std::optional<at::Tensor> alpha_tensor, at::ScalarType out_dtype, OpParamCacheKeys& param_keys, std::optional<OpName> op_name_override, DispatchFn&& dispatch_fn)` — [`L238`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L238)
- `GetBaddbmmOpBuilder(MaybePromotedScalar beta, MaybePromotedScalar alpha, bool beta_is_zero, bool has_beta_tensor, bool has_alpha_tensor, mlir::ElementType out_dtype_mlir, mlir::stablehlo::Precision precision)` — [`L174`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L174)
- <a id="GetBaddbmmOpBuilder"></a>`GetBaddbmmOpBuilder(MaybePromotedScalar beta, MaybePromotedScalar alpha, bool beta_is_zero, bool has_beta_tensor, bool has_alpha_tensor, mlir::ElementType out_dtype_mlir, mlir::stablehlo::Precision precision)` — [`L174`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L174)
- <a id="ResolveAndDispatchBaddbmm"></a>`ResolveAndDispatchBaddbmm(const at::Tensor& self, const at::Tensor& batch1, const at::Tensor& batch2, MaybePromotedScalar beta, MaybePromotedScalar alpha, at::ScalarType out_dtype, OpParamCacheKeys& param_keys, std::optional<OpName> op_name_override, DispatchFn&& dispatch_fn)` — [`L270`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L270)
- <a id="ResolveAndRunBaddbmm"></a>`ResolveAndRunBaddbmm(const at::Tensor& self, const at::Tensor& batch1, const at::Tensor& batch2, MaybePromotedScalar beta, MaybePromotedScalar alpha, at::ScalarType out_dtype, OpParamCacheKeys& param_keys, std::optional<OpName> op_name_override = std::nullopt)` — [`L289`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L289)
- <a id="ResolveAndRunBaddbmmOut"></a>`ResolveAndRunBaddbmmOut(const at::Tensor& self, const at::Tensor& batch1, const at::Tensor& batch2, MaybePromotedScalar beta, MaybePromotedScalar alpha, at::ScalarType out_dtype, OpParamCacheKeys& param_keys, at::Tensor& out, std::optional<OpName> op_name_override = std::nullopt)` — [`L303`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L303)
- <a id="ValidateBaddbmmDtypes"></a>`ValidateBaddbmmDtypes(at::ScalarType input_dtype, at::ScalarType out_dtype)` — [`L99`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L99)
- <a id="ValidateBaddbmmInputs"></a>`ValidateBaddbmmInputs(const at::Tensor& self, const at::Tensor& batch1, const at::Tensor& batch2)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L59)
- <a id="ValidateBaddbmmOut"></a>`ValidateBaddbmmOut(const at::Tensor& out, at::ScalarType expected_dtype)` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/ops/baddbmm/baddbmm_aten_kernels.cc#L51)

