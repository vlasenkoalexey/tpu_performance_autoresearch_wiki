---
title: 'Module: easydel/modules/_base/_vlm_features.py'
type: catalog
provenance: extracted
module: easydel/modules/_base/_vlm_features.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules._base._vlm_features`/
symbols:
  MultiModalMergeFeature.__repr__: MultiModalMergeFeature#__repr__().
  MultiModalMergeFeature.get_placeholder_token_ids: MultiModalMergeFeature#get_placeholder_token_ids().
  VisionEncoderFeature.extract_features: VisionEncoderFeature#extract_features().
  VisionEncoderFeature.__repr__: VisionEncoderFeature#__repr__().
  MultiModalMergeFeature.merge: MultiModalMergeFeature#merge().
  VideoProcessingFeature.__repr__: VideoProcessingFeature#__repr__().
  MultiDimensionalRoPEFeature.__repr__: MultiDimensionalRoPEFeature#__repr__().
  MultiModalMergeFeature.create_multimodal_mask: MultiModalMergeFeature#create_multimodal_mask().
  VisionEncoderFeature: VisionEncoderFeature#
  MultiModalMergeFeature: MultiModalMergeFeature#
  MultiModalMergeFeature.image_token_id: MultiModalMergeFeature#image_token_id.
  MultiModalMergeFeature.video_token_id: MultiModalMergeFeature#video_token_id.
  VideoProcessingFeature: VideoProcessingFeature#
  MultiDimensionalRoPEFeature: MultiDimensionalRoPEFeature#
  VideoProcessingFeature.compute_video_grid: VideoProcessingFeature#compute_video_grid().
  VideoProcessingFeature.get_temporal_positions: VideoProcessingFeature#get_temporal_positions().
  VisionEncoderFeature.vision_feature_layer: VisionEncoderFeature#vision_feature_layer.
  VisionEncoderFeature.vision_feature_select_strategy: VisionEncoderFeature#vision_feature_select_strategy.
  VideoProcessingFeature.temporal_patch_size: VideoProcessingFeature#temporal_patch_size.
  VideoProcessingFeature.tokens_per_second: VideoProcessingFeature#tokens_per_second.
  MultiModalMergeFeature.strategy: MultiModalMergeFeature#strategy.
  MultiModalMergeFeature._merge_with_cumsum: MultiModalMergeFeature#_merge_with_cumsum().
  MultiDimensionalRoPEFeature.spatial_merge_size: MultiDimensionalRoPEFeature#spatial_merge_size.
  MultiDimensionalRoPEFeature.mrope_section: MultiDimensionalRoPEFeature#mrope_section.
  VisionEncoderFeature.__init__: VisionEncoderFeature#__init__().
  MultiModalMergeFeature.__init__: MultiModalMergeFeature#__init__().
  VideoProcessingFeature.__init__: VideoProcessingFeature#__init__().
  VideoProcessingFeature.is_enabled: VideoProcessingFeature#is_enabled().
  MultiDimensionalRoPEFeature.__init__: MultiDimensionalRoPEFeature#__init__().
  MultiDimensionalRoPEFeature.is_enabled: MultiDimensionalRoPEFeature#is_enabled().
  MultiDimensionalRoPEFeature.compute_vision_positions: MultiDimensionalRoPEFeature#compute_vision_positions().
  MultiDimensionalRoPEFeature.get_default_position_ids: MultiDimensionalRoPEFeature#get_default_position_ids().
---
# Module: [`easydel/modules/_base/_vlm_features.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py)

## Classes
### `MultiDimensionalRoPEFeature`
- def: [`easydel/modules/_base/_vlm_features.py:722`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L722)
- doc: Compute 3D mRoPE position IDs for multimodal tokens.
- signature: `class MultiDimensionalRoPEFeature:`
- members:
  - `__init__(self, spatial_merge_size: int = 2, mrope_section: tuple[int, int, int] = (24, 20, 20))` — [`L765`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L765) — Initialize multi-dimensional RoPE feature.
  - `__repr__(self)` — [`L927`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L927) — Return string representation of the feature.
  - `compute_vision_positions(self, grid_thw: tuple[int, int, int], start_position: int = 0)` — [`L809`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L809) — Compute 3D position indices for a single vision input.
  - `get_default_position_ids(self, sequence_length: int, batch_size: int = 1)` — [`L882`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L882) — Get default position IDs for text-only sequences.
  - `is_enabled(self)` — [`L801`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L801) — Check if mRoPE is enabled.
  - `mrope_section` — [`L798`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L798)
  - `spatial_merge_size` — [`L797`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L797)
