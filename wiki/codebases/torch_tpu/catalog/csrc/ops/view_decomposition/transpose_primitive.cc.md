---
title: 'Module: csrc/ops/view_decomposition/transpose_primitive.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/transpose_primitive.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  operator: '`operator<<`(c10568c4e307dbcf).'
  UpdateLayout: UpdateLayout(486f5aded24c3e9b).
  CheckTranspose: '`$anonymous_namespace_csrc/ops/view_decomposition/transpose_primitive.cc`/CheckTranspose(9bbb2e54d14bf076).'
  ViewPrimitiveShlo: ViewPrimitiveShlo(4a1c001c7c5b318d).
---
# Module: [`csrc/ops/view_decomposition/transpose_primitive.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/transpose_primitive.cc)

## Functions
- <a id="CheckTranspose"></a>`CheckTranspose(const TransposePrimitive& transpose, const StridedLayout& layout)` — [`L37`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/transpose_primitive.cc#L37)
- <a id="UpdateLayout"></a>`UpdateLayout(StridedLayout& layout, const TransposePrimitive& transpose)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/transpose_primitive.cc#L80) — Updates the layout to reflect the effect of applying the given transpose.
- <a id="ViewPrimitiveShlo"></a>`ViewPrimitiveShlo(mlir::MlirOp input, const TransposePrimitive& transpose)` — [`L103`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/transpose_primitive.cc#L103) — An overload for the ViewPrimitiveShlo function that handles transpose
- <a id="operator"></a>`operator<<(std::ostream& os, const TransposePrimitive& transpose)` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/transpose_primitive.cc#L74) — Formats the transpose like "transpose([1, 2, 0])".

