---
title: 'Module: csrc/ops/scaled_dot_product_attention/helpers.cc'
type: catalog
provenance: extracted
module: csrc/ops/scaled_dot_product_attention/helpers.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  flatten_batch_dims: flatten_batch_dims(4ee3dbb69c99e93a).
  EmptyLikeStrides: EmptyLikeStrides(4f148ada945ab42c).
  unflatten_batch_dims: unflatten_batch_dims(3bc34110f3947668).
  get_batch_size: get_batch_size(b7b59651fad9ca8).
  MatchingLayoutStrides: MatchingLayoutStrides(c7146bbaa203fc68).
  GetScaleDefaulted: GetScaleDefaulted(ad423de620e3fc61).
  ReshapeBatchDimsOrDie: '`$anonymous_namespace_csrc/ops/scaled_dot_product_attention/helpers.cc`/ReshapeBatchDimsOrDie(f90d011bcfad1240).'
---
# Module: [`csrc/ops/scaled_dot_product_attention/helpers.cc`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/helpers.cc)

## Functions
- <a id="EmptyLikeStrides"></a>`EmptyLikeStrides(const at::TensorBase& tensor)` — [`L104`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/helpers.cc#L104) — Returns the strides of `torch.empty_like(tensor)` with the default — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="GetScaleDefaulted"></a>`GetScaleDefaulted(mlir::MlirBuilder& builder, std::optional<double> maybe_scale, int64_t head_dim, mlir::Type element_type)` — [`L93`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/helpers.cc#L93)
- <a id="MatchingLayoutStrides"></a>`MatchingLayoutStrides(const at::TensorBase& query, absl::Span<const int64_t> result_sizes)` — [`L114`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/helpers.cc#L114) — Returns the strides of `alloc_with_matching_layout(query, result_sizes)` in
- <a id="ReshapeBatchDimsOrDie"></a>`ReshapeBatchDimsOrDie(mlir::MlirOp mlir_op, absl::Span<const int64_t> shape)` — [`L49`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/helpers.cc#L49) — Batch dim (un)flattening is a valid reshape reassociation as long as at most
- <a id="flatten_batch_dims"></a>`flatten_batch_dims(mlir::MlirOp mlir_op, int batch_size, int num_batch_dims)` — [`L59`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/helpers.cc#L59) — Batch dim (un)flattening helpers. Shapes are static sizes, or upper bounds — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="get_batch_size"></a>`get_batch_size(absl::Span<const int64_t> shape)` — [`L83`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/helpers.cc#L83) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- <a id="unflatten_batch_dims"></a>`unflatten_batch_dims(mlir::MlirOp mlir_op, mlir::MlirOp mlir_op_with_target_dims)` — [`L77`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/helpers.cc#L77) — documented in [scaled-dot-product-attention](../../../../concepts/scaled-dot-product-attention.md)
- `unflatten_batch_dims(mlir::MlirOp mlir_op, absl::Span<const int64_t> shape)` — [`L72`](../../../../../../../raw/code/torch_tpu/csrc/ops/scaled_dot_product_attention/helpers.cc#L72)

