---
title: 'Module: easydel/modules/qwen2_moe/qwen2_moe_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen2_moe/qwen2_moe_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen2_moe.qwen2_moe_configuration`/Qwen2MoeConfig#
symbols:
  Qwen2MoeConfig: ''
  Qwen2MoeConfig.get_mask_details: get_mask_details().
  Qwen2MoeConfig.layer_types: layer_types.
  Qwen2MoeConfig.hidden_size: hidden_size.
  Qwen2MoeConfig.num_experts: num_experts.
  Qwen2MoeConfig.__init__: __init__().
  Qwen2MoeConfig.sliding_window: sliding_window.
  Qwen2MoeConfig.moe_intermediate_size: moe_intermediate_size.
  Qwen2MoeConfig.initializer_range: initializer_range.
  Qwen2MoeConfig.granted_freq_max_position_embedding: granted_freq_max_position_embedding().
  Qwen2MoeConfig.granted_mask_max_position_embedding: granted_mask_max_position_embedding().
  Qwen2MoeConfig.use_sliding_window: use_sliding_window.
  Qwen2MoeConfig.num_attention_heads: num_attention_heads.
  Qwen2MoeConfig.rms_norm_eps: rms_norm_eps.
  Qwen2MoeConfig.max_position_embeddings: max_position_embeddings.
  Qwen2MoeConfig.num_hidden_layers: num_hidden_layers.
  Qwen2MoeConfig.rope_theta: rope_theta.
  Qwen2MoeConfig.attention_dropout: attention_dropout.
  Qwen2MoeConfig.num_experts_per_tok: num_experts_per_tok.
  Qwen2MoeConfig.norm_topk_prob: norm_topk_prob.
  Qwen2MoeConfig.shared_expert_intermediate_size: shared_expert_intermediate_size.
  Qwen2MoeConfig.mlp_only_layers: mlp_only_layers.
  Qwen2MoeConfig.decoder_sparse_step: decoder_sparse_step.
  Qwen2MoeConfig.vocab_size: vocab_size.
  Qwen2MoeConfig.gradient_checkpointing: gradient_checkpointing.
  Qwen2MoeConfig.max_window_layers: max_window_layers.
  Qwen2MoeConfig.model_type: model_type.
  Qwen2MoeConfig.intermediate_size: intermediate_size.
  Qwen2MoeConfig.qkv_bias: qkv_bias.
  Qwen2MoeConfig.num_key_value_heads: num_key_value_heads.
  Qwen2MoeConfig.head_dim: head_dim.
  Qwen2MoeConfig.hidden_act: hidden_act.
  Qwen2MoeConfig.use_cache: use_cache.
  Qwen2MoeConfig.output_router_logits: output_router_logits.
  Qwen2MoeConfig.router_aux_loss_coef: router_aux_loss_coef.
  Qwen2MoeConfig.bits: bits.
  Qwen2MoeConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/qwen2_moe/qwen2_moe_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py)

