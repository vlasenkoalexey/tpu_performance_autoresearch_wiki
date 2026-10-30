---
title: 'Module: csrc/ops/macros/kernel.h'
type: catalog
provenance: extracted
module: csrc/ops/macros/kernel.h
status: fresh
symbol_base: cxx . . $ torch_tpu/internal/
symbols:
  InvalidOpParamCacheKeys.InvalidOpParamCacheKeys: InvalidOpParamCacheKeys#InvalidOpParamCacheKeys(ced63f7c635d850d).
  InvalidOpParamCacheKeys: InvalidOpParamCacheKeys#
  ConditionalStaticAssert: ConditionalStaticAssert(49f6e7a06ebc5aa8).
  AppendPromotedScalarPointers: AppendPromotedScalarPointers(faa3ced3b054be0d).
  CollectPromotedScalarPointers: CollectPromotedScalarPointers(3e14da6c51b5d798).
  ArgDoesNotAffectCacheKey.value: ArgDoesNotAffectCacheKey#value.
  NoArgAffectsCacheKey.value: NoArgAffectsCacheKey#value.
  ArgDoesNotAffectCacheKey: ArgDoesNotAffectCacheKey#
  NoArgAffectsCacheKey: NoArgAffectsCacheKey#
  NoArgAffectsCacheKey.NoArgAffectsCacheKey-Ts...: NoArgAffectsCacheKey#`NoArgAffectsCacheKey<Ts...>`(3eb398314feba58b).
---
# Module: [`csrc/ops/macros/kernel.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h)

## Classes
### <a id="ArgDoesNotAffectCacheKey"></a>`ArgDoesNotAffectCacheKey`
- def: [`csrc/ops/macros/kernel.h:261`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L261)
- doc: Checks if an argument should be ignored in the cache key.
- signature: `template <size_t kParamIndex, typename ParamType> struct ArgDoesNotAffectCacheKey`
- members:
  - <a id="ArgDoesNotAffectCacheKey.value"></a>`value` — [`L262`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L262)
