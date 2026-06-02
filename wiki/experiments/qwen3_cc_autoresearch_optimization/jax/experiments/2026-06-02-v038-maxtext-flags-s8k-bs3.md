---
title: "Qwen3-8B jax v038 — MaxText XLA flag superset @ seq8192 bs3 (flags-only probe)"
type: experiment
hypothesis: qwen3-jax-xla-flag-stack
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-maxtext-ce-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, libtpu-xla-flags, maxtext, scan, splash, remat, seq8192, bs3, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v038 — MaxText XLA flag superset @ seq8192 bs3

## Hypothesis under test

**Hypothesis**: adding the ~9 XLA flags MaxText uses that we lack — LAYOUT_FOR_ALL_REDUCE_SCATTER (3),
DATA_PARALLEL_OVERLAP (2), CF_FOR_ALL_GATHER extras (2), HOST_OFFLOAD extras incl the `*_in_chain` flags (4)
— to the v035 frontier (no offload, no code change) is neutral-or-better and, crucially, **validates that
these flags are accepted by our libtpu build** before they're combined with the offload recipe (v039).

**Mechanism**: image `qwen3-8b-jax:v033-maxtext-ce`, v035 config (`--use_remat --use_splash --use_scan
--use_maxtext_ce --batch_size=3 --seqlen=8192`) + existing 12-flag bundle + the 11 new MaxText flags.

**Predicted signal**: compiles clean (all flags valid); tok/s/chip ≥ v035 6,030 (the RS-layout / DP-overlap
flags may help reduce-scatter; the offload-pipelining flags are likely no-ops without offload).

**Falsification criterion**: a flag is rejected (5 s crash → report the name, prune for v039); or < 6,030
beyond noise (a flag regresses → ablate).

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
