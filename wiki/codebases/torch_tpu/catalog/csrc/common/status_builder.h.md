---
title: 'Module: csrc/common/status_builder.h'
type: catalog
provenance: extracted
module: csrc/common/status_builder.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  StatusBuilder: StatusBuilder#
  StatusBuilder.operator: StatusBuilder#`operator<<`(eb3a3f69b0dc5ccb).
  operator: '`operator<<`(f070428b10606a60).'
  StatusBuilderWithMessage: StatusBuilderWithMessage#
  StatusBuilder.SetPrepend: StatusBuilder#SetPrepend(7a0f075352295503).
  StatusBuilder.Rep: StatusBuilder#Rep#
  StatusBuilder.SetOverride: StatusBuilder#SetOverride(7a0f075352295503).
  StatusBuilder.rep_: StatusBuilder#rep_.
  StatusBuilder.Rep.message_join_style: StatusBuilder#Rep#message_join_style.
  kRootOpNameUrl: internal/kRootOpNameUrl.
  StatusBuilder.Rep.stream: StatusBuilder#Rep#stream.
  kCppErrorTraceUrl: internal/kCppErrorTraceUrl.
  StatusBuilder.MessageJoinStyle: StatusBuilder#MessageJoinStyle#
  StatusBuilder.Rep.status: StatusBuilder#Rep#status.
  StatusBuilderWithMessage.StatusBuilderWithMessage: StatusBuilderWithMessage#StatusBuilderWithMessage(c2f12816a211f944).
  StatusBuilderWithMessage.operator-Status: StatusBuilderWithMessage#`operator Status`(d69269dbbecbffa7).
  StatusBuilder.StatusBuilder: StatusBuilder#StatusBuilder(92e4302bfdc18b1c).
  StatusBuilder.ok: StatusBuilder#ok(50ce9a9e25b4a850).
  StatusBuilder.Rep.InitRep: StatusBuilder#Rep#InitRep(d910431b67e4195c).
  StatusBuilder.MessageJoinStyle.kAppend: StatusBuilder#MessageJoinStyle#kAppend.
  StatusBuilder.MessageJoinStyle.kOverride: StatusBuilder#MessageJoinStyle#kOverride.
  StatusBuilder.operator-type-parameter-0-0: StatusBuilder#`operator type-parameter-0-0`(8f5363d873dd4781).
  StatusBuilder.MessageJoinStyle.kPrepend: StatusBuilder#MessageJoinStyle#kPrepend.
---
# Module: [`csrc/common/status_builder.h`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h)

## Classes
### <a id="StatusBuilder"></a>`StatusBuilder`
- def: [`csrc/common/status_builder.h:63`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L63) — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)
- doc: Creates a Status based on an original_status, but enriched with additional
- signature: `class [[nodiscard]] StatusBuilder`
- members:
  - `SetOverride()` — [`L251`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L251)
  - <a id="StatusBuilder.SetOverride"></a>`SetOverride()` — [`L246`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L246) — Mutates the builder so that the final additional message overrides the
  - `SetPrepend()` — [`L242`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L242)
  - <a id="StatusBuilder.SetPrepend"></a>`SetPrepend()` — [`L237`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L237) — Mutates the builder so that the final additional message is prepended to
  - `StatusBuilder(StatusBuilder&&)` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L75)
  - <a id="StatusBuilder.StatusBuilder"></a>`StatusBuilder(const StatusBuilder& sb)` — [`L222`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L222) — StatusBuilder is copyable and movable. — documented in [error-handling](../../../concepts/error-handling.md)
  - <a id="StatusBuilder.ok"></a>`ok()` — [`L271`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L271) — Returns true if the Status created by this builder will be ok().
  - <a id="StatusBuilder.operator-type-parameter-0-0"></a>`operator type-parameter-0-0()` — [`L117`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L117) — This operator prevents the StatusBuilder from being converted to an
  - `operator<<(const T& value)` — [`L256`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L256) — Appends to the extra message that will be added to the original status.  By
  - <a id="StatusBuilder.operator"></a>`operator<<(const T& value)` — [`L267`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L267) — documented in [error-handling](../../../concepts/error-handling.md)
  - `operator=(StatusBuilder&&)` — [`L76`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L76)
  - `operator=(const StatusBuilder& sb)` — [`L228`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L228)
  - <a id="StatusBuilder.rep_"></a>`rep_` — [`L189`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L189) — nullptr if the result status will be OK.  Extra fields moved to the heap to
