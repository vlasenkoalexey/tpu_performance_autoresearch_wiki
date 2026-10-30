---
title: Dataset mixing, concatenation, and sequence packing
type: doc-concept
provenance: doc
source: torchtitan/components/data/README.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Dataset mixing, concatenation, and sequence packing

## Definition
Composition configs combine one or more child dataset configs before the loader. **Mixing** draws
from children by relative weight; **concatenation** treats finite children as one corpus where
every row appears once (sizes set proportions); **packing** fills fixed-length rows from variable
length samples. Where packing sits relative to mixing decides what the weights count.

## In torchtitan (grounded)
- Mixing: [`DatasetMixConfig`](../catalog/torchtitan/components/data/dataset.md#DatasetMixConfig) of
  [`WeightedDataset`](../catalog/torchtitan/components/data/dataset.md#WeightedDataset) entries
  (any positive weights, normalized internally).
- Concatenation: [`DatasetConcatConfig`](../catalog/torchtitan/components/data/dataset.md#DatasetConcatConfig)
  - globally shuffles the combined finite index space, then DP-shards.
- Packing: [`ConcatThenSplitPackingConfig`](../catalog/torchtitan/components/data/packing.md#ConcatThenSplitPackingConfig "torchtitan/components/data/packing.py:L22")
  (pretraining: concatenate documents then split into rows) and
  [`FirstFitPackingConfig`](../catalog/torchtitan/components/data/packing.md#FirstFitPackingConfig)
  (SFT: first-fit bin packing of whole samples); multimodal uses
  [`MMSamplePackingConfig`](../catalog/torchtitan/hf_datasets/multimodal/mm_datasets.md#MMSamplePackingConfig),
  whose `num_packing_bins` is the number of candidate packed rows kept open (not an input buffer).
- Repeat policy: [`GrainDataLoader.Config.repeat`](../catalog/torchtitan/components/data/loader.md#GrainDataLoader.Config.repeat)
  repeats the whole composed dataset; it does not change a child's share.

## Why it matters / when it applies
- **Mix before packing -> weights count documents.** `ConcatThenSplitPackingConfig(dataset=mix)`.
- **Pack each child before mixing -> weights count fixed-length rows (i.e. tokens).**
  `DatasetMixConfig([WeightedDataset(ConcatThenSplitPackingConfig(books), 0.67), ...])`.
  Choose this when the target ratio is a token ratio.
- **Exact duplication vs frequency.** To include a finite child k times per epoch, repeat it k times
  inside `DatasetConcatConfig`; use mixing when you want relative selection frequency or have
  streaming children.
- **Packing and attention metadata.** Packed rows carry several documents; models consume the
  per-document boundaries through position ids / varlen offsets or block masks (e.g. DeepSeek-V3 MTP
  uses position resets to avoid crossing documents, see
  [deepseek-v3-multi-token-prediction](deepseek-v3-multi-token-prediction.md)). Packing is what keeps
  every TPU step at a fixed, padding-free shape - the static-shape property XLA compilation wants.
- Automatic weight adjustment from observed document or supervised-token counts is not implemented;
  a custom mix can keep moving averages and rebalance.
- Packing runs **locally on each DP rank** after data ownership is decided (see
  [data-parallel-sharding-and-loader-state](data-parallel-sharding-and-loader-state.md)).

## Connections
- Code concepts: [data-loading](../concepts/data-loading.md),
  [hf-datasets](../concepts/hf-datasets.md).
- Module catalogs: [torchtitan/components/data/dataset](../catalog/torchtitan/components/data/dataset.md),
  [torchtitan/components/data/packing](../catalog/torchtitan/components/data/packing.md),
  [torchtitan/hf_datasets/multimodal/mm_datasets](../catalog/torchtitan/hf_datasets/multimodal/mm_datasets.md).
- Related doc-concepts: [grain-data-pipeline](grain-data-pipeline.md),
  [data-parallel-sharding-and-loader-state](data-parallel-sharding-and-loader-state.md).

## Source
Extracted from `torchtitan/components/data/README.md` (kept in place).
