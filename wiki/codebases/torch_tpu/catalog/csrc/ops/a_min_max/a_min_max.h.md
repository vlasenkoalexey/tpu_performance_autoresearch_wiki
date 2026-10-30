---
title: 'Module: csrc/ops/a_min_max/a_min_max.h'
type: catalog
provenance: extracted
module: csrc/ops/a_min_max/a_min_max.h
status: fresh
symbol_base: cxx . . $ torch_tpu/AMinMaxOp#
symbols:
  AMinMaxOp.kAmin: kAmin.
  AMinMaxOp: ''
  AMinMaxOp.kAmax: kAmax.
---
# Module: [`csrc/ops/a_min_max/a_min_max.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/a_min_max/a_min_max.h)

## Classes
### <a id="AMinMaxOp"></a>`AMinMaxOp`
- def: [`csrc/ops/a_min_max/a_min_max.h:28`](../../../../../../../raw/code/torch_tpu/csrc/ops/a_min_max/a_min_max.h#L28)
- signature: `enum class AMinMaxOp`
- members:
  - <a id="AMinMaxOp.kAmax"></a>`kAmax` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/a_min_max/a_min_max.h#L29)
  - <a id="AMinMaxOp.kAmin"></a>`kAmin` — [`L30`](../../../../../../../raw/code/torch_tpu/csrc/ops/a_min_max/a_min_max.h#L30)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions), [`MlirOpResults`](../op_builder_utils.h.md#MlirOpResults), [`ReductionMode`](../reductions/reductions.h.md#ReductionMode), [`BuildAMinMaxShlo`](a_min_max.cc.md#BuildAMinMaxShlo), [`BuildFusedAMinMaxShlo`](a_min_max.cc.md#BuildFusedAMinMaxShlo), [`BuildFusedAMinMaxShlo`](a_min_max.cc.md#BuildFusedAMinMaxShlo)
- used by: [`AtenAmaxOut`](a_min_max_aten_kernels.cc.md#AtenAmaxOut), [`AtenAminOut`](a_min_max_aten_kernels.cc.md#AtenAminOut), [`AMinMax`](a_min_max_aten_kernels.cc.md#AMinMax), [`BuildAMinMaxShlo`](a_min_max.cc.md#BuildAMinMaxShlo), [`GetOpName`](a_min_max_aten_kernels.cc.md#GetOpName)

