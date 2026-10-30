---
title: 'Module: csrc/ops/dot/vdot_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/dot/vdot_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenVdot: AtenVdot(91c7cc726c97ea99).
  ValidateInputs: '`$anonymous_namespace_csrc/ops/dot/vdot_aten_kernels.cc`/ValidateInputs(b2d6689cde60befb).'
  Vdot: '`$anonymous_namespace_csrc/ops/dot/vdot_aten_kernels.cc`/Vdot(a040e14dea9dc5e7).'
  BuildVdotShlo: '`$anonymous_namespace_csrc/ops/dot/vdot_aten_kernels.cc`/BuildVdotShlo(b90871bd45ad311f).'
---
# Module: [`csrc/ops/dot/vdot_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/dot/vdot_aten_kernels.cc)

## Functions
- <a id="AtenVdot"></a>`AtenVdot(const at::Tensor& lhs, const at::Tensor& rhs)` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/ops/dot/vdot_aten_kernels.cc#L86)
- `BuildVdotShlo(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::Precision precision)` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/ops/dot/vdot_aten_kernels.cc#L42)
- <a id="BuildVdotShlo"></a>`BuildVdotShlo(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::stablehlo::Precision precision)` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/ops/dot/vdot_aten_kernels.cc#L42)
- <a id="ValidateInputs"></a>`ValidateInputs(const at::Tensor& lhs, const at::Tensor& rhs)` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/dot/vdot_aten_kernels.cc#L48)
- <a id="Vdot"></a>`Vdot(const at::Tensor& lhs, const at::Tensor& rhs, OpParamCacheKeys param_keys)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/dot/vdot_aten_kernels.cc#L59)

