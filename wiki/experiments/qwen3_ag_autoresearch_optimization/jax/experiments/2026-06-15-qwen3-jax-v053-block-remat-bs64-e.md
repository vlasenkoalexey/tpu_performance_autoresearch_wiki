---
title: "qwen3-jax-v053-block-remat-bs64-e"
type: experiment
model: qwen3-cc-jax
variant: 8B/v6e-8
hypothesis: "Encapsulate the block-wise rematerialization scan in a `shard_map` to prevent GSPMD's `NotImplementedError` on auto-partitioning Mosaic kernels."
status: in_progress
created: 2026-06-15
origin: 2026-06-15-qwen3-jax-v053-block-remat-bs64-d
---

# qwen3-jax-v053-block-remat-bs64-e

## Hypothesis under test

**Hypothesis**: Grouping layers into blocks of K=4 and applying `nnx.remat` only at the block boundary (instead of per-layer) will reduce the layer boundary memory footprint by 75% (~11 GB), allowing `batch_size=8` (global 64) to fit within the 31.25 GB HBM limit.

**Mechanism**: We reshaped the `self.layers` parameters from `(36, ...)` to `(9, 4, ...)` in `modeling_qwen3.py`. We use a nested `nnx.scan`: an outer scan over the 9 blocks with `nnx.remat` applied to the block, and an inner scan over the 4 layers without `remat`. This means during the backward pass, we recompute 4 layers at a time from a single saved boundary, rather than saving 36 boundaries.

**Predicted signal**: Expect peak HBM usage to drop from >33 GB to ~22-26 GB, allowing compilation and execution to succeed at `bs=64` per chip. 

**Falsification criterion**: HBM exceeds 31.25 GB or step time degrades excessively compared to baseline.

## Setup

Fork from v053-d. Add explicit `shard_map` encapsulation around the `nnx.scan` block to prevent GSPMD from auto-partitioning Mosaic kernels.

## Results

## Profile

## HLO Dump

## Verdict
