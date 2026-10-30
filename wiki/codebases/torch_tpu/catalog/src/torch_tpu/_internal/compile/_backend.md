---
title: 'Module: src/torch_tpu/_internal/compile/_backend.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/_backend.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile._backend`/
symbols:
  TpuBackend.__call__: TpuBackend#__call__().
  TpuBackend._compile_graph_module: TpuBackend#_compile_graph_module().
  resolve_compilations: resolve_compilations().
  _CacheSavesManager.async_save: _CacheSavesManager#async_save().
  clear_cache: clear_cache().
  async_compile: async_compile().
  _get_reload_source_placeholder: _get_reload_source_placeholder().
  _mark_pinned_host_inputs: _mark_pinned_host_inputs().
  _CacheSavesManager.flush: _CacheSavesManager#flush().
  _serialization_context: _serialization_context().
  make_backend_compiler: make_backend_compiler().
  _CacheSavesManager._get_futures: _CacheSavesManager#_get_futures().
  _CacheSavesManager._add: _CacheSavesManager#_add().
  _CacheSavesManager._discard: _CacheSavesManager#_discard().
  _CacheSavesManager._difference_update: _CacheSavesManager#_difference_update().
  _CacheSavesManager.async_aot_cache_saves: _CacheSavesManager#async_aot_cache_saves().
  TpuBackend.clear_cache: TpuBackend#clear_cache().
  _cache_saves_manager._cache_saves_manager: _cache_saves_manager._cache_saves_manager.
  to_device: to_device().
  _CacheSavesManager._cache_save_lock: _CacheSavesManager#_cache_save_lock.
  AsyncCompilationSubmitted.artifact: AsyncCompilationSubmitted#artifact.
  _log_gm_and_inputs: _log_gm_and_inputs().
  TpuBackend.skip_execution_on_warmup_if_async: TpuBackend#skip_execution_on_warmup_if_async().
  _CacheSavesManager._pending_cache_saves: _CacheSavesManager#_pending_cache_saves.
  AsyncCompilationSubmitted: AsyncCompilationSubmitted#
  to_device._to: to_device()._to().
  _serialization_context._patched_cache_inference_info: _serialization_context()._patched_cache_inference_info().
  AsyncCompilationSubmitted.resolve: AsyncCompilationSubmitted#resolve().
  _sanitize_module_name: _sanitize_module_name().
  _get_module_name: _get_module_name().
  _serialization_context._patched_extract_meta: _serialization_context()._patched_extract_meta().
  TpuBackend: TpuBackend#
  TpuBackend._debug: TpuBackend#_debug.
  TpuBackend._num_compiled_executables: TpuBackend#_num_compiled_executables.
  _ExpectedTypes._ExpectedTypes: _ExpectedTypes._ExpectedTypes.
  _MAX_DYNAMIC_BUCKETS: _MAX_DYNAMIC_BUCKETS.
  _is_ao_op: _is_ao_op().
  _extract_tensor_node: _extract_tensor_node().
  _split_str_for_logging: _split_str_for_logging().
  _CacheSavesManager: _CacheSavesManager#
  TpuBackend._enable_serialization: TpuBackend#_enable_serialization.
  TpuBackend._compiled_executables: TpuBackend#_compiled_executables.
  _TPU_DECOMPOSITIONS: _TPU_DECOMPOSITIONS.
  _is_view_node: _is_view_node().
  _CacheSavesManager._cache_save_executor: _CacheSavesManager#_cache_save_executor.
  _CacheSavesManager._safe_save: _CacheSavesManager#_safe_save().
  _guard_input_storage_offsets: _guard_input_storage_offsets().
  _VALID_SYMBOL_REGEX: _VALID_SYMBOL_REGEX.
  TpuBackend.wait_and_call: TpuBackend#wait_and_call().
  _unpack_warmup_args: _unpack_warmup_args().
  get_default_cpu_backend: get_default_cpu_backend().
  _CacheSavesManager.__init__: _CacheSavesManager#__init__().
  AsyncCompilationSubmitted.__init__: AsyncCompilationSubmitted#__init__().
  TpuBackend.__init__: TpuBackend#__init__().
  TpuBackend._dynamism: TpuBackend#_dynamism.
