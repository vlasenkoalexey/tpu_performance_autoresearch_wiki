---
title: 'Module: torchtitan/experiments/graph_trainer/graph_pp/utils.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/graph_pp/utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.graph_pp.utils`/
symbols:
  _MetaShapeEnvTransfer._copy_value: _MetaShapeEnvTransfer#_copy_value().
  graph_pp_value_spec: graph_pp_value_spec().
  output_names: output_names().
  trace_graph_pp_graph: trace_graph_pp_graph().
  flatten_graph_values: flatten_graph_values().
  unique_in_order: unique_in_order().
  GraphPPValueSpec.wrap_flat_values: GraphPPValueSpec#wrap_flat_values().
  _MetaShapeEnvTransfer.dst_shape_env: _MetaShapeEnvTransfer#dst_shape_env.
  _MetaShapeEnvTransfer.collect: _MetaShapeEnvTransfer#collect().
  GraphPPValueSpec.num_flat_values: GraphPPValueSpec#num_flat_values().
  _MetaShapeEnvTransfer.copy_meta: _MetaShapeEnvTransfer#copy_meta().
  placeholder_names: placeholder_names().
  _MetaShapeEnvTransfer.seed: _MetaShapeEnvTransfer#seed().
  _wrap_unwrapped_values: _wrap_unwrapped_values().
  _iter_meta_leaves: _iter_meta_leaves().
  normalize_graph_pp_microbatch_inputs: normalize_graph_pp_microbatch_inputs().
  _MetaShapeEnvTransfer._collect_symint: _MetaShapeEnvTransfer#_collect_symint().
  _num_unwrapped_values: _num_unwrapped_values().
  _MetaShapeEnvTransfer._collect_fake_tensor: _MetaShapeEnvTransfer#_collect_fake_tensor().
  _MetaShapeEnvTransfer._copy_symint: _MetaShapeEnvTransfer#_copy_symint().
  _MetaShapeEnvTransfer._copy_sympy_expr: _MetaShapeEnvTransfer#_copy_sympy_expr().
  node_closure: node_closure().
  is_mutation_node: is_mutation_node().
  GraphPPValueSpec: GraphPPValueSpec#
  GraphPPValueSpec.unflatten: GraphPPValueSpec#unflatten().
  placeholder_dependencies: placeholder_dependencies().
  GraphPPValueSpec.layouts: GraphPPValueSpec#layouts.
  _MetaShapeEnvTransfer.dst_fake_mode: _MetaShapeEnvTransfer#dst_fake_mode.
  _find_fake_mode: _find_fake_mode().
  normalize_graph_pp_microbatch_inputs.normalize_tree: normalize_graph_pp_microbatch_inputs().normalize_tree().
  _MetaShapeEnvTransfer._symbol_sources: _MetaShapeEnvTransfer#_symbol_sources.
  graph_outputs: graph_outputs().
  overlap_fw_bw_sub_actions: overlap_fw_bw_sub_actions().
  _MetaShapeEnvTransfer._copy_fake_tensor: _MetaShapeEnvTransfer#_copy_fake_tensor().
  graph_module_outputs: graph_module_outputs().
  _subclass_layout_slice: _subclass_layout_slice().
  _graphable_split_block_mask: _graphable_split_block_mask().
  normalize_graph_pp_microbatch_inputs.normalize_leaf: normalize_graph_pp_microbatch_inputs().normalize_leaf().
  _MetaShapeEnvTransfer._source: _MetaShapeEnvTransfer#_source().
  node_order: node_order().
  allow_fx_graph_extraction_of_side_effectful_ops: allow_fx_graph_extraction_of_side_effectful_ops().
  GraphPPValueSpec.num_values: GraphPPValueSpec#num_values.
  GraphPPValueSpec.tree_spec: GraphPPValueSpec#tree_spec.
  T: T.
  _MetaShapeEnvTransfer: _MetaShapeEnvTransfer#
  is_getitem_node: is_getitem_node().
  base_tensor_for_mutation_target: base_tensor_for_mutation_target().
  is_fake_tensor_node: is_fake_tensor_node().
  rename_placeholder: rename_placeholder().
  example_inputs_from_placeholders: example_inputs_from_placeholders().
  _UNSUPPORTED_SYMBOLIC_META_TYPES._UNSUPPORTED_SYMBOLIC_META_TYPES: _UNSUPPORTED_SYMBOLIC_META_TYPES._UNSUPPORTED_SYMBOLIC_META_TYPES.
  _value_name: _value_name().
  _graphable_split_block_mask.graphable_mask_mod: _graphable_split_block_mask().graphable_mask_mod().
  _MetaShapeEnvTransfer.__init__: _MetaShapeEnvTransfer#__init__().
---
# Module: [`torchtitan/experiments/graph_trainer/graph_pp/utils.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py)

