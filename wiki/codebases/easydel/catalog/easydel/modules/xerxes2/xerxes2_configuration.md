---
title: 'Module: easydel/modules/xerxes2/xerxes2_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/xerxes2/xerxes2_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.xerxes2.xerxes2_configuration`/Xerxes2Config#
symbols:
  Xerxes2Config: ''
  Xerxes2Config.hidden_size: hidden_size.
  Xerxes2Config.initializer_range: initializer_range.
  Xerxes2Config._get_rope_config: _get_rope_config().
  Xerxes2Config.layer_types: layer_types.
  Xerxes2Config.num_experts: num_experts.
  Xerxes2Config.rope_scaling: rope_scaling.
  Xerxes2Config.kv_lora_dim: kv_lora_dim.
  Xerxes2Config.q_lora_dim: q_lora_dim.
  Xerxes2Config.num_attention_heads: num_attention_heads.
  Xerxes2Config.qk_nope_head_dim: qk_nope_head_dim.
  Xerxes2Config.qk_rope_head_dim: qk_rope_head_dim.
  Xerxes2Config.moe_intermediate_size: moe_intermediate_size.
  Xerxes2Config.vhead_dim: vhead_dim.
  Xerxes2Config.intermediate_size: intermediate_size.
  Xerxes2Config.rms_norm_eps: rms_norm_eps.
  Xerxes2Config.num_hidden_layers: num_hidden_layers.
  Xerxes2Config.hidden_act: hidden_act.
  Xerxes2Config.num_experts_per_tok: num_experts_per_tok.
  Xerxes2Config.norm_topk_prob: norm_topk_prob.
  Xerxes2Config.mlp_only_layers: mlp_only_layers.
  Xerxes2Config.decoder_sparse_step: decoder_sparse_step.
  Xerxes2Config.vocab_size: vocab_size.
  Xerxes2Config.model_type: model_type.
  Xerxes2Config.__init__: __init__().
  Xerxes2Config.bits: bits.
  Xerxes2Config.scan_layers: scan_layers.
  Xerxes2Config.max_position_embeddings: max_position_embeddings.
  Xerxes2Config.output_router_logits: output_router_logits.
  Xerxes2Config.router_aux_loss_coef: router_aux_loss_coef.
  Xerxes2Config.use_cache: use_cache.
  Xerxes2Config.rope_theta: rope_theta.
  Xerxes2Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/xerxes2/xerxes2_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py)

## Classes
### `Xerxes2Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/xerxes2/xerxes2_configuration.py:24`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L24)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class Xerxes2Config(EasyDeLBaseConfig):`
- members:
  - `_get_rope_config(self)` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L169) — Get RoPE configuration from the instance attributes.
  - `get_partition_rules(self, *args, **kwargs)` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L156) — Returns partition rules for model sharding.
  - `bits` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L115)
  - `decoder_sparse_step` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L122)
  - `hidden_act` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L140)
  - `hidden_size` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L119)
  - `initializer_range` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L130)
  - `intermediate_size` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L120)
  - `kv_lora_dim` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L135)
  - `layer_types` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L144)
  - `max_position_embeddings` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L118)
  - `mlp_only_layers` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L139)
  - `model_type` — [`L77`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L77)
  - `moe_intermediate_size` — [`L121`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L121)
  - `norm_topk_prob` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L125)
  - `num_attention_heads` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L129)
  - `num_experts` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L123)
  - `num_experts_per_tok` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L124)
  - `num_hidden_layers` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L128)
  - `output_router_logits` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L126)
  - `q_lora_dim` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L134)
  - `qk_nope_head_dim` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L137)
  - `qk_rope_head_dim` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L136)
  - `rms_norm_eps` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L131)
  - `rope_scaling` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L143)
  - `rope_theta` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L133)
  - `router_aux_loss_coef` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L127)
  - `scan_layers` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L116)
  - `use_cache` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L132)
  - `vhead_dim` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L138)
  - `vocab_size` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L117)
- protocol/private: `__init__`[`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/xerxes2/xerxes2_configuration.py#L79)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`RopeConfig`](../../layers/rotary/_configs.md#RopeConfig), [`from_dict`](../../layers/rotary/_configs.md#RopeConfig.from_dict), [`original_max_position_embeddings`](../../layers/rotary/_configs.md#RopeConfig.original_max_position_embeddings)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`define_network`](modeling_xerxes2.md#Xerxes2Attention.define_network), [`__init__`](modeling_xerxes2.md#Xerxes2MoeSparseBlock.__init__), [`_get_rope_config`](../../infra/base_config.md#EasyDeLBaseConfig._get_rope_config), [`embed_tokens`](modeling_xerxes2.md#Xerxes2Model.embed_tokens), [`mlp`](modeling_xerxes2.md#Xerxes2DecoderLayer.mlp), [`down_proj`](modeling_xerxes2.md#Xerxes2MoeMLPStack.down_proj), [`gate_proj`](modeling_xerxes2.md#Xerxes2MoeMLPStack.gate_proj), [`up_proj`](modeling_xerxes2.md#Xerxes2MoeMLPStack.up_proj), [`Xerxes2Model`](modeling_xerxes2.md#Xerxes2Model), [`_create_attention_performer`](modeling_xerxes2.md#Xerxes2Attention._create_attention_performer), [`is_moe`](modeling_xerxes2.md#Xerxes2DecoderLayer.is_moe), [`gate`](modeling_xerxes2.md#Xerxes2MoeSparseBlock.gate), [`Xerxes2ForCausalLM`](modeling_xerxes2.md#Xerxes2ForCausalLM), [`norm`](modeling_xerxes2.md#Xerxes2Model.norm), [`q_head_dim`](modeling_xerxes2.md#Xerxes2Attention.q_head_dim), [`__init__`](modeling_xerxes2.md#Xerxes2ForCausalLM.__init__), [`act`](modeling_xerxes2.md#Xerxes2MLP.act), [`kv_lora_rank`](modeling_xerxes2.md#Xerxes2Attention.kv_lora_rank), [`act_fn`](modeling_xerxes2.md#Xerxes2MoeMLPStack.act_fn), [`down_proj`](modeling_xerxes2.md#Xerxes2MLP.down_proj), [`gate_up_proj`](modeling_xerxes2.md#Xerxes2MLP.gate_up_proj), [`__init__`](modeling_xerxes2.md#Xerxes2Model.__init__), [`layers`](modeling_xerxes2.md#Xerxes2Model.layers), [`v_head_dim`](modeling_xerxes2.md#Xerxes2Attention.v_head_dim), [`__init__`](modeling_xerxes2.md#Xerxes2Attention.__init__), [`__init__`](modeling_xerxes2.md#Xerxes2DecoderLayer.__init__), [`__init__`](modeling_xerxes2.md#Xerxes2MLP.__init__), [`__init__`](modeling_xerxes2.md#Xerxes2MoeMLPStack.__init__), [`_config_class`](modeling_xerxes2.md#Xerxes2ForCausalLM._config_class), [`qk_nope_head_dim`](modeling_xerxes2.md#Xerxes2Attention.qk_nope_head_dim), [`qk_rope_head_dim`](modeling_xerxes2.md#Xerxes2Attention.qk_rope_head_dim)

