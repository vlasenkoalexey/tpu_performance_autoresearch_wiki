---
title: 'Module: torchtitan/models/kimi_k3/model.py'
type: catalog
provenance: extracted
module: torchtitan/models/kimi_k3/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.kimi_k3.model`/
symbols:
  KimiMLAAttention.forward: KimiMLAAttention#forward().
  KimiK3Model.Config.get_nparams_and_flops: KimiK3Model#Config#get_nparams_and_flops().
  KimiK3TransformerBlock.forward: KimiK3TransformerBlock#forward().
  KimiK3Model.preprocess_inputs: KimiK3Model#preprocess_inputs().
  KimiK3Model.forward: KimiK3Model#forward().
  KimiK3Model.get_attention_masks: KimiK3Model#get_attention_masks().
  KimiK3TransformerBlock.Config.delta_attention: KimiK3TransformerBlock#Config#delta_attention.
  KimiK3Model: KimiK3Model#
  KimiK3TransformerBlock.Config.moe: KimiK3TransformerBlock#Config#moe.
  KimiK3Model.Config.layers: KimiK3Model#Config#layers.
  KimiK3Model.vision_encoder: KimiK3Model#vision_encoder.
  KimiK3TransformerBlock.__init__: KimiK3TransformerBlock#__init__().
  KimiMLAAttention.Config.inner_attention: KimiMLAAttention#Config#inner_attention.
  KimiK3TransformerBlock.Config.attention: KimiK3TransformerBlock#Config#attention.
  KimiK3Model.Config: KimiK3Model#Config#
  KimiK3Model.Config.vision_encoder: KimiK3Model#Config#vision_encoder.
  KimiK3Model._prepare_multimodal_embeds: KimiK3Model#_prepare_multimodal_embeds().
  KimiMLAAttention.Config: KimiMLAAttention#Config#
  KimiK3Model.Config.update_from_config: KimiK3Model#Config#update_from_config().
  KimiK3TransformerBlock.Config.feed_forward: KimiK3TransformerBlock#Config#feed_forward.
  KimiK3TransformerBlock.Config.attention_res_norm: KimiK3TransformerBlock#Config#attention_res_norm.
  _apply_attention_residual: _apply_attention_residual().
  KimiK3TransformerBlock.Config: KimiK3TransformerBlock#Config#
  KimiK3TransformerBlock.Config.attention_res_proj: KimiK3TransformerBlock#Config#attention_res_proj.
  KimiK3TransformerBlock.attention: KimiK3TransformerBlock#attention.
  KimiK3TransformerBlock.moe: KimiK3TransformerBlock#moe.
  KimiMLAAttention: KimiMLAAttention#
  KimiMLAAttention.Config.wq_a: KimiMLAAttention#Config#wq_a.
  KimiMLAAttention.Config.q_norm: KimiMLAAttention#Config#q_norm.
  KimiMLAAttention.Config.wq_b: KimiMLAAttention#Config#wq_b.
  KimiMLAAttention.Config.wkv_a: KimiMLAAttention#Config#wkv_a.
  KimiMLAAttention.Config.kv_norm: KimiMLAAttention#Config#kv_norm.
  KimiMLAAttention.Config.wkv_b: KimiMLAAttention#Config#wkv_b.
  KimiMLAAttention.Config.gate: KimiMLAAttention#Config#gate.
  KimiMLAAttention.Config.wo: KimiMLAAttention#Config#wo.
  KimiMLAAttention.q_head_dim: KimiMLAAttention#q_head_dim.
  KimiK3TransformerBlock.Config.attention_norm: KimiK3TransformerBlock#Config#attention_norm.
  KimiK3TransformerBlock.Config.ffn_norm: KimiK3TransformerBlock#Config#ffn_norm.
  KimiK3TransformerBlock.Config.ffn_res_norm: KimiK3TransformerBlock#Config#ffn_res_norm.
  KimiK3TransformerBlock.Config.ffn_res_proj: KimiK3TransformerBlock#Config#ffn_res_proj.
  KimiK3TransformerBlock.delta_attention: KimiK3TransformerBlock#delta_attention.
  KimiK3TransformerBlock.feed_forward: KimiK3TransformerBlock#feed_forward.
  KimiK3TransformerBlock.attention_res_norm: KimiK3TransformerBlock#attention_res_norm.
  KimiK3TransformerBlock.attention_res_proj: KimiK3TransformerBlock#attention_res_proj.
  KimiK3Model.Config.output_res_norm: KimiK3Model#Config#output_res_norm.
  KimiK3Model.Config.output_res_proj: KimiK3Model#Config#output_res_proj.
  KimiMLAAttention.n_heads: KimiMLAAttention#n_heads.
  KimiMLAAttention.wq_a: KimiMLAAttention#wq_a.
  KimiMLAAttention.q_norm: KimiMLAAttention#q_norm.
  KimiMLAAttention.wq_b: KimiMLAAttention#wq_b.
  KimiMLAAttention.wkv_a: KimiMLAAttention#wkv_a.
  KimiMLAAttention.kv_norm: KimiMLAAttention#kv_norm.
  KimiMLAAttention.wkv_b: KimiMLAAttention#wkv_b.
  KimiMLAAttention.gate: KimiMLAAttention#gate.
  KimiMLAAttention.wo: KimiMLAAttention#wo.
  KimiMLAAttention.inner_attention: KimiMLAAttention#inner_attention.
  KimiK3TransformerBlock.attention_norm: KimiK3TransformerBlock#attention_norm.
  KimiK3TransformerBlock.ffn_norm: KimiK3TransformerBlock#ffn_norm.
  KimiK3TransformerBlock.ffn_res_norm: KimiK3TransformerBlock#ffn_res_norm.
  KimiK3TransformerBlock.ffn_res_proj: KimiK3TransformerBlock#ffn_res_proj.
  KimiK3Model.output_res_norm: KimiK3Model#output_res_norm.
  KimiK3Model.output_res_proj: KimiK3Model#output_res_proj.
  KimiK3AttentionMaskDict: KimiK3AttentionMaskDict.
  KimiMLAAttention.v_head_dim: KimiMLAAttention#v_head_dim.
  KimiK3TransformerBlock: KimiK3TransformerBlock#
  KimiK3Model.__init__: KimiK3Model#__init__().
  KimiMLAAttention.qk_nope_head_dim: KimiMLAAttention#qk_nope_head_dim.
  KimiMLAAttention.qk_rope_head_dim: KimiMLAAttention#qk_rope_head_dim.
  KimiMLAAttention.Config.qk_nope_head_dim: KimiMLAAttention#Config#qk_nope_head_dim.
  KimiMLAAttention.Config.qk_rope_head_dim: KimiMLAAttention#Config#qk_rope_head_dim.
  KimiMLAAttention.kv_lora_rank: KimiMLAAttention#kv_lora_rank.
  KimiMLAAttention.scale: KimiMLAAttention#scale.
  KimiK3TransformerBlock.layer_id: KimiK3TransformerBlock#layer_id.
  KimiK3TransformerBlock.attn_res_block_size: KimiK3TransformerBlock#attn_res_block_size.
  KimiK3TransformerBlock.attn_mask_key: KimiK3TransformerBlock#attn_mask_key.
  KimiMLAAttention.Config.v_head_dim: KimiMLAAttention#Config#v_head_dim.
  KimiMLAAttention.__init__: KimiMLAAttention#__init__().
  KimiK3TransformerBlock.moe_enabled: KimiK3TransformerBlock#moe_enabled.
  KimiMLAAttention.Config.kv_lora_rank: KimiMLAAttention#Config#kv_lora_rank.
  KimiK3TransformerBlock.Config.layer_id: KimiK3TransformerBlock#Config#layer_id.
  KimiK3TransformerBlock.Config.attn_res_block_size: KimiK3TransformerBlock#Config#attn_res_block_size.
  KimiMLAAttention.Config.dim: KimiMLAAttention#Config#dim.
---
# Module: [`torchtitan/models/kimi_k3/model.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py)

