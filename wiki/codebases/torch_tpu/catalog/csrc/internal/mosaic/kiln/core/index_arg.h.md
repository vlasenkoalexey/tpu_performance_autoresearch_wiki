---
title: 'Module: csrc/internal/mosaic/kiln/core/index_arg.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/index_arg.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/IndexArg#
symbols:
  IndexArg.IndexArg: IndexArg(8bb134018e17eaec).
  IndexArg: ''
  IndexArg.ToScalar: ToScalar(a6b4eefc4c3c7356).
  IndexArg.AsInt: AsInt(57a65ae535d7db84).
  IndexArg.val_: val_.
  IndexArg.IsInt: IsInt(50ce9a9e25b4a850).
---
# Module: [`csrc/internal/mosaic/kiln/core/index_arg.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_arg.h)

## Classes
### <a id="IndexArg"></a>`IndexArg`
- def: [`csrc/internal/mosaic/kiln/core/index_arg.h:30`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_arg.h#L30)
- doc: An argument representing an index or dimension offset/bound.
- signature: `class IndexArg`
- members:
  - <a id="IndexArg.AsInt"></a>`AsInt()` — [`L43`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_arg.h#L43)
  - `IndexArg(T v)` — [`L34`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_arg.h#L34) — implicit
  - <a id="IndexArg.IndexArg"></a>`IndexArg(Scalar s)` — [`L36`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_arg.h#L36) — implicit
  - <a id="IndexArg.IsInt"></a>`IsInt()` — [`L42`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_arg.h#L42)
  - <a id="IndexArg.ToScalar"></a>`ToScalar()` — [`L44`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_arg.h#L44)
  - <a id="IndexArg.val_"></a>`val_` — [`L52`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/index_arg.h#L52)
- uses (calls/refs, reference-scoped): [`Scalar`](scalar.h.md#Scalar), [`Literal`](literal.h.md#Literal.Literal), [`dtype`](value_base.h.md#ValueBase.dtype), [`I32`](scalar.cc.md#I32), [`IsInt`](dtype.h.md#DType.IsInt)
- used by: [`TestBody`](../kiln_test.cc.md#KilnTest_SimplifiedOverloadsAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RotateGatherExtractBitcastAndMaskedStore_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ForLoopWithInductionVarAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarMismatchedTypesFail_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarPrefetchAndLoop_Test.TestBody), [`EmitIndexMapFunction`](kernel.cc.md#EmitIndexMapFunction), [`SliceRefImpl`](ref.cc.md#SliceRefImpl), [`For`](control_flow.cc.md#For), [`MakeConstant`](tile.h.md#Tile.MakeConstant), [`Rotate`](tile.cc.md#Tile.Rotate), [`DimDesc`](ref.h.md#DimDesc), [`ToIndex`](control_flow.cc.md#ToIndex), [`IndexIndices`](index_map.h.md#IndexIndices), [`For`](control_flow.h.md#For), [`Slice`](ref.h.md#Slice), [`From`](ref.h.md#DimDesc.From), [`Rotate`](tile.h.md#Rotate), [`offset`](ref.h.md#DimDesc.offset), [`SliceDim`](ref.h.md#SliceDim)

