---
title: 'Module: csrc/mlir/registration.cc'
type: catalog
provenance: extracted
module: csrc/mlir/registration.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  RegisterTorchTpuPasses: RegisterTorchTpuPasses(49f6e7a06ebc5aa8).
  RegisterTorchTpuDialects: RegisterTorchTpuDialects(84bc6d99746846d2).
---
# Module: [`csrc/mlir/registration.cc`](../../../../../../raw/code/torch_tpu/csrc/mlir/registration.cc)

## Functions
- <a id="RegisterTorchTpuDialects"></a>`RegisterTorchTpuDialects(mlir::DialectRegistry& registry)` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/mlir/registration.cc#L38) — Registers dependent dialects for custom Torch TPU passes. — documented in [mlir-optimization-passes](../../../concepts/mlir-optimization-passes.md)
- <a id="RegisterTorchTpuPasses"></a>`RegisterTorchTpuPasses()` — [`L30`](../../../../../../raw/code/torch_tpu/csrc/mlir/registration.cc#L30) — Registers all custom Torch TPU passes with the MLIR global registry. — documented in [mlir-optimization-passes](../../../concepts/mlir-optimization-passes.md)

