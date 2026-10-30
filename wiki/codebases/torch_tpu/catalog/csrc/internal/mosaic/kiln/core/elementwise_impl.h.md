---
title: 'Module: csrc/internal/mosaic/kiln/core/elementwise_impl.h'
type: catalog
provenance: extracted
module: csrc/internal/mosaic/kiln/core/elementwise_impl.h
status: fresh
symbol_base: cxx . . $ torch_tpu/kiln/internal/
symbols:
  Compare: Compare(52d6c663bd6167fa).
  ElementwiseOps.Select: ElementwiseOps#Select(9fa7fe51f4fbe656).
  UnaryFloat: UnaryFloat(ee9bd89164e44e8d).
  EmitBinary: EmitBinary(81585f0897c1969c).
  ElementwiseOps.Neg: ElementwiseOps#Neg(ada6a8422704cf8a).
  ElementwiseOps.Abs: ElementwiseOps#Abs(ada6a8422704cf8a).
  ElementwiseOps.Bitcast: ElementwiseOps#Bitcast(6f235b18fd188b9a).
  Bitwise: Bitwise(81f358263ddc9d67).
  Arith: Arith(6078e244e01e1ea7).
  ElementwiseOps.Rem: ElementwiseOps#Rem(f80f7d6260b3ee3a).
  ElementwiseOps.AsType: ElementwiseOps#AsType(6f235b18fd188b9a).
  ElementwiseOps.Ge: ElementwiseOps#Ge(432a41af475097c9).
  ElementwiseOps.Gt: ElementwiseOps#Gt(432a41af475097c9).
  ElementwiseOps.Eq: ElementwiseOps#Eq(432a41af475097c9).
  ElementwiseOps.Ne: ElementwiseOps#Ne(432a41af475097c9).
  ElementwiseOps.Le: ElementwiseOps#Le(432a41af475097c9).
  ElementwiseOps.Lt: ElementwiseOps#Lt(432a41af475097c9).
  ElementwiseOps.And: ElementwiseOps#And(f80f7d6260b3ee3a).
  ElementwiseOps.Log2: ElementwiseOps#Log2(ada6a8422704cf8a).
  ElementwiseOps.Add: ElementwiseOps#Add(f80f7d6260b3ee3a).
  ElementwiseOps.Xor: ElementwiseOps#Xor(f80f7d6260b3ee3a).
  ElementwiseOps.Sub: ElementwiseOps#Sub(f80f7d6260b3ee3a).
  ElementwiseOps.Div: ElementwiseOps#Div(f80f7d6260b3ee3a).
  ElementwiseOps.Mul: ElementwiseOps#Mul(f80f7d6260b3ee3a).
  ElementwiseOps.Tanh: ElementwiseOps#Tanh(ada6a8422704cf8a).
  ElementwiseOps.Exp: ElementwiseOps#Exp(ada6a8422704cf8a).
  ElementwiseOps.Min: ElementwiseOps#Min(f80f7d6260b3ee3a).
  ElementwiseOps.Max: ElementwiseOps#Max(f80f7d6260b3ee3a).
  ElementwiseOps.Exp2: ElementwiseOps#Exp2(ada6a8422704cf8a).
  ElementwiseOps.Sqrt: ElementwiseOps#Sqrt(ada6a8422704cf8a).
  ElementwiseOps.ShiftRight: ElementwiseOps#ShiftRight(f80f7d6260b3ee3a).
  ElementwiseOps.Or: ElementwiseOps#Or(f80f7d6260b3ee3a).
  ElementwiseOps.Log: ElementwiseOps#Log(ada6a8422704cf8a).
  ElementwiseOps.Rsqrt: ElementwiseOps#Rsqrt(ada6a8422704cf8a).
  ElementwiseOps.ShiftLeft: ElementwiseOps#ShiftLeft(f80f7d6260b3ee3a).
  CheckSameDType: CheckSameDType(9e9ecd5409840685).
  CheckIntOrFloat: CheckIntOrFloat(ae49bf5e02efe79a).
---
# Module: [`csrc/internal/mosaic/kiln/core/elementwise_impl.h`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h)

