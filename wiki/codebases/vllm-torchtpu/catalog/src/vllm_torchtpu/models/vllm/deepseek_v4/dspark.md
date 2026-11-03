---
title: 'Module: src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.models.vllm.deepseek_v4.dspark`/
symbols:
  DSparkDeepseekV4Model.forward: DSparkDeepseekV4Model#forward().
  DSparkDeepseekV4Model.layers: DSparkDeepseekV4Model#layers.
  DSparkDeepseekV4ForCausalLM.model: DSparkDeepseekV4ForCausalLM#model.
  DSparkDeepseekV4ForCausalLM.load_weights: DSparkDeepseekV4ForCausalLM#load_weights().
  DSparkDeepseekV4Model.precompute_and_store_context_kv: DSparkDeepseekV4Model#precompute_and_store_context_kv().
  DSparkDeepseekV4ForCausalLM.compute_logits: DSparkDeepseekV4ForCausalLM#compute_logits().
  DSparkDeepseekV4Model.get_draft_kv_cache_layer_names: DSparkDeepseekV4Model#get_draft_kv_cache_layer_names().
  DSparkDeepseekV4Model.confidence_head: DSparkDeepseekV4Model#confidence_head.
  DSparkDeepseekV4ForCausalLM.markov_bias: DSparkDeepseekV4ForCausalLM#markov_bias().
  DSparkDeepseekV4Model.combine_hidden_states: DSparkDeepseekV4Model#combine_hidden_states().
  DSparkDeepseekV4Model.mhc_post_op: DSparkDeepseekV4Model#mhc_post_op.
  DSparkDeepseekV4Model.load_weights: DSparkDeepseekV4Model#load_weights.
  DSparkDeepseekV4Model.get_expert_mapping: DSparkDeepseekV4Model#get_expert_mapping.
  DSparkDeepseekV4ForCausalLM.embed_input_ids: DSparkDeepseekV4ForCausalLM#embed_input_ids().
  DSparkDeepseekV4ForCausalLM.combine_hidden_states: DSparkDeepseekV4ForCausalLM#combine_hidden_states().
  DSparkDeepseekV4ForCausalLM.get_draft_attn_causal: DSparkDeepseekV4ForCausalLM#get_draft_attn_causal().
  DSparkDeepseekV4ForCausalLM.get_draft_kv_cache_layer_names: DSparkDeepseekV4ForCausalLM#get_draft_kv_cache_layer_names().
  DSparkDeepseekV4ForCausalLM.precompute_and_store_context_kv: DSparkDeepseekV4ForCausalLM#precompute_and_store_context_kv().
  DSparkDeepseekV4ForCausalLM.markov_embed: DSparkDeepseekV4ForCausalLM#markov_embed().
  DSparkDeepseekV4ForCausalLM.compute_confidence: DSparkDeepseekV4ForCausalLM#compute_confidence().
  DSparkDeepseekV4Model.embed_input_ids: DSparkDeepseekV4Model#embed_input_ids().
  DSparkDeepseekV4ForCausalLM.logits_processor: DSparkDeepseekV4ForCausalLM#logits_processor.
  DSparkDeepseekV4Model.hc_mult: DSparkDeepseekV4Model#hc_mult.
  logger: logger.
  _rewrite_dspark_name: _rewrite_dspark_name().
  DSparkDeepseekV4Model.main_proj: DSparkDeepseekV4Model#main_proj.
  DSparkDeepseekV4Model.norm: DSparkDeepseekV4Model#norm.
  DSparkDeepseekV4Model.hc_head_fn: DSparkDeepseekV4Model#hc_head_fn.
  DSparkDeepseekV4Model.hc_head_base: DSparkDeepseekV4Model#hc_head_base.
  DSparkDeepseekV4Model.get_draft_attn_causal: DSparkDeepseekV4Model#get_draft_attn_causal().
  DSparkDeepseekV4ForCausalLM._layer_stream: DSparkDeepseekV4ForCausalLM#_layer_stream().
  DSparkDeepseekV4ForCausalLM.forward: DSparkDeepseekV4ForCausalLM#forward().
  DSparkDeepseekV4ForCausalLM.compute_draft_logits: DSparkDeepseekV4ForCausalLM#compute_draft_logits().
  DSparkDeepseekV4Model.embed_tokens: DSparkDeepseekV4Model#embed_tokens.
  DSparkDeepseekV4Model.markov_head: DSparkDeepseekV4Model#markov_head.
  DSparkDeepseekV4ForCausalLM.config: DSparkDeepseekV4ForCausalLM#config.
  DSparkDeepseekV4ForCausalLM.lm_head: DSparkDeepseekV4ForCausalLM#lm_head.
  _remap_dspark_name: _remap_dspark_name().
  _insert_context_kv: _insert_context_kv().
  DSparkDeepseekV4Model: DSparkDeepseekV4Model#
  DSparkDeepseekV4Model.hc_eps: DSparkDeepseekV4Model#hc_eps.
  DSparkDeepseekV4Model.rms_norm_eps: DSparkDeepseekV4Model#rms_norm_eps.
  DSparkDeepseekV4Model.num_hidden_layers: DSparkDeepseekV4Model#num_hidden_layers.
  DSparkDeepseekV4Model.target_layer_ids: DSparkDeepseekV4Model#target_layer_ids.
  DSparkDeepseekV4Model.num_dspark_layers: DSparkDeepseekV4Model#num_dspark_layers.
  DSparkDeepseekV4Model.main_norm: DSparkDeepseekV4Model#main_norm.
  DSparkDeepseekV4Model.topk_indices_buffer: DSparkDeepseekV4Model#topk_indices_buffer.
  DSparkDeepseekV4Model.hc_head_scale: DSparkDeepseekV4Model#hc_head_scale.
  DSparkDeepseekV4Model.__init__: DSparkDeepseekV4Model#__init__().
  DSparkDeepseekV4Model.config: DSparkDeepseekV4Model#config.
  DSparkDeepseekV4ForCausalLM: DSparkDeepseekV4ForCausalLM#
  DSparkDeepseekV4ForCausalLM.has_own_embed_tokens: DSparkDeepseekV4ForCausalLM#has_own_embed_tokens.
  DSparkDeepseekV4ForCausalLM.has_own_lm_head: DSparkDeepseekV4ForCausalLM#has_own_lm_head.
  DSparkDeepseekV4ForCausalLM.owns_context_kv: DSparkDeepseekV4ForCausalLM#owns_context_kv.
  DSparkDeepseekV4ForCausalLM.__init__: DSparkDeepseekV4ForCausalLM#__init__().
  DSparkDeepseekV4ForCausalLM.map_draft_to_target: DSparkDeepseekV4ForCausalLM#map_draft_to_target().
