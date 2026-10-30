---
title: 'Module: src/torch_tpu/_internal/compile/compiler.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/compiler.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.compiler`/
symbols:
  StaticCompiler._compile: StaticCompiler#_compile().
  StaticCompiler.__call__: StaticCompiler#__call__().
  Compiler._debug: Compiler#_debug.
  Compiler.__init__: Compiler#__init__().
  Compiler: Compiler#
  _create_storage_aware_placeholders: _create_storage_aware_placeholders().
  StaticCompiler: StaticCompiler#
  Compiler.compilation_context: Compiler#compilation_context.
  Compiler.execute_pre_grad_passes: Compiler#execute_pre_grad_passes().
  Compiler.__call__: Compiler#__call__().
  has_dynamic_symints: has_dynamic_symints().
  StaticCompiler.__init__: StaticCompiler#__init__().
  CompilationContext: CompilationContext#
  has_dynamic_symints._is_dynamic_symint: has_dynamic_symints()._is_dynamic_symint().
  _is_tracing_enabled: _is_tracing_enabled().
  is_pinned_host_tensor: is_pinned_host_tensor().
  Compiler._use_stablehlo_bounds: Compiler#_use_stablehlo_bounds.
  _mark_auto_functionalized_mutations: _mark_auto_functionalized_mutations().
  StaticCompiler._async_compile_executor: StaticCompiler#_async_compile_executor.
  StaticCompiler._async_compile: StaticCompiler#_async_compile.
---
# Module: [`src/torch_tpu/_internal/compile/compiler.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py)

