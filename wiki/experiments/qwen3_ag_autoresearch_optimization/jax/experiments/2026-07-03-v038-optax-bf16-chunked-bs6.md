---
variant: 8B/v6e-8
hypothesis: "In v037, standard optax natively in bfloat16 OOMed during XLA compilation even at `bs=4`, using 34.03G of 31.25G HBM. This indicates the memory blow-up is caused by XLA's materialization of intermediate buffers during the massive vocabulary reduction (151936 classes) within standard Cross Entropy, regardless of the precision. By chunking the sequence dimension via `jax.lax.scan` into smaller blocks of size 1024 before calculating `optax.softmax_cross_entropy_with_integer_labels`, we can strictly bound the temporary HBM footprint of the CE reduction logic. This should comfortably allow us to scale back up to `bs=6` and finally exceed 35% MFU."
commit: 2026-07-03-v038-optax-bf16-chunked-bs6
status: filed
verdict: pending
---

# v038: bs=6 with Chunked Optax bfloat16 CE

## Hypothesis under test
- **Mechanism**: Chunk the sequence dimension into blocks of `1024` using `jax.lax.scan` to compute `optax.softmax_cross_entropy_with_integer_labels` iteratively, bypassing the XLA massive-reduction buffer blowup at `bs=6`.
- **Predicted signal**: The model compiles without HBM OOM at `bs=6` and achieves MFU > 35%.

## Implementation
1. Copy `v036` codebase.
2. Implement `jax.lax.scan` in `loss_fn` to chunk logits across the sequence dimension.
3. Launch via `xpk` with `batch_size=6` and `seqlen=8192`.

## Results
- **Step time**: N/A
- **Throughput**: N/A
- **MFU**: N/A

## Verdict
**FAILED**. The model OOMed during XLA compilation, using 43.82G out of 31.25G HBM (exceeded by 12.57G). The `jax.lax.scan` chunking logic in the forward pass of `optax.softmax_cross_entropy_with_integer_labels` completely unrolled during XLA's backward pass compilation. This led to an astronomical program space of 43.82G. Chunking CE inside a standard AD graph without a custom VJP (which controls the backward pass materialization) still fails at `bs=6`.


## Next hypotheses

None — TODO: backfill reason


## See also

<!-- TODO: add links -->


## Sources

<!-- TODO: add sources -->
