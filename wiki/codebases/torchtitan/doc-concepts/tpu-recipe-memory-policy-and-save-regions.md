---
title: Recipe memory policies - full AC vs tpu_selective save regions (Splash output, MoE routing)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/recipes/ironwood/muse-glimmer-30b/tpu7x-4x4x4/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Recipe memory policies - full AC vs tpu_selective save regions (Splash output, MoE routing)

## Definition
The TPU recipes almost always recompute the whole transformer block in backward. On the regular trainer
this is eager full activation checkpointing (`activation-checkpoint:full`); on GraphTrainer it is a graph
memory policy. The newest Ironwood recipes use `tpu_selective`: recompute everything `full` would,
**except** named *save regions* whose values are kept for backward - `attention.inner_attention` (each
layer's Splash output and LSE, so backward does not rerun the forward Splash kernel) and `moe.routing`
(router top-k ids and token sort permutation). A region can be saved in every layer or only in the last N
layers, trading step time for peak HBM roughly linearly.

## In torchtitan (grounded)
- Region names are constants in `remat_regions`:
  [`ATTENTION_INNER_ATTENTION`](../catalog/torchtitan/experiments/tpu/remat_regions.md#ATTENTION_INNER_ATTENTION) and
  [`MOE_ROUTING`](../catalog/torchtitan/experiments/tpu/remat_regions.md#MOE_ROUTING); model code marks values with
  [`annotate_region`](../catalog/torchtitan/experiments/tpu/remat_regions.md#annotate_region) (metadata only, does not change what runs).
- Policy selection: [`TpuGraphTrainerCompileConfig.memory_policy`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.memory_policy),
  [`save_regions`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.save_regions)
  (saved in every layer) and
  [`save_last_n_layers`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#TpuGraphTrainerCompileConfig.save_last_n_layers)
  (saved only in the last N layers, which backward reaches first). A region goes in one of the two, not both;
  [`resolve_save_regions`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.md#resolve_save_regions)
  enforces that, and [`_validate_tpu_selective`](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md#_validate_tpu_selective)
  rejects save regions under any policy other than `tpu_selective` / `tpu_selective_and_offload`.
- The pass: [`full_remat_with_saves`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.md#full_remat_with_saves)
  with selectors [`select_splash_attention`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.md#select_splash_attention)
  and [`select_routing`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.md#select_routing).
- Eager side: [`FullAC`](../catalog/torchtitan/distributed/activation_checkpoint.md#FullAC) /
  [`SelectiveAC`](../catalog/torchtitan/distributed/activation_checkpoint.md#SelectiveAC) with
  [`preserve_rng_state`](../catalog/torchtitan/distributed/activation_checkpoint.md#ActivationCheckpointing.Config.preserve_rng_state)
  (the FLUX recipes pass `--activation-checkpoint.no-preserve-rng-state`).

### Memory policy per recipe

| Recipe | Trainer | Policy |
|---|---|---|
| Llama3 8B/70B (v6e, tpu7x) | TPUTrainer | `FullAC` from config ([`llama3_70b`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_70b)) |
| FLUX.1-dev (v6e, tpu7x) | TPUTrainer | `activation-checkpoint:full`, no RNG-state preservation |
| Qwen3-8B v6e | TPUTrainer | `FullAC`; README: `SelectiveAC` OOMs on v6e "due to XLA activation limits"; plus `materialize_forward_before_backward` |
| Conformer v6e-8 | minimal loop | full AC |
| Qwen3-8B tpu7x ([`qwen3_8b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_8b)) | GraphTrainer | `memory_policy="default"` (Zero-2) |
| Qwen3-32B tpu7x ([`qwen3_32b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_32b)) | GraphTrainer | `full` (inherited from `qwen3_8b_zero3`) |
| Muse Glimmer 30B ([`muse_glimmer_30b_full_logits`](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md#muse_glimmer_30b_full_logits)) | GraphTrainer | `tpu_selective`, save `attention.inner_attention` |
| Qwen3-30B-A3B ([`_qwen3_moe_30b_fsdp_only_full_ac`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac)) | GraphTrainer | `tpu_selective`, save `moe.routing` + `attention.inner_attention` |
| Mamba2 / Mamba3 256K ([`mamba2_2_7b_256k`](../catalog/torchtitan/experiments/tpu/examples/mamba2/config_registry.md#mamba2_2_7b_256k)) | TPUTrainer | `FullAC` |

### Measured trade-offs

Muse Glimmer 30B on tpu7x-4x4x4 (10/14/2026, c4_test, mean of steps 10-30, 52 layers):

| Memory policy | Step time | MFU | Physical peak HBM |
|---|---|---|---|
| `full` | ~5.60 s | ~44.0% | 46.18 GiB |
| Splash saved in last 26 layers | ~5.45 s (-2.6%) | ~45.2% | 46.18 GiB |
| Splash saved in all 52 layers (default) | ~5.32 s (-5.1%) | ~46.3% | 63.77 GiB |

Qwen3-30B-A3B on tpu7x-4x4x4: routing + Splash saved in every layer is 2.9% faster per step than plain `full`
for ~13.5 GiB more peak HBM per device. Saving Splash costs ~0.28 GiB per layer; saving it in only the last 24
layers was 1.6% faster than `full` for 6.8 GiB more. Routing state is under 1 MiB per layer. Losses match `full`
(stated for Muse Glimmer).

CLI recipes from the READMEs:
- Opt out: `--compile.memory_policy=full --compile.save_regions` (the bare flag clears the regions, which only apply to `tpu_selective`).
- Half the speedup at no extra peak (Muse Glimmer): `--compile.save_regions --compile.save_last_n_layers attention.inner_attention 26`.
- Qwen3-30B-A3B partial: `--compile.save_regions moe.routing --compile.save_last_n_layers attention.inner_attention 24`.

## Why it matters / when it applies
- The READMEs' rationale for saving the Splash output is that backward then does not rerun the forward Splash
  kernel; both recipes measured a step-time win for it (2.9-5.1%) at a per-layer HBM cost.
- The "last N layers" form is useful when peak HBM is set by the early part of backward: the Muse Glimmer
  last-26 point gets -2.6% step time with an unchanged 46.18 GiB peak.
- On v6e selective AC did not fit for Qwen3-8B, so the v6e recipes stay on full AC and the
  regular trainer.
- Recompute policy also determines what an in-graph optimizer and the FSDP barrier policy can overlap; the
  barrier policies require remat barriers ([tpu-recipe-simplefsdp-schedules](tpu-recipe-simplefsdp-schedules.md)).

## Connections
- Code concepts: [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md),
  [tpu-graph-trainer](../concepts/tpu-graph-trainer.md), [graph-trainer](../concepts/graph-trainer.md),
  [training-components](../concepts/training-components.md), [muse-glimmer-model](../concepts/muse-glimmer-model.md),
  [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md)
- Module catalogs: [remat_regions](../catalog/torchtitan/experiments/tpu/remat_regions.md),
  [graph_trainer/tpu_memory_policy](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.md),
  [graph_trainer/config](../catalog/torchtitan/experiments/tpu/graph_trainer/config.md),
  [distributed/activation_checkpoint](../catalog/torchtitan/distributed/activation_checkpoint.md)
- Related doc-concepts: [tpu-recipe-matrix](tpu-recipe-matrix.md),
  [tpu-recipe-simplefsdp-schedules](tpu-recipe-simplefsdp-schedules.md),
  [tpu-recipe-splash-and-loss-kernel-choices](tpu-recipe-splash-and-loss-kernel-choices.md),
  [tpu-graph-trainer-memory-policies](tpu-graph-trainer-memory-policies.md),
  [graph-trainer-memory-policy](graph-trainer-memory-policy.md),
  [tpu-scan-graph-splitter-cpu-offload](tpu-scan-graph-splitter-cpu-offload.md)

## Source
Extracted from (kept in place):
- `torchtitan/experiments/tpu/recipes/ironwood/muse-glimmer-30b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-30b-a3b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-32b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/qwen3-8b/v6e-8/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/qwen3-8b/v6e-256/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/flux1/v6e-8/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/llama3-70b/tpu7x-2x2x4/README.md`

Cross-checked against `torchtitan/experiments/tpu/remat_regions.py`,
`torchtitan/experiments/tpu/graph_trainer/tpu_memory_policy.py` and `graph_trainer/config.py` at commit 2ad96c939.
