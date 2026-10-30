---
title: Muse Glimmer architecture (iRoPE, per-layer sliding windows, soft-capped LM head, vision path)
type: doc-concept
provenance: doc
source: torchtitan/models/muse_glimmer/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Muse Glimmer architecture (iRoPE, per-layer sliding windows, soft-capped LM head, vision path)

## Definition
Muse Glimmer is a GQA decoder (30B: dim 6656, 52 layers, 32 Q / 2 KV heads, head dim 128, vocab
202048) with an optional vision encoder + adapter that the model owns and runs inside `forward`.
Its distinctive pieces are gain-centered and scaleless RMSNorms, QK-norm before RoPE with a tuned
query scale and a sigmoid output gate, iRoPE (RoPE skipped on every 4th layer), a cyclic per-layer
pattern of sliding-window vs global attention, post-norm residuals, SwiGLU FFN, and a soft-capped
LM head.

## In torchtitan (grounded)
- Model: [`MuseGlimmerModel`](../catalog/torchtitan/models/muse_glimmer/model.md#MuseGlimmerModel "torchtitan/models/muse_glimmer/model.py:L262")
  ([`Config`](../catalog/torchtitan/models/muse_glimmer/model.md#MuseGlimmerModel.Config "torchtitan/models/muse_glimmer/model.py:L270")),
  [`MuseGlimmerTransformerBlock`](../catalog/torchtitan/models/muse_glimmer/model.md#MuseGlimmerTransformerBlock),
  [`RMSGainCenterNorm`](../catalog/torchtitan/models/muse_glimmer/model.md#RMSGainCenterNorm)
  (effective scale `weight + gain_center`, weight initialized to 0),
  [`EmbeddingWithNorm`](../catalog/torchtitan/models/muse_glimmer/model.md#EmbeddingWithNorm), and
  [`SoftCappedLinear`](../catalog/torchtitan/models/muse_glimmer/model.md#SoftCappedLinear "torchtitan/models/muse_glimmer/model.py:L190") (output
  multiplier + tanh soft-cap inside the head, so it stays correct under `ChunkedLossWrapper`).
- Vision: [`MuseGlimmerVisionEncoder`](../catalog/torchtitan/models/muse_glimmer/vision_encoder.md#MuseGlimmerVisionEncoder "torchtitan/models/muse_glimmer/vision_encoder.py:L208"),
  [`MuseGlimmerVisionAdapter`](../catalog/torchtitan/models/muse_glimmer/vision_encoder.md#MuseGlimmerVisionAdapter).
- Parallelism: [`parallelize_muse_glimmer`](../catalog/torchtitan/models/muse_glimmer/parallelize.md#parallelize_muse_glimmer "torchtitan/models/muse_glimmer/parallelize.py:L30"),
  [`set_muse_glimmer_sharding_config`](../catalog/torchtitan/models/muse_glimmer/sharding.md#set_muse_glimmer_sharding_config "torchtitan/models/muse_glimmer/sharding.py:L55"),
  [`set_muse_glimmer_vision_sharding_config`](../catalog/torchtitan/models/muse_glimmer/sharding.md#set_muse_glimmer_vision_sharding_config "torchtitan/models/muse_glimmer/sharding.py:L183").
- Recipes: [`muse_glimmer_debugmodel`](../catalog/torchtitan/models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel "torchtitan/models/muse_glimmer/config_registry.py:L113"),
  [`muse_glimmer_30b`](../catalog/torchtitan/models/muse_glimmer/config_registry.md#muse_glimmer_30b "torchtitan/models/muse_glimmer/config_registry.py:L205"),
  [`muse_glimmer_30b_mm`](../catalog/torchtitan/models/muse_glimmer/config_registry.md#muse_glimmer_30b_mm "torchtitan/models/muse_glimmer/config_registry.py:L243");
  CP variants are built with `ContextParallelTransform` in `torchtitan_recipes/muse_glimmer.py`.
- **TPU lane** (`torchtitan/experiments/tpu/muse_glimmer/`): upstream implements the per-layer
  windows only for the `flex` (BlockMask dict) and `varlen` (FA3) backends, neither of which runs on
  TPU, and plain SDPA silently ignores the window. The TPU lane adds
  [`SlidingWindowScaledDotProductInnerAttention`](../catalog/torchtitan/experiments/tpu/muse_glimmer/attention.md#SlidingWindowScaledDotProductInnerAttention "torchtitan/experiments/tpu/muse_glimmer/attention.py:L118")
  (explicit causal sliding-window mask; exposes
  [`sliding_window_size`](../catalog/torchtitan/experiments/tpu/muse_glimmer/attention.md#SlidingWindowScaledDotProductInnerAttention.sliding_window_size)
  so the Splash patch picks a `LocalMask`), [`TpuMuseGlimmerAttention`](../catalog/torchtitan/experiments/tpu/muse_glimmer/attention.md#TpuMuseGlimmerAttention),
  TPU parallelization ([`parallelize_muse_glimmer`](../catalog/torchtitan/experiments/tpu/muse_glimmer/infra/parallelize.md#parallelize_muse_glimmer)),
  and fused-CE recipes such as [`muse_glimmer_30b_fused_ce`](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md#muse_glimmer_30b_fused_ce),
  which use [`fused_loss_soft_capped_lm_head`](../catalog/torchtitan/experiments/tpu/overrides/fused_loss.md#fused_loss_soft_capped_lm_head)
  to re-apply the soft cap inside the loss kernel.

## Why it matters / when it applies
- **Sliding-window layers are where attention FLOPs are saved** - but only if the backend honors the
  window. On TPU an SDPA path without the window runs every layer as full causal attention: a silent
  perf (and semantics) change worth checking in any Muse Glimmer HLO/profile. Window conventions
  differ by one: Muse Glimmer `window_size=W` (`0 <= q-k < W`) vs Splash `local_window_size=L`
  (`0 <= q-k <= L`), so `sliding_window_size = window_size - 1`.
- **Soft-capped head and fused loss:** because the cap is part of the head, fusing the LM-head
  projection into the cross-entropy kernel must carry the cap along - the TPU fused-loss override for
  `SoftCappedLinear` does exactly that.
- **Parallelism:** FSDP, HSDP, TP, SP, CP, `torch.compile`, and PP. The multimodal path supports CP,
  TP+CP+SP, and TP+CP+PP+SP, keeping vision compute replicated across CP; multimodal fusion is
  TP-replicated and the first decoder layer restores the standard (sequence-parallel) layout. Vision
  bank indices are prepared before token sharding.
- **Flex backend upstream:** sliding-window vs global attention is currently implemented with the
  Flex attention backend.

## Connections
- Code concepts: [muse-glimmer-model](../concepts/muse-glimmer-model.md),
  [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md),
  [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md),
  [model-building-blocks](../concepts/model-building-blocks.md),
  [training-components](../concepts/training-components.md).
- Module catalogs: [torchtitan/models/muse_glimmer/model](../catalog/torchtitan/models/muse_glimmer/model.md),
  [torchtitan/models/muse_glimmer/sharding](../catalog/torchtitan/models/muse_glimmer/sharding.md),
  [torchtitan/experiments/tpu/muse_glimmer/attention](../catalog/torchtitan/experiments/tpu/muse_glimmer/attention.md),
  [torchtitan/experiments/tpu/overrides/fused_loss](../catalog/torchtitan/experiments/tpu/overrides/fused_loss.md).
- Related doc-concepts: [model-support-overview](model-support-overview.md),
  [model-config-transforms](model-config-transforms.md),
  [configurable-overrides](configurable-overrides.md),
  [tpu-fused-linear-cross-entropy](tpu-fused-linear-cross-entropy.md),
  [tpu-splash-attention-tiles-and-vmem](tpu-splash-attention-tiles-and-vmem.md).

## Source
Extracted from `torchtitan/models/muse_glimmer/README.md` (kept in place).
