# Experiment: v010 Splash + TP=2 + Tokamax CE (bs=8)

**Status:** Completed
**Lane:** jax
**Date:** 2026-06-02

## Hypothesis under test
- **Hypothesis**: `v009` (Splash + TP=2 at `bs=8`) failed to compile, exceeding HBM limits by ~4GB. By adding Tokamax CE to the stack, we can eliminate the materialization of the `[batch*seq, vocab_size]` logit tensors (saving ~5GB). Because the layout already utilizes TP=2 (which Tokamax natively supports), the Pallas cross-entropy kernel should correctly shard its work and not trigger the massive `fsdp` memory bloat seen in `v006`. This combined 3-part memory stack should theoretically provide enough headroom to fit `bs=8` under the 31.25GB limit.
- **Mechanism**: Use the `v008` Splash Attention + TP=2 image and edit `train.py` to replace standard CE with `tokamax.linear_softmax_cross_entropy_loss(x, y, w.T, reduction='sum')`.
- **Predicted signal**: The workload will compile and run successfully at `bs=8` without OOM, pushing MFU beyond the 28.6% achieved in `v008`.
- **Falsification criterion**: The workload still OOMs at `bs=8`.

## Configuration
- **Model**: Qwen/Qwen3-8B
- **Framework**: JAX (Flax NNX)
- **Batch Size**: 8
- **Seq Length**: 2048
- **Remat Policy**: `checkpoint_dots_with_no_batch_dims`
- **Attention**: Splash Attention
- **Image**: `us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v6e8-qwen3-8b-jax-20260602-v010-splash-tp2-tokamax-bs8`
- **Flags**: `--tp_parallelism=2 --batch_size=8 --use_splash=True`

## Setup
- Branched from `v008` fork.
- Modified `loss_fn` in `train.py` to use `tokamax.linear_softmax_cross_entropy_loss(x, y, w.T, reduction='sum')`.
- Built and pushed image as `v010-splash-tp2-tokamax-bs8`.
- Launched via `gke-cluster-runner`.

## Results
- **Status**: Crashed
- **Error**: `RESOURCE_EXHAUSTED: XLA:TPU compile permanent error. Ran out of memory in memory space hbm. Used 33.98G of 31.25G hbm. Exceeded hbm capacity by 2.74G.`

## Verdict
**Refuted**.
While Tokamax CE successfully eliminated some overhead compared to `v009` (which requested 35.21GB), the `v010` compile still hit 33.98GB—exceeding HBM capacity by 2.74GB. Tokamax CE combined with TP=2 was structurally sound, but the raw memory pressure from the `bs=8` activation footprint is simply too large.

## Next Steps
We must turn to **Activation Checkpointing (Rematerialization)**. The current policy `checkpoint_dots_with_no_batch_dims` saves some memory by recomputing element-wise ops, but it still stores large matmul outputs for the backward pass. We should move to a more aggressive rematerialization policy (e.g. `checkpoint_dots` or fully recomputing the transformer block) to slash the activation footprint. This will cost some compute cycles (reducing MFU slightly per step) but will unlock the ability to scale batch size massively.
