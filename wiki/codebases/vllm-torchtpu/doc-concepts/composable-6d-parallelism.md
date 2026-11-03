---
title: Composable 6D parallelism (TP, DP, PP, EP, PCP, DCP) and logical device count
type: doc-concept
provenance: doc
source: docs/user_guide/parallelism.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Composable 6D parallelism (TP, DP, PP, EP, PCP, DCP) and logical device count

## Definition
The parallelism guide presents six composable axes, all driven by standard vLLM flags:
tensor (`--tensor-parallel-size`), data (`--data-parallel-size`), pipeline
(`--pipeline-parallel-size`), expert (`--enable-expert-parallel`, sharding routed
experts over the `TP * DP` mesh), prefill context (`--prefill-context-parallel-size`,
splitting long prefills) and decode context (`--decode-context-parallel-size`,
sharding the KV cache along sequence). An engine group consumes `DP * TP * PP * PCP`
**logical** devices, and on TPU v7x each physical chip exposes **two** logical
TensorCore devices, so a 4-chip v7x host offers 8 (e.g. `TP=8`, `DP=8,TP=1`,
`DP=4,TP=2`).

## In vllm-torchtpu (grounded)
| Axis | Collective behavior (doc) | Where it lives in code |
|---|---|---|
| TP | all-reduce / reduce-scatter per layer | vLLM groups; MoE sequence-parallel variant via [`_configure_sequence_parallel_moe`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#_configure_sequence_parallel_moe) |
| DP | no attention collective at TP=1; MoE all-to-all over `TP * DP` with EP | [`TpuDpScheduler`](../catalog/src/vllm_torchtpu/core/tpu_scheduler.md#TpuDpScheduler) (opt-in `DP_SCHED_ENABLED`) |
| EP | Pallas SparseCore / GMM ragged dispatch + combine | [`build_ep_mesh`](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md#build_ep_mesh), [`get_ep_group`](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md#get_ep_group), [`ep_rank_order`](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md#ep_rank_order) |
| PP | point-to-point activation hand-off, dynamic microbatch chunks | [`ring_handoff`](../catalog/src/vllm_torchtpu/distributed/pp_push.md#ring_handoff), [`patch_executor_for_pp_handoff`](../catalog/src/vllm_torchtpu/distributed/pp_push.md#patch_executor_for_pp_handoff), [`validate_pipeline_parallel_config`](../catalog/src/vllm_torchtpu/platforms/pp_validation.md#validate_pipeline_parallel_config) |
| PCP | topology-aware ring over adjacent ICI neighbors | [`resolve_pcp_topology_order`](../catalog/src/vllm_torchtpu/distributed/pcp_rank_order.md#resolve_pcp_topology_order), [`PcpStaticSupportValidator`](../catalog/src/vllm_torchtpu/platforms/pcp_validation.md#PcpStaticSupportValidator) |
| DCP | online LSE merge across ranks | [`forward_with_dcp`](../catalog/src/vllm_torchtpu/layers/adapter/cp_attention.md#forward_with_dcp), [`merge_attn_results`](../catalog/src/vllm_torchtpu/layers/adapter/cp_attention.md#merge_attn_results), [`merge_lse_partials_scatter_heads`](../catalog/src/vllm_torchtpu/layers/adapter/cp_mla_attention.md#merge_lse_partials_scatter_heads) |

The two-cores-per-chip fact is modelled by [`ChipTopology`](../catalog/src/vllm_torchtpu/distributed/chip_topology.md#ChipTopology)
([`get_chip_topology`](../catalog/src/vllm_torchtpu/distributed/chip_topology.md#get_chip_topology)),
which the intra-chip knobs (`TPU_MOE_HIERARCHICAL_EP`, `TPU_LATENT_PROJ_INTRA_CHIP_TP`)
build on.

## Why it matters / when it applies
- Choosing the axis mix is the first-order throughput decision for large models: the
  guide's main recommendation (DP + EP over wide TP for MoE) is detailed in
  [dp-ep-moe-layouts](dp-ep-moe-layouts.md).
- Count logical devices, not chips, on v7x; `TP=2` maps naturally onto the two cores of
  one chip (cheapest collective domain).
- Some combinations are rejected at startup at this commit (see
  [context-parallelism-pcp-dcp](context-parallelism-pcp-dcp.md) and
  [pipeline-parallel-stage-handoff](pipeline-parallel-stage-handoff.md)); crossing
  hosts needs [multihost-execution-backends](multihost-execution-backends.md).

## Connections
- Code concepts: [distributed-parallelism-and-meshes](../concepts/distributed-parallelism-and-meshes.md), [tpu-schedulers](../concepts/tpu-schedulers.md), [fused-moe-kernels](../concepts/fused-moe-kernels.md), [pcp-streaming-rpa-kernel](../concepts/pcp-streaming-rpa-kernel.md)
- Module catalogs: [ep_mesh](../catalog/src/vllm_torchtpu/distributed/ep_mesh.md), [chip_topology](../catalog/src/vllm_torchtpu/distributed/chip_topology.md), [pp_push](../catalog/src/vllm_torchtpu/distributed/pp_push.md), [pcp_rank_order](../catalog/src/vllm_torchtpu/distributed/pcp_rank_order.md), [cp_attention](../catalog/src/vllm_torchtpu/layers/adapter/cp_attention.md)
- Related doc-concepts: [dp-ep-moe-layouts](dp-ep-moe-layouts.md), [pipeline-parallel-stage-handoff](pipeline-parallel-stage-handoff.md), [context-parallelism-pcp-dcp](context-parallelism-pcp-dcp.md), [multihost-execution-backends](multihost-execution-backends.md), [raiden-pd-disaggregation](raiden-pd-disaggregation.md)

## Source
Extracted from `docs/user_guide/parallelism.md` (section 1, kept in place).
