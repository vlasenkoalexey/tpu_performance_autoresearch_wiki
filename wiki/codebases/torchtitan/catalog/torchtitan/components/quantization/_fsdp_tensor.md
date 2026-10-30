---
title: 'Module: torchtitan/components/quantization/_fsdp_tensor.py'
type: catalog
provenance: extracted
module: torchtitan/components/quantization/_fsdp_tensor.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.quantization._fsdp_tensor`/
symbols:
  _ShardedFSDPTensor.fsdp_post_all_gather: _ShardedFSDPTensor#fsdp_post_all_gather().
  _UnshardedFSDPTensor: _UnshardedFSDPTensor#
  _ShardedFSDPTensor: _ShardedFSDPTensor#
  _ShardedFSDPTensor._tensor: _ShardedFSDPTensor#_tensor.
  _UnshardedFSDPTensor.__torch_dispatch__: _UnshardedFSDPTensor#__torch_dispatch__().
  _UnshardedFSDPTensor._operands: _UnshardedFSDPTensor#_operands.
  _UnshardedFSDPTensor.wrap_view: _UnshardedFSDPTensor#wrap_view().
  _ShardedFSDPTensor.unwrap: _ShardedFSDPTensor#unwrap().
  _unsharded_inner_tensors: _unsharded_inner_tensors().
  _UnshardedFSDPTensor.unwrap: _UnshardedFSDPTensor#unwrap().
  _ShardedFSDPTensor._build_operands: _ShardedFSDPTensor#_build_operands().
  _UnshardedFSDPTensor.operands: _UnshardedFSDPTensor#operands().
  _ShardedFSDPTensor.__torch_dispatch__: _ShardedFSDPTensor#__torch_dispatch__().
  _UnshardedFSDPTensor.__tensor_flatten__: _UnshardedFSDPTensor#__tensor_flatten__().
  _UnshardedFSDPTensor.__tensor_unflatten__: _UnshardedFSDPTensor#__tensor_unflatten__().
  _FSDPTensorBase: _FSDPTensorBase#
  _unsharded_inner_tensor_names: _unsharded_inner_tensor_names().
  _ShardedFSDPTensor.fsdp_pre_all_gather: _ShardedFSDPTensor#fsdp_pre_all_gather().
  _UnshardedFSDPTensor.__repr__: _UnshardedFSDPTensor#__repr__().
  _FSDP_SHARDED_OPS: _FSDP_SHARDED_OPS.
  _FSDP_UNSHARDED_VIEW_OPS: _FSDP_UNSHARDED_VIEW_OPS.
  _FSDP_UNSHARDED_FACTORY_OPS: _FSDP_UNSHARDED_FACTORY_OPS.
  _validate_refilled_tensor_identity: _validate_refilled_tensor_identity().
  _FSDPTensorBase.__new__: _FSDPTensorBase#__new__().
  _ShardedFSDPTensor.__init__: _ShardedFSDPTensor#__init__().
  _ShardedFSDPTensor.__tensor_flatten__: _ShardedFSDPTensor#__tensor_flatten__().
  _ShardedFSDPTensor.__tensor_unflatten__: _ShardedFSDPTensor#__tensor_unflatten__().
  _ShardedFSDPTensor.fsdp_should_release_all_gather_outputs_after_post_all_gather: _ShardedFSDPTensor#fsdp_should_release_all_gather_outputs_after_post_all_gather().
  _UnshardedFSDPTensor.__init__: _UnshardedFSDPTensor#__init__().
  __all__.__all__: __all__.__all__.
---
# Module: [`torchtitan/components/quantization/_fsdp_tensor.py`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py)

## Classes
### <a id="_FSDPTensorBase"></a>`_FSDPTensorBase`
- def: [`torchtitan/components/quantization/_fsdp_tensor.py:238`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L238)
- doc: Logical high-precision metadata shared by both lifecycle states.
- signature: `class _FSDPTensorBase(torch.Tensor):`
- protocol/private: <a id="_FSDPTensorBase.__new__"></a>`__new__`[`L242`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L242)
- uses (calls/refs, reference-scoped): [`_ShardedFSDPTensor`](_fsdp_tensor.md#_ShardedFSDPTensor)
- used by: [`_UnshardedFSDPTensor`](_fsdp_tensor.md#_UnshardedFSDPTensor), [`_ShardedFSDPTensor`](_fsdp_tensor.md#_ShardedFSDPTensor)

### <a id="_ShardedFSDPTensor"></a>`_ShardedFSDPTensor`  ·  implements/extends _FSDPTensorBase
- def: [`torchtitan/components/quantization/_fsdp_tensor.py:259`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L259) — documented in [quantization](../../../../concepts/quantization.md)
- doc: Persistent high-precision parameter that owns the FSDP hooks.
- signature: `class _ShardedFSDPTensor(_FSDPTensorBase):`
- members:
  - <a id="_ShardedFSDPTensor._build_operands"></a>`_build_operands(self, logical_tensor: torch.Tensor, out: Any = None)` — [`L323`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L323) — Quantize ``logical_tensor``, into ``out``'s tensors when refilling.
  - <a id="_ShardedFSDPTensor.fsdp_post_all_gather"></a>`fsdp_post_all_gather(self, all_gather_outputs, metadata, param_dtype, *, out=None)` — [`L398`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L398) — Create or refill the unsharded tensor operands after all-gather. — documented in [quantization](../../../../concepts/quantization.md)
  - <a id="_ShardedFSDPTensor.fsdp_pre_all_gather"></a>`fsdp_pre_all_gather(self, mesh, outer_size, outer_stride, module, mp_policy)` — [`L335`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L335) — Return the high-precision communication tensor and the logical size.
  - <a id="_ShardedFSDPTensor.fsdp_should_release_all_gather_outputs_after_post_all_gather"></a>`fsdp_should_release_all_gather_outputs_after_post_all_gather(self)` — [`L331`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L331) — Release the high-precision all-gather output after state construction.
  - <a id="_ShardedFSDPTensor.unwrap"></a>`unwrap(tensor: _ShardedFSDPTensor)` — [`L306`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L306)
- protocol/private: <a id="_ShardedFSDPTensor.__init__"></a>`__init__`[`L287`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L287), <a id="_ShardedFSDPTensor.__tensor_flatten__"></a>`__tensor_flatten__`[`L291`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L291), <a id="_ShardedFSDPTensor.__tensor_unflatten__"></a>`__tensor_unflatten__`[`L295`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L295), <a id="_ShardedFSDPTensor.__torch_dispatch__"></a>`__torch_dispatch__`[`L301`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L301), <a id="_ShardedFSDPTensor._tensor"></a>`_tensor`[`L289`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L289)
- uses (calls/refs, reference-scoped): [`_UnshardedFSDPTensor`](_fsdp_tensor.md#_UnshardedFSDPTensor), [`_build_operands`](mxfp8/tensor.md#_LinearShardedTensorWithMXFP8Compute._build_operands), [`_operands`](_fsdp_tensor.md#_UnshardedFSDPTensor._operands), [`_unsharded_inner_tensors`](_fsdp_tensor.md#_unsharded_inner_tensors), [`_LinearShardedTensorWithMXFP8Compute`](mxfp8/tensor.md#_LinearShardedTensorWithMXFP8Compute), [`operands`](_fsdp_tensor.md#_UnshardedFSDPTensor.operands), [`_FSDPTensorBase`](_fsdp_tensor.md#_FSDPTensorBase), [`_FSDP_SHARDED_OPS`](_fsdp_tensor.md#_FSDP_SHARDED_OPS), [`_validate_refilled_tensor_identity`](_fsdp_tensor.md#_validate_refilled_tensor_identity)
- used by: [`forward`](mxfp8/linear.md#MXFP8Linear.forward), [`forward`](../../experiments/graph_trainer/simple_fsdp.md#ReplicateComputation.forward), [`forward`](../../experiments/graph_trainer/simple_fsdp.md#_BuildUnshardedTensorFunction.forward), [`_LinearShardedTensorWithMXFP8Compute`](mxfp8/tensor.md#_LinearShardedTensorWithMXFP8Compute), [`_FSDPTensorBase`](_fsdp_tensor.md#_FSDPTensorBase)

### <a id="_UnshardedFSDPTensor"></a>`_UnshardedFSDPTensor`
- def: [`torchtitan/components/quantization/_fsdp_tensor.py:446`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L446) — documented in [quantization](../../../../concepts/quantization.md)
- members:
  - <a id="_UnshardedFSDPTensor.operands"></a>`operands(self)` — [`L580`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L580) — Return the operands for the current unshard lifetime.
  - <a id="_UnshardedFSDPTensor.unwrap"></a>`unwrap(tensor: _UnshardedFSDPTensor)` — [`L526`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L526)
  - <a id="_UnshardedFSDPTensor.wrap_view"></a>`wrap_view(tensor: torch.Tensor)` — [`L542`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L542)
- protocol/private: <a id="_UnshardedFSDPTensor.__init__"></a>`__init__`[`L462`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L462), <a id="_UnshardedFSDPTensor.__repr__"></a>`__repr__`[`L484`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L484), <a id="_UnshardedFSDPTensor.__tensor_flatten__"></a>`__tensor_flatten__`[`L497`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L497), <a id="_UnshardedFSDPTensor.__tensor_unflatten__"></a>`__tensor_unflatten__`[`L503`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L503), <a id="_UnshardedFSDPTensor.__torch_dispatch__"></a>`__torch_dispatch__`[`L522`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L522), <a id="_UnshardedFSDPTensor._operands"></a>`_operands`[`L473`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L473)
- uses (calls/refs, reference-scoped): [`_unsharded_inner_tensors`](_fsdp_tensor.md#_unsharded_inner_tensors), [`_FSDPTensorBase`](_fsdp_tensor.md#_FSDPTensorBase), [`_unsharded_inner_tensor_names`](_fsdp_tensor.md#_unsharded_inner_tensor_names), [`_FSDP_UNSHARDED_FACTORY_OPS`](_fsdp_tensor.md#_FSDP_UNSHARDED_FACTORY_OPS), [`_FSDP_UNSHARDED_VIEW_OPS`](_fsdp_tensor.md#_FSDP_UNSHARDED_VIEW_OPS)
- used by: [`forward`](mxfp8/linear.md#MXFP8Linear.forward), [`fsdp_post_all_gather`](_fsdp_tensor.md#_ShardedFSDPTensor.fsdp_post_all_gather), [`forward`](mxfp8/linear.md#_MXFP8LinearFunction.forward), [`forward`](../../experiments/graph_trainer/simple_fsdp.md#ReplicateComputation.forward), [`backward`](mxfp8/linear.md#_MXFP8LinearFunction.backward), [`forward`](../../experiments/graph_trainer/simple_fsdp.md#_BuildUnshardedTensorFunction.forward)

## Functions
- <a id="_unsharded_inner_tensor_names"></a>`_unsharded_inner_tensor_names(operands_cls: type)` — [`L188`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L188) — Return the names of the unsharded inner tensors an operands dataclass owns.
- <a id="_unsharded_inner_tensors"></a>`_unsharded_inner_tensors(operands: Any)` — [`L198`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L198) — Return the unsharded inner tensors an operands dataclass owns.
- <a id="_validate_refilled_tensor_identity"></a>`_validate_refilled_tensor_identity(unsharded_inner_tensors: tuple[torch.Tensor, ...], refilled_tensors: tuple[torch.Tensor, ...])` — [`L222`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L222) — Require a refill to preserve every tensor object managed by FSDP.

## Module values
- <a id="_FSDP_SHARDED_OPS"></a>`_FSDP_SHARDED_OPS` — [`L154`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L154)
- <a id="_FSDP_UNSHARDED_FACTORY_OPS"></a>`_FSDP_UNSHARDED_FACTORY_OPS` — [`L181`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L181)
- <a id="_FSDP_UNSHARDED_VIEW_OPS"></a>`_FSDP_UNSHARDED_VIEW_OPS` — [`L174`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L174)
- <a id="__all__.__all__"></a>`__all__` — [`L150`](../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/_fsdp_tensor.py#L150)

