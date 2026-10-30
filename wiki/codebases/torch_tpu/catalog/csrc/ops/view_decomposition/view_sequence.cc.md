---
title: 'Module: csrc/ops/view_decomposition/view_sequence.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/view_sequence.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  operator: '`operator==`(f569bef9f3d28d5a).'
  Simplify: Simplify(7891c79eb2461e5e).
  SymbolicViewCacheKey: '`$anonymous_namespace_csrc/ops/view_decomposition/view_sequence.cc`/SymbolicViewCacheKey(9f68fdfd35a08f84).'
  ViewSequenceCacheKey: ViewSequenceCacheKey(ed00685fa9d31475).
  UpdateLayout: UpdateLayout(a59bb0ebb4e5826e).
  RemoveNoOps: '`$anonymous_namespace_csrc/ops/view_decomposition/view_sequence.cc`/RemoveNoOps(444690831355b48c).'
  ViewCacheKeyVisitor.operator: '`$anonymous_namespace_csrc/ops/view_decomposition/view_sequence.cc`/ViewCacheKeyVisitor#`operator()`(bfa244c0cfc27725).'
  ViewPrimitiveShlo: ViewPrimitiveShlo(f7980773d7fe79ea).
  MaybeMergeSequential: '`$anonymous_namespace_csrc/ops/view_decomposition/view_sequence.cc`/MaybeMergeSequential(94023abbc1482e90).'
  ViewSequenceShlo: ViewSequenceShlo(2c60bd0362552296).
  ViewToCacheKey: '`$anonymous_namespace_csrc/ops/view_decomposition/view_sequence.cc`/ViewToCacheKey(d0b9aaf2727c19ad).'
  MergeAllSequential: '`$anonymous_namespace_csrc/ops/view_decomposition/view_sequence.cc`/MergeAllSequential(30ce46cb091eb21e).'
  ViewCacheKeyVisitor: '`$anonymous_namespace_csrc/ops/view_decomposition/view_sequence.cc`/ViewCacheKeyVisitor#'
---
# Module: [`csrc/ops/view_decomposition/view_sequence.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc)

