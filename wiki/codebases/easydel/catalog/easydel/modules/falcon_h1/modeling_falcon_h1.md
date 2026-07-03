---
title: 'Module: easydel/modules/falcon_h1/modeling_falcon_h1.py'
type: catalog
provenance: extracted
module: easydel/modules/falcon_h1/modeling_falcon_h1.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.falcon_h1.modeling_falcon_h1`/
symbols:
  FalconH1Mixer.__call__: FalconH1Mixer#__call__().
  FalconH1DecoderLayer.__call__: FalconH1DecoderLayer#__call__().
  FalconH1Model.__call__: FalconH1Model#__call__().
  FalconH1Mixer.intermediate_size: FalconH1Mixer#intermediate_size.
  Conv1D.__call__: Conv1D#__call__().
  compute_mup_vector: compute_mup_vector().
  FalconH1MLP.__call__: FalconH1MLP#__call__().
  FalconH1Model.embed_tokens: FalconH1Model#embed_tokens.
  FalconH1Mixer._body: FalconH1Mixer#_body().
  FalconH1ForCausalLM: FalconH1ForCausalLM#
  FalconH1Model: FalconH1Model#
  FalconH1Mixer.in_proj: FalconH1Mixer#in_proj.
  FalconH1Mixer.norm: FalconH1Mixer#norm.
  FalconH1Mixer.out_proj: FalconH1Mixer#out_proj.
  FalconH1Mixer.conv1d: FalconH1Mixer#conv1d.
  FalconH1Mixer.n_groups: FalconH1Mixer#n_groups.
  FalconH1Mixer.chunk_size: FalconH1Mixer#chunk_size.
  FalconH1Mixer.conv_dim: FalconH1Mixer#conv_dim.
  FalconH1ForCausalLM.prepare_inputs_for_generation: FalconH1ForCausalLM#prepare_inputs_for_generation().
  FalconH1Mixer.D: FalconH1Mixer#D.
  FalconH1Mixer.num_heads: FalconH1Mixer#num_heads.
  FalconH1RMSNormGated.__call__: FalconH1RMSNormGated#__call__().
  FalconH1ForCausalLM.__init__: FalconH1ForCausalLM#__init__().
  FalconH1ForCausalLM.make_lm_head_fn: FalconH1ForCausalLM#make_lm_head_fn().
  FalconH1Mixer.ssm_state_size: FalconH1Mixer#ssm_state_size.
  FalconH1Mixer.conv_kernel_size: FalconH1Mixer#conv_kernel_size.
  FalconH1Mixer.dt_bias: FalconH1Mixer#dt_bias.
  FalconH1Mixer.A_log: FalconH1Mixer#A_log.
  FalconH1MLP.gate_proj: FalconH1MLP#gate_proj.
  FalconH1MLP.up_proj: FalconH1MLP#up_proj.
  FalconH1MLP.down_proj: FalconH1MLP#down_proj.
  FalconH1DecoderLayer.input_layernorm: FalconH1DecoderLayer#input_layernorm.
  FalconH1DecoderLayer.pre_ff_layernorm: FalconH1DecoderLayer#pre_ff_layernorm.
  FalconH1Model.final_layernorm: FalconH1Model#final_layernorm.
  FalconH1Mixer.act: FalconH1Mixer#act.
  FalconH1ForCausalLM.__call__: FalconH1ForCausalLM#__call__().
  Conv1D.kernel: Conv1D#kernel.
  Conv1D.bias: Conv1D#bias.
  FalconH1RMSNormGated.kernel: FalconH1RMSNormGated#kernel.
  FalconH1MLP.act_fn: FalconH1MLP#act_fn.
  FalconH1Mixer.hidden_size: FalconH1Mixer#hidden_size.
  FalconH1Mixer.head_dim: FalconH1Mixer#head_dim.
  FalconH1Mixer.mamba_rms_norm: FalconH1Mixer#mamba_rms_norm.
  FalconH1Attention.__init__: FalconH1Attention#__init__().
  FalconH1MLP.precision: FalconH1MLP#precision.
  FalconH1Model.__init__: FalconH1Model#__init__().
  FalconH1ForCausalLM.update_inputs_for_generation: FalconH1ForCausalLM#update_inputs_for_generation().
  FalconH1Mixer.use_conv_bias: FalconH1Mixer#use_conv_bias.
  FalconH1Model.layers: FalconH1Model#layers.
  apply_mask_to_padding_states: apply_mask_to_padding_states().
  FalconH1RMSNormGated.n_groups: FalconH1RMSNormGated#n_groups.
  FalconH1Attention: FalconH1Attention#
  FalconH1Attention.key_multiplier: FalconH1Attention#key_multiplier.
  FalconH1Mixer.use_bias: FalconH1Mixer#use_bias.
  FalconH1Mixer.layer_norm_epsilon: FalconH1Mixer#layer_norm_epsilon.
  FalconH1Mixer.ssm_in_multiplier: FalconH1Mixer#ssm_in_multiplier.
  FalconH1Mixer.ssm_op: FalconH1Mixer#ssm_op.
  FalconH1MLP.down_multiplier: FalconH1MLP#down_multiplier.
  FalconH1DecoderLayer.feed_forward: FalconH1DecoderLayer#feed_forward.
  FalconH1DecoderLayer.mamba: FalconH1DecoderLayer#mamba.
  FalconH1DecoderLayer.self_attn: FalconH1DecoderLayer#self_attn.
  FalconH1DecoderLayer.attention_in_multiplier: FalconH1DecoderLayer#attention_in_multiplier.
  FalconH1DecoderLayer.ssm_out_multiplier: FalconH1DecoderLayer#ssm_out_multiplier.
  FalconH1DecoderLayer.attn_out_multiplier: FalconH1DecoderLayer#attn_out_multiplier.
  FalconH1Model.embedding_multiplier: FalconH1Model#embedding_multiplier.
  FalconH1Model.lm_head_multiplier: FalconH1Model#lm_head_multiplier.
  Conv1D.dtype: Conv1D#dtype.
  FalconH1Mixer.config: FalconH1Mixer#config.
  FalconH1Attention._postprocess_qkv: FalconH1Attention#_postprocess_qkv().
  FalconH1Mixer.__init__: FalconH1Mixer#__init__().
  FalconH1Mixer.activation: FalconH1Mixer#activation.
  FalconH1MLP.__init__: FalconH1MLP#__init__().
  FalconH1DecoderLayer.__init__: FalconH1DecoderLayer#__init__().
  FalconH1Model.get_decoder: FalconH1Model#get_decoder().
  FalconH1Model.get_embedding: FalconH1Model#get_embedding().
  Conv1D.padding: Conv1D#padding.
  FalconH1RMSNormGated.norm_before_gate: FalconH1RMSNormGated#norm_before_gate.
  FalconH1MLP.config: FalconH1MLP#config.
  Conv1D: Conv1D#
  Conv1D.stride: Conv1D#stride.
  Conv1D.dilation: Conv1D#dilation.
  Conv1D.groups: Conv1D#groups.
  Conv1D.use_bias: Conv1D#use_bias.
  Conv1D.precision: Conv1D#precision.
  FalconH1RMSNormGated: FalconH1RMSNormGated#
  FalconH1RMSNormGated.variance_epsilon: FalconH1RMSNormGated#variance_epsilon.
  FalconH1Mixer: FalconH1Mixer#
  FalconH1Mixer.precision: FalconH1Mixer#precision.
  FalconH1MLP: FalconH1MLP#
  FalconH1MLP.gate_multiplier: FalconH1MLP#gate_multiplier.
  FalconH1DecoderLayer: FalconH1DecoderLayer#
  FalconH1DecoderLayer.config: FalconH1DecoderLayer#config.
  FalconH1ForCausalLM._project: FalconH1ForCausalLM#_project().
  Conv1D.__init__: Conv1D#__init__().
  Conv1D.features: Conv1D#features.
  Conv1D.kernel_size: Conv1D#kernel_size.
  Conv1D.param_dtype: Conv1D#param_dtype.
  Conv1D.craft_sharding: Conv1D#craft_sharding().
  FalconH1RMSNormGated.__init__: FalconH1RMSNormGated#__init__().
  FalconH1RMSNormGated.hidden_size: FalconH1RMSNormGated#hidden_size.
  FalconH1RMSNormGated.dtype: FalconH1RMSNormGated#dtype.
  FalconH1RMSNormGated.craft_sharding: FalconH1RMSNormGated#craft_sharding().
  FalconH1Mixer.layer_idx: FalconH1Mixer#layer_idx.
  FalconH1Mixer.dtype: FalconH1Mixer#dtype.
  FalconH1Mixer.param_dtype: FalconH1Mixer#param_dtype.
  FalconH1Mixer.craft_sharding: FalconH1Mixer#craft_sharding().
  FalconH1MLP.dtype: FalconH1MLP#dtype.
  FalconH1MLP.param_dtype: FalconH1MLP#param_dtype.
  FalconH1DecoderLayer.layer_idx: FalconH1DecoderLayer#layer_idx.
  FalconH1DecoderLayer.dtype: FalconH1DecoderLayer#dtype.
  FalconH1DecoderLayer.param_dtype: FalconH1DecoderLayer#param_dtype.
  FalconH1DecoderLayer.precision: FalconH1DecoderLayer#precision.
  FalconH1ForCausalLM.get_decoder: FalconH1ForCausalLM#get_decoder().
  FalconH1ForCausalLM.get_embedding: FalconH1ForCausalLM#get_embedding().
---
# Module: [`easydel/modules/falcon_h1/modeling_falcon_h1.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py)

