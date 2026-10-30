---
title: 'Module: torchtitan/experiments/rl/models/vllm_wrapper.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/models/vllm_wrapper.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.models.vllm_wrapper`/
symbols:
  VLLMModelWrapper.parallel_dims: VLLMModelWrapper#parallel_dims.
  _replace_vllm_layer_configs: _replace_vllm_layer_configs().
  VLLMModelWrapper._maybe_initial_load_weights: VLLMModelWrapper#_maybe_initial_load_weights().
  VLLMModelWrapper.model: VLLMModelWrapper#model.
  VLLMModelWrapper.__init__._InferenceConfig.training: VLLMModelWrapper#__init__()._InferenceConfig#training.
  VLLMModelWrapper._checkpoint_config: VLLMModelWrapper#_checkpoint_config.
  VLLMModelWrapper.config: VLLMModelWrapper#config.
  VLLMModelWrapper.compute_logits: VLLMModelWrapper#compute_logits().
  VLLMModelWrapper.__init__: VLLMModelWrapper#__init__().
  _patch_vllm_all_reduce: _patch_vllm_all_reduce().
  VLLMModelWrapper._inject_attention_sinks: VLLMModelWrapper#_inject_attention_sinks().
  PlainToDTensorStateDictAdapter.to_hf: PlainToDTensorStateDictAdapter#to_hf().
  VLLMModelWrapper: VLLMModelWrapper#
  VLLMModelWrapper.get_state_dict_layouts: VLLMModelWrapper#get_state_dict_layouts().
  VLLMModelWrapper.spmd_context: VLLMModelWrapper#spmd_context.
  PlainToDTensorStateDictAdapter.from_hf: PlainToDTensorStateDictAdapter#from_hf().
  PlainToDTensorStateDictAdapter.parallel_dims: PlainToDTensorStateDictAdapter#parallel_dims.
  VLLMModelWrapper.embed_input_ids: VLLMModelWrapper#embed_input_ids().
  PlainToDTensorStateDictAdapter.__init__: PlainToDTensorStateDictAdapter#__init__().
  PlainToDTensorStateDictAdapter.get_hf_storage_reader: PlainToDTensorStateDictAdapter#get_hf_storage_reader().
  VLLMModelWrapper.forward: VLLMModelWrapper#forward().
  VLLMModelWrapper.load_weights: VLLMModelWrapper#load_weights().
  VLLMModelWrapper.state_dict_adapter: VLLMModelWrapper#state_dict_adapter.
  PlainToDTensorStateDictAdapter: PlainToDTensorStateDictAdapter#
  _dtensor_safe_weak_ref_tensor: _dtensor_safe_weak_ref_tensor().
  VLLMModelWrapper.parallelize_fn: VLLMModelWrapper#parallelize_fn.
  VLLMModelWrapper.__init__._InferenceConfig: VLLMModelWrapper#__init__()._InferenceConfig#
  VLLMModelWrapper.__init__._InferenceConfig.parallelism: VLLMModelWrapper#__init__()._InferenceConfig#parallelism.
  logger: logger.
  PlainToDTensorStateDictAdapter.adapter: PlainToDTensorStateDictAdapter#adapter.
  _tp_all_reduce_patched: _tp_all_reduce_patched.
  VLLMModelWrapper.get_input_embeddings: VLLMModelWrapper#get_input_embeddings().
  PlainToDTensorStateDictAdapter.state_dict_layouts: PlainToDTensorStateDictAdapter#state_dict_layouts.
  _original_weak_ref_tensor: _original_weak_ref_tensor.
  _patch_vllm_all_reduce.all_reduce: _patch_vllm_all_reduce().all_reduce().
  _patch_vllm_all_reduce.custom_all_reduce: _patch_vllm_all_reduce().custom_all_reduce().
  _patch_vllm_all_reduce.redistribute: _patch_vllm_all_reduce().redistribute().
  VLLMModelWrapper.is_text_generation_model: VLLMModelWrapper#is_text_generation_model.
  VLLMModelWrapper.supports_pp: VLLMModelWrapper#supports_pp.
  VLLMModelWrapper.supports_multimodal: VLLMModelWrapper#supports_multimodal.
