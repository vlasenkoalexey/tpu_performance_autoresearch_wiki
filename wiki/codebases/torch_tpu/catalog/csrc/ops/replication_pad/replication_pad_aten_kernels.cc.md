---
title: 'Module: csrc/ops/replication_pad/replication_pad_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/replication_pad/replication_pad_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenReplicationPad3dBackward: AtenReplicationPad3dBackward(7a3ba4552e2a8785).
  AtenReplicationPad2dBackward: AtenReplicationPad2dBackward(7a3ba4552e2a8785).
  AtenReplicationPad3dBackwardGradInput: AtenReplicationPad3dBackwardGradInput(67ea18198051e64b).
  AtenReplicationPad2dBackwardGradInput: AtenReplicationPad2dBackwardGradInput(67ea18198051e64b).
  AtenReplicationPad1dBackwardGradInput: AtenReplicationPad1dBackwardGradInput(67ea18198051e64b).
  AtenReplicationPad3dOut: AtenReplicationPad3dOut(b80b45ac1719e16d).
  AtenReplicationPad1dOut: AtenReplicationPad1dOut(b80b45ac1719e16d).
  AtenReplicationPad2dOut: AtenReplicationPad2dOut(b80b45ac1719e16d).
  ReplicationPadHelper: '`$anonymous_namespace_csrc/ops/replication_pad/replication_pad_aten_kernels.cc`/ReplicationPadHelper(97c374cfe47a43b6).'
  Validate3DPaddingIsValid: '`$anonymous_namespace_csrc/ops/replication_pad/replication_pad_aten_kernels.cc`/Validate3DPaddingIsValid(2f39c304bc96430f).'
  BuildReplicationPadBackwardShlo: '`$anonymous_namespace_csrc/ops/replication_pad/replication_pad_aten_kernels.cc`/BuildReplicationPadBackwardShlo(4637dcfe7f09c56b).'
  BuildReplicationPadShlo: '`$anonymous_namespace_csrc/ops/replication_pad/replication_pad_aten_kernels.cc`/BuildReplicationPadShlo(4637dcfe7f09c56b).'
  BuildReplicationPadBackwardSidePaddingShlo: '`$anonymous_namespace_csrc/ops/replication_pad/replication_pad_aten_kernels.cc`/BuildReplicationPadBackwardSidePaddingShlo(4edda1d434532867).'
---
# Module: [`csrc/ops/replication_pad/replication_pad_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc)

## Functions
- <a id="AtenReplicationPad1dBackwardGradInput"></a>`AtenReplicationPad1dBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef padding, at::Tensor& grad_input)` — [`L340`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L340)
- <a id="AtenReplicationPad1dOut"></a>`AtenReplicationPad1dOut(const at::Tensor& self, at::IntArrayRef padding, at::Tensor& out)` — [`L308`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L308)
- <a id="AtenReplicationPad2dBackward"></a>`AtenReplicationPad2dBackward(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef padding)` — [`L382`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L382)
- <a id="AtenReplicationPad2dBackwardGradInput"></a>`AtenReplicationPad2dBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef padding, at::Tensor& grad_input)` — [`L354`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L354)
- <a id="AtenReplicationPad2dOut"></a>`AtenReplicationPad2dOut(const at::Tensor& self, at::IntArrayRef padding, at::Tensor& out)` — [`L319`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L319)
- <a id="AtenReplicationPad3dBackward"></a>`AtenReplicationPad3dBackward(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef padding)` — [`L431`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L431)
- <a id="AtenReplicationPad3dBackwardGradInput"></a>`AtenReplicationPad3dBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef padding, at::Tensor& grad_input)` — [`L368`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L368)
- <a id="AtenReplicationPad3dOut"></a>`AtenReplicationPad3dOut(const at::Tensor& self, at::IntArrayRef padding, at::Tensor& out)` — [`L330`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L330)
- <a id="BuildReplicationPadBackwardShlo"></a>`BuildReplicationPadBackwardShlo(mlir::MlirOp input, Dimensions padding, Dimensions output_shape, int num_pad_dimensions)` — [`L163`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L163)
- <a id="BuildReplicationPadBackwardSidePaddingShlo"></a>`BuildReplicationPadBackwardSidePaddingShlo(mlir::MlirOp op, mlir::RankedTensorType input_tensor_type, Dimensions input_shape, int64_t padding_size, int64_t dimension, int64_t left_bound, int64_t right_bound)` — [`L126`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L126) — Generate code to handle accumulation of the padding slice, or propagation of
- <a id="BuildReplicationPadShlo"></a>`BuildReplicationPadShlo(mlir::MlirOp input, Dimensions padding, Dimensions output_shape, int num_pad_dimensions)` — [`L57`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L57)
- <a id="ReplicationPadHelper"></a>`ReplicationPadHelper(absl::AnyInvocable<absl::StatusOr<mlir::MlirOp>(mlir::MlirOp input, Dimensions padding, Dimensions output_shape, int num_pad_dimensions) const> shlo_builder_function, OpParamCacheKeys param_keys, const at::Tensor& self, at::IntArrayRef padding, at::Tensor& out, int num_pad_dimensions)` — [`L227`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L227)
- <a id="Validate3DPaddingIsValid"></a>`Validate3DPaddingIsValid(absl::Span<const int64_t> grad_output, absl::Span<const int64_t> padding)` — [`L271`](../../../../../../../raw/code/torch_tpu/csrc/ops/replication_pad/replication_pad_aten_kernels.cc#L271)