## Classes
### <a id="ViewCacheKeyVisitor"></a>`ViewCacheKeyVisitor`
- def: [`csrc/ops/view_decomposition/view_sequence.cc:344`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L344)
- signature: `struct ViewCacheKeyVisitor`
- members:
  - `operator()()` — [`L416`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L416)
  - `operator()()` — [`L422`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L422)
  - <a id="ViewCacheKeyVisitor.operator"></a>`operator()()` — [`L348`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L348) — Special handling for reshape primitive since we only support affine
  - `operator()()` — [`L426`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L426)
  - `operator()()` — [`L431`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L431)
  - `operator()()` — [`L438`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L438)
  - `operator()()` — [`L443`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L443)
  - `operator()()` — [`L455`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L455)
  - `operator()()` — [`L478`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L478) — Fallback for all other view primitives.
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`MaybeAddCppSourceLoc`](../../common/status_builder.cc.md#MaybeAddCppSourceLoc), [`GetRootOpName`](../python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../../common/status_builder.cc.md#SetRootOpNamePayload), [`StatusBuilder`](../../common/status_builder.h.md#StatusBuilder), [`operator<<`](../../common/status_builder.h.md#StatusBuilder.operator), [`is_status_or_ref`](../../common/error_utils.h.md#is_status_or_ref), [`operator<<`](../op_names.h.md#operator), [`operator<<`](../../common/status_builder.h.md#operator), [`operator<<`](../../common/status_builder.h.md#operator), [`operator<<`](../../common/cache_key.cc.md#operator), [`operator<<`](strided_layout.cc.md#operator), [`ToString`](../../common/dtype.cc.md#ToString), [`operator<<`](bitcast_primitive.cc.md#operator), [`ReshapePrimitive`](reshape_primitive.h.md#ReshapePrimitive), [`operator<<`](bitcast_primitive.cc.md#operator), [`operator<<`](bitcast_primitive.cc.md#operator), [`operator<<`](bitcast_primitive.cc.md#operator), [`operator<<`](bitcast_primitive.cc.md#operator), [`operator<<`](reshape_primitive.cc.md#operator), [`operator<<`](broadcast_primitive.cc.md#operator), [`operator<<`](slice_primitive.cc.md#operator), [`operator<<`](pad_primitive.cc.md#operator), [`operator<<`](pad_primitive.cc.md#operator), [`operator==`](view_sequence.cc.md#operator), [`ReassociationToString`](../op_builder_utils.cc.md#ReassociationToString), [`kPythonNotImplementedError`](../../common/error_utils.h.md#kPythonNotImplementedError), [`RealToRealBitcast`](bitcast_primitive.h.md#RealToRealBitcast), [`operator<<`](view_sequence.cc.md#operator), [`operator==`](strided_layout.cc.md#operator), [`GetReshapeReassociation`](../op_builder_utils.cc.md#GetReshapeReassociation), [`operator==`](strided_layout.cc.md#operator), [`operator==`](pad_primitive.cc.md#operator), [`ComplexToRealBitcast`](bitcast_primitive.h.md#ComplexToRealBitcast), [`operator==`](pad_primitive.cc.md#operator), [`operator==`](slice_primitive.cc.md#operator), [`operator==`](bitcast_primitive.cc.md#operator), [`operator==`](bitcast_primitive.cc.md#operator), [`new_sizes`](reshape_primitive.h.md#ReshapePrimitive.new_sizes), [`operator==`](bitcast_primitive.cc.md#operator)  (+33 more)
- used by: [`ViewToCacheKey`](view_sequence.cc.md#ViewToCacheKey)

## Functions
- <a id="MaybeMergeSequential"></a>`MaybeMergeSequential(T& first, ViewPrimitive& second)` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L91) — Returns true if the second primitive was merged into the first.
- `MaybeMergeSequential(PadPrimitive& first, ViewPrimitive& second)` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L116)
- `MaybeMergeSequential(ViewAsComplex& first, ViewPrimitive& second)` — [`L128`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L128)
- `MaybeMergeSequential(RealToRealBitcast& first, ViewPrimitive& second)` — [`L120`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L120)
- `MaybeMergeSequential(TransposePrimitive& first, ViewPrimitive& second)` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L112)
- `MaybeMergeSequential(ComplexToRealBitcast& first, ViewPrimitive& second)` — [`L124`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L124)
- `MaybeMergeSequential(ViewPrimitive& first, ViewPrimitive& second)` — [`L151`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L151)
- `MaybeMergeSequential(UnfoldPrimitive& first, ViewPrimitive& second)` — [`L132`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L132)
- `MaybeMergeSequential(BroadcastPrimitive& first, ViewPrimitive& second)` — [`L108`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L108) — The decomposition sequence will only produce at most one broadcast, one
- `MaybeMergeSequential(ConjPrimitive& first, ViewPrimitive& second)` — [`L136`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L136)
- <a id="MergeAllSequential"></a>`MergeAllSequential(ViewSequence& sequence)` — [`L157`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L157)
- `MergeAllSequential(ViewSequence& sequence)` — [`L157`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L157)
- <a id="RemoveNoOps"></a>`RemoveNoOps(ViewSequence& sequence, absl::Span<const int64_t> contiguous_base_shape)` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L61) — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- `RemoveNoOps(ViewSequence& sequence, absl::Span<const int64_t> contiguous_base_shape)` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L61)
- `Simplify(ViewSequence& sequence, absl::Span<const int64_t> contiguous_base_shape)` — [`L320`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L320) — Simplifies a sequence of view primitives by removing no-ops and merging
- <a id="Simplify"></a>`Simplify(ViewSequence& sequence, absl::Span<const int64_t> contiguous_base_shape)` — [`L320`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L320) — Simplifies a sequence of view primitives by removing no-ops and merging — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- <a id="SymbolicViewCacheKey"></a>`SymbolicViewCacheKey(ViewSequenceSpan view_sequence)` — [`L491`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L491) — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- `UpdateLayout(StridedLayout& layout, ViewSequenceSpan view_sequence)` — [`L312`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L312) — Updates the layout to reflect the effect of applying the given view
- <a id="UpdateLayout"></a>`UpdateLayout(StridedLayout& layout, const ViewPrimitive& primitive)` — [`L287`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L287) — Updates the layout to reflect the effect of applying the given view
- <a id="ViewPrimitiveShlo"></a>`ViewPrimitiveShlo(mlir::MlirOp input, const ViewPrimitive& primitive)` — [`L295`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L295) — Applies the given view primitive to the input, using the corresponding
- `ViewSequenceCacheKey(ViewSequenceSpan view_sequence, absl::Span<const int64_t> view_strides, int64_t view_storage_offset)` — [`L510`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L510)
- <a id="ViewSequenceCacheKey"></a>`ViewSequenceCacheKey(ViewSequenceSpan view_sequence, const c10::TensorImpl& tensor)` — [`L532`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L532) — Returns the cache key for the given view sequence and tensor.
- <a id="ViewSequenceShlo"></a>`ViewSequenceShlo(mlir::MlirOp input, ViewSequenceSpan view_sequence)` — [`L333`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L333) — An MlirOpBuilder to apply the given view sequence to the input.
- <a id="ViewToCacheKey"></a>`ViewToCacheKey(const ViewPrimitive& primitive)` — [`L486`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L486)
- `operator!=(const ViewPrimitive& lhs, const ViewPrimitive& rhs)` — [`L243`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L243)
- `operator<<(std::ostream& os, const ViewPrimitive& primitive)` — [`L247`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L247) — Formats the view primitive as one of:
- <a id="operator"></a>`operator==(const ViewPrimitive& lhs, const ViewPrimitive& rhs)` — [`L186`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/view_sequence.cc#L186)

