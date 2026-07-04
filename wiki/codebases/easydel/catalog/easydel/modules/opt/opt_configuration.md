---
title: 'Module: easydel/modules/opt/opt_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/opt/opt_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.opt.opt_configuration`/OPTConfig#
symbols:
  OPTConfig: ''
  OPTConfig.__init__: __init__().
  OPTConfig.layer_types: layer_types.
  OPTConfig.init_std: init_std.
  OPTConfig.num_hidden_layers: num_hidden_layers.
  OPTConfig.hidden_size: hidden_size.
  OPTConfig.num_attention_heads: num_attention_heads.
  OPTConfig.attention_dropout: attention_dropout.
  OPTConfig.do_layer_norm_before: do_layer_norm_before.
  OPTConfig.dropout: dropout.
  OPTConfig.activation_function: activation_function.
  OPTConfig.vocab_size: vocab_size.
  OPTConfig.word_embed_proj_dim: word_embed_proj_dim.
  OPTConfig.gradient_checkpointing: gradient_checkpointing.
  OPTConfig.model_type: model_type.
  OPTConfig.attribute_map: attribute_map.
  OPTConfig.keys_to_ignore_at_inference: keys_to_ignore_at_inference.
  OPTConfig.max_position_embeddings: max_position_embeddings.
  OPTConfig.ffn_dim: ffn_dim.
  OPTConfig.layerdrop: layerdrop.
  OPTConfig.use_cache: use_cache.
  OPTConfig.enable_bias: enable_bias.
  OPTConfig.layer_norm_elementwise_affine: layer_norm_elementwise_affine.
  OPTConfig._remove_final_layer_norm: _remove_final_layer_norm.
  OPTConfig.from_pt: from_pt.
  OPTConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/opt/opt_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py)

## Classes
### `OPTConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/opt/opt_configuration.py:26`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L26)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class OPTConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 50272, hidden_size: int = 768, num_hidden_layers: int = 12, ffn_dim: int = 3072, max_position_embeddings: int = 2048, do_layer_norm_before: bool = True, _remove_final_layer_norm: bool = False, word_embed_proj_dim: int | None = None, dropout: float = 0.1, attention_dropout: float = 0, num_attention_heads: int = 12, activation_function: str = "relu", layerdrop: float = 0, init_std: float = 0.02, use_cache: bool = True, pad_token_id: int = 1, bos_token_id: int = 2, eos_token_id: int = 2, enable_bias: bool = True, layer_norm_elementwise_affine: bool = True, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, layer_types: list[str] | None = None, **kwargs)` — [`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L85) — Initializes the OPTConfig object.
  - `get_partition_rules(self, *args, **kwargs)` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L168) — Returns partition rules for model sharding.
  - `activation_function` — [`L155`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L155)
  - `attention_dropout` — [`L154`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L154)
  - `attribute_map` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L82)
  - `do_layer_norm_before` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L159)
  - `dropout` — [`L153`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L153)
  - `enable_bias` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L160)
  - `ffn_dim` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L150)
  - `from_pt` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L163)
  - `gradient_checkpointing` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L146)
  - `hidden_size` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L151)
  - `init_std` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L156)
  - `keys_to_ignore_at_inference` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L83)
  - `layer_norm_elementwise_affine` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L161)
  - `layer_types` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L164)
  - `layerdrop` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L157)
  - `max_position_embeddings` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L147)
  - `model_type` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L81)
  - `num_attention_heads` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L148)
  - `num_hidden_layers` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L152)
  - `use_cache` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L158)
  - `vocab_size` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L145)
  - `word_embed_proj_dim` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L149)
- protocol/private: `_remove_final_layer_norm`[`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/opt/opt_configuration.py#L162)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`final_layer_norm`](modeling_opt.md#OPTDecoder.final_layer_norm), [`OPTForCausalLM`](modeling_opt.md#OPTForCausalLM), [`embed_tokens`](modeling_opt.md#OPTDecoder.embed_tokens), [`embed_dim`](modeling_opt.md#OPTDecoderLayer.embed_dim), [`embed_positions`](modeling_opt.md#OPTDecoder.embed_positions), [`self_attn`](modeling_opt.md#OPTDecoderLayer.self_attn), [`head_dim`](modeling_opt.md#OPTAttention.head_dim), [`__init__`](modeling_opt.md#OPTForCausalLM.__init__), [`do_layer_norm_before`](modeling_opt.md#OPTDecoderLayer.do_layer_norm_before), [`activation_fn`](modeling_opt.md#OPTDecoderLayer.activation_fn), [`fc1`](modeling_opt.md#OPTDecoderLayer.fc1), [`fc2`](modeling_opt.md#OPTDecoderLayer.fc2), [`dropout_layer`](modeling_opt.md#OPTDecoderLayer.dropout_layer), [`__init__`](modeling_opt.md#OPTAttention.__init__), [`__init__`](modeling_opt.md#OPTDecoder.__init__), [`__init__`](modeling_opt.md#OPTModel.__init__), [`layers`](modeling_opt.md#OPTDecoder.layers), [`__init__`](modeling_opt.md#OPTDecoderLayer.__init__), [`_config_class`](modeling_opt.md#OPTForCausalLM._config_class)

