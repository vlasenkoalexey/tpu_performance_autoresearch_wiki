---
title: 'Module: torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.graph_pp.graph_builder`/
symbols:
  _build_stage_graphs: _build_stage_graphs().
  _build_graph_pp_overlap_graphs: _build_graph_pp_overlap_graphs().
  _apply_graph_pp_pre_partition_passes: _apply_graph_pp_pre_partition_passes().
  GraphTrainerStageGraphProvider.prepare_graphs: GraphTrainerStageGraphProvider#prepare_graphs().
  GraphTrainerStageGraphs.meta: GraphTrainerStageGraphs#meta.
  _compile_stage_graphs: _compile_stage_graphs().
  _compile_graph_pp_module: _compile_graph_pp_module().
  GraphTrainerOverlapGraphs.forward_backward: GraphTrainerOverlapGraphs#forward_backward().
  GraphTrainerStageGraphs.modules: GraphTrainerStageGraphs#modules.
  GraphTrainerStageGraphs._backward_args: GraphTrainerStageGraphs#_backward_args().
  _annotate_graph_pp_modules: _annotate_graph_pp_modules().
  GraphTrainerStageGraphs.backward_input: GraphTrainerStageGraphs#backward_input().
  GraphTrainerStageGraphs.reduce_grads: GraphTrainerStageGraphs#reduce_grads().
  GraphTrainerStageGraphs.forward: GraphTrainerStageGraphs#forward().
  GraphTrainerStageGraphs._forward_args: GraphTrainerStageGraphs#_forward_args().
  GraphTrainerStageGraphs.unshard_params: GraphTrainerStageGraphs#unshard_params().
  GraphTrainerStageGraphs._split_forward_outputs: GraphTrainerStageGraphs#_split_forward_outputs().
  GraphTrainerStageGraphProvider._warn_if_cudagraph_pass_requested: GraphTrainerStageGraphProvider#_warn_if_cudagraph_pass_requested().
  GraphTrainerStageGraphs.__post_init__: GraphTrainerStageGraphs#__post_init__().
  GraphTrainerStageGraphs.full_backward: GraphTrainerStageGraphs#full_backward().
  GraphTrainerStageGraphs._split_full_backward_outputs: GraphTrainerStageGraphs#_split_full_backward_outputs().
  GraphTrainerStageGraphProvider.compile_config: GraphTrainerStageGraphProvider#compile_config.
  _StageGraphMeta.num_flat_param_values: _StageGraphMeta#num_flat_param_values.
  _execute_graph_module: _execute_graph_module().
  GraphTrainerStageGraphProvider.model_config: GraphTrainerStageGraphProvider#model_config.
  GraphTrainerStageGraphs: GraphTrainerStageGraphs#
  GraphTrainerStageGraphs._flat_user_forward_inputs: GraphTrainerStageGraphs#_flat_user_forward_inputs().
  GraphTrainerStageGraphProvider._overlap_graphs: GraphTrainerStageGraphProvider#_overlap_graphs.
  _build_stage_graphs.stage_step: _build_stage_graphs().stage_step().
  _StageGraphMeta.partition: _StageGraphMeta#partition.
  GraphTrainerStageGraphs.supports_backward_input_weight_split: GraphTrainerStageGraphs#supports_backward_input_weight_split().
  GraphTrainerStageGraphs.backward_weight: GraphTrainerStageGraphs#backward_weight().
  GraphTrainerStageGraphs.param_grads_for_accumulation: GraphTrainerStageGraphs#param_grads_for_accumulation().
  GraphTrainerOverlapGraphs.bw_graphs: GraphTrainerOverlapGraphs#bw_graphs.
  _StageGraphModules.fw: _StageGraphModules#fw.
  _StageGraphModules.bw_di: _StageGraphModules#bw_di.
  _StageGraphModules.bw_dw: _StageGraphModules#bw_dw.
  _StageGraphMeta.num_param_grad_values: _StageGraphMeta#num_param_grad_values.
  GraphTrainerStageGraphProvider.parallelism: GraphTrainerStageGraphProvider#parallelism.
  _StageGraphModules.full_bw: _StageGraphModules#full_bw.
  _StageGraphModules.unshard: _StageGraphModules#unshard.
  _StageGraphModules.reduce_grad: _StageGraphModules#reduce_grad.
  GraphTrainerStageGraphs._validate_unsharded_param_grads: GraphTrainerStageGraphs#_validate_unsharded_param_grads().
  _split_stage_step_output_spec: _split_stage_step_output_spec().
  _trace_args_for_stage: _trace_args_for_stage().
  _StageGraphMeta.input_grad_values: _StageGraphMeta#input_grad_values.
  GraphTrainerOverlapGraphs.fw_graphs: GraphTrainerOverlapGraphs#fw_graphs.
  _StageGraphMeta.fwd_input_names: _StageGraphMeta#fwd_input_names.
  GraphTrainerStageGraphs.num_unsharded_param_grad_values: GraphTrainerStageGraphs#num_unsharded_param_grad_values().
  GraphTrainerStageGraphProvider: GraphTrainerStageGraphProvider#
  _StageGraphMeta.fwd_output_values: _StageGraphMeta#fwd_output_values.
  _StageGraphMeta.param_grad_values: _StageGraphMeta#param_grad_values.
  _required_multiplex_pairs: _required_multiplex_pairs().
  _StageGraphModules: _StageGraphModules#
  _StageGraphMeta.num_user_outputs: _StageGraphMeta#num_user_outputs.
  _StageGraphMeta.num_input_grad_values: _StageGraphMeta#num_input_grad_values.
  _StageGraphMeta.fwd_flat_input_indices: _StageGraphMeta#fwd_flat_input_indices.
  GraphTrainerStageGraphs.compiled: GraphTrainerStageGraphs#compiled.
  GraphTrainerStageGraphProvider.loss_fn: GraphTrainerStageGraphProvider#loss_fn.
  _GraphTrainerPassConfigView.compile: _GraphTrainerPassConfigView#compile.
  _GraphTrainerPassConfigView.parallelism: _GraphTrainerPassConfigView#parallelism.
  GraphTrainerOverlapGraphs: GraphTrainerOverlapGraphs#
  _flat_output_grads_from_stage_metadata: _flat_output_grads_from_stage_metadata().
  _example_args_from_stage_metadata: _example_args_from_stage_metadata().
  _trace_target_from_context: _trace_target_from_context().
  _StageGraphMeta.num_saved_for_backward: _StageGraphMeta#num_saved_for_backward.
  _StageGraphMeta.num_fw_unsharded_param_inputs: _StageGraphMeta#num_fw_unsharded_param_inputs.
  _StageGraphMeta.is_last_stage: _StageGraphMeta#is_last_stage.
  _grad_input_leaves: _grad_input_leaves().
  _StageGraphMeta: _StageGraphMeta#
  _StageGraphMeta.bw_no_fsdp_output_names: _StageGraphMeta#bw_no_fsdp_output_names.
  _StageGraphMeta.reduce_grad_input_names: _StageGraphMeta#reduce_grad_input_names.
  _StageGraphMeta.unshard_flat_param_indices: _StageGraphMeta#unshard_flat_param_indices.
  GraphTrainerOverlapGraphs.multiplexed_graph: GraphTrainerOverlapGraphs#multiplexed_graph.
  _requires_grad_like: _requires_grad_like().
  _annotate_graph_pp_graph: _annotate_graph_pp_graph().
  GraphTrainerStageGraphProvider._warned_cudagraph: GraphTrainerStageGraphProvider#_warned_cudagraph.
  _GraphTrainerPassConfigView: _GraphTrainerPassConfigView#
  _GraphTrainerPassConfigView.model_spec: _GraphTrainerPassConfigView#model_spec.
  _validate_stage_step_output_spec: _validate_stage_step_output_spec().
  _trace_kwargs_from_context: _trace_kwargs_from_context().
