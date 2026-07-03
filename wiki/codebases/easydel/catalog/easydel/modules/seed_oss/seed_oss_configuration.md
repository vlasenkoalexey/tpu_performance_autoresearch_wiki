---
title: 'Module: easydel/modules/seed_oss/seed_oss_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/seed_oss/seed_oss_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.seed_oss.seed_oss_configuration`/
symbols:
  SeedOssConfig: SeedOssConfig#
  SeedOssConfig.mlp_bias: SeedOssConfig#mlp_bias.
  SeedOssConfig.get_mask_details: SeedOssConfig#get_mask_details().
  SeedOssConfig.hidden_size: SeedOssConfig#hidden_size.
  SeedOssConfig.rope_scaling: SeedOssConfig#rope_scaling.
  SeedOssConfig.layer_types: SeedOssConfig#layer_types.
  SeedOssConfig.__init__: SeedOssConfig#__init__().
  SeedOssConfig.bits: SeedOssConfig#bits.
  SeedOssConfig.initializer_range: SeedOssConfig#initializer_range.
  SeedOssConfig.intermediate_size: SeedOssConfig#intermediate_size.
  SeedOssConfig.sliding_window: SeedOssConfig#sliding_window.
  SeedOssConfig.rms_norm_eps: SeedOssConfig#rms_norm_eps.
  SeedOssConfig.gradient_checkpointing_targets: SeedOssConfig#gradient_checkpointing_targets.
  SeedOssConfig.num_hidden_layers: SeedOssConfig#num_hidden_layers.
  SeedOssConfig.resid_pdrop: SeedOssConfig#resid_pdrop.
  SeedOssConfig.hidden_act: SeedOssConfig#hidden_act.
  SeedOssConfig.use_scan_mlp: SeedOssConfig#use_scan_mlp.
  SeedOssConfig.scan_mlp_chunk_size: SeedOssConfig#scan_mlp_chunk_size.
  SeedOssConfig.vocab_size: SeedOssConfig#vocab_size.
  SeedOssConfig.embd_pdrop: SeedOssConfig#embd_pdrop.
  SeedOssConfig.gradient_checkpointing: SeedOssConfig#gradient_checkpointing.
  SeedOssConfig.use_sliding_window: SeedOssConfig#use_sliding_window.
  SeedOssConfig.max_window_layers: SeedOssConfig#max_window_layers.
  SeedOssConfig.attention_bias: SeedOssConfig#attention_bias.
  SeedOssConfig.model_type: SeedOssConfig#model_type.
  SeedOssConfig.num_attention_heads: SeedOssConfig#num_attention_heads.
  SeedOssConfig.num_key_value_heads: SeedOssConfig#num_key_value_heads.
  SeedOssConfig.head_dim: SeedOssConfig#head_dim.
  SeedOssConfig.max_position_embeddings: SeedOssConfig#max_position_embeddings.
  SeedOssConfig.rope_theta: SeedOssConfig#rope_theta.
  SeedOssConfig.tie_word_embeddings: SeedOssConfig#tie_word_embeddings.
  SeedOssConfig.attention_dropout: SeedOssConfig#attention_dropout.
  SeedOssConfig.use_cache: SeedOssConfig#use_cache.
  SeedOssConfig.attention_out_bias: SeedOssConfig#attention_out_bias.
  SeedOssConfig.residual_dropout: SeedOssConfig#residual_dropout.
  SeedOssConfig.scan_layers: SeedOssConfig#scan_layers.
  SeedOssConfig.get_partition_rules: SeedOssConfig#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/seed_oss/seed_oss_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py)

