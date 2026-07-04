---
title: 'Module: easydel/modules/gpt_neox/gpt_neox_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/gpt_neox/gpt_neox_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gpt_neox.gpt_neox_configuration`/GPTNeoXConfig#
symbols:
  GPTNeoXConfig: ''
  GPTNeoXConfig.layer_types: layer_types.
  GPTNeoXConfig.__init__: __init__().
  GPTNeoXConfig.hidden_size: hidden_size.
  GPTNeoXConfig.num_hidden_layers: num_hidden_layers.
  GPTNeoXConfig.intermediate_size: intermediate_size.
  GPTNeoXConfig.layer_norm_eps: layer_norm_eps.
  GPTNeoXConfig.hidden_act: hidden_act.
  GPTNeoXConfig.rotary_pct: rotary_pct.
  GPTNeoXConfig.rotary_emb_base: rotary_emb_base.
  GPTNeoXConfig.hidden_dropout: hidden_dropout.
  GPTNeoXConfig.gradient_checkpointing: gradient_checkpointing.
  GPTNeoXConfig.attention_dropout: attention_dropout.
  GPTNeoXConfig.use_parallel_residual: use_parallel_residual.
  GPTNeoXConfig.model_type: model_type.
  GPTNeoXConfig.vocab_size: vocab_size.
  GPTNeoXConfig.max_position_embeddings: max_position_embeddings.
  GPTNeoXConfig.num_attention_heads: num_attention_heads.
  GPTNeoXConfig.rope_theta: rope_theta.
  GPTNeoXConfig.classifier_dropout: classifier_dropout.
  GPTNeoXConfig.initializer_range: initializer_range.
  GPTNeoXConfig.use_cache: use_cache.
  GPTNeoXConfig.tie_word_embeddings: tie_word_embeddings.
  GPTNeoXConfig.rope_scaling: rope_scaling.
  GPTNeoXConfig.attention_bias: attention_bias.
  GPTNeoXConfig.from_pt: from_pt.
  GPTNeoXConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/gpt_neox/gpt_neox_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py)

## Classes
### `GPTNeoXConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/gpt_neox/gpt_neox_configuration.py:24`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L24)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class GPTNeoXConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 50432, hidden_size: int = 6144, num_hidden_layers: int = 44, num_attention_heads: int = 64, intermediate_size: int = 24576, hidden_act: str = "gelu", rotary_pct: float = 0.25, rotary_emb_base: int = 10000, attention_dropout: float = 0, hidden_dropout: float = 0, classifier_dropout: float = 0.1, max_position_embeddings: int = 2048, initializer_range: float = 0.02, layer_norm_eps: float = 0.00001, use_cache: bool = True, bos_token_id: int = 0, eos_token_id: int = 2, tie_word_embeddings: bool = False, use_parallel_residual: bool = True, rope_scaling: dict | None = None, attention_bias: bool = True, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, layer_types: list[str] | None = None, **kwargs)` — [`L74`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L74) — Initializes a GPTNeoXConfig object.
  - `get_partition_rules(self, *args, **kwargs)` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L156) — Returns partition rules for model sharding.
  - `attention_bias` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L149)
  - `attention_dropout` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L146)
  - `classifier_dropout` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L139)
  - `from_pt` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L150)
  - `gradient_checkpointing` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L145)
  - `hidden_act` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L135)
  - `hidden_dropout` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L144)
  - `hidden_size` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L131)
  - `initializer_range` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L140)
  - `intermediate_size` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L134)
  - `layer_norm_eps` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L141)
  - `layer_types` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L151)
  - `max_position_embeddings` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L130)
  - `model_type` — [`L72`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L72)
  - `num_attention_heads` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L133)
  - `num_hidden_layers` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L132)
  - `rope_scaling` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L148)
  - `rope_theta` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L138)
  - `rotary_emb_base` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L137)
  - `rotary_pct` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L136)
  - `tie_word_embeddings` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L143)
  - `use_cache` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L142)
  - `use_parallel_residual` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L147)
  - `vocab_size` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_neox/gpt_neox_configuration.py#L129)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`GPTNeoXForCausalLM`](modeling_gpt_neox.md#GPTNeoXForCausalLM), [`GPTNeoXModel`](modeling_gpt_neox.md#GPTNeoXModel), [`emb_dropout`](modeling_gpt_neox.md#GPTNeoXModel.emb_dropout), [`_create_rotary`](modeling_gpt_neox.md#GPTNeoXAttention._create_rotary), [`dense_4h_to_h`](modeling_gpt_neox.md#GPTNeoXMlp.dense_4h_to_h), [`dense_h_to_4h`](modeling_gpt_neox.md#GPTNeoXMlp.dense_h_to_4h), [`final_layer_norm`](modeling_gpt_neox.md#GPTNeoXModel.final_layer_norm), [`_create_attention_performer`](modeling_gpt_neox.md#GPTNeoXAttention._create_attention_performer), [`post_attention_layernorm`](modeling_gpt_neox.md#GPTNeoXBlock.post_attention_layernorm), [`act`](modeling_gpt_neox.md#GPTNeoXMlp.act), [`input_layernorm`](modeling_gpt_neox.md#GPTNeoXBlock.input_layernorm), [`__init__`](modeling_gpt_neox.md#GPTNeoXForCausalLM.__init__), [`__init__`](modeling_gpt_neox.md#GPTNeoXAttention.__init__), [`__init__`](modeling_gpt_neox.md#GPTNeoXModel.__init__), [`layers`](modeling_gpt_neox.md#GPTNeoXModel.layers), [`use_parallel_residual`](modeling_gpt_neox.md#GPTNeoXBlock.use_parallel_residual), [`__init__`](modeling_gpt_neox.md#GPTNeoXBlock.__init__), [`__init__`](modeling_gpt_neox.md#GPTNeoXMlp.__init__), [`_config_class`](modeling_gpt_neox.md#GPTNeoXForCausalLM._config_class)

