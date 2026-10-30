---
title: 'Module: torchtitan/experiments/rl/models/vllm_registry.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/rl/models/vllm_registry.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.rl.models.vllm_registry`/
symbols:
  register_to_vllm: register_to_vllm().
  InferenceParallelismConfig.to_training: InferenceParallelismConfig#to_training().
  InferenceParallelismConfig: InferenceParallelismConfig#
  InferenceParallelismConfig.tensor_parallel_degree: InferenceParallelismConfig#tensor_parallel_degree.
  InferenceParallelismConfig.data_parallel_degree: InferenceParallelismConfig#data_parallel_degree.
  _configure_gdn_hybrid_model: _configure_gdn_hybrid_model().
  model_spec_to_hf_config_dict: model_spec_to_hf_config_dict().
  InferenceParallelismConfig.expert_parallel_degree: InferenceParallelismConfig#expert_parallel_degree.
  InferenceParallelismConfig.expert_sequence_parallel_size: InferenceParallelismConfig#expert_sequence_parallel_size().
  TORCHTITAN_CONFIG_FORMAT: TORCHTITAN_CONFIG_FORMAT.
  VLLM_MODEL_NAME: VLLM_MODEL_NAME.
  register_to_vllm.VLLMModelFromSpec: register_to_vllm().VLLMModelFromSpec#
  TORCHTITAN_WORKER_CLS: TORCHTITAN_WORKER_CLS.
  InferenceParallelismConfig.enable_sequence_parallel: InferenceParallelismConfig#enable_sequence_parallel.
  register_to_vllm.VLLMModelFromSpec.__init__: register_to_vllm().VLLMModelFromSpec#__init__().
  register_to_vllm.TorchTitanConfigParser: register_to_vllm().TorchTitanConfigParser#
  register_to_vllm.TorchTitanConfigParser.parse: register_to_vllm().TorchTitanConfigParser#parse().
  InferenceParallelismConfig.spmd_backend: InferenceParallelismConfig#spmd_backend.
  _configure_gdn_hybrid_model.get_state_shape: _configure_gdn_hybrid_model().get_state_shape().
  _configure_gdn_hybrid_model.get_state_dtype: _configure_gdn_hybrid_model().get_state_dtype().
  _configure_gdn_hybrid_model.get_state_copy_func: _configure_gdn_hybrid_model().get_state_copy_func().
  _configure_gdn_hybrid_model.get_state_copy_funcs: _configure_gdn_hybrid_model().get_state_copy_funcs().
---
# Module: [`torchtitan/experiments/rl/models/vllm_registry.py`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py)

## Classes
### <a id="InferenceParallelismConfig"></a>`InferenceParallelismConfig`
- def: [`torchtitan/experiments/rl/models/vllm_registry.py:52`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L52) — documented in [rl-training](../../../../../concepts/rl-training.md)
- doc: Parallelism for vLLM inference — a focused subset of the training
- signature: `class InferenceParallelismConfig:`
- members:
  - <a id="InferenceParallelismConfig.expert_sequence_parallel_size"></a>`expert_sequence_parallel_size(self)` — [`L83`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L83) — TP-axis shard count used internally by expert-parallel MoE.
  - <a id="InferenceParallelismConfig.to_training"></a>`to_training(self)` — [`L89`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L89) — Translate to the training ``ParallelismConfig`` for utils that need
  - <a id="InferenceParallelismConfig.data_parallel_degree"></a>`data_parallel_degree` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L66) — ---
  - <a id="InferenceParallelismConfig.enable_sequence_parallel"></a>`enable_sequence_parallel` — [`L76`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L76) — ---
  - <a id="InferenceParallelismConfig.expert_parallel_degree"></a>`expert_parallel_degree` — [`L73`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L73) — ---
  - <a id="InferenceParallelismConfig.spmd_backend"></a>`spmd_backend` — [`L79`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L79) — ---
  - <a id="InferenceParallelismConfig.tensor_parallel_degree"></a>`tensor_parallel_degree` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L70) — ---
