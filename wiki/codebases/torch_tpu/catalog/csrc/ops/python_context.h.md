---
title: 'Module: csrc/ops/python_context.h'
type: catalog
provenance: extracted
module: csrc/ops/python_context.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ScopedPythonContextCapturer: ScopedPythonContextCapturer#
  ScopedPythonContextProvider: ScopedPythonContextProvider#
  PythonContext: PythonContext#
  PythonContext.op_call_chain: PythonContext#op_call_chain(f5f2959be38ccc08).
  ScopedPythonContextProvider.MaybeGetContext: ScopedPythonContextProvider#MaybeGetContext(7316ac81068d767e).
  MaybeSharedTraceback: MaybeSharedTraceback#
  ScopedPythonContextProvider.scoped_builder_loc_: ScopedPythonContextProvider#scoped_builder_loc_.
  PythonStackLocationOptions.kPythonAndCpp: PythonStackLocationOptions#kPythonAndCpp.
  ScopedPythonContextCapturer.operator: ScopedPythonContextCapturer#`operator=`(dad61bd9be248d68).
  PythonContext.Copy: PythonContext#Copy(67312eb118199013).
  ScopedPythonContextCapturer.SetTracebackForTesting: ScopedPythonContextCapturer#SetTracebackForTesting(f5dc857a438281ac).
  PythonTraceback: PythonTraceback#
  PythonContext.traceback: PythonContext#traceback(43ee0e7f0dbbca90).
  PythonStackLocationOptions: PythonStackLocationOptions#
  PythonTraceback.frames: PythonTraceback#frames.
  PythonContext.PythonContext: PythonContext#PythonContext(ced63f7c635d850d).
  ScopedPythonContextProvider.operator: ScopedPythonContextProvider#`operator=`(90c0ed1fc3328f15).
  PythonStackFrame: PythonStackFrame#
  PythonContext.op_call_chain_: PythonContext#op_call_chain_.
  PythonStackFrame.file_name: PythonStackFrame#file_name.
  ScopedPythonContextProvider.previous_context_: ScopedPythonContextProvider#previous_context_.
  SharedTraceback: SharedTraceback#
  PythonStackFrame.func_name: PythonStackFrame#func_name.
  PythonApiName.PythonApiName: PythonApiName#PythonApiName(c8024318075daf50).
  ScopedPythonContextCapturer.GetNumAliveForThread: ScopedPythonContextCapturer#GetNumAliveForThread(da6335ded91d79c2).
  PythonApiName: PythonApiName#
  PythonStackLocationOptions.kPythonOnly: PythonStackLocationOptions#kPythonOnly.
  PythonContext.traceback_: PythonContext#traceback_.
  ScopedPythonContextCapturer.ScopedPythonContextCapturer: ScopedPythonContextCapturer#ScopedPythonContextCapturer(489454b73d545eac).
  PythonContext.operator: PythonContext#`operator=`(baafb06a6ead5bbb).
  ScopedPythonContextProvider.ScopedPythonContextProvider: ScopedPythonContextProvider#ScopedPythonContextProvider(d36f16c68802d956).
  PythonStackFrame.line_number: PythonStackFrame#line_number.
  PythonApiName.name: PythonApiName#name.
---
# Module: [`csrc/ops/python_context.h`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h)

