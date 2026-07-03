---
title: 'Module: easydel/modules/phi3/phi3_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/phi3/phi3_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.phi3.phi3_configuration`/Phi3Config#
symbols:
  Phi3Config: ''
  Phi3Config.get_mask_details: get_mask_details().
  Phi3Config.layer_types: layer_types.
  Phi3Config.hidden_size: hidden_size.
  Phi3Config.rope_scaling: rope_scaling.
  Phi3Config.__init__: __init__().
  Phi3Config.resid_pdrop: resid_pdrop.
  Phi3Config._rope_scaling_validation: _rope_scaling_validation().
  Phi3Config.initializer_range: initializer_range.
  Phi3Config.sliding_window: sliding_window.
  Phi3Config.rms_norm_eps: rms_norm_eps.
  Phi3Config.granted_freq_max_position_embedding: granted_freq_max_position_embedding().
  Phi3Config.granted_mask_max_position_embedding: granted_mask_max_position_embedding().
  Phi3Config.intermediate_size: intermediate_size.
  Phi3Config.vocab_size: vocab_size.
  Phi3Config.num_hidden_layers: num_hidden_layers.
  Phi3Config.max_position_embeddings: max_position_embeddings.
  Phi3Config.hidden_act: hidden_act.
  Phi3Config.num_attention_heads: num_attention_heads.
  Phi3Config.num_key_value_heads: num_key_value_heads.
  Phi3Config.rope_theta: rope_theta.
  Phi3Config.embd_pdrop: embd_pdrop.
  Phi3Config.gradient_checkpointing: gradient_checkpointing.
  Phi3Config.model_type: model_type.
  Phi3Config.attention_dropout: attention_dropout.
  Phi3Config.original_max_position_embeddings: original_max_position_embeddings.
  Phi3Config.use_cache: use_cache.
  Phi3Config.bits: bits.
  Phi3Config.head_dim: head_dim.
  Phi3Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/phi3/phi3_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py)

## Classes
### `Phi3Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/phi3/phi3_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L25)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class Phi3Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size=32064, hidden_size=3072, intermediate_size=8192, num_hidden_layers=32, num_attention_heads=32, num_key_value_heads=None, resid_pdrop=0, embd_pdrop=0, attention_dropout=0, hidden_act="silu", max_position_embeddings=4096, original_max_position_embeddings=4096, initializer_range=0.02, rms_norm_eps=0.00001, use_cache=True, tie_word_embeddings=False, rope_theta=10000, rope_scaling=None, bos_token_id=1, eos_token_id=32000, pad_token_id=32000, sliding_window=None, bits: int | None = None, layer_types: list[str] | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, **kwargs)` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L89) — Initializes a Phi3Config object.
  - `_rope_scaling_validation(self)` — [`L203`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L203) — Validate the `rope_scaling` configuration.
  - `get_mask_details(self)` — [`L248`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L248) — Retrieve attention mask details for each layer in the model.
  - `get_partition_rules(self, *args, **kwargs)` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L190) — Returns partition rules for model sharding.
  - `granted_freq_max_position_embedding(self)` — [`L225`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L225) — Returns the maximum position embedding size specifically for frequency-based position embeddings.
  - `granted_mask_max_position_embedding(self)` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L237) — Returns the maximum position embedding size specifically for mask-based position embeddings.
  - `attention_dropout` — [`L160`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L160)
  - `bits` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L172)
  - `embd_pdrop` — [`L159`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L159)
  - `gradient_checkpointing` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L173)
  - `head_dim` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L174)
  - `hidden_act` — [`L161`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L161)
  - `hidden_size` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L149)
  - `initializer_range` — [`L164`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L164)
  - `intermediate_size` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L150)
  - `layer_types` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L175)
  - `max_position_embeddings` — [`L162`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L162)
  - `model_type` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L87)
  - `num_attention_heads` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L152)
  - `num_hidden_layers` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L151)
  - `num_key_value_heads` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L157)
  - `original_max_position_embeddings` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L163)
  - `resid_pdrop` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L158)
  - `rms_norm_eps` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L165)
  - `rope_scaling` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L168)
  - `rope_theta` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L167)
  - `sliding_window` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L170)
  - `use_cache` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L166)
  - `vocab_size` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi3/phi3_configuration.py#L148)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`granted_freq_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_freq_max_position_embedding), [`granted_mask_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_mask_max_position_embedding), [`Phi3ForCausalLM`](modeling_phi3.md#Phi3ForCausalLM), [`Phi3Model`](modeling_phi3.md#Phi3Model), [`embed_dropout`](modeling_phi3.md#Phi3Model.embed_dropout), [`_create_rotary`](modeling_phi3.md#Phi3Attention._create_rotary), [`post_attention_layernorm`](modeling_phi3.md#Phi3DecoderLayer.post_attention_layernorm), [`define_network`](modeling_phi3.md#Phi3Attention.define_network), [`embed_tokens`](modeling_phi3.md#Phi3Model.embed_tokens), [`activation_fn`](modeling_phi3.md#Phi3MLP.activation_fn), [`input_layernorm`](modeling_phi3.md#Phi3DecoderLayer.input_layernorm), [`norm`](modeling_phi3.md#Phi3Model.norm), [`qkv_proj`](modeling_phi3.md#Phi3Attention.qkv_proj), [`resid_dropout`](modeling_phi3.md#Phi3Attention.resid_dropout), [`__init__`](modeling_phi3.md#Phi3Attention.__init__), [`__init__`](modeling_phi3.md#Phi3ForCausalLM.__init__), [`precision`](modeling_phi3.md#Phi3MLP.precision), [`down_proj`](modeling_phi3.md#Phi3MLP.down_proj), [`gate_up_proj`](modeling_phi3.md#Phi3MLP.gate_up_proj), [`resid_attn_dropout`](modeling_phi3.md#Phi3DecoderLayer.resid_attn_dropout), [`resid_mlp_dropout`](modeling_phi3.md#Phi3DecoderLayer.resid_mlp_dropout), [`__init__`](modeling_phi3.md#Phi3Model.__init__), [`rotary`](modeling_phi3.md#Phi3Attention.rotary), [`__init__`](modeling_phi3.md#Phi3DecoderLayer.__init__), [`__init__`](modeling_phi3.md#Phi3MLP.__init__), [`_config_class`](modeling_phi3.md#Phi3ForCausalLM._config_class), [`vocab_size`](modeling_phi3.md#Phi3Model.vocab_size)

