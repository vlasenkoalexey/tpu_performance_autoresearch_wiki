---
title: 'Module: csrc/ops/view_decomposition/broadcast_primitive.h'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/broadcast_primitive.h
status: fresh
symbol_base: cxx . . $ torch_tpu/BroadcastPrimitive#
symbols:
  BroadcastPrimitive: ''
  BroadcastPrimitive.broadcast_dimensions: broadcast_dimensions.
  BroadcastPrimitive.new_sizes: new_sizes.
  BroadcastPrimitive.base_shape: base_shape.
---
# Module: [`csrc/ops/view_decomposition/broadcast_primitive.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/broadcast_primitive.h)

## Classes
### <a id="BroadcastPrimitive"></a>`BroadcastPrimitive`
- def: [`csrc/ops/view_decomposition/broadcast_primitive.h:51`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/broadcast_primitive.h#L51)
- doc: A broadcast primitive converts an M-dimensional tensor into an N-dimensional
- signature: `struct BroadcastPrimitive`
- members:
  - <a id="BroadcastPrimitive.base_shape"></a>`base_shape` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/broadcast_primitive.h#L53) — The shape of the input tensor.
  - <a id="BroadcastPrimitive.broadcast_dimensions"></a>`broadcast_dimensions` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/broadcast_primitive.h#L59) — A mapping from input dimensions to output dimensions.
  - <a id="BroadcastPrimitive.new_sizes"></a>`new_sizes` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/broadcast_primitive.h#L55) — The shape of the output tensor.
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`StridedLayout`](strided_layout.h.md#StridedLayout), [`operator<<`](broadcast_primitive.cc.md#operator), [`ViewPrimitiveShlo`](broadcast_primitive.cc.md#ViewPrimitiveShlo), [`UpdateLayout`](broadcast_primitive.cc.md#UpdateLayout)
- used by: [`operator<<`](broadcast_primitive.cc.md#operator), [`operator==`](view_sequence.cc.md#operator), [`ViewPrimitive`](view_sequence.h.md#ViewPrimitive), [`operator<<`](view_sequence.cc.md#operator), [`ViewPrimitiveShlo`](broadcast_primitive.cc.md#ViewPrimitiveShlo), [`UpdateLayout`](broadcast_primitive.cc.md#UpdateLayout), [`RemoveExtraDim`](decomposition.cc.md#RemoveExtraDim), [`InvertViewPrimitive`](inversion.cc.md#InvertViewPrimitive), [`operator()`](view_sequence.cc.md#ViewCacheKeyVisitor.operator), [`TestBody`](view_sequence_test.cc.md#SymbolicViewPrimitive_BroadcastViewCacheKeys_Test.TestBody), [`CheckBroadcast`](broadcast_primitive.cc.md#CheckBroadcast), [`BuildTailBroadcast`](decomposition.cc.md#BuildTailBroadcast), [`TestBody`](view_sequence_test.cc.md#Simplify_NothingToSimplify_Test.TestBody), [`CheckBroadcast`](broadcast_primitive.cc.md#CheckBroadcast), [`TestBody`](broadcast_primitive_test.cc.md#UpdateLayoutBroadcast_ScalarNoOp_Test.TestBody), [`TestBody`](broadcast_primitive_test.cc.md#UpdateLayoutBroadcast_ScalarToTensor_Test.TestBody), [`TestBody`](broadcast_primitive_test.cc.md#UpdateLayoutBroadcast_TensorNoOp_Test.TestBody), [`TestBody`](broadcast_primitive_test.cc.md#UpdateLayoutBroadcast_TensorToTensor_Test.TestBody), [`CheckBroadcast`](broadcast_primitive.cc.md#CheckBroadcast), [`TestBody`](view_sequence_test.cc.md#Simplify_RemoveNoOpBroadcast_Test.TestBody), [`TestBody`](view_sequence_test.cc.md#ViewPrimitiveEquality_BroadcastPrimitive_Test.TestBody), [`IndexedStridedDimensionSortCriterion`](decomposition.cc.md#IndexedStridedDimensionSortCriterion), [`MaybeMergeSequential`](view_sequence.cc.md#MaybeMergeSequential)

