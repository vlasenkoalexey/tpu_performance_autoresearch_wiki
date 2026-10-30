---
title: 'Module: torchtitan/components/quantization/mxfp8/tensor.py'
type: catalog
provenance: extracted
module: torchtitan/components/quantization/mxfp8/tensor.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.quantization.mxfp8.tensor`/
symbols:
  _quantize_mxfp8_weight: _quantize_mxfp8_weight().
  _LinearShardedTensorWithMXFP8Compute._build_operands: _LinearShardedTensorWithMXFP8Compute#_build_operands().
  _MXFP8_BLOCK_SIZE: _MXFP8_BLOCK_SIZE.
  _LinearShardedTensorWithMXFP8Compute: _LinearShardedTensorWithMXFP8Compute#
  _MXFP8LinearOperands.weight_qdata_dgrad_NK: _MXFP8LinearOperands#weight_qdata_dgrad_NK.
  _MXFP8LinearOperands: _MXFP8LinearOperands#
  _MXFP8LinearOperands.weight_scale_fprop_swizzled: _MXFP8LinearOperands#weight_scale_fprop_swizzled.
  _MXFP8LinearOperands.weight_scale_dgrad_swizzled: _MXFP8LinearOperands#weight_scale_dgrad_swizzled.
  _MXFP8LinearOperands.weight_qdata_fprop_KN: _MXFP8LinearOperands#weight_qdata_fprop_KN().
  __all__.__all__: __all__.__all__.
---
# Module: [`torchtitan/components/quantization/mxfp8/tensor.py`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/tensor.py)

## Classes
### <a id="_LinearShardedTensorWithMXFP8Compute"></a>`_LinearShardedTensorWithMXFP8Compute`  ·  implements/extends _ShardedFSDPTensor
- def: [`torchtitan/components/quantization/mxfp8/tensor.py:83`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/tensor.py#L83)
- doc: The persistent BF16 linear parameter; quantizes to MXFP8 on unshard.
- signature: `class _LinearShardedTensorWithMXFP8Compute(_ShardedFSDPTensor):`
- protocol/private: <a id="_LinearShardedTensorWithMXFP8Compute._build_operands"></a>`_build_operands`[`L92`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/tensor.py#L92)
- uses (calls/refs, reference-scoped): [`_quantize_mxfp8_weight`](tensor.md#_quantize_mxfp8_weight), [`_ShardedFSDPTensor`](../_fsdp_tensor.md#_ShardedFSDPTensor), [`weight_qdata_dgrad_NK`](tensor.md#_MXFP8LinearOperands.weight_qdata_dgrad_NK), [`_MXFP8LinearOperands`](tensor.md#_MXFP8LinearOperands), [`weight_scale_dgrad_swizzled`](tensor.md#_MXFP8LinearOperands.weight_scale_dgrad_swizzled), [`weight_scale_fprop_swizzled`](tensor.md#_MXFP8LinearOperands.weight_scale_fprop_swizzled)
- used by: [`forward`](linear.md#MXFP8Linear.forward), [`_ShardedFSDPTensor`](../_fsdp_tensor.md#_ShardedFSDPTensor), [`weight`](linear.md#MXFP8Linear.weight), [`_build_operands`](../_fsdp_tensor.md#_ShardedFSDPTensor._build_operands)

### <a id="_MXFP8LinearOperands"></a>`_MXFP8LinearOperands`
- def: [`torchtitan/components/quantization/mxfp8/tensor.py:34`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/tensor.py#L34)
- doc: The independent MXFP8 tensors owned by one FSDP unshard lifetime.
- signature: `class _MXFP8LinearOperands:`
- members:
  - <a id="_MXFP8LinearOperands.weight_qdata_fprop_KN"></a>`weight_qdata_fprop_KN(self)` — [`L50`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/tensor.py#L50)
  - <a id="_MXFP8LinearOperands.weight_qdata_dgrad_NK"></a>`weight_qdata_dgrad_NK` — [`L45`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/tensor.py#L45)
  - <a id="_MXFP8LinearOperands.weight_scale_dgrad_swizzled"></a>`weight_scale_dgrad_swizzled` — [`L47`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/tensor.py#L47)
  - <a id="_MXFP8LinearOperands.weight_scale_fprop_swizzled"></a>`weight_scale_fprop_swizzled` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/tensor.py#L46)
- used by: [`forward`](linear.md#MXFP8Linear.forward), [`_quantize_mxfp8_weight`](tensor.md#_quantize_mxfp8_weight), [`_build_operands`](tensor.md#_LinearShardedTensorWithMXFP8Compute._build_operands)

## Functions
- <a id="_quantize_mxfp8_weight"></a>`_quantize_mxfp8_weight(weight_NK: torch.Tensor)` — [`L54`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/tensor.py#L54) — Quantize a BF16 weight using fixed square 32x32 scale tiles. — documented in [quantization](../../../../../concepts/quantization.md)

## Module values
- <a id="_MXFP8_BLOCK_SIZE"></a>`_MXFP8_BLOCK_SIZE` — [`L30`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/tensor.py#L30)
- <a id="__all__.__all__"></a>`__all__` — [`L23`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/tensor.py#L23)

