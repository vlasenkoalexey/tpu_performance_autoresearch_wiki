---
title: 'Area: src/vllm_torchtpu/platforms'
type: area
area: 'src/vllm_torchtpu/platforms'
description: 'vLLM platform plugin entry for TorchTPU: TpuPlatform, a startup-time config compiler that rewrites a GPU-shaped vLLM config into a TPU-servable one (compile mode, token-bucket ladder, dtype, executor, backends) and validates PP/PCP support.'
updated: 2026-11-03
generated: {by: wikify/0.4.1, at: 2026-11-03T02:35:38Z}
---
# Area: `src/vllm_torchtpu/platforms`

## Purpose
vLLM discovers hardware through platform plugins, and this area is the plugin entry this repo registers in `pyproject.toml`. [tpu-platform](../concepts/tpu-platform.md) owns the mechanism. `TpuPlatform` is a class of classmethods that vLLM calls at fixed points: device identity, distributed backend, attention backend, compile backend, Punica wrapper, and above all `check_and_update_config`.

The key design idea is that the platform is a startup-time config compiler, not a runtime layer. `check_and_update_config` runs once in every process that builds a `VllmConfig`. It forces whole-graph `VLLM_COMPILE`, replaces CUDA-graph capture sizes with a ladder of token buckets (one compiled TPU program each), forces bf16, picks the [executor](executors.md) and worker class, seeds the TorchTPU bootstrap environment, and runs static validators for pipeline and prefill-context parallelism. Every later performance property of the run, including bucket granularity, padding waste, compile count and which attention backend and KV layout are used, is fixed here.

So this area feeds almost every other area: the [compiler adaptor](compilation.md) gets its bucket ladder, the [runner](runner.md) its padding rules, and the [layers](layers.md) their attention backend choice.

## How the units connect
All five modules are covered by [tpu-platform](../concepts/tpu-platform.md): `__init__.py` (`register_tpu_platform`, the entry point vLLM calls during import), `tpu_platform.py` (`TpuPlatform` and its config rewriting), `tpu_block_size_utils.py` (KV block-size choice and `unified_kv_layout_enabled`, the switch for the unified KV pool), and the static validators `pcp_validation.py` and `pp_validation.py`. The platform also names the runtime pieces other areas implement: `TPUWorker` from [worker](worker.md), `PunicaWrapperTPU` from [lora](lora.md), and the compiler adaptor from [compilation-and-graph-capture](../concepts/compilation-and-graph-capture.md).

<!-- area:auto:begin -->
## Units
1 planned unit(s) in `src/vllm_torchtpu/platforms`; deep units have their own mechanism page, the rest are sections below.

| Unit | Modules | Symbols | Callers outside | Entry points | Page |
|---|---|---|---|---|---|
| `src/vllm_torchtpu/platforms` | 5 | 155 | 25 | [`TpuPlatform`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform "src/vllm_torchtpu/platforms/tpu_platform.py:L453"), [`unified_kv_layout_enabled`](../catalog/src/vllm_torchtpu/platforms/tpu_block_size_utils.md#unified_kv_layout_enabled "src/vllm_torchtpu/platforms/tpu_block_size_utils.py:L54"), [`_find_non_ssm_backend`](../catalog/src/vllm_torchtpu/platforms/tpu_platform.md#TpuPlatform._find_non_ssm_backend "src/vllm_torchtpu/platforms/tpu_platform.py:L1249") | [tpu-platform](../concepts/tpu-platform.md) |

<!-- area:auto:end -->
