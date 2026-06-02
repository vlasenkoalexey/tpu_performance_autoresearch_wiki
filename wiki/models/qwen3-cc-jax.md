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
| 8B | v6e-8 | open | — (lane not yet implemented) | — | 0 | — |

## Cross-variant open hypotheses

(none yet — lane not implemented; the first "hypothesis" is the port itself)

## Variant-specific open hypotheses

(none yet)

## Retired hypotheses

(none yet)

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
- Program: [`../experiments/qwen3_cc_autoresearch_optimization/program.md`](../experiments/qwen3_cc_autoresearch_optimization/program.md)
- Lane README: [`../experiments/qwen3_cc_autoresearch_optimization/jax/README.md`](../experiments/qwen3_cc_autoresearch_optimization/jax/README.md)

## Sources

- `wiki/experiments/qwen3_cc_autoresearch_optimization/jax/` (scaffold).
