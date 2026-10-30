---
title: 'Module: csrc/ops/col2im/col2im_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/col2im/col2im_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenCol2ImOut: AtenCol2ImOut(bf7fd02ae0557710).
  AtenCol2Im: AtenCol2Im(b6e4b409e345b95c).
  ComputeOutputSize: '`$anonymous_namespace_csrc/ops/col2im/col2im_aten_kernels.cc`/ComputeOutputSize(f26d823a32f0204f).'
  GetOutputDimensions: '`$anonymous_namespace_csrc/ops/col2im/col2im_aten_kernels.cc`/GetOutputDimensions(f350fcdcafcc9a70).'
---
# Module: [`csrc/ops/col2im/col2im_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/col2im/col2im_aten_kernels.cc)

## Functions
- <a id="AtenCol2Im"></a>`AtenCol2Im(const at::Tensor& input, at::IntArrayRef output_size, at::IntArrayRef kernel_size, at::IntArrayRef dilation, at::IntArrayRef padding, at::IntArrayRef stride)` — [`L169`](../../../../../../../raw/code/torch_tpu/csrc/ops/col2im/col2im_aten_kernels.cc#L169)
- `AtenCol2Im(const at::Tensor& input, at::IntArrayRef output_size, at::IntArrayRef kernel_size, at::IntArrayRef dilation, at::IntArrayRef padding, at::IntArrayRef stride, OpParamCacheKeys param_keys)` — [`L134`](../../../../../../../raw/code/torch_tpu/csrc/ops/col2im/col2im_aten_kernels.cc#L134)
- <a id="AtenCol2ImOut"></a>`AtenCol2ImOut(const at::Tensor& input, at::IntArrayRef output_size, at::IntArrayRef kernel_size, at::IntArrayRef dilation, at::IntArrayRef padding, at::IntArrayRef stride, at::Tensor& out)` — [`L182`](../../../../../../../raw/code/torch_tpu/csrc/ops/col2im/col2im_aten_kernels.cc#L182)
- <a id="ComputeOutputSize"></a>`ComputeOutputSize(at::IntArrayRef input_size, at::IntArrayRef padding, at::IntArrayRef dilation, at::IntArrayRef kernel_size, at::IntArrayRef stride)` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/col2im/col2im_aten_kernels.cc#L48) — Returns the number of blocks to slide over the input tensor.
- <a id="GetOutputDimensions"></a>`GetOutputDimensions(const at::Tensor& input, at::IntArrayRef output_size, at::IntArrayRef kernel_size, at::IntArrayRef dilation, at::IntArrayRef padding, at::IntArrayRef stride)` — [`L74`](../../../../../../../raw/code/torch_tpu/csrc/ops/col2im/col2im_aten_kernels.cc#L74) — Returns the output dimensions for a col2im operation, and validates

