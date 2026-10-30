---
title: 'Module: csrc/ops/python_context.cc'
type: catalog
provenance: extracted
module: csrc/ops/python_context.cc
status: fresh
symbol_base: 'cxx . . $ '
symbols:
  GetRootOpName: torch_tpu/GetRootOpName(3684c9265f839858).
  ScopedPythonContextCapturer.ScopedPythonContextCapturer: torch_tpu/ScopedPythonContextCapturer#ScopedPythonContextCapturer(eed00ffa8ace304f).
  ScopedPythonContextCapturer.GetContext: torch_tpu/ScopedPythonContextCapturer#GetContext(12f11b49d3d3bbf6).
  CaptureCurrentPythonTrackback: torch_tpu/CaptureCurrentPythonTrackback(dce451a09e97b9cf).
  ScopedPythonContextCapturer.MaybeGetContext: torch_tpu/ScopedPythonContextCapturer#MaybeGetContext(1330516da04f90b5).
  ScopedPythonContextProvider.ScopedPythonContextProvider: torch_tpu/ScopedPythonContextProvider#ScopedPythonContextProvider(34f69cba5325650b).
  MakeMlirLocation: torch_tpu/MakeMlirLocation(6a96d82cbe85d768).
  GetTracebackMode: torch_tpu/GetTracebackMode(5dd7a433a30cb062).
  ScopedPythonContextCapturer.traceback_: torch_tpu/ScopedPythonContextCapturer#traceback_.
  ScopedPythonContextProvider.top_context_: torch_tpu/ScopedPythonContextProvider#top_context_.
  PythonContext.PythonContext: torch_tpu/PythonContext#PythonContext(8ca8d13865ce245e).
  ScopedPythonContextCapturer.op_names_: torch_tpu/ScopedPythonContextCapturer#op_names_.
  ScopedPythonContextCapturer.-ScopedPythonContextCapturer: torch_tpu/ScopedPythonContextCapturer#`~ScopedPythonContextCapturer`(ced63f7c635d850d).
  FLAGS_help_storage_torch_tpu_internal_mlir_tracebacks: FLAGS_help_storage_torch_tpu_internal_mlir_tracebacks.
  MakeFuncFileLineColLoc: torch_tpu/`$anonymous_namespace_csrc/ops/python_context.cc`/MakeFuncFileLineColLoc(d8d4c429b757fdc0).
  MakeLocFromPythonTraceback: torch_tpu/`$anonymous_namespace_csrc/ops/python_context.cc`/MakeLocFromPythonTraceback(dd09e8d9643056b1).
  IsUserFrame: torch_tpu/`$anonymous_namespace_csrc/ops/python_context.cc`/IsUserFrame(6af2824ebcb17499).
  ScopedPythonContextProvider.-ScopedPythonContextProvider: torch_tpu/ScopedPythonContextProvider#`~ScopedPythonContextProvider`(ced63f7c635d850d).
  MakeNameScopeOpStringFromCallChain: torch_tpu/`$anonymous_namespace_csrc/ops/python_context.cc`/MakeNameScopeOpStringFromCallChain(fb1181c56e49d69).
  FLAGS_torch_tpu_internal_mlir_tracebacks: FLAGS_torch_tpu_internal_mlir_tracebacks.
  FileLineColLoc: torch_tpu/`$anonymous_namespace_csrc/ops/python_context.cc`/FileLineColLoc(7ca1436fa006f402).
  NamedLocation: torch_tpu/`$anonymous_namespace_csrc/ops/python_context.cc`/NamedLocation(742e432665299dc5).
  AbslFlagDefaultGenFortorch_tpu_internal_mlir_tracebacks: AbslFlagDefaultGenFortorch_tpu_internal_mlir_tracebacks#
  AbslFlagDefaultGenFortorch_tpu_internal_mlir_tracebacks.value: AbslFlagDefaultGenFortorch_tpu_internal_mlir_tracebacks#value.
  GetCanonicalFilename: torch_tpu/`$anonymous_namespace_csrc/ops/python_context.cc`/GetCanonicalFilename(59d317b252f70f25).
  AbslFlagHelpGenFortorch_tpu_internal_mlir_tracebacks.Value: AbslFlagHelpGenFortorch_tpu_internal_mlir_tracebacks#Value(59d317b252f70f25).
  AbslFlagHelpGenFortorch_tpu_internal_mlir_tracebacks: AbslFlagHelpGenFortorch_tpu_internal_mlir_tracebacks#
  AbslFlagDefaultGenFortorch_tpu_internal_mlir_tracebacks.Gen: AbslFlagDefaultGenFortorch_tpu_internal_mlir_tracebacks#Gen(5d22bdacc48458e8).
  FLAGS_notorch_tpu_internal_mlir_tracebacks: FLAGS_notorch_tpu_internal_mlir_tracebacks.
  AbslFlagHelpGenFortorch_tpu_internal_mlir_tracebacks.NonConst: AbslFlagHelpGenFortorch_tpu_internal_mlir_tracebacks#NonConst(efd28698952f529a).
