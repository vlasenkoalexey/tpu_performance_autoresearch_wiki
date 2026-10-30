---
title: 'Module: torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.graph_pp.split_fsdp_collectives`/
symbols:
  split_forward_fsdp_collectives: split_forward_fsdp_collectives().
  split_backward_fsdp_collectives: split_backward_fsdp_collectives().
  GraphPPFSDPForwardSplit.unshard_module: GraphPPFSDPForwardSplit#unshard_module.
  GraphPPFSDPBackwardSplit.reduce_grad_module: GraphPPFSDPBackwardSplit#reduce_grad_module.
  GraphPPFSDPBackwardSplit.bw_no_fsdp_module: GraphPPFSDPBackwardSplit#bw_no_fsdp_module.
  GraphPPFSDPForwardSplit.fw_no_fsdp_module: GraphPPFSDPForwardSplit#fw_no_fsdp_module.
  GraphPPFSDPBackwardSplit.bw_no_fsdp_output_names: GraphPPFSDPBackwardSplit#bw_no_fsdp_output_names.
  GraphPPFSDPForwardSplit.fw_no_fsdp_flat_input_indices: GraphPPFSDPForwardSplit#fw_no_fsdp_flat_input_indices.
  GraphPPFSDPForwardSplit.unshard_flat_param_indices: GraphPPFSDPForwardSplit#unshard_flat_param_indices.
  GraphPPFSDPBackwardSplit.reduce_grad_input_names: GraphPPFSDPBackwardSplit#reduce_grad_input_names.
  GraphPPFSDPForwardSplit: GraphPPFSDPForwardSplit#
  GraphPPFSDPForwardSplit.fw_no_fsdp_input_names: GraphPPFSDPForwardSplit#fw_no_fsdp_input_names.
  GraphPPFSDPForwardSplit.num_fw_unsharded_param_inputs: GraphPPFSDPForwardSplit#num_fw_unsharded_param_inputs.
  GraphPPFSDPBackwardSplit: GraphPPFSDPBackwardSplit#
  GraphPPFSDPForwardSplit.unshard_output_names: GraphPPFSDPForwardSplit#unshard_output_names.
  GraphPPFSDPForwardSplit.fw_no_fsdp_output_names: GraphPPFSDPForwardSplit#fw_no_fsdp_output_names.
---
# Module: [`torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py)

## Classes
### <a id="GraphPPFSDPBackwardSplit"></a>`GraphPPFSDPBackwardSplit`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py:66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L66)
- doc: Backward graph split around FSDP/DDP/HSDP reduce-grad collectives.
- signature: `class GraphPPFSDPBackwardSplit:`
- members:
  - <a id="GraphPPFSDPBackwardSplit.bw_no_fsdp_module"></a>`bw_no_fsdp_module` — [`L82`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L82)
  - <a id="GraphPPFSDPBackwardSplit.bw_no_fsdp_output_names"></a>`bw_no_fsdp_output_names` — [`L84`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L84)
  - <a id="GraphPPFSDPBackwardSplit.reduce_grad_input_names"></a>`reduce_grad_input_names` — [`L85`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L85)
  - <a id="GraphPPFSDPBackwardSplit.reduce_grad_module"></a>`reduce_grad_module` — [`L83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L83)
- used by: [`_build_stage_graphs`](graph_builder.md#_build_stage_graphs), [`split_backward_fsdp_collectives`](split_fsdp_collectives.md#split_backward_fsdp_collectives)  (3 test-only)

### <a id="GraphPPFSDPForwardSplit"></a>`GraphPPFSDPForwardSplit`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py:31`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L31)
- doc: Forward graph split around FSDP unshard collectives.
- signature: `class GraphPPFSDPForwardSplit:`
- members:
  - <a id="GraphPPFSDPForwardSplit.fw_no_fsdp_flat_input_indices"></a>`fw_no_fsdp_flat_input_indices` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L60)
  - <a id="GraphPPFSDPForwardSplit.fw_no_fsdp_input_names"></a>`fw_no_fsdp_input_names` — [`L59`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L59)
  - <a id="GraphPPFSDPForwardSplit.fw_no_fsdp_module"></a>`fw_no_fsdp_module` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L56)
  - <a id="GraphPPFSDPForwardSplit.fw_no_fsdp_output_names"></a>`fw_no_fsdp_output_names` — [`L62`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L62)
  - <a id="GraphPPFSDPForwardSplit.num_fw_unsharded_param_inputs"></a>`num_fw_unsharded_param_inputs` — [`L61`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L61)
  - <a id="GraphPPFSDPForwardSplit.unshard_flat_param_indices"></a>`unshard_flat_param_indices` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L57)
  - <a id="GraphPPFSDPForwardSplit.unshard_module"></a>`unshard_module` — [`L55`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L55)
  - <a id="GraphPPFSDPForwardSplit.unshard_output_names"></a>`unshard_output_names` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L58)
- used by: [`_build_stage_graphs`](graph_builder.md#_build_stage_graphs), [`split_forward_fsdp_collectives`](split_fsdp_collectives.md#split_forward_fsdp_collectives)  (3 test-only)

## Functions
- <a id="split_backward_fsdp_collectives"></a>`split_backward_fsdp_collectives(bw_module: fx.GraphModule, *, num_param_grads: int)` — [`L246`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L246) — Split backward FSDP/DDP/HSDP reduce-grad epilogues.
- <a id="split_forward_fsdp_collectives"></a>`split_forward_fsdp_collectives(fw_module: fx.GraphModule, *, num_params: int, fwd_input_names: tuple[str, ...], fwd_flat_input_indices: tuple[int, ...])` — [`L88`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_fsdp_collectives.py#L88) — Split forward FSDP all-gather chains from a forward graph.

