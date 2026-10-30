---
title: 'Module: torchtitan/components/data/sources.py'
type: catalog
provenance: extracted
module: torchtitan/components/data/sources.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.data.sources`/
symbols:
  HuggingFaceRandomAccessSource.__init__: HuggingFaceRandomAccessSource#__init__().
  HuggingFaceStreamingSource.__init__: HuggingFaceStreamingSource#__init__().
  HuggingFaceStreamingSource: HuggingFaceStreamingSource#
  HuggingFaceStreamingSource.Config: HuggingFaceStreamingSource#Config#
  _HuggingFaceCursorIterator.__next__: _HuggingFaceCursorIterator#__next__().
  HuggingFaceRandomAccessSource: HuggingFaceRandomAccessSource#
  HuggingFaceRandomAccessSource.Config: HuggingFaceRandomAccessSource#Config#
  HuggingFaceStreamingSource.Config.path: HuggingFaceStreamingSource#Config#path.
  HuggingFaceStreamingSource.Config.split: HuggingFaceStreamingSource#Config#split.
  IndexedJsonlSource._byte_offsets: IndexedJsonlSource#_byte_offsets.
  HuggingFaceStreamingSource.__iter__: HuggingFaceStreamingSource#__iter__().
  _HuggingFaceCursorIterator.set_state: _HuggingFaceCursorIterator#set_state().
  IndexedJsonlSource.__getitem__: IndexedJsonlSource#__getitem__().
  cache_dir: cache_dir.
  IndexedJsonlSource._paths: IndexedJsonlSource#_paths.
  HuggingFaceRandomAccessSource.Config.path: HuggingFaceRandomAccessSource#Config#path.
  HuggingFaceRandomAccessSource.Config.split: HuggingFaceRandomAccessSource#Config#split.
  _HuggingFaceCursorIterator._dataset: _HuggingFaceCursorIterator#_dataset.
  SourceConfig.build: SourceConfig#build().
  IndexedJsonlSource.Config: IndexedJsonlSource#Config#
  HuggingFaceRandomAccessSource.Config.load_dataset_kwargs: HuggingFaceRandomAccessSource#Config#load_dataset_kwargs.
  HuggingFaceStreamingSource.Config.load_dataset_kwargs: HuggingFaceStreamingSource#Config#load_dataset_kwargs.
  HuggingFaceStreamingSource._dataset: HuggingFaceStreamingSource#_dataset.
  IndexedJsonlSource.__init__: IndexedJsonlSource#__init__().
  _HuggingFaceCursorIterator._epoch: _HuggingFaceCursorIterator#_epoch.
  _HuggingFaceCursorIterator.get_state: _HuggingFaceCursorIterator#get_state().
  RandomAccessDataSource: RandomAccessDataSource#
  _HuggingFaceCursorIterator._iterator: _HuggingFaceCursorIterator#_iterator.
  IndexedJsonlSource: IndexedJsonlSource#
  HuggingFaceStreamingSource._repeat: HuggingFaceStreamingSource#_repeat.
  HuggingFaceStreamingSource._shuffle: HuggingFaceStreamingSource#_shuffle.
  SourceConfig: SourceConfig#
  HuggingFaceStreamingSource.Config.name: HuggingFaceStreamingSource#Config#name.
  IndexedJsonlSource.__len__: IndexedJsonlSource#__len__().
  HuggingFaceRandomAccessSource.Config.__post_init__: HuggingFaceRandomAccessSource#Config#__post_init__().
  HuggingFaceRandomAccessSource.__len__: HuggingFaceRandomAccessSource#__len__().
  HuggingFaceRandomAccessSource.__getitem__: HuggingFaceRandomAccessSource#__getitem__().
  HuggingFaceStreamingSource.Config.__post_init__: HuggingFaceStreamingSource#Config#__post_init__().
  IndexedJsonlSource._path_ids: IndexedJsonlSource#_path_ids.
  HuggingFaceRandomAccessSource.Config.name: HuggingFaceRandomAccessSource#Config#name.
  HuggingFaceRandomAccessSource._dataset: HuggingFaceRandomAccessSource#_dataset.
  _HuggingFaceCursorIterator._shuffle: _HuggingFaceCursorIterator#_shuffle.
  IndexedJsonlSource.Config.patterns: IndexedJsonlSource#Config#patterns.
  HuggingFaceRandomAccessSource.Config.revision: HuggingFaceRandomAccessSource#Config#revision.
  HuggingFaceStreamingSource.Config.revision: HuggingFaceStreamingSource#Config#revision.
  _file_patterns_to_paths: _file_patterns_to_paths().
  _HuggingFaceCursorIterator._repeat: _HuggingFaceCursorIterator#_repeat.
  _HuggingFaceCursorIterator._initial_state: _HuggingFaceCursorIterator#_initial_state.
  _HuggingFaceCursorIterator: _HuggingFaceCursorIterator#
  RandomAccessDataSource.__len__: RandomAccessDataSource#__len__().
  RandomAccessDataSource.__getitem__: RandomAccessDataSource#__getitem__().
  _HuggingFaceCursorIterator.__init__: _HuggingFaceCursorIterator#__init__().
---
# Module: [`torchtitan/components/data/sources.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py)

