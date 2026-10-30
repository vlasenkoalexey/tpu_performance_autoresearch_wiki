---
title: 'Module: csrc/ops/view_decomposition/decomposition.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/decomposition.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  DecomposeIntoViewSequence: DecomposeIntoViewSequence(43e37ce098563dea).
  CheckViewPreconditions: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/CheckViewPreconditions(dec54efcb05cc743).'
  BuildBodyStepOverlapping: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildBodyStepOverlapping(481a459e6a31f54d).'
  BuildBodyStepNonOverlapping: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildBodyStepNonOverlapping(481a459e6a31f54d).'
  BuildFinalDimension: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildFinalDimension(a21825717bd3db81).'
  BuildHead: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildHead(9a73fef3c2c5c89b).'
  GetContiguousBaseShape: GetContiguousBaseShape(1fdc47d6a060d955).
  CreateTrailingDimension: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/CreateTrailingDimension(e74d703282c03994).'
  RemoveExtraDim: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/RemoveExtraDim(402f9cce1831f915).'
  BuildTailNoBroadcast: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildTailNoBroadcast(cbcae1e148272ecc).'
  BuildTail: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildTail(c156eef2bc2087ce).'
  MaybeAddComplexToRealBitcast: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/MaybeAddComplexToRealBitcast(2695f2186d6ca88a).'
  BuildHeadFlatten: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildHeadFlatten(76edb2fdca4e68c8).'
  ShiftInitialViewWindow: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/ShiftInitialViewWindow(3ae9be5e510ccc2d).'
  MaybeAddViewAsComplex: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/MaybeAddViewAsComplex(d043afb221544f55).'
  BuildTailBroadcast: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildTailBroadcast(3020a73982a8de80).'
  MaybeAddRealToRealBitcast: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/MaybeAddRealToRealBitcast(5c3dac778bd7b65a).'
  BuildBodyStep: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildBodyStep(e392ed4d4f7649c).'
  BuildHeadPad: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildHeadPad(e50519eb6a40a175).'
  BuildHeadBitcast: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildHeadBitcast(57434e58ed54df96).'
  BuildHeadSliceToViewWindow: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildHeadSliceToViewWindow(53b6f045d8c6d50f).'
  IndexedStridedDimensionSortCriterion: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/IndexedStridedDimensionSortCriterion(50f27ea5650e3d64).'
  IndexedStridedDimension.size: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/IndexedStridedDimension#size.'
  IsRowMajorIgnoringTrivialDimensions: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/IsRowMajorIgnoringTrivialDimensions(80f21816c8c14a36).'
  IndexedStridedDimension.stride: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/IndexedStridedDimension#stride.'
  IndexedStridedDimension.index: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/IndexedStridedDimension#index.'
  ReshapeThenTranspose.reshape: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/ReshapeThenTranspose#reshape.'
  IndexedStridedDimension: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/IndexedStridedDimension#'
  BuildHeadResult.view_widths: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildHeadResult#view_widths.'
  ReshapeThenTranspose: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/ReshapeThenTranspose#'
  ReshapeThenTranspose.transpose: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/ReshapeThenTranspose#transpose.'
  BuildHeadResult: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildHeadResult#'
  BuildHeadResult.head_sequence: '`$anonymous_namespace_csrc/ops/view_decomposition/decomposition.cc`/BuildHeadResult#head_sequence.'
---
# Module: [`csrc/ops/view_decomposition/decomposition.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc)

