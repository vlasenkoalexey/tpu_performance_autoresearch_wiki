---
title: 'Module: src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.dynamic.symbol_bounds`/
symbols:
  SymbolBounds: SymbolBounds#
  SymbolBounds.get_upper_bound: SymbolBounds#get_upper_bound().
  _is_valid_bound: _is_valid_bound().
  SymbolBounds._symbol_ranges: SymbolBounds#_symbol_ranges.
  SymbolBounds.get_symint_bounds: SymbolBounds#get_symint_bounds().
  SymbolBounds.__repr__: SymbolBounds#__repr__().
  SymbolBounds.merge_bounds: SymbolBounds#merge_bounds().
  SymbolBounds.symbol_ranges: SymbolBounds#symbol_ranges().
  get_symint_bounds: get_symint_bounds().
  _lookup_bounds_in_shape_env: _lookup_bounds_in_shape_env().
  SymbolBounds.__init__: SymbolBounds#__init__().
  find_violated_guard: find_violated_guard().
  get_fallback_upper_bound: get_fallback_upper_bound().
  SymbolBounds._sym_sort_key: SymbolBounds#_sym_sort_key().
---
# Module: [`src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py)

## Classes
### <a id="SymbolBounds"></a>`SymbolBounds`
- def: [`src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py:218`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L218) — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- doc: Holds lower and upper bounds for atomic symbols and evaluates symbolic expressions.
- signature: `class SymbolBounds:`
- members:
  - <a id="SymbolBounds.get_symint_bounds"></a>`get_symint_bounds(self, sym_int: torch.SymInt)` — [`L274`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L274) — Gets lower and upper bounds for a given SymInt or symbolic expression.
  - <a id="SymbolBounds.get_upper_bound"></a>`get_upper_bound(self, val: Any)` — [`L296`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L296) — Gets the upper bound for an int, SymInt, or SymInt FX node. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="SymbolBounds.merge_bounds"></a>`merge_bounds(cls, bounds_seq: Sequence[SymbolBounds])` — [`L258`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L258) — Returns a SymbolBounds spanning the union of ranges across `bounds_seq`. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="SymbolBounds.symbol_ranges"></a>`symbol_ranges(self)` — [`L229`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L229)
- protocol/private: <a id="SymbolBounds.__init__"></a>`__init__`[`L223`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L223), <a id="SymbolBounds.__repr__"></a>`__repr__`[`L234`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L234), <a id="SymbolBounds._sym_sort_key"></a>`_sym_sort_key`[`L235`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L235), <a id="SymbolBounds._symbol_ranges"></a>`_symbol_ranges`[`L221`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L221)
- uses (calls/refs, reference-scoped): [`is_symint`](sym_utils.md#is_symint), [`is_symint_node`](sym_utils.md#is_symint_node), [`_is_valid_bound`](symbol_bounds.md#_is_valid_bound)
- used by: [`__call__`](dynamic_compiler.md#DynamicCompiler.__call__), [`apply_dynamism_transformations`](graph_transformations.md#apply_dynamism_transformations), [`_prepare_bucket_spec`](dynamic_compiler.md#DynamicCompiler._prepare_bucket_spec), [`get_upper_bound`](graph_transform_context.md#GraphTransformContext.get_upper_bound), [`get_bucketed_symbol_bounds`](sym_bounds_manager.md#SymBoundsManager.get_bucketed_symbol_bounds), [`get_fallback_symbol_bounds`](sym_bounds_manager.md#SymBoundsManager.get_fallback_symbol_bounds), [`_symbol_bucket_uppers`](dynamic_executable.md#DynamicTpuCompiledExecutable._symbol_bucket_uppers), [`add_bound_checks`](sym_bounds_manager.md#SymBoundsManager.add_bound_checks), [`_create_bounded_model_inputs`](dynamic_compiler.md#_create_bounded_model_inputs), [`symbol_bounds`](dynamic_executable.md#BucketCompilationSpec.symbol_bounds), [`get_symint_bounds`](graph_transform_context.md#GraphTransformContext.get_symint_bounds), [`__init__`](graph_transform_context.md#GraphTransformContext.__init__)

## Functions
- <a id="_is_valid_bound"></a>`_is_valid_bound(s: sympy.Expr)` — [`L29`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L29)
- <a id="_lookup_bounds_in_shape_env"></a>`_lookup_bounds_in_shape_env(expr: sympy.Expr, shape_env)` — [`L33`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L33) — Queries the shape environment using all available lookups and math solvers.
- <a id="find_violated_guard"></a>`find_violated_guard(shape_env: Any, upper_bounds: Mapping[str, int])` — [`L95`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L95) — Checks whether the assignment of symbol upper bounds satisfies active shape guards.
- <a id="get_fallback_upper_bound"></a>`get_fallback_upper_bound(lower_bound: int)` — [`L90`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L90) — Computes the fallback upper bound when candidate bounds violate shape guards.
- <a id="get_symint_bounds"></a>`get_symint_bounds(sym_int: torch.SymInt)` — [`L176`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/symbol_bounds.py#L176) — Gets lower and upper bounds for a given SymInt, evaluating expressions if needed.