## Classes
### <a id="MaybeSharedTraceback"></a>`MaybeSharedTraceback`
- def: [`csrc/ops/python_context.h:71`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L71)
- signature: `using MaybeSharedTraceback = absl_nullable std::shared_ptr<const PythonTraceback>`
- uses (calls/refs, reference-scoped): [`GetTracebackMode`](python_context.cc.md#GetTracebackMode), [`TracebackMode`](../common/context_states.h.md#TracebackMode), [`PythonTraceback`](python_context.h.md#PythonTraceback)
- used by: [`PythonContext`](python_context.cc.md#PythonContext.PythonContext), [`op_names_`](python_context.cc.md#ScopedPythonContextCapturer.op_names_), [`op_call_chain`](python_context.h.md#PythonContext.op_call_chain), [`MakeLocFromPythonTraceback`](python_context.cc.md#MakeLocFromPythonTraceback), [`SetTracebackForTesting`](python_context.h.md#ScopedPythonContextCapturer.SetTracebackForTesting), [`PythonContext`](python_context.h.md#PythonContext.PythonContext), [`op_call_chain_`](python_context.h.md#PythonContext.op_call_chain_)

### <a id="PythonApiName"></a>`PythonApiName`
- def: [`csrc/ops/python_context.h:139`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L139) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
- doc: Encapsulates the name of the Python API boundary call.
- signature: `struct PythonApiName`
- members:
  - <a id="PythonApiName.PythonApiName"></a>`PythonApiName(const std::string_view name)` — [`L140`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L140) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
  - <a id="PythonApiName.name"></a>`name` — [`L143`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L143) — The string representation of the Python API name.
- used by: [`ScopedPythonContextCapturer`](python_context.h.md#ScopedPythonContextCapturer), [`ScopedPythonContextCapturer`](python_context.cc.md#ScopedPythonContextCapturer.ScopedPythonContextCapturer), [`impl`](../common/pybind_error_utils.h.md#ErrorHandlingHelper.impl)

### <a id="PythonContext"></a>`PythonContext`
- def: [`csrc/ops/python_context.h:97`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L97) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
- doc: The python context of an op.
- signature: `class PythonContext`
- members:
  - <a id="PythonContext.Copy"></a>`Copy()` — [`L109`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L109) — Returns a copy of this PythonContext.
  - `PythonContext()` — [`L99`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L99)
  - <a id="PythonContext.PythonContext"></a>`PythonContext()` — [`L99`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L99) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
  - `PythonContext(PythonContext&& other)` — [`L103`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L103) — This type is move-only.
  - `PythonContext(const PythonContext&)` — [`L105`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L105)
  - `PythonContext(PythonContext&& other)` — [`L103`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L103) — This type is move-only.
  - `op_call_chain()` — [`L115`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L115) — Returns the names of the ops in the op call chain leading to the current
  - <a id="PythonContext.op_call_chain"></a>`op_call_chain()` — [`L115`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L115) — Returns the names of the ops in the op call chain leading to the current
  - `operator=(PythonContext&& other)` — [`L104`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L104)
  - <a id="PythonContext.operator"></a>`operator=(const PythonContext&)` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L106)
  - `operator=(PythonContext&& other)` — [`L104`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L104)
  - <a id="PythonContext.traceback"></a>`traceback()` — [`L120`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L120) — Returns the python traceback of the op, if one has been captured.
  - <a id="PythonContext.op_call_chain_"></a>`op_call_chain_` — [`L130`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L130) — Names of the ops in the op call chain leading to the current op (for
  - <a id="PythonContext.traceback_"></a>`traceback_` — [`L132`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L132) — The python traceback of the op, if one has been captured.
- uses (calls/refs, reference-scoped): [`PythonContext`](python_context.cc.md#PythonContext.PythonContext), [`PythonContext`](python_context.cc.md#PythonContext.PythonContext), [`MaybeSharedTraceback`](python_context.h.md#MaybeSharedTraceback)
- used by: [`GetRootOpName`](python_context.cc.md#GetRootOpName), [`BuildMlirModule`](../eager/traversal.cc.md#Traversal.BuildMlirModule), [`GetContext`](python_context.cc.md#ScopedPythonContextCapturer.GetContext), [`BuildModuleNameFromPyContext`](op_builder_utils.cc.md#BuildModuleNameFromPyContext), [`MaybeGetContext`](python_context.cc.md#ScopedPythonContextCapturer.MaybeGetContext), [`ScopedPythonContextProvider`](python_context.cc.md#ScopedPythonContextProvider.ScopedPythonContextProvider), [`MakeMlirLocation`](python_context.cc.md#MakeMlirLocation), [`top_context_`](python_context.cc.md#ScopedPythonContextProvider.top_context_), [`ScopedPythonContextProvider`](python_context.h.md#ScopedPythonContextProvider), [`PythonContext`](python_context.cc.md#PythonContext.PythonContext), [`AppendFxOpRow`](../eager/traversal.cc.md#AppendFxOpRow), [`TestBody`](python_context_test.cc.md#ScopedPythonContextCapturerTrackebackTest_CapturesTracebackWhenEnabled_Test.TestBody), [`TestBody`](python_context_test.cc.md#ScopedPythonContextCapturerTrackebackTest_DoesNotCaptureTracebackWhenDisabled_Test.TestBody), [`TestBody`](python_context_test.cc.md#CaptureCurrentPythonTrackback_CapturesPythonStack_Test.TestBody), [`TestBody`](python_context_test.cc.md#GetOriginalOpName_ReturnsFirstOpNameWhenProviderIsAlive_Test.TestBody), [`TestBody`](python_context_test.cc.md#ScopedPythonContextCapturer_TwoObjectsAreAlive_Test.TestBody), [`TestBody`](python_context_test.cc.md#ScopedPythonContextProvider_OneObjectIsAlive_Test.TestBody), [`TestBody`](python_context_test.cc.md#ScopedPythonContextProvider_TwoObjectsAreAlive_Test.TestBody), [`TestBody`](python_context_test.cc.md#CaptureCurrentPythonTrackback_CapturesCppStackWhenRequested_Test.TestBody), [`TestBody`](python_context_test.cc.md#ScopedPythonContextCapturer_OneObjectIsAlive_Test.TestBody), [`inputs`](../eager/device_buffer.h.md#DeferredOp.inputs), [`~ScopedPythonContextCapturer`](python_context.cc.md#ScopedPythonContextCapturer.-ScopedPythonContextCapturer), [`MaybeGetContext`](python_context.h.md#ScopedPythonContextProvider.MaybeGetContext), [`ToResultVector`](op_builder_utils.h.md#ToResultVector), [`AnnotateMlirPlacements`](../eager/traversal.cc.md#AnnotateMlirPlacements), [`IntoParts`](../eager/traversal.h.md#Traversal.IntoParts), [`scoped_builder_loc_`](python_context.h.md#ScopedPythonContextProvider.scoped_builder_loc_), [`~ScopedPythonContextProvider`](python_context.cc.md#ScopedPythonContextProvider.-ScopedPythonContextProvider), [`operator=`](python_context.h.md#ScopedPythonContextCapturer.operator), [`MakeNameScopeOpStringFromCallChain`](python_context.cc.md#MakeNameScopeOpStringFromCallChain), [`operator=`](python_context.h.md#ScopedPythonContextProvider.operator), [`op_param_cache_keys_`](../eager/device_buffer.h.md#DeferredOp.op_param_cache_keys_)

### <a id="PythonStackFrame"></a>`PythonStackFrame`
- def: [`csrc/ops/python_context.h:59`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L59) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
- doc: We define our own traceback format here instead of using
- signature: `struct PythonStackFrame`
- members:
  - <a id="PythonStackFrame.file_name"></a>`file_name` — [`L60`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L60)
  - <a id="PythonStackFrame.func_name"></a>`func_name` — [`L61`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L61)
  - <a id="PythonStackFrame.line_number"></a>`line_number` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L63) — 1-based line number.
- used by: [`AppendFxOpRow`](../eager/traversal.cc.md#AppendFxOpRow), [`MakeFuncFileLineColLoc`](python_context.cc.md#MakeFuncFileLineColLoc), [`BuildBufferIndexMap`](../eager/traversal.cc.md#BuildBufferIndexMap), [`IsUserFrame`](python_context.cc.md#IsUserFrame), [`PickUserFrame`](../eager/traversal.cc.md#PickUserFrame), [`PythonTraceback`](python_context.h.md#PythonTraceback)

### <a id="PythonStackLocationOptions"></a>`PythonStackLocationOptions`
- def: [`csrc/ops/python_context.h:82`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L82)
- doc: Options for specifying what stack traces to include in the MLIR Location.
- signature: `enum class PythonStackLocationOptions`
- members:
  - <a id="PythonStackLocationOptions.kPythonAndCpp"></a>`kPythonAndCpp` — [`L84`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L84)
  - <a id="PythonStackLocationOptions.kPythonOnly"></a>`kPythonOnly` — [`L83`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L83)
- uses (calls/refs, reference-scoped): [`CaptureCurrentPythonTrackback`](python_context.cc.md#CaptureCurrentPythonTrackback), [`SharedTraceback`](python_context.h.md#SharedTraceback)
- used by: [`CaptureCurrentPythonTrackback`](python_context.cc.md#CaptureCurrentPythonTrackback), [`TestBody`](python_context_test.cc.md#CaptureCurrentPythonTrackback_CapturesPythonStack_Test.TestBody), [`TestBody`](python_context_test.cc.md#CaptureCurrentPythonTrackback_CapturesCppStackWhenRequested_Test.TestBody)

### <a id="PythonTraceback"></a>`PythonTraceback`
- def: [`csrc/ops/python_context.h:66`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L66) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
- signature: `struct PythonTraceback`
- members:
  - <a id="PythonTraceback.frames"></a>`frames` — [`L67`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L67)
- uses (calls/refs, reference-scoped): [`PythonStackFrame`](python_context.h.md#PythonStackFrame)
- used by: [`CaptureCurrentPythonTrackback`](python_context.cc.md#CaptureCurrentPythonTrackback), [`TestBody`](../eager/traversal_test.cc.md#TraversalTest_ReadableStringWithTraceback_Test.TestBody), [`MakeLocFromPythonTraceback`](python_context.cc.md#MakeLocFromPythonTraceback), [`MaybeSharedTraceback`](python_context.h.md#MaybeSharedTraceback), [`PickUserFrame`](../eager/traversal.cc.md#PickUserFrame), [`SharedTraceback`](python_context.h.md#SharedTraceback)

### <a id="ScopedPythonContextCapturer"></a>`ScopedPythonContextCapturer`
- def: [`csrc/ops/python_context.h:165`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L165) — documented in [dynamic-shape-ops](../../../concepts/dynamic-shape-ops.md)
- doc: RAII class to capture the python context for an op. Conceptually, it
- signature: `class ScopedPythonContextCapturer`
- members:
  - <a id="ScopedPythonContextCapturer.GetNumAliveForThread"></a>`GetNumAliveForThread()` — [`L216`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L216) — Returns the number of alive ScopedPythonContextCapturer instances for the
  - <a id="ScopedPythonContextCapturer.ScopedPythonContextCapturer"></a>`ScopedPythonContextCapturer(ScopedPythonContextCapturer&&)` — [`L186`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L186)
  - `ScopedPythonContextCapturer(const ScopedPythonContextCapturer&)` — [`L183`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L183) — This class is neither copyable nor movable. — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
  - <a id="ScopedPythonContextCapturer.SetTracebackForTesting"></a>`SetTracebackForTesting(MaybeSharedTraceback traceback)` — [`L205`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L205) — For testing only: override the traceback of all currently alive contexts.
  - `operator=(const ScopedPythonContextCapturer&)` — [`L184`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L184)
  - <a id="ScopedPythonContextCapturer.operator"></a>`operator=(ScopedPythonContextCapturer&&)` — [`L187`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L187)
- uses (calls/refs, reference-scoped): [`OpName`](op_names.h.md#OpName), [`ScopedPythonContextCapturer`](python_context.cc.md#ScopedPythonContextCapturer.ScopedPythonContextCapturer), [`GetContext`](python_context.cc.md#ScopedPythonContextCapturer.GetContext), [`MaybeGetContext`](python_context.cc.md#ScopedPythonContextCapturer.MaybeGetContext), [`ScopedPythonContextCapturer`](python_context.cc.md#ScopedPythonContextCapturer.ScopedPythonContextCapturer), [`traceback_`](python_context.cc.md#ScopedPythonContextCapturer.traceback_), [`ScopedPythonContextCapturer`](python_context.cc.md#ScopedPythonContextCapturer.ScopedPythonContextCapturer), [`op_names_`](python_context.cc.md#ScopedPythonContextCapturer.op_names_), [`PythonContext`](python_context.h.md#PythonContext), [`~ScopedPythonContextCapturer`](python_context.cc.md#ScopedPythonContextCapturer.-ScopedPythonContextCapturer), [`MaybeSharedTraceback`](python_context.h.md#MaybeSharedTraceback), [`PythonApiName`](python_context.h.md#PythonApiName)
- used by: [`GetRootOpName`](python_context.cc.md#GetRootOpName), [`ScopedPythonContextCapturer`](python_context.cc.md#ScopedPythonContextCapturer.ScopedPythonContextCapturer), [`alltoall`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.alltoall), [`AtenPreluKernelBackward`](prelu/prelu_aten_kernels.cc.md#AtenPreluKernelBackward), [`AtenMaskedScatter_`](masked_scatter/masked_scatter_aten_kernels.cc.md#AtenMaskedScatter_), [`AtenPreluKernel`](prelu/prelu_aten_kernels.cc.md#AtenPreluKernel), [`CreateViewDeviceBufferRef`](../eager/device_buffer_utils.cc.md#CreateViewDeviceBufferRef), [`AtenWeightNormInterface`](weight_norm/weight_norm_aten_kernels.cc.md#AtenWeightNormInterface), [`AtenChannelShuffle`](channel_shuffle/channel_shuffle_aten_kernels.cc.md#AtenChannelShuffle), [`AtenIndexTensorOut`](index/index_aten_kernels.cc.md#AtenIndexTensorOut), [`allgather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allgather), [`AtenCtcLossTensor`](ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`AtenVarMeanCorrection`](reductions/var_aten_kernels.cc.md#AtenVarMeanCorrection), [`AtenDigammaOut`](digamma/digamma_aten_kernels.cc.md#AtenDigammaOut), [`_allgather_base`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu._allgather_base), [`AtenBinCount`](bincount/bincount_aten_kernels.cc.md#AtenBinCount), [`AtenCtcLossBackwardTensor`](ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossBackwardTensor), [`AtenRmsNorm`](rms_norm/rms_norm_aten_kernels.cc.md#AtenRmsNorm), [`allreduce`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allreduce), [`AtenLinalgLuSolveOut`](linalg/lu/linalg_lu_kernels.cc.md#AtenLinalgLuSolveOut), [`PyCreateAssociativeScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateAssociativeScanOp), [`AtenFusedRmsNorm`](rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNorm), [`AtenArangeStartOut`](arange/arange_aten_kernels.cc.md#AtenArangeStartOut), [`AtenFusedRmsNormBackward`](rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNormBackward), [`AtenLinalgSolveExOut`](linalg/linalg_kernels.cc.md#AtenLinalgSolveExOut), [`AtenReplicationPad3dBackward`](replication_pad/replication_pad_aten_kernels.cc.md#AtenReplicationPad3dBackward), [`gather`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.gather), [`AtenLinalgSvdU`](linalg/linalg_svd_kernels.cc.md#AtenLinalgSvdU), [`AtenSegmentReduce`](segment_reduce/segment_reduce_aten_kernels.cc.md#AtenSegmentReduce), [`_reduce_scatter_base`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu._reduce_scatter_base), [`AtenLinalgInvExInverse`](linalg/linalg_kernels.cc.md#AtenLinalgInvExInverse), [`AtenAdaptiveAvgPool3dOut`](pooling/adaptive_avg_pool_aten_kernels.cc.md#AtenAdaptiveAvgPool3dOut), [`AtenGridSampler3dBackward`](grid_sampler/grid_sampler_aten_kernels.cc.md#AtenGridSampler3dBackward), [`AtenNativeGroupNormBackward`](group_norm/group_norm_aten_kernels.cc.md#AtenNativeGroupNormBackward), [`AtenViewAsComplex`](view/view_aten_kernels.cc.md#AtenViewAsComplex), [`AtenCdistBackward`](distance/dist_aten_kernels.cc.md#AtenCdistBackward), [`AtenCdistForward`](distance/dist_aten_kernels.cc.md#AtenCdistForward), [`AtenExponential_`](exponential/exponential_aten_kernels.cc.md#AtenExponential_), [`AtenLinalgLuFactorExOut`](linalg/lu/linalg_lu_kernels.cc.md#AtenLinalgLuFactorExOut), [`AtenLinspaceOut`](linspace/linspace_aten_kernels.cc.md#AtenLinspaceOut)  (+792 more)

### <a id="ScopedPythonContextProvider"></a>`ScopedPythonContextProvider`
- def: [`csrc/ops/python_context.h:248`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L248) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
- doc: RAII class to provide a PythonContext captured earlier to an MlirOp build
- signature: `class ScopedPythonContextProvider`
- members:
  - <a id="ScopedPythonContextProvider.MaybeGetContext"></a>`MaybeGetContext()` — [`L273`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L273) — Returns the top python context on the singleton context provider stack for
  - <a id="ScopedPythonContextProvider.ScopedPythonContextProvider"></a>`ScopedPythonContextProvider(const ScopedPythonContextProvider&)` — [`L259`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L259) — This class is neither copyable nor movable.
  - `ScopedPythonContextProvider(ScopedPythonContextProvider&&)` — [`L262`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L262) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
  - `operator=(const ScopedPythonContextProvider&)` — [`L260`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L260)
  - <a id="ScopedPythonContextProvider.operator"></a>`operator=(ScopedPythonContextProvider&&)` — [`L263`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L263)
  - <a id="ScopedPythonContextProvider.previous_context_"></a>`previous_context_` — [`L288`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L288) — Each alive ScopedPythonContextProvider instance corresponds to an element
  - <a id="ScopedPythonContextProvider.scoped_builder_loc_"></a>`scoped_builder_loc_` — [`L292`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L292) — The RAII object that sets the location attribute of `builder` in its
- uses (calls/refs, reference-scoped): [`GetRootOpName`](python_context.cc.md#GetRootOpName), [`OpName`](op_names.h.md#OpName), [`ScopedPythonContextProvider`](python_context.cc.md#ScopedPythonContextProvider.ScopedPythonContextProvider), [`MakeMlirLocation`](python_context.cc.md#MakeMlirLocation), [`top_context_`](python_context.cc.md#ScopedPythonContextProvider.top_context_), [`PythonContext`](python_context.h.md#PythonContext), [`~ScopedPythonContextProvider`](python_context.cc.md#ScopedPythonContextProvider.-ScopedPythonContextProvider)
- used by: [`GetRootOpName`](python_context.cc.md#GetRootOpName), [`BuildMlirModule`](../eager/traversal.cc.md#Traversal.BuildMlirModule), [`ExtractMlirFromGraph`](../internal/compile/compiled_mode.cc.md#ExtractMlirFromGraph), [`PyCompileMlir`](../internal/compile/tpu_torch_compile.cc.md#PyCompileMlir), [`ScopedPythonContextProvider`](python_context.cc.md#ScopedPythonContextProvider.ScopedPythonContextProvider), [`traceback_`](python_context.cc.md#ScopedPythonContextCapturer.traceback_), [`PyAsyncTraverseAndCompile`](../internal/compile/tpu_torch_compile.cc.md#PyAsyncTraverseAndCompile), [`PyGetComputationGraphviz`](../internal/sync/sync_py.cc.md#PyGetComputationGraphviz), [`PyGetComputationMlir`](../internal/sync/sync_py.cc.md#PyGetComputationMlir), [`TestBody`](python_context_test.cc.md#GetOriginalOpName_ReturnsFirstOpNameWhenProviderIsAlive_Test.TestBody), [`TestBody`](python_context_test.cc.md#ScopedPythonContextProvider_OneObjectIsAlive_Test.TestBody), [`TestBody`](python_context_test.cc.md#ScopedPythonContextProvider_TwoObjectsAreAlive_Test.TestBody), [`TestBody`](python_context_test.cc.md#ScopedPythonContextProvider_NoObjectIsAlive_Test.TestBody), [`~ScopedPythonContextProvider`](python_context.cc.md#ScopedPythonContextProvider.-ScopedPythonContextProvider)

### <a id="SharedTraceback"></a>`SharedTraceback`
- def: [`csrc/ops/python_context.h:70`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.h#L70)
- signature: `using SharedTraceback = absl_nonnull std::shared_ptr<const PythonTraceback>`
- uses (calls/refs, reference-scoped): [`PythonTraceback`](python_context.h.md#PythonTraceback)
- used by: [`PythonContext`](python_context.cc.md#PythonContext.PythonContext), [`kPythonAndCpp`](python_context.h.md#PythonStackLocationOptions.kPythonAndCpp)

