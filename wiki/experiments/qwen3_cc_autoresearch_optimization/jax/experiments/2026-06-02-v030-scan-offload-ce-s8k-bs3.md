---
title: "Qwen3-8B jax v030 — scan + offload + CE(f32) + bs3 @ seq8192"
type: experiment
hypothesis: qwen3-jax-host-offload-bs3-seq8192
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-scanfull-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, scan, offload, tokamax-ce, overlap, seq8192, bs3, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v030 — scan + offload + CE(f32) + bs3 @ seq8192

## Hypothesis under test

**Hypothesis**: v026 (offload + CE + bs3, NO scan) OOM'd by only **+2.34G**. Adding **scan** — which
compiles 1 layer body instead of 36 unrolled, shrinking the concurrent activation/program footprint — frees
enough HBM to **fit bs3**, and with scan+overlap making collectives cheap (v028), bs3 should amortize toward
MaxText (45.3% / 6,942 tok/s/chip). CE weight stays **f32** (mosaic kernel requires it — v029).

**Mechanism**: image `qwen3-8b-jax:v030-scan-full`. `--use_remat --use_splash --use_scan --offload_remat
--use_tokamax_ce --tokamax_ce_impl=mosaic_tpu --batch_size=3 --seqlen=8192` + 7 scheduler + 4 overlap flags.

**Predicted signal**: bs3 fits (scan frees > +2.34G); loss ~12.07 stable; MFU/tok-s-chip > v028 bs1 (5,632),
toward 6,942.

**Falsification criterion**: still OOM (scan didn't free enough → need vocab-sharded CE or bs2 fallback);
MFU ≤ 5,632 (bs3 doesn't amortize even with scan+overlap → v028 bs1 is the seq8192 frontier).

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
