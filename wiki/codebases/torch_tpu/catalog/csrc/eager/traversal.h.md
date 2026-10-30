---
title: 'Module: csrc/eager/traversal.h'
type: catalog
provenance: extracted
module: csrc/eager/traversal.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  Traversal: Traversal#
  Traversal.outputs: Traversal#outputs(cdca2a773587f60d).
  Traversal.execution_order: Traversal#execution_order(6391e595ccdb3f89).
  Traversal.operator: Traversal#`operator=`(a41e538acd9735cf).
  Traversal.Traversal: Traversal#Traversal(184626d03e650198).
  Traversal.arguments: Traversal#arguments(cdca2a773587f60d).
  Traversal.core_pinning_mode_: Traversal#core_pinning_mode_.
  Traversal.arguments_: Traversal#arguments_.
  RefToOpMap: RefToOpMap#
  Traversal.SortByCreationOrder: Traversal#SortByCreationOrder(49f6e7a06ebc5aa8).
  Traversal.outputs_: Traversal#outputs_.
  Traversal.IntoParts: Traversal#IntoParts(1a12cd578f5911f9).
  Traversal.execution_order_: Traversal#execution_order_.
  Traversal.SetCorePinningMode: Traversal#SetCorePinningMode(3895345c27d01d54).
  Traversal.resolved_da_: Traversal#resolved_da_.
  Traversal.core_pinning_mode: Traversal#core_pinning_mode(288fbb0adaf44ad9).
  Traversal.Parts: Traversal#Parts#
  Traversal.graph_key_: Traversal#graph_key_.
  Traversal.Parts.execution_order: Traversal#Parts#execution_order.
  Traversal.Parts.arguments: Traversal#Parts#arguments.
  Traversal.Parts.outputs: Traversal#Parts#outputs.
  Traversal.shape_dynamism_metadata_: Traversal#shape_dynamism_metadata_.
---
# Module: [`csrc/eager/traversal.h`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h)

