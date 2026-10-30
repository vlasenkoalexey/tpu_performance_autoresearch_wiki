---
title: 'Module: csrc/ops/convolution/convolution_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/convolution/convolution_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenConvolution: AtenConvolution(5081f0b50c95bd63).
  AtenConvolutionOut: AtenConvolutionOut(30b06ed9437d527a).
  AtenConvolutionBackward: AtenConvolutionBackward(e545f387b2556f8d).
  ConvolutionBackward: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ConvolutionBackward(9e6b45a57c838d4f).'
  PrepareConvolutionDispatch: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/PrepareConvolutionDispatch(b48b27b74cba1770).'
  ConvolutionTernaryOut: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ConvolutionTernaryOut(cacc22b7a44e9597).'
  ConvolutionBinaryOut: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ConvolutionBinaryOut(eea678cc41c63d48).'
  GetPromotedType: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/GetPromotedType(d31afbc8afbfda08).'
  IsTypeSupported: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/IsTypeSupported(d8359b99282c084c).'
  ConvolutionOut: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ConvolutionOut(fbfaf215aa9ad6a0).'
  ValidateConvolutionInputs: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ValidateConvolutionInputs(c1ba541b67561c4b).'
  GetPromotedTypeBackward: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/GetPromotedTypeBackward(c895b2c054e47339).'
  ExpandIfNecessary: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ExpandIfNecessary(52b9a17ab31e7e74).'
  GetOutputDimensions: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/GetOutputDimensions(2d904964f5f07be8).'
  ConvolutionDispatchParams.output_dims: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ConvolutionDispatchParams#output_dims.'
  ConvolutionDispatchParams.current_precision: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ConvolutionDispatchParams#current_precision.'
  ConvolutionDispatchParams.expanded_dilation: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ConvolutionDispatchParams#expanded_dilation.'
  ConvolutionDispatchParams.expanded_padding: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ConvolutionDispatchParams#expanded_padding.'
  ConvolutionDispatchParams: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ConvolutionDispatchParams#'
  ConvolutionDispatchParams.mlir_dtype: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ConvolutionDispatchParams#mlir_dtype.'
  ConvolutionDispatchParams.expanded_output_padding: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ConvolutionDispatchParams#expanded_output_padding.'
  ConvolutionDispatchParams.expanded_stride: '`$anonymous_namespace_csrc/ops/convolution/convolution_aten_kernels.cc`/ConvolutionDispatchParams#expanded_stride.'
---
# Module: [`csrc/ops/convolution/convolution_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc)

## Classes
### <a id="ConvolutionDispatchParams"></a>`ConvolutionDispatchParams`
- def: [`csrc/ops/convolution/convolution_aten_kernels.cc:201`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L201)
- signature: `struct ConvolutionDispatchParams`
- members:
  - <a id="ConvolutionDispatchParams.current_precision"></a>`current_precision` — [`L208`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L208)
  - <a id="ConvolutionDispatchParams.expanded_dilation"></a>`expanded_dilation` — [`L204`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L204)
  - <a id="ConvolutionDispatchParams.expanded_output_padding"></a>`expanded_output_padding` — [`L205`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L205)
  - <a id="ConvolutionDispatchParams.expanded_padding"></a>`expanded_padding` — [`L203`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L203)
  - <a id="ConvolutionDispatchParams.expanded_stride"></a>`expanded_stride` — [`L202`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L202)
  - <a id="ConvolutionDispatchParams.mlir_dtype"></a>`mlir_dtype` — [`L207`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L207)
  - <a id="ConvolutionDispatchParams.output_dims"></a>`output_dims` — [`L206`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L206)
