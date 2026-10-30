---
title: 'Module: csrc/internal/mosaic/kiln/core/cond.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/cond.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/Cond#
symbols:
  Cond: ''
---
# Module: [`csrc/internal/mosaic/kiln/core/cond.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/cond.h)

## Classes
### <a id="Cond"></a>`Cond`  ·  implements/extends ValueBase
- def: [`csrc/internal/mosaic/kiln/core/cond.h:26`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/cond.h#L26) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- doc: An i1 scalar condition handle.
- signature: `class Cond : public ValueBase`
- uses (calls/refs, reference-scoped): [`DType`](dtype.h.md#DType), [`ValueAccess`](context.h.md#ValueAccess), [`ValueBase`](value_base.h.md#ValueBase), [`Cond`](cond.cc.md#Cond.Cond), [`operator!`](cond.cc.md#operator), [`operator&&`](cond.cc.md#operator), [`operator||`](cond.cc.md#operator)
- used by: [`Scalar`](scalar.h.md#Scalar), [`ElementwiseOps`](elementwise.h.md#ElementwiseOps), [`TestBody`](../kiln_test.cc.md#KilnTest_SimplifiedOverloadsAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_LiteralOverloads_Test.TestBody), [`If`](control_flow.cc.md#If), [`ValueBase`](value_base.h.md#ValueBase), [`operator Cond`](scalar.cc.md#Scalar.operator-Cond), [`Cond`](cond.cc.md#Cond.Cond), [`If`](control_flow.cc.md#If), [`Scalar`](scalar.cc.md#Scalar.Scalar), [`operator!`](cond.cc.md#operator), [`operator&&`](cond.cc.md#operator), [`operator||`](cond.cc.md#operator)

