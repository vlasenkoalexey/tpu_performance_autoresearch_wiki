---
title: 'Module: torchtitan/experiments/graph_trainer/ep_chunk_pass.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/ep_chunk_pass.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.ep_chunk_pass`/
symbols:
  _split_live_ins: _split_live_ins().
  _transform_region: _transform_region().
  _Plan.region: _Plan#region.
  _materialize_live_out: _materialize_live_out().
  apply_chunk_pass: apply_chunk_pass().
  _materialize_full_live_out: _materialize_full_live_out().
  _copy_body: _copy_body().
  _split_live_out_users: _split_live_out_users().
  _set_synthetic_meta: _set_synthetic_meta().
  _validate_no_non_ep_collectives: _validate_no_non_ep_collectives().
  _find_regions: _find_regions().
  populate_chunk_dim_metadata_pass: populate_chunk_dim_metadata_pass().
  _materialization_boundary: _materialization_boundary().
  _plan_regions: _plan_regions().
  _chunk_dim_from_symbols: _chunk_dim_from_symbols().
  _materialize_suffix_from_full_boundary: _materialize_suffix_from_full_boundary().
  _chunk_influenced_region_nodes: _chunk_influenced_region_nodes().
  _grad_escape_boundaries: _grad_escape_boundaries().
  ep_overlap_chunk_pass: ep_overlap_chunk_pass().
  _chunk_copied_meta: _chunk_copied_meta().
  _map_arg: _map_arg().
  _Region.root_fqn: _Region#root_fqn.
  _region_nodes: _region_nodes().
  _validate_selected_symbol_shapes: _validate_selected_symbol_shapes().
  _is_contiguous_chunk_input_stride: _is_contiguous_chunk_input_stride().
  _validate_view_shape_uses_symbolic_extent: _validate_view_shape_uses_symbolic_extent().
  _ep_annotated_roots: _ep_annotated_roots().
  ChunkMode: ChunkMode.
  _Region: _Region#
  _Plan: _Plan#
  prepare_ep_overlap_trace_inputs: prepare_ep_overlap_trace_inputs().
  _Region.is_backward: _Region#is_backward.
  _set_chunk_meta: _set_chunk_meta().
  _chunk_dim_for_live_in: _chunk_dim_for_live_in().
  _build_plan: _build_plan().
  _copy_body.materialize_raw_chunk_symbol_arg: _copy_body().materialize_raw_chunk_symbol_arg().
  _split_live_ins.first_chunk_symbol_consumer: _split_live_ins().first_chunk_symbol_consumer().
  _region_roots: _region_roots().
  _is_chunkable: _is_chunkable().
  _is_tensor_with_chunk_dim: _is_tensor_with_chunk_dim().
  _rewrite_symbolic_value: _rewrite_symbolic_value().
  _pattern_root: _pattern_root().
  aten: aten.
  _Region.nodes: _Region#nodes.
  mark_chunk_dynamic_dims: mark_chunk_dynamic_dims().
  prepare_ep_overlap_trace_call_inputs: prepare_ep_overlap_trace_call_inputs().
  _Plan.body: _Plan#body.
  _MaterializationBoundary.node: _MaterializationBoundary#node.
  _materialize_symint_arg: _materialize_symint_arg().
  _rewrite_chunk_symint: _rewrite_chunk_symint().
  _validate_materialized: _validate_materialized().
  _owned_chunk_dependencies: _owned_chunk_dependencies().
  _grad_output_suffix_nodes: _grad_output_suffix_nodes().
  _semantic_body_closure: _semantic_body_closure().
  _create_size_or_stride_node: _create_size_or_stride_node().
  _create_half_extent_node: _create_half_extent_node().
  _chunk_tensor_meta: _chunk_tensor_meta().
  _chunk_meta_value: _chunk_meta_value().
  _is_shape_preserving_reduction: _is_shape_preserving_reduction().
  _is_materialization_suffix_node: _is_materialization_suffix_node().
  _add_materialization_proof: _add_materialization_proof().
  _ep_roots: _ep_roots().
  _MatchedRoot.root_fqn: _MatchedRoot#root_fqn.
  _tensor_inputs: _tensor_inputs().
  _Plan.live_ins: _Plan#live_ins.
  _materialize_symint_args: _materialize_symint_args().
  _is_ep_collective_node: _is_ep_collective_node().
  _shape_env_for_symbol: _shape_env_for_symbol().
  _freshen_copied_unbacked_bindings: _freshen_copied_unbacked_bindings().
  _linear_extent_coeff: _linear_extent_coeff().
  _split_live_ins.first_chunk_symbol_consumer.value_depends_on_chunk_symbol: _split_live_ins().first_chunk_symbol_consumer().value_depends_on_chunk_symbol().
  _mutates_input: _mutates_input().
  _is_semantic_user: _is_semantic_user().
  _node_depends_on_chunk_symbol: _node_depends_on_chunk_symbol().
  _ChunkDim.dim: _ChunkDim#dim.
  _MaterializationBoundary: _MaterializationBoundary#
  _chunk_symbol_subs: _chunk_symbol_subs().
  _split_live_ins.first_body_user: _split_live_ins().first_body_user().
  _describe_node: _describe_node().
  _MaterializationBoundary.suffix: _MaterializationBoundary#suffix.
  _MatchedRoot: _MatchedRoot#
  _custom_meta: _custom_meta().
  prepare_ep_overlap_trace_inputs.mark_leaf: prepare_ep_overlap_trace_inputs().mark_leaf().
  _is_contiguous_with_hints: _is_contiguous_with_hints().
  _symbol_has_selected_runtime_assert: _symbol_has_selected_runtime_assert().
  _hint_for_copied_unbacked_symbol: _hint_for_copied_unbacked_symbol().
  _fresh_unbacked_symbol_for_copy: _fresh_unbacked_symbol_for_copy().
  _rewrite_unbacked_keypath: _rewrite_unbacked_keypath().
  _shape_arg_depends_on_chunk_symbol: _shape_arg_depends_on_chunk_symbol().
  _validate_no_raw_chunk_symbol_args: _validate_no_raw_chunk_symbol_args().
  _erase_unused_copied_body: _erase_unused_copied_body().
  _Plan.live_out_users: _Plan#live_out_users.
  _ChunkDim: _ChunkDim#
  _copy_meta: _copy_meta().
  _Region.synthetic_parent_fqn: _Region#synthetic_parent_fqn.
  _Plan.grad_escape_boundaries: _Plan#grad_escape_boundaries.
  _ChunkDim.hint: _ChunkDim#hint.
  _MatchedRoot.synthetic_parent_fqn: _MatchedRoot#synthetic_parent_fqn.
  _mutable_arg_indices: _mutable_arg_indices().
  prepare_ep_overlap_trace_call_inputs.rebind: prepare_ep_overlap_trace_call_inputs().rebind().
  _contiguous_chunk_meta: _contiguous_chunk_meta().
  _graph_output_nodes: _graph_output_nodes().
  _map_arg.scalar_for_chunk: _map_arg().scalar_for_chunk().
  _set_direction_meta: _set_direction_meta().
  _split_view_meta: _split_view_meta().
  _symbolic_scalars: _symbolic_scalars().
  _source_stack: _source_stack().
  _static_placeholders: _static_placeholders().
