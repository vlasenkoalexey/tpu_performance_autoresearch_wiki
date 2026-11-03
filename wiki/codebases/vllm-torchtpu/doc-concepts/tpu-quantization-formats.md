---
title: TPU quantization formats and the quant-config dispatch
type: doc-concept
provenance: doc
source: docs/user_guide/quantization.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# TPU quantization formats and the quant-config dispatch

## Definition
vllm-torchtpu implements weight, activation and KV-cache quantization natively under
`layers/adapter/quantization/`. Per the quantization guide, quantized weights are
reshaped and packed **once at load time** (`process_weights_after_loading`) so the
Pallas matmul, attention and fused-MoE kernels run directly on the MXU's native
low-precision paths (`fp8`, and `int4`/`fp4` upcast to `fp8`) with no runtime layout
work. Self-describing Hugging Face checkpoints (a `quantization_config` in
`config.json`) are detected automatically; `--quantization` is only needed to override.
Pairing FP8 weights with `--kv-cache-dtype fp8` halves weight and KV HBM and, per the
doc, doubles MXU throughput on v6e and v7x.

## In vllm-torchtpu (grounded)
- Dispatch: [`get_tpu_quantization_config`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/__init__.md#get_tpu_quantization_config)
  maps vLLM's method name to a TPU config class and re-registers it under a `tpu-`
  prefix ([`get_tpu_quant_method`](../catalog/src/vllm_torchtpu/layers/core/quant_methods.md#get_tpu_quant_method)).
  The map at this commit:

| vLLM method name | TPU config class | Doc's name |
|---|---|---|
| (none) | [`VllmUnquantizedConfig`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/unquantized.md#VllmUnquantizedConfig) | - |
| `fp8` | [`VllmFp8Config`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md#VllmFp8Config) | `fp8` |
| `mxfp4` | [`VllmMxfp4Config`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.md#VllmMxfp4Config) | `mxfp4` |
| `modelopt_fp4` ([`NVFP4`](../catalog/src/vllm_torchtpu/layers/core/quant_methods.md#NVFP4)) | [`VllmNvfp4Config`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.md#VllmNvfp4Config) | `nvfp4` |
| `compressed-tensors` | [`VllmCompressedTensorsConfig`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors.md#VllmCompressedTensorsConfig) | `compressed-tensors` |
| `deepseek_v4_fp8` | [`VllmDeepseekV4Fp8Config`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/deepseek_v4_fp8.md#VllmDeepseekV4Fp8Config) | `deepseek_v4_fp8` |

  Any other method raises `NotImplementedError`. The platform's accepted list is
  [`TpuPlatform.supported_quantization`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.supported_quantization).
- Linear FP8: [`VllmFp8LinearMethodTPU`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md#VllmFp8LinearMethodTPU)
  ([`process_weights_after_loading`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md#VllmFp8LinearMethodTPU.process_weights_after_loading));
  MoE FP8: [`VllmFp8MoEMethodTPU`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md#VllmFp8MoEMethodTPU);
  MXFP4 MoE: [`VllmMxfp4MoEMethod`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.md#VllmMxfp4MoEMethod);
  NVFP4 MoE: [`VllmNvfp4MoEMethod`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.md#VllmNvfp4MoEMethod);
  compressed-tensors MoE: [`VllmCompressedTensorsW4A16MoEMethod`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.md#VllmCompressedTensorsW4A16MoEMethod),
  [`VllmCompressedTensorsW4ANMxfp4MoEMethod`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4an_mxfp4.md#VllmCompressedTensorsW4ANMxfp4MoEMethod).
- Load-time FP8 for *selected unquantized Linear layers* (module docstring) is a policy
  attached by
  [`attach_online_fp8`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.md#attach_online_fp8)
  from `--additional-config '{"tpu_online_fp8": {...}}'`
  ([`OnlineFp8Policy`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.md#OnlineFp8Policy):
  `targets`, `exclude`, `weight_scheme`, `weight_block_size`), checked by
  [`validate_online_fp8`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.md#validate_online_fp8).

## Doc-vs-code disagreements
- **`awq` and `gptq`** are listed as supported; at this commit neither is in the
  dispatch map (AWQ is a commented-out TODO, GPTQ absent), so both raise
  `NotImplementedError` from `get_tpu_quantization_config`.
- **`online_fp8`** is not a `--quantization` value. The plugin's online FP8 is the
  `tpu_online_fp8` additional-config policy, and `attach_online_fp8` only accepts it on
  top of an `fp8` or `modelopt_fp4` quant config. Quantizing a plain bf16 checkpoint at
  load goes through `--quantization fp8` (the non-serialized branch of
  `VllmFp8LinearMethodTPU` uses a fixed per-channel FP8 contract).
- **`nvfp4`**: NVFP4 checkpoints route through vLLM's `modelopt_fp4` method name.
- `TpuPlatform.supported_quantization` also lists `tpu_int8` and `awq`, which the
  dispatch map does not handle.

## Why it matters / when it applies
- FP8 weights + FP8 KV is the default recipe for every large model in CI (Qwen3.5,
  Qwen3-Coder, GLM-5.2, Kimi-K3, Gemma 4); NVFP4/MXFP4/W4A16 trade further HBM savings
  for 4-bit unpack cost, mostly on MoE experts.
- Because packing happens at load, the format choice changes load time and peak host
  memory, not per-step layout cost; per-step cost is set by which kernel the method
  dispatches to (see [load-time-requantization](load-time-requantization.md)).

## Connections
- Code concepts: [quantization-methods](../concepts/quantization-methods.md), [fused-moe-kernels](../concepts/fused-moe-kernels.md), [vllm-layer-adapters](../concepts/vllm-layer-adapters.md), [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md)
- Module catalogs: [quantization/__init__](../catalog/src/vllm_torchtpu/layers/adapter/quantization/__init__.md), [fp8](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md), [mxfp4](../catalog/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.md), [nvfp4](../catalog/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.md), [online_fp8](../catalog/src/vllm_torchtpu/layers/adapter/quantization/online_fp8.md), [quant_methods](../catalog/src/vllm_torchtpu/layers/core/quant_methods.md)
- Related doc-concepts: [load-time-requantization](load-time-requantization.md), [supported-models-and-feature-matrix](supported-models-and-feature-matrix.md), [dp-ep-moe-layouts](dp-ep-moe-layouts.md)

## Source
Extracted from `docs/user_guide/quantization.md` (sections 1-2, kept in place).
