---
title: 'Module: easydel/modules/grok_1/modeling_grok_1.py'
type: catalog
provenance: extracted
module: easydel/modules/grok_1/modeling_grok_1.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.grok_1.modeling_grok_1`/Grok1
symbols:
  Grok1Attention.__call__: Attention#__call__().
  Grok1Model.__call__: Model#__call__().
  Grok1DecoderLayer.__call__: DecoderLayer#__call__().
  Grok1SparseMoeBlock.__call__: SparseMoeBlock#__call__().
  Grok1ForCausalLM.__call__: ForCausalLM#__call__().
  Grok1Model.embed_tokens: Model#embed_tokens.
  Grok1ForCausalLM: ForCausalLM#
  Grok1Model: Model#
  Grok1Attention.q_proj: Attention#q_proj.
  Grok1Attention.k_proj: Attention#k_proj.
  Grok1Attention.v_proj: Attention#v_proj.
  Grok1Attention.o_proj: Attention#o_proj.
  Grok1BLockSparseMLP.linear: BLockSparseMLP#linear.
  Grok1BLockSparseMLP.linear_1: BLockSparseMLP#linear_1.
  Grok1BLockSparseMLP.linear_v: BLockSparseMLP#linear_v.
  Grok1Attention.head_dim: Attention#head_dim.
  Grok1BLockSparseMLP.__call__: BLockSparseMLP#__call__().
  Grok1SparseMoeBlock.gate: SparseMoeBlock#gate.
  Grok1DecoderLayer.pre_attn_norm: DecoderLayer#pre_attn_norm.
  Grok1DecoderLayer.post_attn_norm: DecoderLayer#post_attn_norm.
  Grok1DecoderLayer.pre_moe_norm: DecoderLayer#pre_moe_norm.
  Grok1DecoderLayer.post_moe_norm: DecoderLayer#post_moe_norm.
  Grok1SparseMoeBlock.experts: SparseMoeBlock#experts.
  Grok1DecoderLayer.config: DecoderLayer#config.
  Grok1Attention.rotary: Attention#rotary.
  Grok1Attention.attention_performer: Attention#attention_performer.
  Grok1SparseMoeBlock.config: SparseMoeBlock#config.
  Grok1ForCausalLM.__init__: ForCausalLM#__init__().
  Grok1ForCausalLM.make_lm_head_fn: ForCausalLM#make_lm_head_fn().
  Grok1Attention.num_key_value_groups: Attention#num_key_value_groups.
  Grok1DecoderLayer.attn: DecoderLayer#attn.
  Grok1Model.norm: Model#norm.
  Grok1Model.frequencies: Model#frequencies().
  Grok1ForCausalLM._compute_aux_loss: ForCausalLM#_compute_aux_loss().
  Grok1Attention.__init__: Attention#__init__().
  Grok1Model.__init__: Model#__init__().
  Grok1ForCausalLM._task_type: ForCausalLM#_task_type.
  Grok1ForCausalLM.apply_lm_head: ForCausalLM#apply_lm_head().
  Grok1Model.layers: Model#layers.
  Grok1ForCausalLM.output_multiplier_scale: ForCausalLM#output_multiplier_scale.
  Grok1Attention.precision: Attention#precision.
  Grok1Attention: Attention#
  Grok1Attention.hidden_size: Attention#hidden_size.
  Grok1Attention.resid_dropout: Attention#resid_dropout.
  Grok1Attention._merge_heads: Attention#_merge_heads().
  Grok1DecoderLayer.moe_block: DecoderLayer#moe_block.
  Grok1BLockSparseMLP.precision: BLockSparseMLP#precision.
  Grok1BLockSparseMLP.__init__: BLockSparseMLP#__init__().
  Grok1SparseMoeBlock.__init__: SparseMoeBlock#__init__().
  Grok1DecoderLayer.__init__: DecoderLayer#__init__().
  Grok1Model.get_embedding: Model#get_embedding().
  Grok1ForCausalLM._config_class: ForCausalLM#_config_class.
  Grok1BLockSparseMLP.config: BLockSparseMLP#config.
  Grok1SparseMoeBlock.dtype: SparseMoeBlock#dtype.
  Grok1Attention.dtype: Attention#dtype.
  Grok1BLockSparseMLP: BLockSparseMLP#
  Grok1SparseMoeBlock: SparseMoeBlock#
  Grok1DecoderLayer: DecoderLayer#
  Grok1ForCausalLM._project: ForCausalLM#_project().
  Grok1Attention.param_dtype: Attention#param_dtype.
  Grok1Attention.rngs: Attention#rngs.
  Grok1Attention.layer_index: Attention#layer_index.
  Grok1BLockSparseMLP.dtype: BLockSparseMLP#dtype.
  Grok1BLockSparseMLP.param_dtype: BLockSparseMLP#param_dtype.
  Grok1BLockSparseMLP.rngs: BLockSparseMLP#rngs.
  Grok1SparseMoeBlock.param_dtype: SparseMoeBlock#param_dtype.
  Grok1SparseMoeBlock.precision: SparseMoeBlock#precision.
  Grok1SparseMoeBlock.rngs: SparseMoeBlock#rngs.
  Grok1DecoderLayer.layer_index: DecoderLayer#layer_index.
  Grok1DecoderLayer.dtype: DecoderLayer#dtype.
  Grok1DecoderLayer.param_dtype: DecoderLayer#param_dtype.
  Grok1DecoderLayer.precision: DecoderLayer#precision.
  Grok1DecoderLayer.rngs: DecoderLayer#rngs.
  Grok1Model.get_encoder: Model#get_encoder().
  Grok1Model.get_decoder: Model#get_decoder().
  Grok1Model.get_lm_head: Model#get_lm_head().
  Grok1ForCausalLM._model_type: ForCausalLM#_model_type.
---
# Module: [`easydel/modules/grok_1/modeling_grok_1.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py)

