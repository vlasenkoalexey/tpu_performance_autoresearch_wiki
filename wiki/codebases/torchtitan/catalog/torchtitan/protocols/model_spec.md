---
title: 'Module: torchtitan/protocols/model_spec.py'
type: catalog
provenance: extracted
module: torchtitan/protocols/model_spec.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.protocols.model_spec`/
symbols:
  ModelSpec.model: ModelSpec#model.
  ModelSpec.max_context_length: ModelSpec#max_context_length.
  ModelSpec: ModelSpec#
  ModelSpec.parallelize_fn: ModelSpec#parallelize_fn.
  ModelSpec.name: ModelSpec#name.
  ModelSpec.flavor: ModelSpec#flavor.
  ModelSpec.state_dict_adapter: ModelSpec#state_dict_adapter.
  ModelSpec.pipelining_fn: ModelSpec#pipelining_fn.
  ModelSpec.post_optimizer_build_fn: ModelSpec#post_optimizer_build_fn.
  ModelSpec.traverse: ModelSpec#traverse().
  ParallelizeFunction.ParallelizeFunction: ParallelizeFunction.ParallelizeFunction.
  PipeliningFunction.PipeliningFunction: PipeliningFunction.PipeliningFunction.
  FragmentFunction.FragmentFunction: FragmentFunction.FragmentFunction.
  PostOptimizerBuildFn.PostOptimizerBuildFn: PostOptimizerBuildFn.PostOptimizerBuildFn.
---
# Module: [`torchtitan/protocols/model_spec.py`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py)

## Classes
### <a id="ModelSpec"></a>`ModelSpec`
- def: [`torchtitan/protocols/model_spec.py:33`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L33) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
- doc: Per-model bundle. Contains already-selected arch config + callables.
- signature: `class ModelSpec:`
- members:
  - <a id="ModelSpec.traverse"></a>`traverse(self, config_cls: type, *, recurse: bool = False, _prefix: str = "")` — [`L50`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L50) — Expose the nested model config to ``Configurable.Config.traverse``.
  - <a id="ModelSpec.flavor"></a>`flavor` — [`L37`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L37) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
  - <a id="ModelSpec.max_context_length"></a>`max_context_length` — [`L39`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L39) — documented in [llama3-model](../../../concepts/llama3-model.md)
  - <a id="ModelSpec.model"></a>`model` — [`L38`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L38) — documented in [llama3-model](../../../concepts/llama3-model.md)
  - <a id="ModelSpec.name"></a>`name` — [`L36`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L36) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
  - <a id="ModelSpec.parallelize_fn"></a>`parallelize_fn` — [`L45`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L45) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
  - <a id="ModelSpec.pipelining_fn"></a>`pipelining_fn` — [`L46`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L46) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
  - <a id="ModelSpec.post_optimizer_build_fn"></a>`post_optimizer_build_fn` — [`L47`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L47) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
  - <a id="ModelSpec.state_dict_adapter"></a>`state_dict_adapter` — [`L48`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L48) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
- uses (calls/refs, reference-scoped): [`Configurable`](../config/configurable.md#Configurable), [`Config`](../config/configurable.md#Configurable.Config), [`BaseModel`](model.md#BaseModel), [`traverse`](../config/configurable.md#Configurable.Config.traverse), [`Config`](model.md#BaseModel.Config), [`BaseStateDictAdapter`](state_dict_adapter.md#BaseStateDictAdapter), [`FaultTolerantModelSpec`](../experiments/torchft/config/job_config.md#FaultTolerantModelSpec)
- used by: [`model_spec`](../trainer.md#Trainer.Config.model_spec), [`sft_llama3_8b_metamath`](../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`reg_trainer_qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`start_trainer`](../experiments/tpu/conformer/train_minimal.md#start_trainer), [`qwen3_1_7b`](../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](../models/llama3/config_registry.md#llama3_debugmodel), [`_qwen3_moe_30b_fsdp_only_full_ac`](../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`llama3_torchft_debugmodel`](../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`__init__`](../experiments/torchft/trainer.md#FaultTolerantTrainer.__init__), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`pp_schedule`](../experiments/torchft/trainer.md#FaultTolerantTrainer.pp_schedule), [`qwen3_moe_30b`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b), [`_tpu_hf_config`](../experiments/tpu/transformers_modeling_backend/config_registry.md#_tpu_hf_config), [`_collect_moe_routing_metrics`](../trainer.md#Trainer._collect_moe_routing_metrics), [`sft_debugmodel`](../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`qwen35_debugmodel_moe`](../models/qwen3_5/config_registry.md#qwen35_debugmodel_moe), [`deepseek_v4_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`qwen38_debugmodel_moe`](../models/qwen3_8/config_registry.md#qwen38_debugmodel_moe), [`deepseek_v3_debugmodel`](../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`transfer_stream`](../trainer.md#Trainer.transfer_stream), [`deepseek_v4_flash`](../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`qwen36_debugmodel_moe`](../models/qwen3_6/config_registry.md#qwen36_debugmodel_moe), [`_gpt_oss_debugmodel`](../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`deepseek_v4_mtp_debugmodel`](../models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`kimi_k2_5_debugmodel`](../models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel), [`muse_glimmer_debugmodel`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`qwen3_debugmodel`](../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel), [`qwen35_debugmodel`](../models/qwen3_5/config_registry.md#qwen35_debugmodel), [`qwen38_debugmodel`](../models/qwen3_8/config_registry.md#qwen38_debugmodel), [`kimi_k2_5`](../models/kimi_k2_7/config_registry.md#kimi_k2_5), [`llama3_70b`](../models/llama3/config_registry.md#llama3_70b), [`muse_glimmer_debugmodel_mm`](../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel_mm), [`qwen36_debugmodel`](../models/qwen3_6/config_registry.md#qwen36_debugmodel), [`deepseek_v3_671b`](../models/deepseek_v3/config_registry.md#deepseek_v3_671b), [`qwen3_debugmodel`](../models/qwen3/config_registry.md#qwen3_debugmodel)  (+120 more; 64 test-only)

## Module values
- <a id="FragmentFunction.FragmentFunction"></a>`FragmentFunction` — [`L27`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L27)
- <a id="ParallelizeFunction.ParallelizeFunction"></a>`ParallelizeFunction` — [`L23`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L23)
- <a id="PipeliningFunction.PipeliningFunction"></a>`PipeliningFunction` — [`L24`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L24)
- <a id="PostOptimizerBuildFn.PostOptimizerBuildFn"></a>`PostOptimizerBuildFn` — [`L28`](../../../../../../raw/code/torchtitan/torchtitan/protocols/model_spec.py#L28)

