---
title: 'Module: torchtitan/components/validate.py'
type: catalog
provenance: extracted
module: torchtitan/components/validate.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.validate`/
symbols:
  Validator.validate: Validator#validate().
  Validator: Validator#
  Validator.Config: Validator#Config#
  Validator.Config.dataloader: Validator#Config#dataloader.
  Validator.Config.steps: Validator#Config#steps.
  BaseValidator.Config.freq: BaseValidator#Config#freq.
  Validator.Config.enable: Validator#Config#enable.
  Validator.__init__: Validator#__init__().
  iterate_and_close_dataloader: iterate_and_close_dataloader().
  BaseValidator: BaseValidator#
  Validator.Config.__post_init__: Validator#Config#__post_init__().
  BaseValidator.Config: BaseValidator#Config#
  BaseValidator.should_validate: BaseValidator#should_validate().
  Validator.pp_has_last_stage: Validator#pp_has_last_stage.
  Validator.dl_config: Validator#dl_config.
  BaseValidator.validate: BaseValidator#validate().
  BaseValidator.Config.__post_init__: BaseValidator#Config#__post_init__().
  BaseValidator.__init__: BaseValidator#__init__().
  BaseValidator.config: BaseValidator#config.
  Validator.parallelism: Validator#parallelism.
  Validator.parallel_dims: Validator#parallel_dims.
  Validator.pp_has_first_stage: Validator#pp_has_first_stage.
  ValidationContext.ValidationContext: ValidationContext.ValidationContext.
  Validator.validation_context: Validator#validation_context.
  Validator.metrics_processor: Validator#metrics_processor.
  Validator.pp_schedule: Validator#pp_schedule.
  Validator.tokenizer: Validator#tokenizer.
  Validator.loss_fn: Validator#loss_fn.
  Validator.dp_world_size: Validator#dp_world_size.
  Validator.dp_rank: Validator#dp_rank.
  Validator.seq_len: Validator#seq_len.
  Validator.num_tokens_per_batch: Validator#num_tokens_per_batch.
---
# Module: [`torchtitan/components/validate.py`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py)

## Classes
### <a id="BaseValidator"></a>`BaseValidator`  ·  implements/extends Configurable
- def: [`torchtitan/components/validate.py:31`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L31)
- signature: `class BaseValidator(Configurable):`
- members:
  - <a id="BaseValidator.should_validate"></a>`should_validate(self, step: int)` — [`L53`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L53)
  - <a id="BaseValidator.validate"></a>`validate(self, model_parts: list[nn.Module], step: int)` — [`L50`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L50)
  - <a id="BaseValidator.config"></a>`config` — [`L48`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L48)
- protocol/private: <a id="BaseValidator.__init__"></a>`__init__`[`L43`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L43)
- uses (calls/refs, reference-scoped): [`Configurable`](../config/configurable.md#Configurable), [`validate`](validate.md#Validator.validate), [`Validator`](validate.md#Validator), [`freq`](validate.md#BaseValidator.Config.freq), [`Config`](validate.md#BaseValidator.Config)
- used by: [`Configurable`](../config/configurable.md#Configurable), [`train`](../experiments/torchft/trainer.md#FaultTolerantTrainer.train), [`train`](../trainer.md#Trainer.train), [`validate`](validate.md#Validator.validate), [`Validator`](validate.md#Validator), [`Config`](validate.md#Validator.Config), [`__init__`](validate.md#Validator.__init__), [`__post_init__`](validate.md#Validator.Config.__post_init__), [`validator`](../trainer.md#Trainer.validator)

### <a id="BaseValidator.Config"></a>`BaseValidator.Config`  ·  implements/extends Config
- def: [`torchtitan/components/validate.py:33`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L33)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="BaseValidator.Config.freq"></a>`freq` — [`L34`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L34) — ---
- protocol/private: <a id="BaseValidator.Config.__post_init__"></a>`__post_init__`[`L37`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L37)
- uses (calls/refs, reference-scoped): [`Configurable`](../config/configurable.md#Configurable), [`Config`](../config/configurable.md#Configurable.Config)
- used by: [`qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#qwen3_8b), [`flux_debugmodel`](../models/flux/config_registry.md#flux_debugmodel), [`reg_trainer_qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`qwen3_1_7b`](../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](../models/llama3/config_registry.md#llama3_debugmodel), [`llama3_torchft_debugmodel`](../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`flux_dev`](../models/flux/config_registry.md#flux_dev), [`flux_schnell`](../models/flux/config_registry.md#flux_schnell), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`_gpt_oss_debugmodel`](../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`qwen3_debugmodel`](../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel), [`llama3_70b`](../models/llama3/config_registry.md#llama3_70b), [`llama3_8b`](../models/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](../experiments/tpu/llama3/config_registry.md#llama3_debugmodel), [`llama3_1b`](../experiments/tpu/llama3/config_registry.md#llama3_1b), [`Config`](validate.md#Validator.Config), [`__post_init__`](validate.md#Validator.Config.__post_init__), [`should_validate`](validate.md#BaseValidator.should_validate), [`__init__`](validate.md#BaseValidator.__init__)  (2 test-only)

