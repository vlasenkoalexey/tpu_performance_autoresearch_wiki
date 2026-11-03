---
title: 'Module: src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.kimi_k3.dspark`/
symbols:
  K3DSparkModel.config: K3DSparkModel#config.
  K3DSparkModel.precompute_and_store_context_kv: K3DSparkModel#precompute_and_store_context_kv().
  K3DSparkForCausalLM.load_weights: K3DSparkForCausalLM#load_weights().
  K3DSparkForCausalLM.model: K3DSparkForCausalLM#model.
  K3DSparkModel.layers: K3DSparkModel#layers.
  K3DSparkDecoderLayer.forward: K3DSparkDecoderLayer#forward().
  K3DSparkForCausalLM.get_draft_kv_cache_layer_names: K3DSparkForCausalLM#get_draft_kv_cache_layer_names().
  K3DSparkModel.forward: K3DSparkModel#forward().
  K3DSparkForCausalLM.markov_bias: K3DSparkForCausalLM#markov_bias().
  K3DSparkModel.combine_hidden_states: K3DSparkModel#combine_hidden_states().
  K3DSparkForCausalLM.compute_draft_logits: K3DSparkForCausalLM#compute_draft_logits().
  K3DSparkDecoderLayer.self_attn: K3DSparkDecoderLayer#self_attn.
  K3DSparkForCausalLM.embed_input_ids: K3DSparkForCausalLM#embed_input_ids().
  K3DSparkForCausalLM.combine_hidden_states: K3DSparkForCausalLM#combine_hidden_states().
  K3DSparkForCausalLM.get_draft_attn_causal: K3DSparkForCausalLM#get_draft_attn_causal().
  K3DSparkForCausalLM.tpu_precompute_and_store_context_kv: K3DSparkForCausalLM#tpu_precompute_and_store_context_kv().
  K3DSparkForCausalLM.markov_embed: K3DSparkForCausalLM#markov_embed().
  K3DSparkModel.markov_head: K3DSparkModel#markov_head.
  K3DSparkModel.embed_input_ids: K3DSparkModel#embed_input_ids().
  K3DSparkForCausalLM.logits_processor: K3DSparkForCausalLM#logits_processor.
  K3DSparkDecoderLayer.mlp: K3DSparkDecoderLayer#mlp.
  K3DSparkModel.context_proj: K3DSparkModel#context_proj.
  K3DSparkModel.context_norm: K3DSparkModel#context_norm.
  K3DSparkModel.context_kv_proj: K3DSparkModel#context_kv_proj.
  K3DSparkModel.final_norm: K3DSparkModel#final_norm.
  K3DSparkModel.get_draft_attn_causal: K3DSparkModel#get_draft_attn_causal().
  K3DSparkForCausalLM.forward: K3DSparkForCausalLM#forward().
  K3DSparkForCausalLM.compute_logits: K3DSparkForCausalLM#compute_logits().
  K3DSparkModel: K3DSparkModel#
  K3DSparkModel.embed_tokens: K3DSparkModel#embed_tokens.
  K3DSparkForCausalLM.config: K3DSparkForCausalLM#config.
  K3DSparkForCausalLM.lm_head: K3DSparkForCausalLM#lm_head.
  _duplicate_context_kv_weights: _duplicate_context_kv_weights().
  K3DSparkDecoderLayer: K3DSparkDecoderLayer#
  K3DSparkDecoderLayer.input_layernorm: K3DSparkDecoderLayer#input_layernorm.
  K3DSparkDecoderLayer.post_attention_layernorm: K3DSparkDecoderLayer#post_attention_layernorm.
  K3DSparkForCausalLM: K3DSparkForCausalLM#
  K3DSparkForCausalLM.hf_to_vllm_mapper: K3DSparkForCausalLM#hf_to_vllm_mapper.
  K3DSparkForCausalLM.filtered_weights: K3DSparkForCausalLM#filtered_weights().
  K3DSparkDecoderLayer.__init__: K3DSparkDecoderLayer#__init__().
  K3DSparkModel.__init__: K3DSparkModel#__init__().
  K3DSparkForCausalLM.has_own_embed_tokens: K3DSparkForCausalLM#has_own_embed_tokens.
  K3DSparkForCausalLM.has_own_lm_head: K3DSparkForCausalLM#has_own_lm_head.
  K3DSparkForCausalLM.draft_id_to_target_id: K3DSparkForCausalLM#draft_id_to_target_id.
  K3DSparkForCausalLM.__init__: K3DSparkForCausalLM#__init__().
  K3DSparkForCausalLM.map_draft_to_target: K3DSparkForCausalLM#map_draft_to_target().
---
# Module: [`src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py)

