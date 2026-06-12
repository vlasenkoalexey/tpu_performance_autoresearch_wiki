# Experiment: v014 Splash + TP=2 + Tokamax CE + Per-Layer Remat (bs=8)

**Status:** Completed
**Lane:** jax
**Date:** 2026-06-03

## Hypothesis under test
- **Hypothesis**: In `v010` (Splash + TP=2 + Tokamax CE at bs=8) we OOMed at ~33.9GB. We proved in `v011` that the `checkpoint_dots` policy alone wasn't enough. The root issue is the `Qwen3Model` loop saves every activation intermediate across all 36 decoder blocks. By applying per-layer rematerialization (`nnx.remat`) around the `Qwen3DecoderLayer` application in the forward loop, we will trade recompute efficiency to drastically slash the activation memory footprint, finally unlocking `bs=8` at `TP=2`.
- **Mechanism**: Use the `v010` Tokamax CE image. Edit `model/modeling_qwen3.py` to wrap the layer application in `nnx.remat(layer)(hidden_states, ...)`. Launch with `--tp_parallelism=2` and `--batch_size=8`.
- **Predicted signal**: The workload will compile and run at `bs=8` without OOM, pushing MFU significantly higher.
- **Falsification criterion**: The workload still OOMs, or the massive recompute penalty degrades throughput worse than the `bs=4` baseline.

## Configuration
- **Model**: Qwen/Qwen3-8B
- **Framework**: JAX (Flax NNX)
- **Batch Size**: 8
- **Seq Length**: 2048
- **Remat Policy**: `nnx.remat` (per-layer)
- **Attention**: Splash Attention
- **Image**: `us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v6e8-qwen3-8b-jax-20260602-v014-splash-tp2-tokamax-remat-bs8`
- **Flags**: `--tp_parallelism=2 --batch_size=8 --use_splash=True`

## Setup
Derived from `v010` (Splash + TP=2 + Tokamax CE). 
1. In `model/modeling_qwen3.py`, wrapped the `Qwen3DecoderLayer` application inside the `Qwen3Model.__call__` loop with `nnx.remat`: `hidden_states = nnx.remat(layer)(hidden_states, (cos, sin), attention_mask=None)`.
2. Built new docker image `us-central1-docker.pkg.dev/tpu-pytorch/torchtitan-images/qwen3-8b-jax:v6e8-qwen3-8b-jax-20260602-v014-splash-tp2-tokamax-remat-bs8` containing the modified model code.
3. Launched via `gke-cluster-runner`.

## Results
- **Status**: Completed (Exit Code 0)
- **Throughput**: 47558 tok/s (5945/chip)
- **Approx MFU**: 30.6%

## Profile Analysis
- `convolution fusion` (main matmuls) accounts for 35.8% of the step.
- `all-reduce-scatter fusion`, `all-gather`, and `all-to-all` accounts for a combined ~27.9% of the step. This is the TP=2 overhead.
- `loop fusion` (elementwise / activations) accounts for 12.8%.
- HBM Peak: 31.23 GB / 31.25 GB (99.94%).

## Verdict
**Supported**.
The application of `nnx.remat` successfully slashed the memory footprint, allowing `bs=8` to compile and run without OOM! Even with the heavy compute penalty of recalculating the forward pass during the backward pass, the increased arithmetic intensity from scaling the batch size pushed our overall MFU to 30.6% (our best result yet).

However, the profile shows our HBM utilization peaked at exactly 99.94% (31.23 / 31.25 GB). This means we have absolutely zero memory headroom left. Batch size 16 is completely impossible with this stack. 

## Next Steps
Since we cannot scale batch size any further without OOMing, we must look for pure compute-efficiency optimizations at `bs=8`. 
The profile shows `loop fusion` consuming 12.8% of the step time. 
According to the `program.md` constraints, Qwen3 has a unique structural feature: `QK-norm`, an RMSNorm applied to Q and K immediately before RoPE. 
We should write/integrate a custom Pallas kernel that fuses `QK-norm + RoPE` together in SRAM to eliminate the massive memory-bandwidth roundtrips associated with those element-wise operations. This should yield the final push we need to reach >35% MFU.
