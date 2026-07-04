---
title: 'Module: easydel/modules/llava/modeling_llava.py'
type: catalog
provenance: extracted
module: easydel/modules/llava/modeling_llava.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.llava.modeling_llava`/
symbols:
  LlavaForConditionalGeneration.__call__: LlavaForConditionalGeneration#__call__().
  LlavaModel.__call__: LlavaModel#__call__().
  LlavaForConditionalGeneration: LlavaForConditionalGeneration#
  LlavaModel: LlavaModel#
  LlavaModel.compute_embedding: LlavaModel#compute_embedding().
  LlavaModel.get_image_features: LlavaModel#get_image_features().
  LlavaForConditionalGeneration.__init__: LlavaForConditionalGeneration#__init__().
  LlavaModel.language_model: LlavaModel#language_model.
  LlavaModel.vision_tower: LlavaModel#vision_tower.
  LlavaMultiModalProjector.linear_1: LlavaMultiModalProjector#linear_1.
  LlavaMultiModalProjector.__call__: LlavaMultiModalProjector#__call__().
  LlavaMultiModalProjector.act: LlavaMultiModalProjector#act.
  LlavaMultiModalProjector.linear_2: LlavaMultiModalProjector#linear_2.
  LlavaModel.init_cache: LlavaModel#init_cache().
  LlavaModel.__init__: LlavaModel#__init__().
  LlavaModel.pad_token_id: LlavaModel#pad_token_id.
  LlavaModel.prepare_inputs_for_generation: LlavaModel#prepare_inputs_for_generation().
  LlavaModel.update_inputs_for_generation: LlavaModel#update_inputs_for_generation().
  LlavaModel.get_decoder: LlavaModel#get_decoder().
  LlavaModel.get_embedding: LlavaModel#get_embedding().
  LlavaForConditionalGeneration._task_type: LlavaForConditionalGeneration#_task_type.
  LlavaForConditionalGeneration.get_image_features: LlavaForConditionalGeneration#get_image_features().
  LlavaForConditionalGeneration.compute_embedding: LlavaForConditionalGeneration#compute_embedding().
  LlavaForConditionalGeneration.init_cache: LlavaForConditionalGeneration#init_cache().
  LlavaForConditionalGeneration.get_vision_tower: LlavaForConditionalGeneration#get_vision_tower().
  LlavaForConditionalGeneration.get_projector: LlavaForConditionalGeneration#get_projector().
  LlavaForConditionalGeneration.get_language_model: LlavaForConditionalGeneration#get_language_model().
  LlavaModel.multi_modal_projector: LlavaModel#multi_modal_projector.
  LlavaCausalLMOutputWithPast: LlavaCausalLMOutputWithPast#
  LlavaCausalLMOutputWithPast.past_key_values: LlavaCausalLMOutputWithPast#past_key_values.
  LlavaModel.vision_feature_layer: LlavaModel#vision_feature_layer.
  LlavaMultiModalProjector.__init__: LlavaMultiModalProjector#__init__().
  LlavaMultiModalProjector.rngs: LlavaMultiModalProjector#rngs.
  LlavaModel.get_encoder: LlavaModel#get_encoder().
  LlavaForConditionalGeneration._config_class: LlavaForConditionalGeneration#_config_class.
  LlavaModel.vision_feature_select_strategy: LlavaModel#vision_feature_select_strategy.
  LlavaCausalLMOutputWithPast.hidden_states: LlavaCausalLMOutputWithPast#hidden_states.
  LlavaCausalLMOutputWithPast.last_hidden_state: LlavaCausalLMOutputWithPast#last_hidden_state.
  LlavaCausalLMOutputWithPast.attentions: LlavaCausalLMOutputWithPast#attentions.
  LlavaCausalLMOutputWithPast.image_hidden_states: LlavaCausalLMOutputWithPast#image_hidden_states.
  LlavaMultiModalProjector: LlavaMultiModalProjector#
  logger: logger.
  LlavaCausalLMOutputWithPast.loss: LlavaCausalLMOutputWithPast#loss.
  LlavaCausalLMOutputWithPast.logits: LlavaCausalLMOutputWithPast#logits.
  LlavaMultiModalProjector.config: LlavaMultiModalProjector#config.
  LlavaMultiModalProjector.dtype: LlavaMultiModalProjector#dtype.
  LlavaMultiModalProjector.param_dtype: LlavaMultiModalProjector#param_dtype.
  LlavaMultiModalProjector.precision: LlavaMultiModalProjector#precision.
  LlavaModel.get_lm_head: LlavaModel#get_lm_head().
  LlavaForConditionalGeneration._model_type: LlavaForConditionalGeneration#_model_type.
  LlavaForConditionalGeneration._auto_register: LlavaForConditionalGeneration#_auto_register.
  LlavaForConditionalGeneration._supports_video: LlavaForConditionalGeneration#_supports_video.
  LlavaForConditionalGeneration._uses_mrope: LlavaForConditionalGeneration#_uses_mrope.
  LlavaForConditionalGeneration._vision_tower_name: LlavaForConditionalGeneration#_vision_tower_name.
  LlavaForConditionalGeneration._projector_name: LlavaForConditionalGeneration#_projector_name.
  LlavaForConditionalGeneration._language_model_name: LlavaForConditionalGeneration#_language_model_name.
  LlavaForConditionalGeneration.loss_type: LlavaForConditionalGeneration#loss_type.
  LlavaForConditionalGeneration.apply_lm_head: LlavaForConditionalGeneration#apply_lm_head().
---
# Module: [`easydel/modules/llava/modeling_llava.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py)

