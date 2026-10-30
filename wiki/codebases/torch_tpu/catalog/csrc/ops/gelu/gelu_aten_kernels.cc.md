---
title: 'Module: csrc/ops/gelu/gelu_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/gelu/gelu_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenGeluBackwardGradInput: AtenGeluBackwardGradInput(8388c8daf3c363e6).
  AtenGeluOut: AtenGeluOut(3b23420f629115cf).
  AtenGelu: AtenGelu(dbb2153b688a06b).
  GetGeluFunctional: '`$anonymous_namespace_csrc/ops/gelu/gelu_aten_kernels.cc`/GetGeluFunctional(5b7aa9a35c51ad39).'
---
# Module: [`csrc/ops/gelu/gelu_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/gelu/gelu_aten_kernels.cc)

## Functions
- <a id="AtenGelu"></a>`AtenGelu(const at::Tensor& self, c10::string_view approximate)` — [`L55`](../../../../../../../raw/code/torch_tpu/csrc/ops/gelu/gelu_aten_kernels.cc#L55)
- <a id="AtenGeluBackwardGradInput"></a>`AtenGeluBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, c10::string_view approximate, at::Tensor& grad_input)` — [`L102`](../../../../../../../raw/code/torch_tpu/csrc/ops/gelu/gelu_aten_kernels.cc#L102)
- <a id="AtenGeluOut"></a>`AtenGeluOut(const at::Tensor& self, c10::string_view approximate, at::Tensor& out)` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/gelu/gelu_aten_kernels.cc#L78)
- <a id="GetGeluFunctional"></a>`GetGeluFunctional(c10::string_view approximate, mlir::ElementType output_dtype)` — [`L45`](../../../../../../../raw/code/torch_tpu/csrc/ops/gelu/gelu_aten_kernels.cc#L45)

