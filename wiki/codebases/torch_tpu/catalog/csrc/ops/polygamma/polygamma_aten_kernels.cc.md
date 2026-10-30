---
title: 'Module: csrc/ops/polygamma/polygamma_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/polygamma/polygamma_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenPolygammaOut: AtenPolygammaOut(f45958b75ca857c5).
  BuildPolygammaShlo: '`$anonymous_namespace_csrc/ops/polygamma/polygamma_aten_kernels.cc`/BuildPolygammaShlo(2a68a8517faa8fcb).'
  BuildZeta: '`$anonymous_namespace_csrc/ops/polygamma/polygamma_aten_kernels.cc`/BuildZeta(e7d667c95bb7d9f4).'
  EvaluatePolynomial: '`$anonymous_namespace_csrc/ops/polygamma/polygamma_aten_kernels.cc`/EvaluatePolynomial(5707232bf0321dfe).'
  GetEpsilon: '`$anonymous_namespace_csrc/ops/polygamma/polygamma_aten_kernels.cc`/GetEpsilon(1da28fdfc09cd382).'
  ComputeCotDerivativeCoeffs: '`$anonymous_namespace_csrc/ops/polygamma/polygamma_aten_kernels.cc`/ComputeCotDerivativeCoeffs(7864480464b09eea).'
  kPi: '`$anonymous_namespace_csrc/ops/polygamma/polygamma_aten_kernels.cc`/kPi.'
---
# Module: [`csrc/ops/polygamma/polygamma_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/polygamma/polygamma_aten_kernels.cc)

## Functions
- <a id="AtenPolygammaOut"></a>`AtenPolygammaOut(int64_t n, const at::Tensor& self, at::Tensor& out)` — [`L408`](../../../../../../../raw/code/torch_tpu/csrc/ops/polygamma/polygamma_aten_kernels.cc#L408)
- <a id="BuildPolygammaShlo"></a>`BuildPolygammaShlo(mlir::MlirOp self_op, int64_t n, mlir::ElementType out_mlir_type)` — [`L294`](../../../../../../../raw/code/torch_tpu/csrc/ops/polygamma/polygamma_aten_kernels.cc#L294) — Computes the polygamma function of order n at self_op.
- <a id="BuildZeta"></a>`BuildZeta(mlir::MlirOp x, mlir::MlirOp q, mlir::MlirBuilder& builder)` — [`L107`](../../../../../../../raw/code/torch_tpu/csrc/ops/polygamma/polygamma_aten_kernels.cc#L107) — Computes the Hurwitz Zeta function of x and q.
- `ComputeCotDerivativeCoeffs(int n)` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/polygamma/polygamma_aten_kernels.cc#L56)
- <a id="ComputeCotDerivativeCoeffs"></a>`ComputeCotDerivativeCoeffs(int n)` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/polygamma/polygamma_aten_kernels.cc#L56)
- `EvaluatePolynomial(mlir::MlirOp y, const std::vector<double>& coeffs)` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/ops/polygamma/polygamma_aten_kernels.cc#L77)
- <a id="EvaluatePolynomial"></a>`EvaluatePolynomial(mlir::MlirOp y, const std::vector<double>& coeffs)` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/ops/polygamma/polygamma_aten_kernels.cc#L77)
- <a id="GetEpsilon"></a>`GetEpsilon(mlir::ElementType type)` — [`L89`](../../../../../../../raw/code/torch_tpu/csrc/ops/polygamma/polygamma_aten_kernels.cc#L89) — Returns the machine epsilon for the given type.

## Module values
- <a id="kPi"></a>`kPi` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/polygamma/polygamma_aten_kernels.cc#L54)

