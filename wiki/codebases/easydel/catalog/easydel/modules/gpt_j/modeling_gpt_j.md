---
title: 'Module: easydel/modules/gpt_j/modeling_gpt_j.py'
type: catalog
provenance: extracted
module: easydel/modules/gpt_j/modeling_gpt_j.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gpt_j.modeling_gpt_j`/
symbols:
  GPTJModel.__call__: GPTJModel#__call__().
  GPTJBlock.__call__: GPTJBlock#__call__().
  GPTJForCausalLM: GPTJForCausalLM#
  GPTJModel: GPTJModel#
  GPTJMLP.__call__: GPTJMLP#__call__().
  GPTJModel.dropout: GPTJModel#dropout.
  GPTJModel.wte: GPTJModel#wte.
  GPTJAttention._create_rotary: GPTJAttention#_create_rotary().
  GPTJAttention._create_attention_performer: GPTJAttention#_create_attention_performer().
  GPTJAttention.out_proj: GPTJAttention#out_proj.
  GPTJBlock.ln_1: GPTJBlock#ln_1.
  GPTJAttention._split_heads: GPTJAttention#_split_heads().
  GPTJAttention._create_k_proj: GPTJAttention#_create_k_proj().
  GPTJAttention._create_v_proj: GPTJAttention#_create_v_proj().
  GPTJBlock.config: GPTJBlock#config.
  GPTJForCausalLM.__init__: GPTJForCausalLM#__init__().
  GPTJMLP.act: GPTJMLP#act.
  GPTJModel.ln_f: GPTJModel#ln_f.
  GPTJModel.frequencies: GPTJModel#frequencies().
  GPTJAttention.__init__: GPTJAttention#__init__().
  GPTJAttention._create_q_proj: GPTJAttention#_create_q_proj().
  GPTJAttention.define_network: GPTJAttention#define_network().
  GPTJAttention._get_output_proj: GPTJAttention#_get_output_proj().
  GPTJBlock.precision: GPTJBlock#precision.
  GPTJModel.__init__: GPTJModel#__init__().
  GPTJForCausalLM._task_type: GPTJForCausalLM#_task_type.
  GPTJMLP.config: GPTJMLP#config.
  GPTJBlock.mlp: GPTJBlock#mlp.
  GPTJModel.h: GPTJModel#h.
  GPTJAttention: GPTJAttention#
  GPTJAttention.resid_dropout: GPTJAttention#resid_dropout.
  GPTJMLP.fc_in: GPTJMLP#fc_in.
  GPTJMLP.fc_out: GPTJMLP#fc_out.
  GPTJMLP.dropout: GPTJMLP#dropout.
  GPTJBlock.attn: GPTJBlock#attn.
  GPTJAttention._get_query_proj: GPTJAttention#_get_query_proj().
  GPTJAttention._get_key_proj: GPTJAttention#_get_key_proj().
  GPTJAttention._get_value_proj: GPTJAttention#_get_value_proj().
  GPTJMLP.__init__: GPTJMLP#__init__().
  GPTJMLP.intermediate_size: GPTJMLP#intermediate_size.
  GPTJBlock.__init__: GPTJBlock#__init__().
  GPTJModel.get_embedding: GPTJModel#get_embedding().
  GPTJForCausalLM._config_class: GPTJForCausalLM#_config_class.
  GPTJMLP: GPTJMLP#
  GPTJBlock: GPTJBlock#
  GPTJModel.embed_dim: GPTJModel#embed_dim.
  logger: logger.
  GPTJAttention.projection_mapping: GPTJAttention#projection_mapping.
  GPTJAttention._create_o_proj: GPTJAttention#_create_o_proj().
  GPTJMLP.dtype: GPTJMLP#dtype.
  GPTJMLP.param_dtype: GPTJMLP#param_dtype.
  GPTJMLP.precision: GPTJMLP#precision.
  GPTJBlock.dtype: GPTJBlock#dtype.
  GPTJBlock.param_dtype: GPTJBlock#param_dtype.
  GPTJModel.get_encoder: GPTJModel#get_encoder().
  GPTJModel.get_decoder: GPTJModel#get_decoder().
  GPTJModel.get_lm_head: GPTJModel#get_lm_head().
  GPTJForCausalLM._model_type: GPTJForCausalLM#_model_type.
---
# Module: [`easydel/modules/gpt_j/modeling_gpt_j.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py)

