---
title: 'Module: src/torch_tpu/_internal/compile/fx_passes/force_collectives_output.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/fx_passes/force_collectives_output.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.fx_passes.force_collectives_output`/
symbols:
  apply: apply().
  _mark_live: _mark_live().
  _is_collective_or_wait: _is_collective_or_wait().
---
# Module: [`src/torch_tpu/_internal/compile/fx_passes/force_collectives_output.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/force_collectives_output.py)

## Functions
- <a id="_is_collective_or_wait"></a>`_is_collective_or_wait(node: torch.fx.Node)` — [`L23`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/force_collectives_output.py#L23) — Returns True if the node is a collective or a wait_tensor. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_mark_live"></a>`_mark_live(node: torch.fx.Node, live: set[torch.fx.Node])` — [`L34`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/force_collectives_output.py#L34) — Adds the node and everything it transitively depends on to `live`. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="apply"></a>`apply(gm: torch.fx.GraphModule)` — [`L45`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/force_collectives_output.py#L45) — Forces all is_collective submodules to output their collective results. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)

