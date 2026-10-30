---
title: 'Module: csrc/eager/execution_task.cc'
type: catalog
provenance: extracted
module: csrc/eager/execution_task.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  VerifyAndCompileTraversal: '`$anonymous_namespace_csrc/eager/execution_task.cc`/VerifyAndCompileTraversal(50817c4992fe0ef2).'
  ExtractArgumentLayoutsIfDifferentFromDefault: '`$anonymous_namespace_csrc/eager/execution_task.cc`/ExtractArgumentLayoutsIfDifferentFromDefault(2cb79e7a335c19a8).'
  ExecutionTask.RunInternal: ExecutionTask#RunInternal(c8a92d17d58c956f).
  ExecutionTask.FromTraversal: ExecutionTask#FromTraversal(b46597a8241dfeb9).
  FinalizePushTraceEvent: '`$anonymous_namespace_csrc/eager/execution_task.cc`/FinalizePushTraceEvent(71c704a4fe59dc08).'
  ExecutionTask.SetOutputNodesAsMaterialized: ExecutionTask#SetOutputNodesAsMaterialized(365121bef01be58a).
  PropagateBoundedDynamism: '`$anonymous_namespace_csrc/eager/execution_task.cc`/PropagateBoundedDynamism(ca19b81571c8bd61).'
  ExecutionTask.FromExecutable: ExecutionTask#FromExecutable(fa660a71d7354877).
  ExecutionTask.GetArgumentBuffers: ExecutionTask#GetArgumentBuffers(b126dc7c1de90089).
  MaybeStartTraceEvent: '`$anonymous_namespace_csrc/eager/execution_task.cc`/MaybeStartTraceEvent(8ba63c6321160ac8).'
  RunSequentialExecutables: '`$anonymous_namespace_csrc/eager/execution_task.cc`/RunSequentialExecutables(4817ea0dba6e2c80).'
  ExecutionTask.GetCachedExecutables: ExecutionTask#GetCachedExecutables(32b27946a8db50ca).
  ExecutionTask.FromTraversalWithLogging: ExecutionTask#FromTraversalWithLogging(96c7096886a00d1c).
  GetShapesFromDeviceBuffers: '`$anonymous_namespace_csrc/eager/execution_task.cc`/GetShapesFromDeviceBuffers(637a2b3bf07c05fd).'
  ExecutionTask.SetOutputNodesAsError: ExecutionTask#SetOutputNodesAsError(2814731695a089b8).
  LogCompilationWait: '`$anonymous_namespace_csrc/eager/execution_task.cc`/LogCompilationWait(a6cba5485d5ce43a).'
  ExecutionTask.Run: ExecutionTask#Run(c8a92d17d58c956f).
  TilesMatchDefault: '`$anonymous_namespace_csrc/eager/execution_task.cc`/TilesMatchDefault(fc8f8704e25a86af).'
  CompiledTraversal.compiled_kernel: '`$anonymous_namespace_csrc/eager/execution_task.cc`/CompiledTraversal#compiled_kernel.'
  CompiledTraversal: '`$anonymous_namespace_csrc/eager/execution_task.cc`/CompiledTraversal#'
  CompiledTraversal.compilation_cache_key: '`$anonymous_namespace_csrc/eager/execution_task.cc`/CompiledTraversal#compilation_cache_key.'
---
# Module: [`csrc/eager/execution_task.cc`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc)

## Classes
### <a id="CompiledTraversal"></a>`CompiledTraversal`
- def: [`csrc/eager/execution_task.cc:281`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L281)
- signature: `struct CompiledTraversal`
- members:
  - <a id="CompiledTraversal.compilation_cache_key"></a>`compilation_cache_key` — [`L282`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L282)
  - <a id="CompiledTraversal.compiled_kernel"></a>`compiled_kernel` — [`L283`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L283)
