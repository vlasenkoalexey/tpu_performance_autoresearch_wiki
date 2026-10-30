---
title: 'Module: csrc/common/warnings.h'
type: catalog
provenance: extracted
module: csrc/common/warnings.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  GetWarningPrefix: GetWarningPrefix(5d4ea0d2eb13d895).
  WarningCategory: WarningCategory#
  IsDeprecationWarning: IsDeprecationWarning(aa9b99c898bfdac7).
  WarningCategory.kPerformance: WarningCategory#kPerformance.
  WarningCategory.kTorchTpu: WarningCategory#kTorchTpu.
  WarningCategory.kCorrectness: WarningCategory#kCorrectness.
  WarningCategory.kDeprecatedApi: WarningCategory#kDeprecatedApi.
  WarningCategory.kExperimentalApi: WarningCategory#kExperimentalApi.
  WarningCategory.kUnoptimizedBuild: WarningCategory#kUnoptimizedBuild.
  WarningCategory.kApiStage: WarningCategory#kApiStage.
  WarningCategory.kTcMalloc: WarningCategory#kTcMalloc.
  WarningCategory.kInternalApi: WarningCategory#kInternalApi.
---
# Module: [`csrc/common/warnings.h`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h)

## Classes
### <a id="WarningCategory"></a>`WarningCategory`
- def: [`csrc/common/warnings.h:36`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h#L36)
- doc: Categories of the warnings TorchTPU emits, from both C++ and Python.
- signature: `enum class WarningCategory`
- members:
  - <a id="WarningCategory.kApiStage"></a>`kApiStage` — [`L42`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h#L42)
  - <a id="WarningCategory.kCorrectness"></a>`kCorrectness` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h#L41)
  - <a id="WarningCategory.kDeprecatedApi"></a>`kDeprecatedApi` — [`L45`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h#L45)
  - <a id="WarningCategory.kExperimentalApi"></a>`kExperimentalApi` — [`L44`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h#L44)
  - <a id="WarningCategory.kInternalApi"></a>`kInternalApi` — [`L43`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h#L43)
  - <a id="WarningCategory.kPerformance"></a>`kPerformance` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h#L38)
  - <a id="WarningCategory.kTcMalloc"></a>`kTcMalloc` — [`L40`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h#L40)
  - <a id="WarningCategory.kTorchTpu"></a>`kTorchTpu` — [`L37`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h#L37)
  - <a id="WarningCategory.kUnoptimizedBuild"></a>`kUnoptimizedBuild` — [`L39`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h#L39)
- used by: [`HistcHelperOut`](../ops/histc/histc_aten_kernels.cc.md#HistcHelperOut), [`ValidateTakeInputs`](../ops/take/take_aten_kernels.cc.md#ValidateTakeInputs), [`AtenFusedSdpChoice`](../ops/scaled_dot_product_attention/scaled_dot_product_attention_aten_kernels.cc.md#AtenFusedSdpChoice), [`TpuMemcpyDtoH`](../pjrt/pjrt_transfer.cc.md#TpuMemcpyDtoH), [`AtenAoWaitTensor`](../ops/ao/ao_offload_kernels.cc.md#AtenAoWaitTensor), [`GetEnvOnce`](env_vars.h.md#GetEnvOnce), [`ValidateDeviceIndex`](../eager/tpu_hooks.cc.md#ValidateDeviceIndex), [`PyUnsafeGetPrecision`](../ops/precision_context.cc.md#PyUnsafeGetPrecision), [`GetWarningPrefix`](warnings.h.md#GetWarningPrefix), [`TorchTpuPyBindInitModule_warnings_impl`](../internal/warnings_impl.cc.md#TorchTpuPyBindInitModule_warnings_impl), [`GetBooleanEnvOnce`](env_vars.h.md#GetBooleanEnvOnce), [`IsDeprecationWarning`](warnings.h.md#IsDeprecationWarning), [`WarnIfInvalidCorrection`](../ops/reductions/var_aten_kernels.cc.md#WarnIfInvalidCorrection), [`ImplExperimental`](../eager/tpu_aten_kernels.cc.md#ImplExperimental), [`WarnIfInvalidCorrection`](../ops/reductions/std_aten_kernels.cc.md#WarnIfInvalidCorrection), [`GetIntegerEnvOnce`](env_vars.h.md#GetIntegerEnvOnce), [`ImplDeprecated`](../eager/tpu_aten_kernels.cc.md#ImplDeprecated), [`getDeviceStats`](../eager/tensor_to_buffer.cc.md#TpuAllocator.getDeviceStats), [`getMemoryInfo`](../eager/tensor_to_buffer.cc.md#TpuAllocator.getMemoryInfo), [`resetPeakStats`](../eager/tensor_to_buffer.cc.md#TpuAllocator.resetPeakStats), [`block`](../eager/tpu_hooks.cc.md#TpuDeviceGuardImpl.block), [`queryStream`](../eager/tpu_hooks.cc.md#TpuDeviceGuardImpl.queryStream), [`empty_cache`](../eager/tensor_to_buffer.cc.md#TpuPinnedAllocator.empty_cache), [`EmitTtWarn`](../internal/testing.cc.md#EmitTtWarn), [`EmitTtWarnOnce`](../internal/testing.cc.md#EmitTtWarnOnce), [`resetAccumulatedStats`](../eager/tensor_to_buffer.cc.md#TpuAllocator.resetAccumulatedStats)

## Functions
- <a id="GetWarningPrefix"></a>`GetWarningPrefix(WarningCategory category)` — [`L49`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h#L49) — Returns the message prefix of warnings in `category`.
- <a id="IsDeprecationWarning"></a>`IsDeprecationWarning(WarningCategory category)` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/common/warnings.h#L75) — Returns whether warnings in `category` are emitted as Python

