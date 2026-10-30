---
title: SDPA backend selection when porting attention code
type: doc-concept
provenance: doc
source: docs/markdown/porting_vit_mnist.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T02:38:46Z}
---
# SDPA backend selection when porting attention code

## Definition
The ViT porting tutorial writes multi-head attention by hand (`q @ k.transpose(-2, -1)`, `softmax`, `@ v`) in a `TpuAttentionBlock` whose docstring says it "avoids SDP MATH fallback on TPU". The message for porters: `F.scaled_dot_product_attention` on TPU picks among backends, and if the inputs miss the fast paths it falls back to the generic decomposed MATH path.

## In torch_tpu (grounded)
The choice is made by the TPU override of `aten::_fused_sdp_choice`, [`AtenFusedSdpChoice`](../catalog/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc.md#AtenFusedSdpChoice "csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc:L123"), which reads the user's `torch.backends.cuda` SDP enable flags and returns, in order:
1. **Flash** (reported in the `cudnn_attention` slot, implemented by the Mosaic flash-attention kernel, e.g. [`CreateFlashAttentionKernelImpl`](../catalog/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc.md#CreateFlashAttentionKernelImpl "csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc:L468")) when inputs are f32/bf16, static-shaped, same rank, query rank >= 4, head dim < 128 or divisible by 128, dropout in [0, 1), and the mask does not require grad.
2. **SHLO "optimized MATH"** (the `overrideable` slot, [`ScaledDotProductFusedAttentionShlo`](../catalog/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc.md#ScaledDotProductFusedAttentionShlo "csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc:L885")) when flash does not apply but there is a batch dim, no dropout, a floating dtype and a no-grad mask.
3. **MATH** - upstream's op-by-op decomposition - only as the last resort; if MATH is also disabled it raises `kFailedPrecondition`.

Each miss emits a one-time `kPerformance` warning listing the violated condition, so a porting run's warnings tell you which branch you landed on.

## Why it matters / when it applies
- The tutorial's tiny ViT (head dim 32, explicit matmuls) sidesteps the question entirely. In real models, calling `F.scaled_dot_product_attention` with 4-D bf16 inputs is the better choice: it reaches the flash kernel, which a hand-written `softmax(q k^T) v` never will.
- Watch for the conditions that silently demote you: dynamic shapes, dropout during training, a 3-D (no batch) layout, a mask with `requires_grad`, or an odd head dim.
- `_fused_sdp_choice` arguments that do not affect the SHLO are excluded from the cache key, so toggling them does not recompile.

## Connections
- Code concepts: [scaled-dot-product-attention](../concepts/scaled-dot-product-attention.md), [mosaic-matmul](../concepts/mosaic-matmul.md), [pallas-custom-kernels](../concepts/pallas-custom-kernels.md), [compilation-cache-key](../concepts/compilation-cache-key.md), [dynamic-shape-ops](../concepts/dynamic-shape-ops.md)
- Module catalogs: [csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc](../catalog/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc.md), [csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc](../catalog/csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_shlo.cc.md), [csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc](../catalog/csrc/ops/scaled_dot_product_attention/flash_attention_kernel_builder.cc.md)
- Related doc-concepts: [host-sync-avoidance-in-training-loops](host-sync-avoidance-in-training-loops.md), [pallas-jax-op-bridge](pallas-jax-op-bridge.md), [torch-compile-static-shapes-and-bounded-dynamism](torch-compile-static-shapes-and-bounded-dynamism.md)

## Source
Extracted from `docs/markdown/porting_vit_mnist.md` (kept in place). Backend conditions verified in `csrc/ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc`.
