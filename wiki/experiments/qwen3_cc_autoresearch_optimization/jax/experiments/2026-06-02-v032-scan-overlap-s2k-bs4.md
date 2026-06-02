---
title: "Qwen3-8B jax v032 — scan + overlap @ seq2048 bs4 (lift the v018 frontier)"
type: experiment
hypothesis: qwen3-jax-scan-layers
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-scanfull-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, scan, overlap, splash, remat, seq2048, bs4, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v032 — scan + overlap @ seq2048 bs4

## Hypothesis under test

**Hypothesis**: scan + the overlap flags lifted the seq8192 frontier (v028, +6.2%); applying the same to
the **seq2048** frontier (v018, 35.8% / 6,964 tok/s/chip) should similarly improve it toward MaxText's
seq2048 (38.0% / 7,116) — a quick win on the shape where we're already near parity (97.9%).

**Mechanism**: image `qwen3-8b-jax:v030-scan-full`. v018 frontier shape + scan + overlap:
`--use_remat --use_splash --use_scan --batch_size=4 --seqlen=2048` (no offload, no CE — plain CE fits at
seq2048 bs4 like v018) + 7 scheduler + 4 overlap flags.

**Predicted signal**: MFU/tok-s-chip > v018 35.8% / 6,964, toward MaxText 7,116; loss parity; exit 0.

**Falsification criterion**: ≤ v018 6,964 beyond noise (scan/overlap don't help at seq2048 — its
collectives are already a smaller share at the shorter seq, so less to overlap).

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
