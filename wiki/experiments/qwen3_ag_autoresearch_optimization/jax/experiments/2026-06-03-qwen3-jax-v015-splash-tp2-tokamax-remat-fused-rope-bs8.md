# Experiment: v015 Splash + TP=2 + Tokamax CE + Per-Layer Remat + Fused QK-norm RoPE (bs=8)

**Status:** Completed
**Lane:** jax
**Date:** 2026-06-03

## Hypothesis under test
- **Hypothesis**: The `v014` profile (bs=8, Splash, TP=2, Tokamax CE, nnx.remat) reached 30.6% MFU, but showed a 12.8% step time overhead in `loop fusion`. According to Qwen3 architecture, `QK-norm` and `RoPE` are distinct element-wise ops interrupted by a tensor transpose. By moving the `QK-norm` application to *after* the transpose, we make it contiguous with RoPE, encouraging XLA to fuse them into a single loop. This should eliminate the element-wise memory bandwidth overhead and push our MFU higher towards 35%.
- **Mechanism**: Use the `v014` image. Edit `modeling_qwen3.py` to move `self.q_norm` and `self.k_norm` to after the `jnp.transpose`.
- **Predicted signal**: MFU increases noticeably past 30.6%.
- **Falsification criterion**: MFU remains identical, indicating XLA was already fusing them or the memory bandwidth saving is negligible.

## Configuration
- **Model**: Qwen/Qwen3-8B
- **Framework**: JAX (Flax NNX)
- **Batch Size**: 8
- **Seq Length**: 2048
- **Remat Policy**: `nnx.remat` (per-layer)
- **Attention**: Splash Attention
- **Image**: `us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v6e8-qwen3-8b-jax-20260602-v015-splash-tp2-tokamax-remat-fused-rope-bs8`
- **Flags**: `--tp_parallelism=2 --batch_size=8 --use_splash=True`

## Setup
Derived from `v014`.
Modified `Qwen3Attention.__call__` to apply `q_norm` and `k_norm` after `q` and `k` transposes.
Launched via `gke-cluster-runner`.

## Results
- **Status**: Completed (Exit Code 0)
- **Throughput**: 47781 tok/s (5973/chip)
- **Approx MFU**: 30.7%

## Verdict
**Refuted**.
The throughput only increased from 47558 to 47781 tok/s, a marginal 0.1% MFU bump. The minor structural edit did not unlock any massive XLA fusions, likely because XLA is already heavily optimizing the graph or the element-wise overhead is dominated by other activations.

## Next Steps
We are at 30.7% MFU. To reach >35% MFU, we need to eliminate the `all-reduce-scatter` and `all-gather` TP=2 communication overhead (which costs ~23% of step time). 
If we use Pure FSDP (TP=1), we eliminate TP communication. However, `bs=8` at TP=1 will OOM. We know `bs=4` at TP=1 has the *exact same* sequence and activation memory footprint as `bs=8` at TP=2 (because the sequence/head dimension is not split by 2, but the batch size is halved). `bs=4` at TP=1 should fit perfectly inside 31.25GB HBM, and it completely eliminates Tensor Parallelism.
