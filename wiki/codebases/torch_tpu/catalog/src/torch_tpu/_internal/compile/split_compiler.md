---
title: 'Module: src/torch_tpu/_internal/compile/split_compiler.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/split_compiler.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.split_compiler`/
symbols:
  SplitCompiler._compile_graph: SplitCompiler#_compile_graph().
  _SplitCompiledExecutable._maybe_handshake_and_recompile: _SplitCompiledExecutable#_maybe_handshake_and_recompile().
  _SplitCompiledExecutable.compiled_executables: _SplitCompiledExecutable#compiled_executables().
  _SplitCompiledExecutable.__reduce__: _SplitCompiledExecutable#__reduce__().
  SplitCompiler.__call__: SplitCompiler#__call__().
  _submit_handshake: _submit_handshake().
  _SubmodCompiler.run_node: _SubmodCompiler#run_node().
  _SplitCompiledExecutable: _SplitCompiledExecutable#
  _SubmodCompiler.compile_submod: _SubmodCompiler#compile_submod().
  _collect_namedtuple_types: _collect_namedtuple_types().
  _SplitCompiledExecutable.resolve: _SplitCompiledExecutable#resolve().
  _unpickle_split_compiled_executable: _unpickle_split_compiled_executable().
  _WrapperModule.forward: _WrapperModule#forward().
  _SubmodCompiler.fake_mode: _SubmodCompiler#fake_mode.
  _SplitCompiledExecutable.__init__: _SplitCompiledExecutable#__init__().
  _SplitCompiledExecutable.__call__: _SplitCompiledExecutable#__call__().
  _register_output_namedtuple_globals: _register_output_namedtuple_globals().
  _RANK_COLLECTIVE_COUNTS._RANK_COLLECTIVE_COUNTS: _RANK_COLLECTIVE_COUNTS._RANK_COLLECTIVE_COUNTS.
  ProcessGroupId: ProcessGroupId.
  CompiledArtifact: CompiledArtifact.
  _SplitCompiledExecutable.recompile_fn: _SplitCompiledExecutable#recompile_fn.
  _SubmodCompiler._convert_to_fake_tensor: _SubmodCompiler#_convert_to_fake_tensor().
  _SplitCompiledExecutable.fingerprint: _SplitCompiledExecutable#fingerprint().
  _WrapperModule.submod: _WrapperModule#submod.
  _SubmodCompiler.base_module_name: _SubmodCompiler#base_module_name.
  _SplitCompiledExecutable.pg_to_num_collectives: _SplitCompiledExecutable#pg_to_num_collectives.
  _SplitCompiledExecutable._split_gm: _SplitCompiledExecutable#_split_gm.
  _SubmodCompiler.__init__: _SubmodCompiler#__init__().
  _SplitCompiledExecutable.graph_module_debug_strs: _SplitCompiledExecutable#graph_module_debug_strs().
  _SplitCompiledExecutable.mlir_texts: _SplitCompiledExecutable#mlir_texts().
  _SplitCompiledExecutable.updates_default_generator_state: _SplitCompiledExecutable#updates_default_generator_state().
  _SplitCompiledExecutable._resolve: _SplitCompiledExecutable#_resolve().
  _SplitCompiledExecutable.is_resolved: _SplitCompiledExecutable#is_resolved().
  SplitCompiler.execute_pre_grad_passes: SplitCompiler#execute_pre_grad_passes().
  RankCollectiveCounts: RankCollectiveCounts.
  _WrapperModule: _WrapperModule#
  _SplitCompiledExecutable._graph_module_str: _SplitCompiledExecutable#_graph_module_str.
  SplitCompiler.base_compiler: SplitCompiler#base_compiler.
  CollectiveHandshakeRequest: CollectiveHandshakeRequest.
  Handshake: Handshake.
  _RANK_COLLECTIVE_COUNTS_LOCK: _RANK_COLLECTIVE_COUNTS_LOCK.
  _get_unique_wait_tensor_producer: _get_unique_wait_tensor_producer().
  _is_getitem_of_collective: _is_getitem_of_collective().
  _WrapperModule.unwrap_singleton_tuple: _WrapperModule#unwrap_singleton_tuple.
  _allow_non_fake_inputs: _allow_non_fake_inputs().
  _SubmodCompiler: _SubmodCompiler#
  _SubmodCompiler.compiler_fn: _SubmodCompiler#compiler_fn.
  AsyncCompiledArtifact: AsyncCompiledArtifact.
  TorchTpuCompiledExecutable: TorchTpuCompiledExecutable.
  _WrapperModule.__init__: _WrapperModule#__init__().
  SplitCompiler: SplitCompiler#
  SplitCompiler.__init__: SplitCompiler#__init__().
