---
title: JAX lane (fsdp, tp) mesh and parameter sharding maps
type: doc-concept
provenance: doc
source: torchtitan/experiments/jax/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# JAX lane (fsdp, tp) mesh and parameter sharding maps

## Definition
The JAX lane builds a 2-D named mesh `(fsdp, tp)` with `tp = --parallelism.tensor_parallel_degree` and `fsdp = num_devices // tp` (v6e-4 with tp=1 -> `fsdp=4, tp=1`). Parameters are placed with `jax.sharding.NamedSharding` according to a **path-pattern -> PartitionSpec map**; multi-slice runs build the mesh with `create_hybrid_device_mesh` so the fsdp axis spans slices over DCN.

## In torchtitan (grounded)
- Mesh construction is in [`main`](../catalog/torchtitan/experiments/jax/train_minimal.md#main): `jax.make_mesh((fsdp, tp), ('fsdp','tp'))` for one slice; for [`JaxConfig.tpu_num_slices`](../catalog/torchtitan/experiments/jax/jax_job_config.md#JaxConfig.tpu_num_slices) > 1 it calls `create_hybrid_device_mesh` with ICI shape `(fsdp // slices, tp)` and DCN shape `(slices, 1)`.
- Sharding maps: [`sharding_map_scan`](../catalog/torchtitan/experiments/jax/llama3/sharding.md#sharding_map_scan) and [`sharding_map_original`](../catalog/torchtitan/experiments/jax/llama3/sharding.md#sharding_map_original) (non-scan). They are applied by [`apply_sharding_to_state`](../catalog/torchtitan/experiments/jax/distributed.md#apply_sharding_to_state) (path matching in [`_match_path`](../catalog/torchtitan/experiments/jax/distributed.md#_match_path), placement via [`sharded_device_put`](../catalog/torchtitan/experiments/jax/distributed.md#sharded_device_put)); batches are placed with [`shard_input`](../catalog/torchtitan/experiments/jax/distributed.md#shard_input).
- Splash attention runs under `shard_map` with Q sharded `P('fsdp', 'tp', None, None)` (batch on fsdp, heads on tp) in [`make_splash_attention_fn`](../catalog/torchtitan/experiments/jax/splash_attn.md#make_splash_attention_fn).

## Why it matters / when it applies
- Placement decides the HBM footprint per chip and which collectives XLA inserts; the maps are the lane's whole parallel plan.
- The scan map makes two deliberate memory choices documented in code comments: the output projection is sharded on the **vocab** dim so the fp32-upcast logits in cross-entropy are `[B, S, V/fsdp]` (~4 GiB -> ~1 GiB/chip at b=16, s=2048, V=128256, at the cost of an all-reduce inside log-sum-exp), and the embedding is sharded on the hidden dim.
- The RoPE `freqs_cis` table is replicated in both maps.
- **TPU relevance.** This is the native-JAX statement of the FSDP-on-a-named-mesh model that the torch-on-TPU lane expresses through its own parallelization code; see [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md) and, for multi-slice, the TPU guide's [tpu-multislice-hsdp-over-dcn](tpu-multislice-hsdp-over-dcn.md).

**Doc vs code at this commit:**
- The README says the embedding table is replicated to avoid gather ambiguity. That is true only for the non-scan map; the default scan map shards the embedding as `(None, 'fsdp')` on the hidden dim.
- The README says all attention and FFN weights are FSDP-sharded on their **leading** weight dim. In both maps `wo` and `w2` are sharded on their second dim (`(None, 'fsdp')`, or `(None, None, 'fsdp')` when stacked).
- Neither sharding map references the `tp` axis. Setting `tensor_parallel_degree > 1` shrinks the fsdp axis, and only the splash-attention `shard_map` uses `tp` (heads). Weights are not tensor-parallel-sharded.

## Connections
- Code concepts: [jax-lane](../concepts/jax-lane.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md), [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md), [llama3-model](../concepts/llama3-model.md)
- Module catalogs: [jax/distributed](../catalog/torchtitan/experiments/jax/distributed.md), [jax/llama3/sharding](../catalog/torchtitan/experiments/jax/llama3/sharding.md), [jax/train_minimal](../catalog/torchtitan/experiments/jax/train_minimal.md), [jax/splash_attn](../catalog/torchtitan/experiments/jax/splash_attn.md)
- Related doc-concepts: [jax-flax-nnx-lane](jax-flax-nnx-lane.md), [jax-scan-over-layers](jax-scan-over-layers.md), [tpu-multislice-hsdp-over-dcn](tpu-multislice-hsdp-over-dcn.md), [tpu-splash-attention-tiles-and-vmem](tpu-splash-attention-tiles-and-vmem.md)

## Source
Extracted from `torchtitan/experiments/jax/README.md` (kept in place).