## Classes
### <a id="RefToOpMap"></a>`RefToOpMap`
- def: [`csrc/eager/traversal.h:90`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L90)
- signature: `using RefToOpMap = absl::flat_hash_map<DeviceBufferRef, mlir::MlirOp>`
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](device_buffer.h.md#DeviceBufferRef), [`GraphKey`](../common/cache_key.h.md#GraphKey), [`CustomLayout`](../common/dimension_types.h.md#CustomLayout), [`AnnotateGraphKeyWithArgumentLayouts`](traversal.cc.md#AnnotateGraphKeyWithArgumentLayouts), [`AnnotateGraphKeyWithDonatedInputs`](traversal.cc.md#AnnotateGraphKeyWithDonatedInputs)
- used by: [`BuildMlirModule`](traversal.cc.md#Traversal.BuildMlirModule)

### <a id="Traversal"></a>`Traversal`
- def: [`csrc/eager/traversal.h:108`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L108)
- doc: A traversed graph of deferred ops, ready to be compiled and (optionally)
- signature: `class Traversal`
- members:
  - <a id="Traversal.IntoParts"></a>`IntoParts()` — [`L248`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L248) — Breaks the Traversal into its core components, leaving an empty (and
  - <a id="Traversal.SetCorePinningMode"></a>`SetCorePinningMode(CorePinningMode core_pinning_mode)` — [`L270`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L270) — Sets the core pinning mode for the Traversal.
  - <a id="Traversal.SortByCreationOrder"></a>`SortByCreationOrder()` — [`L257`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L257) — Sorts the Traversal's execution_order by op creation index.
  - `Traversal(Traversal&&)` — [`L115`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L115)
  - `Traversal(std::vector<DeviceBufferRef> arguments, std::vector<SharedDeviceBufferList> execution_order, std::vector<DeviceBufferRef> outputs)` — [`L300`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L300) — Private constructor, only called by Traversal::Create().
  - `Traversal()` — [`L111`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L111) — Traversal cannot be directly constructed; use Create() instead.
  - `Traversal(const Traversal&)` — [`L114`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L114) — Delete copy and move constructors and assignment operators.
  - <a id="Traversal.Traversal"></a>`Traversal(std::vector<DeviceBufferRef> arguments, std::vector<SharedDeviceBufferList> execution_order, std::vector<DeviceBufferRef> outputs)` — [`L300`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L300) — Private constructor, only called by Traversal::Create().
  - <a id="Traversal.arguments"></a>`arguments()` — [`L160`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L160) — Returns the graph arguments.
  - <a id="Traversal.core_pinning_mode"></a>`core_pinning_mode()` — [`L265`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L265)
  - <a id="Traversal.execution_order"></a>`execution_order()` — [`L169`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L169) — Returns a topological sort of the deferred ops in the graph needed for
  - `operator=(const Traversal&)` — [`L116`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L116)
  - <a id="Traversal.operator"></a>`operator=(Traversal&&)` — [`L117`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L117)
  - <a id="Traversal.outputs"></a>`outputs()` — [`L175`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L175) — Returns the graph outputs.
  - <a id="Traversal.arguments_"></a>`arguments_` — [`L333`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L333) — The arguments to the Traversal are all DeviceBufferRefs which are in either
  - <a id="Traversal.core_pinning_mode_"></a>`core_pinning_mode_` — [`L354`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L354)
  - <a id="Traversal.execution_order_"></a>`execution_order_` — [`L338`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L338) — A execution_order traversal of the deferred ops in the graph.
  - <a id="Traversal.graph_key_"></a>`graph_key_` — [`L344`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L344) — The graph key of the Traversal, without considering the argument layouts
  - <a id="Traversal.outputs_"></a>`outputs_` — [`L341`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L341) — The tensor outputs of the Traversal. These may be in any state, but the
  - <a id="Traversal.resolved_da_"></a>`resolved_da_` — [`L347`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L347) — INT_VEC_OK
  - <a id="Traversal.shape_dynamism_metadata_"></a>`shape_dynamism_metadata_` — [`L352`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L352) — The acceptable dynamic bounds for each dimension in the traversal's
- uses (calls/refs, reference-scoped): [`DeviceBufferList`](device_buffer.h.md#DeviceBufferList), [`DeviceBufferRef`](device_buffer.h.md#DeviceBufferRef), [`ShapeDynamismMetadata`](../common/cache_key.h.md#ShapeDynamismMetadata), [`BuildMlirModule`](traversal.cc.md#Traversal.BuildMlirModule), [`CompilationCacheKey`](../common/cache_key.h.md#CompilationCacheKey), [`Compile`](traversal.cc.md#Traversal.Compile), [`SharedDeviceBufferList`](device_buffer.h.md#SharedDeviceBufferList), [`MaterializationReason`](structured_log_buffer.h.md#MaterializationReason), [`GetCacheKey`](traversal.cc.md#Traversal.GetCacheKey), [`BuildGraphKey`](traversal.cc.md#Traversal.BuildGraphKey), [`CompileOptionsKey`](../common/compile_options_key.h.md#CompileOptionsKey), [`Create`](traversal.cc.md#Traversal.Create), [`ValidateAndReorderArguments`](traversal.cc.md#Traversal.ValidateAndReorderArguments), [`GraphKey`](../common/cache_key.h.md#GraphKey), [`Validate`](traversal.cc.md#Traversal.Validate), [`CreateFromExecutionOrder`](traversal.cc.md#Traversal.CreateFromExecutionOrder), [`ReadableString`](traversal.cc.md#Traversal.ReadableString), [`CustomLayout`](../common/dimension_types.h.md#CustomLayout), [`GetMlirOpForProcessedBuffer`](traversal.cc.md#Traversal.GetMlirOpForProcessedBuffer), [`CompilationSpec`](../common/compilation_spec.h.md#CompilationSpec), [`GetGraphviz`](traversal.cc.md#GetGraphviz), [`CompiledKernel`](../common/compilation.h.md#CompiledKernel), [`PythonContext`](../ops/python_context.h.md#PythonContext), [`ApplyDeviceAssignmentToCompileSpec`](traversal.cc.md#Traversal.ApplyDeviceAssignmentToCompileSpec), [`MaybeUpdateSpecWithLayout`](traversal.cc.md#Traversal.MaybeUpdateSpecWithLayout), [`Create`](traversal.cc.md#Traversal.Create), [`ApplyDeviceAssignmentToCompileSpec`](traversal.cc.md#Traversal.ApplyDeviceAssignmentToCompileSpec), [`HasSparseCoreOp`](traversal.cc.md#Traversal.HasSparseCoreOp), [`DebugString`](traversal.cc.md#Traversal.DebugString), [`ResolveDeviceAssignment`](traversal.cc.md#Traversal.ResolveDeviceAssignment), [`IsSimpleNodeTraversal`](traversal.cc.md#IsSimpleNodeTraversal), [`CorePinningMode`](../common/cache_key.h.md#CorePinningMode), [`GetPythonContext`](traversal.cc.md#Traversal.GetPythonContext), [`IsBoundedDynamic`](traversal.cc.md#Traversal.IsBoundedDynamic), [`Create`](traversal.cc.md#Traversal.Create), [`kUnpinned`](../common/cache_key.h.md#CorePinningMode.kUnpinned), [`creation_index`](device_buffer.h.md#DeviceBufferList.creation_index), [`ResolveDeviceAssignment`](traversal.cc.md#Traversal.ResolveDeviceAssignment), [`GetGraphviz`](traversal.cc.md#GetGraphviz), [`Create`](traversal.cc.md#Traversal.Create)  (+3 more)
- used by: [`TraverseAndCompile`](../internal/compile/compiled_mode.cc.md#TraverseAndCompile), [`BuildMlirModule`](traversal.cc.md#Traversal.BuildMlirModule), [`ExtractMlirFromGraph`](../internal/compile/compiled_mode.cc.md#ExtractMlirFromGraph), [`ExtractArgumentLayoutsIfDifferentFromDefault`](execution_task.cc.md#ExtractArgumentLayoutsIfDifferentFromDefault), [`VerifyAndCompileTraversal`](execution_task.cc.md#VerifyAndCompileTraversal), [`Compile`](traversal.cc.md#Traversal.Compile), [`GetCacheKey`](traversal.cc.md#Traversal.GetCacheKey), [`TestBody`](../common/dynamism_utils_test.cc.md#DynamismOpsTest_GetTraversalOutputDimensionsWithBoundedInput_Test.TestBody), [`TestBody`](../common/dynamism_utils_test.cc.md#DynamismOpsTest_GetTraversalOutputDimensionsNoBoundedInput_Test.TestBody), [`BuildGraphKey`](traversal.cc.md#Traversal.BuildGraphKey), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_PrepareStreamTraversals_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_StreamsMaterializeSeparately_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_PrepareDeviceTraversals_Test.TestBody), [`TestBody`](traversal_test.cc.md#TraversalTest_CompileAnnotatesArgumentLayoutsWithTilingAndCaching_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_DeadSideEffectsRetained_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_GetsLiveDeferredBuffers_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_MaterializationAppendsExplicitEmptyOps_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_MaterializationIgnoresUnusedEmptyOps_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_SingleTraversalIfPossible_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_SplitModeRespected_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_UsedEmptyOpsMaterializedOnFirstUse_Test.TestBody), [`TestBody`](traversal_test.cc.md#TraversalTest_CompilePopulatesAndResetsOutCacheKey_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_DeadCodeEliminated_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_StreamMustMaterializeEmptyTensors_Test.TestBody), [`PrepareTraversals`](events_queue.cc.md#PrepareTraversals), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_DeviceMustMaterializeEmptyTensors_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_MultipleSnapshotsPulled_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_NodeMatcherAcrossSmallAndLargeSpans_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_NotPulledAfterLastSnapshot_Test.TestBody), [`TestBody`](events_queue_test.cc.md#EventsQueueTest_SingleOpFastPathAndExtraConstantFallback_Test.TestBody), [`FromTraversal`](execution_task.cc.md#ExecutionTask.FromTraversal), [`ApplySplitMode`](materialize.cc.md#ApplySplitMode), [`GraphvizVertexParams`](traversal.cc.md#GraphvizVertexParams), [`ExecutionTask`](execution_task.h.md#ExecutionTask), [`ValidateAndReorderArguments`](traversal.cc.md#Traversal.ValidateAndReorderArguments), [`TestBody`](split_traversal_test.cc.md#SplitTraversalTest_ApplySplitPointsSorted_Test.TestBody), [`TestBody`](traversal_test.cc.md#TraversalTest_CompileAnnotatesArgumentLayouts_Test.TestBody), [`TestBody`](traversal_test.cc.md#TraversalTest_PreCompileAndCompileCacheKeyMatch_Test.TestBody), [`Validate`](traversal.cc.md#Traversal.Validate), [`kBlack`](traversal.cc.md#Traversal.Create.Color.kBlack)  (+46 more)

### <a id="Traversal.Parts"></a>`Traversal.Parts`
- def: [`csrc/eager/traversal.h:239`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L239)
- doc: The core components of a Traversal, returned by IntoParts().
- signature: `struct Parts`
- members:
  - <a id="Traversal.Parts.arguments"></a>`arguments` — [`L240`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L240)
  - <a id="Traversal.Parts.execution_order"></a>`execution_order` — [`L241`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L241)
  - <a id="Traversal.Parts.outputs"></a>`outputs` — [`L242`](../../../../../../raw/code/torch_tpu/csrc/eager/traversal.h#L242)
- uses (calls/refs, reference-scoped): [`DeviceBufferRef`](device_buffer.h.md#DeviceBufferRef), [`SharedDeviceBufferList`](device_buffer.h.md#SharedDeviceBufferList)
- used by: [`FromTraversal`](execution_task.cc.md#ExecutionTask.FromTraversal), [`ApplySplitPoints`](split_traversal.cc.md#ApplySplitPoints)

