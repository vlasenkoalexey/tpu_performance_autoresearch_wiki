---
title: 'Module: torchtitan/models/qwen3_5/model.py'
type: catalog
provenance: extracted
module: torchtitan/models/qwen3_5/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.qwen3_5.model`/
symbols:
  Qwen35Model.preprocess_inputs: Qwen35Model#preprocess_inputs().
  Qwen35Model.Config.get_nparams_and_flops: Qwen35Model#Config#get_nparams_and_flops().
  Qwen35Attention.forward: Qwen35Attention#forward().
  Qwen35Model: Qwen35Model#
  Qwen35Model.Config: Qwen35Model#Config#
  Qwen35TransformerBlock.forward: Qwen35TransformerBlock#forward().
  Qwen35Model.Config.vision_encoder: Qwen35Model#Config#vision_encoder.
  Qwen35Model.get_attention_masks: Qwen35Model#get_attention_masks().
  Qwen35Model.forward: Qwen35Model#forward().
  OffsetRMSNorm: OffsetRMSNorm#
  OffsetRMSNorm.Config: OffsetRMSNorm#Config#
  Qwen35Attention: Qwen35Attention#
  Qwen35TransformerBlock: Qwen35TransformerBlock#
  Qwen35TransformerBlock.attn: Qwen35TransformerBlock#attn.
  Qwen35Attention.rotary_dim: Qwen35Attention#rotary_dim.
  Qwen35Model.Config.update_from_config: Qwen35Model#Config#update_from_config().
  Qwen35Attention.Config: Qwen35Attention#Config#
  Qwen35TransformerBlock.Config: Qwen35TransformerBlock#Config#
  Qwen35Attention.head_dim: Qwen35Attention#head_dim.
  Qwen35TransformerBlock.Config.attention: Qwen35TransformerBlock#Config#attention.
  Qwen35TransformerBlock.Config.delta_net: Qwen35TransformerBlock#Config#delta_net.
  Qwen35TransformerBlock.Config.moe: Qwen35TransformerBlock#Config#moe.
  Qwen35Model._prepare_multimodal_embeds: Qwen35Model#_prepare_multimodal_embeds().
  Qwen35TransformerBlock.Config.feed_forward: Qwen35TransformerBlock#Config#feed_forward.
  Qwen35Model.vision_encoder: Qwen35Model#vision_encoder.
  Qwen35TransformerBlock.moe: Qwen35TransformerBlock#moe.
  Qwen35AttentionMaskDict: Qwen35AttentionMaskDict.
  Qwen35TransformerBlock.Config.attention_norm: Qwen35TransformerBlock#Config#attention_norm.
  Qwen35TransformerBlock.Config.ffn_norm: Qwen35TransformerBlock#Config#ffn_norm.
  OffsetRMSNorm.forward: OffsetRMSNorm#forward().
  Qwen35TransformerBlock.moe_enabled: Qwen35TransformerBlock#moe_enabled.
  Qwen35Attention.Config.rope: Qwen35Attention#Config#rope.
  Qwen35Attention.Config.wq: Qwen35Attention#Config#wq.
  Qwen35Attention.Config.wk: Qwen35Attention#Config#wk.
  Qwen35Attention.Config.wv: Qwen35Attention#Config#wv.
  Qwen35Attention.Config.wo: Qwen35Attention#Config#wo.
  Qwen35Attention.Config.q_norm: Qwen35Attention#Config#q_norm.
  Qwen35Attention.Config.k_norm: Qwen35Attention#Config#k_norm.
  Qwen35Attention.Config.inner_attention: Qwen35Attention#Config#inner_attention.
  Qwen35Attention.wq: Qwen35Attention#wq.
  Qwen35Attention.wk: Qwen35Attention#wk.
  Qwen35Attention.wv: Qwen35Attention#wv.
  Qwen35Attention.q_norm: Qwen35Attention#q_norm.
  Qwen35Attention.k_norm: Qwen35Attention#k_norm.
  Qwen35Attention.rope: Qwen35Attention#rope.
  Qwen35Attention.inner_attention: Qwen35Attention#inner_attention.
  Qwen35Attention.enable_gqa: Qwen35Attention#enable_gqa.
  Qwen35Attention.wo: Qwen35Attention#wo.
  Qwen35TransformerBlock.attention_norm: Qwen35TransformerBlock#attention_norm.
  Qwen35TransformerBlock.ffn_norm: Qwen35TransformerBlock#ffn_norm.
  Qwen35TransformerBlock.feed_forward: Qwen35TransformerBlock#feed_forward.
  Qwen35TransformerBlock.full_attn: Qwen35TransformerBlock#full_attn.
  Qwen35Model.__init__: Qwen35Model#__init__().
  Qwen35Model.spatial_merge_size: Qwen35Model#spatial_merge_size.
  Qwen35Attention.scaling: Qwen35Attention#scaling.
  Qwen35TransformerBlock.attn_mask_key: Qwen35TransformerBlock#attn_mask_key.
  OffsetRMSNorm.eps: OffsetRMSNorm#eps.
  OffsetRMSNorm.weight: OffsetRMSNorm#weight.
  Qwen35Model._get_vision_embeds: Qwen35Model#_get_vision_embeds().
  Qwen35Attention.Config.head_dim: Qwen35Attention#Config#head_dim.
  OffsetRMSNorm.__init__: OffsetRMSNorm#__init__().
  Qwen35Attention.n_heads: Qwen35Attention#n_heads.
  Qwen35Attention.n_kv_heads: Qwen35Attention#n_kv_heads.
  Qwen35Attention.Config.n_heads: Qwen35Attention#Config#n_heads.
  Qwen35Attention.__init__: Qwen35Attention#__init__().
  Qwen35TransformerBlock.__init__: Qwen35TransformerBlock#__init__().
  OffsetRMSNorm.Config.dim: OffsetRMSNorm#Config#dim.
  OffsetRMSNorm.Config.eps: OffsetRMSNorm#Config#eps.
  Qwen35Attention.Config.n_kv_heads: Qwen35Attention#Config#n_kv_heads.
  Qwen35Attention.Config.rotary_dim: Qwen35Attention#Config#rotary_dim.
---
# Module: [`torchtitan/models/qwen3_5/model.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py)

