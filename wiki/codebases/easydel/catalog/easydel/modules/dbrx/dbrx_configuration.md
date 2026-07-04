---
title: 'Module: easydel/modules/dbrx/dbrx_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/dbrx/dbrx_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.dbrx.dbrx_configuration`/D
symbols:
  DbrxConfig: brxConfig#
  DbrxConfig.ffn_config: brxConfig#ffn_config.
  DbrxConfig.layer_types: brxConfig#layer_types.
  DbrxConfig.__init__: brxConfig#__init__().
  DbrxConfig.attn_config: brxConfig#attn_config.
  DbrxAttentionConfig: brxAttentionConfig#
  DbrxFFNConfig: brxFFNConfig#
  DbrxConfig.num_key_value_heads: brxConfig#num_key_value_heads().
  DbrxFFNConfig.from_pretrained: brxFFNConfig#from_pretrained().
  DbrxConfig.rope_parameters: brxConfig#rope_parameters.
  DbrxFFNConfig.moe_num_experts: brxFFNConfig#moe_num_experts.
  DbrxConfig.d_model: brxConfig#d_model.
  DbrxConfig.rope_theta: brxConfig#rope_theta.
  DbrxFFNConfig.ffn_hidden_size: brxFFNConfig#ffn_hidden_size.
  DbrxConfig.resid_pdrop: brxConfig#resid_pdrop.
  DbrxConfig.initializer_range: brxConfig#initializer_range.
  DbrxAttentionConfig.__init__: brxAttentionConfig#__init__().
  DbrxAttentionConfig.from_pretrained: brxAttentionConfig#from_pretrained().
  DbrxFFNConfig.__init__: brxFFNConfig#__init__().
  DbrxAttentionConfig.kv_n_heads: brxAttentionConfig#kv_n_heads.
  DbrxAttentionConfig.rope_theta: brxAttentionConfig#rope_theta.
  DbrxFFNConfig.ffn_act_fn: brxFFNConfig#ffn_act_fn.
  DbrxFFNConfig.moe_top_k: brxFFNConfig#moe_top_k.
  DbrxFFNConfig.moe_jitter_eps: brxFFNConfig#moe_jitter_eps.
  DbrxFFNConfig.moe_normalize_expert_weights: brxFFNConfig#moe_normalize_expert_weights.
  DbrxFFNConfig.uniform_expert_assignment: brxFFNConfig#uniform_expert_assignment.
  DbrxConfig.n_layers: brxConfig#n_layers.
  DbrxConfig.gradient_checkpointing: brxConfig#gradient_checkpointing.
  DBRX_PRETRAINED_CONFIG_ARCHIVE_MAP: BRX_PRETRAINED_CONFIG_ARCHIVE_MAP.
  DbrxAttentionConfig.attn_pdrop: brxAttentionConfig#attn_pdrop.
  DbrxAttentionConfig.clip_qkv: brxAttentionConfig#clip_qkv.
  DbrxFFNConfig.moe_loss_weight: brxFFNConfig#moe_loss_weight.
  DbrxConfig.model_type: brxConfig#model_type.
  DbrxConfig.attribute_map: brxConfig#attribute_map.
  DbrxConfig.n_heads: brxConfig#n_heads.
  DbrxConfig.max_seq_len: brxConfig#max_seq_len.
  DbrxConfig.vocab_size: brxConfig#vocab_size.
  DbrxConfig.emb_pdrop: brxConfig#emb_pdrop.
  DbrxConfig.use_cache: brxConfig#use_cache.
  DbrxConfig.output_router_logits: brxConfig#output_router_logits.
  DbrxConfig.router_aux_loss_coef: brxConfig#router_aux_loss_coef.
  DbrxConfig.get_partition_rules: brxConfig#get_partition_rules().
---
# Module: [`easydel/modules/dbrx/dbrx_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py)

## Classes
### `DbrxAttentionConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/dbrx/dbrx_configuration.py:30`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L30)
- doc: This is the configuration class to store the attention related configuration of a \[`DbrxModel`\].
- signature: `class DbrxAttentionConfig(EasyDeLBaseConfig):`
- members:
  - `from_pretrained(cls, pretrained_model_name_or_path: str, **kwargs: tp.Any)` — [`L66`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L66)
  - `attn_pdrop` — [`L54`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L54)
  - `clip_qkv` — [`L55`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L55)
  - `kv_n_heads` — [`L56`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L56)
  - `rope_theta` — [`L57`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L57)
