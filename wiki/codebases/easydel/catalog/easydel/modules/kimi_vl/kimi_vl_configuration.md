---
title: 'Module: easydel/modules/kimi_vl/kimi_vl_configuration.py'
type: catalog
provenance: extracted
module: easydel/modules/kimi_vl/kimi_vl_configuration.py
status: fresh
symbol_base: scip-python python easydel 0.0.0 `easydel.modules.kimi_vl.kimi_vl_configuration`/
symbols:
  MoonViTConfig: MoonViTConfig#
  KimiVLConfig: KimiVLConfig#
  KimiVLConfig.vision_config: KimiVLConfig#vision_config.
  KimiVLConfig.text_config: KimiVLConfig#text_config.
  KimiVLConfig.sub_configs: KimiVLConfig#sub_configs.
  KimiVLConfig.__init__: KimiVLConfig#__init__().
  KimiVLConfig.vocab_size: KimiVLConfig#vocab_size.
  KimiVLConfig.get_text_config: KimiVLConfig#get_text_config().
  MoonViTConfig.hidden_size: MoonViTConfig#hidden_size.
  MoonViTConfig.__init__: MoonViTConfig#__init__().
  MoonViTConfig.patch_size: MoonViTConfig#patch_size.
  MoonViTConfig.merge_kernel_size: MoonViTConfig#merge_kernel_size.
  MoonViTConfig.init_pos_emb_height: MoonViTConfig#init_pos_emb_height.
  MoonViTConfig.init_pos_emb_width: MoonViTConfig#init_pos_emb_width.
  MoonViTConfig.num_attention_heads: MoonViTConfig#num_attention_heads.
  MoonViTConfig.num_hidden_layers: MoonViTConfig#num_hidden_layers.
  MoonViTConfig.intermediate_size: MoonViTConfig#intermediate_size.
  KimiVLConfig.media_placeholder_token_id: KimiVLConfig#media_placeholder_token_id.
  MoonViTConfig.model_type: MoonViTConfig#model_type.
  MoonViTConfig.base_config_key: MoonViTConfig#base_config_key.
  MoonViTConfig.get_partition_rules: MoonViTConfig#get_partition_rules().
  KimiVLConfig.model_type: KimiVLConfig#model_type.
  KimiVLConfig.keys_to_ignore_at_inference: KimiVLConfig#keys_to_ignore_at_inference.
  KimiVLConfig.ignore_index: KimiVLConfig#ignore_index.
  KimiVLConfig.get_partition_rules: KimiVLConfig#get_partition_rules().
  __all__: __all__.
---
# Module: [`easydel/modules/kimi_vl/kimi_vl_configuration.py`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py)

## Classes
### `KimiVLConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/kimi_vl/kimi_vl_configuration.py:102`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L102)
- doc: Top-level configuration for the Kimi-VL vision-language model.
- signature: `class KimiVLConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L169`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L169) — Returns partition rules for model sharding.
  - `get_text_config(self, decoder: bool = True)` — [`L166`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L166)
  - `ignore_index` — [`L156`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L156)
  - `keys_to_ignore_at_inference` — [`L130`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L130)
  - `media_placeholder_token_id` — [`L157`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L157)
  - `model_type` — [`L128`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L128)
  - `sub_configs` — [`L129`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L129)
  - `text_config` — [`L150`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L150)
  - `vision_config` — [`L143`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L143)
  - `vocab_size` — [`L158`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L158)
- protocol/private: `__init__`[`L132`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L132)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__), [`_fix_parent_kws`](../../infra/base_config.md#EasyDeLBaseConfig._fix_parent_kws), [`DeepseekV3Config`](../deepseek_v3/deepseek_configuration.md#DeepseekV3Config), [`MoonViTConfig`](kimi_vl_configuration.md#MoonViTConfig)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`KimiVLForConditionalGeneration`](modeling_kimi_vl.md#KimiVLForConditionalGeneration), [`__init__`](modeling_kimi_vl.md#KimiVLForConditionalGeneration.__init__), [`__init__`](modeling_kimi_vl.md#KimiVLMultiModalProjector.__init__), [`pre_norm`](modeling_kimi_vl.md#KimiVLMultiModalProjector.pre_norm), [`vision_tower`](modeling_kimi_vl.md#KimiVLForConditionalGeneration.vision_tower), [`linear_2`](modeling_kimi_vl.md#KimiVLMultiModalProjector.linear_2), [`_config_class`](modeling_kimi_vl.md#KimiVLForConditionalGeneration._config_class)

### `MoonViTConfig`  ·  implements/extends EasyDeLBaseConfig
- def: [`easydel/modules/kimi_vl/kimi_vl_configuration.py:36`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L36)
- doc: Configuration for the MoonViT vision encoder used in Kimi-VL.
- signature: `class MoonViTConfig(EasyDeLBaseConfig):`
- members:
  - `get_partition_rules(self, *args, **kwargs)` — [`L87`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L87) — Returns partition rules for model sharding.
  - `base_config_key` — [`L63`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L63)
  - `hidden_size` — [`L83`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L83)
  - `init_pos_emb_height` — [`L79`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L79)
  - `init_pos_emb_width` — [`L80`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L80)
  - `intermediate_size` — [`L84`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L84)
  - `merge_kernel_size` — [`L85`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L85)
  - `model_type` — [`L62`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L62)
  - `num_attention_heads` — [`L81`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L81)
  - `num_hidden_layers` — [`L82`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L82)
  - `patch_size` — [`L78`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L78)
- protocol/private: `__init__`[`L65`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L65)
- uses (calls/refs, reference-scoped): [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`register_config`](../../infra/factory.md#register_config), [`__init__`](../../infra/base_config.md#EasyDeLBaseConfig.__init__)
- used by: [`_import_structure`](../../__init__.md#_import_structure), [`EasyDeLBaseConfig`](../../infra/base_config.md#EasyDeLBaseConfig), [`get_partition_rules`](../../infra/base_config.md#EasyDeLBaseConfig.get_partition_rules), [`encoder`](modeling_kimi_vl.md#MoonVitPretrainedModel.encoder), [`patch_embed`](modeling_kimi_vl.md#MoonVitPretrainedModel.patch_embed), [`__init__`](modeling_kimi_vl.md#MoonVitEncoder.__init__), [`__init__`](modeling_kimi_vl.md#KimiVLMultiModalProjector.__init__), [`pre_norm`](modeling_kimi_vl.md#KimiVLMultiModalProjector.pre_norm), [`__init__`](kimi_vl_configuration.md#KimiVLConfig.__init__), [`sub_configs`](kimi_vl_configuration.md#KimiVLConfig.sub_configs), [`merge_kernel_size`](modeling_kimi_vl.md#MoonVitPretrainedModel.merge_kernel_size), [`__init__`](modeling_kimi_vl.md#MoonVitEncoderLayer.__init__), [`__init__`](modeling_kimi_vl.md#MoonVitPretrainedModel.__init__), [`patch_size`](modeling_kimi_vl.md#MoonVitPretrainedModel.patch_size)

## Module values
- `__all__` — [`L183`](../../../../../../../raw/code/EasyDeL/easydel/modules/kimi_vl/kimi_vl_configuration.py#L183)

