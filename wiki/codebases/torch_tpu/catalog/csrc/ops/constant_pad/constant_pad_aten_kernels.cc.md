---
title: 'Module: csrc/ops/constant_pad/constant_pad_aten_kernels.cc'
type: catalog
provenance: extracted
module: csrc/ops/constant_pad/constant_pad_aten_kernels.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  AtenConstantPadNd: AtenConstantPadNd(844849243203ec2).
  BuildConstantPadNdShlo: '`$anonymous_namespace_csrc/ops/constant_pad/constant_pad_aten_kernels.cc`/BuildConstantPadNdShlo(d8b0c1361adef3b).'
  PadSingleDimensionShlo: '`$anonymous_namespace_csrc/ops/constant_pad/constant_pad_aten_kernels.cc`/PadSingleDimensionShlo(67e69c3dc5749b97).'
---
# Module: [`csrc/ops/constant_pad/constant_pad_aten_kernels.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/constant_pad/constant_pad_aten_kernels.cc)

## Functions
- <a id="AtenConstantPadNd"></a>`AtenConstantPadNd(const at::Tensor& self, at::IntArrayRef pad, const at::Scalar& value)` — [`L154`](../../../../../../../raw/code/torch_tpu/csrc/ops/constant_pad/constant_pad_aten_kernels.cc#L154) — Implements aten::constant_pad_nd (torch.nn.functional.pad with
- <a id="BuildConstantPadNdShlo"></a>`BuildConstantPadNdShlo(mlir::MlirOp input, mlir::MlirOp val_scalar, const Dimensions& pad_vec)` — [`L129`](../../../../../../../raw/code/torch_tpu/csrc/ops/constant_pad/constant_pad_aten_kernels.cc#L129) — Builds the StableHLO graph for N-dimensional constant padding.
- <a id="PadSingleDimensionShlo"></a>`PadSingleDimensionShlo(mlir::MlirOp input, mlir::MlirOp val_scalar, const mlir::RankedTensorType input_type, const int64_t dim, const int64_t left_pad, const int64_t right_pad, Dimensions& cur_shape)` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/ops/constant_pad/constant_pad_aten_kernels.cc#L51) — Applies constant padding (and/or negative-padding cropping) along a single

