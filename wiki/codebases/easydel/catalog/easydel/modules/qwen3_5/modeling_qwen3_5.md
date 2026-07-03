---
title: 'Module: easydel/modules/qwen3_5/modeling_qwen3_5.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen3_5/modeling_qwen3_5.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen3_5.modeling_qwen3_5`/
symbols:
  Qwen3_5Model.__init__: Qwen3_5Model#__init__().
  Qwen3_5Model.__call__: Qwen3_5Model#__call__().
  Qwen3_5Model: Qwen3_5Model#
  Qwen3_5ForConditionalGeneration.__init__: Qwen3_5ForConditionalGeneration#__init__().
  Qwen3_5ForConditionalGeneration: Qwen3_5ForConditionalGeneration#
  Qwen3_5TextModel: Qwen3_5TextModel#
  Qwen3_5ForCausalLM: Qwen3_5ForCausalLM#
  Qwen3_5ForCausalLM.__init__: Qwen3_5ForCausalLM#__init__().
  Qwen3_5Model.language_model: Qwen3_5Model#language_model.
  _maybe_flatten_position_ids_for_text: _maybe_flatten_position_ids_for_text().
  Qwen3_5Model.visual: Qwen3_5Model#visual.
  Qwen3_5ForConditionalGeneration._task_type: Qwen3_5ForConditionalGeneration#_task_type.
  Qwen3_5ForConditionalGeneration.vocab_size: Qwen3_5ForConditionalGeneration#vocab_size.
  _get_rope_index_from_mm_token_types: _get_rope_index_from_mm_token_types().
  Qwen3_5ForCausalLM._config_class: Qwen3_5ForCausalLM#_config_class.
  Qwen3_5ForConditionalGeneration._config_class: Qwen3_5ForConditionalGeneration#_config_class.
  Qwen3_5ForCausalLM._model_type: Qwen3_5ForCausalLM#_model_type.
  Qwen3_5ForConditionalGeneration._model_type: Qwen3_5ForConditionalGeneration#_model_type.
  Qwen3_5ForConditionalGeneration._auto_register: Qwen3_5ForConditionalGeneration#_auto_register.
  Qwen3_5ForConditionalGeneration._supports_video: Qwen3_5ForConditionalGeneration#_supports_video.
  Qwen3_5ForConditionalGeneration._uses_mrope: Qwen3_5ForConditionalGeneration#_uses_mrope.
  Qwen3_5ForConditionalGeneration._vision_tower_name: Qwen3_5ForConditionalGeneration#_vision_tower_name.
  Qwen3_5ForConditionalGeneration._projector_name: Qwen3_5ForConditionalGeneration#_projector_name.
  Qwen3_5ForConditionalGeneration._language_model_name: Qwen3_5ForConditionalGeneration#_language_model_name.
  Qwen3_5ForConditionalGeneration.loss_type: Qwen3_5ForConditionalGeneration#loss_type.
  Qwen3_5ForConditionalGeneration.get_input_embeddings: Qwen3_5ForConditionalGeneration#get_input_embeddings().
  Qwen3_5ForConditionalGeneration.set_input_embeddings: Qwen3_5ForConditionalGeneration#set_input_embeddings().
  Qwen3_5ForConditionalGeneration.set_decoder: Qwen3_5ForConditionalGeneration#set_decoder().
  Qwen3_5ForConditionalGeneration.get_decoder: Qwen3_5ForConditionalGeneration#get_decoder().
  Qwen3_5ForConditionalGeneration.visual: Qwen3_5ForConditionalGeneration#visual().
  Qwen3_5ForConditionalGeneration.language_model: Qwen3_5ForConditionalGeneration#language_model().
  Qwen3_5ForConditionalGeneration.get_video_features: Qwen3_5ForConditionalGeneration#get_video_features().
  Qwen3_5ForConditionalGeneration.get_image_features: Qwen3_5ForConditionalGeneration#get_image_features().
  Qwen3_5ForConditionalGeneration.compute_embedding: Qwen3_5ForConditionalGeneration#compute_embedding().
  __all__: __all__.
---
# Module: [`easydel/modules/qwen3_5/modeling_qwen3_5.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py)

