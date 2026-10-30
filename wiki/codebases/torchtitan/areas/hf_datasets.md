---
title: 'Area: torchtitan/hf_datasets'
type: area
area: 'torchtitan/hf_datasets'
description: 'Hugging Face dataset sources of torchtitan: text and multimodal datasets, chat formatting and sample packing.'
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Area: `torchtitan/hf_datasets`

## Purpose
`torchtitan/hf_datasets/` provides the dataset sources and processors (text, chat, multimodal) that the data pipeline wraps; see [hf-datasets](../concepts/hf-datasets.md). The perf-relevant point is shape: text batches are packed to a fixed token budget, while multimodal batches carry a variable number of image patches and can trigger recompiles on TorchTPU.

## How the units connect
- [hf-datasets](../concepts/hf-datasets.md) sources are consumed by [data-loading](../concepts/data-loading.md), which does packing, collation and checkpointable iteration.

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `torchtitan/hf_datasets`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `torchtitan/hf_datasets` | 6 | 89 | 59 | [`DATASETS`](../catalog/torchtitan/hf_datasets/text_datasets.md#DATASETS.DATASETS "torchtitan/hf_datasets/text_datasets.py:L163"), [`MM_DATASETS`](../catalog/torchtitan/hf_datasets/multimodal/mm_datasets.md#MM_DATASETS.MM_DATASETS "torchtitan/hf_datasets/multimodal/mm_datasets.py:L339"), [`MultiModalProcessor`](../catalog/torchtitan/hf_datasets/multimodal/mm_datasets.md#MultiModalProcessor "torchtitan/hf_datasets/multimodal/mm_datasets.py:L275") | [hf-datasets](../concepts/hf-datasets.md) |

<!-- area:auto:end -->
