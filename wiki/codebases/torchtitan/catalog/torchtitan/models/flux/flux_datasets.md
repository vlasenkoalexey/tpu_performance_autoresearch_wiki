---
title: 'Module: torchtitan/models/flux/flux_datasets.py'
type: catalog
provenance: extracted
module: torchtitan/models/flux/flux_datasets.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.flux.flux_datasets`/
symbols:
  DATASETS.DATASETS: DATASETS.DATASETS.
  FluxSampleProcessor.__call__: FluxSampleProcessor#__call__().
  FluxValidationDatasetConfig.build: FluxValidationDatasetConfig#build().
  FluxSampleProcessor.Config: FluxSampleProcessor#Config#
  FluxCollator.Config: FluxCollator#Config#
  _cc12m_wds_data_processor: _cc12m_wds_data_processor().
  FluxSampleProcessor: FluxSampleProcessor#
  FluxSampleProcessor.__init__: FluxSampleProcessor#__init__().
  FluxSampleProcessor._tokenizer: FluxSampleProcessor#_tokenizer.
  FluxCollator: FluxCollator#
  FluxCollator._num_rows_per_batch: FluxCollator#_num_rows_per_batch.
  _coco_data_processor: _coco_data_processor().
  FluxValidationDatasetConfig.dataset: FluxValidationDatasetConfig#dataset.
  FluxSampleProcessor.Config.prompt_dropout_prob: FluxSampleProcessor#Config#prompt_dropout_prob.
  FluxValidationDatasetConfig: FluxValidationDatasetConfig#
  FluxSampleProcessor.Config.data_processor: FluxSampleProcessor#Config#data_processor.
  _add_validation_timestep: _add_validation_timestep().
  FluxCollator.__init__: FluxCollator#__init__().
  FluxCollator.__call__: FluxCollator#__call__().
  _is_not_none: _is_not_none().
  FluxSample: FluxSample#
  FluxSampleProcessor._data_processor: FluxSampleProcessor#_data_processor.
  FluxSampleProcessor.prompt_dropout_prob: FluxSampleProcessor#prompt_dropout_prob.
  FluxSampleProcessor.img_size: FluxSampleProcessor#img_size.
  FluxSampleProcessor.Config.__post_init__: FluxSampleProcessor#Config#__post_init__().
  FluxCollator.num_rows_per_batch: FluxCollator#num_rows_per_batch().
  _process_cc12m_image: _process_cc12m_image().
  FluxSampleProcessor.Config.img_size: FluxSampleProcessor#Config#img_size.
  _VALIDATION_TIMESTEPS: _VALIDATION_TIMESTEPS.
  FluxSampleProcessor._t5_empty_token: FluxSampleProcessor#_t5_empty_token.
  FluxSampleProcessor._clip_empty_token: FluxSampleProcessor#_clip_empty_token.
  FluxSample.t5: FluxSample#t5.
  FluxSample.clip: FluxSample#clip.
  FluxSample.prompt: FluxSample#prompt.
  FluxSample.image: FluxSample#image.
  FluxSample.timestep: FluxSample#timestep.
---
# Module: [`torchtitan/models/flux/flux_datasets.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py)

## Classes
### <a id="FluxCollator"></a>`FluxCollator`  ·  implements/extends Collator
- def: [`torchtitan/models/flux/flux_datasets.py:198`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L198)
- doc: Stacks Flux samples and moves images to the trainer label slot.
- signature: `class FluxCollator(Collator):`
- members:
  - <a id="FluxCollator.num_rows_per_batch"></a>`num_rows_per_batch(self)` — [`L216`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L216)
