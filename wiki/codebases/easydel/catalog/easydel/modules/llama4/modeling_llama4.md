---
title: 'Module: easydel/modules/llama4/modeling_llama4.py'
type: catalog
provenance: extracted
module: easydel/modules/llama4/modeling_llama4.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.llama4.modeling_llama4`/
symbols:
  Llama4TextModel.__call__: Llama4TextModel#__call__().
  Llama4VisionModel.__call__: Llama4VisionModel#__call__().
  Llama4TextDecoderLayer.__call__: Llama4TextDecoderLayer#__call__().
  Llama4TextMoe.__init__: Llama4TextMoe#__init__().
  Llama4VisionAttention.__call__: Llama4VisionAttention#__call__().
  Llama4ForConditionalGeneration.__call__: Llama4ForConditionalGeneration#__call__().
  Llama4TextMoe.__call__: Llama4TextMoe#__call__().
  Llama4VisionEncoderLayer.__call__: Llama4VisionEncoderLayer#__call__().
  Llama4ForCausalLM: Llama4ForCausalLM#
  Llama4TextModel: Llama4TextModel#
  Llama4VisionModel: Llama4VisionModel#
  Llama4TextModel.embed_tokens: Llama4TextModel#embed_tokens.
  Llama4ForSequenceClassification: Llama4ForSequenceClassification#
  Llama4ForConditionalGeneration: Llama4ForConditionalGeneration#
  Llama4TextMLP.__call__: Llama4TextMLP#__call__().
  Llama4TextAttention._postprocess_qkv: Llama4TextAttention#_postprocess_qkv().
  Llama4VisionEncoder.__call__: Llama4VisionEncoder#__call__().
  Llama4VisionModel.positional_embedding_vlm: Llama4VisionModel#positional_embedding_vlm.
  Llama4ForConditionalGeneration.compute_embedding: Llama4ForConditionalGeneration#compute_embedding().
  Llama4TextExperts.gate_proj: Llama4TextExperts#gate_proj.
  Llama4TextExperts.up_proj: Llama4TextExperts#up_proj.
  Llama4TextExperts.down_proj: Llama4TextExperts#down_proj.
  Llama4TextDecoderLayer.feed_forward: Llama4TextDecoderLayer#feed_forward.
  Llama4VisionAttention.head_dim: Llama4VisionAttention#head_dim.
  Llama4VisionModel.class_embedding: Llama4VisionModel#class_embedding.
  Llama4TextAttention.qk_norm: Llama4TextAttention#qk_norm.
  Llama4TextExperts.__call__: Llama4TextExperts#__call__().
  Llama4VisionEncoder.precision: Llama4VisionEncoder#precision.
  Llama4UnfoldConvolution.stride: Llama4UnfoldConvolution#stride.
  Llama4TextMoe.experts: Llama4TextMoe#experts.
  Llama4TextDecoderLayer.input_layernorm: Llama4TextDecoderLayer#input_layernorm.
  Llama4TextDecoderLayer.post_attention_layernorm: Llama4TextDecoderLayer#post_attention_layernorm.
  Llama4VisionAttention.q_proj: Llama4VisionAttention#q_proj.
  Llama4VisionAttention.k_proj: Llama4VisionAttention#k_proj.
  Llama4VisionAttention.v_proj: Llama4VisionAttention#v_proj.
  Llama4VisionAttention.o_proj: Llama4VisionAttention#o_proj.
  Llama4VisionAttention.attention_performer: Llama4VisionAttention#attention_performer.
  Llama4VisionEncoderLayer.post_attention_layernorm: Llama4VisionEncoderLayer#post_attention_layernorm.
  Llama4UnfoldConvolution.hidden_size: Llama4UnfoldConvolution#hidden_size.
  Llama4TextExperts.act_fn: Llama4TextExperts#act_fn.
  Llama4ForConditionalGeneration.vision_model: Llama4ForConditionalGeneration#vision_model.
  Llama4TextAttention._create_attention_performer: Llama4TextAttention#_create_attention_performer().
  Llama4TextAttention._create_rotary: Llama4TextAttention#_create_rotary().
  Llama4TextAttention._apply_rotary: Llama4TextAttention#_apply_rotary().
  Llama4ForCausalLM.__init__: Llama4ForCausalLM#__init__().
  Llama4ForSequenceClassification.__init__: Llama4ForSequenceClassification#__init__().
  Llama4VisionPixelShuffleMLP.__call__: Llama4VisionPixelShuffleMLP#__call__().
  Llama4VisionAttention.attention_dropout: Llama4VisionAttention#attention_dropout.
  Llama4VisionMLP2.__call__: Llama4VisionMLP2#__call__().
  Llama4VisionMLP.__call__: Llama4VisionMLP#__call__().
  Llama4UnfoldConvolution.__call__: Llama4UnfoldConvolution#__call__().
  Llama4ForConditionalGeneration.__init__: Llama4ForConditionalGeneration#__init__().
  Llama4TextDecoderLayer.is_moe_layer: Llama4TextDecoderLayer#is_moe_layer.
  Llama4VisionMLP2.activation_fn: Llama4VisionMLP2#activation_fn.
  Llama4ForConditionalGeneration.get_image_features: Llama4ForConditionalGeneration#get_image_features().
  Llama4VisionAttention.embed_dim: Llama4VisionAttention#embed_dim.
  Llama4VisionAttention.num_heads: Llama4VisionAttention#num_heads.
  Llama4UnfoldConvolution.kernel_size: Llama4UnfoldConvolution#kernel_size.
  Llama4VisionModel.hidden_size: Llama4VisionModel#hidden_size.
  Llama4TextMLP.activation_fn: Llama4TextMLP#activation_fn.
  Llama4TextMoe.router: Llama4TextMoe#router.
  Llama4TextMoe.ffn_activation: Llama4TextMoe#ffn_activation().
  Llama4TextAttention.attn_temperature_tuning: Llama4TextAttention#attn_temperature_tuning.
  Llama4TextModel.norm: Llama4TextModel#norm.
  Llama4VisionEncoderLayer.input_layernorm: Llama4VisionEncoderLayer#input_layernorm.
  Llama4VisionEncoder.layers: Llama4VisionEncoder#layers.
  Llama4UnfoldConvolution.linear: Llama4UnfoldConvolution#linear.
  Llama4VisionModel.num_patches: Llama4VisionModel#num_patches.
  Llama4VisionModel.layernorm_pre: Llama4VisionModel#layernorm_pre.
  Llama4VisionModel.layernorm_post: Llama4VisionModel#layernorm_post.
  Llama4TextMLP.precision: Llama4TextMLP#precision.
  Llama4TextModel.__init__: Llama4TextModel#__init__().
  Llama4ForCausalLM._task_type: Llama4ForCausalLM#_task_type.
  Llama4ForSequenceClassification._task_type: Llama4ForSequenceClassification#_task_type.
  Llama4VisionAttention.__init__: Llama4VisionAttention#__init__().
  Llama4UnfoldConvolution.__init__: Llama4UnfoldConvolution#__init__().
  Llama4VisionModel.__init__: Llama4VisionModel#__init__().
  Llama4ForConditionalGeneration._task_type: Llama4ForConditionalGeneration#_task_type.
  Llama4ForConditionalGeneration.pad_token_id: Llama4ForConditionalGeneration#pad_token_id.
  Llama4TextModel.layers: Llama4TextModel#layers.
  Llama4VisionModel.scale: Llama4VisionModel#scale.
  Llama4VisionModel.patch_embedding: Llama4VisionModel#patch_embedding.
  Llama4ForConditionalGeneration.multi_modal_projector: Llama4ForConditionalGeneration#multi_modal_projector.
  Llama4TextAttention.use_rope: Llama4TextAttention#use_rope.
  Llama4TextL2Norm._norm: Llama4TextL2Norm#_norm().
  Llama4TextMoe: Llama4TextMoe#
  Llama4TextMoe.shared_expert: Llama4TextMoe#shared_expert.
  Llama4TextMoe._sigmoid_topk_weights: Llama4TextMoe#_sigmoid_topk_weights().
  Llama4TextAttention: Llama4TextAttention#
  Llama4TextAttention.attn_scale: Llama4TextAttention#attn_scale.
  Llama4TextAttention.floor_scale: Llama4TextAttention#floor_scale.
  Llama4TextDecoderLayer.self_attn: Llama4TextDecoderLayer#self_attn.
  Llama4MultiModalProjector.linear_1: Llama4MultiModalProjector#linear_1.
  Llama4VisionPixelShuffleMLP.mlp: Llama4VisionPixelShuffleMLP#mlp.
  vision_apply_rotary_emb: vision_apply_rotary_emb().
  Llama4VisionAttention: Llama4VisionAttention#
  Llama4VisionMLP2.fc1: Llama4VisionMLP2#fc1.
  Llama4VisionMLP.activation_fn: Llama4VisionMLP#activation_fn.
  Llama4VisionEncoderLayer.self_attn: Llama4VisionEncoderLayer#self_attn.
  Llama4VisionEncoderLayer.mlp: Llama4VisionEncoderLayer#mlp.
  Llama4UnfoldConvolution.num_channels: Llama4UnfoldConvolution#num_channels.
  Llama4VisionModel.image_size: Llama4VisionModel#image_size.
  Llama4VisionModel.patch_size: Llama4VisionModel#patch_size.
  Llama4VisionModel.model: Llama4VisionModel#model.
  Llama4VisionModel.vision_adapter: Llama4VisionModel#vision_adapter.
  Llama4VisionModel.vision_idx: Llama4VisionModel#vision_idx.
  Llama4TextMLP.config: Llama4TextMLP#config.
  Llama4VisionEncoder.config: Llama4VisionEncoder#config.
  Llama4CausalLMOutputWithPast: Llama4CausalLMOutputWithPast#
  Llama4CausalLMOutputWithPast.past_key_values: Llama4CausalLMOutputWithPast#past_key_values.
  Llama4TextExperts.__init__: Llama4TextExperts#__init__().
  Llama4TextExperts.num_experts: Llama4TextExperts#num_experts.
  Llama4TextExperts.expert_dim: Llama4TextExperts#expert_dim.
  Llama4TextL2Norm.__call__: Llama4TextL2Norm#__call__().
  Llama4TextMLP.__init__: Llama4TextMLP#__init__().
  Llama4TextMoe.num_experts: Llama4TextMoe#num_experts.
  Llama4TextAttention.__init__: Llama4TextAttention#__init__().
  Llama4TextDecoderLayer.__init__: Llama4TextDecoderLayer#__init__().
  Llama4TextModel.get_embedding: Llama4TextModel#get_embedding().
  Llama4ForCausalLM._config_class: Llama4ForCausalLM#_config_class.
  Llama4ForSequenceClassification._config_class: Llama4ForSequenceClassification#_config_class.
  Llama4MultiModalProjector.__call__: Llama4MultiModalProjector#__call__().
  Llama4VisionPixelShuffleMLP.inner_dim: Llama4VisionPixelShuffleMLP#inner_dim.
  Llama4VisionMLP.rngs: Llama4VisionMLP#rngs.
  Llama4VisionEncoderLayer.__init__: Llama4VisionEncoderLayer#__init__().
  Llama4VisionEncoder.__init__: Llama4VisionEncoder#__init__().
  Llama4VisionModel.num_channels: Llama4VisionModel#num_channels.
  Llama4VisionModel.get_embedding: Llama4VisionModel#get_embedding().
  Llama4ForConditionalGeneration._config_class: Llama4ForConditionalGeneration#_config_class.
  Llama4ForConditionalGeneration.get_encoder: Llama4ForConditionalGeneration#get_encoder().
  Llama4ForConditionalGeneration.get_vision_tower: Llama4ForConditionalGeneration#get_vision_tower().
  Llama4ForConditionalGeneration.get_projector: Llama4ForConditionalGeneration#get_projector().
  Llama4TextMLP: Llama4TextMLP#
  Llama4TextAttention._cached_position_ids: Llama4TextAttention#_cached_position_ids.
  Llama4VisionPixelShuffleMLP.pixel_shuffle_ratio: Llama4VisionPixelShuffleMLP#pixel_shuffle_ratio.
  Llama4VisionEncoderLayer.config: Llama4VisionEncoderLayer#config.
  _vision_freqs: _vision_freqs().
  Llama4TextExperts: Llama4TextExperts#
  Llama4TextExperts.config: Llama4TextExperts#config.
  Llama4TextExperts.intermediate_size: Llama4TextExperts#intermediate_size.
  Llama4TextL2Norm: Llama4TextL2Norm#
  Llama4TextL2Norm.eps: Llama4TextL2Norm#eps.
  Llama4TextMLP.gate_proj: Llama4TextMLP#gate_proj.
  Llama4TextMLP.down_proj: Llama4TextMLP#down_proj.
  Llama4TextMLP.up_proj: Llama4TextMLP#up_proj.
  Llama4TextMoe._scale_inputs: Llama4TextMoe#_scale_inputs().
  Llama4TextMoe._passthrough_weights: Llama4TextMoe#_passthrough_weights().
  Llama4TextMoe._unity_output_weights: Llama4TextMoe#_unity_output_weights().
  Llama4TextDecoderLayer: Llama4TextDecoderLayer#
  Llama4MultiModalProjector: Llama4MultiModalProjector#
  pixel_shuffle: pixel_shuffle().
  Llama4VisionPixelShuffleMLP: Llama4VisionPixelShuffleMLP#
  reshape_for_broadcast: reshape_for_broadcast().
  Llama4VisionMLP2.intermediate_size: Llama4VisionMLP2#intermediate_size.
  Llama4VisionMLP2.fc2: Llama4VisionMLP2#fc2.
  Llama4VisionMLP: Llama4VisionMLP#
  Llama4VisionMLP.fc1: Llama4VisionMLP#fc1.
  Llama4VisionMLP.fc2: Llama4VisionMLP#fc2.
  Llama4VisionEncoderLayer: Llama4VisionEncoderLayer#
  Llama4VisionEncoderLayer.layer_idx: Llama4VisionEncoderLayer#layer_idx.
  Llama4VisionEncoder: Llama4VisionEncoder#
  Llama4UnfoldConvolution: Llama4UnfoldConvolution#
  Llama4ForConditionalGeneration.vocab_size: Llama4ForConditionalGeneration#vocab_size.
  Llama4VisionMLP2: Llama4VisionMLP2#
  Llama4CausalLMOutputWithPast.loss: Llama4CausalLMOutputWithPast#loss.
  Llama4CausalLMOutputWithPast.logits: Llama4CausalLMOutputWithPast#logits.
  Llama4CausalLMOutputWithPast.hidden_states: Llama4CausalLMOutputWithPast#hidden_states.
  Llama4CausalLMOutputWithPast.attentions: Llama4CausalLMOutputWithPast#attentions.
  Llama4CausalLMOutputWithPast.image_hidden_states: Llama4CausalLMOutputWithPast#image_hidden_states.
  _create_chunked_attention_mask: _create_chunked_attention_mask().
  Llama4TextExperts.reform_param: Llama4TextExperts#reform_param.
  Llama4TextExperts.dtype: Llama4TextExperts#dtype.
  Llama4TextExperts.param_dtype: Llama4TextExperts#param_dtype.
  Llama4TextExperts.precision: Llama4TextExperts#precision.
  Llama4TextExperts.hidden_size: Llama4TextExperts#hidden_size.
  Llama4TextL2Norm.kernel_init: Llama4TextL2Norm#kernel_init.
  Llama4TextL2Norm.__init__: Llama4TextL2Norm#__init__().
  Llama4TextMLP.dtype: Llama4TextMLP#dtype.
  Llama4TextMLP.param_dtype: Llama4TextMLP#param_dtype.
  Llama4TextMoe.dtype: Llama4TextMoe#dtype.
  Llama4TextMoe.param_dtype: Llama4TextMoe#param_dtype.
  Llama4TextMoe.precision: Llama4TextMoe#precision.
  Llama4TextMoe.rngs: Llama4TextMoe#rngs.
  Llama4TextMoe.top_k: Llama4TextMoe#top_k.
  Llama4TextMoe.hidden_dim: Llama4TextMoe#hidden_dim.
  Llama4TextDecoderLayer.config: Llama4TextDecoderLayer#config.
  Llama4TextDecoderLayer.dtype: Llama4TextDecoderLayer#dtype.
  Llama4TextDecoderLayer.param_dtype: Llama4TextDecoderLayer#param_dtype.
  Llama4TextDecoderLayer.precision: Llama4TextDecoderLayer#precision.
  Llama4TextDecoderLayer.use_chunked_attention: Llama4TextDecoderLayer#use_chunked_attention.
  Llama4TextDecoderLayer.layer_idx: Llama4TextDecoderLayer#layer_idx.
  Llama4TextModel.get_encoder: Llama4TextModel#get_encoder().
  Llama4TextModel.get_decoder: Llama4TextModel#get_decoder().
  Llama4TextModel.get_lm_head: Llama4TextModel#get_lm_head().
  Llama4ForCausalLM._model_type: Llama4ForCausalLM#_model_type.
  Llama4ForSequenceClassification._model_type: Llama4ForSequenceClassification#_model_type.
  Llama4MultiModalProjector.__init__: Llama4MultiModalProjector#__init__().
  Llama4MultiModalProjector.config: Llama4MultiModalProjector#config.
  Llama4MultiModalProjector.dtype: Llama4MultiModalProjector#dtype.
  Llama4MultiModalProjector.param_dtype: Llama4MultiModalProjector#param_dtype.
  Llama4MultiModalProjector.precision: Llama4MultiModalProjector#precision.
  Llama4MultiModalProjector.rngs: Llama4MultiModalProjector#rngs.
  Llama4VisionPixelShuffleMLP.__init__: Llama4VisionPixelShuffleMLP#__init__().
  Llama4VisionPixelShuffleMLP.config: Llama4VisionPixelShuffleMLP#config.
  Llama4VisionPixelShuffleMLP.dtype: Llama4VisionPixelShuffleMLP#dtype.
  Llama4VisionPixelShuffleMLP.param_dtype: Llama4VisionPixelShuffleMLP#param_dtype.
  Llama4VisionPixelShuffleMLP.precision: Llama4VisionPixelShuffleMLP#precision.
  Llama4VisionPixelShuffleMLP.rngs: Llama4VisionPixelShuffleMLP#rngs.
  Llama4VisionPixelShuffleMLP.output_dim: Llama4VisionPixelShuffleMLP#output_dim.
  Llama4VisionAttention.layer_idx: Llama4VisionAttention#layer_idx.
  Llama4VisionAttention.dtype: Llama4VisionAttention#dtype.
  Llama4VisionAttention.param_dtype: Llama4VisionAttention#param_dtype.
  Llama4VisionAttention.precision: Llama4VisionAttention#precision.
  Llama4VisionAttention.rngs: Llama4VisionAttention#rngs.
  Llama4VisionAttention.num_key_value_groups: Llama4VisionAttention#num_key_value_groups.
  Llama4VisionMLP2.__init__: Llama4VisionMLP2#__init__().
  Llama4VisionMLP2.config: Llama4VisionMLP2#config.
  Llama4VisionMLP2.dtype: Llama4VisionMLP2#dtype.
  Llama4VisionMLP2.param_dtype: Llama4VisionMLP2#param_dtype.
  Llama4VisionMLP2.precision: Llama4VisionMLP2#precision.
  Llama4VisionMLP2.rngs: Llama4VisionMLP2#rngs.
  Llama4VisionMLP2.hidden_size: Llama4VisionMLP2#hidden_size.
  Llama4VisionMLP.__init__: Llama4VisionMLP#__init__().
  Llama4VisionMLP.config: Llama4VisionMLP#config.
  Llama4VisionMLP.dtype: Llama4VisionMLP#dtype.
  Llama4VisionMLP.param_dtype: Llama4VisionMLP#param_dtype.
  Llama4VisionMLP.precision: Llama4VisionMLP#precision.
  Llama4VisionEncoderLayer.dtype: Llama4VisionEncoderLayer#dtype.
  Llama4VisionEncoderLayer.param_dtype: Llama4VisionEncoderLayer#param_dtype.
  Llama4VisionEncoderLayer.precision: Llama4VisionEncoderLayer#precision.
  Llama4VisionEncoder.dtype: Llama4VisionEncoder#dtype.
  Llama4VisionEncoder.param_dtype: Llama4VisionEncoder#param_dtype.
  Llama4VisionModel.craft_sharding: Llama4VisionModel#craft_sharding().
  Llama4VisionModel.get_encoder: Llama4VisionModel#get_encoder().
  Llama4VisionModel.get_decoder: Llama4VisionModel#get_decoder().
  Llama4VisionModel.get_lm_head: Llama4VisionModel#get_lm_head().
  Llama4ForConditionalGeneration._model_type: Llama4ForConditionalGeneration#_model_type.
  Llama4ForConditionalGeneration._auto_register: Llama4ForConditionalGeneration#_auto_register.
  Llama4ForConditionalGeneration._supports_video: Llama4ForConditionalGeneration#_supports_video.
  Llama4ForConditionalGeneration._uses_mrope: Llama4ForConditionalGeneration#_uses_mrope.
  Llama4ForConditionalGeneration._vision_tower_name: Llama4ForConditionalGeneration#_vision_tower_name.
  Llama4ForConditionalGeneration._projector_name: Llama4ForConditionalGeneration#_projector_name.
  Llama4ForConditionalGeneration._language_model_name: Llama4ForConditionalGeneration#_language_model_name.
  Llama4ForConditionalGeneration.loss_type: Llama4ForConditionalGeneration#loss_type.
  Llama4ForConditionalGeneration.init_cache: Llama4ForConditionalGeneration#init_cache().
  Llama4ForConditionalGeneration.prepare_inputs_for_generation: Llama4ForConditionalGeneration#prepare_inputs_for_generation().
  Llama4ForConditionalGeneration.update_inputs_for_generation: Llama4ForConditionalGeneration#update_inputs_for_generation().
  Llama4ForConditionalGeneration.get_decoder: Llama4ForConditionalGeneration#get_decoder().
  Llama4ForConditionalGeneration.get_lm_head: Llama4ForConditionalGeneration#get_lm_head().
  Llama4ForConditionalGeneration.get_embedding: Llama4ForConditionalGeneration#get_embedding().
  Llama4ForConditionalGeneration.get_language_model: Llama4ForConditionalGeneration#get_language_model().
---
# Module: [`easydel/modules/llama4/modeling_llama4.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py)