## Classes
### `SeedOssConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/seed_oss/seed_oss_configuration.py:27`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L27)
- doc: Configuration class for the Seed OSS decoder-only transformer.
- signature: `class SeedOssConfig(EasyDeLBaseConfig):`
- members:
  - `get_mask_details(self)` — [`L146`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L146) — Return per-layer attention mask settings.
  - `get_partition_rules(self, *args, **kwargs)` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L143)
  - `attention_bias` — [`L112`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L112)
  - `attention_dropout` — [`L104`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L104)
  - `attention_out_bias` — [`L113`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L113)
  - `bits` — [`L131`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L131)
  - `embd_pdrop` — [`L106`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L106)
  - `gradient_checkpointing` — [`L126`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L126)
  - `gradient_checkpointing_targets` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L127)
  - `head_dim` — [`L94`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L94)
  - `hidden_act` — [`L95`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L95)
  - `hidden_size` — [`L89`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L89)
  - `initializer_range` — [`L97`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L97)
  - `intermediate_size` — [`L90`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L90)
  - `layer_types` — [`L111`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L111)
  - `max_position_embeddings` — [`L96`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L96)
  - `max_window_layers` — [`L110`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L110)
  - `mlp_bias` — [`L115`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L115)
  - `model_type` — [`L40`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L40)
  - `num_attention_heads` — [`L92`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L92)
  - `num_hidden_layers` — [`L91`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L91)
  - `num_key_value_heads` — [`L93`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L93)
  - `resid_pdrop` — [`L105`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L105)
  - `residual_dropout` — [`L114`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L114)
  - `rms_norm_eps` — [`L98`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L98)
  - `rope_scaling` — [`L100`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L100)
  - `rope_theta` — [`L99`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L99)
  - `scan_layers` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L128)
  - `scan_mlp_chunk_size` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L130)
  - `sliding_window` — [`L109`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L109)
  - `tie_word_embeddings` — [`L103`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L103)
  - `use_cache` — [`L107`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L107)
  - `use_scan_mlp` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L129)
  - `use_sliding_window` — [`L108`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L108)
  - `vocab_size` — [`L88`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L88)
- protocol/private: `__init__`[`L42`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L42)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`AttnMaskDetail`](../../infra/utils.md#AttnMaskDetail), [`AttnMaskType`](../../infra/utils.md#AttnMaskType), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`from_hf`](../../infra/utils.md#AttnMaskType.from_hf)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`get_mask_details`](../../infra/base_config.md#EasyDeLBaseConfig.get_mask_details), [`__call__`](modeling_seed_oss.md#SeedOssDecoderLayer.__call__), [`_create_o_proj`](modeling_seed_oss.md#SeedOssAttention._create_o_proj), [`SeedOssForCausalLM`](modeling_seed_oss.md#SeedOssForCausalLM), [`SeedOssForSequenceClassification`](modeling_seed_oss.md#SeedOssForSequenceClassification), [`dropout`](modeling_seed_oss.md#SeedOssModel.dropout), [`embed_tokens`](modeling_seed_oss.md#SeedOssModel.embed_tokens), [`sliding_window`](modeling_seed_oss.md#SeedOssAttention.sliding_window), [`precision`](modeling_seed_oss.md#SeedOssMLP.precision), [`act_fn`](modeling_seed_oss.md#SeedOssMLP.act_fn), [`input_layernorm`](modeling_seed_oss.md#SeedOssDecoderLayer.input_layernorm), [`norm`](modeling_seed_oss.md#SeedOssModel.norm), [`post_attention_layernorm`](modeling_seed_oss.md#SeedOssDecoderLayer.post_attention_layernorm), [`__init__`](modeling_seed_oss.md#SeedOssForCausalLM.__init__), [`__init__`](modeling_seed_oss.md#SeedOssForSequenceClassification.__init__), [`SeedOssAttention`](modeling_seed_oss.md#SeedOssAttention), [`down_proj`](modeling_seed_oss.md#SeedOssMLP.down_proj), [`gate_proj`](modeling_seed_oss.md#SeedOssMLP.gate_proj), [`up_proj`](modeling_seed_oss.md#SeedOssMLP.up_proj), [`__init__`](modeling_seed_oss.md#SeedOssModel.__init__), [`layers`](modeling_seed_oss.md#SeedOssModel.layers), [`dropout`](modeling_seed_oss.md#SeedOssMLP.dropout), [`__init__`](modeling_seed_oss.md#SeedOssAttention.__init__), [`__init__`](modeling_seed_oss.md#SeedOssDecoderLayer.__init__), [`__init__`](modeling_seed_oss.md#SeedOssMLP.__init__), [`_config_class`](modeling_seed_oss.md#SeedOssForCausalLM._config_class), [`_config_class`](modeling_seed_oss.md#SeedOssForSequenceClassification._config_class), [`layer_idx`](modeling_seed_oss.md#SeedOssAttention.layer_idx)

## Module values
- `__all__` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/seed_oss/seed_oss_configuration.py#L157)