### <a id="Validator"></a>`Validator`  ·  implements/extends BaseValidator
- def: [`torchtitan/components/validate.py:57`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L57) — documented in [training-components](../../../concepts/training-components.md)
- doc: Simple validator focused on correctness and integration.
- signature: `class Validator(BaseValidator):`
- members:
  - <a id="Validator.validate"></a>`validate(self, model_parts: list[nn.Module], step: int)` — [`L142`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L142) — documented in [training-components](../../../concepts/training-components.md)
  - <a id="Validator.dl_config"></a>`dl_config` — [`L129`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L129)
  - <a id="Validator.dp_rank"></a>`dp_rank` — [`L131`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L131)
  - <a id="Validator.dp_world_size"></a>`dp_world_size` — [`L130`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L130)
  - <a id="Validator.loss_fn"></a>`loss_fn` — [`L127`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L127)
  - <a id="Validator.metrics_processor"></a>`metrics_processor` — [`L135`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L135)
  - <a id="Validator.num_tokens_per_batch"></a>`num_tokens_per_batch` — [`L133`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L133)
  - <a id="Validator.parallel_dims"></a>`parallel_dims` — [`L126`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L126)
  - <a id="Validator.parallelism"></a>`parallelism` — [`L124`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L124)
  - <a id="Validator.pp_has_first_stage"></a>`pp_has_first_stage` — [`L137`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L137)
  - <a id="Validator.pp_has_last_stage"></a>`pp_has_last_stage` — [`L138`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L138)
  - <a id="Validator.pp_schedule"></a>`pp_schedule` — [`L136`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L136)
  - <a id="Validator.seq_len"></a>`seq_len` — [`L132`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L132)
  - <a id="Validator.tokenizer"></a>`tokenizer` — [`L125`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L125)
  - <a id="Validator.validation_context"></a>`validation_context` — [`L134`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L134)
