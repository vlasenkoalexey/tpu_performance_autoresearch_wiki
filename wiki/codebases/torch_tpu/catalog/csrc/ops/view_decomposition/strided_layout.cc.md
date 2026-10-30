---
title: 'Module: csrc/ops/view_decomposition/strided_layout.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/strided_layout.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  operator: '`operator<<`(85ef34dff2643773).'
  MakeContiguousBaseLayout: MakeContiguousBaseLayout(96bc713054ce8a29).
  GetSizes: GetSizes(f430b3f36ae2023a).
  GetStrides: GetStrides(f430b3f36ae2023a).
  StridedLayout.FromTensor: StridedLayout#FromTensor(591cefd16a36784f).
---
# Module: [`csrc/ops/view_decomposition/strided_layout.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/strided_layout.cc)

## Functions
- <a id="GetSizes"></a>`GetSizes(const StridedLayout& layout)` — [`L104`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/strided_layout.cc#L104) — Given a StridedLayout, returns a vector with all dimension sizes gathered.
- <a id="GetStrides"></a>`GetStrides(const StridedLayout& layout)` — [`L111`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/strided_layout.cc#L111) — Given a StridedLayout, returns a vector with all dimension strides gathered.
- <a id="MakeContiguousBaseLayout"></a>`MakeContiguousBaseLayout(absl::Span<const int64_t> shape)` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/strided_layout.cc#L35) — Given a shape, returns the unique contiguous base layout with that shape. — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- <a id="operator"></a>`operator<<(std::ostream& os, const StridedLayout& layout)` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/strided_layout.cc#L70) — documented in [view-decomposition](../../../../concepts/view-decomposition.md)
- `operator==(const StridedLayout& lhs, const StridedLayout& rhs)` — [`L84`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/strided_layout.cc#L84)
- `operator==(const StridedDimension& lhs, const StridedDimension& rhs)` — [`L31`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/strided_layout.cc#L31)

## Other members
- <a id="StridedLayout.FromTensor"></a>`StridedLayout.FromTensor` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/strided_layout.cc#L57)

