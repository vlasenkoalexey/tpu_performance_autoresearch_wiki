---
title: 'Module: torchtitan/models/deepseek_v4/attention.py'
type: catalog
provenance: extracted
module: torchtitan/models/deepseek_v4/attention.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.deepseek_v4.attention`/
symbols:
  Attention.forward: Attention#forward().
  DSV4FlexInnerAttention._forward_impl: DSV4FlexInnerAttention#_forward_impl().
  DSV4FlexInnerAttention: DSV4FlexInnerAttention#
  DSV4FlexInnerAttention.Config: DSV4FlexInnerAttention#Config#
  Attention.Config.inner_attention: Attention#Config#inner_attention.
  Attention.Config: Attention#Config#
  Attention.Config.compressor: Attention#Config#compressor.
  Attention.Config.compressor_128: Attention#Config#compressor_128.
  Attention.Config.indexer: Attention#Config#indexer.
  Attention.attn_sink: Attention#attn_sink.
  Attention.compressor: Attention#compressor.
  Attention.indexer: Attention#indexer.
  Attention.Config.rope: Attention#Config#rope.
  Attention.inner_attention: Attention#inner_attention.
  DSV4FlexInnerAttention.compress_ratio: DSV4FlexInnerAttention#compress_ratio.
  Attention: Attention#
  Attention.compress_ratio: Attention#compress_ratio.
  Attention.Config.head_dim: Attention#Config#head_dim.
  Attention.Config.wq_a: Attention#Config#wq_a.
  Attention.Config.q_norm: Attention#Config#q_norm.
  Attention.Config.wq_b: Attention#Config#wq_b.
  Attention.Config.wkv: Attention#Config#wkv.
  Attention.Config.kv_norm: Attention#Config#kv_norm.
  Attention.Config.wo_a: Attention#Config#wo_a.
  Attention.Config.wo_b: Attention#Config#wo_b.
  Attention.Config.attn_sink: Attention#Config#attn_sink.
  Attention.rope: Attention#rope.
  Attention.head_dim: Attention#head_dim.
  DSV4FlexInnerAttention._build_block_mask: DSV4FlexInnerAttention#_build_block_mask().
  SlidingWindowAttention.Config: SlidingWindowAttention#Config#
  CompressedSparseAttention.Config: CompressedSparseAttention#Config#
  Attention.Config.compress_ratio: Attention#Config#compress_ratio.
  Attention.wq_a: Attention#wq_a.
  Attention.q_norm: Attention#q_norm.
  Attention.wq_b: Attention#wq_b.
  Attention.wkv: Attention#wkv.
  Attention.kv_norm: Attention#kv_norm.
  Attention.wo_a: Attention#wo_a.
  Attention.wo_b: Attention#wo_b.
  Attention.compressor_128: Attention#compressor_128.
  _assert_spmd_attention_type: _assert_spmd_attention_type().
  SlidingWindowAttention: SlidingWindowAttention#
  DSV4FlexInnerAttention.__init__: DSV4FlexInnerAttention#__init__().
  HeavilyCompressedAttention.Config: HeavilyCompressedAttention#Config#
  HeavilyCompressedAttention: HeavilyCompressedAttention#
  CompressedSparseAttention: CompressedSparseAttention#
  DSV4FlexInnerAttention.Config.window_size: DSV4FlexInnerAttention#Config#window_size.
  DSV4FlexInnerAttention.Config.index_topk: DSV4FlexInnerAttention#Config#index_topk.
  Attention.Config.n_heads: Attention#Config#n_heads.
  DSV4FlexInnerAttention.window_size: DSV4FlexInnerAttention#window_size.
  DSV4FlexInnerAttention.softmax_scale: DSV4FlexInnerAttention#softmax_scale.
  DSV4FlexInnerAttention.index_topk: DSV4FlexInnerAttention#index_topk.
  DSV4FlexInnerAttention.block_size: DSV4FlexInnerAttention#block_size.
  DSV4FlexInnerAttention.get_window_topk_idxs: DSV4FlexInnerAttention#get_window_topk_idxs().
  DSV4FlexInnerAttention.get_compress_topk_idxs: DSV4FlexInnerAttention#get_compress_topk_idxs().
  Attention.n_heads: Attention#n_heads.
  Attention.rope_head_dim: Attention#rope_head_dim.
  Attention.o_lora_rank: Attention#o_lora_rank.
  Attention.n_groups: Attention#n_groups.
  Attention.norm_eps: Attention#norm_eps.
  DSV4FlexInnerAttention.Config.softmax_scale: DSV4FlexInnerAttention#Config#softmax_scale.
  SlidingWindowAttention.forward: SlidingWindowAttention#forward().
  HeavilyCompressedAttention.forward: HeavilyCompressedAttention#forward().
  CompressedSparseAttention.forward: CompressedSparseAttention#forward().
  Attention.__init__: Attention#__init__().
  Attention.q_lora_rank: Attention#q_lora_rank.
  Attention.softmax_scale: Attention#softmax_scale.
  Attention.layer_id: Attention#layer_id.
  Attention.n_layers: Attention#n_layers.
  DSV4FlexInnerAttention.Config.compress_ratio: DSV4FlexInnerAttention#Config#compress_ratio.
  Attention.Config.rope_head_dim: Attention#Config#rope_head_dim.
  Attention.Config.q_lora_rank: Attention#Config#q_lora_rank.
  Attention.Config.o_lora_rank: Attention#Config#o_lora_rank.
  Attention.Config.n_groups: Attention#Config#n_groups.
  Attention.Config.norm_eps: Attention#Config#norm_eps.
  Attention.Config.index_n_heads: Attention#Config#index_n_heads.
  Attention.Config.index_head_dim: Attention#Config#index_head_dim.
  Attention.Config.n_layers: Attention#Config#n_layers.
  Attention.Config.layer_id: Attention#Config#layer_id.
  DSV4FlexInnerAttention.dsa_mask_mod: DSV4FlexInnerAttention#dsa_mask_mod().
  DSV4FlexInnerAttention.v4_sink_score_mod: DSV4FlexInnerAttention#v4_sink_score_mod().
  Attention.Config.dim: Attention#Config#dim.
  Attention.Config.mask_type: Attention#Config#mask_type.
---
# Module: [`torchtitan/models/deepseek_v4/attention.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py)