## Classes
### <a id="CompilationContext"></a>`CompilationContext`
- def: [`src/torch_tpu/_internal/compile/compiler.py:57`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L57) — documented in [compilation-pipeline](../../../../../concepts/compilation-pipeline.md)
- doc: Compilation state for a single graph module.
- signature: `class CompilationContext:`
- used by: [`__init__`](compiler.md#Compiler.__init__), [`compilation_context`](compiler.md#Compiler.compilation_context)

### <a id="Compiler"></a>`Compiler`  ·  implements/extends ABC
- def: [`src/torch_tpu/_internal/compile/compiler.py:66`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L66)
- doc: Abstract base class for a compiler.
- signature: `class Compiler(abc.ABC, AOTDispatchCompiler):`
- members:
  - <a id="Compiler.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule, example_inputs: Sequence[InputType], is_fwd: bool = True, module_name: str | None = None)` — [`L120`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L120) — Compiles the FX graph module into a callable artifact.
  - <a id="Compiler.__init__"></a>`__init__(self, compilation_context: CompilationContext | None = None, *, debug: bool | TpuCompileDebug | None = None, use_stablehlo_bounds: bool = False)` — [`L76`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L76) — Initializes the Compiler.
  - <a id="Compiler.execute_pre_grad_passes"></a>`execute_pre_grad_passes(self, graph_module: torch.fx.GraphModule)` — [`L103`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L103) — Executes graph passes on the FX graph module before AOT Autograd. — documented in [fx-graph-passes](../../../../../concepts/fx-graph-passes.md)
  - <a id="Compiler.compilation_context"></a>`compilation_context` — [`L95`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L95)
- protocol/private: <a id="Compiler._debug"></a>`_debug`[`L100`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L100), <a id="Compiler._use_stablehlo_bounds"></a>`_use_stablehlo_bounds`[`L101`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L101)
- uses (calls/refs, reference-scoped): [`CompiledArtifact`](torch_tpu_compiled_executable.md#CompiledArtifact), [`apply`](fx_passes/fold_gqa.md#apply), [`TpuCompileDebug`](debug.md#TpuCompileDebug), [`StaticCompiler`](compiler.md#StaticCompiler), [`CompilationContext`](compiler.md#CompilationContext)
- used by: [`_compile`](compiler.md#StaticCompiler._compile), [`StaticCompiler`](compiler.md#StaticCompiler), [`__init__`](compiler.md#StaticCompiler.__init__)

### <a id="StaticCompiler"></a>`StaticCompiler`  ·  implements/extends Compiler
- def: [`src/torch_tpu/_internal/compile/compiler.py:312`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L312)
- doc: Compiler for static shapes.
- signature: `class StaticCompiler(Compiler):`
- members:
  - <a id="StaticCompiler.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule, example_inputs: Sequence[InputType], is_fwd: bool = True, bounds: Sequence[Any] | None = None, argument_layouts: Sequence[Sequence[int]] | None = None, dynamic_outputs: Sequence[bool] | None = None, donated_inputs: Sequence[int] | None = None, module_name: str | None = None)` — [`L463`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L463) — Compiles the FX graph module for static shapes. — documented in [fx-graph-passes](../../../../../concepts/fx-graph-passes.md)
  - <a id="StaticCompiler.__init__"></a>`__init__(self, *args, async_compile: bool = False, **kwargs)` — [`L328`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L328) — Initializes a StaticCompiler instance.
- protocol/private: <a id="StaticCompiler._async_compile"></a>`_async_compile`[`L338`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L338), <a id="StaticCompiler._async_compile_executor"></a>`_async_compile_executor`[`L324`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L324), <a id="StaticCompiler._compile"></a>`_compile`[`L340`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L340)
- uses (calls/refs, reference-scoped): [`CompiledArtifact`](torch_tpu_compiled_executable.md#CompiledArtifact), [`TorchTpuCompiledExecutable`](torch_tpu_compiled_executable.md#TorchTpuCompiledExecutable), [`apply`](fx_passes/fold_gqa.md#apply), [`TpuCompileDebug`](debug.md#TpuCompileDebug), [`_debug`](compiler.md#Compiler._debug), [`graph_module_debug_str`](torch_tpu_compiled_executable.md#TorchTpuCompiledExecutable.graph_module_debug_str), [`mlir_text`](torch_tpu_compiled_executable.md#TorchTpuCompiledExecutable.mlir_text), [`AsyncCompiledArtifact`](torch_tpu_compiled_executable.md#AsyncCompiledArtifact), [`NoOpCompiledArtifact`](torch_tpu_compiled_executable.md#NoOpCompiledArtifact), [`__init__`](compiler.md#Compiler.__init__), [`apply`](fx_passes/detect_causal_mask.md#apply), [`stablehlo_backward_text`](debug.md#TpuCompileDebug.stablehlo_backward_text), [`stablehlo_forward_text`](debug.md#TpuCompileDebug.stablehlo_forward_text), [`Compiler`](compiler.md#Compiler), [`_create_storage_aware_placeholders`](compiler.md#_create_storage_aware_placeholders), [`_is_tracing_enabled`](compiler.md#_is_tracing_enabled), [`apply`](fx_passes/mark_embedded_constants.md#apply), [`_mark_auto_functionalized_mutations`](compiler.md#_mark_auto_functionalized_mutations), [`_use_stablehlo_bounds`](compiler.md#Compiler._use_stablehlo_bounds), [`apply`](fx_passes/mark_activation_checkpoints.md#apply)
- used by: [`Compiler`](compiler.md#Compiler)

## Functions
- <a id="_create_storage_aware_placeholders"></a>`_create_storage_aware_placeholders(example_inputs: Sequence[Any], bounds: Sequence[Any] | None = None, enabled: bool = True)` — [`L221`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L221) — Creates placeholder arguments preserving shared storage and view relationships.
- <a id="has_dynamic_symints._is_dynamic_symint"></a>`_is_dynamic_symint(val: Any)` — [`L164`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L164)
- <a id="_is_tracing_enabled"></a>`_is_tracing_enabled()` — [`L178`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L178) — Returns whether structured trace logging handlers are enabled.
- <a id="_mark_auto_functionalized_mutations"></a>`_mark_auto_functionalized_mutations(gm_or_graph: torch.fx.GraphModule | torch.fx.Graph)` — [`L204`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L204) — Marks auto_functionalized ops so decompose_auto_functionalized doesn't clone them.
- <a id="has_dynamic_symints"></a>`has_dynamic_symints(args: Any)` — [`L150`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L150) — Checks whether truly dynamic SymInt inputs or shapes exist.
- <a id="is_pinned_host_tensor"></a>`is_pinned_host_tensor(t: Any)` — [`L187`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/compiler.py#L187) — Returns whether `t` is a Tensor located in pinned host memory.

