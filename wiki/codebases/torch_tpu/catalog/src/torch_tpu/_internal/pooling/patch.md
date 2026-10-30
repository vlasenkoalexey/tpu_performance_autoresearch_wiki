---
title: 'Module: src/torch_tpu/_internal/pooling/patch.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/pooling/patch.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.pooling.patch`/
symbols:
  patched_max_pool2d: patched_max_pool2d().
  patch_max_pool: patch_max_pool().
  unpatch_max_pool: unpatch_max_pool().
  patched_max_pool1d: patched_max_pool1d().
  patched_max_pool3d: patched_max_pool3d().
  _is_tpu_tensor: _is_tpu_tensor().
  _IS_PATCHED._IS_PATCHED: _IS_PATCHED._IS_PATCHED.
  _ORIG_F_MAX_POOL1D: _ORIG_F_MAX_POOL1D.
  _ORIG_F_MAX_POOL2D: _ORIG_F_MAX_POOL2D.
  _ORIG_F_MAX_POOL3D: _ORIG_F_MAX_POOL3D.
  _TpuMaxPool2dFunction: _TpuMaxPool2dFunction#
  _TpuMaxPool1dFunction: _TpuMaxPool1dFunction#
  _TpuMaxPool3dFunction: _TpuMaxPool3dFunction#
  _TpuMaxPool1dFunction.forward: _TpuMaxPool1dFunction#forward().
  _TpuMaxPool1dFunction.setup_context: _TpuMaxPool1dFunction#setup_context().
  _TpuMaxPool1dFunction.backward: _TpuMaxPool1dFunction#backward().
  _TpuMaxPool2dFunction.forward: _TpuMaxPool2dFunction#forward().
  _TpuMaxPool2dFunction.setup_context: _TpuMaxPool2dFunction#setup_context().
  _TpuMaxPool2dFunction.backward: _TpuMaxPool2dFunction#backward().
  _TpuMaxPool3dFunction.forward: _TpuMaxPool3dFunction#forward().
  _TpuMaxPool3dFunction.setup_context: _TpuMaxPool3dFunction#setup_context().
  _TpuMaxPool3dFunction.backward: _TpuMaxPool3dFunction#backward().
---
# Module: [`src/torch_tpu/_internal/pooling/patch.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py)

## Classes
### <a id="_TpuMaxPool1dFunction"></a>`_TpuMaxPool1dFunction`
- def: [`src/torch_tpu/_internal/pooling/patch.py:101`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L101)
- doc: Differentiable TPU 1D max pooling using SelectAndScatter without indices.
- signature: `class _TpuMaxPool1dFunction(torch.autograd.Function):`
- members:
  - <a id="_TpuMaxPool1dFunction.backward"></a>`backward(ctx: Any, *grad_outputs: Any)` — [`L144`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L144) — Computes grad_input using SelectAndScatter from saved input tensor.
  - <a id="_TpuMaxPool1dFunction.forward"></a>`forward(input: torch.Tensor, kernel_size: list[int], stride: list[int], padding: list[int], dilation: list[int], ceil_mode: bool)` — [`L111`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L111) — Executes native 1D max pooling without index materialization.
  - <a id="_TpuMaxPool1dFunction.setup_context"></a>`setup_context(ctx: Any, inputs: tuple[Any, ...], output: Any)` — [`L125`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L125) — Saves only the forward input tensor and pooling metadata for backward.
