---
title: 'Module: csrc/ops/take/take_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/take/take_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenTake: AtenTake(91c7cc726c97ea99).
  AtenTakeOut: AtenTakeOut(dcc870e438d8791).
  ValidateTakeInputs: '`$anonymous_namespace_csrc/ops/take/take_aten_kernels.cc`/ValidateTakeInputs(b2d6689cde60befb).'
  ValidateIndices: '`$anonymous_namespace_csrc/ops/take/take_aten_kernels.cc`/ValidateIndices(8aa209b812aff327).'
  BuildTakeShlo: '`$anonymous_namespace_csrc/ops/take/take_aten_kernels.cc`/BuildTakeShlo(33905599cf21d92f).'
---
# Module: [`csrc/ops/take/take_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/take/take_aten_kernels.cc)

## Functions
- <a id="AtenTake"></a>`AtenTake(const at::Tensor& self, const at::Tensor& index)` — [`L142`](../../../../../../../raw/code/torch_tpu/csrc/ops/take/take_aten_kernels.cc#L142)
- <a id="AtenTakeOut"></a>`AtenTakeOut(const at::Tensor& self, const at::Tensor& index, at::Tensor& out)` — [`L165`](../../../../../../../raw/code/torch_tpu/csrc/ops/take/take_aten_kernels.cc#L165)
- <a id="BuildTakeShlo"></a>`BuildTakeShlo(const int64_t num_elements, mlir::MlirOp input_op, mlir::MlirOp index_op)` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/take/take_aten_kernels.cc#L53)
- <a id="ValidateIndices"></a>`ValidateIndices(const int64_t num_elements, const at::Tensor& index)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/take/take_aten_kernels.cc#L100) — Validates that the indices are in the range [-num_elements, num_elements).
- <a id="ValidateTakeInputs"></a>`ValidateTakeInputs(const at::Tensor& self, const at::Tensor& index)` — [`L119`](../../../../../../../raw/code/torch_tpu/csrc/ops/take/take_aten_kernels.cc#L119)

