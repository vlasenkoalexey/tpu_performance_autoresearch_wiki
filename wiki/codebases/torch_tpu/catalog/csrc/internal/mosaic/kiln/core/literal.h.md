---
title: 'Module: csrc/internal/mosaic/kiln/core/literal.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/literal.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/
symbols:
  Literal.Literal: Literal#Literal(9b289cee16747614).
  Literal: Literal#
  operator: '`operator==`(1e99b4c6ecdc046e).'
  Select: Select(61b49fb2205eafce).
  Max: Max(3d8acda827e36bf0).
  WithLiteralOps: WithLiteralOps#
  Min: Min(3d8acda827e36bf0).
  Literal.value_: Literal#value_.
  Literal.AsDouble: Literal#AsDouble(21b6c25e127938e2).
  Literal.AsInt: Literal#AsInt(57a65ae535d7db84).
  Literal.IsInt: Literal#IsInt(50ce9a9e25b4a850).
  Literal.IsDouble: Literal#IsDouble(50ce9a9e25b4a850).
---
# Module: [`csrc/internal/mosaic/kiln/core/literal.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h)

## Classes
### <a id="Literal"></a>`Literal`
- def: [`csrc/internal/mosaic/kiln/core/literal.h:29`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L29) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- doc: A numeric literal holding either `int64_t` or `double`. Implicitly
- signature: `class Literal`
- members:
  - <a id="Literal.AsDouble"></a>`AsDouble()` — [`L47`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L47)
  - <a id="Literal.AsInt"></a>`AsInt()` — [`L44`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L44)
  - <a id="Literal.IsDouble"></a>`IsDouble()` — [`L42`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L42)
  - <a id="Literal.IsInt"></a>`IsInt()` — [`L41`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L41)
  - <a id="Literal.Literal"></a>`Literal(T v)` — [`L33`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L33) — implicit — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
  - <a id="Literal.value_"></a>`value_` — [`L52`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L52)
