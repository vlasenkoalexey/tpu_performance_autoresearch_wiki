---
title: 'Module: csrc/pjrt/pjrt_state.h'
type: catalog
provenance: extracted
module: csrc/pjrt/pjrt_state.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  PjrtBackend: PjrtBackend#
  PjrtBackend.operator: PjrtBackend#`operator=`(faa207f40398d3).
  PjrtBackend.mutex_: PjrtBackend#mutex_.
  PjRtDeviceAttributes: PjRtDeviceAttributes#
  PjRtDeviceAttributes.id: PjRtDeviceAttributes#id.
  PjrtBackend.client_: PjrtBackend#client_.
  PjrtBackend.init_status_: PjrtBackend#init_status_.
  PjrtBackend.device_: PjrtBackend#device_.
  PjrtBackend.device_type_: PjrtBackend#device_type_.
  PjrtBackend.-PjrtBackend: PjrtBackend#`~PjrtBackend`(ced63f7c635d850d).
  PjRtDeviceAttributes.coords: PjRtDeviceAttributes#coords.
  PjrtBackend.init_attempted_: PjrtBackend#init_attempted_.
  PjRtDeviceAttributes.slice_index: PjRtDeviceAttributes#slice_index.
  PjRtDeviceAttributes.core_on_chip: PjRtDeviceAttributes#core_on_chip.
  PjRtDeviceAttributes.device_kind: PjRtDeviceAttributes#device_kind.
  PjrtBackend.options_: PjrtBackend#options_.
  PjRtDeviceAttributes.process_index: PjRtDeviceAttributes#process_index.
  PjrtBackend.global_device_id_: PjrtBackend#global_device_id_.
  PjrtBackend.global_device_count_: PjrtBackend#global_device_count_.
  PjrtBackend.bad_fork_checker_: PjrtBackend#bad_fork_checker_.
  PjRtInitializationOptions.device_type: PjRtInitializationOptions#device_type.
  PjRtInitializationOptions.premapped_buffer_size_bytes: PjRtInitializationOptions#premapped_buffer_size_bytes.
  PjRtInitializationOptions.bad_fork_checker: PjRtInitializationOptions#bad_fork_checker.
  PjRtInitializationOptions: PjRtInitializationOptions#
  BadForkChecker: BadForkChecker#
  PjrtBackend.PjrtBackend: PjrtBackend#PjrtBackend(893d4b4011cb2cae).
  PjrtBackend.on_initialized_hook_: PjrtBackend#on_initialized_hook_.
  OnInitializedHook: OnInitializedHook#
  PjRtInitializationOptions.on_initialized_hook: PjRtInitializationOptions#on_initialized_hook.
---
# Module: [`csrc/pjrt/pjrt_state.h`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h)

## Classes
### <a id="BadForkChecker"></a>`BadForkChecker`
- def: [`csrc/pjrt/pjrt_state.h:41`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L41)
- doc: Function pointer hooks for fork detection and runtime initialization.
- signature: `using BadForkChecker = bool (*)()`
- used by: [`IsInBadFork`](pjrt_state.cc.md#PjrtBackend.IsInBadFork), [`init_status_`](pjrt_state.h.md#PjrtBackend.init_status_), [`premapped_buffer_size_bytes`](pjrt_state.h.md#PjRtInitializationOptions.premapped_buffer_size_bytes)

### <a id="OnInitializedHook"></a>`OnInitializedHook`
- def: [`csrc/pjrt/pjrt_state.h:42`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L42)
- signature: `using OnInitializedHook = void (*)()`
- used by: [`bad_fork_checker_`](pjrt_state.h.md#PjrtBackend.bad_fork_checker_), [`bad_fork_checker`](pjrt_state.h.md#PjRtInitializationOptions.bad_fork_checker)

### <a id="PjRtDeviceAttributes"></a>`PjRtDeviceAttributes`
- def: [`csrc/pjrt/pjrt_state.h:53`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L53) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- doc: PJRT device attributes populated from the PJRT runtime.
- signature: `struct PjRtDeviceAttributes`
- members:
  - <a id="PjRtDeviceAttributes.coords"></a>`coords` — [`L57`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L57) — INT_VEC_OK
  - <a id="PjRtDeviceAttributes.core_on_chip"></a>`core_on_chip` — [`L58`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L58)
  - <a id="PjRtDeviceAttributes.device_kind"></a>`device_kind` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L56)
  - <a id="PjRtDeviceAttributes.id"></a>`id` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L54) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
  - <a id="PjRtDeviceAttributes.process_index"></a>`process_index` — [`L55`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L55)
  - <a id="PjRtDeviceAttributes.slice_index"></a>`slice_index` — [`L59`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L59)
