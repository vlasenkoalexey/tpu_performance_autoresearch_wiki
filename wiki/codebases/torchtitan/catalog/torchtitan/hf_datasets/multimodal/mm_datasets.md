---
title: 'Module: torchtitan/hf_datasets/multimodal/mm_datasets.py'
type: catalog
provenance: extracted
module: torchtitan/hf_datasets/multimodal/mm_datasets.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.hf_datasets.multimodal.mm_datasets`/
symbols:
  MM_DATASETS.MM_DATASETS: MM_DATASETS.MM_DATASETS.
  MultiModalProcessor.__call__: MultiModalProcessor#__call__().
  MMSamplePackingConfig.build: MMSamplePackingConfig#build().
  _process_mm_sample: _process_mm_sample().
  MultiModalProcessor: MultiModalProcessor#
  MultiModalProcessor.Config: MultiModalProcessor#Config#
  MultiModalProcessor._config: MultiModalProcessor#_config.
  MultiModalProcessor.Config.patch_size: MultiModalProcessor#Config#patch_size.
  MultiModalProcessor.Config.temporal_patch_size: MultiModalProcessor#Config#temporal_patch_size.
  MultiModalProcessor.Config.spatial_merge_size: MultiModalProcessor#Config#spatial_merge_size.
  MultiModalProcessor.Config.sample_processor: MultiModalProcessor#Config#sample_processor.
  _process_cc12_wd_sample: _process_cc12_wd_sample().
  _process_obelics_sample: _process_obelics_sample().
  MultiModalProcessor.Config.resize_fn: MultiModalProcessor#Config#resize_fn.
  MultiModalProcessor.__init__: MultiModalProcessor#__init__().
  MultiModalProcessor._max_context_length: MultiModalProcessor#_max_context_length.
  MultiModalProcessor._tokenizer: MultiModalProcessor#_tokenizer.
  MMSamplePackingConfig.dataset: MMSamplePackingConfig#dataset.
  MultiModalProcessor.Config.image_mean: MultiModalProcessor#Config#image_mean.
  MultiModalProcessor.Config.image_std: MultiModalProcessor#Config#image_std.
  MultiModalProcessor.Config.max_patches: MultiModalProcessor#Config#max_patches.
  MultiModalProcessor.Config.max_patches_per_side: MultiModalProcessor#Config#max_patches_per_side.
  MMSamplePackingConfig.__post_init__: MMSamplePackingConfig#__post_init__().
  MultiModalProcessor.Config.min_pixels: MultiModalProcessor#Config#min_pixels.
  MultiModalProcessor.Config.max_pixels: MultiModalProcessor#Config#max_pixels.
  MultiModalProcessor.Config.video_dir: MultiModalProcessor#Config#video_dir.
  MultiModalProcessor.Config.video_fps: MultiModalProcessor#Config#video_fps.
  MultiModalProcessor.Config.video_min_frames: MultiModalProcessor#Config#video_min_frames.
  MultiModalProcessor.Config.video_max_frames: MultiModalProcessor#Config#video_max_frames.
  MMSamplePackingConfig.num_packing_bins: MMSamplePackingConfig#num_packing_bins.
  _mm_sample_to_packing_input: _mm_sample_to_packing_input().
  _packing_output_to_mm_sample: _packing_output_to_mm_sample().
  MMSamplePackingConfig: MMSamplePackingConfig#
---
# Module: [`torchtitan/hf_datasets/multimodal/mm_datasets.py`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py)

## Classes
### <a id="MMSamplePackingConfig"></a>`MMSamplePackingConfig`
- def: [`torchtitan/hf_datasets/multimodal/mm_datasets.py:377`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L377)
- doc: Packs whole multimodal documents into fixed-length rows.
- signature: `class MMSamplePackingConfig:`
- members:
  - <a id="MMSamplePackingConfig.build"></a>`build(self, *, context: DatasetBuildContext, dataset_iteration_policy: DatasetIterationPolicy)` — [`L388`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L388) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MMSamplePackingConfig.dataset"></a>`dataset` — [`L380`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L380)
  - <a id="MMSamplePackingConfig.num_packing_bins"></a>`num_packing_bins` — [`L381`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L381) — ---
- protocol/private: <a id="MMSamplePackingConfig.__post_init__"></a>`__post_init__`[`L384`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L384)
- uses (calls/refs, reference-scoped): [`IGNORE_INDEX`](../../components/loss.md#IGNORE_INDEX), [`DatasetBuildContext`](../../components/data/types.md#DatasetBuildContext), [`DatasetIterationPolicy`](../../components/data/types.md#DatasetIterationPolicy), [`num_tokens_per_batch`](../../components/data/types.md#DatasetBuildContext.num_tokens_per_batch), [`build`](../../components/data/dataset.md#DatasetConfig.build), [`max_context_length`](../../components/data/types.md#DatasetBuildContext.max_context_length), [`tokenizer`](../../components/data/types.md#DatasetBuildContext.tokenizer), [`DatasetConfig`](../../components/data/dataset.md#DatasetConfig), [`seed`](../../components/data/types.md#DatasetIterationPolicy.seed), [`read_options`](../../components/data/types.md#DatasetBuildContext.read_options), [`shuffle`](../../components/data/types.md#DatasetIterationPolicy.shuffle), [`_mm_sample_to_packing_input`](mm_datasets.md#_mm_sample_to_packing_input), [`_packing_output_to_mm_sample`](mm_datasets.md#_packing_output_to_mm_sample)

### <a id="MultiModalProcessor"></a>`MultiModalProcessor`  ·  implements/extends SampleProcessor
- def: [`torchtitan/hf_datasets/multimodal/mm_datasets.py:275`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L275) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
- doc: Adapts a multimodal processor to Grain's map contract.
- signature: `class MultiModalProcessor(SampleProcessor):`
- protocol/private: <a id="MultiModalProcessor.__call__"></a>`__call__`[`L303`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L303), <a id="MultiModalProcessor.__init__"></a>`__init__`[`L298`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L298), <a id="MultiModalProcessor._config"></a>`_config`[`L299`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L299), <a id="MultiModalProcessor._max_context_length"></a>`_max_context_length`[`L301`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L301), <a id="MultiModalProcessor._tokenizer"></a>`_tokenizer`[`L300`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L300)
- uses (calls/refs, reference-scoped): [`logger`](../../tools/logging.md#logger), [`DatasetBuildContext`](../../components/data/types.md#DatasetBuildContext), [`SampleProcessor`](../../components/data/dataset.md#SampleProcessor), [`Config`](mm_datasets.md#MultiModalProcessor.Config), [`max_context_length`](../../components/data/types.md#DatasetBuildContext.max_context_length), [`tokenizer`](../../components/data/types.md#DatasetBuildContext.tokenizer), [`patch_size`](mm_datasets.md#MultiModalProcessor.Config.patch_size), [`spatial_merge_size`](mm_datasets.md#MultiModalProcessor.Config.spatial_merge_size), [`temporal_patch_size`](mm_datasets.md#MultiModalProcessor.Config.temporal_patch_size), [`sample_processor`](mm_datasets.md#MultiModalProcessor.Config.sample_processor), [`resize_fn`](mm_datasets.md#MultiModalProcessor.Config.resize_fn), [`image_mean`](mm_datasets.md#MultiModalProcessor.Config.image_mean), [`image_std`](mm_datasets.md#MultiModalProcessor.Config.image_std), [`max_patches`](mm_datasets.md#MultiModalProcessor.Config.max_patches), [`max_patches_per_side`](mm_datasets.md#MultiModalProcessor.Config.max_patches_per_side), [`max_pixels`](mm_datasets.md#MultiModalProcessor.Config.max_pixels), [`min_pixels`](mm_datasets.md#MultiModalProcessor.Config.min_pixels), [`video_dir`](mm_datasets.md#MultiModalProcessor.Config.video_dir), [`video_fps`](mm_datasets.md#MultiModalProcessor.Config.video_fps), [`video_max_frames`](mm_datasets.md#MultiModalProcessor.Config.video_max_frames), [`video_min_frames`](mm_datasets.md#MultiModalProcessor.Config.video_min_frames)
- used by: [`_kimi_multimodal_dataloader`](../../models/kimi_k2_7/config_registry.md#_kimi_multimodal_dataloader), [`MM_DATASETS`](mm_datasets.md#MM_DATASETS.MM_DATASETS), [`_muse_glimmer_mm_dataloader`](../../models/muse_glimmer/config_registry.md#_muse_glimmer_mm_dataloader), [`_kimi_k3_multimodal_dataloader`](../../models/kimi_k3/config_registry.md#_kimi_k3_multimodal_dataloader), [`_multimodal_collator_config`](../../models/qwen3_5/config_registry.md#_multimodal_collator_config), [`_multimodal_collator_config`](../../models/qwen3_6/config_registry.md#_multimodal_collator_config), [`_multimodal_collator_config`](../../models/qwen3_8/config_registry.md#_multimodal_collator_config), [`SampleProcessor`](../../components/data/dataset.md#SampleProcessor)

### <a id="MultiModalProcessor.Config"></a>`MultiModalProcessor.Config`  ·  implements/extends Config
- def: [`torchtitan/hf_datasets/multimodal/mm_datasets.py:279`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L279) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
- signature: `class Config(SampleProcessor.Config):`
- members:
  - <a id="MultiModalProcessor.Config.image_mean"></a>`image_mean` — [`L286`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L286)
  - <a id="MultiModalProcessor.Config.image_std"></a>`image_std` — [`L287`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L287)
  - <a id="MultiModalProcessor.Config.max_patches"></a>`max_patches` — [`L291`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L291)
  - <a id="MultiModalProcessor.Config.max_patches_per_side"></a>`max_patches_per_side` — [`L292`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L292)
  - <a id="MultiModalProcessor.Config.max_pixels"></a>`max_pixels` — [`L285`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L285)
  - <a id="MultiModalProcessor.Config.min_pixels"></a>`min_pixels` — [`L284`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L284)
  - <a id="MultiModalProcessor.Config.patch_size"></a>`patch_size` — [`L281`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L281) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalProcessor.Config.resize_fn"></a>`resize_fn` — [`L288`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L288) — --- — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalProcessor.Config.sample_processor"></a>`sample_processor` — [`L280`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L280) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalProcessor.Config.spatial_merge_size"></a>`spatial_merge_size` — [`L283`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L283) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalProcessor.Config.temporal_patch_size"></a>`temporal_patch_size` — [`L282`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L282) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
  - <a id="MultiModalProcessor.Config.video_dir"></a>`video_dir` — [`L293`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L293)
  - <a id="MultiModalProcessor.Config.video_fps"></a>`video_fps` — [`L294`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L294)
  - <a id="MultiModalProcessor.Config.video_max_frames"></a>`video_max_frames` — [`L296`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L296)
  - <a id="MultiModalProcessor.Config.video_min_frames"></a>`video_min_frames` — [`L295`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L295)
- uses (calls/refs, reference-scoped): [`SampleProcessor`](../../components/data/dataset.md#SampleProcessor), [`Config`](../../components/data/dataset.md#SampleProcessor.Config), [`resize_to_pixel_budget`](utils/image.md#resize_to_pixel_budget)
- used by: [`_kimi_multimodal_dataloader`](../../models/kimi_k2_7/config_registry.md#_kimi_multimodal_dataloader), [`MM_DATASETS`](mm_datasets.md#MM_DATASETS.MM_DATASETS), [`_muse_glimmer_mm_dataloader`](../../models/muse_glimmer/config_registry.md#_muse_glimmer_mm_dataloader), [`_kimi_k3_multimodal_dataloader`](../../models/kimi_k3/config_registry.md#_kimi_k3_multimodal_dataloader), [`__call__`](mm_datasets.md#MultiModalProcessor.__call__), [`_multimodal_collator_config`](../../models/qwen3_5/config_registry.md#_multimodal_collator_config), [`_multimodal_collator_config`](../../models/qwen3_6/config_registry.md#_multimodal_collator_config), [`_multimodal_collator_config`](../../models/qwen3_8/config_registry.md#_multimodal_collator_config), [`__init__`](mm_datasets.md#MultiModalProcessor.__init__)

## Functions
- <a id="_mm_sample_to_packing_input"></a>`_mm_sample_to_packing_input(sample: dict[str, Any])` — [`L437`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L437) — Convert Torch token fields to the arrays expected by Grain packing.
- <a id="_packing_output_to_mm_sample"></a>`_packing_output_to_mm_sample(packing_output: dict[str, Any], *, max_context_length: int)` — [`L448`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L448) — Restore Torch token fields and flatten per-document media lists.
- <a id="_process_cc12_wd_sample"></a>`_process_cc12_wd_sample(sample: dict[str, Any], tokenizer: MultiModalTokenizer, patch_size: int, temporal_patch_size: int, spatial_merge_size: int, min_pixels: int, max_pixels: int, image_mean: tuple[float, ...], image_std: tuple[float, ...], **kwargs)` — [`L241`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L241) — Process a sample from the CC12-WD dataset (text-image pairs). — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
- <a id="_process_mm_sample"></a>`_process_mm_sample(texts: list[str | None], images: list[bytes | None], tokenizer: MultiModalTokenizer, patch_size: int, temporal_patch_size: int, spatial_merge_size: int, min_pixels: int, max_pixels: int, image_mean: tuple[float, ...], image_std: tuple[float, ...], resize_fn: Callable[..., tuple[int, int, int, int]], max_patches: int, max_patches_per_side: int, **kwargs)` — [`L89`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L89) — Common processing logic for multimodal samples. — documented in [hf-datasets](../../../../concepts/hf-datasets.md)
- <a id="_process_obelics_sample"></a>`_process_obelics_sample(sample: dict[str, Any], tokenizer: MultiModalTokenizer, patch_size: int, temporal_patch_size: int, spatial_merge_size: int, min_pixels: int, max_pixels: int, image_mean: tuple[float, ...], image_std: tuple[float, ...], **kwargs)` — [`L213`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L213) — Process a sample from the OBELICS dataset (interleaved text and images). — documented in [hf-datasets](../../../../concepts/hf-datasets.md)

## Module values
- <a id="MM_DATASETS.MM_DATASETS"></a>`MM_DATASETS` — [`L339`](../../../../../../../raw/code/torchtitan/torchtitan/hf_datasets/multimodal/mm_datasets.py#L339) — documented in [hf-datasets](../../../../concepts/hf-datasets.md)

