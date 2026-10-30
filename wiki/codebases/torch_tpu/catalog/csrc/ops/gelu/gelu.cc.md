---
title: 'Module: csrc/ops/gelu/gelu.cc'
type: catalog
provenance: extracted
module: csrc/ops/gelu/gelu.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildGeluShlo: BuildGeluShlo(a92b2863729499a4).
  BuildGeluBackwardGradInputShlo: BuildGeluBackwardGradInputShlo(6a923a983ac8ec6d).
  BuildGeluApproximateShlo: '`$anonymous_namespace_csrc/ops/gelu/gelu.cc`/BuildGeluApproximateShlo(a7867b6222e713f9).'
  BuildGeluNoneShlo: '`$anonymous_namespace_csrc/ops/gelu/gelu.cc`/BuildGeluNoneShlo(a7867b6222e713f9).'
  BuildGeluBackwardGradInputApproximateShlo: '`$anonymous_namespace_csrc/ops/gelu/gelu.cc`/BuildGeluBackwardGradInputApproximateShlo(9dd408ac7de815bd).'
  BuildGeluBackwardGradInputNoneShlo: '`$anonymous_namespace_csrc/ops/gelu/gelu.cc`/BuildGeluBackwardGradInputNoneShlo(9dd408ac7de815bd).'
---
# Module: [`csrc/ops/gelu/gelu.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/gelu/gelu.cc)

## Functions
- <a id="BuildGeluApproximateShlo"></a>`BuildGeluApproximateShlo(mlir::MlirOp input_op)` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/ops/gelu/gelu.cc#L43) — TODO:(gleasonk) Make builder API allow inline exprs
- <a id="BuildGeluBackwardGradInputApproximateShlo"></a>`BuildGeluBackwardGradInputApproximateShlo(mlir::MlirOp grad_output_op, mlir::MlirOp input_op)` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/ops/gelu/gelu.cc#L86) — When approximation_type == "tanh", we compute the approximate gelu formula.
- <a id="BuildGeluBackwardGradInputNoneShlo"></a>`BuildGeluBackwardGradInputNoneShlo(mlir::MlirOp grad_output_op, mlir::MlirOp input_op)` — [`L146`](../../../../../../../raw/code/torch_tpu/csrc/ops/gelu/gelu.cc#L146) — When approximation_type == "none", we compute the exact gelu formula.
- <a id="BuildGeluBackwardGradInputShlo"></a>`BuildGeluBackwardGradInputShlo(mlir::MlirOp grad_output_op, mlir::MlirOp input_op, std::string_view approximation_type, mlir::ElementType output_dtype)` — [`L204`](../../../../../../../raw/code/torch_tpu/csrc/ops/gelu/gelu.cc#L204)
- <a id="BuildGeluNoneShlo"></a>`BuildGeluNoneShlo(mlir::MlirOp input_op)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/gelu/gelu.cc#L63)
- <a id="BuildGeluShlo"></a>`BuildGeluShlo(mlir::MlirOp input_op, std::string_view approximation_type, mlir::ElementType output_dtype)` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/ops/gelu/gelu.cc#L179)

