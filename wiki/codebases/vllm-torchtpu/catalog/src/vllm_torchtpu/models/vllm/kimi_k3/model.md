---
title: 'Module: src/vllm_torchtpu/models/vllm/kimi_k3/model.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/kimi_k3/model.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.kimi_k3.model`/
symbols:
  KimiModel.forward: KimiModel#forward().
  KimiK3ForConditionalGeneration.vision_tower: KimiK3ForConditionalGeneration#vision_tower.
  KimiDecoderLayer.forward: KimiDecoderLayer#forward().
  KimiLinearForCausalLM.process_weights_after_loading: KimiLinearForCausalLM#process_weights_after_loading().
  KimiK3ForConditionalGeneration.mm_projector: KimiK3ForConditionalGeneration#mm_projector.
  KimiDecoderLayer.self_attn: KimiDecoderLayer#self_attn.
  KimiK3ForConditionalGeneration.embed_multimodal: KimiK3ForConditionalGeneration#embed_multimodal().
  KimiLinearForCausalLM.load_weights: KimiLinearForCausalLM#load_weights().
  KimiLinearForCausalLM.set_aux_hidden_state_layers: KimiLinearForCausalLM#set_aux_hidden_state_layers().
  KimiModel.sp_group: KimiModel#sp_group.
  KimiK3ForConditionalGeneration.language_model: KimiK3ForConditionalGeneration#language_model.
  KimiK3ForConditionalGeneration.encoder_eager_forward: KimiK3ForConditionalGeneration#encoder_eager_forward().
  KimiModel.sp_prefill: KimiModel#sp_prefill.
  KimiLinearForCausalLM.config: KimiLinearForCausalLM#config.
  KimiDecoderLayer.layer_idx: KimiDecoderLayer#layer_idx.
  KimiLinearForCausalLM.model: KimiLinearForCausalLM#model.
  KimiLinearForCausalLM.compute_logits: KimiLinearForCausalLM#compute_logits().
  _tpu_tp_all_gather: _tpu_tp_all_gather().
  KimiDecoderLayer.attn_res_block_size: KimiDecoderLayer#attn_res_block_size.
  KimiModel.aux_hidden_state_layers: KimiModel#aux_hidden_state_layers.
  KimiLinearForCausalLM: KimiLinearForCausalLM#
  KimiLinearForCausalLM.embed_input_ids: KimiLinearForCausalLM#embed_input_ids().
  KimiK3ForConditionalGeneration.set_aux_hidden_state_layers: KimiK3ForConditionalGeneration#set_aux_hidden_state_layers().
  KimiK3ForConditionalGeneration.get_encoder_cudagraph_item_specs: KimiK3ForConditionalGeneration#get_encoder_cudagraph_item_specs().
  KimiK3ForConditionalGeneration.prepare_encoder_cudagraph_replay_buffers: KimiK3ForConditionalGeneration#prepare_encoder_cudagraph_replay_buffers().
  KimiK3ForConditionalGeneration.encoder_cudagraph_forward: KimiK3ForConditionalGeneration#encoder_cudagraph_forward().
  KimiK3ForConditionalGeneration.embed_input_ids: KimiK3ForConditionalGeneration#embed_input_ids().
  KimiK3ForConditionalGeneration.compute_logits: KimiK3ForConditionalGeneration#compute_logits().
  KimiK3ForConditionalGeneration.process_weights_after_loading: KimiK3ForConditionalGeneration#process_weights_after_loading().
  KimiK3ForConditionalGeneration.get_mamba_state_dtype_from_config: KimiK3ForConditionalGeneration#get_mamba_state_dtype_from_config().
  KimiK3ForConditionalGeneration.get_mamba_state_shape_from_config: KimiK3ForConditionalGeneration#get_mamba_state_shape_from_config().
  KimiK3ForConditionalGeneration.get_mamba_state_copy_func: KimiK3ForConditionalGeneration#get_mamba_state_copy_func().
  KimiDecoderLayer.block_sparse_moe: KimiDecoderLayer#block_sparse_moe.
  KimiDecoderLayer.mlp: KimiDecoderLayer#mlp.
  KimiModel.layers: KimiModel#layers.
  KimiModel.embed_input_ids: KimiModel#embed_input_ids().
  KimiK3ForConditionalGeneration.use_data_parallel: KimiK3ForConditionalGeneration#use_data_parallel.
  KimiK3ForConditionalGeneration._grid_thw_list: KimiK3ForConditionalGeneration#_grid_thw_list().
  logger: logger.
  KimiDecoderLayer.self_attention_res: KimiDecoderLayer#self_attention_res.
  KimiDecoderLayer.mlp_res: KimiDecoderLayer#mlp_res.
  KimiModel.output_attn_res: KimiModel#output_attn_res.
  KimiLinearForCausalLM.lm_head: KimiLinearForCausalLM#lm_head.
  KimiLinearForCausalLM.logits_processor: KimiLinearForCausalLM#logits_processor.
  KimiLinearForCausalLM.get_mamba_state_dtype_from_config: KimiLinearForCausalLM#get_mamba_state_dtype_from_config().
  KimiLinearForCausalLM._ordinary_weights: KimiLinearForCausalLM#_ordinary_weights().
  KimiK3ForConditionalGeneration._parse_and_validate_media_input: KimiK3ForConditionalGeneration#_parse_and_validate_media_input().
  KimiK3ForConditionalGeneration.device: KimiK3ForConditionalGeneration#device.
  KimiModel.__init__: KimiModel#__init__().
  KimiLinearForCausalLM.forward: KimiLinearForCausalLM#forward().
  KimiK3ForConditionalGeneration.get_encoder_cudagraph_config: KimiK3ForConditionalGeneration#get_encoder_cudagraph_config().
  KimiK3ForConditionalGeneration.select_encoder_cudagraph_items: KimiK3ForConditionalGeneration#select_encoder_cudagraph_items().
  KimiK3ForConditionalGeneration.prepare_encoder_cudagraph_capture_inputs: KimiK3ForConditionalGeneration#prepare_encoder_cudagraph_capture_inputs().
  KimiK3ForConditionalGeneration.forward: KimiK3ForConditionalGeneration#forward().
  KimiK3ForConditionalGeneration.load_weights: KimiK3ForConditionalGeneration#load_weights().
  KimiDecoderLayer.is_moe: KimiDecoderLayer#is_moe.
  KimiDecoderLayer.input_layernorm: KimiDecoderLayer#input_layernorm.
  KimiDecoderLayer.post_attention_layernorm: KimiDecoderLayer#post_attention_layernorm.
  KimiModel: KimiModel#
  KimiModel.attn_res_block_size: KimiModel#attn_res_block_size.
  KimiDecoderLayer: KimiDecoderLayer#
  KimiModel.embed_tokens: KimiModel#embed_tokens.
  KimiModel.norm: KimiModel#norm.
  KimiLinearForCausalLM.hf_to_vllm_mapper: KimiLinearForCausalLM#hf_to_vllm_mapper.
  KimiLinearForCausalLM.fused_mla_mapper: KimiLinearForCausalLM#fused_mla_mapper.
  KimiLinearForCausalLM.fused_attention_params_mapping: KimiLinearForCausalLM#fused_attention_params_mapping.
  KimiLinearForCausalLM.get_mamba_state_shape_from_config: KimiLinearForCausalLM#get_mamba_state_shape_from_config().
  KimiLinearForCausalLM.get_mamba_state_copy_func: KimiLinearForCausalLM#get_mamba_state_copy_func().
  KimiK3ForConditionalGeneration: KimiK3ForConditionalGeneration#
  KimiK3ForConditionalGeneration.hf_to_vllm_mapper: KimiK3ForConditionalGeneration#hf_to_vllm_mapper.
  KimiK3ForConditionalGeneration.hidden_size: KimiK3ForConditionalGeneration#hidden_size.
  KimiK3ForConditionalGeneration._maybe_ignore_quant_config: KimiK3ForConditionalGeneration#_maybe_ignore_quant_config().
  KimiDecoderLayer.__init__: KimiDecoderLayer#__init__().
  KimiLinearForCausalLM.__init__: KimiLinearForCausalLM#__init__().
  KimiK3ForConditionalGeneration.supports_encoder_tp_data: KimiK3ForConditionalGeneration#supports_encoder_tp_data.
  KimiK3ForConditionalGeneration.get_placeholder_str: KimiK3ForConditionalGeneration#get_placeholder_str().
  KimiK3ForConditionalGeneration.__init__: KimiK3ForConditionalGeneration#__init__().
  KimiK3ForConditionalGeneration.config: KimiK3ForConditionalGeneration#config.
  KimiK3ForConditionalGeneration.quant_config: KimiK3ForConditionalGeneration#quant_config.
  KimiK3ForConditionalGeneration.media_placeholder: KimiK3ForConditionalGeneration#media_placeholder.
  KimiK3ForConditionalGeneration.supports_encoder_cudagraph: KimiK3ForConditionalGeneration#supports_encoder_cudagraph.
  KimiK3ForConditionalGeneration.get_input_modality: KimiK3ForConditionalGeneration#get_input_modality().
  KimiK3ForConditionalGeneration.get_max_frames_per_video: KimiK3ForConditionalGeneration#get_max_frames_per_video().
  KimiK3ForConditionalGeneration.get_encoder_cudagraph_budget_range: KimiK3ForConditionalGeneration#get_encoder_cudagraph_budget_range().
