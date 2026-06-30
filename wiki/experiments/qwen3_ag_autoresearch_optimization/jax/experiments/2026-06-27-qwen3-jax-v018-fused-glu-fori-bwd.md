# 2026-06-27-qwen3-jax-v018-fused-glu-fori-bwd

## Objective
Fix the Compile OOM from `v017` by implementing the reduction dimension inside the custom Pallas backward kernel (using `jax.lax.fori_loop` or `pl.dot`) to accumulate gradients in fast SRAM, avoiding Pallas grid reduction HBM materialization.

## Hypothesis
In `v017`, we successfully tiled the blocks to fit within VMEM, but mapped the reduction dimension to the Pallas `grid`. Pallas grid reductions materialize massive intermediate buffers in HBM, causing a 166 GB compile-time OOM. By moving the reduction logic into an explicit loop *inside* the Pallas kernel (using `jax.lax.fori_loop`), we will accumulate gradients purely in SRAM and only write the final output blocks to HBM, fitting within the 31.25 GB limit and achieving the MFU gain intended by the custom backward pass.

## Falsification Criterion
Compile OOM or step MFU does not exceed the `v009` baseline of 32.5%.
