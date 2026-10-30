---
title: 'Module: torchtitan/experiments/graph_trainer/fsdp_passes.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/fsdp_passes.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.fsdp_passes`/
symbols:
  schedule_fsdp_comms_to_dense_regions_pass: schedule_fsdp_comms_to_dense_regions_pass().
  _collect_bucketed_fsdp_comms: _collect_bucketed_fsdp_comms().
  deduplicate_fsdp_unshard_chains_pass: deduplicate_fsdp_unshard_chains_pass().
  reassign_collective_pgs_pass: reassign_collective_pgs_pass().
  JointManualOverlapScheduler.scheduled: JointManualOverlapScheduler#scheduled.
  _EXTRA_FSDP_PG_REGISTRY._EXTRA_FSDP_PG_REGISTRY: _EXTRA_FSDP_PG_REGISTRY._EXTRA_FSDP_PG_REGISTRY.
  _build_layer_dense_regions: _build_layer_dense_regions().
  JointManualOverlapScheduler._manual_reorder_graph: JointManualOverlapScheduler#_manual_reorder_graph().
  JointManualOverlapScheduler._schedule_ag_prefetch: JointManualOverlapScheduler#_schedule_ag_prefetch().
  _build_top_dense_regions: _build_top_dense_regions().
  joint_transformer_block_bucketing_reordering_pass: joint_transformer_block_bucketing_reordering_pass().
  JointManualOverlapScheduler._manual_bucket_collectives: JointManualOverlapScheduler#_manual_bucket_collectives().
  _FsdpComm.kind: _FsdpComm#kind.
  _FsdpComm.logical_index: _FsdpComm#logical_index.
  JointManualOverlapScheduler.bucketer: JointManualOverlapScheduler#bucketer.
  _collect_bucketed_fsdp_comms._infer_fqn_and_direction: _collect_bucketed_fsdp_comms()._infer_fqn_and_direction().
  schedule_fsdp_comms_to_dense_regions_pass._add_move: schedule_fsdp_comms_to_dense_regions_pass()._add_move().
  _FsdpComm.wait: _FsdpComm#wait.
  JointManualOverlapScheduler._is_backward_fn: JointManualOverlapScheduler#_is_backward_fn.
  get_transformer_block_bucket_counts: get_transformer_block_bucket_counts().
  _is_backward_or_recomputed_node: _is_backward_or_recomputed_node().
  _get_or_create_extra_fsdp_pg: _get_or_create_extra_fsdp_pg().
  FSDPParamOrderBucketer._param_order_key: FSDPParamOrderBucketer#_param_order_key().
  _FsdpComm.launch: _FsdpComm#launch.
  _FsdpComm.direction: _FsdpComm#direction.
  _fsdp_bucket_logical_index: _fsdp_bucket_logical_index().
  _collect_bucketed_fsdp_comms._infer_fqn_and_direction._nearest_from: _collect_bucketed_fsdp_comms()._infer_fqn_and_direction()._nearest_from().
  FSDPParamOrderBucketer._bucket_group: FSDPParamOrderBucketer#_bucket_group().
  JointManualOverlapScheduler._annotate_new_bucket_nodes: JointManualOverlapScheduler#_annotate_new_bucket_nodes().
  _read_fsdp_bucket_meta: _read_fsdp_bucket_meta().
  _FSDP_BUCKET_META: _FSDP_BUCKET_META.
  _get_or_create_extra_pg: _get_or_create_extra_pg().
  JointManualOverlapScheduler.in_degree: JointManualOverlapScheduler#in_degree.
  joint_transformer_block_bucketing_reordering_pass._stack_fn: joint_transformer_block_bucketing_reordering_pass()._stack_fn().
  schedule_fsdp_comms_to_dense_regions_pass._find_dense_target: schedule_fsdp_comms_to_dense_regions_pass()._find_dense_target().
  schedule_fsdp_comms_to_dense_regions_pass._sink_output_only_wait_closure: schedule_fsdp_comms_to_dense_regions_pass()._sink_output_only_wait_closure().
  schedule_fsdp_comms_to_dense_regions_pass._move_chain_before: schedule_fsdp_comms_to_dense_regions_pass()._move_chain_before().
  autobucketing_reordering_pass: autobucketing_reordering_pass().
  transformer_block_bucketing_reordering_pass: transformer_block_bucketing_reordering_pass().
  JointManualOverlapScheduler.nodes: JointManualOverlapScheduler#nodes.
  _FsdpComm: _FsdpComm#
  _layer_id_from_fqn: _layer_id_from_fqn().
  JointManualOverlapScheduler.node_idx: JointManualOverlapScheduler#node_idx.
  get_fsdp_param_module_order: get_fsdp_param_module_order().
  FSDPParamOrderBucketer.fsdp_param_module_order: FSDPParamOrderBucketer#fsdp_param_module_order.
  JointManualOverlapScheduler.on_path_ready: JointManualOverlapScheduler#on_path_ready.
  JointManualOverlapScheduler._apply_trailing_block: JointManualOverlapScheduler#_apply_trailing_block().
  _FsdpComm.plan_fqns: _FsdpComm#plan_fqns.
  _is_top_level_param_fqn: _is_top_level_param_fqn().
  _is_dense_region_target_node: _is_dense_region_target_node().
  schedule_fsdp_comms_to_dense_regions_pass._collect_launch_chain: schedule_fsdp_comms_to_dense_regions_pass()._collect_launch_chain().
  _chain_nodes_to_placeholder: _chain_nodes_to_placeholder().
  deduplicate_fsdp_unshard_chains_pass._is_impure_for_fsdp_dedup: deduplicate_fsdp_unshard_chains_pass()._is_impure_for_fsdp_dedup().
  is_wait_tensor_from_fsdp: is_wait_tensor_from_fsdp().
  _reorder_overlap_nodes: _reorder_overlap_nodes().
  FSDPParamOrderBucketer: FSDPParamOrderBucketer#
  JointManualOverlapScheduler: JointManualOverlapScheduler#
  JointManualOverlapScheduler._schedule_rs_prefetch: JointManualOverlapScheduler#_schedule_rs_prefetch().
  _bucket_plan_fqns: _bucket_plan_fqns().
  _is_moe_layer_dense_fqn: _is_moe_layer_dense_fqn().
  _has_waited_fsdp_comm_launches: _has_waited_fsdp_comm_launches().
  _validate_transformer_block_bucket_counts: _validate_transformer_block_bucket_counts().
  schedule_fsdp_comms_to_dense_regions_pass._is_allowed_wait_tail_node: schedule_fsdp_comms_to_dense_regions_pass()._is_allowed_wait_tail_node().
  FSDPParamOrderBucketer.__init__: FSDPParamOrderBucketer#__init__().
  JointManualOverlapScheduler.__init__: JointManualOverlapScheduler#__init__().
