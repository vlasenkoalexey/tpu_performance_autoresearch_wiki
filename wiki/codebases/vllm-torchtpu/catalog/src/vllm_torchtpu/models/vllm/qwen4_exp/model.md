---
title: 'Module: src/vllm_torchtpu/models/vllm/qwen4_exp/model.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/qwen4_exp/model.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.qwen4_exp.model`/
symbols:
  Qwen4ExpDecoderLayer.forward: Qwen4ExpDecoderLayer#forward().
  Qwen4ExpModel.forward: Qwen4ExpModel#forward().
  Qwen4ExpDecoderLayer.ple: Qwen4ExpDecoderLayer#ple.
  Qwen4ExpForCausalLM.embed_input_ids: Qwen4ExpForCausalLM#embed_input_ids().
  Qwen4ExpForCausalLM.compute_logits: Qwen4ExpForCausalLM#compute_logits().
  Qwen4ExpForCausalLM.load_weights: Qwen4ExpForCausalLM#load_weights().
  Qwen4ExpModel.embed_input_ids: Qwen4ExpModel#embed_input_ids().
  Qwen4ExpForCausalLM.model: Qwen4ExpForCausalLM#model.
  Qwen4ExpDecoderLayer.layer_type: Qwen4ExpDecoderLayer#layer_type.
  Qwen4ExpDecoderLayer.linear_attn: Qwen4ExpDecoderLayer#linear_attn.
  Qwen4ExpDecoderLayer.self_attn: Qwen4ExpDecoderLayer#self_attn.
  Qwen4ExpDecoderLayer.mlp: Qwen4ExpDecoderLayer#mlp.
  Qwen4ExpModel.layers: Qwen4ExpModel#layers.
  Qwen4ExpModel.hyper_connection_mixer: Qwen4ExpModel#hyper_connection_mixer.
  Qwen4ExpForCausalLM.forward: Qwen4ExpForCausalLM#forward().
  _hc_config: _hc_config().
  Qwen4ExpDecoderLayer.attn_hyper_connection: Qwen4ExpDecoderLayer#attn_hyper_connection.
  Qwen4ExpDecoderLayer.mlp_hyper_connection: Qwen4ExpDecoderLayer#mlp_hyper_connection.
  Qwen4ExpDecoderLayer: Qwen4ExpDecoderLayer#
  Qwen4ExpModel: Qwen4ExpModel#
  Qwen4ExpModel.hc_count: Qwen4ExpModel#hc_count.
  Qwen4ExpModel.embed_tokens: Qwen4ExpModel#embed_tokens.
  Qwen4ExpForCausalLM.hf_to_vllm_mapper: Qwen4ExpForCausalLM#hf_to_vllm_mapper.
  Qwen4ExpForCausalLM.lm_head: Qwen4ExpForCausalLM#lm_head.
  Qwen4ExpForCausalLM.logits_processor: Qwen4ExpForCausalLM#logits_processor.
  Qwen4ExpDecoderLayer.__init__: Qwen4ExpDecoderLayer#__init__().
  Qwen4ExpModel.__init__: Qwen4ExpModel#__init__().
  Qwen4ExpForCausalLM: Qwen4ExpForCausalLM#
  Qwen4ExpForCausalLM.packed_modules_mapping: Qwen4ExpForCausalLM#packed_modules_mapping.
  Qwen4ExpForCausalLM.__init__: Qwen4ExpForCausalLM#__init__().
  Qwen4ExpForCausalLM.get_mamba_state_dtype_from_config: Qwen4ExpForCausalLM#get_mamba_state_dtype_from_config().
  Qwen4ExpForCausalLM.get_mamba_state_shape_from_config: Qwen4ExpForCausalLM#get_mamba_state_shape_from_config().
  Qwen4ExpForCausalLM.get_mamba_state_copy_func: Qwen4ExpForCausalLM#get_mamba_state_copy_func().
---
# Module: [`src/vllm_torchtpu/models/vllm/qwen4_exp/model.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py)

## Classes
### <a id="Qwen4ExpDecoderLayer"></a>`Qwen4ExpDecoderLayer`
- def: [`src/vllm_torchtpu/models/vllm/qwen4_exp/model.py:80`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L80)
- doc: Attention and MoE sublayers, each wrapped by a gated hyper-connection.
- signature: `class Qwen4ExpDecoderLayer(nn.Module):`
- members:
  - <a id="Qwen4ExpDecoderLayer.forward"></a>`forward(self, positions: torch.Tensor, hidden_states: torch.Tensor)` — [`L137`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L137)
  - <a id="Qwen4ExpDecoderLayer.attn_hyper_connection"></a>`attn_hyper_connection` — [`L134`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L134)
  - <a id="Qwen4ExpDecoderLayer.layer_type"></a>`layer_type` — [`L93`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L93)
  - <a id="Qwen4ExpDecoderLayer.linear_attn"></a>`linear_attn` — [`L113`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L113)
  - <a id="Qwen4ExpDecoderLayer.mlp"></a>`mlp` — [`L132`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L132)
  - <a id="Qwen4ExpDecoderLayer.mlp_hyper_connection"></a>`mlp_hyper_connection` — [`L135`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L135)
  - <a id="Qwen4ExpDecoderLayer.ple"></a>`ple` — [`L98`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L98)
  - <a id="Qwen4ExpDecoderLayer.self_attn"></a>`self_attn` — [`L122`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L122)
