---
title: 'Module: torchtitan/experiments/graph_trainer/graph_pp/runner.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/graph_pp/runner.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.graph_pp.runner`/
symbols:
  GraphPipelineRuntime._handle_overlap_fw_bw: GraphPipelineRuntime#_handle_overlap_fw_bw().
  GraphPipelineRuntime.ensure_ready: GraphPipelineRuntime#ensure_ready().
  GraphPipelineRuntime._populate_stage_states: GraphPipelineRuntime#_populate_stage_states().
  GraphPipelineRuntime._handle_forward: GraphPipelineRuntime#_handle_forward().
  GraphPipelineRuntime._handle_backward_input: GraphPipelineRuntime#_handle_backward_input().
  register_graph_pp_schedule: register_graph_pp_schedule().
  GraphPipelineRuntime.schedule: GraphPipelineRuntime#schedule.
  GraphPipelineRuntime._handle_backward_weight: GraphPipelineRuntime#_handle_backward_weight().
  GraphPipelineRuntime._handle_reduce_grad: GraphPipelineRuntime#_handle_reduce_grad().
  GraphPipelineRuntime._handle_full_backward: GraphPipelineRuntime#_handle_full_backward().
  GraphPipelineRuntime.stage_graphs: GraphPipelineRuntime#stage_graphs.
  GraphPipelineRuntime._ensure_reduced_grads: GraphPipelineRuntime#_ensure_reduced_grads().
  GraphPipelineRuntime._accumulate_stage_sharded_grads: GraphPipelineRuntime#_accumulate_stage_sharded_grads().
  GraphPipelineRuntime.step: GraphPipelineRuntime#step().
  GraphPipelineRuntime.eval: GraphPipelineRuntime#eval().
  _ensure_unsharded_param_values: _ensure_unsharded_param_values().
  GraphPipelineRuntime._graph_pp_ready: GraphPipelineRuntime#_graph_pp_ready.
  _scale_graph_pp_sharded_grads: _scale_graph_pp_sharded_grads().
  GraphPipelineRuntime._handle_unshard: GraphPipelineRuntime#_handle_unshard().
  GraphPipelineRuntime._handle_reshard: GraphPipelineRuntime#_handle_reshard().
  _accumulate_stage_unsharded_grads: _accumulate_stage_unsharded_grads().
  GraphPipelineRuntime: GraphPipelineRuntime#
  GraphPipelineRuntime.loss_kwargs: GraphPipelineRuntime#loss_kwargs.
  _stage_map_and_stage_from_action: _stage_map_and_stage_from_action().
  _prepare_backward_common: _prepare_backward_common().
  GraphPipelineRuntime.overlap_graphs: GraphPipelineRuntime#overlap_graphs.
  _prepare_fwd_common: _prepare_fwd_common().
  _prepare_fwd_user_args: _prepare_fwd_user_args().
  _post_fwd_common: _post_fwd_common().
  _prepare_backward_values: _prepare_backward_values().
  _post_backward_common: _post_backward_common().
  GraphPipelineRuntime.graph_provider: GraphPipelineRuntime#graph_provider.
  GraphPipelineRuntime.__init__: GraphPipelineRuntime#__init__().
  _scale_grad_values_: _scale_grad_values_().
  _accumulate_flat_grad_values_: _accumulate_flat_grad_values_().
  __all__: __all__.
---
# Module: [`torchtitan/experiments/graph_trainer/graph_pp/runner.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py)

## Classes
### <a id="GraphPipelineRuntime"></a>`GraphPipelineRuntime`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/runner.py:306`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L306) — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)
- doc: Execute a runtime PP schedule with GraphPP stage graph handlers.
- signature: `class GraphPipelineRuntime:`
- members:
  - <a id="GraphPipelineRuntime.ensure_ready"></a>`ensure_ready(self, ctx: _PipelineContext)` — [`L361`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L361) — Ensure local stage graphs and runtime state are ready for execution.
  - <a id="GraphPipelineRuntime.eval"></a>`eval(self, *args: Any, **kwargs: Any)` — [`L681`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L681) — Run evaluation through the wrapped pipeline schedule.
  - <a id="GraphPipelineRuntime.step"></a>`step(self, *args: Any, **kwargs: Any)` — [`L656`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L656) — Run one training step through the wrapped pipeline schedule.
  - <a id="GraphPipelineRuntime.graph_provider"></a>`graph_provider` — [`L348`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L348)
  - <a id="GraphPipelineRuntime.loss_kwargs"></a>`loss_kwargs` — [`L351`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L351)
  - <a id="GraphPipelineRuntime.overlap_graphs"></a>`overlap_graphs` — [`L349`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L349)
  - <a id="GraphPipelineRuntime.schedule"></a>`schedule` — [`L347`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L347)
  - <a id="GraphPipelineRuntime.stage_graphs"></a>`stage_graphs` — [`L350`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L350)
