---
title: TorchFT replica-group fault tolerance (HSDP across independent instances)
type: doc-concept
provenance: doc
source: torchtitan/experiments/torchft/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# TorchFT replica-group fault tolerance (HSDP across independent instances)

## Definition
TorchFT adds fault tolerance to training with **replicated** weights (DDP/HSDP). Instead of one job with a `(replicate, shard)` mesh, you launch one TorchTitan instance per **replica group**; each instance shards weights internally (FSDP), and the groups replicate across each other through TorchFT. A lighthouse service tracks quorum, so when one group fails the others keep training without losing weights - no stop-and-restore from the last checkpoint.

## In torchtitan (grounded)
- Trainer: [`FaultTolerantTrainer`](../catalog/torchtitan/experiments/torchft/trainer.md#FaultTolerantTrainer) extends core `Trainer`; [`FaultTolerantTrainer.init_distributed`](../catalog/torchtitan/experiments/torchft/trainer.md#FaultTolerantTrainer.init_distributed) builds the TorchFT manager and [`FaultTolerantTrainer.train_step`](../catalog/torchtitan/experiments/torchft/trainer.md#FaultTolerantTrainer.train_step) runs under it.
- Manager: [`TorchFTManager`](../catalog/torchtitan/experiments/torchft/manager.md#TorchFTManager) with [`TorchFTManager.Config`](../catalog/torchtitan/experiments/torchft/manager.md#TorchFTManager.Config): [`enable`](../catalog/torchtitan/experiments/torchft/manager.md#TorchFTManager.Config.enable), [`replica_id`](../catalog/torchtitan/experiments/torchft/manager.md#TorchFTManager.Config.replica_id), [`group_size`](../catalog/torchtitan/experiments/torchft/manager.md#TorchFTManager.Config.group_size), [`min_replica_size`](../catalog/torchtitan/experiments/torchft/manager.md#TorchFTManager.Config.min_replica_size), [`process_group`](../catalog/torchtitan/experiments/torchft/manager.md#TorchFTManager.Config.process_group) (`gloo` default or `nccl`), [`process_group_timeout_ms`](../catalog/torchtitan/experiments/torchft/manager.md#TorchFTManager.Config.process_group_timeout_ms). Cross-group gradient all-reduce is hooked in by [`TorchFTManager.maybe_set_all_reduce_hook`](../catalog/torchtitan/experiments/torchft/manager.md#TorchFTManager.maybe_set_all_reduce_hook); [`TorchFTManager.get_dp_info`](../catalog/torchtitan/experiments/torchft/manager.md#TorchFTManager.get_dp_info) folds the replica group into the dataloader's DP rank/degree.
- State: [`TorchFTCheckpointManager`](../catalog/torchtitan/experiments/torchft/checkpoint.md#TorchFTCheckpointManager) (the alive group with the smallest replica ID saves checkpoints) and [`TorchFTOptimizersContainer`](../catalog/torchtitan/experiments/torchft/optimizer.md#TorchFTOptimizersContainer).
- Recipe: [`llama3_torchft_debugmodel`](../catalog/torchtitan/experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel) (`MODULE=torchft.llama3`).

## Why it matters / when it applies
- Example from the README: HSDP 2 x 4 on 8 GPUs normally runs as `--parallelism.data_parallel_replicate_degree=2 --parallelism.data_parallel_shard_degree=4`. With TorchFT it becomes two instances of 4 GPUs each (`--fault_tolerance.enable --fault_tolerance.group_size=2 --fault_tolerance.replica_id={0,1} --parallelism.data_parallel_shard_degree=4`) plus a `torchft_lighthouse --min_replicas 1 ...` process.
- When enabled, `data_parallel_replicate_degree` must stay 1; the replicate dimension is dynamic and bounded by `group_size`.
- Environment: `TORCHFT_LIGHTHOUSE` (default `http://localhost:29510`), `TORCHFT_MANAGER_PORT`, `REPLICA_GROUP_ID`, plus Rust logging/backtrace vars.
- **TPU relevance.** GPU/NCCL-or-gloo only at this commit. The replicate-across-groups / shard-within-group structure is the same HSDP shape the TPU lane uses across slices over DCN (see [tpu-multislice-hsdp-over-dcn](tpu-multislice-hsdp-over-dcn.md)), but without per-group failure recovery.

**Doc vs code at this commit:** the README presents Example 1 as plain per-step fault-tolerant HSDP and Example 2 as "semi-synchronous". Both use the same command, and the referenced `llama3_torchft_debugmodel` config already sets `semi_sync_method="diloco"`, `sync_steps=10`, `num_fragments=2`, `process_group="nccl"`. So Example 1 as written also runs DiLoCo. To get per-step synchronous FT you have to clear `semi_sync_method`. See [torchft-semi-sync-diloco](torchft-semi-sync-diloco.md).

## Connections
- Code concepts: [trainer-and-train-loop](../concepts/trainer-and-train-loop.md), [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md), [checkpointing](../concepts/checkpointing.md), [optimizers-and-lr-schedulers](../concepts/optimizers-and-lr-schedulers.md)
- Module catalogs: [torchft/trainer](../catalog/torchtitan/experiments/torchft/trainer.md), [torchft/manager](../catalog/torchtitan/experiments/torchft/manager.md), [torchft/checkpoint](../catalog/torchtitan/experiments/torchft/checkpoint.md), [torchft/llama3/config_registry](../catalog/torchtitan/experiments/torchft/llama3/config_registry.md)
- Related doc-concepts: [torchft-semi-sync-diloco](torchft-semi-sync-diloco.md), [tpu-multislice-hsdp-over-dcn](tpu-multislice-hsdp-over-dcn.md), [experiments-contribution-contract](experiments-contribution-contract.md)

## Source
Extracted from `torchtitan/experiments/torchft/README.md` (kept in place).
