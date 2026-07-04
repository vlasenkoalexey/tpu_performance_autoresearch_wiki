---
title: 'Module: easydel/modules/qwen3_5/qwen3_5_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen3_5/qwen3_5_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen3_5.qwen3_5_configuration`/
symbols:
  Qwen3_5Config.text_config: Qwen3_5Config#text_config.
  Qwen3_5TextConfig: Qwen3_5TextConfig#
  Qwen3_5Config: Qwen3_5Config#
  Qwen3_5Config.vision_config: Qwen3_5Config#vision_config.
  Qwen3_5VisionConfig: Qwen3_5VisionConfig#
  Qwen3_5TextConfig.linear_attention_separate_proj: Qwen3_5TextConfig#linear_attention_separate_proj.
  Qwen3_5TextConfig.__init__: Qwen3_5TextConfig#__init__().
  Qwen3_5Config.sub_configs: Qwen3_5Config#sub_configs.
  Qwen3_5Config.__init__: Qwen3_5Config#__init__().
  Qwen3_5Config.get_text_config: Qwen3_5Config#get_text_config().
  Qwen3_5Config.vision_end_token_id: Qwen3_5Config#vision_end_token_id.
  _normalize_rope_scaling_for_mrope: _normalize_rope_scaling_for_mrope().
  Qwen3_5VisionConfig.__init__: Qwen3_5VisionConfig#__init__().
  Qwen3_5VisionConfig.deepstack_visual_indexes: Qwen3_5VisionConfig#deepstack_visual_indexes.
  Qwen3_5Config.image_token_id: Qwen3_5Config#image_token_id.
  Qwen3_5Config.video_token_id: Qwen3_5Config#video_token_id.
  Qwen3_5Config.vision_start_token_id: Qwen3_5Config#vision_start_token_id.
  _hf_supports_mrope_rope_type: _hf_supports_mrope_rope_type().
  _has_hf_qwen3_5_text_impl: _has_hf_qwen3_5_text_impl().
  Qwen3_5TextConfig.model_type: Qwen3_5TextConfig#model_type.
  Qwen3_5TextConfig.rope_parameters: Qwen3_5TextConfig#rope_parameters.
  Qwen3_5TextConfig.is_moe_layer: Qwen3_5TextConfig#is_moe_layer().
  Qwen3_5TextConfig.get_partition_rules: Qwen3_5TextConfig#get_partition_rules().
  Qwen3_5VisionConfig.model_type: Qwen3_5VisionConfig#model_type.
  Qwen3_5VisionConfig.base_config_key: Qwen3_5VisionConfig#base_config_key.
  Qwen3_5Config.model_type: Qwen3_5Config#model_type.
  Qwen3_5Config.keys_to_ignore_at_inference: Qwen3_5Config#keys_to_ignore_at_inference.
  Qwen3_5Config.get_partition_rules: Qwen3_5Config#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/qwen3_5/qwen3_5_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py)

## Classes
### `Qwen3_5Config`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen3_5/qwen3_5_configuration.py:275`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L275)
- doc: Configuration for the Qwen3.5 multimodal (vision-language) model.
- signature: `class Qwen3_5Config(EasyDeLBaseConfig):`
- members:
  - `__init__(self, text_config: Mapping[str, typing.Any] | Qwen3_5TextConfig | None = None, vision_config: Mapping[str, typing.Any] | Qwen3_5VisionConfig | None = None, image_token_id: int = 248056, video_token_id: int = 248057, vision_start_token_id: int = 248053, vision_end_token_id: int = 248054, tie_word_embeddings: bool = False, **kwargs)` — [`L306`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L306) — Initialize Qwen3.5 composite configuration with text and vision sub-configs.
  - `get_partition_rules(self, *args, **kwargs)` — [`L345`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L345) — Returns partition rules for model sharding.
  - `get_text_config(self, decoder: bool = True)` — [`L341`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L341) — Get the text configuration object.
  - `image_token_id` — [`L335`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L335)
  - `keys_to_ignore_at_inference` — [`L304`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L304)
  - `model_type` — [`L299`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L299)
  - `sub_configs` — [`L300`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L300)
  - `text_config` — [`L322`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L322)
  - `video_token_id` — [`L336`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L336)
  - `vision_config` — [`L329`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L329)
  - `vision_end_token_id` — [`L338`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L338)
  - `vision_start_token_id` — [`L337`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L337)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_fix_parent_kws`](../../infra/base_config.md#EasyDeLBaseConfig._fix_parent_kws), [`Qwen3_5TextConfig`](qwen3_5_configuration.md#Qwen3_5TextConfig), [`Qwen3_5VisionConfig`](qwen3_5_configuration.md#Qwen3_5VisionConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__init__`](modeling_qwen3_5.md#Qwen3_5Model.__init__), [`Qwen3_5Model`](modeling_qwen3_5.md#Qwen3_5Model), [`__init__`](modeling_qwen3_5.md#Qwen3_5ForConditionalGeneration.__init__), [`Qwen3_5ForConditionalGeneration`](modeling_qwen3_5.md#Qwen3_5ForConditionalGeneration), [`language_model`](modeling_qwen3_5.md#Qwen3_5Model.language_model), [`visual`](modeling_qwen3_5.md#Qwen3_5Model.visual), [`vocab_size`](modeling_qwen3_5.md#Qwen3_5ForConditionalGeneration.vocab_size), [`_config_class`](modeling_qwen3_5.md#Qwen3_5ForConditionalGeneration._config_class)

### `Qwen3_5TextConfig`  ·  implements/extends Qwen3NextConfig
- def: [`easydel/modules/qwen3_5/qwen3_5_configuration.py:61`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L61)
- doc: Configuration objects inherit from \[`Qwen3NextConfig`\] and can be used to control the model outputs. Read
- signature: `class Qwen3_5TextConfig(Qwen3NextConfig):`
- members:
  - `__init__(self, vocab_size: int = 248320, hidden_size: int = 4096, intermediate_size: int = 12288, num_hidden_layers: int = 32, num_attention_heads: int = 16, num_key_value_heads: int = 4, head_dim: int = 256, hidden_act: str = "silu", max_position_embeddings: int = 32768, initializer_range: float = 0.02, rms_norm_eps: float = 0.000001, use_cache: bool = True, tie_word_embeddings: bool = False, rope_theta: float | None = None, rope_scaling: dict | None = None, rope_parameters: dict | None = None, attention_bias: bool = False, attention_dropout: float = 0, partial_rotary_factor: float = 0.25, layer_types: list[str] | None = None, full_attention_interval: int = 4, linear_conv_kernel_dim: int = 4, linear_key_head_dim: int = 128, linear_value_head_dim: int = 128, linear_num_key_heads: int = 16, linear_num_value_heads: int = 32, decoder_sparse_step: int = 1, moe_intermediate_size: int = 512, shared_expert_intermediate_size: int = 512, num_experts_per_tok: int = 8, num_experts: int = 256, norm_topk_prob: bool = True, output_router_logits: bool = False, router_aux_loss_coef: float = 0.001, mlp_only_layers: list[int] | None = None, linear_attention_separate_proj: bool | None = None, **kwargs)` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L129) — Initialize Qwen3.5 text config with hybrid attention and MoE parameters.
  - `get_partition_rules(self, *args, **kwargs)` — [`L234`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L234) — Returns partition rules for model sharding.
  - `is_moe_layer(self, layer_idx: int)` — [`L230`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L230) — Qwen3.5 text checkpoints are dense (no MoE FFN layers).
  - `linear_attention_separate_proj` — [`L224`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L224)
  - `model_type` — [`L127`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L127)
  - `rope_parameters` — [`L228`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L228)
