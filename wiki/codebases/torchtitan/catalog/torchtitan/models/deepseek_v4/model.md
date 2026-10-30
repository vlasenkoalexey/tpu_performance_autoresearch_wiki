---
title: 'Module: torchtitan/models/deepseek_v4/model.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v4/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v4.model`/
symbols:
  DeepSeekV4Model.Config.get_nparams_and_flops: DeepSeekV4Model#Config#get_nparams_and_flops().
  DeepSeekV4TransformerBlock.forward: DeepSeekV4TransformerBlock#forward().
  DeepSeekV4Model.forward: DeepSeekV4Model#forward().
  DeepSeekV4TransformerBlock.Config.moe: DeepSeekV4TransformerBlock#Config#moe.
  DeepSeekV4Model.Config.update_from_config: DeepSeekV4Model#Config#update_from_config().
  DeepSeekV4Model.mtp_layers: DeepSeekV4Model#mtp_layers.
  DeepSeekV4TransformerBlock: DeepSeekV4TransformerBlock#
  DeepSeekV4Model: DeepSeekV4Model#
  DeepSeekV4Model.Config: DeepSeekV4Model#Config#
  DeepSeekV4Model.Config.mtp_layers: DeepSeekV4Model#Config#mtp_layers.
  DeepSeekV4TransformerBlock.Config: DeepSeekV4TransformerBlock#Config#
  DeepSeekV4TransformerBlock.Config.attention: DeepSeekV4TransformerBlock#Config#attention.
  DeepSeekV4Model.mtp_forward: DeepSeekV4Model#mtp_forward().
  DeepSeekV4TransformerBlock.Config.hc_attn_pre: DeepSeekV4TransformerBlock#Config#hc_attn_pre.
  DeepSeekV4TransformerBlock.Config.hc_ffn_pre: DeepSeekV4TransformerBlock#Config#hc_ffn_pre.
  DeepSeekV4TransformerBlock.Config.hc_post: DeepSeekV4TransformerBlock#Config#hc_post.
  DeepSeekV4Model.Config.hc_head: DeepSeekV4Model#Config#hc_head.
  DeepSeekV4TransformerBlock.ffn_norm: DeepSeekV4TransformerBlock#ffn_norm.
  DeepSeekV4TransformerBlock.moe: DeepSeekV4TransformerBlock#moe.
  DeepSeekV4TransformerBlock.feed_forward: DeepSeekV4TransformerBlock#feed_forward.
  DeepSeekV4TransformerBlock.moe_enabled: DeepSeekV4TransformerBlock#moe_enabled.
  DeepSeekV4TransformerBlock.hc_post: DeepSeekV4TransformerBlock#hc_post.
  DeepSeekV4Model.Config.n_layers: DeepSeekV4Model#Config#n_layers.
  DeepSeekV4TransformerBlock.attention: DeepSeekV4TransformerBlock#attention.
  DeepSeekV4TransformerBlock.attention_norm: DeepSeekV4TransformerBlock#attention_norm.
  DeepSeekV4TransformerBlock.hc_attn_pre: DeepSeekV4TransformerBlock#hc_attn_pre.
  DeepSeekV4TransformerBlock.hc_ffn_pre: DeepSeekV4TransformerBlock#hc_ffn_pre.
  DeepSeekV4Model.hc_head: DeepSeekV4Model#hc_head.
  DeepSeekV4Model.Config.hc_mult: DeepSeekV4Model#Config#hc_mult.
  DeepSeekV4Model.Config.compress_ratios: DeepSeekV4Model#Config#compress_ratios.
  DeepSeekV4Model.__init__: DeepSeekV4Model#__init__().
  DeepSeekV4Model.compress_ratios: DeepSeekV4Model#compress_ratios.
  DeepSeekV4Model.Config.n_mtp_layers: DeepSeekV4Model#Config#n_mtp_layers.
  DeepSeekV4TransformerBlock.__init__: DeepSeekV4TransformerBlock#__init__().
  DeepSeekV4Model.hc_mult: DeepSeekV4Model#hc_mult.
  DeepSeekV4Model.n_main_layers: DeepSeekV4Model#n_main_layers.
  DeepSeekV4Model.Config.dim: DeepSeekV4Model#Config#dim.
  DeepSeekV4Model.Config.vocab_size: DeepSeekV4Model#Config#vocab_size.
  DeepSeekV4Model.Config.norm_eps: DeepSeekV4Model#Config#norm_eps.
  DeepSeekV4Model.n_mtp_layers: DeepSeekV4Model#n_mtp_layers.
  DeepSeekV4Model.get_attention_masks: DeepSeekV4Model#get_attention_masks().
