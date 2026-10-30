---
title: 'Module: torchtitan/protocols/sharding.py'
type: catalog
provenance: extracted
module: torchtitan/protocols/sharding.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.protocols.sharding`/
symbols:
  ShardingConfig: ShardingConfig#
  ShardingConfig.state_shardings: ShardingConfig#state_shardings.
  ShardingConfig.in_src_shardings: ShardingConfig#in_src_shardings.
  ShardingConfig.out_src_shardings: ShardingConfig#out_src_shardings.
  ShardingConfig.in_dst_shardings: ShardingConfig#in_dst_shardings.
  ShardingConfig.out_dst_shardings: ShardingConfig#out_dst_shardings.
  LocalMapConfig: LocalMapConfig#
  resolve_placements: resolve_placements().
  ShardingConfig.local_map: ShardingConfig#local_map.
  LocalMapConfig.in_grad_placements: LocalMapConfig#in_grad_placements.
  __all__: __all__.
  LocalMapConfig.to_dict: LocalMapConfig#to_dict().
  ShardingConfig.to_dict: ShardingConfig#to_dict().
---
# Module: [`torchtitan/protocols/sharding.py`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py)

## Classes
### <a id="LocalMapConfig"></a>`LocalMapConfig`
- def: [`torchtitan/protocols/sharding.py:34`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L34) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
- doc: Spec for modules computing on local tensors.
- signature: `class LocalMapConfig:`
- members:
  - <a id="LocalMapConfig.to_dict"></a>`to_dict(self)` — [`L55`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L55)
  - <a id="LocalMapConfig.in_grad_placements"></a>`in_grad_placements` — [`L53`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L53)
- used by: [`set_vision_transformer_block_sharding_config`](../models/common/vision_encoder_sharding.md#set_vision_transformer_block_sharding_config), [`set_muse_glimmer_vision_sharding_config`](../models/muse_glimmer/sharding.md#set_muse_glimmer_vision_sharding_config), [`_set_deltanet_sharding`](../models/qwen3_5/sharding.md#_set_deltanet_sharding), [`set_qwen35_sharding_config`](../models/qwen3_5/sharding.md#set_qwen35_sharding_config), [`set_hf_sharding_configs`](../experiments/transformers_modeling_backend/hf_sharding.md#set_hf_sharding_configs), [`set_decoder_sharding_config`](../models/common/decoder_sharding.md#set_decoder_sharding_config), [`_shard_decoder_after_embedding_scatter`](../models/kimi_k2_7/sharding.md#_shard_decoder_after_embedding_scatter), [`vision_scaled_bias_rowwise_config`](../models/common/vision_encoder_sharding.md#vision_scaled_bias_rowwise_config), [`_attach_flex_kernel`](../experiments/transformers_modeling_backend/hf_sharding.md#_attach_flex_kernel), [`_routed_experts_sharding_configs`](../models/common/moe_sharding.md#_routed_experts_sharding_configs), [`set_gqa_inner_attention_local_map`](../models/common/decoder_sharding.md#set_gqa_inner_attention_local_map), [`triton_offset_rmsnorm`](../overrides/offset_rmsnorm.md#triton_offset_rmsnorm), [`_set_inner_kda_sharding`](../models/kimi_k3/sharding.md#_set_inner_kda_sharding), [`scaled_bias_rowwise_config`](../models/gpt_oss/sharding.md#scaled_bias_rowwise_config), [`set_dsa_flex_attention_sharding`](../models/deepseek_v4/sharding.md#set_dsa_flex_attention_sharding), [`build`](../components/quantization/nvfp4.md#NVFP4Linear.Config.build), [`set_flux_inner_attention_local_map`](../models/flux/sharding.md#set_flux_inner_attention_local_map), [`local_map`](sharding.md#ShardingConfig.local_map), [`_apply_local_map`](module.md#Module._apply_local_map)

### <a id="ShardingConfig"></a>`ShardingConfig`
- def: [`torchtitan/protocols/sharding.py:60`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L60) — documented in [config-overrides](../../../concepts/config-overrides.md)
- doc: Declarative sharding for a Module's states and activations.
- signature: `class ShardingConfig:`
- members:
  - <a id="ShardingConfig.to_dict"></a>`to_dict(self)` — [`L115`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L115) — Serialize for JSON logging. Placements become repr strings.
  - <a id="ShardingConfig.in_dst_shardings"></a>`in_dst_shardings` — [`L110`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L110) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
  - <a id="ShardingConfig.in_src_shardings"></a>`in_src_shardings` — [`L109`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L109) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
  - <a id="ShardingConfig.local_map"></a>`local_map` — [`L113`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L113) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
  - <a id="ShardingConfig.out_dst_shardings"></a>`out_dst_shardings` — [`L112`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L112) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
  - <a id="ShardingConfig.out_src_shardings"></a>`out_src_shardings` — [`L111`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L111) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
  - <a id="ShardingConfig.state_shardings"></a>`state_shardings` — [`L108`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L108) — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)
- uses (calls/refs, reference-scoped): [`LocalMapConfig`](sharding.md#LocalMapConfig)
- used by: [`sharding_config`](module.md#Module.Config.sharding_config), [`_set_deepseek_v3_layer_sharding`](../models/deepseek_v3/sharding.md#_set_deepseek_v3_layer_sharding), [`set_vision_transformer_block_sharding_config`](../models/common/vision_encoder_sharding.md#set_vision_transformer_block_sharding_config), [`set_deepseek_v4_layer_sharding`](../models/deepseek_v4/sharding.md#set_deepseek_v4_layer_sharding), [`_set_muse_glimmer_layer_sharding`](../models/muse_glimmer/sharding.md#_set_muse_glimmer_layer_sharding), [`set_muse_glimmer_vision_sharding_config`](../models/muse_glimmer/sharding.md#set_muse_glimmer_vision_sharding_config), [`_set_deltanet_sharding`](../models/qwen3_5/sharding.md#_set_deltanet_sharding), [`_set_qwen3_layer_sharding`](../models/qwen3/sharding.md#_set_qwen3_layer_sharding), [`_set_gpt_oss_layer_sharding`](../models/gpt_oss/sharding.md#_set_gpt_oss_layer_sharding), [`set_deepseek_v4_sharding_config`](../models/deepseek_v4/sharding.md#set_deepseek_v4_sharding_config), [`set_qwen35_sharding_config`](../models/qwen3_5/sharding.md#set_qwen35_sharding_config), [`build_and_swap_native_moe`](../experiments/transformers_modeling_backend/moe_replacement.md#build_and_swap_native_moe), [`_set_full_attention_sharding`](../models/qwen3_5/sharding.md#_set_full_attention_sharding), [`_set_vision_encoder_sharding`](../models/qwen3_5/sharding.md#_set_vision_encoder_sharding), [`set_gqa_attention_sharding`](../models/common/decoder_sharding.md#set_gqa_attention_sharding), [`set_hf_sharding_configs`](../experiments/transformers_modeling_backend/hf_sharding.md#set_hf_sharding_configs), [`set_decoder_sharding_config`](../models/common/decoder_sharding.md#set_decoder_sharding_config), [`_shard_decoder_after_embedding_scatter`](../models/kimi_k2_7/sharding.md#_shard_decoder_after_embedding_scatter), [`vision_scaled_bias_rowwise_config`](../models/common/vision_encoder_sharding.md#vision_scaled_bias_rowwise_config), [`set_dense_ffn_sharding`](../models/common/decoder_sharding.md#set_dense_ffn_sharding), [`_attach_flex_kernel`](../experiments/transformers_modeling_backend/hf_sharding.md#_attach_flex_kernel), [`_routed_experts_sharding_configs`](../models/common/moe_sharding.md#_routed_experts_sharding_configs), [`set_deepseek_v4_attention_sharding`](../models/deepseek_v4/sharding.md#set_deepseek_v4_attention_sharding), [`set_gqa_inner_attention_local_map`](../models/common/decoder_sharding.md#set_gqa_inner_attention_local_map), [`norm_config`](../models/common/decoder_sharding.md#norm_config), [`triton_offset_rmsnorm`](../overrides/offset_rmsnorm.md#triton_offset_rmsnorm), [`_set_deepseek_v3_mtp_sharding`](../models/deepseek_v3/sharding.md#_set_deepseek_v3_mtp_sharding), [`colwise_config`](../models/common/decoder_sharding.md#colwise_config), [`_set_inner_kda_sharding`](../models/kimi_k3/sharding.md#_set_inner_kda_sharding), [`invariant_norm_config`](../models/common/vision_encoder_sharding.md#invariant_norm_config), [`scaled_bias_rowwise_config`](../models/gpt_oss/sharding.md#scaled_bias_rowwise_config), [`vision_invariant_linear_config`](../models/common/vision_encoder_sharding.md#vision_invariant_linear_config), [`_maybe_wrap_with_local_region`](module.md#Module._maybe_wrap_with_local_region), [`_redistribute_inputs`](module.md#Module._redistribute_inputs), [`_set_layer_sharding_configs`](../experiments/transformers_modeling_backend/hf_sharding.md#_set_layer_sharding_configs), [`_set_multimodal_sharding`](../models/muse_glimmer/sharding.md#_set_multimodal_sharding), [`_set_vision_encoder_sharding`](../models/kimi_k2_7/sharding.md#_set_vision_encoder_sharding), [`_distribute_states`](module.md#Module._distribute_states), [`rowwise_config`](../models/common/decoder_sharding.md#rowwise_config), [`_moe_sharding_config`](../models/common/moe_sharding.md#_moe_sharding_config)  (+27 more; 2 test-only)

## Functions
- <a id="resolve_placements"></a>`resolve_placements(layout: SpmdType, mesh: DeviceMesh)` — [`L120`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L120) — Resolve an SPMD type against a mesh in axis order. — documented in [model-spec-protocols](../../../concepts/model-spec-protocols.md)

## Module values
- <a id="__all__"></a>`__all__` — [`L26`](../../../../../../raw/code/torchtitan/torchtitan/protocols/sharding.py#L26)

