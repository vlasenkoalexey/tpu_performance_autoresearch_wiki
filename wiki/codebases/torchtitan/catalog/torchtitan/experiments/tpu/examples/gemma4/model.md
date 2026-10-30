---
title: 'Module: torchtitan/experiments/tpu/examples/gemma4/model.py'
type: catalog
provenance: extracted
module: torchtitan/experiments/tpu/examples/gemma4/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.experiments.tpu.examples.gemma4.model`/
symbols:
  Gemma4Model.Config.get_nparams_and_flops: Gemma4Model#Config#get_nparams_and_flops().
  Gemma4Model.Config.update_from_config: Gemma4Model#Config#update_from_config().
  Gemma4TransformerBlock.forward: Gemma4TransformerBlock#forward().
  Gemma4Model.get_attention_masks: Gemma4Model#get_attention_masks().
  Gemma4Attention.__init__: Gemma4Attention#__init__().
  Gemma4Attention.forward: Gemma4Attention#forward().
  Gemma4TransformerBlock.post_feedforward_layernorm_2: Gemma4TransformerBlock#post_feedforward_layernorm_2.
  Gemma4Model: Gemma4Model#
  Gemma4Model.Config: Gemma4Model#Config#
  Gemma4MoE.forward: Gemma4MoE#forward().
  Gemma4TransformerBlock.Config.moe: Gemma4TransformerBlock#Config#moe.
  Gemma4RoPE._precompute_cache: Gemma4RoPE#_precompute_cache().
  SlidingWindowScaledDotProductAttention.forward: SlidingWindowScaledDotProductAttention#forward().
  Gemma4Router.forward: Gemma4Router#forward().
  Gemma4Embedding.Config: Gemma4Embedding#Config#
  Gemma4Attention.Config: Gemma4Attention#Config#
  Gemma4Attention: Gemma4Attention#
  Gemma4TransformerBlock.Config: Gemma4TransformerBlock#Config#
  Gemma4MoE.Config.pre_feedforward_layernorm_2: Gemma4MoE#Config#pre_feedforward_layernorm_2.
  Gemma4TransformerBlock.Config.post_feedforward_layernorm_1: Gemma4TransformerBlock#Config#post_feedforward_layernorm_1.
  Gemma4TransformerBlock.Config.post_feedforward_layernorm_2: Gemma4TransformerBlock#Config#post_feedforward_layernorm_2.
  Gemma4Embedding: Gemma4Embedding#
  Gemma4TransformerBlock: Gemma4TransformerBlock#
  Gemma4Attention.Config.v_norm: Gemma4Attention#Config#v_norm.
  Gemma4MoE.Config: Gemma4MoE#Config#
  Gemma4Attention.scaling: Gemma4Attention#scaling.
  Gemma4TransformerBlock.post_feedforward_layernorm: Gemma4TransformerBlock#post_feedforward_layernorm.
  Gemma4RoPE.Config: Gemma4RoPE#Config#
  QKVLinearKeqV.Config: QKVLinearKeqV#Config#
  Gemma4Attention.Config.sliding_window_size: Gemma4Attention#Config#sliding_window_size.
  Gemma4Router.Config: Gemma4Router#Config#
  Gemma4Router.Config.norm: Gemma4Router#Config#norm.
  Gemma4TransformerBlock.Config.post_attention_layernorm: Gemma4TransformerBlock#Config#post_attention_layernorm.
  Gemma4TransformerBlock.Config.post_feedforward_layernorm: Gemma4TransformerBlock#Config#post_feedforward_layernorm.
  Gemma4Model.Config.vocab_size: Gemma4Model#Config#vocab_size.
  Gemma4RoPE.__init__: Gemma4RoPE#__init__().
  QKVLinearKeqV.__init__: QKVLinearKeqV#__init__().
  QKVLinearKeqV.forward: QKVLinearKeqV#forward().
  Gemma4FeedForward.forward: Gemma4FeedForward#forward().
  Gemma4MoE: Gemma4MoE#
  QKVLinearKeqV.local_qkv_head_split: QKVLinearKeqV#local_qkv_head_split().
  SlidingWindowScaledDotProductAttention.Config: SlidingWindowScaledDotProductAttention#Config#
  Gemma4MoE.pre_feedforward_layernorm_2: Gemma4MoE#pre_feedforward_layernorm_2.
  Gemma4Model.Config.enable_weight_tying: Gemma4Model#Config#enable_weight_tying.
  Gemma4RoPE: Gemma4RoPE#
  SlidingWindowScaledDotProductAttention: SlidingWindowScaledDotProductAttention#
  Gemma4Router: Gemma4Router#
  QKVLinearKeqV.wq: QKVLinearKeqV#wq.
  QKVLinearKeqV.wk: QKVLinearKeqV#wk.
  Gemma4Attention.Config.is_sliding: Gemma4Attention#Config#is_sliding.
  Gemma4Attention.v_norm: Gemma4Attention#v_norm.
  Gemma4FeedForward.Config: Gemma4FeedForward#Config#
  Gemma4Router.norm: Gemma4Router#norm.
  Gemma4TransformerBlock.attention: Gemma4TransformerBlock#attention.
  Gemma4TransformerBlock.attention_norm: Gemma4TransformerBlock#attention_norm.
  Gemma4TransformerBlock.post_attention_layernorm: Gemma4TransformerBlock#post_attention_layernorm.
  Gemma4TransformerBlock.ffn_norm: Gemma4TransformerBlock#ffn_norm.
  Gemma4TransformerBlock.feed_forward: Gemma4TransformerBlock#feed_forward.
  QKVLinearKeqV: QKVLinearKeqV#
  Gemma4TransformerBlock.moe: Gemma4TransformerBlock#moe.
  Gemma4TransformerBlock.post_feedforward_layernorm_1: Gemma4TransformerBlock#post_feedforward_layernorm_1.
  Gemma4TransformerBlock.layer_scalar: Gemma4TransformerBlock#layer_scalar.
  Gemma4Embedding.__init__: Gemma4Embedding#__init__().
  Gemma4Embedding.forward: Gemma4Embedding#forward().
  SlidingWindowScaledDotProductAttention.__init__: SlidingWindowScaledDotProductAttention#__init__().
  Gemma4Router.__init__: Gemma4Router#__init__().
  Gemma4MoE.__init__: Gemma4MoE#__init__().
  Gemma4Model.Config.sliding_window_size: Gemma4Model#Config#sliding_window_size.
  Gemma4Model.__init__: Gemma4Model#__init__().
  Gemma4Attention.is_sliding: Gemma4Attention#is_sliding.
  Gemma4Attention.sliding_window_size: Gemma4Attention#sliding_window_size.
  Gemma4FeedForward: Gemma4FeedForward#
  Gemma4Router.per_expert_scale: Gemma4Router#per_expert_scale.
  Gemma4TransformerBlock.moe_enabled: Gemma4TransformerBlock#moe_enabled.
  Gemma4Router.Config.dim: Gemma4Router#Config#dim.
  Gemma4Embedding.embed_scale: Gemma4Embedding#embed_scale.
  Gemma4Router.root_size: Gemma4Router#root_size.
  Gemma4Router.scale: Gemma4Router#scale.
  Gemma4Model.sliding_window_size: Gemma4Model#sliding_window_size.
  Gemma4Model.Config.dim: Gemma4Model#Config#dim.
  Gemma4Router.dim: Gemma4Router#dim.
  Gemma4TransformerBlock.__init__: Gemma4TransformerBlock#__init__().
  Gemma4TransformerBlock._init_self_buffers: Gemma4TransformerBlock#_init_self_buffers().
  Gemma4RoPE.Config.partial_rotary_factor: Gemma4RoPE#Config#partial_rotary_factor.
  SlidingWindowScaledDotProductAttention.sliding_window_size: SlidingWindowScaledDotProductAttention#sliding_window_size.
  Gemma4RoPE.partial_rotary_factor: Gemma4RoPE#partial_rotary_factor.
  __all__: __all__.
---
# Module: [`torchtitan/experiments/tpu/examples/gemma4/model.py`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py)

## Classes
### <a id="Gemma4Attention"></a>`Gemma4Attention`  ·  implements/extends GQAttention
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:216`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L216)
- doc: Gemma4 attention supporting hybrid sliding/global layers, K=V, and Q/K/V norms.
- signature: `class Gemma4Attention(GQAttention):`
- members:
  - <a id="Gemma4Attention.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None, segment_ids: torch.Tensor | None = None)` — [`L253`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L253)
  - <a id="Gemma4Attention.is_sliding"></a>`is_sliding` — [`L242`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L242)
  - <a id="Gemma4Attention.scaling"></a>`scaling` — [`L245`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L245)
  - <a id="Gemma4Attention.sliding_window_size"></a>`sliding_window_size` — [`L243`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L243)
  - <a id="Gemma4Attention.v_norm"></a>`v_norm` — [`L241`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L241)
