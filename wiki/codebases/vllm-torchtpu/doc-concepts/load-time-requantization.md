---
title: Load-time weight requantization and small-bucket W8A16
type: doc-concept
provenance: doc
source: docs/user_guide/quantization.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Load-time weight requantization and small-bucket W8A16

## Definition
When a checkpoint's native block granularity or weight dtype is not a good fit for MXU
tiling, vllm-torchtpu can **requantize weights at load time**. The quantization guide
documents env vars for dense linear layers (`REQUANTIZE_WEIGHT_DTYPE`,
`REQUANTIZE_BLOCK_SIZE`, and `ENABLE_QUANTIZED_MATMUL_KERNEL` to dispatch to the Pallas
quantized matmul), for MoE experts (`MOE_REQUANTIZE_WEIGHT_DTYPE`,
`MOE_REQUANTIZE_BLOCK_SIZE`, e.g. `fp4` with block 512 plus
`MOE_FUSED_EP_ENABLE_W4A8=1` for W4A8 experts in the fused EP kernel), and an opt-in
**W8A16** mode for small FP8 decode steps (`TPU_FP8_LINEAR_W8A16_MAX_ROWS`).

## In vllm-torchtpu (grounded)
- Dense linear config: [`VllmQuantLinearConfig`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/configs.md#VllmQuantLinearConfig)
  captures [`ENABLE_QUANTIZED_MATMUL_KERNEL`](../catalog/src/vllm_torchtpu/envs.md#ENABLE_QUANTIZED_MATMUL_KERNEL),
  [`REQUANTIZE_BLOCK_SIZE`](../catalog/src/vllm_torchtpu/envs.md#REQUANTIZE_BLOCK_SIZE),
  [`REQUANTIZE_WEIGHT_DTYPE`](../catalog/src/vllm_torchtpu/envs.md#REQUANTIZE_WEIGHT_DTYPE)
  and the W8A16 threshold; [`_get_linear_quant_config`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md#_get_linear_quant_config)
  turns them into the target dtype/block for FP8-serialized checkpoints (load-time
  quantization of an unquantized checkpoint uses a fixed per-channel contract instead).
- MoE: [`_get_moe_quant_config`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md#_get_moe_quant_config)
  reads [`MOE_REQUANTIZE_WEIGHT_DTYPE`](../catalog/src/vllm_torchtpu/envs.md#MOE_REQUANTIZE_WEIGHT_DTYPE)
  / [`MOE_REQUANTIZE_BLOCK_SIZE`](../catalog/src/vllm_torchtpu/envs.md#MOE_REQUANTIZE_BLOCK_SIZE);
  the W4A16 compressed-tensors and NVFP4 MoE methods read them in their
  `process_weights_after_loading`
  ([`VllmCompressedTensorsW4A16MoEMethod.process_weights_after_loading`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/compressed_tensors/compressed_tensors_moe/compressed_tensors_moe_w4a16.md#VllmCompressedTensorsW4A16MoEMethod.process_weights_after_loading),
  [`VllmNvfp4MoEMethod.process_weights_after_loading`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.md#VllmNvfp4MoEMethod.process_weights_after_loading)).
  Per the envs.py comment, when `MOE_REQUANTIZE_BLOCK_SIZE` is unset, NVFP4 EP layers
  admitted to the fused EP kernel with W4A8 use the kernel's smallest supported block
  (also automatic with `MOE_FUSED_EP_KERNEL_IMPL=adaptive`).
- W4A8 prebuild: [`prebuild_fused_moe_ep`](../catalog/src/vllm_torchtpu/layers/adapter/fused_moe_ep.md#prebuild_fused_moe_ep)
  and [`_prebuild_w4a8`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.md#_prebuild_w4a8)
  read [`MOE_FUSED_EP_ENABLE_W4A8`](../catalog/src/vllm_torchtpu/envs.md#MOE_FUSED_EP_ENABLE_W4A8).
- W8A16: [`VllmFp8LinearMethodTPU.__init__`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md#VllmFp8LinearMethodTPU.__init__)
  stores [`TPU_FP8_LINEAR_W8A16_MAX_ROWS`](../catalog/src/vllm_torchtpu/envs.md#TPU_FP8_LINEAR_W8A16_MAX_ROWS);
  steps whose padded bucket is at most that many rows keep bf16 activations against FP8
  weights. Rationale from the code comment: small decode steps are weight-bandwidth
  bound, so the per-call activation abs-max + cast costs more than FP8 activations save
  (measured on v7x only). Only the per-channel FP8 path; the blockwise kernel path
  (`ENABLE_QUANTIZED_MATMUL_KERNEL=1`) and int8 weights always quantize, and if no
  compile bucket is below the threshold nothing changes.
- DeepSeek-V4 MXFP4 experts dequantize on device by default
  ([`VLLM_TPU_MXFP4_DEVICE_DEQUANT`](../catalog/src/vllm_torchtpu/envs.md#VLLM_TPU_MXFP4_DEVICE_DEQUANT),
  [`VllmDeepseekV4Mxfp4MoEMethod._dequantize_and_pad`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/mxfp4.md#VllmDeepseekV4Mxfp4MoEMethod._dequantize_and_pad)).

## Why it matters / when it applies
- Requantization lets one checkpoint be served in the kernel-preferred format (e.g.
  re-blocking FP8 for MXU tiles, or FP8 -> FP4 experts to free HBM for KV on
  DeepSeek-V4 DP16 + EP, the guide's W4A8 example).
- W8A16 is a decode-latency lever: set the threshold to the largest decode bucket.
- All of these env vars join the compile cache key and are forwarded to Ray workers
  ([`TpuPlatform.additional_env_vars`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.additional_env_vars)).
- `REQUANTIZE_WEIGHT_DTYPE` / `MOE_REQUANTIZE_WEIGHT_DTYPE` are read as raw strings
  (no registry validation), so a typo surfaces later, at weight processing.

## Connections
- Code concepts: [quantization-methods](../concepts/quantization-methods.md), [fused-moe-kernels](../concepts/fused-moe-kernels.md), [adaptive-fused-moe-kernel](../concepts/adaptive-fused-moe-kernel.md), [custom-ops](../concepts/custom-ops.md)
- Module catalogs: [fp8](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md), [configs](../catalog/src/vllm_torchtpu/layers/adapter/quantization/configs.md), [nvfp4](../catalog/src/vllm_torchtpu/layers/adapter/quantization/nvfp4.md), [fused_moe_ep](../catalog/src/vllm_torchtpu/layers/adapter/fused_moe_ep.md)
- Related doc-concepts: [tpu-quantization-formats](tpu-quantization-formats.md), [dp-ep-moe-layouts](dp-ep-moe-layouts.md), [token-padding-buckets](token-padding-buckets.md), [env-var-reference-by-subsystem](env-var-reference-by-subsystem.md)

## Source
Extracted from `docs/user_guide/quantization.md` (section 3, kept in place).
