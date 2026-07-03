---
title: 'Module: easydel/modules/qwen3/qwen3_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen3/qwen3_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen3.qwen3_configuration`/
symbols:
  Qwen3Config: Qwen3Config#
  Qwen3Config.layer_types: Qwen3Config#layer_types.
  Qwen3Config.get_mask_details: Qwen3Config#get_mask_details().
  Qwen3Config.hidden_size: Qwen3Config#hidden_size.
  Qwen3Config.rope_scaling: Qwen3Config#rope_scaling.
  Qwen3Config.initializer_range: Qwen3Config#initializer_range.
  Qwen3Config.intermediate_size: Qwen3Config#intermediate_size.
  Qwen3Config.sliding_window: Qwen3Config#sliding_window.
  Qwen3Config.rms_norm_eps: Qwen3Config#rms_norm_eps.
  Qwen3Config.num_hidden_layers: Qwen3Config#num_hidden_layers.
  logger: logger.
  Qwen3Config.hidden_act: Qwen3Config#hidden_act.
  Qwen3Config.vocab_size: Qwen3Config#vocab_size.
  Qwen3Config.max_window_layers: Qwen3Config#max_window_layers.
  Qwen3Config.model_type: Qwen3Config#model_type.
  Qwen3Config.__init__: Qwen3Config#__init__().
  Qwen3Config.max_position_embeddings: Qwen3Config#max_position_embeddings.
  Qwen3Config.num_attention_heads: Qwen3Config#num_attention_heads.
  Qwen3Config.use_sliding_window: Qwen3Config#use_sliding_window.
  Qwen3Config.num_key_value_heads: Qwen3Config#num_key_value_heads.
  Qwen3Config.head_dim: Qwen3Config#head_dim.
  Qwen3Config.use_cache: Qwen3Config#use_cache.
  Qwen3Config.rope_theta: Qwen3Config#rope_theta.
  Qwen3Config.attention_bias: Qwen3Config#attention_bias.
  Qwen3Config.attention_dropout: Qwen3Config#attention_dropout.
  Qwen3Config.get_partition_rules: Qwen3Config#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/qwen3/qwen3_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py)

## Classes
### `Qwen3Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen3/qwen3_configuration.py:27`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L27)
- doc: Configuration for the Qwen3 decoder-only transformer architecture.
- signature: `class Qwen3Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 151936, hidden_size: int = 4096, intermediate_size: int = 22016, num_hidden_layers: int = 32, num_attention_heads: int = 32, num_key_value_heads: int | None = 32, head_dim: int = 128, hidden_act: str = "silu", max_position_embeddings: int = 32768, initializer_range: float = 0.02, rms_norm_eps: float = 0.000001, use_cache: bool = True, tie_word_embeddings: bool = False, rope_theta: float = 10000, rope_scaling: dict | None = None, attention_bias: bool = False, use_sliding_window: bool = False, sliding_window: int | None = 4096, max_window_layers: int = 28, attention_dropout: float = 0, layer_types: list[str] | None = None, **kwargs)` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L83) — Initialize Qwen3Config with model architecture hyperparameters.
  - `get_mask_details(self)` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L164) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L151) — Returns partition rules for model sharding.
  - `attention_bias` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L134)
  - `attention_dropout` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L135)
  - `head_dim` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L127)
  - `hidden_act` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L128)
  - `hidden_size` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L114)
  - `initializer_range` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L129)
  - `intermediate_size` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L115)
  - `layer_types` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L136)
  - `max_position_embeddings` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L113)
  - `max_window_layers` — [`L120`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L120)
  - `model_type` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L81)
  - `num_attention_heads` — [`L117`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L117)
  - `num_hidden_layers` — [`L116`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L116)
  - `num_key_value_heads` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L126)
  - `rms_norm_eps` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L130)
  - `rope_scaling` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L133)
  - `rope_theta` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L132)
  - `sliding_window` — [`L119`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L119)
  - `use_cache` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L131)
  - `use_sliding_window` — [`L118`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L118)
  - `vocab_size` — [`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L112)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`embed_tokens`](modeling_qwen3.md#Qwen3Model.embed_tokens), [`Qwen3Model`](modeling_qwen3.md#Qwen3Model), [`Qwen3ForCausalLM`](modeling_qwen3.md#Qwen3ForCausalLM), [`Qwen3ForEmbedding`](modeling_qwen3.md#Qwen3ForEmbedding), [`Qwen3ForSequenceClassification`](modeling_qwen3.md#Qwen3ForSequenceClassification), [`input_layernorm`](modeling_qwen3.md#Qwen3DecoderLayer.input_layernorm), [`post_attention_layernorm`](modeling_qwen3.md#Qwen3DecoderLayer.post_attention_layernorm), [`__init__`](modeling_qwen3.md#Qwen3Attention.__init__), [`act_fn`](modeling_qwen3.md#Qwen3MLP.act_fn), [`norm`](modeling_qwen3.md#Qwen3Model.norm), [`__init__`](modeling_qwen3.md#Qwen3ForCausalLM.__init__), [`__init__`](modeling_qwen3.md#Qwen3ForEmbedding.__init__), [`__init__`](modeling_qwen3.md#Qwen3ForSequenceClassification.__init__), [`precision`](modeling_qwen3.md#Qwen3MLP.precision), [`down_proj`](modeling_qwen3.md#Qwen3MLP.down_proj), [`gate_proj`](modeling_qwen3.md#Qwen3MLP.gate_proj), [`up_proj`](modeling_qwen3.md#Qwen3MLP.up_proj), [`__init__`](modeling_qwen3.md#Qwen3Model.__init__), [`layers`](modeling_qwen3.md#Qwen3Model.layers), [`__init__`](modeling_qwen3.md#Qwen3DecoderLayer.__init__), [`__init__`](modeling_qwen3.md#Qwen3MLP.__init__), [`_config_class`](modeling_qwen3.md#Qwen3ForCausalLM._config_class), [`_config_class`](modeling_qwen3.md#Qwen3ForEmbedding._config_class), [`_config_class`](modeling_qwen3.md#Qwen3ForSequenceClassification._config_class)

## Module values
- `__all__` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L189)
- `logger` — [`L23`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3/qwen3_configuration.py#L23)

