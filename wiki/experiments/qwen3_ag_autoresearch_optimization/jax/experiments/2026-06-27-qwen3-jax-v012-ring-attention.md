---
variant: 8B/v6e-8
hypothesis: Ring Attention Pallas kernel
status: completed
created: 2026-06-27
---

# Experiment v012: Ring Attention Pallas kernel

## Hypothesis under test

**Hypothesis**: By implementing Ring Attention (distributing the sequence length dimension across multiple TPU chips), we can radically reduce the peak memory footprint per chip, unlocking the ability to increase batch size or sequence length without running out of HBM.

**Mechanism**: We will replace the standard `splash_attention` with a Ring Attention kernel (referencing implementations from `maxdiffusion` or `haoliuhl/ringattention`). Ring Attention splits the sequence dimension across the TPU mesh, passing KV blocks in a ring topology.

**Predicted signal**: The model will compile and execute with `batch_size=2` at `seqlen=8192` (or higher sequence lengths), pushing MFU beyond the 32.5% single-chip baseline.

**Falsification criterion**: Step time regressions due to sub-optimal Pallas tile sizes or compiler spills, or OOMs/hangs.

## Setup

See launch_cmd in the training workflow.

## Results

The run succeeded with the following configuration and fixes:
1. **2D FSDP**: Sharding the weights across `("fsdp", "sp")` to prevent memory blow-up.
2. **Loss fix**: Removing an `.reshape(-1, v)` in the cross-entropy function that broke the 2D tensor sharding and caused a 9GB all-gather.
3. **Pallas tile sizes**: Reducing the `SPLASH_BQ_DKV`, `SPLASH_BKV_DKV`, and `SPLASH_BKV_DKV_COMPUTE` defaults from 2048 to 1024, preventing a VMEM (SRAM) OOM during the backward pass compilation (`34.96M > 32.00M`).

**Metrics:**
- global_batch: 8
- seqlen: 8192
- avg throughput: 31797 tok/s (3975/chip)
- **MFU**: 22.8% (v6e bf16 peak)

## Verdict

**Status:** Confirmed

The Ring Attention / Pallas Splash attention implementation allows `seqlen=8192` with `batch_size=8` across 4 chips with 2D FSDP (`sp=2`). However, the MFU dropped to 22.8%, which is lower than the previous single-chip baseline. This regression needs to be profiled to understand the communication overhead of `sp=2` and tile size efficiency.


## Next hypotheses

None — TODO: backfill reason


## See also

<!-- TODO: add links -->


## Sources

<!-- TODO: add sources -->
