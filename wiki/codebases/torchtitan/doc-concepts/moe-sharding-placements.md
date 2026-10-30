---
title: MoE sharding placements (EP on/off x SP on/off)
type: doc-concept
provenance: doc
source: torchtitan/models/common/MOE_SHARDING.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# MoE sharding placements (EP on/off x SP on/off)

## Definition
MoE layers are sharded through the same declarative config mechanism as dense layers. The MoE
wrapper redistributes its input from the sequence-parallel layout to the layout the experts need,
the router is replicated, shared experts follow the dense TP plan, and routed experts run their
dispatch/compute/combine on **local tensors** inside a `local_map` boundary. Which mesh the routed
expert weights live on depends on whether expert parallelism is enabled.

## In torchtitan (grounded)
- Entry: [`set_moe_sharding_config`](../catalog/torchtitan/models/common/moe_sharding.md#set_moe_sharding_config)
  (args `enable_ep`, `enable_sp`, `expert_param_layout`), populating every submodule of
  [`MoE.Config`](../catalog/torchtitan/models/common/moe.md#MoE.Config).
- Submodules: [`MoE.router`](../catalog/torchtitan/models/common/moe.md#MoE.router) (gate weights
  `Replicate`, output stays DTensor), [`MoE.shared_experts`](../catalog/torchtitan/models/common/moe.md#MoE.shared_experts)
  (w1/w3 colwise, w2 rowwise, output left `Partial`), and
  [`MoE.routed_experts`](../catalog/torchtitan/models/common/moe.md#MoE.routed_experts) =
  [`RoutedExperts`](../catalog/torchtitan/models/common/moe.md#RoutedExperts), whose
  [`LocalMapConfig`](../catalog/torchtitan/protocols/sharding.md#LocalMapConfig "torchtitan/protocols/sharding.py:L34") converts DTensor
  inputs to local tensors, runs its [`token_dispatcher`](../catalog/torchtitan/models/common/moe.md#RoutedExperts.token_dispatcher)
  and [`inner_experts`](../catalog/torchtitan/models/common/moe.md#RoutedExperts.inner_experts)
  ([`GroupedExperts`](../catalog/torchtitan/models/common/moe.md#GroupedExperts "torchtitan/models/common/moe.py:L440")), and re-wraps the
  output as `DTensor(Partial)`. Expert-weight `state_shardings` live on the `GroupedExperts` child.
- Weight placement helpers: [`expert_param_placement_sparse`](../catalog/torchtitan/models/common/moe_sharding.md#expert_param_placement_sparse)
  and [`expert_param_placement_dense`](../catalog/torchtitan/models/common/moe_sharding.md#expert_param_placement_dense).
- **TPU lane:** the TPU MoE path swaps in its own routed experts / dispatcher / grouped experts
  through converters - [`TpuRoutedExperts`](../catalog/torchtitan/experiments/tpu/token_dispatcher.md#TpuRoutedExperts "torchtitan/experiments/tpu/token_dispatcher.py:L294"),
  [`TpuAllToAllTokenDispatcher`](../catalog/torchtitan/experiments/tpu/token_dispatcher.md#TpuAllToAllTokenDispatcher "torchtitan/experiments/tpu/token_dispatcher.py:L235"),
  [`TpuGroupedExperts`](../catalog/torchtitan/experiments/tpu/grouped_experts.md#TpuGroupedExperts "torchtitan/experiments/tpu/grouped_experts.py:L90") -
  inside the same `local_map` contract.

## Why it matters / when it applies

| Config | Routed expert mesh | Routed expert weights | MoE input src -> dst | MoE output |
|---|---|---|---|---|
| EP on, SP on | sparse (EP/EFSDP) | `Shard(0)` on EP | `Shard(1)` -> `Shard(1)` | `Partial` -> `Shard(1)` |
| EP on, SP off | sparse (EP/EFSDP) | `Shard(0)` on EP | `Replicate` -> `Replicate` | `Partial` -> `Replicate` |
| EP off, SP on | dense (TP) | TP colwise/rowwise | `Shard(1)` -> `Replicate` | `Partial` -> `Shard(1)` |
| EP off, SP off | dense (TP) | TP colwise/rowwise | `Replicate` -> `Replicate` | `Partial` -> `Replicate` |

- **One reduction per MoE layer.** Shared experts and routed experts both leave their output
  `Partial`; the reduction to the SP layout happens once at the MoE boundary (a reduce-scatter
  with SP, all-reduce without). Count these when attributing collective time in a profile.
- **EP off + SP on costs an all-gather on entry** (`Shard(1)` -> `Replicate`) because TP-sharded
  experts need the full sequence; with EP on, tokens stay sequence-sharded into the dispatcher and
  the dispatcher's all-to-all does the movement instead.
- **Expert weights on the sparse mesh** (`dp_replicate, efsdp, ep`) get expert-FSDP over the
  `efsdp` axis, separate from the dense FSDP of attention/MLP - this is why
  `apply_fsdp_to_decoder` takes `ep_degree` / `edp_mesh`.
- **Dispatch is local code.** Because routed experts run on local tensors, swapping the dispatcher
  (DeepEP, HybridEP, padded TorchAO dispatcher for MXFP8, TPU all-to-all) does not touch the
  sharding config.
- `expert_param_layout` (from code) maps each routed-expert parameter to its dense TP placement:
  `Shard(1)` colwise, `Shard(2)` rowwise for the 3D `[E, ...]` weights, used only on the EP-off +
  TP-on path.

## Connections
- Code concepts: [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [model-building-blocks](../concepts/model-building-blocks.md),
  [deepseek-v3-model](../concepts/deepseek-v3-model.md), [qwen3-model](../concepts/qwen3-model.md).
- Module catalogs: [torchtitan/models/common/moe_sharding](../catalog/torchtitan/models/common/moe_sharding.md),
  [torchtitan/models/common/moe](../catalog/torchtitan/models/common/moe.md),
  [torchtitan/models/common/token_dispatcher](../catalog/torchtitan/models/common/token_dispatcher.md),
  [torchtitan/experiments/tpu/token_dispatcher](../catalog/torchtitan/experiments/tpu/token_dispatcher.md).
- Related doc-concepts: [tpu-moe-kernel-switches](tpu-moe-kernel-switches.md), [declarative-sharding-config](declarative-sharding-config.md),
  [mxfp8-training](mxfp8-training.md),
  [flexshard-optimizer-compute-layouts](flexshard-optimizer-compute-layouts.md).

## Source
Extracted from `torchtitan/models/common/MOE_SHARDING.md` (kept in place). The doc's diagram
(`assets/images/moe_sharding.png`) is not reproduced.