---
# Module: [`src/torch_tpu/_internal/compile/split_compiler.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py)

## Classes
### <a id="SplitCompiler"></a>`SplitCompiler`
- def: [`src/torch_tpu/_internal/compile/split_compiler.py:593`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L593)
- doc: Compiler that splits the graph on collectives and compiles submodules.
- signature: `class SplitCompiler(compiler.Compiler):`
- members:
  - <a id="SplitCompiler.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule, example_inputs: Sequence[InputType], is_fwd: bool = True, module_name: str | None = None)` — [`L745`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L745) — Splits the graph on collectives and compiles the submodules. — documented in [torch-compile-backend](../../../../../concepts/torch-compile-backend.md)
  - <a id="SplitCompiler._compile_graph"></a>`_compile_graph(self, graph_module: torch.fx.GraphModule, example_inputs: Sequence[InputType], is_fwd: bool = True, materialize_collectives: bool = True, module_name: str | None = None, **kwargs)` — [`L608`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L608) — Splits the graph on collectives and compiles the submodules. — documented in [fx-graph-passes](../../../../../concepts/fx-graph-passes.md)
  - <a id="SplitCompiler.execute_pre_grad_passes"></a>`execute_pre_grad_passes(self, graph_module: torch.fx.GraphModule)` — [`L602`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L602)
  - <a id="SplitCompiler.base_compiler"></a>`base_compiler` — [`L600`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L600)
