---
title: Context parallelism - prefill (PCP) and decode (DCP)
type: doc-concept
provenance: doc
source: docs/user_guide/parallelism.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Context parallelism - prefill (PCP) and decode (DCP)

## Definition
For long-context workloads (32K-256K+ tokens) and P/D disaggregation the guide offers
two context-parallel axes. **Prefill context parallelism** (`--prefill-context-parallel-size`)
distributes a prefill's sequence chunks across PCP ranks (ring attention) to cut TTFT;
with `TPU_PCP_TOPOLOGY_AWARE_MESH=1` (default) consecutive PCP ranks sit on adjacent ICI
torus neighbors to minimize hop count. **Decode context parallelism**
(`--decode-context-parallel-size`) shards KV-cache pages along sequence across DCP ranks
and merges partial attention with an online log-sum-exp (LSE) merge
(`TPU_DCP_LSE_MERGE_A2A` switches small steps to an all-to-all merge).

## In vllm-torchtpu (grounded)
- PCP rank ordering: [`resolve_pcp_topology_order`](../catalog/src/vllm_torchtpu/distributed/pcp_rank_order.md#resolve_pcp_topology_order)
  (reads [`TPU_PCP_TOPOLOGY_AWARE_MESH`](../catalog/src/vllm_torchtpu/envs.md#TPU_PCP_TOPOLOGY_AWARE_MESH)),
  [`pcp_topology_order`](../catalog/src/vllm_torchtpu/distributed/pcp_rank_order.md#pcp_topology_order),
  [`verify_pcp_topology_order`](../catalog/src/vllm_torchtpu/distributed/pcp_rank_order.md#verify_pcp_topology_order).
- PCP constraints: [`PcpStaticSupportValidator.validate_platform_config`](../catalog/src/vllm_torchtpu/platforms/pcp_validation.md#PcpStaticSupportValidator.validate_platform_config)
  requires `--enable-expert-parallel` on MoE models, rejects DCP > 1 in the same
  engine, limits speculative decoding to MTP with `num_speculative_tokens=1`, and needs
  `cp_kv_cache_interleave_size > 0` (a multiple of 128 with the HND KV layout).
- DCP merge: [`forward_with_dcp`](../catalog/src/vllm_torchtpu/layers/adapter/cp_attention.md#forward_with_dcp)
  / [`merge_attn_results`](../catalog/src/vllm_torchtpu/layers/adapter/cp_attention.md#merge_attn_results)
  for GQA; for MLA, [`merge_lse_partials_scatter_heads`](../catalog/src/vllm_torchtpu/layers/adapter/cp_mla_attention.md#merge_lse_partials_scatter_heads)
  uses the all-to-all path ([`merge_lse_partials_all_to_all`](../catalog/src/vllm_torchtpu/layers/adapter/cp_mla_attention.md#merge_lse_partials_all_to_all))
  when [`TPU_DCP_LSE_MERGE_A2A`](../catalog/src/vllm_torchtpu/envs.md#TPU_DCP_LSE_MERGE_A2A)
  is on and the step is at most
  [`TPU_DCP_LSE_MERGE_A2A_MAX_TOKENS`](../catalog/src/vllm_torchtpu/envs.md#TPU_DCP_LSE_MERGE_A2A_MAX_TOKENS)
  (64) tokens, else reduce-scatter; only the backbone graph chooses by size (the choice
  is baked in at trace time per bucket group; the MTP drafter always reduce-scatters). Sparse MLA under DCP can cap per-rank top-k
  ([`TPU_DCP_MLA_TOPK_CAP`](../catalog/src/vllm_torchtpu/envs.md#TPU_DCP_MLA_TOPK_CAP),
  [`sparse_mla_attention_dcp`](../catalog/src/vllm_torchtpu/layers/core/attention_interface.md#sparse_mla_attention_dcp)).
- The PCP prefill attention kernel is the experimental streaming RPA
  ([pcp-streaming-rpa-kernel](../concepts/pcp-streaming-rpa-kernel.md)); hybrid GDN models
  have a PCP-fused GDN kernel ([gdn-pcp-fused-kernel](../concepts/gdn-pcp-fused-kernel.md)).

## Why it matters / when it applies
- PCP is a TTFT lever for long prompts; it is typically used on the prefill pool of a
  disaggregated deployment (the guide's `TP=2, PCP=4` example; the disagg guide reshards
  PCP prefill KV into DP/TP decode). DCP is the decode-side lever when one rank's HBM
  cannot hold a long sequence's KV.
- Because PCP and DCP cannot be combined in one engine at this commit, "PCP + DCP"
  configurations in the docs are P/D pairs (PCP on prefill, DCP on decode).
- Under PCP, compile sizes count rows on one rank (rank 0 holds the most), which affects
  the token-budget check in [token-padding-buckets](token-padding-buckets.md).

## Connections
- Code concepts: [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md), [pcp-streaming-rpa-kernel](../concepts/pcp-streaming-rpa-kernel.md), [gdn-pcp-fused-kernel](../concepts/gdn-pcp-fused-kernel.md), [mla-attention-kernels](../concepts/mla-attention-kernels.md), [attention-and-layer-core](../concepts/attention-and-layer-core.md)
- Module catalogs: [pcp_rank_order](../catalog/src/vllm_torchtpu/distributed/pcp_rank_order.md), [pcp_validation](../catalog/src/vllm_torchtpu/platforms/pcp_validation.md), [cp_attention](../catalog/src/vllm_torchtpu/layers/adapter/cp_attention.md), [cp_mla_attention](../catalog/src/vllm_torchtpu/layers/adapter/cp_mla_attention.md)
- Related doc-concepts: [composable-6d-parallelism](composable-6d-parallelism.md), [raiden-pd-disaggregation](raiden-pd-disaggregation.md), [pipeline-parallel-stage-handoff](pipeline-parallel-stage-handoff.md)

## Source
Extracted from `docs/user_guide/parallelism.md` (section 5, kept in place).
