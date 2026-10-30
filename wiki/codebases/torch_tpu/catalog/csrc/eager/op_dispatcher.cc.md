---
title: 'Module: csrc/eager/op_dispatcher.cc'
type: catalog
provenance: extracted
module: csrc/eager/op_dispatcher.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  PromoteScalar: PromoteScalar(71a0e35ca1f08e1b).
  MakeTensor: MakeTensor(29ac4abcbdab6d03).
  AutoDonateInPlaceBuffers: internal/AutoDonateInPlaceBuffers(987e37f465d4f7a4).
  AssignBufferToOutput: internal/AssignBufferToOutput(d87fe0632de7dd7a).
  AssignBuffersToOutputs: internal/AssignBuffersToOutputs(9f4053c8ec40ff8f).
  EncodeParamCacheKey: internal/EncodeParamCacheKey(a28ca550004a2672).
  GetOpDispatchFailure: internal/GetOpDispatchFailure(81275779af2fbb29).
  MakeBuffer: '`$anonymous_namespace_csrc/eager/op_dispatcher.cc`/MakeBuffer(caea714e3a2e2728).'
  SetOpDispatchFailure: internal/SetOpDispatchFailure(d96256af6d38cfc3).
  IsEligibleDonor: '`$anonymous_namespace_csrc/eager/op_dispatcher.cc`/IsEligibleDonor(9a30b6b35f947a76).'
  MarkDonatedAndAliases: '`$anonymous_namespace_csrc/eager/op_dispatcher.cc`/MarkDonatedAndAliases(38c43ef42093f3ee).'
---
# Module: [`csrc/eager/op_dispatcher.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc)

## Functions
- <a id="AssignBufferToOutput"></a>`AssignBufferToOutput(const at::Tensor& output, DeviceBufferRef result_buffer)` — [`L271`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L271) — Resizes `output` (if shape differs) and assigns `result_buffer` to it. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="AssignBuffersToOutputs"></a>`AssignBuffersToOutputs(absl::Span<const at::Tensor> outputs, absl::Span<DeviceBufferRef> result_buffers)` — [`L281`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L281) — Resizes each defined tensor in `outputs` (if shape differs) and assigns the — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="AutoDonateInPlaceBuffers"></a>`AutoDonateInPlaceBuffers(absl::Span<const at::Tensor> outputs, absl::Span<const mlir::ElementType> out_dtypes, absl::Span<const absl::Span<const int64_t>> out_dims_list, absl::Span<const at::Tensor> inputs, Indices& donated_indices)` — [`L239`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L239) — Automatically detects and configures buffer donations from `inputs` into — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="EncodeParamCacheKey"></a>`EncodeParamCacheKey(const std::optional<PromotedScalar>& value)` — [`L216`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L216) — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="GetOpDispatchFailure"></a>`GetOpDispatchFailure()` — [`L205`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L205) — Returns the injected op dispatch failure. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="IsEligibleDonor"></a>`IsEligibleDonor(const at::Tensor& in, const at::Tensor& out, mlir::ElementType out_dtype, at::IntArrayRef destination_dims)` — [`L155`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L155) — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="MakeBuffer"></a>`MakeBuffer(const at::Scalar& scalar, c10::optional<at::ScalarType> scalar_type_opt = std::nullopt)` — [`L67`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L67) — Internal helper for MakeTensor that returns the — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="MakeTensor"></a>`MakeTensor(const at::Scalar& scalar, c10::optional<at::ScalarType> scalar_type_opt)` — [`L295`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L295) — Creates an at::Tensor from an at::Scalar. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- <a id="MarkDonatedAndAliases"></a>`MarkDonatedAndAliases(size_t donated_idx, absl::Span<const at::Tensor> inputs, std::vector<bool>& input_donated)` — [`L190`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L190)
- `MarkDonatedAndAliases(size_t donated_idx, absl::Span<const at::Tensor> inputs, std::vector<bool>& input_donated)` — [`L190`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L190)
- <a id="PromoteScalar"></a>`PromoteScalar(at::Scalar scalar)` — [`L302`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L302) — Promotes the given scalar to a tensor lazily. — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)
- `PromoteScalar(at::ArrayRef<at::Scalar> scalars)` — [`L321`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L321) — Promotes the given scalars to tensors lazily.
- `PromoteScalar(at::ArrayRef<at::Scalar> scalars)` — [`L321`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L321) — Promotes the given scalars to tensors lazily.
- `PromoteScalar(std::optional<at::Scalar> scalar)` — [`L314`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L314) — Promotes the given optional scalar to an optional tensor lazily.
- <a id="SetOpDispatchFailure"></a>`SetOpDispatchFailure(std::string op_base_name, std::string failure_message)` — [`L210`](../../../../../../raw/code/torch_tpu/csrc/eager/op_dispatcher.cc#L210) — Forces the op with the given base name to fail with the given message. This — documented in [eager-op-dispatch](../../../concepts/eager-op-dispatch.md)