- uses (calls/refs, reference-scoped): [`operator<<`](status_builder.h.md#operator), [`operator<<`](status_builder.h.md#operator), [`StatusBuilderWithMessage`](status_builder.h.md#StatusBuilderWithMessage), [`StatusBuilder`](status_builder.cc.md#StatusBuilder.StatusBuilder), [`Rep`](status_builder.h.md#StatusBuilder.Rep), [`message_join_style`](status_builder.h.md#StatusBuilder.Rep.message_join_style), [`stream`](status_builder.h.md#StatusBuilder.Rep.stream), [`MessageJoinStyle`](status_builder.h.md#StatusBuilder.MessageJoinStyle), [`status`](status_builder.h.md#StatusBuilder.Rep.status), [`StatusBuilder`](status_builder.cc.md#StatusBuilder.StatusBuilder), [`InitStream`](status_builder.cc.md#StatusBuilder.Rep.InitStream), [`kOverride`](status_builder.h.md#StatusBuilder.MessageJoinStyle.kOverride), [`kPrepend`](status_builder.h.md#StatusBuilder.MessageJoinStyle.kPrepend), [`StatusBuilder`](status_builder.cc.md#StatusBuilder.StatusBuilder), [`~StatusBuilder`](status_builder.cc.md#StatusBuilder.-StatusBuilder)
- used by: [`operator<<`](status_builder.h.md#operator), [`StatusBuilderWithMessage`](status_builder.h.md#StatusBuilderWithMessage), [`StatusBuilder`](status_builder.cc.md#StatusBuilder.StatusBuilder), [`CastIfNeeded`](../ops/op_builder_utils.cc.md#CastIfNeeded), [`BroadcastIfNeeded`](../ops/op_builder_utils.cc.md#BroadcastIfNeeded), [`CreateDeferred`](../eager/device_buffer.cc.md#DeviceBufferList.CreateDeferred), [`SafeWrapDim`](error_utils.cc.md#SafeWrapDim), [`BroadcastIfNeeded`](../ops/op_builder_utils.cc.md#BroadcastIfNeeded), [`AssignBufferToAtTensor`](../eager/tensor_to_buffer.cc.md#AssignBufferToAtTensor), [`UnaryOpOut`](../ops/unary_aten_kernels.cc.md#UnaryOpOut), [`DispatchOp`](../eager/op_dispatcher.h.md#DispatchOp), [`NumElements`](error_utils.cc.md#NumElements), [`LstmInputBackwardImpl`](../ops/lstm/lstm_aten_kernels.cc.md#LstmInputBackwardImpl), [`SafeMultiply`](error_utils.cc.md#SafeMultiply), [`TorchTpuPyBindInitModule_tpu_torch_compile`](../internal/compile/tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`AdaptXlaError`](error_utils.cc.md#AdaptXlaError), [`AdaptVfioDeviceCollisionError`](error_utils.cc.md#AdaptVfioDeviceCollisionError), [`Broadcast`](../ops/op_builder_utils.cc.md#Broadcast), [`SafeMultiply`](error_utils.cc.md#SafeMultiply), [`SafeAdd`](error_utils.cc.md#SafeAdd), [`MakeZeroSizedTensor`](../ops/op_builder_utils.cc.md#MakeZeroSizedTensor), [`alltoall`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.alltoall), [`operator[]`](../eager/device_buffer.cc.md#DeviceBufferList.Data.operator), [`AtenPreluKernelBackward`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernelBackward), [`ToElementType`](dtype.cc.md#ToElementType), [`AtenMaskedScatter_`](../ops/masked_scatter/masked_scatter_aten_kernels.cc.md#AtenMaskedScatter_), [`AtenPreluKernel`](../ops/prelu/prelu_aten_kernels.cc.md#AtenPreluKernel), [`GetBuffer`](../eager/tensor_to_buffer.cc.md#GetBuffer), [`EncodeParamCacheKey`](cache_key.cc.md#EncodeParamCacheKey), [`CreateViewDeviceBufferRef`](../eager/device_buffer_utils.cc.md#CreateViewDeviceBufferRef), [`AtenWeightNormInterface`](../ops/weight_norm/weight_norm_aten_kernels.cc.md#AtenWeightNormInterface), [`TraverseAndCompile`](../internal/compile/compiled_mode.cc.md#TraverseAndCompile), [`ContiguousToView`](../ops/view_decomposition/contiguous_to_view.cc.md#ContiguousToView), [`AtenChannelShuffle`](../ops/channel_shuffle/channel_shuffle_aten_kernels.cc.md#AtenChannelShuffle), [`SliceModuleCacheKey`](cache_key.cc.md#SliceModuleCacheKey), [`allgather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allgather), [`AtenCtcLossTensor`](../ops/ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`AtenDigammaOut`](../ops/digamma/digamma_aten_kernels.cc.md#AtenDigammaOut), [`_allgather_base`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu._allgather_base), [`AtenBinCount`](../ops/bincount/bincount_aten_kernels.cc.md#AtenBinCount)  (+763 more)

### <a id="StatusBuilder.MessageJoinStyle"></a>`StatusBuilder.MessageJoinStyle`
- def: [`csrc/common/status_builder.h:137`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L137)
- doc: Specifies how to join the error message in the original status and any
- signature: `enum class MessageJoinStyle`
- members:
  - <a id="StatusBuilder.MessageJoinStyle.kAppend"></a>`kAppend` — [`L138`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L138)
  - <a id="StatusBuilder.MessageJoinStyle.kOverride"></a>`kOverride` — [`L140`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L140)
  - <a id="StatusBuilder.MessageJoinStyle.kPrepend"></a>`kPrepend` — [`L139`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L139)
- used by: [`SetPrepend`](status_builder.h.md#StatusBuilder.SetPrepend), [`SetOverride`](status_builder.h.md#StatusBuilder.SetOverride), [`JoinMessageToStatus`](status_builder.cc.md#StatusBuilder.JoinMessageToStatus), [`message_join_style`](status_builder.h.md#StatusBuilder.Rep.message_join_style), [`stream`](status_builder.h.md#StatusBuilder.Rep.stream)

### <a id="StatusBuilder.Rep"></a>`StatusBuilder.Rep`
- def: [`csrc/common/status_builder.h:149`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L149)
- doc: Infrequently set builder options, instantiated lazily. This reduces
- signature: `struct Rep`
- members:
  - <a id="StatusBuilder.Rep.InitRep"></a>`InitRep(absl::Status&& s)` — [`L163`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L163)
  - `InitRep(const absl::Status& s)` — [`L156`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L156)
  - `InitRep(absl::Status&& s)` — [`L163`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L163)
  - `InitRep(const absl::Status& s)` — [`L156`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L156)
  - <a id="StatusBuilder.Rep.message_join_style"></a>`message_join_style` — [`L175`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L175)
  - <a id="StatusBuilder.Rep.status"></a>`status` — [`L171`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L171) — The status that the result will be based on.
  - <a id="StatusBuilder.Rep.stream"></a>`stream` — [`L174`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L174) — Gathers additional messages added with `<<` for use in the final status.
- uses (calls/refs, reference-scoped): [`JoinMessageToStatus`](status_builder.cc.md#StatusBuilder.JoinMessageToStatus), [`CreateStatus`](status_builder.cc.md#StatusBuilder.CreateStatus), [`MessageJoinStyle`](status_builder.h.md#StatusBuilder.MessageJoinStyle), [`Rep`](status_builder.cc.md#StatusBuilder.Rep.Rep), [`Rep`](status_builder.cc.md#StatusBuilder.Rep.Rep), [`Rep`](status_builder.cc.md#StatusBuilder.Rep.Rep), [`InitStream`](status_builder.cc.md#StatusBuilder.Rep.InitStream), [`~Rep`](status_builder.cc.md#StatusBuilder.Rep.-Rep), [`kAppend`](status_builder.h.md#StatusBuilder.MessageJoinStyle.kAppend)
- used by: [`StatusBuilder`](status_builder.cc.md#StatusBuilder.StatusBuilder), [`operator<<`](status_builder.h.md#StatusBuilder.operator), [`SetPrepend`](status_builder.h.md#StatusBuilder.SetPrepend), [`SetOverride`](status_builder.h.md#StatusBuilder.SetOverride), [`CreateStatus`](status_builder.cc.md#StatusBuilder.CreateStatus), [`StatusBuilder`](status_builder.cc.md#StatusBuilder.StatusBuilder), [`Rep`](status_builder.cc.md#StatusBuilder.Rep.Rep), [`operator Status`](status_builder.cc.md#StatusBuilderWithMessage.operator-Status), [`Rep`](status_builder.cc.md#StatusBuilder.Rep.Rep), [`Rep`](status_builder.cc.md#StatusBuilder.Rep.Rep), [`StatusBuilder`](status_builder.h.md#StatusBuilder.StatusBuilder), [`InitStream`](status_builder.cc.md#StatusBuilder.Rep.InitStream), [`ok`](status_builder.h.md#StatusBuilder.ok), [`operator=`](status_builder.h.md#StatusBuilder.operator), [`~Rep`](status_builder.cc.md#StatusBuilder.Rep.-Rep)

### <a id="StatusBuilderWithMessage"></a>`StatusBuilderWithMessage`  ·  implements/extends StatusBuilder
- def: [`csrc/common/status_builder.h:195`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L195) — documented in [error-handling](../../../concepts/error-handling.md)
- doc: A status builder that already contains a message. It can be implicitly
- signature: `class [[nodiscard]] StatusBuilderWithMessage : public StatusBuilder`
- members:
  - <a id="StatusBuilderWithMessage.StatusBuilderWithMessage"></a>`StatusBuilderWithMessage` — [`L197`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L197)
  - `StatusBuilderWithMessage` — [`L197`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L197)
  - `StatusBuilderWithMessage` — [`L197`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L197)
  - `StatusBuilderWithMessage` — [`L197`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L197)
  - <a id="StatusBuilderWithMessage.operator-Status"></a>`operator Status()` — [`L275`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L275) — Implicit conversion to Status.
- uses (calls/refs, reference-scoped): [`StatusBuilder`](status_builder.h.md#StatusBuilder), [`StatusBuilder`](status_builder.cc.md#StatusBuilder.StatusBuilder), [`rep_`](status_builder.h.md#StatusBuilder.rep_), [`CreateStatus`](status_builder.cc.md#StatusBuilder.CreateStatus), [`TorchShowCppStacktraces`](status_builder.cc.md#TorchShowCppStacktraces), [`StatusBuilder`](status_builder.cc.md#StatusBuilder.StatusBuilder), [`operator Status`](status_builder.cc.md#StatusBuilderWithMessage.operator-Status), [`StatusBuilder`](status_builder.h.md#StatusBuilder.StatusBuilder), [`StatusBuilder`](status_builder.h.md#StatusBuilder.StatusBuilder)
- used by: [`StatusBuilder`](status_builder.h.md#StatusBuilder), [`operator<<`](status_builder.h.md#operator), [`operator<<`](status_builder.h.md#operator), [`StatusBuilder`](status_builder.cc.md#StatusBuilder.StatusBuilder), [`Consume`](error_utils.h.md#ReturnIfErrorAdaptor.Consume), [`NumElements`](error_utils.cc.md#NumElements), [`TorchTpuPyBindInitModule_tpu_torch_compile`](../internal/compile/tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`TraverseAndCompile`](../internal/compile/compiled_mode.cc.md#TraverseAndCompile), [`ValidateTensorByteSize`](dtype.cc.md#ValidateTensorByteSize), [`PrepareCompiledModeArgumentsImpl`](../internal/compile/compiled_mode.cc.md#PrepareCompiledModeArgumentsImpl), [`operator<<`](status_builder.h.md#StatusBuilder.operator), [`ExtractMlirFromGraph`](../internal/compile/compiled_mode.cc.md#ExtractMlirFromGraph), [`SerializePortableArtifact`](../ops/op_builder_utils.cc.md#SerializePortableArtifact), [`InitializeInternal`](../pjrt/pjrt_state.cc.md#PjrtBackend.InitializeInternal), [`CopyTpuToTpu`](../ops/copy_from/tpu_to_tpu.cc.md#CopyTpuToTpu), [`PrepareCompiledModeArgumentsImpl`](../internal/compile/compiled_mode.cc.md#PrepareCompiledModeArgumentsImpl), [`PyCallCustomKernel`](../internal/pallas/pallas_py.cc.md#PyCallCustomKernel), [`CopyTpuToCpu`](../ops/copy_from/tpu_to_cpu.cc.md#CopyTpuToCpu), [`ViewSymIntsToDimensions`](../ops/view/view_aten_kernels.cc.md#ViewSymIntsToDimensions), [`ExecuteCompiledModelImpl`](../internal/compile/compiled_mode.cc.md#ExecuteCompiledModelImpl), [`ValidateAddmmInputsAndGetOutputDtype`](../ops/addmm/addmm_aten_kernels.cc.md#ValidateAddmmInputsAndGetOutputDtype), [`BuildPowShlo`](../ops/binary.cc.md#BuildPowShlo), [`PrepareCompiledModeArgumentsNonSequentialFallback`](../internal/compile/compiled_mode.cc.md#PrepareCompiledModeArgumentsNonSequentialFallback), [`CheckMaterialization`](../eager/device_buffer.cc.md#DeviceBufferList.CheckMaterialization), [`BuildPolarShlo`](../ops/binary.cc.md#BuildPolarShlo), [`allocate`](../eager/tensor_to_buffer.cc.md#TpuPinnedAllocator.allocate), [`GetReductionFactor`](../ops/reductions/reduction_utils.cc.md#GetReductionFactor), [`PyGetDynamicPadModule`](../internal/compile/tpu_torch_compile.cc.md#PyGetDynamicPadModule), [`BuildComplexShlo`](../ops/binary.cc.md#BuildComplexShlo), [`CopyCpuToTpu`](../ops/copy_from/cpu_to_tpu.cc.md#CopyCpuToTpu), [`LoadSerializedExecutable`](compilation_cache_utils.cc.md#LoadSerializedExecutable), [`CompileModuleWithCache`](../internal/compile/tpu_torch_compile.cc.md#CompileModuleWithCache), [`PyMakeDynamicPlaceholder`](../internal/compile/tpu_torch_compile.cc.md#PyMakeDynamicPlaceholder), [`GetIndexBroadcastShape`](../ops/index_put/index_put_aten_kernels.cc.md#GetIndexBroadcastShape), [`AtomicWriteToCacheFile`](compilation_cache_utils.cc.md#AtomicWriteToCacheFile), [`PyMakePlaceholderLike`](../internal/compile/tpu_torch_compile.cc.md#PyMakePlaceholderLike), [`BuildArangeOp`](../ops/arange/arange.cc.md#BuildArangeOp), [`TestBody`](error_utils_test.cc.md#AssignOrCrashDeathTest_ErrorExpressionDoesNotHaveToReference__Test.TestBody), [`TestBody`](error_utils_test.cc.md#AssignOrReturn_ErrorExpressionDoesNotHaveToReference__Test.TestBody), [`AssignOrThrowExpressionNo_`](error_utils_test.cc.md#AssignOrThrowExpressionNo_)  (+35 more)

## Functions
- `operator<<(std::ostream& os, const StatusBuilderWithMessage& builder)` — [`L213`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L213) — Implicitly converts `builder` to `Status` and write it to `os`.
- <a id="operator"></a>`operator<<(std::ostream& os, StatusBuilderWithMessage&& builder)` — [`L217`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L217)

## Module values
- <a id="kCppErrorTraceUrl"></a>`kCppErrorTraceUrl` — [`L309`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L309) — Key for the payload in absl::Status that stores the C++ error trace,
- <a id="kRootOpNameUrl"></a>`kRootOpNameUrl` — [`L313`](../../../../../../raw/code/torch_tpu/csrc/common/status_builder.h#L313) — Key for the payload in absl::Status that stores the root op name.

