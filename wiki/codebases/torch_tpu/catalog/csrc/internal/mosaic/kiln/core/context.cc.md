---
title: 'Module: csrc/internal/mosaic/kiln/core/context.cc'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/context.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/internal/
symbols:
  CurrentBuilder: CurrentBuilder(4e4d1e92161e2696).
  ToMlirType: ToMlirType(835e0705205d24e6).
  EmitCast: EmitCast(a810a74f9211c8f4).
  LiteralToAttr: LiteralToAttr(9558e8353792cb75).
  EmitBitcast: EmitBitcast(a810a74f9211c8f4).
  BuilderScope.BuilderScope: BuilderScope#BuilderScope(a0624967aed5266f).
  EmitIntCast: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/context.cc`/EmitIntCast(c57276435655ca4b).'
  tls_builder: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/context.cc`/tls_builder.'
  BuilderScope.-BuilderScope: BuilderScope#`~BuilderScope`(ced63f7c635d850d).
  WithElementType: '`$anonymous_namespace_csrc/internal/mosaic/kiln/core/context.cc`/WithElementType(fca8d8b231b04b5b).'
---
# Module: [`csrc/internal/mosaic/kiln/core/context.cc`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.cc)

## Functions
- <a id="CurrentBuilder"></a>`CurrentBuilder()` — [`L70`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.cc#L70) — Returns the active MLIR ImplicitLocOpBuilder for the current thread. — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="EmitBitcast"></a>`EmitBitcast(mlir::Value value, DType source, DType target)` — [`L148`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.cc#L148)
- <a id="EmitCast"></a>`EmitCast(mlir::Value value, DType source, DType target)` — [`L112`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.cc#L112)
- <a id="EmitIntCast"></a>`EmitIntCast(mlir::ImplicitLocOpBuilder& b, mlir::Value value, DType source, DType target, mlir::Type dst_mlir_type)` — [`L47`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.cc#L47)
- <a id="LiteralToAttr"></a>`LiteralToAttr(mlir::ImplicitLocOpBuilder& b, DType dtype, Literal literal)` — [`L102`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.cc#L102)
- `ToMlirType(DType dtype)` — [`L98`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.cc#L98)
- <a id="ToMlirType"></a>`ToMlirType(DType dtype, mlir::MLIRContext* ctx)` — [`L83`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.cc#L83)
- <a id="WithElementType"></a>`WithElementType(mlir::Type type, DType target)` — [`L39`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.cc#L39)

## Module values
- <a id="tls_builder"></a>`tls_builder` — [`L37`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.cc#L37)

## Other members
- <a id="BuilderScope.-BuilderScope"></a>`BuilderScope.-BuilderScope` — [`L81`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.cc#L81)
- <a id="BuilderScope.BuilderScope"></a>`BuilderScope.BuilderScope` — [`L76`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.cc#L76)