## Classes
### <a id="OffsetRMSNorm"></a>`OffsetRMSNorm`  ·  implements/extends Module
- def: [`torchtitan/models/qwen3_5/model.py:62`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L62) — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- doc: RMSNorm with offset: `(1 + weight) * norm(x)`.
- signature: `class OffsetRMSNorm(Module):`
- members:
  - <a id="OffsetRMSNorm.forward"></a>`forward(self, x: torch.Tensor)` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L78)
  - <a id="OffsetRMSNorm.eps"></a>`eps` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L75)
  - <a id="OffsetRMSNorm.weight"></a>`weight` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L76)
- protocol/private: <a id="OffsetRMSNorm.__init__"></a>`__init__`[`L73`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L73)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`forward`](../../overrides/offset_rmsnorm.md#TritonOffsetRMSNorm.forward), [`Config`](model.md#OffsetRMSNorm.Config), [`TritonOffsetRMSNorm`](../../overrides/offset_rmsnorm.md#TritonOffsetRMSNorm), [`dim`](model.md#OffsetRMSNorm.Config.dim), [`eps`](model.md#OffsetRMSNorm.Config.eps)
- used by: [`Module`](../../protocols/module.md#Module), [`_offset_norm`](__init__.md#_offset_norm), [`triton_offset_rmsnorm`](../../overrides/offset_rmsnorm.md#triton_offset_rmsnorm), [`forward`](../../overrides/offset_rmsnorm.md#TritonOffsetRMSNorm.forward), [`attention_norm`](model.md#Qwen35TransformerBlock.Config.attention_norm), [`ffn_norm`](model.md#Qwen35TransformerBlock.Config.ffn_norm), [`Config`](../../overrides/offset_rmsnorm.md#TritonOffsetRMSNorm.Config), [`k_norm`](model.md#Qwen35Attention.Config.k_norm), [`q_norm`](model.md#Qwen35Attention.Config.q_norm), [`__init__`](../../overrides/offset_rmsnorm.md#TritonOffsetRMSNorm.__init__), [`TritonOffsetRMSNorm`](../../overrides/offset_rmsnorm.md#TritonOffsetRMSNorm)

### <a id="OffsetRMSNorm.Config"></a>`OffsetRMSNorm.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3_5/model.py:69`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L69)
- signature: `class Config(Module.Config):`
- members:
  - <a id="OffsetRMSNorm.Config.dim"></a>`dim` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L70)
  - <a id="OffsetRMSNorm.Config.eps"></a>`eps` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L71)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config)
