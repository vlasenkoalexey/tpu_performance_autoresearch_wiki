---
variant: 8B/v6e-8
hypothesis: Fused GLU custom backward kernel
status: in_progress
created: 2026-06-27
---

# Experiment v016: Fused GLU custom backward kernel

## Hypothesis under test

**Hypothesis**: Implementing a full custom Pallas backward kernel for Fused GLU (SwiGLU) will eliminate the HBM materialization overhead observed in `v013`, reducing total memory traffic and increasing overall step MFU beyond the `v009` baseline of 32.5%.

**Mechanism**: In `v013`, the forward pass of SwiGLU was fused using Pallas, but the backward pass fell back to `jax.custom_vjp` invoking standard `jnp.dot` and `jax.remat` redundant recalculations, creating a ~3x compute overhead and materializing large intermediates (`u`, `gate`, `du`, `dgate`) in HBM. For `v016`, we write a custom backward Pallas kernel that calculates `dx`, `dw_up`, and `dw_gate` on the fly inside SRAM, keeping intermediate states off HBM entirely.

**Predicted signal**: We expect step MFU to exceed the 32.5% single-chip baseline. `approx MFU` and `tps` should show a net gain. Peak HBM should decrease relative to the baseline.

**Falsification criterion**: Step MFU does not exceed 32.5% or the implementation fails numerical equivalence.

## Setup

```bash
LIBTPU_INIT_ARGS="--xla_tpu_scoped_vmem_limit_kib=81920" XLA_FLAGS="--xla_dump_to=gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-06-27-qwen3-jax-v016-fused-glu-bwd/hlo --xla_dump_hlo_as_text --xla_dump_hlo_as_proto --xla_dump_hlo_pass_re=.*" JAX_PERSISTENT_CACHE_MIN_COMPILE_TIME_SECS=1 JAX_PERSISTENT_CACHE_MIN_ENTRY_SIZE_BYTES=0 JAX_COMPILATION_CACHE_DIR=gs://tpu-pytorch-alekseyv-us-central2/jax-compile-cache JAX_REMAT=1 python -m train --train_steps 20 --batch_size 1 --seqlen 8192 --profile_dir gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_ag/2026-06-27-qwen3-jax-v016-fused-glu-bwd/plugins/profile --profile_start_step 10 --profile_steps 3
```

## Results
- **Avg Throughput**: 66,175 tok/s (2,068 tok/s/chip)
- **Approx MFU**: 11.9%
- **Status**: The run completed 20 steps successfully, but the MFU (11.9%) is a massive regression from both the `v009` baseline (32.5%) and the forward-only `v013` experiment (30.6%).

## Profile
- **Top HLO Ops by Time**: `convolution fusion` (49.07%), `loop fusion` (37.52%), and `fusion` (4.48%). These dominate execution time completely.
- **Step Time**: ~3.96 seconds per step (throughput dropped to 2,068 tok/s/chip).
- **Idle Time**: High host overhead due to dispatching over 2 million microscopic HLO operations per step.

## HLO Dump
- **Custom Kernels**: The `pallas_call` for the SwiGLU backward pass (`dx_kernel` and `dw_kernel`) **failed to compile** to a Mosaic `custom-call`. It silently fell back to `jax.lax.scan` reference ops.
- **Dominant Costs**: The fallback caused the backward pass to unroll into ~2 million individual `convolution fusion` and `loop fusion` nodes. This happened because the `BlockSpec` for the weights (`w_up`, `w_gate`) in the backward pass requested the full `(F, D)` shape in SRAM, which is ~205.5 MB per tensor—massively exceeding the 32 MB VMEM limit of TPU v6e. The `dw_kernel` also requested the full activation sequence (`B, D` = 58.7 MB) in VMEM.

## Verdict
**Falsified**. The hypothesis mechanism never executed on the hardware. The custom Pallas backward kernel violated VMEM constraints and silently fell back to unrolled JAX reference operations, causing a catastrophic HLO explosion and destroying MFU. We need to formulate a new hypothesis that correctly chunks the weight and activation gradients (using proper inner block loops) to fit within the 32 MB VMEM limit.
