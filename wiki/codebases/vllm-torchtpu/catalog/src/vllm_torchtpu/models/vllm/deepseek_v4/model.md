---
title: 'Module: src/vllm_torchtpu/models/vllm/deepseek_v4/model.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/deepseek_v4/model.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.deepseek_v4.model`/
symbols:
  DeepseekV4Model.forward: DeepseekV4Model#forward().
  DeepseekV4DecoderLayer.forward: DeepseekV4DecoderLayer#forward().
  DeepseekV4Model._dp_gather_hash_moe_input_ids: DeepseekV4Model#_dp_gather_hash_moe_input_ids().
  DeepseekV4DecoderLayer.mhc_ops: DeepseekV4DecoderLayer#mhc_ops().
  DeepseekV4Model.load_weights: DeepseekV4Model#load_weights().
  DeepseekV4DecoderLayer.rms_norm_eps: DeepseekV4DecoderLayer#rms_norm_eps.
  DeepseekV4ForCausalLM.model: DeepseekV4ForCausalLM#model.
  _HostStagedParams.flush_all: _HostStagedParams#flush_all().
  DeepseekV4Model.layers: DeepseekV4Model#layers.
  DeepseekV4ForCausalLM.set_aux_hidden_state_layers: DeepseekV4ForCausalLM#set_aux_hidden_state_layers().
  DeepseekV4ForCausalLM.load_weights: DeepseekV4ForCausalLM#load_weights().
  DeepseekV4DecoderLayer: DeepseekV4DecoderLayer#
  _HostStagedParams._staged: _HostStagedParams#_staged.
  DeepseekV4Model.norm: DeepseekV4Model#norm.
  _HostStagedParams.stage: _HostStagedParams#stage().
  DeepseekV4DecoderLayer.attn: DeepseekV4DecoderLayer#attn.
  DeepseekV4DecoderLayer.attn_norm: DeepseekV4DecoderLayer#attn_norm.
  DeepseekV4DecoderLayer.ffn_norm: DeepseekV4DecoderLayer#ffn_norm.
  DeepseekV4DecoderLayer.hc_post_alpha: DeepseekV4DecoderLayer#hc_post_alpha.
  DeepseekV4DecoderLayer.hc_pre: DeepseekV4DecoderLayer#hc_pre().
  DeepseekV4Model.hc_head_fn: DeepseekV4Model#hc_head_fn.
  DeepseekV4Model._mtp_hidden_buffer: DeepseekV4Model#_mtp_hidden_buffer.
  DeepseekV4Model.make_empty_intermediate_tensors: DeepseekV4Model#make_empty_intermediate_tensors().
  DeepseekV4Model.mhc_post_op: DeepseekV4Model#mhc_post_op().
  DeepseekV4Model.get_expert_mapping: DeepseekV4Model#get_expert_mapping().
  DeepseekV4Model: DeepseekV4Model#
  DeepseekV4Model.config: DeepseekV4Model#config.
  DeepseekV4Model.hc_mult: DeepseekV4Model#hc_mult.
  DeepseekV4ForCausalLM.config: DeepseekV4ForCausalLM#config.
  DeepseekV4ForCausalLM.make_empty_intermediate_tensors: DeepseekV4ForCausalLM#make_empty_intermediate_tensors.
  DeepseekV4ForCausalLM.embed_input_ids: DeepseekV4ForCausalLM#embed_input_ids().
  DeepseekV4ForCausalLM.compute_logits: DeepseekV4ForCausalLM#compute_logits().
  DeepseekV4ForCausalLM.get_expert_mapping: DeepseekV4ForCausalLM#get_expert_mapping().
  DeepseekV4DecoderLayer.ffn: DeepseekV4DecoderLayer#ffn.
  DeepseekV4Model.hc_dim: DeepseekV4Model#hc_dim.
  DeepseekV4Model.embed_tokens: DeepseekV4Model#embed_tokens.
  DeepseekV4Model.embed_input_ids: DeepseekV4Model#embed_input_ids().
  DeepseekV4ForCausalLM.hf_to_vllm_mapper: DeepseekV4ForCausalLM#hf_to_vllm_mapper.
  DeepseekV4ForCausalLM.lm_head: DeepseekV4ForCausalLM#lm_head.
  DeepseekV4Model.start_layer: DeepseekV4Model#start_layer.
  _make_deepseek_v4_weights_mapper: _make_deepseek_v4_weights_mapper().
  logger: logger.
  _HostStagedParams._flush: _HostStagedParams#_flush().
  DeepseekV4Model.hc_head_base: DeepseekV4Model#hc_head_base.
  DeepseekV4ForCausalLM.model_cls: DeepseekV4ForCausalLM#model_cls.
  DeepseekV4DecoderLayer.hidden_size: DeepseekV4DecoderLayer#hidden_size.
  DeepseekV4DecoderLayer.hc_mult: DeepseekV4DecoderLayer#hc_mult.
  DeepseekV4Model.end_layer: DeepseekV4Model#end_layer.
  DeepseekV4Model.aux_hidden_state_layers: DeepseekV4Model#aux_hidden_state_layers.
  DeepseekV4ForCausalLM.forward: DeepseekV4ForCausalLM#forward().
  DeepseekV4ForCausalLM.get_mtp_target_hidden_states: DeepseekV4ForCausalLM#get_mtp_target_hidden_states().
  DeepseekV4DecoderLayer.hc_eps: DeepseekV4DecoderLayer#hc_eps.
  DeepseekV4DecoderLayer.hc_attn_fn: DeepseekV4DecoderLayer#hc_attn_fn.
  DeepseekV4DecoderLayer.hc_attn_base: DeepseekV4DecoderLayer#hc_attn_base.
  DeepseekV4DecoderLayer.hc_attn_scale: DeepseekV4DecoderLayer#hc_attn_scale.
  DeepseekV4Model.rms_norm_eps: DeepseekV4Model#rms_norm_eps.
  DeepseekV4DecoderLayer.hc_sinkhorn_iters: DeepseekV4DecoderLayer#hc_sinkhorn_iters.
  DeepseekV4DecoderLayer.hc_ffn_fn: DeepseekV4DecoderLayer#hc_ffn_fn.
  DeepseekV4DecoderLayer.hc_ffn_base: DeepseekV4DecoderLayer#hc_ffn_base.
  DeepseekV4DecoderLayer.hc_ffn_scale: DeepseekV4DecoderLayer#hc_ffn_scale.
  _HostStagedParams: _HostStagedParams#
  DeepseekV4Model.hc_eps: DeepseekV4Model#hc_eps.
  DeepseekV4Model.topk_indices_buffer: DeepseekV4Model#topk_indices_buffer.
  DeepseekV4Model.hc_head_scale: DeepseekV4Model#hc_head_scale.
  DeepseekV4ForCausalLM: DeepseekV4ForCausalLM#
  DeepseekV4ForCausalLM.logits_processor: DeepseekV4ForCausalLM#logits_processor.
  DeepseekV4DecoderLayer.__init__: DeepseekV4DecoderLayer#__init__().
  DeepseekV4DecoderLayer.prefix: DeepseekV4DecoderLayer#prefix.
  DeepseekV4DecoderLayer.layer_idx: DeepseekV4DecoderLayer#layer_idx.
  _HostStagedParams.__init__: _HostStagedParams#__init__().
  DeepseekV4Model.__init__: DeepseekV4Model#__init__().
  DeepseekV4Model.vocab_size: DeepseekV4Model#vocab_size.
  DeepseekV4ForCausalLM.__init__: DeepseekV4ForCausalLM#__init__().