- protocol/private: <a id="Validator.__init__"></a>`__init__`[`L104`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L104)
- uses (calls/refs, reference-scoped): [`ParallelismConfig`](../config/configs.md#ParallelismConfig), [`ParallelDims`](../distributed/parallel_dims.md#ParallelDims), [`build`](../config/configurable.md#Configurable.Config.build), [`validate`](../models/flux/validate.md#FluxValidator.validate), [`MetricsProcessor`](metrics.md#MetricsProcessor), [`BaseModel`](../protocols/model.md#BaseModel), [`log_trace_span`](../observability/structured_logger/structured_logging.md#log_trace_span), [`get_mesh`](../distributed/parallel_dims.md#ParallelDims.get_mesh), [`get_optional_mesh`](../distributed/parallel_dims.md#ParallelDims.get_optional_mesh), [`device_type`](../tools/utils.md#device_type), [`pp_enabled`](../distributed/parallel_dims.md#ParallelDims.pp_enabled), [`log_validation`](metrics.md#MetricsProcessor.log_validation), [`Config`](validate.md#Validator.Config), [`num_pp_microbatches`](../config/configs.md#ParallelismConfig.num_pp_microbatches), [`dataloader`](validate.md#Validator.Config.dataloader), [`BaseTokenizer`](tokenizer.md#BaseTokenizer), [`steps`](validate.md#Validator.Config.steps), [`dp_enabled`](../distributed/parallel_dims.md#ParallelDims.dp_enabled), [`preprocess_inputs`](../protocols/model.md#BaseModel.preprocess_inputs), [`LossFunction`](loss.md#LossFunction.LossFunction), [`add_step_tag`](../observability/structured_logger/step_state.md#add_step_tag), [`dist_sum`](../distributed/utils.md#dist_sum), [`dp_cp_enabled`](../distributed/parallel_dims.md#ParallelDims.dp_cp_enabled), [`iterate_and_close_dataloader`](validate.md#iterate_and_close_dataloader), [`BaseValidator`](validate.md#BaseValidator), [`dist_sum_tensor`](../distributed/utils.md#dist_sum_tensor), [`ntokens_since_last_log`](metrics.md#MetricsProcessor.ntokens_since_last_log), [`FluxValidator`](../models/flux/validate.md#FluxValidator), [`__init__`](validate.md#BaseValidator.__init__), [`ValidationContext`](validate.md#ValidationContext.ValidationContext), [`config`](validate.md#BaseValidator.config)
- used by: [`qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#qwen3_8b), [`reg_trainer_qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`qwen3_1_7b`](../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](../models/llama3/config_registry.md#llama3_debugmodel), [`_qwen3_moe_30b_fsdp_only_full_ac`](../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`llama3_torchft_debugmodel`](../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`_muse_glimmer_30b_base`](../experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`qwen3_moe_30b`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b), [`qwen35_moe_35b`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_moe_35b), [`_gpt_oss_debugmodel`](../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`qwen3_debugmodel`](../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel), [`llama3_70b`](../models/llama3/config_registry.md#llama3_70b), [`conformer_test`](../experiments/tpu/conformer/config_registry.md#conformer_test), [`llama3_8b`](../models/llama3/config_registry.md#llama3_8b), [`qwen35_debugmodel`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_debugmodel), [`llama3_debugmodel`](../experiments/tpu/llama3/config_registry.md#llama3_debugmodel), [`llama3_1b`](../experiments/tpu/llama3/config_registry.md#llama3_1b), [`validator`](../trainer.md#Trainer.Config.validator), [`BaseValidator`](validate.md#BaseValidator), [`Config`](../models/flux/validate.md#FluxValidator.Config), [`FluxValidator`](../models/flux/validate.md#FluxValidator), [`validate`](validate.md#BaseValidator.validate)  (2 test-only)

### <a id="Validator.Config"></a>`Validator.Config`  ·  implements/extends Config
- def: [`torchtitan/components/validate.py:77`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L77)
- signature: `class Config(BaseValidator.Config):`
- members:
  - <a id="Validator.Config.dataloader"></a>`dataloader` — [`L87`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L87) — --- — documented in [training-components](../../../concepts/training-components.md)
  - <a id="Validator.Config.enable"></a>`enable` — [`L78`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L78) — ---
  - <a id="Validator.Config.steps"></a>`steps` — [`L81`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L81) — ---
- protocol/private: <a id="Validator.Config.__post_init__"></a>`__post_init__`[`L97`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L97)
- uses (calls/refs, reference-scoped): [`GrainDataLoader`](data/loader.md#GrainDataLoader), [`DATASETS`](../hf_datasets/text_datasets.md#DATASETS.DATASETS), [`Config`](data/loader.md#GrainDataLoader.Config), [`dataset`](data/loader.md#GrainDataLoader.Config.dataset), [`ConcatThenSplitPackingConfig`](data/packing.md#ConcatThenSplitPackingConfig), [`dataset`](data/packing.md#ConcatThenSplitPackingConfig.dataset), [`BaseDataLoader`](data/loader.md#BaseDataLoader), [`BaseValidator`](validate.md#BaseValidator), [`Config`](data/loader.md#BaseDataLoader.Config), [`Config`](validate.md#BaseValidator.Config), [`repeat`](data/loader.md#GrainDataLoader.Config.repeat), [`__post_init__`](validate.md#BaseValidator.Config.__post_init__)
- used by: [`qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#qwen3_8b), [`flux_debugmodel`](../models/flux/config_registry.md#flux_debugmodel), [`reg_trainer_qwen3_8b`](../experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b), [`qwen3_1_7b`](../experiments/tpu/qwen3/config_registry.md#qwen3_1_7b), [`llama3_70b`](../experiments/tpu/llama3/config_registry.md#llama3_70b), [`llama3_405b`](../experiments/tpu/llama3/config_registry.md#llama3_405b), [`llama3_8b`](../experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_debugmodel`](../models/llama3/config_registry.md#llama3_debugmodel), [`_qwen3_moe_30b_fsdp_only_full_ac`](../experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac), [`llama3_torchft_debugmodel`](../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`_muse_glimmer_30b_base`](../experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base), [`flux_dev`](../models/flux/config_registry.md#flux_dev), [`flux_schnell`](../models/flux/config_registry.md#flux_schnell), [`llama3_405b`](../models/llama3/config_registry.md#llama3_405b), [`pp_schedule`](../experiments/torchft/trainer.md#FaultTolerantTrainer.pp_schedule), [`qwen3_moe_30b`](../experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b), [`_collect_moe_routing_metrics`](../trainer.md#Trainer._collect_moe_routing_metrics), [`qwen35_moe_35b`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_moe_35b), [`_gpt_oss_debugmodel`](../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`qwen3_debugmodel`](../experiments/tpu/qwen3/config_registry.md#qwen3_debugmodel), [`llama3_70b`](../models/llama3/config_registry.md#llama3_70b), [`conformer_test`](../experiments/tpu/conformer/config_registry.md#conformer_test), [`llama3_8b`](../models/llama3/config_registry.md#llama3_8b), [`qwen35_debugmodel`](../experiments/tpu/qwen3_5/config_registry.md#qwen35_debugmodel), [`llama3_debugmodel`](../experiments/tpu/llama3/config_registry.md#llama3_debugmodel), [`llama3_1b`](../experiments/tpu/llama3/config_registry.md#llama3_1b), [`validate`](../models/flux/validate.md#FluxValidator.validate), [`t5_encoder`](../models/flux/trainer.md#FluxTrainer.t5_encoder), [`train`](../experiments/torchft/trainer.md#FaultTolerantTrainer.train), [`train`](../trainer.md#Trainer.train), [`_validate_cuda_graphs`](../trainer.md#Trainer.Config._validate_cuda_graphs), [`flux_testmodel`](../experiments/tpu/flux/config_registry.md#flux_testmodel), [`validator`](../trainer.md#Trainer.Config.validator), [`__init__`](validate.md#Validator.__init__), [`dl_config`](../models/flux/validate.md#FluxValidator.dl_config), [`Config`](../models/flux/validate.md#FluxValidator.Config), [`metrics_processor`](../models/flux/validate.md#FluxValidator.metrics_processor), [`dl_config`](validate.md#Validator.dl_config)  (3 test-only)

## Functions
- <a id="iterate_and_close_dataloader"></a>`iterate_and_close_dataloader(dataloader: BaseDataLoader)` — [`L288`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L288) — Close a temporary dataloader when its consumer stops iterating.

## Module values
- <a id="ValidationContext.ValidationContext"></a>`ValidationContext` — [`L28`](../../../../../../raw/code/torchtitan/torchtitan/components/validate.py#L28)

