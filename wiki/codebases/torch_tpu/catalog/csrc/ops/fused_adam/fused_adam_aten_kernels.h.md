---
title: 'Module: csrc/ops/fused_adam/fused_adam_aten_kernels.h'
type: catalog
provenance: extracted
module: csrc/ops/fused_adam/fused_adam_aten_kernels.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AdamStepConfig.maximize: AdamStepConfig#maximize(50ce9a9e25b4a850).
  AdamStepConfig.amsgrad: AdamStepConfig#amsgrad(50ce9a9e25b4a850).
  AdamAmsgradMode: AdamAmsgradMode#
  AdamObjectiveMode: AdamObjectiveMode#
  AdamStepConfig: AdamStepConfig#
  AdamAmsgradMode.kEnabled: AdamAmsgradMode#kEnabled.
  AdamStepConfig.has_grad_scale: AdamStepConfig#has_grad_scale.
  AdamStepConfig.amsgrad_mode: AdamStepConfig#amsgrad_mode.
  AdamObjectiveMode.kMaximize: AdamObjectiveMode#kMaximize.
  AdamAmsgradMode.kDisabled: AdamAmsgradMode#kDisabled.
  AdamObjectiveMode.kMinimize: AdamObjectiveMode#kMinimize.
  AdamStepConfig.maximize_mode: AdamStepConfig#maximize_mode.
  AdamStepConfig.has_found_inf: AdamStepConfig#has_found_inf.
---
# Module: [`csrc/ops/fused_adam/fused_adam_aten_kernels.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h)

## Classes
### <a id="AdamAmsgradMode"></a>`AdamAmsgradMode`
- def: [`csrc/ops/fused_adam/fused_adam_aten_kernels.h:27`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L27)
- signature: `enum class AdamAmsgradMode : bool`
- members:
  - <a id="AdamAmsgradMode.kDisabled"></a>`kDisabled` — [`L27`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L27)
  - <a id="AdamAmsgradMode.kEnabled"></a>`kEnabled` — [`L27`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L27)
- used by: [`AtenFusedAdam`](fused_adam_aten_kernels.cc.md#AtenFusedAdam), [`AtenFusedAdamTensorLr`](fused_adam_aten_kernels.cc.md#AtenFusedAdamTensorLr), [`DispatchAdam`](fused_adam_aten_kernels.cc.md#DispatchAdam), [`BuildAdamStepForOneParam`](fused_adam_aten_kernels.cc.md#BuildAdamStepForOneParam), [`amsgrad`](fused_adam_aten_kernels.h.md#AdamStepConfig.amsgrad), [`AdamStepConfig`](fused_adam_aten_kernels.h.md#AdamStepConfig)

### <a id="AdamObjectiveMode"></a>`AdamObjectiveMode`
- def: [`csrc/ops/fused_adam/fused_adam_aten_kernels.h:28`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L28)
- signature: `enum class AdamObjectiveMode : bool`
- members:
  - <a id="AdamObjectiveMode.kMaximize"></a>`kMaximize` — [`L28`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L28)
  - <a id="AdamObjectiveMode.kMinimize"></a>`kMinimize` — [`L28`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L28)
- used by: [`AtenFusedAdam`](fused_adam_aten_kernels.cc.md#AtenFusedAdam), [`AtenFusedAdamTensorLr`](fused_adam_aten_kernels.cc.md#AtenFusedAdamTensorLr), [`DispatchAdam`](fused_adam_aten_kernels.cc.md#DispatchAdam), [`BuildAdamStepForOneParam`](fused_adam_aten_kernels.cc.md#BuildAdamStepForOneParam), [`maximize`](fused_adam_aten_kernels.h.md#AdamStepConfig.maximize), [`amsgrad_mode`](fused_adam_aten_kernels.h.md#AdamStepConfig.amsgrad_mode)

### <a id="AdamStepConfig"></a>`AdamStepConfig`
- def: [`csrc/ops/fused_adam/fused_adam_aten_kernels.h:32`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L32)
- doc: Configuration options for an Adam optimizer step, bundling enum modes and
- signature: `struct AdamStepConfig`
- members:
  - <a id="AdamStepConfig.amsgrad"></a>`amsgrad()` — [`L38`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L38)
  - <a id="AdamStepConfig.maximize"></a>`maximize()` — [`L39`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L39)
  - <a id="AdamStepConfig.amsgrad_mode"></a>`amsgrad_mode` — [`L33`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L33)
  - <a id="AdamStepConfig.has_found_inf"></a>`has_found_inf` — [`L36`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L36)
  - <a id="AdamStepConfig.has_grad_scale"></a>`has_grad_scale` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L35)
  - <a id="AdamStepConfig.maximize_mode"></a>`maximize_mode` — [`L34`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adam/fused_adam_aten_kernels.h#L34)
- uses (calls/refs, reference-scoped): [`AtenFusedAdam`](fused_adam_aten_kernels.cc.md#AtenFusedAdam), [`AtenFusedAdamTensorLr`](fused_adam_aten_kernels.cc.md#AtenFusedAdamTensorLr), [`MetaFusedAdamTensorLr`](fused_adam_aten_kernels.cc.md#MetaFusedAdamTensorLr), [`MetaFusedAdamFunctionalTensorLr`](fused_adam_aten_kernels.cc.md#MetaFusedAdamFunctionalTensorLr), [`AdamAmsgradMode`](fused_adam_aten_kernels.h.md#AdamAmsgradMode), [`MetaFusedAdamFunctional`](fused_adam_aten_kernels.cc.md#MetaFusedAdamFunctional), [`AdamObjectiveMode`](fused_adam_aten_kernels.h.md#AdamObjectiveMode), [`kEnabled`](fused_adam_aten_kernels.h.md#AdamAmsgradMode.kEnabled), [`kMaximize`](fused_adam_aten_kernels.h.md#AdamObjectiveMode.kMaximize)
- used by: [`BuildAdamShlo`](fused_adam_aten_kernels.cc.md#BuildAdamShlo), [`DispatchAdam`](fused_adam_aten_kernels.cc.md#DispatchAdam), [`ExtractAdamInputs`](fused_adam_aten_kernels.cc.md#ExtractAdamInputs), [`ExtractAdamDtypes`](fused_adam_aten_kernels.cc.md#ExtractAdamDtypes)

