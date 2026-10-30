---
title: 'Module: csrc/common/shape.h'
type: catalog
provenance: extracted
module: csrc/common/shape.h
status: fresh
symbol_base: cxx . . $ torch_tpu/
symbols:
  Shape: Shape#
  Shape.Shape: Shape#Shape(183e55de4df2029c).
  Shape.dimensions: Shape#dimensions(6ce8297fad51686c).
  Shape.dtype: Shape#dtype(8d8220464a956245).
  BoundedDynamicDimension: BoundedDynamicDimension#
  Shape.dynamic_dimensions: Shape#dynamic_dimensions(d9f1e7baf22fe916).
  BoundedDynamicDimension.dimension: BoundedDynamicDimension#dimension.
  Shape.layout: Shape#layout(e77471b654267188).
  operator: '`operator==`(fc4cde702266c6dd).'
  BoundedDynamicDimension.upper_bound: BoundedDynamicDimension#upper_bound.
  Shape.layout_: Shape#layout_.
  Shape.set_layout: Shape#set_layout(96e5925aa4a6ad90).
  Shape.on_device_shape_is_dynamic_: Shape#on_device_shape_is_dynamic_.
  BoundedDynamicDimension.lower_bound: BoundedDynamicDimension#lower_bound.
  Shape.set_on_device_shape_is_dynamic: Shape#set_on_device_shape_is_dynamic(b45ddcbc8423892c).
  Shape.dynamic_dimensions_: Shape#dynamic_dimensions_.
  Shape.dimensions_: Shape#dimensions_.
  Shape.dtype_: Shape#dtype_.
  Shape.set_dtype: Shape#set_dtype(e824c7a5a6a70ba6).
  Shape.on_device_shape_is_dynamic: Shape#on_device_shape_is_dynamic(50ce9a9e25b4a850).
---
# Module: [`csrc/common/shape.h`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h)

## Classes
### <a id="BoundedDynamicDimension"></a>`BoundedDynamicDimension`
- def: [`csrc/common/shape.h:36`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L36)
- doc: A dimension that should be interpreted as dynamic.
- signature: `struct BoundedDynamicDimension`
- members:
  - <a id="BoundedDynamicDimension.dimension"></a>`dimension` — [`L37`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L37)
  - <a id="BoundedDynamicDimension.lower_bound"></a>`lower_bound` — [`L38`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L38)
  - <a id="BoundedDynamicDimension.upper_bound"></a>`upper_bound` — [`L39`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L39)
