---
title: 'Module: torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.graph_pp.split_di_dw`/
symbols:
  split_di_dw_graph: split_di_dw_graph().
  GraphPPDiDwSplit.num_input_grads: GraphPPDiDwSplit#num_input_grads.
  _collect_saved_values_for_dw: _collect_saved_values_for_dw().
  GraphPPDiDwSplit: GraphPPDiDwSplit#
  GraphPPDiDwSplit.bw_di_module: GraphPPDiDwSplit#bw_di_module.
  GraphPPDiDwSplit.bw_dw_module: GraphPPDiDwSplit#bw_dw_module.
  GraphPPDiDwSplit.bw_dw_input_names: GraphPPDiDwSplit#bw_dw_input_names.
  GraphPPDiDwSplit.bw_di_input_names: GraphPPDiDwSplit#bw_di_input_names.
  GraphPPDiDwSplit.bw_di_output_names: GraphPPDiDwSplit#bw_di_output_names.
  GraphPPDiDwSplit.bw_dw_output_names: GraphPPDiDwSplit#bw_dw_output_names.
  _reorder_backward_outputs_for_di: _reorder_backward_outputs_for_di().
---
# Module: [`torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py)

## Classes
### <a id="GraphPPDiDwSplit"></a>`GraphPPDiDwSplit`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py:30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py#L30)
- doc: Backward graph split into dI and dW GraphPP callables.
- signature: `class GraphPPDiDwSplit:`
- members:
  - <a id="GraphPPDiDwSplit.bw_di_input_names"></a>`bw_di_input_names` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py#L52)
  - <a id="GraphPPDiDwSplit.bw_di_module"></a>`bw_di_module` — [`L49`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py#L49)
  - <a id="GraphPPDiDwSplit.bw_di_output_names"></a>`bw_di_output_names` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py#L53)
  - <a id="GraphPPDiDwSplit.bw_dw_input_names"></a>`bw_dw_input_names` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py#L54)
  - <a id="GraphPPDiDwSplit.bw_dw_module"></a>`bw_dw_module` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py#L50)
  - <a id="GraphPPDiDwSplit.bw_dw_output_names"></a>`bw_dw_output_names` — [`L55`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py#L55)
  - <a id="GraphPPDiDwSplit.num_input_grads"></a>`num_input_grads` — [`L51`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py#L51)
- used by: [`_build_stage_graphs`](graph_builder.md#_build_stage_graphs), [`split_di_dw_graph`](split_di_dw.md#split_di_dw_graph)  (1 test-only)

## Functions
- <a id="_collect_saved_values_for_dw"></a>`_collect_saved_values_for_dw(bw_gm: fx.GraphModule, di_graph: fx.Graph, dw_output_nodes: list[fx.Node] | None = None)` — [`L89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py#L89)
- <a id="_reorder_backward_outputs_for_di"></a>`_reorder_backward_outputs_for_di(gm: fx.GraphModule, *, num_param_grads: int)` — [`L58`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py#L58)
- <a id="split_di_dw_graph"></a>`split_di_dw_graph(bw_module: fx.GraphModule, *, num_param_grads: int)` — [`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/split_di_dw.py#L151) — Split a backward graph into input-gradient and weight-gradient graphs.

