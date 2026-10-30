---
title: 'Module: csrc/ops/view_decomposition/pad_primitive.h'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/pad_primitive.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  PadPrimitive.pad_dims: PadPrimitive#pad_dims.
  PadPrimitive: PadPrimitive#
  PadDimension: PadDimension#
  PadDimension.interior_padding: PadDimension#interior_padding.
  PadDimension.high_padding: PadDimension#high_padding.
  PadDimension.low_padding: PadDimension#low_padding.
---
# Module: [`csrc/ops/view_decomposition/pad_primitive.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.h)

## Classes
### <a id="PadDimension"></a>`PadDimension`
- def: [`csrc/ops/view_decomposition/pad_primitive.h:61`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.h#L61)
- doc: One dimension of a pad primitive.
- signature: `struct PadDimension`
- members:
  - <a id="PadDimension.high_padding"></a>`high_padding` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.h#L65) — The number of rows to add to above the last row in the input dimension.
  - <a id="PadDimension.interior_padding"></a>`interior_padding` — [`L67`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.h#L67) — The number of rows to add between each element in the input dimension.
  - <a id="PadDimension.low_padding"></a>`low_padding` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.h#L63) — The number of rows to add to below the first row in the input dimension.
- uses (calls/refs, reference-scoped): [`operator<<`](pad_primitive.cc.md#operator), [`operator==`](pad_primitive.cc.md#operator)
- used by: [`operator<<`](pad_primitive.cc.md#operator), [`BuildBodyStepOverlapping`](decomposition.cc.md#BuildBodyStepOverlapping), [`BuildBodyStepNonOverlapping`](decomposition.cc.md#BuildBodyStepNonOverlapping), [`BuildFinalDimension`](decomposition.cc.md#BuildFinalDimension), [`UpdateLayout`](pad_primitive.cc.md#UpdateLayout), [`ReplaceStridedSlice`](inversion.cc.md#ReplaceStridedSlice), [`InvertViewPrimitive`](inversion.cc.md#InvertViewPrimitive), [`operator==`](pad_primitive.cc.md#operator), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_SliceTensorStridedNonContiguous_Test.TestBody), [`PadPrimitive`](pad_primitive.h.md#PadPrimitive), [`ViewPrimitiveShlo`](pad_primitive.cc.md#ViewPrimitiveShlo), [`ShiftInitialViewWindow`](decomposition.cc.md#ShiftInitialViewWindow), [`CheckPad`](pad_primitive.cc.md#CheckPad), [`ShiftInitialViewWindow`](decomposition.cc.md#ShiftInitialViewWindow), [`BuildHeadPad`](decomposition.cc.md#BuildHeadPad), [`operator()`](view_sequence.cc.md#ViewCacheKeyVisitor.operator)

### <a id="PadPrimitive"></a>`PadPrimitive`
- def: [`csrc/ops/view_decomposition/pad_primitive.h:85`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.h#L85)
- doc: A pad primitive converts an N-dimensional tensor into another
- signature: `struct PadPrimitive`
- members:
  - <a id="PadPrimitive.pad_dims"></a>`pad_dims` — [`L86`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.h#L86)
- uses (calls/refs, reference-scoped): [`StridedLayout`](strided_layout.h.md#StridedLayout), [`operator<<`](pad_primitive.cc.md#operator), [`UpdateLayout`](pad_primitive.cc.md#UpdateLayout), [`operator==`](pad_primitive.cc.md#operator), [`ViewPrimitiveShlo`](pad_primitive.cc.md#ViewPrimitiveShlo), [`PadDimension`](pad_primitive.h.md#PadDimension)
- used by: [`operator<<`](pad_primitive.cc.md#operator), [`operator==`](view_sequence.cc.md#operator), [`DecomposeIntoViewSequence`](decomposition.cc.md#DecomposeIntoViewSequence), [`ViewPrimitive`](view_sequence.h.md#ViewPrimitive), [`operator<<`](view_sequence.cc.md#operator), [`BuildBodyStepOverlapping`](decomposition.cc.md#BuildBodyStepOverlapping), [`BuildBodyStepNonOverlapping`](decomposition.cc.md#BuildBodyStepNonOverlapping), [`BuildFinalDimension`](decomposition.cc.md#BuildFinalDimension), [`UpdateLayout`](pad_primitive.cc.md#UpdateLayout), [`ReplaceStridedSlice`](inversion.cc.md#ReplaceStridedSlice), [`operator==`](pad_primitive.cc.md#operator), [`InvertViewPrimitive`](inversion.cc.md#InvertViewPrimitive), [`TestBody`](inversion_test.cc.md#ComputeInverseViewOperation_SliceTensorStridedNonContiguous_Test.TestBody), [`TestBody`](view_sequence_test.cc.md#SymbolicViewPrimitive_PadViewCacheKeys_Test.TestBody), [`BuildHeadFlatten`](decomposition.cc.md#BuildHeadFlatten), [`ViewPrimitiveShlo`](pad_primitive.cc.md#ViewPrimitiveShlo), [`CheckPad`](pad_primitive.cc.md#CheckPad), [`BuildHeadPad`](decomposition.cc.md#BuildHeadPad), [`TestBody`](pad_primitive_test.cc.md#UpdateLayoutPad_ScalarNoOp_Test.TestBody), [`operator()`](view_sequence.cc.md#ViewCacheKeyVisitor.operator), [`TestBody`](pad_primitive_test.cc.md#UpdateLayoutPad_TensorNoOp_Test.TestBody), [`TestBody`](pad_primitive_test.cc.md#UpdateLayoutPad_TensorToTensor_Test.TestBody), [`TestBody`](view_sequence_test.cc.md#Simplify_RemoveNoOpPad_Test.TestBody), [`MaybeMergeSequential`](view_sequence.cc.md#MaybeMergeSequential)

