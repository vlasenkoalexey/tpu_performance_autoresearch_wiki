---
title: 'Module: torchtitan/experiments/graph_trainer/graph_pp/partition.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/graph_pp/partition.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.graph_pp.partition`/
symbols:
  partition_joint_graph: partition_joint_graph().
  _forward_mutations_to_materialize: _forward_mutations_to_materialize().
  _flatten_saved_values_for_backward: _flatten_saved_values_for_backward().
  GraphMeta.fwd_flat_input_indices: GraphMeta#fwd_flat_input_indices.
  GraphMeta.__post_init__: GraphMeta#__post_init__().
  _flatten_saved_values_for_backward.flatten_if_backward_uses_items: _flatten_saved_values_for_backward().flatten_if_backward_uses_items().
  GraphMeta: GraphMeta#
  GraphMeta.fwd_input_names: GraphMeta#fwd_input_names.
  GraphMeta.backward_grad_input_names: GraphMeta#backward_grad_input_names.
  GraphMeta.num_saved_for_backward: GraphMeta#num_saved_for_backward().
  GraphMeta.saved_for_backward_names: GraphMeta#saved_for_backward_names.
  GraphMeta.num_fwd_user_outputs: GraphMeta#num_fwd_user_outputs.
  GraphMeta.backward_grad_input_indices: GraphMeta#backward_grad_input_indices.
  GraphMeta.bwd_input_names: GraphMeta#bwd_input_names.
  GraphMeta.num_backward_grad_inputs: GraphMeta#num_backward_grad_inputs().
  GraphMeta.num_fwd_side_effect_outputs: GraphMeta#num_fwd_side_effect_outputs().
  GraphMeta.num_bwd_outputs: GraphMeta#num_bwd_outputs().
  _saved_values_for_backward: _saved_values_for_backward().
  _backward_passthrough_placeholders: _backward_passthrough_placeholders().
  _forward_inputs_from_outputs: _forward_inputs_from_outputs().
  _backward_grad_inputs_from_schedule: _backward_grad_inputs_from_schedule().
  GraphMeta.num_fwd_inputs: GraphMeta#num_fwd_inputs().
  GraphMeta.num_bwd_inputs: GraphMeta#num_bwd_inputs().
  GraphMeta.fwd_side_effect_output_names: GraphMeta#fwd_side_effect_output_names.
  GraphMeta.bwd_output_names: GraphMeta#bwd_output_names.
  _forward_flat_input_indices: _forward_flat_input_indices().
  _validate_backward_only_input_indices: _validate_backward_only_input_indices().
  _invalid_backward_only_value_names: _invalid_backward_only_value_names().
  _is_tuple_like_node: _is_tuple_like_node().
---
# Module: [`torchtitan/experiments/graph_trainer/graph_pp/partition.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py)

## Classes
### <a id="GraphMeta"></a>`GraphMeta`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/partition.py:97`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L97)
- doc: Calling convention for GraphTrainer-native GraphPP fwd/bwd graphs.
- signature: `class GraphMeta:`
- members:
  - <a id="GraphMeta.num_backward_grad_inputs"></a>`num_backward_grad_inputs(self)` — [`L180`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L180) — int: Number of backward placeholders supplied by the PP schedule.
  - <a id="GraphMeta.num_bwd_inputs"></a>`num_bwd_inputs(self)` — [`L175`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L175) — int: Number of backward graph placeholders.
  - <a id="GraphMeta.num_bwd_outputs"></a>`num_bwd_outputs(self)` — [`L185`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L185) — int: Number of backward graph outputs.
  - <a id="GraphMeta.num_fwd_inputs"></a>`num_fwd_inputs(self)` — [`L160`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L160) — int: Number of forward graph placeholders.
  - <a id="GraphMeta.num_fwd_side_effect_outputs"></a>`num_fwd_side_effect_outputs(self)` — [`L170`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L170) — int: Number of forward outputs kept only for side effects.
  - <a id="GraphMeta.num_saved_for_backward"></a>`num_saved_for_backward(self)` — [`L165`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L165) — int: Number of forward outputs saved for backward.
  - <a id="GraphMeta.backward_grad_input_indices"></a>`backward_grad_input_indices` — [`L140`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L140)
  - <a id="GraphMeta.backward_grad_input_names"></a>`backward_grad_input_names` — [`L139`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L139)
  - <a id="GraphMeta.bwd_input_names"></a>`bwd_input_names` — [`L141`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L141)
  - <a id="GraphMeta.bwd_output_names"></a>`bwd_output_names` — [`L142`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L142)
  - <a id="GraphMeta.fwd_flat_input_indices"></a>`fwd_flat_input_indices` — [`L135`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L135)
  - <a id="GraphMeta.fwd_input_names"></a>`fwd_input_names` — [`L134`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L134)
  - <a id="GraphMeta.fwd_side_effect_output_names"></a>`fwd_side_effect_output_names` — [`L138`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L138)
  - <a id="GraphMeta.num_fwd_user_outputs"></a>`num_fwd_user_outputs` — [`L136`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L136)
  - <a id="GraphMeta.saved_for_backward_names"></a>`saved_for_backward_names` — [`L137`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L137)
