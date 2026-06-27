---
title: "Qwen3 8B — jax"
type: model
architecture: qwen3-ag
lane: jax
sizes: ["8B"]
hardwares: ["v6e-8"]
tags: [qwen3-ag, jax]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3 8B — jax

Qwen3 8B (`Qwen/Qwen3-8B`) as a native-JAX (Flax NNX) port on **TPU v6e-8**.
**Scaffold only** — the trainer is not yet written. This lane lights up once the
[torchax](qwen3-ag-torchax.md) baseline is stable and a from-scratch JAX port
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
| 8B | v6e-8 | live | 512 ms / 31,955 TPS / 20.5% MFU @ seq2048 bs8 | 1511 ms / 43,300 TPS / 31.0% MFU @ seq8192 bs8 | 1 | [2026-06-26 v004-gradient-checkpointing](../experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-26-qwen3-jax-v004-gradient-checkpointing.md) |

*Baseline captured at seq 2048 (global batch 8). **Cross-lane: jax 20.5% MFU /
3,994 tok/s/chip beats torchax 19.2% / 3,724 (+7.3% tok/s/chip, +1.3 pp)** at the
identical shape — the native-JAX path has lower collective/dispatch overhead
(profile: 21.7% collective vs torchax 31.3%). See the
[jax baseline](../experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v6e8-baseline.md)
and [torchax baseline](../experiments/qwen3_ag_autoresearch_optimization/torchax/experiments/2026-06-02-qwen3-torchax-v6e8-baseline.md).*

## Cross-variant open hypotheses

Ranked after the [2026-06-26 v004-gradient-checkpointing](../experiments/qwen3_ag_autoresearch_optimization/jax/experiments/2026-06-26-qwen3-jax-v004-gradient-checkpointing.md) (31.0% MFU @ 8K context):

1. [Per-chip batch scaling](../hypotheses/qwen3-jax-batch-scaling.md) — fill MXU occupancy at 8K context. Effort S.

## Variant-specific open hypotheses

(none yet)

## Retired hypotheses

1. [Splash attention](../hypotheses/qwen3-jax-splash-attention.md) — GQA-native kernel; avoids `[B,H,S,S]`. Status: **Confirmed** (via `v004-gradient-checkpointing`).
2. [Gradient Checkpointing](../hypotheses/qwen3-jax-gradient-checkpointing.md) — Status: **Confirmed**.
3. [tokamax streamed cross-entropy](../hypotheses/qwen3-jax-tokamax-ce.md) — drop `[B,L,V]` logits at the lm_head. Status: **Blocked** (refuted during compilation due to SDPA OOM).

## Knobs translation matrix

| Technique | 8B/v6e-8 | Notes |
|-----------|----------|-------|
(populated after the lane is implemented)

## Iteration ladder

1. Port Qwen3 8B to native JAX (Flax NNX), matching the torchax baseline number.
2. Apply the MaxText-style XLA flag stack + collective offload.
3. Cross-lane comparison vs the torchax frontier.

## See also

- [Qwen3 8B — torchax](qwen3-ag-torchax.md) — primary lane (live frontier).
- Program: [`../experiments/qwen3_ag_autoresearch_optimization/program.md`](../experiments/qwen3_ag_autoresearch_optimization/program.md)
- Lane README: [`../experiments/qwen3_ag_autoresearch_optimization/jax/README.md`](../experiments/qwen3_ag_autoresearch_optimization/jax/README.md)

## Sources

- `wiki/experiments/qwen3_ag_autoresearch_optimization/jax/` (scaffold).
