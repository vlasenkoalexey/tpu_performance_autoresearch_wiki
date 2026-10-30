---
title: TPU recipe matrix (model x hardware -> config, parallelism, batch, flags, reported metrics)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/recipes/
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# TPU recipe matrix (model x hardware -> config, parallelism, batch, flags, reported metrics)

## Definition
The TPU lane ships one README per (model, TPU slice) under `torchtitan/experiments/tpu/recipes/<generation>/<model>/<topology>/`
(Ironwood = TPU7x, Trillium = v6e), plus two Mamba long-context recipes under
`torchtitan/experiments/tpu/examples/mamba{2,3}/recipes/`. Each README is a launch command
(`gcluster job submit` + `torchrun -m torchtitan.experiments.tpu.train --module=... --config=...`) and the
step time / TPS / MFU / HBM the maintainers measured with it on a given date. This page folds the
~20 READMEs into one matrix so the recipes can be compared side by side; the recurring techniques
have their own pages (see Connections).

## In torchtitan (grounded)
Every recipe resolves to a config-registry function; the README command only overrides a few fields.
The registry function is the real source of truth for parallelism, kernels and (for the newer recipes)
libtpu flags.

- Entry point: [`start_trainer`](../catalog/torchtitan/experiments/tpu/train.md#start_trainer) builds
  [`TPUTrainer`](../catalog/torchtitan/experiments/tpu/train.md#TPUTrainer) for a
  [`TPUTrainerConfig`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUTrainerConfig), or
  [`TpuGraphTrainer`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer)
  for a [`TpuGraphTrainer.Config`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer.Config)
  (the registry function's return type decides which trainer a recipe uses).
- Llama3: [`llama3_8b`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_8b),
  [`llama3_70b`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_70b),
  [`llama3_70b_float8`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_70b_float8).
- Qwen3 dense: [`reg_trainer_qwen3_8b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b),
  [`qwen3_8b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_8b),
  [`qwen3_8b_zero3`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_8b_zero3),
  [`qwen3_32b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_32b),
  [`qwen3_32b_4x8x8`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_32b_4x8x8).
- Qwen3 MoE: [`qwen3_moe_30b_fsdp_only_full_ac_benchmark`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_moe_30b_fsdp_only_full_ac_benchmark)
  (built on [`_qwen3_moe_30b_fsdp_only_full_ac`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac)).
- Muse Glimmer: [`muse_glimmer_30b_full_logits`](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md#muse_glimmer_30b_full_logits)
  (alternative [`muse_glimmer_30b_fused_ce`](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md#muse_glimmer_30b_fused_ce)).
- FLUX.1-dev: upstream [`flux_dev`](../catalog/torchtitan/models/flux/config_registry.md#flux_dev) with the TPU-side
  [`FluxConfig.img_size`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#FluxConfig.img_size) override applied by
  [`_apply_flux_img_size`](../catalog/torchtitan/experiments/tpu/train.md#_apply_flux_img_size).
- Conformer: [`conformer_test`](../catalog/torchtitan/experiments/tpu/conformer/config_registry.md#conformer_test), run through
  the minimal loop [`start_trainer`](../catalog/torchtitan/experiments/tpu/conformer/train_minimal.md#start_trainer).
- Mamba: [`mamba2_2_7b_256k`](../catalog/torchtitan/experiments/tpu/examples/mamba2/config_registry.md#mamba2_2_7b_256k),
  [`mamba3_2_7b_256k`](../catalog/torchtitan/experiments/tpu/examples/mamba3/config_registry.md#mamba3_2_7b_256k).

### Ironwood (TPU7x) - 2 TensorCores per chip, one process (device) per core, 8 processes per host

| Recipe | Slice (chips / devices, hosts x procs) | Config / trainer | Parallelism + memory | Batch / seq | Key flags | Reported (date) |
|---|---|---|---|---|---|---|
| flux1 tpu7x-4x4x4 | 64 / 128, 16x8 | `flux_dev`, TPUTrainer | SimpleFSDP + topo mesh, `torch.compile` backend `tpu`, Splash, `activation-checkpoint:full` (no RNG preserve) | fp32: 13824 tok/rank (3 images @ 4608); bf16: 23040 (5 images) | `xla_tpu_scoped_vmem_limit_kib=65536` | fp32 + bf16 MP: 2.57 s, 0.86 s/PDB, MFU 20.47% (9/28/26); pure bf16: 4.04 s, 0.81 s/PDB, MFU 21.64% (9/30/26) |
| llama3-70b tpu7x-2x2x4 | 16 / 32, 4x8 | `llama3_70b`, TPUTrainer (layerwise compile) | SimpleFSDP + topo mesh, full AC, Splash 2048, Pallas CE | seq 8192, 4 seq/device (32768 tok), GBS 128 | vmem 131072 | 1,138 TPS/device, MFU 47.51%, 36,426 TPS total (9/28/26) |
| llama3-70b tpu7x-64 | 32 / 64, 8x8 (topology 2x4x4) | same | same | seq 8192, 4 seq/device, GBS 256 | vmem 131072 | 1,157 TPS/device, MFU 48.29%, 74,049 total (9/28/26) |
| llama3-70b tpu7x-128 | 64 / 128, 16x8 (4x4x4) | `llama3_70b` or `llama3_70b_float8`, TPUTrainer | same; float8 = torchao rowwise `Float8Linear`, lm_head in bf16 | seq 8192, 2 seq/device (16384 tok), GBS 256 | via `--extra-libtpu-init-flags`: p-state 7, vmem 131072, SC async all-gather bundle, copy-insertion region analysis | bf16: 13.27 s, 1,235 TPS/dev, 594 TFLOP/s/dev, MFU 51.5%, 7.37 GiB; float8: 10.02 s, 1,636 TPS/dev, 787 TFLOP/s/dev, MFU N/A, 8.67 GiB (10/5/26) |
| muse-glimmer-30b tpu7x-4x4x4 | 64 / 128, 16x8 | `muse_glimmer_30b_full_logits`, GraphTrainer | SimpleFSDP Zero-3, `prefetch` FSDP barriers, `tpu_selective` (Splash saved), optimizer in graph, Splash 1024 + local mask, plain CE | seq 16384, local batch 1, GBS 128 | config-carried: p-state 7, vmem 65472, SC LHS pair, hierarchical RS | ~3,082 TPS, ~534.6 TFLOPS, MFU ~46.3%, ~5.32 s, 63.77 GiB (10/14/2026) |
| qwen3-30b-a3b tpu7x-4x4x4 | 64 / 128, 16x8 | `qwen3_moe_30b_fsdp_only_full_ac_benchmark`, GraphTrainer | FSDP over 128 (EP=1), Zero-2, `tpu_selective` (routing + Splash saved), packed QKV, Pallas grouped matmul | seq 2048, 6 seq/rank, GBS 768 | CLI: SC LHS pair, hierarchical RS, p-state 7 | MFU 18.02% (MaxText FLOPs; 20.12% torchtitan FLOPs), 10,056 TPS, 207.82 TFLOPS, 76.09 GiB, 1.222 s (10/13/2026) |
| qwen3-32b tpu7x-4x4x4 | 64 / 128, 16x8 | `qwen3_32b`, GraphTrainer | Zero-3 + `prefetch`, full graph remat, packed QKV, optimizer in graph | seq 4096, local 8, GBS 1024 | config-carried: p-state 7, vmem 65472, SC LHS pair, hierarchical RS | ~2,618 TPS, ~536.1 TFLOPS, MFU ~46.5%, ~12.52 s, 35.66 GiB (10/4/2026, c4_test); streamed C4 9/25: ~2,742 TPS, MFU ~48.7%, ~11.95 s |
| qwen3-32b tpu7x-4x8x8 | 256 / 512, 64x8 | `qwen3_32b_4x8x8`, GraphTrainer | as 4x4x4 plus `interleave` barriers and all-reduce+slice for w1/w3 gradients | seq 4096, local 8, GBS 4096 | same as 4x4x4 | ~2,656 TPS, ~544.0 TFLOPS, MFU ~47.2%, ~12.34 s, 83.07 GiB (9/25/2026, xpk launch, streamed C4) |
| qwen3-8b tpu7x-2x2x2 | 8 / 16, 2x8 | `qwen3_8b`, GraphTrainer | SimpleFSDP (Zero-2 in config) + topo mesh, optimizer in graph, Splash tiles 1024 | seq 2048, 6 seq/rank (12288 tok) | CLI: p-state 7, vmem 65472, SC LHS pair, dual-SC reduce-scatter | ~11,650 TPS, ~550.12 TFLOPS, MFU ~47.69%, ~1.05 s, 80.48 GiB (9/28/2026) |
| qwen3-8b tpu7x-4x4x4 | 64 / 128, 16x8 | `qwen3_8b`, GraphTrainer | same | same | CLI: as 2x2x2 plus hierarchical RS | ~11,850 TPS, ~559.58 TFLOPS, MFU ~48.51%, ~1.037 s, 79.26 GiB (9/28/2026) |
| mamba2-2.7b-256k 2x2x1 | 4 / 8, 1x8 | `mamba2_2_7b_256k`, TPUTrainer | FSDP2 1-D DP, Pallas SSD scan | seq 262144, 8 or 1 seq/core | none | estimated MFU 17.0-22.4% (local 8) / 14.0-18.6% (local 1); ~31.8 / ~10.4 GiB |
| mamba3-2.7b-256k 2x2x1 | 4 / 8, 1x8 | `mamba3_2_7b_256k`, TPUTrainer | FSDP2 1-D DP, Pallas SSD3 scan | seq 262144, 8 or 1 seq/core | none | estimated MFU 16.6-21.7% / 13.5-18.1%; ~34.0 / ~10.7 GiB |

### Trillium (v6e) - one device per chip, 4 processes per host (`ct6e-standard-4t`)

| Recipe | Slice (chips, hosts x procs) | Config / trainer | Parallelism + memory | Batch / seq | Key flags | Reported (date) |
|---|---|---|---|---|---|---|
| conformer v6e-8 | 8, 2x4 (2x4) | `conformer_test` via `conformer.train_minimal` | DDP (replicate=-1, shard=1) through SimpleFSDP, full AC, Splash, CTC loss, random data | 262144 tok/rank | none | compiled (`compile.mode=layer`): 87,181 TPS/chip, MFU 6.37%, 697,448 total; eager `DEFER_AND_FUSE`: 88,664 TPS/chip, MFU 6.48%, 709,312 total (9/30/26) |
| flux1 v6e-8 | 8, 2x4 | `flux_dev`, TPUTrainer | SimpleFSDP (no topo mesh), compile `tpu`, Splash, full AC | fp32: 9216 tok (2 images); bf16: 13824 (3 images) | vmem 65536 | fp32 + MP: 2.82 s, 1.41 s/PDB; bf16: 3.59 s, 1.20 s/PDB (9/29/26) |
| flux1 v6e-256 | 256, 64x4 (16x16) | same | same | same | `SPARSECORE_COLLECTIVE_OFFLOAD` bundle (aggregator, LHS queuing, 2D/3D AG, RS offload) | fp32 + MP: 2.88 s, 1.44 s/PDB; bf16: 4.05 s, 1.35 s/PDB (9/29/26) |
| llama3-8b v6e-8 | 8, 2x4 | `llama3_8b`, TPUTrainer | SimpleFSDP (+ topo mesh from config), full AC, Splash 2048, Pallas CE, eager `DEFER_AND_FUSE` | seq 8192, 2 seq/rank, GBS 16 | vmem 131072, `tpu_program_stack_shrink_after_unload=false` | 5,383 TPS/chip, MFU 33.96%, 43,068 total (9/29/26) |
| llama3-8b v6e-256 | 256, 64x4 | same | same | seq 8192, 4 seq/rank, GBS 1024 | vmem 131072 | 6,177 TPS/chip, MFU 38.97%, 1,581,235 total (9/29/26) |
| qwen3-8b v6e-8 | 8, 2x4 | `reg_trainer_qwen3_8b`, TPUTrainer | SimpleFSDP + topo mesh, full AC, layer compile, materialize forward before backward, Splash 1024, legacy loss kernel | seq 2048, 6 seq/rank, GBS 48 | enhanced launch barrier off, vmem 65536 | 5,753 TPS, 271.65 TFLOPS, MFU 29.59%, 2.14 s (10/4/2026) |
| qwen3-8b v6e-256 | 256, 64x4 | same | same | seq 2048, 6 seq/rank, GBS 1536 | same | 6,377 TPS, 301.12 TFLOPS, MFU 32.80%, 1.93 s (9/30/2026) |

(PDB = per-device batch: the FLUX READMEs divide step time by images per device; e.g. 2.57 s / 3 = 0.86 s.)

## Why it matters / when it applies
- **The recurring stack.** Almost every transformer recipe is SimpleFSDP (pure FSDP over all devices,
  usually with the topology-aware mesh) + Splash attention + the `tpu` compile backend + float32 master
  weights with bf16 compute. No recipe uses TP, PP or CP; the only EP-capable family (Qwen3 MoE) is
  benchmarked FSDP-only with EP=1. Scale-out is handled by FSDP schedule and collective-offload tuning,
  not by adding parallelism axes.
- **Trainer split by generation.** The Ironwood Qwen3 / Muse Glimmer recipes run on GraphTrainer
  (joint forward/backward graph, in-graph optimizer, graph-level memory policies). Both Trillium Qwen3
  READMEs (dated 8/30/2026 and 8/31/2026) say GraphTrainer still OOMs on v6e, so they use
  `reg_trainer_qwen3_8b` on the regular trainer. Llama3 and FLUX use the regular trainer on both generations.
- **Weak scaling is close to flat.** Llama3-70B MFU is 47.51% / 48.29% / 51.5% at 32 / 64 / 128 devices
  (the 128-device run uses half the per-device batch and a richer flag set, so it is not a pure scaling
  point); Qwen3-32B holds ~47% from 128 to 512 devices only after the w1/w3 all-reduce+slice fix.
- **Comparing numbers.** Ironwood numbers are per device (per TensorCore) against a 1,153.5 TFLOP/s peak;
  Trillium numbers are per chip. Dates, datasets (c4_test vs streamed C4) and FLOP conventions differ
  between READMEs; see [tpu-recipe-precision-and-throughput-accounting](tpu-recipe-precision-and-throughput-accounting.md)
  before comparing rows.
- **Launch pattern.** All recipes except Mamba-3 use `gcluster job submit` with `torchrun
  --rdzv_backend=static`, `--nnodes` = hosts, `--nproc_per_node` 8 (TPU7x) or 4 (v6e), and
  `--gke-disable-parallel-containers` on TPU7x. Mamba-3 still uses `xpk workload create` with `c10d` rendezvous.

### Doc vs code at this commit
- The Llama3 READMEs list "Loss Kernel: Enabled"; in code that is the fused Pallas cross entropy
  installed by [`_enable_pallas_cross_entropy`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#_enable_pallas_cross_entropy),
  not [`LossKernelConfig.use_loss_kernel`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#LossKernelConfig) (which stays False).
  The v6e Llama3 commands also repeat `--splash_attention_kernel.sa_block_kv_compute=2048`, already the config value.
- The FLUX tpu7x README title says "64 TPU ... (v7x-64)", but topology 4x4x4 with 16 hosts x 8 processes is
  64 chips / 128 devices.
- Conformer: the README labels the recipe "DDP" while noting `--tpu_config.use_simple_fsdp`. Both hold:
  Conformer reads [`TPUConfig.use_simple_fsdp`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUConfig.use_simple_fsdp)
  (not the [`ParallelismConfig.use_simple_fsdp`](../catalog/torchtitan/config/configs.md#ParallelismConfig.use_simple_fsdp)
  the LLM recipes use), and with shard degree 1 / replicate -1
  [`_determine_parallel_strategy`](../catalog/torchtitan/experiments/tpu/conformer/infra/parallelize.md#_determine_parallel_strategy)
  picks `DDP_W_SIMPLEFSDP`.
- The Qwen3-32B tpu7x-4x8x8 numbers predate the move to `gcluster` and were not re-measured; the Mamba MFU
  columns are estimates, not measurements (see [tpu-recipe-mamba-256k-long-context](tpu-recipe-mamba-256k-long-context.md)).

## Connections
- Code concepts: [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [tpu-graph-trainer](../concepts/tpu-graph-trainer.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [llama3-model](../concepts/llama3-model.md), [qwen3-model](../concepts/qwen3-model.md),
  [muse-glimmer-model](../concepts/muse-glimmer-model.md), [flux-diffusion-model](../concepts/flux-diffusion-model.md),
  [tpu-moe-dispatch-and-grouped-experts](../concepts/tpu-moe-dispatch-and-grouped-experts.md),
  [tpu-pallas-kernels](../concepts/tpu-pallas-kernels.md), [quantization](../concepts/quantization.md)
- Module catalogs: [llama3/config_registry](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md),
  [qwen3/config_registry](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md),
  [muse_glimmer/config_registry](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md),
  [conformer/config_registry](../catalog/torchtitan/experiments/tpu/conformer/config_registry.md),
  [examples/mamba2/config_registry](../catalog/torchtitan/experiments/tpu/examples/mamba2/config_registry.md),
  [examples/mamba3/config_registry](../catalog/torchtitan/experiments/tpu/examples/mamba3/config_registry.md),
  [train](../catalog/torchtitan/experiments/tpu/train.md), [tpu_job_config](../catalog/torchtitan/experiments/tpu/tpu_job_config.md)
- Related doc-concepts: [tpu-recipe-libtpu-flag-sets](tpu-recipe-libtpu-flag-sets.md),
  [tpu-recipe-simplefsdp-schedules](tpu-recipe-simplefsdp-schedules.md),
  [tpu-recipe-memory-policy-and-save-regions](tpu-recipe-memory-policy-and-save-regions.md),
  [tpu-recipe-splash-and-loss-kernel-choices](tpu-recipe-splash-and-loss-kernel-choices.md),
  [tpu-recipe-precision-and-throughput-accounting](tpu-recipe-precision-and-throughput-accounting.md),
  [tpu-recipe-mamba-256k-long-context](tpu-recipe-mamba-256k-long-context.md),
  [tpu-libtpu-xla-flag-layering](tpu-libtpu-xla-flag-layering.md),
  [tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md),
  [tpu-graph-trainer-memory-policies](tpu-graph-trainer-memory-policies.md),
  [tpu-defer-and-fuse-eager-mode](tpu-defer-and-fuse-eager-mode.md),
  [tpu-per-block-torch-compile](tpu-per-block-torch-compile.md),
  [tpu-launch-and-profiling-workflow](tpu-launch-and-profiling-workflow.md)

## Source
Extracted from (kept in place):
- `torchtitan/experiments/tpu/recipes/ironwood/flux1/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/llama3-70b/tpu7x-128/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/llama3-70b/tpu7x-2x2x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/llama3-70b/tpu7x-64/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/muse-glimmer-30b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-30b-a3b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-32b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-32b/tpu7x-4x8x8/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-8b/tpu7x-2x2x2/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-8b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/conformer/v6e-8/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/flux1/v6e-256/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/flux1/v6e-8/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/llama3-8b/v6e-256/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/llama3-8b/v6e-8/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/qwen3-8b/v6e-256/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/qwen3-8b/v6e-8/README.md`
- `torchtitan/experiments/tpu/examples/mamba2/recipes/ironwood/mamba2-2.7b-256k/2x2x1/README.md`
- `torchtitan/experiments/tpu/examples/mamba3/recipes/ironwood/mamba3-2.7b-256k/2x2x1/README.md`

Cross-checked against the config registries named above at commit 2ad96c939.
