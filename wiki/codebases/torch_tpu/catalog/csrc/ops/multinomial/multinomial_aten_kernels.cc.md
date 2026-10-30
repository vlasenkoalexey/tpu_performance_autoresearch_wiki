---
title: 'Module: csrc/ops/multinomial/multinomial_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/multinomial/multinomial_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenMultinomial: AtenMultinomial(e311a927be854b0e).
  AtenMultinomialOut: AtenMultinomialOut(833a0c8c30699c50).
  ValidateInputs: '`$anonymous_namespace_csrc/ops/multinomial/multinomial_aten_kernels.cc`/ValidateInputs(3fee75a57e1cc4e0).'
  GetRngUsage: '`$anonymous_namespace_csrc/ops/multinomial/multinomial_aten_kernels.cc`/GetRngUsage(7d2f485495068561).'
  GetMultinomialFunctional: '`$anonymous_namespace_csrc/ops/multinomial/multinomial_aten_kernels.cc`/GetMultinomialFunctional(30e38414d1badfd0).'
  GetOutputDimensions: '`$anonymous_namespace_csrc/ops/multinomial/multinomial_aten_kernels.cc`/GetOutputDimensions(3758c68a339ded85).'
---
# Module: [`csrc/ops/multinomial/multinomial_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/multinomial/multinomial_aten_kernels.cc)

## Functions
- <a id="AtenMultinomial"></a>`AtenMultinomial(const at::Tensor& self, int64_t num_samples, bool replacement, c10::optional<at::Generator> generator)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/multinomial/multinomial_aten_kernels.cc#L100)
- <a id="AtenMultinomialOut"></a>`AtenMultinomialOut(const at::Tensor& self, int64_t num_samples, bool replacement, c10::optional<at::Generator> generator, at::Tensor& out)` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/ops/multinomial/multinomial_aten_kernels.cc#L130)
- <a id="GetMultinomialFunctional"></a>`GetMultinomialFunctional(int64_t num_samples, bool replacement)` — [`L88`](../../../../../../../raw/code/torch_tpu/csrc/ops/multinomial/multinomial_aten_kernels.cc#L88)
- `GetMultinomialFunctional(int64_t num_samples, bool replacement)` — [`L88`](../../../../../../../raw/code/torch_tpu/csrc/ops/multinomial/multinomial_aten_kernels.cc#L88)
- <a id="GetOutputDimensions"></a>`GetOutputDimensions(const at::Tensor& self, int64_t num_samples)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/multinomial/multinomial_aten_kernels.cc#L49)
- <a id="GetRngUsage"></a>`GetRngUsage(const at::Tensor& self, int64_t num_samples, bool replacement)` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/ops/multinomial/multinomial_aten_kernels.cc#L77)
- <a id="ValidateInputs"></a>`ValidateInputs(const at::Tensor& self, int64_t num_samples, bool replacement)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/multinomial/multinomial_aten_kernels.cc#L54)