---
# Module: [`torchtitan/models/deepseek_v4/model.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py)

## Classes
### <a id="DeepSeekV4Model"></a>`DeepSeekV4Model`  ·  implements/extends Decoder
- def: [`torchtitan/models/deepseek_v4/model.py:101`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L101) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- doc: DeepSeek V4 decoder model with HC branches and sparse attention.
- signature: `class DeepSeekV4Model(Decoder):`
- members:
  - <a id="DeepSeekV4Model.forward"></a>`forward(self, tokens: torch.Tensor, positions: torch.Tensor | None = None, attention_masks: AttentionMasksType | None = None)` — [`L230`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L230) — Run the DeepSeek V4 decoder. — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepSeekV4Model.get_attention_masks"></a>`get_attention_masks(self, positions, *, padding_mask=None, max_num_documents=None, max_context_length=None)` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L219)
  - <a id="DeepSeekV4Model.mtp_forward"></a>`mtp_forward(self, prev_hc_hidden: torch.Tensor, tokens: torch.Tensor, attention_masks: AttentionMasksType | None = None, positions: torch.Tensor | None = None)` — [`L272`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L272) — Run auxiliary MTP depths and return prediction hidden states. — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepSeekV4Model.compress_ratios"></a>`compress_ratios` — [`L209`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L209)
  - <a id="DeepSeekV4Model.hc_head"></a>`hc_head` — [`L212`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L212)
  - <a id="DeepSeekV4Model.hc_mult"></a>`hc_mult` — [`L207`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L207)
  - <a id="DeepSeekV4Model.mtp_layers"></a>`mtp_layers` — [`L213`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L213) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepSeekV4Model.n_main_layers"></a>`n_main_layers` — [`L210`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L210)
  - <a id="DeepSeekV4Model.n_mtp_layers"></a>`n_mtp_layers` — [`L208`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L208)
- protocol/private: <a id="DeepSeekV4Model.__init__"></a>`__init__`[`L203`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L203)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`Decoder`](../common/decoder.md#Decoder), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`tok_embeddings`](../common/decoder.md#Decoder.tok_embeddings), [`lm_head`](../common/decoder.md#Decoder.lm_head), [`ModuleList`](../../protocols/module.md#ModuleList), [`norm`](../common/decoder.md#Decoder.norm), [`layers`](../common/decoder.md#Decoder.layers), [`Config`](model.md#DeepSeekV4Model.Config), [`mtp_layers`](model.md#DeepSeekV4Model.Config.mtp_layers), [`__init__`](../common/decoder.md#Decoder.__init__), [`hc_head`](model.md#DeepSeekV4Model.Config.hc_head), [`_skip_lm_head`](../common/decoder.md#Decoder._skip_lm_head), [`n_layers`](model.md#DeepSeekV4Model.Config.n_layers), [`compress_ratios`](model.md#DeepSeekV4Model.Config.compress_ratios), [`hc_mult`](model.md#DeepSeekV4Model.Config.hc_mult), [`roll_mtp_sequence`](../deepseek_v3/mtp.md#roll_mtp_sequence), [`n_mtp_layers`](model.md#DeepSeekV4Model.Config.n_mtp_layers)
- used by: [`_debugmodel`](__init__.md#_debugmodel), [`_deepseek_v4_flash`](__init__.md#_deepseek_v4_flash), [`_deepseek_v4_pro`](__init__.md#_deepseek_v4_pro), [`Decoder`](../common/decoder.md#Decoder), [`set_deepseek_v4_sharding_config`](sharding.md#set_deepseek_v4_sharding_config), [`get_attention_masks`](../common/decoder.md#Decoder.get_attention_masks), [`get_nparams_and_flops`](model.md#DeepSeekV4Model.Config.get_nparams_and_flops), [`forward`](../common/decoder.md#Decoder.forward), [`_replicated_layout`](sharding.md#_replicated_layout), [`__init__`](state_dict_adapter.md#DeepSeekV4StateDictAdapter.__init__)

### <a id="DeepSeekV4Model.Config"></a>`DeepSeekV4Model.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/model.py:105`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L105)
- signature: `class Config(Decoder.Config):`
- members:
  - <a id="DeepSeekV4Model.Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L153`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L153) — Estimate DeepSeek V4 training FLOPs from the final model config. — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepSeekV4Model.Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L116`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L116)
  - <a id="DeepSeekV4Model.Config.compress_ratios"></a>`compress_ratios` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L110)
  - <a id="DeepSeekV4Model.Config.dim"></a>`dim` — [`L106`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L106)
  - <a id="DeepSeekV4Model.Config.hc_head"></a>`hc_head` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L113)
  - <a id="DeepSeekV4Model.Config.hc_mult"></a>`hc_mult` — [`L108`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L108)
  - <a id="DeepSeekV4Model.Config.mtp_layers"></a>`mtp_layers` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L114) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepSeekV4Model.Config.n_layers"></a>`n_layers` — [`L111`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L111)
  - <a id="DeepSeekV4Model.Config.n_mtp_layers"></a>`n_mtp_layers` — [`L109`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L109)
  - <a id="DeepSeekV4Model.Config.norm_eps"></a>`norm_eps` — [`L112`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L112)
  - <a id="DeepSeekV4Model.Config.vocab_size"></a>`vocab_size` — [`L107`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L107)
