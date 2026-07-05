---
variant: 8B/v6e-8
hypothesis: Fuse gate_proj and up_proj into a single gate_up_proj, and q, k, v into qkv_proj, to increase the M_N_K sizes of the matmuls, combating the shape penalty caused by TP=2 halving dimensions.
commit: 2026-06-27-v022-tp2-gate-up-fusion
status: filed
verdict: pending
---

# v022: Fused gate_up_proj and qkv_proj in TP=2

## Hypothesis under test
- **Mechanism**: Fusing `gate_proj` and `up_proj` linear layers into a single `gate_up_proj` (size `[4096, 12288]` before sharding) and fusing `q_proj`, `k_proj`, `v_proj` into `qkv_proj` (size `[4096, 6144]`). 
- **Predicted signal**: MXU utilization rises, step time drops due to fewer matmuls with larger dimension sizes, addressing the memory-bandwidth constraint introduced by `TP=2`. MFU should recover from 22.9%.

## Implementation
1. Copied `.repo/2026-06-27-v021-tp2` into `.repo/2026-06-27-v022-tp2-gate-up-fusion`.
2. Modified `model/modeling_qwen3.py` to replace `gate` and `up` with `gate_up_proj`, and `q`, `k`, `v` with `qkv_proj`.
3. Updated `model/sharding.py` to correctly map the fused weights.

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