- uses (calls/refs, reference-scoped): [`Dimensions`](../../common/dimension_types.h.md#Dimensions)
- used by: [`PrepareConvolutionDispatch`](convolution_aten_kernels.cc.md#PrepareConvolutionDispatch), [`ConvolutionBinaryOut`](convolution_aten_kernels.cc.md#ConvolutionBinaryOut), [`ConvolutionTernaryOut`](convolution_aten_kernels.cc.md#ConvolutionTernaryOut)

## Functions
- <a id="AtenConvolution"></a>`AtenConvolution(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias_opt, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool transposed, at::IntArrayRef output_padding, int64_t groups)` — [`L463`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L463) — at::convolution
- <a id="AtenConvolutionBackward"></a>`AtenConvolutionBackward(const at::Tensor& grad_output, const at::Tensor& input, const at::Tensor& weight, at::OptionalIntArrayRef bias_sizes, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool transposed, at::IntArrayRef output_padding, int64_t groups, std::array<bool, 3> output_mask)` — [`L508`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L508) — at::convolution_backward
- <a id="AtenConvolutionOut"></a>`AtenConvolutionOut(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias_opt, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool transposed, at::IntArrayRef output_padding, int64_t groups, at::Tensor& out)` — [`L489`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L489) — at::convolution.out
- `ConvolutionBackward(const at::Tensor& grad_output, const at::Tensor& input, const at::Tensor& weight, at::OptionalIntArrayRef bias_sizes, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool transposed, at::IntArrayRef output_padding, int64_t groups, std::array<bool, 3> output_mask, OpParamCacheKeys param_keys)` — [`L360`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L360)
- <a id="ConvolutionBackward"></a>`ConvolutionBackward(const at::Tensor& grad_output, const at::Tensor& input, const at::Tensor& weight, at::OptionalIntArrayRef bias_sizes, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool transposed, at::IntArrayRef output_padding, int64_t groups, std::array<bool, 3> output_mask, OpParamCacheKeys param_keys)` — [`L360`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L360)
- <a id="ConvolutionBinaryOut"></a>`ConvolutionBinaryOut(const at::Tensor& input, const at::Tensor& weight, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool transposed, at::IntArrayRef output_padding, int64_t groups, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L249`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L249)
- <a id="ConvolutionOut"></a>`ConvolutionOut(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias_opt, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool transposed, at::IntArrayRef output_padding, int64_t groups, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L332`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L332)
- <a id="ConvolutionTernaryOut"></a>`ConvolutionTernaryOut(const at::Tensor& input, const at::Tensor& weight, const at::Tensor& bias, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool transposed, at::IntArrayRef output_padding, int64_t groups, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L291`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L291)
- <a id="ExpandIfNecessary"></a>`ExpandIfNecessary(at::IntArrayRef param, int num_spatial_dims)` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L74) — This helper function handles PyTorch's parameter broadcasting for
- <a id="GetOutputDimensions"></a>`GetOutputDimensions(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias_opt, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, bool transposed, absl::Span<const int64_t> output_padding, int64_t groups)` — [`L125`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L125)
- <a id="GetPromotedType"></a>`GetPromotedType(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias_opt)` — [`L176`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L176)
- <a id="GetPromotedTypeBackward"></a>`GetPromotedTypeBackward(const at::Tensor& grad_output, const at::Tensor& input, const at::Tensor& weight)` — [`L349`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L349)
- <a id="IsTypeSupported"></a>`IsTypeSupported(const at::Tensor& tensor, const std::string_view arg_name)` — [`L167`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L167)
- <a id="PrepareConvolutionDispatch"></a>`PrepareConvolutionDispatch(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias_opt, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool transposed, at::IntArrayRef output_padding, int64_t groups, OpParamCacheKeys& param_keys)` — [`L211`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L211)
- <a id="ValidateConvolutionInputs"></a>`ValidateConvolutionInputs(const at::Tensor& input, const at::Tensor& weight, absl::Span<const int64_t> bias, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, bool transposed, absl::Span<const int64_t> output_padding, int64_t groups)` — [`L81`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L81)
- `ValidateConvolutionInputs(const at::Tensor& input, const at::Tensor& weight, const std::optional<at::Tensor>& bias_opt, absl::Span<const int64_t> stride, absl::Span<const int64_t> padding, absl::Span<const int64_t> dilation, bool transposed, absl::Span<const int64_t> output_padding, int64_t groups)` — [`L113`](../../../../../../../raw/code/torch_tpu/csrc/ops/convolution/convolution_aten_kernels.cc#L113)