- uses (calls/refs, reference-scoped): [`layers`](../common/decoder.md#Decoder.Config.layers), [`Decoder`](../common/decoder.md#Decoder), [`set_deepseek_v4_sharding_config`](sharding.md#set_deepseek_v4_sharding_config), [`update_from_config`](../common/decoder.md#Decoder.Config.update_from_config), [`Config`](../common/decoder.md#Decoder.Config), [`lm_head`](../common/decoder.md#Decoder.lm_head), [`get_nparams_and_active_nparams`](../utils.md#get_nparams_and_active_nparams), [`quadratic_attention_flops_per_token`](../utils.md#quadratic_attention_flops_per_token), [`mtp_layers`](model.md#DeepSeekV4Model.mtp_layers), [`DeepSeekV4Model`](model.md#DeepSeekV4Model), [`Config`](mhc.md#HcHead.Config), [`attention`](model.md#DeepSeekV4TransformerBlock.Config.attention), [`HcHead`](mhc.md#HcHead), [`inner_attention`](attention.md#Attention.Config.inner_attention), [`Config`](mtp.md#MTPBlock.Config), [`MTPBlock`](mtp.md#MTPBlock), [`h_proj`](mtp.md#MTPBlock.h_proj), [`head_dim`](attention.md#Attention.Config.head_dim), [`compress_ratio`](attention.md#Attention.Config.compress_ratio), [`index_topk`](attention.md#DSV4FlexInnerAttention.Config.index_topk), [`n_heads`](attention.md#Attention.Config.n_heads), [`window_size`](attention.md#DSV4FlexInnerAttention.Config.window_size), [`index_head_dim`](attention.md#Attention.Config.index_head_dim), [`index_n_heads`](attention.md#Attention.Config.index_n_heads)
- used by: [`_debugmodel`](__init__.md#_debugmodel), [`_deepseek_v4_flash`](__init__.md#_deepseek_v4_flash), [`_deepseek_v4_pro`](__init__.md#_deepseek_v4_pro), [`set_deepseek_v4_sharding_config`](sharding.md#set_deepseek_v4_sharding_config), [`mtp_layers`](model.md#DeepSeekV4Model.mtp_layers), [`compress_ratios`](state_dict_adapter.md#DeepSeekV4StateDictAdapter.compress_ratios), [`__init__`](state_dict_adapter.md#DeepSeekV4StateDictAdapter.__init__), [`hc_head`](model.md#DeepSeekV4Model.hc_head), [`__init__`](model.md#DeepSeekV4Model.__init__), [`compress_ratios`](model.md#DeepSeekV4Model.compress_ratios), [`hc_mult`](model.md#DeepSeekV4Model.hc_mult), [`n_main_layers`](model.md#DeepSeekV4Model.n_main_layers), [`n_mtp_layers`](model.md#DeepSeekV4Model.n_mtp_layers)

### <a id="DeepSeekV4TransformerBlock"></a>`DeepSeekV4TransformerBlock`  ·  implements/extends TransformerBlock
- def: [`torchtitan/models/deepseek_v4/model.py:30`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L30) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- doc: Transformer block with HC pre/post mixing around attention and FFN.
- signature: `class DeepSeekV4TransformerBlock(TransformerBlock):`
- members:
  - <a id="DeepSeekV4TransformerBlock.forward"></a>`forward(self, x: torch.Tensor, input_ids_T: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None)` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L64) — Run one DeepSeek V4 decoder block. — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepSeekV4TransformerBlock.attention"></a>`attention` — [`L47`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L47)
  - <a id="DeepSeekV4TransformerBlock.attention_norm"></a>`attention_norm` — [`L48`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L48)
  - <a id="DeepSeekV4TransformerBlock.feed_forward"></a>`feed_forward` — [`L57`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L57)
  - <a id="DeepSeekV4TransformerBlock.ffn_norm"></a>`ffn_norm` — [`L49`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L49)
  - <a id="DeepSeekV4TransformerBlock.hc_attn_pre"></a>`hc_attn_pre` — [`L60`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L60)
  - <a id="DeepSeekV4TransformerBlock.hc_ffn_pre"></a>`hc_ffn_pre` — [`L61`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L61)
  - <a id="DeepSeekV4TransformerBlock.hc_post"></a>`hc_post` — [`L62`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L62)
  - <a id="DeepSeekV4TransformerBlock.moe"></a>`moe` — [`L52`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L52)
  - <a id="DeepSeekV4TransformerBlock.moe_enabled"></a>`moe_enabled` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L53)
