---
title: 'Module: csrc/ops/softmax/_masked_softmax_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/softmax/_masked_softmax_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenMaskedSoftmax: AtenMaskedSoftmax(43747c020ae61c12).
  AtenMaskedSoftmaxBackward: AtenMaskedSoftmaxBackward(bb78a4f39ba303ce).
  AtenMaskedSoftmaxBackwardOut: AtenMaskedSoftmaxBackwardOut(c140091bf65199ec).
  AtenMaskedSoftmaxOut: AtenMaskedSoftmaxOut(e29881c7346a2785).
  ValidateMaskedSoftmaxInputs: '`$anonymous_namespace_csrc/ops/softmax/_masked_softmax_aten_kernels.cc`/ValidateMaskedSoftmaxInputs(e23ac55e597fa859).'
  ValidateMaskedSoftmaxBackwardInputs: '`$anonymous_namespace_csrc/ops/softmax/_masked_softmax_aten_kernels.cc`/ValidateMaskedSoftmaxBackwardInputs(6ddad2e2cbb424ad).'
  MaskedSoftmaxBackwardInternalOut: '`$anonymous_namespace_csrc/ops/softmax/_masked_softmax_aten_kernels.cc`/MaskedSoftmaxBackwardInternalOut(cac8783ef3777009).'
  MaskedSoftmaxInternalOut: '`$anonymous_namespace_csrc/ops/softmax/_masked_softmax_aten_kernels.cc`/MaskedSoftmaxInternalOut(a9d7adb8fe046572).'
---
# Module: [`csrc/ops/softmax/_masked_softmax_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/_masked_softmax_aten_kernels.cc)

## Functions
- <a id="AtenMaskedSoftmax"></a>`AtenMaskedSoftmax(const at::Tensor& self, const at::Tensor& mask, std::optional<int64_t> dim, std::optional<int64_t> mask_type)` — [`L231`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/_masked_softmax_aten_kernels.cc#L231)
- <a id="AtenMaskedSoftmaxBackward"></a>`AtenMaskedSoftmaxBackward(const at::Tensor& grad_output, const at::Tensor& output, const at::Tensor& mask, std::optional<int64_t> dim)` — [`L256`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/_masked_softmax_aten_kernels.cc#L256)
- <a id="AtenMaskedSoftmaxBackwardOut"></a>`AtenMaskedSoftmaxBackwardOut(const at::Tensor& grad_output, const at::Tensor& output, const at::Tensor& mask, std::optional<int64_t> dim, at::Tensor& grad_input)` — [`L272`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/_masked_softmax_aten_kernels.cc#L272)
- <a id="AtenMaskedSoftmaxOut"></a>`AtenMaskedSoftmaxOut(const at::Tensor& self, const at::Tensor& mask, std::optional<int64_t> dim, std::optional<int64_t> mask_type, at::Tensor& out)` — [`L244`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/_masked_softmax_aten_kernels.cc#L244)
- <a id="MaskedSoftmaxBackwardInternalOut"></a>`MaskedSoftmaxBackwardInternalOut(const at::Tensor& grad_output, const at::Tensor& output, const at::Tensor& mask, std::optional<int64_t> dim, at::Tensor& grad_input, OpParamCacheKeys param_keys)` — [`L189`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/_masked_softmax_aten_kernels.cc#L189)
- <a id="MaskedSoftmaxInternalOut"></a>`MaskedSoftmaxInternalOut(const at::Tensor& self, const at::Tensor& mask, std::optional<int64_t> dim, std::optional<int64_t> mask_type, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L150`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/_masked_softmax_aten_kernels.cc#L150)
- <a id="ValidateMaskedSoftmaxBackwardInputs"></a>`ValidateMaskedSoftmaxBackwardInputs(const at::Tensor& grad_output, const at::Tensor& output, const at::Tensor& mask)` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/_masked_softmax_aten_kernels.cc#L116)
- <a id="ValidateMaskedSoftmaxInputs"></a>`ValidateMaskedSoftmaxInputs(const at::Tensor& self, const at::Tensor& mask, std::optional<int64_t> mask_type)` — [`L46`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/_masked_softmax_aten_kernels.cc#L46)