---
# Module: [`src/vllm_torchtpu/models/vllm/deepseek_v4/model.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py)

## Classes
### <a id="DeepseekV4DecoderLayer"></a>`DeepseekV4DecoderLayer`
- def: [`src/vllm_torchtpu/models/vllm/deepseek_v4/model.py:69`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L69) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
- doc: Single transformer decoder layer for DeepSeek-V4 with MHC residual stream.
- signature: `class DeepseekV4DecoderLayer(nn.Module):`
- members:
  - <a id="DeepseekV4DecoderLayer.forward"></a>`forward(self, x: torch.Tensor, positions: torch.Tensor, input_ids: torch.Tensor | None = None, post_mix: torch.Tensor | None = None, res_mix: torch.Tensor | None = None, residual: torch.Tensor | None = None)` — [`L168`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L168) — Defer each post into the next pre so the pair is one kernel. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4DecoderLayer.hc_pre"></a>`hc_pre(self, x: torch.Tensor, hc_fn: torch.Tensor, hc_scale: torch.Tensor, hc_base: torch.Tensor)` — [`L153`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L153) — Gate the residual streams into this sublayer's input. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4DecoderLayer.mhc_ops"></a>`mhc_ops(self)` — [`L135`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L135) — This layer's mHC Pallas ops, built once outside the trace. — documented in [custom-ops](../../../../../../concepts/custom-ops.md)
  - <a id="DeepseekV4DecoderLayer.attn"></a>`attn` — [`L93`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L93) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4DecoderLayer.attn_norm"></a>`attn_norm` — [`L101`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L101) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4DecoderLayer.ffn"></a>`ffn` — [`L99`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L99) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4DecoderLayer.ffn_norm"></a>`ffn_norm` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L102) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4DecoderLayer.hc_attn_base"></a>`hc_attn_base` — [`L117`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L117)
  - <a id="DeepseekV4DecoderLayer.hc_attn_fn"></a>`hc_attn_fn` — [`L109`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L109)
  - <a id="DeepseekV4DecoderLayer.hc_attn_scale"></a>`hc_attn_scale` — [`L125`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L125)
  - <a id="DeepseekV4DecoderLayer.hc_eps"></a>`hc_eps` — [`L105`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L105)
  - <a id="DeepseekV4DecoderLayer.hc_ffn_base"></a>`hc_ffn_base` — [`L121`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L121)
  - <a id="DeepseekV4DecoderLayer.hc_ffn_fn"></a>`hc_ffn_fn` — [`L113`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L113)
  - <a id="DeepseekV4DecoderLayer.hc_ffn_scale"></a>`hc_ffn_scale` — [`L129`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L129)
  - <a id="DeepseekV4DecoderLayer.hc_mult"></a>`hc_mult` — [`L103`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L103)
  - <a id="DeepseekV4DecoderLayer.hc_post_alpha"></a>`hc_post_alpha` — [`L106`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L106)
  - <a id="DeepseekV4DecoderLayer.hc_sinkhorn_iters"></a>`hc_sinkhorn_iters` — [`L104`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L104)
  - <a id="DeepseekV4DecoderLayer.hidden_size"></a>`hidden_size` — [`L81`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L81)
  - <a id="DeepseekV4DecoderLayer.layer_idx"></a>`layer_idx` — [`L85`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L85)
  - <a id="DeepseekV4DecoderLayer.prefix"></a>`prefix` — [`L82`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L82)
  - <a id="DeepseekV4DecoderLayer.rms_norm_eps"></a>`rms_norm_eps` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L87) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
