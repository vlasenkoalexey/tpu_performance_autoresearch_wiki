---
title: 'Module: csrc/ops/arange/arange_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/arange/arange_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenArangeStartOut: AtenArangeStartOut(785e5c722b1f740c).
  ValidateArangeInputs: '`$anonymous_namespace_csrc/ops/arange/arange_aten_kernels.cc`/ValidateArangeInputs(7b973bb98edb8a6).'
  GetArangeNumElements: '`$anonymous_namespace_csrc/ops/arange/arange_aten_kernels.cc`/GetArangeNumElements(b58b2fb5cc59ec1e).'
  ComputeArangeNumElements: '`$anonymous_namespace_csrc/ops/arange/arange_aten_kernels.cc`/ComputeArangeNumElements(4e0c72050fa9ccb7).'
---
# Module: [`csrc/ops/arange/arange_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/arange/arange_aten_kernels.cc)

## Functions
- <a id="AtenArangeStartOut"></a>`AtenArangeStartOut(const at::Scalar& start, const at::Scalar& end, const at::Scalar& step, at::Tensor& out)` — [`L175`](../../../../../../../raw/code/torch_tpu/csrc/ops/arange/arange_aten_kernels.cc#L175) — arange.start_out
- <a id="ComputeArangeNumElements"></a>`ComputeArangeNumElements(const at::Scalar& start, const at::Scalar& end, const at::Scalar& step, const at::ScalarType output_dtype)` — [`L109`](../../../../../../../raw/code/torch_tpu/csrc/ops/arange/arange_aten_kernels.cc#L109) — This implementation is based on the PyTorch compute_arange_size() function.
- <a id="GetArangeNumElements"></a>`GetArangeNumElements(const at::Scalar& start, const at::Scalar& end, const at::Scalar& step, const at::ScalarType output_dtype)` — [`L130`](../../../../../../../raw/code/torch_tpu/csrc/ops/arange/arange_aten_kernels.cc#L130)
- <a id="ValidateArangeInputs"></a>`ValidateArangeInputs(const RangeBound start, const RangeBound end, const double step)` — [`L68`](../../../../../../../raw/code/torch_tpu/csrc/ops/arange/arange_aten_kernels.cc#L68) — Check that the inputs are valid for the arange operation.

