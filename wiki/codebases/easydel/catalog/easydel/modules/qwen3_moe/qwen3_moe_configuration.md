---
title: 'Module: easydel/modules/qwen3_moe/qwen3_moe_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen3_moe/qwen3_moe_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen3_moe.qwen3_moe_configuration`/
symbols:
  Qwen3MoeConfig: Qwen3MoeConfig#
  Qwen3MoeConfig.get_mask_details: Qwen3MoeConfig#get_mask_details().
  Qwen3MoeConfig.layer_types: Qwen3MoeConfig#layer_types.
  Qwen3MoeConfig.hidden_size: Qwen3MoeConfig#hidden_size.
  Qwen3MoeConfig.num_experts: Qwen3MoeConfig#num_experts.
  Qwen3MoeConfig.initializer_range: Qwen3MoeConfig#initializer_range.
  Qwen3MoeConfig.sliding_window: Qwen3MoeConfig#sliding_window.
  Qwen3MoeConfig.rope_scaling: Qwen3MoeConfig#rope_scaling.
  Qwen3MoeConfig.moe_intermediate_size: Qwen3MoeConfig#moe_intermediate_size.
  Qwen3MoeConfig.max_window_layers: Qwen3MoeConfig#max_window_layers.
  Qwen3MoeConfig.rms_norm_eps: Qwen3MoeConfig#rms_norm_eps.
  Qwen3MoeConfig.num_hidden_layers: Qwen3MoeConfig#num_hidden_layers.
  logger: logger.
  Qwen3MoeConfig.attention_dropout: Qwen3MoeConfig#attention_dropout.
  Qwen3MoeConfig.hidden_act: Qwen3MoeConfig#hidden_act.
  Qwen3MoeConfig.use_sliding_window: Qwen3MoeConfig#use_sliding_window.
  Qwen3MoeConfig.intermediate_size: Qwen3MoeConfig#intermediate_size.
  Qwen3MoeConfig.num_experts_per_tok: Qwen3MoeConfig#num_experts_per_tok.
  Qwen3MoeConfig.norm_topk_prob: Qwen3MoeConfig#norm_topk_prob.
  Qwen3MoeConfig.mlp_only_layers: Qwen3MoeConfig#mlp_only_layers.
  Qwen3MoeConfig.decoder_sparse_step: Qwen3MoeConfig#decoder_sparse_step.
  Qwen3MoeConfig.vocab_size: Qwen3MoeConfig#vocab_size.
  Qwen3MoeConfig.model_type: Qwen3MoeConfig#model_type.
  Qwen3MoeConfig.__init__: Qwen3MoeConfig#__init__().
  Qwen3MoeConfig.max_position_embeddings: Qwen3MoeConfig#max_position_embeddings.
  Qwen3MoeConfig.num_attention_heads: Qwen3MoeConfig#num_attention_heads.
  Qwen3MoeConfig.num_key_value_heads: Qwen3MoeConfig#num_key_value_heads.
  Qwen3MoeConfig.head_dim: Qwen3MoeConfig#head_dim.
  Qwen3MoeConfig.use_cache: Qwen3MoeConfig#use_cache.
  Qwen3MoeConfig.rope_theta: Qwen3MoeConfig#rope_theta.
  Qwen3MoeConfig.attention_bias: Qwen3MoeConfig#attention_bias.
  Qwen3MoeConfig.output_router_logits: Qwen3MoeConfig#output_router_logits.
  Qwen3MoeConfig.router_aux_loss_coef: Qwen3MoeConfig#router_aux_loss_coef.
  Qwen3MoeConfig.get_partition_rules: Qwen3MoeConfig#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/qwen3_moe/qwen3_moe_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py)

