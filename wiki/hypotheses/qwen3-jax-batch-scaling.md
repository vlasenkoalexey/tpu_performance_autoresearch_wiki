---
title: "Qwen3 jax — per-chip batch scaling"
type: hypothesis
model: qwen3-cc-jax
variants: ["8B/v6e-8"]
status: open
expected_gain: "1.5-2.5x throughput / MFU"
confidence: high
effort: S
origin: 2026-06-02-qwen3-jax-v6e8-baseline
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3 jax — per-chip batch scaling

*Hypothesis*: Raising `--batch_size` (per-chip batch > 1) lifts MXU occupancy
above the baseline 19.9% with no code change, until HBM (Adam state +
activations + `[B,L,V]` logits) binds.

*Mechanism*: The [baseline](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v6e8-baseline.md)
ran per-chip batch 1 (global 8 on fsdp=8) at ~20% MXU. More work per step
amortizes fixed per-step overhead (collectives + dispatch).

*Falsification criterion*: throughput/chip does not rise with batch, or OOM
before any gain → refuted.
