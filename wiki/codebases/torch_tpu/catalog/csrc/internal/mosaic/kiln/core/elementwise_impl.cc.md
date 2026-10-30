---
title: 'Module: csrc/internal/mosaic/kiln/core/elementwise_impl.cc'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/elementwise_impl.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/internal/
symbols:
  EmitBroadcast: EmitBroadcast(dd46b79fc56eec51).
  AlignShapes: AlignShapes(2c612b004f152098).
  BroadcastShapes: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/elementwise_impl.cc`/BroadcastShapes(29e1e2629924f499).'
  ShapeOf: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/elementwise_impl.cc`/ShapeOf(da4b966f9aed6df6).'
---
# Module: [`csrc/internal/mosaic/kiln/core/elementwise_impl.cc`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.cc)

## Functions
- <a id="AlignShapes"></a>`AlignShapes(llvm::MutableArrayRef<mlir::Value> values)` — [`L77`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.cc#L77) — Brings the operands of a multi-operand elementwise op to a common shape. — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="BroadcastShapes"></a>`BroadcastShapes(llvm::ArrayRef<int64_t> lhs, llvm::ArrayRef<int64_t> rhs)` — [`L46`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.cc#L46) — numpy broadcasting rule over two static shapes; CHECK-fails if the shapes
- <a id="EmitBroadcast"></a>`EmitBroadcast(mlir::Value value, llvm::ArrayRef<int64_t> shape)` — [`L66`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.cc#L66) — Broadcasts `value` (a scalar or vector) to a vector of `shape`. Returns — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="ShapeOf"></a>`ShapeOf(mlir::Value value)` — [`L37`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.cc#L37) — The shape of a scalar or vector value; scalars are rank 0.

