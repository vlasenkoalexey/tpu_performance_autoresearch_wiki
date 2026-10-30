---
title: 'Module: csrc/internal/mosaic/kiln/core/kernel.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/kernel.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/
symbols:
  Kernel: Kernel#
  CreateKernel: CreateKernel(cc3699a2f10d5357).
  CreateKernelImpl: internal/CreateKernelImpl(a63ad72acc905aac).
  RegisterSpec.Resolver: internal/RegisterSpec(134d053c09a608a9).Resolver#
  RegisterSpec: internal/RegisterSpec(8d0246d5dc1b2d67).
  Kernel.impl_: Kernel#impl_.
  ToString: ToString(a326bb71bdfb4a47).
---
# Module: [`csrc/internal/mosaic/kiln/core/kernel.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h)

## Classes
### <a id="Kernel"></a>`Kernel`
- def: [`csrc/internal/mosaic/kiln/core/kernel.h:56`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h#L56) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- doc: An opaque handle to a lowered KILN kernel module.
- signature: `class Kernel`
- members:
  - <a id="Kernel.impl_"></a>`impl_` — [`L75`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h#L75)
- uses (calls/refs, reference-scoped): [`BuildKernel`](kernel.cc.md#BuildKernel), [`Serialize`](kernel.cc.md#Kernel.Serialize), [`Verify`](kernel.cc.md#Kernel.Verify), [`ToString`](kernel.cc.md#Kernel.ToString), [`KernelSpec`](specs.h.md#KernelSpec), [`Impl`](kernel.cc.md#Kernel.Impl), [`Kernel`](kernel.cc.md#Kernel.Kernel), [`Kernel`](kernel.cc.md#Kernel.Kernel), [`operator=`](kernel.cc.md#Kernel.operator), [`~Kernel`](kernel.cc.md#Kernel.-Kernel)
- used by: [`BuildKernel`](kernel.cc.md#BuildKernel), [`TestBody`](../kiln_test.cc.md#KilnTest_TileScalarOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_SimplifiedOverloadsAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarFloatOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_LiteralOverloads_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RotateGatherExtractBitcastAndMaskedStore_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_TypeHelpersInsideKernel_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BitwiseOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ForLoopWithInductionVarAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarMismatchedTypesFail_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarPrefetchAndLoop_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_DTypeInTileAndScalarOps_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedAndSignedCasts_Test.TestBody), [`Serialize`](kernel.cc.md#Kernel.Serialize), [`TestBody`](../kiln_test.cc.md#KilnTest_RefSliceRankCollapsing_Test.TestBody), [`Verify`](kernel.cc.md#Kernel.Verify), [`ExpectKernelMatches`](../kiln_test.cc.md#KilnTest.ExpectKernelMatches), [`CreateKernelImpl`](kernel.h.md#CreateKernelImpl), [`ToString`](kernel.cc.md#Kernel.ToString), [`Resolver`](kernel.h.md#RegisterSpec.Resolver), [`GetAt`](kernel.cc.md#GetAt), [`Scratch`](kernel.cc.md#Scratch), [`module`](kernel.cc.md#Kernel.Impl.module), [`Kernel`](kernel.cc.md#Kernel.Kernel), [`ToString`](kernel.h.md#ToString), [`Kernel`](kernel.cc.md#Kernel.Kernel), [`operator=`](kernel.cc.md#Kernel.operator), [`~Kernel`](kernel.cc.md#Kernel.-Kernel)

### <a id="RegisterSpec.Resolver"></a>`RegisterSpec.Resolver`
- def: [`csrc/internal/mosaic/kiln/core/kernel.h:110`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h#L110)
- signature: `using Resolver = decltype(RegisterSpec(k, *s))`
- uses (calls/refs, reference-scoped): [`Ref`](ref.h.md#Ref), [`Kernel`](kernel.h.md#Kernel), [`RegisterSpec`](kernel.h.md#RegisterSpec), [`RegisterSpec`](kernel.h.md#RegisterSpec), [`RegisterSpec`](kernel.h.md#RegisterSpec), [`RegisterSpec`](kernel.h.md#RegisterSpec), [`RegisterSpec`](kernel.h.md#RegisterSpec)

## Functions
- <a id="CreateKernel"></a>`CreateKernel(GridSpec grid, SpecsAndBody&&... specs_and_body)` — [`L150`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h#L150) — Builds a Mosaic kernel from a `GridSpec`, a variadic list of operand specs
- `CreateKernelImpl(GridSpec grid, std::index_sequence<Is...>, SpecsAndBody&&... specs_and_body)` — [`L122`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h#L122)
- <a id="CreateKernelImpl"></a>`CreateKernelImpl(GridSpec grid, std::index_sequence<Is...>, SpecsAndBody&&... specs_and_body)` — [`L122`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h#L122)
- `RegisterSpec(KernelSpec& k, const std::optional<Spec>& s)` — [`L109`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h#L109)
- <a id="RegisterSpec"></a>`RegisterSpec(KernelSpec& k, const OutSpec& s)` — [`L98`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h#L98)
- `RegisterSpec(KernelSpec& k, const ScalarPrefetchSpec& s)` — [`L88`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h#L88)
- `RegisterSpec(KernelSpec& k, const InSpec& s)` — [`L93`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h#L93)
- `RegisterSpec(KernelSpec& k, const ScratchSpec& s)` — [`L103`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h#L103)
- <a id="ToString"></a>`ToString(const Kernel& kernel)` — [`L158`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/kernel.h#L158) — Pretty-prints a kernel (for logging / tests).