- protocol/private: <a id="GraphPipelineRuntime.__init__"></a>`__init__`[`L341`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L341), <a id="GraphPipelineRuntime._accumulate_stage_sharded_grads"></a>`_accumulate_stage_sharded_grads`[`L426`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L426), <a id="GraphPipelineRuntime._ensure_reduced_grads"></a>`_ensure_reduced_grads`[`L414`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L414), <a id="GraphPipelineRuntime._graph_pp_ready"></a>`_graph_pp_ready`[`L352`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L352), <a id="GraphPipelineRuntime._handle_backward_input"></a>`_handle_backward_input`[`L497`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L497), <a id="GraphPipelineRuntime._handle_backward_weight"></a>`_handle_backward_weight`[`L537`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L537), <a id="GraphPipelineRuntime._handle_forward"></a>`_handle_forward`[`L436`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L436), <a id="GraphPipelineRuntime._handle_full_backward"></a>`_handle_full_backward`[`L466`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L466), <a id="GraphPipelineRuntime._handle_overlap_fw_bw"></a>`_handle_overlap_fw_bw`[`L584`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L584), <a id="GraphPipelineRuntime._handle_reduce_grad"></a>`_handle_reduce_grad`[`L574`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L574), <a id="GraphPipelineRuntime._handle_reshard"></a>`_handle_reshard`[`L569`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L569), <a id="GraphPipelineRuntime._handle_unshard"></a>`_handle_unshard`[`L563`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L563), <a id="GraphPipelineRuntime._populate_stage_states"></a>`_populate_stage_states`[`L393`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L393)
- uses (calls/refs, reference-scoped): [`logger`](../../../tools/logging.md#logger), [`GraphPipelineStage`](stage.md#GraphPipelineStage), [`state`](stage.md#GraphPipelineStage.state), [`_ensure_unsharded_param_values`](runner.md#_ensure_unsharded_param_values), [`clear`](stage.md#GraphPPStageRuntimeState.clear), [`flatten_graph_values`](utils.md#flatten_graph_values), [`_scale_graph_pp_sharded_grads`](runner.md#_scale_graph_pp_sharded_grads), [`graphs`](stage.md#GraphPipelineStage.graphs), [`_accumulate_stage_unsharded_grads`](runner.md#_accumulate_stage_unsharded_grads), [`GraphPPOverlapGraphs`](stage.md#GraphPPOverlapGraphs), [`sharded_param_grads`](stage.md#GraphPPStageRuntimeState.sharded_param_grads), [`GraphPPStageGraphs`](stage.md#GraphPPStageGraphs), [`_stage_map_and_stage_from_action`](runner.md#_stage_map_and_stage_from_action), [`accumulate_param_grads_`](../common_utils.md#accumulate_param_grads_), [`_prepare_backward_common`](runner.md#_prepare_backward_common), [`unsharded_param_grads`](stage.md#GraphPPStageRuntimeState.unsharded_param_grads), [`unsharded_param_values`](stage.md#GraphPPStageRuntimeState.unsharded_param_values), [`_prepare_fwd_common`](runner.md#_prepare_fwd_common), [`_post_fwd_common`](runner.md#_post_fwd_common), [`_prepare_fwd_user_args`](runner.md#_prepare_fwd_user_args), [`_post_backward_common`](runner.md#_post_backward_common), [`_prepare_backward_values`](runner.md#_prepare_backward_values), [`flat_buffer_values`](stage.md#GraphPPStageRuntimeState.flat_buffer_values), [`reduce_grads`](stage.md#GraphPPStageGraphs.reduce_grads), [`supports_backward_input_weight_split`](stage.md#GraphPPStageGraphs.supports_backward_input_weight_split), [`flat_param_values`](stage.md#GraphPPStageRuntimeState.flat_param_values), [`overlap_fw_bw_sub_actions`](utils.md#overlap_fw_bw_sub_actions), [`trainable_params`](stage.md#GraphPPStageRuntimeState.trainable_params), [`backward_input`](stage.md#GraphPPStageGraphs.backward_input), [`backward_weight`](stage.md#GraphPPStageGraphs.backward_weight), [`forward`](stage.md#GraphPPStageGraphs.forward), [`forward_backward`](stage.md#GraphPPOverlapGraphs.forward_backward), [`full_backward`](stage.md#GraphPPStageGraphs.full_backward), [`num_unsharded_param_grad_values`](stage.md#GraphPPStageGraphs.num_unsharded_param_grad_values), [`param_grads_for_accumulation`](stage.md#GraphPPStageGraphs.param_grads_for_accumulation), [`prepare_graphs`](stage.md#GraphPPStageGraphsProvider.prepare_graphs), [`GraphPPStageGraphsProvider`](stage.md#GraphPPStageGraphsProvider), [`_graph_pp_grads_scaled`](stage.md#GraphPipelineStage._graph_pp_grads_scaled), [`saved_values_for_backward_weight_cache`](stage.md#GraphPipelineStage.saved_values_for_backward_weight_cache)
- used by: [`graph_pipeline_llm`](pipeline.md#graph_pipeline_llm), [`register_graph_pp_schedule`](runner.md#register_graph_pp_schedule)  (4 test-only)

## Functions
- <a id="_accumulate_flat_grad_values_"></a>`_accumulate_flat_grad_values_(accumulated: list[Any], grads: list[Any], *, label: str, runtime_validate: bool)` — [`L71`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L71) — Accumulate raw flat graph-gradient values before boundary rewrapping.
- <a id="_accumulate_stage_unsharded_grads"></a>`_accumulate_stage_unsharded_grads(stage: GraphPipelineStage, grads: list[Any])` — [`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L119)
- <a id="_ensure_unsharded_param_values"></a>`_ensure_unsharded_param_values(stage: GraphPipelineStage, graphs: GraphPPStageGraphs)` — [`L107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L107)
- <a id="_post_backward_common"></a>`_post_backward_common(stage: GraphPipelineStage, mb_index: int, input_grads: list[Any], stage_index_to_stage: dict[int, GraphPipelineStage], is_prev_stage_on_this_rank: bool)` — [`L285`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L285) — Store input gradients and propagate same-rank backward inputs.
- <a id="_post_fwd_common"></a>`_post_fwd_common(stage: GraphPipelineStage, mb_index: int, output: Any, saved_values_for_backward: tuple[Any, ...], schedule: _PipelineScheduleRuntime, stage_index_to_stage: dict[int, GraphPipelineStage], is_next_stage_on_this_rank: bool)` — [`L206`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L206) — Store forward graph outputs and propagate same-rank activations.
- <a id="_prepare_backward_common"></a>`_prepare_backward_common(schedule: _PipelineScheduleRuntime, action: _Action)` — [`L248`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L248) — Prepare PP schedule state before one GraphPP backward graph call.
- <a id="_prepare_backward_values"></a>`_prepare_backward_values(stage: GraphPipelineStage, mb_index: int)` — [`L233`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L233) — Package cached forward values and received output grads for backward.
- <a id="_prepare_fwd_common"></a>`_prepare_fwd_common(schedule: _PipelineScheduleRuntime, action: _Action)` — [`L174`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L174) — Prepare PP schedule state before one GraphPP forward graph call.
- <a id="_prepare_fwd_user_args"></a>`_prepare_fwd_user_args(stage: GraphPipelineStage, mb_index: int, ctx: _PipelineContext)` — [`L131`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L131) — Package runtime forward inputs for a stage graph call.
- <a id="_scale_grad_values_"></a>`_scale_grad_values_(grads: list[Any], grad_scale_factor: int)` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L52)
- <a id="_scale_graph_pp_sharded_grads"></a>`_scale_graph_pp_sharded_grads(stage: GraphPipelineStage, schedule: _PipelineScheduleRuntime)` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L60)
- <a id="_stage_map_and_stage_from_action"></a>`_stage_map_and_stage_from_action(schedule: _PipelineScheduleRuntime, action: _Action)` — [`L155`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L155) — Return local GraphPP stages for an upstream schedule action.
- <a id="register_graph_pp_schedule"></a>`register_graph_pp_schedule(schedule: _PipelineScheduleRuntime, *, graph_provider: GraphPPStageGraphsProvider | None = None)` — [`L709`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L709) — Register GraphPP action handlers on a runtime PP schedule.

## Module values
- <a id="__all__"></a>`__all__` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/runner.py#L46)

