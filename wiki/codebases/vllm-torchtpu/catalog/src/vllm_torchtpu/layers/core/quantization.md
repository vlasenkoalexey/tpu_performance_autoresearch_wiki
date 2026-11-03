---
title: 'Module: src/vllm_torchtpu/layers/core/quantization.py'
type: catalog
provenance: extracted
module: src/vllm_torchtpu/layers/core/quantization.py
status: fresh
symbol_base: scip-python python vllm-torchtpu 0.0.0 `src.vllm_torchtpu.layers.core.quantization`/
symbols:
  quantize_tensor: quantize_tensor().
  dequantize_mxfp4_packed: dequantize_mxfp4_packed().
  dequantize_tensor: dequantize_tensor().
  quantize_kv: quantize_kv().
  quantize_tensor_to_fp4: quantize_tensor_to_fp4().
  e8m0_to_fp32_bits: e8m0_to_fp32_bits().
  static_per_tensor_quantize_tensor: static_per_tensor_quantize_tensor().
  _safe_inverse_scale: _safe_inverse_scale().
  unpack_uint8_to_fp4: unpack_uint8_to_fp4().
  e8m0_to_fp32: e8m0_to_fp32().
  E8M0_MIN_EXP: E8M0_MIN_EXP.
  pack_fp4_indices: pack_fp4_indices().
  FP8_E4M3_MAX: FP8_E4M3_MAX.
  dtype_max: dtype_max().
  is_floating_dtype: is_floating_dtype().
  REQUANTIZED_BLOCK_SIZE: REQUANTIZED_BLOCK_SIZE.
  E8M0_MAX_EXP: E8M0_MAX_EXP.
  MXFP4_BLOCK_SIZE: MXFP4_BLOCK_SIZE.
  fp4_indices_to_float: fp4_indices_to_float().
---
# Module: [`src/vllm_torchtpu/layers/core/quantization.py`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py)

## Functions
- <a id="_safe_inverse_scale"></a>`_safe_inverse_scale(scale: torch.Tensor)` — [`L68`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L68) — Return 1 / scale while keeping zero-scale blocks exactly zero.
- <a id="dequantize_mxfp4_packed"></a>`dequantize_mxfp4_packed(weight_packed: torch.Tensor, scale_u8: torch.Tensor, axis: int = -1, out_dtype: torch.dtype = torch.float32)` — [`L334`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L334) — Dequantize MXFP4 packed weights to float.
- <a id="dequantize_tensor"></a>`dequantize_tensor(tensor_q: torch.Tensor, scale: torch.Tensor, axis: int | Sequence[int] = -1, out_dtype: torch.dtype = torch.float32)` — [`L195`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L195) — Dequantize a quantized tensor with block scaling.
- <a id="dtype_max"></a>`dtype_max(dtype: jnp.dtype)` — [`L59`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L59)
- <a id="e8m0_to_fp32"></a>`e8m0_to_fp32(u8: torch.Tensor)` — [`L106`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L106) — Convert e8m0 (8-bit exponent only) to float32.
- <a id="e8m0_to_fp32_bits"></a>`e8m0_to_fp32_bits(u8: torch.Tensor)` — [`L133`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L133) — Decode scale bytes on their device with the CPU ldexp result's bits.
- <a id="fp4_indices_to_float"></a>`fp4_indices_to_float(indices: torch.Tensor)` — [`L484`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L484) — Convert FP4 indices (0-15) to float values.
- <a id="is_floating_dtype"></a>`is_floating_dtype(dtype: torch.dtype)` — [`L64`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L64)
- <a id="pack_fp4_indices"></a>`pack_fp4_indices(indices: torch.Tensor)` — [`L458`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L458) — Pack FP4 indices (0-15) into uint8 (two per byte).
- <a id="quantize_kv"></a>`quantize_kv(quant_dtype: torch.dtype, key: torch.Tensor, value: torch.Tensor | None = None, k_scale: float = 1, v_scale: float = 1)` — [`L91`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L91) — Static quantize key/value tensors with per-tensor scales.
- <a id="quantize_tensor"></a>`quantize_tensor(tensor: torch.Tensor, quant_dtype: torch.dtype, axis: int = -1, block_size: int | None = None, use_ue8m0: bool = False)` — [`L245`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L245) — Quantize a tensor with block scaling. — documented in [attention-and-layer-core](../../../../../concepts/attention-and-layer-core.md)
- <a id="quantize_tensor_to_fp4"></a>`quantize_tensor_to_fp4(tensor: torch.Tensor, axis: int | Sequence[int] = -1, block_size: int = REQUANTIZED_BLOCK_SIZE)` — [`L361`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L361) — Quantize float tensor to FP4 with block scaling.
- <a id="static_per_tensor_quantize_tensor"></a>`static_per_tensor_quantize_tensor(tensor: torch.Tensor, quant_dtype: torch.dtype, scale: float)` — [`L73`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L73) — Quantize tensor with a fixed scalar scale and clamp to dtype range.
- <a id="unpack_uint8_to_fp4"></a>`unpack_uint8_to_fp4(packed: torch.Tensor)` — [`L144`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L144) — Unpack uint8 tensor containing two fp4 (e2m1) values per byte.

## Module values
- <a id="E8M0_MAX_EXP"></a>`E8M0_MAX_EXP` — [`L53`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L53)
- <a id="E8M0_MIN_EXP"></a>`E8M0_MIN_EXP` — [`L52`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L52)
- <a id="FP8_E4M3_MAX"></a>`FP8_E4M3_MAX` — [`L56`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L56)
- <a id="MXFP4_BLOCK_SIZE"></a>`MXFP4_BLOCK_SIZE` — [`L43`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L43)
- <a id="REQUANTIZED_BLOCK_SIZE"></a>`REQUANTIZED_BLOCK_SIZE` — [`L46`](../../../../../../../../raw/code/vllm-torchtpu/src/vllm_torchtpu/layers/core/quantization.py#L46)

