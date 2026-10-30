---
title: FlexShard optimizer compute layouts (storage-to-compute redistribution for DistMuon)
type: doc-concept
provenance: doc
source: torchtitan/distributed/flex_shard/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# FlexShard optimizer compute layouts (storage-to-compute redistribution for DistMuon)

## Definition
FlexShard lets optimizer math run on a **compute layout** that differs from how a parameter is
**stored** as a DTensor. Matrix optimizers like Muon need whole matrices (or whole blocks/heads) on
one rank, while FSDP/EP storage shards them arbitrarily; FlexShard plans a packed
storage-to-compute redistribution per parameter, overlaps that communication with optimizer work
in buckets, and returns updates to storage. DistMuon is its first consumer.

## In torchtitan (grounded)
- Public API in `torchtitan/distributed/flex_shard/`:
  [`ComputeLayout`](../catalog/torchtitan/distributed/flex_shard/optimizer_reshard.md#ComputeLayout "torchtitan/distributed/flex_shard/optimizer_reshard.py:L111")
  (temporary compute sharding over named mesh axes using DTensor placements plus
  [`BlockShard`](../catalog/torchtitan/distributed/flex_shard/optimizer_reshard.md#BlockShard "torchtitan/distributed/flex_shard/optimizer_reshard.py:L35") or
  [`Owned`](../catalog/torchtitan/distributed/flex_shard/optimizer_reshard.md#Owned "torchtitan/distributed/flex_shard/optimizer_reshard.py:L22"), with optional
  [`shard_order_by_tensor_dim`](../catalog/torchtitan/distributed/flex_shard/optimizer_reshard.md#ComputeLayout.shard_order_by_tensor_dim)),
  [`BucketConfig`](../catalog/torchtitan/distributed/flex_shard/optimizer_reshard.md#BucketConfig "torchtitan/distributed/flex_shard/optimizer_reshard.py:L252")
  (group/order parameters by FQN for packed redistribution + overlap), and
  [`build_dist_muon`](../catalog/torchtitan/distributed/flex_shard/dist_muon.md#build_dist_muon "torchtitan/distributed/flex_shard/dist_muon.py:L58") /
  [`DistMuon`](../catalog/torchtitan/distributed/flex_shard/dist_muon.md#DistMuon "torchtitan/distributed/flex_shard/dist_muon.py:L252")
  ([`step`](../catalog/torchtitan/distributed/flex_shard/dist_muon.md#DistMuon.step)).
- First integration: the Kimi config registry's shared
  [`_dist_muon_optimizer`](../catalog/torchtitan/models/kimi_k2_7/config_registry.md#_dist_muon_optimizer "torchtitan/models/kimi_k2_7/config_registry.py:L294")
  selects attention, dense-MLP, routed/shared-expert and router matrices for DistMuon (everything
  else stays AdamW), defines per-parameter compute layouts including per-head Muon for compatible
  attention projections, and groups layers into buckets. Expert layouts come from
  [`_per_expert_compute_layout`](../catalog/torchtitan/models/kimi_k2_7/config_registry.md#_per_expert_compute_layout "torchtitan/models/kimi_k2_7/config_registry.py:L267").

## Why it matters / when it applies
- **Placement semantics.** `BlockShard` shards complete fixed-size blocks along one tensor dim
  without views or rank change; `Owned` gives a whole subgroup-local tensor to one dynamically
  chosen rank. DistMuon's `BlockShard` path accepts only a contiguous 2D `[M*R, C]` parameter with
  `block_size=R` on dim 0 (each R rows is an independent `[R, C]` matrix), viewed as
  `[M_local, R, C]` just before Muon compute; native 3D `[M, R, C]` uses `Shard(0)`; a single 2D
  matrix uses `Owned`.
- **Constraints.** Flat matrix-batch compute supports `BlockShard` on at most one non-unit mesh axis;
  storage on that axis must be exact `Shard(0)` or `Replicate`, and every other non-unit storage
  axis replicated.
- **Multi-axis ordering for MoE.** Several mesh axes may shard the same dim; default order is storage
  mesh order, override with `shard_order_by_tensor_dim` (outermost first). Kimi preserves the EP-axis
  `Shard(0)` and repartitions each EP-local expert domain over EFSDP with order `("ep", "efsdp")`.
- **Checkpointing.** Compute sharding is construction-time, validated and frozen at optimizer build,
  and **not** in the optimizer state dict - restore must rebuild with matching values.
- **Perf lever.** Optimizer-step time for Muon-class optimizers is dominated by the
  redistribution; bucket sizing/order is the overlap knob. The Kimi docs note TP-produced
  `_StridedShard` layouts are currently rejected by DistMuon recipes.
- **Package boundary.** FlexShard is PyTorch-only and must not depend on TorchTitan model/training
  code (`TorchTitan -> FlexShard -> PyTorch`); it is slated to become a standalone package.
- TPU relevance: no TPU recipe uses DistMuon at this commit; the layout model is generic DTensor.

## Connections
- Code concepts: [flex-shard](../concepts/flex-shard.md),
  [optimizers-and-lr-schedulers](../concepts/optimizers-and-lr-schedulers.md),
  [kimi-k2-7-model](../concepts/kimi-k2-7-model.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md).
- Module catalogs: [torchtitan/distributed/flex_shard/optimizer_reshard](../catalog/torchtitan/distributed/flex_shard/optimizer_reshard.md),
  [torchtitan/distributed/flex_shard/dist_muon](../catalog/torchtitan/distributed/flex_shard/dist_muon.md),
  [torchtitan/models/kimi_k2_7/config_registry](../catalog/torchtitan/models/kimi_k2_7/config_registry.md).
- Related doc-concepts: [kimi-k2-7-model-notes](kimi-k2-7-model-notes.md),
  [moe-sharding-placements](moe-sharding-placements.md).

## Source
Extracted from `torchtitan/distributed/flex_shard/README.md` (kept in place).
