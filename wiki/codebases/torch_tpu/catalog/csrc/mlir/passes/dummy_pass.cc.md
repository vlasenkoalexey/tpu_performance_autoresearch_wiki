---
title: 'Module: csrc/mlir/passes/dummy_pass.cc'
type: catalog
provenance: extracted
module: csrc/mlir/passes/dummy_pass.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  DummyPass: '`$anonymous_namespace_csrc/mlir/passes/dummy_pass.cc`/DummyPass#'
  createDummyPass: createDummyPass(f08ceea556e4e246).
  DummyPass.resolveTypeID: '`$anonymous_namespace_csrc/mlir/passes/dummy_pass.cc`/DummyPass#resolveTypeID(1920234c947e2cee).'
  DummyPass.runOnOperation: '`$anonymous_namespace_csrc/mlir/passes/dummy_pass.cc`/DummyPass#runOnOperation(49f6e7a06ebc5aa8).'
  DummyPass.getDescription: '`$anonymous_namespace_csrc/mlir/passes/dummy_pass.cc`/DummyPass#getDescription(b9baacb27e9a3fdd).'
  DummyPass.getArgument: '`$anonymous_namespace_csrc/mlir/passes/dummy_pass.cc`/DummyPass#getArgument(b9baacb27e9a3fdd).'
---
# Module: [`csrc/mlir/passes/dummy_pass.cc`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/dummy_pass.cc)

## Classes
### <a id="DummyPass"></a>`DummyPass`  ·  implements/extends OperationPass, Pass, PassWrapper
- def: [`csrc/mlir/passes/dummy_pass.cc:31`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/dummy_pass.cc#L31) — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)
- signature: `struct DummyPass : public mlir::PassWrapper<DummyPass, mlir::OperationPass<mlir::ModuleOp>>`
- members:
  - <a id="DummyPass.getArgument"></a>`getArgument()` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/dummy_pass.cc#L35)
  - <a id="DummyPass.getDescription"></a>`getDescription()` — [`L36`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/dummy_pass.cc#L36)
  - <a id="DummyPass.resolveTypeID"></a>`resolveTypeID(DummyPass)` — [`L33`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/dummy_pass.cc#L33)
  - <a id="DummyPass.runOnOperation"></a>`runOnOperation()` — [`L38`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/dummy_pass.cc#L38)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`createDummyPass`](dummy_pass.cc.md#createDummyPass)

## Functions
- <a id="createDummyPass"></a>`createDummyPass()` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/mlir/passes/dummy_pass.cc#L48) — documented in [mlir-optimization-passes](../../../../concepts/mlir-optimization-passes.md)

