---
title: "Qwen3-8B jax v008 — splash bs=4 + scoped-VMEM fix"
type: experiment
hypothesis: qwen3-jax-splash-attention
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-splash-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, splash, remat, vmem, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v008 — splash bs=4 + scoped-VMEM fix

## Hypothesis under test

**Hypothesis**: Raising the scoped-VMEM cap clears the 2.15 M overrun that crashed
[v006](2026-06-02-v006-splash-bs4.md)'s splash backward kernel, letting splash+remat+bs=4
run — and (since splash already cleared the HBM wall) it beats the remat-only frontier (25.1%).

**Mechanism**: Same as v006 (`--use_remat --use_splash --batch_size=4`, image
`qwen3-8b-jax:v006-splash`) **plus** `LIBTPU_INIT_ARGS=--xla_tpu_scoped_vmem_limit_kib=98304`
(raises the splash-backward Pallas stack limit from 32 M → 96 M). Flag-only.

**Predicted signal**: no VMEM OOM; **loss ~12 stable** (first chance to verify splash
numerical correctness); MFU > 25.1% (bs=4 occupancy on top of splash).

**Falsification criterion**: still VMEM-OOM (need smaller dkv blocks instead), NaN
loss (splash mis-wired), or MFU ≤ 25.1%.

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
