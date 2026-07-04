---
title: 'Module: easydel/modules/openelm/openelm_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/openelm/openelm_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.openelm.openelm_configuration`/
symbols:
  OpenELMConfig.__post_init__: OpenELMConfig#__post_init__().
  OpenELMConfig: OpenELMConfig#
  OpenELMConfig.num_kv_heads: OpenELMConfig#num_kv_heads.
  OpenELMConfig.model_dim: OpenELMConfig#model_dim.
  OpenELMConfig.layer_types: OpenELMConfig#layer_types.
  OpenELMConfig.ffn_multipliers: OpenELMConfig#ffn_multipliers.
  OpenELMConfig.num_transformer_layers: OpenELMConfig#num_transformer_layers.
  OpenELMConfig.initializer_range: OpenELMConfig#initializer_range.
  OpenELMConfig.qkv_multipliers: OpenELMConfig#qkv_multipliers.
  OpenELMConfig.num_query_heads: OpenELMConfig#num_query_heads.
  OpenELMConfig.head_dim: OpenELMConfig#head_dim.
  OpenELMConfig.__init__: OpenELMConfig#__init__().
  make_divisible: make_divisible().
  OpenELMConfig.num_gqa_groups: OpenELMConfig#num_gqa_groups.
  OpenELMConfig.bits: OpenELMConfig#bits.
  OpenELMConfig.granted_freq_max_position_embedding: OpenELMConfig#granted_freq_max_position_embedding().
  OpenELMConfig.granted_mask_max_position_embedding: OpenELMConfig#granted_mask_max_position_embedding().
  OpenELMConfig.vocab_size: OpenELMConfig#vocab_size.
  compute_heads: compute_heads().
  OpenELMConfig.max_context_length: OpenELMConfig#max_context_length.
  OpenELMConfig.normalize_qk_projections: OpenELMConfig#normalize_qk_projections.
  OpenELMConfig.rope_freq_constant: OpenELMConfig#rope_freq_constant.
  OpenELMConfig.ffn_dim_divisor: OpenELMConfig#ffn_dim_divisor.
  OpenELMConfig.ffn_with_glu: OpenELMConfig#ffn_with_glu.
  OpenELMConfig.activation_fn_name: OpenELMConfig#activation_fn_name.
  OpenELMConfig.use_scan_mlp: OpenELMConfig#use_scan_mlp.
  OpenELMConfig.scan_mlp_chunk_size: OpenELMConfig#scan_mlp_chunk_size.
  OpenELMConfig.share_input_output_layers: OpenELMConfig#share_input_output_layers.
  OpenELMConfig.model_type: OpenELMConfig#model_type.
  OpenELMConfig.attribute_map: OpenELMConfig#attribute_map.
  OpenELMConfig.normalization_layer_name: OpenELMConfig#normalization_layer_name.
  OpenELMConfig.rope_max_length: OpenELMConfig#rope_max_length.
  OpenELMConfig.use_cache: OpenELMConfig#use_cache.
  OpenELMConfig.bos_token_id: OpenELMConfig#bos_token_id.
  OpenELMConfig.eos_token_id: OpenELMConfig#eos_token_id.
  OpenELMConfig.rope_scaling: OpenELMConfig#rope_scaling.
  OpenELMConfig.gradient_checkpointing: OpenELMConfig#gradient_checkpointing.
  OpenELMConfig.get_partition_rules: OpenELMConfig#get_partition_rules().
---
# Module: [`easydel/modules/openelm/openelm_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py)

