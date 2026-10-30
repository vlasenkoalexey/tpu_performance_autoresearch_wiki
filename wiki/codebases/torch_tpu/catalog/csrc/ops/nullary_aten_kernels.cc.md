---
title: 'Module: csrc/ops/nullary_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/nullary_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenEfficientZeroTensor: AtenEfficientZeroTensor(b1bc70646752fa00).
  AtenEmptyStrided: AtenEmptyStrided(730ca7d668b9f363).
  ApplyNullaryOpOut: ApplyNullaryOpOut(fca2e3a91dac76ff).
  AtenEmptyMemoryFormat: AtenEmptyMemoryFormat(357680b8bbd706b8).
  ApplyNullaryOp: ApplyNullaryOp(34a7fb565d0b0bfb).
---
# Module: [`csrc/ops/nullary_aten_kernels.cc`](../../../../../../raw/code/torch_tpu/csrc/ops/nullary_aten_kernels.cc)

## Functions
- <a id="ApplyNullaryOp"></a>`ApplyNullaryOp(MlirNullaryOpBuilder op_builder, c10::ScalarType out_dtype, at::IntArrayRef out_dims, OpParamCacheKeys op_param_cache_keys, OpSplitMode split_mode)` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/ops/nullary_aten_kernels.cc#L56)
- <a id="ApplyNullaryOpOut"></a>`ApplyNullaryOpOut(at::Tensor& out, MlirNullaryOpBuilder op_builder, c10::ScalarType out_dtype, at::IntArrayRef out_dims, OpParamCacheKeys op_param_cache_keys, OpSplitMode split_mode)` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/ops/nullary_aten_kernels.cc#L75)
- <a id="AtenEfficientZeroTensor"></a>`AtenEfficientZeroTensor(at::IntArrayRef size, c10::optional<at::ScalarType> dtype_opt, c10::optional<at::Layout> layout_opt, c10::optional<at::Device> device_opt, c10::optional<bool> pin_memory_opt)` — [`L192`](../../../../../../raw/code/torch_tpu/csrc/ops/nullary_aten_kernels.cc#L192)
- <a id="AtenEmptyMemoryFormat"></a>`AtenEmptyMemoryFormat(at::IntArrayRef size, c10::optional<at::ScalarType> dtype_opt, c10::optional<at::Layout> layout_opt, c10::optional<at::Device> device_opt, c10::optional<bool> pin_memory_opt, c10::optional<at::MemoryFormat> memory_format_opt)` — [`L106`](../../../../../../raw/code/torch_tpu/csrc/ops/nullary_aten_kernels.cc#L106)
- <a id="AtenEmptyStrided"></a>`AtenEmptyStrided(c10::SymIntArrayRef size_sym, c10::SymIntArrayRef stride_sym, c10::optional<at::ScalarType> dtype_opt, c10::optional<at::Layout> layout_opt, c10::optional<at::Device> device_opt, c10::optional<bool> pin_memory_opt)` — [`L127`](../../../../../../raw/code/torch_tpu/csrc/ops/nullary_aten_kernels.cc#L127)

