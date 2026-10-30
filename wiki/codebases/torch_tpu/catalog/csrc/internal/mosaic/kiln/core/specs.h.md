---
title: 'Module: csrc/internal/mosaic/kiln/core/specs.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/specs.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/
symbols:
  InSpec: InSpec#
  OutSpec: OutSpec#
  GridSpec: GridSpec#
  KernelSpec.grid: KernelSpec#grid.
  KernelSpec: KernelSpec#
  DimensionSemantics: DimensionSemantics#
  GridSpec.grid: GridSpec#grid.
  KernelSpec.scalar_prefetch: KernelSpec#scalar_prefetch.
  KernelSpec.in_specs: KernelSpec#in_specs.
  KernelSpec.out_specs: KernelSpec#out_specs.
  BlockSpec: BlockSpec#
  MemorySpace: MemorySpace#
  BasicBlockSpec.dtype: BasicBlockSpec#dtype.
  BasicBlockSpec.block_shape: BasicBlockSpec#block_shape.
  KernelSpec.scratch: KernelSpec#scratch.
  BasicBlockSpec.memory_space: BasicBlockSpec#memory_space.
  BasicBlockSpec.index_map: BasicBlockSpec#index_map.
  ScratchSpec: ScratchSpec#
  ScalarPrefetchSpec: ScalarPrefetchSpec#
  DimensionSemantics.kParallel: DimensionSemantics#kParallel.
  GridSpec.dimension_semantics: GridSpec#dimension_semantics.
  ScratchSpec.memory_space: ScratchSpec#memory_space.
  ScratchSpec.dtype: ScratchSpec#dtype.
  GridSpec.name: GridSpec#name.
  BlockRole.kOut: BlockRole#kOut.
  BasicBlockSpec: BasicBlockSpec#
  ScalarPrefetchSpec.shape: ScalarPrefetchSpec#shape.
  ScratchSpec.shape: ScratchSpec#shape.
  DimensionSemantics.kArbitrary: DimensionSemantics#kArbitrary.
  MemorySpace.kVmem: MemorySpace#kVmem.
  MemorySpace.kSmem: MemorySpace#kSmem.
  BlockRole: BlockRole#
  ScalarPrefetchSpec.dtype: ScalarPrefetchSpec#dtype.
  BlockRole.kIn: BlockRole#kIn.
  BlockRole.kNone: BlockRole#kNone.
---
# Module: [`csrc/internal/mosaic/kiln/core/specs.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h)

## Classes
### <a id="BasicBlockSpec"></a>`BasicBlockSpec`
- def: [`csrc/internal/mosaic/kiln/core/specs.h:46`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L46)
- doc: Block specification for a kernel operand, optionally tagged with a role
- signature: `template <BlockRole Role = BlockRole::kNone> struct BasicBlockSpec`
- members:
  - <a id="BasicBlockSpec.block_shape"></a>`block_shape` — [`L47`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L47)
  - <a id="BasicBlockSpec.dtype"></a>`dtype` — [`L48`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L48)
  - <a id="BasicBlockSpec.index_map"></a>`index_map` — [`L49`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L49)
  - <a id="BasicBlockSpec.memory_space"></a>`memory_space` — [`L50`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L50)
