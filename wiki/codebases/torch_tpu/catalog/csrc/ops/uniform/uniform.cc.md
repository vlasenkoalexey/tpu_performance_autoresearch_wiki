---
title: 'Module: csrc/ops/uniform/uniform.cc'
type: catalog
provenance: extracted
module: csrc/ops/uniform/uniform.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BitsToUniform: BitsToUniform(28dc33d166dda8e).
  BuildUniformShlo: BuildUniformShlo(5dd59e67c3000056).
---
# Module: [`csrc/ops/uniform/uniform.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/uniform/uniform.cc)

## Functions
- <a id="BitsToUniform"></a>`BitsToUniform(mlir::MlirOp random_bits, mlir::MlirOp from, mlir::MlirOp to)` — [`L40`](../../../../../../../raw/code/torch_tpu/csrc/ops/uniform/uniform.cc#L40) — Converts random bits to a uniform distribution in [from, to). The idea is
- `BuildUniformShlo(mlir::MlirOp rng_input_state, const double from, const double to, const llvm::ArrayRef<int64_t> sizes, const mlir::ElementType mlir_type)` — [`L142`](../../../../../../../raw/code/torch_tpu/csrc/ops/uniform/uniform.cc#L142) — Uses the philox algorithm and `rng_input_state` to generate random u64s and
- `BuildUniformShlo(mlir::MlirOp rng_input_state, const double from, const double to, const llvm::ArrayRef<int64_t> sizes, const mlir::ElementType mlir_type)` — [`L142`](../../../../../../../raw/code/torch_tpu/csrc/ops/uniform/uniform.cc#L142) — Uses the philox algorithm and `rng_input_state` to generate random u64s and
- <a id="BuildUniformShlo"></a>`BuildUniformShlo(mlir::MlirOp rng_input_state, const double from, const double to, mlir::RankedTensorType output_tensor_type, std::optional<mlir::MlirOp> shape_reference)` — [`L118`](../../../../../../../raw/code/torch_tpu/csrc/ops/uniform/uniform.cc#L118)
- `BuildUniformShlo(mlir::MlirOp rng_input_state, const double from, const double to, mlir::RankedTensorType output_tensor_type, std::optional<mlir::MlirOp> shape_reference)` — [`L118`](../../../../../../../raw/code/torch_tpu/csrc/ops/uniform/uniform.cc#L118)