## Classes
### `Llama4CausalLMOutputWithPast`  ·  implements/extends ModelOutput
- def: [`easydel/modules/llama4/modeling_llama4.py:72`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L72)
- doc: Base class for Llama4Vision causal language model (or autoregressive) outputs.
- signature: `class Llama4CausalLMOutputWithPast(ModelOutput):`
- members:
  - `attentions` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L110)
  - `hidden_states` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L109)
  - `image_hidden_states` — [`L111`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L111)
  - `logits` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L107)
  - `loss` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L106)
  - `past_key_values` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L108)
- uses (calls/refs, reference-scoped): [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`ModelOutput`](../../infra/modeling_outputs.md#ModelOutput)
- used by: [`ModelOutput`](../../infra/modeling_outputs.md#ModelOutput)

### `Llama4ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/llama4/modeling_llama4.py:1000`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1000)
- doc: Llama4 model with a language modeling head for causal language modeling tasks.
- signature: `class Llama4ForCausalLM(BaseCausalLMModule[Llama4TextModel, Llama4TextConfig]):`
- members:
  - `__init__(self, config: Llama4TextConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1017`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1017) — Initialize Llama4 model for causal language modeling.
- protocol/private: `_config_class`[`L1015`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1015), `_model_type`[`L1014`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1014), `_task_type`[`L1013`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1013)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`Llama4TextConfig`](llama4_configuration.md#Llama4TextConfig), [`Llama4TextModel`](modeling_llama4.md#Llama4TextModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`Llama4ForConditionalGeneration`](modeling_llama4.md#Llama4ForConditionalGeneration), [`__init__`](modeling_llama4.md#Llama4ForConditionalGeneration.__init__)

### `Llama4ForConditionalGeneration`  ·  implements/extends BaseVisionLanguageModule
- def: [`easydel/modules/llama4/modeling_llama4.py:2014`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2014)
- doc: Llama4 Vision model for conditional text generation based on image inputs.
- signature: `class Llama4ForConditionalGeneration(BaseVisionLanguageModule[Llama4ForCausalLM, Llama4Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, pixel_values: Array | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, **lm_kwargs)` — [`L2190`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2190) — Forward pass through the vision-language model.
  - `__init__(self, config: Llama4Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L2052`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2052) — Initialize Llama4 vision-language model for conditional generation.
  - `compute_embedding(self, input_ids: Int[Array, "batch seq_len"] | None, *, image_features: Array | None = None, pixel_values: Array | None = None, **kwargs)` — [`L2128`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2128) — Compute input embeddings with merged image and text features.
  - `get_decoder(self)` — [`L2349`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2349) — Returns the decoder part of the model.
  - `get_embedding(self)` — [`L2357`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2357) — Returns the embedding layer.
  - `get_encoder(self)` — [`L2345`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2345) — Returns the encoder part of the model (vision tower).
  - `get_image_features(self, pixel_values: Array, **kwargs)` — [`L2110`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2110) — Extracts and projects image features from the vision tower.
  - `get_language_model(self)` — [`L2369`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2369) — Returns the language model component.
  - `get_lm_head(self)` — [`L2353`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2353) — Returns the language model head.
  - `get_projector(self)` — [`L2365`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2365) — Returns the multimodal projector component.
  - `get_vision_tower(self)` — [`L2361`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2361) — Returns the vision tower component.
  - `init_cache(self, batch_size, max_length, starts=None, shardings=None, pad_token_id=None)` — [`L2275`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2275) — Initialize the key-value cache for autoregressive generation.
  - `prepare_inputs_for_generation(self, input_ids: Int[Array, "batch seq_len"], max_length: int, pad_token_id: int, starts: int | None = None, pixel_values: Array | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None)` — [`L2301`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2301) — Prepares inputs for text generation, including pixel values if provided.
  - `update_inputs_for_generation(self, model_outputs, model_kwargs)` — [`L2331`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2331) — Updates model inputs for the next step of generation, removing pixel values after the first step.
  - `loss_type` — [`L2050`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2050)
  - `multi_modal_projector` — [`L2100`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2100)
  - `pad_token_id` — [`L2108`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2108)
  - `vision_model` — [`L2093`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2093)
  - `vocab_size` — [`L2107`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2107)
