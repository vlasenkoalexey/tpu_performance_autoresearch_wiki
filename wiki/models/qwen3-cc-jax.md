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
| 8B | v6e-8 | live | 512 ms / 31,955 TPS / 20.5% MFU @ seq2048 bs8 | **1,301 ms / 50,389 TPS / 32.4% MFU @ seq2048 bs32 (remat+splash bs=4)** | 2 | [v008 splash bs4](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-v008-splash-vmem-bs4.md) |

*Climb (seq2048): baseline 20.5% → remat bs2 22.0% (v004) → remat bs3 25.1% (v005) → **remat+splash bs4 32.4%** (v008), **+11.9 pp / +58% tok/s/chip**; MXU 44.6% (≈ MaxText-reference regime). Stable seq2048 config: `--use_remat --use_splash --batch_size=4` + `--xla_tpu_scoped_vmem_limit_kib=98304` on qwen3-8b-jax:v006-splash.*

***Seq-8192 target reached** (v009): splash+remat bs1 seq8192 = **30.4% MFU / 5,305 tok/s/chip** — the program-target seq, which the dense path can't run at all. Best-for-target-seq.*

*tokamax CE: validated numerically correct (v013) but **not** a seq2048 frontier-mover — CE+splash bs6 (v014) = 30.5% < 32.4% (bs4 is the seq2048 occupancy sweet spot; CE is a memory-enabler, overhead not repaid where logits already fit). CE's live value is at seq8192 (larger logits) → next: seq8192+CE+bs2.*

*Baseline captured at seq 2048 (global batch 8). **Cross-lane: jax 20.5% MFU /
3,994 tok/s/chip beats torchax 19.2% / 3,724 (+7.3% tok/s/chip, +1.3 pp)** at the
identical shape — the native-JAX path has lower collective/dispatch overhead
(profile: 21.7% collective vs torchax 31.3%). See the
[jax baseline](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v6e8-baseline.md)
and [torchax baseline](../experiments/qwen3_cc_autoresearch_optimization/torchax/experiments/2026-06-02-qwen3-torchax-v6e8-baseline.md).*

## Cross-variant open hypotheses

Ranked after the [2026-06-02 baseline](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v6e8-baseline.md) (~20% MXU → win occupancy/memory first):

1. [Per-chip batch scaling](../hypotheses/qwen3-jax-batch-scaling.md) — fill MXU occupancy. Effort S — cheapest first move.
2. [Splash attention](../hypotheses/qwen3-jax-splash-attention.md) — GQA-native kernel; avoids `[B,H,S,S]`; prerequisite for seq 8192. Effort M.
3. [tokamax streamed cross-entropy](../hypotheses/qwen3-jax-tokamax-ce.md) — drop `[B,L,V]` logits at the lm_head; unlocks seq 8192. Effort M.

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
