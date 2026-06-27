---
hypothesis: qwen3-jax-splash-tokamax
model: qwen3-ag-jax
variant: "8B/v6e-8"
status: in_progress
created: 2026-06-26
---

## Hypothesis under test
**Hypothesis**: By combining `splash-attention` (which resolves the `[B, Hq, T, T]` attention matrix materialization OOM) and `tokamax-ce` (which resolves the `[B, L, V]` logits materialization OOM), we can successfully run the Qwen3-8B jax model at 8192 sequence length without encountering an HBM `RESOURCE_EXHAUSTED` error.

**Mechanism**: We fork from `v001-splash` and integrate the `tokamax.linear_softmax_cross_entropy_loss` using `shard_map` and the `mosaic_tpu` implementation backend.

**Predicted signal**: The model should compile and execute 20 steps at 8K sequence length successfully without memory limits being breached.

## Setup

- **Code**: `jax/experiments/.repo/2026-06-26-v003-splash-tokamax` (forked from `v001-splash`)
- **Hardware**: TPU v6e-8 (`alekseyv-tpu-v6e8-spot-xpk`)
- **Command**: `JAX_ATTENTION_IMPL=splash python -m train --use_tokamax_ce=True --tokamax_ce_impl="mosaic_tpu" --train_steps 20 --batch_size 1 --seqlen 8192`

## Results

**Status**: Crashed (OOM during XLA compilation).

Used 45.12G of 31.25G HBM. This is almost exactly the same memory footprint as `v001-splash` alone (which used 44.8G). The combination of `splash-attention` and `tokamax-ce` was insufficient to unlock the 8K context length. While they removed the causal attention matrix and LM head materialization respectively, the memory footprint remains dominated by the forward pass activations for the MLP and attention blocks.

## Verdict

**Refuted**. 

The combination of splash attention and tokamax-ce does not fit in HBM. We need to reduce the activation memory footprint via gradient checkpointing (rematerialization) to fit the 8K sequence length.