---
# Module: [`torchtitan/experiments/rl/models/vllm_wrapper.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py)

## Classes
### <a id="PlainToDTensorStateDictAdapter"></a>`PlainToDTensorStateDictAdapter`  ·  implements/extends BaseStateDictAdapter
- def: [`torchtitan/experiments/rl/models/vllm_wrapper.py:122`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L122)
- doc: Add plain local tensor handling to a model-format state-dict adapter.
- signature: `class PlainToDTensorStateDictAdapter(BaseStateDictAdapter):`
- members:
  - <a id="PlainToDTensorStateDictAdapter.from_hf"></a>`from_hf(self, hf_state_dict: dict[str, Any])` — [`L146`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L146)
  - <a id="PlainToDTensorStateDictAdapter.get_hf_storage_reader"></a>`get_hf_storage_reader(self, path: str, from_quantized: bool = False)` — [`L149`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L149)
  - <a id="PlainToDTensorStateDictAdapter.to_hf"></a>`to_hf(self, state_dict: dict[str, Any])` — [`L137`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L137)
  - <a id="PlainToDTensorStateDictAdapter.adapter"></a>`adapter` — [`L131`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L131)
  - <a id="PlainToDTensorStateDictAdapter.parallel_dims"></a>`parallel_dims` — [`L133`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L133)
  - <a id="PlainToDTensorStateDictAdapter.state_dict_layouts"></a>`state_dict_layouts` — [`L132`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L132)
