---
title: 'Module: csrc/ops/lerp/lerp_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/lerp/lerp_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenLerpTensorOut: AtenLerpTensorOut(5c91f28b56e0652e).
  AtenLerpScalarOut: AtenLerpScalarOut(82d77f320475bbd9).
  ValidateLerpSelfInput: '`$anonymous_namespace_csrc/ops/lerp/lerp_aten_kernels.cc`/ValidateLerpSelfInput(fd0458bfc68bb174).'
  BuildLerpShlo: '`$anonymous_namespace_csrc/ops/lerp/lerp_aten_kernels.cc`/BuildLerpShlo(1afb0f87c3c97102).'
  GetLerpTensorOutFunctional: '`$anonymous_namespace_csrc/ops/lerp/lerp_aten_kernels.cc`/GetLerpTensorOutFunctional(ef7a755529aae27a).'
---
# Module: [`csrc/ops/lerp/lerp_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/lerp/lerp_aten_kernels.cc)

## Functions
- <a id="AtenLerpScalarOut"></a>`AtenLerpScalarOut(const at::Tensor& self, const at::Tensor& end, const at::Scalar& weight, at::Tensor& out)` — [`L124`](../../../../../../../raw/code/torch_tpu/csrc/ops/lerp/lerp_aten_kernels.cc#L124)
- <a id="AtenLerpTensorOut"></a>`AtenLerpTensorOut(const at::Tensor& self, const at::Tensor& end, const at::Tensor& weight, at::Tensor& out)` — [`L90`](../../../../../../../raw/code/torch_tpu/csrc/ops/lerp/lerp_aten_kernels.cc#L90)
- <a id="BuildLerpShlo"></a>`BuildLerpShlo(mlir::MlirOp self, mlir::MlirOp end, mlir::MlirOp weight, mlir::ElementType common_type)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/lerp/lerp_aten_kernels.cc#L59)
- `BuildLerpShlo(mlir::MlirOp self, mlir::MlirOp end, mlir::MlirOp weight, mlir::ElementType common_type)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/lerp/lerp_aten_kernels.cc#L59)
- `GetLerpTensorOutFunctional(mlir::ElementType common_type)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/lerp/lerp_aten_kernels.cc#L80)
- <a id="GetLerpTensorOutFunctional"></a>`GetLerpTensorOutFunctional(mlir::ElementType common_type)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/lerp/lerp_aten_kernels.cc#L80)
- <a id="ValidateLerpSelfInput"></a>`ValidateLerpSelfInput(const at::Tensor& self)` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/lerp/lerp_aten_kernels.cc#L47)

