---
title: 'Module: csrc/internal/dynamism/dynamism_ops.cc'
type: catalog
provenance: extracted
module: csrc/internal/dynamism/dynamism_ops.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  Slice: '`$anonymous_namespace_csrc/internal/dynamism/dynamism_ops.cc`/Slice(8417f6002b1ef712).'
  Pad: '`$anonymous_namespace_csrc/internal/dynamism/dynamism_ops.cc`/Pad(8417f6002b1ef712).'
  GetPadModule: GetPadModule(ae29a3410e5e54aa).
  GetDynamicPadModule: GetDynamicPadModule(293d0774051e47c).
  GetSliceModule: GetSliceModule(5eb8736ae408420a).
  MakeDynamicTensorType: '`$anonymous_namespace_csrc/internal/dynamism/dynamism_ops.cc`/MakeDynamicTensorType(edad69b9e064db34).'
---
# Module: [`csrc/internal/dynamism/dynamism_ops.cc`](../../../../../../../raw/code/torch_tpu/csrc/internal/dynamism/dynamism_ops.cc)

## Functions
- <a id="GetDynamicPadModule"></a>`GetDynamicPadModule(mlir::MLIRContext& mlir_context, absl::Span<const Shape> shapes)` — [`L214`](../../../../../../../raw/code/torch_tpu/csrc/internal/dynamism/dynamism_ops.cc#L214) — Universal dynamic pad module. Given a list of shapes with dynamic dimensions,
- <a id="GetPadModule"></a>`GetPadModule(mlir::MLIRContext& mlir_context, absl::Span<const Shape> shapes, bool pad_only_module)` — [`L171`](../../../../../../../raw/code/torch_tpu/csrc/internal/dynamism/dynamism_ops.cc#L171) — Universal pad module. Given a list of shapes with dynamic dimensions, returns
- <a id="GetSliceModule"></a>`GetSliceModule(mlir::MLIRContext& mlir_context, absl::Span<const Dimensions> dimensions_vec, absl::Span<const Dimensions> padded_dimensions_vec, absl::Span<const mlir::ElementType> input_dtypes)` — [`L269`](../../../../../../../raw/code/torch_tpu/csrc/internal/dynamism/dynamism_ops.cc#L269) — Universal slice module. Given a list of padded and unpadded shapes, returns a
- <a id="MakeDynamicTensorType"></a>`MakeDynamicTensorType(mlir::MLIRContext& context, const Dimensions& dimensions, const Dimensions& padded_dimensions, mlir::ElementType element_type)` — [`L147`](../../../../../../../raw/code/torch_tpu/csrc/internal/dynamism/dynamism_ops.cc#L147)
- <a id="Pad"></a>`Pad(mlir::MlirOp input_op, const Dimensions& target_dimensions)` — [`L51`](../../../../../../../raw/code/torch_tpu/csrc/internal/dynamism/dynamism_ops.cc#L51) — Pads the input tensor to the target dimensions.
- <a id="Slice"></a>`Slice(mlir::MlirOp input_op, const Dimensions& target_dimensions)` — [`L92`](../../../../../../../raw/code/torch_tpu/csrc/internal/dynamism/dynamism_ops.cc#L92) — Slices the input tensor to the target dimensions.

