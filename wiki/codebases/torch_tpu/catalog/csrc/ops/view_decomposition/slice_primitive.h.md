---
title: 'Module: csrc/ops/view_decomposition/slice_primitive.h'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/slice_primitive.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  SlicePrimitive.slice_dims: SlicePrimitive#slice_dims.
  SlicePrimitive: SlicePrimitive#
  SliceDimension: SliceDimension#
  SliceDimension.stride: SliceDimension#stride.
  SliceDimension.start_index: SliceDimension#start_index.
  SliceDimension.limit_index: SliceDimension#limit_index.
---
# Module: [`csrc/ops/view_decomposition/slice_primitive.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.h)

## Classes
### <a id="SliceDimension"></a>`SliceDimension`
- def: [`csrc/ops/view_decomposition/slice_primitive.h:41`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.h#L41)
- doc: One dimension of a slice primitive.
- signature: `struct SliceDimension`
- members:
  - <a id="SliceDimension.limit_index"></a>`limit_index` — [`L45`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.h#L45) — The high index of the slice on the input axis (exclusive).
  - <a id="SliceDimension.start_index"></a>`start_index` — [`L43`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.h#L43) — The low index of the slice on the input axis (inclusive).
  - <a id="SliceDimension.stride"></a>`stride` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.h#L47) — The number of input rows to increment for each output index (min 1).
- uses (calls/refs, reference-scoped): [`operator<<`](slice_primitive.cc.md#operator), [`operator==`](slice_primitive.cc.md#operator)
- used by: [`operator<<`](slice_primitive.cc.md#operator), [`ViewPrimitiveShlo`](slice_primitive.cc.md#ViewPrimitiveShlo), [`UpdateLayout`](slice_primitive.cc.md#UpdateLayout), [`SlicePrimitive`](slice_primitive.h.md#SlicePrimitive), [`ReplaceStridedSlices`](inversion.cc.md#ReplaceStridedSlices), [`BuildBodyStepOverlapping`](decomposition.cc.md#BuildBodyStepOverlapping), [`BuildBodyStepNonOverlapping`](decomposition.cc.md#BuildBodyStepNonOverlapping), [`BuildFinalDimension`](decomposition.cc.md#BuildFinalDimension), [`ReplaceStridedSlice`](inversion.cc.md#ReplaceStridedSlice), [`InvertViewPrimitive`](inversion.cc.md#InvertViewPrimitive), [`InvertNonStridedSliceShlo`](inversion.cc.md#InvertNonStridedSliceShlo), [`operator==`](slice_primitive.cc.md#operator), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ImaginaryPartPreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_RealPartPreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ImaginaryPart_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_RealPart_Test.TestBody), [`CreateTrailingDimension`](decomposition.cc.md#CreateTrailingDimension), [`CheckSlice`](slice_primitive.cc.md#CheckSlice), [`ShiftInitialViewWindow`](decomposition.cc.md#ShiftInitialViewWindow), [`ShiftInitialViewWindow`](decomposition.cc.md#ShiftInitialViewWindow), [`Merge`](slice_primitive.cc.md#Merge), [`BuildHeadSliceToViewWindow`](decomposition.cc.md#BuildHeadSliceToViewWindow), [`ComputeNewSize`](slice_primitive.cc.md#ComputeNewSize)

### <a id="SlicePrimitive"></a>`SlicePrimitive`
- def: [`csrc/ops/view_decomposition/slice_primitive.h:67`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.h#L67) — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- doc: A slice primitive converts an N-dimensional tensor into another
- signature: `struct SlicePrimitive`
- members:
  - <a id="SlicePrimitive.slice_dims"></a>`slice_dims` — [`L68`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.h#L68) — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- uses (calls/refs, reference-scoped): [`StridedLayout`](strided_layout.h.md#StridedLayout), [`operator<<`](slice_primitive.cc.md#operator), [`ViewPrimitiveShlo`](slice_primitive.cc.md#ViewPrimitiveShlo), [`UpdateLayout`](slice_primitive.cc.md#UpdateLayout), [`SliceDimension`](slice_primitive.h.md#SliceDimension), [`Merge`](slice_primitive.cc.md#Merge)
- used by: [`operator<<`](slice_primitive.cc.md#operator), [`operator==`](view_sequence.cc.md#operator), [`ViewPrimitiveShlo`](slice_primitive.cc.md#ViewPrimitiveShlo), [`operator==`](inversion.cc.md#operator), [`UpdateLayout`](slice_primitive.cc.md#UpdateLayout), [`ViewPrimitive`](view_sequence.h.md#ViewPrimitive), [`ReplaceStridedSlices`](inversion.cc.md#ReplaceStridedSlices), [`operator<<`](view_sequence.cc.md#operator), [`BuildBodyStepOverlapping`](decomposition.cc.md#BuildBodyStepOverlapping), [`operator<<`](inversion.cc.md#operator), [`BuildBodyStepNonOverlapping`](decomposition.cc.md#BuildBodyStepNonOverlapping), [`BuildFinalDimension`](decomposition.cc.md#BuildFinalDimension), [`ReplaceStridedSlice`](inversion.cc.md#ReplaceStridedSlice), [`InvertViewPrimitive`](inversion.cc.md#InvertViewPrimitive), [`InvertAndPartition`](inversion.cc.md#InvertAndPartition), [`InvertNonStridedSliceShlo`](inversion.cc.md#InvertNonStridedSliceShlo), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ImaginaryPartPreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_RealPartPreserveBase_Test.TestBody), [`operator==`](inversion.cc.md#operator), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_ImaginaryPart_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_RealPart_Test.TestBody), [`CreateTrailingDimension`](decomposition.cc.md#CreateTrailingDimension), [`InverseViewPrimitive`](inversion.h.md#InverseViewPrimitive), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_SliceTensorStridedNonContiguous_Test.TestBody), [`InvertViewPrimitive`](inversion.cc.md#InvertViewPrimitive), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_SliceTensorHighPreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_SliceTensorHigh_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_SliceTensorStridedContiguousPreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_SliceTensorStridedContiguous_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_SliceTensorStridedWithLowAndHighIndexPreserveBase_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_SliceTensorStridedWithLowAndHighIndex_Test.TestBody), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_SliceTensorLow_Test.TestBody), [`CheckSlice`](slice_primitive.cc.md#CheckSlice), [`ShiftInitialViewWindow`](decomposition.cc.md#ShiftInitialViewWindow), [`Merge`](slice_primitive.cc.md#Merge), [`TestBody`](view_sequence_test.cc.md#Simplify_NothingToSimplify_Test.TestBody), [`TestBody`](slice_primitive_test.cc.md#MergeSlice_ValidMerge_Test.TestBody), [`BuildHeadPad`](decomposition.cc.md#BuildHeadPad), [`CheckSliceMerge`](slice_primitive.cc.md#CheckSliceMerge), [`TestBody`](slice_primitive_test.cc.md#UpdateLayoutSlice_ScalarNoOp_Test.TestBody)  (+8 more)

