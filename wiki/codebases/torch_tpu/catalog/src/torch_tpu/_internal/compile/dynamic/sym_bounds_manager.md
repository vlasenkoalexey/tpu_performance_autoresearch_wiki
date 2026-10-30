---
title: 'Module: src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.dynamic.sym_bounds_manager`/SymBoundsManager#
symbols:
  SymBoundsManager.get_bucketed_symbol_bounds: get_bucketed_symbol_bounds().
  SymBoundsManager.get_fallback_symbol_bounds: get_fallback_symbol_bounds().
  SymBoundsManager.add_bound_checks: add_bound_checks().
  SymBoundsManager._atomic_symints: _atomic_symints.
  SymBoundsManager.__init__: __init__().
  SymBoundsManager._populate_atomic_symbols: _populate_atomic_symbols().
  SymBoundsManager: ''
---
# Module: [`src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py)

## Classes
### <a id="SymBoundsManager"></a>`SymBoundsManager`
- def: [`src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py:32`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py#L32)
- doc: Manages lower and upper bounds for dynamic SymInts.
- signature: `class SymBoundsManager:`
- members:
  - <a id="SymBoundsManager._populate_atomic_symbols"></a>`_populate_atomic_symbols(self, example_inputs: Sequence[InputType])` — [`L228`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py#L228) — Populates atomic SymInts from inputs.
  - <a id="SymBoundsManager.add_bound_checks"></a>`add_bound_checks(self, bounds: symbol_bounds.SymbolBounds | Sequence[symbol_bounds.SymbolBounds])` — [`L265`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py#L265) — Adds bound checks for all SymInts in the graph across the given bounds. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="SymBoundsManager.get_bucketed_symbol_bounds"></a>`get_bucketed_symbol_bounds(self, output_sym_shapes: Sequence[output_sym_shape.OutputSymShape], num_buckets: int = 1, bucket_step: int = 128)` — [`L75`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py#L75) — Computes a sequence of bucketed SymbolBounds using 128k - c alignment. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
  - <a id="SymBoundsManager.get_fallback_symbol_bounds"></a>`get_fallback_symbol_bounds(self)` — [`L41`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py#L41) — Computes and validates a single SymbolBounds using explicit or fallback bounds. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)
- protocol/private: <a id="SymBoundsManager.__init__"></a>`__init__`[`L37`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py#L37), <a id="SymBoundsManager._atomic_symints"></a>`_atomic_symints`[`L35`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/dynamic/sym_bounds_manager.py#L35)
- uses (calls/refs, reference-scoped): [`SymbolBounds`](symbol_bounds.md#SymbolBounds), [`get_symint_bounds`](symbol_bounds.md#SymbolBounds.get_symint_bounds), [`merge_bounds`](symbol_bounds.md#SymbolBounds.merge_bounds), [`OutputSymShape`](output_sym_shape.md#OutputSymShape), [`get_symint_bounds`](symbol_bounds.md#get_symint_bounds), [`extract_symbol_offsets`](output_sym_shape.md#OutputSymShape.extract_symbol_offsets), [`find_violated_guard`](symbol_bounds.md#find_violated_guard), [`get_fallback_upper_bound`](symbol_bounds.md#get_fallback_upper_bound)
- used by: [`__call__`](dynamic_compiler.md#DynamicCompiler.__call__)

