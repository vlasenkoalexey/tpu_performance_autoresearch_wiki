---
variant: 8B/v6e-8
hypothesis: "By applying the `checkpoint_dots_with_no_batch_dims_saveable` policy to the layer-wise `nnx.remat` at `global_batch=8` (bs=1), we can avoid recomputing the dense dot products (qkv, gate_up, down, o projections) during the backward pass. Since `bs=1` keeps the saved dot-product inputs comfortably within the 31.25 GB HBM limit (~22 GB total memory), this will slash the recomputation FLOPs by 33%, dropping step time by up to 25% and pushing the calculated MFU from 32.8% to over 40%."
commit: 2026-06-27-v026-unfused-bs8-checkpoint-dots
status: filed
verdict: pending
---

# v026: Unfused Layers, bs=1, Checkpoint Dots Policy

## Hypothesis under test
- **Mechanism**: In `v025`, we achieved 32.8% MFU with `bs=2` (global 16) but were compute bound. To increase MFU, we can reduce the recomputation overhead of `nnx.remat` by saving the inputs to the dot products, thereby avoiding recomputing them in the backward pass. We use `policy=jax.checkpoint_policies.dots_with_no_batch_dims_saveable` inside `model/modeling_qwen3.py`. Since saving the dot inputs takes ~13.8 GB at `bs=1`, we reduce batch size from 2 to 1 to stay within the 31.25 GB HBM limit.
- **Predicted signal**: The model compiles without OOM and step time drops significantly compared to `v020` (which had `bs=1` and `1455ms` step time). MFU exceeds 35%.

## Implementation
1. Re-use `v025` codebase.
2. Edit `model/modeling_qwen3.py` to add `policy=checkpoint_policies.dots_with_no_batch_dims_saveable` to the `jax.checkpoint` wrapper inside `Qwen3ScannedLayers.__call__`.
3. Launch with `batch_size=1` (global_batch=8).

## Results
- **Step time**:
- **Throughput**:
- **MFU**:

## Verdict
**PENDING**. 


## Next hypotheses

None — TODO: backfill reason


## See also

<!-- TODO: add links -->


## Sources

<!-- TODO: add sources -->
