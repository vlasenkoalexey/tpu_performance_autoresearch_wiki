---
title: Data ownership under parallelism and loader checkpoint state
type: doc-concept
provenance: doc
source: torchtitan/components/data/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Data ownership under parallelism and loader checkpoint state

## Definition
Only the **effective data-parallel coordinate** selects data: effective DP =
`data_parallel_replicate_degree * data_parallel_shard_degree`. Different effective-DP ranks read
disjoint source rows; TP, PP, and CP peers of the same DP coordinate read the same rows. Data
ownership is fixed before batching, and the loader's full position is part of the training
checkpoint.

## In torchtitan (grounded)
- The degrees come from [`ParallelismConfig.data_parallel_replicate_degree`](../catalog/torchtitan/config/configs.md#ParallelismConfig.data_parallel_replicate_degree "torchtitan/config/configs.py:L149")
  and [`ParallelismConfig.data_parallel_shard_degree`](../catalog/torchtitan/config/configs.md#ParallelismConfig.data_parallel_shard_degree "torchtitan/config/configs.py:L160").
- Ownership by stage: random-access source -> global shuffle -> contiguous balanced DP shard; HF
  stream -> source-level DP shard; [`DatasetMixConfig`](../catalog/torchtitan/components/data/dataset.md#DatasetMixConfig)
  combines children already owned by the rank; [`DatasetConcatConfig`](../catalog/torchtitan/components/data/dataset.md#DatasetConcatConfig)
  concatenates, shuffles globally, then shards; packing runs locally per rank;
  [`GrainDataLoader`](../catalog/torchtitan/components/data/loader.md#GrainDataLoader "torchtitan/components/data/loader.py:L61") batches and
  collates that rank's samples.
- Checkpointing: [`GrainDataLoader.state_dict`](../catalog/torchtitan/components/data/loader.md#GrainDataLoader.state_dict) /
  [`load_state_dict`](../catalog/torchtitan/components/data/loader.md#GrainDataLoader.load_state_dict)
  record source cursors, shuffle/repeat progress, mix-child and packing-buffer state, batching and
  prefetch state, and the effective DP degree; the trainer saves it through
  [`CheckpointManager`](../catalog/torchtitan/components/checkpointer/dcp.md#CheckpointManager "torchtitan/components/checkpointer/dcp.py:L89").
- Guard (from code): the loader raises if effective DP > 1 and
  [`repeat`](../catalog/torchtitan/components/data/loader.md#GrainDataLoader.Config.repeat) is `False`.

## Why it matters / when it applies
- **Changing CP/TP/PP does not change what data a DP rank sees**, so parallelism sweeps on a fixed
  DP degree compare like for like on data. Changing the DP degree (e.g. trading FSDP for TP on the
  same chip count) changes data ownership.
- **Shards are of the shuffled index space**, not contiguous corpus regions.
- **`repeat=False` with DP > 1 is rejected** because ranks can exhaust at different steps and hang
  the training collectives; use `repeat=True` and let the trainer's step count stop training. A hang
  on a collective near an epoch boundary is the symptom this guard prevents.
- **Resume is strict:** it requires unchanged code, config, source contents, tokenizer, **and
  effective DP degree**. Re-sharding a run onto a different DP degree (e.g. moving from v6e-8 to
  v6e-32 with more FSDP) cannot restore the loader position - plan the resume or accept a data
  restart.

## Connections
- Code concepts: [data-loading](../concepts/data-loading.md),
  [checkpointing](../concepts/checkpointing.md),
  [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md).
- Module catalogs: [torchtitan/components/data/loader](../catalog/torchtitan/components/data/loader.md),
  [torchtitan/components/data/dataset](../catalog/torchtitan/components/data/dataset.md),
  [torchtitan/config/configs](../catalog/torchtitan/config/configs.md).
- Related doc-concepts: [grain-data-pipeline](grain-data-pipeline.md),
  [dataset-mixing-and-packing](dataset-mixing-and-packing.md).

## Source
Extracted from `torchtitan/components/data/README.md` (kept in place).
