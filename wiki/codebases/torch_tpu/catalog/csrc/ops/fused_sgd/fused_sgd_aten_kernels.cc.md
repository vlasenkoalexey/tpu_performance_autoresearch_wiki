---
title: 'Module: csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenFusedSgdTensorLr: AtenFusedSgdTensorLr(3288d7647ee2c8b7).
  AtenFusedSgd: AtenFusedSgd(2df38b5b0e074d0f).
  DispatchSgd: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/DispatchSgd(603efda95e022564).'
  BuildSgdShlo: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/BuildSgdShlo(a11c3c78c3af61d8).'
  BuildSgdStepForOneParam: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/BuildSgdStepForOneParam(ec6b819403f6b69c).'
  ValidateSgdTensorListSizes: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/ValidateSgdTensorListSizes(173068af927da865).'
  SetSgdParamCacheKeys: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SetSgdParamCacheKeys(e4827a271556e314).'
  ApplyFoundInfRevert: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/ApplyFoundInfRevert(37f039461d405f03).'
  AssignBuffers: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/AssignBuffers(68f0efce82a960d6).'
  AppendDtypes: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/AppendDtypes(9449544dff2f41b4).'
  MomentumMode: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/MomentumMode#'
  CastOneParamOutputs: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/CastOneParamOutputs(deaacb0f3da2248).'
  ExtractSgdInputs: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/ExtractSgdInputs(85d751c5a5b132b7).'
  GradScaleMode: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/GradScaleMode#'
  GatherSgdOutDtypes: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/GatherSgdOutDtypes(33f3be4ae37d12d1).'
  GatherSgdOutDims: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/GatherSgdOutDims(4e18e52879cb75d8).'
  AssignSgdResultBuffers: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/AssignSgdResultBuffers(d35a449eaa150b87).'
  GatherSgdInputs: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/GatherSgdInputs(b63aef76d7dcea57).'
  ExtractSgdDtypes: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/ExtractSgdDtypes(9592a78b17df12b2).'
  CombineSgdResults: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/CombineSgdResults(cf1cfbc495d52504).'
  OneParamResult.momentum_buffer: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/OneParamResult#momentum_buffer.'
  MomentumMode.kEnabled: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/MomentumMode#kEnabled.'
  GetMomentumMode: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/GetMomentumMode(e065a29791d03060).'
  GetGradScaleMode: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/GetGradScaleMode(9571ae46e3dcae0f).'
  OneParamResult.grad: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/OneParamResult#grad.'
  GetFoundInfMode: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/GetFoundInfMode(78cf493ad9e67ae9).'
  FoundInfMode: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/FoundInfMode#'
  GradScaleMode.kEnabled: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/GradScaleMode#kEnabled.'
  OneParamResult.param: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/OneParamResult#param.'
  MetaFusedSgd: MetaFusedSgd(2df38b5b0e074d0f).
  OneParamResult: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/OneParamResult#'
  MetaFusedSgdTensorLr: MetaFusedSgdTensorLr(3288d7647ee2c8b7).
  MetaFusedSgdFunctionalTensorLr: MetaFusedSgdFunctionalTensorLr(2c999f8a21d1a323).
  AppendDims: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/AppendDims(9449544dff2f41b4).'
  MetaFusedSgdFunctional: MetaFusedSgdFunctional(efa87d5a6ba31056).
  SgdDtypeSpans: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdDtypeSpans#'
  SgdInputSpans: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdInputSpans#'
  NesterovMode: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/NesterovMode#'
  SgdObjectiveMode: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdObjectiveMode#'
  SgdDtypeSpans.grads: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdDtypeSpans#grads.'
  IsFirstStepMode: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/IsFirstStepMode#'
  SgdInputSpans.grads: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdInputSpans#grads.'
  SgdInputSpans.params: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdInputSpans#params.'
  SgdDtypeSpans.params: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdDtypeSpans#params.'
  FoundInfMode.kEnabled: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/FoundInfMode#kEnabled.'
  SgdDtypeSpans.momentum_buffers: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdDtypeSpans#momentum_buffers.'
  SgdInputSpans.grad_scale: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdInputSpans#grad_scale.'
  SgdInputSpans.momentum: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdInputSpans#momentum.'
  SgdInputSpans.momentum_buffers: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdInputSpans#momentum_buffers.'
  SgdInputSpans.dampening: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdInputSpans#dampening.'
  SgdInputSpans.weight_decay: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdInputSpans#weight_decay.'
  SgdInputSpans.lr: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdInputSpans#lr.'
  SgdInputSpans.found_inf: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdInputSpans#found_inf.'
  NesterovMode.kEnabled: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/NesterovMode#kEnabled.'
  IsFirstStepMode.kTrue: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/IsFirstStepMode#kTrue.'
  SgdObjectiveMode.kMaximize: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdObjectiveMode#kMaximize.'
  NesterovMode.kDisabled: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/NesterovMode#kDisabled.'
  SgdObjectiveMode.kMinimize: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/SgdObjectiveMode#kMinimize.'
  IsFirstStepMode.kFalse: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/IsFirstStepMode#kFalse.'
  GradScaleMode.kDisabled: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/GradScaleMode#kDisabled.'
  FoundInfMode.kDisabled: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/FoundInfMode#kDisabled.'
  MomentumMode.kDisabled: '`$anonymous_namespace_csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`/MomentumMode#kDisabled.'
