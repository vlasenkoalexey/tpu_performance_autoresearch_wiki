---
title: 'Module: src/torch_tpu/_internal/compile/debug.py'
type: catalog
provenance: extracted
module: src/torch_tpu/_internal/compile/debug.py
status: fresh
symbol_base: scip-python python torch_tpu 0.0.0 `src.torch_tpu._internal.compile.debug`/TpuCompileDebug#
symbols:
  TpuCompileDebug.__repr__: __repr__().
  TpuCompileDebug.__str__: __str__().
  TpuCompileDebug: ''
  TpuCompileDebug.pre_autograd_fx_code: pre_autograd_fx_code.
  TpuCompileDebug.post_autograd_fx_forward_code: post_autograd_fx_forward_code.
  TpuCompileDebug.post_autograd_fx_backward_code: post_autograd_fx_backward_code.
  TpuCompileDebug.stablehlo_forward_text: stablehlo_forward_text.
  TpuCompileDebug.stablehlo_backward_text: stablehlo_backward_text.
  TpuCompileDebug.compiled_executables: compiled_executables.
  TpuCompileDebug.pre_autograd_fx_readable: pre_autograd_fx_readable.
  TpuCompileDebug.post_autograd_fx_forward_readable: post_autograd_fx_forward_readable.
  TpuCompileDebug.post_autograd_fx_backward_readable: post_autograd_fx_backward_readable.
---
# Module: [`src/torch_tpu/_internal/compile/debug.py`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py)

## Classes
### <a id="TpuCompileDebug"></a>`TpuCompileDebug`
- def: [`src/torch_tpu/_internal/compile/debug.py:22`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py#L22) — documented in [torch-compile-backend](../../../../../concepts/torch-compile-backend.md)
- doc: Log container for TorchTPU compilation artifacts.
- signature: `class TpuCompileDebug:`
- members:
  - <a id="TpuCompileDebug.compiled_executables"></a>`compiled_executables` — [`L46`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py#L46)
  - <a id="TpuCompileDebug.post_autograd_fx_backward_code"></a>`post_autograd_fx_backward_code` — [`L36`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py#L36)
  - <a id="TpuCompileDebug.post_autograd_fx_backward_readable"></a>`post_autograd_fx_backward_readable` — [`L39`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py#L39)
  - <a id="TpuCompileDebug.post_autograd_fx_forward_code"></a>`post_autograd_fx_forward_code` — [`L29`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py#L29)
  - <a id="TpuCompileDebug.post_autograd_fx_forward_readable"></a>`post_autograd_fx_forward_readable` — [`L32`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py#L32)
  - <a id="TpuCompileDebug.pre_autograd_fx_code"></a>`pre_autograd_fx_code` — [`L26`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py#L26)
  - <a id="TpuCompileDebug.pre_autograd_fx_readable"></a>`pre_autograd_fx_readable` — [`L27`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py#L27)
  - <a id="TpuCompileDebug.stablehlo_backward_text"></a>`stablehlo_backward_text` — [`L44`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py#L44)
  - <a id="TpuCompileDebug.stablehlo_forward_text"></a>`stablehlo_forward_text` — [`L43`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py#L43)
- protocol/private: <a id="TpuCompileDebug.__repr__"></a>`__repr__`[`L78`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py#L78), <a id="TpuCompileDebug.__str__"></a>`__str__`[`L48`](../../../../../../../../raw/code/torch_tpu/src/torch_tpu/_internal/compile/debug.py#L48)
- used by: [`__call__`](_backend.md#TpuBackend.__call__), [`_compile_graph_module`](_backend.md#TpuBackend._compile_graph_module), [`_compile`](compiler.md#StaticCompiler._compile), [`__init__`](compiler.md#Compiler.__init__), [`make_backend_compiler`](_backend.md#make_backend_compiler)

