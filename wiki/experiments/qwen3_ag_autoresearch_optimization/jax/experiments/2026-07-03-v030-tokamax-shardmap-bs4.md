---
variant: 8B/v6e-8
hypothesis: "The dense XLA cross-entropy loss materializes the entire [B, L, V] logits tensor in HBM during the backward pass (for bs=4, 8192 seqlen, 151936 vocab, this is ~9.27 GB). This massive buffer prevents global batch size 32 (bs=4) from fitting within the 31.25 GB HBM limit. By replacing the default CE with Tokamax's Pallas CE kernel wrapped in `shard_map` (manual vocab parallelism), we bypass materializing the dense logits and operate directly on the `fsdp` sharded weights, lowering HBM usage to fit bs=4 and pushing MFU past 35%."
commit: 2026-07-03-v030-tokamax-shardmap-bs4
status: filed
verdict: pending
---

# v030: bs=4 with Tokamax Pallas CE (shard_map)

## Hypothesis under test
- **Mechanism**: Use `jax.experimental.shard_map.shard_map` to wrap `tokamax.linear_softmax_cross_entropy_loss` with `implementation='mosaic_tpu'`. This eliminates the 9.27 GB dense logit allocation.
- **Predicted signal**: The model compiles without HBM OOM at bs=4 (global 32) and achieves MFU > 35%.

## Implementation
1. Re-use `v029` codebase but edit `train.py` to bypass `lm_head` and use Tokamax CE inside `shard_map`.
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
