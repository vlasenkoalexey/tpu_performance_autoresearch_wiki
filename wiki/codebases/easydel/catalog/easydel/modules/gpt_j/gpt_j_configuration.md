---
title: 'Module: easydel/modules/gpt_j/gpt_j_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/gpt_j/gpt_j_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gpt_j.gpt_j_configuration`/GPTJConfig#
symbols:
  GPTJConfig: ''
  GPTJConfig.layer_types: layer_types.
  GPTJConfig.__init__: __init__().
  GPTJConfig.n_inner: n_inner.
  GPTJConfig.resid_pdrop: resid_pdrop.
  GPTJConfig.initializer_range: initializer_range.
  GPTJConfig.n_layer: n_layer.
  GPTJConfig.rotary_dim: rotary_dim.
  GPTJConfig.activation_function: activation_function.
  GPTJConfig.attn_pdrop: attn_pdrop.
  GPTJConfig.layer_norm_epsilon: layer_norm_epsilon.
  GPTJConfig.gradient_checkpointing: gradient_checkpointing.
  GPTJConfig.model_type: model_type.
  GPTJConfig.attribute_map: attribute_map.
  GPTJConfig.bits: bits.
  GPTJConfig.vocab_size: vocab_size.
  GPTJConfig.n_positions: n_positions.
  GPTJConfig.n_embd: n_embd.
  GPTJConfig.n_head: n_head.
  GPTJConfig.embd_pdrop: embd_pdrop.
  GPTJConfig.use_cache: use_cache.
  GPTJConfig.bos_token_id: bos_token_id.
  GPTJConfig.eos_token_id: eos_token_id.
  GPTJConfig.from_pt: from_pt.
  GPTJConfig.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/gpt_j/gpt_j_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py)

## Classes
### `GPTJConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/gpt_j/gpt_j_configuration.py:26`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L26)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class GPTJConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 50400, n_positions: int = 2048, n_embd: int = 4096, n_layer: int = 28, n_head: int = 16, rotary_dim: int = 64, n_inner: int | None = None, activation_function: str = "gelu_new", resid_pdrop: float = 0, embd_pdrop: float = 0, attn_pdrop: float = 0, layer_norm_epsilon: float = 0.00001, initializer_range: int = 0.02, use_cache: int = True, bos_token_id: int = 50256, eos_token_id: int = 50256, tie_word_embeddings: bool = False, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, bits: int | None = None, layer_types: list[str] | None = None, **kwargs)` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L84) — Initializes a GPTJConfig object.
  - `get_partition_rules(self, *args, **kwargs)` — [`L163`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L163) — Returns partition rules for model sharding.
  - `activation_function` — [`L141`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L141)
  - `attn_pdrop` — [`L144`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L144)
  - `attribute_map` — [`L77`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L77)
  - `bits` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L133)
  - `bos_token_id` — [`L148`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L148)
  - `embd_pdrop` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L143)
  - `eos_token_id` — [`L149`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L149)
  - `from_pt` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L150)
  - `gradient_checkpointing` — [`L151`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L151)
  - `initializer_range` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L146)
  - `layer_norm_epsilon` — [`L145`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L145)
  - `layer_types` — [`L152`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L152)
  - `model_type` — [`L76`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L76)
  - `n_embd` — [`L136`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L136)
  - `n_head` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L138)
  - `n_inner` — [`L139`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L139)
  - `n_layer` — [`L137`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L137)
  - `n_positions` — [`L135`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L135)
  - `resid_pdrop` — [`L142`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L142)
  - `rotary_dim` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L140)
  - `use_cache` — [`L147`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L147)
  - `vocab_size` — [`L134`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt_j/gpt_j_configuration.py#L134)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`GPTJForCausalLM`](modeling_gpt_j.md#GPTJForCausalLM), [`GPTJModel`](modeling_gpt_j.md#GPTJModel), [`dropout`](modeling_gpt_j.md#GPTJModel.dropout), [`wte`](modeling_gpt_j.md#GPTJModel.wte), [`_create_attention_performer`](modeling_gpt_j.md#GPTJAttention._create_attention_performer), [`_create_rotary`](modeling_gpt_j.md#GPTJAttention._create_rotary), [`ln_1`](modeling_gpt_j.md#GPTJBlock.ln_1), [`__init__`](modeling_gpt_j.md#GPTJForCausalLM.__init__), [`config`](modeling_gpt_j.md#GPTJBlock.config), [`act`](modeling_gpt_j.md#GPTJMLP.act), [`__init__`](modeling_gpt_j.md#GPTJAttention.__init__), [`__init__`](modeling_gpt_j.md#GPTJModel.__init__), [`define_network`](modeling_gpt_j.md#GPTJAttention.define_network), [`precision`](modeling_gpt_j.md#GPTJBlock.precision), [`config`](modeling_gpt_j.md#GPTJMLP.config), [`dropout`](modeling_gpt_j.md#GPTJMLP.dropout), [`resid_dropout`](modeling_gpt_j.md#GPTJAttention.resid_dropout), [`__init__`](modeling_gpt_j.md#GPTJBlock.__init__), [`__init__`](modeling_gpt_j.md#GPTJMLP.__init__), [`_config_class`](modeling_gpt_j.md#GPTJForCausalLM._config_class), [`intermediate_size`](modeling_gpt_j.md#GPTJMLP.intermediate_size)

