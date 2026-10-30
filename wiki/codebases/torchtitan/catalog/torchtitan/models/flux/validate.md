---
title: 'Module: torchtitan/models/flux/validate.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/validate.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.validate`/FluxValidator#
symbols:
  FluxValidator.validate: validate().
  FluxValidator.__init__: __init__().
  FluxValidator.all_timesteps: all_timesteps.
  FluxValidator.dl_config: dl_config.
  FluxValidator.Config: Config#
  FluxValidator.Config.dataloader: Config#dataloader.
  FluxValidator.Config.sampling: Config#sampling.
  FluxValidator.config: config.
  FluxValidator: ''
  FluxValidator.metrics_processor: metrics_processor.
  FluxValidator.Config.all_timesteps: Config#all_timesteps.
  FluxValidator.flux_init: flux_init().
  FluxValidator.device: device.
  FluxValidator.Config.save_img_count: Config#save_img_count.
  FluxValidator.Config.save_img_folder: Config#save_img_folder.
  FluxValidator.tokenizer: tokenizer.
  FluxValidator._dtype: _dtype.
  FluxValidator.autoencoder: autoencoder.
  FluxValidator.t5_encoder: t5_encoder.
  FluxValidator.clip_encoder: clip_encoder.
  FluxValidator.parallel_dims: parallel_dims.
  FluxValidator.loss_fn: loss_fn.
  FluxValidator.dp_world_size: dp_world_size.
  FluxValidator.dp_rank: dp_rank.
  FluxValidator.seq_len: seq_len.
  FluxValidator.num_tokens_per_batch: num_tokens_per_batch.
  FluxValidator.validation_context: validation_context.
  FluxValidator.dump_folder: dump_folder.
  FluxValidator.parallelism: parallelism.
---
# Module: [`torchtitan/models/flux/validate.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py)

## Classes
### <a id="FluxValidator"></a>`FluxValidator`  ·  implements/extends Validator
- def: [`torchtitan/models/flux/validate.py:36`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L36)
- doc: Flux model validator focused on correctness and integration.
- signature: `class FluxValidator(Validator):`
- members:
  - <a id="FluxValidator.flux_init"></a>`flux_init(self, device: torch.device, _dtype: torch.dtype, autoencoder: AutoEncoder, t5_encoder: FluxEmbedder, clip_encoder: FluxEmbedder, dump_folder: str)` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L124)
  - <a id="FluxValidator.validate"></a>`validate(self, model_parts: list[nn.Module], step: int)` — [`L142`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L142) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
  - <a id="FluxValidator.all_timesteps"></a>`all_timesteps` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L93) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
  - <a id="FluxValidator.autoencoder"></a>`autoencoder` — [`L136`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L136)
  - <a id="FluxValidator.clip_encoder"></a>`clip_encoder` — [`L138`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L138)
  - <a id="FluxValidator.config"></a>`config` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L88)
  - <a id="FluxValidator.device"></a>`device` — [`L134`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L134)
  - <a id="FluxValidator.dl_config"></a>`dl_config` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L101) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
  - <a id="FluxValidator.dp_rank"></a>`dp_rank` — [`L111`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L111)
  - <a id="FluxValidator.dp_world_size"></a>`dp_world_size` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L110)
  - <a id="FluxValidator.dump_folder"></a>`dump_folder` — [`L139`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L139)
  - <a id="FluxValidator.loss_fn"></a>`loss_fn` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L92)
  - <a id="FluxValidator.metrics_processor"></a>`metrics_processor` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L116)
  - <a id="FluxValidator.num_tokens_per_batch"></a>`num_tokens_per_batch` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L113)
  - <a id="FluxValidator.parallel_dims"></a>`parallel_dims` — [`L91`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L91)
  - <a id="FluxValidator.parallelism"></a>`parallelism` — [`L89`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L89)
  - <a id="FluxValidator.seq_len"></a>`seq_len` — [`L112`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L112)
  - <a id="FluxValidator.t5_encoder"></a>`t5_encoder` — [`L137`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L137)
  - <a id="FluxValidator.tokenizer"></a>`tokenizer` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L90)
  - <a id="FluxValidator.validation_context"></a>`validation_context` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L114)
