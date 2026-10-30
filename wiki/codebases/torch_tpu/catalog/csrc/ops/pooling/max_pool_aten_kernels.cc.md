---
title: 'Module: csrc/ops/pooling/max_pool_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/pooling/max_pool_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenMaxPool3dWithIndicesOut: AtenMaxPool3dWithIndicesOut(b650e72cf608e805).
  AtenMaxPool3dWithIndicesBackwardGradInput: AtenMaxPool3dWithIndicesBackwardGradInput(609872cb8c22c4ec).
  AtenMaxPool2dWithIndicesOut: AtenMaxPool2dWithIndicesOut(b650e72cf608e805).
  AtenMaxPool2dWithIndicesBackwardGradInput: AtenMaxPool2dWithIndicesBackwardGradInput(609872cb8c22c4ec).
  TpuMaxPool2d: TpuMaxPool2d(5a61ee1d528b11ee).
  TpuMaxPool3dBackward: TpuMaxPool3dBackward(d4a03e41cfc2633).
  TpuMaxPool1d: TpuMaxPool1d(5a61ee1d528b11ee).
  TpuMaxPool3d: TpuMaxPool3d(5a61ee1d528b11ee).
  TpuMaxPool1dBackward: TpuMaxPool1dBackward(d4a03e41cfc2633).
  TpuMaxPool2dBackward: TpuMaxPool2dBackward(d4a03e41cfc2633).
  AtenMaxPool3dWithIndices: AtenMaxPool3dWithIndices(3fad9a2695f9f59).
  AtenMaxPool3dWithIndicesBackward: AtenMaxPool3dWithIndicesBackward(238f691bd7cdd776).
  ComputeMaxPoolWithIndices: '`$anonymous_namespace_csrc/ops/pooling/max_pool_aten_kernels.cc`/ComputeMaxPoolWithIndices(c8b8efe116da9bf3).'
  BuildMaxPoolWithIndicesOutNd: '`$anonymous_namespace_csrc/ops/pooling/max_pool_aten_kernels.cc`/BuildMaxPoolWithIndicesOutNd(a39a9859c09f5fd).'
  BuildMaxPoolWithIndicesShlo: '`$anonymous_namespace_csrc/ops/pooling/max_pool_aten_kernels.cc`/BuildMaxPoolWithIndicesShlo(835419f9f57935a9).'
  BuildMaxPoolBackwardShlo: '`$anonymous_namespace_csrc/ops/pooling/max_pool_aten_kernels.cc`/BuildMaxPoolBackwardShlo(f104c6ebc0fb3238).'
  BuildMaxPoolShlo: '`$anonymous_namespace_csrc/ops/pooling/max_pool_aten_kernels.cc`/BuildMaxPoolShlo(64c6a557e0949ee9).'
  CheckMaxPoolDtypes: '`$anonymous_namespace_csrc/ops/pooling/max_pool_aten_kernels.cc`/CheckMaxPoolDtypes(45982de3b0bc1087).'
  BuildMaxPoolNd: '`$anonymous_namespace_csrc/ops/pooling/max_pool_aten_kernels.cc`/BuildMaxPoolNd(563b26f1ed200f7).'
  BuildMaxPoolWithIndicesBackwardGradInputNd: '`$anonymous_namespace_csrc/ops/pooling/max_pool_aten_kernels.cc`/BuildMaxPoolWithIndicesBackwardGradInputNd(6ee6b3a61055cae6).'
  BuildMaxPoolBackwardGradInputNd: '`$anonymous_namespace_csrc/ops/pooling/max_pool_aten_kernels.cc`/BuildMaxPoolBackwardGradInputNd(4096bb43233171f3).'
  BuildMaxPoolWithIndicesBackwardShlo: '`$anonymous_namespace_csrc/ops/pooling/max_pool_aten_kernels.cc`/BuildMaxPoolWithIndicesBackwardShlo(be85f442e1a9d349).'
  ComputeMaxPool: '`$anonymous_namespace_csrc/ops/pooling/max_pool_aten_kernels.cc`/ComputeMaxPool(a1c4858071da26a2).'
  TpuMaxPool2dAutograd.forward: TpuMaxPool2dAutograd#forward(54895bd1fa1b4941).
  TpuMaxPool3dAutograd.forward: TpuMaxPool3dAutograd#forward(54895bd1fa1b4941).
  TpuMaxPool1dAutograd.forward: TpuMaxPool1dAutograd#forward(54895bd1fa1b4941).
  TpuMaxPool2dAutograd.backward: TpuMaxPool2dAutograd#backward(305625f81d7e100).
  TpuMaxPool1dAutograd.backward: TpuMaxPool1dAutograd#backward(305625f81d7e100).
  TpuMaxPool3dAutograd.backward: TpuMaxPool3dAutograd#backward(305625f81d7e100).
  AtenMaxPool1d: AtenMaxPool1d(5a61ee1d528b11ee).
  AtenMaxPool2d: AtenMaxPool2d(5a61ee1d528b11ee).
  AtenMaxPool3d: AtenMaxPool3d(5a61ee1d528b11ee).
  CreatePoolIndicesIota: '`$anonymous_namespace_csrc/ops/pooling/max_pool_aten_kernels.cc`/CreatePoolIndicesIota(b9502e7e3a3b59a6).'
