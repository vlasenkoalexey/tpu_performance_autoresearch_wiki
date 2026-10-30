---
title: 'Module: torchtitan/experiments/graph_trainer/graph_pp/stage.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/graph_pp/stage.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.graph_pp.stage`/
symbols:
  GraphPipelineStage: GraphPipelineStage#
  GraphPipelineStage.state: GraphPipelineStage#state.
  GraphPPStageRuntimeState.clear: GraphPPStageRuntimeState#clear().
  GraphPipelineStage.graphs: GraphPipelineStage#graphs.
  GraphPPOverlapGraphs: GraphPPOverlapGraphs#
  GraphPPStageRuntimeState.sharded_param_grads: GraphPPStageRuntimeState#sharded_param_grads.
  GraphPPStageGraphs: GraphPPStageGraphs#
  GraphPPStageRuntimeState.unsharded_param_values: GraphPPStageRuntimeState#unsharded_param_values.
  GraphPPStageRuntimeState.unsharded_param_grads: GraphPPStageRuntimeState#unsharded_param_grads.
  GraphPipelineStage.scale_grads: GraphPipelineStage#scale_grads().
  GraphPPStageRuntimeState: GraphPPStageRuntimeState#
  GraphPPStageRuntimeState.flat_buffer_values: GraphPPStageRuntimeState#flat_buffer_values.
  GraphPipelineStage.set_graphs: GraphPipelineStage#set_graphs().
  GraphPPStageGraphs.supports_backward_input_weight_split: GraphPPStageGraphs#supports_backward_input_weight_split().
  GraphPPStageGraphs.reduce_grads: GraphPPStageGraphs#reduce_grads().
  GraphPPStageRuntimeState.flat_param_values: GraphPPStageRuntimeState#flat_param_values.
  GraphPPStageRuntimeState.trainable_params: GraphPPStageRuntimeState#trainable_params.
  GraphPPStageGraphs.num_unsharded_param_grad_values: GraphPPStageGraphs#num_unsharded_param_grad_values().
  GraphPPStageGraphs.unshard_params: GraphPPStageGraphs#unshard_params().
  GraphPPStageGraphs.forward: GraphPPStageGraphs#forward().
  GraphPPStageGraphs.full_backward: GraphPPStageGraphs#full_backward().
  GraphPPStageGraphs.backward_input: GraphPPStageGraphs#backward_input().
  GraphPPStageGraphs.backward_weight: GraphPPStageGraphs#backward_weight().
  GraphPPStageGraphs.param_grads_for_accumulation: GraphPPStageGraphs#param_grads_for_accumulation().
  GraphPPOverlapGraphs.forward_backward: GraphPPOverlapGraphs#forward_backward().
  GraphPPStageGraphsProvider.prepare_graphs: GraphPPStageGraphsProvider#prepare_graphs().
  GraphPipelineStage._graph_pp_grads_scaled: GraphPipelineStage#_graph_pp_grads_scaled.
  GraphPPStageGraphsProvider: GraphPPStageGraphsProvider#
  GraphPipelineStage.saved_values_for_backward_weight_cache: GraphPipelineStage#saved_values_for_backward_weight_cache.
  GraphPipelineStage.__init__: GraphPipelineStage#__init__().
---
# Module: [`torchtitan/experiments/graph_trainer/graph_pp/stage.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py)

## Classes
### <a id="GraphPPOverlapGraphs"></a>`GraphPPOverlapGraphs`  ·  implements/extends Protocol
- def: [`torchtitan/experiments/graph_trainer/graph_pp/stage.py:199`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L199)
- doc: Bound graph execution contract for one `OVERLAP_F_B` stage pair.
- signature: `class GraphPPOverlapGraphs(Protocol):`
- members:
  - <a id="GraphPPOverlapGraphs.forward_backward"></a>`forward_backward(self, *, backward_stage_output: tuple[Any, ...], backward_saved_values_for_backward: tuple[Any, ...], output_grads_from_next: tuple[Any, ...], forward_args: tuple[Any, ...], forward_kwargs: dict[str, Any], forward_target: Any, forward_loss_kwargs: dict[str, Any], forward_unsharded_param_values: list[Any], forward_flat_buffer_values: list[Any], runtime_validate: bool = False)` — [`L202`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L202) — Run one multiplexed forward/backward graph pair.
