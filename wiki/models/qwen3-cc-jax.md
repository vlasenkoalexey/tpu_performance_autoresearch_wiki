---
title: "Qwen3 8B — jax"
type: model
architecture: qwen3-cc
lane: jax
sizes: ["8B"]
hardwares: ["v6e-8"]
tags: [qwen3-cc, jax]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3 8B — jax

Qwen3 8B (`Qwen/Qwen3-8B`) as a native-JAX (Flax NNX) port on **TPU v6e-8**.
**Scaffold only** — the trainer is not yet written. This lane lights up once the
[torchax](qwen3-cc-torchax.md) baseline is stable and a from-scratch JAX port
becomes a ranked hypothesis; it then serves as the reference ceiling for
cross-lane comparison.

## Target metrics

- Primary: MFU at seq_len=8192 (v6e bf16 peak ≈ 918 TFLOPS/chip).
- Secondary: tokens/sec (and tok/s/chip), step time, peak HBM.

## How to run

```
TODO: native-JAX trainer not yet written.
```

## Variant matrix

| Size | Hardware | Status | Baseline (step / TPS / MFU) | Current best (step / TPS / MFU) | Open hyps | Frontier exp |
|------|----------|--------|-----------------------------|----------------------------------|-----------|--------------|
| 8B | v6e-8 | live | 512 ms / 31,955 TPS / 20.5% MFU @ seq2048 bs8 | 4077.5 ms / 48,218 TPS / 34.6% MFU @ seq8192 bs24 | 2 | [2026-06-02 v036](../experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v036-sc-bs3.md) |

*Baseline captured at seq 2048 (global batch 8). **Current frontier runs at seq 8192 (global batch 24) on v6e-8, climbing to 34.6% MFU / 6,027 tok/s/chip** via Splash attention, layer-scan, selective remat, and custom cross-entropy. See [v033b](../experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v033b-maxtext-ce-s8k-bs1.md), [v034](../experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v034-maxtext-ce-s8k-bs2.md), [v035](../experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3.md), and [v036](../experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v036-sc-bs3.md).*

## Cross-variant open hypotheses

Ranked after the [2026-06-02 v036](../experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v036-sc-bs3.md):

1. [Per-chip batch scaling](../hypotheses/qwen3-jax-batch-scaling.md) — scale to bs=4 to find the OOM limit. Effort S.
2. [Selective SparseCore offload](../hypotheses/qwen3-jax-selective-sparsecore-offload.md) — selectively offload FSDP collectives to minimize transfer overhead. Effort S.

## Variant-specific open hypotheses

(none yet)

## Retired hypotheses

- [SparseCore collective offload](../hypotheses/qwen3-jax-sparsecore-offload.md) — Refuted by [2026-06-02 v036](../experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v036-sc-bs3.md). Offloading all collectives slightly degraded step time (+0.6%) due to SC-TC memory transfer/PCIe overhead.

## Knobs translation matrix

| Technique | 8B/v6e-8 | Notes |
|-----------|----------|-------|
(populated after the lane is implemented)

## Iteration ladder

1. Port Qwen3 8B to native JAX (Flax NNX), matching the torchax baseline number.
2. Apply the MaxText-style XLA flag stack + collective offload.
3. Cross-lane comparison vs the torchax frontier.

## See also

- [Qwen3 8B — torchax](qwen3-cc-torchax.md) — primary lane (live frontier).
- Program: [`../experiments/qwen3_ag_autoresearch_optimization/program.md`](../experiments/qwen3_ag_autoresearch_optimization/program.md)
- Lane README: [`../experiments/qwen3_ag_autoresearch_optimization/jax/README.md`](../experiments/qwen3_ag_autoresearch_optimization/jax/README.md)

## Sources

- `wiki/experiments/qwen3_ag_autoresearch_optimization/jax/` (scaffold).