- protocol/private: `_auto_register`[`L2041`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2041), `_config_class`[`L2040`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2040), `_language_model_name`[`L2048`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2048), `_model_type`[`L2039`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2039), `_projector_name`[`L2047`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2047), `_supports_video`[`L2042`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2042), `_task_type`[`L2038`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2038), `_uses_mrope`[`L2043`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2043), `_vision_tower_name`[`L2046`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2046)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseVisionLanguageModule`](../_base/vision_language_module.md#BaseVisionLanguageModule), `pad_token_id`, [`VLMCausalLMOutput`](../../infra/modeling_outputs.md#VLMCausalLMOutput), `output_hidden_states`, [`compute_embedding`](../_base/vision_language_module.md#BaseVisionLanguageModule.compute_embedding), [`IMAGE_TEXT_TO_TEXT`](../../infra/factory.md#TaskType.IMAGE_TEXT_TO_TEXT), [`last_hidden_state`](../../infra/modeling_outputs.md#BaseModelOutput.last_hidden_state), [`__init__`](../_base/vision_language_module.md#BaseVisionLanguageModule.__init__), [`Llama4ForCausalLM`](modeling_llama4.md#Llama4ForCausalLM), [`Llama4VisionModel`](modeling_llama4.md#Llama4VisionModel), [`vision_config`](llama4_configuration.md#Llama4Config.vision_config), [`Llama4Config`](llama4_configuration.md#Llama4Config), [`Llama4MultiModalProjector`](modeling_llama4.md#Llama4MultiModalProjector)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`BaseVisionLanguageModule`](../_base/vision_language_module.md#BaseVisionLanguageModule), [`init_cache`](../../infra/mixins/generation.md#EasyGenerationMixin.init_cache), [`compute_embedding`](../_base/vision_language_module.md#BaseVisionLanguageModule.compute_embedding), [`get_image_features`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_image_features), [`get_language_model`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_language_model), [`get_vision_tower`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_vision_tower), [`get_decoder`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_decoder), [`get_projector`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_projector), [`get_lm_head`](../_base/conditional_generation_module.md#BaseConditionalGenerationModule.get_lm_head), [`update_inputs_for_generation`](../_base/vision_language_module.md#BaseVisionLanguageModule.update_inputs_for_generation), [`prepare_inputs_for_generation`](../_base/vision_language_module.md#BaseVisionLanguageModule.prepare_inputs_for_generation), [`get_encoder`](../_base/vision_language_module.md#BaseVisionLanguageModule.get_encoder)

### `Llama4ForSequenceClassification`  ·  implements/extends BaseSequenceClassificationModule
- def: [`easydel/modules/llama4/modeling_llama4.py:1048`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1048)
- doc: Llama4 model for sequence classification tasks.
- signature: `class Llama4ForSequenceClassification(BaseSequenceClassificationModule[Llama4TextModel, Llama4TextConfig]):`
- members:
  - `__init__(self, config: Llama4TextConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1065`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1065) — Initialize Llama4 model for sequence classification.
- protocol/private: `_config_class`[`L1063`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1063), `_model_type`[`L1062`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1062), `_task_type`[`L1061`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1061)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule), [`SEQUENCE_CLASSIFICATION`](../../infra/factory.md#TaskType.SEQUENCE_CLASSIFICATION), [`__init__`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule.__init__), [`Llama4TextConfig`](llama4_configuration.md#Llama4TextConfig), [`Llama4TextModel`](modeling_llama4.md#Llama4TextModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseSequenceClassificationModule`](../_base/sequence_classification_module.md#BaseSequenceClassificationModule)

### `Llama4MultiModalProjector`  ·  implements/extends Module
- def: [`easydel/modules/llama4/modeling_llama4.py:1096`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1096)
- doc: Multi-modal projector for Llama4 vision-language models.
- signature: `class Llama4MultiModalProjector(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L1138`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1138) — Project vision features to text embedding space.
  - `__init__(self, config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1103`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1103) — Initialize Llama4 multi-modal projector.
  - `config` — [`L1122`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1122)
  - `dtype` — [`L1123`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1123)
  - `linear_1` — [`L1127`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1127)
  - `param_dtype` — [`L1124`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1124)
  - `precision` — [`L1125`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1125)
  - `rngs` — [`L1126`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1126)
