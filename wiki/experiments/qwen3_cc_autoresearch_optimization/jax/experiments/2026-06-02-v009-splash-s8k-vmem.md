---
title: "Qwen3-8B jax v009 — splash @ seq8192 + scoped-VMEM fix"
type: experiment
hypothesis: qwen3-jax-splash-attention
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-splash-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, splash, remat, seq8192, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v009 — splash @ seq8192 + scoped-VMEM fix

## Hypothesis under test

**Hypothesis**: With the scoped-VMEM cap raised, splash+remat reaches the
program-target seq 8192 (bs=1) — the seq the dense path can't — at MFU > the
seq2048 frontier (25.1%/32.4%). Splash is validated at seq2048/bs4 ([v008](2026-06-02-v008-splash-vmem-bs4.md), 32.4%).

**Mechanism**: `--use_remat --use_splash --batch_size=1 --seqlen=8192` +
`--xla_tpu_scoped_vmem_limit_kib=98304`, image `qwen3-8b-jax:v006-splash`.

**Predicted signal**: no OOM/VMEM at seq8192; loss ~12 stable; MFU > 32.4% (target-shape number).

**Falsification criterion**: OOM/VMEM at seq8192, NaN loss, or MFU ≤ 32.4%.

*(First attempt lost to spot preemption; runner re-submitted — run in progress, ContainerCreating.)*

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
