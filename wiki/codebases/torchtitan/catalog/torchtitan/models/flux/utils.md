---
title: 'Module: torchtitan/models/flux/utils.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/utils.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.utils`/
symbols:
  preprocess_data: preprocess_data().
  pack_latents: pack_latents().
  PATCH_HEIGHT: PATCH_HEIGHT.
  PATCH_WIDTH: PATCH_WIDTH.
  create_position_encoding_for_latents: create_position_encoding_for_latents().
  IMAGE_LATENT_SIZE_RATIO: IMAGE_LATENT_SIZE_RATIO.
  generate_noise_latent: generate_noise_latent().
  unpack_latents: unpack_latents().
  LATENT_CHANNELS: LATENT_CHANNELS.
---
# Module: [`torchtitan/models/flux/utils.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/utils.py)

## Functions
- <a id="create_position_encoding_for_latents"></a>`create_position_encoding_for_latents(bsz: int, latent_height: int, latent_width: int, position_dim: int = 3)` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/utils.py#L92) — Create the packed latents' position encodings for the Flux flow model. — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
- <a id="generate_noise_latent"></a>`generate_noise_latent(bsz: int, height: int, width: int, device: str | torch.device, dtype: torch.dtype, seed: int | None = None)` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/utils.py#L61) — Generate noise latents for the Flux flow model. The random seed will be set at the beginning of training.
- <a id="pack_latents"></a>`pack_latents(x: Tensor)` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/utils.py#L126) — Rearrange latents from an image-like format into a sequence of patches. — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
- <a id="preprocess_data"></a>`preprocess_data(device: torch.device, dtype: torch.dtype, *, autoencoder: AutoEncoder | None, clip_encoder: FluxEmbedder, t5_encoder: FluxEmbedder, batch: dict[str, Tensor])` — [`L18`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/utils.py#L18) — Take a batch of inputs and encoder as input and return a batch of preprocessed data. — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
- <a id="unpack_latents"></a>`unpack_latents(x: Tensor, latent_height: int, latent_width: int)` — [`L153`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/utils.py#L153) — Rearrange latents from a sequence of patches into an image-like format.

## Module values
- <a id="IMAGE_LATENT_SIZE_RATIO"></a>`IMAGE_LATENT_SIZE_RATIO` — [`L15`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/utils.py#L15)
- <a id="LATENT_CHANNELS"></a>`LATENT_CHANNELS` — [`L15`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/utils.py#L15)
- <a id="PATCH_HEIGHT"></a>`PATCH_HEIGHT` — [`L14`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/utils.py#L14)
- <a id="PATCH_WIDTH"></a>`PATCH_WIDTH` — [`L14`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/utils.py#L14)

