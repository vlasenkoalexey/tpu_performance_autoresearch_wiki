---
title: 'Module: csrc/ops/view_decomposition/conj_primitive.h'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/conj_primitive.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ConjPrimitive: ConjPrimitive#
  UpdateLayout: UpdateLayout(26b5877a645ad1da).
  ConjPrimitive.is_set: ConjPrimitive#is_set.
---
# Module: [`csrc/ops/view_decomposition/conj_primitive.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/conj_primitive.h)

## Classes
### <a id="ConjPrimitive"></a>`ConjPrimitive`
- def: [`csrc/ops/view_decomposition/conj_primitive.h:25`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/conj_primitive.h#L25)
- signature: `struct ConjPrimitive`
- members:
  - <a id="ConjPrimitive.is_set"></a>`is_set` — [`L26`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/conj_primitive.h#L26)
- used by: [`operator==`](view_sequence.cc.md#operator), [`DecomposeIntoViewSequence`](decomposition.cc.md#DecomposeIntoViewSequence), [`operator==`](inversion.cc.md#operator), [`ViewPrimitive`](view_sequence.h.md#ViewPrimitive), [`operator<<`](view_sequence.cc.md#operator), [`operator<<`](inversion.cc.md#operator), [`TestBody`](view_sequence_test.cc.md#SymbolicViewPrimitive_CastingViewCacheKeys_Test.TestBody), [`InverseViewPrimitive`](inversion.h.md#InverseViewPrimitive), [`UpdateLayout`](inversion.cc.md#UpdateLayout), [`ViewPrimitiveShlo`](view_sequence.cc.md#ViewPrimitiveShlo), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_InvertConj_Test.TestBody), [`MaybeMergeSequential`](view_sequence.cc.md#MaybeMergeSequential), [`UpdateLayout`](conj_primitive.h.md#UpdateLayout), [`TestBody`](view_sequence_test.cc.md#Simplify_ReshapeConj_Test.TestBody), [`TestBody`](view_sequence_test.cc.md#Simplify_ConjComplex_Test.TestBody), [`TestBody`](view_sequence_test.cc.md#Simplify_ConjReal_Test.TestBody), [`TestBody`](view_sequence_test.cc.md#Simplify_DoubleConj_Test.TestBody), [`TestBody`](view_sequence_test.cc.md#ViewPrimitiveEquality_ConjPrimitive_Test.TestBody), [`InvertViewPrimitive`](inversion.cc.md#InvertViewPrimitive), [`operator()`](view_sequence.cc.md#ViewCacheKeyVisitor.operator)

## Functions
- <a id="UpdateLayout"></a>`UpdateLayout(StridedLayout& layout, const ConjPrimitive& primitive)` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/conj_primitive.h#L29)

