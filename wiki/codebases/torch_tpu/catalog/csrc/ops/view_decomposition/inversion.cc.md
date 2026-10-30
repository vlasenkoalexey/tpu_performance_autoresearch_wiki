---
title: 'Module: csrc/ops/view_decomposition/inversion.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/inversion.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ComputeInverseViewOperation: ComputeInverseViewOperation(994ffbdf54b563cc).
  InverseViewOperationShlo: InverseViewOperationShlo(cca7205e746a6003).
  operator: '`operator==`(85a4a28f8b5c1769).'
  InvertViewSequence: InvertViewSequence(73447a33d2332c5c).
  ReplaceStridedSlices: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/ReplaceStridedSlices(b330294f58b69dae).'
  ReplaceStridedSlice: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/ReplaceStridedSlice(b572031640850ae8).'
  InvertViewPrimitive: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/InvertViewPrimitive(3e488ef0cb80dc90).'
  InvertAndPartition: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/InvertAndPartition(d9691f5df7c5055).'
  InvertNonStridedSliceShlo: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/InvertNonStridedSliceShlo(8c616828421deefb).'
  CalculatePostBitcastBaseToView: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/CalculatePostBitcastBaseToView(70a180e30e0326d).'
  GetBitcastTransforms: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/GetBitcastTransforms(dd444a9b92bf1119).'
  UpdateLayout: UpdateLayout(ac2f3797c977ba0e).
  GetBitcastSequenceToWritable: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/GetBitcastSequenceToWritable(e99a5f1e87a8b9bc).'
  InverseViewPrimitiveShlo: InverseViewPrimitiveShlo(33551809f0760975).
  InvertSingleDimSliceViaConcat: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/InvertSingleDimSliceViaConcat(c95a1199cf7c582a).'
  InverseViewSequenceShlo: InverseViewSequenceShlo(eee6e3a8044727ba).
  GetCurrentDimensions: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/GetCurrentDimensions(f430b3f36ae2023a).'
  BitcastTransforms: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/BitcastTransforms#'
  BitcastTransforms.writable_dtype: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/BitcastTransforms#writable_dtype.'
  BitcastTransforms.invertible_bitcast: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/BitcastTransforms#invertible_bitcast.'
  BitcastTransforms.base_dtype_after_transform: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/BitcastTransforms#base_dtype_after_transform.'
  BitcastTransforms.bitcast_view: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/BitcastTransforms#bitcast_view.'
  BitcastTransforms.base_transform: '`$anonymous_namespace_csrc/ops/view_decomposition/inversion.cc`/BitcastTransforms#base_transform.'
---
# Module: [`csrc/ops/view_decomposition/inversion.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc)

## Classes
### <a id="BitcastTransforms"></a>`BitcastTransforms`
- def: [`csrc/ops/view_decomposition/inversion.cc:710`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L710)
- signature: `struct BitcastTransforms`
- members:
  - <a id="BitcastTransforms.base_dtype_after_transform"></a>`base_dtype_after_transform` — [`L712`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L712)
  - <a id="BitcastTransforms.base_transform"></a>`base_transform` — [`L711`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L711)
  - <a id="BitcastTransforms.bitcast_view"></a>`bitcast_view` — [`L713`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L713)
  - <a id="BitcastTransforms.invertible_bitcast"></a>`invertible_bitcast` — [`L715`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L715)
  - <a id="BitcastTransforms.writable_dtype"></a>`writable_dtype` — [`L714`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L714)
