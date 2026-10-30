---
title: 'Module: csrc/ops/view_decomposition/slice_primitive.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/slice_primitive.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  operator: '`operator<<`(6e826b86e3dd7c1).'
  ViewPrimitiveShlo: ViewPrimitiveShlo(351e2114d0c237c).
  UpdateLayout: UpdateLayout(c04d73199a82f2d4).
  CheckSlice: '`$anonymous_namespace_csrc/ops/view_decomposition/slice_primitive.cc`/CheckSlice(b158d5dc9b367798).'
  Merge: Merge(b1f0e49b9398ab6b).
  CheckSliceMerge: '`$anonymous_namespace_csrc/ops/view_decomposition/slice_primitive.cc`/CheckSliceMerge(f256cc7e0ec4510b).'
  ComputeNewSize: '`$anonymous_namespace_csrc/ops/view_decomposition/slice_primitive.cc`/ComputeNewSize(7c165f7170aa719e).'
---
# Module: [`csrc/ops/view_decomposition/slice_primitive.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.cc)

## Functions
- <a id="CheckSlice"></a>`CheckSlice(const SlicePrimitive& slice, absl::Span<const int64_t> sizes, const GetErrorMessageSuffix& get_error_message_suffix)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.cc#L54)
- <a id="CheckSliceMerge"></a>`CheckSliceMerge(const SlicePrimitive& first, const SlicePrimitive& second)` — [`L104`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.cc#L104)
- <a id="ComputeNewSize"></a>`ComputeNewSize(const SliceDimension& slice_dim)` — [`L46`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.cc#L46)
- <a id="Merge"></a>`Merge(SlicePrimitive first, const SlicePrimitive second)` — [`L168`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.cc#L168) — Merges two sequential slices into a single slice.
- <a id="UpdateLayout"></a>`UpdateLayout(StridedLayout& layout, const SlicePrimitive& slice)` — [`L135`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.cc#L135) — Updates the layout to reflect the effect of applying the given slice
- <a id="ViewPrimitiveShlo"></a>`ViewPrimitiveShlo(mlir::MlirOp input, const SlicePrimitive& slice)` — [`L199`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.cc#L199) — An overload for the ViewPrimitiveShlo function that handles slice — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- `operator<<(std::ostream& os, const SliceDimension& dim)` — [`L124`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.cc#L124) — Formats the slice dimension like "(start=1, limit=2, stride=3)".
- <a id="operator"></a>`operator<<(std::ostream& os, const SlicePrimitive& slice)` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.cc#L130) — Formats the slice like
- `operator==(const SliceDimension& lhs, const SliceDimension& rhs)` — [`L119`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/slice_primitive.cc#L119)

