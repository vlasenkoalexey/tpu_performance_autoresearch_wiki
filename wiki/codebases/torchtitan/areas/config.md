---
title: 'Area: torchtitan/config'
type: area
area: 'torchtitan/config'
description: 'Job configuration of torchtitan: the frozen Config tree, recipe registry functions and the CLI that selects and overrides them.'
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Area: `torchtitan/config`

## Purpose
`torchtitan/config/` defines the job configuration: a tree of dataclass `Config`s (training, parallelism, compile, activation checkpointing, checkpoint, profiling, ...) that recipes build in Python and the CLI can override. [job-config](../concepts/job-config.md) explains the tree, recipe functions and the frozen-CLI rules (the model tree is not CLI-addressable; derived values do not follow later flags).

For TPU work this is where parallelism degrees, compile and activation-checkpointing modes live; the TPU lane extends it with its own trainer config ([tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md)), which also carries the libtpu/XLA flag maps.

## How the units connect
- [job-config](../concepts/job-config.md) is consumed by [trainer-and-train-loop](../concepts/trainer-and-train-loop.md); its parallelism block becomes the device mesh in [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md).
- Config transforms and overrides are applied through [config-overrides](../concepts/config-overrides.md) and the model-spec traversal in [model-spec-protocols](../concepts/model-spec-protocols.md).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `torchtitan/config`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `torchtitan/config` | 11 | 147 | 235 | [`ParallelismConfig`](../catalog/torchtitan/config/configs.md#ParallelismConfig "torchtitan/config/configs.py:L123"), [`TrainingConfig`](../catalog/torchtitan/config/configs.md#TrainingConfig "torchtitan/config/configs.py:L36"), [`max_context_length`](../catalog/torchtitan/config/configs.md#TrainingConfig.max_context_length "torchtitan/config/configs.py:L51") | [job-config](../concepts/job-config.md) |

<!-- area:auto:end -->