- used by: [`ToString`](shape.cc.md#ToString), [`PadModuleCacheKey`](cache_key.cc.md#PadModuleCacheKey), [`MarkDynamic`](../eager/device_buffer.cc.md#DeviceBufferList.MarkDynamic), [`on_device_shape_is_dynamic`](../eager/device_buffer.cc.md#DeviceBufferRef.on_device_shape_is_dynamic), [`ShapeDynamismMetadata`](cache_key.cc.md#ShapeDynamismMetadata.ShapeDynamismMetadata), [`on_device_shape_is_dynamic`](../eager/device_buffer.cc.md#DeviceBufferList.on_device_shape_is_dynamic), [`MarkDynamic`](../internal/dynamism/dynamism.cc.md#MarkDynamic), [`MakePadDynamicShapes`](../internal/compile/tpu_torch_compile.cc.md#MakePadDynamicShapes), [`GetPadModule`](../internal/dynamism/dynamism_ops.cc.md#GetPadModule), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_DynamicCacheLayoutMismatch_Test.TestBody), [`GetDynamicPadModule`](../internal/dynamism/dynamism_ops.cc.md#GetDynamicPadModule), [`MakePlaceholder`](../internal/compile/compiled_mode.cc.md#MakePlaceholder), [`DeviceBufferList`](../eager/device_buffer.h.md#DeviceBufferList.DeviceBufferList), [`PyMarkDynamic`](../internal/dynamism/dynamism_py.cc.md#PyMarkDynamic), [`PyMakeDynamicPlaceholder`](../internal/compile/tpu_torch_compile.cc.md#PyMakeDynamicPlaceholder), [`PyGetDynamismInfo`](../internal/dynamism/dynamism_py.cc.md#PyGetDynamismInfo), [`TorchTpuPyBindInitModule__tpu_torch_dynamism`](../internal/dynamism/dynamism_py.cc.md#TorchTpuPyBindInitModule__tpu_torch_dynamism), [`ResolvePaddingShapes`](compilation_cache.cc.md#ResolvePaddingShapes), [`ValidateStaticShape`](static_shape_check.cc.md#ValidateStaticShape), [`TestBody`](../internal/dynamism/dynamism_ops_test.cc.md#DynamismOpsTest_GetPadModuleDocstringExample_Test.TestBody), [`Shape`](shape.h.md#Shape.Shape), [`dynamic_dimensions`](shape.h.md#Shape.dynamic_dimensions), [`ToPaddedShapes`](../internal/compile/tpu_torch_compile.cc.md#ToPaddedShapes), [`CreatePaddedDynamicArgumentOp`](../eager/traversal.cc.md#CreatePaddedDynamicArgumentOp), [`CreateNativeDynamicArgumentOp`](../eager/traversal.cc.md#CreateNativeDynamicArgumentOp), [`index`](../eager/device_buffer.h.md#DeviceBufferRef.index), [`GetShapeStringWithDynamicDimensionsUpperBound`](static_shape_check.cc.md#GetShapeStringWithDynamicDimensionsUpperBound), [`operator==`](shape.h.md#operator), [`on_device_shape_is_dynamic_`](shape.h.md#Shape.on_device_shape_is_dynamic_), [`set_on_device_shape_is_dynamic`](shape.h.md#Shape.set_on_device_shape_is_dynamic)

### <a id="Shape"></a>`Shape`
- def: [`csrc/common/shape.h:51`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L51)
- doc: A tensor shape, consisting of dimensions and element type.
- signature: `class Shape`
- members:
  - `Shape(Dimensions dimensions, mlir::ElementType dtype)` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L54)
  - `Shape()` — [`L53`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L53)
  - <a id="Shape.Shape"></a>`Shape(Dimensions dimensions, mlir::ElementType dtype)` — [`L54`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L54)
  - `Shape(Dimensions dimensions, mlir::ElementType dtype, absl::InlinedVector<BoundedDynamicDimension, 1> dynamic_dimensions)` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L56)
  - `Shape(Dimensions dimensions, mlir::ElementType dtype, absl::InlinedVector<BoundedDynamicDimension, 1> dynamic_dimensions)` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L56)
  - `Shape(Dimensions dimensions, mlir::ElementType dtype, absl::InlinedVector<BoundedDynamicDimension, 1> dynamic_dimensions)` — [`L56`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L56)
  - `dimensions()` — [`L62`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L62)
  - `dimensions()` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L63)
  - `dimensions()` — [`L63`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L63)
  - <a id="Shape.dimensions"></a>`dimensions()` — [`L62`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L62)
  - <a id="Shape.dtype"></a>`dtype()` — [`L65`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L65)
  - `dynamic_dimensions()` — [`L79`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L79)
  - `dynamic_dimensions()` — [`L79`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L79)
  - <a id="Shape.dynamic_dimensions"></a>`dynamic_dimensions()` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L75)
  - `dynamic_dimensions()` — [`L75`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L75)
  - <a id="Shape.layout"></a>`layout()` — [`L83`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L83)
  - <a id="Shape.on_device_shape_is_dynamic"></a>`on_device_shape_is_dynamic()` — [`L68`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L68)
  - <a id="Shape.set_dtype"></a>`set_dtype(mlir::ElementType dtype)` — [`L66`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L66)
  - <a id="Shape.set_layout"></a>`set_layout(CustomLayout layout)` — [`L84`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L84)
  - <a id="Shape.set_on_device_shape_is_dynamic"></a>`set_on_device_shape_is_dynamic(bool on_device_shape_is_dynamic)` — [`L71`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L71)
  - <a id="Shape.dimensions_"></a>`dimensions_` — [`L94`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L94)
  - <a id="Shape.dtype_"></a>`dtype_` — [`L95`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L95)
  - <a id="Shape.dynamic_dimensions_"></a>`dynamic_dimensions_` — [`L100`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L100) — We choose 1 as the inlined size because most Shapes are not dynamic, and
  - <a id="Shape.layout_"></a>`layout_` — [`L101`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L101)
  - <a id="Shape.on_device_shape_is_dynamic_"></a>`on_device_shape_is_dynamic_` — [`L96`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L96)