## Classes
### `Grok1Attention`  ·  implements/extends AttentionModule
- def: [`easydel/modules/grok_1/modeling_grok_1.py:50`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L50)
- doc: Grok-1 Attention module.
- signature: `class Grok1Attention(AttentionModule):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo | None, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L159) — Forward pass through the Grok-1 attention layer.
  - `__init__(self, config: Grok1Config, layer_index: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L65`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L65) — Initialize Grok-1 attention with rotary position embeddings.
  - `_merge_heads(self, hidden_states)` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L147) — Merges the attention heads into a single hidden state tensor.
  - `attention_performer` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L139)
  - `dtype` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L86)
  - `head_dim` — [`L92`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L92)
  - `hidden_size` — [`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L91)
  - `k_proj` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L107)
  - `layer_index` — [`L90`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L90)
  - `num_key_value_groups` — [`L93`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L93)
  - `o_proj` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L127)
  - `param_dtype` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L87)
  - `precision` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L88)
  - `q_proj` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L97)
  - `resid_dropout` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L145)
  - `rngs` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L89)
  - `rotary` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L138)
  - `v_proj` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L117)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`forward`](../../layers/attention/_flexible.md#FlexibleAttentionModule.forward), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`concatenate`](../../layers/attention/_flexible.md#AttentionModule.concatenate), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`AttentionModule`](../../layers/attention/_flexible.md#AttentionModule), [`shard_attention_prod`](../../layers/attention/_flexible.md#AttentionModule.shard_attention_prod), [`apply_qkv_shardings`](../../layers/attention/_flexible.md#AttentionModule.apply_qkv_shardings), [`attention_weights`](../../operations/_attention_outputs.md#AttentionOutput.attention_weights), [`Grok1Config`](grok_1_configuration.md#Grok1Config), [`hidden_size`](grok_1_configuration.md#Grok1Config.hidden_size), [`__init__`](../../layers/attention/_flexible.md#AttentionModule.__init__), [`initializer_range`](grok_1_configuration.md#Grok1Config.initializer_range), [`num_attention_heads`](grok_1_configuration.md#Grok1Config.num_attention_heads), [`num_key_value_heads`](grok_1_configuration.md#Grok1Config.num_key_value_heads), [`attention_dropout`](grok_1_configuration.md#Grok1Config.attention_dropout), [`resid_pdrop`](grok_1_configuration.md#Grok1Config.resid_pdrop)
- used by: [`AttentionModule`](../../layers/attention/_flexible.md#AttentionModule), [`_merge_heads`](../../layers/attention/_flexible.md#AttentionModule._merge_heads), [`attn`](modeling_grok_1.md#Grok1DecoderLayer.attn)

### `Grok1BLockSparseMLP`  ·  implements/extends Module
- def: [`easydel/modules/grok_1/modeling_grok_1.py:247`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L247)
- doc: Grok-1 Block Sparse MLP module.
- signature: `class Grok1BLockSparseMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L321`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L321) — Apply gated MLP transformation for expert processing.
  - `__init__(self, config: Grok1Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L261`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L261) — Initialize Grok-1 Block Sparse MLP.
  - `config` — [`L284`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L284)
  - `dtype` — [`L285`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L285)
  - `linear` — [`L290`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L290)
  - `linear_1` — [`L300`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L300)
  - `linear_v` — [`L310`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L310)
  - `param_dtype` — [`L286`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L286)
  - `precision` — [`L287`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L287)
  - `rngs` — [`L288`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L288)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`Grok1Config`](grok_1_configuration.md#Grok1Config), [`hidden_size`](grok_1_configuration.md#Grok1Config.hidden_size), [`initializer_range`](grok_1_configuration.md#Grok1Config.initializer_range), [`intermediate_size`](grok_1_configuration.md#Grok1Config.intermediate_size)
- used by: [`experts`](modeling_grok_1.md#Grok1SparseMoeBlock.experts)

### `Grok1DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/grok_1/modeling_grok_1.py:464`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L464)
- doc: Grok-1 Transformer Decoder Layer.
- signature: `class Grok1DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], mode: common_types.RUNTIME_MODE_TYPES, cache_view: TransformerCacheView | RaggedPagesCacheView | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, output_attentions: bool = False, output_router_logits: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L552`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L552) — Forward pass through the decoder layer.
  - `__init__(self, config: Grok1Config, layer_index: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L479`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L479) — Initialize Grok-1 decoder layer.
  - `attn` — [`L508`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L508)
  - `config` — [`L502`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L502)
  - `dtype` — [`L504`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L504)
  - `layer_index` — [`L503`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L503)
  - `moe_block` — [`L516`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L516)
  - `param_dtype` — [`L505`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L505)
  - `post_attn_norm` — [`L530`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L530)
  - `post_moe_norm` — [`L544`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L544) — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
  - `pre_attn_norm` — [`L523`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L523) — documented in [easydel-layers-norms-_norms](../../../../concepts/easydel-layers-norms-_norms.md)
  - `pre_moe_norm` — [`L537`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L537)
  - `precision` — [`L506`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L506)
  - `rngs` — [`L507`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L507)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`RaggedPagesCacheView`](../../caching/ragged_page/cache.md#RaggedPagesCacheView), [`TransformerCacheView`](../../caching/transformer/cache.md#TransformerCacheView), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`Grok1Config`](grok_1_configuration.md#Grok1Config), [`hidden_size`](grok_1_configuration.md#Grok1Config.hidden_size), [`rms_norm_eps`](grok_1_configuration.md#Grok1Config.rms_norm_eps), [`Grok1Attention`](modeling_grok_1.md#Grok1Attention), [`Grok1SparseMoeBlock`](modeling_grok_1.md#Grok1SparseMoeBlock)
- used by: [`embed_tokens`](modeling_grok_1.md#Grok1Model.embed_tokens)

### `Grok1ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/grok_1/modeling_grok_1.py:868`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L868)
- doc: Grok-1 model with a language modeling head.
- signature: `class Grok1ForCausalLM(BaseCausalLMModule[Grok1Model, Grok1Config]):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None, apply_lm_head: bool = True)` — [`L918`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L918) — Forward pass through the Grok-1 causal language model.
  - `__init__(self, config: Grok1Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L887`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L887) — Initialize Grok-1 model for causal language modeling.
  - `_compute_aux_loss(self, outputs, attention_mask)` — [`L981`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L981) — Compute auxiliary load balancing loss from router logits.
  - `apply_lm_head(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L1002`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L1002) — Apply language model head with Grok-1's output multiplier scaling.
  - `make_lm_head_fn(self)` — [`L1018`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L1018) — Trace-safe projection with Grok-1 output multiplier scaling.
  - `output_multiplier_scale` — [`L916`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L916)
