---
title: 'Module: csrc/eager/device_buffer_utils.cc'
type: catalog
provenance: extracted
module: csrc/eager/device_buffer_utils.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  CreateViewDeviceBufferRef: CreateViewDeviceBufferRef(abb6a9b201a7d981).
  CreateDeferredDeviceBufferList: internal/CreateDeferredDeviceBufferList(7f609ee6f4e6a492).
  CreateZeroSizeDeviceBufferRef: CreateZeroSizeDeviceBufferRef(c33ef7ccf336a4df).
  CreateInverseViewDeviceBufferRef: CreateInverseViewDeviceBufferRef(38d7c462ec8b441c).
  CreateEmptyDeviceBufferRef: CreateEmptyDeviceBufferRef(c33ef7ccf336a4df).
  CreateConstantDeviceBufferRefImpl: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/CreateConstantDeviceBufferRefImpl(a63c132a5d5ee7a8).'
  MakeAsStridedInverseBuilder: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/MakeAsStridedInverseBuilder(63aaf418cd7ef32a).'
  DeferNeverDispatch: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/DeferNeverDispatch(cba2d0ed9b8b79a0).'
  SliceOperandIfNeeded: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/SliceOperandIfNeeded(30eb95b885372fd2).'
  ComputeConstantDeviceBufferRefOpParamCacheKeys: internal/ComputeConstantDeviceBufferRefOpParamCacheKeys(e2e65c4c4f3f42d7).
  CastOutputs: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/CastOutputs(7902758ab0c5675).'
  ApplyComputationDtype: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/ApplyComputationDtype(36709c63a37b0dc).'
  RequiredStorageBytes: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/RequiredStorageBytes(8ec8b071cfb4efea).'
  DeferAndFuseDispatch: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/DeferAndFuseDispatch(d6b1555679adc471).'
  GetRepeatedOpsMaterializationMode: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/GetRepeatedOpsMaterializationMode(2450e1f23e16b97).'
  CreateConstantDeviceBufferRef: CreateConstantDeviceBufferRef(8cce2aa7c1434c1f).
  MustApplyRepeatedOpsHeuristic: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/MustApplyRepeatedOpsHeuristic(c9857a73d68e59ba).'
  CastInputs: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/CastInputs(420308b38535fb81).'
  AsStridedInverseBuilderResult: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/AsStridedInverseBuilderResult#'
  kRepeatedOpSafeMode: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/kRepeatedOpSafeMode.'
  AsStridedInverseBuilderResult.builder: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/AsStridedInverseBuilderResult#builder.'
  AsStridedInverseBuilderResult.donated_indices: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/AsStridedInverseBuilderResult#donated_indices.'
  AsStridedInverseBuilderResult.inputs: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/AsStridedInverseBuilderResult#inputs.'
  kRepeatedOpAggressiveMode: '`$anonymous_namespace_csrc/eager/device_buffer_utils.cc`/kRepeatedOpAggressiveMode.'
---
# Module: [`csrc/eager/device_buffer_utils.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc)

