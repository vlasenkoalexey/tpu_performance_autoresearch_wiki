---
title: 'Module: torchtitan/models/flux/inference/sampling.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/inference/sampling.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.inference.sampling`/
symbols:
  generate_image: generate_image().
  denoise: denoise().
  save_image: save_image().
  get_schedule: get_schedule().
  time_shift: time_shift().
  get_lin_function: get_lin_function().
---
# Module: [`torchtitan/models/flux/inference/sampling.py`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/inference/sampling.py)

## Functions
- <a id="denoise"></a>`denoise(device: torch.device, dtype: torch.dtype, model: FluxModel, img_width: int, img_height: int, denoising_steps: int, clip_encodings: torch.Tensor, t5_encodings: torch.Tensor, enable_classifier_free_guidance: bool = False, empty_t5_encodings: torch.Tensor | None = None, empty_clip_encodings: torch.Tensor | None = None, classifier_free_guidance_scale: float | None = None)` — [`L157`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/inference/sampling.py#L157) — Sampling images from noise using a given prompt, by running inference with trained Flux model. — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
- <a id="generate_image"></a>`generate_image(device: torch.device, dtype: torch.dtype, img_height: int, img_width: int, enable_classifier_free_guidance: bool, denoising_steps: int, classifier_free_guidance_scale: float, model: FluxModel, prompt: str | list[str], autoencoder: AutoEncoder, tokenizer: FluxTokenizerContainer, t5_encoder: FluxEmbedder, clip_encoder: FluxEmbedder)` — [`L70`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/inference/sampling.py#L70) — Sampling and save a single images from noise using a given prompt. — documented in [flux-diffusion-model](../../../../../concepts/flux-diffusion-model.md)
- <a id="get_lin_function"></a>`get_lin_function(x1: float = 256, y1: float = 0.5, x2: float = 4096, y2: float = 1.15)` — [`L38`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/inference/sampling.py#L38)
- <a id="get_schedule"></a>`get_schedule(num_steps: int, image_seq_len: int, base_shift: float = 0.5, max_shift: float = 1.15, shift: bool = True)` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/inference/sampling.py#L46)
- <a id="save_image"></a>`save_image(name: str, output_dir: str, x: torch.Tensor, add_sampling_metadata: bool, prompt: str)` — [`L234`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/inference/sampling.py#L234)
- <a id="time_shift"></a>`time_shift(mu: float, sigma: float, t: Tensor)` — [`L34`](../../../../../../../../raw/code/torchtitan/torchtitan/models/flux/inference/sampling.py#L34)

