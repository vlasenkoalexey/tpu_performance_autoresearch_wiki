---
title: 'Module: csrc/common/pybind_error_utils.h'
type: catalog
provenance: extracted
module: csrc/common/pybind_error_utils.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  PyBindModule.def: PyBindModule#def(e521dcbaaebc20).
  PyBindModule: PyBindModule#
  PyBindClass.def: PyBindClass#def(43c74ff37f81810d).
  PyBindClass.def_readonly: PyBindClass#def_readonly(fb4d20943f91d2b9).
  GetPyBindHandle: GetPyBindHandle(ffb021ab2a405034).
  PyBindModule.PyBindModule: PyBindModule#PyBindModule(11ad959dc12ac29f).
  PyBindClass: PyBindClass#
  ErrorHandlingHelper.impl: internal/ErrorHandlingHelper#impl(3e43521ffca6eabb).
  PyBindModule.attr: PyBindModule#attr(6c83c1196ef65f52).
  PyBindClass.def_property: PyBindClass#def_property(b1aa71c5b5fa4344).
  PyBindClass.def_property_readonly: PyBindClass#def_property_readonly(43c74ff37f81810d).
  PyBindErrorHandlingWrapper.PyBindErrorHandlingWrapper-PyBindType: internal/PyBindErrorHandlingWrapper#`PyBindErrorHandlingWrapper<PyBindType>`(8e935d9c2e576e3a).
  PyBindErrorHandlingWrapper.def: internal/PyBindErrorHandlingWrapper#def(8cb5bc97a568ddfa).
  PyBindClass.PyBindClass-T-Options...: PyBindClass#`PyBindClass<T, Options...>`(6237dafbaf136d61).
  ErrorHandlingHelper: internal/ErrorHandlingHelper#
  PyBindModule.Import: PyBindModule#Import(5df5a1a95db29467).
  PyBindClass.def_readwrite: PyBindClass#def_readwrite(fb4d20943f91d2b9).
  PyBindClass.wrapped_: PyBindClass#wrapped_.
  WrapWithErrorHandling: internal/WrapWithErrorHandling(f1cba5ac2036ec63).
  PyBindErrorHandlingWrapper: internal/PyBindErrorHandlingWrapper#
  PyBindErrorHandlingWrapper.prefix_: internal/PyBindErrorHandlingWrapper#prefix_.
  PyBindModule.wrapped_: PyBindModule#wrapped_.
  PyBindErrorHandlingWrapper.wrapped_: internal/PyBindErrorHandlingWrapper#wrapped_.
  WrapWithErrorHandling.FuncType: internal/WrapWithErrorHandling(f1cba5ac2036ec63).FuncType#
  ErrorHandlingHelper.wrap: internal/ErrorHandlingHelper#wrap(e3e0f68e0ae3e1ef).
  PyBindWrapWithErrorHandling: PyBindWrapWithErrorHandling(df80c7d91d68be3f).
  PyBindModule.def_submodule: PyBindModule#def_submodule(52aaec2cae298b03).
  IsPyBindClass: internal/IsPyBindClass#
  PyBindModule.doc: PyBindModule#doc(1d9ba80bac720809).
  PyBindClass.prefix_: PyBindClass#prefix_.
  PyBindErrorHandlingWrapper.def_readonly: internal/PyBindErrorHandlingWrapper#def_readonly(37a08d1cd34bf2b5).
  WrapWithErrorHandling.InferredTraits: internal/WrapWithErrorHandling(f1cba5ac2036ec63).InferredTraits#
  PyBindClass.RawClass: PyBindClass#RawClass#
---
# Module: [`csrc/common/pybind_error_utils.h`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h)

## Classes
### <a id="ErrorHandlingHelper"></a>`ErrorHandlingHelper`
- def: [`csrc/common/pybind_error_utils.h:62`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L62)
- doc: Helper struct to wrap functions bound to Python APIs with TorchTPU error
- signature: `template <typename Ret, typename... Args> struct ErrorHandlingHelper<Ret(Args...)>`
- members:
  - <a id="ErrorHandlingHelper.impl"></a>`impl(const std::string_view api_name, const F& f, Args... args)` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L71) — TorchTPU specific logic in the wrapper.
  - <a id="ErrorHandlingHelper.wrap"></a>`wrap(const std::string_view api_name, const F& f)` — [`L83`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L83) — Wraps the Python API callable in a lambda that executes with proper