- used by: [`_mrope_feature`](vision_language_module.md#BaseVisionLanguageModule._mrope_feature)

### `MultiModalMergeFeature`
- def: [`easydel/modules/_base/_vlm_features.py:243`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L243)
- doc: Handle multimodal embedding merge strategies for VLM models.
- signature: `class MultiModalMergeFeature:`
- members:
  - `__init__(self, strategy: str = "placeholder", image_token_id: int | None = None, video_token_id: int | None = None)` — [`L280`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L280) — Initialize multimodal merge feature.
  - `__repr__(self)` — [`L495`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L495) — Return string representation of the feature.
  - `_merge_with_cumsum(self, inputs_embeds: Float[Array, "batch seq_len hidden"], is_multimodal: Array, multimodal_embeddings: Float[Array, "num_tokens hidden"])` — [`L423`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L423) — Merge using efficient cumsum-based gathering.
  - `create_multimodal_mask(self, input_ids: Int[Array, "batch seq_len"])` — [`L464`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L464) — Create boolean mask indicating multimodal token positions.
  - `get_placeholder_token_ids(self)` — [`L330`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L330) — Get list of all configured placeholder token IDs.
  - `merge(self, input_ids: Int[Array, "batch seq_len"], inputs_embeds: Float[Array, "batch seq_len hidden"], multimodal_embeddings: Float[Array, "num_tokens hidden"], placeholder_token_id: int | list[int] | None = None)` — [`L354`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L354) — Merge multimodal embeddings into text embeddings.
  - `image_token_id` — [`L327`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L327)
  - `strategy` — [`L326`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L326)
  - `video_token_id` — [`L328`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L328)
- used by: [`_multimodal_merge_feature`](vision_language_module.md#BaseVisionLanguageModule._multimodal_merge_feature), [`_get_multimodal_mask`](vision_language_module.md#BaseVisionLanguageModule._get_multimodal_mask)

### `VideoProcessingFeature`
- def: [`easydel/modules/_base/_vlm_features.py:507`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L507)
- doc: Handle video-specific processing for VLM models.
- signature: `class VideoProcessingFeature:`
- members:
  - `__init__(self, temporal_patch_size: int = 2, tokens_per_second: float = 1)` — [`L546`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L546) — Initialize video processing feature.
  - `__repr__(self)` — [`L710`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L710) — Return string representation of the feature.
  - `compute_video_grid(self, num_frames: int, height: int, width: int, patch_size: int, spatial_merge_size: int = 1)` — [`L596`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L596) — Compute temporal, height, width grid dimensions for video.
  - `get_temporal_positions(self, video_grid_thw: Array, second_per_grid_ts: list[float] | None = None)` — [`L652`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L652) — Compute temporal position indices for video tokens.
  - `is_enabled(self)` — [`L588`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L588) — Check if video processing is enabled.
  - `temporal_patch_size` — [`L584`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L584)
  - `tokens_per_second` — [`L585`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L585)
- used by: [`_video_feature`](vision_language_module.md#BaseVisionLanguageModule._video_feature)

### `VisionEncoderFeature`
- def: [`easydel/modules/_base/_vlm_features.py:72`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L72)
- doc: Manage vision encoder feature extraction for VLM models.
- signature: `class VisionEncoderFeature:`
- members:
  - `__init__(self, vision_feature_layer: int | list[int] = -1, vision_feature_select_strategy: str = "default")` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L108) — Initialize vision encoder feature.
  - `__repr__(self)` — [`L234`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L234) — Return string representation of the feature.
  - `extract_features(self, hidden_states: tuple[Array, ...], feature_layer: int | list[int] | None = None, select_strategy: str | None = None)` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L165) — Extract and process features from vision encoder hidden states.
  - `vision_feature_layer` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L162)
  - `vision_feature_select_strategy` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/_base/_vlm_features.py#L163)
- used by: [`_select_vision_features`](vision_language_module.md#BaseVisionLanguageModule._select_vision_features), [`_vision_encoder_feature`](vision_language_module.md#BaseVisionLanguageModule._vision_encoder_feature)