- uses (calls/refs, reference-scoped): [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear)
- used by: [`multi_modal_projector`](modeling_llama4.md#Llama4ForConditionalGeneration.multi_modal_projector)

### `Llama4TextAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/llama4/modeling_llama4.py:545`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L545)
- doc: Attention module for the Llama4 text decoder with optional sliding windows.
- signature: `class Llama4TextAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: Llama4TextConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L552`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L552) — Initialize Llama4 text attention layer.
  - `attn_scale` — [`L573`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L573)
  - `attn_temperature_tuning` — [`L575`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L575)
  - `floor_scale` — [`L574`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L574)
  - `qk_norm` — [`L586`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L586)
  - `use_rope` — [`L572`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L572)
- protocol/private: `_apply_rotary`[`L601`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L601), `_cached_position_ids`[`L587`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L587), `_create_attention_performer`[`L589`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L589), `_create_rotary`[`L597`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L597), `_postprocess_qkv`[`L614`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L614)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`Llama4TextConfig`](llama4_configuration.md#Llama4TextConfig), [`_apply_rotary`](../../layers/attention/_unified.md#UnifiedAttention._apply_rotary), [`Llama4TextL2Norm`](modeling_llama4.md#Llama4TextL2Norm), [`apply_complex_rotary`](../../layers/attention/_flexible.md#AttentionModule.apply_complex_rotary), [`attn_scale`](llama4_configuration.md#Llama4TextConfig.attn_scale), [`attn_temperature_tuning`](llama4_configuration.md#Llama4TextConfig.attn_temperature_tuning), [`floor_scale`](llama4_configuration.md#Llama4TextConfig.floor_scale), [`use_qk_norm`](llama4_configuration.md#Llama4TextConfig.use_qk_norm)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`_postprocess_qkv`](../../layers/attention/_unified.md#UnifiedAttention._postprocess_qkv), [`_apply_rotary`](../../layers/attention/_unified.md#UnifiedAttention._apply_rotary), [`self_attn`](modeling_llama4.md#Llama4TextDecoderLayer.self_attn)

### `Llama4TextDecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/llama4/modeling_llama4.py:638`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L638)
- doc: Single Llama4 text decoder block combining attention and MLP.
- signature: `class Llama4TextDecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, output_router_logits: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L715`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L715) — Forward pass through the decoder layer.
  - `__init__(self, config: Llama4TextConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L645`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L645) — Initialize Llama4 text decoder layer.
  - `config` — [`L665`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L665)
  - `dtype` — [`L666`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L666)
  - `feed_forward` — [`L681`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L681)
  - `input_layernorm` — [`L698`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L698)
  - `is_moe_layer` — [`L679`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L679)
  - `layer_idx` — [`L713`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L713)
  - `param_dtype` — [`L667`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L667)
  - `post_attention_layernorm` — [`L705`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L705)
  - `precision` — [`L668`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L668)
  - `self_attn` — [`L670`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L670)
  - `use_chunked_attention` — [`L678`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L678)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`Llama4TextConfig`](llama4_configuration.md#Llama4TextConfig), [`Llama4TextAttention`](modeling_llama4.md#Llama4TextAttention), [`Llama4TextMoe`](modeling_llama4.md#Llama4TextMoe), [`hidden_size`](llama4_configuration.md#Llama4TextConfig.hidden_size), [`Llama4TextMLP`](modeling_llama4.md#Llama4TextMLP), [`rms_norm_eps`](llama4_configuration.md#Llama4TextConfig.rms_norm_eps), [`intermediate_size_mlp`](llama4_configuration.md#Llama4TextConfig.intermediate_size_mlp), [`moe_layers`](llama4_configuration.md#Llama4TextConfig.moe_layers)
- used by: [`embed_tokens`](modeling_llama4.md#Llama4TextModel.embed_tokens)

### `Llama4TextExperts`  ·  implements/extends Module
- def: [`easydel/modules/llama4/modeling_llama4.py:148`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L148)
- doc: Mixture of Experts module for Llama4 text models.
- signature: `class Llama4TextExperts(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], group_sizes: Array, sorted_experts: Array | None = None)` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L238) — Forward pass through MoE experts.
  - `__init__(self, config: Llama4Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L172) — Initialize Llama4 text experts module.
  - `act_fn` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L236)
  - `config` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L191)
  - `down_proj` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L224)
  - `dtype` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L192)
  - `expert_dim` — [`L198`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L198)
  - `gate_proj` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L200)
  - `hidden_size` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L197)
  - `intermediate_size` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L196)
  - `num_experts` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L195)
  - `param_dtype` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L193)
  - `precision` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L194)
  - `reform_param` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L155)
  - `up_proj` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L212)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`use_expert_tensor_mode`](../../infra/base_config.md#EasyDeLBaseConfig.use_expert_tensor_mode), [`ColumnParallelMoELinear`](../../layers/linears/_linear_moe.md#ColumnParallelMoELinear), [`RowParallelMoELinear`](../../layers/linears/_linear_moe.md#RowParallelMoELinear), [`num_local_experts`](../../infra/base_config.md#EasyDeLBaseConfig.num_local_experts), [`Llama4Config`](llama4_configuration.md#Llama4Config)
- used by: [`__call__`](modeling_llama4.md#Llama4TextMoe.__call__), [`experts`](modeling_llama4.md#Llama4TextMoe.experts), [`ffn_activation`](modeling_llama4.md#Llama4TextMoe.ffn_activation)

### `Llama4TextL2Norm`  ·  implements/extends Module
- def: [`easydel/modules/llama4/modeling_llama4.py:259`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L259)
- doc: L2 normalization layer for Llama4 text models.
- signature: `class Llama4TextL2Norm(nn.Module):`
- members:
  - `__call__(self, x: jnp.ndarray)` — [`L280`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L280) — Apply L2 normalization.
  - `__init__(self, eps: float = 0.000001)` — [`L268`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L268) — Initialize L2 normalization layer.
  - `eps` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L274)
  - `kernel_init` — [`L266`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L266)
- protocol/private: `_norm`[`L276`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L276)
- used by: [`qk_norm`](modeling_llama4.md#Llama4TextAttention.qk_norm)

### `Llama4TextMLP`  ·  implements/extends Module
- def: [`easydel/modules/llama4/modeling_llama4.py:292`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L292)
- doc: Multi-Layer Perceptron for Llama4 text models.
- signature: `class Llama4TextMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L350`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L350) — Apply SwiGLU feedforward transformation.
  - `__init__(self, config: Llama4Config, intermediate_size=None, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L299`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L299) — Initialize Llama4 text MLP block.
  - `activation_fn` — [`L348`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L348)
  - `config` — [`L321`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L321)
  - `down_proj` — [`L346`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L346)
  - `dtype` — [`L322`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L322)
  - `gate_proj` — [`L345`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L345)
  - `param_dtype` — [`L323`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L323)
  - `precision` — [`L324`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L324)
  - `up_proj` — [`L347`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L347)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`Llama4Config`](llama4_configuration.md#Llama4Config)
- used by: [`feed_forward`](modeling_llama4.md#Llama4TextDecoderLayer.feed_forward), [`shared_expert`](modeling_llama4.md#Llama4TextMoe.shared_expert)

### `Llama4TextModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/llama4/modeling_llama4.py:777`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L777)
- doc: Decoder-only Llama4 text model built from embeddings and decoder blocks.
- signature: `class Llama4TextModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L851`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L851) — Forward pass through the Llama4 text base model.
  - `__init__(self, config: Llama4TextConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L790`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L790) — Initialize Llama4 text base model.
  - `get_decoder(self)` — [`L979`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L979) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L992`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L992) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L972`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L972) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L985`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L985) — Returns the language model head of the module.
  - `embed_tokens` — [`L816`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L816)
  - `layers` — [`L830`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L830)
  - `norm` — [`L843`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L843)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`Llama4TextConfig`](llama4_configuration.md#Llama4TextConfig), [`compute_complex_rotary`](../../infra/base_module.md#EasyDeLBaseModule.compute_complex_rotary), [`Llama4TextDecoderLayer`](modeling_llama4.md#Llama4TextDecoderLayer)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`Llama4ForCausalLM`](modeling_llama4.md#Llama4ForCausalLM), [`Llama4ForSequenceClassification`](modeling_llama4.md#Llama4ForSequenceClassification), [`__init__`](modeling_llama4.md#Llama4ForCausalLM.__init__), [`__init__`](modeling_llama4.md#Llama4ForSequenceClassification.__init__)

### `Llama4TextMoe`  ·  implements/extends BaseMoeModule
- def: [`easydel/modules/llama4/modeling_llama4.py:375`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L375)
- doc: Mixture of Experts layer for Llama4 text models.
- signature: `class Llama4TextMoe(BaseMoeModule):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], training: bool = False, layer_idx: int | None = None)` — [`L500`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L500) — Forward pass through the MoE layer.
  - `__init__(self, config: Llama4Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L382`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L382) — Initialize Llama4 Mixture of Experts layer.
  - `_passthrough_weights(weights: jax.Array)` — [`L472`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L472) — Pass through weights unchanged (avoid default sum normalization).
  - `_scale_inputs(inputs: jax.Array, weights: jax.Array)` — [`L460`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L460) — Scale replicated inputs by their corresponding weights (input scaling).
  - `_sigmoid_topk_weights(logits: jax.Array)` — [`L451`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L451) — Apply sigmoid to logits, zero out non-top-k.
  - `_unity_output_weights(weights: jax.Array)` — [`L480`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L480) — Replace output weights with 1.0 since scaling is done on inputs.
  - `ffn_activation(gate, up)` — [`L526`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L526)
  - `dtype` — [`L412`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L412)
  - `experts` — [`L420`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L420)
  - `hidden_dim` — [`L417`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L417)
  - `num_experts` — [`L418`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L418)
  - `param_dtype` — [`L413`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L413)
  - `precision` — [`L414`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L414)
  - `rngs` — [`L415`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L415)
  - `router` — [`L427`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L427)
  - `shared_expert` — [`L437`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L437)
  - `top_k` — [`L416`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L416)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`kernel`](../../layers/linears/_linear_moe.md#ParallelMoELinear.kernel), [`MoeRoutingStrategy`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy), [`moe_call`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_call), [`MoeLoadBalancingStrategy`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy), [`__init__`](../../layers/moe/_moe_module.md#BaseMoeModule.__init__), [`moe_hooks`](../../layers/moe/_moe_module.md#BaseMoeModule.moe_hooks), [`TOP_K`](../../layers/moe/_communication_utils.md#MoeRoutingStrategy.TOP_K), [`STANDARD`](../../layers/moe/_communication_utils.md#MoeLoadBalancingStrategy.STANDARD), [`num_local_experts`](../../infra/base_config.md#EasyDeLBaseConfig.num_local_experts), [`num_experts_per_tok`](../../layers/moe/_moe_module.md#BaseMoeModule.num_experts_per_tok), [`Llama4Config`](llama4_configuration.md#Llama4Config), [`down_proj`](modeling_llama4.md#Llama4TextExperts.down_proj), [`gate_proj`](modeling_llama4.md#Llama4TextExperts.gate_proj), [`up_proj`](modeling_llama4.md#Llama4TextExperts.up_proj), [`replace`](../../layers/moe/_communication_utils.md#MoeFusedHooks.replace), [`act_fn`](modeling_llama4.md#Llama4TextExperts.act_fn), [`Llama4TextMLP`](modeling_llama4.md#Llama4TextMLP), [`Llama4TextExperts`](modeling_llama4.md#Llama4TextExperts)
- used by: [`BaseMoeModule`](../../layers/moe/_moe_module.md#BaseMoeModule), [`feed_forward`](modeling_llama4.md#Llama4TextDecoderLayer.feed_forward)

### `Llama4UnfoldConvolution`  ·  implements/extends Module
- def: [`easydel/modules/llama4/modeling_llama4.py:1722`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1722)
- doc: Unfold convolution module for Llama4 vision models.
- signature: `class Llama4UnfoldConvolution(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L1772`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1772) — Extract and embed image patches.
  - `__init__(self, config: Llama4VisionConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1729`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1729) — Initialize Llama4 unfold convolution layer.
  - `hidden_size` — [`L1758`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1758)
  - `kernel_size` — [`L1749`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1749)
  - `linear` — [`L1762`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1762)
  - `num_channels` — [`L1757`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1757)
  - `stride` — [`L1753`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1753)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`Llama4VisionConfig`](llama4_configuration.md#Llama4VisionConfig), [`hidden_size`](llama4_configuration.md#Llama4VisionConfig.hidden_size), [`patch_size`](llama4_configuration.md#Llama4VisionConfig.patch_size), [`num_channels`](llama4_configuration.md#Llama4VisionConfig.num_channels)
- used by: [`patch_embedding`](modeling_llama4.md#Llama4VisionModel.patch_embedding)

### `Llama4VisionAttention`  ·  implements/extends AttentionModule
- def: [`easydel/modules/llama4/modeling_llama4.py:1268`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1268)
- doc: Attention module for the Llama4 vision transformer.
- signature: `class Llama4VisionAttention(AttentionModule):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], frequencies: Float[Array, "seq_len head_dim"] | None = None, output_attentions: bool = False)` — [`L1330`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1330) — Forward pass through vision attention layer.
  - `__init__(self, config: Llama4VisionConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L1275`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1275) — Initialize Llama4 vision attention layer.
  - `attention_dropout` — [`L1306`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1306)
  - `attention_performer` — [`L1322`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1322)
  - `dtype` — [`L1297`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1297)
  - `embed_dim` — [`L1302`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1302)
  - `head_dim` — [`L1304`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1304)
  - `k_proj` — [`L1318`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1318)
  - `layer_idx` — [`L1296`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1296)
  - `num_heads` — [`L1303`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1303)
  - `num_key_value_groups` — [`L1305`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1305)
  - `o_proj` — [`L1320`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1320)
  - `param_dtype` — [`L1298`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1298)
  - `precision` — [`L1299`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1299)
  - `q_proj` — [`L1317`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1317)
  - `rngs` — [`L1300`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1300)
  - `v_proj` — [`L1319`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1319)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`forward`](../../layers/attention/_flexible.md#FlexibleAttentionModule.forward), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`AttentionModule`](../../layers/attention/_flexible.md#AttentionModule), [`shard_attention_prod`](../../layers/attention/_flexible.md#AttentionModule.shard_attention_prod), [`apply_qkv_shardings`](../../layers/attention/_flexible.md#AttentionModule.apply_qkv_shardings), [`attention_weights`](../../operations/_attention_outputs.md#AttentionOutput.attention_weights), [`Llama4VisionConfig`](llama4_configuration.md#Llama4VisionConfig), [`__init__`](../../layers/attention/_flexible.md#AttentionModule.__init__), [`hidden_size`](llama4_configuration.md#Llama4VisionConfig.hidden_size), [`vision_apply_rotary_emb`](modeling_llama4.md#vision_apply_rotary_emb), [`num_attention_heads`](llama4_configuration.md#Llama4VisionConfig.num_attention_heads), [`attention_dropout`](llama4_configuration.md#Llama4VisionConfig.attention_dropout), [`initializer_range`](llama4_configuration.md#Llama4VisionConfig.initializer_range)
- used by: [`AttentionModule`](../../layers/attention/_flexible.md#AttentionModule), [`self_attn`](modeling_llama4.md#Llama4VisionEncoderLayer.self_attn)

### `Llama4VisionEncoder`  ·  implements/extends Module
- def: [`easydel/modules/llama4/modeling_llama4.py:1618`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1618)
- doc: Vision encoder stack for Llama4 models.
- signature: `class Llama4VisionEncoder(nn.Module):`
- members:
  - `__call__(self, hidden_states: jax.Array, frequencies: jax.Array, attention_mask: jax.Array | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L1668`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1668) — Forward pass through all vision encoder layers.
  - `__init__(self, config: Llama4VisionConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1625`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1625) — Initialize Llama4 vision encoder.
  - `config` — [`L1643`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1643)
  - `dtype` — [`L1644`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1644)
  - `layers` — [`L1654`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1654)
  - `param_dtype` — [`L1645`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1645)
  - `precision` — [`L1646`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1646)