## Classes
### `OpenELMConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/openelm/openelm_configuration.py:69`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L69)
- doc: Configuration objects inherit from \[`EasyDeLBaseConfig`\] and can be used to control the model outputs. Read
- signature: `class OpenELMConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, vocab_size: int = 32000, max_context_length: int = 2048, num_transformer_layers: int = 12, model_dim: int = 2048, head_dim: int = 128, qkv_multipliers: Number | list[Number] = 1, num_query_heads: int | None = None, num_gqa_groups: int | None = 1, ffn_multipliers: Number | list[Number] = 4, ffn_with_glu: bool = True, ffn_dim_divisor: int = 256, activation_fn_name: str = "swish", normalization_layer_name: str = "rms_norm", normalize_qk_projections: bool = False, share_input_output_layers: bool = False, rope_freq_constant: int = 10000, rope_max_length: int = 4096, initializer_range: float = 0.02, use_cache: bool = True, bos_token_id: int = 1, eos_token_id: int = 2, rope_scaling: dict[str, str | float] | None = None, gradient_checkpointing: EasyDeLGradientCheckPointers = EasyDeLGradientCheckPointers.NONE, use_scan_mlp: bool = False, scan_mlp_chunk_size: int = 1024, bits: int | None = None, layer_types: list[str] | None = None, **kwargs)` — [`L140`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L140) — The __init__ function is called when the class is instantiated.
  - `__post_init__(self, **_kwargs)` — [`L258`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L258) — Performs post-initialization checks and calculations.
  - `get_partition_rules(self, *args, **kwargs)` — [`L245`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L245) — Returns partition rules for model sharding.
  - `granted_freq_max_position_embedding(self)` — [`L342`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L342) — Returns the maximum position embedding size specifically for frequency-based position embeddings.
  - `granted_mask_max_position_embedding(self)` — [`L358`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L358) — Returns the maximum position embedding size specifically for mask-based position embeddings.
  - `activation_fn_name` — [`L219`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L219)
  - `attribute_map` — [`L133`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L133)
  - `bits` — [`L229`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L229)
  - `bos_token_id` — [`L232`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L232)
  - `eos_token_id` — [`L233`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L233)
  - `ffn_dim_divisor` — [`L218`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L218)
  - `ffn_multipliers` — [`L216`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L216)
  - `ffn_with_glu` — [`L217`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L217)
  - `gradient_checkpointing` — [`L235`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L235)
  - `head_dim` — [`L213`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L213)
  - `initializer_range` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L228)
  - `layer_types` — [`L238`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L238)
  - `max_context_length` — [`L210`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L210)
  - `model_dim` — [`L212`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L212)
  - `model_type` — [`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L132)
  - `normalization_layer_name` — [`L220`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L220)
  - `normalize_qk_projections` — [`L221`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L221)
  - `num_gqa_groups` — [`L215`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L215)
  - `num_kv_heads` — [`L307`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L307)
  - `num_query_heads` — [`L225`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L225)
  - `num_transformer_layers` — [`L211`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L211)
  - `qkv_multipliers` — [`L214`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L214)
  - `rope_freq_constant` — [`L223`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L223)
  - `rope_max_length` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L224)
  - `rope_scaling` — [`L234`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L234)
  - `scan_mlp_chunk_size` — [`L237`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L237)
  - `share_input_output_layers` — [`L222`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L222)
  - `use_cache` — [`L231`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L231)
  - `use_scan_mlp` — [`L236`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L236)
  - `vocab_size` — [`L209`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L209)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`EasyDeLGradientCheckPointers`](../../infra/etils.md#EasyDeLGradientCheckPointers), [`NONE`](../../infra/etils.md#EasyDeLGradientCheckPointers.NONE), [`make_divisible`](openelm_configuration.md#make_divisible), [`compute_heads`](openelm_configuration.md#compute_heads)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__call__`](modeling_openelm.md#OpenELMDecoderLayer.__call__), [`granted_freq_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_freq_max_position_embedding), [`granted_mask_max_position_embedding`](../../infra/base_config.md#EasyDeLBaseConfig.granted_mask_max_position_embedding), [`ffn_with_glu`](modeling_openelm.md#OpenELMFeedForwardNetwork.ffn_with_glu), [`qkv_proj`](modeling_openelm.md#OpenELMMultiHeadCausalAttention.qkv_proj), [`OpenELMForCausalLM`](modeling_openelm.md#OpenELMForCausalLM), [`OpenELMModel`](modeling_openelm.md#OpenELMModel), [`head_dim`](modeling_openelm.md#OpenELMMultiHeadCausalAttention.head_dim), [`out_proj`](modeling_openelm.md#OpenELMMultiHeadCausalAttention.out_proj), [`norm`](modeling_openelm.md#OpenELMModel.norm), [`layer_idx`](modeling_openelm.md#OpenELMFeedForwardNetwork.layer_idx), [`token_embeddings`](modeling_openelm.md#OpenELMModel.token_embeddings), [`num_q_heads`](modeling_openelm.md#OpenELMMultiHeadCausalAttention.num_q_heads), [`_create_rotary`](modeling_openelm.md#OpenELMMultiHeadCausalAttention._create_rotary), [`_openelm_decoder_layer_block`](modeling_openelm.md#_openelm_decoder_layer_block), [`classifier`](modeling_openelm.md#OpenELMModel.classifier), [`proj_1`](modeling_openelm.md#OpenELMFeedForwardNetwork.proj_1), [`proj_2`](modeling_openelm.md#OpenELMFeedForwardNetwork.proj_2), [`attn_norm`](modeling_openelm.md#OpenELMDecoderLayer.attn_norm), [`ffn_norm`](modeling_openelm.md#OpenELMDecoderLayer.ffn_norm), [`num_k_heads`](modeling_openelm.md#OpenELMMultiHeadCausalAttention.num_k_heads), [`__init__`](modeling_openelm.md#OpenELMForCausalLM.__init__), [`act`](modeling_openelm.md#OpenELMFeedForwardNetwork.act), [`__init__`](modeling_openelm.md#OpenELMModel.__init__), [`num_v_heads`](modeling_openelm.md#OpenELMMultiHeadCausalAttention.num_v_heads), [`__init__`](modeling_openelm.md#OpenELMDecoderLayer.__init__), [`__init__`](modeling_openelm.md#OpenELMFeedForwardNetwork.__init__), [`__init__`](modeling_openelm.md#OpenELMMultiHeadCausalAttention.__init__), [`_config_class`](modeling_openelm.md#OpenELMForCausalLM._config_class), [`define_network`](modeling_openelm.md#OpenELMMultiHeadCausalAttention.define_network), [`num_transformer_layers`](modeling_openelm.md#OpenELMModel.num_transformer_layers), [`transformer_dim`](modeling_openelm.md#OpenELMMultiHeadCausalAttention.transformer_dim)

## Functions
- `compute_heads(model_dim: int, head_dim: int)` — [`L52`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L52) — Compute the number of heads.
- `make_divisible(v: float | int, divisor: int | None = 8, min_value: float | int | None = None)` — [`L27`](../../../../../../../raw/code/EasyDeL/easydel/modules/openelm/openelm_configuration.py#L27) — This function is taken from the original tf repo.

