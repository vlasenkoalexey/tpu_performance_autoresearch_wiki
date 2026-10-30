---
title: 'Module: src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.dynamic.dynamic_executable`/
symbols:
  DynamicTpuCompiledExecutable.__call__: DynamicTpuCompiledExecutable#__call__().
  DynamicTpuCompiledExecutable._symbol_to_input_loc: DynamicTpuCompiledExecutable#_symbol_to_input_loc.
  DynamicTpuCompiledExecutable._compile_bucket: DynamicTpuCompiledExecutable#_compile_bucket().
  DynamicTpuCompiledExecutable._get_model_inputs: DynamicTpuCompiledExecutable#_get_model_inputs().
  DynamicTpuCompiledExecutable.get_executable: DynamicTpuCompiledExecutable#get_executable().
  DynamicTpuCompiledExecutable._compute_output_shapes: DynamicTpuCompiledExecutable#_compute_output_shapes().
  DynamicTpuCompiledExecutable._symbol_bucket_uppers: DynamicTpuCompiledExecutable#_symbol_bucket_uppers.
  DynamicTpuCompiledExecutable._model_executables: DynamicTpuCompiledExecutable#_model_executables.
  DynamicTpuCompiledExecutable._compile_and_execute_pad_subgraph: DynamicTpuCompiledExecutable#_compile_and_execute_pad_subgraph().
  DynamicTpuCompiledExecutable._get_bucket_index: DynamicTpuCompiledExecutable#_get_bucket_index().
  DynamicTpuCompiledExecutable._bucket_specs: DynamicTpuCompiledExecutable#_bucket_specs.
  BucketCompilationSpec.symbol_bounds: BucketCompilationSpec#symbol_bounds.
  DynamicTpuCompiledExecutable._bucket_dynamic_tensor_bounds: DynamicTpuCompiledExecutable#_bucket_dynamic_tensor_bounds.
  DynamicTpuCompiledExecutable.__init__: DynamicTpuCompiledExecutable#__init__().
  DynamicTpuCompiledExecutable._promoted_scalar_output_indices: DynamicTpuCompiledExecutable#_promoted_scalar_output_indices.
  DynamicTpuCompiledExecutable._default_scalar_tensor_cache: DynamicTpuCompiledExecutable#_default_scalar_tensor_cache.
  BucketCompilationSpec: BucketCompilationSpec#
  DynamicTpuCompiledExecutable._num_lookahead_buckets: DynamicTpuCompiledExecutable#_num_lookahead_buckets.
  DynamicTpuCompiledExecutable._dynamic_outputs: DynamicTpuCompiledExecutable#_dynamic_outputs.
  DynamicTpuCompiledExecutable._get_backend_device: DynamicTpuCompiledExecutable#_get_backend_device().
  DynamicTpuCompiledExecutable._get_dynamic_input_tensors: DynamicTpuCompiledExecutable#_get_dynamic_input_tensors().
  DynamicTpuCompiledExecutable._dynamic_target_indices: DynamicTpuCompiledExecutable#_dynamic_target_indices.
  DynamicTpuCompiledExecutable._get_model_inputs_layouts: DynamicTpuCompiledExecutable#_get_model_inputs_layouts().
  DynamicTpuCompiledExecutable._convert_promoted_outputs_to_scalars: DynamicTpuCompiledExecutable#_convert_promoted_outputs_to_scalars().
  BucketCompilationSpec.model_input_bounds: BucketCompilationSpec#model_input_bounds.
  DynamicTpuCompiledExecutable: DynamicTpuCompiledExecutable#
  DynamicTpuCompiledExecutable._unique_output_indices: DynamicTpuCompiledExecutable#_unique_output_indices.
  DynamicTpuCompiledExecutable._backend_device: DynamicTpuCompiledExecutable#_backend_device.
  DynamicTpuCompiledExecutable._dynamic_tensor_map: DynamicTpuCompiledExecutable#_dynamic_tensor_map.
  DynamicTpuCompiledExecutable.updates_default_generator_state: DynamicTpuCompiledExecutable#updates_default_generator_state().
  BucketCompilationSpec.graph_module: BucketCompilationSpec#graph_module.
  BucketCompilationSpec.bounded_model_inputs: BucketCompilationSpec#bounded_model_inputs.
  DynamicTpuCompiledExecutable._static_compiler: DynamicTpuCompiledExecutable#_static_compiler.
  DynamicTpuCompiledExecutable._output_sym_shapes: DynamicTpuCompiledExecutable#_output_sym_shapes.
  DynamicTpuCompiledExecutable._view_arg_indices: DynamicTpuCompiledExecutable#_view_arg_indices.
  DynamicTpuCompiledExecutable._dynamic_input_indices: DynamicTpuCompiledExecutable#_dynamic_input_indices.
  DynamicTpuCompiledExecutable._static_tensor_map: DynamicTpuCompiledExecutable#_static_tensor_map.
  DynamicTpuCompiledExecutable._dynamic_scalar_map: DynamicTpuCompiledExecutable#_dynamic_scalar_map.
  DynamicTpuCompiledExecutable._static_scalar_map: DynamicTpuCompiledExecutable#_static_scalar_map.
  _TensorInfo: _TensorInfo#
  _TensorInfo.shape: _TensorInfo#shape.
  _TensorInfo.dtype: _TensorInfo#dtype.
  DynamicTpuCompiledExecutable._example_inputs: DynamicTpuCompiledExecutable#_example_inputs.
  DynamicTpuCompiledExecutable._is_fwd: DynamicTpuCompiledExecutable#_is_fwd.
  DynamicTpuCompiledExecutable._module_name: DynamicTpuCompiledExecutable#_module_name.
  DynamicTpuCompiledExecutable._use_pad_subgraph: DynamicTpuCompiledExecutable#_use_pad_subgraph.
  DynamicTpuCompiledExecutable._prepare_input_packing_plan: DynamicTpuCompiledExecutable#_prepare_input_packing_plan().
  DynamicTpuCompiledExecutable._model_inputs_template_length: DynamicTpuCompiledExecutable#_model_inputs_template_length.
  DynamicTpuCompiledExecutable.__reduce__: DynamicTpuCompiledExecutable#__reduce__().