---
# Module: [`csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc)

## Classes
### <a id="FoundInfMode"></a>`FoundInfMode`
- def: [`csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc:58`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L58)
- signature: `enum class FoundInfMode : bool`
- members:
  - <a id="FoundInfMode.kDisabled"></a>`kDisabled` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L58)
  - <a id="FoundInfMode.kEnabled"></a>`kEnabled` — [`L58`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L58)
- used by: [`DispatchSgd`](fused_sgd_aten_kernels.cc.md#DispatchSgd), [`BuildSgdShlo`](fused_sgd_aten_kernels.cc.md#BuildSgdShlo), [`SetSgdParamCacheKeys`](fused_sgd_aten_kernels.cc.md#SetSgdParamCacheKeys), [`ExtractSgdInputs`](fused_sgd_aten_kernels.cc.md#ExtractSgdInputs), [`GatherSgdInputs`](fused_sgd_aten_kernels.cc.md#GatherSgdInputs), [`GetGradScaleMode`](fused_sgd_aten_kernels.cc.md#GetGradScaleMode), [`GetFoundInfMode`](fused_sgd_aten_kernels.cc.md#GetFoundInfMode)

### <a id="GradScaleMode"></a>`GradScaleMode`
- def: [`csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc:57`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L57)
- signature: `enum class GradScaleMode : bool`
- members:
  - <a id="GradScaleMode.kDisabled"></a>`kDisabled` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L57)
  - <a id="GradScaleMode.kEnabled"></a>`kEnabled` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L57)
- used by: [`DispatchSgd`](fused_sgd_aten_kernels.cc.md#DispatchSgd), [`BuildSgdShlo`](fused_sgd_aten_kernels.cc.md#BuildSgdShlo), [`SetSgdParamCacheKeys`](fused_sgd_aten_kernels.cc.md#SetSgdParamCacheKeys), [`ExtractSgdInputs`](fused_sgd_aten_kernels.cc.md#ExtractSgdInputs), [`GatherSgdOutDtypes`](fused_sgd_aten_kernels.cc.md#GatherSgdOutDtypes), [`AssignSgdResultBuffers`](fused_sgd_aten_kernels.cc.md#AssignSgdResultBuffers), [`GatherSgdOutDims`](fused_sgd_aten_kernels.cc.md#GatherSgdOutDims), [`GatherSgdInputs`](fused_sgd_aten_kernels.cc.md#GatherSgdInputs), [`ExtractSgdDtypes`](fused_sgd_aten_kernels.cc.md#ExtractSgdDtypes), [`CombineSgdResults`](fused_sgd_aten_kernels.cc.md#CombineSgdResults), [`GetGradScaleMode`](fused_sgd_aten_kernels.cc.md#GetGradScaleMode), [`GetMomentumMode`](fused_sgd_aten_kernels.cc.md#GetMomentumMode)

### <a id="IsFirstStepMode"></a>`IsFirstStepMode`
- def: [`csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc:55`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L55)
- signature: `enum class IsFirstStepMode : bool`
- members:
  - <a id="IsFirstStepMode.kFalse"></a>`kFalse` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L55)
  - <a id="IsFirstStepMode.kTrue"></a>`kTrue` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L55)
