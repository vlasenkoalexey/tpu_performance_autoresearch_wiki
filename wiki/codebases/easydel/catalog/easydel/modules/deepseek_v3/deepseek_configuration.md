---
title: 'Module: easydel/modules/deepseek_v3/deepseek_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/deepseek_v3/deepseek_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.deepseek_v3.deepseek_configuration`/D
symbols:
  DeepseekV3Config: eepseekV3Config#
  DeepseekV3Config.hidden_size: eepseekV3Config#hidden_size.
  DeepseekV3Config._get_rope_config: eepseekV3Config#_get_rope_config().
  DeepseekV3Config.layer_types: eepseekV3Config#layer_types.
  DeepseekV3Config.n_routed_experts: eepseekV3Config#n_routed_experts.
  DeepseekV3Config.initializer_range: eepseekV3Config#initializer_range.
  DeepseekV3Config.rope_scaling: eepseekV3Config#rope_scaling.
  DeepseekV3Config.num_attention_heads: eepseekV3Config#num_attention_heads.
  DeepseekV3Config.kv_lora_rank: eepseekV3Config#kv_lora_rank.
  DeepseekV3Config.q_lora_rank: eepseekV3Config#q_lora_rank.
  DeepseekV3Config.rms_norm_eps: eepseekV3Config#rms_norm_eps.
  DeepseekV3Config.n_shared_experts: eepseekV3Config#n_shared_experts.
  DeepseekV3Config.qk_rope_head_dim: eepseekV3Config#qk_rope_head_dim.
  DeepseekV3Config.qk_nope_head_dim: eepseekV3Config#qk_nope_head_dim.
  DeepseekV3Config.num_experts_per_tok: eepseekV3Config#num_experts_per_tok.
  DeepseekV3Config.attention_bias: eepseekV3Config#attention_bias.
  DEEPSEEK_PRETRAINED_CONFIG_ARCHIVE_MAP: EEPSEEK_PRETRAINED_CONFIG_ARCHIVE_MAP.
  DeepseekV3Config.__setattr__: eepseekV3Config#__setattr__().
  DeepseekV3Config.intermediate_size: eepseekV3Config#intermediate_size.
  DeepseekV3Config.moe_intermediate_size: eepseekV3Config#moe_intermediate_size.
  DeepseekV3Config.v_head_dim: eepseekV3Config#v_head_dim.
  DeepseekV3Config.hidden_act: eepseekV3Config#hidden_act.
  DeepseekV3Config.num_hidden_layers: eepseekV3Config#num_hidden_layers.
  DeepseekV3Config.routed_scaling_factor: eepseekV3Config#routed_scaling_factor.
  DeepseekV3Config.topk_method: eepseekV3Config#topk_method.
  DeepseekV3Config.n_group: eepseekV3Config#n_group.
  DeepseekV3Config.topk_group: eepseekV3Config#topk_group.
  DeepseekV3Config.moe_layer_freq: eepseekV3Config#moe_layer_freq.
  DeepseekV3Config.first_k_dense_replace: eepseekV3Config#first_k_dense_replace.
  DeepseekV3Config.norm_topk_prob: eepseekV3Config#norm_topk_prob.
  DeepseekV3Config.scoring_func: eepseekV3Config#scoring_func.
  DeepseekV3Config.seq_aux: eepseekV3Config#seq_aux.
  DeepseekV3Config.model_type: eepseekV3Config#model_type.
  DeepseekV3Config.keys_to_ignore_at_inference: eepseekV3Config#keys_to_ignore_at_inference.
  DeepseekV3Config.__init__: eepseekV3Config#__init__().
  DeepseekV3Config.vocab_size: eepseekV3Config#vocab_size.
  DeepseekV3Config.max_position_embeddings: eepseekV3Config#max_position_embeddings.
  DeepseekV3Config.num_nextn_predict_layers: eepseekV3Config#num_nextn_predict_layers.
  DeepseekV3Config.ep_size: eepseekV3Config#ep_size.
  DeepseekV3Config.head_dim: eepseekV3Config#head_dim.
  DeepseekV3Config.aux_loss_alpha: eepseekV3Config#aux_loss_alpha.
  DeepseekV3Config.num_key_value_heads: eepseekV3Config#num_key_value_heads.
  DeepseekV3Config.pretraining_tp: eepseekV3Config#pretraining_tp.
  DeepseekV3Config.use_cache: eepseekV3Config#use_cache.
  DeepseekV3Config.rope_theta: eepseekV3Config#rope_theta.
  DeepseekV3Config.attention_dropout: eepseekV3Config#attention_dropout.
  DeepseekV3Config.get_partition_rules: eepseekV3Config#get_partition_rules().
