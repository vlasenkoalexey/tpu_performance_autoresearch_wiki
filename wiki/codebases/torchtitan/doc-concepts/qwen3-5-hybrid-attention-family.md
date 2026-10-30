---
title: Qwen3.5 / 3.6 / 3.8 family (hybrid GatedDeltaNet + full attention, vision scatter)
type: doc-concept
provenance: doc
source: torchtitan/models/qwen3_5/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Qwen3.5 / 3.6 / 3.8 family (hybrid GatedDeltaNet + full attention, vision scatter)

## Definition
Qwen3.5 is a multimodal model with a **hybrid decoder**: about 75% of layers are GatedDeltaNet
(linear attention with a recurrent state) and 25% are full attention with output gating and partial
RoPE, plus a ViT vision encoder (2D RoPE, interpolated learned position embeddings), a patch merger
(`merge_size^2` patches -> 1 token), interleaved MRoPE in decoder layers, and an MoE variant with
routed experts plus a sigmoid-gated shared expert. Qwen3.6 and Qwen3.8 are thin version packages
that reuse the Qwen3.5 implementation and own only their registry, recipes, and HF asset paths.

## In torchtitan (grounded)
- Implementation (`torchtitan/models/qwen3_5/`): [`Qwen35Model`](../catalog/torchtitan/models/qwen3_5/model.md#Qwen35Model "torchtitan/models/qwen3_5/model.py:L248"),
  [`GatedDeltaNet`](../catalog/torchtitan/models/qwen3_5/gdn.md#GatedDeltaNet),
  [`Qwen35Attention`](../catalog/torchtitan/models/qwen3_5/model.md#Qwen35Attention),
  [`OffsetRMSNorm`](../catalog/torchtitan/models/qwen3_5/model.md#OffsetRMSNorm "torchtitan/models/qwen3_5/model.py:L62"),
  [`MRoPE`](../catalog/torchtitan/models/qwen3_5/rope.md#MRoPE "torchtitan/models/qwen3_5/rope.py:L15"),
  [`Qwen35VisionEncoder`](../catalog/torchtitan/models/qwen3_5/vision_encoder.md#Qwen35VisionEncoder),
  [`PatchMerger`](../catalog/torchtitan/models/qwen3_5/vision_encoder.md#PatchMerger).
- Parallelism: [`parallelize_qwen3_5`](../catalog/torchtitan/models/qwen3_5/parallelize.md#parallelize_qwen3_5 "torchtitan/models/qwen3_5/parallelize.py:L34"),
  [`set_qwen35_sharding_config`](../catalog/torchtitan/models/qwen3_5/sharding.md#set_qwen35_sharding_config "torchtitan/models/qwen3_5/sharding.py:L115")
  (GatedDeltaNet projections head-sharded under TP, see
  [`_set_deltanet_sharding`](../catalog/torchtitan/models/qwen3_5/sharding.md#_set_deltanet_sharding "torchtitan/models/qwen3_5/sharding.py:L303")).
- Registries: [`qwen3_5 model_registry`](../catalog/torchtitan/models/qwen3_5/__init__.md#model_registry "torchtitan/models/qwen3_5/__init__.py:L1096"),
  [`qwen3_6 model_registry`](../catalog/torchtitan/models/qwen3_6/__init__.md#model_registry),
  [`qwen3_8 model_registry`](../catalog/torchtitan/models/qwen3_8/__init__.md#model_registry); recipes
  such as [`qwen35_27b`](../catalog/torchtitan/models/qwen3_5/config_registry.md#qwen35_27b "torchtitan/models/qwen3_5/config_registry.py:L275"),
  [`qwen36_27b`](../catalog/torchtitan/models/qwen3_6/config_registry.md#qwen36_27b "torchtitan/models/qwen3_6/config_registry.py:L129"),
  [`qwen38_27b`](../catalog/torchtitan/models/qwen3_8/config_registry.md#qwen38_27b "torchtitan/models/qwen3_8/config_registry.py:L142"),
  [`qwen38_2_4t_a95b`](../catalog/torchtitan/models/qwen3_8/config_registry.md#qwen38_2_4t_a95b).
- Optional fused-norm override: [`triton_offset_rmsnorm`](../catalog/torchtitan/overrides/offset_rmsnorm.md#triton_offset_rmsnorm "torchtitan/overrides/offset_rmsnorm.py:L343") (GPU).
- **TPU lane** (`torchtitan/experiments/tpu/qwen3_5/`): upstream GatedDeltaNet uses CUDA/Triton
  kernels for the gated delta rule and varlen causal conv1d; the TPU replacements are
  [`chunked_gated_delta`](../catalog/torchtitan/experiments/tpu/qwen3_5/gated_delta.md#chunked_gated_delta)
  (FLA `chunk_gdn` math as batched matmuls XLA compiles),
  [`TpuGatedDeltaKernel`](../catalog/torchtitan/experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaKernel),
  [`TpuInnerGatedDeltaNet`](../catalog/torchtitan/experiments/tpu/qwen3_5/gated_delta.md#TpuInnerGatedDeltaNet), and
  [`TpuGatedDeltaNet`](../catalog/torchtitan/experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaNet)
  (static-shape `[B, S]` segment-id masks instead of dynamic `cu_seqlens`), with TPU recipes like
  [`qwen35_moe_35b`](../catalog/torchtitan/experiments/tpu/qwen3_5/config_registry.md#qwen35_moe_35b "torchtitan/experiments/tpu/qwen3_5/config_registry.py:L78").

## Why it matters / when it applies
- **Two attention cost models in one stack.** Linear-attention layers scale with sequence length
  linearly but carry a recurrent/chunked kernel; full-attention layers carry the usual quadratic
  kernel. Step-time attribution must split the two; on TPU the GDN chunk size
  ([`chunk_size`](../catalog/torchtitan/experiments/tpu/qwen3_5/gated_delta.md#TpuGatedDeltaKernel.Config.chunk_size),
  default 64) is a tuning knob.
- **Parallelism (README + code):** FSDP/HSDP with the decoder sharded per layer and the vision
  encoder as one unit (a single all-gather); TP with SP, head-sharded on GDN projections; EP for MoE;
  PP with the vision encoder on stage 0 (1F1B, Interleaved1F1B); sample packing opt-in via
  `MMSamplePackingConfig`. **CP is not supported** - `parallelize_qwen3_5` raises.
- **Numerics:** 4B multimodal vs HF KL ~3e-7, 100% top-1/top-5; bit-identical logits across
  none/FSDP/FSDP+EP/FSDP+EP+TP.
- **Variants:** dense 0.8B-27B (head dim 256, ViT 12-27 layers), MoE 35B-A3B / 122B-A10B /
  397B-A17B (256-512 experts, top-8/10, shared expert). Qwen3.6: 27B dense and 35B-A3B MoE, both with
  vision. Qwen3.8: 27B (architecturally identical to Qwen3.5-27B) and a text-only 2.4T-A95B MoE (8192
  dim, 92 layers, 512 experts, top-10) whose weights live under `model.*` instead of
  `model.language_model.*`. Qwen3.8's HF `output_gate_type: "swish"` matches the existing SiLU gate in
  GatedDeltaNet; full-attention output gating stays sigmoid.
- **Checkpoint limits:** released MTP weights are neither imported nor exported (only the primary
  next-token decoder trains); pre-quantized FP8 HF repos are not supported by the adapter - convert
  from non-FP8 checkpoints. Video dataset configs are a TODO.

## Connections
- Code concepts: [qwen3-5-model](../concepts/qwen3-5-model.md), [qwen3-model](../concepts/qwen3-model.md),
  [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md),
  [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md),
  [hf-datasets](../concepts/hf-datasets.md).
- Module catalogs: [torchtitan/models/qwen3_5/gdn](../catalog/torchtitan/models/qwen3_5/gdn.md),
  [torchtitan/models/qwen3_5/model](../catalog/torchtitan/models/qwen3_5/model.md),
  [torchtitan/models/qwen3_5/sharding](../catalog/torchtitan/models/qwen3_5/sharding.md),
  [torchtitan/experiments/tpu/qwen3_5/gated_delta](../catalog/torchtitan/experiments/tpu/qwen3_5/gated_delta.md).
- Related doc-concepts: [model-support-overview](model-support-overview.md),
  [dataset-mixing-and-packing](dataset-mixing-and-packing.md),
  [configurable-overrides](configurable-overrides.md).

## Source
Extracted from `torchtitan/models/qwen3_5/README.md`, `torchtitan/models/qwen3_6/README.md`, and
`torchtitan/models/qwen3_8/README.md` (kept in place).
