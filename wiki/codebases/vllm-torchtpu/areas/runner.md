---
title: 'Area: src/vllm_torchtpu/runner'
type: area
area: 'src/vllm_torchtpu/runner'
description: 'TPUModelRunner and its managers: drives every forward at a padded shape from a precompiled bucket ladder, chunks oversized steps, prepares inputs on the host, and owns KV cache materialization, sampling, speculative-decoding and multimodal-encoder orchestration.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/runner`

## Purpose
The runner is the hot loop of TPU serving. [tpu-model-runner](../concepts/tpu-model-runner.md) owns the design: `TPUModelRunner` subclasses vLLM's `GPUModelRunner` and keeps its engine-facing contract (`execute_model`, `sample_tokens`, `profile_run`, `capture_model`, `initialize_kv_cache`). It replaces dynamic shapes and CUDA graphs with one rule: every device program runs at a shape from a small, finite ladder compiled before the first request. Token and request counts round up to buckets, and a step with more requests than the ragged-paged-attention scalar prefetch can hold runs as several forwards inside one `execute_model`. Inputs are prepared on the host into preallocated staging tensors, and startup walks the ladder with dummy forwards so serving is all cache hits.

What enters the area is the scheduler output, forwarded by the [TPU worker](worker.md). What leaves is sampled tokens and, for pipeline parallelism, stage hand-offs. On the way it builds the per-step [attention metadata](../concepts/attention-and-layer-core.md), installs the [model wrapper context](../concepts/vllm-model-patches.md), and drives the [speculative drafters](../concepts/speculative-decoding.md) and [structured decoding](structured_decoding.md).

The runner also owns KV-cache allocation. [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md) covers how the HBM budget is computed after the profile run, which post-profile reserves are subtracted, and which physical layout `initialize_kv_cache` materializes. Bucket choice, padding waste, chunk count and KV block count, the main per-step performance levers outside the kernels, are all decided in this area.

## How the units connect
One unit (13 modules) whose centre is `tpu_runner.py`, covered by [tpu-model-runner](../concepts/tpu-model-runner.md). The managers it composes:
- `kv_cache_manager.py`, `kv_cache_dsv4.py`, `kernel_block_table.py`: KV cache allocation and block tables, see [kv-cache-layout-and-hbm-budget](../concepts/kv-cache-layout-and-hbm-budget.md).
- `speculative_decoding_manager.py`: per-step drafter orchestration for [speculative-decoding](../concepts/speculative-decoding.md).
- `mm_encoder_manager.py`, `mm_video_chunking.py`: multimodal encoder scheduling.
- `tpu_runner_async_output.py`, `greedy_top_tokens.py`, `min_tokens.py`, `tpu_pooling.py`, `stage_timing.py`, `utils.py`: async output copy, sampling helpers, pooling models and per-stage timing.

The runner also builds the samplers in `layers/adapter/sample` (see [layers](layers.md)), the `StructuredDecodingManager` from [structured_decoding](structured_decoding.md), and the LoRA manager from [lora](lora.md).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/runner`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/runner` | 13 | 656 | 77 | [`device`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.device "src/vllm_torchtpu/runner/tpu_runner.py:L5513"), [`mesh`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner.mesh "src/vllm_torchtpu/runner/tpu_runner.py:L1118"), [`TPUModelRunner`](../catalog/src/vllm_torchtpu/runner/tpu_runner.md#TPUModelRunner "src/vllm_torchtpu/runner/tpu_runner.py:L642") | [tpu-model-runner](../concepts/tpu-model-runner.md) |

<!-- area:auto:end -->