- uses (calls/refs, reference-scoped): [`Dimensions`](dimension_types.h.md#Dimensions), [`ToString`](shape.cc.md#ToString), [`MakeShape`](shape.cc.md#MakeShape), [`CustomLayout`](dimension_types.h.md#CustomLayout), [`BoundedDynamicDimension`](shape.h.md#BoundedDynamicDimension)
- used by: [`CreateDeferred`](../eager/device_buffer.cc.md#DeviceBufferList.CreateDeferred), [`DispatchOp`](../eager/op_dispatcher.h.md#DispatchOp), [`ShapeDynamismMetadata`](cache_key.h.md#ShapeDynamismMetadata), [`ComputeInverseViewOperation`](../ops/view_decomposition/inversion.cc.md#ComputeInverseViewOperation), [`ToString`](shape.cc.md#ToString), [`PadModuleCacheKey`](cache_key.cc.md#PadModuleCacheKey), [`CreateViewDeviceBufferRef`](../eager/device_buffer_utils.cc.md#CreateViewDeviceBufferRef), [`stages`](../ops/view_decomposition/inversion.h.md#InverseViewOperation.stages), [`MarkDynamic`](../eager/device_buffer.cc.md#DeviceBufferList.MarkDynamic), [`AtenSparseMapRow`](../ops/experimental/sparse_map_row/sparse_map_row_aten_kernels.cc.md#AtenSparseMapRow), [`pjrt_buffer_size`](../eager/device_buffer.cc.md#DeviceBufferList.pjrt_buffer_size), [`CreateInverseViewDeviceBufferRef`](../eager/device_buffer_utils.cc.md#CreateInverseViewDeviceBufferRef), [`GetOutputShapes`](../internal/compile/compiled_mode.cc.md#GetOutputShapes), [`PyCreateScanOp`](../internal/compile/dispatch_scan.cc.md#PyCreateScanOp), [`CreatePending`](../eager/device_buffer.cc.md#DeviceBufferList.CreatePending), [`GetSliceModuleCacheKey`](cache_key.cc.md#ShapeDynamismMetadata.GetSliceModuleCacheKey), [`AtenSparseDenseMatmulGradWithSgd`](../ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_sgd_aten_kernels.cc.md#AtenSparseDenseMatmulGradWithSgd), [`AtenSparseDenseMatmulGradWithAdagrad`](../ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adagrad_aten_kernels.cc.md#AtenSparseDenseMatmulGradWithAdagrad), [`AtenSparseDenseMatmulGradWithAdam`](../ops/experimental/sparse_dense_matmul/sparse_dense_matmul_grad_with_adam_aten_kernels.cc.md#AtenSparseDenseMatmulGradWithAdam), [`is_constant`](../eager/device_buffer.cc.md#DeviceBufferRef.is_constant), [`CreateEmptyDeviceBufferRef`](../eager/device_buffer_utils.cc.md#CreateEmptyDeviceBufferRef), [`ShapeDynamismMetadata`](cache_key.cc.md#ShapeDynamismMetadata.ShapeDynamismMetadata), [`size_bytes`](../eager/device_buffer.cc.md#DeviceBufferList.size_bytes), [`TestBody`](compilation_cache_test.cc.md#CompilationCacheTest_UnboundedDynamicCache_Test.TestBody), [`dimensions`](../eager/device_buffer.cc.md#DeviceBufferList.dimensions), [`on_device_shape_is_dynamic`](../eager/device_buffer.cc.md#DeviceBufferList.on_device_shape_is_dynamic), [`dynamic_dimensions`](../eager/device_buffer.cc.md#DeviceBufferList.dynamic_dimensions), [`element_type`](../eager/device_buffer.cc.md#DeviceBufferList.element_type), [`num_elements`](../eager/device_buffer.cc.md#DeviceBufferList.num_elements), [`IsStaticShapeCompatible`](cache_key.cc.md#ShapeDynamismMetadata.IsStaticShapeCompatible), [`ExtractArgumentLayoutsIfDifferentFromDefault`](../eager/execution_task.cc.md#ExtractArgumentLayoutsIfDifferentFromDefault), [`VerifyAndCompileTraversal`](../eager/execution_task.cc.md#VerifyAndCompileTraversal), [`GetOrCreateCacheEntry`](compilation_cache.cc.md#CompilationCache.GetOrCreateCacheEntry), [`Compile`](../eager/traversal.cc.md#Traversal.Compile), [`TestBody`](../experimental/precompiled_kernels/nonzero_indices_test.cc.md#NonzeroIndicesTest_Benchmark_Test.TestBody), [`TestBody`](../experimental/precompiled_kernels/nonzero_indices_test.cc.md#NonzeroIndicesTest_UnboundedDynamicCacheServesKernel_Test.TestBody), [`TestBody`](../eager/materialize_test.cc.md#MaterializeTest_CompilerOptionsPropagateToMaterializeThread_Test.TestBody), [`UnboundedDynamicCache`](compilation_cache.h.md#CompilationCache.UnboundedDynamicCache), [`GetOrCompileImpl`](compilation_cache.cc.md#CompilationCache.GetOrCompileImpl), [`ExecuteCompiledModelImpl`](../internal/compile/compiled_mode.cc.md#ExecuteCompiledModelImpl)  (+183 more)

## Functions
- `operator==(const BoundedDynamicDimension& lhs, const BoundedDynamicDimension& rhs)` — [`L41`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L41)
- <a id="operator"></a>`operator==(const Shape& lhs, const Shape& rhs)` — [`L86`](../../../../../../raw/code/torch_tpu/csrc/common/shape.h#L86)

