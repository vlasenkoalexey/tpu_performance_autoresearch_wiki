---
title: 'Module: csrc/internal/mosaic/kiln/core/elementwise.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/elementwise.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/
symbols:
  ElementwiseOps: internal/ElementwiseOps#
  operator: operator+(f80f7d6260b3ee3a).
  WithElementwiseOps.AsType: WithElementwiseOps#AsType(a1eec924e4552342).
  WithElementwiseOps.Ops: WithElementwiseOps#Ops#
  WithElementwiseOps.ToF32: WithElementwiseOps#ToF32(8f5363d873dd4781).
  Select: Select(9fa7fe51f4fbe656).
  WithElementwiseOps.ToI32: WithElementwiseOps#ToI32(8f5363d873dd4781).
  WithElementwiseOps.Bitcast: WithElementwiseOps#Bitcast(a1eec924e4552342).
  WithElementwiseOps.ToBF16: WithElementwiseOps#ToBF16(8f5363d873dd4781).
  Min: Min(f80f7d6260b3ee3a).
  WithElementwiseOps: WithElementwiseOps#
  Max: Max(f80f7d6260b3ee3a).
  Bitcast: Bitcast(6f235b18fd188b9a).
  Abs: Abs(ada6a8422704cf8a).
  WithElementwiseOps.ToU8: WithElementwiseOps#ToU8(8f5363d873dd4781).
  WithElementwiseOps.ToU64: WithElementwiseOps#ToU64(8f5363d873dd4781).
  WithElementwiseOps.ToU16: WithElementwiseOps#ToU16(8f5363d873dd4781).
  WithElementwiseOps.ToU32: WithElementwiseOps#ToU32(8f5363d873dd4781).
  Rsqrt: Rsqrt(ada6a8422704cf8a).
  Log: Log(ada6a8422704cf8a).
  Sqrt: Sqrt(ada6a8422704cf8a).
  Exp: Exp(ada6a8422704cf8a).
  Exp2: Exp2(ada6a8422704cf8a).
  Log2: Log2(ada6a8422704cf8a).
  Tanh: Tanh(ada6a8422704cf8a).
  WithElementwiseOps.derived: WithElementwiseOps#derived(ea465e50d690edfe).
---
# Module: [`csrc/internal/mosaic/kiln/core/elementwise.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h)