## Classes
### `GPTJAttention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/gpt_j/modeling_gpt_j.py:53`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L53)
- doc: GPT-J Attention module with partial Rotary Position Embeddings (RoPE).
- signature: `class GPTJAttention(UnifiedAttention):`
- members:
  - `__init__(self, config: GPTJConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs, layer_idx: int)` — [`L90`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L90) — Initialize GPT-J attention module.
  - `_create_attention_performer(self, config: GPTJConfig, rngs: nn.Rngs)` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L143) — Create attention performer with GPT-J specific dropout settings.
  - `_create_k_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L186) — Create key projection layer.
  - `_create_o_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L236) — Create output projection layer.
  - `_create_q_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L161) — Create query projection layer.
  - `_create_rotary(self, config: GPTJConfig, dtype: jnp.dtype)` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L121) — Create GPT-J-specific rotary embedding with partial RoPE.
  - `_create_v_proj(self, config, dtype, param_dtype, precision, rngs)` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L211) — Create value projection layer.
  - `_get_key_proj(self, hidden_states: Array)` — [`L314`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L314) — Apply key projection with checkpoint naming and head splitting.
  - `_get_output_proj(self, attn_output: Array)` — [`L338`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L338) — Apply output projection with checkpoint naming and residual dropout.
  - `_get_query_proj(self, hidden_states: Array)` — [`L302`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L302) — Apply query projection with checkpoint naming and head splitting.
  - `_get_value_proj(self, hidden_states: Array)` — [`L326`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L326) — Apply value projection with checkpoint naming and head splitting.
  - `_split_heads(self, hidden_states)` — [`L291`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L291) — Split hidden states into separate attention heads.
  - `define_network(self, config: GPTJConfig, dtype: jnp.dtype, param_dtype: jnp.dtype, precision: jax.lax.PrecisionLike, rngs: nn.Rngs)` — [`L265`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L265) — Define GPT-J-specific network architecture with residual dropout.
  - `out_proj` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L253)
  - `projection_mapping` — [`L75`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L75)
  - `resid_dropout` — [`L289`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L289)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`head_dim`](../../layers/attention/_unified.md#UnifiedAttention.head_dim), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`define_network`](../../layers/attention/_unified.md#UnifiedAttention.define_network), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`get_basic_rope`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_rope), [`GPTJConfig`](gpt_j_configuration.md#GPTJConfig), [`num_key_value_heads`](../../layers/attention/_unified.md#UnifiedAttention.num_key_value_heads), [`resid_pdrop`](gpt_j_configuration.md#GPTJConfig.resid_pdrop), [`attn_pdrop`](gpt_j_configuration.md#GPTJConfig.attn_pdrop), [`rotary_dim`](gpt_j_configuration.md#GPTJConfig.rotary_dim)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_create_attention_performer`](../../layers/attention/_unified.md#UnifiedAttention._create_attention_performer), [`_create_rotary`](../../layers/attention/_unified.md#UnifiedAttention._create_rotary), [`define_network`](../../layers/attention/_unified.md#UnifiedAttention.define_network), [`_create_o_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_o_proj), [`_create_q_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_q_proj), [`_create_k_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_k_proj), [`_create_v_proj`](../../layers/attention/_unified.md#UnifiedAttention._create_v_proj), [`attn`](modeling_gpt_j.md#GPTJBlock.attn)

### `GPTJBlock`  ·  implements/extends Module
- def: [`easydel/modules/gpt_j/modeling_gpt_j.py:442`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L442)
- doc: GPT-J Transformer block.
- signature: `class GPTJBlock(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L511`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L511) — Forward pass of the GPTJBlock module with parallel attention and FFN.
  - `__init__(self, config: GPTJConfig, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L457`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L457) — Initialize GPT-J transformer block.
  - `attn` — [`L493`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L493)
  - `config` — [`L477`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L477)
  - `dtype` — [`L478`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L478)
  - `ln_1` — [`L485`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L485)
  - `mlp` — [`L502`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L502)
  - `param_dtype` — [`L479`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L479)
  - `precision` — [`L480`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L480)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`GPTJConfig`](gpt_j_configuration.md#GPTJConfig), [`GPTJAttention`](modeling_gpt_j.md#GPTJAttention), [`n_inner`](gpt_j_configuration.md#GPTJConfig.n_inner), [`GPTJMLP`](modeling_gpt_j.md#GPTJMLP), [`layer_norm_epsilon`](gpt_j_configuration.md#GPTJConfig.layer_norm_epsilon)
- used by: [`dropout`](modeling_gpt_j.md#GPTJModel.dropout)

### `GPTJForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/gpt_j/modeling_gpt_j.py:817`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L817)
- doc: GPT-J model with a language modeling head for autoregressive text generation.
- signature: `class GPTJForCausalLM(BaseCausalLMModule[GPTJModel, GPTJConfig]):`
- members:
  - `__init__(self, config: GPTJConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L838`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L838) — Initialize GPT-J for causal language modeling.
- protocol/private: `_config_class`[`L836`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L836), `_model_type`[`L835`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L835), `_task_type`[`L834`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L834)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`GPTJConfig`](gpt_j_configuration.md#GPTJConfig), [`GPTJModel`](modeling_gpt_j.md#GPTJModel)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule)

### `GPTJMLP`  ·  implements/extends Module
- def: [`easydel/modules/gpt_j/modeling_gpt_j.py:351`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L351)
- doc: GPT-J MLP module.
- signature: `class GPTJMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L415`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L415) — Forward pass of the GPTJMLP module.
  - `__init__(self, config: GPTJConfig, intermediate_size: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L365`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L365) — Initialize GPT-J MLP module.
  - `act` — [`L412`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L412)
  - `config` — [`L385`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L385)
  - `dropout` — [`L413`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L413)
  - `dtype` — [`L386`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L386)
  - `fc_in` — [`L393`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L393)
  - `fc_out` — [`L402`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L402)
  - `intermediate_size` — [`L389`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L389)
  - `param_dtype` — [`L387`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L387)
  - `precision` — [`L388`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L388)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`GPTJConfig`](gpt_j_configuration.md#GPTJConfig), [`initializer_range`](gpt_j_configuration.md#GPTJConfig.initializer_range), [`resid_pdrop`](gpt_j_configuration.md#GPTJConfig.resid_pdrop), [`activation_function`](gpt_j_configuration.md#GPTJConfig.activation_function)
- used by: [`mlp`](modeling_gpt_j.md#GPTJBlock.mlp)

### `GPTJModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/gpt_j/modeling_gpt_j.py:580`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L580)
- doc: GPT-J model implementation.
- signature: `class GPTJModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, extra_embedding: Float[Array, "batch seq_len hidden_dim"] | None = None, output_attentions: bool = False, output_hidden_states: bool = False)` — [`L682`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L682) — Forward pass through the GPTJModel.
  - `__init__(self, config: GPTJConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: str | jax.lax.Precision | None = None, *, rngs: nn.Rngs)` — [`L594`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L594) — Initialize GPT-J base model.
  - `frequencies(self)` — [`L660`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L660) — Compute rotary position embedding frequencies for GPT-J.
  - `get_decoder(self)` — [`L796`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L796) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L809`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L809) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L789`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L789) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L802`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L802) — Returns the language model head of the module.
  - `dropout` — [`L628`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L628)
  - `embed_dim` — [`L619`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L619)
  - `h` — [`L638`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L638)
  - `ln_f` — [`L651`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L651)
  - `wte` — [`L620`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L620)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`LayerNorm`](../../layers/norms/_norms.md#LayerNorm), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`max_position_embeddings`](../../infra/base_config.md#EasyDeLBaseConfig.max_position_embeddings), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`views`](../../caching/transformer/cache.md#TransformerCache.views), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), [`get_basic_frequencies`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_frequencies), [`GPTJConfig`](gpt_j_configuration.md#GPTJConfig), [`initializer_range`](gpt_j_configuration.md#GPTJConfig.initializer_range), [`GPTJBlock`](modeling_gpt_j.md#GPTJBlock), [`gradient_checkpointing`](gpt_j_configuration.md#GPTJConfig.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`GPTJForCausalLM`](modeling_gpt_j.md#GPTJForCausalLM), [`__init__`](modeling_gpt_j.md#GPTJForCausalLM.__init__)

## Module values
- `logger` — [`L50`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/modeling_gpt_j.py#L50)