- protocol/private: <a id="GraphMeta.__post_init__"></a>`__post_init__`[`L144`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L144)
- used by: [`_build_stage_graphs`](graph_builder.md#_build_stage_graphs), [`partition_joint_graph`](partition.md#partition_joint_graph), [`_backward_args`](graph_builder.md#GraphTrainerStageGraphs._backward_args), [`partition`](graph_builder.md#_StageGraphMeta.partition)  (6 test-only)

## Functions
- <a id="_backward_grad_inputs_from_schedule"></a>`_backward_grad_inputs_from_schedule(backward_only_inputs: list[fx.Node], *, bwd_outputs: Sequence[object])` — [`L414`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L414) — Return schedule-supplied grad placeholders consumed by backward.
- <a id="_backward_passthrough_placeholders"></a>`_backward_passthrough_placeholders(*, bwd_outputs: Sequence[object], backward_only_names: set[str])` — [`L329`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L329) — Preserve metadata placeholders returned by backward directly.
- <a id="_flatten_saved_values_for_backward"></a>`_flatten_saved_values_for_backward(joint: fx.GraphModule, *, saved_values: list[fx.Node], bwd_outputs: Sequence[object])` — [`L357`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L357) — Expose saved tuple intermediates as tensor leaves.
- <a id="_forward_flat_input_indices"></a>`_forward_flat_input_indices(gm: fx.GraphModule, placeholder_index_by_name: dict[str, int])` — [`L190`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L190) — Map extracted forward placeholders to traced flat input positions.
- <a id="_forward_inputs_from_outputs"></a>`_forward_inputs_from_outputs(placeholders: list[fx.Node], *, fw_outputs: Sequence[object], backward_only_names: set[str])` — [`L395`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L395) — Select forward placeholders and reject backward-only dependencies.
- <a id="_forward_mutations_to_materialize"></a>`_forward_mutations_to_materialize(joint: fx.GraphModule, *, fwd_outputs: Sequence[object], bwd_outputs: Sequence[object], backward_only_names: set[str])` — [`L271`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L271) — Find forward-side mutations that must execute in the forward callable.
- <a id="_invalid_backward_only_value_names"></a>`_invalid_backward_only_value_names(values: Iterable[object], backward_only_names: set[str])` — [`L229`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L229) — Return backward-only placeholders that were selected for forward save.
- <a id="_is_tuple_like_node"></a>`_is_tuple_like_node(node: fx.Node)` — [`L353`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L353)
- <a id="_saved_values_for_backward"></a>`_saved_values_for_backward(joint: fx.GraphModule, *, fwd_outputs: Sequence[object], bwd_outputs: Sequence[object], backward_only_names: set[str])` — [`L244`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L244) — Select forward-computed values needed by the backward callable.
- <a id="_validate_backward_only_input_indices"></a>`_validate_backward_only_input_indices(indices: tuple[int, ...], *, num_placeholders: int)` — [`L207`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L207) — Validate caller-selected traced inputs that only backward may consume.
- <a id="_flatten_saved_values_for_backward.flatten_if_backward_uses_items"></a>`flatten_if_backward_uses_items(node: fx.Node)` — [`L375`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L375)
- <a id="partition_joint_graph"></a>`partition_joint_graph(traced: TracedResult, *, num_fwd_outputs: int, backward_only_input_indices: tuple[int, ...] = ())` — [`L439`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/partition.py#L439) — Partition a post-pass GraphTrainer joint graph into GraphPP callables.

