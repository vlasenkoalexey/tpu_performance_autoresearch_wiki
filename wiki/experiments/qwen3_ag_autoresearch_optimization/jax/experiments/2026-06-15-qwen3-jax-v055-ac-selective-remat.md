---
title: "qwen3-jax-v055-ac-selective-remat"
type: experiment
model: qwen3-cc-jax
variant: 8B/v6e-8
hypothesis: "Applying jax.checkpoint to the Qwen3 Attention and MLP blocks selectively will reduce peak HBM during the forward pass, allowing us to scale the sequence length/batch size and avoid OOM errors on v6e."
status: in_progress
created: 2026-06-15
origin: retrospective-recommendation
---

# qwen3-jax-v055-ac-selective-remat

## Hypothesis under test

**Hypothesis**: The lane is currently bottlenecked by the 31.25 GB HBM capacity on v6e, which is preventing batch scaling. Prior experiments hitting OOM errors (like the `v054` Pallas fusion attempts which crash at allocation size 34GB) indicate severe memory pressure during the forward pass. Activation Checkpointing (AC) is a proven technique for trading compute for memory by discarding intermediate activations during the forward pass and recomputing them during the backward pass.

**Mechanism**: Modify `model/modeling_qwen3.py` to wrap the `Qwen3Attention` and `Qwen3MLP` modules (or the entire `Qwen3DecoderLayer`) with `jax.checkpoint`. 

**Predicted signal**: Peak memory allocation should drop significantly, preventing OOM errors and allowing larger batch sizes or sequence lengths, ultimately leading to higher MFU.

**Falsification criterion**: If applying `jax.checkpoint` does not resolve the OOM errors or causes a severe degradation in MFU due to recomputation overhead, the hypothesis is refuted.

## Setup
Modify `model/modeling_qwen3.py` to use `jax.checkpoint` on the decoder layers.

## Results

## Profile

## HLO Dump

## Verdict

