---
title: 'Module: torchtitan/models/gpt_oss/model.py'
type: catalog
provenance: extracted
module: torchtitan/models/gpt_oss/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.gpt_oss.model`/
symbols:
  GptOssModel.get_attention_masks: GptOssModel#get_attention_masks().
  GptOssModel: GptOssModel#
  Attention.forward: Attention#forward().
  GptOssTransformerBlock.forward: GptOssTransformerBlock#forward().
  Attention.softmax_scale: Attention#softmax_scale.
  Attention.Config.inner_attention: Attention#Config#inner_attention.
  GptOssModel.Config: GptOssModel#Config#
  Attention: Attention#
  Attention.Config: Attention#Config#
  Attention.Config.rope: Attention#Config#rope.
  GptOssTransformerBlock.__init__: GptOssTransformerBlock#__init__().
  GptOssModel.Config.update_from_config: GptOssModel#Config#update_from_config().
  GptOssTransformerBlock.ffn_norm: GptOssTransformerBlock#ffn_norm.
  Attention.Config.qkv_linear: Attention#Config#qkv_linear.
  Attention.Config.wo: Attention#Config#wo.
  GptOssTransformerBlock.Config: GptOssTransformerBlock#Config#
  GptOssModel.Config.get_nparams_and_flops: GptOssModel#Config#get_nparams_and_flops().
  Attention.inner_attention: Attention#inner_attention.
  GptOssTransformerBlock: GptOssTransformerBlock#
  Attention.enable_gqa: Attention#enable_gqa.
  Attention.qkv_linear: Attention#qkv_linear.
  Attention.wo: Attention#wo.
  Attention.rope: Attention#rope.
  Attention._apply_sinks: Attention#_apply_sinks().
  GptOssTransformerBlock.attn_mask_key: GptOssTransformerBlock#attn_mask_key.
  GptOssTransformerBlock.attention: GptOssTransformerBlock#attention.
  GptOssTransformerBlock.attention_norm: GptOssTransformerBlock#attention_norm.
  GptOssTransformerBlock.moe: GptOssTransformerBlock#moe.
  Attention.n_rep: Attention#n_rep.
  GptOssModel.Config.vocab_size: GptOssModel#Config#vocab_size.
  GptOssModel.__init__: GptOssModel#__init__().
  Attention.sinks: Attention#sinks.
  Attention.n_heads: Attention#n_heads.
  Attention.n_kv_heads: Attention#n_kv_heads.
  Attention.Config.sliding_window_size: Attention#Config#sliding_window_size.
  Attention.head_dim: Attention#head_dim.
  apply_attention_sink_rescale: apply_attention_sink_rescale().
  Attention.Config.n_heads: Attention#Config#n_heads.
  GptOssModel.Config.dim: GptOssModel#Config#dim.
  Attention.__init__: Attention#__init__().
  Attention.Config.n_kv_heads: Attention#Config#n_kv_heads.
  Attention.Config.head_dim: Attention#Config#head_dim.
  Attention.Config.dim: Attention#Config#dim.
  GptOssTransformerBlock.moe_enabled: GptOssTransformerBlock#moe_enabled.
---
# Module: [`torchtitan/models/gpt_oss/model.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py)