- uses (calls/refs, reference-scoped): [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), `output_hidden_states`, [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`Llama4VisionConfig`](llama4_configuration.md#Llama4VisionConfig), [`attention_weight`](../../infra/modeling_outputs.md#EncoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#EncoderLayerOutput.hidden_states), [`Llama4VisionEncoderLayer`](modeling_llama4.md#Llama4VisionEncoderLayer), [`num_hidden_layers`](llama4_configuration.md#Llama4VisionConfig.num_hidden_layers)
- used by: [`model`](modeling_llama4.md#Llama4VisionModel.model)

### `Llama4VisionEncoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/llama4/modeling_llama4.py:1504`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1504)
- doc: Single encoder layer for Llama4 vision models.
- signature: `class Llama4VisionEncoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L1570`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1570) — Forward pass through the vision encoder layer.
  - `__init__(self, config: Llama4VisionConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L1511`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1511) — Initialize Llama4 vision encoder layer.
  - `config` — [`L1531`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1531)
  - `dtype` — [`L1533`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1533)
  - `input_layernorm` — [`L1553`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1553)
  - `layer_idx` — [`L1532`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1532)
  - `mlp` — [`L1545`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1545)
  - `param_dtype` — [`L1534`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1534)
  - `post_attention_layernorm` — [`L1560`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1560)
  - `precision` — [`L1535`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1535)
  - `self_attn` — [`L1537`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1537)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`Llama4VisionConfig`](llama4_configuration.md#Llama4VisionConfig), [`EncoderLayerOutput`](../../infra/modeling_outputs.md#EncoderLayerOutput), [`hidden_size`](llama4_configuration.md#Llama4VisionConfig.hidden_size), [`Llama4VisionAttention`](modeling_llama4.md#Llama4VisionAttention), [`Llama4VisionMLP`](modeling_llama4.md#Llama4VisionMLP)
- used by: [`precision`](modeling_llama4.md#Llama4VisionEncoder.precision)

### `Llama4VisionMLP`  ·  implements/extends Module
- def: [`easydel/modules/llama4/modeling_llama4.py:1443`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1443)
- doc: MLP module for Llama4 vision transformer.
- signature: `class Llama4VisionMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L1489`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1489) — Apply feedforward transformation with GELU activation.
  - `__init__(self, config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1450`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1450) — Initialize Llama4 vision MLP block.
  - `activation_fn` — [`L1487`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1487)
  - `config` — [`L1469`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1469)
  - `dtype` — [`L1470`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1470)
  - `fc1` — [`L1485`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1485)
  - `fc2` — [`L1486`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1486)
  - `param_dtype` — [`L1471`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1471)
  - `precision` — [`L1472`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1472)
  - `rngs` — [`L1473`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1473)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN)
