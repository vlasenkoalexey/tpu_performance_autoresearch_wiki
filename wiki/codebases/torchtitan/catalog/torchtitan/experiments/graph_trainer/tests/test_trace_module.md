---
title: 'Module: torchtitan/experiments/graph_trainer/tests/test_trace_module.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/graph_trainer/tests/test_trace_module.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.graph_trainer.tests.test_trace_module`/
symbols:
  TinyFlexMLA.attn: TinyFlexMLA#attn.
  TestTraceContextParallel._trace_llama3_step_code: TestTraceContextParallel#_trace_llama3_step_code().
  TestTraceFSDP.test_graph_gradient_accumulation_preserves_fsdp_layout: TestTraceFSDP#test_graph_gradient_accumulation_preserves_fsdp_layout().
  TestTraceModels.test_flex_attention_annotations: TestTraceModels#test_flex_attention_annotations().
  TestAutogradGradVsBackwardFSDP.test_peak_memory_identical_fsdp: TestAutogradGradVsBackwardFSDP#test_peak_memory_identical_fsdp().
  TestTraceModels.test_deepseek_v3_flex_attention: TestTraceModels#test_deepseek_v3_flex_attention().
  TestTraceFSDP._run_fsdp_model_test: TestTraceFSDP#_run_fsdp_model_test().
  TestTraceModule.DEVICE: TestTraceModule#DEVICE.
  TestMinimalFXTracerDynamicShapes.forward: TestMinimalFXTracerDynamicShapes#forward().
  TestTraceModels.test_gpt_oss: TestTraceModels#test_gpt_oss().
  TestReparametrizeOptimizer.test_titan_optimizers_container: TestReparametrizeOptimizer#test_titan_optimizers_container().
  TestGraphGradientAccumulation.test_inplace_grad_accumulation_uses_stable_optimizer_buffers: TestGraphGradientAccumulation#test_inplace_grad_accumulation_uses_stable_optimizer_buffers().
  TestTraceModels._run_model_test: TestTraceModels#_run_model_test().
  TestGraphGradientAccumulation.make_trainer: TestGraphGradientAccumulation#make_trainer().
  TestTraceFSDP.parallel_dims: TestTraceFSDP#parallel_dims.
  TestTraceModule.test_mlp_multistep_bitwise: TestTraceModule#test_mlp_multistep_bitwise().
  TestTraceDTensor.test_dtensor_forward: TestTraceDTensor#test_dtensor_forward().
  TestMetadataPropagation.test_copy_fwd_metadata_propagates_custom: TestMetadataPropagation#test_copy_fwd_metadata_propagates_custom().
  TestTraceModels._run_bitwise_test: TestTraceModels#_run_bitwise_test().
  TestTraceModule.test_chunked_loss_train_step: TestTraceModule#test_chunked_loss_train_step().
  TestTraceDTensor.test_dtensor_train_step: TestTraceDTensor#test_dtensor_train_step().
  TestGraphGradientAccumulation.run_trainer: TestGraphGradientAccumulation#run_trainer().
  SimpleMLP: SimpleMLP#
  TestTraceModule._make_mlp: TestTraceModule#_make_mlp().
  TestGraphGradientAccumulation.test_cuda_graph_numerics_match_external_accumulation: TestGraphGradientAccumulation#test_cuda_graph_numerics_match_external_accumulation().
  TestTraceModule.test_mlp_train_step: TestTraceModule#test_mlp_train_step().
  TestTraceModule.test_kwargs_roundtrip: TestTraceModule#test_kwargs_roundtrip().
  TestTraceModule.test_kwargs_runtime_reorder_raises: TestTraceModule#test_kwargs_runtime_reorder_raises().
  TestTraceModule.test_kwargs_unknown_kwarg_raises: TestTraceModule#test_kwargs_unknown_kwarg_raises().
  TestTraceModule.test_kwargs_default_omitted_bakes_constant: TestTraceModule#test_kwargs_default_omitted_bakes_constant().
  TestTraceModule.test_kwargs_var_keyword_missing_key_raises: TestTraceModule#test_kwargs_var_keyword_missing_key_raises().
  TestTraceDTensor.test_full_inductor_pass_migrates_cpu_attrs: TestTraceDTensor#test_full_inductor_pass_migrates_cpu_attrs().
  TestMetadataPropagation.test_backward_nodes_have_seq_nr: TestMetadataPropagation#test_backward_nodes_have_seq_nr().
  TestMetadataPropagation.test_backward_nodes_have_stack_trace: TestMetadataPropagation#test_backward_nodes_have_stack_trace().
  TestTraceFSDP.test_gpt_oss_fsdp: TestTraceFSDP#test_gpt_oss_fsdp().
  TestTraceModule.DTYPE: TestTraceModule#DTYPE.
  TestTraceModels.DEVICE: TestTraceModels#DEVICE.
  TestMinimalFXTracerDynamicShapes.test_mark_dynamic_token_dim_with_rope: TestMinimalFXTracerDynamicShapes#test_mark_dynamic_token_dim_with_rope().
  TestTraceModule.test_mismatched_module_raises_when_validation_enabled: TestTraceModule#test_mismatched_module_raises_when_validation_enabled().
  TestTraceDTensor.test_full_inductor_pass_on_collective: TestTraceDTensor#test_full_inductor_pass_on_collective().
  TestTraceModels.test_deepseek_v3: TestTraceModels#test_deepseek_v3().
  _apply_regional_inductor: _apply_regional_inductor().
  TestTraceDTensor.DEVICE: TestTraceDTensor#DEVICE.
  get_loss: get_loss().
  TestGraphGradientAccumulation.test_graph_gradient_state_rejects_graph_state_replacement: TestGraphGradientAccumulation#test_graph_gradient_state_rejects_graph_state_replacement().
  TestMinimalFXTracerDynamicShapes.test_mark_unbacked_positions_token_dim_with_rope: TestMinimalFXTracerDynamicShapes#test_mark_unbacked_positions_token_dim_with_rope().
  TestTraceModule.test_non_tensor_leaf_raises: TestTraceModule#test_non_tensor_leaf_raises().
  TestTraceModule.test_flex_attention_block_mask_mark_unbacked: TestTraceModule#test_flex_attention_block_mask_mark_unbacked().
  TestTraceModule.test_module_in_args_raises: TestTraceModule#test_module_in_args_raises().
  TestTraceFSDP.test_deepseek_v3_fsdp: TestTraceFSDP#test_deepseek_v3_fsdp().
  TestTraceModule.forward: TestTraceModule#forward().
  TestTraceModule.train_step: TestTraceModule#train_step().
  make_train_step: make_train_step().
  TestGraphGradientAccumulation.test_graph_gradient_state_prepares_after_both_zero_grad_policies: TestGraphGradientAccumulation#test_graph_gradient_state_prepares_after_both_zero_grad_policies().
  EmptyModel.second: EmptyModel#second.
  TestMinimalFXTracerDynamicShapes.test_mark_unbacked_min_max_preserves_unbacked_placeholder_dim: TestMinimalFXTracerDynamicShapes#test_mark_unbacked_min_max_preserves_unbacked_placeholder_dim().
  TestMinimalFXTracerDynamicShapes.test_mark_unbacked_preserves_unbacked_placeholder_dim: TestMinimalFXTracerDynamicShapes#test_mark_unbacked_preserves_unbacked_placeholder_dim().
  TestTraceModule.test_mlp_forward: TestTraceModule#test_mlp_forward().
  TestTraceModule.test_optimizer_passed_without_module_raises: TestTraceModule#test_optimizer_passed_without_module_raises().
  InplaceWgradModel.projection: InplaceWgradModel#projection.
  TestMinimalFXTracerDynamicShapes._trace_mark_dynamic_value_range: TestMinimalFXTracerDynamicShapes#_trace_mark_dynamic_value_range().
  _disable_flex_autotune: _disable_flex_autotune().
  create_model: create_model().
  TestMetadataPropagation.DEVICE: TestMetadataPropagation#DEVICE.
  _restore_flex_autotune: _restore_flex_autotune().
  SimpleMLP.forward: SimpleMLP#forward().
  TiedModel.tied_weight: TiedModel#tied_weight.
  TestGraphGradientAccumulation.test_graph_gradient_state_rejects_partial_grad_clear: TestGraphGradientAccumulation#test_graph_gradient_state_rejects_partial_grad_clear().
  AliasedModel.second: AliasedModel#second.
  TestGraphGradientAccumulation.test_graph_gradient_state_rejects_parameter_storage_replacement: TestGraphGradientAccumulation#test_graph_gradient_state_rejects_parameter_storage_replacement().
  TestMinimalFXTracerDynamicShapes.test_mark_dynamic_wrapper_subclass_rejected: TestMinimalFXTracerDynamicShapes#test_mark_dynamic_wrapper_subclass_rejected().
  TestMinimalFXTracerDynamicShapes.test_nested_wrapper_subclass_marked_inner_rejected: TestMinimalFXTracerDynamicShapes#test_nested_wrapper_subclass_marked_inner_rejected().
  TestMinimalFXTracerDynamicShapes.test_mark_unbacked_mixed_with_static_input_replay: TestMinimalFXTracerDynamicShapes#test_mark_unbacked_mixed_with_static_input_replay().
  TestMinimalFXTracerDynamicShapes.test_mark_unbacked_input_symbol_is_not_pending_fresh: TestMinimalFXTracerDynamicShapes#test_mark_unbacked_input_symbol_is_not_pending_fresh().
  TestMinimalFXTracerDynamicShapes.test_mark_unbacked_multiple_inputs_replay: TestMinimalFXTracerDynamicShapes#test_mark_unbacked_multiple_inputs_replay().
  TestMinimalFXTracerDynamicShapes.test_data_dependent_check_emits_runtime_asserts: TestMinimalFXTracerDynamicShapes#test_data_dependent_check_emits_runtime_asserts().
  TestMinimalFXTracerDynamicShapes.test_no_runtime_asserts_when_no_constraints: TestMinimalFXTracerDynamicShapes#test_no_runtime_asserts_when_no_constraints().
  TestMinimalFXTracerDynamicShapes.test_mark_unbacked_shape_id_multiple_inputs_replay: TestMinimalFXTracerDynamicShapes#test_mark_unbacked_shape_id_multiple_inputs_replay().
  TestReparametrizeOptimizer.test_minimal_fx_tracer_with_bucketed_optimizer: TestReparametrizeOptimizer#test_minimal_fx_tracer_with_bucketed_optimizer().
  TestTraceDTensor.test_dtensor_mark_unbacked_rejected: TestTraceDTensor#test_dtensor_mark_unbacked_rejected().
  TestTraceModels.test_llama3: TestTraceModels#test_llama3().
  TestTraceModels.test_qwen3: TestTraceModels#test_qwen3().
  TestTraceModels.test_qwen3_moe: TestTraceModels#test_qwen3_moe().
  TestTraceModels.test_deepseek_v3_flex_attention.TinyFlexMLA.forward: TestTraceModels#test_deepseek_v3_flex_attention().TinyFlexMLA#forward().
  TestTraceFSDP.test_llama3_fsdp: TestTraceFSDP#test_llama3_fsdp().
  TestTraceFSDP.test_qwen3_fsdp: TestTraceFSDP#test_qwen3_fsdp().
  _TraceableWrapper: _TraceableWrapper#
  TestTraceModule.make_mask: TestTraceModule#make_mask().
  TestGraphGradientAccumulation.test_graph_gradient_state_binding_failure_is_atomic: TestGraphGradientAccumulation#test_graph_gradient_state_binding_failure_is_atomic().
  TestGraphGradientAccumulation.test_storage_keys_handle_fake_empty_and_nested_wrapper_tensors: TestGraphGradientAccumulation#test_storage_keys_handle_fake_empty_and_nested_wrapper_tensors().
  TestMinimalFXTracerDynamicShapes.test_rope_symbolic_positions_compile_fullgraph: TestMinimalFXTracerDynamicShapes#test_rope_symbolic_positions_compile_fullgraph().
  TestMinimalFXTracerDynamicShapes.test_mark_unbacked_shape_branch_rejected: TestMinimalFXTracerDynamicShapes#test_mark_unbacked_shape_branch_rejected().
  TestTraceModels.DTYPE: TestTraceModels#DTYPE.
  TestTraceModels.tearDown: TestTraceModels#tearDown().
  TestTraceModels.test_deepseek_v3_flex_attention.TinyFlexMLA.init_states: TestTraceModels#test_deepseek_v3_flex_attention().TinyFlexMLA#init_states().
  TestTraceFSDP._setup: TestTraceFSDP#_setup().
  TestAutogradGradVsBackwardFSDP.run_backward: TestAutogradGradVsBackwardFSDP#run_backward().
  TestAutogradGradVsBackwardFSDP.run_grad: TestAutogradGradVsBackwardFSDP#run_grad().
  TestTraceDTensor.f: TestTraceDTensor#f().
  TestTraceModels.BATCH_SIZE: TestTraceModels#BATCH_SIZE.
  TestGraphGradientAccumulation.train_step: TestGraphGradientAccumulation#train_step().
  TestTraceModule.train_step_closure: TestTraceModule#train_step_closure().
  TestTraceModule.make_mask_fn: TestTraceModule#make_mask_fn().
  TestTraceModels._flex_orig: TestTraceModels#_flex_orig.
  TestTraceModule.BATCH_SIZE: TestTraceModule#BATCH_SIZE.
  TestTraceModule.SEQ_LEN: TestTraceModule#SEQ_LEN.
  TestTraceDTensor.DTYPE: TestTraceDTensor#DTYPE.
  TestTraceDTensor._distribute_params: TestTraceDTensor#_distribute_params().
  TestMetadataPropagation.DTYPE: TestMetadataPropagation#DTYPE.
  TestTraceModels.SEQ_LEN: TestTraceModels#SEQ_LEN.
  _TraceableWrapper.__tensor_unflatten__: _TraceableWrapper#__tensor_unflatten__().
  TestGraphGradientAccumulation.test_graph_gradient_state_rejects_tied_parameters.TiedModel.__init__: TestGraphGradientAccumulation#test_graph_gradient_state_rejects_tied_parameters().TiedModel#__init__().
  ? TestGraphGradientAccumulation.test_graph_gradient_state_rejects_inplace_wgrad_modules_before_binding.InplaceWgradModel.__init__
  : TestGraphGradientAccumulation#test_graph_gradient_state_rejects_inplace_wgrad_modules_before_binding().InplaceWgradModel#__init__().
  TestGraphGradientAccumulation.test_accumulate_param_grads_clones_param_grad_when_requested: TestGraphGradientAccumulation#test_accumulate_param_grads_clones_param_grad_when_requested().
  TestMinimalFXTracerDynamicShapes.test_fakeify_input_copies_only_shape_annotations: TestMinimalFXTracerDynamicShapes#test_fakeify_input_copies_only_shape_annotations().
  TestMinimalFXTracerDynamicShapes.test_mark_dynamic_min_max_preserves_range: TestMinimalFXTracerDynamicShapes#test_mark_dynamic_min_max_preserves_range().
  TestMinimalFXTracerDynamicShapes.test_mark_dynamic_one_sided_ranges_preserve_bounds: TestMinimalFXTracerDynamicShapes#test_mark_dynamic_one_sided_ranges_preserve_bounds().
  TestMinimalFXTracerDynamicShapes.test_maybe_materialize_grad_for_param_layout_restores_param_strides: TestMinimalFXTracerDynamicShapes#test_maybe_materialize_grad_for_param_layout_restores_param_strides().
  TestMetadataPropagation.test_copy_fwd_metadata_uses_backward_tagging: TestMetadataPropagation#test_copy_fwd_metadata_uses_backward_tagging().
  TestTraceContextParallel.test_llama3_cp_only_codegen_all_gather_before_sdpa: TestTraceContextParallel#test_llama3_cp_only_codegen_all_gather_before_sdpa().
  TestGraphGradientAccumulation.run_microbatches: TestGraphGradientAccumulation#run_microbatches().
  TestTraceModule.LR: TestTraceModule#LR.
  TestReparametrizeOptimizer.DEVICE: TestReparametrizeOptimizer#DEVICE.
  TestReparametrizeOptimizer.train_step: TestReparametrizeOptimizer#train_step().
  TestTraceDTensor.forward: TestTraceDTensor#forward().
  TestTraceModels.NUM_STEPS: TestTraceModels#NUM_STEPS.
  TestTraceModels.LR: TestTraceModels#LR.
  make_train_step.train_step: make_train_step().train_step().
  _graph_placeholder_fake_inputs: _graph_placeholder_fake_inputs().
  _graph_fake_mode: _graph_fake_mode().
  SimpleMLP.embed: SimpleMLP#embed.
  SimpleMLP.fc1: SimpleMLP#fc1.
  SimpleMLP.fc2: SimpleMLP#fc2.
  TestGraphGradientAccumulation.test_graph_gradient_state_rejects_tied_parameters.TiedModel: TestGraphGradientAccumulation#test_graph_gradient_state_rejects_tied_parameters().TiedModel#
  TiedModel.weight: TiedModel#weight.
  TestGraphGradientAccumulation.test_graph_gradient_state_rejects_inplace_wgrad_modules_before_binding.InplaceWgradModel: TestGraphGradientAccumulation#test_graph_gradient_state_rejects_inplace_wgrad_modules_before_binding().InplaceWgradModel#
  TestGraphGradientAccumulation.test_graph_gradient_state_rejects_shared_parameter_storage.AliasedModel: TestGraphGradientAccumulation#test_graph_gradient_state_rejects_shared_parameter_storage().AliasedModel#
  TestGraphGradientAccumulation.test_graph_gradient_state_allows_empty_parameters.EmptyModel: TestGraphGradientAccumulation#test_graph_gradient_state_allows_empty_parameters().EmptyModel#
  TestTraceModule.NUM_STEPS: TestTraceModule#NUM_STEPS.
  TestTraceModule.fn: TestTraceModule#fn().
  TestTraceModule.mask_mod: TestTraceModule#mask_mod().
  TestReparametrizeOptimizer.DTYPE: TestReparametrizeOptimizer#DTYPE.
  TestMetadataPropagation.is_backward: TestMetadataPropagation#is_backward().
  TestTraceModels.test_deepseek_v3_flex_attention.TinyFlexMLA: TestTraceModels#test_deepseek_v3_flex_attention().TinyFlexMLA#
  TinyFlexMLA.embed: TinyFlexMLA#embed.
  TinyFlexMLA.proj: TinyFlexMLA#proj.
  TestTraceModels.forward: TestTraceModels#forward().
  TestTraceFSDP.world_size: TestTraceFSDP#world_size().
  TestTraceFSDP.train_step: TestTraceFSDP#train_step().
  TestAutogradGradVsBackwardFSDP.world_size: TestAutogradGradVsBackwardFSDP#world_size().
  SimpleMLP.__init__: SimpleMLP#__init__().
  _TraceableWrapper.elem: _TraceableWrapper#elem.
  _TraceableWrapper.__slots__: _TraceableWrapper#__slots__.
  _TraceableWrapper.__new__: _TraceableWrapper#__new__().
  _TraceableWrapper.__torch_dispatch__: _TraceableWrapper#__torch_dispatch__().
  _TraceableWrapper.__tensor_flatten__: _TraceableWrapper#__tensor_flatten__().
  TestGraphGradientAccumulation: TestGraphGradientAccumulation#
  TestGraphGradientAccumulation.test_graph_gradient_state_rejects_tied_parameters: TestGraphGradientAccumulation#test_graph_gradient_state_rejects_tied_parameters().
  TestGraphGradientAccumulation.test_graph_gradient_state_rejects_inplace_wgrad_modules_before_binding: TestGraphGradientAccumulation#test_graph_gradient_state_rejects_inplace_wgrad_modules_before_binding().
  TestGraphGradientAccumulation.test_graph_gradient_state_rejects_shared_parameter_storage: TestGraphGradientAccumulation#test_graph_gradient_state_rejects_shared_parameter_storage().
  TestGraphGradientAccumulation.test_graph_gradient_state_rejects_shared_parameter_storage.AliasedModel.__init__: TestGraphGradientAccumulation#test_graph_gradient_state_rejects_shared_parameter_storage().AliasedModel#__init__().
  AliasedModel.first: AliasedModel#first.
  TestGraphGradientAccumulation.test_graph_gradient_state_allows_empty_parameters: TestGraphGradientAccumulation#test_graph_gradient_state_allows_empty_parameters().
  TestGraphGradientAccumulation.test_graph_gradient_state_allows_empty_parameters.EmptyModel.__init__: TestGraphGradientAccumulation#test_graph_gradient_state_allows_empty_parameters().EmptyModel#__init__().
  EmptyModel.first: EmptyModel#first.
  TestMinimalFXTracerDynamicShapes: TestMinimalFXTracerDynamicShapes#
  TestTraceModule: TestTraceModule#
  TestTraceModule.setUp: TestTraceModule#setUp().
  TestTraceModule.tearDown: TestTraceModule#tearDown().
  TestReparametrizeOptimizer: TestReparametrizeOptimizer#
  TestTraceDTensor: TestTraceDTensor#
  TestTraceDTensor.setUp: TestTraceDTensor#setUp().
  TestTraceDTensor.tearDown: TestTraceDTensor#tearDown().
  TestMetadataPropagation: TestMetadataPropagation#
  TestMetadataPropagation.setUp: TestMetadataPropagation#setUp().
  TestTraceModels: TestTraceModels#
  TestTraceModels.setUp: TestTraceModels#setUp().
  TestTraceModels.test_deepseek_v3_flex_attention.TinyFlexMLA.__init__: TestTraceModels#test_deepseek_v3_flex_attention().TinyFlexMLA#__init__().
  TestTraceFSDP: TestTraceFSDP#
  TestTraceContextParallel: TestTraceContextParallel#
  TestTraceContextParallel.world_size: TestTraceContextParallel#world_size().
  TestAutogradGradVsBackwardFSDP: TestAutogradGradVsBackwardFSDP#