## Classes
### <a id="Attention"></a>`Attention`  ·  implements/extends BaseAttention
- def: [`torchtitan/models/gpt_oss/model.py:46`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L46) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- doc: Multi-head attention (MLA) module with sink attention.
- signature: `class Attention(BaseAttention):`
- members:
  - <a id="Attention._apply_sinks"></a>`_apply_sinks(self, out: torch.Tensor, lse: torch.Tensor)` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L129) — out_transform hook: rescale attention output by this layer's sinks.
  - <a id="Attention.forward"></a>`forward(self, x: torch.Tensor, attention_masks: AttentionMasksType, positions: torch.Tensor | None = None, segment_ids: torch.Tensor | None = None)` — [`L89`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L89) — Forward pass for the Multi-Head Latent Attention (MLA) Layer. — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="Attention.enable_gqa"></a>`enable_gqa` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L71)
  - <a id="Attention.head_dim"></a>`head_dim` — [`L68`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L68)
  - <a id="Attention.inner_attention"></a>`inner_attention` — [`L86`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L86)
  - <a id="Attention.n_heads"></a>`n_heads` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L69)
  - <a id="Attention.n_kv_heads"></a>`n_kv_heads` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L70)
  - <a id="Attention.n_rep"></a>`n_rep` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L73)
  - <a id="Attention.qkv_linear"></a>`qkv_linear` — [`L83`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L83)
  - <a id="Attention.rope"></a>`rope` — [`L87`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L87)
  - <a id="Attention.sinks"></a>`sinks` — [`L85`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L85)
  - <a id="Attention.softmax_scale"></a>`softmax_scale` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L76) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="Attention.wo"></a>`wo` — [`L84`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L84)
