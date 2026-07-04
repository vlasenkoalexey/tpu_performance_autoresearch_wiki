---
title: 'Module: easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen3_5_moe.modeling_qwen3_5_moe`/
symbols:
  Qwen3_5MoeModel.__init__: Qwen3_5MoeModel#__init__().
  Qwen3_5MoeModel.__call__: Qwen3_5MoeModel#__call__().
  Qwen3_5MoeForConditionalGeneration.__init__: Qwen3_5MoeForConditionalGeneration#__init__().
  Qwen3_5MoeModel: Qwen3_5MoeModel#
  Qwen3_5MoeForConditionalGeneration: Qwen3_5MoeForConditionalGeneration#
  Qwen3_5MoeTextModel: Qwen3_5MoeTextModel#
  Qwen3_5MoeForCausalLM: Qwen3_5MoeForCausalLM#
  Qwen3_5MoeForCausalLM.__init__: Qwen3_5MoeForCausalLM#__init__().
  Qwen3_5MoeModel.language_model: Qwen3_5MoeModel#language_model.
  Qwen3_5MoeModel.visual: Qwen3_5MoeModel#visual.
  Qwen3_5MoeForConditionalGeneration._task_type: Qwen3_5MoeForConditionalGeneration#_task_type.
  Qwen3_5MoeForConditionalGeneration.vocab_size: Qwen3_5MoeForConditionalGeneration#vocab_size.
  Qwen3_5MoeForCausalLM._config_class: Qwen3_5MoeForCausalLM#_config_class.
  Qwen3_5MoeForConditionalGeneration._config_class: Qwen3_5MoeForConditionalGeneration#_config_class.
  Qwen3_5MoeForCausalLM._model_type: Qwen3_5MoeForCausalLM#_model_type.
  Qwen3_5MoeForConditionalGeneration._model_type: Qwen3_5MoeForConditionalGeneration#_model_type.
  Qwen3_5MoeForConditionalGeneration._auto_register: Qwen3_5MoeForConditionalGeneration#_auto_register.
  Qwen3_5MoeForConditionalGeneration._supports_video: Qwen3_5MoeForConditionalGeneration#_supports_video.
  Qwen3_5MoeForConditionalGeneration._uses_mrope: Qwen3_5MoeForConditionalGeneration#_uses_mrope.
  Qwen3_5MoeForConditionalGeneration._vision_tower_name: Qwen3_5MoeForConditionalGeneration#_vision_tower_name.
  Qwen3_5MoeForConditionalGeneration._projector_name: Qwen3_5MoeForConditionalGeneration#_projector_name.
  Qwen3_5MoeForConditionalGeneration._language_model_name: Qwen3_5MoeForConditionalGeneration#_language_model_name.
  Qwen3_5MoeForConditionalGeneration.loss_type: Qwen3_5MoeForConditionalGeneration#loss_type.
  Qwen3_5MoeForConditionalGeneration.get_input_embeddings: Qwen3_5MoeForConditionalGeneration#get_input_embeddings().
  Qwen3_5MoeForConditionalGeneration.set_input_embeddings: Qwen3_5MoeForConditionalGeneration#set_input_embeddings().
  Qwen3_5MoeForConditionalGeneration.set_decoder: Qwen3_5MoeForConditionalGeneration#set_decoder().
  Qwen3_5MoeForConditionalGeneration.get_decoder: Qwen3_5MoeForConditionalGeneration#get_decoder().
  Qwen3_5MoeForConditionalGeneration.visual: Qwen3_5MoeForConditionalGeneration#visual().
  Qwen3_5MoeForConditionalGeneration.language_model: Qwen3_5MoeForConditionalGeneration#language_model().
  Qwen3_5MoeForConditionalGeneration.get_video_features: Qwen3_5MoeForConditionalGeneration#get_video_features().
  Qwen3_5MoeForConditionalGeneration.get_image_features: Qwen3_5MoeForConditionalGeneration#get_image_features().
  Qwen3_5MoeForConditionalGeneration.compute_embedding: Qwen3_5MoeForConditionalGeneration#compute_embedding().
  __all__: __all__.
---
# Module: [`easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py)

## Classes
### `Qwen3_5MoeForCausalLM`  ·  implements/extends Qwen3NextForCausalLM
- def: [`easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py:58`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L58)
- doc: Qwen3.5-MoE text causal language model.
- signature: `class Qwen3_5MoeForCausalLM(Qwen3NextForCausalLM):`
- members:
  - `__init__(self, config: Qwen3_5MoeTextConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L75`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L75) — Initialize Qwen3.5-MoE text causal LM.
