---
title: 'Module: csrc/ops/hardsigmoid/hardsigmoid_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/hardsigmoid/hardsigmoid_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenHardsigmoidBackwardGradInput: AtenHardsigmoidBackwardGradInput(dcc870e438d8791).
  AtenHardsigmoidOut: AtenHardsigmoidOut(4655895dd4ef7692).
  BuildHardsigmoidShlo: '`$anonymous_namespace_csrc/ops/hardsigmoid/hardsigmoid_aten_kernels.cc`/BuildHardsigmoidShlo(a7867b6222e713f9).'
  BuildHardsigmoidBackwardShlo: '`$anonymous_namespace_csrc/ops/hardsigmoid/hardsigmoid_aten_kernels.cc`/BuildHardsigmoidBackwardShlo(9dd408ac7de815bd).'
---
# Module: [`csrc/ops/hardsigmoid/hardsigmoid_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardsigmoid/hardsigmoid_aten_kernels.cc)

## Functions
- <a id="AtenHardsigmoidBackwardGradInput"></a>`AtenHardsigmoidBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::Tensor& grad_input)` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardsigmoid/hardsigmoid_aten_kernels.cc#L109)
- <a id="AtenHardsigmoidOut"></a>`AtenHardsigmoidOut(const at::Tensor& self, at::Tensor& out)` — [`L96`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardsigmoid/hardsigmoid_aten_kernels.cc#L96)
- <a id="BuildHardsigmoidBackwardShlo"></a>`BuildHardsigmoidBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp self)` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardsigmoid/hardsigmoid_aten_kernels.cc#L64)
- <a id="BuildHardsigmoidShlo"></a>`BuildHardsigmoidShlo(mlir::MlirOp input_op)` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/ops/hardsigmoid/hardsigmoid_aten_kernels.cc#L43)

