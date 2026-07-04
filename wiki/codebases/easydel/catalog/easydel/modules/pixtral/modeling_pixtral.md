---
title: 'Module: easydel/modules/pixtral/modeling_pixtral.py'
type: catalog
provenance: extracted
module: easydel/modules/pixtral/modeling_pixtral.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.pixtral.modeling_pixtral`/
symbols:
  PixtralAttention.__call__: PixtralAttention#__call__().
  PixtralBlock.__call__: PixtralBlock#__call__().
  PixtralVisionModel.__call__: PixtralVisionModel#__call__().
  PixtralMLP.__call__: PixtralMLP#__call__().
  PixtralVisionModel: PixtralVisionModel#
  PixtralAttention.num_key_value_groups: PixtralAttention#num_key_value_groups.
  PixtralAttention.head_dim: PixtralAttention#head_dim.
  PixtralTransformer.rngs: PixtralTransformer#rngs.
  PixtralTransformer.__call__: PixtralTransformer#__call__().
  PixtralVisionModel.patch_conv: PixtralVisionModel#patch_conv.
  PixtralMLP.act_fn: PixtralMLP#act_fn.
  PixtralAttention.q_proj: PixtralAttention#q_proj.
  PixtralAttention.k_proj: PixtralAttention#k_proj.
  PixtralAttention.v_proj: PixtralAttention#v_proj.
  PixtralAttention.o_proj: PixtralAttention#o_proj.
  PixtralAttention.attention_performer: PixtralAttention#attention_performer.
  PixtralMLP.precision: PixtralMLP#precision.
  PixtralMLP.gate_proj: PixtralMLP#gate_proj.
  PixtralMLP.down_proj: PixtralMLP#down_proj.
  PixtralMLP.up_proj: PixtralMLP#up_proj.
  PixtralBlock.attention_norm: PixtralBlock#attention_norm.
  PixtralBlock.ffn_norm: PixtralBlock#ffn_norm.
  PixtralTransformer.layers: PixtralTransformer#layers.
  PixtralVisionModel.ln_pre: PixtralVisionModel#ln_pre.
  PixtralVisionModel.frequencies: PixtralVisionModel#frequencies().
  PixtralAttention.__init__: PixtralAttention#__init__().
  PixtralVisionModel.__init__: PixtralVisionModel#__init__().
  PixtralBlock.feed_forward: PixtralBlock#feed_forward.
  apply_rotary_pos_emb: apply_rotary_pos_emb().
  PixtralAttention: PixtralAttention#
  PixtralBlock.attention: PixtralBlock#attention.
  PixtralVisionModel.transformer: PixtralVisionModel#transformer.
  PixtralMLP.config: PixtralMLP#config.
  PixtralMLP.__init__: PixtralMLP#__init__().
  PixtralAttention.hidden_size: PixtralAttention#hidden_size.
  PixtralBlock.__init__: PixtralBlock#__init__().
  PixtralTransformer.__init__: PixtralTransformer#__init__().
  PixtralVisionModel.get_embedding: PixtralVisionModel#get_embedding().
  rotate_half: rotate_half().
  PixtralBlock.config: PixtralBlock#config.
  position_ids_in_meshgrid: position_ids_in_meshgrid().
  generate_block_attention_mask: generate_block_attention_mask().
  compute_frequencies: compute_frequencies().
  PixtralMLP: PixtralMLP#
  PixtralBlock: PixtralBlock#
  PixtralTransformer: PixtralTransformer#
  PixtralTransformer.config: PixtralTransformer#config.
  PixtralMLP.dtype: PixtralMLP#dtype.
  PixtralMLP.param_dtype: PixtralMLP#param_dtype.
  PixtralAttention.dtype: PixtralAttention#dtype.
  PixtralAttention.param_dtype: PixtralAttention#param_dtype.
  PixtralAttention.precision: PixtralAttention#precision.
  PixtralAttention.rngs: PixtralAttention#rngs.
  PixtralBlock.dtype: PixtralBlock#dtype.
  PixtralBlock.param_dtype: PixtralBlock#param_dtype.
  PixtralBlock.precision: PixtralBlock#precision.
  PixtralTransformer.dtype: PixtralTransformer#dtype.
  PixtralTransformer.param_dtype: PixtralTransformer#param_dtype.
  PixtralTransformer.precision: PixtralTransformer#precision.
  PixtralVisionModel.get_encoder: PixtralVisionModel#get_encoder().
  PixtralVisionModel.get_decoder: PixtralVisionModel#get_decoder().
  PixtralVisionModel.get_lm_head: PixtralVisionModel#get_lm_head().
---
# Module: [`easydel/modules/pixtral/modeling_pixtral.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py)

