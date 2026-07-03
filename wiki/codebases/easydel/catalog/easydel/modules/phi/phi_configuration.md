---
title: 'Module: easydel/modules/phi/phi_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/phi/phi_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.phi.phi_configuration`/PhiConfig#
symbols:
  PhiConfig: ''
  PhiConfig.layer_types: layer_types.
  PhiConfig.hidden_size: hidden_size.
  PhiConfig.__init__: __init__().
  PhiConfig.granted_freq_max_position_embedding: granted_freq_max_position_embedding().
  PhiConfig.granted_mask_max_position_embedding: granted_mask_max_position_embedding().
  PhiConfig.intermediate_size: intermediate_size.
  PhiConfig.initializer_range: initializer_range.
  PhiConfig.qk_layernorm: qk_layernorm.
  PhiConfig.partial_rotary_factor: partial_rotary_factor.
  PhiConfig.layer_norm_eps: layer_norm_eps.
  PhiConfig.vocab_size: vocab_size.
  PhiConfig.max_position_embeddings: max_position_embeddings.
  PhiConfig.hidden_act: hidden_act.
  PhiConfig.attention_dropout: attention_dropout.
  PhiConfig.resid_pdrop: resid_pdrop.
  PhiConfig.embd_pdrop: embd_pdrop.
  PhiConfig.gradient_checkpointing: gradient_checkpointing.
  PhiConfig.num_hidden_layers: num_hidden_layers.
  PhiConfig.model_type: model_type.
  PhiConfig.num_attention_heads: num_attention_heads.
  PhiConfig.num_key_value_heads: num_key_value_heads.
  PhiConfig.use_cache: use_cache.
  PhiConfig.rope_theta: rope_theta.
  PhiConfig.rope_scaling: rope_scaling.
  PhiConfig.bits: bits.
  PhiConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/phi/phi_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py)

## Classes
### `PhiConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/phi/phi_configuration.py:24`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L24)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class PhiConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size=51200, hidden_size=2048, intermediate_size=8192, num_hidden_layers=24, num_attention_heads=32, num_key_value_heads=None, resid_pdrop=0, embd_pdrop=0, attention_dropout=0, hidden_act="gelu_new", max_position_embeddings=2048, initializer_range=0.02, layer_norm_eps=0.00001, use_cache=True, tie_word_embeddings=False, rope_theta=10000, rope_scaling=None, partial_rotary_factor=0.5, qk_layernorm=False, bos_token_id=1, eos_token_id=2, bits: int | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, layer_types: list[str] | None = None, **kwargs)` — [`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L91) — Initialize PhiConfig with model architecture hyperparameters.
  - `get_partition_rules(self, *args, **kwargs)` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L158) — Returns partition rules for model sharding.
  - `granted_freq_max_position_embedding(self)` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L172) — Returns the maximum position embedding size specifically for frequency-based position embeddings.
  - `granted_mask_max_position_embedding(self)` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L188) — Returns the maximum position embedding size specifically for mask-based position embeddings.
  - `attention_dropout` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L135)
  - `bits` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L145)
  - `embd_pdrop` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L134)
  - `gradient_checkpointing` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L146)
  - `hidden_act` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L136)
  - `hidden_size` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L124)
  - `initializer_range` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L138)
  - `intermediate_size` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L125)
  - `layer_norm_eps` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L139)
  - `layer_types` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L147)
  - `max_position_embeddings` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L137)
  - `model_type` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L89)
  - `num_attention_heads` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L127)
  - `num_hidden_layers` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L126)
  - `num_key_value_heads` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L132)
  - `partial_rotary_factor` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L143)
  - `qk_layernorm` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L144)
  - `resid_pdrop` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L133)
  - `rope_scaling` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L142)
  - `rope_theta` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L141)
  - `use_cache` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L140)
  - `vocab_size` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/phi/phi_configuration.py#L123)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`granted_freq_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_freq_max_position_embedding), [`granted_mask_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_mask_max_position_embedding), [`PhiForCausalLM`](modeling_phi.md#PhiForCausalLM), [`PhiModel`](modeling_phi.md#PhiModel), [`embed_dropout`](modeling_phi.md#PhiModel.embed_dropout), [`fc1`](modeling_phi.md#PhiMLP.fc1), [`fc2`](modeling_phi.md#PhiMLP.fc2), [`embed_tokens`](modeling_phi.md#PhiModel.embed_tokens), [`act`](modeling_phi.md#PhiMLP.act), [`final_layernorm`](modeling_phi.md#PhiModel.final_layernorm), [`input_layernorm`](modeling_phi.md#PhiDecoderLayer.input_layernorm), [`__init__`](modeling_phi.md#PhiForCausalLM.__init__), [`resid_dropout`](modeling_phi.md#PhiDecoderLayer.resid_dropout), [`__init__`](modeling_phi.md#PhiModel.__init__), [`qk_layernorm`](modeling_phi.md#PhiAttention.qk_layernorm), [`rotary_emb_dim`](modeling_phi.md#PhiAttention.rotary_emb_dim), [`__init__`](modeling_phi.md#PhiAttention.__init__), [`__init__`](modeling_phi.md#PhiDecoderLayer.__init__), [`__init__`](modeling_phi.md#PhiMLP.__init__), [`_config_class`](modeling_phi.md#PhiForCausalLM._config_class), [`attention_dropout`](modeling_phi.md#PhiAttention.attention_dropout), [`partial_rotary_factor`](modeling_phi.md#PhiAttention.partial_rotary_factor), [`vocab_size`](modeling_phi.md#PhiModel.vocab_size)