## Classes
### `LlavaCausalLMOutputWithPast`  ·  implements/extends ModelOutput
- def: [`easydel/modules/llava/modeling_llava.py:48`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L48)
- doc: Base class for Llava causal language model (or autoregressive) outputs.
- signature: `class LlavaCausalLMOutputWithPast(ModelOutput):`
- members:
  - `attentions` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L87)
  - `hidden_states` — [`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L85)
  - `image_hidden_states` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L88)
  - `last_hidden_state` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L86)
  - `logits` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L83)
  - `loss` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L82)
  - `past_key_values` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L84)
- uses (calls/refs, reference-scoped): [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`ModelOutput`](../../infra/modeling_outputs.md#ModelOutput)
- used by: [`ModelOutput`](../../infra/modeling_outputs.md#ModelOutput), [`__call__`](modeling_llava.md#LlavaForConditionalGeneration.__call__), [`__call__`](modeling_llava.md#LlavaModel.__call__)

### `LlavaForConditionalGeneration`  ·  implements/extends BaseVisionLanguageModule
- def: [`easydel/modules/llava/modeling_llava.py:522`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L522)
- doc: LLaVA model for conditional text generation based on image inputs.
- signature: `class LlavaForConditionalGeneration(BaseVisionLanguageModule[LlavaModel, LlavaConfig]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, pixel_values: Array | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, **lm_kwargs)` — [`L632`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L632) — Forward pass for image-conditioned text generation.
  - `__init__(self, config: LlavaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L557`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L557) — Initialize LLaVA model for conditional generation.
  - `apply_lm_head(self, hidden_states: Array)` — [`L757`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L757) — Apply the language modeling head to hidden states.
  - `compute_embedding(self, input_ids, *args, **kwargs)` — [`L617`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L617) — Compute input embeddings with merged image and text features.
  - `get_image_features(self, pixel_values: Float[Array, "batch channels height width"], **kwargs)` — [`L596`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L596) — Extract and project image features from pixel values.
  - `get_language_model(self)` — [`L787`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L787) — Return the language model component.
  - `get_projector(self)` — [`L779`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L779) — Return the multimodal projector component.
  - `get_vision_tower(self)` — [`L771`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L771) — Return the vision tower component.
  - `init_cache(self, batch_size, max_length, starts=None, shardings=None, pad_token_id=None)` — [`L733`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L733) — Initialize the key-value cache for autoregressive generation.
  - `loss_type` — [`L555`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L555)
- protocol/private: `_auto_register`[`L546`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L546), `_config_class`[`L545`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L545), `_language_model_name`[`L553`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L553), `_model_type`[`L544`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L544), `_projector_name`[`L552`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L552), `_supports_video`[`L547`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L547), `_task_type`[`L543`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L543), `_uses_mrope`[`L548`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L548), `_vision_tower_name`[`L551`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L551)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`base_model`](../_base/_base_task_module.md#BaseTaskModule.base_model), [`BaseVisionLanguageModule`](../_base/vision_language_module.md#BaseVisionLanguageModule), [`VLMCausalLMOutput`](../../infra/modeling_outputs.md#VLMCausalLMOutput), `output_hidden_states`, [`IMAGE_TEXT_TO_TEXT`](../../infra/factory.md#TaskType.IMAGE_TEXT_TO_TEXT), [`compute_lm_logits`](../_base/_base_task_module.md#BaseTaskModule.compute_lm_logits), [`__init__`](../_base/vision_language_module.md#BaseVisionLanguageModule.__init__), [`apply_logit_cap`](../_base/_base_task_module.md#BaseTaskModule.apply_logit_cap), [`LlavaModel`](modeling_llava.md#LlavaModel), [`compute_embedding`](modeling_llava.md#LlavaModel.compute_embedding), [`get_image_features`](modeling_llava.md#LlavaModel.get_image_features), [`LlavaConfig`](llava_configuration.md#LlavaConfig), [`language_model`](modeling_llava.md#LlavaModel.language_model), [`vision_tower`](modeling_llava.md#LlavaModel.vision_tower), [`vision_feature_layer`](llava_configuration.md#LlavaConfig.vision_feature_layer), [`init_cache`](modeling_llava.md#LlavaModel.init_cache), [`multi_modal_projector`](modeling_llava.md#LlavaModel.multi_modal_projector), [`past_key_values`](modeling_llava.md#LlavaCausalLMOutputWithPast.past_key_values), [`attentions`](modeling_llava.md#LlavaCausalLMOutputWithPast.attentions), [`hidden_states`](modeling_llava.md#LlavaCausalLMOutputWithPast.hidden_states), [`image_hidden_states`](modeling_llava.md#LlavaCausalLMOutputWithPast.image_hidden_states), [`image_token_id`](llava_configuration.md#LlavaConfig.image_token_id), [`last_hidden_state`](modeling_llava.md#LlavaCausalLMOutputWithPast.last_hidden_state)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseVisionLanguageModule`](../_base/vision_language_module.md#BaseVisionLanguageModule), [`init_cache`](../../infra/mixins/generation.md#EasyGenerationMixin.init_cache), [`compute_embedding`](../_base/vision_language_module.md#BaseVisionLanguageModule.compute_embedding), [`get_image_features`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_image_features), [`get_language_model`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_language_model), [`get_vision_tower`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_vision_tower), [`apply_lm_head`](../_base/conditional_generation_module.md#BaseConditionalGenerationModule.apply_lm_head), [`get_projector`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_projector)

### `LlavaModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/llava/modeling_llava.py:167`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L167)
- doc: LlavaModel model for conditional text generation based on image inputs.
- signature: `class LlavaModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, pixel_values: Array | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, **lm_kwargs)` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L307) — Forward pass through the LLaVA base model.
  - `__init__(self, config: LlavaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L180) — Initialize LLaVA base model.
  - `compute_embedding(self, input_ids: Int[Array, "batch seq_len"] | None, *, image_features: Array | None = None, pixel_values: Array | None = None, **kwargs)` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L253) — Compute input embeddings with merged image and text features.
  - `get_decoder(self)` — [`L496`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L496) — Return the decoder component of the model.
  - `get_embedding(self)` — [`L512`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L512) — Return the embedding layer of the model.
  - `get_encoder(self)` — [`L486`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L486) — Return the encoder component of the model.
  - `get_image_features(self, pixel_values: Array)` — [`L234`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L234) — Extracts and projects image features from the vision tower.
  - `get_lm_head(self)` — [`L504`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L504) — Return the language model head.
  - `init_cache(self, batch_size, max_length, starts=None, shardings=None, pad_token_id=None)` — [`L402`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L402) — Initialize the key-value cache for autoregressive generation.
  - `prepare_inputs_for_generation(self, input_ids: Int[Array, "batch seq_len"], max_length: int, pad_token_id: int, starts: int | None = None, pixel_values: Array | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None)` — [`L428`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L428) — Prepare inputs for autoregressive text generation.
  - `update_inputs_for_generation(self, model_outputs, model_kwargs)` — [`L466`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L466) — Update model inputs for the next generation step.
  - `language_model` — [`L222`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L222)
  - `multi_modal_projector` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L215)
  - `pad_token_id` — [`L230`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L230)
  - `vision_feature_layer` — [`L231`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L231)
  - `vision_feature_select_strategy` — [`L232`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L232)
  - `vision_tower` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L208)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`BaseVisionLanguageModule`](../_base/vision_language_module.md#BaseVisionLanguageModule), `pad_token_id`, [`init_cache`](../../infra/mixins/generation.md#EasyGenerationMixin.init_cache), [`prepare_inputs_for_generation`](../../infra/mixins/generation.md#EasyGenerationMixin.prepare_inputs_for_generation), `output_hidden_states`, [`compute_embedding`](../../infra/base_module.md#EasyDeLBaseModule.compute_embedding), [`update_inputs_for_generation`](../../infra/mixins/generation.md#EasyGenerationMixin.update_inputs_for_generation), [`from_config`](../auto/auto_modeling.md#BaseAutoEasyModel.from_config), [`BASE_VISION`](../../infra/factory.md#TaskType.BASE_VISION), [`AutoEasyDeLVisionModel`](../auto/auto_modeling.md#AutoEasyDeLVisionModel), [`AutoEasyDeLModel`](../auto/auto_modeling.md#AutoEasyDeLModel), [`LlavaConfig`](llava_configuration.md#LlavaConfig), [`vision_feature_layer`](llava_configuration.md#LlavaConfig.vision_feature_layer), [`merge_multimodal_embeddings`](../_base/vision_language_module.md#BaseVisionLanguageModule.merge_multimodal_embeddings), [`vision_config`](llava_configuration.md#LlavaConfig.vision_config), [`LlavaCausalLMOutputWithPast`](modeling_llava.md#LlavaCausalLMOutputWithPast), [`LlavaMultiModalProjector`](modeling_llava.md#LlavaMultiModalProjector)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`init_cache`](../../infra/mixins/generation.md#EasyGenerationMixin.init_cache), [`prepare_inputs_for_generation`](../../infra/mixins/generation.md#EasyGenerationMixin.prepare_inputs_for_generation), [`compute_embedding`](../../infra/base_module.md#EasyDeLBaseModule.compute_embedding), [`update_inputs_for_generation`](../../infra/mixins/generation.md#EasyGenerationMixin.update_inputs_for_generation), [`LlavaForConditionalGeneration`](modeling_llava.md#LlavaForConditionalGeneration), [`__init__`](modeling_llava.md#LlavaForConditionalGeneration.__init__), [`compute_embedding`](modeling_llava.md#LlavaForConditionalGeneration.compute_embedding), [`get_image_features`](modeling_llava.md#LlavaForConditionalGeneration.get_image_features), [`get_language_model`](modeling_llava.md#LlavaForConditionalGeneration.get_language_model), [`get_projector`](modeling_llava.md#LlavaForConditionalGeneration.get_projector), [`get_vision_tower`](modeling_llava.md#LlavaForConditionalGeneration.get_vision_tower), [`init_cache`](modeling_llava.md#LlavaForConditionalGeneration.init_cache)

### `LlavaMultiModalProjector`  ·  implements/extends Module
- def: [`easydel/modules/llava/modeling_llava.py:91`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L91)
- doc: Multi-modal projector for LLaVA models.
- signature: `class LlavaMultiModalProjector(nn.Module):`
- members:
  - `__call__(self, image_features: jax.Array)` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L149) — Project image features into the language model embedding space.
  - `__init__(self, config: LlavaConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L99) — Initialize the LLaVA multi-modal projector.
  - `act` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L137)
  - `config` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L118)
  - `dtype` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L119)
  - `linear_1` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L126)
  - `linear_2` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L138)
  - `param_dtype` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L120)
  - `precision` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L121)
  - `rngs` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L122)
- uses (calls/refs, reference-scoped): [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`LlavaConfig`](llava_configuration.md#LlavaConfig), [`vision_feature_layer`](llava_configuration.md#LlavaConfig.vision_feature_layer), [`vision_config`](llava_configuration.md#LlavaConfig.vision_config), [`multimodal_projector_bias`](llava_configuration.md#LlavaConfig.multimodal_projector_bias), [`projector_hidden_act`](llava_configuration.md#LlavaConfig.projector_hidden_act)
- used by: [`multi_modal_projector`](modeling_llava.md#LlavaModel.multi_modal_projector)

## Module values
- `logger` — [`L44`](../../../../../../../raw/code/EasyDeL/easydel/modules/llava/modeling_llava.py#L44)