---
# Module: [`torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py)

## Classes
### <a id="GraphTrainerOverlapGraphs"></a>`GraphTrainerOverlapGraphs`  ·  implements/extends GraphPPOverlapGraphs
- def: [`torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py:584`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L584)
- doc: GraphTrainer-backed executor for one multiplexed `OVERLAP_F_B` pair.
- signature: `class GraphTrainerOverlapGraphs(GraphPPOverlapGraphs):`
- members:
  - <a id="GraphTrainerOverlapGraphs.forward_backward"></a>`forward_backward(self, *, backward_stage_output: tuple[Any, ...], backward_saved_values_for_backward: tuple[Any, ...], output_grads_from_next: tuple[Any, ...], forward_args: tuple[Any, ...], forward_kwargs: dict[str, Any], forward_target: Any, forward_loss_kwargs: dict[str, Any], forward_unsharded_param_values: list[Any], forward_flat_buffer_values: list[Any], runtime_validate: bool = False)` — [`L591`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L591) — Run the multiplexed graph and split backward/forward outputs.
  - <a id="GraphTrainerOverlapGraphs.bw_graphs"></a>`bw_graphs` — [`L588`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L588)
  - <a id="GraphTrainerOverlapGraphs.fw_graphs"></a>`fw_graphs` — [`L587`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L587)
  - <a id="GraphTrainerOverlapGraphs.multiplexed_graph"></a>`multiplexed_graph` — [`L589`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L589)
