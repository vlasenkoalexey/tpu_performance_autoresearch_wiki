---
title: 'Module: csrc/ops/softmax/softmax_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/softmax/softmax_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  SoftmaxBackwardDataInternalOut: '`$anonymous_namespace_csrc/ops/softmax/softmax_aten_kernels.cc`/SoftmaxBackwardDataInternalOut(8ad6a46571a9b2e3).'
  AtenLogSoftmaxBackwardDataOut: AtenLogSoftmaxBackwardDataOut(26d14c5c4bb8cf1e).
  AtenSoftmaxOut: AtenSoftmaxOut(d2726ba75db4162d).
  AtenSoftmaxBackwardDataOut: AtenSoftmaxBackwardDataOut(26d14c5c4bb8cf1e).
  AtenLogSoftmaxOut: AtenLogSoftmaxOut(d2726ba75db4162d).
  SoftmaxInternalOut: '`$anonymous_namespace_csrc/ops/softmax/softmax_aten_kernels.cc`/SoftmaxInternalOut(22fd99e34646787f).'
  GetComputationDType: '`$anonymous_namespace_csrc/ops/softmax/softmax_aten_kernels.cc`/GetComputationDType(994972f8ba8e72d6).'
  GetSoftmaxBackwardDataFunctional: '`$anonymous_namespace_csrc/ops/softmax/softmax_aten_kernels.cc`/GetSoftmaxBackwardDataFunctional(55d1bb2569a91790).'
  GetSoftmaxFunctional: '`$anonymous_namespace_csrc/ops/softmax/softmax_aten_kernels.cc`/GetSoftmaxFunctional(db58a2cc8bf9ac36).'
---
# Module: [`csrc/ops/softmax/softmax_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax_aten_kernels.cc)

## Functions
- <a id="AtenLogSoftmaxBackwardDataOut"></a>`AtenLogSoftmaxBackwardDataOut(const at::Tensor& grad_output, const at::Tensor& output, int64_t dim, at::ScalarType input_dtype, at::Tensor& grad_input)` — [`L179`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax_aten_kernels.cc#L179)
- <a id="AtenLogSoftmaxOut"></a>`AtenLogSoftmaxOut(const at::Tensor& self, int64_t dim, bool half_to_float, at::Tensor& out)` — [`L155`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax_aten_kernels.cc#L155)
- <a id="AtenSoftmaxBackwardDataOut"></a>`AtenSoftmaxBackwardDataOut(const at::Tensor& grad_output, const at::Tensor& output, int64_t dim, at::ScalarType input_dtype, at::Tensor& grad_input)` — [`L166`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax_aten_kernels.cc#L166)
- <a id="AtenSoftmaxOut"></a>`AtenSoftmaxOut(const at::Tensor& self, int64_t dim, bool half_to_float, at::Tensor& out)` — [`L145`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax_aten_kernels.cc#L145)
- <a id="GetComputationDType"></a>`GetComputationDType(const at::Tensor& self, bool half_to_float)` — [`L65`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax_aten_kernels.cc#L65)
- `GetSoftmaxBackwardDataFunctional(int64_t dim, SoftmaxMode softmax_mode, mlir::stablehlo::Precision precision)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax_aten_kernels.cc#L54)
- <a id="GetSoftmaxBackwardDataFunctional"></a>`GetSoftmaxBackwardDataFunctional(int64_t dim, SoftmaxMode softmax_mode, mlir::stablehlo::Precision precision)` — [`L54`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax_aten_kernels.cc#L54)
- <a id="GetSoftmaxFunctional"></a>`GetSoftmaxFunctional(int64_t dim, SoftmaxMode softmax_mode)` — [`L48`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax_aten_kernels.cc#L48)
- <a id="SoftmaxBackwardDataInternalOut"></a>`SoftmaxBackwardDataInternalOut(const at::Tensor& grad_output, const at::Tensor& output, int64_t dim, at::ScalarType input_dtype, SoftmaxMode softmax_mode, at::Tensor& grad_input, OpParamCacheKeys param_keys)` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax_aten_kernels.cc#L109)
- <a id="SoftmaxInternalOut"></a>`SoftmaxInternalOut(const at::Tensor& self, int64_t dim, bool half_to_float, SoftmaxMode softmax_mode, at::Tensor& out, OpParamCacheKeys param_keys)` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/ops/softmax/softmax_aten_kernels.cc#L77)

