---
title: 'Module: easydel/modules/glm46v/modeling_glm46v.py'
type: catalog
provenance: extracted
module: easydel/modules/glm46v/modeling_glm46v.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.glm46v.modeling_glm46v`/
symbols:
  Glm46VForConditionalGeneration.__call__: Glm46VForConditionalGeneration#__call__().
  Glm46VForConditionalGeneration.__init__: Glm46VForConditionalGeneration#__init__().
  Glm46VForConditionalGeneration: Glm46VForConditionalGeneration#
  Glm46VModel: Glm46VModel#
  Glm46VModel.__init__: Glm46VModel#__init__().
  Glm46VForConditionalGeneration._task_type: Glm46VForConditionalGeneration#_task_type.
  Glm46VForConditionalGeneration.vocab_size: Glm46VForConditionalGeneration#vocab_size.
  Glm46VForConditionalGeneration.visual: Glm46VForConditionalGeneration#visual().
  Glm46VForConditionalGeneration.language_model: Glm46VForConditionalGeneration#language_model().
  Glm46VForConditionalGeneration.get_video_features: Glm46VForConditionalGeneration#get_video_features().
  Glm46VForConditionalGeneration.get_image_features: Glm46VForConditionalGeneration#get_image_features().
  Glm46VForConditionalGeneration.compute_embedding: Glm46VForConditionalGeneration#compute_embedding().
  Glm46VForConditionalGeneration._config_class: Glm46VForConditionalGeneration#_config_class.
  Glm46VForConditionalGeneration._model_type: Glm46VForConditionalGeneration#_model_type.
  Glm46VForConditionalGeneration._auto_register: Glm46VForConditionalGeneration#_auto_register.
  Glm46VForConditionalGeneration._supports_video: Glm46VForConditionalGeneration#_supports_video.
  Glm46VForConditionalGeneration._uses_mrope: Glm46VForConditionalGeneration#_uses_mrope.
  Glm46VForConditionalGeneration._vision_tower_name: Glm46VForConditionalGeneration#_vision_tower_name.
  Glm46VForConditionalGeneration._projector_name: Glm46VForConditionalGeneration#_projector_name.
  Glm46VForConditionalGeneration._language_model_name: Glm46VForConditionalGeneration#_language_model_name.
  Glm46VForConditionalGeneration.loss_type: Glm46VForConditionalGeneration#loss_type.
  __all__: __all__.
---
# Module: [`easydel/modules/glm46v/modeling_glm46v.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py)

## Classes
### `Glm46VForConditionalGeneration`  ·  implements/extends BaseVisionLanguageModule
- def: [`easydel/modules/glm46v/modeling_glm46v.py:86`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L86)
- doc: GLM-4.6V model for image/video-to-text conditional generation.
- signature: `class Glm46VForConditionalGeneration(BaseVisionLanguageModule[Glm46VModel, Glm46VConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, pixel_values: Array | None = None, pixel_values_videos: Array | None = None, image_grid_thw: Array | None = None, video_grid_thw: Array | None = None, rope_deltas: Array | None = None, cache_position: Array | None = None, **kwargs)` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L217) — Forward pass for multimodal conditional generation.
  - `__init__(self, config: Glm46VConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L118) — Initialize GLM-4.6V model for conditional generation.
  - `compute_embedding(self, input_ids, *args, **kwargs)` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L202) — Compute combined text and visual embeddings.
  - `get_image_features(self, pixel_values: Array, image_grid_thw: Array | None = None, **kwargs)` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L188) — Extract visual features from image inputs.
  - `get_video_features(self, pixel_values_videos: Array, video_grid_thw: Array | None = None, **kwargs)` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L173) — Extract visual features from video inputs.
  - `language_model(self)` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L165) — Access the language model decoder component.
  - `visual(self)` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L156) — Access the vision encoder component.
  - `loss_type` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L116)
  - `vocab_size` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L153)
- protocol/private: `_auto_register`[`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L108), `_config_class`[`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L107), `_language_model_name`[`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L114), `_model_type`[`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L106), `_projector_name`[`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L113), `_supports_video`[`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L109), `_task_type`[`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L105), `_uses_mrope`[`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L110), `_vision_tower_name`[`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L112)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`base_model`](../_base/_base_task_module.md#BaseTaskModule.base_model), [`BaseVisionLanguageModule`](../_base/vision_language_module.md#BaseVisionLanguageModule), [`VLMCausalLMOutput`](../../infra/modeling_outputs.md#VLMCausalLMOutput), `output_hidden_states`, [`IMAGE_TEXT_TO_TEXT`](../../infra/factory.md#TaskType.IMAGE_TEXT_TO_TEXT), [`compute_lm_logits`](../_base/_base_task_module.md#BaseTaskModule.compute_lm_logits), [`__init__`](../_base/vision_language_module.md#BaseVisionLanguageModule.__init__), [`compute_embedding`](../glm4v/modeling_glm4v.md#Glm4vModel.compute_embedding), [`apply_logit_cap`](../_base/_base_task_module.md#BaseTaskModule.apply_logit_cap), [`Glm46VModel`](modeling_glm46v.md#Glm46VModel), [`Glm46VConfig`](glm46v_configuration.md#Glm46VConfig), [`visual`](../glm4v/modeling_glm4v.md#Glm4vModel.visual), [`language_model`](../glm4v/modeling_glm4v.md#Glm4vModel.language_model), [`get_image_features`](../glm4v/modeling_glm4v.md#Glm4vModel.get_image_features), [`get_video_features`](../glm4v/modeling_glm4v.md#Glm4vModel.get_video_features), [`text_config`](glm46v_configuration.md#Glm46VConfig.text_config), [`vision_config`](glm46v_configuration.md#Glm46VConfig.vision_config), [`spatial_merge_size`](../glm4v/glm4v_configuration.md#Glm4vVisionConfig.spatial_merge_size), [`vocab_size`](../glm4v/glm4v_configuration.md#Glm4vTextConfig.vocab_size), [`image_token_id`](glm46v_configuration.md#Glm46VConfig.image_token_id), [`video_token_id`](glm46v_configuration.md#Glm46VConfig.video_token_id)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseVisionLanguageModule`](../_base/vision_language_module.md#BaseVisionLanguageModule), [`compute_embedding`](../_base/vision_language_module.md#BaseVisionLanguageModule.compute_embedding), [`get_image_features`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_image_features), [`get_video_features`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_video_features)

### `Glm46VModel`  ·  implements/extends Glm4vModel
- def: [`easydel/modules/glm46v/modeling_glm46v.py:40`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L40)
- doc: GLM-4.6V multimodal model integrating vision encoder and text decoder.
- signature: `class Glm46VModel(Glm4vModel):`
- members:
  - `__init__(self, config: Glm46VConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L57`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L57) — Initialize GLM-4.6V multimodal base model.
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`Glm4vModel`](../glm4v/modeling_glm4v.md#Glm4vModel), [`Glm46VConfig`](glm46v_configuration.md#Glm46VConfig), [`VISION_LM`](../../infra/factory.md#TaskType.VISION_LM), [`__init__`](../glm4v/modeling_glm4v.md#Glm4vModel.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`Glm4vModel`](../glm4v/modeling_glm4v.md#Glm4vModel), [`__init__`](modeling_glm46v.md#Glm46VForConditionalGeneration.__init__), [`Glm46VForConditionalGeneration`](modeling_glm46v.md#Glm46VForConditionalGeneration)

## Module values
- `__all__` — [`L329`](../../../../../../../raw/code/EasyDeL/easydel/modules/glm46v/modeling_glm46v.py#L329)

