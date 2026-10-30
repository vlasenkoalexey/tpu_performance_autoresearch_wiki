---
title: 'Module: csrc/ops/reductions/std_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/reductions/std_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenStd: AtenStd(785075c1ed694a3e).
  AtenStdOut: AtenStdOut(51db267bd4eaabb6).
  CreateStdBuilder: '`$anonymous_namespace_csrc/ops/reductions/std_aten_kernels.cc`/CreateStdBuilder(600167654cdf438).'
  WarnIfInvalidCorrection: '`$anonymous_namespace_csrc/ops/reductions/std_aten_kernels.cc`/WarnIfInvalidCorrection(69e3bcab7d28d8c6).'
---
# Module: [`csrc/ops/reductions/std_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/std_aten_kernels.cc)

## Functions
- <a id="AtenStd"></a>`AtenStd(const at::Tensor& self, c10::OptionalArrayRef<int64_t> dim, const std::optional<at::Scalar>& correction, bool keep_dim)` — [`L136`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/std_aten_kernels.cc#L136) — Implements aten::std.correction. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="AtenStdOut"></a>`AtenStdOut(const at::Tensor& self, c10::OptionalArrayRef<int64_t> dim, const std::optional<at::Scalar>& correction, bool keep_dim, at::Tensor& out)` — [`L189`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/std_aten_kernels.cc#L189) — Implements aten::std.correction_out. — documented in [reductions](../../../../concepts/reductions.md)
- <a id="CreateStdBuilder"></a>`CreateStdBuilder(Dimensions dim_vec, const ReductionMode reduction_mode, const int64_t reduction_size)` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/std_aten_kernels.cc#L60) — documented in [reductions](../../../../concepts/reductions.md)
- `CreateStdBuilder(Dimensions dim_vec, const ReductionMode reduction_mode, const int64_t reduction_size)` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/std_aten_kernels.cc#L60)
- <a id="WarnIfInvalidCorrection"></a>`WarnIfInvalidCorrection(OpName op_name, double correction_val, int64_t reduction_size)` — [`L122`](../../../../../../../raw/code/torch_tpu/csrc/ops/reductions/std_aten_kernels.cc#L122) — documented in [reductions](../../../../concepts/reductions.md)