- uses (calls/refs, reference-scoped): [`ViewSequence`](view_sequence.h.md#ViewSequence)
- used by: [`GetBitcastTransforms`](inversion.cc.md#GetBitcastTransforms)

## Functions
- `CalculatePostBitcastBaseToView(const StridedLayout& base_layout, const StridedLayout& view_layout, ViewSequenceSpan bitcast_view, ViewSequence&& invertible_bitcast, mlir::ElementType writable_dtype, bool is_conj)` — [`L805`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L805) — Computes a bitcast-free view sequence from the post-bitcast base to the
- <a id="CalculatePostBitcastBaseToView"></a>`CalculatePostBitcastBaseToView(const StridedLayout& base_layout, const StridedLayout& view_layout, ViewSequenceSpan bitcast_view, ViewSequence&& invertible_bitcast, mlir::ElementType writable_dtype, bool is_conj)` — [`L805`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L805) — Computes a bitcast-free view sequence from the post-bitcast base to the
- <a id="ComputeInverseViewOperation"></a>`ComputeInverseViewOperation(absl::Span<const int64_t> contiguous_base_shape, mlir::ElementType contiguous_base_dtype, const StridedLayout& view_layout, mlir::ElementType view_dtype, bool is_conj, bool preserve_base)` — [`L903`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L903) — Computes the inverse view operation necessary to produce an updated — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- `GetBitcastSequenceToWritable(mlir::ElementType from_dtype, mlir::ElementType to_dtype, StridedLayout& layout)` — [`L536`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L536) — Gets a view sequence to bitcast from the given dtype to a writable dtype.
- <a id="GetBitcastSequenceToWritable"></a>`GetBitcastSequenceToWritable(mlir::ElementType from_dtype, mlir::ElementType to_dtype, StridedLayout& layout)` — [`L536`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L536) — Gets a view sequence to bitcast from the given dtype to a writable dtype.
- <a id="GetBitcastTransforms"></a>`GetBitcastTransforms(absl::Span<const int64_t> contiguous_base_shape, mlir::ElementType contiguous_base_dtype, const StridedLayout& view_layout, mlir::ElementType view_dtype)` — [`L717`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L717)
- <a id="GetCurrentDimensions"></a>`GetCurrentDimensions(const StridedLayout& layout)` — [`L205`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L205)
- <a id="InverseViewOperationShlo"></a>`InverseViewOperationShlo(mlir::MlirOp contiguous_base, mlir::MlirOp mutated_view, const InverseViewOperation& inverse_view_operation)` — [`L953`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L953) — Applies the inverse view operation to the mutated view, resulting in a — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- <a id="InverseViewPrimitiveShlo"></a>`InverseViewPrimitiveShlo(mlir::MlirOp input, const InverseViewPrimitive& primitive)` — [`L461`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L461)
- <a id="InverseViewSequenceShlo"></a>`InverseViewSequenceShlo(mlir::MlirOp mutated_view, InverseViewSequenceSpan inverted_view_sequence)` — [`L521`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L521) — Applies the inverse view sequence to the mutated view, resulting in a
- <a id="InvertAndPartition"></a>`InvertAndPartition(StridedLayout& base_layout, ViewSequence& base_transform, ViewSequence&& base_to_view, Shape& final_shape, bool preserve_base)` — [`L853`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L853) — Given a base layout, a base transform, and a view sequence to some view
- `InvertAndPartition(StridedLayout& base_layout, ViewSequence& base_transform, ViewSequence&& base_to_view, Shape& final_shape, bool preserve_base)` — [`L853`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L853) — Given a base layout, a base transform, and a view sequence to some view
- <a id="InvertNonStridedSliceShlo"></a>`InvertNonStridedSliceShlo(mlir::MlirOp pre_slice_value, mlir::MlirOp post_slice_value, const SlicePrimitive& slice)` — [`L651`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L651)
- <a id="InvertSingleDimSliceViaConcat"></a>`InvertSingleDimSliceViaConcat(mlir::MlirOp pre_slice_value, mlir::MlirOp post_slice_value, int64_t active_dim, int64_t start_index, int64_t limit_index, const mlir::stablehlo::Dimensions& pre_slice_dims)` — [`L613`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L613) — Inverts a non-strided slice update along a single dimension by concatenating
- `InvertSingleDimSliceViaConcat(mlir::MlirOp pre_slice_value, mlir::MlirOp post_slice_value, int64_t active_dim, int64_t start_index, int64_t limit_index, const mlir::stablehlo::Dimensions& pre_slice_dims)` — [`L613`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L613) — Inverts a non-strided slice update along a single dimension by concatenating
- `InvertViewPrimitive(const ReshapePrimitive& reshape, const StridedLayout& layout_before)` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L64) — Computes the inverse of a reshape primitive.
- `InvertViewPrimitive(const ComplexToRealBitcast& complex_to_real, const StridedLayout& layout_before)` — [`L176`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L176)
- `InvertViewPrimitive(const ViewPrimitive& primitive, const StridedLayout& layout_before)` — [`L196`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L196) — Computes the inverse of a view primitive.
- `InvertViewPrimitive(const BroadcastPrimitive& broadcast, const StridedLayout& layout_before)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L100) — Error message only, for use with std::visit.
- `InvertViewPrimitive(const SlicePrimitive& slice, const StridedLayout& layout_before)` — [`L120`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L120) — Error message only, for use with std::visit.
- `InvertViewPrimitive(const UnfoldPrimitive& unfold, const StridedLayout& layout_before)` — [`L110`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L110) — Error message only, for use with std::visit.
- <a id="InvertViewPrimitive"></a>`InvertViewPrimitive(const PadPrimitive& pad, const StridedLayout& layout_before)` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L135) — Computes the inverse of a pad primitive.
- `InvertViewPrimitive(const TransposePrimitive& transpose, const StridedLayout& layout_before)` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L74) — Computes the inverse of a permute primitive.
- `InvertViewPrimitive(const ViewAsComplex& view_as_complex, const StridedLayout& layout_before)` — [`L187`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L187)
- `InvertViewPrimitive(const RealToRealBitcast& real_to_real, const StridedLayout& layout_before)` — [`L165`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L165)
- `InvertViewPrimitive(const ConjPrimitive& conj, const StridedLayout& layout_before)` — [`L128`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L128)
- `InvertViewSequence(StridedLayout& layout, absl::Span<const ViewPrimitive> view_sequence)` — [`L470`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L470) — Constructs the inverse of a view sequence, which will reconstruct the
- <a id="InvertViewSequence"></a>`InvertViewSequence(StridedLayout& layout, absl::Span<const ViewPrimitive> view_sequence)` — [`L470`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L470) — Constructs the inverse of a view sequence, which will reconstruct the — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- `ReplaceStridedSlice(const SlicePrimitive& strided_slice, StridedLayout& current_layout, ViewSequence& result)` — [`L216`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L216) — Replaces a strided slice with an equivalent sequence of pad, reshape,
- <a id="ReplaceStridedSlice"></a>`ReplaceStridedSlice(const SlicePrimitive& strided_slice, StridedLayout& current_layout, ViewSequence& result)` — [`L216`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L216) — Replaces a strided slice with an equivalent sequence of pad, reshape,
- `ReplaceStridedSlices(absl::Span<const int64_t> contiguous_base_shape, ViewSequence& view_sequence)` — [`L312`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L312) — If a view sequence contains a strided slice (stride > 1 on at least one
- <a id="ReplaceStridedSlices"></a>`ReplaceStridedSlices(absl::Span<const int64_t> contiguous_base_shape, ViewSequence& view_sequence)` — [`L312`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L312) — If a view sequence contains a strided slice (stride > 1 on at least one
- <a id="UpdateLayout"></a>`UpdateLayout(StridedLayout& layout, const InverseViewPrimitive& primitive)` — [`L447`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L447) — Updates the layout to reflect the effect of applying the given inverse view
- `operator<<(std::ostream& os, const InverseViewPrimitive& primitive)` — [`L393`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L393) — Formats the inverse view primitive as one of:
- `operator<<(std::ostream& os, const InverseViewStage& stage)` — [`L437`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L437)
- <a id="operator"></a>`operator==(const InverseViewPrimitive& lhs, const InverseViewPrimitive& rhs)` — [`L360`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L360)
- `operator==(const InverseViewStage& lhs, const InverseViewStage& rhs)` — [`L420`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/inversion.cc#L420)

