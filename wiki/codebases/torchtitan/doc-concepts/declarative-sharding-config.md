---
title: Declarative sharding config (ShardingConfig, canonical mesh-axis order, spmd backends)
type: doc-concept
provenance: doc
source: torchtitan/models/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Declarative sharding config (ShardingConfig, canonical mesh-axis order, spmd backends)

## Definition
TP, SP, EP, and inner-attention `local_map` placements are expressed **declaratively**: each
`Module.Config` in the model tree carries a `sharding_config` describing parameter/state placements
and activation input/output redistributions per named mesh axis. `Module.parallelize` walks the
tree and applies them, replacing the older per-model imperative `parallelize_module` plan dicts.
Mesh axes are always declared in canonical outer-to-inner SPMD order, and the active SPMD backend
decides which axes are actually materialized.

## In torchtitan (grounded)
- The per-module record: [`ShardingConfig`](../catalog/torchtitan/protocols/sharding.md#ShardingConfig "torchtitan/protocols/sharding.py:L60")
  ([`state_shardings`](../catalog/torchtitan/protocols/sharding.md#ShardingConfig.state_shardings "torchtitan/protocols/sharding.py:L108"),
  [`in_src_shardings`](../catalog/torchtitan/protocols/sharding.md#ShardingConfig.in_src_shardings "torchtitan/protocols/sharding.py:L109") /
  [`in_dst_shardings`](../catalog/torchtitan/protocols/sharding.md#ShardingConfig.in_dst_shardings "torchtitan/protocols/sharding.py:L110"),
  [`out_src_shardings`](../catalog/torchtitan/protocols/sharding.md#ShardingConfig.out_src_shardings "torchtitan/protocols/sharding.py:L111") /
  [`out_dst_shardings`](../catalog/torchtitan/protocols/sharding.md#ShardingConfig.out_dst_shardings "torchtitan/protocols/sharding.py:L112"),
  [`local_map`](../catalog/torchtitan/protocols/sharding.md#ShardingConfig.local_map "torchtitan/protocols/sharding.py:L113") ->
  [`LocalMapConfig`](../catalog/torchtitan/protocols/sharding.md#LocalMapConfig "torchtitan/protocols/sharding.py:L34")).
- Applied by [`Module.parallelize`](../catalog/torchtitan/protocols/module.md#Module.parallelize "torchtitan/protocols/module.py:L279");
  meshes come from [`ParallelDims.resolve_mesh`](../catalog/torchtitan/distributed/parallel_dims.md#ParallelDims.resolve_mesh)
  using axis names from [`MeshAxisName`](../catalog/torchtitan/distributed/parallel_dims.md#MeshAxisName "torchtitan/distributed/parallel_dims.py:L72").
- Shared helpers in `torchtitan/models/common/decoder_sharding.py`:
  [`set_decoder_sharding_config`](../catalog/torchtitan/models/common/decoder_sharding.md#set_decoder_sharding_config),
  [`set_dense_ffn_sharding`](../catalog/torchtitan/models/common/decoder_sharding.md#set_dense_ffn_sharding),
  [`set_gqa_attention_sharding`](../catalog/torchtitan/models/common/decoder_sharding.md#set_gqa_attention_sharding),
  [`norm_config`](../catalog/torchtitan/models/common/decoder_sharding.md#norm_config),
  [`dense_param_placement`](../catalog/torchtitan/models/common/decoder_sharding.md#dense_param_placement "torchtitan/models/common/decoder_sharding.py:L24"),
  [`dense_activation_placement`](../catalog/torchtitan/models/common/decoder_sharding.md#dense_activation_placement "torchtitan/models/common/decoder_sharding.py:L39");
  MoE uses [`set_moe_sharding_config`](../catalog/torchtitan/models/common/moe_sharding.md#set_moe_sharding_config)
  (see [moe-sharding-placements](moe-sharding-placements.md)).
- Backend selector: [`ParallelismConfig.spmd_backend`](../catalog/torchtitan/config/configs.md#ParallelismConfig.spmd_backend "torchtitan/config/configs.py:L199")
  (`"partial_dtensor"` default or `"spmd_types"`).

## Why it matters / when it applies
- **Canonical axis order:** `(dp, cp, tp)` for dense modules (attention, MLP, norms, embedding, LM
  head) and `(dp_replicate, efsdp, ep)` for sparse MoE expert weights. Every placement names every
  axis; the backend drops what it keeps out-of-band.
- **Backend decides what is in-band (from code):** `resolve_mesh` keeps only `tp` and `ep` under
  `partial_dtensor` (DP/CP are handled by FSDP and the CP input path), while `spmd_types` also keeps
  `dp` and `cp`. Context parallelism requires `spmd_types` (see
  [model-config-transforms](model-config-transforms.md)), and several low-precision and TPU CP
  recipes switch to it explicitly. Changing the backend therefore changes which collectives appear
  in the traced graph - a first-order thing to check in an HLO diff.
- **Placements depend on the run's parallelism:** the setter is called from the model config's
  `update_from_config()`, so `enable_sp` and EP on/off are resolved from `parallelism` at trainer
  init, before overrides run. An override module that declares its own `ShardingConfig` composes
  with this automatically (see [override-implementation-contract](override-implementation-contract.md)).
- **No imperative per-model plans** means a new model mostly reuses the decoder helpers; model-only
  modules (e.g. Qwen3.5 GatedDeltaNet, DeepSeek-V4 compressors, MTP blocks) add small setters.
- **TPU lane:** TPU-specific mesh shaping sits outside these configs, e.g.
  [`ParallelismConfig.enable_tpu_topo_mesh`](../catalog/torchtitan/config/configs.md#ParallelismConfig.enable_tpu_topo_mesh)
  (topology-aware TPU mesh) and SimpleFSDP shard-dim tuning such as
  [`configure_qwen_simple_fsdp_shard_dims`](../catalog/torchtitan/experiments/tpu/qwen3_sharding.md#configure_qwen_simple_fsdp_shard_dims "torchtitan/experiments/tpu/qwen3_sharding.py:L19").

## Connections
- Code concepts: [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [model-spec-protocols](../concepts/model-spec-protocols.md),
  [model-building-blocks](../concepts/model-building-blocks.md),
  [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md),
  [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md).
- Module catalogs: [torchtitan/protocols/sharding](../catalog/torchtitan/protocols/sharding.md),
  [torchtitan/protocols/module](../catalog/torchtitan/protocols/module.md),
  [torchtitan/models/common/decoder_sharding](../catalog/torchtitan/models/common/decoder_sharding.md),
  [torchtitan/distributed/parallel_dims](../catalog/torchtitan/distributed/parallel_dims.md).
- Related doc-concepts: [simple-fsdp](simple-fsdp.md), [tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md), [model-folder-contract](model-folder-contract.md),
  [moe-sharding-placements](moe-sharding-placements.md),
  [deepseek-v3-multi-token-prediction](deepseek-v3-multi-token-prediction.md).

## Source
Extracted from `torchtitan/models/README.md` (kept in place).