## Classes
### `Conv1D`  ·  implements/extends Module
- def: [`easydel/modules/falcon_h1/modeling_falcon_h1.py:192`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L192)
- doc: Depthwise causal 1D convolution layer for the Mamba SSM mixer.
- signature: `class Conv1D(nn.Module):`
- members:
  - `__call__(self, x: Array)` — [`L280`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L280) — Apply 1D convolution to the input.
  - `__init__(self, features: int, kernel_size: int, *, rngs: nn.Rngs, stride: int = 1, padding: int = 0, dilation: int = 1, groups: int = 1, use_bias: bool = True, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None)` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L216) — Initialize the 1D convolution layer.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L273`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L273) — Return sharding specs for convolution parameters.
  - `bias` — [`L266`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L266)
  - `dilation` — [`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L252)
  - `dtype` — [`L255`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L255)
  - `features` — [`L248`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L248)
  - `groups` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L253)
  - `kernel` — [`L259`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L259)
  - `kernel_size` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L249)
  - `padding` — [`L251`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L251)
  - `param_dtype` — [`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L256)
  - `precision` — [`L257`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L257)
  - `stride` — [`L250`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L250)
  - `use_bias` — [`L254`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L254)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound)
- used by: [`__call__`](modeling_falcon_h1.md#FalconH1Mixer.__call__), [`conv1d`](modeling_falcon_h1.md#FalconH1Mixer.conv1d)

### `FalconH1Attention`  ·  implements/extends UnifiedAttention
- def: [`easydel/modules/falcon_h1/modeling_falcon_h1.py:116`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L116)
- doc: Multi-head attention layer for FalconH1 hybrid models.
- signature: `class FalconH1Attention(UnifiedAttention):`
- members:
  - `__init__(self, config: FalconH1Config, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L130) — Initialize FalconH1 attention layer with RoPE and muP key scaling.
  - `_postprocess_qkv(self, query_states: Float[Array, "batch_size seq_len num_heads head_dim"], key_states: Float[Array, "batch_size seq_len num_kv_heads head_dim"], value_states: Float[Array, "batch_size seq_len num_kv_heads head_dim"])` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L163) — Apply muP key scaling after QKV projection.
  - `key_multiplier` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L161)
