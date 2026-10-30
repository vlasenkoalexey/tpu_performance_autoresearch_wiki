---
title: 'Module: csrc/ops/view_decomposition/pad_primitive.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/pad_primitive.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  operator: '`operator<<`(83f6fc51b9c47547).'
  UpdateLayout: UpdateLayout(c18a0f134575a464).
  ViewPrimitiveShlo: ViewPrimitiveShlo(288cd0ee88ce5035).
  CheckPad: '`$anonymous_namespace_csrc/ops/view_decomposition/pad_primitive.cc`/CheckPad(ac4f3e1e3b8df0c3).'
---
# Module: [`csrc/ops/view_decomposition/pad_primitive.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.cc)

## Functions
- <a id="CheckPad"></a>`CheckPad(const PadPrimitive& pad, const size_t rank, const std::string_view error_message_suffix)` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.cc#L41)
- <a id="UpdateLayout"></a>`UpdateLayout(StridedLayout& layout, const PadPrimitive& pad)` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.cc#L83) — Updates the layout to reflect the effect of applying the given pad
- <a id="ViewPrimitiveShlo"></a>`ViewPrimitiveShlo(mlir::MlirOp input, const PadPrimitive& pad)` — [`L123`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.cc#L123) — An overload for the ViewPrimitiveShlo function that handles pad
- `operator<<(std::ostream& os, const PadDimension& dim)` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.cc#L72) — Formats the pad dimension like "(low=1, high=2, interior=3)".
- <a id="operator"></a>`operator<<(std::ostream& os, const PadPrimitive& pad)` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.cc#L78) — Formats the pad like
- `operator==(const PadDimension& lhs, const PadDimension& rhs)` — [`L62`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.cc#L62)
- `operator==(const PadPrimitive& lhs, const PadPrimitive& rhs)` — [`L68`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/pad_primitive.cc#L68)

