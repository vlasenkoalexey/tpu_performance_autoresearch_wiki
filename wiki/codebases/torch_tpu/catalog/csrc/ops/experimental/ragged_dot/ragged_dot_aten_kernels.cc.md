---
title: 'Module: csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenRaggedDotOut: AtenRaggedDotOut(5c91f28b56e0652e).
  AtenRaggedDotWeightGrad: AtenRaggedDotWeightGrad(7048bed50d562265).
  AtenRaggedDot: AtenRaggedDot(7048bed50d562265).
  RaggedDotWeightGradCommon: '`$anonymous_namespace_csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc`/RaggedDotWeightGradCommon(a8c45a720273836c).'
  RaggedDotCommon: '`$anonymous_namespace_csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc`/RaggedDotCommon(a8c45a720273836c).'
  AtenRaggedDotAutograd.forward: AtenRaggedDotAutograd#forward(e8201b08d703e8bd).
  BuildRaggedDotShlo: '`$anonymous_namespace_csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc`/BuildRaggedDotShlo(9cf4131192e75483).'
  BuildRaggedDotWeightGradShlo: '`$anonymous_namespace_csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc`/BuildRaggedDotWeightGradShlo(23bf05612740aa1f).'
  AtenRaggedDotAutograd.backward: AtenRaggedDotAutograd#backward(305625f81d7e100).
---
# Module: [`csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc)

## Functions
- <a id="AtenRaggedDot"></a>`AtenRaggedDot(const at::Tensor& lhs, const at::Tensor& rhs, const at::Tensor& group_sizes)` — [`L186`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc#L186) — Ragged dot product of two arrays, useful for implementing Mixture-of-Experts — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="AtenRaggedDotOut"></a>`AtenRaggedDotOut(const at::Tensor& lhs, const at::Tensor& rhs, const at::Tensor& group_sizes, at::Tensor& out)` — [`L195`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc#L195) — Ragged dot product of two arrays (out variant). — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="AtenRaggedDotWeightGrad"></a>`AtenRaggedDotWeightGrad(const at::Tensor& lhs, const at::Tensor& grad_output, const at::Tensor& group_sizes)` — [`L205`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc#L205) — Ragged dot product weight gradient. — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- `BuildRaggedDotShlo(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::MlirOp group_sizes, mlir::ElementType output_element_type, mlir::stablehlo::Precision precision)` — [`L56`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc#L56)
- <a id="BuildRaggedDotShlo"></a>`BuildRaggedDotShlo(mlir::MlirOp lhs, mlir::MlirOp rhs, mlir::MlirOp group_sizes, mlir::ElementType output_element_type, mlir::stablehlo::Precision precision)` — [`L56`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc#L56)
- `BuildRaggedDotWeightGradShlo(mlir::MlirOp lhs, mlir::MlirOp grad_output, mlir::MlirOp group_sizes, mlir::ElementType output_element_type, mlir::stablehlo::Precision precision)` — [`L118`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc#L118)
- <a id="BuildRaggedDotWeightGradShlo"></a>`BuildRaggedDotWeightGradShlo(mlir::MlirOp lhs, mlir::MlirOp grad_output, mlir::MlirOp group_sizes, mlir::ElementType output_element_type, mlir::stablehlo::Precision precision)` — [`L118`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc#L118)
- <a id="RaggedDotCommon"></a>`RaggedDotCommon(const at::Tensor& lhs, const at::Tensor& rhs, const at::Tensor& group_sizes, OpParamCacheKeys& param_keys)` — [`L85`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc#L85) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)
- <a id="RaggedDotWeightGradCommon"></a>`RaggedDotWeightGradCommon(const at::Tensor& lhs, const at::Tensor& grad_output, const at::Tensor& group_sizes, OpParamCacheKeys& param_keys)` — [`L154`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc#L154) — documented in [ragged-collectives-and-sparse-ops](../../../../../concepts/ragged-collectives-and-sparse-ops.md)

## Other members
- <a id="AtenRaggedDotAutograd.backward"></a>`AtenRaggedDotAutograd.backward` — [`L234`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc#L234)
- <a id="AtenRaggedDotAutograd.forward"></a>`AtenRaggedDotAutograd.forward` — [`L217`](../../../../../../../../raw/code/torch_tpu/csrc/ops/experimental/ragged_dot/ragged_dot_aten_kernels.cc#L217)