- protocol/private: <a id="PlainToDTensorStateDictAdapter.__init__"></a>`__init__`[`L125`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L125)
- uses (calls/refs, reference-scoped): [`ParallelDims`](../../../distributed/parallel_dims.md#ParallelDims), [`to_hf`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf), [`fqn_to_index_mapping`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.fqn_to_index_mapping), [`BaseStateDictAdapter`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter), [`plain_tensor_to_dtensor_state_dict`](../../../distributed/spmd_types.md#plain_tensor_to_dtensor_state_dict), [`get_hf_storage_reader`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.get_hf_storage_reader), [`hf_assets_path`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.hf_assets_path), [`dtensor_to_plain_tensor_state_dict`](../../../distributed/spmd_types.md#dtensor_to_plain_tensor_state_dict)
- used by: [`to_hf`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.to_hf), [`from_hf`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.from_hf), [`_maybe_initial_load_weights`](vllm_wrapper.md#VLLMModelWrapper._maybe_initial_load_weights), [`BaseStateDictAdapter`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter), [`get_hf_storage_reader`](../../../protocols/state_dict_adapter.md#BaseStateDictAdapter.get_hf_storage_reader)

### <a id="VLLMModelWrapper"></a>`VLLMModelWrapper`  ·  implements/extends Module
- def: [`torchtitan/experiments/rl/models/vllm_wrapper.py:268`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L268)
- doc: Generic vLLM-compatible model wrapper for TorchTitan models. Implemented
- signature: `class VLLMModelWrapper(Module):`
- members:
  - <a id="VLLMModelWrapper._inject_attention_sinks"></a>`_inject_attention_sinks(self)` — [`L415`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L415) — Give each gpt-oss attention's vLLM backend its sink-rescale hook.
  - <a id="VLLMModelWrapper._maybe_initial_load_weights"></a>`_maybe_initial_load_weights(self)` — [`L534`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L534) — Load initial HF weights via CheckpointManager.
  - <a id="VLLMModelWrapper.compute_logits"></a>`compute_logits(self, hidden_states: torch.Tensor, sampling_metadata=None)` — [`L484`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L484) — vLLM required API.
  - <a id="VLLMModelWrapper.embed_input_ids"></a>`embed_input_ids(self, input_ids: torch.Tensor)` — [`L431`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L431) — vLLM required API.
  - <a id="VLLMModelWrapper.forward"></a>`forward(self, input_ids: torch.Tensor | None = None, positions: torch.Tensor | None = None, inputs_embeds: torch.Tensor | None = None, **kwargs)` — [`L442`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L442) — vLLM required API.
  - <a id="VLLMModelWrapper.get_input_embeddings"></a>`get_input_embeddings(self, input_ids: torch.Tensor)` — [`L437`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L437) — vLLM required API.
  - <a id="VLLMModelWrapper.get_state_dict_layouts"></a>`get_state_dict_layouts(self)` — [`L577`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L577) — Return SPMD layouts keyed by the model's exposed state-dict names.
  - <a id="VLLMModelWrapper.load_weights"></a>`load_weights(self, weights_iter)` — [`L633`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L633) — vLLM required API.
  - <a id="VLLMModelWrapper.config"></a>`config` — [`L306`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L306)
  - <a id="VLLMModelWrapper.is_text_generation_model"></a>`is_text_generation_model` — [`L283`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L283)
  - <a id="VLLMModelWrapper.model"></a>`model` — [`L367`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L367)
  - <a id="VLLMModelWrapper.parallel_dims"></a>`parallel_dims` — [`L316`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L316)
  - <a id="VLLMModelWrapper.parallelize_fn"></a>`parallelize_fn` — [`L304`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L304)
  - <a id="VLLMModelWrapper.spmd_context"></a>`spmd_context` — [`L327`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L327)
  - <a id="VLLMModelWrapper.state_dict_adapter"></a>`state_dict_adapter` — [`L303`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L303)
  - <a id="VLLMModelWrapper.supports_multimodal"></a>`supports_multimodal` — [`L285`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L285)
  - <a id="VLLMModelWrapper.supports_pp"></a>`supports_pp` — [`L284`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L284)
- protocol/private: <a id="VLLMModelWrapper.__init__"></a>`__init__`[`L287`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L287), <a id="VLLMModelWrapper._checkpoint_config"></a>`_checkpoint_config`[`L384`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L384)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`TrainingConfig`](../../../config/configs.md#TrainingConfig), [`model`](../../../protocols/model_spec.md#ModelSpec.model), [`ParallelDims`](../../../distributed/parallel_dims.md#ParallelDims), [`build`](../../../config/configurable.md#Configurable.Config.build), [`CheckpointManager`](../../../components/checkpointer/dcp.md#CheckpointManager), [`CompileConfig`](../../../config/configs.md#CompileConfig), [`Config`](../../../components/checkpointer/dcp.md#CheckpointManager.Config), [`ModelSpec`](../../../protocols/model_spec.md#ModelSpec), [`data_parallel_shard_degree`](../../../config/configs.md#ParallelismConfig.data_parallel_shard_degree), [`tensor_parallel_degree`](../../../config/configs.md#ParallelismConfig.tensor_parallel_degree), [`expert_parallel_degree`](../../../config/configs.md#ParallelismConfig.expert_parallel_degree), [`spmd_backend`](../../../config/configs.md#ParallelismConfig.spmd_backend), [`enable`](../../../components/checkpointer/base.md#BaseCheckpointManager.Config.enable), [`get_mesh`](../../../distributed/parallel_dims.md#ParallelDims.get_mesh), [`parallelize_fn`](../../../protocols/model_spec.md#ModelSpec.parallelize_fn), [`context_parallel_degree`](../../../config/configs.md#ParallelismConfig.context_parallel_degree), [`pp`](../../../distributed/parallel_dims.md#ParallelDims.pp), [`pipeline_parallel_degree`](../../../config/configs.md#ParallelismConfig.pipeline_parallel_degree), [`tp`](../../../distributed/parallel_dims.md#ParallelDims.tp), [`cp`](../../../distributed/parallel_dims.md#ParallelDims.cp), [`dp_shard`](../../../distributed/parallel_dims.md#ParallelDims.dp_shard), [`ep`](../../../distributed/parallel_dims.md#ParallelDims.ep), [`dp_replicate`](../../../distributed/parallel_dims.md#ParallelDims.dp_replicate), [`world_size`](../../../distributed/parallel_dims.md#ParallelDims.world_size), [`_replace_vllm_layer_configs`](vllm_wrapper.md#_replace_vllm_layer_configs), [`spmd_backend`](../../../distributed/parallel_dims.md#ParallelDims.spmd_backend), [`to_training`](vllm_registry.md#InferenceParallelismConfig.to_training), [`state_dict_adapter`](../../../protocols/model_spec.md#ModelSpec.state_dict_adapter), [`InferenceParallelismConfig`](vllm_registry.md#InferenceParallelismConfig), [`tp_enabled`](../../../distributed/parallel_dims.md#ParallelDims.tp_enabled), [`FusedQKVLinear`](../../../models/common/attention.md#FusedQKVLinear), [`data_parallel_replicate_degree`](../../../config/configs.md#ParallelismConfig.data_parallel_replicate_degree), [`OverrideConfig`](../../../config/override.md#OverrideConfig), [`current_spmd_mesh`](../../../distributed/spmd_types.md#current_spmd_mesh), [`is_in_batch_invariant_mode`](../../../distributed/utils.md#is_in_batch_invariant_mode), [`initial_load_path`](../../../components/checkpointer/base.md#BaseCheckpointManager.Config.initial_load_path), [`get_spmd_context`](../../../distributed/utils.md#get_spmd_context), [`_patch_vllm_all_reduce`](vllm_wrapper.md#_patch_vllm_all_reduce), [`set_spmd_backend`](../../../distributed/utils.md#set_spmd_backend)  (+8 more)
- used by: [`Module`](../../../protocols/module.md#Module), [`register_to_vllm`](vllm_registry.md#register_to_vllm), [`training`](vllm_wrapper.md#VLLMModelWrapper.__init__._InferenceConfig.training), [`VLLMModelFromSpec`](vllm_registry.md#register_to_vllm.VLLMModelFromSpec), [`__init__`](vllm_registry.md#register_to_vllm.VLLMModelFromSpec.__init__)  (1 test-only)

### <a id="VLLMModelWrapper.__init__._InferenceConfig"></a>`VLLMModelWrapper.__init__._InferenceConfig`
- def: [`torchtitan/experiments/rl/models/vllm_wrapper.py:339`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L339)
- signature: `class _InferenceConfig:`
- members:
  - <a id="VLLMModelWrapper.__init__._InferenceConfig.parallelism"></a>`parallelism` — [`L340`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L340)
  - <a id="VLLMModelWrapper.__init__._InferenceConfig.training"></a>`training` — [`L343`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L343)
- uses (calls/refs, reference-scoped): [`ParallelismConfig`](../../../config/configs.md#ParallelismConfig), [`TrainingConfig`](../../../config/configs.md#TrainingConfig), [`max_context_length`](../../../config/configs.md#TrainingConfig.max_context_length), [`num_tokens_per_microbatch_per_dp_rank`](../../../config/configs.md#TrainingConfig.num_tokens_per_microbatch_per_dp_rank), [`apply_overrides`](../../../config/override.md#apply_overrides), [`imports`](../../../config/override.md#OverrideConfig.imports), [`config`](vllm_wrapper.md#VLLMModelWrapper.config)

## Functions
- <a id="_dtensor_safe_weak_ref_tensor"></a>`_dtensor_safe_weak_ref_tensor(tensor)` — [`L167`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L167)
- <a id="_patch_vllm_all_reduce"></a>`_patch_vllm_all_reduce()` — [`L181`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L181) — Route the generator's tensor-parallel all-reduce through vLLM's custom
- <a id="_replace_vllm_layer_configs"></a>`_replace_vllm_layer_configs(model_config)` — [`L57`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L57) — Replace inner-computation configs with vLLM generation variants.
- <a id="_patch_vllm_all_reduce.all_reduce"></a>`all_reduce(input, reduce_op, group_name)` — [`L220`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L220)
- <a id="_patch_vllm_all_reduce.custom_all_reduce"></a>`custom_all_reduce(input)` — [`L238`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L238)
- <a id="_patch_vllm_all_reduce.redistribute"></a>`redistribute(x, group, *, src, dst, **kwargs)` — [`L248`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L248)

## Module values
- <a id="_original_weak_ref_tensor"></a>`_original_weak_ref_tensor` — [`L164`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L164)
- <a id="_tp_all_reduce_patched"></a>`_tp_all_reduce_patched` — [`L178`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L178)
- <a id="logger"></a>`logger` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_wrapper.py#L54)