- uses (calls/refs, reference-scoped): [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`__init__`](../../layers/attention/_unified.md#UnifiedAttention.__init__), [`FalconH1Config`](falcon_h1_configuration.md#FalconH1Config), [`key_multiplier`](falcon_h1_configuration.md#FalconH1Config.key_multiplier)
- used by: [`UnifiedAttention`](../../layers/attention/_unified.md#UnifiedAttention), [`_postprocess_qkv`](../../layers/attention/_unified.md#UnifiedAttention._postprocess_qkv), [`self_attn`](modeling_falcon_h1.md#FalconH1DecoderLayer.self_attn)

### `FalconH1DecoderLayer`  ·  implements/extends Module
- def: [`easydel/modules/falcon_h1/modeling_falcon_h1.py:905`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L905)
- doc: Single decoder layer for FalconH1 hybrid models.
- signature: `class FalconH1DecoderLayer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Array, mask_info: MaskInfo | None, position_ids: Array, mode: common_types.RUNTIME_MODE_TYPES, cache_view: HybridCacheView | None = None, cache_metadata: OperationsMetadata | None = None, output_attentions: bool = False, frequencies: Array | None = None)` — [`L1001`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1001) — Forward pass through the FalconH1 decoder layer.
  - `__init__(self, config: FalconH1Config, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L931`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L931) — Initialize the FalconH1 decoder layer.
  - `attention_in_multiplier` — [`L982`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L982)
  - `attn_out_multiplier` — [`L984`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L984)
  - `config` — [`L952`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L952)
  - `dtype` — [`L954`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L954)
  - `feed_forward` — [`L958`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L958)
  - `input_layernorm` — [`L986`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L986)
  - `layer_idx` — [`L953`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L953)
  - `mamba` — [`L965`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L965)
  - `param_dtype` — [`L955`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L955)
  - `pre_ff_layernorm` — [`L993`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L993)
  - `precision` — [`L956`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L956)
  - `self_attn` — [`L973`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L973)
  - `ssm_out_multiplier` — [`L983`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L983)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`DecoderLayerOutput`](../../infra/modeling_outputs.md#DecoderLayerOutput), [`attention_output`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_output), [`cache_view`](../../infra/modeling_outputs.md#AttentionLayerOutput.cache_view), [`attention_weight`](../../infra/modeling_outputs.md#AttentionLayerOutput.attention_weight), [`HybridCacheView`](../../caching/hybrid/cache.md#HybridCacheView), [`FalconH1Config`](falcon_h1_configuration.md#FalconH1Config), [`hidden_size`](falcon_h1_configuration.md#FalconH1Config.hidden_size), [`rms_norm_eps`](falcon_h1_configuration.md#FalconH1Config.rms_norm_eps), [`FalconH1Attention`](modeling_falcon_h1.md#FalconH1Attention), [`FalconH1MLP`](modeling_falcon_h1.md#FalconH1MLP), [`FalconH1Mixer`](modeling_falcon_h1.md#FalconH1Mixer), [`attention_in_multiplier`](falcon_h1_configuration.md#FalconH1Config.attention_in_multiplier), [`attention_out_multiplier`](falcon_h1_configuration.md#FalconH1Config.attention_out_multiplier), [`ssm_out_multiplier`](falcon_h1_configuration.md#FalconH1Config.ssm_out_multiplier)
- used by: [`embed_tokens`](modeling_falcon_h1.md#FalconH1Model.embed_tokens)

### `FalconH1ForCausalLM`  ·  implements/extends BaseCausalLMModule
- def: [`easydel/modules/falcon_h1/modeling_falcon_h1.py:1350`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1350)
- doc: FalconH1 model with a language modeling head for causal language modeling.
- signature: `class FalconH1ForCausalLM(BaseCausalLMModule[FalconH1Model, FalconH1Config]):`
- members:
  - `__call__(self, input_ids: Array | None = None, attention_mask: Array | None = None, position_ids: Array | None = None, past_key_values: HybridCache | None = None, inputs_embeds: Array | None = None, use_cache: bool | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, mask_info: MaskInfo | None = None, cache_metadata: OperationsMetadata | None = None, apply_lm_head: bool = True, **kwargs)` — [`L1406`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1406) — Perform forward pass for causal language modeling.
  - `__init__(self, config: FalconH1Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1373`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1373) — Initialize the FalconH1 causal language model.
  - `get_decoder(self)` — [`L1602`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1602) — Return the decoder layers of the underlying model.
  - `get_embedding(self)` — [`L1611`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1611) — Return the token embedding layer of the underlying model.
  - `make_lm_head_fn(self)` — [`L1492`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1492) — Trace-safe projection with Falcon-H1 muP lm_head_multiplier.
  - `prepare_inputs_for_generation(self, input_ids: Array, max_length: int, pad_token_id: int, starts: Array | None = None, attention_mask: Array | None = None, **kwargs)` — [`L1502`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1502) — Prepare inputs for the first step of autoregressive generation.
  - `update_inputs_for_generation(self, model_outputs: CausalLMOutput, model_kwargs: dict[str, tp.Any])` — [`L1568`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1568) — Update model inputs for the next autoregressive generation step.
- protocol/private: `_project`[`L1497`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1497)
- uses (calls/refs, reference-scoped): [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`register_module`](../../infra/factory.md#register_module), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`CAUSAL_LM`](../../infra/factory.md#TaskType.CAUSAL_LM), [`base_model`](../_base/_base_task_module.md#BaseTaskModule.base_model), [`init_operations_cache`](../../infra/mixins/generation.md#EasyGenerationMixin.init_operations_cache), [`CausalLMOutput`](../../infra/modeling_outputs.md#CausalLMOutput), [`__init__`](../_base/causal_lm_module.md#BaseCausalLMModule.__init__), [`make_lm_head_fn`](../_base/_base_task_module.md#BaseTaskModule.make_lm_head_fn), [`FalconH1Config`](falcon_h1_configuration.md#FalconH1Config), [`FalconH1Model`](modeling_falcon_h1.md#FalconH1Model), [`prepare_inputs_for_call`](../../infra/base_module.md#EasyDeLBaseModule.prepare_inputs_for_call), [`compute_prefill_length`](../../infra/mixins/generation.md#EasyGenerationMixin.compute_prefill_length), `tie_word_embeddings`, [`past_key_values`](../../infra/modeling_outputs.md#MaskedLMOutput.past_key_values), [`lm_head_multiplier`](modeling_falcon_h1.md#FalconH1Model.lm_head_multiplier), [`_pad_maskinfo_to_maxlen`](../../infra/mixins/generation.md#EasyGenerationMixin._pad_maskinfo_to_maxlen), [`compute_prefill_length_from_mask`](../../infra/mixins/generation.md#EasyGenerationMixin.compute_prefill_length_from_mask)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`BaseCausalLMModule`](../_base/causal_lm_module.md#BaseCausalLMModule), [`get_embedding`](../_base/_base_task_module.md#BaseTaskModule.get_embedding), [`get_decoder`](../_base/_base_task_module.md#BaseTaskModule.get_decoder), [`prepare_inputs_for_generation`](../../infra/mixins/generation.md#EasyGenerationMixin.prepare_inputs_for_generation), [`make_lm_head_fn`](../_base/_base_task_module.md#BaseTaskModule.make_lm_head_fn), [`update_inputs_for_generation`](../../infra/mixins/generation.md#EasyGenerationMixin.update_inputs_for_generation)

### `FalconH1MLP`  ·  implements/extends Module
- def: [`easydel/modules/falcon_h1/modeling_falcon_h1.py:814`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L814)
- doc: SwiGLU Multi-Layer Perceptron for FalconH1 models.
- signature: `class FalconH1MLP(nn.Module):`
- members:
  - `__call__(self, x: Array)` — [`L879`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L879) — Apply SwiGLU feedforward transformation with muP scaling.
  - `__init__(self, config: FalconH1Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L834`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L834) — Initialize the SwiGLU MLP block.
  - `act_fn` — [`L876`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L876)
  - `config` — [`L854`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L854)
  - `down_multiplier` — [`L877`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L877)
  - `down_proj` — [`L874`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L874)
  - `dtype` — [`L855`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L855)
  - `gate_multiplier` — [`L877`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L877)
  - `gate_proj` — [`L872`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L872)
  - `param_dtype` — [`L856`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L856)
  - `precision` — [`L857`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L857)
  - `up_proj` — [`L873`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L873)
- uses (calls/refs, reference-scoped): [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`FalconH1Config`](falcon_h1_configuration.md#FalconH1Config), [`hidden_size`](falcon_h1_configuration.md#FalconH1Config.hidden_size), [`hidden_act`](falcon_h1_configuration.md#FalconH1Config.hidden_act), [`intermediate_size`](falcon_h1_configuration.md#FalconH1Config.intermediate_size), [`mlp_bias`](falcon_h1_configuration.md#FalconH1Config.mlp_bias), [`mlp_multipliers`](falcon_h1_configuration.md#FalconH1Config.mlp_multipliers)
- used by: [`feed_forward`](modeling_falcon_h1.md#FalconH1DecoderLayer.feed_forward)

### `FalconH1Mixer`  ·  implements/extends Module
- def: [`easydel/modules/falcon_h1/modeling_falcon_h1.py:406`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L406)
- doc: Mamba2-style selective state space model (SSM) mixer for FalconH1 blocks.
- signature: `class FalconH1Mixer(nn.Module):`
- members:
  - `__call__(self, hidden_states: Array, mask_info: MaskInfo | None, cache_view: HybridCacheView | None = None, cache_metadata: OperationsMetadata | None = None)` — [`L568`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L568) — Process input through the Mamba SSM mixer.
  - `__init__(self, config: FalconH1Config, layer_idx: int, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L432`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L432) — Initialize the FalconH1 Mamba mixer.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L560`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L560) — Return sharding specs for state space parameters.
  - `A_log` — [`L520`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L520)
  - `D` — [`L526`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L526)
  - `act` — [`L483`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L483)
  - `activation` — [`L482`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L482)
  - `chunk_size` — [`L474`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L474)
  - `config` — [`L459`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L459)
  - `conv1d` — [`L492`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L492)
  - `conv_dim` — [`L491`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L491)
  - `conv_kernel_size` — [`L468`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L468)
  - `dt_bias` — [`L514`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L514)
  - `dtype` — [`L461`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L461)
  - `head_dim` — [`L473`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L473)
  - `hidden_size` — [`L466`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L466)
  - `in_proj` — [`L504`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L504)
  - `intermediate_size` — [`L469`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L469)
  - `layer_idx` — [`L460`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L460)
  - `layer_norm_epsilon` — [`L486`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L486)
  - `mamba_rms_norm` — [`L487`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L487)
  - `n_groups` — [`L472`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L472)
  - `norm` — [`L534`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L534)
  - `num_heads` — [`L465`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L465)
  - `out_proj` — [`L543`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L543)
  - `param_dtype` — [`L462`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L462)
  - `precision` — [`L463`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L463)
  - `ssm_in_multiplier` — [`L489`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L489)
  - `ssm_op` — [`L558`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L558)
  - `ssm_state_size` — [`L467`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L467)
  - `use_bias` — [`L484`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L484)
  - `use_conv_bias` — [`L481`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L481)
- protocol/private: `_body`[`L654`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L654)
- uses (calls/refs, reference-scoped): [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`partition_manager`](../../infra/base_config.md#EasyDeLBaseConfig.partition_manager), [`ColumnParallelLinear`](../../layers/linears/_linear.md#ColumnParallelLinear), [`RowParallelLinear`](../../layers/linears/_linear.md#RowParallelLinear), [`ACT2FN`](../../infra/utils.md#ACT2FN), [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound), [`attention_outputs`](../../operations/_attention_outputs.md#AttentionOutput.attention_outputs), [`OperationMetadata`](../../operations/_operation_meta.md#OperationMetadata), [`concatenate_to_cache`](../../caching/hybrid/cache.md#HybridCacheView.concatenate_to_cache), [`compute_mup_vector`](modeling_falcon_h1.md#compute_mup_vector), [`HybridCacheView`](../../caching/hybrid/cache.md#HybridCacheView), [`FalconH1Config`](falcon_h1_configuration.md#FalconH1Config), [`recurrent_state`](../../caching/hybrid/cache.md#HybridCacheView.recurrent_state), [`conv_state`](../../caching/hybrid/cache.md#HybridCacheView.conv_state), [`hidden_size`](falcon_h1_configuration.md#FalconH1Config.hidden_size), [`SSM2Op`](../../operations/kernels/ssm2.md#SSM2Op), [`ssm_state`](../../operations/kernels/ssm2.md#SSM2Output.ssm_state), [`bias`](modeling_falcon_h1.md#Conv1D.bias), [`kernel`](modeling_falcon_h1.md#Conv1D.kernel), [`mamba_d_ssm`](falcon_h1_configuration.md#FalconH1Config.mamba_d_ssm), [`_single_step_ssm2_fwd`](../../operations/kernels/ssm2.md#_single_step_ssm2_fwd), [`apply_mask_to_padding_states`](modeling_falcon_h1.md#apply_mask_to_padding_states), [`rms_norm_eps`](falcon_h1_configuration.md#FalconH1Config.rms_norm_eps), [`hidden_act`](falcon_h1_configuration.md#FalconH1Config.hidden_act), [`mamba_expand`](falcon_h1_configuration.md#FalconH1Config.mamba_expand), [`mamba_d_state`](falcon_h1_configuration.md#FalconH1Config.mamba_d_state), [`mamba_n_groups`](falcon_h1_configuration.md#FalconH1Config.mamba_n_groups), [`mamba_n_heads`](falcon_h1_configuration.md#FalconH1Config.mamba_n_heads), [`Conv1D`](modeling_falcon_h1.md#Conv1D), [`FalconH1RMSNormGated`](modeling_falcon_h1.md#FalconH1RMSNormGated), [`mamba_chunk_size`](falcon_h1_configuration.md#FalconH1Config.mamba_chunk_size), [`mamba_conv_bias`](falcon_h1_configuration.md#FalconH1Config.mamba_conv_bias), [`mamba_d_conv`](falcon_h1_configuration.md#FalconH1Config.mamba_d_conv), [`mamba_d_head`](falcon_h1_configuration.md#FalconH1Config.mamba_d_head), [`mamba_norm_before_gate`](falcon_h1_configuration.md#FalconH1Config.mamba_norm_before_gate), [`mamba_proj_bias`](falcon_h1_configuration.md#FalconH1Config.mamba_proj_bias), [`mamba_rms_norm`](falcon_h1_configuration.md#FalconH1Config.mamba_rms_norm), [`projectors_bias`](falcon_h1_configuration.md#FalconH1Config.projectors_bias), [`ssm_in_multiplier`](falcon_h1_configuration.md#FalconH1Config.ssm_in_multiplier)
- used by: [`mamba`](modeling_falcon_h1.md#FalconH1DecoderLayer.mamba)

### `FalconH1Model`  ·  implements/extends EasyDeLBaseModule
- def: [`easydel/modules/falcon_h1/modeling_falcon_h1.py:1098`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1098)
- doc: FalconH1 base model implementing a parallel hybrid Mamba-Attention architecture.
- signature: `class FalconH1Model(EasyDeLBaseModule):`
- members:
  - `__call__(self, input_ids: Array | None = None, attention_mask: Array | None = None, position_ids: Array | None = None, past_key_values: HybridCache | None = None, inputs_embeds: Array | None = None, use_cache: bool | None = None, output_attentions: bool | None = None, output_hidden_states: bool | None = None, mode: common_types.RUNTIME_MODE_TYPES | None = None, mask_info: MaskInfo | None = None, cache_metadata: OperationsMetadata | None = None, **kwargs)` — [`L1191`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1191) — Perform forward pass through the FalconH1 transformer model.
  - `__init__(self, config: FalconH1Config, dtype: jnp.dtype = jnp.bfloat16, param_dtype: jnp.dtype = jnp.bfloat16, precision: jax.lax.PrecisionLike = None, *, rngs: nn.Rngs)` — [`L1127`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1127) — Initialize the FalconH1 base model.
  - `get_decoder(self)` — [`L1332`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1332) — Return the decoder layers of the model.
  - `get_embedding(self)` — [`L1340`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1340) — Return the token embedding layer of the model.
  - `embed_tokens` — [`L1156`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1156)
  - `embedding_multiplier` — [`L1188`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1188)
  - `final_layernorm` — [`L1184`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1184)
  - `layers` — [`L1170`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1170)
  - `lm_head_multiplier` — [`L1189`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L1189)
- uses (calls/refs, reference-scoped): [`config`](../../infra/base_module.md#EasyDeLBaseModule.config), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`TaskType`](../../infra/factory.md#TaskType), [`OperationsMetadata`](../../caching/_abstracts.md#OperationsMetadata), [`HybridCache`](../../caching/hybrid/cache.md#HybridCache), [`register_module`](../../infra/factory.md#register_module), [`RMSNorm`](../../layers/norms/_norms.md#RMSNorm), [`BaseModelOutput`](../../infra/modeling_outputs.md#BaseModelOutput), [`auto_remat`](../../infra/utils.md#auto_remat), [`Embed`](../../layers/embeddings/_embeddings.md#Embed), [`gradient_checkpointing_targets`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing_targets), [`__init__`](../../infra/base_module.md#EasyDeLBaseModule.__init__), [`BASE_MODULE`](../../infra/factory.md#TaskType.BASE_MODULE), [`attention_weight`](../../infra/modeling_outputs.md#DecoderLayerOutput.attention_weight), [`hidden_states`](../../infra/modeling_outputs.md#DecoderLayerOutput.hidden_states), [`cache_view`](../../infra/modeling_outputs.md#DecoderLayerOutput.cache_view), `output_hidden_states`, [`gradient_checkpointing`](../../infra/base_config.md#EasyDeLBaseConfig.gradient_checkpointing), [`FalconH1Config`](falcon_h1_configuration.md#FalconH1Config), [`get_view`](../../caching/hybrid/cache.md#HybridCache.get_view), [`hidden_size`](falcon_h1_configuration.md#FalconH1Config.hidden_size), [`update_view`](../../caching/hybrid/cache.md#HybridCache.update_view), [`rms_norm_eps`](falcon_h1_configuration.md#FalconH1Config.rms_norm_eps), [`num_hidden_layers`](falcon_h1_configuration.md#FalconH1Config.num_hidden_layers), [`FalconH1DecoderLayer`](modeling_falcon_h1.md#FalconH1DecoderLayer), [`embedding_multiplier`](falcon_h1_configuration.md#FalconH1Config.embedding_multiplier), [`lm_head_multiplier`](falcon_h1_configuration.md#FalconH1Config.lm_head_multiplier), [`vocab_size`](falcon_h1_configuration.md#FalconH1Config.vocab_size)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseModule`](../../infra/base_module.md#EasyDeLBaseModule), [`get_embedding`](../../infra/base_module.md#EasyDeLBaseModule.get_embedding), [`get_decoder`](../../infra/base_module.md#EasyDeLBaseModule.get_decoder), [`FalconH1ForCausalLM`](modeling_falcon_h1.md#FalconH1ForCausalLM), [`__init__`](modeling_falcon_h1.md#FalconH1ForCausalLM.__init__), [`make_lm_head_fn`](modeling_falcon_h1.md#FalconH1ForCausalLM.make_lm_head_fn)

### `FalconH1RMSNormGated`  ·  implements/extends Module
- def: [`easydel/modules/falcon_h1/modeling_falcon_h1.py:306`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L306)
- doc: Group RMS normalization with optional SiLU gating for FalconH1 Mamba blocks.
- signature: `class FalconH1RMSNormGated(nn.Module):`
- members:
  - `__call__(self, hidden_states: Array, gate: Array | None = None)` — [`L364`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L364) — Apply grouped RMS normalization with optional SiLU gating.
  - `__init__(self, hidden_size: int, eps: float, *, rngs: nn.Rngs, n_groups: int = 1, norm_before_gate: bool = True, dtype: jnp.dtype = jnp.float32)` — [`L325`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L325) — Initialize the gated group RMS normalization layer.
  - `craft_sharding(self, *, partition_manager=None, **_kwargs)` — [`L360`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L360) — Return sharding specs for normalization parameters.
  - `dtype` — [`L352`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L352)
  - `hidden_size` — [`L348`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L348)
  - `kernel` — [`L353`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L353)
  - `n_groups` — [`L350`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L350)
  - `norm_before_gate` — [`L351`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L351)
  - `variance_epsilon` — [`L349`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L349)
- uses (calls/refs, reference-scoped): [`ArrayParam`](../../infra/utils.md#ArrayParam), [`bound`](../../infra/utils.md#ArrayParam.bound)
- used by: [`norm`](modeling_falcon_h1.md#FalconH1Mixer.norm)

## Functions
- `apply_mask_to_padding_states(hidden_states: Array, attention_mask: Array | None)` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L89) — Apply attention mask to zero out hidden states at padding positions.
- `compute_mup_vector(config: FalconH1Config)` — [`L48`](../../../../../../../raw/code/EasyDeL/easydel/modules/falcon_h1/modeling_falcon_h1.py#L48) — Compute the muP (maximal update parameterization) scaling vector for FalconH1 SSM.

