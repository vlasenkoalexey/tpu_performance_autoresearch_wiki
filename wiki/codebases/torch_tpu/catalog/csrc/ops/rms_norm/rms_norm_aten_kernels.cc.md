---
title: 'Module: csrc/ops/rms_norm/rms_norm_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/rms_norm/rms_norm_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenRmsNorm: AtenRmsNorm(5dbe13ef8b9bcda).
  AtenFusedRmsNorm: AtenFusedRmsNorm(26d476beb7421e6c).
  AtenFusedRmsNormBackward: AtenFusedRmsNormBackward(1a62cd8f0d7c5081).
  ValidateRmsNormInputs: '`$anonymous_namespace_csrc/ops/rms_norm/rms_norm_aten_kernels.cc`/ValidateRmsNormInputs(97f4b8583802111f).'
  ValidateRmsNormInputsOrThrow: '`$anonymous_namespace_csrc/ops/rms_norm/rms_norm_aten_kernels.cc`/ValidateRmsNormInputsOrThrow(962e51a4c6edaf4a).'
  AtenRmsNormAutograd: AtenRmsNormAutograd(5dbe13ef8b9bcda).
  GetRmsNormEpsilon: '`$anonymous_namespace_csrc/ops/rms_norm/rms_norm_aten_kernels.cc`/GetRmsNormEpsilon(736e63ae44a94a66).'
  DelegateRmsNormFakeOrFunctorch: '`$anonymous_namespace_csrc/ops/rms_norm/rms_norm_aten_kernels.cc`/DelegateRmsNormFakeOrFunctorch(35393b8b5b3e0b7a).'
  RmsNormComposite: '`$anonymous_namespace_csrc/ops/rms_norm/rms_norm_aten_kernels.cc`/RmsNormComposite(5dbe13ef8b9bcda).'
  IsFakeOrFunctorchTensor: '`$anonymous_namespace_csrc/ops/rms_norm/rms_norm_aten_kernels.cc`/IsFakeOrFunctorchTensor(b580d0b7e29ca914).'
---
# Module: [`csrc/ops/rms_norm/rms_norm_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm_aten_kernels.cc)

## Functions
- <a id="AtenFusedRmsNorm"></a>`AtenFusedRmsNorm(const at::Tensor& input, at::IntArrayRef normalized_shape, const std::optional<at::Tensor>& weight, std::optional<double> eps)` — [`L312`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm_aten_kernels.cc#L312)
- <a id="AtenFusedRmsNormBackward"></a>`AtenFusedRmsNormBackward(const at::Tensor& grad_out, const at::Tensor& input, at::IntArrayRef normalized_shape, const at::Tensor& rstd, const std::optional<at::Tensor>& weight, std::array<bool, 2> output_mask)` — [`L405`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm_aten_kernels.cc#L405)
- <a id="AtenRmsNorm"></a>`AtenRmsNorm(const at::Tensor& input, at::IntArrayRef normalized_shape, const std::optional<at::Tensor>& weight, std::optional<double> eps)` — [`L205`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm_aten_kernels.cc#L205)
- <a id="AtenRmsNormAutograd"></a>`AtenRmsNormAutograd(const at::Tensor& input, at::IntArrayRef normalized_shape, const std::optional<at::Tensor>& weight, std::optional<double> eps)` — [`L274`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm_aten_kernels.cc#L274)
- <a id="DelegateRmsNormFakeOrFunctorch"></a>`DelegateRmsNormFakeOrFunctorch(const at::Tensor& input, at::IntArrayRef normalized_shape, const std::optional<at::Tensor>& weight, std::optional<double> eps, bool any_has_fw_grad)` — [`L190`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm_aten_kernels.cc#L190)
- <a id="GetRmsNormEpsilon"></a>`GetRmsNormEpsilon(std::optional<double> eps, c10::ScalarType input_dtype)` — [`L69`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm_aten_kernels.cc#L69)
- <a id="IsFakeOrFunctorchTensor"></a>`IsFakeOrFunctorchTensor(const at::Tensor& tensor)` — [`L138`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm_aten_kernels.cc#L138)
- <a id="RmsNormComposite"></a>`RmsNormComposite(const at::Tensor& input, at::IntArrayRef normalized_shape, const std::optional<at::Tensor>& weight, std::optional<double> eps)` — [`L154`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm_aten_kernels.cc#L154) — Composite fallback using TORCH_API-exported ATen ops for FakeTensor
- <a id="ValidateRmsNormInputs"></a>`ValidateRmsNormInputs(const at::Tensor& input, at::IntArrayRef normalized_shape, const std::optional<at::Tensor>& weight)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm_aten_kernels.cc#L80)
- <a id="ValidateRmsNormInputsOrThrow"></a>`ValidateRmsNormInputsOrThrow(const at::Tensor& input, at::IntArrayRef normalized_shape, const std::optional<at::Tensor>& weight)` — [`L127`](../../../../../../../raw/code/torch_tpu/csrc/ops/rms_norm/rms_norm_aten_kernels.cc#L127)

