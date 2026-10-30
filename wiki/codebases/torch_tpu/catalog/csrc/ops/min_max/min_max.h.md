---
title: 'Module: csrc/ops/min_max/min_max.h'
type: catalog
provenance: extracted
module: csrc/ops/min_max/min_max.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  MinMaxOp: MinMaxOp#
  MinMaxOutputs.indices: MinMaxOutputs#indices.
  MinMaxOp.kMax: MinMaxOp#kMax.
  MinMaxOutputs: MinMaxOutputs#
  MinMaxOutputs.values: MinMaxOutputs#values.
  MinMaxOp.kMin: MinMaxOp#kMin.
---
# Module: [`csrc/ops/min_max/min_max.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.h)

## Classes
### <a id="MinMaxOp"></a>`MinMaxOp`
- def: [`csrc/ops/min_max/min_max.h:29`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.h#L29)
- signature: `enum class MinMaxOp`
- members:
  - <a id="MinMaxOp.kMax"></a>`kMax` — [`L30`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.h#L30)
  - <a id="MinMaxOp.kMin"></a>`kMin` — [`L31`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.h#L31)
- used by: [`AtenMax`](min_max_aten_kernels.cc.md#AtenMax), [`AtenMin`](min_max_aten_kernels.cc.md#AtenMin), [`AtenMaxUnaryOut`](min_max_aten_kernels.cc.md#AtenMaxUnaryOut), [`AtenMinUnaryOut`](min_max_aten_kernels.cc.md#AtenMinUnaryOut), [`AtenArgmaxOut`](min_max_aten_kernels.cc.md#AtenArgmaxOut), [`AtenArgminOut`](min_max_aten_kernels.cc.md#AtenArgminOut), [`AtenMaxDimMax`](min_max_aten_kernels.cc.md#AtenMaxDimMax), [`AtenMinDimMin`](min_max_aten_kernels.cc.md#AtenMinDimMin), [`ArgMinMax`](min_max_aten_kernels.cc.md#ArgMinMax), [`UnaryMinMax`](min_max_aten_kernels.cc.md#UnaryMinMax), [`ValidateNormalStdPreconditions`](../normal/normal_aten_kernels.cc.md#ValidateNormalStdPreconditions), [`AtenMinMaxDim`](min_max_aten_kernels.cc.md#AtenMinMaxDim), [`DispatchUnaryMinMax`](min_max_aten_kernels.cc.md#DispatchUnaryMinMax), [`BuildMinMaxShlo`](min_max.cc.md#BuildMinMaxShlo), [`BuildMultinomialShlo`](../multinomial/multinomial.cc.md#BuildMultinomialShlo), [`indices`](min_max.h.md#MinMaxOutputs.indices), [`GetMinMaxInitValue`](min_max.cc.md#GetMinMaxInitValue), [`BuildReduceBody`](min_max.cc.md#BuildReduceBody)

### <a id="MinMaxOutputs"></a>`MinMaxOutputs`
- def: [`csrc/ops/min_max/min_max.h:34`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.h#L34)
- signature: `struct MinMaxOutputs`
- members:
  - <a id="MinMaxOutputs.indices"></a>`indices` — [`L36`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.h#L36)
  - <a id="MinMaxOutputs.values"></a>`values` — [`L35`](../../../../../../../raw/code/torch_tpu/csrc/ops/min_max/min_max.h#L35)
- uses (calls/refs, reference-scoped): [`ReductionMode`](../reductions/reductions.h.md#ReductionMode), [`BuildMinMaxShlo`](min_max.cc.md#BuildMinMaxShlo), [`MinMaxOp`](min_max.h.md#MinMaxOp)
- used by: [`ArgMinMax`](min_max_aten_kernels.cc.md#ArgMinMax), [`UnaryMinMax`](min_max_aten_kernels.cc.md#UnaryMinMax), [`AtenMinMaxDim`](min_max_aten_kernels.cc.md#AtenMinMaxDim), [`DispatchUnaryMinMax`](min_max_aten_kernels.cc.md#DispatchUnaryMinMax), [`BuildMinMaxShlo`](min_max.cc.md#BuildMinMaxShlo), [`BuildMultinomialShlo`](../multinomial/multinomial.cc.md#BuildMultinomialShlo), [`GetMinMaxInitValue`](min_max.cc.md#GetMinMaxInitValue), [`RestoreReducedDims`](min_max.cc.md#RestoreReducedDims)