---
# Module: [`src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py)

## Classes
### <a id="DSparkDeepseekV4ForCausalLM"></a>`DSparkDeepseekV4ForCausalLM`
- def: [`src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py:313`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L313)
- doc: Registry entry for `architectures=["DSparkDraftModel"]` on TPU.
- signature: `class DSparkDeepseekV4ForCausalLM(nn.Module):`
- members:
  - <a id="DSparkDeepseekV4ForCausalLM.combine_hidden_states"></a>`combine_hidden_states(self, aux_hidden_states: torch.Tensor)` — [`L340`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L340)
  - <a id="DSparkDeepseekV4ForCausalLM.compute_confidence"></a>`compute_confidence(self, head_hidden: torch.Tensor, markov_embed: torch.Tensor)` — [`L385`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L385) — Per-position acceptance probability of each drafted token, from the
  - <a id="DSparkDeepseekV4ForCausalLM.compute_draft_logits"></a>`compute_draft_logits(self, hidden_states: torch.Tensor)` — [`L372`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L372)
  - <a id="DSparkDeepseekV4ForCausalLM.compute_logits"></a>`compute_logits(self, hidden_states: torch.Tensor)` — [`L367`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L367) — Base logits = lm_head(norm(pre-norm head hidden)).
  - <a id="DSparkDeepseekV4ForCausalLM.embed_input_ids"></a>`embed_input_ids(self, input_ids: torch.Tensor)` — [`L337`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L337)
  - <a id="DSparkDeepseekV4ForCausalLM.forward"></a>`forward(self, input_ids: torch.Tensor, positions: torch.Tensor, inputs_embeds: torch.Tensor | None = None)` — [`L359`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L359)
  - <a id="DSparkDeepseekV4ForCausalLM.get_draft_attn_causal"></a>`get_draft_attn_causal(self)` — [`L343`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L343)
  - <a id="DSparkDeepseekV4ForCausalLM.get_draft_kv_cache_layer_names"></a>`get_draft_kv_cache_layer_names(self)` — [`L346`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L346)
  - <a id="DSparkDeepseekV4ForCausalLM.load_weights"></a>`load_weights(self, weights: Iterable[tuple[str, torch.Tensor]])` — [`L395`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L395) — Load ``mtp.{i}.*`` draft weights from the target checkpoint. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DSparkDeepseekV4ForCausalLM.map_draft_to_target"></a>`map_draft_to_target(self, draft_ids: torch.Tensor)` — [`L376`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L376)
  - <a id="DSparkDeepseekV4ForCausalLM.markov_bias"></a>`markov_bias(self, markov_embed: torch.Tensor)` — [`L382`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L382)
  - <a id="DSparkDeepseekV4ForCausalLM.markov_embed"></a>`markov_embed(self, token_ids: torch.Tensor)` — [`L379`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L379)
  - <a id="DSparkDeepseekV4ForCausalLM.precompute_and_store_context_kv"></a>`precompute_and_store_context_kv(self, hidden_states: torch.Tensor, positions: torch.Tensor, metadata: tuple)` — [`L349`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L349)
  - <a id="DSparkDeepseekV4ForCausalLM.config"></a>`config` — [`L327`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L327)
  - <a id="DSparkDeepseekV4ForCausalLM.has_own_embed_tokens"></a>`has_own_embed_tokens` — [`L318`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L318)
  - <a id="DSparkDeepseekV4ForCausalLM.has_own_lm_head"></a>`has_own_lm_head` — [`L319`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L319)
  - <a id="DSparkDeepseekV4ForCausalLM.lm_head"></a>`lm_head` — [`L332`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L332)
  - <a id="DSparkDeepseekV4ForCausalLM.logits_processor"></a>`logits_processor` — [`L333`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L333)
  - <a id="DSparkDeepseekV4ForCausalLM.model"></a>`model` — [`L328`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L328)
  - <a id="DSparkDeepseekV4ForCausalLM.owns_context_kv"></a>`owns_context_kv` — [`L322`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L322)
