---
title: 'Module: src/torch_tpu/_internal/compile/dynamic/sym_utils.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/dynamic/sym_utils.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.dynamic.sym_utils`/
symbols:
  is_symint: is_symint().
  is_symint_node: is_symint_node().
  has_dynamic_shape: has_dynamic_shape().
  _sym_reduce: _sym_reduce().
  CUSTOM_SYMPY_FUNCS: CUSTOM_SYMPY_FUNCS.
  get_constant_symint_value: get_constant_symint_value().
  is_constant_symint: is_constant_symint().
  is_base_symbol_node: is_base_symbol_node().
  _sym_max: _sym_max().
  _sym_min: _sym_min().
  is_symexpr_node: is_symexpr_node().
  symexpr_to_aten: symexpr_to_aten().
  is_scalar: is_scalar().
  get_target_device: get_target_device().
  _ensure_tensor_proxy: _ensure_tensor_proxy().
  is_statically_equal: is_statically_equal().
  _get_tracer: _get_tracer().
  _get_target_dtype: _get_target_dtype().
  get_symint_hint: get_symint_hint().
---
# Module: [`src/torch_tpu/_internal/compile/dynamic/sym_utils.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py)

## Functions
- <a id="_ensure_tensor_proxy"></a>`_ensure_tensor_proxy(x: Any, tracer: torch.fx.Tracer, dtype: torch.dtype = torch.int32)` — [`L46`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L46)
- <a id="_get_target_dtype"></a>`_get_target_dtype(*args)` — [`L33`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L33)
- <a id="_get_tracer"></a>`_get_tracer(*args)` — [`L26`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L26)
- <a id="_sym_max"></a>`_sym_max(*args)` — [`L77`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L77)
- <a id="_sym_min"></a>`_sym_min(*args)` — [`L81`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L81)
- <a id="_sym_reduce"></a>`_sym_reduce(op: Any, *args)` — [`L63`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L63)
- <a id="get_constant_symint_value"></a>`get_constant_symint_value(val: Any)` — [`L139`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L139) — Extracts a concrete integer from a constant SymInt.
- <a id="get_symint_hint"></a>`get_symint_hint(val: Any)` — [`L152`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L152) — Returns the trace-time hint of an int, SymInt, or SymInt FX node.
- <a id="get_target_device"></a>`get_target_device(consumer_node: torch.fx.Node)` — [`L247`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L247) — Extracts target device from consumer node's input, graph, or kwargs.
- <a id="has_dynamic_shape"></a>`has_dynamic_shape(val: Any)` — [`L194`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L194) — Checks if a tensor, FX Node, or FakeTensor has any dynamic dimensions.
- <a id="is_base_symbol_node"></a>`is_base_symbol_node(node: torch.fx.Node)` — [`L235`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L235) — Checks if the FX node represents a raw base symbol variable token (e.g., s0).
- <a id="is_constant_symint"></a>`is_constant_symint(val: Any)` — [`L125`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L125) — Checks if a value represents a constant SymInt with no free symbols.
- <a id="is_scalar"></a>`is_scalar(val: Any)` — [`L187`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L187) — Checks if a value or FX node represents a Python scalar (int, float, bool).
- <a id="is_statically_equal"></a>`is_statically_equal(lhs: Any, rhs: Any)` — [`L171`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L171) — Returns whether lhs == rhs holds without installing a Dynamo guard.
- <a id="is_symexpr_node"></a>`is_symexpr_node(node: torch.fx.Node)` — [`L215`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L215) — Checks if the FX node represents a complex math expression (e.g., s0 + 1).
- <a id="is_symint"></a>`is_symint(val: Any)` — [`L111`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L111) — Checks if a value or FX node represents a symbolic integer (SymInt). — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- <a id="is_symint_node"></a>`is_symint_node(node: Any)` — [`L93`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L93) — Checks if the FX node evaluates to a symbolic integer (SymInt). — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- <a id="symexpr_to_aten"></a>`symexpr_to_aten(graph_module: torch.fx.GraphModule, consumer_node: torch.fx.Node, expr: sympy.Expr, symint_to_placeholder: Mapping[str, torch.fx.Node])` — [`L269`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L269) — Creates a chain of aten ops for a symexpr using lambdify and inserts them into the graph before the consumer node.

## Module values
- <a id="CUSTOM_SYMPY_FUNCS"></a>`CUSTOM_SYMPY_FUNCS` — [`L85`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_utils.py#L85)