- used by: [`AtenFusedSgd`](fused_sgd_aten_kernels.cc.md#AtenFusedSgd), [`AtenFusedSgdTensorLr`](fused_sgd_aten_kernels.cc.md#AtenFusedSgdTensorLr), [`DispatchSgd`](fused_sgd_aten_kernels.cc.md#DispatchSgd), [`BuildSgdShlo`](fused_sgd_aten_kernels.cc.md#BuildSgdShlo), [`BuildSgdStepForOneParam`](fused_sgd_aten_kernels.cc.md#BuildSgdStepForOneParam)

### <a id="MomentumMode"></a>`MomentumMode`
- def: [`csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc:56`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L56)
- signature: `enum class MomentumMode : bool`
- members:
  - <a id="MomentumMode.kDisabled"></a>`kDisabled` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L56)
  - <a id="MomentumMode.kEnabled"></a>`kEnabled` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L56)
- used by: [`DispatchSgd`](fused_sgd_aten_kernels.cc.md#DispatchSgd), [`BuildSgdShlo`](fused_sgd_aten_kernels.cc.md#BuildSgdShlo), [`BuildSgdStepForOneParam`](fused_sgd_aten_kernels.cc.md#BuildSgdStepForOneParam), [`ValidateSgdTensorListSizes`](fused_sgd_aten_kernels.cc.md#ValidateSgdTensorListSizes), [`SetSgdParamCacheKeys`](fused_sgd_aten_kernels.cc.md#SetSgdParamCacheKeys), [`ApplyFoundInfRevert`](fused_sgd_aten_kernels.cc.md#ApplyFoundInfRevert), [`CastOneParamOutputs`](fused_sgd_aten_kernels.cc.md#CastOneParamOutputs), [`ExtractSgdInputs`](fused_sgd_aten_kernels.cc.md#ExtractSgdInputs), [`GatherSgdOutDtypes`](fused_sgd_aten_kernels.cc.md#GatherSgdOutDtypes), [`AssignSgdResultBuffers`](fused_sgd_aten_kernels.cc.md#AssignSgdResultBuffers), [`GatherSgdOutDims`](fused_sgd_aten_kernels.cc.md#GatherSgdOutDims), [`GatherSgdInputs`](fused_sgd_aten_kernels.cc.md#GatherSgdInputs), [`ExtractSgdDtypes`](fused_sgd_aten_kernels.cc.md#ExtractSgdDtypes), [`CombineSgdResults`](fused_sgd_aten_kernels.cc.md#CombineSgdResults), [`GetMomentumMode`](fused_sgd_aten_kernels.cc.md#GetMomentumMode)

### <a id="NesterovMode"></a>`NesterovMode`
- def: [`csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc:53`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L53)
- signature: `enum class NesterovMode : bool`
- members:
  - <a id="NesterovMode.kDisabled"></a>`kDisabled` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L53)
  - <a id="NesterovMode.kEnabled"></a>`kEnabled` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L53)
