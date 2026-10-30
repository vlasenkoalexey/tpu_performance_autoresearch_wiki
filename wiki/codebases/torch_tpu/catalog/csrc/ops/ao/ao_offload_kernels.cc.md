---
title: 'Module: csrc/ops/ao/ao_offload_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/ao/ao_offload_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenAoReload: AtenAoReload(af1a68f1fe5cb839).
  AtenAoOffload: AtenAoOffload(28959186f7a4bda8).
  AtenAoWaitTensor: AtenAoWaitTensor(e012ef1ab88bc537).
  MaybeApplyStridedView: '`$anonymous_namespace_csrc/ops/ao/ao_offload_kernels.cc`/MaybeApplyStridedView(430fdf0ccf6134e8).'
  ReshapeIfNeeded: '`$anonymous_namespace_csrc/ops/ao/ao_offload_kernels.cc`/ReshapeIfNeeded(2976d31bcd0dea57).'
  BuildPlacementOp: '`$anonymous_namespace_csrc/ops/ao/ao_offload_kernels.cc`/BuildPlacementOp(df4636a109c0b388).'
  CustomCallApiVersion: '`$anonymous_namespace_csrc/ops/ao/ao_offload_kernels.cc`/CustomCallApiVersion#'
  CustomCallApiVersionAttr: '`$anonymous_namespace_csrc/ops/ao/ao_offload_kernels.cc`/CustomCallApiVersionAttr#'
---
# Module: [`csrc/ops/ao/ao_offload_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/ao/ao_offload_kernels.cc)

## Classes
### <a id="CustomCallApiVersion"></a>`CustomCallApiVersion`
- def: [`csrc/ops/ao/ao_offload_kernels.cc:53`](../../../../../../../raw/code/torch_tpu/csrc/ops/ao/ao_offload_kernels.cc#L53)
- signature: `using mlir::stablehlo::CustomCallApiVersion`
- uses (calls/refs, reference-scoped): (none in-repo)

### <a id="CustomCallApiVersionAttr"></a>`CustomCallApiVersionAttr`
- def: [`csrc/ops/ao/ao_offload_kernels.cc:54`](../../../../../../../raw/code/torch_tpu/csrc/ops/ao/ao_offload_kernels.cc#L54)
- signature: `using mlir::stablehlo::CustomCallApiVersionAttr`
- uses (calls/refs, reference-scoped): (none in-repo)

## Functions
- <a id="AtenAoOffload"></a>`AtenAoOffload(const at::Tensor& tensor)` — [`L106`](../../../../../../../raw/code/torch_tpu/csrc/ops/ao/ao_offload_kernels.cc#L106) — Activation offload kernel. Emits annotate_device_placement with placement
- <a id="AtenAoReload"></a>`AtenAoReload(const at::Tensor& tensor, at::Device device, at::OptionalIntArrayRef original_size, at::OptionalIntArrayRef original_stride)` — [`L127`](../../../../../../../raw/code/torch_tpu/csrc/ops/ao/ao_offload_kernels.cc#L127) — Activation reload kernel. Emits annotate_device_placement with placement
- <a id="AtenAoWaitTensor"></a>`AtenAoWaitTensor(const at::Tensor& tensor, const std::optional<at::Tensor>& keepalive, const std::optional<at::Tensor>& last_use_of_storage)` — [`L168`](../../../../../../../raw/code/torch_tpu/csrc/ops/ao/ao_offload_kernels.cc#L168) — Activation wait_tensor kernel (no-op pass-through).
- <a id="BuildPlacementOp"></a>`BuildPlacementOp(mlir::MlirOp input, std::string_view placement)` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/ao/ao_offload_kernels.cc#L56)
- <a id="MaybeApplyStridedView"></a>`MaybeApplyStridedView(DeviceBufferRef device_buffer, at::OptionalIntArrayRef original_stride)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/ao/ao_offload_kernels.cc#L80)
- <a id="ReshapeIfNeeded"></a>`ReshapeIfNeeded(mlir::MlirOp input, at::IntArrayRef input_shape, at::IntArrayRef target_shape)` — [`L93`](../../../../../../../raw/code/torch_tpu/csrc/ops/ao/ao_offload_kernels.cc#L93)

