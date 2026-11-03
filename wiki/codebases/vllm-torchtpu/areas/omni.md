---
title: 'Area: src/vllm_torchtpu/omni'
type: area
area: 'src/vllm_torchtpu/omni'
description: 'vLLM-Omni platform for TPU: a platform subclass that combines vLLM-Omni''s OmniPlatform with TpuPlatform and applies run-once performance patches for diffusion transformers (Wan2.2, LTX-2, Qwen-Image), plus diffusion attention and RoPE hooks and a TPU profiler.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/omni`

## Purpose
This area makes the plugin a platform for vLLM-Omni, the multimodal and diffusion serving stack, installed through the `omni` extra. Its single entry point, `OmniTpuPlatform`, inherits both vLLM-Omni's `OmniPlatform` and this repo's [TpuPlatform](../concepts/tpu-platform.md). It reuses all TPU device and runtime plumbing and adds only what diffusion workers need. Because vLLM-Omni spawns its own diffusion workers outside the TPU worker lifecycle, the platform applies its own run-once patches: a global set at construction, and a model-specific set when vLLM-Omni asks for a diffusion attention backend.

[omni-diffusion-support](../concepts/omni-diffusion-support.md) documents those patches. Most of them are performance fixes with measured v7x numbers. They remove per-step recompiles, layout copies and redundant fusion work that torch_tpu/XLA would otherwise emit for diffusion transformers. Attention and RoPE are routed to the Pallas diffusion kernels in [kernels](kernels.md) (`diffusion_attention`).

Nothing here is on the LLM serving path. The area matters only for diffusion and multimodal-generation workloads.

## How the units connect
One unit owned by [omni-diffusion-support](../concepts/omni-diffusion-support.md): `platform.py` (the platform class and patch triggers), `patches.py` (global and per-model patches), `attention.py` and `rope.py` (adapters onto the `diffusion_attention` splash kernel and fused q/k norm + RoPE kernel), and `profiler.py` (a TPU device profiler subclass for vLLM-Omni workers).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/omni`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/omni` | 6 | 118 | 1 | [`OmniTpuPlatform`](../catalog/src/vllm_torchtpu/omni/platform.md#OmniTpuPlatform "src/vllm_torchtpu/omni/platform.py:L30") | [omni-diffusion-support](../concepts/omni-diffusion-support.md) |

<!-- area:auto:end -->
