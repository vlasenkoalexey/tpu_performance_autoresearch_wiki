---
title: 'Module: csrc/ops/fused_adamw/fused_adamw_aten_kernels.h'
type: catalog
provenance: extracted
module: csrc/ops/fused_adamw/fused_adamw_aten_kernels.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ObjectiveMode.kMaximize: ObjectiveMode#kMaximize.
  AmsgradMode: AmsgradMode#
  ObjectiveMode: ObjectiveMode#
  AmsgradMode.kEnabled: AmsgradMode#kEnabled.
  AmsgradMode.kDisabled: AmsgradMode#kDisabled.
  ObjectiveMode.kMinimize: ObjectiveMode#kMinimize.
---
# Module: [`csrc/ops/fused_adamw/fused_adamw_aten_kernels.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.h)

## Classes
### <a id="AmsgradMode"></a>`AmsgradMode`
- def: [`csrc/ops/fused_adamw/fused_adamw_aten_kernels.h:25`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.h#L25)
- signature: `enum class AmsgradMode : bool`
- members:
  - <a id="AmsgradMode.kDisabled"></a>`kDisabled` — [`L25`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.h#L25)
  - <a id="AmsgradMode.kEnabled"></a>`kEnabled` — [`L25`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.h#L25)
- used by: [`AtenFusedAdamw`](fused_adamw_aten_kernels.cc.md#AtenFusedAdamw), [`AtenFusedAdamwTensorLr`](fused_adamw_aten_kernels.cc.md#AtenFusedAdamwTensorLr), [`BuildAdamwShlo`](fused_adamw_aten_kernels.cc.md#BuildAdamwShlo), [`DispatchAdamw`](fused_adamw_aten_kernels.cc.md#DispatchAdamw), [`BuildAdamwStepForOneParam`](fused_adamw_aten_kernels.cc.md#BuildAdamwStepForOneParam)

### <a id="ObjectiveMode"></a>`ObjectiveMode`
- def: [`csrc/ops/fused_adamw/fused_adamw_aten_kernels.h:26`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.h#L26)
- signature: `enum class ObjectiveMode : bool`
- members:
  - <a id="ObjectiveMode.kMaximize"></a>`kMaximize` — [`L26`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.h#L26)
  - <a id="ObjectiveMode.kMinimize"></a>`kMinimize` — [`L26`](../../../../../../../raw/code/torch_tpu/csrc/ops/fused_adamw/fused_adamw_aten_kernels.h#L26)
- uses (calls/refs, reference-scoped): [`AtenFusedAdamw`](fused_adamw_aten_kernels.cc.md#AtenFusedAdamw), [`AtenFusedAdamwTensorLr`](fused_adamw_aten_kernels.cc.md#AtenFusedAdamwTensorLr)
- used by: [`AtenFusedAdamw`](fused_adamw_aten_kernels.cc.md#AtenFusedAdamw), [`AtenFusedAdamwTensorLr`](fused_adamw_aten_kernels.cc.md#AtenFusedAdamwTensorLr), [`BuildAdamwShlo`](fused_adamw_aten_kernels.cc.md#BuildAdamwShlo), [`DispatchAdamw`](fused_adamw_aten_kernels.cc.md#DispatchAdamw), [`BuildAdamwStepForOneParam`](fused_adamw_aten_kernels.cc.md#BuildAdamwStepForOneParam)

