---
title: 'Module: csrc/ops/linspace/linspace_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/linspace/linspace_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenLinspaceOut: AtenLinspaceOut(cc5732730f3ec055).
  BuildLinspaceInterpolation: '`$anonymous_namespace_csrc/ops/linspace/linspace_aten_kernels.cc`/BuildLinspaceInterpolation(d8fd86e77ff8a7a9).'
  BuildLinspaceOp: '`$anonymous_namespace_csrc/ops/linspace/linspace_aten_kernels.cc`/BuildLinspaceOp(fd51b25f6874c926).'
  PrepareScalar: '`$anonymous_namespace_csrc/ops/linspace/linspace_aten_kernels.cc`/PrepareScalar(d8fb12d83a1e7678).'
  GetComputeType: '`$anonymous_namespace_csrc/ops/linspace/linspace_aten_kernels.cc`/GetComputeType(b55dd0519e0ab1fe).'
---
# Module: [`csrc/ops/linspace/linspace_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/linspace/linspace_aten_kernels.cc)

## Functions
- <a id="AtenLinspaceOut"></a>`AtenLinspaceOut(const at::Scalar& start, const at::Scalar& end, int64_t steps, at::Tensor& out)` — [`L237`](../../../../../../../raw/code/torch_tpu/csrc/ops/linspace/linspace_aten_kernels.cc#L237)
- <a id="BuildLinspaceInterpolation"></a>`BuildLinspaceInterpolation(mlir::MlirBuilder& builder, int64_t steps, mlir::MlirOp start_scalar, mlir::MlirOp end_scalar, mlir::RankedTensorType compute_tensor_type, mlir::Type mlir_type)` — [`L78`](../../../../../../../raw/code/torch_tpu/csrc/ops/linspace/linspace_aten_kernels.cc#L78)
- <a id="BuildLinspaceOp"></a>`BuildLinspaceOp(mlir::MlirBuilder& builder, int64_t steps, mlir::MlirOp start_op, mlir::MlirOp end_op, mlir::ElementType output_mlir_type)` — [`L191`](../../../../../../../raw/code/torch_tpu/csrc/ops/linspace/linspace_aten_kernels.cc#L191)
- <a id="GetComputeType"></a>`GetComputeType(mlir::MlirBuilder& builder, mlir::Type mlir_type)` — [`L63`](../../../../../../../raw/code/torch_tpu/csrc/ops/linspace/linspace_aten_kernels.cc#L63)
- <a id="PrepareScalar"></a>`PrepareScalar(mlir::MlirOp scalar, const mlir::RankedTensorType output_type)` — [`L52`](../../../../../../../raw/code/torch_tpu/csrc/ops/linspace/linspace_aten_kernels.cc#L52)