## Classes
### `Qwen3_5ForCausalLM`  ·  implements/extends Qwen3NextForCausalLM
- def: [`easydel/modules/qwen3_5/modeling_qwen3_5.py:169`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L169)
- doc: Qwen3.5 text causal language model.
- signature: `class Qwen3_5ForCausalLM(Qwen3NextForCausalLM):`
- members:
  - `__init__(self, config: Qwen3_5TextConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L186) — Initialize Qwen3.5 text causal LM with MoE support.
- protocol/private: `_config_class`[`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L184), `_model_type`[`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L183)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`Qwen3NextForCausalLM`](../qwen3_next/modeling_qwen3_next.md#Qwen3NextForCausalLM), [`Qwen3_5TextConfig`](qwen3_5_configuration.md#Qwen3_5TextConfig), [`Qwen3_5TextModel`](modeling_qwen3_5.md#Qwen3_5TextModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`Qwen3NextForCausalLM`](../qwen3_next/modeling_qwen3_next.md#Qwen3NextForCausalLM)

### `Qwen3_5ForConditionalGeneration`  ·  implements/extends BaseVisionLanguageModule
- def: [`easydel/modules/qwen3_5/modeling_qwen3_5.py:419`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L419)
- doc: Qwen3.5 multimodal conditional generation model.
- signature: `class Qwen3_5ForConditionalGeneration(BaseVisionLanguageModule[Qwen3_5Model, Qwen3_5Config]):`
- members:
  - `__init__(self, config: Qwen3_5Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L447`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L447) — Initialize Qwen3.5 for conditional generation with vision-language support.
  - `compute_embedding(self, input_ids, *args, **kwargs)` — [`L527`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L527) — Compute embeddings with multimodal fusion.
  - `get_decoder(self)` — [`L495`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L495) — Get the language model decoder.
  - `get_image_features(self, pixel_values: jax.Array, image_grid_thw: jax.Array | None = None, image_max_grid_size: int | None = None)` — [`L518`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L518) — Encode images into continuous embeddings.
  - `get_input_embeddings(self)` — [`L483`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L483) — Get the input embedding layer.
  - `get_video_features(self, pixel_values_videos: jax.Array, video_grid_thw: jax.Array | None = None, video_max_grid_size: int | None = None)` — [`L509`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L509) — Encode videos into continuous embeddings.
  - `language_model(self)` — [`L505`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L505) — Property to access the language model for backward compatibility.
  - `set_decoder(self, decoder)` — [`L491`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L491) — Set the language model decoder.
  - `set_input_embeddings(self, value)` — [`L487`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L487) — Set the input embedding layer.
  - `visual(self)` — [`L500`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L500) — Property to access the vision transformer for backward compatibility.
  - `loss_type` — [`L445`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L445)
  - `vocab_size` — [`L481`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L481)
- protocol/private: `_auto_register`[`L437`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L437), `_config_class`[`L436`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L436), `_language_model_name`[`L443`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L443), `_model_type`[`L435`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L435), `_projector_name`[`L442`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L442), `_supports_video`[`L438`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L438), `_task_type`[`L434`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L434), `_uses_mrope`[`L439`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L439), `_vision_tower_name`[`L441`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L441)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseVisionLanguageModule`](../_base/vision_language_module.md#BaseVisionLanguageModule), [`IMAGE_TEXT_TO_TEXT`](../../infra/factory.md#TaskType.IMAGE_TEXT_TO_TEXT), [`text_config`](qwen3_5_configuration.md#Qwen3_5Config.text_config), [`__init__`](../_base/vision_language_module.md#BaseVisionLanguageModule.__init__), [`Qwen3_5Model`](modeling_qwen3_5.md#Qwen3_5Model), [`Qwen3_5Config`](qwen3_5_configuration.md#Qwen3_5Config), [`vision_config`](qwen3_5_configuration.md#Qwen3_5Config.vision_config), [`vocab_size`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.vocab_size), [`spatial_merge_size`](../qwen3_vl/qwen3_vl_configuration.md#Qwen3VLVisionConfig.spatial_merge_size), [`image_token_id`](qwen3_5_configuration.md#Qwen3_5Config.image_token_id), [`video_token_id`](qwen3_5_configuration.md#Qwen3_5Config.video_token_id)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseVisionLanguageModule`](../_base/vision_language_module.md#BaseVisionLanguageModule), [`compute_embedding`](../_base/vision_language_module.md#BaseVisionLanguageModule.compute_embedding), [`get_image_features`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_image_features), [`get_video_features`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_video_features), [`get_decoder`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_decoder)

### `Qwen3_5Model`  ·  implements/extends Qwen3VLModel
- def: [`easydel/modules/qwen3_5/modeling_qwen3_5.py:220`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L220)
- doc: Qwen3.5 multimodal (vision-language) base model.
- signature: `class Qwen3_5Model(Qwen3VLModel):`
- members:
  - `__call__(self, input_ids: jax.Array | None = None, inputs_embeds: jax.Array | None = None, attention_mask: jax.Array | None = None, mask_info: object | None = None, position_ids: jax.Array | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, visual_pos_masks: jax.Array | None = None, deepstack_visual_embeds: list[jax.Array] | None = None, pixel_values: jax.Array | None = None, pixel_values_videos: jax.Array | None = None, image_grid_thw: tuple | None = None, video_grid_thw: tuple | None = None, image_max_grid_size: int | None = None, video_max_grid_size: int | None = None, cache_position: jax.Array | None = None, rope_deltas: jax.Array | None = None, mm_token_type_ids: jax.Array | None = None, **kwargs)` — [`L312`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L312) — Forward pass through the Qwen3.5 multimodal model.
  - `__init__(self, config: Qwen3_5Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L236) — Initialize Qwen3.5 multimodal model with vision encoder and text decoder.
  - `language_model` — [`L304`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L304)
  - `visual` — [`L297`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L297)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`text_config`](qwen3_5_configuration.md#Qwen3_5Config.text_config), [`hidden_size`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.hidden_size), [`Qwen3VLModel`](../qwen3_vl/modeling_qwen3_vl.md#Qwen3VLModel), [`Qwen3VisionTransformerPretrainedModel`](../qwen3_vl/modeling_qwen3_vl.md#Qwen3VisionTransformerPretrainedModel), [`to_dict`](../../infra/base_config.md#EasyDeLBaseConfig.to_dict), [`Qwen3VLConfig`](../qwen3_vl/qwen3_vl_configuration.md#Qwen3VLConfig), [`Qwen3_5TextModel`](modeling_qwen3_5.md#Qwen3_5TextModel), [`compute_embedding`](../qwen3_vl/modeling_qwen3_vl.md#Qwen3VLModel.compute_embedding), [`Qwen3VLTextConfig`](../qwen3_vl/qwen3_vl_configuration.md#Qwen3VLTextConfig), [`initializer_range`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.initializer_range), [`Qwen3_5Config`](qwen3_5_configuration.md#Qwen3_5Config), [`get_image_features`](../qwen3_vl/modeling_qwen3_vl.md#Qwen3VLModel.get_image_features), [`vision_config`](qwen3_5_configuration.md#Qwen3_5Config.vision_config), [`VISION_LM`](../../infra/factory.md#TaskType.VISION_LM), [`get_rope_index`](../qwen3_vl/modeling_qwen3_vl.md#Qwen3VLModel.get_rope_index), [`Qwen3VLModelOutputWithPast`](../qwen3_vl/modeling_qwen3_vl.md#Qwen3VLModelOutputWithPast), [`get_video_features`](../qwen3_vl/modeling_qwen3_vl.md#Qwen3VLModel.get_video_features), [`__init__`](../qwen3_vl/modeling_qwen3_vl.md#Qwen3VLModel.__init__), [`attentions`](../../infra/modeling_outputs.md#MoeModelOutput.attentions), [`hidden_states`](../../infra/modeling_outputs.md#MoeModelOutput.hidden_states), [`last_hidden_state`](../../infra/modeling_outputs.md#MoeModelOutput.last_hidden_state), [`rms_norm_eps`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.rms_norm_eps), [`_maybe_flatten_position_ids_for_text`](modeling_qwen3_5.md#_maybe_flatten_position_ids_for_text), [`past_key_values`](../../infra/modeling_outputs.md#MoeModelOutput.past_key_values), [`vocab_size`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.vocab_size), [`hidden_act`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.hidden_act), [`num_hidden_layers`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.num_hidden_layers), [`vision_end_token_id`](qwen3_5_configuration.md#Qwen3_5Config.vision_end_token_id), [`_get_rope_index_from_mm_token_types`](modeling_qwen3_5.md#_get_rope_index_from_mm_token_types), [`head_dim`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.head_dim)  (+11 more)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`Qwen3VLModel`](../qwen3_vl/modeling_qwen3_vl.md#Qwen3VLModel), [`__init__`](modeling_qwen3_5.md#Qwen3_5ForConditionalGeneration.__init__), [`Qwen3_5ForConditionalGeneration`](modeling_qwen3_5.md#Qwen3_5ForConditionalGeneration)

### `Qwen3_5TextModel`  ·  implements/extends Qwen3NextModel
- def: [`easydel/modules/qwen3_5/modeling_qwen3_5.py:159`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L159)
- doc: Qwen3.5 text-only base model (no LM head).
- signature: `class Qwen3_5TextModel(Qwen3NextModel):`
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`Qwen3NextModel`](../qwen3_next/modeling_qwen3_next.md#Qwen3NextModel), [`Qwen3_5TextConfig`](qwen3_5_configuration.md#Qwen3_5TextConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`Qwen3NextModel`](../qwen3_next/modeling_qwen3_next.md#Qwen3NextModel), [`__init__`](modeling_qwen3_5.md#Qwen3_5ForCausalLM.__init__), [`language_model`](modeling_qwen3_5.md#Qwen3_5Model.language_model)

## Functions
- `_get_rope_index_from_mm_token_types(input_ids: jax.Array, mm_token_type_ids: jax.Array, image_grid_thw: jax.Array | None = None, video_grid_thw: jax.Array | None = None, attention_mask: jax.Array | None = None, spatial_merge_size: int = 1)` — [`L46`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L46) — Compute 3D mRoPE position ids from modality token-type ids.
- `_maybe_flatten_position_ids_for_text(config: Qwen3_5TextConfig, position_ids: jax.Array)` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L141) — Flatten 3D mRoPE position ids to 1D when the text config does not enable mRoPE.

## Module values
- `__all__` — [`L532`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/modeling_qwen3_5.py#L532)

