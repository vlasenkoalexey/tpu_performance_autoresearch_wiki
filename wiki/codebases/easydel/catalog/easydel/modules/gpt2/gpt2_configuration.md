---
title: 'Module: easydel/modules/gpt2/gpt2_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/gpt2/gpt2_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.gpt2.gpt2_configuration`/GPT2Config#
symbols:
  GPT2Config: ''
  GPT2Config.layer_types: layer_types.
  GPT2Config.__init__: __init__().
  GPT2Config.layer_norm_epsilon: layer_norm_epsilon.
  GPT2Config.n_inner: n_inner.
  GPT2Config.resid_pdrop: resid_pdrop.
  GPT2Config.n_layer: n_layer.
  GPT2Config.activation_function: activation_function.
  GPT2Config.attn_pdrop: attn_pdrop.
  GPT2Config.gradient_checkpointing: gradient_checkpointing.
  GPT2Config.model_type: model_type.
  GPT2Config.keys_to_ignore_at_inference: keys_to_ignore_at_inference.
  GPT2Config.attribute_map: attribute_map.
  GPT2Config.vocab_size: vocab_size.
  GPT2Config.n_positions: n_positions.
  GPT2Config.n_embd: n_embd.
  GPT2Config.n_head: n_head.
  GPT2Config.embd_pdrop: embd_pdrop.
  GPT2Config.initializer_range: initializer_range.
  GPT2Config.summary_type: summary_type.
  GPT2Config.summary_use_proj: summary_use_proj.
  GPT2Config.summary_activation: summary_activation.
  GPT2Config.summary_first_dropout: summary_first_dropout.
  GPT2Config.summary_proj_to_labels: summary_proj_to_labels.
  GPT2Config.scale_attn_weights: scale_attn_weights.
  GPT2Config.use_cache: use_cache.
  GPT2Config.scale_attn_by_inverse_layer_idx: scale_attn_by_inverse_layer_idx.
  GPT2Config.reorder_and_upcast_attn: reorder_and_upcast_attn.
  GPT2Config.bos_token_id: bos_token_id.
  GPT2Config.eos_token_id: eos_token_id.
  GPT2Config.bits: bits.
  GPT2Config.get_partition_rules: get_partition_rules().
---
# Module: [`easydel/modules/gpt2/gpt2_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py)

## Classes
### `GPT2Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/gpt2/gpt2_configuration.py:26`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L26)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class GPT2Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 50257, n_positions: int = 1024, n_embd: int = 768, n_layer: int = 12, n_head: int = 12, n_inner: int | None = None, activation_function: str = "gelu_new", resid_pdrop: float = 0.1, embd_pdrop: float = 0.1, attn_pdrop: float = 0.1, layer_norm_epsilon: float = 0.00001, initializer_range: float = 0.02, summary_type: str = "cls_index", summary_use_proj: bool = True, summary_activation: str | None = None, summary_proj_to_labels: bool = True, summary_first_dropout: float = 0.1, scale_attn_weights: bool = True, use_cache: bool = True, bos_token_id: int = 50256, eos_token_id: int = 50256, scale_attn_by_inverse_layer_idx: bool = False, reorder_and_upcast_attn: bool = False, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, tie_word_embeddings: bool = False, bits: int | None = None, layer_types: list[str] | None = None, **kwargs)` — [`L101`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L101) — Initializes a GPT2Config object.
  - `get_partition_rules(self, *args, **kwargs)` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L202) — Returns partition rules for model sharding.
  - `activation_function` — [`L171`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L171)
  - `attn_pdrop` — [`L174`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L174)
  - `attribute_map` — [`L94`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L94)
  - `bits` — [`L190`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L190)
  - `bos_token_id` — [`L187`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L187)
  - `embd_pdrop` — [`L173`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L173)
  - `eos_token_id` — [`L188`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L188)
  - `gradient_checkpointing` — [`L189`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L189)
  - `initializer_range` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L176)
  - `keys_to_ignore_at_inference` — [`L93`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L93)
  - `layer_norm_epsilon` — [`L175`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L175)
  - `layer_types` — [`L191`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L191)
  - `model_type` — [`L92`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L92)
  - `n_embd` — [`L167`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L167)
  - `n_head` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L169)
  - `n_inner` — [`L170`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L170)
  - `n_layer` — [`L168`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L168)
  - `n_positions` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L166)
  - `reorder_and_upcast_attn` — [`L185`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L185)
  - `resid_pdrop` — [`L172`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L172)
  - `scale_attn_by_inverse_layer_idx` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L184)
  - `scale_attn_weights` — [`L182`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L182)
  - `summary_activation` — [`L179`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L179)
  - `summary_first_dropout` — [`L180`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L180)
  - `summary_proj_to_labels` — [`L181`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L181)
  - `summary_type` — [`L177`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L177)
  - `summary_use_proj` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L178)
  - `use_cache` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L183)
  - `vocab_size` — [`L165`](../../../../../../../raw/code/EasyDeL/easydel/modules/gpt2/gpt2_configuration.py#L165)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`GPT2LMHeadModel`](modeling_gpt2.md#GPT2LMHeadModel), [`GPT2Model`](modeling_gpt2.md#GPT2Model), [`dropout`](modeling_gpt2.md#GPT2Model.dropout), [`_create_attention_performer`](modeling_gpt2.md#GPT2Attention._create_attention_performer), [`resid_dropout`](modeling_gpt2.md#GPT2Attention.resid_dropout), [`ln_2`](modeling_gpt2.md#GPT2Block.ln_2), [`__init__`](modeling_gpt2.md#GPT2LMHeadModel.__init__), [`act`](modeling_gpt2.md#GPT2MLP.act), [`ln_1`](modeling_gpt2.md#GPT2Block.ln_1), [`ln_cross_attn`](modeling_gpt2.md#GPT2Block.ln_cross_attn), [`__init__`](modeling_gpt2.md#GPT2Model.__init__), [`define_network`](modeling_gpt2.md#GPT2Attention.define_network), [`precision`](modeling_gpt2.md#GPT2Block.precision), [`dropout`](modeling_gpt2.md#GPT2MLP.dropout), [`__init__`](modeling_gpt2.md#GPT2Attention.__init__), [`__init__`](modeling_gpt2.md#GPT2Block.__init__), [`__init__`](modeling_gpt2.md#GPT2MLP.__init__), [`_config_class`](modeling_gpt2.md#GPT2LMHeadModel._config_class)