---
# Module: [`src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py)

## Classes
### <a id="BucketCompilationSpec"></a>`BucketCompilationSpec`
- def: [`src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py:38`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L38)
- doc: Pre-transformed FX graph and bounded inputs for a single SymbolBounds bucket.
- signature: `class BucketCompilationSpec:`
- members:
  - <a id="BucketCompilationSpec.bounded_model_inputs"></a>`bounded_model_inputs` — [`L43`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L43)
  - <a id="BucketCompilationSpec.graph_module"></a>`graph_module` — [`L42`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L42)
  - <a id="BucketCompilationSpec.model_input_bounds"></a>`model_input_bounds` — [`L44`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L44)
  - <a id="BucketCompilationSpec.symbol_bounds"></a>`symbol_bounds` — [`L41`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L41) — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- uses (calls/refs, reference-scoped): [`SymbolBounds`](symbol_bounds.md#SymbolBounds)
- used by: [`__call__`](dynamic_executable.md#DynamicTpuCompiledExecutable.__call__), [`_compile_bucket`](dynamic_executable.md#DynamicTpuCompiledExecutable._compile_bucket), [`_prepare_bucket_spec`](dynamic_compiler.md#DynamicCompiler._prepare_bucket_spec), [`_symbol_bucket_uppers`](dynamic_executable.md#DynamicTpuCompiledExecutable._symbol_bucket_uppers), [`_get_bucket_index`](dynamic_executable.md#DynamicTpuCompiledExecutable._get_bucket_index), [`_bucket_dynamic_tensor_bounds`](dynamic_executable.md#DynamicTpuCompiledExecutable._bucket_dynamic_tensor_bounds), [`__init__`](dynamic_executable.md#DynamicTpuCompiledExecutable.__init__)

### <a id="DynamicTpuCompiledExecutable"></a>`DynamicTpuCompiledExecutable`
- def: [`src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py:59`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L59)
- doc: A callable wrapper for dynamic MLIR programs with TPU executable.
- signature: `class DynamicTpuCompiledExecutable(compiler.CompiledArtifact):`
- members:
  - <a id="DynamicTpuCompiledExecutable.__init__"></a>`__init__(self, static_compiler: compiler.StaticCompiler, example_inputs: Sequence[Any], bucket_specs: Sequence[BucketCompilationSpec], output_sym_shapes: Sequence[OutputSymShape], is_fwd: bool, view_arg_indices: set[int], use_pad_real_to_static: bool = True, module_name: str | None = None, num_lookahead_buckets: int | None = None)` — [`L62`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L62) — Initializes DynamicTpuCompiledExecutable.
  - <a id="DynamicTpuCompiledExecutable._compile_and_execute_pad_subgraph"></a>`_compile_and_execute_pad_subgraph(self, tensor_args: Sequence[torch.Tensor], bucket_idx: int)` — [`L151`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L151) — Compiles and executes the pad subgraph. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="DynamicTpuCompiledExecutable._compile_bucket"></a>`_compile_bucket(self, bucket_idx: int, argument_layouts: Sequence[Sequence[int]] | None = None)` — [`L417`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L417) — Compiles the pre-transformed FX graph for `bucket_idx` and `argument_layouts`. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="DynamicTpuCompiledExecutable._compute_output_shapes"></a>`_compute_output_shapes(self, args: Sequence[Any])` — [`L360`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L360) — Computes the runtime output shapes from symbolic shapes and arguments. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="DynamicTpuCompiledExecutable._convert_promoted_outputs_to_scalars"></a>`_convert_promoted_outputs_to_scalars(self, outputs: Any)` — [`L401`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L401) — Converts output tensors at promoted scalar positions back to Python scalars.
  - <a id="DynamicTpuCompiledExecutable._get_bucket_index"></a>`_get_bucket_index(self, args: Sequence[Any])` — [`L272`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L272) — Returns the index of the first SymbolBounds bucket that fits `args`. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="DynamicTpuCompiledExecutable._get_dynamic_input_tensors"></a>`_get_dynamic_input_tensors(self, args: Sequence[Any])` — [`L133`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L133) — Returns dynamic input tensors and validates they are on device.
  - <a id="DynamicTpuCompiledExecutable._get_model_inputs"></a>`_get_model_inputs(self, args: Sequence[Any], pad_outputs: Sequence[torch.Tensor])` — [`L296`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L296) — Assembles the actual runtime inputs for the model executable. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="DynamicTpuCompiledExecutable.get_executable"></a>`get_executable(self, layout_key: tuple[tuple[int, ...], ...], argument_layouts: Sequence[Sequence[int]] | None = None, bucket_idx: int = 0)` — [`L438`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L438) — Returns the resolved compiled executable for `(bucket_idx, layout_key)`, compiling if needed. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="DynamicTpuCompiledExecutable.updates_default_generator_state"></a>`updates_default_generator_state(self)` — [`L579`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L579)
- protocol/private: <a id="DynamicTpuCompiledExecutable.__call__"></a>`__call__`[`L515`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L515), <a id="DynamicTpuCompiledExecutable.__reduce__"></a>`__reduce__`[`L573`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L573), <a id="DynamicTpuCompiledExecutable._backend_device"></a>`_backend_device`[`L126`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L126), <a id="DynamicTpuCompiledExecutable._bucket_dynamic_tensor_bounds"></a>`_bucket_dynamic_tensor_bounds`[`L220`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L220), <a id="DynamicTpuCompiledExecutable._bucket_specs"></a>`_bucket_specs`[`L99`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L99), <a id="DynamicTpuCompiledExecutable._default_scalar_tensor_cache"></a>`_default_scalar_tensor_cache`[`L124`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L124), <a id="DynamicTpuCompiledExecutable._dynamic_input_indices"></a>`_dynamic_input_indices`[`L219`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L219), <a id="DynamicTpuCompiledExecutable._dynamic_outputs"></a>`_dynamic_outputs`[`L118`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L118), <a id="DynamicTpuCompiledExecutable._dynamic_scalar_map"></a>`_dynamic_scalar_map`[`L217`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L217), <a id="DynamicTpuCompiledExecutable._dynamic_target_indices"></a>`_dynamic_target_indices`[`L254`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L254), <a id="DynamicTpuCompiledExecutable._dynamic_tensor_map"></a>`_dynamic_tensor_map`[`L216`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L216), <a id="DynamicTpuCompiledExecutable._example_inputs"></a>`_example_inputs`[`L98`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L98), <a id="DynamicTpuCompiledExecutable._get_backend_device"></a>`_get_backend_device`[`L128`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L128), <a id="DynamicTpuCompiledExecutable._get_model_inputs_layouts"></a>`_get_model_inputs_layouts`[`L335`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L335), <a id="DynamicTpuCompiledExecutable._is_fwd"></a>`_is_fwd`[`L104`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L104), <a id="DynamicTpuCompiledExecutable._model_executables"></a>`_model_executables`[`L114`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L114), <a id="DynamicTpuCompiledExecutable._model_inputs_template_length"></a>`_model_inputs_template_length`[`L253`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L253), <a id="DynamicTpuCompiledExecutable._module_name"></a>`_module_name`[`L106`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L106), <a id="DynamicTpuCompiledExecutable._num_lookahead_buckets"></a>`_num_lookahead_buckets`[`L107`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L107), <a id="DynamicTpuCompiledExecutable._output_sym_shapes"></a>`_output_sym_shapes`[`L100`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L100), <a id="DynamicTpuCompiledExecutable._prepare_input_packing_plan"></a>`_prepare_input_packing_plan`[`L214`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L214), <a id="DynamicTpuCompiledExecutable._promoted_scalar_output_indices"></a>`_promoted_scalar_output_indices`[`L101`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L101), <a id="DynamicTpuCompiledExecutable._static_compiler"></a>`_static_compiler`[`L97`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L97), <a id="DynamicTpuCompiledExecutable._static_scalar_map"></a>`_static_scalar_map`[`L218`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L218), <a id="DynamicTpuCompiledExecutable._static_tensor_map"></a>`_static_tensor_map`[`L215`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L215), <a id="DynamicTpuCompiledExecutable._symbol_bucket_uppers"></a>`_symbol_bucket_uppers`[`L257`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L257), <a id="DynamicTpuCompiledExecutable._symbol_to_input_loc"></a>`_symbol_to_input_loc`[`L224`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L224), <a id="DynamicTpuCompiledExecutable._unique_output_indices"></a>`_unique_output_indices`[`L121`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L121), <a id="DynamicTpuCompiledExecutable._use_pad_subgraph"></a>`_use_pad_subgraph`[`L123`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L123), <a id="DynamicTpuCompiledExecutable._view_arg_indices"></a>`_view_arg_indices`[`L105`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L105)
- uses (calls/refs, reference-scoped): [`has_dynamic_shape`](sym_utils.md#has_dynamic_shape), [`symbol_bounds`](dynamic_executable.md#BucketCompilationSpec.symbol_bounds), [`OutputSymShape`](output_sym_shape.md#OutputSymShape), [`get_base_tensor`](view_decomposition.md#get_base_tensor), [`symbol_ranges`](symbol_bounds.md#SymbolBounds.symbol_ranges), [`BucketCompilationSpec`](dynamic_executable.md#BucketCompilationSpec), [`get_output_runtime_shape`](output_sym_shape.md#OutputSymShape.get_output_runtime_shape), [`is_dynamic`](output_sym_shape.md#OutputSymShape.is_dynamic), [`model_input_bounds`](dynamic_executable.md#BucketCompilationSpec.model_input_bounds), [`bounded_model_inputs`](dynamic_executable.md#BucketCompilationSpec.bounded_model_inputs), [`graph_module`](dynamic_executable.md#BucketCompilationSpec.graph_module), [`_TensorInfo`](dynamic_executable.md#_TensorInfo), [`dtype`](dynamic_executable.md#_TensorInfo.dtype), [`is_promoted_scalar`](output_sym_shape.md#OutputSymShape.is_promoted_scalar), [`is_tensor`](output_sym_shape.md#OutputSymShape.is_tensor), [`shape`](dynamic_executable.md#_TensorInfo.shape)
- used by: [`__call__`](dynamic_compiler.md#DynamicCompiler.__call__)

### <a id="_TensorInfo"></a>`_TensorInfo`  ·  implements/extends NamedTuple
- def: [`src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py:47`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L47)
- doc: Tensor information.
- signature: `class _TensorInfo(NamedTuple):`
- members:
  - <a id="_TensorInfo.dtype"></a>`dtype` — [`L56`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L56)
  - <a id="_TensorInfo.shape"></a>`shape` — [`L55`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/dynamic_executable.py#L55)
- used by: [`_compile_and_execute_pad_subgraph`](dynamic_executable.md#DynamicTpuCompiledExecutable._compile_and_execute_pad_subgraph)

