---
title: 'Module: csrc/internal/mosaic/kiln/core/context.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/context.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/internal/
symbols:
  unwrap: unwrap(f840c5a22b5d1e2c).
  wrap: wrap(9577566eb3ca8ae6).
  ValueAccess: ValueAccess#
  BuilderScope: BuilderScope#
  BuilderScope.prev_: BuilderScope#prev_.
  ValueAccess.Get: ValueAccess#Get(f840c5a22b5d1e2c).
  ValueAccess.Make: ValueAccess#Make(9577566eb3ca8ae6).
  BuilderScope.operator: BuilderScope#`operator=`(a66817c5015f7ec9).
  BuilderScope.BuilderScope: BuilderScope#BuilderScope(158743baab76d149).
---
# Module: [`csrc/internal/mosaic/kiln/core/context.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.h)

## Classes
### <a id="BuilderScope"></a>`BuilderScope`
- def: [`csrc/internal/mosaic/kiln/core/context.h:32`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.h#L32)
- doc: RAII helper to install and restore the active thread-local builder.
- signature: `class BuilderScope`
- members:
  - <a id="BuilderScope.BuilderScope"></a>`BuilderScope(const BuilderScope&)` — [`L37`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.h#L37)
  - <a id="BuilderScope.operator"></a>`operator=(const BuilderScope&)` — [`L38`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.h#L38)
  - <a id="BuilderScope.prev_"></a>`prev_` — [`L41`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.h#L41)
- uses (calls/refs, reference-scoped): [`DType`](dtype.h.md#DType), [`CurrentBuilder`](context.cc.md#CurrentBuilder), [`ToMlirType`](context.cc.md#ToMlirType), [`ToMlirType`](context.cc.md#ToMlirType), [`BuilderScope`](context.cc.md#BuilderScope.BuilderScope), [`~BuilderScope`](context.cc.md#BuilderScope.-BuilderScope)
- used by: [`CurrentBuilder`](context.cc.md#CurrentBuilder), [`spec`](kernel.cc.md#KernelScope.spec), [`BuilderScope`](context.cc.md#BuilderScope.BuilderScope), [`~BuilderScope`](context.cc.md#BuilderScope.-BuilderScope)

### <a id="ValueAccess"></a>`ValueAccess`
- def: [`csrc/internal/mosaic/kiln/core/context.h:51`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.h#L51) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- signature: `struct ValueAccess`
- members:
  - <a id="ValueAccess.Get"></a>`Get(const ValueBase& v)` — [`L52`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.h#L52)
  - <a id="ValueAccess.Make"></a>`Make(mlir::Value v, DType dtype)` — [`L56`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.h#L56)
- uses (calls/refs, reference-scoped): [`DType`](dtype.h.md#DType), [`ValueBase`](value_base.h.md#ValueBase), [`impl`](value_base.h.md#ValueBase.impl)
- used by: [`Scalar`](scalar.h.md#Scalar), [`unwrap`](context.h.md#unwrap), [`Cond`](cond.h.md#Cond), [`wrap`](context.h.md#wrap), [`operator()`](ref.h.md#Ref.operator), [`Gather`](tile.h.md#Tile.Gather), [`impl`](value_base.h.md#ValueBase.impl)

## Functions
- <a id="unwrap"></a>`unwrap(const ValueBase& v)` — [`L61`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.h#L61) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- <a id="wrap"></a>`wrap(mlir::Value v, DType dtype)` — [`L64`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/context.h#L64) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)

