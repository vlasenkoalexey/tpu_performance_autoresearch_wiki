---
title: "Qwen3-8B jax (Flax NNX) v033b: Splash + Scan + Remat + MaxText CE @ bs=1, seq=8192"
type: experiment
hypothesis: qwen3-jax-splash-attention
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: 14d392838fc92391b57881545ef41a55405922bc
verdict: supported
tags: [qwen3-cc, jax, flax-nnx, splash-attention, scan, remat, maxtext-ce, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax (Flax NNX) v033b: Splash + Scan + Remat + MaxText CE @ bs=1, seq=8192

Enabling the full optimized native-JAX stack (**Splash attention**, **layer-scan**, **selective rematerialization**, and **custom MaxText Cross-Entropy**) to target the program goal of **seqlen=8192** at batch size 1 (global batch 8).

## Hypothesis under test

This experiment tests the [Splash attention (jax)](../../../../hypotheses/qwen3-jax-splash-attention.md) and [tokamax streamed cross-entropy (jax)](../../../../hypotheses/qwen3-jax-tokamax-ce.md) hypotheses together. We expect that by avoiding intermediate score and logit materialization, we can eliminate the memory wall and successfully execute seqlen=8192 on TPU v6e-8.

## Setup

- **Hardware**: TPU v6e-8 — 2 hosts × 4 chips, fsdp=8, tp=1. Cluster `alekseyv-tpu-v6e8-spot-xpk` (zone `us-central2-b`).
- **Dispatch**: GKE/XPK. Workload `alekseyv-qwen3-cc-jax-v033b-mtce-s8k`.
- **Image**: `qwen3-8b-jax:v033-maxtext-ce`.
- **Command**:
  ```bash
  python -u train.py --model_id=Qwen/Qwen3-8B --use_real_data=False \
    --batch_size=1 --seqlen=8192 --tp_parallelism=1 \
    --train_steps=20 --weights_dtype=bf16 \
    --use_scan=True --use_remat=True --use_splash=True --use_maxtext_ce=True \
    --profile_dir=gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_cc/2026-06-02-qwen3-jax-v033-maxtext-ce-s8k-bs1 \
    --profile_start_step=12 --profile_steps=3
  ```
  global_batch = 1 × 8 = 8; tokens/step = 8 × 8192 = 65,536.

## Baseline comparison

Comparison against the [v6e-8 baseline](2026-06-02-qwen3-jax-v6e8-baseline.md) (seqlen 2048, no optimizations):

| Run | Seqlen | Step time | Throughput | tok/s/chip | MFU |
|---|---|---|---|---|---|
| baseline | 2048 | 512.6 ms | 31,955 tok/s | 3,994 | 20.5% |
| **v033b** | **8192** | **1446.8 ms** | **45,245 tok/s** | **5,656** | **32.4%** |
| **Δ (v033b − baseline)** | **+300%** | **+182.2%** | **+41.6%** | **+41.6%** | **+11.9 pp** |

Despite a 4x increase in sequence length, throughput and MFU increase substantially (**+41.6% tok/s/chip**). The optimizations successfully bypass the quadratic attention and large vocabulary logit memory walls.

## Results

| Metric | This run (v033b) | Notes |
|---|---|---|
| Steady step time | **1446.8 ms** | step 0 cold (36.2 s) excluded |
| Throughput | **45,245 tok/s** (5,656 / chip) | 18 steps measured |
| MFU | **32.4%** | v6e bf16 peak 918 TFLOPS/chip |
| Exit code | 0 | clean 20-step run |

## Profile

- **xprof URL**: `http://localhost:8791/?run=2026-06-02-qwen3-jax-v033-maxtext-ce-s8k-bs1`
- **GCS run dir**: `gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_cc/2026-06-02-qwen3-jax-v033-maxtext-ce-s8k-bs1/plugins/profile/2026_06_02_17_40_21/`
- **Local pointer**: [`raw/profiles/2026-06-02-qwen3-jax-v033b-maxtext-ce-s8k-bs1/`](../../../../../raw/profiles/2026-06-02-qwen3-jax-v033b-maxtext-ce-s8k-bs1/GCS_LOCATION.txt)
- **Profiled steps**: 12–14.
- **Op profile description**: Splash attention kernel and MaxText custom cross-entropy are fully active and fused, reducing memory bandwidth pressure.

## Observations

- Enabling splash attention, layer-scan, selective remat, and custom cross-entropy successfully unlocks sequence length 8192 without OOM.
- Model FLOPS Utilization (MFU) rises from 20.5% to 32.4%, showing that the TPU v6e-8 is utilized much more efficiently when running longer sequences with optimized kernels.

## Verdict + reasoning

**supported** — The hypothesis that combining splash attention, scan, remat, and chunked cross-entropy allows seqlen=8192 to run efficiently on v6e-8 is fully supported.

## Next hypotheses

- [Per-chip batch scaling (jax)](../../../../hypotheses/qwen3-jax-batch-scaling.md) — increase per-chip batch size to 2 (`v034`) to improve hardware utilization.

## Sources

- Profile + HLO (GCS): `gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_cc/2026-06-02-qwen3-jax-v033-maxtext-ce-s8k-bs1/`
- Local pointer: `raw/profiles/2026-06-02-qwen3-jax-v033b-maxtext-ce-s8k-bs1/GCS_LOCATION.txt`
- Model page: `wiki/models/qwen3-cc-jax.md`
