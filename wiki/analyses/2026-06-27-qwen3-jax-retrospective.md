---
title: "Retrospective — qwen3 / jax as of 2026-06-27"
type: analysis
tags: [retrospective, qwen3, jax]
model: qwen3
lane: jax
created: 2026-06-27
updated: 2026-06-27
---

# qwen3 / jax retrospective — 2026-06-27

**Scope**: 8B/v6e-8
**Period**: 2026-06-26 → 2026-06-27
**Experiments**: 13 total
**Frontier**: 32.5% MFU (v009)

## Search-strategy assessment

⚠️ **Single-axis-heavy vs Kernel Work**: The recent experiments (v011, v012, v013) shifted to Pallas kernel ports, but have encountered backward pass autodiff friction.
⚠️ **Frontier stuck**: The highest MFU remains 32.5% from `v009-scan-over-layers`.

**Inference**: We need to solve the Pallas custom VJP backward pass HBM materialization issue. Without it, custom kernels like Fused GLU and RMSNorm+RoPE cannot be utilized efficiently for training.

## Mechanism tree

- **torch.compile + scan-over-layers**
  - nnx.scan over layers — 🏆 v009 +32.5% MFU
- **Splash attention**
  - splash integration — ✅ v001
  - splash 2048 blocks — ❌ v007
  - ring attention (sp=2) — ✅ v012 (22.8% MFU, regression due to comms)
- **FSDP / collective optimization**
  - async-overlap flags — ❌ v010
  - sparsecore-offload — ❌ v008
- **Pallas kernels**
  - rmsnorm-rope — 💥 v011 (crashed, no VJP)
  - fused-glu — ❌ v013 (30.6% MFU, HBM materialization due to jax.custom_vjp fallback)
  - 🔵 tokamax CE — UNEXPLORED / WIP
- **Activation Checkpointing (AC)**
  - gradient checkpointing — ✅ v004

## Coverage gaps — what's NOT been explored

- Custom VJPs for Pallas kernels in the backward pass.
- FSDP over sequence chunks (Ring Attention optimizations).

## Recommended next directions

| # | Direction | Topic | Gain | Conf | Effort | Score | Source |
|---|---|---|---|---|---|---|---|
| 1 | Pallas Custom VJP for Fused GLU backward pass | Pallas kernels | +2-3pp | high | L | 0.33 | local-gap |
| 2 | Profile Ring Attention sp=2 communication overhead | FSDP / Splash | +5pp | medium | M | 1.16 | local-gap |
| 3 | Tokamax Cross-Entropy loss | CE / Softmax | +1-2pp | high | M | 0.33 | local-gap |

## Anti-recommendations

- Standard `jax.custom_vjp` on Pallas kernels without a custom backward kernel (causes massive intermediate HBM materialization).

## Experiment ledger (machine-readable)

| v-ID | Date | Variant | Topic | Verdict | Frontier-shift |
|---|---|---|---|---|---|
| v009 | 2026-06-27 | 8B/v6e-8 | torch.compile | supported | yes |
| v010 | 2026-06-27 | 8B/v6e-8 | fsdp | refuted | no |
| v011 | 2026-06-27 | 8B/v6e-8 | pallas-kernels | invalid | no |
| v012 | 2026-06-27 | 8B/v6e-8 | splash-attention | supported | no |
| v013 | 2026-06-27 | 8B/v6e-8 | pallas-kernels | refuted | no |
