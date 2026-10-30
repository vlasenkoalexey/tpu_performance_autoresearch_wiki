---
title: 'Module: csrc/ops/round/round_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/round/round_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenRoundDecimalsOut: AtenRoundDecimalsOut(bb14b1a8f74bfba5).
  AtenRoundOut: AtenRoundOut(4655895dd4ef7692).
  ValidateNumericDtype: '`$anonymous_namespace_csrc/ops/round/round_aten_kernels.cc`/ValidateNumericDtype(90723f725b74ed91).'
  GetRoundFunctional: '`$anonymous_namespace_csrc/ops/round/round_aten_kernels.cc`/GetRoundFunctional(958806b738c7c32f).'
---
# Module: [`csrc/ops/round/round_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/round/round_aten_kernels.cc)

## Functions
- <a id="AtenRoundDecimalsOut"></a>`AtenRoundDecimalsOut(const at::Tensor& self, int64_t decimals, at::Tensor& out)` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/round/round_aten_kernels.cc#L72)
- <a id="AtenRoundOut"></a>`AtenRoundOut(const at::Tensor& self, at::Tensor& out)` — [`L61`](../../../../../../../raw/code/torch_tpu/csrc/ops/round/round_aten_kernels.cc#L61)
- <a id="GetRoundFunctional"></a>`GetRoundFunctional(int64_t decimals)` — [`L42`](../../../../../../../raw/code/torch_tpu/csrc/ops/round/round_aten_kernels.cc#L42)
- <a id="ValidateNumericDtype"></a>`ValidateNumericDtype(at::ScalarType scalar_type)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/round/round_aten_kernels.cc#L49) — Check that the provided dtype is appropriate for rounding.

