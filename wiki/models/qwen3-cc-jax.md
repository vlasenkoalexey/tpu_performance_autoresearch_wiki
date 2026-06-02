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
| 8B | v6e-8 | live | 512 ms / 31,955 TPS / 20.5% MFU @ seq2048 bs8 | **1,154 ms / 56,782 TPS / 35.8% MFU @ seq2048 bs32 (remat+splash+XLA-flag-stack bs=4)** | 3 | [v018 XLA flag stack](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-v018-xla-flag-stack.md) |

*Climb (seq2048): baseline 20.5% → remat bs2 22.0% (v004) → remat bs3 25.1% (v005) → remat+splash bs4 32.4% (v008) → **+MaxText HOST_OFFLOAD XLA flag stack 35.8%** (v018), **+15.3 pp / +74% tok/s/chip**. Stable seq2048 config: `--use_remat --use_splash --batch_size=4` + `LIBTPU_INIT_ARGS` = scoped-vmem(98304) + the 7-flag scheduler bundle (all_experimental_scheduler_features, scheduler_memory_pressure_tracking, ag_backward_pipelining, host_transfer_overlap_limit=24, scheduler_percent_shared_memory_limit=100, latency_hiding_scheduler_rerun=2, max_concurrent_host_send_recv=100), on qwen3-8b-jax:v006-splash. (Note: `xla_jf_spmd_threshold_for_windowed_einsum_mib` is invalid on this XLA build — v019 — and is NOT part of the config; the +3.4 pp is from the 7 scheduler flags.) Remaining gap to llama3-jax sibling (43.3%): ~7.5 pp.*

***Seq-8192 target reached** (v009): splash+remat bs1 seq8192 = **30.4% MFU / 5,305 tok/s/chip** — the program-target seq, which the dense path can't run at all. Best-for-target-seq.*

> [!warning] Seq8192 frontier REOPENED by the MaxText reference (2026-06-02)
> The [MaxText Qwen3-8B reference](qwen3-cc-maxtext.md) measured **45.3% MFU / 6,942 tok/s/chip @ seq8192 bs3** — **+31% tok/s/chip** over v009. The jax seq8192 frontier (30.4%, bs1) is **~15 pp below the achievable ceiling**. MaxText fits bs3 via **host-offload of the decoder-layer input + QKV/out projections** (`decoder_layer_input`+`*_proj=offload`) — a lever the jax lane never tried (remat alone capped us at bs1; CE enabled bs2 without throughput gain). New open hyp: [host-offload bs3 @ seq8192](../hypotheses/qwen3-jax-host-offload-bs3-seq8192.md). The "jax at ceiling" conclusion holds for **seq2048** but is **superseded for seq8192**.

*tokamax CE: validated numerically correct (v013) but **not** a seq2048 frontier-mover — CE+splash bs6 (v014) = 30.5% < 32.4% (bs4 is the seq2048 occupancy sweet spot; CE is a memory-enabler, overhead not repaid where logits already fit). CE's live value is at seq8192 (larger logits) → next: seq8192+CE+bs2.*

*Baseline captured at seq 2048 (global batch 8). **Cross-lane: jax 20.5% MFU /
3,994 tok/s/chip beats torchax 19.2% / 3,724 (+7.3% tok/s/chip, +1.3 pp)** at the
identical shape — the native-JAX path has lower collective/dispatch overhead
(profile: 21.7% collective vs torchax 31.3%). See the
[jax baseline](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-qwen3-jax-v6e8-baseline.md)
and [torchax baseline](../experiments/qwen3_cc_autoresearch_optimization/torchax/experiments/2026-06-02-qwen3-torchax-v6e8-baseline.md).*

## Cross-variant open hypotheses

Re-ranked after [v018](../experiments/qwen3_cc_autoresearch_optimization/jax/experiments/2026-06-02-v018-xla-flag-stack.md) (XLA flag stack SUPPORTED, new frontier 35.8%; batch/CE/SparseCore closed). The XLA flag stack is now part of the frontier config — remaining open levers stack on it:

