---
title: 'Area: torchtitan/models'
type: area
area: 'torchtitan/models'
description: 'Model zoo of torchtitan: shared building blocks plus Llama3, Qwen3/3.5, DeepSeek-V3/V4, Kimi, GPT-OSS, Muse Glimmer and Flux, each with its parallelize function and recipes.'
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-10-29T06:34:20Z}
---
# Area: `torchtitan/models`

## Purpose
`torchtitan/models/` holds the shared building blocks ([model-building-blocks](../concepts/model-building-blocks.md): attention backends, MoE, linears, norms, RoPE, decoder sharding helpers) and one package per model family. Each family registers a `ModelSpec` ([model-spec-protocols](../concepts/model-spec-protocols.md)) with a config registry of recipes and a `parallelize_fn` that applies the parallelism axes.

Family pages: [llama3-model](../concepts/llama3-model.md), [qwen3-model](../concepts/qwen3-model.md), [qwen3-5-model](../concepts/qwen3-5-model.md), [deepseek-v3-model](../concepts/deepseek-v3-model.md), [deepseek-v4-model](../concepts/deepseek-v4-model.md), [kimi-k2-7-model](../concepts/kimi-k2-7-model.md), [kimi-k3-model](../concepts/kimi-k3-model.md), [gpt-oss-model](../concepts/gpt-oss-model.md), [muse-glimmer-model](../concepts/muse-glimmer-model.md), [flux-diffusion-model](../concepts/flux-diffusion-model.md). The TPU lane reuses these models unchanged and swaps kernels and `parallelize_fn` at build time ([tpu-trainer-and-job-config](../concepts/tpu-trainer-and-job-config.md)).

## How the units connect
- Every family composes [model-building-blocks](../concepts/model-building-blocks.md) and is parallelized through [parallel-dims-and-parallelization](../concepts/parallel-dims-and-parallelization.md).
- `qwen3_6` and `qwen3_8` are small config-only variants (catalog-only).
- TPU recipes for Llama3, Qwen3 and Muse Glimmer live in the TPU lane; several families (DeepSeek-V4, Kimi-K3, GPT-OSS) have no TPU recipe.

