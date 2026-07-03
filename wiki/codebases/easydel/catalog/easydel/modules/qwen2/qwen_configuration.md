---
title: 'Module: easydel/modules/qwen2/qwen_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen2/qwen_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen2.qwen_configuration`/Qwen2Config#
symbols:
  Qwen2Config: ''
  Qwen2Config.layer_types: layer_types.
  Qwen2Config.get_mask_details: get_mask_details().
  Qwen2Config.hidden_size: hidden_size.
  Qwen2Config.__init__: __init__().
  Qwen2Config.rope_scaling: rope_scaling.
  Qwen2Config.initializer_range: initializer_range.
  Qwen2Config.intermediate_size: intermediate_size.
  Qwen2Config.sliding_window: sliding_window.
  Qwen2Config.rms_norm_eps: rms_norm_eps.
  Qwen2Config.num_hidden_layers: num_hidden_layers.
  Qwen2Config.num_attention_heads: num_attention_heads.
  Qwen2Config.resid_pdrop: resid_pdrop.
  Qwen2Config.hidden_act: hidden_act.
  Qwen2Config.rope_theta: rope_theta.
  Qwen2Config.attention_dropout: attention_dropout.
  Qwen2Config.use_scan_mlp: use_scan_mlp.
  Qwen2Config.scan_mlp_chunk_size: scan_mlp_chunk_size.
  Qwen2Config.vocab_size: vocab_size.
  Qwen2Config.embd_pdrop: embd_pdrop.
  Qwen2Config.gradient_checkpointing: gradient_checkpointing.
  Qwen2Config.max_window_layers: max_window_layers.
  Qwen2Config.model_type: model_type.
  Qwen2Config.max_position_embeddings: max_position_embeddings.
  Qwen2Config.use_sliding_window: use_sliding_window.
  Qwen2Config.num_key_value_heads: num_key_value_heads.
  Qwen2Config.use_cache: use_cache.
  Qwen2Config.scan_layers: scan_layers.
  Qwen2Config.number_rep_kv: number_rep_kv.
  Qwen2Config.tie_word_embeddings: tie_word_embeddings.
  Qwen2Config.fcm_min_ratio: fcm_min_ratio.
  Qwen2Config.fcm_max_ratio: fcm_max_ratio.
  Qwen2Config.bits: bits.
  Qwen2Config.head_dim: head_dim.
  Qwen2Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/qwen2/qwen_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py)

## Classes
### `Qwen2Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen2/qwen_configuration.py:26`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L26)
- doc: Configuration objects inherit from \[`PretrainedConfig`\] and can be used to control the model outputs. Read
- signature: `class Qwen2Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 151936, hidden_size: int = 4096, intermediate_size: int = 22016, num_hidden_layers: int = 32, num_attention_heads: int = 32, num_key_value_heads: int | None = 32, hidden_act: str = "silu", max_position_embeddings: int = 32768, initializer_range: float = 0.02, rms_norm_eps: float = 0.000001, use_cache: bool = True, tie_word_embeddings: bool = False, rope_theta: float = 10000, use_sliding_window: bool = False, sliding_window: int | None = 4096, max_window_layers: int = 28, attention_dropout: float = 0, resid_pdrop: float = 0, embd_pdrop: float = 0, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, fcm_min_ratio: float = 0, fcm_max_ratio: float = 0, use_scan_mlp: bool = False, scan_mlp_chunk_size: int = 1024, number_rep_kv: int = 1, bits: int | None = None, scan_layers: bool = True, layer_types: list[str] | None = None, rope_scaling: Mapping[str, str | float] | None = None, **kwargs)` — [`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L96) — Initializes a Qwen2Config object.
  - `get_mask_details(self)` — [`L231`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L231) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L218`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L218) — Returns partition rules for model sharding.
  - `attention_dropout` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L189)
  - `bits` — [`L196`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L196)
  - `embd_pdrop` — [`L186`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L186)
  - `fcm_max_ratio` — [`L193`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L193)
  - `fcm_min_ratio` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L192)
  - `gradient_checkpointing` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L191)
  - `head_dim` — [`L197`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L197)
  - `hidden_act` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L180)
  - `hidden_size` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L166)
  - `initializer_range` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L181)
  - `intermediate_size` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L167)
  - `layer_types` — [`L198`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L198)
  - `max_position_embeddings` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L165)
  - `max_window_layers` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L172)
  - `model_type` — [`L94`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L94)
  - `num_attention_heads` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L169)
  - `num_hidden_layers` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L168)
  - `num_key_value_heads` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L179)
  - `number_rep_kv` — [`L187`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L187)
  - `resid_pdrop` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L188)
  - `rms_norm_eps` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L182)
  - `rope_scaling` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L178)
  - `rope_theta` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L184)
  - `scan_layers` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L185)
  - `scan_mlp_chunk_size` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L195)
  - `sliding_window` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L171)
  - `tie_word_embeddings` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L190)
  - `use_cache` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L183)
  - `use_scan_mlp` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L194)
  - `use_sliding_window` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L170)
  - `vocab_size` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen2/qwen_configuration.py#L164)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`__call__`](modeling_qwen.md#Qwen2DecoderLayer.__call__), [`Qwen2Model`](modeling_qwen.md#Qwen2Model), [`Qwen2ForCausalLM`](modeling_qwen.md#Qwen2ForCausalLM), [`Qwen2ForEmbedding`](modeling_qwen.md#Qwen2ForEmbedding), [`Qwen2ForSequenceClassification`](modeling_qwen.md#Qwen2ForSequenceClassification), [`dropout`](modeling_qwen.md#Qwen2Model.dropout), [`_create_rotary`](modeling_qwen.md#Qwen2Attention._create_rotary), [`embed_tokens`](modeling_qwen.md#Qwen2Model.embed_tokens), [`input_layernorm`](modeling_qwen.md#Qwen2DecoderLayer.input_layernorm), [`post_attention_layernorm`](modeling_qwen.md#Qwen2DecoderLayer.post_attention_layernorm), [`__init__`](modeling_qwen.md#Qwen2Attention.__init__), [`_create_attention_performer`](modeling_qwen.md#Qwen2Attention._create_attention_performer), [`act_fn`](modeling_qwen.md#Qwen2MLP.act_fn), [`norm`](modeling_qwen.md#Qwen2Model.norm), [`__init__`](modeling_qwen.md#Qwen2ForCausalLM.__init__), [`__init__`](modeling_qwen.md#Qwen2ForEmbedding.__init__), [`__init__`](modeling_qwen.md#Qwen2ForSequenceClassification.__init__), [`precision`](modeling_qwen.md#Qwen2MLP.precision), [`down_proj`](modeling_qwen.md#Qwen2MLP.down_proj), [`dropout`](modeling_qwen.md#Qwen2MLP.dropout), [`gate_proj`](modeling_qwen.md#Qwen2MLP.gate_proj), [`up_proj`](modeling_qwen.md#Qwen2MLP.up_proj), [`__init__`](modeling_qwen.md#Qwen2Model.__init__), [`layers`](modeling_qwen.md#Qwen2Model.layers), [`__init__`](modeling_qwen.md#Qwen2DecoderLayer.__init__), [`__init__`](modeling_qwen.md#Qwen2MLP.__init__), [`_config_class`](modeling_qwen.md#Qwen2ForCausalLM._config_class), [`_config_class`](modeling_qwen.md#Qwen2ForEmbedding._config_class), [`_config_class`](modeling_qwen.md#Qwen2ForSequenceClassification._config_class)