---
# Module: [`src/vllm_torchtpu/models/vllm/kimi_k3/model.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py)

## Classes
### <a id="KimiDecoderLayer"></a>`KimiDecoderLayer`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/model.py:90`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L90)
- signature: `class KimiDecoderLayer(nn.Module):`
- members:
  - <a id="KimiDecoderLayer.forward"></a>`forward(self, positions: torch.Tensor, hidden_states: torch.Tensor, block_residuals: torch.Tensor | None, sequence_parallel: bool = False)` — [`L150`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L150) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiDecoderLayer.attn_res_block_size"></a>`attn_res_block_size` — [`L137`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L137)
  - <a id="KimiDecoderLayer.block_sparse_moe"></a>`block_sparse_moe` — [`L119`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L119)
  - <a id="KimiDecoderLayer.input_layernorm"></a>`input_layernorm` — [`L134`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L134)
  - <a id="KimiDecoderLayer.is_moe"></a>`is_moe` — [`L117`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L117)
  - <a id="KimiDecoderLayer.layer_idx"></a>`layer_idx` — [`L98`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L98)
  - <a id="KimiDecoderLayer.mlp"></a>`mlp` — [`L125`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L125)
  - <a id="KimiDecoderLayer.mlp_res"></a>`mlp_res` — [`L144`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L144)
  - <a id="KimiDecoderLayer.post_attention_layernorm"></a>`post_attention_layernorm` — [`L135`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L135)
  - <a id="KimiDecoderLayer.self_attention_res"></a>`self_attention_res` — [`L139`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L139)
  - <a id="KimiDecoderLayer.self_attn"></a>`self_attn` — [`L100`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L100) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
