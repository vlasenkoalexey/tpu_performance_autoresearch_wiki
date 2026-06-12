# Experiment: v006 Tokamax Fused Cross-Entropy

**Status:** Completed
**Lane:** jax
**Date:** 2026-06-02

## Hypothesis under test
- **Hypothesis**: The out-of-memory error at `bs=2` is caused by the materialization of massive `[batch*seq, vocab_size]` logit arrays (151k vocab size requires >4.9GB of memory for logits in bf16 and another 4.9GB for gradients). Using `tokamax.linear_softmax_cross_entropy_loss` fused Pallas kernel will bypass the `lm_head` projection, performing the cross-entropy reduction locally on SRAM without materializing full logits in HBM, thus saving ~10GB of peak memory per chip and unblocking `bs=2`.
- **Mechanism**: Import `tokamax` and replace `optax.softmax_cross_entropy` + `lm_head` projection with the fused `linear_softmax_cross_entropy_loss` call. Pass the pre-projection hidden states and `lm_head_weight`.
- **Predicted signal**: The model compiles and runs successfully at `bs=2` without OOM, significantly pushing the frontier past 20.0% MFU.
- **Falsification criterion**: The workload still OOMs, indicating the bottleneck is not the logits but the self-attention activation KV cache or seqlen materialization.

## Configuration
- **Model**: Qwen/Qwen3-8B
- **Framework**: JAX (Flax NNX)
- **Batch Size**: 2
- **Seq Length**: 2048
- **Remat Policy**: `checkpoint_dots_with_no_batch_dims`
- **Attention**: SDPA (Baseline)
- **Image**: `us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v6e8-qwen3-8b-jax-20260602-v006-tokamax-ce-e`
- **Flags**: `--batch_size=2`

## Setup
- Created fork directory: `.repo/2026-06-02-v006-tokamax-ce/`
- Modified `loss_fn` in `train.py` to use `tokamax.linear_softmax_cross_entropy_loss` directly, bypassing the model's `lm_head` projection to apply the fused CE kernel on the pre-projection hidden states directly. Passed `w.T` to correctly match kernel expectations. (Removed previous manual `shard_map` wrapping since the kernel natively supports global `jax.Array` objects with SPyMD sharding.)
- Eagerly initialized `absl.flags` before importing `tokamax` to prevent `absl.flags.FLAGS` initialization from crashing due to unrecognized command line flags before `fire.Fire` runs.
- Built and pushed image: `us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v6e8-qwen3-8b-jax-20260602-v006-tokamax-ce-e`

## Results
- **Status**: Crashed
- **Error**: `RESOURCE_EXHAUSTED: XLA:TPU compile permanent error. Ran out of memory in memory space hbm. Used 41.77G of 31.25G hbm. Exceeded hbm capacity by 10.52G.`

## Verdict
**Refuted/Invalid**.
The integration of the Tokamax fused CE kernel without `shard_map` over an FSDP mesh resulted in a catastrophic memory explosion during compilation (41.77 GB HBM requested, far exceeding the baseline `bs=2` SDPA memory profile of ~16.5 GB). This suggests the kernel either fell back to an unoptimized XLA implementation, forcefully gathered massive gradient tensors because it expects Tensor Parallelism (`tp`) instead of FSDP, or failed to partition the `X @ W` backward pass correctly in a pure FSDP environment.

## Next Steps
Focus on `v008` (Splash Attention + TP=2), which structurally reduces memory by both avoiding materializing attention matrices (via flash attention blocks) and sharding KV cache across chips.
