---
title: 'Module: src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.dynamic.dynamic_compiler`/
symbols:
  DynamicCompiler.__call__: DynamicCompiler#__call__().
  DynamicCompiler._prepare_bucket_spec: DynamicCompiler#_prepare_bucket_spec().
  _create_bounded_model_inputs: _create_bounded_model_inputs().
  DynamicCompiler.execute_pre_grad_passes: DynamicCompiler#execute_pre_grad_passes().
  _can_use_pad_real_to_static: _can_use_pad_real_to_static().
  DynamicCompiler.static_compiler: DynamicCompiler#static_compiler.
  DynamicCompiler: DynamicCompiler#
  DynamicCompiler._num_buckets: DynamicCompiler#_num_buckets.
  DynamicCompiler._num_lookahead_buckets: DynamicCompiler#_num_lookahead_buckets.
  DynamicCompiler._bucket_size: DynamicCompiler#_bucket_size.
  DynamicCompiler.__init__: DynamicCompiler#__init__().
---
# Module: [`src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py)

## Classes
### <a id="DynamicCompiler"></a>`DynamicCompiler`
- def: [`src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py:113`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py#L113) — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- doc: Compiler for handling dynamic shapes in torch.compile().
- signature: `class DynamicCompiler(compiler.Compiler):`
- members:
  - <a id="DynamicCompiler.__call__"></a>`__call__(self, graph_module: torch.fx.GraphModule, example_inputs: Sequence[InputType], is_fwd: bool = True, module_name: str | None = None)` — [`L217`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py#L217) — Called by AOT Autograd to compile the graph. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="DynamicCompiler.__init__"></a>`__init__(self, compilation_context: compiler.CompilationContext | None = None, *, debug: bool | compiler.TpuCompileDebug | None = None, num_buckets: int = 1, num_lookahead_buckets: int | None = None, bucket_size: int = 128)` — [`L116`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py#L116) — Initializes the DynamicCompiler instance.
  - <a id="DynamicCompiler._prepare_bucket_spec"></a>`_prepare_bucket_spec(self, graph_module: torch.fx.GraphModule, example_inputs: Sequence[InputType], symbol_bounds: SymbolBounds, use_pad_real_to_static: bool)` — [`L173`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py#L173) — Transforms a cloned FX graph and creates bounded inputs for `symbol_bounds`. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="DynamicCompiler.execute_pre_grad_passes"></a>`execute_pre_grad_passes(self, graph_module: torch.fx.GraphModule)` — [`L161`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py#L161)
  - <a id="DynamicCompiler.static_compiler"></a>`static_compiler` — [`L154`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py#L154)
- protocol/private: <a id="DynamicCompiler._bucket_size"></a>`_bucket_size`[`L151`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py#L151), <a id="DynamicCompiler._num_buckets"></a>`_num_buckets`[`L142`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py#L142), <a id="DynamicCompiler._num_lookahead_buckets"></a>`_num_lookahead_buckets`[`L148`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py#L148)
- uses (calls/refs, reference-scoped): [`apply_dynamism_transformations`](graph_transformations.md#apply_dynamism_transformations), [`SymbolBounds`](symbol_bounds.md#SymbolBounds), [`apply_pre_dynamism_transformations`](graph_transformations.md#apply_pre_dynamism_transformations), [`get_bucketed_symbol_bounds`](sym_bounds_manager.md#SymBoundsManager.get_bucketed_symbol_bounds), [`get_fallback_symbol_bounds`](sym_bounds_manager.md#SymBoundsManager.get_fallback_symbol_bounds), [`add_bound_checks`](sym_bounds_manager.md#SymBoundsManager.add_bound_checks), [`create_output_sym_shapes`](output_sym_shape.md#create_output_sym_shapes), [`_create_bounded_model_inputs`](dynamic_compiler.md#_create_bounded_model_inputs), [`symbol_bounds`](dynamic_executable.md#BucketCompilationSpec.symbol_bounds), [`merge_bounds`](symbol_bounds.md#SymbolBounds.merge_bounds), [`BucketCompilationSpec`](dynamic_executable.md#BucketCompilationSpec), [`_can_use_pad_real_to_static`](dynamic_compiler.md#_can_use_pad_real_to_static), [`DynamicTpuCompiledExecutable`](dynamic_executable.md#DynamicTpuCompiledExecutable), [`model_input_bounds`](dynamic_executable.md#BucketCompilationSpec.model_input_bounds), [`SymBoundsManager`](sym_bounds_manager.md#SymBoundsManager), [`bounded_model_inputs`](dynamic_executable.md#BucketCompilationSpec.bounded_model_inputs), [`graph_module`](dynamic_executable.md#BucketCompilationSpec.graph_module), [`ReplaceDynamicOutputBroadcastOpsPreGradPass`](view_ops_passes.md#ReplaceDynamicOutputBroadcastOpsPreGradPass)
- used by: [`make_backend_compiler`](../_backend.md#make_backend_compiler)

## Functions
- <a id="_can_use_pad_real_to_static"></a>`_can_use_pad_real_to_static(example_inputs: Sequence[Any])` — [`L97`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py#L97) — Returns True if dynamic input tensors can be lowered to pad_real_to_static.
- <a id="_create_bounded_model_inputs"></a>`_create_bounded_model_inputs(example_inputs: Sequence[InputType], bounds: SymbolBounds)` — [`L41`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_compiler.py#L41) — Specializes dynamic inputs to their static upper bounds and constructs TensorBounds.

