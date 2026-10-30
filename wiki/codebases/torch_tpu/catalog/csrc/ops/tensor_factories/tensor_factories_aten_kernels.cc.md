---
title: 'Module: csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  CreateScalarFilledTensor: '`$anonymous_namespace_csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc`/CreateScalarFilledTensor(1de7bdcb86680681).'
  AtenFullLike: AtenFullLike(a9301164b2bc7e08).
  AtenZerosLike: AtenZerosLike(f6172c4a7f8fcb3a).
  AtenOnesLike: AtenOnesLike(f6172c4a7f8fcb3a).
  AtenNewFull: AtenNewFull(21034997483f66ae).
  AtenFull: AtenFull(5a7cedb090ce6317).
  AtenNewZeros: AtenNewZeros(acea1d81df47886b).
  AtenNewOnes: AtenNewOnes(acea1d81df47886b).
  AtenOnes: AtenOnes(b1bc70646752fa00).
  AtenZeros: AtenZeros(b1bc70646752fa00).
  ValidateFactoryOptions: '`$anonymous_namespace_csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc`/ValidateFactoryOptions(7aa45068e2e7059e).'
  CreateConstantFilledTensor: '`$anonymous_namespace_csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc`/CreateConstantFilledTensor(d00ad1e2acbdf166).'
  ValidateLikeMemoryFormat: '`$anonymous_namespace_csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc`/ValidateLikeMemoryFormat(96a6cf09de4a2d).'
  ResolveFullOutputDtype: '`$anonymous_namespace_csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc`/ResolveFullOutputDtype(fca1b846b7cf968f).'
  ApplyLikeTensorRestride: '`$anonymous_namespace_csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc`/ApplyLikeTensorRestride(6fa9309bab2204b2).'
---
# Module: [`csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc)

## Functions
- <a id="ApplyLikeTensorRestride"></a>`ApplyLikeTensorRestride(at::Tensor& result, const at::Tensor& self, at::MemoryFormat memory_format)` — [`L100`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L100)
- <a id="AtenFull"></a>`AtenFull(at::IntArrayRef size, const at::Scalar& fill_value, std::optional<at::ScalarType> dtype_opt, std::optional<at::Layout> layout_opt, std::optional<at::Device> device_opt, std::optional<bool> pin_memory_opt)` — [`L237`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L237)
- <a id="AtenFullLike"></a>`AtenFullLike(const at::Tensor& self, const at::Scalar& fill_value, std::optional<at::ScalarType> dtype_opt, std::optional<at::Layout> layout_opt, std::optional<at::Device> device_opt, std::optional<bool> pin_memory_opt, std::optional<at::MemoryFormat> memory_format_opt)` — [`L329`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L329)
- <a id="AtenNewFull"></a>`AtenNewFull(const at::Tensor& self, at::IntArrayRef size, const at::Scalar& fill_value, std::optional<at::ScalarType> dtype_opt, std::optional<at::Layout> layout_opt, std::optional<at::Device> device_opt, std::optional<bool> pin_memory_opt)` — [`L420`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L420)
- <a id="AtenNewOnes"></a>`AtenNewOnes(const at::Tensor& self, at::IntArrayRef size, std::optional<at::ScalarType> dtype_opt, std::optional<at::Layout> layout_opt, std::optional<at::Device> device_opt, std::optional<bool> pin_memory_opt)` — [`L393`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L393)
- <a id="AtenNewZeros"></a>`AtenNewZeros(const at::Tensor& self, at::IntArrayRef size, std::optional<at::ScalarType> dtype_opt, std::optional<at::Layout> layout_opt, std::optional<at::Device> device_opt, std::optional<bool> pin_memory_opt)` — [`L366`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L366)
- <a id="AtenOnes"></a>`AtenOnes(at::IntArrayRef size, std::optional<at::ScalarType> dtype_opt, std::optional<at::Layout> layout_opt, std::optional<at::Device> device_opt, std::optional<bool> pin_memory_opt)` — [`L217`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L217)
- <a id="AtenOnesLike"></a>`AtenOnesLike(const at::Tensor& self, std::optional<at::ScalarType> dtype_opt, std::optional<at::Layout> layout_opt, std::optional<at::Device> device_opt, std::optional<bool> pin_memory_opt, std::optional<at::MemoryFormat> memory_format_opt)` — [`L296`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L296)
- <a id="AtenZeros"></a>`AtenZeros(at::IntArrayRef size, std::optional<at::ScalarType> dtype_opt, std::optional<at::Layout> layout_opt, std::optional<at::Device> device_opt, std::optional<bool> pin_memory_opt)` — [`L197`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L197)
- <a id="AtenZerosLike"></a>`AtenZerosLike(const at::Tensor& self, std::optional<at::ScalarType> dtype_opt, std::optional<at::Layout> layout_opt, std::optional<at::Device> device_opt, std::optional<bool> pin_memory_opt, std::optional<at::MemoryFormat> memory_format_opt)` — [`L263`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L263)
- <a id="CreateConstantFilledTensor"></a>`CreateConstantFilledTensor(at::IntArrayRef size, double scalar_val, at::ScalarType out_dtype, std::optional<at::Layout> layout_opt, std::optional<at::Device> device_opt, std::optional<bool> pin_memory_opt, std::string_view op_name_str)` — [`L137`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L137)
- <a id="CreateScalarFilledTensor"></a>`CreateScalarFilledTensor(at::IntArrayRef size, PromotedScalar& promoted_fill_value, at::ScalarType out_dtype, std::optional<at::Layout> layout_opt, std::optional<at::Device> device_opt, std::optional<bool> pin_memory_opt, std::string_view op_name_str, OpParamCacheKeys param_keys)` — [`L159`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L159)
- <a id="ResolveFullOutputDtype"></a>`ResolveFullOutputDtype(std::optional<at::ScalarType> dtype_opt, const PromotedScalar& promoted_fill_value)` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L116)
- <a id="ValidateFactoryOptions"></a>`ValidateFactoryOptions(at::ScalarType out_dtype, std::optional<at::Layout> layout_opt, std::optional<at::Device> device_opt, std::optional<bool> pin_memory_opt, std::string_view op_name_str)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L59)
- <a id="ValidateLikeMemoryFormat"></a>`ValidateLikeMemoryFormat(const at::Tensor& self, at::MemoryFormat memory_format)` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/tensor_factories/tensor_factories_aten_kernels.cc#L78)