- uses (calls/refs, reference-scoped): [`register_config`](../../infra/factory.md#register_config), [`Qwen3NextConfig`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig), [`_normalize_rope_scaling_for_mrope`](qwen3_5_configuration.md#_normalize_rope_scaling_for_mrope), [`__init__`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.__init__), [`_has_hf_qwen3_5_text_impl`](qwen3_5_configuration.md#_has_hf_qwen3_5_text_impl)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`Qwen3NextConfig`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig), [`Qwen3_5TextModel`](modeling_qwen3_5.md#Qwen3_5TextModel), [`Qwen3_5ForCausalLM`](modeling_qwen3_5.md#Qwen3_5ForCausalLM), [`__init__`](modeling_qwen3_5.md#Qwen3_5ForCausalLM.__init__), [`is_moe_layer`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.is_moe_layer), [`_maybe_flatten_position_ids_for_text`](modeling_qwen3_5.md#_maybe_flatten_position_ids_for_text), [`__init__`](qwen3_5_configuration.md#Qwen3_5Config.__init__), [`get_partition_rules`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.get_partition_rules), [`get_text_config`](qwen3_5_configuration.md#Qwen3_5Config.get_text_config), [`sub_configs`](qwen3_5_configuration.md#Qwen3_5Config.sub_configs), [`_config_class`](modeling_qwen3_5.md#Qwen3_5ForCausalLM._config_class)

### `Qwen3_5VisionConfig`  ·  implements/extends Qwen3VLVisionConfig
- def: [`easydel/modules/qwen3_5/qwen3_5_configuration.py:240`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L240)
- doc: Configuration for the Qwen3.5 vision encoder, inheriting from \[`Qwen3VLVisionConfig`\].
- signature: `class Qwen3_5VisionConfig(Qwen3VLVisionConfig):`
- members:
  - `__init__(self, deepstack_visual_indexes: list[int] | None = None, **kwargs)` — [`L258`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L258) — Initialize Qwen3.5 vision config with optional deepstack layer indexes.
  - `base_config_key` — [`L256`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L256)
  - `deepstack_visual_indexes` — [`L271`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L271)
  - `model_type` — [`L255`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L255)
- uses (calls/refs, reference-scoped): [`register_config`](../../infra/factory.md#register_config), [`Qwen3VLVisionConfig`](../qwen3_vl/qwen3_vl_configuration.md#Qwen3VLVisionConfig), [`__init__`](../qwen3_vl/qwen3_vl_configuration.md#Qwen3VLVisionConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`Qwen3VLVisionConfig`](../qwen3_vl/qwen3_vl_configuration.md#Qwen3VLVisionConfig), [`__init__`](qwen3_5_configuration.md#Qwen3_5Config.__init__), [`sub_configs`](qwen3_5_configuration.md#Qwen3_5Config.sub_configs)

## Functions
- `_has_hf_qwen3_5_text_impl()` — [`L55`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L55) — Whether the installed transformers version exposes Qwen3.5 text classes.
- `_hf_supports_mrope_rope_type()` — [`L29`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L29) — Check whether the installed HF rope validator supports ``rope_type='mrope'``.
- `_normalize_rope_scaling_for_mrope(rope_scaling: dict | None)` — [`L40`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L40) — Normalize mRoPE config while remaining compatible with older HF validators.

## Module values
- `__all__` — [`L350`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5/qwen3_5_configuration.py#L350)

