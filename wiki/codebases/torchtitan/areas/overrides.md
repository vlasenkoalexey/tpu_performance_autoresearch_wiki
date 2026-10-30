---
title: 'Area: torchtitan/overrides'
type: area
area: 'torchtitan/overrides'
description: 'Kernel/module overrides of torchtitan: config-driven replacement of RoPE, norms, fused SwiGLU/MLA and grouped experts with Triton/Helion implementations.'
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Area: `torchtitan/overrides`

## Purpose
`torchtitan/overrides/` registers module overrides that a recipe applies by config (fused grouped experts, Helion RoPE, Triton norms, fused MLA attention); see [config-overrides](../concepts/config-overrides.md). All in-repo overrides here are CUDA-only. The TPU lane keeps its own override modules (bf16 and scan-safe RoPE, a Pallas fused-loss LM head, an MoE token counter).

## How the units connect
- [config-overrides](../concepts/config-overrides.md) uses the traversal in [model-spec-protocols](../concepts/model-spec-protocols.md) to rewrite the config tree before the model is built by [trainer-and-train-loop](../concepts/trainer-and-train-loop.md).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `torchtitan/overrides`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `torchtitan/overrides` | 5 | 142 | 11 | [`forward`](../catalog/torchtitan/overrides/fused_mla.md#FusedMLAAttention.forward "torchtitan/overrides/fused_mla.py:L818"), [`forward`](../catalog/torchtitan/overrides/offset_rmsnorm.md#TritonOffsetRMSNorm.forward "torchtitan/overrides/offset_rmsnorm.py:L317"), [`FusedSwiGLU`](../catalog/torchtitan/overrides/fused_swiglu.md#FusedSwiGLU "torchtitan/overrides/fused_swiglu.py:L450") | [config-overrides](../concepts/config-overrides.md) |

<!-- area:auto:end -->