- uses (calls/refs, reference-scoped): [`ParallelismConfig`](../../../config/configs.md#ParallelismConfig), [`data_parallel_shard_degree`](../../../config/configs.md#ParallelismConfig.data_parallel_shard_degree), [`tensor_parallel_degree`](../../../config/configs.md#ParallelismConfig.tensor_parallel_degree), [`expert_parallel_degree`](../../../config/configs.md#ParallelismConfig.expert_parallel_degree), [`spmd_backend`](../../../config/configs.md#ParallelismConfig.spmd_backend), [`context_parallel_degree`](../../../config/configs.md#ParallelismConfig.context_parallel_degree), [`pipeline_parallel_degree`](../../../config/configs.md#ParallelismConfig.pipeline_parallel_degree), [`data_parallel_replicate_degree`](../../../config/configs.md#ParallelismConfig.data_parallel_replicate_degree), [`enable_sequence_parallel`](../../../config/configs.md#ParallelismConfig.enable_sequence_parallel)
- used by: [`model_path`](../actors/generator.md#VLLMGenerator.model_path), [`trainer_dp_degree`](../controller.md#Controller.trainer_dp_degree), [`_multi_node`](../../tpu/rl_nc_ray/grpo.md#RayController._multi_node), [`parallelism`](../actors/generator.md#VLLMGenerator.Config.parallelism), [`register_to_vllm`](vllm_registry.md#register_to_vllm), [`__post_init__`](../actors/generator.md#VLLMGenerator.Config.__post_init__), [`config`](vllm_wrapper.md#VLLMModelWrapper.config), [`__init__`](vllm_wrapper.md#VLLMModelWrapper.__init__), [`_dp_degree`](../actors/generator.md#VLLMGenerator._dp_degree), [`_compute_generator_world_size`](../train.md#_compute_generator_world_size)  (26 test-only)

### <a id="register_to_vllm.TorchTitanConfigParser"></a>`register_to_vllm.TorchTitanConfigParser`
- def: [`torchtitan/experiments/rl/models/vllm_registry.py:343`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L343)
- signature: `class TorchTitanConfigParser(ConfigParserBase):`
- members:
  - <a id="register_to_vllm.TorchTitanConfigParser.parse"></a>`parse(self, model, trust_remote_code, revision=None, code_revision=None, **kwargs)` — [`L344`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L344)
- uses (calls/refs, reference-scoped): [`model_spec_to_hf_config_dict`](vllm_registry.md#model_spec_to_hf_config_dict), [`TORCHTITAN_CONFIG_FORMAT`](vllm_registry.md#TORCHTITAN_CONFIG_FORMAT)

### <a id="register_to_vllm.VLLMModelFromSpec"></a>`register_to_vllm.VLLMModelFromSpec`  ·  implements/extends VLLMModelWrapper
- def: [`torchtitan/experiments/rl/models/vllm_registry.py:319`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L319)
- signature: `class VLLMModelFromSpec(VLLMModelWrapper):`
- protocol/private: <a id="register_to_vllm.VLLMModelFromSpec.__init__"></a>`__init__`[`L320`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L320)
- uses (calls/refs, reference-scoped): [`__init__`](vllm_wrapper.md#VLLMModelWrapper.__init__), [`VLLMModelWrapper`](vllm_wrapper.md#VLLMModelWrapper)
- used by: [`register_to_vllm`](vllm_registry.md#register_to_vllm), [`VLLMModelWrapper`](vllm_wrapper.md#VLLMModelWrapper)

## Functions
- <a id="_configure_gdn_hybrid_model"></a>`_configure_gdn_hybrid_model(model_cls: type, model_spec: ModelSpec)` — [`L184`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L184) — Attach vLLM's hybrid-state interface when the model contains GDN layers.
- <a id="_configure_gdn_hybrid_model.get_state_copy_func"></a>`get_state_copy_func(cls)` — [`L244`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L244)
- <a id="_configure_gdn_hybrid_model.get_state_copy_funcs"></a>`get_state_copy_funcs(cls, mamba_types)` — [`L249`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L249)
- <a id="_configure_gdn_hybrid_model.get_state_dtype"></a>`get_state_dtype(cls, vllm_config)` — [`L237`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L237)
- <a id="_configure_gdn_hybrid_model.get_state_shape"></a>`get_state_shape(cls, vllm_config)` — [`L222`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L222)
- <a id="model_spec_to_hf_config_dict"></a>`model_spec_to_hf_config_dict(spec: ModelSpec)` — [`L114`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L114) — Build the HF-shaped config dict that vLLM's engine init reads.
- <a id="register_to_vllm"></a>`register_to_vllm(model_spec: ModelSpec, *, parallelism: InferenceParallelismConfig, compile_config: CompileConfig, checkpoint_config: CheckpointManager.Config, override: OverrideConfig)` — [`L260`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L260) — Register the TorchTitan model class and the TorchTitan config parser with vLLM.

## Module values
- <a id="TORCHTITAN_CONFIG_FORMAT"></a>`TORCHTITAN_CONFIG_FORMAT` — [`L43`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L43)
- <a id="TORCHTITAN_WORKER_CLS"></a>`TORCHTITAN_WORKER_CLS` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L46)
- <a id="VLLM_MODEL_NAME"></a>`VLLM_MODEL_NAME` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/experiments/rl/models/vllm_registry.py#L39)

