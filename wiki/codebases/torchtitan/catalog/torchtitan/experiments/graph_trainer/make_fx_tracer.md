---
title: 'Module: torchtitan/experiments/graph_trainer/make_fx_tracer.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/make_fx_tracer.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.make_fx_tracer`/
symbols:
  TracedResult.gm: TracedResult#gm.
  minimal_fx_tracer: minimal_fx_tracer().
  run_traced: run_traced().
  minimal_fx_tracer._trace_with_args: minimal_fx_tracer()._trace_with_args().
  TracedResult.example_inputs: TracedResult#example_inputs.
  TracedResult: TracedResult#
  TracedResult.num_static_inputs: TracedResult#num_static_inputs().
  run_traced._run: run_traced()._run().
  SubclassLayout: SubclassLayout#
  _unwrap_subclass: _unwrap_subclass().
  _wrap_to_subclass: _wrap_to_subclass().
  _wrap_subclasses: _wrap_subclasses().
  _unwrap_subclasses: _unwrap_subclasses().
  TracedResult.output_subclass_layouts: TracedResult#output_subclass_layouts.
  TracedResult.graph_state: TracedResult#graph_state.
  extract_module_state: extract_module_state().
  TracedResult.state_fqns: TracedResult#state_fqns.
  TracedResult.input_subclass_layouts: TracedResult#input_subclass_layouts.
  GraphStateSpec.mappings: GraphStateSpec#mappings.
  GraphStateSpec.fqns: GraphStateSpec#fqns().
  extract_train_state: extract_train_state().
  minimal_fx_tracer._trace_with_args.fn_with_subclass_handling: minimal_fx_tracer()._trace_with_args().fn_with_subclass_handling().
  TracedResult.num_flat_outputs: TracedResult#num_flat_outputs.
  TracedResult.user_inputs_spec: TracedResult#user_inputs_spec.
  TracedResult.output_spec: TracedResult#output_spec.
  _copy_fwd_metadata_to_bw_nodes: _copy_fwd_metadata_to_bw_nodes().
  GraphStateSpec: GraphStateSpec#
  TracedResult.tensor_input_indices: TracedResult#tensor_input_indices.
  TracedResult.num_runtime_mesh_inputs: TracedResult#num_runtime_mesh_inputs.
  _flat_tensor_ranges: _flat_tensor_ranges().
  SubclassLayout.num_tensors: SubclassLayout#num_tensors.
  GraphStateMapping: GraphStateMapping#
  GraphStateSpec.__post_init__: GraphStateSpec#__post_init__().
  SubclassLayout.meta: SubclassLayout#meta.
  SubclassMeta: SubclassMeta#
  TracedResult.num_flat_inputs: TracedResult#num_flat_inputs.
  TracedResult.num_optimizer_state_inputs: TracedResult#num_optimizer_state_inputs.
  GraphStateMapping.fqn: GraphStateMapping#fqn.
  SubclassMeta.cls: SubclassMeta#cls.
  SubclassMeta.attrs: SubclassMeta#attrs.
  SubclassMeta.ctx: SubclassMeta#ctx.
  SubclassMeta.inner_metas: SubclassMeta#inner_metas.
  SubclassMeta.outer_size: SubclassMeta#outer_size.
  SubclassMeta.outer_stride: SubclassMeta#outer_stride.
  _copy_fwd_metadata_to_bw_nodes._is_backward: _copy_fwd_metadata_to_bw_nodes()._is_backward().
  _check_optimizer_has_module: _check_optimizer_has_module().
  GraphStateMapping.input_indices: GraphStateMapping#input_indices.
  _ALLOWED_LEAF_TYPES: _ALLOWED_LEAF_TYPES.
  _skip_nested_compile: _skip_nested_compile().
  _reparametrize_train_state: _reparametrize_train_state().
---
# Module: [`torchtitan/experiments/graph_trainer/make_fx_tracer.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py)

## Classes
### <a id="GraphStateMapping"></a>`GraphStateMapping`
- def: [`torchtitan/experiments/graph_trainer/make_fx_tracer.py:291`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L291)
- doc: Trace-time locations associated with one trainer-owned tensor.
- signature: `class GraphStateMapping:`
- members:
  - <a id="GraphStateMapping.fqn"></a>`fqn` — [`L307`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L307)
  - <a id="GraphStateMapping.input_indices"></a>`input_indices` — [`L308`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L308)
