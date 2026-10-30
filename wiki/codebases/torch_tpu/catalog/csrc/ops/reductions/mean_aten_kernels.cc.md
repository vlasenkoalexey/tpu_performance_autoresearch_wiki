---
title: 'Module: csrc/ops/reductions/mean_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/reductions/mean_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenMeanOut: AtenMeanOut(3a05ce237ec877a5).
  BuildMeanShlo: BuildMeanShlo(ecf6793c361629f0).
  GetOutputScalarType: '`$anonymous_namespace_csrc/ops/reductions/mean_aten_kernels.cc`/GetOutputScalarType(a173971b31a9121d).'
---
# Module: [`csrc/ops/reductions/mean_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/mean_aten_kernels.cc)

## Functions
- <a id="AtenMeanOut"></a>`AtenMeanOut(const at::Tensor& self, c10::OptionalArrayRef<int64_t> dim, bool keep_dim, std::optional<c10::ScalarType> dtype, at::Tensor& out)` — [`L71`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/mean_aten_kernels.cc#L71) — Implements aten::mean.out. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="BuildMeanShlo"></a>`BuildMeanShlo(mlir::MlirOp input, absl::Span<const int64_t> canonical_dims, ReductionMode reduction_mode, mlir::ElementType mlir_type)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/mean_aten_kernels.cc#L59) — documented in [reductions](../../../../concepts/reductions.md)
- <a id="GetOutputScalarType"></a>`GetOutputScalarType(const at::Tensor& tensor, std::optional<c10::ScalarType> dtype)` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/mean_aten_kernels.cc#L50) — Get the output scalar type and throw if it is float or complex. — documented in [reductions](../../../../concepts/reductions.md)

