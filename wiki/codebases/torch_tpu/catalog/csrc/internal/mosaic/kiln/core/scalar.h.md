---
title: 'Module: csrc/internal/mosaic/kiln/core/scalar.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/scalar.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/Scalar#
symbols:
  Scalar: ''
---
# Module: [`csrc/internal/mosaic/kiln/core/scalar.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/scalar.h)

## Classes
### <a id="Scalar"></a>`Scalar`  ·  implements/extends ValueBase, WithElementwiseOps, WithLiteralOps
- def: [`csrc/internal/mosaic/kiln/core/scalar.h:35`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/scalar.h#L35) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- doc: A scalar SSA value (boolean, integer, or floating-point). Grid indices,
- signature: `class Scalar : public ValueBase, public WithElementwiseOps<Scalar, Cond>, public WithLiteralOps<Scalar, Cond>`
- uses (calls/refs, reference-scoped): [`DType`](dtype.h.md#DType), [`Cond`](cond.h.md#Cond), [`Literal`](literal.h.md#Literal), [`I32`](scalar.cc.md#I32), [`U32`](scalar.cc.md#U32), [`ValueAccess`](context.h.md#ValueAccess), [`ValueBase`](value_base.h.md#ValueBase), [`operator Cond`](scalar.cc.md#Scalar.operator-Cond), [`Scalar`](scalar.cc.md#Scalar.Scalar), [`F32`](scalar.cc.md#F32), [`Scalar`](scalar.cc.md#Scalar.Scalar), [`MakeConstant`](scalar.cc.md#Scalar.MakeConstant), [`WithElementwiseOps`](elementwise.h.md#WithElementwiseOps), [`WithLiteralOps`](literal.h.md#WithLiteralOps)
- used by: [`Tile`](tile.h.md#Tile), [`ElementwiseOps`](elementwise.h.md#ElementwiseOps), [`TestBody`](../kiln_test.cc.md#KilnTest_TileScalarOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_SimplifiedOverloadsAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarFloatOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_LiteralOverloads_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RotateGatherExtractBitcastAndMaskedStore_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BitwiseOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ForLoopWithInductionVarAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarMismatchedTypesFail_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarPrefetchAndLoop_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_DTypeInTileAndScalarOps_Test.TestBody), [`Tile`](tile.cc.md#Tile.Tile), [`Verify`](kernel.cc.md#Kernel.Verify), [`I32`](scalar.cc.md#I32), [`For`](control_flow.cc.md#For), [`Gather`](tile.h.md#Tile.Gather), [`Gather`](tile.cc.md#Tile.Gather), [`U32`](scalar.cc.md#U32), [`Rotate`](tile.cc.md#Tile.Rotate), [`operator=`](ref.cc.md#Ref.operator), [`Splat`](tile.cc.md#Splat), [`operator Scalar`](ref.cc.md#Ref.operator-Scalar), [`Extract`](tile.cc.md#Tile.Extract), [`MakeScalarConstant`](scalar.cc.md#MakeScalarConstant), [`ValueBase`](value_base.h.md#ValueBase), [`IndexArg`](index_arg.h.md#IndexArg.IndexArg), [`operator Cond`](scalar.cc.md#Scalar.operator-Cond), [`Scalar`](scalar.cc.md#Scalar.Scalar), [`operator=`](ref.h.md#Ref.operator), [`Scalar`](scalar.cc.md#Scalar.Scalar), [`ToScalar`](index_arg.h.md#IndexArg.ToScalar), [`For`](control_flow.h.md#For), [`MakeConstant`](scalar.cc.md#Scalar.MakeConstant), [`Gather`](tile.h.md#Gather), [`AsInt`](index_arg.h.md#IndexArg.AsInt), [`WithElementwiseOps`](elementwise.h.md#WithElementwiseOps), [`WithLiteralOps`](literal.h.md#WithLiteralOps)  (+1 more)