---
# Module: [`easydel/modules/deepseek_v3/deepseek_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py)

## Classes
### `DeepseekV3Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/deepseek_v3/deepseek_configuration.py:28`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L28)
- doc: This is the configuration class to store the configuration of a \[`DeepseekV3Model`\]. It is used to
- signature: `class DeepseekV3Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 129280, hidden_size: int = 7168, intermediate_size: int = 18432, moe_intermediate_size: int = 2048, num_hidden_layers: int = 61, num_nextn_predict_layers: int = 1, num_attention_heads: int = 128, num_key_value_heads: int | None = 128, n_shared_experts: int | None = 1, n_routed_experts: int | None = 256, ep_size: int = 1, routed_scaling_factor: float = 2.5, kv_lora_rank: int = 512, q_lora_rank: int | None = 1536, qk_rope_head_dim: int = 64, v_head_dim: int = 128, qk_nope_head_dim: int = 128, topk_method: str = "noaux_tc", n_group: int = 8, topk_group: int = 4, num_experts_per_tok: int = 8, moe_layer_freq: int = 1, first_k_dense_replace: int = 3, norm_topk_prob: bool = True, scoring_func: str = "sigmoid", aux_loss_alpha: float = 0.001, seq_aux: bool = True, hidden_act: str = "silu", max_position_embeddings: int = 4096, initializer_range: float = 0.02, rms_norm_eps: float = 0.000001, use_cache: bool = True, pad_token_id: int | None = None, bos_token_id: int = 0, eos_token_id: int = 1, pretraining_tp: int = 1, tie_word_embeddings: bool = False, rope_theta: float = 10000, rope_scaling: dict | None = None, attention_bias: bool = False, attention_dropout: float = 0, layer_types: list[str] | None = None, **kwargs)` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L143) — Initialize a new DeepseekV3Config instance.
  - `_get_rope_config(self)` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L307) — Get RoPE configuration from the instance attributes.
  - `get_partition_rules(self, *args, **kwargs)` — [`L294`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L294) — Returns partition rules for model sharding.
  - `attention_bias` — [`L275`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L275)
  - `attention_dropout` — [`L276`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L276)
  - `aux_loss_alpha` — [`L261`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L261)
  - `ep_size` — [`L245`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L245)
  - `first_k_dense_replace` — [`L258`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L258)
  - `head_dim` — [`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L252)
  - `hidden_act` — [`L268`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L268)
  - `hidden_size` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L237)
  - `initializer_range` — [`L269`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L269)
  - `intermediate_size` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L238)
  - `keys_to_ignore_at_inference` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L131)
  - `kv_lora_rank` — [`L247`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L247)
  - `layer_types` — [`L277`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L277)
  - `max_position_embeddings` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L236)
  - `model_type` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L130)
  - `moe_intermediate_size` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L239)
  - `moe_layer_freq` — [`L257`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L257)
  - `n_group` — [`L254`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L254)
  - `n_routed_experts` — [`L244`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L244)
  - `n_shared_experts` — [`L243`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L243)
  - `norm_topk_prob` — [`L259`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L259)
  - `num_attention_heads` — [`L242`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L242)
  - `num_experts_per_tok` — [`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L256)
  - `num_hidden_layers` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L240)
  - `num_key_value_heads` — [`L267`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L267)
  - `num_nextn_predict_layers` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L241)
  - `pretraining_tp` — [`L271`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L271)
  - `q_lora_rank` — [`L248`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L248)
  - `qk_nope_head_dim` — [`L251`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L251)
  - `qk_rope_head_dim` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L249)
  - `rms_norm_eps` — [`L270`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L270)
  - `rope_scaling` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L274)
  - `rope_theta` — [`L273`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L273)
  - `routed_scaling_factor` — [`L246`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L246)
  - `scoring_func` — [`L260`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L260)
  - `seq_aux` — [`L262`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L262)
  - `topk_group` — [`L255`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L255)
  - `topk_method` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L253)
  - `use_cache` — [`L272`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L272)
  - `v_head_dim` — [`L250`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L250)
  - `vocab_size` — [`L235`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L235)