- used by: [`InitializeRankToDeviceMappings`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.InitializeRankToDeviceMappings), [`GetDeviceAttributes`](pjrt_state.cc.md#PjrtBackend.GetDeviceAttributes), [`TorchTpuPyBindInitModule_tpu_distributed`](../internal/distributed/tpu_distributed.cc.md#TorchTpuPyBindInitModule_tpu_distributed), [`DeserializeDeviceAttributes`](../distributed/process_group_tpu.cc.md#DeserializeDeviceAttributes), [`operator=`](pjrt_state.h.md#PjrtBackend.operator), [`TestBody`](../distributed/process_group_tpu_test.cc.md#ProcessGroupTpuTest_ComputeRankToTopologyOrderTwoSliceTpu7x_Test.TestBody), [`ComputeRankToTopologyOrder`](../distributed/process_group_tpu.cc.md#ComputeRankToTopologyOrder), [`TopologyKey`](../distributed/process_group_tpu.cc.md#ComputeRankToTopologyOrder.TopologyKey), [`SerializeDeviceAttributes`](../distributed/process_group_tpu.cc.md#SerializeDeviceAttributes), [`TestBody`](../distributed/process_group_tpu_test.cc.md#ProcessGroupTpuTest_ComputeRankToTopologyOrderMissingAttributes_Test.TestBody), [`GetDeviceType`](pjrt_state.cc.md#PjrtBackend.GetDeviceType), [`WorldTopology`](../distributed/process_group_tpu.cc.md#WorldTopology), [`GetDeviceVmemLimitBytes`](../ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc.md#GetDeviceVmemLimitBytes), [`WorldTopologyState`](../distributed/process_group_tpu.cc.md#WorldTopologyState)

### <a id="PjRtInitializationOptions"></a>`PjRtInitializationOptions`
- def: [`csrc/pjrt/pjrt_state.h:45`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L45)
- doc: PjRt initialization options. Defaults to TPU, no pre-mapped buffer.
- signature: `struct PjRtInitializationOptions`
- members:
  - <a id="PjRtInitializationOptions.bad_fork_checker"></a>`bad_fork_checker` — [`L48`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L48)
  - <a id="PjRtInitializationOptions.device_type"></a>`device_type` — [`L46`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L46)
  - <a id="PjRtInitializationOptions.on_initialized_hook"></a>`on_initialized_hook` — [`L49`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L49)
  - <a id="PjRtInitializationOptions.premapped_buffer_size_bytes"></a>`premapped_buffer_size_bytes` — [`L47`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L47)
- uses (calls/refs, reference-scoped): [`BadForkChecker`](pjrt_state.h.md#BadForkChecker), [`OnInitializedHook`](pjrt_state.h.md#OnInitializedHook)
- used by: [`InitializeInternal`](pjrt_state.cc.md#PjrtBackend.InitializeInternal), [`SetPjRtInitializationOptions`](pjrt_state.cc.md#PjrtBackend.SetPjRtInitializationOptions), [`operator=`](pjrt_state.h.md#PjrtBackend.operator), [`global_device_id_`](pjrt_state.h.md#PjrtBackend.global_device_id_)

### <a id="PjrtBackend"></a>`PjrtBackend`
- def: [`csrc/pjrt/pjrt_state.h:66`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L66) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
- doc: PjrtBackend manages the lifecycle and state of the PjRt runtime.
- signature: `class PjrtBackend`
- members:
  - <a id="PjrtBackend.PjrtBackend"></a>`PjrtBackend(const PjrtBackend&)` — [`L69`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L69) — PjrtBackend is neither copyable nor movable.
  - `PjrtBackend(PjrtBackend&&)` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L71)
  - `PjrtBackend()` — [`L141`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L141)
  - <a id="PjrtBackend.operator"></a>`operator=(PjrtBackend&&)` — [`L72`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L72) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
  - `operator=(const PjrtBackend&)` — [`L70`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L70)
  - <a id="PjrtBackend.-PjrtBackend"></a>`~PjrtBackend()` — [`L142`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L142) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
  - `~PjrtBackend()` — [`L142`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L142)
  - <a id="PjrtBackend.bad_fork_checker_"></a>`bad_fork_checker_` — [`L160`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L160)
  - <a id="PjrtBackend.client_"></a>`client_` — [`L150`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L150) — The PjRtClient singleton. Nullable because it is lazily initialized on the — documented in [pjrt-client](../../../concepts/pjrt-client.md)
  - <a id="PjrtBackend.device_"></a>`device_` — [`L152`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L152) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
  - <a id="PjrtBackend.device_type_"></a>`device_type_` — [`L153`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L153)
  - <a id="PjrtBackend.global_device_count_"></a>`global_device_count_` — [`L155`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L155)
  - <a id="PjrtBackend.global_device_id_"></a>`global_device_id_` — [`L156`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L156)
  - <a id="PjrtBackend.init_attempted_"></a>`init_attempted_` — [`L158`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L158)
  - <a id="PjrtBackend.init_status_"></a>`init_status_` — [`L159`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L159)
  - <a id="PjrtBackend.mutex_"></a>`mutex_` — [`L147`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L147) — documented in [pjrt-client](../../../concepts/pjrt-client.md)
  - <a id="PjrtBackend.on_initialized_hook_"></a>`on_initialized_hook_` — [`L161`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L161)
  - <a id="PjrtBackend.options_"></a>`options_` — [`L157`](../../../../../../raw/code/torch_tpu/csrc/pjrt/pjrt_state.h#L157)
- uses (calls/refs, reference-scoped): [`GetInstance`](pjrt_state.cc.md#PjrtBackend.GetInstance), [`GetClient`](pjrt_state.cc.md#PjrtBackend.GetClient), [`EnsureInitialized`](pjrt_state.cc.md#PjrtBackend.EnsureInitialized), [`InitializeInternal`](pjrt_state.cc.md#PjrtBackend.InitializeInternal), [`SetPjRtInitializationOptions`](pjrt_state.cc.md#PjrtBackend.SetPjRtInitializationOptions), [`GetDevice`](pjrt_state.cc.md#PjrtBackend.GetDevice), [`GetDeviceAttributes`](pjrt_state.cc.md#PjrtBackend.GetDeviceAttributes), [`GetGlobalDeviceCount`](pjrt_state.cc.md#PjrtBackend.GetGlobalDeviceCount), [`GetGlobalDeviceId`](pjrt_state.cc.md#PjrtBackend.GetGlobalDeviceId), [`IsInitialized`](pjrt_state.cc.md#PjrtBackend.IsInitialized), [`Shutdown`](pjrt_state.cc.md#PjrtBackend.Shutdown), [`GetHostAllocator`](pjrt_state.cc.md#PjrtBackend.GetHostAllocator), [`GetSharedClient`](pjrt_state.cc.md#PjrtBackend.GetSharedClient), [`GetAllocatorStats`](pjrt_state.cc.md#PjrtBackend.GetAllocatorStats), [`PjRtDeviceAttributes`](pjrt_state.h.md#PjRtDeviceAttributes), [`ClearAllocatorStats`](pjrt_state.cc.md#PjrtBackend.ClearAllocatorStats), [`IsInBadFork`](pjrt_state.cc.md#PjrtBackend.IsInBadFork), [`GetDeviceType`](pjrt_state.cc.md#PjrtBackend.GetDeviceType), [`PjRtDeviceType`](../common/device_type.h.md#PjRtDeviceType), [`BadForkChecker`](pjrt_state.h.md#BadForkChecker), [`PjRtInitializationOptions`](pjrt_state.h.md#PjRtInitializationOptions), [`kUnknown`](../common/device_type.h.md#PjRtDeviceType.kUnknown), [`OnInitializedHook`](pjrt_state.h.md#OnInitializedHook)
- used by: [`GetInstance`](pjrt_state.cc.md#PjrtBackend.GetInstance), [`GetClient`](pjrt_state.cc.md#PjrtBackend.GetClient), [`ProcessGroupTpu`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.ProcessGroupTpu), [`EnsureInitialized`](pjrt_state.cc.md#PjrtBackend.EnsureInitialized), [`InitializeInternal`](pjrt_state.cc.md#PjrtBackend.InitializeInternal), [`SetPjRtInitializationOptions`](pjrt_state.cc.md#PjrtBackend.SetPjRtInitializationOptions), [`SetMaterializationStarted`](../eager/device_buffer.cc.md#DeviceBufferList.Data.SetMaterializationStarted), [`ExtractArgumentLayoutsIfDifferentFromDefault`](../eager/execution_task.cc.md#ExtractArgumentLayoutsIfDifferentFromDefault), [`PyCompileMlir`](../internal/compile/tpu_torch_compile.cc.md#PyCompileMlir), [`GetDevice`](pjrt_state.cc.md#PjrtBackend.GetDevice), [`InitializeRankToDeviceMappings`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.InitializeRankToDeviceMappings), [`Data`](../eager/device_buffer.cc.md#DeviceBufferList.Data.Data), [`GetDeviceAttributes`](pjrt_state.cc.md#PjrtBackend.GetDeviceAttributes), [`TestBody`](../eager/shutdown_test.cc.md#ShutdownTest_E2EShutdownCompletes_Test.TestBody), [`allocate`](../eager/tensor_to_buffer.cc.md#TpuAllocator.allocate), [`CrossHostReceiveBuffers`](../distributed/process_group_tpu.cc.md#ProcessGroupTpu.CrossHostReceiveBuffers), [`allocate`](../eager/tensor_to_buffer.cc.md#TpuPinnedAllocator.allocate), [`GetGlobalDeviceCount`](pjrt_state.cc.md#PjrtBackend.GetGlobalDeviceCount), [`MakeTensorBuffer`](../api/tensor_buffer.cc.md#MakeTensorBuffer), [`GetDefaultInstance`](../eager/device_gen_impl.cc.md#DeviceGenerators.GetDefaultInstance), [`GetGlobalDeviceId`](pjrt_state.cc.md#PjrtBackend.GetGlobalDeviceId), [`ValidateDeviceIndex`](../eager/tpu_hooks.cc.md#ValidateDeviceIndex), [`LoadSerializedExecutable`](../common/compilation_cache_utils.cc.md#LoadSerializedExecutable), [`IsInitialized`](pjrt_state.cc.md#PjrtBackend.IsInitialized), [`TestBody`](../common/compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCacheBackendNotInitialized_Test.TestBody), [`Compile`](../common/compilation_cache.cc.md#CompilationCache.Compile), [`CreateDynamicKernelAdapter`](../common/compilation_cache.cc.md#CompilationCache.CreateDynamicKernelAdapter), [`Shutdown`](pjrt_state.cc.md#PjrtBackend.Shutdown), [`TestBody`](../api/tensor_buffer_test.cc.md#TensorBufferTest_CreateTensorBufferFromPjRtBufferAndToTensor_Test.TestBody), [`InjectCustomKernel`](../ops/custom_kernels.cc.md#InjectCustomKernel), [`GetHostAllocator`](pjrt_state.cc.md#PjrtBackend.GetHostAllocator), [`CompileMlirExecutable`](../internal/compile/compiled_mode.cc.md#CompileMlirExecutable), [`IsDefaultDeviceLayout`](../eager/traversal.cc.md#IsDefaultDeviceLayout), [`GetSharedClient`](pjrt_state.cc.md#PjrtBackend.GetSharedClient), [`TestBody`](pjrt_init_test.cc.md#PjRtInitTest_BadForkCheckerPreventsAccessAfterInit_Test.TestBody), [`MaybeUpdateSpecWithLayout`](../eager/traversal.cc.md#Traversal.MaybeUpdateSpecWithLayout), [`PyGetDefaultLayout`](../internal/compile/tpu_torch_compile.cc.md#PyGetDefaultLayout), [`ApplyDeviceAssignmentToCompileSpec`](../eager/traversal.cc.md#Traversal.ApplyDeviceAssignmentToCompileSpec), [`GetAllocatorStats`](pjrt_state.cc.md#PjrtBackend.GetAllocatorStats), [`TestBody`](pjrt_init_test.cc.md#PjRtInitTest_InitializeExpandsRankInEnvVars_Test.TestBody)  (+47 more)