## Classes
### <a id="KimiK3Model"></a>`KimiK3Model`  ·  implements/extends Decoder
- def: [`torchtitan/models/kimi_k3/model.py:289`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L289)
- signature: `class KimiK3Model(Decoder):`
- members:
  - <a id="KimiK3Model.forward"></a>`forward(self, tokens: torch.Tensor, *, pixel_values: torch.Tensor | None = None, grid_thw: torch.Tensor | None = None, pixel_values_videos: torch.Tensor | None = None, grid_thw_videos: torch.Tensor | None = None, special_tokens: dict[str, int] | None = None, positions: torch.Tensor | None = None, attention_masks: KimiK3AttentionMaskDict | None = None)` — [`L461`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L461) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3Model.get_attention_masks"></a>`get_attention_masks(self, positions: torch.Tensor, *, padding_mask: torch.Tensor | None = None, max_num_documents: int | None = None, max_context_length: int | None = None)` — [`L385`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L385) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3Model.preprocess_inputs"></a>`preprocess_inputs(self, input_dict: dict[str, torch.Tensor], *, parallel_dims: ParallelDims, parallelism: ParallelismConfig, max_num_documents: int | None = None, max_context_length: int | None = None)` — [`L340`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L340) — Build masks and annotate K3 multimodal inputs. — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3Model.output_res_norm"></a>`output_res_norm` — [`L334`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L334) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3Model.output_res_proj"></a>`output_res_proj` — [`L335`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L335) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3Model.vision_encoder"></a>`vision_encoder` — [`L336`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L336) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- protocol/private: <a id="KimiK3Model.__init__"></a>`__init__`[`L332`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L332), <a id="KimiK3Model._prepare_multimodal_embeds"></a>`_prepare_multimodal_embeds`[`L420`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L420)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`ParallelismConfig`](../../config/configs.md#ParallelismConfig), [`ParallelDims`](../../distributed/parallel_dims.md#ParallelDims), [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`MeshAxisName`](../../distributed/parallel_dims.md#MeshAxisName), [`Decoder`](../common/decoder.md#Decoder), [`spmd_backend`](../../config/configs.md#ParallelismConfig.spmd_backend), [`VarlenInnerAttention`](../common/attention.md#VarlenInnerAttention), [`get_attention_masks`](../common/decoder.md#Decoder.get_attention_masks), [`Config`](../common/attention.md#FlexInnerAttention.Config), [`tok_embeddings`](../common/decoder.md#Decoder.tok_embeddings), [`lm_head`](../common/decoder.md#Decoder.lm_head), [`Config`](../common/attention.md#VarlenInnerAttention.Config), [`create_varlen_metadata_for_document`](../common/attention.md#create_varlen_metadata_for_document), [`decoder_input_sharding`](../common/decoder_sharding.md#decoder_input_sharding), [`norm`](../common/decoder.md#Decoder.norm), [`layers`](../common/decoder.md#Decoder.layers), [`annotate_input_spmd_types`](../../distributed/spmd_types.md#annotate_input_spmd_types), [`config`](../common/decoder.md#Decoder.config), [`first_full_attention_backend`](../common/decoder.md#Decoder.Config.first_full_attention_backend), [`inner_attention`](../common/attention.md#BaseAttention.Config.inner_attention), [`first_attention`](../common/decoder.md#Decoder.Config.first_attention), [`DP`](../../distributed/parallel_dims.md#MeshAxisName.DP), [`spmd_local_context`](../../distributed/spmd_types.md#spmd_local_context), [`Config`](model.md#KimiK3Model.Config), [`__init__`](../common/decoder.md#Decoder.__init__), [`vision_encoder`](model.md#KimiK3Model.Config.vision_encoder), [`_apply_attention_residual`](model.md#_apply_attention_residual), [`_skip_lm_head`](../common/decoder.md#Decoder._skip_lm_head), [`get_vision_positions`](../common/multimodal.md#get_vision_positions), [`output_res_norm`](model.md#KimiK3Model.Config.output_res_norm), [`output_res_proj`](model.md#KimiK3Model.Config.output_res_proj), [`scatter_vision_embeds`](../common/multimodal.md#scatter_vision_embeds), [`KimiK3AttentionMaskDict`](model.md#KimiK3AttentionMaskDict)