## Classes
### <a id="ElementwiseOps"></a>`ElementwiseOps`
- def: [`csrc/internal/mosaic/kiln/core/elementwise.h:41`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L41) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- doc: Emitters for the elementwise operations shared by `Scalar` and `Tile`.
- signature: `template <typename T, typename CmpResult> struct ElementwiseOps`
- uses (calls/refs, reference-scoped): [`Tile`](tile.h.md#Tile), [`Scalar`](scalar.h.md#Scalar), [`DType`](dtype.h.md#DType), [`Cond`](cond.h.md#Cond), [`Select`](elementwise_impl.h.md#ElementwiseOps.Select), [`Neg`](elementwise_impl.h.md#ElementwiseOps.Neg), [`Abs`](elementwise_impl.h.md#ElementwiseOps.Abs), [`AsType`](elementwise_impl.h.md#ElementwiseOps.AsType), [`Bitcast`](elementwise_impl.h.md#ElementwiseOps.Bitcast), [`Rem`](elementwise_impl.h.md#ElementwiseOps.Rem), [`Eq`](elementwise_impl.h.md#ElementwiseOps.Eq), [`Ge`](elementwise_impl.h.md#ElementwiseOps.Ge), [`Gt`](elementwise_impl.h.md#ElementwiseOps.Gt), [`Le`](elementwise_impl.h.md#ElementwiseOps.Le), [`Lt`](elementwise_impl.h.md#ElementwiseOps.Lt), [`Ne`](elementwise_impl.h.md#ElementwiseOps.Ne), [`Add`](elementwise_impl.h.md#ElementwiseOps.Add), [`And`](elementwise_impl.h.md#ElementwiseOps.And), [`Div`](elementwise_impl.h.md#ElementwiseOps.Div), [`Exp`](elementwise_impl.h.md#ElementwiseOps.Exp), [`Exp2`](elementwise_impl.h.md#ElementwiseOps.Exp2), [`Log`](elementwise_impl.h.md#ElementwiseOps.Log), [`Log2`](elementwise_impl.h.md#ElementwiseOps.Log2), [`Max`](elementwise_impl.h.md#ElementwiseOps.Max), [`Min`](elementwise_impl.h.md#ElementwiseOps.Min), [`Mul`](elementwise_impl.h.md#ElementwiseOps.Mul), [`Or`](elementwise_impl.h.md#ElementwiseOps.Or), [`Rsqrt`](elementwise_impl.h.md#ElementwiseOps.Rsqrt), [`ShiftLeft`](elementwise_impl.h.md#ElementwiseOps.ShiftLeft), [`ShiftRight`](elementwise_impl.h.md#ElementwiseOps.ShiftRight), [`Sqrt`](elementwise_impl.h.md#ElementwiseOps.Sqrt), [`Sub`](elementwise_impl.h.md#ElementwiseOps.Sub), [`Tanh`](elementwise_impl.h.md#ElementwiseOps.Tanh), [`Xor`](elementwise_impl.h.md#ElementwiseOps.Xor)
- used by: [`Ops`](elementwise.h.md#WithElementwiseOps.Ops), [`Select`](elementwise_impl.h.md#ElementwiseOps.Select), [`UnaryFloat`](elementwise_impl.h.md#UnaryFloat), [`Neg`](elementwise_impl.h.md#ElementwiseOps.Neg), [`AsType`](elementwise_impl.h.md#ElementwiseOps.AsType), [`Bitcast`](elementwise_impl.h.md#ElementwiseOps.Bitcast), [`Rem`](elementwise_impl.h.md#ElementwiseOps.Rem), [`Eq`](elementwise_impl.h.md#ElementwiseOps.Eq), [`Ge`](elementwise_impl.h.md#ElementwiseOps.Ge), [`Gt`](elementwise_impl.h.md#ElementwiseOps.Gt), [`Le`](elementwise_impl.h.md#ElementwiseOps.Le), [`Lt`](elementwise_impl.h.md#ElementwiseOps.Lt), [`Ne`](elementwise_impl.h.md#ElementwiseOps.Ne), [`Add`](elementwise_impl.h.md#ElementwiseOps.Add), [`And`](elementwise_impl.h.md#ElementwiseOps.And), [`Div`](elementwise_impl.h.md#ElementwiseOps.Div), [`Exp`](elementwise_impl.h.md#ElementwiseOps.Exp), [`Exp2`](elementwise_impl.h.md#ElementwiseOps.Exp2), [`Log`](elementwise_impl.h.md#ElementwiseOps.Log), [`Log2`](elementwise_impl.h.md#ElementwiseOps.Log2), [`Max`](elementwise_impl.h.md#ElementwiseOps.Max), [`Min`](elementwise_impl.h.md#ElementwiseOps.Min), [`Mul`](elementwise_impl.h.md#ElementwiseOps.Mul), [`Or`](elementwise_impl.h.md#ElementwiseOps.Or), [`Rsqrt`](elementwise_impl.h.md#ElementwiseOps.Rsqrt), [`ShiftLeft`](elementwise_impl.h.md#ElementwiseOps.ShiftLeft), [`ShiftRight`](elementwise_impl.h.md#ElementwiseOps.ShiftRight), [`Sqrt`](elementwise_impl.h.md#ElementwiseOps.Sqrt), [`Sub`](elementwise_impl.h.md#ElementwiseOps.Sub), [`Tanh`](elementwise_impl.h.md#ElementwiseOps.Tanh), [`Xor`](elementwise_impl.h.md#ElementwiseOps.Xor)

### <a id="WithElementwiseOps"></a>`WithElementwiseOps`
- def: [`csrc/internal/mosaic/kiln/core/elementwise.h:93`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L93)
- doc: CRTP mixin providing the elementwise operators and math functions shared by
- signature: `template <typename Derived, typename CmpResult = Derived> class WithElementwiseOps`
- members:
  - <a id="WithElementwiseOps.AsType"></a>`AsType(DType target)` — [`L98`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L98) — Element type conversion (float<->float, int<->float, int widths). — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
  - <a id="WithElementwiseOps.Bitcast"></a>`Bitcast(DType target)` — [`L101`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L101) — Reinterprets the bit pattern of each element as `target` (must have the
  - <a id="WithElementwiseOps.ToBF16"></a>`ToBF16()` — [`L110`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L110)
  - <a id="WithElementwiseOps.ToF32"></a>`ToF32()` — [`L109`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L109)
  - <a id="WithElementwiseOps.ToI32"></a>`ToI32()` — [`L104`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L104)
  - <a id="WithElementwiseOps.ToU16"></a>`ToU16()` — [`L106`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L106)
  - <a id="WithElementwiseOps.ToU32"></a>`ToU32()` — [`L107`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L107)
  - <a id="WithElementwiseOps.ToU64"></a>`ToU64()` — [`L108`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L108)
  - <a id="WithElementwiseOps.ToU8"></a>`ToU8()` — [`L105`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L105)
  - <a id="WithElementwiseOps.derived"></a>`derived()` — [`L189`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L189)
- uses (calls/refs, reference-scoped): [`Tile`](tile.h.md#Tile), [`Scalar`](scalar.h.md#Scalar), [`DType`](dtype.h.md#DType), [`Float32Type`](dtype.h.md#Float32Type), [`Int32Type`](dtype.h.md#Int32Type), [`Ops`](elementwise.h.md#WithElementwiseOps.Ops), [`UInt32Type`](dtype.h.md#UInt32Type), [`BFloat16Type`](dtype.h.md#BFloat16Type), [`UInt8Type`](dtype.h.md#UInt8Type), [`UInt16Type`](dtype.h.md#UInt16Type), [`UInt64Type`](dtype.h.md#UInt64Type)
- used by: [`Tile`](tile.h.md#Tile), [`Scalar`](scalar.h.md#Scalar), [`TestBody`](../kiln_test.cc.md#KilnTest_TileScalarOperations_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_LiteralOverloads_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BlockwiseMatmul_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_BitwiseOperations_Test.TestBody), [`EmitIndexMapFunction`](kernel.cc.md#EmitIndexMapFunction), [`TestBody`](../kiln_test.cc.md#KilnTest_DTypeInTileAndScalarOps_Test.TestBody), [`TestBody`](../kiln_test.cc.md#KilnTest_UnsignedAndSignedCasts_Test.TestBody), [`SliceRefImpl`](ref.cc.md#SliceRefImpl), [`Store`](ref.cc.md#Ref.Store), [`Rotate`](tile.cc.md#Tile.Rotate), [`operator=`](ref.cc.md#Ref.operator)

### <a id="WithElementwiseOps.Ops"></a>`WithElementwiseOps.Ops`
- def: [`csrc/internal/mosaic/kiln/core/elementwise.h:94`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L94)
- signature: `using Ops = internal::ElementwiseOps<Derived, CmpResult>`
- uses (calls/refs, reference-scoped): [`ElementwiseOps`](elementwise.h.md#ElementwiseOps)
- used by: [`operator+`](elementwise.h.md#operator), [`AsType`](elementwise.h.md#WithElementwiseOps.AsType), [`Select`](elementwise.h.md#Select), [`Bitcast`](elementwise.h.md#WithElementwiseOps.Bitcast), [`operator==`](elementwise.h.md#operator), [`Min`](elementwise.h.md#Min), [`operator%`](elementwise.h.md#operator), [`operator/`](elementwise.h.md#operator), [`operator>>`](elementwise.h.md#operator), [`operator|`](elementwise.h.md#operator), [`Abs`](elementwise.h.md#Abs), [`Max`](elementwise.h.md#Max), [`operator!=`](elementwise.h.md#operator), [`operator&`](elementwise.h.md#operator), [`operator<`](elementwise.h.md#operator), [`operator<=`](elementwise.h.md#operator), [`operator>`](elementwise.h.md#operator), [`operator^`](elementwise.h.md#operator), [`Exp`](elementwise.h.md#Exp), [`Log`](elementwise.h.md#Log), [`Rsqrt`](elementwise.h.md#Rsqrt), [`Sqrt`](elementwise.h.md#Sqrt), [`operator*`](elementwise.h.md#operator), [`operator-`](elementwise.h.md#operator), [`operator-`](elementwise.h.md#operator), [`operator<<`](elementwise.h.md#operator), [`operator>=`](elementwise.h.md#operator), [`Exp2`](elementwise.h.md#Exp2), [`Log2`](elementwise.h.md#Log2), [`Tanh`](elementwise.h.md#Tanh)

## Functions
- <a id="Abs"></a>`Abs(Derived v)` — [`L185`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L185)
- <a id="Bitcast"></a>`Bitcast(Derived v, DType target)` — [`L186`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L186)
- <a id="Exp"></a>`Exp(Derived v)` — [`L178`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L178) — Unary math on floating-point operands (`Abs` also accepts integers).
- <a id="Exp2"></a>`Exp2(Derived v)` — [`L179`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L179)
- <a id="Log"></a>`Log(Derived v)` — [`L180`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L180)
- <a id="Log2"></a>`Log2(Derived v)` — [`L181`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L181)
- <a id="Max"></a>`Max(Derived lhs, Derived rhs)` — [`L172`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L172)
- <a id="Min"></a>`Min(Derived lhs, Derived rhs)` — [`L171`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L171) — Elementwise min / max / select. On bool operands `Min` / `Max` are
- <a id="Rsqrt"></a>`Rsqrt(Derived v)` — [`L183`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L183)
- <a id="Select"></a>`Select(CmpResult mask, Derived if_true, Derived if_false)` — [`L173`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L173)
- <a id="Sqrt"></a>`Sqrt(Derived v)` — [`L182`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L182)
- <a id="Tanh"></a>`Tanh(Derived v)` — [`L184`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L184)
- `operator!=(Derived lhs, Derived rhs)` — [`L153`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L153)
- `operator%(Derived lhs, Derived rhs)` — [`L127`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L127) — Remainder; integer operands only.
- `operator&(Derived lhs, Derived rhs)` — [`L133`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L133) — Bitwise / logical ops on integer and bool (mask) operands. `>>` is an
- `operator*(Derived lhs, Derived rhs)` — [`L120`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L120)
- <a id="operator"></a>`operator+(Derived lhs, Derived rhs)` — [`L114`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L114) — documented in [kiln-kernel-dsl](../../../../../../concepts/kiln-kernel-dsl.md)
- `operator-(Derived v)` — [`L113`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L113) — Arithmetic on integer or floating-point operands.
- `operator-(Derived lhs, Derived rhs)` — [`L117`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L117)
- `operator/(Derived lhs, Derived rhs)` — [`L123`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L123)
- `operator<(Derived lhs, Derived rhs)` — [`L156`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L156)
- `operator<<(Derived lhs, Derived rhs)` — [`L142`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L142)
- `operator<=(Derived lhs, Derived rhs)` — [`L159`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L159)
- `operator==(Derived lhs, Derived rhs)` — [`L150`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L150) — Comparisons on integer or floating-point operands.
- `operator>(Derived lhs, Derived rhs)` — [`L162`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L162)
- `operator>=(Derived lhs, Derived rhs)` — [`L165`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L165)
- `operator>>(Derived lhs, Derived rhs)` — [`L145`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L145)
- `operator^(Derived lhs, Derived rhs)` — [`L139`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L139)
- `operator|(Derived lhs, Derived rhs)` — [`L136`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise.h#L136)

