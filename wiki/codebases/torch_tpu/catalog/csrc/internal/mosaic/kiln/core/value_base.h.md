---
title: 'Module: csrc/internal/mosaic/kiln/core/value_base.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/value_base.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/ValueBase#
symbols:
  ValueBase.dtype: dtype(16ed140383721f86).
  ValueBase: ''
  ValueBase.ValueBase: ValueBase(cac036679d256d0e).
  ValueBase.impl: impl(3a8ef3fdc6e817ef).
  ValueBase.impl_: impl_.
  ValueBase.dtype_: dtype_.
---
# Module: [`csrc/internal/mosaic/kiln/core/value_base.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/value_base.h)

## Classes
### <a id="ValueBase"></a>`ValueBase`
- def: [`csrc/internal/mosaic/kiln/core/value_base.h:30`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/value_base.h#L30)
- doc: Common base for KILN SSA handles (`Scalar`, `Cond`, `Tile`, `Ref`). Holds
- signature: `class ValueBase`
- members:
  - <a id="ValueBase.ValueBase"></a>`ValueBase(const void* impl, DType dtype)` — [`L35`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/value_base.h#L35)
  - <a id="ValueBase.dtype"></a>`dtype()` — [`L32`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/value_base.h#L32) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
  - <a id="ValueBase.impl"></a>`impl()` — [`L36`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/value_base.h#L36)
  - <a id="ValueBase.dtype_"></a>`dtype_` — [`L41`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/value_base.h#L41)
  - <a id="ValueBase.impl_"></a>`impl_` — [`L40`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/value_base.h#L40)
- uses (calls/refs, reference-scoped): [`Tile`](tile.h.md#Tile), [`Ref`](ref.h.md#Ref), [`Scalar`](scalar.h.md#Scalar), [`DType`](dtype.h.md#DType), [`Cond`](cond.h.md#Cond), [`ValueAccess`](context.h.md#ValueAccess)
- used by: [`Tile`](tile.h.md#Tile), [`Ref`](ref.h.md#Ref), [`Scalar`](scalar.h.md#Scalar), [`TestBody`](../kiln_test.cc.md#KilnTest_TileScalarOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_SimplifiedOverloadsAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarFloatOperations_Test.TestBody), [`unwrap`](context.h.md#unwrap), [`TestBody`](../kiln_test.cc.md#KilnTest_LiteralOverloads_Test.TestBody), [`Cond`](cond.h.md#Cond), [`TestBody`](../kiln_test.cc.md#KilnTest_ForLoopWithInductionVarAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_DTypeInTileAndScalarOps_Test.TestBody), [`Dot`](tile.cc.md#Dot), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedAndSignedCasts_Test.TestBody), [`SliceRefImpl`](ref.cc.md#SliceRefImpl), [`Store`](ref.cc.md#Ref.Store), [`Lanes`](tile.cc.md#Tile.Lanes), [`Reshape`](tile.cc.md#Tile.Reshape), [`Reduce`](tile.cc.md#Reduce), [`Gather`](tile.cc.md#Tile.Gather), [`operator Tile`](ref.cc.md#Ref.operator-Tile), [`Rotate`](tile.cc.md#Tile.Rotate), [`operator=`](ref.cc.md#Ref.operator), [`Slice`](tile.cc.md#Tile.Slice), [`Splat`](tile.cc.md#Splat), [`MaxReduce`](tile.cc.md#MaxReduce), [`operator Scalar`](ref.cc.md#Ref.operator-Scalar), [`BroadcastTo`](tile.cc.md#Tile.BroadcastTo), [`Extract`](tile.cc.md#Tile.Extract), [`SumReduce`](tile.cc.md#SumReduce), [`IndexArg`](index_arg.h.md#IndexArg.IndexArg), [`operator Cond`](scalar.cc.md#Scalar.operator-Cond), [`Scalar`](scalar.cc.md#Scalar.Scalar), [`Cond`](cond.cc.md#Cond.Cond), [`Ref`](ref.cc.md#Ref.Ref), [`Reciprocal`](tile.cc.md#Reciprocal), [`Tile`](tile.cc.md#Tile.Tile), [`Transpose`](tile.cc.md#Transpose), [`Full`](tile.cc.md#Tile.Full), [`MakeConstant`](scalar.cc.md#Scalar.MakeConstant)  (+1 more)