- protocol/private: `__init__`[`L45`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L45)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_set_token_in_kwargs`](../../infra/base_config.md#EasyDeLBaseConfig._set_token_in_kwargs)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`from_pretrained`](../../infra/base_config.md#EasyDeLBaseConfig.from_pretrained), [`_create_rotary`](modeling_dbrx.md#DbrxAttention._create_rotary), [`__init__`](dbrx_configuration.md#DbrxConfig.__init__), [`attn_config`](dbrx_configuration.md#DbrxConfig.attn_config), [`num_key_value_heads`](dbrx_configuration.md#DbrxConfig.num_key_value_heads)

### `DbrxConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/dbrx/dbrx_configuration.py:157`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L157)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class DbrxConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, d_model: int = 2048, n_heads: int = 16, n_layers: int = 24, max_seq_len: int = 2048, vocab_size: int = 32000, resid_pdrop: float = 0, emb_pdrop: float = 0, attn_config: DbrxAttentionConfig | None = None, ffn_config: DbrxFFNConfig | None = None, use_cache: bool = True, initializer_range: float = 0.02, output_router_logits: bool = False, router_aux_loss_coef: float = 0.05, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, layer_types: list[str] | None = None, **kwargs: tp.Any)` — [`L202`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L202) — Initialize the DbrxConfig with the specified parameters.
  - `get_partition_rules(self, *args, **kwargs)` — [`L288`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L288) — Returns partition rules for model sharding.
  - `num_key_value_heads(self)` — [`L284`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L284) — Get the number of key-value heads from the attention config.
  - `attn_config` — [`L242`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L242)
  - `attribute_map` — [`L195`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L195)
  - `d_model` — [`L255`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L255)
  - `emb_pdrop` — [`L261`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L261)
  - `ffn_config` — [`L249`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L249)
  - `gradient_checkpointing` — [`L266`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L266)
  - `initializer_range` — [`L263`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L263)
  - `layer_types` — [`L267`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L267)
  - `max_seq_len` — [`L258`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L258)
  - `model_type` — [`L194`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L194)
  - `n_heads` — [`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L256)
  - `n_layers` — [`L257`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L257)
  - `output_router_logits` — [`L264`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L264)
  - `resid_pdrop` — [`L260`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L260)
  - `rope_parameters` — [`L275`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L275)
  - `rope_theta` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L274)
  - `router_aux_loss_coef` — [`L265`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L265)
  - `use_cache` — [`L262`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L262)
  - `vocab_size` — [`L259`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L259)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`DbrxAttentionConfig`](dbrx_configuration.md#DbrxAttentionConfig), [`DbrxFFNConfig`](dbrx_configuration.md#DbrxFFNConfig), [`ffn_hidden_size`](dbrx_configuration.md#DbrxFFNConfig.ffn_hidden_size), [`kv_n_heads`](dbrx_configuration.md#DbrxAttentionConfig.kv_n_heads)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__call__`](modeling_dbrx.md#DbrxExpertGLU.__call__), [`DbrxModel`](modeling_dbrx.md#DbrxModel), [`DbrxForCausalLM`](modeling_dbrx.md#DbrxForCausalLM), [`DbrxForSequenceClassification`](modeling_dbrx.md#DbrxForSequenceClassification), [`wte`](modeling_dbrx.md#DbrxModel.wte), [`rngs`](modeling_dbrx.md#DbrxExpertGLU.rngs), [`out_proj`](modeling_dbrx.md#DbrxAttention.out_proj), [`moe_jitter_eps`](modeling_dbrx.md#DbrxRouter.moe_jitter_eps), [`_create_rotary`](modeling_dbrx.md#DbrxAttention._create_rotary), [`activation_fn`](modeling_dbrx.md#DbrxExpertGLU.activation_fn), [`moe_num_experts`](modeling_dbrx.md#DbrxRouter.moe_num_experts), [`moe_top_k`](modeling_dbrx.md#DbrxRouter.moe_top_k), [`__call__`](modeling_dbrx.md#DbrxExperts.__call__), [`resid_pdrop`](modeling_dbrx.md#DbrxBlock.resid_pdrop), [`moe_normalize_expert_weights`](modeling_dbrx.md#DbrxRouter.moe_normalize_expert_weights), [`_create_attention_performer`](modeling_dbrx.md#DbrxAttention._create_attention_performer), [`uniform_expert_assignment`](modeling_dbrx.md#DbrxRouter.uniform_expert_assignment), [`__init__`](modeling_dbrx.md#DbrxForCausalLM.__init__), [`__init__`](modeling_dbrx.md#DbrxForSequenceClassification.__init__), [`Wqkv`](modeling_dbrx.md#DbrxAttention.Wqkv), [`dropout`](modeling_dbrx.md#DbrxNormAttentionNorm.dropout), [`layer`](modeling_dbrx.md#DbrxRouter.layer), [`__init__`](modeling_dbrx.md#DbrxAttention.__init__), [`__init__`](modeling_dbrx.md#DbrxModel.__init__), [`define_network`](modeling_dbrx.md#DbrxAttention.define_network), [`hidden_size`](modeling_dbrx.md#DbrxBlock.hidden_size), [`hidden_size`](modeling_dbrx.md#DbrxRouter.hidden_size), [`__init__`](modeling_dbrx.md#DbrxBlock.__init__), [`__init__`](modeling_dbrx.md#DbrxExpertGLU.__init__), [`__init__`](modeling_dbrx.md#DbrxExperts.__init__), [`__init__`](modeling_dbrx.md#DbrxFFN.__init__), [`__init__`](modeling_dbrx.md#DbrxNormAttentionNorm.__init__), [`__init__`](modeling_dbrx.md#DbrxRouter.__init__), [`_config_class`](modeling_dbrx.md#DbrxForCausalLM._config_class), [`_config_class`](modeling_dbrx.md#DbrxForSequenceClassification._config_class), [`resid_dropout`](modeling_dbrx.md#DbrxAttention.resid_dropout)

### `DbrxFFNConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/dbrx/dbrx_configuration.py:84`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L84)
- doc: This is the configuration class to store the feed forward related configuration of a \[`DbrxModel`\].
- signature: `class DbrxFFNConfig(EasyDeLBaseConfig):`
- members:
  - `from_pretrained(cls, pretrained_model_name_or_path: str, **kwargs: tp.Any)` — [`L138`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L138)
  - `ffn_act_fn` — [`L122`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L122)
  - `ffn_hidden_size` — [`L123`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L123)
  - `moe_jitter_eps` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L126)
  - `moe_loss_weight` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L127)
  - `moe_normalize_expert_weights` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L128)
  - `moe_num_experts` — [`L124`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L124)
  - `moe_top_k` — [`L125`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L125)
  - `uniform_expert_assignment` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L129)