- used by: [`AtenFusedSgd`](fused_sgd_aten_kernels.cc.md#AtenFusedSgd), [`AtenFusedSgdTensorLr`](fused_sgd_aten_kernels.cc.md#AtenFusedSgdTensorLr), [`DispatchSgd`](fused_sgd_aten_kernels.cc.md#DispatchSgd), [`BuildSgdShlo`](fused_sgd_aten_kernels.cc.md#BuildSgdShlo), [`BuildSgdStepForOneParam`](fused_sgd_aten_kernels.cc.md#BuildSgdStepForOneParam)

### <a id="OneParamResult"></a>`OneParamResult`
- def: [`csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc:89`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L89)
- signature: `struct OneParamResult`
- members:
  - <a id="OneParamResult.grad"></a>`grad` — [`L91`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L91)
  - <a id="OneParamResult.momentum_buffer"></a>`momentum_buffer` — [`L92`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L92)
  - <a id="OneParamResult.param"></a>`param` — [`L90`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L90)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildSgdShlo`](fused_sgd_aten_kernels.cc.md#BuildSgdShlo), [`BuildSgdStepForOneParam`](fused_sgd_aten_kernels.cc.md#BuildSgdStepForOneParam), [`ApplyFoundInfRevert`](fused_sgd_aten_kernels.cc.md#ApplyFoundInfRevert), [`CastOneParamOutputs`](fused_sgd_aten_kernels.cc.md#CastOneParamOutputs)

### <a id="SgdDtypeSpans"></a>`SgdDtypeSpans`
- def: [`csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc:306`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L306)
- signature: `struct SgdDtypeSpans`
- members:
  - <a id="SgdDtypeSpans.grads"></a>`grads` — [`L308`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L308)
  - <a id="SgdDtypeSpans.momentum_buffers"></a>`momentum_buffers` — [`L309`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L309)
  - <a id="SgdDtypeSpans.params"></a>`params` — [`L307`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L307)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildSgdShlo`](fused_sgd_aten_kernels.cc.md#BuildSgdShlo), [`ExtractSgdDtypes`](fused_sgd_aten_kernels.cc.md#ExtractSgdDtypes)

### <a id="SgdInputSpans"></a>`SgdInputSpans`
- def: [`csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc:261`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L261)
- signature: `struct SgdInputSpans`
- members:
  - <a id="SgdInputSpans.dampening"></a>`dampening` — [`L268`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L268)
  - <a id="SgdInputSpans.found_inf"></a>`found_inf` — [`L270`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L270)
  - <a id="SgdInputSpans.grad_scale"></a>`grad_scale` — [`L269`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L269)
  - <a id="SgdInputSpans.grads"></a>`grads` — [`L263`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L263)
  - <a id="SgdInputSpans.lr"></a>`lr` — [`L267`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L267)
  - <a id="SgdInputSpans.momentum"></a>`momentum` — [`L266`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L266)
  - <a id="SgdInputSpans.momentum_buffers"></a>`momentum_buffers` — [`L264`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L264)
  - <a id="SgdInputSpans.params"></a>`params` — [`L262`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L262)
  - <a id="SgdInputSpans.weight_decay"></a>`weight_decay` — [`L265`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L265)
- uses (calls/refs, reference-scoped): (none in-repo)
- used by: [`BuildSgdShlo`](fused_sgd_aten_kernels.cc.md#BuildSgdShlo), [`ExtractSgdInputs`](fused_sgd_aten_kernels.cc.md#ExtractSgdInputs)

### <a id="SgdObjectiveMode"></a>`SgdObjectiveMode`
- def: [`csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc:54`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L54)
- signature: `enum class SgdObjectiveMode : bool`
- members:
  - <a id="SgdObjectiveMode.kMaximize"></a>`kMaximize` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L54)
  - <a id="SgdObjectiveMode.kMinimize"></a>`kMinimize` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L54)
