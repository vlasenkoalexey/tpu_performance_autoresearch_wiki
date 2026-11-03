---
title: Q4 2026 roadmap mapped to the code at this commit
type: doc-concept
provenance: doc
source: docs/roadmap.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Q4 2026 roadmap mapped to the code at this commit

## Definition
The public roadmap (last updated 2026-10-19) lists vllm-torchtpu milestones by target
month for October-December 2026. It frames the project as sharing the `torch_tpu`
runtime, the Tokamax kernel library and the TPU recipes with a sibling
`sglang-torchtpu`, so platform milestones benefit both. Dates are planning targets, not
commitments. This page lists the performance-relevant milestones and what already exists
for each in the tree at `bf318e424` (2026-11-02), so a reader can tell shipped
machinery from plans.

## In vllm-torchtpu (grounded)
| Milestone (target) | Perf-relevant claim | State in code at this commit |
|---|---|---|
| Co-maintainership with an external partner (Oct) | custom megakernels, price-performance on InferenceX / AgentX | Megakernel framework present: [`ModelSpec`](../catalog/src/vllm_torchtpu/megakernel/spec.md#ModelSpec), [`Plan`](../catalog/src/vllm_torchtpu/megakernel/planner.md#Plan), [`Module`](../catalog/src/vllm_torchtpu/megakernel/module.md#Module); see [megakernel](../concepts/megakernel.md), [megakernel-pool](../concepts/megakernel-pool.md). |
| Qwen 3.5 397B and Gemma 4 recipes (Oct) | v7x FP8 W8A8 inference recipes | Both families are CI/Nightly-validated with FP8 weights + KV (see [supported-models-and-feature-matrix](supported-models-and-feature-matrix.md)); recipes themselves live in an external recipes repo. |
| Ray integration (Oct) | native Ray orchestration | Ray multi-host backend exists ([`RayDistributedExecutorV2`](../catalog/src/vllm_torchtpu/executors/ray_distributed_executor_v2.md#RayDistributedExecutorV2), `TPU_MULTIHOST_BACKEND=ray`); see [multihost-execution-backends](multihost-execution-backends.md). |
| 100% Tokamax PyTorch interfaces (Oct) | one shared kernel integration layer | No Tokamax import anywhere under `src/` at this commit; kernels are in-tree Pallas (see [tpu-kernel-library-map](tpu-kernel-library-map.md)). |
| Multi-host disaggregation xP-yD with llm-d (Oct) | low-latency multi-host P/D | Raiden P/D with heterogeneous resharding and multi-host launchers exists ([`TPURaidenConnector`](../catalog/src/vllm_torchtpu/distributed/kv_transfer/tpu_connector.md#TPURaidenConnector)); see [raiden-pd-disaggregation](raiden-pd-disaggregation.md). |
| TPU-Sync and Lustre KV-cache offloading (Oct) | host RAM + managed Lustre tiers, 128K -> 1M+ context | Host offload via [`TPURaidenOffloadingConnector`](../catalog/src/vllm_torchtpu/offload/raiden_connector.md#TPURaidenOffloadingConnector) and the store tier [`RaidenOffloadingManager`](../catalog/src/vllm_torchtpu/offload/raiden_store.md#RaidenOffloadingManager); the storage backend knob [`RAIDEN_STORAGE_TYPE`](../catalog/src/vllm_torchtpu/envs.md#RAIDEN_STORAGE_TYPE) documents `posix` as the only type today (a POSIX mount, so a Lustre mount would go through it; no Lustre-specific code). See [host-offload](../concepts/host-offload.md). |
| Speculative decoding incl. MTP, agentic traces (Nov) | multi-host spec decode benchmarks | EAGLE-3, MTP (with fused draft loop), DFlash, DSpark, n-gram implemented; see [speculative-decoding-methods](speculative-decoding-methods.md). |
| Native diffusion serving via vllm-omni (Nov) | Wan 2.2 etc. | Omni platform present ([`OmniTpuPlatform`](../catalog/src/vllm_torchtpu/omni/platform.md#OmniTpuPlatform)); see [omni-diffusion-support](../concepts/omni-diffusion-support.md). |
| Public nightly CI support matrix (Nov) | model status, BF16/FP8/MXFP4, eval scores | `support_matrices/nightly/` is referenced from the README. |
| Qwen 3.5, Kimi K3, GLM 5.2/5.3 benchmarks (Nov) | hill-climbing, 1M context | Dedicated Kimi-K3 implementation and GLM MLA dispatch profile exist ([kimi-k3-model](../concepts/kimi-k3-model.md), [mla-attention-kernels](../concepts/mla-attention-kernels.md)). |
| DeepSeek V4 readiness (Dec) | Day-0 support, kernel perf | Dedicated V4 model, sparse MLA, StreamIndex top-k, compress-and-store kernels and `deepseek_v4_fp8` already in tree ([deepseek-v4-model](../concepts/deepseek-v4-model.md)); V4 checkpoints are Nightly-validated. |
| Smart caching, routing and memory tiers (Dec) | prefix/cache/session-aware routing, dynamic length bucketing | A prefix-aware admission scheduler exists but is not installed by default ([`PrefixAwareScheduler`](../catalog/src/vllm_torchtpu/core/prefix_aware_scheduler.md#PrefixAwareScheduler)); static token buckets plus optional linear buckets today ([token-padding-buckets](token-padding-buckets.md)). |

## Why it matters / when it applies
- Several "upcoming" items (DeepSeek-V4, MTP, multi-host P/D, megakernel) already have
  substantial code, so roadmap dates understate what can be measured now; others
  (Tokamax interfaces, dynamic length bucketing, Lustre-specific offload) have no code
  at this commit and should not be assumed when planning experiments.
- The roadmap is a dated snapshot; re-check against the tree before relying on it.

## Connections
- Code concepts: [megakernel](../concepts/megakernel.md), [host-offload](../concepts/host-offload.md), [kv-transfer-and-disaggregated-serving](../concepts/kv-transfer-and-disaggregated-serving.md), [speculative-decoding](../concepts/speculative-decoding.md), [omni-diffusion-support](../concepts/omni-diffusion-support.md), [deepseek-v4-model](../concepts/deepseek-v4-model.md)
- Module catalogs: [megakernel/spec](../catalog/src/vllm_torchtpu/megakernel/spec.md), [offload/raiden_store](../catalog/src/vllm_torchtpu/offload/raiden_store.md), [omni/platform](../catalog/src/vllm_torchtpu/omni/platform.md)
- Related doc-concepts: [supported-models-and-feature-matrix](supported-models-and-feature-matrix.md), [tpu-kernel-library-map](tpu-kernel-library-map.md), [raiden-pd-disaggregation](raiden-pd-disaggregation.md)

## Source
Extracted from `docs/roadmap.md` (kept in place).