- protocol/private: <a id="FluxValidator.__init__"></a>`__init__`[`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L69), <a id="FluxValidator._dtype"></a>`_dtype`[`L135`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L135)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`ParallelismConfig`](../../config/configs.md#ParallelismConfig), [`ParallelDims`](../../distributed/parallel_dims.md#ParallelDims), [`build`](../../config/configurable.md#Configurable.Config.build), [`MetricsProcessor`](../../components/metrics.md#MetricsProcessor), [`dataset`](../../components/data/loader.md#GrainDataLoader.Config.dataset), [`get_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_mesh), [`get_optional_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_optional_mesh), [`device_type`](../../tools/utils.md#device_type), [`log_validation`](../../components/metrics.md#MetricsProcessor.log_validation), [`Validator`](../../components/validate.md#Validator), [`cp_enabled`](../../distributed/parallel_dims.md#ParallelDims.cp_enabled), [`BaseTokenizer`](../../components/tokenizer.md#BaseTokenizer), [`steps`](../../components/validate.md#Validator.Config.steps), [`FluxEmbedder`](model/hf_embedder.md#FluxEmbedder), [`generate_image`](inference/sampling.md#generate_image), [`AutoEncoder`](model/autoencoder.md#AutoEncoder), [`dp_enabled`](../../distributed/parallel_dims.md#ParallelDims.dp_enabled), [`FluxTokenizerContainer`](tokenizer.md#FluxTokenizerContainer), [`preprocess_data`](utils.md#preprocess_data), [`LossFunction`](../../components/loss.md#LossFunction.LossFunction), [`pack_latents`](utils.md#pack_latents), [`dist_sum`](../../distributed/utils.md#dist_sum), [`dp_cp_enabled`](../../distributed/parallel_dims.md#ParallelDims.dp_cp_enabled), [`create_position_encoding_for_latents`](utils.md#create_position_encoding_for_latents), [`cp_shard`](../../distributed/context_parallel/api.md#cp_shard), [`iterate_and_close_dataloader`](../../components/validate.md#iterate_and_close_dataloader), [`Config`](validate.md#FluxValidator.Config), [`dataloader`](validate.md#FluxValidator.Config.dataloader), [`dist_sum_tensor`](../../distributed/utils.md#dist_sum_tensor), [`ntokens_since_last_log`](../../components/metrics.md#MetricsProcessor.ntokens_since_last_log), [`dataset`](flux_datasets.md#FluxValidationDatasetConfig.dataset), [`sampling`](validate.md#FluxValidator.Config.sampling), [`FluxValidationDatasetConfig`](flux_datasets.md#FluxValidationDatasetConfig), [`save_image`](inference/sampling.md#save_image), [`all_timesteps`](validate.md#FluxValidator.Config.all_timesteps), [`classifier_free_guidance_scale`](configs.md#SamplingConfig.classifier_free_guidance_scale), [`denoising_steps`](configs.md#SamplingConfig.denoising_steps), [`enable_classifier_free_guidance`](configs.md#SamplingConfig.enable_classifier_free_guidance), [`save_img_count`](validate.md#FluxValidator.Config.save_img_count)  (+2 more)
- used by: [`flux_debugmodel`](config_registry.md#flux_debugmodel), [`flux_dev`](config_registry.md#flux_dev), [`flux_schnell`](config_registry.md#flux_schnell), [`validate`](../../components/validate.md#Validator.validate), [`Validator`](../../components/validate.md#Validator)

### <a id="FluxValidator.Config"></a>`FluxValidator.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/validate.py:53`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L53)
- signature: `class Config(Validator.Config):`
- members:
  - <a id="FluxValidator.Config.all_timesteps"></a>`all_timesteps` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L57) — ---
  - <a id="FluxValidator.Config.dataloader"></a>`dataloader` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L54) — ---
  - <a id="FluxValidator.Config.sampling"></a>`sampling` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L66) — ---
  - <a id="FluxValidator.Config.save_img_count"></a>`save_img_count` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L60) — ---
  - <a id="FluxValidator.Config.save_img_folder"></a>`save_img_folder` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/validate.py#L63) — ---
- uses (calls/refs, reference-scoped): [`GrainDataLoader`](../../components/data/loader.md#GrainDataLoader), [`Config`](../../components/data/loader.md#GrainDataLoader.Config), [`Validator`](../../components/validate.md#Validator), [`Config`](../../components/validate.md#Validator.Config), [`SamplingConfig`](configs.md#SamplingConfig)
- used by: [`flux_debugmodel`](config_registry.md#flux_debugmodel), [`flux_dev`](config_registry.md#flux_dev), [`flux_schnell`](config_registry.md#flux_schnell), [`validate`](validate.md#FluxValidator.validate), [`__init__`](validate.md#FluxValidator.__init__), [`all_timesteps`](validate.md#FluxValidator.all_timesteps), [`dl_config`](validate.md#FluxValidator.dl_config)

