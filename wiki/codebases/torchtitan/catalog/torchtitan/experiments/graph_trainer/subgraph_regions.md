---
title: 'Module: torchtitan/experiments/graph_trainer/subgraph_regions.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/subgraph_regions.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.subgraph_regions`/
symbols:
  apply_subgraph_region_annotations_pass: apply_subgraph_region_annotations_pass().
  mark_invoke_subgraph: mark_invoke_subgraph().
  _meta_value_key: _meta_value_key().
  SUBGRAPH_REGION: SUBGRAPH_REGION.
  subgraph_region_key: subgraph_region_key().
  subgraph: subgraph().
  _SUBGRAPH_REGION_CUSTOM_KEYS: _SUBGRAPH_REGION_CUSTOM_KEYS.
  _arg_key: _arg_key().
  _subgraph_structural_key: _subgraph_structural_key().
  SUBGRAPH_REGION_ROLE: SUBGRAPH_REGION_ROLE.
  mark_invoke_subgraph.make_input_replacement: mark_invoke_subgraph().make_input_replacement().
  collect_subgraph_region_groups: collect_subgraph_region_groups().
  _strip_subgraph_arg_annotations: _strip_subgraph_arg_annotations().
  _custom_key: _custom_key().
  _node_meta_key: _node_meta_key().
  mark_invoke_subgraph.add_boundary_arg: mark_invoke_subgraph().add_boundary_arg().
  SUBGRAPH_REGION_PRESERVE_ORDER: SUBGRAPH_REGION_PRESERVE_ORDER.
  _has_graph_module_arg: _has_graph_module_arg().
  _record_subgraph_region: _record_subgraph_region().
  collect_subgraph_region_groups.flush: collect_subgraph_region_groups().flush().
  _getattr_or_none: _getattr_or_none().
  _strip_custom_keys_from_meta: _strip_custom_keys_from_meta().
  _copy_placeholder_meta: _copy_placeholder_meta().
  _target_key: _target_key().
  _reuse_subgraph_module: _reuse_subgraph_module().
  mark_invoke_subgraph.collect_external_input: mark_invoke_subgraph().collect_external_input().
  mark_invoke_subgraph.load_arg: mark_invoke_subgraph().load_arg().
  mark_invoke_subgraph.make_outer_arg: mark_invoke_subgraph().make_outer_arg().
---
# Module: [`torchtitan/experiments/graph_trainer/subgraph_regions.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py)

## Functions
- <a id="_arg_key"></a>`_arg_key(value, node_indices)` — [`L245`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L245)
- <a id="_copy_placeholder_meta"></a>`_copy_placeholder_meta(placeholder: fx.Node, input_node: fx.Node, owning_module: fx.GraphModule)` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L165)
- <a id="_custom_key"></a>`_custom_key(custom)` — [`L268`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L268)
- <a id="_getattr_or_none"></a>`_getattr_or_none(module: torch.fx.GraphModule, target: str)` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L74)
- <a id="_has_graph_module_arg"></a>`_has_graph_module_arg(node: Node)` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L84)
- <a id="_meta_value_key"></a>`_meta_value_key(value)` — [`L222`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L222)
- <a id="_node_meta_key"></a>`_node_meta_key(node)` — [`L280`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L280)
- <a id="_record_subgraph_region"></a>`_record_subgraph_region(module: torch.fx.GraphModule, region_node: Node, region: str, region_id: str, region_role: str, preserve_order: bool)` — [`L524`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L524)
- <a id="_reuse_subgraph_module"></a>`_reuse_subgraph_module(module, region_node, canonical_target)` — [`L307`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L307)
- <a id="_strip_custom_keys_from_meta"></a>`_strip_custom_keys_from_meta(meta: dict[str, Any], keys: tuple[str, ...])` — [`L174`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L174)
- <a id="_strip_subgraph_arg_annotations"></a>`_strip_subgraph_arg_annotations(module: torch.fx.GraphModule, nodes: list[Node], keys: tuple[str, ...])` — [`L197`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L197)
- <a id="_subgraph_structural_key"></a>`_subgraph_structural_key(gm)` — [`L293`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L293)
- <a id="_target_key"></a>`_target_key(target)` — [`L216`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L216)
- <a id="mark_invoke_subgraph.add_boundary_arg"></a>`add_boundary_arg(input_node: fx.Node, path: tuple[int, ...], meta_val: Any)` — [`L400`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L400)
- <a id="apply_subgraph_region_annotations_pass"></a>`apply_subgraph_region_annotations_pass(gm: torch.fx.GraphModule, example_inputs: tuple | None = None)` — [`L573`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L573)
- <a id="mark_invoke_subgraph.collect_external_input"></a>`collect_external_input(node: fx.Node)` — [`L362`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L362)
- <a id="collect_subgraph_region_groups"></a>`collect_subgraph_region_groups(graph: torch.fx.Graph)` — [`L136`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L136)
- <a id="collect_subgraph_region_groups.flush"></a>`flush()` — [`L143`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L143)
- <a id="mark_invoke_subgraph.load_arg"></a>`load_arg(node: fx.Node)` — [`L427`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L427)
- <a id="mark_invoke_subgraph.make_input_replacement"></a>`make_input_replacement(input_node: fx.Node, value: Any, path: tuple[int, ...] = ())` — [`L410`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L410)
- <a id="mark_invoke_subgraph.make_outer_arg"></a>`make_outer_arg(input_node: fx.Node, path: tuple[int, ...], meta_val: Any)` — [`L466`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L466)
- <a id="mark_invoke_subgraph"></a>`mark_invoke_subgraph(graph: fx.Graph, nodes: list[fx.Node], *, region_name_prefix: str)` — [`L326`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L326) — Outline FX nodes into an invoke_subgraph HOP and return the HOP node.
- <a id="subgraph"></a>`subgraph(name: str | None, role: str | None = None, *, preserve_order: bool = False)` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L30) — Mark operations for outlining as explicit ``invoke_subgraph`` regions.
- <a id="subgraph_region_key"></a>`subgraph_region_key(node: Node)` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L96)

## Module values
- <a id="SUBGRAPH_REGION"></a>`SUBGRAPH_REGION` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L20)
- <a id="SUBGRAPH_REGION_PRESERVE_ORDER"></a>`SUBGRAPH_REGION_PRESERVE_ORDER` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L22)
- <a id="SUBGRAPH_REGION_ROLE"></a>`SUBGRAPH_REGION_ROLE` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L21)
- <a id="_SUBGRAPH_REGION_CUSTOM_KEYS"></a>`_SUBGRAPH_REGION_CUSTOM_KEYS` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/subgraph_regions.py#L23)