---
# Module: [`csrc/ops/pooling/max_pool_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc)

## Functions
- <a id="AtenMaxPool1d"></a>`AtenMaxPool1d(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode)` — [`L922`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L922) — Dispatched from AutogradPrivateUse1 for aten::max_pool1d.
- <a id="AtenMaxPool2d"></a>`AtenMaxPool2d(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode)` — [`L1031`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L1031) — Dispatched from AutogradPrivateUse1 for aten::max_pool2d.
- <a id="AtenMaxPool2dWithIndicesBackwardGradInput"></a>`AtenMaxPool2dWithIndicesBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode, const at::Tensor& indices, at::Tensor& grad_input)` — [`L855`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L855) — Dispatched from ATen PrivateUse1 for
- <a id="AtenMaxPool2dWithIndicesOut"></a>`AtenMaxPool2dWithIndicesOut(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode, at::Tensor& out, at::Tensor& indices)` — [`L792`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L792) — Dispatched from ATen PrivateUse1 for aten::max_pool2d_with_indices.out.
- <a id="AtenMaxPool3d"></a>`AtenMaxPool3d(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode)` — [`L1141`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L1141) — Dispatched from AutogradPrivateUse1 for aten::max_pool3d.
- <a id="AtenMaxPool3dWithIndices"></a>`AtenMaxPool3dWithIndices(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode)` — [`L826`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L826) — Dispatched from ATen PrivateUse1 for aten::max_pool3d_with_indices.
- <a id="AtenMaxPool3dWithIndicesBackward"></a>`AtenMaxPool3dWithIndicesBackward(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode, const at::Tensor& indices)` — [`L872`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L872) — Dispatched from ATen PrivateUse1 for aten::max_pool3d_with_indices_backward.
- <a id="AtenMaxPool3dWithIndicesBackwardGradInput"></a>`AtenMaxPool3dWithIndicesBackwardGradInput(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode, const at::Tensor& indices, at::Tensor& grad_input)` — [`L902`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L902) — Dispatched from ATen PrivateUse1 for
- <a id="AtenMaxPool3dWithIndicesOut"></a>`AtenMaxPool3dWithIndicesOut(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode, at::Tensor& out, at::Tensor& indices)` — [`L809`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L809) — Dispatched from ATen PrivateUse1 for aten::max_pool3d_with_indices.out.
- <a id="BuildMaxPoolBackwardGradInputNd"></a>`BuildMaxPoolBackwardGradInputNd(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode, int64_t spatial_dim_count, OpParamCacheKeys param_keys)` — [`L510`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L510) — Builds the backward pass for max_pool (without indices) directly returning
- <a id="BuildMaxPoolBackwardShlo"></a>`BuildMaxPoolBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp input, const int64_t spatial_dim_count, Dimensions kernel_size, Dimensions stride, Dimensions padding, Dimensions dilation, const bool ceil_mode)` — [`L377`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L377)
- <a id="BuildMaxPoolNd"></a>`BuildMaxPoolNd(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode, int64_t spatial_dim_count, OpParamCacheKeys param_keys)` — [`L718`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L718) — Builds max_pool forward pass (without indices) for N-D spatial dimensions
- <a id="BuildMaxPoolShlo"></a>`BuildMaxPoolShlo(mlir::MlirOp input, const int64_t spatial_dim_count, Dimensions kernel_size, Dimensions stride, Dimensions padding, Dimensions dilation, const bool ceil_mode)` — [`L325`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L325)
- <a id="BuildMaxPoolWithIndicesBackwardGradInputNd"></a>`BuildMaxPoolWithIndicesBackwardGradInputNd(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode, const at::Tensor& indices, at::Tensor& grad_input, int64_t spatial_dim_count, OpParamCacheKeys param_keys)` — [`L749`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L749) — Helper function to build and dispatch N-dimensional max_pool backward ops.
- <a id="BuildMaxPoolWithIndicesBackwardShlo"></a>`BuildMaxPoolWithIndicesBackwardShlo(mlir::MlirOp grad_output, mlir::MlirOp input, mlir::MlirOp indices, const int64_t spatial_dim_count, Dimensions kernel_size, Dimensions stride, Dimensions padding, Dimensions dilation, const bool ceil_mode)` — [`L562`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L562) — Builds the backward pass for max_pool with indices using StableHLO's
- <a id="BuildMaxPoolWithIndicesOutNd"></a>`BuildMaxPoolWithIndicesOutNd(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode, at::Tensor& out, at::Tensor& indices, int64_t spatial_dim_count, OpParamCacheKeys param_keys)` — [`L674`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L674) — Helper function to build and dispatch N-dimensional max_pool operations.
- `BuildMaxPoolWithIndicesShlo(mlir::MlirOp input, const int64_t spatial_dim_count, Dimensions kernel_size, Dimensions stride, Dimensions padding, Dimensions dilation, const bool ceil_mode)` — [`L263`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L263) — Builds the max_pool operations with indices and out tensors using
- <a id="BuildMaxPoolWithIndicesShlo"></a>`BuildMaxPoolWithIndicesShlo(mlir::MlirOp input, const int64_t spatial_dim_count, Dimensions kernel_size, Dimensions stride, Dimensions padding, Dimensions dilation, const bool ceil_mode)` — [`L263`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L263) — Builds the max_pool operations with indices and out tensors using
- <a id="CheckMaxPoolDtypes"></a>`CheckMaxPoolDtypes(const at::Tensor& self)` — [`L778`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L778)
- <a id="ComputeMaxPool"></a>`ComputeMaxPool(const BatchInput& batch_input_info, const ReduceWindowAttributes& reduce_window_attributes, const int64_t spatial_dim_count)` — [`L197`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L197)
- `ComputeMaxPoolWithIndices(const BatchInput& batch_input_info, const ReduceWindowAttributes& reduce_window_attributes, const int64_t spatial_dim_count)` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L116)
- <a id="ComputeMaxPoolWithIndices"></a>`ComputeMaxPoolWithIndices(const BatchInput& batch_input_info, const ReduceWindowAttributes& reduce_window_attributes, const int64_t spatial_dim_count)` — [`L116`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L116)
- <a id="CreatePoolIndicesIota"></a>`CreatePoolIndicesIota(const mlir::RankedTensorType& input_shape, mlir::MlirBuilder& builder, mlir::Type element_type)` — [`L80`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L80) — Creates an index tensor containing the local flattened index for each
- <a id="TpuMaxPool1d"></a>`TpuMaxPool1d(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode)` — [`L940`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L940) — Dispatched from PrivateUse1 for tpu::_max_pool1d.
- <a id="TpuMaxPool1dBackward"></a>`TpuMaxPool1dBackward(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode)` — [`L959`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L959) — Dispatched from PrivateUse1 for tpu::_max_pool1d_backward.
- <a id="TpuMaxPool2d"></a>`TpuMaxPool2d(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode)` — [`L1049`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L1049) — Dispatched from PrivateUse1 for tpu::_max_pool2d.
- <a id="TpuMaxPool2dBackward"></a>`TpuMaxPool2dBackward(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode)` — [`L1068`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L1068) — Dispatched from PrivateUse1 for tpu::_max_pool2d_backward.
- <a id="TpuMaxPool3d"></a>`TpuMaxPool3d(const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode)` — [`L1159`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L1159) — Dispatched from PrivateUse1 for tpu::_max_pool3d.
- <a id="TpuMaxPool3dBackward"></a>`TpuMaxPool3dBackward(const at::Tensor& grad_output, const at::Tensor& self, at::IntArrayRef kernel_size, at::IntArrayRef stride, at::IntArrayRef padding, at::IntArrayRef dilation, bool ceil_mode)` — [`L1178`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L1178) — Dispatched from PrivateUse1 for tpu::_max_pool3d_backward.

## Other members
- <a id="TpuMaxPool1dAutograd.backward"></a>`TpuMaxPool1dAutograd.backward` — [`L1000`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L1000)
- <a id="TpuMaxPool1dAutograd.forward"></a>`TpuMaxPool1dAutograd.forward` — [`L978`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L978)
- <a id="TpuMaxPool2dAutograd.backward"></a>`TpuMaxPool2dAutograd.backward` — [`L1110`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L1110)
- <a id="TpuMaxPool2dAutograd.forward"></a>`TpuMaxPool2dAutograd.forward` — [`L1087`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L1087)
- <a id="TpuMaxPool3dAutograd.backward"></a>`TpuMaxPool3dAutograd.backward` — [`L1220`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L1220)
- <a id="TpuMaxPool3dAutograd.forward"></a>`TpuMaxPool3dAutograd.forward` — [`L1197`](../../../../../../../raw/code/torch_tpu/csrc/ops/pooling/max_pool_aten_kernels.cc#L1197)