- used by: [`AtenFusedSgd`](fused_sgd_aten_kernels.cc.md#AtenFusedSgd), [`AtenFusedSgdTensorLr`](fused_sgd_aten_kernels.cc.md#AtenFusedSgdTensorLr), [`DispatchSgd`](fused_sgd_aten_kernels.cc.md#DispatchSgd), [`BuildSgdShlo`](fused_sgd_aten_kernels.cc.md#BuildSgdShlo), [`BuildSgdStepForOneParam`](fused_sgd_aten_kernels.cc.md#BuildSgdStepForOneParam)

## Functions
- `AppendDims(const at::TensorList tensors, std::vector<absl::Span<const int64_t>>& out_dims)` — [`L81`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L81) — Appends dimension spans of input tensors to the output dimension vector.
- <a id="AppendDims"></a>`AppendDims(const at::TensorList tensors, std::vector<absl::Span<const int64_t>>& out_dims)` — [`L81`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L81) — Appends dimension spans of input tensors to the output dimension vector.
- <a id="AppendDtypes"></a>`AppendDtypes(const at::TensorList tensors, std::vector<mlir::ElementType>& out_dtypes)` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L70) — Appends converted MLIR element types of input tensors to the output vector.
- `AppendDtypes(const at::TensorList tensors, std::vector<mlir::ElementType>& out_dtypes)` — [`L70`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L70) — Appends converted MLIR element types of input tensors to the output vector.
- <a id="ApplyFoundInfRevert"></a>`ApplyFoundInfRevert(OneParamResult current, mlir::MlirOp param_old, mlir::MlirOp grad_old, std::optional<mlir::MlirOp> momentum_buffer_old, mlir::MlirOp found_inf, mlir::ElementType comp_type, const MomentumMode momentum_mode)` — [`L97`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L97) — Reverts parameter, gradient, and moment tensors to pre-step values if inf/nan
- `AssignBuffers(std::vector<DeviceBufferRef>& buffers, const size_t offset, const at::TensorList tensors)` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L61) — Assigns compiled output device buffers to input tensors starting at offset.
- <a id="AssignBuffers"></a>`AssignBuffers(std::vector<DeviceBufferRef>& buffers, const size_t offset, const at::TensorList tensors)` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L61) — Assigns compiled output device buffers to input tensors starting at offset.
- `AssignSgdResultBuffers(std::vector<DeviceBufferRef>& result_buffers, at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode)` — [`L544`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L544) — Assigns compiled TPU device buffers back to ATen tensor inputs and optimizer
- <a id="AssignSgdResultBuffers"></a>`AssignSgdResultBuffers(std::vector<DeviceBufferRef>& result_buffers, at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode)` — [`L544`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L544) — Assigns compiled TPU device buffers back to ATen tensor inputs and optimizer
- <a id="AtenFusedSgd"></a>`AtenFusedSgd(at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, double weight_decay, double momentum, double lr, double dampening, bool nesterov, bool maximize, bool is_first_step, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf)` — [`L638`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L638) — Executes multi-tensor SGD optimizer step with a scalar learning rate. — documented in [fused-optimizer-kernels](../../../../concepts/fused-optimizer-kernels.md)
- <a id="AtenFusedSgdTensorLr"></a>`AtenFusedSgdTensorLr(at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, double weight_decay, double momentum, const at::Tensor& lr, double dampening, bool nesterov, bool maximize, bool is_first_step, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf)` — [`L682`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L682) — Executes multi-tensor SGD optimizer step with a tensor learning rate.
- <a id="BuildSgdShlo"></a>`BuildSgdShlo(absl::Span<mlir::MlirOp> inputs, const size_t num_tensors, const MomentumMode momentum_mode, const NesterovMode nesterov_mode, const SgdObjectiveMode maximize_mode, const IsFirstStepMode is_first_step_mode, const GradScaleMode grad_scale_mode, const FoundInfMode found_inf_mode, absl::Span<const mlir::ElementType> out_dtypes)` — [`L361`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L361) — Constructs the combined StableHLO graph for all tensors in the optimizer
- `BuildSgdShlo(absl::Span<mlir::MlirOp> inputs, const size_t num_tensors, const MomentumMode momentum_mode, const NesterovMode nesterov_mode, const SgdObjectiveMode maximize_mode, const IsFirstStepMode is_first_step_mode, const GradScaleMode grad_scale_mode, const FoundInfMode found_inf_mode, absl::Span<const mlir::ElementType> out_dtypes)` — [`L361`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L361) — Constructs the combined StableHLO graph for all tensors in the optimizer
- <a id="BuildSgdStepForOneParam"></a>`BuildSgdStepForOneParam(mlir::MlirOp param, mlir::MlirOp grad, std::optional<mlir::MlirOp> momentum_buffer, mlir::MlirOp lr, mlir::MlirOp weight_decay, mlir::MlirOp momentum, mlir::MlirOp dampening, const NesterovMode nesterov_mode, const SgdObjectiveMode maximize_mode, const IsFirstStepMode is_first_step_mode, std::optional<mlir::MlirOp> grad_scale, std::optional<mlir::MlirOp> found_inf, mlir::ElementType param_dtype, mlir::ElementType grad_dtype, std::optional<mlir::ElementType> momentum_buffer_dtype, const MomentumMode momentum_mode)` — [`L158`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L158) — Builds the StableHLO graph for updating a single parameter tensor and its
- <a id="CastOneParamOutputs"></a>`CastOneParamOutputs(OneParamResult res, mlir::ElementType param_dtype, mlir::ElementType grad_dtype, std::optional<mlir::ElementType> momentum_buffer_dtype, const MomentumMode momentum_mode)` — [`L132`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L132) — Casts computed intermediate ops back to their respective target output buffer
- `CombineSgdResults(const std::vector<mlir::MlirOp>& params, const std::vector<mlir::MlirOp>& grads, const std::vector<mlir::MlirOp>& momentum_buffers, const size_t num_tensors, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode)` — [`L338`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L338) — Combines updated parameter, gradient, and momentum MLIR handles into a single
- <a id="CombineSgdResults"></a>`CombineSgdResults(const std::vector<mlir::MlirOp>& params, const std::vector<mlir::MlirOp>& grads, const std::vector<mlir::MlirOp>& momentum_buffers, const size_t num_tensors, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode)` — [`L338`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L338) — Combines updated parameter, gradient, and momentum MLIR handles into a single
- <a id="DispatchSgd"></a>`DispatchSgd(at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, const at::Tensor& weight_decay_tensor, const at::Tensor& momentum_tensor, const at::Tensor& lr_tensor, const at::Tensor& dampening_tensor, const NesterovMode nesterov_mode, const SgdObjectiveMode maximize_mode, const IsFirstStepMode is_first_step_mode, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf, OpParamCacheKeys param_keys)` — [`L565`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L565) — Dispatches multi-tensor SGD optimizer computation to TPU runtime.
- <a id="ExtractSgdDtypes"></a>`ExtractSgdDtypes(absl::Span<const mlir::ElementType> out_dtypes, const size_t num_tensors, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode)` — [`L314`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L314) — Extracts individual output element type spans for parameters, gradients, and
- <a id="ExtractSgdInputs"></a>`ExtractSgdInputs(absl::Span<mlir::MlirOp> inputs, const size_t num_tensors, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode, const FoundInfMode found_inf_mode)` — [`L275`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L275) — Extracts individual input spans and optional tensors from the flattened MLIR
- `GatherSgdInputs(at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, const at::Tensor& weight_decay_tensor, const at::Tensor& momentum_tensor, const at::Tensor& lr_tensor, const at::Tensor& dampening_tensor, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode, const FoundInfMode found_inf_mode)` — [`L467`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L467) — Gathers and flattens all input tensors and scalar hyperparameters into a
- <a id="GatherSgdInputs"></a>`GatherSgdInputs(at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, const at::Tensor& weight_decay_tensor, const at::Tensor& momentum_tensor, const at::Tensor& lr_tensor, const at::Tensor& dampening_tensor, const std::optional<at::Tensor>& grad_scale, const std::optional<at::Tensor>& found_inf, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode, const FoundInfMode found_inf_mode)` — [`L467`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L467) — Gathers and flattens all input tensors and scalar hyperparameters into a
- `GatherSgdOutDims(at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode)` — [`L522`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L522) — Gathers output tensor shapes for parameters, gradients, and momentum buffers.
- <a id="GatherSgdOutDims"></a>`GatherSgdOutDims(at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode)` — [`L522`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L522) — Gathers output tensor shapes for parameters, gradients, and momentum buffers.
- <a id="GatherSgdOutDtypes"></a>`GatherSgdOutDtypes(at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode)` — [`L501`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L501) — Gathers output element types for parameters, gradients, and momentum buffers.
- `GatherSgdOutDtypes(at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode)` — [`L501`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L501) — Gathers output element types for parameters, gradients, and momentum buffers.
- <a id="GetFoundInfMode"></a>`GetFoundInfMode(const std::optional<at::Tensor>& found_inf)` — [`L445`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L445) — Determines whether inf/nan checking and conditional reversion is enabled.
- <a id="GetGradScaleMode"></a>`GetGradScaleMode(const std::optional<at::Tensor>& grad_scale)` — [`L438`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L438) — Determines whether gradient unscaling is enabled based on scale tensor
- <a id="GetMomentumMode"></a>`GetMomentumMode(at::TensorList momentum_buffer_list)` — [`L431`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L431) — Determines whether momentum computation is enabled based on momentum buffer
- <a id="MetaFusedSgd"></a>`MetaFusedSgd(at::TensorList /*self*/, at::TensorList /*grads*/, at::TensorList /*momentum_buffer_list*/, double /*weight_decay*/, double /*momentum*/, double /*lr*/, double /*dampening*/, bool /*nesterov*/, bool /*maximize*/, bool /*is_first_step*/, const std::optional<at::Tensor>& /*grad_scale*/, const std::optional<at::Tensor>& /*found_inf*/)` — [`L728`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L728) — Meta kernel for in-place `aten::_fused_sgd_` (scalar `double lr` overload,
- <a id="MetaFusedSgdFunctional"></a>`MetaFusedSgdFunctional(at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, double /*weight_decay*/, double /*momentum*/, double /*lr*/, double /*dampening*/, bool /*nesterov*/, bool /*maximize*/, bool /*is_first_step*/, const std::optional<at::Tensor>& /*grad_scale*/, const std::optional<at::Tensor>& /*found_inf*/)` — [`L756`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L756) — Meta kernel for out-of-place functional `aten::_fused_sgd` (scalar `double
- <a id="MetaFusedSgdFunctionalTensorLr"></a>`MetaFusedSgdFunctionalTensorLr(at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, double /*weight_decay*/, double /*momentum*/, const at::Tensor& /*lr*/, double /*dampening*/, bool /*nesterov*/, bool /*maximize*/, bool /*is_first_step*/, const std::optional<at::Tensor>& /*grad_scale*/, const std::optional<at::Tensor>& /*found_inf*/)` — [`L780`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L780) — Meta kernel for out-of-place functional `aten::_fused_sgd.tensor_lr` (`const
- <a id="MetaFusedSgdTensorLr"></a>`MetaFusedSgdTensorLr(at::TensorList /*self*/, at::TensorList /*grads*/, at::TensorList /*momentum_buffer_list*/, double /*weight_decay*/, double /*momentum*/, const at::Tensor& /*lr*/, double /*dampening*/, bool /*nesterov*/, bool /*maximize*/, bool /*is_first_step*/, const std::optional<at::Tensor>& /*grad_scale*/, const std::optional<at::Tensor>& /*found_inf*/)` — [`L741`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L741) — Meta kernel for in-place `aten::_fused_sgd_.tensor_lr` (`const at::Tensor&
- <a id="SetSgdParamCacheKeys"></a>`SetSgdParamCacheKeys(OpParamCacheKeys& param_keys, const MomentumMode momentum_mode, const GradScaleMode grad_scale_mode, const FoundInfMode found_inf_mode)` — [`L453`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L453) — Sets cache key parameters for optional optimizer features (grad scale,
- <a id="ValidateSgdTensorListSizes"></a>`ValidateSgdTensorListSizes(at::TensorList self, at::TensorList grads, at::TensorList momentum_buffer_list, const MomentumMode momentum_mode)` — [`L412`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_sgd/fused_sgd_aten_kernels.cc#L412) — Validates that gradient and momentum buffer lists match the parameter tensor

