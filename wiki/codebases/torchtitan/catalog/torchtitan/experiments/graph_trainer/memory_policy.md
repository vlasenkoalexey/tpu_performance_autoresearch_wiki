---
title: 'Module: torchtitan/experiments/graph_trainer/memory_policy.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/memory_policy.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.memory_policy`/
symbols:
  tag_sac_policy: tag_sac_policy().
  _make_full_memory_policy: _make_full_memory_policy().
  _full_memory_policy_pass: _full_memory_policy_pass().
  tag_with_memory_policy_pass: tag_with_memory_policy_pass().
  validate_memory_policy_config: validate_memory_policy_config().
  _make_default_memory_policy: _make_default_memory_policy().
  _default_memory_policy_pass: _default_memory_policy_pass().
  _configured_fsdp_force_save_nodes: _configured_fsdp_force_save_nodes().
  _eager_memory_policy_pass: _eager_memory_policy_pass().
  _min_cut_memory_policy_pass: _min_cut_memory_policy_pass().
  _sac_and_offload_memory_policy_pass: _sac_and_offload_memory_policy_pass().
  _make_full_memory_policy.policy_fn: _make_full_memory_policy().policy_fn().
  _make_eager_memory_policy: _make_eager_memory_policy().
  _make_eager_memory_policy.policy_fn: _make_eager_memory_policy().policy_fn().
  _find_fsdp_unshard_save_nodes: _find_fsdp_unshard_save_nodes().
  _backward_side_nodes: _backward_side_nodes().
  tag_min_cut_saved_values: tag_min_cut_saved_values().
  tag_min_cut_saved_values.visit: tag_min_cut_saved_values().visit().
  _parse_full_recompute_save_ops: _parse_full_recompute_save_ops().
  _INF_DISTANCE: _INF_DISTANCE.
  _is_backward_side: _is_backward_side().
  _node_info_for_graph_trainer: _node_info_for_graph_trainer().
  tag_sac_policy._is_recomputable: tag_sac_policy()._is_recomputable().
  _make_default_memory_policy.policy_fn: _make_default_memory_policy().policy_fn().
  _resolve_op_target: _resolve_op_target().
---
# Module: [`torchtitan/experiments/graph_trainer/memory_policy.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py)

## Functions
- <a id="_backward_side_nodes"></a>`_backward_side_nodes(gm: torch.fx.GraphModule)` — [`L447`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L447)
- <a id="_configured_fsdp_force_save_nodes"></a>`_configured_fsdp_force_save_nodes(gm: torch.fx.GraphModule, config: GraphTrainer.Config)` — [`L144`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L144) — Return the unshard values SAC must save for an explicit Zero-2 policy.
- <a id="_default_memory_policy_pass"></a>`_default_memory_policy_pass(gm: torch.fx.GraphModule, *, config: GraphTrainer.Config)` — [`L397`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L397) — SAC policy that saves compute-intensive ops and required FSDP unshards.
- <a id="_eager_memory_policy_pass"></a>`_eager_memory_policy_pass(gm: torch.fx.GraphModule, *, config: GraphTrainer.Config)` — [`L427`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L427) — SAC policy that alternates mm ops between save/recompute.
- <a id="_find_fsdp_unshard_save_nodes"></a>`_find_fsdp_unshard_save_nodes(gm: torch.fx.GraphModule)` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L80)
- <a id="_full_memory_policy_pass"></a>`_full_memory_policy_pass(gm: torch.fx.GraphModule, *, config: GraphTrainer.Config)` — [`L412`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L412) — Full recompute except for user-selected module operations.
- <a id="_is_backward_side"></a>`_is_backward_side(node: torch.fx.Node, backward_side: set[torch.fx.Node])` — [`L441`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L441)
- <a id="tag_sac_policy._is_recomputable"></a>`_is_recomputable(n: torch.fx.Node)` — [`L339`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L339)
- <a id="_make_default_memory_policy"></a>`_make_default_memory_policy(save_ops: set | None = None)` — [`L67`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L67) — Create a SAC policy function from a set of op targets to save.
- <a id="_make_eager_memory_policy"></a>`_make_eager_memory_policy(save_ops: set | None = None)` — [`L203`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L203) — Eager-compatible SAC policy that alternates mm ops between save/recompute.
- <a id="_make_full_memory_policy"></a>`_make_full_memory_policy(save_ops: str = "")` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L165) — Full recompute policy: mark everything as MUST_RECOMPUTE.
- <a id="_min_cut_memory_policy_pass"></a>`_min_cut_memory_policy_pass(gm: torch.fx.GraphModule, *, config: GraphTrainer.Config)` — [`L560`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L560) — Choose saved activations with the min-cut partitioner.
- <a id="_node_info_for_graph_trainer"></a>`_node_info_for_graph_trainer(gm: torch.fx.GraphModule, backward_side: OrderedSet[torch.fx.Node])` — [`L457`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L457)
- <a id="_parse_full_recompute_save_ops"></a>`_parse_full_recompute_save_ops(value: str)` — [`L109`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L109) — Parse ``FQN::OP | FQN::OP`` save selectors.
- <a id="_resolve_op_target"></a>`_resolve_op_target(op_name: str)` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L87) — Resolve ``aten.mm.default``-style names through ``torch.ops``.
- <a id="_sac_and_offload_memory_policy_pass"></a>`_sac_and_offload_memory_policy_pass(gm: torch.fx.GraphModule, *, config: GraphTrainer.Config)` — [`L580`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L580) — SAC + CPU offload: apply default SAC, then offload within budget.
- <a id="_make_default_memory_policy.policy_fn"></a>`policy_fn(node: torch.fx.Node)` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L72)
- <a id="_make_full_memory_policy.policy_fn"></a>`policy_fn(node: torch.fx.Node)` — [`L189`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L189)
- <a id="_make_eager_memory_policy.policy_fn"></a>`policy_fn(node: torch.fx.Node)` — [`L221`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L221)
- <a id="tag_min_cut_saved_values"></a>`tag_min_cut_saved_values(gm: torch.fx.GraphModule, backward_side: OrderedSet[torch.fx.Node], saved_values: set[torch.fx.Node])` — [`L500`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L500)
- <a id="tag_sac_policy"></a>`tag_sac_policy(gm: torch.fx.GraphModule, example_inputs: tuple | None = None, *, policy_fn: Callable[[torch.fx.Node], CheckpointPolicy] | None = None, force_save_nodes: set[torch.fx.Node] | None = None)` — [`L239`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L239) — Apply selective activation checkpointing on the joint graph.
- <a id="tag_with_memory_policy_pass"></a>`tag_with_memory_policy_pass(gm: torch.fx.GraphModule, example_inputs: tuple | None = None, *, config: GraphTrainer.Config)` — [`L594`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L594) — Tag forward nodes with MUST_SAVE, PREFER_RECOMPUTE, or MUST_CPU_OFFLOAD.
- <a id="validate_memory_policy_config"></a>`validate_memory_policy_config(compile_config: GraphTrainerCompileConfig)` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L129) — Validate memory-policy options before tracing the training graph.
- <a id="tag_min_cut_saved_values.visit"></a>`visit(node: torch.fx.Node)` — [`L539`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L539)

## Module values
- <a id="_INF_DISTANCE"></a>`_INF_DISTANCE` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/memory_policy.py#L64)