## Classes
### <a id="Attention"></a>`Attention`  ·  implements/extends BaseAttention
- def: [`torchtitan/models/deepseek_v4/attention.py:353`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L353)
- doc: DeepSeek V4 attention wrapper around sparse inner attention.
- signature: `class Attention(BaseAttention):`
- members:
  - <a id="Attention.forward"></a>`forward(self, x, attention_masks=None, positions=None)` — [`L431`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L431) — Apply one DeepSeek V4 attention layer over folded tokens. — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="Attention.attn_sink"></a>`attn_sink` — [`L420`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L420)
  - <a id="Attention.compress_ratio"></a>`compress_ratio` — [`L405`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L405)
  - <a id="Attention.compressor"></a>`compressor` — [`L423`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L423)
  - <a id="Attention.compressor_128"></a>`compressor_128` — [`L427`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L427)
  - <a id="Attention.head_dim"></a>`head_dim` — [`L400`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L400)
  - <a id="Attention.indexer"></a>`indexer` — [`L425`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L425)
  - <a id="Attention.inner_attention"></a>`inner_attention` — [`L429`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L429)
  - <a id="Attention.kv_norm"></a>`kv_norm` — [`L417`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L417)
  - <a id="Attention.layer_id"></a>`layer_id` — [`L408`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L408)
  - <a id="Attention.n_groups"></a>`n_groups` — [`L404`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L404)
  - <a id="Attention.n_heads"></a>`n_heads` — [`L399`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L399)
  - <a id="Attention.n_layers"></a>`n_layers` — [`L409`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L409)
  - <a id="Attention.norm_eps"></a>`norm_eps` — [`L406`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L406)
  - <a id="Attention.o_lora_rank"></a>`o_lora_rank` — [`L403`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L403)
  - <a id="Attention.q_lora_rank"></a>`q_lora_rank` — [`L402`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L402)
  - <a id="Attention.q_norm"></a>`q_norm` — [`L414`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L414)
  - <a id="Attention.rope"></a>`rope` — [`L410`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L410)
  - <a id="Attention.rope_head_dim"></a>`rope_head_dim` — [`L401`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L401)
  - <a id="Attention.softmax_scale"></a>`softmax_scale` — [`L407`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L407)
  - <a id="Attention.wkv"></a>`wkv` — [`L416`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L416)
  - <a id="Attention.wo_a"></a>`wo_a` — [`L418`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L418)
  - <a id="Attention.wo_b"></a>`wo_b` — [`L419`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L419)
  - <a id="Attention.wq_a"></a>`wq_a` — [`L413`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L413)
  - <a id="Attention.wq_b"></a>`wq_b` — [`L415`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L415)