- uses (calls/refs, reference-scoped): [`meta`](graph_builder.md#GraphTrainerStageGraphs.meta), [`_backward_args`](graph_builder.md#GraphTrainerStageGraphs._backward_args), [`_forward_args`](graph_builder.md#GraphTrainerStageGraphs._forward_args), [`_split_forward_outputs`](graph_builder.md#GraphTrainerStageGraphs._split_forward_outputs), [`GraphPPOverlapGraphs`](stage.md#GraphPPOverlapGraphs), [`_split_full_backward_outputs`](graph_builder.md#GraphTrainerStageGraphs._split_full_backward_outputs), [`_execute_graph_module`](graph_builder.md#_execute_graph_module), [`GraphTrainerStageGraphs`](graph_builder.md#GraphTrainerStageGraphs), [`num_param_grad_values`](graph_builder.md#_StageGraphMeta.num_param_grad_values), [`num_input_grad_values`](graph_builder.md#_StageGraphMeta.num_input_grad_values)
- used by: [`_build_graph_pp_overlap_graphs`](graph_builder.md#_build_graph_pp_overlap_graphs), [`GraphPPOverlapGraphs`](stage.md#GraphPPOverlapGraphs), [`forward_backward`](stage.md#GraphPPOverlapGraphs.forward_backward)

### <a id="GraphTrainerStageGraphProvider"></a>`GraphTrainerStageGraphProvider`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py:1262`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1262)
- doc: Build bound GraphPP stage graphs with GraphTrainer tracing and passes.
- signature: `class GraphTrainerStageGraphProvider:`
- members:
  - <a id="GraphTrainerStageGraphProvider.prepare_graphs"></a>`prepare_graphs(self, schedule: _PipelineScheduleRuntime, ctx: _PipelineContext, *, loss_kwargs: dict[str, Any])` — [`L1297`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1297) — Build, multiplex, and compile all local GraphPP graphs for one step. — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)
  - <a id="GraphTrainerStageGraphProvider.compile_config"></a>`compile_config` — [`L1275`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1275)
  - <a id="GraphTrainerStageGraphProvider.loss_fn"></a>`loss_fn` — [`L1274`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1274)
  - <a id="GraphTrainerStageGraphProvider.model_config"></a>`model_config` — [`L1276`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1276)
  - <a id="GraphTrainerStageGraphProvider.parallelism"></a>`parallelism` — [`L1277`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1277)
- protocol/private: <a id="GraphTrainerStageGraphProvider._overlap_graphs"></a>`_overlap_graphs`[`L1279`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1279), <a id="GraphTrainerStageGraphProvider._warn_if_cudagraph_pass_requested"></a>`_warn_if_cudagraph_pass_requested`[`L1281`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1281), <a id="GraphTrainerStageGraphProvider._warned_cudagraph"></a>`_warned_cudagraph`[`L1278`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1278)
- uses (calls/refs, reference-scoped): [`ParallelismConfig`](../../../config/configs.md#ParallelismConfig), [`_build_stage_graphs`](graph_builder.md#_build_stage_graphs), [`enable`](../../../config/configs.md#CompileConfig.enable), [`GraphTrainerCompileConfig`](../configs.md#GraphTrainerCompileConfig), [`BaseModel`](../../../protocols/model.md#BaseModel), [`_build_graph_pp_overlap_graphs`](graph_builder.md#_build_graph_pp_overlap_graphs), [`GraphPipelineStage`](stage.md#GraphPipelineStage), [`_compile_stage_graphs`](graph_builder.md#_compile_stage_graphs), [`maybe_register_blockmask_pytree_node`](../common_utils.md#maybe_register_blockmask_pytree_node), [`Config`](../../../protocols/model.md#BaseModel.Config), [`graphs`](stage.md#GraphPipelineStage.graphs), [`GraphPPOverlapGraphs`](stage.md#GraphPPOverlapGraphs), [`enable_passes`](../configs.md#GraphTrainerCompileConfig.enable_passes), [`normalize_graph_pp_microbatch_inputs`](utils.md#normalize_graph_pp_microbatch_inputs), [`_trace_args_for_stage`](graph_builder.md#_trace_args_for_stage), [`_required_multiplex_pairs`](graph_builder.md#_required_multiplex_pairs), [`disable_passes`](../configs.md#GraphTrainerCompileConfig.disable_passes), [`_trace_target_from_context`](graph_builder.md#_trace_target_from_context), [`_trace_kwargs_from_context`](graph_builder.md#_trace_kwargs_from_context)
- used by: [`graph_pipeline_llm`](pipeline.md#graph_pipeline_llm)  (2 test-only)

### <a id="GraphTrainerStageGraphs"></a>`GraphTrainerStageGraphs`  ·  implements/extends GraphPPStageGraphs
- def: [`torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py:183`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L183)
- doc: GraphTrainer-backed bound graph executor for one GraphPP stage.
- signature: `class GraphTrainerStageGraphs(GraphPPStageGraphs):`
- members:
  - <a id="GraphTrainerStageGraphs._backward_args"></a>`_backward_args(self, stage_output: tuple[Any, ...], saved_values_for_backward: tuple[Any, ...], output_grads_from_next: tuple[Any, ...], *, runtime_validate: bool = False)` — [`L396`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L396) — Pack backward graph inputs from saved tensors and next-stage grads.
  - <a id="GraphTrainerStageGraphs._flat_user_forward_inputs"></a>`_flat_user_forward_inputs(self, args: tuple[Any, ...], kwargs: dict[str, Any], target: Any, loss_kwargs: dict[str, Any])` — [`L278`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L278) — Flatten the non-state runtime inputs supplied by PP for forward.
  - <a id="GraphTrainerStageGraphs._forward_args"></a>`_forward_args(self, args: tuple[Any, ...], kwargs: dict[str, Any], target: Any, loss_kwargs: dict[str, Any], *, unsharded_param_values: list[Any], flat_buffer_values: list[Any], runtime_validate: bool = False)` — [`L295`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L295) — Pack the extracted forward graph inputs in placeholder order.
  - <a id="GraphTrainerStageGraphs._split_forward_outputs"></a>`_split_forward_outputs(self, fw_outputs: tuple[Any, ...])` — [`L349`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L349) — Split user-visible outputs from saved values for backward.
  - <a id="GraphTrainerStageGraphs._split_full_backward_outputs"></a>`_split_full_backward_outputs(self, bw_outputs: tuple[Any, ...])` — [`L451`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L451) — Split ``full_bw`` outputs into input grads and param grads.
  - <a id="GraphTrainerStageGraphs.backward_input"></a>`backward_input(self, stage_output: tuple[Any, ...], saved_values_for_backward: tuple[Any, ...], output_grads_from_next: tuple[Any, ...], *, runtime_validate: bool = False)` — [`L486`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L486) — Return input grads and saved values for later weight backward.
  - <a id="GraphTrainerStageGraphs.backward_weight"></a>`backward_weight(self, saved_values_for_backward_weight: tuple[Any, ...])` — [`L512`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L512) — Return flat unsharded parameter gradients.
  - <a id="GraphTrainerStageGraphs.forward"></a>`forward(self, args: tuple[Any, ...], kwargs: dict[str, Any], target: Any, loss_kwargs: dict[str, Any], *, unsharded_param_values: list[Any], flat_buffer_values: list[Any], runtime_validate: bool = False)` — [`L362`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L362) — Return ``(stage_output, saved_values_for_backward)``.
  - <a id="GraphTrainerStageGraphs.full_backward"></a>`full_backward(self, stage_output: tuple[Any, ...], saved_values_for_backward: tuple[Any, ...], output_grads_from_next: tuple[Any, ...], *, runtime_validate: bool = False)` — [`L464`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L464) — Return ``(input_grads_to_prev, unsharded_param_grads)``.
  - <a id="GraphTrainerStageGraphs.num_unsharded_param_grad_values"></a>`num_unsharded_param_grad_values(self)` — [`L225`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L225)
  - <a id="GraphTrainerStageGraphs.param_grads_for_accumulation"></a>`param_grads_for_accumulation(self, sharded_param_grads: list[Any])` — [`L574`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L574) — Return parameter gradients in optimizer accumulation structure.
  - <a id="GraphTrainerStageGraphs.reduce_grads"></a>`reduce_grads(self, unsharded_param_grads: list[Any], *, runtime_validate: bool = False)` — [`L545`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L545) — Run the optional FSDP reduce-grad graph.
  - <a id="GraphTrainerStageGraphs.supports_backward_input_weight_split"></a>`supports_backward_input_weight_split(self)` — [`L221`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L221)
  - <a id="GraphTrainerStageGraphs.unshard_params"></a>`unshard_params(self, flat_param_values: list[Any], *, runtime_validate: bool = False)` — [`L228`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L228) — Run the optional FSDP unshard graph.
  - <a id="GraphTrainerStageGraphs.compiled"></a>`compiled` — [`L199`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L199)
  - <a id="GraphTrainerStageGraphs.meta"></a>`meta` — [`L198`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L198)
  - <a id="GraphTrainerStageGraphs.modules"></a>`modules` — [`L197`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L197)
- protocol/private: <a id="GraphTrainerStageGraphs.__post_init__"></a>`__post_init__`[`L201`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L201), <a id="GraphTrainerStageGraphs._validate_unsharded_param_grads"></a>`_validate_unsharded_param_grads`[`L527`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L527)
- uses (calls/refs, reference-scoped): [`flatten_graph_values`](utils.md#flatten_graph_values), [`wrap_flat_values`](utils.md#GraphPPValueSpec.wrap_flat_values), [`GraphPPStageGraphs`](stage.md#GraphPPStageGraphs), [`_execute_graph_module`](graph_builder.md#_execute_graph_module), [`num_flat_param_values`](graph_builder.md#_StageGraphMeta.num_flat_param_values), [`partition`](graph_builder.md#_StageGraphMeta.partition), [`backward_grad_input_names`](partition.md#GraphMeta.backward_grad_input_names), [`bw_di`](graph_builder.md#_StageGraphModules.bw_di), [`bw_dw`](graph_builder.md#_StageGraphModules.bw_dw), [`fw`](graph_builder.md#_StageGraphModules.fw), [`num_param_grad_values`](graph_builder.md#_StageGraphMeta.num_param_grad_values), [`full_bw`](graph_builder.md#_StageGraphModules.full_bw), [`reduce_grad`](graph_builder.md#_StageGraphModules.reduce_grad), [`saved_for_backward_names`](partition.md#GraphMeta.saved_for_backward_names), [`unflatten`](utils.md#GraphPPValueSpec.unflatten), [`unshard`](graph_builder.md#_StageGraphModules.unshard), [`input_grad_values`](graph_builder.md#_StageGraphMeta.input_grad_values), [`backward_grad_input_indices`](partition.md#GraphMeta.backward_grad_input_indices), [`bwd_input_names`](partition.md#GraphMeta.bwd_input_names), [`fwd_input_names`](graph_builder.md#_StageGraphMeta.fwd_input_names), [`fwd_output_values`](graph_builder.md#_StageGraphMeta.fwd_output_values), [`param_grad_values`](graph_builder.md#_StageGraphMeta.param_grad_values), [`_StageGraphModules`](graph_builder.md#_StageGraphModules), [`fwd_flat_input_indices`](graph_builder.md#_StageGraphMeta.fwd_flat_input_indices), [`num_input_grad_values`](graph_builder.md#_StageGraphMeta.num_input_grad_values), [`num_user_outputs`](graph_builder.md#_StageGraphMeta.num_user_outputs), [`is_last_stage`](graph_builder.md#_StageGraphMeta.is_last_stage), [`num_fw_unsharded_param_inputs`](graph_builder.md#_StageGraphMeta.num_fw_unsharded_param_inputs), [`num_saved_for_backward`](graph_builder.md#_StageGraphMeta.num_saved_for_backward), [`_StageGraphMeta`](graph_builder.md#_StageGraphMeta), [`bw_no_fsdp_output_names`](graph_builder.md#_StageGraphMeta.bw_no_fsdp_output_names), [`reduce_grad_input_names`](graph_builder.md#_StageGraphMeta.reduce_grad_input_names), [`unshard_flat_param_indices`](graph_builder.md#_StageGraphMeta.unshard_flat_param_indices)
- used by: [`_build_stage_graphs`](graph_builder.md#_build_stage_graphs), [`_build_graph_pp_overlap_graphs`](graph_builder.md#_build_graph_pp_overlap_graphs), [`_compile_stage_graphs`](graph_builder.md#_compile_stage_graphs), [`forward_backward`](graph_builder.md#GraphTrainerOverlapGraphs.forward_backward), [`GraphPPStageGraphs`](stage.md#GraphPPStageGraphs), [`bw_graphs`](graph_builder.md#GraphTrainerOverlapGraphs.bw_graphs), [`fw_graphs`](graph_builder.md#GraphTrainerOverlapGraphs.fw_graphs), [`reduce_grads`](stage.md#GraphPPStageGraphs.reduce_grads), [`supports_backward_input_weight_split`](stage.md#GraphPPStageGraphs.supports_backward_input_weight_split), [`backward_input`](stage.md#GraphPPStageGraphs.backward_input), [`backward_weight`](stage.md#GraphPPStageGraphs.backward_weight), [`forward`](stage.md#GraphPPStageGraphs.forward), [`full_backward`](stage.md#GraphPPStageGraphs.full_backward), [`num_unsharded_param_grad_values`](stage.md#GraphPPStageGraphs.num_unsharded_param_grad_values), [`param_grads_for_accumulation`](stage.md#GraphPPStageGraphs.param_grads_for_accumulation), [`unshard_params`](stage.md#GraphPPStageGraphs.unshard_params)

### <a id="_GraphTrainerPassConfigView"></a>`_GraphTrainerPassConfigView`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py:91`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L91)
- doc: Minimal config-shaped view needed by reused GraphTrainer pass builders.
- signature: `class _GraphTrainerPassConfigView:`
- members:
  - <a id="_GraphTrainerPassConfigView.compile"></a>`compile` — [`L101`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L101)
  - <a id="_GraphTrainerPassConfigView.model_spec"></a>`model_spec` — [`L103`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L103)
  - <a id="_GraphTrainerPassConfigView.parallelism"></a>`parallelism` — [`L102`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L102)
- uses (calls/refs, reference-scoped): [`ParallelismConfig`](../../../config/configs.md#ParallelismConfig), [`GraphTrainerCompileConfig`](../configs.md#GraphTrainerCompileConfig)
- used by: [`_apply_graph_pp_pre_partition_passes`](graph_builder.md#_apply_graph_pp_pre_partition_passes)

### <a id="_StageGraphMeta"></a>`_StageGraphMeta`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py:119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L119)
- doc: GraphTrainer metadata for one bound GraphPP stage graph executor.
- signature: `class _StageGraphMeta:`
- members:
  - <a id="_StageGraphMeta.bw_no_fsdp_output_names"></a>`bw_no_fsdp_output_names` — [`L155`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L155)
  - <a id="_StageGraphMeta.fwd_flat_input_indices"></a>`fwd_flat_input_indices` — [`L154`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L154)
  - <a id="_StageGraphMeta.fwd_input_names"></a>`fwd_input_names` — [`L153`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L153)
  - <a id="_StageGraphMeta.fwd_output_values"></a>`fwd_output_values` — [`L149`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L149)
  - <a id="_StageGraphMeta.input_grad_values"></a>`input_grad_values` — [`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L151)
  - <a id="_StageGraphMeta.is_last_stage"></a>`is_last_stage` — [`L159`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L159)
  - <a id="_StageGraphMeta.num_flat_param_values"></a>`num_flat_param_values` — [`L148`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L148)
  - <a id="_StageGraphMeta.num_fw_unsharded_param_inputs"></a>`num_fw_unsharded_param_inputs` — [`L158`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L158)
  - <a id="_StageGraphMeta.num_input_grad_values"></a>`num_input_grad_values` — [`L147`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L147)
  - <a id="_StageGraphMeta.num_param_grad_values"></a>`num_param_grad_values` — [`L146`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L146)
  - <a id="_StageGraphMeta.num_saved_for_backward"></a>`num_saved_for_backward` — [`L145`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L145)
  - <a id="_StageGraphMeta.num_user_outputs"></a>`num_user_outputs` — [`L144`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L144)
  - <a id="_StageGraphMeta.param_grad_values"></a>`param_grad_values` — [`L150`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L150)
  - <a id="_StageGraphMeta.partition"></a>`partition` — [`L152`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L152)
  - <a id="_StageGraphMeta.reduce_grad_input_names"></a>`reduce_grad_input_names` — [`L156`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L156)
  - <a id="_StageGraphMeta.unshard_flat_param_indices"></a>`unshard_flat_param_indices` — [`L157`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L157)
- uses (calls/refs, reference-scoped): [`GraphMeta`](partition.md#GraphMeta), [`GraphPPValueSpec`](utils.md#GraphPPValueSpec)
- used by: [`_build_stage_graphs`](graph_builder.md#_build_stage_graphs), [`meta`](graph_builder.md#GraphTrainerStageGraphs.meta), [`forward_backward`](graph_builder.md#GraphTrainerOverlapGraphs.forward_backward), [`_backward_args`](graph_builder.md#GraphTrainerStageGraphs._backward_args), [`backward_input`](graph_builder.md#GraphTrainerStageGraphs.backward_input), [`reduce_grads`](graph_builder.md#GraphTrainerStageGraphs.reduce_grads), [`forward`](graph_builder.md#GraphTrainerStageGraphs.forward), [`_forward_args`](graph_builder.md#GraphTrainerStageGraphs._forward_args), [`unshard_params`](graph_builder.md#GraphTrainerStageGraphs.unshard_params), [`_split_forward_outputs`](graph_builder.md#GraphTrainerStageGraphs._split_forward_outputs), [`__post_init__`](graph_builder.md#GraphTrainerStageGraphs.__post_init__), [`_split_full_backward_outputs`](graph_builder.md#GraphTrainerStageGraphs._split_full_backward_outputs), [`_flat_user_forward_inputs`](graph_builder.md#GraphTrainerStageGraphs._flat_user_forward_inputs), [`param_grads_for_accumulation`](graph_builder.md#GraphTrainerStageGraphs.param_grads_for_accumulation), [`_validate_unsharded_param_grads`](graph_builder.md#GraphTrainerStageGraphs._validate_unsharded_param_grads), [`num_unsharded_param_grad_values`](graph_builder.md#GraphTrainerStageGraphs.num_unsharded_param_grad_values)

### <a id="_StageGraphModules"></a>`_StageGraphModules`
- def: [`torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py:107`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L107)
- doc: FX graph modules produced by GraphTrainer stage graph construction.
- signature: `class _StageGraphModules:`
- members:
  - <a id="_StageGraphModules.bw_di"></a>`bw_di` — [`L112`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L112)
  - <a id="_StageGraphModules.bw_dw"></a>`bw_dw` — [`L113`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L113)
  - <a id="_StageGraphModules.full_bw"></a>`full_bw` — [`L111`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L111)
  - <a id="_StageGraphModules.fw"></a>`fw` — [`L110`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L110)
  - <a id="_StageGraphModules.reduce_grad"></a>`reduce_grad` — [`L115`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L115)
  - <a id="_StageGraphModules.unshard"></a>`unshard` — [`L114`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L114)
- used by: [`_build_stage_graphs`](graph_builder.md#_build_stage_graphs), [`_build_graph_pp_overlap_graphs`](graph_builder.md#_build_graph_pp_overlap_graphs), [`_compile_stage_graphs`](graph_builder.md#_compile_stage_graphs), [`modules`](graph_builder.md#GraphTrainerStageGraphs.modules), [`_annotate_graph_pp_modules`](graph_builder.md#_annotate_graph_pp_modules), [`backward_input`](graph_builder.md#GraphTrainerStageGraphs.backward_input), [`reduce_grads`](graph_builder.md#GraphTrainerStageGraphs.reduce_grads), [`forward`](graph_builder.md#GraphTrainerStageGraphs.forward), [`unshard_params`](graph_builder.md#GraphTrainerStageGraphs.unshard_params), [`full_backward`](graph_builder.md#GraphTrainerStageGraphs.full_backward), [`backward_weight`](graph_builder.md#GraphTrainerStageGraphs.backward_weight), [`supports_backward_input_weight_split`](graph_builder.md#GraphTrainerStageGraphs.supports_backward_input_weight_split)

## Functions
- <a id="_annotate_graph_pp_graph"></a>`_annotate_graph_pp_graph(gm: fx.GraphModule, *, stage_index: int, callable_name: str, action_name: str)` — [`L738`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L738)
- <a id="_annotate_graph_pp_modules"></a>`_annotate_graph_pp_modules(modules: _StageGraphModules, *, stage_index: int)` — [`L756`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L756)
- <a id="_apply_graph_pp_pre_partition_passes"></a>`_apply_graph_pp_pre_partition_passes(stage: GraphPipelineStage, traced: TracedResult, *, compile_config: GraphTrainerCompileConfig, model_config: BaseModel.Config | None, parallelism: ParallelismConfig | None)` — [`L779`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L779) — Apply the graph invariants GraphPP needs before partition. — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)
- <a id="_build_graph_pp_overlap_graphs"></a>`_build_graph_pp_overlap_graphs(schedule: _PipelineScheduleRuntime, *, compile_config: GraphTrainerCompileConfig)` — [`L1169`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1169) — Build multiplexed graphs required by ``OVERLAP_F_B`` schedule actions. — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)
- <a id="_build_stage_graphs"></a>`_build_stage_graphs(stage: GraphPipelineStage, args: tuple[Any, ...], kwargs: dict[str, Any], target: Any, loss_kwargs: dict[str, Any], *, loss_fn: Callable | None = None, compile_config: GraphTrainerCompileConfig, model_config: BaseModel.Config | None = None, parallelism: ParallelismConfig | None = None, compile_graphs: bool = True)` — [`L909`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L909) — Trace one stage-local train step and attach bound GraphPP graphs. — documented in [graph-trainer](../../../../../concepts/graph-trainer.md)
- <a id="_compile_graph_pp_module"></a>`_compile_graph_pp_module(gm: fx.GraphModule, *, compile_config: GraphTrainerCompileConfig, graph_name: str)` — [`L660`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L660) — Compile one extracted GraphPP callable with GraphTrainer Inductor passes.
- <a id="_compile_stage_graphs"></a>`_compile_stage_graphs(stage: GraphPipelineStage, *, compile_config: GraphTrainerCompileConfig)` — [`L694`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L694) — Compile the GraphTrainer graphs attached to ``stage`` once.
- <a id="_example_args_from_stage_metadata"></a>`_example_args_from_stage_metadata(stage: GraphPipelineStage)` — [`L1219`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1219)
- <a id="_execute_graph_module"></a>`_execute_graph_module(gm: fx.GraphModule, args: list[Any])` — [`L162`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L162) — Execute one boxed FX graph module and normalize its result to a tuple.
- <a id="_flat_output_grads_from_stage_metadata"></a>`_flat_output_grads_from_stage_metadata(stage: GraphPipelineStage)` — [`L835`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L835) — Return flat non-last output grads supplied by upstream PP metadata.
- <a id="_grad_input_leaves"></a>`_grad_input_leaves(stage_args: tuple[Any, ...], stage_kwargs: dict[str, Any])` — [`L648`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L648)
- <a id="_required_multiplex_pairs"></a>`_required_multiplex_pairs(schedule: _PipelineScheduleRuntime)` — [`L1150`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1150)
- <a id="_requires_grad_like"></a>`_requires_grad_like(value: Any)` — [`L642`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L642)
- <a id="_split_stage_step_output_spec"></a>`_split_stage_step_output_spec(traced: TracedResult, *, stage_index: int)` — [`L859`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L859) — Split the traced ``(forward_output, param_grads, input_grads)`` spec.
- <a id="_trace_args_for_stage"></a>`_trace_args_for_stage(stage: GraphPipelineStage, ctx: _PipelineContext)` — [`L1228`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1228) — Return representative positional inputs for a stage trace.
- <a id="_trace_kwargs_from_context"></a>`_trace_kwargs_from_context(ctx: _PipelineContext)` — [`L1246`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1246)
- <a id="_trace_target_from_context"></a>`_trace_target_from_context(stage: GraphPipelineStage, ctx: _PipelineContext)` — [`L1252`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L1252)
- <a id="_validate_stage_step_output_spec"></a>`_validate_stage_step_output_spec(*, stage_index: int, fwd_output_spec: pytree.TreeSpec, param_grad_spec: pytree.TreeSpec, input_grad_spec: pytree.TreeSpec, num_grad_params: int, num_input_grad_leaves: int)` — [`L879`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L879) — Validate traced grouped outputs against the GraphPP calling convention.
- <a id="_build_stage_graphs.stage_step"></a>`stage_step(stage_args, stage_kwargs, target, loss_kwargs)` — [`L948`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/graph_pp/graph_builder.py#L948)

