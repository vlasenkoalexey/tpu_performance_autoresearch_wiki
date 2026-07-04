---
title: 'Module: easydel/modules/deepseek_v2/deepseek_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/deepseek_v2/deepseek_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.deepseek_v2.deepseek_configuration`/DeepseekV2Config#
symbols:
  DeepseekV2Config: ''
  DeepseekV2Config.hidden_size: hidden_size.
  DeepseekV2Config._get_rope_config: _get_rope_config().
  DeepseekV2Config.layer_types: layer_types.
  DeepseekV2Config.n_routed_experts: n_routed_experts.
  DeepseekV2Config.initializer_range: initializer_range.
  DeepseekV2Config.__init__: __init__().
  DeepseekV2Config.rope_scaling: rope_scaling.
  DeepseekV2Config.num_attention_heads: num_attention_heads.
  DeepseekV2Config.kv_lora_rank: kv_lora_rank.
  DeepseekV2Config.q_lora_rank: q_lora_rank.
  DeepseekV2Config.rms_norm_eps: rms_norm_eps.
  DeepseekV2Config.n_shared_experts: n_shared_experts.
  DeepseekV2Config.qk_rope_head_dim: qk_rope_head_dim.
  DeepseekV2Config.qk_nope_head_dim: qk_nope_head_dim.
  DeepseekV2Config.num_experts_per_tok: num_experts_per_tok.
  DeepseekV2Config.attention_bias: attention_bias.
  DeepseekV2Config.__setattr__: __setattr__().
  DeepseekV2Config.granted_freq_max_position_embedding: granted_freq_max_position_embedding().
  DeepseekV2Config.granted_mask_max_position_embedding: granted_mask_max_position_embedding().
  DeepseekV2Config.max_position_embeddings: max_position_embeddings.
  DeepseekV2Config.intermediate_size: intermediate_size.
  DeepseekV2Config.moe_intermediate_size: moe_intermediate_size.
  DeepseekV2Config.routed_scaling_factor: routed_scaling_factor.
  DeepseekV2Config.v_head_dim: v_head_dim.
  DeepseekV2Config.topk_method: topk_method.
  DeepseekV2Config.n_group: n_group.
  DeepseekV2Config.topk_group: topk_group.
  DeepseekV2Config.norm_topk_prob: norm_topk_prob.
  DeepseekV2Config.hidden_act: hidden_act.
  DeepseekV2Config.num_hidden_layers: num_hidden_layers.
  DeepseekV2Config.moe_layer_freq: moe_layer_freq.
  DeepseekV2Config.first_k_dense_replace: first_k_dense_replace.
  DeepseekV2Config.scoring_func: scoring_func.
  DeepseekV2Config.aux_loss_alpha: aux_loss_alpha.
  DeepseekV2Config.seq_aux: seq_aux.
  DeepseekV2Config.gradient_checkpointing: gradient_checkpointing.
  DeepseekV2Config.model_type: model_type.
  DeepseekV2Config.vocab_size: vocab_size.
  DeepseekV2Config.ep_size: ep_size.
  DeepseekV2Config.head_dim: head_dim.
  DeepseekV2Config.num_key_value_heads: num_key_value_heads.
  DeepseekV2Config.pretraining_tp: pretraining_tp.
  DeepseekV2Config.use_cache: use_cache.
  DeepseekV2Config.rope_theta: rope_theta.
  DeepseekV2Config.attention_dropout: attention_dropout.
  DeepseekV2Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/deepseek_v2/deepseek_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py)