## Classes
### <a id="AsStridedInverseBuilderResult"></a>`AsStridedInverseBuilderResult`
- def: [`csrc/eager/device_buffer_utils.cc:425`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L425)
- doc: A builder and its required inputs for a view inversion (simulated write),
- signature: `struct AsStridedInverseBuilderResult`
- members:
  - <a id="AsStridedInverseBuilderResult.builder"></a>`builder` — [`L427`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L427) — The MlirOpBuilder to put in the constructed DeferredOp.
  - <a id="AsStridedInverseBuilderResult.donated_indices"></a>`donated_indices` — [`L431`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L431)
  - <a id="AsStridedInverseBuilderResult.inputs"></a>`inputs` — [`L430`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L430) — Either the write buffer only (if the view covers the entire base), or both
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](device_buffer.h.md#DeviceBufferRef), [`Indices`](../common/dimension_types.h.md#Indices), [`MlirOpBuilder`](../ops/op_builder_utils.h.md#MlirOpBuilder)
- used by: [`SliceOperandIfNeeded`](device_buffer_utils.cc.md#SliceOperandIfNeeded)

## Functions
- <a id="ApplyComputationDtype"></a>`ApplyComputationDtype(internal::DeferredOpParams& params)` — [`L113`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L113) — Modifies the op_builder to reflect the computation dtype of the op, if
- `CastInputs(mlir::MlirBuilder& builder, absl::Span<mlir::MlirOp> inputs, std::optional<mlir::ElementType> computation_dtype)` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L71) — Upcasts inputs to computation_dtype if specified.
- <a id="CastInputs"></a>`CastInputs(mlir::MlirBuilder& builder, absl::Span<mlir::MlirOp> inputs, std::optional<mlir::ElementType> computation_dtype)` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L71) — Upcasts inputs to computation_dtype if specified.
- `CastOutputs(mlir::MlirBuilder& builder, const DynamicMlirOpResults& results, absl::Span<const mlir::ElementType> expected_out_dtypes)` — [`L93`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L93) — Downcasts outputs to their expected dtypes.
- <a id="CastOutputs"></a>`CastOutputs(mlir::MlirBuilder& builder, const DynamicMlirOpResults& results, absl::Span<const mlir::ElementType> expected_out_dtypes)` — [`L93`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L93) — Downcasts outputs to their expected dtypes.
- <a id="ComputeConstantDeviceBufferRefOpParamCacheKeys"></a>`ComputeConstantDeviceBufferRefOpParamCacheKeys(absl::Span<const char> cpu_tensor_data, const Dimensions& dimensions, mlir::ElementType element_type)` — [`L251`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L251) — Computes the OpParamCacheKeys for CreateConstantDeviceBufferRefImpl.
- <a id="CreateConstantDeviceBufferRef"></a>`CreateConstantDeviceBufferRef(std::vector<char> cpu_tensor_data, Dimensions dimensions, mlir::ElementType element_type)` — [`L346`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L346) — Creates a deferred DeviceBufferList containing a constant tensor value,
- `CreateConstantDeviceBufferRef(std::vector<char> cpu_tensor_data, Dimensions dimensions, mlir::ElementType element_type)` — [`L346`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L346) — Creates a deferred DeviceBufferList containing a constant tensor value,
- <a id="CreateConstantDeviceBufferRefImpl"></a>`CreateConstantDeviceBufferRefImpl(std::vector<char> cpu_tensor_data, Dimensions dimensions, mlir::ElementType element_type, OpName op_name)` — [`L270`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L270) — Common pathway for CreateConstantDeviceBufferRef and
- `CreateConstantDeviceBufferRefImpl(std::vector<char> cpu_tensor_data, Dimensions dimensions, mlir::ElementType element_type, OpName op_name)` — [`L270`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L270) — Common pathway for CreateConstantDeviceBufferRef and
- `CreateDeferredDeviceBufferList(DeferredOpParams&& params)` — [`L213`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L213) — Don't use this directly when defining ops. Use DispatchOp<kNumInputs,
- <a id="CreateDeferredDeviceBufferList"></a>`CreateDeferredDeviceBufferList(DeferredOpParams&& params)` — [`L213`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L213) — Don't use this directly when defining ops. Use DispatchOp<kNumInputs, — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="CreateEmptyDeviceBufferRef"></a>`CreateEmptyDeviceBufferRef(Dimensions dimensions, mlir::ElementType element_type)` — [`L354`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L354) — Creates a DeviceBufferList as if by using the torch.empty() operation — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="CreateInverseViewDeviceBufferRef"></a>`CreateInverseViewDeviceBufferRef(DeviceBufferRef base_buffer_ref, DeviceBufferRef write_buf, const TpuLayout& tpu_layout, bool view_is_conj, bool donate_base)` — [`L633`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L633) — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="CreateViewDeviceBufferRef"></a>`CreateViewDeviceBufferRef(DeviceBufferRef base_buffer_ref, const TpuLayout& tpu_layout, bool view_is_conj)` — [`L535`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L535) — Creates a DeviceBufferRef representing a view of a base DeviceBufferRef. — documented in [deferred-execution-and-materialization](../../../concepts/deferred-execution-and-materialization.md)
- <a id="CreateZeroSizeDeviceBufferRef"></a>`CreateZeroSizeDeviceBufferRef(Dimensions dimensions, mlir::ElementType element_type)` — [`L382`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L382) — Creates a DeviceBufferList with a constant value of "no data".
- <a id="DeferAndFuseDispatch"></a>`DeferAndFuseDispatch(absl::Span<const DeviceBufferRef> results)` — [`L191`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L191) — Handles post-op creation events for the kDeferAndFuse eager mode.
- <a id="DeferNeverDispatch"></a>`DeferNeverDispatch(absl::Span<const DeviceBufferRef> results, const OpName op_name, const bool block)` — [`L146`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L146) — Handles post-op creation events for the kDeferNever and
- <a id="GetRepeatedOpsMaterializationMode"></a>`GetRepeatedOpsMaterializationMode()` — [`L181`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L181)
- <a id="MakeAsStridedInverseBuilder"></a>`MakeAsStridedInverseBuilder(InverseViewOperation inverse_view_operation, DeviceBufferRef base_buffer_ref, DeviceBufferRef write_buf, Dimensions view_dimensions, bool donate_base)` — [`L464`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L464) — Helper function for AssignBufferToAtTensor to switch between two cases:
- <a id="MustApplyRepeatedOpsHeuristic"></a>`MustApplyRepeatedOpsHeuristic()` — [`L173`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L173)
- <a id="RequiredStorageBytes"></a>`RequiredStorageBytes(absl::Span<const int64_t> view_dimensions, absl::Span<const int64_t> view_strides, mlir::ElementType view_element_type, int64_t view_storage_offset)` — [`L401`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L401)
- <a id="SliceOperandIfNeeded"></a>`SliceOperandIfNeeded(mlir::MlirOp input, const Dimensions& view_dimensions)` — [`L436`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L436) — Slices an MLIR input operand down to view_dimensions if its compiled type

## Module values
- <a id="kRepeatedOpAggressiveMode"></a>`kRepeatedOpAggressiveMode` — [`L171`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L171)
- <a id="kRepeatedOpSafeMode"></a>`kRepeatedOpSafeMode` — [`L170`](../../../../../../raw/code/torch_tpu/csrc/eager/device_buffer_utils.cc#L170)