- protocol/private: <a id="Qwen4ExpDecoderLayer.__init__"></a>`__init__`[`L87`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L87)
- uses (calls/refs, reference-scoped): [`Qwen4ExpPLELayer`](ple.md#Qwen4ExpPLELayer), [`_hc_config`](model.md#_hc_config)
- used by: [`layers`](model.md#Qwen4ExpModel.layers)

### <a id="Qwen4ExpForCausalLM"></a>`Qwen4ExpForCausalLM`
- def: [`src/vllm_torchtpu/models/vllm/qwen4_exp/model.py:208`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L208)
- doc: Text-only Qwen4Exp on TPU, also used for the vision-language arch.
- signature: `class Qwen4ExpForCausalLM(nn.Module, HasInnerState, IsHybrid):`
- members:
  - <a id="Qwen4ExpForCausalLM.compute_logits"></a>`compute_logits(self, hidden_states: torch.Tensor)` — [`L262`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L262)
  - <a id="Qwen4ExpForCausalLM.embed_input_ids"></a>`embed_input_ids(self, input_ids: torch.Tensor)` — [`L248`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L248)
  - <a id="Qwen4ExpForCausalLM.forward"></a>`forward(self, input_ids: torch.Tensor | None, positions: torch.Tensor, intermediate_tensors: object | None = None, inputs_embeds: torch.Tensor | None = None)` — [`L251`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L251)
  - <a id="Qwen4ExpForCausalLM.get_mamba_state_copy_func"></a>`get_mamba_state_copy_func(cls)` — [`L290`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L290)
  - <a id="Qwen4ExpForCausalLM.get_mamba_state_dtype_from_config"></a>`get_mamba_state_dtype_from_config(cls, vllm_config: VllmConfig)` — [`L266`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L266)
  - <a id="Qwen4ExpForCausalLM.get_mamba_state_shape_from_config"></a>`get_mamba_state_shape_from_config(cls, vllm_config: VllmConfig)` — [`L276`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L276)
  - <a id="Qwen4ExpForCausalLM.load_weights"></a>`load_weights(self, weights: Iterable[tuple[str, torch.Tensor]])` — [`L295`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L295)
  - <a id="Qwen4ExpForCausalLM.hf_to_vllm_mapper"></a>`hf_to_vllm_mapper` — [`L219`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L219)
  - <a id="Qwen4ExpForCausalLM.lm_head"></a>`lm_head` — [`L241`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L241)
  - <a id="Qwen4ExpForCausalLM.logits_processor"></a>`logits_processor` — [`L246`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L246)
  - <a id="Qwen4ExpForCausalLM.model"></a>`model` — [`L238`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L238)
  - <a id="Qwen4ExpForCausalLM.packed_modules_mapping"></a>`packed_modules_mapping` — [`L211`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L211)
- protocol/private: <a id="Qwen4ExpForCausalLM.__init__"></a>`__init__`[`L235`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L235)
- uses (calls/refs, reference-scoped): [`embed_input_ids`](model.md#Qwen4ExpModel.embed_input_ids), [`Qwen4ExpPLELayer`](ple.md#Qwen4ExpPLELayer), [`Qwen4ExpModel`](model.md#Qwen4ExpModel)

### <a id="Qwen4ExpModel"></a>`Qwen4ExpModel`
- def: [`src/vllm_torchtpu/models/vllm/qwen4_exp/model.py:169`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L169)
- signature: `class Qwen4ExpModel(nn.Module):`
- members:
  - <a id="Qwen4ExpModel.embed_input_ids"></a>`embed_input_ids(self, input_ids: torch.Tensor)` — [`L189`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L189)
  - <a id="Qwen4ExpModel.forward"></a>`forward(self, input_ids: torch.Tensor | None, positions: torch.Tensor, inputs_embeds: torch.Tensor | None = None)` — [`L192`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L192)
  - <a id="Qwen4ExpModel.embed_tokens"></a>`embed_tokens` — [`L174`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L174)
  - <a id="Qwen4ExpModel.hc_count"></a>`hc_count` — [`L173`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L173)
  - <a id="Qwen4ExpModel.hyper_connection_mixer"></a>`hyper_connection_mixer` — [`L185`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L185)
  - <a id="Qwen4ExpModel.layers"></a>`layers` — [`L179`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L179)
- protocol/private: <a id="Qwen4ExpModel.__init__"></a>`__init__`[`L170`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L170)
- uses (calls/refs, reference-scoped): [`_hc_config`](model.md#_hc_config), [`Qwen4ExpDecoderLayer`](model.md#Qwen4ExpDecoderLayer)
- used by: [`embed_input_ids`](model.md#Qwen4ExpForCausalLM.embed_input_ids), [`model`](model.md#Qwen4ExpForCausalLM.model)

## Functions
- <a id="_hc_config"></a>`_hc_config(vllm_config: VllmConfig)` — [`L66`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/qwen4_exp/model.py#L66)