- protocol/private: <a id="SplitCompiler.__init__"></a>`__init__`[`L596`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L596)
- uses (calls/refs, reference-scoped): [`_submit_handshake`](split_compiler.md#_submit_handshake), [`apply`](fx_passes/clone_mutated_returned_placeholders.md#apply), [`_SplitCompiledExecutable`](split_compiler.md#_SplitCompiledExecutable), [`apply`](fx_passes/sink_get_attr_constants.md#apply), [`apply`](fx_passes/force_collectives_output.md#apply), [`apply`](fx_passes/propagate_symints.md#apply), [`_register_output_namedtuple_globals`](split_compiler.md#_register_output_namedtuple_globals), [`ProcessGroupId`](split_compiler.md#ProcessGroupId), [`recompile_fn`](split_compiler.md#_SplitCompiledExecutable.recompile_fn), [`apply`](fx_passes/reorder_symints.md#apply), [`pg_to_num_collectives`](split_compiler.md#_SplitCompiledExecutable.pg_to_num_collectives), [`apply`](fx_passes/mark_embedded_constants.md#apply), [`_SubmodCompiler`](split_compiler.md#_SubmodCompiler), [`_get_unique_wait_tensor_producer`](split_compiler.md#_get_unique_wait_tensor_producer), [`_is_getitem_of_collective`](split_compiler.md#_is_getitem_of_collective)

### <a id="_SplitCompiledExecutable"></a>`_SplitCompiledExecutable`
- def: [`src/torch_tpu/_internal/compile/split_compiler.py:431`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L431) — documented in [torch-compile-backend](../../../../../concepts/torch-compile-backend.md)
- doc: A CompiledArtifact supporting split submodules.
- signature: `class _SplitCompiledExecutable(CompiledArtifact):`
- members:
  - <a id="_SplitCompiledExecutable.__init__"></a>`__init__(self, target: torch.fx.GraphModule, recompile_fn: Callable[[], _SplitCompiledExecutable] | None = None, pg_to_num_collectives: dict[ProcessGroupId, int] | None = None, graph_module_str: str | None = None)` — [`L434`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L434) — Initializes a _SplitCompiledExecutable.
  - <a id="_SplitCompiledExecutable.__reduce__"></a>`__reduce__(self)` — [`L488`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L488) — Enables pickling of the _SplitCompiledExecutable.
  - <a id="_SplitCompiledExecutable._maybe_handshake_and_recompile"></a>`_maybe_handshake_and_recompile(self)` — [`L460`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L460) — Verifies rank consensus on dispatch when running in DISPATCH_STAGE.
  - <a id="_SplitCompiledExecutable.compiled_executables"></a>`compiled_executables(self)` — [`L514`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L514) — Returns the list of underlying compiled executables.
  - <a id="_SplitCompiledExecutable.fingerprint"></a>`fingerprint(self)` — [`L558`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L558)
  - <a id="_SplitCompiledExecutable.graph_module_debug_strs"></a>`graph_module_debug_strs(self)` — [`L524`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L524) — List of string representations of the FX graph module's code for each submodule.
  - <a id="_SplitCompiledExecutable.is_resolved"></a>`is_resolved(self)` — [`L554`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L554) — Returns True if all submodule compilations are resolved.
  - <a id="_SplitCompiledExecutable.mlir_texts"></a>`mlir_texts(self)` — [`L533`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L533) — List of MLIR text representations of the compiled submodule's code.
  - <a id="_SplitCompiledExecutable.resolve"></a>`resolve(self)` — [`L545`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L545) — Waits for any pending background compilation in submodules to complete.
  - <a id="_SplitCompiledExecutable.updates_default_generator_state"></a>`updates_default_generator_state(self)` — [`L539`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L539)
  - <a id="_SplitCompiledExecutable.pg_to_num_collectives"></a>`pg_to_num_collectives` — [`L453`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L453)
  - <a id="_SplitCompiledExecutable.recompile_fn"></a>`recompile_fn` — [`L452`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L452)
- protocol/private: <a id="_SplitCompiledExecutable.__call__"></a>`__call__`[`L481`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L481), <a id="_SplitCompiledExecutable._graph_module_str"></a>`_graph_module_str`[`L456`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L456), <a id="_SplitCompiledExecutable._resolve"></a>`_resolve`[`L550`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L550), <a id="_SplitCompiledExecutable._split_gm"></a>`_split_gm`[`L458`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L458)
- uses (calls/refs, reference-scoped): [`_submit_handshake`](split_compiler.md#_submit_handshake), [`_unpickle_split_compiled_executable`](split_compiler.md#_unpickle_split_compiled_executable), [`CompiledArtifact`](split_compiler.md#CompiledArtifact), [`ProcessGroupId`](split_compiler.md#ProcessGroupId), [`submod`](split_compiler.md#_WrapperModule.submod), [`_WrapperModule`](split_compiler.md#_WrapperModule)
- used by: [`_compile_graph`](split_compiler.md#SplitCompiler._compile_graph), [`__call__`](split_compiler.md#SplitCompiler.__call__), [`_unpickle_split_compiled_executable`](split_compiler.md#_unpickle_split_compiled_executable)

### <a id="_SubmodCompiler"></a>`_SubmodCompiler`
- def: [`src/torch_tpu/_internal/compile/split_compiler.py:308`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L308)
- doc: Interpreter to propagate shape information and compile submodules.
- signature: `class _SubmodCompiler(torch.fx.interpreter.Interpreter):`
- members:
  - <a id="_SubmodCompiler.compile_submod"></a>`compile_submod(self, input_mod: torch.fx.GraphModule, args: list[torch.Tensor], kwargs: Any, submod_name: str | None = None)` — [`L349`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L349) — Compiles a single submodule into a PJRT executable wrapper.
  - <a id="_SubmodCompiler.run_node"></a>`run_node(self, n: torch.fx.Node)` — [`L384`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L384) — Intercepts submodule calls to compile them and propagate shapes.
  - <a id="_SubmodCompiler.base_module_name"></a>`base_module_name` — [`L326`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L326)
  - <a id="_SubmodCompiler.compiler_fn"></a>`compiler_fn` — [`L324`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L324)
  - <a id="_SubmodCompiler.fake_mode"></a>`fake_mode` — [`L325`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L325)
- protocol/private: <a id="_SubmodCompiler.__init__"></a>`__init__`[`L316`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L316), <a id="_SubmodCompiler._convert_to_fake_tensor"></a>`_convert_to_fake_tensor`[`L329`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L329)
- uses (calls/refs, reference-scoped): [`CompiledArtifact`](split_compiler.md#CompiledArtifact), [`_WrapperModule`](split_compiler.md#_WrapperModule), [`_allow_non_fake_inputs`](split_compiler.md#_allow_non_fake_inputs)
- used by: [`_compile_graph`](split_compiler.md#SplitCompiler._compile_graph)

### <a id="_WrapperModule"></a>`_WrapperModule`
- def: [`src/torch_tpu/_internal/compile/split_compiler.py:264`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L264)
- doc: Wrapper module for compiled submodules.
- signature: `class _WrapperModule(torch.nn.Module):`
- members:
  - <a id="_WrapperModule.forward"></a>`forward(self, *args: Any)` — [`L272`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L272)
  - <a id="_WrapperModule.submod"></a>`submod` — [`L269`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L269)
  - <a id="_WrapperModule.unwrap_singleton_tuple"></a>`unwrap_singleton_tuple` — [`L270`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L270)
- protocol/private: <a id="_WrapperModule.__init__"></a>`__init__`[`L267`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L267)
- used by: [`compiled_executables`](split_compiler.md#_SplitCompiledExecutable.compiled_executables), [`compile_submod`](split_compiler.md#_SubmodCompiler.compile_submod)

## Functions
- <a id="_allow_non_fake_inputs"></a>`_allow_non_fake_inputs(fake_mode: torch._subclasses.fake_tensor.FakeTensorMode)` — [`L283`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L283) — Temporarily lets `fake_mode` accept real tensors alongside fake ones.
- <a id="_collect_namedtuple_types"></a>`_collect_namedtuple_types(arg: Any, seen: dict[type[Any], None])` — [`L227`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L227) — Recursively collects namedtuple types from an FX node argument.
- <a id="_get_unique_wait_tensor_producer"></a>`_get_unique_wait_tensor_producer(node: torch.fx.Node)` — [`L137`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L137) — Returns the unique wait tensor producer node if it exists.
- <a id="_is_getitem_of_collective"></a>`_is_getitem_of_collective(node: torch.fx.Node)` — [`L199`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L199) — Checks whether node is a getitem extracting from a collective.
- <a id="_register_output_namedtuple_globals"></a>`_register_output_namedtuple_globals(gm: torch.fx.GraphModule)` — [`L241`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L241) — Registers namedtuple output types in the FX graph's codegen globals.
- <a id="_submit_handshake"></a>`_submit_handshake(executable_fingerprint: str, pg_to_num_collectives: dict[ProcessGroupId, int], graph_module_str: str | None = None)` — [`L71`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L71) — Submits a handshake message across participating ranks.
- <a id="_unpickle_split_compiled_executable"></a>`_unpickle_split_compiled_executable(target: torch.fx.GraphModule, recompile_fn: Callable[[], _SplitCompiledExecutable] | None = None, pg_to_num_collectives: dict[ProcessGroupId, int] | None = None, graph_module_str: str | None = None)` — [`L565`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L565) — Reconstructs a _SplitCompiledExecutable from target.

## Module values
- <a id="AsyncCompiledArtifact"></a>`AsyncCompiledArtifact` — [`L56`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L56)
- <a id="CollectiveHandshakeRequest"></a>`CollectiveHandshakeRequest` — [`L57`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L57)
- <a id="CompiledArtifact"></a>`CompiledArtifact` — [`L58`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L58)
- <a id="Handshake"></a>`Handshake` — [`L62`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L62)
- <a id="ProcessGroupId"></a>`ProcessGroupId` — [`L54`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L54)
- <a id="RankCollectiveCounts"></a>`RankCollectiveCounts` — [`L55`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L55)
- <a id="TorchTpuCompiledExecutable"></a>`TorchTpuCompiledExecutable` — [`L59`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L59)
- <a id="_RANK_COLLECTIVE_COUNTS._RANK_COLLECTIVE_COUNTS"></a>`_RANK_COLLECTIVE_COUNTS` — [`L67`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L67)
- <a id="_RANK_COLLECTIVE_COUNTS_LOCK"></a>`_RANK_COLLECTIVE_COUNTS_LOCK` — [`L68`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/split_compiler.py#L68)

