---
title: 'Module: torchtitan/experiments/graph_trainer/ep_pass_utils.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/ep_pass_utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.ep_pass_utils`/
symbols:
  concretize_ep_chunk_symbolic_shapes_pass: concretize_ep_chunk_symbolic_shapes_pass().
  tensor_meta: tensor_meta().
  collect_chunked_regions: collect_chunked_regions().
  ChunkBody.owner: ChunkBody#owner.
  free_symbols: free_symbols().
  ChunkOwner: ChunkOwner#
  chunk_symbol_hints_for_mode: chunk_symbol_hints_for_mode().
  _eval_hint: _eval_hint().
  same_shape_with_hints: same_shape_with_hints().
  ChunkedRegion.bodies_by_chunk: ChunkedRegion#bodies_by_chunk.
  dim_hint: dim_hint().
  _chunk_owner: _chunk_owner().
  CHUNK_SYMBOL_HINTS_META: CHUNK_SYMBOL_HINTS_META.
  ChunkOwner.root_fqn: ChunkOwner#root_fqn.
  ChunkOwner.chunk_id: ChunkOwner#chunk_id.
  ChunkBody: ChunkBody#
  _record_symbols_from_extent: _record_symbols_from_extent().
  _concretize_value: _concretize_value().
  ChunkBody.nodes: ChunkBody#nodes.
  _placeholder_symbol_hints: _placeholder_symbol_hints().
  _concretize_graph_module: _concretize_graph_module().
  ChunkOwner.is_backward: ChunkOwner#is_backward.
  ChunkedRegion: ChunkedRegion#
  _concretize_arg: _concretize_arg().
  expr_key: expr_key().
  depends_on_chunk_symbol: depends_on_chunk_symbol().
  _validate_no_chunk_symbols: _validate_no_chunk_symbols().
  ordered_nodes: ordered_nodes().
  _hint: _hint().
  _concretize_tensor_meta: _concretize_tensor_meta().
  same_symbolic_expr: same_symbolic_expr().
  is_module_fqn_inside_root: is_module_fqn_inside_root().
  ChunkedRegion.is_backward: ChunkedRegion#is_backward.
  _concretize_meta_value: _concretize_meta_value().
  _concretize_chunk_example_inputs: _concretize_chunk_example_inputs().
  _is_dead_chunk_scalar_plumbing: _is_dead_chunk_scalar_plumbing().
  _validate_no_false_guards: _validate_no_false_guards().
  is_c10d_functional_node: is_c10d_functional_node().
  ChunkedRegion.root_fqn: ChunkedRegion#root_fqn.
  symbolic_expr: symbolic_expr().
  same_dim_hint: same_dim_hint().
  same_tensor_domain: same_tensor_domain().
  _selected_symbol_hints: _selected_symbol_hints().
  _is_assert_target: _is_assert_target().
  statically_equals_hint: statically_equals_hint().
  _DEAD_CHUNK_SCALAR_TARGETS: _DEAD_CHUNK_SCALAR_TARGETS.
  _ASSERT_TARGETS: _ASSERT_TARGETS.
  _derive_symbol_hint: _derive_symbol_hint().
  _clear_chunk_tensor_marks: _clear_chunk_tensor_marks().
  _concretized_guard_value: _concretized_guard_value().
  view_shape_arg_index: view_shape_arg_index().
  numel_hint: numel_hint().
  aten: aten.
  is_view_target: is_view_target().
  ChunkBody.node_set: ChunkBody#node_set.
  ChunkBody.live_ins: ChunkBody#live_ins.
  ChunkBody.producer: ChunkBody#producer.
  _merge_symbol_hint: _merge_symbol_hint().
  _iter_graph_modules: _iter_graph_modules().
  concretize_ep_chunk_symbolic_shapes_pass.replace_scalar: concretize_ep_chunk_symbolic_shapes_pass().replace_scalar().
---
# Module: [`torchtitan/experiments/graph_trainer/ep_pass_utils.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py)