## Classes
### `Qwen3MoeConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen3_moe/qwen3_moe_configuration.py:27`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L27)
- doc: Configuration for the Qwen3-MoE mixture-of-experts decoder architecture.
- signature: `class Qwen3MoeConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 151936, hidden_size: int = 2048, intermediate_size: int = 6144, num_hidden_layers: int = 24, num_attention_heads: int = 32, num_key_value_heads: int = 4, head_dim: int | None = None, hidden_act: str = "silu", max_position_embeddings: int = 32768, initializer_range: float = 0.02, rms_norm_eps: float = 0.000001, use_cache: bool = True, tie_word_embeddings: bool = False, rope_theta: float = 10000, rope_scaling: dict | None = None, attention_bias: bool = False, use_sliding_window: bool = False, sliding_window: int = 4096, max_window_layers: int = 28, attention_dropout: float = 0, decoder_sparse_step: int = 1, moe_intermediate_size: int = 768, num_experts_per_tok: int = 8, num_experts: int = 128, norm_topk_prob: bool = False, output_router_logits: bool = False, router_aux_loss_coef: float = 0.001, mlp_only_layers: list[int] | None = None, layer_types: list[str] | None = None, **kwargs)` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L99) — Initialize Qwen3MoeConfig with MoE architecture hyperparameters.
  - `get_mask_details(self)` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L192) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L179) — Returns partition rules for model sharding.
  - `attention_bias` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L154)
  - `attention_dropout` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L155)
  - `decoder_sparse_step` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L159)
  - `head_dim` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L147)
  - `hidden_act` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L148)
  - `hidden_size` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L138)
  - `initializer_range` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L149)
  - `intermediate_size` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L139)
  - `layer_types` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L167)
  - `max_position_embeddings` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L137)
  - `max_window_layers` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L144)
  - `mlp_only_layers` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L166)
  - `model_type` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L97)
  - `moe_intermediate_size` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L160)
  - `norm_topk_prob` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L163)
  - `num_attention_heads` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L141)
  - `num_experts` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L162)
  - `num_experts_per_tok` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L161)
  - `num_hidden_layers` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L140)
  - `num_key_value_heads` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L146)
  - `output_router_logits` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L164)
  - `rms_norm_eps` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L150)
  - `rope_scaling` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L153)
  - `rope_theta` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L152)
  - `router_aux_loss_coef` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L165)
  - `sliding_window` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L143)
  - `use_cache` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L151)
  - `use_sliding_window` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L142)
  - `vocab_size` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L136)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`SLIDING`](../../infra/utils.md#AttnMaskType.SLIDING)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`__init__`](modeling_qwen3_moe.md#Qwen3MoeSparseBlock.__init__), [`embed_tokens`](modeling_qwen3_moe.md#Qwen3MoeModel.embed_tokens), [`Qwen3MoeModel`](modeling_qwen3_moe.md#Qwen3MoeModel), [`Qwen3MoeForCausalLM`](modeling_qwen3_moe.md#Qwen3MoeForCausalLM), [`Qwen3MoeForSequenceClassification`](modeling_qwen3_moe.md#Qwen3MoeForSequenceClassification), [`down_proj`](modeling_qwen3_moe.md#Qwen3MoeMLPStack.down_proj), [`gate_proj`](modeling_qwen3_moe.md#Qwen3MoeMLPStack.gate_proj), [`up_proj`](modeling_qwen3_moe.md#Qwen3MoeMLPStack.up_proj), [`__init__`](modeling_qwen3_moe.md#Qwen3MoeAttention.__init__), [`is_moe`](modeling_qwen3_moe.md#Qwen3MoeDecoderLayer.is_moe), [`gate`](modeling_qwen3_moe.md#Qwen3MoeSparseBlock.gate), [`input_layernorm`](modeling_qwen3_moe.md#Qwen3MoeDecoderLayer.input_layernorm), [`post_attention_layernorm`](modeling_qwen3_moe.md#Qwen3MoeDecoderLayer.post_attention_layernorm), [`precision`](modeling_qwen3_moe.md#Qwen3MoeMLP.precision), [`act_fn`](modeling_qwen3_moe.md#Qwen3MoeMLP.act_fn), [`norm`](modeling_qwen3_moe.md#Qwen3MoeModel.norm), [`__init__`](modeling_qwen3_moe.md#Qwen3MoeForCausalLM.__init__), [`__init__`](modeling_qwen3_moe.md#Qwen3MoeForSequenceClassification.__init__), [`act_fn`](modeling_qwen3_moe.md#Qwen3MoeMLPStack.act_fn), [`__init__`](modeling_qwen3_moe.md#Qwen3MoeModel.__init__), [`layers`](modeling_qwen3_moe.md#Qwen3MoeModel.layers), [`down_proj`](modeling_qwen3_moe.md#Qwen3MoeMLP.down_proj), [`gate_proj`](modeling_qwen3_moe.md#Qwen3MoeMLP.gate_proj), [`up_proj`](modeling_qwen3_moe.md#Qwen3MoeMLP.up_proj), [`__init__`](modeling_qwen3_moe.md#Qwen3MoeDecoderLayer.__init__), [`__init__`](modeling_qwen3_moe.md#Qwen3MoeMLP.__init__), [`__init__`](modeling_qwen3_moe.md#Qwen3MoeMLPStack.__init__), [`_config_class`](modeling_qwen3_moe.md#Qwen3MoeForCausalLM._config_class), [`_config_class`](modeling_qwen3_moe.md#Qwen3MoeForSequenceClassification._config_class)

## Module values
- `__all__` — [`L214`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L214)
- `logger` — [`L23`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_moe/qwen3_moe_configuration.py#L23)

