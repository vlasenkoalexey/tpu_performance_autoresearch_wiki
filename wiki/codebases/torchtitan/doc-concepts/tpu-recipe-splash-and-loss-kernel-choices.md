---
title: Recipe kernel choices - Splash tiles/layouts, fused Pallas cross entropy vs full logits, packed QKV
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/recipes/
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Recipe kernel choices - Splash tiles/layouts, fused Pallas cross entropy vs full logits, packed QKV

## Definition
Beyond parallelism and flags, each TPU recipe fixes three kernel-level choices: the Splash (Pallas block-sparse
flash) attention tile sizes and Q/K/V layouts, how the loss is computed (XLA LM-head matmul + cross entropy over
full logits, or a vocab-tiled Pallas kernel that fuses the LM head with the loss so logits are never
materialized), and whether Q/K/V projections run as one packed matmul. The READMEs report when each choice wins:
the fused loss is a *memory* tool, not a speed tool, and packed QKV removes relayouts.

## In torchtitan (grounded)
- Splash knobs: [`SplashAttentionKernelConfig`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#SplashAttentionKernelConfig)
  - [`use_splash_attention_kernel`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#SplashAttentionKernelConfig.use_splash_attention_kernel),
  [`use_tokamax_splash_attention_kernel`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#SplashAttentionKernelConfig.use_tokamax_splash_attention_kernel),
  [`use_vmap_bwd`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#SplashAttentionKernelConfig.use_vmap_bwd),
  [`sa_use_document_aware_block_skipping`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#SplashAttentionKernelConfig.sa_use_document_aware_block_skipping),
  nine block sizes from [`sa_block_q`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#SplashAttentionKernelConfig.sa_block_q) to
  [`sa_block_kv_dq`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#SplashAttentionKernelConfig.sa_block_kv_dq) (default 512 each), and
  [`sa_q_layout`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#SplashAttentionKernelConfig.sa_q_layout) /
  [`sa_k_layout`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#SplashAttentionKernelConfig.sa_k_layout) /
  [`sa_v_layout`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#SplashAttentionKernelConfig.sa_v_layout) (default `HEAD_DIM_MINOR`).
- Fused loss: [`PallasCrossEntropyLoss`](../catalog/torchtitan/experiments/tpu/loss.md#PallasCrossEntropyLoss), installed together with
  an LM-head override by [`_enable_pallas_cross_entropy`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#_enable_pallas_cross_entropy)
  (Qwen3), its Llama3 twin [`_enable_pallas_cross_entropy`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#_enable_pallas_cross_entropy),
  and the soft-capped Muse Glimmer variant [`_enable_pallas_cross_entropy`](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md#_enable_pallas_cross_entropy)
  (passes [`soft_cap`](../catalog/torchtitan/experiments/tpu/loss.md#PallasCrossEntropyLoss.Config.soft_cap) and
  [`output_multiplier`](../catalog/torchtitan/experiments/tpu/loss.md#PallasCrossEntropyLoss.Config.output_multiplier) so the cap is applied per logits tile in-kernel).
  The older path is [`LossKernelConfig.use_loss_kernel`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#LossKernelConfig), used only by
  [`reg_trainer_qwen3_8b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b) among these recipes.
- Packed QKV: [`TpuPackedQKVConverter`](../catalog/torchtitan/experiments/tpu/qkv.md#TpuPackedQKVConverter) swaps in
  [`TpuPackedQKVLinear`](../catalog/torchtitan/experiments/tpu/qkv.md#TpuPackedQKVLinear), which keeps checkpoint keys
  per-projection via [`_split_qkv_on_save`](../catalog/torchtitan/experiments/tpu/qkv.md#TpuPackedQKVLinear._split_qkv_on_save) /
  [`_merge_qkv_on_load`](../catalog/torchtitan/experiments/tpu/qkv.md#TpuPackedQKVLinear._merge_qkv_on_load).

### Splash settings per recipe

| Recipe (config) | Splash variant | Tiles | Layouts / extras |
|---|---|---|---|
| Llama3 8B/70B ([`llama3_8b`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_8b), [`llama3_70b`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_70b)) | JAX Pallas Splash | all nine 2048 ("block size 2048") | Q/K `SEQ_MINOR` |
| Qwen3-8B v6e ([`reg_trainer_qwen3_8b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b)) | JAX Pallas Splash | all nine 1024 | defaults |
| Qwen3-8B tpu7x ([`qwen3_8b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_8b)) | Tokamax Splash, no document-aware block skipping | config: q/kv/dkv/q_dq/kv_dq 1024, kv_compute 512, q_dkv/kv_dkv 2048, kv_dkv_compute 1024; README commands: all nine 1024 | Q/K `SEQ_MINOR`, V `HEAD_DIM_MINOR` |
| Qwen3-32B (via `qwen3_8b_zero3`) | Tokamax Splash, `use_vmap_bwd` | inherited from `qwen3_8b` | as above |
| Qwen3-30B-A3B ([`_qwen3_moe_30b_fsdp_only_full_ac`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac)) | Tokamax Splash, `use_vmap_bwd`, batch-native masking | as `qwen3_8b` config | Q/K `SEQ_MINOR` |
| Muse Glimmer 30B ([`_muse_glimmer_30b_base`](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base)) | JAX Pallas Splash, local mask on sliding-window layers | all nine 1024 | defaults |
| FLUX, Conformer | Splash enabled from the CLI | defaults (512) | defaults |

Measured notes carried in config comments next to these choices: for Qwen3-30B on TPU7x, `sa_block_kv_compute=512`
gave a 26.3 ms (1.60%) step win and 0.199 GiB lower peak HBM even though the attention calls themselves got 2.5 ms
slower (a whole-program scheduling effect); batch-native masking + `use_vmap_bwd` lowered peak HBM from 14.924 to
14.575 GiB at local batch 6.

### Loss and projection choices with their measured trade-offs
- **Full logits vs fused cross entropy (Muse Glimmer 30B, tpu7x-4x4x4).** At 16384 tokens per device the logits
  do not set peak HBM (46.18 vs 46.12 GiB under plain `full` remat), so the fused kernel saves nothing while the
  plain XLA LM-head matmul + CE is ~2% faster (2,913 vs 2,851 TPS, 43.8% vs 42.9% MFU; config docstring). At
  2 x 16384 tokens per device, peak is 87.62 GiB with full logits vs 51.84 GiB fused, and the regular trainer
  runs out of HBM at step 1 with full logits. Hence `muse_glimmer_30b_full_logits` is the recipe and
  [`muse_glimmer_30b_fused_ce`](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md#muse_glimmer_30b_fused_ce)
  is the option for larger local batches or longer sequences.
- **Packed QKV (Qwen3-32B).** The README: Q/K/V run as one packed matmul; checkpoint keys stay `wq`/`wk`/`wv`
  but optimizer state is layout-specific. The `qwen3_32b` code comment quantifies it: -3.5% step time and
  -19.7 GiB peak HBM at local batch 8, by removing the fused projection's interleaved-output relayouts.
- **Legacy loss kernel on v6e.** The Trillium Qwen3 recipes pass `--loss_kernel.use_loss_kernel`; the Muse Glimmer
  registry notes that this legacy path bypasses the soft-capped LM head and is rejected for that model.

## Why it matters / when it applies
- Splash tiles are model- and topology-specific: Llama3 at seq 8192 uses 2048 tiles; Qwen3 at seq 2048-4096 uses
  1024 (or the asymmetric tokamax set). Tiles interact with the scoped-VMEM budget set by the recipe flags.
- The fused loss pays off only when logits dominate peak HBM (large vocab x many tokens per device); otherwise
  XLA's unfused matmul + CE was faster in the one A/B the READMEs report.
- Packed QKV changes optimizer-state layout, so it cannot be toggled when resuming from a checkpoint with optimizer state.

### Doc vs code at this commit
- The qwen3-8b tpu7x-4x4x4 README says "Q/K/V layouts and backward tiles are tuned for this model and topology",
  but its command passes all nine `--splash_attention_kernel.sa_block_*=1024`, which overrides the config's tuned
  asymmetric tiles (kv_compute 512, q_dkv / kv_dkv 2048); only the layouts and the tokamax kernel remain from the
  config. The 2x2x2 README is explicit that it sets "1024 across the board". Running `--config=qwen3_8b` without
  those flags gives the config tiles, not the README's.

## Connections
- Code concepts: [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md),
  [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md),
  [model-building-blocks](../concepts/model-building-blocks.md), [training-components](../concepts/training-components.md),
  [qwen3-model](../concepts/qwen3-model.md), [muse-glimmer-model](../concepts/muse-glimmer-model.md),
  [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md),
  [config-overrides](../concepts/config-overrides.md)
- Module catalogs: [tpu_job_config](../catalog/torchtitan/experiments/tpu/tpu_job_config.md),
  [loss](../catalog/torchtitan/experiments/tpu/loss.md), [qkv](../catalog/torchtitan/experiments/tpu/qkv.md),
  [qwen3/config_registry](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md),
  [muse_glimmer/config_registry](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md),
  [llama3/config_registry](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md)
- Related doc-concepts: [tpu-recipe-matrix](tpu-recipe-matrix.md),
  [tpu-recipe-memory-policy-and-save-regions](tpu-recipe-memory-policy-and-save-regions.md),
  [tpu-recipe-libtpu-flag-sets](tpu-recipe-libtpu-flag-sets.md),
  [tpu-splash-attention-tiles-and-vmem](tpu-splash-attention-tiles-and-vmem.md),
  [tpu-fused-linear-cross-entropy](tpu-fused-linear-cross-entropy.md),
  [tpu-moe-kernel-switches](tpu-moe-kernel-switches.md)

## Source
Extracted from (kept in place):
- `torchtitan/experiments/tpu/recipes/ironwood/muse-glimmer-30b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-32b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-8b/tpu7x-2x2x2/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-8b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/llama3-70b/tpu7x-64/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/llama3-8b/v6e-8/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/llama3-8b/v6e-256/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/qwen3-8b/v6e-8/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/qwen3-8b/v6e-256/README.md`

Cross-checked against `torchtitan/experiments/tpu/tpu_job_config.py`, `qkv.py`, `loss.py` and the config
registries at commit 2ad96c939.
