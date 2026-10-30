---
title: 'Module: src/torch_tpu/_internal/compile/fx_passes/mark_embedded_constants.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/fx_passes/mark_embedded_constants.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.fx_passes.mark_embedded_constants`/
symbols:
  apply: apply().
---
# Module: [`src/torch_tpu/_internal/compile/fx_passes/mark_embedded_constants.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/mark_embedded_constants.py)

## Functions
- <a id="apply"></a>`apply(gm_or_graph: torch.fx.GraphModule | torch.fx.Graph)` — [`L24`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/mark_embedded_constants.py#L24) — Marks embedded constants (get_attr node targets) in an FX graph so that they may be properly handled during MLIR generation. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)

