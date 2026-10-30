---
title: 'Module: csrc/ops/view_decomposition/transpose_primitive.h'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/transpose_primitive.h
status: fresh
symbol_base: cxx . . $ torch_tpu/TransposePrimitive#
symbols:
  TransposePrimitive: ''
  TransposePrimitive.permutation: permutation.
---
# Module: [`csrc/ops/view_decomposition/transpose_primitive.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/transpose_primitive.h)

## Classes
### <a id="TransposePrimitive"></a>`TransposePrimitive`
- def: [`csrc/ops/view_decomposition/transpose_primitive.h:50`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/transpose_primitive.h#L50)
- doc: A transpose primitive converts an N-dimensionsal tensor into another
- signature: `struct TransposePrimitive`
- members:
  - <a id="TransposePrimitive.permutation"></a>`permutation` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/transpose_primitive.h#L51)
- uses (calls/refs, reference-scoped): [`StridedLayout`](strided_layout.h.md#StridedLayout), [`Indices`](../../common/dimension_types.h.md#Indices), [`operator<<`](transpose_primitive.cc.md#operator), [`UpdateLayout`](transpose_primitive.cc.md#UpdateLayout), [`ViewPrimitiveShlo`](transpose_primitive.cc.md#ViewPrimitiveShlo)
- used by: [`operator==`](view_sequence.cc.md#operator), [`operator<<`](transpose_primitive.cc.md#operator), [`operator==`](inversion.cc.md#operator), [`ViewPrimitive`](view_sequence.h.md#ViewPrimitive), [`operator<<`](view_sequence.cc.md#operator), [`operator<<`](inversion.cc.md#operator), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ImaginaryPartPreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_RealPartPreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ImaginaryPart_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_RealPart_Test.TestBody), [`InvertViewPrimitive`](inversion.cc.md#InvertViewPrimitive), [`InverseViewPrimitive`](inversion.h.md#InverseViewPrimitive), [`UpdateLayout`](transpose_primitive.cc.md#UpdateLayout), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_PermuteTensor_Test.TestBody), [`BuildTailNoBroadcast`](decomposition.cc.md#BuildTailNoBroadcast), [`TestBody`](view_sequence_test.cc.md#SymbolicViewPrimitive_MultipleViewCacheKeys_Test.TestBody), [`TestBody`](view_sequence_test.cc.md#SymbolicViewPrimitive_TransposeViewCacheKeys_Test.TestBody), [`TestBody`](view_sequence_test.cc.md#Simplify_NothingToSimplify_Test.TestBody), [`CheckTranspose`](transpose_primitive.cc.md#CheckTranspose), [`TestBody`](transpose_primitive_test.cc.md#UpdateLayoutPermute_ScalarNoOp_Test.TestBody), [`TestBody`](view_sequence_test.cc.md#Simplify_RecursiveSimplify_Test.TestBody), [`TestBody`](transpose_primitive_test.cc.md#UpdateLayoutPermute_TensorNoOp_Test.TestBody), [`TestBody`](transpose_primitive_test.cc.md#UpdateLayoutPermute_TensorToTensor_Test.TestBody), [`TestBody`](view_sequence_test.cc.md#Simplify_RemoveNoOpPermute_Test.TestBody), [`ViewPrimitiveShlo`](transpose_primitive.cc.md#ViewPrimitiveShlo), [`operator()`](view_sequence.cc.md#ViewCacheKeyVisitor.operator), [`reshape`](decomposition.cc.md#ReshapeThenTranspose.reshape), [`MaybeMergeSequential`](view_sequence.cc.md#MaybeMergeSequential)

