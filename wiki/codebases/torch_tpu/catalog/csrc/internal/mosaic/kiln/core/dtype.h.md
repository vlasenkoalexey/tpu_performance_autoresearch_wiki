---
title: 'Module: csrc/internal/mosaic/kiln/core/dtype.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/dtype.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/
symbols:
  DType: DType#
  DType.GetIntOrFloatBitWidth: DType#GetIntOrFloatBitWidth(ddd8539a2fcdd4ce).
  DType.Kind: DType#Kind#
  Float32Type: Float32Type(d11b6c957c4cfb56).
  DType.ToString: DType#ToString(28b48b7ac385737).
  DType.IsFloat: DType#IsFloat(50ce9a9e25b4a850).
  DType.IsUnsigned: DType#IsUnsigned(50ce9a9e25b4a850).
  Int32Type: Int32Type(d11b6c957c4cfb56).
  DType.IsSigned: DType#IsSigned(50ce9a9e25b4a850).
  DType.IsIntOrFloat: DType#IsIntOrFloat(50ce9a9e25b4a850).
  BoolType: BoolType(d11b6c957c4cfb56).
  DType.IsInt: DType#IsInt(50ce9a9e25b4a850).
  UInt32Type: UInt32Type(d11b6c957c4cfb56).
  DType.IsUnsignedInteger: DType#IsUnsignedInteger(8de63fdb265b07c1).
  DType.IsBool: DType#IsBool(50ce9a9e25b4a850).
  DType.kind_: DType#kind_.
  BFloat16Type: BFloat16Type(d11b6c957c4cfb56).
  DType.IsSignedInteger: DType#IsSignedInteger(8de63fdb265b07c1).
  UInt8Type: UInt8Type(d11b6c957c4cfb56).
  DType.DType: DType#DType(2a3617cdc38c91d5).
  Shape: Shape#
  UInt16Type: UInt16Type(d11b6c957c4cfb56).
  UInt64Type: UInt64Type(d11b6c957c4cfb56).
  Float16Type: Float16Type(d11b6c957c4cfb56).
  Int8Type: Int8Type(d11b6c957c4cfb56).
  operator: '`operator<<`(23445ef3b0edcbf6).'
  Int64Type: Int64Type(d11b6c957c4cfb56).
  Int16Type: Int16Type(d11b6c957c4cfb56).
  DType.IsInteger: DType#IsInteger(8de63fdb265b07c1).
  AbslStringify: AbslStringify(98fdd7a5a57f9e67).
  DType.operator: DType#`operator==`(f62bd5ddc16b922b).
  DType.Kind.kBF16: DType#Kind#kBF16.
  DType.Kind.kF32: DType#Kind#kF32.
  DType.Kind.kF16: DType#Kind#kF16.
  DType.kind: DType#kind(a70683fc8eedd0fb).
  DType.Kind.kI8: DType#Kind#kI8.
  DType.Kind.kI16: DType#Kind#kI16.
  DType.Kind.kU16: DType#Kind#kU16.
  DType.Kind.kBool: DType#Kind#kBool.
  DType.Kind.kI64: DType#Kind#kI64.
  DType.Kind.kU64: DType#Kind#kU64.
  DType.Kind.kI32: DType#Kind#kI32.
  DType.Kind.kU8: DType#Kind#kU8.
  DType.Kind.kU32: DType#Kind#kU32.
---
# Module: [`csrc/internal/mosaic/kiln/core/dtype.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h)

