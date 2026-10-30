---
title: 'Area: torchtitan/components'
type: area
area: 'torchtitan/components'
description: 'Training components of torchtitan: data loading, checkpointing, optimizers and LR schedulers, quantization converters, loss/metrics/validation.'
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Area: `torchtitan/components`

## Purpose
`torchtitan/components/` holds the pieces the trainer assembles around a model: the token-budget data pipeline ([data-loading](../concepts/data-loading.md)), distributed checkpointing ([checkpointing](../concepts/checkpointing.md)), optimizer containers and LR schedulers ([optimizers-and-lr-schedulers](../concepts/optimizers-and-lr-schedulers.md)), and the model converters that swap in float8 / MXFP8 / NVFP4 linears ([quantization](../concepts/quantization.md)). The top-level modules (loss, metrics, validation, tokenizer, fault tolerance glue) are covered by [training-components](../concepts/training-components.md).

Each component is a `Configurable` whose `Config` is a field on the job config ([job-config](../concepts/job-config.md)), so choosing an implementation (foreach vs fused optimizer, chunked loss, a quantization recipe) is a config diff rather than code. For TPU the relevant facts are that batches have a fixed token shape, the upstream quantization converters are CUDA-only, and TPU recipes use the foreach optimizer.

## How the units connect
- [trainer-and-train-loop](../concepts/trainer-and-train-loop.md) builds every component from its config and drives them each step.
- [data-loading](../concepts/data-loading.md) feeds packed, fixed-size token batches; [hf-datasets](../concepts/hf-datasets.md) provides the Hugging Face sources it wraps.
- [optimizers-and-lr-schedulers](../concepts/optimizers-and-lr-schedulers.md) and [checkpointing](../concepts/checkpointing.md) share state through the trainer's stateful containers; [quantization](../concepts/quantization.md) rewrites modules before parallelization ([parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md)).

<!-- area:auto:begin -->
## Units
5 planned unit(s) in `torchtitan/components`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `torchtitan/components` | 5 | 230 | 125 | [`CrossEntropyLoss`](../catalog/torchtitan/components/loss.md#CrossEntropyLoss "torchtitan/components/loss.py:L287"), [`global_vocab_size`](../catalog/torchtitan/components/loss.md#CrossEntropyLoss.Config.global_vocab_size "torchtitan/components/loss.py:L292"), [`ChunkedLossWrapper`](../catalog/torchtitan/components/loss.md#ChunkedLossWrapper "torchtitan/components/loss.py:L515") | [training-components](../concepts/training-components.md) |
| `torchtitan/components/data` | 7 | 168 | 114 | [`GrainDataLoader`](../catalog/torchtitan/components/data/loader.md#GrainDataLoader "torchtitan/components/data/loader.py:L61"), [`Config`](../catalog/torchtitan/components/data/loader.md#GrainDataLoader.Config "torchtitan/components/data/loader.py:L65"), [`dataset`](../catalog/torchtitan/components/data/loader.md#GrainDataLoader.Config.dataset "torchtitan/components/data/loader.py:L66") | [data-loading](../concepts/data-loading.md) |
| `torchtitan/components/checkpointer` | 5 | 159 | 67 | [`CheckpointManager`](../catalog/torchtitan/components/checkpointer/dcp.md#CheckpointManager "torchtitan/components/checkpointer/dcp.py:L89"), [`Config`](../catalog/torchtitan/components/checkpointer/dcp.md#CheckpointManager.Config "torchtitan/components/checkpointer/dcp.py:L136"), [`interval`](../catalog/torchtitan/components/checkpointer/base.md#BaseCheckpointManager.Config.interval "torchtitan/components/checkpointer/base.py:L538") | [checkpointing](../concepts/checkpointing.md) |
| `torchtitan/components/optimizer` | 4 | 74 | 81 | [`LRSchedulersContainer`](../catalog/torchtitan/components/optimizer/lr_scheduler.md#LRSchedulersContainer "torchtitan/components/optimizer/lr_scheduler.py:L25"), [`Config`](../catalog/torchtitan/components/optimizer/lr_scheduler.md#LRSchedulersContainer.Config "torchtitan/components/optimizer/lr_scheduler.py:L51"), [`warmup_steps`](../catalog/torchtitan/components/optimizer/lr_scheduler.md#LRSchedulersContainer.Config.warmup_steps "torchtitan/components/optimizer/lr_scheduler.py:L52") | [optimizers-and-lr-schedulers](../concepts/optimizers-and-lr-schedulers.md) |
| `torchtitan/components/quantization` | 9 | 143 | 21 | [`model_compile_enabled`](../catalog/torchtitan/components/quantization/__init__.md#QuantizationConverter.Config.model_compile_enabled "torchtitan/components/quantization/__init__.py:L30"), [`Config`](../catalog/torchtitan/components/quantization/nvfp4.md#NVFP4LinearConverter.Config "torchtitan/components/quantization/nvfp4.py:L271"), [`NVFP4LinearConverter`](../catalog/torchtitan/components/quantization/nvfp4.md#NVFP4LinearConverter "torchtitan/components/quantization/nvfp4.py:L267") | [quantization](../concepts/quantization.md) |

<!-- area:auto:end -->