- protocol/private: `_config_class`[`L73`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L73), `_model_type`[`L72`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L72)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`Qwen3NextForCausalLM`](../qwen3_next/modeling_qwen3_next.md#Qwen3NextForCausalLM), [`Qwen3_5MoeTextModel`](modeling_qwen3_5_moe.md#Qwen3_5MoeTextModel), [`Qwen3_5MoeTextConfig`](qwen3_5_moe_configuration.md#Qwen3_5MoeTextConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`Qwen3NextForCausalLM`](../qwen3_next/modeling_qwen3_next.md#Qwen3NextForCausalLM)

### `Qwen3_5MoeForConditionalGeneration`  ·  implements/extends BaseVisionLanguageModule
- def: [`easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py:316`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L316)
- doc: Qwen3.5-MoE multimodal conditional generation model.
- signature: `class Qwen3_5MoeForConditionalGeneration(BaseVisionLanguageModule[Qwen3_5MoeModel, Qwen3_5MoeConfig]):`
- members:
  - `__init__(self, config: Qwen3_5MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L345`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L345) — Initialize Qwen3.5 MoE vision-language model for conditional generation.
  - `compute_embedding(self, input_ids, *args, **kwargs)` — [`L429`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L429) — Compute embeddings with multimodal fusion.
  - `get_decoder(self)` — [`L397`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L397) — Get the language model decoder.
  - `get_image_features(self, pixel_values: jax.Array, image_grid_thw: jax.Array | None = None, image_max_grid_size: int | None = None)` — [`L420`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L420) — Encode images into continuous embeddings.
  - `get_input_embeddings(self)` — [`L385`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L385) — Get the input embedding layer.
  - `get_video_features(self, pixel_values_videos: jax.Array, video_grid_thw: jax.Array | None = None, video_max_grid_size: int | None = None)` — [`L411`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L411) — Encode videos into continuous embeddings.
  - `language_model(self)` — [`L407`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L407) — Property to access the language model for backward compatibility.
  - `set_decoder(self, decoder)` — [`L393`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L393) — Set the language model decoder.
  - `set_input_embeddings(self, value)` — [`L389`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L389) — Set the input embedding layer.
  - `visual(self)` — [`L402`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L402) — Property to access the vision transformer for backward compatibility.
  - `loss_type` — [`L343`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L343)
  - `vocab_size` — [`L383`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L383)
