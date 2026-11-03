---
title: DP + EP layouts for MoE and the MoE execution knobs
type: doc-concept
provenance: doc
source: docs/user_guide/parallelism.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# DP + EP layouts for MoE and the MoE execution knobs

## Definition
For large MoE models with GQA or MLA attention (Qwen3.5-397B-A17B, DeepSeek-V4,
GLM-5.2), the parallelism guide recommends **data parallel attention + expert parallel
MoE** over pure wide TP: attention stays chip-local (`TP=1` or `TP=2`), avoiding 8- or
16-way all-reduces every layer, while routed experts shard across the whole slice
(`EP = TP * DP`, each device holding `num_experts / (TP * DP)` experts), leaving HBM for
weights and KV. Two reference layouts on one 8-device v7x host: `DP=8, TP=1 + EP`
(max throughput) and `DP=4, TP=2 + EP` (TP across the two cores of a chip, when HBM is
tighter or single-stream concurrency matters). A set of env vars then selects the MoE
execution path.

## In vllm-torchtpu (grounded)
- EP mesh construction: [`build_ep_mesh`](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md#build_ep_mesh),
  [`ep_device_ids`](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md#ep_device_ids),
  [`ep_token_replica_groups`](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md#ep_token_replica_groups).
- SparseCore offload ([`USE_MOE_SPARSE_CORE`](../catalog/src/vllm_torchtpu/envs.md#USE_MOE_SPARSE_CORE), default on)
  and the one-hot vs SparseCore permute switch
  ([`ONEHOT_MOE_PERMUTE_THRESHOLD`](../catalog/src/vllm_torchtpu/envs.md#ONEHOT_MOE_PERMUTE_THRESHOLD),
  resolved by [`resolve_onehot_permute_threshold`](../catalog/src/vllm_torchtpu/layers/core/fused_moe_gmm.md#resolve_onehot_permute_threshold):
  rows = `num_tokens * topk`; unset = auto from SparseCore geometry, `0` = always
  SparseCore). The doc's DP8 example sets it to `32768`, i.e. the one-hot path for every
  step whose routed rows (tokens x top-k) stay <= 32768.
- Fused EP Pallas kernel: [`USE_MOE_FUSED_EP_KERNEL`](../catalog/src/vllm_torchtpu/envs.md#USE_MOE_FUSED_EP_KERNEL)
  / [`MOE_FUSED_EP_KERNEL_IMPL`](../catalog/src/vllm_torchtpu/envs.md#MOE_FUSED_EP_KERNEL_IMPL),
  prebuilt by [`prebuild_fused_moe_ep`](../catalog/src/vllm_torchtpu/layers/adapter/fused_moe_ep.md#prebuild_fused_moe_ep).
  **Doc-vs-code:** the guide says `v1` or `v2`; the code accepts `v2` or `adaptive`
  (see [adaptive-fused-moe-kernel](../concepts/adaptive-fused-moe-kernel.md)), and setting the
  impl alone already turns the fused kernel on.
- Hierarchical EP on dual-core v7x: [`TPU_MOE_HIERARCHICAL_EP`](../catalog/src/vllm_torchtpu/envs.md#TPU_MOE_HIERARCHICAL_EP)
  -> [`hierarchical_split_or_none`](../catalog/src/vllm_torchtpu/layers/adapter/moe_hierarchical.md#hierarchical_split_or_none)
  -> [`hierarchical_moe_split`](../catalog/src/vllm_torchtpu/distributed/chip_topology.md#hierarchical_moe_split);
  falls back to flat EP (with a warning) when the topology cannot be used.
- Sequence-parallel MoE: [`TPU_MOE_SEQUENCE_PARALLEL`](../catalog/src/vllm_torchtpu/envs.md#TPU_MOE_SEQUENCE_PARALLEL)
  replaces the post-attention all-reduce with reduce-scatter + all-gather so the router
  and experts run on `T/tp` tokens ([`_configure_sequence_parallel_moe`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_configure_sequence_parallel_moe));
  the envs.py comment restricts it to Qwen3.5 MoE with EP and TP > 1.
- Intra-chip MLA latent projection TP: [`TPU_LATENT_PROJ_INTRA_CHIP_TP`](../catalog/src/vllm_torchtpu/envs.md#TPU_LATENT_PROJ_INTRA_CHIP_TP)
  -> [`shard_group_or_none`](../catalog/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.md#shard_group_or_none),
  [`IntraChipColumnParallelLinear`](../catalog/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.md#IntraChipColumnParallelLinear).
- Other MoE knobs from the env reference: [`TPU_MOE_ROUTER_TOPK`](../catalog/src/vllm_torchtpu/envs.md#TPU_MOE_ROUTER_TOPK)
  (`rowmax` sort-free top-k vs `sort`), [`TPU_MOE_FP8_ALL_GATHER`](../catalog/src/vllm_torchtpu/envs.md#TPU_MOE_FP8_ALL_GATHER),
  [`TPU_ATTN_MOE_OVERLAP`](../catalog/src/vllm_torchtpu/envs.md#TPU_ATTN_MOE_OVERLAP) (Qwen3.5 only).

## Why it matters / when it applies
- MoE serving throughput on TPU is usually bound by attention all-reduces at wide TP
  and by token permutation; DP + EP removes the former and SparseCore/one-hot/fused EP
  choices target the latter.
- All of these knobs join the compile cache key; sweeping them means cold compiles.
- The guide's recipes pair DP+EP with FP8 weights and FP8 KV (`--kv-cache-dtype fp8`)
  and `--block-size 256`; see [tpu-quantization-formats](tpu-quantization-formats.md).

## Connections
- Code concepts: [fused-moe-kernels](../concepts/fused-moe-kernels.md), [adaptive-fused-moe-kernel](../concepts/adaptive-fused-moe-kernel.md), [sparsecore-ragged-gather-scatter](../concepts/sparsecore-ragged-gather-scatter.md), [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md), [mla-attention-kernels](../concepts/mla-attention-kernels.md), [vllm-layer-adapters](../concepts/vllm-layer-adapters.md)
- Module catalogs: [ep_mesh](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md), [moe_hierarchical](../catalog/src/vllm_torchtpu/layers/adapter/moe_hierarchical.md), [fused_moe_ep](../catalog/src/vllm_torchtpu/layers/adapter/fused_moe_ep.md), [fused_moe_gmm](../catalog/src/vllm_torchtpu/layers/core/fused_moe_gmm.md), [latent_proj_intra_chip](../catalog/src/vllm_torchtpu/layers/adapter/latent_proj_intra_chip.md)
- Related doc-concepts: [composable-6d-parallelism](composable-6d-parallelism.md), [load-time-requantization](load-time-requantization.md), [env-var-reference-by-subsystem](env-var-reference-by-subsystem.md), [token-padding-buckets](token-padding-buckets.md)

## Source
Extracted from `docs/user_guide/parallelism.md` (sections 2-3, kept in place).
