---
title: "Qwen3-8B jax v035 — MaxText custom_vjp CE @ seq8192 bs3 (climb past bs2)"
type: experiment
hypothesis: qwen3-jax-maxtext-ce
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: jax-maxtext-ce-2026-06-02
status: supported
verdict: supported
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

- **Hardware**: v6e-8 (fsdp=8), image `qwen3-8b-jax:v033-maxtext-ce`. Config = v034 + `--batch_size=3`,
  **NO offload**: `--use_remat --use_splash --use_scan --use_maxtext_ce --batch_size=3 --seqlen=8192` + 7
  scheduler + 4 overlap flags. All four levers active; `[train] starting ... per_chip_batch=3 global_batch=24`.

## Results — bs3 FITS without offload; marginal new frontier

| run | config | tok/s/chip | MFU | steady step (ms) |
|-----|--------|-----------|-----|------------------|
| v034 | maxtext-CE, **bs2** | 5,992 | 34.4% | 2,732 |
| **v035** | maxtext-CE, **bs3** | **6,030** | **34.6%** | 4,075 |
| v030 | tokamax-CE+offload, bs3 | 4,595 | 26.4% | 5,347 |
| MaxText | bs3 reference | 6,942 | 45.3% | 3,546 |

v035 = **+0.6% vs v034 bs2** (+38 tok/s/chip) — a marginal new frontier. Loss 12.0994 → 12.0513
monotone, no NaN/Inf, exit 0. Step 0 compile 34.8 s (cache warm).

**Two findings**: (1) **bs3 fits without offload** — maxtext-CE eliminated the tokamax f32[H,V]
weight-gather (~4.6G) that forced v030 to use offload; bs3 now compiles clean and beats v030's
offloaded bs3 (4,595) by +31%. (2) **Batch amortization has plateaued** — bs2→bs3 is near-linear in
step time (2,732 → 4,075ms ≈ ×1.49 for ×1.5 batch), so the +0.6% is the residual amortization tail.
The seq8192 batch sweet spot is ~bs2–bs3; pushing batch further won't close the MaxText gap.

## Profile

- **Run name**: `2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3` · xprof [`http://localhost:8791/?run=2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3`](http://localhost:8791/?run=2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3) · GCS `.../plugins/profile/2026_06_02_18_05_52/` (steps 12–14). On-disk: [`raw/profiles/2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3/`](../../../../../raw/profiles/2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3/). Profile-analyzer dispatched to attribute the residual MaxText gap (MXU occupancy / reduce-scatter overlap / splash block sizing) — enriched below on return.

## HLO Dump

- **GCS**: `.../2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3/hlo/`. Profile-analyzer to confirm scan 1-body + splash + custom_vjp CE fusion.

## Verdict

**Supported — marginal new seq8192 frontier (34.6% / 6,030, bs3), and a clean structural finding.**
maxtext-CE lets bs3 fit without offload (vs v030's offloaded 4,595) and edges v034 by +0.6%. But batch
amortization is now saturated (near-linear bs2→bs3 step scaling). The remaining gap to MaxText
(6,030 → 6,942, **86.9%**, −13.1%) is **not** a memory/batch ceiling — bs3 fits — but a
scheduling/fusion/kernel-config difference (suspected: MXU occupancy, reduce-scatter overlap quality at
bs3, or splash block sizing not re-tuned for bs3). Profile-analyzer will localize it. **frontier v034 → v035.**

## Next hypotheses

- [Close the residual seq8192 gap to MaxText](../../../../hypotheses/qwen3-jax-seq8192-kernel-gap.md) — re-tune the top residual-gap bucket vs MaxText (splash block size for bs3 / reduce-scatter overlap / MXU occupancy); the specific lever is named by the pending v035 profile-analyzer pass. This is the remaining ~13% to MaxText 6,942.
- [MaxText CE @ seq2048](../../../../hypotheses/qwen3-jax-maxtext-ce-seq2048.md) — re-test the v018 seq2048 frontier (35.8%) with maxtext-CE; CE-backward share is smaller at seq2048 so likely neutral, but cheap to confirm so maxtext-CE becomes the lane's universal default CE.
- bs4 — **deprioritized**: bs2→bs3 already near-linear (amortization saturated); bs4 unlikely to help, risks OOM.

