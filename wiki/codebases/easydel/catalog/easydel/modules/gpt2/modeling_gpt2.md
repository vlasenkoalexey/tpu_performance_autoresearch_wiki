---
title: 'Module: easydel/modules/gpt2/modeling_gpt2.py'
type: catalog
provenance: extracted
module: easydel/modules/gpt2/modeling_gpt2.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gpt2.modeling_gpt2`/
symbols:
  GPT2Block.__call__: GPT2Block#__call__().
  GPT2Attention.__call__: GPT2Attention#__call__().
  GPT2Model.__call__: GPT2Model#__call__().
  GPT2LMHeadModel: GPT2LMHeadModel#
  GPT2Model: GPT2Model#
  GPT2MLP.__call__: GPT2MLP#__call__().
  GPT2Model.wpe: GPT2Model#wpe.
  GPT2Model.dropout: GPT2Model#dropout.
  GPT2Model.wte: GPT2Model#wte.
  Conv1D.__call__: Conv1D#__call__().
  GPT2Attention.q_attn: GPT2Attention#q_attn.
  GPT2Attention.resid_dropout: GPT2Attention#resid_dropout.
  GPT2Attention._create_attention_performer: GPT2Attention#_create_attention_performer().
  GPT2Attention.embed_dim: GPT2Attention#embed_dim.
  GPT2Block.ln_2: GPT2Block#ln_2.
  GPT2Model.ln_f: GPT2Model#ln_f.
  GPT2Attention.c_attn: GPT2Attention#c_attn.
  GPT2Attention._split_heads: GPT2Attention#_split_heads().
  GPT2LMHeadModel.__init__: GPT2LMHeadModel#__init__().
  Conv1D.bias: Conv1D#bias.
  GPT2Attention.head_dim: GPT2Attention#head_dim.
  Conv1D: Conv1D#
  Conv1D.kernel: Conv1D#kernel.
  GPT2Attention.c_proj: GPT2Attention#c_proj.
  GPT2MLP.act: GPT2MLP#act.
  GPT2Block.config: GPT2Block#config.
  GPT2Block.ln_1: GPT2Block#ln_1.
  GPT2Block.ln_cross_attn: GPT2Block#ln_cross_attn.
  Conv1D.craft_sharding: Conv1D#craft_sharding().
  GPT2Attention.define_network: GPT2Attention#define_network().
  GPT2Block.precision: GPT2Block#precision.
  GPT2Model.__init__: GPT2Model#__init__().
  GPT2LMHeadModel._task_type: GPT2LMHeadModel#_task_type.
  GPT2LMHeadModel.get_embedding: GPT2LMHeadModel#get_embedding().
  GPT2Attention: GPT2Attention#
  GPT2Attention.num_heads: GPT2Attention#num_heads.
  GPT2Block.mlp: GPT2Block#mlp.
  GPT2Model.embed_dim: GPT2Model#embed_dim.
  GPT2Model.h: GPT2Model#h.
  GPT2Attention._merge_heads: GPT2Attention#_merge_heads().
  GPT2MLP.c_fc: GPT2MLP#c_fc.
  GPT2MLP.c_proj: GPT2MLP#c_proj.
  GPT2MLP.dropout: GPT2MLP#dropout.
  GPT2Block.attn: GPT2Block#attn.
  GPT2Block.crossattention: GPT2Block#crossattention.
  Conv1D.dtype: Conv1D#dtype.
  GPT2Attention.__init__: GPT2Attention#__init__().
  GPT2MLP.__init__: GPT2MLP#__init__().
  GPT2Block.__init__: GPT2Block#__init__().
  GPT2Model.get_embedding: GPT2Model#get_embedding().
  GPT2LMHeadModel._config_class: GPT2LMHeadModel#_config_class.
  Conv1D.dot_general: Conv1D#dot_general.
  Conv1D.sharding_axis: Conv1D#sharding_axis.
  GPT2Attention.causal: GPT2Attention#causal.
  GPT2MLP.config: GPT2MLP#config.
  Conv1D.precision: Conv1D#precision.
  GPT2Attention.is_cross_attention: GPT2Attention#is_cross_attention.
  GPT2MLP: GPT2MLP#
  GPT2Block: GPT2Block#
  Conv1D.__init__: Conv1D#__init__().
  Conv1D.use_bias: Conv1D#use_bias.
  Conv1D.param_dtype: Conv1D#param_dtype.
  GPT2Attention.precision: GPT2Attention#precision.
  GPT2Attention.dtype: GPT2Attention#dtype.
  GPT2MLP.precision: GPT2MLP#precision.
  GPT2MLP.dtype: GPT2MLP#dtype.
  GPT2Block.dtype: GPT2Block#dtype.
  GPT2Block.param_dtype: GPT2Block#param_dtype.
  GPT2Model.get_encoder: GPT2Model#get_encoder().
  GPT2Model.get_decoder: GPT2Model#get_decoder().
  GPT2Model.get_lm_head: GPT2Model#get_lm_head().
  GPT2LMHeadModel._model_type: GPT2LMHeadModel#_model_type.
  GPT2LMHeadModel.loss_type: GPT2LMHeadModel#loss_type.
---
# Module: [`easydel/modules/gpt2/modeling_gpt2.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py)