- protocol/private: <a id="Gemma4Attention.__init__"></a>`__init__`[`L225`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L225)
- uses (calls/refs, reference-scoped): [`build`](../../../../protocols/module.md#Module.Config.build), [`param_init`](../../../../protocols/module.md#Module.Config.param_init), [`sharding_config`](../../../../protocols/module.md#Module.Config.sharding_config), [`ScaledDotProductInnerAttention`](../../../../models/common/attention.md#ScaledDotProductInnerAttention), [`AttentionMasksType`](../../../../models/common/attention.md#AttentionMasksType), [`GQAttention`](../../../../models/common/attention.md#GQAttention), [`k_norm`](../../../../models/common/attention.md#GQAttention.k_norm), [`Config`](../../../../models/common/attention.md#ScaledDotProductInnerAttention.Config), [`rope`](../../../../models/common/attention.md#GQAttention.rope), [`inner_attention`](../../../../models/common/attention.md#GQAttention.Config.inner_attention), [`q_norm`](../../../../models/common/attention.md#GQAttention.q_norm), [`inner_attention`](../../../../models/common/attention.md#GQAttention.inner_attention), [`qkv_linear`](../../../../models/common/attention.md#GQAttention.qkv_linear), [`enable_gqa`](../../../../models/common/attention.md#GQAttention.enable_gqa), [`wo`](../../../../models/common/attention.md#GQAttention.wo), [`__init__`](../../../../models/common/attention.md#GQAttention.__init__)  (6 test-only)
- used by: [`GQAttention`](../../../../models/common/attention.md#GQAttention), [`forward`](../../../../models/common/attention.md#GQAttention.forward)  (5 test-only)

### <a id="Gemma4Attention.Config"></a>`Gemma4Attention.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:220`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L220)
- signature: `class Config(GQAttention.Config):`
- members:
  - <a id="Gemma4Attention.Config.is_sliding"></a>`is_sliding` — [`L222`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L222)
  - <a id="Gemma4Attention.Config.sliding_window_size"></a>`sliding_window_size` — [`L223`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L223)
  - <a id="Gemma4Attention.Config.v_norm"></a>`v_norm` — [`L221`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L221)
- uses (calls/refs, reference-scoped): [`RMSNorm`](../../../../models/common/nn_modules.md#RMSNorm), [`Config`](../../../../models/common/nn_modules.md#RMSNorm.Config), [`GQAttention`](../../../../models/common/attention.md#GQAttention), [`Config`](../../../../models/common/attention.md#GQAttention.Config)
- used by: (9 test-only callers)

### <a id="Gemma4Embedding"></a>`Gemma4Embedding`  ·  implements/extends Embedding
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:35`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L35)
- doc: Token embedding scaled by `sqrt(embedding_dim)` as in Gemma models.
- signature: `class Gemma4Embedding(Embedding):`
- members:
  - <a id="Gemma4Embedding.forward"></a>`forward(self, input: torch.Tensor)` — [`L46`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L46)
  - <a id="Gemma4Embedding.embed_scale"></a>`embed_scale` — [`L44`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L44)
- protocol/private: <a id="Gemma4Embedding.__init__"></a>`__init__`[`L42`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L42)
- uses (calls/refs, reference-scoped): [`Embedding`](../../../../models/common/embedding.md#Embedding), [`embedding_dim`](../../../../models/common/embedding.md#Embedding.Config.embedding_dim), [`__init__`](../../../../models/common/embedding.md#Embedding.__init__), [`forward`](../../../../models/common/embedding.md#Embedding.forward)  (1 test-only)
- used by: [`Embedding`](../../../../models/common/embedding.md#Embedding), [`forward`](../../../../models/common/embedding.md#Embedding.forward)  (3 test-only)

### <a id="Gemma4Embedding.Config"></a>`Gemma4Embedding.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:39`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L39)
- signature: `class Config(Embedding.Config):`
- uses (calls/refs, reference-scoped): [`Embedding`](../../../../models/common/embedding.md#Embedding), [`Config`](../../../../models/common/embedding.md#Embedding.Config)
- used by: (4 test-only callers)

### <a id="Gemma4FeedForward"></a>`Gemma4FeedForward`  ·  implements/extends FeedForward
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:295`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L295)
- doc: GeGLU feed-forward network (GELU with tanh approximation).
- signature: `class Gemma4FeedForward(FeedForward):`
- members:
  - <a id="Gemma4FeedForward.forward"></a>`forward(self, x: torch.Tensor)` — [`L302`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L302)
- uses (calls/refs, reference-scoped): [`FeedForward`](../../../../models/common/feed_forward.md#FeedForward), [`w2`](../../../../models/common/feed_forward.md#FeedForward.w2), [`w1`](../../../../models/common/feed_forward.md#FeedForward.w1), [`w3`](../../../../models/common/feed_forward.md#FeedForward.w3)
- used by: [`FeedForward`](../../../../models/common/feed_forward.md#FeedForward), [`forward`](../../../../models/common/feed_forward.md#FeedForward.forward)  (1 test-only)

### <a id="Gemma4FeedForward.Config"></a>`Gemma4FeedForward.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:299`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L299)
- signature: `class Config(FeedForward.Config):`
- uses (calls/refs, reference-scoped): [`FeedForward`](../../../../models/common/feed_forward.md#FeedForward), [`Config`](../../../../models/common/feed_forward.md#FeedForward.Config)
- used by: (1 test-only callers)

### <a id="Gemma4MoE"></a>`Gemma4MoE`  ·  implements/extends MoE
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:344`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L344)
- doc: Gemma4 MoE module applying `pre_feedforward_layernorm_2` to expert inputs while routing on residual `x_TD`.
- signature: `class Gemma4MoE(MoE):`
- members:
  - <a id="Gemma4MoE.forward"></a>`forward(self, x_TD: torch.Tensor, **router_kwargs)` — [`L359`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L359)
  - <a id="Gemma4MoE.pre_feedforward_layernorm_2"></a>`pre_feedforward_layernorm_2` — [`L353`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L353)
- protocol/private: <a id="Gemma4MoE.__init__"></a>`__init__`[`L351`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L351)
- uses (calls/refs, reference-scoped): [`build`](../../../../protocols/module.md#Module.Config.build), [`MoE`](../../../../models/common/moe.md#MoE), [`routed_experts`](../../../../models/common/moe.md#MoE.routed_experts), [`router`](../../../../models/common/moe.md#MoE.router), [`shared_experts`](../../../../models/common/moe.md#MoE.shared_experts), [`__init__`](../../../../models/common/moe.md#MoE.__init__), [`tokens_per_expert_E`](../../../../models/common/moe.md#MoE.tokens_per_expert_E), [`_tokens_per_expert`](../../../../models/common/moe.md#_tokens_per_expert), [`expert_bias_E`](../../../../models/common/moe.md#MoE.expert_bias_E)  (2 test-only)
- used by: [`MoE`](../../../../models/common/moe.md#MoE), [`forward`](../../../../models/common/moe.md#MoE.forward)  (3 test-only)

### <a id="Gemma4MoE.Config"></a>`Gemma4MoE.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:348`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L348)
- signature: `class Config(MoE.Config):`
- members:
  - <a id="Gemma4MoE.Config.pre_feedforward_layernorm_2"></a>`pre_feedforward_layernorm_2` — [`L349`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L349)
- uses (calls/refs, reference-scoped): [`RMSNorm`](../../../../models/common/nn_modules.md#RMSNorm), [`Config`](../../../../models/common/nn_modules.md#RMSNorm.Config), [`MoE`](../../../../models/common/moe.md#MoE), [`Config`](../../../../models/common/moe.md#MoE.Config)
- used by: (5 test-only callers)

### <a id="Gemma4Model"></a>`Gemma4Model`  ·  implements/extends Decoder
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:478`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L478)
- doc: Gemma4 text decoder model supporting hybrid sliding/global attention and dense/MoE blocks.
- signature: `class Gemma4Model(Decoder):`
- members:
  - <a id="Gemma4Model.get_attention_masks"></a>`get_attention_masks(self, positions: torch.Tensor, *, padding_mask: torch.Tensor | None = None, max_num_documents: int | None = None, max_context_length: int | None = None)` — [`L680`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L680)
  - <a id="Gemma4Model.sliding_window_size"></a>`sliding_window_size` — [`L678`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L678)
- protocol/private: <a id="Gemma4Model.__init__"></a>`__init__`[`L676`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L676)
- uses (calls/refs, reference-scoped): [`FlexInnerAttention`](../../../../models/common/attention.md#FlexInnerAttention), [`Decoder`](../../../../models/common/decoder.md#Decoder), [`AttentionMasksType`](../../../../models/common/attention.md#AttentionMasksType), [`get_attention_masks`](../../../../models/common/decoder.md#Decoder.get_attention_masks), [`Config`](../../../../models/common/attention.md#FlexInnerAttention.Config), [`get_causal_mask_mod`](../../../../models/common/attention.md#get_causal_mask_mod), [`_create_flex_attention_mask`](../../../../models/common/decoder.md#Decoder._create_flex_attention_mask), [`config`](../../../../models/common/decoder.md#Decoder.config), [`inner_attention`](../../../../models/common/attention.md#BaseAttention.Config.inner_attention), [`first_attention`](../../../../models/common/decoder.md#Decoder.Config.first_attention), [`get_sliding_window_mask_mod`](../../../../models/common/attention.md#get_sliding_window_mask_mod), [`get_efficient_causal_mask_mod_for_packed_document`](../../../../models/common/attention.md#get_efficient_causal_mask_mod_for_packed_document), [`__init__`](../../../../models/common/decoder.md#Decoder.__init__)  (2 test-only)
- used by: [`Decoder`](../../../../models/common/decoder.md#Decoder), [`get_attention_masks`](../../../../models/common/decoder.md#Decoder.get_attention_masks)  (10 test-only)

### <a id="Gemma4Model.Config"></a>`Gemma4Model.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:482`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L482)
- signature: `class Config(Decoder.Config):`
- members:
  - <a id="Gemma4Model.Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L615`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L615) — Parameter count and MaxText-style training FLOPs per token.
  - <a id="Gemma4Model.Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L488`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L488)
  - <a id="Gemma4Model.Config.dim"></a>`dim` — [`L483`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L483)
  - <a id="Gemma4Model.Config.enable_weight_tying"></a>`enable_weight_tying` — [`L485`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L485)
  - <a id="Gemma4Model.Config.sliding_window_size"></a>`sliding_window_size` — [`L486`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L486)
  - <a id="Gemma4Model.Config.vocab_size"></a>`vocab_size` — [`L484`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L484)
- uses (calls/refs, reference-scoped): [`logger`](../../../../tools/logging.md#logger), [`out_features`](../../../../models/common/linear.md#Linear.Config.out_features), [`layers`](../../../../models/common/decoder.md#Decoder.Config.layers), [`FlexInnerAttention`](../../../../models/common/attention.md#FlexInnerAttention), [`Decoder`](../../../../models/common/decoder.md#Decoder), [`MoE`](../../../../models/common/moe.md#MoE), [`VarlenInnerAttention`](../../../../models/common/attention.md#VarlenInnerAttention), [`update_from_config`](../../../../models/common/decoder.md#Decoder.Config.update_from_config), [`FeedForward`](../../../../models/common/feed_forward.md#FeedForward), [`feed_forward`](../../../../models/common/decoder.md#TransformerBlock.Config.feed_forward), [`Config`](../../../../models/common/attention.md#FlexInnerAttention.Config), [`Config`](../../../../models/common/decoder.md#Decoder.Config), [`Config`](../../../../models/common/moe.md#MoE.Config), [`attention`](../../../../models/common/decoder.md#TransformerBlock.Config.attention), [`Config`](../../../../models/common/attention.md#VarlenInnerAttention.Config), [`hidden_dim`](../../../../models/common/moe.md#GroupedExperts.Config.hidden_dim), [`Config`](../../../../models/common/feed_forward.md#FeedForward.Config), [`inner_attention`](../../../../models/common/attention.md#GQAttention.Config.inner_attention), [`w1`](../../../../models/common/feed_forward.md#FeedForward.Config.w1), [`router`](../../../../models/common/moe.md#MoE.Config.router), [`inner_experts`](../../../../models/common/moe.md#RoutedExperts.Config.inner_experts), [`n_heads`](../../../../models/common/attention.md#GQAttention.Config.n_heads), [`routed_experts`](../../../../models/common/moe.md#MoE.Config.routed_experts), [`n_kv_heads`](../../../../models/common/attention.md#GQAttention.Config.n_kv_heads), [`num_experts`](../../../../models/common/moe.md#MoE.Config.num_experts), [`qkv_linear`](../../../../models/common/attention.md#GQAttention.Config.qkv_linear), [`update_moe_aux_loss_configs`](../../../../models/common/config_utils.md#update_moe_aux_loss_configs), [`head_dim`](../../../../models/common/attention.md#GQAttention.Config.head_dim), [`top_k`](../../../../models/common/moe.md#TokenChoiceTopKRouter.Config.top_k), [`moe_load_balance_aux_loss_configs`](../../../../models/common/config_utils.md#moe_load_balance_aux_loss_configs), [`block_size`](../../../../models/common/attention.md#FlexInnerAttention.Config.block_size), [`window_size`](../../../../models/common/attention.md#VarlenInnerAttention.Config.window_size), [`_debug_force_load_balance`](../../../../models/common/moe.md#TokenChoiceTopKRouter.Config._debug_force_load_balance)  (10 test-only)
- used by: (18 test-only callers)

### <a id="Gemma4RoPE"></a>`Gemma4RoPE`  ·  implements/extends CosSinRoPE
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:50`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L50)
- doc: RoPE with optional proportional rotary factor for Gemma4 global layers.
- signature: `class Gemma4RoPE(CosSinRoPE):`
- members:
  - <a id="Gemma4RoPE.partial_rotary_factor"></a>`partial_rotary_factor` — [`L58`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L58)
- protocol/private: <a id="Gemma4RoPE.__init__"></a>`__init__`[`L57`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L57), <a id="Gemma4RoPE._precompute_cache"></a>`_precompute_cache`[`L61`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L61)
- uses (calls/refs, reference-scoped): [`CosSinRoPE`](../../../../models/common/rope.md#CosSinRoPE), [`dim`](../../../../models/common/rope.md#RoPE.Config.dim), [`max_context_length`](../../../../models/common/rope.md#RoPE.Config.max_context_length), [`theta`](../../../../models/common/rope.md#RoPE.Config.theta), [`scaling`](../../../../models/common/rope.md#RoPE.Config.scaling), [`config`](../../../../models/common/rope.md#RoPE.config), [`__init__`](../../../../models/common/rope.md#RoPE.__init__)  (2 test-only)
- used by: [`CosSinRoPE`](../../../../models/common/rope.md#CosSinRoPE), [`_precompute_cache`](../../../../models/common/rope.md#CosSinRoPE._precompute_cache)  (2 test-only)

### <a id="Gemma4RoPE.Config"></a>`Gemma4RoPE.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:54`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L54)
- signature: `class Config(CosSinRoPE.Config):`
- members:
  - <a id="Gemma4RoPE.Config.partial_rotary_factor"></a>`partial_rotary_factor` — [`L55`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L55)
- uses (calls/refs, reference-scoped): [`CosSinRoPE`](../../../../models/common/rope.md#CosSinRoPE), [`Config`](../../../../models/common/rope.md#CosSinRoPE.Config)
- used by: (3 test-only callers)

### <a id="Gemma4Router"></a>`Gemma4Router`  ·  implements/extends TokenChoiceTopKRouter
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:306`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L306)
- doc: Gemma4 top-k router with input RMSNorm, learned input scale, and per-expert scale.
- signature: `class Gemma4Router(TokenChoiceTopKRouter):`
- members:
  - <a id="Gemma4Router.forward"></a>`forward(self, x_TD: torch.Tensor, expert_bias_E: torch.Tensor | None = None, **router_kwargs)` — [`L322`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L322)
  - <a id="Gemma4Router.dim"></a>`dim` — [`L316`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L316)
  - <a id="Gemma4Router.norm"></a>`norm` — [`L318`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L318)
  - <a id="Gemma4Router.per_expert_scale"></a>`per_expert_scale` — [`L320`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L320)
  - <a id="Gemma4Router.root_size"></a>`root_size` — [`L317`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L317)
  - <a id="Gemma4Router.scale"></a>`scale` — [`L319`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L319)
- protocol/private: <a id="Gemma4Router.__init__"></a>`__init__`[`L314`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L314)
- uses (calls/refs, reference-scoped): [`build`](../../../../protocols/module.md#Module.Config.build), [`forward`](../../../../models/common/moe.md#TokenChoiceTopKRouter.forward), [`TokenChoiceTopKRouter`](../../../../models/common/moe.md#TokenChoiceTopKRouter), [`num_experts`](../../../../models/common/moe.md#TokenChoiceTopKRouter.Config.num_experts), [`__init__`](../../../../models/common/moe.md#TokenChoiceTopKRouter.__init__)  (3 test-only)
- used by: [`forward`](../../../../models/common/moe.md#TokenChoiceTopKRouter.forward), [`TokenChoiceTopKRouter`](../../../../models/common/moe.md#TokenChoiceTopKRouter)  (2 test-only)

### <a id="Gemma4Router.Config"></a>`Gemma4Router.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:310`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L310)
- signature: `class Config(TokenChoiceTopKRouter.Config):`
- members:
  - <a id="Gemma4Router.Config.dim"></a>`dim` — [`L311`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L311)
  - <a id="Gemma4Router.Config.norm"></a>`norm` — [`L312`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L312)
- uses (calls/refs, reference-scoped): [`RMSNorm`](../../../../models/common/nn_modules.md#RMSNorm), [`Config`](../../../../models/common/nn_modules.md#RMSNorm.Config), [`TokenChoiceTopKRouter`](../../../../models/common/moe.md#TokenChoiceTopKRouter), [`Config`](../../../../models/common/moe.md#TokenChoiceTopKRouter.Config)
- used by: (7 test-only callers)

### <a id="Gemma4TransformerBlock"></a>`Gemma4TransformerBlock`  ·  implements/extends TransformerBlock
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:400`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L400)
- doc: Gemma4 Transformer block with pre/post norms, layer_scalar, and parallel dense + MoE FFN.
- signature: `class Gemma4TransformerBlock(TransformerBlock):`
- members:
  - <a id="Gemma4TransformerBlock.forward"></a>`forward(self, x: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None, segment_ids: torch.Tensor | None = None)` — [`L448`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L448)
  - <a id="Gemma4TransformerBlock.attention"></a>`attention` — [`L413`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L413)
  - <a id="Gemma4TransformerBlock.attention_norm"></a>`attention_norm` — [`L414`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L414)
  - <a id="Gemma4TransformerBlock.feed_forward"></a>`feed_forward` — [`L420`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L420)
  - <a id="Gemma4TransformerBlock.ffn_norm"></a>`ffn_norm` — [`L417`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L417)
  - <a id="Gemma4TransformerBlock.layer_scalar"></a>`layer_scalar` — [`L444`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L444)
  - <a id="Gemma4TransformerBlock.moe"></a>`moe` — [`L423`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L423)
  - <a id="Gemma4TransformerBlock.moe_enabled"></a>`moe_enabled` — [`L422`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L422)
  - <a id="Gemma4TransformerBlock.post_attention_layernorm"></a>`post_attention_layernorm` — [`L415`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L415)
  - <a id="Gemma4TransformerBlock.post_feedforward_layernorm"></a>`post_feedforward_layernorm` — [`L418`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L418)
  - <a id="Gemma4TransformerBlock.post_feedforward_layernorm_1"></a>`post_feedforward_layernorm_1` — [`L424`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L424)
  - <a id="Gemma4TransformerBlock.post_feedforward_layernorm_2"></a>`post_feedforward_layernorm_2` — [`L425`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L425)
- protocol/private: <a id="Gemma4TransformerBlock.__init__"></a>`__init__`[`L411`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L411), <a id="Gemma4TransformerBlock._init_self_buffers"></a>`_init_self_buffers`[`L440`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L440)
- uses (calls/refs, reference-scoped): [`build`](../../../../protocols/module.md#Module.Config.build), [`RMSNorm`](../../../../models/common/nn_modules.md#RMSNorm), [`TransformerBlock`](../../../../models/common/decoder.md#TransformerBlock), [`AttentionMasksType`](../../../../models/common/attention.md#AttentionMasksType), [`feed_forward`](../../../../models/common/decoder.md#TransformerBlock.Config.feed_forward), [`attention`](../../../../models/common/decoder.md#TransformerBlock.Config.attention), [`attention_norm`](../../../../models/common/decoder.md#TransformerBlock.Config.attention_norm), [`ffn_norm`](../../../../models/common/decoder.md#TransformerBlock.Config.ffn_norm)  (7 test-only)
- used by: [`TransformerBlock`](../../../../models/common/decoder.md#TransformerBlock), [`_init_self_buffers`](../../../../protocols/module.md#Module._init_self_buffers)  (4 test-only)

### <a id="Gemma4TransformerBlock.Config"></a>`Gemma4TransformerBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:404`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L404)
- signature: `class Config(TransformerBlock.Config):`
- members:
  - <a id="Gemma4TransformerBlock.Config.moe"></a>`moe` — [`L407`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L407)
  - <a id="Gemma4TransformerBlock.Config.post_attention_layernorm"></a>`post_attention_layernorm` — [`L405`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L405)
  - <a id="Gemma4TransformerBlock.Config.post_feedforward_layernorm"></a>`post_feedforward_layernorm` — [`L406`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L406)
  - <a id="Gemma4TransformerBlock.Config.post_feedforward_layernorm_1"></a>`post_feedforward_layernorm_1` — [`L408`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L408)
  - <a id="Gemma4TransformerBlock.Config.post_feedforward_layernorm_2"></a>`post_feedforward_layernorm_2` — [`L409`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L409)
- uses (calls/refs, reference-scoped): [`RMSNorm`](../../../../models/common/nn_modules.md#RMSNorm), [`Config`](../../../../models/common/nn_modules.md#RMSNorm.Config), [`TransformerBlock`](../../../../models/common/decoder.md#TransformerBlock), [`Config`](../../../../models/common/decoder.md#TransformerBlock.Config)  (2 test-only)
- used by: (9 test-only callers)

### <a id="QKVLinearKeqV"></a>`QKVLinearKeqV`  ·  implements/extends QKVLinear
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:92`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L92)
- doc: Two separate linear projections for Q and K, reusing K as V (global K=V layers).
- signature: `class QKVLinearKeqV(QKVLinear):`
- members:
  - <a id="QKVLinearKeqV.forward"></a>`forward(self, x: torch.Tensor)` — [`L105`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L105)
  - <a id="QKVLinearKeqV.local_qkv_head_split"></a>`local_qkv_head_split(tensor: torch.Tensor)` — [`L111`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L111)
  - <a id="QKVLinearKeqV.wk"></a>`wk` — [`L103`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L103)
  - <a id="QKVLinearKeqV.wq"></a>`wq` — [`L102`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L102)
- protocol/private: <a id="QKVLinearKeqV.__init__"></a>`__init__`[`L99`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L99)
- uses (calls/refs, reference-scoped): [`build`](../../../../protocols/module.md#Module.Config.build), [`get_spmd_backend`](../../../../distributed/utils.md#get_spmd_backend), [`QKVLinear`](../../../../models/common/attention.md#QKVLinear), [`wkv`](../../../../models/common/attention.md#QKVLinear.Config.wkv), [`wq`](../../../../models/common/attention.md#QKVLinear.Config.wq), [`head_dim`](../../../../models/common/attention.md#BaseQKVLinear.head_dim), [`__init__`](../../../../models/common/attention.md#BaseQKVLinear.__init__)  (1 test-only)
- used by: [`QKVLinear`](../../../../models/common/attention.md#QKVLinear), [`forward`](../../../../models/common/attention.md#QKVLinear.forward)  (2 test-only)

### <a id="QKVLinearKeqV.Config"></a>`QKVLinearKeqV.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:96`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L96)
- signature: `class Config(QKVLinear.Config):`
- uses (calls/refs, reference-scoped): [`QKVLinear`](../../../../models/common/attention.md#QKVLinear), [`Config`](../../../../models/common/attention.md#QKVLinear.Config)
- used by: (3 test-only callers)

### <a id="SlidingWindowScaledDotProductAttention"></a>`SlidingWindowScaledDotProductAttention`  ·  implements/extends ScaledDotProductInnerAttention
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:127`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L127) — documented in [tpu-context-parallel-attention](../../../../../../concepts/tpu-context-parallel-attention.md)
- doc: `ScaledDotProductInnerAttention` that honors `sliding_window_size`.
- signature: `class SlidingWindowScaledDotProductAttention(ScaledDotProductInnerAttention):`
- members:
  - <a id="SlidingWindowScaledDotProductAttention.forward"></a>`forward(self, q_BLHK: torch.Tensor, k_BLHK: torch.Tensor, v_BLHV: torch.Tensor, *, attention_masks: AttentionMasksType | None = None, scale: float | None = None, enable_gqa: bool = False, is_causal: bool = True, **kwargs)` — [`L146`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L146)
  - <a id="SlidingWindowScaledDotProductAttention.sliding_window_size"></a>`sliding_window_size` — [`L144`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L144)
- protocol/private: <a id="SlidingWindowScaledDotProductAttention.__init__"></a>`__init__`[`L142`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L142)
- uses (calls/refs, reference-scoped): [`ScaledDotProductInnerAttention`](../../../../models/common/attention.md#ScaledDotProductInnerAttention), [`AttentionMasksType`](../../../../models/common/attention.md#AttentionMasksType), [`forward`](../../../../models/common/attention.md#ScaledDotProductInnerAttention.forward), [`get_unflatten_seq_len`](../../unflatten_shim.md#get_unflatten_seq_len), [`__init__`](../../../../models/common/attention.md#ScaledDotProductInnerAttention.__init__), [`sdpa_backends`](../../../../models/common/attention.md#ScaledDotProductInnerAttention.sdpa_backends)  (1 test-only)
- used by: [`ScaledDotProductInnerAttention`](../../../../models/common/attention.md#ScaledDotProductInnerAttention), [`forward`](../../../../models/common/attention.md#ScaledDotProductInnerAttention.forward)  (3 test-only)

### <a id="SlidingWindowScaledDotProductAttention.Config"></a>`SlidingWindowScaledDotProductAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/experiments/tpu/examples/gemma4/model.py:139`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L139)
- signature: `class Config(ScaledDotProductInnerAttention.Config):`
- uses (calls/refs, reference-scoped): [`ScaledDotProductInnerAttention`](../../../../models/common/attention.md#ScaledDotProductInnerAttention), [`Config`](../../../../models/common/attention.md#ScaledDotProductInnerAttention.Config)
- used by: (2 test-only callers)

## Module values
- <a id="__all__"></a>`__all__` — [`L722`](../../../../../../../../../raw/code/torchtitan/torchtitan/experiments/tpu/examples/gemma4/model.py#L722)

