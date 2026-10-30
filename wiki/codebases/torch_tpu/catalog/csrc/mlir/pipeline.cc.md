---
title: 'Module: csrc/mlir/pipeline.cc'
type: catalog
provenance: extracted
module: csrc/mlir/pipeline.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  RunTorchTpuOptimizationPasses: RunTorchTpuOptimizationPasses(ed158db35b603e84).
  AddTorchTpuOptimizationPasses: AddTorchTpuOptimizationPasses(1a73a1fe8fd0682f).
  AddShloPasses: '`$anonymous_namespace_csrc/mlir/pipeline.cc`/AddShloPasses(1a73a1fe8fd0682f).'
  AddCleanupPasses: '`$anonymous_namespace_csrc/mlir/pipeline.cc`/AddCleanupPasses(1a73a1fe8fd0682f).'
---
# Module: [`csrc/mlir/pipeline.cc`](../../../../../../raw/code/torch_tpu/csrc/mlir/pipeline.cc)

## Functions
- <a id="AddCleanupPasses"></a>`AddCleanupPasses(mlir::PassManager& pm)` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/mlir/pipeline.cc#L38) — documented in [mlir-optimization-passes](../../../concepts/mlir-optimization-passes.md)
- <a id="AddShloPasses"></a>`AddShloPasses(mlir::PassManager& pm)` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/mlir/pipeline.cc#L50) — documented in [mlir-optimization-passes](../../../concepts/mlir-optimization-passes.md)
- <a id="AddTorchTpuOptimizationPasses"></a>`AddTorchTpuOptimizationPasses(mlir::PassManager& pm)` — [`L61`](../../../../../../raw/code/torch_tpu/csrc/mlir/pipeline.cc#L61) — Adds Torch TPU optimization passes to the pass manager. — documented in [mlir-optimization-passes](../../../concepts/mlir-optimization-passes.md)
- <a id="RunTorchTpuOptimizationPasses"></a>`RunTorchTpuOptimizationPasses(mlir::ModuleOp module, mlir::MLIRContext* context)` — [`L68`](../../../../../../raw/code/torch_tpu/csrc/mlir/pipeline.cc#L68) — Runs all custom Torch TPU optimization passes on the given module. — documented in [mlir-optimization-passes](../../../concepts/mlir-optimization-passes.md)

