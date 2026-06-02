---
title: "Qwen3-jax: close the residual seq8192 gap to MaxText (kernel/scheduling)"
type: hypothesis
model: qwen3-cc-jax
variants: ["8B/v6e-8"]
status: open
expected_gain: "up to ~13% (6,030 → 6,942 MaxText) if the dominant bucket transfers"
confidence: low
effort: M
origin: 2026-06-02-v035-maxtext-ce-s8k-bs3
hlo_prefilter: pending
tags: [qwen3-cc, jax, seq8192, mfu-gap, splash, reduce-scatter, mxu, profile-driven]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-jax: close the residual seq8192 gap to MaxText

## Statement

After maxtext-CE cracked the batch wall (v035 bs3 = 34.6% / 6,030), the residual gap to MaxText bs3
(45.3% / 6,942, −13.1%) is **not** memory/batch (bs3 fits) but a scheduling/fusion/kernel-config
difference. Re-tuning the dominant residual bucket (named by the v035 profile-analyzer pass) closes a
measurable fraction of that gap.

## Rationale

v035 shows near-linear bs2→bs3 step scaling (collective not amortizing further) at 86.9% of MaxText.
The [MaxText gap teardown](../analyses/2026-06-02-maxtext-vs-jax-qwen3-8b-mfu-gap.md) attributes MaxText's
edge to MXU occupancy (61.2% vs our ~48%) + async-overlapped reduce-scatter (4.0% vs our higher,
possibly-still-synchronous share) + splash block sizing. The specific lever is **pending the v035
profile-analyzer attribution** — this stub will split into a concrete, falsifiable hypothesis (e.g.
"splash bq/bkv re-tune for bs3", "force reduce-scatter async at bs3", or a VMEM-limit change) once the
dominant bucket is named.

## Proposed experiment

(pending v035 profile attribution — file the concrete flag/block-size change against the named bucket)

## See also

- [Qwen3 8B — jax](../models/qwen3-cc-jax.md) · [MaxText gap teardown](../analyses/2026-06-02-maxtext-vs-jax-qwen3-8b-mfu-gap.md) · [v035](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-v035-maxtext-ce-s8k-bs3.md)