- used by: [`_trace_with_args`](make_fx_tracer.md#minimal_fx_tracer._trace_with_args), [`mappings`](make_fx_tracer.md#GraphStateSpec.mappings), [`fqns`](make_fx_tracer.md#GraphStateSpec.fqns), [`__post_init__`](make_fx_tracer.md#GraphStateSpec.__post_init__)  (2 test-only)

### <a id="GraphStateSpec"></a>`GraphStateSpec`
- def: [`torchtitan/experiments/graph_trainer/make_fx_tracer.py:312`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L312)
- doc: Locations of trainer-owned tensors passed to the traced function.
- signature: `class GraphStateSpec:`
- members:
  - <a id="GraphStateSpec.fqns"></a>`fqns(self)` — [`L323`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L323)
  - <a id="GraphStateSpec.mappings"></a>`mappings` — [`L315`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L315)
- protocol/private: <a id="GraphStateSpec.__post_init__"></a>`__post_init__`[`L317`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L317)
- uses (calls/refs, reference-scoped): [`GraphStateMapping`](make_fx_tracer.md#GraphStateMapping), [`fqn`](make_fx_tracer.md#GraphStateMapping.fqn)
- used by: [`_trace_with_args`](make_fx_tracer.md#minimal_fx_tracer._trace_with_args), [`from_traced_result`](precompile.md#PrecompiledFxTraceArtifact.from_traced_result), [`num_static_inputs`](make_fx_tracer.md#TracedResult.num_static_inputs), [`_run`](make_fx_tracer.md#run_traced._run), [`_resolve_state_tensors`](runner.md#_resolve_state_tensors), [`graph_state`](make_fx_tracer.md#TracedResult.graph_state)  (4 test-only)

### <a id="SubclassLayout"></a>`SubclassLayout`
- def: [`torchtitan/experiments/graph_trainer/make_fx_tracer.py:75`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L75)
- signature: `class SubclassLayout:`
- members:
  - <a id="SubclassLayout.meta"></a>`meta` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L77)
  - <a id="SubclassLayout.num_tensors"></a>`num_tensors` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L76)
- uses (calls/refs, reference-scoped): [`SubclassMeta`](make_fx_tracer.md#SubclassMeta)
- used by: [`_trace_with_args`](make_fx_tracer.md#minimal_fx_tracer._trace_with_args), [`num_static_inputs`](make_fx_tracer.md#TracedResult.num_static_inputs), [`graph_pp_value_spec`](graph_pp/utils.md#graph_pp_value_spec), [`_wrap_subclasses`](make_fx_tracer.md#_wrap_subclasses), [`_unwrap_subclasses`](make_fx_tracer.md#_unwrap_subclasses), [`output_subclass_layouts`](make_fx_tracer.md#TracedResult.output_subclass_layouts), [`input_subclass_layouts`](make_fx_tracer.md#TracedResult.input_subclass_layouts), [`_wrap_unwrapped_values`](graph_pp/utils.md#_wrap_unwrapped_values), [`_num_unwrapped_values`](graph_pp/utils.md#_num_unwrapped_values), [`_flat_tensor_ranges`](make_fx_tracer.md#_flat_tensor_ranges), [`input_subclass_layouts`](precompile.md#PrecompiledFxTraceArtifact.input_subclass_layouts), [`layouts`](graph_pp/utils.md#GraphPPValueSpec.layouts), [`output_subclass_layouts`](precompile.md#PrecompiledFxTraceArtifact.output_subclass_layouts), [`_subclass_layout_slice`](graph_pp/utils.md#_subclass_layout_slice)  (2 test-only)

### <a id="SubclassMeta"></a>`SubclassMeta`
- def: [`torchtitan/experiments/graph_trainer/make_fx_tracer.py:65`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L65)
- signature: `class SubclassMeta:`
- members:
  - <a id="SubclassMeta.attrs"></a>`attrs` — [`L67`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L67)
  - <a id="SubclassMeta.cls"></a>`cls` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L66)
  - <a id="SubclassMeta.ctx"></a>`ctx` — [`L68`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L68)
  - <a id="SubclassMeta.inner_metas"></a>`inner_metas` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L69)
  - <a id="SubclassMeta.outer_size"></a>`outer_size` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L70)
  - <a id="SubclassMeta.outer_stride"></a>`outer_stride` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L71)