## Classes
### <a id="BuildHeadResult"></a>`BuildHeadResult`
- def: [`csrc/ops/view_decomposition/decomposition.cc:603`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L603)
- doc: The result of building the head of the decomposition.
- signature: `struct BuildHeadResult`
- members:
  - <a id="BuildHeadResult.head_sequence"></a>`head_sequence` — [`L604`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L604)
  - <a id="BuildHeadResult.view_widths"></a>`view_widths` — [`L605`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L605)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`ViewSequence`](view_sequence.h.md#ViewSequence)

### <a id="IndexedStridedDimension"></a>`IndexedStridedDimension`
- def: [`csrc/ops/view_decomposition/decomposition.cc:119`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L119)
- doc: A strided dimension, with the index it originated from. Used for constructing
- signature: `struct IndexedStridedDimension`
- members:
  - <a id="IndexedStridedDimension.index"></a>`index` — [`L120`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L120)
  - <a id="IndexedStridedDimension.size"></a>`size` — [`L121`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L121)
  - <a id="IndexedStridedDimension.stride"></a>`stride` — [`L122`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L122)
- used by: [`BuildTailNoBroadcast`](decomposition.cc.md#BuildTailNoBroadcast), [`BuildTail`](decomposition.cc.md#BuildTail), [`BuildTailBroadcast`](decomposition.cc.md#BuildTailBroadcast), [`IndexedStridedDimensionSortCriterion`](decomposition.cc.md#IndexedStridedDimensionSortCriterion)

### <a id="ReshapeThenTranspose"></a>`ReshapeThenTranspose`
- def: [`csrc/ops/view_decomposition/decomposition.cc:219`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L219)
- doc: If the view has no expanded dimensions, but the nontrivial dimensions are not
- signature: `struct ReshapeThenTranspose`
- members:
  - <a id="ReshapeThenTranspose.reshape"></a>`reshape` — [`L220`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L220)
  - <a id="ReshapeThenTranspose.transpose"></a>`transpose` — [`L221`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L221)
- uses (calls/refs, reference-scoped): [`ReshapePrimitive`](reshape_primitive.h.md#ReshapePrimitive), [`TransposePrimitive`](transpose_primitive.h.md#TransposePrimitive)
- used by: [`BuildTailNoBroadcast`](decomposition.cc.md#BuildTailNoBroadcast)

## Functions
- <a id="BuildBodyStep"></a>`BuildBodyStep(StridedLayout& head_layout, const StridedLayout& tail_layout, const Dimensions& view_widths, ViewSequence& result, const int64_t head_pad_index)` — [`L1059`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L1059) — Adds one reshape and either a slice or an unfold to satisfy one or more
- `BuildBodyStep(StridedLayout& head_layout, const StridedLayout& tail_layout, const Dimensions& view_widths, ViewSequence& result, const int64_t head_pad_index)` — [`L1059`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L1059) — Adds one reshape and either a slice or an unfold to satisfy one or more
- `BuildBodyStepNonOverlapping(StridedLayout& head_layout, const StridedLayout& tail_layout, const Dimensions& view_widths, ViewSequence& result, const int64_t head_pad_index)` — [`L874`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L874) — Satisfies one or more non-overlapping tail dimensions in the tail layout
- <a id="BuildBodyStepNonOverlapping"></a>`BuildBodyStepNonOverlapping(StridedLayout& head_layout, const StridedLayout& tail_layout, const Dimensions& view_widths, ViewSequence& result, const int64_t head_pad_index)` — [`L874`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L874) — Satisfies one or more non-overlapping tail dimensions in the tail layout — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- <a id="BuildBodyStepOverlapping"></a>`BuildBodyStepOverlapping(StridedLayout& head_layout, const StridedLayout& tail_layout, const Dimensions& view_widths, ViewSequence& result, const int64_t head_pad_index)` — [`L1010`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L1010) — Satisfies one overlapping tail dimension in the tail layout using exactly one — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- `BuildBodyStepOverlapping(StridedLayout& head_layout, const StridedLayout& tail_layout, const Dimensions& view_widths, ViewSequence& result, const int64_t head_pad_index)` — [`L1010`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L1010) — Satisfies one overlapping tail dimension in the tail layout using exactly one
- `BuildFinalDimension(StridedLayout& head_layout, const StridedLayout& tail_layout, ViewSequence& result, const int64_t head_pad_index)` — [`L1117`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L1117) — If the last (most-minor) dimension has stride > 1, then we need to do either
- <a id="BuildFinalDimension"></a>`BuildFinalDimension(StridedLayout& head_layout, const StridedLayout& tail_layout, ViewSequence& result, const int64_t head_pad_index)` — [`L1117`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L1117) — If the last (most-minor) dimension has stride > 1, then we need to do either — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- <a id="BuildHead"></a>`BuildHead(StridedLayout& head_layout, const mlir::ElementType continuous_base_dtype, StridedLayout& tail_layout, const mlir::ElementType view_dtype)` — [`L614`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L614) — Builds the first ops in the decomposition, which restructure an
- <a id="BuildHeadBitcast"></a>`BuildHeadBitcast(StridedLayout& head_layout, const mlir::ElementType contiguous_base_dtype, StridedLayout& tail_layout, const mlir::ElementType view_dtype)` — [`L580`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L580)
- `BuildHeadBitcast(StridedLayout& head_layout, const mlir::ElementType contiguous_base_dtype, StridedLayout& tail_layout, const mlir::ElementType view_dtype)` — [`L580`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L580)
- <a id="BuildHeadFlatten"></a>`BuildHeadFlatten(const StridedLayout& head_layout)` — [`L311`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L311) — Builds the first op in the decomposition, which may flatten the head layout
- <a id="BuildHeadPad"></a>`BuildHeadPad(const StridedLayout& head_layout, const int64_t required_storage_capacity)` — [`L333`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L333) — Builds the second op in the decomposition, which may pad the head layout
- <a id="BuildHeadSliceToViewWindow"></a>`BuildHeadSliceToViewWindow(const StridedLayout& head_layout, const int64_t storage_offset, const int64_t view_width)` — [`L354`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L354) — Builds the third op in the decomposition, which may slice the head layout
- `BuildTail(StridedLayout& tail_layout)` — [`L253`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L253)
- <a id="BuildTail"></a>`BuildTail(StridedLayout& tail_layout)` — [`L253`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L253)
- <a id="BuildTailBroadcast"></a>`BuildTailBroadcast(StridedLayout& tail_layout, absl::Span<const IndexedStridedDimension> sorted_dimensions)` — [`L156`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L156) — Builds the last op in a decomposition with any stride == 0, size > 1
- <a id="BuildTailNoBroadcast"></a>`BuildTailNoBroadcast(StridedLayout& tail_layout, absl::Span<const IndexedStridedDimension> sorted_dimensions)` — [`L224`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L224)
- <a id="CheckViewPreconditions"></a>`CheckViewPreconditions(absl::Span<const int64_t> contiguous_base_shape, const mlir::ElementType contiguous_base_dtype, const StridedLayout& view_layout, const mlir::ElementType view_dtype)` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L58) — Checks necessary preconditions that can be easily validated: — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- <a id="CreateTrailingDimension"></a>`CreateTrailingDimension(ViewSequence& result, StridedLayout& head_layout, const int64_t trailing_size)` — [`L453`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L453) — Adds reshapes and slices to the result decomposition necessary to create
- `CreateTrailingDimension(ViewSequence& result, StridedLayout& head_layout, const int64_t trailing_size)` — [`L453`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L453) — Adds reshapes and slices to the result decomposition necessary to create
- <a id="DecomposeIntoViewSequence"></a>`DecomposeIntoViewSequence(absl::Span<const int64_t> contiguous_base_shape, mlir::ElementType contiguous_base_dtype, const StridedLayout& view_layout, mlir::ElementType view_dtype, bool is_conj)` — [`L1244`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L1244) — Implementation notes:
- `DecomposeIntoViewSequence(absl::Span<const int64_t> contiguous_base_shape, mlir::ElementType contiguous_base_dtype, const StridedLayout& view_layout, mlir::ElementType view_dtype, bool is_conj)` — [`L1244`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L1244) — Implementation notes:
- <a id="GetContiguousBaseShape"></a>`GetContiguousBaseShape(const StridedLayout& view_layout)` — [`L1346`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L1346) — Returns a base shape which can be converted to the desired view layout in
- <a id="IndexedStridedDimensionSortCriterion"></a>`IndexedStridedDimensionSortCriterion(const IndexedStridedDimension& a, const IndexedStridedDimension& b)` — [`L129`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L129) — Sorts a list of indexed strided dimensions in the following order:
- <a id="IsRowMajorIgnoringTrivialDimensions"></a>`IsRowMajorIgnoringTrivialDimensions(const StridedLayout& layout)` — [`L191`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L191)
- <a id="MaybeAddComplexToRealBitcast"></a>`MaybeAddComplexToRealBitcast(ViewSequence& result, StridedLayout& head_layout, const mlir::ElementType contiguous_base_dtype, StridedLayout& tail_layout)` — [`L375`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L375) — If the base type is complex, adds a complex-to-real bitcast to the
- `MaybeAddComplexToRealBitcast(ViewSequence& result, StridedLayout& head_layout, const mlir::ElementType contiguous_base_dtype, StridedLayout& tail_layout)` — [`L375`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L375) — If the base type is complex, adds a complex-to-real bitcast to the
- <a id="MaybeAddRealToRealBitcast"></a>`MaybeAddRealToRealBitcast(ViewSequence& result, StridedLayout& head_layout, const mlir::ElementType real_head_element_type, const StridedLayout& tail_layout, const mlir::ElementType view_dtype)` — [`L515`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L515) — If necessary, adds a real-to-real bitcast to the decomposition.
- `MaybeAddRealToRealBitcast(ViewSequence& result, StridedLayout& head_layout, const mlir::ElementType real_head_element_type, const StridedLayout& tail_layout, const mlir::ElementType view_dtype)` — [`L515`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L515) — If necessary, adds a real-to-real bitcast to the decomposition.
- <a id="MaybeAddViewAsComplex"></a>`MaybeAddViewAsComplex(ViewSequence& result, StridedLayout& head_layout, const mlir::ElementType real_tail_element_type, const StridedLayout& tail_layout, const mlir::ElementType view_dtype)` — [`L555`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L555) — If the view type is complex, adds a view_as_complex to the decomposition.
- `MaybeAddViewAsComplex(ViewSequence& result, StridedLayout& head_layout, const mlir::ElementType real_tail_element_type, const StridedLayout& tail_layout, const mlir::ElementType view_dtype)` — [`L555`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L555) — If the view type is complex, adds a view_as_complex to the decomposition.
- <a id="RemoveExtraDim"></a>`RemoveExtraDim(StridedLayout& head_layout, const StridedLayout& tail_layout, ViewSequence& result, absl::Span<ViewPrimitive> tail_sequence)` — [`L1179`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L1179)
- `RemoveExtraDim(StridedLayout& head_layout, const StridedLayout& tail_layout, ViewSequence& result, absl::Span<ViewPrimitive> tail_sequence)` — [`L1179`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L1179)
- <a id="ShiftInitialViewWindow"></a>`ShiftInitialViewWindow(PadDimension& head_pad, SliceDimension& head_slice, const StridedLayout& layout_before_slice, SlicePrimitive& body_slice)` — [`L735`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L735) — Reduces or eliminates the initial pad and slice operations to the largest
- `ShiftInitialViewWindow(PadDimension& head_pad, SliceDimension& head_slice, const StridedLayout& layout_before_slice, UnfoldPrimitive& unfold)` — [`L798`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/decomposition.cc#L798)