## Classes
### `Conv1D`  ·  implements/extends Module
- def: [`easydel/modules/gpt2/modeling_gpt2.py:53`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L53)
- doc: Custom 1D Convolution layer used in GPT-2.
- signature: `class Conv1D(nn.Module):`
- members:
  - `__call__(self, inputs)` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L123) — Forward pass of the Conv1D layer.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L111`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L111)
  - `bias` — [`L93`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L93)
  - `dot_general` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L108)
  - `dtype` — [`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L105)
  - `kernel` — [`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L85)
  - `param_dtype` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L106)
  - `precision` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L107)
  - `sharding_axis` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L109)
  - `use_bias` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L104)
- protocol/private: `__init__`[`L72`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L72)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound)
- used by: [`q_attn`](modeling_gpt2.md#GPT2Attention.q_attn), [`c_attn`](modeling_gpt2.md#GPT2Attention.c_attn), [`c_proj`](modeling_gpt2.md#GPT2Attention.c_proj), [`c_fc`](modeling_gpt2.md#GPT2MLP.c_fc), [`c_proj`](modeling_gpt2.md#GPT2MLP.c_proj)

### `GPT2Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/gpt2/modeling_gpt2.py:151`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L151)
- doc: GPT-2 Attention module.
- signature: `class GPT2Attention(UnifiedAttention):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None, key_value_states: Float[Array, "batch seq_len hidden_dim"] | None = None)` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L274) — Forward pass of the GPT2Attention module.
  - `_create_attention_performer(self, config: GPT2Config, rngs: nn.Rngs)` — [`L250`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L250) — Use GPT-2 specific attention dropout setting.
  - `_merge_heads(self, hidden_states)` — [`L262`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L262) — Merges the attention heads into a single hidden state tensor.
  - `define_network(self, config: GPT2Config, dtype: jnp.dtype, param_dtype: jnp.dtype, precision: jax.lax.PrecisionLike, rngs: nn.Rngs)` — [`L198`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L198) — Create GPT-2 specific projection layers.
  - `c_attn` — [`L208`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L208)
  - `c_proj` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L238)
  - `causal` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L195)
  - `dtype` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L194)
  - `embed_dim` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L180)
  - `head_dim` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L196)
  - `is_cross_attention` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L179)
  - `num_heads` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L181)
  - `precision` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L193)
  - `q_attn` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L217)
  - `resid_dropout` — [`L247`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L247)
- protocol/private: `__init__`[`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L167), `_split_heads`[`L259`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L259)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`forward`](../../layers/attention/_flexible.md#FlexibleAttentionModule.forward), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`concatenate`](../../layers/attention/_flexible.md#AttentionModule.concatenate), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`attention_performer`](../../layers/attention/_unified.md#UnifiedAttention.attention_performer), [`shard_attention_prod`](../../layers/attention/_flexible.md#AttentionModule.shard_attention_prod), [`attention_weights`](../../operations/_attention_outputs.md#AttentionOutput.attention_weights), [`GPT2Config`](gpt2_configuration.md#GPT2Config), [`Conv1D`](modeling_gpt2.md#Conv1D), [`resid_pdrop`](gpt2_configuration.md#GPT2Config.resid_pdrop), [`attn_pdrop`](gpt2_configuration.md#GPT2Config.attn_pdrop)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`define_network`](../../layers/attention/_unified.md#UnifiedAttention.define_network), [`_merge_heads`](../../layers/attention/_unified.md#UnifiedAttention._merge_heads), [`attn`](modeling_gpt2.md#GPT2Block.attn), [`crossattention`](modeling_gpt2.md#GPT2Block.crossattention)

### `GPT2Block`  ·  implements/extends Module
- def: [`easydel/modules/gpt2/modeling_gpt2.py:440`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L440)
- doc: GPT-2 Transformer block.
- signature: `class GPT2Block(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None, encoder_hidden_states: Float[Array, "batch seq_len hidden_dim"] | None = None, encoder_mask_info: MaskInfo | None = None)` — [`L523`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L523) — Forward pass of the GPT2Block module.
  - `attn` — [`L481`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L481)
  - `config` — [`L466`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L466)
  - `crossattention` — [`L498`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L498)
  - `dtype` — [`L467`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L467)
  - `ln_1` — [`L473`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L473)
  - `ln_2` — [`L489`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L489)
  - `ln_cross_attn` — [`L506`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L506)
  - `mlp` — [`L514`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L514)
  - `param_dtype` — [`L468`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L468)
  - `precision` — [`L469`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L469)
- protocol/private: `__init__`[`L455`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L455)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`GPT2Config`](gpt2_configuration.md#GPT2Config), [`GPT2Attention`](modeling_gpt2.md#GPT2Attention), [`layer_norm_epsilon`](gpt2_configuration.md#GPT2Config.layer_norm_epsilon), `add_cross_attention`, [`n_inner`](gpt2_configuration.md#GPT2Config.n_inner), [`GPT2MLP`](modeling_gpt2.md#GPT2MLP)
- used by: [`dropout`](modeling_gpt2.md#GPT2Model.dropout)

### `GPT2LMHeadModel`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/gpt2/modeling_gpt2.py:863`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L863)
- doc: GPT-2 model with a language modeling head.
- signature: `class GPT2LMHeadModel(BaseCausalLMModule[GPT2Model, GPT2Config]):`
- members:
  - `get_embedding(self)` — [`L904`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L904) — Returns the embedding layer of the module.
  - `loss_type` — [`L882`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L882)
- protocol/private: `__init__`[`L884`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L884), `_config_class`[`L880`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L880), `_model_type`[`L879`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L879), `_task_type`[`L878`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L878)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`base_model`](../_base/_base_task_module.md#BaseTaskModule.base_model), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`GPT2Config`](gpt2_configuration.md#GPT2Config), [`GPT2Model`](modeling_gpt2.md#GPT2Model), [`wte`](modeling_gpt2.md#GPT2Model.wte)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding)

### `GPT2MLP`  ·  implements/extends Module
- def: [`easydel/modules/gpt2/modeling_gpt2.py:360`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L360)
- doc: GPT-2 MLP module.
- signature: `class GPT2MLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L414`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L414) — Forward pass of the GPT2MLP module.
  - `act` — [`L408`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L408)
  - `c_fc` — [`L390`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L390)
  - `c_proj` — [`L399`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L399)
  - `config` — [`L386`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L386)
  - `dropout` — [`L409`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L409)
  - `dtype` — [`L388`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L388)
  - `precision` — [`L387`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L387)
- protocol/private: `__init__`[`L375`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L375)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`GPT2Config`](gpt2_configuration.md#GPT2Config), [`Conv1D`](modeling_gpt2.md#Conv1D), [`resid_pdrop`](gpt2_configuration.md#GPT2Config.resid_pdrop), [`activation_function`](gpt2_configuration.md#GPT2Config.activation_function)
- used by: [`mlp`](modeling_gpt2.md#GPT2Block.mlp)

### `GPT2Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/gpt2/modeling_gpt2.py:621`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L621)
- doc: GPT-2 model implementation.
- signature: `class GPT2Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, encoder_hidden_states: Float[Array, "batch seq_len hidden_dim"] | None = None, encoder_attention_mask: Bool[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, output_hidden_states: bool = False)` — [`L699`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L699) — Performs forward pass through the GPT-2 transformer model.
  - `get_decoder(self)` — [`L842`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L842) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L855`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L855) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L835`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L835) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L848`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L848) — Returns the language model head of the module.
  - `dropout` — [`L671`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L671)
  - `embed_dim` — [`L652`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L652)
  - `h` — [`L678`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L678)
  - `ln_f` — [`L691`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L691)
  - `wpe` — [`L662`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L662)
  - `wte` — [`L654`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L654)
- protocol/private: `__init__`[`L636`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/modeling_gpt2.py#L636)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`dtype`](../../infra/base_module.md#EasyDeLBaseModule.dtype), [`GPT2Config`](gpt2_configuration.md#GPT2Config), [`BaseModelOutputWithPastAndCrossAttentions`](../../infra/modeling_outputs.md#BaseModelOutputWithPastAndCrossAttentions), [`GPT2Block`](modeling_gpt2.md#GPT2Block), [`gradient_checkpointing`](gpt2_configuration.md#GPT2Config.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`GPT2LMHeadModel`](modeling_gpt2.md#GPT2LMHeadModel), [`__init__`](modeling_gpt2.md#GPT2LMHeadModel.__init__), [`get_embedding`](modeling_gpt2.md#GPT2LMHeadModel.get_embedding)

