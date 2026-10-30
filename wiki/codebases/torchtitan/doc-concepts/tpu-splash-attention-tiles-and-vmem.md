---
title: Splash attention block sizes and the scoped VMEM budget
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/torch-tpu-optimization-guide.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Splash attention block sizes and the scoped VMEM budget

## Definition
Splash attention is a flash-style TPU Pallas attention kernel patched into a model's attention. Like
every Pallas kernel its speed depends on block (tile) sizes, and the usable tiles are capped by the
per-core **scoped VMEM limit** (`xla_tpu_scoped_vmem_limit_kib`), whose libtpu default is
conservative. The guide's rule: defaults are a starting point - sweep tiles per model shape and TPU
generation, gated by the VMEM budget.

## In torchtitan (grounded)
- Kernel: [`SplashAttention`](../catalog/torchtitan/experiments/tpu/kernels/splash_attention.md#SplashAttention);
  patched into the model by [`use_splash_attention_patch`](../catalog/torchtitan/experiments/tpu/workarounds.md#use_splash_attention_patch)
  (tokamax variant: [`use_tokamax_splash_attention_patch`](../catalog/torchtitan/experiments/tpu/workarounds.md#use_tokamax_splash_attention_patch),
  [`splash_sdpa`](../catalog/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.md#splash_sdpa)),
  applied from [`apply_patches`](../catalog/torchtitan/experiments/tpu/workarounds.md#apply_patches).
- Config: [`SplashAttentionKernelConfig`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#SplashAttentionKernelConfig)
  (CLI `--splash_attention_kernel.*`):

| Field | Default | Note |
|---|---|---|
| `use_splash_attention_kernel` / `use_tokamax_splash_attention_kernel` | False | enable (one of) |
| `sa_block_q`, `sa_block_kv`, `sa_block_kv_compute` | 512 | forward tiles; retune q/kv first |
| `sa_block_q_dkv`, `sa_block_kv_dkv`, `sa_block_kv_dkv_compute`, `sa_block_dkv` | 512 | dK/dV backward tiles |
| `sa_block_q_dq`, `sa_block_kv_dq` | 512 | dQ tiles (unused under the fused backward) |
| `sa_use_fused_bwd_kernel` | True | fused dQ/dKV backward |
| `sa_q_layout`, `sa_k_layout`, `sa_v_layout` | `HEAD_DIM_MINOR` | `SEQ_MINOR` used by Llama3 recipes |
| `sa_use_document_aware_block_skipping` | True | skip cross-document blocks (exact segment-id masking either way) |
| `use_vmap_bwd` | False | vectorize backward instead of a memory-safe sequential scan; validate peak HBM |

- Recipe example: [`llama3_8b`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_8b)
  uses all nine blocks at **2048** with `SEQ_MINOR` q/k layouts at seq 8192; the HF backend lane uses
  1024 forward/dkv blocks (512 measured worse, 2048 failed to compile on its packed 2048-token
  stream; [`_tpu_hf_config`](../catalog/torchtitan/experiments/tpu/transformers_modeling_backend/config_registry.md#_tpu_hf_config)).
- VMEM is a libtpu flag, set through the config's flag layer
  ([tpu-libtpu-xla-flag-layering](tpu-libtpu-xla-flag-layering.md)), e.g.
  `--extra-libtpu-init-flags=xla_tpu_scoped_vmem_limit_kib=65536`.

## Why it matters / when it applies
- Splash matters most at **long sequence** and under memory pressure; at short sequence it is often
  a wash against TorchTPU's built-in flash SDPA - measure before adopting.
- Larger blocks (1024/2048) help at long sequence *if they fit VMEM*; 256 cuts VMEM but usually
  underperforms and can trip kernel constraints.
- **VMEM guidance:** on v6e (Trillium) the guide's recommended value is `65536` KiB (64 MiB), the
  value the Trillium recipes converged on (older baselines used 131072). Raise it if a kernel reports
  insufficient VMEM for a bigger tile; lower it on VMEM-limit rejections at startup. It is
  generation-specific - verify it is accepted at init. Shipped recipes span 65472 / 65536 / 131072
  (e.g. the Llama3 scan bundle uses 131072).
- Under GraphTrainer's `default` memory policy splash output is recomputed (it is a Pallas custom op,
  not on the save list); only `tpu_selective` saves it - see
  [tpu-graph-trainer-memory-policies](tpu-graph-trainer-memory-policies.md). Under the regular trainer,
  [`AttentionSavingSelectiveAC`](../catalog/torchtitan/experiments/tpu/activation_checkpoint.md#AttentionSavingSelectiveAC)
  keeps the Pallas attention output.

## Connections
- Code concepts: [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md),
  [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md),
  [model-building-blocks](../concepts/model-building-blocks.md),
  [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md)
- Module catalogs: [kernels/splash_attention](../catalog/torchtitan/experiments/tpu/kernels/splash_attention.md),
  [kernels/tokamax_splash_attention](../catalog/torchtitan/experiments/tpu/kernels/tokamax_splash_attention.md),
  [workarounds](../catalog/torchtitan/experiments/tpu/workarounds.md),
  [tpu_job_config](../catalog/torchtitan/experiments/tpu/tpu_job_config.md),
  [activation_checkpoint (tpu)](../catalog/torchtitan/experiments/tpu/activation_checkpoint.md)
- Related doc-concepts: [tpu-fused-linear-cross-entropy](tpu-fused-linear-cross-entropy.md),
  [tpu-libtpu-xla-flag-layering](tpu-libtpu-xla-flag-layering.md),
  [hf-transformers-backend-on-tpu](hf-transformers-backend-on-tpu.md),
  [tpu-moe-kernel-switches](tpu-moe-kernel-switches.md),
  [tpu-recipe-splash-and-loss-kernel-choices](tpu-recipe-splash-and-loss-kernel-choices.md)

## Source
Extracted from `torchtitan/experiments/tpu/torch-tpu-optimization-guide.md` (section 4, "Splash
attention" and "VMEM budget"; kept in place).
