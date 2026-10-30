---
title: 'Module: csrc/common/error_utils.h'
type: catalog
provenance: extracted
module: csrc/common/error_utils.h
status: fresh
symbol_base: 'cxx . . $ '
symbols:
  is_status_or_ref: torch_tpu/is_status_or_ref#
  ReturnIfErrorAdaptor: torch_tpu/internal/ReturnIfErrorAdaptor#
  ReturnIfErrorAdaptor.ReturnIfErrorAdaptor: torch_tpu/internal/ReturnIfErrorAdaptor#ReturnIfErrorAdaptor(2814731695a089b8).
  TtError: torch_tpu/TtError#
  kInvalidArgument: torch_tpu/error/kInvalidArgument.
  GetStatus: torch_tpu/GetStatus(8bf3545770fcdbc4).
  ThrowIfErrorAdapter.operator: torch_tpu/internal/ThrowIfErrorAdapter#`operator=`(a265851f2957e2c9).
  ThrowIfErrorAdapter.ThrowIfErrorAdapter: torch_tpu/internal/ThrowIfErrorAdapter#ThrowIfErrorAdapter(89794384c242646).
  ThrowIfErrorAdapter: torch_tpu/internal/ThrowIfErrorAdapter#
  ReturnIfErrorAdaptor.Consume: torch_tpu/internal/ReturnIfErrorAdaptor#Consume(ee7fe3990f364d8d).
  ReturnIfErrorAdaptor.ConsumeRequiringMessage: torch_tpu/internal/ReturnIfErrorAdaptor#ConsumeRequiringMessage(5793c86ea492b1cc).
  kInternal: torch_tpu/error/kInternal.
  kPythonNotImplementedError: torch_tpu/error/kPythonNotImplementedError.
  GetRequiredIntegerEnvOnce: torch_tpu/GetRequiredIntegerEnvOnce(408ce8d7a2250886).
  kFailedPrecondition: torch_tpu/error/kFailedPrecondition.
  SequenceToReadableStr: torch_tpu/SequenceToReadableStr(586d02034d1c85d9).
  kPythonIndexError: torch_tpu/error/kPythonIndexError.
  AnythingCompatibleWithThrow.operator-type-parameter-0-0: torch_tpu/internal/AnythingCompatibleWithThrow#`operator
    type-parameter-0-0`(1e6269539e51e84a).
  GetRequiredEnvOnce: torch_tpu/GetRequiredEnvOnce(185a3e07b793237a).
  AdaptXlaError: torch_tpu/AdaptXlaError(6c93678b1feef568).
  HasStickyError: torch_tpu/HasStickyError(c9857a73d68e59ba).
  kNotFound: torch_tpu/error/kNotFound.
  CheckDeviceIsTpu: absl/torch_tpu/CheckDeviceIsTpu.
  kXlaCompilerFailedWith: absl/torch_tpu/kXlaCompilerFailedWith.
  NumElements: absl/torch_tpu/NumElements.
  kIndexError: torch_tpu/error/kIndexError.
  AnythingCompatibleWithThrow.StaticAssertCanThrow: torch_tpu/internal/AnythingCompatibleWithThrow#StaticAssertCanThrow(49f6e7a06ebc5aa8).
  FormatCount: torch_tpu/FormatCount(52159380abb6ee9b).
  kOk: torch_tpu/error/kOk.
  ReturnIfErrorAdaptor.operator-bool: torch_tpu/internal/ReturnIfErrorAdaptor#`operator
    bool`(50ce9a9e25b4a850).
  TtError.operator: torch_tpu/TtError#`operator=`(75c791c4b7218597).
  kUnavailable: torch_tpu/error/kUnavailable.
  TtError.thrown_from_: absl/torch_tpu/TtError#thrown_from_.
  kPythonRuntimeError: torch_tpu/error/kPythonRuntimeError.
  ReturnIfErrorAdaptor.operator: torch_tpu/internal/ReturnIfErrorAdaptor#`operator=`(fbbe63e777a2106d).
  GetValueAtIndexErrorStr: torch_tpu/GetValueAtIndexErrorStr(5f723b604c97b975).
  ReturnIfErrorAdaptor.-anonymous_type_0.status_: torch_tpu/internal/ReturnIfErrorAdaptor#$anonymous_type_0#status_.
  TtError.status: absl/torch_tpu/TtError#status(7455ad1f6f9a48b1).
  TtError.TtError: torch_tpu/TtError#TtError(37625dab65a739d3).
  TtError.thrown_from: absl/torch_tpu/TtError#thrown_from(ec45a031f4e09d1e).
  ReturnIfErrorAdaptor.-ReturnIfErrorAdaptor: absl/torch_tpu/internal/ReturnIfErrorAdaptor#`~ReturnIfErrorAdaptor`(ced63f7c635d850d).
  kAborted: torch_tpu/error/kAborted.
  kDeadlineExceeded: torch_tpu/error/kDeadlineExceeded.
  IsStatusOrTrait: torch_tpu/internal/IsStatusOrTrait#
  kResourceExhausted: torch_tpu/error/kResourceExhausted.
  TtError.status_: torch_tpu/TtError#status_.
  kDataLoss: torch_tpu/error/kDataLoss.
  kAlreadyExists: absl/torch_tpu/error/kAlreadyExists.
  kCancelled: absl/torch_tpu/error/kCancelled.
  kUnauthenticated: torch_tpu/error/kUnauthenticated.
  kPermissionDenied: absl/torch_tpu/error/kPermissionDenied.
  ReturnIfErrorAdaptor.-anonymous_type_0: absl/torch_tpu/internal/ReturnIfErrorAdaptor#$anonymous_type_0#
  ThrowIfErrorAdapter.function_: torch_tpu/internal/ThrowIfErrorAdapter#function_.
  ThrowIfErrorAdapter.line_: torch_tpu/internal/ThrowIfErrorAdapter#line_.
  ThrowIfErrorAdapter.file_: torch_tpu/internal/ThrowIfErrorAdapter#file_.
  g_has_sticky_error: absl/torch_tpu/internal/g_has_sticky_error.
  AnythingCompatibleWithThrow.AnythingCompatibleWithThrow: absl/torch_tpu/internal/AnythingCompatibleWithThrow#AnythingCompatibleWithThrow(49f6e7a06ebc5aa8).
  ReturnIfErrorAdaptor.-anonymous_type_0.nothing_: absl/torch_tpu/internal/ReturnIfErrorAdaptor#$anonymous_type_0#nothing_.
  AnythingCompatibleWithThrow: torch_tpu/internal/AnythingCompatibleWithThrow#
---
# Module: [`csrc/common/error_utils.h`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h)

## Classes
### `AnythingCompatibleWithThrow`
- def: [`csrc/common/error_utils.h:902`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L902)
- doc: A class that can be implicitly converted to any type T where throwing
- signature: `class AnythingCompatibleWithThrow`
- members:
  - <a id="AnythingCompatibleWithThrow.AnythingCompatibleWithThrow"></a>`AnythingCompatibleWithThrow()` — [`L904`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L904)
  - `AnythingCompatibleWithThrow()` — [`L904`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L904)
  - `StaticAssertCanThrow()` — [`L930`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L930) — Statically asserts that T is a type where throwing in a function returning
  - <a id="AnythingCompatibleWithThrow.StaticAssertCanThrow"></a>`StaticAssertCanThrow()` — [`L930`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L930) — Statically asserts that T is a type where throwing in a function returning
  - <a id="AnythingCompatibleWithThrow.operator-type-parameter-0-0"></a>`operator type-parameter-0-0()` — [`L919`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L919) — This version is for functions that return by value.
  - `operator type-parameter-0-0()` — [`L919`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L919) — This version is for functions that return by value.
  - `operator type-parameter-0-0 &()` — [`L911`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L911) — Allows `return AnythingCompatibleWithThrow();` to compile in any function
  - `operator type-parameter-0-0 &()` — [`L911`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L911) — Allows `return AnythingCompatibleWithThrow();` to compile in any function
- uses (calls/refs, reference-scoped): [`operator<<`](../ops/op_names.h.md#operator), [`operator<<`](status_builder.h.md#operator), [`operator<<`](status_builder.h.md#operator), [`operator<<`](../ops/view_decomposition/strided_layout.cc.md#operator), [`operator<<`](../distributed/types.cc.md#operator), [`operator<<`](../ops/view_decomposition/bitcast_primitive.cc.md#operator), [`operator<<`](../ops/view_decomposition/bitcast_primitive.cc.md#operator), [`operator<<`](../ops/view_decomposition/bitcast_primitive.cc.md#operator), [`operator<<`](../ops/view_decomposition/slice_primitive.cc.md#operator), [`operator<<`](../ops/view_decomposition/bitcast_primitive.cc.md#operator), [`operator<<`](../ops/view_decomposition/bitcast_primitive.cc.md#operator), [`operator<<`](../ops/view_decomposition/reshape_primitive.cc.md#operator), [`operator<<`](../ops/view_decomposition/slice_primitive.cc.md#operator), [`operator<<`](../ops/view_decomposition/transpose_primitive.cc.md#operator), [`IsStatusOrTrait`](error_utils.h.md#IsStatusOrTrait), [`IsStatusOrTrait`](error_utils.h.md#IsStatusOrTrait)

### <a id="IsStatusOrTrait"></a>`IsStatusOrTrait`  ·  implements/extends integral_constant
- def: [`csrc/common/error_utils.h:895`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L895)
- doc: IsStatusOrTrait<Type>::value is true iff Type is an absl::StatusOr<>.
- signature: `template <typename T> struct IsStatusOrTrait : std::false_type`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`StaticAssertCanThrow`](error_utils.h.md#AnythingCompatibleWithThrow.StaticAssertCanThrow)

### <a id="ReturnIfErrorAdaptor"></a>`ReturnIfErrorAdaptor`
- def: [`csrc/common/error_utils.h:831`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L831) — documented in [error-handling](../../../concepts/error-handling.md)
- doc: Special adaptor for use by TT_RETURN_IF_ERROR for absl::Status
- signature: `class ReturnIfErrorAdaptor`
- members:
  - `Consume(const std::string_view file, const int line, const std::string_view function)` — [`L878`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L878) — Returns a status builder that contains a copy of the original status,
  - `Consume(const std::string_view file, const int line, const std::string_view function)` — [`L878`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L878) — Returns a status builder that contains a copy of the original status,
  - `Consume()` — [`L861`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L861) — Returns a status builder based on the original status.
  - <a id="ReturnIfErrorAdaptor.Consume"></a>`Consume()` — [`L861`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L861) — Returns a status builder based on the original status.
  - `ConsumeRequiringMessage()` — [`L867`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L867) — Like Consume(), but enforces at compile time that the caller to stream at
  - <a id="ReturnIfErrorAdaptor.ConsumeRequiringMessage"></a>`ConsumeRequiringMessage()` — [`L867`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L867) — Like Consume(), but enforces at compile time that the caller to stream at
  - <a id="ReturnIfErrorAdaptor.ReturnIfErrorAdaptor"></a>`ReturnIfErrorAdaptor(absl::Status status)` — [`L833`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L833)
  - `ReturnIfErrorAdaptor(absl::Status status)` — [`L833`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L833)
  - `ReturnIfErrorAdaptor()` — [`L836`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L836)
  - `ReturnIfErrorAdaptor(const ReturnIfErrorAdaptor&)` — [`L837`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L837)
  - `ReturnIfErrorAdaptor(const ReturnIfErrorAdaptor&)` — [`L837`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L837)
  - `ReturnIfErrorAdaptor()` — [`L836`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L836)
  - <a id="ReturnIfErrorAdaptor.operator-bool"></a>`operator bool()` — [`L854`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L854)
  - `operator bool()` — [`L854`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L854)
  - <a id="ReturnIfErrorAdaptor.operator"></a>`operator=(const ReturnIfErrorAdaptor&)` — [`L838`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L838)
  - `operator=(const ReturnIfErrorAdaptor&)` — [`L838`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L838)
  - <a id="ReturnIfErrorAdaptor.-ReturnIfErrorAdaptor"></a>`~ReturnIfErrorAdaptor()` — [`L840`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L840)
  - `~ReturnIfErrorAdaptor()` — [`L840`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L840)
- uses (calls/refs, reference-scoped): [`MaybeAddCppSourceLoc`](status_builder.cc.md#MaybeAddCppSourceLoc), [`StatusBuilder`](status_builder.h.md#StatusBuilder), [`StatusBuilderWithMessage`](status_builder.h.md#StatusBuilderWithMessage), [`StatusBuilder`](status_builder.cc.md#StatusBuilder.StatusBuilder), [`status_`](error_utils.h.md#ReturnIfErrorAdaptor.-anonymous_type_0.status_), [`ReturnIfErrorAdaptor`](error_utils.h.md#ReturnIfErrorAdaptor), [`status_`](error_utils.h.md#ReturnIfErrorAdaptor.-anonymous_type_0.status_)
- used by: [`CreateDeferred`](../eager/device_buffer.cc.md#DeviceBufferList.CreateDeferred), [`UnaryOpOut`](../ops/unary_aten_kernels.cc.md#UnaryOpOut), [`ReshapeFromStaticDimensions`](../ops/op_builder_utils.cc.md#ReshapeFromStaticDimensions), [`LstmInputBackwardImpl`](../ops/lstm/lstm_aten_kernels.cc.md#LstmInputBackwardImpl), [`SyncAndCheckStickyError`](error_utils.cc.md#SyncAndCheckStickyError), [`alltoall`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.alltoall), [`BinaryOpOut`](../ops/binary_aten_kernels.h.md#BinaryOpOut), [`operator[]`](../eager/device_buffer.cc.md#DeviceBufferList.Data.operator), [`AtenPreluKernelBackward`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernelBackward), [`AtenMaskedScatter_`](../ops/masked_scatter/masked_scatter_aten_kernels.cc.md#AtenMaskedScatter_), [`AtenPreluKernel`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernel), [`AtenWeightNormInterface`](../ops/weight_norm/weight_norm_aten_kernels.cc.md#AtenWeightNormInterface), [`ContiguousToView`](../ops/view_decomposition/contiguous_to_view.cc.md#ContiguousToView), [`AtenChannelShuffle`](../ops/channel_shuffle/channel_shuffle_aten_kernels.cc.md#AtenChannelShuffle), [`AtenIndexTensorOut`](../ops/index/index_aten_kernels.cc.md#AtenIndexTensorOut), [`SliceModuleCacheKey`](cache_key.cc.md#SliceModuleCacheKey), [`allgather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allgather), [`AtenCtcLossTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`AtenVarMeanCorrection`](../ops/reductions/var_aten_kernels.cc.md#AtenVarMeanCorrection), [`AtenDigammaOut`](../ops/digamma/digamma_aten_kernels.cc.md#AtenDigammaOut), [`_allgather_base`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu._allgather_base), [`AtenBinCount`](../ops/bincount/bincount_aten_kernels.cc.md#AtenBinCount), [`CreateDeferredDeviceBufferList`](../eager/device_buffer_utils.cc.md#CreateDeferredDeviceBufferList), [`AtenCtcLossBackwardTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossBackwardTensor), [`CreatePlaceholder`](../eager/device_buffer.cc.md#DeviceBufferList.CreatePlaceholder), [`AtenRmsNorm`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenRmsNorm), [`TORCH_LIBRARY_IMPL_static_init_tpu_Meta_10`](../eager/tpu_aten_kernels.cc.md#TORCH_LIBRARY_IMPL_static_init_tpu_Meta_10), [`allreduce`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allreduce), [`AtenLinalgLuSolveOut`](../ops/linalg/lu/linalg_lu_kernels.cc.md#AtenLinalgLuSolveOut), [`PyCreateAssociativeScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateAssociativeScanOp), [`AtenFusedRmsNorm`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNorm), [`AtenArangeStartOut`](../ops/arange/arange_aten_kernels.cc.md#AtenArangeStartOut), [`AtenFusedRmsNormBackward`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNormBackward), [`AtenLinalgSolveExOut`](../ops/linalg/linalg_kernels.cc.md#AtenLinalgSolveExOut), [`AtenReplicationPad3dBackward`](../ops/replication_pad/replication_pad_aten_kernels.cc.md#AtenReplicationPad3dBackward), [`gather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.gather), [`AtenLinalgSvdU`](../ops/linalg/linalg_svd_kernels.cc.md#AtenLinalgSvdU), [`AtenSegmentReduce`](../ops/segment_reduce/segment_reduce_aten_kernels.cc.md#AtenSegmentReduce), [`GetClient`](../pjrt/pjrt_state.cc.md#PjrtBackend.GetClient), [`_reduce_scatter_base`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu._reduce_scatter_base)  (+875 more)

### `ReturnIfErrorAdaptor.-anonymous_type_0`
- def: [`csrc/common/error_utils.h:887`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L887)
- doc: Place the status inside a union so we can avoid generating unnecessary code
- signature: `union`
- members:
  - <a id="ReturnIfErrorAdaptor.-anonymous_type_0.nothing_"></a>`nothing_` — [`L889`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L889)
  - `nothing_` — [`L889`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L889)
  - <a id="ReturnIfErrorAdaptor.-anonymous_type_0.status_"></a>`status_` — [`L888`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L888)
  - `status_` — [`L888`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L888)
- used by: [`ReturnIfErrorAdaptor`](error_utils.h.md#ReturnIfErrorAdaptor.ReturnIfErrorAdaptor), [`Consume`](error_utils.h.md#ReturnIfErrorAdaptor.Consume), [`ConsumeRequiringMessage`](error_utils.h.md#ReturnIfErrorAdaptor.ConsumeRequiringMessage), [`Consume`](error_utils.h.md#ReturnIfErrorAdaptor.Consume), [`operator bool`](error_utils.h.md#ReturnIfErrorAdaptor.operator-bool)

### `ThrowIfErrorAdapter`
- def: [`csrc/common/error_utils.h:791`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L791)
- doc: Special adaptor for use by TT_THROW_IF_ERROR for absl::Status
- signature: `class ThrowIfErrorAdapter`
- members:
  - `ThrowIfErrorAdapter(const char* file, uint32_t line, const char* function)` — [`L793`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L793)
  - `ThrowIfErrorAdapter(ThrowIfErrorAdapter&&)` — [`L799`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L799)
  - `ThrowIfErrorAdapter(const ThrowIfErrorAdapter&)` — [`L797`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L797) — This is trivially copyable and movable.
  - <a id="ThrowIfErrorAdapter.ThrowIfErrorAdapter"></a>`ThrowIfErrorAdapter(const char* file, uint32_t line, const char* function)` — [`L793`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L793)
  - `ThrowIfErrorAdapter(ThrowIfErrorAdapter&&)` — [`L799`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L799)
  - `ThrowIfErrorAdapter(const ThrowIfErrorAdapter&)` — [`L797`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L797) — This is trivially copyable and movable.
  - `operator=(const absl::Status& status)` — [`L813`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L813) — Converts a Status to a python exception. The weird choice of
  - `operator=(ThrowIfErrorAdapter&&)` — [`L800`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L800)
  - `operator=(const ThrowIfErrorAdapter&)` — [`L798`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L798)
  - <a id="ThrowIfErrorAdapter.operator"></a>`operator=(const absl::Status& status)` — [`L813`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L813) — Converts a Status to a python exception. The weird choice of
  - `operator=(ThrowIfErrorAdapter&&)` — [`L800`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L800)
  - `operator=(const ThrowIfErrorAdapter&)` — [`L798`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L798)
  - <a id="ThrowIfErrorAdapter.file_"></a>`file_` — [`L819`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L819)
  - `file_` — [`L819`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L819)
  - <a id="ThrowIfErrorAdapter.function_"></a>`function_` — [`L821`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L821)
  - `function_` — [`L821`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L821)
  - `line_` — [`L820`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L820)
  - <a id="ThrowIfErrorAdapter.line_"></a>`line_` — [`L820`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L820)
- uses (calls/refs, reference-scoped): [`TtError`](error_utils.cc.md#TtError.TtError), [`TtError`](error_utils.h.md#TtError), [`ThrowIfErrorAdapter`](error_utils.h.md#ThrowIfErrorAdapter)
- used by: [`SyncAndCheckStickyError`](error_utils.cc.md#SyncAndCheckStickyError), [`alltoall`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.alltoall), [`AtenPreluKernelBackward`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernelBackward), [`AtenMaskedScatter_`](../ops/masked_scatter/masked_scatter_aten_kernels.cc.md#AtenMaskedScatter_), [`AtenPreluKernel`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernel), [`AtenWeightNormInterface`](../ops/weight_norm/weight_norm_aten_kernels.cc.md#AtenWeightNormInterface), [`AtenChannelShuffle`](../ops/channel_shuffle/channel_shuffle_aten_kernels.cc.md#AtenChannelShuffle), [`AtenIndexTensorOut`](../ops/index/index_aten_kernels.cc.md#AtenIndexTensorOut), [`SliceModuleCacheKey`](cache_key.cc.md#SliceModuleCacheKey), [`allgather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allgather), [`AtenCtcLossTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`AtenVarMeanCorrection`](../ops/reductions/var_aten_kernels.cc.md#AtenVarMeanCorrection), [`AtenDigammaOut`](../ops/digamma/digamma_aten_kernels.cc.md#AtenDigammaOut), [`_allgather_base`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu._allgather_base), [`AtenBinCount`](../ops/bincount/bincount_aten_kernels.cc.md#AtenBinCount), [`AtenCtcLossBackwardTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossBackwardTensor), [`AtenRmsNorm`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenRmsNorm), [`TORCH_LIBRARY_IMPL_static_init_tpu_Meta_10`](../eager/tpu_aten_kernels.cc.md#TORCH_LIBRARY_IMPL_static_init_tpu_Meta_10), [`allreduce`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allreduce), [`AtenLinalgLuSolveOut`](../ops/linalg/lu/linalg_lu_kernels.cc.md#AtenLinalgLuSolveOut), [`PyCreateAssociativeScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateAssociativeScanOp), [`AtenFusedRmsNorm`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNorm), [`AtenArangeStartOut`](../ops/arange/arange_aten_kernels.cc.md#AtenArangeStartOut), [`AtenFusedRmsNormBackward`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNormBackward), [`AtenLinalgSolveExOut`](../ops/linalg/linalg_kernels.cc.md#AtenLinalgSolveExOut), [`AtenReplicationPad3dBackward`](../ops/replication_pad/replication_pad_aten_kernels.cc.md#AtenReplicationPad3dBackward), [`gather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.gather), [`AtenLinalgSvdU`](../ops/linalg/linalg_svd_kernels.cc.md#AtenLinalgSvdU), [`AtenSegmentReduce`](../ops/segment_reduce/segment_reduce_aten_kernels.cc.md#AtenSegmentReduce), [`_reduce_scatter_base`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu._reduce_scatter_base), [`AtenLinalgInvExInverse`](../ops/linalg/linalg_kernels.cc.md#AtenLinalgInvExInverse), [`AtenAdaptiveAvgPool3dOut`](../ops/pooling/adaptive_avg_pool_aten_kernels.cc.md#AtenAdaptiveAvgPool3dOut), [`AtenGridSampler3dBackward`](../ops/grid_sampler/grid_sampler_aten_kernels.cc.md#AtenGridSampler3dBackward), [`AtenNativeGroupNormBackward`](../ops/group_norm/group_norm_aten_kernels.cc.md#AtenNativeGroupNormBackward), [`AtenViewAsComplex`](../ops/view/view_aten_kernels.cc.md#AtenViewAsComplex), [`AtenCdistBackward`](../ops/distance/dist_aten_kernels.cc.md#AtenCdistBackward), [`AtenCdistForward`](../ops/distance/dist_aten_kernels.cc.md#AtenCdistForward), [`AtenExponential_`](../ops/exponential/exponential_aten_kernels.cc.md#AtenExponential_), [`AtenLinalgLuFactorExOut`](../ops/linalg/lu/linalg_lu_kernels.cc.md#AtenLinalgLuFactorExOut), [`AtenLinspaceOut`](../ops/linspace/linspace_aten_kernels.cc.md#AtenLinspaceOut)  (+646 more)

### <a id="TtError"></a>`TtError`  ·  implements/extends runtime_error
- def: [`csrc/common/error_utils.h:348`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L348) — documented in [error-handling](../../../concepts/error-handling.md)
- doc: An exception thrown by a TT_* macro. It's a std::runtime_error with two
- signature: `class TtError : public std::runtime_error`
- members:
  - `TtError(TtError&& other)` — [`L352`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L352)
  - <a id="TtError.TtError"></a>`TtError(const TtError&)` — [`L354`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L354)
  - `TtError(TtError&& other)` — [`L352`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L352)
  - `TtError(const TtError&)` — [`L354`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L354)
  - `operator=(const TtError&)` — [`L355`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L355)
  - `operator=(TtError&& other)` — [`L353`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L353)
  - <a id="TtError.operator"></a>`operator=(const TtError&)` — [`L355`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L355)
  - `operator=(TtError&& other)` — [`L353`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L353)
  - <a id="TtError.status"></a>`status()` — [`L358`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L358) — Getters.
  - `status()` — [`L358`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L358) — Getters.
  - `thrown_from()` — [`L359`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L359)
  - <a id="TtError.thrown_from"></a>`thrown_from()` — [`L359`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L359)
  - `status_` — [`L364`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L364) — Invariant: must not be OK.
  - <a id="TtError.status_"></a>`status_` — [`L364`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L364) — Invariant: must not be OK.
  - `thrown_from_` — [`L365`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L365)
  - <a id="TtError.thrown_from_"></a>`thrown_from_` — [`L365`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L365)
- uses (calls/refs, reference-scoped): [`TranslateToC10ErrorAndThrow`](error_utils.cc.md#TranslateToC10ErrorAndThrow), [`TtError`](error_utils.h.md#TtError)
- used by: [`TranslateToC10ErrorAndThrow`](error_utils.cc.md#TranslateToC10ErrorAndThrow), [`TtError`](error_utils.cc.md#TtError.TtError), [`operator=`](error_utils.h.md#ThrowIfErrorAdapter.operator), [`TorchTpuPyBindInitModule_tpu_torch_compile`](../internal/compile/tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`alltoall`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.alltoall), [`AtenPreluKernelBackward`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernelBackward), [`PadModuleCacheKey`](cache_key.cc.md#PadModuleCacheKey), [`AtenMaskedScatter_`](../ops/masked_scatter/masked_scatter_aten_kernels.cc.md#AtenMaskedScatter_), [`AtenPreluKernel`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernel), [`AtenWeightNormInterface`](../ops/weight_norm/weight_norm_aten_kernels.cc.md#AtenWeightNormInterface), [`AtenChannelShuffle`](../ops/channel_shuffle/channel_shuffle_aten_kernels.cc.md#AtenChannelShuffle), [`AtenIndexTensorOut`](../ops/index/index_aten_kernels.cc.md#AtenIndexTensorOut), [`allgather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allgather), [`AtenCtcLossTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`AtenVarMeanCorrection`](../ops/reductions/var_aten_kernels.cc.md#AtenVarMeanCorrection), [`AtenDigammaOut`](../ops/digamma/digamma_aten_kernels.cc.md#AtenDigammaOut), [`_allgather_base`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu._allgather_base), [`AtenBinCount`](../ops/bincount/bincount_aten_kernels.cc.md#AtenBinCount), [`AtenCtcLossBackwardTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossBackwardTensor), [`AtenRmsNorm`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenRmsNorm), [`TORCH_LIBRARY_IMPL_static_init_tpu_Meta_10`](../eager/tpu_aten_kernels.cc.md#TORCH_LIBRARY_IMPL_static_init_tpu_Meta_10), [`allreduce`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allreduce), [`AtenLinalgLuSolveOut`](../ops/linalg/lu/linalg_lu_kernels.cc.md#AtenLinalgLuSolveOut), [`PyCreateAssociativeScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateAssociativeScanOp), [`AtenFusedRmsNorm`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNorm), [`AtenArangeStartOut`](../ops/arange/arange_aten_kernels.cc.md#AtenArangeStartOut), [`AtenFusedRmsNormBackward`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNormBackward), [`AtenLinalgSolveExOut`](../ops/linalg/linalg_kernels.cc.md#AtenLinalgSolveExOut), [`AtenReplicationPad3dBackward`](../ops/replication_pad/replication_pad_aten_kernels.cc.md#AtenReplicationPad3dBackward), [`gather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.gather), [`AtenLinalgSvdU`](../ops/linalg/linalg_svd_kernels.cc.md#AtenLinalgSvdU), [`AtenSegmentReduce`](../ops/segment_reduce/segment_reduce_aten_kernels.cc.md#AtenSegmentReduce), [`_reduce_scatter_base`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu._reduce_scatter_base), [`AtenLinalgInvExInverse`](../ops/linalg/linalg_kernels.cc.md#AtenLinalgInvExInverse), [`AtenAdaptiveAvgPool3dOut`](../ops/pooling/adaptive_avg_pool_aten_kernels.cc.md#AtenAdaptiveAvgPool3dOut), [`AtenGridSampler3dBackward`](../ops/grid_sampler/grid_sampler_aten_kernels.cc.md#AtenGridSampler3dBackward), [`AtenNativeGroupNormBackward`](../ops/group_norm/group_norm_aten_kernels.cc.md#AtenNativeGroupNormBackward), [`AtenViewAsComplex`](../ops/view/view_aten_kernels.cc.md#AtenViewAsComplex), [`AtenCdistBackward`](../ops/distance/dist_aten_kernels.cc.md#AtenCdistBackward), [`AtenCdistForward`](../ops/distance/dist_aten_kernels.cc.md#AtenCdistForward)  (+871 more)

### <a id="is_status_or_ref"></a>`is_status_or_ref`  ·  implements/extends integral_constant
- def: [`csrc/common/error_utils.h:1164`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L1164) — documented in [error-handling](../../../concepts/error-handling.md)
- doc: Trait: is the type a StatusOr<T&>?
- signature: `template <typename T> struct is_status_or_ref : std::false_type`
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`PromoteScalar`](../eager/op_dispatcher.cc.md#PromoteScalar), [`CastIfNeeded`](../ops/op_builder_utils.cc.md#CastIfNeeded), [`ConvertTo`](dtype.h.md#ConvertTo), [`ConvertTo`](dtype.h.md#ConvertTo), [`ConvertTo`](dtype.h.md#ConvertTo), [`MakeConstantLike`](../ops/op_builder_utils.cc.md#MakeConstantLike), [`AssignBufferToAtTensor`](../eager/tensor_to_buffer.cc.md#AssignBufferToAtTensor), [`UnaryOpOut`](../ops/unary_aten_kernels.cc.md#UnaryOpOut), [`Unsqueeze`](../ops/op_builder_utils.cc.md#Unsqueeze), [`DispatchOp`](../eager/op_dispatcher.h.md#DispatchOp), [`ReshapeFromStaticDimensions`](../ops/op_builder_utils.cc.md#ReshapeFromStaticDimensions), [`NumElements`](error_utils.cc.md#NumElements), [`LstmInputBackwardImpl`](../ops/lstm/lstm_aten_kernels.cc.md#LstmInputBackwardImpl), [`MakeTensor`](../eager/op_dispatcher.cc.md#MakeTensor), [`TorchTpuPyBindInitModule_tpu_torch_compile`](../internal/compile/tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`ComputeInverseViewOperation`](../ops/view_decomposition/inversion.cc.md#ComputeInverseViewOperation), [`alltoall`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.alltoall), [`AtenPreluKernelBackward`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernelBackward), [`PadModuleCacheKey`](cache_key.cc.md#PadModuleCacheKey), [`AtenMaskedScatter_`](../ops/masked_scatter/masked_scatter_aten_kernels.cc.md#AtenMaskedScatter_), [`AtenPreluKernel`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernel), [`GetBuffer`](../eager/tensor_to_buffer.cc.md#GetBuffer), [`CreateViewDeviceBufferRef`](../eager/device_buffer_utils.cc.md#CreateViewDeviceBufferRef), [`AtenWeightNormInterface`](../ops/weight_norm/weight_norm_aten_kernels.cc.md#AtenWeightNormInterface), [`TraverseAndCompile`](../internal/compile/compiled_mode.cc.md#TraverseAndCompile), [`ContiguousToView`](../ops/view_decomposition/contiguous_to_view.cc.md#ContiguousToView), [`AtenChannelShuffle`](../ops/channel_shuffle/channel_shuffle_aten_kernels.cc.md#AtenChannelShuffle), [`AtenIndexTensorOut`](../ops/index/index_aten_kernels.cc.md#AtenIndexTensorOut), [`allgather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allgather), [`AtenCtcLossTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`AtenVarMeanCorrection`](../ops/reductions/var_aten_kernels.cc.md#AtenVarMeanCorrection), [`AtenDigammaOut`](../ops/digamma/digamma_aten_kernels.cc.md#AtenDigammaOut), [`_allgather_base`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu._allgather_base), [`AtenBinCount`](../ops/bincount/bincount_aten_kernels.cc.md#AtenBinCount), [`CreateDeferredDeviceBufferList`](../eager/device_buffer_utils.cc.md#CreateDeferredDeviceBufferList), [`AtenCtcLossBackwardTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossBackwardTensor), [`AtenRmsNorm`](../ops/rms_norm/rms_norm_aten_kernels.cc.md#AtenRmsNorm), [`TORCH_LIBRARY_IMPL_static_init_tpu_Meta_10`](../eager/tpu_aten_kernels.cc.md#TORCH_LIBRARY_IMPL_static_init_tpu_Meta_10), [`allreduce`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allreduce), [`AtenLinalgLuSolveOut`](../ops/linalg/lu/linalg_lu_kernels.cc.md#AtenLinalgLuSolveOut)  (+1726 more)

## Functions
- <a id="AdaptXlaError"></a>`AdaptXlaError(absl::StatusOr<T> status_or, const std::string_view context)` — [`L231`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L231) — documented in [error-handling](../../../concepts/error-handling.md)
- `FormatCount(const int64_t count, const std::string_view singular, const std::string_view plural)` — [`L250`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L250) — Formats the given number of items. E.g.
- <a id="FormatCount"></a>`FormatCount(const int64_t count, const std::string_view singular, const std::string_view plural)` — [`L250`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L250) — Formats the given number of items. E.g.
- `GetRequiredEnvOnce()` — [`L1226`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L1226) — Returns the value of the environment variable with the given name, or an
- <a id="GetRequiredEnvOnce"></a>`GetRequiredEnvOnce()` — [`L1226`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L1226) — Returns the value of the environment variable with the given name, or an
- <a id="GetRequiredIntegerEnvOnce"></a>`GetRequiredIntegerEnvOnce()` — [`L1242`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L1242) — Returns the integer value of the environment variable with the given name, or
- `GetRequiredIntegerEnvOnce()` — [`L1242`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L1242) — Returns the integer value of the environment variable with the given name, or
- <a id="GetStatus"></a>`GetStatus(absl::Status&& status)` — [`L329`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L329) — documented in [error-handling](../../../concepts/error-handling.md)
- `GetStatus(const absl::StatusOr<T>& status_or)` — [`L333`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L333)
- `GetStatus(absl::StatusOr<T>&& status_or)` — [`L337`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L337)
- `GetStatus(const absl::StatusOr<T>& status_or)` — [`L333`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L333)
- `GetStatus(const absl::Status& status)` — [`L326`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L326) — Retrieves the status from a Status or StatusOr. Useful for contexts where we
- `GetStatus(absl::Status&& status)` — [`L329`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L329)
- `GetStatus(const absl::Status& status)` — [`L326`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L326) — Retrieves the status from a Status or StatusOr. Useful for contexts where we
- <a id="GetValueAtIndexErrorStr"></a>`GetValueAtIndexErrorStr(absl::Span<const int64_t> indices, const ToValue& to_value)` — [`L267`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L267) — Format a list of indices as a comma-separated error string.
- `HasStickyError()` — [`L177`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L177) — Returns true if the global sticky error state is set.
- <a id="HasStickyError"></a>`HasStickyError()` — [`L177`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L177) — Returns true if the global sticky error state is set.
- `SequenceToReadableStr(absl::Span<const Value> values, const ValueToString& value_to_string)` — [`L292`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L292) — Formats a list of `values` into a readable string.
- <a id="SequenceToReadableStr"></a>`SequenceToReadableStr(absl::Span<const Value> values)` — [`L318`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L318)

## Module values
- `AdaptXlaError` — [`L231`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L231)
- <a id="CheckDeviceIsTpu"></a>`CheckDeviceIsTpu` — [`L157`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L157) — Checks that `device_opt` is TPU (PrivateUse1), or crashes if it is not.
- `GetStatus` — [`L337`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L337)
- `GetValueAtIndexErrorStr` — [`L267`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L267) — Format a list of indices as a comma-separated error string.
- <a id="NumElements"></a>`NumElements` — [`L137`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L137) — Returns the number of elements in a tensor with the given dimensions.
- `SequenceToReadableStr` — [`L292`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L292) — Formats a list of `values` into a readable string.
- <a id="g_has_sticky_error"></a>`g_has_sticky_error` — [`L173`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L173)
- <a id="kAborted"></a>`kAborted` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L63) — Aliases for absl::StatusCode enums.
- `kAborted` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L63) — Aliases for absl::StatusCode enums.
- `kAlreadyExists` — [`L65`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L65)
- <a id="kAlreadyExists"></a>`kAlreadyExists` — [`L65`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L65)
- <a id="kCancelled"></a>`kCancelled` — [`L67`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L67)
- `kCancelled` — [`L67`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L67)
- <a id="kDataLoss"></a>`kDataLoss` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L69)
- `kDataLoss` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L69)
- <a id="kDeadlineExceeded"></a>`kDeadlineExceeded` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L71)
- `kDeadlineExceeded` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L71)
- `kFailedPrecondition` — [`L73`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L73)
- <a id="kFailedPrecondition"></a>`kFailedPrecondition` — [`L73`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L73)
- <a id="kIndexError"></a>`kIndexError` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L75)
- `kIndexError` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L75)
- <a id="kInternal"></a>`kInternal` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L77)
- `kInternal` — [`L77`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L77)
- `kInvalidArgument` — [`L79`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L79)
- <a id="kInvalidArgument"></a>`kInvalidArgument` — [`L79`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L79) — documented in [stablehlo-op-builder](../../../concepts/stablehlo-op-builder.md)
- `kNotFound` — [`L81`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L81)
- <a id="kNotFound"></a>`kNotFound` — [`L81`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L81)
- `kOk` — [`L83`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L83)
- <a id="kOk"></a>`kOk` — [`L83`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L83)
- `kPermissionDenied` — [`L85`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L85)
- <a id="kPermissionDenied"></a>`kPermissionDenied` — [`L85`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L85)
- <a id="kPythonIndexError"></a>`kPythonIndexError` — [`L97`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L97) — StatusCode aliases for Python error kinds.
- `kPythonIndexError` — [`L97`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L97) — StatusCode aliases for Python error kinds.
- `kPythonNotImplementedError` — [`L99`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L99)
- <a id="kPythonNotImplementedError"></a>`kPythonNotImplementedError` — [`L99`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L99)
- `kPythonRuntimeError` — [`L101`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L101)
- <a id="kPythonRuntimeError"></a>`kPythonRuntimeError` — [`L101`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L101)
- `kResourceExhausted` — [`L87`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L87)
- <a id="kResourceExhausted"></a>`kResourceExhausted` — [`L87`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L87)
- <a id="kUnauthenticated"></a>`kUnauthenticated` — [`L89`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L89)
- `kUnauthenticated` — [`L89`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L89)
- `kUnavailable` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L91)
- <a id="kUnavailable"></a>`kUnavailable` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L91)
- <a id="kXlaCompilerFailedWith"></a>`kXlaCompilerFailedWith` — [`L116`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L116) — Sentinel string for XLA compiler errors.
- `kXlaCompilerFailedWith` — [`L116`](../../../../../../raw/code/torch_tpu/csrc/common/error_utils.h#L116) — Sentinel string for XLA compiler errors.