- used by: [`_offset_norm`](__init__.md#_offset_norm), [`triton_offset_rmsnorm`](../../overrides/offset_rmsnorm.md#triton_offset_rmsnorm), [`attention_norm`](model.md#Qwen35TransformerBlock.Config.attention_norm), [`ffn_norm`](model.md#Qwen35TransformerBlock.Config.ffn_norm), [`Config`](../../overrides/offset_rmsnorm.md#TritonOffsetRMSNorm.Config), [`k_norm`](model.md#Qwen35Attention.Config.k_norm), [`q_norm`](model.md#Qwen35Attention.Config.q_norm), [`eps`](model.md#OffsetRMSNorm.eps), [`weight`](model.md#OffsetRMSNorm.weight), [`__init__`](model.md#OffsetRMSNorm.__init__)

### <a id="Qwen35Attention"></a>`Qwen35Attention`  ·  implements/extends BaseAttention
- def: [`torchtitan/models/qwen3_5/model.py:87`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L87)
- doc: Full attention with output gating and partial RoPE for Qwen3.5.
- signature: `class Qwen35Attention(BaseAttention):`
- members:
  - <a id="Qwen35Attention.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None)` — [`L138`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L138)
  - <a id="Qwen35Attention.enable_gqa"></a>`enable_gqa` — [`L122`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L122)
  - <a id="Qwen35Attention.head_dim"></a>`head_dim` — [`L120`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L120)
  - <a id="Qwen35Attention.inner_attention"></a>`inner_attention` — [`L136`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L136)
  - <a id="Qwen35Attention.k_norm"></a>`k_norm` — [`L132`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L132)
  - <a id="Qwen35Attention.n_heads"></a>`n_heads` — [`L118`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L118)
  - <a id="Qwen35Attention.n_kv_heads"></a>`n_kv_heads` — [`L119`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L119)
  - <a id="Qwen35Attention.q_norm"></a>`q_norm` — [`L131`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L131)
  - <a id="Qwen35Attention.rope"></a>`rope` — [`L129`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L129)
  - <a id="Qwen35Attention.rotary_dim"></a>`rotary_dim` — [`L121`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L121)
  - <a id="Qwen35Attention.scaling"></a>`scaling` — [`L134`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L134)
  - <a id="Qwen35Attention.wk"></a>`wk` — [`L125`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L125)
  - <a id="Qwen35Attention.wo"></a>`wo` — [`L127`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L127)
  - <a id="Qwen35Attention.wq"></a>`wq` — [`L124`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L124)
  - <a id="Qwen35Attention.wv"></a>`wv` — [`L126`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L126)
- protocol/private: <a id="Qwen35Attention.__init__"></a>`__init__`[`L116`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L116)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`BaseAttention`](../common/attention.md#BaseAttention), [`forward`](../../experiments/tpu/qwen3_5/model.md#TpuQwen35Attention.forward), [`Config`](model.md#Qwen35Attention.Config), [`inner_attention`](model.md#Qwen35Attention.Config.inner_attention), [`k_norm`](model.md#Qwen35Attention.Config.k_norm), [`q_norm`](model.md#Qwen35Attention.Config.q_norm), [`rope`](model.md#Qwen35Attention.Config.rope), [`wk`](model.md#Qwen35Attention.Config.wk), [`wo`](model.md#Qwen35Attention.Config.wo), [`wq`](model.md#Qwen35Attention.Config.wq), [`wv`](model.md#Qwen35Attention.Config.wv), [`TpuQwen35Attention`](../../experiments/tpu/qwen3_5/model.md#TpuQwen35Attention), [`head_dim`](model.md#Qwen35Attention.Config.head_dim), [`n_heads`](model.md#Qwen35Attention.Config.n_heads), [`n_kv_heads`](model.md#Qwen35Attention.Config.n_kv_heads), [`rotary_dim`](model.md#Qwen35Attention.Config.rotary_dim)
- used by: [`_qwen35_attention_config`](__init__.md#_qwen35_attention_config), [`_set_full_attention_sharding`](sharding.md#_set_full_attention_sharding), [`BaseAttention`](../common/attention.md#BaseAttention), [`get_nparams_and_flops`](model.md#Qwen35Model.Config.get_nparams_and_flops), [`forward`](../../experiments/tpu/qwen3_5/model.md#TpuQwen35Attention.forward), [`TP`](sharding.md#TP), [`attention`](model.md#Qwen35TransformerBlock.Config.attention), [`Config`](../../experiments/tpu/qwen3_5/model.md#TpuQwen35Attention.Config), [`TpuQwen35Attention`](../../experiments/tpu/qwen3_5/model.md#TpuQwen35Attention)

### <a id="Qwen35Attention.Config"></a>`Qwen35Attention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3_5/model.py:102`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L102)
- signature: `class Config(BaseAttention.Config):`
- members:
  - <a id="Qwen35Attention.Config.head_dim"></a>`head_dim` — [`L105`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L105)
  - <a id="Qwen35Attention.Config.inner_attention"></a>`inner_attention` — [`L114`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L114)
  - <a id="Qwen35Attention.Config.k_norm"></a>`k_norm` — [`L113`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L113)
  - <a id="Qwen35Attention.Config.n_heads"></a>`n_heads` — [`L103`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L103)
  - <a id="Qwen35Attention.Config.n_kv_heads"></a>`n_kv_heads` — [`L104`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L104)
  - <a id="Qwen35Attention.Config.q_norm"></a>`q_norm` — [`L112`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L112)
  - <a id="Qwen35Attention.Config.rope"></a>`rope` — [`L107`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L107)
  - <a id="Qwen35Attention.Config.rotary_dim"></a>`rotary_dim` — [`L106`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L106)
  - <a id="Qwen35Attention.Config.wk"></a>`wk` — [`L109`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L109)
  - <a id="Qwen35Attention.Config.wo"></a>`wo` — [`L111`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L111)
  - <a id="Qwen35Attention.Config.wq"></a>`wq` — [`L108`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L108)
  - <a id="Qwen35Attention.Config.wv"></a>`wv` — [`L110`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L110)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`Config`](../../protocols/module.md#Module.Config), [`BaseAttention`](../common/attention.md#BaseAttention), [`Config`](../common/attention.md#BaseAttention.Config), [`Config`](rope.md#MRoPE.Config), [`MRoPE`](rope.md#MRoPE), [`OffsetRMSNorm`](model.md#OffsetRMSNorm), [`Config`](model.md#OffsetRMSNorm.Config)
- used by: [`_qwen35_attention_config`](__init__.md#_qwen35_attention_config), [`_set_full_attention_sharding`](sharding.md#_set_full_attention_sharding), [`get_nparams_and_flops`](model.md#Qwen35Model.Config.get_nparams_and_flops), [`rotary_dim`](model.md#Qwen35Attention.rotary_dim), [`head_dim`](model.md#Qwen35Attention.head_dim), [`attention`](model.md#Qwen35TransformerBlock.Config.attention), [`Config`](../../experiments/tpu/qwen3_5/model.md#TpuQwen35Attention.Config), [`inner_attention`](model.md#Qwen35Attention.inner_attention), [`k_norm`](model.md#Qwen35Attention.k_norm), [`q_norm`](model.md#Qwen35Attention.q_norm), [`rope`](model.md#Qwen35Attention.rope), [`wk`](model.md#Qwen35Attention.wk), [`wo`](model.md#Qwen35Attention.wo), [`wq`](model.md#Qwen35Attention.wq), [`wv`](model.md#Qwen35Attention.wv), [`n_heads`](model.md#Qwen35Attention.n_heads), [`n_kv_heads`](model.md#Qwen35Attention.n_kv_heads), [`__init__`](model.md#Qwen35Attention.__init__)

### <a id="Qwen35Model"></a>`Qwen35Model`  ·  implements/extends Decoder
- def: [`torchtitan/models/qwen3_5/model.py:248`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L248) — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- doc: Qwen3.5: Multimodal model with hybrid attention.
- signature: `class Qwen35Model(Decoder):`
- members:
  - <a id="Qwen35Model._get_vision_embeds"></a>`_get_vision_embeds(self, pixel_values: torch.Tensor, *, grid_thw: torch.Tensor)` — [`L512`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L512) — Run the vision encoder and return packed embeddings with token counts.
  - <a id="Qwen35Model._prepare_multimodal_embeds"></a>`_prepare_multimodal_embeds(self, tokens: torch.Tensor, *, pixel_values: torch.Tensor | None, pixel_values_videos: torch.Tensor | None, grid_thw: torch.Tensor | None, grid_thw_videos: torch.Tensor | None, special_tokens: dict[str, int] | None)` — [`L538`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L538) — Embed tokens, run vision encoder, scatter vision into text.
  - <a id="Qwen35Model.forward"></a>`forward(self, tokens: torch.Tensor, *, pixel_values: torch.Tensor | None = None, pixel_values_videos: torch.Tensor | None = None, grid_thw: torch.Tensor | None = None, grid_thw_videos: torch.Tensor | None = None, attention_masks: Qwen35AttentionMaskDict | None = None, positions: torch.Tensor | None = None, special_tokens: dict[str, int] | None = None)` — [`L599`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L599)
  - <a id="Qwen35Model.get_attention_masks"></a>`get_attention_masks(self, positions: torch.Tensor, *, padding_mask: torch.Tensor | None = None, max_num_documents: int | None = None, max_context_length: int | None = None)` — [`L455`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L455)
  - <a id="Qwen35Model.preprocess_inputs"></a>`preprocess_inputs(self, input_dict: dict[str, torch.Tensor], *, parallel_dims: ParallelDims, parallelism: ParallelismConfig, max_num_documents: int | None = None, max_context_length: int | None = None)` — [`L376`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L376) — Build masks, CP-shard, SPMD-wrap (+ deltanet annotation), and return. — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
  - <a id="Qwen35Model.spatial_merge_size"></a>`spatial_merge_size` — [`L370`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L370)
  - <a id="Qwen35Model.vision_encoder"></a>`vision_encoder` — [`L367`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L367)
- protocol/private: <a id="Qwen35Model.__init__"></a>`__init__`[`L364`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L364)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`ParallelismConfig`](../../config/configs.md#ParallelismConfig), [`ParallelDims`](../../distributed/parallel_dims.md#ParallelDims), [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`MeshAxisName`](../../distributed/parallel_dims.md#MeshAxisName), [`Decoder`](../common/decoder.md#Decoder), [`spmd_backend`](../../config/configs.md#ParallelismConfig.spmd_backend), [`get_spmd_backend`](../../distributed/utils.md#get_spmd_backend), [`get_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_mesh), [`VarlenInnerAttention`](../common/attention.md#VarlenInnerAttention), [`get_attention_masks`](../common/decoder.md#Decoder.get_attention_masks), [`Config`](../common/attention.md#FlexInnerAttention.Config), [`tok_embeddings`](../common/decoder.md#Decoder.tok_embeddings), [`cp_enabled`](../../distributed/parallel_dims.md#ParallelDims.cp_enabled), [`Config`](model.md#Qwen35Model.Config), [`lm_head`](../common/decoder.md#Decoder.lm_head), [`Config`](../common/attention.md#VarlenInnerAttention.Config), [`create_varlen_metadata_for_document`](../common/attention.md#create_varlen_metadata_for_document), [`decoder_input_sharding`](../common/decoder_sharding.md#decoder_input_sharding), [`norm`](../common/decoder.md#Decoder.norm), [`layers`](../common/decoder.md#Decoder.layers), [`vision_encoder`](model.md#Qwen35Model.Config.vision_encoder), [`annotate_input_spmd_types`](../../distributed/spmd_types.md#annotate_input_spmd_types), [`prepare_context_parallel_input`](../../distributed/context_parallel/api.md#prepare_context_parallel_input), [`context_parallel_load_balancer`](../../config/configs.md#ParallelismConfig.context_parallel_load_balancer), [`CP`](../../distributed/parallel_dims.md#MeshAxisName.CP), [`config`](../common/decoder.md#Decoder.config), [`first_full_attention_backend`](../common/decoder.md#Decoder.Config.first_full_attention_backend), [`inner_attention`](../common/attention.md#BaseAttention.Config.inner_attention), [`first_attention`](../common/decoder.md#Decoder.Config.first_attention), [`DP`](../../distributed/parallel_dims.md#MeshAxisName.DP), [`annotate_deltanet_cu_seqlens`](sharding.md#annotate_deltanet_cu_seqlens), [`TP`](../../distributed/parallel_dims.md#MeshAxisName.TP), [`spmd_local_context`](../../distributed/spmd_types.md#spmd_local_context), [`set_current_spmd_mesh`](../../distributed/spmd_types.md#set_current_spmd_mesh), [`spmd_dense_mesh`](../../distributed/parallel_dims.md#ParallelDims.spmd_dense_mesh), [`__init__`](../common/decoder.md#Decoder.__init__), [`Qwen35AttentionMaskDict`](model.md#Qwen35AttentionMaskDict), [`multimodal_input_sharding`](../common/vision_encoder_sharding.md#multimodal_input_sharding), [`_skip_lm_head`](../common/decoder.md#Decoder._skip_lm_head)  (+5 more)
- used by: [`Decoder`](../common/decoder.md#Decoder), [`_27b`](__init__.md#_27b), [`_debugmodel`](__init__.md#_debugmodel), [`_debugmodel_moe`](__init__.md#_debugmodel_moe), [`_35b_a3b`](__init__.md#_35b_a3b), [`_0_8b`](__init__.md#_0_8b), [`_122b_a10b`](__init__.md#_122b_a10b), [`_2b`](__init__.md#_2b), [`_397b_a17b`](__init__.md#_397b_a17b), [`_4b`](__init__.md#_4b), [`_9b`](__init__.md#_9b), [`_qwen3_8_2_4t_a95b`](../qwen3_8/__init__.md#_qwen3_8_2_4t_a95b), [`set_qwen35_sharding_config`](sharding.md#set_qwen35_sharding_config), [`use_tpu_modules`](../../experiments/tpu/qwen3_5/__init__.md#use_tpu_modules), [`get_attention_masks`](../common/decoder.md#Decoder.get_attention_masks), [`preprocess_inputs`](../common/decoder.md#Decoder.preprocess_inputs), [`forward`](../common/decoder.md#Decoder.forward), [`get_nparams_and_flops`](model.md#Qwen35Model.Config.get_nparams_and_flops), [`TP`](sharding.md#TP), [`__init__`](state_dict_adapter.md#Qwen35StateDictAdapter.__init__)

### <a id="Qwen35Model.Config"></a>`Qwen35Model.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3_5/model.py:292`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L292) — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- signature: `class Config(Decoder.Config):`
- members:
  - <a id="Qwen35Model.Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L332`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L332)
  - <a id="Qwen35Model.Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L295`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L295)
  - <a id="Qwen35Model.Config.vision_encoder"></a>`vision_encoder` — [`L293`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L293) — documented in [qwen3-5-model](../../../../concepts/qwen3-5-model.md)
- uses (calls/refs, reference-scoped): [`out_features`](../common/linear.md#Linear.Config.out_features), [`layers`](../common/decoder.md#Decoder.Config.layers), [`Decoder`](../common/decoder.md#Decoder), [`set_qwen35_sharding_config`](sharding.md#set_qwen35_sharding_config), [`update_from_config`](../common/decoder.md#Decoder.Config.update_from_config), [`Config`](../common/decoder.md#Decoder.Config), [`get_nparams_and_active_nparams`](../utils.md#get_nparams_and_active_nparams), [`quadratic_attention_flops_per_token`](../utils.md#quadratic_attention_flops_per_token), [`GatedDeltaNet`](gdn.md#GatedDeltaNet), [`Qwen35Attention`](model.md#Qwen35Attention), [`Config`](gdn.md#GatedDeltaNet.Config), [`Config`](model.md#Qwen35Attention.Config), [`Config`](vision_encoder.md#Qwen35VisionEncoder.Config), [`vision_encoder`](model.md#Qwen35Model.vision_encoder), [`Qwen35VisionEncoder`](vision_encoder.md#Qwen35VisionEncoder), [`in_proj_v`](gdn.md#GatedDeltaNet.Config.in_proj_v), [`value_head_dim`](gdn.md#GatedDeltaNet.Config.value_head_dim), [`delta_rule_flops_per_token`](../utils.md#delta_rule_flops_per_token), [`head_dim`](model.md#Qwen35Attention.Config.head_dim), [`key_head_dim`](gdn.md#GatedDeltaNet.Config.key_head_dim), [`n_heads`](model.md#Qwen35Attention.Config.n_heads)
- used by: [`_27b`](__init__.md#_27b), [`_debugmodel`](__init__.md#_debugmodel), [`_debugmodel_moe`](__init__.md#_debugmodel_moe), [`_35b_a3b`](__init__.md#_35b_a3b), [`_0_8b`](__init__.md#_0_8b), [`_122b_a10b`](__init__.md#_122b_a10b), [`_2b`](__init__.md#_2b), [`_397b_a17b`](__init__.md#_397b_a17b), [`_4b`](__init__.md#_4b), [`_9b`](__init__.md#_9b), [`_qwen3_8_2_4t_a95b`](../qwen3_8/__init__.md#_qwen3_8_2_4t_a95b), [`set_qwen35_sharding_config`](sharding.md#set_qwen35_sharding_config), [`use_tpu_modules`](../../experiments/tpu/qwen3_5/__init__.md#use_tpu_modules), [`to_hf`](state_dict_adapter.md#Qwen35StateDictAdapter.to_hf), [`from_hf_map`](state_dict_adapter.md#Qwen35StateDictAdapter.from_hf_map), [`hf_language_model_prefix`](state_dict_adapter.md#Qwen35StateDictAdapter.hf_language_model_prefix), [`vision_encoder`](model.md#Qwen35Model.vision_encoder), [`__init__`](state_dict_adapter.md#Qwen35StateDictAdapter.__init__), [`__init__`](model.md#Qwen35Model.__init__), [`spatial_merge_size`](model.md#Qwen35Model.spatial_merge_size)

### <a id="Qwen35TransformerBlock"></a>`Qwen35TransformerBlock`  ·  implements/extends Module
- def: [`torchtitan/models/qwen3_5/model.py:185`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L185)
- doc: Hybrid transformer block for Qwen3.5.
- signature: `class Qwen35TransformerBlock(Module):`
- members:
  - <a id="Qwen35TransformerBlock.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks: Qwen35AttentionMaskDict | None, positions: torch.Tensor | None = None)` — [`L224`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L224)
  - <a id="Qwen35TransformerBlock.attention_norm"></a>`attention_norm` — [`L221`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L221)
  - <a id="Qwen35TransformerBlock.attn"></a>`attn` — [`L208`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L208)
  - <a id="Qwen35TransformerBlock.attn_mask_key"></a>`attn_mask_key` — [`L205`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L205)
  - <a id="Qwen35TransformerBlock.feed_forward"></a>`feed_forward` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L219)
  - <a id="Qwen35TransformerBlock.ffn_norm"></a>`ffn_norm` — [`L222`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L222)
  - <a id="Qwen35TransformerBlock.full_attn"></a>`full_attn` — [`L204`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L204)
  - <a id="Qwen35TransformerBlock.moe"></a>`moe` — [`L216`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L216)
  - <a id="Qwen35TransformerBlock.moe_enabled"></a>`moe_enabled` — [`L213`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L213)
- protocol/private: <a id="Qwen35TransformerBlock.__init__"></a>`__init__`[`L202`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L202)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`forward`](../../experiments/tpu/qwen3_5/model.md#TpuQwen35TransformerBlock.forward), [`Config`](model.md#Qwen35TransformerBlock.Config), [`attention`](model.md#Qwen35TransformerBlock.Config.attention), [`delta_net`](model.md#Qwen35TransformerBlock.Config.delta_net), [`moe`](model.md#Qwen35TransformerBlock.Config.moe), [`feed_forward`](model.md#Qwen35TransformerBlock.Config.feed_forward), [`Qwen35AttentionMaskDict`](model.md#Qwen35AttentionMaskDict), [`attention_norm`](model.md#Qwen35TransformerBlock.Config.attention_norm), [`ffn_norm`](model.md#Qwen35TransformerBlock.Config.ffn_norm), [`TpuQwen35TransformerBlock`](../../experiments/tpu/qwen3_5/model.md#TpuQwen35TransformerBlock)
- used by: [`Module`](../../protocols/module.md#Module), [`_build_qwen35_moe_layers`](__init__.md#_build_qwen35_moe_layers), [`_set_qwen35_layer_sharding`](sharding.md#_set_qwen35_layer_sharding), [`_build_qwen35_layers`](__init__.md#_build_qwen35_layers), [`TP`](sharding.md#TP), [`forward`](../../experiments/tpu/qwen3_5/model.md#TpuQwen35TransformerBlock.forward), [`Config`](../../experiments/tpu/qwen3_5/model.md#TpuQwen35TransformerBlock.Config), [`TpuQwen35TransformerBlock`](../../experiments/tpu/qwen3_5/model.md#TpuQwen35TransformerBlock)

### <a id="Qwen35TransformerBlock.Config"></a>`Qwen35TransformerBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/qwen3_5/model.py:194`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L194)
- signature: `class Config(Module.Config):`
- members:
  - <a id="Qwen35TransformerBlock.Config.attention"></a>`attention` — [`L195`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L195)
  - <a id="Qwen35TransformerBlock.Config.attention_norm"></a>`attention_norm` — [`L199`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L199)
  - <a id="Qwen35TransformerBlock.Config.delta_net"></a>`delta_net` — [`L196`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L196)
  - <a id="Qwen35TransformerBlock.Config.feed_forward"></a>`feed_forward` — [`L197`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L197)
  - <a id="Qwen35TransformerBlock.Config.ffn_norm"></a>`ffn_norm` — [`L200`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L200)
  - <a id="Qwen35TransformerBlock.Config.moe"></a>`moe` — [`L198`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L198)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Config`](../../protocols/module.md#Module.Config), [`OffsetRMSNorm`](model.md#OffsetRMSNorm), [`GatedDeltaNet`](gdn.md#GatedDeltaNet), [`Config`](model.md#OffsetRMSNorm.Config), [`Qwen35Attention`](model.md#Qwen35Attention), [`Config`](gdn.md#GatedDeltaNet.Config), [`Config`](model.md#Qwen35Attention.Config)
- used by: [`_build_qwen35_moe_layers`](__init__.md#_build_qwen35_moe_layers), [`_set_qwen35_layer_sharding`](sharding.md#_set_qwen35_layer_sharding), [`_build_qwen35_layers`](__init__.md#_build_qwen35_layers), [`attn`](model.md#Qwen35TransformerBlock.attn), [`moe`](model.md#Qwen35TransformerBlock.moe), [`moe_enabled`](model.md#Qwen35TransformerBlock.moe_enabled), [`Config`](../../experiments/tpu/qwen3_5/model.md#TpuQwen35TransformerBlock.Config), [`attention_norm`](model.md#Qwen35TransformerBlock.attention_norm), [`feed_forward`](model.md#Qwen35TransformerBlock.feed_forward), [`ffn_norm`](model.md#Qwen35TransformerBlock.ffn_norm), [`full_attn`](model.md#Qwen35TransformerBlock.full_attn), [`__init__`](model.md#Qwen35TransformerBlock.__init__)

## Module values
- <a id="Qwen35AttentionMaskDict"></a>`Qwen35AttentionMaskDict` — [`L59`](../../../../../../../raw/code/torchtitan/torchtitan/models/qwen3_5/model.py#L59)

