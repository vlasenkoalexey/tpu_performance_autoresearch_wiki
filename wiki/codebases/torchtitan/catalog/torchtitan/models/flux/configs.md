---
title: 'Module: torchtitan/models/flux/configs.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/configs.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.configs`/
symbols:
  SamplingConfig: SamplingConfig#
  Inference: Inference#
  FluxEncoderConfig: FluxEncoderConfig#
  SamplingConfig.enable_classifier_free_guidance: SamplingConfig#enable_classifier_free_guidance.
  SamplingConfig.classifier_free_guidance_scale: SamplingConfig#classifier_free_guidance_scale.
  SamplingConfig.denoising_steps: SamplingConfig#denoising_steps.
  FluxEncoderConfig.autoencoder_path: FluxEncoderConfig#autoencoder_path.
  FluxEncoderConfig.random_init: FluxEncoderConfig#random_init.
  Inference.sampling: Inference#sampling.
  FluxEncoderConfig.t5_encoder: FluxEncoderConfig#t5_encoder.
  FluxEncoderConfig.clip_encoder: FluxEncoderConfig#clip_encoder.
  Inference.save_img_folder: Inference#save_img_folder.
  Inference.prompts_path: Inference#prompts_path.
  Inference.local_batch_size: Inference#local_batch_size.
  Inference.img_size: Inference#img_size.
---
# Module: [`torchtitan/models/flux/configs.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py)

## Classes
### <a id="FluxEncoderConfig"></a>`FluxEncoderConfig`
- def: [`torchtitan/models/flux/configs.py:11`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L11)
- doc: Configuration for Flux encoders (T5 text encoder, CLIP text encoder, and autoencoder).
- signature: `class FluxEncoderConfig:`
- members:
  - <a id="FluxEncoderConfig.autoencoder_path"></a>`autoencoder_path` — [`L18`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L18) — ---
  - <a id="FluxEncoderConfig.clip_encoder"></a>`clip_encoder` — [`L16`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L16) — ---
  - <a id="FluxEncoderConfig.random_init"></a>`random_init` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L22) — ---
  - <a id="FluxEncoderConfig.t5_encoder"></a>`t5_encoder` — [`L14`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L14) — ---
- used by: [`flux_debugmodel`](config_registry.md#flux_debugmodel), [`flux_dev`](config_registry.md#flux_dev), [`flux_schnell`](config_registry.md#flux_schnell), [`t5_encoder`](trainer.md#FluxTrainer.t5_encoder), [`flux_testmodel`](../../experiments/tpu/flux/config_registry.md#flux_testmodel), [`encoder`](trainer.md#FluxTrainer.Config.encoder)

### <a id="Inference"></a>`Inference`
- def: [`torchtitan/models/flux/configs.py:54`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L54)
- doc: Inference configuration
- signature: `class Inference:`
- members:
  - <a id="Inference.img_size"></a>`img_size` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L63) — ---
  - <a id="Inference.local_batch_size"></a>`local_batch_size` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L61) — ---
  - <a id="Inference.prompts_path"></a>`prompts_path` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L59) — ---
  - <a id="Inference.sampling"></a>`sampling` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L65) — ---
  - <a id="Inference.save_img_folder"></a>`save_img_folder` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L57) — ---
- uses (calls/refs, reference-scoped): [`SamplingConfig`](configs.md#SamplingConfig)
- used by: [`flux_debugmodel`](config_registry.md#flux_debugmodel), [`inference`](inference/infer.md#inference), [`inference`](trainer.md#FluxTrainer.Config.inference)

### <a id="SamplingConfig"></a>`SamplingConfig`
- def: [`torchtitan/models/flux/configs.py:27`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L27)
- doc: Shared configuration for image generation sampling (used by both validation and inference).
- signature: `class SamplingConfig:`
- members:
  - <a id="SamplingConfig.classifier_free_guidance_scale"></a>`classifier_free_guidance_scale` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L40) — ---
  - <a id="SamplingConfig.denoising_steps"></a>`denoising_steps` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L49) — ---
  - <a id="SamplingConfig.enable_classifier_free_guidance"></a>`enable_classifier_free_guidance` — [`L30`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/configs.py#L30) — ---
- used by: [`flux_debugmodel`](config_registry.md#flux_debugmodel), [`flux_dev`](config_registry.md#flux_dev), [`flux_schnell`](config_registry.md#flux_schnell), [`validate`](validate.md#FluxValidator.validate), [`inference`](inference/infer.md#inference), [`sampling`](validate.md#FluxValidator.Config.sampling), [`Inference`](configs.md#Inference)

