---
title: TPU libtpu / XLA flag layering (config -> CLI -> environment)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# TPU libtpu / XLA flag layering (config -> CLI -> environment)

## Definition
`LIBTPU_INIT_ARGS` and `XLA_FLAGS` are normally set by the launcher. The TPU lane makes them
first-class fields of the training config (`libtpu_init_flags`, `xla_flags`), so a recipe carries
the compiler/runtime flags it was tuned with. Three layers resolve in increasing precedence:
config -> CLI `--extra-*` -> exported environment variable. Values are whitespace-separated
`flag=value` entries, and named *bundles* group flags that only make sense together.

## In torchtitan (grounded)
- The four fields live on [`BaseTPUTrainerConfig`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#BaseTPUTrainerConfig):
  [`libtpu_init_flags`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#BaseTPUTrainerConfig.libtpu_init_flags),
  [`xla_flags`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#BaseTPUTrainerConfig.xla_flags),
  [`extra_libtpu_init_flags`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#BaseTPUTrainerConfig.extra_libtpu_init_flags),
  [`extra_xla_flags`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#BaseTPUTrainerConfig.extra_xla_flags).
  Each is a [`FlagMap`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#FlagMap), a dict subtype with
  its own tyro rule so the CLI accepts a free-form `flag=value ...` string (a plain dict field could
  only retune keys already present in its default).
- [`parse_flags`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#parse_flags) strips leading `-`,
  splits on whitespace, and turns `!name` into the [`REMOVE`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#REMOVE)
  sentinel; [`resolve_flags`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#resolve_flags) merges
  layers and drops removed names.
- [`apply_init_flags`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#apply_init_flags) renders both
  env vars via [`_apply_flags`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#_apply_flags). It is
  called from [`_start_trainer`](../catalog/torchtitan/experiments/tpu/gmain.md#_start_trainer) before the
  first TPU device use: libtpu latches the values when the first program compiles, so flags applied
  later are silently ignored.
- Bundles are module constants composed with [`merge_flags`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#merge_flags)
  (later arguments win; Python bools render as lowercase `true`/`false`).

### Precedence rules (doc and code agree)

| Layer | How set | Effect |
|---|---|---|
| 1. Config | recipe's `libtpu_init_flags` / `xla_flags`; or CLI `--libtpu-init-flags` / `--xla-flags` | CLI form **replaces the whole set**; `''` runs with libtpu/XLA defaults |
| 2. CLI extra | `--extra-libtpu-init-flags` / `--extra-xla-flags` | adds new flags, overrides same-named ones, `!flag` drops one |
| 3. Environment | exported `LIBTPU_INIT_ARGS` / `XLA_FLAGS` | last word: overrides config values (logged as WARNING) and adds new flags |

Logging: removals and CLI overrides are `INFO`; an env value overriding a config value is a
`WARNING` ("already sets ... in the environment; keeping it and ignoring the config value").
`--debug.print-config` ([`DebugConfig.print_config`](../catalog/torchtitan/config/configs.md#DebugConfig.print_config))
prints the resolved flags, but the README cautions that torch_tpu can still override `XLA_FLAGS`
per compile via `TORCH_TPU_INTERNAL_XLA_OPTIONS` and a `custom_compiler_options` context manager.

### Named bundles (the perf knobs)

| Bundle | Flags | Purpose (from code comments) |
|---|---|---|
| [`SPARSECORE_LATENCY_HIDING_SCHEDULER`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#SPARSECORE_LATENCY_HIDING_SCHEDULER.SPARSECORE_LATENCY_HIDING_SCHEDULER) | `xla_tpu_enable_sparse_core_collective_aggregator`, `xla_tpu_enable_latency_hiding_layer_scheduler` | overlap FSDP collectives with compute; scheduler requires the aggregator |
| [`DUAL_SPARSECORE_REDUCE_SCATTER`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#DUAL_SPARSECORE_REDUCE_SCATTER.DUAL_SPARSECORE_REDUCE_SCATTER) | `xla_tpu_use_single_sparse_core_for_reduce_scatter_offload=false` | RS on both SparseCores; best for ZeRO-2 or dependency-ordered ZeRO-3 interleave |
| [`HIERARCHICAL_REDUCE_SCATTER`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#HIERARCHICAL_REDUCE_SCATTER.HIERARCHICAL_REDUCE_SCATTER) | dual-SC RS + ND RS offload + hierarchical RS | multi-dim RS split into stages; libtpu >= 0.0.47 |
| [`SELECTIVE_ICI_RS_PIPELINING`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#SELECTIVE_ICI_RS_PIPELINING.SELECTIVE_ICI_RS_PIPELINING) | `xla_tpu_enable_ici_rs_pipelining`, threshold 1024 KiB | pipeline small RS across the scan-backward loop back-edge |
| [`ICI_AG_PIPELINING`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#ICI_AG_PIPELINING.ICI_AG_PIPELINING) | `xla_tpu_enable_ici_ag_pipelining` | prefetch next layer's FSDP AG one scan iteration early (costs HBM) |
| [`SPARSECORE_ASYNC_ALL_GATHER`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#SPARSECORE_ASYNC_ALL_GATHER.SPARSECORE_ASYNC_ALL_GATHER) | async AG, prefer AG over AR, SC AG offload | offload FSDP AG to SparseCore |
| [`SPARSECORE_COLLECTIVE_OFFLOAD`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#SPARSECORE_COLLECTIVE_OFFLOAD.SPARSECORE_COLLECTIVE_OFFLOAD) | aggregator, LHS queuing, 2D/3D AG offload, RS offload | move AG/RS themselves off the TensorCore |
| [`CONVOLUTION_UNFUSING`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#CONVOLUTION_UNFUSING.CONVOLUTION_UNFUSING) | `xla_tpu_enable_convolution_unfusing` | unfuse elementwise from MXU matmuls when fusion hurts tile choice |
| [`TPU7X_THROUGHPUT_P_STATE`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#TPU7X_THROUGHPUT_P_STATE.TPU7X_THROUGHPUT_P_STATE) | `xla_tpu_dvfs_p_state=7` | v7x throughput power state; graph unchanged |
| [`DISABLE_ENHANCED_LAUNCH_BARRIER`](../catalog/torchtitan/experiments/tpu/tpu_flags.md#DISABLE_ENHANCED_LAUNCH_BARRIER.DISABLE_ENHANCED_LAUNCH_BARRIER) | `xla_tpu_use_enhanced_launch_barrier=false` | avoid distributed hangs; torch_tpu already forces it off when absent |

Worked composition: [`_LLAMA3_SCAN_FLAGS`](../catalog/torchtitan/experiments/tpu/llama3/config_registry.md#_LLAMA3_SCAN_FLAGS)
merges the p-state, `xla_tpu_scoped_vmem_limit_kib=131072`, the offload-copy flags, hierarchical RS,
RS/AG pipelining, SC async AG, the LHS bundle and convolution unfusing.

## Why it matters / when it applies
- Flags are part of what a recipe's measured MFU depends on; codifying them in config makes runs
  reproducible and diffable (`--debug.print-config`).
- Use `--extra-*` for A/B experiments on one flag without restating the recipe; use `!flag` to test
  a bundle member's contribution; use the bare `--libtpu-init-flags=''` to measure against defaults.
- An exported env var silently wins over the recipe (only a WARNING) - check logs when a flag sweep
  appears to have no effect.
- `xla_dump_to` is an XLA flag, not a libtpu one: put it in `--extra-xla-flags`; libtpu rejects it.

## Connections
- Code concepts: [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [job-config](../concepts/job-config.md), [config-overrides](../concepts/config-overrides.md),
  [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md)
- Module catalogs: [tpu_flags](../catalog/torchtitan/experiments/tpu/tpu_flags.md),
  [tpu_job_config](../catalog/torchtitan/experiments/tpu/tpu_job_config.md),
  [gmain](../catalog/torchtitan/experiments/tpu/gmain.md)
- Related doc-concepts: [tpu-multislice-hsdp-over-dcn](tpu-multislice-hsdp-over-dcn.md),
  [tpu-splash-attention-tiles-and-vmem](tpu-splash-attention-tiles-and-vmem.md),
  [tpu-scan-graph-splitter-cpu-offload](tpu-scan-graph-splitter-cpu-offload.md),
  [tpu-launch-and-profiling-workflow](tpu-launch-and-profiling-workflow.md),
  [tpu-recipe-libtpu-flag-sets](tpu-recipe-libtpu-flag-sets.md)

## Source
Extracted from `torchtitan/experiments/tpu/README.md` (section "Configuring XLA and libtpu flags"),
cross-checked against `torchtitan/experiments/tpu/tpu_flags.py` (kept in place).
