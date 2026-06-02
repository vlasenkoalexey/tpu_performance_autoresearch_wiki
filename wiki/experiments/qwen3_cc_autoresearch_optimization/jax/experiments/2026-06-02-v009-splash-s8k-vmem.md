---
title: "Qwen3-8B jax v009 — splash @ seq8192 + scoped-VMEM fix"
type: experiment
hypothesis: qwen3-jax-splash-attention
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-splash-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, splash, remat, seq8192, vmem, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v009 — splash @ seq8192 + scoped-VMEM fix

## Hypothesis under test

**Hypothesis**: With the scoped-VMEM cap raised (the v007 fix), splash+remat reaches
the **program-target seq 8192** (bs=1) that the dense path can't, at sane loss and
MFU > the 25.1% seq2048 frontier.

**Mechanism**: v007 config + `LIBTPU_INIT_ARGS=--xla_tpu_scoped_vmem_limit_kib=98304`
(clears the 988 K splash-backward overrun). `--use_remat --use_splash --batch_size=1
--seqlen=8192`, image `qwen3-8b-jax:v006-splash`.

**Predicted signal**: no VMEM OOM; loss ~12 stable (splash correctness at long seq);
MFU at seq8192 > 25.1%.

**Falsification criterion**: still VMEM-OOM (shrink dkv blocks next), NaN loss, or MFU ≤ 25.1%.

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