---
# Module: [`torchtitan/experiments/graph_trainer/fsdp_passes.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py)

## Classes
### <a id="FSDPParamOrderBucketer"></a>`FSDPParamOrderBucketer`
- def: [`torchtitan/experiments/graph_trainer/fsdp_passes.py:276`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L276) — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- doc: Pack FSDP buckets in Eager FSDP2 parameter order.
- signature: `class FSDPParamOrderBucketer(ManualOverlapPreservingBucketer):`
- members:
  - <a id="FSDPParamOrderBucketer.fsdp_param_module_order"></a>`fsdp_param_module_order` — [`L286`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L286)
- protocol/private: <a id="FSDPParamOrderBucketer.__init__"></a>`__init__`[`L279`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L279), <a id="FSDPParamOrderBucketer._bucket_group"></a>`_bucket_group`[`L293`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L293), <a id="FSDPParamOrderBucketer._param_order_key"></a>`_param_order_key`[`L288`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L288)
- uses (calls/refs, reference-scoped): [`_MODULE_FQN`](common_utils.md#_MODULE_FQN)
- used by: [`bucketer`](fsdp_passes.md#JointManualOverlapScheduler.bucketer)

### <a id="JointManualOverlapScheduler"></a>`JointManualOverlapScheduler`
- def: [`torchtitan/experiments/graph_trainer/fsdp_passes.py:299`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L299) — documented in [graph-trainer](../../../../concepts/graph-trainer.md)
- doc: Manual overlap scheduler for joint forward+backward graphs.
- signature: `class JointManualOverlapScheduler(ManualOverlapScheduler):`
- members:
  - <a id="JointManualOverlapScheduler._manual_bucket_collectives"></a>`_manual_bucket_collectives(self)` — [`L353`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L353) — Bucket per module, splitting by direction to keep fwd/bwd buckets disjoint.
  - <a id="JointManualOverlapScheduler._manual_reorder_graph"></a>`_manual_reorder_graph(self)` — [`L398`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L398) — Reorder pass with separate fwd/bwd buffers so AG pairing never
  - <a id="JointManualOverlapScheduler._schedule_ag_prefetch"></a>`_schedule_ag_prefetch(self, overlap_deps: dict[fx.Node, OrderedSet[fx.Node]])` — [`L466`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L466) — Reversed walk that emits per-direction AG prefetch edges.
  - <a id="JointManualOverlapScheduler._schedule_rs_prefetch"></a>`_schedule_rs_prefetch(self, overlap_deps: dict[fx.Node, OrderedSet[fx.Node]])` — [`L426`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L426) — Top-down scheduling loop that emits RS prefetch edges.
  - <a id="JointManualOverlapScheduler.bucketer"></a>`bucketer` — [`L345`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L345)
  - <a id="JointManualOverlapScheduler.in_degree"></a>`in_degree` — [`L376`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L376)
  - <a id="JointManualOverlapScheduler.node_idx"></a>`node_idx` — [`L439`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L439)
  - <a id="JointManualOverlapScheduler.nodes"></a>`nodes` — [`L375`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L375)
  - <a id="JointManualOverlapScheduler.on_path_ready"></a>`on_path_ready` — [`L440`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L440)
  - <a id="JointManualOverlapScheduler.scheduled"></a>`scheduled` — [`L441`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L441)
- protocol/private: <a id="JointManualOverlapScheduler.__init__"></a>`__init__`[`L325`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L325), <a id="JointManualOverlapScheduler._annotate_new_bucket_nodes"></a>`_annotate_new_bucket_nodes`[`L378`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L378), <a id="JointManualOverlapScheduler._apply_trailing_block"></a>`_apply_trailing_block`[`L523`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L523), <a id="JointManualOverlapScheduler._is_backward_fn"></a>`_is_backward_fn`[`L343`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L343)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`_FSDP_BUCKET_META`](fsdp_passes.md#_FSDP_BUCKET_META), [`FSDPParamOrderBucketer`](fsdp_passes.md#FSDPParamOrderBucketer), [`_bucket_plan_fqns`](fsdp_passes.md#_bucket_plan_fqns), [`_reorder_overlap_nodes`](fsdp_passes.md#_reorder_overlap_nodes)
- used by: [`joint_transformer_block_bucketing_reordering_pass`](fsdp_passes.md#joint_transformer_block_bucketing_reordering_pass)

### <a id="_FsdpComm"></a>`_FsdpComm`
- def: [`torchtitan/experiments/graph_trainer/fsdp_passes.py:600`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L600)
- signature: `class _FsdpComm:`
- members:
  - <a id="_FsdpComm.direction"></a>`direction` — [`L604`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L604)
  - <a id="_FsdpComm.kind"></a>`kind` — [`L603`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L603)
  - <a id="_FsdpComm.launch"></a>`launch` — [`L601`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L601)
  - <a id="_FsdpComm.logical_index"></a>`logical_index` — [`L606`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L606)
  - <a id="_FsdpComm.plan_fqns"></a>`plan_fqns` — [`L605`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L605)
  - <a id="_FsdpComm.wait"></a>`wait` — [`L602`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L602)
- used by: [`schedule_fsdp_comms_to_dense_regions_pass`](fsdp_passes.md#schedule_fsdp_comms_to_dense_regions_pass), [`_collect_bucketed_fsdp_comms`](fsdp_passes.md#_collect_bucketed_fsdp_comms), [`_collect_rs_wait_deadlines`](../tpu/graph_trainer/remat_schedule.md#_collect_rs_wait_deadlines), [`_collect_backward_fsdp_owners`](../tpu/graph_trainer/graph_split.md#_collect_backward_fsdp_owners)  (1 test-only)

## Functions
- <a id="schedule_fsdp_comms_to_dense_regions_pass._add_move"></a>`_add_move(launch: fx.Node, wait: fx.Node, dense_region: list[fx.Node], description: str)` — [`L1230`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L1230)
- <a id="_bucket_plan_fqns"></a>`_bucket_plan_fqns(bucket: list[str] | str)` — [`L609`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L609)
- <a id="_build_layer_dense_regions"></a>`_build_layer_dense_regions(gm: torch.fx.GraphModule, n_layers: int, moe_layer_ids: frozenset[int])` — [`L755`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L755) — Build per-layer dense-region node lists for forward and backward.
- <a id="_build_top_dense_regions"></a>`_build_top_dense_regions(gm: torch.fx.GraphModule)` — [`L788`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L788) — Build dense compute regions for norm/lm_head outside transformer blocks.
- <a id="_chain_nodes_to_placeholder"></a>`_chain_nodes_to_placeholder(output: fx.Node, placeholder: fx.Node)` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L58) — Return graph nodes in one FSDP unshard chain, excluding the placeholder.
- <a id="_collect_bucketed_fsdp_comms"></a>`_collect_bucketed_fsdp_comms(gm: torch.fx.GraphModule, *, n_layers: int)` — [`L815`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L815) — Collect bucketed FSDP AG and RS (launch, wait) pairs per layer and direction.
- <a id="schedule_fsdp_comms_to_dense_regions_pass._collect_launch_chain"></a>`_collect_launch_chain(launch: fx.Node)` — [`L1113`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L1113) — Collect the FSDP infrastructure chain rooted at ``launch``.
- <a id="schedule_fsdp_comms_to_dense_regions_pass._find_dense_target"></a>`_find_dense_target(launch: fx.Node, dense_region: list[fx.Node])` — [`L1129`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L1129) — Pick the first dense node after the launch chain's external deps.
- <a id="_fsdp_bucket_logical_index"></a>`_fsdp_bucket_logical_index(plan_fqns: tuple[str, ...], *, n_layers: int)` — [`L672`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L672) — Map bucket provenance to the logical model slot it owns.
- <a id="_get_or_create_extra_fsdp_pg"></a>`_get_or_create_extra_fsdp_pg(source_pg_name: str)` — [`L189`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L189) — Return an extra FSDP PG with the same ranks and a distinct NCCL stream.
- <a id="_get_or_create_extra_pg"></a>`_get_or_create_extra_pg(source_pg_name: str, registry: dict[str, str], *, group_desc: str, high_priority: bool = False)` — [`L155`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L155)
- <a id="_has_waited_fsdp_comm_launches"></a>`_has_waited_fsdp_comm_launches(gm: torch.fx.GraphModule)` — [`L938`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L938) — Return whether the graph contains any waited FSDP AG/RS launch.
- <a id="_collect_bucketed_fsdp_comms._infer_fqn_and_direction"></a>`_infer_fqn_and_direction(launch: fx.Node, wait: fx.Node)` — [`L835`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L835)
- <a id="schedule_fsdp_comms_to_dense_regions_pass._is_allowed_wait_tail_node"></a>`_is_allowed_wait_tail_node(node: fx.Node, closure: set[fx.Node], wait: fx.Node)` — [`L1082`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L1082)
- <a id="_is_backward_or_recomputed_node"></a>`_is_backward_or_recomputed_node(node: fx.Node)` — [`L750`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L750) — Return whether ``node`` executes in the backward section.
- <a id="_is_dense_region_target_node"></a>`_is_dense_region_target_node(node: fx.Node)` — [`L705`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L705) — Return whether ``node`` is useful dense compute, not FSDP plumbing.
- <a id="deduplicate_fsdp_unshard_chains_pass._is_impure_for_fsdp_dedup"></a>`_is_impure_for_fsdp_dedup(node: fx.Node)` — [`L106`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L106)
- <a id="_is_moe_layer_dense_fqn"></a>`_is_moe_layer_dense_fqn(fqn: str)` — [`L660`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L660) — Return whether an MoE-layer FQN belongs to the dense attention region.
- <a id="_is_top_level_param_fqn"></a>`_is_top_level_param_fqn(fqn: str)` — [`L668`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L668)
- <a id="_layer_id_from_fqn"></a>`_layer_id_from_fqn(fqn: str)` — [`L613`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L613) — Extract layer index from ``layers.N...`` FQN prefix.
- <a id="schedule_fsdp_comms_to_dense_regions_pass._move_chain_before"></a>`_move_chain_before(launch: fx.Node, target: fx.Node)` — [`L1168`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L1168) — Move an AG/RS launch and its FSDP infrastructure chain before ``target``.
- <a id="_collect_bucketed_fsdp_comms._infer_fqn_and_direction._nearest_from"></a>`_nearest_from(starts: Iterable[fx.Node])` — [`L838`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L838)
- <a id="_read_fsdp_bucket_meta"></a>`_read_fsdp_bucket_meta(node: fx.Node)` — [`L804`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L804)
- <a id="_reorder_overlap_nodes"></a>`_reorder_overlap_nodes(graph: fx.Graph, overlap_deps: dict[fx.Node, OrderedSet[fx.Node]], bucketed_node_types: dict[fx.Node, str])` — [`L142`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L142)
- <a id="schedule_fsdp_comms_to_dense_regions_pass._sink_output_only_wait_closure"></a>`_sink_output_only_wait_closure(wait: fx.Node)` — [`L1146`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L1146) — Sink an RS wait and tail-only output/grad-accum users.
- <a id="joint_transformer_block_bucketing_reordering_pass._stack_fn"></a>`_stack_fn(node: torch.fx.Node)` — [`L576`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L576)
- <a id="_validate_transformer_block_bucket_counts"></a>`_validate_transformer_block_bucket_counts(comms: dict[int, dict[str, list[tuple[fx.Node, fx.Node]]]], *, n_layers: int, expected_bucket_counts: dict[int, int])` — [`L953`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L953)
- <a id="autobucketing_reordering_pass"></a>`autobucketing_reordering_pass(gm: torch.fx.GraphModule, example_inputs: tuple | None = None)` — [`L235`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L235) — Apply autobucketing and reordering optimization.
- <a id="deduplicate_fsdp_unshard_chains_pass"></a>`deduplicate_fsdp_unshard_chains_pass(gm: torch.fx.GraphModule, example_inputs: tuple | None = None)` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L74) — Canonicalize duplicate SimpleFSDP unshard chains per flat parameter.
- <a id="get_fsdp_param_module_order"></a>`get_fsdp_param_module_order(state_fqns: list[str])` — [`L265`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L265) — Return module order matching FSDP2's first-seen parameter order.
- <a id="get_transformer_block_bucket_counts"></a>`get_transformer_block_bucket_counts(module_bucket_plans: list[list[str] | str], *, n_layers: int)` — [`L623`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L623) — Count how many bucket-plan entries belong to each transformer block.
- <a id="is_wait_tensor_from_fsdp"></a>`is_wait_tensor_from_fsdp(node: torch.fx.Node)` — [`L121`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L121) — Returns True if the node is a wait_tensor node that is the result of an all_gather
- <a id="joint_transformer_block_bucketing_reordering_pass"></a>`joint_transformer_block_bucketing_reordering_pass(gm: torch.fx.GraphModule, example_inputs: tuple | None = None, *, module_bucket_plans: list[list[str] | str], insert_overlap_deps: bool = False, bucket_mode: BucketMode | None = None, fsdp_param_module_order: dict[str, int] | None = None)` — [`L543`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L543) — Run joint-graph manual bucketing and reordering.
- <a id="reassign_collective_pgs_pass"></a>`reassign_collective_pgs_pass(gm: torch.fx.GraphModule, example_inputs: tuple | None = None)` — [`L198`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L198) — Reassign collectives to dedicated NCCL process groups.
- <a id="schedule_fsdp_comms_to_dense_regions_pass"></a>`schedule_fsdp_comms_to_dense_regions_pass(gm: torch.fx.GraphModule, example_inputs: tuple[Any, ...] | None = None, *, moe_layer_ids: frozenset[int], n_layers: int, transformer_bucket_counts_by_layer: dict[int, int] | None = None, strict: bool = False)` — [`L1008`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L1008) — Schedule bucketed FSDP comms to overlap with dense (attention) regions. — documented in [tpu-graph-trainer](../../../../concepts/tpu-graph-trainer.md)
- <a id="transformer_block_bucketing_reordering_pass"></a>`transformer_block_bucketing_reordering_pass(gm: torch.fx.GraphModule, example_inputs: tuple | None = None, *, fsdp_manual_buckets)` — [`L249`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L249) — Apply aten-level manual bucketing and reordering optimization.

## Module values
- <a id="_EXTRA_FSDP_PG_REGISTRY._EXTRA_FSDP_PG_REGISTRY"></a>`_EXTRA_FSDP_PG_REGISTRY` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L139)
- <a id="_FSDP_BUCKET_META"></a>`_FSDP_BUCKET_META` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_passes.py#L55)

