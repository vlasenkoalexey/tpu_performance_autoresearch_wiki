# 2026-06-27-qwen3-jax-v017-fused-glu-tiled-bwd

## Objective
Implementing a full custom Pallas backward kernel for Fused GLU (SwiGLU) with proper chunking/tiling using BlockSpec to fit within VMEM. This will eliminate the HBM materialization overhead observed in v013 and the Pallas reference-op fallback observed in v016, increasing overall step MFU beyond the v009 baseline of 32.5%.

## Hypothesis
In v016, the custom backward Pallas kernel requested the full (F, D) shape in SRAM, which exceeded the TPU v6e VMEM limit. This caused a silent fallback to jax.vmap reference ops, exploding into millions of microscopic operations and destroying performance (11.9% MFU). For v017, we rewrite the custom backward Pallas kernel to correctly tile/chunk the weights and activations using BlockSpec and an inner block loop so the kernel can compile to Mosaic and execute efficiently on the TPU.

## Falsification Criterion
Step MFU does not exceed 32.5% or the implementation fails numerical equivalence.

## Result

- **Status**: Crashed (Compile OOM)

## Profile
- **Compile OOM**: The workload crashed during `train_step` JIT compilation.
- **Error**: `jax.errors.JaxRuntimeError: RESOURCE_EXHAUSTED: XLA:TPU compile permanent error. Ran out of memory in memory space hbm. Used 166.08G of 31.25G hbm. Exceeded hbm capacity by 134.83G.`

## HLO Dump
- **Cause**: In `fused_glu.py`, the `dx_kernel` and `dw_kernel` correctly chunked the block shapes to fit in VMEM, but the reduction dimension (`num_f` and `num_b`) was placed in the `pallas_call` grid with `dimension_semantics='arbitrary'`. 
- **Consequence**: Pallas maps grid reductions to massive HBM buffers (`num_f` separate tensors of size `[B, D]` = 3.28 GB per layer), and then inserts an external XLA reduction. For 28 layers, this required ~92 GB of HBM buffers, causing XLA to crash during compilation.

## Verdict
**Falsified**. The implementation traded a VMEM OOM for an HBM compile-time OOM. Pallas `grid` reductions cannot be used for large reduction dimensions because they materialize the intermediate grid outputs into HBM. A successful custom backward kernel must implement the reduction loop *inside* the kernel (e.g., using `jax.lax.fori_loop` or `pl.dot`) to accumulate gradients purely in SRAM before writing the final output block to HBM.


## Next hypotheses

None — TODO: backfill reason


## See also

<!-- TODO: add links -->


## Sources

<!-- TODO: add sources -->
