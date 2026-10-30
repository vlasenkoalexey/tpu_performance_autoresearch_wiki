---
title: TPU lane launch and profiling workflow (TPU VM, GKE, xprof)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# TPU lane launch and profiling workflow (TPU VM, GKE, xprof)

## Definition
The TPU README defines one entry point for every TorchTPU run -
`torchrun ... -m torchtitan.experiments.tpu.train --module=<tpu model pkg> --config=<recipe fn>` -
launched either directly on a single-host TPU VM (development, small models) or as a multi-host GKE
workload submitted with Cluster Toolkit's `gcluster job submit` (larger models). torchrun spawns
**one process per TensorCore**, and profiling is the standard TorchTitan `--profiler.*` block
exported as an xprof trace viewable in TensorBoard.

## In torchtitan (grounded)
- Entry: `torchtitan/experiments/tpu/train.py` runs `gmain.handle_main(start_trainer)`
  ([`handle_main`](../catalog/torchtitan/experiments/tpu/gmain.md#handle_main),
  [`start_trainer`](../catalog/torchtitan/experiments/tpu/train.md#start_trainer)). Config parsing is
  the core [`ConfigManager`](../catalog/torchtitan/config/manager.md#ConfigManager) (`--module` +
  `--config` select a registry function, CLI flags override fields).
- Before any device is touched, [`_start_trainer`](../catalog/torchtitan/experiments/tpu/gmain.md#_start_trainer)
  renders libtpu/XLA flags ([tpu-libtpu-xla-flag-layering](tpu-libtpu-xla-flag-layering.md)), then
  [`distributed_utils.maybe_init_distributed`](../catalog/torchtitan/experiments/tpu/distributed_utils.md#maybe_init_distributed)
  (delegating to [`cloud_distributed_utils.maybe_init_distributed`](../catalog/torchtitan/experiments/tpu/cloud_distributed_utils.md#maybe_init_distributed))
  derives TPU slice-builder addresses / topology from torchrun's `LOCAL_RANK`/`RANK`/`WORLD_SIZE`
  (GKE path [`_maybe_init_distributed_on_gke`](../catalog/torchtitan/experiments/tpu/cloud_distributed_utils.md#_maybe_init_distributed_on_gke),
  TPU-VM path [`_maybe_init_distributed_on_tpu_vm`](../catalog/torchtitan/experiments/tpu/cloud_distributed_utils.md#_maybe_init_distributed_on_tpu_vm)),
  and enters the configured `tpu_config.eager_mode` ([tpu-defer-and-fuse-eager-mode](tpu-defer-and-fuse-eager-mode.md)).
- [`start_trainer`](../catalog/torchtitan/experiments/tpu/train.md#start_trainer) dispatches on config
  type: a [`TpuGraphTrainer.Config`](../catalog/torchtitan/experiments/tpu/graph_trainer/tpu_graph_trainer.md#TpuGraphTrainer.Config)
  selects GraphTrainer, otherwise [`TPUTrainer`](../catalog/torchtitan/experiments/tpu/train.md#TPUTrainer).
  It also defaults `debug.seed` to 42 (a hang workaround) and inserts a barrier before trainer init.
- Profiling: [`Profiler.Config`](../catalog/torchtitan/tools/profiler.md#Profiler.Config) fields
  `enable_profiling`, `profile_freq`, `profiler_warmup`, `profiler_active` (validated so
  `profile_freq >= warmup + active`). The TPU lane patches the profiler via
  [`profiler_workaround.init`](../catalog/torchtitan/experiments/tpu/profiler_workaround.md#init);
  `tpu_config.use_jax_profiler` ([`TPUConfig.use_jax_profiler`](../catalog/torchtitan/experiments/tpu/tpu_job_config.md#TPUConfig.use_jax_profiler))
  routes capture through the JAX profiler.

### Canonical commands (from the README)

| Scenario | Command essentials |
|---|---|
| Single host, v6e-4, Qwen3 1.7B, no downloads | `torchrun --nproc_per_node=4 -m torchtitan.experiments.tpu.train --module=torchtitan.experiments.tpu.qwen3 --config=qwen3_1_7b --training.steps=10` |
| GKE v6e-8 (`2x4`, 2 hosts x 4 chips), Qwen3 8B FSDP | `torchrun --nnodes=2 --nproc_per_node=4 --rdzv_backend=static --rdzv_endpoint=$WORKERS_0_HOSTNAME:29501 --node_rank=$TPU_WORKER_ID ... --config=reg_trainer_qwen3_8b --libtpu-init-flags="xla_tpu_use_enhanced_launch_barrier=false xla_tpu_scoped_vmem_limit_kib=65536"` |
| Profiling add-on | `--profiler.enable_profiling --profiler.profile_freq=5 --profiler.profiler_warmup=3 --profiler.profiler_active=1 --metrics.enable_tensorboard` |
| Multi-slice | see [tpu-multislice-hsdp-over-dcn](tpu-multislice-hsdp-over-dcn.md) |

Recipes referenced: [`qwen3_1_7b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#qwen3_1_7b),
[`reg_trainer_qwen3_8b`](../catalog/torchtitan/experiments/tpu/qwen3/config_registry.md#reg_trainer_qwen3_8b).

### Install / image knobs that affect measurements
- Option A (recommended): `torch==2.15.0 torch_tpu==0.2.0` + `experiments/tpu/requirements.txt`,
  Python 3.14; Option B: build the torch_tpu wheel from source (`bazel build --config=wheel_common
  //ci/wheel:torch_tpu_wheel`) for the PyTorch nightly. The optimization guide warns: build wheels
  with optimizations on (`-c opt`); a fastbuild wheel has dramatically slower eager dispatch and
  silently ruins every measurement.
- The Docker image (`experiments/tpu/Dockerfile`) takes `TORCH_TPU_VERSION`, `TORCH_VERSION`,
  `TORCH_INDEX_URL` build args, or a locally copied wheel.
- After a hard crash, `rm -f /tmp/libtpu_lockfile` or the next run may fail to init the device.

### GKE provisioning shape
Cluster Toolkit blueprint `examples/gke-tpu-v6e/gke-tpu-v6e.yaml` with `machine_type`
(e.g. `ct6e-standard-4t`), `tpu_topology` (e.g. `2x4`), `num_slices`, and `enable_gcsfuse_csi=true`.
It creates a VPC with MTU 8896 "for optimal performance", installs Kueue + JobSet, and a GCS bucket
can be mounted per job (`--mount "$BUCKET;/data;rw"` + `--service-account workload-identity-k8s-sa`)
to export logs and profiles.

## Why it matters / when it applies
- `--nproc_per_node` must equal the TensorCores per host (4 on a v6e host here, 8 on a v7x VM); this
  also multiplies any per-process host-memory reservation (MegaScale pool, offload budget).
- Profile only steady-state steps: warmup must cover compilation; TorchTitan's own guidance is at
  least 10 steps for perf tests.
- The trace is read with TensorBoard + `tensorboard_plugin_profile` / `xprof`:
  `tensorboard --logdir=$BUCKET/<workload>/rank_0`.

**Doc vs code:** the README says traces land in `--dump_folder` + `profile_trace`; at this commit the
core default `Profiler.Config.save_traces_folder` is `profiling/traces` (and `TPUTrainerConfig`
defaults `dump_folder` to `/tmp/outputs` when unset), so look under `<dump_folder>/profiling/traces`
unless overridden.

## Connections
- Code concepts: [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md),
  [trainer-and-train-loop](../concepts/trainer-and-train-loop.md),
  [observability](../concepts/observability.md),
  [debug-and-profiling-tools](../concepts/debug-and-profiling-tools.md),
  [qwen3-model](../concepts/qwen3-model.md), [job-config](../concepts/job-config.md)
- Module catalogs: [train (tpu)](../catalog/torchtitan/experiments/tpu/train.md),
  [gmain](../catalog/torchtitan/experiments/tpu/gmain.md),
  [cloud_distributed_utils](../catalog/torchtitan/experiments/tpu/cloud_distributed_utils.md),
  [profiler_workaround](../catalog/torchtitan/experiments/tpu/profiler_workaround.md),
  [tools/profiler](../catalog/torchtitan/tools/profiler.md)
- Related doc-concepts: [tpu-multislice-hsdp-over-dcn](tpu-multislice-hsdp-over-dcn.md),
  [tpu-libtpu-xla-flag-layering](tpu-libtpu-xla-flag-layering.md),
  [tpu-dispatch-bound-mental-model](tpu-dispatch-bound-mental-model.md),
  [a3-mega-gpu-multinode-guides](a3-mega-gpu-multinode-guides.md),
  [torchtitan-tpu-distribution](torchtitan-tpu-distribution.md), [tpu-recipe-matrix](tpu-recipe-matrix.md)

## Source
Extracted from `torchtitan/experiments/tpu/README.md` (single-host, GKE, profiling and cleanup
sections; kept in place). Operational notes from `torchtitan/experiments/tpu/torch-tpu-optimization-guide.md`.