---
# Module: [`csrc/ops/python_context.cc`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc)

## Classes
### <a id="AbslFlagDefaultGenFortorch_tpu_internal_mlir_tracebacks"></a>`AbslFlagDefaultGenFortorch_tpu_internal_mlir_tracebacks`
- def: [`csrc/ops/python_context.cc:50`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L50)
- signature: `ABSL_FLAG(std::optional<bool>, torch_tpu_internal_mlir_tracebacks, std::nullopt, "If set, MLIR location tracebacks will be enabled or disabled by " "default depending on the Boolean value. Otherwise, the default is " "disabling tracebacks in the eager mode and enabling them in the " "compiled mode. This can be overridden by the enable_tracebacks() " "context manager.")`
- members:
  - <a id="AbslFlagDefaultGenFortorch_tpu_internal_mlir_tracebacks.Gen"></a>`Gen(std::optional<bool>, torch_tpu_internal_mlir_tracebacks, std::nullopt, "If set, MLIR location tracebacks will be enabled or disabled by " "default depending on the Boolean value. Otherwise, the default is " "disabling tracebacks in the eager mode and enabling them in the " "compiled mode. This can be overridden by the enable_tracebacks() " "context manager.")` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L50)
  - <a id="AbslFlagDefaultGenFortorch_tpu_internal_mlir_tracebacks.value"></a>`value` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L50)
- used by: [`FLAGS_help_storage_torch_tpu_internal_mlir_tracebacks`](python_context.cc.md#FLAGS_help_storage_torch_tpu_internal_mlir_tracebacks)

### <a id="AbslFlagHelpGenFortorch_tpu_internal_mlir_tracebacks"></a>`AbslFlagHelpGenFortorch_tpu_internal_mlir_tracebacks`
- def: [`csrc/ops/python_context.cc:50`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L50)
- signature: `ABSL_FLAG(std::optional<bool>, torch_tpu_internal_mlir_tracebacks, std::nullopt, "If set, MLIR location tracebacks will be enabled or disabled by " "default depending on the Boolean value. Otherwise, the default is " "disabling tracebacks in the eager mode and enabling them in the " "compiled mode. This can be overridden by the enable_tracebacks() " "context manager.")`
- members:
  - <a id="AbslFlagHelpGenFortorch_tpu_internal_mlir_tracebacks.NonConst"></a>`NonConst(std::optional<bool>, torch_tpu_internal_mlir_tracebacks, std::nullopt, "If set, MLIR location tracebacks will be enabled or disabled by " "default depending on the Boolean value. Otherwise, the default is " "disabling tracebacks in the eager mode and enabling them in the " "compiled mode. This can be overridden by the enable_tracebacks() " "context manager.")` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L50)
  - <a id="AbslFlagHelpGenFortorch_tpu_internal_mlir_tracebacks.Value"></a>`Value(std::optional<bool>, torch_tpu_internal_mlir_tracebacks, std::nullopt, "If set, MLIR location tracebacks will be enabled or disabled by " "default depending on the Boolean value. Otherwise, the default is " "disabling tracebacks in the eager mode and enabling them in the " "compiled mode. This can be overridden by the enable_tracebacks() " "context manager.")` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L50) — long enough for NonConst to work correctly.
