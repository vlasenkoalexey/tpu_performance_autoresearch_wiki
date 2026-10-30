---
title: JAX lane scan-over-layers (ScannedTransformerBlocks) and remat policy
type: doc-concept
provenance: doc
source: torchtitan/experiments/jax/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# JAX lane scan-over-layers (ScannedTransformerBlocks) and remat policy

## Definition
With `use_scan=True` the JAX lane stacks every transformer block's parameters along a new leading layer axis and runs the blocks with `jax.lax.scan`. XLA then compiles **one** block body regardless of depth, giving a constant-size graph, much faster compilation than unrolled layers, and parameter names that a sharding map can target directly. Activation checkpointing is applied to the scanned body through a JAX remat policy.

## In torchtitan (grounded)
- [`ScannedTransformerBlocks`](../catalog/torchtitan/experiments/jax/llama3/model.md#ScannedTransformerBlocks) holds the stacked weights as named `nnx.Param` attributes derived from the block's NNX state paths (e.g. `attention_wq_kernel`, `feed_forward_w2_kernel`); [`ScannedTransformerBlocks.__call__`](../catalog/torchtitan/experiments/jax/llama3/model.md#ScannedTransformerBlocks.__call__) performs the scan. The top-level model chooses scan vs a Python list of blocks in [`Transformer.layers`](../catalog/torchtitan/experiments/jax/llama3/model.md#Transformer.layers).
- Switch: [`JaxConfig.use_scan`](../catalog/torchtitan/experiments/jax/jax_job_config.md#JaxConfig.use_scan) (default True), read in [`JaxTrainer.setup_model`](../catalog/torchtitan/experiments/jax/trainer.md#JaxTrainer.setup_model).
- Remat policy selection in `setup_model`: core [`FullAC`](../catalog/torchtitan/distributed/activation_checkpoint.md#FullAC) config -> `jax.checkpoint_policies.nothing_saveable`; [`SelectiveAC`](../catalog/torchtitan/distributed/activation_checkpoint.md#SelectiveAC) config -> `dots_saveable`; no AC config -> no remat.
- The scan variant has its own sharding map, [`sharding_map_scan`](../catalog/torchtitan/experiments/jax/llama3/sharding.md#sharding_map_scan), whose keys are the stacked attribute names with a leading unsharded layer axis.

## Why it matters / when it applies
- Compile time scales with depth for unrolled models (Llama3 70B has 80 layers); scan makes it roughly depth-independent, which is why the quick start uses `--jax_config.use_scan` and the published ~20% MFU number is a scan + full-AC run.
- `selective` here means "save matmul outputs" (`dots_saveable`), which is a different policy from the torch lanes' op-list SAC; comparisons of "selective AC" across lanes must account for that.
- **TPU relevance.** This is the same structural lever the torch-on-TPU lane reaches with its layer loop / scan path; see [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md) and the TPU guide's [tpu-scan-graph-splitter-cpu-offload](tpu-scan-graph-splitter-cpu-offload.md).

**Doc vs code at this commit:** the README's key-flag table lists `--activation_checkpoint.mode` with values `full`, `selective`, `nothing`. The trainer does not read a `mode` string; it dispatches on the type of the `activation_checkpoint` config object (`FullAC.Config` / `SelectiveAC.Config` / `None`), and any other config type falls back to `nothing_saveable` (full recompute).

## Connections
- Code concepts: [jax-lane](../concepts/jax-lane.md), [tpu-layer-loop-remat-and-layouts](../concepts/tpu-layer-loop-remat-and-layouts.md), [llama3-model](../concepts/llama3-model.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md)
- Module catalogs: [jax/llama3/model](../catalog/torchtitan/experiments/jax/llama3/model.md), [jax/llama3/sharding](../catalog/torchtitan/experiments/jax/llama3/sharding.md), [jax/trainer](../catalog/torchtitan/experiments/jax/trainer.md), [distributed/activation_checkpoint](../catalog/torchtitan/distributed/activation_checkpoint.md)
- Related doc-concepts: [jax-flax-nnx-lane](jax-flax-nnx-lane.md), [jax-fsdp-tp-mesh-sharding](jax-fsdp-tp-mesh-sharding.md), [graph-trainer-memory-policy](graph-trainer-memory-policy.md), [tpu-scan-graph-splitter-cpu-offload](tpu-scan-graph-splitter-cpu-offload.md)

## Source
Extracted from `torchtitan/experiments/jax/README.md` (kept in place).
