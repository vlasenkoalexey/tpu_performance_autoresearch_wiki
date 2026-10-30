---
title: 'Module: csrc/ops/triangular/triangular.cc'
type: catalog
provenance: extracted
module: csrc/ops/triangular/triangular.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  BuildTriangularShlo: BuildTriangularShlo(5f1d4270535be7de).
  TriangularMask: '`$anonymous_namespace_csrc/ops/triangular/triangular.cc`/TriangularMask(b7802e666cfcf91f).'
---
# Module: [`csrc/ops/triangular/triangular.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/triangular/triangular.cc)

## Functions
- <a id="BuildTriangularShlo"></a>`BuildTriangularShlo(const int64_t diagonal, const TriangleType triangle_type, mlir::MlirOp input_op)` — [`L97`](../../../../../../../raw/code/torch_tpu/csrc/ops/triangular/triangular.cc#L97)
- `TriangularMask(mlir::MlirBuilder& builder, const Dimensions& input_shape, int64_t diagonal, TriangleType triangle_type)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/triangular/triangular.cc#L63) — Creates a boolean mask for the upper/lower triangle of a matrix.
- <a id="TriangularMask"></a>`TriangularMask(mlir::MlirBuilder& builder, const Dimensions& input_shape, int64_t diagonal, TriangleType triangle_type)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/triangular/triangular.cc#L63) — Creates a boolean mask for the upper/lower triangle of a matrix.

