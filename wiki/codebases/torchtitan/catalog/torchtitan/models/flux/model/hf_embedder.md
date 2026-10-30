---
title: 'Module: torchtitan/models/flux/model/hf_embedder.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/model/hf_embedder.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.model.hf_embedder`/FluxEmbedder#
symbols:
  FluxEmbedder: ''
  FluxEmbedder.hf_module: hf_module.
  FluxEmbedder.Config: Config#
  FluxEmbedder.Config.version: Config#version.
  FluxEmbedder.output_key: output_key.
  FluxEmbedder.forward: forward().
  FluxEmbedder.is_clip: is_clip.
  FluxEmbedder.init_weights: init_weights().
  FluxEmbedder.Config.hf_kwargs: Config#hf_kwargs.
  FluxEmbedder.make_parameters_contiguous: make_parameters_contiguous().
  FluxEmbedder.__init__: __init__().
  FluxEmbedder.Config.random_init: Config#random_init.
---
# Module: [`torchtitan/models/flux/model/hf_embedder.py`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py)

## Classes
### <a id="FluxEmbedder"></a>`FluxEmbedder`  ·  implements/extends Module
- def: [`torchtitan/models/flux/model/hf_embedder.py:18`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py#L18) — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
- signature: `class FluxEmbedder(Module):`
- members:
  - <a id="FluxEmbedder.forward"></a>`forward(self, batch_tokens: Tensor)` — [`L77`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py#L77) — batch_tokens: [bsz, embedding_length]
  - <a id="FluxEmbedder.init_weights"></a>`init_weights(self)` — [`L66`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py#L66)
  - <a id="FluxEmbedder.make_parameters_contiguous"></a>`make_parameters_contiguous(self)` — [`L60`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py#L60) — Make all non-contiguous parameters contiguous to avoid FSDP issues.
  - <a id="FluxEmbedder.hf_module"></a>`hf_module` — [`L39`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py#L39) — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
  - <a id="FluxEmbedder.is_clip"></a>`is_clip` — [`L27`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py#L27)
  - <a id="FluxEmbedder.output_key"></a>`output_key` — [`L28`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py#L28)
- protocol/private: <a id="FluxEmbedder.__init__"></a>`__init__`[`L25`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py#L25)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](hf_embedder.md#FluxEmbedder.Config), [`version`](hf_embedder.md#FluxEmbedder.Config.version), [`hf_kwargs`](hf_embedder.md#FluxEmbedder.Config.hf_kwargs), [`random_init`](hf_embedder.md#FluxEmbedder.Config.random_init)
- used by: [`Module`](../../../protocols/module.md#Module), [`_flux_debug`](../__init__.md#_flux_debug), [`_flux_dev`](../__init__.md#_flux_dev), [`_flux_schnell`](../__init__.md#_flux_schnell), [`_flux_test`](../__init__.md#_flux_test), [`t5_encoder`](../trainer.md#FluxTrainer.t5_encoder), [`parallelize_encoders`](../parallelize.md#parallelize_encoders), [`generate_image`](../inference/sampling.md#generate_image), [`preprocess_data`](../utils.md#preprocess_data), [`clip_encoder`](model.md#FluxModel.Config.clip_encoder), [`t5_encoder`](model.md#FluxModel.Config.t5_encoder), [`flux_init`](../validate.md#FluxValidator.flux_init)

### <a id="FluxEmbedder.Config"></a>`FluxEmbedder.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/model/hf_embedder.py:20`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py#L20)
- signature: `class Config(Module.Config):`
- members:
  - <a id="FluxEmbedder.Config.hf_kwargs"></a>`hf_kwargs` — [`L23`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py#L23)
  - <a id="FluxEmbedder.Config.random_init"></a>`random_init` — [`L22`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py#L22)
  - <a id="FluxEmbedder.Config.version"></a>`version` — [`L21`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/model/hf_embedder.py#L21)
- uses (calls/refs, reference-scoped): [`Module`](../../../protocols/module.md#Module), [`Config`](../../../protocols/module.md#Module.Config)
- used by: [`_flux_debug`](../__init__.md#_flux_debug), [`_flux_dev`](../__init__.md#_flux_dev), [`_flux_schnell`](../__init__.md#_flux_schnell), [`_flux_test`](../__init__.md#_flux_test), [`t5_encoder`](../trainer.md#FluxTrainer.t5_encoder), [`hf_module`](hf_embedder.md#FluxEmbedder.hf_module), [`output_key`](hf_embedder.md#FluxEmbedder.output_key), [`clip_encoder`](model.md#FluxModel.Config.clip_encoder), [`t5_encoder`](model.md#FluxModel.Config.t5_encoder), [`is_clip`](hf_embedder.md#FluxEmbedder.is_clip), [`__init__`](hf_embedder.md#FluxEmbedder.__init__)