- protocol/private: <a id="Attention.__init__"></a>`__init__`[`L66`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L66)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`BaseAttention`](../common/attention.md#BaseAttention), [`scaling`](../common/rope.md#RoPE.Config.scaling), [`rope_factor`](../common/rope.md#RoPE.Config.rope_factor), [`inner_attention`](model.md#Attention.Config.inner_attention), [`Config`](model.md#Attention.Config), [`rope`](model.md#Attention.Config.rope), [`qkv_linear`](model.md#Attention.Config.qkv_linear), [`wo`](model.md#Attention.Config.wo), [`apply_attention_sink_rescale`](model.md#apply_attention_sink_rescale), [`n_heads`](model.md#Attention.Config.n_heads), [`head_dim`](model.md#Attention.Config.head_dim), [`n_kv_heads`](model.md#Attention.Config.n_kv_heads)
- used by: [`_make_gptoss_attn_config`](__init__.md#_make_gptoss_attn_config), [`_set_gpt_oss_layer_sharding`](sharding.md#_set_gpt_oss_layer_sharding), [`BaseAttention`](../common/attention.md#BaseAttention), [`get_attention_masks`](model.md#GptOssModel.get_attention_masks), [`_inject_attention_sinks`](../../experiments/rl/models/vllm_wrapper.md#VLLMModelWrapper._inject_attention_sinks), [`__init__`](model.md#GptOssTransformerBlock.__init__)

### <a id="Attention.Config"></a>`Attention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/gpt_oss/model.py:52`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L52) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- signature: `class Config(BaseAttention.Config):`
- members:
  - <a id="Attention.Config.dim"></a>`dim` — [`L56`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L56)
  - <a id="Attention.Config.head_dim"></a>`head_dim` — [`L55`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L55)
  - <a id="Attention.Config.inner_attention"></a>`inner_attention` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L59) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="Attention.Config.n_heads"></a>`n_heads` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L53)
  - <a id="Attention.Config.n_kv_heads"></a>`n_kv_heads` — [`L54`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L54)
  - <a id="Attention.Config.qkv_linear"></a>`qkv_linear` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L57) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="Attention.Config.rope"></a>`rope` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L64) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="Attention.Config.sliding_window_size"></a>`sliding_window_size` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L62) — --- — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="Attention.Config.wo"></a>`wo` — [`L58`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L58)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`Config`](../../protocols/module.md#Module.Config), [`VarlenInnerAttention`](../common/attention.md#VarlenInnerAttention), [`BaseAttention`](../common/attention.md#BaseAttention), [`RoPE`](../common/rope.md#RoPE), [`Config`](../common/attention.md#VarlenInnerAttention.Config), [`Config`](../common/rope.md#RoPE.Config), [`Config`](../common/attention.md#BaseAttention.Config), [`BaseQKVLinear`](../common/attention.md#BaseQKVLinear), [`Config`](../common/attention.md#BaseQKVLinear.Config)
- used by: [`_make_gptoss_attn_config`](__init__.md#_make_gptoss_attn_config), [`_set_gpt_oss_layer_sharding`](sharding.md#_set_gpt_oss_layer_sharding), [`get_attention_masks`](model.md#GptOssModel.get_attention_masks), [`softmax_scale`](model.md#Attention.softmax_scale), [`__init__`](model.md#GptOssTransformerBlock.__init__), [`inner_attention`](model.md#Attention.inner_attention), [`attn_mask_key`](model.md#GptOssTransformerBlock.attn_mask_key), [`qkv_linear`](model.md#Attention.qkv_linear), [`rope`](model.md#Attention.rope), [`wo`](model.md#Attention.wo), [`n_heads`](model.md#Attention.n_heads), [`n_kv_heads`](model.md#Attention.n_kv_heads), [`sinks`](model.md#Attention.sinks), [`head_dim`](model.md#Attention.head_dim), [`__init__`](model.md#Attention.__init__)

### <a id="GptOssModel"></a>`GptOssModel`  ·  implements/extends Decoder
- def: [`torchtitan/models/gpt_oss/model.py:195`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L195) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- doc: GPT-OSS Transformer model with attention and feed-forward layers.
- signature: `class GptOssModel(Decoder):`
- members:
  - <a id="GptOssModel.get_attention_masks"></a>`get_attention_masks(self, positions: torch.Tensor, *, padding_mask: torch.Tensor | None = None, max_num_documents: int | None = None, max_context_length: int | None = None)` — [`L241`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L241) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- protocol/private: <a id="GptOssModel.__init__"></a>`__init__`[`L238`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L238)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`Decoder`](../common/decoder.md#Decoder), [`VarlenInnerAttention`](../common/attention.md#VarlenInnerAttention), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`Config`](../common/attention.md#FlexInnerAttention.Config), [`get_causal_mask_mod`](../common/attention.md#get_causal_mask_mod), [`Config`](../common/attention.md#VarlenInnerAttention.Config), [`create_varlen_metadata_for_document`](../common/attention.md#create_varlen_metadata_for_document), [`_create_flex_attention_mask`](../common/decoder.md#Decoder._create_flex_attention_mask), [`config`](../common/decoder.md#Decoder.config), [`get_sliding_window_mask_mod`](../common/attention.md#get_sliding_window_mask_mod), [`get_efficient_causal_mask_mod_for_packed_document`](../common/attention.md#get_efficient_causal_mask_mod_for_packed_document), [`Config`](model.md#GptOssModel.Config), [`inner_attention`](model.md#Attention.Config.inner_attention), [`Attention`](model.md#Attention), [`Config`](model.md#Attention.Config), [`__init__`](../common/decoder.md#Decoder.__init__), [`sliding_window_size`](model.md#Attention.Config.sliding_window_size)
- used by: [`Decoder`](../common/decoder.md#Decoder), [`_120b`](__init__.md#_120b), [`_20b`](__init__.md#_20b), [`_debugmodel`](__init__.md#_debugmodel), [`parallelize_gptoss`](parallelize.md#parallelize_gptoss), [`get_attention_masks`](../common/decoder.md#Decoder.get_attention_masks), [`set_gpt_oss_sharding_config`](sharding.md#set_gpt_oss_sharding_config), [`__init__`](state_dict_adapter.md#GptOssStateDictAdapter.__init__), [`_raise_dynamo_recompile_limit`](parallelize.md#_raise_dynamo_recompile_limit), [`_has_sliding_window_attention`](parallelize.md#_has_sliding_window_attention)  (3 test-only)

### <a id="GptOssModel.Config"></a>`GptOssModel.Config`  ·  implements/extends Config
- def: [`torchtitan/models/gpt_oss/model.py:201`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L201) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
- signature: `class Config(Decoder.Config):`
- members:
  - <a id="GptOssModel.Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L222`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L222)
  - <a id="GptOssModel.Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L205`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L205) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="GptOssModel.Config.dim"></a>`dim` — [`L202`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L202)
  - <a id="GptOssModel.Config.vocab_size"></a>`vocab_size` — [`L203`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L203)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`Decoder`](../common/decoder.md#Decoder), [`update_from_config`](../common/decoder.md#Decoder.Config.update_from_config), [`Config`](../common/decoder.md#Decoder.Config), [`get_nparams_and_active_nparams`](../utils.md#get_nparams_and_active_nparams), [`quadratic_attention_flops_per_token`](../utils.md#quadratic_attention_flops_per_token), [`set_gpt_oss_sharding_config`](sharding.md#set_gpt_oss_sharding_config)
- used by: [`_120b`](__init__.md#_120b), [`_20b`](__init__.md#_20b), [`_debugmodel`](__init__.md#_debugmodel), [`set_gpt_oss_sharding_config`](sharding.md#set_gpt_oss_sharding_config), [`__init__`](state_dict_adapter.md#GptOssStateDictAdapter.__init__), [`__init__`](model.md#GptOssModel.__init__)  (2 test-only)

### <a id="GptOssTransformerBlock"></a>`GptOssTransformerBlock`  ·  implements/extends TransformerBlock
- def: [`torchtitan/models/gpt_oss/model.py:137`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L137)
- doc: GptOss Transformer block with sliding window attention support.
- signature: `class GptOssTransformerBlock(TransformerBlock):`
- members:
  - <a id="GptOssTransformerBlock.forward"></a>`forward(self, x: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None, segment_ids: torch.Tensor | None = None)` — [`L162`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L162) — Forward pass for the Transformer block. — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="GptOssTransformerBlock.attention"></a>`attention` — [`L154`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L154)
  - <a id="GptOssTransformerBlock.attention_norm"></a>`attention_norm` — [`L155`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L155)
  - <a id="GptOssTransformerBlock.attn_mask_key"></a>`attn_mask_key` — [`L149`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L149)
  - <a id="GptOssTransformerBlock.ffn_norm"></a>`ffn_norm` — [`L156`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L156) — documented in [gpt-oss-model](../../../../concepts/gpt-oss-model.md)
  - <a id="GptOssTransformerBlock.moe"></a>`moe` — [`L159`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L159)
  - <a id="GptOssTransformerBlock.moe_enabled"></a>`moe_enabled` — [`L160`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L160)
- protocol/private: <a id="GptOssTransformerBlock.__init__"></a>`__init__`[`L146`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L146)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`attention`](../common/decoder.md#TransformerBlock.Config.attention), [`attention_norm`](../common/decoder.md#TransformerBlock.Config.attention_norm), [`ffn_norm`](../common/decoder.md#TransformerBlock.Config.ffn_norm), [`moe`](../common/decoder.md#TransformerBlock.Config.moe), [`Attention`](model.md#Attention), [`Config`](model.md#Attention.Config), [`Config`](model.md#GptOssTransformerBlock.Config), [`sliding_window_size`](model.md#Attention.Config.sliding_window_size)
- used by: [`_build_gptoss_layers`](__init__.md#_build_gptoss_layers), [`_set_gpt_oss_layer_sharding`](sharding.md#_set_gpt_oss_layer_sharding), [`TransformerBlock`](../common/decoder.md#TransformerBlock)

### <a id="GptOssTransformerBlock.Config"></a>`GptOssTransformerBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/gpt_oss/model.py:143`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L143)
- signature: `class Config(TransformerBlock.Config):`
- uses (calls/refs, reference-scoped): [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`Config`](../common/decoder.md#TransformerBlock.Config)
- used by: [`_build_gptoss_layers`](__init__.md#_build_gptoss_layers), [`_set_gpt_oss_layer_sharding`](sharding.md#_set_gpt_oss_layer_sharding), [`__init__`](model.md#GptOssTransformerBlock.__init__)

## Functions
- <a id="apply_attention_sink_rescale"></a>`apply_attention_sink_rescale(out: torch.Tensor, lse: torch.Tensor, sinks: torch.Tensor)` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/gpt_oss/model.py#L37) — Rescale attention output by the learned per-head sink term.