## Classes
### `Qwen2MoeConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen2_moe/qwen2_moe_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L25)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class Qwen2MoeConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 151936, hidden_size: int = 2048, intermediate_size: int = 5632, num_hidden_layers: int = 24, num_attention_heads: int = 16, num_key_value_heads: int = 16, head_dim: int | None = None, hidden_act: str = "silu", max_position_embeddings: int = 32768, initializer_range: float = 0.02, rms_norm_eps: float = 0.000001, use_cache: bool = True, tie_word_embeddings: bool = False, qkv_bias: bool = False, rope_theta: float = 10000, use_sliding_window: bool = False, sliding_window: int | None = 4096, max_window_layers: int = 28, attention_dropout: float = 0, decoder_sparse_step: int = 1, moe_intermediate_size: int = 1408, shared_expert_intermediate_size: int = 5632, num_experts_per_tok: int = 4, num_experts: int = 60, norm_topk_prob: bool = False, output_router_logits: bool = False, router_aux_loss_coef: float = 0.001, mlp_only_layers: list[int] | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, bits: int | None = None, layer_types: list[str] | None = None, **kwargs)` — [`L98`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L98) — Initializes a Qwen2MoeConfig object.
  - `get_mask_details(self)` — [`L250`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L250) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L213) — Returns partition rules for model sharding.
  - `granted_freq_max_position_embedding(self)` — [`L227`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L227) — Returns the maximum position embedding size specifically for frequency-based position embeddings.
  - `granted_mask_max_position_embedding(self)` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L239) — Returns the maximum position embedding size specifically for mask-based position embeddings.
  - `attention_dropout` — [`L187`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L187)
  - `bits` — [`L199`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L199)
  - `decoder_sparse_step` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L190)
  - `gradient_checkpointing` — [`L198`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L198)
  - `head_dim` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L181)
  - `hidden_act` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L182)
  - `hidden_size` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L172)
  - `initializer_range` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L183)
  - `intermediate_size` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L173)
  - `layer_types` — [`L201`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L201)
  - `max_position_embeddings` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L171)
  - `max_window_layers` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L178)
  - `mlp_only_layers` — [`L200`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L200)
  - `model_type` — [`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L96)
  - `moe_intermediate_size` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L191)
  - `norm_topk_prob` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L195)
  - `num_attention_heads` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L175)
  - `num_experts` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L194)
  - `num_experts_per_tok` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L193)
  - `num_hidden_layers` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L174)
  - `num_key_value_heads` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L180)
  - `output_router_logits` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L196)
  - `qkv_bias` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L179)
  - `rms_norm_eps` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L184)
  - `rope_theta` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L186)
  - `router_aux_loss_coef` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L197)
  - `shared_expert_intermediate_size` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L192)
  - `sliding_window` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L177)
  - `use_cache` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L185)
  - `use_sliding_window` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L176)
  - `vocab_size` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2_moe/qwen2_moe_configuration.py#L170)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`SLIDING`](../../infra/utils.md#AttnMaskType.SLIDING)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`__call__`](modeling_qwen2_moe.md#Qwen2MoeDecoderLayer.__call__), [`granted_freq_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_freq_max_position_embedding), [`__init__`](modeling_qwen2_moe.md#Qwen2MoeSparseBlock.__init__), [`granted_mask_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_mask_max_position_embedding), [`embed_tokens`](modeling_qwen2_moe.md#Qwen2MoeModel.embed_tokens), [`precision`](modeling_qwen2_moe.md#Qwen2MoeDecoderLayer.precision), [`Qwen2MoeModel`](modeling_qwen2_moe.md#Qwen2MoeModel), [`Qwen2MoeForCausalLM`](modeling_qwen2_moe.md#Qwen2MoeForCausalLM), [`Qwen2MoeForSequenceClassification`](modeling_qwen2_moe.md#Qwen2MoeForSequenceClassification), [`down_proj`](modeling_qwen2_moe.md#Qwen2MoeMLPStack.down_proj), [`gate_proj`](modeling_qwen2_moe.md#Qwen2MoeMLPStack.gate_proj), [`up_proj`](modeling_qwen2_moe.md#Qwen2MoeMLPStack.up_proj), [`_create_rotary`](modeling_qwen2_moe.md#Qwen2MoeAttention._create_rotary), [`gate`](modeling_qwen2_moe.md#Qwen2MoeSparseBlock.gate), [`input_layernorm`](modeling_qwen2_moe.md#Qwen2MoeDecoderLayer.input_layernorm), [`post_attention_layernorm`](modeling_qwen2_moe.md#Qwen2MoeDecoderLayer.post_attention_layernorm), [`shared_expert_gate`](modeling_qwen2_moe.md#Qwen2MoeSparseBlock.shared_expert_gate), [`__init__`](modeling_qwen2_moe.md#Qwen2MoeAttention.__init__), [`_create_attention_performer`](modeling_qwen2_moe.md#Qwen2MoeAttention._create_attention_performer), [`__init__`](modeling_qwen2_moe.md#Qwen2MoeForCausalLM.__init__), [`__init__`](modeling_qwen2_moe.md#Qwen2MoeForSequenceClassification.__init__), [`precision`](modeling_qwen2_moe.md#Qwen2MoeMLP.precision), [`shared_expert`](modeling_qwen2_moe.md#Qwen2MoeSparseBlock.shared_expert), [`__init__`](modeling_qwen2_moe.md#Qwen2MoeModel.__init__), [`down_proj`](modeling_qwen2_moe.md#Qwen2MoeMLP.down_proj), [`gate_proj`](modeling_qwen2_moe.md#Qwen2MoeMLP.gate_proj), [`up_proj`](modeling_qwen2_moe.md#Qwen2MoeMLP.up_proj), [`__init__`](modeling_qwen2_moe.md#Qwen2MoeDecoderLayer.__init__), [`__init__`](modeling_qwen2_moe.md#Qwen2MoeMLP.__init__), [`__init__`](modeling_qwen2_moe.md#Qwen2MoeMLPStack.__init__), [`_config_class`](modeling_qwen2_moe.md#Qwen2MoeForCausalLM._config_class), [`_config_class`](modeling_qwen2_moe.md#Qwen2MoeForSequenceClassification._config_class)

