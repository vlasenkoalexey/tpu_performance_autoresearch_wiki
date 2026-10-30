---
title: 'Module: torchtitan/components/data/dataset.py'
type: catalog
provenance: extracted
module: torchtitan/components/data/dataset.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.data.dataset`/
symbols:
  SingleDatasetConfig: SingleDatasetConfig#
  SingleDatasetConfig.source: SingleDatasetConfig#source.
  SingleDatasetConfig.processor: SingleDatasetConfig#processor.
  SingleDatasetConfig._build_map_dataset: SingleDatasetConfig#_build_map_dataset().
  SingleDatasetConfig._build_iter_dataset: SingleDatasetConfig#_build_iter_dataset().
  SampleProcessor: SampleProcessor#
  DatasetMixConfig.build: DatasetMixConfig#build().
  DatasetConcatConfig.build: DatasetConcatConfig#build().
  TextSequence.input_ids: TextSequence#input_ids.
  SingleDatasetConfig.build: SingleDatasetConfig#build().
  TextSequence: TextSequence#
  SingleDatasetConfig.post_filters: SingleDatasetConfig#post_filters.
  DatasetConfig.build: DatasetConfig#build().
  DatasetConfig: DatasetConfig#
  TextSequence.positions: TextSequence#positions.
  TextSequence.labels: TextSequence#labels.
  TextSequence.padding_mask: TextSequence#padding_mask.
  TextSequence.__post_init__: TextSequence#__post_init__().
  SampleProcessor.Config: SampleProcessor#Config#
  DatasetMixConfig.datasets: DatasetMixConfig#datasets.
  GrainDataset.GrainDataset: GrainDataset.GrainDataset.
  WeightedDataset.dataset: WeightedDataset#dataset.
  DatasetConcatConfig.datasets: DatasetConcatConfig#datasets.
  WeightedDataset.weight: WeightedDataset#weight.
  SingleDatasetConfig.pre_filters: SingleDatasetConfig#pre_filters.
  WeightedDataset: WeightedDataset#
  DatasetMixConfig: DatasetMixConfig#
  DatasetConcatConfig: DatasetConcatConfig#
  SampleProcessor.__call__: SampleProcessor#__call__().
---
# Module: [`torchtitan/components/data/dataset.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py)

## Classes
### <a id="DatasetConcatConfig"></a>`DatasetConcatConfig`
- def: [`torchtitan/components/data/dataset.py:267`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L267)
- doc: Concatenates finite children before global shuffle and DP sharding.
- signature: `class DatasetConcatConfig:`
- members:
  - <a id="DatasetConcatConfig.build"></a>`build(self, *, context: DatasetBuildContext, dataset_iteration_policy: DatasetIterationPolicy)` — [`L272`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L272) — documented in [data-loading](../../../../concepts/data-loading.md)
  - <a id="DatasetConcatConfig.datasets"></a>`datasets` — [`L270`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L270)
- uses (calls/refs, reference-scoped): [`DatasetBuildContext`](types.md#DatasetBuildContext), [`DatasetIterationPolicy`](types.md#DatasetIterationPolicy), [`build`](dataset.md#DatasetConfig.build), [`DatasetConfig`](dataset.md#DatasetConfig), [`dp_rank`](types.md#DatasetIterationPolicy.dp_rank), [`seed`](types.md#DatasetIterationPolicy.seed), [`dp_world_size`](types.md#DatasetIterationPolicy.dp_world_size), [`shuffle`](types.md#DatasetIterationPolicy.shuffle), [`repeat`](types.md#DatasetIterationPolicy.repeat)

### <a id="DatasetConfig"></a>`DatasetConfig`  ·  implements/extends Protocol
- def: [`torchtitan/components/data/dataset.py:26`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L26) — documented in [data-loading](../../../../concepts/data-loading.md)
- doc: Builds one node of a Grain dataset graph.
- signature: `class DatasetConfig(Protocol):`
- members:
  - <a id="DatasetConfig.build"></a>`build(self, *, context: DatasetBuildContext, dataset_iteration_policy: DatasetIterationPolicy)` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L29)