- used by: [`mlp`](modeling_llama4.md#Llama4VisionEncoderLayer.mlp)

### `Llama4VisionMLP2`
- def: [`easydel/modules/llama4/modeling_llama4.py:1384`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1384)
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L1430`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1430) — Apply two-layer feedforward transformation with GELU activation.
  - `__init__(self, config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1391`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1391) — Initialize Llama4 vision two-layer MLP.
  - `activation_fn` — [`L1415`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1415)
  - `config` — [`L1410`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1410)
  - `dtype` — [`L1411`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1411)
  - `fc1` — [`L1427`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1427)
  - `fc2` — [`L1428`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1428)
  - `hidden_size` — [`L1425`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1425)
  - `intermediate_size` — [`L1426`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1426)
  - `param_dtype` — [`L1412`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1412)
  - `precision` — [`L1413`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1413)
  - `rngs` — [`L1414`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1414)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN)
- used by: [`mlp`](modeling_llama4.md#Llama4VisionPixelShuffleMLP.mlp)

### `Llama4VisionModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/llama4/modeling_llama4.py:1800`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1800)
- doc: Vision transformer for Llama4 including patchify stem, transformer blocks, and final norm.
- signature: `class Llama4VisionModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, pixel_values: jax.Array, attention_mask: jax.Array | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L1906`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1906) — Forward pass through the Llama4 vision model.
  - `__init__(self, config: Llama4VisionConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1813`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1813) — Initialize Llama4 vision model.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L1899`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1899) — Return sharding specs for vision-only parameters.
  - `get_decoder(self)` — [`L1992`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1992) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L2006`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L2006) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L1985`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1985) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L1999`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1999) — Returns the language model head of the module.
  - `class_embedding` — [`L1853`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1853)
  - `hidden_size` — [`L1840`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1840)
  - `image_size` — [`L1838`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1838)
  - `layernorm_post` — [`L1874`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1874)
  - `layernorm_pre` — [`L1867`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1867)
  - `model` — [`L1883`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1883)
  - `num_channels` — [`L1841`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1841)
  - `num_patches` — [`L1843`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1843)
  - `patch_embedding` — [`L1846`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1846)
  - `patch_size` — [`L1839`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1839)
  - `positional_embedding_vlm` — [`L1860`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1860)
  - `scale` — [`L1844`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1844)
  - `vision_adapter` — [`L1890`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1890)
  - `vision_idx` — [`L1897`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1897)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`ArrayParam`](../../infra/utils.md#ArrayParam), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`bound`](../../infra/utils.md#ArrayParam.bound), `output_hidden_states`, [`last_hidden_state`](../../infra/modeling_outputs.md#BaseModelOutput.last_hidden_state), [`attentions`](../../infra/modeling_outputs.md#BaseModelOutput.attentions), [`hidden_states`](../../infra/modeling_outputs.md#BaseModelOutput.hidden_states), [`Llama4VisionConfig`](llama4_configuration.md#Llama4VisionConfig), [`BASE_VISION`](../../infra/factory.md#TaskType.BASE_VISION), [`hidden_size`](llama4_configuration.md#Llama4VisionConfig.hidden_size), [`patch_size`](llama4_configuration.md#Llama4VisionConfig.patch_size), [`num_channels`](llama4_configuration.md#Llama4VisionConfig.num_channels), [`Llama4UnfoldConvolution`](modeling_llama4.md#Llama4UnfoldConvolution), [`Llama4VisionEncoder`](modeling_llama4.md#Llama4VisionEncoder), [`Llama4VisionPixelShuffleMLP`](modeling_llama4.md#Llama4VisionPixelShuffleMLP), [`_vision_freqs`](modeling_llama4.md#_vision_freqs), [`image_size`](llama4_configuration.md#Llama4VisionConfig.image_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`vision_model`](modeling_llama4.md#Llama4ForConditionalGeneration.vision_model)

### `Llama4VisionPixelShuffleMLP`  ·  implements/extends Module
- def: [`easydel/modules/llama4/modeling_llama4.py:1177`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1177)
- doc: Pixel shuffle MLP for Llama4 vision models.
- signature: `class Llama4VisionPixelShuffleMLP(nn.Module):`
- members:
  - `__call__(self, encoded_patches: Array)` — [`L1221`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1221) — Apply pixel shuffle and MLP transformation to vision features.
  - `__init__(self, config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1184`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1184) — Initialize Llama4 vision pixel shuffle MLP.
  - `config` — [`L1203`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1203)
  - `dtype` — [`L1204`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1204)
  - `inner_dim` — [`L1210`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1210)
  - `mlp` — [`L1213`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1213)
  - `output_dim` — [`L1211`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1211)
  - `param_dtype` — [`L1205`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1205)
  - `pixel_shuffle_ratio` — [`L1209`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1209)
  - `precision` — [`L1206`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1206)
  - `rngs` — [`L1207`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1207)
- uses (calls/refs, reference-scoped): [`Llama4VisionMLP2`](modeling_llama4.md#Llama4VisionMLP2), [`pixel_shuffle`](modeling_llama4.md#pixel_shuffle)
- used by: [`vision_adapter`](modeling_llama4.md#Llama4VisionModel.vision_adapter)

## Functions
- `_create_chunked_attention_mask(attention_chunk_size: int, start: int, end: int)` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L134) — Create a chunked causal attention mask for sliding window attention.
- `_vision_freqs(idx, hidden_size, num_attention_heads, rope_theta)` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L115) — Compute rotary frequencies for the vision transformer grid.
- `pixel_shuffle(input_tensor, shuffle_ratio)` — [`L1150`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1150) — Rearrange flattened vision tokens to a denser spatial grid.
- `reshape_for_broadcast(frequencies: jax.Array, query: jax.Array)` — [`L1234`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1234) — Reshape rotary frequencies so they broadcast over the complex query tensor.
- `vision_apply_rotary_emb(query: jax.Array, key: jax.Array, frequencies: jax.Array)` — [`L1243`](../../../../../../../raw/code/EasyDeL/easydel/modules/llama4/modeling_llama4.py#L1243) — Apply rotary position embeddings to complex-valued vision queries and keys.

