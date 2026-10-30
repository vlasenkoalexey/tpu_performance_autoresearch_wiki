---
title: 'Module: torchtitan/components/data/collators.py'
type: catalog
provenance: extracted
module: torchtitan/components/data/collators.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.data.collators`/
symbols:
  TextCollator.__call__: TextCollator#__call__().
  Collator: Collator#
  TrainerBatch.TrainerBatch: TrainerBatch.TrainerBatch.
  HAS_PIN_MEMORY: HAS_PIN_MEMORY.
  Collator.Config: Collator#Config#
  TextCollator.Config: TextCollator#Config#
  TextCollator: TextCollator#
  TextCollator._num_tokens_per_batch: TextCollator#_num_tokens_per_batch.
  TextCollator.__init__: TextCollator#__init__().
  TextCollator._max_context_length: TextCollator#_max_context_length.
  Collator.__call__: Collator#__call__().
  Collator.num_rows_per_batch: Collator#num_rows_per_batch().
---
# Module: [`torchtitan/components/data/collators.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py)

## Classes
### <a id="Collator"></a>`Collator`  ·  implements/extends ABC, Configurable
- def: [`torchtitan/components/data/collators.py:36`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py#L36) — documented in [data-loading](../../../../concepts/data-loading.md)
- doc: Configured row-to-batch conversion.
- signature: `class Collator(Configurable, ABC):`
- members:
  - <a id="Collator.num_rows_per_batch"></a>`num_rows_per_batch(self)` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py#L47) — Return the number of dataset rows consumed by one trainer batch.
- protocol/private: <a id="Collator.__call__"></a>`__call__`[`L44`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py#L44)
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`MultiModalCollator`](../../hf_datasets/multimodal/mm_collator.md#MultiModalCollator), [`TrainerBatch`](collators.md#TrainerBatch.TrainerBatch), [`FluxCollator`](../../models/flux/flux_datasets.md#FluxCollator), [`TextCollator`](collators.md#TextCollator), [`num_rows_per_batch`](../../models/flux/flux_datasets.md#FluxCollator.num_rows_per_batch)
- used by: [`Configurable`](../../config/configurable.md#Configurable), [`collator`](loader.md#GrainDataLoader.Config.collator), [`MultiModalCollator`](../../hf_datasets/multimodal/mm_collator.md#MultiModalCollator), [`Config`](../../hf_datasets/multimodal/mm_collator.md#MultiModalCollator.Config), [`Config`](../../models/flux/flux_datasets.md#FluxCollator.Config), [`FluxCollator`](../../models/flux/flux_datasets.md#FluxCollator), [`Config`](collators.md#TextCollator.Config), [`TextCollator`](collators.md#TextCollator)

### <a id="Collator.Config"></a>`Collator.Config`  ·  implements/extends Config
- def: [`torchtitan/components/data/collators.py:40`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py#L40)
- signature: `class Config(Configurable.Config):`
- uses (calls/refs, reference-scoped): [`Configurable`](../../config/configurable.md#Configurable), [`Config`](../../config/configurable.md#Configurable.Config)
- used by: [`collator`](loader.md#GrainDataLoader.Config.collator), [`Config`](../../hf_datasets/multimodal/mm_collator.md#MultiModalCollator.Config), [`Config`](../../models/flux/flux_datasets.md#FluxCollator.Config), [`Config`](collators.md#TextCollator.Config)

### <a id="TextCollator"></a>`TextCollator`  ·  implements/extends Collator
- def: [`torchtitan/components/data/collators.py:52`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py#L52) — documented in [data-loading](../../../../concepts/data-loading.md)
- doc: Packs text rows into one page-locked, pre-padded token batch.
- signature: `class TextCollator(Collator):`
- protocol/private: <a id="TextCollator.__call__"></a>`__call__`[`L64`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py#L64), <a id="TextCollator.__init__"></a>`__init__`[`L59`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py#L59), <a id="TextCollator._max_context_length"></a>`_max_context_length`[`L62`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py#L62), <a id="TextCollator._num_tokens_per_batch"></a>`_num_tokens_per_batch`[`L61`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py#L61)
- uses (calls/refs, reference-scoped): [`IGNORE_INDEX`](../loss.md#IGNORE_INDEX), [`DatasetBuildContext`](types.md#DatasetBuildContext), [`Collator`](collators.md#Collator), [`input_ids`](dataset.md#TextSequence.input_ids), [`TextSequence`](dataset.md#TextSequence), [`TrainerBatch`](collators.md#TrainerBatch.TrainerBatch), [`num_tokens_per_batch`](types.md#DatasetBuildContext.num_tokens_per_batch), [`max_context_length`](types.md#DatasetBuildContext.max_context_length), [`positions`](dataset.md#TextSequence.positions), [`HAS_PIN_MEMORY`](collators.md#HAS_PIN_MEMORY), [`labels`](dataset.md#TextSequence.labels), [`padding_mask`](dataset.md#TextSequence.padding_mask), [`Config`](collators.md#TextCollator.Config)
- used by: [`collator`](loader.md#GrainDataLoader.Config.collator), [`Collator`](collators.md#Collator)

### <a id="TextCollator.Config"></a>`TextCollator.Config`  ·  implements/extends Config
- def: [`torchtitan/components/data/collators.py:56`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py#L56) — documented in [data-loading](../../../../concepts/data-loading.md)
- signature: `class Config(Collator.Config):`
- uses (calls/refs, reference-scoped): [`Collator`](collators.md#Collator), [`Config`](collators.md#Collator.Config)
- used by: [`collator`](loader.md#GrainDataLoader.Config.collator), [`__init__`](collators.md#TextCollator.__init__)

## Module values
- <a id="HAS_PIN_MEMORY"></a>`HAS_PIN_MEMORY` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py#L33)
- <a id="TrainerBatch.TrainerBatch"></a>`TrainerBatch` — [`L27`](../../../../../../../raw/code/torchtitan/torchtitan/components/data/collators.py#L27) — documented in [data-loading](../../../../concepts/data-loading.md)

