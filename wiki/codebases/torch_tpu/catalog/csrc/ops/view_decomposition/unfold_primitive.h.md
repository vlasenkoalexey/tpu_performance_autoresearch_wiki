---
title: 'Module: csrc/ops/view_decomposition/unfold_primitive.h'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/unfold_primitive.h
status: fresh
symbol_base: cxx . . $ torch_tpu/UnfoldPrimitive#
symbols:
  UnfoldPrimitive.window_size: window_size.
  UnfoldPrimitive: ''
  UnfoldPrimitive.start_index: start_index.
  UnfoldPrimitive.limit_index: limit_index.
  UnfoldPrimitive.window_stride: window_stride.
---
# Module: [`csrc/ops/view_decomposition/unfold_primitive.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.h)

## Classes
### <a id="UnfoldPrimitive"></a>`UnfoldPrimitive`
- def: [`csrc/ops/view_decomposition/unfold_primitive.h:55`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.h#L55)
- doc: An unfold primitive converts a tensor of shape (..., 1, M) with strides
- signature: `struct UnfoldPrimitive`
- members:
  - <a id="UnfoldPrimitive.limit_index"></a>`limit_index` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.h#L57)
  - <a id="UnfoldPrimitive.start_index"></a>`start_index` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.h#L56)
  - <a id="UnfoldPrimitive.window_size"></a>`window_size` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.h#L59)
  - <a id="UnfoldPrimitive.window_stride"></a>`window_stride` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.h#L58)
- uses (calls/refs, reference-scoped): [`StridedLayout`](strided_layout.h.md#StridedLayout), [`UpdateLayout`](unfold_primitive.cc.md#UpdateLayout), [`operator<<`](unfold_primitive.cc.md#operator), [`ViewPrimitiveShlo`](unfold_primitive.cc.md#ViewPrimitiveShlo)
- used by: [`operator==`](view_sequence.cc.md#operator), [`ViewPrimitive`](view_sequence.h.md#ViewPrimitive), [`operator<<`](view_sequence.cc.md#operator), [`BuildBodyStepOverlapping`](decomposition.cc.md#BuildBodyStepOverlapping), [`UpdateLayout`](unfold_primitive.cc.md#UpdateLayout), [`operator<<`](unfold_primitive.cc.md#operator), [`InvertViewPrimitive`](inversion.cc.md#InvertViewPrimitive), [`TestBody`](view_sequence_test.cc.md#SymbolicViewPrimitive_UnsupportedViewCacheKeys_Test.TestBody), [`ShiftInitialViewWindow`](decomposition.cc.md#ShiftInitialViewWindow), [`ViewPrimitiveShlo`](unfold_primitive.cc.md#ViewPrimitiveShlo), [`CheckUnfold`](unfold_primitive.cc.md#CheckUnfold), [`CheckUnfold`](unfold_primitive.cc.md#CheckUnfold), [`CheckUnfold`](unfold_primitive.cc.md#CheckUnfold), [`TestBody`](unfold_primitive_test.cc.md#UpdateLayoutUnfold_TensorNoOp_Test.TestBody), [`TestBody`](unfold_primitive_test.cc.md#UpdateLayoutUnfold_TensorValidUnfold_Test.TestBody), [`TestBody`](unfold_primitive_test.cc.md#UpdateLayoutUnfold_UnfoldWithStrideOnLastDimension_Test.TestBody), [`TestBody`](view_sequence_test.cc.md#Simplify_RemoveNoOpUnfold_Test.TestBody), [`MaybeMergeSequential`](view_sequence.cc.md#MaybeMergeSequential)