- protocol/private: <a id="FluxCollator.__call__"></a>`__call__`[`L219`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L219), <a id="FluxCollator.__init__"></a>`__init__`[`L205`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L205), <a id="FluxCollator._num_rows_per_batch"></a>`_num_rows_per_batch`[`L207`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L207)
- uses (calls/refs, reference-scoped): [`DatasetBuildContext`](../../components/data/types.md#DatasetBuildContext), [`Collator`](../../components/data/collators.md#Collator), [`TrainerBatch`](../../components/data/collators.md#TrainerBatch.TrainerBatch), [`num_tokens_per_batch`](../../components/data/types.md#DatasetBuildContext.num_tokens_per_batch), [`max_context_length`](../../components/data/types.md#DatasetBuildContext.max_context_length), [`Config`](flux_datasets.md#FluxCollator.Config), [`FluxSample`](flux_datasets.md#FluxSample)
- used by: [`flux_debugmodel`](config_registry.md#flux_debugmodel), [`flux_dev`](config_registry.md#flux_dev), [`flux_schnell`](config_registry.md#flux_schnell), [`Collator`](../../components/data/collators.md#Collator), [`num_rows_per_batch`](../../components/data/collators.md#Collator.num_rows_per_batch)

### <a id="FluxCollator.Config"></a>`FluxCollator.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/flux_datasets.py:202`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L202)
- signature: `class Config(Collator.Config):`
- uses (calls/refs, reference-scoped): [`Collator`](../../components/data/collators.md#Collator), [`Config`](../../components/data/collators.md#Collator.Config)
- used by: [`flux_debugmodel`](config_registry.md#flux_debugmodel), [`flux_dev`](config_registry.md#flux_dev), [`flux_schnell`](config_registry.md#flux_schnell), [`__init__`](flux_datasets.md#FluxCollator.__init__)

### <a id="FluxSample"></a>`FluxSample`  ·  implements/extends _TypedDict
- def: [`torchtitan/models/flux/flux_datasets.py:31`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L31)
- signature: `class FluxSample(TypedDict):`
- members:
  - <a id="FluxSample.clip"></a>`clip` — [`L33`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L33)
  - <a id="FluxSample.image"></a>`image` — [`L35`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L35)
  - <a id="FluxSample.prompt"></a>`prompt` — [`L34`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L34)
  - <a id="FluxSample.t5"></a>`t5` — [`L32`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L32)
  - <a id="FluxSample.timestep"></a>`timestep` — [`L36`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L36)
- used by: [`__call__`](flux_datasets.md#FluxSampleProcessor.__call__), [`_add_validation_timestep`](flux_datasets.md#_add_validation_timestep), [`__call__`](flux_datasets.md#FluxCollator.__call__)

### <a id="FluxSampleProcessor"></a>`FluxSampleProcessor`  ·  implements/extends SampleProcessor
- def: [`torchtitan/models/flux/flux_datasets.py:136`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L136)
- doc: Applies an existing Flux processor and classifier-free prompt dropout.
- signature: `class FluxSampleProcessor(SampleProcessor):`
- members:
  - <a id="FluxSampleProcessor.img_size"></a>`img_size` — [`L164`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L164)
  - <a id="FluxSampleProcessor.prompt_dropout_prob"></a>`prompt_dropout_prob` — [`L163`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L163)
- protocol/private: <a id="FluxSampleProcessor.__call__"></a>`__call__`[`L166`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L166), <a id="FluxSampleProcessor.__init__"></a>`__init__`[`L152`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L152), <a id="FluxSampleProcessor._clip_empty_token"></a>`_clip_empty_token`[`L161`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L161), <a id="FluxSampleProcessor._data_processor"></a>`_data_processor`[`L162`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L162), <a id="FluxSampleProcessor._t5_empty_token"></a>`_t5_empty_token`[`L160`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L160), <a id="FluxSampleProcessor._tokenizer"></a>`_tokenizer`[`L158`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L158)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`DatasetBuildContext`](../../components/data/types.md#DatasetBuildContext), [`SampleProcessor`](../../components/data/dataset.md#SampleProcessor), [`FluxTokenizerContainer`](tokenizer.md#FluxTokenizerContainer), [`Config`](flux_datasets.md#FluxSampleProcessor.Config), [`encode`](tokenizer.md#FluxTokenizerContainer.encode), [`tokenizer`](../../components/data/types.md#DatasetBuildContext.tokenizer), [`prompt_dropout_prob`](flux_datasets.md#FluxSampleProcessor.Config.prompt_dropout_prob), [`data_processor`](flux_datasets.md#FluxSampleProcessor.Config.data_processor), [`FluxSample`](flux_datasets.md#FluxSample), [`img_size`](flux_datasets.md#FluxSampleProcessor.Config.img_size)
- used by: [`DATASETS`](flux_datasets.md#DATASETS.DATASETS), [`__init__`](../../experiments/tpu/datasets.md#TPUGrainDataLoader.__init__), [`SampleProcessor`](../../components/data/dataset.md#SampleProcessor), [`_flux_dataset`](config_registry.md#_flux_dataset)

### <a id="FluxSampleProcessor.Config"></a>`FluxSampleProcessor.Config`  ·  implements/extends Config
- def: [`torchtitan/models/flux/flux_datasets.py:140`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L140)
- signature: `class Config(SampleProcessor.Config):`
- members:
  - <a id="FluxSampleProcessor.Config.data_processor"></a>`data_processor` — [`L141`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L141)
  - <a id="FluxSampleProcessor.Config.img_size"></a>`img_size` — [`L143`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L143)
  - <a id="FluxSampleProcessor.Config.prompt_dropout_prob"></a>`prompt_dropout_prob` — [`L142`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L142)
- protocol/private: <a id="FluxSampleProcessor.Config.__post_init__"></a>`__post_init__`[`L145`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L145)
- uses (calls/refs, reference-scoped): [`SampleProcessor`](../../components/data/dataset.md#SampleProcessor), [`Config`](../../components/data/dataset.md#SampleProcessor.Config)
- used by: [`DATASETS`](flux_datasets.md#DATASETS.DATASETS), [`__init__`](../../experiments/tpu/datasets.md#TPUGrainDataLoader.__init__), [`_flux_dataset`](config_registry.md#_flux_dataset), [`__init__`](flux_datasets.md#FluxSampleProcessor.__init__), [`_data_processor`](flux_datasets.md#FluxSampleProcessor._data_processor), [`img_size`](flux_datasets.md#FluxSampleProcessor.img_size), [`prompt_dropout_prob`](flux_datasets.md#FluxSampleProcessor.prompt_dropout_prob)

### <a id="FluxValidationDatasetConfig"></a>`FluxValidationDatasetConfig`
- def: [`torchtitan/models/flux/flux_datasets.py:315`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L315)
- doc: Adds checkpointable round-robin validation timesteps to Flux rows.
- signature: `class FluxValidationDatasetConfig:`
- members:
  - <a id="FluxValidationDatasetConfig.build"></a>`build(self, *, context: DatasetBuildContext, dataset_iteration_policy: DatasetIterationPolicy)` — [`L320`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L320)
  - <a id="FluxValidationDatasetConfig.dataset"></a>`dataset` — [`L318`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L318)
- uses (calls/refs, reference-scoped): [`DatasetBuildContext`](../../components/data/types.md#DatasetBuildContext), [`DatasetIterationPolicy`](../../components/data/types.md#DatasetIterationPolicy), [`build`](../../components/data/dataset.md#DatasetConfig.build), [`DatasetConfig`](../../components/data/dataset.md#DatasetConfig), [`read_options`](../../components/data/types.md#DatasetBuildContext.read_options), [`_add_validation_timestep`](flux_datasets.md#_add_validation_timestep)
- used by: [`flux_debugmodel`](config_registry.md#flux_debugmodel), [`flux_dev`](config_registry.md#flux_dev), [`flux_schnell`](config_registry.md#flux_schnell), [`all_timesteps`](validate.md#FluxValidator.all_timesteps), [`dl_config`](validate.md#FluxValidator.dl_config)

## Functions
- <a id="_add_validation_timestep"></a>`_add_validation_timestep(index: int, sample: FluxSample)` — [`L303`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L303)
- <a id="_cc12m_wds_data_processor"></a>`_cc12m_wds_data_processor(sample: dict[str, Any], tokenizer: FluxTokenizerContainer, output_size: int = 256, *, rng: np.random.Generator)` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L81) — Preprocess CC12M dataset sample image and text for Flux model.
- <a id="_coco_data_processor"></a>`_coco_data_processor(sample: dict[str, Any], tokenizer: FluxTokenizerContainer, output_size: int = 256, *, rng: np.random.Generator)` — [`L107`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L107) — Preprocess COCO dataset sample image and text for Flux model.
- <a id="_is_not_none"></a>`_is_not_none(sample: Any)` — [`L225`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L225)
- <a id="_process_cc12m_image"></a>`_process_cc12m_image(img: PIL.Image.Image, output_size: int = 256, *, rng: np.random.Generator)` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L39) — Process CC12M image to the desired size.

## Module values
- <a id="DATASETS.DATASETS"></a>`DATASETS` — [`L229`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L229) — documented in [flux-diffusion-model](../../../../concepts/flux-diffusion-model.md)
- <a id="_VALIDATION_TIMESTEPS"></a>`_VALIDATION_TIMESTEPS` — [`L300`](../../../../../../../raw/code/torchtitan/torchtitan/models/flux/flux_datasets.py#L300)

