---
title: Supported models, validation levels and the feature matrix
type: doc-concept
provenance: doc
source: docs/user_guide/supported_models.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Supported models, validation levels and the feature matrix

## Definition
The supported-models page is the project's statement of what works **today**, in two
tables keyed by a four-level evidence scale: **CI** (every PR, perf/accuracy or
integration on v7x), **Nightly**, **Tests** (unit/kernel/component only, no end-to-end
serving in CI) and **Example** (a script/config/recipe exists, not scheduled). The model
table lists, per family, the validated checkpoints and the *architecture-specific TPU
support* each needs; the feature table lists how each serving feature is enabled and
which models validate it. A model missing from a feature row means "not run in CI", not
"unsupported".

## In vllm-torchtpu (grounded)
Model families and the TPU-specific machinery they rely on:

| Family | TPU-specific support (doc) | Code |
|---|---|---|
| Qwen3.5 (hybrid GDN + full attention, MoE, MTP) | GDN chunked-prefill / recurrent-decode kernels; unified block pool for GDN state + KV; native MTP | [gated-deltanet-kernels](../concepts/gated-deltanet-kernels.md), [`unified_kv_layout_enabled_for_architecture`](../catalog/src/vllm_torchtpu/gdn_pool_layout.md#unified_kv_layout_enabled_for_architecture), [`MtpDraftModel`](../catalog/src/vllm_torchtpu/spec_decode/mtp_fused_loop.md#MtpDraftModel), [`maybe_patch_qwen3_5_attn_moe_overlap`](../catalog/src/vllm_torchtpu/models/vllm/qwen3_5_patch.md#maybe_patch_qwen3_5_attn_moe_overlap) |
| Kimi-Linear (KDA + MLA) | KDA kernels (fused conv1d + delta rule), pooled KDA state | [kimi-k3-kernels](../concepts/kimi-k3-kernels.md) |
| Qwen3 / Qwen3-Coder (dense, MoE) | reference path: RPA v3, fused EP MoE (GMM / SparseCore), FP8 and NVFP4 | [ragged-paged-attention-kernel](../concepts/ragged-paged-attention-kernel.md), [fused-moe-kernels](../concepts/fused-moe-kernels.md) |
| DeepSeek-V2 / V4 (MLA, sparse attention, MoE) | dedicated V4 implementation; sparse MLA with SparseCore top-k and `sparsecore`/TensorCore KV layouts; `deepseek_v4_fp8` FP8 + W4A8 MoE; DSpark | [deepseek-v4-model](../concepts/deepseek-v4-model.md), [deepseek-v4-streamindex-topk-kernel](../concepts/deepseek-v4-streamindex-topk-kernel.md), [`VllmDeepseekV4Fp8Config`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/deepseek_v4_fp8.md#VllmDeepseekV4Fp8Config), [`DSparkProposer`](../catalog/src/vllm_torchtpu/spec_decode/dspark.md#DSparkProposer) |
| Kimi-K2.6 / K3 (MLA; K3 adds KDA + MoonViT) | dedicated K3 implementation; W4A16 K2.6; DSpark | [kimi-k3-model](../concepts/kimi-k3-model.md), [`VllmCompressedTensorsW4A16MoEMethod`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.md#VllmCompressedTensorsW4A16MoEMethod) |
| GLM-5.2 (MLA, MoE) | calibrated MLA dispatch profile; NVFP4 MoE with host KV offload | [mla-attention-kernels](../concepts/mla-attention-kernels.md), [host-offload](../concepts/host-offload.md) |
| Gemma 4 (dense + MoE, multimodal, sliding-window hybrid) | sliding-window / global page sizing | [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md) |
| Llama 3.x | reference dense path; EAGLE-3 | [`Eagle3Proposer`](../catalog/src/vllm_torchtpu/spec_decode/eagle3.md#Eagle3Proposer) |
| Qwen2.5-VL / Qwen3-VL | 3D M-RoPE, encoder attention patches, video frame chunking | [`maybe_patch_qwen3_vl`](../catalog/src/vllm_torchtpu/models/vllm/qwen3_vl_patch.md#maybe_patch_qwen3_vl), [`get_video_chunk_patch_size`](../catalog/src/vllm_torchtpu/runner/mm_video_chunking.md#get_video_chunk_patch_size) |
| Embedding / safety classifiers | on-device pooling with request bucketing and static compilation | [`VLLM_TPU_STATIC_POOLER`](../catalog/src/vllm_torchtpu/envs.md#VLLM_TPU_STATIC_POOLER), [`TPUModelRunner._resolve_static_pooler`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner._resolve_static_pooler) |

Feature rows with TPU-specific enablement (all other rows are stock vLLM flags):
the prefix-caching row names [`PrefixAwareScheduler`](../catalog/src/vllm_torchtpu/core/prefix_aware_scheduler.md#PrefixAwareScheduler)
(admits ready requests with the fewest uncached prompt tokens within a 64-request window);
chunked prefill / async scheduling are tuned by the bucket knobs and
[`DP_SCHED_ENABLED`](../catalog/src/vllm_torchtpu/envs.md#DP_SCHED_ENABLED);
KV offloading uses [`TPURaidenOffloadingConnector`](../catalog/src/vllm_torchtpu/offload/raiden_connector.md#TPURaidenOffloadingConnector)
(`kv_connector_module_path: vllm_torchtpu.offload.raiden_connector`, which matches the
code); under `TPU_MOE_HIERARCHICAL_EP`, `--enable-ep-weight-filter` is taught chip-block
expert ownership by [`align_ep_weight_filter`](../catalog/src/vllm_torchtpu/layers/adapter/moe_hierarchical.md#align_ep_weight_filter).

## Doc-vs-code disagreements
- Compilation-cache row lists `VLLM_XLA_CACHE_PATH`, which no plugin code reads (see
  [compilation-cache-and-warmup](compilation-cache-and-warmup.md)).
- Disaggregated-serving row names `TpuRaidenConnector`; the class is
  `TPURaidenConnector` (see [raiden-pd-disaggregation](raiden-pd-disaggregation.md)).
- Speculative-decoding row lists `suffix`, which the runner rejects
  (see [speculative-decoding-methods](speculative-decoding-methods.md)); conversely it
  correctly lists `dspark`, which the speculative-decoding guide omits.
- Quantization row lists `awq`, `gptq`, `online_fp8` as `--quantization` values; see
  [tpu-quantization-formats](tpu-quantization-formats.md) for why those fail.
- `PrefixAwareScheduler` is presented as part of `--enable-prefix-caching`, but nothing
  under `src/` installs it at this commit (only tests reference it); it must be selected
  explicitly as the scheduler class.
- The sparse MLA layout values are `sparsecore` / `tensorcore` (the page says `tc`).

## Why it matters / when it applies
- The validation level is the evidence bar for a perf baseline: only CI/Nightly rows on
  v7x have regression-gated numbers (the exact topologies and flags are in the v7x
  recipes, see [v7x-serving-recipe-matrix](v7x-serving-recipe-matrix.md)); Tests/Example
  rows need a self-established baseline.
- The architecture column tells you which kernel family dominates a model's step time
  and therefore which env vars and deep pages matter (see
  [tpu-kernel-library-map](tpu-kernel-library-map.md)).

## Connections
- Code concepts: [vllm-model-patches](../concepts/vllm-model-patches.md), [deepseek-v4-model](../concepts/deepseek-v4-model.md), [kimi-k3-model](../concepts/kimi-k3-model.md), [gated-deltanet-kernels](../concepts/gated-deltanet-kernels.md), [mla-attention-kernels](../concepts/mla-attention-kernels.md), [speculative-decoding](../concepts/speculative-decoding.md), [host-offload](../concepts/host-offload.md), [omni-diffusion-support](../concepts/omni-diffusion-support.md), [tpu-schedulers](../concepts/tpu-schedulers.md)
- Module catalogs: [models/vllm/qwen3_5_patch](../catalog/src/vllm_torchtpu/models/vllm/qwen3_5_patch.md), [prefix_aware_scheduler](../catalog/src/vllm_torchtpu/core/prefix_aware_scheduler.md), [offload/raiden_connector](../catalog/src/vllm_torchtpu/offload/raiden_connector.md), [gdn_pool_layout](../catalog/src/vllm_torchtpu/gdn_pool_layout.md)
- Related doc-concepts: [tpu-kernel-library-map](tpu-kernel-library-map.md), [tpu-quantization-formats](tpu-quantization-formats.md), [speculative-decoding-methods](speculative-decoding-methods.md), [raiden-pd-disaggregation](raiden-pd-disaggregation.md), [v7x-serving-recipe-matrix](v7x-serving-recipe-matrix.md), [multimodal-encoder-inference](multimodal-encoder-inference.md), [multi-lora-inference](multi-lora-inference.md)

## Source
Extracted from `docs/user_guide/supported_models.md` (kept in place).
