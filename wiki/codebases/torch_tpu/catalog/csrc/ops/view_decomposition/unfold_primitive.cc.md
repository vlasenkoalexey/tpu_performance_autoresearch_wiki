---
title: 'Module: csrc/ops/view_decomposition/unfold_primitive.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/unfold_primitive.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  UpdateLayout: UpdateLayout(80ab30cede5b3c1e).
  operator: '`operator<<`(cffb68637505b586).'
  ViewPrimitiveShlo: ViewPrimitiveShlo(796c9e5c3ee322e9).
  CheckUnfold: '`$anonymous_namespace_csrc/ops/view_decomposition/unfold_primitive.cc`/CheckUnfold(f5ae314ab5de81c3).'
---
# Module: [`csrc/ops/view_decomposition/unfold_primitive.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.cc)

## Functions
- `CheckUnfold(const StridedLayout& layout, const UnfoldPrimitive& unfold)` — [`L89`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.cc#L89)
- <a id="CheckUnfold"></a>`CheckUnfold(const UnfoldPrimitive& unfold, absl::Span<const int64_t> sizes, const std::string_view error_message_suffix)` — [`L38`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.cc#L38)
- `CheckUnfold(mlir::MlirOp input, const UnfoldPrimitive& unfold)` — [`L95`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.cc#L95)
- <a id="UpdateLayout"></a>`UpdateLayout(StridedLayout& layout, const UnfoldPrimitive& unfold)` — [`L112`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.cc#L112) — Updates the layout to reflect the effect of applying the given unfold.
- <a id="ViewPrimitiveShlo"></a>`ViewPrimitiveShlo(mlir::MlirOp input, const UnfoldPrimitive& unfold)` — [`L141`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.cc#L141) — An overload for the ViewPrimitiveShlo function that handles unfold
- <a id="operator"></a>`operator<<(std::ostream& os, const UnfoldPrimitive& unfold)` — [`L104`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/unfold_primitive.cc#L104)