---
# Module: [`torchtitan/experiments/graph_trainer/ep_chunk_pass.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py)

## Classes
### <a id="_ChunkDim"></a>`_ChunkDim`
- def: [`torchtitan/experiments/graph_trainer/ep_chunk_pass.py:131`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L131)
- signature: `class _ChunkDim:`
- members:
  - <a id="_ChunkDim.dim"></a>`dim` — [`L132`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L132)
  - <a id="_ChunkDim.hint"></a>`hint` — [`L133`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L133)
- used by: [`_materialize_live_out`](ep_chunk_pass.md#_materialize_live_out), [`_chunk_dim_from_symbols`](ep_chunk_pass.md#_chunk_dim_from_symbols), [`_is_contiguous_chunk_input_stride`](ep_chunk_pass.md#_is_contiguous_chunk_input_stride), [`_chunk_dim_for_live_in`](ep_chunk_pass.md#_chunk_dim_for_live_in)  (1 test-only)

### <a id="_MatchedRoot"></a>`_MatchedRoot`
- def: [`torchtitan/experiments/graph_trainer/ep_chunk_pass.py:143`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L143)
- signature: `class _MatchedRoot:`
- members:
  - <a id="_MatchedRoot.root_fqn"></a>`root_fqn` — [`L144`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L144)
  - <a id="_MatchedRoot.synthetic_parent_fqn"></a>`synthetic_parent_fqn` — [`L145`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L145)
- used by: [`_find_regions`](ep_chunk_pass.md#_find_regions), [`_ep_annotated_roots`](ep_chunk_pass.md#_ep_annotated_roots), [`_region_roots`](ep_chunk_pass.md#_region_roots), [`_pattern_root`](ep_chunk_pass.md#_pattern_root), [`_ep_roots`](ep_chunk_pass.md#_ep_roots)

### <a id="_MaterializationBoundary"></a>`_MaterializationBoundary`
- def: [`torchtitan/experiments/graph_trainer/ep_chunk_pass.py:137`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L137)
- signature: `class _MaterializationBoundary:`
- members:
  - <a id="_MaterializationBoundary.node"></a>`node` — [`L138`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L138)
  - <a id="_MaterializationBoundary.suffix"></a>`suffix` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L139)
- used by: [`_materialize_full_live_out`](ep_chunk_pass.md#_materialize_full_live_out), [`_materialization_boundary`](ep_chunk_pass.md#_materialization_boundary)

### <a id="_Plan"></a>`_Plan`
- def: [`torchtitan/experiments/graph_trainer/ep_chunk_pass.py:122`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L122)
- signature: `class _Plan:`
- members:
  - <a id="_Plan.body"></a>`body` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L124)
  - <a id="_Plan.grad_escape_boundaries"></a>`grad_escape_boundaries` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L127)
  - <a id="_Plan.live_ins"></a>`live_ins` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L125)
  - <a id="_Plan.live_out_users"></a>`live_out_users` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L126)
  - <a id="_Plan.region"></a>`region` — [`L123`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L123)
