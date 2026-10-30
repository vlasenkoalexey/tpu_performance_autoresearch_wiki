---
title: 'Module: src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.fx_passes.clone_mutated_returned_placeholders`/
symbols:
  apply: apply().
  _find_placeholders_to_clone: _find_placeholders_to_clone().
  _normalize_gm_and_graph: _normalize_gm_and_graph().
  _get_output_node: _get_output_node().
  _get_returned_nodes: _get_returned_nodes().
  _is_returned_compute_placeholder: _is_returned_compute_placeholder().
  _clone_and_replace_placeholder: _clone_and_replace_placeholder().
---
# Module: [`src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.py)

## Functions
- <a id="_clone_and_replace_placeholder"></a>`_clone_and_replace_placeholder(graph: torch.fx.Graph, placeholder: torch.fx.Node)` — [`L71`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.py#L71) — Clones a placeholder and redirects all downstream uses to the clone. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_find_placeholders_to_clone"></a>`_find_placeholders_to_clone(graph: torch.fx.Graph, returned_nodes: set[torch.fx.Node])` — [`L59`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.py#L59) — Identifies all placeholder nodes that need cloning. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_get_output_node"></a>`_get_output_node(graph: torch.fx.Graph)` — [`L29`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.py#L29) — Finds and validates that the graph has at most one output node. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_get_returned_nodes"></a>`_get_returned_nodes(output_node: torch.fx.Node)` — [`L41`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.py#L41) — Extracts all FX nodes returned by the output node. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_is_returned_compute_placeholder"></a>`_is_returned_compute_placeholder(node: torch.fx.Node, returned_nodes: set[torch.fx.Node])` — [`L47`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.py#L47) — Checks if a node is a torch.Tensor output placeholder consumed by compute operations. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_normalize_gm_and_graph"></a>`_normalize_gm_and_graph(gm_or_graph: torch.fx.GraphModule | torch.fx.Graph)` — [`L20`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.py#L20) — Extracts the owning GraphModule (if any) and the Graph.
- <a id="apply"></a>`apply(gm_or_graph: torch.fx.GraphModule | torch.fx.Graph)` — [`L88`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/clone_mutated_returned_placeholders.py#L88) — Clones placeholder nodes that are returned in the output and used in compute. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)