- uses (calls/refs, reference-scoped): [`IncludeInCacheKey`](../../common/cache_key.h.md#IncludeInCacheKey)
- used by: [`value`](kernel.h.md#NoArgAffectsCacheKey.value)

### <a id="InvalidOpParamCacheKeys"></a>`InvalidOpParamCacheKeys`
- def: [`csrc/ops/macros/kernel.h:223`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L223) — documented in [aten-kernel-authoring](../../../../concepts/aten-kernel-authoring.md)
- doc: A type that can't be used to do anything useful.
- signature: `class InvalidOpParamCacheKeys`
- members:
  - <a id="InvalidOpParamCacheKeys.InvalidOpParamCacheKeys"></a>`InvalidOpParamCacheKeys()` — [`L225`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L225) — documented in [aten-kernel-authoring](../../../../concepts/aten-kernel-authoring.md)
  - `InvalidOpParamCacheKeys()` — [`L225`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L225)
- uses (calls/refs, reference-scoped): [`OpParamCacheKeys`](../../common/cache_key.h.md#OpParamCacheKeys), [`IncludeInCacheKey`](../../common/cache_key.h.md#IncludeInCacheKey)
- used by: [`alltoall`](../../distributed/process_group_tpu.cc.md#ProcessGroupTpu.alltoall), [`AtenPreluKernelBackward`](../prelu/prelu_aten_kernels.cc.md#AtenPreluKernelBackward), [`AtenMaskedScatter_`](../masked_scatter/masked_scatter_aten_kernels.cc.md#AtenMaskedScatter_), [`AtenPreluKernel`](../prelu/prelu_aten_kernels.cc.md#AtenPreluKernel), [`AtenWeightNormInterface`](../weight_norm/weight_norm_aten_kernels.cc.md#AtenWeightNormInterface), [`AtenChannelShuffle`](../channel_shuffle/channel_shuffle_aten_kernels.cc.md#AtenChannelShuffle), [`AtenIndexTensorOut`](../index/index_aten_kernels.cc.md#AtenIndexTensorOut), [`allgather`](../../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allgather), [`AtenCtcLossTensor`](../ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossTensor), [`AtenVarMeanCorrection`](../reductions/var_aten_kernels.cc.md#AtenVarMeanCorrection), [`AtenDigammaOut`](../digamma/digamma_aten_kernels.cc.md#AtenDigammaOut), [`_allgather_base`](../../distributed/process_group_tpu.cc.md#ProcessGroupTpu._allgather_base), [`AtenBinCount`](../bincount/bincount_aten_kernels.cc.md#AtenBinCount), [`AtenCtcLossBackwardTensor`](../ctc_loss/ctc_loss_aten_kernels.cc.md#AtenCtcLossBackwardTensor), [`AtenRmsNorm`](../rms_norm/rms_norm_aten_kernels.cc.md#AtenRmsNorm), [`allreduce`](../../distributed/process_group_tpu.cc.md#ProcessGroupTpu.allreduce), [`AtenLinalgLuSolveOut`](../linalg/lu/linalg_lu_kernels.cc.md#AtenLinalgLuSolveOut), [`AtenFusedRmsNorm`](../rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNorm), [`AtenArangeStartOut`](../arange/arange_aten_kernels.cc.md#AtenArangeStartOut), [`AtenFusedRmsNormBackward`](../rms_norm/rms_norm_aten_kernels.cc.md#AtenFusedRmsNormBackward), [`AtenLinalgSolveExOut`](../linalg/linalg_kernels.cc.md#AtenLinalgSolveExOut), [`AtenReplicationPad3dBackward`](../replication_pad/replication_pad_aten_kernels.cc.md#AtenReplicationPad3dBackward), [`gather`](../../distributed/process_group_tpu.cc.md#ProcessGroupTpu.gather), [`AtenLinalgSvdU`](../linalg/linalg_svd_kernels.cc.md#AtenLinalgSvdU), [`AtenSegmentReduce`](../segment_reduce/segment_reduce_aten_kernels.cc.md#AtenSegmentReduce), [`_reduce_scatter_base`](../../distributed/process_group_tpu.cc.md#ProcessGroupTpu._reduce_scatter_base), [`AtenLinalgInvExInverse`](../linalg/linalg_kernels.cc.md#AtenLinalgInvExInverse), [`AtenAdaptiveAvgPool3dOut`](../pooling/adaptive_avg_pool_aten_kernels.cc.md#AtenAdaptiveAvgPool3dOut), [`AtenGridSampler3dBackward`](../grid_sampler/grid_sampler_aten_kernels.cc.md#AtenGridSampler3dBackward), [`AtenNativeGroupNormBackward`](../group_norm/group_norm_aten_kernels.cc.md#AtenNativeGroupNormBackward), [`AtenViewAsComplex`](../view/view_aten_kernels.cc.md#AtenViewAsComplex), [`AtenCdistBackward`](../distance/dist_aten_kernels.cc.md#AtenCdistBackward), [`AtenCdistForward`](../distance/dist_aten_kernels.cc.md#AtenCdistForward), [`AtenExponential_`](../exponential/exponential_aten_kernels.cc.md#AtenExponential_), [`AtenLinalgLuFactorExOut`](../linalg/lu/linalg_lu_kernels.cc.md#AtenLinalgLuFactorExOut), [`AtenLinspaceOut`](../linspace/linspace_aten_kernels.cc.md#AtenLinspaceOut), [`AtenReflectionPad2dBackward`](../reflection_pad/reflection_pad_aten_kernels.cc.md#AtenReflectionPad2dBackward), [`AtenReplicationPad2dBackward`](../replication_pad/replication_pad_aten_kernels.cc.md#AtenReplicationPad2dBackward), [`AtenSelectScatterOut`](../select_scatter/select_scatter_aten_kernels.cc.md#AtenSelectScatterOut), [`AtenSliceScatterOut`](../slice_scatter/slice_scatter_aten_kernels.cc.md#AtenSliceScatterOut)  (+726 more)

### <a id="NoArgAffectsCacheKey"></a>`NoArgAffectsCacheKey`
- def: [`csrc/ops/macros/kernel.h:289`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L289)
- doc: Checks if all arguments in a pack should be ignored in the cache key.
- signature: `template <typename... Ts> struct NoArgAffectsCacheKey`
- members:
  - <a id="NoArgAffectsCacheKey.NoArgAffectsCacheKey-Ts..."></a>`NoArgAffectsCacheKey<Ts...>(const Ts&...)` — [`L290`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L290)
  - <a id="NoArgAffectsCacheKey.value"></a>`value` — [`L292`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L292)
- uses (calls/refs, reference-scoped): [`ArgDoesNotAffectCacheKey`](kernel.h.md#ArgDoesNotAffectCacheKey)

## Functions
- `AppendPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const std::optional<PromotedScalar>& arg)` — [`L177`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L177) — Case: std::optional<PromotedScalar>
- `AppendPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const PromotedScalar& arg)` — [`L171`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L171) — Case: PromotedScalar
- `AppendPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const std::optional<PromotedScalar>& arg)` — [`L177`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L177) — Case: std::optional<PromotedScalar>
- `AppendPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const IgnoredInCacheKey<T>& arg)` — [`L191`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L191) — Case: IgnoredInCacheKey<T>
- <a id="AppendPromotedScalarPointers"></a>`AppendPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const PromotedScalar& arg)` — [`L171`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L171) — Case: PromotedScalar
- `AppendPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const T& arg)` — [`L198`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L198) — Case: anything else (no-op)
- `AppendPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const IgnoredInCacheKey<T>& arg)` — [`L191`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L191) — Case: IgnoredInCacheKey<T>
- `AppendPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const T& arg)` — [`L198`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L198) — Case: anything else (no-op)
- <a id="CollectPromotedScalarPointers"></a>`CollectPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const T& arg, const Args&... rest_args)` — [`L208`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L208) — Recursive case: collect pointers from the next argument and then call the — documented in [aten-kernel-authoring](../../../../concepts/aten-kernel-authoring.md)
- `CollectPromotedScalarPointers(PromotedTensorStates& promoted_scalars, const T& arg, const Args&... rest_args)` — [`L208`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L208) — Recursive case: collect pointers from the next argument and then call the
- `CollectPromotedScalarPointers(PromotedTensorStates& promoted_scalars)` — [`L202`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L202) — Base case: 0 arguments to collect.
- `CollectPromotedScalarPointers(PromotedTensorStates& promoted_scalars)` — [`L202`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L202) — Base case: 0 arguments to collect.
- <a id="ConditionalStaticAssert"></a>`ConditionalStaticAssert()` — [`L335`](../../../../../../../raw/code/torch_tpu/csrc/ops/macros/kernel.h#L335) — ConditionalStaticAssert() is a helper to trigger a static_assert inside a

