---
title: 'Module: csrc/internal/mosaic/kiln/core/tile.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/tile.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/
symbols:
  Tile: Tile#
  Tile.Gather: Tile#Gather(443f3a781cdba6fe).
  Tile.MakeConstant: Tile#MakeConstant(b41e689cc09aa588).
  Extract: Extract(c880b6044fad032c).
  DotOptions.precision: DotOptions#precision.
  Rotate: Rotate(e4f288166e3a5ef0).
  Gather: Gather(915f1b12dde45292).
  ContractPrecision: ContractPrecision#
  DotOptions.transpose_rhs: DotOptions#transpose_rhs.
  DotOptions.transpose_lhs: DotOptions#transpose_lhs.
  DotOptions: DotOptions#
  ContractPrecision.kBF16: ContractPrecision#kBF16.
  ContractPrecision.kFP32: ContractPrecision#kFP32.
  ContractPrecision.kBF16x3: ContractPrecision#kBF16x3.
---
# Module: [`csrc/internal/mosaic/kiln/core/tile.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h)

## Classes
### <a id="ContractPrecision"></a>`ContractPrecision`
- def: [`csrc/internal/mosaic/kiln/core/tile.h:117`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L117)
- signature: `enum class ContractPrecision`
- members:
  - <a id="ContractPrecision.kBF16"></a>`kBF16` — [`L118`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L118)
  - <a id="ContractPrecision.kBF16x3"></a>`kBF16x3` — [`L120`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L120)
  - <a id="ContractPrecision.kFP32"></a>`kFP32` — [`L119`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L119)
- used by: [`Dot`](tile.cc.md#Dot), [`transpose_rhs`](tile.h.md#DotOptions.transpose_rhs)

### <a id="DotOptions"></a>`DotOptions`
- def: [`csrc/internal/mosaic/kiln/core/tile.h:123`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L123)
- signature: `struct DotOptions`
- members:
  - <a id="DotOptions.precision"></a>`precision` — [`L126`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L126)
  - <a id="DotOptions.transpose_lhs"></a>`transpose_lhs` — [`L124`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L124)
  - <a id="DotOptions.transpose_rhs"></a>`transpose_rhs` — [`L125`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L125)
- uses (calls/refs, reference-scoped): [`Tile`](tile.h.md#Tile), [`Dot`](tile.cc.md#Dot), [`ContractPrecision`](tile.h.md#ContractPrecision)
- used by: [`Dot`](tile.cc.md#Dot)

### <a id="Tile"></a>`Tile`  ·  implements/extends ValueBase, WithElementwiseOps, WithLiteralOps
- def: [`csrc/internal/mosaic/kiln/core/tile.h:41`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L41) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- doc: A vector-typed value: a tile living in vregs.
- signature: `class Tile : public ValueBase, public WithElementwiseOps<Tile, Tile>, public WithLiteralOps<Tile, Tile>`
- members:
  - <a id="Tile.Gather"></a>`Gather(Tile indices, int32_t axis)` — [`L73`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L73) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
  - <a id="Tile.MakeConstant"></a>`MakeConstant(Literal value)` — [`L48`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L48) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- uses (calls/refs, reference-scoped): [`Scalar`](scalar.h.md#Scalar), [`DType`](dtype.h.md#DType), [`rank`](tile.cc.md#Tile.rank), [`shape`](tile.cc.md#Tile.shape), [`Literal`](literal.h.md#Literal), [`Tile`](tile.cc.md#Tile.Tile), [`Lanes`](tile.cc.md#Tile.Lanes), [`Reshape`](tile.cc.md#Tile.Reshape), [`Gather`](tile.cc.md#Tile.Gather), [`Iota`](tile.cc.md#Iota), [`Rotate`](tile.cc.md#Tile.Rotate), [`Full`](tile.cc.md#Full), [`Slice`](tile.cc.md#Tile.Slice), [`Splat`](tile.cc.md#Splat), [`NInf`](tile.cc.md#NInf), [`BroadcastTo`](tile.cc.md#Tile.BroadcastTo), [`Extract`](tile.cc.md#Tile.Extract), [`ValueAccess`](context.h.md#ValueAccess), [`Zeros`](tile.cc.md#Zeros), [`ValueBase`](value_base.h.md#ValueBase), [`Tile`](tile.cc.md#Tile.Tile), [`Full`](tile.cc.md#Tile.Full), [`IndexArg`](index_arg.h.md#IndexArg), [`ToShape`](tile.cc.md#Tile.ToShape), [`num_elements`](tile.cc.md#Tile.num_elements), [`Squeeze`](tile.cc.md#Tile.Squeeze), [`WithElementwiseOps`](elementwise.h.md#WithElementwiseOps), [`WithLiteralOps`](literal.h.md#WithLiteralOps)
- used by: [`ElementwiseOps`](elementwise.h.md#ElementwiseOps), [`TestBody`](../kiln_test.cc.md#KilnTest_TileScalarOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_SimplifiedOverloadsAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedOperations_Test.TestBody), [`rank`](tile.cc.md#Tile.rank), [`TestBody`](../kiln_test.cc.md#KilnTest_LiteralOverloads_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RotateGatherExtractBitcastAndMaskedStore_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_TypeHelpersInsideKernel_Test.TestBody), [`operator=`](ref.cc.md#Ref.operator), [`TestBody`](../kiln_test.cc.md#KilnTest_BitwiseOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ForLoopWithInductionVarAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarMismatchedTypesFail_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarPrefetchAndLoop_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_DTypeInTileAndScalarOps_Test.TestBody), [`shape`](tile.cc.md#Tile.shape), [`Dot`](tile.cc.md#Dot), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedAndSignedCasts_Test.TestBody), [`Tile`](tile.cc.md#Tile.Tile), [`TestBody`](../kiln_test.cc.md#KilnTest_RefSliceRankCollapsing_Test.TestBody), [`Store`](ref.cc.md#Ref.Store), [`Lanes`](tile.cc.md#Tile.Lanes), [`Reshape`](tile.cc.md#Tile.Reshape), [`Reduce`](tile.cc.md#Reduce), [`Gather`](tile.cc.md#Tile.Gather), [`operator Tile`](ref.cc.md#Ref.operator-Tile), [`Iota`](tile.cc.md#Iota), [`Rotate`](tile.cc.md#Tile.Rotate), [`Full`](tile.cc.md#Full), [`Slice`](tile.cc.md#Tile.Slice), [`Splat`](tile.cc.md#Splat), [`MaxReduce`](tile.cc.md#MaxReduce), [`NInf`](tile.cc.md#NInf), [`BroadcastTo`](tile.cc.md#Tile.BroadcastTo), [`Extract`](tile.cc.md#Tile.Extract), [`Zeros`](tile.cc.md#Zeros), [`SumReduce`](tile.cc.md#SumReduce), [`ValueBase`](value_base.h.md#ValueBase), [`MinValue`](tile.cc.md#MinValue), [`operator=`](ref.h.md#Ref.operator)  (+16 more)

## Functions
- <a id="Extract"></a>`Extract(Tile t, llvm::ArrayRef<int64_t> indices)` — [`L103`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L103)
- <a id="Gather"></a>`Gather(Tile source, Tile indices, int32_t axis)` — [`L100`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L100)
- `Gather(Tile source, Tile indices, llvm::ArrayRef<int32_t> dimensions)` — [`L96`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L96)
- <a id="Rotate"></a>`Rotate(Tile t, IndexArg amount, int32_t axis)` — [`L93`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.h#L93)

