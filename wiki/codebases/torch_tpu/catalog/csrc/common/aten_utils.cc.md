---
title: 'Module: csrc/common/aten_utils.cc'
type: catalog
provenance: extracted
module: csrc/common/aten_utils.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  InferOutputDtype: InferOutputDtype(8a782c978018d3d).
  operator: '`operator==`(c66407ca4e89b815).'
  InferComputationDtype: InferComputationDtype(4dad59169ac167a9).
  ToString: ToString(f639a3523e9e4913).
  CanCastScalarWithoutOverflow: CanCastScalarWithoutOverflow(168139e60c42bcfd).
---
# Module: [`csrc/common/aten_utils.cc`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.cc)

## Functions
- <a id="CanCastScalarWithoutOverflow"></a>`CanCastScalarWithoutOverflow(const at::Scalar& scalar, at::ScalarType scalar_type)` — [`L112`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.cc#L112) — Returns true if `scalar` can be cast to `scalar_type` without overflow,
- <a id="InferComputationDtype"></a>`InferComputationDtype(mlir::ElementType input_dtype)` — [`L99`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.cc#L99) — Return PyTorch's computation dtype for a given input dtype.
- <a id="InferOutputDtype"></a>`InferOutputDtype(const at::Tensor& self)` — [`L91`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.cc#L91) — Returns the input dtype if it is a floating-point type or complex type.
- <a id="ToString"></a>`ToString(const at::ScalarType& scalar_type, const std::string_view name)` — [`L39`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.cc#L39) — Use these functions only for debugging purposes.
- <a id="operator"></a>`operator==(const HashableScalar& lhs, const HashableScalar& rhs)` — [`L49`](../../../../../../raw/code/torch_tpu/csrc/common/aten_utils.cc#L49) — at::Scalars also lack an == operator by default, so we need to define one