<!-- area:auto:begin -->
## Units
14 planned unit(s) in `torchtitan/models`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `torchtitan/models/common` | 20 | 638 | 670 | [`Linear`](../catalog/torchtitan/models/common/linear.md#Linear "torchtitan/models/common/linear.py:L31"), [`Config`](../catalog/torchtitan/models/common/linear.md#Linear.Config "torchtitan/models/common/linear.py:L35"), [`layers`](../catalog/torchtitan/models/common/decoder.md#Decoder.Config.layers "torchtitan/models/common/decoder.py:L84") | [model-building-blocks](../concepts/model-building-blocks.md) |
| `torchtitan/models/flux` | 19 | 504 | 18 | [`validate`](../catalog/torchtitan/models/flux/validate.md#FluxValidator.validate "torchtitan/models/flux/validate.py:L142"), [`train_step`](../catalog/torchtitan/models/flux/trainer.md#FluxTrainer.train_step "torchtitan/models/flux/trainer.py:L357"), [`forward_backward_step`](../catalog/torchtitan/models/flux/trainer.md#FluxTrainer.forward_backward_step "torchtitan/models/flux/trainer.py:L216") | [flux-diffusion-model](../concepts/flux-diffusion-model.md) |
| `torchtitan/models/qwen3_5` | 9 | 260 | 24 | [`OffsetRMSNorm`](../catalog/torchtitan/models/qwen3_5/model.md#OffsetRMSNorm "torchtitan/models/qwen3_5/model.py:L62"), [`Qwen35StateDictAdapter`](../catalog/torchtitan/models/qwen3_5/state_dict_adapter.md#Qwen35StateDictAdapter "torchtitan/models/qwen3_5/state_dict_adapter.py:L36"), [`_27b`](../catalog/torchtitan/models/qwen3_5/__init__.md#_27b "torchtitan/models/qwen3_5/__init__.py:L831") | [qwen3-5-model](../concepts/qwen3-5-model.md) |
| `torchtitan/models/deepseek_v4` | 10 | 299 | 15 | [`forward`](../catalog/torchtitan/models/deepseek_v4/model.md#DeepSeekV4Model.forward "torchtitan/models/deepseek_v4/model.py:L230"), [`from_hf`](../catalog/torchtitan/models/deepseek_v4/state_dict_adapter.md#DeepSeekV4StateDictAdapter.from_hf "torchtitan/models/deepseek_v4/state_dict_adapter.py:L203"), [`to_hf`](../catalog/torchtitan/models/deepseek_v4/state_dict_adapter.md#DeepSeekV4StateDictAdapter.to_hf "torchtitan/models/deepseek_v4/state_dict_adapter.py:L169") | [deepseek-v4-model](../concepts/deepseek-v4-model.md) |
| `torchtitan/models/kimi_k3` | 9 | 231 | 16 | [`to_hf`](../catalog/torchtitan/models/kimi_k3/state_dict_adapter.md#KimiK3StateDictAdapter.to_hf "torchtitan/models/kimi_k3/state_dict_adapter.py:L136"), [`preprocess_inputs`](../catalog/torchtitan/models/kimi_k3/model.md#KimiK3Model.preprocess_inputs "torchtitan/models/kimi_k3/model.py:L340"), [`forward`](../catalog/torchtitan/models/kimi_k3/model.md#KimiK3Model.forward "torchtitan/models/kimi_k3/model.py:L461") | [kimi-k3-model](../concepts/kimi-k3-model.md) |
| `torchtitan/models/muse_glimmer` | 7 | 206 | 14 | [`preprocess_inputs`](../catalog/torchtitan/models/muse_glimmer/model.md#MuseGlimmerModel.preprocess_inputs "torchtitan/models/muse_glimmer/model.py:L360"), [`get_attention_masks`](../catalog/torchtitan/models/muse_glimmer/model.md#MuseGlimmerModel.get_attention_masks "torchtitan/models/muse_glimmer/model.py:L534"), [`MuseGlimmerModel`](../catalog/torchtitan/models/muse_glimmer/model.md#MuseGlimmerModel "torchtitan/models/muse_glimmer/model.py:L262") | [muse-glimmer-model](../concepts/muse-glimmer-model.md) |
| `torchtitan/models/deepseek_v3` | 7 | 137 | 38 | [`Attention`](../catalog/torchtitan/models/deepseek_v3/model.md#Attention "torchtitan/models/deepseek_v3/model.py:L32"), [`from_hf`](../catalog/torchtitan/models/deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.from_hf "torchtitan/models/deepseek_v3/state_dict_adapter.py:L211"), [`to_hf`](../catalog/torchtitan/models/deepseek_v3/state_dict_adapter.md#DeepSeekV3StateDictAdapter.to_hf "torchtitan/models/deepseek_v3/state_dict_adapter.py:L152") | [deepseek-v3-model](../concepts/deepseek-v3-model.md) |
| `torchtitan/models/kimi_k2_7` | 8 | 144 | 15 | [`MoonViTEncoder`](../catalog/torchtitan/models/kimi_k2_7/vision_encoder.md#MoonViTEncoder "torchtitan/models/kimi_k2_7/vision_encoder.py:L328"), [`VisionRotaryEmbedding2D`](../catalog/torchtitan/models/kimi_k2_7/vision_encoder.md#VisionRotaryEmbedding2D "torchtitan/models/kimi_k2_7/vision_encoder.py:L234"), [`rotary_pos_emb`](../catalog/torchtitan/models/kimi_k2_7/vision_encoder.md#MoonViTEncoder.Config.rotary_pos_emb "torchtitan/models/kimi_k2_7/vision_encoder.py:L344") | [kimi-k2-7-model](../concepts/kimi-k2-7-model.md) |
| `torchtitan/models/qwen3` | 6 | 70 | 5 | [`Qwen3Model`](../catalog/torchtitan/models/qwen3/model.md#Qwen3Model "torchtitan/models/qwen3/model.py:L75"), [`from_hf`](../catalog/torchtitan/models/qwen3/state_dict_adapter.md#Qwen3StateDictAdapter.from_hf "torchtitan/models/qwen3/state_dict_adapter.py:L131"), [`to_hf`](../catalog/torchtitan/models/qwen3/state_dict_adapter.md#Qwen3StateDictAdapter.to_hf "torchtitan/models/qwen3/state_dict_adapter.py:L56") | [qwen3-model](../concepts/qwen3-model.md) |
| `torchtitan/models/gpt_oss` | 7 | 95 | 11 | [`get_attention_masks`](../catalog/torchtitan/models/gpt_oss/model.md#GptOssModel.get_attention_masks "torchtitan/models/gpt_oss/model.py:L241"), [`forward`](../catalog/torchtitan/models/gpt_oss/moe.md#GptOssGroupedExperts.forward "torchtitan/models/gpt_oss/moe.py:L96"), [`GptOssModel`](../catalog/torchtitan/models/gpt_oss/model.md#GptOssModel "torchtitan/models/gpt_oss/model.py:L195") | [gpt-oss-model](../concepts/gpt-oss-model.md) |
| `torchtitan/models/llama3` | 6 | 59 | 5 | [`Llama3Model`](../catalog/torchtitan/models/llama3/model.md#Llama3Model "torchtitan/models/llama3/model.py:L59"), [`from_hf`](../catalog/torchtitan/models/llama3/state_dict_adapter.md#Llama3StateDictAdapter.from_hf "torchtitan/models/llama3/state_dict_adapter.py:L113"), [`to_hf`](../catalog/torchtitan/models/llama3/state_dict_adapter.md#Llama3StateDictAdapter.to_hf "torchtitan/models/llama3/state_dict_adapter.py:L69") | [llama3-model](../concepts/llama3-model.md) |
| `torchtitan/models` | 2 | 18 | 40 | [`validate_converter_order`](../catalog/torchtitan/models/utils.md#validate_converter_order "torchtitan/models/utils.py:L27"), [`quadratic_attention_flops_per_token`](../catalog/torchtitan/models/utils.md#quadratic_attention_flops_per_token "torchtitan/models/utils.py:L416"), [`get_nparams_and_active_nparams`](../catalog/torchtitan/models/utils.md#get_nparams_and_active_nparams "torchtitan/models/utils.py:L480") | (registry glue; catalog-only) |
| `torchtitan/models/qwen3_6` | 2 | 10 | 0 | (internal) | section below |
| `torchtitan/models/qwen3_8` | 2 | 11 | 0 | (internal) | section below |

## Small units
### `torchtitan/models/qwen3_6`
- modules: `torchtitan/models/qwen3_6/__init__.py`, `torchtitan/models/qwen3_6/config_registry.py`
- entry points: (none - internal unit)
- hubs: [`qwen36_debugmodel_moe`](../catalog/torchtitan/models/qwen3_6/config_registry.md#qwen36_debugmodel_moe "torchtitan/models/qwen3_6/config_registry.py:L87"), [`qwen36_debugmodel`](../catalog/torchtitan/models/qwen3_6/config_registry.md#qwen36_debugmodel "torchtitan/models/qwen3_6/config_registry.py:L41"), [`qwen36_35b_a3b`](../catalog/torchtitan/models/qwen3_6/config_registry.md#qwen36_35b_a3b "torchtitan/models/qwen3_6/config_registry.py:L164")

### `torchtitan/models/qwen3_8`
- modules: `torchtitan/models/qwen3_8/__init__.py`, `torchtitan/models/qwen3_8/config_registry.py`
- entry points: (none - internal unit)
- hubs: [`qwen38_debugmodel_moe`](../catalog/torchtitan/models/qwen3_8/config_registry.md#qwen38_debugmodel_moe "torchtitan/models/qwen3_8/config_registry.py:L98"), [`qwen38_debugmodel`](../catalog/torchtitan/models/qwen3_8/config_registry.md#qwen38_debugmodel "torchtitan/models/qwen3_8/config_registry.py:L48"), [`qwen38_27b`](../catalog/torchtitan/models/qwen3_8/config_registry.md#qwen38_27b "torchtitan/models/qwen3_8/config_registry.py:L142")

<!-- area:auto:end -->