- protocol/private: <a id="KimiDecoderLayer.__init__"></a>`__init__`[`L91`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L91)
- uses (calls/refs, reference-scoped): [`KimiMLP`](layers.md#KimiMLP), [`MultiHeadLatentAttention`](attention.md#MultiHeadLatentAttention), [`AttentionResidual`](layers.md#AttentionResidual), [`KimiMoE`](moe.md#KimiMoE), [`KimiDeltaAttention`](attention.md#KimiDeltaAttention)
- used by: [`layers`](model.md#KimiModel.layers)

### <a id="KimiK3ForConditionalGeneration"></a>`KimiK3ForConditionalGeneration`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/model.py:546`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L546)
- doc: Kimi-K3 with upstream preprocessing and TPU model execution.
- signature: `class KimiK3ForConditionalGeneration(nn.Module, SupportsMultiModal, SupportsEncoderCudaGraph, SupportsQuant, HasInnerState, IsHybrid):`
- members:
  - <a id="KimiK3ForConditionalGeneration.compute_logits"></a>`compute_logits(self, hidden_states: torch.Tensor, **kwargs: object)` — [`L983`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L983)
  - <a id="KimiK3ForConditionalGeneration.embed_input_ids"></a>`embed_input_ids(self, input_ids: torch.Tensor, multimodal_embeddings: NestedTensors | None = None, *, is_multimodal: torch.Tensor | None = None)` — [`L921`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L921)
  - <a id="KimiK3ForConditionalGeneration.embed_multimodal"></a>`embed_multimodal(self, **kwargs: object)` — [`L672`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L672)
  - <a id="KimiK3ForConditionalGeneration.encoder_cudagraph_forward"></a>`encoder_cudagraph_forward(self, inputs: dict[str, torch.Tensor], path: str = "default")` — [`L874`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L874)
  - <a id="KimiK3ForConditionalGeneration.encoder_eager_forward"></a>`encoder_eager_forward(self, mm_kwargs: dict[str, object], path: str = "default")` — [`L891`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L891)
  - <a id="KimiK3ForConditionalGeneration.forward"></a>`forward(self, input_ids: torch.Tensor | None, positions: torch.Tensor, intermediate_tensors: IntermediateTensors | None = None, inputs_embeds: torch.Tensor | None = None, **kwargs: object)` — [`L967`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L967)
  - <a id="KimiK3ForConditionalGeneration.get_encoder_cudagraph_budget_range"></a>`get_encoder_cudagraph_budget_range(self, vllm_config: VllmConfig)` — [`L727`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L727)
  - <a id="KimiK3ForConditionalGeneration.get_encoder_cudagraph_config"></a>`get_encoder_cudagraph_config(self)` — [`L703`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L703)
  - <a id="KimiK3ForConditionalGeneration.get_encoder_cudagraph_item_specs"></a>`get_encoder_cudagraph_item_specs(self, mm_kwargs: dict[str, object])` — [`L746`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L746)
  - <a id="KimiK3ForConditionalGeneration.get_input_modality"></a>`get_input_modality(self, mm_kwargs: dict[str, object])` — [`L720`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L720)
  - <a id="KimiK3ForConditionalGeneration.get_mamba_state_copy_func"></a>`get_mamba_state_copy_func(cls)` — [`L1014`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L1014)
  - <a id="KimiK3ForConditionalGeneration.get_mamba_state_dtype_from_config"></a>`get_mamba_state_dtype_from_config(cls, vllm_config: VllmConfig)` — [`L994`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L994)
  - <a id="KimiK3ForConditionalGeneration.get_mamba_state_shape_from_config"></a>`get_mamba_state_shape_from_config(cls, vllm_config: VllmConfig)` — [`L1004`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L1004)
  - <a id="KimiK3ForConditionalGeneration.get_max_frames_per_video"></a>`get_max_frames_per_video(self)` — [`L724`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L724)
  - <a id="KimiK3ForConditionalGeneration.get_placeholder_str"></a>`get_placeholder_str(cls, modality: str, i: int)` — [`L567`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L567)
  - <a id="KimiK3ForConditionalGeneration.load_weights"></a>`load_weights(self, weights: Iterable[tuple[str, torch.Tensor]])` — [`L1017`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L1017)
  - <a id="KimiK3ForConditionalGeneration.prepare_encoder_cudagraph_capture_inputs"></a>`prepare_encoder_cudagraph_capture_inputs(self, token_budget: int, max_batch_size: int, max_frames_per_batch: int, device: torch.device, dtype: torch.dtype, path: str = "default", axis_keys: tuple[Hashable, ...] | None = None)` — [`L784`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L784)
  - <a id="KimiK3ForConditionalGeneration.prepare_encoder_cudagraph_replay_buffers"></a>`prepare_encoder_cudagraph_replay_buffers(self, mm_kwargs: dict[str, object], max_batch_size: int, max_frames_per_batch: int, path: str = "default")` — [`L853`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L853)
  - <a id="KimiK3ForConditionalGeneration.process_weights_after_loading"></a>`process_weights_after_loading(self)` — [`L989`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L989)
  - <a id="KimiK3ForConditionalGeneration.select_encoder_cudagraph_items"></a>`select_encoder_cudagraph_items(self, mm_kwargs: dict[str, object], indices: list[int])` — [`L759`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L759)
  - <a id="KimiK3ForConditionalGeneration.set_aux_hidden_state_layers"></a>`set_aux_hidden_state_layers(self, layers: tuple[int, ...])` — [`L627`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L627)
  - <a id="KimiK3ForConditionalGeneration.config"></a>`config` — [`L582`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L582)
  - <a id="KimiK3ForConditionalGeneration.device"></a>`device` — [`L584`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L584)
  - <a id="KimiK3ForConditionalGeneration.hf_to_vllm_mapper"></a>`hf_to_vllm_mapper` — [`L558`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L558)
  - <a id="KimiK3ForConditionalGeneration.hidden_size"></a>`hidden_size` — [`L583`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L583)
  - <a id="KimiK3ForConditionalGeneration.language_model"></a>`language_model` — [`L616`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L616)
  - <a id="KimiK3ForConditionalGeneration.media_placeholder"></a>`media_placeholder` — [`L625`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L625)
  - <a id="KimiK3ForConditionalGeneration.mm_projector"></a>`mm_projector` — [`L603`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L603)
  - <a id="KimiK3ForConditionalGeneration.quant_config"></a>`quant_config` — [`L614`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L614)
  - <a id="KimiK3ForConditionalGeneration.supports_encoder_cudagraph"></a>`supports_encoder_cudagraph` — [`L701`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L701)
  - <a id="KimiK3ForConditionalGeneration.supports_encoder_tp_data"></a>`supports_encoder_tp_data` — [`L556`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L556)
  - <a id="KimiK3ForConditionalGeneration.use_data_parallel"></a>`use_data_parallel` — [`L585`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L585)
  - <a id="KimiK3ForConditionalGeneration.vision_tower"></a>`vision_tower` — [`L591`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L591) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
- protocol/private: <a id="KimiK3ForConditionalGeneration.__init__"></a>`__init__`[`L573`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L573), <a id="KimiK3ForConditionalGeneration._grid_thw_list"></a>`_grid_thw_list`[`L741`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L741), <a id="KimiK3ForConditionalGeneration._maybe_ignore_quant_config"></a>`_maybe_ignore_quant_config`[`L633`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L633), <a id="KimiK3ForConditionalGeneration._parse_and_validate_media_input"></a>`_parse_and_validate_media_input`[`L640`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L640)
- uses (calls/refs, reference-scoped): [`synchronize_tensors`](../../../utils.md#synchronize_tensors), [`fresh_buffer`](../../../utils.md#fresh_buffer), [`process_weights_after_loading`](model.md#KimiLinearForCausalLM.process_weights_after_loading), [`set_aux_hidden_state_layers`](model.md#KimiLinearForCausalLM.set_aux_hidden_state_layers), [`_tpu_tp_all_gather`](model.md#_tpu_tp_all_gather), [`compute_logits`](model.md#KimiLinearForCausalLM.compute_logits), [`KimiLinearForCausalLM`](model.md#KimiLinearForCausalLM), [`get_mamba_state_dtype_from_config`](model.md#KimiLinearForCausalLM.get_mamba_state_dtype_from_config), [`KimiK3MoonViT3dPretrainedModel`](kimi_vit.md#KimiK3MoonViT3dPretrainedModel), [`get_mamba_state_copy_func`](model.md#KimiLinearForCausalLM.get_mamba_state_copy_func), [`get_mamba_state_shape_from_config`](model.md#KimiLinearForCausalLM.get_mamba_state_shape_from_config)

### <a id="KimiLinearForCausalLM"></a>`KimiLinearForCausalLM`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/model.py:321`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L321)
- doc: Kimi text model for TPU.
- signature: `class KimiLinearForCausalLM(nn.Module, HasInnerState, IsHybrid):`
- members:
  - <a id="KimiLinearForCausalLM.compute_logits"></a>`compute_logits(self, hidden_states: torch.Tensor)` — [`L397`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L397)
  - <a id="KimiLinearForCausalLM.embed_input_ids"></a>`embed_input_ids(self, input_ids: torch.Tensor)` — [`L373`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L373)
  - <a id="KimiLinearForCausalLM.forward"></a>`forward(self, input_ids: torch.Tensor | None, positions: torch.Tensor, inputs_embeds: torch.Tensor | None = None, intermediate_tensors: object | None = None)` — [`L382`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L382)
  - <a id="KimiLinearForCausalLM.get_mamba_state_copy_func"></a>`get_mamba_state_copy_func(cls)` — [`L444`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L444)
  - <a id="KimiLinearForCausalLM.get_mamba_state_dtype_from_config"></a>`get_mamba_state_dtype_from_config(cls, vllm_config: VllmConfig)` — [`L415`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L415)
  - <a id="KimiLinearForCausalLM.get_mamba_state_shape_from_config"></a>`get_mamba_state_shape_from_config(cls, vllm_config: VllmConfig)` — [`L424`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L424)
  - <a id="KimiLinearForCausalLM.load_weights"></a>`load_weights(self, weights: Iterable[tuple[str, torch.Tensor]])` — [`L449`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L449)
  - <a id="KimiLinearForCausalLM.process_weights_after_loading"></a>`process_weights_after_loading(self)` — [`L400`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L400) — Fold every AttentionResidual's norm and projection weights. — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiLinearForCausalLM.set_aux_hidden_state_layers"></a>`set_aux_hidden_state_layers(self, layers: tuple[int, ...])` — [`L376`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L376)
  - <a id="KimiLinearForCausalLM.config"></a>`config` — [`L360`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L360)
  - <a id="KimiLinearForCausalLM.fused_attention_params_mapping"></a>`fused_attention_params_mapping` — [`L348`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L348)
  - <a id="KimiLinearForCausalLM.fused_mla_mapper"></a>`fused_mla_mapper` — [`L342`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L342)
  - <a id="KimiLinearForCausalLM.hf_to_vllm_mapper"></a>`hf_to_vllm_mapper` — [`L324`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L324)
  - <a id="KimiLinearForCausalLM.lm_head"></a>`lm_head` — [`L365`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L365)
  - <a id="KimiLinearForCausalLM.logits_processor"></a>`logits_processor` — [`L371`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L371)
  - <a id="KimiLinearForCausalLM.model"></a>`model` — [`L361`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L361)
- protocol/private: <a id="KimiLinearForCausalLM.__init__"></a>`__init__`[`L358`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L358), <a id="KimiLinearForCausalLM._ordinary_weights"></a>`_ordinary_weights`[`L477`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L477)
- uses (calls/refs, reference-scoped): [`prepare_sp_mla_gate`](attention.md#MultiHeadLatentAttention.prepare_sp_mla_gate), [`process_weights_after_loading`](layers.md#AttentionResidual.process_weights_after_loading), [`MultiHeadLatentAttention`](attention.md#MultiHeadLatentAttention), [`initialize_dummy_router`](moe.md#KimiMoE.initialize_dummy_router), [`aux_hidden_state_layers`](model.md#KimiModel.aux_hidden_state_layers), [`AttentionResidual`](layers.md#AttentionResidual), [`embed_input_ids`](model.md#KimiModel.embed_input_ids), [`layers`](model.md#KimiModel.layers), [`KimiMoE`](moe.md#KimiMoE), [`kda_state_dtype`](attention.md#kda_state_dtype), [`KimiModel`](model.md#KimiModel)
- used by: [`language_model`](model.md#KimiK3ForConditionalGeneration.language_model), [`compute_logits`](model.md#KimiK3ForConditionalGeneration.compute_logits), [`get_mamba_state_copy_func`](model.md#KimiK3ForConditionalGeneration.get_mamba_state_copy_func), [`get_mamba_state_dtype_from_config`](model.md#KimiK3ForConditionalGeneration.get_mamba_state_dtype_from_config), [`get_mamba_state_shape_from_config`](model.md#KimiK3ForConditionalGeneration.get_mamba_state_shape_from_config), [`process_weights_after_loading`](model.md#KimiK3ForConditionalGeneration.process_weights_after_loading), [`set_aux_hidden_state_layers`](model.md#KimiK3ForConditionalGeneration.set_aux_hidden_state_layers)

### <a id="KimiModel"></a>`KimiModel`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/model.py:209`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L209)
- signature: `class KimiModel(nn.Module):`
- members:
  - <a id="KimiModel.embed_input_ids"></a>`embed_input_ids(self, input_ids: torch.Tensor)` — [`L261`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L261)
  - <a id="KimiModel.forward"></a>`forward(self, input_ids: torch.Tensor | None, positions: torch.Tensor, inputs_embeds: torch.Tensor | None = None)` — [`L264`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L264) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="KimiModel.attn_res_block_size"></a>`attn_res_block_size` — [`L223`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L223)
  - <a id="KimiModel.aux_hidden_state_layers"></a>`aux_hidden_state_layers` — [`L253`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L253)
  - <a id="KimiModel.embed_tokens"></a>`embed_tokens` — [`L236`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L236)
  - <a id="KimiModel.layers"></a>`layers` — [`L242`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L242)
  - <a id="KimiModel.norm"></a>`norm` — [`L252`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L252)
  - <a id="KimiModel.output_attn_res"></a>`output_attn_res` — [`L255`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L255)
  - <a id="KimiModel.sp_group"></a>`sp_group` — [`L234`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L234)
  - <a id="KimiModel.sp_prefill"></a>`sp_prefill` — [`L224`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L224)
- protocol/private: <a id="KimiModel.__init__"></a>`__init__`[`L210`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L210)
- uses (calls/refs, reference-scoped): [`all_gather`](collective_ops.md#TokenShardCollectives.all_gather), [`AttentionResidual`](layers.md#AttentionResidual), [`TPU_K3_SP_PREFILL`](../../../envs.md#TPU_K3_SP_PREFILL), [`TokenShardCollectives`](collective_ops.md#TokenShardCollectives), [`world_size`](collective_ops.md#TokenShardCollectives.world_size), [`logger`](model.md#logger), [`KimiDecoderLayer`](model.md#KimiDecoderLayer), [`rank_in_group`](collective_ops.md#TokenShardCollectives.rank_in_group)
- used by: [`set_aux_hidden_state_layers`](model.md#KimiLinearForCausalLM.set_aux_hidden_state_layers), [`model`](model.md#KimiLinearForCausalLM.model), [`embed_input_ids`](model.md#KimiLinearForCausalLM.embed_input_ids)

## Functions
- <a id="_tpu_tp_all_gather"></a>`_tpu_tp_all_gather(input_: torch.Tensor, dim: int = -1)` — [`L532`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L532) — Gather a materialized encoder output without leaving the TPU.

## Module values
- <a id="logger"></a>`logger` — [`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/model.py#L87)

