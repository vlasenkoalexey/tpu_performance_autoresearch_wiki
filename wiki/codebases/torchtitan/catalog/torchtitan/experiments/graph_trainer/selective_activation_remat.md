---
title: 'Module: torchtitan/experiments/graph_trainer/selective_activation_remat.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/selective_activation_remat.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.selective_activation_remat`/
symbols:
  selective_activation_remat_pass: selective_activation_remat_pass().
  _collect_backward_regions: _collect_backward_regions().
  selective_activation_remat_pass.ensure_offload_chain_before: selective_activation_remat_pass().ensure_offload_chain_before().
  selective_activation_remat_pass.collect_fw_nodes_to_recompute_for._gather: selective_activation_remat_pass().collect_fw_nodes_to_recompute_for()._gather().
  selective_activation_remat_pass.collect_fw_nodes_to_recompute_for: selective_activation_remat_pass().collect_fw_nodes_to_recompute_for().
  selective_activation_remat_pass.duplicate_subgraph_get_attrs: selective_activation_remat_pass().duplicate_subgraph_get_attrs().
  selective_activation_remat_pass.remat_and_dup_get_attr: selective_activation_remat_pass().remat_and_dup_get_attr().
  log: log.
  selective_activation_remat_pass.remat_input: selective_activation_remat_pass().remat_input().
  _privatize_custom_meta: _privatize_custom_meta().
  _NON_AC_MODULE_FQNS: _NON_AC_MODULE_FQNS.
---
# Module: [`torchtitan/experiments/graph_trainer/selective_activation_remat.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/selective_activation_remat.py)

## Functions
- <a id="_collect_backward_regions"></a>`_collect_backward_regions(gm: fx.GraphModule)` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/selective_activation_remat.py#L53) — Returns (bwd_start, bwd_end, needs_remat) for each model-layer backward region.
- <a id="selective_activation_remat_pass.collect_fw_nodes_to_recompute_for._gather"></a>`_gather(n: fx.Node)` — [`L170`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/selective_activation_remat.py#L170)
- <a id="_privatize_custom_meta"></a>`_privatize_custom_meta(node: fx.Node)` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/selective_activation_remat.py#L30) — Give ``node`` its own ``meta["custom"]`` dict.
- <a id="selective_activation_remat_pass.collect_fw_nodes_to_recompute_for"></a>`collect_fw_nodes_to_recompute_for(bwd_node: fx.Node)` — [`L167`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/selective_activation_remat.py#L167)
- <a id="selective_activation_remat_pass.duplicate_subgraph_get_attrs"></a>`duplicate_subgraph_get_attrs(fwd_node: fx.Node, bwd_target: fx.Node)` — [`L315`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/selective_activation_remat.py#L315) — Give a recompute dup private copies of its subgraph get_attr inputs.
- <a id="selective_activation_remat_pass.ensure_offload_chain_before"></a>`ensure_offload_chain_before(reload_node: fx.Node, target: fx.Node)` — [`L224`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/selective_activation_remat.py#L224) — Move ``reload_node`` and its bwd-region deps in front of ``target``.
- <a id="selective_activation_remat_pass.remat_and_dup_get_attr"></a>`remat_and_dup_get_attr(x: object, _dups=get_attr_dups)` — [`L360`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/selective_activation_remat.py#L360)
- <a id="selective_activation_remat_pass.remat_input"></a>`remat_input(x: object)` — [`L302`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/selective_activation_remat.py#L302) — Arg-transform: redirect must_recompute originals to their dups, and
- <a id="selective_activation_remat_pass"></a>`selective_activation_remat_pass(gm: fx.GraphModule, example_inputs: Any = None)` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/selective_activation_remat.py#L101) — In-place remat: insert recompute duplicates before backward consumers. — documented in [tpu-graph-trainer](../../../../concepts/tpu-graph-trainer.md)

## Module values
- <a id="_NON_AC_MODULE_FQNS"></a>`_NON_AC_MODULE_FQNS` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/selective_activation_remat.py#L50)
- <a id="log"></a>`log` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/selective_activation_remat.py#L27)