- uses (calls/refs, reference-scoped): [`forward_backward`](graph_builder.md#GraphTrainerOverlapGraphs.forward_backward), [`GraphTrainerOverlapGraphs`](graph_builder.md#GraphTrainerOverlapGraphs)
- used by: [`_build_graph_pp_overlap_graphs`](graph_builder.md#_build_graph_pp_overlap_graphs), [`_handle_overlap_fw_bw`](runner.md#GraphPipelineRuntime._handle_overlap_fw_bw), [`prepare_graphs`](graph_builder.md#GraphTrainerStageGraphProvider.prepare_graphs), [`_overlap_graphs`](graph_builder.md#GraphTrainerStageGraphProvider._overlap_graphs), [`overlap_graphs`](runner.md#GraphPipelineRuntime.overlap_graphs), [`GraphTrainerOverlapGraphs`](graph_builder.md#GraphTrainerOverlapGraphs), [`prepare_graphs`](stage.md#GraphPPStageGraphsProvider.prepare_graphs)

### <a id="GraphPPStageGraphs"></a>`GraphPPStageGraphs`  ·  implements/extends Protocol
- def: [`torchtitan/experiments/graph_trainer/graph_pp/stage.py:21`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L21)
- doc: Bound graph execution contract for one GraphPP pipeline stage.
- signature: `class GraphPPStageGraphs(Protocol):`
- members:
  - <a id="GraphPPStageGraphs.backward_input"></a>`backward_input(self, stage_output: tuple[Any, ...], saved_values_for_backward: tuple[Any, ...], output_grads_from_next: tuple[Any, ...], *, runtime_validate: bool = False)` — [`L126`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L126) — Run the input-gradient half of split backward.
  - <a id="GraphPPStageGraphs.backward_weight"></a>`backward_weight(self, saved_values_for_backward_weight: tuple[Any, ...])` — [`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L151) — Run the weight-gradient half of split backward.
  - <a id="GraphPPStageGraphs.forward"></a>`forward(self, args: tuple[Any, ...], kwargs: dict[str, Any], target: Any, loss_kwargs: dict[str, Any], *, unsharded_param_values: list[Any], flat_buffer_values: list[Any], runtime_validate: bool = False)` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L67) — Run the stage forward graph.
  - <a id="GraphPPStageGraphs.full_backward"></a>`full_backward(self, stage_output: tuple[Any, ...], saved_values_for_backward: tuple[Any, ...], output_grads_from_next: tuple[Any, ...], *, runtime_validate: bool = False)` — [`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L101) — Run the full backward graph for one microbatch.
  - <a id="GraphPPStageGraphs.num_unsharded_param_grad_values"></a>`num_unsharded_param_grad_values(self)` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L40) — Return the number of unsharded param-grad accumulator slots.
  - <a id="GraphPPStageGraphs.param_grads_for_accumulation"></a>`param_grads_for_accumulation(self, sharded_param_grads: list[Any])` — [`L183`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L183) — Prepare parameter gradients for accumulation on model parameters.
  - <a id="GraphPPStageGraphs.reduce_grads"></a>`reduce_grads(self, unsharded_param_grads: list[Any], *, runtime_validate: bool = False)` — [`L165`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L165) — Reduce unsharded parameter gradients.
  - <a id="GraphPPStageGraphs.supports_backward_input_weight_split"></a>`supports_backward_input_weight_split(self)` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L30) — Return whether backward input and weight graphs are separate.
  - <a id="GraphPPStageGraphs.unshard_params"></a>`unshard_params(self, flat_param_values: list[Any], *, runtime_validate: bool = False)` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L48) — Materialize parameter values consumed by forward graphs.
