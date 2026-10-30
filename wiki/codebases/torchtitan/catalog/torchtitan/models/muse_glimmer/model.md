---
title: 'Module: torchtitan/models/muse_glimmer/model.py'
type: catalog
provenance: extracted
module: torchtitan/models/muse_glimmer/model.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.models.muse_glimmer.model`/
symbols:
  MuseGlimmerModel.preprocess_inputs: MuseGlimmerModel#preprocess_inputs().
  MuseGlimmerModel.get_attention_masks: MuseGlimmerModel#get_attention_masks().
  MuseGlimmerModel: MuseGlimmerModel#
  Attention.forward: Attention#forward().
  MuseGlimmerModel.Config: MuseGlimmerModel#Config#
  MuseGlimmerModel.forward: MuseGlimmerModel#forward().
  MuseGlimmerTransformerBlock.forward: MuseGlimmerTransformerBlock#forward().
  MuseGlimmerModel.Config.get_nparams_and_flops: MuseGlimmerModel#Config#get_nparams_and_flops().
  SoftCappedLinear: SoftCappedLinear#
  Attention.o_gate: Attention#o_gate.
  Attention: Attention#
  SoftCappedLinear.Config: SoftCappedLinear#Config#
  MuseGlimmerModel.vision_encoder: MuseGlimmerModel#vision_encoder.
  Attention.Config: Attention#Config#
  MuseGlimmerModel.Config.vision_encoder: MuseGlimmerModel#Config#vision_encoder.
  MuseGlimmerModel.vision_adapter: MuseGlimmerModel#vision_adapter.
  MuseGlimmerModel._prepare_multimodal_embeds: MuseGlimmerModel#_prepare_multimodal_embeds().
  Attention.Config.o_gate: Attention#Config#o_gate.
  MuseGlimmerModel.Config.vision_projection: MuseGlimmerModel#Config#vision_projection.
  MuseGlimmerModel.Config.perception_emb_norm: MuseGlimmerModel#Config#perception_emb_norm.
  MuseGlimmerModel.Config.update_from_config: MuseGlimmerModel#Config#update_from_config().
  MuseGlimmerTransformerBlock.Config: MuseGlimmerTransformerBlock#Config#
  MuseGlimmerTransformerBlock.attention: MuseGlimmerTransformerBlock#attention.
  MuseGlimmerModel.__init__: MuseGlimmerModel#__init__().
  RMSGainCenterNorm.Config: RMSGainCenterNorm#Config#
  MuseGlimmerTransformerBlock.Config.post_attention_norm: MuseGlimmerTransformerBlock#Config#post_attention_norm.
  MuseGlimmerTransformerBlock.Config.post_ffn_norm: MuseGlimmerTransformerBlock#Config#post_ffn_norm.
  EmbeddingWithNorm.Config: EmbeddingWithNorm#Config#
  EmbeddingWithNorm.Config.embedding: EmbeddingWithNorm#Config#embedding.
  EmbeddingWithNorm.Config.norm: EmbeddingWithNorm#Config#norm.
  MuseGlimmerModel.Config.dim: MuseGlimmerModel#Config#dim.
  MuseGlimmerModel.Config.tok_embeddings: MuseGlimmerModel#Config#tok_embeddings.
  MuseGlimmerModel.Config.vision_adapter: MuseGlimmerModel#Config#vision_adapter.
  MuseGlimmerModel.vision_projection: MuseGlimmerModel#vision_projection.
  MuseGlimmerModel.perception_emb_norm: MuseGlimmerModel#perception_emb_norm.
  MuseGlimmerTransformerBlock: MuseGlimmerTransformerBlock#
  MuseGlimmerTransformerBlock.feed_forward: MuseGlimmerTransformerBlock#feed_forward.
  MuseGlimmerTransformerBlock.attention_norm: MuseGlimmerTransformerBlock#attention_norm.
  MuseGlimmerTransformerBlock.ffn_norm: MuseGlimmerTransformerBlock#ffn_norm.
  MuseGlimmerTransformerBlock.post_attention_norm: MuseGlimmerTransformerBlock#post_attention_norm.
  MuseGlimmerTransformerBlock.post_ffn_norm: MuseGlimmerTransformerBlock#post_ffn_norm.
  EmbeddingWithNorm.embedding: EmbeddingWithNorm#embedding.
  EmbeddingWithNorm.norm: EmbeddingWithNorm#norm.
  MuseGlimmerModel._get_vision_features: MuseGlimmerModel#_get_vision_features().
  RMSGainCenterNorm: RMSGainCenterNorm#
  SoftCappedLinear.output_soft_cap_temp: SoftCappedLinear#output_soft_cap_temp.
  EmbeddingWithNorm: EmbeddingWithNorm#
  RMSGainCenterNorm.__init__: RMSGainCenterNorm#__init__().
  Attention.__init__: Attention#__init__().
  SoftCappedLinear.__init__: SoftCappedLinear#__init__().
  SoftCappedLinear.forward: SoftCappedLinear#forward().
  EmbeddingWithNorm.forward: EmbeddingWithNorm#forward().
  Attention.scale_query_by: Attention#scale_query_by.
  SoftCappedLinear.output_multiplier: SoftCappedLinear#output_multiplier.
  MuseGlimmerModel._build_mask: MuseGlimmerModel#_build_mask().
  Attention.Config.window_size: Attention#Config#window_size.
  SoftCappedLinear.Config.output_soft_cap_temp: SoftCappedLinear#Config#output_soft_cap_temp.
  RMSGainCenterNorm.gain_center: RMSGainCenterNorm#gain_center.
  Attention.window_size: Attention#window_size.
  _window_mask_key: _window_mask_key().
  SoftCappedLinear.Config.output_multiplier: SoftCappedLinear#Config#output_multiplier.
  MuseGlimmerModel.Config.vocab_size: MuseGlimmerModel#Config#vocab_size.
  RMSGainCenterNorm.forward: RMSGainCenterNorm#forward().
  Attention.Config.sliding_window_size: Attention#Config#sliding_window_size().
  MuseGlimmerTransformerBlock.__init__: MuseGlimmerTransformerBlock#__init__().
  EmbeddingWithNorm.__init__: EmbeddingWithNorm#__init__().
  RMSGainCenterNorm.Config.gain_center: RMSGainCenterNorm#Config#gain_center.
  Attention.Config.scale_query_by: Attention#Config#scale_query_by.
---
# Module: [`torchtitan/models/muse_glimmer/model.py`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py)

## Classes
### <a id="Attention"></a>`Attention`  ·  implements/extends GQAttention
- def: [`torchtitan/models/muse_glimmer/model.py:79`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L79) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- doc: Muse Glimmer GQA attention.
- signature: `class Attention(GQAttention):`
- members:
  - <a id="Attention.forward"></a>`forward(self, x_TD: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None)` — [`L111`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L111) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
  - <a id="Attention.o_gate"></a>`o_gate` — [`L107`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L107) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
  - <a id="Attention.scale_query_by"></a>`scale_query_by` — [`L105`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L105)
  - <a id="Attention.window_size"></a>`window_size` — [`L106`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L106)
- protocol/private: <a id="Attention.__init__"></a>`__init__`[`L103`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L103)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`Linear`](../common/linear.md#Linear), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`GQAttention`](../common/attention.md#GQAttention), [`k_norm`](../common/attention.md#GQAttention.k_norm), [`forward`](../../experiments/tpu/muse_glimmer/attention.md#TpuMuseGlimmerAttention.forward), [`rope`](../common/attention.md#GQAttention.rope), [`q_norm`](../common/attention.md#GQAttention.q_norm), [`Config`](model.md#Attention.Config), [`inner_attention`](../common/attention.md#GQAttention.inner_attention), [`qkv_linear`](../common/attention.md#GQAttention.qkv_linear), [`enable_gqa`](../common/attention.md#GQAttention.enable_gqa), [`o_gate`](model.md#Attention.Config.o_gate), [`wo`](../common/attention.md#GQAttention.wo), [`scaling`](../common/attention.md#GQAttention.scaling), [`TpuMuseGlimmerAttention`](../../experiments/tpu/muse_glimmer/attention.md#TpuMuseGlimmerAttention), [`__init__`](../common/attention.md#GQAttention.__init__), [`window_size`](model.md#Attention.Config.window_size), [`_window_mask_key`](model.md#_window_mask_key), [`scale_query_by`](model.md#Attention.Config.scale_query_by)
- used by: [`_build_muse_glimmer_attention`](__init__.md#_build_muse_glimmer_attention), [`_set_muse_glimmer_layer_sharding`](sharding.md#_set_muse_glimmer_layer_sharding), [`GQAttention`](../common/attention.md#GQAttention), [`forward`](../common/attention.md#GQAttention.forward), [`forward`](../../experiments/tpu/muse_glimmer/attention.md#TpuMuseGlimmerAttention.forward), [`Config`](../../experiments/tpu/muse_glimmer/attention.md#TpuMuseGlimmerAttention.Config), [`TpuMuseGlimmerAttention`](../../experiments/tpu/muse_glimmer/attention.md#TpuMuseGlimmerAttention)  (1 test-only)

### <a id="Attention.Config"></a>`Attention.Config`  ·  implements/extends Config
- def: [`torchtitan/models/muse_glimmer/model.py:89`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L89)
- signature: `class Config(GQAttention.Config):`
- members:
  - <a id="Attention.Config.sliding_window_size"></a>`sliding_window_size(self)` — [`L96`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L96)
  - <a id="Attention.Config.o_gate"></a>`o_gate` — [`L91`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L91)
  - <a id="Attention.Config.scale_query_by"></a>`scale_query_by` — [`L90`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L90)
  - <a id="Attention.Config.window_size"></a>`window_size` — [`L93`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L93)
- uses (calls/refs, reference-scoped): [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`GQAttention`](../common/attention.md#GQAttention), [`Config`](../common/attention.md#GQAttention.Config)
- used by: [`_build_muse_glimmer_attention`](__init__.md#_build_muse_glimmer_attention), [`_set_muse_glimmer_layer_sharding`](sharding.md#_set_muse_glimmer_layer_sharding), [`use_tpu_attention`](../../experiments/tpu/muse_glimmer/__init__.md#use_tpu_attention), [`o_gate`](model.md#Attention.o_gate), [`Config`](../../experiments/tpu/muse_glimmer/attention.md#TpuMuseGlimmerAttention.Config), [`__init__`](model.md#Attention.__init__), [`scale_query_by`](model.md#Attention.scale_query_by), [`window_size`](model.md#Attention.window_size)  (1 test-only)

### <a id="EmbeddingWithNorm"></a>`EmbeddingWithNorm`  ·  implements/extends Module
- def: [`torchtitan/models/muse_glimmer/model.py:223`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L223)
- doc: Token embedding bundled with a scaleless RMSNorm on the looked-up
- signature: `class EmbeddingWithNorm(Module):`
- members:
  - <a id="EmbeddingWithNorm.forward"></a>`forward(self, tokens: torch.Tensor)` — [`L258`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L258)
  - <a id="EmbeddingWithNorm.embedding"></a>`embedding` — [`L255`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L255)
  - <a id="EmbeddingWithNorm.norm"></a>`norm` — [`L256`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L256)
- protocol/private: <a id="EmbeddingWithNorm.__init__"></a>`__init__`[`L253`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L253)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`build`](../../protocols/module.md#Module.Config.build), [`Config`](model.md#EmbeddingWithNorm.Config), [`embedding`](model.md#EmbeddingWithNorm.Config.embedding), [`norm`](model.md#EmbeddingWithNorm.Config.norm)
- used by: [`Module`](../../protocols/module.md#Module), [`_muse_glimmer_config`](__init__.md#_muse_glimmer_config), [`tok_embeddings`](model.md#MuseGlimmerModel.Config.tok_embeddings)

### <a id="EmbeddingWithNorm.Config"></a>`EmbeddingWithNorm.Config`  ·  implements/extends Config
- def: [`torchtitan/models/muse_glimmer/model.py:249`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L249)
- signature: `class Config(Module.Config):`
- members:
  - <a id="EmbeddingWithNorm.Config.embedding"></a>`embedding` — [`L250`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L250)
  - <a id="EmbeddingWithNorm.Config.norm"></a>`norm` — [`L251`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L251)
- uses (calls/refs, reference-scoped): [`Module`](../../protocols/module.md#Module), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../../protocols/module.md#Module.Config), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`Embedding`](../common/embedding.md#Embedding), [`Config`](../common/embedding.md#Embedding.Config)
- used by: [`_muse_glimmer_config`](__init__.md#_muse_glimmer_config), [`_set_tok_embeddings_sharding`](sharding.md#_set_tok_embeddings_sharding), [`tok_embeddings`](model.md#MuseGlimmerModel.Config.tok_embeddings), [`embedding`](model.md#EmbeddingWithNorm.embedding), [`norm`](model.md#EmbeddingWithNorm.norm), [`__init__`](model.md#EmbeddingWithNorm.__init__)

### <a id="MuseGlimmerModel"></a>`MuseGlimmerModel`  ·  implements/extends Decoder
- def: [`torchtitan/models/muse_glimmer/model.py:262`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L262) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- doc: Muse Glimmer decoder-only language model.
- signature: `class MuseGlimmerModel(Decoder):`
- members:
  - <a id="MuseGlimmerModel._get_vision_features"></a>`_get_vision_features(self, pixel_values: torch.Tensor, grid_thw: torch.Tensor)` — [`L450`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L450) — Encode packed ``pixel_values`` and adapter-project into features.
  - <a id="MuseGlimmerModel._prepare_multimodal_embeds"></a>`_prepare_multimodal_embeds(self, h_TD: torch.Tensor, *, pixel_values: torch.Tensor | None, grid_thw: torch.Tensor | None, vision_bank_indices_T: torch.Tensor | None)` — [`L466`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L466) — Build and inject image embeddings on the embedding pipeline stage. — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
  - <a id="MuseGlimmerModel.forward"></a>`forward(self, tokens: torch.Tensor, positions: torch.Tensor | None = None, attention_masks: AttentionMasksType | None = None, *, pixel_values: torch.Tensor | None = None, grid_thw: torch.Tensor | None = None, pixel_values_videos: torch.Tensor | None = None, grid_thw_videos: torch.Tensor | None = None, vision_bank_indices_T: torch.Tensor | None = None)` — [`L492`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L492) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
  - <a id="MuseGlimmerModel.get_attention_masks"></a>`get_attention_masks(self, positions: torch.Tensor, *, padding_mask: torch.Tensor | None = None, max_num_documents: int | None = None, max_context_length: int | None = None)` — [`L534`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L534) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
  - <a id="MuseGlimmerModel.preprocess_inputs"></a>`preprocess_inputs(self, input_dict: dict[str, torch.Tensor], *, parallel_dims: ParallelDims, parallelism: ParallelismConfig, max_num_documents: int | None = None, max_context_length: int | None = None)` — [`L360`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L360) — Build first-stage vision-bank indices and masks, then shard the batch. — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
  - <a id="MuseGlimmerModel.perception_emb_norm"></a>`perception_emb_norm` — [`L346`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L346)
  - <a id="MuseGlimmerModel.vision_adapter"></a>`vision_adapter` — [`L356`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L356)
  - <a id="MuseGlimmerModel.vision_encoder"></a>`vision_encoder` — [`L353`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L353)
  - <a id="MuseGlimmerModel.vision_projection"></a>`vision_projection` — [`L341`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L341)
- protocol/private: <a id="MuseGlimmerModel.__init__"></a>`__init__`[`L338`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L338), <a id="MuseGlimmerModel._build_mask"></a>`_build_mask`[`L575`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L575)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`ParallelismConfig`](../../config/configs.md#ParallelismConfig), [`ParallelDims`](../../distributed/parallel_dims.md#ParallelDims), [`layers`](../common/decoder.md#Decoder.Config.layers), [`FlexInnerAttention`](../common/attention.md#FlexInnerAttention), [`Decoder`](../common/decoder.md#Decoder), [`spmd_backend`](../../config/configs.md#ParallelismConfig.spmd_backend), [`VarlenInnerAttention`](../common/attention.md#VarlenInnerAttention), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`Config`](../common/attention.md#FlexInnerAttention.Config), [`get_causal_mask_mod`](../common/attention.md#get_causal_mask_mod), [`tok_embeddings`](../common/decoder.md#Decoder.tok_embeddings), [`cp_enabled`](../../distributed/parallel_dims.md#ParallelDims.cp_enabled), [`tp_enabled`](../../distributed/parallel_dims.md#ParallelDims.tp_enabled), [`lm_head`](../common/decoder.md#Decoder.lm_head), [`Config`](../common/attention.md#VarlenInnerAttention.Config), [`create_attention_mask`](../common/attention.md#create_attention_mask), [`create_varlen_metadata_for_document`](../common/attention.md#create_varlen_metadata_for_document), [`_cp_shard_inputs`](../common/decoder.md#Decoder._cp_shard_inputs), [`decoder_input_sharding`](../common/decoder_sharding.md#decoder_input_sharding), [`Config`](model.md#MuseGlimmerModel.Config), [`norm`](../common/decoder.md#Decoder.norm), [`layers`](../common/decoder.md#Decoder.layers), [`annotate_input_spmd_types`](../../distributed/spmd_types.md#annotate_input_spmd_types), [`is_in_batch_invariant_mode`](../../distributed/utils.md#is_in_batch_invariant_mode), [`config`](../common/decoder.md#Decoder.config), [`inner_attention`](../common/attention.md#BaseAttention.Config.inner_attention), [`first_attention`](../common/decoder.md#Decoder.Config.first_attention), [`enable_sequence_parallel`](../../config/configs.md#ParallelismConfig.enable_sequence_parallel), [`get_sliding_window_mask_mod`](../common/attention.md#get_sliding_window_mask_mod), [`get_efficient_causal_mask_mod_for_packed_document`](../common/attention.md#get_efficient_causal_mask_mod_for_packed_document), [`spmd_local_context`](../../distributed/spmd_types.md#spmd_local_context), [`vision_encoder`](model.md#MuseGlimmerModel.Config.vision_encoder), [`__init__`](../common/decoder.md#Decoder.__init__), [`get_dense_tp_mesh`](../../distributed/parallel_dims.md#ParallelDims.get_dense_tp_mesh), [`perception_emb_norm`](model.md#MuseGlimmerModel.Config.perception_emb_norm), [`vision_projection`](model.md#MuseGlimmerModel.Config.vision_projection), [`GraphTrainerMuseGlimmerModel`](../../experiments/graph_trainer/muse_glimmer/model.md#GraphTrainerMuseGlimmerModel), [`vision_bank_indices_placement`](sharding.md#vision_bank_indices_placement), [`multimodal_input_sharding`](../common/vision_encoder_sharding.md#multimodal_input_sharding)  (+6 more)
- used by: [`_muse_glimmer_config`](__init__.md#_muse_glimmer_config), [`Decoder`](../common/decoder.md#Decoder), [`_muse_glimmer_mm_dataloader`](config_registry.md#_muse_glimmer_mm_dataloader), [`parallelize_muse_glimmer`](parallelize.md#parallelize_muse_glimmer), [`get_attention_masks`](../common/decoder.md#Decoder.get_attention_masks), [`preprocess_inputs`](../common/decoder.md#Decoder.preprocess_inputs), [`forward`](../common/decoder.md#Decoder.forward), [`_set_multimodal_sharding`](sharding.md#_set_multimodal_sharding), [`use_tpu_attention`](../../experiments/tpu/muse_glimmer/__init__.md#use_tpu_attention), [`set_muse_glimmer_sharding_config`](sharding.md#set_muse_glimmer_sharding_config), [`_set_tok_embeddings_sharding`](sharding.md#_set_tok_embeddings_sharding), [`get_nparams_and_flops`](model.md#MuseGlimmerModel.Config.get_nparams_and_flops), [`_testmodel`](../../experiments/tpu/muse_glimmer/__init__.md#_testmodel), [`_muse_glimmer_debugmodel_mm`](__init__.md#_muse_glimmer_debugmodel_mm), [`_muse_glimmer_30b`](__init__.md#_muse_glimmer_30b), [`_upstream_flavor`](../../experiments/tpu/muse_glimmer/__init__.md#_upstream_flavor), [`GraphTrainerMuseGlimmerModel`](../../experiments/graph_trainer/muse_glimmer/model.md#GraphTrainerMuseGlimmerModel), [`_debugmodel`](__init__.md#_debugmodel), [`Config`](../../experiments/graph_trainer/muse_glimmer/model.md#GraphTrainerMuseGlimmerModel.Config), [`__init__`](state_dict_adapter.md#MuseGlimmerStateDictAdapter.__init__), [`__init__`](../../experiments/graph_trainer/muse_glimmer/model.md#GraphTrainerMuseGlimmerModel.__init__)  (8 test-only)

### <a id="MuseGlimmerModel.Config"></a>`MuseGlimmerModel.Config`  ·  implements/extends Config
- def: [`torchtitan/models/muse_glimmer/model.py:270`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L270) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- signature: `class Config(Decoder.Config):`
- members:
  - <a id="MuseGlimmerModel.Config.get_nparams_and_flops"></a>`get_nparams_and_flops(self, model: nn.Module, seq_len: int)` — [`L307`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L307)
  - <a id="MuseGlimmerModel.Config.update_from_config"></a>`update_from_config(self, *, config, **kwargs)` — [`L291`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L291)
  - <a id="MuseGlimmerModel.Config.dim"></a>`dim` — [`L271`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L271)
  - <a id="MuseGlimmerModel.Config.perception_emb_norm"></a>`perception_emb_norm` — [`L282`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L282)
  - <a id="MuseGlimmerModel.Config.tok_embeddings"></a>`tok_embeddings` — [`L277`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L277)
  - <a id="MuseGlimmerModel.Config.vision_adapter"></a>`vision_adapter` — [`L289`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L289)
  - <a id="MuseGlimmerModel.Config.vision_encoder"></a>`vision_encoder` — [`L288`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L288) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
  - <a id="MuseGlimmerModel.Config.vision_projection"></a>`vision_projection` — [`L281`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L281)
  - <a id="MuseGlimmerModel.Config.vocab_size"></a>`vocab_size` — [`L272`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L272)
- uses (calls/refs, reference-scoped): [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config), [`layers`](../common/decoder.md#Decoder.Config.layers), [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`Decoder`](../common/decoder.md#Decoder), [`update_from_config`](../common/decoder.md#Decoder.Config.update_from_config), [`Config`](../common/decoder.md#Decoder.Config), [`get_nparams_and_active_nparams`](../utils.md#get_nparams_and_active_nparams), [`set_muse_glimmer_sharding_config`](sharding.md#set_muse_glimmer_sharding_config), [`quadratic_attention_flops_per_token`](../utils.md#quadratic_attention_flops_per_token), [`vision_encoder`](model.md#MuseGlimmerModel.vision_encoder), [`Config`](vision_encoder.md#MuseGlimmerVisionAdapter.Config), [`Config`](vision_encoder.md#MuseGlimmerVisionEncoder.Config), [`MuseGlimmerVisionAdapter`](vision_encoder.md#MuseGlimmerVisionAdapter), [`MuseGlimmerVisionEncoder`](vision_encoder.md#MuseGlimmerVisionEncoder), [`vision_adapter`](model.md#MuseGlimmerModel.vision_adapter), [`Config`](model.md#EmbeddingWithNorm.Config), [`perception_emb_norm`](model.md#MuseGlimmerModel.perception_emb_norm), [`vision_projection`](model.md#MuseGlimmerModel.vision_projection), [`EmbeddingWithNorm`](model.md#EmbeddingWithNorm)
- used by: [`_muse_glimmer_config`](__init__.md#_muse_glimmer_config), [`_muse_glimmer_mm_dataloader`](config_registry.md#_muse_glimmer_mm_dataloader), [`preprocess_inputs`](model.md#MuseGlimmerModel.preprocess_inputs), [`_set_multimodal_sharding`](sharding.md#_set_multimodal_sharding), [`use_tpu_attention`](../../experiments/tpu/muse_glimmer/__init__.md#use_tpu_attention), [`set_muse_glimmer_sharding_config`](sharding.md#set_muse_glimmer_sharding_config), [`_set_tok_embeddings_sharding`](sharding.md#_set_tok_embeddings_sharding), [`_testmodel`](../../experiments/tpu/muse_glimmer/__init__.md#_testmodel), [`_muse_glimmer_debugmodel_mm`](__init__.md#_muse_glimmer_debugmodel_mm), [`vision_encoder`](model.md#MuseGlimmerModel.vision_encoder), [`_muse_glimmer_30b`](__init__.md#_muse_glimmer_30b), [`_upstream_flavor`](../../experiments/tpu/muse_glimmer/__init__.md#_upstream_flavor), [`vision_adapter`](model.md#MuseGlimmerModel.vision_adapter), [`_attn_geometry`](state_dict_adapter.md#MuseGlimmerStateDictAdapter._attn_geometry), [`_vision_num_heads`](state_dict_adapter.md#MuseGlimmerStateDictAdapter._vision_num_heads), [`__init__`](model.md#MuseGlimmerModel.__init__), [`_debugmodel`](__init__.md#_debugmodel), [`Config`](../../experiments/graph_trainer/muse_glimmer/model.md#GraphTrainerMuseGlimmerModel.Config), [`perception_emb_norm`](model.md#MuseGlimmerModel.perception_emb_norm), [`vision_projection`](model.md#MuseGlimmerModel.vision_projection), [`__init__`](state_dict_adapter.md#MuseGlimmerStateDictAdapter.__init__)  (11 test-only)

### <a id="MuseGlimmerTransformerBlock"></a>`MuseGlimmerTransformerBlock`  ·  implements/extends TransformerBlock
- def: [`torchtitan/models/muse_glimmer/model.py:155`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L155)
- doc: Muse Glimmer transformer block with post-norm residuals.
- signature: `class MuseGlimmerTransformerBlock(TransformerBlock):`
- members:
  - <a id="MuseGlimmerTransformerBlock.forward"></a>`forward(self, x: torch.Tensor, attention_masks: AttentionMasksType | None, positions: torch.Tensor | None = None)` — [`L177`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L177)
  - <a id="MuseGlimmerTransformerBlock.attention"></a>`attention` — [`L169`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L169)
  - <a id="MuseGlimmerTransformerBlock.attention_norm"></a>`attention_norm` — [`L172`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L172)
  - <a id="MuseGlimmerTransformerBlock.feed_forward"></a>`feed_forward` — [`L171`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L171)
  - <a id="MuseGlimmerTransformerBlock.ffn_norm"></a>`ffn_norm` — [`L173`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L173)
  - <a id="MuseGlimmerTransformerBlock.post_attention_norm"></a>`post_attention_norm` — [`L174`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L174)
  - <a id="MuseGlimmerTransformerBlock.post_ffn_norm"></a>`post_ffn_norm` — [`L175`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L175)
- protocol/private: <a id="MuseGlimmerTransformerBlock.__init__"></a>`__init__`[`L167`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L167)
- uses (calls/refs, reference-scoped): [`build`](../../protocols/module.md#Module.Config.build), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`AttentionMasksType`](../common/attention.md#AttentionMasksType), [`feed_forward`](../common/decoder.md#TransformerBlock.Config.feed_forward), [`attention`](../common/decoder.md#TransformerBlock.Config.attention), [`attention_norm`](../common/decoder.md#TransformerBlock.Config.attention_norm), [`ffn_norm`](../common/decoder.md#TransformerBlock.Config.ffn_norm), [`Config`](model.md#MuseGlimmerTransformerBlock.Config), [`post_attention_norm`](model.md#MuseGlimmerTransformerBlock.Config.post_attention_norm), [`post_ffn_norm`](model.md#MuseGlimmerTransformerBlock.Config.post_ffn_norm)
- used by: [`_set_muse_glimmer_layer_sharding`](sharding.md#_set_muse_glimmer_layer_sharding), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`_build_muse_glimmer_layers`](__init__.md#_build_muse_glimmer_layers)

### <a id="MuseGlimmerTransformerBlock.Config"></a>`MuseGlimmerTransformerBlock.Config`  ·  implements/extends Config
- def: [`torchtitan/models/muse_glimmer/model.py:163`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L163)
- signature: `class Config(TransformerBlock.Config):`
- members:
  - <a id="MuseGlimmerTransformerBlock.Config.post_attention_norm"></a>`post_attention_norm` — [`L164`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L164)
  - <a id="MuseGlimmerTransformerBlock.Config.post_ffn_norm"></a>`post_ffn_norm` — [`L165`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L165)
- uses (calls/refs, reference-scoped): [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../common/nn_modules.md#RMSNorm.Config), [`TransformerBlock`](../common/decoder.md#TransformerBlock), [`Config`](../common/decoder.md#TransformerBlock.Config)
- used by: [`_set_muse_glimmer_layer_sharding`](sharding.md#_set_muse_glimmer_layer_sharding), [`_build_muse_glimmer_layers`](__init__.md#_build_muse_glimmer_layers), [`post_attention_norm`](model.md#MuseGlimmerTransformerBlock.post_attention_norm), [`post_ffn_norm`](model.md#MuseGlimmerTransformerBlock.post_ffn_norm), [`__init__`](model.md#MuseGlimmerTransformerBlock.__init__)

### <a id="RMSGainCenterNorm"></a>`RMSGainCenterNorm`  ·  implements/extends RMSNorm
- def: [`torchtitan/models/muse_glimmer/model.py:58`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L58)
- doc: RMSNorm whose effective scale is `weight + gain_center`.
- signature: `class RMSGainCenterNorm(RMSNorm):`
- members:
  - <a id="RMSGainCenterNorm.forward"></a>`forward(self, x: torch.Tensor)` — [`L74`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L74)
  - <a id="RMSGainCenterNorm.gain_center"></a>`gain_center` — [`L72`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L72)
- protocol/private: <a id="RMSGainCenterNorm.__init__"></a>`__init__`[`L70`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L70)
- uses (calls/refs, reference-scoped): [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`__init__`](../common/nn_modules.md#RMSNorm.__init__), [`Config`](model.md#RMSGainCenterNorm.Config), [`gain_center`](model.md#RMSGainCenterNorm.Config.gain_center)
- used by: [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`_gain_norm`](__init__.md#_gain_norm)

### <a id="RMSGainCenterNorm.Config"></a>`RMSGainCenterNorm.Config`  ·  implements/extends Config
- def: [`torchtitan/models/muse_glimmer/model.py:67`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L67)
- signature: `class Config(RMSNorm.Config):`
- members:
  - <a id="RMSGainCenterNorm.Config.gain_center"></a>`gain_center` — [`L68`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L68)
- uses (calls/refs, reference-scoped): [`RMSNorm`](../common/nn_modules.md#RMSNorm), [`Config`](../common/nn_modules.md#RMSNorm.Config)
- used by: [`_gain_norm`](__init__.md#_gain_norm), [`__init__`](model.md#RMSGainCenterNorm.__init__), [`gain_center`](model.md#RMSGainCenterNorm.gain_center)

### <a id="SoftCappedLinear"></a>`SoftCappedLinear`  ·  implements/extends Linear
- def: [`torchtitan/models/muse_glimmer/model.py:190`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L190) — documented in [muse-glimmer-model](../../../../concepts/muse-glimmer-model.md)
- doc: Output head that applies Muse Glimmer's output multiplier and optional tanh
- signature: `class SoftCappedLinear(Linear):`
- members:
  - <a id="SoftCappedLinear.forward"></a>`forward(self, input: torch.Tensor)` — [`L212`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L212)
  - <a id="SoftCappedLinear.output_multiplier"></a>`output_multiplier` — [`L209`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L209)
  - <a id="SoftCappedLinear.output_soft_cap_temp"></a>`output_soft_cap_temp` — [`L210`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L210)
- protocol/private: <a id="SoftCappedLinear.__init__"></a>`__init__`[`L207`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L207)
- uses (calls/refs, reference-scoped): [`Linear`](../common/linear.md#Linear), [`__init__`](../common/linear.md#Linear.__init__), [`Config`](model.md#SoftCappedLinear.Config), [`output_soft_cap_temp`](model.md#SoftCappedLinear.Config.output_soft_cap_temp), [`output_multiplier`](model.md#SoftCappedLinear.Config.output_multiplier)
- used by: [`Linear`](../common/linear.md#Linear), [`_muse_glimmer_config`](__init__.md#_muse_glimmer_config), [`fused_loss_soft_capped_lm_head`](../../experiments/tpu/overrides/fused_loss.md#fused_loss_soft_capped_lm_head)  (5 test-only)

### <a id="SoftCappedLinear.Config"></a>`SoftCappedLinear.Config`  ·  implements/extends Config
- def: [`torchtitan/models/muse_glimmer/model.py:203`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L203)
- signature: `class Config(Linear.Config):`
- members:
  - <a id="SoftCappedLinear.Config.output_multiplier"></a>`output_multiplier` — [`L204`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L204)
  - <a id="SoftCappedLinear.Config.output_soft_cap_temp"></a>`output_soft_cap_temp` — [`L205`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L205)
- uses (calls/refs, reference-scoped): [`Linear`](../common/linear.md#Linear), [`Config`](../common/linear.md#Linear.Config)
- used by: [`_muse_glimmer_config`](__init__.md#_muse_glimmer_config), [`fused_loss_soft_capped_lm_head`](../../experiments/tpu/overrides/fused_loss.md#fused_loss_soft_capped_lm_head), [`output_soft_cap_temp`](model.md#SoftCappedLinear.output_soft_cap_temp), [`__init__`](model.md#SoftCappedLinear.__init__), [`output_multiplier`](model.md#SoftCappedLinear.output_multiplier)  (3 test-only)

## Functions
- <a id="_window_mask_key"></a>`_window_mask_key(window_size: int | None)` — [`L53`](../../../../../../../raw/code/torchtitan/torchtitan/models/muse_glimmer/model.py#L53) — Mask-dict key for a layer's attention window (``"global"`` or ``"swa_<n>"``).