- used by: [`_unwrap_subclass`](make_fx_tracer.md#_unwrap_subclass), [`_wrap_to_subclass`](make_fx_tracer.md#_wrap_to_subclass), [`meta`](make_fx_tracer.md#SubclassLayout.meta)

### <a id="TracedResult"></a>`TracedResult`
- def: [`torchtitan/experiments/graph_trainer/make_fx_tracer.py:328`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L328)
- doc: Execution metadata returned by `minimal_fx_tracer`.
- signature: `class TracedResult:`
- members:
  - <a id="TracedResult.num_static_inputs"></a>`num_static_inputs(self)` — [`L369`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L369) — Number of leading graph inputs with stable tensor addresses.
  - <a id="TracedResult.example_inputs"></a>`example_inputs` — [`L351`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L351)
  - <a id="TracedResult.gm"></a>`gm` — [`L348`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L348)
  - <a id="TracedResult.graph_state"></a>`graph_state` — [`L364`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L364)
  - <a id="TracedResult.input_subclass_layouts"></a>`input_subclass_layouts` — [`L353`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L353)
  - <a id="TracedResult.num_flat_inputs"></a>`num_flat_inputs` — [`L352`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L352)
  - <a id="TracedResult.num_flat_outputs"></a>`num_flat_outputs` — [`L358`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L358)
  - <a id="TracedResult.num_optimizer_state_inputs"></a>`num_optimizer_state_inputs` — [`L365`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L365)
  - <a id="TracedResult.num_runtime_mesh_inputs"></a>`num_runtime_mesh_inputs` — [`L366`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L366)
  - <a id="TracedResult.output_spec"></a>`output_spec` — [`L360`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L360)
  - <a id="TracedResult.output_subclass_layouts"></a>`output_subclass_layouts` — [`L359`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L359)
  - <a id="TracedResult.state_fqns"></a>`state_fqns` — [`L363`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L363)
  - <a id="TracedResult.tensor_input_indices"></a>`tensor_input_indices` — [`L355`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L355)
  - <a id="TracedResult.user_inputs_spec"></a>`user_inputs_spec` — [`L354`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L354)
- uses (calls/refs, reference-scoped): [`SubclassLayout`](make_fx_tracer.md#SubclassLayout), [`mappings`](make_fx_tracer.md#GraphStateSpec.mappings), [`GraphStateSpec`](make_fx_tracer.md#GraphStateSpec), [`num_tensors`](make_fx_tracer.md#SubclassLayout.num_tensors)
- used by: [`_build_stage_graphs`](graph_pp/graph_builder.md#_build_stage_graphs), [`minimal_fx_tracer`](make_fx_tracer.md#minimal_fx_tracer), [`compile_time_passes`](passes.md#compile_time_passes), [`_make_fx_forward_backward_step`](trainer.md#GraphTrainer._make_fx_forward_backward_step), [`run_traced`](make_fx_tracer.md#run_traced), [`partition_joint_graph`](graph_pp/partition.md#partition_joint_graph), [`_trace_with_args`](make_fx_tracer.md#minimal_fx_tracer._trace_with_args), [`_fwd_bwd_adamw_step`](../tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer._fwd_bwd_adamw_step), [`split_and_compile`](../tpu/graph_trainer/graph_split.md#GraphSplitter.split_and_compile), [`_precompile_aot_fx_trace`](precompile_main.md#_precompile_aot_fx_trace), [`to_traced_result`](precompile.md#PrecompiledFxTraceArtifact.to_traced_result), [`_make_fx_forward_backward_step`](../tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer._make_fx_forward_backward_step), [`construct_tpu_transform_passes`](../tpu/graph_trainer/tpu_backend_pass.md#construct_tpu_transform_passes), [`_apply_graph_pp_pre_partition_passes`](graph_pp/graph_builder.md#_apply_graph_pp_pre_partition_passes), [`from_traced_result`](precompile.md#PrecompiledFxTraceArtifact.from_traced_result), [`precompile_fx_trace_load`](precompile.md#precompile_fx_trace_load), [`_traced_step`](trainer.md#GraphTrainer._traced_step), [`precompile_fx_trace_save`](precompile.md#precompile_fx_trace_save), [`clip_grad_norm_`](../tpu/grad_norm.md#CompiledGradNorm.clip_grad_norm_), [`_run`](make_fx_tracer.md#run_traced._run), [`__call__`](runner.md#GraphRunner.__call__), [`construct_tpu_pass_pipeline`](../tpu/graph_trainer/tpu_backend_pass.md#construct_tpu_pass_pipeline), [`_flatten_state_inputs`](runner.md#_flatten_state_inputs), [`construct_default_graph_passes`](passes.md#construct_default_graph_passes), [`_build_compiled_optimizer_groups`](../tpu/compiled_optimizers/separate_graph.md#_build_compiled_optimizer_groups), [`_resolve_state_tensors`](runner.md#_resolve_state_tensors), [`_run`](../tpu/compiled_optimizers/separate_graph.md#_build_compiled_optimizer_groups._run), [`_validate_runtime_meshes`](runner.md#GraphRunner._validate_runtime_meshes), [`_split_stage_step_output_spec`](graph_pp/graph_builder.md#_split_stage_step_output_spec), [`_validate_user_inputs`](runner.md#GraphRunner._validate_user_inputs), [`__init__`](runner.md#GraphRunner.__init__)  (70 test-only)

## Functions
- <a id="_check_optimizer_has_module"></a>`_check_optimizer_has_module(module: nn.Module | None, optimizer: torch.optim.Optimizer | None)` — [`L245`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L245) — Optimizer parameters align with module.named_parameters() by order, so
- <a id="_copy_fwd_metadata_to_bw_nodes"></a>`_copy_fwd_metadata_to_bw_nodes(fx_g: torch.fx.GraphModule)` — [`L168`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L168) — Copy forward metadata to backward nodes across all nested FX subgraphs.
- <a id="_flat_tensor_ranges"></a>`_flat_tensor_ranges(num_values: int, layouts: dict[int, SubclassLayout])` — [`L390`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L390)
- <a id="_copy_fwd_metadata_to_bw_nodes._is_backward"></a>`_is_backward(node: torch.fx.Node)` — [`L178`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L178)
- <a id="_reparametrize_train_state"></a>`_reparametrize_train_state(module: nn.Module | None, optimizer: torch.optim.Optimizer | None, model_state: dict[str, torch.Tensor], optim_state: dict[str, Any])` — [`L259`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L259) — Reparametrize module and optimizer with explicit tensor state for tracing.
- <a id="run_traced._run"></a>`_run(*args: Any, **kwargs: Any)` — [`L694`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L694)
- <a id="_skip_nested_compile"></a>`_skip_nested_compile()` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L48) — Tell dynamo to skip torch.compile calls encountered during make_fx tracing.
- <a id="minimal_fx_tracer._trace_with_args"></a>`_trace_with_args(*args: Any, **kwargs: Any)` — [`L467`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L467)
- <a id="_unwrap_subclass"></a>`_unwrap_subclass(t: torch.Tensor)` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L80)
- <a id="_unwrap_subclasses"></a>`_unwrap_subclasses(args: list)` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L125) — Unwrap tensor subclasses into plain tensors.
- <a id="_wrap_subclasses"></a>`_wrap_subclasses(flat_tensors: tuple | list, num_args: int, layouts: dict[int, SubclassLayout])` — [`L145`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L145) — Rewrap plain tensors back into their original subclass types.
- <a id="_wrap_to_subclass"></a>`_wrap_to_subclass(plain_tensors: list[torch.Tensor], meta: SubclassMeta)` — [`L102`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L102)
- <a id="extract_module_state"></a>`extract_module_state(mod: nn.Module)` — [`L222`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L222) — Return a merged dict of the module's named parameters and buffers.
- <a id="extract_train_state"></a>`extract_train_state(module: nn.Module | None = None, optimizer: torch.optim.Optimizer | None = None)` — [`L230`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L230) — Return ``(model_state, optim_state)`` for ``minimal_fx_tracer``.
- <a id="minimal_fx_tracer._trace_with_args.fn_with_subclass_handling"></a>`fn_with_subclass_handling(*plain_args: Any)` — [`L559`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L559)
- <a id="minimal_fx_tracer"></a>`minimal_fx_tracer(fn: Callable, module: nn.Module | None = None, optimizer: torch.optim.Optimizer | None = None, *, precompile_meshes: list[DeviceMesh] | None = None, graph_state: dict[str, torch.Tensor] | None = None, prepare_inputs: Callable[[tuple[Any, ...], dict[str, Any]], None] | None = None, prepare_call_inputs: Callable[[tuple[Any, ...], dict[str, Any]], tuple[tuple[Any, ...], dict[str, Any]] | None,] | None = None, record_stack_traces: bool = True, _insert_runtime_asserts: bool = False)` — [`L405`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L405) — Return a tracer that captures ``fn`` with implicit module/optimizer state.
- <a id="run_traced"></a>`run_traced(traced_result: TracedResult, *, module: nn.Module | None = None, optimizer: torch.optim.Optimizer | None = None, precompile_meshes: list[DeviceMesh] | None = None, graph_state: dict[str, torch.Tensor] | None = None, _validate_runtime: bool = False, interpreter_cls: type | None = None)` — [`L658`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L658) — Return a runner that executes a traced graph against live module/optimizer state.

## Module values
- <a id="_ALLOWED_LEAF_TYPES"></a>`_ALLOWED_LEAF_TYPES` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/make_fx_tracer.py#L36)

