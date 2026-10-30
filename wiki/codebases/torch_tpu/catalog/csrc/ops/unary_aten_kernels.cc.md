---
title: 'Module: csrc/ops/unary_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/unary_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  UnaryOpOut: UnaryOpOut(d45fb58d5560ff35).
  AtenSignOut: AtenSignOut(4655895dd4ef7692).
  AtenFloorOut: AtenFloorOut(4655895dd4ef7692).
  AtenFracOut: AtenFracOut(4655895dd4ef7692).
  AtenCeilOut: AtenCeilOut(4655895dd4ef7692).
  AtenRelu_: AtenRelu_(2c0150b1d2cc4760).
  AtenRelu: AtenRelu(28959186f7a4bda8).
  AtenSignbitOut: AtenSignbitOut(4655895dd4ef7692).
  AtenErfOut: AtenErfOut(4655895dd4ef7692).
  AtenTruncOut: AtenTruncOut(4655895dd4ef7692).
  AtenErfInvOut: AtenErfInvOut(4655895dd4ef7692).
  AtenAbsOut: AtenAbsOut(4655895dd4ef7692).
  AtenSqrtOut: AtenSqrtOut(4655895dd4ef7692).
  AtenCosOut: AtenCosOut(4655895dd4ef7692).
  AtenExp2Out: AtenExp2Out(4655895dd4ef7692).
  AtenTanOut: AtenTanOut(4655895dd4ef7692).
  AtenTanhOut: AtenTanhOut(4655895dd4ef7692).
  AtenSinhOut: AtenSinhOut(4655895dd4ef7692).
  AtenRsqrtOut: AtenRsqrtOut(4655895dd4ef7692).
  AtenExpm1Out: AtenExpm1Out(4655895dd4ef7692).
  AtenLog10Out: AtenLog10Out(4655895dd4ef7692).
  AtenAsinhOut: AtenAsinhOut(4655895dd4ef7692).
  AtenAcoshOut: AtenAcoshOut(4655895dd4ef7692).
  AtenReciprocalOut: AtenReciprocalOut(4655895dd4ef7692).
  AtenLog1pOut: AtenLog1pOut(4655895dd4ef7692).
  AtenExpOut: AtenExpOut(4655895dd4ef7692).
  AtenLogOut: AtenLogOut(4655895dd4ef7692).
  AtenCoshOut: AtenCoshOut(4655895dd4ef7692).
  AtenLgammaOut: AtenLgammaOut(4655895dd4ef7692).
  AtenSinOut: AtenSinOut(4655895dd4ef7692).
  AtenAcosOut: AtenAcosOut(4655895dd4ef7692).
  AtenAsinOut: AtenAsinOut(4655895dd4ef7692).
  AtenLog2Out: AtenLog2Out(4655895dd4ef7692).
  AtenAtanOut: AtenAtanOut(4655895dd4ef7692).
  AtenAtanhOut: AtenAtanhOut(4655895dd4ef7692).
  UnaryOp: UnaryOp(aff119914ebf96f1).
  AtenNegOut: AtenNegOut(4655895dd4ef7692).
  AtenConjPhysicalOut: AtenConjPhysicalOut(4655895dd4ef7692).
  AtenSgnOut: AtenSgnOut(4655895dd4ef7692).
  AtenBitwiseNotOut: AtenBitwiseNotOut(4655895dd4ef7692).
  AtenLiftFreshOut: AtenLiftFreshOut(4655895dd4ef7692).
  UnaryOpInPlace: UnaryOpInPlace(8f66957868df415e).
  ValidateNotComplex: ValidateNotComplex(d8359b99282c084c).
---
# Module: [`csrc/ops/unary_aten_kernels.cc`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc)

