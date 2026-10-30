---
title: 'Module: src/torch_tpu/_internal/compile/fx_passes/propagate_symints.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/fx_passes/propagate_symints.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.fx_passes.propagate_symints`/
symbols:
  _collect_free_symbols: _collect_free_symbols().
  apply: apply().
---
# Module: [`src/torch_tpu/_internal/compile/fx_passes/propagate_symints.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/propagate_symints.py)

## Functions
- <a id="_collect_free_symbols"></a>`_collect_free_symbols(val: Any)` — [`L23`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/propagate_symints.py#L23) — Extracts free symbol string names from a SymInt or Tensor metadata. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="apply"></a>`apply(gm: torch.fx.GraphModule)` — [`L51`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/propagate_symints.py#L51) — Propagates SymInt placeholders to submodules that need them. — documented in [dynamic-shapes-compiler](../../../../../../concepts/dynamic-shapes-compiler.md)

