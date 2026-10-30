---
title: 'Module: csrc/ops/triangular/triangular.h'
type: catalog
provenance: extracted
module: csrc/ops/triangular/triangular.h
status: fresh
symbol_base: cxx . . $ torch_tpu/TriangleType#
symbols:
  TriangleType.kLower: kLower.
  TriangleType: ''
  TriangleType.kUpper: kUpper.
---
# Module: [`csrc/ops/triangular/triangular.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/triangular/triangular.h)

## Classes
### <a id="TriangleType"></a>`TriangleType`
- def: [`csrc/ops/triangular/triangular.h:27`](../../../../../../../raw/code/torch_tpu/csrc/ops/triangular/triangular.h#L27)
- signature: `enum class TriangleType`
- members:
  - <a id="TriangleType.kLower"></a>`kLower` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/triangular/triangular.h#L29)
  - <a id="TriangleType.kUpper"></a>`kUpper` — [`L28`](../../../../../../../raw/code/torch_tpu/csrc/ops/triangular/triangular.h#L28)
- uses (calls/refs, reference-scoped): [`BuildTriangularShlo`](triangular.cc.md#BuildTriangularShlo)
- used by: [`AtenTrilOut`](triangular_aten_kernels.cc.md#AtenTrilOut), [`AtenTriuOut`](triangular_aten_kernels.cc.md#AtenTriuOut), [`BuildTriangularShlo`](triangular.cc.md#BuildTriangularShlo), [`TriangularMask`](triangular.cc.md#TriangularMask)

