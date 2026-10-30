---
title: 'Module: csrc/common/fingerprint_utils.h'
type: catalog
provenance: extracted
module: csrc/common/fingerprint_utils.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  Fingerprint: Fingerprint(c6bf0951926639cd).
  FingerprintType: FingerprintType#
  FingerprintCat: FingerprintCat(e98ad67573a95bd1).
  Fingerprint64Impl.Compute: internal/Fingerprint64Impl#Compute(ec40c8edbfccc0c6).
---
# Module: [`csrc/common/fingerprint_utils.h`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h)

## Classes
### <a id="FingerprintType"></a>`FingerprintType`
- def: [`csrc/common/fingerprint_utils.h:42`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L42)
- doc: Represents the fingerprint of a chunk of data.
- signature: `using FingerprintType = uint64_t`
- uses (calls/refs, reference-scoped): [`Fingerprint`](fingerprint_utils.h.md#Fingerprint)
- used by: [`Fingerprint`](fingerprint_utils.h.md#Fingerprint), [`EncodeParamCacheKey`](cache_key.cc.md#EncodeParamCacheKey), [`EncodeParamCacheKey`](cache_key.cc.md#EncodeParamCacheKey), [`live_data_ptrs`](../eager/device_buffer.cc.md#DeviceBufferRef.live_data_ptrs), [`EncodeParamCacheKey`](cache_key.h.md#EncodeParamCacheKey), [`EncodeParamCacheKey`](cache_key.cc.md#EncodeParamCacheKey), [`EncodeParamCacheKey`](cache_key.h.md#EncodeParamCacheKey), [`Hash`](../eager/device_buffer.cc.md#DeferredOp.Hash), [`EncodeParamCacheKey`](cache_key.cc.md#EncodeParamCacheKey), [`Result`](cache_key.h.md#EncodeParamCacheKeyForRange.Result), [`ReturnType`](cache_key.h.md#OpParamCacheKeys.SetParam.ReturnType), [`Kernel5`](../ops/macros/kernel_test.cc.md#Kernel5), [`FingerprintCat`](fingerprint_utils.h.md#FingerprintCat), [`FingerprintedKey`](cache_key.h.md#FingerprintedKey), [`ApplyCompilerOptionOverrides`](compilation.cc.md#ApplyCompilerOptionOverrides), [`GetCrossHostTransferKey`](../distributed/process_group_tpu.cc.md#GetCrossHostTransferKey), [`GetTorchTpuBinaryFingerprint`](compilation_cache_utils.cc.md#GetTorchTpuBinaryFingerprint), [`CompileOptionsKey`](compile_options_key.h.md#CompileOptionsKey.CompileOptionsKey), [`EncodeParamCacheKey`](cache_key.h.md#EncodeParamCacheKey), [`EncodeParamCacheKey`](cache_key.h.md#EncodeParamCacheKey), [`EncodeParamCacheKey`](cache_key.h.md#EncodeParamCacheKey), [`AnnotateGraphKeyWithArgumentLayouts`](../eager/traversal.cc.md#AnnotateGraphKeyWithArgumentLayouts), [`TestBody`](../eager/device_buffer_utils_test.cc.md#DeviceBufferUtilsTest_ComputeConstantDeviceBufferRefOpParamCacheKeysMatchesGoldenMap_Test.TestBody), [`key`](compile_options_key.h.md#CompileOptionsKey.key), [`EncodeParamCacheKey`](cache_key.h.md#EncodeParamCacheKey), [`EncodeParamCacheKey`](cache_key.h.md#EncodeParamCacheKey), [`FingerprintCat`](fingerprint_utils.h.md#FingerprintCat), [`ShapelessKey`](cache_key.h.md#ShapelessKey.ShapelessKey), [`U`](cache_key.h.md#IncludeInCacheKey.U), [`TestBody`](cache_key_test.cc.md#OpParamCacheKeys_SetParamDouble_Test.TestBody), [`SetDefaultDeviceAssignment`](compilation.cc.md#SetDefaultDeviceAssignment), [`FingerprintCat`](fingerprint_utils.h.md#FingerprintCat), [`EncodeParamCacheKey`](cache_key.h.md#EncodeParamCacheKey), [`TestBody`](compile_options_key_test.cc.md#CompileOptionsKeyDeathTest_LibtpuInitArgsAffectsFingerprint_Test.TestBody), [`EncodeParamCacheKey`](cache_key.h.md#EncodeParamCacheKey), [`EncodeParamCacheKey`](cache_key.h.md#EncodeParamCacheKey), [`EncodeParamCacheKey`](cache_key.h.md#EncodeParamCacheKey), [`GetPjRtVersion`](compilation_cache_utils.cc.md#GetPjRtVersion), [`AbslStringify`](compilation_cache_utils.h.md#AbslStringify), [`Fingerprint`](compilation.cc.md#Fingerprint)  (+22 more)

## Functions
- <a id="Fingerprint"></a>`Fingerprint(const T& t)` — [`L168`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L168) — Returns the fingerprint of the given value.
- `FingerprintCat(const T& t)` — [`L185`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L185)
- `FingerprintCat()` — [`L183`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L183) — FingerprintCat(ts...) returns the fingerprint of the given values in a
- <a id="FingerprintCat"></a>`FingerprintCat(const T0& t0, const T1& t1, const Ts&... ts)` — [`L190`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L190) — The recursive case. — documented in [compilation-cache-key](../../../concepts/compilation-cache-key.md)

## Other members
- `Compute` — [`L121`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L121)
- `Compute` — [`L64`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L64)
- `Compute` — [`L93`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L93)
- `Compute` — [`L114`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L114)
- `Compute` — [`L130`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L130)
- `Compute` — [`L140`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L140)
- `Compute` — [`L102`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L102)
- `Compute` — [`L84`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L84)
- `Compute` — [`L155`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L155)
- <a id="Fingerprint64Impl.Compute"></a>`Fingerprint64Impl.Compute` — [`L72`](../../../../../../raw/code/torch_tpu/csrc/common/fingerprint_utils.h#L72)