- uses (calls/refs, reference-scoped): [`DatasetBuildContext`](types.md#DatasetBuildContext), [`DatasetIterationPolicy`](types.md#DatasetIterationPolicy), [`GrainDataset`](dataset.md#GrainDataset.GrainDataset)
- used by: [`dataset`](loader.md#GrainDataLoader.Config.dataset), [`_rank_id`](loader.md#GrainDataLoader._rank_id), [`dataset`](packing.md#ConcatThenSplitPackingConfig.dataset), [`build`](packing.md#FirstFitPackingConfig.build), [`build`](../../hf_datasets/multimodal/mm_datasets.md#MMSamplePackingConfig.build), [`build`](packing.md#ConcatThenSplitPackingConfig.build), [`build`](dataset.md#DatasetConcatConfig.build), [`build`](dataset.md#DatasetMixConfig.build), [`build`](../../models/flux/flux_datasets.md#FluxValidationDatasetConfig.build), [`dataset`](packing.md#FirstFitPackingConfig.dataset), [`dataset`](../../models/flux/flux_datasets.md#FluxValidationDatasetConfig.dataset), [`dataset`](dataset.md#WeightedDataset.dataset), [`dataset`](../../hf_datasets/multimodal/mm_datasets.md#MMSamplePackingConfig.dataset), [`datasets`](dataset.md#DatasetConcatConfig.datasets)

### <a id="DatasetMixConfig"></a>`DatasetMixConfig`
- def: [`torchtitan/components/data/dataset.py:211`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L211)
- doc: Interleave weighted children.
- signature: `class DatasetMixConfig:`
- members:
  - <a id="DatasetMixConfig.build"></a>`build(self, *, context: DatasetBuildContext, dataset_iteration_policy: DatasetIterationPolicy)` — [`L226`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L226) — documented in [data-loading](../../../../concepts/data-loading.md)
  - <a id="DatasetMixConfig.datasets"></a>`datasets` — [`L224`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L224)
- uses (calls/refs, reference-scoped): [`DatasetBuildContext`](types.md#DatasetBuildContext), [`DatasetIterationPolicy`](types.md#DatasetIterationPolicy), [`build`](dataset.md#DatasetConfig.build), [`seed`](types.md#DatasetIterationPolicy.seed), [`read_options`](types.md#DatasetBuildContext.read_options), [`GrainDataset`](dataset.md#GrainDataset.GrainDataset), [`dataset`](dataset.md#WeightedDataset.dataset), [`weight`](dataset.md#WeightedDataset.weight), [`WeightedDataset`](dataset.md#WeightedDataset)

### <a id="SampleProcessor"></a>`SampleProcessor`  ·  implements/extends ABC, Configurable
- def: [`torchtitan/components/data/dataset.py:67`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L67) — documented in [data-loading](../../../../concepts/data-loading.md)
- doc: Configured row processor using Grain-provided deterministic randomness.
- signature: `class SampleProcessor(Configurable, ABC):`
- protocol/private: <a id="SampleProcessor.__call__"></a>`__call__`[`L75`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L75)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`MultiModalProcessor`](../../hf_datasets/multimodal/mm_datasets.md#MultiModalProcessor), [`ChatProcessor`](../../hf_datasets/text_datasets.md#ChatProcessor), [`FluxSampleProcessor`](../../models/flux/flux_datasets.md#FluxSampleProcessor), [`TextProcessor`](../../hf_datasets/text_datasets.md#TextProcessor)
- used by: [`Configurable`](../../config/configurable.md#Configurable), [`processor`](dataset.md#SingleDatasetConfig.processor), [`MultiModalProcessor`](../../hf_datasets/multimodal/mm_datasets.md#MultiModalProcessor), [`Config`](../../hf_datasets/multimodal/mm_datasets.md#MultiModalProcessor.Config), [`Config`](../../models/flux/flux_datasets.md#FluxSampleProcessor.Config), [`ChatProcessor`](../../hf_datasets/text_datasets.md#ChatProcessor), [`FluxSampleProcessor`](../../models/flux/flux_datasets.md#FluxSampleProcessor), [`Config`](../../hf_datasets/text_datasets.md#ChatProcessor.Config), [`Config`](../../hf_datasets/text_datasets.md#TextProcessor.Config), [`TextProcessor`](../../hf_datasets/text_datasets.md#TextProcessor)

### <a id="SampleProcessor.Config"></a>`SampleProcessor.Config`  ·  implements/extends Config
- def: [`torchtitan/components/data/dataset.py:71`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L71)
- signature: `class Config(Configurable.Config):`
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`Config`](../../config/configurable.md#Configurable.Config)
- used by: [`processor`](dataset.md#SingleDatasetConfig.processor), [`Config`](../../hf_datasets/multimodal/mm_datasets.md#MultiModalProcessor.Config), [`Config`](../../models/flux/flux_datasets.md#FluxSampleProcessor.Config), [`Config`](../../hf_datasets/text_datasets.md#ChatProcessor.Config), [`Config`](../../hf_datasets/text_datasets.md#TextProcessor.Config)

### <a id="SingleDatasetConfig"></a>`SingleDatasetConfig`
- def: [`torchtitan/components/data/dataset.py:84`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L84) — documented in [data-loading](../../../../concepts/data-loading.md)
- doc: Build one dataset from a source and row-level transforms.
- signature: `class SingleDatasetConfig:`
- members:
  - <a id="SingleDatasetConfig._build_iter_dataset"></a>`_build_iter_dataset(self, dataset: grain.IterDataset, *, context: DatasetBuildContext, dataset_iteration_policy: DatasetIterationPolicy)` — [`L173`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L173) — Shuffle streaming rows before row processing. — documented in [data-loading](../../../../concepts/data-loading.md)
  - <a id="SingleDatasetConfig._build_map_dataset"></a>`_build_map_dataset(self, dataset: grain.MapDataset, *, context: DatasetBuildContext, dataset_iteration_policy: DatasetIterationPolicy)` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L126) — Process globally indexed rows before shuffle, sharding, and repeat. — documented in [data-loading](../../../../concepts/data-loading.md)
  - <a id="SingleDatasetConfig.build"></a>`build(self, *, context: DatasetBuildContext, dataset_iteration_policy: DatasetIterationPolicy)` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L96) — documented in [data-loading](../../../../concepts/data-loading.md)
  - <a id="SingleDatasetConfig.post_filters"></a>`post_filters` — [`L94`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L94) — documented in [data-loading](../../../../concepts/data-loading.md)
  - <a id="SingleDatasetConfig.pre_filters"></a>`pre_filters` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L92)
  - <a id="SingleDatasetConfig.processor"></a>`processor` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L93) — documented in [data-loading](../../../../concepts/data-loading.md)
  - <a id="SingleDatasetConfig.source"></a>`source` — [`L91`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L91) — documented in [data-loading](../../../../concepts/data-loading.md)
- uses (calls/refs, reference-scoped): [`build`](../../config/configurable.md#Configurable.Config.build), [`DatasetBuildContext`](types.md#DatasetBuildContext), [`SampleProcessor`](dataset.md#SampleProcessor), [`DatasetIterationPolicy`](types.md#DatasetIterationPolicy), [`Config`](dataset.md#SampleProcessor.Config), [`dp_rank`](types.md#DatasetIterationPolicy.dp_rank), [`seed`](types.md#DatasetIterationPolicy.seed), [`dp_world_size`](types.md#DatasetIterationPolicy.dp_world_size), [`shuffle`](types.md#DatasetIterationPolicy.shuffle), [`build`](sources.md#SourceConfig.build), [`RandomAccessDataSource`](sources.md#RandomAccessDataSource), [`GrainDataset`](dataset.md#GrainDataset.GrainDataset), [`repeat`](types.md#DatasetIterationPolicy.repeat), [`SourceConfig`](sources.md#SourceConfig), [`streaming_shuffle_buffer_size`](types.md#DatasetIterationPolicy.streaming_shuffle_buffer_size)
- used by: [`sft_llama3_8b_metamath`](../../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`transformers_modeling_backend_sft_full`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](../../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`DATASETS`](../../hf_datasets/text_datasets.md#DATASETS.DATASETS), [`_kimi_multimodal_dataloader`](../../models/kimi_k2_7/config_registry.md#_kimi_multimodal_dataloader), [`MM_DATASETS`](../../hf_datasets/multimodal/mm_datasets.md#MM_DATASETS.MM_DATASETS), [`_muse_glimmer_mm_dataloader`](../../models/muse_glimmer/config_registry.md#_muse_glimmer_mm_dataloader), [`_kimi_k3_multimodal_dataloader`](../../models/kimi_k3/config_registry.md#_kimi_k3_multimodal_dataloader), [`DATASETS`](../../models/flux/flux_datasets.md#DATASETS.DATASETS), [`__init__`](../../experiments/tpu/datasets.md#TPUGrainDataLoader.__init__), [`_multimodal_collator_config`](../../models/qwen3_5/config_registry.md#_multimodal_collator_config), [`_multimodal_collator_config`](../../models/qwen3_6/config_registry.md#_multimodal_collator_config), [`_multimodal_collator_config`](../../models/qwen3_8/config_registry.md#_multimodal_collator_config), [`_flux_dataset`](../../models/flux/config_registry.md#_flux_dataset), [`_text_dataset`](../../experiments/tpu/datasets.md#_text_dataset)  (4 test-only)

### <a id="TextSequence"></a>`TextSequence`
- def: [`torchtitan/components/data/dataset.py:39`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L39) — documented in [data-loading](../../../../concepts/data-loading.md)
- doc: Next-token-aligned text preserved through composition and packing.
- signature: `class TextSequence:`
- members:
  - <a id="TextSequence.input_ids"></a>`input_ids` — [`L46`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L46) — --- — documented in [data-loading](../../../../concepts/data-loading.md)
  - <a id="TextSequence.labels"></a>`labels` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L48) — ---
  - <a id="TextSequence.padding_mask"></a>`padding_mask` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L52) — ---
  - <a id="TextSequence.positions"></a>`positions` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L50) — ---
