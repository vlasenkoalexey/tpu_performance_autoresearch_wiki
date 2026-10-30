---
title: 'Module: csrc/internal/mosaic/kiln/core/ref.cc'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/ref.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/
symbols:
  Ref.operator: Ref#`operator=`(5b698a2ea967c03f).
  SliceRefImpl: internal/SliceRefImpl(ec6e33d7df1154da).
  Ref.Store: Ref#Store(dd67c6c98bf872a9).
  Ref.operator-Tile: Ref#`operator Tile`(d2f5bebfb031fb).
  Ref.rank: Ref#rank(57a65ae535d7db84).
  Ref.operator-Scalar: Ref#`operator Scalar`(a6b4eefc4c3c7356).
  Ref.shape: Ref#shape(ca5f3f460c69a328).
  Ref.Ref: Ref#Ref(cac036679d256d0e).
  MemRefTypeOf: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/ref.cc`/MemRefTypeOf(17e843e516807bf8).'
  HasMemorySpace: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/ref.cc`/HasMemorySpace(2d0e918ffd4c79b2).'
  IsSmemRef: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/ref.cc`/IsSmemRef(f3162fe5c35bb0fc).'
  IsVmemRef: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/ref.cc`/IsVmemRef(f3162fe5c35bb0fc).'
  ZeroIndices: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/ref.cc`/ZeroIndices(e6e417a31e6f2419).'
---
# Module: [`csrc/internal/mosaic/kiln/core/ref.cc`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc)

## Functions
- <a id="HasMemorySpace"></a>`HasMemorySpace(const Ref& r, tpu::MemorySpace expected_space)` — [`L59`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L59)
- <a id="IsSmemRef"></a>`IsSmemRef(const Ref& r)` — [`L65`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L65)
- <a id="IsVmemRef"></a>`IsVmemRef(const Ref& r)` — [`L69`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L69)
- <a id="MemRefTypeOf"></a>`MemRefTypeOf(const Ref& r)` — [`L55`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L55)
- <a id="SliceRefImpl"></a>`SliceRefImpl(Ref base, llvm::ArrayRef<DimDesc> dims)` — [`L148`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L148) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="ZeroIndices"></a>`ZeroIndices(mlir::ImplicitLocOpBuilder& b, int64_t rank)` — [`L49`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L49)

## Other members
- `operator=` — [`L86`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L86)
- <a id="Ref.Ref"></a>`Ref.Ref` — [`L75`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L75)
- <a id="Ref.Store"></a>`Ref.Store` — [`L119`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L119) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Ref.operator"></a>`Ref.operator` — [`L81`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L81) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Ref.operator-Scalar"></a>`Ref.operator-Scalar` — [`L97`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L97) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Ref.operator-Tile"></a>`Ref.operator-Tile` — [`L108`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L108) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Ref.rank"></a>`Ref.rank` — [`L144`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L144)
- <a id="Ref.shape"></a>`Ref.shape` — [`L140`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/ref.cc#L140)

