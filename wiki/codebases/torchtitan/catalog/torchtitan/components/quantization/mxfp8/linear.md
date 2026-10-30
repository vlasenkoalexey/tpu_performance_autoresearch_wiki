---
title: 'Module: torchtitan/components/quantization/mxfp8/linear.py'
type: catalog
provenance: extracted
module: torchtitan/components/quantization/mxfp8/linear.py
status: fresh
symbol_base: scip-python python torchtitan 0.0.0 `torchtitan.components.quantization.mxfp8.linear`/
symbols:
  MXFP8Linear.forward: MXFP8Linear#forward().
  _MXFP8LinearFunction.forward: _MXFP8LinearFunction#forward().
  MXFP8Linear: MXFP8Linear#
  _MXFP8LinearFunction.backward: _MXFP8LinearFunction#backward().
  MXFP8Linear.Config.build: MXFP8Linear#Config#build().
  MXFP8Linear.Config: MXFP8Linear#Config#
  MXFP8Linear.weight: MXFP8Linear#weight.
  MXFP8Linear.Config.__post_init__: MXFP8Linear#Config#__post_init__().
  MXFP8Linear.Config.input_activation_format_for_backward: MXFP8Linear#Config#input_activation_format_for_backward.
  _pad_rows: _pad_rows().
  MXFP8Linear.__init__: MXFP8Linear#__init__().
  MXFP8Linear.input_activation_format_for_backward: MXFP8Linear#input_activation_format_for_backward.
  _MXFP8_SCALING_MODE: _MXFP8_SCALING_MODE.
  InputActivationFormatForBackward: InputActivationFormatForBackward.
  _INPUT_ACTIVATION_FORMATS_FOR_BACKWARD: _INPUT_ACTIVATION_FORMATS_FOR_BACKWARD.
  _MXFP8LinearFunction: _MXFP8LinearFunction#
  __all__: __all__.
---
# Module: [`torchtitan/components/quantization/mxfp8/linear.py`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py)

## Classes
### <a id="MXFP8Linear"></a>`MXFP8Linear`  ·  implements/extends Linear
- def: [`torchtitan/components/quantization/mxfp8/linear.py:303`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L303) — documented in [quantization](../../../../../concepts/quantization.md)
- doc: Linear using 1D activations and cached 32x32 weight quantization.
- signature: `class MXFP8Linear(Linear):`
- members:
  - <a id="MXFP8Linear.forward"></a>`forward(self, input: torch.Tensor)` — [`L368`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L368) — documented in [quantization](../../../../../concepts/quantization.md)
  - <a id="MXFP8Linear.input_activation_format_for_backward"></a>`input_activation_format_for_backward` — [`L356`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L356)
  - <a id="MXFP8Linear.weight"></a>`weight` — [`L363`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L363)