- protocol/private: `__init__`[`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L107)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_set_token_in_kwargs`](../../infra/base_config.md#EasyDeLBaseConfig._set_token_in_kwargs)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__call__`](modeling_dbrx.md#DbrxExpertGLU.__call__), [`ffn_config`](dbrx_configuration.md#DbrxConfig.ffn_config), [`rngs`](modeling_dbrx.md#DbrxExpertGLU.rngs), [`from_pretrained`](../../infra/base_config.md#EasyDeLBaseConfig.from_pretrained), [`layer_types`](dbrx_configuration.md#DbrxConfig.layer_types), [`moe_jitter_eps`](modeling_dbrx.md#DbrxRouter.moe_jitter_eps), [`activation_fn`](modeling_dbrx.md#DbrxExpertGLU.activation_fn), [`moe_num_experts`](modeling_dbrx.md#DbrxRouter.moe_num_experts), [`moe_top_k`](modeling_dbrx.md#DbrxRouter.moe_top_k), [`__call__`](modeling_dbrx.md#DbrxExperts.__call__), [`__init__`](dbrx_configuration.md#DbrxConfig.__init__), [`moe_normalize_expert_weights`](modeling_dbrx.md#DbrxRouter.moe_normalize_expert_weights), [`uniform_expert_assignment`](modeling_dbrx.md#DbrxRouter.uniform_expert_assignment)

## Module values
- `DBRX_PRETRAINED_CONFIG_ARCHIVE_MAP` — [`L27`](../../../../../../../raw/code/EasyDeL/easydel/modules/dbrx/dbrx_configuration.py#L27)