## Classes
### `PixtralAttention`  ·  implements/extends AttentionModule
- def: [`easydel/modules/pixtral/modeling_pixtral.py:262`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L262)
- doc: Multi-head attention layer with 2D RoPE embeddings for Pixtral vision models.
- signature: `class PixtralAttention(AttentionModule):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L331`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L331) — Apply multi-head self-attention with 2D RoPE.
  - `__init__(self, config: PixtralVisionConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L271`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L271) — Initialize Pixtral attention layer with 2D RoPE support.
  - `attention_performer` — [`L323`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L323)
  - `dtype` — [`L290`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L290)
  - `head_dim` — [`L295`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L295)
  - `hidden_size` — [`L294`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L294)
  - `k_proj` — [`L319`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L319)
  - `num_key_value_groups` — [`L297`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L297)
  - `o_proj` — [`L321`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L321)
  - `param_dtype` — [`L291`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L291)
  - `precision` — [`L292`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L292)
  - `q_proj` — [`L318`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L318)
  - `rngs` — [`L293`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L293)
  - `v_proj` — [`L320`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L320)
- uses (calls/refs, reference-scoped): [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`FlexibleAttentionModule`](../../layers/attention/_flexible.md#FlexibleAttentionModule), [`config`](../../layers/attention/_flexible.md#AttentionModule.config), [`forward`](../../layers/attention/_flexible.md#FlexibleAttentionModule.forward), [`AttentionLayerOutput`](../../infra/modeling_outputs.md#AttentionLayerOutput), [`concatenate`](../../layers/attention/_flexible.md#AttentionModule.concatenate), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`AttentionModule`](../../layers/attention/_flexible.md#AttentionModule), [`shard_attention_prod`](../../layers/attention/_flexible.md#AttentionModule.shard_attention_prod), [`attention_weights`](../../operations/_attention_outputs.md#AttentionOutput.attention_weights), [`_merge_heads`](../../layers/attention/_flexible.md#AttentionModule._merge_heads), [`PixtralVisionConfig`](pixtral_configuration.md#PixtralVisionConfig), [`__init__`](../../layers/attention/_flexible.md#AttentionModule.__init__), [`hidden_size`](pixtral_configuration.md#PixtralVisionConfig.hidden_size), [`initializer_range`](pixtral_configuration.md#PixtralVisionConfig.initializer_range), [`num_attention_heads`](pixtral_configuration.md#PixtralVisionConfig.num_attention_heads), [`apply_rotary_pos_emb`](modeling_pixtral.md#apply_rotary_pos_emb), [`attention_dropout`](pixtral_configuration.md#PixtralVisionConfig.attention_dropout)
- used by: [`AttentionModule`](../../layers/attention/_flexible.md#AttentionModule), [`attention`](modeling_pixtral.md#PixtralBlock.attention)

### `PixtralBlock`  ·  implements/extends Module
- def: [`easydel/modules/pixtral/modeling_pixtral.py:424`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L424)
- doc: Single transformer block for Pixtral vision models.
- signature: `class PixtralBlock(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"], mask_info: MaskInfo, position_ids: Int[Array, "batch seq_len"], output_attentions: bool = False, frequencies: Float[Array, "seq_len head_dim"] | None = None)` — [`L483`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L483) — Forward pass through the transformer block.
  - `__init__(self, config: PixtralVisionConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L431`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L431) — Initialize Pixtral transformer block.
  - `attention` — [`L454`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L454)
  - `attention_norm` — [`L468`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L468)
  - `config` — [`L449`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L449)
  - `dtype` — [`L450`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L450)
  - `feed_forward` — [`L461`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L461)
  - `ffn_norm` — [`L475`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L475)
  - `param_dtype` — [`L451`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L451)
  - `precision` — [`L452`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L452)
- uses (calls/refs, reference-scoped): [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`block_wise_ffn`](../../infra/utils.md#block_wise_ffn), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`scan_mlp_chunk_size`](../../infra/base_config.md#EasyDeLBaseConfig.scan_mlp_chunk_size), [`use_scan_mlp`](../../infra/base_config.md#EasyDeLBaseConfig.use_scan_mlp), [`PixtralVisionConfig`](pixtral_configuration.md#PixtralVisionConfig), [`hidden_size`](pixtral_configuration.md#PixtralVisionConfig.hidden_size), [`PixtralAttention`](modeling_pixtral.md#PixtralAttention), [`PixtralMLP`](modeling_pixtral.md#PixtralMLP)
- used by: [`rngs`](modeling_pixtral.md#PixtralTransformer.rngs)

### `PixtralMLP`  ·  implements/extends Module
- def: [`easydel/modules/pixtral/modeling_pixtral.py:170`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L170)
- doc: Multi-Layer Perceptron module for Pixtral vision models.
- signature: `class PixtralMLP(nn.Module):`
- members:
  - `__call__(self, hidden_states: Float[Array, "batch seq_len hidden_dim"])` — [`L235`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L235) — Apply SiLU-gated feedforward transformation.
  - `__init__(self, config: PixtralVisionConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L177) — Initialize Pixtral MLP block.
  - `act_fn` — [`L233`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L233)
  - `config` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L196)
  - `down_proj` — [`L223`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L223)
  - `dtype` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L197)
  - `gate_proj` — [`L218`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L218)
  - `param_dtype` — [`L198`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L198)
  - `precision` — [`L199`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L199)
  - `up_proj` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L228)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`PixtralVisionConfig`](pixtral_configuration.md#PixtralVisionConfig), [`hidden_size`](pixtral_configuration.md#PixtralVisionConfig.hidden_size), [`initializer_range`](pixtral_configuration.md#PixtralVisionConfig.initializer_range), [`intermediate_size`](pixtral_configuration.md#PixtralVisionConfig.intermediate_size), [`hidden_act`](pixtral_configuration.md#PixtralVisionConfig.hidden_act)
- used by: [`feed_forward`](modeling_pixtral.md#PixtralBlock.feed_forward)

### `PixtralTransformer`  ·  implements/extends Module
- def: [`easydel/modules/pixtral/modeling_pixtral.py:529`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L529)
- doc: Transformer stack for Pixtral vision models.
- signature: `class PixtralTransformer(nn.Module):`
- members:
  - `__call__(self, inputs_embeds: Float[Array, "batch seq_len hidden_dim"], position_embeddings: Array | None = None, attention_mask: Bool[Array, "batch seq_len"] | None = None, mask_info: MaskInfo | None = None, position_ids: Int[Array, "batch seq_len"] | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None)` — [`L578`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L578) — Forward pass through the Pixtral transformer stack.
  - `__init__(self, config: PixtralVisionConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L536`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L536) — Initialize Pixtral transformer stack.
  - `config` — [`L554`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L554)
  - `dtype` — [`L555`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L555)
  - `layers` — [`L565`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L565)
  - `param_dtype` — [`L556`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L556)
  - `precision` — [`L557`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L557)
  - `rngs` — [`L558`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L558)
- uses (calls/refs, reference-scoped): [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`PixtralVisionConfig`](pixtral_configuration.md#PixtralVisionConfig), [`PixtralBlock`](modeling_pixtral.md#PixtralBlock), [`num_hidden_layers`](pixtral_configuration.md#PixtralVisionConfig.num_hidden_layers)
- used by: [`transformer`](modeling_pixtral.md#PixtralVisionModel.transformer)

### `PixtralVisionModel`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/pixtral/modeling_pixtral.py:649`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L649)
- doc: Pixtral vision encoder model.
- signature: `class PixtralVisionModel(EasyDeLBaseModule):`
- members:
  - `__call__(self, pixel_values: list[Array], output_hidden_states: bool | None = False, output_attentions: bool | None = None, *args, **kwargs)` — [`L727`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L727) — Forward pass through the Pixtral vision model.
  - `__init__(self, config: PixtralVisionConfig, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L663`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L663) — Initialize Pixtral vision model.
  - `frequencies(self)` — [`L715`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L715) — Compute and cache 2D RoPE frequencies for patch positions.
  - `get_decoder(self)` — [`L789`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L789) — Returns the decoder (not applicable for encoder-only vision model).
  - `get_embedding(self)` — [`L797`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L797) — Returns the patch embedding layer.
  - `get_encoder(self)` — [`L785`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L785) — Returns the encoder (this vision model acts as the encoder).
  - `get_lm_head(self)` — [`L793`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L793) — Returns the language model head (not applicable for vision encoder).
  - `ln_pre` — [`L699`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L699)
  - `patch_conv` — [`L688`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L688)
  - `transformer` — [`L706`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L706)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`dtype`](../../infra/base_module.md#EasyDeLBaseModule.dtype), [`last_hidden_state`](../../infra/modeling_outputs.md#BaseModelOutput.last_hidden_state), [`attentions`](../../infra/modeling_outputs.md#BaseModelOutput.attentions), [`hidden_states`](../../infra/modeling_outputs.md#BaseModelOutput.hidden_states), [`BASE_VISION`](../../infra/factory.md#TaskType.BASE_VISION), [`PixtralVisionConfig`](pixtral_configuration.md#PixtralVisionConfig), [`hidden_size`](pixtral_configuration.md#PixtralVisionConfig.hidden_size), [`patch_size`](pixtral_configuration.md#PixtralVisionConfig.patch_size), [`PixtralTransformer`](modeling_pixtral.md#PixtralTransformer), [`compute_frequencies`](modeling_pixtral.md#compute_frequencies), [`generate_block_attention_mask`](modeling_pixtral.md#generate_block_attention_mask), [`num_channels`](pixtral_configuration.md#PixtralVisionConfig.num_channels), [`position_ids_in_meshgrid`](modeling_pixtral.md#position_ids_in_meshgrid)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_lm_head`](../../infra/base_module.md#EasyDeLBaseModule.get_lm_head), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`get_encoder`](../../infra/base_module.md#EasyDeLBaseModule.get_encoder), [`frequencies`](../../infra/base_module.md#EasyDeLBaseModule.frequencies)

## Functions
- `apply_rotary_pos_emb(q, k, cos, sin, position_ids=None, unsqueeze_dim=0)` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L133) — Applies Rotary Position Embedding to the query and key tensors.
- `compute_frequencies(dim: int, max_patches_per_side: int, theta: float = 10000)` — [`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L91) — Computes frequencies with a fixed max length for RoPE.
- `generate_block_attention_mask(patch_embeds_list, tensor)` — [`L58`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L58) — Generates a block-diagonal attention mask for multi-image processing.
- `position_ids_in_meshgrid(patch_embeds_list, max_width)` — [`L37`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L37) — Generates position IDs based on a meshgrid for a list of patch embeddings.
- `rotate_half(x)` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/pixtral/modeling_pixtral.py#L125) — Rotates half the hidden dims of the input.

