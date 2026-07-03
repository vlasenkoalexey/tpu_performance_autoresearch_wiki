---
title: 'Module: easydel/modules/mosaic_mpt/mosaic_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/mosaic_mpt/mosaic_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.mosaic_mpt.mosaic_configuration`/Mpt
symbols:
  MptConfig: Config#
  MptConfig.attn_config: Config#attn_config.
  MptConfig.layer_types: Config#layer_types.
  MptAttentionConfig: AttentionConfig#
  MptConfig.__init__: Config#__init__().
  MptAttentionConfig.attn_pdrop: AttentionConfig#attn_pdrop.
  MptAttentionConfig.from_pretrained: AttentionConfig#from_pretrained().
  MptConfig.use_bias: Config#use_bias.
  MptConfig.initializer_range: Config#initializer_range.
  MptConfig.layer_norm_epsilon: Config#layer_norm_epsilon.
  MptConfig.use_norm_bias: Config#use_norm_bias.
  MptAttentionConfig.__init__: AttentionConfig#__init__().
  MptConfig.expansion_ratio: Config#expansion_ratio.
  MptAttentionConfig.softmax_scale: AttentionConfig#softmax_scale.
  MptConfig.n_heads: Config#n_heads.
  MptAttentionConfig.alibi_bias_max: AttentionConfig#alibi_bias_max.
  MptConfig.vocab_size: Config#vocab_size.
  MptConfig.d_model: Config#d_model.
  MptConfig.gradient_checkpointing: Config#gradient_checkpointing.
  MptConfig.n_layers: Config#n_layers.
  MptAttentionConfig.attn_type: AttentionConfig#attn_type.
  MptAttentionConfig.attn_impl: AttentionConfig#attn_impl.
  MptAttentionConfig.clip_qkv: AttentionConfig#clip_qkv.
  MptAttentionConfig.prefix_lm: AttentionConfig#prefix_lm.
  MptAttentionConfig.attn_uses_sequence_id: AttentionConfig#attn_uses_sequence_id.
  MptAttentionConfig.alibi: AttentionConfig#alibi.
  MptAttentionConfig.qk_ln: AttentionConfig#qk_ln.
  MptConfig.model_type: Config#model_type.
  MptConfig.attribute_map: Config#attribute_map.
  MptConfig.use_lm_head: Config#use_lm_head.
  MptConfig.max_seq_len: Config#max_seq_len.
  MptConfig.resid_prob_drop: Config#resid_prob_drop.
  MptConfig.emb_prob_drop: Config#emb_prob_drop.
  MptConfig.norm_type: Config#norm_type.
  MptConfig.learned_pos_emb: Config#learned_pos_emb.
  MptConfig.act_fn: Config#act_fn.
  MptConfig.logit_scale: Config#logit_scale.
  MptConfig.no_bias: Config#no_bias.
  MptConfig.qk_ln: Config#qk_ln.
  MptConfig.alibi: Config#alibi.
  MptConfig.verbose: Config#verbose.
  MptConfig.embedding_fraction: Config#embedding_fraction.
  MptConfig.init_device: Config#init_device.
  MptConfig.use_cache: Config#use_cache.
  MptConfig.bits: Config#bits.
  MptConfig.from_pt: Config#from_pt.
  MptConfig._set_config_defaults: Config#_set_config_defaults().
  MptConfig.get_partition_rules: Config#get_partition_rules().
---
# Module: [`easydel/modules/mosaic_mpt/mosaic_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py)