- protocol/private: `__setattr__`[`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L133)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`RopeConfig`](../../layers/rotary/_configs.md#RopeConfig), [`__setattr__`](../../infra/base_config.md#EasyDeLBaseConfig.__setattr__), [`from_dict`](../../layers/rotary/_configs.md#RopeConfig.from_dict), [`original_max_position_embeddings`](../../layers/rotary/_configs.md#RopeConfig.original_max_position_embeddings)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`define_network`](modeling_deepseek.md#DeepseekV3Attention.define_network), [`__call__`](modeling_deepseek.md#DeepseekV3MoE.__call__), [`_get_rope_config`](../../infra/base_config.md#EasyDeLBaseConfig._get_rope_config), [`__init__`](modeling_deepseek.md#DeepseekV3MoE.__init__), [`DeepseekV3ForCausalLM`](modeling_deepseek.md#DeepseekV3ForCausalLM), [`DeepseekV3Model`](modeling_deepseek.md#DeepseekV3Model), [`_create_attention_performer`](modeling_deepseek.md#DeepseekV3Attention._create_attention_performer), [`experts`](modeling_deepseek.md#DeepseekV3MoE.experts), [`down_proj`](modeling_deepseek.md#DeepseekV3MLPMoE.down_proj), [`gate_proj`](modeling_deepseek.md#DeepseekV3MLPMoE.gate_proj), [`up_proj`](modeling_deepseek.md#DeepseekV3MLPMoE.up_proj), [`gating_dim`](modeling_deepseek.md#MoEGate.gating_dim), [`intermediate_size`](modeling_deepseek.md#DeepseekV3MLP.intermediate_size), [`n_routed_experts`](modeling_deepseek.md#MoEGate.n_routed_experts), [`gate`](modeling_deepseek.md#DeepseekV3MoE.gate), [`input_layernorm`](modeling_deepseek.md#DeepseekV3DecoderLayer.input_layernorm), [`mlp`](modeling_deepseek.md#DeepseekV3DecoderLayer.mlp), [`post_attention_layernorm`](modeling_deepseek.md#DeepseekV3DecoderLayer.post_attention_layernorm), [`q_head_dim`](modeling_deepseek.md#DeepseekV3Attention.q_head_dim), [`topk_method`](modeling_deepseek.md#MoEGate.topk_method), [`__init__`](modeling_deepseek.md#DeepseekV3ForCausalLM.__init__), [`hidden_size`](modeling_deepseek.md#DeepseekV3DecoderLayer.hidden_size), [`kv_lora_rank`](modeling_deepseek.md#DeepseekV3Attention.kv_lora_rank), [`act_fn`](modeling_deepseek.md#DeepseekV3MLPMoE.act_fn), [`n_group`](modeling_deepseek.md#MoEGate.n_group), [`scoring_func`](modeling_deepseek.md#MoEGate.scoring_func), [`top_k`](modeling_deepseek.md#MoEGate.top_k), [`act_fn`](modeling_deepseek.md#DeepseekV3MLP.act_fn), [`linear_2`](../kimi_vl/modeling_kimi_vl.md#KimiVLMultiModalProjector.linear_2), [`norm_topk_prob`](modeling_deepseek.md#MoEGate.norm_topk_prob), [`routed_scaling_factor`](modeling_deepseek.md#MoEGate.routed_scaling_factor), [`topk_group`](modeling_deepseek.md#MoEGate.topk_group), [`hidden_size`](modeling_deepseek.md#DeepseekV3MLP.hidden_size), [`__init__`](modeling_deepseek.md#DeepseekV3Model.__init__), [`__init__`](../kimi_vl/kimi_vl_configuration.md#KimiVLConfig.__init__), [`get_text_config`](../kimi_vl/kimi_vl_configuration.md#KimiVLConfig.get_text_config), [`precision`](modeling_deepseek.md#DeepseekV3MLPMoE.precision)  (+13 more)

## Module values
- `DEEPSEEK_PRETRAINED_CONFIG_ARCHIVE_MAP` — [`L24`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v3/deepseek_configuration.py#L24)