## Functions
- <a id="AtenAbsOut"></a>`AtenAbsOut(const at::Tensor& self, at::Tensor& out)` — [`L229`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L229) — go/keep-sorted end
- <a id="AtenAcosOut"></a>`AtenAcosOut(OpName::kAcosOut, AtenAcos, BuildAcosShlo)` — [`L202`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L202)
- <a id="AtenAcoshOut"></a>`AtenAcoshOut(OpName::kAcoshOut, AtenAcosh, BuildAcoshShlo)` — [`L203`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L203)
- <a id="AtenAsinOut"></a>`AtenAsinOut(OpName::kAsinOut, AtenAsin, BuildAsinShlo)` — [`L204`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L204)
- <a id="AtenAsinhOut"></a>`AtenAsinhOut(OpName::kAsinhOut, AtenAsinh, BuildAsinhShlo)` — [`L205`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L205)
- <a id="AtenAtanOut"></a>`AtenAtanOut(OpName::kAtanOut, AtenAtan, BuildAtanShlo)` — [`L206`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L206)
- <a id="AtenAtanhOut"></a>`AtenAtanhOut(OpName::kAtanhOut, AtenAtanh, BuildAtanhShlo)` — [`L207`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L207)
- <a id="AtenBitwiseNotOut"></a>`AtenBitwiseNotOut(OpName::kBitwiseNotOut, AtenBitwiseNot, BuildNotShlo)` — [`L373`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L373)
- <a id="AtenCeilOut"></a>`AtenCeilOut(const at::Tensor& self, at::Tensor& out)` — [`L381`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L381) — go/keep-sorted end
- <a id="AtenConjPhysicalOut"></a>`AtenConjPhysicalOut(OpName::kConjPhysicalOut, AtenConjPhysical, BuildConjPhysicalShlo)` — [`L374`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L374)
- <a id="AtenCosOut"></a>`AtenCosOut(OpName::kCosOut, AtenCos, BuildCosShlo)` — [`L208`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L208)
- <a id="AtenCoshOut"></a>`AtenCoshOut(OpName::kCoshOut, AtenCosh, BuildCoshShlo)` — [`L209`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L209)
- <a id="AtenErfInvOut"></a>`AtenErfInvOut(const at::Tensor& self, at::Tensor& out)` — [`L262`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L262)
- <a id="AtenErfOut"></a>`AtenErfOut(const at::Tensor& self, at::Tensor& out)` — [`L246`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L246)
- <a id="AtenExp2Out"></a>`AtenExp2Out(OpName::kExp2Out, AtenExp2, BuildExp2Shlo)` — [`L210`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L210)
- <a id="AtenExpOut"></a>`AtenExpOut(OpName::kExpOut, AtenExp, BuildExpShlo)` — [`L212`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L212)
- <a id="AtenExpm1Out"></a>`AtenExpm1Out(OpName::kExpM1Out, AtenExpm1, BuildExpm1Shlo)` — [`L211`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L211)
- <a id="AtenFloorOut"></a>`AtenFloorOut(const at::Tensor& self, at::Tensor& out)` — [`L394`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L394)
- <a id="AtenFracOut"></a>`AtenFracOut(const at::Tensor& self, at::Tensor& out)` — [`L407`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L407)
- <a id="AtenLgammaOut"></a>`AtenLgammaOut(OpName::kLgammaOut, AtenLgamma, BuildLgammaShlo)` — [`L213`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L213)
- <a id="AtenLiftFreshOut"></a>`AtenLiftFreshOut(OpName::kLiftFreshOut, AtenLiftFresh, BuildLiftFreshShlo)` — [`L376`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L376)
- <a id="AtenLog10Out"></a>`AtenLog10Out(OpName::kLog10Out, AtenLog10, BuildLog10Shlo)` — [`L215`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L215)
- <a id="AtenLog1pOut"></a>`AtenLog1pOut(OpName::kLog1pOut, AtenLog1p, BuildLog1pShlo)` — [`L216`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L216)
- <a id="AtenLog2Out"></a>`AtenLog2Out(OpName::kLog2Out, AtenLog2, BuildLog2Shlo)` — [`L217`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L217)
- <a id="AtenLogOut"></a>`AtenLogOut(OpName::kLogOut, AtenLog, BuildLogShlo)` — [`L218`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L218)
- <a id="AtenNegOut"></a>`AtenNegOut(const at::Tensor& self, at::Tensor& out)` — [`L278`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L278)
- <a id="AtenReciprocalOut"></a>`AtenReciprocalOut(OpName::kReciprocalOut, AtenReciprocal, BuildReciprocalShlo)` — [`L219`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L219)
- <a id="AtenRelu"></a>`AtenRelu(const at::Tensor& self)` — [`L288`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L288) — Relu requires both an in-place and out-of-place kernel.
- <a id="AtenRelu_"></a>`AtenRelu_(at::Tensor& self)` — [`L301`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L301)
- <a id="AtenRsqrtOut"></a>`AtenRsqrtOut(OpName::kRsqrtOut, AtenRsqrt, BuildRsqrtShlo)` — [`L221`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L221)
- <a id="AtenSgnOut"></a>`AtenSgnOut(OpName::kSgnOut, AtenSgn, BuildSgnShlo)` — [`L378`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L378)
- <a id="AtenSignOut"></a>`AtenSignOut(const at::Tensor& self, at::Tensor& out)` — [`L313`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L313)
- <a id="AtenSignbitOut"></a>`AtenSignbitOut(const at::Tensor& self, at::Tensor& out)` — [`L328`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L328)
- <a id="AtenSinOut"></a>`AtenSinOut(OpName::kSinOut, AtenSin, BuildSinShlo)` — [`L222`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L222)
- <a id="AtenSinhOut"></a>`AtenSinhOut(OpName::kSinhOut, AtenSinh, BuildSinhShlo)` — [`L223`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L223)
- <a id="AtenSqrtOut"></a>`AtenSqrtOut(OpName::kSqrtOut, AtenSqrt, BuildSqrtShlo)` — [`L224`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L224)
- <a id="AtenTanOut"></a>`AtenTanOut(OpName::kTanOut, AtenTan, BuildTanShlo)` — [`L225`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L225)
- <a id="AtenTanhOut"></a>`AtenTanhOut(OpName::kTanhOut, AtenTanh, BuildTanhShlo)` — [`L226`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L226)
- <a id="AtenTruncOut"></a>`AtenTruncOut(const at::Tensor& self, at::Tensor& out)` — [`L360`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L360)
- `UnaryOp(const at::Tensor& self, OpName op_name, MlirUnaryOpBuilder op_builder, UnaryOpOptions options)` — [`L130`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L130)
- <a id="UnaryOp"></a>`UnaryOp(const at::Tensor& self, MlirUnaryOpBuilder op_builder, UnaryOpOptions options)` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L106) — Safely applies a functional unary operation to the input tensor. — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)
- <a id="UnaryOpInPlace"></a>`UnaryOpInPlace(at::Tensor& self, MlirUnaryOpBuilder op_builder, UnaryOpOptions options)` — [`L140`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L140) — Like UnaryOpCallback, but the result overwrites the input. — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)
- `UnaryOpInPlace(at::Tensor& self, OpName op_name, MlirUnaryOpBuilder op_builder, UnaryOpOptions options)` — [`L153`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L153)
- <a id="UnaryOpOut"></a>`UnaryOpOut(const at::Tensor& self, at::Tensor& out, MlirUnaryOpBuilder op_builder, UnaryOpOptions options)` — [`L163`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L163) — Like UnaryOpCallback, but the result overwrites the provided `out` tensor. — documented in [aten-kernel-authoring](../../../concepts/aten-kernel-authoring.md)
- `UnaryOpOut(const at::Tensor& self, at::Tensor& out, OpName op_name, MlirUnaryOpBuilder op_builder, UnaryOpOptions options)` — [`L192`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L192)
- <a id="ValidateNotComplex"></a>`ValidateNotComplex(const at::Tensor& tensor, const std::string_view arg_name)` — [`L98`](../../../../../../raw/code/torch_tpu/csrc/ops/unary_aten_kernels.cc#L98)