- used by: [`patched_max_pool1d`](patch.md#patched_max_pool1d)

### <a id="_TpuMaxPool2dFunction"></a>`_TpuMaxPool2dFunction`
- def: [`src/torch_tpu/_internal/pooling/patch.py:162`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L162)
- doc: Differentiable TPU 2D max pooling using SelectAndScatter without indices.
- signature: `class _TpuMaxPool2dFunction(torch.autograd.Function):`
- members:
  - <a id="_TpuMaxPool2dFunction.backward"></a>`backward(ctx: Any, *grad_outputs: Any)` — [`L205`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L205) — Computes grad_input using SelectAndScatter from saved input tensor.
  - <a id="_TpuMaxPool2dFunction.forward"></a>`forward(input: torch.Tensor, kernel_size: list[int], stride: list[int], padding: list[int], dilation: list[int], ceil_mode: bool)` — [`L172`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L172) — Executes native 2D max pooling without index materialization.
  - <a id="_TpuMaxPool2dFunction.setup_context"></a>`setup_context(ctx: Any, inputs: tuple[Any, ...], output: Any)` — [`L186`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L186) — Saves only the forward input tensor and pooling metadata for backward.
- used by: [`patched_max_pool2d`](patch.md#patched_max_pool2d), [`test_patched_max_pool2d_tpu_train_routes_to_autograd_function`](patch_test.md#PatchTest.test_patched_max_pool2d_tpu_train_routes_to_autograd_function)

### <a id="_TpuMaxPool3dFunction"></a>`_TpuMaxPool3dFunction`
- def: [`src/torch_tpu/_internal/pooling/patch.py:223`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L223)
- doc: Differentiable TPU 3D max pooling using SelectAndScatter without indices.
- signature: `class _TpuMaxPool3dFunction(torch.autograd.Function):`
- members:
  - <a id="_TpuMaxPool3dFunction.backward"></a>`backward(ctx: Any, *grad_outputs: Any)` — [`L266`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L266) — Computes grad_input using SelectAndScatter from saved input tensor.
  - <a id="_TpuMaxPool3dFunction.forward"></a>`forward(input: torch.Tensor, kernel_size: list[int], stride: list[int], padding: list[int], dilation: list[int], ceil_mode: bool)` — [`L233`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L233) — Executes native 3D max pooling without index materialization.
  - <a id="_TpuMaxPool3dFunction.setup_context"></a>`setup_context(ctx: Any, inputs: tuple[Any, ...], output: Any)` — [`L247`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L247) — Saves only the forward input tensor and pooling metadata for backward.
- used by: [`patched_max_pool3d`](patch.md#patched_max_pool3d)

## Functions
- <a id="_is_tpu_tensor"></a>`_is_tpu_tensor(tensor: Any)` — [`L87`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L87) — Returns True if the object is a Tensor on a TPU device.
- <a id="patch_max_pool"></a>`patch_max_pool()` — [`L480`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L480) — Patches PyTorch functional max pooling operations with TPU-optimized variants.
- <a id="patched_max_pool1d"></a>`patched_max_pool1d(input: torch.Tensor, kernel_size: Any, stride: Any = None, padding: Any = 0, dilation: Any = 1, ceil_mode: bool = False, return_indices: bool = False)` — [`L290`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L290) — Optimized max_pool1d for TPU tensors avoiding unused index overhead.
- <a id="patched_max_pool2d"></a>`patched_max_pool2d(input: torch.Tensor, kernel_size: Any, stride: Any = None, padding: Any = 0, dilation: Any = 1, ceil_mode: bool = False, return_indices: bool = False)` — [`L352`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L352) — Optimized max_pool2d for TPU tensors avoiding unused index overhead.
- <a id="patched_max_pool3d"></a>`patched_max_pool3d(input: torch.Tensor, kernel_size: Any, stride: Any = None, padding: Any = 0, dilation: Any = 1, ceil_mode: bool = False, return_indices: bool = False)` — [`L414`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L414) — Optimized max_pool3d for TPU tensors avoiding unused index overhead.
- <a id="unpatch_max_pool"></a>`unpatch_max_pool()` — [`L496`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L496) — Restores original PyTorch functional max pooling operations.

## Module values
- <a id="_IS_PATCHED._IS_PATCHED"></a>`_IS_PATCHED` — [`L84`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L84)
- <a id="_ORIG_F_MAX_POOL1D"></a>`_ORIG_F_MAX_POOL1D` — [`L79`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L79)
- <a id="_ORIG_F_MAX_POOL2D"></a>`_ORIG_F_MAX_POOL2D` — [`L80`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L80)
- <a id="_ORIG_F_MAX_POOL3D"></a>`_ORIG_F_MAX_POOL3D` — [`L81`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/pooling/patch.py#L81)

