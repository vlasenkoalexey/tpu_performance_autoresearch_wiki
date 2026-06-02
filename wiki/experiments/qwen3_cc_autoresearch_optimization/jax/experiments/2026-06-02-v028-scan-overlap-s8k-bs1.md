---
title: "Qwen3-8B jax v028 — scan-over-layers + collective-overlap flags @ seq8192 bs1"
type: experiment
hypothesis: qwen3-jax-scan-layers
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-scan-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, scan, collective-overlap, splash, remat, seq8192, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v028 — scan + collective-overlap @ seq8192 bs1

## Hypothesis under test

**Hypothesis**: `nnx`/`lax.scan` over the 36 decoder layers (stacked-param storage; 1 compiled body)
gives the XLA scheduler the structure to **overlap the FSDP reduce-scatter** (the v018 profile's #1
non-matmul cost: 12.9% synchronous) — productive *only* on the scanned graph (the same async-collective-
fusion flags REGRESSED on the unrolled graph, [v023](2026-06-02-v023-async-collective-fusion.md)). Tested at
the bs1 seq8192 shape (fits, = v009) to isolate the scan+overlap benefit before scaling to bs3.

**Mechanism**: image `qwen3-8b-jax:v028-scan` (scan refactor — stacked layers via vmap-init + lax.scan;
CPU equivalence PASS, scan↔unrolled fwd/grad parity to 1e-6). Launch `--use_remat --use_splash --use_scan
--batch_size=1 --seqlen=8192` + the v018 7 scheduler flags + the 4 async-collective-fusion overlap flags.

**Predicted signal**: MFU > v009 30.4% / v019 30.7% (scan enables RS overlap → recover part of the 12.9%);
loss ~12.07 stable; exit 0. This is the scan-isolation step; the MaxText 45.3% target needs bs3 (next).

**Falsification criterion**: MFU ≤ 30.7% beyond noise (scan + overlap flags don't help at bs1 either —
would mean the seq8192 win genuinely needs bs3, not just scan).

## Setup
(populated on completion)
## Results
(populated on completion)
## Profile
(populated on completion)
## HLO Dump
(populated on completion)
## Verdict
(populated on completion)

## Next hypotheses
(populated on completion)
