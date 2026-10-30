---
title: Kimi K2.x (DeepSeek-V3 decoder + MoonViT3d) - QK clipping, DistMuon, parallelism limits
type: doc-concept
provenance: doc
source: torchtitan/models/kimi_k2_7/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Kimi K2.x (DeepSeek-V3 decoder + MoonViT3d) - QK clipping, DistMuon, parallelism limits

## Definition
Kimi K2.5, K2.6, and K2.7-Code share one architecture: a DeepSeek-V3-style decoder (Multi-head
Latent Attention + MoE) paired with a MoonViT3d vision encoder whose projected embeddings are
scattered into the text sequence at media-placeholder runs. All TorchTitan recipes train with
DistMuon plus the Kimi K2 "QK clipping" update. The package also hosts Moonlight-16B-A3B
(text-only) and Kimi-VL-A3B.

## In torchtitan (grounded)
- Model: [`KimiK25Model`](../catalog/torchtitan/models/kimi_k2_7/model.md#KimiK25Model "torchtitan/models/kimi_k2_7/model.py:L45") with
  [`KimiK25VisionEncoder`](../catalog/torchtitan/models/kimi_k2_7/vision_encoder.md#KimiK25VisionEncoder "torchtitan/models/kimi_k2_7/vision_encoder.py:L472") /
  [`MoonViTEncoder`](../catalog/torchtitan/models/kimi_k2_7/vision_encoder.md#MoonViTEncoder "torchtitan/models/kimi_k2_7/vision_encoder.py:L328") and
  [`VisionProjector`](../catalog/torchtitan/models/kimi_k2_7/vision_encoder.md#VisionProjector);
  registry [`model_registry`](../catalog/torchtitan/models/kimi_k2_7/__init__.md#model_registry "torchtitan/models/kimi_k2_7/__init__.py:L506").
- Recipes (named for K2.5): [`kimi_k2_5_debugmodel`](../catalog/torchtitan/models/kimi_k2_7/config_registry.md#kimi_k2_5_debugmodel "torchtitan/models/kimi_k2_7/config_registry.py:L91"),
  [`moonlight_16b_a3b`](../catalog/torchtitan/models/kimi_k2_7/config_registry.md#moonlight_16b_a3b "torchtitan/models/kimi_k2_7/config_registry.py:L133"),
  [`kimi_vl_a3b`](../catalog/torchtitan/models/kimi_k2_7/config_registry.md#kimi_vl_a3b "torchtitan/models/kimi_k2_7/config_registry.py:L176"),
  [`kimi_k2_5`](../catalog/torchtitan/models/kimi_k2_7/config_registry.md#kimi_k2_5 "torchtitan/models/kimi_k2_7/config_registry.py:L222").
- QK clipping: [`QKClipFlexInnerAttention`](../catalog/torchtitan/models/kimi_k2_7/qk_clip.md#QKClipFlexInnerAttention)
  records per-head max attention logits
  ([`max_attention_logits_H`](../catalog/torchtitan/models/kimi_k2_7/qk_clip.md#QKClipFlexInnerAttention.max_attention_logits_H));
  [`qk_clip`](../catalog/torchtitan/models/kimi_k2_7/qk_clip.md#qk_clip) rescales Q/K projection
  weights after each optimizer step, installed by
  [`register_qk_clip_hook`](../catalog/torchtitan/models/kimi_k2_7/qk_clip.md#register_qk_clip_hook).
- Optimizer: [`_dist_muon_optimizer`](../catalog/torchtitan/models/kimi_k2_7/config_registry.md#_dist_muon_optimizer "torchtitan/models/kimi_k2_7/config_registry.py:L294")
  over FlexShard (see [flexshard-optimizer-compute-layouts](flexshard-optimizer-compute-layouts.md)).
- Parallelism: [`parallelize_kimi_k2_5`](../catalog/torchtitan/models/kimi_k2_7/parallelize.md#parallelize_kimi_k2_5 "torchtitan/models/kimi_k2_7/parallelize.py:L36"),
  [`set_kimi_k2_5_sharding_config`](../catalog/torchtitan/models/kimi_k2_7/sharding.md#set_kimi_k2_5_sharding_config "torchtitan/models/kimi_k2_7/sharding.py:L52").
- HF adapter: [`KimiK25StateDictAdapter`](../catalog/torchtitan/models/kimi_k2_7/state_dict_adapter.md#KimiK25StateDictAdapter).

## Why it matters / when it applies
- **QK clipping is an extra post-step pass:** per-head maxima are reduced across DP and CP ranks
  every step, then Q/K weights are clipped (`threshold=100.0`, `alpha=0.5`, hard-coded in `qk_clip`).
  It needs an attention variant that exposes the logit max, which ties these recipes to the Flex
  inner attention.
- **Parallelism:**
  - FSDP/HSDP: decoder sharded per layer; without PP the vision encoder is its own FSDP unit, with PP
    it joins the first stage's root unit.
  - TP: supported by the model, but DistMuon recipes reject TP-produced `_StridedShard` layouts.
  - EP: DistMuon keeps EP-axis `Shard(0)` storage and redistributes the EFSDP-axis storage from
    `Shard(1)` to compute `Shard(0)` ordered after EP when `efsdp_size * ep_size > num_experts`.
  - PP: vision encoder folded into stage 0; 1F1B and Interleaved1F1B. DistMuon requires every stage
    to own >= 1 transformer layer (a stage with only norm + LM head has an empty Muon group and the
    optimizer build fails with "matched no parameters").
  - CP: not supported (code raises `NotImplementedError`).
- **Numerics:** Kimi-VL HF comparison (fp32, text+image): vision cosine 0.999977; last-token KL
  4.3e-2 normally, 5.3e-4 with routing pinned to HF's choices (a diagnostic, not a parity claim).
  Parallelism: bit-identical logits for none/FSDP/FSDP+EP, within bf16 tolerance for FSDP+EP+TP+SP.
- **Checkpoints:** released K2.5/K2.6/K2.7-Code 1T checkpoints are INT4 group-quantized; the
  inherited adapter only handles FP8 block-scale, so the 1T config trains from scratch but cannot
  load them yet. Video training pipeline is a TODO.
- No TPU-lane recipe for this family at this commit.

## Connections
- Code concepts: [kimi-k2-7-model](../concepts/kimi-k2-7-model.md),
  [deepseek-v3-model](../concepts/deepseek-v3-model.md),
  [flex-shard](../concepts/flex-shard.md),
  [optimizers-and-lr-schedulers](../concepts/optimizers-and-lr-schedulers.md).
- Module catalogs: [torchtitan/models/kimi_k2_7/qk_clip](../catalog/torchtitan/models/kimi_k2_7/qk_clip.md),
  [torchtitan/models/kimi_k2_7/config_registry](../catalog/torchtitan/models/kimi_k2_7/config_registry.md),
  [torchtitan/models/kimi_k2_7/parallelize](../catalog/torchtitan/models/kimi_k2_7/parallelize.md),
  [torchtitan/models/kimi_k2_7/vision_encoder](../catalog/torchtitan/models/kimi_k2_7/vision_encoder.md).
- Related doc-concepts: [flexshard-optimizer-compute-layouts](flexshard-optimizer-compute-layouts.md),
  [model-support-overview](model-support-overview.md),
  [moe-sharding-placements](moe-sharding-placements.md).

## Source
Extracted from `torchtitan/models/kimi_k2_7/README.md` (kept in place).
