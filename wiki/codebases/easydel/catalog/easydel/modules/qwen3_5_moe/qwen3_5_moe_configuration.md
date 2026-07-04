---
title: 'Module: easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.qwen3_5_moe.qwen3_5_moe_configuration`/
symbols:
  Qwen3_5MoeConfig.text_config: Qwen3_5MoeConfig#text_config.
  Qwen3_5MoeTextConfig: Qwen3_5MoeTextConfig#
  Qwen3_5MoeConfig: Qwen3_5MoeConfig#
  Qwen3_5MoeConfig.vision_config: Qwen3_5MoeConfig#vision_config.
  Qwen3_5MoeVisionConfig: Qwen3_5MoeVisionConfig#
  Qwen3_5MoeTextConfig.__init__: Qwen3_5MoeTextConfig#__init__().
  Qwen3_5MoeConfig.sub_configs: Qwen3_5MoeConfig#sub_configs.
  Qwen3_5MoeConfig.__init__: Qwen3_5MoeConfig#__init__().
  Qwen3_5MoeConfig.get_text_config: Qwen3_5MoeConfig#get_text_config().
  Qwen3_5MoeConfig.vision_end_token_id: Qwen3_5MoeConfig#vision_end_token_id.
  _normalize_rope_scaling_for_mrope: _normalize_rope_scaling_for_mrope().
  _patch_hf_qwen3_5_moe_load_balancing_loss: _patch_hf_qwen3_5_moe_load_balancing_loss().
  Qwen3_5MoeTextConfig.linear_attention_separate_proj: Qwen3_5MoeTextConfig#linear_attention_separate_proj.
  Qwen3_5MoeVisionConfig.__init__: Qwen3_5MoeVisionConfig#__init__().
  Qwen3_5MoeVisionConfig.deepstack_visual_indexes: Qwen3_5MoeVisionConfig#deepstack_visual_indexes.
  Qwen3_5MoeConfig.image_token_id: Qwen3_5MoeConfig#image_token_id.
  Qwen3_5MoeConfig.video_token_id: Qwen3_5MoeConfig#video_token_id.
  _patch_hf_qwen3_5_moe_load_balancing_loss._patched_load_balancing_loss_func: _patch_hf_qwen3_5_moe_load_balancing_loss()._patched_load_balancing_loss_func().
  Qwen3_5MoeConfig.vision_start_token_id: Qwen3_5MoeConfig#vision_start_token_id.
  _hf_supports_mrope_rope_type: _hf_supports_mrope_rope_type().
  Qwen3_5MoeTextConfig.model_type: Qwen3_5MoeTextConfig#model_type.
  Qwen3_5MoeTextConfig.rope_parameters: Qwen3_5MoeTextConfig#rope_parameters.
  Qwen3_5MoeTextConfig.get_partition_rules: Qwen3_5MoeTextConfig#get_partition_rules().
  Qwen3_5MoeVisionConfig.model_type: Qwen3_5MoeVisionConfig#model_type.
  Qwen3_5MoeVisionConfig.base_config_key: Qwen3_5MoeVisionConfig#base_config_key.
  Qwen3_5MoeConfig.model_type: Qwen3_5MoeConfig#model_type.
  Qwen3_5MoeConfig.keys_to_ignore_at_inference: Qwen3_5MoeConfig#keys_to_ignore_at_inference.
  Qwen3_5MoeConfig.get_partition_rules: Qwen3_5MoeConfig#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py)