## Classes
### <a id="GraphPPValueSpec"></a>`GraphPPValueSpec`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/utils.py:466`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L466)
- doc: Subclass/tree metadata for one semantic slice of a flat GraphPP API.
- signature: `class GraphPPValueSpec:`
- members:
  - <a id="GraphPPValueSpec.num_flat_values"></a>`num_flat_values(self)` — [`L479`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L479)
  - <a id="GraphPPValueSpec.unflatten"></a>`unflatten(self, values: tuple[Any, ...] | list[Any])` — [`L489`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L489)
  - <a id="GraphPPValueSpec.wrap_flat_values"></a>`wrap_flat_values(self, values: tuple[Any, ...] | list[Any])` — [`L482`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L482)
  - <a id="GraphPPValueSpec.layouts"></a>`layouts` — [`L475`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L475)
  - <a id="GraphPPValueSpec.num_values"></a>`num_values` — [`L474`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L474)
  - <a id="GraphPPValueSpec.tree_spec"></a>`tree_spec` — [`L476`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L476)
- uses (calls/refs, reference-scoped): [`SubclassLayout`](../make_fx_tracer.md#SubclassLayout), [`_wrap_unwrapped_values`](utils.md#_wrap_unwrapped_values), [`_num_unwrapped_values`](utils.md#_num_unwrapped_values)
- used by: [`_build_stage_graphs`](graph_builder.md#_build_stage_graphs), [`backward_input`](graph_builder.md#GraphTrainerStageGraphs.backward_input), [`graph_pp_value_spec`](utils.md#graph_pp_value_spec), [`_split_forward_outputs`](graph_builder.md#GraphTrainerStageGraphs._split_forward_outputs), [`_split_full_backward_outputs`](graph_builder.md#GraphTrainerStageGraphs._split_full_backward_outputs), [`param_grads_for_accumulation`](graph_builder.md#GraphTrainerStageGraphs.param_grads_for_accumulation), [`input_grad_values`](graph_builder.md#_StageGraphMeta.input_grad_values), [`fwd_output_values`](graph_builder.md#_StageGraphMeta.fwd_output_values), [`param_grad_values`](graph_builder.md#_StageGraphMeta.param_grad_values)

### <a id="_MetaShapeEnvTransfer"></a>`_MetaShapeEnvTransfer`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/utils.py:96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L96)
- doc: Move copied FX metadata into a destination ShapeEnv.
- signature: `class _MetaShapeEnvTransfer:`
- members:
  - <a id="_MetaShapeEnvTransfer.collect"></a>`collect(self, meta: dict[str, Any])` — [`L122`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L122)
  - <a id="_MetaShapeEnvTransfer.copy_meta"></a>`copy_meta(self, meta: dict[str, Any])` — [`L146`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L146)
  - <a id="_MetaShapeEnvTransfer.seed"></a>`seed(self)` — [`L131`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L131)
  - <a id="_MetaShapeEnvTransfer.dst_fake_mode"></a>`dst_fake_mode` — [`L118`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L118)
  - <a id="_MetaShapeEnvTransfer.dst_shape_env"></a>`dst_shape_env` — [`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L119)
- protocol/private: <a id="_MetaShapeEnvTransfer.__init__"></a>`__init__`[`L117`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L117), <a id="_MetaShapeEnvTransfer._collect_fake_tensor"></a>`_collect_fake_tensor`[`L155`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L155), <a id="_MetaShapeEnvTransfer._collect_symint"></a>`_collect_symint`[`L162`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L162), <a id="_MetaShapeEnvTransfer._copy_fake_tensor"></a>`_copy_fake_tensor`[`L214`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L214), <a id="_MetaShapeEnvTransfer._copy_symint"></a>`_copy_symint`[`L227`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L227), <a id="_MetaShapeEnvTransfer._copy_sympy_expr"></a>`_copy_sympy_expr`[`L247`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L247), <a id="_MetaShapeEnvTransfer._copy_value"></a>`_copy_value`[`L180`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L180), <a id="_MetaShapeEnvTransfer._source"></a>`_source`[`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L151), <a id="_MetaShapeEnvTransfer._symbol_sources"></a>`_symbol_sources`[`L120`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L120)
- uses (calls/refs, reference-scoped): [`_iter_meta_leaves`](utils.md#_iter_meta_leaves), [`_UNSUPPORTED_SYMBOLIC_META_TYPES`](utils.md#_UNSUPPORTED_SYMBOLIC_META_TYPES._UNSUPPORTED_SYMBOLIC_META_TYPES)
- used by: [`multiplex_fw_bw_graph`](graph_multiplex.md#multiplex_fw_bw_graph)

## Functions
- <a id="_find_fake_mode"></a>`_find_fake_mode(gm: fx.GraphModule)` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L85) — Return the first FakeTensorMode referenced by graph node metadata.
- <a id="_graphable_split_block_mask"></a>`_graphable_split_block_mask(block_mask: BlockMask)` — [`L531`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L531) — Make a PyTorch PP-split BlockMask replayable by one traced graph.
- <a id="_iter_meta_leaves"></a>`_iter_meta_leaves(value: Any)` — [`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L73)
- <a id="_num_unwrapped_values"></a>`_num_unwrapped_values(num_values: int, layouts: dict[int, SubclassLayout])` — [`L455`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L455)
- <a id="_subclass_layout_slice"></a>`_subclass_layout_slice(layouts: dict[int, SubclassLayout], *, start: int, count: int)` — [`L442`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L442)
- <a id="_value_name"></a>`_value_name(value: Any, index: int)` — [`L280`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L280)
- <a id="_wrap_unwrapped_values"></a>`_wrap_unwrapped_values(values: tuple[Any, ...] | list[Any], *, num_values: int, layouts: dict[int, SubclassLayout])` — [`L515`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L515)
- <a id="allow_fx_graph_extraction_of_side_effectful_ops"></a>`allow_fx_graph_extraction_of_side_effectful_ops(exclude_vals: set[object])` — [`L410`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L410) — Temporarily allow FX graph extraction to copy selected side-effect ops.
- <a id="base_tensor_for_mutation_target"></a>`base_tensor_for_mutation_target(value: object)` — [`L357`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L357) — Return the placeholder/intermediate base reached through view nodes.
- <a id="example_inputs_from_placeholders"></a>`example_inputs_from_placeholders(gm: fx.GraphModule)` — [`L395`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L395) — Read fake/example values from placeholder metadata.
- <a id="flatten_graph_values"></a>`flatten_graph_values(values: list[Any])` — [`L510`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L510)
- <a id="graph_module_outputs"></a>`graph_module_outputs(gm: fx.GraphModule)` — [`L274`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L274) — Return flattened output values from ``gm``.
- <a id="graph_outputs"></a>`graph_outputs(graph: fx.Graph)` — [`L265`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L265) — Return the flattened values from the graph's single output node.
- <a id="graph_pp_value_spec"></a>`graph_pp_value_spec(layouts: dict[int, SubclassLayout], *, start: int, count: int, tree_spec: pytree.TreeSpec | None = None)` — [`L496`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L496)
- <a id="_graphable_split_block_mask.graphable_mask_mod"></a>`graphable_mask_mod(b: torch.Tensor, h: torch.Tensor, q_idx: torch.Tensor, kv_idx: torch.Tensor)` — [`L575`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L575)
- <a id="is_fake_tensor_node"></a>`is_fake_tensor_node(node: fx.Node)` — [`L375`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L375)
- <a id="is_getitem_node"></a>`is_getitem_node(node: fx.Node)` — [`L337`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L337)
- <a id="is_mutation_node"></a>`is_mutation_node(node: fx.Node)` — [`L341`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L341) — Return whether ``node`` writes to one of its aliased arguments.
- <a id="node_closure"></a>`node_closure(values: Iterable[object])` — [`L301`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L301) — Return all FX nodes needed to compute ``values``.
- <a id="node_order"></a>`node_order(graph: fx.Graph)` — [`L325`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L325) — Map each node in ``graph`` to its topological position.
- <a id="normalize_graph_pp_microbatch_inputs"></a>`normalize_graph_pp_microbatch_inputs(args_split: list[Any], kwargs_split: list[Any])` — [`L591`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L591) — Normalize PP-split inputs so one GraphPP trace can replay all microbatches.
- <a id="normalize_graph_pp_microbatch_inputs.normalize_leaf"></a>`normalize_leaf(value: Any)` — [`L602`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L602)
- <a id="normalize_graph_pp_microbatch_inputs.normalize_tree"></a>`normalize_tree(value: Any)` — [`L607`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L607)
- <a id="output_names"></a>`output_names(gm: fx.GraphModule)` — [`L292`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L292) — Return stable names for flattened graph outputs.
- <a id="overlap_fw_bw_sub_actions"></a>`overlap_fw_bw_sub_actions(action: _Action)` — [`L422`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L422) — Validate an ``OVERLAP_F_B`` action and return ``(fw_action, bw_action)``.
- <a id="placeholder_dependencies"></a>`placeholder_dependencies(values: Iterable[object])` — [`L319`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L319) — Return placeholder nodes in the dependency closure of ``values``.
- <a id="placeholder_names"></a>`placeholder_names(gm: fx.GraphModule)` — [`L286`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L286) — Return graph placeholder names in calling-convention order.
- <a id="rename_placeholder"></a>`rename_placeholder(gm: fx.GraphModule, node: fx.Node, new_name: str)` — [`L379`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L379) — Replace a placeholder with a new placeholder that has ``new_name``.
- <a id="trace_graph_pp_graph"></a>`trace_graph_pp_graph(name: str, gm: fx.GraphModule)` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L56) — Emit a readable FX graph artifact for tlparse.
- <a id="unique_in_order"></a>`unique_in_order(values: Iterable[T])` — [`L331`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L331) — Return ``values`` without duplicates, preserving first occurrence.

## Module values
- <a id="T"></a>`T` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L45)
- <a id="_UNSUPPORTED_SYMBOLIC_META_TYPES._UNSUPPORTED_SYMBOLIC_META_TYPES"></a>`_UNSUPPORTED_SYMBOLIC_META_TYPES` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/utils.py#L46)

