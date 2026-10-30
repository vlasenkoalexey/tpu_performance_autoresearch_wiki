---
title: 'Module: csrc/ops/view_decomposition/reshape_primitive.h'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/reshape_primitive.h
status: fresh
symbol_base: cxx . . $ torch_tpu/ReshapePrimitive#
symbols:
  ReshapePrimitive: ''
  ReshapePrimitive.new_sizes: new_sizes.
  ReshapePrimitive.base_sizes: base_sizes.
---
# Module: [`csrc/ops/view_decomposition/reshape_primitive.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.h)

## Classes
### <a id="ReshapePrimitive"></a>`ReshapePrimitive`
- def: [`csrc/ops/view_decomposition/reshape_primitive.h:55`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.h#L55) — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- doc: A reshape primitive converts an N-dimensional tensor into an
- signature: `struct ReshapePrimitive`
- members:
  - <a id="ReshapePrimitive.base_sizes"></a>`base_sizes` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.h#L56)
  - <a id="ReshapePrimitive.new_sizes"></a>`new_sizes` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/reshape_primitive.h#L57)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`StridedLayout`](strided_layout.h.md#StridedLayout), [`operator<<`](reshape_primitive.cc.md#operator), [`UpdateLayout`](reshape_primitive.cc.md#UpdateLayout), [`ViewPrimitiveShlo`](reshape_primitive.cc.md#ViewPrimitiveShlo), [`Merge`](reshape_primitive.cc.md#Merge)
- used by: [`operator<<`](reshape_primitive.cc.md#operator), [`UpdateLayout`](reshape_primitive.cc.md#UpdateLayout), [`operator==`](view_sequence.cc.md#operator), [`operator==`](inversion.cc.md#operator), [`InvertViewSequence`](inversion.cc.md#InvertViewSequence), [`ViewPrimitive`](view_sequence.h.md#ViewPrimitive), [`operator<<`](view_sequence.cc.md#operator), [`BuildBodyStepOverlapping`](decomposition.cc.md#BuildBodyStepOverlapping), [`ViewPrimitiveShlo`](reshape_primitive.cc.md#ViewPrimitiveShlo), [`operator<<`](inversion.cc.md#operator), [`BuildBodyStepNonOverlapping`](decomposition.cc.md#BuildBodyStepNonOverlapping), [`BuildFinalDimension`](decomposition.cc.md#BuildFinalDimension), [`ReplaceStridedSlice`](inversion.cc.md#ReplaceStridedSlice), [`InvertAndPartition`](inversion.cc.md#InvertAndPartition), [`operator()`](view_sequence.cc.md#ViewCacheKeyVisitor.operator), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ImaginaryPartPreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_RealPartPreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ComplexF32ToComplexF64PreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ComplexF32ToComplexF64_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ComplexF64ToComplexF32PreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ComplexF64ToComplexF32_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ImaginaryPart_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_RealPart_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ViewAsRealPreserveBase_Test.TestBody), [`GetContiguousBaseShape`](decomposition.cc.md#GetContiguousBaseShape), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ViewAsComplexPreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ViewAsComplex_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ViewAsReal_Test.TestBody), [`CreateTrailingDimension`](decomposition.cc.md#CreateTrailingDimension), [`InverseViewPrimitive`](inversion.h.md#InverseViewPrimitive), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_BoolToLargerSizePreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_BoolToLargerSize_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_RealToRealLargerSizePreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_RealToRealLargerSize_Test.TestBody), [`RemoveExtraDim`](decomposition.cc.md#RemoveExtraDim), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_SliceTensorStridedNonContiguous_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_BoolToBytePreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_BoolToByte_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ByteToBoolPreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ByteToBool_Test.TestBody)  (+49 more)

