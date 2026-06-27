---
hypothesis: qwen3-jax-gradient-checkpointing
model: qwen3-ag-jax
variant: "8B/v6e-8"
status: in_progress
created: 2026-06-26
---

## Hypothesis under test
**Hypothesis**: By combining `splash-attention` (which resolves the `[B, Hq, T, T]` attention matrix materialization OOM) and `jax.remat` (gradient checkpointing, which resolves the activation memory wall from the forward pass of the deep transformer layers), we can successfully compile and run the Qwen3-8B jax model at 8192 sequence length without an HBM `RESOURCE_EXHAUSTED` error.

**Mechanism**: We fork from `v001-splash` and wrap the `Qwen3Block` application in `jax.checkpoint` during the model definition or call. (We will use NNX's `nnx.remat` or standard `jax.remat`).

**Predicted signal**: The model should compile and execute 20 steps at 8K sequence length successfully without memory limits being breached, albeit with slightly higher compute time per step due to recomputation.

## Setup

- **Code**: `jax/experiments/.repo/2026-06-26-v004-gradient-checkpointing` (forked from `v001-splash`)
- **Hardware**: TPU v6e-8 (`alekseyv-tpu-v6e8-spot-xpk`)
- **Command**: `JAX_REMAT=1 JAX_ATTENTION_IMPL=splash python -m train --train_steps 20 --batch_size 1 --seqlen 8192`

## Results

**Status**: Completed successfully.

The experiment compiled and ran to completion at 8192 sequence length without encountering any OOM. 
- **MFU**: 31.0% (v6e bf16 peak)
- **Throughput**: ~43300 tok/s

## Profile
gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-06-26-qwen3-jax-v004-gradient-checkpointing/plugins/profile

## HLO Dump
gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-06-26-qwen3-jax-v004-gradient-checkpointing/hlo

## Verdict

**Confirmed**.

Adding gradient checkpointing (rematerialization) to the deep transformer layers successfully trades compute for memory, allowing the model to fit in HBM during the backward pass at 8K context length. Splash attention resolved the attention memory limit, and remat resolved the activation memory limit. 

We can now use this setup as the baseline for further scale and performance optimizations.