1. [Async collective fusion](../hypotheses/qwen3-jax-async-collective-fusion.md) — overlap the synchronous FSDP grad reduce-scatter (v018 profile: 12.9% of step, the #1 non-matmul cost) with bwd compute. Analyzer estimate **+7–13 pp**. Effort S, flag-only. Overlap (transferable category), not offload. **In flight (v023).**
2. [scan-over-layers](../hypotheses/qwen3-jax-scan-layers.md) — structural/compiler lever; **profile says NOT the dominant bottleneck** (train step fully unrolled, but the cost is runtime collective/kernel/HBM). Worth testing as a compile-time/scheduling lever; low MFU prior. Effort M.
3. [AMP fp32-master / bf16-compute](../hypotheses/qwen3-jax-amp-mixed-precision.md) — **deprioritized**: trainer already full-bf16; true AMP adds fp32 master (~+16 GB → OOM risk at bs4), matmuls stay bf16, so quality lever (SCHEMA rule 8) not MFU. Effort M.

Profile-driven (v018 frontier, profile-analyzer): NOT matmul-bound (MXU 48.3%, 48.6% non-matmul). Top non-matmul = grad reduce-scatter 12.9% (→ async fusion, #1), splash 12.3%, loop-fusion/norms 11.0% (HBM-bound). QK-norm+RoPE already XLA-fused (custom kernel → xla-already-fuses; deprioritized).

Validated this lane: [XLA flag stack](../hypotheses/qwen3-jax-xla-flag-stack.md) (**supported** seq2048 +3.4 pp / v018; **neutral seq8192** / v019). Retired kernel-swap levers: tokamax-splash (v020 −8.5%), splash-block-tuning (v021/v022 neutral). Catalogued: fused QK-norm+RoPE kernel (deprioritized), seq16384, XLA flag-ablation.

Also catalogued (not yet filed as pages): scan-over-layers (compile-HBM), fused QK-norm+RoPE Pallas kernel (Qwen3-specific), seq16384 (splash scale).

## Variant-specific open hypotheses

(none yet)

## Retired hypotheses

- [Per-chip batch scaling](../hypotheses/qwen3-jax-batch-scaling.md) — **refuted** for 8B/v6e-8 (v001/v002 compile-OOM on the dense path; subsumed by remat, which is now the baseline).
- [tokamax streamed cross-entropy](../hypotheses/qwen3-jax-tokamax-ce.md) — **refuted** for 8B/v6e-8 (v013 correct, but v014 seq2048 = 30.5% and v016 seq8192 = 29.5%, both below the splash frontier; memory enabler, not a throughput lever).
- [SparseCore collective-offload](../hypotheses/qwen3-jax-sparsecore-offload.md) — **refuted** for 8B/v6e-8 at every shape (v003 bs1 −4 pp, v017 bs4 −0.7 pp; collective share already low at 6.3%).

## Knobs translation matrix

| Technique | 8B/v6e-8 | Notes |
|-----------|----------|-------|
(populated after the lane is implemented)

## Iteration ladder

1. Port Qwen3 8B to native JAX (Flax NNX), matching the torchax baseline number.
2. Apply the MaxText-style XLA flag stack + collective offload.
3. Cross-lane comparison vs the torchax frontier.

## See also

- [Qwen3 8B — maxtext](qwen3-cc-maxtext.md) — reference-ceiling lane (MaxText `qwen3-8b.yml`; reference run dispatched 2026-06-02).
- [Qwen3 8B — torchax](qwen3-cc-torchax.md) — primary lane (live frontier).
- Program: [`../experiments/qwen3_cc_autoresearch_optimization/program.md`](../experiments/qwen3_cc_autoresearch_optimization/program.md)
- Lane README: [`../experiments/qwen3_cc_autoresearch_optimization/jax/README.md`](../experiments/qwen3_cc_autoresearch_optimization/jax/README.md)

## Sources

- `wiki/experiments/qwen3_cc_autoresearch_optimization/jax/` (scaffold).
