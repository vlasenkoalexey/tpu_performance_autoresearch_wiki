---
title: 'Module: csrc/ops/prelu/prelu_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/prelu/prelu_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenPreluKernelBackward: AtenPreluKernelBackward(972b2be973e3a372).
  AtenPreluKernel: AtenPreluKernel(91c7cc726c97ea99).
  ValidateIsFloatingPoint: '`$anonymous_namespace_csrc/ops/prelu/prelu_aten_kernels.cc`/ValidateIsFloatingPoint(d8359b99282c084c).'
  BuildPreluKernelBackwardShlo: '`$anonymous_namespace_csrc/ops/prelu/prelu_aten_kernels.cc`/BuildPreluKernelBackwardShlo(92320f878f865bee).'
  BuildPreluKernelShlo: '`$anonymous_namespace_csrc/ops/prelu/prelu_aten_kernels.cc`/BuildPreluKernelShlo(9dd408ac7de815bd).'
---
# Module: [`csrc/ops/prelu/prelu_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/prelu/prelu_aten_kernels.cc)

## Functions
- <a id="AtenPreluKernel"></a>`AtenPreluKernel(const at::Tensor& self, const at::Tensor& weight)` — [`L141`](../../../../../../../raw/code/torch_tpu/csrc/ops/prelu/prelu_aten_kernels.cc#L141)
- <a id="AtenPreluKernelBackward"></a>`AtenPreluKernelBackward(const at::Tensor& grad_output, const at::Tensor& self, const at::Tensor& weight)` — [`L180`](../../../../../../../raw/code/torch_tpu/csrc/ops/prelu/prelu_aten_kernels.cc#L180)
- <a id="BuildPreluKernelBackwardShlo"></a>`BuildPreluKernelBackwardShlo(mlir::MlirOp grad_output_op, mlir::MlirOp self_op, mlir::MlirOp weight_op, c10::IntArrayRef self_shape, c10::IntArrayRef weight_shape)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/prelu/prelu_aten_kernels.cc#L80)
- `BuildPreluKernelBackwardShlo(mlir::MlirOp grad_output_op, mlir::MlirOp self_op, mlir::MlirOp weight_op, c10::IntArrayRef self_shape, c10::IntArrayRef weight_shape)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/prelu/prelu_aten_kernels.cc#L80)
- <a id="BuildPreluKernelShlo"></a>`BuildPreluKernelShlo(mlir::MlirOp self_op, mlir::MlirOp weight_op)` — [`L64`](../../../../../../../raw/code/torch_tpu/csrc/ops/prelu/prelu_aten_kernels.cc#L64)
- <a id="ValidateIsFloatingPoint"></a>`ValidateIsFloatingPoint(const at::Tensor& tensor, const std::string_view name)` — [`L56`](../../../../../../../raw/code/torch_tpu/csrc/ops/prelu/prelu_aten_kernels.cc#L56)

