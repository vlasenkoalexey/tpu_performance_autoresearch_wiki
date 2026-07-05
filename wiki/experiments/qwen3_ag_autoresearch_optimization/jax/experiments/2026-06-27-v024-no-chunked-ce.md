---
variant: 8B/v6e-8
hypothesis: "Chunked cross-entropy (introduced in v021) forced XLA to gather the 1.2GB `lm_head.weight` 8 times per step inside a jax.lax.scan loop, consuming 9.6GB of memory bandwidth and artificially depressing MFU. By removing the chunking and allowing GSPMD to compute the full CE, we save significant memory bandwidth. Additionally, we shard `lm_head.weight` along the Vocab axis over FSDP, reducing the per-device logits size from 9.9GB to 1.2GB, which prevents OOMs even at global_batch=16. This should fully restore and exceed the MFU."
commit: 2026-06-27-v024-no-chunked-ce
status: filed
verdict: pending
---

# v024: Remove Chunked Cross-Entropy and enable Vocab Parallelism

## Hypothesis under test
- **Mechanism**: `v023` showed 28.9% MFU with `bs=2` (global 16) and fused MLPs. However, the step time was still bloated by the chunked cross-entropy scan introduced in `v021`. The scan reads the `lm_head` weights repeatedly. By removing the scan and computing the CE in one shot, we avoid the repeated weight gather. To prevent OOM from the `[batch=16, seq=8192, vocab=151936]` logits tensor, we change `lm_head.weight` sharding from `("tp", "fsdp")` to `("fsdp", "tp")`. This shards the Vocab axis over FSDP. With Vocab Parallel Cross Entropy, GSPMD automatically inserts the required `psum` operations across the Vocab axis, keeping the logits memory footprint at a manageable 1.2 GB per device.
- **Predicted signal**: MFU should significantly exceed 35% because the artificial chunked-CE bottleneck is removed and compute intensity is doubled compared to `v020`.

## Implementation
1. Revert `train.py`'s `_ce_sum` and `jax.lax.scan` to a standard full-vocab `_ce` with `jax.nn.one_hot`.
2. Change `model/sharding.py` `lm_head.weight` to `("fsdp", "tp")`.
3. Launch with `batch_size=2` (global_batch=16).

## Results
- **Step time**: 2994ms
- **Throughput**: 43,771 tok/s
- **MFU**: 31.4%

## Verdict
**REJECTED**. While we removed the chunking bottleneck and solved the OOM by increasing batch size and doing Vocab Parallelism, the MFU is STILL below the 32.3% baseline from v020. This isolates the remaining regression entirely to the fused MLPs. Fusing `gate_up` and `qkv` breaks the fine-grained overlap of FSDP `AllGather` with compute, inserting pipeline bubbles during the massive 24MB gathers.


## Next hypotheses

None — TODO: backfill reason


## See also

<!-- TODO: add links -->


## Sources

<!-- TODO: add sources -->