- used by: [`FLAGS_help_storage_torch_tpu_internal_mlir_tracebacks`](python_context.cc.md#FLAGS_help_storage_torch_tpu_internal_mlir_tracebacks)

## Functions
- <a id="CaptureCurrentPythonTrackback"></a>`CaptureCurrentPythonTrackback(PythonStackLocationOptions opts)` — [`L209`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L209) — Used in deferred op builders to capture stack traces while building
- <a id="FileLineColLoc"></a>`FileLineColLoc(mlir::MLIRContext& ctx, std::string_view filename, unsigned lineno, unsigned column)` — [`L133`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L133) — Creates an MLIR FileLineColLoc class for the given string. Useful for
- <a id="GetCanonicalFilename"></a>`GetCanonicalFilename(std::string_view filename)` — [`L84`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L84)
- <a id="GetRootOpName"></a>`GetRootOpName(const std::optional<OpName> current_op_name)` — [`L325`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L325) — Returns the root op name for the current op. — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)
- <a id="GetTracebackMode"></a>`GetTracebackMode()` — [`L61`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L61) — Returns the traceback mode in the current context.
- <a id="IsUserFrame"></a>`IsUserFrame(const PythonStackFrame& frame)` — [`L95`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L95)
- <a id="MakeFuncFileLineColLoc"></a>`MakeFuncFileLineColLoc(mlir::MLIRContext& ctx, const PythonStackFrame& frame)` — [`L143`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L143) — Utility function for creating Function & FileLineCol debuginfo in the proper
- <a id="MakeLocFromPythonTraceback"></a>`MakeLocFromPythonTraceback(mlir::MLIRContext& ctx, MaybeSharedTraceback tb)` — [`L154`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L154) — Returns a location of the callstack->func->filename as described in the
- <a id="MakeMlirLocation"></a>`MakeMlirLocation(mlir::MLIRContext& ctx, const PythonContext& python_context)` — [`L239`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L239) — See header file for format of locations
- <a id="MakeNameScopeOpStringFromCallChain"></a>`MakeNameScopeOpStringFromCallChain(const PythonContext& python_context)` — [`L186`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L186) — Create a name scope / op loc for the given call chain.
- <a id="NamedLocation"></a>`NamedLocation(std::string_view name, mlir::Location loc)` — [`L124`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L124) — Creates an MLIR NamedLocation class for the given string. Useful for

## Module values
- <a id="FLAGS_help_storage_torch_tpu_internal_mlir_tracebacks"></a>`FLAGS_help_storage_torch_tpu_internal_mlir_tracebacks` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L50)
- <a id="FLAGS_notorch_tpu_internal_mlir_tracebacks"></a>`FLAGS_notorch_tpu_internal_mlir_tracebacks` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L50)
- <a id="FLAGS_torch_tpu_internal_mlir_tracebacks"></a>`FLAGS_torch_tpu_internal_mlir_tracebacks` — [`L50`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L50) — second redeclaration is to allow applying attributes

## Other members
- `ScopedPythonContextCapturer` — [`L270`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L270)
- `ScopedPythonContextCapturer` — [`L253`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L253)
- `PythonContext` — [`L204`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L204)
- <a id="PythonContext.PythonContext"></a>`PythonContext.PythonContext` — [`L204`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L204) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
- <a id="ScopedPythonContextCapturer.-ScopedPythonContextCapturer"></a>`ScopedPythonContextCapturer.-ScopedPythonContextCapturer` — [`L277`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L277)
- <a id="ScopedPythonContextCapturer.GetContext"></a>`ScopedPythonContextCapturer.GetContext` — [`L287`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L287)
- <a id="ScopedPythonContextCapturer.MaybeGetContext"></a>`ScopedPythonContextCapturer.MaybeGetContext` — [`L296`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L296)
- <a id="ScopedPythonContextCapturer.ScopedPythonContextCapturer"></a>`ScopedPythonContextCapturer.ScopedPythonContextCapturer` — [`L274`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L274) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
- <a id="ScopedPythonContextCapturer.op_names_"></a>`ScopedPythonContextCapturer.op_names_` — [`L303`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L303)
- <a id="ScopedPythonContextCapturer.traceback_"></a>`ScopedPythonContextCapturer.traceback_` — [`L305`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L305)
- <a id="ScopedPythonContextProvider.-ScopedPythonContextProvider"></a>`ScopedPythonContextProvider.-ScopedPythonContextProvider` — [`L317`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L317)
- <a id="ScopedPythonContextProvider.ScopedPythonContextProvider"></a>`ScopedPythonContextProvider.ScopedPythonContextProvider` — [`L307`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L307) — documented in [op-names-and-python-context](../../../concepts/op-names-and-python-context.md)
- <a id="ScopedPythonContextProvider.top_context_"></a>`ScopedPythonContextProvider.top_context_` — [`L323`](../../../../../../raw/code/torch_tpu/csrc/ops/python_context.cc#L323)

