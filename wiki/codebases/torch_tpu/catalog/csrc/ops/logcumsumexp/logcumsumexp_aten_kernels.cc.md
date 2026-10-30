---
title: 'Module: csrc/ops/logcumsumexp/logcumsumexp_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/logcumsumexp/logcumsumexp_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenLogcumsumexpOut: AtenLogcumsumexpOut(bb14b1a8f74bfba5).
  AtenLogcumsumexp: AtenLogcumsumexp(bdddabee2c33be9d).
  BuildLogcumsumexpShlo: '`$anonymous_namespace_csrc/ops/logcumsumexp/logcumsumexp_aten_kernels.cc`/BuildLogcumsumexpShlo(7ffe041ec13ead19).'
  LogaddexpScanBody: '`$anonymous_namespace_csrc/ops/logcumsumexp/logcumsumexp_aten_kernels.cc`/LogaddexpScanBody(975424d98b53259).'
---
# Module: [`csrc/ops/logcumsumexp/logcumsumexp_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/logcumsumexp/logcumsumexp_aten_kernels.cc)

## Functions
- <a id="AtenLogcumsumexp"></a>`AtenLogcumsumexp(const at::Tensor& self, const int64_t dim)` — [`L158`](../../../../../../../raw/code/torch_tpu/csrc/ops/logcumsumexp/logcumsumexp_aten_kernels.cc#L158)
- <a id="AtenLogcumsumexpOut"></a>`AtenLogcumsumexpOut(const at::Tensor& self, const int64_t dim, at::Tensor& out)` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/ops/logcumsumexp/logcumsumexp_aten_kernels.cc#L179)
- <a id="BuildLogcumsumexpShlo"></a>`BuildLogcumsumexpShlo(const int64_t normalized_dim, const std::optional<mlir::ElementType> out_dtype, mlir::MlirOp input)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/logcumsumexp/logcumsumexp_aten_kernels.cc#L100) — Lowers logcumsumexp along 'normalized_dim' to an associative chlo.ScanOp
- <a id="LogaddexpScanBody"></a>`LogaddexpScanBody(mlir::OpBuilder& op_builder, mlir::Location loc, mlir::ValueRange input_slices, mlir::Value /*index*/, mlir::ValueRange carries)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/logcumsumexp/logcumsumexp_aten_kernels.cc#L59) — Associative scan combiner for logcumsumexp: a numerically stable logaddexp.

