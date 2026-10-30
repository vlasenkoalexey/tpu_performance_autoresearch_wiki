---
title: 'Module: torchtitan/experiments/tpu/graph_trainer/remat_schedule.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/graph_trainer/remat_schedule.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.graph_trainer.remat_schedule`/
symbols:
  apply_tpu_remat_schedule: apply_tpu_remat_schedule().
  apply_tpu_remat_fsdp_all_gather_schedule: apply_tpu_remat_fsdp_all_gather_schedule().
  apply_tpu_fsdp_rs_deadline_schedule: apply_tpu_fsdp_rs_deadline_schedule().
  _collect_rs_wait_deadlines: _collect_rs_wait_deadlines().
  _collect_fsdp_all_gather_barriers: _collect_fsdp_all_gather_barriers().
  _ordering_gradient: _ordering_gradient().
  _TPU_REMAT_BARRIER_KIND_META: _TPU_REMAT_BARRIER_KIND_META.
  _optimization_barrier: _optimization_barrier().
  _TPU_FSDP_RS_DEADLINE_META: _TPU_FSDP_RS_DEADLINE_META.
  _TPU_REMAT_REGION_ID_META: _TPU_REMAT_REGION_ID_META.
  _TPU_REMAT_LAYER_ENTRY_ANCHOR_META: _TPU_REMAT_LAYER_ENTRY_ANCHOR_META.
  _is_tensor_node: _is_tensor_node().
  apply_tpu_remat_schedule.depends_on_nonstatic_input: apply_tpu_remat_schedule().depends_on_nonstatic_input().
  apply_tpu_remat_fsdp_all_gather_schedule.depends_on_model_state: apply_tpu_remat_fsdp_all_gather_schedule().depends_on_model_state().
  _parameter_layer_id: _parameter_layer_id().
  _is_recomputed: _is_recomputed().
  _EXPERT_FQN_INFIX: _EXPERT_FQN_INFIX.
  _find_local_grad_before_reduce_dtype_cast: _find_local_grad_before_reduce_dtype_cast().
  _depends_on: _depends_on().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/graph_trainer/remat_schedule.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py)

## Functions
- <a id="_collect_fsdp_all_gather_barriers"></a>`_collect_fsdp_all_gather_barriers(gm: torch.fx.GraphModule)` — [`L640`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L640)
- <a id="_collect_rs_wait_deadlines"></a>`_collect_rs_wait_deadlines(gm: torch.fx.GraphModule, barrier_by_region: dict[int, torch.fx.Node], *, n_layers: int)` — [`L665`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L665) — Assign RS waits to the next transformer-layer AG bundle in FX order.
- <a id="_depends_on"></a>`_depends_on(node: torch.fx.Node, dependency: torch.fx.Node)` — [`L702`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L702) — Return whether adding dependency -> node would create a cycle.
- <a id="_find_local_grad_before_reduce_dtype_cast"></a>`_find_local_grad_before_reduce_dtype_cast(reduce_grad_input: torch.fx.Node)` — [`L65`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L65) — Match the expert BF16 dWeight before its FP32 FSDP reduction cast.
- <a id="_is_recomputed"></a>`_is_recomputed(node: torch.fx.Node)` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L60) — Whether selective_activation_remat_pass added this node as a recompute.
- <a id="_is_tensor_node"></a>`_is_tensor_node(node: torch.fx.Node)` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L56)
- <a id="_optimization_barrier"></a>`_optimization_barrier(*values: torch.Tensor)` — [`L42`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L42)
- <a id="_ordering_gradient"></a>`_ordering_gradient(gradient: torch.fx.Node, parameter_fqns: tuple[str, ...])` — [`L115`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L115)
- <a id="_parameter_layer_id"></a>`_parameter_layer_id(parameter_fqns: tuple[str, ...])` — [`L98`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L98)
- <a id="apply_tpu_fsdp_rs_deadline_schedule"></a>`apply_tpu_fsdp_rs_deadline_schedule(gm: torch.fx.GraphModule, example_inputs: tuple, *, n_layers: int, strict: bool = False)` — [`L716`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L716) — Keep TPU LHS from moving later backward AGs ahead of scheduled RSs. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="apply_tpu_remat_fsdp_all_gather_schedule"></a>`apply_tpu_remat_fsdp_all_gather_schedule(gm: torch.fx.GraphModule, example_inputs: tuple, *, num_static_inputs: int, prefetch_distance: int = 1)` — [`L401`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L401) — Keep recomputed FSDP unshards distinct and eligible for prefetch. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="apply_tpu_remat_schedule"></a>`apply_tpu_remat_schedule(gm: torch.fx.GraphModule, example_inputs: tuple, *, num_static_inputs: int)` — [`L137`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L137) — Keep each layer's parameter gradients adjacent to its recomputation. — documented in [tpu-graph-trainer](../../../../../concepts/tpu-graph-trainer.md)
- <a id="apply_tpu_remat_fsdp_all_gather_schedule.depends_on_model_state"></a>`depends_on_model_state(node: torch.fx.Node)` — [`L442`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L442) — Whether ``node`` derives from GraphTrainer parameter/buffer inputs.
- <a id="apply_tpu_remat_schedule.depends_on_nonstatic_input"></a>`depends_on_nonstatic_input(node: torch.fx.Node)` — [`L194`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L194)

## Module values
- <a id="_EXPERT_FQN_INFIX"></a>`_EXPERT_FQN_INFIX` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L39)
- <a id="_TPU_FSDP_RS_DEADLINE_META"></a>`_TPU_FSDP_RS_DEADLINE_META` — [`L36`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L36)
- <a id="_TPU_REMAT_BARRIER_KIND_META"></a>`_TPU_REMAT_BARRIER_KIND_META` — [`L33`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L33)
- <a id="_TPU_REMAT_LAYER_ENTRY_ANCHOR_META"></a>`_TPU_REMAT_LAYER_ENTRY_ANCHOR_META` — [`L35`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L35)
- <a id="_TPU_REMAT_REGION_ID_META"></a>`_TPU_REMAT_REGION_ID_META` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L34)
- <a id="__all__"></a>`__all__` — [`L803`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/graph_trainer/remat_schedule.py#L803)