## Classes
### <a id="K3DSparkDecoderLayer"></a>`K3DSparkDecoderLayer`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py:72`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L72)
- signature: `class K3DSparkDecoderLayer(nn.Module):`
- members:
  - <a id="K3DSparkDecoderLayer.forward"></a>`forward(self, positions: torch.Tensor, hidden_states: torch.Tensor)` — [`L102`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L102)
  - <a id="K3DSparkDecoderLayer.input_layernorm"></a>`input_layernorm` — [`L99`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L99)
  - <a id="K3DSparkDecoderLayer.mlp"></a>`mlp` — [`L92`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L92)
  - <a id="K3DSparkDecoderLayer.post_attention_layernorm"></a>`post_attention_layernorm` — [`L100`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L100)
  - <a id="K3DSparkDecoderLayer.self_attn"></a>`self_attn` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L84)
- protocol/private: <a id="K3DSparkDecoderLayer.__init__"></a>`__init__`[`L73`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L73)
- uses (calls/refs, reference-scoped): [`KimiMLP`](layers.md#KimiMLP), [`MultiHeadLatentAttention`](attention.md#MultiHeadLatentAttention)
- used by: [`precompute_and_store_context_kv`](dspark.md#K3DSparkModel.precompute_and_store_context_kv), [`layers`](dspark.md#K3DSparkModel.layers), [`get_draft_kv_cache_layer_names`](dspark.md#K3DSparkForCausalLM.get_draft_kv_cache_layer_names)

### <a id="K3DSparkForCausalLM"></a>`K3DSparkForCausalLM`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py:258`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L258)
- doc: vLLM model-registry entry used by `architectures=K3DSparkModel`.
- signature: `class K3DSparkForCausalLM(nn.Module):`
- members:
  - <a id="K3DSparkForCausalLM.combine_hidden_states"></a>`combine_hidden_states(self, hidden_states: torch.Tensor)` — [`L295`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L295)
  - <a id="K3DSparkForCausalLM.compute_draft_logits"></a>`compute_draft_logits(self, hidden_states: torch.Tensor)` — [`L323`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L323)
  - <a id="K3DSparkForCausalLM.compute_logits"></a>`compute_logits(self, hidden_states: torch.Tensor)` — [`L327`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L327)
  - <a id="K3DSparkForCausalLM.embed_input_ids"></a>`embed_input_ids(self, input_ids: torch.Tensor)` — [`L292`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L292)
  - <a id="K3DSparkForCausalLM.filtered_weights"></a>`filtered_weights()` — [`L343`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L343)
  - <a id="K3DSparkForCausalLM.forward"></a>`forward(self, input_ids: torch.Tensor, positions: torch.Tensor, inputs_embeds: torch.Tensor | None = None)` — [`L315`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L315)
  - <a id="K3DSparkForCausalLM.get_draft_attn_causal"></a>`get_draft_attn_causal(self)` — [`L298`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L298)
  - <a id="K3DSparkForCausalLM.get_draft_kv_cache_layer_names"></a>`get_draft_kv_cache_layer_names(self)` — [`L301`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L301)
  - <a id="K3DSparkForCausalLM.load_weights"></a>`load_weights(self, weights: Iterable[tuple[str, torch.Tensor]])` — [`L339`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L339)
  - <a id="K3DSparkForCausalLM.map_draft_to_target"></a>`map_draft_to_target(self, draft_ids: torch.Tensor)` — [`L330`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L330)
  - <a id="K3DSparkForCausalLM.markov_bias"></a>`markov_bias(self, markov_embed: torch.Tensor)` — [`L336`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L336)
  - <a id="K3DSparkForCausalLM.markov_embed"></a>`markov_embed(self, token_ids: torch.Tensor)` — [`L333`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L333)
  - <a id="K3DSparkForCausalLM.tpu_precompute_and_store_context_kv"></a>`tpu_precompute_and_store_context_kv(self, hidden_states: torch.Tensor, positions: torch.Tensor, metadata: tuple)` — [`L305`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L305)
  - <a id="K3DSparkForCausalLM.config"></a>`config` — [`L277`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L277)
  - <a id="K3DSparkForCausalLM.draft_id_to_target_id"></a>`draft_id_to_target_id` — [`L263`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L263)
  - <a id="K3DSparkForCausalLM.has_own_embed_tokens"></a>`has_own_embed_tokens` — [`L261`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L261)
  - <a id="K3DSparkForCausalLM.has_own_lm_head"></a>`has_own_lm_head` — [`L262`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L262)
  - <a id="K3DSparkForCausalLM.hf_to_vllm_mapper"></a>`hf_to_vllm_mapper` — [`L264`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L264)
  - <a id="K3DSparkForCausalLM.lm_head"></a>`lm_head` — [`L286`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L286)
  - <a id="K3DSparkForCausalLM.logits_processor"></a>`logits_processor` — [`L287`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L287)
  - <a id="K3DSparkForCausalLM.model"></a>`model` — [`L281`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L281)
- protocol/private: <a id="K3DSparkForCausalLM.__init__"></a>`__init__`[`L274`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L274)
- uses (calls/refs, reference-scoped): [`mla_attn`](attention.md#MultiHeadLatentAttention.mla_attn), [`precompute_and_store_context_kv`](dspark.md#K3DSparkModel.precompute_and_store_context_kv), [`layers`](dspark.md#K3DSparkModel.layers), [`combine_hidden_states`](dspark.md#K3DSparkModel.combine_hidden_states), [`self_attn`](dspark.md#K3DSparkDecoderLayer.self_attn), [`embed_input_ids`](dspark.md#K3DSparkModel.embed_input_ids), [`markov_head`](dspark.md#K3DSparkModel.markov_head), [`get_draft_attn_causal`](dspark.md#K3DSparkModel.get_draft_attn_causal), [`K3DSparkModel`](dspark.md#K3DSparkModel), [`_duplicate_context_kv_weights`](dspark.md#_duplicate_context_kv_weights)

### <a id="K3DSparkModel"></a>`K3DSparkModel`
- def: [`src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py:116`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L116)
- signature: `class K3DSparkModel(nn.Module):`
- members:
  - <a id="K3DSparkModel.combine_hidden_states"></a>`combine_hidden_states(self, hidden_states: torch.Tensor)` — [`L173`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L173)
  - <a id="K3DSparkModel.embed_input_ids"></a>`embed_input_ids(self, input_ids: torch.Tensor)` — [`L169`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L169)
  - <a id="K3DSparkModel.forward"></a>`forward(self, input_ids: torch.Tensor, positions: torch.Tensor, inputs_embeds: torch.Tensor | None = None)` — [`L244`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L244)
  - <a id="K3DSparkModel.get_draft_attn_causal"></a>`get_draft_attn_causal(self)` — [`L177`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L177)
  - <a id="K3DSparkModel.precompute_and_store_context_kv"></a>`precompute_and_store_context_kv(self, target_hidden_states: torch.Tensor, positions: torch.Tensor, metadata: tuple)` — [`L180`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L180) — Project target aux states and insert five latent context caches. — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="K3DSparkModel.config"></a>`config` — [`L126`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L126) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="K3DSparkModel.context_kv_proj"></a>`context_kv_proj` — [`L153`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L153)
  - <a id="K3DSparkModel.context_norm"></a>`context_norm` — [`L138`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L138)
  - <a id="K3DSparkModel.context_proj"></a>`context_proj` — [`L131`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L131)
  - <a id="K3DSparkModel.embed_tokens"></a>`embed_tokens` — [`L130`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L130)
  - <a id="K3DSparkModel.final_norm"></a>`final_norm` — [`L161`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L161)
  - <a id="K3DSparkModel.layers"></a>`layers` — [`L139`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L139) — documented in [kimi-k3-model](../../../../../../concepts/kimi-k3-model.md)
  - <a id="K3DSparkModel.markov_head"></a>`markov_head` — [`L162`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L162)
- protocol/private: <a id="K3DSparkModel.__init__"></a>`__init__`[`L117`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L117)
- uses (calls/refs, reference-scoped): [`mla_attn`](attention.md#MultiHeadLatentAttention.mla_attn), [`quantize_kv`](../../../layers/core/quantization.md#quantize_kv), [`self_attn`](dspark.md#K3DSparkDecoderLayer.self_attn), [`mla_op`](../../../layers/adapter/custom_ops/mla_attention_op.md#VllmTPUMLAAttention.mla_op), [`K3DSparkDecoderLayer`](dspark.md#K3DSparkDecoderLayer)
- used by: [`load_weights`](dspark.md#K3DSparkForCausalLM.load_weights), [`model`](dspark.md#K3DSparkForCausalLM.model), [`get_draft_kv_cache_layer_names`](dspark.md#K3DSparkForCausalLM.get_draft_kv_cache_layer_names), [`markov_bias`](dspark.md#K3DSparkForCausalLM.markov_bias), [`combine_hidden_states`](dspark.md#K3DSparkForCausalLM.combine_hidden_states), [`embed_input_ids`](dspark.md#K3DSparkForCausalLM.embed_input_ids), [`get_draft_attn_causal`](dspark.md#K3DSparkForCausalLM.get_draft_attn_causal), [`markov_embed`](dspark.md#K3DSparkForCausalLM.markov_embed), [`tpu_precompute_and_store_context_kv`](dspark.md#K3DSparkForCausalLM.tpu_precompute_and_store_context_kv)

## Functions
- <a id="_duplicate_context_kv_weights"></a>`_duplicate_context_kv_weights(weights: Iterable[tuple[str, torch.Tensor]], num_layers: int)` — [`L49`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/kimi_k3/dspark.py#L49) — Also load every layer's KV-A projection into one fused projection.

