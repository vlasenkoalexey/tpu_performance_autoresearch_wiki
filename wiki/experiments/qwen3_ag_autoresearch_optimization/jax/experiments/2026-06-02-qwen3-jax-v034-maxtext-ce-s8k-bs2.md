---
title: "Qwen3-8B jax (Flax NNX) v034: Per-Chip Batch Scaling @ bs=2, seq=8192"
type: experiment
hypothesis: qwen3-jax-batch-scaling
model: qwen3-cc-jax
variant: "8B/v6e-8"
commit: 14d392838fc92391b57881545ef41a55405922bc
verdict: supported
tags: [qwen3-cc, jax, flax-nnx, batch-scaling, v6e-8]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3-8B jax (Flax NNX) v034: Per-Chip Batch Scaling @ bs=2, seq=8192

Scaling per-chip batch size to 2 (global batch 16) on top of the fully optimized JAX stack at seqlen=8192 to increase hardware utilization.

## Hypothesis under test

This experiment tests the [Per-chip batch scaling (jax)](../../../../hypotheses/qwen3-jax-batch-scaling.md) hypothesis. Increasing the workload per step from bs=1 to bs=2 should better amortize fixed communication and framework dispatch overheads, lifting MXU utilization and MFU without binding on HBM capacity.

## Setup

- **Hardware**: TPU v6e-8 — 2 hosts × 4 chips, fsdp=8, tp=1. Cluster `alekseyv-tpu-v6e8-spot-xpk` (zone `us-central2-b`).
- **Dispatch**: GKE/XPK. Workload `alekseyv-qwen3-cc-jax-v034-mtce-s8k-bs2`.
- **Image**: `qwen3-8b-jax:v033-maxtext-ce`.
- **Command**:
  ```bash
  python -u train.py --model_id=Qwen/Qwen3-8B --use_real_data=False \
    --batch_size=2 --seqlen=8192 --tp_parallelism=1 \
    --train_steps=20 --weights_dtype=bf16 \
    --use_scan=True --use_remat=True --use_splash=True --use_maxtext_ce=True \
    --profile_dir=gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_cc/2026-06-02-qwen3-jax-v034-maxtext-ce-s8k-bs2 \
    --profile_start_step=12 --profile_steps=3
  ```
  global_batch = 2 × 8 = 16; tokens/step = 16 × 8192 = 131,072.

## Baseline comparison

Comparison against the [v033b run](2026-06-02-qwen3-jax-v033b-maxtext-ce-s8k-bs1.md) (bs=1, seqlen=8192):

| Run | Batch size | Step time | Throughput | tok/s/chip | MFU |
|---|---|---|---|---|---|
| v033b | 1 | 1446.8 ms | 45,245 tok/s | 5,656 | 32.4% |
| **v034** | **2** | **2731.2 ms** | **47,937 tok/s** | **5,992** | **34.4%** |
| **Δ (v034 − v033b)** | **+100%** | **+88.8%** | **+6.0%** | **+5.0%** | **+2.0 pp** |

Doubling the batch size increases throughput by **+6.0%** and lifts MFU by **2.0 pp**, proving that the larger batch size successfully amortizes fixed dispatch and collective overhead.

## Results

| Metric | This run (v034) | Notes |
|---|---|---|
| Steady step time | **2731.2 ms** | step 0 cold (39.2 s) excluded |
| Throughput | **47,937 tok/s** (5,992 / chip) | 18 steps measured |
| MFU | **34.4%** | v6e bf16 peak 918 TFLOPS/chip |
| Exit code | 0 | clean 20-step run |

## Profile

- **xprof URL**: `http://localhost:8791/?run=2026-06-02-qwen3-jax-v034-maxtext-ce-s8k-bs2`
- **GCS run dir**: `gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_cc/2026-06-02-qwen3-jax-v034-maxtext-ce-s8k-bs2/plugins/profile/2026_06_02_17_53_14/`
- **Local pointer**: [`raw/profiles/2026-06-02-qwen3-jax-v034-maxtext-ce-s8k-bs2/`](../../../../../raw/profiles/2026-06-02-qwen3-jax-v034-maxtext-ce-s8k-bs2/GCS_LOCATION.txt)
- **Profiled steps**: 12–14.
- **Op profile description**: MXU utilization is enhanced with higher batch occupancy; the time spent in XLA dispatch is successfully amortized.

## Observations

- Scaling per-chip batch size to 2 operates cleanly within the HBM capacity limits on TPU v6e-8.
- Step time scales sub-linearly with batch size (doubling batch size only increases step time by 88.8%), yielding a clear efficiency gain.

## Verdict + reasoning

**supported** — The hypothesis that batch scaling to bs=2 increases efficiency is fully supported.

## Next hypotheses

- [Per-chip batch scaling (jax)](../../../../hypotheses/qwen3-jax-batch-scaling.md) — increase per-chip batch size to 3 (`v035`) to explore further scaling benefits and find the OOM limit.

## Sources

- Profile + HLO (GCS): `gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_cc/2026-06-02-qwen3-jax-v034-maxtext-ce-s8k-bs2/`
- Local pointer: `raw/profiles/2026-06-02-qwen3-jax-v034-maxtext-ce-s8k-bs2/GCS_LOCATION.txt`
- Model page: `wiki/models/qwen3-cc-jax.md`