- protocol/private: `_config_class`[`L885`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L885), `_model_type`[`L884`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L884), `_project`[`L1023`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L1023), `_task_type`[`L883`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L883)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`MoeCausalLMOutput`](../../infra/modeling_outputs.md#MoeCausalLMOutput), [`make_lm_head_fn`](../_base/_base_task_module.md#BaseTaskModule.make_lm_head_fn), [`auxiliary_load_balancing_loss_func`](../../infra/loss_utils.md#auxiliary_load_balancing_loss_func), [`forward_moe`](../_base/causal_lm_module.md#BaseCausalLMModule.forward_moe), [`apply_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.apply_lm_head), [`Grok1Config`](grok_1_configuration.md#Grok1Config), [`Grok1Model`](modeling_grok_1.md#Grok1Model)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`make_lm_head_fn`](../_base/_base_task_module.md#BaseTaskModule.make_lm_head_fn), [`apply_lm_head`](../_base/causal_lm_module.md#BaseCausalLMModule.apply_lm_head)

### `Grok1Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/grok_1/modeling_grok_1.py:618`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L618)
- doc: Grok-1 model implementation.
- signature: `class Grok1Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Int[Array, "batch seq_len"] | None = None, inputs_embeds: Float[Array, "batch seq_len hidden_dim"] | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, output_router_logits: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, past_key_values: TransformerCache | RaggedPagesCache | HybridCache | None = None, cache_metadata: TransformerMetadata | RaggedPagesMetadata | OperationsMetadata | None = None)` — [`L707`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L707) — Forward pass through the Grok-1 base model.
  - `__init__(self, config: Grok1Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L633`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L633) — Initialize Grok-1 base model.
  - `frequencies(self)` — [`L696`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L696) — Compute and cache rotary position embedding frequencies.
  - `get_decoder(self)` — [`L847`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L847) — Returns the decoder part of the model's graph definition.
  - `get_embedding(self)` — [`L860`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L860) — Returns the embedding layer of the module.
  - `get_encoder(self)` — [`L840`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L840) — Returns the encoder part of the model's graph definition.
  - `get_lm_head(self)` — [`L853`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L853) — Returns the language model head of the module.
  - `embed_tokens` — [`L659`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L659)
  - `layers` — [`L673`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L673)
  - `norm` — [`L687`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L687)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`RaggedPagesMetadata`](../../caching/ragged_page/cache.md#RaggedPagesMetadata), [`TransformerMetadata`](../../caching/transformer/cache.md#TransformerMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`TransformerCache`](../../caching/transformer/cache.md#TransformerCache), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`RaggedPagesCache`](../../caching/ragged_page/cache.md#RaggedPagesCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`init_empty`](../../caching/transformer/cache.md#TransformerCache.init_empty), [`MoeModelOutput`](../../infra/modeling_outputs.md#MoeModelOutput), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), `output_hidden_states`, [`get_basic_frequencies`](../../infra/base_config.md#EasyDeLBaseConfig.get_basic_frequencies), [`router_logits`](../../infra/modeling_outputs.md#DecoderLayerOutput.router_logits), [`Grok1Config`](grok_1_configuration.md#Grok1Config), [`Grok1DecoderLayer`](modeling_grok_1.md#Grok1DecoderLayer), [`gradient_checkpointing`](grok_1_configuration.md#Grok1Config.gradient_checkpointing)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies), [`Grok1ForCausalLM`](modeling_grok_1.md#Grok1ForCausalLM), [`__init__`](modeling_grok_1.md#Grok1ForCausalLM.__init__)

### `Grok1SparseMoeBlock`  ·  implements/extends Module
- def: [`easydel/modules/grok_1/modeling_grok_1.py:348`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L348)
- doc: Grok-1 Sparse Mixture of Experts (MoE) block.
- signature: `class Grok1SparseMoeBlock(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L413`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L413) — Forward pass through the Sparse MoE block.
  - `__init__(self, config: Grok1Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L362`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L362) — Initialize Grok-1 Sparse MoE block.
  - `config` — [`L384`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L384)
  - `dtype` — [`L385`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L385)
  - `experts` — [`L400`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L400)
  - `gate` — [`L389`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L389)
  - `param_dtype` — [`L386`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L386)
  - `precision` — [`L387`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L387)
  - `rngs` — [`L388`](../../../../../../../raw/code/EasyDeL/easydel/modules/grok_1/modeling_grok_1.py#L388)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`Grok1Config`](grok_1_configuration.md#Grok1Config), [`hidden_size`](grok_1_configuration.md#Grok1Config.hidden_size), [`num_experts`](grok_1_configuration.md#Grok1Config.num_experts), [`Grok1BLockSparseMLP`](modeling_grok_1.md#Grok1BLockSparseMLP), [`num_experts_per_tok`](grok_1_configuration.md#Grok1Config.num_experts_per_tok)
- used by: [`moe_block`](modeling_grok_1.md#Grok1DecoderLayer.moe_block)

