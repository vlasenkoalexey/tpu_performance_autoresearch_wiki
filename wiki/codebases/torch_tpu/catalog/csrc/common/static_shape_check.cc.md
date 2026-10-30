---
title: 'Module: csrc/common/static_shape_check.cc'
type: catalog
provenance: extracted
module: csrc/common/static_shape_check.cc
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  ValidateStaticShapeImpl: '`$anonymous_namespace_csrc/common/static_shape_check.cc`/ValidateStaticShapeImpl(d0766ac5a5188d2a).'
  ValidateStaticShape: ValidateStaticShape(e7216eec7df4b20).
  GetShapeStringWithDynamicDimensionsUpperBound: '`$anonymous_namespace_csrc/common/static_shape_check.cc`/GetShapeStringWithDynamicDimensionsUpperBound(49e0bc290b4601d8).'
  GetShapeStringWithDynamicDimensions: '`$anonymous_namespace_csrc/common/static_shape_check.cc`/GetShapeStringWithDynamicDimensions(7805b7965c04c4bb).'
---
# Module: [`csrc/common/static_shape_check.cc`](../../../../../../raw/code/torch_tpu/csrc/common/static_shape_check.cc)

## Functions
- <a id="GetShapeStringWithDynamicDimensions"></a>`GetShapeStringWithDynamicDimensions(2, 3, 4, 5)` — [`L59`](../../../../../../raw/code/torch_tpu/csrc/common/static_shape_check.cc#L59) — Return a string representation of the shape of `type`.
- <a id="GetShapeStringWithDynamicDimensionsUpperBound"></a>`GetShapeStringWithDynamicDimensionsUpperBound(2, 3, 4, 5)` — [`L89`](../../../../../../raw/code/torch_tpu/csrc/common/static_shape_check.cc#L89) — Return a string representation of the shape of `sizes`.
- <a id="ValidateStaticShape"></a>`ValidateStaticShape(const at::Tensor& tensor, const DeviceBufferRef& buffer_ref, const std::string_view arg_name)` — [`L140`](../../../../../../raw/code/torch_tpu/csrc/common/static_shape_check.cc#L140) — Checks that the given `tensor` only has static dimensions.
- `ValidateStaticShape(mlir::RankedTensorType type, const std::string_view arg_name)` — [`L129`](../../../../../../raw/code/torch_tpu/csrc/common/static_shape_check.cc#L129) — Checks that the given `type` only has static dimensions.
- <a id="ValidateStaticShapeImpl"></a>`ValidateStaticShapeImpl(const int64_t dynamic_dimensions_number, const std::string_view name, const GetExtraErrorMessage& get_extra_error_message)` — [`L115`](../../../../../../raw/code/torch_tpu/csrc/common/static_shape_check.cc#L115) — Runs the actual static shape check.

