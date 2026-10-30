---
title: libtpu flag sets used by the TPU recipes (per slice, with measured effects)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/recipes/
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# libtpu flag sets used by the TPU recipes (per slice, with measured effects)

## Definition
Each TPU recipe pins a small set of libtpu init flags that its numbers were measured with: a scoped-VMEM
budget, (on TPU7x) the throughput power state, and SparseCore collective-offload / scheduler flags that let
FSDP all-gathers and reduce-scatters overlap compute. Older recipes pass them on the launch command
(`--libtpu-init-flags=...` or `--extra-libtpu-init-flags=...`); newer ones carry them on the config so the
command repeats nothing. This page records which set each recipe uses and the gains the READMEs attribute to
individual flags. The layering mechanics (config -> CLI -> env) are on
[tpu-libtpu-xla-flag-layering](tpu-libtpu-xla-flag-layering.md).

## In torchtitan (grounded)
- Flags are fields of [`BaseTPUTrainerConfig`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#BaseTPUTrainerConfig)
  ([`libtpu_init_flags`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#BaseTPUTrainerConfig.libtpu_init_flags),
  [`extra_libtpu_init_flags`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#BaseTPUTrainerConfig.extra_libtpu_init_flags)),
  exported by [`apply_init_flags`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#apply_init_flags) before PJRT starts.
  `--libtpu-init-flags` on the CLI **replaces** the config's whole set; `--extra-libtpu-init-flags` adds/overrides
  individual flags; an exported `LIBTPU_INIT_ARGS` wins over both (the Qwen3-30B-A3B README states the last rule explicitly).
- Named bundles, composed with [`merge_flags`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#merge_flags):
  [`TPU7X_THROUGHPUT_P_STATE`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#TPU7X_THROUGHPUT_P_STATE.TPU7X_THROUGHPUT_P_STATE),
  [`SPARSECORE_LATENCY_HIDING_SCHEDULER`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#SPARSECORE_LATENCY_HIDING_SCHEDULER.SPARSECORE_LATENCY_HIDING_SCHEDULER),
  [`DUAL_SPARSECORE_REDUCE_SCATTER`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#DUAL_SPARSECORE_REDUCE_SCATTER.DUAL_SPARSECORE_REDUCE_SCATTER),
  [`HIERARCHICAL_REDUCE_SCATTER`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#HIERARCHICAL_REDUCE_SCATTER.HIERARCHICAL_REDUCE_SCATTER),
  [`SPARSECORE_ASYNC_ALL_GATHER`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#SPARSECORE_ASYNC_ALL_GATHER.SPARSECORE_ASYNC_ALL_GATHER),
  [`SPARSECORE_COLLECTIVE_OFFLOAD`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#SPARSECORE_COLLECTIVE_OFFLOAD.SPARSECORE_COLLECTIVE_OFFLOAD),
  [`DISABLE_ENHANCED_LAUNCH_BARRIER`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#DISABLE_ENHANCED_LAUNCH_BARRIER.DISABLE_ENHANCED_LAUNCH_BARRIER).
- Config-carried sets: [`_QWEN3_DENSE_4X4X4_FLAGS`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#_QWEN3_DENSE_4X4X4_FLAGS)
  (merged into [`qwen3_32b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_32b) and inherited by
  [`qwen3_32b_4x8x8`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_32b_4x8x8)) and the identical
  [`_MUSE_GLIMMER_4X4X4_FLAGS`](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md#_MUSE_GLIMMER_4X4X4_FLAGS)
  (merged in [`_muse_glimmer_30b_base`](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md#_muse_glimmer_30b_base)).

### Flag set per recipe

| Recipe | How passed | Flags (bundle names where they match exactly) |
|---|---|---|
| llama3-8b v6e-8 | CLI `--libtpu-init-flags` | `xla_tpu_scoped_vmem_limit_kib=131072`, `tpu_program_stack_shrink_after_unload=false` |
| llama3-8b v6e-256 | CLI | vmem 131072 |
| qwen3-8b v6e-8 / v6e-256 | CLI | `DISABLE_ENHANCED_LAUNCH_BARRIER`, vmem 65536 |
| flux1 v6e-8, flux1 tpu7x-4x4x4 | CLI | vmem 65536 |
| flux1 v6e-256 | CLI | `SPARSECORE_COLLECTIVE_OFFLOAD` (aggregator, LHS queuing, 2D + 3D all-gather offload, reduce-scatter offload) |
| llama3-70b tpu7x-2x2x4 / tpu7x-64 | CLI | vmem 131072 |
| llama3-70b tpu7x-128 | CLI `--extra-libtpu-init-flags` | `TPU7X_THROUGHPUT_P_STATE`, vmem 131072, `xla_tpu_enable_offloading_copy_to_sparsecore=false`, `SPARSECORE_ASYNC_ALL_GATHER`, `xla_tpu_copy_insertion_use_region_analysis=true` with limit 1000 |
| qwen3-8b tpu7x-2x2x2 | CLI | p-state 7, vmem 65472, `SPARSECORE_LATENCY_HIDING_SCHEDULER`, `DUAL_SPARSECORE_REDUCE_SCATTER` |
| qwen3-8b tpu7x-4x4x4 | CLI | p-state 7, vmem 65472, `SPARSECORE_LATENCY_HIDING_SCHEDULER`, `HIERARCHICAL_REDUCE_SCATTER` (= `_QWEN3_DENSE_4X4X4_FLAGS`) |
| qwen3-32b tpu7x-4x4x4 / 4x8x8 | config | `_QWEN3_DENSE_4X4X4_FLAGS` |
| muse-glimmer-30b tpu7x-4x4x4 | config | `_MUSE_GLIMMER_4X4X4_FLAGS` (same set) |
| qwen3-30b-a3b tpu7x-4x4x4 | CLI | `SPARSECORE_LATENCY_HIDING_SCHEDULER`, `HIERARCHICAL_REDUCE_SCATTER`, p-state 7 |
| conformer v6e-8, mamba2/3 2x2x1 | none | libtpu defaults |

### Effects the READMEs attribute to individual flags
- **Latency-hiding layer scheduler + SparseCore collective aggregator** (Qwen3-30B-A3B, 30-step matched runs):
  about +5% throughput at both GBS 768 / seq 2K and GBS 1024 / seq 2K, keeping FP32 FSDP reductions. The two flags
  must be enabled or disabled together (the scheduler requires the aggregator); dropping both runs the same
  TorchTitan config without the scheduler.
- **Hierarchical n-D reduce-scatter** (Qwen3-30B-A3B, on top of the scheduler): a further +1.09% throughput,
  ring-equivalent reduce-scatter bus bandwidth 351.29 -> 364.57 GB/s.
- **Dual-SparseCore reduce-scatter** (`xla_tpu_use_single_sparse_core_for_reduce_scatter_offload=false`): optimal
  for the Zero-2 schedule (no parameter all-gathers in backward competing with reduce-scatter) and for the
  dependency-ordered Zero-3 interleave; the README says to re-evaluate it for Zero-3 `prefetch` or any schedule
  that makes all-gather and reduce-scatter concurrent.
- **p-state 7** (`xla_tpu_dvfs_p_state=7`): trades higher device power for faster compute; it does not change the graph.
- **`tpu_program_stack_shrink_after_unload=false`** (Llama3-8B v6e-8): keeps the TPU program stack at its
  high-water mark; with HBM nearly full, letting it shrink makes later program loads trigger HBM
  defragmentation stalls (~0.6% slower step time on libtpu 0.0.50).
- **Scoped VMEM** is raised on almost every recipe: 131072 KiB for Llama3, 65536 or 65472 KiB for FLUX / Qwen3 /
  Muse Glimmer. The READMEs give no per-recipe A/B for it.

## Why it matters / when it applies
- The SparseCore flags are what make pure FSDP competitive at 128-512 devices: they move or reschedule FSDP
  collectives off the TensorCore critical path. Their best setting depends on the FSDP schedule (Zero-2 vs
  Zero-3 prefetch vs interleave), so a flag set tuned for one schedule should be re-measured when the schedule
  changes - see [tpu-recipe-simplefsdp-schedules](tpu-recipe-simplefsdp-schedules.md).
- p-state 7 is a TPU7x-only operating point; Trillium recipes never set it.
- Because `--libtpu-init-flags` replaces the config's set, adding it to a config-carried recipe (Qwen3-32B,
  Muse Glimmer) silently drops the recipe's flags; use `--extra-libtpu-init-flags` for one-flag A/Bs.

### Doc vs code at this commit
- Several READMEs (Llama3 v6e, Llama3-70B 2x2x4/64, Qwen3-8B v6e, Qwen3-30B-A3B) describe their flags as
  "carried by the torchtitan config". The registry functions they name
  ([`llama3_8b`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_8b),
  [`llama3_70b`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#llama3_70b),
  [`reg_trainer_qwen3_8b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b),
  [`qwen3_8b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_8b),
  [`_qwen3_moe_30b_fsdp_only_full_ac`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#_qwen3_moe_30b_fsdp_only_full_ac))
  declare no libtpu flags; the flags exist only because the launch command sets the config field. Running those
  configs without the README's `--libtpu-init-flags` gives libtpu defaults. Only the Qwen3-32B and Muse Glimmer
  30B recipes (plus the scan / Qwen3-235B lines not covered here) truly carry flags in code.
- The Mamba READMEs pin libtpu 0.0.41; `HIERARCHICAL_REDUCE_SCATTER` needs libtpu 0.0.47 or newer per its code comment,
  so the flag sets above assume a newer container than the Mamba recipes list.

## Connections
- Code concepts: [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [job-config](../concepts/job-config.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md),
  [tpu-graph-trainer](../concepts/tpu-graph-trainer.md)
- Module catalogs: [tpu_flags](../catalog/torchtitan/experiments/tpu/tpu_flags.md),
  [tpu_job_config](../catalog/torchtitan/experiments/tpu/tpu_job_config.md),
  [qwen3/config_registry](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md),
  [muse_glimmer/config_registry](../catalog/torchtitan/experiments/tpu/muse_glimmer/config_registry.md)
- Related doc-concepts: [tpu-libtpu-xla-flag-layering](tpu-libtpu-xla-flag-layering.md),
  [tpu-recipe-matrix](tpu-recipe-matrix.md), [tpu-recipe-simplefsdp-schedules](tpu-recipe-simplefsdp-schedules.md),
  [tpu-splash-attention-tiles-and-vmem](tpu-splash-attention-tiles-and-vmem.md),
  [tpu-simplefsdp-and-mixed-precision](tpu-simplefsdp-and-mixed-precision.md)

## Source
Extracted from (kept in place):
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-30b-a3b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-8b/tpu7x-2x2x2/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-8b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/qwen3-32b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/muse-glimmer-30b/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/llama3-70b/tpu7x-128/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/llama3-70b/tpu7x-2x2x4/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/llama3-70b/tpu7x-64/README.md`
- `torchtitan/experiments/tpu/recipes/ironwood/flux1/tpu7x-4x4x4/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/flux1/v6e-8/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/flux1/v6e-256/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/llama3-8b/v6e-8/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/llama3-8b/v6e-256/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/qwen3-8b/v6e-8/README.md`
- `torchtitan/experiments/tpu/recipes/trillium/qwen3-8b/v6e-256/README.md`

Cross-checked against `torchtitan/experiments/tpu/tpu_flags.py` and the config registries at commit 2ad96c939.
