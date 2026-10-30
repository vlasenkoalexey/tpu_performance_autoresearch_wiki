---
title: Mamba-2 / Mamba-3 2.7B at 256K context on TPU7x 2x2x1 (SSM long-context recipes)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/examples/mamba2/recipes/ironwood/mamba2-2.7b-256k/2x2x1/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Mamba-2 / Mamba-3 2.7B at 256K context on TPU7x 2x2x1 (SSM long-context recipes)

## Definition
Two example recipes train ~3.3B-parameter state-space models (Mamba-2 and Mamba-3, both d_model 2560, 64 layers,
80 heads of dim 64) at a sequence length of 262,144 tokens on a single TPU7x host (2x2x1 topology = 4 chips =
8 TensorCores). There is no attention and no context parallelism: each sequence lives on one core, the SSM is
computed by a chunked Pallas scan kernel, and the model is sharded with plain 1-D FSDP2. The READMEs pitch the
recipe as "linear in sequence length": activation memory and compute scale with B x S, so 256K fits in a third
of HBM.

## In torchtitan (grounded)
- Configs: [`mamba2_2_7b_256k`](../catalog/torchtitan/experiments/tpu/examples/mamba2/config_registry.md#mamba2_2_7b_256k) and
  [`mamba3_2_7b_256k`](../catalog/torchtitan/experiments/tpu/examples/mamba3/config_registry.md#mamba3_2_7b_256k): regular
  [`TPUTrainerConfig`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUTrainerConfig), 8 x 262144 tokens per rank,
  `max_context_length=262144`, [`FullAC`](../catalog/torchtitan/distributed/activation_checkpoint.md#FullAC), AdamW lr 3e-4, `c4_test` data.
  Both registries default every flavor's context bound to 262144 (`_DEFAULT_MAX_CONTEXT_LENGTH`).
- Models: [`Mamba2Config`](../catalog/torchtitan/experiments/tpu/examples/mamba2/model.md#Mamba2Config)
  ([`chunk_size`](../catalog/torchtitan/experiments/tpu/examples/mamba2/model.md#Mamba2Config.chunk_size) 64,
  [`d_state`](../catalog/torchtitan/experiments/tpu/examples/mamba2/model.md#Mamba2Config.d_state) 16 for 2.7B,
  [`ssm_backend`](../catalog/torchtitan/experiments/tpu/examples/mamba2/model.md#Mamba2Config.ssm_backend) `"pallas"`) and
  [`Mamba3Config`](../catalog/torchtitan/experiments/tpu/examples/mamba3/model.md#Mamba3Config) (chunk 256, d_state 128).
- Kernels: [`ssd_chunk_scan_pallas`](../catalog/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.md#ssd_chunk_scan_pallas)
  (Mamba-2 SSD) and [`ssd3_chunk_scan_pallas`](../catalog/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.md#ssd3_chunk_scan_pallas) (Mamba-3).
- Parallelism: [`parallelize_mamba2`](../catalog/torchtitan/experiments/tpu/examples/mamba2/parallelize.md#parallelize_mamba2) applies
  upstream FSDP2 (`apply_fsdp_to_decoder`) and rejects TP and CP; Mamba-3 has the same shape in `examples/mamba3/parallelize.py`.
- FLOPs: [`Mamba2Config.get_nparams_and_flops`](../catalog/torchtitan/experiments/tpu/examples/mamba2/model.md#Mamba2Config.get_nparams_and_flops)
  returns `6 * nparams` per token, the same convention the READMEs use for MFU.

### Numbers stated in the READMEs

| | Mamba-2 2.7B | Mamba-3 2.7B |
|---|---|---|
| Parameters | 3,280,906,240 | 3,266,507,264 untied (2,938,171,904 tied) |
| d_state / chunk | 16 / 64 (4,096 chunks at 256K) | 128 / 256 (1,024 chunks) |
| Static state per core (bf16 params + grads, fp32 Adam + master, sharded over 8) | ~6.56 GiB | ~6.56 GiB |
| Peak per core, local batch 1 (GBS 8, 2.1M tok/step) | ~10.4 GiB | ~10.7 GiB |
| Peak per core, local batch 8 (GBS 64, 16.8M tok/step) | ~31.8 GiB | ~34.0 GiB |
| "Expected" MFU, local batch 1 | 14.0-18.6% (est. step 24-32 s) | 13.5-18.1% (est. 25-33 s) |
| "Expected" MFU, local batch 8 | 17.0-22.4% (est. step 160-210 s) | 16.6-21.7% (est. 165-215 s) |
| Short-context baseline (S=128, local batch 2) | 0.023% MFU, 2.35 s | ~0.023%, ~2.30 s |

Peak FLOPs are taken as 8 cores x 1,153.5 TFLOP/s = 9,228 TFLOP/s. The Mamba-3 README additionally reports
measured single-core numbers: the Pallas SSD3 kernel alone (H=80, D=64, N=128, batch 1) sustains 298K-404K tokens/s
from 4K to 256K (781.84 ms fwd+bwd at 256K), while one full `Mamba3Block` reaches only 2.2-2.7% single-core MFU,
which the README attributes to narrow matmul M dimension at batch 1 and no collective overlap.

## Why it matters / when it applies
- This is the lane's only 256K-context training recipe, and it reaches it without context parallelism: the SSM's
  per-token state replaces the attention KV, so one core holds a whole sequence and plain FSDP suffices.
- MFU is low at short context (0.023% at S=128 - host and sync overhead dominate) and only becomes meaningful when
  tokens per step are in the millions; local batch 8 at 256K is the throughput configuration.
- 6 x N counts only parameter matmuls. It does not include the sequence-dependent SSM scan work (an observation
  about the convention, not a README claim), so MFU here is a lower-bound style figure comparable to the torchtitan
  convention, not to attention-model MFU with attention FLOPs included.

### Doc vs code at this commit
- **Activation checkpointing.** The Mamba-2 README's memory breakdown says "Selective Activation Checkpointing";
  `mamba2_2_7b_256k` sets `FullAC`. (Mamba-3's README says full AC, which matches.)
- **Stale CLI in Mamba-3.** The Mamba-3 commands pass `--training.local_batch_size` and `--training.seq_len`, which no
  longer exist on [`TrainingConfig`](../catalog/torchtitan/config/configs.md#TrainingConfig) (token budgets only); use
  `--training.num_tokens_per_microbatch_per_dp_rank=<seqs x 262144>` and `--training.max_context_length=262144` as the
  Mamba-2 README does. The Mamba-3 README also still launches with `xpk` (c10d rendezvous, an undefined `REPOSITORY`
  variable) while every other recipe uses `gcluster`.
- **Estimated, not measured.** The cluster-level TPS / step time / MFU columns are given as ranges labeled "Est." and
  "Expected"; only the Mamba-3 single-core kernel and block tables are presented as measurements. Both READMEs pin an
  older software stack (torch 2.12.0, torch_tpu 0.1.1, libtpu 0.0.41, jax 0.11.0).

## Connections
- Code concepts: [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md), [model-spec-protocols](../concepts/model-spec-protocols.md),
  [tpu-context-parallel-attention](../concepts/tpu-context-parallel-attention.md) (the attention-model route to long context)
- Module catalogs: [examples/mamba2/config_registry](../catalog/torchtitan/experiments/tpu/examples/mamba2/config_registry.md),
  [examples/mamba3/config_registry](../catalog/torchtitan/experiments/tpu/examples/mamba3/config_registry.md),
  [examples/mamba2/model](../catalog/torchtitan/experiments/tpu/examples/mamba2/model.md),
  [examples/mamba3/model](../catalog/torchtitan/experiments/tpu/examples/mamba3/model.md),
  [examples/mamba2/kernels/mamba2_pallas](../catalog/torchtitan/experiments/tpu/examples/mamba2/kernels/mamba2_pallas.md),
  [examples/mamba3/kernels/mamba3_pallas](../catalog/torchtitan/experiments/tpu/examples/mamba3/kernels/mamba3_pallas.md)
- Related doc-concepts: [tpu-recipe-matrix](tpu-recipe-matrix.md),
  [tpu-recipe-precision-and-throughput-accounting](tpu-recipe-precision-and-throughput-accounting.md),
  [tpu-recipe-memory-policy-and-save-regions](tpu-recipe-memory-policy-and-save-regions.md)

## Source
Extracted from (kept in place):
- `torchtitan/experiments/tpu/examples/mamba2/recipes/ironwood/mamba2-2.7b-256k/2x2x1/README.md`
- `torchtitan/experiments/tpu/examples/mamba3/recipes/ironwood/mamba3-2.7b-256k/2x2x1/README.md`

Cross-checked against `torchtitan/experiments/tpu/examples/mamba{2,3}/{config_registry,model,parallelize}.py` at commit 2ad96c939.
