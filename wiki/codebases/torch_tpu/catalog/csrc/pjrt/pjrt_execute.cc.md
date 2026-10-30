---
title: 'Module: csrc/pjrt/pjrt_execute.cc'
type: catalog
provenance: extracted
module: csrc/pjrt/pjrt_execute.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  PrepareDynamicExecutionArguments: '`$anonymous_namespace_csrc/pjrt/pjrt_execute.cc`/PrepareDynamicExecutionArguments(c4a5dba8b9eb348).'
  Execute: Execute(3bd326a9df87920f).
  CreateRuntimeShapeMetadataBuffer: '`$anonymous_namespace_csrc/pjrt/pjrt_execute.cc`/CreateRuntimeShapeMetadataBuffer(2e57cf19ae687799).'
  MakeXlaShape: '`$anonymous_namespace_csrc/pjrt/pjrt_execute.cc`/MakeXlaShape(4adaf788354615e8).'
  DynamicExecutionArguments.ephemeral_buffers: '`$anonymous_namespace_csrc/pjrt/pjrt_execute.cc`/DynamicExecutionArguments#ephemeral_buffers.'
  DynamicExecutionArguments.full_args: '`$anonymous_namespace_csrc/pjrt/pjrt_execute.cc`/DynamicExecutionArguments#full_args.'
  HloModuleContainsCollective: '`$anonymous_namespace_csrc/pjrt/pjrt_execute.cc`/HloModuleContainsCollective(a81851cf957d50b6).'
  DynamicExecutionArguments: '`$anonymous_namespace_csrc/pjrt/pjrt_execute.cc`/DynamicExecutionArguments#'
---
# Module: [`csrc/pjrt/pjrt_execute.cc`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.cc)

## Classes
### <a id="DynamicExecutionArguments"></a>`DynamicExecutionArguments`
- def: [`csrc/pjrt/pjrt_execute.cc:106`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.cc#L106)
- doc: Holds the full physical argument pointer list and any newly allocated
- signature: `struct DynamicExecutionArguments`
- members:
  - <a id="DynamicExecutionArguments.ephemeral_buffers"></a>`ephemeral_buffers` — [`L108`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.cc#L108)
  - <a id="DynamicExecutionArguments.full_args"></a>`full_args` — [`L107`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.cc#L107)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`PrepareDynamicExecutionArguments`](pjrt_execute.cc.md#PrepareDynamicExecutionArguments), [`Execute`](pjrt_execute.cc.md#Execute)

## Functions
- `CreateRuntimeShapeMetadataBuffer(absl::Span<const int64_t> dimensions, const xla::Layout& layout, xla::PjRtClient* absl_nonnull client, xla::PjRtMemorySpace* absl_nonnull memory_space)` — [`L78`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.cc#L78) — Creates a 1D S32[rank] PjRtBuffer containing the concrete runtime dimension
- <a id="CreateRuntimeShapeMetadataBuffer"></a>`CreateRuntimeShapeMetadataBuffer(absl::Span<const int64_t> dimensions, const xla::Layout& layout, xla::PjRtClient* absl_nonnull client, xla::PjRtMemorySpace* absl_nonnull memory_space)` — [`L78`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.cc#L78) — Creates a 1D S32[rank] PjRtBuffer containing the concrete runtime dimension — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- `Execute(const SharedLoadedExecutableWithMetadata& executable, std::vector<xla::PjRtBuffer* absl_nullable> argument_buffers, absl::Span<const Shape> logical_output_shapes)` — [`L206`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.cc#L206) — Launches the executable. This is a synchronous call, and will block
- <a id="Execute"></a>`Execute(const SharedLoadedExecutableWithMetadata& executable, std::vector<xla::PjRtBuffer* absl_nullable> argument_buffers, absl::Span<const Shape> logical_output_shapes)` — [`L206`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.cc#L206) — Launches the executable. This is a synchronous call, and will block — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="HloModuleContainsCollective"></a>`HloModuleContainsCollective(const xla::HloModule* hlo_module)` — [`L193`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.cc#L193)
- <a id="MakeXlaShape"></a>`MakeXlaShape(const Shape& shape, const xla::Layout& layout)` — [`L64`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.cc#L64) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- <a id="PrepareDynamicExecutionArguments"></a>`PrepareDynamicExecutionArguments(const UnboundedDynamicExecutionMetadata& meta, absl::Span<xla::PjRtBuffer* const> argument_buffers, absl::Span<const Shape> logical_output_shapes)` — [`L117`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_execute.cc#L117) — Routes logical argument buffers, pre-allocated donated dynamic output — documented in [pjrt-client](../../../concepts/pjrt-client.md)

