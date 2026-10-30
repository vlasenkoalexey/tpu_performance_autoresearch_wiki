---
title: 'Module: torchtitan/components/data/types.py'
type: catalog
provenance: extracted
module: torchtitan/components/data/types.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.data.types`/
symbols:
  DatasetBuildContext: DatasetBuildContext#
  DatasetIterationPolicy: DatasetIterationPolicy#
  DatasetBuildContext.num_tokens_per_batch: DatasetBuildContext#num_tokens_per_batch.
  DatasetBuildContext.max_context_length: DatasetBuildContext#max_context_length.
  DatasetBuildContext.tokenizer: DatasetBuildContext#tokenizer.
  DatasetIterationPolicy.seed: DatasetIterationPolicy#seed.
  DatasetIterationPolicy.dp_rank: DatasetIterationPolicy#dp_rank.
  DatasetIterationPolicy.dp_world_size: DatasetIterationPolicy#dp_world_size.
  DatasetBuildContext.read_options: DatasetBuildContext#read_options.
  DatasetIterationPolicy.shuffle: DatasetIterationPolicy#shuffle.
  DatasetBuildContext.max_num_documents: DatasetBuildContext#max_num_documents.
  DatasetIterationPolicy.repeat: DatasetIterationPolicy#repeat.
  DatasetIterationPolicy.streaming_shuffle_buffer_size: DatasetIterationPolicy#streaming_shuffle_buffer_size.
---
# Module: [`torchtitan/components/data/types.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py)

## Classes
### <a id="DatasetBuildContext"></a>`DatasetBuildContext`
- def: [`torchtitan/components/data/types.py:17`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L17) — documented in [data-loading](../../../../concepts/data-loading.md)
- doc: Runtime values shared while building the data pipeline.
- signature: `class DatasetBuildContext:`
- members:
  - <a id="DatasetBuildContext.max_context_length"></a>`max_context_length` — [`L21`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L21)
  - <a id="DatasetBuildContext.max_num_documents"></a>`max_num_documents` — [`L24`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L24)
  - <a id="DatasetBuildContext.num_tokens_per_batch"></a>`num_tokens_per_batch` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L22) — documented in [data-loading](../../../../concepts/data-loading.md)
  - <a id="DatasetBuildContext.read_options"></a>`read_options` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L23)
  - <a id="DatasetBuildContext.tokenizer"></a>`tokenizer` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L20)
