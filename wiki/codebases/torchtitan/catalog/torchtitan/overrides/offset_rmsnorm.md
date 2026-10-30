---
title: 'Module: torchtitan/overrides/offset_rmsnorm.py'
type: catalog
provenance: extracted
module: torchtitan/overrides/offset_rmsnorm.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.overrides.offset_rmsnorm`/
symbols:
  triton_offset_rmsnorm: triton_offset_rmsnorm().
  TritonOffsetRMSNorm.forward: TritonOffsetRMSNorm#forward().
  _triton_offset_rms_norm_backward_op: _triton_offset_rms_norm_backward_op().
  _triton_offset_rms_norm_op: _triton_offset_rms_norm_op().
  TritonOffsetRMSNorm.Config: TritonOffsetRMSNorm#Config#
  TritonOffsetRMSNorm.__init__: TritonOffsetRMSNorm#__init__().
  TritonOffsetRMSNorm: TritonOffsetRMSNorm#
  TritonOffsetRMSNorm.weight_grad_sharding: TritonOffsetRMSNorm#weight_grad_sharding.
  _triton_offset_rms_norm_autograd_backward: _triton_offset_rms_norm_autograd_backward().
  triton_offset_rms_norm: triton_offset_rms_norm().
  _DW_BLOCK_N: _DW_BLOCK_N.
  _num_warps: _num_warps().
  _MAX_BLOCK_SIZE: _MAX_BLOCK_SIZE.
  _DW_BLOCK_M: _DW_BLOCK_M.
  _SUPPORTED_DTYPES: _SUPPORTED_DTYPES.
  _offset_rms_norm_forward_kernel: _offset_rms_norm_forward_kernel().
  _offset_rms_norm_input_grad_kernel: _offset_rms_norm_input_grad_kernel().
  _offset_rms_norm_weight_grad_partial_kernel: _offset_rms_norm_weight_grad_partial_kernel().
  _offset_rms_norm_weight_grad_reduce_kernel: _offset_rms_norm_weight_grad_reduce_kernel().
  _triton_offset_rms_norm_setup_context: _triton_offset_rms_norm_setup_context().
  TritonOffsetRMSNorm.Config.weight_grad_sharding: TritonOffsetRMSNorm#Config#weight_grad_sharding.
  __all__: __all__.
---
# Module: [`torchtitan/overrides/offset_rmsnorm.py`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py)

## Classes
### <a id="TritonOffsetRMSNorm"></a>`TritonOffsetRMSNorm`  ·  implements/extends OffsetRMSNorm
- def: [`torchtitan/overrides/offset_rmsnorm.py:306`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L306)
- doc: Qwen3.5 OffsetRMSNorm implemented by a fused Triton kernel.
- signature: `class TritonOffsetRMSNorm(OffsetRMSNorm):`
- members:
  - <a id="TritonOffsetRMSNorm.forward"></a>`forward(self, input: torch.Tensor)` — [`L317`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L317) — documented in [config-overrides](../../../concepts/config-overrides.md)
  - <a id="TritonOffsetRMSNorm.weight_grad_sharding"></a>`weight_grad_sharding` — [`L315`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L315) — documented in [config-overrides](../../../concepts/config-overrides.md)
- protocol/private: <a id="TritonOffsetRMSNorm.__init__"></a>`__init__`[`L313`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L313)
- uses (calls/refs, reference-scoped): [`resolve_placements`](../protocols/sharding.md#resolve_placements), [`OffsetRMSNorm`](../models/qwen3_5/model.md#OffsetRMSNorm), [`forward`](../models/qwen3_5/model.md#OffsetRMSNorm.forward), [`Config`](offset_rmsnorm.md#TritonOffsetRMSNorm.Config), [`eps`](../models/qwen3_5/model.md#OffsetRMSNorm.eps), [`weight`](../models/qwen3_5/model.md#OffsetRMSNorm.weight), [`__init__`](../models/qwen3_5/model.md#OffsetRMSNorm.__init__), [`triton_offset_rms_norm`](offset_rmsnorm.md#triton_offset_rms_norm), [`_SUPPORTED_DTYPES`](offset_rmsnorm.md#_SUPPORTED_DTYPES), [`weight_grad_sharding`](offset_rmsnorm.md#TritonOffsetRMSNorm.Config.weight_grad_sharding)
- used by: [`triton_offset_rmsnorm`](offset_rmsnorm.md#triton_offset_rmsnorm), [`OffsetRMSNorm`](../models/qwen3_5/model.md#OffsetRMSNorm), [`forward`](../models/qwen3_5/model.md#OffsetRMSNorm.forward)

### <a id="TritonOffsetRMSNorm.Config"></a>`TritonOffsetRMSNorm.Config`  ·  implements/extends Config
- def: [`torchtitan/overrides/offset_rmsnorm.py:310`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L310)
- signature: `class Config(OffsetRMSNorm.Config):`
- members:
  - <a id="TritonOffsetRMSNorm.Config.weight_grad_sharding"></a>`weight_grad_sharding` — [`L311`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L311)
- uses (calls/refs, reference-scoped): [`OffsetRMSNorm`](../models/qwen3_5/model.md#OffsetRMSNorm), [`Config`](../models/qwen3_5/model.md#OffsetRMSNorm.Config)
- used by: [`triton_offset_rmsnorm`](offset_rmsnorm.md#triton_offset_rmsnorm), [`__init__`](offset_rmsnorm.md#TritonOffsetRMSNorm.__init__), [`weight_grad_sharding`](offset_rmsnorm.md#TritonOffsetRMSNorm.weight_grad_sharding)

## Functions
- <a id="_num_warps"></a>`_num_warps(block_size: int)` — [`L43`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L43)
- <a id="_offset_rms_norm_forward_kernel"></a>`_offset_rms_norm_forward_kernel(input_ptr, weight_ptr, output_ptr, inverse_rms_ptr, num_cols: tl.constexpr, eps: tl.constexpr, BLOCK_SIZE: tl.constexpr)` — [`L52`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L52)
- <a id="_offset_rms_norm_input_grad_kernel"></a>`_offset_rms_norm_input_grad_kernel(grad_output_ptr, input_ptr, weight_ptr, inverse_rms_ptr, grad_input_ptr, num_cols: tl.constexpr, BLOCK_SIZE: tl.constexpr)` — [`L78`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L78)
- <a id="_offset_rms_norm_weight_grad_partial_kernel"></a>`_offset_rms_norm_weight_grad_partial_kernel(grad_output_ptr, input_ptr, inverse_rms_ptr, partial_grad_weight_ptr, num_rows, num_cols: tl.constexpr, BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr)` — [`L109`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L109)
- <a id="_offset_rms_norm_weight_grad_reduce_kernel"></a>`_offset_rms_norm_weight_grad_reduce_kernel(partial_grad_weight_ptr, grad_weight_ptr, num_partials, num_cols: tl.constexpr, BLOCK_M: tl.constexpr, BLOCK_N: tl.constexpr)` — [`L148`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L148)
- <a id="_triton_offset_rms_norm_autograd_backward"></a>`_triton_offset_rms_norm_autograd_backward(ctx, grad_output: torch.Tensor, _grad_inverse_rms: torch.Tensor | None)` — [`L271`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L271)
- <a id="_triton_offset_rms_norm_backward_op"></a>`_triton_offset_rms_norm_backward_op(grad_output: torch.Tensor, input: torch.Tensor, weight: torch.Tensor, inverse_rms: torch.Tensor)` — [`L204`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L204) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="_triton_offset_rms_norm_op"></a>`_triton_offset_rms_norm_op(input: torch.Tensor, weight: torch.Tensor, eps: float)` — [`L175`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L175) — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="_triton_offset_rms_norm_setup_context"></a>`_triton_offset_rms_norm_setup_context(ctx, inputs, output)` — [`L265`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L265)
- <a id="triton_offset_rms_norm"></a>`triton_offset_rms_norm(input: torch.Tensor, weight: torch.Tensor, eps: float)` — [`L292`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L292) — Compute ``(1 + weight) * rmsnorm(input)`` with Triton. — documented in [config-overrides](../../../concepts/config-overrides.md)
- <a id="triton_offset_rmsnorm"></a>`triton_offset_rmsnorm(cfg: OffsetRMSNorm.Config)` — [`L343`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L343) — documented in [config-overrides](../../../concepts/config-overrides.md)

## Module values
- <a id="_DW_BLOCK_M"></a>`_DW_BLOCK_M` — [`L39`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L39)
- <a id="_DW_BLOCK_N"></a>`_DW_BLOCK_N` — [`L40`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L40)
- <a id="_MAX_BLOCK_SIZE"></a>`_MAX_BLOCK_SIZE` — [`L38`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L38)
- <a id="_SUPPORTED_DTYPES"></a>`_SUPPORTED_DTYPES` — [`L37`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L37)
- <a id="__all__"></a>`__all__` — [`L30`](../../../../../../raw/code/torchtitan/torchtitan/overrides/offset_rmsnorm.py#L30)

