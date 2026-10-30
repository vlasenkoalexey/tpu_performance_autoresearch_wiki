---
title: 'Module: csrc/ops/index_fill/index_fill_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/index_fill/index_fill_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenIndexFillIntTensor_: AtenIndexFillIntTensor_(8491dc5ce42d9f2e).
  AtenIndexFillIntScalar_: AtenIndexFillIntScalar_(d9c40b656cafb993).
  ValidateIndexFillInputs: '`$anonymous_namespace_csrc/ops/index_fill/index_fill_aten_kernels.cc`/ValidateIndexFillInputs(1640b93e43d240ae).'
  BuildIndexFillShlo: '`$anonymous_namespace_csrc/ops/index_fill/index_fill_aten_kernels.cc`/BuildIndexFillShlo(20f53584273fe272).'
---
# Module: [`csrc/ops/index_fill/index_fill_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_fill/index_fill_aten_kernels.cc)

## Functions
- <a id="AtenIndexFillIntScalar_"></a>`AtenIndexFillIntScalar_(at::Tensor& self, int64_t dim, const at::Tensor& index, const at::Scalar& value)` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_fill/index_fill_aten_kernels.cc#L116)
- <a id="AtenIndexFillIntTensor_"></a>`AtenIndexFillIntTensor_(at::Tensor& self, int64_t dim, const at::Tensor& index, const at::Tensor& value)` — [`L148`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_fill/index_fill_aten_kernels.cc#L148)
- <a id="BuildIndexFillShlo"></a>`BuildIndexFillShlo(mlir::MlirOp self, int64_t dim, mlir::MlirOp index, mlir::MlirOp value)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_fill/index_fill_aten_kernels.cc#L54)
- <a id="ValidateIndexFillInputs"></a>`ValidateIndexFillInputs(const at::Tensor& self, int64_t dim, const at::Tensor& index)` — [`L105`](../../../../../../../raw/code/torch_tpu/csrc/ops/index_fill/index_fill_aten_kernels.cc#L105)

