---
title: 'Module: torchtitan/models/flux/sharding.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.sharding`/
symbols:
  set_flux_sharding_config: set_flux_sharding_config().
  set_flux_inner_attention_local_map: set_flux_inner_attention_local_map().
  annotate_flux_forward_inputs: annotate_flux_forward_inputs().
  flux_activation_placement: flux_activation_placement().
  DP: DP.
  CP: CP.
---
# Module: [`torchtitan/models/flux/sharding.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/sharding.py)

## Functions
- <a id="annotate_flux_forward_inputs"></a>`annotate_flux_forward_inputs(*, latents: torch.Tensor, latent_pos_enc: torch.Tensor, t5_encodings: torch.Tensor, text_pos_enc: torch.Tensor, target: torch.Tensor, clip_encodings: torch.Tensor, timesteps: torch.Tensor)` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/sharding.py#L71)
- <a id="flux_activation_placement"></a>`flux_activation_placement(*, cp: spmd.PerMeshAxisSpmdType)` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/sharding.py#L25)
- <a id="set_flux_inner_attention_local_map"></a>`set_flux_inner_attention_local_map(inner_attention_cfg)` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/sharding.py#L37)
- <a id="set_flux_sharding_config"></a>`set_flux_sharding_config(config: FluxModel.Config)` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/sharding.py#L61) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)

## Module values
- <a id="CP"></a>`CP` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/sharding.py#L22)
- <a id="DP"></a>`DP` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/sharding.py#L21)

