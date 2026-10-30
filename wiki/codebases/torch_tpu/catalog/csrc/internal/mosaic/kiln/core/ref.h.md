---
title: 'Module: csrc/internal/mosaic/kiln/core/ref.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/ref.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/
symbols:
  Ref: Ref#
  Ref.operator: Ref#`operator()`(4e1e9be508f1077c).
  DimDesc: internal/DimDesc#
  Slice: Slice(fbc3677d4788dd09).
  Ref.Ref: Ref#Ref(5036bd43bbbb2151).
  DimDesc.From: internal/DimDesc#From(29469f8875c83977).
  all: all.
  Store: Store(8caaa4e4c8d7a06b).
  DimDesc.offset: internal/DimDesc#offset.
  SliceDim: SliceDim#
  All: All#
  DimDesc.collapsed: internal/DimDesc#collapsed.
  DimDesc.is_all: internal/DimDesc#is_all.
  SliceDim.size: SliceDim#size.
  DimDesc.size: internal/DimDesc#size.
  SliceDim.offset: SliceDim#offset.
---
# Module: [`csrc/internal/mosaic/kiln/core/ref.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h)

## Classes
### <a id="All"></a>`All`
- def: [`csrc/internal/mosaic/kiln/core/ref.h:35`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L35)
- doc: Sentinel representing full slice along a dimension (`:` in JAX / Pallas).
- signature: `struct All`
- used by: [`From`](ref.h.md#DimDesc.From)

### <a id="DimDesc"></a>`DimDesc`
- def: [`csrc/internal/mosaic/kiln/core/ref.h:51`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L51)
- signature: `struct DimDesc`
- members:
  - <a id="DimDesc.From"></a>`From(const SliceDim& s)` — [`L60`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L60)
  - `From(IndexArg s)` — [`L66`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L66)
  - `From(All)` — [`L57`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L57)
  - <a id="DimDesc.collapsed"></a>`collapsed` — [`L55`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L55) — true for scalar index (collapses dimension)
  - <a id="DimDesc.is_all"></a>`is_all` — [`L54`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L54) — true for full dimension (All)
  - <a id="DimDesc.offset"></a>`offset` — [`L52`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L52)
  - <a id="DimDesc.size"></a>`size` — [`L53`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L53)
- uses (calls/refs, reference-scoped): [`Ref`](ref.h.md#Ref), [`SliceRefImpl`](ref.cc.md#SliceRefImpl), [`IndexArg`](index_arg.h.md#IndexArg), [`IndexArg`](index_arg.h.md#IndexArg.IndexArg), [`SliceDim`](ref.h.md#SliceDim), [`All`](ref.h.md#All), [`size`](ref.h.md#SliceDim.size), [`offset`](ref.h.md#SliceDim.offset)
- used by: [`SliceRefImpl`](ref.cc.md#SliceRefImpl), [`operator()`](ref.h.md#Ref.operator)

### <a id="Ref"></a>`Ref`  ·  implements/extends ValueBase
- def: [`csrc/internal/mosaic/kiln/core/ref.h:79`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L79) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- doc: A memref kernel argument (VMEM block, SMEM scalar-prefetch buffer or
- signature: `class Ref : public ValueBase`
- members:
  - `Ref(const Ref&)` — [`L81`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L81)
  - <a id="Ref.Ref"></a>`Ref(const Ref&)` — [`L81`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L81)
  - <a id="Ref.operator"></a>`operator()()` — [`L102`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L102) — Slices a view of the ref: — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
  - `operator=(const Ref&)` — [`L82`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L82)
- uses (calls/refs, reference-scoped): [`Tile`](tile.h.md#Tile), [`Scalar`](scalar.h.md#Scalar), [`DType`](dtype.h.md#DType), [`operator=`](ref.cc.md#Ref.operator), [`SliceRefImpl`](ref.cc.md#SliceRefImpl), [`Store`](ref.cc.md#Ref.Store), [`operator Tile`](ref.cc.md#Ref.operator-Tile), [`rank`](ref.cc.md#Ref.rank), [`operator=`](ref.cc.md#Ref.operator), [`operator Scalar`](ref.cc.md#Ref.operator-Scalar), [`ValueAccess`](context.h.md#ValueAccess), [`ValueBase`](value_base.h.md#ValueBase), [`shape`](ref.cc.md#Ref.shape), [`Ref`](ref.cc.md#Ref.Ref), [`DimDesc`](ref.h.md#DimDesc), [`From`](ref.h.md#DimDesc.From), [`From`](ref.h.md#DimDesc.From), [`From`](ref.h.md#DimDesc.From)
- used by: [`TestBody`](../kiln_test.cc.md#KilnTest_TileScalarOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_SimplifiedOverloadsAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarFloatOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_LiteralOverloads_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RotateGatherExtractBitcastAndMaskedStore_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_TypeHelpersInsideKernel_Test.TestBody), [`operator=`](ref.cc.md#Ref.operator), [`TestBody`](../kiln_test.cc.md#KilnTest_BitwiseOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ForLoopWithInductionVarAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarMismatchedTypesFail_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarPrefetchAndLoop_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_DTypeInTileAndScalarOps_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedAndSignedCasts_Test.TestBody), [`SliceRefImpl`](ref.cc.md#SliceRefImpl), [`TestBody`](../kiln_test.cc.md#KilnTest_RefSliceRankCollapsing_Test.TestBody), [`Store`](ref.cc.md#Ref.Store), [`operator Tile`](ref.cc.md#Ref.operator-Tile), [`operator=`](ref.cc.md#Ref.operator), [`operator Scalar`](ref.cc.md#Ref.operator-Scalar), [`ValueBase`](value_base.h.md#ValueBase), [`shape`](ref.cc.md#Ref.shape), [`Resolver`](kernel.h.md#RegisterSpec.Resolver), [`Ref`](ref.cc.md#Ref.Ref), [`ScalarPrefetch`](kernel.cc.md#ScalarPrefetch), [`MemRefTypeOf`](ref.cc.md#MemRefTypeOf), [`Scratch`](kernel.cc.md#Scratch), [`In`](kernel.cc.md#In), [`Out`](kernel.cc.md#Out), [`Slice`](ref.h.md#Slice), [`GridRank`](kernel.cc.md#GridRank), [`From`](ref.h.md#DimDesc.From), [`Store`](ref.h.md#Store), [`HasMemorySpace`](ref.cc.md#HasMemorySpace), [`IsSmemRef`](ref.cc.md#IsSmemRef), [`IsVmemRef`](ref.cc.md#IsVmemRef), [`inputs`](kernel.cc.md#KernelScope.inputs), [`outputs`](kernel.cc.md#KernelScope.outputs), [`program_ids`](kernel.cc.md#KernelScope.program_ids)  (+1 more)

### <a id="SliceDim"></a>`SliceDim`
- def: [`csrc/internal/mosaic/kiln/core/ref.h:38`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L38)
- signature: `struct SliceDim`
- members:
  - <a id="SliceDim.offset"></a>`offset` — [`L39`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L39)
  - <a id="SliceDim.size"></a>`size` — [`L40`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L40)
- uses (calls/refs, reference-scoped): [`IndexArg`](index_arg.h.md#IndexArg)
- used by: [`Slice`](ref.h.md#Slice), [`From`](ref.h.md#DimDesc.From)

## Functions
- <a id="Slice"></a>`Slice(IndexArg offset, int64_t size)` — [`L43`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L43)
- <a id="Store"></a>`Store(Ref dst, Tile value, std::optional<Tile> mask = std::nullopt)` — [`L115`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L115) — Stores `value` into `dst` (a VMEM ref), optionally masked by an i1 `mask`

## Module values
- <a id="all"></a>`all` — [`L36`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.h#L36)

