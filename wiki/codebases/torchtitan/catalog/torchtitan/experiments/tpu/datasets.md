---
title: 'Module: torchtitan/experiments/tpu/datasets.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/datasets.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.datasets`/
symbols:
  c4_test_dataloader: c4_test_dataloader().
  TPUGrainDataLoader.__init__: TPUGrainDataLoader#__init__().
  _text_dataset: _text_dataset().
  TPUGrainDataLoader.Config: TPUGrainDataLoader#Config#
  TPUGrainDataLoader: TPUGrainDataLoader#
  TPUGrainDataLoader.Config.dataset: TPUGrainDataLoader#Config#dataset.
  TPUGrainDataLoader.Config.dataset_path: TPUGrainDataLoader#Config#dataset_path.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/datasets.py`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/datasets.py)

## Classes
### <a id="TPUGrainDataLoader"></a>`TPUGrainDataLoader`  ·  implements/extends GrainDataLoader
- def: [`torchtitan/experiments/tpu/datasets.py:65`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/datasets.py#L65)
- doc: GrainDataLoader wrapper preserving TPU CLI flags (`dataset`, `dataset_path`).
- signature: `class TPUGrainDataLoader(GrainDataLoader):`
- protocol/private: <a id="TPUGrainDataLoader.__init__"></a>`__init__`[`L73`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/datasets.py#L73)
- uses (calls/refs, reference-scoped): [`GrainDataLoader`](../../components/data/loader.md#GrainDataLoader), [`DATASETS`](../../hf_datasets/text_datasets.md#DATASETS.DATASETS), [`ConcatThenSplitPackingConfig`](../../components/data/packing.md#ConcatThenSplitPackingConfig), [`DATASETS`](../../models/flux/flux_datasets.md#DATASETS.DATASETS), [`dataset`](../../components/data/packing.md#ConcatThenSplitPackingConfig.dataset), [`source`](../../components/data/dataset.md#SingleDatasetConfig.source), [`processor`](../../components/data/dataset.md#SingleDatasetConfig.processor), [`_text_dataset`](datasets.md#_text_dataset), [`Config`](../../models/flux/flux_datasets.md#FluxSampleProcessor.Config), [`FluxSampleProcessor`](../../models/flux/flux_datasets.md#FluxSampleProcessor), [`Config`](datasets.md#TPUGrainDataLoader.Config), [`__init__`](../../components/data/loader.md#GrainDataLoader.__init__), [`dataset`](datasets.md#TPUGrainDataLoader.Config.dataset), [`dataset_path`](datasets.md#TPUGrainDataLoader.Config.dataset_path), [`img_size`](../../models/flux/flux_datasets.md#FluxSampleProcessor.Config.img_size)
- used by: [`flux_debugmodel`](../../models/flux/config_registry.md#flux_debugmodel), [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`qwen35_moe_35b`](qwen3_5/config_registry.md#qwen35_moe_35b), [`GrainDataLoader`](../../components/data/loader.md#GrainDataLoader), [`c4_test_dataloader`](datasets.md#c4_test_dataloader)

### <a id="TPUGrainDataLoader.Config"></a>`TPUGrainDataLoader.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/datasets.py:69`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/datasets.py#L69)
- signature: `class Config(GrainDataLoader.Config):`
- members:
  - <a id="TPUGrainDataLoader.Config.dataset"></a>`dataset` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/datasets.py#L70)
  - <a id="TPUGrainDataLoader.Config.dataset_path"></a>`dataset_path` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/datasets.py#L71)
- uses (calls/refs, reference-scoped): [`GrainDataLoader`](../../components/data/loader.md#GrainDataLoader), [`Config`](../../components/data/loader.md#GrainDataLoader.Config)
- used by: [`flux_debugmodel`](../../models/flux/config_registry.md#flux_debugmodel), [`qwen3_moe_30b`](qwen3/config_registry.md#qwen3_moe_30b), [`qwen35_moe_35b`](qwen3_5/config_registry.md#qwen35_moe_35b), [`c4_test_dataloader`](datasets.md#c4_test_dataloader), [`__init__`](datasets.md#TPUGrainDataLoader.__init__)

## Functions
- <a id="_text_dataset"></a>`_text_dataset(name: str, dataset_path: str | None)` — [`L29`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/datasets.py#L29) — Resolves a registered text dataset, applying `dataset_path` if given.
- <a id="c4_test_dataloader"></a>`c4_test_dataloader(**kwargs: Any)` — [`L97`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/datasets.py#L97) — Builds the packed `c4_test` dataloader used by the TPU test recipes.

## Module values
- <a id="__all__"></a>`__all__` — [`L23`](../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/datasets.py#L23)