- protocol/private: <a id="DeepseekV4DecoderLayer.__init__"></a>`__init__`[`L72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L72)
- uses (calls/refs, reference-scoped): [`get_mhc_ops`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.md#get_mhc_ops), [`VllmDeepseekV4MLAAttention`](attention.md#VllmDeepseekV4MLAAttention), [`MHCOps`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.md#MHCOps), [`VllmDeepseekV4MLAAttentionIntraChip`](attn_intra_chip.md#VllmDeepseekV4MLAAttentionIntraChip), [`fused`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.md#MHCOps.fused), [`DeepseekV4MoE`](moe.md#DeepseekV4MoE), [`pre`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.md#MHCOps.pre), [`TPU_DSV4_ATTN_INTRA_CHIP_TP`](../../../envs.md#TPU_DSV4_ATTN_INTRA_CHIP_TP)
- used by: [`layers`](dspark.md#DSparkDeepseekV4Model.layers), [`_dp_gather_hash_moe_input_ids`](model.md#DeepseekV4Model._dp_gather_hash_moe_input_ids), [`precompute_and_store_context_kv`](dspark.md#DSparkDeepseekV4Model.precompute_and_store_context_kv), [`get_draft_kv_cache_layer_names`](dspark.md#DSparkDeepseekV4Model.get_draft_kv_cache_layer_names), [`layers`](model.md#DeepseekV4Model.layers)

### <a id="DeepseekV4ForCausalLM"></a>`DeepseekV4ForCausalLM`
- def: [`src/vllm_torchtpu/models/vllm/deepseek_v4/model.py:657`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L657)
- doc: DeepSeek-V4 causal language model registered for TPU inference.
- signature: `class DeepseekV4ForCausalLM(nn.Module, SupportsPP):`
- members:
  - <a id="DeepseekV4ForCausalLM.compute_logits"></a>`compute_logits(self, hidden_states: torch.Tensor)` — [`L693`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L693)
  - <a id="DeepseekV4ForCausalLM.embed_input_ids"></a>`embed_input_ids(self, input_ids: torch.Tensor)` — [`L690`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L690)
  - <a id="DeepseekV4ForCausalLM.forward"></a>`forward(self, input_ids: torch.Tensor | None, positions: torch.Tensor, intermediate_tensors: IntermediateTensors | None = None, inputs_embeds: torch.Tensor | None = None)` — [`L699`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L699)
  - <a id="DeepseekV4ForCausalLM.get_expert_mapping"></a>`get_expert_mapping(self)` — [`L742`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L742)
  - <a id="DeepseekV4ForCausalLM.get_mtp_target_hidden_states"></a>`get_mtp_target_hidden_states(self)` — [`L708`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L708)
  - <a id="DeepseekV4ForCausalLM.load_weights"></a>`load_weights(self, weights: Iterable[tuple[str, torch.Tensor]])` — [`L720`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L720)
  - <a id="DeepseekV4ForCausalLM.set_aux_hidden_state_layers"></a>`set_aux_hidden_state_layers(self, layers: tuple[int, ...])` — [`L711`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L711) — Tag layers whose post-layer state feeds an eagle-family draft.
  - <a id="DeepseekV4ForCausalLM.config"></a>`config` — [`L669`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L669)
  - <a id="DeepseekV4ForCausalLM.hf_to_vllm_mapper"></a>`hf_to_vllm_mapper` — [`L661`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L661)
  - <a id="DeepseekV4ForCausalLM.lm_head"></a>`lm_head` — [`L678`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L678)
  - <a id="DeepseekV4ForCausalLM.logits_processor"></a>`logits_processor` — [`L685`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L685)
  - <a id="DeepseekV4ForCausalLM.make_empty_intermediate_tensors"></a>`make_empty_intermediate_tensors` — [`L686`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L686)
  - <a id="DeepseekV4ForCausalLM.model"></a>`model` — [`L674`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L674)
  - <a id="DeepseekV4ForCausalLM.model_cls"></a>`model_cls` — [`L660`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L660)
- protocol/private: <a id="DeepseekV4ForCausalLM.__init__"></a>`__init__`[`L663`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L663)
- uses (calls/refs, reference-scoped): [`layers`](model.md#DeepseekV4Model.layers), [`VllmDeepseekCompressor`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.md#VllmDeepseekCompressor), [`make_empty_intermediate_tensors`](model.md#DeepseekV4Model.make_empty_intermediate_tensors), [`transpose_wkv_wgate`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_compressor.md#VllmDeepseekCompressor.transpose_wkv_wgate), [`get_expert_mapping`](model.md#DeepseekV4Model.get_expert_mapping), [`DeepseekV4Model`](model.md#DeepseekV4Model), [`embed_input_ids`](model.md#DeepseekV4Model.embed_input_ids), [`_make_deepseek_v4_weights_mapper`](model.md#_make_deepseek_v4_weights_mapper), [`aux_hidden_state_layers`](model.md#DeepseekV4Model.aux_hidden_state_layers)

### <a id="DeepseekV4Model"></a>`DeepseekV4Model`
- def: [`src/vllm_torchtpu/models/vllm/deepseek_v4/model.py:285`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L285)
- doc: DeepSeek-V4 backbone model containing token embedding, layers, and head.
- signature: `class DeepseekV4Model(nn.Module):`
- members:
  - <a id="DeepseekV4Model._dp_gather_hash_moe_input_ids"></a>`_dp_gather_hash_moe_input_ids(self, input_ids: torch.Tensor)` — [`L375`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L375) — All-gather input_ids over the DP group for hash-MoE routing. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4Model.embed_input_ids"></a>`embed_input_ids(self, input_ids: torch.Tensor)` — [`L372`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L372) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4Model.forward"></a>`forward(self, input_ids: torch.Tensor, positions: torch.Tensor, intermediate_tensors: IntermediateTensors | None = None, inputs_embeds: torch.Tensor | None = None)` — [`L424`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L424) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4Model.get_expert_mapping"></a>`get_expert_mapping(self)` — [`L615`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L615) — Generate MoE expert parameter mappings for weight loading.
  - <a id="DeepseekV4Model.load_weights"></a>`load_weights(self, weights: Iterable[tuple[str, torch.Tensor]])` — [`L500`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L500) — Load checkpoint tensors into stacked, expert, sink and plain params.
  - <a id="DeepseekV4Model.make_empty_intermediate_tensors"></a>`make_empty_intermediate_tensors(self, batch_size: int, dtype: torch.dtype, device: torch.device)` — [`L409`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L409)
  - <a id="DeepseekV4Model.mhc_post_op"></a>`mhc_post_op(self)` — [`L359`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L359) — The op that settles the post the last decoder layer deferred. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4Model.aux_hidden_state_layers"></a>`aux_hidden_state_layers` — [`L356`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L356)
  - <a id="DeepseekV4Model.config"></a>`config` — [`L293`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L293) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4Model.embed_tokens"></a>`embed_tokens` — [`L307`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L307)
  - <a id="DeepseekV4Model.end_layer"></a>`end_layer` — [`L316`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L316)
  - <a id="DeepseekV4Model.hc_dim"></a>`hc_dim` — [`L297`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L297)
  - <a id="DeepseekV4Model.hc_eps"></a>`hc_eps` — [`L295`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L295)
  - <a id="DeepseekV4Model.hc_head_base"></a>`hc_head_base` — [`L336`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L336)
  - <a id="DeepseekV4Model.hc_head_fn"></a>`hc_head_fn` — [`L332`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L332) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4Model.hc_head_scale"></a>`hc_head_scale` — [`L340`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L340)
  - <a id="DeepseekV4Model.hc_mult"></a>`hc_mult` — [`L296`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L296) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4Model.layers"></a>`layers` — [`L316`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L316)
  - <a id="DeepseekV4Model.norm"></a>`norm` — [`L328`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L328) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DeepseekV4Model.rms_norm_eps"></a>`rms_norm_eps` — [`L298`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L298)
  - <a id="DeepseekV4Model.start_layer"></a>`start_layer` — [`L316`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L316)
  - <a id="DeepseekV4Model.topk_indices_buffer"></a>`topk_indices_buffer` — [`L300`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L300)
  - <a id="DeepseekV4Model.vocab_size"></a>`vocab_size` — [`L294`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L294)
- protocol/private: <a id="DeepseekV4Model.__init__"></a>`__init__`[`L288`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L288), <a id="DeepseekV4Model._mtp_hidden_buffer"></a>`_mtp_hidden_buffer`[`L346`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L346)
- uses (calls/refs, reference-scoped): [`get_mhc_post_op`](../../../layers/adapter/custom_ops/deepseek_v4/deepseek_v4_mhc_op.md#get_mhc_post_op), [`flush_all`](model.md#_HostStagedParams.flush_all), [`DeepseekV4DecoderLayer`](model.md#DeepseekV4DecoderLayer), [`stage`](model.md#_HostStagedParams.stage), [`ffn`](model.md#DeepseekV4DecoderLayer.ffn), [`mhc_collapse_head`](layers.md#mhc_collapse_head), [`routes_dp_gathered_tokens`](moe.md#DeepseekV4MoE.routes_dp_gathered_tokens), [`_HostStagedParams`](model.md#_HostStagedParams)
- used by: [`set_aux_hidden_state_layers`](model.md#DeepseekV4ForCausalLM.set_aux_hidden_state_layers), [`load_weights`](dspark.md#DSparkDeepseekV4Model.load_weights), [`mhc_post_op`](dspark.md#DSparkDeepseekV4Model.mhc_post_op), [`embed_input_ids`](model.md#DeepseekV4ForCausalLM.embed_input_ids), [`get_expert_mapping`](dspark.md#DSparkDeepseekV4Model.get_expert_mapping), [`get_expert_mapping`](model.md#DeepseekV4ForCausalLM.get_expert_mapping), [`make_empty_intermediate_tensors`](model.md#DeepseekV4ForCausalLM.make_empty_intermediate_tensors), [`model_cls`](model.md#DeepseekV4ForCausalLM.model_cls)

### <a id="_HostStagedParams"></a>`_HostStagedParams`
- def: [`src/vllm_torchtpu/models/vllm/deepseek_v4/model.py:218`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L218)
- doc: Redirects weight-loading writes into host memory, one device write out.
- signature: `class _HostStagedParams:`
- members:
  - <a id="_HostStagedParams.flush_all"></a>`flush_all(self)` — [`L264`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L264) — Flush every staged parameter and release all host buffers.
  - <a id="_HostStagedParams.stage"></a>`stage(self, name: str, param: torch.nn.Parameter)` — [`L238`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L238) — Return a host-backed stand-in for `param` for loaders to write.
- protocol/private: <a id="_HostStagedParams.__init__"></a>`__init__`[`L234`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L234), <a id="_HostStagedParams._flush"></a>`_flush`[`L257`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L257), <a id="_HostStagedParams._staged"></a>`_staged`[`L236`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L236)
- uses (calls/refs, reference-scoped): [`logger`](model.md#logger)
- used by: [`load_weights`](model.md#DeepseekV4Model.load_weights)

## Functions
- <a id="_make_deepseek_v4_weights_mapper"></a>`_make_deepseek_v4_weights_mapper(expert_dtype: str)` — [`L626`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L626) — Weights mapper adapting checkpoint naming to vllm-torchtpu layer names.

## Module values
- <a id="logger"></a>`logger` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/model.py#L66)