- uses (calls/refs, reference-scoped): [`_Region`](ep_chunk_pass.md#_Region)
- used by: [`_split_live_ins`](ep_chunk_pass.md#_split_live_ins), [`_transform_region`](ep_chunk_pass.md#_transform_region), [`_materialize_live_out`](ep_chunk_pass.md#_materialize_live_out), [`apply_chunk_pass`](ep_chunk_pass.md#apply_chunk_pass), [`_materialize_full_live_out`](ep_chunk_pass.md#_materialize_full_live_out), [`_copy_body`](ep_chunk_pass.md#_copy_body), [`_split_live_out_users`](ep_chunk_pass.md#_split_live_out_users), [`_materialization_boundary`](ep_chunk_pass.md#_materialization_boundary), [`_plan_regions`](ep_chunk_pass.md#_plan_regions), [`_validate_no_non_ep_collectives`](ep_chunk_pass.md#_validate_no_non_ep_collectives), [`_materialize_suffix_from_full_boundary`](ep_chunk_pass.md#_materialize_suffix_from_full_boundary), [`_build_plan`](ep_chunk_pass.md#_build_plan), [`first_chunk_symbol_consumer`](ep_chunk_pass.md#_split_live_ins.first_chunk_symbol_consumer), [`materialize_raw_chunk_symbol_arg`](ep_chunk_pass.md#_copy_body.materialize_raw_chunk_symbol_arg), [`first_body_user`](ep_chunk_pass.md#_split_live_ins.first_body_user)

### <a id="_Region"></a>`_Region`
- def: [`torchtitan/experiments/graph_trainer/ep_chunk_pass.py:114`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L114)
- signature: `class _Region:`
- members:
  - <a id="_Region.is_backward"></a>`is_backward` — [`L117`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L117)
  - <a id="_Region.nodes"></a>`nodes` — [`L118`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L118)
  - <a id="_Region.root_fqn"></a>`root_fqn` — [`L115`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L115)
  - <a id="_Region.synthetic_parent_fqn"></a>`synthetic_parent_fqn` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L116)
- used by: [`_split_live_ins`](ep_chunk_pass.md#_split_live_ins), [`_transform_region`](ep_chunk_pass.md#_transform_region), [`region`](ep_chunk_pass.md#_Plan.region), [`_materialize_live_out`](ep_chunk_pass.md#_materialize_live_out), [`apply_chunk_pass`](ep_chunk_pass.md#apply_chunk_pass), [`_copy_body`](ep_chunk_pass.md#_copy_body), [`_split_live_out_users`](ep_chunk_pass.md#_split_live_out_users), [`_set_synthetic_meta`](ep_chunk_pass.md#_set_synthetic_meta), [`_find_regions`](ep_chunk_pass.md#_find_regions), [`_materialization_boundary`](ep_chunk_pass.md#_materialization_boundary), [`_validate_no_non_ep_collectives`](ep_chunk_pass.md#_validate_no_non_ep_collectives), [`_build_plan`](ep_chunk_pass.md#_build_plan), [`_set_chunk_meta`](ep_chunk_pass.md#_set_chunk_meta), [`first_chunk_symbol_consumer`](ep_chunk_pass.md#_split_live_ins.first_chunk_symbol_consumer), [`_materialize_symint_arg`](ep_chunk_pass.md#_materialize_symint_arg), [`_create_half_extent_node`](ep_chunk_pass.md#_create_half_extent_node), [`_create_size_or_stride_node`](ep_chunk_pass.md#_create_size_or_stride_node), [`_materialize_symint_args`](ep_chunk_pass.md#_materialize_symint_args)  (1 test-only)

## Functions
- <a id="_add_materialization_proof"></a>`_add_materialization_proof(live_out: fx.Node, users: tuple[fx.Node, ...], *, is_backward: bool, grad_escape_boundaries: frozenset[fx.Node])` — [`L1893`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1893) — Step 5: prove when add reconstructs a no-chunk-dim live-out.
- <a id="_build_plan"></a>`_build_plan(region: _Region, grad_escape_boundaries: set[fx.Node] | frozenset[fx.Node])` — [`L1279`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1279) — Step 2: compute live-ins and live-outs for the current graph.
- <a id="_chunk_copied_meta"></a>`_chunk_copied_meta(meta: dict[str, Any], symbol_hints: dict[object, int], symbol_replacements: dict[object, object] | None = None)` — [`L1080`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1080)
- <a id="_chunk_dim_for_live_in"></a>`_chunk_dim_for_live_in(node: fx.Node, symbol_hints: dict[object, int])` — [`L771`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L771)
- <a id="_chunk_dim_from_symbols"></a>`_chunk_dim_from_symbols(val: torch.Tensor | None, symbol_hints: dict[object, int])` — [`L732`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L732) — Map the selected unbacked symbol to the tensor dimension it appears in.
- <a id="_chunk_influenced_region_nodes"></a>`_chunk_influenced_region_nodes(gm: fx.GraphModule, candidates: set[fx.Node], is_backward: bool, symbol_hints: dict[object, int], grad_escape_boundaries: set[fx.Node], per_chunk_sources: set[fx.Node])` — [`L466`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L466) — Shrink module candidates to the body that must be duplicated per chunk.
- <a id="_chunk_meta_value"></a>`_chunk_meta_value(value: object, symbol_hints: dict[object, int], symbol_replacements: dict[object, object])` — [`L1067`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1067)
- <a id="_chunk_symbol_subs"></a>`_chunk_symbol_subs(symbol_hints: dict[object, int])` — [`L835`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L835)
- <a id="_chunk_tensor_meta"></a>`_chunk_tensor_meta(val: torch.Tensor, symbol_hints: dict[object, int], symbol_replacements: dict[object, object] | None = None)` — [`L1044`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1044)
- <a id="_contiguous_chunk_meta"></a>`_contiguous_chunk_meta(val: torch.Tensor, dim: int)` — [`L792`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L792)
- <a id="_copy_body"></a>`_copy_body(gm: fx.GraphModule, plan: _Plan, *, chunks: dict[fx.Node, tuple[fx.Node, fx.Node]], scalars: dict[object, object], symbol_hints: dict[object, int], mode: ChunkMode, chunk_id: int, originals: dict[fx.Node, tuple[tuple[Any, ...], dict[str, Any], dict[str, Any], str]], in_place: bool, prior_chunk_copies: dict[fx.Node, fx.Node] | None = None, preserve_originals: set[fx.Node] | None = None)` — [`L1441`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1441) — Step 4: rewrite/copy one chunk body with remapped args and metadata.
- <a id="_copy_meta"></a>`_copy_meta(meta: dict[str, Any])` — [`L176`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L176)
- <a id="_create_half_extent_node"></a>`_create_half_extent_node(gm: fx.GraphModule, live_in: fx.Node, dim: int, *, region: _Region)` — [`L889`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L889)
- <a id="_create_size_or_stride_node"></a>`_create_size_or_stride_node(gm: fx.GraphModule, target: object, tensor_node: fx.Node, dim: int, *, region: _Region, role: str, chunk_id: int | None = None)` — [`L869`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L869)
- <a id="_custom_meta"></a>`_custom_meta(node: fx.Node)` — [`L148`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L148) — Return mutable custom metadata when present, otherwise an empty dict.
- <a id="_describe_node"></a>`_describe_node(node: fx.Node)` — [`L2125`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L2125)
- <a id="_ep_annotated_roots"></a>`_ep_annotated_roots(gm: fx.GraphModule, module_pattern: str)` — [`L2338`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L2338) — Find selected roots from EP annotations when no real EP PG is present.
- <a id="_ep_roots"></a>`_ep_roots(gm: fx.GraphModule, module_pattern: str)` — [`L2320`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L2320) — Find selected roots that contain real all-to-all collectives.
- <a id="_erase_unused_copied_body"></a>`_erase_unused_copied_body(gm: fx.GraphModule, copied_by_chunk: dict[int, dict[fx.Node, fx.Node]], *, protected: set[fx.Node])` — [`L2134`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L2134) — Step 6: erase unused copied nodes while preserving side effects/provenance.
- <a id="_find_regions"></a>`_find_regions(gm: fx.GraphModule, patterns: list[str], *, symbol_hints: dict[object, int], grad_escape_boundaries: set[fx.Node], per_chunk_sources: set[fx.Node])` — [`L516`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L516) — Build ordered forward/backward regions for all matched roots.
- <a id="_fresh_unbacked_symbol_for_copy"></a>`_fresh_unbacked_symbol_for_copy(shape_env: object, symbol: sympy.Symbol, symbol_hints: dict[object, int])` — [`L981`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L981)
- <a id="_freshen_copied_unbacked_bindings"></a>`_freshen_copied_unbacked_bindings(copied_meta: dict[str, Any], symbol_replacements: dict[object, object], symbol_hints: dict[object, int])` — [`L1026`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1026)
- <a id="_grad_escape_boundaries"></a>`_grad_escape_boundaries(gm: fx.GraphModule, *, mode: ChunkMode, symbol_hints: dict[object, int], optimize_grad_live_out: bool)` — [`L1197`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1197) — Step 2: identify backward no-chunk-dim grad escape boundaries.
- <a id="_grad_output_suffix_nodes"></a>`_grad_output_suffix_nodes(gm: fx.GraphModule, grad_escape_boundaries: set[fx.Node])` — [`L414`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L414) — Return post-materialization grad-output plumbing outside chunk bodies.
- <a id="_graph_output_nodes"></a>`_graph_output_nodes(gm: fx.GraphModule)` — [`L1123`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1123)
- <a id="_hint_for_copied_unbacked_symbol"></a>`_hint_for_copied_unbacked_symbol(shape_env: object, symbol: sympy.Symbol, hint: int, symbol_hints: dict[object, int])` — [`L968`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L968)
- <a id="_is_chunkable"></a>`_is_chunkable(node: fx.Node, *, mode: ChunkMode, static_nodes: set[fx.Node], symbol_hints: dict[object, int])` — [`L816`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L816)
- <a id="_is_contiguous_chunk_input_stride"></a>`_is_contiguous_chunk_input_stride(value: object, split_live_ins: list[fx.Node], symbol_hints: dict[object, int])` — [`L1370`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1370) — Return whether ``value`` is a stride from the contiguous chunk input.
- <a id="_is_contiguous_with_hints"></a>`_is_contiguous_with_hints(val: torch.Tensor, symbol_hints: dict[object, int])` — [`L798`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L798) — Return contiguity using explicit hints instead of symbolic guards.
- <a id="_is_ep_collective_node"></a>`_is_ep_collective_node(node: fx.Node, body: frozenset[fx.Node])` — [`L333`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L333) — Return whether a c10d node belongs to EP token exchange/count plumbing.
- <a id="_is_materialization_suffix_node"></a>`_is_materialization_suffix_node(node: fx.Node, *, optimize_grad_live_out: bool, symbol_hints: dict[object, int])` — [`L1149`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1149)
- <a id="_is_semantic_user"></a>`_is_semantic_user(node: fx.Node)` — [`L171`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L171) — Return whether a user must be preserved when crossing a chunk boundary.
- <a id="_is_shape_preserving_reduction"></a>`_is_shape_preserving_reduction(node: fx.Node, symbol_hints: dict[object, int])` — [`L1132`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1132)
- <a id="_is_tensor_with_chunk_dim"></a>`_is_tensor_with_chunk_dim(node: fx.Node, symbol_hints: dict[object, int])` — [`L831`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L831)
- <a id="_linear_extent_coeff"></a>`_linear_extent_coeff(value: object, symbols: set[object])` — [`L1349`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1349)
- <a id="_map_arg"></a>`_map_arg(arg: object, *, copied: dict[fx.Node, fx.Node], chunks: dict[fx.Node, tuple[fx.Node, fx.Node]], scalars: dict[object, object], symbol_replacements: dict[object, object], symbol_hints: dict[object, int], chunk_id: int, map_symbolic_exprs: bool = False)` — [`L1299`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1299) — Map original node/scalar arguments to the selected chunk equivalents.
- <a id="_materialization_boundary"></a>`_materialization_boundary(live_out: fx.Node, *, plan: _Plan, optimize_grad_live_out: bool, symbol_hints: dict[object, int])` — [`L1168`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1168) — Choose the earliest safe boundary before materializing a grad suffix once.
- <a id="_materialize_full_live_out"></a>`_materialize_full_live_out(gm: fx.GraphModule, plan: _Plan, live_out: fx.Node, users: tuple[fx.Node, ...], *, mode: ChunkMode, symbol_hints: dict[object, int], originals: dict[fx.Node, tuple[tuple[Any, ...], dict[str, Any], dict[str, Any], str]], copied_by_chunk: dict[int, dict[fx.Node, fx.Node]], optimize_grad_live_out: bool, memo: dict[fx.Node, fx.Node])` — [`L2033`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L2033) — Step 5: materialize a full live-out, possibly before a suffix chain.
- <a id="_materialize_live_out"></a>`_materialize_live_out(gm: fx.GraphModule, plan: _Plan, live_out: fx.Node, copies: tuple[fx.Node, fx.Node], users: tuple[fx.Node, ...], *, mode: ChunkMode, symbol_hints: dict[object, int], original_meta: dict[str, Any])` — [`L1918`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1918) — Step 5: reconstruct one full live-out from its two chunk values.
- <a id="_materialize_suffix_from_full_boundary"></a>`_materialize_suffix_from_full_boundary(gm: fx.GraphModule, plan: _Plan, boundary: fx.Node, materialized: fx.Node, suffix: tuple[fx.Node, ...], *, originals: dict[fx.Node, tuple[tuple[Any, ...], dict[str, Any], dict[str, Any], str]])` — [`L1981`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1981) — Step 5: copy tensor or shape suffixes after a boundary is full.
- <a id="_materialize_symint_arg"></a>`_materialize_symint_arg(gm: fx.GraphModule, value: torch.SymInt | int, *, region: _Region, role: str, chunk_id: int | None = None)` — [`L856`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L856)
- <a id="_materialize_symint_args"></a>`_materialize_symint_args(gm: fx.GraphModule, values: list[torch.SymInt | int] | tuple[torch.SymInt | int, ...], *, region: _Region, role: str, chunk_id: int | None = None)` — [`L839`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L839) — Materialize symbolic scalar args as FX nodes at the current insertion point.
- <a id="_mutable_arg_indices"></a>`_mutable_arg_indices(node: fx.Node)` — [`L159`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L159) — Return positional schema arg indices written by ``node``.
- <a id="_mutates_input"></a>`_mutates_input(node: fx.Node)` — [`L154`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L154) — Return whether a call_function schema writes through an aliased input.
- <a id="_node_depends_on_chunk_symbol"></a>`_node_depends_on_chunk_symbol(node: fx.Node, symbol_hints: dict[object, int])` — [`L323`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L323) — Return whether a node's fake value carries the selected chunk symbol.
- <a id="_owned_chunk_dependencies"></a>`_owned_chunk_dependencies(body: set[fx.Node], candidates: set[fx.Node], symbol_hints: dict[object, int])` — [`L368`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L368) — Return selected-symbol producers owned by an eager chunk body.
- <a id="_pattern_root"></a>`_pattern_root(pattern: str, fqn: str)` — [`L231`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L231) — Return the matched root and synthetic-parent FQN for a module pattern.
- <a id="_plan_regions"></a>`_plan_regions(gm: fx.GraphModule, patterns: list[str], *, mode: ChunkMode, optimize_grad_live_out: bool, per_chunk_sources: set[fx.Node] | None = None)` — [`L1241`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1241) — Step 2: plan all selected regions before lowering one direction.
- <a id="_region_nodes"></a>`_region_nodes(gm: fx.GraphModule, root: str, *, is_backward: bool, symbol_hints: dict[object, int], grad_escape_boundaries: set[fx.Node], per_chunk_sources: set[fx.Node])` — [`L263`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L263) — Return selected-symbol-influenced nodes inside one root/direction.
- <a id="_region_roots"></a>`_region_roots(gm: fx.GraphModule, patterns: list[str])` — [`L247`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L247) — Find concrete module roots matching the configured chunk patterns.
- <a id="_rewrite_chunk_symint"></a>`_rewrite_chunk_symint(value: object, symbol_hints: dict[object, int])` — [`L902`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L902)
- <a id="_rewrite_symbolic_value"></a>`_rewrite_symbolic_value(value: object, symbol_subs: dict[object, object], symbol_hints: dict[object, int])` — [`L911`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L911)
- <a id="_rewrite_unbacked_keypath"></a>`_rewrite_unbacked_keypath(keypath: tuple[object, ...], symbol_subs: dict[object, object], symbol_hints: dict[object, int])` — [`L1006`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1006)
- <a id="_semantic_body_closure"></a>`_semantic_body_closure(body: set[fx.Node])` — [`L436`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L436) — Keep only nodes needed to produce chunked tensor outputs.
- <a id="_set_chunk_meta"></a>`_set_chunk_meta(node: fx.Node, *, region: _Region, role: str, chunk_id: int | None = None)` — [`L192`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L192)
- <a id="_set_direction_meta"></a>`_set_direction_meta(node: fx.Node, *, is_backward: bool)` — [`L185`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L185)
- <a id="_set_synthetic_meta"></a>`_set_synthetic_meta(node: fx.Node, *, region: _Region, role: str, chunk_id: int | None = None)` — [`L210`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L210) — Attach parent-wrapper metadata to nodes introduced by graph chunking.
- <a id="_shape_arg_depends_on_chunk_symbol"></a>`_shape_arg_depends_on_chunk_symbol(shape_arg: object, symbol_hints: dict[object, int])` — [`L1389`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1389)
- <a id="_shape_env_for_symbol"></a>`_shape_env_for_symbol(meta: dict[str, Any], symbol: sympy.Symbol)` — [`L944`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L944)
- <a id="_source_stack"></a>`_source_stack(node: fx.Node)` — [`L1401`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1401)
- <a id="_split_live_ins"></a>`_split_live_ins(gm: fx.GraphModule, plan: _Plan, *, mode: ChunkMode, static_nodes: set[fx.Node], per_chunk: dict[fx.Node, tuple[fx.Node, fx.Node]])` — [`L1598`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1598) — Step 3: split chunked live-ins or recover existing provenance chunks.
- <a id="_split_live_out_users"></a>`_split_live_out_users(users: tuple[fx.Node, ...], plans: list[_Plan], producer_region: _Region, symbol_hints: dict[object, int])` — [`L1848`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1848) — Step 5: classify live-out consumers as chunked or full.
- <a id="_split_view_meta"></a>`_split_view_meta(val: torch.Tensor, dim: int)` — [`L786`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L786)
- <a id="_static_placeholders"></a>`_static_placeholders(gm: fx.GraphModule, num_static_inputs: int)` — [`L2311`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L2311) — Return placeholders that represent static model state.
- <a id="_symbol_has_selected_runtime_assert"></a>`_symbol_has_selected_runtime_assert(shape_env: object, symbol: sympy.Symbol, symbol_hints: dict[object, int])` — [`L954`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L954)
- <a id="_symbolic_scalars"></a>`_symbolic_scalars(value: object)` — [`L934`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L934)
- <a id="_tensor_inputs"></a>`_tensor_inputs(node: fx.Node)` — [`L1128`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1128)
- <a id="_transform_region"></a>`_transform_region(gm: fx.GraphModule, plan: _Plan, *, mode: ChunkMode, static_nodes: set[fx.Node], plans: list[_Plan], per_chunk: dict[fx.Node, tuple[fx.Node, fx.Node]], optimize_grad_live_out: bool)` — [`L2154`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L2154) — Steps 3-6: lower one planned region into two chunks.
- <a id="_validate_materialized"></a>`_validate_materialized(materialized: fx.Node, original: fx.Node, *, original_val: torch.Tensor | None = None, symbol_hints: dict[object, int])` — [`L1102`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1102) — Verify a materialized full value matches the original fake shape.
- <a id="_validate_no_non_ep_collectives"></a>`_validate_no_non_ep_collectives(plan: _Plan)` — [`L348`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L348) — Graph chunking may only duplicate EP collectives inside chunk bodies.
- <a id="_validate_no_raw_chunk_symbol_args"></a>`_validate_no_raw_chunk_symbol_args(gm: fx.GraphModule, symbol_hints: dict[object, int])` — [`L1575`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1575) — Reject chunk-created executable args that still embed selected SymInts.
- <a id="_validate_selected_symbol_shapes"></a>`_validate_selected_symbol_shapes(gm: fx.GraphModule, *, mode: ChunkMode)` — [`L751`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L751) — Check every chunk-created selected-symbol tensor is still classifiable.
- <a id="_validate_view_shape_uses_symbolic_extent"></a>`_validate_view_shape_uses_symbolic_extent(node: fx.Node, args: tuple[Any, ...], *, original_meta: dict[str, Any], symbol_hints: dict[object, int])` — [`L1406`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1406) — Reject baked Python shape constants in chunk-influenced view ops.
- <a id="apply_chunk_pass"></a>`apply_chunk_pass(gm: fx.GraphModule, example_inputs: tuple[Any, ...] | None = None, *, mode: ChunkMode, module_patterns: list[str], num_static_inputs: int = 0, optimize_grad_live_out: bool = True)` — [`L2354`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L2354) — Run graph chunking for the requested mode and module patterns.
- <a id="ep_overlap_chunk_pass"></a>`ep_overlap_chunk_pass(gm: fx.GraphModule, example_inputs: tuple[Any, ...] | None = None, *, mode: ChunkMode, module_pattern: str, num_static_inputs: int = 0, optimize_grad_live_out: bool = True, require_all_to_all: bool = True)` — [`L2426`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L2426) — Resolve EP roots from one pattern, then run graph chunking.
- <a id="_split_live_ins.first_body_user"></a>`first_body_user(node: fx.Node)` — [`L1678`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1678)
- <a id="_split_live_ins.first_chunk_symbol_consumer"></a>`first_chunk_symbol_consumer(node: fx.Node)` — [`L1681`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1681)
- <a id="mark_chunk_dynamic_dims"></a>`mark_chunk_dynamic_dims(tensor: torch.Tensor, *, mode: ChunkMode)` — [`L590`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L590) — Step 1: mark the user-selected tensor dimension unbacked with a hint.
- <a id="prepare_ep_overlap_trace_inputs.mark_leaf"></a>`mark_leaf(value: object)` — [`L643`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L643)
- <a id="_copy_body.materialize_raw_chunk_symbol_arg"></a>`materialize_raw_chunk_symbol_arg(arg: object, *, chunk_id: int)` — [`L1462`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1462)
- <a id="populate_chunk_dim_metadata_pass"></a>`populate_chunk_dim_metadata_pass(gm: fx.GraphModule, example_inputs: tuple[Any, ...] | None = None, *, mode: ChunkMode)` — [`L552`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L552) — Step 1: record selected dynamic symbol hints on placeholders.
- <a id="prepare_ep_overlap_trace_call_inputs"></a>`prepare_ep_overlap_trace_call_inputs(compile_config: Any, args: tuple[Any, ...], kwargs: dict[str, Any])` — [`L670`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L670) — Bind FlexInnerAttention mask lengths to fake token-grid dims during tracing.
- <a id="prepare_ep_overlap_trace_inputs"></a>`prepare_ep_overlap_trace_inputs(compile_config: Any, args: tuple[Any, ...], kwargs: dict[str, Any])` — [`L627`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L627) — Step 1: prepare trace inputs for graph chunking when EP overlap is enabled.
- <a id="prepare_ep_overlap_trace_call_inputs.rebind"></a>`rebind(mask: object)` — [`L694`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L694)
- <a id="_map_arg.scalar_for_chunk"></a>`scalar_for_chunk(value: object)` — [`L1312`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1312)
- <a id="_split_live_ins.first_chunk_symbol_consumer.value_depends_on_chunk_symbol"></a>`value_depends_on_chunk_symbol(value: object)` — [`L1682`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L1682)

## Module values
- <a id="ChunkMode"></a>`ChunkMode` — [`L107`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L107)
- <a id="aten"></a>`aten` — [`L106`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/ep_chunk_pass.py#L106)