---
# Module: [`torchtitan/experiments/graph_trainer/tests/test_trace_module.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py)

> **Collapsed catalog** (182 symbols) — one row per symbol with its source line; member detail omitted. See the source link above, or the curated codebase page, for depth.

- <a id="AliasedModel.first"></a>`AliasedModel.first` — [`L511`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L511)
- <a id="AliasedModel.second"></a>`AliasedModel.second` — [`L512`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L512)
- <a id="EmptyModel.first"></a>`EmptyModel.first` — [`L524`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L524)
- <a id="EmptyModel.second"></a>`EmptyModel.second` — [`L525`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L525)
- <a id="InplaceWgradModel.projection"></a>`InplaceWgradModel.projection` — [`L483`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L483)
- <a id="SimpleMLP"></a>`SimpleMLP` — [`L119`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L119)
- <a id="SimpleMLP.__init__"></a>`SimpleMLP.__init__` — [`L120`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L120)
- <a id="SimpleMLP.embed"></a>`SimpleMLP.embed` — [`L122`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L122)
- <a id="SimpleMLP.fc1"></a>`SimpleMLP.fc1` — [`L123`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L123)
- <a id="SimpleMLP.fc2"></a>`SimpleMLP.fc2` — [`L124`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L124)
- <a id="SimpleMLP.forward"></a>`SimpleMLP.forward` — [`L126`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L126)
- <a id="TestAutogradGradVsBackwardFSDP"></a>`TestAutogradGradVsBackwardFSDP` — [`L2723`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2723)
- <a id="TestAutogradGradVsBackwardFSDP.run_backward"></a>`TestAutogradGradVsBackwardFSDP.run_backward` — [`L2778`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2778)
- <a id="TestAutogradGradVsBackwardFSDP.run_grad"></a>`TestAutogradGradVsBackwardFSDP.run_grad` — [`L2783`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2783)
- <a id="TestAutogradGradVsBackwardFSDP.test_peak_memory_identical_fsdp"></a>`TestAutogradGradVsBackwardFSDP.test_peak_memory_identical_fsdp` — [`L2730`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2730)
- <a id="TestAutogradGradVsBackwardFSDP.world_size"></a>`TestAutogradGradVsBackwardFSDP.world_size` — [`L2727`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2727)
- <a id="TestGraphGradientAccumulation"></a>`TestGraphGradientAccumulation` — [`L162`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L162)
- <a id="TestGraphGradientAccumulation.make_trainer"></a>`TestGraphGradientAccumulation.make_trainer` — [`L185`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L185)
- <a id="TestGraphGradientAccumulation.run_microbatches"></a>`TestGraphGradientAccumulation.run_microbatches` — [`L242`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L242)
- <a id="TestGraphGradientAccumulation.run_trainer"></a>`TestGraphGradientAccumulation.run_trainer` — [`L218`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L218)
- <a id="TestGraphGradientAccumulation.test_accumulate_param_grads_clones_param_grad_when_requested"></a>`TestGraphGradientAccumulation.test_accumulate_param_grads_clones_param_grad_when_requested` — [`L567`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L567)
- <a id="TestGraphGradientAccumulation.test_cuda_graph_numerics_match_external_accumulation"></a>`TestGraphGradientAccumulation.test_cuda_graph_numerics_match_external_accumulation` — [`L164`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L164)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_allows_empty_parameters"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_allows_empty_parameters` — [`L519`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L519)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_allows_empty_parameters.EmptyModel"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_allows_empty_parameters.EmptyModel` — [`L520`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L520)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_allows_empty_parameters.EmptyModel.__init__"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_allows_empty_parameters.EmptyModel.__init__` — [`L521`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L521)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_binding_failure_is_atomic"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_binding_failure_is_atomic` — [`L433`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L433)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_prepares_after_both_zero_grad_policies"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_prepares_after_both_zero_grad_policies` — [`L444`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L444)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_rejects_graph_state_replacement"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_rejects_graph_state_replacement` — [`L556`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L556)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_rejects_inplace_wgrad_modules_before_binding"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_rejects_inplace_wgrad_modules_before_binding` — [`L477`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L477)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_rejects_inplace_wgrad_modules_before_binding.InplaceWgradModel"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_rejects_inplace_wgrad_modules_before_binding.InplaceWgradModel` — [`L480`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L480)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_rejects_inplace_wgrad_modules_before_binding.InplaceWgradModel.__init__"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_rejects_inplace_wgrad_modules_before_binding.InplaceWgradModel.__init__` — [`L481`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L481)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_rejects_parameter_storage_replacement"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_rejects_parameter_storage_replacement` — [`L546`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L546)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_rejects_partial_grad_clear"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_rejects_partial_grad_clear` — [`L468`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L468)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_rejects_shared_parameter_storage"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_rejects_shared_parameter_storage` — [`L506`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L506)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_rejects_shared_parameter_storage.AliasedModel"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_rejects_shared_parameter_storage.AliasedModel` — [`L507`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L507)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_rejects_shared_parameter_storage.AliasedModel.__init__"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_rejects_shared_parameter_storage.AliasedModel.__init__` — [`L508`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L508)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_rejects_tied_parameters"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_rejects_tied_parameters` — [`L421`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L421)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_rejects_tied_parameters.TiedModel"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_rejects_tied_parameters.TiedModel` — [`L422`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L422)
- <a id="TestGraphGradientAccumulation.test_graph_gradient_state_rejects_tied_parameters.TiedModel.__init__"></a>`TestGraphGradientAccumulation.test_graph_gradient_state_rejects_tied_parameters.TiedModel.__init__` — [`L423`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L423)
- <a id="TestGraphGradientAccumulation.test_inplace_grad_accumulation_uses_stable_optimizer_buffers"></a>`TestGraphGradientAccumulation.test_inplace_grad_accumulation_uses_stable_optimizer_buffers` — [`L339`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L339)
- <a id="TestGraphGradientAccumulation.test_storage_keys_handle_fake_empty_and_nested_wrapper_tensors"></a>`TestGraphGradientAccumulation.test_storage_keys_handle_fake_empty_and_nested_wrapper_tensors` — [`L534`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L534)
- <a id="TestGraphGradientAccumulation.train_step"></a>`TestGraphGradientAccumulation.train_step` — [`L347`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L347)
- <a id="TestMetadataPropagation"></a>`TestMetadataPropagation` — [`L1657`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1657)
- <a id="TestMetadataPropagation.DEVICE"></a>`TestMetadataPropagation.DEVICE` — [`L1660`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1660)
- <a id="TestMetadataPropagation.DTYPE"></a>`TestMetadataPropagation.DTYPE` — [`L1661`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1661)
- <a id="TestMetadataPropagation.is_backward"></a>`TestMetadataPropagation.is_backward` — [`L1717`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1717)
- <a id="TestMetadataPropagation.setUp"></a>`TestMetadataPropagation.setUp` — [`L1663`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1663)
- <a id="TestMetadataPropagation.test_backward_nodes_have_seq_nr"></a>`TestMetadataPropagation.test_backward_nodes_have_seq_nr` — [`L1666`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1666)
- <a id="TestMetadataPropagation.test_backward_nodes_have_stack_trace"></a>`TestMetadataPropagation.test_backward_nodes_have_stack_trace` — [`L1749`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1749)
- <a id="TestMetadataPropagation.test_copy_fwd_metadata_propagates_custom"></a>`TestMetadataPropagation.test_copy_fwd_metadata_propagates_custom` — [`L1693`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1693)
- <a id="TestMetadataPropagation.test_copy_fwd_metadata_uses_backward_tagging"></a>`TestMetadataPropagation.test_copy_fwd_metadata_uses_backward_tagging` — [`L1734`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1734)
- <a id="TestMinimalFXTracerDynamicShapes"></a>`TestMinimalFXTracerDynamicShapes` — [`L583`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L583)
- <a id="TestMinimalFXTracerDynamicShapes._trace_mark_dynamic_value_range"></a>`TestMinimalFXTracerDynamicShapes._trace_mark_dynamic_value_range` — [`L584`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L584)
- <a id="TestMinimalFXTracerDynamicShapes.forward"></a>`TestMinimalFXTracerDynamicShapes.forward` — [`L587`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L587)
- <a id="TestMinimalFXTracerDynamicShapes.test_data_dependent_check_emits_runtime_asserts"></a>`TestMinimalFXTracerDynamicShapes.test_data_dependent_check_emits_runtime_asserts` — [`L941`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L941)
- <a id="TestMinimalFXTracerDynamicShapes.test_fakeify_input_copies_only_shape_annotations"></a>`TestMinimalFXTracerDynamicShapes.test_fakeify_input_copies_only_shape_annotations` — [`L608`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L608)
- <a id="TestMinimalFXTracerDynamicShapes.test_mark_dynamic_min_max_preserves_range"></a>`TestMinimalFXTracerDynamicShapes.test_mark_dynamic_min_max_preserves_range` — [`L627`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L627)
- <a id="TestMinimalFXTracerDynamicShapes.test_mark_dynamic_one_sided_ranges_preserve_bounds"></a>`TestMinimalFXTracerDynamicShapes.test_mark_dynamic_one_sided_ranges_preserve_bounds` — [`L633`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L633)
- <a id="TestMinimalFXTracerDynamicShapes.test_mark_dynamic_token_dim_with_rope"></a>`TestMinimalFXTracerDynamicShapes.test_mark_dynamic_token_dim_with_rope` — [`L683`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L683)
- <a id="TestMinimalFXTracerDynamicShapes.test_mark_dynamic_wrapper_subclass_rejected"></a>`TestMinimalFXTracerDynamicShapes.test_mark_dynamic_wrapper_subclass_rejected` — [`L649`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L649)
- <a id="TestMinimalFXTracerDynamicShapes.test_mark_unbacked_input_symbol_is_not_pending_fresh"></a>`TestMinimalFXTracerDynamicShapes.test_mark_unbacked_input_symbol_is_not_pending_fresh` — [`L869`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L869)
- <a id="TestMinimalFXTracerDynamicShapes.test_mark_unbacked_min_max_preserves_unbacked_placeholder_dim"></a>`TestMinimalFXTracerDynamicShapes.test_mark_unbacked_min_max_preserves_unbacked_placeholder_dim` — [`L842`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L842)
- <a id="TestMinimalFXTracerDynamicShapes.test_mark_unbacked_mixed_with_static_input_replay"></a>`TestMinimalFXTracerDynamicShapes.test_mark_unbacked_mixed_with_static_input_replay` — [`L797`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L797)
- <a id="TestMinimalFXTracerDynamicShapes.test_mark_unbacked_multiple_inputs_replay"></a>`TestMinimalFXTracerDynamicShapes.test_mark_unbacked_multiple_inputs_replay` — [`L918`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L918)
- <a id="TestMinimalFXTracerDynamicShapes.test_mark_unbacked_positions_token_dim_with_rope"></a>`TestMinimalFXTracerDynamicShapes.test_mark_unbacked_positions_token_dim_with_rope` — [`L731`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L731)
- <a id="TestMinimalFXTracerDynamicShapes.test_mark_unbacked_preserves_unbacked_placeholder_dim"></a>`TestMinimalFXTracerDynamicShapes.test_mark_unbacked_preserves_unbacked_placeholder_dim` — [`L889`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L889)
- <a id="TestMinimalFXTracerDynamicShapes.test_mark_unbacked_shape_branch_rejected"></a>`TestMinimalFXTracerDynamicShapes.test_mark_unbacked_shape_branch_rejected` — [`L824`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L824)
- <a id="TestMinimalFXTracerDynamicShapes.test_mark_unbacked_shape_id_multiple_inputs_replay"></a>`TestMinimalFXTracerDynamicShapes.test_mark_unbacked_shape_id_multiple_inputs_replay` — [`L982`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L982)
- <a id="TestMinimalFXTracerDynamicShapes.test_maybe_materialize_grad_for_param_layout_restores_param_strides"></a>`TestMinimalFXTracerDynamicShapes.test_maybe_materialize_grad_for_param_layout_restores_param_strides` — [`L784`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L784)
- <a id="TestMinimalFXTracerDynamicShapes.test_nested_wrapper_subclass_marked_inner_rejected"></a>`TestMinimalFXTracerDynamicShapes.test_nested_wrapper_subclass_marked_inner_rejected` — [`L664`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L664)
- <a id="TestMinimalFXTracerDynamicShapes.test_no_runtime_asserts_when_no_constraints"></a>`TestMinimalFXTracerDynamicShapes.test_no_runtime_asserts_when_no_constraints` — [`L963`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L963)
- <a id="TestMinimalFXTracerDynamicShapes.test_rope_symbolic_positions_compile_fullgraph"></a>`TestMinimalFXTracerDynamicShapes.test_rope_symbolic_positions_compile_fullgraph` — [`L765`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L765)
- <a id="TestReparametrizeOptimizer"></a>`TestReparametrizeOptimizer` — [`L1351`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1351)
- <a id="TestReparametrizeOptimizer.DEVICE"></a>`TestReparametrizeOptimizer.DEVICE` — [`L1361`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1361)
- <a id="TestReparametrizeOptimizer.DTYPE"></a>`TestReparametrizeOptimizer.DTYPE` — [`L1362`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1362)
- <a id="TestReparametrizeOptimizer.test_minimal_fx_tracer_with_bucketed_optimizer"></a>`TestReparametrizeOptimizer.test_minimal_fx_tracer_with_bucketed_optimizer` — [`L1433`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1433)
- <a id="TestReparametrizeOptimizer.test_titan_optimizers_container"></a>`TestReparametrizeOptimizer.test_titan_optimizers_container` — [`L1364`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1364)
- <a id="TestReparametrizeOptimizer.train_step"></a>`TestReparametrizeOptimizer.train_step` — [`L1447`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1447)
- <a id="TestTraceContextParallel"></a>`TestTraceContextParallel` — [`L2569`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2569)
- <a id="TestTraceContextParallel._trace_llama3_step_code"></a>`TestTraceContextParallel._trace_llama3_step_code` — [`L2574`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2574)
- <a id="TestTraceContextParallel.test_llama3_cp_only_codegen_all_gather_before_sdpa"></a>`TestTraceContextParallel.test_llama3_cp_only_codegen_all_gather_before_sdpa` — [`L2705`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2705)
- <a id="TestTraceContextParallel.world_size"></a>`TestTraceContextParallel.world_size` — [`L2571`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2571)
- <a id="TestTraceDTensor"></a>`TestTraceDTensor` — [`L1472`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1472)
- <a id="TestTraceDTensor.DEVICE"></a>`TestTraceDTensor.DEVICE` — [`L1473`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1473)
- <a id="TestTraceDTensor.DTYPE"></a>`TestTraceDTensor.DTYPE` — [`L1474`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1474)
- <a id="TestTraceDTensor._distribute_params"></a>`TestTraceDTensor._distribute_params` — [`L1496`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1496)
- <a id="TestTraceDTensor.f"></a>`TestTraceDTensor.f` — [`L1597`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1597)
- <a id="TestTraceDTensor.forward"></a>`TestTraceDTensor.forward` — [`L1519`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1519)
- <a id="TestTraceDTensor.setUp"></a>`TestTraceDTensor.setUp` — [`L1476`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1476)
- <a id="TestTraceDTensor.tearDown"></a>`TestTraceDTensor.tearDown` — [`L1489`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1489)
- <a id="TestTraceDTensor.test_dtensor_forward"></a>`TestTraceDTensor.test_dtensor_forward` — [`L1507`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1507)
- <a id="TestTraceDTensor.test_dtensor_mark_unbacked_rejected"></a>`TestTraceDTensor.test_dtensor_mark_unbacked_rejected` — [`L1532`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1532)
- <a id="TestTraceDTensor.test_dtensor_train_step"></a>`TestTraceDTensor.test_dtensor_train_step` — [`L1551`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1551)
- <a id="TestTraceDTensor.test_full_inductor_pass_migrates_cpu_attrs"></a>`TestTraceDTensor.test_full_inductor_pass_migrates_cpu_attrs` — [`L1612`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1612)
- <a id="TestTraceDTensor.test_full_inductor_pass_on_collective"></a>`TestTraceDTensor.test_full_inductor_pass_on_collective` — [`L1585`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1585)
- <a id="TestTraceFSDP"></a>`TestTraceFSDP` — [`L2254`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2254)
- <a id="TestTraceFSDP._run_fsdp_model_test"></a>`TestTraceFSDP._run_fsdp_model_test` — [`L2382`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2382)
- <a id="TestTraceFSDP._setup"></a>`TestTraceFSDP._setup` — [`L2259`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2259)
- <a id="TestTraceFSDP.parallel_dims"></a>`TestTraceFSDP.parallel_dims` — [`L2262`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2262)
- <a id="TestTraceFSDP.test_deepseek_v3_fsdp"></a>`TestTraceFSDP.test_deepseek_v3_fsdp` — [`L2505`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2505)
- <a id="TestTraceFSDP.test_gpt_oss_fsdp"></a>`TestTraceFSDP.test_gpt_oss_fsdp` — [`L2526`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2526)
- <a id="TestTraceFSDP.test_graph_gradient_accumulation_preserves_fsdp_layout"></a>`TestTraceFSDP.test_graph_gradient_accumulation_preserves_fsdp_layout` — [`L2273`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2273)
- <a id="TestTraceFSDP.test_llama3_fsdp"></a>`TestTraceFSDP.test_llama3_fsdp` — [`L2482`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2482)
- <a id="TestTraceFSDP.test_qwen3_fsdp"></a>`TestTraceFSDP.test_qwen3_fsdp` — [`L2491`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2491)
- <a id="TestTraceFSDP.train_step"></a>`TestTraceFSDP.train_step` — [`L2299`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2299)
- <a id="TestTraceFSDP.world_size"></a>`TestTraceFSDP.world_size` — [`L2256`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2256)
- <a id="TestTraceModels"></a>`TestTraceModels` — [`L1830`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1830)
- <a id="TestTraceModels.BATCH_SIZE"></a>`TestTraceModels.BATCH_SIZE` — [`L1833`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1833)
- <a id="TestTraceModels.DEVICE"></a>`TestTraceModels.DEVICE` — [`L1831`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1831)
- <a id="TestTraceModels.DTYPE"></a>`TestTraceModels.DTYPE` — [`L1832`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1832)
- <a id="TestTraceModels.LR"></a>`TestTraceModels.LR` — [`L1836`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1836)
- <a id="TestTraceModels.NUM_STEPS"></a>`TestTraceModels.NUM_STEPS` — [`L1835`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1835)
- <a id="TestTraceModels.SEQ_LEN"></a>`TestTraceModels.SEQ_LEN` — [`L1834`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1834)
- <a id="TestTraceModels._flex_orig"></a>`TestTraceModels._flex_orig` — [`L1841`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1841)
- <a id="TestTraceModels._run_bitwise_test"></a>`TestTraceModels._run_bitwise_test` — [`L1847`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1847)
- <a id="TestTraceModels._run_model_test"></a>`TestTraceModels._run_model_test` — [`L1909`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1909)
- <a id="TestTraceModels.forward"></a>`TestTraceModels.forward` — [`L2226`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2226)
- <a id="TestTraceModels.setUp"></a>`TestTraceModels.setUp` — [`L1838`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1838)
- <a id="TestTraceModels.tearDown"></a>`TestTraceModels.tearDown` — [`L1843`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1843)
- <a id="TestTraceModels.test_deepseek_v3"></a>`TestTraceModels.test_deepseek_v3` — [`L1989`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1989)
- <a id="TestTraceModels.test_deepseek_v3_flex_attention"></a>`TestTraceModels.test_deepseek_v3_flex_attention` — [`L2009`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2009)
- <a id="TestTraceModels.test_deepseek_v3_flex_attention.TinyFlexMLA"></a>`TestTraceModels.test_deepseek_v3_flex_attention.TinyFlexMLA` — [`L2035`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2035)
- <a id="TestTraceModels.test_deepseek_v3_flex_attention.TinyFlexMLA.__init__"></a>`TestTraceModels.test_deepseek_v3_flex_attention.TinyFlexMLA.__init__` — [`L2036`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2036)
- <a id="TestTraceModels.test_deepseek_v3_flex_attention.TinyFlexMLA.forward"></a>`TestTraceModels.test_deepseek_v3_flex_attention.TinyFlexMLA.forward` — [`L2085`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2085)
- <a id="TestTraceModels.test_deepseek_v3_flex_attention.TinyFlexMLA.init_states"></a>`TestTraceModels.test_deepseek_v3_flex_attention.TinyFlexMLA.init_states` — [`L2080`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2080)
- <a id="TestTraceModels.test_flex_attention_annotations"></a>`TestTraceModels.test_flex_attention_annotations` — [`L2187`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2187)
- <a id="TestTraceModels.test_gpt_oss"></a>`TestTraceModels.test_gpt_oss` — [`L2141`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2141)
- <a id="TestTraceModels.test_llama3"></a>`TestTraceModels.test_llama3` — [`L1952`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1952)
- <a id="TestTraceModels.test_qwen3"></a>`TestTraceModels.test_qwen3` — [`L1961`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1961)
- <a id="TestTraceModels.test_qwen3_moe"></a>`TestTraceModels.test_qwen3_moe` — [`L1975`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1975)
- <a id="TestTraceModule"></a>`TestTraceModule` — [`L1008`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1008)
- <a id="TestTraceModule.BATCH_SIZE"></a>`TestTraceModule.BATCH_SIZE` — [`L1011`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1011)
- <a id="TestTraceModule.DEVICE"></a>`TestTraceModule.DEVICE` — [`L1009`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1009)
- <a id="TestTraceModule.DTYPE"></a>`TestTraceModule.DTYPE` — [`L1010`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1010)
- <a id="TestTraceModule.LR"></a>`TestTraceModule.LR` — [`L1014`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1014)
- <a id="TestTraceModule.NUM_STEPS"></a>`TestTraceModule.NUM_STEPS` — [`L1013`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1013)
- <a id="TestTraceModule.SEQ_LEN"></a>`TestTraceModule.SEQ_LEN` — [`L1012`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1012)
- <a id="TestTraceModule._make_mlp"></a>`TestTraceModule._make_mlp` — [`L1023`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1023)
- <a id="TestTraceModule.fn"></a>`TestTraceModule.fn` — [`L1145`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1145)
- <a id="TestTraceModule.forward"></a>`TestTraceModule.forward` — [`L1036`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1036)
- <a id="TestTraceModule.make_mask"></a>`TestTraceModule.make_mask` — [`L1280`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1280)
- <a id="TestTraceModule.make_mask_fn"></a>`TestTraceModule.make_mask_fn` — [`L1270`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1270)
- <a id="TestTraceModule.mask_mod"></a>`TestTraceModule.mask_mod` — [`L1271`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1271)
- <a id="TestTraceModule.setUp"></a>`TestTraceModule.setUp` — [`L1016`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1016)
- <a id="TestTraceModule.tearDown"></a>`TestTraceModule.tearDown` — [`L1020`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1020)
- <a id="TestTraceModule.test_chunked_loss_train_step"></a>`TestTraceModule.test_chunked_loss_train_step` — [`L1065`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1065)
- <a id="TestTraceModule.test_flex_attention_block_mask_mark_unbacked"></a>`TestTraceModule.test_flex_attention_block_mask_mark_unbacked` — [`L1260`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1260)
- <a id="TestTraceModule.test_kwargs_default_omitted_bakes_constant"></a>`TestTraceModule.test_kwargs_default_omitted_bakes_constant` — [`L1220`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1220)
- <a id="TestTraceModule.test_kwargs_roundtrip"></a>`TestTraceModule.test_kwargs_roundtrip` — [`L1174`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1174)
- <a id="TestTraceModule.test_kwargs_runtime_reorder_raises"></a>`TestTraceModule.test_kwargs_runtime_reorder_raises` — [`L1189`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1189)
- <a id="TestTraceModule.test_kwargs_unknown_kwarg_raises"></a>`TestTraceModule.test_kwargs_unknown_kwarg_raises` — [`L1206`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1206)
- <a id="TestTraceModule.test_kwargs_var_keyword_missing_key_raises"></a>`TestTraceModule.test_kwargs_var_keyword_missing_key_raises` — [`L1240`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1240)
- <a id="TestTraceModule.test_mismatched_module_raises_when_validation_enabled"></a>`TestTraceModule.test_mismatched_module_raises_when_validation_enabled` — [`L1151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1151)
- <a id="TestTraceModule.test_mlp_forward"></a>`TestTraceModule.test_mlp_forward` — [`L1033`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1033)
- <a id="TestTraceModule.test_mlp_multistep_bitwise"></a>`TestTraceModule.test_mlp_multistep_bitwise` — [`L1106`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1106)
- <a id="TestTraceModule.test_mlp_train_step"></a>`TestTraceModule.test_mlp_train_step` — [`L1044`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1044)
- <a id="TestTraceModule.test_module_in_args_raises"></a>`TestTraceModule.test_module_in_args_raises` — [`L1338`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1338)
- <a id="TestTraceModule.test_non_tensor_leaf_raises"></a>`TestTraceModule.test_non_tensor_leaf_raises` — [`L1139`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1139)
- <a id="TestTraceModule.test_optimizer_passed_without_module_raises"></a>`TestTraceModule.test_optimizer_passed_without_module_raises` — [`L1168`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1168)
- <a id="TestTraceModule.train_step"></a>`TestTraceModule.train_step` — [`L1084`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1084)
- <a id="TestTraceModule.train_step_closure"></a>`TestTraceModule.train_step_closure` — [`L1095`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1095)
- <a id="TiedModel.tied_weight"></a>`TiedModel.tied_weight` — [`L426`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L426)
- <a id="TiedModel.weight"></a>`TiedModel.weight` — [`L425`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L425)
- <a id="TinyFlexMLA.attn"></a>`TinyFlexMLA.attn` — [`L2043`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2043)
- <a id="TinyFlexMLA.embed"></a>`TinyFlexMLA.embed` — [`L2038`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2038)
- <a id="TinyFlexMLA.proj"></a>`TinyFlexMLA.proj` — [`L2078`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L2078)
- <a id="_TraceableWrapper"></a>`_TraceableWrapper` — [`L130`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L130)
- <a id="_TraceableWrapper.__new__"></a>`_TraceableWrapper.__new__` — [`L136`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L136)
- <a id="_TraceableWrapper.__slots__"></a>`_TraceableWrapper.__slots__` — [`L133`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L133)
- <a id="_TraceableWrapper.__tensor_flatten__"></a>`_TraceableWrapper.__tensor_flatten__` — [`L154`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L154)
- <a id="_TraceableWrapper.__tensor_unflatten__"></a>`_TraceableWrapper.__tensor_unflatten__` — [`L158`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L158)
- <a id="_TraceableWrapper.__torch_dispatch__"></a>`_TraceableWrapper.__torch_dispatch__` — [`L151`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L151)
- <a id="_TraceableWrapper.elem"></a>`_TraceableWrapper.elem` — [`L131`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L131)
- <a id="_apply_regional_inductor"></a>`_apply_regional_inductor` — [`L75`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L75)
- <a id="_disable_flex_autotune"></a>`_disable_flex_autotune` — [`L1797`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1797)
- <a id="_graph_fake_mode"></a>`_graph_fake_mode` — [`L108`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L108)
- <a id="_graph_placeholder_fake_inputs"></a>`_graph_placeholder_fake_inputs` — [`L96`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L96)
- <a id="_restore_flex_autotune"></a>`_restore_flex_autotune` — [`L1823`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L1823)
- <a id="create_model"></a>`create_model` — [`L67`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L67)
- <a id="get_loss"></a>`get_loss` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L45)
- <a id="make_train_step"></a>`make_train_step` — [`L53`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L53)
- <a id="make_train_step.train_step"></a>`make_train_step.train_step` — [`L56`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/graph_trainer/tests/test_trace_module.py#L56)