---
# Module: [`src/torch_tpu/_internal/compile/_backend.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py)

## Classes
### <a id="AsyncCompilationSubmitted"></a>`AsyncCompilationSubmitted`  ·  implements/extends Exception
- def: [`src/torch_tpu/_internal/compile/_backend.py:534`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L534)
- doc: Control-flow signal to force AOTAutograd to skip execution after compile.
- signature: `class AsyncCompilationSubmitted(Exception):`
- members:
  - <a id="AsyncCompilationSubmitted.resolve"></a>`resolve(self)` — [`L549`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L549) — Waits for the pending background compilation to complete.
  - <a id="AsyncCompilationSubmitted.artifact"></a>`artifact` — [`L547`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L547)
- protocol/private: <a id="AsyncCompilationSubmitted.__init__"></a>`__init__`[`L545`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L545)
- used by: [`resolve_compilations`](_backend.md#resolve_compilations), [`async_compile`](_backend.md#async_compile), [`skip_execution_on_warmup_if_async`](_backend.md#TpuBackend.skip_execution_on_warmup_if_async)

### <a id="TpuBackend"></a>`TpuBackend`
- def: [`src/torch_tpu/_internal/compile/_backend.py:613`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L613)
- doc: TPU backend for torch.compile() integration.
- signature: `class TpuBackend:`
- members:
  - <a id="TpuBackend.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule, example_inputs: Sequence[torch.Tensor], **kwargs)` — [`L654`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L654) — Compiles the provided `torch.fx.GraphModule` with the XLA compiler. — documented in [torch-compile-backend](../../../../../concepts/torch-compile-backend.md)
  - <a id="TpuBackend.__init__"></a>`__init__(self, debug: bool = False, dynamism: bool = False, enable_serialization: bool = True)` — [`L618`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L618) — Initializes the TPU backend.
  - <a id="TpuBackend._compile_graph_module"></a>`_compile_graph_module(self, compiler_instance: compiler.Compiler, is_fwd: bool, custom_module_name: str | None, debug: TpuCompileDebug | None, compiled_artifacts: list[compiler.CompiledArtifact], graph_module: torch.fx.GraphModule, example_inputs: Sequence[torch.Tensor])` — [`L866`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L866) — Compiles the graph_module with the given inputs for TPU. — documented in [torch-compile-backend](../../../../../concepts/torch-compile-backend.md)
  - <a id="TpuBackend.clear_cache"></a>`clear_cache(self)` — [`L649`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L649) — Clears any cached/retained compiled executables and resets counters.
  - <a id="TpuBackend.skip_execution_on_warmup_if_async"></a>`skip_execution_on_warmup_if_async(*args: Any, **kwargs: Any)` — [`L825`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L825)
  - <a id="TpuBackend.wait_and_call"></a>`wait_and_call()` — [`L851`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L851)
- protocol/private: <a id="TpuBackend._compiled_executables"></a>`_compiled_executables`[`L646`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L646), <a id="TpuBackend._debug"></a>`_debug`[`L641`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L641), <a id="TpuBackend._dynamism"></a>`_dynamism`[`L642`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L642), <a id="TpuBackend._enable_serialization"></a>`_enable_serialization`[`L643`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L643), <a id="TpuBackend._num_compiled_executables"></a>`_num_compiled_executables`[`L647`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L647)
- uses (calls/refs, reference-scoped): [`TpuCompileDebug`](debug.md#TpuCompileDebug), [`_mark_pinned_host_inputs`](_backend.md#_mark_pinned_host_inputs), [`AsyncCompiledArtifact`](torch_tpu_compiled_executable.md#AsyncCompiledArtifact), [`_serialization_context`](_backend.md#_serialization_context), [`async_aot_cache_saves`](_backend.md#_CacheSavesManager.async_aot_cache_saves), [`make_backend_compiler`](_backend.md#make_backend_compiler), [`_cache_saves_manager`](_backend.md#_cache_saves_manager._cache_saves_manager), [`_log_gm_and_inputs`](_backend.md#_log_gm_and_inputs), [`AsyncCompilationSubmitted`](_backend.md#AsyncCompilationSubmitted), [`post_autograd_fx_backward_code`](debug.md#TpuCompileDebug.post_autograd_fx_backward_code), [`post_autograd_fx_forward_code`](debug.md#TpuCompileDebug.post_autograd_fx_forward_code), [`pre_autograd_fx_code`](debug.md#TpuCompileDebug.pre_autograd_fx_code), [`_get_module_name`](_backend.md#_get_module_name), [`compiled_executables`](debug.md#TpuCompileDebug.compiled_executables), [`_MAX_DYNAMIC_BUCKETS`](_backend.md#_MAX_DYNAMIC_BUCKETS), [`_future`](torch_tpu_compiled_executable.md#AsyncCompiledArtifact._future), [`_TPU_DECOMPOSITIONS`](_backend.md#_TPU_DECOMPOSITIONS), [`_guard_input_storage_offsets`](_backend.md#_guard_input_storage_offsets), [`post_autograd_fx_backward_readable`](debug.md#TpuCompileDebug.post_autograd_fx_backward_readable), [`post_autograd_fx_forward_readable`](debug.md#TpuCompileDebug.post_autograd_fx_forward_readable), [`pre_autograd_fx_readable`](debug.md#TpuCompileDebug.pre_autograd_fx_readable)
- used by: [`clear_cache`](_backend.md#clear_cache)

### <a id="_CacheSavesManager"></a>`_CacheSavesManager`
- def: [`src/torch_tpu/_internal/compile/_backend.py:468`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L468)
- doc: Manages asynchronously saving to the AOTAutograd cache in a thread-safe manner.
- signature: `class _CacheSavesManager:`
- members:
  - <a id="_CacheSavesManager.async_aot_cache_saves"></a>`async_aot_cache_saves(self)` — [`L504`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L504) — Offloads AOTAutogradCache.save to a background thread during async compile.
  - <a id="_CacheSavesManager.async_save"></a>`async_save(*args: Any, **kwargs: Any)` — [`L510`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L510) — documented in [torch-compile-backend](../../../../../concepts/torch-compile-backend.md)
  - <a id="_CacheSavesManager.flush"></a>`flush(self)` — [`L496`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L496) — Waits for all pending asynchronous AOTAutograd cache saves to complete.
- protocol/private: <a id="_CacheSavesManager.__init__"></a>`__init__`[`L471`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L471), <a id="_CacheSavesManager._add"></a>`_add`[`L482`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L482), <a id="_CacheSavesManager._cache_save_executor"></a>`_cache_save_executor`[`L472`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L472), <a id="_CacheSavesManager._cache_save_lock"></a>`_cache_save_lock`[`L475`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L475), <a id="_CacheSavesManager._difference_update"></a>`_difference_update`[`L490`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L490), <a id="_CacheSavesManager._discard"></a>`_discard`[`L486`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L486), <a id="_CacheSavesManager._get_futures"></a>`_get_futures`[`L478`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L478), <a id="_CacheSavesManager._pending_cache_saves"></a>`_pending_cache_saves`[`L476`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L476), <a id="_CacheSavesManager._safe_save"></a>`_safe_save`[`L511`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L511)
- used by: [`__call__`](_backend.md#TpuBackend.__call__), [`resolve_compilations`](_backend.md#resolve_compilations), [`clear_cache`](_backend.md#clear_cache), [`_cache_saves_manager`](_backend.md#_cache_saves_manager._cache_saves_manager)

## Functions
- <a id="_extract_tensor_node"></a>`_extract_tensor_node(node: torch.fx.Node)` — [`L162`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L162) — Extracts the input tensor node from positional args or kwargs.
- <a id="_get_module_name"></a>`_get_module_name(custom_module_name: str | None, is_fwd: bool, split_idx: int)` — [`L600`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L600) — Extracts a human-readable module name for the compiled MLIR graph.
- <a id="_get_reload_source_placeholder"></a>`_get_reload_source_placeholder(node: torch.fx.Node | None)` — [`L176`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L176) — Unwraps views from a reload argument to find its source placeholder, if any.
- <a id="_guard_input_storage_offsets"></a>`_guard_input_storage_offsets(graph_module: torch.fx.GraphModule)` — [`L559`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L559) — Installs Dynamo guards on storage_offset for all tensor placeholder inputs.
- <a id="_is_ao_op"></a>`_is_ao_op(node: torch.fx.Node, op_name: str)` — [`L127`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L127) — Returns whether `node` represents a torch.ops.ao.{op_name} operation.
- <a id="_is_view_node"></a>`_is_view_node(node: torch.fx.Node)` — [`L139`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L139) — Returns whether `node` is a view, container unpack, or `index_select`.
- <a id="_log_gm_and_inputs"></a>`_log_gm_and_inputs(loc: str, pre_or_post: str, gm: torch.fx.GraphModule, inputs: Sequence[Any])` — [`L410`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L410) — Logs the FX graph and example inputs.
- <a id="_mark_pinned_host_inputs"></a>`_mark_pinned_host_inputs(graph_module: torch.fx.GraphModule, example_inputs: Sequence[Any])` — [`L207`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L207) — Marks example inputs corresponding to offloaded activations. — documented in [torch-compile-backend](../../../../../concepts/torch-compile-backend.md)
- <a id="_serialization_context._patched_cache_inference_info"></a>`_patched_cache_inference_info(aot_config, fw_metadata, maybe_subclass_meta, compiled_fw, aot_forward_graph_str, wrappers)` — [`L317`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L317)
- <a id="_serialization_context._patched_extract_meta"></a>`_patched_extract_meta(t: torch.Tensor)` — [`L290`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L290)
- <a id="_sanitize_module_name"></a>`_sanitize_module_name(name: str)` — [`L595`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L595) — Ensures name is a valid MLIR symbol (alphanumeric + underscores).
- <a id="_serialization_context"></a>`_serialization_context(example_inputs: Sequence[Any], enable: bool = False)` — [`L232`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L232) — Optionally configures aot_autograd to produce a BundledAOTAutogradResult.
- <a id="_split_str_for_logging"></a>`_split_str_for_logging(text, limit=13000)` — [`L396`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L396) — Splits a string longer than the log line char limit into multiple chunks.
- <a id="to_device._to"></a>`_to(t: _ExpectedTypes)` — [`L115`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L115)
- <a id="_unpack_warmup_args"></a>`_unpack_warmup_args(args: Any)` — [`L969`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L969) — Unpacks warmup argument item into positional tuple and keyword dictionary.
- <a id="async_compile"></a>`async_compile(fn: Callable[..., Any], warmup_inputs: Sequence[Any], *, no_grad: bool = True, **backend_kwargs: Any)` — [`L989`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L989) — Compiles `fn` across multiple static shapes asynchronously, overlapping
- <a id="clear_cache"></a>`clear_cache()` — [`L934`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L934) — Flushes pending AOTAutograd cache saves and clears TpuBackend state.
- <a id="get_default_cpu_backend"></a>`get_default_cpu_backend()` — [`L82`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L82) — Returns the default Dynamo backend to use for CPU-only graphs.
- <a id="make_backend_compiler"></a>`make_backend_compiler(example_inputs: Sequence[Any], async_compile: bool = False, debug: TpuCompileDebug | None = None, num_dynamic_buckets: int = 1, bucket_size: int = 128)` — [`L432`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L432) — Creates a compiler configured for static or dynamic compilation. — documented in [dynamic-shapes-compiler](../../../../../concepts/dynamic-shapes-compiler.md)
- <a id="resolve_compilations"></a>`resolve_compilations(artifacts: Sequence[Any])` — [`L943`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L943) — Waits for a sequence of pending compilation artifacts to finish compiling.
- <a id="to_device"></a>`to_device(x: Any, backend: str | torch.device)` — [`L96`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L96) — Moves complex objects containing tensors to the specified backend device.

## Module values
- <a id="_ExpectedTypes._ExpectedTypes"></a>`_ExpectedTypes` — [`L76`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L76)
- <a id="_MAX_DYNAMIC_BUCKETS"></a>`_MAX_DYNAMIC_BUCKETS` — [`L79`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L79)
- <a id="_TPU_DECOMPOSITIONS"></a>`_TPU_DECOMPOSITIONS` — [`L67`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L67)
- <a id="_VALID_SYMBOL_REGEX"></a>`_VALID_SYMBOL_REGEX` — [`L592`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L592)
- <a id="_cache_saves_manager._cache_saves_manager"></a>`_cache_saves_manager` — [`L530`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/_backend.py#L530)

