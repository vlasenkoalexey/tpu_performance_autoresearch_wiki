---
title: 'Module: src/vllm_torchtpu/layers/adapter/ir_ops.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/adapter/ir_ops.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.adapter.ir_ops`/
symbols:
  TPU_IR_PROVIDER: TPU_IR_PROVIDER.
  rms_norm: rms_norm().
  fused_add_rms_norm: fused_add_rms_norm().
  _normalize_fp32: _normalize_fp32().
---
# Module: [`src/vllm_torchtpu/layers/adapter/ir_ops.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/ir_ops.py)

## Functions
- <a id="_normalize_fp32"></a>`_normalize_fp32(x_f32: Tensor, weight: Tensor | None, epsilon: float, variance_size: int | None)` — [`L50`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/ir_ops.py#L50) — ``x * rsqrt(mean(x^2) + eps) * w`` entirely in FP32 (CUDA order).
- <a id="fused_add_rms_norm"></a>`fused_add_rms_norm(x: Tensor, x_residual: Tensor, weight: Tensor | None, epsilon: float, variance_size: int | None = None)` — [`L73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/ir_ops.py#L73) — Residual add rounded to the activation dtype, then FP32 RMSNorm.
- <a id="rms_norm"></a>`rms_norm(x: Tensor, weight: Tensor | None, epsilon: float, variance_size: int | None = None)` — [`L63`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/ir_ops.py#L63) — RMSNorm with the weight multiply in FP32, matching ``rms_norm_kernel``.

## Module values
- <a id="TPU_IR_PROVIDER"></a>`TPU_IR_PROVIDER` — [`L47`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/adapter/ir_ops.py#L47)

