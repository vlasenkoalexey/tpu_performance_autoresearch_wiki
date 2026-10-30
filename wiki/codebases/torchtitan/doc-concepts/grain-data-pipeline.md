---
title: Grain data pipeline (source -> dataset -> compose -> GrainDataLoader)
type: doc-concept
provenance: doc
source: torchtitan/components/data/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Grain data pipeline (source -> dataset -> compose -> GrainDataLoader)

## Definition
TorchTitan uses **one Grain-based data pipeline** for text pretraining, SFT, and image/multimodal
training. A run's data is a config tree with five layers: a **source** (random-access or
streaming), a **single dataset** (pre-filter -> process -> post-filter over that source), optional
**composition** (mix, concatenate, pack), the **loader** (convert to iterable if needed -> batch
-> collate -> prefetch), and finally the trainer consuming a batch per step.

## In torchtitan (grounded)
- Sources: [`SourceConfig`](../catalog/torchtitan/components/data/sources.md#SourceConfig),
  [`RandomAccessDataSource`](../catalog/torchtitan/components/data/sources.md#RandomAccessDataSource),
  [`IndexedJsonlSource`](../catalog/torchtitan/components/data/sources.md#IndexedJsonlSource) (one JSON
  object per line), [`HuggingFaceRandomAccessSource`](../catalog/torchtitan/components/data/sources.md#HuggingFaceRandomAccessSource "torchtitan/components/data/sources.py:L94")
  (materialized HF dataset) and [`HuggingFaceStreamingSource`](../catalog/torchtitan/components/data/sources.md#HuggingFaceStreamingSource "torchtitan/components/data/sources.py:L145")
  (no materialization).
- Dataset stage: [`SingleDatasetConfig`](../catalog/torchtitan/components/data/dataset.md#SingleDatasetConfig "torchtitan/components/data/dataset.py:L84")
  with a [`SampleProcessor`](../catalog/torchtitan/components/data/dataset.md#SampleProcessor "torchtitan/components/data/dataset.py:L67") producing
  e.g. [`TextSequence`](../catalog/torchtitan/components/data/dataset.md#TextSequence "torchtitan/components/data/dataset.py:L39"); processors
  receive a [`DatasetBuildContext`](../catalog/torchtitan/components/data/types.md#DatasetBuildContext "torchtitan/components/data/types.py:L17"),
  sources a [`DatasetIterationPolicy`](../catalog/torchtitan/components/data/types.md#DatasetIterationPolicy "torchtitan/components/data/types.py:L28").
  Text processors: [`TextProcessor`](../catalog/torchtitan/hf_datasets/text_datasets.md#TextProcessor "torchtitan/hf_datasets/text_datasets.py:L32")
  (pretraining) and [`ChatProcessor`](../catalog/torchtitan/hf_datasets/text_datasets.md#ChatProcessor "torchtitan/hf_datasets/text_datasets.py:L61")
  (applies the chat template, masks prompt labels to `IGNORE_INDEX`).
- Loader: [`GrainDataLoader`](../catalog/torchtitan/components/data/loader.md#GrainDataLoader "torchtitan/components/data/loader.py:L61") /
  [`GrainDataLoader.Config`](../catalog/torchtitan/components/data/loader.md#GrainDataLoader.Config "torchtitan/components/data/loader.py:L65")
  (`dataset`, `collator`, `seed`, `shuffle`, `repeat`, `streaming_shuffle_buffer_size`,
  `read_options`, `num_prefetch_batches`).
- Multimodal: [`MultiModalProcessor`](../catalog/torchtitan/hf_datasets/multimodal/mm_datasets.md#MultiModalProcessor "torchtitan/hf_datasets/multimodal/mm_datasets.py:L275"),
  [`MMSamplePackingConfig`](../catalog/torchtitan/hf_datasets/multimodal/mm_datasets.md#MMSamplePackingConfig),
  [`MultiModalCollator`](../catalog/torchtitan/hf_datasets/multimodal/mm_collator.md#MultiModalCollator "torchtitan/hf_datasets/multimodal/mm_collator.py:L22")
  - same source/dataset/loader/sharding/checkpoint contracts, modality-specific samples, model-specific
  collation.
- **TPU lane:** [`TPUGrainDataLoader`](../catalog/torchtitan/experiments/tpu/datasets.md#TPUGrainDataLoader)
  wraps `GrainDataLoader` to keep the TPU CLI flags `dataset` / `dataset_path` working, and
  [`c4_test_dataloader`](../catalog/torchtitan/experiments/tpu/datasets.md#c4_test_dataloader)
  builds the packed `c4_test` loader used by TPU test recipes.

## Why it matters / when it applies
- **Input stalls are a step-time term.** The loader runs ahead of the trainer:
  `num_prefetch_batches` is how many complete, collated batches may wait (while the trainer
  computes batch 10, a background thread prepares 11 and 12). On fast TPU steps an undersized
  prefetch or slow processor shows up as host-side gaps before each step.
- **Map vs iter datasets.** A random-access source becomes a `MapDataset`; packing (and any mix
  containing a stream) converts children to `IterDataset`, and the loader converts if nothing earlier
  did. Each Map->Iter conversion has its own `read_options` (`num_threads` concurrent indexed reads,
  `prefetch_buffer_size` samples waiting). An all-map mix converts once; a mix with a stream converts
  each map child separately - multiplying threads/buffers.
- **Streaming shuffle** keeps `streaming_shuffle_buffer_size` raw rows for approximate shuffling;
  bigger mixes better but costs host memory.
- **SFT changes the processor and packing policy, not the loader**; custom image augmentation
  belongs in a `SampleProcessor`; a pretokenized corpus is just a custom `RandomAccessDataSource`
  (e.g. memmap + document offsets) reusing the normal processing/packing configs.
- `TrainerBatch` (the loader's output type named in the doc) is not a separately indexed symbol at
  this commit.

## Connections
- Code concepts: [data-loading](../concepts/data-loading.md),
  [hf-datasets](../concepts/hf-datasets.md),
  [trainer-and-train-loop](../concepts/trainer-and-train-loop.md),
  [tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md).
- Module catalogs: [torchtitan/components/data/sources](../catalog/torchtitan/components/data/sources.md),
  [torchtitan/components/data/dataset](../catalog/torchtitan/components/data/dataset.md),
  [torchtitan/components/data/loader](../catalog/torchtitan/components/data/loader.md),
  [torchtitan/components/data/packing](../catalog/torchtitan/components/data/packing.md),
  [torchtitan/experiments/tpu/datasets](../catalog/torchtitan/experiments/tpu/datasets.md).
- Related doc-concepts: [dataset-mixing-and-packing](dataset-mixing-and-packing.md),
  [data-parallel-sharding-and-loader-state](data-parallel-sharding-and-loader-state.md).

## Source
Extracted from `torchtitan/components/data/README.md` (kept in place).