- uses (calls/refs, reference-scoped): [`CompilationCacheKey`](../common/cache_key.h.md#CompilationCacheKey), [`CompiledKernel`](../common/compilation.h.md#CompiledKernel)
- used by: [`VerifyAndCompileTraversal`](execution_task.cc.md#VerifyAndCompileTraversal), [`FromTraversal`](execution_task.cc.md#ExecutionTask.FromTraversal)

## Functions
- `ExtractArgumentLayoutsIfDifferentFromDefault(const Traversal& traversal)` — [`L222`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L222)
- <a id="ExtractArgumentLayoutsIfDifferentFromDefault"></a>`ExtractArgumentLayoutsIfDifferentFromDefault(const Traversal& traversal)` — [`L222`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L222)
- `FinalizePushTraceEvent(std::unique_ptr<StructuredLogEvent> event, std::string captured_mlir, bool compile_ok, std::string aten_graph_payload)` — [`L182`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L182)
- <a id="FinalizePushTraceEvent"></a>`FinalizePushTraceEvent(std::unique_ptr<StructuredLogEvent> event, std::string captured_mlir, bool compile_ok, std::string aten_graph_payload)` — [`L182`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L182)
- `GetShapesFromDeviceBuffers(absl::Span<const DeviceBufferRef> buffers)` — [`L363`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L363)
- <a id="GetShapesFromDeviceBuffers"></a>`GetShapesFromDeviceBuffers(absl::Span<const DeviceBufferRef> buffers)` — [`L363`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L363)
- <a id="LogCompilationWait"></a>`LogCompilationWait(const CompiledKernel& compiled_kernel, std::string_view task_name)` — [`L481`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L481)
- <a id="MaybeStartTraceEvent"></a>`MaybeStartTraceEvent(MaterializationReason reason, const Traversal& split_traversal)` — [`L164`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L164) — Returns nullptr if tracing is disabled. The returned event is only
- `MaybeStartTraceEvent(MaterializationReason reason, const Traversal& split_traversal)` — [`L164`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L164) — Returns nullptr if tracing is disabled. The returned event is only
- <a id="PropagateBoundedDynamism"></a>`PropagateBoundedDynamism(Traversal& traversal, mlir::MLIRContext& mlir_context)` — [`L138`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L138) — Propagates bounded dynamism annotations from one traversal to others
- `RunSequentialExecutables(absl::Span<const SharedLoadedExecutableWithMetadata> executables, std::vector<xla::PjRtBuffer*> argument_buffers, absl::Span<const Shape> logical_output_shapes, std::string_view task_name)` — [`L508`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L508)
- <a id="RunSequentialExecutables"></a>`RunSequentialExecutables(absl::Span<const SharedLoadedExecutableWithMetadata> executables, std::vector<xla::PjRtBuffer*> argument_buffers, absl::Span<const Shape> logical_output_shapes, std::string_view task_name)` — [`L508`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L508)
- <a id="TilesMatchDefault"></a>`TilesMatchDefault(absl::Span<const Indices> layout_tiles, absl::Span<const xla::Tile> default_tiles)` — [`L205`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L205) — Returns whether the specified layout tiles match the device default tiles.
- `TilesMatchDefault(absl::Span<const Indices> layout_tiles, absl::Span<const xla::Tile> default_tiles)` — [`L205`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L205) — Returns whether the specified layout tiles match the device default tiles.
- <a id="VerifyAndCompileTraversal"></a>`VerifyAndCompileTraversal(Traversal& traversal, mlir::MLIRContext& mlir_context, const CompilationSpec& compilation_spec, std::string* absl_nullable out_mlir_text)` — [`L286`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L286)

## Other members
- `FromExecutable` — [`L409`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L409)
- `SetOutputNodesAsMaterialized` — [`L608`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L608)
- `GetCachedExecutables` — [`L532`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L532)
- `GetArgumentBuffers` — [`L583`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L583)
- `FromTraversalWithLogging` — [`L447`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L447)
- `FromTraversal` — [`L377`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L377)
- <a id="ExecutionTask.FromExecutable"></a>`ExecutionTask.FromExecutable` — [`L409`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L409)
- <a id="ExecutionTask.FromTraversal"></a>`ExecutionTask.FromTraversal` — [`L377`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L377)
- <a id="ExecutionTask.FromTraversalWithLogging"></a>`ExecutionTask.FromTraversalWithLogging` — [`L447`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L447)
- <a id="ExecutionTask.GetArgumentBuffers"></a>`ExecutionTask.GetArgumentBuffers` — [`L583`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L583)
- <a id="ExecutionTask.GetCachedExecutables"></a>`ExecutionTask.GetCachedExecutables` — [`L532`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L532)
- <a id="ExecutionTask.Run"></a>`ExecutionTask.Run` — [`L688`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L688)
- <a id="ExecutionTask.RunInternal"></a>`ExecutionTask.RunInternal` — [`L646`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L646)
- <a id="ExecutionTask.SetOutputNodesAsError"></a>`ExecutionTask.SetOutputNodesAsError` — [`L473`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L473)
- <a id="ExecutionTask.SetOutputNodesAsMaterialized"></a>`ExecutionTask.SetOutputNodesAsMaterialized` — [`L608`](../../../../../../raw/code/torch_tpu/csrc/eager/execution_task.cc#L608)

