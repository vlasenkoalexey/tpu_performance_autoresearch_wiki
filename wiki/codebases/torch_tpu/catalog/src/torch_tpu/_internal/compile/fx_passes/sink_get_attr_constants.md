---
title: 'Module: src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.fx_passes.sink_get_attr_constants`/
symbols:
  _sink_constants_for_submodule: _sink_constants_for_submodule().
  apply: apply().
  _get_sinkable_constant: _get_sinkable_constant().
  _map_call_module_nodes: _map_call_module_nodes().
  _get_placeholders: _get_placeholders().
  _replace_placeholder_with_get_attr: _replace_placeholder_with_get_attr().
  _erase_dead_get_attrs: _erase_dead_get_attrs().
---
# Module: [`src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.py`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.py)

## Functions
- <a id="_erase_dead_get_attrs"></a>`_erase_dead_get_attrs(gm: torch.fx.GraphModule)` — [`L156`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.py#L156) — Removes get_attr nodes that no longer have any users and deletes their attributes. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_get_placeholders"></a>`_get_placeholders(graph: torch.fx.Graph)` — [`L38`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.py#L38) — Returns the placeholder (input) nodes of a graph, in order.
- <a id="_get_sinkable_constant"></a>`_get_sinkable_constant(gm: torch.fx.GraphModule, arg: object)` — [`L43`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.py#L43) — Returns the (name, tensor) a call-site arg refers to, if it can be sunk. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_map_call_module_nodes"></a>`_map_call_module_nodes(gm: torch.fx.GraphModule)` — [`L22`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.py#L22) — Maps each submodule name to the call_module nodes that invoke it. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_replace_placeholder_with_get_attr"></a>`_replace_placeholder_with_get_attr(submod: torch.fx.GraphModule, placeholder: torch.fx.Node, attr_name: str, attr_val: torch.Tensor)` — [`L72`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.py#L72) — Registers a constant on a submodule and swaps its placeholder for get_attr. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="_sink_constants_for_submodule"></a>`_sink_constants_for_submodule(gm: torch.fx.GraphModule, submod: torch.fx.GraphModule, submod_name: str, call_site_nodes: list[torch.fx.Node])` — [`L91`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.py#L91) — Sinks the constant get_attr arguments shared by all calls to a submodule. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)
- <a id="apply"></a>`apply(gm: torch.fx.GraphModule)` — [`L169`](../../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/fx_passes/sink_get_attr_constants.py#L169) — Sinks get_attr arguments from root module into child submodules. — documented in [fx-graph-passes](../../../../../../concepts/fx-graph-passes.md)

