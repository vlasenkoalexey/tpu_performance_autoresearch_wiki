---
title: 'Module: csrc/ops/reductions/var_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/reductions/var_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenVarMeanCorrection: AtenVarMeanCorrection(e8b5b51af5840bf).
  AtenVar: AtenVar(785075c1ed694a3e).
  AtenVarOut: AtenVarOut(51db267bd4eaabb6).
  CreateVarBuilder: '`$anonymous_namespace_csrc/ops/reductions/var_aten_kernels.cc`/CreateVarBuilder(70eb8009a9252343).'
  WarnIfInvalidCorrection: '`$anonymous_namespace_csrc/ops/reductions/var_aten_kernels.cc`/WarnIfInvalidCorrection(69e3bcab7d28d8c6).'
---
# Module: [`csrc/ops/reductions/var_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/var_aten_kernels.cc)

## Functions
- <a id="AtenVar"></a>`AtenVar(const at::Tensor& self, c10::OptionalArrayRef<int64_t> dim, const std::optional<at::Scalar>& correction, bool keep_dim)` — [`L151`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/var_aten_kernels.cc#L151) — Implements aten::var.correction. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="AtenVarMeanCorrection"></a>`AtenVarMeanCorrection(const at::Tensor& self, c10::OptionalArrayRef<int64_t> dim, const std::optional<at::Scalar>& correction, bool keep_dim)` — [`L246`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/var_aten_kernels.cc#L246) — Implements aten::var_mean.correction. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="AtenVarOut"></a>`AtenVarOut(const at::Tensor& self, c10::OptionalArrayRef<int64_t> dim, const std::optional<at::Scalar>& correction, bool keep_dim, at::Tensor& out)` — [`L196`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/var_aten_kernels.cc#L196) — Implements aten::var.correction_out. — documented in [reductions](../../../../concepts/reductions.md)
- `CreateVarBuilder(Dimensions dim_vec, ReductionMode reduction_mode, int64_t reduction_size, mlir::ElementType scalar_dtype_mlir)` — [`L66`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/var_aten_kernels.cc#L66)
- <a id="CreateVarBuilder"></a>`CreateVarBuilder(Dimensions dim_vec, ReductionMode reduction_mode, int64_t reduction_size, mlir::ElementType scalar_dtype_mlir)` — [`L66`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/var_aten_kernels.cc#L66) — documented in [reductions](../../../../concepts/reductions.md)
- <a id="WarnIfInvalidCorrection"></a>`WarnIfInvalidCorrection(OpName op_name, double correction_val, int64_t reduction_size)` — [`L137`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/var_aten_kernels.cc#L137) — documented in [reductions](../../../../concepts/reductions.md)

