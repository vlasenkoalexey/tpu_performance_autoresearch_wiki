---
title: 'Module: easydel/modules/internlm2/internlm2_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/internlm2/internlm2_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.internlm2.internlm2_configuration`/InternLM2Config#
symbols:
  InternLM2Config: ''
  InternLM2Config.layer_types: layer_types.
  InternLM2Config.hidden_size: hidden_size.
  InternLM2Config.__init__: __init__().
  InternLM2Config.intermediate_size: intermediate_size.
  InternLM2Config.rms_norm_eps: rms_norm_eps.
  InternLM2Config.granted_freq_max_position_embedding: granted_freq_max_position_embedding().
  InternLM2Config.granted_mask_max_position_embedding: granted_mask_max_position_embedding().
  InternLM2Config.initializer_range: initializer_range.
  InternLM2Config.num_hidden_layers: num_hidden_layers.
  InternLM2Config.max_position_embeddings: max_position_embeddings.
  InternLM2Config.vocab_size: vocab_size.
  InternLM2Config.rope_theta: rope_theta.
  InternLM2Config.gradient_checkpointing: gradient_checkpointing.
  InternLM2Config.hidden_act: hidden_act.
  InternLM2Config.model_type: model_type.
  InternLM2Config.num_key_value_heads: num_key_value_heads.
  InternLM2Config.head_dim: head_dim.
  InternLM2Config.bias: bias.
  InternLM2Config.num_attention_heads: num_attention_heads.
  InternLM2Config.use_cache: use_cache.
  InternLM2Config.pretraining_tp: pretraining_tp.
  InternLM2Config.fcm_min_ratio: fcm_min_ratio.
  InternLM2Config.fcm_max_ratio: fcm_max_ratio.
  InternLM2Config.rope_scaling: rope_scaling.
  InternLM2Config.bits: bits.
  InternLM2Config.scan_layers: scan_layers.
  InternLM2Config.attn_implementation: attn_implementation.
  InternLM2Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/internlm2/internlm2_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py)

## Classes
### `InternLM2Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/internlm2/internlm2_configuration.py:24`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L24)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class InternLM2Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 103168, hidden_size: int = 4096, intermediate_size: int = 11008, num_hidden_layers: int = 32, num_attention_heads: int = 32, num_key_value_heads: int | None = None, head_dim: int | None = None, hidden_act: str = "silu", max_position_embeddings: int = 2048, initializer_range: float = 0.02, rms_norm_eps: float = 0.000001, use_cache: bool = True, pad_token_id: int = 0, bos_token_id: int = 1, eos_token_id: int = 2, pretraining_tp: int = 1, tie_word_embeddings: bool = False, bias: bool = True, rope_theta: float = 10000, rope_scaling: dict | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, fcm_min_ratio: float = -1, fcm_max_ratio: float = -1, scan_mlp_chunk_size: int = 1024, bits: int | None = None, scan_layers: bool = False, layer_types: list[str] | None = None, **kwargs)` — [`L95`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L95) — Initializes an InternLM2Config object.
  - `get_partition_rules(self, *args, **kwargs)` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L209) — Returns partition rules for model sharding.
  - `granted_freq_max_position_embedding(self)` — [`L223`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L223) — Returns the maximum position embedding size specifically for frequency-based position embeddings.
  - `granted_mask_max_position_embedding(self)` — [`L239`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L239) — Returns the maximum position embedding size specifically for mask-based position embeddings.
  - `attn_implementation` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L181)
  - `bias` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L168)
  - `bits` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L179)
  - `fcm_max_ratio` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L177)
  - `fcm_min_ratio` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L175)
  - `gradient_checkpointing` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L174)
  - `head_dim` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L163)
  - `hidden_act` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L176)
  - `hidden_size` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L162)
  - `initializer_range` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L164)
  - `intermediate_size` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L165)
  - `layer_types` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L184)
  - `max_position_embeddings` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L170)
  - `model_type` — [`L93`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L93)
  - `num_attention_heads` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L169)
  - `num_hidden_layers` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L166)
  - `num_key_value_heads` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L159)
  - `pretraining_tp` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L173)
  - `rms_norm_eps` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L171)
  - `rope_scaling` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L178)
  - `rope_theta` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L167)
  - `scan_layers` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L180)
  - `use_cache` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L172)
  - `vocab_size` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/internlm2/internlm2_configuration.py#L160)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`granted_freq_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_freq_max_position_embedding), [`granted_mask_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_mask_max_position_embedding), [`tok_embeddings`](modeling_internlm2.md#InternLM2Model.tok_embeddings), [`InternLM2Model`](modeling_internlm2.md#InternLM2Model), [`InternLM2ForCausalLM`](modeling_internlm2.md#InternLM2ForCausalLM), [`InternLM2ForSequenceClassification`](modeling_internlm2.md#InternLM2ForSequenceClassification), [`__init__`](modeling_internlm2.md#InternLM2ForCausalLM.__init__), [`_create_rotary`](modeling_internlm2.md#InternLM2Attention._create_rotary), [`attention_norm`](modeling_internlm2.md#InternLM2Block.attention_norm), [`ffn_norm`](modeling_internlm2.md#InternLM2Block.ffn_norm), [`norm`](modeling_internlm2.md#InternLM2Model.norm), [`precision`](modeling_internlm2.md#InternLM2MLP.precision), [`__init__`](modeling_internlm2.md#InternLM2ForSequenceClassification.__init__), [`_create_attention_performer`](modeling_internlm2.md#InternLM2Attention._create_attention_performer), [`act_fn`](modeling_internlm2.md#InternLM2MLP.act_fn), [`w1`](modeling_internlm2.md#InternLM2MLP.w1), [`w2`](modeling_internlm2.md#InternLM2MLP.w2), [`w3`](modeling_internlm2.md#InternLM2MLP.w3), [`__init__`](modeling_internlm2.md#InternLM2Attention.__init__), [`__init__`](modeling_internlm2.md#InternLM2Model.__init__), [`layers`](modeling_internlm2.md#InternLM2Model.layers), [`__init__`](modeling_internlm2.md#InternLM2Block.__init__), [`__init__`](modeling_internlm2.md#InternLM2MLP.__init__), [`_config_class`](modeling_internlm2.md#InternLM2ForCausalLM._config_class), [`_config_class`](modeling_internlm2.md#InternLM2ForSequenceClassification._config_class)