## Classes
### `Qwen3_5MoeConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py:317`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L317)
- doc: Configuration for the Qwen3.5-MoE multimodal (vision-language) model.
- signature: `class Qwen3_5MoeConfig(EasyDeLBaseConfig):`
- members:
  - `__init__(self, text_config: Mapping[str, typing.Any] | Qwen3_5MoeTextConfig | None = None, vision_config: Mapping[str, typing.Any] | Qwen3_5MoeVisionConfig | None = None, image_token_id: int = 248056, video_token_id: int = 248057, vision_start_token_id: int = 248053, vision_end_token_id: int = 248054, tie_word_embeddings: bool = False, **kwargs)` — [`L348`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L348) — Initialize Qwen3.5-MoE composite configuration with text and vision sub-configs.
  - `get_partition_rules(self, *args, **kwargs)` — [`L387`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L387) — Returns partition rules for model sharding.
  - `get_text_config(self, decoder: bool = True)` — [`L383`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L383) — Get the text configuration object.
  - `image_token_id` — [`L377`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L377)
  - `keys_to_ignore_at_inference` — [`L346`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L346)
  - `model_type` — [`L341`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L341)
  - `sub_configs` — [`L342`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L342)
  - `text_config` — [`L364`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L364)
  - `video_token_id` — [`L378`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L378)
  - `vision_config` — [`L371`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L371)
  - `vision_end_token_id` — [`L380`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L380)
  - `vision_start_token_id` — [`L379`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L379)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_fix_parent_kws`](../../infra/base_config.md#EasyDeLBaseConfig._fix_parent_kws), [`Qwen3_5MoeTextConfig`](qwen3_5_moe_configuration.md#Qwen3_5MoeTextConfig), [`Qwen3_5MoeVisionConfig`](qwen3_5_moe_configuration.md#Qwen3_5MoeVisionConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`__init__`](modeling_qwen3_5_moe.md#Qwen3_5MoeModel.__init__), [`__init__`](modeling_qwen3_5_moe.md#Qwen3_5MoeForConditionalGeneration.__init__), [`Qwen3_5MoeModel`](modeling_qwen3_5_moe.md#Qwen3_5MoeModel), [`Qwen3_5MoeForConditionalGeneration`](modeling_qwen3_5_moe.md#Qwen3_5MoeForConditionalGeneration), [`language_model`](modeling_qwen3_5_moe.md#Qwen3_5MoeModel.language_model), [`visual`](modeling_qwen3_5_moe.md#Qwen3_5MoeModel.visual), [`vocab_size`](modeling_qwen3_5_moe.md#Qwen3_5MoeForConditionalGeneration.vocab_size), [`_config_class`](modeling_qwen3_5_moe.md#Qwen3_5MoeForConditionalGeneration._config_class)

### `Qwen3_5MoeTextConfig`  ·  implements/extends Qwen3NextConfig
- def: [`easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py:111`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L111)
- doc: Configuration objects inherit from \[`Qwen3NextConfig`\] and can be used to control the model outputs. Read
- signature: `class Qwen3_5MoeTextConfig(Qwen3NextConfig):`
- members:
  - `__init__(self, vocab_size: int = 248320, hidden_size: int = 2048, intermediate_size: int = 5632, num_hidden_layers: int = 40, num_attention_heads: int = 16, num_key_value_heads: int = 2, head_dim: int = 256, hidden_act: str = "silu", max_position_embeddings: int = 32768, initializer_range: float = 0.02, rms_norm_eps: float = 0.000001, use_cache: bool = True, tie_word_embeddings: bool = False, rope_theta: float | None = None, rope_scaling: dict | None = None, rope_parameters: dict | None = None, attention_bias: bool = False, attention_dropout: float = 0, partial_rotary_factor: float = 0.25, layer_types: list[str] | None = None, full_attention_interval: int = 4, linear_conv_kernel_dim: int = 4, linear_key_head_dim: int = 128, linear_value_head_dim: int = 128, linear_num_key_heads: int = 16, linear_num_value_heads: int = 32, decoder_sparse_step: int = 1, moe_intermediate_size: int = 512, shared_expert_intermediate_size: int = 512, num_experts_per_tok: int = 8, num_experts: int = 256, norm_topk_prob: bool = True, output_router_logits: bool = False, router_aux_loss_coef: float = 0.001, mlp_only_layers: list[int] | None = None, linear_attention_separate_proj: bool | None = None, **kwargs)` — [`L178`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L178) — Initialize Qwen3.5-MoE text config with hybrid attention and MoE parameters.
  - `get_partition_rules(self, *args, **kwargs)` — [`L276`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L276) — Returns partition rules for model sharding.
  - `linear_attention_separate_proj` — [`L270`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L270)
  - `model_type` — [`L176`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L176)
  - `rope_parameters` — [`L274`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L274)
- uses (calls/refs, reference-scoped): [`register_config`](../../infra/factory.md#register_config), [`Qwen3NextConfig`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig), [`_normalize_rope_scaling_for_mrope`](qwen3_5_moe_configuration.md#_normalize_rope_scaling_for_mrope), [`__init__`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`Qwen3NextConfig`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig), [`Qwen3_5MoeTextModel`](modeling_qwen3_5_moe.md#Qwen3_5MoeTextModel), [`Qwen3_5MoeForCausalLM`](modeling_qwen3_5_moe.md#Qwen3_5MoeForCausalLM), [`__init__`](modeling_qwen3_5_moe.md#Qwen3_5MoeForCausalLM.__init__), [`__init__`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig.__init__), [`get_partition_rules`](../qwen3_next/qwen3_next_configuration.md#Qwen3NextConfig.get_partition_rules), [`get_text_config`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig.get_text_config), [`sub_configs`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig.sub_configs), [`_config_class`](modeling_qwen3_5_moe.md#Qwen3_5MoeForCausalLM._config_class)

### `Qwen3_5MoeVisionConfig`  ·  implements/extends Qwen3VLMoeVisionConfig
- def: [`easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py:282`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L282)
- doc: Configuration for the Qwen3.5-MoE vision encoder, inheriting from \[`Qwen3VLMoeVisionConfig`\].
- signature: `class Qwen3_5MoeVisionConfig(Qwen3VLMoeVisionConfig):`
- members:
  - `__init__(self, deepstack_visual_indexes: list[int] | None = None, **kwargs)` — [`L300`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L300) — Initialize Qwen3.5-MoE vision config with optional deepstack layer indexes.
  - `base_config_key` — [`L298`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L298)
  - `deepstack_visual_indexes` — [`L313`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L313)
  - `model_type` — [`L297`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L297)
- uses (calls/refs, reference-scoped): [`register_config`](../../infra/factory.md#register_config), [`Qwen3VLMoeVisionConfig`](../qwen3_vl_moe/qwen3_vl_moe_configuration.md#Qwen3VLMoeVisionConfig), [`__init__`](../qwen3_vl_moe/qwen3_vl_moe_configuration.md#Qwen3VLMoeVisionConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`Qwen3VLMoeVisionConfig`](../qwen3_vl_moe/qwen3_vl_moe_configuration.md#Qwen3VLMoeVisionConfig), [`__init__`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig.__init__), [`sub_configs`](qwen3_5_moe_configuration.md#Qwen3_5MoeConfig.sub_configs)

## Functions
- `_hf_supports_mrope_rope_type()` — [`L28`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L28) — Check whether the installed HF rope validator supports ``rope_type='mrope'``.
- `_normalize_rope_scaling_for_mrope(rope_scaling: dict | None)` — [`L39`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L39) — Normalize mRoPE config while remaining compatible with older HF validators.
- `_patch_hf_qwen3_5_moe_load_balancing_loss()` — [`L54`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L54) — Monkey-patch the HF ``load_balancing_loss_func`` for Qwen3.5-MoE.
- `_patched_load_balancing_loss_func(gate_logits, num_experts=None, top_k=2, attention_mask=None)` — [`L74`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L74)

## Module values
- `__all__` — [`L392`](../../../../../../../raw/code/EasyDeL/easydel/modules/qwen3_5_moe/qwen3_5_moe_configuration.py#L392)

