---
title: 'Module: torchtitan/experiments/graph_trainer/debug_utils.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/debug_utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.debug_utils`/
symbols:
  snapshot_graph: snapshot_graph().
  log_graph_diff: log_graph_diff().
  tlparse_log_graph_pass: tlparse_log_graph_pass().
  _get_node_target_name: _get_node_target_name().
---
# Module: [`torchtitan/experiments/graph_trainer/debug_utils.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/debug_utils.py)

## Functions
- <a id="_get_node_target_name"></a>`_get_node_target_name(node: torch.fx.Node)` — [`L15`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/debug_utils.py#L15) — Return a human-readable name for a node's target.
- <a id="log_graph_diff"></a>`log_graph_diff(before: dict, after: dict, pass_name: str)` — [`L51`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/debug_utils.py#L51) — Log a structured summary of what a graph pass changed.
- <a id="snapshot_graph"></a>`snapshot_graph(gm: torch.fx.GraphModule)` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/debug_utils.py#L25) — Capture a structural snapshot of a graph for comparison.
- <a id="tlparse_log_graph_pass"></a>`tlparse_log_graph_pass(gm: torch.fx.GraphModule, example_inputs: tuple | None = None, *, graph_name: str, debug: bool = False)` — [`L95`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/debug_utils.py#L95) — Log the transformed graph to tlparse via trace_structured.