- uses (calls/refs, reference-scoped): [`TranslateToC10ErrorAndThrow`](error_utils.cc.md#TranslateToC10ErrorAndThrow), [`TtError`](error_utils.h.md#TtError), [`ScopedPythonContextCapturer`](../ops/python_context.h.md#ScopedPythonContextCapturer), [`ScopedPythonContextCapturer`](../ops/python_context.cc.md#ScopedPythonContextCapturer.ScopedPythonContextCapturer), [`PythonApiName`](../ops/python_context.h.md#PythonApiName.PythonApiName), [`PythonApiName`](../ops/python_context.h.md#PythonApiName)
- used by: [`TestBody`](pybind_error_utils_test.cc.md#PyBindErrorUtilsInternalTest_ImplMemberFunctionLambdaThrowsC10Error_Test.TestBody), [`TestHelperRaises`](pybind_error_utils_test.cc.md#TestHelperRaises), [`FuncType`](pybind_error_utils.h.md#WrapWithErrorHandling.FuncType), [`IsPyBindClass`](pybind_error_utils.h.md#IsPyBindClass)

### <a id="IsPyBindClass"></a>`IsPyBindClass`  ·  implements/extends integral_constant
- def: [`csrc/common/pybind_error_utils.h:42`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L42)
- doc: Detects if a type is pybind11 class_.
- signature: `template <typename T> struct IsPyBindClass : std::false_type`
- uses (calls/refs, reference-scoped): [`ErrorHandlingHelper`](pybind_error_utils.h.md#ErrorHandlingHelper)
- used by: [`PyBindErrorHandlingWrapper<PyBindType>`](pybind_error_utils.h.md#PyBindErrorHandlingWrapper.PyBindErrorHandlingWrapper-PyBindType), [`PyBindErrorHandlingWrapper`](pybind_error_utils.h.md#PyBindErrorHandlingWrapper)

### <a id="PyBindClass"></a>`PyBindClass`
- def: [`csrc/common/pybind_error_utils.h:262`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L262)
- doc: Wrapper around pybind11 class_ constructor to automatically wrap `def()`
- signature: `template <typename T, typename... Options> class PyBindClass`
- members:
  - <a id="PyBindClass.PyBindClass-T-Options..."></a>`PyBindClass<T, Options...>(PyBindModule& m, const char* name, const Extra&... extra)` — [`L268`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L268)
  - `def(Init&& init, Extra&&... extra)` — [`L280`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L280) — Overload for init or other non-named defs (e.g., py::init with py::arg):
  - <a id="PyBindClass.def"></a>`def(const char* name, const F& f, const Extra&... extra)` — [`L288`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L288) — Registers the Python API `name` to the function `f` wrapped with TorchTPU
  - <a id="PyBindClass.def_property"></a>`def_property(const char* name, const Getter& getter, const Setter& setter, const Extra&... extra)` — [`L330`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L330) — Registers a read-write property `name` using `getter` and `setter` wrapped
  - <a id="PyBindClass.def_property_readonly"></a>`def_property_readonly(const char* name, const Getter& f, const Extra&... extra)` — [`L319`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L319) — Registers a read-only property `name` using getter function `f` wrapped
  - <a id="PyBindClass.def_readonly"></a>`def_readonly(Args&&... args)` — [`L300`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L300) — Forwards `def_readonly()` to the wrapped class_ without wrapping it with
  - <a id="PyBindClass.def_readwrite"></a>`def_readwrite(Args&&... args)` — [`L311`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L311) — Forwards `def_readwrite()` to the wrapped pybind11 class_ without
  - <a id="PyBindClass.prefix_"></a>`prefix_` — [`L341`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L341)
  - <a id="PyBindClass.wrapped_"></a>`wrapped_` — [`L340`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L340)
- uses (calls/refs, reference-scoped): [`PyBindModule`](pybind_error_utils.h.md#PyBindModule), [`GetPyBindHandle`](pybind_error_utils.h.md#GetPyBindHandle), [`WrapWithErrorHandling`](pybind_error_utils.h.md#WrapWithErrorHandling), [`RawClass`](pybind_error_utils.h.md#PyBindClass.RawClass)
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](../internal/compile/tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`TorchTpuPyBindInitModule_testing`](../internal/testing.cc.md#TorchTpuPyBindInitModule_testing), [`TorchTpuPyBindInitModule_tpu_distributed`](../internal/distributed/tpu_distributed.cc.md#TorchTpuPyBindInitModule_tpu_distributed), [`TorchTpuPyBindInitModule_batch_transfer_impl`](../internal/batch_transfer/batch_transfer_impl.cc.md#TorchTpuPyBindInitModule_batch_transfer_impl), [`TorchTpuPyBindInitModule__tpu_torch_dynamism`](../internal/dynamism/dynamism_py.cc.md#TorchTpuPyBindInitModule__tpu_torch_dynamism)

### <a id="PyBindClass.RawClass"></a>`PyBindClass.RawClass`
- def: [`csrc/common/pybind_error_utils.h:264`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L264)
- signature: `using RawClass = pybind11::class_<T, Options...>`
- used by: [`def_property`](pybind_error_utils.h.md#PyBindClass.def_property)

### <a id="PyBindErrorHandlingWrapper"></a>`PyBindErrorHandlingWrapper`
- def: [`csrc/common/pybind_error_utils.h:133`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L133)
- doc: Wrapper around pybind11 objects to automatically wrap `def()` calls with
- signature: `PyBindErrorHandlingWrapper`
- members:
  - <a id="PyBindErrorHandlingWrapper.PyBindErrorHandlingWrapper-PyBindType"></a>`PyBindErrorHandlingWrapper<PyBindType>(PyBindType& wrapped)` — [`L147`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L147) — If `PyBindType` is a class, it sets the `prefix_` to "<class-name>."
  - `def(Func&& f)` — [`L164`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L164) — Overload for single-argument def (like py::init): forwards directly.
  - <a id="PyBindErrorHandlingWrapper.def"></a>`def(const char* name, const F& f, const Extra&... extra)` — [`L175`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L175) — Registers the Python API `name` to the function `f` wrapped by the
  - <a id="PyBindErrorHandlingWrapper.def_readonly"></a>`def_readonly(Args&&... args)` — [`L157`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L157) — Forward other common pybind11 class methods we use.
  - <a id="PyBindErrorHandlingWrapper.prefix_"></a>`prefix_` — [`L198`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L198) — The prefix string prepended to the API name.
  - <a id="PyBindErrorHandlingWrapper.wrapped_"></a>`wrapped_` — [`L189`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L189) — The pybind11 module or class object being wrapped.
- uses (calls/refs, reference-scoped): [`WrapWithErrorHandling`](pybind_error_utils.h.md#WrapWithErrorHandling), [`IsPyBindClass`](pybind_error_utils.h.md#IsPyBindClass)
- used by: [`PyBindWrapWithErrorHandling`](pybind_error_utils.h.md#PyBindWrapWithErrorHandling)

### <a id="PyBindModule"></a>`PyBindModule`
- def: [`csrc/common/pybind_error_utils.h:215`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L215)
- doc: Wrapper around pybind11 module_ to automatically wrap `def()` calls with
- signature: `class PyBindModule`
- members:
  - <a id="PyBindModule.Import"></a>`Import(const char* name)` — [`L236`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L236) — Imports an existing Python module and wraps it in a `PyBindModule`.
  - <a id="PyBindModule.PyBindModule"></a>`PyBindModule(pybind11::module_ wrapped)` — [`L217`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L217)
  - <a id="PyBindModule.attr"></a>`attr(const char* name)` — [`L243`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L243)
  - <a id="PyBindModule.def"></a>`def(const char* name, const F& f, const Extra&... extra)` — [`L224`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L224) — Registers the Python API `name` to the function `f` wrapped with TorchTPU
  - <a id="PyBindModule.def_submodule"></a>`def_submodule(const char* name, const Extra&... extra)` — [`L231`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L231) — Creates and returns a new submodule wrapped in a `PyBindModule`.
  - <a id="PyBindModule.doc"></a>`doc()` — [`L242`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L242)
  - <a id="PyBindModule.wrapped_"></a>`wrapped_` — [`L248`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L248) — RAW_PYBIND_OK=Wrapper implementation.
- uses (calls/refs, reference-scoped): [`GetPyBindHandle`](pybind_error_utils.h.md#GetPyBindHandle), [`WrapWithErrorHandling`](pybind_error_utils.h.md#WrapWithErrorHandling)
- used by: [`TorchTpuPyBindInitModule_tpu_torch_compile`](../internal/compile/tpu_torch_compile.cc.md#TorchTpuPyBindInitModule_tpu_torch_compile), [`TorchTpuPyBindInitModule_testing`](../internal/testing.cc.md#TorchTpuPyBindInitModule_testing), [`TorchTpuPyBindInitModule_tpu_distributed`](../internal/distributed/tpu_distributed.cc.md#TorchTpuPyBindInitModule_tpu_distributed), [`TorchTpuPyBindInitModule_execution_mode_impl`](../internal/execution_mode/execution_mode_impl.cc.md#TorchTpuPyBindInitModule_execution_mode_impl), [`TorchTpuPyBindInitModule_warnings_impl`](../internal/warnings_impl.cc.md#TorchTpuPyBindInitModule_warnings_impl), [`TorchTpuPyBindInitModule__profiler_backend`](../internal/profiler/profiler_api.cc.md#TorchTpuPyBindInitModule__profiler_backend), [`TorchTpuPyBindInitModule_batch_transfer_impl`](../internal/batch_transfer/batch_transfer_impl.cc.md#TorchTpuPyBindInitModule_batch_transfer_impl), [`TorchTpuPyBindInitModule__tpu_torch_sync`](../internal/sync/sync_py.cc.md#TorchTpuPyBindInitModule__tpu_torch_sync), [`TorchTpuPyBindInitModule_env`](../internal/env.cc.md#TorchTpuPyBindInitModule_env), [`TorchTpuPyBindInitModule__tpu_torch_dynamism`](../internal/dynamism/dynamism_py.cc.md#TorchTpuPyBindInitModule__tpu_torch_dynamism), [`TorchTpuPyBindInitModule_precision_impl`](../internal/precision/precision_impl.cc.md#TorchTpuPyBindInitModule_precision_impl), [`TorchTpuPyBindInitModule_tpu_torch_pallas`](../internal/pallas/pallas_py.cc.md#TorchTpuPyBindInitModule_tpu_torch_pallas), [`GetPyBindHandle`](pybind_error_utils.h.md#GetPyBindHandle), [`TorchTpuPyBindInitModule_compiler_options_impl`](../internal/compiler_options/compiler_options_impl.cc.md#TorchTpuPyBindInitModule_compiler_options_impl), [`PyBindClass<T, Options...>`](pybind_error_utils.h.md#PyBindClass.PyBindClass-T-Options...), [`ResetDefaultDeviceGenerators`](../internal/testing.cc.md#ResetDefaultDeviceGenerators)

### <a id="WrapWithErrorHandling.FuncType"></a>`WrapWithErrorHandling.FuncType`
- def: [`csrc/common/pybind_error_utils.h:119`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L119)
- signature: `using FuncType = typename InferredTraits::func_type`
- uses (calls/refs, reference-scoped): [`ErrorHandlingHelper`](pybind_error_utils.h.md#ErrorHandlingHelper), [`InferredTraits`](pybind_error_utils.h.md#WrapWithErrorHandling.InferredTraits)

### <a id="WrapWithErrorHandling.InferredTraits"></a>`WrapWithErrorHandling.InferredTraits`
- def: [`csrc/common/pybind_error_utils.h:118`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L118)
- signature: `using InferredTraits = typename c10::guts::infer_function_traits<F>::type`
- used by: [`FuncType`](pybind_error_utils.h.md#WrapWithErrorHandling.FuncType)

## Functions
- <a id="GetPyBindHandle"></a>`GetPyBindHandle(const PyBindModule& m)` — [`L255`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L255) — Returns the underlying pybind11 handle from a `PyBindModule` instance.
- <a id="PyBindWrapWithErrorHandling"></a>`PyBindWrapWithErrorHandling(T& wrapped)` — [`L208`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L208) — Creates a PyBindErrorHandlingWrapper for a pybind11 object.
- <a id="WrapWithErrorHandling"></a>`WrapWithErrorHandling(const std::string_view api_name, const F& f)` — [`L117`](../../../../../../raw/code/torch_tpu/csrc/common/pybind_error_utils.h#L117) — Unified helper that extracts function signature traits using PyTorch's

