---
title: 'Module: csrc/ops/layer_norm/layer_norm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/layer_norm/layer_norm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenNativeLayerNorm: AtenNativeLayerNorm(1bbd880b828c048d).
  AtenLayerNormBackward: AtenLayerNormBackward(b50d8f37b0bf0935).
  ValidateInputs: '`$anonymous_namespace_csrc/ops/layer_norm/layer_norm_aten_kernels.cc`/ValidateInputs(acaaaa651dcb7b51).'
---
# Module: [`csrc/ops/layer_norm/layer_norm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm_aten_kernels.cc)

## Functions
- <a id="AtenLayerNormBackward"></a>`AtenLayerNormBackward(const at::Tensor& dY, const at::Tensor& input, at::IntArrayRef normalized_shape, const at::Tensor& mean, const at::Tensor& rstd, const std::optional<at::Tensor>& weight_opt, const std::optional<at::Tensor>& bias_opt, std::array<bool, 3> grad_input_mask)` — [`L170`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm_aten_kernels.cc#L170)
- <a id="AtenNativeLayerNorm"></a>`AtenNativeLayerNorm(const at::Tensor& input, const at::IntArrayRef normalized_shape, const c10::optional<at::Tensor>& weight_opt, const c10::optional<at::Tensor>& bias_opt, const double eps)` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm_aten_kernels.cc#L72)
- <a id="ValidateInputs"></a>`ValidateInputs(const at::Tensor& input, const at::IntArrayRef normalized_shape)` — [`L53`](../../../../../../../raw/code/torch_tpu/csrc/ops/layer_norm/layer_norm_aten_kernels.cc#L53)

