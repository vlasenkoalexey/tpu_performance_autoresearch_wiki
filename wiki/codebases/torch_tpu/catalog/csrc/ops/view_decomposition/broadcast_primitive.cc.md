---
title: 'Module: csrc/ops/view_decomposition/broadcast_primitive.cc'
type: catalog
provenance: extracted
module: csrc/ops/view_decomposition/broadcast_primitive.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  operator: '`operator<<`(c1c0f01d69f0c8ba).'
  ViewPrimitiveShlo: ViewPrimitiveShlo(c2360f241173593e).
  UpdateLayout: UpdateLayout(383015e89f0d65e5).
  CheckBroadcast: '`$anonymous_namespace_csrc/ops/view_decomposition/broadcast_primitive.cc`/CheckBroadcast(f54516041a09cec8).'
---
# Module: [`csrc/ops/view_decomposition/broadcast_primitive.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/broadcast_primitive.cc)

## Functions
- `CheckBroadcast(const BroadcastPrimitive& broadcast, const StridedLayout& layout)` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/broadcast_primitive.cc#L91)
- `CheckBroadcast(const BroadcastPrimitive& broadcast, mlir::RankedTensorType type)` — [`L81`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/broadcast_primitive.cc#L81)
- <a id="CheckBroadcast"></a>`CheckBroadcast(const BroadcastPrimitive& broadcast, absl::Span<const int64_t> input_sizes, const std::string_view error_message_suffix, const IsDynamicDim& is_dynamic_dim)` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/broadcast_primitive.cc#L41)
- <a id="UpdateLayout"></a>`UpdateLayout(StridedLayout& layout, const BroadcastPrimitive& broadcast)` — [`L110`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/broadcast_primitive.cc#L110) — Updates the layout to reflect the effect of applying the given broadcast
- <a id="ViewPrimitiveShlo"></a>`ViewPrimitiveShlo(mlir::MlirOp input, const BroadcastPrimitive& broadcast)` — [`L132`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/broadcast_primitive.cc#L132) — An overload for the ViewPrimitiveShlo function that handles broadcast
- <a id="operator"></a>`operator<<(std::ostream& os, const BroadcastPrimitive& broadcast)` — [`L101`](../../../../../../../raw/code/torch_tpu/csrc/ops/view_decomposition/broadcast_primitive.cc#L101) — Formats the broadcast like "broadcast(new_sizes=[1, 2, 3],

