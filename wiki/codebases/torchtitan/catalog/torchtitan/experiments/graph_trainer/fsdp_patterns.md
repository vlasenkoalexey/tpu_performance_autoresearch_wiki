---
title: 'Module: torchtitan/experiments/graph_trainer/fsdp_patterns.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/fsdp_patterns.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.fsdp_patterns`/
symbols:
  find_fsdp_unshard_outputs: find_fsdp_unshard_outputs().
  _unshard_output_from_all_gather: _unshard_output_from_all_gather().
  find_fsdp_unshard_save_nodes: find_fsdp_unshard_save_nodes().
  find_fsdp_reduce_grad_input: find_fsdp_reduce_grad_input().
  is_reduce_grad_collective: is_reduce_grad_collective().
  find_fsdp_unshard_output: find_fsdp_unshard_output().
  _find_last_all_gather_in_chain: _find_last_all_gather_in_chain().
  find_fsdp_unshard_save_node: find_fsdp_unshard_save_node().
  is_all_gather_into_tensor: is_all_gather_into_tensor().
  is_wait_tensor: is_wait_tensor().
  is_reduce_scatter_tensor: is_reduce_scatter_tensor().
  is_all_reduce: is_all_reduce().
  _find_last_user_in_wait_chain: _find_last_user_in_wait_chain().
  _find_last_non_view_node_in_chain: _find_last_non_view_node_in_chain().
---
# Module: [`torchtitan/experiments/graph_trainer/fsdp_patterns.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py)

## Functions
- <a id="_find_last_all_gather_in_chain"></a>`_find_last_all_gather_in_chain(start_node: fx.Node)` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L58) — Find the final all-gather in a linear FSDP unshard launch chain.
- <a id="_find_last_non_view_node_in_chain"></a>`_find_last_non_view_node_in_chain(node: fx.Node)` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L120) — Return the value GraphPP should pass across the unshard boundary.
- <a id="_find_last_user_in_wait_chain"></a>`_find_last_user_in_wait_chain(wait_node: fx.Node)` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L74) — Find the last FSDP unshard node before the value enters real compute.
- <a id="_unshard_output_from_all_gather"></a>`_unshard_output_from_all_gather(last_all_gather: fx.Node)` — [`L130`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L130)
- <a id="find_fsdp_reduce_grad_input"></a>`find_fsdp_reduce_grad_input(param_grad_output: Any)` — [`L202`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L202) — Return the split point before an FSDP reduce-grad epilogue.
- <a id="find_fsdp_unshard_output"></a>`find_fsdp_unshard_output(param_placeholder: fx.Node)` — [`L175`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L175) — Return the extracted unshard output for one flat parameter input.
- <a id="find_fsdp_unshard_outputs"></a>`find_fsdp_unshard_outputs(param_placeholder: fx.Node)` — [`L147`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L147) — Return all FSDP unshard outputs launched from one flat parameter input.
- <a id="find_fsdp_unshard_save_node"></a>`find_fsdp_unshard_save_node(param_placeholder: fx.Node)` — [`L193`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L193)
- <a id="find_fsdp_unshard_save_nodes"></a>`find_fsdp_unshard_save_nodes(param_placeholder: fx.Node)` — [`L197`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L197) — Return all FSDP unshard values that SAC must save for one parameter.
- <a id="is_all_gather_into_tensor"></a>`is_all_gather_into_tensor(node: fx.Node)` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L33)
- <a id="is_all_reduce"></a>`is_all_reduce(node: fx.Node)` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L47)
- <a id="is_reduce_grad_collective"></a>`is_reduce_grad_collective(node: fx.Node)` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L54)
- <a id="is_reduce_scatter_tensor"></a>`is_reduce_scatter_tensor(node: fx.Node)` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L40)
- <a id="is_wait_tensor"></a>`is_wait_tensor(node: fx.Node)` — [`L26`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/fsdp_patterns.py#L26)

