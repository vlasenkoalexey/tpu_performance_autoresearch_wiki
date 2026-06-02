---
title: "Qwen3-8B jax v031 — scan + overlap + CE + bs2 (no offload) @ seq8192"
type: experiment
hypothesis: qwen3-jax-scan-layers
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-scanfull-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, scan, overlap, tokamax-ce, splash, remat, seq8192, bs2, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v031 — scan + overlap + CE + bs2 (no offload) @ seq8192

## Hypothesis under test

**Hypothesis**: v030 showed bs3 regresses (offload host-transfer drag). Isolate batch amortization from the
offload: bs2 fits at seq8192 with streamed CE and **no offload** (v016 proved bs2+CE fits). With scan +
overlap (which v028 showed help at bs1), does **bs2 beat v028 bs1 (5,632 tok/s/chip)**? If yes, batch
amortizes and the v030 drag is the offload (→ pursue lighter offload for bs3); if no, batch genuinely
doesn't amortize → v028 bs1 is the seq8192 ceiling for our stack.

**Mechanism**: image `qwen3-8b-jax:v030-scan-full`. `--use_remat --use_splash --use_scan --use_tokamax_ce
--tokamax_ce_impl=mosaic_tpu --batch_size=2 --seqlen=8192` (NO `--offload_remat`) + 7 sched + 4 overlap.

**Predicted signal**: fits (v016 bs2+CE fit w/o offload); MFU/tok-s-chip vs v028 5,632 and v016 5,139.

**Falsification criterion**: ≤ v028 5,632 → batch doesn't amortize even clean (v028 bs1 is the frontier);
OOM → bs2 needs offload after all.

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
