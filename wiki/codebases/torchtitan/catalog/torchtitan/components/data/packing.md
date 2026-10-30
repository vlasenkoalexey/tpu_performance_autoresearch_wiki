---
title: 'Module: torchtitan/components/data/packing.py'
type: catalog
provenance: extracted
module: torchtitan/components/data/packing.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.data.packing`/
symbols:
  ConcatThenSplitPackingConfig: ConcatThenSplitPackingConfig#
  ConcatThenSplitPackingConfig.dataset: ConcatThenSplitPackingConfig#dataset.
  FirstFitPackingConfig.build: FirstFitPackingConfig#build().
  _DocumentAwareConcatThenSplitIterator.__next__: _DocumentAwareConcatThenSplitIterator#__next__().
  ConcatThenSplitPackingConfig.build: ConcatThenSplitPackingConfig#build().
  _SplitTextSequenceDocuments.flat_map: _SplitTextSequenceDocuments#flat_map().
  _packing_output_to_text_sequence: _packing_output_to_text_sequence().
  _text_sequence_to_packing_input: _text_sequence_to_packing_input().
  _DocumentAwareConcatThenSplitIterator._remainder_offset: _DocumentAwareConcatThenSplitIterator#_remainder_offset.
  _DocumentAwareConcatThenSplitIterator._remainder: _DocumentAwareConcatThenSplitIterator#_remainder.
  _DocumentAwareConcatThenSplitIterDataset.__iter__: _DocumentAwareConcatThenSplitIterDataset#__iter__().
  _DocumentAwareConcatThenSplitIterator.get_state: _DocumentAwareConcatThenSplitIterator#get_state().
  _DocumentAwareConcatThenSplitIterator.set_state: _DocumentAwareConcatThenSplitIterator#set_state().
  FirstFitPackingConfig: FirstFitPackingConfig#
  FirstFitPackingConfig.dataset: FirstFitPackingConfig#dataset.
  _DocumentAwareConcatThenSplitIterator._remainder_parent_state: _DocumentAwareConcatThenSplitIterator#_remainder_parent_state.
  _DocumentAwareConcatThenSplitIterator._finished: _DocumentAwareConcatThenSplitIterator#_finished.
  _DocumentAwareConcatThenSplitIterator._num_tokens_per_row: _DocumentAwareConcatThenSplitIterator#_num_tokens_per_row.
  FirstFitPackingConfig.__post_init__: FirstFitPackingConfig#__post_init__().
  _DocumentAwareConcatThenSplitIterator._max_context_length: _DocumentAwareConcatThenSplitIterator#_max_context_length.
  FirstFitPackingConfig.num_packing_bins: FirstFitPackingConfig#num_packing_bins.
  _next_document_chunk_end: _next_document_chunk_end().
  _DocumentAwareConcatThenSplitIterDataset._max_num_documents_per_row: _DocumentAwareConcatThenSplitIterDataset#_max_num_documents_per_row.
  _DocumentAwareConcatThenSplitIterDataset._max_context_length: _DocumentAwareConcatThenSplitIterDataset#_max_context_length.
  _DocumentAwareConcatThenSplitIterDataset._num_tokens_per_row: _DocumentAwareConcatThenSplitIterDataset#_num_tokens_per_row.
  _DocumentAwareConcatThenSplitIterator._max_num_documents_per_row: _DocumentAwareConcatThenSplitIterator#_max_num_documents_per_row.
  _SplitTextSequenceDocuments._max_context_length: _SplitTextSequenceDocuments#_max_context_length.
  _packing_output_is_full: _packing_output_is_full().
  _DocumentAwareConcatThenSplitIterDataset: _DocumentAwareConcatThenSplitIterDataset#
  _DocumentAwareConcatThenSplitIterator: _DocumentAwareConcatThenSplitIterator#
  _SplitTextSequenceDocuments: _SplitTextSequenceDocuments#
  _DocumentAwareConcatThenSplitIterDataset.__init__: _DocumentAwareConcatThenSplitIterDataset#__init__().
  _DocumentAwareConcatThenSplitIterator.__init__: _DocumentAwareConcatThenSplitIterator#__init__().
  _SplitTextSequenceDocuments.__init__: _SplitTextSequenceDocuments#__init__().
  _SplitTextSequenceDocuments.max_fan_out: _SplitTextSequenceDocuments#max_fan_out.
---
# Module: [`torchtitan/components/data/packing.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py)

