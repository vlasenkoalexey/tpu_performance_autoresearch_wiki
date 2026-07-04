---
title: 'Module: easydel/modules/cohere2/cohere2_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/cohere2/cohere2_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.cohere2.cohere2_configuration`/Cohere2Config#
symbols:
  Cohere2Config: ''
  Cohere2Config.layer_types: layer_types.
  Cohere2Config.get_mask_details: get_mask_details().
  Cohere2Config.__init__: __init__().
  Cohere2Config.hidden_size: hidden_size.
  Cohere2Config.intermediate_size: intermediate_size.
  Cohere2Config.num_hidden_layers: num_hidden_layers.
  Cohere2Config.initializer_range: initializer_range.
  Cohere2Config.sliding_window: sliding_window.
  Cohere2Config.sliding_window_pattern: sliding_window_pattern.
  Cohere2Config.vocab_size: vocab_size.
  Cohere2Config.layer_norm_eps: layer_norm_eps.
  Cohere2Config.attention_dropout: attention_dropout.
  Cohere2Config.gradient_checkpointing: gradient_checkpointing.
  Cohere2Config.model_type: model_type.
  Cohere2Config.max_position_embeddings: max_position_embeddings.
  Cohere2Config.logit_scale: logit_scale.
  Cohere2Config.num_attention_heads: num_attention_heads.
  Cohere2Config.num_key_value_heads: num_key_value_heads.
  Cohere2Config.hidden_act: hidden_act.
  Cohere2Config.use_cache: use_cache.
  Cohere2Config.rope_theta: rope_theta.
  Cohere2Config.rope_scaling: rope_scaling.
  Cohere2Config.attention_bias: attention_bias.
  Cohere2Config.head_dim: head_dim.
  Cohere2Config.bits: bits.
  Cohere2Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/cohere2/cohere2_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py)

## Classes
### `Cohere2Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/cohere2/cohere2_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L25)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class Cohere2Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 256000, hidden_size: int = 8192, intermediate_size: int = 22528, logit_scale: float = 0.0625, num_hidden_layers: int = 40, num_attention_heads: int = 64, num_key_value_heads: int | None = None, hidden_act: str = "silu", max_position_embeddings: int = 8192, initializer_range: float = 0.02, layer_norm_eps: float = 0.00001, use_cache: bool = True, pad_token_id: int = 0, bos_token_id: int = 5, eos_token_id: int = 255001, tie_word_embeddings: bool = True, rope_theta: float = 10000, rope_scaling: dict | None = None, attention_bias: bool = False, attention_dropout: float = 0, sliding_window: int = 4096, sliding_window_pattern: int = 4, layer_types: list[str] | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, bits: int | None = None, **kwargs)` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L84) — Initializes the Cohere2Config instance.
  - `get_mask_details(self)` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L196) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L183) — Returns partition rules for model sharding.
  - `attention_bias` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L160)
  - `attention_dropout` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L161)
  - `bits` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L166)
  - `gradient_checkpointing` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L165)
  - `head_dim` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L164)
  - `hidden_act` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L154)
  - `hidden_size` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L144)
  - `initializer_range` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L155)
  - `intermediate_size` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L146)
  - `layer_norm_eps` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L156)
  - `layer_types` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L168)
  - `logit_scale` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L145)
  - `max_position_embeddings` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L143)
  - `model_type` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L82)
  - `num_attention_heads` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L148)
  - `num_hidden_layers` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L147)
  - `num_key_value_heads` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L153)
  - `rope_scaling` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L159)
  - `rope_theta` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L158)
  - `sliding_window` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L162)
  - `sliding_window_pattern` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L163)
  - `use_cache` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L157)
  - `vocab_size` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/cohere2/cohere2_configuration.py#L142)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`embed_tokens`](modeling_cohere2.md#Cohere2Model.embed_tokens), [`Cohere2Model`](modeling_cohere2.md#Cohere2Model), [`Cohere2ForCausalLM`](modeling_cohere2.md#Cohere2ForCausalLM), [`Cohere2ForSequenceClassification`](modeling_cohere2.md#Cohere2ForSequenceClassification), [`precision`](modeling_cohere2.md#Cohere2MLP.precision), [`input_layernorm`](modeling_cohere2.md#Cohere2Block.input_layernorm), [`vision_config`](../aya_vision/aya_vision_configuration.md#AyaVisionConfig.vision_config), [`__init__`](modeling_cohere2.md#Cohere2Attention.__init__), [`_create_attention_performer`](modeling_cohere2.md#Cohere2Attention._create_attention_performer), [`__init__`](modeling_cohere2.md#Cohere2ForCausalLM.__init__), [`__init__`](modeling_cohere2.md#Cohere2ForSequenceClassification.__init__), [`_create_rotary`](modeling_cohere2.md#Cohere2Attention._create_rotary), [`down_proj`](modeling_cohere2.md#Cohere2MLP.down_proj), [`gate_proj`](modeling_cohere2.md#Cohere2MLP.gate_proj), [`up_proj`](modeling_cohere2.md#Cohere2MLP.up_proj), [`__init__`](modeling_cohere2.md#Cohere2Model.__init__), [`is_sliding`](modeling_cohere2.md#Cohere2Block.is_sliding), [`layers`](modeling_cohere2.md#Cohere2Model.layers), [`__init__`](modeling_cohere2.md#Cohere2Block.__init__), [`__init__`](modeling_cohere2.md#Cohere2MLP.__init__), [`_config_class`](modeling_cohere2.md#Cohere2ForCausalLM._config_class), [`_config_class`](modeling_cohere2.md#Cohere2ForSequenceClassification._config_class), [`sliding_window`](modeling_cohere2.md#Cohere2Block.sliding_window)