## Classes
### <a id="HuggingFaceRandomAccessSource"></a>`HuggingFaceRandomAccessSource`  ·  implements/extends Configurable
- def: [`torchtitan/components/data/sources.py:94`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L94) — documented in [data-loading](../../../../concepts/data-loading.md)
- doc: Provides random access to a materialized Hugging Face dataset.
- signature: `class HuggingFaceRandomAccessSource(Configurable):`
- protocol/private: <a id="HuggingFaceRandomAccessSource.__getitem__"></a>`__getitem__`[`L141`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L141), <a id="HuggingFaceRandomAccessSource.__init__"></a>`__init__`[`L115`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L115), <a id="HuggingFaceRandomAccessSource.__len__"></a>`__len__`[`L138`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L138), <a id="HuggingFaceRandomAccessSource._dataset"></a>`_dataset`[`L136`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L136)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`DatasetIterationPolicy`](types.md#DatasetIterationPolicy), [`Config`](sources.md#HuggingFaceRandomAccessSource.Config), [`cache_dir`](sources.md#cache_dir), [`path`](sources.md#HuggingFaceRandomAccessSource.Config.path), [`split`](sources.md#HuggingFaceRandomAccessSource.Config.split), [`load_dataset_kwargs`](sources.md#HuggingFaceRandomAccessSource.Config.load_dataset_kwargs), [`name`](sources.md#HuggingFaceRandomAccessSource.Config.name), [`revision`](sources.md#HuggingFaceRandomAccessSource.Config.revision)
- used by: [`Configurable`](../../config/configurable.md#Configurable), [`sft_llama3_8b_metamath`](../../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`transformers_modeling_backend_sft_full`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](../../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`DATASETS`](../../hf_datasets/text_datasets.md#DATASETS.DATASETS)

### <a id="HuggingFaceRandomAccessSource.Config"></a>`HuggingFaceRandomAccessSource.Config`  ·  implements/extends Config
- def: [`torchtitan/components/data/sources.py:98`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L98)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="HuggingFaceRandomAccessSource.Config.load_dataset_kwargs"></a>`load_dataset_kwargs` — [`L103`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L103)
  - <a id="HuggingFaceRandomAccessSource.Config.name"></a>`name` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L101)
  - <a id="HuggingFaceRandomAccessSource.Config.path"></a>`path` — [`L99`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L99)
  - <a id="HuggingFaceRandomAccessSource.Config.revision"></a>`revision` — [`L102`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L102)
  - <a id="HuggingFaceRandomAccessSource.Config.split"></a>`split` — [`L100`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L100)
- protocol/private: <a id="HuggingFaceRandomAccessSource.Config.__post_init__"></a>`__post_init__`[`L105`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L105)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`Config`](../../config/configurable.md#Configurable.Config)
- used by: [`sft_llama3_8b_metamath`](../../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`transformers_modeling_backend_sft_full`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](../../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel), [`DATASETS`](../../hf_datasets/text_datasets.md#DATASETS.DATASETS), [`__init__`](sources.md#HuggingFaceRandomAccessSource.__init__)

### <a id="HuggingFaceStreamingSource"></a>`HuggingFaceStreamingSource`  ·  implements/extends Configurable
- def: [`torchtitan/components/data/sources.py:145`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L145) — documented in [data-loading](../../../../concepts/data-loading.md)
- doc: Provides a DP-sharded Hugging Face stream with cursor checkpointing.
- signature: `class HuggingFaceStreamingSource(Configurable, grain.IterDataset):`
- protocol/private: <a id="HuggingFaceStreamingSource.__init__"></a>`__init__`[`L166`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L166), <a id="HuggingFaceStreamingSource.__iter__"></a>`__iter__`[`L201`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L201), <a id="HuggingFaceStreamingSource._dataset"></a>`_dataset`[`L193`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L193), <a id="HuggingFaceStreamingSource._repeat"></a>`_repeat`[`L198`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L198), <a id="HuggingFaceStreamingSource._shuffle"></a>`_shuffle`[`L199`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L199)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`DatasetIterationPolicy`](types.md#DatasetIterationPolicy), [`Config`](sources.md#HuggingFaceStreamingSource.Config), [`path`](sources.md#HuggingFaceStreamingSource.Config.path), [`split`](sources.md#HuggingFaceStreamingSource.Config.split), [`dp_rank`](types.md#DatasetIterationPolicy.dp_rank), [`dp_world_size`](types.md#DatasetIterationPolicy.dp_world_size), [`cache_dir`](sources.md#cache_dir), [`shuffle`](types.md#DatasetIterationPolicy.shuffle), [`load_dataset_kwargs`](sources.md#HuggingFaceStreamingSource.Config.load_dataset_kwargs), [`repeat`](types.md#DatasetIterationPolicy.repeat), [`name`](sources.md#HuggingFaceStreamingSource.Config.name), [`_HuggingFaceCursorIterator`](sources.md#_HuggingFaceCursorIterator), [`revision`](sources.md#HuggingFaceStreamingSource.Config.revision)
- used by: [`Configurable`](../../config/configurable.md#Configurable), [`DATASETS`](../../hf_datasets/text_datasets.md#DATASETS.DATASETS), [`MM_DATASETS`](../../hf_datasets/multimodal/mm_datasets.md#MM_DATASETS.MM_DATASETS), [`DATASETS`](../../models/flux/flux_datasets.md#DATASETS.DATASETS)

### <a id="HuggingFaceStreamingSource.Config"></a>`HuggingFaceStreamingSource.Config`  ·  implements/extends Config
- def: [`torchtitan/components/data/sources.py:149`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L149)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="HuggingFaceStreamingSource.Config.load_dataset_kwargs"></a>`load_dataset_kwargs` — [`L154`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L154)
  - <a id="HuggingFaceStreamingSource.Config.name"></a>`name` — [`L152`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L152)
  - <a id="HuggingFaceStreamingSource.Config.path"></a>`path` — [`L150`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L150)
  - <a id="HuggingFaceStreamingSource.Config.revision"></a>`revision` — [`L153`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L153)
  - <a id="HuggingFaceStreamingSource.Config.split"></a>`split` — [`L151`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L151)
- protocol/private: <a id="HuggingFaceStreamingSource.Config.__post_init__"></a>`__post_init__`[`L156`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L156)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`Config`](../../config/configurable.md#Configurable.Config)
- used by: [`DATASETS`](../../hf_datasets/text_datasets.md#DATASETS.DATASETS), [`MM_DATASETS`](../../hf_datasets/multimodal/mm_datasets.md#MM_DATASETS.MM_DATASETS), [`DATASETS`](../../models/flux/flux_datasets.md#DATASETS.DATASETS), [`__init__`](sources.md#HuggingFaceStreamingSource.__init__)

### <a id="IndexedJsonlSource"></a>`IndexedJsonlSource`  ·  implements/extends Configurable
- def: [`torchtitan/components/data/sources.py:50`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L50)
- doc: Provides random access to JSONL rows through compact byte offsets.
- signature: `class IndexedJsonlSource(Configurable):`
- protocol/private: <a id="IndexedJsonlSource.__getitem__"></a>`__getitem__`[`L83`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L83), <a id="IndexedJsonlSource.__init__"></a>`__init__`[`L57`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L57), <a id="IndexedJsonlSource.__len__"></a>`__len__`[`L80`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L80), <a id="IndexedJsonlSource._byte_offsets"></a>`_byte_offsets`[`L66`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L66), <a id="IndexedJsonlSource._path_ids"></a>`_path_ids`[`L65`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L65), <a id="IndexedJsonlSource._paths"></a>`_paths`[`L64`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L64)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`DatasetIterationPolicy`](types.md#DatasetIterationPolicy), [`Config`](sources.md#IndexedJsonlSource.Config), [`_file_patterns_to_paths`](sources.md#_file_patterns_to_paths), [`patterns`](sources.md#IndexedJsonlSource.Config.patterns)
- used by: [`Configurable`](../../config/configurable.md#Configurable)

### <a id="IndexedJsonlSource.Config"></a>`IndexedJsonlSource.Config`  ·  implements/extends Config
- def: [`torchtitan/components/data/sources.py:54`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L54)
- signature: `class Config(Configurable.Config):`
- members:
  - <a id="IndexedJsonlSource.Config.patterns"></a>`patterns` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L55)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`Config`](../../config/configurable.md#Configurable.Config)
- used by: [`_paths`](sources.md#IndexedJsonlSource._paths), [`__init__`](sources.md#IndexedJsonlSource.__init__)

### <a id="RandomAccessDataSource"></a>`RandomAccessDataSource`  ·  implements/extends Protocol
- def: [`torchtitan/components/data/sources.py:29`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L29)
- doc: Finite data source addressable by integer index.
- signature: `class RandomAccessDataSource(Protocol):`
- protocol/private: <a id="RandomAccessDataSource.__getitem__"></a>`__getitem__`[`L35`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L35), <a id="RandomAccessDataSource.__len__"></a>`__len__`[`L32`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L32)
- used by: [`build`](dataset.md#SingleDatasetConfig.build), [`build`](sources.md#SourceConfig.build)

### <a id="SourceConfig"></a>`SourceConfig`  ·  implements/extends Protocol
- def: [`torchtitan/components/data/sources.py:39`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L39)
- doc: Builds a random-access or streaming source.
- signature: `class SourceConfig(Protocol):`
- members:
  - <a id="SourceConfig.build"></a>`build(self, *, dataset_iteration_policy: DatasetIterationPolicy)` — [`L42`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L42)
- uses (calls/refs, reference-scoped): [`DatasetIterationPolicy`](types.md#DatasetIterationPolicy), [`RandomAccessDataSource`](sources.md#RandomAccessDataSource)
- used by: [`source`](dataset.md#SingleDatasetConfig.source), [`build`](dataset.md#SingleDatasetConfig.build)

### <a id="_HuggingFaceCursorIterator"></a>`_HuggingFaceCursorIterator`
- def: [`torchtitan/components/data/sources.py:226`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L226)
- members:
  - <a id="_HuggingFaceCursorIterator.get_state"></a>`get_state(self)` — [`L257`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L257)
  - <a id="_HuggingFaceCursorIterator.set_state"></a>`set_state(self, state: dict[str, Any])` — [`L263`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L263)
- protocol/private: <a id="_HuggingFaceCursorIterator.__init__"></a>`__init__`[`L229`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L229), <a id="_HuggingFaceCursorIterator.__next__"></a>`__next__`[`L244`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L244), <a id="_HuggingFaceCursorIterator._dataset"></a>`_dataset`[`L237`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L237), <a id="_HuggingFaceCursorIterator._epoch"></a>`_epoch`[`L240`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L240), <a id="_HuggingFaceCursorIterator._initial_state"></a>`_initial_state`[`L241`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L241), <a id="_HuggingFaceCursorIterator._iterator"></a>`_iterator`[`L242`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L242), <a id="_HuggingFaceCursorIterator._repeat"></a>`_repeat`[`L238`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L238), <a id="_HuggingFaceCursorIterator._shuffle"></a>`_shuffle`[`L239`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L239)
- used by: [`__iter__`](sources.md#HuggingFaceStreamingSource.__iter__)

## Functions
- <a id="_file_patterns_to_paths"></a>`_file_patterns_to_paths(patterns: tuple[str, ...])` — [`L209`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L209) — Return sorted, unique absolute paths matched by file patterns.

## Module values
- <a id="cache_dir"></a>`cache_dir` — [`L20`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/sources.py#L20)

