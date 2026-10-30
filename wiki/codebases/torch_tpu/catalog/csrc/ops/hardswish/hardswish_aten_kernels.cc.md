---
title: 'Module: csrc/ops/hardswish/hardswish_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/hardswish/hardswish_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenHardswishBackward: AtenHardswishBackward(91c7cc726c97ea99).
  AtenHardswish_: AtenHardswish_(2c0150b1d2cc4760).
  AtenHardswishOut: AtenHardswishOut(4655895dd4ef7692).
  AtenHardswish: AtenHardswish(28959186f7a4bda8).
  BuildHardswishShlo: '`$anonymous_namespace_csrc/ops/hardswish/hardswish_aten_kernels.cc`/BuildHardswishShlo(a7867b6222e713f9).'
  BuildHardswishBackwardShlo: '`$anonymous_namespace_csrc/ops/hardswish/hardswish_aten_kernels.cc`/BuildHardswishBackwardShlo(9dd408ac7de815bd).'
---
# Module: [`csrc/ops/hardswish/hardswish_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardswish/hardswish_aten_kernels.cc)

## Functions
- <a id="AtenHardswish"></a>`AtenHardswish(const at::Tensor& self)` — [`L89`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardswish/hardswish_aten_kernels.cc#L89)
- <a id="AtenHardswishBackward"></a>`AtenHardswishBackward(const at::Tensor& grad_output, const at::Tensor& self)` — [`L128`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardswish/hardswish_aten_kernels.cc#L128)
- <a id="AtenHardswishOut"></a>`AtenHardswishOut(const at::Tensor& self, at::Tensor& out)` — [`L103`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardswish/hardswish_aten_kernels.cc#L103)
- <a id="AtenHardswish_"></a>`AtenHardswish_(at::Tensor& self)` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardswish/hardswish_aten_kernels.cc#L116)
- <a id="BuildHardswishBackwardShlo"></a>`BuildHardswishBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp self)` — [`L60`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardswish/hardswish_aten_kernels.cc#L60)
- <a id="BuildHardswishShlo"></a>`BuildHardswishShlo(mlir::MlirOp input_op)` — [`L45`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardswish/hardswish_aten_kernels.cc#L45)