## Classes
### <a id="DType"></a>`DType`
- def: [`csrc/internal/mosaic/kiln/core/dtype.h:31`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L31) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- doc: An element data type.
- signature: `class DType`
- members:
  - <a id="DType.DType"></a>`DType(Kind kind)` — [`L48`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L48)
  - <a id="DType.GetIntOrFloatBitWidth"></a>`GetIntOrFloatBitWidth()` — [`L76`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L76) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
  - <a id="DType.IsBool"></a>`IsBool()` — [`L52`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L52)
  - <a id="DType.IsFloat"></a>`IsFloat()` — [`L54`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L54)
  - <a id="DType.IsInt"></a>`IsInt()` — [`L65`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L65)
  - <a id="DType.IsIntOrFloat"></a>`IsIntOrFloat()` — [`L66`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L66)
  - <a id="DType.IsInteger"></a>`IsInteger(unsigned width)` — [`L67`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L67)
  - <a id="DType.IsSigned"></a>`IsSigned()` — [`L57`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L57)
  - <a id="DType.IsSignedInteger"></a>`IsSignedInteger(unsigned width)` — [`L70`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L70)
  - <a id="DType.IsUnsigned"></a>`IsUnsigned()` — [`L61`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L61)
  - <a id="DType.IsUnsignedInteger"></a>`IsUnsignedInteger(unsigned width)` — [`L73`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L73)
  - <a id="DType.ToString"></a>`ToString()` — [`L98`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L98)
  - <a id="DType.kind"></a>`kind()` — [`L50`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L50)
  - `operator!=(DType other)` — [`L128`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L128)
  - <a id="DType.operator"></a>`operator==(DType other)` — [`L127`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L127)
  - <a id="DType.kind_"></a>`kind_` — [`L136`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L136)