- protocol/private: <a id="MXFP8Linear.__init__"></a>`__init__`[`L354`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L354)
- uses (calls/refs, reference-scoped): [`Linear`](../../../models/common/linear.md#Linear), [`_quantize_mxfp8_weight`](tensor.md#_quantize_mxfp8_weight), [`__init__`](../../../models/common/linear.md#Linear.__init__), [`_UnshardedFSDPTensor`](../_fsdp_tensor.md#_UnshardedFSDPTensor), [`_tensor`](../_fsdp_tensor.md#_ShardedFSDPTensor._tensor), [`Config`](linear.md#MXFP8Linear.Config), [`input_activation_format_for_backward`](linear.md#MXFP8Linear.Config.input_activation_format_for_backward), [`_LinearShardedTensorWithMXFP8Compute`](tensor.md#_LinearShardedTensorWithMXFP8Compute), [`operands`](../_fsdp_tensor.md#_UnshardedFSDPTensor.operands), [`weight_qdata_dgrad_NK`](tensor.md#_MXFP8LinearOperands.weight_qdata_dgrad_NK), [`weight_scale_dgrad_swizzled`](tensor.md#_MXFP8LinearOperands.weight_scale_dgrad_swizzled), [`weight_scale_fprop_swizzled`](tensor.md#_MXFP8LinearOperands.weight_scale_fprop_swizzled), [`weight_qdata_fprop_KN`](tensor.md#_MXFP8LinearOperands.weight_qdata_fprop_KN), [`_MXFP8LinearFunction`](linear.md#_MXFP8LinearFunction)
- used by: [`Linear`](../../../models/common/linear.md#Linear), [`model_compile_enabled`](../__init__.md#QuantizationConverter.Config.model_compile_enabled), [`convert`](converter.md#MXFP8LinearConverter.convert), [`has_quantization`](../utils.md#has_quantization), [`__init__`](converter.md#MXFP8LinearConverter.__init__), [`import_error`](converter.md#import_error), [`_mxfp8_linear_import_error`](converter.md#_mxfp8_linear_import_error._mxfp8_linear_import_error)

### <a id="MXFP8Linear.Config"></a>`MXFP8Linear.Config`  ·  implements/extends Config
- def: [`torchtitan/components/quantization/mxfp8/linear.py:307`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L307)
- doc: Drop-in replacement for `Linear.Config`.
- signature: `class Config(Linear.Config):`
- members:
  - <a id="MXFP8Linear.Config.build"></a>`build(self, **kwargs)` — [`L336`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L336) — documented in [quantization](../../../../../concepts/quantization.md)
  - <a id="MXFP8Linear.Config.input_activation_format_for_backward"></a>`input_activation_format_for_backward` — [`L310`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L310) — ---
- protocol/private: <a id="MXFP8Linear.Config.__post_init__"></a>`__post_init__`[`L318`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L318)
- uses (calls/refs, reference-scoped): [`build`](../../../protocols/module.md#Module.Config.build), [`Linear`](../../../models/common/linear.md#Linear), [`Config`](../../../models/common/linear.md#Linear.Config), [`get_spmd_backend`](../../../distributed/utils.md#get_spmd_backend), [`_MXFP8_BLOCK_SIZE`](tensor.md#_MXFP8_BLOCK_SIZE), [`InputActivationFormatForBackward`](linear.md#InputActivationFormatForBackward), [`_INPUT_ACTIVATION_FORMATS_FOR_BACKWARD`](linear.md#_INPUT_ACTIVATION_FORMATS_FOR_BACKWARD)
- used by: [`convert`](converter.md#MXFP8LinearConverter.convert), [`has_quantization`](../utils.md#has_quantization), [`__init__`](linear.md#MXFP8Linear.__init__), [`input_activation_format_for_backward`](linear.md#MXFP8Linear.input_activation_format_for_backward)

### <a id="_MXFP8LinearFunction"></a>`_MXFP8LinearFunction`
- def: [`torchtitan/components/quantization/mxfp8/linear.py:66`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L66)
- signature: `class _MXFP8LinearFunction(torch.autograd.Function):`
- members:
  - <a id="_MXFP8LinearFunction.backward"></a>`backward(ctx, grad_output: torch.Tensor)` — [`L201`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L201) — documented in [quantization](../../../../../concepts/quantization.md)
  - <a id="_MXFP8LinearFunction.forward"></a>`forward(ctx, x: torch.Tensor, weight_NK: torch.Tensor, weight_qdata_fprop_KN: torch.Tensor, weight_scale_fprop_swizzled: torch.Tensor, weight_qdata_dgrad_NK: torch.Tensor, weight_scale_dgrad_swizzled: torch.Tensor, bias_N: torch.Tensor | None, input_activation_format_for_backward: InputActivationFormatForBackward)` — [`L69`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L69) — documented in [quantization](../../../../../concepts/quantization.md)
- uses (calls/refs, reference-scoped): [`_UnshardedFSDPTensor`](../_fsdp_tensor.md#_UnshardedFSDPTensor), [`_MXFP8_BLOCK_SIZE`](tensor.md#_MXFP8_BLOCK_SIZE), [`_pad_rows`](linear.md#_pad_rows), [`operands`](../_fsdp_tensor.md#_UnshardedFSDPTensor.operands), [`_MXFP8_SCALING_MODE`](linear.md#_MXFP8_SCALING_MODE), [`InputActivationFormatForBackward`](linear.md#InputActivationFormatForBackward)
- used by: [`forward`](linear.md#MXFP8Linear.forward)

## Functions
- <a id="_pad_rows"></a>`_pad_rows(x_MK: torch.Tensor)` — [`L52`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L52)

## Module values
- <a id="InputActivationFormatForBackward"></a>`InputActivationFormatForBackward` — [`L48`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L48)
- <a id="_INPUT_ACTIVATION_FORMATS_FOR_BACKWARD"></a>`_INPUT_ACTIVATION_FORMATS_FOR_BACKWARD` — [`L49`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L49)
- <a id="_MXFP8_SCALING_MODE"></a>`_MXFP8_SCALING_MODE` — [`L46`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L46)
- <a id="__all__"></a>`__all__` — [`L40`](../../../../../../../../raw/code/torchtitan/torchtitan/components/quantization/mxfp8/linear.py#L40)

