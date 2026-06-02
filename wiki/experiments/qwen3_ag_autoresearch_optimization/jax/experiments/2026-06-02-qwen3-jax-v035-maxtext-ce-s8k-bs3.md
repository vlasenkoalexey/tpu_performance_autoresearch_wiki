---
title: "Qwen3-8B jax (Flax NNX) v035: Per-Chip Batch Scaling @ bs=3, seq=8192"
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

# Qwen3-8B jax (Flax NNX) v035: Per-Chip Batch Scaling @ bs=3, seq=8192

Scaling per-chip batch size further to 3 (global batch 24) on top of the fully optimized JAX stack at seqlen=8192 to explore the efficiency limit.

## Hypothesis under test

This experiment tests the [Per-chip batch scaling (jax)](../../../../hypotheses/qwen3-jax-batch-scaling.md) hypothesis at a higher scale. Increasing batch size from bs=2 to bs=3 should continue to amortize fixed overheads and improve MXU occupancy, moving closer to the TPU v6e compute ceiling without running out of HBM (OOM).

## Setup

- **Hardware**: TPU v6e-8 — 2 hosts × 4 chips, fsdp=8, tp=1. Cluster `alekseyv-tpu-v6e8-spot-xpk` (zone `us-central2-b`).
- **Dispatch**: GKE/XPK. Workload `alekseyv-qwen3-cc-jax-v035-mtce-s8k-bs3`.
- **Image**: `qwen3-8b-jax:v033-maxtext-ce`.
- **Command**:
  ```bash
  python -u train.py --model_id=Qwen/Qwen3-8B --use_real_data=False \
    --batch_size=3 --seqlen=8192 --tp_parallelism=1 \
    --train_steps=20 --weights_dtype=bf16 \
    --use_scan=True --use_remat=True --use_splash=True --use_maxtext_ce=True \
    --profile_dir=gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_cc/2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3 \
    --profile_start_step=12 --profile_steps=3
  ```
  global_batch = 3 × 8 = 24; tokens/step = 24 × 8192 = 196,608.

## Baseline comparison

Comparison against the [v034 run](2026-06-02-qwen3-jax-v034-maxtext-ce-s8k-bs2.md) (bs=2, seqlen=8192):

| Run | Batch size | Step time | Throughput | tok/s/chip | MFU |
|---|---|---|---|---|---|
| v034 | 2 | 2731.2 ms | 47,937 tok/s | 5,992 | 34.4% |
| **v035** | **3** | **4077.5 ms** | **48,218 tok/s** | **6,027** | **34.6%** |
| **Δ (v035 − v034)** | **+50%** | **+49.3%** | **+0.6%** | **+0.6%** | **+0.2 pp** |

Increasing batch size from 2 to 3 provides a minor boost to throughput (**+0.6%**) and MFU (**+0.2 pp**), indicating that we are nearing the saturation point of amortization benefits for batch scaling. Crucially, the run completes with no OOM.

## Results

| Metric | This run (v035) | Notes |
|---|---|---|
| Steady step time | **4077.5 ms** | step 0 cold (34.7 s) excluded |
| Throughput | **48,218 tok/s** (6,027 / chip) | 18 steps measured |
| MFU | **34.6%** | v6e bf16 peak 918 TFLOPS/chip |
| Exit code | 0 | clean 20-step run |

## Profile

- **xprof URL**: `http://localhost:8791/?run=2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3`
- **GCS run dir**: `gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_cc/2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3/plugins/profile/2026_06_02_18_05_52/`
- **Local pointer**: [`raw/profiles/2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3/`](../../../../../raw/profiles/2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3/GCS_LOCATION.txt)
- **Profiled steps**: 12–14.
- **Op profile description**: Hardware execution is highly efficient with MXU and memory units heavily saturated. The marginal gain indicates we are close to the memory-activation-or-compute roofline.

## Observations

- Batch size 3 runs without memory issues (no OOM), demonstrating the efficacy of the selective remat, layer-scan, and MaxText CE.
- The small delta in throughput (+0.6%) suggests that at bs=2, we had already successfully amortized the vast majority of fixed overheads.

## Verdict + reasoning

**supported** — The hypothesis that further scaling to bs=3 runs successfully and delivers slight additional performance is supported.

## Next hypotheses

- [Per-chip batch scaling (jax)](../../../../hypotheses/qwen3-jax-batch-scaling.md) — scale to `bs=4` to see if OOM is reached or if throughput starts to degrade.
- [SparseCore collective offloads (jax)](../../../../hypotheses/qwen3-jax-sparsecore-offload.md) — offload FSDP collectives to SparseCore (similar to Llama 3 playbook) to reclaim TensorCore cycles for matmul compute, which is the next key frontier.

## Sources

- Profile + HLO (GCS): `gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_cc/2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3/`
- Local pointer: `raw/profiles/2026-06-02-qwen3-jax-v035-maxtext-ce-s8k-bs3/GCS_LOCATION.txt`
- Model page: `wiki/models/qwen3-cc-jax.md`