- used by: [`_kimi_k3_config`](__init__.md#_kimi_k3_config), [`Decoder`](../common/decoder.md#Decoder), [`parallelize_kimi_k3`](parallelize.md#parallelize_kimi_k3), [`get_attention_masks`](../common/decoder.md#Decoder.get_attention_masks), [`preprocess_inputs`](../common/decoder.md#Decoder.preprocess_inputs), [`get_nparams_and_flops`](model.md#KimiK3Model.Config.get_nparams_and_flops), [`forward`](../common/decoder.md#Decoder.forward), [`set_kimi_k3_sharding_config`](sharding.md#set_kimi_k3_sharding_config), [`_debugmodel`](__init__.md#_debugmodel), [`_kimi_k3`](__init__.md#_kimi_k3), [`__init__`](state_dict_adapter.md#KimiK3StateDictAdapter.__init__)

### <a id="KimiK3Model.Config"></a>`KimiK3Model.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k3/model.py:291`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L291)
- signature: `class Config(Decoder.Config):`
- members:
  - <a id="KimiK3Model.Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L303`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L303) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3Model.Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L297`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L297)
  - <a id="KimiK3Model.Config.layers"></a>`layers` — [`L292`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L292) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3Model.Config.output_res_norm"></a>`output_res_norm` — [`L293`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L293)
  - <a id="KimiK3Model.Config.output_res_proj"></a>`output_res_proj` — [`L294`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L294)
  - <a id="KimiK3Model.Config.vision_encoder"></a>`vision_encoder` — [`L295`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L295) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- uses (calls/refs, reference-scoped): [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`Decoder`](../common/decoder.md#Decoder), [`update_from_config`](../common/decoder.md#Decoder.Config.update_from_config), [`Config`](../common/decoder.md#Decoder.Config), [`set_kimi_k3_sharding_config`](sharding.md#set_kimi_k3_sharding_config), [`get_nparams_and_active_nparams`](../utils.md#get_nparams_and_active_nparams), [`quadratic_attention_flops_per_token`](../utils.md#quadratic_attention_flops_per_token), [`Config`](vision_encoder.md#KimiK3VisionEncoder.Config), [`delta_attention`](model.md#KimiK3TransformerBlock.Config.delta_attention), [`vision_encoder`](model.md#KimiK3Model.vision_encoder), [`attention`](model.md#KimiK3TransformerBlock.Config.attention), [`KimiK3VisionEncoder`](vision_encoder.md#KimiK3VisionEncoder), [`Config`](kda.md#KDA.Config), [`Config`](model.md#KimiMLAAttention.Config), [`KDA`](kda.md#KDA), [`Config`](model.md#KimiK3TransformerBlock.Config), [`head_dim`](kda.md#KDA.Config.head_dim), [`num_heads`](kda.md#KDA.Config.num_heads), [`KimiMLAAttention`](model.md#KimiMLAAttention), [`n_heads`](../common/attention.md#BaseAttention.Config.n_heads), [`KimiK3TransformerBlock`](model.md#KimiK3TransformerBlock), [`delta_rule_flops_per_token`](../utils.md#delta_rule_flops_per_token), [`qk_nope_head_dim`](model.md#KimiMLAAttention.Config.qk_nope_head_dim), [`qk_rope_head_dim`](model.md#KimiMLAAttention.Config.qk_rope_head_dim), [`v_head_dim`](model.md#KimiMLAAttention.Config.v_head_dim)
- used by: [`_kimi_k3_config`](__init__.md#_kimi_k3_config), [`to_hf`](state_dict_adapter.md#KimiK3StateDictAdapter.to_hf), [`from_hf`](state_dict_adapter.md#KimiK3StateDictAdapter.from_hf), [`set_kimi_k3_sharding_config`](sharding.md#set_kimi_k3_sharding_config), [`_map_from_hf_layer_key`](state_dict_adapter.md#KimiK3StateDictAdapter._map_from_hf_layer_key), [`vision_encoder`](model.md#KimiK3Model.vision_encoder), [`_debugmodel`](__init__.md#_debugmodel), [`_kimi_k3`](__init__.md#_kimi_k3), [`__init__`](state_dict_adapter.md#KimiK3StateDictAdapter.__init__), [`output_res_norm`](model.md#KimiK3Model.output_res_norm), [`output_res_proj`](model.md#KimiK3Model.output_res_proj), [`__init__`](model.md#KimiK3Model.__init__)

### <a id="KimiK3TransformerBlock"></a>`KimiK3TransformerBlock`  ·  implements/extends Module
- def: [`torchtitan/models/kimi_k3/model.py:175`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L175)
- doc: Hybrid KDA/MLA decoder block with Kimi attention residuals.
- signature: `class KimiK3TransformerBlock(Module):`
- members:
  - <a id="KimiK3TransformerBlock.forward"></a>`forward(self, x_TD: torch.Tensor, block_residual_TND: torch.Tensor, attention_masks: KimiK3AttentionMaskDict | None = None, positions: torch.Tensor | None = None)` — [`L234`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L234) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3TransformerBlock.attention"></a>`attention` — [`L203`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L203)
  - <a id="KimiK3TransformerBlock.attention_norm"></a>`attention_norm` — [`L219`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L219)
  - <a id="KimiK3TransformerBlock.attention_res_norm"></a>`attention_res_norm` — [`L221`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L221)
  - <a id="KimiK3TransformerBlock.attention_res_proj"></a>`attention_res_proj` — [`L226`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L226)
  - <a id="KimiK3TransformerBlock.attn_mask_key"></a>`attn_mask_key` — [`L216`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L216)
  - <a id="KimiK3TransformerBlock.attn_res_block_size"></a>`attn_res_block_size` — [`L202`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L202)
  - <a id="KimiK3TransformerBlock.delta_attention"></a>`delta_attention` — [`L206`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L206)
  - <a id="KimiK3TransformerBlock.feed_forward"></a>`feed_forward` — [`L211`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L211)
  - <a id="KimiK3TransformerBlock.ffn_norm"></a>`ffn_norm` — [`L220`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L220)
  - <a id="KimiK3TransformerBlock.ffn_res_norm"></a>`ffn_res_norm` — [`L231`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L231)
  - <a id="KimiK3TransformerBlock.ffn_res_proj"></a>`ffn_res_proj` — [`L232`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L232)
  - <a id="KimiK3TransformerBlock.layer_id"></a>`layer_id` — [`L201`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L201)
  - <a id="KimiK3TransformerBlock.moe"></a>`moe` — [`L214`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L214)
  - <a id="KimiK3TransformerBlock.moe_enabled"></a>`moe_enabled` — [`L215`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L215)
- protocol/private: <a id="KimiK3TransformerBlock.__init__"></a>`__init__`[`L193`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L193)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`delta_attention`](model.md#KimiK3TransformerBlock.Config.delta_attention), [`moe`](model.md#KimiK3TransformerBlock.Config.moe), [`attention`](model.md#KimiK3TransformerBlock.Config.attention), [`attention_res_norm`](model.md#KimiK3TransformerBlock.Config.attention_res_norm), [`feed_forward`](model.md#KimiK3TransformerBlock.Config.feed_forward), [`Config`](model.md#KimiK3TransformerBlock.Config), [`_apply_attention_residual`](model.md#_apply_attention_residual), [`attention_res_proj`](model.md#KimiK3TransformerBlock.Config.attention_res_proj), [`attention_norm`](model.md#KimiK3TransformerBlock.Config.attention_norm), [`ffn_norm`](model.md#KimiK3TransformerBlock.Config.ffn_norm), [`ffn_res_norm`](model.md#KimiK3TransformerBlock.Config.ffn_res_norm), [`ffn_res_proj`](model.md#KimiK3TransformerBlock.Config.ffn_res_proj), [`KimiK3AttentionMaskDict`](model.md#KimiK3AttentionMaskDict), [`attn_res_block_size`](model.md#KimiK3TransformerBlock.Config.attn_res_block_size), [`layer_id`](model.md#KimiK3TransformerBlock.Config.layer_id)
- used by: [`Module`](../../protocols/module.md#Module), [`_kimi_k3_config`](__init__.md#_kimi_k3_config), [`layers`](model.md#KimiK3Model.Config.layers)

### <a id="KimiK3TransformerBlock.Config"></a>`KimiK3TransformerBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k3/model.py:179`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L179)
- signature: `class Config(Module.Config):`
- members:
  - <a id="KimiK3TransformerBlock.Config.attention"></a>`attention` — [`L182`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L182) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3TransformerBlock.Config.attention_norm"></a>`attention_norm` — [`L186`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L186)
  - <a id="KimiK3TransformerBlock.Config.attention_res_norm"></a>`attention_res_norm` — [`L188`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L188) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3TransformerBlock.Config.attention_res_proj"></a>`attention_res_proj` — [`L189`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L189)
  - <a id="KimiK3TransformerBlock.Config.attn_res_block_size"></a>`attn_res_block_size` — [`L181`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L181)
  - <a id="KimiK3TransformerBlock.Config.delta_attention"></a>`delta_attention` — [`L183`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L183) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiK3TransformerBlock.Config.feed_forward"></a>`feed_forward` — [`L184`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L184)
  - <a id="KimiK3TransformerBlock.Config.ffn_norm"></a>`ffn_norm` — [`L187`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L187)
  - <a id="KimiK3TransformerBlock.Config.ffn_res_norm"></a>`ffn_res_norm` — [`L190`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L190)
  - <a id="KimiK3TransformerBlock.Config.ffn_res_proj"></a>`ffn_res_proj` — [`L191`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L191)
  - <a id="KimiK3TransformerBlock.Config.layer_id"></a>`layer_id` — [`L180`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L180)
  - <a id="KimiK3TransformerBlock.Config.moe"></a>`moe` — [`L185`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L185) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../../protocols/module.md#Module.Config), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`Config`](kda.md#KDA.Config), [`Config`](model.md#KimiMLAAttention.Config), [`Config`](moe.md#KimiFeedForward.Config), [`Config`](moe.md#KimiLatentMoE.Config), [`KDA`](kda.md#KDA), [`KimiFeedForward`](moe.md#KimiFeedForward), [`KimiLatentMoE`](moe.md#KimiLatentMoE), [`KimiMLAAttention`](model.md#KimiMLAAttention)
- used by: [`_kimi_k3_config`](__init__.md#_kimi_k3_config), [`get_nparams_and_flops`](model.md#KimiK3Model.Config.get_nparams_and_flops), [`to_hf`](state_dict_adapter.md#KimiK3StateDictAdapter.to_hf), [`from_hf`](state_dict_adapter.md#KimiK3StateDictAdapter.from_hf), [`set_kimi_k3_sharding_config`](sharding.md#set_kimi_k3_sharding_config), [`_map_from_hf_layer_key`](state_dict_adapter.md#KimiK3StateDictAdapter._map_from_hf_layer_key), [`layers`](model.md#KimiK3Model.Config.layers), [`__init__`](model.md#KimiK3TransformerBlock.__init__), [`attention`](model.md#KimiK3TransformerBlock.attention), [`moe`](model.md#KimiK3TransformerBlock.moe), [`attention_res_norm`](model.md#KimiK3TransformerBlock.attention_res_norm), [`attention_res_proj`](model.md#KimiK3TransformerBlock.attention_res_proj), [`delta_attention`](model.md#KimiK3TransformerBlock.delta_attention), [`feed_forward`](model.md#KimiK3TransformerBlock.feed_forward), [`attention_norm`](model.md#KimiK3TransformerBlock.attention_norm), [`ffn_norm`](model.md#KimiK3TransformerBlock.ffn_norm), [`ffn_res_norm`](model.md#KimiK3TransformerBlock.ffn_res_norm), [`ffn_res_proj`](model.md#KimiK3TransformerBlock.ffn_res_proj), [`attn_res_block_size`](model.md#KimiK3TransformerBlock.attn_res_block_size), [`layer_id`](model.md#KimiK3TransformerBlock.layer_id)

### <a id="KimiMLAAttention"></a>`KimiMLAAttention`  ·  implements/extends BaseAttention
- def: [`torchtitan/models/kimi_k3/model.py:58`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L58)
- doc: Kimi K3 multi-head latent attention.
- signature: `class KimiMLAAttention(BaseAttention):`
- members:
  - <a id="KimiMLAAttention.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks: AttentionMasksType | None = None, positions: torch.Tensor | None = None)` — [`L106`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L106) — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)
  - <a id="KimiMLAAttention.gate"></a>`gate` — [`L102`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L102)
  - <a id="KimiMLAAttention.inner_attention"></a>`inner_attention` — [`L104`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L104)
  - <a id="KimiMLAAttention.kv_lora_rank"></a>`kv_lora_rank` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L93)
  - <a id="KimiMLAAttention.kv_norm"></a>`kv_norm` — [`L100`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L100)
  - <a id="KimiMLAAttention.n_heads"></a>`n_heads` — [`L88`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L88)
  - <a id="KimiMLAAttention.q_head_dim"></a>`q_head_dim` — [`L91`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L91)
  - <a id="KimiMLAAttention.q_norm"></a>`q_norm` — [`L97`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L97)
  - <a id="KimiMLAAttention.qk_nope_head_dim"></a>`qk_nope_head_dim` — [`L89`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L89)
  - <a id="KimiMLAAttention.qk_rope_head_dim"></a>`qk_rope_head_dim` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L90)
  - <a id="KimiMLAAttention.scale"></a>`scale` — [`L94`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L94)
  - <a id="KimiMLAAttention.v_head_dim"></a>`v_head_dim` — [`L92`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L92)
  - <a id="KimiMLAAttention.wkv_a"></a>`wkv_a` — [`L99`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L99)
  - <a id="KimiMLAAttention.wkv_b"></a>`wkv_b` — [`L101`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L101)
  - <a id="KimiMLAAttention.wo"></a>`wo` — [`L103`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L103)
  - <a id="KimiMLAAttention.wq_a"></a>`wq_a` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L96)
  - <a id="KimiMLAAttention.wq_b"></a>`wq_b` — [`L98`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L98)
- protocol/private: <a id="KimiMLAAttention.__init__"></a>`__init__`[`L86`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L86)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`BaseAttention`](../common/attention.md#BaseAttention), [`inner_attention`](model.md#KimiMLAAttention.Config.inner_attention), [`Config`](model.md#KimiMLAAttention.Config), [`gate`](model.md#KimiMLAAttention.Config.gate), [`kv_norm`](model.md#KimiMLAAttention.Config.kv_norm), [`q_norm`](model.md#KimiMLAAttention.Config.q_norm), [`wkv_a`](model.md#KimiMLAAttention.Config.wkv_a), [`wkv_b`](model.md#KimiMLAAttention.Config.wkv_b), [`wo`](model.md#KimiMLAAttention.Config.wo), [`wq_a`](model.md#KimiMLAAttention.Config.wq_a), [`wq_b`](model.md#KimiMLAAttention.Config.wq_b), [`n_heads`](../common/attention.md#BaseAttention.Config.n_heads), [`qk_nope_head_dim`](model.md#KimiMLAAttention.Config.qk_nope_head_dim), [`qk_rope_head_dim`](model.md#KimiMLAAttention.Config.qk_rope_head_dim), [`v_head_dim`](model.md#KimiMLAAttention.Config.v_head_dim), [`kv_lora_rank`](model.md#KimiMLAAttention.Config.kv_lora_rank)
- used by: [`BaseAttention`](../common/attention.md#BaseAttention), [`_mla_config`](__init__.md#_mla_config), [`get_nparams_and_flops`](model.md#KimiK3Model.Config.get_nparams_and_flops), [`attention`](model.md#KimiK3TransformerBlock.Config.attention)

### <a id="KimiMLAAttention.Config"></a>`KimiMLAAttention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/kimi_k3/model.py:68`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L68)
- signature: `class Config(BaseAttention.Config):`
- members:
  - <a id="KimiMLAAttention.Config.dim"></a>`dim` — [`L69`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L69)
  - <a id="KimiMLAAttention.Config.gate"></a>`gate` — [`L80`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L80)
  - <a id="KimiMLAAttention.Config.inner_attention"></a>`inner_attention` — [`L82`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L82)
  - <a id="KimiMLAAttention.Config.kv_lora_rank"></a>`kv_lora_rank` — [`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L70)
  - <a id="KimiMLAAttention.Config.kv_norm"></a>`kv_norm` — [`L78`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L78)
  - <a id="KimiMLAAttention.Config.q_norm"></a>`q_norm` — [`L75`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L75)
  - <a id="KimiMLAAttention.Config.qk_nope_head_dim"></a>`qk_nope_head_dim` — [`L71`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L71)
  - <a id="KimiMLAAttention.Config.qk_rope_head_dim"></a>`qk_rope_head_dim` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L72)
  - <a id="KimiMLAAttention.Config.v_head_dim"></a>`v_head_dim` — [`L73`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L73)
  - <a id="KimiMLAAttention.Config.wkv_a"></a>`wkv_a` — [`L77`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L77)
  - <a id="KimiMLAAttention.Config.wkv_b"></a>`wkv_b` — [`L79`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L79)
  - <a id="KimiMLAAttention.Config.wo"></a>`wo` — [`L81`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L81)
  - <a id="KimiMLAAttention.Config.wq_a"></a>`wq_a` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L74)
  - <a id="KimiMLAAttention.Config.wq_b"></a>`wq_b` — [`L76`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L76)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`Config`](../../protocols/module.md#Module.Config), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`BaseAttention`](../common/attention.md#BaseAttention), [`Config`](../common/attention.md#FlexInnerAttention.Config), [`Config`](../common/attention.md#BaseAttention.Config)
- used by: [`_mla_config`](__init__.md#_mla_config), [`get_nparams_and_flops`](model.md#KimiK3Model.Config.get_nparams_and_flops), [`attention`](model.md#KimiK3TransformerBlock.Config.attention), [`q_head_dim`](model.md#KimiMLAAttention.q_head_dim), [`gate`](model.md#KimiMLAAttention.gate), [`inner_attention`](model.md#KimiMLAAttention.inner_attention), [`kv_norm`](model.md#KimiMLAAttention.kv_norm), [`q_norm`](model.md#KimiMLAAttention.q_norm), [`wkv_a`](model.md#KimiMLAAttention.wkv_a), [`wkv_b`](model.md#KimiMLAAttention.wkv_b), [`wo`](model.md#KimiMLAAttention.wo), [`wq_a`](model.md#KimiMLAAttention.wq_a), [`wq_b`](model.md#KimiMLAAttention.wq_b), [`v_head_dim`](model.md#KimiMLAAttention.v_head_dim), [`qk_nope_head_dim`](model.md#KimiMLAAttention.qk_nope_head_dim), [`qk_rope_head_dim`](model.md#KimiMLAAttention.qk_rope_head_dim), [`kv_lora_rank`](model.md#KimiMLAAttention.kv_lora_rank), [`__init__`](model.md#KimiMLAAttention.__init__)

## Functions
- <a id="_apply_attention_residual"></a>`_apply_attention_residual(prefix_sum_TD: torch.Tensor, block_residual_TND: torch.Tensor, projection: Linear, norm: RMSNorm)` — [`L152`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L152) — Apply Kimi's block-level attention residual in FP32. — documented in [kimi-k3-model](../../../../concepts/kimi-k3-model.md)

## Module values
- <a id="KimiK3AttentionMaskDict"></a>`KimiK3AttentionMaskDict` — [`L50`](../../../../../../../raw/code/torchtitan/torchtitan/models/kimi_k3/model.py#L50)