- protocol/private: <a id="TextSequence.__post_init__"></a>`__post_init__`[`L55`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L55)
- used by: [`__next__`](packing.md#_DocumentAwareConcatThenSplitIterator.__next__), [`_tokenize_sample`](../../hf_datasets/text_datasets.md#ChatProcessor._tokenize_sample), [`__call__`](collators.md#TextCollator.__call__), [`flat_map`](packing.md#_SplitTextSequenceDocuments.flat_map), [`_packing_output_to_text_sequence`](packing.md#_packing_output_to_text_sequence), [`__call__`](../../hf_datasets/text_datasets.md#TextProcessor.__call__), [`_text_sequence_to_packing_input`](packing.md#_text_sequence_to_packing_input), [`_remainder`](packing.md#_DocumentAwareConcatThenSplitIterator._remainder), [`__call__`](../../hf_datasets/text_datasets.md#ChatProcessor.__call__)

### <a id="WeightedDataset"></a>`WeightedDataset`
- def: [`torchtitan/components/data/dataset.py:203`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L203)
- doc: A dataset and its relative selection weight.
- signature: `class WeightedDataset:`
- members:
  - <a id="WeightedDataset.dataset"></a>`dataset` — [`L206`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L206)
  - <a id="WeightedDataset.weight"></a>`weight` — [`L207`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L207)
- uses (calls/refs, reference-scoped): [`DatasetConfig`](dataset.md#DatasetConfig)
- used by: [`build`](dataset.md#DatasetMixConfig.build), [`datasets`](dataset.md#DatasetMixConfig.datasets)

## Module values
- <a id="GrainDataset.GrainDataset"></a>`GrainDataset` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/dataset.py#L23)