- uses (calls/refs, reference-scoped): [`DType`](dtype.h.md#DType), [`IndexMap`](index_map.h.md#IndexMap), [`Shape`](dtype.h.md#Shape), [`MemorySpace`](specs.h.md#MemorySpace), [`kVmem`](specs.h.md#MemorySpace.kVmem)
- used by: [`BuildKernel`](kernel.cc.md#BuildKernel), [`KernelScope`](kernel.cc.md#KernelScope.KernelScope), [`SetGridAttributes`](kernel.cc.md#SetGridAttributes), [`InSpec`](specs.h.md#InSpec), [`OutSpec`](specs.h.md#OutSpec), [`RegisterSpec`](kernel.h.md#RegisterSpec), [`RegisterSpec`](kernel.h.md#RegisterSpec), [`BlockSpec`](specs.h.md#BlockSpec)

### <a id="BlockRole"></a>`BlockRole`
- def: [`csrc/internal/mosaic/kiln/core/specs.h:41`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L41)
- signature: `enum class BlockRole`
- members:
  - <a id="BlockRole.kIn"></a>`kIn` — [`L41`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L41)
  - <a id="BlockRole.kNone"></a>`kNone` — [`L41`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L41)
  - <a id="BlockRole.kOut"></a>`kOut` — [`L41`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L41)
- used by: [`InSpec`](specs.h.md#InSpec), [`OutSpec`](specs.h.md#OutSpec)

### <a id="BlockSpec"></a>`BlockSpec`
- def: [`csrc/internal/mosaic/kiln/core/specs.h:53`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L53)
- signature: `using BlockSpec = BasicBlockSpec<>`
- uses (calls/refs, reference-scoped): [`BasicBlockSpec`](specs.h.md#BasicBlockSpec)
- used by: [`BuildKernel`](kernel.cc.md#BuildKernel), [`SetGridAttributes`](kernel.cc.md#SetGridAttributes), [`scalar_prefetch`](specs.h.md#KernelSpec.scalar_prefetch), [`in_specs`](specs.h.md#KernelSpec.in_specs)

### <a id="DimensionSemantics"></a>`DimensionSemantics`
- def: [`csrc/internal/mosaic/kiln/core/specs.h:32`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L32) — documented in [mosaic-matmul](../../../../../../concepts/mosaic-matmul.md)
- doc: Iteration order guarantees for a grid dimension (Pallas
- signature: `enum class DimensionSemantics`
- members:
  - <a id="DimensionSemantics.kArbitrary"></a>`kArbitrary` — [`L38`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L38) — Iterations along this axis have data dependencies and must execute
  - <a id="DimensionSemantics.kParallel"></a>`kParallel` — [`L35`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L35) — Iterations along this axis are independent and may be reordered or executed
- used by: [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`SetGridAttributes`](kernel.cc.md#SetGridAttributes), [`ToMlirDimensionSemantics`](kernel.cc.md#ToMlirDimensionSemantics), [`grid`](specs.h.md#GridSpec.grid)

### <a id="GridSpec"></a>`GridSpec`
- def: [`csrc/internal/mosaic/kiln/core/specs.h:68`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L68)
- signature: `struct GridSpec`
- members:
  - <a id="GridSpec.dimension_semantics"></a>`dimension_semantics` — [`L72`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L72) — One entry per grid axis. Defaults to `kParallel` for every axis.
  - <a id="GridSpec.grid"></a>`grid` — [`L70`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L70) — documented in [mosaic-matmul](../../../../../../concepts/mosaic-matmul.md)
  - <a id="GridSpec.name"></a>`name` — [`L69`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L69)
- uses (calls/refs, reference-scoped): [`DimensionSemantics`](specs.h.md#DimensionSemantics), [`Shape`](dtype.h.md#Shape)
- used by: [`BuildKernel`](kernel.cc.md#BuildKernel), [`TestBody`](../kiln_test.cc.md#KilnTest_TileScalarOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_SimplifiedOverloadsAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarFloatOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_LiteralOverloads_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RotateGatherExtractBitcastAndMaskedStore_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_TypeHelpersInsideKernel_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BitwiseOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ForLoopWithInductionVarAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarMismatchedTypesFail_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarPrefetchAndLoop_Test.TestBody), [`EmitIndexMapFunction`](kernel.cc.md#EmitIndexMapFunction), [`TestBody`](../kiln_test.cc.md#KilnTest_DTypeInTileAndScalarOps_Test.TestBody), [`KernelScope`](kernel.cc.md#KernelScope.KernelScope), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedAndSignedCasts_Test.TestBody), [`SetGridAttributes`](kernel.cc.md#SetGridAttributes), [`TestBody`](../kiln_test.cc.md#KilnTest_RefSliceRankCollapsing_Test.TestBody), [`CreateKernel`](kernel.h.md#CreateKernel), [`CreateKernelImpl`](kernel.h.md#CreateKernelImpl), [`KernelSpec`](specs.h.md#KernelSpec), [`NumPrograms`](kernel.cc.md#NumPrograms), [`GridRank`](kernel.cc.md#GridRank)

### <a id="InSpec"></a>`InSpec`
- def: [`csrc/internal/mosaic/kiln/core/specs.h:54`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L54)
- signature: `using InSpec = BasicBlockSpec<BlockRole::kIn>`
- uses (calls/refs, reference-scoped): [`BasicBlockSpec`](specs.h.md#BasicBlockSpec), [`BlockRole`](specs.h.md#BlockRole), [`kIn`](specs.h.md#BlockRole.kIn)
- used by: [`TestBody`](../kiln_test.cc.md#KilnTest_TileScalarOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_SimplifiedOverloadsAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarFloatOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_LiteralOverloads_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RotateGatherExtractBitcastAndMaskedStore_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_TypeHelpersInsideKernel_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BitwiseOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ForLoopWithInductionVarAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarMismatchedTypesFail_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarPrefetchAndLoop_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_DTypeInTileAndScalarOps_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedAndSignedCasts_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RefSliceRankCollapsing_Test.TestBody), [`RegisterSpec`](kernel.h.md#RegisterSpec)

### <a id="KernelSpec"></a>`KernelSpec`
- def: [`csrc/internal/mosaic/kiln/core/specs.h:75`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L75)
- signature: `struct KernelSpec`
- members:
  - <a id="KernelSpec.grid"></a>`grid` — [`L76`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L76)
  - <a id="KernelSpec.in_specs"></a>`in_specs` — [`L78`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L78)
  - <a id="KernelSpec.out_specs"></a>`out_specs` — [`L79`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L79)
  - <a id="KernelSpec.scalar_prefetch"></a>`scalar_prefetch` — [`L77`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L77)
  - <a id="KernelSpec.scratch"></a>`scratch` — [`L80`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L80)
- uses (calls/refs, reference-scoped): [`GridSpec`](specs.h.md#GridSpec), [`BlockSpec`](specs.h.md#BlockSpec), [`ScalarPrefetchSpec`](specs.h.md#ScalarPrefetchSpec), [`ScratchSpec`](specs.h.md#ScratchSpec)
- used by: [`BuildKernel`](kernel.cc.md#BuildKernel), [`EmitIndexMapFunction`](kernel.cc.md#EmitIndexMapFunction), [`KernelScope`](kernel.cc.md#KernelScope.KernelScope), [`SetGridAttributes`](kernel.cc.md#SetGridAttributes), [`CreateKernelImpl`](kernel.h.md#CreateKernelImpl), [`RegisterSpec`](kernel.h.md#RegisterSpec), [`RegisterSpec`](kernel.h.md#RegisterSpec), [`NumPrograms`](kernel.cc.md#NumPrograms), [`impl_`](kernel.h.md#Kernel.impl_), [`GridRank`](kernel.cc.md#GridRank), [`RegisterSpec`](kernel.h.md#RegisterSpec), [`RegisterSpec`](kernel.h.md#RegisterSpec), [`builder`](kernel.cc.md#KernelScope.builder), [`RegisterSpec`](kernel.h.md#RegisterSpec)

### <a id="MemorySpace"></a>`MemorySpace`
- def: [`csrc/internal/mosaic/kiln/core/specs.h:28`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L28)
- signature: `enum class MemorySpace`
- members:
  - <a id="MemorySpace.kSmem"></a>`kSmem` — [`L28`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L28)
  - <a id="MemorySpace.kVmem"></a>`kVmem` — [`L28`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L28)
- used by: [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarFloatOperations_Test.TestBody), [`BlockType`](kernel.cc.md#BlockType), [`memory_space`](specs.h.md#BasicBlockSpec.memory_space), [`index_map`](specs.h.md#BasicBlockSpec.index_map), [`memory_space`](specs.h.md#ScratchSpec.memory_space), [`dtype`](specs.h.md#ScratchSpec.dtype)

### <a id="OutSpec"></a>`OutSpec`
- def: [`csrc/internal/mosaic/kiln/core/specs.h:55`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L55)
- signature: `using OutSpec = BasicBlockSpec<BlockRole::kOut>`
- uses (calls/refs, reference-scoped): [`kOut`](specs.h.md#BlockRole.kOut), [`BasicBlockSpec`](specs.h.md#BasicBlockSpec), [`BlockRole`](specs.h.md#BlockRole)
- used by: [`TestBody`](../kiln_test.cc.md#KilnTest_TileScalarOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_SimplifiedOverloadsAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarFloatOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_LiteralOverloads_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RotateGatherExtractBitcastAndMaskedStore_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_TypeHelpersInsideKernel_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BitwiseOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ForLoopWithInductionVarAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarMismatchedTypesFail_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarPrefetchAndLoop_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_DTypeInTileAndScalarOps_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedAndSignedCasts_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RefSliceRankCollapsing_Test.TestBody), [`RegisterSpec`](kernel.h.md#RegisterSpec)

### <a id="ScalarPrefetchSpec"></a>`ScalarPrefetchSpec`
- def: [`csrc/internal/mosaic/kiln/core/specs.h:63`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L63)
- signature: `struct ScalarPrefetchSpec`
- members:
  - <a id="ScalarPrefetchSpec.dtype"></a>`dtype` — [`L65`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L65)
  - <a id="ScalarPrefetchSpec.shape"></a>`shape` — [`L64`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L64)
- uses (calls/refs, reference-scoped): [`DType`](dtype.h.md#DType), [`Shape`](dtype.h.md#Shape)
- used by: [`BuildKernel`](kernel.cc.md#BuildKernel), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarPrefetchAndLoop_Test.TestBody), [`KernelScope`](kernel.cc.md#KernelScope.KernelScope), [`grid`](specs.h.md#KernelSpec.grid), [`RegisterSpec`](kernel.h.md#RegisterSpec)

### <a id="ScratchSpec"></a>`ScratchSpec`
- def: [`csrc/internal/mosaic/kiln/core/specs.h:57`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L57)
- signature: `struct ScratchSpec`
- members:
  - <a id="ScratchSpec.dtype"></a>`dtype` — [`L59`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L59)
  - <a id="ScratchSpec.memory_space"></a>`memory_space` — [`L60`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L60)
  - <a id="ScratchSpec.shape"></a>`shape` — [`L58`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/specs.h#L58)
- uses (calls/refs, reference-scoped): [`DType`](dtype.h.md#DType), [`Shape`](dtype.h.md#Shape), [`MemorySpace`](specs.h.md#MemorySpace), [`kVmem`](specs.h.md#MemorySpace.kVmem)
- used by: [`BuildKernel`](kernel.cc.md#BuildKernel), [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`KernelScope`](kernel.cc.md#KernelScope.KernelScope), [`RegisterSpec`](kernel.h.md#RegisterSpec), [`out_specs`](specs.h.md#KernelSpec.out_specs)

