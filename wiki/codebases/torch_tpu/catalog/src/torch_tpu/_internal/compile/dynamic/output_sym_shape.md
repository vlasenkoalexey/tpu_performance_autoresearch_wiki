---
title: 'Module: src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.dynamic.output_sym_shape`/
symbols:
  OutputSymShape.from_output_node_meta_value: OutputSymShape#from_output_node_meta_value().
  create_output_sym_shapes: create_output_sym_shapes().
  OutputSymShape: OutputSymShape#
  OutputSymShape.__post_init__: OutputSymShape#__post_init__().
  OutputSymShape.get_output_runtime_shape: OutputSymShape#get_output_runtime_shape().
  OutputSymShape.extract_symbol_offsets: OutputSymShape#extract_symbol_offsets().
  OutputSymShape.output_sym_shape: OutputSymShape#output_sym_shape.
  OutputSymShape.is_dynamic: OutputSymShape#is_dynamic.
  OutputSymShape.is_tensor: OutputSymShape#is_tensor.
  OutputSymShape.is_promoted_scalar: OutputSymShape#is_promoted_scalar.
  _make_compiled_fn: _make_compiled_fn().
  _get_output_node_meta_val: _get_output_node_meta_val().
---
# Module: [`src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py)

## Classes
### <a id="OutputSymShape"></a>`OutputSymShape`
- def: [`src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py:31`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py#L31)
- doc: Information needed to compute the runtime shape of a dynamic output tensor.
- signature: `class OutputSymShape:`
- members:
  - <a id="OutputSymShape.extract_symbol_offsets"></a>`extract_symbol_offsets(self)` — [`L99`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py#L99) — Extracts non-negative constant offsets `c` from `s` or `s + c` output shape expressions.
  - <a id="OutputSymShape.from_output_node_meta_value"></a>`from_output_node_meta_value(cls, output_node_meta_value: Any, symint_to_tensor_dim: Mapping[str, tuple[int, int]])` — [`L151`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py#L151) — Creates output sym shape from output node's meta value. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="OutputSymShape.get_output_runtime_shape"></a>`get_output_runtime_shape(self, inputs: Sequence[torch.Tensor | int])` — [`L60`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py#L60) — Computes the runtime shape of the output tensor.
  - <a id="OutputSymShape.is_dynamic"></a>`is_dynamic` — [`L53`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py#L53)
  - <a id="OutputSymShape.is_promoted_scalar"></a>`is_promoted_scalar` — [`L52`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py#L52)
  - <a id="OutputSymShape.is_tensor"></a>`is_tensor` — [`L51`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py#L51)
  - <a id="OutputSymShape.output_sym_shape"></a>`output_sym_shape` — [`L50`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py#L50)
- protocol/private: <a id="OutputSymShape.__post_init__"></a>`__post_init__`[`L55`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py#L55)
- uses (calls/refs, reference-scoped): [`is_symint`](sym_utils.md#is_symint), [`CUSTOM_SYMPY_FUNCS`](sym_utils.md#CUSTOM_SYMPY_FUNCS), [`is_scalar`](sym_utils.md#is_scalar), [`_make_compiled_fn`](output_sym_shape.md#_make_compiled_fn)
- used by: [`get_bucketed_symbol_bounds`](sym_bounds_manager.md#SymBoundsManager.get_bucketed_symbol_bounds), [`_compute_output_shapes`](dynamic_executable.md#DynamicTpuCompiledExecutable._compute_output_shapes), [`create_output_sym_shapes`](output_sym_shape.md#create_output_sym_shapes), [`__init__`](dynamic_executable.md#DynamicTpuCompiledExecutable.__init__), [`_promoted_scalar_output_indices`](dynamic_executable.md#DynamicTpuCompiledExecutable._promoted_scalar_output_indices), [`_dynamic_outputs`](dynamic_executable.md#DynamicTpuCompiledExecutable._dynamic_outputs)

## Functions
- <a id="_get_output_node_meta_val"></a>`_get_output_node_meta_val(graph_module: torch.fx.GraphModule)` — [`L228`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py#L228) — Reads output node.meta['val'] from a graph.
- <a id="_make_compiled_fn"></a>`_make_compiled_fn(base_fn: Any, param_names: Sequence[str])` — [`L223`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py#L223) — Wraps a lambdified sympy expression to accept keyword arguments by name.
- <a id="create_output_sym_shapes"></a>`create_output_sym_shapes(graph_module: torch.fx.GraphModule, example_inputs: Sequence[torch.Tensor | int])` — [`L264`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/output_sym_shape.py#L264) — Creates symbolic shape specifications for all output tensors of the graph. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)

