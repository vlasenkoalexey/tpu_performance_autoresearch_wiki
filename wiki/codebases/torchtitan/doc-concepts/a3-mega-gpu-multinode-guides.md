---
title: A3 Mega (H100) multi-node launch guides - XPK/GKE and Slurm (GPU, not TPU)
type: doc-concept
provenance: doc
source: torchtitan/experiments/tpu/torchtitan-gke-xpk.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# A3 Mega (H100) multi-node launch guides - XPK/GKE and Slurm (GPU, not TPU)

## Definition
Two operational guides that live in the TPU experiment directory but describe **GPU** training:
Llama 3.1 70B on GCP A3 Mega (`h100-mega-80gb-8`, GPUDirect-TCPXO networking), provisioned either
as an XPK-managed GKE cluster or as a Cluster Toolkit Slurm cluster. They run upstream
`-m torchtitan.train` (not the TPU entry point) with NCCL/TCPXO environment tuning and an FP8 + FSDP
+ `torch.compile` configuration. They are useful as a GPU comparison baseline for TPU lane results,
not as TPU recipes.

## In torchtitan (grounded)
- Entry point: core `torchtitan/train.py` ([`main`](../catalog/torchtitan/train.md#main)) with config
  parsing by [`ConfigManager`](../catalog/torchtitan/config/manager.md#ConfigManager); the 70B
  model config is [`llama3_70b`](../catalog/torchtitan/models/llama3/config_registry.md#llama3_70b).
- FP8: [`Float8LinearConverter`](../catalog/torchtitan/components/quantization/float8.md#Float8LinearConverter)
  (torchao `Float8Linear` swap), see the [float8-training](float8-training.md) doc-concept.
- Profiling / metrics: [`Profiler.Config`](../catalog/torchtitan/tools/profiler.md#Profiler.Config)
  and the TensorBoard logger in [components/metrics](../catalog/torchtitan/components/metrics.md).
- The repo-root `multinode_trainer.slurm` that the Slurm guide copies now launches
  `torchrun --nnodes 4 --nproc_per_node 8 ... -m torchtitan.train --module ${MODULE} --config ${CONFIG}`.

### Perf-relevant settings the guides use
| Area | Setting |
|---|---|
| Parallelism | FSDP across nodes (`data_parallel_shard_degree=4` for 4 nodes) |
| Compile | `compile.enable=true` |
| FP8 | float8 Linear converter with FP8 FSDP all-gather and precomputed dynamic scales |
| NCCL (XPK) | `NCCL_SOCKET_IFNAME=eth0`, `NCCL_FASTRAK_CTRL_DEV=eth0`, `NCCL_FASTRAK_IFNAME=eth1..eth8`, source `nccl-env-profile.sh`; `PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True` |
| NCCL (Slurm) | `NCCL_BUFFSIZE=2097152`, FASTRAK ifnames `enp*`, `NCCL_FASTRAK_LLCM_DEVICE_DIRECTORY=/dev/aperture_devices`; `dcgmi profile --pause/--resume` around the run |
| Storage | GCS FUSE mount at `/data` (XPK: `xpk storage attach --type=gcsfuse`; Slurm: patched blueprint mounting `/gcs` on login + compute nodes) for tokenizer, checkpoints, traces |
| Validation | run the NCCL test workload before training |

Operational gotchas recorded by the guides: XPK built from source with a manual patch commenting out
an extra reservation placement policy in `blueprint_generator.py`; Slurm cluster name must match
`^[a-z](?:[a-z0-9]{0,9})$`; clean up VPC peerings after a failed deploy.

## Why it matters / when it applies
Use these only when standing up a GPU reference run to compare against TPU numbers (same model,
FSDP + compile + FP8). Nothing here applies to TorchTPU: TPU launches use
`-m torchtitan.experiments.tpu.train` with one process per TensorCore
([tpu-launch-and-profiling-workflow](tpu-launch-and-profiling-workflow.md)).

**Doc vs code (stale CLI):** both guides use the pre-registry CLI - `--job.config_file
llama3_70b.toml` (copied from `torchtitan/models/llama3/train_configs/`, which no longer exists),
`--model.converters '["quantize.linear.float8"]'`,
`--quantize.linear.float8.enable_fsdp_float8_all_gather`,
`--quantize.linear.float8.precompute_float8_dynamic_scale_for_fsdp`,
`--profiling.save_traces_folder`, `--metrics.save_tb_folder`. At this commit configs are Python
registry functions selected by `--module` / `--config`, float8 is configured through
`Float8LinearConverter.Config` (no `enable_fsdp_float8_all_gather` / `precompute_float8_...` fields
exist), the profiler block is `--profiler.*`, and the TensorBoard folder lives on the metrics config
(`save_tb_folder`). Expect to translate every flag before running.

## Connections
- Code concepts: [quantization](../concepts/quantization.md),
  [trainer-and-train-loop](../concepts/trainer-and-train-loop.md),
  [job-config](../concepts/job-config.md), [llama3-model](../concepts/llama3-model.md),
  [observability](../concepts/observability.md)
- Module catalogs: [train (core)](../catalog/torchtitan/train.md),
  [config/manager](../catalog/torchtitan/config/manager.md),
  [components/quantization/float8](../catalog/torchtitan/components/quantization/float8.md),
  [models/llama3/config_registry](../catalog/torchtitan/models/llama3/config_registry.md)
- Related doc-concepts: [float8-training](float8-training.md),
  [tpu-launch-and-profiling-workflow](tpu-launch-and-profiling-workflow.md)

## Source
Extracted from `torchtitan/experiments/tpu/torchtitan-gke-xpk.md` and
`torchtitan/experiments/tpu/torchtitan-slurm.md` (both kept in place).
