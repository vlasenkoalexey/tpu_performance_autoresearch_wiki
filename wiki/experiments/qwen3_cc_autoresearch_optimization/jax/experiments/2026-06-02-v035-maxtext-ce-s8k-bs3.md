---
title: "Qwen3-8B jax v035 — MaxText custom_vjp CE @ seq8192 bs3 (climb past bs2)"
type: experiment
hypothesis: qwen3-jax-maxtext-ce
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-maxtext-ce-2026-06-02
status: in_progress
tags: [qwen3-cc, jax, cross-entropy, maxtext, custom-vjp, scan, overlap, splash, remat, seq8192, bs3, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax v035 — MaxText custom_vjp CE @ seq8192 bs3

## Hypothesis under test

**Hypothesis**: v034 showed maxtext-CE makes batch amortize at seq8192 (bs2 5,992 > bs1 5,632). If the
trend continues, **bs3 beats bs2 (5,992)** toward MaxText (6,942, bs3). Also: maxtext-CE drops the
~4.6G tokamax f32[H,V] lm_head-weight all-gather that forced v030 to use offload, so bs3 may now **fit
without offload**.

**Mechanism**: image `qwen3-8b-jax:v033-maxtext-ce`. `--use_remat --use_splash --use_scan
--use_maxtext_ce --batch_size=3 --seqlen=8192` + 7 scheduler + 4 overlap flags. NO offload.

**Predicted signal**: fits (no tokamax weight wall); bs3 tok/s/chip vs v034 bs2 (5,992) and MaxText (6,942).

**Falsification criterion**: OOM (bs3 still over budget without offload → try +offload or stay at bs2);
≤ v034 5,992 (bs3 doesn't amortize past bs2 → v034 is the frontier).

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