## Classes
### `MptAttentionConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/mosaic_mpt/mosaic_configuration.py:25`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L25)
- doc: This is the configuration class to store the attention related configuration of a \[`MptModel`\].
- signature: `class MptAttentionConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, attn_type: str = "multihead_attention", attn_pdrop: float | None = 0, attn_impl: str = "torch", clip_qkv: float | None = None, softmax_scale: float | None = None, prefix_lm: bool = False, qk_ln: bool = False, attn_uses_sequence_id: bool = False, alibi: bool = True, alibi_bias_max: int = 8, **kwargs)` — [`L52`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L52) — Initializes an MptAttentionConfig object.
  - `from_pretrained(cls, pretrained_model_name_or_path, **kwargs)` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L99) — Loads attention configuration from a pretrained model configuration file.
  - `alibi` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L89)
  - `alibi_bias_max` — [`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L91)
  - `attn_impl` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L84)
  - `attn_pdrop` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L83)
  - `attn_type` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L82)
  - `attn_uses_sequence_id` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L88)
  - `clip_qkv` — [`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L85)
  - `prefix_lm` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L87)
  - `qk_ln` — [`L90`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L90)
  - `softmax_scale` — [`L86`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L86)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_set_token_in_kwargs`](../../infra/base_config.md#EasyDeLBaseConfig._set_token_in_kwargs)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`_compute_alibi_bias`](modeling_mosaic.md#MptAttention._compute_alibi_bias), [`_create_attention_performer`](modeling_mosaic.md#MptAttention._create_attention_performer), [`attn_config`](mosaic_configuration.md#MptConfig.attn_config), [`resid_dropout`](modeling_mosaic.md#MptAttention.resid_dropout), [`from_pretrained`](../../infra/base_config.md#EasyDeLBaseConfig.from_pretrained), [`dropout_rate`](modeling_mosaic.md#MptBlock.dropout_rate), [`hidden_dropout`](modeling_mosaic.md#MptMLP.hidden_dropout), [`__init__`](mosaic_configuration.md#MptConfig.__init__)

### `MptConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/mosaic_mpt/mosaic_configuration.py:118`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L118)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class MptConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, d_model: int = 2048, n_heads: int = 16, n_layers: int = 24, expansion_ratio: int = 4, max_seq_len: int = 2048, vocab_size: int = 50368, resid_prob_drop: float = 0, layer_norm_epsilon: float = 0.00001, emb_prob_drop: float = 0, learned_pos_emb: bool = True, attn_config: MptAttentionConfig | None = None, init_device: str = "cpu", logit_scale: float | str | None = None, no_bias: bool = True, verbose: int = 0, embedding_fraction: float = 1, norm_type: str = "low_precision_layernorm", use_cache: bool = False, initializer_range: float = 0.02, alibi: bool = True, use_bias: bool = False, act_fn: str = "gelu", qk_ln: bool = False, use_lm_head: bool = False, use_norm_bias: bool = False, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, bits: int | None = None, layer_types: list[str] | None = None, **kwargs)` — [`L192`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L192) — Initializes an MptConfig object.
  - `_set_config_defaults(config, config_defaults)` — [`L297`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L297) — Sets default values for missing configuration parameters.
  - `get_partition_rules(self, *args, **kwargs)` — [`L312`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L312) — Returns partition rules for model sharding.
  - `act_fn` — [`L277`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L277)
  - `alibi` — [`L281`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L281)
  - `attn_config` — [`L258`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L258)
  - `attribute_map` — [`L184`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L184)
  - `bits` — [`L287`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L287)
  - `d_model` — [`L263`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L263)
  - `emb_prob_drop` — [`L273`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L273)
  - `embedding_fraction` — [`L284`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L284)
  - `expansion_ratio` — [`L268`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L268)
  - `from_pt` — [`L289`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L289)
  - `gradient_checkpointing` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L274)
  - `init_device` — [`L285`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L285)
  - `initializer_range` — [`L283`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L283)
  - `layer_norm_epsilon` — [`L288`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L288)
  - `layer_types` — [`L290`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L290)
  - `learned_pos_emb` — [`L276`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L276)
  - `logit_scale` — [`L278`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L278)
  - `max_seq_len` — [`L269`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L269)
  - `model_type` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L183)
  - `n_heads` — [`L266`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L266)
  - `n_layers` — [`L267`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L267)
  - `no_bias` — [`L279`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L279)
  - `norm_type` — [`L275`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L275)
  - `qk_ln` — [`L280`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L280)
  - `resid_prob_drop` — [`L271`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L271)
  - `use_bias` — [`L272`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L272)
  - `use_cache` — [`L286`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L286)
  - `use_lm_head` — [`L265`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L265)
  - `use_norm_bias` — [`L264`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L264)
  - `verbose` — [`L282`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L282)
  - `vocab_size` — [`L270`](../../../../../../../raw/code/EasyDeL/easydel/modules/mosaic_mpt/mosaic_configuration.py#L270)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`MptAttentionConfig`](mosaic_configuration.md#MptAttentionConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`wte`](modeling_mosaic.md#MptModel.wte), [`MptForCausalLM`](modeling_mosaic.md#MptForCausalLM), [`MptModel`](modeling_mosaic.md#MptModel), [`config`](modeling_mosaic.md#MptMLP.config), [`_compute_alibi_bias`](modeling_mosaic.md#MptAttention._compute_alibi_bias), [`_create_attention_performer`](modeling_mosaic.md#MptAttention._create_attention_performer), [`resid_dropout`](modeling_mosaic.md#MptAttention.resid_dropout), [`__init__`](modeling_mosaic.md#MptForCausalLM.__init__), [`Wqkv`](modeling_mosaic.md#MptAttention.Wqkv), [`dropout_rate`](modeling_mosaic.md#MptBlock.dropout_rate), [`hidden_dropout`](modeling_mosaic.md#MptMLP.hidden_dropout), [`norm_1`](modeling_mosaic.md#MptBlock.norm_1), [`norm_2`](modeling_mosaic.md#MptBlock.norm_2), [`norm_f`](modeling_mosaic.md#MptModel.norm_f), [`out_proj`](modeling_mosaic.md#MptAttention.out_proj), [`down_proj`](modeling_mosaic.md#MptMLP.down_proj), [`up_proj`](modeling_mosaic.md#MptMLP.up_proj), [`__init__`](modeling_mosaic.md#MptAttention.__init__), [`__init__`](modeling_mosaic.md#MptModel.__init__), [`__init__`](modeling_mosaic.md#MptBlock.__init__), [`__init__`](modeling_mosaic.md#MptMLP.__init__), [`_config_class`](modeling_mosaic.md#MptForCausalLM._config_class), [`define_network`](modeling_mosaic.md#MptAttention.define_network)