## Classes
### <a id="ChunkBody"></a>`ChunkBody`
- def: [`torchtitan/experiments/graph_trainer/ep_pass_utils.py:140`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L140)
- doc: A planned chunk body plus its external graph inputs.
- signature: `class ChunkBody:`
- members:
  - <a id="ChunkBody.live_ins"></a>`live_ins` — [`L146`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L146)
  - <a id="ChunkBody.node_set"></a>`node_set` — [`L145`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L145)
  - <a id="ChunkBody.nodes"></a>`nodes` — [`L144`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L144)
  - <a id="ChunkBody.owner"></a>`owner` — [`L143`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L143)
  - <a id="ChunkBody.producer"></a>`producer` — [`L147`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L147)
- uses (calls/refs, reference-scoped): [`ChunkOwner`](ep_pass_utils.md#ChunkOwner)
- used by: [`_build_region_phases`](ep_overlap_pass.md#_build_region_phases), [`_plan_region`](ep_overlap_pass.md#_plan_region), [`_split_token_count_sync_closure`](ep_overlap_pass.md#_split_token_count_sync_closure), [`collect_chunked_regions`](ep_pass_utils.md#collect_chunked_regions), [`_collect_token_exchanges`](ep_overlap_pass.md#_collect_token_exchanges), [`_schedule_ep_overlap_regions`](ep_overlap_pass.md#_schedule_ep_overlap_regions), [`_body_deps`](ep_overlap_pass.md#_body_deps), [`visit`](ep_overlap_pass.md#_marker_closure.visit), [`_validate_token_count_sync_copies`](ep_overlap_pass.md#_validate_token_count_sync_copies), [`bodies_by_chunk`](ep_pass_utils.md#ChunkedRegion.bodies_by_chunk), [`_body_ancestors`](ep_overlap_pass.md#_body_ancestors), [`_marker_closure`](ep_overlap_pass.md#_marker_closure)  (1 test-only)

### <a id="ChunkOwner"></a>`ChunkOwner`
- def: [`torchtitan/experiments/graph_trainer/ep_pass_utils.py:131`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L131)
- doc: Stable identity for one chunk body in one direction of one module.
- signature: `class ChunkOwner:`
- members:
  - <a id="ChunkOwner.chunk_id"></a>`chunk_id` — [`L136`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L136)
  - <a id="ChunkOwner.is_backward"></a>`is_backward` — [`L135`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L135)
  - <a id="ChunkOwner.root_fqn"></a>`root_fqn` — [`L134`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L134)
- used by: [`_build_region_phases`](ep_overlap_pass.md#_build_region_phases), [`_plan_region`](ep_overlap_pass.md#_plan_region), [`_split_token_count_sync_closure`](ep_overlap_pass.md#_split_token_count_sync_closure), [`collect_chunked_regions`](ep_pass_utils.md#collect_chunked_regions), [`owner`](ep_pass_utils.md#ChunkBody.owner), [`_body_deps`](ep_overlap_pass.md#_body_deps), [`visit`](ep_overlap_pass.md#_marker_closure.visit), [`_validate_token_count_sync_copies`](ep_overlap_pass.md#_validate_token_count_sync_copies), [`_chunk_owner`](ep_pass_utils.md#_chunk_owner), [`_ready_nodes`](ep_overlap_pass.md#_ready_nodes), [`_same_region_owner`](ep_overlap_pass.md#_same_region_owner), [`_append_ready_blocks`](ep_overlap_pass.md#_append_ready_blocks), [`_hidden_body_deps`](ep_overlap_pass.md#_hidden_body_deps), [`_body_ancestors`](ep_overlap_pass.md#_body_ancestors), [`_marker_closure`](ep_overlap_pass.md#_marker_closure)  (1 test-only)

### <a id="ChunkedRegion"></a>`ChunkedRegion`
- def: [`torchtitan/experiments/graph_trainer/ep_pass_utils.py:151`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L151)
- doc: The chunk bodies for one module/direction pair.
- signature: `class ChunkedRegion:`
- members:
  - <a id="ChunkedRegion.bodies_by_chunk"></a>`bodies_by_chunk` — [`L156`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L156)
  - <a id="ChunkedRegion.is_backward"></a>`is_backward` — [`L155`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L155)
  - <a id="ChunkedRegion.root_fqn"></a>`root_fqn` — [`L154`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L154)
- uses (calls/refs, reference-scoped): [`ChunkBody`](ep_pass_utils.md#ChunkBody)
- used by: [`_build_region_phases`](ep_overlap_pass.md#_build_region_phases), [`_plan_region`](ep_overlap_pass.md#_plan_region), [`collect_chunked_regions`](ep_pass_utils.md#collect_chunked_regions), [`_schedule_ep_overlap_regions`](ep_overlap_pass.md#_schedule_ep_overlap_regions), [`_apply_schedule`](ep_overlap_pass.md#_apply_schedule), [`_ready_nodes`](ep_overlap_pass.md#_ready_nodes), [`_append_ready_blocks`](ep_overlap_pass.md#_append_ready_blocks), [`region`](ep_overlap_pass.md#_ScheduledRegion.region)  (1 test-only)

## Functions
- <a id="_chunk_owner"></a>`_chunk_owner(node: fx.Node)` — [`L159`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L159)
- <a id="_clear_chunk_tensor_marks"></a>`_clear_chunk_tensor_marks(tensor: torch.Tensor, symbol_hints: dict[object, int])` — [`L529`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L529)
- <a id="_concretize_arg"></a>`_concretize_arg(arg: object, symbol_hints: dict[object, int])` — [`L492`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L492)
- <a id="_concretize_chunk_example_inputs"></a>`_concretize_chunk_example_inputs(example_inputs: list[Any] | tuple[Any, ...] | None, symbol_hints: dict[object, int])` — [`L563`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L563)
- <a id="_concretize_graph_module"></a>`_concretize_graph_module(gm: fx.GraphModule, symbol_hints: dict[object, int])` — [`L623`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L623)
- <a id="_concretize_meta_value"></a>`_concretize_meta_value(value: object, symbol_hints: dict[object, int])` — [`L521`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L521)
- <a id="_concretize_tensor_meta"></a>`_concretize_tensor_meta(val: torch.Tensor, symbol_hints: dict[object, int])` — [`L508`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L508)
- <a id="_concretize_value"></a>`_concretize_value(value: object, symbol_hints: dict[object, int])` — [`L466`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L466)
- <a id="_concretized_guard_value"></a>`_concretized_guard_value(value: object, symbol_hints: dict[object, int], scalar_constants: dict[fx.Node, int | bool])` — [`L664`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L664)
- <a id="_derive_symbol_hint"></a>`_derive_symbol_hint(expr: object, extent_hint: int, symbol: object)` — [`L247`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L247)
- <a id="_eval_hint"></a>`_eval_hint(value: object, hints: dict[object, int])` — [`L223`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L223) — Evaluate ``value`` by substituting known symbol hints.
- <a id="_hint"></a>`_hint(value: object)` — [`L207`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L207) — Return a concrete/optimization hint when PyTorch exposes one.
- <a id="_is_assert_target"></a>`_is_assert_target(target: object)` — [`L660`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L660)
- <a id="_is_dead_chunk_scalar_plumbing"></a>`_is_dead_chunk_scalar_plumbing(node: fx.Node)` — [`L649`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L649) — Return whether ``node`` is dead scalar shape/assert plumbing.
- <a id="_iter_graph_modules"></a>`_iter_graph_modules(gm: fx.GraphModule)` — [`L601`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L601) — Return ``gm`` and GraphModule subgraphs referenced by its nodes.
- <a id="_merge_symbol_hint"></a>`_merge_symbol_hint(hints: dict[object, int], symbol: object, hint: int, *, source: str)` — [`L263`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L263)
- <a id="_placeholder_symbol_hints"></a>`_placeholder_symbol_hints(gm: fx.GraphModule)` — [`L326`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L326)
- <a id="_record_symbols_from_extent"></a>`_record_symbols_from_extent(hints: dict[object, int], extent: object, *, source: str)` — [`L275`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L275)
- <a id="_selected_symbol_hints"></a>`_selected_symbol_hints(node: fx.Node)` — [`L297`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L297)
- <a id="_validate_no_chunk_symbols"></a>`_validate_no_chunk_symbols(gm: fx.GraphModule, symbol_hints: dict[object, int])` — [`L579`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L579)
- <a id="_validate_no_false_guards"></a>`_validate_no_false_guards(gm: fx.GraphModule, symbol_hints: dict[object, int], scalar_constants: dict[fx.Node, int | bool])` — [`L682`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L682)
- <a id="chunk_symbol_hints_for_mode"></a>`chunk_symbol_hints_for_mode(gm: fx.GraphModule, mode: str | None = None)` — [`L302`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L302) — Collect the selected chunk symbols and their optimization hints.
- <a id="collect_chunked_regions"></a>`collect_chunked_regions(gm: fx.GraphModule, *, module_pattern: str)` — [`L175`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L175) — Collect chunk bodies matching ``module_pattern`` in graph order.
- <a id="concretize_ep_chunk_symbolic_shapes_pass"></a>`concretize_ep_chunk_symbolic_shapes_pass(gm: fx.GraphModule, example_inputs: list[Any] | tuple[Any, ...] | None = None)` — [`L706`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L706) — Concretize EP chunk symbolic shapes after scheduling.
- <a id="depends_on_chunk_symbol"></a>`depends_on_chunk_symbol(value: object, symbol_hints: dict[object, int])` — [`L440`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L440) — Return whether ``value`` still references any selected chunk symbol.
- <a id="dim_hint"></a>`dim_hint(dim: object, symbol_hints: dict[object, int])` — [`L397`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L397) — Return the hinted integer value for a dimension-like object.
- <a id="expr_key"></a>`expr_key(value: object)` — [`L392`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L392) — Return the canonical object used to match identical symbolic expressions.
- <a id="free_symbols"></a>`free_symbols(value: object)` — [`L118`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L118) — Return symbolic-shape free symbols for values accepted by PyTorch.
- <a id="is_c10d_functional_node"></a>`is_c10d_functional_node(node: fx.Node)` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L69) — Return whether a node is a distributed functional op (AG/RS/A2A/wait).
- <a id="is_module_fqn_inside_root"></a>`is_module_fqn_inside_root(fqn: str, root_fqn: str)` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L58) — Return whether ``fqn`` is exactly ``root_fqn`` or one of its children.
- <a id="is_view_target"></a>`is_view_target(target: object)` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L78) — Return whether a target is a true PyTorch view op overload.
- <a id="numel_hint"></a>`numel_hint(shape: object, symbol_hints: dict[object, int])` — [`L405`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L405) — Return hinted numel for a shape, or ``None`` if it is not provable.
- <a id="ordered_nodes"></a>`ordered_nodes(gm: fx.GraphModule)` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L125) — Map each graph node to its current topological position.
- <a id="concretize_ep_chunk_symbolic_shapes_pass.replace_scalar"></a>`replace_scalar(arg)` — [`L751`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L751)
- <a id="same_dim_hint"></a>`same_dim_hint(lhs: object, rhs: object, symbol_hints: dict[object, int])` — [`L420`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L420) — Return whether two dimensions are equal under chunk hints.
- <a id="same_shape_with_hints"></a>`same_shape_with_hints(lhs: object, rhs: object, node: fx.Node, symbol_hints: dict[object, int] | None = None)` — [`L343`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L343) — Compare tensor shapes after substituting available chunk hints.
- <a id="same_symbolic_expr"></a>`same_symbolic_expr(lhs: object, rhs: object)` — [`L374`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L374) — Return whether two symbolic/concrete expressions are structurally equal.
- <a id="same_tensor_domain"></a>`same_tensor_domain(lhs: fx.Node, rhs: fx.Node)` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L83) — Return whether two tensor nodes share dtype/device/layout metadata.
- <a id="statically_equals_hint"></a>`statically_equals_hint(value: object, hint: int | bool)` — [`L429`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L429) — Return whether symbolic reasoning proves ``value == hint``.
- <a id="symbolic_expr"></a>`symbolic_expr(value: object)` — [`L369`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L369) — Return the symbolic expression object for a PyTorch symbolic scalar.
- <a id="tensor_meta"></a>`tensor_meta(node: fx.Node)` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L63) — Return tensor fake value metadata, if this node has tensor metadata.
- <a id="view_shape_arg_index"></a>`view_shape_arg_index(target: object)` — [`L95`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L95) — Return the positional shape arg index for Tensor -> Tensor view ops.

## Module values
- <a id="CHUNK_SYMBOL_HINTS_META"></a>`CHUNK_SYMBOL_HINTS_META` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L38)
- <a id="_ASSERT_TARGETS"></a>`_ASSERT_TARGETS` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L55)
- <a id="_DEAD_CHUNK_SCALAR_TARGETS"></a>`_DEAD_CHUNK_SCALAR_TARGETS` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L39)
- <a id="aten"></a>`aten` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_pass_utils.py#L37)