## Functions
- <a id="Arith"></a>`Arith(T lhs, T rhs, std::string_view what)` — [`L77`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L77) — Binary op on integer or floating-point operands, dispatching on the element
- <a id="Bitwise"></a>`Bitwise(T lhs, T rhs, std::string_view what)` — [`L91`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L91) — Binary op on integer or bool (mask) operands.
- <a id="CheckIntOrFloat"></a>`CheckIntOrFloat(T v, std::string_view what)` — [`L58`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L58)
- <a id="CheckSameDType"></a>`CheckSameDType(T lhs, T rhs, std::string_view what)` — [`L52`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L52)
- <a id="Compare"></a>`Compare(T lhs, T rhs, mlir::arith::CmpFPredicate fpred, mlir::arith::CmpIPredicate ipred)` — [`L99`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L99)
- `Compare(T lhs, T rhs, mlir::arith::CmpFPredicate fpred, mlir::arith::CmpIPredicate signed_ipred, mlir::arith::CmpIPredicate unsigned_ipred)` — [`L116`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L116)
- <a id="EmitBinary"></a>`EmitBinary(T lhs, T rhs)` — [`L66`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L66) — Aligns the operand shapes and emits the binary `Op`. Callers validate the
- <a id="UnaryFloat"></a>`UnaryFloat(T v, std::string_view what)` — [`L125`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L125)

## Other members
- <a id="ElementwiseOps.Abs"></a>`ElementwiseOps.Abs` — [`L316`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L316)
- <a id="ElementwiseOps.Add"></a>`ElementwiseOps.Add` — [`L152`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L152)
- <a id="ElementwiseOps.And"></a>`ElementwiseOps.And` — [`L201`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L201)
- <a id="ElementwiseOps.AsType"></a>`ElementwiseOps.AsType` — [`L132`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L132)
- <a id="ElementwiseOps.Bitcast"></a>`ElementwiseOps.Bitcast` — [`L137`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L137)
- <a id="ElementwiseOps.Div"></a>`ElementwiseOps.Div` — [`L167`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L167)
- <a id="ElementwiseOps.Eq"></a>`ElementwiseOps.Eq` — [`L229`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L229)
- <a id="ElementwiseOps.Exp"></a>`ElementwiseOps.Exp` — [`L281`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L281)
- <a id="ElementwiseOps.Exp2"></a>`ElementwiseOps.Exp2` — [`L286`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L286)
- <a id="ElementwiseOps.Ge"></a>`ElementwiseOps.Ge` — [`L262`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L262)
- <a id="ElementwiseOps.Gt"></a>`ElementwiseOps.Gt` — [`L255`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L255)
- <a id="ElementwiseOps.Le"></a>`ElementwiseOps.Le` — [`L248`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L248)
- <a id="ElementwiseOps.Log"></a>`ElementwiseOps.Log` — [`L291`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L291)
- <a id="ElementwiseOps.Log2"></a>`ElementwiseOps.Log2` — [`L296`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L296)
- <a id="ElementwiseOps.Lt"></a>`ElementwiseOps.Lt` — [`L241`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L241)
- <a id="ElementwiseOps.Max"></a>`ElementwiseOps.Max` — [`L192`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L192)
- <a id="ElementwiseOps.Min"></a>`ElementwiseOps.Min` — [`L183`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L183)
- <a id="ElementwiseOps.Mul"></a>`ElementwiseOps.Mul` — [`L162`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L162)
- <a id="ElementwiseOps.Ne"></a>`ElementwiseOps.Ne` — [`L235`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L235)
- <a id="ElementwiseOps.Neg"></a>`ElementwiseOps.Neg` — [`L142`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L142)
- <a id="ElementwiseOps.Or"></a>`ElementwiseOps.Or` — [`L206`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L206)
- <a id="ElementwiseOps.Rem"></a>`ElementwiseOps.Rem` — [`L173`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L173)
- <a id="ElementwiseOps.Rsqrt"></a>`ElementwiseOps.Rsqrt` — [`L306`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L306)
- <a id="ElementwiseOps.Select"></a>`ElementwiseOps.Select` — [`L269`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L269)
- <a id="ElementwiseOps.ShiftLeft"></a>`ElementwiseOps.ShiftLeft` — [`L216`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L216)
- <a id="ElementwiseOps.ShiftRight"></a>`ElementwiseOps.ShiftRight` — [`L221`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L221)
- <a id="ElementwiseOps.Sqrt"></a>`ElementwiseOps.Sqrt` — [`L301`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L301)
- <a id="ElementwiseOps.Sub"></a>`ElementwiseOps.Sub` — [`L157`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L157)
- <a id="ElementwiseOps.Tanh"></a>`ElementwiseOps.Tanh` — [`L311`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L311)
- <a id="ElementwiseOps.Xor"></a>`ElementwiseOps.Xor` — [`L211`](../../../../../../../../../raw/code/torch_tpu/csrc/internal/mosaic/kiln/core/elementwise_impl.h#L211)