- protocol/private: <a id="Attention.__init__"></a>`__init__`[`L396`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L396)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`get_spmd_backend`](../../distributed/utils.md#get_spmd_backend), [`BaseAttention`](../common/attention.md#BaseAttention), [`inner_attention`](attention.md#Attention.Config.inner_attention), [`Config`](attention.md#Attention.Config), [`compressor`](attention.md#Attention.Config.compressor), [`compressor_128`](attention.md#Attention.Config.compressor_128), [`indexer`](attention.md#Attention.Config.indexer), [`rope`](attention.md#Attention.Config.rope), [`attn_sink`](attention.md#Attention.Config.attn_sink), [`head_dim`](attention.md#Attention.Config.head_dim), [`kv_norm`](attention.md#Attention.Config.kv_norm), [`q_norm`](attention.md#Attention.Config.q_norm), [`wkv`](attention.md#Attention.Config.wkv), [`wo_a`](attention.md#Attention.Config.wo_a), [`wo_b`](attention.md#Attention.Config.wo_b), [`wq_a`](attention.md#Attention.Config.wq_a), [`wq_b`](attention.md#Attention.Config.wq_b), [`compress_ratio`](attention.md#Attention.Config.compress_ratio), [`_assert_spmd_attention_type`](attention.md#_assert_spmd_attention_type), [`n_heads`](attention.md#Attention.Config.n_heads), [`layer_id`](attention.md#Attention.Config.layer_id), [`n_groups`](attention.md#Attention.Config.n_groups), [`n_layers`](attention.md#Attention.Config.n_layers), [`norm_eps`](attention.md#Attention.Config.norm_eps), [`o_lora_rank`](attention.md#Attention.Config.o_lora_rank), [`q_lora_rank`](attention.md#Attention.Config.q_lora_rank), [`rope_head_dim`](attention.md#Attention.Config.rope_head_dim)
- used by: [`_make_v4_attn_config`](__init__.md#_make_v4_attn_config), [`BaseAttention`](../common/attention.md#BaseAttention), [`attention`](model.md#DeepSeekV4TransformerBlock.Config.attention)

### <a id="Attention.Config"></a>`Attention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/attention.py:362`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L362)
- signature: `class Config(BaseAttention.Config):`
- members:
  - <a id="Attention.Config.attn_sink"></a>`attn_sink` — [`L389`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L389)
  - <a id="Attention.Config.compress_ratio"></a>`compress_ratio` — [`L372`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L372)
  - <a id="Attention.Config.compressor"></a>`compressor` — [`L392`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L392) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="Attention.Config.compressor_128"></a>`compressor_128` — [`L393`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L393) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="Attention.Config.dim"></a>`dim` — [`L363`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L363)
  - <a id="Attention.Config.head_dim"></a>`head_dim` — [`L367`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L367)
  - <a id="Attention.Config.index_head_dim"></a>`index_head_dim` — [`L375`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L375)
  - <a id="Attention.Config.index_n_heads"></a>`index_n_heads` — [`L374`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L374)
  - <a id="Attention.Config.indexer"></a>`indexer` — [`L394`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L394)
  - <a id="Attention.Config.inner_attention"></a>`inner_attention` — [`L365`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L365) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="Attention.Config.kv_norm"></a>`kv_norm` — [`L386`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L386)
  - <a id="Attention.Config.layer_id"></a>`layer_id` — [`L377`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L377)
  - <a id="Attention.Config.mask_type"></a>`mask_type` — [`L378`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L378)
  - <a id="Attention.Config.n_groups"></a>`n_groups` — [`L371`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L371)
  - <a id="Attention.Config.n_heads"></a>`n_heads` — [`L364`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L364)
  - <a id="Attention.Config.n_layers"></a>`n_layers` — [`L376`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L376)
  - <a id="Attention.Config.norm_eps"></a>`norm_eps` — [`L373`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L373)
  - <a id="Attention.Config.o_lora_rank"></a>`o_lora_rank` — [`L370`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L370)
  - <a id="Attention.Config.q_lora_rank"></a>`q_lora_rank` — [`L369`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L369)
  - <a id="Attention.Config.q_norm"></a>`q_norm` — [`L383`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L383)
  - <a id="Attention.Config.rope"></a>`rope` — [`L366`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L366)
  - <a id="Attention.Config.rope_head_dim"></a>`rope_head_dim` — [`L368`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L368)
  - <a id="Attention.Config.wkv"></a>`wkv` — [`L385`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L385)
  - <a id="Attention.Config.wo_a"></a>`wo_a` — [`L387`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L387)
  - <a id="Attention.Config.wo_b"></a>`wo_b` — [`L388`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L388)
  - <a id="Attention.Config.wq_a"></a>`wq_a` — [`L382`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L382)
  - <a id="Attention.Config.wq_b"></a>`wq_b` — [`L384`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L384)
- uses (calls/refs, reference-scoped): [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`BaseAttention`](../common/attention.md#BaseAttention), [`RoPE`](../common/rope.md#RoPE), [`Config`](../common/rope.md#RoPE.Config), [`Config`](../common/attention.md#BaseAttention.Config), [`DSV4FlexInnerAttention`](attention.md#DSV4FlexInnerAttention), [`Config`](compressor.md#Compressor.Config), [`Config`](attention.md#DSV4FlexInnerAttention.Config), [`Compressor`](compressor.md#Compressor), [`Config`](compressor.md#Indexer.Config), [`Indexer`](compressor.md#Indexer)
- used by: [`_make_v4_attn_config`](__init__.md#_make_v4_attn_config), [`get_nparams_and_flops`](model.md#DeepSeekV4Model.Config.get_nparams_and_flops), [`_make_mtp_inner_block`](__init__.md#_make_mtp_inner_block), [`attention`](model.md#DeepSeekV4TransformerBlock.Config.attention), [`attn_sink`](attention.md#Attention.attn_sink), [`compressor`](attention.md#Attention.compressor), [`indexer`](attention.md#Attention.indexer), [`inner_attention`](attention.md#Attention.inner_attention), [`compress_ratio`](attention.md#Attention.compress_ratio), [`rope`](attention.md#Attention.rope), [`head_dim`](attention.md#Attention.head_dim), [`compressor_128`](attention.md#Attention.compressor_128), [`kv_norm`](attention.md#Attention.kv_norm), [`q_norm`](attention.md#Attention.q_norm), [`wkv`](attention.md#Attention.wkv), [`wo_a`](attention.md#Attention.wo_a), [`wo_b`](attention.md#Attention.wo_b), [`wq_a`](attention.md#Attention.wq_a), [`wq_b`](attention.md#Attention.wq_b), [`n_groups`](attention.md#Attention.n_groups), [`n_heads`](attention.md#Attention.n_heads), [`norm_eps`](attention.md#Attention.norm_eps), [`o_lora_rank`](attention.md#Attention.o_lora_rank), [`rope_head_dim`](attention.md#Attention.rope_head_dim), [`__init__`](attention.md#Attention.__init__), [`layer_id`](attention.md#Attention.layer_id), [`n_layers`](attention.md#Attention.n_layers), [`q_lora_rank`](attention.md#Attention.q_lora_rank), [`softmax_scale`](attention.md#Attention.softmax_scale)

### <a id="CompressedSparseAttention"></a>`CompressedSparseAttention`  ·  implements/extends DSV4FlexInnerAttention
- def: [`torchtitan/models/deepseek_v4/attention.py:324`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L324)
- signature: `class CompressedSparseAttention(DSV4FlexInnerAttention):`
- members:
  - <a id="CompressedSparseAttention.forward"></a>`forward(self, q, swa_k, cmp_k, idx_q, idx_k, idx_w, attn_sink, *, attention_masks=None)` — [`L329`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L329)
- uses (calls/refs, reference-scoped): [`_forward_impl`](attention.md#DSV4FlexInnerAttention._forward_impl), [`DSV4FlexInnerAttention`](attention.md#DSV4FlexInnerAttention)
- used by: [`_make_v4_attn_config`](__init__.md#_make_v4_attn_config), [`forward`](../common/attention.md#FlexInnerAttention.forward), [`DSV4FlexInnerAttention`](attention.md#DSV4FlexInnerAttention)

### <a id="CompressedSparseAttention.Config"></a>`CompressedSparseAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/attention.py:326`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L326)
- signature: `class Config(DSV4FlexInnerAttention.Config):`
- uses (calls/refs, reference-scoped): [`DSV4FlexInnerAttention`](attention.md#DSV4FlexInnerAttention), [`Config`](attention.md#DSV4FlexInnerAttention.Config)
- used by: [`_make_v4_attn_config`](__init__.md#_make_v4_attn_config)

### <a id="DSV4FlexInnerAttention"></a>`DSV4FlexInnerAttention`  ·  implements/extends FlexInnerAttention
- def: [`torchtitan/models/deepseek_v4/attention.py:30`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L30) — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
- doc: DeepSeek sparse attention core for DeepSeek-V4.
- signature: `class DSV4FlexInnerAttention(FlexInnerAttention):`
- members:
  - <a id="DSV4FlexInnerAttention._build_block_mask"></a>`_build_block_mask(self, bsz: int, seqlen: int, kv_len: int, selected_indices: torch.Tensor, device)` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L129) — Build a FlexInnerAttention block mask from selected KV indices.
  - <a id="DSV4FlexInnerAttention._forward_impl"></a>`_forward_impl(self, q, swa_k, attn_sink, *, cmp_k=None, idx_q=None, idx_k=None, idx_w=None, attention_masks=None)` — [`L193`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L193) — Run DSV4 sparse attention over a folded token stream. — documented in [deepseek-v4-model](../../../../concepts/deepseek-v4-model.md)
  - <a id="DSV4FlexInnerAttention.dsa_mask_mod"></a>`dsa_mask_mod(b, h, q_idx, kv_idx)` — [`L182`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L182)
  - <a id="DSV4FlexInnerAttention.get_compress_topk_idxs"></a>`get_compress_topk_idxs(self, *, bsz: int, seqlen: int, n_cmp: int, device)` — [`L100`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L100) — Return causal compressed KV indices in the concatenated KV space.
  - <a id="DSV4FlexInnerAttention.get_window_topk_idxs"></a>`get_window_topk_idxs(self, *, bsz: int, seqlen: int, device)` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L76) — Return sliding-window KV indices in the concatenated KV space.
  - <a id="DSV4FlexInnerAttention.v4_sink_score_mod"></a>`v4_sink_score_mod(score, b, h, q_idx, kv_idx)` — [`L267`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L267)
  - <a id="DSV4FlexInnerAttention.block_size"></a>`block_size` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L74)
  - <a id="DSV4FlexInnerAttention.compress_ratio"></a>`compress_ratio` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L71)
  - <a id="DSV4FlexInnerAttention.index_topk"></a>`index_topk` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L73)
  - <a id="DSV4FlexInnerAttention.softmax_scale"></a>`softmax_scale` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L72)
  - <a id="DSV4FlexInnerAttention.window_size"></a>`window_size` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L70)
- protocol/private: <a id="DSV4FlexInnerAttention.__init__"></a>`__init__`[`L68`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L68)
- uses (calls/refs, reference-scoped): [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`forward`](../common/attention.md#FlexInnerAttention.forward), [`Config`](attention.md#DSV4FlexInnerAttention.Config), [`Indexer`](compressor.md#Indexer), [`block_size`](../common/attention.md#FlexInnerAttention.Config.block_size), [`SlidingWindowAttention`](attention.md#SlidingWindowAttention), [`__init__`](../common/attention.md#FlexInnerAttention.__init__), [`CompressedSparseAttention`](attention.md#CompressedSparseAttention), [`HeavilyCompressedAttention`](attention.md#HeavilyCompressedAttention), [`index_topk`](attention.md#DSV4FlexInnerAttention.Config.index_topk), [`window_size`](attention.md#DSV4FlexInnerAttention.Config.window_size), [`softmax_scale`](attention.md#DSV4FlexInnerAttention.Config.softmax_scale), [`compress_ratio`](attention.md#DSV4FlexInnerAttention.Config.compress_ratio), [`select`](compressor.md#Indexer.select)
- used by: [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`inner_attention`](attention.md#Attention.Config.inner_attention), [`Config`](attention.md#CompressedSparseAttention.Config), [`Config`](attention.md#SlidingWindowAttention.Config), [`SlidingWindowAttention`](attention.md#SlidingWindowAttention), [`Config`](attention.md#HeavilyCompressedAttention.Config), [`CompressedSparseAttention`](attention.md#CompressedSparseAttention), [`HeavilyCompressedAttention`](attention.md#HeavilyCompressedAttention), [`forward`](attention.md#CompressedSparseAttention.forward), [`forward`](attention.md#HeavilyCompressedAttention.forward), [`forward`](attention.md#SlidingWindowAttention.forward)

### <a id="DSV4FlexInnerAttention.Config"></a>`DSV4FlexInnerAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/attention.py:62`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L62)
- signature: `class Config(FlexInnerAttention.Config):`
- members:
  - <a id="DSV4FlexInnerAttention.Config.compress_ratio"></a>`compress_ratio` — [`L64`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L64)
  - <a id="DSV4FlexInnerAttention.Config.index_topk"></a>`index_topk` — [`L66`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L66)
  - <a id="DSV4FlexInnerAttention.Config.softmax_scale"></a>`softmax_scale` — [`L65`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L65)
  - <a id="DSV4FlexInnerAttention.Config.window_size"></a>`window_size` — [`L63`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L63)
- uses (calls/refs, reference-scoped): [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`Config`](../common/attention.md#FlexInnerAttention.Config)
- used by: [`get_nparams_and_flops`](model.md#DeepSeekV4Model.Config.get_nparams_and_flops), [`_make_mtp_inner_block`](__init__.md#_make_mtp_inner_block), [`inner_attention`](attention.md#Attention.Config.inner_attention), [`compress_ratio`](attention.md#DSV4FlexInnerAttention.compress_ratio), [`Config`](attention.md#CompressedSparseAttention.Config), [`Config`](attention.md#SlidingWindowAttention.Config), [`Config`](attention.md#HeavilyCompressedAttention.Config), [`__init__`](attention.md#DSV4FlexInnerAttention.__init__), [`index_topk`](attention.md#DSV4FlexInnerAttention.index_topk), [`softmax_scale`](attention.md#DSV4FlexInnerAttention.softmax_scale), [`window_size`](attention.md#DSV4FlexInnerAttention.window_size)

### <a id="HeavilyCompressedAttention"></a>`HeavilyCompressedAttention`  ·  implements/extends DSV4FlexInnerAttention
- def: [`torchtitan/models/deepseek_v4/attention.py:301`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L301)
- signature: `class HeavilyCompressedAttention(DSV4FlexInnerAttention):`
- members:
  - <a id="HeavilyCompressedAttention.forward"></a>`forward(self, q, swa_k, cmp_k, attn_sink, *, attention_masks=None)` — [`L306`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L306)
- uses (calls/refs, reference-scoped): [`_forward_impl`](attention.md#DSV4FlexInnerAttention._forward_impl), [`DSV4FlexInnerAttention`](attention.md#DSV4FlexInnerAttention)
- used by: [`_make_v4_attn_config`](__init__.md#_make_v4_attn_config), [`forward`](../common/attention.md#FlexInnerAttention.forward), [`DSV4FlexInnerAttention`](attention.md#DSV4FlexInnerAttention)

### <a id="HeavilyCompressedAttention.Config"></a>`HeavilyCompressedAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/attention.py:303`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L303)
- signature: `class Config(DSV4FlexInnerAttention.Config):`
- uses (calls/refs, reference-scoped): [`DSV4FlexInnerAttention`](attention.md#DSV4FlexInnerAttention), [`Config`](attention.md#DSV4FlexInnerAttention.Config)

### <a id="SlidingWindowAttention"></a>`SlidingWindowAttention`  ·  implements/extends DSV4FlexInnerAttention
- def: [`torchtitan/models/deepseek_v4/attention.py:280`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L280)
- signature: `class SlidingWindowAttention(DSV4FlexInnerAttention):`
- members:
  - <a id="SlidingWindowAttention.forward"></a>`forward(self, q, swa_k, attn_sink, *, attention_masks=None)` — [`L285`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L285)
- uses (calls/refs, reference-scoped): [`_forward_impl`](attention.md#DSV4FlexInnerAttention._forward_impl), [`DSV4FlexInnerAttention`](attention.md#DSV4FlexInnerAttention)
- used by: [`_make_v4_attn_config`](__init__.md#_make_v4_attn_config), [`_make_mtp_inner_block`](__init__.md#_make_mtp_inner_block), [`forward`](../common/attention.md#FlexInnerAttention.forward), [`DSV4FlexInnerAttention`](attention.md#DSV4FlexInnerAttention)

### <a id="SlidingWindowAttention.Config"></a>`SlidingWindowAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/deepseek_v4/attention.py:282`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L282)
- signature: `class Config(DSV4FlexInnerAttention.Config):`
- uses (calls/refs, reference-scoped): [`DSV4FlexInnerAttention`](attention.md#DSV4FlexInnerAttention), [`Config`](attention.md#DSV4FlexInnerAttention.Config)
- used by: [`_make_mtp_inner_block`](__init__.md#_make_mtp_inner_block)

## Functions
- <a id="_assert_spmd_attention_type"></a>`_assert_spmd_attention_type(tensor, *, tp)` — [`L22`](../../../../../../../raw/code/torchtitan/torchtitan/models/deepseek_v4/attention.py#L22)