- protocol/private: <a id="DSparkDeepseekV4ForCausalLM.__init__"></a>`__init__`[`L324`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L324), <a id="DSparkDeepseekV4ForCausalLM._layer_stream"></a>`_layer_stream`[`L409`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L409)
- uses (calls/refs, reference-scoped): [`precompute_and_store_context_kv`](dspark.md#DSparkDeepseekV4Model.precompute_and_store_context_kv), [`get_draft_kv_cache_layer_names`](dspark.md#DSparkDeepseekV4Model.get_draft_kv_cache_layer_names), [`confidence_head`](dspark.md#DSparkDeepseekV4Model.confidence_head), [`combine_hidden_states`](dspark.md#DSparkDeepseekV4Model.combine_hidden_states), [`load_weights`](dspark.md#DSparkDeepseekV4Model.load_weights), [`embed_input_ids`](dspark.md#DSparkDeepseekV4Model.embed_input_ids), [`_make_deepseek_v4_weights_mapper`](model.md#_make_deepseek_v4_weights_mapper), [`_rewrite_dspark_name`](dspark.md#_rewrite_dspark_name), [`get_draft_attn_causal`](dspark.md#DSparkDeepseekV4Model.get_draft_attn_causal), [`logger`](dspark.md#logger), [`norm`](dspark.md#DSparkDeepseekV4Model.norm), [`markov_head`](dspark.md#DSparkDeepseekV4Model.markov_head), [`DSparkDeepseekV4Model`](dspark.md#DSparkDeepseekV4Model)

### <a id="DSparkDeepseekV4Model"></a>`DSparkDeepseekV4Model`
- def: [`src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py:139`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L139)
- signature: `class DSparkDeepseekV4Model(nn.Module):`
- members:
  - <a id="DSparkDeepseekV4Model.combine_hidden_states"></a>`combine_hidden_states(self, aux_hidden_states: torch.Tensor)` — [`L246`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L246) — main_x = main_norm(main_proj(concat of target aux states)).
  - <a id="DSparkDeepseekV4Model.embed_input_ids"></a>`embed_input_ids(self, input_ids: torch.Tensor)` — [`L242`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L242) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DSparkDeepseekV4Model.forward"></a>`forward(self, input_ids: torch.Tensor, positions: torch.Tensor, inputs_embeds: torch.Tensor | None = None)` — [`L281`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L281) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DSparkDeepseekV4Model.get_draft_attn_causal"></a>`get_draft_attn_causal(self)` — [`L250`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L250)
  - <a id="DSparkDeepseekV4Model.get_draft_kv_cache_layer_names"></a>`get_draft_kv_cache_layer_names(self)` — [`L255`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L255)
  - <a id="DSparkDeepseekV4Model.precompute_and_store_context_kv"></a>`precompute_and_store_context_kv(self, target_hidden_states: torch.Tensor, positions: torch.Tensor, metadata: tuple)` — [`L261`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L261) — Insert the sliding-window context KV for every draft layer. — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DSparkDeepseekV4Model.confidence_head"></a>`confidence_head` — [`L226`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L226)
  - <a id="DSparkDeepseekV4Model.config"></a>`config` — [`L144`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L144)
  - <a id="DSparkDeepseekV4Model.embed_tokens"></a>`embed_tokens` — [`L154`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L154)
  - <a id="DSparkDeepseekV4Model.get_expert_mapping"></a>`get_expert_mapping` — [`L239`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L239)
  - <a id="DSparkDeepseekV4Model.hc_eps"></a>`hc_eps` — [`L146`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L146)
  - <a id="DSparkDeepseekV4Model.hc_head_base"></a>`hc_head_base` — [`L207`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L207)
  - <a id="DSparkDeepseekV4Model.hc_head_fn"></a>`hc_head_fn` — [`L203`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L203)
  - <a id="DSparkDeepseekV4Model.hc_head_scale"></a>`hc_head_scale` — [`L211`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L211)
  - <a id="DSparkDeepseekV4Model.hc_mult"></a>`hc_mult` — [`L145`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L145)
  - <a id="DSparkDeepseekV4Model.layers"></a>`layers` — [`L173`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L173) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DSparkDeepseekV4Model.load_weights"></a>`load_weights` — [`L240`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L240)
  - <a id="DSparkDeepseekV4Model.main_norm"></a>`main_norm` — [`L164`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L164)
  - <a id="DSparkDeepseekV4Model.main_proj"></a>`main_proj` — [`L156`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L156)
  - <a id="DSparkDeepseekV4Model.markov_head"></a>`markov_head` — [`L218`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L218)
  - <a id="DSparkDeepseekV4Model.mhc_post_op"></a>`mhc_post_op` — [`L238`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L238) — documented in [deepseek-v4-model](../../../../../../concepts/deepseek-v4-model.md)
  - <a id="DSparkDeepseekV4Model.norm"></a>`norm` — [`L201`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L201)
  - <a id="DSparkDeepseekV4Model.num_dspark_layers"></a>`num_dspark_layers` — [`L150`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L150)
  - <a id="DSparkDeepseekV4Model.num_hidden_layers"></a>`num_hidden_layers` — [`L148`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L148)
  - <a id="DSparkDeepseekV4Model.rms_norm_eps"></a>`rms_norm_eps` — [`L147`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L147)
  - <a id="DSparkDeepseekV4Model.target_layer_ids"></a>`target_layer_ids` — [`L149`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L149)
  - <a id="DSparkDeepseekV4Model.topk_indices_buffer"></a>`topk_indices_buffer` — [`L166`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L166)
- protocol/private: <a id="DSparkDeepseekV4Model.__init__"></a>`__init__`[`L140`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L140)
- uses (calls/refs, reference-scoped): [`mla_attn`](attention.md#VllmDeepseekV4MLAAttention.mla_attn), [`load_weights`](model.md#DeepseekV4Model.load_weights), [`DeepseekV4DecoderLayer`](model.md#DeepseekV4DecoderLayer), [`attn`](model.md#DeepseekV4DecoderLayer.attn), [`get_expert_mapping`](model.md#DeepseekV4Model.get_expert_mapping), [`mhc_post_op`](model.md#DeepseekV4Model.mhc_post_op), [`DeepseekV4Model`](model.md#DeepseekV4Model), [`mhc_collapse_head`](layers.md#mhc_collapse_head), [`_insert_context_kv`](dspark.md#_insert_context_kv), [`non_causal_multi_token_decode`](attention.md#VllmDeepseekV4MLAAttention.non_causal_multi_token_decode)
- used by: [`load_weights`](dspark.md#DSparkDeepseekV4ForCausalLM.load_weights), [`model`](dspark.md#DSparkDeepseekV4ForCausalLM.model), [`compute_logits`](dspark.md#DSparkDeepseekV4ForCausalLM.compute_logits), [`markov_bias`](dspark.md#DSparkDeepseekV4ForCausalLM.markov_bias), [`combine_hidden_states`](dspark.md#DSparkDeepseekV4ForCausalLM.combine_hidden_states), [`compute_confidence`](dspark.md#DSparkDeepseekV4ForCausalLM.compute_confidence), [`embed_input_ids`](dspark.md#DSparkDeepseekV4ForCausalLM.embed_input_ids), [`get_draft_attn_causal`](dspark.md#DSparkDeepseekV4ForCausalLM.get_draft_attn_causal), [`get_draft_kv_cache_layer_names`](dspark.md#DSparkDeepseekV4ForCausalLM.get_draft_kv_cache_layer_names), [`markov_embed`](dspark.md#DSparkDeepseekV4ForCausalLM.markov_embed), [`precompute_and_store_context_kv`](dspark.md#DSparkDeepseekV4ForCausalLM.precompute_and_store_context_kv)

## Functions
- <a id="_insert_context_kv"></a>`_insert_context_kv(attn, kv: torch.Tensor, positions: torch.Tensor, metadata)` — [`L84`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L84) — Insert the context KV of verified tokens into one draft layer's cache.
- <a id="_remap_dspark_name"></a>`_remap_dspark_name(name: str, keep_confidence_head: bool = False)` — [`L42`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L42) — Map a checkpoint ``mtp.{i}.*`` name to this model's parameter path.
- <a id="_rewrite_dspark_name"></a>`_rewrite_dspark_name(name: str, mapper: WeightsMapper, keep_confidence_head: bool = False)` — [`L67`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L67) — Checkpoint name -> ``DeepseekV4Model`` parameter path.

## Module values
- <a id="logger"></a>`logger` — [`L39`](../../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/models/vllm/deepseek_v4/dspark.py#L39)