## Classes
### `DeepseekV2Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/deepseek_v2/deepseek_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L25)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class DeepseekV2Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 102400, hidden_size: int = 4096, intermediate_size: int = 11008, moe_intermediate_size: int = 1407, num_hidden_layers: int = 30, num_attention_heads: int = 32, num_key_value_heads: int | None = 32, n_shared_experts: int | None = None, n_routed_experts: int | None = None, ep_size: int = 1, routed_scaling_factor: float = 1, kv_lora_rank: int = 512, q_lora_rank: int | None = 1536, qk_rope_head_dim: int = 64, v_head_dim: int = 128, qk_nope_head_dim: int = 128, topk_method: str = "gready", n_group: int | None = None, topk_group: int | None = None, num_experts_per_tok: int | None = None, moe_layer_freq: int = 1, first_k_dense_replace: int = 0, norm_topk_prob: bool = False, scoring_func: str = "softmax", aux_loss_alpha: float = 0.001, seq_aux: bool = True, hidden_act: str = "silu", max_position_embeddings: int = 2048, initializer_range: float = 0.02, rms_norm_eps: float = 0.000001, use_cache: bool = True, pad_token_id: int | None = None, bos_token_id: int = 100000, eos_token_id: int = 100001, pretraining_tp: int = 1, tie_word_embeddings: bool = False, rope_theta: float = 10000, attention_bias: bool = False, attention_dropout: float = 0, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, use_scan_mlp: bool = False, scan_mlp_chunk_size: int = 1024, bits: int | None = None, rope_scaling: dict[str, str | float] | None = None, layer_types: list[str] | None = None, **kwargs)` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L137) — Initialize a new DeepseekV2Config instance.
  - `_get_rope_config(self)` — [`L336`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L336) — Get RoPE configuration from the instance attributes.
  - `get_partition_rules(self, *args, **kwargs)` — [`L297`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L297) — Returns partition rules for model sharding.
  - `granted_freq_max_position_embedding(self)` — [`L311`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L311) — Returns the maximum position embedding size for frequency-based position embeddings.
  - `granted_mask_max_position_embedding(self)` — [`L324`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L324) — Returns the maximum position embedding size for mask-based position embeddings.
  - `attention_bias` — [`L275`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L275)
  - `attention_dropout` — [`L276`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L276)
  - `aux_loss_alpha` — [`L261`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L261)
  - `ep_size` — [`L245`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L245)
  - `first_k_dense_replace` — [`L258`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L258)
  - `gradient_checkpointing` — [`L277`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L277)
  - `head_dim` — [`L252`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L252)
  - `hidden_act` — [`L268`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L268)
  - `hidden_size` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L238)
  - `initializer_range` — [`L269`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L269)
  - `intermediate_size` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L239)
  - `kv_lora_rank` — [`L247`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L247)
  - `layer_types` — [`L278`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L278)
  - `max_position_embeddings` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L237)
  - `model_type` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L125)
  - `moe_intermediate_size` — [`L240`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L240)
  - `moe_layer_freq` — [`L257`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L257)
  - `n_group` — [`L254`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L254)
  - `n_routed_experts` — [`L244`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L244)
  - `n_shared_experts` — [`L243`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L243)
  - `norm_topk_prob` — [`L259`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L259)
  - `num_attention_heads` — [`L242`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L242)
  - `num_experts_per_tok` — [`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L256)
  - `num_hidden_layers` — [`L241`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L241)
  - `num_key_value_heads` — [`L267`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L267)
  - `pretraining_tp` — [`L271`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L271)
  - `q_lora_rank` — [`L248`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L248)
  - `qk_nope_head_dim` — [`L251`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L251)
  - `qk_rope_head_dim` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L249)
  - `rms_norm_eps` — [`L270`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L270)
  - `rope_scaling` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L274)
  - `rope_theta` — [`L273`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L273)
  - `routed_scaling_factor` — [`L246`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L246)
  - `scoring_func` — [`L260`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L260)
  - `seq_aux` — [`L262`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L262)
  - `topk_group` — [`L255`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L255)
  - `topk_method` — [`L253`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L253)
  - `use_cache` — [`L272`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L272)
  - `v_head_dim` — [`L250`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L250)
  - `vocab_size` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L236)
- protocol/private: `__setattr__`[`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/deepseek_v2/deepseek_configuration.py#L127)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`RopeConfig`](../../layers/rotary/_configs.md#RopeConfig), [`__setattr__`](../../infra/base_config.md#EasyDeLBaseConfig.__setattr__), [`from_dict`](../../layers/rotary/_configs.md#RopeConfig.from_dict), [`original_max_position_embeddings`](../../layers/rotary/_configs.md#RopeConfig.original_max_position_embeddings)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`define_network`](modeling_deepseek.md#DeepseekV2Attention.define_network), [`granted_freq_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_freq_max_position_embedding), [`__call__`](modeling_deepseek.md#DeepseekV2MoE.__call__), [`shared_experts`](modeling_deepseek.md#DeepseekV2MoE.shared_experts), [`granted_mask_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_mask_max_position_embedding), [`_get_rope_config`](../../infra/base_config.md#EasyDeLBaseConfig._get_rope_config), [`__init__`](modeling_deepseek.md#DeepseekV2MoE.__init__), [`DeepseekV2ForCausalLM`](modeling_deepseek.md#DeepseekV2ForCausalLM), [`embed_tokens`](modeling_deepseek.md#DeepseekV2Model.embed_tokens), [`DeepseekV2Model`](modeling_deepseek.md#DeepseekV2Model), [`_create_attention_performer`](modeling_deepseek.md#DeepseekV2Attention._create_attention_performer), [`experts`](modeling_deepseek.md#DeepseekV2MoE.experts), [`down_proj`](modeling_deepseek.md#DeepseekV2MLPMoE.down_proj), [`gate_proj`](modeling_deepseek.md#DeepseekV2MLPMoE.gate_proj), [`up_proj`](modeling_deepseek.md#DeepseekV2MLPMoE.up_proj), [`config`](modeling_deepseek.md#DeepseekV2MLP.config), [`gate`](modeling_deepseek.md#DeepseekV2MoE.gate), [`input_layernorm`](modeling_deepseek.md#DeepseekV2DecoderLayer.input_layernorm), [`mlp`](modeling_deepseek.md#DeepseekV2DecoderLayer.mlp), [`post_attention_layernorm`](modeling_deepseek.md#DeepseekV2DecoderLayer.post_attention_layernorm), [`q_head_dim`](modeling_deepseek.md#DeepseekV2Attention.q_head_dim), [`__init__`](modeling_deepseek.md#DeepseekV2ForCausalLM.__init__), [`hidden_size`](modeling_deepseek.md#DeepseekV2DecoderLayer.hidden_size), [`kv_lora_rank`](modeling_deepseek.md#DeepseekV2Attention.kv_lora_rank), [`act_fn`](modeling_deepseek.md#DeepseekV2MLPMoE.act_fn), [`config`](modeling_deepseek.md#DeepseekV2MLPMoE.config), [`act_fn`](modeling_deepseek.md#DeepseekV2MLP.act_fn), [`__init__`](modeling_deepseek.md#DeepseekV2Model.__init__), [`v_head_dim`](modeling_deepseek.md#DeepseekV2Attention.v_head_dim), [`gating_dim`](modeling_deepseek.md#MoEGate.gating_dim), [`n_routed_experts`](modeling_deepseek.md#MoEGate.n_routed_experts), [`__init__`](modeling_deepseek.md#DeepseekV2Attention.__init__), [`__init__`](modeling_deepseek.md#DeepseekV2DecoderLayer.__init__), [`__init__`](modeling_deepseek.md#DeepseekV2MLP.__init__), [`__init__`](modeling_deepseek.md#DeepseekV2MLPMoE.__init__), [`__init__`](modeling_deepseek.md#MoEGate.__init__), [`_config_class`](modeling_deepseek.md#DeepseekV2ForCausalLM._config_class)  (+13 more)