- uses (calls/refs, reference-scoped): [`backward_input`](graph_builder.md#GraphTrainerStageGraphs.backward_input), [`reduce_grads`](graph_builder.md#GraphTrainerStageGraphs.reduce_grads), [`forward`](graph_builder.md#GraphTrainerStageGraphs.forward), [`unshard_params`](graph_builder.md#GraphTrainerStageGraphs.unshard_params), [`full_backward`](graph_builder.md#GraphTrainerStageGraphs.full_backward), [`GraphTrainerStageGraphs`](graph_builder.md#GraphTrainerStageGraphs), [`backward_weight`](graph_builder.md#GraphTrainerStageGraphs.backward_weight), [`param_grads_for_accumulation`](graph_builder.md#GraphTrainerStageGraphs.param_grads_for_accumulation), [`supports_backward_input_weight_split`](graph_builder.md#GraphTrainerStageGraphs.supports_backward_input_weight_split), [`num_unsharded_param_grad_values`](graph_builder.md#GraphTrainerStageGraphs.num_unsharded_param_grad_values)
- used by: [`_populate_stage_states`](runner.md#GraphPipelineRuntime._populate_stage_states), [`_handle_forward`](runner.md#GraphPipelineRuntime._handle_forward), [`_handle_backward_input`](runner.md#GraphPipelineRuntime._handle_backward_input), [`_handle_backward_weight`](runner.md#GraphPipelineRuntime._handle_backward_weight), [`_handle_reduce_grad`](runner.md#GraphPipelineRuntime._handle_reduce_grad), [`_handle_full_backward`](runner.md#GraphPipelineRuntime._handle_full_backward), [`stage_graphs`](runner.md#GraphPipelineRuntime.stage_graphs), [`_accumulate_stage_sharded_grads`](runner.md#GraphPipelineRuntime._accumulate_stage_sharded_grads), [`_ensure_reduced_grads`](runner.md#GraphPipelineRuntime._ensure_reduced_grads), [`_ensure_unsharded_param_values`](runner.md#_ensure_unsharded_param_values), [`graphs`](stage.md#GraphPipelineStage.graphs), [`GraphTrainerStageGraphs`](graph_builder.md#GraphTrainerStageGraphs), [`set_graphs`](stage.md#GraphPipelineStage.set_graphs)

### <a id="GraphPPStageGraphsProvider"></a>`GraphPPStageGraphsProvider`  ·  implements/extends Protocol
- def: [`torchtitan/experiments/graph_trainer/graph_pp/stage.py:247`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L247)
- doc: Build or attach stage graphs before GraphPP runtime execution.
- signature: `class GraphPPStageGraphsProvider(Protocol):`
- members:
  - <a id="GraphPPStageGraphsProvider.prepare_graphs"></a>`prepare_graphs(self, schedule: _PipelineScheduleRuntime, ctx: _PipelineContext, *, loss_kwargs: dict[str, Any])` — [`L250`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L250) — Prepare every local GraphPP stage for runtime execution.
- uses (calls/refs, reference-scoped): [`GraphPPOverlapGraphs`](stage.md#GraphPPOverlapGraphs)
- used by: [`ensure_ready`](runner.md#GraphPipelineRuntime.ensure_ready), [`register_graph_pp_schedule`](runner.md#register_graph_pp_schedule), [`__init__`](runner.md#GraphPipelineRuntime.__init__)

### <a id="GraphPPStageRuntimeState"></a>`GraphPPStageRuntimeState`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/stage.py:275`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L275)
- doc: Mutable per-step runtime state for a `GraphPipelineStage`.
- signature: `class GraphPPStageRuntimeState:`
- members:
  - <a id="GraphPPStageRuntimeState.clear"></a>`clear(self)` — [`L300`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L300) — Clear all per-step runtime values.
  - <a id="GraphPPStageRuntimeState.flat_buffer_values"></a>`flat_buffer_values` — [`L294`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L294)
  - <a id="GraphPPStageRuntimeState.flat_param_values"></a>`flat_param_values` — [`L293`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L293)
  - <a id="GraphPPStageRuntimeState.sharded_param_grads"></a>`sharded_param_grads` — [`L297`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L297)
  - <a id="GraphPPStageRuntimeState.trainable_params"></a>`trainable_params` — [`L298`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L298)
  - <a id="GraphPPStageRuntimeState.unsharded_param_grads"></a>`unsharded_param_grads` — [`L296`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L296)
  - <a id="GraphPPStageRuntimeState.unsharded_param_values"></a>`unsharded_param_values` — [`L295`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L295)
- used by: [`_handle_overlap_fw_bw`](runner.md#GraphPipelineRuntime._handle_overlap_fw_bw), [`state`](stage.md#GraphPipelineStage.state), [`_populate_stage_states`](runner.md#GraphPipelineRuntime._populate_stage_states), [`_handle_forward`](runner.md#GraphPipelineRuntime._handle_forward), [`_handle_reduce_grad`](runner.md#GraphPipelineRuntime._handle_reduce_grad), [`_accumulate_stage_sharded_grads`](runner.md#GraphPipelineRuntime._accumulate_stage_sharded_grads), [`_ensure_reduced_grads`](runner.md#GraphPipelineRuntime._ensure_reduced_grads), [`step`](runner.md#GraphPipelineRuntime.step), [`eval`](runner.md#GraphPipelineRuntime.eval), [`_ensure_unsharded_param_values`](runner.md#_ensure_unsharded_param_values), [`_scale_graph_pp_sharded_grads`](runner.md#_scale_graph_pp_sharded_grads), [`_handle_reshard`](runner.md#GraphPipelineRuntime._handle_reshard), [`_accumulate_stage_unsharded_grads`](runner.md#_accumulate_stage_unsharded_grads), [`scale_grads`](stage.md#GraphPipelineStage.scale_grads)  (4 test-only)

### <a id="GraphPipelineStage"></a>`GraphPipelineStage`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/stage.py:310`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L310) — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)
- doc: Pipeline stage whose compute actions are backed by explicit graphs.
- signature: `class GraphPipelineStage(PipelineStage):`
- members:
  - <a id="GraphPipelineStage.scale_grads"></a>`scale_grads(self, grad_scale_factor: int)` — [`L372`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L372) — Scale accumulated graph gradients with upstream PP semantics.
  - <a id="GraphPipelineStage.set_graphs"></a>`set_graphs(self, graphs: GraphPPStageGraphs)` — [`L359`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L359) — Attach a bound graph executor to this stage.
  - <a id="GraphPipelineStage.graphs"></a>`graphs` — [`L354`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L354)
  - <a id="GraphPipelineStage.saved_values_for_backward_weight_cache"></a>`saved_values_for_backward_weight_cache` — [`L356`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L356)
  - <a id="GraphPipelineStage.state"></a>`state` — [`L355`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L355)
- protocol/private: <a id="GraphPipelineStage.__init__"></a>`__init__`[`L332`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L332), <a id="GraphPipelineStage._graph_pp_grads_scaled"></a>`_graph_pp_grads_scaled`[`L357`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/stage.py#L357)
- uses (calls/refs, reference-scoped): [`sharded_param_grads`](stage.md#GraphPPStageRuntimeState.sharded_param_grads), [`GraphPPStageGraphs`](stage.md#GraphPPStageGraphs), [`unsharded_param_grads`](stage.md#GraphPPStageRuntimeState.unsharded_param_grads), [`GraphPPStageRuntimeState`](stage.md#GraphPPStageRuntimeState)
- used by: [`_build_stage_graphs`](graph_builder.md#_build_stage_graphs), [`graph_pipeline_llm`](pipeline.md#graph_pipeline_llm), [`_build_graph_pp_overlap_graphs`](graph_builder.md#_build_graph_pp_overlap_graphs), [`_apply_graph_pp_pre_partition_passes`](graph_builder.md#_apply_graph_pp_pre_partition_passes), [`_handle_overlap_fw_bw`](runner.md#GraphPipelineRuntime._handle_overlap_fw_bw), [`prepare_graphs`](graph_builder.md#GraphTrainerStageGraphProvider.prepare_graphs), [`_compile_stage_graphs`](graph_builder.md#_compile_stage_graphs), [`ensure_ready`](runner.md#GraphPipelineRuntime.ensure_ready), [`_populate_stage_states`](runner.md#GraphPipelineRuntime._populate_stage_states), [`_handle_forward`](runner.md#GraphPipelineRuntime._handle_forward), [`_handle_backward_input`](runner.md#GraphPipelineRuntime._handle_backward_input), [`_handle_backward_weight`](runner.md#GraphPipelineRuntime._handle_backward_weight), [`_handle_reduce_grad`](runner.md#GraphPipelineRuntime._handle_reduce_grad), [`_accumulate_stage_sharded_grads`](runner.md#GraphPipelineRuntime._accumulate_stage_sharded_grads), [`_ensure_reduced_grads`](runner.md#GraphPipelineRuntime._ensure_reduced_grads), [`step`](runner.md#GraphPipelineRuntime.step), [`eval`](runner.md#GraphPipelineRuntime.eval), [`_ensure_unsharded_param_values`](runner.md#_ensure_unsharded_param_values), [`_graph_pp_ready`](runner.md#GraphPipelineRuntime._graph_pp_ready), [`_scale_graph_pp_sharded_grads`](runner.md#_scale_graph_pp_sharded_grads), [`_handle_reshard`](runner.md#GraphPipelineRuntime._handle_reshard), [`_accumulate_stage_unsharded_grads`](runner.md#_accumulate_stage_unsharded_grads), [`_stage_map_and_stage_from_action`](runner.md#_stage_map_and_stage_from_action), [`_prepare_backward_common`](runner.md#_prepare_backward_common), [`_prepare_fwd_common`](runner.md#_prepare_fwd_common), [`_post_fwd_common`](runner.md#_post_fwd_common), [`_prepare_fwd_user_args`](runner.md#_prepare_fwd_user_args), [`_trace_args_for_stage`](graph_builder.md#_trace_args_for_stage), [`_post_backward_common`](runner.md#_post_backward_common), [`_prepare_backward_values`](runner.md#_prepare_backward_values), [`_example_args_from_stage_metadata`](graph_builder.md#_example_args_from_stage_metadata), [`_flat_output_grads_from_stage_metadata`](graph_builder.md#_flat_output_grads_from_stage_metadata), [`_trace_target_from_context`](graph_builder.md#_trace_target_from_context)