- protocol/private: `_auto_register`[`L335`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L335), `_config_class`[`L334`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L334), `_language_model_name`[`L341`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L341), `_model_type`[`L333`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L333), `_projector_name`[`L340`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L340), `_supports_video`[`L336`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L336), `_task_type`[`L332`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L332), `_uses_mrope`[`L337`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L337), `_vision_tower_name`[`L339`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L339)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseVisionLanguageModule`](../_base/vision_language_module.md#BaseVisionLanguageModule), [`IMAGE_TEXT_TO_TEXT`](../../infra/factory.md#TaskType.IMAGE_TEXT_TO_TEXT), [`text_config`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig.text_config), [`__init__`](../_base/vision_language_module.md#BaseVisionLanguageModule.__init__), [`Qwen3_5MoeModel`](modeling_qwen3_5_moe.md#Qwen3_5MoeModel), [`Qwen3_5MoeConfig`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig), [`vision_config`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig.vision_config), [`vocab_size`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.vocab_size), [`spatial_merge_size`](../qwen3_vl_moe/qwen3_vl_moe_configuration.md#Qwen3VLMoeVisionConfig.spatial_merge_size), [`image_token_id`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig.image_token_id), [`video_token_id`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig.video_token_id)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseVisionLanguageModule`](../_base/vision_language_module.md#BaseVisionLanguageModule), [`compute_embedding`](../_base/vision_language_module.md#BaseVisionLanguageModule.compute_embedding), [`get_image_features`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_image_features), [`get_video_features`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_video_features), [`get_decoder`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_decoder)

### `Qwen3_5MoeModel`  ·  implements/extends Qwen3VLMoeModel
- def: [`easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py:109`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L109)
- doc: Qwen3.5-MoE multimodal (vision-language) base model.
- signature: `class Qwen3_5MoeModel(Qwen3VLMoeModel):`
- members:
  - `__call__(self, input_ids: jax.Array | None = None, inputs_embeds: jax.Array | None = None, attention_mask: jax.Array | None = None, mask_info: object | None = None, position_ids: jax.Array | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, visual_pos_masks: jax.Array | None = None, deepstack_visual_embeds: list[jax.Array] | None = None, pixel_values: jax.Array | None = None, pixel_values_videos: jax.Array | None = None, image_grid_thw: tuple | None = None, video_grid_thw: tuple | None = None, image_max_grid_size: int | None = None, video_max_grid_size: int | None = None, cache_position: jax.Array | None = None, rope_deltas: jax.Array | None = None, mm_token_type_ids: jax.Array | None = None, **kwargs)` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L209) — Forward pass through the Qwen3.5-MoE multimodal model.
  - `__init__(self, config: Qwen3_5MoeConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L125) — Initialize Qwen3.5-MoE multimodal model with vision encoder and MoE text decoder.
  - `language_model` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L201)
  - `visual` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L194)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`text_config`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig.text_config), [`hidden_size`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.hidden_size), [`Qwen3VLMoeModel`](../qwen3_vl_moe/modeling_qwen3_vl_moe.md#Qwen3VLMoeModel), [`Qwen3VLMoeConfig`](../qwen3_vl_moe/qwen3_vl_moe_configuration.md#Qwen3VLMoeConfig), [`Qwen3VLMoeTextConfig`](../qwen3_vl_moe/qwen3_vl_moe_configuration.md#Qwen3VLMoeTextConfig), [`Qwen3VLMoeVisionTransformerPretrainedModel`](../qwen3_vl_moe/modeling_qwen3_vl_moe.md#Qwen3VLMoeVisionTransformerPretrainedModel), [`to_dict`](../../infra/base_config.md#EasyDeLBaseConfig.to_dict), [`Qwen3_5MoeTextModel`](modeling_qwen3_5_moe.md#Qwen3_5MoeTextModel), [`compute_embedding`](../qwen3_vl_moe/modeling_qwen3_vl_moe.md#Qwen3VLMoeModel.compute_embedding), [`initializer_range`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.initializer_range), [`Qwen3_5MoeConfig`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig), [`get_image_features`](../qwen3_vl_moe/modeling_qwen3_vl_moe.md#Qwen3VLMoeModel.get_image_features), [`vision_config`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig.vision_config), [`VISION_LM`](../../infra/factory.md#TaskType.VISION_LM), [`get_rope_index`](../qwen3_vl_moe/modeling_qwen3_vl_moe.md#Qwen3VLMoeModel.get_rope_index), [`Qwen3VLMoeModelOutputWithPast`](../qwen3_vl_moe/modeling_qwen3_vl_moe.md#Qwen3VLMoeModelOutputWithPast), [`get_video_features`](../qwen3_vl_moe/modeling_qwen3_vl_moe.md#Qwen3VLMoeModel.get_video_features), [`__init__`](../qwen3_vl_moe/modeling_qwen3_vl_moe.md#Qwen3VLMoeModel.__init__), [`attentions`](../../infra/modeling_outputs.md#MoeModelOutput.attentions), [`hidden_states`](../../infra/modeling_outputs.md#MoeModelOutput.hidden_states), [`last_hidden_state`](../../infra/modeling_outputs.md#MoeModelOutput.last_hidden_state), [`rms_norm_eps`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.rms_norm_eps), [`_maybe_flatten_position_ids_for_text`](../qwen3_5/modeling_qwen3_5.md#_maybe_flatten_position_ids_for_text), [`past_key_values`](../../infra/modeling_outputs.md#MoeModelOutput.past_key_values), [`vocab_size`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.vocab_size), [`hidden_act`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.hidden_act), [`num_hidden_layers`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.num_hidden_layers), [`vision_end_token_id`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig.vision_end_token_id), [`_get_rope_index_from_mm_token_types`](../qwen3_5/modeling_qwen3_5.md#_get_rope_index_from_mm_token_types), [`head_dim`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.head_dim)  (+11 more)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`Qwen3VLMoeModel`](../qwen3_vl_moe/modeling_qwen3_vl_moe.md#Qwen3VLMoeModel), [`__init__`](modeling_qwen3_5_moe.md#Qwen3_5MoeForConditionalGeneration.__init__), [`Qwen3_5MoeForConditionalGeneration`](modeling_qwen3_5_moe.md#Qwen3_5MoeForConditionalGeneration)

### `Qwen3_5MoeTextModel`  ·  implements/extends Qwen3NextModel
- def: [`easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py:48`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L48)
- doc: Qwen3.5-MoE text-only base model (no LM head).
- signature: `class Qwen3_5MoeTextModel(Qwen3NextModel):`
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`Qwen3NextModel`](../qwen3_next/modeling_qwen3_next.md#Qwen3NextModel), [`Qwen3_5MoeTextConfig`](qwen3_5_moe_configuration.md#Qwen3_5MoeTextConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`Qwen3NextModel`](../qwen3_next/modeling_qwen3_next.md#Qwen3NextModel), [`__init__`](modeling_qwen3_5_moe.md#Qwen3_5MoeForCausalLM.__init__), [`language_model`](modeling_qwen3_5_moe.md#Qwen3_5MoeModel.language_model)

## Module values
- `__all__` — [`L434`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/modeling_qwen3_5_moe.py#L434)

