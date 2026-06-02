---
title: "Qwen3 8B — maxtext (reference lane)"
type: model
architecture: qwen3-cc
lane: maxtext
sizes: ["8B"]
hardwares: ["v6e-8"]
tags: [qwen3-cc, maxtext, reference]
created: 2026-06-02
updated: 2026-06-02
---

# Qwen3 8B — maxtext (reference lane)

Upstream **MaxText** running `Qwen/Qwen3-8B` on **TPU v6e-8**, used as the **reference ceiling** for the
qwen3_cc program (mirrors the llama3 program's torchax→jax→MaxText structure). We run MaxText verbatim —
no model code in this lane; the architecture is MaxText's own `configs/models/qwen3-8b.yml`, which matches
our trainer exactly (4096 hidden, 32 q / 8 kv heads, head_dim 128, 36 layers, mlp 12288, QK-norm, SwiGLU,
vocab 151936, rope θ 1e6 — see [observation](../observations/qwen3-maxtext-config-exists.md)).

**Purpose**: establish the MaxText MFU for this exact architecture so the jax (35.8% @ seq2048 / 30.4% @
seq8192) and torchax (19.2%) lanes have a true apples-to-apples ceiling, the way llama3-8b-jax (43.3%) is
measured against the MaxText Llama-3.1-8B reference (44.6%).

## Target metrics

- Primary: MFU at seq_len=8192 (v6e bf16 peak ≈ 918 TFLOPS/chip), reported as TFLOP/s/device → MFU.
- Secondary: tokens/sec/device, step time, peak HBM.

## How to run

Run from the MaxText worktree (`/mnt/disks/persist/maxtext-tpu-recipes-v0.1.4`, tag `tpu-recipes-v0.1.4`,
commit `9f1820b47`) in the maxtext venv (`/mnt/disks/persist/venv-maxtext-v0.1.4`), base image
`maxtext_base_image:latest` (built via `docker_build_dependency_image.sh DEVICE=tpu MODE=stable_stack
BASEIMAGE=us-docker.pkg.dev/cloud-tpu-images/jax-ai-image/tpu:jax0.6.1-rev1`):

```bash
export PROJECT=tpu-pytorch ZONE=us-central2-b CLUSTER_NAME=alekseyv-tpu-v6e8-spot-xpk
export OUTPUT_DIR=gs://tpu-pytorch-alekseyv-us-central2/autoresearch/qwen3_cc/maxtext/<run>
python3 -m benchmarks.benchmark_runner xpk \
  --project=$PROJECT --zone=$ZONE --device_type=v6e-8 --num_slices=1 \
  --cluster_name=$CLUSTER_NAME --base_output_directory=$OUTPUT_DIR \
  --model_name=qwen3_8b_8192_ref \        # or qwen3_8b_2048_ref for the seq2048 shape
  --base_docker_image=maxtext_base_image
```

The benchmark configs `qwen3_8b_8192_ref` (seq8192, bs3) and `qwen3_8b_2048_ref` (seq2048, bs4) were added
to the worktree's `benchmarks/maxtext_trillium_model_configs.py`, mirroring the proven
`llama3_1-8b-8192-no-collective-matmul` recipe tuning (remat custom + decoder/proj offloads, attention
flash/splash with `sa_block_*=2048` + `sa_use_fused_bwd_kernel`, synthetic data, the HOST_OFFLOAD +
SparseCore-offload + DISABLE_COLLECTIVE_MATMUL XLA flag stack).

## Variant matrix

| Size | Hardware | Status | Baseline (step / TPS / MFU) | Current best | Open hyps | Frontier exp |
|------|----------|--------|------------------------------|--------------|-----------|--------------|
| 8B | v6e-8 | open | — (reference run in progress) | — | 0 | — |

*First reference run dispatching 2026-06-02 (seq8192 `qwen3_8b_8192_ref`, then seq2048 `qwen3_8b_2048_ref`).
The MaxText Llama-3.1-8B reference on the same cluster was 44.6% MFU; Qwen3-8B is the same architecture
class (+QK-norm), so a similar regime is expected — to be measured, not assumed.*

## Cross-variant open hypotheses

(none yet — the reference baseline must land first)

## Variant-specific open hypotheses

(none yet)

## Retired hypotheses

(none yet)

## Knobs translation matrix

| Technique | 8B/v6e-8 | Notes |
|-----------|----------|-------|
(populated after the reference baseline + first ablations)

## Iteration ladder

1. **Reference baseline** — `qwen3_8b_8192_ref` (seq8192, recipe tuning) on v6e-8; measure MFU/TFLOP-s.
2. `qwen3_8b_2048_ref` (seq2048) — direct shape-match to the jax v018 frontier (35.8%).
3. Cross-lane analysis: MaxText vs jax (35.8%/30.4%) vs torchax (19.2%) — quantify each stack's gap to the
   MaxText ceiling, as the llama3 program does.

## See also

- [Qwen3 8B — jax](qwen3-cc-jax.md) — hand-tuned native-JAX lane (frontier 35.8% MFU).
- [Qwen3 8B — torchax](qwen3-cc-torchax.md) — torchax lane (19.2%).
- [observation: MaxText qwen3-8b config exists](../observations/qwen3-maxtext-config-exists.md)
- [maxtext codebase](../codebases/maxtext.md); MaxText Llama-3.1-8B reference: [llama3 maxtext baseline](../experiments/llama3_8B_autoresearch_optimization/maxtext/experiments/2026-04-25-maxtext-llama3-1-8b-v6e8-baseline.md)

## Sources

- `raw/code/maxtext/` @ `532c8b3d8` (`configs/models/qwen3-8b.yml`); worktree `tpu-recipes-v0.1.4` (`9f1820b47`).
