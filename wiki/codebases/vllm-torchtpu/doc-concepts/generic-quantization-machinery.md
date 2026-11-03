---
title: Generic quantization machinery and the quant-method recipe
type: doc-concept
provenance: doc
source: docs/developers_guide/optimization_best_practices.md
updated: 2026-10-29
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Generic quantization machinery and the quant-method recipe

## Definition
The optimization guide's quantization standard (Q-1..Q-7). Its core idea: a format is a
point in `(block_size, weight_dtype, scale_dtype)` space - mxfp4, for example, is
subchannel quantization with block 32, fp4 weights and e8m0 scales - so the code should
be **one generic subchannel implementation** parameterized by those three values, with
per-checkpoint pre-processing in front of shared linear / MoE weight processing, not a
fork per format. Numeric verification and memory validation are non-negotiable.

## In vllm-torchtpu (grounded)
- Shared numeric home `layers/core/quantization.py`:
  [`quantize_tensor`](../catalog/src/vllm_torchtpu/layers/core/quantization.md#quantize_tensor)
  takes `quant_dtype`, `axis`, `block_size` and `use_ue8m0` (e8m0 vs float32 scales),
  matching Q-1's parameter space;
  [`dequantize_tensor`](../catalog/src/vllm_torchtpu/layers/core/quantization.md#dequantize_tensor),
  [`e8m0_to_fp32`](../catalog/src/vllm_torchtpu/layers/core/quantization.md#e8m0_to_fp32),
  [`unpack_uint8_to_fp4`](../catalog/src/vllm_torchtpu/layers/core/quantization.md#unpack_uint8_to_fp4)
  and [`quantize_tensor_to_fp4`](../catalog/src/vllm_torchtpu/layers/core/quantization.md#quantize_tensor_to_fp4)
  cover the formats.
- Quant methods live in `layers/adapter/quantization/` and subclass the upstream vLLM
  method (R-3.1), e.g.
  [`VllmFp8MoEMethodTPU`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md#VllmFp8MoEMethodTPU)
  (over upstream `Fp8MoEMethod`) and
  [`VllmFp8LinearMethodTPU`](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md#VllmFp8LinearMethodTPU)
  (over `Fp8LinearMethod`); sibling modules cover mxfp4, nvfp4, online fp8 and
  compressed-tensors.
- Hardware preference is declared through the platform:
  [`TpuPlatform.fp8_dtype`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform.fp8_dtype)
  returns `float8_e5m2` on v6e (for the FP8 KV cache) and `float8_e4m3fn` otherwise (Q-7).
- Load-time requantization (Q-4) is exposed as a documented dial:
  [`REQUANTIZE_WEIGHT_DTYPE`](../catalog/src/vllm_torchtpu/envs.md#REQUANTIZE_WEIGHT_DTYPE) /
  [`REQUANTIZE_BLOCK_SIZE`](../catalog/src/vllm_torchtpu/envs.md#REQUANTIZE_BLOCK_SIZE)
  and the MoE counterparts
  [`MOE_REQUANTIZE_WEIGHT_DTYPE`](../catalog/src/vllm_torchtpu/envs.md#MOE_REQUANTIZE_WEIGHT_DTYPE) /
  [`MOE_REQUANTIZE_BLOCK_SIZE`](../catalog/src/vllm_torchtpu/envs.md#MOE_REQUANTIZE_BLOCK_SIZE).

## The rules
| ID | Rule |
|---|---|
| Q-1 | Generic machinery, not per-format forks; layer shared linear/MoE processing under per-checkpoint pre-processing |
| Q-2 | Recipe: config class -> linear method (`NotImplementedError` for MoE at first) -> `process_weights_after_loading` reshaping to TPU-friendly shapes -> `apply` dispatching to the kernel -> unit test that loads and runs a real model; home `layers/adapter/quantization/` |
| Q-3 | Before/after eval (e.g. MMLU, gsm8k) plus serving benchmark on the identical rig, exact repro commands, separate "Numeric validation" and "Performance validation" sections; layer-level test builds real vLLM layers and confirms the custom path triggers within quantization error |
| Q-4 | Requantization allowed when proven quality-neutral; deliberate approximations are options with the exact mode still available |
| Q-5 | Track scale tensors independently of weights; assert on untested granularities (odd blocks, asymmetric 2D blocks, non-divisible dims) |
| Q-6 | Memory validation via `total_hbm_used_gb` before/after (see [perf-evidence-standard](perf-evidence-standard.md)) |
| Q-7 | Dtype/scale choices are hardware-driven; state per-generation guidance; emulate missing hardware support at load time; use TPU-native stochastic rounding when requantizing; never assume fp16 -> bf16 is free |

## Why it matters / when it applies
Quantization is the biggest single lever on MXU throughput and HBM residency (P-9: w8a16
beats w16a16; ride 4-bit weights on the fp8 path). Doing it through one generic path
keeps every format on the same tuned kernels and the same load-time preprocessing
([weight-load-time-preprocessing](weight-load-time-preprocessing.md)), and the
verification rules keep a speedup from being a silent quality regression - which this
repo treats as invalid.

## Connections
- Code concepts: [quantization-methods](../concepts/quantization-methods.md),
  [fused-moe-kernels](../concepts/fused-moe-kernels.md),
  [vllm-layer-adapters](../concepts/vllm-layer-adapters.md),
  [attention-and-layer-core](../concepts/attention-and-layer-core.md)
- Module catalogs: [layers/core/quantization](../catalog/src/vllm_torchtpu/layers/core/quantization.md),
  [quantization/fp8](../catalog/src/vllm_torchtpu/layers/adapter/quantization/fp8.md),
  [envs](../catalog/src/vllm_torchtpu/envs.md)
- Related doc-concepts: [weight-load-time-preprocessing](weight-load-time-preprocessing.md),
  [kernel-hardware-resource-rules](kernel-hardware-resource-rules.md),
  [perf-evidence-standard](perf-evidence-standard.md),
  [plugin-architecture-and-kernel-bridge](plugin-architecture-and-kernel-bridge.md)

## Source
Extracted from `docs/developers_guide/optimization_best_practices.md` section 2
(kept in place).