- used by: [`Scalar`](scalar.h.md#Scalar), [`TestBody`](../kiln_test.cc.md#KilnTest_TileScalarOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_SimplifiedOverloadsAndBounds_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarFloatOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_LiteralOverloads_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_RotateGatherExtractBitcastAndMaskedStore_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BitwiseOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_ForLoopWithInductionVarAndBounds_Test.TestBody), [`wrap`](context.h.md#wrap), [`TestBody`](../kiln_test.cc.md#KilnTest_ScalarMismatchedTypesFail_Test.TestBody), [`I32`](scalar.cc.md#I32), [`Gather`](tile.h.md#Tile.Gather), [`U32`](scalar.cc.md#U32), [`MakeConstant`](tile.h.md#Tile.MakeConstant), [`LiteralToAttr`](context.cc.md#LiteralToAttr), [`Full`](tile.cc.md#Full), [`MakeScalarConstant`](scalar.cc.md#MakeScalarConstant), [`Zeros`](tile.cc.md#Zeros), [`SumReduce`](tile.cc.md#SumReduce), [`F32`](scalar.cc.md#F32), [`Full`](tile.cc.md#Tile.Full), [`operator==`](literal.h.md#operator), [`ToScalar`](index_arg.h.md#IndexArg.ToScalar), [`Select`](literal.h.md#Select), [`operator+`](literal.h.md#operator), [`MakeConstant`](scalar.cc.md#Scalar.MakeConstant), [`operator&`](literal.h.md#operator), [`Max`](literal.h.md#Max), [`operator<<`](literal.h.md#operator), [`operator<<`](literal.h.md#operator), [`Min`](literal.h.md#Min), [`operator*`](literal.h.md#operator), [`operator>`](literal.h.md#operator), [`Max`](literal.h.md#Max), [`Min`](literal.h.md#Min), [`Select`](literal.h.md#Select), [`operator%`](literal.h.md#operator), [`operator%`](literal.h.md#operator)  (+23 more)

### <a id="WithLiteralOps"></a>`WithLiteralOps`
- def: [`csrc/internal/mosaic/kiln/core/literal.h:59`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L59)
- doc: CRTP mixin providing (Derived, Literal) and (Literal, Derived) binary
- signature: `template <typename Derived, typename CmpResult = Derived> class WithLiteralOps`
- uses (calls/refs, reference-scoped): [`Tile`](tile.h.md#Tile), [`Scalar`](scalar.h.md#Scalar)
- used by: [`Tile`](tile.h.md#Tile), [`Scalar`](scalar.h.md#Scalar)

## Functions
- <a id="Max"></a>`Max(Derived lhs, Literal rhs)` — [`L122`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L122)
- `Max(Literal lhs, Derived rhs)` — [`L125`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L125)
- `Min(Literal lhs, Derived rhs)` — [`L119`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L119)
- <a id="Min"></a>`Min(Derived lhs, Literal rhs)` — [`L116`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L116) — Elementwise min / max / select
- `Select(CmpResult cond, Literal if_true, Derived if_false)` — [`L131`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L131)
- <a id="Select"></a>`Select(CmpResult cond, Derived if_true, Literal if_false)` — [`L128`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L128)
- `operator!=(Literal lhs, Derived rhs)` — [`L143`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L143)
- `operator!=(Derived lhs, Literal rhs)` — [`L140`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L140)
- `operator%(Literal lhs, Derived rhs)` — [`L85`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L85)
- `operator%(Derived lhs, Literal rhs)` — [`L82`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L82)
- `operator&(Literal lhs, Derived rhs)` — [`L93`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L93)
- `operator&(Derived lhs, Literal rhs)` — [`L90`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L90) — Bitwise / logical ops
- `operator*(Derived lhs, Literal rhs)` — [`L72`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L72)
- `operator*(Literal lhs, Derived rhs)` — [`L75`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L75)
- `operator+(Literal lhs, Derived rhs)` — [`L65`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L65)
- `operator+(Derived lhs, Literal rhs)` — [`L62`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L62) — Arithmetic
- `operator-(Derived lhs, Literal rhs)` — [`L66`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L66)
- `operator-(Literal lhs, Derived rhs)` — [`L69`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L69)
- `operator/(Derived lhs, Literal rhs)` — [`L76`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L76)
- `operator/(Literal lhs, Derived rhs)` — [`L79`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L79)
- `operator<(Literal lhs, Derived rhs)` — [`L147`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L147)
- `operator<(Derived lhs, Literal rhs)` — [`L144`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L144)
- `operator<<(Derived lhs, Literal rhs)` — [`L102`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L102)
- `operator<<(Literal lhs, Derived rhs)` — [`L105`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L105)
- `operator<=(Derived lhs, Literal rhs)` — [`L148`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L148)
- `operator<=(Literal lhs, Derived rhs)` — [`L151`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L151)
- `operator==(Literal lhs, Derived rhs)` — [`L139`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L139)
- <a id="operator"></a>`operator==(Derived lhs, Literal rhs)` — [`L136`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L136) — Comparisons
- `operator>(Derived lhs, Literal rhs)` — [`L152`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L152)
- `operator>(Literal lhs, Derived rhs)` — [`L155`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L155)
- `operator>=(Derived lhs, Literal rhs)` — [`L156`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L156)
- `operator>=(Literal lhs, Derived rhs)` — [`L159`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L159)
- `operator>>(Derived lhs, Literal rhs)` — [`L108`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L108)
- `operator>>(Literal lhs, Derived rhs)` — [`L111`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L111)
- `operator^(Literal lhs, Derived rhs)` — [`L101`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L101)
- `operator^(Derived lhs, Literal rhs)` — [`L98`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L98)
- `operator|(Derived lhs, Literal rhs)` — [`L94`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L94)
- `operator|(Literal lhs, Derived rhs)` — [`L97`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/literal.h#L97)