- uses (calls/refs, reference-scoped): [`Kind`](dtype.h.md#DType.Kind), [`kBF16`](dtype.h.md#DType.Kind.kBF16), [`kF16`](dtype.h.md#DType.Kind.kF16), [`kF32`](dtype.h.md#DType.Kind.kF32), [`kBool`](dtype.h.md#DType.Kind.kBool), [`kI16`](dtype.h.md#DType.Kind.kI16), [`kI32`](dtype.h.md#DType.Kind.kI32), [`kI64`](dtype.h.md#DType.Kind.kI64), [`kI8`](dtype.h.md#DType.Kind.kI8), [`kU16`](dtype.h.md#DType.Kind.kU16), [`kU32`](dtype.h.md#DType.Kind.kU32), [`kU64`](dtype.h.md#DType.Kind.kU64), [`kU8`](dtype.h.md#DType.Kind.kU8)
- used by: [`Scalar`](scalar.h.md#Scalar), [`ElementwiseOps`](elementwise.h.md#ElementwiseOps), [`TestBody`](../kiln_test.cc.md#KilnTest_TileScalarOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_SimplifiedOverloadsAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarFloatOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_LiteralOverloads_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RotateGatherExtractBitcastAndMaskedStore_Test.TestBody), [`Cond`](cond.h.md#Cond), [`TestBody`](../kiln_test.cc.md#KilnTest_TypeHelpersInsideKernel_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BitwiseOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ForLoopWithInductionVarAndBounds_Test.TestBody), [`wrap`](context.h.md#wrap), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarPrefetchAndLoop_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_DTypeInTileAndScalarOps_Test.TestBody), [`Dot`](tile.cc.md#Dot), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedAndSignedCasts_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_DTypeProperties_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RefSliceRankCollapsing_Test.TestBody), [`Float32Type`](dtype.h.md#Float32Type), [`ToMlirType`](context.cc.md#ToMlirType), [`Store`](ref.cc.md#Ref.Store), [`operator()`](ref.h.md#Ref.operator), [`AsType`](elementwise.h.md#WithElementwiseOps.AsType), [`ToMlirType`](context.cc.md#ToMlirType), [`Int32Type`](dtype.h.md#Int32Type), [`Gather`](tile.h.md#Tile.Gather), [`Gather`](tile.cc.md#Tile.Gather), [`Iota`](tile.cc.md#Iota), [`EmitCast`](context.cc.md#EmitCast), [`LiteralToAttr`](context.cc.md#LiteralToAttr), [`Full`](tile.cc.md#Full), [`MaxReduce`](tile.cc.md#MaxReduce), [`NInf`](tile.cc.md#NInf), [`BlockType`](kernel.cc.md#BlockType), [`MakeScalarConstant`](scalar.cc.md#MakeScalarConstant), [`Zeros`](tile.cc.md#Zeros), [`SumReduce`](tile.cc.md#SumReduce), [`ValueBase`](value_base.h.md#ValueBase)  (+34 more)

### <a id="DType.Kind"></a>`DType.Kind`
- def: [`csrc/internal/mosaic/kiln/core/dtype.h:33`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L33) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- signature: `enum class Kind : uint8_t`
- members:
  - <a id="DType.Kind.kBF16"></a>`kBF16` — [`L44`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L44)
  - <a id="DType.Kind.kBool"></a>`kBool` — [`L34`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L34)
  - <a id="DType.Kind.kF16"></a>`kF16` — [`L43`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L43)
  - <a id="DType.Kind.kF32"></a>`kF32` — [`L45`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L45)
  - <a id="DType.Kind.kI16"></a>`kI16` — [`L36`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L36)
  - <a id="DType.Kind.kI32"></a>`kI32` — [`L37`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L37)
  - <a id="DType.Kind.kI64"></a>`kI64` — [`L38`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L38)
  - <a id="DType.Kind.kI8"></a>`kI8` — [`L35`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L35)
  - <a id="DType.Kind.kU16"></a>`kU16` — [`L40`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L40)
  - <a id="DType.Kind.kU32"></a>`kU32` — [`L41`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L41)
  - <a id="DType.Kind.kU64"></a>`kU64` — [`L42`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L42)
  - <a id="DType.Kind.kU8"></a>`kU8` — [`L39`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L39)
- used by: [`GetIntOrFloatBitWidth`](dtype.h.md#DType.GetIntOrFloatBitWidth), [`Float32Type`](dtype.h.md#Float32Type), [`ToMlirType`](context.cc.md#ToMlirType), [`ToString`](dtype.h.md#DType.ToString), [`IsFloat`](dtype.h.md#DType.IsFloat), [`Int32Type`](dtype.h.md#Int32Type), [`IsUnsigned`](dtype.h.md#DType.IsUnsigned), [`IsSigned`](dtype.h.md#DType.IsSigned), [`BoolType`](dtype.h.md#BoolType), [`UInt32Type`](dtype.h.md#UInt32Type), [`IsBool`](dtype.h.md#DType.IsBool), [`BFloat16Type`](dtype.h.md#BFloat16Type), [`DType`](dtype.h.md#DType.DType), [`UInt8Type`](dtype.h.md#UInt8Type), [`UInt16Type`](dtype.h.md#UInt16Type), [`UInt64Type`](dtype.h.md#UInt64Type), [`Float16Type`](dtype.h.md#Float16Type), [`Int8Type`](dtype.h.md#Int8Type), [`Int16Type`](dtype.h.md#Int16Type), [`Int64Type`](dtype.h.md#Int64Type), [`AbslStringify`](dtype.h.md#AbslStringify)

### <a id="Shape"></a>`Shape`
- def: [`csrc/internal/mosaic/kiln/core/dtype.h:28`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L28)
- signature: `using Shape = llvm::SmallVector<int64_t, 4>`
- used by: [`Lanes`](tile.cc.md#Tile.Lanes), [`Reduce`](tile.cc.md#Reduce), [`AlignShapes`](elementwise_impl.cc.md#AlignShapes), [`BroadcastShapes`](elementwise_impl.cc.md#BroadcastShapes), [`ShapeOf`](elementwise_impl.cc.md#ShapeOf), [`ScalarPrefetchSpec`](specs.h.md#ScalarPrefetchSpec), [`ScratchSpec`](specs.h.md#ScratchSpec), [`name`](specs.h.md#GridSpec.name), [`BasicBlockSpec`](specs.h.md#BasicBlockSpec)

## Functions
- <a id="AbslStringify"></a>`AbslStringify(Sink& sink, const DType& dtype)` — [`L131`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L131)
- <a id="BFloat16Type"></a>`BFloat16Type()` — [`L154`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L154)
- <a id="BoolType"></a>`BoolType()` — [`L144`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L144) — Types
- <a id="Float16Type"></a>`Float16Type()` — [`L153`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L153)
- <a id="Float32Type"></a>`Float32Type()` — [`L155`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L155) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Int16Type"></a>`Int16Type()` — [`L146`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L146)
- <a id="Int32Type"></a>`Int32Type()` — [`L147`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L147)
- <a id="Int64Type"></a>`Int64Type()` — [`L148`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L148)
- <a id="Int8Type"></a>`Int8Type()` — [`L145`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L145)
- <a id="UInt16Type"></a>`UInt16Type()` — [`L150`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L150)
- <a id="UInt32Type"></a>`UInt32Type()` — [`L151`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L151)
- <a id="UInt64Type"></a>`UInt64Type()` — [`L152`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L152)
- <a id="UInt8Type"></a>`UInt8Type()` — [`L149`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L149)
- <a id="operator"></a>`operator<<(std::ostream& os, DType dtype)` — [`L139`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/dtype.h#L139)

