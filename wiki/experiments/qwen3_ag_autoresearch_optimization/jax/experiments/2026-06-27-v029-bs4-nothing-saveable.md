---
variant: 8B/v6e-8
hypothesis: "By explicitly setting `policy=jax.checkpoint_policies.nothing_saveable` in the `jax.checkpoint` wrapper for `layer_fn`, we prevent JAX from saving intermediate activations inside the layer for the backward pass. This maximizes recomputation but minimizes memory usage, potentially allowing `bs=4` (global 32) to compile and fit within the 31.25GB HBM limit. If `bs=4` fits, the increased arithmetic intensity should amortize communication overhead and push the MFU over 35%."
commit: 2026-06-27-v029-bs4-nothing-saveable
status: filed
verdict: pending
---

# v029: bs=4 with nothing_saveable policy

## Hypothesis under test
- **Mechanism**: Use `jax.checkpoint_policies.nothing_saveable` for layer checkpointing, and launch with `bs=4` (global 32).
- **Predicted signal**: The model compiles without OOM and achieves an MFU > 35%.

## Implementation
1. Re-use `v025` codebase but modify `modeling_qwen3.py` to use `policy=jax.checkpoint_policies.nothing_saveable`.
2. Launch via `xpk` with `batch_size=4` and `seqlen=8192`.

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
