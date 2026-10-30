---
title: 'Module: csrc/internal/mosaic/kiln/core/tile.cc'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/tile.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/
symbols:
  Tile.rank: Tile#rank(57a65ae535d7db84).
  Tile.shape: Tile#shape(ca5f3f460c69a328).
  Dot: Dot(43ec172705795562).
  Tile.Tile: Tile#Tile(8bb134018e17eaec).
  Tile.Lanes: Tile#Lanes(42c9c5acc1bb8895).
  Tile.Reshape: Tile#Reshape(a073675ddd08ff98).
  Reduce: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/tile.cc`/Reduce(fe1b8d8aa18a0a74).'
  Tile.Gather: Tile#Gather(4c04137040efea54).
  Iota: Iota(559ce6db7d0e5145).
  Tile.Rotate: Tile#Rotate(4b164ec27b4fb090).
  Full: Full(daffaaa50c228af).
  Tile.Slice: Tile#Slice(17e3a81bbc234f60).
  Splat: Splat(a3b39acfd2b19835).
  MaxReduce: MaxReduce(b67a849e39f0576d).
  NInf: NInf(e391de935d1f2903).
  Tile.Extract: Tile#Extract(31699b53f270fbe6).
  Tile.BroadcastTo: Tile#BroadcastTo(a073675ddd08ff98).
  Zeros: Zeros(e391de935d1f2903).
  SumReduce: SumReduce(b67a849e39f0576d).
  MinValue: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/tile.cc`/MinValue(fc43f7c664df2f42).'
  Reciprocal: Reciprocal(735358cb9a449e0a).
  Transpose: Transpose(3b6c45358a9b700).
  Tile.Full: Tile#Full(b41e689cc09aa588).
  Tile.ToShape: Tile#ToShape(a073675ddd08ff98).
  VectorTypeOf: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/tile.cc`/VectorTypeOf(d3a431ed081b79a4).'
  Tile.num_elements: Tile#num_elements(57a65ae535d7db84).
  Tile.Squeeze: Tile#Squeeze(d2f5bebfb031fb).
  SplatConstant: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/tile.cc`/SplatConstant(5efc3ca6f7cafb18).'
---
# Module: [`csrc/internal/mosaic/kiln/core/tile.cc`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc)

## Functions
- <a id="Dot"></a>`Dot(Tile lhs, Tile rhs, const DotOptions& options)` — [`L331`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L331) — 2-D matmul on the MXU with f32 accumulation. — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Full"></a>`Full(llvm::ArrayRef<int64_t> shape, DType dtype, Literal value)` — [`L250`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L250) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Iota"></a>`Iota(llvm::ArrayRef<int64_t> shape, DType dtype, int axis)` — [`L270`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L270) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="MaxReduce"></a>`MaxReduce(Tile t, int axis)` — [`L299`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L299) — Reductions along `axis`, keeping the reduced dimension as size 1. — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="MinValue"></a>`MinValue(mlir::ImplicitLocOpBuilder& b, DType dtype)` — [`L68`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L68) — Get the min value for the given dtype.
- <a id="NInf"></a>`NInf(llvm::ArrayRef<int64_t> shape, DType dtype)` — [`L259`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L259) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Reciprocal"></a>`Reciprocal(Tile t, bool approx)` — [`L290`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L290) — Approximate or exact reciprocal (`tpu.reciprocal`).
- <a id="Reduce"></a>`Reduce(const Tile& t, int axis, vector::CombiningKind kind, mlir::TypedAttr init)` — [`L85`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L85) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Splat"></a>`Splat(Scalar scalar, llvm::ArrayRef<int64_t> shape)` — [`L285`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L285)
- <a id="SplatConstant"></a>`SplatConstant(mlir::ImplicitLocOpBuilder& b, mlir::VectorType type, mlir::TypedAttr attr)` — [`L59`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L59)
- <a id="SumReduce"></a>`SumReduce(Tile t, int axis)` — [`L314`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L314)
- <a id="Transpose"></a>`Transpose(Tile t)` — [`L322`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L322) — 2-D transpose.
- <a id="VectorTypeOf"></a>`VectorTypeOf(const Tile& t)` — [`L55`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L55)
- <a id="Zeros"></a>`Zeros(llvm::ArrayRef<int64_t> shape, DType dtype)` — [`L246`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L246) — Tile constructors. — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)

## Other members
- `Tile` — [`L105`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L105)
- <a id="Tile.BroadcastTo"></a>`Tile.BroadcastTo` — [`L150`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L150) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Tile.Extract"></a>`Tile.Extract` — [`L228`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L228) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Tile.Full"></a>`Tile.Full` — [`L242`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L242)
- <a id="Tile.Gather"></a>`Tile.Gather` — [`L207`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L207) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Tile.Lanes"></a>`Tile.Lanes` — [`L155`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L155) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Tile.Reshape"></a>`Tile.Reshape` — [`L123`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L123) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Tile.Rotate"></a>`Tile.Rotate` — [`L194`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L194) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Tile.Slice"></a>`Tile.Slice` — [`L173`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L173) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Tile.Squeeze"></a>`Tile.Squeeze` — [`L136`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L136)
- <a id="Tile.Tile"></a>`Tile.Tile` — [`L111`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L111) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Tile.ToShape"></a>`Tile.ToShape` — [`L142`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L142)
- <a id="Tile.num_elements"></a>`Tile.num_elements` — [`L119`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L119)
- <a id="Tile.rank"></a>`Tile.rank` — [`L117`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L117) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="Tile.shape"></a>`Tile.shape` — [`L113`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/tile.cc#L113) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)

