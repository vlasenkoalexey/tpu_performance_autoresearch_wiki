---
title: 'Module: csrc/internal/testing.cc'
type: catalog
provenance: extracted
module: csrc/internal/testing.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  TorchTpuPyBindInitModule_testing: TorchTpuPyBindInitModule_testing(d5b68cea704bb038).
  ThrowTtErrorInFreeFunction: '`$anonymous_namespace_csrc/internal/testing.cc`/ThrowTtErrorInFreeFunction(49f6e7a06ebc5aa8).'
  ThrowTtErrorIndexError: '`$anonymous_namespace_csrc/internal/testing.cc`/ThrowTtErrorIndexError(49f6e7a06ebc5aa8).'
  TestErrorClass.ThrowTtErrorInMemberFunction: '`$anonymous_namespace_csrc/internal/testing.cc`/TestErrorClass#ThrowTtErrorInMemberFunction(49f6e7a06ebc5aa8).'
  PyGetMemoryKind: '`$anonymous_namespace_csrc/internal/testing.cc`/PyGetMemoryKind(1afa6f5962e0729).'
  EmitTtWarn: '`$anonymous_namespace_csrc/internal/testing.cc`/EmitTtWarn(f2a0e2f180426392).'
  EmitTtWarnOnce: '`$anonymous_namespace_csrc/internal/testing.cc`/EmitTtWarnOnce(f2a0e2f180426392).'
  ResetDefaultDeviceGenerators: '`$anonymous_namespace_csrc/internal/testing.cc`/ResetDefaultDeviceGenerators(49f6e7a06ebc5aa8).'
  pybind11_init_testing: pybind11_init_testing(85901dfccbeca8c6).
  pybind11_exec_testing: pybind11_exec_testing(6642082b04e1bfd8).
  ResetEagerState: '`$anonymous_namespace_csrc/internal/testing.cc`/ResetEagerState(49f6e7a06ebc5aa8).'
  TestMembersClass: '`$anonymous_namespace_csrc/internal/testing.cc`/TestMembersClass#'
  EmitTorchWarnDeprecation: '`$anonymous_namespace_csrc/internal/testing.cc`/EmitTorchWarnDeprecation(9c546c94e5fcce4e).'
  EmitTorchWarn: '`$anonymous_namespace_csrc/internal/testing.cc`/EmitTorchWarn(9c546c94e5fcce4e).'
  EmitTorchWarnOnce: '`$anonymous_namespace_csrc/internal/testing.cc`/EmitTorchWarnOnce(9c546c94e5fcce4e).'
  TestErrorClass: '`$anonymous_namespace_csrc/internal/testing.cc`/TestErrorClass#'
  TestMembersClass.read_only_field: '`$anonymous_namespace_csrc/internal/testing.cc`/TestMembersClass#read_only_field.'
  TestMembersClass.read_write_field: '`$anonymous_namespace_csrc/internal/testing.cc`/TestMembersClass#read_write_field.'
---
# Module: [`csrc/internal/testing.cc`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc)

## Classes
### <a id="TestErrorClass"></a>`TestErrorClass`
- def: [`csrc/internal/testing.cc:87`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L87)
- doc: Test fixtures used by pybind_error_utils_test to verify Python API error
- signature: `struct TestErrorClass`
- members:
  - <a id="TestErrorClass.ThrowTtErrorInMemberFunction"></a>`ThrowTtErrorInMemberFunction()` — [`L88`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L88)
- uses (calls/refs, reference-scoped): [`NormalizeIfInsideBuildDirectory`](../common/macro_utils.cc.md#NormalizeIfInsideBuildDirectory), [`GetRootOpName`](../ops/python_context.cc.md#GetRootOpName), [`SetRootOpNamePayload`](../common/status_builder.cc.md#SetRootOpNamePayload), [`operator<<`](../common/status_builder.h.md#StatusBuilder.operator), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor), [`ReturnIfErrorAdaptor`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ReturnIfErrorAdaptor), [`kInvalidArgument`](../common/error_utils.h.md#kInvalidArgument), [`operator=`](../common/error_utils.h.md#ThrowIfErrorAdapter.operator), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter.ThrowIfErrorAdapter), [`ThrowIfErrorAdapter`](../common/error_utils.h.md#ThrowIfErrorAdapter), [`ConsumeRequiringMessage`](../common/error_utils.h.md#ReturnIfErrorAdaptor.ConsumeRequiringMessage)
- used by: [`TorchTpuPyBindInitModule_testing`](testing.cc.md#TorchTpuPyBindInitModule_testing)

### <a id="TestMembersClass"></a>`TestMembersClass`
- def: [`csrc/internal/testing.cc:109`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L109)
- doc: Test struct used by pybind_error_utils_test to verify correct forwarding of
- signature: `struct TestMembersClass`
- members:
  - <a id="TestMembersClass.read_only_field"></a>`read_only_field` — [`L110`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L110)
  - <a id="TestMembersClass.read_write_field"></a>`read_write_field` — [`L111`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L111)
- used by: [`TorchTpuPyBindInitModule_testing`](testing.cc.md#TorchTpuPyBindInitModule_testing)

## Functions
- <a id="EmitTorchWarn"></a>`EmitTorchWarn(const std::string& msg)` — [`L114`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L114)
- <a id="EmitTorchWarnDeprecation"></a>`EmitTorchWarnDeprecation(const std::string& msg)` — [`L126`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L126)
- <a id="EmitTorchWarnOnce"></a>`EmitTorchWarnOnce(const std::string& msg)` — [`L120`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L120)
- <a id="EmitTtWarn"></a>`EmitTtWarn(WarningCategory category, const std::string& msg)` — [`L132`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L132)
- <a id="EmitTtWarnOnce"></a>`EmitTtWarnOnce(WarningCategory category, const std::string& msg)` — [`L138`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L138)
- <a id="PyGetMemoryKind"></a>`PyGetMemoryKind(const at::Tensor& tensor)` — [`L74`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L74)
- <a id="ResetDefaultDeviceGenerators"></a>`ResetDefaultDeviceGenerators()` — [`L55`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L55) — Resets default device generators across both C++ and Python.
- <a id="ResetEagerState"></a>`ResetEagerState()` — [`L45`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L45)
- <a id="ThrowTtErrorInFreeFunction"></a>`ThrowTtErrorInFreeFunction()` — [`L95`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L95)
- <a id="ThrowTtErrorIndexError"></a>`ThrowTtErrorIndexError()` — [`L101`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L101)
- <a id="TorchTpuPyBindInitModule_testing"></a>`TorchTpuPyBindInitModule_testing(testing, m)` — [`L147`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L147)
- <a id="pybind11_exec_testing"></a>`pybind11_exec_testing(testing, m)` — [`L147`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L147)
- <a id="pybind11_init_testing"></a>`pybind11_init_testing(testing, m)` — [`L147`](../../../../../../raw/code/torch_tpu/csrc/internal/testing.cc#L147)