- uses (calls/refs, reference-scoped): [`BaseTokenizer`](../tokenizer.md#BaseTokenizer)
- used by: [`_rank_id`](loader.md#GrainDataLoader._rank_id), [`build`](packing.md#FirstFitPackingConfig.build), [`build`](../../hf_datasets/multimodal/mm_datasets.md#MMSamplePackingConfig.build), [`build`](packing.md#ConcatThenSplitPackingConfig.build), [`_build_map_dataset`](dataset.md#SingleDatasetConfig._build_map_dataset), [`_build_iter_dataset`](dataset.md#SingleDatasetConfig._build_iter_dataset), [`build`](dataset.md#DatasetConcatConfig.build), [`build`](dataset.md#DatasetMixConfig.build), [`build`](dataset.md#SingleDatasetConfig.build), [`build`](../../models/flux/flux_datasets.md#FluxValidationDatasetConfig.build), [`build`](dataset.md#DatasetConfig.build), [`__init__`](../../hf_datasets/text_datasets.md#ChatProcessor.__init__), [`__init__`](../../models/flux/flux_datasets.md#FluxSampleProcessor.__init__), [`_num_rows_per_batch`](../../models/flux/flux_datasets.md#FluxCollator._num_rows_per_batch), [`_tokenizer`](../../models/flux/flux_datasets.md#FluxSampleProcessor._tokenizer), [`tokenizer`](../../hf_datasets/multimodal/mm_collator.md#MultiModalCollator.tokenizer), [`_eos_id`](../../hf_datasets/text_datasets.md#ChatProcessor._eos_id), [`_tokenizer`](../../hf_datasets/text_datasets.md#ChatProcessor._tokenizer), [`_num_tokens_per_batch`](collators.md#TextCollator._num_tokens_per_batch), [`__init__`](collators.md#TextCollator.__init__), [`__init__`](../../hf_datasets/multimodal/mm_collator.md#MultiModalCollator.__init__), [`__init__`](../../hf_datasets/multimodal/mm_datasets.md#MultiModalProcessor.__init__), [`__init__`](../../hf_datasets/text_datasets.md#TextProcessor.__init__), [`__init__`](../../models/flux/flux_datasets.md#FluxCollator.__init__), [`_max_context_length`](../../hf_datasets/multimodal/mm_datasets.md#MultiModalProcessor._max_context_length), [`_max_context_length`](../../hf_datasets/text_datasets.md#ChatProcessor._max_context_length), [`_max_context_length`](collators.md#TextCollator._max_context_length), [`_max_context_length`](../../hf_datasets/multimodal/mm_collator.md#MultiModalCollator._max_context_length), [`_num_tokens_per_batch`](../../hf_datasets/multimodal/mm_collator.md#MultiModalCollator._num_tokens_per_batch), [`_tokenizer`](../../hf_datasets/multimodal/mm_datasets.md#MultiModalProcessor._tokenizer), [`_tokenizer`](../../hf_datasets/text_datasets.md#TextProcessor._tokenizer)

### <a id="DatasetIterationPolicy"></a>`DatasetIterationPolicy`
- def: [`torchtitan/components/data/types.py:28`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L28) — documented in [data-loading](../../../../concepts/data-loading.md)
- doc: Controls dataset order, repetition, and data-parallel ownership.
- signature: `class DatasetIterationPolicy:`
- members:
  - <a id="DatasetIterationPolicy.dp_rank"></a>`dp_rank` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L34)
  - <a id="DatasetIterationPolicy.dp_world_size"></a>`dp_world_size` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L35)
  - <a id="DatasetIterationPolicy.repeat"></a>`repeat` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L33)
  - <a id="DatasetIterationPolicy.seed"></a>`seed` — [`L31`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L31)
  - <a id="DatasetIterationPolicy.shuffle"></a>`shuffle` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L32)
  - <a id="DatasetIterationPolicy.streaming_shuffle_buffer_size"></a>`streaming_shuffle_buffer_size` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/types.py#L36)
- used by: [`_rank_id`](loader.md#GrainDataLoader._rank_id), [`build`](packing.md#FirstFitPackingConfig.build), [`build`](../../hf_datasets/multimodal/mm_datasets.md#MMSamplePackingConfig.build), [`build`](packing.md#ConcatThenSplitPackingConfig.build), [`_build_map_dataset`](dataset.md#SingleDatasetConfig._build_map_dataset), [`_build_iter_dataset`](dataset.md#SingleDatasetConfig._build_iter_dataset), [`build`](dataset.md#DatasetConcatConfig.build), [`build`](dataset.md#DatasetMixConfig.build), [`__init__`](sources.md#HuggingFaceRandomAccessSource.__init__), [`__init__`](sources.md#HuggingFaceStreamingSource.__init__), [`build`](dataset.md#SingleDatasetConfig.build), [`build`](../../models/flux/flux_datasets.md#FluxValidationDatasetConfig.build), [`build`](dataset.md#DatasetConfig.build), [`cache_dir`](sources.md#cache_dir), [`_dataset`](sources.md#HuggingFaceStreamingSource._dataset), [`build`](sources.md#SourceConfig.build), [`__init__`](sources.md#IndexedJsonlSource.__init__), [`_repeat`](sources.md#HuggingFaceStreamingSource._repeat), [`_shuffle`](sources.md#HuggingFaceStreamingSource._shuffle)

