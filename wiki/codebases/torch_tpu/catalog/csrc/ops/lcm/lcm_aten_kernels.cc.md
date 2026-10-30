---
title: 'Module: csrc/ops/lcm/lcm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/lcm/lcm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenLcmOut: AtenLcmOut(dcc870e438d8791).
  ValidateLcmInputs: '`$anonymous_namespace_csrc/ops/lcm/lcm_aten_kernels.cc`/ValidateLcmInputs(6ddad2e2cbb424ad).'
  BuildLcmShlo: '`$anonymous_namespace_csrc/ops/lcm/lcm_aten_kernels.cc`/BuildLcmShlo(9dd408ac7de815bd).'
  BuildGcdShlo: '`$anonymous_namespace_csrc/ops/lcm/lcm_aten_kernels.cc`/BuildGcdShlo(43934ba9e2582ad7).'
  kMaxGcdIterationsI64: '`$anonymous_namespace_csrc/ops/lcm/lcm_aten_kernels.cc`/kMaxGcdIterationsI64.'
  kMaxGcdIterationsI32: '`$anonymous_namespace_csrc/ops/lcm/lcm_aten_kernels.cc`/kMaxGcdIterationsI32.'
---
# Module: [`csrc/ops/lcm/lcm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/lcm/lcm_aten_kernels.cc)

## Functions
- <a id="AtenLcmOut"></a>`AtenLcmOut(const at::Tensor& self, const at::Tensor& other, at::Tensor& out)` — [`L161`](../../../../../../../raw/code/torch_tpu/csrc/ops/lcm/lcm_aten_kernels.cc#L161)
- <a id="BuildGcdShlo"></a>`BuildGcdShlo(mlir::MlirOp a, mlir::MlirOp b, const int32_t max_iters)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/lcm/lcm_aten_kernels.cc#L63) — Computes the greatest common divisor of `a` and `b` (which must share the
- <a id="BuildLcmShlo"></a>`BuildLcmShlo(mlir::MlirOp self, mlir::MlirOp other)` — [`L122`](../../../../../../../raw/code/torch_tpu/csrc/ops/lcm/lcm_aten_kernels.cc#L122)
- <a id="ValidateLcmInputs"></a>`ValidateLcmInputs(const at::Tensor& self, const at::Tensor& other, const at::Tensor& out)` — [`L50`](../../../../../../../raw/code/torch_tpu/csrc/ops/lcm/lcm_aten_kernels.cc#L50)

## Module values
- <a id="kMaxGcdIterationsI32"></a>`kMaxGcdIterationsI32` — [`L47`](../../../../../../../raw/code/torch_tpu/csrc/ops/lcm/lcm_aten_kernels.cc#L47) — Upper bounds on Euclidean algorithm iterations by Lamé's theorem:
- <a id="kMaxGcdIterationsI64"></a>`kMaxGcdIterationsI64` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/lcm/lcm_aten_kernels.cc#L48)

