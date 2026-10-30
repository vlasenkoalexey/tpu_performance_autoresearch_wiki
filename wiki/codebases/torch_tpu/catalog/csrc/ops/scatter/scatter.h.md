---
title: 'Module: csrc/ops/scatter/scatter.h'
type: catalog
provenance: extracted
module: csrc/ops/scatter/scatter.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ScatterOp: ScatterOp#
  EncodeParamCacheKey: EncodeParamCacheKey(7e617100a12d7003).
  ScatterIncludeSelf: ScatterIncludeSelf#
  ScatterIncludeSelf.kYes: ScatterIncludeSelf#kYes.
  ScatterOp.kAdd: ScatterOp#kAdd.
  ScatterOp.kAmax: ScatterOp#kAmax.
  ScatterOp.kProd: ScatterOp#kProd.
  ScatterOp.kSum: ScatterOp#kSum.
  ScatterOp.kMean: ScatterOp#kMean.
  ScatterOp.kAmin: ScatterOp#kAmin.
  ScatterOp.kMul: ScatterOp#kMul.
  ScatterIncludeSelf.kNo: ScatterIncludeSelf#kNo.
  ScatterOp.kReplace: ScatterOp#kReplace.
  ScatterVersion: ScatterVersion#
  ScatterVersion.kV2: ScatterVersion#kV2.
  ScatterVersion.kV1: ScatterVersion#kV1.
---
# Module: [`csrc/ops/scatter/scatter.h`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h)

## Classes
### <a id="ScatterIncludeSelf"></a>`ScatterIncludeSelf`
- def: [`csrc/ops/scatter/scatter.h:32`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L32)
- doc: Whether to include the self tensor in the scatter operation.
- signature: `enum class ScatterIncludeSelf`
- members:
  - <a id="ScatterIncludeSelf.kNo"></a>`kNo` — [`L32`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L32)
  - <a id="ScatterIncludeSelf.kYes"></a>`kYes` — [`L32`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L32)
- used by: [`BuildScatterShlo`](scatter.cc.md#BuildScatterShlo), [`Scatter`](scatter_aten_kernels.cc.md#Scatter), [`AtenScatterReduceOut`](scatter_aten_kernels.cc.md#AtenScatterReduceOut), [`AtenScatterReduceTwoOut`](scatter_aten_kernels.cc.md#AtenScatterReduceTwoOut), [`AtenScatterValueOut`](scatter_aten_kernels.cc.md#AtenScatterValueOut), [`AtenScatterValueReduceOut`](scatter_aten_kernels.cc.md#AtenScatterValueReduceOut), [`AtenScatterSrcOut`](scatter_aten_kernels.cc.md#AtenScatterSrcOut), [`IndexReduce`](../index_reduce/index_reduce_aten_kernels.cc.md#IndexReduce), [`EncodeParamCacheKey`](scatter.h.md#EncodeParamCacheKey)

### <a id="ScatterOp"></a>`ScatterOp`
- def: [`csrc/ops/scatter/scatter.h:29`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L29)
- signature: `enum class ScatterOp`
- members:
  - <a id="ScatterOp.kAdd"></a>`kAdd` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L29)
  - <a id="ScatterOp.kAmax"></a>`kAmax` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L29)
  - <a id="ScatterOp.kAmin"></a>`kAmin` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L29)
  - <a id="ScatterOp.kMean"></a>`kMean` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L29)
  - <a id="ScatterOp.kMul"></a>`kMul` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L29)
  - <a id="ScatterOp.kProd"></a>`kProd` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L29)
  - <a id="ScatterOp.kReplace"></a>`kReplace` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L29)
  - <a id="ScatterOp.kSum"></a>`kSum` — [`L29`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L29)
- used by: [`BuildScatterShlo`](scatter.cc.md#BuildScatterShlo), [`Scatter`](scatter_aten_kernels.cc.md#Scatter), [`AtenScatterReduceOut`](scatter_aten_kernels.cc.md#AtenScatterReduceOut), [`AtenScatterReduceTwoOut`](scatter_aten_kernels.cc.md#AtenScatterReduceTwoOut), [`AtenScatterValueOut`](scatter_aten_kernels.cc.md#AtenScatterValueOut), [`AtenScatterValueReduceOut`](scatter_aten_kernels.cc.md#AtenScatterValueReduceOut), [`AtenScatterSrcOut`](scatter_aten_kernels.cc.md#AtenScatterSrcOut), [`BuildNllLossBackwardGradInputShlo`](../nll_loss/nll_loss.cc.md#BuildNllLossBackwardGradInputShlo), [`ParseScatterOp`](scatter_aten_kernels.cc.md#ParseScatterOp), [`BuildCrossEntropyClassIndicesBackwardShlo`](../cross_entropy_loss/cross_entropy_loss_aten_kernels.cc.md#BuildCrossEntropyClassIndicesBackwardShlo), [`IndexReduce`](../index_reduce/index_reduce_aten_kernels.cc.md#IndexReduce), [`GetReduceOp`](../index_reduce/index_reduce_aten_kernels.cc.md#GetReduceOp), [`GetIdentityValue`](scatter.cc.md#GetIdentityValue), [`EncodeParamCacheKey`](scatter.h.md#EncodeParamCacheKey), [`EncodeParamCacheKey`](scatter.h.md#EncodeParamCacheKey)

### <a id="ScatterVersion"></a>`ScatterVersion`
- def: [`csrc/ops/scatter/scatter.h:36`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L36)
- doc: ScatterVersion distinguishes between legacy scatter aten ops and newer
- signature: `enum class ScatterVersion`
- members:
  - <a id="ScatterVersion.kV1"></a>`kV1` — [`L37`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L37) — Supports 'add' and 'multiply'
  - <a id="ScatterVersion.kV2"></a>`kV2` — [`L38`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L38) — Supports 'sum', 'prod', 'mean', 'amax', 'amin'
- used by: [`AtenScatterReduceTwoOut`](scatter_aten_kernels.cc.md#AtenScatterReduceTwoOut), [`ParseScatterOp`](scatter_aten_kernels.cc.md#ParseScatterOp)

## Functions
- `EncodeParamCacheKey(const ScatterIncludeSelf include_self)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L63)
- <a id="EncodeParamCacheKey"></a>`EncodeParamCacheKey(const ScatterOp scatter_op)` — [`L41`](../../../../../../../raw/code/torch_tpu/csrc/ops/scatter/scatter.h#L41)

