---
title: 'Module: csrc/ops/dropout/dropout_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/dropout/dropout_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenNativeDropoutBackward: AtenNativeDropoutBackward(d576f26a894a8fe6).
  AtenDropoutCommonImpl: '`$anonymous_namespace_csrc/ops/dropout/dropout_aten_kernels.cc`/AtenDropoutCommonImpl(597383183c0b574c).'
  AtenDropout: AtenDropout(4ef8c25e4b1fcd4).
  AtenFusedDropout: AtenFusedDropout(db27a03b65bf3810).
  GetDropoutFunctional: '`$anonymous_namespace_csrc/ops/dropout/dropout_aten_kernels.cc`/GetDropoutFunctional(780a064ba7354c7a).'
  GetDropoutBackwardFunctional: '`$anonymous_namespace_csrc/ops/dropout/dropout_aten_kernels.cc`/GetDropoutBackwardFunctional(d51f491be7bf135e).'
---
# Module: [`csrc/ops/dropout/dropout_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout_aten_kernels.cc)

## Functions
- <a id="AtenDropout"></a>`AtenDropout(const at::Tensor& input, double p, c10::optional<bool> train)` — [`L145`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout_aten_kernels.cc#L145)
- <a id="AtenDropoutCommonImpl"></a>`AtenDropoutCommonImpl(const at::Tensor& input, double p, bool train, c10::optional<at::Generator> generator, OpParamCacheKeys param_keys)` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout_aten_kernels.cc#L72) — Common helper function for forward dropout operations (AtenDropout and
- <a id="AtenFusedDropout"></a>`AtenFusedDropout(const at::Tensor& self, double p, c10::optional<at::Generator> generator)` — [`L155`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout_aten_kernels.cc#L155)
- <a id="AtenNativeDropoutBackward"></a>`AtenNativeDropoutBackward(const at::Tensor& grad_output, const at::Tensor& mask, double scale)` — [`L175`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout_aten_kernels.cc#L175)
- `GetDropoutBackwardFunctional(double scale)` — [`L165`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout_aten_kernels.cc#L165)
- <a id="GetDropoutBackwardFunctional"></a>`GetDropoutBackwardFunctional(double scale)` — [`L165`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout_aten_kernels.cc#L165)
- `GetDropoutFunctional(const at::Tensor& input, double p)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout_aten_kernels.cc#L59) — Builds the SHLO for dropout in the train mode.
- <a id="GetDropoutFunctional"></a>`GetDropoutFunctional(const at::Tensor& input, double p)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/dropout/dropout_aten_kernels.cc#L59) — Builds the SHLO for dropout in the train mode.