## Classes
### <a id="ConcatThenSplitPackingConfig"></a>`ConcatThenSplitPackingConfig`
- def: [`torchtitan/components/data/packing.py:22`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L22) — documented in [data-loading](../../../../concepts/data-loading.md)
- doc: Concatenates documents, chunking them into fixed-length rows.
- signature: `class ConcatThenSplitPackingConfig:`
- members:
  - <a id="ConcatThenSplitPackingConfig.build"></a>`build(self, *, context: DatasetBuildContext, dataset_iteration_policy: DatasetIterationPolicy)` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L27) — documented in [data-loading](../../../../concepts/data-loading.md)
  - <a id="ConcatThenSplitPackingConfig.dataset"></a>`dataset` — [`L25`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L25)
- uses (calls/refs, reference-scoped): [`DatasetBuildContext`](types.md#DatasetBuildContext), [`DatasetIterationPolicy`](types.md#DatasetIterationPolicy), [`_packing_output_to_text_sequence`](packing.md#_packing_output_to_text_sequence), [`num_tokens_per_batch`](types.md#DatasetBuildContext.num_tokens_per_batch), [`_text_sequence_to_packing_input`](packing.md#_text_sequence_to_packing_input), [`build`](dataset.md#DatasetConfig.build), [`max_context_length`](types.md#DatasetBuildContext.max_context_length), [`DatasetConfig`](dataset.md#DatasetConfig), [`read_options`](types.md#DatasetBuildContext.read_options), [`max_num_documents`](types.md#DatasetBuildContext.max_num_documents), [`_DocumentAwareConcatThenSplitIterDataset`](packing.md#_DocumentAwareConcatThenSplitIterDataset), [`_packing_output_is_full`](packing.md#_packing_output_is_full)
- used by: [`llama3_debugmodel`](../../models/llama3/config_registry.md#llama3_debugmodel), [`llama3_torchft_debugmodel`](../../experiments/torchft/llama3/config_registry.md#llama3_torchft_debugmodel), [`llama3_405b`](../../models/llama3/config_registry.md#llama3_405b), [`deepseek_v4_debugmodel`](../../models/deepseek_v4/config_registry.md#deepseek_v4_debugmodel), [`deepseek_v3_debugmodel`](../../models/deepseek_v3/config_registry.md#deepseek_v3_debugmodel), [`deepseek_v4_flash`](../../models/deepseek_v4/config_registry.md#deepseek_v4_flash), [`deepseek_v4_pro`](../../models/deepseek_v4/config_registry.md#deepseek_v4_pro), [`_gpt_oss_debugmodel`](../../models/gpt_oss/config_registry.md#_gpt_oss_debugmodel), [`deepseek_v4_mtp_debugmodel`](../../models/deepseek_v4/config_registry.md#deepseek_v4_mtp_debugmodel), [`muse_glimmer_debugmodel`](../../models/muse_glimmer/config_registry.md#muse_glimmer_debugmodel), [`transformers_modeling_backend_debugmodel`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel), [`transformers_modeling_backend_debugmodel_moe`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_debugmodel_moe), [`kimi_k2_5`](../../models/kimi_k2_7/config_registry.md#kimi_k2_5), [`llama3_70b`](../../models/llama3/config_registry.md#llama3_70b), [`deepseek_v3_671b`](../../models/deepseek_v3/config_registry.md#deepseek_v3_671b), [`qwen3_debugmodel`](../../models/qwen3/config_registry.md#qwen3_debugmodel), [`deepseek_v3_16b`](../../models/deepseek_v3/config_registry.md#deepseek_v3_16b), [`qwen3_moe_debug`](../../models/qwen3/config_registry.md#qwen3_moe_debug), [`llama3_8b`](../../models/llama3/config_registry.md#llama3_8b), [`qwen3_moe_deepep`](../../models/qwen3/config_registry.md#qwen3_moe_deepep), [`transformers_modeling_backend_full`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_full), [`qwen3_debugmodel_flex_flash`](../../models/qwen3/config_registry.md#qwen3_debugmodel_flex_flash), [`moonlight_16b_a3b`](../../models/kimi_k2_7/config_registry.md#moonlight_16b_a3b), [`qwen3_14b`](../../models/qwen3/config_registry.md#qwen3_14b), [`qwen3_30b_a3b`](../../models/qwen3/config_registry.md#qwen3_30b_a3b), [`muse_glimmer_30b`](../../models/muse_glimmer/config_registry.md#muse_glimmer_30b), [`qwen3_32b`](../../models/qwen3/config_registry.md#qwen3_32b), [`transformers_modeling_backend_full_moe`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_full_moe), [`gpt_oss_120b`](../../models/gpt_oss/config_registry.md#gpt_oss_120b), [`gpt_oss_20b`](../../models/gpt_oss/config_registry.md#gpt_oss_20b), [`qwen38_2_4t_a95b`](../../models/qwen3_8/config_registry.md#qwen38_2_4t_a95b), [`qwen3_0_6b`](../../models/qwen3/config_registry.md#qwen3_0_6b), [`qwen3_1_7b`](../../models/qwen3/config_registry.md#qwen3_1_7b), [`__init__`](../../experiments/tpu/datasets.md#TPUGrainDataLoader.__init__), [`dataloader`](../validate.md#Validator.Config.dataloader), [`graph_trainer_llama3_8b_c4_test`](../../experiments/graph_trainer/llama3/config_registry.md#graph_trainer_llama3_8b_c4_test), [`_c4_test_loader`](../../experiments/tpu/transformers_modeling_backend/config_registry.md#_c4_test_loader)

### <a id="FirstFitPackingConfig"></a>`FirstFitPackingConfig`
- def: [`torchtitan/components/data/packing.py:225`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L225)
- doc: Packs document chunks no longer than the context window.
- signature: `class FirstFitPackingConfig:`
- members:
  - <a id="FirstFitPackingConfig.build"></a>`build(self, *, context: DatasetBuildContext, dataset_iteration_policy: DatasetIterationPolicy)` — [`L236`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L236) — documented in [data-loading](../../../../concepts/data-loading.md)
  - <a id="FirstFitPackingConfig.dataset"></a>`dataset` — [`L228`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L228)
  - <a id="FirstFitPackingConfig.num_packing_bins"></a>`num_packing_bins` — [`L229`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L229) — ---
- protocol/private: <a id="FirstFitPackingConfig.__post_init__"></a>`__post_init__`[`L232`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L232)
- uses (calls/refs, reference-scoped): [`IGNORE_INDEX`](../loss.md#IGNORE_INDEX), [`DatasetBuildContext`](types.md#DatasetBuildContext), [`DatasetIterationPolicy`](types.md#DatasetIterationPolicy), [`_packing_output_to_text_sequence`](packing.md#_packing_output_to_text_sequence), [`num_tokens_per_batch`](types.md#DatasetBuildContext.num_tokens_per_batch), [`_text_sequence_to_packing_input`](packing.md#_text_sequence_to_packing_input), [`build`](dataset.md#DatasetConfig.build), [`max_context_length`](types.md#DatasetBuildContext.max_context_length), [`DatasetConfig`](dataset.md#DatasetConfig), [`seed`](types.md#DatasetIterationPolicy.seed), [`read_options`](types.md#DatasetBuildContext.read_options), [`shuffle`](types.md#DatasetIterationPolicy.shuffle), [`max_num_documents`](types.md#DatasetBuildContext.max_num_documents), [`_SplitTextSequenceDocuments`](packing.md#_SplitTextSequenceDocuments)
- used by: [`sft_llama3_8b_metamath`](../../experiments/tpu/llama3/config_registry.md#sft_llama3_8b_metamath), [`transformers_modeling_backend_sft_full`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_full), [`sft_debugmodel`](../../models/llama3/config_registry.md#sft_debugmodel), [`sft_qwen3_8b_math`](../../models/qwen3/config_registry.md#sft_qwen3_8b_math), [`transformers_modeling_backend_sft_debugmodel`](../../experiments/transformers_modeling_backend/config_registry.md#transformers_modeling_backend_sft_debugmodel)

### <a id="_DocumentAwareConcatThenSplitIterDataset"></a>`_DocumentAwareConcatThenSplitIterDataset`
- def: [`torchtitan/components/data/packing.py:72`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L72)
- protocol/private: <a id="_DocumentAwareConcatThenSplitIterDataset.__init__"></a>`__init__`[`L75`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L75), <a id="_DocumentAwareConcatThenSplitIterDataset.__iter__"></a>`__iter__`[`L88`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L88), <a id="_DocumentAwareConcatThenSplitIterDataset._max_context_length"></a>`_max_context_length`[`L85`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L85), <a id="_DocumentAwareConcatThenSplitIterDataset._max_num_documents_per_row"></a>`_max_num_documents_per_row`[`L84`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L84), <a id="_DocumentAwareConcatThenSplitIterDataset._num_tokens_per_row"></a>`_num_tokens_per_row`[`L86`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L86)
- uses (calls/refs, reference-scoped): [`_DocumentAwareConcatThenSplitIterator`](packing.md#_DocumentAwareConcatThenSplitIterator)
- used by: [`build`](packing.md#ConcatThenSplitPackingConfig.build)

### <a id="_DocumentAwareConcatThenSplitIterator"></a>`_DocumentAwareConcatThenSplitIterator`
- def: [`torchtitan/components/data/packing.py:97`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L97)
- members:
  - <a id="_DocumentAwareConcatThenSplitIterator.get_state"></a>`get_state(self)` — [`L199`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L199)
  - <a id="_DocumentAwareConcatThenSplitIterator.set_state"></a>`set_state(self, state: dict[str, Any])` — [`L212`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L212)
- protocol/private: <a id="_DocumentAwareConcatThenSplitIterator.__init__"></a>`__init__`[`L100`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L100), <a id="_DocumentAwareConcatThenSplitIterator.__next__"></a>`__next__`[`L117`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L117), <a id="_DocumentAwareConcatThenSplitIterator._finished"></a>`_finished`[`L115`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L115), <a id="_DocumentAwareConcatThenSplitIterator._max_context_length"></a>`_max_context_length`[`L110`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L110), <a id="_DocumentAwareConcatThenSplitIterator._max_num_documents_per_row"></a>`_max_num_documents_per_row`[`L109`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L109), <a id="_DocumentAwareConcatThenSplitIterator._num_tokens_per_row"></a>`_num_tokens_per_row`[`L111`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L111), <a id="_DocumentAwareConcatThenSplitIterator._remainder"></a>`_remainder`[`L112`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L112), <a id="_DocumentAwareConcatThenSplitIterator._remainder_offset"></a>`_remainder_offset`[`L114`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L114), <a id="_DocumentAwareConcatThenSplitIterator._remainder_parent_state"></a>`_remainder_parent_state`[`L113`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L113)
- uses (calls/refs, reference-scoped): [`IGNORE_INDEX`](../loss.md#IGNORE_INDEX), [`input_ids`](dataset.md#TextSequence.input_ids), [`TextSequence`](dataset.md#TextSequence), [`positions`](dataset.md#TextSequence.positions), [`labels`](dataset.md#TextSequence.labels), [`padding_mask`](dataset.md#TextSequence.padding_mask), [`_next_document_chunk_end`](packing.md#_next_document_chunk_end)
- used by: [`__iter__`](packing.md#_DocumentAwareConcatThenSplitIterDataset.__iter__)

### <a id="_SplitTextSequenceDocuments"></a>`_SplitTextSequenceDocuments`
- def: [`torchtitan/components/data/packing.py:294`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L294)
- members:
  - <a id="_SplitTextSequenceDocuments.flat_map"></a>`flat_map(self, element: TextSequence)` — [`L305`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L305) — documented in [data-loading](../../../../concepts/data-loading.md)
  - <a id="_SplitTextSequenceDocuments.max_fan_out"></a>`max_fan_out` — [`L303`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L303)
- protocol/private: <a id="_SplitTextSequenceDocuments.__init__"></a>`__init__`[`L297`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L297), <a id="_SplitTextSequenceDocuments._max_context_length"></a>`_max_context_length`[`L302`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L302)
- uses (calls/refs, reference-scoped): [`input_ids`](dataset.md#TextSequence.input_ids), [`TextSequence`](dataset.md#TextSequence), [`positions`](dataset.md#TextSequence.positions), [`labels`](dataset.md#TextSequence.labels), [`padding_mask`](dataset.md#TextSequence.padding_mask), [`_next_document_chunk_end`](packing.md#_next_document_chunk_end)
- used by: [`build`](packing.md#FirstFitPackingConfig.build)

## Functions
- <a id="_next_document_chunk_end"></a>`_next_document_chunk_end(*, num_tokens: int, positions: np.ndarray | None, start: int, max_context_length: int)` — [`L335`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L335) — Return the next document boundary or context-sized chunk boundary.
- <a id="_packing_output_is_full"></a>`_packing_output_is_full(packing_output: dict[str, np.ndarray])` — [`L351`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L351) — Return whether concat-then-split filled the entire token batch.
- <a id="_packing_output_to_text_sequence"></a>`_packing_output_to_text_sequence(packing_output: dict[str, np.ndarray], *, max_context_length: int)` — [`L381`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L381) — Finalize packed text by masking padding and canonicalizing positions. — documented in [data-loading](../../../../concepts/data-loading.md)
- <a id="_text_sequence_to_packing_input"></a>`_text_sequence_to_packing_input(text_sequence: TextSequence, *, max_context_length: int)` — [`L356`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/packing.py#L356) — Convert a `TextSequence` to the array dictionary expected by text packing.