- protocol/private: <a id="DeepSeekV4TransformerBlock.__init__"></a>`__init__`[`L43`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L43)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`feed_forward`](../common/decoder.md#TransformerBlock.Config.feed_forward), [`attention_norm`](../common/decoder.md#TransformerBlock.Config.attention_norm), [`ffn_norm`](../common/decoder.md#TransformerBlock.Config.ffn_norm), [`moe`](model.md#DeepSeekV4TransformerBlock.Config.moe), [`forward`](mtp.md#MTPBlock.forward), [`Config`](model.md#DeepSeekV4TransformerBlock.Config), [`attention`](model.md#DeepSeekV4TransformerBlock.Config.attention), [`hc_attn_pre`](model.md#DeepSeekV4TransformerBlock.Config.hc_attn_pre), [`hc_ffn_pre`](model.md#DeepSeekV4TransformerBlock.Config.hc_ffn_pre), [`hc_post`](model.md#DeepSeekV4TransformerBlock.Config.hc_post), [`MTPBlock`](mtp.md#MTPBlock)
- used by: [`_build_mtp_layers`](__init__.md#_build_mtp_layers), [`_build_v4_layers`](__init__.md#_build_v4_layers), [`set_deepseek_v4_layer_sharding`](sharding.md#set_deepseek_v4_layer_sharding), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`_make_mtp_inner_block`](__init__.md#_make_mtp_inner_block), [`forward`](mtp.md#MTPBlock.forward), [`Config`](mtp.md#MTPBlock.Config), [`_replicated_layout`](sharding.md#_replicated_layout), [`MTPBlock`](mtp.md#MTPBlock), [`__init__`](mtp.md#MTPBlock.__init__)

### <a id="DeepSeekV4TransformerBlock.Config"></a>`DeepSeekV4TransformerBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/model.py:34`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L34)
- signature: `class Config(TransformerBlock.Config):`
- members:
  - <a id="DeepSeekV4TransformerBlock.Config.attention"></a>`attention` — [`L37`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L37)
  - <a id="DeepSeekV4TransformerBlock.Config.hc_attn_pre"></a>`hc_attn_pre` — [`L39`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L39)
  - <a id="DeepSeekV4TransformerBlock.Config.hc_ffn_pre"></a>`hc_ffn_pre` — [`L40`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L40)
  - <a id="DeepSeekV4TransformerBlock.Config.hc_post"></a>`hc_post` — [`L41`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L41)
  - <a id="DeepSeekV4TransformerBlock.Config.moe"></a>`moe` — [`L38`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/model.py#L38) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- uses (calls/refs, reference-scoped): [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`Config`](../common/decoder.md#TransformerBlock.Config), [`Config`](moe.md#DeepSeekV4MoE.Config), [`Config`](mhc.md#HcPre.Config), [`Config`](attention.md#Attention.Config), [`HcPre`](mhc.md#HcPre), [`Config`](mhc.md#HcPost.Config), [`Attention`](attention.md#Attention), [`DeepSeekV4MoE`](moe.md#DeepSeekV4MoE), [`HcPost`](mhc.md#HcPost)
- used by: [`_build_mtp_layers`](__init__.md#_build_mtp_layers), [`_build_v4_layers`](__init__.md#_build_v4_layers), [`set_deepseek_v4_layer_sharding`](sharding.md#set_deepseek_v4_layer_sharding), [`get_nparams_and_flops`](model.md#DeepSeekV4Model.Config.get_nparams_and_flops), [`_make_mtp_inner_block`](__init__.md#_make_mtp_inner_block), [`ffn_norm`](model.md#DeepSeekV4TransformerBlock.ffn_norm), [`Config`](mtp.md#MTPBlock.Config), [`moe`](model.md#DeepSeekV4TransformerBlock.moe), [`hc_post`](model.md#DeepSeekV4TransformerBlock.hc_post), [`attention`](model.md#DeepSeekV4TransformerBlock.attention), [`hc_attn_pre`](model.md#DeepSeekV4TransformerBlock.hc_attn_pre), [`hc_ffn_pre`](model.md#DeepSeekV4TransformerBlock.hc_ffn_pre), [`__init__`](model.md#DeepSeekV4TransformerBlock.__init__)

