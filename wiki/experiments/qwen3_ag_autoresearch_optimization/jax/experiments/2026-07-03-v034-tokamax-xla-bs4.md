---
variant: 8B/v6e-8
hypothesis: "In v033, we ran Tokamax xla CE with bs=6 and it OOMed during compilation using 36.59G (exceeded by 5.34G). Since bs=6 exceeded by 5.34G, dropping to bs=4 will reduce the sequence dimension and activation sizes enough to fit within the 31.25 GB HBM limit. At bs=4, Tokamax xla without float32 cast overhead should achieve high throughput and push the MFU past 35%."
commit: 2026-07-03-v034-tokamax-xla-bs4
status: filed
verdict: pending
---

# v034: bs=4 with Tokamax XLA CE (shard_map)

## Hypothesis under test
- **Mechanism**: Use `jax.experimental.shard_map.shard_map` to wrap `tokamax.linear_softmax_cross_entropy_loss` with `implementation='xla'`. Set `bs=4`.
- **Predicted signal**: The model compiles without HBM OOM at bs=4 (global 32) and achieves MFU > 35%.

## Implementation
1. Re-use `v033` codebase/image (`implementation='xla'` without float32 cast).
2. Launch via `xpk` with `batch_size=4` and `seqlen=8192`.

## Results
- **Step time**: 5709ms
- **Throughput**: 45938 tok/s
- **MFU**: 32.9%

## Verdict
**FAILED**. While `bs=4` compiled and avoided OOM, the Tokamax XLA implementation lowered directly to a reference implementation with explicit, un-fused matmuls and elementwise ops. Furthermore, the `shard_map` wrapper failed to partition the sequence dimension, causing the 9.95 GB `[32768, 151936]` logits tensor to be redundantly materialized and computed on every device. The redundant computation kept the MXUs busy (49.6% utilization), but since the redundant FLOPs don't count towards the theoretical model FLOPs, the effective MFU plummeted to 32.9%.


## Next hypotheses

None — TODO: backfill reason


## See also

<!-- TODO: add links -->


## Sources

<!-- TODO: add sources -->
